# HUMAN_OBSERVER_AUDIT_001 — preregistration

**Mode:** DISTINGUISH only / no predictor / no Groundup-002  
**Entering state:** `R0 = Groundup-001 / #20`, `K5`  
**Question:** Can competent human observers recover an objective-specific mastery distinction from the completed transcript that the current representation and failed descriptive diagnostics do not recover?

## Scientific target

The audit tests observability before machine representation:

```math
\boxed{\text{Can a competent observer see what }R_0\text{ cannot?}}
```

It does **not** ask raters to predict the benchmark label directly. It asks which objective has stronger **visible evidence that the student themselves demonstrated competence** in the session.

Response set is frozen:

```text
A_STRONGER
B_STRONGER
APPROX_EQUAL
INSUFFICIENT_EVIDENCE
```

Tutor explanation counts only insofar as student behavior demonstrates uptake or competence. Raters must not use generic objective difficulty as evidence.

## Population

Use the exact existing hard residual class `C2`:

- same session;
- opposite outcomes;
- exact tie in combined lexical coverage;
- exact tie in student lexical coverage;
- exact tie in tutor lexical coverage;
- absolute frozen Groundup-001 probability difference <= 0.05.

Frozen population:

```text
163 pairs / 157 sessions
discovery:    73 pairs / 70 sessions
confirmation: 90 pairs / 87 sessions
```

The discovery/confirmation assignment is the already-used deterministic session hash and is hidden from raters.

## Blinding

Raters receive only:

```text
completed transcript
objective A wording
objective B wording
pair pseudonym
```

They do **not** receive:

- outcome labels;
- which objective is the positive/negative member of the pair;
- Groundup-001 predictions;
- lexical support values;
- prior audit values;
- discovery/confirmation membership;
- other raters' judgments.

A/B orientation is deterministic from a pair pseudonym hash and does not use outcome identity.

## Raters

Primary assay requires **three independent human raters**.

For competition-rule compliance, every person who sees Trace competition transcripts must already be a registered competition participant authorized to access the data, e.g. the participant or a formal team member. Do not distribute competition data to unaffiliated annotators.

All three raters must complete all 163 pairs for the primary authorization rule. If fewer than three eligible human raters are available, or any primary rater has incomplete judgments, the audit may be described as incomplete but **cannot authorize `D2`**.

Raters must annotate independently and remain blind to outcomes until all three judgment files are frozen.

## Primary agreement endpoint

For agreement only, collapse the four responses to three stance categories:

```text
A_STRONGER            -> A
B_STRONGER            -> B
APPROX_EQUAL          -> ABSTAIN
INSUFFICIENT_EVIDENCE -> ABSTAIN
```

Compute Fleiss' kappa across the three raters separately in discovery and confirmation. Report exact four-category agreement as a secondary diagnostic.

Bootstrap 95% confidence intervals by resampling **sessions**, preserving all pairs from a sampled session.

Agreement requirement:

```math
\boxed{\kappa_{disc}>0,\;CI_{disc}^{low}>0\quad\land\quad\kappa_{conf}>0,\;CI_{conf}^{low}>0}
```

## Primary outcome-association endpoint

Map each rater judgment to a signed blinded vote:

```text
A_STRONGER             +1
B_STRONGER             -1
APPROX_EQUAL            0
INSUFFICIENT_EVIDENCE   0
```

For pair `i`, let:

```math
v_i = \frac{1}{3}\sum_{r=1}^3 v_{ir}
```

and let hidden truth orientation be:

```math
t_i=+1 \text{ if A is the correct-outcome objective, else } -1.
```

Define pair semantic distinguishability score:

```math
\boxed{s_i=t_i v_i}
```

so correct directional evidence is positive, wrong direction is negative, and abstention/equality contributes zero.

Aggregate within session first, then across sessions. Separately in discovery and confirmation report:

- mean session score;
- session-bootstrap 95% CI with 10,000 resamples;
- two-sided session-level sign-flip p-value with 50,000 draws.

Outcome-association requirement:

```math
\boxed{\bar s_{disc}>0,\;CI_{disc}^{low}>0,\;p_{disc}<0.05}
```

and independently:

```math
\boxed{\bar s_{conf}>0,\;CI_{conf}^{low}>0,\;p_{conf}<0.05.}
```

There is one preregistered primary association endpoint, so no multiplicity correction is applied to it.

## Authorization rule

`D2` is constituted at the human semantic/functional level **only if both conditions hold**:

1. positive beyond-chance inter-rater stance agreement in discovery **and** confirmation;
2. positive semantic distinguishability score in discovery **and** confirmation under the frozen rule above.

If either condition fails:

```math
\boxed{(R_0,K_5)\rightarrow(R_0,K_6)}
```

with no transformation authorized.

If both conditions pass:

```text
D2 constituted at semantic/functional observer level
R0 still frozen
next legal operation = constitute a separate minimal TRANSFORM experiment
```

Passing this audit does **not** prove any particular machine semantic representation is correct.

## Secondary diagnostics

Report without promotion power:

- four-category Fleiss kappa;
- exact agreement fraction;
- directional coverage;
- per-rater signed semantic score;
- A/B side-choice imbalance;
- fraction `APPROX_EQUAL`;
- fraction `INSUFFICIENT_EVIDENCE`.

No secondary diagnostic may rescue a failed primary authorization rule.

## Packet identity

The blinded packet was generated before human outcome inspection.

```text
HUMAN_OBSERVER_PACKET.csv SHA-256:
e156c410dc708e1d4ac443cba35a31d793d860df479a5049ca8f49a77d02dfe4

SEALED_OUTCOME_KEY.json SHA-256:
6b0f6f92f2b3e43cab629d293189c36b29d95389c51700eaadd110f8dc031e94
```

The outcome key is not included in any rater packet and must remain sealed until all three rating files are frozen.

## Data-governance boundary

Competition transcript data and the sealed outcome key are **not to be committed to the public research repository**. The repository may preserve this preregistration, source code that reconstructs the packet from authorized local competition data, hashes, and later aggregate results.
