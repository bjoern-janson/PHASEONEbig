# Empirical Lineage — 2026-08-27

This document preserves the experimental lineage that stress-tested the adaptive-intelligence proposal:

```math
\boxed{I_{\rm adaptive}\propto C_{\rm improve}}
```

with:

```math
\boxed{
C_{\rm improve}(t,H,e)
=
V_H(S_t^{+\mathrm{AF}};e)
-
V_H(S_t^{\mathrm{ctrl}(AF)};e)
}
```

The lineage should be read as a sequence of attempts to answer one question without fooling ourselves:

> **Does adaptive feedback make the future better than it otherwise would have been?**

The later mechanisms — sham controls, authority, calibration, sequencing, composition, path dependence, policy monitoring — are not replacements for the definition. They are part of the causal anatomy required to interpret `C_improve` correctly.

The guiding developmental loop remained:

```math
\boxed{
\text{distinguish}
\rightarrow
\text{transform}
\rightarrow
\text{reconstitute}
\rightarrow
\text{continue}
\rightarrow
\text{distinguish better}
}
```

The methodological rule, learned the hard way, is:

```math
\boxed{
\text{claim}
\rightarrow
\text{attack}
\rightarrow
\text{failure localization}
\rightarrow
\text{minimal repair}
\rightarrow
\text{retest}
\rightarrow
\textbf{return to }C_{\rm improve}
}
```

---

# 0. Definition correction: trajectory is not causal contribution

The first correction was to separate:

```math
\boxed{
\text{adaptive capacity}
\neq
\text{realized adaptive causal contribution}
\neq
\text{observed viability trajectory}
}
```

Therefore:

```math
\boxed{\frac{dV}{dt}\neq C_{\rm improve}}
```

Examples:

- `100 → 100` can reflect positive adaptive contribution if the matched control would have fallen to `50`;
- `100 → 80` can still reflect positive contribution if the control would have fallen to `10`;
- `100 → 120` does not establish adaptive contribution if `120` would have happened without adaptive feedback.

When a capacity-level quantity is needed across environments, aggregate realized contribution explicitly:

```math
\boxed{
C_{\rm AF}(t,H;\mathcal E)
=
\mathcal A_{e\sim\mathcal E}
[C_{\rm improve}(t,H,e)]
}
```

### What this changed about `C_improve`

It made the quantity counterfactual rather than observational.

### Claim ceiling

This is a proposed definition of **adaptive intelligence**, not every ordinary use of intelligence.

---

# 1. Feedback constitution: useful input is not automatically feedback

The hostile review asked what makes a channel feedback rather than ordinary computation.

The causal topology became:

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

Requirements:

1. the consequence must be causally downstream of relevant actual or candidate behavior;
2. consequence information must be able to alter later behavior.

This excludes exogenous useful information when it is not behavior-dependent.

## Yoked/replay control

Two systems can be identical on one reference trajectory while differing causally.

For a true feedback system:

```math
\operatorname{do}(C_k=c')
\Rightarrow
A_{>k}^{c'}\neq A_{>k}^{c}
```

while a replay/yoked system continues receiving the old consequence stream.

Thus:

```math
\boxed{
\text{observational equivalence}
\not\Rightarrow
\text{causal equivalence}
}
```

### What this changed about `C_improve`

It constrained what may count as the `+AF` intervention.

---

# 2. Competence versus adaptive intelligence

A frozen system can solve difficult novel tasks while having no current consequence-return loop.

Therefore:

```math
\boxed{
\text{competence}
\neq
\text{current adaptive intelligence}
}
```

A system may inherit enormous capability from earlier adaptation while contributing little current adaptive improvement.

### What this changed about `C_improve`

It prevented inherited performance from being mistaken for current feedback-caused improvement.

---

# 3. Frozen-versus-adaptive was confounded by generic plasticity

The first shift experiment compared an adaptive learner with a frozen system and initially suggested that environmental departure increased adaptive value.

A sham/yoked plasticity arm broke that interpretation.

The decomposition became:

```math
\boxed{
\begin{aligned}
V_{\rm frozen}&=\text{inherited competence}\\
C_{\rm plasticity}&=V_{\rm sham}-V_{\rm frozen}\\
C_{\rm feedback}&=V_{\rm true}-V_{\rm sham}\\
C_{\rm total}&=C_{\rm plasticity}+C_{\rm feedback}
\end{aligned}}
```

