# PHASEONEbig

> **Experimental assay for detecting deterioration in the compositional validity of an authority rule during continued adaptive operation.**

## Purpose

This repository begins **after** a substantial predecessor experimental lineage.

The live question is deliberately narrow:

> **Can a system detect, using information available during operation, that its own authority rule is losing compositional validity?**

Everything before this boundary is prior evidence and provenance. This repository should not silently re-open or re-label those predecessor results as if they were newly established here.

## Governing definition

The upstream adaptive-intelligence proposal is frozen as:

```math
\boxed{I_{\rm adaptive}\propto C_{\rm improve}}
```

with realized counterfactual contribution:

```math
\boxed{
C_{\rm improve}(t,H,e)
=
V_H(S_t^{+\mathrm{AF}};e)
-
V_H(S_t^{-\mathrm{AF}};e)
}
```

The important correction is:

```math
\boxed{
\text{adaptive capacity}
\neq
\text{realized causal contribution}
\neq
\text{observed viability trajectory}
}
```

Adaptive intelligence therefore does **not** require observed growth. It can manifest as maintained viability, reduced decline, damage avoidance, or recovery relative to the matched counterfactual.

## Feedback constitution

The predecessor work operationalized feedback through the causal return path:

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

where the purported consequence must be causally downstream of relevant actual or candidate behavior.

This distinguishes consequence-sensitive feedback from useful but feed-forward input, replayed updates, and generic plasticity.

## Core control decomposition

The central three-arm assay became:

```math
\boxed{
\begin{aligned}
V_{\rm frozen}
&:\text{ inherited competence}\\
V_{\rm sham}-V_{\rm frozen}
&:\text{ generic plasticity contribution}\\
V_{\rm true}-V_{\rm sham}
&:\text{ consequence-sensitive feedback contribution}
\end{aligned}
}
```

A matched sham/yoked control is essential. A frozen-vs-adaptive comparison alone can falsely credit generic plasticity to feedback.

## Current empirical boundary

The predecessor experiments established an observable gap between **local correction quality** and **trajectory validity**.

For accepted corrections with positive isolated local value:

```math
\boxed{\sum_i C_i^{(1)} > 0}
```

while the realized long-horizon feedback-specific contribution can become negative:

```math
\boxed{C_{\rm realized}^{(H)} < 0}
```

because the composition term becomes strongly negative:

```math
\boxed{
\Gamma_H
=
C_{\rm realized}^{(H)}
-
\sum_i C_i^{(1)}
\ll 0
}
```

This yields the operational distinction:

```math
\boxed{A_{\rm local}\neq A_{\rm policy}}
```

- `A_local`: does this correction deserve authority here?
- `A_policy`: does repeatedly granting authority according to this rule remain viable over the trajectory?

The key inherited result is that the local authority criterion can remain well calibrated to its **local target** while repeated locally beneficial corrections become globally maladaptive because their interactions accumulate.

## Research status

```text
LOCAL AUTHORITY          → demonstrated within predecessor assay
SEQUENCING               → demonstrated within predecessor assay
SELECTION + SEQUENCING   → demonstrated within predecessor assay
LONG-HORIZON COMPOSITION → failure localized
SELF-MONITORING OF RULE  → OPEN / untested here
```

`OPEN` means **not yet tested**. It does not mean failed.

## Live question

```math
\boxed{
\textbf{Can operational evidence reveal that the authority rule itself is losing compositional validity?}
}
```

The immediate target is **detection**, not automatic rule revision.

A future intervention may test whether evidence of deteriorating compositional validity should cause the system to increase abstention, suspend the current authority rule, or otherwise revise policy. That intervention should only be introduced after the detection problem is independently established.

## Predecessor lineage

```text
definition
  ↓
feedback constitution
  ↓
sham/yoked decomposition
  ↓
authority
  ↓
composition failure
  ↓
path dependence
  ↓
sequencing control
  ↓
continuous endogenous control
  ↓
calibrated selection
  ↓
long-horizon composition failure
  ↓
CURRENT OPEN QUESTION: self-monitoring of rule adequacy
```

See:

- [`docs/2026-08-27_EMPIRICAL_LINEAGE.md`](docs/2026-08-27_EMPIRICAL_LINEAGE.md) — full predecessor provenance chain.
- [`docs/CURRENT_BOUNDARY.md`](docs/CURRENT_BOUNDARY.md) — the one live research question and first assay constraints.
- [`docs/CLAIM_LEDGER.md`](docs/CLAIM_LEDGER.md) — demonstrated, provisional, open, and explicitly unearned claims.

## Methodological discipline

```math
\boxed{
\text{claim}
\rightarrow
\text{attack}
\rightarrow
\text{failure localization}
\rightarrow
\text{minimal sufficient repair}
\rightarrow
\text{retest}
}
```

Controls should preserve everything possible while severing only the causal edge under test.

In particular:

- do not substitute frozen baselines for matched sham/yoked controls when measuring feedback-specific value;
- do not use post-hoc oracle outcomes in online authority decisions;
- distinguish local update utility from feedback-specific utility;
- distinguish pointwise authority from policy-level authority;
- distinguish non-additivity from path dependence;
- distinguish demonstrated mechanism from speculative generalization;
- keep the current self-monitoring question live without importing unearned claims from the predecessor lineage.

## Claim ceiling

This repository does **not** begin from the claim that recursive self-correction has been demonstrated.

The strongest inherited result is narrower:

> **A locally well-calibrated correction policy can become globally maladaptive because repeated locally beneficial corrections interact negatively; the policy can remain accurate about its local target while losing compositional validity over the trajectory.**

The next boundary is whether that loss of compositional validity is itself detectable from operational evidence.
