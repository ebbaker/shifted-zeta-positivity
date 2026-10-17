# Theta correlations, Laguerre signs, and hypercomplex jets

> **Chat-history routing update, 17 October 2026.** Current histories: [Chat 19 — Review octonionic signed-bound ideas](chat-histories/0019_2026-10-15T06-24-10Z_review-octonionic-signed-bound-ideas.json). Use this investigation’s [local registry](chat-histories/index.json) and [relocation receipt](CHAT_HISTORY_RELOCATION_20261017.json) for current numbers and preserved provenance; this supersedes the routing and numbering below. All future investigation 21 chats belong in this investigation’s `chat-histories/` folder.

Investigation 21 — 15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**.

Start with the [current research overview](research-overview/RESEARCH_OVERVIEW_20261015_SIGNED_FORMS_AND_PRIMITIVE.md) and [manuscript](manuscript/quaternion_theta_geometry.tex). The current 96-page revision integrates Notes 38–53, including the signed-form and positive-primitive continuation. [Review 32](reviews/32_SIGNED_FORMS_PRIMITIVE_MANUSCRIPT_INTEGRATION_20261015.md) and the [build record](manuscript/BUILD_RECORD.json) record the checks and scope.

The objective is to exclude every positive-time real collision of the theta heat flow. With \(h_j=\partial_x^jH\), the detector is \(E=h_0^2+h_1^2\); the signed observations are \(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\) on the full stationary sets \(S_j=\{h_{j+1}=0\}\), for \(j=0,1\). A source-prescribed bound \(\mathcal L_j\ge-\kappa_jE\), locally bounded through covered candidate events, would suffice. The all-cutoff logarithmic and subpower alternatives are conditional transfers. The required theta estimate remains open.

| Established coverage | Scope |
| --- | --- |
| Finite physical gap and both stationary signs | \(0\le t\le1/2\), \(|x|\le112\), \(\sqrt E>10^{-17}\) |
| Uniform four-jet asymptotic and both full strict signs | Sufficiently large \(|x|\), \(0<t\le1/2\), \(t\log(|x|/(4\pi))\ge61/24\), with unevaluated starting height |
| Explicit conservative outer result | \(|x|\ge4\pi e^{10^9}\), \(t\log(|x|/(4\pi))\ge5\) |

Exact source identities, sharp integrated positivity, and the positive theta primitive add analytic structure without enlarging this sign coverage. The inner cusp and finite transition remain open. The next task is an energy-relative estimate for the complete signed primitive reconstruction or boundary current, preserving cancellation and both predecessor branches.

| Program | Notes |
| --- | --- |
| PR01 — weighted outer remainders | [01_weighted_outer_remainders](notes/01_weighted_outer_remainders/README.md) |
| PR02 — signed control in the inner cusp | [02_signed_cusp_control](notes/02_signed_cusp_control/README.md) |
| PR03 — effective heights and finite bridging | [03_effective_bridge](notes/03_effective_bridge/README.md) |
| ALG — octonionic and signed-form reductions | [04_octonionic_reductions](notes/04_octonionic_reductions/README.md) |
| PR02-CORR — complete theta correlations and primitive | [05_theta_correlation_kernels](notes/05_theta_correlation_kernels/README.md) |
| COORD — integration and continuation | [00_research_coordination](notes/00_research_coordination/README.md) |

The [notes index](notes/README.md) preserves historical numbered notes. Current handoff is [Note 59](notes/00_research_coordination/59_PRIMITIVE_CONTROLS_AND_COMPLETED_PHASE_BUDGET_CONTINUATION_20261015.md); detailed assessments are in [reviews](reviews/README.md), and concise milestones in [DRAFT_HISTORY.md](DRAFT_HISTORY.md). The PDF is built from the [stable source](manuscript/quaternion_theta_geometry.tex) into the repository-root `output/pdf/` folder, which git ignores; it is not stored in the repository. Historical backups remain unchanged; no new snapshot, commit, or tag was created.

The author's two unpublished 2014 working notes are in `source-documents/`; [Review 30](reviews/30_QUATERNION_FORMS_DRAFT_COMPARISON_AND_RELEVANCE_20261015.md) compares their approaches and records their acknowledged incompleteness. Source files are preserved.

Follow the repository [research instructions](../../../../AGENTS.md), [history workflow](../../../../tools/CHAT_HISTORY.md), and [large-file policy](../../../../LARGE_FILES.md). Investigation conversations normally belong in [chat-histories](chat-histories/README.md). This integration conversation retains its explicitly authorized formal-replay history **16**; its [verification receipt](reviews/CHAT_HISTORY_SIGNED_FORMS_INTEGRATION_VERIFICATION_20261015.json) confirms the original identity and preceding final replies. Other conversations retain their own registrations.

## Subsequent research continuation

[Notes 56–59](notes/00_research_coordination/59_PRIMITIVE_CONTROLS_AND_COMPLETED_PHASE_BUDGET_CONTINUATION_20261015.md) add a primitive-compatible collision control, quantify circle negative-mass overpayment, and complete the explicit carrier-to-phase budget at 409/L. [Review 33](reviews/33_PRIMITIVE_CIRCLE_AND_CARRIER_CONTINUATION_REVIEW_20261015.md) records the independent internal checks. The imported exponent-pair constants and theta stationary estimate remain open; these results are not yet incorporated into the stable manuscript. This continuation preserves formal-replay history **17** under the explicit local instruction. Updated 15 October 2026 for Edward Baker with substantial LLM assistance, **gpt-6-astra**, effort **ultra**.

## Dedicated manifold continuation, 15 October 2026

At the author's request, the manifold and connection direction now has its own
[Investigation 22](../22_theta_manifold_geometry/README.md), with a systematic
[manuscript](../22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex)
and a high-level
[research overview](../22_theta_manifold_geometry/research-overview/RESEARCH_OVERVIEW_20261015.md).
Notes 60–63 remain the provenance for this branch. The present manuscript,
source documents and established analytic results stay here. The new project
adds the covariant theta-source formula and an explicit abelian ASD connection;
the theta-specific signed estimate remains open.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra**,
reasoning effort **ultra**.
