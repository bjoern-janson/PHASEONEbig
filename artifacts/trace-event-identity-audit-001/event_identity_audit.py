from pathlib import Path
import csv, io, json, re, hashlib, zipfile
import numpy as np
import pandas as pd
from scipy import sparse

ROOT=Path('/mnt/data/trace_groundup/data/cea2_pretrained_runtime_data')
CA=Path('/mnt/data/trace_groundup/cache4096')
BUILD=Path('/mnt/data/trace_groundup/groundup_001_build')
ZIP=Path('/mnt/data/train_transcripts(1).zip')
OUT=Path('/mnt/data/trace_groundup/EVENT_IDENTITY_AUDIT.json')
REPORT=Path('/mnt/data/trace_groundup/EVENT_IDENTITY_AUDIT.md')
PREREG=Path('/mnt/data/trace_groundup/EVENT_IDENTITY_AUDIT_PREREG.md')
EPS=1e-6
RAW=['n_turns','stu_turns','stu_words','stu_chars','stu_questions','stu_num','stu_numonly','tut_turns','tut_words','tut_chars','tut_questions','tut_num','tut_numonly']
STOP=set('''a an and are as at be been being but by can could did do does doing for from had has have having he her hers him his how i if in into is it its may me might my no not of on or our ours she should so some such than that the their theirs them then there these they this those to too under up us very was we what when where which who why will with would you your yours use using find finding give giving make making know knowing understand understanding identify identifying determine determining calculate calculating solve solving work working read reading write writing compare comparing order ordering represent representing see seeing'''.split())
RX=re.compile(r'[a-z0-9]+')

FORMS=['add_sub','mult_div','fraction_ratio','decimal','comparison_order','money','geometry']
CANDS=['student_event_identity_alignment','tutor_event_identity_alignment']+[f'student_{f}_alignment' for f in FORMS]

# Objective demand patterns: fixed before outcome inspection.
OBJ_PATTERNS={
    'add_sub': re.compile(r'add|subtract|\bsum\b|difference',re.I),
    'mult_div': re.compile(r'multip|divid|division|times table|sharing|grouping',re.I),
    'fraction_ratio': re.compile(r'fraction|ratio|mixed number',re.I),
    'decimal': re.compile(r'decimal',re.I),
    'comparison_order': re.compile(r'compar|order|greater|less|ascending|descending|inequal',re.I),
    'money': re.compile(r'money|cost|change|pound|£|currency',re.I),
    'geometry': re.compile(r'angle|degree|triangle|polygon|shape|area|perimeter|circle|geometry',re.I),
}

# Target-independent transcript event identity rules.
# They are applied once per turn before any objective is supplied.
TURN_RULES={
    'add_sub': [
        re.compile(r'\bplus\b|\bminus\b|\badd(?:ed|ing|ition)?\b|\bsubtract(?:ed|ing|ion)?\b|\bdifference\b|take\s+away',re.I),
        re.compile(r'\d\s*[+]\s*\d'),
        re.compile(r'\d\s*[-−]\s*\d'),
    ],
    'mult_div': [
        re.compile(r'\btimes\b|\bmultip(?:ly|lied|lying|lication)?\b|\bdivid(?:e|ed|ing)?\b|\bdivision\b|\bquotient\b|\bproduct\b|\bshared\b|groups?\s+of',re.I),
        re.compile(r'\d\s*[×*]\s*\d'),
        re.compile(r'\d\s*[÷]\s*\d'),
    ],
    'fraction_ratio': [
        re.compile(r'\bfraction\b|\bnumerator\b|\bdenominator\b|\bratio\b|\bhalf\b|\bquarter\b',re.I),
        re.compile(r'\b\d+\s*/\s*\d+\b'),
        re.compile(r'\b\d+\s*:\s*\d+\b'),
    ],
    'decimal': [
        re.compile(r'\bdecimal\b',re.I),
        re.compile(r'\b\d+\.\d+\b'),
        re.compile(r'\b\d+\s+point\s+\d+',re.I),
    ],
    'comparison_order': [
        re.compile(r'\bgreater\b|\bless\b|\bbigger\b|\bsmaller\b|\bascending\b|\bdescending\b|\bcompare\b|\bcomparison\b|\border(?:ed|ing)?\b',re.I),
        re.compile(r'[<>]'),
    ],
    'money': [
        re.compile(r'[£$€]'),
        re.compile(r'\bpounds?\b|\bpence\b|\bpenny\b|\bmoney\b|\bcost(?:s|ing)?\b|\bchange\b',re.I),
    ],
    'geometry': [
        re.compile(r'\bangle\b|\bdegrees?\b|\btriangle\b|\bshape\b|\barea\b|\bperimeter\b',re.I),
        re.compile(r'°'),
    ],
}

