# EVENT_IDENTITY_AUDIT_001 — preregistration

## State entering

```text
R0 = Groundup-001 / #20 (frozen)
K4 = lexical support, speaker lexical decomposition, lexical-order relations,
     and a broader lexical-event relation family all failed to authorize D2.
```

No Groundup-002 exists. This is a **DISTINGUISH-only** audit. No predictor will be fitted.

## Question

The previous relational family shared one upstream event constitution: a turn was objective-relevant iff it contained retained target-objective terms.

This audit asks a different question:

> Among the same hard residual collisions, is there a reproducible difference in the **kind of mathematical act that occurred**, when event identity is constituted independently of target-objective lexical overlap?

The scientific separation is:

```math
\boxed{\text{relation failure}\neq\text{event-constitution failure}}
```

This audit tests only one primitive non-overlap event constitution: **mathematical act identity**.

## Residual population C2

Frozen exactly from K4:

- same completed session;
- opposite outcomes;
- exact tie in combined lexical objective coverage;
- exact tie in student lexical objective coverage;
- exact tie in tutor lexical objective coverage;
- absolute frozen Groundup-001 probability difference <= 0.05.

Expected population from the frozen construction: 163 pairs / 157 sessions.

The deterministic discovery/confirmation split remains the SHA-256 parity split by session used in K3/K4.

## Event constitution: target-independent transcript labels

Each student/tutor turn is labeled **without access to the target objective** using fixed surface/domain-act rules. A turn may carry multiple labels.

Eligible act identities were selected solely by an outcome-blind support rule: at least 8 C2 pairs must contain paired objectives that differ in whether they demand that act identity.

### 1. add_sub

Transcript cues include arithmetic `+` / subtraction syntax and generic act words such as `plus`, `minus`, `add*`, `subtract*`, `difference`, `take away`.

Objective demand cues include `add*`, `subtract*`, `sum`, `difference`.

### 2. mult_div

Transcript cues include `×`, `÷`, `*`, and generic act words such as `times`, `multip*`, `divid*`, `quotient`, `product`, `shared`, `groups of`.

Objective demand cues include `multip*`, `divid*`, `division`, `times table`, `sharing`, `grouping`.

### 3. fraction_ratio

Transcript cues include fraction/ratio syntax (`a/b`, `a:b`) and generic act words such as `fraction`, `numerator`, `denominator`, `ratio`, `half`, `quarter`.

Objective demand cues include `fraction`, `ratio`, `mixed number`.

### 4. decimal

Transcript cues include decimal numeric literals and the generic words `decimal` / `point` in numerical context.

Objective demand cue: `decimal`.

### 5. comparison_order

Transcript cues include `<`, `>`, and generic comparison/order words (`greater`, `less`, `bigger`, `smaller`, `ascending`, `descending`, `compare`, `order`).

Objective demand cues include `compar*`, `order*`, `greater`, `less`, `ascending`, `descending`, `inequal*`.

### 6. money

Transcript cues include currency symbols and generic money-form words (`pound`, `pence`, `money`, `cost`, `change`).

Objective demand cues include `money`, `cost`, `change`, `pound`, currency symbols.

### 7. geometry

Transcript cues include generic geometry-act words (`angle`, `degree`, `triangle`, `shape`, `area`, `perimeter`) and the degree symbol.

Objective demand cues include `angle`, `degree`, `triangle`, `polygon`, `shape`, `area`, `perimeter`, `circle`, `geometry`.

### Explicit exclusion

The audit does **not** compute, reuse, or condition event identity on:

```text
terms(objective) ∩ terms(turn)
```

or any descendant of the failed lexical support predicate. Transcript event labels are generated once per turn before any target objective is supplied. Objective demand labels are generated independently from the objective wording. Matching occurs only at the predeclared **act-identity category** level.

This is not a semantic encoder, classifier, embedding, or learned taxonomy.

## Diagnostic quantities

For each split and act identity `f`, define the session event rate separately for student and tutor turns:

```math
E_f^{role}(s)=\frac{\#\text{ role turns labeled }f}{\#\text{ role turns}}.
```

To prevent objective-demand main effects from masquerading as event evidence, center each event rate **outcome-blind within the split**:

```math
\widetilde E_f^{role}(s)=E_f^{role}(s)-\mathbb E_{s'\in split}[E_f^{role}(s')].
```

For objective `o`, let `Q_f(o)∈{0,1}` indicate whether the objective demands act identity `f`.

Form-specific student support is:

```math
D_f(s,o)=Q_f(o)\widetilde E_f^{student}(s).
```

The student composite event-identity alignment is the mean centered event rate over all demanded eligible identities for that objective, or zero when no eligible identity is recognized.

The tutor composite is defined analogously and is retained as a role-channel comparison, not as a claim about student mastery.

## Preregistered diagnostic family (9)

1. `student_event_identity_alignment` — composite across all demanded eligible act identities.
2. `tutor_event_identity_alignment` — same construction on tutor turns.
3. `student_add_sub_alignment`.
4. `student_mult_div_alignment`.
5. `student_fraction_ratio_alignment`.
6. `student_decimal_alignment`.
7. `student_comparison_order_alignment`.
8. `student_money_alignment`.
9. `student_geometry_alignment`.

No additional candidate may be added after outcome inspection in this audit.

## Statistical unit and uncertainty

For each C2 pair, compute candidate value on the correct objective minus candidate value on the incorrect objective.

Because a session may contribute multiple pairs, inferential statistics operate on **session-mean pair contrasts**.

For each candidate and each split report:

- pair count;
- session count;
- mean pair contrast;
- mean session contrast;
- median pair contrast;
- positive / negative / zero pair fractions;
- session-cluster bootstrap 95% interval (10,000 resamples);
- two-sided session-level sign-flip p-value (50,000 draws).

Holm correction is applied across all 9 candidates separately within discovery and confirmation.

## Authorization rule

A candidate event-identity dependency earns `ESTABLISHED` only if:

```math
p_{Holm}^{disc}<0.05
\land
p_{Holm}^{conf}<0.05
\land
\operatorname{sign}(\Delta_{disc})=\operatorname{sign}(\Delta_{conf})\neq0.
```

Only then may `D2` be said to exist for this constituted event-identity family.

No model transformation occurs in this audit even if a distinction is established. A separate TRANSFORM experiment would have to be constituted afterward.

## Negative result interpretation

If nothing is established:

```math
(R_0,K_4)\rightarrow(R_0,K_5).
```

Earned failure statement only:

> Primitive target-independent mathematical-act event identity, aligned to target objective demand at the category level, did not reproducibly distinguish the current hardest residual futures.

This would **not** establish that event identity is irrelevant, that semantics are irrelevant, or that the session-objective dependency does not exist.

## Guardrail

```math
\boxed{\text{EVENT IDENTITY AUDIT}\neq\text{feature shopping}}
```

All nine candidates, including nulls, must be reported.
