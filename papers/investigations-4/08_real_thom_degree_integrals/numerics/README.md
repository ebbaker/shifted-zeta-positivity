# Numerical records

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual coordinating model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**, verified from the current turn metadata.

[check_real_thom_integral_budget.py](check_real_thom_integral_budget.py) and [REAL_THOM_INTEGRAL_BUDGET_20261022.json](REAL_THOM_INTEGRAL_BUDGET_20261022.json) implement the continuation: complete upper<0.699 with nine retained origin-containing first-jet rectangles. From the repository root, in a Python environment with python-flint>=0.9.0:

```sh
python3 papers/investigations-4/08_real_thom_degree_integrals/numerics/check_real_thom_integral_budget.py \
  --upstream-checker papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_boundary_winding.py \
  --output papers/investigations-4/08_real_thom_degree_integrals/numerics/REAL_THOM_INTEGRAL_BUDGET_20261022.json
```

The fixed 160-bit supplier extends to 78 midpoint jets and moment79, with complete tails. The wider r=1e-7,b=1.5e-7 comparison pays548 boundary-only first-jet ranges and253 four-jet bulk ranges. Direct costs 255 two-jet ranges and needs only 76 midpoint integrals. The raw integral enclosure is obtained before integer-count inference, and direct is run only afterward. Retained-support cells are integrated with a positive upper allowance; actual nonempty theta support and signed-cancellation gains are not asserted. The tiny-radius failure and quadratic/inflated-error refusal controls are retained.

Nonfinite ranges or invalid provenance cannot produce a successful certificate. Floating priorities only select subdivisions; all proof comparisons use outward interval endpoints. [Note 04](../notes/04_INTEGRAL_BOUNDS_WITHOUT_INTERIOR_NONVANISHING_20261022.md) and [Review 02](../reviews/02_ACTIVE_BULK_COMPARISON_INTERNAL_REVIEW_20261022.md) explain the result, independent process replay and cost loss. The source callback/order assumptions and complete tails are inherited transparently. Timings are observations; replay comparisons remove timing fields recursively.

The earlier support-only record is preserved:

[check_real_thom_support_pilot.py](check_real_thom_support_pilot.py) reproduces the fixed first comparison; [REAL_THOM_SUPPORT_PILOT_20261022.json](REAL_THOM_SUPPORT_PILOT_20261022.json) is its small record. Requires Python with python-flint>=0.9.0; the recorded run used 0.9.0, 160-bit Arb. From the repository root:

```sh
python3 papers/investigations-4/08_real_thom_degree_integrals/numerics/check_real_thom_support_pilot.py \
  --upstream-checker papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_boundary_winding.py \
  --output papers/investigations-4/08_real_thom_degree_integrals/numerics/REAL_THOM_SUPPORT_PILOT_20261022.json
```

The first-jet supplier is copied transparently with provenance from the unchanged earlier checker; the documented optional argument verifies its hash. All omitted theta modes and the infinite source ray are enclosed. Precision, box and support/collar radii are fixed; no external archive is required. The compact output is exactly zero by complete whole-strip support rejection; no active-support quadrature or higher-jet acquisition is claimed.

Consumer costs are 698 winding,255 direct and 255 support calls after the common 76 midpoint integrals. Support cells pay their own boundary collar once. A separately acquired boundary floor would make support cost 719. Diagnostic control calls are separate. The [analysis](../notes/02_SUPPORT_REJECTION_AND_CONTROL_ANALYSIS_20261022.md) and [internal review](../reviews/01_OPENING_SUPPORT_COMPARISON_INTERNAL_REVIEW_20261022.md) explain scope, replay and refusal checks.

An invalid upstream hash exits nonzero. Unresolved/support-hit data are not certified as empty support; boundary events are refused. A refinement-limit exception is a failed/inconclusive run and produces no successful receipt. Timings are implementation observations; compare mathematical content after omitting timing fields. Hashes identify source/records and never replace the interval arithmetic. Follow [LARGE_FILES.md](../../../../LARGE_FILES.md); these sources and records are small.
