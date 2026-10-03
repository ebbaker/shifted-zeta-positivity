# Signed full-source certificate at L=6/5

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and reasoning effort not exposed.

This package certifies `Q[F]>=3/2000 ||F||²` for all smooth complex sources
supported in `(-3/5,3/5)` with zero mean and both exponential moments at
plus and minus one half. With the fixed Sonin prime set `{2,3}` it also
certifies `|K[F]|<=3458 ||F||²` and `Q[F]>=3/6916003 B[F]`.
See the [outcome and proof](../../notes/ALL_WINDOW_EXTENSION_OUTCOME_20261003.md),
[preflight](../../notes/ALL_WINDOW_EXTENSION_PREFLIGHT_20261003.md),
[general-L analysis](../../reviews/ALL_WINDOW_SCALING_AUDIT_20261003.md), and
[implementation audit](../../reviews/ALL_WINDOW_EXTENSION_CERTIFICATE_REVIEW_20261003.md).

## Reproduction

The certificate requires Python and python-flint only. Recorded runtime:
Python 3.10.0, python-flint 0.9.0, FLINT 3.6.0. From this directory:

```sh
python3 -B certify_extension.py --bits 192 --output /tmp/extension-192.json
python3 -B certify_extension.py --bits 256 --output /tmp/extension-256.json
```

Defaults are length 6/5, lambda 1/2, cutoff 100, rank 100, nodes 30000,
signed integration, matrix cap 249/500, error cap 1/2000, correction cap 3458.
The first 192-bit run took about 41 seconds. The Python 3.10 runtime in the
originating environment obtained flint from
`PYTHONPATH=/private/tmp/sonin-moment-python-deps`. This is a discovered
local dependency location, not a portable or persistent dependency guarantee.
Do not mix Python 3.10 and Python 3.12 extension modules.

The generator locates the inherited prolate replay record in the sibling
baseline package and verifies its gap and generator binding. It reuses
that earlier outward proof; it does not rebuild the prolate model each time.
The arithmetic Q gap itself does not depend on the prolate input.

## What is proved by the computation

Unitary dilation gives the low-band operator an overall factor L, phase
Lt, and full constraint vectors `1, exp(Ly/2), exp(-Ly/2)`. The code
projects those full analytic functions before taking 100 Legendre coordinates.
It retains the signed weight `lambda-q_L`, tests both 50-by-50 parity blocks
by outward LDL, and adds dimension-independent midpoint and full Legendre
tail remainders. Positive contribution inside the band is retained in the
matrix. Absolute values are used only to bound errors.

The frequency cutoff, constraint norms, LDL pivots, source tail ratio,
total error and correction cap must pass strict outward comparisons.
The combined operator error is below 0.000320680, within the chosen 0.0005
allowance. The signed matrix is bounded by 0.498 I. Their combination with
lambda 0.5 gives the stated conservative gap 0.0015. Every omitted source
mode and the cross terms are included in the error; this is not a test
only of the finite family.

The CLI also contains a capped-weight comparison mode, with its correct
first-variation error. It is not used for the successful certificate.
There is no automatic parameter or window sweep. Guards cap length at 6/5,
cutoff at 200, rank at 192, nodes at 80000, and precision at 384 bits.
Failed inequalities raise an exception instead of saving a success record.

## Records and bindings

- `baseline_replay.json`: one fresh 192-bit baseline replay, with every
  mathematical field and matrix hash matching its immutable saved record.
- `certificate_192.json`, `certificate_256.json`: outward endpoint records
  binding the new generator and regenerated matrix enclosures.
- `replay_check.json`: final bindings, scalar enclosure overlap, and
  strict inequality checks for the new records.
- `pilot_extension.py`, `pilot_10000.json`, `pilot_20000.json`: floating
  diagnostics comparing capped and signed weights at exactly two parameter
  choices for the same window; these are not certificate inputs.
- `check_pilot.py`, `pilot_checks.json`: floating comparison of the analytic
  projection with direct spatial quadrature, and of two actual-Q quadratures.

No matrix, frequency grid, or large derived data file is saved. Matrix
enclosure hashes identify generated data; they are not proof steps and
may differ with precision and library versions. Acceptance depends on
outward inequalities. Small trial-direction coefficients in the pilot
records identify its diagnostic examples only.

The pilot requires NumPy and SciPy (recorded Python 3.12.14, NumPy 2.5.3,
SciPy 1.17.1). Its CLI gives the reproducible finite configurations:

```sh
python3 -B pilot_extension.py --nodes 10000 --actual-q --output /tmp/extension-pilot-10000.json
python3 -B pilot_extension.py --nodes 20000 --output /tmp/extension-pilot-20000.json
```

The first command includes the actual-Q diagnostic used in the saved first
record. Finite-Q quadrature, analytic tail-bound evaluation and all pilot
eigenvalues are floating diagnostics, explicitly separated from the
outward full-space proof. The worst capped directions have positive
actual-Q diagnostics; failure of the capped comparison measures discarded
positive energy.

The result covers one larger anchor and its smaller supports. It does
not prove an all-window estimate, unweighted `B>=K_plus`, place
monotonicity, or RH. The separate scaling audit establishes relative
compactness for every finite prime set but leaves quantitative global
comparison estimates open. The manuscript and old certificate remain unchanged.
