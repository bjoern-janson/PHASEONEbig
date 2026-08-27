# LIVE STATE — recovery spine

**Status:** authoritative persistence checkpoint for the live research state after the Trace proving-ground and adaptive-loop protocol/conformance work of 2026-08-27.

Read this file first if conversational state is lost.

The program center remains deliberately small:

```math
\boxed{I_{\rm adaptive}\propto C_{\rm improve}}
```

with realized future contribution judged against the matched alternative, and the developmental loop:

```math
\boxed{\text{distinguish}\rightarrow\text{transform}\rightarrow\text{reconstitute}\rightarrow\text{continue}\rightarrow\text{distinguish better}}
```

The key methodological realization from the proving ground is:

> **A failed transformation may leave the operative representation unchanged while still improving the research/search state.**

Equivalently:

```math
(R_i,K_i)\rightarrow(R_i,K_{i+1})
```

is a legitimate adaptive transition when the evidence changes what distinctions are justified next.

---

## 1. Trace the Ace incumbent

The authoritative predictive state is still:

```text
R0 = Groundup-001 / leaderboard #20
LL = 0.6020
AUC = 0.6274
```

No Groundup-002 has earned inheritance.

The proving-ground rule is:

> **Do not search feature space. Search the equivalence classes imposed by the current representation.**

Before any successor is allowed to exist, identify a future-relevant distinction or dependency the incumbent cannot express, then test the smallest representation of that distinction against an independent future.

A failed representation must not justify itself by becoming more complicated.

---

## 2. Trace search-state lineage: K0 -> K3

### K0: temporal-prefix hypothesis — rejected

Groundup-001 constructs one session representation and reuses it for all response targets in the session. This initially suggested prediction-time temporal aliasing.

The data contract did not support that interpretation: the target assessment occurs after the completed tutoring session, and the participant feature table exposes no response-specific transcript cutoff/prefix field.

**Earned result:** distinct response-time transcript prefixes within one session are **not established** as the relevant collision.

### K0 -> K1: session-objective structural collision

The stronger structural limitation is the additive form:

```math
f(s,o)=A(s)+B(o).
```

For two objectives in the same completed session:

```math
f(s,o_1)-f(s,o_2)=B(o_1)-B(o_2),
```

so all transcript/session evidence cancels. Groundup-001 cannot represent:

> this completed conversation is stronger evidence for objective `o1` than for objective `o2`.

Training geometry supporting investigation of this dependency:

- 35,072 response rows / 22,821 sessions;
- 8,364 sessions have multiple target objectives;
- 3,207 multi-target sessions contain both correct and incorrect objective outcomes;
- those mixed sessions contain 8,296 responses.

A diagnostic lexical relation showed modest within-session association, but this did **not** authorize a model.

### K1: lexical session-objective measurement 001 — killed

Scientific distinction remained broad:

```text
D_objective<->dialogue = how much the completed conversation bears on this target objective
```

First measurement implementation only:

```text
r(s,o) = fraction of retained objective terms present in Groundup-001's observed dialogue text
```

Frozen decision path:

- development seed 13: `LL 0.550809272097 -> 0.550803031202`, `C_improve = +0.000006240895`;
- fresh session seed 73: `LL 0.546514352689 -> 0.546502745953`, `C_improve = +0.000011606736`;
- cold-objective seed 52: `LL 0.616042026063 -> 0.616099755564`, `C_improve = -0.000057729501`;
- cold-objective AUC also worsened: `0.605609208 -> 0.605362925`.

**Decision:** kill lexical-support measurement 001. No tuning, no rescue, no submission.

Important distinction:

```math
\boxed{\text{candidate relation identified}\neq\text{candidate relation successfully represented}}
```

The broader session-objective dependency remained open.

### K1 -> K2: residual-collision role audit — no surviving distinction established

Residual collisions were defined among opposite-outcome objective pairs in the same session with equal failed combined lexical support and near-equal frozen Groundup-001 predictions.

Population:

- 238 residual pairs;
- 226 sessions.

Primitive student/tutor decompositions all had bootstrap intervals crossing zero. Examples:

- both student+tutor support: mean contrast `+0.02913`, CI `[-0.00495,+0.06417]`;
- student coverage: `+0.02400`, CI `[-0.01063,+0.06025]`;
- tutor coverage: `+0.00513`, CI `[-0.02194,+0.03234]`;
- student-tutor balance: `+0.01888`, CI `[-0.03252,+0.07098]`.

**Earned result:** the failed combined lexical measurement cannot be repaired merely by splitting lexical support into marginal student/tutor channels.

No successor model authorized.

### K2 -> K3: relational-collision audit — no D2 authorized

A stricter hard residual class required:

- same completed session;
- opposite objective outcomes;
- exact tie in combined lexical coverage;
- exact tie in student lexical coverage;
- exact tie in tutor lexical coverage;
- frozen Groundup-001 probability difference <= 0.05.

Population:

- 163 pairs / 157 sessions;
- discovery: 73 pairs / 70 sessions;
- confirmation: 90 pairs / 87 sessions.

Four predeclared primitive relations were tested without fitting a successor model:

