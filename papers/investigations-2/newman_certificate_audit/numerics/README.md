# Newman certificate audit numerics

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: Claude Fable 5.1 (`claude-fable-5-1`). Internal LLM-assisted
computations, not independent validation. The package replays here are
floating-point corroboration of a sealed FLINT/Arb certificate; they are
not themselves certificates.

Audited package: `judegomila/dbn-lambda-01787854-candidate-audit` at commit
`a74738deb6d5e0f76887cb36901da08b68dca705` (see the
[dependency ledger](../notes/1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md)).
No file of the package is stored in this repository; recover it with
`git clone` at that commit and check `sha256sum -c SHA256SUMS` (443 files).

## 1. Error-budget replay (standard library)

[check_newman_error_budget.py](check_newman_error_budget.py) recomputes,
with Python's `decimal` module at 50 significant digits, the Polymath
Theorem 1.3 bounds (20)–(23), the display (24) with its stated constant
`10.44`, and the Section 6 refined bounds for `e_C` and `e_{C,0}`, at the
package's exact row (`X = 6000000185827`, `t_0 = 129/800`,
`y_0^2 = 87677/2500000`, `N = 690988`), at both ends of the finite-lane
height range, at two corners of the closed barrier box, and at the
repository's own Note 22 calibration height (`m = 22066`). It then forms the
"C dropped" versus "C retained" budgets and converts the difference into a
maximal parameter gain using the finite-difference sensitivities measured
by the row replay below.

```sh
python3 check_newman_error_budget.py --output /tmp/budget_replay.json
```

The retained record is
[ERROR_BUDGET_REPLAY_RECORD_20261012.json](ERROR_BUDGET_REPLAY_RECORD_20261012.json).
Point evaluation only, no interval arithmetic, no `t`-box: the package's
directed Arb values (`e_{C,0} = 2.3349285e-7` finite lane,
`3.565226e-4` barrier corner) are slightly larger than the pointwise
values here (`2.334925e-7`, `3.565218e-4`), as they must be. The
`e_A + e_B` sum is evaluated over all `N` terms; `--head K` truncates it
for a quick replay.

## 2. Finite-row replay and sensitivities (numpy, float64)

[replay_triangle_row.py](replay_triangle_row.py) reimplements the stored
lower bound of the package's finite lane,

```
L_N = (1 − g − Σ_{n=2}^{DN} w(n) n^{−σ}) / M − g Σ_{m=2}^{N} b_t(m)(m^{κ} − 1) m^{y−σ},
```

with the plain triangle weight `w = |B_{N,n}| + g|A_{N,n}|`
(`--weight triangle`, the weight of every stored row) and, for comparison,
the Polymath Section 8.5 "improved triangle inequality" weight
`w = max(|B − gA|, (1−g)/(1+g)|B + gA|)` (`--weight sharp`, the
`WEIGHT SHARP` mode of the package's own producer source, not used by any
stored row). The Euler mollifier, the constants `g, σ, κ, M` and the
`κ`-correction follow `src/lemma_sweep_p235711.c` and
`NATIVE_BINDING.md` literally. The `DN ≈ 1.6·10^9` terms of the P11 leg
are accumulated in chunks of `2·10^7`; one row takes about 45 s on two
cores. **This script needs numpy and is not a check programme in the
sense of the repository's validation conventions**; it is a benchmark and
replay tool, and its output is float64 with no error bound.

```sh
python3 replay_triangle_row.py --N 690988                      # weakest stored row
python3 replay_triangle_row.py --N 690988 --y2 0.0349708       # sensitivity in y^2
python3 replay_triangle_row.py --N 690988 --t 0.16115          # sensitivity in t
python3 replay_triangle_row.py --N 729000 --mtype 5 --t 161250000/1000000000
python3 replay_triangle_row.py --N 690988 --weight sharp
```

The retained record
[FINITE_ROW_REPLAY_RECORD_20261012.json](FINITE_ROW_REPLAY_RECORD_20261012.json)
lists every run of this session: the replayed rows against their stored
floors, the four sensitivity runs, and the sharp-weight scan. The stored
floors are certified lower bounds that are exact (to the printed six
digits) only at the first row of each producer run; later rows in a run
are deliberately lower (frozen sawtooth weights). The replay reproduces
all first-of-run rows to the stored digits.

## 3. What these computations establish

- The lane formulas of the package are the ones it states, and the
  weakest row is reproduced by an independent implementation.
- The Theorem 1.3 constants are transcribed correctly and the pointwise
  budget agrees with the package's directed enclosures.
- The relative sizes of approximation error and certified margin in each
  lane, and the finite-difference slopes `∂L/∂(y^2) ≈ 9.53`,
  `∂L/∂t ≈ 19.06` at the weakest row, which bound every conceivable gain
  from a smaller error term.

They do not establish Theorem 1.3, the package's analytic reductions, or
any new bound on `Λ`.
