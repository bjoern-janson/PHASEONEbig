# RELATIONAL_DISTINCTION_AUDIT

**Status:** DISTINGUISH-only diagnostic; no predictor was fit and Groundup-001 remained immutable.

Preregistration SHA-256: `b71a988d87859913e345896c089d56c5144df87eaf9d42e30de6d806923835f1`
Result JSON SHA-256: `fd8b6c874d0094a35d89191888c4d70aa56a90275dca20feac101757c656a24a`

## Question

Within the hard residual class C2—where Groundup-001, combined lexical support, student lexical support, and tutor lexical support already treat opposite-outcome objectives as effectively equivalent—does any preregistered primitive event relation still separate the futures?

## Population

- 163 pairs across 157 sessions
- discovery: 73 pairs / 70 sessions
- confirmation: 90 pairs / 87 sessions

## Authorization rule

ESTABLISHED only if discovery Holm p<0.05 AND confirmation Holm p<0.05 AND same nonzero sign. No model fit.

Multiplicity: Holm correction across all 8 relations separately within discovery and confirmation; session-level two-sided sign-flip p-values.

## Full family

| Candidate dependency | Discovery mean Δ | Disc. 95% CI | Disc. Holm p | Confirmation mean Δ | Conf. 95% CI | Conf. Holm p | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| `student_rel_question_to_tutor_rel_response` | +0.053401 | [-0.007143, +0.118707] | 0.855023 | +0.014368 | [-0.034483, +0.066092] | 1.000000 | **NOT ESTABLISHED** |
| `tutor_rel_question_to_student_rel_response` | -0.003724 | [-0.030815, +0.024140] | 1.000000 | +0.010965 | [-0.031720, +0.052815] | 1.000000 | **NOT ESTABLISHED** |
| `student_return_after_tutor_rel_contrast` | -0.002132 | [-0.047287, +0.059802] | 1.000000 | -0.016603 | [-0.059068, +0.024904] | 1.000000 | **NOT ESTABLISHED** |
| `student_entry_after_tutor_rel_contrast` | -0.001179 | [-0.025371, +0.022830] | 1.000000 | +0.003066 | [-0.039704, +0.042672] | 1.000000 | **NOT ESTABLISHED** |
| `cross_role_relevant_adjacency_density` | +0.001167 | [-0.001339, +0.004337] | 1.000000 | +0.000738 | [-0.001589, +0.002871] | 1.000000 | **NOT ESTABLISHED** |
| `relevance_segment_fragmentation` | +0.005086 | [-0.035457, +0.051562] | 1.000000 | -0.013597 | [-0.067190, +0.040758] | 1.000000 | **NOT ESTABLISHED** |
| `student_to_tutor_relevant_proximity` | +0.003118 | [-0.036012, +0.041626] | 1.000000 | +0.009159 | [-0.029132, +0.047068] | 1.000000 | **NOT ESTABLISHED** |
| `tutor_to_student_relevant_proximity` | -0.000420 | [-0.016135, +0.015366] | 1.000000 | -0.001916 | [-0.022523, +0.017899] | 1.000000 | **NOT ESTABLISHED** |

## Result

```text
ESTABLISHED D2: none
Groundup-001: unchanged
Groundup-002: not authorized
R state: R0 remains frozen
Research state: K3 -> K4
```

No member of the preregistered family achieved familywise-significant separation in discovery and confirmation with the same sign. The strongest discovery-looking question-response signal did not survive multiplicity control and was weak in confirmation.

## K4 update

The current evidence now rules out, for this hard residual population, the tested family of simple objective-conditioned event relations as an established separator: question→response relevance, S→T→S return/entry contrasts, cross-role relevance adjacency, relevance fragmentation/re-entry, and directional relevant-turn proximity.

This does **not** establish that interaction, sequence, or session–objective dependency is irrelevant. It establishes only that these preregistered primitive measurements did not identify a replicating residual distinction.

## Claim ceiling

Observational diagnostic inside C2. Does not itself establish positive C_improve.

Next legal Trace operation remains **DISTINGUISH**. Revision depth remains at the question/measurement level; no representation change is justified by this audit.
