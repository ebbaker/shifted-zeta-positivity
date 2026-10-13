# Tail lemma and uniform error budget: audit of the remaining analytic suppliers of hypothesis (ii)

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the
serving model may differ), Anthropic, Cowork session; reasoning effort
max. This is an internal LLM-assisted audit record, not independent
mathematical validation or formal verification.

This note carries out step B1 of the parallel plan: the
[Claude amended plan](../../brainstorm/reviews/REVIEW_OF_CODEX_RESPONSE_AND_PARALLEL_PLAN_CLAUDE_20261012.md)
§4.3, as confirmed by the
[Codex strategy assessment](../../brainstorm/reviews/STRATEGY_AND_PARALLEL_LAYOUT_REVIEW_CODEX_20261012.md).
It audits the tail lemma, starting with the partition and the status of
`OV` and then its caps and its all-`N`, `y` and error gates. It also
audits the uniformity gates of the finite-lane error budget `E_max`.

Labels:

- **[source]**: read from a pinned primary source.
- **[checked]**: an argument of the package, read and verified step by step here.
- **[proved here]**: a short argument given in this note.
- **[certified computation]**: a standard-library computation with directed rounding.
- **[replay]**: the package's own program, rebuilt and rerun here.
- **[package]**: a value copied from the package.

Pinned package: `judegomila/dbn-lambda-01787854-candidate-audit` at
`a74738deb6d5e0f76887cb36901da08b68dca705`. The seal (443/443) was
re-verified in a fresh clone this session.

A verification pass in the same session checked §§3.1–3.8, §4.2, the
thin-gate figures, the reverse-order argument and the Polymath
discrepancies. It was run by a separate Claude subagent with its own
scripts, mpmath, and instrumented Arb runs. It confirmed all of them,
and its three corrections of wording are incorporated: (24) is true,
the domain of `M_0`, and the `P` slack. This was a same-family check,
not an independent review.

Companions: the [dependency ledger](1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md),
the [finite-lane audit](3_CERTIFIED_ROW_REPLAY_AND_FINITE_LANE_REDUCTIONS_20261012.md),
the [cross-model review](../reviews/1_CROSS_MODEL_REVIEW_OF_NOTES_1_2_20261012.md),
and the [numerics](../numerics/README.md).

## 0. Summary

1. **Both suppliers check.** No defect was found in the tail lemma
   (`TAIL_LEMMA.md`, `verifiers/verify_tail_arb.c`) or in the uniform
   budget (Proposition 4.10 of `PROOF_NOTE.md`,
   `verifiers/verify_prop410_arb.c`).
2. **`OV` is redundant padding.** The partition (4.3) is exact, and `TR`
   already bounds the entire remainder. The `OV` caps lie inside the
   `TR` caps, so `OV` bounds part of the remainder a second time.
   - Without `OV`: `D' = P + TR + M_max·AB = 0.960478 < 1`, reserve
     `1 − D' = 0.03952`.
   - With `OV`: reserve `2.79·10⁻⁴`, as the package prints. The true
     reserve is 142 times larger.
   - The normalized margin without `OV` is
     `(1 − D')/M_max − err = 0.024574`, against an error of
     `err = 1.17·10⁻⁸`.
3. **`E_max` checks.** The reduction U1–U5 is correct. The budget is
   uniform on every window `N ≥ 690988`, every `y ∈ [y0, √(1 − 2t0)]` and
   the whole `t`-box. The recomputed value is
   `E_max ≤ 2.334949052123378488·10⁻⁷`, so `L_690988/E_max ≥ 3.3892`.
4. **One thin gate, not load-bearing.** The package checks the all-`N`
   gate of the `A`-side cap on the extended `y`-hull. There its margin is
   `1.29·10⁻⁶`, and the head `M = 153814` is the largest for which it
   holds. Reversing the order of the `y`- and `N`-reductions needs the
   gate only on the `y`-box, where it is `2.02` (§3.5).
5. **Paper-internal discrepancies.** Two displayed bounds of the Polymath
   paper do not follow literally from their written proofs: (21) against
   Proposition 6.6(ii), and the constant `10.44` in (24) against `10.50`.
   Both displays are nevertheless true, and the tail and `E_max` depend
   on neither (§2). *Correction, 13 October:* the finite lane and the
   barrier do use (21) in its displayed form; see note 5 §4.1.
