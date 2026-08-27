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

The top-level question is therefore:

> **Does adaptive feedback make the future better than it otherwise would have been?**

Everything else in this repository serves that question.

---

## Developmental loop

The guiding developmental loop is:

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

The loop is deliberately mechanism-agnostic. Memory, learning, planning, compression, representation change, selection, authority gating, sequencing, repair, inheritance, and other mechanisms may implement parts of it. None of those mechanisms is the definition.

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

When a capacity-level quantity is needed across environments or futures, define the aggregation explicitly rather than silently replacing realized contribution with an average:

```math
\boxed{
C_{\rm AF}(t,H;\mathcal E)
=
\mathcal A_{e\sim\mathcal E}
\left[C_{\rm improve}(t,H,e)\right]
}
```

where `\mathcal A` may be expectation, a risk-sensitive functional, a survival threshold functional, or another justified viability aggregation.

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

# The guardrail

Whenever a new mechanism or distinction appears, ask:

> **Does this change our estimate or causal interpretation of `C_improve`, or does it merely help us understand how `C_improve` is produced?**

If it only helps explain the quantity, keep it subordinate.

The methodological cycle should be:

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

The final arrow is a deliberate anti-scope-creep rule.

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

That is a legitimate next falsification target because it may help explain or improve long-horizon `C_improve`.

It is not the center of the program.

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
