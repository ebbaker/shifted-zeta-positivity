# Heat-density asymptotics and averaged evolution

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.

**Current consolidation, 25 October 2026, chat 0016:** the maintained
manuscript is now **92 checked pages**, including Notes 42–45's fixed-gap
full-support spatial comparison, constructive clipped-positive source and
effective complete outer field/jet proof. [Note 46](notes/46_NOTES42_45_MANUSCRIPT_CONSOLIDATION_20261025.md)
and [Review 28](reviews/28_NOTES42_45_CONSOLIDATION_PRODUCTION_ASSESSMENT_20261025.md)
record integration and checks. The author's goal remains an analytic
approximation for every real height and time, with useful errors extending
to infinity and both time endpoints. The existing overview/progress now
track fixed-width time coverage, core conditioning and switch assembly.
**Next: Analysis — Sol**, [HDA-18-AN04 r1](research-progress/handoffs/HDA-18-AN04.md).
HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled are unchanged.
Prepared for Edward Baker with LLM assistance, gpt-6-astra, actual effort max.

Study the **average shape of the unnormalized density**

\[
\rho_\epsilon(t,z)=
\frac{\epsilon^2|H_z(t,z)|^2}
{\pi\bigl(|H(t,z)|^2+\epsilon^2\bigr)^2},
\qquad H_t=-H_{zz},
\]

in the [source manuscript](../../investigations-4/12_height_dependent_heat_contours/manuscript/book.tex).
The author's clarifications govern this investigation: preserve the density's
absolute scale, focus on average behavior rather than individual peaks,
and allow **time averaging as well as spatial averaging**.

The research sequence is to determine the two infinite heat-time limits,
derive the averaged evolution with fluctuation corrections, and solve a
compatible boundary problem. Three research rounds have produced finite
pilots and analytic endpoint estimates. The maintained analytical manuscript now incorporates results through Notes 42–45,
with the scoped Note 38 interpretation, including negative and positive
evolution, actual covariance, gamma static comparison and inner overlap,
alongside the adaptive regulator,
explicit differentiated clock and finite-source comparison. The
full evolution closure and boundary solve remain open.

[Note 11](notes/11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md) gives an
all-real-height negative-time Gaussian density approximation with an
explicit O(T^-3) error, plus a conservative global positive-time hierarchy.
[Note 12](notes/12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md)
gives a positive-time coarse clock on growing height windows, with density,
Vandermonde and Hessian error bounds. Its stationary interpretation uses
unfolding: the physical intensity still grows like log(t)/(4pi). The
fixed-regulator clock limit is not uniform over the whole height axis.
Proofs are in-note and same-assistant reviewed; numerical observations
remain floating. Task status belongs to the sole progress register.
The [analytical manuscript](manuscript/README.md) consolidates the
proofs, with brief numerical backup in the appendix and
references to the detailed notes. The [integration note](notes/21_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261024.md)
and [review](reviews/07_ANALYTICAL_MANUSCRIPT_INTEGRATION_SELF_REVIEW_20261024.md) record the earlier rewrite.
The current 92-page integration is pinned by the [build record](manuscript/BUILD_RECORD_20261025.json)
and [production assessment](reviews/28_NOTES42_45_CONSOLIDATION_PRODUCTION_ASSESSMENT_20261025.md).
[Note 14](notes/14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md)
derives the potential forcing, curvature correction and current source for
epsilon depending on height and time. It adds a weak bias bound and
adaptive endpoint profiles, including an explicit saddle-based regulator
that preserves the positive inner-window error.
[Note 16](notes/16_ADAPTIVE_FORCING_AND_DIFFERENTIATED_CLOCK_20261024.md) bounds the adaptive forcing, signed source,
finite-epsilon weak current and density time derivative on the inner
growing window. Complete source differentiation gives a moving-clock
transport error O(L*kappa^-7/6); finite lattice phase is retained.
These are proved-in-note results with same-assistant checks, supported
by six floating theta contour observations. At that checkpoint covariance closure, outer-height approximation and
boundary stability remained open; Notes 30--31 below supply later
outer comparison, while closure and full boundary assembly remain open.
[Note 19](notes/19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md)
now gives a formula using only the explicit saddle and five exact
periodic-polynomial density terms. It removes the L^-3 phase allowance
and retains the differentiated growing-window error. [Note 20](notes/20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md)
defines a global regulator and a finite-source connection with paid
jet and actual covariance errors; a useful full-transition mesh and
all-time theorem remain open. [Note 23](notes/23_FINITE_TRANSITION_CONTRACT_AND_LOCAL_BOUNDS_20261024.md)
now declares a first transition contract and sharpens its cellwise source,
amplitude-aware nonlinear and actual covariance bounds. The bounded
192-cell trial fails the declared tolerances; its arithmetic and filtering
failures are retained. The new lemmas are integrated in the maintained
manuscript; no uniform numerical certificate or full transition is claimed.
For the next session, use the current assignment in the
[progress register](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md).
[Note 39](notes/39_MANUSCRIPT_ANALYTICAL_RECOMMENDATIONS_20261024.md) gives
the requested analytical manuscript recommendations; [HDA-10-MI2 r1](research-progress/handoffs/HDA-10-MI2.md)
is now CLOSED at checked 78-page production scope; [Note 41](notes/41_NOTE39_MANUSCRIPT_IMPLEMENTATION_20261024.md) records the implementation. [Note 38](notes/38_PHASE_TRANSITION_LITERATURE_AND_JOIN_DIAGNOSTICS_20261024.md)
and [Review 21](reviews/21_NOTES35_37_PROJECT_AND_JOIN_ASSESSMENT_20261024.md)
separate the known regulator crossover from the new correlation/response
question. HDA-21 is Ready for a bounded analytical specification.

