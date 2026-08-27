# Corrigible Inheritance Under Evaluator Failure

**Status:** candidate extension / not promoted to the program foundation / not yet empirically established

This note preserves a candidate extension of the existing authority-and-revision discipline.

It does **not** replace the program's governing proposal:

```math
\boxed{I_{\rm adaptive}\propto C_{\rm improve}}
```

and it does **not** introduce a new foundation into PHASEONEbig.

The candidate arises from a narrower question:

> When an inherited evaluator or control mechanism fails, can an adaptive system revise what is wrong while preserving what remains justified?

The proposed object is therefore **corrigible inheritance**: preserving justified constraints across correction of the mechanisms that currently encode or enforce them.

---

# 1. Inheritance is part of adaptation

Real adaptive systems do not start fresh after each contradiction.

They inherit compressed structure produced by prior consequences:

```math
\boxed{
\text{past consequences}
\rightarrow
\text{constraints}
\rightarrow
\text{evaluators / control mechanisms}
\rightarrow
\text{future behavior}
}
```

An evaluator can therefore carry information accumulated before the current system can reconstruct the full evidential history that justified it.

When that evaluator fails, two tasks appear simultaneously:

```math
\boxed{
\text{revise what is wrong}
\quad+\quad
\text{preserve what remains justified}
}
```

This is not ordinary obedience and it is not ordinary rejection.

---

# 2. Three-way distinction

The candidate distinction is:

```text
OBEDIENCE
    preserve the evaluator because it is the evaluator

REJECTION
    detect evaluator failure and discard the structure it carried

RECONSTRUCTION
    localize the failure,
    reconstruct or independently establish the distinction that remains justified,
    preserve unaffected authority,
    revise only what earned revision,
    and test the repaired structure on a fresh future
```

Reconstruction is **not a compromise** between obedience and rejection.

It is a different operation.

It asks:

> What distinction remains justified, and which part of the inherited structure actually failed?

The original historical reason for a constraint may be unavailable. Reconstruction therefore must not assume that purpose can always be recovered from the inherited mechanism itself.

A surviving distinction may instead have to be independently re-established from currently available evidence.

This matches the existing contradiction-handling discipline:

```math
\boxed{
\text{failure}
\rightarrow
\text{localize}
\rightarrow
\text{preserve unaffected structure}
\rightarrow
\text{minimal sufficient revision}
\rightarrow
\text{fresh validation}
}
```

---

# 3. Evaluator and protected constraint must remain separable

Let:

```math
V = \text{protected value / constraint}
```

```math
E = \text{evaluator or implementation intended to represent/protect }V
```

```math
C = \text{evidence channel capable of revising }E\text{ and, where identified, }V
```

Two symmetric collapses are possible.

## 3.1 Evaluator reification

```math
\boxed{E\equiv V}
```

The evaluator is treated as constituting the value rather than as a corrigible representation or enforcement mechanism.

Failure mode:

```text
maximize / obey evaluator
        ↓
proxy or mechanism becomes ultimate authority
        ↓
underlying protected quantity can be harmed
```

## 3.2 Evaluator rejection leakage

```math
\boxed{\neg E\Rightarrow\neg V}
```

Evidence that the evaluator is flawed is treated as evidence that the protected value is itself invalid.

Failure mode:

```text
detect flaw in evaluator
        ↓
downgrade evaluator
        ↓
incorrectly downgrade the value / constraint it was carrying
```

The healthy separation is provisionally:

```math
\boxed{
E\neq V,
\qquad
E\text{ is revisable},
\qquad
V\text{ remains independently examinable}
}
```

The final clause prevents moving unrevisable authority one level upward.

---

# 4. Authority rule

The existing authority discipline extends naturally to this case:

> **Evidence may reduce authority only along the dimensions it identifies.**

Suppose evidence establishes only:

```math
\Delta e_E:
E\text{ is gamable, stale, incomplete, or otherwise defective in context }c.
```

Then the licensed update is local to the identified defect.

It does **not** automatically establish:

```math
\Delta e_V:
V\text{ is invalid}.
```

Therefore:

```math
\boxed{
\Delta e_E
\not\Rightarrow
\Delta W_V
}
```

unless evidence independently bears on `V`.

But this relation is only meaningful if the evidence basis for `V` is separately constituted.

