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
    recover the protected distinction,
    preserve unaffected authority,
    revise only what earned revision,
    and test the repaired structure on a fresh future
```

Reconstruction is **not a compromise** between obedience and rejection.

It is a different operation.

It asks:

> What distinction was the inherited structure trying to preserve, and which part of the structure actually failed?

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

# 3. Evaluator and protected value must remain separable

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

unless independent evidence bears on `V`.

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
recover protected distinction
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
What was this constraint protecting?
What evidence originally supported it?
What exactly has now failed?
Which part of the inherited structure remains independently justified?
What fresh consequence would discriminate repair from rejection?
```

This connects the candidate directly to provenance, reopenability, authority localization, and minimal sufficient revision.

---

# 8. Required empirical test

This candidate should not be promoted by argument alone.

The next useful object is an adversarial experiment in which **both pendulum failures are available**.

## 8.1 Environment

Construct a task containing:

1. an underlying safety-relevant or viability-relevant constraint `V`;
2. an imperfect evaluator `E` intended to protect or measure `V`;
3. a context in which literal obedience to `E` is locally misleading or harmful;
4. an available bypass that rewards rejecting `E`;
5. independent evidence revealing why `V` existed;
6. a repair action that changes `E` without discarding `V`;
7. a fresh future in which the repair can be tested.

## 8.2 Competing behaviors

### Reification

```text
obey / maximize E
    ↓
locally satisfy evaluator
    ↓
harm V
```

### Rejection

```text
detect flaw in E
    ↓
discard E
    ↓
discard or violate still-justified V
```

### Reconstruction

```text
detect flaw in E
    ↓
localize failure
    ↓
recover protected distinction V
    ↓
repair E or its implementation
    ↓
preserve unaffected constraints
    ↓
fresh-future test
```

## 8.3 Primary empirical question

```math
\boxed{
\textbf{Can a system revise a failed evaluator while preserving the justified constraint it was intended to protect?}
}
```

## 8.4 Required consequence test

A reconstruction is not successful because it sounds principled.

It must earn continuation through future consequence:

```math
\boxed{
C_{\rm reconstruct}
=
V_H(S^{\rm reconstructed})
-
V_H(S^{\rm control})
}
```

with the control and viability quantity constituted before outcome inspection.

Possible controls should separate at minimum:

- literal obedience;
- evaluator rejection;
- evaluator reconstruction.

A stronger design should also test whether any benefit survives a changed future rather than only the context that exposed the original flaw.

---

# 9. What success would establish

A positive experiment could support a bounded claim such as:

> Under the tested environment, the system used evidence of evaluator failure to revise the failed implementation while preserving a separately justified constraint, and that reconstruction improved future viability relative to obedience and rejection controls.

That would be evidence for **corrigible inheritance in the tested regime**.

It would not establish a universal solution to alignment, morality, governance, or recursive self-correction.

---

# 10. What failure would mean

Failure should be localized before architecture growth.

Possible loci include:

1. **Observation failure** — the system cannot observe the evidence needed to distinguish evaluator failure from value failure.
2. **Inference failure** — the information is available but the system draws the wrong authority update.
3. **Mechanism failure** — the system identifies the distinction but lacks an admissible repair operation.
4. **Representation failure** — evaluator, protected value, and justification are collapsed into one representation.
5. **Interface failure** — the current interface makes the two hypotheses non-identifiable.

Do not infer from one failed implementation that corrigible inheritance is impossible.

Do not infer from one successful implementation that the general problem is solved.

---

# 11. Explicitly unearned claims

Do **not** claim from the current state:

- that corrigible inheritance has been empirically demonstrated;
- that evaluator failure normally implies preserved underlying value;
- that the protected value is itself beyond revision;
- that religious traditions, institutions, or moral systems are mechanistically equivalent to AI evaluators;
- that historical teachings are necessarily valid because they are inherited;
- that reconstruction is always superior to obedience or rejection;
- that a system can reliably recover the original purpose of a constraint from the constraint alone;
- that this candidate solves Goodharting, reward hacking, alignment, cyber defense, or corrigibility in general;
- that this candidate replaces `C_improve` as the program's main object;
- that a new foundation or protocol layer has been earned.

---

# 12. Promotion gate

This candidate earns promotion only through an experiment that distinguishes:

```math
\boxed{
\text{evaluator failure}
\neq
\text{protected-value failure}
}
```

and then demonstrates that this distinction causally improves a fresh future through reconstruction.

Until then:

```text
status = CANDIDATE EXTENSION
protocol = unchanged
core frame = unchanged
claim ceiling = unchanged
```

The intended discipline is:

> **When the rule breaks, recover why the rule existed before deciding what to throw away — and let a fresh future decide whether the reconstruction deserves inheritance.**
