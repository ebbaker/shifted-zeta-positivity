# S06 transverse observation checks

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**. Exact algebra and inherited source-specific controls, with
same-model internal review.

The [derivation](../notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md)
proves the scoped analytic statements. The
[checker](check_transverse_observation.py) passed **166 exact assertions**:
finite normalized jets and their zero modes, the general base-p formula
through order six, all Green identity boundary signs on a polynomial
basis, fixed-parity physical reduction, mixed-operator Fourier multipliers,
and the interpolation domain and determinant. These checks do not prove
infinite convergence or a signed theta inequality.

The [small record](TRANSVERSE_OBSERVATION_CHECKS_20261018.json) also records
four fresh inherited geometry replays and the existing rejection interface
on five control events plus the separate Euler negative-Laguerre witness.
The control-interface precision is 192 bits; imported certificates retain
their own recorded precision. No theta error constants are assigned to a
different control. Bulk intermediate receipts are regenerable and remain
outside the repository.

From the repository root, using Python with **python-flint 0.9.0**, run:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/numerics/check_transverse_observation.py \
  --repo . \
  --output /tmp/S06_TRANSVERSE_OBSERVATION_CHECKS.json \
  --replay-dir /tmp/s06-transverse-replay \
  --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The finite algebra uses the Python standard library; the inherited controls
require python-flint. The record pins current note, code, mathematical
sources and inherited checker identities. Run metadata and generated
receipt hashes may change across replays. A hash identifies bytes and does
not establish a mathematical claim.

The scoped-obstruction gate passes. Physical approximation error, cost,
coverage and global nonvanishing are unchanged. See the
[internal review](../reviews/01_TRANSVERSE_OBSERVATION_INTERNAL_REVIEW_20261018.md).

## Signed observation and exact compensation

The [continuation note](../notes/02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md)
establishes a signed raw auxiliary bound and its mismatch with physical
energy. The exact source completion gives a signed current inequality
**from the existing physical margin**, rather than a new sign premise.
Records at [192 bits](S06_SIGNED_TRANSVERSE_192_20261018.json) and
[256 bits](S06_SIGNED_TRANSVERSE_256_20261018.json) preserve both results.
The [checker](check_signed_transverse.py) uses analytic all-half-line
majorants and complete n>=9 source tails for the raw signed estimate.
Its physical comparison and 64-cell margin use fresh complete contour
quadrature; no obsolete setup cache is imported.

With python-flint 0.9.0, run from the repository root:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/numerics/check_signed_transverse.py \
  --repo . --bits 192 \
  --output /tmp/S06_SIGNED_TRANSVERSE_192.json \
  --replay-dir /tmp/s06-signed-192 \
  --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

Repeat with `--bits 256` and distinct output/replay paths. The records keep
the failed order-four signed payment and the single order-six repair.
Constant evaluation uses outward Arb arithmetic, including Gaussian
moments and geometric tails. The inherited physical quadrature separately
pays rounding, quadrature, mode/source tails and whole-cell propagation.
The centered-current control test is exactly a positive factor times the
inherited signed test; raw K positivity alone is not a collision test.

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**, 18 October 2026;
[same-model internal review](../reviews/02_SIGNED_TRANSVERSE_ESTIMATE_INTERNAL_REVIEW_20261018.md).
See [file identities](../reviews/S06_SIGNED_FILE_IDENTITIES_20261018.json)
for the saved note, review, code and record hashes. No complete physical
error decrease, cost improvement or new coverage is claimed.


## Geometric symmetry coverage checks

18 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), actual effort ultra**. The
[coverage checker](check_geometric_symmetry_coverage.py) and
[small record](GEOMETRIC_SYMMETRY_COVERAGE_CHECKS_20261018.json) verify 61
exact rational identities: quaternion matrices and pairings, tangent and
curvature signs, failure of pointwise J to preserve closedness, and the
declared J/K first/second source insertions, diagonal Hessian corrections,
and primitive compensation.
The analytic interpretation and scope are in
[Review 03](../reviews/03_GEOMETRIC_SYMMETRY_COVERAGE_POINCARE_AND_HYPERKAHLER_20261018.md).

From the repository root, reproduce with the standard-library interpreter:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/numerics/check_geometric_symmetry_coverage.py --repo . --output /tmp/geometric_symmetry_coverage.json
```

This is finite algebra, not a new interval collision certificate. The
opening checker was additionally rerun through its 163 exact algebra
assertions in memory by a delegated reader. The inherited event controls
and full signed 192/256-bit certificate were inspected, not freshly
rerun in this coverage review. No independent physical sign estimate is claimed.
