# The Jet Order Is Exactly Two, and Why That Makes Witten 1978 the Right Reference

*Working memo #9 — August 23, 2026. Follows memo 8. Answers the question memo 8 left open — how close to the slice may the extra point be? — and evaluates the ambitwistor/infinitesimal-neighbourhood lead against the brief's screening checklist. Certified by `lab_jet_order.py`; literature claims flagged individually.*

---

## 0. Result

Memo 8 showed that a one-slice condition is blind, and that one slice **plus one finite off-slice point** already forces `S = 0`. The point can be taken infinitesimally close, so the real question is the **order of the transverse jet**. It has an exact answer.

> **Theorem (jet order).** Inside the R1 family, the deficit `det M − P_p` is an even polynomial in the transverse distance `ν` with no constant term. Its lowest nonvanishing order is `ν²`, with
> $$\det M - P_p = 4\nu^2\, R_0 \sum_p \sigma_p^2 \prod_{q\neq p}\big(B_{q,0}^2 - 4t^2\sigma_q^2\big) + O(\nu^4),$$
> where `R_0 = ∏_{real roots}(A + t²)`, `B_{j,0} = A_j + t² + σ_j²`, `A_j = (x_0−τ_j)²`. Every factor is strictly positive, so the `ν²` coefficient is `> 0` unless every `σ_p = 0`.

So the ladder is:

| condition | what it forces |
|---|---|
| the slice `Π_e` itself | nothing — every real monic `p` (memo 8) |
| the **1st** infinitesimal neighbourhood `Π_e^(1)` | **still nothing** — the deficit has no linear transverse term at all |
| the **2nd** infinitesimal neighbourhood `Π_e^(2)` | `S = 0`, i.e. `p` hyperbolic — total collapse |

**Two is the answer, and there is nothing between one and two.** The transverse Hessian of the deficit *is* the discriminant: it is isotropic of rank 2 — exactly the two sphere directions equivariance quotients out, and the same `2` as the `−(2/r)B` Vekua trace term — and it is positive definite iff `S ≠ 0`.

**On the Witten lead: the resonance is real, and it is not the part one hopes for.** Witten 1978 / Isenberg–Yasskin–Green 1978 do exactly what the intuition says — they trade slice-level data for formal-neighbourhood data, and Witten's `N=3` super-formulation replaces the thickening by odd directions. But per Atiyah–Dunajski–Mason, Witten's supersymmetric version *reformulates* the third-order extension condition; it does not add to it. So **supersymmetric data is a bookkeeping device for jet data, not a new source of information** — which is the correct thing for it to be, and it means the intuition should be read as "you need the transverse 2-jet", which we have now proved and quantified.

**What genuinely imports from Witten is not the thickening but the direction of the logic.** In the ambitwistor correspondence the bundle on the un-thickened space imposes **no field equations at all**, and the Yang–Mills equations appear as the **obstruction to extending** to higher order. That is precisely the shape the brief §1.4 and §7.1 ask for — cheap existence, isolation/discrimination as a theorem — and it is the opposite of every dictionary this programme has tried, all of which *imposed* the condition as a matching. §5 below develops the translation and §6 records one structural finding that came out of it for free.

**What it does not do: it does not rescue matching.** The order-2 condition collapses the data exactly as a single finite point does (§3). Screen 7 of the checklist holds at the level of jets too. And nothing here touches rationality (§6.5 of the brief).

---

## 1. The question, made precise

Fix a unit imaginary `e`, the slice `Π_e = {x_0 + y e}`, and for `q ∈ H` write

```
Im q = t e + n ,   n ⊥ e ,   t = <Im q, e> ,   nu = |n| ,   r^2 = t^2 + nu^2 .
```

So `ν` is the distance from `q` to `Π_e`, and memo 8's discriminant is `r² − t² = ν²` — **the squared distance to the slice, nothing else**. That already suggests the answer, and makes the question the right one to ask: the deficit is a function that vanishes on `Π_e`, so ask to what order.

Formally, the `m`-th infinitesimal neighbourhood condition is