6. **Computations.**
   - An independent standard-library recomputation passes all 54 gates.
     It agrees with the package's Arb transcripts to within
     `1.5·10⁻¹¹` relative for the contraction terms and `8·10⁻⁸` for the
     error terms. In every case the package's value is the more
     conservative one.
   - Rebuilt here with gcc 13.3 and FLINT 3.0.1 on x86-64, both Arb
     programs reproduce the four sealed transcripts byte for byte.
7. **Status of hypothesis (ii).** It is now audited at every analytic
   link. What remains is:
   - the barrier, hypothesis (iii);
   - the producer's 3,148,981 rows that were not recomputed;
   - the imported published theorems.

   The Polymath TeX source used here also contains §8, so the barrier
   audit (B2) no longer needs the PDF.

## 1. Sources

**Package files read** (SHA-256 prefixes):

| File | SHA-256 |
| --- | --- |
| `TAIL_LEMMA.md` | `197d1268…` |
| `verifiers/verify_tail_arb.c` | `d077d50b…` |
| `PROOF_NOTE.md` | `eb669afe…` |
| `verifiers/verify_prop410_arb.c` | `0d40f9b8…` |
| `provenance/RECORD_BINDING.upstream.md` (statement of U1–U5) | `9c708b42…` |
| `ERROR_CONSTANT_WELD.md` | `4c29fdcd…` |
| `OPEN_REVIEW_QUESTIONS.md` | `f7b1aaa9…` |
| `PROP410_ARB_PROVENANCE.md`, `TAIL_PROVENANCE.md` | `3b3ac1ec…`, `93ca44d1…` |
| `provenance/ERROR_TERMS_AUDIT.upstream.md` | `da91b3da…` |
| `logs/tail_arb_{256,512}.log` | `bd189e50…`, `ee09daef…` |
| `logs/prop410_arb_{256,512}.log` | `995651e4…`, `3945dee5…` |

The header of the supplementary Python line
`verifiers/verify_tail_1787854_256.py` (`3e1718f1…`) was also read.

**Polymath.** Earlier sessions read arXiv:1904.12438v2 through WebFetch,
whose text extraction stops in §7. This session read the paper's TeX
source from the Polymath project's own repository instead:

- `km-git-acc/dbn_upper_bound`, `Writeup/debruijn.tex` at `8e8a6ab`
  (7 August 2019, SHA-256 `0115d452…`).
- Since `a377700` (26 July 2019, "implemented referee changes",
  `560a28fe…`), that file has changed only by three typo fixes in §3
  and one figure caption. arXiv v2 is dated 4 August 2019.
- The repository's compiled PDF of `a377700` has 68 pages, as v2 does.
  It numbers Theorem 1.3, (20)–(24), (71)–(74), Proposition 6.6 and
  Lemmas 8.4 and 8.5 exactly as the package cites v2.
- The statement of Theorem 1.3 agrees, constant by constant, with a
  WebFetch extraction of arXiv v2.

Byte identity with arXiv v2 (package hash `60d0d2d3…`) is not
established. A comparison against the v2 PDF would close it. The clones
were made in the session's cloud workspace and are not part of the
repository.

## 2. What the two suppliers import from Polymath [source]

| Item | Where | Content used | Used by |
| --- | --- | --- | --- |
| region, (14), (19) | Thm 1.3 | `0 < t ≤ 1/2`, `0 ≤ y ≤ 1`, `x ≥ 200`; `f_t = Σ_{n≤N} b_n n^{−s*} + γ Σ_{n≤N} n^y b_n n^{−s̄*−κ}`; `N = ⌊√(x/4π + t/16)⌋` | both |
| (20) | Thm 1.3, Prop 6.6(i) | `|γ| ≤ e^{0.02y}(x/4π)^{−y/2}` | both |
| (21) | Thm 1.3, Prop 6.6(ii) | `Re s* ≥ (1+y)/2 + (t/4) log(x/4π) − (t/2x²)(…)₊` | both, with `(…)₊ ≤ 1` |
| (22) | Prop 6.6(iii) | `|κ| ≤ ty/(2(x − 6))` | both |
| (71)–(72) | §6 | `e_A = |γ| Σ n^y b_n n^{−Re s* − Re κ} ε_{t,n}(s₋)`, `e_B = Σ b_n n^{−Re s*} ε_{t,n}(s₊)` | tail |
| bound on `ε_{t,n}` | proof of 6.6(iv)–(v) | `ε_{t,n} ≤ exp(((t²/16) log²(x/4πn²) + 0.626)/(x − 6.66)) − 1` | both |
| (23) | Thm 1.3 = 6.6(iv)+(v) | the same, with `N^{|κ|}` outside the sum | `E_max` |
| 6.6(vi) and weld | §6, `ERROR_CONSTANT_WELD.md` | `e_{C,0} ≤ (x/4π)^{−(1+y)/4} exp(−(t/16)L² + 1.24(3^y+3^{−y})/(N − 0.125) + (3|L + iπ/2| + 10.50)/(x − 12))`, `L = log(x/4π)` | both |
| Lemma 8.2 | §8.3 | endpoint cap: `Σ_{n≤N} b_n n^{−σ} ≤ Σ_{n≤N₀} + max(E(N₀), E(N)) log(N/N₀)` when `σ > (t/2) log N` | tail Lemma 3.1 (a restriction); `E_max` U3 |

