# Referee report — *Archimedean first-slab positivity for shifted zeta canonical systems*

**Draft reviewed:** WORKING_DRAFT_first_slab_positivity, 31 August 2026, with EDITORIAL_NOTES_first_slab_revision_20260831
**Stance:** adversarial. I tried to break the result. I did not break it, but I found one false theorem statement, one avoidable factor-2 loss that costs half the headline margin, and one structural fact that invalidates the paper's own plan for the next slab.
**Method:** every analytic identity re-derived independently; every checkable constant recomputed from scratch in mpmath/numpy; the central Legendre certificate rebuilt from the definitions in §5.1 without reference to the draft's code.

---

## 0. Verdict

The proof chain is **sound as far as it goes**, and Theorem B survives an independent reconstruction. Nothing I found threatens Theorems A, B or C on the stated range. But the draft is not circulation-ready, for three reasons that are not presentational:

1. **§4.2's boxed representation is false at ω = 1/2**, by a quantity three orders of magnitude larger than the certified margin (§2 below). The certificate is safe because it does not use that formula, but the paper states it unconditionally and a reader or reimplementer who uses it will get a wrong answer.
2. **The headline margin is half of what it should be**, because the kernel bound 0.024587 is exactly twice the sharp Schur value (§3).
3. **L = log 2 has ~7% of headroom, not a comfortable margin**, and the prime-free form goes negative just past it — which contradicts the second-slab strategy proposed in §12.3 (§4).

Everything below is ordered by severity.

---

## 1. What I independently confirmed

I re-derived these and agree; they are correct as stated.

| Claim | Status |
|---|---|
| §2.2 `H = VR = RV*`, `RVR = V*`, `H² = VV*`, `‖H‖ = ‖V‖`, `I ± H ≻ 0 ⟺ ‖V‖ < 1` | correct, all four identities |
| §2.1 only `n = 1` contributes for `L ≤ log 2`; `n = 2` sits on a null set | correct |
| §3.1 `K_ω(p) = π^ω · (p+α)(p−β)/[(p+β)(p−α)] · Γ((p+α)/2)/Γ((p+β)/2)` | correct (uses `α + β = 1`) |
| §3.2 explicit impulse `κ_ω` | **numerically verified**: its Laplace transform matches `K_ω(p)` to rel. 1.5e−17 at ω=1/2, 8.3e−11 at ω=0.3 (residual is my quadrature against the `t^{ω−1}` endpoint, not the formula) |
| §3.3 Sonine identity `a_ω * b_ω = 2e^{−αt}` | correct — `A(p) = Γ((p+α)/2)/Γ((p+β)/2)`, `B(p) = Γ((p+β)/2)/Γ((p+α)/2+1)`, product `= 2/(p+α)` |
| §3.3 rational collapse `F_{1−ω}(p+1)K_ω(p) = 2π^ω(p−β)/[(p+β)(p−α)]` | correct |
| §4.1 formula for `a_ω(p)` | correct, from `ℓ'(p) = 1/(p+½) + 1/(p−½) − ½log π + ½ψ((p+½)/2)` |
| §4.3 Prop 4.1, kernel `c_ω = (cosh(ω\|x−y\|)−1)R(\|x−y\|)` | **correct** — verified analytically and numerically to 30 digits (see §5 for the proof-writing objection) |
| §4.4 `R(t) = −1/(2t) + 7/4 + O(t)`, `c_ω = O(\|x−y\|)`, Hilbert–Schmidt | correct |
| §6.1 `S(t) = te^{t/2} − ½e^{−3t/2}·t/sinh t`, analytic in `\|t\| < π` | correct |
| §6.2 Legendre correlation formula for `(T_{k,L})_{mn}` | **correct** — I re-derived it independently; the `L^{d+2k}/(d+2k+j)` bookkeeping is right |
| §6.3 `t₀ = 0.2811995743229618465…` | correct to 25 digits |
| §5.2 `p_n = √(2T₀(2n+1)) i_n(T₀/2)` | correct, both parities |
| §10.2 `Θ_{1/2}(u) = ((u−i)/(u+i))·φ((1−iu)/2)` | correct, including the sign |
| §10.4 Euler product `Σ c_ω(n)n^{−s−1/2} = ζ(s+½−ω)/ζ(s+½+ω)` | correct |
| §8.6 compactness ⇒ `‖V‖ < 1` from `D ≻ 0` | correct |

