# Paired source and test deformations

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Organization task J-E04.

This direction asks whether evolving the source and its testing function together can preserve the desired determinant while making its complete signed expression easier to estimate.

**Research task: J-B07, B — Astra.** The conceptual choice is a deformation and a specific sign estimate it would improve. The [sole progress register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns status. This is a separate tool-development direction with a Jensen consumer, not an assumed prerequisite for the other branches.

## Target and inherited identity

Under justified domains, regularity, and boundary conditions, adjoint evolution gives
\[
\partial_s\rho_s=L_s^*\rho_s,\qquad
\partial_s p_s=-L_sp_s,\qquad
\frac d{ds}\int\rho_sp_s=0.
\]
The second equation is a backward test evolution and needs an existence and growth argument. The identity alone does not supply one.

[Investigation05 Note17](../../../../05_radial_theta_collision_geometry/notes/17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md) provides an explicit paired Darboux construction preserving H. Its complete energy identity retains forcing and boundary terms and gives no additional scalar event condition by itself. That scoped comparison leaves other transformed estimates open.

For Jensen work, preserving one spectral value is insufficient. Show that the transformation preserves the required moment entries or the complete determinant integral, with any spectral differentiation and integration justified. Alternatively, prove an explicit comparison strong enough for the intended sign conclusion.

## First bounded question

Choose one paired deformation, beginning with the existing Darboux family as a candidate, and one consumer such as D_{4,1}. Identify the actual transformed expression and its endpoint terms. Select one estimate that becomes better or structurally simpler, and compare it with its pullback to the original variables using the same information.

**Completion:** one explicit transfer and a concrete improved estimating problem, or a scoped reason the selected deformation provides no gain. Transporting an unchanged identity or discarding the transformed forcing does not meet the completion test. A new generator, observation, or numerical campaign requires its own bounded contract.

## Connections and reading

- [Note14, Section 5](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) distinguishes complete-density evolution from source-and-test evolution.
- [Negative-mass flows](../03_conservative_negative_mass_flows/README.md) can consume a better signed density or dissipation estimate.
- [Signed averaging](../../02_signed_averaging/README.md) can consume a more tractable observable only with all required tilted expectations preserved or compared.
- [Order induction](../../01_mellin_curvature/README.md) can consume an improved bound on the complete neighboring-index balance.

## Organization

Save new derivations in this folder. Put computations and small records in the matching `01_jensen/numerics/04_paired_source_test_deformations/` subfolder and assessments in `01_jensen/reviews/04_paired_source_test_deformations/` when first needed. Keep one canonical source for reusable results and link applications. Existing numbered notes and this chat’s registration keep their current locations.

[Ideas index](../../../ideas/README.md) · [Common assessment](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) · [Live register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md)

## Initial evaluation, 1 November 2026

[The bounded return](01_INITIAL_BRANCH_EVALUATION_20261101.md) is complete. All required Darboux moments are preserved. For the selected absolute-residual coefficient-box estimate, the direct bound dominates the transformed one.
Prepared for Edward Baker with substantial LLM assistance, actual gpt-6-astra / ultra. [Coordinator Review02](../../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md) records the comparison and internal same-model review limits. The sole live register owns task status; next actions in the return are recommendations.
