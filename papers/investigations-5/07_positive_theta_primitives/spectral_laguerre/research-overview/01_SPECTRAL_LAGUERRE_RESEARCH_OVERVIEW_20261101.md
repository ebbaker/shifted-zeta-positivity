# Spectral Laguerre criterion and theta correlations: research overview

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **xhigh**.

**Status: initial research overview and plan.** This route studies whether
theta structure can provide positive definiteness of the correlations
equivalent to the generalized spectral Laguerre inequalities.
No new global spectral sign is established here. The
[spectral progress register][sl-progress] owns SL-task status;
the [overall overview][base-overview] owns shared-method planning.

## Mathematical destination and normalization

Use \(H(z)=\int_0^\infty\Phi(u)\cos(zu)\,du\), with the canonical even
theta source in the [common conventions](../../README.md#common-mathematical-normalization).
Define
\[
|H(x+iy)|^2=\sum_{n\ge0}\Lambda_n[H](x)y^{2n},\qquad
\Lambda_n[H](x)=\frac{1}{(2n)!}
\sum_{j=0}^{2n}(-1)^{j+n}\binom{2n}{j}
H^{(j)}(x)H^{(2n-j)}(x).
\]
For this entire function, RH is equivalent to
\(\Lambda_n[H](x)\ge0\) for every n and every real x. This is a
classical complete criterion, not a new reduction. In particular,
\[
\Lambda_1=H'^2-HH'',\qquad
\Lambda_2=\frac{HH^{(4)}-4H'H^{(3)}+3H''^2}{12}.
\]
These are spectral expressions. They are not the iterates of
\(\mathcal L[f]=(f')^2-ff''\), whether applied to H or the source
\(S(x)=\Phi(\sqrt x)\).

For the associated kernels
\[
K_n(v)=\int_{\mathbb R}u^{2n}\Phi(u+v)\Phi(u-v)\,du,
\]
the half-line convention gives
\[
\Lambda_n[H](x)=
\frac{2^{2n-1}}{(2n)!}\int_{\mathbb R}K_n(v)\cos(2xv)\,dv.
\]
Thus the complete criterion is also positive definiteness of every K_n.
This means that every finite quadratic form
\(\sum_{i,j}\alpha_i\overline{\alpha_j}K_n(v_i-v_j)\)
is nonnegative. Pointwise positivity of K_n does not establish it.
The [formulation note][formulations] and [catalog][catalog] record the
classical source and the factor-of-four inconsistency in its printed
half-line formula; the formula above uses the full-line theorem and
the conversion to our H.

## Baseline and possible milestones

The n=0 case follows from the autocorrelation identity and checks
normalization. A global proof of \(\Lambda_1\ge0\) would be a meaningful
lower-order milestone; it would not by itself establish the full criterion.
A compact frequency result is a compact result unless a separate argument
covers the exterior. A finite hierarchy requires a proved extension
mechanism before it becomes an all-order statement.

Classical source-concavity and CNV results supply successful moment-sign
transfers, but not this full spectral conclusion. The
[closure note][closure] identifies the difficulty: the oscillatory cosine
kernel lacks the fixed determinant sign used in the moment argument.
Recent theta-specific differential algebra supplies pointwise identities,
not automatic closure of products of shifted sources after integration.

The existing [literature survey][foundation] and [reference records][references]
are the starting bibliography. Importing a recent preprint lemma requires
checking the particular proof and hypotheses used; this setup adds no
new source audit or positivity evidence.

## Candidate mechanisms and the main obligation

The first comparison should use one complete expression, initially K_1
or the equivalent \(\Lambda_1\), so the target is concrete.
Two possibilities are worth evaluating: an exact Gram/autocorrelation
representation, and a decomposition into a positive-definite part plus
a signed correction that can actually be controlled. Neither is asserted
to exist for the needed kernel.

For the second possibility, a small pointwise correction is insufficient.
The estimate must preserve nonnegativity of the full Fourier transform
or of all required quadratic forms, including where a proposed main term
has a small margin. The complete signed interaction remains part of
the target.

Theta identities at the two shifted arguments, primitive integration by
parts and joint remainder estimates may expose useful structure.
A candidate derivation must retain all mixed quantities, endpoints and
justifications for differentiation and integration. If repeated
differentiation creates an unclosed hierarchy, that hierarchy is an
output to analyze rather than an assumed finite system.

The first representation must also say what changes with n and with
unbounded frequency. A useful n=1 mechanism need not solve every n
immediately, but its limitations must be visible. Heat time zero is the
default; an auxiliary flow needs a specific analytical purpose and a
proved return to the original H.

## Research contracts

The [model workflow][workflow] classifies conceptual and execution work
before it starts. Readiness belongs in the progress register.

| ID | Type and recommendation | Dependency | Deliverable and completion condition |
| --- | --- | --- | --- |
| SL-B01 | B — Astra; choose a representation that might control the full spectral sign | Existing shared foundation | Compare at most two representations of K_1 or its exact spectral counterpart. Return one selected mechanism, domain, baseline, missing sign estimate and higher-order limitation; or a scoped reason neither is ready. |
| SL-E01 | E — Sol; derive a specified correlation identity with full normalization | SL-B01 selects a mechanism and issues a bounded derivation request | Derive the requested formula, its n=0 normalization check and n=1 specialization; retain mixed terms, boundaries and convergence. State the exact PD or spectral implication and any remaining estimate. |
| SL-B02 | B — Astra; resolve the missing sign or positive-definiteness mechanism | SL-E01 return, plus any explicitly needed shared result | Address one named estimate or structural factorization. Return a proof, a fixed execution contract or a scoped obstruction, with its order/frequency coverage and actual theta premise. |
| SL-E02 | E — Sol; execute a fixed proof or finite acquisition request | A tractable SL-B02 contract | Complete one revision with specified lemmas/cases, error and tail payments and work limits. Return the result and failed cases. Sampling quadratic forms or frequencies is labeled finite evidence. |
| SL-E03 | E — Sol; assess a fixed spectral claim and its coverage | A versioned SL-E02 return or complete analytical SL-B02 proof | Check constants, all terms, imported hypotheses, control outcomes and global/finite scope. Save one assessment, identify its review relationship and update the route's evidence links and live register. |

SL-E01 returns to SL-B01 if a new representation is needed.
SL-E02 returns to SL-B02 when the fixed contract requires a new
mathematical mechanism or wider question. An analytical SL-B02 proof
can go directly to SL-E03. Numerical work is optional and begins only
with fixed cases, method, limits and acceptance criteria.

## Shared requests and evidence

Requests to [shared work][base-overview] may concern a two-source theta
identity, a boundary-complete primitive transfer, determinant composition
or a joint remainder estimate. Name the consuming K_n or Lambda formula,
the range and the desired gain. A common source identity helps the
[Jensen route][j-overview] only after its separate coefficient transfer
is established.

Use the [result index][results], especially [theta identities][theta] and
[controls][controls], with the [avoid index][avoid]:
[reformulations][reformulations], [generic premises][shape],
[joint bounds][joint], [scoped failures][scopes] and [imports][imports].
For a proposed sufficient estimate, determine which actual premises
each relevant control satisfies and test the claimed implication on its
declared domain. A generic Gram construction for a different positive
object is not a proof that K_n is positive definite.

Useful returns are a new applicable representation with a tractable
remaining obligation, an actual sign estimate on a specified domain,
or a precisely scoped failure. These have different evidentiary statuses.
Neither an exact identity nor favorable samples are evidence for the
complete RH-equivalent criterion.

## First continuation

**Next: [B] SL-B01 — Astra.** Produce one short comparison and decision
note for the complete n=1 expression, stating what supplies the sign
and the first requested shared tool. Keep all-frequency and all-order
obligations explicit. Do not begin an unrestricted frequency scan.

Save derivations in route notes, computations in numerics and assessments
in reviews, creating those folders with their first artifacts. Reusable
tools and the common reference catalog remain at the investigation base.

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
[j-overview]: ../../jensen/research-overview/01_JENSEN_RESEARCH_OVERVIEW_20261101.md
[j-progress]: ../../jensen/research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[sl-overview]: ../../spectral_laguerre/research-overview/01_SPECTRAL_LAGUERRE_RESEARCH_OVERVIEW_20261101.md
[sl-progress]: ../../spectral_laguerre/research-progress/01_SPECTRAL_LAGUERRE_RESEARCH_PROGRESS_20261101.md
