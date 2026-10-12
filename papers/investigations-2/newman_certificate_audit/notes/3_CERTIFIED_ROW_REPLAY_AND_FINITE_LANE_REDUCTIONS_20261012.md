# Certified row replay and audit of the finite-lane reductions

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: Claude Opus 5.5 (configured model `claude-opus-5-5`, Cowork
session; reasoning effort: max). This is an internal LLM-assisted audit
record, not independent mathematical validation or formal verification.

Labels:

- **[checked]**: an argument of the package read and verified step by step here.
- **[proved here]**: a short argument given in this note.
- **[certified computation]**: a standard-library interval or exact computation with error bounds.
- **[float exploration]**: float64 sampling with no error bound.
- **[package]**: a value copied from the pinned package.

Pinned package: `judegomila/dbn-lambda-01787854-candidate-audit` at
`a74738deb6d5e0f76887cb36901da08b68dca705` (seal 443/443).

Companions:

- [dependency ledger](1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md)
- [benchmark](2_FINITE_LANE_REPLAY_AND_CORRECTED_BUDGET_BENCHMARK_20261012.md)
- [cross-model review of notes 1–2](../reviews/1_CROSS_MODEL_REVIEW_OF_NOTES_1_2_20261012.md)
- [numerics](../numerics/README.md)

## 0. Summary

The finite lane proves hypothesis (ii) of Polymath Theorem 1.2 on the
windows `N = 690988…3840000` through five links:

- **(a) Native binding.** In window `W_N`, `|f_{t0}(x+iy)| ≥ L_N(y)` whenever `L_N(y) > 0`.
- **(b) Window freeze.** The constants frozen at the left edge `x_N` are conservative on all of `W_N`.
- **(c) `y`-transfer.** `L_N(y) ≥ L_N(y0)` for `y0 ≤ y ≤ √(1−2t0)`.
- **(d) Stored floors.** `T_N ≤ L_N(y0)` for every stored row.
- **(e) Error budget.** `E_max ≥ e_A + e_B + e_{C,0}` uniformly on the lane.

This session checked (a) and (b) by hand and found them correct. For (c),
it checked the reduction step by step and re-verified the numerical gate
independently with an explicit 25 % margin; the package's reported worst
gate ratio `0.99999860767` is not a margin (§4.3). For (d), it certified
32 stored rows independently, including the weakest row and every
first-of-run row. Link (e) was not re-audited. It rests on the package's
Arb program and on the pointwise agreement recorded in note 1.

The left side of the lane's decisive inequality at its weakest row now has
an independent certificate:

```
L_690988(t0, y0) ≥ 7.9136674559412e-7,    L_690988 − E_max[package] ≥ 5.5787184e-7 > 0.
```

## 1. Native binding [checked]

`NATIVE_BINDING.md` writes the Theorem 1.3 main term as
`f_t = A + γ C_κ`, with `A = Σ_{m≤N} b_t(m) m^{−s*}` and
`C_κ = Σ_{m≤N} m^y b_t(m) m^{−s̄*−κ}`. The argument has four steps.

1. **Convolution identities.** The Euler factor
   `E = Π_{p∈P}(1 − b_t(p) p^{−s*})` has real coefficients
   `λ_d = (−1)^{ω(d)} Π_{p|d} b_t(p)`. Hence `E A = Σ B_{N,n} n^{−s*}` and
   `Ē C_0 = Σ A_{N,n} n^{−s̄*}` exactly. Here `Ē(s*) = E(s̄*)`, and both
   leading coefficients are 1.
2. **Triangle inequality.** `|E||f| = |EA + γ E C_κ|`, and
   `|γ E C_κ| = |γ||Ē C_κ|`. So
   `|E||f| ≥ 1 − g_N − Σ_{n≥2}(|B| + g_N|A|) n^{−σ_N} − g_N |E| C_N`.
   This uses `|m^{−κ} − 1| ≤ m^{|κ|} − 1` for complex `κ`.
3. **Normalization.** `|E| ≤ M_N = Σ|λ_d| d^{−σ_N}`. When
   `L_N = Q_N/M_N − g_N C_N > 0`, the numerator `Q_N` is positive. Then
   `E ≠ 0`, and dividing by `|E| ≤ M_N` goes in the safe direction.