The `n^{−Re κ} ≤ n^{|κ|}` step from (71), and the inequality
`4π/x ≤ x/(4πn²) ≤ x/4π` for `n ≤ N`, are in the paper's proof of 6.6.
The second gives `log²(x/4πn²) ≤ log²(x/4π)`. The weld follows from
6.6(vi) by `1 + u ≤ e^u` and `1/(x − 8.52) ≤ 1/(x − 12)`, with
`3.58 + 6.92 = 21/2` exactly **[checked]**.

Two displayed bounds differ from what their written proofs give.

- **(21) against Proposition 6.6(ii).**
  - (21) displays `4y(1+y)/x²` inside the positive part, while the proof
    of 6.6(ii) yields `8y(1−y)/x²`. The identity behind the proof is
    correct **[checked]**:
    `(1+y)/A − 2(1−y)/B = −(1−3y)/A − 8y(1−y)/(AB)`, with
    `A = (1+y)² + x²`, `B = (1−y)² + x²`.
  - For `y < 1/3` the displayed form subtracts less than the proof does,
    so it does not follow from the proof as written. It is nevertheless
    true **[proved here]**. The proof discards
    `(1/4) log(1 + (1+y)²/x²)`, which is at least of order `1/(4x²)`.
    The discrepancy between the two forms is only `O(x⁻⁴)`.
  - Both lanes bound the positive part by 1, which holds for `x² ≥ 8/3`
    in either form. Neither form enters their numbers.
- **(24) against Proposition 6.6(vi).**
  - (24) displays `10.44`. The route stated after 6.6, namely
    `1 + u ≤ e^u` followed by `1/(x − 8.52) ≤ 1/(x − 12)`, gives
    `10.50`.
  - Even keeping `1/(x − 8.52)`, that route yields `10.44` only for
    `x ≤ 1030.1`. At `x ≈ 6·10¹²` the shortfall is a relative
    `10⁻¹⁴` **[proved here]**.
  - (24) is nevertheless true on the whole region **[proved here]**.
    - Keeping the factor `1 + u` instead of `e^u` gains
      `u − log(1 + u)`.
    - Here `u ≥ 2.48/(N − 0.125) ≈ 8.8/√x`, so the gain is of order
      `38/x` or more.
    - The deficit is below `0.06/(x − 12)`.
    - At `x ≈ 6·10¹²` the gain is `6.4·10⁻¹²` against a deficit of
      `10⁻¹⁴`.
  - So, as with (21), the display is true but does not follow by its
    written route. The package uses `10.50` throughout, as
    `ERROR_CONSTANT_WELD.md` records.

The paper's own proof of Proposition 8.1 writes `6.92/(x − 6.66)` where
6.6(vi) has `6.92/(x − 12)`. The package does not use that proof.

## 3. The tail lemma

**Statement** (`TAIL_LEMMA.md` §1). For every `t ∈ I_t = [129/800,
161250001/10⁹]`, every `y ∈ [y0, √(1 − 2t)]` and every
`x ≥ X_{N*}(t) = 4π(N*² − t/16)` with `N* = 3840000`:
`|f_t(x+iy)| > e_A + e_B + e_{C,0}`. The mollifier is the eleven-term
vector `P1113` on `S = {1,2,3,4,5,6,7,10,11,13,14}`. The exact head is
`M = 153814` and the error head is `M_err = 3000`.

### 3.1 The partition (4.3) is exact [proved here; certified computation]

Let `T = {(d,k) : d ∈ S, 1 ≤ k ≤ N}`. Then
`M_λ(s*)F_B = Σ_T λ_d b_t(k)(dk)^{−s*}`. Split `T` by `dk ≤ M` and
`dk > M`.

- **The pairs with `dk ≤ M`.** If `m ≤ M` and `d | m`, then
  `m/d ≤ M < N* ≤ N`. So these pairs are exactly `{(d, m/d) : m ≤ M,
  d | m}`, and they contribute `1 + Σ_{m=2}^M c_m m^{−s*}`, since
  `c_1 = λ_1 b_t(1) = 1`.
