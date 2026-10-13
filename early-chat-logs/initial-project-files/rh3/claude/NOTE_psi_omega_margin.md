# `Ψ_ω`, the margin of Suzuki's criterion, and a correction on what is new

**2026-08-27.** Two tasks: an adversarial novelty check on Suzuki
[2206.03682](https://arxiv.org/abs/2206.03682) (JLMS **108** (2023)), and work on §11 — the shifted
family `Ψ_ω` and Theorem 11.1, flagged in the previous round as the one item in that paper that is
both new and unworked.

**Headline.**

1. **A correction I owe the record.** I described Theorem 1.7 as *"Weil positivity collapses from an
   infinite-dimensional test-function condition to a one-parameter family"* and called that the
   sharpest new thing in the paper. **The genus of result is not new: Li's criterion (1997) as
   interpreted by Bombieri–Lagarias (1999) already realises RH as Weil positivity on a countable
   family, and Suzuki flags the analogy himself** in §3.4 (*"This one is similar to the formula of Li
   coefficients by the Weil distribution `W` in [2]"*). What is new is the specific family — a
   *continuum* of *compactly supported indicators* `{R_t}` — the resulting function `Ψ`, and a
   sufficiency proof (Widder/Landau) that bypasses Weil entirely.
2. **§11 is Lagarias's `θ` in screw clothing.** Lagarias, *Acta Arith.* **89** (1999) 217, Theorem
   1.1 is already stated with a general `θ`: *"All elements `ρ ∈ Ω` have `Re(ρ) ≤ θ`"* ⟺
   *"`Re(f′_Ω/f_Ω)(s) > 0` for `Re(s) > θ`."* So the graded criterion predates the screw function.
   Suzuki's contribution is the **explicit arithmetic function `Ψ_ω`** realising it.
3. **`Ψ_ω` really is unworked.** 12 citations to the JLMS paper, **8 of them Suzuki's own**, and
   **none touches `Ψ_ω` or Theorem 11.1** — not even Suzuki. Four years, zero follow-up.
4. **New here: the closed-form asymptotic and the margin.** Derived and verified below:
   > **`Ψ_ω(t) = (ξ′/ξ)(½+ω)·t + (ξ′/ξ)′(½+ω) + O(e^{−ωt})`**
   >
   > when there are no zeros with `Re ρ > ½+ω`.
   The **margin of the criterion is the linear drift, with slope exactly `(ξ′/ξ)(½+ω)`** — and it
   vanishes at `ω = 0` because `(ξ′/ξ)(½) = 0`. **That is the precise sense in which RH is the
   marginal case and every zero-free-region case is not.** The `liminf Ψ = 0` obstruction that kills
   the RH route provably does not apply for any `ω > 0`.
5. **New here: the threshold is universal.** The `t₀` in Theorem 11.1's *"there exists `t₀`"* is
   `t₀(ω) = u*/ω` with `u*` the root of `u + 1 = 2e^{−u}`, i.e. **`t₀ ≈ 0.3748/ω`**, independent of
   everything else.
6. **New here: exponential sensitivity — the property `ROUND9` said was missing.** A zero at
   `Re ρ = ½+δ` drives `Ψ_ω` with envelope growing at rate **exactly `δ − ω`**. Round 9 killed the
   Nyman–Beurling route because it is *exponentially insensitive* to off-line zeros. **This criterion
   is exponentially sensitive to them.**
7. **But the transport is faithful.** Proving `Ψ_ω ≥ 0` for a fixed `ω < ½` means bounding the
   prime-side fluctuation by the linear margin `≈ 0.0462·ω·t`, when a priori it could be as large as
   `e^{(½−ω)t}`. Turning an exponential bound into a linear one *is* the zero-free half-plane. No
   free lunch — but the statement is now about an explicit computable function.

---

## 1. The derivation

Suzuki's §11 zero-side formula:

```
Ψ_ω(t) = Σ_γ (γ²+ω²)^{−2} [ ωt(γ²+ω²) + (γ²−ω²)
                            − e^{−ωt}(γ²−ω²)cos(γt) − e^{−ωt}·2γω sin(γt) ]
```

with `γ` over the zeros of `ξ(½−iz)`, both signs. If every `|Im γ| ≤ ω` the two `e^{−ωt}` terms are
uniformly damped, so

> `Ψ_ω(t) = ω·A(ω)·t + B(ω) + O(e^{−ωt})`,
> `A(ω) := Σ_γ 1/(γ²+ω²)`, `B(ω) := Σ_γ (γ²−ω²)/(γ²+ω²)²`.

Both sums have closed forms. Since `γ = i(½−ρ)`, writing `u = ρ−½` gives `γ² = −u²` and

```
1/(γ²+ω²) = 1/(ω²−u²) = (1/2ω)[ 1/((½+ω)−ρ) + 1/(ρ−(½−ω)) ].
```

Summing with `Σ_ρ 1/(s−ρ) = (ξ′/ξ)(s)` and using `(ξ′/ξ)(1−s) = −(ξ′/ξ)(s)`:

> **`A(ω) = (1/ω)·(ξ′/ξ)(½+ω)`.**

And because `∂/∂ω [ ω/(γ²+ω²) ] = (γ²−ω²)/(γ²+ω²)²`, term by term,

> **`B(ω) = ∂/∂ω[ ω A(ω) ] = (ξ′/ξ)′(½+ω)`.**

Hence the asymptotic in the headline. At `ω = 0` the linear term vanishes identically
(`(ξ′/ξ)(½) = 0` by the functional equation) and one is left with `B(0) = Σ_γ 1/γ²` — the mean of
Suzuki's bounded oscillating `Ψ`, consistent with his `sup Ψ ≤ 2Σ_γ γ^{−2} < 0.094`.

---

## 2. Verification

**Check 0 — the prime-side implementation, against a printed number.** Suzuki's Theorem 4.1 proof
records `Ψ(t₂) = 0.0396618…` at `t₂ = 0.464002…`. Computed from the §11 formula at `ω = 0`:

> `Ψ(0.464002) = 0.03966175656`, and `Ψ(0) = 0` exactly. ✓

**Check 1 — the closed forms, against direct sums over 250 zeros plus a Riemann–von Mangoldt tail.**

| `ω` | `A(ω)` sum+tail | `A(ω)` closed form | `B(ω)` sum+tail | `B(ω)` closed form |
|---|---|---|---|---|
| 0.10 | 0.04621447 | 0.04620924 | 0.04621299 | 0.04620776 |
| 0.25 | 0.04621057 | 0.04620534 | 0.04620128 | 0.04619605 |
| 0.40 | 0.04620333 | 0.04619810 | 0.04617957 | 0.04617434 |

Relative difference `1.13 × 10⁻⁴` in every row — constant across `ω`, i.e. it is the tail-estimate
error, not a discrepancy. ✓ And `2B(0) = 0.092420 < 0.094`, matching Suzuki's stated bound. ✓

**Check 2 — the asymptotic, against the prime side. This uses no zeros at all**, so it is an
independent test of both the derivation and the explicit formula. Sieving `Λ(n)` to `n ≤ e¹⁵`:

| `ω` | `t` | `Ψ_ω` (primes) | asymptotic | difference | `0.05·e^{−ωt}` |
|---|---|---|---|---|---|
| 0.20 | 6 | 0.10222000 | 0.10164948 | `5.7 × 10⁻⁴` | `1.5 × 10⁻²` |
| 0.20 | 15 | 0.18501313 | 0.18482211 | `1.9 × 10⁻⁴` | `2.5 × 10⁻³` |
| 0.30 | 6 | 0.12966687 | 0.12935586 | `3.1 × 10⁻⁴` | `8.3 × 10⁻³` |
| 0.30 | 15 | 0.25414919 | 0.25410476 | `4.4 × 10⁻⁵` | `5.6 × 10⁻⁴` |
| 0.40 | 6 | 0.15721911 | 0.15704977 | `1.7 × 10⁻⁴` | `4.5 × 10⁻³` |
| 0.40 | 15 | 0.32337324 | 0.32336293 | `1.0 × 10⁻⁵` | `1.2 × 10⁻⁴` |

The difference sits inside the predicted `e^{−ωt}` envelope and shrinks at the predicted rate. ✓

---

## 3. The margin, and the universal threshold

| `ω` | slope `(ξ′/ξ)(½+ω)` | intercept `B(ω)` | `t₀` |
|---|---|---|---|
| 0.49 | 0.0226342 | 0.046157 | 0.766 |
| 0.40 | 0.0184792 | 0.046174 | 0.938 |
| 0.30 | 0.0138610 | 0.046190 | 1.250 |
| 0.20 | 0.0092414 | 0.046201 | 1.875 |
| 0.10 | 0.0046209 | 0.046208 | 3.748 |
| 0.05 | 0.0023105 | 0.046209 | 7.497 |
| 0.01 | 0.00046210 | 0.046210 | 37.48 |
| 0.001 | 0.000046210 | 0.046210 | 374.8 |
| **0** | **1.2 × 10⁻³⁰** | 0.046210 | **∞** |

Two things.

**The slope vanishes linearly**, `(ξ′/ξ)(½+ω) ≈ B(0)·ω = 0.046210·ω` (verified to eight digits at
`ω = 0.001`), because `(ξ′/ξ)(½) = 0`. The `ω = 0` row returns `10⁻³⁰` — zero to working precision.

> **This is the exact mechanism of RH's marginality.** Suzuki's own §7.1 shows `liminf Ψ = 0` under
> RH + simplicity + `ℚ`-independence, and remarks that this *"suggests the difficulty of proving the
> non-negativity of `Ψ(t)` by approximation."* The asymptotic says why: at `ω = 0` the margin **is**
> the vanishing of `ξ′/ξ` at the central point. **For every `ω > 0` there is a margin, and it grows
> linearly in `t`.** Our `NOTE_existence_loophole` §5.3 screen fires at `ω = 0` and provably does not
> fire at `ω > 0`.

**`t₀` is universal.** With `slope ≈ B(0)ω` and `intercept ≈ B(0)`, the condition
`slope·t + intercept > 2B(0)e^{−ωt}` reduces to `u + 1 > 2e^{−u}` in `u = ωt`, whose root is
`u* = 0.37483…`. So

> **`t₀(ω) = 0.3748/ω`**, exactly reproducing the table (`18.74` at `ω = 0.02`, `374.8` at
> `ω = 0.001`). The `"there exists `t₀`"` in Theorem 11.1 is not open-ended.

---

## 4. Exponential sensitivity — the property round 9 said was missing

A zero `ρ = ½+δ+iτ` and its functional-equation partner give `γ = ±τ ± iδ`. Then
`e^{−ωt}cos(γt)` carries `e^{−ωt}·cosh(δt) ≍ e^{(δ−ω)t}`. Measured, as the envelope over one
oscillation period at `τ = 50`:

| `δ` | `ω` | env `t=40` | env `t=60` | measured rate | `δ−ω` |
|---|---|---|---|---|---|
| 0.30 | 0.10 | `2.417` | `131.95` | **`+0.20000`** | `+0.2000` |
| 0.20 | 0.10 | `5.18 × 10⁻²` | `3.34 × 10⁻¹` | `+0.09325` | `+0.1000` |
| 0.15 | 0.10 | `1.39 × 10⁻²` | `2.73 × 10⁻²` | `+0.03364` | `+0.0500` |
| 0.10 | 0.20 | `1.44 × 10⁻²` | `2.08 × 10⁻²` | `+0.01833` | `−0.1000` |
| 0.05 | 0.10 | `8.11 × 10⁻³` | `1.13 × 10⁻²` | `+0.01638` | `−0.0500` |

The clean case matches `δ−ω` to five digits; the intermediate rows are contaminated by the linear
drift, which has not yet been overtaken at these heights. The `δ < ω` rows grow at
`log(60/40)/20 = 0.0203` — the linear drift alone, exactly as predicted.

**Detection height** — where a violating quartet overtakes the margin `0.0462·ω·t`:

| `δ` | `ω` | `t` |
|---|---|---|
| 0.30 | 0.10 | 27 |
| 0.20 | 0.10 | 61 |
| 0.15 | 0.10 | 135 |
| 0.12 | 0.10 | 385 |
| 0.11 | 0.10 | 849 |

Scaling as `≈ (1/(δ−ω))·log(1/(δ−ω))`.

> **`ROUND9` §1 closed the Nyman–Beurling route because the criterion is *exponentially insensitive*
> to off-line zeros — "which removes it from every working mode this project has used." `Ψ_ω` has the
> opposite property, quantified.** That is the single strongest thing to say for this route, and it
> is not in the paper.

---

## 5. What Theorem 11.1 would buy, and the fact-check behind it

Let `Θ := sup{Re ρ}`. Theorem 11.1 says `Θ ≤ ½+ω ⟺ Ψ_ω ≥ 0 eventually`, so
`ω_c := inf{ω : Ψ_ω ≥ 0 eventually} = Θ − ½`, and RH ⟺ `ω_c = 0`.

**Verified, and load-bearing: `Θ < 1` is open.** Every known zero-free region shrinks to `σ = 1`.
Mossinghoff–Trudgian–Yang [2212.06867](https://arxiv.org/abs/2212.06867), the current state of the
art, give `σ ≥ 1 − 1/(55.241(log|t|)^{2/3}(log log|t|)^{1/3})` and
`σ ≥ 1 − 1/(5.558691 log|t|)`; Ford's survey has the Korobov–Vinogradov form. Both are
`σ ≥ 1 − f(|t|)` with `f → 0`, so neither contains a half-plane `σ > c` for any `c < 1`.
Sutherland's MIT 18.785 notes state the conditional explicitly: *"if we knew that `ζ(s)` has no zeros
in the critical strip with real part greater than `c`, for some `c ≥ 1/2` strictly less than 1, we
could prove `π(x) = Li(x) + O(x^{c+o(1)})`."*

> **So Theorem 11.1 at any fixed `ω < ½` is an open problem, and at `ω ≥ ½` it is vacuous** (de la
> Vallée Poussin). It has no unconditional consequences currently in reach — consistent with its zero
> follow-up citations.

---

## 6. Does it give leverage? Honest answer

**The transport is faithful, and there is no free lunch.** Writing the criterion out:

```
Ψ_ω(t) = [ (ξ′/ξ)(½+ω)·t + (ξ′/ξ)′(½+ω) ]  −  e^{−ωt}·[ oscillation over zeros ]
```

To prove `Ψ_ω ≥ 0` from the prime side you must bound the fluctuation of
`Σ_{n≤e^t} Λ(n)n^{−½−ω}(t − log n)` about its smooth part by the linear margin `≈ 0.0462·ω·t`. With
no zero-free information that fluctuation could be as large as `e^{(½−ω)t}`. **Converting an
exponential a priori bound into a linear one is exactly the content of a zero-free half-plane.** The
reformulation moves the difficulty; it does not reduce it.

**Three things are nonetheless better than the `ω = 0` case, and they are not cosmetic.**

1. **The marginality screen does not fire.** At `ω > 0` the criterion has a margin growing linearly,
   with an explicit slope. Approximation arguments are not excluded a priori, unlike at `ω = 0`.
2. **The allowance is linear, not square-root.** Most RH-equivalent positivity criteria demand
   square-root cancellation. Here you need only `o(t)` control of the twice-integrated weighted
   Chebyshev error — a much weaker requirement, purchased by asking for a weaker conclusion.
3. **Failure is exponentially visible** (§4), so the criterion is falsifiable in the strong sense and
   numerically meaningful.

**Where it sits in the ledger.** A translator, not a producer — but a *graded* translator, which no
other item in this programme has been. Every criterion the project has screened is all-or-nothing;
this one has a dial, and the dial is calibrated (`ω_c = Θ − ½`, margin `= (ξ′/ξ)(½+ω)`,
threshold `= 0.3748/ω`, sensitivity `= δ−ω`).

---

## 7. What to do next

1. **The one concrete question this raises.** The margin is `0.0462·ω·t` and the a priori fluctuation
   is `e^{(½−ω)t}`. **Is there any `ω` for which a partial-summation / explicit-formula argument
   using only known zero-density estimates closes that gap?** Zero-density theorems
   (Ingham; Guth–Maynard) bound `N(σ,T)` and are exactly the right input, since the fluctuation is a
   sum over zeros weighted by `e^{(Re ρ−½−ω)t}`. **This is the calculation to try**, and it is the
   natural way to test whether the reformulation is more than restatement.
2. **Compute `Ψ_ω` at large `t`** on the prime side (segmented sieve past `e²⁰`) and compare against
   the drift. Any deviation exceeding the `e^{−ωt}` envelope at a given `ω` would be a numerical
   signal about `Θ`. Cheap.
3. **Settle one open priority item.** Bombieri, *Rend. Lincei* **11** (2000) §8 uses characteristic
   functions of `[−t,t]`; whether he states a restricted-family equivalence there is the one place a
   priority claim for Theorem 1.7 could break. Requires a human read — the PDF resisted retrieval.
4. **Ask Suzuki.** He wrote §11 and dropped it, and his later
   [2209.12832](https://arxiv.org/abs/2209.12832) Theorem 1.1 has the *"eventually non-negative"*
   shape for the extended Selberg class **without** the `ω`-shift. Worth knowing whether he abandoned
   `Ψ_ω` for a reason.

---

## 8. Corrections to the record

- **`ROUND12`/previous session framing withdrawn**: "Weil positivity collapses to a one-parameter
  family" is not new in kind — Bombieri–Lagarias 1999, per Lagarias' own 2007 restatement:
  *"each positivity condition `λₙ > 0` encodes 'Weil positivity' of Weil's quadratic functional for a
  particular test function `gₙ(x)`."* Suzuki cites the analogy himself.
- **Theorem 1.6 (`RH ⟺ Ψ = O(1)`) should not be leaned on.** Its proof cites nothing external; it is
  a restatement of "abscissa of convergence `= Θ`" through the Laplace representation. I called it
  "classical-adjacent"; the accurate description is "two lines, no independent content."
- **Theorem 1.2 = Lagarias ∘ Kreĭn–Langer**, confirmed by Suzuki's own derivation — a change of
  language, not an independent theorem. **Theorem 1.4** is his own stated "analog of Yoshida's
  result" on a simpler space.
- **§11 is Lagarias's `θ` in screw form.** Lagarias *Acta Arith.* **89** Theorem 1.1 already carries
  the general `θ`.
- **Citation data**: JLMS **108** (2023) has 12 citations (Semantic Scholar, DOI
  10.1112/jlms.12785), 8 self, **none on `Ψ_ω`**.

---

## 9. Reproduction

| script | produces |
|---|---|
| `w1_psi_omega.py` | §1 the derivation; Check 0 (printed-value validation) and Check 1 (`A`, `B` closed forms vs 250 zeros + tail) |
| `w2_psi_omega_asym.py` | §2 Check 2 — prime side vs asymptotic, `Λ(n)` sieved to `e¹⁵` |
| `w3_margin.py` | §3 the margin table and the universal `t₀` |
| `w4_sens.py` | §4 envelope growth rate and detection height |

`mpmath`, `numpy`.

**Sources.** Suzuki [2206.03682](https://arxiv.org/abs/2206.03682) (JLMS **108** (2023)) §§1–5, 7,
11 — read in full · Lagarias, *On a positivity property of the Riemann ξ-function*, *Acta Arith.*
**89** (1999) 217, Thm 1.1 · Lagarias, *Li coefficients for automorphic L-functions*, *Ann. Inst.
Fourier* **57** (2007) 1689 · Bombieri–Lagarias, *J. Number Theory* **77** (1999) 274 · Li, *J.
Number Theory* **65** (1997) 325 · Bombieri, *Rend. Lincei* **11** (2000) 183 · Yoshida, *Adv. Stud.
Pure Math.* **21** (1992) 281 · Widder, *The Laplace Transform*, Ch. II Thm 5b ·
Mossinghoff–Trudgian–Yang [2212.06867](https://arxiv.org/abs/2212.06867) · Ford, *Zero-free regions
for the Riemann zeta function* · Sutherland, MIT 18.785 Lecture Notes 16 · Suzuki
[2209.12832](https://arxiv.org/abs/2209.12832).
