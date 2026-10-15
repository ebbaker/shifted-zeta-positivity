# Theta correlations, Laguerre signs, and hypercomplex jets

Investigation 21 — 15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**.

Start with the [current research overview](research-overview/RESEARCH_OVERVIEW_20261015_CORRELATION_KERNELS.md) and the [manuscript](manuscript/quaternion_theta_geometry.tex). The octonionic reduction and literature review are now integrated: the physical observations are planar dot products and determinants, a reflected monogenic lift preserves the physical four-jet with fewer terms, and complete theta correlations express both Laguerre forms and the physical energy in one family.

The objective is to exclude every positive-time real collision of the theta heat flow. With \(h_j=\partial_x^jH\), the collision detector is \(E=h_0^2+h_1^2\), and the stationary observations are \(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\) on \(S_j=\{h_{j+1}=0\}\), for \(j=0,1\). A source-derived bound \(\mathcal L_j\ge-\kappa_jE\), locally bounded through all covered candidate collisions, is sufficient. The all-cutoff and logarithmic-loss versions remain available. The new reductions do not prove that missing theta estimate.

| Established result | Scope |
| --- | --- |
| Finite physical gap and both stationary signs | \(0\le t\le1/2\), \(|x|\le112\), \(\sqrt E>10^{-17}\) |
| Uniform four-jet asymptotic and both full strict signs | Sufficiently large \(|x|\), \(0<t\le1/2\), \(t\log(|x|/(4\pi))\ge61/24\), with unevaluated starting height |
| Explicit conservative outer result | \(|x|\ge4\pi e^{10^9}\), \(t\log(|x|/(4\pi))\ge5\) |
| Octonionic and correlation reductions | Exact identities preserving the detector, signed observations, and original cutoff payments; no new sign region |

The inner cusp and finite transition to asymptotic coverage remain open. The current leading task is a theta-specific signed estimate for the complete or hybrid correlation kernel near small physical energy. The research overview explains the dependencies and acceptance tests.

| Program | Notes |
| --- | --- |
| PR01 — weighted outer remainders | [01_weighted_outer_remainders](notes/01_weighted_outer_remainders/README.md) |
| PR02 — signed control in the inner cusp | [02_signed_cusp_control](notes/02_signed_cusp_control/README.md) |
| PR03 — effective heights and finite bridging | [03_effective_bridge](notes/03_effective_bridge/README.md) |
| ALG — octonionic reductions | [04_octonionic_reductions](notes/04_octonionic_reductions/README.md) |
| PR02-CORR — complete theta correlation kernels | [05_theta_correlation_kernels](notes/05_theta_correlation_kernels/README.md) |
| COORD — integration and continuation | [00_research_coordination](notes/00_research_coordination/README.md) |

The [notes index](notes/README.md) preserves the historical numbered notes at their original paths. Current continuation is [Note 37](notes/00_research_coordination/37_OCTONIONIC_CORRELATION_INTEGRATION_AND_CONTINUATION_20261015.md). Detailed history remains in those notes and the [reviews](reviews/README.md); concise milestones are in [DRAFT_HISTORY.md](DRAFT_HISTORY.md).

The [compiled PDF](../../../../output/pdf/quaternion_theta_geometry.pdf), [build record](manuscript/BUILD_RECORD.json), and [integration review](reviews/26_OCTONIONIC_CORRELATION_MANUSCRIPT_INTEGRATION_20261015.md) identify the current manuscript and validation. The [literature review](reviews/25_OCTONIONIC_MACHINERY_LITERATURE_REVIEW_20261015.md) preserves the assessment that motivated this revision. The explicitly requested pre-integration [source backup](manuscript/quaternion_theta_geometry.backup_20261015.tex), [PDF backup](manuscript/quaternion_theta_geometry.backup_20261015.pdf), and [backup receipt](manuscript/BACKUP_RECORD_20261015.json) retain the preceding 59-page manuscript.

Save incremental arguments in the tagged notes, calculations and small receipts in `numerics/`, and assessments in `reviews/`. Keep the manuscript as one stable source; future milestones should refer to commits or tags. Follow the repository [research instructions](../../../../AGENTS.md), [chat-history workflow](../../../../tools/CHAT_HISTORY.md), and [large-file policy](../../../../LARGE_FILES.md). Synced project references remain read-only.

Investigation-specific conversations normally belong in [chat-histories](chat-histories/README.md). The current conversation retains its separately authorized formal-replay registration, number 13; adding program folders does not move or renumber it.
