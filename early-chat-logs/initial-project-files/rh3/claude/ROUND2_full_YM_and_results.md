# Round 2: full Yang–Mills, a corrected dictionary, and four computational results

**2026-08-24.** Follow-up to `ASSESSMENT_instanton_size.md`. Everything numerical below was
computed here; scripts listed in §7. Two literature sweeps were run in parallel and are cited
inline.

**Headline.** The broadening to full Yang–Mills was the right call, but not for the reason either
of us expected. It does not rescue the size dictionary — it *replaces* it. There is an exact,
verified dictionary in which the zeros of a real polynomial are the spectrum of a matrix on
**Calogero–Moser space** — which *is* the noncommutative U(1) instanton moduli space — and in which
the De Bruijn–Newman flow is a **straight line** in that space. The brief was reading the right
geometry in the wrong slot.

---

## 1. Why ADHM forced the failure — the one-sentence diagnosis

In ADHM the position matrices `a'_n` are **Hermitian by construction**. Their spectrum is therefore
automatically real. So the imaginary part of a zero has nowhere to go except the size block `w` —
and `w` is a free modulus.

> **The reality constraint built into the self-dual sector pushes the non-reality into the one slot
> the theory refuses to constrain. That is the whole failure, and it is a property of the instanton
> sector, not of Yang–Mills.**

This reframes the question productively: *what do you have to relax to let the non-reality live in
the spectrum, where Hilbert–Pólya says it belongs?* Answer, verified below: turn on the
noncommutativity parameter, which is exactly the deformation the brief identified in §6.4 and read
as a dead end.

---

## 2. The corrected dictionary — verified, exact

### 2.1 The identity

Let `p₀` be monic of degree `n` with distinct roots `z₁,…,z_n`. Define

> `X = diag(z₁,…,z_n)`,  `Y_{jk} = 2/(z_j − z_k)` for `j ≠ k`,  `Y_{jj} = Σ_{k≠j} 2/(z_j − z_k)`.

Then `[X,Y] + 2·1 = 2·J` (all-ones), which is **rank one** — the Calogero–Moser condition. And:

> **`e^{−t ∂_z²} p₀(z) = det(z·1 − X − tY)`  for all `t`.**

Verified to machine conditioning at `n = 2,…,6`, over real and complex-conjugate root
configurations, at four times each (max coefficient error `1.6e−14` at `n=2` rising to `3.4e−8` at
`n=6`, entirely from the ill-conditioned root→coefficient map). `rank([X,Y] + 2·1) = 1` at every
sample. I proved the `n = 2` case by hand: the pencil reproduces the heat flow iff the off-diagonal
coefficient is exactly `±2`.

**Consequences.**

- The De Bruijn–Newman flow is the **straight line** `X + tY` in Calogero–Moser space.
- `Λ(p₀) = inf{ t : spec(X + tY) ⊂ ℝ }`.
- Hyperbolicity is the reality of the spectrum of a **non-Hermitian** matrix — a genuine condition,
  not a statement about a free parameter.

### 2.2 The flow is Calogero–Moser, exactly

The induced root dynamics `ż_j = 2Σ_{k≠j}(z_j − z_k)^{−1}` (Rodgers–Tao Thm 11, eq. 56) satisfies,
verified to `4e−16` at `n = 3,4,5,6,8`:

> `z̈_j = −8 Σ_{k≠j} (z_j − z_k)^{−3}` — the **rational Calogero–Moser system with negative
> coupling**, restricted to the Lagrangian section `p = −∇W`.