def terms(x):
    return set(t for t in RX.findall(str(x).lower()) if len(t)>=3 and t not in STOP)

def sig(x):
    x=np.asarray(x,float); return 1/(1+np.exp(-np.clip(x,-40,40)))

def frozen_state_and_c2():
    F=pd.read_csv(ROOT/'train_features.csv').merge(pd.read_csv(ROOT/'train_labels.csv'),on='response_id',validate='one_to_one')
    y=F.is_correct.astype(int).to_numpy(); sess=F.session_id.astype(str).to_numpy(); oid=F.learning_objective_id.astype(str).to_numpy()
    sy=pd.DataFrame({'s':sess,'y':y}).groupby('s').y.agg(['min','max']); mixed=set(sy[(sy['min']==0)&(sy['max']==1)].index); idx=np.where(np.isin(sess,list(mixed)))[0]
    S=pd.read_csv(ROOT/'session_features.csv',usecols=['session_id']+RAW+['student_tail','tutor_tail']).drop_duplicates('session_id').reset_index(drop=True)
    S[['student_tail','tutor_tail']]=S[['student_tail','tutor_tail']].fillna('')
    sm={str(s):i for i,s in enumerate(S.session_id)}; rs=np.array([sm[str(s)] for s in sess],np.int32)
    O=pd.read_csv(CA/'objectives.csv'); om={str(o):i for i,o in enumerate(O.learning_objective_id)}; ro=np.array([om[str(o)] for o in oid],np.int32)
    Xs=sparse.load_npz(CA/'Xs.npz'); Xt=sparse.load_npz(CA/'Xt.npz'); Xo=sparse.load_npz(CA/'Xo.npz')
    CFG=json.loads((BUILD/'model.json').read_text()); M=np.load(BUILD/'model.npz'); c=M['coef']; k=0
    R=np.log1p(np.maximum(S[RAW].fillna(0).to_numpy(float),0)); Rz=((R-M['scaler_mean'])/np.where(M['scaler_scale']==0,1,M['scaler_scale'])).astype(np.float32)
    rates=CFG['objective_rates']; G=float(CFG['global_rate']); ps=np.array([float(rates.get(str(oid[i]),G)) for i in idx]); ps=np.clip(ps,EPS,1-EPS)
    score=np.log(ps/(1-ps))*c[k]; k+=1
    score+=Rz[rs[idx]]@c[k:k+len(RAW)]; k+=len(RAW)
    score+=np.asarray(Xs[rs[idx]].dot(c[k:k+4096])).ravel(); k+=4096
    score+=np.asarray(Xt[rs[idx]].dot(c[k:k+4096])).ravel(); k+=4096
    score+=np.asarray(Xo[ro[idx]].dot(c[k:k+4096])).ravel()+float(M['intercept'][0])
    p=sig(score)
    Sx=S[S.session_id.astype(str).isin(mixed)].copy()
    st={str(r.session_id):terms(r.student_tail) for r in Sx.itertuples()}; tt={str(r.session_id):terms(r.tutor_tail) for r in Sx.itertuples()}
    ot={str(a):terms(b) for a,b in F[['learning_objective_id','learning_objective']].drop_duplicates().itertuples(index=False)}
    rec={}
    for ii,pred in zip(idx,p):
        s=sess[ii]; o=oid[ii]; q=ot[o]; d=len(q)
        if d:
            a=q&st[s]; b=q&tt[s]
            vals={'r':len(a|b)/d,'student_cov':len(a)/d,'tutor_cov':len(b)/d}
        else:
            vals={'r':0.0,'student_cov':0.0,'tutor_cov':0.0}
        vals.update({'y':int(y[ii]),'p':float(pred),'s':s,'o':o,'objective':str(F.iloc[ii].learning_objective)})
        rec[int(ii)]=vals
    D=pd.DataFrame([{'i':i,**v} for i,v in rec.items()])
    pairs=[]
    for s,g in D.groupby('s'):
        for a in g[g.y==1].itertuples():
            for b in g[g.y==0].itertuples():
                pairs.append((s,int(a.i),int(b.i),abs(a.p-b.p),abs(a.r-b.r),abs(a.student_cov-b.student_cov),abs(a.tutor_cov-b.tutor_cov)))
    P=pd.DataFrame(pairs,columns=['s','pos','neg','dp','dr','dsc','dtc'])
    C2=P[(P.dr<=1e-12)&(P.dsc<=1e-12)&(P.dtc<=1e-12)&(P.dp<=.05)].copy()
    return rec,C2

