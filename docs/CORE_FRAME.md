# Core Frame

## Main object

The research program is centered on one proposed quantity:

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
V_H(S_t^{\mathrm{ctrl}(AF)};e)
}
```

In plain language:

> **Adaptive intelligence is the capacity to convert feedback into greater future viability than would otherwise be achieved.**

The matched control is whatever surgical counterfactual removes the adaptive-feedback contribution being credited while preserving other relevant machinery. In many assays this is a sham/yoked adaptive control, not a frozen system.

`C_improve(t,H,e)` is the realized assay unit for a specified state, horizon, environment, and control. A claim about **capacity** requires behavior across an explicitly relevant set of futures; one favorable realization is not automatically a capacity-level result.

The top-level question is therefore:

> **Does adaptive feedback make the future better than it otherwise would have been?**

Everything else in this repository serves that question.

---

## Developmental loop

The guiding process is:

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

A useful reading is:

- **distinguish** — detect a difference that matters for future viability;
- **transform** — alter state, policy, representation, structure, or behavior in response;
- **reconstitute** — preserve or rebuild a functioning system after the change;
- **continue** — remain viable long enough for the change to matter;
- **distinguish better** — acquire greater future capacity to detect, represent, or act on consequential differences.

The loop is the **process description**. `C_improve` is the **causal score of what that process accomplished**.

The loop is deliberately mechanism-agnostic. Memory, learning, planning, compression, representation change, selection, authority gating, sequencing, repair, inheritance, self-monitoring, and rule revision may implement parts of it. None of them is the definition.

---

## Three quantities that must not be conflated

```math
\boxed{
\text{adaptive capacity}
\neq
\text{realized adaptive causal contribution}
\neq
\text{observed viability trajectory}
}
```

Observed growth is not required.

A system can have positive adaptive contribution while declining if it declines less than the matched control. A system can grow while having zero adaptive contribution if the same growth would have occurred without adaptive feedback.

Therefore:

```math
\boxed{\frac{dV}{dt}\neq C_{\rm improve}}
```

When a capacity-level quantity is needed across environments or futures, define the aggregation explicitly rather than silently treating one realized trajectory as the capacity:

```math
\boxed{
C_{\rm AF}(t,H;\mathcal E)
=
\mathcal A_{e\sim\mathcal E}
\left[C_{\rm improve}(t,H,e)\right]
}
```

where `\mathcal A` may be expectation, a risk-sensitive functional, a survival-threshold functional, or another justified viability aggregation.

This aggregation is not a new foundation. It is bookkeeping required whenever the word **capacity** ranges over more than one realized future.

---

## Feedback is causal, not merely informative

The minimal feedback topology used in the predecessor assays is:

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

The purported consequence must be causally downstream of relevant actual or candidate behavior, and consequence information must be able to alter later behavior.

Useful exogenous information is not automatically feedback.

This is why yoked/replay controls matter: two systems can be observationally identical along one trajectory yet differ in whether an intervention on consequence changes future behavior.

---

# Research hierarchy

The program should preserve this order.

## Level 1 — Definition

```math
\boxed{I_{\rm adaptive}\propto C_{\rm improve}}
```

Question:

> Did adaptive feedback causally improve the future relative to the matched counterfactual?

## Level 2 — Developmental loop

```math
\boxed{
D\rightarrow T\rightarrow R\rightarrow C\rightarrow D'
}
```

Question:

> Does the system convert consequential distinctions into changes that preserve continuation and improve future distinction capacity?

## Level 3 — Mechanisms

Examples:

- plasticity;
- memory;
- representation change;
- feedback authority;
- calibration;
- sequencing;
- planning;
- compression and reuse;
- structural inheritance;
- self-monitoring;
- rule revision.

These are candidate contributors to `C_improve`.

They are not definitions of intelligence.

## Level 4 — Assays and controls

Examples:

- matched sham/yoked adaptive controls;
- frozen controls for inherited competence;
- consequence interventions;
- delayed-audit gates;
- oracle-only post-hoc diagnostics;
- held-out prediction tests;
- order interventions;
- common-anchor composition tests.

These make causal attribution trustworthy.

They are not the theory.

## Level 5 — Failure modes

Examples discovered in the predecessor lineage:

- generic plasticity masquerading as feedback benefit;
- reliable sources producing harmful adaptive contribution;
- update utility masquerading as feedback-specific authority;
- good local corrections failing to compose;
- path dependence;
- locally valid authority producing long-horizon policy failure;
- composition burden overwhelming accumulated local benefit.

These explain why `C_improve` may be smaller or negative.

They do not replace `C_improve` as the main object.

---

# The small-theory / hard-experiment rule

```math
\boxed{
\textbf{keep the theory small; let the experiments become as complicated as causal attribution requires}
}
```

Experimental complexity is justified when it removes a confound, distinguishes competing causal explanations, or improves estimation/control of `C_improve`.

Complexity is **not** justified merely because a mechanism admits another layer of description.

The apparatus protects the small claim from being fooled. It does not become the claim.

---

# Promotion test for new distinctions

Whenever a new distinction appears, ask:

> **Does this distinction alter our estimate or causal interpretation of `C_improve`, or does it merely explain the mechanism?**

There are only three useful outcomes.

### 1. It changes measurement or causal interpretation

Keep it in the active empirical model.

Examples from the predecessor lineage include:

- frozen versus sham control;
- update authority versus feedback-specific authority;
- isolated local value versus realized trajectory value.

These distinctions changed what could legitimately be credited to adaptive feedback.

### 2. It explains a mechanism without changing the top-level quantity

Preserve it as subordinate anatomy.

Examples include particular sequencing features, update geometry, or candidate explanatory decompositions after causal attribution is already fixed.

### 3. It changes neither measurement nor useful explanation

Do not create another branch for it.

This is the anti-bureaucracy rule.

---

# Preserve correction-relevant distinctions without worshipping distinctions

The program has two symmetric responsibilities:

```math
\boxed{
\text{preserve distinctions needed for future correction}
}
```

and:

```math
\boxed{
\text{do not promote explanation-only distinctions into the object itself}
}
```

Too little distinction collapses causal differences that matter.

Too much promoted distinction turns explanatory plumbing into a substitute research object.

The objective is **corrigible compression**, not maximal conceptual granularity.

---

# Methodological cycle

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

The final arrow is deliberate.

A successful localization should normally close a branch and hand authority back to the main quantity unless independent evidence shows that the new distinction changes the active causal model.

---

# Why the predecessor plumbing matters

The predecessor experiments did not replace the definition. They showed why a naive measurement of it can be fooled.

A few examples:

- `V_true > V_frozen` can occur because generic plasticity helps even when consequence coupling hurts;
- source accuracy can be high while `C_feedback < 0`;
- an update can look locally useful without the feedback-specific component deserving causal credit;
- every accepted correction can be locally beneficial while their repeated interaction makes the realized trajectory harmful;
- the same correction opportunities can have different aggregate value in different orders.

These findings strengthen the need for the top-level counterfactual quantity.

Internal sophistication is not the target. The future difference is.

---

# Current empirical stress point

The strongest late predecessor result is:

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

Thus individually beneficial corrections can accumulate into a harmful adaptive trajectory because the interaction term overwhelms their local value.

This yields an important diagnostic distinction:

```math
\boxed{A_{\rm local}\neq A_{\rm policy}}
```

But this remains a finding **inside the causal anatomy of `C_improve`**.

It is not a replacement definition.

---

# Current diagnostic branch

One open assay asks:

```math
\boxed{
\textbf{Can operational evidence reveal that an authority rule is losing compositional validity?}
}
```

That is a legitimate falsification target because it may improve explanation or long-horizon control of `C_improve`.

It is not the center of the program, and the branch should be abandoned if it ceases to add information about the main quantity.

Self-monitoring has not been demonstrated. Rule self-revision has not been demonstrated.

---

# Claim ceiling

This repository does not claim:

- that all ordinary intelligence is adaptive intelligence;
- that the proportionality is a universal established scientific law;
- that one mechanism implements adaptive intelligence everywhere;
- that every useful feedback event produces positive long-horizon value;
- that local authority implies policy-level authority;
- that self-monitoring or recursive self-correction has been achieved.

The central proposal remains deliberately small:

> **Measure adaptive intelligence by the causal future viability gained because the system can use feedback, relative to what would otherwise have happened.**