- **The pairs with `dk > M`.** For an integer `k`, `dk > M` holds if
  and only if `k > ⌊M/d⌋`. So these pairs form
  `⋃_d {d} × (⌊M/d⌋, N]`.
- **Disjointness.** Each pair belongs to exactly one block.

The self-test of the checker verifies the identity coefficient by
coefficient, in exact integer arithmetic with random integer weights.
The cases are `(M, N) = (500, 2000)`, `(153, 154)`, `(997, 5000)` and
`(14, 15)`.

### 3.2 `OV` is redundant [proved here]

By (4.3), `|M_λ F_B − 1| ≤ P + TR`, where each routed sum over
`(⌊M/d⌋, N]` is bounded by one cap. Nothing else remains. For `d > 1`,
the `OV` cap covers `k ∈ [N/(d+1), N]`. That range lies inside
`(⌊M/d⌋, N]`, since `⌊M/d⌋ ≤ N/(d+1)` for every `d ∈ S∖{1}` (exact
check). So `OV` bounds part of the routed remainder a second time.

The package says so itself, in `TAIL_LEMMA.md` §4 and in the comment
"OV is redundant nonnegative padding" in `verify_tail_arb.c`
(l. 538–566). The term is a remnant of the deposited second-line
engine, whose header calls it a "real-endpoint overshoot device"
**[read]**.

This answers questions 2 and 3 under Priority 6 of
`OPEN_REVIEW_QUESTIONS.md`:

- (4.3) is a disjoint and exhaustive partition.
- `OV` is optional padding. It is neither missing from the identity nor
  needed by it.

The moving-cap argument for `OV` (question 5) is valid, but it is not
needed.

### 3.3 The frozen bounds (2.1) [checked]

In the window of `N`, `N² − t/16 ≤ x/4π`. From this:

- **`|γ|`.** (20) gives `|γ| ≤ G`.
- **`Re s*`.** Bound the positive part in (21) by 1. Then
  `(t/4) log(x/4π) ≥ (t/2) log N − (t/4)(−log(1 − t/(16N²)))` gives
  `Re s* ≥ σ1`. Both parts of `δ(N,t)` decrease in `N`, so
  `δ(N,t) ≤ δ(N*, t) ≤ δ̂`.
- **`|κ|`.** (22) with `y ≤ 1` gives `|κ| ≤ k̂`.
- **The `A` terms.** Then
  `|n^y b_t(n) n^{−s̄*−κ}| = b_t(n) n^{y − Re s* − Re κ} ≤ b_t(n) n^{−σ2}`,
  with `σ2 = σ1 − y − k̂`. This is (5.1).

### 3.4 The endpoint caps [checked]

Lemma 3.1 is Polymath's Lemma 8.2 applied on a subrange `(a, c]`:

- the summand decreases when `σ > (t/2) log c`;
- the sum is bounded by the integral;
- the exponent `(1 − σ)v + (t/4)v²` is convex, so the integrand is
  largest at an endpoint.

The validity condition does not depend on `N` for either exponent:
`σ1 − (t/2) log N = (1+y)/2 − δ̂` and
`σ2 − (t/2) log N = (1−y)/2 − δ̂ − k̂`. So the gates SC1 and SC2,
checked at `N*`, hold for every `N ≥ N*`. The caps are of four kinds:

- eleven `TR` caps, with `a = ⌊M/d⌋`;
- the `A` cap, with `a = M`;
- two error caps, with `a = 3000`, one for each `σ`;
- the moving `OV` caps.

### 3.5 All `N ≥ N*`; one thin gate [checked; proved here]

Put `q = log N`. For a cap with fixed left end `a`, the two candidates,
each multiplied by the width `q − log a`, have the logarithmic
derivatives (6.2) and (6.3). For the right endpoint the `(t/2)q` terms
cancel, so `d/dq log E(N) = 1 − σ`. Both derivatives are negative under
(6.4) and (6.5). The left sides of (6.4) and (6.5) increase with `q`,
so a gate that holds at `N*` holds for all `N ≥ N*` **[checked]**.

Lower bounds of the gate values **[certified computation]**:

| Cap | gate (6.4) | gate (6.5) | exponent used |
| --- | ---: | ---: | --- |
| `TR`, `d = 1, …, 14` | `≥ 3.098` | `≥ 2.625` | `σ1` at `y_lo` |
| `A` cap, `a = M` | `3.098` | **`1.0000013`** on the extended hull; `2.0229` on the box | `σ2` at the top of the hull or box |
| error caps, `a = 3000` | `4.618` | `5.838` (`σ1`), `2.224` (`σ2`) | extended hull |
| `OV` moving caps | — | `σ1 > 1` | — |