**And, most importantly, Theorem B.** I rebuilt the central and shifted head matrices from the §5.1 definitions — my own Legendre basis, my own frequency quadrature, my own digamma and Bessel evaluations, my own perturbation reduction — and got:

| Quantity (L = log 2, 16 modes/sector) | My value | Draft |
|---|---:|---:|
| λ_min(Q₀ head), even, with the β\* floor | 1.15446881e−3 | ≥ 1e−3 (§5.3) |
| λ_min(Q₀ head), odd, with the β\* floor | 5.81399439e−2 | ≥ 5e−2 (§5.3) |
| λ_min(Q₀ + C_{1/2}) − Schur loss, even | 3.322614e−4 | 3.096539e−4 |
| λ_min(Q₀ + C_{1/2}) − Schur loss, odd | 5.232337e−2 | 5.231472e−2 |

My values sit *above* the draft's certified minima by exactly the amount one expects from interval widening over a box. **Theorem B is independently corroborated.** Mode-count convergence is excellent (8 → 28 modes/sector moves λ_min by < 0.15%), so the choice of sixteen modes is amply justified.

I also reverse-engineered the Schur loss exactly:

```
loss = (0.024587 + κ)² / 1.5053999819194765
κ_even = 1.4084884e−9  →  4.015681184546116e−4   (draft: 4.01568118454612e−4)
κ_odd  = 2.2191643e−10 →  4.015680796951506e−4   (draft: 4.01568079695150e−4)
```

Fifteen-digit agreement. That is a good sign for the code, and it is what lets me say the following two things with confidence.

---

## 2. **Critical.** The §4.2 boxed representation is false at ω = 1/2

The display

> `Q_{ω,L}[f] = (1/2π)∫ w_ω(τ)|f̂(τ)|²dτ + |C_α(f)|² + |C_β(f)|² − |S_α(f)|² − |S_β(f)|²`

is boxed with no restriction on ω, and Theorem B's range is `0 ≤ ω ≤ 1/2` inclusive. It is wrong at the right endpoint.

**Why.** As `α = ½ − ω ↓ 0`, `½ Re ψ((α+iτ)/2) ≈ −α/(α²+τ²)`, which converges to `−π δ(τ)`, not to its pointwise limit. Equivalently, the difference kernel

`G_ω(u) = −e^{−|u|/2}(cosh(ωu) − 1)/(1 − e^{−2|u|})`

decays for every ω < 1/2 but tends to the constant `−1/2` at infinity when ω = 1/2 (I checked: `G_{1/2}(30) = −0.4999997`).

**How much.** I evaluated both sides for several even test functions on `I_{log2}`:

| f | ω | Fourier side − kernel side |
|---|---|---:|
| 1 | 0.30 | −9.6e−12 (quadrature noise) |
| 1 | 0.45 | −2.2e−11 |
| **1** | **0.50** | **+0.24022651** |
| 1 + 3x² | 0.30 | −1.8e−11 |

and `0.240226507 = ½(∫_{I_L} f)²` to every digit shown. So the boxed formula, read literally at ω = 1/2, **overstates `Q_{1/2,L}[f]` by exactly `½|∫_{I_L} f|²`**. For the even sector at `L = log 2` that is ≈ 0.24, against a certified margin of 3.1e−4 — a factor of 776.

**Consequences.**
- §7.3's assurance ("no limiting digamma evaluation is used there… carries the boundary delta contribution") is *correct*, and the certificate is safe because it goes through `Q₀ + C_ω`. But the draft never says what the lost contribution is, so the assurance is unverifiable by a reader and unusable by a reimplementer.
- §4.2's closing sentence ("a pointwise limit… would lose its distributional boundary contribution") is the right instinct stated too vaguely to be checkable.

**Fix.** Restrict the boxed display to `0 ≤ ω < 1/2`, then state the endpoint case as a short lemma:

> At ω = 1/2 (α = 0), the same formula holds with `w_{1/2}` the pointwise limit provided the coefficient of `|C₀(f)|² = |∫ f|²` is **1/2 rather than 1** — equivalently, `w_{1/2}` carries an additional `−π δ(τ)`.

This is one paragraph and it removes the paper's single most dangerous sentence. Add it to the §12.1 human-check list as well; item 2 currently says "check the contour displacement and the ω = 1/2 boundary convention line by line" without saying what the answer is.

---

## 3. **Significant.** The kernel bound 0.024587 is exactly 2× the sharp value, and it costs you half the headline margin

