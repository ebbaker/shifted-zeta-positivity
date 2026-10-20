# Initial research questions for boundary winding

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model: **gpt-6-astra (Codex)**;
actual reasoning effort: **xhigh**, verified from the recorded turn metadata.

## Research status and standards

This is an initial exploration note, not a completed research program,
progress tracker, new theorem, or numerical acceptance record. The
[living brainstorm][brainstorm] supplies the common RH context. Read the
[result summaries][results] and [patterns to avoid][avoid], especially
[target classification][classification], [collision controls][controls],
[control premises][control-rule], [scoped exclusions][scope], and
[signed recombination][pairing]. Existing results keep their source status;
the required new estimates below are proposed work.

Before quantitative work, identify the exact source versions, domain,
normalization, derivative orders, cutoff conventions, and complete error
norm. Any control run must use the control's own source and errors on a
domain containing its event or relevant witness. Analytic existence results
must not be assigned invented numerical event locations. The analytic
screens below select premises; they are not new numerical validations.

## Hypothetical event and exact contradiction

Let \(J=(H,H_x)\) be the physical first jet, orient spacetime by
\(dt\wedge dx\), and let \(D\) be a bounded Jordan domain whose closure
lies in the analytic domain. Assume \(J\ne0\) on \(\partial D\).
The existing [spacetime index theorem][winding] gives

\[
\operatorname{wind}_{\partial D}(H+iH_x)
=-\sum_{(T,x)\in D:\,H=H_x=0}\left\lfloor m(T,x)/2\right\rfloor.
\]

Every finite-multiplicity collision contributes with the same negative
sign. An interior event therefore forces winding at most \(-1\).
The desired contradiction is an independent arithmetic determination that
the boundary winding is zero. A validated lower bound strictly greater
than \(-1\) is enough once the integer and sign law applies.

This avoids requiring a useful lower bound for the jet throughout the
interior. It requires nonvanishing and controlled winding along the whole
boundary. The index identity is an existing reduction, not a new arithmetic
estimate. It also does not say that an arbitrary planar map of degree zero
has no zeros; the heat-specific sign of every local index is essential.

## Existing approximation and comparison interfaces

If a boundary approximant satisfies
\(\|J-\widetilde J\|<\|\widetilde J\|\) everywhere on \(\partial D\),
the straight-line homotopy is nonzero there and preserves the winding.
Source errors, interpolation, segment variation, corners, and cutoff
crossings must all be enclosed. Sampling points alone is insufficient.

When using normalized coordinates, prove that the transformation preserves
the relevant boundary degree and pay its uncertainty. Do not silently
exchange the physical jet with a phase-scaled or rotating jet whose
orientation or winding contribution has not been checked. Moving-wall
root-count formulations must retain the stated wall-flux and tangency
conditions.

The [GEO-T1 comparison][wind-comparison] certified winding zero on an
already covered box but did not beat optimized direct certification on
the matched cost criterion. Its result closes that setup, not all boundary
methods. [Summary 13][laws] records the exact scope. A new attempt needs
a different domain, genuinely new boundary information, or an acquisition
advantage linked to a specified result.

## Questions for the first deeper discussion

1. Can a useful boundary be chosen where complete arithmetic is simpler
   than in the interior? Identify the information needed on its time
   faces and spatial walls before selecting a large region.
2. Can paired boundary contributions be bounded together, preserving
   their signed cancellation and integer information? A bound for each
   face separately may lose the needed margin.
3. Can a boundary region enclose the uncertain small-jet set of the
   retained-sum route while staying inside a complete error contract?
   Boundary regularity must be proved, not inferred from a plot.
4. Would a finite regional exclusion or a boundary estimate with a
   quantified gain be useful even without an exhaustive RH application?

The initial research question is an arithmetic boundary estimate, not
another derivation of the index formula. Topological language is useful
only when it identifies information that can actually be bounded.

## Control screen

For a nondegenerate double heat event,
\(\det D_{(t,x)}(H,H_x)=-H_{xx}^2<0\). A sufficiently small boundary
around it has winding \(-1\). The higher-multiplicity law gives the
corresponding negative integer for every finite-order control event.
Thus a purported generic zero-winding argument must fail on such a region.
These facts are analytic screens; no new boundary certificate is run here.

Polynomial heat controls share the PDE and index law but lack complete
theta arithmetic. Weighted-square and finite-prime controls fail full
reflection or unchanged coefficients; reflected smooth controls lack the
theta square expansion; Euler modifications alter their arithmetic data.
A proposed boundary estimate must use a premise that the applicable
control fails and use source-specific errors when tested numerically.

## Useful first results and remaining scope

A useful result could be new regional noncollision, a boundary estimate
that is unavailable from the current pointwise balls, or a demonstrated
cost reduction enabling a named larger region. Give direct certification
the same reusable data and optimizations in any comparison. A scoped loss
can be informative if it identifies the precise norm or acquisition cost.

An exhaustive family of zero-winding regions covering all possible
positive-time events is RH-equivalent. A single boundary certificate is
not. Higher multiplicities are included by the index law, but boundary
nonvanishing, possible event locations, and the limit toward time zero
remain separate coverage obligations. No new global exhaustion is asserted
by this setup.

[brainstorm]: ../../../brainstorm/notes/04_SMALL_JET_OBSTRUCTION_AND_RH_CONTRADICTION_TARGETS_ASTRA_20261019.md
[winding]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[wind-comparison]: ../../../11_arithmetic_collision_rigidity/symmetries/notes/06_GEO_T1_WINDING_AND_DIRECT_COMPARISON_20261019.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[laws]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[control-rule]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[pairing]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
