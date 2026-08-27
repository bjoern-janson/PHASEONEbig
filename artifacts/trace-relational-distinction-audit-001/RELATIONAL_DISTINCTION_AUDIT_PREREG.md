# RELATIONAL_DISTINCTION_AUDIT — preregistration

Status: DISTINGUISH ONLY. No predictor fitting, no Groundup successor, no leaderboard submission.

Incumbent: `R0 = Groundup-001 / #20`, immutable.
Search state entering audit: `K3`.

## Hard residual population C2

Within-session correct-vs-wrong objective pairs satisfying all of:

- same completed tutoring session;
- opposite outcomes;
- exact tie in failed combined objective lexical coverage;
- exact tie in student objective lexical coverage;
- exact tie in tutor objective lexical coverage;
- absolute frozen Groundup-001 probability difference <= 0.05.

Session IDs are deterministically assigned, outcome-blindly, to discovery/confirmation by SHA-256 parity, identical to the prior relational audit.

## Event representation

Each transcript is reduced to ordered student/tutor turns. For each target objective, each turn receives primitive indicators only:

- role: student or tutor;
- objective-relevant: contains >=1 retained objective term under the already-frozen tokenizer/stoplist;
- question: raw turn contains `?`;
- order in the student/tutor event sequence.

No embedding, semantic model, learned representation, label-conditioned feature construction, or fitted predictor is allowed.

## Predeclared family (8 relations)

1. `student_rel_question_to_tutor_rel_response`
   Fraction of objective-relevant student questions whose immediately following cross-role tutor turn is objective-relevant.

2. `tutor_rel_question_to_student_rel_response`
   Fraction of objective-relevant tutor questions whose immediately following cross-role student turn is objective-relevant.

3. `student_return_after_tutor_rel_contrast`
   In consecutive S→T→S triplets whose first student turn is objective-relevant: P(final S relevant | T relevant) - P(final S relevant | T nonrelevant). Returns 0 when either conditioning cell is absent.

4. `student_entry_after_tutor_rel_contrast`
   In consecutive S→T→S triplets whose first student turn is nonrelevant: P(final S relevant | T relevant) - P(final S relevant | T nonrelevant). Returns 0 when either conditioning cell is absent.

5. `cross_role_relevant_adjacency_density`
   Number of consecutive cross-role pairs where both turns are objective-relevant divided by the number of consecutive cross-role pairs.

6. `relevance_segment_fragmentation`
   Number of contiguous objective-relevant segments in the student/tutor sequence divided by number of objective-relevant turns (0 if none). Higher means repeated re-entry/dispersal rather than one contiguous burst.

7. `student_to_tutor_relevant_proximity`
   For each objective-relevant student turn, find the next later objective-relevant tutor turn. Score 1/(1+event lag); missing future match scores 0. Average over objective-relevant student turns (0 if none).

8. `tutor_to_student_relevant_proximity`
   Symmetric version from objective-relevant tutor turns to next later objective-relevant student turn.

## Estimand

For each C2 pair and relation D:

`delta = D(correct objective) - D(wrong objective)`.

Pairs are clustered by session; inferential unit is the session mean delta.

## Discovery / confirmation and multiplicity

For each relation and split report:

- pair count and session count;
- mean pair delta;
- mean session delta;
- median pair delta;
- positive/negative/zero pair fractions;
- session-cluster bootstrap 95% CI (fixed RNG seed 20260827, 10,000 bootstrap draws);
- two-sided session-level sign-flip permutation p-value (fixed RNG seed, 50,000 draws).

Within each split, apply Holm correction across all 8 relations.

A relation is `ESTABLISHED` as D2 only if:

1. discovery Holm-adjusted p < 0.05;
2. confirmation Holm-adjusted p < 0.05;
3. discovery and confirmation mean session deltas have the same nonzero sign.

Otherwise it is `NOT ESTABLISHED`.

All 8 relations and both split results will be reported regardless of apparent significance. No relation may be redefined after seeing outcomes. No model may be fit from this audit.

## Claim ceiling

Even an ESTABLISHED D2 would be only an observational residual dependency. It would authorize constitution of a separate minimal transformation experiment; it would not itself establish positive `C_improve` or mutate Groundup-001.
