# Predecessor Experimental Lineage — 2026-08-27

This document preserves the experimental lineage that motivated `PHASEONEbig`.

It is **provenance**, not the live assay. The current repository begins at the final boundary described below: whether an adaptive system can detect deterioration in the compositional validity of its own authority rule during continued operation.

---

## 0. Governing adaptive-intelligence proposal

The upstream proposal was reduced to:

```math
\boxed{I_{\rm adaptive}\propto C_{\rm improve}}
```

with realized causal contribution:

```math
\boxed{
C_{\rm improve}(t,H,e)
=
V_H(S_t^{+\mathrm{AF}};e)
-
V_H(S_t^{-\mathrm{AF}};e)
}
```

The key correction was to stop using observed trajectory as a proxy for causal adaptive contribution:

```math
\boxed{
\frac{dV}{dt}\neq C_{\rm improve}
}
```

and to distinguish:

```math
\boxed{
\text{capacity}
\rightarrow
\text{realized adaptive contribution}
\rightarrow
\text{observed viability trajectory}
}
```

Thus:

- `100 → 100` can reflect positive adaptive contribution if the matched no-feedback counterfactual would have been `100 → 50`;
- `100 → 80` can reflect positive adaptive contribution if the counterfactual would have been `100 → 10`;
- `100 → 120` does not establish adaptive intelligence if `120` would have happened anyway.

A capacity-level quantity, when needed, can aggregate across an explicit environment/future distribution:

```math
\boxed{
C_{\rm AF}(t,H;\mathcal E)
=
\mathcal A_{e\sim\mathcal E}
\left[C_{\rm improve}(t,H,e)\right]
}
```

where `\mathcal A` is left abstract because expectation is not always the relevant viability functional in thresholded or survival-critical settings.

### Claim ceiling

This is a proposed definition of **adaptive intelligence**, not a demonstrated definition of every ordinary use of intelligence.

Frozen competence, one-shot generalization, and feed-forward inference can be high while current adaptive contribution is near zero.

---

## 1. Feedback constitution

The hostile review asked what separates genuine feedback from ordinary useful computation.

The minimal causal topology became:

```math
\boxed{
A_{\le t}^{(\mathrm{actual/candidate})}
\rightsquigarrow
C_t
\rightsquigarrow
E_t
\rightsquigarrow
A_{>t}
}
```

with two requirements:

1. the purported consequence must be causally downstream of relevant actual or candidate behavior;
2. consequence information must be able to alter later behavior.

This excluded:

- arbitrary feed-forward input;
- replayed updates;
- lucky random mutation;
- fixed competence that does not remain consequence-coupled.

It retained:

- thermostatic control;
- prediction-error learning;
- evolutionary selection;
- adaptive control;
- model-mediated candidate evaluation/planning.

### Yoked/replay control

Two systems can be observationally identical on one reference trajectory while differing causally.

A genuine feedback system changes after an intervention on consequence:

```math
\operatorname{do}(C_k=c')
\Rightarrow
A_{>k}^{c'}\neq A_{>k}^{c}
```

while a yoked replay continues receiving the old/replayed feedback stream.

This established:

```math
\boxed{
\text{observational equivalence}
\not\Rightarrow
\text{causal equivalence}
}
```

---

## 2. Competence versus adaptive intelligence

The extensional stress test produced a real boundary:

A frozen system can solve difficult novel problems while having no current consequence-return loop.

Therefore:

```math
\boxed{
\text{competence}\neq\text{adaptive intelligence}
}
```

A useful 2×2 is:

```math
\begin{array}{c|cc}
& C_{\rm AF}\text{ low} & C_{\rm AF}\text{ high}\\ \hline
V\text{ high} & \text{capable but brittle} & \text{capable and adaptive}\\
V\text{ low} & \text{weak/brittle} & \text{adaptive but currently limited}
\end{array}
```

The broader relationship between adaptive intelligence and ordinary intelligence remains open.

---

## 3. Frozen versus adaptive was not a surgical feedback assay

