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


2026-10-24 — **Compact weak transfer and local time join, HDA-17/18.**
[Note 34](notes/34_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_20261024.md), working
tree, no commit/tag or manuscript snapshot. Reduces source-error inputs to
orders 0/2 for the full fixed-filter norm and pays the local time-cutoff
residual; spatial assembly and informative cost remain open.
[Review 17](reviews/17_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_SELF_REVIEW_20261024.md);
[Sol request](research-progress/handoffs/HDA-17-AN01.md). Prepared for Edward
Baker with LLM assistance, gpt-6-astra, actual effort xhigh.


24 October 2026 — **HDA-17-AN01 bounded method decision, no manuscript version.**
[Note 35](notes/35_WEAK_TRANSFER_BUDGET_DECISION_20261024.md), working tree,
no commit/tag/snapshot: implements weak A/B/C maps and exact selected
controls, retains failed source/filter budgets, and chooses local/default
with individual weak gains. HDA-17 Partial/HDA-18 Gated.
[Review 18](reviews/18_WEAK_TRANSFER_BUDGET_ASSESSMENT_20261024.md),
[index record](numerics/WEAK_TRANSFER_DIAGNOSTIC_20261024.json).
Prepared for Edward Baker with LLM assistance, gpt-6.1-sol, ultra, chat 0011.


24 October 2026 — **AN02 source/filter milestone, no manuscript version.**
[Note 36](notes/36_SOURCE_CURVATURE_AND_PEAK_INTEGRATION_20261024.md), working
tree, no commit/tag/snapshot: continuous source-cap/chord and signed-source
bounds, 24.37-fold source allowance gain, composite peak integration;
source/covariance and arithmetic/continuous gates remain.
[Review 19](reviews/19_SOURCE_CURVATURE_AND_PEAK_ASSESSMENT_20261024.md),
[record](numerics/SOURCE_PEAK_DIAGNOSTIC_20261024.json). Prepared for Edward
Baker with LLM assistance, gpt-6.1-sol, ultra, chat 0011.


24 October 2026 — **AN03 positive-Hermite source, no manuscript version.**
[Note 37](notes/37_POSITIVE_HERMITE_SOURCE_AND_REMAINDERS_20261024.md), working
tree, no commit/tag/snapshot: explicit positive source/remainder bounds,
1963-fold same-mesh interpolation gain with slope storage, r1 failure
retained, r2 sampled source allowances fit (worst ratio 0.688748).
Arithmetic/continuous integration remain unpaid.
[Review 20](reviews/20_POSITIVE_HERMITE_SOURCE_ASSESSMENT_20261024.md),
[r1](numerics/POSITIVE_HERMITE_DIAGNOSTIC_20261024.json),
[r2](numerics/HERMITE_DIRECTIONAL_CAPS_20261024.json). Prepared for Edward
Baker with LLM assistance, gpt-6.1-sol, ultra, chat 0011.


24 October 2026 — **HDA-10-MI2 r1, Note 39 analytical integration.** Maintained working-tree [source](manuscript/main.tex) and [build record](manuscript/BUILD_RECORD_20261024.json), no commit/tag or snapshot: checked 78-page revision adds Notes 34–37 transfer/time-join/source/Hermite proofs and scoped Note 38 interpretation. [Note 41](notes/41_NOTE39_MANUSCRIPT_IMPLEMENTATION_20261024.md), [Review 22](reviews/22_NOTE39_ANALYTICAL_INTEGRATION_PRODUCTION_ASSESSMENT_20261024.md). Production only; no numerical execution or core/global acceptance. Prepared for Edward Baker with LLM assistance, gpt-6.1-sol, actual effort xhigh, chat 0013.

2026-10-25 — **Heat-density Notes 42–45 consolidation and global contract.**
[Maintained source](manuscript/main.tex), [source/export hashes](manuscript/BUILD_RECORD_20261025.json);
working tree, no commit or snapshot. The 92-page revision integrates the
fixed-gap full-support theorem, clipped-source construction and effective
complex-buffer field proof; the existing program now tracks fixed-width,
conditioning and switch tasks toward all-height/all-time analytic coverage.
[Note 46](notes/46_NOTES42_45_MANUSCRIPT_CONSOLIDATION_20261025.md),
[Review 28](reviews/28_NOTES42_45_CONSOLIDATION_PRODUCTION_ASSESSMENT_20261025.md).
For Edward Baker with LLM assistance, gpt-6-astra, actual effort max.

