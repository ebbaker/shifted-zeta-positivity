# Continuation for analytic open boundary flux research

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**.

## The author's request

Investigate whether allowing zeros to enter a bounded heat-flow region, with an estimated flux allowance, can permit a useful larger backward width ε at high height and strengthen the estimating tools. **Focus on analytic goals. Numerics have a supporting role.** Start from proofs and source-specific inequalities; do not make a numerical acquisition, a parameter scan or a search for a large ε the opening research task.

Use the [new overview][overview] for the program and the [OBF progress register][progress] for current task status. The first application is RH-conditional simplicity, with almost-all simplicity the first global target compatible with a sublinear allowance. The finite tool is not an RH proof or a new simplicity theorem.

## Read before developing the estimate

1. Read repository [AGENTS.md][agents], [result summaries][results], [patterns to avoid][avoid], [large-file policy][large] and [chat-history workflow][history]. Pay particular attention to [target reformulations][a01], [control premises][a02], [numerics before structure][a10], [coupled estimates][a12], and [scoped exclusions][a07].
2. Read [Brainstorm Note 04][flux] and the new overview/progress pair. Note 04 contains the finite derivation, the exact limitation on enlarging ε and the quadratic/cubic entry controls.
3. Read [HDC Note 05][earlier] for the earlier nonreal and complete projected-pair consumers. Read the [regularized counting note][regularization] for total-divisor transport, which is not already a nonreal-inflow estimate.
4. Read [HDC Note 12][coefficient] for the fixed-population coefficient method, and the [physical contour section][contours] for the different first-jet boundary condition. Consult the [current HDC snapshot][hdc-snapshot] for inherited results and remaining arithmetic work.
5. When choosing source inputs, read the [corrected microscopic reference][reference] and [positive-time height-boundary analysis][height] in their stated regimes. Read the [collision control register][controls] before claiming that a proposed inequality is specific to theta.

## What has been accomplished

The preceding chat reviewed the current manuscript and saved [a high-level assessment][review]. It then derived the elementary open-boundary extension

\[
 N_{\rm nr}(0)=N_{\rm nr}(-\epsilon)
       +J_{\rm in}^{\rm nr}-J_{\rm out}^{\rm nr}-B_{\rm real},
 \qquad
 M_0\le\tfrac32\bigl(N_{\rm nr}(-\epsilon)+J_{\rm in}^{\rm nr}\bigr)
\]

under the stated finite heat-flow conditions and endpoint reality for the full multiplicity consumer. The factor 3/2 is sharp on the cubic entry control. No negative-time theta bound on either resource has been acquired. The first formula's event sum includes t=0 and excludes t=−ε.

Simple wall zeros are allowed by the physical cap when H_z≠0. They do change a fixed prepared polynomial's population. Signed total zero flux, one-sided nonreal entry, and the physical first-jet side integral are three different quantities. Use the one needed by the consumer.

For a fixed region, extending the interval backward increases the exact conservative resource by the outward nonreal flux and real births in the added interval. The potential gain from larger ε must therefore come from a better completed approximation/error estimate or an enlarged useful range, not from a presumed decrease in that exact resource.

## Start with this bounded analytic task

**Work on OBF-01 and the first part of OBF-02.** Produce one substantive analytical note that makes the finite transport and error requirements precise and obtains, or sharply identifies the missing input for, a complete-field inflow bound.

First audit the hard-wall proof. Specify the complete finite population convention, transverse crossings, endpoint treatment, interior events and treatment of a multiple boundary event. Keep the statement for real endpoint multiplicity separate from its RH-based application to all canonical zeros. Check the quadratic and cubic examples analytically, including entry times and orientation.

Then compare two representations: a one-sided boundary current obtained from the full field on the space-time wall, and a smooth window with an explicitly defect-sensitive transport term. For a smooth window, prove the nonreal event balance and integrability before using the proposed positive variation. The total-divisor logarithmic identity by itself is not that proof. Choose the representation offering the clearest route to a source inequality; do not develop both into long parallel programs.

Seek an estimate of the form J_in^nr≤F_θ+E on a declared band, with F_θ bounded through independently available complete-source information. Expose field regularization, the near-real strip, buffer geometry, derivative errors and recrossings. A formula in which F_θ is merely another name for the unknown crossing count is an interface, not the desired estimate. If a uniform wall or H_z floor reappears, identify it explicitly and determine whether the proposed relaxation has actually gained anything.

