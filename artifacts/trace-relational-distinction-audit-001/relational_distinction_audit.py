from pathlib import Path
import csv, io, json, re, hashlib, zipfile
import numpy as np
import pandas as pd
from scipy import sparse

ROOT=Path('/mnt/data/trace_groundup/data/cea2_pretrained_runtime_data')
CA=Path('/mnt/data/trace_groundup/cache4096')
BUILD=Path('/mnt/data/trace_groundup/groundup_001_build')
ZIP=Path('/mnt/data/train_transcripts(1).zip')
OUT=Path('/mnt/data/trace_groundup/RELATIONAL_DISTINCTION_AUDIT.json')
PREREG=Path('/mnt/data/trace_groundup/RELATIONAL_DISTINCTION_AUDIT_PREREG.md')
EPS=1e-6
RAW=['n_turns','stu_turns','stu_words','stu_chars','stu_questions','stu_num','stu_numonly','tut_turns','tut_words','tut_chars','tut_questions','tt_num','tut_numonly']
STOP=set('''a an and are as at be been being but by can could did do does doing for from had has have having he her hers him his how i if in into is it its may me might my no not of on or our ours she should so some such than that the their theirs them then there these they this those to too under up us very was we what when where which who why will with would you your yours use using find finding give giving make making know knowing understand understanding identify identifying determine determining calculate calculating solve solving work working read reading write writing compare comparing order ordering represent representing see seeing'''.split())
RX=re.compile(r'[a-z0-9]+')
COLS=[
    'student_rel_question_to_tutor_rel_response',
    'tutor_rel_question_to_student_rel_response',
    'student_return_after_tutor_rel_contrast',
    'student_entry_after_tutor_rel_contrast',
    'cross_role_relevant_adjacency_density',
    'relevance_segment_fragmentation',
    'student_to_tutor_relevant_proximity',
    'tutor_to_student_relevant_proximity',
]

def terms(x):
    return set(t for t in RX.findall(str(x).lower()) if len(t)>=3 and t not in STOP)

def sig(x):
    x=np.asarray(x,float); return 1/(1+nl.exp(-np.clip(x,-40,40)))

def frozen_state_and_c2():
    F=pd.read_csv(ROOT/'train_features.csv').merge(pd.read_csv(ROOT/'train_labels.csv'),on='response_id',validate='one_to_one')
    y=F.is_correct.astype(int).to_numpy(); sess=F.session_id.astype(str).to_numpy(); oid=F.learning_objective_id.astype(str).to_numpy()
    sy=pd.DataFrame({'s':sess,'y':y}).groupby('s').y.agg(X'min','max']); mixed=set(sy[(sy['min']==0)&(sy['max']==1)].index); idx=np.where(np.isin(sess,list(mixed)))[0]
    S=pd.read_csv(ROOT/'session_features.csv',usecols=['session_id']+RAW+['student_tail','tutor_tail']).drop_duplicates('session_id').reset_index(drop=True)
    S[['student_tail','tutor_tail']]=S[['student_tail','tutor_tail']].fillna('')
    sm={str(s):i for i,s in enumerate(S.session_id)}; rs=np.array([sm[str(s)] for s in sess],np.int32)
    O=pd.read_csv(CA/'objectives.csv'); om={str(o):i for i,o in enumerate(O.learning_objective_id)}; ro=np.array([om[str(o)] for o in oid],np.int32)
    Xs=sparse.load_npz(CA/'Xs.npz'); Xt=sparse.load_npz(CA/'Xt.npz'); Xo=sparse.load_npz(CA/'Xo.npz')
    CFG=json.loads((BUILD/'model.json').read_text()); M=np.load(BUILD/'model.npz'); c=M['coef']; k=0
    R=np.log1p(np.maximum(S[RAW].fillna(0).to_numpy(float),0)); Rz
=((R-M['scaler_mean'])/np.where(M['scaler_scale']==0,1,M['scaler_scale'])).astype(np.float32)
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