A key masking failure was observed:

```math
V_{\rm true}>V_{\rm frozen}
```

while simultaneously:

```math
\boxed{V_{\rm true}<V_{\rm sham}}
```

Meaning:

> Plasticity helped; the actual consequence relationship hurt.

### What this changed about `C_improve`

The no-feedback counterfactual had to become **matched and surgical**. In feedback-specific assays, sham/yoked adaptation is often the right control, not freezing.

---

# 4. Synthetic feedback quality: the sign can reverse

A controlled reliability parameter `q` was introduced while preserving matched sham adaptation.

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

The important result was the sign reversal around informational neutrality, **not** `0.5` as a universal threshold.

The pattern replicated qualitatively in a stylized adaptive-control plant and real handwritten-digit classification under rotation shift.

At high shift, misleading feedback became more harmful and reliable feedback more valuable.

A defensible cross-assay statement was:

> **Environmental departure can increase exposure to feedback quality.**

### What this changed about `C_improve`

It showed that “having feedback” is not intrinsically positive. The sign of the causal contribution must be measured.

---

# 5. Natural reliability: source accuracy was not enough

Synthetic corruption was removed. A weak classifier supplied naturally varying feedback as digit rotation increased.

At `15°`:

```text
teacher accuracy  ≈ 72.5%
student inherited accuracy ≈ 62.5%
```

Yet:

```math
\boxed{C_{\rm feedback}\approx-0.0172}
```

Therefore:

```math
\boxed{
\text{source reliability}
\neq
\text{adaptive contribution}
}
```

Post-hoc diagnostics found roughly:

```text
r(source accuracy, C_feedback) ≈ 0.665
r(feedback-specific update alignment, C_feedback) ≈ 0.90
Spearman alignment ≈ 0.964
```

The alignment diagnostic used true labels post hoc, so it was a mechanism probe rather than an online policy.

### What this changed about `C_improve`

It killed the shortcut “accurate source ⇒ useful adaptive authority.”

---

# 6. Authority: agreement and generic update utility were insufficient

## 6.1 Independent-teacher agreement failed

Two separately trained weak teachers often agreed on the same shifted error.

At `60°`:

```text
agreement ≈ 88%
teacher accuracies ≈ 40%
```

Thus:

```math
\boxed{
\text{independent agreement}
\neq
\text{independent corrective evidence}
}
```

## 6.2 Past-audit utility gate

A gate used only previously audited outcomes to ask whether a candidate update would improve performance on the past-audit buffer.

It beat always-trust and many matched random-count controls.

But under a strict matched sham comparator it usually did not establish:

```math
V_{\rm UtilityTrue}>V_{\rm UtilitySham}
```

So it had learned:

```math
A_{\rm update}:
\text{Should this change occur?}
```

more than:

```math
A_{\rm feedback}:
\text{Should this consequence relationship be the reason for the change?}
```

Therefore:

```math
\boxed{A_{\rm update}\neq A_{\rm feedback}}
```

### What this changed about `C_improve`

It separated generic update usefulness from feedback-specific causal credit.

---

# 7. Feedback-specific authority: first partial causal success

The next gate compared true and matched sham candidate updates using past audits:

```math
\boxed{
\Delta\hat U_t
=
\hat U(u_T)-\hat U(u_S)
}
```

and granted true-feedback authority when:

```math
\Delta\hat U_t>0.
```

A clean success occurred at `15°`:

```text
always-trust C_feedback ≈ -0.01674
gated C_feedback        ≈ +0.00826
```

In regimes where the gate did not cross positive, it often removed roughly `97–99%` of feedback-specific harm.

Earned characterization:

> **Partial feedback-specific authority acquisition plus strong harm suppression.**

### What this changed about `C_improve`

It showed that some pre-decision evidence can causally improve the feedback-specific component of future viability.

---

# 8. Mechanistic audit: discrimination versus calibration, local versus horizon

Two failure modes appeared.

## F1 — wrong causal zero-point

The authority score could rank candidates well while placing the trust threshold badly.

At `75°`:

```text
Spearman(score, oracle differential) ≈ 0.665
oracle-positive among accepted       ≈ 2%
```

