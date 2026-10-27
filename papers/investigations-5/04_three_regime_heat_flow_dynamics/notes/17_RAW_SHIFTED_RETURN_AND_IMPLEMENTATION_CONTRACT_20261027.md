# Raw-versus-shifted return and the next implementation contract

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.
Chat0005, thread `01a17e41-99d3-79c1-b932-2bae84ad0d47`.

The analytical comparison requested in [Note14][n14] is now completed for
the declared finite-mode source Taylor family. [Note15][n15] pays both
arms, both physical first-jet components, both cutoffs, analytic quadrature
and finite-coefficient allowances on the same symbolic box. [Note16][n16]
compares those complete sufficient schedules. Read [Review07][review]
and [the CE register][progress] for exact statuses and limitations.

The findings are:

- Full reflection must precede truncation. Fixed raw theta-mode cutoffs
  leave a genuine inverse-square error; a fixed frequency wall leaves
  a first-jet error of order 1/x. The shifted completed truncations keep
  exponential errors. These are fixed-cutoff comparisons, not joint
  complexity lower bounds.
- At fixed shifts, the smaller Taylor order is offset at leading order
  by the smaller strip-safe source radius. Both optimized derivative
  ledgers have leading term (e/8)X log X. The inherited mode-count
  constant improvement survives, but is not a runtime measurement.
- On each fixed positive slab b>0, selecting strip gap
  g=zeta log^2 X/X with zeta<b/16 gives a stronger sufficient schedule:
  K=O(sqrt X/log X), Jq=O(X log X), and KJq=O(X^(3/2)). The matched raw
  ledger is O(X^(3/2)log X). Positive-time carrier growth pays the mode
  tail. The complete frequency and quadrature bounds retain this gain.

The last result is a logarithmic improvement in a declared source-data
ledger. It is not a certified evaluator, an operation count, new coverage,
or a lower first-jet margin. Its onset and constants depend on b; it does
not justify a uniform limit at zero. The source approximation remains
compatible with a hypothetical collision and the energy coefficient is
unchanged.

## Next bounded calculation

Implement a single **fixed-parameter** paired source reference with the
source-coefficient and point-evaluation allowances in Note15 (11).
Before choosing a new high box, compare its rigorous coefficient-generation
and summation costs against the existing complete canonical oracle in
[HDC Note13][hdc13] and [Note15][hdc15]. Use their box only as calibration.
Record the same input precision, physical first-jet errors, wall/cell
coverage, coefficient generation cost and final summation cost. The new
KJq ledger does not account for derivative convolution or precision cost;
the implementation must measure and enclose those separately.

An implementation should retain paired phases and shared physical
derivatives. Freeze all shifts and orders on each box. Do not differentiate
the endpoint-dependent selection rule, discard vertical seams from a
pre-truncated source, force evenness on the shifted finite model, or replace
the physical derivative by an unpaid normalized derivative.

Advance to a new covered domain only if this bounded comparison acquires
a complete accuracy/cost advantage or an actual positive first-jet margin.
Use the existing [positive-threshold Section 5A][jet] consumer; no new
criterion is needed. If neither advantage survives coefficient evaluation,
close that implementation branch with its measured complete costs.

The [result index][results], [control register][controls], [avoid index][avoid],
[target classification][a01], [scoped exclusions][a07] and
[matched estimates][a12] remain controlling. No parent task ownership,
new automation, manuscript milestone or Newman bound changes in this return.

[n14]: 14_SECOND_RETURN_AND_NEXT_CANONICAL_CALCULATION_20261027.md
[n15]: 15_MATCHED_RAW_AND_SHIFTED_SOURCE_ERROR_BUDGET_20261027.md
[n16]: 16_STRIP_RADIUS_AND_POSITIVE_SLAB_COMPARISON_20261027.md
[review]: ../reviews/07_RAW_SHIFTED_SOURCE_COMPARISON_REVIEW_20261027.md
[progress]: ../research-progress/02_COLLISION_ENERGY_RESEARCH_PROGRESS_20261027.md
[hdc13]: ../../../investigations-4/12_height_dependent_heat_contours/notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md
[hdc15]: ../../../investigations-4/12_height_dependent_heat_contours/notes/15_COMPLETE_PHYSICAL_CAP_COMPARISON_20261023.md
[jet]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
