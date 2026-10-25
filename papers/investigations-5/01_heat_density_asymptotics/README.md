# Heat-density asymptotics and averaged evolution

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.

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
pilots and analytic endpoint estimates. The maintained analytical manuscript now incorporates results through Note 31, including negative and positive
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
The current 65-page integration is pinned by the [build record](manuscript/BUILD_RECORD_20261024.json)
and [production assessment](reviews/16_REVIEW15_REVISION_PRODUCTION_ASSESSMENT_20261024.md).
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
For the next research session, start with
[Note 32](notes/32_CONTINUATION_FINITE_CORE_AND_JOINING_20261024.md), which specifies the finite-core and joining deliverable.
For the latest mathematical result, read
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
Notes 25--28 and 30--31 are now integrated in the maintained 65-page
manuscript. The earlier HDA-10-MI1 r1 remains a completed historical
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

**Manual GPT model division:** GPT-6 Astra leads analytical formulas and
proofs; GPT-6.1 Sol handles all numerical work. Edward Baker manages the
chats. Follow the [handoff workflow](../../../GPT_RESEARCH_MODEL_WORKFLOW.md)
and the current assignment at the top of the
[progress register](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md).
Each numerical request returns to Astra for analytical assessment.

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
manuscript and PDF unchanged; the implementation is recorded below. [Note 32](notes/32_CONTINUATION_FINITE_CORE_AND_JOINING_20261024.md) is the current research handoff;
no new theorem, numerical task or independent review is claimed.


**Review 15 implemented, 24 October 2026 (chat 0008):** the verified
65-page manuscript now includes Note 31 evolution/covariance and residual
equations, the notation correction, finite inner allowances and early
model guide. [Production assessment](reviews/16_REVIEW15_REVISION_PRODUCTION_ASSESSMENT_20261024.md);
[current build record](manuscript/BUILD_RECORD_20261024.json). Prepared
for Edward Baker with substantial LLM assistance, gpt-6.1-sol, actual
effort ultra. HDA-17/HDA-18 finite-core and joining work and HDA-20
distinct review retain their existing statuses; no numerical run was added.
