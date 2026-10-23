# Late heat caps and charge transport

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**, verified from the active turn metadata.

**Status: geometry and canonical late-cap estimates proved in-note; complete closures evaluated; endpoint exclusion remains open.**

Analytical execution, 22 October 2026, for Edward Baker with substantial LLM assistance: actual **gpt-6-astra (Codex), effort ultra**. The [four research notes](notes/README.md) and [internal review](reviews/03_FINITE_TUBES_CAPS_AND_CLOSURES_INTERNAL_REVIEW_20261022.md) complete the declared finite/growing-interval geometry and cap tasks. The sole [progress register][progress] records the remaining signed-estimate and exclusion obligations.
This investigation asks whether the actual theta heat field at large real
heat time supplies a cap estimate which, together with controlled moving
sides and closing pieces, excludes a multiple zero at time zero under RH.
Late-time pair statistics are a possible input to that estimate. Proving
a particular PCC formulation is not imposed as a prerequisite when direct
field or normalized-jet asymptotics can address the cap.

Start with the [research overview][overview] and the sole detailed
[progress register][progress]. The [founding assessment][assessment]
contains the exact cap bounds, finite-cluster pair identity and controls
that motivated this direction; it remains at its original source path.
The [setup review][review] assesses the program and its scope, not a new
theta theorem.

The [continuation note](brainstorm/01_CONTINUATION_PROMPT_LATE_HEAT_CAPS_AND_CHARGE_TRANSPORT_20261022.md) has now been executed. Start from the current [progress register][progress] for further work; its original unstarted state is historical.

The analytical priorities are:

1. Specify a complete regular boundary containing the candidate event,
   with every early cap, linking sphere, imaginary-time face and chart seam.
2. Construct genuine zero-following projective sides and prove their
   continuation or retain their complete connector flux.
3. Derive uniform complex-time asymptotics for the full normalized jet on
   the chosen late cap, including its possibly nonzero reference flux.
4. If useful, convert weighted late-heat root statistics into a cap bound,
   paying small gaps, the exterior factor and complex-time phase.
5. Prove a complete signed charge bound with a strict margin below one;
   then address arbitrary candidate height and every multiplicity.

For G=(H,H_z), the complete charge is

\[
 Q_W=\frac1{4\pi^2}\int_{\partial W}\mathcal A\wedge d\mathcal A
     =\sum_{p\in W}\binom{m_p}{2},\qquad
 \mathcal A=\frac{\operatorname{Im}(G^*dG)}{|G|^2}.
\]

On an early-to-late tube, Q_W=I_T-I_-+S_T. Vanishing sides leave both
caps. If a full regular enclosing boundary really has only one nonzero
cap contribution, that cap itself equals Q_W. These conditional identities
are inherited; an independently proved theta estimate is the research task.

The limit is real heat time T tending to positive infinity, not zero
height tending to infinity. The established fixed-rank late-time theta
profile is cosine-like. [Note 02](notes/02_COMPLEX_TIME_THETA_JETS_AND_LATE_CAPS_20261022.md) now gives a complete canonical cap estimate on its actual projective root disks, including a nonzero fixed-width limit. No growing-population PCC theorem is claimed. [Note 04](notes/04_IMAGINARY_TIME_CLOSURE_CONCENTRATION_20261022.md) retains the complete charge in the closures; cap smallness alone supplies no exclusion.

Numerics support analytical work through exact identity checks, adverse
models and, after a theorem is specified, finite interval bounds for its
constants. Zero plots, fitted correlation curves and height sweeps do not
replace a proof of the asymptotic cap or a uniform boundary contract.
See [numerical guidance](numerics/README.md).

This home owns LHCT tasks. [Home 10][mass] retains CHB mass/trace tasks;
[home 03][transport] retains its broader heat-transport work;
[home 02][source] supplies the unchanged canonical source. No parent or
sibling exclusion gate is upgraded by this setup.

Follow the [result index][results], [avoid index][avoid],
[collision controls][controls], [heat-geometry summary][geometry],
[large-file policy][large] and [history policy][history-policy].
Save derivations in notes/, small computations in numerics/, assessments
in reviews/, and concise milestones in [DRAFT_HISTORY.md](DRAFT_HISTORY.md).
[Chat-history guidance](chat-histories/README.md) points to the founding
conversation's unique existing archive.

[overview]: research-overview/01_LATE_HEAT_CAPS_AND_CHARGE_TRANSPORT_PROGRAM_20261022.md
[progress]: research-progress/01_LATE_HEAT_CAPS_AND_CHARGE_TRANSPORT_PROGRESS_20261022.md
[assessment]: ../10_chern_hopf_integral_estimates/notes/03_LATE_HEAT_PAIR_STATISTICS_AND_CAP_FLUX_20261022.md
[review]: reviews/01_SETUP_AND_ANALYTICAL_PROGRAM_REVIEW_20261022.md
[mass]: ../10_chern_hopf_integral_estimates/README.md
[transport]: ../03_heat_transport_and_charges/README.md
[source]: ../02_theta_source_constraints/README.md
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[large]: ../../../LARGE_FILES.md
[history-policy]: ../../../tools/CHAT_HISTORY.md

## Zero counts, pair matrices and RHE — 22 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**. The user's follow-up is developed in a new [overview](research-overview/02_ZERO_COUNT_TRANSPORT_AND_PAIR_MATRIX_PROGRAM_20261022.md) and separate [ZTP progress note](research-progress/02_ZERO_COUNT_TRANSPORT_AND_PAIR_MATRIX_PROGRESS_20261022.md). [Notes 05–08](notes/README.md) consolidate the complete all-zero real cap balance, prove quantitative fixed-rank pair-matrix convergence to a clock, screen PCC-to-cap implications, and derive an exact low-value Hodge count with a canonical-theta corollary using home 09's acquired boundary data. [Review 04](reviews/04_ZERO_COUNTS_PAIR_MATRICES_AND_HODGE_BRIDGE_REVIEW_20261022.md) records the internal audits. The original LHCT ledger remains the sole owner of LHCT tasks; the new register owns ZTP tasks only. The complete signed exclusion is still open.

## Shared manuscript routing — 22 October 2026

The detailed analytic synthesis now lives at the Investigations 4 base: [Zero Counts, Heat Transport, and Localized Hodge Energy](../manuscript/zero_count_heat_transport/README.md), with [PDF](../manuscript/zero_count_heat_transport/main.pdf), [shared overview](../research-overview/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRAM_20261022.md), [progress](../research-progress/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRESS_20261022.md) and [internal review](../reviews/01_ZERO_COUNT_HEAT_TRANSPORT_MANUSCRIPT_REVIEW_20261022.md). Its source crosswalk preserves LHCT Notes 05–08 and the earlier cap/closure records; the main proofs are self-contained, and existing numerics appear only in a supporting appendix. Prepared for Edward Baker with LLM assistance, **gpt-6-astra, ultra**; review remains same-model internal. LHCT/ZTP ownership and open signed-exclusion tasks are unchanged, as is this conversation's unique home 11 history 0001.
