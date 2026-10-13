# The N=4 SYM seam: the ξ factors cancel in the spectral decomposition

> **SUPERSEDED IN PART — see `NOTE_n4_reformulation.md` (same day).** This note's title and §7
> over-claimed. What is established below is that the *naive* route is dead: the ξ's cancel in the
> `L²` spectral decomposition, and the canonical contour sits at the strip edge. That does **not**
> close the seam. The zeros do appear in the `τ₂→0` asymptotics of the zero-instanton sector, and
> that appearance supports a well-posed RH-equivalence which nobody has written. Read this note for
> §§1–5 and the follow-up for the correction.

**2026-08-25.** Execution of the last unexecuted item on the priority lists: round 2 §8.3 / round 3
§4.3 / round 4 §4 — *does any bootstrap positivity constraint touch the `ξ(2s)` factors in the
`SL(2,ℤ)` spectral decomposition of N=4 SYM integrated correlators?*

**Answer: no, and for two independent reasons, both verifiable from the papers' own equations.**
Round 2's guess ("most likely the ξ factors are pure normalisation and drop out") was right. This
closes the last item on the **Yang–Mills** priority list — not the physics-adjacent space generally,
which §7 shows is now more open than when we started, though not in a direction that reaches RH.

---

## 1. Reason one: the ξ's cancel identically

