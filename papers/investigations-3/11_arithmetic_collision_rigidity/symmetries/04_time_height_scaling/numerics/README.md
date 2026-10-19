# Reproduce the S04 full-cutoff scaling comparison

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, **gpt-6.1-sol, actual reasoning effort ultra**. Same-model
analysis and internal review; no specialist review. Requires Python with
python-flint 0.9.0.

The [note](../notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md)
proves the explicit replacement error for the full signed scalar and the
derivative of that same scalar. The checker verifies the inherited S02
script and analytic source hashes before importing the common formulas;
it evaluates the current general fixed-cutoff disk error afresh. Missing
or stale imported sources fail closed. It does not import S02's bounded
height-1000 error as if it applied at these new heights.

Run from the repository root, with fresh external output paths:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/numerics/check_time_height_scaling.py --repo . --output /tmp/S04_192.json --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/numerics/check_time_height_scaling.py --repo . --output /tmp/S04_256.json --bits 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/s04-controls --output /tmp/S04_CONTROLS.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The first two point jets have exactly kappa=1 and times 1/20 and 1/21;
cutoffs are 22026 and 36315. A third point has kappa=21/20,time=1/20,
sharing the second point's height. The fourth uses a single fixed cutoff
22026 on a radius-1/L disk centered at x=4*pi*(22027^2-t/16),t=1/20.
Its two natural cutoffs are 22026 and 22027. This exact symbolic center
defines its natural center cutoff; outward numerical floor evaluation
alone would be ambiguous at the crossing. An independent short series
checks the added model mode's value and frozen-time spatial derivative.

All finite sums retain the low range 1..16, an intermediate range, and the
complete terminal range of length floor(M^(3/4)); signed contributions are
stored separately and recombined. A stable per-mode difference calculation
checks the model replacement against independent complete finite sums.
The physical return uses (H,Hx)/A=(Q,Qx+aQ), including the amplitude
derivative. Point jets have paid complete AB/C and cutoff errors, phase
uncertainty, rounding and derivatives. No new source quadrature is needed;
the analytic Riemann–Siegel contract is the imported source representation.
The finite-expression checks are not an independent verification of that
theorem, and no real time-height cell cover is claimed.

Both precision runs pass the explicit coordinate and Euclidean model
bounds; the largest observed vector difference is below 4.75e-11.
The added model payment is below (exp(-10)/5) times the inherited uniform
RS upper bound, but the total error has not been reduced: this replacement
adds a small payment. Execution was approximately 2.8 and 3.0 seconds,
including import/setup and all four points, on this host. Those are
descriptive costs, not a matched speed benchmark.

The fresh controls reject five previously certified event boxes and the
separate Euler negative-Laguerre witness using their own sources/errors.
They screen the existing acceptance interface; theta constants are never
transferred to those sources. Regenerable receipts remain outside the
repository under LARGE_FILES.md.

- [192-bit record](S04_SCALING_192_20261018.json)
- [256-bit replay](S04_SCALING_256_20261018.json)
- [Fresh controls](S04_CONTROLS_20261018.json)
- [Internal assessment](../reviews/01_FULL_CUTOFF_SCALING_INTERNAL_REVIEW_20261018.md)
- [Source and output identities](../reviews/S04_OPENING_FILE_IDENTITIES_20261018.json)


## Reproduce S04-T2's signed Gaussian estimate

19 October 2026. For Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. [Note 02](../notes/02_GAUSSIAN_SIGNED_CORE_AND_COMPLETE_AVERAGED_VALUE_20261019.md)
contains the uniform analytic argument. The new checker verifies outward
scalar constants after monotone endpoint reductions and evaluates the
full finite frozen Gaussian transform at three prescribed points. Those
phase-retaining diagnostics are not physical-source quadrature or a height
cover. Source identities are checked before any calculation.

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/numerics/check_gaussian_signed_core.py --repo . --output /tmp/S04_GAUSSIAN_192.json --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/numerics/check_gaussian_signed_core.py --repo . --output /tmp/S04_GAUSSIAN_256.json --bits 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/s04-t2-controls --output /tmp/S04_T2_CONTROLS.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The bounds are intermediate radius <1.382e-6 (reported1.5e-6), complete
physical radius <0.105110347 (reported0.11), weighted Q/2 energy >0.198.
The physical window is finite; only the frozen polynomial is extended to
the full Gaussian line, with its tail paid. A single possible cutoff jump
and translated-kappa endpoint excursions are handled directly from the
real-axis source contract. No second derivative or new acceptance consumer
is used. Averaged energy does not imply noncollision at the center.

- [192-bit ledger](S04_GAUSSIAN_CORE_192_20261019.json)
- [256-bit ledger](S04_GAUSSIAN_CORE_256_20261019.json)
- [Separate fresh 192-bit replay](S04_GAUSSIAN_REVIEW_REPLAY_192_20261019.json)
- [Input guards](S04_GAUSSIAN_REVIEW_INPUT_GUARDS_20261019.json)
- [Inherited acceptance controls](S04_T2_CONTROLS_20261019.json)
- [Internal review](../reviews/02_GAUSSIAN_SIGNED_CORE_INTERNAL_REVIEW_20261019.md)

Missing/stale analytic source and inadequate precision fail closed. The
review includes fresh replay and input-guard results. The controls reject
five event boxes and the Euler witness in the unchanged consumer using
own-source errors; they do not turn the average into a collision test.


## Reproduce S04-T3's uniform local transfer and payment obstruction

19 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. [Note 03](../notes/03_UNIFORM_LOCAL_RESIDUAL_TRANSFER_AND_CUTOFF_PAYMENT_OBSTRUCTION_20261019.md)
proves the parameter reductions. With Python and python-flint0.9.0:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/numerics/check_uniform_residual_transfer.py --repo . --output /tmp/S04_TRANSFER_192.json --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/numerics/check_uniform_residual_transfer.py --repo . --output /tmp/S04_TRANSFER_256.json --bits 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

These runs use complete inherited theorem-source pins, with no imported
point-jet output or new physical quadrature. The local increment coefficient
is140.035/3 and its opening allowance<0.090111. Independent transition
disks across the sector cost>.99exp(1/(4t)). Four scalar displays illustrate
that analytic formula; no height sampling or collision-free coverage.
Own-envelope event/oscillator/Schur fixtures, signed transition cancellation,
five invalid contracts, source mutations and overlapping-ball maximum pass.

The historical opening record has a stale research-guide pin; its math
pins match. It remains intact and is not a successful fresh replay here.
The new source contract pins the actual theorem and derivation notes.

- [192-bit ledger](S04_UNIFORM_TRANSFER_192_20261019.json)
- [256-bit ledger](S04_UNIFORM_TRANSFER_256_20261019.json)
- [Separate fresh 192-bit replay](S04_UNIFORM_REVIEW_REPLAY_192_20261019.json)
- [Fresh inherited acceptance controls](S04_T3_CONTROLS_20261019.json)
- [Internal review](../reviews/03_UNIFORM_RESIDUAL_TRANSFER_INTERNAL_REVIEW_20261019.md)

The existing replay_nonstationary_controls.py command above reproduces
these controls with fresh output/receipt paths. Its record retains producer
date18 October; the S04-T3 execution date is19 October. Five event boxes
and Euler witness reject with own-source errors. Regenerable control
receipts stay outside the repository; all saved records are below1MiB.