> **J`m`.** `det(Δ†Δ) = P_p` on `Π_e`, together with agreement of all transverse partial derivatives up to order `m`.

`J0` is memo 8's R1. `J1`, `J2` are the new conditions. `P1` is memo 8's "slice plus one finite point".

Why the structure is simple, before any computation: within R1, `T_a = e_a S`, so `Σ_{a≥1} x_a T_a = t S` and

```
M(q) = C + s I - 2 x_0 T_0 - 2 t S ,     s = |q|^2 = x_0^2 + t^2 + nu^2 ,
```

i.e. `det M` depends on `q` only through `(x_0, t, ν²)`, while `P_p` depends only on `(x_0, t² + ν²)`. Two consequences fall out immediately and are worth stating separately because they are the whole content:

- the deficit is **even** in `ν` — so *no odd order can ever contribute*, and in particular the first neighbourhood is blind for a structural reason, not an accident;
- the deficit is **isotropic** in the transverse 2-plane — it depends on `n` only through `|n|`, so the transverse Hessian is a multiple of `I_2` and there is exactly one number at order 2.

## 2. The jet-order theorem

Pair the conjugate roots (memo 8 §2 forces `σ → −σ` invariance of the joint spectrum). With `B_j = A_j + t² + ν² + σ_j²`:

```
det M = R * prod_pairs ( B^2 - 4 t^2      sigma^2 ) ,
P_p   = R * prod_pairs ( B^2 - 4 (t^2+nu^2) sigma^2 ) ,   R = prod_real (A + t^2 + nu^2)
```

Corresponding factors differ by **exactly `4 ν² σ²`** — the `B`'s are identical on the two sides, so the entire `ν`-dependence of the difference is explicit. Telescoping `∏F − ∏G = Σ_p (F_p − G_p) ∏_{q<p}G_q ∏_{q>p}F_q` and setting `ν = 0` in the cofactors gives the stated formula. Positivity of the cofactors is memo 8's identity

```
B_0^2 - 4 t^2 sigma^2  >=  B_0^2 - 4 r^2 sigma^2 = (A + (t-sigma)^2)(A + (t+sigma)^2) > 0 ,
```

so `c_2 > 0` iff some `σ_p ≠ 0` iff `S ≠ 0` iff `p` is not hyperbolic. `∎`

*Verified.* `lab_jet_order.py` Part 1: exact symbolic check for 1 and 2 conjugate pairs with 0, 1, 2 real roots — in every case the `ν`-powers present are `{2, 4, …}` only, the `ν¹` coefficient is identically `0`, and the `ν²` coefficient equals the closed form exactly. Part 2: numeric Taylor coefficients from the same `detM`/`P_target` code the earlier memos used — `c_0, c_1, c_3 ~ 10^{-13}` or smaller across the standard test set, `c_2` matching the closed form to `10^{-11}` relative or better (`4.000000` for `z²+1`, `3.000000` for `z²+z+1`, `39.088800` for `(z−1)((z+2)²+9)`, `58.310913` for `(z²+1)(z²+4)`, `0.622363` for the memo-5 quartic, and `0.000000` for both hyperbolic controls). Transverse isotropy verified to `10^{-13}` over 7 directions. Part 4: `c_2` sampled at 400 random slice points per case — strictly positive minimum in every non-hyperbolic case (`4.000` for `z²+1`, where it is constant in `(x_0,t)`; `8.7e−02` for `(z−1)((z+2)²+9)`; `7.7e−04` for the memo-5 quartic), identically zero in the hyperbolic ones.

The memo-5 quartic's `c_2 = 0.62` against `4.00` for `z²+1` is the expected near-miss behaviour: its conjugate pair sits at `±0.0088` after normalisation, and `c_2` is quadratic in the `σ_p`.

## 3. The ladder, searched over the full data

Solved by least squares from random starts over the **full** admissible ADHM data — the R1 family is an output, not an input.

