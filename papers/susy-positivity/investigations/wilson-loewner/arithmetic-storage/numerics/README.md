# Arithmetic-storage numerics

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
