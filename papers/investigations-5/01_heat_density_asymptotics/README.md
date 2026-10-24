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

The research sequence is to characterize negative- and positive-time
values, derive the averaged evolution with its local fluctuation
corrections, solve a compatible boundary problem, and constrain the
solutions against the actual theta heat flow. The first bounded round
derives a local covariance approximation,
negative-time mean and fluctuation coefficients, and an exact cosine-cell
mean with its covariance. A useful uniform theta error bound remains open.

The first averaging contract and 17-case theta pilot are complete.
The next work is positive-time coarse-average transfer and regulator-bias
control; no boundary-matched reduced solution has been obtained.
The progress register owns task status. Start a new chat with the
[continuation note](notes/07_CONTINUATION_FOR_NEW_CHAT_20261024.md).

- [Research overview](research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md)
- [Research progress](research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
- [Opening brainstorm](notes/01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md)
- [Filtered evolution and fluctuation identities](notes/02_FILTERED_EVOLUTION_AND_FLUCTUATION_IDENTITIES_20261024.md)
- [First bounded contract](notes/03_FIRST_BOUNDED_AVERAGING_CONTRACT_20261024.md)
- [Local closure and theta pilot](notes/04_GRADIENT_CLOSURE_AND_ACTUAL_THETA_PILOT_20261024.md)
- [Asymptotic mean shapes and fluctuations](notes/05_ASYMPTOTIC_MEAN_SHAPES_AND_FLUCTUATIONS_20261024.md)
- [Regulator bias and averaged zero counts](notes/06_REGULATOR_BIAS_FOR_SMOOTHED_ZERO_COUNTS_20261024.md)
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