1. student -> tutor conditional objective-relevant response;
2. tutor -> student conditional objective-relevant response;
3. tutor-leading lexical transfer;
4. student-leading lexical transfer.

None satisfied the authorization rule requiring discovery and confirmation 95% intervals to exclude zero with the same sign.

Strongest-looking result, student-leading transfer:

- discovery mean `+0.052857`, CI `[-0.026917,+0.130958]`;
- confirmation mean `+0.026820`, CI `[-0.039464,+0.093678]`.

**Decision:** no `D2`, no `M2`, no Groundup-002.

Current Trace search state:

```text
R0 = Groundup-001 / #20    (frozen)
K3 = temporal-prefix rejected
     + session-objective dependency remains structurally unresolved
     + combined lexical measurement killed for portability
     + marginal role decomposition not established
     + tested primitive lexical-order relations not established
D2 = not identified
M2 = not permitted
```

Next legal Trace operation remains **DISTINGUISH**, not TRANSFORM.

---

## 3. Boundary discipline learned from Trace

Boundary dissolution does not mean boundary erasure.

It means changing a factorization only when the factorization prevents a future-relevant joint relation from being represented.

Working taxonomy:

```text
artificial representational boundary -> candidate for dissolution
functional boundary                 -> preserve identities, permit interaction
causal/evidentiary boundary         -> protect
```

Operational rule:

```math
R_1=R_0\oplus J(X,Y)
```

and, for Trace where viability is negative log loss:

```math
C_{boundary}=LL(R_0)-LL(R_1).
```

A boundary does not earn dissolution because it explains development data. It earns dissolution only when an independently constituted future behaves as though the previous factorization was too rigid.

Compression:

> **Let reality choose the partition.**

---

## 4. Universal abstraction boundary

The correct abstraction is:

```math
\boxed{\text{universal code}\neq\text{universal intelligence architecture}}
```

and:

> **Universalize the survival protocol, not the intelligence mechanism.**

The universal transition grammar is:

```math
(R_i,K_i)\xrightarrow[\text{outside core}]{D_i,T_i}R_i'\xrightarrow[\text{domain-defined}]{F_i}C_i\xrightarrow[\text{fixed rule}]{\text{inherit/reject}}(R_{i+1},K_{i+1}).
```

The core may own only:

- incumbent/candidate identity;
- parentage;
- experiment identity;
- precommitted decision-rule identity;
- declared evaluation contract;
- consequence;
- inherit/reject;
- evaluated-transition knowledge update;
- provenance.

The domain owns:

- what `D` means;
- how `T` is constructed;
- what `F` means;
- how future independence is established;
- what viability `V` means;
- what minimal transformation means;
- how the next `D` is discovered.

The core records declared independence/minimality contracts. It does not prove them.

---

## 5. adaptive-loop-protocol-001 — frozen

Source is preserved under:

```text
artifacts/adaptive-loop-protocol-001/
```

Package SHA-256 from the original generated artifact:

```text
e6e8d0de03e8721b85dd27b1fd040b95388e619cf4c4e992da55144746265238
```

Earned claim ceiling:

> **PROTOCOL-001 can enforce the bookkeeping and survival conditions of an already-constituted adaptive transition without assuming the domain's ontology.**

It has not earned claims that these conditions are sufficient for intelligence, adaptation, corrigibility, causal identification, future independence, or useful improvement.

The key implemented failure branch is:

```math
C_i\le0\Rightarrow R_{i+1}=R_i
```

while an evaluated experiment still appends a knowledge event.

---

## 6. Two-domain conformance — passed narrowly

The unchanged protocol was instantiated in two different ontologies:

1. Trace the Ace predictive representation change;
2. symbolic program repair with executable programs and held-out behavioral tests.

Conformance artifact is preserved under:

```text
artifacts/adaptive-loop-conformance-001/
```

Original package SHA-256:

```text
30781bde1300b2322bb32437203e7d18d955298186ff03b71b8e7d8e0d4906b1
```

All 9 tests passed: 4 frozen protocol tests + 5 conformance tests.

### Trace positive branch

Objective-prior incumbent -> objective prior + 13 direct transcript-structure observables on fresh session seed 23:

```text
LL 0.5518725935510772 -> 0.5425176010683584
C_improve = +0.00935499248271876
INHERIT
```

Conformance evidence only; this does not mutate Groundup-001.

### Trace rejection branch

Frozen lexical candidate on cold-objective seed 52:

```text
LL 0.6160420260629641 -> 0.6160997555644535
C_improve = -0.000057729501489411916
REJECT
R remains Groundup-001
K appends evaluated failure event
```

### Symbolic repair positive branch

Specification: return 1 iff integer `x` is even.

Incumbent program always returns 0. Candidate adds parity predicate.

Held-out accuracy:

```text
0.5 -> 1.0
C_improve = +0.5
INHERIT
```

### Symbolic repair rejection branch

Candidate adds a sign predicate instead.

Held-out accuracy:

```text
0.5 -> 0.5
C_improve = 0.0
REJECT
incumbent program survives
K still appends evaluated failure event
```

