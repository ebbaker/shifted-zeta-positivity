# Newman certificate audit numerics

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Sections 1–2: Claude Fable 5.1 (`claude-fable-5-1`). Sections 3–5,
added later the same day: Claude Opus 5.5 (`claude-opus-5-5`, reasoning
effort max). Sections 6–9, third session (8–9 on 13 October): Claude
Opus 5.5 (`claude-opus-5-5`, reasoning effort max). These are internal
LLM-assisted computations, not independent validation.

- **Sections 1, 2 and 5** are floating-point corroboration or exploration
  of a sealed FLINT/Arb certificate. They are not certificates.
- **Sections 3, 4, 6 and 8** are standard-library interval computations
  with explicit error bounds. They certify the stated inequalities, provided
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

## 6. Tail lemma and uniform error budget (standard library)

[check_tail_and_uniform_error_budget.py](check_tail_and_uniform_error_budget.py)
recomputes, with directed rounding, every quantity and gate of two
programs: the package's tail verifier (`verifiers/verify_tail_arb.c`,
`TAIL_LEMMA.md`) and its uniform finite-lane budget
(`verifiers/verify_prop410_arb.c`, Proposition 4.10 of `PROOF_NOTE.md`).

**Inputs.** The Polymath inputs were read from the paper's TeX source
(`km-git-acc/dbn_upper_bound`, `Writeup/debruijn.tex` at `8e8a6ab`).

**What it computes.**

- *Tail.*
  - `δ̂`, `k̂` and `σ1, σ2` on the `y`-box and the extended hull.
  - The 153,814 exact convolution coefficients `c_m(t)`, as intervals
    over the `t`-box.
  - `P`, `TR`, `OV`, `M_max`, `AB`, and `D` with and without `OV`.
  - The flows, the error terms and every gate value.
  - The head admissible under each form of the `A`-cap gate.
- *`E_max`.* U1–U5, `e_A + e_B`, `e_{C,0}` and `E_max`, with every gate.

**Arithmetic and self-test.**

- *Arithmetic.* `decimal` at 50 digits. `+ − × /` use directed rounding.
  `exp`, `ln` and `sqrt` are correctly rounded and padded by a relative
  `10⁻⁴⁸`. `π` comes from Machin's formula in exact rationals.
- *Self-test (`--selftest`).*
  - The partition (4.3), coefficient by coefficient, in exact integers.
  - `π`.
  - 2,000 random transcendental enclosures against 100-digit values.
  - A floating sanity check of the endpoint cap.

```sh
python3 check_tail_and_uniform_error_budget.py --selftest --output /tmp/tail_rec.json   # 15–55 s
```

The retained record is
[TAIL_AND_UNIFORM_ERROR_BUDGET_RECORD_20261012.json](TAIL_AND_UNIFORM_ERROR_BUDGET_RECORD_20261012.json),
produced by exactly that command. Gates and results are identical on
x86-64 with Python 3.13.16 and on aarch64 with Python 3.10.12.

**Result.**

- All 54 gates pass.
- `OV` is redundant. Without it, `D' ≤ 0.9604782282` and the reserve is
  `0.0395`.
- The extended-hull `A`-cap gate is `1.0000013` and fails at `M + 1`. On
  the box it is `2.02`.
- `E_max ≤ 2.334949052123378488·10⁻⁷`.
- Every value lies on the safe side of the package's Arb value: within
  `1.5·10⁻¹¹` relative for the contraction and `8·10⁻⁸` for the error
  terms.

See [note 4](../notes/4_TAIL_LEMMA_AND_UNIFORM_ERROR_BUDGET_AUDIT_20261012.md).

## 7. Byte replay of the package's Arb verifiers (operational)

These steps need FLINT (`libflint-dev`, which supplies `arb.h`). They are
a replay of the package's own programs, not a check programme of this
repository.

```sh
gcc -O2 -std=c17 -Wall -Wextra -Werror -pedantic $PKG/verifiers/verify_tail_arb.c -o verify_tail_arb -lflint -lmpfr -lgmp
gcc -O2 -std=c17 -Wall -Wextra -Werror -pedantic $PKG/verifiers/verify_prop410_arb.c -o verify_prop410_arb -lflint -lmpfr -lgmp
for b in 256 512; do ./verify_tail_arb $b > tail_arb_$b.log; ./verify_prop410_arb $b > prop410_arb_$b.log; done
for f in tail_arb_256 tail_arb_512 prop410_arb_256 prop410_arb_512; do cmp $f.log $PKG/logs/$f.log; done
```

