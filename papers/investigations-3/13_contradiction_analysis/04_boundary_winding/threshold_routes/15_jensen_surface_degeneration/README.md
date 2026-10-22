# Jensen surface degeneration and resolution

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

**BW-15 — Direction E.** First finite-resolution comparison complete; broader program remains in reserve.

Study how compact surfaces built from complete theta-moment Jensen
polynomials degenerate as degree grows. Finite topology remains compatible
with multiple zeros of the limiting entire function, while root-cluster
scales retain multiplicity information. The program seeks an effective
resolution bound with explicit moment, degree and error costs.

## Start here

- [Research overview][overview]: object, inherited evidence, controls and bounded work.
- [Research progress][progress]: current task statuses, results and next decision.
- [Originating proposal note][proposals]: Direction E and the shared screen in Section 7.
- [BW10 manuscript][manuscript]: the RH-conditional baseline and remaining simplicity problem.

## First research result and next gate

[Note 01][note01] gives a complete local certificate around height 14.1347.
A sharper error bound reduces the sufficient degree from 203,199,427,483
to 46,031,859 at the same 1e-9 approximation-error target, using only 65
retained coefficients and a paid infinite tail. The complete computation
was slower than direct evaluation in both recorded runs, so this particular
single-window comparison stops. Finite simple Jensen roots remain compatible
with a limiting double in the explicit control.

The [progress register][progress] records completed and gated tasks; the
[review][review01] is same-assistant. A new multi-window or period objective
must specify its benefit before further numerical acquisition.

## Relationship to the existing programs

This reserve approximation program is separate from the entire-function
[spectral cover][C] and the [source-transform program][D].
The source note also suggests possible future grouping; these folders
preserve all five individual proposals for continuation.

The original opening organized research without adding a theorem or
certificate; the first research round is now linked above. Inherited
claims retain their recorded review status. [HMC-05 remains open and HMC-06 gated][hmc]. Consult the
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
preserving existing registrations.

[All threshold routes][routes].

[C]: ../13_spectral_covers_and_periods/README.md
[D]: ../14_theta_source_transform_constraints/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[history]: ../../chat-histories/0008_2026-10-21T16-44-53Z_create-proposal-research-folders.json
[history-policy]: ../../../../../../tools/CHAT_HISTORY.md
[hmc]: ../10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[large]: ../../../../../../LARGE_FILES.md
[manuscript]: ../10_rh_implies_simple_zeros/manuscript/main.tex
[overview]: research-overview/01_JENSEN_SURFACE_DEGENERATION_PROGRAM_20261021.md
[progress]: research-progress/01_JENSEN_SURFACE_DEGENERATION_PROGRESS_20261021.md
[proposals]: ../10_rh_implies_simple_zeros/brainstorm/04_GLOBAL_HEAT_GEOMETRY_PROPOSALS_AND_INITIAL_SCREENS_20261021.md
[results]: ../../../../../../result-summaries/README.md
[routes]: ../README.md

[note01]: notes/01_LOCAL_RESOLUTION_AND_COMPLETE_COST_COMPARISON_20261021.md
[review01]: reviews/01_LOCAL_RESOLUTION_SELF_REVIEW_20261021.md
