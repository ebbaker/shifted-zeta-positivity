# Jensen formulation and coefficient positivity: research overview

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **xhigh**.

**Status: initial research overview and plan.** This route asks how exact
theta information can yield coefficient inequalities strong enough for
all-degree Jensen hyperbolicity. No new hyperbolicity theorem is established
here. The [Jensen progress register][j-progress] owns all J-task status.
The [overall overview][base-overview] owns shared-method planning.

## Mathematical destination

Use the [common normalization](../../README.md#common-mathematical-normalization):
\[
b_n=\int_0^\infty u^{2n}\Phi(u)\,du,\qquad
c_n=\frac{b_n}{(2n)!},\qquad\gamma_n=n!c_n.
\]
The Jensen polynomials are
\[
J_\gamma^{d,n}(X)=\sum_{j=0}^{d}\binom dj\gamma_{n+j}X^j.
\]
RH is equivalent to their hyperbolicity for every degree and shift.
All degrees at shift zero already suffice. This classical criterion,
recorded with sources in the [formulation note][formulations], is the
destination rather than a new intermediate theorem.

A complementary representation uses \(F(w)=\sum c_nw^n\).
RH is equivalent to \((c_n)\in\mathrm{PF}_\infty\): all finite minors of
\([c_{j-i}]_{i,j\ge0}\) are nonnegative, with \(c_k=0\) for \(k<0\).
Consecutive minors
\[
D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1}
\]
may be a convenient proving family, but passage from selected minors to
the full condition requires an applicable theorem with its strictness
and other hypotheses. The ordinary c sequence and exponential gamma
sequence are not interchangeable. Neither condition follows from
positivity of raw moment Hankel matrices, which a positive source already
provides.

Coefficient total positivity remains a method within the Jensen program.
The initial choice is which representation exposes the most useful
estimating problem; the organization does not predetermine that choice.

## Literature baseline and the difficult range

The [literature note][foundation], [closure note][closure] and
[reference index][references] supply the initial baseline:

| Available result or technique | What it provides | What remains |
| --- | --- | --- |
| CNV normalized-moment determinant composition | Quadratic Jensen/Turán inequalities from suitable source information | An argument that extends to the chosen higher-order family |
| Source concavity of S and of its first Laguerre transform | Known ordinary and double Turán consequences under the cited hypotheses | A transfer theorem for the full required coefficient family |
| Fixed-degree, large-shift Jensen asymptotics | Hyperbolicity in an eventual shift range for each fixed degree | Uniform treatment of growing degree and the omitted low shifts |
| Katkova's multiple-positivity framework | Coefficient total positivity and fixed-order asymptotic results | An effective sign mechanism covering the remaining minors |
| July2026 coefficient-tail preprint | Reported region \(k\ge10^{18}r^3\) | Proof/certificates not audited here; the complementary region remains outside that stated result |

The last row is a recorded preprint claim, not an adopted lemma.
Recent source-Hankel determinant statements concern a different object
from coefficient Toeplitz minors. Their relevance must be proved through
a transfer, not inferred from the word determinant.

A finite collection of low-degree successes, or a larger verified shift
range for fixed degree, has its stated scope. The complete route needs
all degrees, or a theorem reducing them to an explicitly sufficient
family. In particular, the small-shift, increasing-degree regime cannot
disappear from the plan.

## Candidate mechanisms and shared tools

The first comparison is between a direct integral representation of the
Jensen family and a determinant representation of ordinary coefficients.
For each, identify the complete signed expression before estimating it.
CNV's method suggests that determinant composition can transfer source
signs, but its order-two success does not supply all higher-order
hypotheses.

Jacobi differential algebra may organize derivatives appearing in the
integrand. Primitive integration by parts may change moment weights while
retaining exact endpoints. Modular identities and joint remainder bounds
may retain cancellations lost by termwise estimates. Each is a candidate
tool, not a proved sign mechanism after integration.

A request to [shared work][base-overview] must identify the coefficient
family, the degree/order and shift/index range, the precise formula, the
known baseline and the desired improvement. If the required relation
does not close, list the new mixed quantities rather than discarding them.

## Research contracts

The [model workflow][workflow] classifies work before execution.
The progress register holds readiness; the contracts below define scope.