| `p` | J0 (slice) | J1 (1st nbhd) | J2 (2nd nbhd) | P1 (slice + point) |
|---|---|---|---|---|
| `z²+1` (NOT hyp) | 2.3e−15 | 1.7e−12 | **4.37** | 4.4e−01 |
| `z²+z+1` (NOT hyp) | 4.7e−15 | 2.6e−12 | **2.60** | 9.2e−02 |
| `z²−1` (hyperbolic) | 3.5e−15 | 1.6e−12 | 9.8e−06 | 1.8e−15 |
| `(z−1)(z−2)` (hyp) | 2.9e−14 | 1.3e−11 | 2.3e−03 | 2.6e−14 |

Three readings.

**(i) J1 = J0 exactly.** The first neighbourhood is satisfiable for non-hyperbolic `p` to the same precision as the slice alone. The first-order transverse data is not merely weak; by evenness it is *identically zero on both sides*, so it is not data at all.

**(ii) J2 collapses, and harder than a finite point does.** The non-hyperbolic J2 residuals (`4.37`, `2.60`) are *larger* than the corresponding one-finite-point residuals (`0.44`, `0.092`). The infinitesimal condition is the stronger one — it is imposed at every point of the slice at once, whereas a single finite point is one equation.

**(iii) Caveat on the hyperbolic J2 column.** The jet residuals use central differences with `h = 1e−3`, so a residual `|S|` is amplified by `h^{-2} = 10^6`. The hyperbolic entries `9.8e−06` and `2.3e−03` are therefore optimiser-convergence artifacts (`|S|` reached `5.4e−07` and `2.4e−03`), not signal. The separation here is 3–6 orders rather than the 10–12 of the cleaner tests. The claim rests on Part 1's exact symbolic identity; Part 3 is confirmation of the *direction*, not the precision.

## 4. What Witten 1978 actually says

Checked against the literature; confidence flagged per item, because the numbers matter and there is a specific trap.

**Confirmed.** Ambitwistor space `A` — the space of complex null geodesics of complexified Minkowski space — is the quadric `Z·W = 0` inside `PT × PT* = P³ × P³*`. It has complex dimension 5 and is a **hypersurface**, codimension 1, in the 6-fold. *(Mason–Skinner, hep-th/0510262; Atiyah–Dunajski–Mason, arXiv:1704.07464.)*

**Confirmed (three independent sources).** The correspondence has two steps:

1. A holomorphic bundle on `A` with trivial `c_1`, `c_2` determines and is determined by a **generic analytic connection** — *no field equations whatsoever*.
2. That connection satisfies the **full Yang–Mills equations iff the bundle extends to the THIRD formal neighbourhood** `A_(3)` of `A` in `PT × PT*`.

