# Arithmetic-storage numerics

## First compressed Sonin moment (29 September 2026)

The [main note](../notes/SONIN_COMPACT_FIRST_MOMENT_20260929.md) and
[review](../reviews/SONIN_FIRST_MOMENT_REVIEW_20260929.md) provide the compact
boundary identity, full error budget, first-prime bounds, and their scope.

- [sonin_second_transport_scalar.py](sonin_second_transport_scalar.py): the extra scalar `B_infinity[D2^2F]`, retaining gamma/contact and epsilon tails.
- [moment_compact_certificate.py](moment_compact_certificate.py): actual projection correction, with [polynomial reduction](moment_kernel_polynomial.py) and [exact truncated splines](arithmetic_truncated_spline.py).
- [arithmetic_prime_diagnostic.py](arithmetic_prime_diagnostic.py): independent rigorous prime correlation and direct arithmetic controls.
- [sonin_first_moment_bounds.py](sonin_first_moment_bounds.py): hash-checked combination into compressed-moment, inverse-trace, and residual bounds, plus the information-limit check.
- [arithmetic_truncated_spline_check.py](arithmetic_truncated_spline_check.py): independent Acb integration controls for the finite spline formulas.
- [moment_compact_diagnostic.py](moment_compact_diagnostic.py): separate floating compact quadrature; explicitly diagnostic, not a certificate.

The principal records have the corresponding script names under `records/`.
Additional small controls are `arithmetic_prime_diagnostic_256bit.json`,
`arithmetic_h2_replay.json`, and `moment_compact_fine_diagnostic.json`.
Use Python with `python-flint==0.9.0`, without `-O`/`-OO`; the floating
control additionally uses NumPy and SciPy. No source-grid or matrix arrays
are saved. Full reproduction commands and precision choices are in the note.
The lightweight combination replay, retaining the saved records, is:

```sh
python -B sonin_first_moment_bounds.py --h2 records/sonin_second_transport_scalar.json --correction records/moment_compact_certificate.json --prime records/arithmetic_prime_diagnostic.json --output /tmp/sonin-first-moment-replay.json
```

This checks the saved numerical implications and code/input bindings; it
does not rerun their full generating calculations. Prepared for Edward Baker
with substantial GPT-6 (Codex) assistance; exact serving variant and configured
reasoning effort not exposed.

## Scalar Sonin traces (29 September 2026)

The [scalar note](../notes/SONIN_SCALAR_TRACE_CALCULATION_20260929.md) proves the complete error budget. The [project summary](../PROJECT_SUMMARY.md) distinguishes these evaluated real-place scalars from the still broadly bounded first-prime trace.

- [gamma_scalar_certificate.py](gamma_scalar_certificate.py): full gamma/contact through an Arb FFT, with both Poisson alias bounds and the complete frequency tail.
- [sonin_scalar_epsilon.py](sonin_scalar_epsilon.py): certified finite exponential kernel, exact integer spline autocorrelation, and source/operator error propagation.
- [sonin_scalar_summary.py](sonin_scalar_summary.py): hash-checked scalar combination and updated fixed-space Hilbert–Schmidt residual/trace bounds.
- [epsilon_selected_point_review.py](epsilon_selected_point_review.py): independent finite-kernel Legendre/Bessel normalization control at three scaling values.

Their same-named JSON records are under `records/`. Run each from this folder with Python and `python-flint==0.9.0`, without `-O`/`-OO`. Existing source/prolate modules and records are inputs. All program defaults follow this directory layout. No generated source grids or Fourier arrays are retained. The four final real-place trace intervals have width below `10^-5`; no complete arithmetic residual sign is asserted.

## Actual Sonin enclosures (later 29 September 2026)

The [main note](../notes/SONIN_ACTUAL_PROJECTION_ENCLOSURES_20260929.md)
contains the derivation and full error budget. These programs require
`python-flint==0.9.0` and standard Python; no floating FFT decides a bound.

- [prolate_certificate.py](prolate_certificate.py): cosine Taylor tail,
  interval LDL gap `57/10^6`, and polynomial resolvent certificate.
- [source_norm_enclosures.py](source_norm_enclosures.py): exact A17 source
  normalization and derivative norms, rigorous interior quadrature and endpoint tails.
