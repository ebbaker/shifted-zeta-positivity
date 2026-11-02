# Integrated signed averaging

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Folder setup: **J-E07**, organization only.

This direction asks whether the complete signed determinant average can be compared across coefficient indices even when its integrand is not increasing everywhere. The first proposed test is determinant order four, from index zero to index one, retaining both the positive anchor and the regions where local derivatives are negative.

**Current position:** the earlier order-four pointwise monotonicity mechanism is disproved for the canonical theta observable. The [initial assessment](notes/01_INITIAL_BRANCH_EVALUATION_20261101.md) establishes that scoped obstruction; it does not refute an averaged comparison or determinant positivity. A new theta-specific signed estimate is needed. [Review02](../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md) retains this as the alternative to [signed Mellin-curvature order induction](../01_mellin_curvature/README.md).

## Parallel session documents

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, actual **gpt-6-astra / xhigh**. Preparation task **J-E08**, documentation only.

The author has selected this direction for its own parallel session. Start with the [continuation note](notes/02_CONTINUATION_SIGNED_AVERAGING_20261101.md), then the [research overview](research-overview/01_SIGNED_AVERAGING_RESEARCH_OVERVIEW_20261101.md) and [research plan r1](research-plan/01_SIGNED_AVERAGING_RESEARCH_PLAN_20261101.md). **J-B11 is ready for conceptual work and unstarted.** The sibling task is independent; the plans define separate file ownership and serialized shared-register updates. These packets supersede the earlier choice-between-directions instruction for this launch, while preserving all mathematical cautions.

## Problem and inherited representation

Keep the complete canonical theta source at physical time zero and set
\[
c_n=\frac{1}{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,
\qquad D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},\qquad c_n=0\ (n<0).
\]
These ordinary coefficients differ from raw moments and from \(\gamma_n=n!c_n\). The [Jensen program](../README.md) records their role in coefficient total positivity and real-rooted Jensen polynomials.