*(Witten, Phys. Lett. B 77 (1978) 394; Isenberg–Yasskin–Green, Phys. Lett. B 78 (1978) 462 — the two are attributed jointly for both statements by Mason–Skinner (2005), Atiyah–Dunajski–Mason (2017), and Ward–Wells Ch. 10. IYG's own abstract frames it as generalising the Ward construction with "reality and currentless conditions", "currentless" being `D^a F_{ab} = 0`.)*

**Confirmed (convention).** Order-`m` thickening means structure sheaf `O[y]/(y^{m+1})`, so third order ⟺ the ideal `(Z·W)^4`. Mason–Skinner's ambitwistor YM action carries the measure `D³Z ∧ D³W / (Z·W)^4` and its field equation is `∂̄_a² = O((Z·W)^4)` — the same `4` from the variational side.

**A trap worth flagging.** Witten's own abstract says "the classical **second-order** Yang-Mills field equations" — that is the *differential* order of the PDE, not a neighbourhood order. Every source that names a neighbourhood order says **third**. There is no discrepancy in the literature.

**Confirmed (the supersymmetry link, and its limits).** Witten's contribution specifically is the `N=3` reformulation: the field equations of `N=3` super Yang–Mills are equivalent to existence of the bundle on `N=3` super-ambitwistor space `L^{5|6} ⊂ P^{3|3} × P^{3|3}_*`, with no thickening. ADM state the relationship verbatim: *"The Witten version reformulated this third-order extension condition to the simple requirement of the existence of the bundle on a supersymmetric extension of ambitwistor space built from `N = 3` supersymmetric twistor spaces."* So **the odd directions replace the thickening** — they carry the jet data as nilpotents. (`N=3` and `N=4` SYM agree in field content and equations of motion in 4d, which is why the result is often quoted for `N=4`.)

**Unconfirmed, and it is the one gap that matters here.** No published statement could be located for **what the first and second order extensions impose**. The natural reading — order 0 imposes nothing, orders 1 and 2 are unobstructed, YM is the obstruction at step 3 — is consistent with everything found but is *inference, not citation*. Also unconfirmed: the precise Eastwood–LeBrun `N ↔ order` dictionary (*Thickenings and supersymmetric extensions of complex manifolds*, Amer. J. Math. 108 (1986) 1177–1192; paper inaccessible), and any clean cohomological statement of the obstruction class.

**For calibration, the gravitational ladder is longer** (LeBrun, via ADM Thm 7.1): 5th-order neighbourhoods ⟺ Bach-flat; 6th order, algebraically general ⟺ conformally Einstein. So "which order" is a genuine, discriminating invariant in this literature, not a formality.

**Two negative literature results.** (a) Nothing found on `ρ`-equivariant thickenings of a fibre in `P¹ × P¹` for a *free* antiholomorphic involution, nor on equivariant thickenings for an involution that swaps two fibres. (b) Nothing found connecting twistor or ambitwistor thickenings to the zeta function, zeros of entire functions, or hyperbolic polynomials — the Jensen-polynomial literature (Griffin–Ono–Rolen–Zagier) and the twistor literature have no cross-links. Both are negative search results, not proofs of nonexistence. So: no free ride, and no known no-go either.

## 5. The translation: what imports, and what does not

**Does not import: the thickening as a matching condition.** §3 settles this. Whatever order you impose the matching at, order 1 is free and order 2 collapses. Going super changes nothing, because the super formulation is a reformulation of the same extension condition.

**Does not import: supersymmetry as extra information.** Its content here is that jets become *algebra* — nilpotent even coordinates traded for odd ones — rather than analysis. That is a real convenience and it is worth having if a construction ever needs to carry the 2-jet, but it is not information.

*(One speculative line, recorded so it can be dismissed properly rather than re-invented: a Grassmann algebra over `Q` is a finite-dimensional `Q`-algebra, which is formally the kind of object brief §6.5 says is missing. It does not help. The entries of anything built from `Ξ` are still the moments `M_k = ∫Φ(u)u^k du`, and Weil's argument needs definiteness proved over a `Z`-lattice, not merely a `Q`-algebra to write the answer in. The odd directions supply structure, not arithmetic.)*

**Does import, and is the reason to keep reading Witten: the inversion of the logic.** Compare the two shapes.

```
every dictionary tried in this programme :  IMPOSE  det/degeneracy locus = Z(slice extension of p)
                                            -> rigidity forces collapse (brief §3)

Witten / IYG                             :  bundle on A imposes NOTHING (existence cheap)
                                            field equation = OBSTRUCTION to extending
                                            -> the condition is a theorem, not a hypothesis
```

The second is verbatim the shape brief §1.4 identified as the only productive one — "a class whose existence theorem is cheap and whose isolation property is a theorem" — and §7.1's "transform, not matching". Witten 1978 is the cleanest existing instance of it, which is exactly why the resonance is worth taking seriously even though the thickening itself does not rescue matching.

**And the jet-order theorem now supplies a hard design constraint on any such attempt:**

> Whatever object is built from `Ξ`, the reality-of-zeros information must appear as an obstruction at transverse order `≥ 2`. An obstruction living at order 0 or 1 is provably empty.

That is a cheap, checkable screen of the same kind as brief §8, and it is new. It also sharpens the checklist's screen 1: "slice-statable" should be read as "**1-jet-statable**", since the first neighbourhood is now proved to be as blind as the slice.

**The one type-level encouragement, stated with the discount it deserves.** A spacetime point in the ambitwistor picture corresponds to a quadric surface `Q_x ≅ CP¹ × CP¹ ⊂ PA` (confirmed, Mason–Skinner). The incidence quadric of brief §2.4, on which the `σ`-type invariant lives, is also `P¹ × P¹`. That is a match of *shape*, and it is the first time an object from this programme has had a named home inside an existing correspondence. But the numbers do not line up naively — `PA` is codim 1 in `P³ × P³*` and thickened to order 3, whereas `Q_x` is codim 3 *inside* `PA` — so this is a lead to check, not a dictionary. Do not force it.

## 6. A structural finding that fell out: the real structure has no single-slice form

This is small, independent of the ADHM family, and worth recording because it explains the one-slice failure a second way.

The real structure on the incidence quadric is `ρ(ζ, w) = (ζ̄, −1/w̄)` (brief §2.4). Its two components act independently: ordinary conjugation on `ζ` (fixed locus a circle), and the **antipodal map** on `w`. A product involution's fixed locus is the product of the fixed loci, and the antipodal map has none — so

> **`ρ` is free**, and it maps the fibre `{w = w_0}` to the fibre `{w = −1/w̄_0}`.

Therefore a `ρ`-equivariant thickening of a fibre is necessarily a thickening of the **pair** of antipodal fibres, with `ρ` identifying the two jet towers conjugate-linearly. **There is no real form of a single-fibre thickening.** A one-slice condition is not just blind by Cauchy–Schwarz (memo 8 §3); it is not even a real object in the equivariant category, so it could not have carried a `σ`-type invariant in the first place.

This chimes with memo 8 §3(ii) — two non-parallel slices always suffice — from an entirely different direction, and it is a *positive* structural constraint for §7.2 of the brief: the natural equivariant object is intrinsically two-fibre-plus-jets, which is not slice-statable and therefore clears screen 1 by construction.

*(No literature was found treating equivariant thickenings for a free antiholomorphic involution. If §7.2 is pursued this is the first thing to look up properly, and the Eastwood–LeBrun paper is the place to start.)*

## 7. Screening checklist

Applied to "impose the condition on an infinitesimal neighbourhood of a slice, with the jet data carried supersymmetrically".

| screen | verdict |
|---|---|
| 1. slice-statable? | **passes** at order ≥ 2 (fails at order ≤ 1 — the screen should be restated as *1-jet-statable*) |
| 2. deformation-invariant? | **passes** — a transverse Hessian is not a homology class, degree, or charge |
| 3. uniform separation claimed? | **passes** — `c_2 = 4R Σ σ_p² ∏(…)` is exactly quadratic in the sphere radius, so it degrades continuously to `0`; this is brief §6.4 met in sharp form |
| 4. multiplicative? | n/a — not the image of an extension operator |
| 5. linear functional? | **passes** — the Hessian of a determinant difference is nonlinear |
| 6. trace term | consistent, and informative: the Hessian's rank 2 is the same transverse dimension count as the `−(2/r)B` Vekua term. This is now the **fifth** independent appearance of the transverse-sphere principle, and the first with an *order* attached |
| 7. rigidity / existence | **FAILS as a matching condition.** Order 1 free, order 2 total collapse. Exactly the brief §3 trade-off, with no intermediate order |
| 8. rationality | **untouched.** Supersymmetry supplies no `Q`-structure (see §5). Caps what any version of this can prove |
| 9. circularity | as a matching condition, `J2 ⟺ S = 0 ⟺ T_0 + iS self-adjoint` — the same Hilbert–Pólya landing as memo 8 §5.2 |

Screens 7 and 9 kill the matching reading. Screens 1, 2, 3, 5 mean the *obstruction* reading (§5) survives screening — which is more than any dictionary in this programme has managed.

## 8. Assessment

The lead was worth following, and it converts a vague "you need more than a slice" into a number. That number is **2**, it is proved, and it is stated in the same currency (order of formal neighbourhood) that the ambitwistor literature has used since 1978 — which makes cross-reading possible in both directions for the first time in this programme.

Three things changed.

1. **The blindness is sharper than memo 8 said.** Not only does the slice carry nothing; the first infinitesimal neighbourhood carries nothing either, and for a structural reason (evenness in `ν`), not a quantitative one. Brief §8 screen 1 should be restated accordingly.
2. **The matching paradigm is closed one level deeper.** memo 8 closed it against finite points; this closes it against jets of every order, since orders `≤ 1` are empty and orders `≥ 2` collapse. There is no order at which matching is informative-but-not-trivialising, and now that is a theorem rather than an observation about two data points.
3. **The obstruction reading is the live one, and it now has a design constraint.** Witten/IYG show a working example of "existence free, equation = obstruction to extension". Any attempt to build such a thing for `Ξ` must place the reality information at transverse order `≥ 2`. Plus §6: the equivariant object cannot be single-slice, so it is two-fibre-plus-jets by force.

What has **not** changed: brief §6.5. Rationality is untouched, and `PROGRAM_CLOSED.md` stands. This memo makes the next attempt cheaper and better aimed; it does not reopen anything. The honest summary is that the programme now has a well-posed question it did not have before — *is there a transform carrying `Ξ`'s data to a bundle on a thickened space, for which reality of zeros is the obstruction to extending past second order?* — and no reason yet to think the answer is yes.

**Novelty status: unchecked, and assume known.** §2 is a Taylor expansion of a product of quadratics; the evenness and isotropy are immediate from `M` depending only on `(x_0, t, ν²)`. §6 is the elementary observation that a product involution's fixed locus is the product of the fixed loci, applied to the antipodal map. Neither should be treated as new. The literature claims in §4 carry their own confidence flags; the two flagged as *unconfirmed* (what orders 1 and 2 impose in the ambitwistor setting; the Eastwood–LeBrun `N ↔ order` dictionary) are the ones to resolve first if this is pursued, since the first of them is the direct analogue of the theorem proved here.

---

*Certified by `lab_jet_order.py`: Part 1, exact symbolic identity for 1–2 conjugate pairs with 0–2 real roots (`ν`-powers present, `c_1 = 0`, `c_2` against closed form); Part 2, numeric transverse Taylor coefficients and transverse isotropy on the standard test set, using the same `detM`/`P_target` code as memos 7–8; Part 3, the J0/J1/J2/P1 ladder searched over the full admissible ADHM data at `k = 2` (see the `h^{-2}` caveat in §3(iii)); Part 4, `c_2` sampled at 400 slice points per case. The theorem of §2 and the observation of §6 are proofs, not computations. Literature in §4 established by a separate search pass with per-item confidence flags; primary texts of Witten 1978 and IYG 1978 were NOT accessible and all statements about them are from secondary sources that agree with each other.*

---

## SCOPE CORRECTION (added 2026-08-24, memo 16 §2)

§5's screen — *"Whatever object is built from `Ξ`, the reality-of-zeros information must appear as an obstruction at transverse order `≥ 2`. An obstruction living at order 0 or 1 is provably empty."* — is **withdrawn as stated**.

The theorem of §2 never locates a zero. Its chain is `2nd transverse derivative = 0 ⟹ S = 0 ⟹ T_0` real symmetric `⟹` spectrum real `⟹ p` hyperbolic, and the last three arrows are algebra (the spectral theorem). Local implies global only because the R1 family is finite-dimensional and polynomial: this is a **rigidity** result about that family, not a detection result about jets.

And one step outside the family it fails at every order at once. The datum `T_0 =` companion matrix of `p` (not symmetric), `T_1 = T_2 = T_3 = 0`, `λ = 0`, `C = T_0²` gives `M(q) = (T_0 − x_0I)² + r²I` identically, so the deficit vanishes on **all** of `ℍ` — every jet, every order, every point — with `p` non-hyperbolic (memo 12; global relative sup `10⁻¹⁴`).

Corrected statement: within a family whose deficit depends on `q` only through `(x_0, t, ν²)`, orders 0 and 1 are empty **by evenness**, and the discriminant is the transverse Hessian. That is a property of the family and must be checked for each new one.

§1's Hessian-is-Fubini–Study identification and §6's "no slice is `ρ`-real" are unaffected — the first is a coordinate identity, the second a statement about `ρ` alone.