The first shift experiment compared a genuine online learner against a frozen system and appeared to strongly support:

```math
\boxed{
\text{environmental departure}\uparrow
\Rightarrow
\text{adaptive value}\uparrow
}
```

But a sham/yoked plasticity arm exposed the confound.

The correct decomposition became:

```math
\boxed{
\begin{aligned}
V_{\rm frozen}
&=\text{inherited competence}\\
C_{\rm plasticity}
&=V_{\rm sham}-V_{\rm frozen}\\
C_{\rm feedback}
&=V_{\rm true}-V_{\rm sham}\\
C_{\rm total}
&=C_{\rm plasticity}+C_{\rm feedback}
\end{aligned}
}
```

The initial toy assay found that true-vs-frozen advantage rose sharply with novelty, while true-vs-sham feedback-specific contribution stayed approximately flat.

This killed the original monotonic-novelty hypothesis in that domain.

### Methodological result

A positive adaptive-vs-frozen result can hide harmful consequence coupling.

At high shift and misleading feedback, the system could satisfy:

```math
V_{\rm true}>V_{\rm frozen}
```

while simultaneously:

```math
\boxed{V_{\rm true}<V_{\rm sham}}
```

Meaning:

> Plasticity helped; the actual feedback relationship hurt.

---

## 4. Synthetic feedback reliability

A controlled feedback-reliability sweep introduced a synthetic reliability parameter `q` while preserving the sham control.

In the symmetric binary-noise construction:

```math
q>0.5\Rightarrow C_{\rm feedback}>0
```

```math
q\approx0.5\Rightarrow C_{\rm feedback}\approx0
```

```math
q<0.5\Rightarrow C_{\rm feedback}<0
```

The scientifically relevant result was the **sign reversal around an informationally neutral channel**, not the numerical value `0.5` as a universal threshold.

At high environmental shift, misleading feedback became more harmful and reliable feedback more useful.

A more defensible empirical statement was:

> **Environmental departure can increase exposure to feedback quality.**

This pattern replicated beyond the original toy geometry in:

- a stylized adaptive-control plant;
- real handwritten-digit classification under rotation shift.

The real-data assay also reproduced the masking failure: plasticity could remain positive while consequence-sensitive feedback was negative.

---

## 5. Natural reliability: source accuracy was not enough

Synthetic `q` was then removed.

A separate weak classifier supplied naturally varying feedback as the digit distribution shifted.

At `15°` rotation:

```text
teacher accuracy ≈ 72.5%
student inherited accuracy ≈ 62.5%
```

Yet:

```math
\boxed{C_{\rm feedback}\approx-0.0172}
```

So:

```math
\boxed{
\text{source reliability}
\not\equiv
\text{adaptive contribution}
}
```

Post-hoc diagnostic analysis showed that source accuracy correlated only moderately with feedback-specific contribution, while **feedback-specific update alignment relative to sham** correlated much more strongly.

Approximate reported relationships:

```text
r(source accuracy, C_feedback) ≈ 0.665
r(feedback-specific update alignment, C_feedback) ≈ 0.90
Spearman alignment ≈ 0.964
```

This motivated the distinction between source quality and whether a particular feedback-driven change deserves authority.

### Claim ceiling

The alignment diagnostic used true outcomes post hoc. It was a diagnostic target, not an online authority estimator.

---

## 6. Authority experiments

### 6.1 Independent-teacher agreement failed

Two independently trained weak teachers were used as a consensus authority criterion.

Under shared shift, they often agreed on the same error.

At `60°`, agreement was about `88%` while both teachers were only about `40%` accurate.

So:

```math
\boxed{
\text{independent agreement}
\neq
\text{independent corrective evidence}
}
```

### 6.2 Past-audit utility gate

A stronger online gate evaluated whether a proposed update would improve performance on **previously audited** consequences.

The gate beat always-trust across all tested rotations and beat an exact-count random gate in most regimes.

But under a strict matched sham control:

```math
\boxed{
V_{\rm UtilityTrue}
\not>
V_{\rm UtilitySham}
}
```

