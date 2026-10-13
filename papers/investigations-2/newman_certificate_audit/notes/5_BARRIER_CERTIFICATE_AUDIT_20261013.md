# Barrier certificate: audit of hypothesis (iii)

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the
serving model may differ), Anthropic, Cowork session; reasoning effort
max. This is an internal LLM-assisted audit record, not independent
mathematical validation or formal verification.

This note carries out step B2 of the parallel plan: the
[Claude amended plan](../../brainstorm/reviews/REVIEW_OF_CODEX_RESPONSE_AND_PARALLEL_PLAN_CLAUDE_20261012.md)
§4.3, as confirmed by the
[Codex strategy assessment](../../brainstorm/reviews/STRATEGY_AND_PARALLEL_LAYOUT_REVIEW_CODEX_20261012.md).
It audits the package's proof of hypothesis (iii) of Polymath Theorem 1.2:
that `H_t` has no zero in the closed rectangle
`R = [X, X+1] + i[0.1809, 1]` for every `0 ≤ t ≤ t0`. It covers the
Lemma 8.4 derivative majorants and their extension to the whole box, the
closed-prism gate, the evaluation of `f_t` from stored sums, the uniform
approximation error and the extension to `t = 0`.

Labels:

- **[source]**: read from a pinned primary source.
- **[checked]**: an argument of the package or of the paper, read and verified step by step here.
- **[proved here]**: a short argument given in this note.
- **[certified computation]**: a standard-library computation with directed rounding.
- **[replay]**: the package's own program, rebuilt and rerun here.
- **[corroboration]**: an independent FLINT/Arb program written here. Same library as the package, so not a certificate in this repository's sense.
- **[package]**: a value copied from the package.

Pinned package: `judegomila/dbn-lambda-01787854-candidate-audit` at
`a74738deb6d5e0f76887cb36901da08b68dca705`, the clone whose seal
(443/443) was re-verified on 12 October (note 4).

