# Determinant order induction

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Organization task J-E04.

The question is whether an inequality between neighboring coefficient indices can propagate determinant positivity from order r to order r+1.

**Research task: J-B06, B — Astra.** Selecting a usable log-concavity estimate is the conceptual step. The [sole progress register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns status; this brief records the proposed direction and its limits.

## Target and exact identity

For \(D_{r,k}=\det[c_{k+j-i}]\), with \(c_j=0\) for j<0, the Desnanot–Jacobi identity gives
\[
D_{r+1,k}D_{r-1,k}=D_{r,k}^2-D_{r,k-1}D_{r,k+1}.
\]
When \(D_{r-1,k}>0\), strict log-concavity in k of \(D_{r,k}\) would imply positivity at the next order. The index-zero anchor is triangular; the substantive small-index problem begins at k=1.

Using \(D_{r,k}=Z_{r,k}A_{r,k}/F_{r,k}\), for k>=1 the exact balance is
\[
\frac{D_{r,k}^2}{D_{r,k-1}D_{r,k+1}}
=\frac{A_{r,k}^2}{A_{r,k-1}A_{r,k+1}}
 \frac{Z_{r,k}^2}{Z_{r,k-1}Z_{r,k+1}}
 \frac{F_{r,k-1}F_{r,k+1}}{F_{r,k}^2}.
\]
The Z sequence is log-convex as a positive moment sequence. The factorial factor favors the other direction. The accepted monotonicity of A at order three does not control the full product.

## First bounded question

Use r=3 as a mechanism pilot and identify one concrete estimate on the complete normalized balance that would imply the required strict inequality for k>=1, including k=1. State whether its proof can be expressed with constants depending on arbitrary order r. Do not replace a mixed expression by separately positive pieces or assume the sign of the next determinant.

**Completion:** a selected estimate with its source, hypotheses, index range, and order dependence; a proof or scoped failed comparison; or an exact missing obligation and bounded follow-up contract. Deriving the determinant identity alone does not complete a positivity argument. An order-four consequence would test a method, not enlarge the known coefficient range.

## Connections and reading

- [Note14, Section 3](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) gives the identity and normalization comparison.
- [Note05](../05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md) defines the order-three signed average and positive measure.
- [Signed averaging](../01_higher_order_signed_averaging/README.md) may supply information about A, but its increasing-index theorem is not log-concavity of D.
- [Paired deformations](../04_paired_source_test_deformations/README.md) can be useful only if they improve the complete comparison after all normalization and boundary terms are retained.

## Organization

Save new derivations in this folder. Put computations and small records in the matching `jensen/numerics/02_determinant_order_induction/` subfolder and assessments in `jensen/reviews/02_determinant_order_induction/` when first needed. Keep one canonical source for reusable results and link applications. Existing numbered notes and this chat’s registration keep their current locations.

[Ideas index](../../../ideas/README.md) · [Common assessment](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) · [Live register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md)
