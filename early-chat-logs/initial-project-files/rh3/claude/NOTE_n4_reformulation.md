# N=4 SYM and RH: correcting "closed", and a candidate reformulation

**2026-08-25; revised 2026-08-26 (v2).** Written in response to a direct challenge: *are you sure
N=4 SYM is closed? One route leading to one result (PNT) doesn't mean the seam is closed.*

**The challenge is correct and I am revising.** My previous note over-claimed. What is closed is one
specific route — reading RH off the `SL(2,ℤ)` Plancherel measure, or applying bootstrap positivity to
the spectral density. That is genuinely dead, for reasons that survive stress-testing. But I stated
it as though it closed the seam, and it does not. The zeta zeros appear in an N=4 SYM quantity, that
appearance has never been turned into an RH-equivalence statement, and the equivalence is writable.
This note does the stress test, states the reformulation, and gives an honest assessment of what it
is and is not worth.

> **v2 changelog.** The v1 formula was transcribed from seminar slides and carried a load-bearing
> caveat. The printed paper has now been read: **eq. (4.31), §4.2, matches the transcription character
> for character** — the caveat is discharged, nothing was wrong. Three substantive corrections
> follow: (i) the equation references are **(4.20)** for the contour representation and **(4.31)** for
> the residues, not (3.36)–(3.37) (those are the Mellin–Barnes kernel, the `τ₂ → ∞` side);
> (ii) **the residue numerics in v1 §3.2 were wrong by five to six orders of magnitude** — the
> envelope constant is `8.07·10⁻⁶`, not `2.114`, and the decay rate is `−π/4`, not `−0.674`;
> (iii) **§4 item 5 is reframed** — the `3/4` collision with Benjamin–Chang is not a referee hazard,
> it is a shared mechanism the authors identify and cross-cite in print.

---

## 1. Stress-testing the three reasons

My note gave three reasons. They are not equally strong, and the objection lands on the weakest.

