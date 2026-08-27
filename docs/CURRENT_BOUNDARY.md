# Current Empirical Boundary

This document records one **current diagnostic boundary inside the larger `C_improve` program**.

It is not the definition of adaptive intelligence, and it is not the repository's top-level purpose.

The main object remains:

```math
\boxed{
I_{\rm adaptive}\propto C_{\rm improve}
}
```

with realized causal contribution:

```math
\boxed{
C_{\rm improve}(t,H,e)
=
V_H(S_t^{+\mathrm{AF}};e)
-
V_H(S_t^{\mathrm{ctrl}(AF)};e)
}
```

This branch exists because one predecessor failure mode revealed a gap between locally justified corrections and the realized long-horizon value of repeatedly applying the correction policy.

It remains worth pursuing only while it adds information about, or leverage over, long-horizon `C_improve`.

---

# Observed gap

The inherited empirical object is:

```math
\boxed{
\Gamma_H
=
C_{\rm realized}^{(H)}
-
\sum_i C_i^{(1)}
}
```

with observed regimes satisfying:

```math
\boxed{
\sum_i C_i^{(1)}>0,
\qquad
\Gamma_H\ll0,
\qquad
C_{\rm realized}^{(H)}<0
}
```

Interpretation:

- accepted corrections can remain individually beneficial relative to matched sham;
- the local selector can remain well aligned with its one-step target;
- repeated state-dependent corrections can interact negatively;
- accumulated interaction can overwhelm accumulated local benefit;
- therefore local correctness does not guarantee trajectory-level validity.

The diagnostic distinction is:

```math
\boxed{A_{\rm local}\neq A_{\rm policy}}
```

where:

```math
A_{\rm local}:
\text{Does this correction deserve authority here?}
```

and:

```math
A_{\rm policy}:
\text{Does repeated use of this authority rule produce positive }C_{\rm improve}\text{ over the relevant horizon?}
```

The second question is judged by the matched-counterfactual future difference, not by the apparent sophistication of the local rule.

---

# What was localized

The predecessor admission-time decomposition tested several explanations for the long-horizon sign reversal.

## Not supported as the main failure

### Late corrections simply become individually bad

No. Later accepted corrections became *more* often locally true-better-than-sham in the predecessor stress test.

### The one-step confidence mapping simply becomes stale

No. Ranking against the one-step oracle improved and the calibrated lower bound became conservative against its local target.

## Supported

### Locally beneficial corrections compose badly

Yes. Isolated local value remained positive while realized sequential contribution became increasingly negative.

### Negative interaction burden outruns local benefit

Yes. The cumulative interaction term became negative enough to reverse the sign of the realized feedback-specific trajectory.

The clean statement is:

> **The local authority rule remained competent at its local question while that local question became insufficient for the long-horizon quantity we actually care about.**

---

# Current diagnostic question

```math
\boxed{
\textbf{Can information available during operation predict loss of compositional validity?}
}
```

This is worth testing because a positive answer could improve explanation or control of long-horizon `C_improve`.

It is not the new foundation of the program.

Status: **OPEN / untested**.

---

# Detection target

A post-hoc diagnostic quantity is:

```math
\boxed{
G_t
=
C_{\rm realized}^{(t)}
-
\sum_{i\le t}C_i^{(1)}
}
```

or equivalently a positive composition burden:

```math
\boxed{
B_t
=
\sum_{i\le t}C_i^{(1)}
-
C_{\rm realized}^{(t)}
}
```

But a live diagnostic may not receive unavailable oracle-local values or future viability.

Those remain evaluation targets only.

Any operational estimator must obey:

```math
\boxed{
\mathcal H_t^{\rm available}
\rightarrow
\widehat D_t
\rightarrow
\text{diagnostic output}_t
}
```

with future/oracle outcomes used only afterward for scoring.

---

# First assay: prediction before intervention

If this branch is pursued, the first experiment should ask only whether online-available history predicts impending deterioration beyond cheap baselines.

Possible targets:

- future sign of policy-level `C_feedback` over a fixed horizon;
- future growth in negative composition burden;
- crossing a preregistered deterioration threshold;
- divergence between accumulated locally predicted benefit and later realized causal value.

At minimum compare against:

- elapsed time;
- accepted-update count;
- recent acceptance rate;
- cumulative local authority score;
- recent local calibration residuals;
- update-magnitude summaries;
- model-state summaries legitimately observable online;
- recent realized-loss trends when genuinely available.

A complicated estimator earns nothing if time or update count explains the same signal.

---

# What success would mean

A positive detection result would establish only:

```math
\boxed{
\text{online-available evidence}
\rightarrow
\text{predictable future loss of policy-level validity}
}
```

It would **not** establish:

- successful rule revision;
- recursive self-correction;
- a solved policy-authority problem;
- a new definition of intelligence.

Only after prediction succeeds should a separate causal intervention test whether detected deterioration should alter abstention, suspend the current rule, or otherwise modify policy.

---

# What failure would mean

If no online-available signal predicts deterioration beyond baseline, do not immediately add complexity.

The failure could mean:

1. the estimator is inadequate;
2. the current information interface does not expose the relevant interaction structure;
3. the target is defined at the wrong horizon;
4. the deterioration is intrinsically difficult to forecast from the available history.

Localize before repairing.

If the branch ceases to change what can be measured, predicted, or controlled about `C_improve`, close it rather than promoting more explanatory machinery.

---

# Relation to the developmental loop

The program-level loop remains:

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

The composition failure is one way that apparent success at `transform` can fail to produce a better `continue → distinguish better` trajectory.

A deterioration detector would therefore be one possible mechanism for noticing that the current transformation rule is no longer producing positive future value.

Again: mechanism, not definition.

---

# Research discipline

Use:

```math
\boxed{
\text{candidate diagnostic}
\rightarrow
\text{held-out test}
\rightarrow
\text{failure localization}
\rightarrow
\text{minimal revision}
\rightarrow
\textbf{return to }C_{\rm improve}
}
```

The guardrail is:

> **Does this result change what we know about the causal future difference, or does it merely explain one mechanism inside it?**

Keep explanations subordinate to the main object.