def transcript_map(session_ids):
    wanted=set(str(s) for s in session_ids); out={}
    with zipfile.ZipFile(ZIP) as z:
        names={Path(n).stem:n for n in z.namelist() if n.endswith('.csv')}
        missing=wanted-set(names)
        if missing: raise RuntimeError(f'missing transcript sessions: {len(missing)}')
        for s in wanted:
            text=z.read(names[s]).decode('utf-8-sig',errors='replace')
            rows=[]
            for r in csv.DictReader(io.StringIO(text)):
                role=(r.get('role') or '').strip().lower(); content=(r.get('content') or '').strip()
                if role in ('student','tutor') and content:
                    rows.append({'role':role,'terms':terms(content),'question':'?' in content})
            out[s]=rows
    return out

def mean_or_zero(xs):
    return float(np.mean(xs)) if xs else 0.0

def relation_values(rows,q):
    ev=[{'role':r['role'],'rel':bool(r['terms']&q),'question':r['question']} for r in rows]
    n=len(ev)
    # 1/2: relevant question -> immediately following other-role relevant response
    sq=[]; tq=[]
    for i in range(n-1):
        a,b=ev[i],ev[i+1]
        if a['role']=='student' and a['rel'] and a['question'] and b['role']=='tutor': sq.append(float(b['rel']))
        if a['role']=='tutor' and a['rel'] and a['question'] and b['role']=='student': tq.append(float(b['rel']))
    # 3/4: S-T-S triplet return / entry contrast by tutor relevance
    ret_yes=[]; ret_no=[]; ent_yes=[]; ent_no=[]
    for i in range(n-2):
        a,b,c=ev[i],ev[i+1],ev[i+2]
        if (a['role'],b['role'],c['role'])!=('student','tutor','student'): continue
        target=ret_yes if (a['rel'] and b['rel']) else ret_no if (a['rel'] and not b['rel']) else ent_yes if ((not a['rel']) and b['rel']) else ent_no
        target.append(float(c['rel']))
    def contrast(yes,no):
        return float(np.mean(yes)-np.mean(no)) if yes and no else 0.0
    # 5: cross-role adjacency where both are relevant
    cross=[]
    for i in range(n-1):
        a,b=ev[i],ev[i+1]
        if a['role']!=b['role']:
            cross.append(float(a['rel'] and b['rel']))
    # 6: relevant-segment fragmentation
    rel=[e['rel'] for e in ev]
    nrel=sum(rel)
    seg=0
    prev=False
    for x in rel:
        if x and not prev: seg+=1
        prev=x
    frag=(seg/nrel) if nrel else 0.0
    # 7/8: directional proximity to next later relevant other-role event
    def proximity(src_role,dst_role):
        src=[i for i,e in enumerate(ev) if e['role']==src_role and e['rel']]
        vals=[]
        for i in src:
            js=[j for j in range(i+1,n) if ev[j]['role']==dst_role and ev[j]['rel']]
            vals.append(1.0/(1.0+(js[0]-i)) if js else 0.0)
        return mean_or_zero(vals)
    return {
        COLS[0]:mean_or_zero(sq),
        COLS[1]:mean_or_zero(tq),
        COLS[2]:contrast(ret_yes,ret_no),
        COLS[3]:contrast(ent_yes,ent_no),
        COLS[4]:mean_or_zero(cross),
        COLS[5]:float(frag),
        COLS[6]:proximity('student','tutor'),
        COLS[7]:proximity('tutor','student'),
    }

def split_tag(s):
    h=int(hashlib.sha256(str(s).encode()).hexdigest()[:16],16)
    return 'discovery' if h%2==0 else 'confirmation'

def signflip_p(sd,rng,n_draws=50000):
    sd=np.asarray(sd,float)
    if len(sd)==0: return 1.0
    obs=abs(sd.mean())
    ge=0; done=0; chunk=5000
    while done<n_draws:
        m=min(chunk,n_draws-done)
        signs=rng.choice(np.array([-1.0,1.0]),size=(m,len(sd)))
        means=np.abs((signs*sd).mean(axis=1))
        ge += int((means>=obs-1e-15).sum())
        done += m
    return float((ge+1)/(n_draws+1))

def holm_adjust(ps):
    ps=np.asarray(ps,float); m=len(ps); order=np.argsort(ps); adj=np.empty(m,float); running=0.0
    for rank,idx in enumerate(order):
        val=(m-rank)*ps[idx]
        running=max(running,val)
        adj[idx]=min(1.0,running)
    return adj