4. **Correspondence with the code.** The stored first-of-run values equal
   this `L_N` to 12 decimals (§3), so the formula in `NATIVE_BINDING.md` is
   the one the producer evaluates.

The binding uses only the bounds `|γ| ≤ g_N`, `Re s* ≥ σ_N` and
`|κ| ≤ k_N`, never their exact values.

## 2. Window freeze [checked]

On `W_N = [x_N, x_{N+1})`:

- `G(x,y) = e^{y/50}(x/4π)^{−y/2}` and `K(x,y) = t0 y/(2(x−6))` decrease
  in `x`;
- `Σ(x,y)` increases in `x`, including at the kink of the positive part.

The positive part is nonincreasing because `h_x = −8y(1+y)/x³ ≤ 0`. The
product of the two nonnegative nonincreasing factors `x^{−2}` and `h_+` is
nonincreasing, and `(t0/4) log(x/4π)` is strictly increasing. Link (a)
needs exactly these three directions, and it needs no monotonicity of
`L_N` in its parameters.

**Coverage.** `x_* = X + √(1 − y0²)` satisfies `x_690988 < x_* < x_690989`
**[package, certified]**. Re-derived here in 50-digit decimal, the margins
are `5,377,393.99` and `11,989,041.17`, matching the package. The
half-open windows tile `[x_*, x_3840001)`, and the tail starts at
`x_3840000`.

**Improved inequality.** The same freeze holds for the improved
inequality, because its bound is monotone in the `γ`-bound (review 1
§3.3; §5 below).

## 3. Certified replay of stored rows [certified computation]

### 3.1 Method

The programme is
[`check_finite_row_certified_replay.py`](../numerics/check_finite_row_certified_replay.py).
It uses only the standard library, is deterministic, and writes a JSON
record. It certifies an interval containing

```
L_N = (1 − g_N − Σ_{n=2}^{DN} (|B_{N,n}| + g_N|A_{N,n}|) n^{−σ_N}) / M_N − g_N C_N
```

at `t = t0 = 129/800` and `y = y0`, for the leg's prime set.

- **Enumeration.** Write `n = G k` with `G = gcd(n, D)`. Then
  `gcd(k, D/G) = 1`, the active divisors are `d = G/e` with `e | G` and
  `e k ≤ N`, and `B_{N,n} = Σ_e λ_{G/e} b_t(ek)`. Every contributing `n`
  has `k ≤ N`, so the sum has about `N Π_p(2 − 1/p)` terms with
  `2^{|P|} N` incidences. For the weakest row that is 11,024,402 terms and
  22,111,615 incidences, not the `DN ≈ 1.6·10^9` integers a direct loop
  scans.
- **Tables.**
  - *Computation.* `b_t(m)`, `b_t(m) m^y` and `m^{−σ}` (`m ≤ N`) are
    computed with `decimal` at 45 digits. Arithmetic is correctly
    rounded; `exp` and `ln` are documented as correctly rounded.
  - *Error bound.* `rho_bound()` bounds the relative error of every table
    value, and the programme asserts that it is at most `10^{−40}`.
- **Fixed point.**
  - *Accumulation.* The sum is accumulated exactly in integers at scale
    `2^{110}`, and every shift is a floor.
  - *Error bound.* An a-priori bound `E_S` on all rounding errors is
    derived in the source from the table maxima, the incidence bound and
    the number of terms, and it is added in both directions. For the
    weakest row, `E_S = 5.6·10^{−20}`.
- **Scalars.** `g_N`, `σ_N`, `κ_N`, `M_N` and `C_N` are enclosed with
  directed-rounding interval arithmetic. `C_N` uses
  `κ ln m ≤ m^κ − 1 ≤ κ ln m N^κ`.