in most regimes.

Therefore the gate had learned:

```math
\boxed{
A_{\rm update}:
\text{“Should I permit this change?”}
}
```

more than:

```math
\boxed{
A_{\rm feedback}:
\text{“Should this consequence relationship be the reason for this change?”}
}
```

This established:

```math
\boxed{
\text{update authority}
\neq
\text{feedback-specific authority}
}
```

---

## 7. Feedback-specific authority

The next gate compared a true feedback-driven candidate update `u_T` against a matched sham candidate `u_S`, using only past audited evidence:

```math
\boxed{
\Delta\hat U_t
=
\hat U(u_T)-\hat U(u_S)
}
```

and granted authority when:

```math
\Delta\hat U_t>0.
```

This was the first partial success on the strict criterion:

```math
\boxed{
V_{\rm gated,true}>V_{\rm gated,sham}
}
```

in nontrivial regimes.

A particularly clean result occurred at `15°`:

```text
always-trust feedback-specific value ≈ -0.01674
gated feedback-specific value       ≈ +0.00826
```

The gate also found positive local feedback-specific value at some regimes where global teacher accuracy was only around chance.

### Harm suppression

Where the gate did not cross positive, it often removed roughly `97–99%` of feedback-specific harm.

Thus the earned characterization was:

> **Partial authority acquisition plus strong harm suppression.**

---

## 8. Mechanistic audit: two authority failures

A post-hoc audit of the same estimator separated two failure modes.

### F1 — causal-zero miscalibration

The estimator often ranked candidate pairs well but used the wrong zero-point.

Example at `75°`:

```text
Spearman(ΔÛ, oracle differential) ≈ 0.665
oracle-positive among accepted       ≈ 2%
```

So:

```math
\boxed{
\text{discrimination}
\neq
\text{calibration}
}
```

### F2 — local-to-horizon mismatch

At `90°`, accepted updates were often immediately true-better-than-sham:

```text
P(oracle positive | accepted) ≈ 78.4%
mean immediate differential   > 0
```

while the eventual gated feedback-specific trajectory was negative.

Thus:

```math
\boxed{
\text{good local decision}
\not\Rightarrow
\text{good adaptive trajectory}
}
```

---

## 9. F1 repair: calibrated abstention

A calibrated-abstention gate retained the same one-step estimator but learned a conservative causal zero-point from delayed audited outcomes.

Authority was granted only when a one-sided lower confidence bound was positive.

This increased strict feedback-positive regimes from roughly:

```text
5/11 → 8/11
```

in the replication.

It also unexpectedly flipped the `90°` regime positive, showing that conservative authority can partly suppress longer-horizon failure even without explicitly modeling horizon.

### Important separation

Better feedback-specific authority did not always improve total adaptation, because abstention can discard useful generic plasticity.

Again:

```math
\boxed{A_{\rm feedback}\neq A_{\rm update}}
```

---

## 10. F2 audit: authority grants do not automatically compose

At `90°`, post-hoc horizons `k=1,2,5` were examined.

When the current true/sham candidate was followed by **common future dynamics**, accepted true updates remained positive on average even at `k=5`.

When each branch instead continued under its respective true/sham feedback dynamics, the accepted differential crossed negative by `k=5`.

Therefore:

```math
\boxed{
\textbf{one-step feedback authority does not compose automatically}
}
```

The failure arose from interaction among successive feedback-authorized updates, not simply from one locally good update aging badly.

---

## 11. Naive short-horizon replay failed

A short-horizon authority gate tried to estimate trajectory-level value by replaying recent past feedback contexts after the current candidate.

It failed harder than the pointwise gate.

At `90°`:

```text
pointwise k=1 C_feedback ≈ -0.0020
trajectory k=5 C_feedback ≈ -0.0124
```

Equal-count controls showed this was not merely over-conservatism.

Oracle diagnostics showed that the naive `k=5` replay score was **worse** at predicting actual `k=5` continued-dynamics value than the original one-step score:

```text
Spearman(one-step score, true k=5 value) ≈ 0.357
Spearman(replay-k5 score, true k=5 value) ≈ 0.130
```

This killed:

```math
\boxed{
\text{trajectory authority}
\approx
\text{pointwise authority + replay a few steps}
}
```

The future authority problem is endogenous to prior authority grants.

---

## 12. One actual induced transition did not explain the failure

The next diagnostic compared one accepted true-feedback update against withholding and matched sham, then evaluated the **actual next authority opportunity**.

An accepted true update did **not** make the next authority problem worse.

Relative to withholding:

```text
next oracle differential shifted slightly positive
oracle-positive next opportunity increased by ~2.1 percentage points
```

Relative to a matched sham-induced state, there was a tiny adverse effect, but far too small to explain the later collapse.

Thus:

```math
\boxed{
\text{one accepted correction}
\not\Rightarrow
\text{immediately poisoned next authority surface}
}
```

The remaining hypothesis became repeated interaction / compounding.

---

## 13. Composition failure

For correction blocks:

```math
\boxed{
\Gamma_m
=
C_{\rm joint}^{(m)}
-
\sum_i C_i^{(1)}
}
```

became negative.

An apparent crossover appeared around `m≈8` in the broad accepted population.

But an oracle-positive control, restricting to blocks where **every constituent correction was individually true-better-than-sham from the common anchor**, showed negative composition interaction beginning already at `m=2` and growing with block length.

At `m=10`:

```text
sum of isolated positive effects ≈ 0.019022
joint effect                      ≈ 0.011843
```

so about `38%` of the predicted additive benefit disappeared.

### Metric versus update interaction

The interaction was decomposed into:

```math
\boxed{
\Gamma_{\rm total}
=
\Gamma_{\rm metric}
+
\Gamma_{\rm update}
}
```

with:

```text
Γ_metric > 0
Γ_update < 0
```

For example at `m=10`:

```text
Γ_metric ≈ +0.013259
Γ_update ≈ -0.020438
Γ_total  ≈ -0.007179
```

Thus the negative interaction came specifically from **state-dependent recomputation of later corrections**, not ordinary loss curvature.

The earned structural result was:

> **Individually beneficial feedback corrections are not generally additive because each correction changes the state from which subsequent corrections are generated.**

---

## 14. Path dependence

The same correction-event set was then applied in different orders:

- chronological;
- reverse;
- randomized permutations.

All constituent correction opportunities were individually oracle-positive from a common anchor.

Order materially changed final feedback-specific value.

By `m=10`, the average permutation range was about `42%` of the block’s mean causal value.

Some fixed correction-event sets even showed sign reversals across permutations.

### Fixed-vector control

When the actual parameter update vectors were frozen at the common anchor and simply summed in different orders, the order effect was approximately numerical zero (`~10^-17`).

Therefore path dependence was specifically generated by:

```math
\boxed{
\Delta\theta_i
=
\Delta\theta_i(\theta_{i-1})
}
```

not by ordering an already fixed set of parameter deltas.

Earned statement:

```math
\boxed{
C^{(m,\pi_1)}\neq C^{(m,\pi_2)}
}
```

for the same correction-event set under different orders.

---

## 15. Pre-decision order predictability

Before either correction was applied, pairwise information substantially predicted which order would be better.

Two interfaces were tested:

1. **strict online** — current correction + history only;
2. **pair known** — both candidate opportunities visible before either is applied.

On held-out seeds, the pair-known predictor achieved approximately:

```text
order-winner AUC ≈ 0.900
accuracy         ≈ 81.2%
R² signed order value ≈ 0.697
Spearman signed order value ≈ 0.829
```

A shuffled-target null stayed near chance.

Even strict-online information achieved about:

```text
AUC ≈ 0.751
```

Pairwise non-additivity was even more predictable:

```text
Spearman ≈ 0.904
R²       ≈ 0.787
```

A simple feature — difference in feedback-specific update magnitude — alone achieved about `0.780` AUC for order winner.