def split_tag(s):
    h=int(hashlib.sha256(str(s).encode()).hexdigest()[:16],16)
    return 'discovery' if h%2==0 else 'confirmation'

def objective_demands(text):
    return {f:bool(OBJ_PATTERNS[f].search(str(text))) for f in FORMS}

def turn_labels(content):
    text=str(content)
    return {f:any(rx.search(text) for rx in TURN_RULES[f]) for f in FORMS}

def transcript_rates(session_ids):
    wanted=set(str(s) for s in session_ids); out={}
    with zipfile.ZipFile(ZIP) as z:
        names={Path(n).stem:n for n in z.namelist() if n.endswith('.csv')}
        missing=wanted-set(names)
        if missing: raise RuntimeError(f'missing transcript sessions: {len(missing)}')
        for s in wanted:
            text=z.read(names[s]).decode('utf-8-sig',errors='replace')
            counts={'student':{f:0 for f in FORMS},'tutor':{f:0 for f in FORMS}}
            nrole={'student':0,'tutor':0}
            for r in csv.DictReader(io.StringIO(text)):
                role=(r.get('role') or '').strip().lower(); content=(r.get('content') or '').strip()
                if role not in ('student','tutor') or not content: continue
                nrole[role]+=1
                lab=turn_labels(content)
                for f,v in lab.items(): counts[role][f]+=int(v)
            rates={}
            for role in ('student','tutor'):
                den=max(1,nrole[role])
                rates[role]={f:counts[role][f]/den for f in FORMS}
            out[s]={'rates':rates,'nrole':nrole,'counts':counts}
    return out

def centered_means(C,TR,role):
    sessions=sorted(C.s.unique())
    return {f:float(np.mean([TR[s]['rates'][role][f] for s in sessions])) for f in FORMS}

def candidate_values(C,rec,TR):
    # Centering is outcome-blind and split-specific, per preregistration.
    mus={role:centered_means(C,TR,role) for role in ('student','tutor')}
    ids=set(C.pos)|set(C.neg)
    vals={}
    for i in ids:
        rr=rec[i]; s=rr['s']; dem=objective_demands(rr['objective'])
        out={}
        for role in ('student','tutor'):
            active=[f for f in FORMS if dem[f]]
            out[f'{role}_event_identity_alignment']=(
                float(np.mean([TR[s]['rates'][role][f]-mus[role][f] for f in active])) if active else 0.0
            )
        for f in FORMS:
            out[f'student_{f}_alignment']=float(dem[f])*(TR[s]['rates']['student'][f]-mus['student'][f])
        vals[i]=out
    return vals,mus