| ID | Type and recommendation | Dependency | Deliverable and completion condition |
| --- | --- | --- | --- |
| J-B01 | B — Astra; choose the coefficient representation and a plausible sign mechanism | Existing shared foundation | Compare at most two representations initially, or two revised mechanisms after a scoped failed premise. Return one selected family, its exact target/domain, candidate transfer, baseline and first unresolved estimate; or a scoped reason neither is ready. |
| J-E01 | E — Sol; carry out a fixed normalization and transfer audit | J-B01 selects the representation and issues a bounded derivation request | Audit the selected representation or transfer with its normalization, convergence, boundaries, one declared baseline and imported theorem hypotheses; perform only the source feasibility tests explicitly frozen in the request. Return a complete identity/baseline note or a precise failed step. |
| J-B02 | B — Astra; resolve the missing higher-order sign or uniformity mechanism | J-E01 return, plus any explicitly needed shared result | Address one named missing estimate. Return a proof, a fixed execution contract, or a scoped obstruction. State what changes relative to the literature and how the domain relates to all-degree coverage. |
| J-E02 | E — Sol; prove or acquire the specified consequence | A tractable J-B02 contract | Complete one request revision with its prescribed lemmas or finite cases, error/tail payments and work limits. Record failures as well as successes; no automatic widening of the range. |
| J-E03 | E — Sol; assess a fixed claim and its implication | A versioned J-E02 return or complete analytical J-B02 proof | Check normalization, theorem imports, controls and claimed coverage. Save one assessment with review relationship, corrections and remaining obligations; update the route's evidence links and live register. |

J-E01 returns to J-B01 if the chosen representation requires a different
mechanism. J-E02 returns to J-B02 for an unproved structural premise or
an exhausted request that needs a different approach. A complete analytical
J-B02 argument can go directly to J-E03; a numerical stage is optional.
Execution requests must freeze cases/lemmas, method, limits and acceptance
before dependent work starts.

## Evidence and success criteria

The first baseline derivation is validation, not novelty. A substantive
return should prove a new applicable transfer or estimate, improve a stated
range, or explain precisely why one proposed mechanism fails. If it only
rewrites an unknown determinant sign, retain the identity and name the
missing estimate without claiming a positivity advance.

Use the [result index][results], particularly [theta identities][theta]
and [controls][controls], with the [avoid index][avoid]:
[reformulations][reformulations], [shape-only premises][shape],
[separate bounds][joint], [scoped exclusions][scopes] and
[unchecked imports][imports]. Proposed sufficient claims need their
actual control checks before promotion. The source-concavity diagnostic
in [Note03][formulations] is already useful for screening generic source
arguments; it does not disprove a theta-specific transfer.

## Selected first transfer and continuation

The [J-B01 decision][decision], prepared 1 November 2026 with
gpt-6-astra / max, selects the real multiple-integral representation of
ordinary-coefficient Toeplitz determinants. Its first source condition is
monotonicity and convexity of the curve (Phi''/Phi, Phi^(4)/Phi), sufficient
for order-three consecutive minors. The [J-E01 r1 return][e01-return], executed with gpt-6.1-sol / ultra on
1 November 2026, verifies the representation and classical baseline but
proves that C<0 near the canonical origin. Both tail signs are eventually
positive. The selected everywhere convexity premise is therefore rejected;
the real integral and coefficient route retain their status. No new
coefficient range or global positivity theorem is claimed.

The revised [J-B01 decision][decision-r2], 1 November 2026,
gpt-6-astra / max, selects signed averaging. Its conditional FKG argument
makes the normalized integral nondecreasing in the coefficient index if
R'>0 and K=R'C'-3CR''>=0 globally. The [J-E01 r2 return][e01-r2-return],
1 November 2026, gpt-6.1-sol / ultra, verifies this conditional proof and
Gaussian equality. Q10 proves J(0)>0 and P7 gives eventual
K~3*2^30*t^7>0 with a differentiated theta remainder. Both bounded tests
support the mechanism; the global pair was still unproved at that stage. The payoff
is a structural index comparison, with no new coefficient range or order
induction.

The [J-B02 return][b02-return], 1 November 2026, gpt-6-astra / max,
proves in-note explicit bounds R'>63 t^2 and K>2^30 t^7 for t>=128,
covering u>=1. Complete joint numerators, origin deflation and amplitude
normalization specify a finite compact certificate with Cauchy and
omitted-theta errors. The [J-E02 r1 return][e02-return], 1 November 2026,
gpt-6.1-sol / ultra, audits the tail and certifies one origin leaf and all
126 middle cells at 128 bits, with no subdivision/refinement. The resulting
global R'>0,K>0 gives the normalized order-three comparison.
[J-E03 Review01][e03-review], 1 November 2026, gpt-6.1-sol / ultra,
accepts the fixed claim without correction or unresolved coverage.
It remains same-assistant/same-model internal assessment, not independent
specialist review, and gives no new coefficient range or order induction.

**The current J-B01–J-E03 sequence is complete.** [Continuation13][after-e03]
states the accepted baseline and stopping boundary. No further execution
or higher-order campaign is issued; a new research direction needs an
author-selected conceptual question. The completed [E02 request][e02-request],
its [Continuation10][sol-e02], the [r2 request][request-r2] and
[r1 request][request]/obstruction remain unchanged. The
[progress register][j-progress] owns live status.

## Parallel idea folders

The next-session [parallel evaluation packet](../notes/15_CONTINUATION_PARALLEL_BRANCH_EVALUATION_20261101.md) is ready: five branch returns, one coordinator comparative review, and a high-level final chat summary. It explicitly authorizes subagent evaluation in the next session; no branch has started during preparation.