**Reason 3 (Sarnak's ceiling) — soft, and the objection is right.** "Maass–Selberg positivity yields
effective zero-free regions in `Re(s) ≤ 1`, and fifty years of professional effort has not pushed it
further" is historical evidence, not proof. It should be weighted as evidence about difficulty, not
as a closure. I over-weighted it.

**Reasons 1 and 2 — hard, but narrower than I stated.**

- *Reason 1 (the ξ's cancel).* True, and it is algebra: PPR pair `{𝕆,E_s} = (𝕆,E_s)/Λ(s)` against
  `E*_s = Λ(s)E_s`, so `Λ` cancels and the physical spectral density is Gammas and rationals. **But
  this is a statement about the `L²` spectral decomposition only.** It does not say no N=4 SYM
  quantity carries `ξ` non-trivially — and one does (§2).
- *Reason 2 (wrong contour).* On `Re s = 1/2` you evaluate `ξ(1+2it)`, the strip edge, where
  non-vanishing is PNT (1896). **But this is a statement about the canonical contour.** Deform off
  it — which is exactly what building a `τ₂ → 0` expansion requires — and you cross the zeros.

So reasons 1 and 2 close *the naive route*. I presented them as closing the seam. That was the error.

---

## 2. Where the zeros actually appear in N=4 SYM

Dorigoni–Treilis ([2307.07491](https://arxiv.org/abs/2307.07491), JHEP 11 (2023) 102) study
generalised Eisenstein series `[Δ − λ(λ−1)] E(λ; s₁,s₂) = E(s₁)E(s₂)`. The physically relevant
spectrum `λ ∈ {s₁+s₂+1, s₁+s₂+3, …}` with `s_i ∈ ℕ+1/2` gives the type IIB `D^{2k}R⁴` coefficients
**and the coefficients in the large-`N` expansion of the N=4 SYM integrated correlators of four
half-BPS operators at fixed `τ`**. The case `λ = 4, s₁ = s₂ = 3/2` is the `D⁶R⁴` coefficient.

The zero Fourier mode `a₀` — the **zero-instanton sector** — has a Mellin–Barnes contour
representation (**eq. (4.20)**) whose kernel carries `1/ξ(2−2t)` in the denominator. Its poles are at
`2−2t = ρ`, i.e.

> **`t = 1 − ρ/2`**, so `Re t = 1 − Re(ρ)/2`, which is `3/4` exactly when `Re ρ = 1/2`.

That is the paper's Figure 1: *"an infinite family of poles with `ℜ(t) = 3/4` (if Riemann hypothesis
is correct) coming from the non-trivial zeroes of the Riemann zeta."* The authors call it "surprising
and quite mysterious" and stop. Their closing assessment, verbatim: *"We do not know why Riemann
hypothesis should play any rôle in the strong coupling limit of string theory, nonetheless, we find
this observation extremely fascinating and in need of further exploration."*

The resulting small-`y` expansion (`y = τ₂`), **printed eq. (4.31)**:

```
a₀(λ;s₁,s₂|y) ~ #y^{s₁+s₂−1} + #y^{s₁−s₂} + #y^{s₂−s₁} + #y^{1−s₁−s₂} + #y^λ
              + Σ_{ρ_n} β(ρ_n) y^{t}|_{t = 3/4 + iρ_n/2} + NP(y)

β(ρ) = 2 ξ(t+s₁+s₂−1) ξ(t+s₁−s₂) ξ(t+s₂−s₁) ξ(t+1−s₁−s₂)
       ─────────────────────────────────────────────────────
       (1−t−λ)(t−λ) Γ(s₁)Γ(s₂) π^{1/2−t} Γ(t−1/2) ζ′(2t−1)
```

**Transcription status: verified against print.** v1 flagged this formula as recovered from a
summarising fetch of the seminar slides, with two renderings of the paper disagreeing by one unit in
some arguments. The printed paper has now been read directly. **Eq. (4.31) matches the formula above
character for character.** Nothing was wrong; the caveat is discharged. Note that the printed form
writes the residues at `t = 3/4 + iρ_n/2` — i.e. **the paper's own expansion already assumes RH**,
which is precisely why the statement in §3.4 is worth making explicitly.

Two further things from §4.2 worth having on the record:

- **Footnote 7 is an erratum to the authors' own earlier work**: *"The contribution from these poles
  was inadvertently missed in [37]"* — the zeta-zero terms were absent from Dorigoni–Kleinschmidt–
  Treilis [2208.14087](https://arxiv.org/abs/2208.14087) and are added here.
- **Their numerics.** Figure 2 subtracts every non-zeta term and compares the residual against the
  first **10** zeros — *"consistent with the numerical data within a `10⁻¹⁹` error over the whole
  range of `y` considered"*; Figure 3 repeats it with the first **50**. So the sum converges in
  practice, independently of §3.2 below.

---

## 3. The candidate reformulation, and three computations it needs

Take the physical case `λ = 4, s₁ = s₂ = 3/2`. The four `ξ` arguments become `t+2, t, t, t−2`, and
the pole condition gives `2t−1 = 1−ρ`.

### 3.1 Non-degeneracy is automatic under RH (`n2`)

`β(ρ) = 0` requires one of the four `ξ` factors to vanish. At `t = 1 − ρ/2`:

| factor | argument | `Re` under RH | vanishes? |
|---|---|---|---|
| `ξ(t+2)` | `3 − ρ/2` | `11/4` | no — outside the strip |
| `ξ(t)` (twice) | `1 − ρ/2` | `3/4` | only if `1−ρ/2` is itself a nontrivial zero |
| `ξ(t−2)` | `−1 − ρ/2` | `−5/4` | no — reflect by `ξ(s)=ξ(1−s)`, lands at `Re = 9/4` |

So `β(ρ) = 0` requires two nontrivial zeros with `ρ′ = 1 − ρ/2`, hence `Re ρ′ = 1 − Re(ρ)/2`. If both
lie on the critical line this reads `1/2 = 3/4`. **The degenerate case cannot occur under RH.**
Verified numerically at `n = 1, 10, 50`: every `|ξ|` factor is bounded away from zero.

This matters more than it looks. Benjamin–Chang's 2d CFT analogue has its converse hostage to a
footnote in [2505.18314](https://arxiv.org/abs/2505.18314): *"The converse statement also holds
assuming that for every value of `k` there exists at least one CFT with `δ_k ≠ 0`."* Nobody has
discharged that. Here the residue is in **closed form**, because localisation gives the observable
exactly — so the condition is not an assumption but an explicit arithmetic statement, and in the
forward direction it is automatic.

### 3.2 The sum over zeros converges absolutely (`n1`) — corrected numerics

**v1's table was wrong by five to six orders of magnitude.** It is recomputed here from the
print-verified formula, at `dps = 30`, with stability confirmed at `dps ∈ {20,30,40,60}`.

| `n` | `γ_n` | `\|β_n\|` (correct) | v1 recorded (wrong) |
|---|---|---|---|
| 1 | 14.134725 | `4.010 × 10⁻⁶` | `1.86` |
| 2 | 21.022040 | `2.403 × 10⁻⁸` | |
| 3 | 25.010858 | `2.445 × 10⁻¹⁰` | |
| 5 | 32.935062 | `1.895 × 10⁻¹²` | `6.6 × 10⁻⁴` |
| 10 | 49.773832 | `6.851 × 10⁻²⁰` | `6.4 × 10⁻¹⁰` |
| 20 | 77.144840 | `4.559 × 10⁻²⁸` | `1.4 × 10⁻¹⁶` |
| 25 | 88.809111 | `8.523 × 10⁻³²` | `8.1 × 10⁻²⁰` |
| 50 | 143.111846 | `3.604 × 10⁻⁵¹` | |
| 60 | 163.030710 | `4.274 × 10⁻⁵⁷` | |

Fit: `log|β_n| = −0.795 γ_n − 2.337`, i.e. `|β_n| ~ e^{−0.795 γ_n}`. **This now matches the Stirling
estimate `e^{−πγ/4} = e^{−0.7854γ}` from the four `ξ`'s against `1/Γ(t−1/2)` essentially exactly** —
v1's `−0.674` had a residual discrepancy that I explained away as `1/ζ′(ρ)` plus polynomial factors.
There was no discrepancy; the fit was simply wrong. The clean agreement is itself a check on the
formula.

> `Σ_{n≤80} |β_n| = 4.0342 × 10⁻⁶` over positive ordinates;
> `8.0685 × 10⁻⁶` over all zeros (both signs). Absolutely convergent — the partial sums are already
> stable to 12 digits by `n = 10`, since the decay is exponential in `γ`.

**No source states this.** Dorigoni–Treilis write the expansion with `~` and never address
convergence; their Figures 2–3 check it numerically against 10 and 50 zeros. Absolute convergence is
what turns "envelope" from a formal phrase into a bound:

> **`|oscillatory part of a₀| ≤ 8.07 × 10⁻⁶ · τ₂^{3/4}`, uniformly in `τ₂`.**

The tail beyond `n = 80` is bounded by `e^{−πγ/4}` and is utterly negligible (`4 × 10⁻⁵⁷` scale at
`n = 60` already).

### 3.3 The converse direction has the right sign (`n2`)

Nontrivial zeros come in pairs `ρ, 1−ρ`, and the poles of `1/ξ(2−2t)` sit at **both** `t = 1−ρ/2` and
`t = (1+ρ)/2` by the functional equation. So if RH fails there is a zero with `σ := Re ρ > 1/2`, and
the dominant (smallest) exponent is `min(1−σ/2, (1+σ)/2) = 1−σ/2 < 3/4`. Then `τ₂^{1−σ/2}`
**dominates** `τ₂^{3/4}` as `τ₂ → 0`:

| `σ` | `1 − σ/2` | `(1+σ)/2` | dominant |
|---|---|---|---|
| 0.50 | 0.750 | 0.750 | `= 3/4` |
| 0.60 | 0.700 | 0.800 | 0.700 |
| 0.80 | 0.600 | 0.900 | 0.600 |
| 0.99 | 0.505 | 0.995 | 0.505 |

So the failure of RH is *visible* as an enhanced envelope, not hidden.

### 3.4 The statement

Putting the three together, and assuming simplicity of the zeros (needed for `ζ′(ρ) ≠ 0`):

> **Proposition (candidate).** Let `a₀(4; 3/2, 3/2 | τ₂)` be the zero-instanton sector of the `D⁶R⁴`
> coefficient — equivalently the corresponding coefficient in the large-`N` expansion of the N=4 SYM
> integrated correlator. Then, modulo simplicity of the zeros:
>
> **RH ⟺ the oscillatory part of the `τ₂ → 0` expansion of `a₀` is `O(τ₂^{3/4})`.**
>
> (⟸ contrapositive: a zero with `Re ρ = σ > 1/2` contributes `β(ρ)τ₂^{1−σ/2}` with `1−σ/2 < 3/4`,
> and `β(ρ) ≠ 0` unless `1 − ρ/2` is also a zero.)

The forward direction carries the explicit constant `8.07 × 10⁻⁶`.

Worth stating plainly in any write-up: the printed eq. (4.31) already *presumes* RH, writing its
residues at `t = 3/4 + iρ_n/2`. The content of the proposition is that this presumption is not a
convenience — it is equivalent to the statement being expanded.

---

## 4. Honest assessment: is this worth writing?

Measured against the criteria the community actually applies. Sarnak, in the Clay problem
description: *"There have been many equivalences of RH that have been found over the years. Without
their having led to any new information about the zeta function … it is difficult to know if such
equivalences constitute any real progress."* Connes, in his February 2026 survey, is blunter:
equivalences are *"alluring but treacherous: the history of the subject shows how easily an attempt
to solve the problem can be drawn into the gravitational pull of this 'black hole' of
equivalences."*

**What this has going for it.**

1. **The observable is defined independently of the zeros.** This is the line separating
   Benjamin–Chang (passes) from Remmen's amplitude and the Wei–Nori quantum-processor paper (both
   fail — the spectrum is *built* from the zeros, so the equivalence is a relabelling). The
   integrated correlator is defined by supersymmetric localisation, has independent weak- and
   strong-coupling expansions, and is known in closed form. **This is the strongest card, and neither
   template paper holds it.**
2. **Exact computability discharges the assumption Benjamin–Chang had to make.** Their iff rests on
   an unproven non-degeneracy footnote. Here `β(ρ)` is explicit and §3.1 settles the forward
   direction outright. That is a genuine improvement on the state of the art, not a transposition.
3. **Absolute convergence with an explicit constant** is new information about the expansion, and it
   makes the criterion *approximable at each scale* — the exponential decay `e^{−πγ_n/4}` means
   finitely many zeros control any given precision (10 zeros give `10⁻¹⁹`, per their Figure 2). That
   is one of the properties (Weil positivity's finitary character) that the community counts as
   substantive.

**What it does not have, and this is the honest limit.**

4. **No physical principle forces the envelope.** The `3/4` is `3/4` because RH puts it there.
   Nothing in N=4 SYM — not modularity, not unitarity, not the resurgence structure — is known to
   constrain it. I had a sweep look specifically at whether Dorigoni–Treilis's own modular-invariant
   Borel resummation ([2405.10204](https://arxiv.org/abs/2405.10204)) imposes any such condition:
   **it does not.** That paper resums the large-`N` series at fixed `τ`, a different asymptotic
   direction entirely; its median-summation reality condition acts on the `1/N` transseries and never
   touches the `τ₂ → 0` exponents; and it does not mention zeta zeros at all. The only rigorous
   growth bound in the vicinity (Green–Miller–Vanhove: `F = O(y^s)` at the cusp ⟹ `F_n = O(y^{1−s})`)
   gives `O(τ₂^{−3})` here, which `3/4` satisfies with enormous room. **It cannot force the critical
   line.**
5. **The `3/4` collision with Benjamin–Chang is a shared mechanism, acknowledged in print — lead with
   it, do not defend against it.** *(Reframed in v2; v1 treated this as a referee hazard.)*
   Benjamin–Chang's `T^{c/2−3/4}` and this `τ₂^{3/4}` are the same phenomenon — poles at
   `s = (1+ρ)/2` from `1/ζ` in an `SL(2,ℤ)` Eisenstein decomposition — and Dorigoni–Treilis say so
   themselves. Footnote 5: *"We are extremely grateful to Nathan Benjamin and Cyuan-Han Chang for
   pointing out that such non-perturbative corrections have to be present and for bringing [95] to
   our attention where very similar results were obtained in the spectral decomposition for the
   partition function of certain 2-d conformal field theories."* And §4.2: *"Equation (4.36) is
   directly analogous to the crossing equation (3.22) derived in [95]"*, with [95] =
   Benjamin–Chang [2208.02259](https://arxiv.org/abs/2208.02259). So the correct framing is: *the
   same `SL(2,ℤ)` spectral mechanism appears in a 2d CFT partition function and in a 4d N=4
   integrated correlator; in the 4d case localisation makes the residues explicit, which closes the
   non-degeneracy gap the 2d case had to assume.* That is a contribution, not a duplication.
6. **The mechanism is generic in the `L`-function**, so a Davenport–Heilbronn-style falsification
   control (the move that makes LeClair–Mussardo's Bethe-completeness criterion convincing) would
   pass trivially rather than informatively. Worth doing, worth not overselling.

**Verdict.** It is a well-posed, correct, publishable-shaped reformulation, and it is *unclaimed* —
the Dorigoni–Treilis observation has 7 citations in three years, none in 2026, and nobody has turned
it into an equivalence. It belongs in the Benjamin–Chang / Remmen genre: the equivalence is the
title, and the contribution is something else. Here that something else is exact computability
closing a gap the 2d CFT version had to leave open.

It is **not** a route to a proof, and the cautionary datapoint is close to home: Honda–Yoda's
*"String theory, N=4 SYM and Riemann hypothesis"* ([2203.17091](https://arxiv.org/abs/2203.17091))
is a competent paper in exactly this space that routes through Robin's criterion, and it appears
never to have been published in four years. The failure mode is assuming RH and reporting the
consequence. Any write-up has to run the other way somewhere.

---

## 5. What to do before showing this to anyone

**Step 1 of v1 — "verify the master formula against the printed JHEP paper" — is done (§2).** The
formula is exact; the numerics attached to it were not, and are now corrected (§3.2). What remains:

1. **Reproduce the expansion numerically end to end.** Compute `a₀(4;3/2,3/2|τ₂)` independently at
   small `τ₂` — from the lattice-sum or spectral representation — subtract the power terms and the
   non-perturbative sector, and check the residual against `Σ β_n τ₂^{3/4+iγ_n/2}` with the constant
   `8.07·10⁻⁶`. **Their Figures 2 and 3 are exactly this test** (10 and 50 zeros, `10⁻¹⁹` agreement),
   so the independent value added is the *uniform bound with its constant*, not the check itself.
2. **Decide the simplicity assumption's role.** It enters only through `ζ′(ρ) ≠ 0`. State it as a
   hypothesis rather than burying it; a multiple zero changes the pole order and hence the power of
   `log τ₂`, which is arguably an *additional* observable signature worth spelling out.
3. **Run the Davenport–Heilbronn control** (§4 item 6) and report it honestly as a weak test.
4. **Then** ask the one question that would lift this out of the restatement genre: *is there
   anything in N=4 SYM that constrains the `τ₂ → 0` envelope of the zero-instanton sector?* If the
   answer is yes, the paper is a different and much bigger one. If no — which is my expectation — the
   honest framing is "an exactly-computable reformulation, with the non-degeneracy condition
   discharged," which is a real if modest contribution.

**On sending it to someone.** The natural referee-in-advance is Dorigoni — it is his observation, he
called it mysterious in print, and he has said nothing about it since. With step 1 of v1 now
discharged, sending him a clean statement of the equivalence with the convergence result is a
reasonable thing to do now. Benjamin and Chang are the second obvious recipients, given footnote 5.

---

## 6. Reproduction

| script | produces |
|---|---|
| `n1_residues.py` | §3.2 — residues `β_n` for the first 60 zeros; decay fit; partial sums |
| `n2_checks.py` | §3.1, §3.3, §3.2 — precision stability; non-degeneracy of the four `ξ` factors; converse-direction exponents; absolute convergence and the uniform constant |
| `v_residue.py` | pins the `ξ` convention and verifies the residue structure against the printed kernel |

Dependencies: `mpmath`, `numpy`. See also `ROUND10_boundary_data.md` §2 (the corrected numerics) and
`ROUND11_freeboson_and_positivity.md` §0 (the print verification of eq. (4.31)).

**Sources.** Dorigoni–Treilis [2307.07491](https://arxiv.org/abs/2307.07491) (JHEP 11 (2023) 102),
**§4.2, eqs. (4.20) and (4.31), Figures 1–3, footnotes 5 and 7** — read in full · Treilis, IHES
seminar 18 Oct 2023, and Durham thesis etheses 15640 §5.6 · Dorigoni–Kleinschmidt–Treilis
[2208.14087](https://arxiv.org/abs/2208.14087) · Dorigoni–Treilis
[2405.10204](https://arxiv.org/abs/2405.10204) · Paul–Perlmutter–Raj
[2209.06639](https://arxiv.org/abs/2209.06639) · Benjamin–Chang
[2208.02259](https://arxiv.org/abs/2208.02259) (JHEP 11 (2022) 143) ·
Benjamin–Chang–Fitzpatrick–Ramella [2505.18314](https://arxiv.org/abs/2505.18314) (JHEP 09 (2025)
042) · Remmen [2108.07820](https://arxiv.org/abs/2108.07820) (PRL 127 241602) · LeClair–Mussardo
[2307.01254](https://arxiv.org/abs/2307.01254) (JHEP 04 (2024) 062) · Perlmutter
[2509.21672](https://arxiv.org/abs/2509.21672) · Honda–Yoda
[2203.17091](https://arxiv.org/abs/2203.17091) · Green–Miller–Vanhove (cusp growth lemma) · Sarnak,
*Problems of the Millennium: The Riemann Hypothesis* (Clay, 2004) · Connes
[2602.04022](https://arxiv.org/abs/2602.04022) · Broughan, *Equivalents of the Riemann Hypothesis*
(CUP).
