# Jensen formulation and coefficient positivity

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**.

**Current research:** [J-E03 Review01](reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md) accepts the complete canonical source pair R'>0,K>0 for u>0 and the normalized order-three index comparison. The fixed certificate replay and full coverage/error checks pass without correction. The original J-B01–J-E03 sequence is complete; [Continuation13](notes/13_CONTINUATION_AFTER_J_E03_ACCEPTED_ASSESSMENT_20261101.md) preserves the stopping boundary and model guidance. This remains same-assistant/same-model internal assessment, with no independent specialist review. The r1 negative origin C is unchanged. Assessment: 1 November 2026, gpt-6.1-sol / ultra.

**Status:** canonical global source-sign certificate and normalized index comparison at fixed order three, accepted by internal J-E03 assessment. No new coefficient range, increasing-order argument or RH conclusion is established here. This program and the [spectral Laguerre program](../02_spectral_laguerre/README.md) guide the shared tool development described in the [investigation README](../README.md).

**Numbered research directions:** [01 Mellin curvature](01_mellin_curvature/README.md) develops order induction through the complete signed Mellin-curvature comparison; [02 Signed averaging](02_signed_averaging/README.md) develops the integrated alternative after the order-four pointwise obstruction. Each has notes, numerics, reviews and research-navigation folders. The remaining three assessed approaches stay under [notes](notes/README.md). The [ideas index](../ideas/README.md) preserves the five original branch identities, and the [sole register](research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns all J-task statuses. Folder promotion: J-E07, 1 November 2026, actual **gpt-6-astra / xhigh**, for Edward Baker with substantial LLM assistance.

## Goal and exact formulation

Use the [common normalization](../README.md#common-mathematical-normalization):
\[
b_n=\int_0^\infty u^{2n}\Phi(u)\,du,\qquad
c_n=\frac{b_n}{(2n)!},\qquad \gamma_n=n!c_n.
\]
For integers \(d,n\ge0\), define
\[
J_\gamma^{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}X^j.
\]
The classical Jensen criterion says that RH is equivalent to every such polynomial having only real zeros. All degrees at shift \(n=0\) already suffice. This is the fixed mathematical destination, not a new criterion or a claim of progress. See [Griffin–Ono–Rolen–Zagier, Introduction](https://arxiv.org/html/1902.07321v1) and the [shared formulation note](../notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md).

Coefficient total positivity is a complementary way to attack the same real-zero problem. For
\[
F(w)=\sum_{n\ge0}c_nw^n,
\]
RH is equivalent to the Pólya-frequency property \((c_n)\in\mathrm{PF}_\infty\): every finite minor of the one-sided Toeplitz matrix \([c_{j-i}]_{i,j\ge0}\) is nonnegative, with \(c_k=0\) for \(k<0\). The consecutive minors
\[
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1}
\]
provide a useful family to study. The theorem passing from a selected family to all minors must retain its strictness and other hypotheses. [Katkova's account](https://arxiv.org/html/math/0505174v1) and the [shared source records](../references/04_RH_FORMULATION_SOURCES_20261101.md) give the relevant distinctions.

The ordinary coefficients \(c_n\), exponential coefficients \(\gamma_n\) and raw moments \(b_n\) must remain distinct. In particular, positivity of raw moment Hankel matrices is automatic for a positive source and does not prove the required coefficient condition. The determinant formulation is a tool within this program, not a third separately organized proof route.

## What the existing tools contribute

CNV's normalized-moment argument proves the quadratic Jensen cases through determinant composition. Source concavity of \(S(x)=\Phi(\sqrt x)\) and of \(\mathcal L[S]\) has a known transfer to ordinary and double Turán inequalities. These give examples of successful sign transfer, not the whole arbitrary-degree criterion.

Jacobi differential closure supplies exact relations among theta derivatives. Primitive integration by parts supplies exact moment transfers with boundary terms. Joint algebra and analytic tails can retain correlations lost by independent absolute bounds. The open issue is whether these methods give coefficient inequalities that remain useful as the degree or determinant order grows.

The baseline includes fixed-degree large-shift Jensen results and fixed-order asymptotic multiple positivity. The July2026 coefficient-tail preprint reports a uniform region \(k\ge10^{18}r^3\), but its proof and certificates remain unaudited here. The [reference index](../references/README.md) and [strategy note](../notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md) retain the versions, quantifiers and limitations. A future estimate must specify what it adds to that baseline; reproducing a known low-order case is a validation step when it tests a method intended to extend further.

## Questions for the first detailed notes

1. **Which coefficient family should carry the argument?** Compare an exact representation of Jensen polynomials with one of coefficient minors. Identify the sign information, convergence requirements and normalization each representation needs.
2. **What survives integration?** Determine whether the Jacobi relations or modular identities yield a usable relation among normalized moments or complete determinants, rather than only relations among source derivatives at one point.
3. **Where can a new estimate work?** State a domain in degree and shift, or determinant order and index. Explain whether the mechanism treats a new region, improves a proved bound, or supplies a structural relation uniform in order. The small-shift, increasing-degree regime must remain visible.
4. **Which information is specifically theta?** Separate arguments valid for every positive source from those using the canonical theta identities or coefficients. Screen any proposed sufficient estimate against the applicable controls with its actual hypotheses.

These are questions to investigate, not adopted positivity claims. A representation that merely renames an unknown sign should be recorded as an identity, with the missing estimate exposed.

## Requests to the shared tools program

Useful requests may concern determinant-composition hypotheses, exact boundary-preserving moment identities, a recurrence that retains mixed terms, or an analytic tail estimate uniform in the route's parameters. Each request should link to the consuming formula and state its range, baseline and intended gain. General tools belong in the shared [notes](../notes/README.md) or [numerics](../numerics/README.md); their application and limitations belong here.

The [spectral route](../02_spectral_laguerre/README.md) may expose a different use of the same source identity. A result is transferred between the routes only through an explicit implication with the correct normalization; a shared word such as positivity does not identify the two problems.

## Files and intended outputs

Shared Jensen derivations remain indexed in [notes](notes/README.md), with shared calculations in [numerics](numerics/README.md) and shared assessments in [reviews](reviews/README.md). New work specific to either promoted direction uses that direction’s own notes, numerics and reviews folders. Route-specific [chat provenance](chat-histories/README.md) is separate from the existing cross-route archive. Keep one common [reference catalog](../references/sources.json) and link route uses there. The existing shared notes stay at their present paths.

The [initial research overview](research-overview/01_JENSEN_RESEARCH_OVERVIEW_20261101.md) states the criterion, known baseline, candidate mechanisms and bounded research contracts. The matching [progress register](research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns live task status and dated returns. The first decision note preserves the selected mechanism and frozen execution request. The completed r1 audit supplies an exact obstruction to its required curvature sign. The revised signed-averaging decision and frozen r2 audit preserve that obstruction while testing a different sufficient condition.

Read the [result index](../../../../result-summaries/README.md), especially [theta identities](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../../result-summaries/12_collision_controls_and_screening.md), alongside the [avoid index](../../../../avoid/README.md), especially [reformulations](../../../../avoid/01_restating_the_target.md) and [separate bounds](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). Finite computations support their stated finite conclusions; they become an all-degree argument only with a proved mechanism covering the remaining range.

## Five-branch evaluation

1 November 2026; prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra / ultra** throughout. [Comparative Review02](reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md) checks all five saved assessments. It records an actual canonical obstruction to unchanged h4 coordinatewise monotonicity, a still-open signed order-induction bound, and scoped flow/deformation comparisons. The accepted order-three baseline and negative origin curvature remain unchanged; no new canonical coefficient range is claimed. **Next recommended: [B] J-B10 — Astra**, the complete signed Mellin-curvature comparison in the [live register](research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md).

The [next-session continuation](notes/16_CONTINUATION_BRAINSTORM_AFTER_PARALLEL_REVIEW_20261101.md) prepares brainstorming about J-B10, with room to compare one concrete alternative before selecting a bounded estimate. Preparation: J-E06, documentation only, 1 November 2026, actual **gpt-6-astra / ultra**; no new mathematical assessment.

## Separate parallel continuations: historical preparation

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, actual **gpt-6-astra / xhigh**. Preparation task **J-E08**, documentation only.

The author will run both promoted directions independently: [J-B10 Mellin curvature](01_mellin_curvature/notes/02_CONTINUATION_MELLIN_CURVATURE_20261101.md) and [J-B11 Integrated signed averaging](02_signed_averaging/notes/02_CONTINUATION_SIGNED_AVERAGING_20261101.md). Each has a research overview and issued plan linked from its continuation note. Both are ready for B/Astra conceptual work and remain unstarted; no E campaign is issued. The [sole register](research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns status. The two plans specify disjoint outputs and a common lock for narrow shared updates.

## Mellin physical assessments completed

1 November 2026, for Edward Baker with substantial LLM assistance; coordinator gpt-6-astra / ultra, separate reviews gpt-6.1-sol / ultra.

The [six-direction assessment](01_mellin_curvature/reviews/01_PARALLEL_PHYSICAL_DIRECTIONS_ASSESSMENT_20261101.md) and [Synthesis06](01_mellin_curvature/notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md) record accepted exact physical formulations and scoped failures, with no new Gaussian comparison domain. The [canonical register](research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) records J-B10 packet completion and the still-open quantitative objective. J-B11 remains independent; earlier launch descriptions above are historical.