I computed the Schur test for `c_{1/2}` on `I_{log2}` directly. The row sums `∫_{I_L}|c(x,y)|dy` are maximized at the endpoints and equal

```
sup_x ∫_{I_L} |c_{1/2}(x,y)| dy = 0.0122930504011423196
draft (§6.3)                    = 0.02458610080228464   = 2 × 0.01229305040114231960
```

Exactly double, to all digits. Two readings, and you must say which:

**(a) Deliberate conservatism** (e.g. you bounded `∫_{−L}^{L}` rather than the actual row sum). Then say so, because —

**(b) The `Q = B/2` factor leaking into the kernel.** Appendix A warns about precisely this hazard. I tested it: if the perturbation matrices `T_k` were also doubled, then `λ_min(Q₀ + 2C_{1/2})` even = 2.9738e−4 and the certified even margin becomes **−1.04e−4** — the certificate would fail. Since it does not fail, **the `T_k` are correct and only the scalar bound is loose.** Good news, but the reader cannot tell, and the two constants sit six sections apart.

**Why it matters beyond bookkeeping.** With the exact loss formula recovered in §1:

| | current | with the sharp constant |
|---|---:|---:|
| head–tail coupling bound | 0.024587 | 0.0122931 |
| `d_tail` | 1.5053999819 | 1.5176939315 |
| Schur loss | 4.01568e−4 | **9.9572e−5** |
| certified even margin | 3.0965e−4 | **≈ 6.34e−4** |

The Schur loss currently consumes **55% of the even-sector margin**. Halving one scalar roughly doubles the headline number for free — no new computation, no new interval arithmetic. This is the cheapest robustness gain available to the paper, and a referee who notices the factor of 2 will ask why you left it on the table.

Related, and smaller: §6.3's Taylor remainder `1.532967865231399e−12` is ≈ 3.25× the sharp sign-split value I get (`4.711044e−13`). Harmless — it is twelve orders below the margin — but the text calls it the result of "direct sign-split integration", which it evidently is not. Say what it actually is.

---

## 4. **Significant.** The positivity horizon: L = log 2 has ~7% of headroom, and §12.3's plan does not survive it

I swept the window and the shift, using the untruncated frequency integral (convergence checked to cutoffs 3000/10000/40000; the negative values below are robust, not truncation artifacts) with 24 modes/sector.

**In the window length**, at ω = 0:

| L | even | odd |
|---|---:|---:|
| 0.60 | +7.560e−3 | +2.224e−1 |
| **0.693147 = log 2** | **+1.3279e−3** | **+7.2972e−2** |
| 0.75 | +1.0568e−3 | **−9.721e−3** |
| 0.80 | +6.253e−4 | −7.816e−2 |
| 0.90 | −7.441e−3 | −2.053e−1 |
| **1.098612 = log 3** | **−7.403e−2** | **−4.304e−1** |

Crossings: **L\*(odd) ≈ 0.7429, L\*(even) ≈ 0.8199.**

**In the shift**, at L = log 2: **ω\*(even) ≈ 0.8611**, ω\*(odd) ≈ 1.8047.

Three consequences, in decreasing order of how much they should worry you.

**(a) §12.3's second-slab strategy is stated backwards.** The plan is to write the new generator as "the positive first-slab density plus a bounded delayed correction". On the window `log 2 < L < log 3` where the delayed layer lives, the first-slab density is **not positive** — it is `−9.7e−3` already at L = 0.75 and `−0.43` at L = log 3. The delayed `n = 2` term is therefore not a perturbation of a positive object; it would have to *supply* the missing positivity. That inverts the expected difficulty of the next paper and should be said out loud in §12.3 rather than discovered by whoever attempts it. It also makes §12.3's last bullet ("identifying a precise obstruction if it does not") the likely outcome rather than the fallback.

**(b) §9.3 can be strengthened for free, up to a computable ceiling.** Since `dD/ds = 2V_s*Q_sV_s`, certifying merely `Q_s ⪰ 0` for `s ∈ [1/2, ω]` gives `D_ω ⪰ D_{1/2} ≻ 0`, hence `‖V_ω‖ < 1` — with no Paley–Wiener zero-density argument, no multiplicity analysis, and no appeal to Suzuki's inner range. That is exactly the argument §9.3 declines to make, obtained from the machinery already in the paper. Extending the existing box sweep from `[0, 1/2]` to `[0, 0.85]` would let you delete the caveat and the §12.1 item 6. By my sweep the mechanism dies at ω ≈ 0.861 and no amount of extra boxes gets past it — which is itself worth a remark, since it says the energy-identity route is intrinsically confined to a bounded shift range.

