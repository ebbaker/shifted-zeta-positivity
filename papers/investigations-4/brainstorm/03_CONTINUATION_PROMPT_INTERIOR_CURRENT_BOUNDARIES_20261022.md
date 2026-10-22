# Continuation prompt: interior-current boundaries and backward survival

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from this turn’s metadata.

Copy the prompt below into a new research session, or ask it to read this
file and execute the prompt. Saving this file does not create a chat or
start future work. The [overview][overview] and [progress register][progress]
are authoritative; update those files rather than making dated duplicates.

## Prompt for the new session

Work in `/Users/ebbaker/Documents/shifted-zeta-positivity` on the
interior-current boundaries and backward-survival program in
`papers/investigations-4/`. Begin the next uncompleted task in its dedicated
ICW register. Carry the first bounded candidate analysis through to a
proved estimate or a clearly scoped failure, with a note, appropriate
review/checks and updated progress. Do not stop after restating this plan.

Read, in order:

1. Repository `AGENTS.md`, `LARGE_FILES.md`, `tools/CHAT_HISTORY.md`,
   `result-summaries/README.md` and `avoid/README.md`.
2. `papers/investigations-4/research-overview/02_INTERIOR_CURRENT_BOUNDARIES_AND_BACKWARD_SURVIVAL_PROGRAM_20261022.md`.
3. `papers/investigations-4/research-progress/02_INTERIOR_CURRENT_BOUNDARIES_AND_BACKWARD_SURVIVAL_PROGRESS_20261022.md`.
4. `papers/investigations-4/03_heat_transport_and_charges/notes/02_INTERIOR_CURRENT_WALLS_AND_BACKWARD_SURVIVAL_20261022.md`
   and its corresponding Review 02. Read Note 01 when root-wall/cap scope
   is needed, and follow the overview’s BW09/BW10 source links.
5. The shared Investigations 4 program/register and home 02’s theta-source
   contract for cross-program dependencies. Source records prevail over summaries.

The user’s idea is to start a moving boundary between two zeros and follow
a current to cancel boundary flux. The main proposed strengthening is to
prove backward survival of **two distinct scalar-energy current paths**.
For H_t=-H_xx, that current is v_0=2H_x/H. Under the explicitly justified
all-real product assumptions, v_0,x=-2Q/H²<=0; two paths remaining in the
same gap throughout 0<t<=T retain at least their separation at T. This
would prevent collapse of that pair. The lemma is already available;
**the theta-specific survival estimate is missing**.

Keep three different velocities separate: scalar current 2H_x/H, jet-energy
current 2H_x(H+H_xx)/(H²+H_x²), and phase current Q_x/Q. Phase cancellation
does not imply scalar-flux cancellation. One surviving path, bounded speed,
forward trapping, or survival only on [epsilon,T] does not prove endpoint
noncollision. Q>=0 is not assumed for arbitrary heat fields or an unknown
nonreal regime. An RH-conditional simplicity argument must say it assumes RH.

Start ICW-02 unless the latest ledger has moved beyond it. Select one
explicit canonical-source continuation contract with a declared T, gap
or parameterized window, initial paths, source observations and complete
error budget. Explain how it could control root hitting and the singular
H denominator without assuming an unknown endpoint gap/floor. Include the
epsilon->0 obligation and the strongest direct same-information comparator.
Default to the two-scalar-path route. If choosing the c=0 phase-amplitude
alternative, justify the choice and keep it a single primary pilot.

For that alternative, H_x=0 and the complete cosine moments satisfy
S_1=0, q=C_2/C_0. A signed bound is sigma(C_2-kC_0)<=0 with
sigma=sign C_0. The exact amplitude identity is already known; obtain a
new coupled theta estimate rather than restating it. Retain unchanged
coefficients, complete reflection, full tails, wall uncertainty and event
matching. A uniform finite integral budget preserves amplitude; a bound
kappa log(T/epsilon)+C with kappa<1 excludes an ordinary double only.
No such theta budget has been proved in this program.