- [sonin_trial_enclosure.py](sonin_trial_enclosure.py): actual-Sonin A/H/J/K
  enclosures from compact spline proxies plus complete projection-tail bounds.
- [sonin_omitted_direction_check.py](sonin_omitted_direction_check.py): checks
  the strictly positive omitted-trace lower bounds for the nested trial spaces.

The five small records are in `records/`: `prolate_certificate_rank32.json`,
`source_norm_enclosures.json`, `sonin_trial_enclosure.json`,
`sonin_omitted_direction.json`, and `sonin_omitted_direction_check.json`.
Hashes bind generators and inputs; replay the arithmetic to verify the bounds.
No grid arrays, convolution arrays, or large matrix archives are retained.

To preserve these saved records, copy the four programs and the `records/`
subdirectory into a temporary working directory, then run there in this order:

```sh
python3 -B source_norm_enclosures.py
python3 -B prolate_certificate.py --rank 32
python3 -B sonin_trial_enclosure.py --grid 16384
python3 -B sonin_trial_enclosure.py --grid 16384 --seed-degrees 20 24 21 --output records/sonin_omitted_direction.json
python3 -B sonin_omitted_direction_check.py
```

Use ordinary Python, without `-O`/`-OO` (the source script uses assertion
checks). Separate 192/256-bit prolate builds pass the stated caps. The trial
records use 320-bit arithmetic and retain conservative interpolation errors.
The rank-two test fails the small trace-error target; no complete arithmetic
residual or Weil sign is certified. Prepared for Edward Baker with GPT-6
(Codex) assistance; exact serving variant and reasoning effort not exposed.

## Sonin scalar return bounds (29 September 2026)

[sonin_return_tail_bounds.py](sonin_return_tail_bounds.py) uses exact rational
arithmetic and an integer-square-root bracket to certify scalar tail majorants
for the Neumann and Chebyshev inverse expansions. The [record](records/sonin-return-tail-bounds-20260929.json)
is small and includes the program hash. This is not a Sonin trace evaluation,
projection approximation, source-energy calculation, or Weil certificate.
See the [analysis](../notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md).

From this directory, preserving the saved record:

```sh
python3 -B sonin_return_tail_bounds.py > /tmp/sonin-return-tail-replay.json
```

Standard library only; do not run with `-O`, which disables certificate
assertions. Prepared for Edward Baker with GPT-6 (Codex) assistance;
exact serving variant and reasoning effort not exposed.

## Second session (24 September 2026): closure of the first-prime join, prime-weight rigidity

Read the [research note](../notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md)
and the [review](../reviews/review_claude_first_prime_session_20260924.md). The three
certificate programs import the **unchanged** weil-depth Arb builder
(`papers/shifted-zeta/weil-depth/numerics/certify_arb.py`) and require python-flint, as
weil-depth does. The records were produced with Python 3.11.15, python-flint 0.9.0 and
FLINT 3.6.0. Only Arb balls and exact rationals decide signs; NumPy supplies candidate
vectors and diagnostics.

- `certify_first_prime_join_from_central_floor.py`. Rebuilds weil-depth's N = 128 model at horizon 3/4 and replays its Schur test at the floor 123/250000. It then proves κ₀ ≤ β/(β + m) with β = 2.464 ≥ ‖H_0‖, and the first session's normalized coupling bound (4.4) from its hash-checked 40-digit record, giving 0.99981859 < 1. It also checks weil-depth's continuation inequality: ‖V_{ω,3/4}‖ ≤ e^{−ω/5000} for ω ≤ 1/50.
- `certify_prime_weight_window.py`. For log 2 < R ≤ log 3, builds the head with and without the prime. For trial prime-2 weights outside the admissible interval it certifies a negative ball Rayleigh quotient (plus profile remainder). It replays the Schur test at s = 1 for an elementary inner bound. `--auto` picks trials 2% beyond the floating head edges and a floor of 0.98 × the head minimum.
- `certify_archimedean_threshold.py`. Brackets the length R_A where the prime-free form loses positivity. It runs the full Schur test at the lower length and a certified negative direction at the upper one.
- `crosscheck_first_prime_galerkin.py`. An independently written floating Legendre/Galerkin model of the central form, which is **not a certificate**. It reproduces the first session's numbers, the joined-window bottom, the relative couplings, R_A, and the head intervals.

From the repository root (records are preserved; write replays to `/tmp`):