2026-10-25 — **Notes 47–50 manuscript integration.** Heat-density investigation;
[maintained source](manuscript/main.tex), [hash-bound build](manuscript/BUILD_RECORD_20261025_CHAT0018.json),
working tree, no commit/tag or snapshot. The 101-page version derives finite,
moving/switch and temporal budgets, leading with all-height coverage through
97 and the conditional positive gate. [Note 52](notes/52_NOTES47_50_MANUSCRIPT_INTEGRATION_20261025.md),
[Review 33](reviews/33_NOTES47_50_REVIEW_AND_INTEGRATION_20261025.md),
[next steps](notes/53_NEXT_STEPS_AFTER_TEMPORAL_ASSEMBLY_20261025.md).
For Edward Baker with LLM assistance, gpt-6-astra, actual effort max, chat 0018.


2026-10-25 — **All-time construction and source-cost integration.** Heat-density
investigation; [maintained source](manuscript/main.tex),
[hash-bound 112-page build](manuscript/BUILD_RECORD_20261025_CHAT0020.json),
working tree, no commit/tag or snapshot. Integrates Notes54–55 with effective
positive/compact proofs, both endpoints and fixed-central/direct-source
conditioning. [Note56](notes/56_NOTES54_55_MANUSCRIPT_INTEGRATION_20261025.md),
[Review36](reviews/36_NOTES54_55_REVIEW_AND_INTEGRATION_20261025.md),
[outlook](notes/57_PROGRAM_OUTLOOK_AFTER_ALL_TIME_CONSTRUCTION_20261025.md).
For Edward Baker with LLM assistance, gpt-6-astra, actual effort max, chat0020.


2026-10-26 — **First Book synthesis.** Heat-density investigation;
[new maintained source](book/main.tex), [build record](book/BUILD_RECORD_20261026.json),
working tree, no commit/tag or snapshot. Unifies the negative recurrence,
positive fixed-order hierarchy/compact bridge, global physical construction
and source/evaluation results; technical companions retain proof ownership.
[Revision plan](notes/63_BOOK_SYNTHESIS_AND_COMPANION_REVISION_PLAN_20261026.md),
[production review](reviews/42_BOOK_SYNTHESIS_PRODUCTION_REVIEW_20261026.md),
[continuation](notes/64_BOOK_CONTINUATION_20261026.md).
For Edward Baker with LLM assistance, gpt-6-astra, actual effort max, chat0023.


2026-10-26 — **Research after Book continuation.** Heat-density working
tree at [Return66](notes/66_BOOK_RESEARCH_RETURN_20261026.md), no new
snapshot/commit. Named switch centers are paid below rounding width;
negative exp(-L²/4) delivered comparison extends to[1/L,2] at stated
sufficient onset and revised quadrature cost. [Ansatz Assessment16](ansatz/reviews/16_NAMED_SWITCH_CENTERS_ASSESSMENT_20261026.md),
[Recurrence Review14](recurrence/reviews/14_MOVING_ENDPOINT_ASSESSMENT_20261026.md).
For Edward Baker with LLM assistance, gpt-6.1-sol, actual ultra, base0025;
internal same-model checks, physical consumers and software still open.


2026-10-26 — **Companion integration HDA-B01.** Current [Book](book/main.tex), [parent](manuscript/main.tex), [ansatz](ansatz/manuscript/main.tex) and [recurrence](recurrence/manuscript/main.tex) source trees; no snapshot or commit. Full positive/source/evaluator proofs integrated, common contracts and durable proof links reconciled, subsequent closed-source supplements linked. See [Note65](notes/65_BOOK_COMPANION_INTEGRATION_20261026.md), [Review43](reviews/43_BOOK_COMPANION_INTEGRATION_PRODUCTION_REVIEW_20261026.md) and linked fresh build/hash records. For Edward Baker with LLM assistance, gpt-6.1-sol, actual effort ultra, chat0024. Scientific scopes retained.