[Note 34](notes/34_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_20261024.md) supplies
compact transfer and a local time-join estimate. Notes 35–37 supply
sharper source/local bounds and positive Hermite remainders; AN01–AN03
are closed at diagnostic scope. The next numerical input is a separate
frozen-point arithmetic/filter certificate — Sol. HDA-17 remains Partial
and HDA-18 Gated by useful continuous budgets and global spatial assembly.
The maintained manuscript includes Notes 34–37 and the scoped Note 38 outlook. Note 32 retains the
broader assembly specification, under the current model workflow.

For the preceding endpoint result, read
[Note 31](notes/31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md)
and its [same-assistant review](reviews/13_POSITIVE_EVOLUTION_AND_COVARIANCE_SELF_REVIEW_20261024.md),
using [Note 30](notes/30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md)
for the complete field proof. The positive model now has current, time,
forcing/source and actual Q/Delta Q errors O(t^-1/2) uniformly over all
real heights at sufficiently large time. Compact-time outer evolution
also crosses the flat regulator switch. The exact model residual and
both curvature derivatives remain paid. Next is the finite-core and
joining contract; no all-time construction or numerical onset is claimed.

The preceding contract and focused source list are in
[Note 29](notes/29_CONTINUATION_JOINT_OUTER_TO_INNER_MATCHING_20261024.md), the Astra joint-outer-to-inner continuation
and focused reading list. Note 24 retains the preceding entry instructions. Note 22 retains earlier priority decisions; Note 23 and its
[assessment](reviews/08_FINITE_TRANSITION_LOCAL_BOUNDS_SELF_REVIEW_20261024.md)
hold the preceding transition evidence. The earlier additions are
[Note 25](notes/25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md)
and [Note 26](notes/26_NEGATIVE_ENDPOINT_EVOLUTION_AND_COVARIANCE_20261024.md):
explicit outer tails on slabs ending at 64, a scoped positive-cutoff
potential obstruction after 64, and negative all-height evolution/actual
covariance errors. Their
[same-assistant assessment](reviews/09_OUTER_TAIL_AND_NEGATIVE_ENDPOINT_SELF_REVIEW_20261024.md)
records their original scope. [Note 27](notes/27_COMPACT_TIME_GAMMA_OUTER_DENSITY_20261024.md)
now proves a static adaptive outer density on every compact time interval
strictly above 64, using complete gamma convolution, actual root collars
and paid weak regulator bias. Its exact five-term phase formula has
O(log^2|x|/|x|) absolute error throughout both height tails. The regulator
switch needs a nonuniform layer; that compact-time result supplies no
joint overlap or positive evolution comparison. Note 30 supplies the
later static overlap. [Review 10](reviews/10_GAMMA_OUTER_DENSITY_SELF_REVIEW_20261024.md)
is same-assistant only; constants/onset are not numerically instantiated.
[Note 28](notes/28_JOINT_OUTER_REGULATOR_TRANSFER_AND_SWITCH_LAYER_20261024.md) now extends the static comparison across the
regulator switch and into 32<=t<=(log X)/4, with density and averaged
potential spatial-jet error O(X^-3/4(1+log^4 X)). It resolves the narrow
switch layer and pays the gamma model's heat residual. That older outer
threshold has no inner overlap; Note 30 now supplies static overlap with
a different saddle model. Note 31 subsequently supplies positive
current/time/covariance budgets at the stated endpoint and outer scopes. [Review 11](reviews/11_JOINT_OUTER_AND_SWITCH_LAYER_SELF_REVIEW_20261024.md) is same-assistant only.
Notes 25--28 and 30--31 were integrated in the earlier 65-page
manuscript; MI2 adds Notes 34–37 and the scoped Note 38 interpretation. The earlier HDA-10-MI1 r1 remains a completed historical
revision through Note 30; the Review 15 implementation adds Note 31.
The live research statuses above are preserved.