Paul–Perlmutter–Raj ([2209.06639](https://arxiv.org/abs/2209.06639), JHEP 01 (2023) 149) and
Collier–Perlmutter ([2201.05093](https://arxiv.org/abs/2201.05093), JHEP 08 (2022) 195) both define

- `Λ(s) := π^{−s}Γ(s)ζ(2s)` — this is `ξ(2s)`  (PPR below (2.32); CP (2.12))
- `E*_s := Λ(s)E_s`  (CP (2.15))
- `{𝕆, E_s} := Λ(s)^{−1}(𝕆, E_s)`  (PPR (2.34); CP (2.29))

and the decomposition (PPR (2.29))

`𝕆(τ) = ⟨𝕆⟩ + (1/4πi)∫_{Re s=1/2} ds {𝕆, E_s} E*_s(τ) + Σ_n (𝕆, φ_n) φ_n(τ)`.

The integrand is `{𝕆,E_s}·E*_s = [(𝕆,E_s)/Λ(s)]·[Λ(s)E_s] = (𝕆,E_s)·E_s`. **`Λ(s) = ξ(2s)` appears
once in the numerator and once in the denominator and cancels pointwise.** What remains is textbook
Roelcke–Selberg with the flat Plancherel measure `dt/4π`. The completed normalisation exists solely
to make each factor separately invariant under `s → 1−s` so the contour can be folded; neither paper
offers any physical justification for it.

The physical spectral densities are correspondingly arithmetic-free:

- PPR (3.7): `{G_p^{(N|i,j)}, E_s} = [π/sin πs]·s(1−s)(2s−1)²·g(s)` with `g` a **polynomial**.
- Dorigoni–Treilis ([2405.10204](https://arxiv.org/abs/2405.10204)) (2.28):
  `M_N(s) = [N(N−1)π s(1−s)(2s−1)²/(4 sin πs)]·₃F₂(2−N, s, 1−s; 3, 2 | 1)`.

Gammas, rationals, `sin πs`, a hypergeometric. **No ζ, no ξ, no `1/|ξ(1+2it)|²`, no scattering
matrix, no `φ′/φ`.** Contour deformations in the large-`N`, weak- and strong-coupling expansions pick
up poles at integers and at `s = 0, 1` — never at a zeta zero.

Where `ζ(2s)` comes from physically is also deflating: in a lattice sum,
`Σ_{(m,n)≠0}(τ₂/|m+nτ|²)^s = 2ζ(2s)E_s(τ)`, so the `ζ(2s)` is the Dirichlet factor from summing over
`gcd(m,n)` — the bookkeeping difference between all lattice vectors and primitive ones. That is the
entire arithmetic content of the prefactor.

## 2. Reason two: the physics contour is at the wrong place

Even without the cancellation there would be no lever. On `Re s = 1/2`, `Λ(1/2+it) = ξ(1+2it)` — the
**edge** of the critical strip. Non-vanishing of `ζ` on `Re w = 1` is Hadamard–de la Vallée Poussin
(1896), equivalent to the prime number theorem. The nontrivial zeros sit at `s = ρ/2` with
`Re(ρ/2) ∈ (0, 1/2)` — **strictly off the physics contour**. This is also why the automorphic
scattering matrix `φ(s) = ξ(2s−1)/ξ(2s)` is automatically unimodular on the continuous spectrum:
unitarity of the automorphic S-matrix is worth PNT, not RH.

## 3. The positivity that was hoped for does not exist in the required form

The N=4 bootstrap's positivity is **τ-local**: unitarity on squared OPE coefficients in `(Δ, ℓ)`
space at a fixed point of the conformal manifold (Beem–Rastelli–van Rees
[1304.1803](https://arxiv.org/abs/1304.1803); Chester–Pufu lineage;
[2111.07989](https://arxiv.org/abs/2111.07989)). In that machinery the integrated correlators enter
as **input equalities**, not as objects positivity constrains, and no modular form, Eisenstein series
or zeta function appears in any positivity condition.

No one asserts positivity of an integrated correlator as a function of `τ` on the fundamental
domain, and the Dorigoni–Green–Wen lattice kernel `B_N(t) = Q_N(t)/(t+1)^{2N+1}`
([2102.09537](https://arxiv.org/abs/2102.09537), PRL 126.161601) is a **signed** rational function
with no positivity claim attached.

Two structural reasons no such lever could work anyway:

- **Pointwise positivity is arithmetically empty.** If `𝕆(τ) ≥ 0` on the fundamental domain, one
  learns `(𝕆, E_s) > 0` for real `s ∈ (1/2, 1)`, i.e. information about `ξ(2s)` on a **real**
  segment where non-vanishing is elementary. Complex zeros are not in range.
- **Plancherel positivity is also empty.** Parseval gives a termwise-nonnegative decomposition in
  which `|ξ(1+2it)|² > 0` enters as a positive *factor*. Positivity is insensitive to it.

**And the ceiling is known.** Sarnak's Clay note names exactly this lever and exactly what it buys:
Eisenstein series "have poles at the zeros of `L`-functions (hence the zeros can in this way be
thought of as resonances for a spectral problem)," and "combining this with a positivity argument
using the inner product formula for Eisenstein series ('Maass Selberg Formula') yields **effective
zero free regions in `Re(s) ≤ 1`** for all `L`-functions whose analytic continuation and functional
equations are known." He calls the Eisenstein route "the most powerful one towards GRH" — and its
known ceiling is PNT-strength, not RH. Number theorists have mined that positivity for fifty years.
Any physics positivity acting through the Eisenstein inner product is at best rediscovering it.

## 4. Where the zeta zeros actually do live, and what it is

Dorigoni–Treilis ([2307.07491](https://arxiv.org/abs/2307.07491)) eq. (3.37) has a Mellin–Barnes
kernel with `1/ξ(2−2t)` in the denominator, giving the poles at `Re t = 3/4` "if the Riemann
hypothesis is correct." By the functional equation `ξ(2−2t) = ξ(2t−1)`, which is exactly the
coefficient of `y^{1−t}` in the constant term of `E*_t`. So `1/ξ(2t−1)` is the **inverse of the
constant-term (scattering) data**, and its poles are, under `t ↔ 1−t`, precisely the Lax–Phillips
resonance set `s = ρ/2`.

Two things follow. First, this occurs only in the **zero Fourier mode** — the perturbative,
zero-instanton sector, which is not modular invariant — and only when the contour is deformed **off**
`Re s = 1/2` to build a `τ → 0` expansion. Second, it is not new: it is the automorphic scattering
matrix rediscovered by the back door, in the one place physics is forced to invert it. Lax–Phillips
flagged the obstruction in their own 1976 appendix (Conrey–Li,
[math/9812166](https://arxiv.org/abs/math/9812166): "they explained the difficulty of approaching the
Riemann hypothesis by using the scattering theory"), and Bombieri–Garrett
([2002.07929](https://arxiv.org/abs/2002.07929)) give the modern verdict on all such constructions —
self-adjointness is **permissive, not generative**: it lets spectrum live on the critical line, it
does not force zeros there.

The same factor was found independently in 2d CFT: Benjamin–Chang–Fitzpatrick–Ramella
([2505.18314](https://arxiv.org/abs/2505.18314), JHEP 09 (2025) 042) get the same tower, the same
`3/4`, the same RH caveat — and note the residues `δ_k` are **not positive-definite**, which kills
the positivity route there too.

## 5. The community's own verdict

[2307.07491](https://arxiv.org/abs/2307.07491) has **7 citing records in three years, none in 2026**.
Dorigoni and Treilis applied the identical machinery to the physical correlator in 2024
([2405.10204](https://arxiv.org/abs/2405.10204)) and to heavy operators in 2026
([2602.04963](https://arxiv.org/abs/2602.04963)) with **no mention of zeta zeros in either**.
Dorigoni's September 2025 Durham talk on exactly this material lists three open problems; this is not
among them. The one substantive pickup is in a different corner of physics (2d CFT), and the one
number-theory pickup (Charge–Dixit, [2410.04506](https://arxiv.org/abs/2410.04506)) cites it for a
Bessel-product identity, not for the zeros.

## 6. If anything in this space is live, it is not this

Three items worth knowing, none of them N=4 SYM:

1. **Benjamin–Chang, [2208.02259](https://arxiv.org/abs/2208.02259)** (JHEP 11 (2022) 143), *Scalar
   Modular Bootstrap and Zeros of the Riemann Zeta Function*. In 2d Narain / `U(1)^c` CFT the `Λ`
   factors **do not cancel** — the ratio `Λ((c−1)/2)/Λ(c/2)` persists — and they rephrase RH as a
   statement about the asymptotic density of scalar operators. They then leave the key step open
   verbatim: *"it would be extremely interesting if there were a physical reason why the scalar
   partition function … had to scale as `T^{c/2−3/4}`. This would give a 'physics explanation' of the
   Riemann hypothesis. We leave this problem as an exercise to the reader."* Still unsolved as of
   the 2025 follow-up. **This is the honest version of the question we were asking, in a different
   theory.** Note their logic runs the other way: they use the vanishing of `ζ` to *delete*
   sign-indefinite contributions before applying positivity.
2. **Perlmutter, [2509.21672](https://arxiv.org/abs/2509.21672)** — attaches a self-dual degree-4
   `L`-function to every 2d CFT torus partition function, derives a zero sum rule and a zero-density
   bound from the spectral gap, and explicitly does **not** assume RH. Same author as PPR, having
   crossed into genuine analytic number theory.
3. **Honda–Yoda, [2203.17091](https://arxiv.org/abs/2203.17091)** — the only paper with "N=4 SYM" and
   "Riemann hypothesis" in one title, but the route is **Robin's criterion** via the Schur index, and
   RH is consumed, not produced. Still unpublished.

**Weil positivity remains the real thing and remains open.** Connes' own February 2026 survey
([2602.04022](https://arxiv.org/abs/2602.04022)) states the gap plainly — that the zeros of the
finite Euler products converge to the zeros of zeta "is something which at this point is not
proved" — and mentions no QFT, string theory, or bootstrap anywhere.

## 7. Consequence for the programme — the accurate ledger

*(An earlier draft of this section said "nothing on the geometric or physics side is left open."
That was wrong, and it contradicted findings recorded in this same round. Corrected below into
three columns, because the distinction between them is the whole point.)*

**Column A — closed, with reasons.** The Yang–Mills route specifically:

| item | closed by |
|---|---|
| ADHM/instanton size dictionary | circular; lossy (Rodgers–Tao ↦ `x² ≥ 0`); the deformation that installs dynamics bounds sizes away from zero |
| Undeformed Yang–Mills | no dynamics — instantons are gradient-flow fixed points |
| Non-self-dual YM solutions | discrete classification (`c₂ ≠ ±1`; `(n₋,n₊) ≡ 1 mod 4`); never isolated |
| Vafa–Witten | modularity but no zeros; the arrow runs from the zeta program into gauge theory |
| 2D YM / Witten zeta | special values at even integers, never zeros |
| N=4 SYM Eisenstein / bootstrap positivity | §§1–3 above: `ξ` cancels; contour at the strip edge; Sarnak's ceiling is PNT |
| Existence-statement reframing *as an obstruction question* | no shape obstruction, no type obstruction (`NOTE_existence_loophole.md`) |

**Column B — genuinely open, newly surfaced, and none of them Yang–Mills.** The sweeps this round
turned up four leads that were not previously on our radar. Each is real; none is a route to RH, and
the reason differs in each case:

| lead | what is open | why it is not a route to RH |
|---|---|---|
| Benjamin–Chang [2208.02259](https://arxiv.org/abs/2208.02259), 2d Narain CFT | the `Λ` factors genuinely do **not** cancel; their stated "exercise" — a physical reason for the `T^{c/2−3/4}` envelope — is unsolved after four years | it is a *reformulation*; and the 2025 follow-up finds the residues are not sign-definite, blocking the obvious positivity route |
| ABJM / quantized mirror curves | `Ξ(κ) = det(1+κρ)` is provably Laguerre–Pólya and **nobody has said so**; its `Λ_DN` is undefined | the partition functions are order 2/3, with no functional equation and no Euler product — a new example class for DBN theory, not a bridge to `ξ` |
| Kenyon–Okounkov–Sheffield Harnack/dimer | existence ⟺ total reality, region a closed orthant, in a theory that **is** gauge (brane tilings = 4d `N=1` quivers) | maximal reality of a plane curve is not hyperbolicity of `Ξ`; this is structural analogy, i.e. exactly the round-1 shape-matching failure mode |
| MTV (Annals 170) / Karp Conj. 1.6 / Nekrasov–Shatashvili | Hilbert–Pólya executed successfully via Shapovalov positive-definiteness; the NS translation into gauge-vacua language is unwritten | disqualified by our own marginality screen (§5.3 of the loophole note): it proves reality *with room to spare*, and `Ξ` is a boundary point by Rodgers–Tao |

Perlmutter [2509.21672](https://arxiv.org/abs/2509.21672) belongs alongside these — honest, does not
assume RH, derives zero sum rules and density bounds from spectral gaps — but for degree-4
`L`-functions attached to 2d CFTs, not for `ζ`.

**Column C — open and on the actual critical path.** Round 4's item: derive the edge-law constant
from the GORZ coefficient asymptotics. Plus the detector-paper engineering (interval arithmetic,
`|S(u,χ)|` constants). Both classical analysis, both coefficient-side — which
`NOTE_existence_loophole.md` §6 argues is where they had to be.

**The correct one-line summary is therefore:** *the Yang–Mills route is closed; the physics-adjacent
space is more open than when we started, but nothing in it is a route to RH, and the critical path
runs through classical analysis.* Column B is worth having precisely because two of its four entries
are unremarked results that could be written up on their own terms — not because any of them
revives the programme.

## 8. Sources

Paul–Perlmutter–Raj [2209.06639](https://arxiv.org/abs/2209.06639) · Collier–Perlmutter
[2201.05093](https://arxiv.org/abs/2201.05093) · Dorigoni–Treilis
[2307.07491](https://arxiv.org/abs/2307.07491), [2405.10204](https://arxiv.org/abs/2405.10204) ·
Aprile–Dorigoni–Treilis [2602.04963](https://arxiv.org/abs/2602.04963) · Brown–Dorigoni–Wen
[2603.20083](https://arxiv.org/abs/2603.20083) · Dorigoni–Green–Wen
[2102.09537](https://arxiv.org/abs/2102.09537), [2501.03996](https://arxiv.org/abs/2501.03996) ·
Beem–Rastelli–van Rees [1304.1803](https://arxiv.org/abs/1304.1803) ·
[2111.07989](https://arxiv.org/abs/2111.07989) · Benjamin–Chang
[2208.02259](https://arxiv.org/abs/2208.02259) · Benjamin–Chang–Fitzpatrick–Ramella
[2505.18314](https://arxiv.org/abs/2505.18314) · Perlmutter
[2509.21672](https://arxiv.org/abs/2509.21672) · Honda–Yoda
[2203.17091](https://arxiv.org/abs/2203.17091) · Remmen
[2108.07820](https://arxiv.org/abs/2108.07820) · Charge–Dixit
[2410.04506](https://arxiv.org/abs/2410.04506) · Bombieri–Garrett
[2002.07929](https://arxiv.org/abs/2002.07929) · Conrey–Li
[math/9812166](https://arxiv.org/abs/math/9812166) · Connes–Consani
[2006.13771](https://arxiv.org/abs/2006.13771) · Connes
[2602.04022](https://arxiv.org/abs/2602.04022) · Sarnak, *Problems of the Millennium: The Riemann
Hypothesis* (Clay, 2004) · Bombieri, *Problems of the Millennium: the Riemann Hypothesis* (Clay).