On 12 October these steps ran in the cloud container: Ubuntu 24.04,
x86-64, gcc 13.3.0, libflint-dev 3.0.1. Those are the versions of the
package's review container, on different hardware. All four transcripts
were byte-identical to the sealed ones:

| Transcript | SHA-256 |
| --- | --- |
| `tail_arb_256.log` | `bd189e50…` |
| `tail_arb_512.log` | `ee09daef…` |
| `prop410_arb_256.log` | `995651e4…` |
| `prop410_arb_512.log` | `3945dee5…` |

Precision 255 was refused. Instrumented copies, which printed gate values
and `D'`, were used only for note 4 and are not retained.

## 8. Barrier suppliers (standard library)

[check_barrier_suppliers.py](check_barrier_suppliers.py) recomputes, with
directed rounding, the suppliers of the package's barrier certificate
(hypothesis (iii); `BARRIER_CERTIFICATE.md`, `DERIVATIVE_BOX_LEMMA.md`,
`barrier/src/*.c`).

**What it computes.**

- *uniform*: the uniform approximation budget on the barrier box, as in
  `verify_uniform_error_01787854.c`.
- *gates*: the gates of the derivative-box lemma, with their values.
- *majorants*: the program's Lemma 8.4 majorants summed directly over
  `n ≤ N`, with no quadrature, at prisms 1, 2, 441, 882 and 883, against
  the transcript's integer ceilings.
- *transcript*: both sealed transcripts parsed and checked against their
  SHA-256 seals, all 883 prism gates of each recomputed in exact
  rationals, and the two compared prism by prism.
- *taylor*: the hypotheses and the bound of `StoredSumTaylorTail_cert.c`.

**Arithmetic.** `decimal` at 34 digits. `+ − × /` use directed rounding.
`exp`, `ln` and `sqrt` are correctly rounded and padded by a relative
`10⁻³²`. `π` comes from Machin's formula in exact rationals, and `e^u − 1`
from a rational series bound.

```sh
python3 check_barrier_suppliers.py --transcript $PKG/barrier/certificates/barrier_target_closed.log \
    --corroborating-transcript $PKG/barrier/certificates/barrier_target_closed_macos_arm64_flint36.log \
    --output /tmp/barrier_rec.json       # about 9 minutes
```

The retained record is
[BARRIER_SUPPLIERS_RECORD_20261013.json](BARRIER_SUPPLIERS_RECORD_20261013.json),
produced by exactly that command (x86-64, Python 3.13.16, 556 s). On
aarch64 with Python 3.10.12, run in three parts with `--prisms 1,2`,
`441,882` and `883`, every gate and result is identical.

**Result.** All 44 gates pass.

- The uniform budget is `≤ 3.5652301160003966838·10⁻⁴ < 0.00125`,
  `3.6·10⁻³⁵` above the package's Arb endpoint.
- Every prism gate holds in both transcripts. The smallest recomputed
  margin is `0.519849894613872543387`, at prism 882. `D_z`, `D_t` and the
  mesh are identical across the two toolchains.
- The direct majorant sums lie below the ceilings at all five prisms, by
  `0.004 %` to `3.4 %`.
- The Taylor tail is `≤ 1.954234593244761·10⁻²² < 10⁻²⁰`.

See [note 5](../notes/5_BARRIER_CERTIFICATE_AUDIT_20261013.md).

## 9. Barrier replays and direct-sum corroboration (FLINT/Arb)

These steps need FLINT. They replay the package's programs and run an
exploration tool. They are not check programmes of this repository.

**Replays.** With `$PKG` the pinned clone:

```sh
F="-I/usr/include/flint -lflint -lmpfr -lgmp"
gcc -O3 $PKG/barrier/src/StoredSumSinglemat_interval.c -o storedsum_interval $F
gcc -O3 $PKG/barrier/src/StoredSumTaylorTail_cert.c -o storedsum_taylor_tail $F
gcc -O3 $PKG/barrier/src/TloopSinglemat_closed_cert.c -o barrier_closed $F
gcc -O2 $PKG/barrier/src/verify_uniform_error_01787854.c -o uniform_error $F
./uniform_error > uniform_error_256.log
./storedsum_taylor_tail > storedsum_taylor_tail.log
./storedsum_interval 6000000185827 20 > storedsum_interval_regenerated.txt     # about 10 minutes
python3 $PKG/barrier/compare_storedsum_intervals.py \
    $PKG/barrier/data/storedsum_nolemma_6000000185827_dig_20.txt storedsum_interval_regenerated.txt
./barrier_closed 0 0.16125 0.1809 0 $PKG/barrier/data/storedsum_nolemma_6000000185827_dig_20.txt \
    > barrier_target_closed.log                                                 # about 20 minutes here
```

On 12–13 October these ran in the cloud container: Ubuntu 24.04, x86-64,
gcc 13.3.0, libflint-dev 3.0.1. Those are the versions of the package's
canonical toolchain, on different hardware.

- `uniform_error_256.log`, `storedsum_taylor_tail.log` and
  `storedsum_interval_regenerated.txt` are byte-identical to the sealed
  ones, and the provenance comparison passes.
- `barrier_target_closed.log` is byte-identical to the sealed one except
  its `cpu/wall` line: all 883 prisms.

**Direct-sum corroboration.** [direct_ft_arb.c](direct_ft_arb.c) evaluates
`f_t` by direct summation over `n ≤ N` at 256 bits, with no stored sums
and no code from the package. The
[instrumentation patch](barrier_dump_instrumentation.patch) turns the
package's barrier program into one that prints the stored-sum value and
radius at every mesh point of its first prism; the patch header lists
the two runs used.
[compare_direct_and_stored_sum_values.py](compare_direct_and_stored_sum_values.py)
compares the two at the same points.

```sh
gcc -O2 direct_ft_arb.c -o direct_ft_arb -lflint -lmpfr -lgmp     # about 5 s per point
patch -o barrier_dump.c $PKG/barrier/src/TloopSinglemat_closed_cert.c < barrier_dump_instrumentation.patch
gcc -O3 barrier_dump.c -o barrier_dump -I/usr/include/flint -lflint -lmpfr -lgmp
# run barrier_dump as in the patch header; select points "t re_s im_s" from the DUMP lines
./direct_ft_arb < pts882.txt > direct882.txt
python3 compare_direct_and_stored_sum_values.py --pair 882 dump882.txt direct882.txt \
    --pair 1 dump1.txt direct1.txt --evaluator-source direct_ft_arb.c \
    --patch barrier_dump_instrumentation.patch --output /tmp/corroboration.json
```

The retained record is
[DIRECT_SUM_CORROBORATION_RECORD_20261013.json](DIRECT_SUM_CORROBORATION_RECORD_20261013.json).
It covers all 76 mesh points of prism 882, and 41 of the 38,396 of
prism 1 (every 960th and the minimum-modulus point). Every direct value
lies inside the stored-sum ball, and the largest difference is `1.0·10⁻³`
of the radius. The dumps themselves (7.4 MB for prism 1) are not
retained; the record carries their SHA-256.

## 10. What these computations establish

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

- (Sections 6–7) Every decisive inequality of the tail lemma and of the
  uniform budget holds in an independent standard-library evaluation. The
  tail's contraction holds without the redundant `OV`, with reserve
  `0.0395`. The sealed Arb transcripts are reproducible byte for byte.
- (Sections 8–9) Every decisive inequality of the barrier holds in an
  independent standard-library evaluation: the uniform budget, the
  derivative-box gates, the Taylor tail, all 883 prism gates of both
  transcripts, and the Lemma 8.4 majorants at five prisms by direct
  summation. The barrier's four Arb programs reproduce their sealed
  outputs, and a direct-summation evaluator agrees with the stored-sum
  values at 117 mesh points.

They do not establish Theorem 1.3, the analytic reductions (which notes
3–5 check by reading), the remaining 3,148,981 stored rows, FLINT's
quadrature at the 878 prisms whose majorants were not summed directly, or
any new bound on `Λ`.