The `A`-cap gate on the extended hull has margin `1.29·10⁻⁶` on the
exact hull (Arb, whose `y`-ball is slightly wider: `1.28·10⁻⁶`). At
`M + 1 = 153815` it fails (`0.99999927`). So the package's head is the
largest for which its own gate holds.

The gate is not load-bearing **[proved here]**.

- **The lemma's order.** `TAIL_LEMMA.md` applies the `N`-reduction
  (§6) at every `y` in the range and then the `y`-reduction (§7) at
  `N*`. That order needs (6.5) at the top of the range.
- **The reverse order also works.** Fix `N ≥ N*`.
  1. For `y ≥ y_lo`, `D(N,t,y) ≤ D(N,t,y_lo)`, by the `y`-argument of
     §7. Its gate `YM` holds at every `N ≥ N*`, because its left side
     decreases in `N`.
  2. Then `D(N,t,y_lo) ≤ D(N*,t,y_lo)` needs (6.4) and (6.5) only at
     `y_lo ∈ I_box`. There the `A`-cap gate is `2.0229`.
- **Size of the head.** The box gate would admit heads up to
  `M = 782653`.
- **The error terms.** They are evaluated on the whole extended hull
  without a `y`-reduction, so they do need `N`-monotonicity there. Their
  gates, at least `2.22`, are comfortable.

The other `N`-directions hold as §§6 and 8 of the lemma state
**[checked]**: `P`, `M_max`, `G` (with
`d/dq log G = −yN²/(N² − t/16)`), the `A` head, `δ`, `k`, `Δ` (for
`L > 2`) and the `e_{C,0}` quotient.

### 3.6 The range of `y` and the interval of `t` [checked]

- **`B` side.** `∂σ1/∂y = 1/2`, and every `B`-side term, caps included,
  decreases in `σ1`, because `log u ≥ 0`.
- **`A` side.** For every head term and cap endpoint `u ≤ N`,
  `∂_y log(G·E_{σ2}(u)) = 0.02 − L_N/2 + (log u)/2 ≤ 0.02 − L_N/2 + (log N)/2`.
  The right side is `−7.56` at `N*` (gate `YM`) and decreases in `N`.
  The width `log(N/M)` does not depend on `y`.
- **Hulls.** `I_box` contains `y0`, and the top of the extended hull is
  at least `√(1 − 2t0)`. Both are exact integer checks.
- **`t`.** No monotonicity in `t` is used. Every quantity is evaluated
  on a hull of the closed `t`-box. The package's Arb hull is
  `[t_lo − 2.3·10⁻¹⁸, t_hi + 2.3·10⁻¹⁸]`, a superset **[replay]**.

### 3.7 The error terms [checked]

- **`e_A + e_B`.** (8.2) follows from (71)–(72) term by term, using
  `n^{−Re κ} ≤ n^{k̂}`, the bound on `ε_{t,n}` and
  `log²(x/4πn²) ≤ log²(x/4π)` from §2. The quantity `Δ` decreases in `x`
  for `L > 2`, and in `N`.
- **`e_{C,0}`.** It uses the weld. Its exponent is largest at the
  window's left edge and decreases in `N`, since
  `Q'(x)(x − 12) < 3 < 10.50 ≤ Q` for `Q = 3|L + iπ/2| + 10.50`.
- **Values.** `e_A + e_B ≤ 4.94·10⁻¹³` and `e_{C,0} ≤ 1.16711·10⁻⁸`.

### 3.8 Conclusion of the lemma, and `B_t ≠ 0` [checked; proved here]

`|M_λ f − 1| ≤ D < 1` implies `M_λ f ≠ 0`, hence
`|f| ≥ (1 − D)/|M_λ| ≥ (1 − D)/M_max`. Theorem 1.3 then gives
`|H_t/B_t| ≥ |f| − err > 0`.

`B_t ≠ 0` **[proved here]**:

- `B_t(x+iy) = M_t(s₊) = exp((t/4)α(s₊)²)·M_0(s₊)`.
- By its definition (6), `M_0` maps `C∖(−∞, 1]` into `C∖{0}`: it is a
  product of nonvanishing factors there.
- `s₊ = (1 + y − ix)/2` lies in that domain, because `Im s₊ = −x/2 ≠ 0`.