### Claim ceiling

This did **not** establish a universal “smaller update first” law.

It established that substantial path-quality information was available pre-decision in this assay.

---

## 16. Pairwise path control

The pre-decision predictor was then used causally on held-out seeds.

Four arms:

```text
chronological
reverse
predicted-better
predicted-worse
```

Results on oracle-positive pairs:

```text
C_chronological   ≈ 0.003863
C_reverse         ≈ 0.003862
C_predicted-better≈ 0.003957
C_predicted-worse ≈ 0.003769
C_oracle-better   ≈ 0.003974
```

Primary contrast:

```math
\boxed{
C_{\rm predicted\ better}
-
C_{\rm predicted\ worse}
\approx +0.000188
}
```

The learned controller captured about `84%` of the available oracle pair-order advantage.

This established the causal chain:

```math
\boxed{
\text{pre-decision geometry}
\rightarrow
\text{order prediction}
\rightarrow
\text{order intervention}
\rightarrow
\text{different trajectory}
\rightarrow
\text{greater adaptive value}
}
```

### Non-transitivity

Common-anchor triples showed genuine pairwise preference cycles, but rarely:

```text
raw cycle rate ≈ 1.8%
```

and cycles concentrated near weak-margin comparisons. No cycles were observed in the sampled triples once all pairwise margins exceeded the stronger threshold used in the assay.

Thus strong preferences were mostly coherent; weak/ambiguous preferences generated most cycles.

---

## 17. Selection + sequencing without oracle-positive filtering

The oracle-positive structural filter was removed.

The online selector admitted imperfect pairs:

```text
both positive     ≈ 62.98%
mixed             ≈ 30.83%
both non-positive ≈ 6.19%
```

Yet pairwise sequencing remained predictable (`AUC≈0.890`) and causally useful.

Approximate seed-weighted values:

```text
C_chronological    ≈ 0.002661
C_reverse          ≈ 0.002658
C_predicted-better ≈ 0.002749
C_predicted-worse  ≈ 0.002570
```

Primary contrast:

```math
\boxed{
C_{\rm predicted\ better}
-
C_{\rm predicted\ worse}
\approx +0.000179
}
```

Sequencing even reduced damage on pairs where both selected corrections were actually non-positive.

Thus:

> **An imperfect selector and a learned sequencing controller can operate together; sequencing can improve the adaptive value of the selector’s actual chosen corrections.**

---

## 18. Continuous endogenous execution

The selector and frozen sequencer were then run continuously so earlier order choices altered the actual model state used by later decisions.

### 50-step stream

Predicted sequencing remained causally beneficial relative to chronological ordering:

```text
ΔC_sequencing ≈ +0.000416
```

However, predicted sequencing almost never changed which later corrections the selector admitted:

```text
same acceptance sequence ≈ 97.75% of seeds
accepted-set Jaccard      ≈ 0.998
```

### 200-step stream

Sequencing remained beneficial:

```text
ΔC_sequencing ≈ +0.000708
```

but the underlying feedback-specific process became strongly harmful:

```text
C_feedback ≈ -0.234
```

Sequencing still barely changed the later admission path.

Therefore:

```math
\boxed{
\text{sequencing control works}
}
```

but:

```math
\boxed{
\text{sequencing does not automatically produce recursive selection control}
}
```

---

## 19. Calibrated selection + frozen sequencing

The sequencer was held fixed while the raw pointwise selector was replaced with calibrated abstention.

### 50 steps

The combined controller crossed from slightly negative to clearly positive feedback-specific contribution:

```text
pointwise + sequencing   ≈ -0.000803
calibrated + sequencing  ≈ +0.003264
```

Calibration materially changed the admission path.

### 200 steps

Calibration removed a large fraction of the harm but did not make the process stable indefinitely:

```text
pointwise + sequencing   ≈ -0.228678
calibrated + sequencing  ≈ -0.070901
```

The sequencing increment remained positive but small.

### Horizon scan

