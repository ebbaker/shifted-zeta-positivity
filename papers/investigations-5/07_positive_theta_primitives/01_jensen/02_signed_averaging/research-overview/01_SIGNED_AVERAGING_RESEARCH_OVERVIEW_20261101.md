# Research overview for integrated signed averaging

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Documentation task **J-E08**; no mathematical execution.

The objective is to compare complete signed determinant averages across coefficient indices while allowing regions where the observable decreases. The first question is order four, index zero to index one. The earlier pointwise monotonicity hypothesis fails for canonical theta; the integrated comparison remains open.

**Next task: J-B11, B — recommended Astra.** This is a new conceptual task following completed J-B05. The first decision is a specific theta relation capable of controlling the complete covariance. The [research plan](../research-plan/01_SIGNED_AVERAGING_RESEARCH_PLAN_20261101.md) defines the bounded assessment; the [continuation note](../notes/02_CONTINUATION_SIGNED_AVERAGING_20261101.md) is the session entry point. The author has selected this direction for its own parallel run, so it need not wait for J-B10.

## Mathematical destination and representation

Keep the complete canonical theta source at physical time zero and use
\[
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,\qquad
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},\qquad c_n=0\ (n<0).
\]
Raw moments, ordinary coefficients \(c_n\), and exponential coefficients \(\gamma_n=n!c_n\) must remain distinct. The [parent program](../../README.md) states the full Jensen and coefficient-total-positivity destinations.

Write \(R=\Phi''/\Phi\), \(x_j=R(u_j)\), and \(g_i=(\Phi^{(2i)}/\Phi)\circ R^{-1}\). On \(\Omega_r=\{0<u_1<\cdots<u_r\}\),
\[
h_r=\frac{\det[g_i(x_j)]_{i=0}^{r-1}}{V(\mathbf x)},\qquad
w_{r,k}=\Bigl(\prod_{j=1}^r u_j^{2k}\Phi(u_j)\Bigr)
V(\mathbf u^2)V(R(\mathbf u)).
\]
With \(Z_{r,k}=\int_{\Omega_r}w_{r,k}>0\), the normalized signed average is
\[
A_{r,k}=E_{r,k}h_r=\frac{F_{r,k}D_{r,k}}{Z_{r,k}},\qquad
F_{r,k}=\prod_{j=0}^{r-1}(2k+2j)!.
\]
The carrier is positive by the accepted \(R'>0\); the observable may be negative. Removable coincident-node limits, full evenness at the origin and complete tails are part of the representation in [Note14](../../notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md).

## Established baseline and the scoped failure

[Review01](../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md) accepts \(R'>0,K>0\) and normalized index monotonicity at order three, with internal same-model review. This does not establish order-four coordinatewise monotonicity.

The [completed J-B05 assessment](../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md) proves that unchanged canonical \(h_4\) has a negative fourth-coordinate derivative when three nodes stay in an origin-side region and the fourth is sufficiently distant. Its proof retains the negative origin curvature and uses the exact finite tail calculation. The finding refutes full pointwise increase; it does not establish a negative covariance, a negative determinant, or failure of every signed-averaging argument.

The positive starting value survives:
\[
D_{4,0}=c_0^4,\qquad A_{4,0}=\frac{F_{4,0}c_0^4}{Z_{4,0}}>0.
\]
This triangular anchor is not all-degree Jensen hyperbolicity at shift zero.

## The complete comparison to investigate

Let \(q=\prod_{j=1}^4u_j^2\). The exact change-of-weight identity is
\[
A_{4,1}-A_{4,0}=
\frac{\operatorname{Cov}_{4,0}(h_4,q)}{E_{4,0}q}.
\]
The default sufficient target is a theta-dependent proof that this full covariance is nonnegative. It would transfer the positive anchor and establish a normalized-index comparison at the pilot. It remains unproved. Here “integrated” refers to the full node integral; a continuous index interpolation is not required by this discrete identity.

An estimate allowing some negative covariance could instead preserve positivity by paying for that loss from the anchor. That is a changed comparator and must be identified explicitly. Merely rewriting \(A_{4,1}>0\) as a lower bound on the covariance restates the desired determinant sign. The needed gain is an independently justified quantitative estimate, not the reformulation.

The main challenge is to retain cancellation between favorable and unfavorable configurations, including the proved negative-derivative region. A diagonal test, a tail-only argument, a deletion of negative values, or generic association cannot replace that accounting.

## What would count as progress

The bounded task selects one named theta relation, works through one complete comparison or a precisely scoped failure, and records what remains. If no specific additional input can be justified, the return must explain the information gap rather than proceed to a scan. Any partial estimate must retain the unestimated remainder and say whether it can pay the anchor.

Known order-four positivity makes this a mechanism pilot. The result would not by itself handle all indices, arbitrary determinant order, or RH. Extending to further indices would need new comparisons; extending to higher order would need new source-sensitive estimates. This task does not assume that the parallel Mellin-curvature investigation succeeds.

## Background

- [Note05](../../notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md): the accepted architecture allowing signed observables.
- [Note14, Sections 2–3](../../notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md): general integral, positive anchor and covariance identity.
- [J-B05 return](../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md): canonical obstruction, exact support, endpoints, tails and control screen.
- [Comparative Review02](../../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md): the integrated follow-up and limits of the other tested mechanisms.

## Evidence and research standards

Use the [result index](../../../../../../result-summaries/README.md), especially [theta identities](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), with the [avoid index](../../../../../../avoid/README.md), especially [target reformulation](../../../../../../avoid/01_restating_the_target.md), [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [joint signed estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). Keep the source's status words and internal-review qualifications. An identity, a sufficient conjecture, a numerical observation and a proved estimate are different outputs.

The [common reference catalog](../../../references/README.md) retains inspection limits. Inspect a primary source before importing a new theorem and record the relevant hypotheses and checked passages. A broad literature survey or certificate replay is not needed merely to start this question.
