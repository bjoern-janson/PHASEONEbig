# PHASEONEbig

> **Does adaptive feedback make the future better than it otherwise would have been?**

This repository studies one deliberately small proposal:

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

`C_improve` is the realized assay quantity for a specified state, horizon, environment, and matched control. Claims about **capacity** require performance across an explicitly relevant set of futures; one favorable trajectory is not automatically a capacity claim.

Everything else in this repository is subordinate to that causal difference.

---

## The developmental loop

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

This is the process description. `C_improve` is the causal score of what the process accomplished.

The loop is mechanism-agnostic. Memory, learning, representation change, authority, sequencing, planning, compression, inheritance, self-monitoring, and rule revision are possible mechanisms inside it. They are not the definition.

---

# Research hierarchy

```text
MAIN OBJECT
C_improve
    │
    ├── Is the difference really caused by feedback?
    ├── Is plasticity masquerading as feedback benefit?
    ├── Does a feedback channel deserve causal authority?
    ├── Do locally beneficial corrections compose?
    ├── Does order change aggregate value?
    ├── Can order be controlled beneficially?
    └── Does the adaptive policy remain viable over the relevant horizon?
```

Keep these levels separate:

1. **Definition** — `I_adaptive ∝ C_improve`.
2. **Developmental loop** — distinguish → transform → reconstitute → continue → distinguish better.
3. **Mechanisms** — candidate ways the loop may work.
4. **Assays and controls** — tools for trustworthy causal attribution.
5. **Failure modes** — ways the loop can produce less or negative future value.

The theory is allowed to stay small while the experiments become complicated.

The experiments earn their complexity only by making `C_improve` harder to fool.

See [`docs/CORE_FRAME.md`](docs/CORE_FRAME.md).

---

## Why the counterfactual matters

Observed trajectory is not adaptive contribution:

```math
\boxed{
\text{adaptive capacity}
\neq
\text{realized causal contribution}
\neq
\text{observed viability trajectory}
}
```

and:

```math
\boxed{\frac{dV}{dt}\neq C_{\rm improve}}
```

A system may decline while adaptive feedback still helps if the matched control declines more. A system may grow while adaptive feedback contributes nothing if the same growth would have happened anyway.

The control must remove the adaptive-feedback contribution being credited while preserving as much else as possible.

In many predecessor assays the clean feedback-specific comparison was not `adaptive vs frozen`, but:

```math
\boxed{
C_{\rm feedback}=V_{\rm true}-V_{\rm sham}
}
```

where the sham/yoked arm preserves comparable plasticity while severing the consequence relationship.

---

# What the predecessor experiments taught us

The empirical lineage repeatedly attacked ways of being fooled about `C_improve`.

| Apparent equivalence | What the experiments separated |
|---|---|
| competence = current adaptation | inherited competence can remain high while current feedback contribution is low |
| plasticity = feedback benefit | generic plasticity can help while consequence coupling hurts |
| reliable source = useful authority | an accurate source can still induce harmful adaptive change |
| useful update = feedback-specific value | a change can help without the consequence-linked component deserving causal credit |
| good local corrections = good trajectory | individually positive corrections can compose negatively |
| correction set = correction sequence | the same opportunities can have different value in different orders |
| good local authority = good policy | a locally calibrated rule can become globally maladaptive over a longer horizon |

These distinctions do **not** make the definition larger.

They make the counterfactual more surgical.

The detailed lineage is preserved in [`docs/2026-08-27_EMPIRICAL_LINEAGE.md`](docs/2026-08-27_EMPIRICAL_LINEAGE.md).

---

# Strongest late stress result

For accepted corrections, the predecessor assay reached a regime where:

```math
\boxed{
\sum_i C_i^{(1)}>0,
\qquad
\Gamma_H\ll0,
\qquad
C_{\rm realized}^{(H)}<0
}
```

with:

```math
\boxed{
\Gamma_H
=
C_{\rm realized}^{(H)}
-
\sum_i C_i^{(1)}
}
```

The selector became **better** at identifying individually useful corrections while repeated application became globally maladaptive because state-dependent interaction burden accumulated faster than local benefit.

Thus:

```math
\boxed{A_{\rm local}\neq A_{\rm policy}}
```

This is exactly why the top-level counterfactual matters: impressive local machinery is not a substitute for measuring the future difference the whole adaptive process actually caused.

---

# Current empirical boundary

The observed gap is:

```math
\boxed{
\text{local correctness}
\not\Rightarrow
\text{trajectory-level validity}
}
```

One current diagnostic branch asks:

```math
\boxed{
\textbf{Can information available during operation predict that an authority rule is losing compositional validity?}
}
```

Status: **OPEN / untested**.

Self-monitoring has not been demonstrated. Rule self-revision has not been demonstrated. Recursive self-improvement has not been demonstrated.

This branch is worth pursuing only insofar as it improves our ability to estimate, explain, or causally improve long-horizon `C_improve`.

See [`docs/CURRENT_BOUNDARY.md`](docs/CURRENT_BOUNDARY.md).

---

# Research operating rules

## 1. Return to the main quantity

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

## 2. Promotion test for new distinctions

Whenever a new distinction appears, ask:

> **Does it change our estimate or causal interpretation of `C_improve`, or does it merely explain the mechanism?**

- If it changes the measurement or causal interpretation of `C_improve`, it may belong in the active empirical model.
- If it only explains how `C_improve` is produced, preserve it as subordinate mechanism evidence.
- If it does neither, do not create another research branch for it.

## 3. Preserve correction-relevant distinctions, not explanatory bureaucracy

```math
\boxed{
\text{preserve distinctions needed for correction}
}
```

while also:

```math
\boxed{
\text{do not promote explanation-only distinctions into the object itself}
}
```

The theory stays small; the experiments are allowed to get complicated.

---

# Repository map

- [`docs/CORE_FRAME.md`](docs/CORE_FRAME.md) — canonical definition, loop, hierarchy, and promotion rules.
- [`docs/2026-08-27_EMPIRICAL_LINEAGE.md`](docs/2026-08-27_EMPIRICAL_LINEAGE.md) — detailed provenance: successive attempts to make `C_improve` causally trustworthy.
- [`docs/CLAIM_LEDGER.md`](docs/CLAIM_LEDGER.md) — proposal, demonstrated results, provisional regularities, open questions, and explicitly unearned claims.
- [`docs/CURRENT_BOUNDARY.md`](docs/CURRENT_BOUNDARY.md) — current diagnostic boundary around local correctness versus trajectory validity.
- [`docs/case_studies/`](docs/case_studies/) — real-world methodological stress tests. Case-study relevance does not itself count as causal evidence for `C_improve`.

---

# Claim ceiling

This repository does **not** claim that all intelligence is adaptive intelligence, that `I_adaptive ∝ C_improve` is already a universal scientific law, or that any single discovered mechanism is the essence of intelligence.

The center remains almost embarrassingly small:

```math
\boxed{
\textbf{Does adaptive feedback make the future better than it otherwise would have been?}
}
```

Everything else serves that question.