2026-10-26 — **Fixed-P4 switch physical consumer.** Heat-density research
working tree at [Ansatz Note23](ansatz/notes/23_FIXED_P4_PHYSICAL_TUPLE_20261026.md),
no new manuscript snapshot/commit. All requested physical rates on
[63,65] close, including actual covariance, direct time and residual
defects. [Assessment17](ansatz/reviews/17_FIXED_P4_PHYSICAL_TUPLE_ASSESSMENT_20261026.md),
[AN02 disposition](ansatz/research-progress/handoffs/HDA-A03-AN02.md).
For Edward Baker with LLM assistance, gpt-6.1-sol, actual ultra, same
base0025; symbolic onset, same-model checks and wider open scopes retained.

2026-10-26 — **A08 first small-positive slab.** Research working tree,
[Ansatz Note24](ansatz/notes/24_SMALL_POSITIVE_SLAB_20261026.md)/[Assessment18](ansatz/reviews/18_SMALL_POSITIVE_SLAB_ASSESSMENT_20261026.md).
Complete full-buffer canonical[1/2,1] field/jets/time arithmetic power
X^(-t log2/4), exact residual and endpoint match. AN01 CLOSED; wider
range/zero/physical/cost/audit remain separate. No snapshot, commit or
new build. Edward Baker with LLM assistance, gpt-6.1-sol, actual ultra,
base0025; symbolic onset and internal same-model assessment.

2026-10-26 — **Corrected[3/4,33] field bridge.** Working-tree
[Ansatz Note25](ansatz/notes/25_INTERMEDIATE_POSITIVE_COMPARISON_20261026.md)/[Assessment19](ansatz/reviews/19_INTERMEDIATE_POSITIVE_COMPARISON_ASSESSMENT_20261026.md)
closes A08-AN02 at complete B1, buffered jets/direct time, residual and
both overlaps; fixed-T high-height atlas[1/2,T] with prior sources.
No snapshot/commit/build. Edward Baker with LLM assistance, gpt-6.1-sol,
actual ultra, base0025. Symbolic onset, internal same-model assessment;
near-zero/physical/core/cost/audit remain separate.

2026-10-26 — **Final moving-band result and base0025 handoff.** Research
working tree at [Ansatz Note26](ansatz/notes/26_RETAINED_ARITHMETIC_MOVING_POSITIVE_BAND_20261026.md)/[Assessment20](ansatz/reviews/20_RETAINED_ARITHMETIC_MOVING_BAND_ASSESSMENT_20261026.md).
Retained arithmetic4/L<=t<=1 at eta=Lambda²X^-3/4 and both overlaps;
high-height positive atlas[0,T] with inherited sources. [Summary67](notes/67_CHAT0025_RESEARCH_SUMMARY_AND_HANDOFF_20261026.md)
records all chat results and prepared B02 production. No snapshot/commit/
build. Edward Baker with LLM assistance, gpt-6.1-sol, actual ultra;
symbolic onset, same-model assessment and separate physical/cost/audit gates.

2026-10-26 — **B02 r2 preparation and application priorities.** Heat-density
working-tree [Plan68](notes/68_MANUSCRIPT_UPDATE_PLAN_AFTER_RH_APPLICATION_REVIEW_20261026.md)
and [Continuation69](notes/69_CONTINUATION_AFTER_APPLICATION_REVIEW_20261026.md);
no snapshot/commit or new manuscript build. Reconciles the current
overview and assigns the six regional proofs to their companion homes,
with lower-margin/exterior-energy priorities from
[Review44](reviews/44_HEAT_DENSITY_TO_RH_APPLICATIONS_REVIEW_20261026.md)
and the newer RT Note02. For Edward Baker with LLM assistance,
gpt-6-astra, actual effort max, base0026. B02 remains prepared for Sol;
scientific acceptance states are unchanged.

2026-10-26 — **B02 r2 regional integration and application frontier.**
Working-tree milestone bound by [Note70](notes/70_B02_R2_MANUSCRIPT_INTEGRATION_20261026.md),
[four-source/PDF records](notes/70_B02_R2_PRODUCTION_VERIFICATION_20261026.json)
and [Review45](reviews/45_B02_R2_MANUSCRIPT_INTEGRATION_PRODUCTION_ASSESSMENT_20261026.md).
Six regional arguments now have integrated companion proof homes, exact
parent interfaces and a current Book atlas/conditional application account;
four clean builds and rendered QA. No snapshot/commit or scientific gate
upgrade. Edward Baker with LLM assistance, gpt-6.1-sol, actual ultra, chat0027.