The [research overview](research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md)
and its existing [progress register](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
now prioritize **analytical results extending to infinite height**:
HDA-16/19 now provide the stated endpoint and outer comparisons. The
next HDA-17/HDA-18 work must make their finite-core and joining needs
into an informative all-time contract with complete height coverage. This
supersedes the earlier bounded-window-first schedule. HDA-15 remains
complete at Note 23's scope, and HDA-20 review remains ready. No proof
status is upgraded by this amendment. Every new numerical run must name
the analytical estimate it supports, the decision it can inform and its
stopping rule; see the [numerical policy](numerics/README.md).

**Manual GPT model division, revised 24 October:** GPT-6.1 Sol is the
default for routine and moderately difficult analysis and all numerical
work. Reserve GPT-6 Astra for extra high difficulty analytical tasks.
Edward Baker manages the chats. Follow the [handoff workflow](../../../GPT_RESEARCH_MODEL_WORKFLOW.md)
and the current assignment at the top of the
[progress register](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md).
Sol can complete routine analytical dispositions; escalate only a named
extra high difficulty bottleneck or an author-requested review.

- [Maintained analytical manuscript](manuscript/README.md)
- [Variable-epsilon investigation](notes/14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md)
- [Research overview](research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md)
- [Research progress](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
- [Opening brainstorm](notes/01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md)
- [Filtered evolution and fluctuation identities](notes/02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md)
- [First bounded contract](notes/03_FIRST_BOUNDED_AVERAGING_CONTRACT_20261024.md)
- [Local closure and theta pilot](notes/04_GRADIENT_CLOSURE_AND_ACTUAL_THETA_PILOT_20261024.md)
- [Asymptotic mean shapes and fluctuations](notes/05_ASYMPTOTIC_MEAN_SHAPES_AND_FLUCTUATIONS_20261024.md)
- [Regulator bias and averaged zero counts](notes/06_REGULATOR_BIAS_FOR_SMOOTHED_ZERO_COUNTS_20261024.md)
- [Coarse-transfer contract](notes/08_SECOND_BOUNDED_COARSE_AVERAGING_CONTRACT_20261024.md)
- [Complete-source transfer and weak current](notes/09_COMPLETE_SOURCE_MOMENT_TRANSFER_AND_WEAK_CURRENT_20261024.md)
- [Numerics](numerics/README.md)
- [Reviews](reviews/README.md)
- [References](references/README.md)
- [Chat histories](chat-histories/README.md)
- [Milestone history](DRAFT_HISTORY.md)

Read the [result index](../../../result-summaries/README.md), especially
[collision controls](../../../result-summaries/12_collision_controls_and_screening.md)
and [heat geometry](../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
alongside the [avoid index](../../../avoid/README.md). This is an approximation
program, with no new RH or simplicity criterion.


**Manuscript production handoff, 24 October 2026 (chat 0006):**
[HDA-10-MI1 r1](notes/MANUSCRIPT_INTEGRATION_FOR_SOL_20261024.md) is the
author-requested section-by-section plan for Sol 6.1. Its scope is Notes
25--28 and 30, with later positive-evolution results deferred by the author.
At handoff the manuscript and its recorded PDF were unchanged; the
[input manifest](notes/MANUSCRIPT_INTEGRATION_INPUTS_20261024.json) pins the
reviewed baseline. Prepared for Edward Baker with substantial LLM assistance,
gpt-6-astra, actual effort max.


**Earlier production milestone, 24 October 2026 (chat 0008):** HDA-10-MI1 r1
was implemented in the then-current 54-page local PDF.
[Production assessment](reviews/14_MANUSCRIPT_INTEGRATION_PRODUCTION_REVIEW_20261024.md) and
[current build record](manuscript/BUILD_RECORD_20261024.json). Prepared
for Edward Baker with substantial LLM assistance, gpt-6.1-sol, actual
effort ultra. Positive evolution was deferred under that completed
request; the subsequent Review 15 revision below integrates it without
changing research acceptance or review status.

**Continuation and manuscript review, 24 October 2026 (chat 0007):**
[Review 15](reviews/15_MANUSCRIPT_REVIEW_AND_SOL_RECOMMENDATIONS_20261024.md) recommends the source-bound notation correction,
Note 31 integration, finite inner allowances and an early model/domain guide
for a subsequent Sol revision. That review left its 54-page input
manuscript and PDF unchanged; the implementation is recorded below. [Note 32](notes/32_CONTINUATION_FINITE_CORE_AND_JOINING_20261024.md) was the research handoff at that checkpoint;
no new theorem, numerical task or independent review is claimed.


**Review 15 implemented, 24 October 2026 (chat 0008):** the verified
65-page manuscript now includes Note 31 evolution/covariance and residual
equations, the notation correction, finite inner allowances and early
model guide. [Production assessment](reviews/16_REVIEW15_REVISION_PRODUCTION_ASSESSMENT_20261024.md);
[current build record](manuscript/BUILD_RECORD_20261024.json). Prepared
for Edward Baker with substantial LLM assistance, gpt-6.1-sol, actual
effort ultra. HDA-17/HDA-18 finite-core and joining work and HDA-20
distinct review retain their existing statuses; no numerical run was added.


## AN01 bounded decision — 24 October 2026

[Note 35](notes/35_WEAK_TRANSFER_BUDGET_DECISION_20261024.md) and
[Review 18](reviews/18_WEAK_TRANSFER_BUDGET_ASSESSMENT_20261024.md) close
HDA-17-AN01 r1 as a completed floating diagnostic with retained failure.
The local transfer is preferable for covariance/source; some weak peak rows
remain useful. Source interpolation and peak-sensitive filter integration
fail the budget; arithmetic remains unpaid. The [record](numerics/WEAK_TRANSFER_DIAGNOSTIC_20261024.json)
hashes all small parts. HDA-17 remains Partial and HDA-18 Gated. Next owner:
**Analysis and numerics — Sol**. Model/effort: gpt-6.1-sol, ultra, chat 0011.


## AN02 source/filter gain — 24 October 2026

[Note 36](notes/36_SOURCE_CURVATURE_AND_PEAK_INTEGRATION_20261024.md),
[record](numerics/SOURCE_PEAK_DIAGNOSTIC_20261024.json) and
[Review 19](reviews/19_SOURCE_CURVATURE_AND_PEAK_ASSESSMENT_20261024.md)
close AN02 at bounded floating scope. Continuous source-cap/chord formulas
and one source-only adaptive mesh reduce the zeroth interpolation allowance
24.37 times versus old uniform 768; composite integration settles sampled
actual observables. The source/covariance budget still fails, arithmetic
and continuous integration remain unpaid, and HDA-17/HDA-18 remain
Partial/Gated. Next: positive higher-order finite source — Sol.
Prepared for Edward Baker with LLM assistance, gpt-6.1-sol, ultra, chat 0011.


## AN03 positive-Hermite source — 24 October 2026

[Note 37](notes/37_POSITIVE_HERMITE_SOURCE_AND_REMAINDERS_20261024.md) and
[Review 20](reviews/20_POSITIVE_HERMITE_SOURCE_ASSESSMENT_20261024.md)
close AN03 r1/r2 at bounded diagnostic scope. The nonnegative cubic-Hermite
source has explicit complete-source and ideal-Gauss remainders; same-mesh
interpolation improves about 1963 times with added slope data. R1's source
overrun remains; r2 directional caps give worst sampled source ratio
0.688748 across all 91 rows at the two frozen observations. The
[r1 record](numerics/POSITIVE_HERMITE_DIAGNOSTIC_20261024.json) and
[r2 supplement](numerics/HERMITE_DIRECTIONAL_CAPS_20261024.json) retain cost
and failures. Arithmetic and continuous filter integration remain unpaid;
HDA-17 Partial/HDA-18 Gated. Next fixed-point certification — Sol.
Prepared for Edward Baker with LLM assistance, gpt-6.1-sol, ultra, chat 0011.

**Analytical recommendations and program update, 24 October 2026 (chat 0012):**
[Note 39](notes/39_MANUSCRIPT_ANALYTICAL_RECOMMENDATIONS_20261024.md) and
[MI2 r1](research-progress/handoffs/HDA-10-MI2.md) prepare the next manuscript
revision, with analytical formulas in the text and numerical support by
reference. The overview/progress now include Note 38's crossover,
order-parameter and correlation/response goals. No manuscript build,
new numerical result or proof-status upgrade. Prepared for Edward Baker
with substantial LLM assistance, gpt-6-astra, actual effort xhigh.


**Astra continuation after Sol, 24 October 2026 (chat 0012):**
[Note 40](notes/40_CONTINUATION_ASTRA_AFTER_SOL_20261024.md) and
[HDA-18-A01 r1](research-progress/handoffs/HDA-18-A01.md) prepare the
author-requested post-MI2 analytical review and continuation on one hard
compatibility or differentiated-crossover estimate. Entry requires checking
Sol's actual return; completion is not assumed. Chat 0012's archive was
verified, including the preceding final response. Prepared for Edward
Baker with substantial LLM assistance, gpt-6-astra, actual effort xhigh.
