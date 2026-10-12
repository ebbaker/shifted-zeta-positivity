# Finite-lane replay and the corrected-interface benchmark

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: Claude Fable 5.1 (`claude-fable-5-1`), Cowork session. Internal
LLM-assisted computation and reasoning, not independent validation. The
replays are float64 or 50-digit decimal point evaluations with no error
bounds; the certified numbers are the package's own FLINT/Arb enclosures.

Companion: [dependency ledger](1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md);
records in [numerics/](../numerics/README.md).

## 1. The difficult cells

The portfolio README asked for 20–50 difficult cells of one pinned
certificate. In the pinned package the only cells whose margin is of the
same order as the approximation error are the first rows of the finite
final-time lane (`N = 690988, 690989, …`), where the certified floor is
`T_N ≈ 7.9·10^{−7}` to `3.6·10^{−6}` against an error budget of
`2.33·10^{−7}`. Every barrier prism has margin at least `0.5198` against an
allowance of `0.00125`, and the tail has `1.7·10^{−4}` against
`1.2·10^{−8}`. The difficult cells are therefore the first finite rows,
and the benchmark question is what a smaller error budget buys there.

## 2. Replay of the stored rows

**[replay, float64]** With the formulas of `NATIVE_BINDING.md` and
`src/lemma_sweep_p235711.c` (plain triangle weight):

| `N` | leg (primes) | stored floor | replay `L_N` | first row of its producer run |
| ---: | --- | ---: | ---: | --- |
| 690988 | P11 | 0.000000791366 | 7.913667e-7 | yes — agrees to the six stored digits |
| 690989 | P11 | 0.000000974062 | 9.740621e-7 | yes — agrees |
| 690990 | P11 | 0.000001570095 | 1.622941e-6 | no — stored is lower (frozen weights) |
| 690991 | P11 | 0.000001891132 | 1.891133e-6 | yes — agrees |
| 690995 | P11 | 0.000003354765 | 3.566147e-6 | no — stored is lower |
| 728999 | P11 | 0.014771594320 | 1.530793e-2 | no — stored is lower |
| 729000 | P7 | 0.000315112459 | 3.151688e-4 | yes (`t`-box of width `10^{−9}`) — stored lower by `5.6·10^{−8}` |
| 819000 | P5 | 0.000305788807 | 3.058440e-4 | yes — stored lower by `5.5·10^{−8}` |
| 1028000 | P23 | 0.000309285478 | 3.093387e-4 | yes — stored lower by `5.3·10^{−8}` |
| 3840000 | P23 | 0.299655457299 | 3.019001e-1 | no — stored is lower |

The sign of every discrepancy is the conservative one. The first-row
agreements show that the stored lane is the stated formula. The later-leg
first rows are lower than the point replay by `5·10^{−8}`, consistent with
the producer's `t`-box `[0.16125, 0.161250001]` (slope `∂L/∂t ≈ 19`, see
below, gives `1.9·10^{−8}`) plus ball widening. The weakest-row components
are `g = 0.080920`, `σ = 1.677710`, `M = 1.765097`, `Σ = 0.919078`,
`κ = 2.5·10^{−15}`, correction `1.1·10^{−14}`; so `1 − g − Σ = 1.40·10^{−6}`
and the row is balanced to one part in `10^{6}`.

## 3. Sensitivities at the weakest row

**[replay, float64, central differences with step `10^{−4}`]**

```
∂L/∂(y^2) = 9.528   per unit y^2,       ∂L/∂t = 19.058   per unit t.
```

Thus the certified slack `T_min − E_max = 5.58·10^{−7}` corresponds to
`Δ(y_0^2) = 5.9·10^{−8}` or `Δt_0 = 2.9·10^{−8}`: the published row is
within `3·10^{−8}` of this lane's feasibility boundary at the stated
budget. Along the row the trade between `t_0` and `y_0^2` is almost
neutral for `Λ = t_0 + y_0^2/2` (`∂Λ/∂(y^2)` at fixed `L` is
`1/2 − 9.528/19.058 = 0.0001`), so the row sits where the two parameters
are interchangeable to first order.

## 4. The corrected budget and its maximal effect

**[replay, decimal]** At the first window, `(x_{690988}, y_0, t_0)`:

| Budget | value |
| --- | ---: |
| `e_A + e_B` (Theorem 1.3 (23), all `N` terms) | `8.04·10^{−13}` (Arb directed: `2.06·10^{−12}`) |
| `e_{C,0}` (Section 6, `C` dropped) | `2.334925·10^{−7}` (Arb directed: `2.334928·10^{−7}`) |
| `e_C` (Section 6, `C` retained) | `8.56·10^{−13}` |
| `e_C / e_{C,0}` | `3.66·10^{−6}` |
| dropped-`C` budget | `2.33493·10^{−7}` |
| retained-`C` budget | `1.66·10^{−12}` |

If the whole difference `2.335·10^{−7}` could be returned to the row as
slack, the slopes of §3 convert it to