Run the mandatory analytic screen before a numerical campaign. For
H=x²-2t, only the central scalar-current path survives backward to zero;
all noncentral ones hit a root at positive time. Phase walls can all remain
interior with bounded speed while their first jet collapses. A general
real-analytic ordinary double also admits regular H_x=cH walls with
q=1/t+O(1). For each additional arithmetic collision control, identify a failed premise
of any claimed exclusion, or explain why the estimate correctly remains
compatible with its collision. Do not invent event or continuation data.

Save incremental research in home 03’s notes/, small computations and
receipts in numerics/, and assessments in reviews/. Cross-link any shared
canonical-source result kept in home 02. Include Edward Baker, LLM
assistance and your **actual** model/effort; do not copy the present session’s
configuration as your own. Keep the ICW register current and the parent
I4 ledger at summary level. I4-H01’s complete complex-boundary task and
all-height/higher-multiplicity work stay gated without their own estimates.
Do not revive the failed compact-circle candidates or create manuscripts,
snapshot folders, a broad zero sweep or duplicated ledgers for this pilot.

At the beginning, register or refresh your **actual new chat identity and
title** in `papers/investigations-4/chat-histories/` through
`tools/refresh_chat_history.py`, following `tools/CHAT_HISTORY.md`. The
originating conversation is 0006 with thread ID
`01a1617d-bf0c-7813-a82b-e9e0092f3525`; that is a historical pointer, **not
an ID to use for your new session**. Preserve its registration and founding
0005. Use the next number assigned by the tool. Refresh completed public
text before finishing and arrange the exact-turn final capture. Verify
source/hash/identity checks and report failures rather than fabricating a
complete history. The existing verification receipt is only a dated snapshot.

Finish with the concrete result, its scope and tests/review, file links,
updated task status, and the next genuinely unpaid estimate. A conditional
criterion or failed candidate is not an endpoint exclusion.

[overview]: ../research-overview/02_INTERIOR_CURRENT_BOUNDARIES_AND_BACKWARD_SURVIVAL_PROGRAM_20261022.md
[progress]: ../research-progress/02_INTERIOR_CURRENT_BOUNDARIES_AND_BACKWARD_SURVIVAL_PROGRESS_20261022.md
[prompt]: ../brainstorm/03_CONTINUATION_PROMPT_INTERIOR_CURRENT_BOUNDARIES_20261022.md
[parent]: ../research-overview/01_COMPACT_GEOMETRY_HEAT_TRANSPORT_AND_WEIL_POSITIVITY_PROGRAM_20261021.md
[parent-progress]: ../research-progress/01_COMPACT_GEOMETRY_HEAT_TRANSPORT_AND_WEIL_POSITIVITY_PROGRESS_20261021.md
[home]: ../03_heat_transport_and_charges/README.md
[source-home]: ../02_theta_source_constraints/README.md
[note1]: ../03_heat_transport_and_charges/notes/01_ZERO_FOLLOWING_BOUNDARIES_AND_REMAINING_FLUX_20261021.md
[note2]: ../03_heat_transport_and_charges/notes/02_INTERIOR_CURRENT_WALLS_AND_BACKWARD_SURVIVAL_20261022.md
[review]: ../03_heat_transport_and_charges/reviews/02_INTERIOR_CURRENT_WALL_REVIEW_20261022.md
[results]: ../../../result-summaries/README.md
[geometry]: ../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../avoid/README.md
[a01]: ../../../avoid/01_restating_the_target.md
[a02]: ../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
[a20]: ../../../avoid/20_volume_without_a_gain.md
[product]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/23_CAP_PHASE_CONCENTRATION_AND_FINITE_TIME_BASELINE_20261021.md
[critical]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/05_TOPOLOGICAL_ALTERNATIVES_AND_ENERGY_OBSERVATIONS_20261020.md
[phase]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/06_HEAT_FLOW_CONTOURS_AND_GAUSSIAN_CAP_ENERGY_20261020.md
[history-policy]: ../../../tools/CHAT_HISTORY.md
[large]: ../../../LARGE_FILES.md
[chat-guide]: ../chat-histories/README.md
[chat]: ../chat-histories/0006_2026-10-22T02-43-13Z_review-research-continuation-prompt.json
[verification]: ../chat-histories/CHAT_HISTORY_VERIFICATION_20261022.json