On 1 November 2026, the author requested separate homes for the directions in Note14. The [ideas index](../../ideas/README.md) records the original five branches, initially grouped under the former Jensen notes folder: higher-order signed averaging, determinant order induction, conservative negative-mass flows, paired source/test deformations, and source-changing Jensen flows. Their starting briefs define bounded conceptual questions; the [sole register][j-progress] owns readiness and results. They can be pursued in parallel without changing the completed order-three baseline. Organization J-E04, **gpt-6-astra / xhigh**; no mathematical execution.

Save route derivations in its notes folder, computations in numerics and
assessments in reviews, creating those folders with their first artifacts.
Keep common methods and the [reference catalog][catalog] at the base.
The [spectral plan][sl-overview] is a companion consumer of shared
identities; no implication between the routes is assumed without proof.

[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[reformulations]: ../../../../../avoid/01_restating_the_target.md
[shape]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[imports]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[workflow]: ../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[foundation]: ../../notes/01_LITERATURE_TECHNIQUES_AND_RADIAL_INHERITANCE_20261101.md
[closure]: ../../notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md
[formulations]: ../../notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md
[references]: ../../references/README.md
[catalog]: ../../references/sources.json
[base-overview]: ../../research-overview/01_POSITIVE_THETA_PRIMITIVES_RESEARCH_OVERVIEW_20261101.md
[base-progress]: ../../research-progress/01_POSITIVE_THETA_PRIMITIVES_RESEARCH_PROGRESS_20261101.md
[j-overview]: 01_JENSEN_RESEARCH_OVERVIEW_20261101.md
[j-progress]: ../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[sl-overview]: ../../02_spectral_laguerre/research-overview/01_SPECTRAL_LAGUERRE_RESEARCH_OVERVIEW_20261101.md
[sl-progress]: ../../02_spectral_laguerre/research-progress/01_SPECTRAL_LAGUERRE_RESEARCH_PROGRESS_20261101.md

[decision]: ../notes/01_J_B01_COEFFICIENT_REPRESENTATION_DECISION_20261101.md
[request]: ../notes/01_J_B01_COEFFICIENT_REPRESENTATION_DECISION_20261101.md#7-frozen-execution-request-j-e01-r1

[e01-return]: ../notes/03_J_E01_R1_REPRESENTATION_AND_ENDPOINT_TAIL_RETURN_20261101.md
[after-e01]: ../notes/04_CONTINUATION_AFTER_J_E01_ORIGIN_OBSTRUCTION_20261101.md

[decision-r2]: ../notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md
[request-r2]: ../notes/05_J_B01_SIGNED_AVERAGING_DECISION_20261101.md#7-frozen-execution-request-j-e01-r2
[sol-r2]: ../notes/06_CONTINUATION_FOR_SOL_SIGNED_AVERAGING_AUDIT_20261101.md

[e01-r2-return]: ../notes/07_J_E01_R2_SIGNED_AVERAGING_AND_Q10_P7_RETURN_20261101.md
[after-r2]: ../notes/08_CONTINUATION_FOR_ASTRA_GLOBAL_SIGNED_AVERAGING_20261101.md

[b02-return]: ../notes/09_J_B02_GLOBAL_TAIL_AND_COMPACT_CERTIFICATE_20261101.md
[e02-request]: ../notes/09_J_B02_GLOBAL_TAIL_AND_COMPACT_CERTIFICATE_20261101.md#7-frozen-execution-request-j-e02-r1
[sol-e02]: ../notes/10_CONTINUATION_FOR_SOL_GLOBAL_SIGN_CERTIFICATE_20261101.md

[e02-return]: ../notes/11_J_E02_R1_GLOBAL_SIGN_CERTIFICATE_RETURN_20261101.md
[after-e02]: ../notes/12_CONTINUATION_FOR_SOL_J_E03_GLOBAL_SIGN_ASSESSMENT_20261101.md

[e03-review]: ../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md
[after-e03]: ../notes/13_CONTINUATION_AFTER_J_E03_ACCEPTED_ASSESSMENT_20261101.md

## Evaluation update, 1 November 2026

Prepared for Edward Baker with substantial LLM assistance, actual gpt-6-astra / ultra. [Review02](../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md) now compares the five extension branches. It preserves the accepted order-three baseline and records a canonical h4 pointwise obstruction, an open joint order-induction estimate and scoped deformation/flow limitations. The [sole register][j-progress] owns the completed evaluation statuses and recommended unstarted J-B10. This initial overview is not a second live ledger.

## Numbered research directions

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Organization task **J-E07**.

[01 Mellin curvature](../01_mellin_curvature/README.md) is the home for order induction through the complete signed curvature, including recommended J-B10. [02 Signed averaging](../02_signed_averaging/README.md) is the home for the integrated alternative after the canonical pointwise obstruction. Their READMEs provide current problem statements and reading order; this overview retains the common formulation. The existing Jensen progress file remains the sole live task register.