Notation: `X = 6000000185827`, `t0 = 129/800`, `N = 690988`,
`q(x) = x/4π`, `L = log q(X)`. The rectangle's lower edge is
`y_min = 0.1809`. It lies below Theorem 1.2's `y0 = √(87677/2500000) =
0.18727…`. Throughout, `s = (1 − y + ix)/2` is the barrier program's
variable.

A verification pass in the same session checked §§2–10 against the
sources, the records and its own mpmath, rational and floating scripts.
It was run by a separate Claude subagent. It confirmed every item and
reproduced the direct majorant sums and the Taylor total. Its
corrections are incorporated: the paper's intermediate display in §3.1
is true as written, (21) in its displayed form also enters the finite
lane, the `D_t` tolerance is 2 only up to rounding, and several smaller
points of wording. This was a same-family check, not an independent
review.

Companions: [note 4](4_TAIL_LEMMA_AND_UNIFORM_ERROR_BUDGET_AUDIT_20261012.md)
(Polymath imports §2, `B_t ≠ 0` §3.8), the
[dependency ledger](1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md), and
the [numerics](../numerics/README.md) §§8–9.

## 0. Summary

1. **No defect was found.** Every analytic link of the barrier was read and
   checked. Its decisive inequalities were recomputed independently, and
   the four Arb programs were rebuilt and replayed byte for byte (the
   barrier transcript up to its timing line).
2. **Lemma 8.4 is correct (§3).** One intermediate display of its proof
   writes `(|α(s)| + |α(1−s)| − log n)/2` where the triangle inequality
   gives `|α(s) + α(1−s) − log n|/2`. The written form is true here (it
   is the larger, by about `π²/(16 log(x/4π))`), but it does not follow
   by the stated step. The next display bounds the quantity the step
   gives, and the lemma follows. It also holds at `t = 0`.
3. **Polymath's own gate (91) is not what its argument gives.** It
   divides the time term by `2n`, as `D_t|t′ − t|/(2n)`. The argument
   needs `D_t|t′ − t|`, which is what the package's gate uses (§5.5). The
   package does not inherit the slip.
4. **The derivative-box lemma is correct (§4).** Its endpoint separation,
   the `A`-core monotonicity in `y`, and its head-plus-integral bound all
   check. (21) enters the barrier in its displayed form, inside `const1`,
   at every `y ∈ [0.1809, 1]`. Note 4 §2 proved that form true, and its
   positive-part term weighs `6.35·10⁻²⁷`. It enters the finite lane in
   the same form, which corrects note 4's remark that the package uses
   neither display (§4.1).
5. **One gate is thin but structural.** The tail-exponent gate
   `c0 > (1/2) log N` has margin `2.24·10⁻⁷`. Up to `10⁻²⁶` it is the
   window inequality `N² < X/4π`, which holds with
   `X/4π − N² = 4.28·10⁵`.
6. **The prism gate and its homotopy are correct (§5).** The factor
   `1/2` in `D_z/(2(num − 1))` is justified by the nearer-endpoint disks.
   Then the argument principle excludes zeros of `H_t` in `R` for every
   `t ∈ [0, t0]`, and `R` contains the region of hypothesis (iii).
7. **The stored-sum evaluation is correct (§6).** The identity behind the
   62 × 62 matrix was verified by hand. The Taylor-tail certificate's
   hypotheses were re-derived from explicit formulas for `α`, and its
   bound was recomputed: `1.954234593244761·10⁻²² < 10⁻²⁰`.
8. **The approximation budget and `t → 0` check (§7).** The uniform
   bound `e_A + e_B + e_{C,0} ≤ 3.5652301160003966838·10⁻⁴ < 0.00125`
   was recomputed; it agrees with the package's Arb value to `3.6·10⁻³⁵`.
   The extension of Theorem 1.3 to `t = 0` needs only that uniform bound
   on `(0, t0]` and the continuity of `H_t/B_t − f_t` in `t`.
9. **Computations (§9).**
   - A standard-library checker passes all 44 gates.
   - It re-parses both sealed transcripts and recomputes all 883 prism
     gates of each in exact rationals. The smallest margin is
     `0.519849894613872543387`, at prism 882.
   - It sums the Lemma 8.4 majorants directly over all `n ≤ N` at five
     prisms. The transcript's integer ceilings exceed the direct sums by
     `0.004 %` to `3.4 %`.
   - An independent direct-summation Arb evaluator of `f_t`, which uses
     no stored sums, agrees with the barrier's stored-sum values at 117
     mesh points, the minimum-modulus point of each sampled prism
     included. Every difference is below `1.01·10⁻³` of the radius the
     barrier carries.
10. **Tolerances (§10).** The derivative majorants would have to be
    `×1.497` too small, jointly, at prism 882; `D_z` alone `×1.988`;
    `D_t` alone `×2`, by construction of the step (up to rounding). The
    approximation allowance has room `×1.46·10³` over the actual error.
11. **Status of hypothesis (iii).** Audited at every link. What remains is
    the imported results (Polymath Theorems 1.2 and 1.3, FLINT's
    quadrature and ball arithmetic), and the quadrature values at the 878
    prisms that were not summed directly.

## 1. Sources

**Package files read** (SHA-256 prefixes):

| File | SHA-256 |
| --- | --- |
| `BARRIER_CERTIFICATE.md` | `81bea050…` |
| `DERIVATIVE_BOX_LEMMA.md` | `e8dd32e1…` |
| `barrier/src/TloopSinglemat_closed_cert.c` | `76e4d4f8…` |
| `barrier/src/StoredSumSinglemat_interval.c` | `34da5fb7…` |
| `barrier/src/StoredSumTaylorTail_cert.c` | `480ddcd1…` |
| `barrier/src/verify_uniform_error_01787854.c` | `dd61648f…` |
| `barrier/compare_storedsum_intervals.py`, `scripts/run_barrier_replay.sh` | read |
| `barrier/data/storedsum_nolemma_6000000185827_dig_20.txt` | `d022692f…` |
| `barrier/certificates/barrier_target_closed.log` | `2d010f70…` |
| `barrier/certificates/barrier_target_closed_macos_arm64_flint36.log` | `34f8ed82…` |
| `barrier/certificates/storedsum_interval_regenerated.txt`, `storedsum_provenance.log` | `588fe436…`, `9f0b732e…` |
| `barrier/certificates/storedsum_taylor_tail.log`, `uniform_error_256.log` | `31102fa5…`, `7f43bc24…` |
| `ERROR_CONSTANT_WELD.md` | `4c29fdcd…` |
| `verifiers/verify_barrier_binding.py` (the package's parser) | read |
| `src/lemma_sweep_p235711_triangle_stored.c` l. 325–355, `WINDOW_FREEZE_THEOREM.md`, `verifiers/verify_window_freeze.py` (for §4.1) | read |

Also read: Polymath's historical barrier program
`dbn_upper_bound/arb/TloopSinglematv2.c` (SHA-256 `81d868fa…`), for §5.5.

**Polymath.** `Writeup/debruijn.tex` of `km-git-acc/dbn_upper_bound`
(SHA-256 `0115d452…`), as in note 4 §1; §8.4 is lines 1421–1569. The
repository's `debruijn.aux` gives the numbering used here: (5) the region,
(9) the formula for `α`, (20)–(24), (43) the bound on `α′`, (91) the
barrier condition, (92) the two-sum form of `f_t`, Lemma 8.4.

## 2. What the barrier imports from Polymath [source]

| Item | Content used | Where used |
| --- | --- | --- |
| Theorem 1.2 (iii) | no zero of `H_t` for `X ≤ x ≤ X + √(1 − y0²)`, `√(y0² + 2(t0 − t)) ≤ y ≤ √(1 − 2t)`, `0 ≤ t ≤ t0` | the target; §5.6 |
| Theorem 1.3 with (20)–(23) and the `10.50` weld | `|H_t/B_t − f_t| ≤ e_A + e_B + e_{C,0}` on region (5) | the allowance `0.00125`; §7 |
| (20), (21), (22) | `|γ|`, `Re s*`, `|κ|` | the majorants, §4 |
| (9), (43) | `α(s) = 1/(2s) + 1/(s − 1) + (1/2) Log(s/2π)`; `|α′(s)| ≤ 1/(2 Im s − 6)` for `Im s > 3` | Lemma 8.4, §3 |
| (92) | `f_t = Σ_{n≤N} b_n n^{−s*} + γ Σ_{n≤N} b_n n^{−s**}`, `s** = s + (t/2)α(s)` | stored sums, §6 |
| Lemma 8.4 | the two derivative bounds | re-derived in §3 |

Theorem 1.2's region lies inside `R`. In it, `x ≤ X + √(1 − y0²) < X + 1`,
`y ≥ √(y0² + 2(t0 − t)) ≥ y0 > 0.1809` (since `y0² − 0.1809² =
234599/10⁸`), and `y ≤ √(1 − 2t) ≤ 1` **[checked]**.

## 3. Lemma 8.4 [checked]

The lemma bounds `|∂f_t/∂z|` and `|∂f_t/∂t|` on region (5), away from
jumps of `N`. Here `N` is constant on the closed slab (§7.1). Write
`s = (1 − y + ix)/2`, so `1 − s = (1 + y − ix)/2`. Then
`s* = (1 − s) + (t/2)α(1 − s)` and `s** = s + (t/2)α(s)`.

### 3.1 The `z`-derivative

- `f_t` is holomorphic, so `|∂f_t/∂z| = |∂f_t/∂x|`.
- **`B` sum.** `∂s*/∂x = −i/2 − (it/4)α′(1 − s)`. The bound (43) applies
  at the conjugate point `(1 + y + ix)/2`, and `|α′(z̄)| = |α′(z)|`.
  Hence `|∂s*/∂x| ≤ 1/2 + t/(4(x − 6))`.
- **`A` sum.** Its factor is
  `∂_x log γ − (∂_x s**) log n`. Here
  `∂_x log γ = (it/4)(α(s)α′(s) + α(1−s)α′(1−s)) + (i/2)(α(s) + α(1−s))`
  and `∂_x s** = i/2 + (it/4)α′(s)`. So the factor is at most
  `(1/2)|α(s) + α(1−s) − log n| + t(|α(s)| + |α(1−s)|)/(4(x − 6)) + t log n/(4(x − 6))`.
- **The intermediate display.** The paper writes
  `(|α(s)| + |α(1−s)| − log n)/2` where the step above gives
  `|α(s) + α(1−s) − log n|/2`. Since `|a + b − c| ≤ |a| + |b| − c` is
  false in general, the written form does not follow by that step. It is
  nevertheless true here: `α(s) + α(1−s) ≈ log(x/4π)` while
  `|α(s)| + |α(1−s)| ≈ √(log²(x/4π) + π²/4)`, so the written form is the
  larger, by about `π²/(16 log(x/4π))` (`0.0229` at `x = X`; checked
  numerically at 25 points with `200 ≤ x ≤ 3·10⁴` by the verification
  pass). The next display bounds the quantity the step gives.
- **The logarithmic factor.** By (9), `|1/(2s)| ≤ 1/x` and
  `|1/(s − 1)| ≤ 2/x`. Also `0 ≤ log(|s|/(2πn)) ≤ log(|1 − y + ix|/4π)`
  for `n ≤ N ≤ x/4π`, and `|Arg s| ≤ π/2`. Together:
  `|α(s) − (1/2) log n| ≤ (1/2) log(|1 − y + ix|/4π) + π/4 + 3/x`. That
  is stronger than the paper's `π/2 + 3/(2x)` once `x ≥ 6/π`. The same
  holds for `1 − s` with `|1 + y + ix|`. So both `|α(s) + α(1−s) − log n|`
  and `|α(s)| + |α(1−s)|` are at most
  `L1 := log(|1 + y + ix|/4π) + π + 3/x`.
- **The `A` weight.** `n^{−Re s**} = n^{y − Re κ} n^{−Re s*} ≤ N^{|κ|} n^y n^{−Re s*}`,
  since `Re s** = Re s* − y + Re κ` and `n ≤ N`.

This is the lemma's first bound:

```
|∂f_t/∂z| ≤ Σ_{n≤N} b_n n^{−Re s*} (log n)(1/2 + t/(4(x−6)))
          + |γ| N^{|κ|} Σ_{n≤N} b_n n^y n^{−Re s*} [ t log n/(4(x−6)) + L1 (1/2 + t/(4(x−6))) ].
