# Claim Ledger

This ledger exists to stop **mechanism findings from inflating into definition claims**.

The hierarchy is:

```text
PROPOSED MAIN OBJECT
    ↓
CAUSAL MEASUREMENT RESULTS
    ↓
MECHANISM / FAILURE RESULTS
    ↓
CURRENT OPEN DIAGNOSTICS
```

The center of the program is:

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

The empirical lineage does not prove this as a universal law. It tests how to measure and understand the quantity without being fooled.

---

# A. Program-level proposal

## A1. Adaptive intelligence is proposed to track capacity for feedback-caused future improvement

```math
\boxed{I_{\rm adaptive}\propto C_{\rm improve}}
```

Status: **governing proposal / not a universal established law**.

Plain language:

> Adaptive intelligence is the capacity to convert feedback into greater future viability than would otherwise be achieved.

## A2. Developmental loop

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

Status: **program-level organizing loop**, not an empirically unique mechanism.

## A3. Counterfactual contribution is not observed slope

```math
\boxed{\frac{dV}{dt}\neq C_{\rm improve}}
```

Status: **methodological requirement**.

Observed growth, stability, or decline does not by itself identify the causal contribution of adaptive feedback.

---

# B. Demonstrated causal-measurement results

These results protect the interpretation of `C_improve`.

## B1. Competence and current adaptive contribution are distinct

A frozen system can retain high competence while having little or no current consequence-sensitive adaptive contribution.

```math
\boxed{\text{competence}\neq\text{adaptive intelligence}}
```

Scope: the adaptive-intelligence proposal, not every ordinary use of the word intelligence.

## B2. Feedback requires a causal return path

The predecessor assays used:

```math
\boxed{
A_{\le t}^{(\mathrm{actual/candidate})}
\rightsquigarrow C_t
\rightsquigarrow E_t
\rightsquigarrow A_{>t}
}
```

A purported consequence must be downstream of relevant behavior and able to alter later behavior.

## B3. Observational equivalence is not causal equivalence

Yoked/replay controls showed that systems can match on a reference trajectory while differing under intervention on consequence.

```math
\boxed{
\text{observational equivalence}
\not\Rightarrow
\text{causal equivalence}
}
```

## B4. Frozen-vs-adaptive is not a clean feedback-specific assay

The surgical decomposition is:

```math
\boxed{
\begin{aligned}
C_{\rm plasticity}&=V_{\rm sham}-V_{\rm frozen}\\
C_{\rm feedback}&=V_{\rm true}-V_{\rm sham}
\end{aligned}}
```

A positive true-vs-frozen result can coexist with negative true-vs-sham feedback-specific value.

## B5. Feedback quality can reverse the sign of feedback-specific contribution

Controlled corruption produced positive, neutral, and negative `C_feedback` depending on consequence quality.

The exact neutral point in the symmetric binary assay is not universal.

## B6. Source reliability is not equivalent to adaptive contribution

A source can be substantially above chance while its consequence coupling produces:

```math
C_{\rm feedback}<0.
```

Therefore:

```math
\boxed{
\text{source reliability}
\neq
\text{actionable adaptive authority}
}
```

---

# C. Demonstrated mechanism and failure results

These explain variation in `C_improve`. They do not redefine it.

## C1. Agreement is not sufficient authority evidence

Independently trained sources can share the same shifted error.

```math
\boxed{
\text{agreement}
\neq
\text{independent corrective evidence}
}
```

## C2. Update authority and feedback-specific authority are distinct

A gate can identify a useful change without proving that the consequence-linked component is what deserves causal credit.

```math
\boxed{A_{\rm update}\neq A_{\rm feedback}}
```

## C3. Feedback-specific authority can be partially estimated online

A true-vs-sham differential gate produced positive strict feedback-specific value in some regimes and strong harm suppression in others without current oracle access.

Status: **partial success**, not solved general authority.

## C4. Discrimination and causal-zero calibration are distinct

```math
\boxed{
\text{ranking quality}
\neq
\text{correct authority threshold}
}
```

Calibrated abstention improved the authority gate in the predecessor assay.

## C5. One-step authority does not automatically compose

Locally true-better-than-sham corrections can participate in a harmful continued trajectory.

```math
\boxed{
\text{good local decision}
\not\Rightarrow
\text{good adaptive trajectory}
}
```

## C6. Naive replay is not a sufficient horizon model

Replaying a few recent contexts after a candidate update predicted actual continued-dynamics horizon value worse than the simpler pointwise signal in the stress assay.

This rejects one horizon estimator, not the relevance of horizon.

## C7. One accepted correction does not immediately poison the next opportunity

A one-transition diagnostic did not support a simple immediate-poisoning explanation for the later collapse.

## C8. Individually beneficial corrections are non-additive

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

became negative even when every constituent correction was individually beneficial from a common anchor.

## C9. Negative composition was localized to state-dependent correction recomputation

The decomposition found:

```math
\Gamma_{\rm metric}>0,
\qquad
\Gamma_{\rm update}<0.
```

Thus the negative interaction came from later corrections being regenerated from states changed by earlier corrections, not merely objective curvature.

## C10. Correction value is path-dependent

The same correction-event set produced different aggregate values under different orders:

```math
\boxed{C^{(m,\pi_1)}\neq C^{(m,\pi_2)}}
```

while fixed update vectors were order-invariant to numerical precision.

## C11. Pairwise order preference is substantially predictable before acting

Out-of-seed pair-known prediction achieved roughly `0.90` AUC in the predecessor geometry.

