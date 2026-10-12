# Newman certificate audit numerics

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Sections 1–2: Claude Fable 5.1 (`claude-fable-5-1`). Sections 3–5,
added later the same day: Claude Opus 5.5 (`claude-opus-5-5`, reasoning
effort max). These are internal LLM-assisted computations, not independent
validation.

- **Sections 1, 2 and 5** are floating-point corroboration or exploration
  of a sealed FLINT/Arb certificate. They are not certificates.
- **Sections 3 and 4** are standard-library interval computations with
  explicit error bounds. They certify the stated inequalities, provided
  Python's `decimal` module rounds as documented (correct rounding of
  `+ − × /`, `exp`, `ln` and `sqrt`).

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

## 3. Certified replay of stored rows (standard library)

[check_finite_row_certified_replay.py](check_finite_row_certified_replay.py)
certifies an interval containing the stored functional `L_N` at
`t = t0`, `y = y0`, independently of the package's Arb producer, and
compares it with the stored floor `T_N`. `T_N ≤ L_lo` certifies the row;
`T_N > L_hi` would refute it.

**Method.**

- *Enumeration.* Write `n = gcd(n, D)·k` with `k ≤ N`. This gives about
  `1.1·10^7` terms and `2.2·10^7` incidences for a `{2,3,5,7,11}` row,
  instead of the `DN ≈ 1.6·10^9` integers a direct loop scans.
- *Tables.* 45-digit `decimal`, with an asserted relative error of at most
  `10^{−40}`.
- *Accumulation.* Exact integer fixed point at scale `2^110`, with an
  a-priori bound on rounding errors that is added in both directions.
- *Scalars.* Directed-rounding intervals for `g, σ, κ, M` and `C`.
- *Self-test (`--selftest`).* Compares against a brute-force sum over every
  `n ≤ DN` for all four prime sets.

The programme is deterministic. Expect about 100 s per row of the
`{2,3,5,7,11}` leg; for other legs, budget about 125 µs per `m ≤ N`.

```sh
python3 check_finite_row_certified_replay.py                    # weakest row, about 2 minutes
python3 check_finite_row_certified_replay.py --set all-stored --jobs 2 --selftest \
        --package /path/to/clone --output /tmp/replay.json         # about 55 minutes on 2 cores
```

The retained record is
[CERTIFIED_ROW_REPLAY_RECORD_20261012.json](CERTIFIED_ROW_REPLAY_RECORD_20261012.json),
produced by the second command. It covers 32 stored rows: all 23
first-of-run rows (the weakest among them) and 9 others (leg ends, a shard
end, two interior rows of the `{2,3}` leg, and the last row).

`--package` re-reads the stored floors from the pinned package's shards,
after checking their SHA-256 against the embedded hashes.

**Result.** Every stored floor lies below the certified lower bound. The
twelve singleton-time first-of-run floors reproduce to 12 decimals, and
`L_690988 ∈ [7.9136674559412, 7.9136674559419]·10^{−7}`.

## 4. Dini gate re-verification (standard library)

[check_dini_gate_margin.py](check_dini_gate_margin.py) re-verifies the gate
of the package's `y`-transfer theorem
(`provenance/TRIANGLE_Y_DINI_THEOREM.independent.md`) on the package's own
`(L, y)` domain. It requires `h ≤ 0` or `G h ≤ θ (L/2)|C_0|` on every leaf,
with per-leg thresholds.

- **Arithmetic.** Directed-rounding `decimal` intervals at 30 digits, with
  monotone term enclosures.
- **Lower bounds (`--negative-control`).** Certified lower bounds of the
  ratio at the sampled maximizers show how far each `θ` could be lowered.

```sh
python3 check_dini_gate_margin.py --theta 3/4,3/4,1/4,0 --negative-control --output /tmp/dini.json   # about 4 minutes
```

The retained record is
[DINI_GATE_MARGIN_RECORD_20261012.json](DINI_GATE_MARGIN_RECORD_20261012.json).

**Result.** All four legs pass, with no undecided leaf. The suprema lie in:

| leg | supremum |
| --- | --- |
| `{2,3,5,7,11}` | `[0.7107, 3/4]` |
| `{2,3,5,7}` | `[0.7029, 3/4]` |
| `{2,3,5}` | `[0.1857, 1/4]` |
| `{2,3}` | `h ≤ 0` everywhere |

The package's reported `0.99999860767` is the largest accepted-leaf bound
under a stop-below-1 rule, not the supremum.

## 5. Dini gate landscape (numpy, exploration)

[explore_dini_gate_landscape.py](explore_dini_gate_landscape.py) samples
the gate ratio in float64 on 20001 × 81 points per cell. It locates the
maxima and the zeros of `C_0`, and evaluates the ratio inside the leaves
the package reports as worst.

```sh
python3 explore_dini_gate_landscape.py --output /tmp/landscape.json     # about 1 minute
```

The record is [DINI_GATE_LANDSCAPE_RECORD_20261012.json](DINI_GATE_LANDSCAPE_RECORD_20261012.json).
This is an exploration tool, not a check programme.

## 6. What these computations establish

- (Sections 1–2) The lane formulas of the package are the ones it states, and the
  weakest row is reproduced by an independent implementation.
- The Theorem 1.3 constants are transcribed correctly and the pointwise
  budget agrees with the package's directed enclosures.
- The relative sizes of approximation error and certified margin in each
  lane, and the finite-difference slopes `∂L/∂(y^2) ≈ 9.53`,
  `∂L/∂t ≈ 19.06` at the weakest row, which bound every conceivable gain
  from a smaller error term.
- (Sections 3–4) The left side of the finite lane's decisive inequality at
  its weakest row, `L_690988 − E_max ≥ 5.58·10^{−7}` with the package's
  `E_max`, now holds independently of the package's code. So do 31
  further stored floors.
- (Sections 3–4) The gate of the `y`-transfer has a certified slack of at
  least 25 %.

They do not establish Theorem 1.3, the analytic reductions (which note 3
checks by reading), the remaining 3,148,981 stored rows, the uniform error
budget, the tail or the barrier, or any new bound on `Λ`.
