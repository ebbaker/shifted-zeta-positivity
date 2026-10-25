# Milestone history

Prepared for Edward Baker with substantial LLM assistance.
Opening configuration: gpt-6-astra (Codex), recorded effort max.

| Date | Investigation | Version pointer | Why it matters | Supporting material |
| --- | --- | --- | --- | --- |
| 2026-10-24 | Averaged unnormalized heat density | [Opening note](notes/01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md); working tree, no commit created | Records the author's scope, two time-limit models, spatial/time averaging and a source-anchored matching plan | [Source catalog](references/README.md), [chat history](chat-histories/README.md) |
| 2026-10-24 | Asymptotics, fluctuation closure and boundary-matched evolution | [Research program](research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md); working tree | Specifies the staged research and the explicit covariance term to approximate | [Filtered identities](notes/02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md), [progress ledger](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md) |
| 2026-10-24 | First bounded averaged-density research round | [Asymptotic note](notes/05_ASYMPTOTIC_MEAN_SHAPES_AND_FLUCTUATIONS_20261024.md); working tree, no commit created | Adds fixed-region negative-time covariance, exact whole-period covariance, a 17-case local closure pilot and conditional regulator-bias control | [Pilot note](notes/04_GRADIENT_CLOSURE_AND_ACTUAL_THETA_PILOT_20261024.md), [self-review](reviews/01_FIRST_RESEARCH_ROUND_SELF_REVIEW_20261024.md), [continuation](notes/07_CONTINUATION_FOR_NEW_CHAT_20261024.md) |
| 2026-10-24 | Coarse positive-time density and weak transport | [Note 09](notes/09_COMPLETE_SOURCE_MOMENT_TRANSFER_AND_WEAK_CURRENT_20261024.md); working tree, no commit created | Conditional source-moment/regulator transfer and finite floating mass/current comparisons across seven to nine periods; full closure remains open | [Self-review](reviews/02_COARSE_TRANSFER_AND_WEAK_CURRENT_SELF_REVIEW_20261024.md), [continuation](notes/10_CONTINUATION_AFTER_COARSE_TRANSFER_20261024.md) |
| 2026-10-24 | Two infinite heat-time limits and stationary Vandermonde shape | [Notes 11](notes/11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md) and [12](notes/12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md); working tree, no commit created | Explicit all-height negative density error, growing-height positive clock and growing-block determinant/Hessian bounds; scoped global-clock obstruction and costly all-height analytic fallback | [Self-review](reviews/03_TWO_TIME_LIMITS_AND_VANDERMONDE_SELF_REVIEW_20261024.md), [continuation](notes/13_CONTINUATION_AFTER_TWO_TIME_LIMITS_20261024.md) |
| 2026-10-24 | Analytical draft and adaptive-regulator extension | [Maintained manuscript](manuscript/main.tex) and [Note 14](notes/14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md); working tree, no commit created | Consolidates proofs with numerics in an appendix; adds exact variable-epsilon evolution and weak/asymptotic error bounds, including an explicit saddle regulator | [Build record](manuscript/BUILD_RECORD_20261024.json), [self-review](reviews/04_MANUSCRIPT_AND_VARIABLE_EPSILON_SELF_REVIEW_20261024.md), [continuation](notes/15_CONTINUATION_AFTER_MANUSCRIPT_AND_VARIABLE_EPSILON_20261024.md) |
| 2026-10-24 | Explicit saddle density and finite-time connection | [Note 19](notes/19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md), [Note 20](notes/20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md); working-tree research, no new manuscript version or commit | Pays saddle coefficients, retains exact finite phase, and supplies a global regulator/finite-source comparison; full all-time bridge remains open | [Assessment](reviews/06_EXPLICIT_CLOCK_AND_FINITE_BRIDGE_SELF_REVIEW_20261024.md), [progress](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md) |
| 2026-10-24 | Analytical manuscript integration | [Maintained source](manuscript/main.tex), [hash-bound build record](manuscript/BUILD_RECORD_20261024.json); working tree, no commit or snapshot | Rewrites the background and integrates the adaptive explicit clock and finite-source/covariance proofs; 25-page checked PDF, brief numerical appendix, sharper determinant mean term | [Integration note](notes/21_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261024.md), [review](reviews/07_ANALYTICAL_MANUSCRIPT_INTEGRATION_SELF_REVIEW_20261024.md) |
| 2026-10-24 | HDA-15 local source and nonlinear comparison | [Maintained source](manuscript/main.tex), [current source/export hashes](manuscript/BUILD_RECORD_20261024.json); working tree, no commit or snapshot | 28-page checked manuscript adds a declared contract and sharper source/amplitude/covariance bounds; the finite trial is rejected | [Note 23](notes/23_FINITE_TRANSITION_CONTRACT_AND_LOCAL_BOUNDS_20261024.md), [review](reviews/08_FINITE_TRANSITION_LOCAL_BOUNDS_SELF_REVIEW_20261024.md) |
| 2026-10-24 | HDA-19 outer analysis and HDA-16 negative endpoint | [Note 25](notes/25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md), [Note 26](notes/26_NEGATIVE_ENDPOINT_EVOLUTION_AND_COVARIANCE_20261024.md); working-tree research, no new manuscript version, commit or snapshot | Explicit compact-time outer tails, a scoped cutoff-potential failure, and all-height negative evolution with Q/Delta Q errors O(T^-3)/O(T^-4) | [Review 09](reviews/09_OUTER_TAIL_AND_NEGATIVE_ENDPOINT_SELF_REVIEW_20261024.md), [progress](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md) |
| 2026-10-24 | HDA-19 compact-time adaptive outer density | [Note 27](notes/27_COMPACT_TIME_GAMMA_OUTER_DENSITY_20261024.md); working-tree research, no manuscript version, commit or snapshot | Complete gamma-pair error, physical collars and finite-phase static density O(log^2 X/X); regulator-switch layer and joint-regime gaps retained | [Review 10](reviews/10_GAMMA_OUTER_DENSITY_SELF_REVIEW_20261024.md), [progress](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md) |
| 2026-10-24 | HDA-19 joint outer range and regulator layer | [Note 28](notes/28_JOINT_OUTER_REGULATOR_TRANSFER_AND_SWITCH_LAYER_20261024.md); working-tree research, no commit or manuscript snapshot | Uniform-switch static density/potential jets, a joint outer range, resolved layer and exact model residual; inner gap retained | [Review 11](reviews/11_JOINT_OUTER_AND_SWITCH_LAYER_SELF_REVIEW_20261024.md), [continuation](notes/29_CONTINUATION_JOINT_OUTER_TO_INNER_MATCHING_20261024.md) |
| 2026-10-24 | HDA-19 full gamma saddle and inner overlap | [Note 30](notes/30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md); working-tree research, no commit or snapshot | Static all-height positive endpoint, actual inner overlap and exact model residual; positive evolution remains open | [Review 12](reviews/12_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_SELF_REVIEW_20261024.md), [progress](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md) |
| 2026-10-24 | HDA-16/19 positive evolution and covariance | [Note 31](notes/31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md); working-tree research, no commit or snapshot | All-height O(t^-1/2) current/time/actual-covariance errors, retained defects and compact-time switch coverage; finite-core joining remains | [Review 13](reviews/13_POSITIVE_EVOLUTION_AND_COVARIANCE_SELF_REVIEW_20261024.md), [progress](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md) |

