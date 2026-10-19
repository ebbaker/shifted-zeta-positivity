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


## S03-T1 filtered mechanism and scoped split-prefix obstruction

19 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**; same-model internal review.
[Note 03](../notes/03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md) derives the signed source-filtered discrepancy,
its physical tail ledger and exact heat forcing. Its only new numerical
inequality is the exact-point witness `|I_f(21/200,1001)|>1.912087`,
excluding triangle payments that separately bound physical-source and
approximation prefixes. This is neither a residual lower bound nor a new
uniform residual allowance. The retained source integral is not evaluated
by this checker; S03-T2 still owes that independent combined estimate.

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_filtered_residual_mechanism.py --repo . --output /tmp/S03_T1.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/S03_T1-controls --output /tmp/S03_T1-controls.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The first command defaults to 192 and 256 bits. For a separate replay,
add `--bits 192`. The independent power-series identity checks use nine
corner/center combinations; the written derivation proves the identities.
Full profile and normalization omissions are detected. Exact polynomial
and oscillator controls exercise the generic filter; the separate source
replay rejects five event boxes and the Euler witness with their own errors.
Its legacy producer hardcodes 18 October as its source-version date;
this task replayed it on 19 October.

- [192/256-bit mechanism and obstruction record](S03_FILTERED_MECHANISM_20261019.json)
- [Separate 192-bit internal replay](S03_FILTERED_REVIEW_REPLAY_192_20261019.json)
- [Fresh source-specific controls](S03_T1_SOURCE_CONTROLS_20261019.json)
- [Internal review](../reviews/03_FILTERED_RESIDUAL_INTERNAL_REVIEW_20261019.md)
- [File identities](../reviews/S03_FILTERED_FILE_IDENTITIES_20261019.json)

## S03-T2 analytic-only allowance and absolute-kernel variation screen

19 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**; separate same-model internal review.
[Note 04](../notes/04_PHASE_AWARE_ANALYTIC_ALLOWANCE_AND_KERNEL_VARIATION_OBSTRUCTION_20261019.md) proves the endpoint-ellipse/near-anchor bound
|I_r|<0.812260, compared with same-input endpoint allowance <0.827470.
The complete eta is imported with validated S02 pins; no source jets,
old residual polynomial or new source quadrature enter the estimate.
The fixed 32x128 closed phase cover is unchanged. All inherited residual
costs are in eta; do not add the direct finite-source tail ledger twice.

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_phase_residual_allowance.py --repo . --output /tmp/S03_T2_PHASE.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_kernel_variation_obstruction.py --repo . --output /tmp/S03_T2_KERNEL.json --model ACTUAL_MODEL --effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/S03_T2_controls --output /tmp/S03_T2_controls.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The first two default to 192/256 bits; --bits 192 performs a single replay.
The second independently evaluates elementary source formulas. It proves
that the prescribed separate-channel absolute derivative variation budget
assigns one width-1/64 cell >4037.45136. It performs no source quadrature
and proves no actual-residual or quadrature-error lower bound. Signed
integration and correlated parameter models are outside that obstruction.
All records remain small; no new external data archive.

- [Analytic allowance](S03_PHASE_ANALYTIC_ALLOWANCE_20261019.json)
- [Kernel-payment obstruction](S03_KERNEL_VARIATION_OBSTRUCTION_20261019.json)
- [Separate phase replay](S03_PHASE_REVIEW_REPLAY_192_20261019.json)
- [Separate kernel replay](S03_KERNEL_REVIEW_REPLAY_192_20261019.json)
- [Fresh inherited source controls](S03_T2_SOURCE_CONTROLS_20261019.json)
- [Internal review](../reviews/04_PHASE_ALLOWANCE_AND_KERNEL_OBSTRUCTION_INTERNAL_REVIEW_20261019.md)

The new helper's polynomial event uses its own complete disk allowance 5
and rejects strict propagation. Oscillator, zero-error, invalid-input,
long-phase and absolute-cosine mutation controls exercise the actual helper.
The inherited source-control replay tests the unchanged downstream sign
consumer with each control's own errors, not a new theta sign interface.
Its producer retains source-version date 18 October. The constant-residual
>0.3553758 floor applies only to the envelope class and does not preserve
the exact theta source or its prescribed heat forcing.

## S03-T3 calibrated consumer comparison