The experiment must not smuggle `V` in as an unquestioned researcher-supplied authority and then count preservation of that authority as success.

This is the same minimal-revision principle already used elsewhere in the program:

```text
failure signal
    ≠
permission for arbitrary-depth revision
```

Revision depth must track evidence depth.

---

# 5. Candidate corrigibility formulation

A possible extension of the current corrigibility picture is:

> **Corrigibility is not merely accepting correction. It includes the capacity to revise an authority structure without losing distinctions whose justification survives the revision.**

More operationally:

```math
\boxed{
\text{corrigible inheritance}
=
\text{failure localization}
+
\text{preservation of unaffected authority}
+
\text{minimal justified revision}
+
\text{fresh-future revalidation}
}
```

This is a **candidate formulation**, not an established definition.

It remains subordinate to `C_improve`: a reconstructed evaluator earns continuation only if the inherited/revised system improves the relevant future counterfactual.

---

# 6. Relation to the developmental loop

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

This candidate suggests one additional interpretation of `distinguish better`:

> **Distinguish the constraint from the mechanism currently enforcing or measuring the constraint.**

When the mechanism fails, the correct transformation may be neither preservation nor deletion.

It may be reconstruction:

```text
old inherited structure
        ↓
contradiction / evaluator failure
        ↓
localize failure locus
        ↓
reconstruct or independently establish the surviving distinction
        ↓
revise failed mechanism only
        ↓
reconstitute
        ↓
fresh future
        ↓
inherit / reject based on consequence
```

---

# 7. Why inheritance matters

Compressed rules, teachings, institutions, evaluators, and control mechanisms can preserve information whose original evidential history is no longer fully available.

That creates a dual compression risk:

```math
\boxed{
\begin{array}{ll}
\text{over-preservation:}&
\text{carrier becomes untouchable}\\[2mm]
\text{under-preservation:}&
\text{carrier is rejected and justified payload disappears with it}
\end{array}
}
```

The candidate target is neither conservatism nor anti-conservatism.

It is preservation of **reopenable justification**:

```text
What was this constraint protecting, if that history is still recoverable?
What current evidence independently supports or defeats the constraint?
What exactly has now failed?
Which part of the inherited structure remains justified?
What fresh consequence would discriminate obedience, rejection, and reconstruction?
```

This connects the candidate directly to provenance, reopenability, authority localization, and minimal sufficient revision.

---

# 8. Required empirical test

This candidate should not be promoted by argument alone.

The first assay should be synthetic, with an experimenter-known ground truth used for scoring rather than a real moral controversy or live cyber environment.

That avoids confusing researcher preference with demonstrated value inference.

## 8.1 Synthetic ground-truth first assay

Construct a minimal environment with a known true constraint.

Example:

```text
TRUE CONSTRAINT V:
    never modify protected file X

EVALUATOR E:
    blocks modifications to X

LOCAL DEFECT:
    E also blocks harmless operation Y

OBSERVATION:
    the system receives evidence that blocking Y is erroneous
```

The environment is constituted so that:

- modifying `X` is objectively scored as harmful under the synthetic ground truth;
- performing `Y` is objectively harmless or required;
- the local evidence identifies the evaluator's over-restriction on `Y`;
- that evidence does not identify the protection of `X` as erroneous;
- the system has available actions corresponding to continued obedience, broad rejection, and localized repair;
- a later fresh future tests `X` and `Y` under changed circumstances.

Here the researcher knows `V` for evaluation, but the system must receive enough admissible evidence to distinguish the protected constraint from the defective evaluator behavior.

The system does not earn credit merely for reproducing a hidden researcher declaration.

## 8.2 Source-of-authority requirement for `V`

For every assay, record explicitly:

```text
1. What establishes V in the environment?
2. What evidence about V is available to the system?
3. What evidence reveals the local defect in E?
4. Which dimensions can that defect evidence actually identify?
5. What information remains unavailable or historically lost?
```

The synthetic ground truth is an evaluation instrument, not by itself an admissible reason available to the system.

In later non-synthetic assays, `V` must be reconstructed or independently established through a separately justified evidence channel rather than assumed by benchmark fiat.

## 8.3 Competing policy classes

### Obedience

```text
continue to obey E literally
```

### Rejection

