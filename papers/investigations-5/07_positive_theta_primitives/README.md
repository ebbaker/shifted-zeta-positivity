# Positive theta primitives: Jensen and spectral Laguerre programs

Opened 31 October 2026; organization revised 1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **xhigh**.

Investigation07 studies how exact theta identities, positive primitives and signed integral formulas can help prove real-zero properties of the Riemann transform. It develops two proof routes: the **Jensen formulation** and the **spectral Laguerre criterion**. Questions arising in these routes guide the shared development of tools at the top level of this investigation.

**Status:** [Jensen J-E03 Review01](jensen/reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md) accepts the canonical source pair R'>0,K>0 and normalized signed-averaging index comparison at determinant order three, following the full compact certificate and audited tail. This is same-assistant/same-model internal assessment, not independent specialist review. The original J-B01–J-E03 sequence is complete; [Continuation13](jensen/notes/13_CONTINUATION_AFTER_J_E03_ACCEPTED_ASSESSMENT_20261101.md) records its boundary. Shared and spectral programs retain their own scopes and registers. The prior negative origin C is preserved. No new coefficient range, increasing-order proof, RH or simplicity result is established. Assessment: 1 November 2026, gpt-6.1-sol / ultra.

## Programs and shared work

| Location | Purpose |
| --- | --- |
| [ideas/](ideas/README.md) | Five parallel Jensen research directions, with links to their note folders |
| [jensen/](jensen/README.md) | Jensen hyperbolicity, with coefficient total positivity as a complementary formulation and determinant tool |
| [spectral_laguerre/](spectral_laguerre/README.md) | Generalized spectral Laguerre inequalities and positive definiteness of associated theta correlations |
| [research-overview/](research-overview/README.md) | Overall research plan and shared-tool contracts, linking both route overviews |
| [research-progress/](research-progress/README.md) | Sole live register for shared PT tasks; route statuses remain in their own registers |
| [notes/](notes/README.md) | Shared mathematical tools, normalization, literature synthesis and comparisons that serve both routes |
| [numerics/](numerics/README.md) | Shared exact algebra, computational methods and small execution records |
| [references/](references/README.md) | One canonical bibliography, source catalog and reading record for the investigation and both routes |
| [brainstorm/](brainstorm/README.md) | The founding discussion and exploratory background |
| [chat-histories/](chat-histories/README.md) | Existing cross-route conversation provenance |

Here **top level** means `07_positive_theta_primitives/`, within the larger research checkout. Common research belongs in its existing `notes/`, `numerics/` and, when assessments are written, `reviews/`. The repository-wide infrastructure under `tools/` retains its separate role.

Each proof route will use its own `notes/`, `numerics/` and `reviews/` as work is produced. Create those directories with their first substantive artifacts. Route-specific work stays with its consumer; a reusable method has one canonical home in the shared area, with links from both routes. Existing notes remain at their current paths because they supply the common foundation.

## Common mathematical normalization

