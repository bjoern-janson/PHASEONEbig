# Current Research Boundary

## One live question

```math
\boxed{
\textbf{Can operational evidence reveal that the authority rule itself is losing compositional validity?}
}
```

This is the only live question this repository should treat as unresolved by design.

The repository inherits evidence that local correction authority can remain accurate while the policy formed by repeatedly granting that authority becomes maladaptive over a longer horizon.

The next task is **detection**.

Not automatic repair.
Not meta-learning.
Not recursive self-improvement.
Not a new definition of intelligence.

---

## Inherited empirical object

The predecessor work identified:

```math
\boxed{
\Gamma_H
=
C_{\rm realized}^{(H)}
-
\sum_i C_i^{(1)}
}
```

with observed regimes satisfying:

```math
\boxed{
\sum_i C_i^{(1)}>0,
\qquad
\Gamma_H\ll0,
\qquad
C_{\rm realized}^{(H)}<0.
}
```

Interpretation:

- individual accepted corrections remain locally beneficial relative to matched sham;
- the local authority criterion remains aligned with its local target;
- repeated application generates negative interaction terms;
- those interaction terms can overwhelm the accumulated local benefit;
- therefore local authority does not imply policy-level authority.

This is the observable discrepancy the new assay must work from.

---

## Distinction to preserve

```math
\boxed{
A_{\rm local}
\neq
A_{\rm policy}
}
```

### Local authority

```math
A_{\rm local}:
\text{Does this correction deserve authority here?}
```

### Policy authority

```math
A_{\rm policy}:
\text{Does repeatedly granting authority according to this rule remain viable over the trajectory?}
```

The predecessor selector became increasingly good at the first while the second became negative.

The new assay asks whether the system can detect that divergence **during operation**.

---

# Detection target

A minimal monitoring target should estimate a quantity related to the growing discrepancy between predicted/locally justified adaptive value and realized policy-level adaptive value.

A conceptual diagnostic is:

```math
\boxed{
G_t
=
C_{\rm realized}^{(t)}
-
\sum_{i\le t} C_i^{(1)}
}
```

or equivalently the negative composition burden:

```math
\boxed{
B_t
=
\sum_{i\le t} C_i^{(1)}
-
C_{\rm realized}^{(t)}.
}
```

But the live monitor **must not receive oracle-local values or future viability values unavailable online**.

Those quantities are evaluation targets only.

The actual monitor must estimate deterioration from signals available by time `t`.

---

# Causal chronology requirement

Any live monitor must obey:

```math
\boxed{
\mathcal H_t^{\rm available}
\rightarrow
\widehat{D}_t
\rightarrow
\text{monitor output}_t
\rightarrow
\text{future operation}
}
```

where `\mathcal H_t^{available}` contains only information genuinely available by time `t`.

Post-hoc oracle quantities may be computed later for scoring:

```math
\text{future / oracle outcomes}
\rightarrow
\text{evaluation only}
```

but may not feed back into the monitor at the same decision time.

---

# What counts as success?

The first experiment should establish **prediction**, not intervention.

A successful monitor should show that information available during operation predicts impending deterioration in compositional validity or policy-level feedback-specific contribution.

Possible targets include:

1. future sign of policy-level `C_feedback` over a fixed evaluation horizon;
2. future change in `\Gamma_H` or composition burden;
3. crossing of a pre-registered negative-composition threshold;
4. divergence between cumulative locally predicted benefit and realized causal value.

The target should be pre-registered per experiment and evaluated out of sample.

### Strong positive result

```math
\boxed{
\text{online-available history}
\rightarrow
\text{predictable future loss of compositional validity}
}
```

with calibration and held-out performance beyond simple time/horizon baselines.

### Useful negative result

If the monitor cannot predict deterioration better than baseline, then the current information interface may be insufficient.

That would localize the next question to **missing information**, not automatically to a need for a more complex model.

---

# Baselines and controls

The monitor should be challenged against simple explanations before any recursive interpretation is allowed.

At minimum consider:

- elapsed time / number of accepted corrections;
- cumulative acceptance count;
- cumulative local authority score;
- recent acceptance rate;
- recent local audit accuracy;
- recent local authority calibration residuals;
- model-state norm / update magnitude summaries;
- sequencing interaction summaries already available online;
- simple rolling realized-loss trends that are legitimately observable.

A sophisticated monitor only earns authority if it adds predictive value beyond these cheap baselines.

---

# Failure modes to distinguish

The predecessor decomposition already rejected several explanations in its assay. The new monitor should preserve those distinctions.

## F-A — local authority degradation

The local selector itself stops identifying locally beneficial corrections.

This was **not** the predecessor 200-step failure, but could arise in new domains.

## F-B — stale statistical calibration

The selector's local confidence mapping stops matching its one-step target.

This was also **not** the main predecessor failure.

## F-C — composition burden growth

Local corrections remain beneficial, but their state-dependent interactions accumulate negatively.

This was strongly supported in the predecessor assay.

## F-D — policy-level sign reversal

The realized feedback-specific process crosses from net positive to net negative at a longer horizon even though local evidence remains favorable.

This was observed in the predecessor horizon scan.

The self-monitoring assay should predict the policy-level deterioration without conflating it with F-A or F-B unless those failures are independently observed.

---

# What the monitor is NOT allowed to assume

Do not assume:

- `time` alone is deterioration;
- more accepted corrections are inherently bad;
- local authority scores must decay before policy failure;
- interaction burden must be monotonic;
- one universal horizon exists;
- the predecessor 100–125 step crossover generalizes beyond that assay;
- sequencing is sufficient to repair selection;
- detecting deterioration implies knowing how to repair it.

---

# Detection before control

The first milestone is:

```math
\boxed{
\textbf{detect loss of compositional validity}
}
```

Only after that is demonstrated should the repository test:

```math
\boxed{
\text{detected rule inadequacy}
\rightarrow
\text{changed authority over the rule itself}
}
```

A later causal intervention could compare:

```text
current authority rule continues
vs.
monitor-triggered increased abstention / suspension / revision
```

and ask whether the positive adaptive horizon is extended.

That would be the first test of feedback acquiring authority over the adaptation rule itself.

It is **not yet demonstrated**.

---

# Recursive interpretation — claim ceiling

The predecessor lineage motivates the recursion:

```math
\boxed{
\text{feedback}
\rightarrow
\text{adaptation}
\rightarrow
\text{changed interaction structure}
\rightarrow
\text{evidence about rule adequacy}
\rightarrow
\text{possible rule revision}
}
```

The lineage has experimentally reached the boundary:

```text
evidence about rule adequacy → OPEN
```

It has **not** demonstrated reliable rule self-revision.

Therefore the appropriate current statement is:

> **The system has exhibited an observable gap between local correctness and trajectory validity. Whether that gap can be detected online, and later used to revise the authority rule itself, remains open.**

---

# Stop rule

Do not add a new abstraction merely because the first monitor fails.

Use the same discipline as the predecessor work:

```math
\boxed{
\text{candidate monitor}
\rightarrow
\text{held-out causal/forecast test}
\rightarrow
\text{failure localization}
\rightarrow
\text{minimal revision}
}
```

If a simple observable explains the deterioration, prefer it.

If no online-available variable predicts the target, treat that as evidence about the information interface before escalating model complexity.