**(c) State the headroom.** As written, a reader assumes L = log 2 sits comfortably inside a positivity region. It sits at ~93% of the way to the edge. That is not a defect in the theorem, but it is material to how much the result should be trusted to generalize, and it is the kind of thing a referee finds and you did not disclose.

**One caveat on my own numbers.** These are floating-point Rayleigh minima over the head subspace, not certified. They are upper bounds on the true infimum, so the *negative* entries are meaningful (they exhibit a direction) modulo the dropped high-frequency tail, which I checked converges. But before you cite them, reproduce them in your own Arb pipeline — it is a two-line change to your existing code.

---

## 5. **Significant.** Proposition 4.1 is six lines for the paper's central structural identity, and is not a proof

The identity is right — I verified `w_ω(τ) − w_0(τ) = FT[−e^{−|u|/2}(cosh(ωu)−1)/(1−e^{−2|u|})](τ)` to 30 digits at ω = 0.1 and 0.3. But the proof as written is not one.

The phrase **"up to the common local renormalization"** hides the actual difficulty. The digamma integral representation

`½ψ((p+c)/2) = −γ/2 + ∫₀^∞ [e^{−2t} − e^{−(p+c)t}]/(1 − e^{−2t}) dt`

**cannot be split termwise**: both pieces diverge logarithmically at `t = 0`. So there is no `L¹` kernel for `Q₀` at all, only a Fourier multiplier — which is exactly why `Q₀` is unbounded above and why `D_log` is needed. The cancellation of those divergences in `a_ω − a_0` *is* the content of Proposition 4.1, and it is the step the proof skips.

**Recommended rewrite.** State it as an identity of Fourier multipliers on compactly supported `f`, in two independent halves:
- the four rational terms give `cosh(α(x−y)) + cosh(β(x−y)) − 2cosh((x−y)/2) = 2cosh(\frac{x-y}{2})(cosh(ω(x−y)) − 1)`, elementary and kernel-level;
- the digamma terms give `−e^{−|u|/2}(cosh(ωu) − 1)/(1 − e^{−2|u|})`, as a difference of two convergent multiplier integrals with the `γ` and `log π` constants cancelling before any splitting.

Adding the two and using the algebraic identity

`e^{−u/2}/(1 − e^{−2u}) = e^{−u/2} + e^{−5u/2}/(1 − e^{−2u})`

produces `R`. That identity is worth displaying: as the draft stands, the `e^{−5t/2}` in `R(t)` appears from nowhere and looks like a typo. Then note that the whole argument requires ω < 1/2 and hand the endpoint to the lemma from §2 of this report.

---

## 6. Section 8: four gaps, none fatal, all cheap to close

