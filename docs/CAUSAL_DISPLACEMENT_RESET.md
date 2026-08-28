# Causal Displacement Reset

**Status:** frozen conceptual reset / pre-empirical hierarchy / does not modify the current protocol or claim ledger

This note records the smallest stack currently worth preserving before introducing stronger claims about adaptation or intelligence.

It deliberately separates three objects that are often collapsed:

```math
\boxed{\Phi=\text{causal displacement}}
```

```math
\boxed{C_V=\text{value of that displacement}}
```

```math
\boxed{\mathcal C_{\rm improve}=\text{capacity to repeatedly produce positive }C_V}
```

The methodological order is:

```math
\boxed{\textbf{Difference first. Value second. Capacity third.}}
```

Only after those objects receive empirical definitions does the hypothesis

```math
\boxed{I_{\rm adaptive}\propto\mathcal C_{\rm improve}}
```

become a serious downstream claim rather than a premise.

---

# 1. Ground floor: causal displacement

Let the relevant future random variable over horizon `H` be:

```math
X_{t:t+H}.
```

Let `Y` denote the intervention whose causal influence is being tested, and let `C` fix the common pre-intervention context.

Define:

```math
\boxed{
\Phi_H(Y;C)
=
D_{\rm KL}\!\left(
P(X_{t:t+H}\mid do(Y=1),C)
\;\middle\|\;
P(X_{t:t+H}\mid do(Y=0),C)
\right)
}
```

Interpretation:

> `\Phi` measures distributional causal displacement: how much the specified future distribution changes under the intervention.

This formulation replaces the vague phrase “closest possible universe” with an explicit causal comparison.

The comparison must therefore constitute:

- the future variable `X`;
- the horizon `H`;
- the intervention `Y`;
- the shared pre-intervention context `C`.

No value claim is implied by `\Phi` alone.

---

# 2. Value is a separate projection

Let `V(X)` be a measurable value or viability functional over the same future.

Define:

```math
\boxed{
C_V(Y;C)
=
\mathbb E[V(X)\mid do(Y=1),C]
-
\mathbb E[V(X)\mid do(Y=0),C]
}
```

Interpretation:

> `C_V` measures the value difference projected onto the causal future displacement.

Therefore:

```math
\boxed{\text{causal displacement}\neq\text{causal value}}
```

A system may alter the future substantially while leaving the selected value functional unchanged, improving it, or worsening it.

---

# 3. Exact logical relations currently earned

If:

```math
\Phi=0,
```

then the two interventional future distributions are identical wherever the KL comparison is well-defined.

Therefore every measurable future functional has the same expectation under both distributions, giving:

```math
\boxed{\Phi=0\Rightarrow C_V=0.}
```

The converse does not hold:

```math
\boxed{C_V=0\not\Rightarrow\Phi=0.}
```

A causal intervention can move the future distribution entirely along dimensions ignored by `V`.

Likewise:

```math
\boxed{\Phi>0\not\Rightarrow C_V>0.}
```

When `\Phi>0`, the value consequence may satisfy:

```math
C_V<0,
\qquad
C_V=0,
\qquad\text{or}\qquad
C_V>0.
```

The clean geometry is therefore:

```math
\boxed{
\begin{array}{c}
\Phi=0\\
\Downarrow\\
C_V=0
\end{array}
\qquad
\begin{array}{c}
\Phi>0\\
\Downarrow\\
C_V<0,\;=0,\;\text{or}>0
\end{array}
}
```

A precise verbal compression is:

> **Nonzero causal value requires nonzero causal displacement, but nonzero causal displacement does not determine the sign or magnitude of causal value.**

---

# 4. Capacity is not one realized positive outcome

A single case satisfying:

```math
C_V(Y;C)>0
```

establishes one realized positive causal value contrast under the constituted intervention and future.

It does not yet establish a capacity.

The provisional higher-level object is:

```math
\boxed{
\mathcal C_{\rm improve}
=
\text{capacity for feedback-conditioned change to repeatedly produce positive }C_V
}
```

The aggregation defining this capacity is intentionally unresolved.

Do **not** yet choose among:

- expectation across futures;
- worst-case performance;
- quantile guarantees;
- robustness regions;
- environment-weighted averages;
- survival probabilities;
- any other aggregation.

Choosing one would introduce a substantive commitment that has not yet been earned.

---

# 5. Minimal hierarchy

The current ladder is:

```math
\boxed{
\begin{array}{rcl}
\text{causal displacement} &:& \Phi\\[1mm]
\text{causal value} &:& C_V\\[1mm]
\text{beneficial adaptation} &:& \text{feedback causes }C_V>0\\[1mm]
\text{improvement capacity} &:& \mathcal C_{\rm improve}
\end{array}
}
```

Only after these objects are empirically constituted should the program test:

```math
\boxed{I_{\rm adaptive}\propto\mathcal C_{\rm improve}.}
```

Thus intelligence performs no foundational work in this reset.

It is a downstream hypothesis about a measured capacity.

---

# 6. What remains unresolved

The reset does not answer:

```math
\boxed{\text{What is }X?}
```

Which portion of the future belongs in the causal distribution?

```math
\boxed{\text{What is }H?}
```

At what horizon should displacement and value be assessed?

```math
\boxed{\text{What intervention defines presence / absence?}}
```

Removing a system, action, memory, feedback channel, or policy update creates different counterfactuals.

```math
\boxed{\text{What is }V?}
```

Which future projection is being treated as valuable or viable, and what licenses that choice?

```math
\boxed{\text{How is }\mathcal C_{\rm improve}\text{ aggregated?}}
```

What family of environments and futures must repeated beneficial displacement survive before capacity is credited?

These are not defects to patch by assumption.

They are objects that future experiments must constitute.

---

# 7. Primitive questions

The reset can be operationalized as three questions:

```math
\boxed{
1.\ \text{What future difference did this thing cause?}
}
```

```math
\boxed{
2.\ \text{What value difference, if any, lies in that causal displacement?}
}
```

```math
\boxed{
3.\ \text{Can experience improve the system's ability to cause valuable differences?}
}
```

Or, in the smallest verbal form:

```math
\boxed{\textbf{Difference first. Value second. Capacity third.}}
```

A complementary compression is:

> **What future difference does a thing cause, and what portion of that difference changes what we value?**

---

# 8. Claim ceiling

Do **not** claim from this reset alone:

- that KL divergence is the uniquely correct measure of causal displacement;
- that every meaningful causal comparison admits a finite KL divergence;
- that the relevant intervention, horizon, or future variable is already known;
- that `V` has been universally identified;
- that one positive `C_V` establishes improvement capacity;
- that an aggregation rule for `\mathcal C_{\rm improve}` has been earned;
- that `I_adaptive \propto \mathcal C_improve` is established;
- that causal influence is equivalent to value;
- that large causal displacement implies benefit;
- that this reset replaces the need for matched counterfactual empirical tests.

The current freeze is only:

```math
\boxed{
\Phi=\text{difference},
\qquad
C_V=\text{value projection},
\qquad
\mathcal C_{\rm improve}=\text{capacity candidate}
}
```

with:

```math
\boxed{
\Phi=0\Rightarrow C_V=0,
\qquad
C_V=0\not\Rightarrow\Phi=0,
\qquad
\Phi>0\not\Rightarrow C_V>0.
}
```

Everything above that line must still be earned.
