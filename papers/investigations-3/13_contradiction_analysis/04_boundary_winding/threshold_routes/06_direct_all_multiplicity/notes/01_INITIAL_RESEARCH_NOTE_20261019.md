# Direct boundary estimates for every multiplicity

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**; actual reasoning effort **xhigh**, verified from recorded turn metadata.

**Status: initial research note prepared; mathematical execution not started.**
The [overall program][program] fixes the unchanged theta flow, the positive
threshold hypothesis, control distinctions and complete error requirements.
The [progress register][progress] owns execution status for this route.
Read the [result summaries][results] and [patterns to avoid][avoid], especially
[local index laws][laws], [target classification][a01], [control premises][a02],
and [scoped conclusions][a07]. The full contradiction remains a research
target; the useful first outputs below are restricted milestones.

## Existing topology and new obligation

At a finite real threshold zero of exact multiplicity m>=2, the existing physical index is \(-\lfloor m/2\rfloor\). An isolating boundary therefore has negative winding for every such m. A zero-winding arithmetic estimate applicable without \(H_{xx}\ne0\) would exclude all of them at once. There is no need to reprove the all-multiplicity index theorem.

The proposed extension is in the arithmetic and domain estimates. A bound dividing by Hxx, using an unproved lower curvature floor, or losing all margin as Hxx tends to zero does not automatically cover degenerate events. Conversely, a boundary proof may need no interior curvature lower bound at all; that possibility should be tested against its actual hypotheses.

## First bounded task

Take a concrete estimate from [BW-01](../../01_local_double_winding/README.md) or [BW-04](../../04_later_negative_winding/README.md) and list each use of double-event structure. For each, decide whether it can be replaced by boundary nonvanishing, a finite-multiplicity analytic bound, or a different source observation. State the dependence on m, the first nonzero derivative, radius, T and event height. A uniform numerical margin is not inherently required for a conditional contradiction, but every individual strict margin must be proved.

The initial useful result may cover m=3 or a fixed range, with all remaining orders explicitly open. Covering finitely many m does not prove an unrestricted statement. A finite-multiplicity theorem for the genuine analytic H also uses the fact that its spatial slice is not identically zero.

## Controls and acceptance

Use the Hermite controls and asymmetric variants at the claimed orders to audit orientation, complete boundary coverage, and false exclusions. The [prior replay][replay] covers degrees 2 through 16 only; its finite checks do not prove the general law or any theta arithmetic estimate. Multiplicities two and three have the same index -1, so induction solely on winding magnitude misses the distinction.

Positive-threshold polynomial controls still defeat heat-only or all-real-only arithmetic claims. The complete theta source must enter an actual bound. Quantitative source errors must be recalculated when the derivative order or domain changes; a second-through-fourth-jet certificate cannot silently pay arbitrarily many derivatives.

## Relationship to the other extensions

This route keeps the original H and extends its boundary estimate directly. [BW-07](../../07_multiplicity_reduction/README.md) instead seeks a justified reduction to a class with double events. [BW-08](../../08_deflated_jet_hierarchy/README.md) supplies a possible hierarchy of extra threshold constraints. A successful double-event estimate may guide these choices, but does not decide them in advance. Record a partial extension or precise nondegeneracy obstruction in its own scope; no generic perturbation argument is an automatic extension for the fixed theta field.

[program]: ../../../research-overview/01_THRESHOLD_BOUNDARY_WINDING_RESEARCH_PROGRAM_20261019.md
[progress]: ../../../research-progress/01_THRESHOLD_BOUNDARY_WINDING_PROGRESS_20261019.md
[results]: ../../../../../../../result-summaries/README.md
[laws]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[predecessor]: ../../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[index]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[walls]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[comparison]: ../../../../../11_arithmetic_collision_rigidity/symmetries/notes/06_GEO_T1_WINDING_AND_DIRECT_COMPARISON_20261019.md
[threshold-sign]: ../../../../02_threshold_jet_sign/notes/01_INITIAL_RESEARCH_NOTE_20261019.md
[replay]: ../../../numerics/THRESHOLD_CONTROL_REPLAY_20261019.json
[polymath]: https://arxiv.org/html/1904.12438v2#S3