Thus:

```math
\boxed{
\text{discrimination}
\neq
\text{calibration}
}
```

## F2 — local-to-horizon mismatch

At `90°`:

```text
P(oracle positive | accepted) ≈ 78.4%
mean immediate differential > 0
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

### What this changed about `C_improve`

It exposed horizon as part of the causal quantity rather than a cosmetic evaluation choice.

---

# 9. F1 repair: calibrated abstention

A delayed-audit residual calibration was added while preserving the one-step target.

Authority was granted only when a one-sided lower confidence bound was positive.

This increased strict feedback-positive regimes from approximately:

```text
5/11 → 8/11
```

and flipped the `90°` regime positive in that replication.

But better feedback authority did not always improve total adaptation, because abstention can discard beneficial generic plasticity.

### What this changed about `C_improve`

It showed that threshold calibration can improve causal attribution and short-horizon value without solving long-horizon composition.

---

# 10. One-step authority did not compose automatically

At `90°`, accepted updates were audited over `k=1,2,5`.

When true and sham candidate branches received the **same future dynamics**, the accepted true candidate remained positive on average even at `k=5`.

When each branch continued under its respective true/sham feedback channel, the accepted differential crossed negative by `k=5`.

Therefore:

```math
\boxed{
\textbf{one-step feedback authority does not compose automatically}
}
```

The failure came from interaction among successive feedback-authorized updates, not one isolated good correction simply aging badly.

---

# 11. Naive short-horizon replay failed

A trajectory gate tried to improve horizon reasoning by replaying recent past feedback contexts after the candidate update.

At `90°`:

```text
pointwise k=1 C_feedback ≈ -0.0020
replay k=5 C_feedback    ≈ -0.0124
```

Equal-count controls showed this was not merely stronger abstention.

Post-hoc prediction of actual `k=5` continued-dynamics value was also worse:

```text
Spearman(pointwise score, actual k5) ≈ 0.357
Spearman(replay-k5 score, actual k5) ≈ 0.130
```

This killed:

```math
\boxed{
\text{trajectory authority}
\approx
\text{one-step authority + short replay}
}
```

### What this changed about `C_improve`

It showed that a longer simulation is not automatically a better estimator of future causal contribution if it models the wrong future dynamics.

---

# 12. One induced transition did not explain the collapse

A branch test compared an accepted true correction with withholding and matched sham, then measured the actual next authority opportunity.

Relative to withholding, the accepted true correction made the next oracle opportunity slightly **more** favorable:

```text
next oracle-positive probability ≈ +2.1 percentage points
```

Relative to matched sham there was a tiny adverse effect, far too small to explain the later collapse.

Thus:

```math
\boxed{
\text{one accepted correction}
\not\Rightarrow
\text{immediately poisoned next authority surface}
}
```

The remaining target was repeated interaction.

---

# 13. Composition failure

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

In the broad accepted population the net crossover appeared around `m≈8`, but an oracle-positive control showed interaction was already present from `m=2`.

At `m=10` for blocks where every constituent correction was individually positive from a common anchor:

```text
sum of isolated effects ≈ 0.019022
joint effect             ≈ 0.011843
```

about `38%` below the additive prediction.

## Metric versus state-dependent update interaction

```math
\boxed{
\Gamma_{\rm total}
=
\Gamma_{\rm metric}
+
\Gamma_{\rm update}
}
```

At `m=10`:

```text
Γ_metric ≈ +0.013259
Γ_update ≈ -0.020438
Γ_total  ≈ -0.007179
```

So objective/metric curvature contributed **positively**. The negative term came from recomputing later updates on states changed by earlier updates.

Earned structural statement:

> **Individually beneficial feedback corrections are not generally additive because each correction changes the state from which subsequent corrections are generated.**

### What this changed about `C_improve`

It showed that aggregate adaptive contribution cannot generally be reconstructed by summing isolated one-step contributions.

---

# 14. Path dependence

The same correction-event set was executed in chronological, reverse, and randomized orders.

All constituent opportunities in the main control were individually oracle-positive from a common anchor.

By `m=10`, the average permutation range was about `42%` of the block's mean causal value. Some fixed event sets even crossed sign under different orders.

A fixed-vector control was order-invariant to numerical precision (`~10^-17`).

Therefore the order effect arose from:

```math
\boxed{
\Delta\theta_i
=
\Delta\theta_i(\theta_{i-1})
}
```

not from merely summing fixed deltas in another order.

Thus:

```math
\boxed{C^{(m,\pi_1)}\neq C^{(m,\pi_2)}}
```

for the same correction-event set.

### What this changed about `C_improve`

It showed that future adaptive value can be path-dependent even when the set of correction opportunities is fixed.

---

# 15. Pre-decision sequencing information existed

Two information interfaces were tested:

1. **strict online** — current correction + history only;
2. **pair known** — both candidate correction opportunities visible before either is applied.

On held-out seeds, pair-known prediction achieved approximately:

```text
order-winner AUC ≈ 0.900
accuracy         ≈ 81.2%
R² signed order value ≈ 0.697
Spearman signed order value ≈ 0.829
```

Strict-online information still achieved about:

```text
AUC ≈ 0.751
```

Pairwise non-additivity was even more predictable:

```text
Spearman ≈ 0.904
R²       ≈ 0.787
```

A simple difference in feedback-specific update magnitude alone reached about `0.780` AUC for order winner.

This did **not** establish a universal “smaller update first” law.

### What this changed about `C_improve`

It showed that some path-dependent future value was identifiable before acting.

---

# 16. Sequencing prediction became causal path control

The held-out predictor was used to choose pair order.

Four arms:

```text
chronological
reverse
predicted-better
predicted-worse
```

On oracle-positive pairs:

```text
C_chronological    ≈ 0.003863
C_reverse          ≈ 0.003862
C_predicted-better ≈ 0.003957
C_predicted-worse  ≈ 0.003769
C_oracle-better    ≈ 0.003974
```

Primary contrast:

```math
\boxed{
C_{\rm predicted\ better}
-
C_{\rm predicted\ worse}
\approx+0.000188
}
```

The learned controller captured about `84%` of the available oracle pair-order advantage.

The causal chain was:

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

Pairwise preference cycles occurred in about `1.8%` of common-anchor triples and concentrated near weak margins.

### What this changed about `C_improve`

It demonstrated that understanding one mechanism — interaction geometry — could be converted back into a measurable increase in the top-level causal quantity.

---

# 17. Selection + sequencing survived removal of the oracle-positive filter

The online selector admitted imperfect pairs:

```text
both positive     ≈ 62.98%
mixed             ≈ 30.83%
both non-positive ≈ 6.19%
```

Yet order prediction remained strong (`AUC≈0.890`) and causal sequencing still improved the actual selected population:

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
\approx+0.000179
}
```