def signflip_p(sd,rng,n_draws=50000):
    sd=np.asarray(sd,float)
    if len(sd)==0:return 1.0
    obs=abs(sd.mean()); ge=0; done=0
    while done<n_draws:
        m=min(5000,n_draws-done)
        signs=rng.choice(np.array([-1.,1.]),size=(m,len(sd)))
        ge += int((np.abs((signs*sd).mean(axis=1))>=obs-1e-15).sum()); done+=m
    return float((ge+1)/(n_draws+1))

def holm_adjust(ps):
    ps=np.asarray(ps,float); m=len(ps); order=np.argsort(ps); adj=np.empty(m,float); running=0.0
    for rank,idx in enumerate(order):
        running=max(running,(m-rank)*ps[idx]); adj[idx]=min(1.0,running)
    return adj

def summarize(C,vals,seed):
    raw=[]
    for ci,col in enumerate(CANDS):
        d=np.array([vals[a][col]-vals[b][col] for a,b in zip(C.pos,C.neg)],float)
        x=pd.DataFrame({'s':C.s.to_numpy(),'d':d}); sd=x.groupby('s').d.mean().to_numpy()
        rng=np.random.default_rng(seed+1009*ci)
        if len(sd):
            idxb=rng.integers(0,len(sd),size=(10000,len(sd))); boots=sd[idxb].mean(axis=1)
            ci95=[float(np.quantile(boots,.025)),float(np.quantile(boots,.975))]
            p=signflip_p(sd,rng,50000)
        else: ci95=[0.0,0.0];p=1.0
        raw.append({
            'candidate':col,'n_pairs':int(len(d)),'n_sessions':int(len(sd)),
            'mean_pair_diff':float(d.mean()) if len(d) else 0.0,
            'mean_session_diff':float(sd.mean()) if len(sd) else 0.0,
            'median_pair_diff':float(np.median(d)) if len(d) else 0.0,
            'positive_pair_fraction':float((d>0).mean()) if len(d) else 0.0,
            'negative_pair_fraction':float((d<0).mean()) if len(d) else 0.0,
            'zero_pair_fraction':float((d==0).mean()) if len(d) else 1.0,
            'bootstrap95_session_mean':ci95,'signflip_p_raw':p,
        })
    adj=holm_adjust([r['signflip_p_raw'] for r in raw])
    for r,a in zip(raw,adj):r['signflip_p_holm']=float(a)
    return raw

def support_counts(C2,rec):
    out={}
    for f in FORMS:
        diff=0; either=0
        for r in C2.itertuples():
            a=objective_demands(rec[r.pos]['objective'])[f]; b=objective_demands(rec[r.neg]['objective'])[f]
            diff+=int(a!=b); either+=int(a or b)
        out[f]={'paired_objective_demand_diff_count':diff,'either_objective_demands_count':either}
    return out

rec,C2=frozen_state_and_c2(); C2['split']=[split_tag(s) for s in C2.s]
disc=C2[C2.split=='discovery'].copy(); conf=C2[C2.split=='confirmation'].copy()
TR=transcript_rates(C2.s.unique())
dvals,dmu=candidate_values(disc,rec,TR); cvals,cmu=candidate_values(conf,rec,TR)
dres=summarize(disc,dvals,2026082703); cres=summarize(conf,cvals,2026082704)
D={r['candidate']:r for r in dres}; C={r['candidate']:r for r in cres}
est=[]; rows=[]
for col in CANDS:
    d=D[col]; c=C[col]
    same=np.sign(d['mean_session_diff'])==np.sign(c['mean_session_diff']) and np.sign(d['mean_session_diff'])!=0
    ok=(d['signflip_p_holm']<.05 and c['signflip_p_holm']<.05 and same)
    if ok:est.append(col)
    rows.append({'candidate':col,'discovery':d,'confirmation':c,'status':'ESTABLISHED' if ok else 'NOT ESTABLISHED'})