So `B_t ≠ 0` for every real `t`, including `t = 0`, and every real `y`.
This also settles the prose import "`B_t ≠ 0` on the barrier box"
(Priority 2, question 8), for `[X, X+1] × [0.1809, 1]`.

### 3.9 Proof-to-code map [checked]

Line numbers refer to `verify_tail_arb.c`.

| Lemma item | Code | Agrees |
| --- | --- | :---: |
| exact target, hulls, `λ` vector | `exact_hull_checks` (l. 235–262), reports at l. 344–363 | yes |
| `δ̂`, `k̂`, `σ1`, `σ2` on the box and the extended hull | l. 398–439 (lower points taken over the hull) | yes |
| SC1–SC3 | l. 441–450 (threshold uses `t_hi`) | yes |
| `b_t`, exact convolution `c_m` | l. 463–489 (`m = 1` skipped; `k = 1` uses `λ_d`) | yes |
| `P` | l. 491–502 | yes |
| `TR` and GN-TR | l. 504–536 (`a = ⌊M/d⌋`; gate (6.4) with `t_lo`, (6.5) with `σ1` at `y_lo`) | yes |
| `OV` and OVW | l. 538–566 | yes |
| `M_max`, `G`, `A` head and cap, GN-AB | l. 568–620 | yes |
| `D`, flow | l. 622–630 | yes |
| `YM` | l. 632–652 (two equivalent forms) | yes |
| `Δ`, error heads and caps, `G_err`, `e_A + e_B` | l. 654–709 | yes |
| GN-error | l. 711–723 | yes |
| `e_{C,0}` with `10.50` | l. 725–764 | yes |
| `Δ` and `e_{C,0}` monotonicity signs | l. 771–782 | yes |
| decisive `D < 1` and flow `> err` | l. 801–809 | yes |

The decimal corridors (l. 789–807) are regression tests only. The
theorem uses the strict Arb comparisons, as the lemma says.

## 4. The uniform finite-lane budget `E_max`

### 4.1 Statement [read]

`PROOF_NOTE.md` §§4.4–4.5 (Proposition 4.10) states the bound for every
window `N ≥ N0 = 690988`, hence every `x ≥ x_*`, every
`y ∈ [y0, y_max]` with `y_max = √(1 − 2t0)`, and every
`t ∈ [129/800, 161250001/10⁹]`:

```
e_A + e_B ≤ 2.06·10⁻¹²,   e_{C,0} ≤ 2.33492848·10⁻⁷,   E_max ≤ 2.33494905212337849·10⁻⁷.
```

The reduction is stated as U1–U5 in
`provenance/RECORD_BINDING.upstream.md` §3 and implemented in
`verify_prop410_arb.c`.

### 4.2 U1–U5 [checked]

- **U1.** The exponent of `ε` is at most
  `u1(x) = ((t²/16)L² + 0.626)/(x − 6.66)`, uniformly in `n`, by §2.
  `u1` decreases in `x` for `L > 2`, since its derivative has numerator
  below `−(t²/16)L(L − 2) − 0.626`. It is evaluated at
  `x0 = X_{N0}(t)`; since `x_* ∈ W_690988`, every `x` of the lane
  satisfies `x ≥ x0`.
- **U2.**
  `|γ|N^{|κ|}n^y ≤ e^{0.02y}(1 − t/(16N²))^{−y/2} e^{|κ| log N} ≤ e^{0.02}(1 − t/(16N0²))^{−1/2} exp(t log N0/(2(X_{N0} − 6)))`.
  This uses `n ≤ N`, `y ≤ 1`, `x/4π ≥ N² − t/16`, and the decrease in
  `N` of `t/(16N²)` and of `log N/(X_N − 6)`; the latter holds for
  `log N > 1/2`.
- **U3.**
  `Σ_{n≤N} b_n n^{−Re s*} ≤ 1 + Σ_{n=2}^{2000} b_n n^{−σ1} + Cap(2000, N; σ1)`,
  with `σ1 = σ1(N0, y0)`; `σ1` increases in both `N` and `y`.
  - Validity: `(1 + y0)/2 − δ1 > 0`, which does not depend on `N`.
  - All-`N` gates: `g_t1 = −0.4417` and `g_t2 = −0.5066` at `N0`. Both
    decrease in `N`.
- **The product.** By (23), the sum runs over `n ≤ N` with prefactor
  `1 + |γ|N^{|κ|}n^y`. Hence `e_A + e_B ≤ P_max·S_max·(e^{u1} − 1)`.