Sequencing even reduced damage on pairs where both selected corrections were non-positive.

### What this changed about `C_improve`

It showed that path control adds value even when upstream correction selection is imperfect.

---

# 18. Continuous execution: sequencing stayed useful but barely changed later selection

The selector + frozen sequencer were run continuously.

## 50 steps

```text
ΔC_sequencing ≈ +0.000416
```

but:

```text
same acceptance sequence ≈ 97.75% of seeds
accepted-set Jaccard      ≈ 0.998
```

## 200 steps

```text
ΔC_sequencing ≈ +0.000708
```

while the underlying feedback-specific process became strongly harmful:

```text
C_feedback ≈ -0.234
```

Sequencing still barely changed which later corrections were admitted.

Thus:

```math
\boxed{
\text{sequencing control demonstrated}
}
```

while:

```math
\boxed{
\text{strong sequencing-induced recursive selection control not demonstrated}
}
```

### What this changed about `C_improve`

It separated a useful path-control mechanism from the broader viability of the adaptive policy.

---

# 19. Calibrated selection + frozen sequencing

The sequencer was frozen while pointwise selection was replaced by calibrated abstention.

## 50 steps

```text
pointwise + sequencing  ≈ -0.000803
calibrated + sequencing ≈ +0.003264
```

Calibration materially changed the admission path.

## 200 steps

```text
pointwise + sequencing  ≈ -0.228678
calibrated + sequencing ≈ -0.070901
```

Calibration removed a large fraction of harm but did not stabilize the process indefinitely.

## Horizon scan