```sh
D=papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics
python3 -B $D/certify_first_prime_join_from_central_floor.py --output /tmp/first-prime-join-closure-20260924.json
python3 -B $D/certify_archimedean_threshold.py --output /tmp/archimedean-threshold-20260924.json
for H in 3/4 4/5 17/20 9/10 19/20 1 21/20; do
  python3 -B $D/certify_prime_weight_window.py --horizon $H --auto --output /tmp/prime-weight-window-$(echo $H | tr / o)-20260924.json
done
python3 -B $D/certify_prime_weight_window.py --log-horizon 3 --M 220 --bits 1792 --auto --output /tmp/prime-weight-window-log3-20260924.json
python3 -B $D/crosscheck_first_prime_galerkin.py --output /tmp/first-prime-galerkin-crosscheck-20260924.json
# independent weil-depth implementation at the same horizon and floor:
(cd papers/shifted-zeta/weil-depth/numerics && python3 independent_arb.py --horizon 0.75 --floor 4.92e-4 --output /tmp/independent_h3o4)
```

Each Arb build takes 20–90 s. No ball archive is saved; the records carry weil-depth's
`matrices_content_sha256` for each build (see [LARGE_FILES.md](../../../../../../LARGE_FILES.md)).
Records in `records/`:

- `first-prime-join-closure-20260924.json`
- `prime-weight-window-{3o4,4o5,17o20,9o10,19o20,1,21o20,log3}-20260924.json`
- `archimedean-threshold-20260924.json`
- `first-prime-galerkin-crosscheck-20260924.json`

The first session's four records were replayed unchanged in the cloud container. The 40-
and 60-digit `checks` sections are identical, the diagnostics agree within 1.5·10⁻¹⁴, and
the checker passes. Details are in the review, §2.

Prepared for Edward Baker, 24 September 2026, by Claude (Anthropic): session configured as
`claude-fable-5-1`, runtime-reported serving model Claude Opus 5.5 (`claude-opus-5-5`); the
serving model may differ. Reasoning effort not exposed.

## First session (24 September 2026)

The first session studies L = 11/20, h = 1/5 and ω = 1/1000. Read the
[analysis](../notes/FIRST_PRIME_CONTINUATION_ANALYSIS_20260924.md) for domains, tail bounds,
proof scope, and the all-input mixed-coupling gap it left open. That gap is closed at the
level needed for (4.4) by the second session's `certify_first_prime_join_from_central_floor.py`.

- `certify_first_prime_inputs.py` uses standard-library outward rational
  arithmetic. It certifies two all-input local metric floors and diagonal
  defect floors, two specified witness comparisons, and perturbation bounds.
  It does **not** certify the complete first-prime relative norm.
- `diagnose_first_prime_coupling.py` requires NumPy and uses independent
  physical-delay quadrature. Its finite-input norms are diagnostics, not
  all-input upper bounds.
- `check_first_prime_records.py` checks source bindings, nested precision
  records, and a conditional implication whose hypothesis remains unproved.

From the repository root, preserving committed records:

```sh
python3 -B papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/certify_first_prime_inputs.py --output /tmp/first-prime-inputs-40digits-20260924.json
python3 -B papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/certify_first_prime_inputs.py --digits 60 --output /tmp/first-prime-inputs-60digits-20260924.json
python3 -B papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/diagnose_first_prime_coupling.py --certificate /tmp/first-prime-inputs-40digits-20260924.json --output /tmp/first-prime-coupling-diagnostics-20260924.json
python3 -B papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/check_first_prime_records.py --records /tmp --output /tmp/first-prime-record-checks-20260924.json
```

The interval utility is imported from the existing critical-path anchor; the
floating local-form quadrature is imported from its append diagnostic. Both
dependencies are recorded by source hash. Specify `--repository` when running
copies outside the repository layout. Python must not be run with `-O`.

All generated matrices remain in memory; only small scalar records are saved.
Follow [LARGE_FILES.md](../../../../../../LARGE_FILES.md) for future derived data.
Current evidence: two passing precision runs, 15 nested interval pairs, eight
floating controls, and an exact conditional comparison. Specialist review is
outstanding.

Prepared for Edward Baker, 24 September 2026, with substantial LLM assistance.
Model: GPT-6 (Codex; developer-provided identity). Reasoning effort: not exposed;
not inferred.