The calibrated selector + frozen sequencer remained feedback-positive through roughly the 100-step measurement and crossed negative by the 125-step measurement in this assay:

```text
H=50   +0.003264
H=75   +0.006209
H=100  +0.003956
H=125  -0.005097
H=150  -0.019661
H=200  -0.070901
```

Claim ceiling: these horizon values are assay-specific, not universal thresholds.

The earned result was:

> **Calibrated abstention extends the horizon over which consequence-sensitive adaptation remains net-beneficial, without making that adaptation indefinitely stable.**

---

## 20. Admission-time decomposition: final failure localization

The 200-step calibrated-selection + sequencing process was instrumented by admission time.

Four candidate explanations were tested:

1. later updates become intrinsically bad;
2. one-step calibration becomes stale;
3. later updates remain locally good but compose badly;
4. negative interaction terms accumulate faster than local benefit.

### Later accepted corrections became better locally

Approximate quarter-level pattern:

```text
Admission time  mean local oracle   oracle-positive accepted   rank correlation
1–50            +0.00131            ~78%                       ~0.673
51–100          +0.00211            ~90%                       ~0.836
101–150         +0.00274            ~93%                       ~0.869
151–200         +0.00300            ~95%                       ~0.887
```

Thus the selector was **not** simply admitting worse feedback late.

### Calibration did not go stale against its local target

The calibrated bound became conservative relative to the one-step oracle, and ranking improved over time.

Thus:

```math
\boxed{
\text{local statistical calibration did not collapse}
}
```

### Realized sequential value reversed anyway

Approximate quarter-level decomposition:

```text
Time      isolated local oracle   realized sequential increment   interaction
1–50      +0.001465               +0.000890                       -0.000575
51–100    +0.002198               -0.000125                       -0.002323
101–150   +0.002783               -0.001507                       -0.004290
151–200   +0.003008               -0.002689                       -0.005697
```

So:

```math
\boxed{
\text{isolated local value}\uparrow
\quad\text{while}\quad
\text{realized sequential value}\downarrow
}
```

### Cumulative decomposition

At the 200-step horizon:

```text
sum of isolated local contributions ≈ +0.12561
realized feedback-specific value     ≈ -0.06986
composition / interaction term       ≈ -0.19547
```

Therefore:

```math
\boxed{
\sum_i C_i^{(1)}>0
}
```

while:

```math
\boxed{
C_{\rm realized}^{(H)}<0
}
```

because:

```math
\boxed{
\Gamma_H
=
C_{\rm realized}^{(H)}
-
\sum_i C_i^{(1)}
\ll0
}
```

This killed the stale-calibration story and localized the failure to **compositional validity**.

---

# Current inherited result

The strongest earned statement is:

> **A locally well-calibrated correction policy can become globally maladaptive because repeated locally beneficial corrections interact negatively; the policy can remain accurate about its local target while losing compositional validity over the trajectory.**

Equivalently:

```math
\boxed{A_{\rm local}\neq A_{\rm policy}}
```

and:

```math
\boxed{
\text{local rationality}
\neq
\text{trajectory rationality}
}
```

The observed failure is not that the system runs out of local epistemic accuracy.

It runs out of **compositional validity**.

---

# Current open boundary

Everything above is predecessor evidence.

The live question for `PHASEONEbig` is only:

```math
\boxed{
\textbf{Can operational evidence reveal that the authority rule itself is losing compositional validity?}
}
```

A successful result would require a monitor that uses only information available by time `t` and predicts impending deterioration of policy-level adaptive value.

Post-hoc oracle quantities may be used for evaluation and diagnosis, but not as inputs to the live monitor.

Only after detection is independently established should the repository test whether evidence about rule inadequacy can acquire authority over the rule itself.

---

## Research discipline preserved

```math
\boxed{
\text{candidate mechanism}
\rightarrow
\text{causal test}
\rightarrow
\text{failure localization}
\rightarrow
\text{smaller causal test}
}
```

The lineage above should be treated as a record of what survived successive attempts to falsify earlier interpretations, not as one monolithic theory.
