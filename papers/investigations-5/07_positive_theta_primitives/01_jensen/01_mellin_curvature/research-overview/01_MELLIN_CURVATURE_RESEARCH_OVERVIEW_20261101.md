# Research overview for order induction through signed Mellin curvature

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Documentation task **J-E08**; no mathematical execution.

The objective is a quantitative estimate that can raise the order of coefficient-determinant positivity. The first test uses the accepted order-three theta results to study an order-four implication. Its main unresolved issue is the complete signed logarithmic curvature of a Mellin integral. The proposed Gaussian upper bound remains unproved.

**Current continuation:** [Synthesis06](../notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md), following the [completed six-direction assessment](../reviews/01_PARALLEL_PHYSICAL_DIRECTIONS_ASSESSMENT_20261101.md). Exact physical formulations and scoped obstructions have separate cross-model internal checks; no new Mellin comparison domain is proved. Primary MC03-B02 and deferred physical fallback MC05-B02 are unstarted. 1 November 2026, for Edward Baker with substantial LLM assistance; coordinator gpt-6-astra / ultra, separate reviews gpt-6.1-sol / ultra.

The earlier [research plan r1](../research-plan/01_MELLIN_CURVATURE_RESEARCH_PLAN_20261101.md) is preserved as issued and is historical for this newly requested six-direction launch. J-B11 remains a separate signed-averaging investigation. Neither its unfinished work nor an unfinished physical branch is an assumed input to another branch.

## Mathematical destination and accepted starting point

For the complete canonical source at physical time zero, use
\[
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,\qquad
\gamma_n=n!c_n,\qquad D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},
\quad c_n=0\ (n<0).
\]
The [parent program](../../README.md) explains the full Jensen and coefficient-total-positivity formulations. A selected finite-order determinant result does not establish that full criterion.

[Review01](../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md) accepts the global source pair \(R'>0,K>0\) and normalized order-three index comparison at internal same-model review scope. The negative origin curvature is retained. The [initial J-B06 assessment](../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md) extends the order-three signed-averaging argument to real nonnegative tilts, giving positive \(A(s)\) and \(M(s)\). It also supplies the exact factorial budget and Gaussian normalization.

For \(q=\prod_{j=1}^3u_j^2\), \(T=\log q\), \(w_s=q^sw_0\), \(Z(s)=\int w_s\), \(d\mu_s=w_s/Z(s)\), and \(h=h_3\), put
\[
A(s)=E_s h,\qquad M(s)=Z(s)A(s),\qquad
M(k)=F_{3,k}D_{3,k},\quad F_{3,k}=(2k)!(2k+2)!(2k+4)!.
\]
The positive carrier is \(w_0=(\prod_j\Phi(u_j))V(\mathbf u^2)V(R(\mathbf u))\) on the ordered chamber. The signed observable and removable-node conventions are in [Note14](../../notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md). The integer endpoint identity does not assert a noninteger Toeplitz formula.

## The remaining quantitative question

The exact curvature is
\[
\mathcal C_3(s)=(\log M)''(s)
=\operatorname{Var}_s(T)
+\frac{\operatorname{Cov}_s(h,(T-E_sT)^2)}{A(s)}
-\left(\frac{\operatorname{Cov}_s(h,T)}{A(s)}\right)^2.
\]
The selected sufficient estimate is
\[
\mathcal C_3(s)\le\kappa_3(s)
:=\sum_{j=0}^2\sum_{\nu\ge0}(s+j+\tfrac12+\nu)^{-2},\qquad s\ge0.
\]
Writing \(Q_{3,k}=M(k-1)M(k+1)/M(k)^2\), this would imply
\[
Q_{3,k}\le G_{3,k}=\frac{2k+5}{2k-1},\qquad
D_{4,k}\ge\frac3{k+3}\frac{D_{3,k}^2}{D_{2,k}}>0,\qquad k\ge1.
\]
Given the positive lower-order inputs, the weaker exact condition
\(Q_{3,k}<B_{3,k}=(2k+6)(2k+5)/(2k(2k-1))\) is just the next determinant's sign condition. It is not a newly acquired estimate. The pointwise Gaussian bound implies the integrated Gaussian bound, which implies this exact sign condition. Failure of a stronger bound leaves weaker approaches open.

Positive association controls neither the centered-square covariance nor the complete curvature. The initial return's two-point relaxation defeats an association-only inference; it does not realize canonical theta or a Toeplitz counterexample. Gaussian equality is a normalization check. Any useful new input must supply information beyond those retained assumptions and preserve signed cancellation.

## What would count as progress

An explicit theta-dependent bound on the complete expression, a proved failure of a chosen sufficient comparison, or a precise identification of the surviving uncontrolled term would complete the bounded assessment. A partial-domain result must identify its remainder. Repeating the exact sign condition or bounding only the carrier variance does not settle the question.

The required global domain includes \(s\in[0,2]\) for \(k=1\), all intervening values, and an analytically controlled unbounded tail. Known order-four positivity makes this a method pilot. Arbitrary-order induction would require new estimates for every finite order and, for continuous interpolation, the appropriate real-parameter positivity. The canonical order-four pointwise obstruction prevents simply assuming that the order-three argument repeats.

## Background

- [Note05](../../notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md): signed averaging with a negative source region.
- [Note14](../../notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md): determinant representation, anchors and order-raising identities.
- [J-B06 return, Sections 2–5](../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md): exact budget, signed two-copy formula, curvature, controls and tails.
- [Comparative Review02](../../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md): checked scope and rationale for prioritizing this estimate.

## Evidence and research standards

Use the [result index](../../../../../../result-summaries/README.md), especially [theta identities](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), with the [avoid index](../../../../../../avoid/README.md), especially [target reformulation](../../../../../../avoid/01_restating_the_target.md), [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [joint signed estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). Keep the source's status words and internal-review qualifications. An identity, a sufficient conjecture, a numerical observation and a proved estimate are different outputs.

The [common reference catalog](../../../references/README.md) retains inspection limits. Inspect a primary source before importing a new theorem and record the relevant hypotheses and checked passages. A broad literature survey or certificate replay is not needed merely to start this question.
