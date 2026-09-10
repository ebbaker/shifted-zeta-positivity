# Numerical supplement — v0.4

Read `../STATUS.md` and the manuscript for the mathematical scope. Only python-flint (Arb)
and the standard library decide any sign; NumPy supplies diagnostic eigenvalues and mpmath
the candidate ground-state vectors and the review-time checks. Install `requirements.txt`
in an isolated environment. Certificates were produced under Python 3.10–3.12 with
python-flint 0.9.0 and FLINT 3.6.0 and reproduce bit-for-bit across those versions.
Assertions must be enabled (`python -O` is rejected).

## Layout

| Path | Contents |
|---|---|
| `certify_arb.py` | Builder: exact-rational profiles, full-output ball Grams, analytic tail bounds, ball LDL. `--reuse` replays a saved archive. |
| `enclose_certificate.py` | Sector-wise floor bisection (largest three-significant-figure rational passing the ball test), ball Rayleigh upper bounds, exact continuation constants; writes `enclosure.json`; `--summary` writes `output/enclosure_summary.json` and `output/enclosure_table.tex`. |
| `analyze_certificate.py` | Hash-bound replay of a certificate, exact rational continuation check for given shift/decay/generator bound, relative-coupling diagnostic; writes `analysis.json`. |
| `independent_arb.py` | Separately written construction from the printed formulas. |
| `compare_implementations.py` | All-entry overlap check of head and both Grams between the two implementations and replay of the independently saved Schur matrices, for every pair whose independent archive is present. |
| `review_checks.py` | Moment quadratures, Euler-derivative identities, fractional-tail combinations, parity control, LDL sign controls, failure controls; writes `review/review_checks.json`. |
| `make_tables.py` | Generates `../manuscript/tables_main.tex` and `tables_certificate.tex` from the JSON records, with consistency assertions. Every displayed lower value is the lower endpoint of its ball rounded down and every upper value the upper endpoint rounded up (radius included); exact rationals are printed exactly; only diagnostics are rounded to nearest. |
| `review_claude/` | Independent verification scripts from the v0.2 review: Fourier-side evaluation of the form against zeta zeros, Weber–Schafheitlin head check, direct-quadrature Gram check, floor sweeps. See its `README.md`. |
| `output/<horizon>_N128/` | For `log2 … log6`, `length_1p8` (= 9/5) and `log7`: `central_certificate.json` (pivots at the certified floor, archive hash and matrices content hash), `enclosure.json`, `analysis.json`. The ball archive `central_matrices.json.gz` itself is **not versioned** (see below). |
| `output/independent_*/` | Independent-implementation certificates for all seven horizons (their archives are likewise unversioned; those for `1p8` and `log7` are kept in `numerics-archives/`). |
| `output/enclosure_summary.json`, `enclosure_table.tex`, `paper_numbers.json` | Aggregated records used by the manuscript. |
| `review/` | Cross-implementation comparison records and review checks. |

## The ball archives

Every `central_matrices.json.gz` (about 13 MB) is deterministic output of `certify_arb.py` for
the parameters in the certificate, so the archives are kept outside git; the expected layout,
the hashes and how to obtain or regenerate them are documented in the tracked `../ARCHIVES.md`.
Two hashes tie a certificate to its data: `matrix_archive_sha256` (the exact `.gz` file) and
`matrices_content_sha256` (canonical JSON of the four ball matrices and run parameters, independent
of timestamps and runtime metadata). In the tested environments a rebuild reproduced the content
hash exactly — the 9/5 and `log7` archives built under Python 3.12 and 3.10 hash identically to
rebuilds under 3.11, all with python-flint 0.9.0 / FLINT 3.6.0 — so a reader in such an
environment can regenerate an archive and confirm it is the same object without the original
file. This is an identity check for the saved data, not a claim of bit-for-bit portability across
other Arb/FLINT releases; the sign tests themselves never depend on a hash.
To use saved archives, copy them back into `output/` or set `WEIL_ARCHIVES=/path/to/numerics-archives`;
`certify_arb.py --reuse`, `enclose_certificate.py`, `analyze_certificate.py` and
`compare_implementations.py` fall back to that folder when a file is missing from `output/`.

## Replay (fast)

```bash
python certify_arb.py --reuse --bits 1792 --floor 1.37e-28 --output output/log7_N128
python enclose_certificate.py output/log7_N128
python analyze_certificate.py output/log7_N128 --shift 4e-15 --decay 6e-29 --generator-bound 14
```

The floors, shifts and decays for the other horizons are in `output/enclosure_summary.json`
(and Table 1 of the manuscript). Replay recomputes the analytic bounds, the full-Gram
trace check and the central leakage from the saved head and Grams, then repeats both ball
LDL tests; the enclosure step re-tests every reported floor as an exact rational.

## Full rebuild

```bash
python certify_arb.py --N 128 --M 220 --bits 1792 --log-horizon 7 --floor 1.37e-28 --output output/log7_rebuilt
python certify_arb.py --N 128 --M 180 --bits 1536 --horizon 9/5   --floor 3.38e-23 --output output/rebuilt_1p8
python independent_arb.py --N 128 --M 220 --bits 1792 --log-horizon 7 --floor 1.37e-28 --output output/independent_rebuilt_log7
python review_checks.py
python compare_implementations.py
```

Each 128-mode construction takes 30–90 s; `log2 … log6` use `--log-horizon n` with
`--M 220 --bits 1792`. The builder accepts `0 < L < 3` (the domain of the profile
remainder); acceptance is not positivity. Exact integer comparisons handle logarithmic
endpoints; other unresolved threshold comparisons fail closed. Exact finite-path cosine
norms are used for the delay operators.

## Regenerating the manuscript tables

```bash
python enclose_certificate.py output/log2_N128 output/log3_N128 output/log4_N128 \
  output/log5_N128 output/log6_N128 output/length_1p8_N128 output/log7_N128 --summary output
python make_tables.py
```

`make_tables.py` asserts that each `central_certificate.json` floor equals the enclosure
floor, that each `analysis.json` continuation matches the enclosure constants, and that
the even upper bound (upper endpoint of its ball) is below the odd floor in every row. It
parses each Arb ball string as an interval and rounds outward: lower values (tail floor,
pivots) from the lower endpoint downward, upper values (upper bounds, model error, matrix
radius) from the upper endpoint upward. `output/enclosure_table.tex`, written by
`enclose_certificate.py --summary`, is a plain summary record that prints the midpoint of
each printed upper-bound ball; it is not an input to the manuscript.

## Rules that the code enforces and the reader should keep

Never replace a full-output Gram by the square of a compressed matrix. Profile truncation
and the infinite tail remain necessary regardless of precision. LDL pivots are not
eigenvalue lower bounds. Head eigenvalue lists and relative-coupling values are
floating-point diagnostics. Independent code agreement is not an independent proof of the
analytic tail estimate.