**(a) Which inner product?** §8.1 builds `V_{s,L}` inside the weighted Hardy space `H_η = L²(ℝ₊, e^{−2ηt}dt)`, but `D_{s,L} = I − V*V` and the conclusion `I ± H ≻ 0` must live in **unweighted** `L²(0,L)`. The two spaces coincide as sets with equivalent norms, so norm-differentiability transfers — but *adjoints do not*. As written, §8.4's `V*` is ambiguous. One sentence fixes it: state that `V' = −AV` is an identity of operators on `L²(0,L)` (adjoint-free, so the transfer is legitimate) and that every adjoint in §8.4–8.6 is the unweighted one.

**(b) §8.6's continuity claim is unearned and unnecessary.** "The integrand is continuous and nonnegative on every compact positive-shift interval" — §8.3 gives `V_sL² ⊂ D_log` but nothing about continuity of `s ↦ V_sf` in the `D_log` norm. You do not need it. Measurability suffices: `∫ = 0` with an a.e.-nonnegative integrand forces `Q_s[V_sf] = 0` for a.e. `s`, hence `V_sf = 0` for a.e. `s`, hence `f = 0` along any sequence `s ↓ 0`. Delete the continuity claim; the argument gets shorter *and* correct.

**(c) Uniformity of the gap.** The strictness argument needs `Q_{s,L} ≥ c‖·‖²` with `c > 0` **uniform in s**. Your certificate delivers exactly that (3.0965e−4 over the whole interval), but the text says only "strict positivity", which leaves `c(s) → 0` formally open. Say "uniformly strictly positive, by Theorem B".

**(d) §7.2's "Shorter intervals follow by compression" is one clause doing real work.** Give it two sentences: the kernel `½a_ω(|x−y|)` does not depend on `L`, so `Q_{ω,L'}` is the restriction of `Q_{ω,log2}` under zero-extension, and by causality `V_{ω,L'}` is the compression of `V_{ω,log2}` to `L²(0,L')`. Both directions of Theorem A then follow. As written a referee will stop here.

---

## 7. Numerical reporting: four inconsistencies a referee will find

**(a) §7.1 contradicts itself.** The formula reads `d_tail ≥ β_* − δ_central − 0.024587`, and the displayed value is `1.5053999819194765`. I compute `β_* = log(30/2π) − 1/30 = 1.5299869819194765585`, so `β_* − 0.024587 = 1.5053999819194765585` — **the displayed value, exactly**. Hence `δ_central = 0` in the number you report. Either declare `δ_central = 0` or fix the display.

**(b) The clean-room audit is *less* conservative than the primary, and the draft does not notice.** The audit margins exceed the primary's by +1.645e−8 (even), +2.46e−9 (odd), and the pivot by +1.80e−7. But §7.5 says the audit assigns each central entry radius `5e−10`, **five times** the primary's `1e−10`. A larger radius must give a *smaller* certified margin. So the two pipelines differ in some bounding step (tail bookkeeping? LDL pivot ordering? a different Schur constant?), by ~10⁷ times the quoted quadrature discrepancy of 1.69e−15, and in the wrong direction. §7.5 calls this "a strong independent reproduction" — it is, on the eigenvalues, but the *certificates* disagree in a way that is unexplained. Explain it, or the audit is not auditing what it claims to audit. This is the item I would push hardest on in a second round.

**(c) Unexplained row counts.** Appendix B claims "certified boxes: 512"; the editorial note reports "Investigation 12 rows | 724 verified", "audit rows: 783", "matrix rows: 1,360", "Investigation 13 diagnostics | 90". Nothing says what a row is or why 724 ≠ 512. Define the schema in Appendix B.

**(d) §5.2 phase error.** With the stated convention `f̂(τ) = ∫f(x)e^{−iτx}dx`, the correct coefficient is `φ̂_n(τ) = √(2T₀(2n+1))·(−i)ⁿ·j_n(T₀τ)`, not `iⁿ`. Harmless inside a parity sector (`i^{m−n} = (−i)^{m−n}` when `m ≡ n mod 2`), and it does not affect any reported number, but it is wrong as written and a careful reader will trip on it.

---

## 8. Framing: the paper undersells itself in one direction and oversells in another

**Undersells.** §1.5 is admirably restrained, but it omits the sentence that makes the result interesting. For `0 < ω < 1/2`, `Θ_ω` meromorphic inner ⟺ ξ has no zeros with `Re s > 1/2 + ω` — an **open** quasi-RH statement. Finite-section contractivity is a *necessary condition* for it. So Theorem A verifies, unconditionally and by computation, a necessary condition for something nobody can prove, over the entire critical shift interval — a test that could have failed and did not. For `ω ≥ 1/2` the corresponding statement is unconditional (ξ's zeros lie in the critical strip), so **all** the content is in `ω < 1/2`. Put this in §1.1. As written, a referee can read the whole paper as "prime-free, finite-depth, proves nothing" — which is what §1.5 almost invites.

Relatedly, §9.3's heading "The complementary range ω > 1/2" and its apologetic tone suggest that range is the hard part. It is the easy part. Reword.

**Oversells.** §5.3 says the central certificate "is a short-window instance of the finite-frequency compact-window strategy developed in recent work on Weil positivity [4,5]". Two problems:
- For `L ≤ log 2` **no prime term enters the explicit formula**, so `Q_{0,L}` is precisely the full Weil functional on that window. The ω = 0 case of Theorem B therefore **re-proves a known theorem** rather than instantiating a method. Say so plainly; it costs nothing and pre-empts the obvious referee objection. The genuinely new content of Theorem B is the off-center deformation.
- Reference [5] (Chuk, arXiv:2608.24827 — it exists; I checked) advertises "extending the classical range log 2 by a factor of 2.3", certifying positivity out to a window of 1.6 with margin 8.9e−18. **Reconcile that against my §4 computation, which puts the odd-sector threshold at 0.7429.** Either the two papers use different conventions for "window" (likely — half-width of `f` vs. of `g = f * f̃` differ by a factor of two, and `2 × 0.743 = 1.49` is uncomfortably close to 1.6), or the two forms differ by the pole terms, or one of the computations is wrong. This must be settled before circulation: if [5] really certifies positivity of the *same* form past 0.743, one of you has a bug. It is also directly relevant to §12.1 item 8, the originality search.

---

## 9. References

All numbered references exist and the arXiv identifiers resolve: [1] 1204.1827, [2] 2206.03682, [3] 2606.09096, [4] 2006.13771, [5] 2608.24827, [6] math/0509619, [7] Lagarias, Acta Arith. 89 (1999) 217–234 with the 2005 correction, [8] 2103.00549, [9] 1602.08618, [10] 2509.22765, [11] Osterwalder–Schrader CMP 31 (1973), [12] Graham–Zworski Invent. Math. 152 (2003), [13] DLMF ch. 5. No hallucinated citations. Good.

Two problems anyway:

- **[3], [7], [11], [12], [13] are never cited in the body.** Five of thirteen. Cite or cut. (Osterwalder–Schrader in particular is load-bearing for the phrase "reflection positivity" and should actually be invoked at §9.1.)
- **Two directly relevant recent items are missing**, both of which bear on §12.1 item 8:
  - arXiv:2607.24830, *A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator: The Archimedean Spectral Law, its Universality, and an Operator Form of Weil's Positivity Criterion*
  - arXiv:2607.02828, *A finite Guinand–Weil dictionary and archimedean tail order for the truncated Weil quadratic form*

  Both appear to overlap the compact-window Weil certificate directly. Read them before claiming novelty for anything in §5.

---

## 10. Minor

- **§6.3.** `t₀` has a closed form: `R(t) = 0 ⟺ e^{3t} − e^{t} = 1`, so `t₀ = log ρ` where `ρ = 1.3247179572…` is the **plastic number**, the real root of `x³ = x + 1`. Nineteen decimals of a number with a two-symbol closed form is a missed opportunity, and the closed form makes the interval enclosure trivial.
- **§10.1.** "`S_ω = E_ω/2`" restates `E_ω = 2(ξ'/ξ)(½+ω)` verbatim two lines above it. Either derive it or drop it; as displayed it reads as padding in a list of four "different transforms of one scalar quantity", one of which is a tautology.
- **§9.4.** "Standard positive triangular-factorization results… then *suggest*… A final publication version should either verify… or present…" — this is a research note inside a theorem-grade paper. The editorial note's own item 7 already says to decide. Decide: cut it, keep the Gram factor.
- **§1.4** ("Why this is one paper rather than two") is arguing with a referee who has not spoken yet. Compress to two sentences or move to a cover letter.
- **Appendix C** is genuinely good and should be kept; it is the fastest way for a referee to see what is claimed at what strength. Add rows for the two items in §2 and §4 above once resolved.
- The LM-assistance disclosure and the author-verification notice are appropriate and should stay.

---

## 11. What I would do next, in order

1. Add the ω = 1/2 endpoint lemma (§2). One paragraph. Highest severity, lowest cost.
2. Replace 0.024587 with the sharp 0.0122931 and re-run the boxes (§3). Roughly doubles the headline margin; no new machinery.
3. Reproduce my §4 sweep in the Arb pipeline, and rewrite §12.3 around the answer. If it holds, it is the most interesting fact in the paper and belongs in the introduction, not the future-work section.
4. Resolve the [5] convention question (§8). If it is a real disagreement, everything else waits.
5. Explain the primary-vs-audit certificate discrepancy (§7b).
6. Rewrite Prop 4.1's proof (§5) and the four §8 items.
7. Extend the box sweep to ω ≈ 0.85 and delete the §9.3 caveat and §12.1 item 6 (§4b).

---

### Appendix: reproduction

All numbers in this report were computed independently of the draft's source, in Python (mpmath 1.4.1 / numpy 2.4.4 / scipy 1.17.1), using only the definitions printed in §§4.2, 5.1, 5.2, 6.2 of the draft. Scripts: sign-change and Schur bound; Taylor remainder and tail floor; Legendre certificate reconstruction and ω/L sweeps; Fourier-vs-kernel endpoint comparison; impulse Laplace transform. Frequency-cutoff and mode-count convergence were checked for every reported eigenvalue.
