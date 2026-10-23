# Paths forward for reciprocal energy bounds

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual recorded **gpt-6.1-sol (Codex), reasoning effort ultra**, verified from the parent research turn metadata. Separate agents of the same model contributed derivations and checks.

**Purpose.** Continue the existing analytic manuscript while allowing useful integral bounds for several programs, rather than treating endpoint simplicity as the only acceptance condition. This note records the route selection; proofs and outcomes are in Notes 06–08. No mathematical priority claim is made.

Read the [result index](../../../../result-summaries/README.md), especially [local heat geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) and [controls](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), particularly patterns [01](../../../../avoid/01_restating_the_target.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [20](../../../../avoid/20_volume_without_a_gain.md).

## Starting point

The [manuscript](../manuscript/reciprocal_hodge_energy/main.tex) already proves the complete boundary identity, bounded full remainders after quadratic subtraction, a source-controlled ordinary-double chart, and
\[
 E_\tau=\frac{2\pi}{|A|}\log(1/\tau)+O(1),\qquad
 A=H_{zz}(T,x_*)/2.
\]
It also records one actual regular theta fiber with outward-ball enclosures. Repeating the leading logarithm, certifying another regular box without a new objective, or bounding the same generic moments more accurately would not answer the remaining structural question.

The sibling [BW10 program](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/research-overview/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRAM_20261021.md) needs endpoint and trace control. [BW09](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/research-overview/03_ANALYTICAL_PHASE_SURPLUS_PROGRAM_20261020.md) needs a complete signed cap surplus. A positive integral bound is useful in its own domain, but is not relabeled as either missing conclusion.

## Ranked routes and concrete tests

| Priority | Route | Deliverable that would count | Main risk and stop rule |
| --- | --- | --- | --- |
| 1 | Put a derivative numerator into the reciprocal differential | An upper bound for \(2\int \lvert H_z\rvert^2/\lvert H\rvert\), independent of separation and valid at all multiplicities; preferably over an entire horizontal strip | This changes the observable. Stop any transfer to a phase denominator unless an explicit comparison pays its inverse factor. |
| 2 | Determine the full finite part after subtracting the known logarithm | An exact convergent expression, signed correction, and finite coefficient-tail enclosure replacing the unspecified \(O(1)\) | A finite part does not bound the original divergent energy. Retain uncertainty in the logarithmic coefficient. |
| 3 | Soften the singularity through time averaging or fractional powers | Explicit payments for omitted event-time strips and a separation-uniform fractional integral | A time average does not control an individual singular slice or a one-dimensional trace. State the precise kernel class. |
| 4 | Find a canonical-source bound for the original energy or relative period below the generic collision scale | A new arithmetic inequality incompatible with the ordinary-double chart, with complete errors and controls | No candidate distinguishing inequality has been identified. Do not describe generic source positivity or full reflection alone as such an estimate. |
| 5 | Reuse the regular-fiber acquisition | One declared accuracy or repeated-use objective with all shared observations available to direct evaluation | The current finite comparison already passes its original objective. No broad sweep or repeated timing is justified without a new consumer. |

The first three routes can be worked in parallel and have different acceptance conditions. The first is the most promising for an actual upper bound; the second is the most precise continuation of the present Hodge calculation. The fourth retains the direct RH/simplicity objective but currently lacks a source-specific mechanism. The fifth is available if an application needs measured finite acquisition, rather than as a default continuation.

## Control screen before interpreting an estimate

The quadratic heat family \(z^2-2\tau\) must pass all generic local identities and supplies their exact collision benchmark. A neighboring-root quartic tests isolation of the chosen cluster. Euler-factor controls change the canonical arithmetic; weighted-square and finite-prime controls fail the complete normalized reflection conjunction or unchanged full coefficient sequence; reflected and primitive controls lack canonical square coefficients. These preservation lists are separate. A generic bound proved without the distinguishing premise also applies to a control satisfying its stated analytic hypotheses.

For whole-strip estimates an atomic source may fail spatial decay or an integrable source-derivative budget. It still passes the bounded-disk weighted identity. Failure of a global decay hypothesis is not failure of the local formula and does not establish theta collision exclusion.

## Outcomes and the remaining obstacle

[Note 06](06_FINITE_PART_AND_POSITIVE_ENDPOINT_CORRECTION_20261022.md) replaces the bounded remainder by an exact finite part and a nonnegative coefficient correction. [Note 07](07_TIME_AVERAGED_AND_FRACTIONAL_RECIPROCAL_BOUNDS_20261022.md) gives explicit time-strip and fractional payments. [Note 08](08_DERIVATIVE_WEIGHTED_ENERGY_AND_GLOBAL_STRIP_BOUND_20261022.md) gives the derivative-weighted disk and strip bounds. These are analytic gains, shared with an equally informed direct method; no additional actual theta acquisition is used.

The obstacle to the original endpoint target remains specific: none of these estimates bounds the unweighted \(2\int |H|^{-1}\) uniformly down to an ordinary collision, and none supplies BW09's signed cap surplus or BW10's missing trace estimate. A next transfer must name its exact numerator, denominator, domain and comparison constant. Without that comparison, the useful integral bounds stand as independent results and the endpoint gate stays open.