19 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**; separate same-model internal review.
[Note 05](../notes/05_CALIBRATED_FIRST_JET_AND_MATCHED_DIRECT_COMPARISON_20261019.md) compares complete real first-jet radii on B with the same 32x128
closed cover and historical 192-bit source input. Calibration uses the26 exact
dyadic anchor coefficients, paying the retained anchor uncertainty once.
The strongest same-source direct consumer receives the same cell midpoint
propagation and wins (>1.3898732635 versus calibrated >1.3859351576).
Scalar calibrated transport gives >1.1288659652. This is an old-box
comparison, with no new source/residual theorem, coverage or matched-cost claim.

The [saved anchor export](S03_T3_ANCHOR_EXPORT_20261019.json) supplies
source/code/record pins, exact coefficients, inherited complete error ledger
and per-slab payments. Consume it with an external complete-source setup:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/compare_calibrated_consumers.py --repo . --setup /path/to/SETUP.json --anchors papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/S03_T3_ANCHOR_EXPORT_20261019.json --output /tmp/S03_T3_COMPARE.json --bits 192 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_calibrated_consumer_controls.py --repo . --consumer papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/compare_calibrated_consumers.py --anchors papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/S03_T3_ANCHOR_EXPORT_20261019.json --setup /path/to/SETUP.json --work-dir /tmp/S03_T3_controls --output /tmp/S03_T3_controls.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

If the source setup is absent, regenerate externally at 192 bits:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/high_height_consumer.py --repo . --output-dir /tmp/S03_T3_source --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

Then pass /tmp/S03_T3_source/SETUP.json to the consumer. Its source pins,
fixed parameters and mathematical hash must match the saved export before
any cell is evaluated. Observed setup seconds/callbacks are excluded from
the canonical identity; mathematical midpoint/radius/tail data are retained.
An unmatched regeneration fails closed and needs investigation or a new
proved calibration, not a changed hash to force acceptance.

The initial export can be independently reproduced only with the exact
historical source setup whose stored hash is pinned in Note 02:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/compare_calibrated_consumers.py --repo . --setup /path/to/historical/SETUP.json --export-anchors --output /tmp/S03_T3_anchors.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

Ordinary consumer replay uses the saved export, so it does not require the
historical cache's observational bytes. Both precisions use the same192-bit
source setup and anchors; this is not a second source quadrature. The
combined work/times are descriptive; calibrated setup also owes Note 02's
majorant, mixed coefficients and signed residual prefix computation.

- [192/256 complete ledger](S03_CALIBRATED_CONSUMERS_20261019.json)
- [Separate 192 replay](S03_CALIBRATED_REVIEW_REPLAY_192_20261019.json)
- [Actual-helper, mutation, cache and fresh source controls](S03_T3_CONTROLS_20261019.json)
- [Separate internal review](../reviews/05_CALIBRATED_CONSUMER_COMPARISON_INTERNAL_REVIEW_20261019.md)

Controls use their own source errors. Five event firstjets must reject;
Euler's negative-Laguerre witness rejects the old sign while a nonzero
firstjet may pass. A separately marked constant-ball fixture checks that
complete source errors are not subtracted twice. Seven implementation
mutants and seven changed-input guards are detected. All displayed control
values are required finite; a control-only interval-power diagnostic was
corrected before retaining the record. No large data archive is added.

## G3 arithmetic gamma and edge decomposition

19 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**; separate same-model internal review.
[Note 06](../notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md) proves a uniform finite gamma/heat remainder on B.
The finite-mode filtered error after its prescribed first correction is
<3.874872e-6. The edge hierarchy is explanatory: its Gaussian tails and
RS_K remain unpaid, even though the finite integrals are outward enclosures.
The exact-edge point record instead subtracts exact finite modes from the
historical complete-source enclosure, and is not an independent edge bound.

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_heat_stirling_remainder.py --repo . --output /tmp/G3_HEAT.json --bits 192 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_rs_edge_hierarchy.py --repo . --output /tmp/G3_EDGE.json --bits 192 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/probe_exact_gaussian_modes.py --repo . --setup /path/to/SETUP.json --output /tmp/G3_MODES.json --bits 192 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

Use python-flint 0.9.0. The exact point decomposition's setup is the
historical external complete-source SETUP.json with stored SHA-256
`abd7889c7880e6acd941e95f0a103ab19601e68edec8267a8eb5c377376938d9`.
It is the same source input retained by S03 Note 02 and the T3 anchor export.
A fresh source setup can be regenerated with the command in the preceding
section; producer/domain pins are checked before use. Fresh source balls
need not have identical observational bytes or outward radii. Record their
new setup hash rather than relabeling them as the historical cache.
The heat and RS hierarchy scripts use no source Taylor coefficients.
Both exact-mode precisions use the same 192-bit source input; after each
source evaluation the arithmetic precision is restored before subsequent
mode work. Infinite tails of the exact finite-mode integrals are paid on
physical-x radius-1 discs with Cauchy factors 1,1,2. The theorem's independent
relative-error proof uses radius-5 s discs, hence radius-10 physical-x discs.