The accepted global source sign \(R'>0\), where \(R=\Phi''/\Phi\), gives the positive carrier on the ordered chamber \(\Omega_r=\{0<u_1<\cdots<u_r\}\):
\[
w_{r,k}=\Bigl(\prod_{j=1}^r u_j^{2k}\Phi(u_j)\Bigr)
V(\mathbf u^2)V(R(\mathbf u)),\qquad Z_{r,k}=\int_{\Omega_r}w_{r,k}.
\]
Here \(V\) is the Vandermonde product. With \(x_j=R(u_j)\) and \(g_i=(\Phi^{(2i)}/\Phi)\circ R^{-1}\), the signed observable and its average are
\[
h_r=\frac{\det[g_i(x_j)]_{i=0}^{r-1}}{V(\mathbf x)},\qquad
A_{r,k}=E_{r,k}h_r=\frac{F_{r,k}D_{r,k}}{Z_{r,k}},\quad
F_{r,k}=\prod_{j=0}^{r-1}(2k+2j)!.
\]
The removable coincident-node limits, endpoint cancellations and complete tails belong to the representation. The observable may be negative; the carrier is positive.

## What the order-three result supplies and where extension fails

[Review01](../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md) accepts the canonical global pair \(R'>0,K>0\) and the resulting normalized index comparison at order three. Signed averaging permits the negative origin curvature that defeated an earlier pointwise source-convexity argument. This remains internal same-model assessment.

At order four, the unchanged \(h_4\) has a negative fourth-coordinate derivative when three nodes lie in an origin-side region and the fourth is sufficiently distant. This is an actual canonical obstruction to full coordinatewise increase, not an abstract control. The proof and its small exact P0–P7 calculation are preserved in the [initial return](notes/01_INITIAL_BRANCH_EVALUATION_20261101.md) and [numerics](numerics/README.md).

The negative derivative does not determine the complete covariance. An averaged estimate must explicitly allow this region. Neither a diagonal derivative check nor ignoring the negative part repairs the failed premise.

## The first integrated comparison

For \(q=\prod_{j=1}^4u_j^2\), the exact change-of-weight identity from [Note14](../notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) reads
\[
A_{4,1}-A_{4,0}
=\frac{\operatorname{Cov}_{4,0}(h_4,q)}{E_{4,0}q},
\qquad A_{4,0}=\frac{F_{4,0}c_0^4}{Z_{4,0}}>0.
\]
The initial question is to obtain a theta-specific bound for this complete signed covariance, with all tails and the positive anchor retained. A nonnegative covariance would carry the anchor forward; that sufficient comparison remains unproved. A weaker estimate that spends part of the positive anchor would be a changed comparison and must be identified explicitly. Writing down the covariance condition alone is not progress toward it.

This is a fixed-order, first-index mechanism pilot within known order-four positivity. Success would not by itself settle every index, increasing determinant order, all-degree Jensen hyperbolicity, or RH. In particular, the triangular \(D_{r,0}=c_0^r\) identity is not all-degree Jensen hyperbolicity at shift zero.

## Next bounded question

**J-B11 — B, recommended Astra:** first name a concrete signed theta identity that controls the complete covariance beyond the failed pointwise assumptions. The author has selected a separate parallel session; J-B11 is now registered as ready and unstarted in the [sole Jensen register](../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md). Completed J-B05 retains its original identity. The new plan defines the bounded assessment; document preparation does not execute it.

Return one worked bound or scoped failure for \(r=4,k=0\to1\), explaining the origin, separated and coincident nodes, full tails, and positive-anchor accounting. Stop if the proposed estimate assumes the same covariance sign it must prove, reinstates unchanged-\(h_4\) pointwise monotonicity, or deletes its negative region. Numerical acquisition requires a separate fixed E contract.

## Background and reading order

1. [Note05](../notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md) and [accepted Review01](../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md): the successful order-three architecture and its scope.
2. [Note14, Sections 2–3](../notes/14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md): general integral, normalized averages, positive anchor and covariance identity.
3. [Initial assessment](notes/01_INITIAL_BRANCH_EVALUATION_20261101.md): canonical separated-node obstruction, exact support, endpoint/tail obligations and control screen.
4. [Review02](../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md) and [Continuation16](../notes/16_CONTINUATION_BRAINSTORM_AFTER_PARALLEL_REVIEW_20261101.md): the integrated alternative and its priority conditions.

Consult the [result index](../../../../../result-summaries/README.md), especially [theta identities](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../../result-summaries/12_collision_controls_and_screening.md), with the [avoid index](../../../../../avoid/README.md), especially [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [joint signed estimates](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). Gaussian equality checks normalization; collision controls do not establish an uncomputed covariance sign. A changed premise requires a claim-specific control screen.

## Folder organization

| Folder | Use |
| --- | --- |
| [notes](notes/README.md) | Preserved initial brief, completed J-B05 obstruction, and future numbered derivations. Continuation02 is the session entry point; the next research return is 03. |
| [numerics](numerics/README.md) | The existing finite tail checker and exact record; future small support under fixed contracts. |
| [reviews](reviews/README.md) | Direction-specific assessments; the comparative reviews remain at Jensen level. |
| [research-overview](research-overview/README.md) | Navigation to this problem statement and the common Jensen overview. |
| [research-plan](research-plan/README.md) | Issued bounded research plan; live status stays in the Jensen register. |
| [research-progress](research-progress/README.md) | Pointer to the sole live Jensen task register. |
| [references](references/README.md) | Pointer to the investigation's common bibliography and source catalog. |
| [chat-histories](chat-histories/README.md) | Future chats devoted to this direction, using their actual identities. |

Historical branch01 is now housed here. Its initial brief remains historical; this README states the integrated continuation after the pointwise failure. Existing Jensen chats stay in the [parent archive](../chat-histories/README.md). The [organization record](../notes/17_NUMBERED_RESEARCH_FOLDERS_20261101.md) maps old paths to current homes without changing the earlier mathematical conclusions.