```

### 3.2 The `t`-derivative

- `∂_t s* = α(1 − s)/2`, `∂_t s** = α(s)/2`,
  `∂_t log b_n = log² n/4`, `∂_t log γ = (α(s)² − α(1−s)²)/4`.
- By (43) along a horizontal segment of length at most 1, and by (9) at
  `ix/2`: `α((1 ± y + ix)/2) = (1/2) log(x/4π) + πi/4 + O_≤(4/(x − 6))`.
  Conjugate for `(1 ± y − ix)/2`.
- Hence `|log n/2 − α(1 − s)|`, and likewise with `α(s)`, is at most
  `(1/2) log(x/4πn) + π/4 + 4/(x − 6)`. Multiplied by `(log n)/2`, this
  gives `(1/4) log n log(x/4πn) + (π/8) log n + 2 log n/(x − 6)`.
- `|α(s)² − α(1−s)²| ≤ (π/2 + 8/(x − 6))(log(x/4π) + 8/(x − 6))`.

This is the lemma's second bound, as stated.

### 3.3 At `t = 0`

The proof uses only (9), (43) and the definitions. Its statement keeps
`|γ|`, `N^{|κ|}` and `Re s*` themselves, so it holds verbatim at `t = 0`
**[proved here]**. The majorants of §4 also use (20)–(22), and those hold
at `t = 0` as well: (21) and (22) trivially (`Re s* = (1+y)/2`,
`κ = 0`), and (20) by continuity in `t`, its right side being
independent of `t`. `DERIVATIVE_BOX_LEMMA.md` reaches the same conclusion
by a limit `ε ↓ 0`.

## 4. The derivative-box lemma [checked]

Lemma 8.4 is pointwise in `(x, y, t)`. The program needs suprema over
`[X, X+1] × [y_min, 1]` at a seam, and over the closed prism for `D_t`.

### 4.1 The `B` side

- Put `h(x,y) = 1 − 3y + 4y(1+y)/x²` and
  `c(x,y) = (1/4) log q(x) − h₊/(2x²)`. By (21),
  `Re s* ≥ (1+y)/2 + t c(x,y)`.
- `h_y = −3 + 4(1 + 2y)/x² < 0` (gate `12/X² − 3 < 0`), and
  `h_x = −8y(1+y)/x³ ≤ 0`. So `h₊` decreases in both variables, and `c`
  increases in both. The program's own explicit gate,
  `c_x ≥ 1/(4(X+1)) − 2/X³ > 0`, is a valid second route: with
  `X² > 8`, `h₊ ≤ 1`, and `|∂_x(h/(2x²))| ≤ 1/x³ + 8/x⁵ ≤ 2/x³`.
- Hence, with `c0 = c(X, y_min)` and
  `P(n) = n^{−(1+y_min)/2 + t(log n/4 − c0)}`:
  `b_n n^{−Re s*} ≤ P(n)` on the whole box.

**The form of (21).** The barrier uses (21) in its displayed form,
`4y(1+y)/x²`, at every `y ∈ [y_min, 1]`.

- For `y ≥ 1/3` that form follows from the paper's written proof, since
  `4y(1+y) ≥ 8y(1−y)` there.
- For `y < 1/3` it does not follow from the written proof, and
  `y_min = 0.1809` is in that range. Note 4 §2 proved it true on the
  whole region: the proof discards a term
  `(t/8) log(1 + (1+y)²/x²)` of order `t/(8x²)`, against a
  discrepancy of order `t/x⁴`. A floating check here on
  `0 ≤ y ≤ 1` and four values of `x` from 200 to `X` found the slack
  at least `t/(8x²)`.
- Numerically `h₊/(2X²) ≤ 6.352·10⁻²⁷`. Replacing `h₊` by 1 would change
  `const1` by `7.5·10⁻²⁷`, far below every tolerance.

**A correction to note 4.** Note 4 §0 says that the package depends on
neither of the two displays. That holds for the tail and for `E_max`,
which bound the positive part by 1. The finite lane does use (21) in its
displayed form: the producer (`src/lemma_sweep_p235711_triangle_stored.c`,
l. 336–349) and `WINDOW_FREEZE_THEOREM.md` (with its check S6 in
`verifiers/verify_window_freeze.py`) use `(1 − 3y + 4y(1+y)/x_N²)₊` on
`y ∈ [y0, y_max]`, and `y0 < 1/3`. Since the display is true, nothing
changes. The dependency should be recorded.

### 4.2 The `A`-side core

By (20), (21) and (22), the `A` weight `|γ|N^{|κ|} b_n n^y n^{−Re s*}`
is at most `b_n 𝒜` with
`𝒜 = e^{0.02y} q(x)^{−y/2} N^{ty/(2(x−6))} n^y n^{−(1+y)/2 − t c(x,y)}`.
Its log has `y`-derivative at most
`η = 0.02 − (1/2) log q(x) + t log N/(2(x − 6)) + (1/2) log n`: the
`−t c_y log n` term is `≤ 0`, and at the kink of `h₊` an upper
right derivative serves. The program fails closed unless `η < 0` at
`x = X`, `t = t_top`, `n = N`. Since `η` increases in `t` and `n` and
decreases in `x`, that is the worst case; the value is `η ≤ −6.7029`
**[certified computation]**. So `𝒜` is largest at `y = y_min`. It also
decreases in `x`. With §4.1, the `A` weight is therefore at most
`afac·n^{y_min} P(n)`, where
`afac = e^{0.02 y_min} q(X)^{−y_min/2} N^{t y_min/(2(X−6))}`.

`DERIVATIVE_BOX_LEMMA.md` writes the core with `n^{−Re s*}` itself. For
that form `η` misses a term of size at most `t log n/(4(x − 6)) ≈ 10⁻¹³`.
The argument is rigorous for `𝒜`, with the (21) bound in place of
`Re s*`, and `𝒜` is what the program evaluates.

### 4.3 The remaining factors, and the program's integrands

Every other factor is nonnegative and is bounded at its own worst
endpoint:

- `1/(x − 6)`, `3/x`, `8/(x − 6)` at `X`;
- `log(x/4π)` at `X + 1`;
- `|1 + y + ix|` at `(X + 1, 1)`.

The program's summands are then exactly the lemma's terms
**[checked]**, with `tq = t/(4(X − 6))`:

- `D_z`: `P(n)[log n (1/2 + tq(1 + afac n^{y_min})) + n^{y_min} afac L1⁺ (1/2 + tq)]`,
  with `L1⁺ = log(|2 + i(X+1)|/4π) + π + 3/X` (l. 28–99, 126–152).
- `D_t`: `P(n)[(1 + afac n^{y_min}) log n (C − log n/4) + n^{y_min} afac E]`,
  with `C = log((X+1)/4π)/4 + π/8 + 2/(X − 6)` and
  `E = (1/4)(π/2 + 8/(X − 6))(log((X+1)/4π) + 8/(X − 6))` (l. 230–299, 326–355).

The `D_t` bracket `log n (C − log n/4)` is the lemma's
`(1/4) log n log(x/4πn) + (π/8) log n + 2 log n/(x − 6)`, bounded above.
The gate `2 log N < log(X/4π)` keeps it nonnegative for every `n ≤ N`
(l. 1097–1106). For `D_t` the program evaluates `afac` and the summand
with the interval `t ∈ [t_i, t_{i+1}]` (l. 1385–1428), so no monotonicity
in `t` is assumed.

### 4.4 Head plus integral [checked]

The sum over `n ≤ N` is bounded by the exact terms `n = 1, …, 16` plus
`∫_16^N F(u) du`, which is valid if each summand `F` decreases on
`[16, N]`. With `r = log u`, `P` has logarithmic derivative
`p = −(1 + y_min)/2 + t(r/2 − c0)`.

- **Tail-exponent gate** `c0 > (1/2) log N`. It gives
  `p ≤ −(1 + y_min)/2` for `r ≤ log N`. Margin
  `≥ 2.2406·10⁻⁷` **[certified computation]**. This is thin, but up to
  `h₊/(2X²) ≈ 6·10⁻²⁷` it is `(1/4) log(q(X)/N²) > 0`, i.e. the window
  inequality `N² < X/4π`, which holds with `q(X) − N² = 427919.33`.
- **The components.** Each summand is a nonnegative combination of `Pr`,
  `P u^{y_min} r` and `P u^{y_min}` for `D_z`. For `D_t` it combines
  `PB`, `P u^{y_min} B` and `P u^{y_min}`, with `B = r(C − r/4) ≥ 0` and
  `B′/B ≤ 1/r`. All logarithmic derivatives are at most `p + y_min + 1/r`.
- **Tail-monotonicity gate** `(y_min − 1)/2 + 1/log 16 < 0`. Value
  `≤ −0.048876` **[certified computation]**.

The code integrates `F(Nz)` over `z ∈ [16/N, 1]` and multiplies by `N`,
which is the integral above (l. 164–210, 367–411). The callbacks keep the
complex integration variable and use FLINT's analytic `log` and `pow`
with the analytic flag set exactly when `order ≠ 0`. They fail closed if
the integrator never requests an analytic enclosure. The correctness of
`acb_calc_integrate` itself is imported. At five prisms the direct sums
of §9.1 make the integral unnecessary: the ceilings bound the true sums.

## 5. The prism gate and the argument principle [checked]

### 5.1 Mesh

Each edge carries `num = D_z` points, corners included, so the mesh has
`4 num − 4` points (l. 650–832). In the program's `s`-coordinates the
points are `x = X` and `x = X + 1` with `y` from `y_min` to 1, and
`y = 1` and `y = y_min` with `x` from `X` to `X + 1`. Adjacent points are
at most `h = 1/(num − 1)` apart; on the vertical edges the spacing is
`(1 − y_min)/(num − 1)`.

### 5.2 The homotopy

- Let `F(σ)`, `0 ≤ σ ≤ 1`, be the true image `f_{t_i}` of one subedge,
  and `P(σ)` the chord between its endpoint values.
- For `σ ≤ 1/2`, both `|F(σ) − F(0)|` and `|P(σ) − F(0)|` are at most
  `σ D_z h ≤ D_z h/2`. For `σ ≥ 1/2` the same holds about `F(1)`.
- At time `τ ∈ [t_i, t_{i+1}]`,
  `|H_τ/B_τ − f_{t_i}| ≤ 0.00125 + D_t(τ − t_i)` pointwise on `∂R`.
- So both `H_τ/B_τ` on the subedge and the chord lie in the disk about
  the nearer stored value of radius `D_z h/2 + D_t(t_{i+1} − t_i) + 0.00125`.
  The disk is convex, so it contains the straight-line homotopy between
  them.
- Gate (1) of `BARRIER_CERTIFICATE.md` makes that radius smaller than
  `M_i ≤ |F(0)|, |F(1)|`, where `M_i` is the minimum lower modulus over
  the mesh. So the homotopy avoids 0.

The mesh values are Arb balls, and `M_i` is the minimum of their lower
endpoints (l. 611–616: `arb_min`, not the historical `arb_lt` test). The
gate is a strict interval comparison (l. 1430–1444).

### 5.3 Winding

- Each increment `Arg(F_j/F_{j+1})` is required to lie strictly inside
  `(−π, π)` as a ball, and the closing increment too (l. 1257–1294). A
  chord that avoids 0 changes the argument by its principal increment,
  and a ball that stays inside `(−π, π)` cannot straddle the cut. So the
  sum encloses `2π` times the polygon's winding number.
- The enclosure of the winding number must lie in `(−1/4, 1/4)`, so the
  integer is 0 (l. 1296–1306).
- The code accumulates `Arg(f(z_j)/f(z_{j+1}))`, the reverse orientation.
  That changes nothing here.

### 5.4 Time stepping, seams, the last prism

- The next seam is an exact dyadic number: half a directed lower bound
  of `(M_i − spatial − 0.00125)/D_t`, added with downward rounding
  (l. 1348–1383).
- `D_t` is then recomputed on the closed prism, rounded up to an integer,
  and the gate is rechecked (l. 1385–1444).
- Consecutive seams are the same Arb number (l. 1470–1471), so the prisms
  abut exactly. The first seam is exactly 0 (l. 986–993).
- The last right seam is `target_cover`, a dyadic upper bound of the
  decimal `0.16125 = t0` (l. 972–975). Only its part in `[0, t0]` is
  used, and the allowance `0.00125` is invoked only for `τ ≤ t0`.

### 5.5 Polymath's (91)

Polymath's barrier condition (91) reads
`|f_t(z_j)| > 1.25·10⁻³ + D_z/(2n) + D_t|t′ − t|/(2n)`, with `n` points
per edge. The argument of §5.2 gives `D_t|t′ − t|`. Nothing in it makes
the time motion smaller by a factor `2n` **[proved here]**: for
`f_t = c − D_t t`, (91) would allow `t′ − t` up to about `2n|c|/D_t`.
The package's gate (1) has `D_t(t_{i+1} − t_i)` with no division. It is
the stronger condition, and the right one.

Polymath's own program `dbn_upper_bound/arb/TloopSinglematv2.c`
(l. 970–975) steps by `(M − 1/2)/D_t`, with the undivided time term, so
the `/(2n)` is a slip of the write-up **[source]**. That program also
left `1/2` for the spatial term, which with `num = ⌈D_z⌉` points per edge
is `D_z/(2 num)` rather than the `D_z/(2(num − 1))` the mesh needs, and
it reserved nothing for `1.25·10⁻³`. The package's program corrects all
three; its comment at l. 1340–1344 records the spatial one. These remarks
concern Polymath's historical run, not this package, and were not
pursued.

### 5.6 Conclusion

For each `τ ∈ [0, t0]`, `g_τ = H_τ/B_τ` is holomorphic near `R`. It has
no zero on `∂R`, and the winding number of `g_τ(∂R)` about 0 is that of
the polygon, which is 0. By the argument principle `g_τ` has no zero in
`R`. Since `B_τ ≠ 0` (note 4 §3.8), neither has `H_τ`. With §2, this is
hypothesis (iii).

## 6. Evaluating `f_t`: the stored sums [checked]

### 6.1 The identity

The archived matrix, which `StoredSumSinglemat_interval.c` regenerates
as Arb balls, is, with `x_c = X + 1/2`, `n0 = N/2` and `ℓ_n = log(n/n0)`:

```
M[e][k] = Σ_{n=1}^{N} n^{(−1 + i x_c)/2} ℓ_n^e/e! (ℓ_n²/4)^k/k!,   0 ≤ e, k ≤ 61.
```

The barrier program forms `poly(w) = Σ_{e,k} w^e t^k M[e][k]` (l. 834–867).
At a mesh point it sets `β = −s* + (1 − i x_c)/2` and
`w = β + (t/2) log n0`, and returns
`n0^{β + (t/4) log n0} poly(w)` (l. 561–602). Without truncation, the
exponent of the `n`-th term is

```
(β + (t/4)ℓ0)ℓ0 + ((−1 + i x_c)/2) ℓ + (β + (t/2)ℓ0)(ℓ − ℓ0) + (t/4)(ℓ − ℓ0)²  =  −s* ℓ + (t/4) ℓ²,
```

with `ℓ = log n` and `ℓ0 = log n0`. So the value is `Σ_n b_n n^{−s*}`.

- The `A` sum is the same construction at `s̄ + (t/2)α(s̄)`, then
  conjugated. By `α(z̄) = conj α(z)` this gives `Σ_n b_n n^{−s**}`.
- `afac`, in this routine the exact factor rather than the majorant of
  §4.2, is `exp((t/4)(α(s)² − α(1−s)²)) H01(s)/H01(1 − s)`, where
  `H01 = 8M_0`. That is `M_t(s)/M_t(1 − s) = γ`.
- Altogether the value is (92).

### 6.2 Archived decimals and restored radii [checked; replay]

The archived matrix is printed to 20 decimal places with no radii. The
reader restores a radius `10⁻²⁰ max(1, |component|)` on each real and
imaginary component (l. 1766–1777).

`compare_storedsum_intervals.py` checks that each of the 7,688
independently regenerated Arb balls fits inside the restored ball. The
worst ratio is `0.0177`.

Rebuilt here, the generator reproduces the sealed
`storedsum_interval_regenerated.txt` byte for byte, and the comparison
passes with no containment failure **[replay]**.

### 6.3 The omitted Taylor terms [checked; certified computation]

`StoredSumTaylorTail_cert.c` argues as follows:

- **Remainder.** With `T_m` the degree-`< m` Taylor polynomial, the
  remainder `|e^a e^b − T_m(a)T_m(b)|` is at most
  `e^{|b|} R(|a|) + e^{|a|} R(|b|)`. Here
  `R(r) = Σ_{k≥62} r^k/k! ≤ r^62/62!/(1 − r/63)`.
- **Arguments.** `|w ℓ_n| ≤ A = 0.66|ℓ_n|` needs `|w| < 0.66`, and
  `t ℓ_n²/4 ≤ B = 0.2 ℓ_n²/4` needs `t ≤ 0.2`. Write `I_A = R(A)` and
  `I_B = R(B)`.
- **Expansion radius.** `w = (s − (1 + i x_c)/2) + (t/2)(log n0 − α(1 − s))`.
  The first part has real part of size `y/2 ≤ 1/2` and imaginary part of
  size `|x − x_c|/2 ≤ 1/4`. Put `D = log n0 − α(1 − s)`, and for the `A`
  sum the same with `s̄`.
- **Outer factors.** `|n0^{β + (t/4) log n0}| = n0^{−y/2 − (t/2)(Re α(1−s) − (1/2) log n0)} ≤ 1`.
  For the `A` sum the factor is at most `|γ| √n0`.
- **Total.** The error is at most
  `(1 + 0.089 √n0) Σ_n n^{−1/2}(e^B I_A + e^A I_B) ≤ √n0 Σ_n …`.

The package checks `|Re D| < 0.694` and `|Im D| < 0.7855` by Arb on the
box. Here they follow from explicit formulas **[proved here]**. For
`u = (a − ix)/2` with `a ∈ [0, 2]` (`a = 1 + y` for `1 − s`, `a = 1 − y`
for `s̄`):

```
Re α(u) = a/(a² + x²) + 2(a − 2)/((a − 2)² + x²) + (1/2) log(√(a² + x²)/4π),
Im α(u) = x/(a² + x²) + 2x/((a − 2)² + x²) − (1/2)(π/2 − atan(a/x)).
```

So `Re α ∈ [L/2 − 4/X², (1/2) log(√(4 + (X+1)²)/4π) + 2/X²]` and
`Im α ∈ [−π/4, −π/4 + 4/X]`.

- `−Re D ≤ 0.6931476286762888`, so `|Re D| < 0.694`. The value is close to
  `log 2`, because `n0 = N/2` and `N ≈ √q`.
- `0 < Im D ≤ π/4`, so `|Im D| < 0.7855`.
- `Re α ≥ (1/2) log n0` with a wide margin.
- `|w| ≤ 0.6479080065465433` with the package's constants and its
  `t`-bound `0.1809`. (The package names that variable `t0`; its value is
  `y_min`, not `t0 = 0.16125`, and as an upper bound for `t` it is
  harmless.) With the bounds here and `t ≤ t0`, `|w| ≤ 0.6381060218135189`.
  Both are `< 0.66`.
- `|γ| ≤ e^{0.02 y_min} q(X)^{−y_min/2} ≤ 0.0881477087069745 < 0.089` by (20).
  The package also checks the exact `|γ|` on a 256 × 128 cell grid: at
  most `0.0886`.

The direct sum, recomputed with directed rounding, is
`√n0 Σ_n n^{−1/2}(e^B I_A + e^A I_B) ≤ 1.954234593244761·10⁻²²`. The
package's value is `1.95423459324476·10⁻²²`. The program adds `10⁻²⁰` to the real
and imaginary radii of every value (l. 539–543, 608). That covers a
complex error of modulus `10⁻²⁰`.

## 7. The approximation error, and `t → 0` [checked; certified computation]

### 7.1 The uniform budget

`verify_uniform_error_01787854.c` bounds, on
`[X, X+1] × [y_min, 1] × [0, t0]`:

- **`N`.** `N = 690988` at the corners `(X, 0)` and `(X + 1, t0)`, and
  `N` is monotone in `x` and `t`. Also `N² < X/4π`.
- **Sum core.** `Σ_{n≤N} b_n n^{−Re s*} ≤ 1 + (N^{1−a} − 1)/(1 − a)`, with
  `a = (1 + y_min)/2 − t0(1 + 8/X²)/(2X²)`. This uses (21) with
  `h₊ ≤ 1 + 8/X²`, and `log n ≤ log q(x)`.
- **Prefactor.** `1 + |γ|N^{|κ|}n^y ≤ 1 + e^{0.02} N^{t0/(2(X−6))}`.
- **`e_A + e_B`.** (23) with `log²(x/4πn²) ≤ log²((X+1)/4π)`, divided by
  `X − 6.66`.
- **`e_{C,0}`.** The weld with `(X/4π)^{−(1+y_min)/4}`. The heat factor
  is bounded by 1, `3^y + 3^{−y} ≤ 10/3`,
  `|L + iπ/2| ≤ √(log²((X+1)/4π) + π²/4)`, and the denominator is
  `X − 12`.

Each bound is evaluated at its worst corner, and each monotonicity is
elementary **[checked]**. The recomputed total is
`3.565230116000396683802985102688452·10⁻⁴`. The package's Arb upper
endpoint is `3.565230116000396683802985102688090540476·10⁻⁴`, so the
difference is `3.6·10⁻³⁵` **[certified computation]**. The program's own
scope note says that the analytic justification at `t = 0` is external;
§7.2 supplies it.

### 7.2 `t = 0` [checked]

`BARRIER_CERTIFICATE.md` passes to the limit `t ↓ 0`:

- `H_t(z)` is continuous in `t` by dominated convergence, with majorant
  `e^{t0 u² + u}|Φ(u)|`.
- `B_t` and `1/B_t` are continuous, and `f_t` is a fixed finite sum.

The fourth item of its list, the continuity of the error majorant, is not
needed. The bound `|g_t − f_t| ≤ 3.57·10⁻⁴` holds for every `t ∈ (0, t0]`
uniformly, and `g_t − f_t` is continuous at `t = 0`. So the bound holds
at `t = 0`. No interchange of `x → ∞` with `t → 0` is used.

## 8. Proof-to-code map [checked]

Line numbers refer to `barrier/src/TloopSinglemat_closed_cert.c`.

| Item | Code | Agrees |
| --- | --- | :---: |
| stored-sum reader; restored `10⁻²⁰` radii | l. 1710–1783 | yes |
| closed-slab endpoints, `ts = 0`, `target_cover` | l. 972–993 | yes |
| `N` constant at opposite corners | l. 995–1004 | yes |
| midpoints `x_c = X + 1/2`, `y_c = (1 + y_min)/2`; `n0 = N/2`; `(1 − i x_c)/2` | l. 1012–1027 | yes |
| `c_x` gate | l. 1041–1064 | yes |
| `A`-core gate `η < 0` | l. 1066–1095 | yes |
| bracket gate `2 log N < log(X/4π)` | l. 1097–1106 | yes |
| `h_y` gate | l. 1108–1120 | yes |
| `const1 = c(X, y_min)` | l. 1122–1137 | yes |
| tail-exponent and tail-monotonicity gates | l. 1139–1165 | yes |
| `afac` at the seam; `D_z`, `D_t` and integer ceilings | l. 1188–1227 | yes |
| `D_z` integrand and head + integral | l. 28–227 | yes |
| `D_t` integrand, `const2`, head + integral | l. 230–428 | yes |
| mesh | l. 650–832 | yes |
| value at a mesh point: `α`, `β`, `afac`, stored sums, `+10⁻²⁰`, `M_i` | l. 430–634 | yes |
| winding gates | l. 1257–1308 | yes |
| spatial term `D_z/(2(num − 1))` | l. 1340–1346 | yes |
| step and dyadic seam | l. 1348–1383 | yes |
| `D_t` on the closed prism | l. 1385–1428 | yes |
| decisive gate (1) | l. 1430–1444 | yes |
| coverage and aggregate winding | l. 1474–1492 | yes |

The right-edge extrema (l. 1235–1255) are computed at every prism, but
they are checked and printed only when `prt = 1` (l. 1310–1338). They
are not used. The sealed run is
`barrier_closed 0 0.16125 0.1809 0 storedsum_nolemma_6000000185827_dig_20.txt`
(`scripts/run_barrier_replay.sh`).

## 9. The computations

### 9.1 Standard-library checker [certified computation]

The programme is
[`check_barrier_suppliers.py`](../numerics/check_barrier_suppliers.py),
and its record is
[`BARRIER_SUPPLIERS_RECORD_20261013.json`](../numerics/BARRIER_SUPPLIERS_RECORD_20261013.json).

**Method.** `decimal` at 34 digits. `+ − × /` use directed rounding;
`exp`, `ln` and `sqrt` are correctly rounded and padded by a relative
`10⁻³²`; `π` comes from Machin's formula in exact rationals;
`e^u − 1` uses a rational series bound. Its five parts:

- **uniform**: §7.1, with every gate.
- **gates**: the gates of §4, with values.
- **majorants**: the program's `D_z` and `D_t` summands, summed directly
  over `n = 1, …, N` with no integral. `D_z` is evaluated at the seam;
  `D_t` on the closed prism, with the decreasing heat factor at the left
  seam and the increasing factors at the right seam.
- **transcript**: both sealed transcripts re-parsed. For every prism it
  checks the seams, `mesh = 4 D_z − 4`, the spatial term, the time term
  and the winding, and recomputes gate (1) in exact rationals from the
  printed ball endpoints. The two transcripts are then compared prism by
  prism.
- **taylor**: §6.3.

**Runtime and reproducibility.** The retained record took 556 s in the
cloud container (x86-64, Python 3.13.16). On Teddy's machine (aarch64
Linux VM, Python 3.10.12), with the transcripts fetched there from the
pinned commit and checked against their seals, the same programme was
run in three parts split by `--prisms`, because of a time limit per call
(111 s, 108 s, 92 s). Every gate and every result is identical to the
record, the five direct majorant sums included.

**Results.** All 44 gates pass.

Majorants, direct sums against the transcript's ceilings:

| Prism | seam `t_i` | `D_z` direct | ceiling | `D_t` direct, closed prism | ceiling |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `0` | `9599.0759` | `9600` | `52723.780` | `52726` |
| 2 | `3.5818·10⁻⁵` | `9584.0731` | `9585` | `52641.647` | `52644` |
| 441 | `0.0213490` | `3788.1623` | `3789` | `20874.442` | `20876` |
| 882 | `0.1515257` | `19.3854` | `20` | `102.5581` | `103` |
| 883 | `0.1565727` | `16.4432` | `17` | `85.8955` | `87` |

The head `n ≤ 16` carries `0.15 %` of `D_z` at prism 1 and `20 %` at
prism 882. Every direct sum lies below its ceiling, so at these five
prisms the derivative bounds hold without the integral.

Transcripts:

- Both have 883 prisms, numbered consecutively, with byte-identical
  consecutive seams from exactly 0 to an enclosure of `129/800`.
- Gate (1), recomputed, holds at every prism of both. The smallest
  recomputed margin is `0.519849894613872543387`, at prism 882, in both.
  The package's parser states `0.519849894613872543374989997`. It
  subtracts the upper endpoints of the printed spatial, time and
  allowance balls, where this check uses the exact `D_z/(2(num − 1))`
  and `0.00125`, and takes the smaller of the two transcripts.
- `D_z`, `D_t` and the mesh agree at every prism. The seams differ
  between the two toolchains by at most `1.1·10⁻²⁸`, and only 2 of 883
  right seams are byte-identical.
- 14,493,508 mesh evaluations in each.

### 9.2 Replays [replay]

Rebuilt with gcc 13.3.0 and libflint-dev 3.0.1 (x86-64, Ubuntu 24.04),
with the optimization levels of `scripts/run_barrier_replay.sh` (`-O3`,
and `-O2` for `uniform_error`), the four programs reproduce their sealed
outputs:

- `uniform_error_256.log` and `storedsum_taylor_tail.log`, byte for byte;
- `storedsum_interval_regenerated.txt`, byte for byte, with provenance PASS;
- `barrier_target_closed.log`, all 883 prisms, byte for byte except the
  `cpu/wall` timing line.

These are the versions of the package's canonical toolchain, so this is
a reproduction, not an independent toolchain. The package's macOS
transcript (Apple clang, FLINT 3.6.0) is the cross-toolchain check, and
§9.1 parses it.

### 9.3 Direct-sum corroboration [corroboration]

[`direct_ft_arb.c`](../numerics/direct_ft_arb.c) evaluates
`f_t = Σ_{n≤N} b_n n^{−s*} + γ Σ_{n≤N} b_n n^{−s**}` directly at 256
bits, from (6)–(10), (14)–(17) and (92), with no stored sums and no code
from the package.

An instrumented copy of the barrier program
([patch](../numerics/barrier_dump_instrumentation.patch)) printed the
stored-sum value and radius at every mesh point of one prism:

- prism 882, all 76 mesh points;
- prism 1 (`t = 0`, 38,396 mesh points), every 960th point and the
  minimum-modulus point, 41 in all.

[`compare_direct_and_stored_sum_values.py`](../numerics/compare_direct_and_stored_sum_values.py)
compares the two values; its record is
[`DIRECT_SUM_CORROBORATION_RECORD_20261013.json`](../numerics/DIRECT_SUM_CORROBORATION_RECORD_20261013.json).

| Prism | points | max component `|Δ|` | max `|Δ|`/radius | minimum `|f|` |
| --- | ---: | ---: | ---: | --- |
| 882 | 76 of 76 | `3.7·10⁻²⁴` | `9.8·10⁻⁵` | `1.5672655787014292981` |
| 1 | 41 of 38,396 | `3.0·10⁻²¹` | `1.0·10⁻³` | `4.2783620904181587383` |

Every direct value lies inside the stored-sum ball. The minima equal
the transcript's `min_mesh` to the printed digits. The differences are
mainly the 20-place rounding of the archived matrix. This corroborates
§6 at these points; it uses the same library as the package.

## 10. Tolerances, updated

Each row gives how wrong one supplier would have to be, with the others
held fixed, for the certificate to fail. The barrier rows replace those
of note 4 §6.

| Supplier | Breaks if | Tolerance | Audit status |
| --- | --- | --- | --- |
| Finite floor, `N = 690988` | the triangle mass `S_N` is low by `9.85·10⁻⁷` | relative `1.1·10⁻⁶` | 32 rows certified (note 3) |
| Tail contraction | `D' = P + TR + M_max·AB` reaches 1 | reserve `0.0395` | audited (note 4) |
| Tail error | `err` exceeds `(1 − D')/M_max` | `×2.1·10⁶` | audited (note 4) |
| `E_max` | `E_max` exceeds `L_690988` | `×3.39` | audited (note 4) |
| Barrier `D_z`, `D_t` | the margin of prism 882 is consumed | jointly `×1.497`; `D_z` alone `×1.988`; `D_t` alone `×2` | audited (this note) |
| Barrier approximation | the error exceeds `0.00125` plus the margin of prism 882 | `×1.46·10³` over `3.565·10⁻⁴` | audited (this note) |
| Barrier values of `f_t` | the error exceeds the carried radius by the margin | the radius (`≤ 3·10⁻¹⁸` at the sampled points) would have to grow `×10¹⁷` | audited; corroborated at 117 points |

