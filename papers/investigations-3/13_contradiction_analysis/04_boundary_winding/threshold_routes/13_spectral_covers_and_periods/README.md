# Spectral covers and periods

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

**BW-13 — Direction C.** The first local period calculation is complete.
Its first correction reduces exactly to the event four-jet; a new global
source constraint and a useful finite theta comparison are still missing.

Study the direct spectral family w²=H(t,z), built from the complete
heat function. Multiple zeros become singular fiber points, and their
vanishing cycles carry measurable period behavior. The program asks
whether an estimate using the unchanged theta source improves on the
universal degeneration already present in polynomial heat models.

## Start here

- [Research overview][overview]: object, inherited evidence, controls and bounded work.
- [Research progress][progress]: initial task statuses and next deliverable.
- [Originating proposal note][proposals]: Direction C and the shared screen in Section 7.
- [BW10 manuscript][manuscript]: the RH-conditional baseline and remaining simplicity problem.

## First research result and next step

[Note 01][n01] fixes a finite spectral disk and transported nodal cycle,
subtracts the quadratic period, and bounds the remainder with complete
theta moments through order six. The first correction is
\((5h_3^2-3h_2h_4)/(48h_2^2)\), a combination of the existing BW-08
deflated jet and a square. A same-input coefficient comparison is
therefore closed without a new exclusion or information gain.

The result has [same-assistant self-review][review01] and
[exact/floating polynomial checks][numerics]; no theta numerical pilot
or independent review has been completed. Next specify a finite-time
period estimate or source correlation outside that same-four-jet class,
with a matched direct comparator. Higher multiplicity and height
exhaustion remain gated.

## Relationship to the existing programs

[BW-11][A], [BW-12][B] and [BW-13][C] form the related physical-geometry
group suggested in the proposal note. They have separate registers
and share source controls and boundary accounting.
The source note also suggests possible future grouping; these folders
preserve all five individual proposals for continuation.

The initial opening only organized the program; the first analytic
research and scoped comparison are now linked above. Inherited claims
retain their recorded review status. [HMC-05 remains open and HMC-06 gated][hmc]. Consult the
[result index][results] and [avoid index][avoid], especially
[control matching][controls] and [target classification][a01].

## Research records

Save new derivations in notes/, computations and small receipts in
numerics/, and assessments in reviews/ as work begins. Keep the overview
and progress register current. Maintain DRAFT_HISTORY.md for substantive
milestones using commits or tags; create no manuscript snapshot folders.
Follow [the large-file policy][large].

The shared setup conversation is recorded once in [the boundary-winding
archive][history]. Register future route-specific conversations in this
route's chat-histories/ through [the history workflow][history-policy],
preserving existing registrations. This conversation is registered in
[the route chat archive][route-history].

[All threshold routes][routes].

[n01]: notes/01_NODAL_PERIOD_VARIATION_AND_FOUR_JET_COMPARISON_20261021.md
[review01]: reviews/01_NODAL_PERIOD_SELF_REVIEW_20261021.md
[numerics]: numerics/README.md
[route-history]: chat-histories/README.md
[A]: ../11_global_physical_jet_geometry/README.md
[B]: ../12_relative_chern_hopf_charges/README.md
[C]: README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[history]: ../../chat-histories/0008_2026-10-21T16-44-53Z_create-proposal-research-folders.json
[history-policy]: ../../../../../../tools/CHAT_HISTORY.md
[hmc]: ../10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[large]: ../../../../../../LARGE_FILES.md
[manuscript]: ../10_rh_implies_simple_zeros/manuscript/main.tex
[overview]: research-overview/01_SPECTRAL_COVERS_AND_PERIODS_PROGRAM_20261021.md
[progress]: research-progress/01_SPECTRAL_COVERS_AND_PERIODS_PROGRESS_20261021.md
[proposals]: ../10_rh_implies_simple_zeros/brainstorm/04_GLOBAL_HEAT_GEOMETRY_PROPOSALS_AND_INITIAL_SCREENS_20261021.md
[results]: ../../../../../../result-summaries/README.md
[routes]: ../README.md