Status: **demonstrated in that assay**, not a universal sequencing law.

## C12. Pre-decision ordering information is causally actionable

A held-out order predictor improved the resulting pairwise feedback-specific trajectory relative to fixed and deliberately predicted-worse orderings.

```math
\boxed{
\text{pre-decision information}
\rightarrow
\text{order intervention}
\rightarrow
\text{higher adaptive value}
}
```

## C13. Pairwise sequencing preferences are not perfectly transitive

Common-anchor triples contained genuine cycles, concentrated near weak margins.

Strong-margin preferences were mostly coherent in the sampled assay.

## C14. Sequencing remains useful with imperfect online selection

After removing the oracle-positive pair filter, sequencing still improved the actual selected population and reduced harm even when upstream selection was wrong.

## C15. Sequencing survives continuous execution

Continuous deployment preserved a positive sequencing increment relative to fixed chronological order.

Therefore pairwise path control was not only a common-anchor artifact.

## C16. Sequencing did not materially rewrite future admission decisions in the predecessor stream

Despite changing parameter trajectories, sequencing produced nearly identical later acceptance paths.

```math
\boxed{
\text{sequencing control demonstrated}
}

but:

```math
\boxed{
\text{strong sequencing-induced recursive selection control not demonstrated}
}
```

## C17. Calibrated selection extended the positive adaptive horizon without stabilizing it indefinitely

Replacing pointwise selection with calibrated abstention while freezing the sequencer made the process net-positive over shorter measured horizons and much less harmful at long horizon.

The specific 100–125 step crossover is assay-specific.

## C18. Long-horizon failure was not stale local calibration

Admission-time instrumentation showed later accepted corrections became more often locally true-better-than-sham and the local score became better ranked and more conservative against its one-step target.

Yet realized sequential contribution became increasingly negative.

## C19. Local authority and policy authority are empirically distinct

The final predecessor decomposition showed:

```math
\boxed{
\sum_i C_i^{(1)}>0,
\qquad
\Gamma_H\ll0,
\qquad
C_{\rm realized}^{(H)}<0
}
```

Therefore:

```math
\boxed{A_{\rm local}\neq A_{\rm policy}}
```

This is currently the strongest failure localization in the lineage.

It reinforces the need to return to the top-level counterfactual rather than trusting local machinery as a proxy for adaptive success.

---

# D. Provisional empirical regularities

These are useful patterns, not universal laws.

## D1. Environmental departure can amplify exposure to feedback quality

Across several predecessor geometries, reliable feedback became more useful and misleading feedback more harmful as inherited competence deteriorated.

## D2. Exposure duration can accumulate both benefit and harm

Longer exposure often increased the magnitude of feedback-specific benefit or damage.

## D3. Simple pairwise geometry can contain useful sequencing information

Feedback-specific update magnitude differences predicted order preference strongly in the predecessor geometry.

Do not universalize the particular feature or direction.

## D4. Strong-margin sequencing preferences appear more coherent than weak-margin preferences

Observed cycles concentrated near small order effects.

---

# E. Open questions

Open does not mean failed.

## E1. Generality of the main proposal

How far does:

```math
I_{\rm adaptive}\propto C_{\rm improve}
```

capture ordinary notions of intelligence beyond adaptive intelligence?

## E2. Cross-domain generalization

Which causal measurement and mechanism results survive in other learning, control, agentic, evolutionary, social, and representational systems?

## E3. Better mechanisms for positive long-horizon `C_improve`

Which mechanisms reliably preserve positive adaptive contribution as horizon, novelty, and interaction complexity increase?

## E4. Self-monitoring of compositional validity

```math
\boxed{
\textbf{Can operational evidence predict that a local authority rule is losing trajectory-level validity?}
}
```

This is one current diagnostic branch.

## E5. Rule-level correction

If deterioration can be detected, can that evidence causally alter the authority rule and improve long-horizon `C_improve`?

Untested.

## E6. Interface sufficiency

If deterioration is not predictable, is the limitation estimator capacity or missing information at the current interface?

---

# F. Explicitly unearned claims

Do **not** claim from the current evidence:

- that all intelligence is adaptive intelligence;
- that `I_adaptive ∝ C_improve` is already an established universal scientific law;
- that thermostats, evolution, humans, and AI learning are mechanistically identical;
- that growth is required for positive adaptive contribution;
- that a frozen baseline is always a sufficient counterfactual;
- that source accuracy determines authority;
- that agreement determines corrective authority;
- that feedback-specific authority is solved generally;
- that one-step authority implies long-horizon viability;
- that longer replay/lookahead automatically solves policy authority;
- that the predecessor horizon crossover is universal;
- that smaller corrections should universally come first;
- that pairwise sequencing yields a globally optimal scheduler;
- that sequencing materially rewrites future selection in the demonstrated stream;
- that self-monitoring of policy adequacy has been demonstrated;
- that the authority rule has learned to revise itself;
- that recursive self-improvement has been demonstrated;
- that any mechanism discovered in the lineage replaces `C_improve` as the program's main object.

---

# G. Current claim ceiling

The strongest program-level proposal remains:

> **Adaptive intelligence tracks the causal future viability gained because a system can use feedback, relative to what would otherwise have happened.**

The strongest late empirical result is:

> **A locally well-calibrated correction policy can remain correct about individual corrections while repeated application becomes globally maladaptive because state-dependent interactions overwhelm accumulated local benefit.**

The first statement is the center.

The second is one important diagnostic about how the center can fail.