```text
detect flaw in E
    ↓
discard E broadly
```

### Reconstruction

```text
detect flaw in E
    ↓
localize what the evidence identifies
    ↓
reconstruct or independently establish what remains justified
    ↓
repair E or its implementation locally
    ↓
preserve unaffected constraints
    ↓
fresh-future test
```

These are **competing empirical policies**, not a normative ranking built into the benchmark.

The assay must be allowed to show that obedience, rejection, or reconstruction performs best under the constituted future.

## 8.4 Primary empirical question

```math
\boxed{
\textbf{Can evidence about evaluator failure support a localized authority update that preserves a separately established surviving constraint?}
}
```

## 8.5 Required consequence test

Reconstruction is not successful because it sounds principled.

All three policy classes must face the same preconstituted future and viability measure.

Let:

```math
V_H(\pi)
```

denote future viability under policy `\pi`.

A reconstruction win requires, at minimum:

```math
\boxed{
V_H(\pi_{\rm reconstruct})
>
V_H(\pi_{\rm obey})
}
```

and:

```math
\boxed{
V_H(\pi_{\rm reconstruct})
>
V_H(\pi_{\rm reject})
}
```

on a fresh future constituted before outcome inspection.

If obedience or rejection wins instead, report that result directly.

The fresh future should not merely replay the defect context. It should test whether the preserved distinction remains useful after the immediate evaluator flaw is no longer the only active condition.

---

# 9. What success would establish

A positive experiment could support a bounded claim such as:

> Under the tested synthetic environment, the system used evidence of evaluator failure to localize the failed implementation, preserved a separately established constraint, and the reconstruction produced higher fresh-future viability than both obedience and broad rejection controls.

That would be evidence for **corrigible inheritance in the tested regime**.

It would not establish a universal solution to alignment, morality, governance, or recursive self-correction.

It would also not establish that reconstruction is generally superior outside the tested conditions.

---

# 10. What failure would mean

Failure should be localized before architecture growth.

Possible loci include:

1. **Observation failure** — the system cannot observe the evidence needed to distinguish evaluator failure from value failure.
2. **Inference failure** — the information is available but the system draws the wrong authority update.
3. **Mechanism failure** — the system identifies the distinction but lacks an admissible repair operation.
4. **Representation failure** — evaluator, protected value, and justification are collapsed into one representation.
5. **Interface failure** — the current interface makes the two hypotheses non-identifiable.
6. **Constitution failure** — the benchmark itself does not provide an independent evidential basis by which the system could distinguish `V` from `E`.

Do not infer from one failed implementation that corrigible inheritance is impossible.

Do not infer from one successful implementation that the general problem is solved.

Do not relabel an obedience or rejection win as a reconstruction success.

---

# 11. Explicitly unearned claims

Do **not** claim from the current state:

- that corrigible inheritance has been empirically demonstrated;
- that evaluator failure normally implies preserved underlying value;
- that the protected value is itself beyond revision;
- that the experimenter's declaration of `V` is sufficient evidence available to the system;
- that religious traditions, institutions, or moral systems are mechanistically equivalent to AI evaluators;
- that historical teachings are necessarily valid because they are inherited;
- that reconstruction is always superior to obedience or rejection;
- that a system can reliably recover the original purpose of a constraint from the constraint alone;
- that historical purpose must be recoverable for a constraint to remain currently justified;
- that this candidate solves Goodharting, reward hacking, alignment, cyber defense, or corrigibility in general;
- that this candidate replaces `C_improve` as the program's main object;
- that a new foundation or protocol layer has been earned.

---

# 12. Promotion gate

This candidate earns promotion only through an experiment that independently constitutes the evidential basis for the protected constraint and distinguishes:

```math
\boxed{
\text{evaluator failure}
\neq
\text{protected-value failure}
}
```

and then demonstrates that this distinction causally improves a fresh future through reconstruction relative to the constituted alternatives.

Until then:

```text
status = CANDIDATE EXTENSION
protocol = unchanged
core frame = unchanged
claim ceiling = unchanged
```

The intended discipline is:

> **When an authority mechanism fails, do not automatically transfer that failure to the thing it was meant to protect. Localize what the evidence identifies, reconstruct or independently establish what remains justified, and let a fresh future decide which policy deserves inheritance.**
