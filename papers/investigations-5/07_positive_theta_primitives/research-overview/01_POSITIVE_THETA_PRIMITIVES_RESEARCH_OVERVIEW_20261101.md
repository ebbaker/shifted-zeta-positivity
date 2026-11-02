# Positive theta primitives: research overview

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **xhigh**.

**Status: initial research overview and plan.** This document organizes the
existing foundation into two direct RH programs and shared tool development.
It supplies no new positivity theorem. The [base progress register][base-progress]
owns shared-task status; the [Jensen][j-progress] and
[spectral Laguerre][sl-progress] registers own their respective tasks.

## Objective and organization

The long-term objective is to prove real-rootedness of the canonical Riemann
transform through estimates that exploit theta's exact structure. We pursue
two classical formulations: all-degree Jensen hyperbolicity and the full
spectral Laguerre hierarchy. Their complete statements are RH-equivalent
destinations. Useful intermediate work includes an applicable transfer
theorem, an improved quantified range, or a precise obstruction to a proposed
estimate.

The two routes are meant to generate questions for the common tools.
Investigation05 contributes primitive identities, complete boundary
accounting and techniques for signed expressions; its collision geometry
and auxiliary flows do not determine this investigation's agenda. There
is no requirement to finish one route before exploring the other.

| Program | Mathematical object | First unresolved choice | Its overview |
| --- | --- | --- | --- |
| Jensen | Normalized moments, Jensen polynomials and coefficient Toeplitz minors | Which representation exposes a sign mechanism that might survive increasing degree/order? | [Jensen plan][j-overview] |
| Spectral Laguerre | Generalized Laguerre expressions and associated theta correlations | Which complete correlation representation can support a positive-definiteness argument? | [Spectral plan][sl-overview] |
| Shared tools | Exact theta algebra, determinant transfer, primitive identities and joint remainder bounds | Which requested identity or estimate has a concrete route-level use? | This plan |

## Common objects and the role of concavity