```
Δ(y_0^2) ≤ 2.45·10^{−8}   ⇒  ΔΛ ≤ 1.23·10^{−8}      (via y_0),
Δt_0    ≤ 1.23·10^{−8}   ⇒  ΔΛ ≤ 1.23·10^{−8}      (via t_0).
```

That is the eighth decimal of `0.1787854`. And it cannot be returned at
all, for the structural reason in the ledger (§4 there): the lane bounds
`|f_t|` uniformly over a window of length `≈ 1.7·10^{7}` by a triangle
inequality on coefficients; the oscillating term `C_t/B_t` can enter a
uniform bound only through its supremum, which is `e_{C,0}` up to the
factor `1 + s`, `s = 3.7·10^{−6}`. The corrected interface is a pointwise
and derivative statement on disks; it has no uniform-in-`x` form.

On the barrier the correction *is* applicable (pointwise mesh evaluation,
with the Note 20–22 derivative bounds standing in for the correction's
contribution to `D_z, D_t`), but the allowance it would shrink is
`0.07–0.24 %` of every prism's margin. The mesh density is set by
`D_z/(2(num−1)) ≈ 0.5` and the time steps by `D_t Δt ≈ 0.4–1.9`, both
properties of the finite sum. No prism, mesh count or time step changes.

**Conclusion of the benchmark.** For this certificate class (uniform
triangle lane for hypothesis (ii), prism barrier for (iii) with margins
two to three orders above the allowance), the corrected Riemann–Siegel
interface changes neither feasibility nor cost, and could move the bound by
at most `≈10^{−8}` even under the false assumption that it applies in the
uniform lane. This is the README's stop condition for a record-bound
campaign ("finite-sum cancellation dominates and the correction changes
neither feasibility nor cost"), and it is met with a wide margin.

## 5. An observation outside the benchmark: the weight, not the error, is the lever

**[replay, float64; observation, not a result]** The producer source of
the package has a second weight, `WEIGHT SHARP`, which is the Polymath
Section 8.5 "improved triangle inequality"
`max(|B − gA|, ((1−g)/(1+g))|B + gA|)` (proved there for real
coefficients by the cosine-rule argument; the package's `A_{N,n}, B_{N,n}`
are real). Every stored row uses the plain weight `|B| + g|A|`. At the
certified row the sharp weight gives

```
L_sharp(690988; t_0, y_0^2) = 0.0770        versus   L_plain = 7.9·10^{−7},
```

and the scan

| `t` | `y^2` | `L_sharp` |
| ---: | ---: | ---: |
| 0.16125 | 0.0350708 | +0.0770 |
| 0.15 | 0.0350708 | −0.148 |
| 0.13 | 0.0350708 | −0.844 |
| 0.11 | 0.0350708 | −2.28 |
| 0.16125 | 0.020 | −0.0223 |
| 0.16125 | 0.010 | −0.0930 |
| 0.11 | 0.010 | −2.82 |

places the sharp lane's feasibility boundary near `t ≈ 0.157` at the
certified `y_0`, or near `y_0^2 ≈ 0.023` at the certified `t_0`. The lane
is a cliff in `t` (`Σ` grows from `0.78` to `14` between `t = 0.16125` and
`0.09` because `σ − (t/4)\log n` approaches `1` at `n ≈ N`), so the
`10^{5}`-fold larger `L` converts to only `ΔΛ ≈ 0.004–0.006`. Still, that
is `10^{5}` times the maximal effect of the corrected error budget, and it
is available at the same verification height with no new theorem beyond
the published lemma — *provided* the package's `y`-transfer (Dini) and
window-freeze arguments are re-proved for the sharp weight, which is not
automatic because the sharp weight is a maximum of two signed combinations.
Whether the larger public claims (`< 0.158`, `< 0.149`) come from this
lever, from larger mollifiers, or from a different lower-bound method was
not examined.

This observation is recorded because it answers the portfolio's question
"where is the actual bottleneck of a public certificate" more precisely
than the benchmark alone; it is not a claim of a new bound and nothing
here certifies the sharp-weight values.

## 6. Decision

- **Stop** the corrected-interface campaign as a route to a better `Λ`
  certificate of this class. The benchmark deliverable is complete in the
  negative: measured effect `≤ 1.2·10^{−8}`, and structurally zero in the
  uniform lane.
- **Continue, if at all, as audit only**: the remaining obligations in the
  ledger (§6 there) are the Dini `y`-transfer, the window freeze, the
  Lemma 8.4 majorants, the tail gates and a rigorous interval replay of
  the first row. A rigorous interval replay of `L_{690988}` (Arb or a
  standard-library rational/`decimal` directed implementation of the
  `1.6·10^{9}`-term sum) is the one computation that would upgrade §2 from
  corroboration to an independent certificate of the weakest row.
- **Do not** pursue a sharp-weight parameter campaign inside this
  investigation without first deciding whether a fourth unreviewed
  `Λ` number is wanted at all (the cross-assessment's position was that it
  is not); if it is, the first task is the `y`-transfer proof for the sharp
  weight, not more rows.