- **U4–U5.** The factors of `e_{C,0}` are maximized separately:
  - `−(1+y)L/4` at `(y0, L0)`;
  - `−(t/16)L²` at `(t_lo, L0)`;
  - the `1.24` term at `(y_max, N0)`, since `3^y + 3^{−y}` increases for
    `y > 0`;
  - the last quotient at `x0`, as in §3.7.

No per-window budget remains, and the bound continues past `N = 3840000`.
The gate `G0` (`8/x0² < 3y0`) is not used by the argument, because the
positive part is bounded by 1. It is harmless.

### 4.3 Proof-to-code map [checked]

Line numbers refer to `verify_prop410_arb.c`.

| Quantity | Code | Agrees |
| --- | --- | :---: |
| `δ1`, `σ1`, `Y1`, `κ` | l. 291–325 | yes |
| twelve domain and sign gates | l. 327–371 | yes |
| U1max | l. 372–383 | yes |
| `P_max` | l. 385–400 | yes |
| head (`t_hi` in the quadratic term, `σ1_lo` in the linear one) | l. 402–428 | yes |
| caps at `m0` and `N0`, `S_max` | l. 430–463 | yes |
| `e_A + e_B`, `e_{C,0}`, `E_max` | l. 465–527 | yes |
| decisive comparisons against exact rationals | l. 539–556 | yes |

### 4.4 Values [certified computation]

```
e_A + e_B ≤ 2.05702368866608683·10⁻¹²,  e_{C,0} ≤ 2.33492848188649183·10⁻⁷,
E_max ≤ 2.33494905212337848766·10⁻⁷  (< the package's 2.33494905212337849·10⁻⁷).
```

With the certified floor of note 3:

```
L_690988 − E_max ≥ 5.5787184·10⁻⁷,   L_690988 / E_max ≥ 3.3892.
```

## 5. The computations

### 5.1 Standard-library recomputation [certified computation]

The programme is
[`check_tail_and_uniform_error_budget.py`](../numerics/check_tail_and_uniform_error_budget.py),
and its record is
[`TAIL_AND_UNIFORM_ERROR_BUDGET_RECORD_20261012.json`](../numerics/TAIL_AND_UNIFORM_ERROR_BUDGET_RECORD_20261012.json).

**Method.**

- *Arithmetic.* `decimal` at 50 digits. `+ − × /` use directed
  rounding. `exp`, `ln` and `sqrt` are correctly rounded and padded by a
  relative `10⁻⁴⁸`.
- *Constants.* `π` is enclosed by Machin's formula in exact rationals.
  For the cutoff correction, `−log(1 − z) ≤ z/(1 − z)` replaces an
  evaluated logarithm.
- *Coefficients.* The 153,814 convolution coefficients are enclosed as
  intervals over the `t`-box, from monotone endpoint values of
  `b_t(k)`.
- *Hulls.* The decorrelated hulls follow the lemma. Every enclosure is
  a valid bound on its own.
- *Self-test.* The exact partition test of §3.1, `π`, 2,000 random
  `exp`, `ln` and `sqrt` enclosures checked against 100-digit values,
  and a floating sanity check of the endpoint cap.

**Runtime and reproducibility.** The run takes 55 s in the cloud
container (x86-64, Python 3.13.16) and 15 s on Teddy's machine (aarch64
Linux VM, Python 3.10.12). Gates and results are identical on the two.

**Results.** All 54 gates pass (31 for the tail, 23 for `E_max`), and so
does the self-test. Comparison with the Arb transcripts:

| Quantity | package (Arb) | this programme | relative difference |
| --- | --- | --- | ---: |
| `P` | `0.17022802367812` | `0.17022802367730` | `−4.8·10⁻¹²` |
| `TR` | `0.26290133012479` | `0.26290133012467` | `−4.6·10⁻¹³` |
| `OV` | `0.03924268121018` | `0.03924268121016` | `−4.6·10⁻¹³` |
| `M_max` | `1.60828914495414` | `1.60828914495414` | `−7.7·10⁻¹⁷` |
| `AB` | `0.32789431927099` | `0.32789431926611` | `−1.5·10⁻¹¹` |
| `D` | `0.99972090938875` | `0.99972090937994` | `−8.8·10⁻¹²` |
| flow `(1 − D)/M_max` | `1.7353260894·10⁻⁴` | `1.7353261442·10⁻⁴` | `+3.2·10⁻⁸` |
| tail `e_A + e_B` | `4.9380792·10⁻¹³` | `4.9380788·10⁻¹³` | `−8.0·10⁻⁸` |
| tail `e_{C,0}` | `1.16711096·10⁻⁸` | `1.16711088·10⁻⁸` | `−7.2·10⁻⁸` |
| `D'` (no `OV`) | — | `0.96047822816978` | — |
| flow' (no `OV`) | — | `0.0245737975` | — |
| `E_max` | `2.33494905212337849·10⁻⁷` | `2.33494905212337849·10⁻⁷` | `−5.5·10⁻¹⁹` |