def summarize(C,vals,cols,split_seed):
    raw=[]
    for ci,col in enumerate(cols):
        d=np.array([vals[a][col]-vals[b][col] for a,b in zip(C.pos,C.neg)],float)
        x=pd.DataFrame({'s':C.s.to_numpy(),'d':d}); sd=x.groupby('s').d.mean().to_numpy()
        rng=np.random.default_rng(split_seed+1009*ci)
        if len(sd):
            boots=np.array([rng.choice(sd,len(sd),replace=True).mean() for _ in range(10000)])
            ci95=[float(np.quantile(boots,.025)),float(np.quantile(boots,.975))]
            p=signflip_p(sd,rng,50000)
        else:
            ci95=[0.0,0.0]; p=1.0
        raw.append({
            'candidate':col,'n_pairs':int(len(d)),'n_sessions':int(len(sd)),
            'mean_pair_diff':float(d.mean()) if len(d) else 0.0,
            'mean_session_diff':float(sd.mean()) if len(sd) else 0.0,
            'median_pair_diff':float(np.median(d)) if len(d) else 0.0,
            'positive_pair_fraction':float((d>0).mean()) if len(d) else 0.0,
            'negative_pair_fraction':float((d<0).mean()) if len(d) else 0.0,
            'zero_pair_fraction':float((d==0).mean()) if len(d) else 1.0,
            'bootstrap95_session_mean':ci95,
            'signflip_p_raw':p,
        })
    adj=holm_adjust([r['signflip_p_raw'] for r in raw])
    for r,a in zip(raw,adj): r['signflip_p_holm']=float(a)
    return raw

rec,C2=frozen_state_and_c2()
TR=transcript_map(C2.s.unique())
vals={}
for i in set(C2.pos)|set(C2.neg):
    vals[i]=relation_values(TR[rec[i]['s']],terms(rec[i]['objective']))
C2['split']=[split_tag(s) for s in C2.s]
disc=C2[C2.split=='discovery'].copy(); conf=C2[C2.split=='confirmation'].copy()
dres=summarize(disc,vals,COLS,2026082701); cres=summarize(conf,vals,COLS,2026082702)
D={r['candidate']:r for r in dres}; C={r['candidate']:r for r in cres}
est=[]
for col in COLS:
    d=D[col]; c=C[col]
    same=np.sign(d['mean_session_diff'])==np.sign(c['mean_session_diff']) and np.sign(d['mean_session_diff'])!=0
    ok=(d['signflip_p_holm']<0.05 and c['signflip_p_holm']<0.05 and same)
    if ok: est.append(col)
rows=[]
for col in COLS:
    rows.append({'candidate':col,'discovery':D[col],'confirmation':C[col],
                 'status':'ESTABLISHED' if col in est else 'NOT ESTABLISHED'})
out={
    'status':'DISTINGUISH_ONLY_NO_MODEL',
    'prereg_sha256':hashlib.sha256(PREREG.read_bytes()).hexdigest(),
    'incumbent':'Groundup-001 / #20 immutable',
    'search_state_entering':'K3',
    'C2_definition':{'same_session':True,'opposite_outcome':True,'exact_combined_lexical_coverage_tie':True,'exact_student_lexical_coverage_tie':True,'exact_tutor_lexical_coverage_tie':True,'frozen_R0_probability_abs_diff_max':0.05},
    'population':{'pairs':int(len(C2)),'sessions':int(C2.s.nunique()),'discovery_pairs':int(len(disc)),'discovery_sessions':int(disc.s.nunique()),'confirmation_pairs':int(len(conf)),'confirmation_sessions':int(conf.s.nunique())},
    'family':COLS,
    'multiplicity':'Holm correction across all 8 relations separately within discovery and confirmation; session-level two-sided sign-flip p-values.',
    'authorization_rule':'ESTABLISHED only if discovery Holm p<0.05 AND confirmation Holm p<0.05 AND same nonzero sign. No model fit.',
    'results':rows,
    'established_D2':est,
    'next_state':'D2 identified; separate TRANSFORM experiment may be constituted' if est else 'No D2 authorized; R0 remains frozen and K3 may advance to K4 with this negative family result',
    'claim_boundary':'Observational diagnostic inside C2. Does not itself establish positive C_improve.'
}
OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
