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
pilots and analytic endpoint estimates. The maintained analytical manuscript now incorporates the adaptive
regulator, explicit differentiated clock and finite-source comparison. The
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
and [review](reviews/07_ANALYTICAL_MANUSCRIPT_INTEGRATION_SELF_REVIEW_20261024.md) record the current rewrite.
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
by six floating theta contour observations. Full covariance closure,
outer-height approximation and boundary stability remain open.
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
For a new chat, start with
[Note 24](notes/24_CONTINUATION_FOR_GPT_ASTRA_INFINITE_HEIGHT_ANALYSIS_20261024.md), the Astra infinite-height continuation and focused
reading list. Note 22 retains earlier priority decisions; Note 23 and its
[assessment](reviews/08_FINITE_TRANSITION_LOCAL_BOUNDS_SELF_REVIEW_20261024.md)
hold the latest mathematical evidence.

The [research overview](research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md)
and its existing [progress register](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
now prioritize **analytical results extending to infinite height**:
HDA-19 positive outer-height analysis first, with HDA-16 endpoint evolution
estimates. HDA-17 finite-transition work supports identified analytical
needs; HDA-18 must assemble complete time and height coverage. This
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