Every upper bound here lies below the package's, and every lower bound
above it. The differences come from the package's ball arithmetic:

- Arb inflates the radius of `exp` on wide balls. For `b_t(k)` the
  radius is `2.7·10⁻⁵` relative above `e^m(e^r − 1)`.
- The union balls for `y` are about `2.5·10⁻⁹` wider than the exact
  hulls.

These come from instrumented runs of the package's code.

Both programmes exceed the per-coefficient endpoint maximum
`Σ_m max(|c_m(t_lo)|, |c_m(t_hi)|) m^{−σ1_lo}` by about `1.7·10⁻⁹`.
That excess is the decorrelation of the coefficient intervals; it was
checked against an exact evaluation at both endpoints.

### 5.2 Rebuild of the package's Arb verifiers [replay]

**Build.**

- Environment: an Ubuntu 24.04 container (x86-64) with gcc 13.3.0 and
  libflint-dev 3.0.1. These are the versions of the package's review
  container, on different hardware.
- Flags: `-O2 -std=c17 -Wall -Wextra -Werror -pedantic`.

**Result.**

- The four transcripts `tail_arb_{256,512}.log` and
  `prop410_arb_{256,512}.log` are byte-identical to the sealed ones.
- 255 bits is refused.

Because the toolchain versions match, this is a reproduction, not an
independent toolchain. The package's own macOS corroboration used Apple
clang and FLINT 3.6.0.

**Instrumented copy.** An instrumented copy printed the gate values of
§3.5. It also printed `D' = 0.96047822817857258920` in Arb.

## 6. Tolerances, updated

Each row gives how wrong one supplier's own derivation would have to be,
with the others held fixed, for the certificate to fail.

| Supplier | Breaks if | Tolerance | Audit status |
| --- | --- | --- | --- |
| Finite floor, `N = 690988` | the triangle mass `S_N` is low by `9.85·10⁻⁷` | relative `1.1·10⁻⁶` | 32 rows certified (note 3); remaining coverage from the package's regeneration |
| Tail contraction | `D' = P + TR + M_max·AB` reaches 1 | reserve `0.0395`: `P` low by 23 %, `TR` by 15 %, `M_max·AB` by 7.5 % | audited (this note) |
| Tail error | `err` exceeds `(1 − D')/M_max` | `×2.1·10⁶` | audited (this note) |
| `E_max` | `E_max` exceeds `L_690988` | `×3.39` | audited (this note) |
| Barrier `D_z, D_t` (Lemma 8.4) | the margin of prism 882 is consumed | both `×1.497`; `D_z` alone `×1.988`; `D_t` alone `×2` | not audited |
| Barrier approximation error | the error exceeds the allowance `0.00125` plus the margin of prism 882 | `×1.46·10³` against the actual `3.565·10⁻⁴` | transcription only (note 1) |

The README's figures "`400×`" and "`10⁴×`" measure approximation
allowances only. Among the unaudited suppliers, the barrier's derivative
majorants are now the least tolerant.

## 7. What this establishes and what remains

**Established.** Within the stated tools:

- the tail lemma's partition, caps, all-`N`, `y`, `t` and error
  reductions;
- the uniform budget's U1–U5;
- the proof-to-code maps of both Arb programs;
- independent recomputation of every decisive inequality, and byte
  replay of the sealed transcripts.

With notes 1–3, every analytic link of hypothesis (ii) has now been read
and checked, and its decisive inequalities recomputed independently.

**Not established.**

- The correctness of Polymath Theorems 1.2–1.3 and Lemma 8.2, and of
  Platt–Trudgian (imports).
- The producer's amortized computation of the 3,148,981 rows that were
  not recomputed. The package's own regeneration used the same code.
- The barrier, hypothesis (iii).
- Byte identity of the Polymath source read here with arXiv v2 (§1).

**Next (B2).** The barrier:

- the Lemma 8.4 majorants (the 16-term head and the integral tail);
- the endpoint-separated factors of `DERIVATIVE_BOX_LEMMA.md`;
- the prism gate and the spatial term `D_z/(2(num − 1))`;
- the `t → 0` extension.

Lemma 8.4 is in §8.4 of the TeX source, so no PDF is needed. `B_t ≠ 0`
is settled by §3.8 above.
