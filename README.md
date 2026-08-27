# PHASEONEbig

> **Does adaptive feedback make the future better than it otherwise would have been?**

This repository studies a deliberately simple proposal:

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

Everything else in this repository is subordinate to that quantity.

---

## Developmental loop

The guiding loop is:

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

The loop is mechanism-agnostic. Memory, learning, representation change, authority, sequencing, planning, compression, inheritance, self-monitoring, and rule revision are possible mechanisms inside the loop. They are not the definition.

---

# Research hierarchy

```text
MAIN OBJECT
C_improve
    │
    ├── Does feedback actually cause the difference?
    ├── Does plasticity masquerade as feedback benefit?
    ├── Does feedback have useful authority?
    ├── Do corrections compose?
    ├── Does order matter?
    ├── Can order be controlled?
    └── Does the adaptive policy remain viable over time?
```

The repository should preserve this hierarchy:

1. **Definition** — `I_adaptive ∝ C_improve`.
2. **Developmental loop** — distinguish → transform → reconstitute → continue → distinguish better.
3. **Mechanisms** — candidate ways the loop may work.
4. **Assays and controls** — tools for trustworthy causal attribution.
5. **Failure modes** — reasons the loop may fail or produce negative `C_improve`.

The controls are important because they protect the main quantity from false attribution. They are not the theory.

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

The relevant control must remove the adaptive-feedback contribution being credited while preserving as much else as possible.

In many predecessor assays the clean comparison was not `adaptive vs frozen`, but:

```math
\boxed{
C_{\rm feedback}=V_{\rm true}-V_{\rm sham}
}
```

where the sham/yoked arm preserves plasticity while severing the consequence relationship.

---

# What the predecessor experiments established

The experimental lineage repeatedly attacked ways of being fooled about `C_improve`.

### 1. Competence is not current adaptive contribution

A frozen system can be highly capable while having little or no current consequence-sensitive adaptive contribution.

```math
\boxed{\text{competence}\neq\text{adaptive intelligence}}
```

### 2. Plasticity can masquerade as feedback benefit

A system can outperform a frozen baseline while genuine consequence coupling is harmful.

This motivated the decomposition:

```math
\boxed{
\begin{aligned}
C_{\rm plasticity}&=V_{\rm sham}-V_{\rm frozen}\\
C_{\rm feedback}&=V_{\rm true}-V_{\rm sham}
\end{aligned}}
```

### 3. Source reliability is not actionable authority

Reliable-looking sources can still induce harmful adaptive changes.

```math
\boxed{
\text{source reliability}
\neq
\text{adaptive contribution}
}
```

### 4. Update authority is not feedback-specific authority

A gate can identify useful changes without establishing that the consequence-linked component deserves causal credit.

```math
\boxed{A_{\rm update}\neq A_{\rm feedback}}
```

### 5. Individually beneficial corrections do not automatically compose

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

can be negative even when every constituent correction is individually beneficial.

The negative term was localized to state-dependent recomputation of later corrections, not merely objective curvature.

### 6. Correction value is path-dependent

The same correction opportunities can produce different aggregate causal value under different orders:

```math
\boxed{C^{(m,\pi_1)}\neq C^{(m,\pi_2)}}
```

because:

```math
\boxed{\Delta\theta_i=\Delta\theta_i(\theta_{i-1})}
```

### 7. Sequencing can be predicted and controlled

Pre-decision information predicted which pair ordering would be better, and using that prediction causally improved the resulting trajectory.

```math
\boxed{
\text{pre-decision information}
\rightarrow
\text{order intervention}
\rightarrow
\text{higher adaptive value}
}
```

### 8. Better local selection can extend the viable horizon without stabilizing it indefinitely

Calibrated abstention improved the adaptive-feedback trajectory for finite horizons, but the process eventually crossed negative in the long-horizon stress test.

### 9. Local correctness can coexist with trajectory failure

The strongest late result was:

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

The selector became better at identifying individually useful corrections while the repeated policy became globally maladaptive because interaction burden accumulated faster than local benefit.

Thus:

```math
\boxed{A_{\rm local}\neq A_{\rm policy}}
```

This is a diagnostic result about the causal anatomy of `C_improve`. It is not a new definition of intelligence.

---

# Current empirical boundary

The current observed gap is:

```math
\boxed{
\text{local correctness}
\not\Rightarrow
\text{trajectory-level validity}
}
```

One live diagnostic branch asks:

```math
\boxed{
\textbf{Can operational evidence reveal that the authority rule is losing compositional validity?}
}
```

That question is **open / untested**.

Self-monitoring has not been demonstrated. Rule self-revision has not been demonstrated. Recursive self-improvement has not been demonstrated.

See [`docs/CURRENT_BOUNDARY.md`](docs/CURRENT_BOUNDARY.md).

---

# The anti-scope-creep rule

Whenever a new mechanism appears, ask:

> **Does this change our estimate or causal interpretation of `C_improve`, or does it merely help us understand it?**

If it only explains the quantity, keep it subordinate.

The research cycle is:

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

# Repository map

- [`docs/CORE_FRAME.md`](docs/CORE_FRAME.md) — definition, developmental loop, hierarchy, and anti-scope-creep guardrail.
- [`docs/2026-08-27_EMPIRICAL_LINEAGE.md`](docs/2026-08-27_EMPIRICAL_LINEAGE.md) — detailed experimental provenance: successive attempts to make `C_improve` causally trustworthy.
- [`docs/CLAIM_LEDGER.md`](docs/CLAIM_LEDGER.md) — demonstrated results, provisional regularities, open questions, and explicitly unearned claims.
- [`docs/CURRENT_BOUNDARY.md`](docs/CURRENT_BOUNDARY.md) — current diagnostic boundary around local correctness versus trajectory validity.

---

# Claim ceiling

This repository does **not** claim that all intelligence is adaptive intelligence, that the proportionality is already a universal scientific law, or that any single mechanism is the essence of intelligence.

The center remains small:

```math
\boxed{
\textbf{Does feedback make the future better than it otherwise would have been?}
}
```

Everything else serves that question.