Use the classical theta source and half-line transform
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad H(z)=\int_0^\infty\Phi(u)\cos(zu)\,du.
\]
RH is equivalent to all zeros of H being real. Simplicity is a separate question. Define
\[
S(x)=\Phi(\sqrt x),\quad b_n=\int_0^\infty u^{2n}\Phi(u)\,du,
\quad c_n=\frac{b_n}{(2n)!},\quad\gamma_n=n!c_n,
\]
so that
\[
H(z)=\sum_{n\ge0}(-1)^nc_nz^{2n},\qquad
F(w)=H(i\sqrt w)=\sum_{n\ge0}c_nw^n
=\sum_{n\ge0}\frac{\gamma_n}{n!}w^n.
\]
The source operation \(\mathcal L[f]=(f')^2-ff''\) and its iterates are distinguished from the generalized spectral expressions \(\Lambda_n[H]\). Positivity or concavity of a source, positivity of a Fourier transform, and real-rootedness of an entire function are separate properties. The [formulation note](notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md) explains the implications and gives explicit diagnostics.

## How the routes guide tool development

A route first identifies a concrete expression, its parameter range and the additional information needed to estimate it. Shared work then investigates methods that can supply that information. The result returns to the route for a check of what it actually proves. Questions from both routes may be pursued; there is no standing requirement that one route wait for the other.

| Shared method | Questions it may help answer |
| --- | --- |
| Jacobi differential algebra and modular identities | Which relations among actual theta derivatives remain useful after moment or correlation integration? |
| Determinant composition and integral identities | Under what precise hypotheses can a source sign be transferred to a coefficient minor or a positive-definite kernel? |
| Primitive integration by parts | Can a complete signed expression be estimated with all boundary terms retained? |
| Joint algebraic estimates and rigorous tails | Can bounds retain mixed-term cancellation and remain effective in the route's unbounded parameters? |
| Source diagnostics and controls | Which premise uses canonical theta information beyond generic positivity, decay or concavity? |

A request for shared work should specify the consuming route and formula, the domain, the known baseline and the desired improvement. These details belong in the relevant research note; a separate administrative layer is unnecessary. A shared identity becomes useful to a route only after its hypotheses, convergence and quantitative consequences are established there.

[Investigation05](../05_radial_theta_collision_geometry/README.md) supplies exact primitive transfers, boundary accounting, techniques for complete signed expressions and rigorous local estimates. Its radial flows and collision deadlines are optional tools, not the agenda of this investigation. The current organization develops both proof routes; [Note03](notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md) preserves the earlier recommendation to explore coefficient determinants first as part of the research history.

## Foundation and sources

- [Opening brainstorm and lessons](brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md).
- [Literature techniques and radial inheritance](notes/01_LITERATURE_TECHNIQUES_AND_RADIAL_INHERITANCE_20261101.md).
- [CNV transfer and theta differential closure](notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md).
- [RH formulations, source-concavity diagnostic and research direction](notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md).
- [Reference index](references/README.md), [source catalog](references/sources.json) and [BibTeX](references/sources.bib).
- [Milestone history](DRAFT_HISTORY.md) and [chat provenance](chat-histories/README.md).

Recent preprint results retain their recorded inspection status. Neither a bibliographic entry nor a downloaded paper certifies its claims. New sources are recorded in the common catalog with their route or shared-tool use.

## Research overviews and progress

| Program | Research overview | Live progress |
| --- | --- | --- |
| Overall and shared tools | [Overview01](research-overview/01_POSITIVE_THETA_PRIMITIVES_RESEARCH_OVERVIEW_20261101.md) | [Progress01](research-progress/01_POSITIVE_THETA_PRIMITIVES_RESEARCH_PROGRESS_20261101.md) |
| Jensen | [Overview01](jensen/research-overview/01_JENSEN_RESEARCH_OVERVIEW_20261101.md) | [Progress01](jensen/research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) |
| Spectral Laguerre | [Overview01](spectral_laguerre/research-overview/01_SPECTRAL_LAGUERRE_RESEARCH_OVERVIEW_20261101.md) | [Progress01](spectral_laguerre/research-progress/01_SPECTRAL_LAGUERRE_RESEARCH_PROGRESS_20261101.md) |

The overviews now provide initial background and research contracts. Detailed notes will develop and assess the mechanisms; the overviews will be revised as evidence arrives. Each progress file owns only its task family: PT for shared work, J for Jensen, SL for spectral Laguerre. The first route discussions identify concrete representations and missing estimates that can guide shared tool development.

Follow the [result summaries](../../../result-summaries/README.md), especially [theta identities](../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [controls](../../../result-summaries/12_collision_controls_and_screening.md), and the [patterns to avoid](../../../avoid/README.md), especially [reformulations](../../../avoid/01_restating_the_target.md), [separate bounds](../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../avoid/07_scoped_exclusions_read_as_universal.md). A complete RH criterion is a destination, not a new result; proposed sufficiency estimates require the relevant control checks. Follow the [reference workflow](../../../REFERENCE_WORKFLOW.md), [large-file policy](../../../LARGE_FILES.md) and [chat-history workflow](../../../tools/CHAT_HISTORY.md). Preserve existing chat registrations; future route-specific chats can be registered in their route's `chat-histories/`, while cross-route chats remain here.