Fix the source and half-line transform in the
[program README](../README.md#common-mathematical-normalization):
\[
H(z)=\int_0^\infty\Phi(u)\cos(zu)\,du,\qquad S(x)=\Phi(\sqrt{x}),
\quad b_n=\int_0^\infty u^{2n}\Phi(u)\,du,
\quad c_n=\frac{b_n}{(2n)!},\quad\gamma_n=n!c_n.
\]
Then \(F(w)=H(i\sqrt w)=\sum c_nw^n=\sum\gamma_nw^n/n!\).
RH is equivalent to all zeros of H being real, or all zeros of F being
negative real. Simplicity is a separate issue.

Source concavity is a possible input to a transfer theorem.
The source operation \(\mathcal L[f]=(f')^2-ff''\) is distinct from the
generalized spectral expressions \(\Lambda_n[H]\). Known source-concavity
results yield Turán and double Turán information, but are not the complete
Jensen or spectral criterion. The [formulation note][formulations] gives
an explicit source diagnostic, with exact algebra recorded in
[numerics](../numerics/README.md), that rules out a generic inference from
iterated source concavity to real-rootedness. Its Gaussian and faster-decay
variants have different scopes, retained in that note.

This makes the source-to-target passage the central research question.
The Jacobi differential system closes at a source point. It does not,
by itself, close the mixed moment or correlation integrals required by
either route. An exact primitive identity likewise leaves the sign of
its full transformed expression to be estimated.

## Foundation available at initialization

| Input | Available use | Scope retained |
| --- | --- | --- |
| [Literature and inheritance note][foundation] | Classical determinant composition, primitive transfers, source concavity and selected recent developments | Literature synthesis and selected primary-source inspection, not a complete proof audit |
| [Differential-closure note][closure] | Jacobi derivative algebra, normalization and the distinction between pointwise and integrated closure | Exact identities do not supply an integrated positivity theorem |
| [Formulation note][formulations] | RH criteria, coefficient normalization and source-concavity diagnostic | No new canonical-theta sign or all-order result |
| [Theta result cluster][theta] | Positive primitive, complete-source reconstruction and signed arithmetic identities | Preserve the stated classes of nonclosure and failed separate estimates |
| [Control cluster][controls] | Tests for generic positivity, reflection, decay and primitive premises | Apply each control only to claims and domains for which it is relevant |

The common [reference catalog][catalog] remains canonical for all three
areas. The 2026 source-concavity, source-determinant and coefficient-tail
papers retain the inspection limits in [references][references]. Before a
new theorem depends on one, audit the exact statement and hypotheses
used; this setup performs no additional literature audit.

## Shared research contracts

Task types follow the [repository workflow][workflow]: B denotes a
conceptual decision, normally recommended for Astra; E denotes a specified
execution task, normally recommended for Sol. Edward Baker chooses the
actual model, effort and chat. These plans dispatch no work automatically.

| ID | Type and recommendation | Dependency | Bounded deliverable and completion condition |
| --- | --- | --- | --- |
| PT-E00 | E — Sol; ordinary document organization | Existing program READMEs and foundation notes | Establish these three overview/progress pairs, navigation and initial task ownership; check links and consistency. No mathematical execution is included. |
| PT-B01 | B — Astra; decide which source information could survive the requested integration | One concrete request from J-B01/J-B02 or SL-B01/SL-B02 | Compare at most two shared mechanisms for that request. Return one usable lemma/estimate contract, or identify the unresolved step or scoped failure. Name the consumer, domain, baseline and intended gain. |
| PT-E01 | E — Sol; derive or implement the specified shared method | PT-B01 contract with fixed inputs and acceptance test | Execute one request revision, retaining hypotheses, endpoints, mixed terms and tails. Return a proof or a precise failed obligation. Numerical work, if needed, requires declared finite cases and error/work limits before starting. |
| PT-E02 | E — Sol; assess a fixed return and document its usable scope | One versioned PT-E01 return, or a completed analytical PT-B01 argument | Check the claimed implication and relevant controls; record corrections, actual review relationship and applicable domains. Return one assessment and route-facing statement. |
| PT-B02 | B — Astra; compare mathematical usefulness across the routes | A first representation assessment from each route, or a specific shared-tool return affecting both | Compare only those available returns: what became easier, which parameter regime is addressed, and which tool is next worth developing. Return one priority decision or the remaining choice, without enlarging a failed claim. |

PT-E01 returns to PT-B01 if it needs a new mechanism, source, norm or target.
PT-E02 sends unresolved proof design to PT-B01 rather than silently repairing
it by changing the statement. PT-B02 may recommend a route-specific
continuation; it does not take ownership of that route's tasks.
The [progress register][base-progress] records readiness and returns.

## How a shared request is evaluated

A request identifies an actual formula, its parameter range and the
information missing from its estimate. For Jensen this may be a normalized
moment transfer or a coefficient determinant identity; for Laguerre it may
be a two-source identity or a representation of a complete correlation.
Shared work is justified by the consumer, even if only one route initially
uses it. A second route must establish its own transfer.

Acceptance distinguishes three outcomes: a proved gain on a declared
domain; an exact useful identity whose remaining inequality is explicit;
or a failure restricted to the tested class. Only the first is a positivity
advance. Record the known comparison theorem and its quantifiers, including
the increasing-order and unbounded-frequency obligations when applicable.

Follow the [result index][results] and [avoid index][avoid], especially
[reformulations][reformulations], [control premises][shape],
[joint estimates][joint], [scoped failures][scopes] and
[source inspection][imports]. Before promoting a proposed sufficient
estimate, apply the relevant [controls][controls] to its actual hypotheses
and conclusion; identify which premise each fails. A positive-time
collision is not automatically a counterexample to every time-zero,
finite-order statement. No new proposed sufficient estimate is tested or
promoted by this overview.

## Next research and maintenance

Both initial route discussions can begin from the existing foundation:
**[B] J-B01 — Astra**, comparing coefficient representations, and
**[B] SL-B01 — Astra**, comparing correlation representations. Either may
come first. Their concrete needs, rather than a general expansion of
source-concavity calculations, should initiate PT-B01.

Detailed work goes into the appropriate notes, numerics and reviews
folders. Update this overview when a mechanism, scope or baseline changes;
update live task states only in their owning progress register. The
route overviews link back here for shared tools and references. Retain one
canonical artifact for each reusable result, and link applications to it.

[results]: ../../../../result-summaries/README.md
[theta]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[reformulations]: ../../../../avoid/01_restating_the_target.md
[shape]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scopes]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[imports]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[foundation]: ../notes/01_LITERATURE_TECHNIQUES_AND_RADIAL_INHERITANCE_20261101.md
[closure]: ../notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md
[formulations]: ../notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md
[references]: ../references/README.md
[catalog]: ../references/sources.json
[base-overview]: ../research-overview/01_POSITIVE_THETA_PRIMITIVES_RESEARCH_OVERVIEW_20261101.md
[base-progress]: ../research-progress/01_POSITIVE_THETA_PRIMITIVES_RESEARCH_PROGRESS_20261101.md
[j-overview]: ../01_jensen/research-overview/01_JENSEN_RESEARCH_OVERVIEW_20261101.md
[j-progress]: ../01_jensen/research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[sl-overview]: ../02_spectral_laguerre/research-overview/01_SPECTRAL_LAGUERRE_RESEARCH_OVERVIEW_20261101.md
[sl-progress]: ../02_spectral_laguerre/research-progress/01_SPECTRAL_LAGUERRE_RESEARCH_PROGRESS_20261101.md