```text
H=50   +0.003264
H=75   +0.006209
H=100  +0.003956
H=125  -0.005097
H=150  -0.019661
H=200  -0.070901
```

The exact crossover is assay-specific.

Earned statement:

> **Calibrated abstention extends the horizon over which consequence-sensitive adaptation remains net-beneficial, without making that adaptation indefinitely stable.**

### What this changed about `C_improve`

It demonstrated directly that mechanism improvements can shift the horizon-dependent top-level causal contribution without guaranteeing indefinite positivity.

---

# 20. Final admission-time decomposition: local correctness versus trajectory validity

The 200-step calibrated-selection + sequencing process was instrumented by admission time.

Four explanations were tested:

1. later accepted corrections become intrinsically bad;
2. one-step calibration becomes stale;
3. later corrections remain locally good but compose badly;
4. negative interaction burden accumulates faster than local benefit.

## Later accepted corrections became better locally

```text
Admission time  mean local oracle   oracle-positive accepted   rank correlation
1–50            +0.00131            ~78%                       ~0.673
51–100          +0.00211            ~90%                       ~0.836
101–150         +0.00274            ~93%                       ~0.869
151–200         +0.00300            ~95%                       ~0.887
```

So the selector was not simply admitting worse corrections late.

## Local calibration did not collapse

The calibrated bound became more conservative against its one-step oracle target while ranking improved.

The stale-local-calibration explanation was therefore not supported as the main failure.

## Realized sequential value reversed anyway

```text
Time      isolated local oracle   realized sequential increment   interaction
1–50      +0.001465               +0.000890                       -0.000575
51–100    +0.002198               -0.000125                       -0.002323
101–150   +0.002783               -0.001507                       -0.004290
151–200   +0.003008               -0.002689                       -0.005697
```

Thus:

```math
\boxed{
\text{isolated local value}\uparrow
\quad\text{while}\quad
\text{realized sequential value}\downarrow
}
```

## Cumulative decomposition

At `H=200`:

```text
sum of isolated local contributions ≈ +0.12561
realized feedback-specific value    ≈ -0.06986
composition interaction term        ≈ -0.19547
```

Therefore:

```math
\boxed{
\sum_i C_i^{(1)}>0,
\qquad
\Gamma_H\ll0,
\qquad
C_{\rm realized}^{(H)}<0
}
```

where:

```math
\boxed{
\Gamma_H
=
C_{\rm realized}^{(H)}
-
\sum_i C_i^{(1)}
}
```

This localized the failure to **compositional validity**.

The local authority rule remained good at its local target while the policy produced by repeatedly following it became maladaptive.

Thus:

```math
\boxed{A_{\rm local}\neq A_{\rm policy}}
```

### What this changed about `C_improve`

This result is exactly why the top-level counterfactual remains necessary.

Internal machinery can look increasingly competent while the actual adaptive-feedback future becomes worse than the matched control.

The top-level quantity catches the failure.

---

# What the whole lineage means

The experiments did **not** progressively replace the original definition with authority, sequencing, composition, or self-monitoring.

They progressively showed how naive proxies for `C_improve` can fail.

The correct hierarchy is:

```text
C_improve
    ↓
feedback attribution
    ↓
plasticity control
    ↓
authority diagnostics
    ↓
composition diagnostics
    ↓
path-dependence diagnostics
    ↓
sequencing control
    ↓
policy-horizon diagnostics
```

Then:

```text
return to C_improve
```

The strongest late finding is:

> **Local correctness does not guarantee trajectory-level validity.**

That is a failure mode inside the main program, not a new foundation.

---

# Current empirical boundary

One open diagnostic question naturally follows:

```math
\boxed{
\textbf{Can information available during operation predict that an authority rule is losing compositional validity?}
}
```

This question is **open / untested**.

If pursued, it should remain subordinate to the top-level question:

> **Does the resulting mechanism improve `C_improve` over the relevant horizon and matched control?**

Self-monitoring is not yet demonstrated. Rule self-revision is not yet demonstrated. Recursive self-improvement is not yet demonstrated.

---

# Program guardrail

Whenever a new mechanism is discovered, ask:

> **Does this change our estimate or causal interpretation of `C_improve`, or does it merely help us understand it?**

If it only helps explain the quantity, preserve the result — then return to the main object.