- **Self-test.** A brute-force sum over every `n ≤ DN` (prime sets
  `{2,3,5,7,11}`, `{2,3,5,7}`, `{2,3,5}`, `{2,3}` at small `N`) agrees
  with the enumeration to within `10^{−29}`. This checks the enumeration
  and the error bound, not the transcription of the formula. The
  transcription is checked by the 12-decimal agreement with the stored
  first-of-run rows, a separate implementation (the producer's Arb code),
  and by the float replay of note 2.

Runtime is about 100 s per row in the `{2,3,5,7,11}` leg, dominated by
the tables, and about 125 µs per `m ≤ N` in general.

### 3.2 Results

| `N` | leg | run start | `t`-box | certified `L_N(t0, y0)` (lower end) | stored floor `T_N` | `L_lo − T_N` | 12-decimal floor reproduced |
| ---: | --- | :---: | --- | ---: | ---: | ---: | :---: |
| 690988 | `{2,3,5,7,11}` | yes | singleton | `7.9136674559413e-07` | `0.000000791366` | `7.46e-13` | yes |
| 690989 | `{2,3,5,7,11}` | yes | singleton | `9.7406212746181e-07` | `0.000000974062` | `1.27e-13` | yes |
| 690990 | `{2,3,5,7,11}` | no | singleton | `1.6229410379101e-06` | `0.000001570095` | `5.28e-08` | — |
| 690991 | `{2,3,5,7,11}` | yes | singleton | `1.8911327595971e-06` | `0.000001891132` | `7.60e-13` | yes |
| 690995 | `{2,3,5,7,11}` | no | singleton | `3.5661471834657e-06` | `0.000003354765` | `2.11e-07` | — |
| 690996 | `{2,3,5,7,11}` | yes | singleton | `4.1855654846157e-06` | `0.000004185565` | `4.85e-13` | yes |
| 691011 | `{2,3,5,7,11}` | yes | singleton | `1.0281698054118e-05` | `0.000010281698` | `5.41e-14` | yes |
| 691051 | `{2,3,5,7,11}` | yes | singleton | `2.6905674686835e-05` | `0.000026905674` | `6.87e-13` | yes |
| 691151 | `{2,3,5,7,11}` | yes | singleton | `6.8664152808200e-05` | `0.000068664152` | `8.08e-13` | yes |
| 691501 | `{2,3,5,7,11}` | yes | singleton | `2.1484006993842e-04` | `0.000214840069` | `9.38e-13` | yes |
| 693001 | `{2,3,5,7,11}` | yes | singleton | `8.3996754980222e-04` | `0.000839967549` | `8.02e-13` | yes |
| 697001 | `{2,3,5,7,11}` | yes | singleton | `2.4980553778586e-03` | `0.002498055377` | `8.59e-13` | yes |
| 707001 | `{2,3,5,7,11}` | yes | singleton | `6.5867770778364e-03` | `0.006586777077` | `8.36e-13` | yes |
| 718001 | `{2,3,5,7,11}` | yes | singleton | `1.0993582868608e-02` | `0.010993582868` | `6.08e-13` | yes |
| 728999 | `{2,3,5,7,11}` | no | singleton | `1.5307934770239e-02` | `0.014771594320` | `5.36e-04` | — |
| 729000 | `{2,3,5,7}` | yes | `10⁻⁹` box | `3.1516877049158e-04` | `0.000315112459` | `5.63e-08` | — |
| 818999 | `{2,3,5,7}` | no | `10⁻⁹` box | `3.3428312532302e-02` | `0.029586978955` | `3.84e-03` | — |
| 819000 | `{2,3,5}` | yes | `10⁻⁹` box | `3.0584404030128e-04` | `0.000305788807` | `5.52e-08` | — |
| 1027999 | `{2,3,5}` | no | `10⁻⁹` box | `6.4311755796635e-02` | `0.057544045266` | `6.77e-03` | — |
| 1028000 | `{2,3}` | yes | `10⁻⁹` box | `3.0933866525076e-04` | `0.000309285478` | `5.32e-08` | — |
| 1030000 | `{2,3}` | no | `10⁻⁹` box | `8.8922464901921e-04` | `0.000822612862` | `6.66e-05` | — |
| 1030001 | `{2,3}` | yes | `10⁻⁹` box | `8.8940929931775e-04` | `0.000889356157` | `5.31e-08` | — |
| 1050001 | `{2,3}` | yes | `10⁻⁹` box | `6.6021486762313e-03` | `0.006602095978` | `5.27e-08` | — |
| 1100001 | `{2,3}` | yes | `10⁻⁹` box | `2.0238161656158e-02` | `0.020238110009` | `5.16e-08` | — |
| 1300001 | `{2,3}` | yes | `10⁻⁹` box | `6.7117427999005e-02` | `0.067117380094` | `4.79e-08` | — |
| 1700001 | `{2,3}` | yes | `10⁻⁹` box | `1.3588493578226e-01` | `0.135884893359` | `4.24e-08` | — |
| 2000000 | `{2,3}` | no | `10⁻⁹` box | `1.7388163209101e-01` | `0.170256181382` | `3.63e-03` | — |
| 2200001 | `{2,3}` | yes | `10⁻⁹` box | `1.9495422753808e-01` | `0.194954190481` | `3.71e-08` | — |
| 2800001 | `{2,3}` | yes | `10⁻⁹` box | `2.4450892941672e-01` | `0.244508896569` | `3.28e-08` | — |
| 3000000 | `{2,3}` | no | `10⁻⁹` box | `2.5774254380653e-01` | `0.256532255230` | `1.21e-03` | — |
| 3300001 | `{2,3}` | yes | `10⁻⁹` box | `2.7536978809999e-01` | `0.275369757891` | `3.02e-08` | — |
| 3840000 | `{2,3}` | no | `10⁻⁹` box | `3.0190010391060e-01` | `0.299655457299` | `2.24e-03` | — |

All 32 stored floors lie below the certified lower bound; none lies above
the certified upper bound. The interval widths are `2·10⁻²¹` to `7·10⁻²⁰`.
All 12 first-of-run rows with a singleton time box reproduce the stored
12-decimal floor exactly.

The 11 first-of-run rows with a time box lie `3·10⁻⁸` to `5.6·10⁻⁸` below
`L_N(t0)`. That is the expected effect of the box: a slope near `19` gives
about `2·10⁻⁸` for a width of `10⁻⁹`, and Arb's ball arithmetic over the
time box widens it further. Rows that are not first of a run lie
`5·10⁻⁸` to `7·10⁻³` below `L_N(t0)`, as frozen sawtooth weights make them.

The self-test agrees with brute force to within `8·10⁻³⁰` for each prime
set. With `--package`, the 32 stored values were re-read from the pinned
shards after their SHA-256 hashes were checked. The run took 54 minutes on
two cores; the record is
[CERTIFIED_ROW_REPLAY_RECORD_20261012.json](../numerics/CERTIFIED_ROW_REPLAY_RECORD_20261012.json).

### 3.3 What this establishes

- **Independent certificate of the weakest row.** It agrees with the
  stored floor to all 12 printed decimals, and together with the package's
  `E_max` it gives the lane's decisive inequality with margin
  `5.5787184e-7`. This upgrades note 2 §2 from corroboration to an
  independent certificate of the weakest row.
- **First-of-run rows with a singleton time box.** All of them reproduce
  exactly.
- **Rows that are not first of a run, and rows with a time box.** Their
  stored floors lie below the certified `L_N(t0)`, by amounts consistent
  with the frozen sawtooth weights and the `t`-box of width `10^{−9}`.
- **Not established.** The other 3,148,981 rows were not recomputed. The
  package's external review reports a full regeneration of the sweep in
  its pinned container, but that regeneration used the same code.

## 4. The Dini `y`-transfer

### 4.1 The reduction [checked]

`provenance/TRIANGLE_Y_DINI_THEOREM.independent.md` shows that each
summand `(|B| + γ_N(y)|A(y)|) n^{−σ_N(y)}` of the Triangle mass is
nonincreasing in `y`. Each step was checked as follows.

1. **Slope of `σ_N`.** `σ_N(y₂) − σ_N(y₁) ≥ (y₂ − y₁)/2`, because the
   positive part decreases in `y` (`h_y = −3 + 4(1+2y)/x² < 0`).
2. **Dini derivative at a zero of `A`.** `D⁺(γ|A|) ≤ γ(g|A| + |A'|)` with
   `g = γ'/γ = 1/50 − ½ log q_N`. At a zero of `A` the upper-right Dini
   derivative of `|A|` is `|A'|`, so the bound holds there as well.
3. **Divisor-pattern form.** The factorization
   `λ_d b_t(n/d) = (−1)^{ω(d)} b_t(n) r_d(L)` holds with
   `r_d = exp((t/4)(Σ_{p|d} log²p + log²d − 2L log d))`. The
   `Σ log² p` term is right: the Euler coefficient is `Π b_t(p)`, not
   `b_t(d)`.
4. **Bracket.** With `G = γ e^{yL} = e^{y(L+g)}` (note that
   `γ_N = e^{yg}`), the bracket is at most
   `b_t(n)[G h − (L/2)|C_0|]`, where `h = |LC + C'| + (g − L/2)|C|`. So
   `D⁺ ≤ 0` when `h ≤ 0` or when `G h < (L/2)|C_0|`.
5. **From pointwise to global.** A continuous function with `D⁺ ≤ 0`
   everywhere is nonincreasing, which is the classical Dini monotonicity
   theorem; Lipschitz continuity is not even needed.
6. **Normalizer and `κ`-correction.** `M_N` is nonincreasing in `y`. The
   log-rate bound `g + ½ log N + ρ log N + 1/y0 < −1.36` makes `K_N`
   nonincreasing. Both were checked.

A documentary point: the note states the gate as
`G max(h, 0) < (L/2)|C_0|`. That fails at the zeros of `C_0`, which occur
at `n = p ∈ P`, where `B_p = 0` exactly. The verifier, however, accepts
`h ≤ 0` as a separate branch, and that branch is what the proof needs
(§4.5).

### 4.2 Exhaustiveness and the two `q`-branches [checked]

- **Patterns.** The pairs (gcd pattern `G₀`, sector `d_{j−1} < n/N ≤ d_j`)
  number `Σ_{G₀|D} τ(G₀) = 3^{|P|}`, and each fixes the active set
  `{d | G₀ : d ≥ d_j}` independently of `y`.
- **Bounds on `q_N`.** The verifier bounds `q_N` from below by
  `N_min² − t/16`, valid for every `N` in the leg. Above `log(N_min d_j)`
  it uses `e^{2L}/d_j² − t/16`, valid because `n ≤ d_j N`.
- **Monotonicity in `g`.** The `g`-dependent part `U(g) = e^{y(L+g)}[K + gc]_+`
  is nondecreasing in `g`, so a lower bound on `q_N` is the safe
  direction.
- **Domain.** The covered `L`-domain, `[log 2, log(N_max d_j)]` for
  `j = 0` and `[log(N_min d_{j−1}), log(N_max d_j)]` for `j > 0`, contains
  `log n` for every `n` active in the sector at some `N` of the leg. It
  also contains many values of `L` that no such `n` attains, for example
  `L < log G₀` when `j = 0`.

### 4.3 The reported worst ratio is a property of the bisection, not a margin

**Interpretations in the package.**

- `PROOF_NOTE.md` (4.10) reports `ratio ≤ 0.99999860767275095 < 1`.
- The package's external referee calls this "the thinnest load-bearing
  inequality … slack ≈ 1.39×10⁻⁶".

**What the number is.** The verifier bisects each cell until a leaf's
interval upper bound for `G h_+/((L/2)|C_0|)` falls below 1, and it
reports the largest such bound among the accepted leaves. Because a leaf
is accepted as soon as its bound drops below 1, that maximum sits just
under 1 by construction, whatever the true supremum.

**Location of the reported worst leaves.** Every reported worst leaf lies
where the true ratio is small, and all but one lie at values of `L` that
no active `n` attains. These are float samples on 101 × 41 points per leaf
**[float exploration]**.

| leg | reported leaf | reported bound | sampled ratio in leaf | attained by an integer `n`? |
| --- | --- | ---: | ---: | --- |
| `{2,3,5,7,11}` | `G₀ = 66`, `L ∈ [1.0419, 1.0543]` | 0.9999986 | ≤ 0.119 | no (`n ≥ 66`) |
| `{2,3,5,7}` | `G₀ = 210`, `L ∈ [2.519, 2.532]` | 0.99997 | 0 (`h < 0`) | no |
| `{2,3,5}` | `G₀ = 30`, `L ∈ [0.718, 0.725]` | 0.999995 | 0 (`h < 0`) | no |
| `{2,3}` | `G₀ = 6`, `L ∈ [3.570, 3.981]` | 0.992 | 0 (`h < 0`) | yes (`n = 36, 42, 48`) |

**True supremum.** Over the whole covered domain
([`explore_dini_gate_landscape.py`](../numerics/explore_dini_gate_landscape.py),
20001 × 81 points per cell) the sampled supremum of the ratio is:

| leg | sampled sup, covered domain | sampled sup, attained `L` | max of `h` over domain |
| --- | ---: | ---: | ---: |
| `{2,3,5,7,11}` | 0.711 (`G₀ = 70`, `L = log 2`, `y = y0`) | 0.661 (`G₀ = 330`, sector `(10, 11]`, `L ≈ 15.75`) | 1.57 |
| `{2,3,5,7}` | 0.703 (`G₀ = 70`, `L = log 2`) | 0.368 (`G₀ = 210`, sector `(3, 5]`) | 0.77 |
| `{2,3,5}` | 0.186 (`G₀ = 30`, `L = log 2`) | 0 | 0.035 |
| `{2,3}` | 0 | 0 | −0.204 |

### 4.4 Re-verification with margin [certified computation]

[`check_dini_gate_margin.py`](../numerics/check_dini_gate_margin.py)
re-verifies the gate on the same domain with a stricter acceptance rule.
A leaf passes only if `h ≤ 0` or `G h ≤ θ (L/2)|C_0|`, with per-leg
thresholds `θ = (3/4, 3/4, 1/4, 0)`. It uses only the standard library:
decimal intervals with directed rounding, with term enclosures that
exploit the monotonicity of each `s_d r_d(L) d^{−y}` in `L` and `y` and of
`g − L/2` and `L + g` in `L`.

| leg | `θ` | leaves | leaves with `h ≤ 0` | undecided | package leaves (bound `< 1`) | package reported bound |
| --- | :---: | ---: | ---: | ---: | ---: | ---: |
| `{2,3,5,7,11}` | 3/4 | 268,748 | 82,411 | 0 | 297,490 | `0.99999860767275095` |
| `{2,3,5,7}` | 3/4 | 50,301 | 16,734 | 0 | 52,239 | `0.99997108988463879` |
| `{2,3,5}` | 1/4 | 19,673 | 7,424 | 0 | 9,290 | `0.99999531405046582` |
| `{2,3}` | 0 | 771 | 771 | 0 | 237 | `0.99224052112549543` |

So the gate holds with these certified supremum bounds:

- **`{2,3,5,7,11}` and `{2,3,5,7}`:** supremum at most `3/4` on the
  package's whole covered domain.
- **`{2,3,5}`:** supremum at most `1/4`.
- **`{2,3}`:** `h ≤ 0` everywhere, so each summand's `A`-side and
  `B`-side are separately nonincreasing.

**Lower bounds.** The programme also certifies lower bounds of the ratio
on small rectangles at the sampled maximizers (record field
`negative_control`):

- `{2,3,5,7,11}`: ratio `≥ 0.7107` for `G₀ = 70` with
  `L ∈ [log 2, 0.6931471806]` and `y = y0`;
- `{2,3,5,7}`: ratio `≥ 0.7029` at the same point;
- `{2,3,5}`: ratio `≥ 0.1857` for `G₀ = 30` at the same point;
- `{2,3,5,7,11}`, at a value of `L` an integer attains: ratio `≥ 0.6605`
  at `n = 6910020 = 330·20940`, `N = 690988`, `y = y0`. Here
  `n/N = 10.0002`, so `n` lies in sector `(10, 11]`, and the `q`-bound is
  exact.

The suprema therefore lie in `[0.7107, 3/4]`, `[0.7029, 3/4]` and
`[0.1857, 1/4]`. The gate has at least 25 % certified slack everywhere on
the covered domain: about 29 % at the worst covered point and about 34 %
at the worst attained one. It does not have a slack of `1.4·10⁻⁶`.

The certified run took about 4 minutes; the record is
[DINI_GATE_MARGIN_RECORD_20261012.json](../numerics/DINI_GATE_MARGIN_RECORD_20261012.json).

This is a different implementation (Python `decimal` against Arb) with a
different stopping rule and different enclosures. It shares the
reduction of §4.1, which is the part checked by reading.

### 4.5 Zeros of `C_0` [float exploration]

Over the four legs, `C_0(L)` has 30 zeros inside covered cells:

- 14 at `L = log p` for `G₀ = p ∈ P`, the only ones an integer `n`
  attains (there `B_p = 0`, because the Euler factor removes `n = p`);
- 16 at values of `L` that no integer `n` with that gcd pattern attains,
  for example `L ≈ 2.81` when `G₀ = 66`.

At every zero, `max_y h ≤ −0.32`. The `h ≤ 0` branch therefore
covers neighbourhoods of all zeros, and the certified run resolves them
without undecided leaves.

### 4.6 What (c) still depends on

It still depends on the reduction of §4.1, which was checked by reading
and is not machine-verified, and on the normalizer and `κ`
monotonicities, which were checked by reading. The package's Lean layer
(`lean/aristotle`) was not inspected.

## 5. The improved inequality at the certified row [float exploration; outside the audit]

Review 1 §3.3 proves the improved ("sharp") triangle inequality with
weight `(1 − g) U_g(b, a)`, where
`U_g(b,a) = (|b − g²a| + g|a − b|)/(1 − g²)`, and shows that it holds for
every `g ≥ |γ|` because `U_g` increases with `g`. Two consequences matter
for a decision about a sharp-weight campaign.

1. **Only `t0` needs to move.** At the same `X` and `y0`, lowering `t0`
   to `t0' < t0` leaves hypotheses (i) and (iii) certified.
   - *(iii):* the package's barrier certificate covers
     `R = [X, X+1] × [0.1809, 1]` for all `t ∈ [0, 0.16125]`, and the
     region (iii) requires at `t0'` lies inside `R × [0, t0']`.
   - *(i):* it depends only on `X` and `y0`.

   Only hypothesis (ii) at `t0'` would need new work: a sharp-weight
   finite sweep, its `y`-transfer, the tail lemma, and `E_max` at `t0'`.
2. **The first rows of all four legs stay positive at `t0' = 0.157`.**
   With the current leg structure and the sharp weight
   (`replay_triangle_row.py --weight sharp`):

| `N` (leg) | `L` plain, `t = 0.157` | `L` sharp, `t = 0.157` | `L` sharp, `t = t0` |
| --- | ---: | ---: | ---: |
| 690988 (`{2,3,5,7,11}`) | −0.0870 | +0.00178 | +0.0770 |
| 729000 (`{2,3,5,7}`) | −0.0876 | +0.00263 | — |
| 819000 (`{2,3,5}`) | −0.0892 | +0.00358 | — |
| 1028000 (`{2,3}`) | −0.0916 | +0.00478 | — |

The sharp lane's boundary at the first row is near `t = 0.1569`. A bound
`Λ ≤ 0.157 + y0²/2 = 0.1745354` therefore looks reachable at the
Platt–Trudgian height with the published method, subject to the work
listed in item 1.

**Caveats.**

- Of the three, the tail is the least predictable. Its contraction
  constant is `D = 0.99972` at `t0`, and a smaller `t` lowers `σ`, so a
  larger starting index `N*` may be needed.
- These are float values at four rows. They are not a certificate and not
  a claim.
- Note 2 §6 left the decision to pursue this with Teddy; it is not pursued
  here.

## 6. Remaining obligations and decision

| Link or item | Status |
| --- | --- |
| (a) native binding | checked |
| (b) window freeze | checked |
| (c) `y`-transfer | reduction checked; gate re-verified with margin |
| (d) stored floors | 32 rows certified independently; full sweep regenerated by the package with its own code |
| (e) `E_max` uniform budget | not re-audited: proof-to-code map of `verify_prop410_arb.c` |
| tail lemma (`N ≥ 3840000`) | not audited |
| barrier: Lemma 8.4 majorants, prism gate, `B_t ≠ 0`, `t → 0` | not audited; needs Polymath §8, which the WebFetch extraction available here does not reach |

**Decision.** The finite lane, which carries the certificate's only small
margin, has now been audited at every link except the uniform error
budget. No defect was found.

The next audit target is the barrier's derivative majorants. That audit
needs the Polymath PDF in the session, kept outside the repository. It
should be followed by the proof-to-code map of the uniform budget.

A sharp-weight campaign at `t0' ≈ 0.157` is now a well-defined option
with reusable hypotheses (i) and (iii). It is Teddy's decision, as note 2
§6 records.