- [Exact five-point decomposition 192/256](S03_G3_EXACT_MODES_20261019.json)
- [Uniform finite-mode remainder ledger 192/256](S03_G3_HEAT_STIRLING_REMAINDER_20261019.json)
- [RS finite hierarchy and 126 exact coefficient identities](S03_G3_RS_EDGE_HIERARCHY_20261019.json)
- [Fresh inherited source controls](S03_G3_SOURCE_CONTROLS_20261019.json)
- [Separate exact-mode replay 192](S03_G3_EXACT_MODES_REVIEW_192_20261019.json)
- [Separate finite-mode ledger replay 192/256](S03_G3_HEAT_REVIEW_192_256_20261019.json)
- [Separate finite RS hierarchy replay 192](S03_G3_RS_REVIEW_192_20261019.json)
- [Internal assessment](../reviews/06_ARITHMETIC_GAMMA_AND_EDGE_INTERNAL_REVIEW_20261019.md)

Five source event boxes and the Euler sign witness reject in the unchanged
consumer using their own errors. This continuation introduces no new
acceptance interface. Analytic shape/primitive and finite arithmetic control
premises are screened explicitly in Note 06. No large archive is added.

## G3 complete independent arithmetic edge and increment

19 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. [Note 07](../notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md) supplies the
complete edge payment absent from the preceding diagnostic hierarchy.
The new estimator uses no complete-source SETUP.json, H Taylor coefficients,
source quadrature or inferred point-edge data. It combines the finite
heat–Stirling correction with an RS8 edge model and evaluates the signed
rotating endpoint primitive on a fixed closed 8x32 cover of B.

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/bound_complete_rs_edge.py --repo . --output /tmp/G3_COMPLETE_EDGE.json --bits 192 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/estimate_arithmetic_residual_increment.py --repo . --edge-record /tmp/G3_COMPLETE_EDGE.json --output /tmp/G3_ARITHMETIC_INCREMENT.json --bits 192 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/check_arithmetic_increment_guards.py --repo . --edge-record /tmp/G3_COMPLETE_EDGE.json --output /tmp/G3_EDGE_GUARDS.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

Use python-flint 0.9.0. Nominal 192/256 precisions use explicit512 guardbits
(704/768 working bits) for high-order profile coefficients. First run the
edge producer, which pins the retained model script, then the increment
estimator, which checks producer/model/dependency pins, precision coverage
and radius/error caps. The producer's optional --model-script is only a
staging override; ordinary lookup is the declared repository-relative file.
No machine-specific dependency or archive path is embedded in these scripts.

The complete edge value error is <6e-8 on radius 1 complex physical-x disks;
Cauchy pays x and xx by6e-8 and1.2e-7. The paid central RS, CR, exact-tail
and model-conversion sum is <5.357353e-8. The signed model prefix is
<0.000840994, and both endpoints cost<0.000012291, giving complete
|I_r|<0.000854. This improves independent analytic-only0.812260 by>950-fold,
while source-informed0.000266448 remains stronger. The cover is not tuned
against the source comparator and no consumer rerun or extension is claimed.

- [Complete edge192/256 ledger](S03_G3_COMPLETE_EDGE_BOUND_20261019.json)
- [Complete independent increment192/256 ledger](S03_G3_ARITHMETIC_INCREMENT_20261019.json)
- [Separate edge192 replay](S03_G3_COMPLETE_EDGE_REVIEW_REPLAY_192_20261019.json)
- [Separate increment192 replay](S03_G3_INCREMENT_REVIEW_REPLAY_192_20261019.json)
- [Seven fail-closed input guards](S03_G3_EDGE_GUARDS_20261019.json)
- [Fresh inherited source controls](S03_G3_EDGE_SOURCE_CONTROLS_20261019.json)
- [Separate same-model proof/code review](../reviews/07_COMPLETE_ARITHMETIC_EDGE_AND_INCREMENT_INTERNAL_REVIEW_20261019.md)

The source controls reject five event boxes and Euler's signed witness
using their own errors; no new acceptance interface is introduced. Guard
cases alter producer/model/dependency hashes, precision coverage, empty
runs, value caps and disk radius, and must fail before writing a result.
The old K<=4 finite-integral hierarchy remains a diagnostic; Note 07 does
not retroactively supply an unpaid tail to those older rows. No large
archive is added.