out={
    'status':'DISTINGUISH_ONLY_NO_MODEL',
    'audit':'EVENT_IDENTITY_AUDIT_001',
    'prereg_sha256':hashlib.sha256(PREREG.read_bytes()).hexdigest(),
    'incumbent':'Groundup-001 / #20 immutable','search_state_entering':'K4',
    'event_constitution':'Target-independent turn-level mathematical-act labels; objective demand labels constituted separately; no target-objective/turn token-overlap predicate.',
    'forms':FORMS,'support_counts_outcome_blind':support_counts(C2,rec),
    'population':{'pairs':int(len(C2)),'sessions':int(C2.s.nunique()),'discovery_pairs':int(len(disc)),'discovery_sessions':int(disc.s.nunique()),'confirmation_pairs':int(len(conf)),'confirmation_sessions':int(conf.s.nunique())},
    'split_centering_means':{'discovery':dmu,'confirmation':cmu},
    'family':CANDS,
    'multiplicity':'Holm correction across all 9 candidates separately within discovery and confirmation; session-level two-sided sign-flip p-values.',
    'authorization_rule':'ESTABLISHED only if discovery Holm p<0.05 AND confirmation Holm p<0.05 AND same nonzero sign. No model fit.',
    'results':rows,'established_D2':est,
    'next_state':'D2 identified; separate TRANSFORM experiment may be constituted' if est else 'No D2 authorized; R0 remains frozen and K4 advances to K5 with this negative event-identity family result',
    'claim_boundary':'A negative result rejects only this primitive target-independent mathematical-act event constitution, not event identity or semantics generally.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')

# Compact human report
lines=[]
lines.append('# EVENT_IDENTITY_AUDIT_001 — result\n')
lines.append('**Mode:** DISTINGUISH only / no predictor / no Groundup-002\n')
lines.append(f"**Preregistration SHA-256:** `{out['prereg_sha256']}`\n")
lines.append('## Question\n')
lines.append('Does a target-independent mathematical-act identity of transcript turns reproducibly separate the hardest residual futures when aligned only at the predeclared act-category level to the target objective?\n')
lines.append('This audit does not use the failed `terms(objective) ∩ terms(turn)` relevance predicate.\n')
lines.append('## Population\n')
lines.append(f"- C2: {len(C2)} pairs / {C2.s.nunique()} sessions\n- discovery: {len(disc)} pairs / {disc.s.nunique()} sessions\n- confirmation: {len(conf)} pairs / {conf.s.nunique()} sessions\n")
lines.append('## Results\n')
lines.append('| candidate | discovery Δ_session | disc 95% CI | disc Holm p | confirmation Δ_session | conf 95% CI | conf Holm p | status |\n|---|---:|---:|---:|---:|---:|---:|---|')
for r in rows:
    d=r['discovery']; c=r['confirmation']
    lines.append(f"| `{r['candidate']}` | {d['mean_session_diff']:+.6f} | [{d['bootstrap95_session_mean'][0]:+.6f}, {d['bootstrap95_session_mean'][1]:+.6f}] | {d['signflip_p_holm']:.6g} | {c['mean_session_diff']:+.6f} | [{c['bootstrap95_session_mean'][0]:+.6f}, {c['bootstrap95_session_mean'][1]:+.6f}] | {c['signflip_p_holm']:.6g} | **{r['status']}** |")
lines.append('\n## Decision\n')
if est:
    lines.append('At least one predeclared event-identity dependency met the discovery + confirmation authorization rule:\n')
    for x in est: lines.append(f'- `{x}`')
    lines.append('\n`D2` is constituted for this family, but **no transformation occurs in this audit**.\n')
else:
    lines.append('No member of the preregistered family met the authorization rule.\n\n```math\n\\boxed{(R_0,K_4)\\rightarrow(R_0,K_5)}\n```\n\nGroundup-001 remains frozen. No `D2`, `M2`, or Groundup-002 is authorized.\n')
lines.append('\n## Claim boundary\n')
lines.append('A negative result means only that this primitive, target-independent mathematical-act event constitution did not reproducibly distinguish C2. It does **not** show that event identity, semantics, or the session-objective dependency is irrelevant.\n')
REPORT.write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps(out,indent=2))