**Conformance result:** the narrow survival-transition abstraction survived this ontology change without a protocol edit.

This does not establish universality.

---

## 7. Open pressure point: ownership/meaning of K

Conformance exposed one boundary and deliberately did not patch it.

In PROTOCOL-001, `State.knowledge` is an append-only tuple of `KnowledgeEvent`s produced by `reconstitute()` after a `Candidate + Consequence` transition.

Live Trace `K3`, however, also contains diagnostic-only changes such as residual-collision and relational-collision audits that changed the next research question **without producing a Candidate + Consequence transition**.

Two interpretations remain open:

1. **Narrow K:** core `K` means only the evaluated survival-transition ledger; broader search/research state lives outside the core.
2. **Full K:** core `K` is the entire research state; then PROTOCOL-001 cannot faithfully represent `K2 -> K3` without another primitive.

Do not create `protocol-002` merely to close this gap. Further cross-domain evidence must decide whether the gap is truly universal.

---

## 8. Persistence invariant discovered by self-application

The research process itself exposed a reconstitution failure: meaningful `R/K` transitions were allowed to live only in conversational working state for roughly two hours while GitHub remained stale.

That is unacceptable if `K` is supposed to preserve what future correction needs.

Going forward:

> **A meaningful change in authoritative operative state or correction-relevant research state is not reconstituted until its minimal recovery record is persisted outside the conversation.**

Do not dump scratch work. Persist correction-relevant lineage:

- what state was authoritative;
- what distinction/hypothesis was tested;
- what consequence occurred;
- what was inherited/rejected;
- what changed in the search state;
- what remains open;
- exact artifacts or sufficient source/provenance to reopen the result.

This repository is the durable research lineage unless/until a more appropriate persistent substrate is explicitly adopted.

---

## 9. Method / protocol / research-state separation

A program-level methodological clarification has been added without changing the conceptual core or PROTOCOL-001.

The three layers are:

```text
METHOD
    interrogate the object
    ↓
    constitute the next distinction/transformation

PROTOCOL
    expose candidate to a declared independent future
    ↓
    compute C_improve
    ↓
    inherit / reject

RESEARCH STATE
    preserve consequence
    ↓
    localize failure
    ↓
    change the next question
```

The methodological spine is:

```math
\boxed{\text{interrogate}\rightarrow\text{constitute}\rightarrow\text{transform}\rightarrow\text{independent future}\rightarrow C_{\rm improve}\rightarrow\text{inherit/reject}\rightarrow\text{revise the next question}}
```

This does **not** replace the original developmental loop. It is an operational discipline for entering and traversing it without granting optimization premature authority.

The deepest methodological rule is:

```math
\boxed{\textbf{Revision depth must match failure depth.}}
```

Distinguish at least:

```text
failure of execution      -> repair/simplify implementation
failure of representation -> abandon/reconsider that representation or measurement
failure of constitution   -> change the question/object; do not optimize it
```

Do not infer a deeper failure than the evidence warrants, and do not respond to a deep failure with shallow optimization.

Consequences improve the research process only when they change what questions or distinctions are admissible next. Merely logging failure without changing future search behavior is bookkeeping, not meaningful research adaptation.

A useful compression is:

> **A research system does not become more adaptive by accumulating more transformations. It becomes more adaptive when consequences improve the questions from which later transformations are constituted.**

Anti-sunk-cost rule:

> **A failed object does not earn additional authority or complexity merely because effort has already been invested in it.**

Anti-bureaucracy gate for any proposed universal machinery:

```math
\boxed{\textbf{Does this machinery change what survives, or does it merely describe the machinery?}}
```

- If it changes the admissibility or survival conditions of adaptive change, it may be a candidate protocol concern and must earn that promotion empirically.
- If it only describes how questions are constituted, failures are localized, or search proceeds, keep it in method/provenance/research-state notes unless further evidence demands otherwise.

This clarification does **not** authorize `protocol-002` and does **not** change Trace `K3` or Groundup-001.

---

## 10. Current claim ceiling and next allowed work

Earned:

- Groundup-001 remains the frozen Trace incumbent at #20 with the reported leaderboard result.
- Trace research/search state has advanced to `K3` through negative and diagnostic evidence without authorizing Groundup-002.
- PROTOCOL-001 enforces a narrow survival-transition bookkeeping contract.
- The unchanged protocol conformed to Trace and symbolic program repair for positive and nonpositive `C_improve` branches.
- The method/protocol/research-state separation is a current operating discipline, not a new theory or protocol primitive.

Not earned:

- Groundup-002;
- an identified `D2` in Trace;
- a claim that event interaction is the missing Trace edge;
- protocol sufficiency for intelligence/adaptation/corrigibility;
- universal future independence or minimality machinery;
- full research-state `K` ownership by the core;
- protocol-002.

Next legal Trace operation: **DISTINGUISH**.

Next legal protocol operation: **conformance/falsification**, not enhancement, until evidence resolves the `K` boundary.

The center remains:

```math
\boxed{\textbf{Does adaptive feedback make the future better than it otherwise would have been?}}
```