Future milestones should point to commits or tags. No manuscript snapshot
folder has been created.


24 October 2026 — **Manuscript integration plan, no new manuscript version.**
HDA-10-MI1 r1: [specification](notes/MANUSCRIPT_INTEGRATION_FOR_SOL_20261024.md)
and [frozen inputs](notes/MANUSCRIPT_INTEGRATION_INPUTS_20261024.json), working
tree, no commit or snapshot. Maps Notes 25--28 and 30 into the maintained
TeX for Sol 6.1; newer positive-evolution results are deferred by the author.
The 28-page Note 23 source/build remains unchanged. Prepared for Edward
Baker with substantial LLM assistance, gpt-6-astra, actual effort max.


2026-10-24 — **HDA-10-MI1 r1 production, results through Note 30.**
[Maintained source](manuscript/main.tex) and [source/export hashes](manuscript/BUILD_RECORD_20261024.json),
working tree; no commit or snapshot. Verified 54-page integration adds
negative evolution, gamma static/switch results and actual inner overlap,
retaining residuals and author-deferred positive evolution.
[Specification](notes/MANUSCRIPT_INTEGRATION_FOR_SOL_20261024.md);
[production assessment](reviews/14_MANUSCRIPT_INTEGRATION_PRODUCTION_REVIEW_20261024.md).
Prepared for Edward Baker with substantial LLM assistance, gpt-6.1-sol,
actual effort ultra.

**24 October 2026 — continuation and manuscript assessment, chat 0007.**
[Note 32](notes/32_CONTINUATION_FINITE_CORE_AND_JOINING_20261024.md) sets the finite-core/joining task;
[Review 15](reviews/15_MANUSCRIPT_REVIEW_AND_SOL_RECOMMENDATIONS_20261024.md) records corrections and additions for Sol
against the unchanged 54-page manuscript, with [input hashes](reviews/15_MANUSCRIPT_REVIEW_INPUTS_20261024.json).
Working-tree notes only; no manuscript version, commit or snapshot.
Prepared for Edward Baker with LLM assistance, gpt-6-astra, max.


2026-10-24 — **Review 15 manuscript revision through Note 31.**
[Maintained source](manuscript/main.tex), [source/export hashes](manuscript/BUILD_RECORD_20261024.json);
working tree, no commit or snapshot. Verified 65-page revision adds
positive evolution/actual covariance with residuals, corrects source
notation, and consolidates finite inner inputs and model navigation.
[Review 15](reviews/15_MANUSCRIPT_REVIEW_AND_SOL_RECOMMENDATIONS_20261024.md);
[production assessment](reviews/16_REVIEW15_REVISION_PRODUCTION_ASSESSMENT_20261024.md).
Prepared for Edward Baker with substantial LLM assistance, gpt-6.1-sol,
actual effort ultra; earlier HDA-10-MI1 r1 remains historical.