The first note should end with a precise theorem, an explicit unproved inequality, or a scoped obstruction for the chosen input class. Identify the first point where theta arithmetic, rather than generic heat flow, must enter. Update the OBF register to match that outcome. This is the opening deliverable; it does not require completing the global simplicity program in one chat.

## Carry these constraints into the proof

- A small inflow does not bound the initial nonreal resource N_nr(−ε). OBF-04 is separate and substantive.
- A field/reference formula continued analytically is not an error estimate continued analytically. Existing positive-time real net-flux bounds do not supply negative-time nonreal inflow.
- A smooth cutoff near the real axis may hide precisely the conjugate pairs that create a multiple endpoint. Pay their mass and specify the order of regularization limits.
- A mean density or a finite source fit is not an upper clustering bound. Apply the full collision controls to the actual source premises; none is excluded by the generic flux identity.
- Do not assume a common negative all-real interval or positive semidefiniteness for a complex pair matrix. Do not insert a varying degree into the fixed-degree propagator.
- Distinguish an admissible larger ε from a better estimate at the same target and information. Pay endpoint coverage, overlaps and joins before any all-height conclusion.

Optional exact or interval computations may check signs, constants or a sharply stated model prediction after the analytic question is written down. They remain supporting evidence. A numerical pass does not complete OBF-03, OBF-04 or OBF-05, and more precision is not a response to an unidentified analytic obstacle.

## Files, chat history and completion record

The research checkout is `/Users/ebbaker/Documents/shifted-zeta-positivity`. Keep this continuation's derivations in `papers/investigations-4/12_height_dependent_heat_contours/brainstorm/notes/`, reviews in `reviews/`, and necessary supporting calculations in `numerics/`. Use the next unused filename after inspecting the directory. Keep OBF status in the linked register; existing HDC task status remains with Investigation 12. Record the actual model and effort, author, date and LLM assistance in new notes. Do not create manuscript snapshots or edit synced project reference files.

This originating chat is **Review curved contour manuscript**, thread `01a16a6c-78d1-7353-bf83-a9267a555b0e`, uniquely registered as [brainstorm history 0002][chat]. The [verification receipt][verification] records the checked snapshot and preceding final reply. Preserve this chat's number and registration. A genuinely new chat must register its own actual thread id and title in the brainstorm `chat-histories/` folder; do not reuse history 0002's identity or copy its transcript. If continuing within the same actual chat, refresh its existing registration.

Refresh history at the beginning and end with the repository tool. Unless a trusted completion hook is verified, arrange the bounded exact-turn capture as the final tool action before replying. Never insert a planned answer into a transcript. At the end of the research session, save the proof/obstruction and any assessment, update the OBF register, and state what analytic estimate was obtained and what remains unproved.

[overview]: ../research-overview/01_ANALYTIC_OPEN_BOUNDARY_FLUX_PROGRAM_20261023.md
[progress]: ../research-progress/01_OPEN_BOUNDARY_FLUX_PROGRESS_20261023.md
[flux]: 04_OPEN_BOUNDARIES_ZERO_FLUX_AND_BACKWARD_WIDTH_20261023.md
[review]: 03_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_AND_OBSTACLES_REVIEW_20261023.md
[earlier]: ../../notes/05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md
[regularization]: ../../../11_late_heat_caps_and_charge_transport/notes/08_LOW_VALUE_HODGE_COUNTS_AND_REGULARIZATION_20261022.md
[coefficient]: ../../notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md
[contours]: ../../manuscript/contours.tex
[hdc-snapshot]: ../../research-progress/02_PAIR_SPECTRUM_AND_CURVED_CONTOUR_PROGRESS_20261023.md
[reference]: ../../notes/14_MICROSCOPIC_COMPLETE_REFERENCE_AND_HEAT_DEFECT_20261023.md
[height]: ../../../notes/11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md
[agents]: ../../../../../AGENTS.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a10]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[large]: ../../../../../LARGE_FILES.md
[history]: ../../../../../tools/CHAT_HISTORY.md
[chat]: ../chat-histories/0002_2026-10-23T20-20-56Z_review-curved-contour-manuscript.json
[verification]: ../chat-histories/VERIFICATION_OPEN_BOUNDARY_FLUX_PROGRAM_20261023.json
