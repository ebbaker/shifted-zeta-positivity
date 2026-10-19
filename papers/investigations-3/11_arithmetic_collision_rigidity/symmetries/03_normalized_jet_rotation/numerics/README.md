# Reproduce the S03 signed transport comparison

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. **gpt-6.1-sol, actual effort ultra**. Parallel same-model
analysis and internal review; no specialist review. Requires Python and
python-flint 0.9.0.

The [derivation](../notes/01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md)
proves the endpoint primitive, joint disk residual bound, and scoped scalar
comparison. The checker imports the S02 complete analytic residual after
checking its script and source hashes. Both precision runs use the same
retained S02 192-bit input contract, so the second run replays S03 interval
arithmetic rather than independently deriving S02's approximation theorem.

Run from the repository root; output is external until reviewed:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_normalized_rotation.py --repo . --output /tmp/S03_192.json --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_normalized_rotation.py --repo . --output /tmp/S03_256.json --bits 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/s03-controls --output /tmp/S03_CONTROLS.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The fixed 32-by-128 closed rational cover encloses the whole real box
`[1/100,1/5] x [999,1001]`, with anchor 999, analytic cutoff 8 and disk
radius 1/2. It retains all modes and the complete signed correction;
the leading constant in the rotating jet cancels exactly before endpoint
subtraction. Both direct whole-cell and signed spatial midpoint enclosures
are recorded. Whole-cell derivative bounds justify propagation from each
midpoint without changing the cover. Rounding, phase uncertainty and the
return to physical energy are included. No source quadrature or additional
truncation is introduced by this checker.

Direct normalized radius is greater than 0.909445 with separate Cauchy
errors, and greater than 0.967290 with the joint disk error. Standard
Cauchy defect and independent endpoint Cauchy transport payments fail a
certified point witness. Joint disk transport has positive slack at that
point and an inconclusive lower bound on the fixed whole-box cover.
These are deliberately different status statements. No new region or
performance gain is claimed.

Elementary constant, polynomial-event and oscillator-residual checks test
the transport mechanism. The separate source-specific replay rejects the
five prior event boxes and the Euler negative-Laguerre witness using their
own errors. Neither check substitutes for a theta arithmetic estimate.

- [192-bit run](S03_ROTATION_192_20261018.json)
- [256-bit replay](S03_ROTATION_256_20261018.json)
- [Fresh source-specific controls](S03_CONTROLS_20261018.json)
- [Internal review](../reviews/01_SIGNED_TRANSPORT_INTERNAL_REVIEW_20261018.md)
- [Source and output identities](../reviews/S03_OPENING_FILE_IDENTITIES_20261018.json)

## Correlated arithmetic residual continuation

18 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**; parallel same-model internal review.

[Note 02](../notes/02_CORRELATED_ARITHMETIC_RESIDUAL_AND_PAID_TRANSPORT_20261018.md)
continues the opening comparison with a complete physical residual Taylor
model. Its signed residual increment is below 0.000266448, versus 0.002011747
for independent endpoints computed from the same source data. The paid
transport radius now exceeds 1.124460; the corresponding independent
calculation exceeds 1.122848, and direct exclusion remains stronger at
1.336516. Thus the earlier finite transport uncertainty is resolved using
additional complete-source information, with a separate matched gain from
correlation. No new region or performance improvement is claimed.

Regenerate the source input rather than bypassing a stale source pin:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/high_height_consumer.py --repo . --output-dir /tmp/s03-correlated-reference --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_correlated_residual.py --repo . --setup /tmp/s03-correlated-reference/SETUP.json --output /tmp/S03_CORRELATED_192.json --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_correlated_residual.py --repo . --setup /tmp/s03-correlated-reference/SETUP.json --output /tmp/S03_CORRELATED_256.json --bits 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/s03-correlated-controls --output /tmp/S03_CORRELATED_CONTROLS.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The retained source cache was rebuilt at 192 bits in about 9.10 seconds;
the new comparisons took about 1.3 seconds each. These are descriptive
execution costs, not a matched speed benchmark. Both comparisons consume
the same new source setup, whose exact hash and current analytic pins are
recorded. The regenerable setup and earlier consumer cells stay external;
the small bound records and source are retained here. The checker refuses
a missing, stale, or incompatible source input.

The new model has physical degrees 26 in x and 12 in t; it uses source
midpoint orders through 50 and a majorant through 52. Subtract the complete
arithmetic expression before taking coefficient ranges, then differentiate
that same residual polynomial. A separate 256-cell complex cover bounds
the approximation's Taylor tail on the radius-8/radius-2 polydisk. The
real cover stays fixed at 32-by-128 closed cells. Signed prefix ranges
include every partial last cell; no new quadrature error is introduced.
All source and approximation tails, coefficient radii, normalization and
phase errors remain paid.

The records also supply a nominal oscillator calibration from the
residual anchor, with complete normalized first-jet error below 0.000266449.
The value and physical x-derivative anchor polynomials are each exported
as 13 exact dyadic coefficients in ascending powers of `t-21/200`.
Their definition and conversion to the normalized anchor are recorded
under `calibrated_oscillator.nominal_physical_anchor_time_coefficients`.
This is a finite approximation using the same source input. The unchanged
source-specific controls and new exact prefix-integrator controls have
different roles; theta tail constants are never assigned to a control.

- [Correlated 192-bit certificate](S03_CORRELATED_RESIDUAL_192_20261018.json)
- [Correlated 256-bit replay](S03_CORRELATED_RESIDUAL_256_20261018.json)
- [Fresh source-specific controls](S03_CORRELATED_CONTROLS_20261018.json)
- [Internal review](../reviews/02_CORRELATED_RESIDUAL_INTERNAL_REVIEW_20261018.md)
- [Continuation file identities](../reviews/S03_CORRELATED_FILE_IDENTITIES_20261018.json)

The opening file-identity record retains its historical README hash; this
continuation intentionally appends the present reproduction instructions.
Its mathematical and numerical source pins are preserved.
