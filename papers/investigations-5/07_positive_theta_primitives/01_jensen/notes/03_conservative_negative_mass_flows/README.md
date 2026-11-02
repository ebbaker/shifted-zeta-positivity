# Conservative flows and negative mass

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Organization task J-E04.

The author's hypothesis is that a conservative flow could asymptotically remove the negative part of a determinant integrand and thereby restore a nonnegative-integral proof.

**Research task: J-B04, B — Astra.** This retains the existing task identity from Note14. Selecting the conservative flux and a theta-specific decay estimate remains conceptual. The [sole progress register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns status.

## Target and known comparison

For the complete signed density of one determinant, require
\[
\int f_s=M_{r,k}=F_{r,k}D_{r,k},\qquad
N_{r,k}(s)=\int f_s^-,\qquad f_s^-:=\max(-f_s,0).
\]
Proving N(s)->0 gives \(D_{r,k}\ge0\). Strict positivity additionally needs a surviving positive contribution or a valid positive-anchor comparison. Pointwise convergence to zero is insufficient.

A possible quantitative target is
\[
N'_{r,k}(s)\le-\lambda_{r,k}(s)N_{r,k}(s),\qquad
\int_0^\infty\lambda_{r,k}(s)\,ds=\infty.
\]
This is an unproved sufficient estimate. It must follow from the complete theta source and evolution, without assuming the determinant sign or using an inverse unknown determinant in the generator.

The ordinary heat comparison from [Note14, Section 5](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) is exact:
\[
\lim_{s\to\infty}\int(G_s*f_0)^-=\max\left(-\int f_0,0\right).
\]
Smooth invertible transport preserves negative mass exactly. Diffusion can decrease it, but smoothing alone supplies no theta sign proof.

## First bounded question

For r=4,k=1, compare ordinary product heat with at most one explicitly specified theta-based conservative flux. Give the complete signed density, the domain and all boundary fluxes, global-existence requirements independent of the desired sign, and a quantitative negative-mass estimate or a precise failed premise. Explain how a future arbitrary-order proof would depend on r and k.

**Completion:** one admissible flow and a proved estimate, scoped obstruction, or bounded execution contract. No PDE simulation or numerical positivity campaign is authorized by this brief. The known order-four positivity is a mechanism baseline, not a new result.

## Connections and reading

- [Note14, Sections 4–5 and 7](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) defines the target, the lift to r copies of three-dimensional space, and the heat benchmark.
- [Investigation05 Note25](../../../../05_radial_theta_collision_geometry/notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md) supplies complete-density conservation, boundary accounting, and ordinary heat evolution.
- [Paired deformations](../04_paired_source_test_deformations/README.md) may provide a better initial integrand or comparison.
- [Signed averaging](../../02_signed_averaging/README.md) suggests a different possible target: an increasing observable with preserved tilted averages. That requires its own conservation or comparison theorem.

## Organization

Save new derivations in this folder. Put computations and small records in the matching `01_jensen/numerics/03_conservative_negative_mass_flows/` subfolder and assessments in `01_jensen/reviews/03_conservative_negative_mass_flows/` when first needed. Keep one canonical source for reusable results and link applications. Existing numbered notes and this chat’s registration keep their current locations.

[Ideas index](../../../ideas/README.md) · [Common assessment](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) · [Live register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md)

## Initial evaluation, 1 November 2026

[The bounded return](01_INITIAL_BRANCH_EVALUATION_20261101.md) is complete. Explicit theta-quantile diffusion, global no-flux solution and exponential mixing to the conserved mean. No independent estimate forces negative mass to zero.
Prepared for Edward Baker with substantial LLM assistance, actual gpt-6-astra / ultra. [Coordinator Review02](../../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md) records the comparison and internal same-model review limits. The sole live register owns task status; next actions in the return are recommendations.