And on the real locus the flow is *exactly* gradient descent of `W = −Σ_{j<k} log|x_j − x_k|²`
(verified to `0.000e+00`). Hall–Ho, [arXiv:2202.09660](https://arxiv.org/abs/2202.09660), state the
CM reduction; the pencil identity in §2.1 I did not find in the literature, though Wilson's
linearisation of CM makes it unsurprising.

### 2.3 Where this lands geometrically

Per the literature sweep (Wilson, *Invent. Math.* **133** (1998) 1–41; Etingof
[math/0606233](https://arxiv.org/abs/math/0606233); Nakajima ULS 18; Nekrasov–Schwarz
[hep-th/9802068](https://arxiv.org/abs/hep-th/9802068); Gorsky–Nekrasov–Rubtsov
[hep-th/9901089](https://arxiv.org/abs/hep-th/9901089)):

| `ζ` | space |
|---|---|
| `ζ = 0`, no stability | `Sym^k(ℂ²)`, singular |
| `ζ_ℝ > 0`, `ζ_ℂ = 0` | `Hilb^k(ℂ²)` — Nekrasov–Schwarz noncommutative U(1) instantons |
| `ζ_ℂ ≠ 0` | **Calogero–Moser space `𝒞_k`** — smooth affine, `dim 2k` |

Wilson §8: `𝒞_k` and `Hilb^k(ℂ²)` are the *same hyperkähler manifold in different complex
structures* on the twistor sphere. So the geometry carrying the zeta zeros and their flow is, up to
hyperkähler rotation, the charge-`k` noncommutative instanton moduli space.

**One correction to the brief, in its favour and then against it.** The brief's §6.4 bound
`|w|² ≥ |ζ⃗|` was derived only at `k = 1`. It is general: tracing `[X,Y] + ij = ζ_ℂ·1` gives
`tr(ij) = kζ_ℂ ≠ 0`, so `i ≠ 0` and `j ≠ 0` **at every point of `𝒞_k`, for every `k`**. Under the
brief's own dictionary the sizes can never vanish anywhere on the CM branch — the relabelling lands
on a space where the desired conclusion is identically false, not merely unconstrained.

### 2.4 Why this still is not a proof

`det(z − X) = p(z)`, so "spec `X` real" is still "roots of `p` real". What is *added* is real but
bounded: a symplectic space with an integrable system on which the DBN flow is linear. Push it to a
criterion and you get

> RH ⟺ there is a positive-definite `H` with `HX` Hermitian,

which is Hilbert–Pólya — and the `H` that works is the **Hermite/Bezoutian form**. The corrected
dictionary is a better-furnished room in the same building. It is worth having because it is exact,
it carries the flow, and it is not circular in the fatal way the size reading was. It is not a
mechanism.

---

## 3. Full Yang–Mills: the landscape, ranked

Findings from a systematic sweep. Only one item is a live seam.

### 3.1 Dead, and now provably so: the undeformed theory has no dynamics

On a closed 4-manifold `YM(A) = 8π²|k| + ‖F∓‖²`, so instantons are **absolute minima**, hence
**fixed points of the Yang–Mills gradient flow** `∂_tA = −d_A*F`. The flow is exactly constant on
instanton moduli space; it moves nothing. There is no other canonical flow beyond isometries and
the hyperkähler structure.

> This is why §2 needs `ζ ≠ 0`. The only way to get dynamics is to deform, and the deformation that
> supplies it is the same one that makes the sizes non-vanishing. **The two facts are one fact.**

### 3.2 Dead: non-self-dual Yang–Mills solutions

Sibner–Sibner–Uhlenbeck ([PNAS 86 (1989) 8610](https://www.pnas.org/doi/10.1073/pnas.86.22.8610))
prove existence on `S⁴` by a **non-constructive** equivariant min-max. Sadun–Segert (CMP 145 (1992)
363) and Bor (CMP 145 (1992) 393) classify SO(3)-equivariant families by holonomy parameters
`(n₋,n₊) ≡ 1 mod 4` with `c₂ = (n₋²−n₊²)/8`. But: no ADHM-like classification, no determinant or
product formula, no known discreteness of the action spectrum, and the solutions are **never
isolated** (the conformal group of `S⁴` is 15-dimensional, so every solution sits in an orbit).

The hope that non-minimal solutions supply *rigidity* where instantons supply freedom is reasonable
and does not survive contact with what is known. Nothing to build on.

### 3.3 Real arithmetic, no zeros: Vafa–Witten modularity

Vafa–Witten ([hep-th/9408074](https://arxiv.org/abs/hep-th/9408074)): the twisted N=4 partition
function is a vector-valued modular form of weight `−χ/2`, with `S` mixing 't Hooft fluxes by
discrete Fourier transform; often **mock** modular when `b₂⁺ = 1`. Rigorous versions:
Tanaka–Thomas [1702.08487](https://arxiv.org/abs/1702.08487), Göttsche–Kool
[1703.07196](https://arxiv.org/abs/1703.07196), Manschot [1709.10098](https://arxiv.org/abs/1709.10098).

The only zeta contact is **Males–Ono et al.**, [arXiv:2204.05465](https://arxiv.org/abs/2204.05465),
proving that Vafa–Witten invariants of K3 satisfy all higher-order **Turán inequalities** — using
the Griffin–Ono–Rolen–Zagier machinery. That is an inherited toolkit, not a link: the arrow runs
from the zeta program to gauge theory, not back. Nobody has attached an L-function to a VW
partition function.

### 3.4 The live seam: N=4 SYM, S-duality, and Eisenstein series

The coupling `τ` of N=4 SYM lives on `SL(2,ℤ)\ℍ`. Instanton sums in the effective action give
non-holomorphic Eisenstein series (Green–Gutperle `E_{3/2}`; Green–Vanhove). The completed series
`E*_s = ξ(2s)E_s` has constant term `ξ(2s)y^s + ξ(2s−1)y^{1−s}`, so the automorphic scattering
matrix is

> `φ(s) = ξ(2s−1)/ξ(2s)`,  whose poles sit at `s = ρ/2` for `ζ(ρ) = 0`.

**The physicists have already walked into this.** Dorigoni–Treilis,
[arXiv:2307.07491](https://arxiv.org/abs/2307.07491), JHEP 11 (2023) 102, study generalised
Eisenstein series solving `(Δ−λ)f = E_{s₁}E_{s₂}` that arise directly in the large-`N` expansion of
N=4 SYM **integrated correlators**. Their Mellin–Barnes representation has a contour picking up
"an infinite family of poles with `Re(t) = 3/4` (if the Riemann hypothesis is correct) coming from
the non-trivial zeroes of the Riemann zeta." They call it "surprising and quite mysterious" and
drop it. Paul–Perlmutter–Raj, [arXiv:2209.06639](https://arxiv.org/abs/2209.06639), do the full
`SL(2,ℤ)` spectral decomposition of these correlators and never mention zeta.

This has everything ADHM lacked: it is infinite-dimensional, it carries modularity, the same domain
is simultaneously the S-duality domain and the automorphic one, and the zeros appear as *spectral
data* rather than as a shape match.

**The honest caveats, which are serious.** (i) In Dorigoni–Treilis the zeros are *consumers* of RH —
they assume it to place a contour — not producers. (ii) The underlying framework, Lax–Phillips /
Faddeev–Pavlov scattering on the modular surface, is a correct but **dead** reformulation: the
Lax–Phillips semigroup is a *contraction*, so its spectrum is confined to a half-plane, which
reproduces only the classical zero-free region; forcing resonances onto a line requires a positivity
the automorphic setup does not supply. Tellingly, **neither Bombieri's nor Sarnak's Clay exposition
treats Lax–Phillips as an approach**; Connes replaced resonances with an absorption spectrum
precisely to sidestep this, and that stalls at an unproven trace formula
([math/9811068](https://arxiv.org/abs/math/9811068)).

### 3.5 Not a route: 2D Yang–Mills

I over-weighted this initially and was wrong. The real statement: at zero area
`Z_G(Σ_g) = Σ_π (dim π)^{2−2g}` is the **Witten zeta function**, and for `SU(2)` it is *literally*
`ζ(2g−2)` — but that is special values at even integers, never zeros. The torus theta observation
is correct (`Σ_n e^{−εAn²/2}` is Jacobi theta, area inversion is the modular transformation) and
nobody has written the Mellin step, and I now expect it to be vacuous: it is Riemann's 1859
derivation in gauge-theory costume, with no new input.

### 3.6 Nothing else

The two standard surveys of physics-and-RH — Schumayer–Hutchinson,
[arXiv:1101.3116](https://arxiv.org/abs/1101.3116), *Rev. Mod. Phys.* **83** (2011) 307, and Sierra,
[arXiv:1012.4264](https://arxiv.org/abs/1012.4264) — **do not mention Yang–Mills or gauge theory
anywhere**. Numerous 2024–2026 "spectral-geometric proofs of RH" on Zenodo/academia.edu are outside
credible venues; disregard.

---

## 4. What a faithful dictionary must carry — now known precisely

Rodgers–Tao's proof of `Λ ≥ 0` ([1801.05914](https://arxiv.org/abs/1801.05914)) is the benchmark,
and its structure tells us exactly what geometry can and cannot supply. Assume `Λ < 0`; then
`∂_tH = −4E` with `E = Σ_{k≠k'}|x_k−x_{k'}|^{−2} ≥ 0`, and Riemann–von Mangoldt plus Littlewood pin
`H` at both ends, forcing `∫E dt` finite and hence the zeros into **local equilibrium** — locally an
arithmetic progression at the mean spacing. The contradiction comes from **pair correlation**:
Montgomery plus the Conrey–Ghosh–Goldston–Gonek–Heath-Brown second moment show the gaps have
positive-proportion variance, i.e. the zeros are *less* rigid than equilibrium demands.

So a faithful dictionary needs:

1. the gradient/monotone structure `∂_tH = −4E`, `E ≥ 0`;
2. a two-sided count of zeros (Riemann–von Mangoldt);
3. **a lower bound on `E` — an anti-rigidity statement.**

The Calogero–Moser dictionary supplies (1) exactly and beautifully — it *is* the gradient flow of
the log-gas energy, and it is linear in the geometry. It supplies nothing for (2) or (3).
**(3) is irreducibly arithmetic**, and it is the step that carries the proof.

---

## 5. The GUE test: I predicted wrong, and the way it failed is informative

I predicted the geometry would not reproduce Montgomery–Odlyzko. It does.

**Result 1 — the induced measure.** The flat ADHM measure restricted to the commuting locus (where
real roots exist at all) induces on the instanton centres exactly

> `∏_{i<j} |X_i − X_j|²  d⁴X` — a **β = 2 Coulomb gas in ℝ⁴**.

Verified by computing the Gram determinant of the parametrisation Jacobian: the ratio to
`∏|X_i−X_j|²` is constant to `2e−16`, `7e−16`, `2e−15` at `k = 2,3,4` (the constant is
`2^{k(k−1)/2}`). Restricted to collinear centres this is `∏|τ_i−τ_j|²` — precisely GUE.

**Result 2 — the spacing comparison.** Unfolded nearest-neighbour spacings, β=2 gas vs. 400 actual
zeta zeros near `n = 1000`:

| `s` | β=2 gas | zeta zeros | Poisson |
|---|---|---|---|
| 0.10 | 0.048 | 0.000 | 0.934 |
| 0.50 | 0.578 | 0.389 | 0.632 |
| 0.90 | 0.962 | 1.065 | 0.433 |
| 1.30 | 0.626 | 0.627 | 0.289 |
| 1.90 | 0.113 | 0.113 | 0.156 |

`L¹` distance to zeta: **β=2 gas 0.135, Poisson 0.876.** `P(s<0.2)`: gas 0.0095, zeta 0.0000,
Poisson 0.179.

**Why the pass carries no information.** It happens because ADHM positions are eigenvalues of
Hermitian matrices, and β=2 repulsion is a universal consequence of that — the same reason *every*
random-matrix model matches. And the measure is **non-normalizable**: the geometry supplies no
confining potential, hence no density. Zeta needs density `(1/2π)log(T/2π)`, which is the
non-universal, arithmetic part.

> **The geometry hands you the universal half of Montgomery–Odlyzko for free and the arithmetic half
> not at all.**

Note this is *exactly* item (3) of §4 again, arrived at independently: what Rodgers–Tao need from
arithmetic is a **deviation** from log-gas equilibrium. The geometry gives you the equilibrium. The
proof needs the deviation. Three independent lines — circularity, faithfulness, and now a
measurement — converge on the same boundary.

---

## 6. The `(d,n)` margin map — the one result with standalone value

### 6.1 Setup and an exact benchmark

Moments `M_{2m} = ∫₀^∞ Φ(u)u^{2m}du` computed to 240 digits on a shared 1344-node composite
Gauss–Legendre grid (agreement with adaptive quadrature: `1.6e−206` at `m=1`, `2.9e−135` at
`m=240`). Calibration: **`4M₀` matches `ξ(1/2)` to 208 digits.** (Note: the brief's §1.1 reports
`ξ(1/2) = 0.4971207174`, which is wrong in the 8th digit — the correct value is `0.49712077818831…`,
and the brief's own computed `4M₀` was right. The reported discrepancy was an artefact of a bad
reference value.)

Margin definition: normalise `J^{d,n}` affinely so its roots have mean 0 and variance 1, then take
the De Bruijn–Newman threshold `Λ` (negative = room to spare). The benchmark is Hermite, and it has
a closed form. Since `H_d(x) = e^{−(1/4)∂²}(2x)^d` and `Var(roots of H_d) = (d−1)/2`:

> **`Λ(normalised H_d) = −1/(2(d−1))`**

Verified exactly at `d = 2,3,4,6,8,12,16`.

### 6.2 The map

Entries are `Λ(normalised J^{d,n}) / Λ(normalised H_d)`. **1.000 = exactly as far from the
hyperbolicity boundary as Hermite; negative would mean not hyperbolic.**

```
   n =      0      1      2      3      5      8     12     20     32     50     80    120    170    220
 d= 2   1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000
 d= 3   0.9026 0.8740 0.8574 0.8469 0.8354 0.8287 0.8271 0.8305 0.8381 0.8481 0.8604 0.8716 0.8813 0.8884
 d= 4   0.8371 0.7853 0.7587 0.7427 0.7259 0.7168 0.7152 0.7216 0.7343 0.7506 0.7704 0.7885 0.8042 0.8156
 d= 6   0.6416 0.6559 0.6161 0.5956 0.5758 0.5666 0.5670 0.5783 0.5976 0.6217 0.6507 0.6773 0.7004 0.7173
 d= 8   0.4878 0.5322 0.5133 0.4915 0.4727 0.4655 0.4682 0.4830 0.5064 0.5350 0.5695 0.6012 0.6289 0.6493
 d=10   0.3819 0.4186 0.4360 0.4130 0.3960 0.3912 0.3958 0.4132 0.4391 0.4705 0.5085 0.5436 0.5744 0.5971
 d=12   0.3057 0.3381 0.3769 0.3519 0.3369 0.3340 0.3402 0.3592 0.3866 0.4198 0.4600 0.4974 0.5304 0.5549
 d=16   0.2063 0.2325 0.2582 0.2643 0.2521 0.2522 0.2601 0.2807 0.3093 0.3440 0.3865 0.4266 0.4624 0.4892
```

### 6.3 What it shows

**(a) Everything is hyperbolic.** No `(d,n)` in range is non-hyperbolic — a separate scan found
`J^{d,n}` hyperbolic for every `n ≤ 240−d` at every `d ≤ 14`, extending the Griffin–Ono–Rolen–Zagier
`d ≤ 8` result numerically (not a proof; their theorem covers all `n`, my scan does not).

**(b) The worst case is at moderate `n`, not at either end.** Every row dips to a minimum near
`n ≈ 8–12` and recovers. The recovery toward 1.000 is the GORZ convergence to Hermite, visible
directly — which also confirms the normalisation is the right one. **The hard region of the Pólya
program is neither small `n` nor the asymptotic regime; it is the crossover.**

**(c) The decay is polynomial, not exponential — the good case.**

| `d` | `min_n` margin | `d × min` | local log-log slope |
|---|---|---|---|
| 4 | 0.7152 | 2.86 | −0.505 |
| 6 | 0.5666 | 3.40 | −0.574 |
| 8 | 0.4655 | 3.72 | −0.683 |
| 10 | 0.3912 | 3.91 | −0.779 |
| 12 | 0.3340 | 4.01 | −0.867 |
| 16 | 0.2521 | 4.03 | −0.978 |

The slope converges to `−1` and `d × min` saturates at ≈ **4.03**. So

> `min_n Λ(normalised J^{d,n}) ≈ −4/d × 1/(2(d−1)) ≈ −2/d²`.

**This is the shape question I said was worth answering, and the answer is the encouraging one.**
An exponentially shrinking margin would mean the Pólya route is hopeless — any uniform-in-`d`
argument would need exponentially strong control. A `d^{-2}` margin means there is no cliff: the
hyperbolicity of `J^{d,n}` degrades only polynomially, and a uniform argument needs polynomial
control of the moments. That is the regime where GORZ-style asymptotics with effective error terms
could in principle be pushed.

Caveats: `d ≤ 16`, `n ≤ 220`, and the `1/d` law is an empirical saturation, not derived. The natural
next step is to derive `min_n Λ ≈ −2/d²` from the GORZ Hermite asymptotic with explicit error terms;
if the derivation works, it converts the fitted constant into a theorem and makes the uniformity gap
quantitative.

---

## 7. Revised verdict

Unchanged in conclusion, sharpened in content and now more useful.

1. **The size dictionary is dead**, and more decisively than in round 1: on the Calogero–Moser
   branch — the only branch with dynamics — `tr(ij) = kζ_ℂ ≠ 0` forces the sizes to be non-vanishing
   at every point, for every `k`.
2. **There is a correct dictionary in the same geometry**, exact and verified: the DBN flow is a
   straight line `X + tY` on Calogero–Moser space = noncommutative U(1) instanton moduli, and
   `Λ(p) = inf{t : spec(X+tY) ⊂ ℝ}`. The brief had the right space and the wrong slot.
3. **That dictionary is Hilbert–Pólya with better furniture, not a mechanism.** The positive-definite
   `H` making `HX` Hermitian is the Bezoutian.
4. **Full Yang–Mills changes the diagnosis but not the verdict.** Undeformed YM has no dynamics at
   all (instantons are gradient-flow fixed points). Non-self-dual solutions have no structure to
   use. Vafa–Witten has modularity but no zeros. Only the N=4 SYM / Eisenstein seam is live, and it
   currently consumes RH rather than producing it.
5. **Three independent lines now converge on the same boundary**: circularity (round 1),
   faithfulness (Rodgers–Tao becomes `x² ≥ 0`), and measurement (the geometry gives the log-gas
   equilibrium; the proof needs the arithmetic deviation from it).

---

## 8. What I would do next, in priority order

**1. Write up the pencil identity (§2.1). Days.** `e^{−t∂²}p(z) = det(z − X − tY)` with the explicit
CM data, plus `Λ(p) = inf{t : spec(X+tY) ⊂ ℝ}`. Check against Wilson's linearisation and the
Hall–Ho paper first — the CM reduction of the flow is known, so the pencil form may be too, but I
did not find it stated. Even if known it is worth having written down in this form, because it is
the correct replacement for the brief's §4 and it is the natural bridge to hyperbolic-pencil theory
(Helton–Vinnikov, the Lax conjecture).

**2. Derive `min_n Λ(J^{d,n}) ≈ −2/d²` from the GORZ asymptotic. Weeks.** This is the highest-value
item. It converts a fitted constant into a quantitative statement of the uniformity gap — the thing
that actually stands between the Pólya program and RH. I can extend the map to `d ≤ 40` and
`n ≤ 1000` first to firm up the law; the moment machinery is built and fast.

**3. Ask the one unasked question on the live seam. Speculative but cheap to scope.** N=4 SYM
integrated correlators are spectrally decomposed on `SL(2,ℤ)\ℍ` (Paul–Perlmutter–Raj), and the
Eisenstein contribution carries `1/ξ(2s)`. The conformal bootstrap imposes **positivity** on these
correlators. Does any bootstrap positivity constraint touch the `ξ(2s)` factors? Physics-side
rigidity — unitarity, positivity of spectral densities — is precisely the kind of thing §6.5 of the
round-1 assessment said to look for, and as far as the sweep found, nobody has asked. Most likely
the `ξ` factors are pure normalisation and drop out. Worth one careful afternoon to find out, and
Dorigoni is the person who would know.

**4. Do not pursue:** non-self-dual YM solutions, 2D YM / Witten zeta, Vafa–Witten L-functions, or
any further variation on matching a finite determinant to `Ξ`. §3 closes each.

---

## 9. Reproduction

| script | produces |
|---|---|
| `pencil.py` | §2.1, the CM pencil identity |
| `cmflow.py` | §2.2, the second-order CM reduction and the gradient structure |
| `gue.py`, `gue2.py` | §5, the commuting-locus Jacobian and the spacing comparison |
| `moments2.py` | the 240-digit moment table (`gamma.pkl`), ~28 s |
| `jensen.py` | §6.3(a), the hyperbolicity scan |
| `margin.py`, `fit.py` | §6.1–6.3, the Hermite benchmark, the margin map, the decay fit |

Dependencies: `numpy`, `scipy`, `sympy`, `mpmath`.