The `D_t` tolerance is 2, up to rounding (`2 − 1.3·10⁻¹⁹`), at every
prism but the last, where it is `2.48`. Each step spends half of the
remaining budget. The barrier's tolerances are comfortable. The least
tolerant supplier is still the finite floor, at relative `1.1·10⁻⁶`.

## 11. What this establishes and what remains

**Established.** Within the stated tools:

- Lemma 8.4, its extension to the box and to `t = 0`, and the
  head-plus-integral bound;
- the prism gate, its homotopy, the winding and the argument principle;
- the stored-sum identity and the Taylor-tail bound;
- the uniform approximation budget and its extension to `t = 0`;
- independent recomputation of every decisive inequality, including all
  883 prism gates of both transcripts, and byte replay of the four Arb
  programs.

With notes 1–4 and this note, every analytic link of hypotheses (ii)
and (iii) has now been read and checked, and its decisive inequalities
recomputed.

**Not established.**

- The correctness of Polymath Theorems 1.2 and 1.3 and of Platt–Trudgian
  (imports).
- FLINT's ball arithmetic and its quadrature. The `D_z`, `D_t` ceilings
  at 878 of 883 prisms rest on `acb_calc_integrate`. Direct summation at
  the other five agrees.
- The producer's 3,148,981 finite rows that were not recomputed (B3).
- Byte identity of the Polymath source used here with arXiv v2 (note 4 §1).

**Next.** B3, the producer and shard coverage; then B4, consolidation.
