# Toward a Geometric Formulation with Content: Diagnosis of the Framework, and Four Candidate Conjectures

*Working memo #4 — August 23, 2026. Responds to the question "can the program be reformulated geometrically, and does hyperkähler geometry (Huybrechts–Riemann–Roch, BBF form) connect?", prompted by the desiderata paragraph in Connes, "An essay on the Riemann Hypothesis" (arXiv:1509.05576, §2.3). Continues `RH_program_synthesis.md`, `twistor_lift_computation.md`, `second_involution_resolution.tex`.*

---

## 0. Verdict up front

Three findings, in decreasing order of how much they should change what the program does.

1. **The geometric layer of the program is not merely uninformative — it sits exactly on the degeneracy locus of the very inequality that would carry content.** The zero divisor of the twistor lift has isotropic class in `NS(Q)`, and Castelnuovo–Severi on `Q ≅ P¹×P¹` holds for it *with equality*, i.e. the divisor is degenerate as a correspondence in Weil's precise sense. The cause is traced below to a single choice: intrinsicness. §3.

2. **Your hyperkähler instinct is better aimed than the analogy suggests, but it points at a target format rather than a tool.** Three precise statements, not analogies: (a) the BBF form's signature `(3, b₂−3)` is exactly a Hodge-index form `(1, m−1)` extended by a positive 2-plane spanned by `Re σ, Im σ` — the twistor sphere directions; quaternionic geometry *is* the canonical enlargement of Hodge-index geometry, not a metaphor for it. (b) Connes' desired Riemann–Roch on the square, `dim H⁰ − dim H¹ + dim H² = ½ D•D`, is *literally* the Riemann–Roch formula of a K-trivial surface — exactly `½D²` on an abelian surface, `½D² + 2` on a K3 — so his own formula is implicitly demanding that the square of the curve be holomorphic-symplectic-like. (c) Kuga–Satake is the established machine that converts a K3-type orthogonal ℚ-Hodge structure of signature `(2, m−2)` into an abelian variety carrying Rosati positivity — the exact positivity Weil's proof consumes — and in low rank its even Clifford algebra *is* a quaternion algebra. So quaternionic data is the input format for the machine that manufactures Weil positivity. §6.

3. **The program already has, in embryo, the finite-rank quadratic form it has been hunting, and it is not the object the Second Involution Conjecture was trying to build.** The paper's own algebraic toy model (`Σ|rᵢ|² = max(b²−2c, 2c)` for `x²+bx+c`) is the semialgebraic shadow of **Hermite's theorem**: the Hankel form of power sums has signature `(r+c, c)`, so *the number of negative eigenvalues equals the number of zero spheres exactly*. This is nonlinear (evades Theorem D), finer than homology and degree (evades Theorem E), arithmetically computable, and quantitatively sensitive to small spheres — the full specification §5 of `RH_program_synthesis.md` laid down. Certified numerically in §5 below, including the sensitivity law and the resolution cost. It is also, honestly, already-occupied classical territory (Li's criterion, Turán/Jensen–Pólya, Weil positivity), which sharpens what the program's distinctive contribution would have to be: not another positivity criterion, but a geometric object whose Hodge index theorem *supplies* one.

**One correction to the existing papers, and it inverts the central slogan.** See §4.

---

## 1. The content criterion

The reason to write this memo at all is that the Second Involution Conjecture family has no directional content, and the failure was structural, not a matter of tightening hypotheses. Adopt an explicit test and apply it to every candidate before investing in it.

> **Content test.** For a candidate statement `C`:
> (a) *Is `C` implied by RH?* If yes, `C` is RH-trivial: a proof of `C` cannot be progress, because RH already gives it.
> (b) *Does `C` imply RH?* If no, `C` is RH-orthogonal: proving it leaves the hypothesis exactly where it was.
> `C` has **directional content** iff the answers are *no* and *yes*.

Scorecard for what exists:

| statement | (a) implied by RH? | (b) implies RH? | content |
|---|---|---|---|
| Thm 9.1 (encoding) | yes (`S≡0`) | no | none; it is a diagnosis |
| Conj 10.1 (non-adaptive) | **yes** (`S≡0`) | no | none |
| Conj 10.2 (class-uniform) | no | **no** | none (waypoint only) |
| Thm F(a) (rate criterion) | — | falsifies RH | genuine, but it is the classical wall |
| Lemma 9.2 (oscillation) | no | no | unconditional infrastructure, not directional |

Conjecture 10.2 is the interesting failure: it escapes RH-triviality but still does not imply RH, because a formula computing `D(c)` from prime data leaves untouched the problem of proving `sup_c D = 0` — and that problem, at the exponential-rate level, is the classical equivalence between zero-free regions and prime error terms (already conceded in `second_involution_intro.tex`, §on the degenerate instance). The two failure modes are different but the consequence is the same: **approximation-theoretic statements about the defect cannot have directional content, because RH is not a statement that the defect is computable; it is a statement that the defect vanishes.**

This is the sense in which "more content" and "harder" are coupled, and there is no way around it. What a good conjecture buys is not ease but *direction*: partial results accumulate toward something, and failure is informative.

---

## 2. Inventory: what the framework actually provides

Sorted by what kind of mathematical object each tool is, because the gaps are visible only this way.

**Reformulation devices (dictionary; no theorems of their own).**
- Slice-regular extension: RH ⟺ no zero spheres. Clean, and the correct home for the point/sphere dichotomy.
- Twistor lift to `(Q, ρ)` and the quotient `Y = Q/σ`: RH ⟺ every component of the zero locus in `Y` is nonorientable (`RP²` vs `S²`).
- The `S`-spectrum reading: "no spheres" = "the spectrum of a self-adjoint operator".

**Genuine unconditional theorems.**
- Lemma 9.2 (uniform oscillation of `F(c) = Re Z(c, log 2)`), with effective constants. Real, reusable, independent of everything else.
- Theorem F(a): `limsup λ⁻¹ log|Z(c,λ)| ≤ Y`, so exponential growth in one window disproves RH. The only falsifiable direction in the program.
- Proposition (gateway): `Σ|ρ|⁻² ≥ Σρ⁻¹(1−ρ)⁻¹ = 2 + γ_E − log 4π`, equality iff RH.
- Theorem 10.5 (recurrence lower bound): non-adaptive continuous semialgebraic estimators need `Λ ≥ (1−o(1)) log log x₀`.

**Two no-go theorems, which are the framework's real content.**
- Theorem D: no continuous linear functional of any rotational extension separates on-axis from off-axis zeros.
- Theorem E: the 4-dimensional Brouwer degree weights a sphere by exactly 2 — same as the complex count. Homology and degree are both blind.

**What is absent, and this is the whole story.** No nondegenerate quadratic form. No finite-rank lattice. No ℚ-structure. No `H¹`. No trace formula with a positivity attached. No algebraic correspondence for the reality involution. Every item Connes lists as a desideratum is absent, and the two no-go theorems say precisely that the *coarse* invariants (linear, homological, degree-theoretic) cannot substitute for them.

The gateway proposition deserves a second look, because it is the one place where the program accidentally reproduces Weil's mechanism. Its proof is: with `a = 1/ρ`, `b = 1/(1−ρ)`, a full involution-orbit contributes `2|a|² + 2|b|²` to the left and `4Re(ab)` to the right, and `4Re(ab) ≤ 4|a||b| ≤ 2|a|² + 2|b|²`. That is Cauchy–Schwarz with equality iff `|a| = |b|` iff `Re ρ = ½`. Compare Weil (§4 below): `|Σαᵢⁿ| = |⟨Fⁿ, Δ⟩| ≤ ‖Fⁿ‖‖Δ‖`. **The reality-paired sum is the norm; the functional-equation-paired sum is the inner product; RH is the equality case of Cauchy–Schwarz.** The program has the right shape and the wrong side: the cross-term is classically known, the diagonal is not, and "compute the diagonal" is RH itself. Which is exactly why every attempt to state that as a conjecture came out either RH-trivial or RH-orthogonal.

---

## 3. Why the geometry is degenerate — the computation

Set up intersection theory on `Q ≅ P¹_ζ × P¹_w` and compare with Weil.

`NS(Q) = ℤA ⊕ ℤB` with `A² = B² = 0`, `A·B = 1` — the hyperbolic plane, Gram matrix `[[0,1],[1,0]]`, signature `(1,1)`. This is *literally* Weil's `⟨f₁, f₂⟩ ⊂ NS(C×C)` with `f₁ = C×{pt}`, `f₂ = {pt}×C`. So the program's quadric already carries the Castelnuovo–Severi Gram matrix. Encouraging — until one writes down the divisor.

By Theorem B, the lift is the **product map** `f̃ = F × id`, so
```
Z(f̃) = F⁻¹(0) × P¹_w = Σ mₖ L_{ζₖ},   class = m·A,   m = Σ mₖ .
```
Bidegrees and self-intersection:
```
d₁ = Z·A = 0,      d₂ = Z·B = m,      Z² = m²A² = 0 .
```
Castelnuovo–Severi (`D² ≤ 2d₁d₂`, equality iff `D ≡ d₂f₁ + d₁f₂`) reads
```
0 ≤ 2·0·m = 0 ,
```
**equality**, and the equality condition `D ≡ d₂f₁ + d₁f₂ = mA` is satisfied identically. So:

> The zero divisor of the twistor lift is not merely invisible to intersection theory; it is precisely the *degenerate* case of the inequality Weil's proof consumes — the case Weil discards as carrying no information about the correspondence.

This upgrades Theorem C(2) ("homology cannot separate the two cases") from an observation to a structural statement: the divisor classes span an isotropic line, so the intersection form restricted to them vanishes identically and every Hodge-index argument on `Q` is vacuous *a priori*.

**Root cause, and it is a single choice.** The divisor is ruling-parallel because the lift is a product, and the lift is a product because `Ξ` is *intrinsic*. And intrinsicness is not an incidental convenience — it is the maximal-rigidity condition:

> **Lemma (twistor rigidity; sharper than the form used in the papers).** Let `I', I''` be two *distinct* complex structures in the twistor sphere of a hypercomplex manifold. Then `T⁰¹_{I'} ∩ T⁰¹_{I''} = 0`. Hence any `C¹` function annihilated by both `∂̄_{I'}` and `∂̄_{I''}` is locally constant.
> *Proof.* With `I' = I`, `I'' = aI + bJ + cK`, `a²+b²+c²=1`: from `IJ=K, IK=−J` one gets `I I'' + I'' I = −2a`, so `(I''−I)² = 2(a−1)·id`, invertible whenever `a ≠ 1`. If `v` lies in both, `(I''−I)v = 0`, so `v = 0`. ∎

Two complex structures already suffice; compactness is not needed; the statement is local, hence true on any ball in flat ℍ. So the intrinsic class is defined by exactly the condition that kills function-theoretic freedom, and the price is paid in the geometry: product lift, ruling-parallel divisor, isotropic class, vacuous Hodge index. **The framework's defining choice is what makes its geometry degenerate.** That is a much sharper diagnosis than "the invariant is a relabeling".

**A hard obstruction to the instinct "do the geometry upstairs on twistor space."** Worth knowing before investing:
- `H⁰(Z, O_Z) = ℂ`, and `H⁰(Z, Ω^i_Z) = 0` for `i ≥ 1`.
- For compact `M`: the algebraic dimension is `a(Z) = 1`, every divisor on `Z` is a pullback from `P¹`, and all meromorphic functions are `π`-pullbacks.
- **The twistor space of a compact hypercomplex manifold is never Moishezon and never in Fujiki class 𝒞** — hence never Kähler and never projective (Gorginyan, IMRN 2026, arXiv:2410.24085; for the 4-dimensional ASD case this is Hitchin 1981, so K3 and `T⁴` twistor spaces are already non-Kähler).

So there is no projective intersection theory, no Riemann–Roch, and essentially no divisor theory available on a compact twistor space. **Any geometry with divisors and a Riemann–Roch must live downstairs on a projective object, not upstairs.** This kills a natural-looking direction cheaply, which is worth more than it costs to learn.

---

## 4. Correction: the dictionary for the second involution is stated wrongly, and it inverts the slogan

`zero_sphere_condensed.tex` §8 and `second_involution_intro.tex` write

> `ι_FE : ρ ↦ 1−ρ  (γ ↦ −γ)`,  `ι_R : ρ ↦ ρ̄  (γ ↦ γ̄)`.

The first parenthetical is right; the second is not. With `ρ = ½ + iγ`,
```
ρ̄ = conj(½ + iγ) = ½ − i γ̄ = ½ + i(−γ̄) ,    so  ι_R : γ ↦ −γ̄ ,
```
and the composite `ι_FE ∘ ι_R` is `γ ↦ γ̄`. This matters because the program's central slogan is "RH is the statement that the two involutions agree":
- With the correct dictionary: `ι_FE(γ) = ι_R(γ)` ⟺ `−γ = −γ̄` ⟺ `γ ∈ ℝ` ⟺ RH. ✓
- With the dictionary as printed: `−γ = γ̄` ⟺ `γ` purely imaginary — the *opposite* of the intended statement, and a condition the zeros never satisfy.

Nothing downstream breaks (the group generated by `{γ↦−γ, γ↦γ̄, γ↦−γ̄}` is the same, and the defect `D(c) = Σ(Im γ)² exp(...)` is defined directly), so this is a typo rather than an error in the mathematics. But it is in the abstract-level framing of both papers and should be fixed before circulation. The cleanest correct form of the slogan:

> **RH ⟺ the conjugation correspondence `κ : γ ↦ γ̄` is the identity on the zero multiset.**

That formulation is also the one that connects to §6–§7, because "a correspondence equals the diagonal" is the shape of statement intersection theory is built to handle.

---

## 5. The finite-rank object the program already has: Hermite's theorem

`zero_sphere_condensed.tex` §8 observes that in the exact algebraic model — real polynomials, coefficients playing the role of primes — conjugation-paired sums of roots are computable from the coefficients but only *semialgebraically*: for `x² + bx + c`, `Σrᵢ² = b²−2c` while `Σ|rᵢ|² = max(b²−2c, 2c)`, non-analytic across the discriminant. The paper reads this as dictating the *shape of the conjecture* (semialgebraic estimator). That is the wrong reading. It is the shadow of a classical theorem about a quadratic form:

> **Hermite's theorem.** Let `p ∈ ℝ[x]` have `r` distinct real roots and `c` conjugate pairs, and let `s_k = Σ rᵢᵏ` be the power sums. Then the Hankel form `H = (s_{i+j})` has rank `r + 2c` and signature `(r+c, c)`. In particular:
> **the number of negative eigenvalues equals the number of zero spheres, exactly.**

For `x²+bx+c` the Hankel matrix is `[[2, −b], [−b, b²−2c]]` with determinant `b²−4c`: signature `(2,0)` iff the discriminant is positive, `(1,1)` iff negative. The paper's `max(b²−2c, 2c)` is the semialgebraic *description* of a signature; the signature is the object.

Check this against the program's own specification (`RH_program_synthesis.md` §5, and the two hardness checks):

| requirement | Hankel/Hermite form |
|---|---|
| nonlinear (evades Theorem D) | ✓ quadratic in the zeros |
| finer than homology and degree (evades Theorem E) | ✓ counts spheres with weight 1, not 2 |
| consumes arithmetic | ✓ the moments are explicit classical constants (below) |
| quantitatively sensitive as `y₀ → 0` | ✓ exactly `∝ y₀²`, verified below |
| fails for Davenport–Heilbronn | ✓ by construction: DH has off-line zeros, hence negative eigenvalues |

**Transfer to `Ξ`.** Positive power sums diverge, so use the reciprocal moments. With the zero multiset `{±γₙ}` and `tₙ := γₙ⁻²`,
```
m_k := Σₙ γₙ^{−2k}  (k ≥ 1),   convergent since γₙ ≍ n/log n.
```
RH ⟺ every `γₙ` real ⟺ every `tₙ` real positive ⟺ the atomic measure `Σ tₙ δ_{tₙ}` is a positive measure on `(0,∞)` ⟺ `(m_k)_{k≥1}` is a Stieltjes moment sequence ⟺ the Hankel matrices `(m_{i+j+1})` and `(m_{i+j+2})` are positive semidefinite. The moments are *unconditionally computable in closed form*: they are the classical `Σ_ρ ρ^{−n}` constants (Lehmer, "The sum of like powers of the zeros of the Riemann zeta function", Math. Comp. 50 (1988)), expressible through `γ_E`, `log π`, and values of `ζ`.

**Numerical certification** (`lab_hankel_check.py`, mpmath at 120–400 digits; the Hankel matrices are Hilbert-like and hopeless in float64 — negative-eigenvalue counts are taken from sign changes of leading principal minors, via Jacobi):

1. *Hermite, exact.* Six test polynomials with `c = 0,1,2` conjugate pairs: `#neg eig = c` in every case.
2. *Full-rank Hankel on real `Ξ` data.* First 8 Riemann ordinates, full `8×8` Hankel of the reciprocal-square moments: `#neg eig = 0`. Determinant `4.5085927e−196`, matching the closed form `∏tᵢ · ∏_{i<j}(tᵢ−tⱼ)²` to 385 digits.
3. *Implanted spheres.* Replacing `c` real ordinates by conjugate pairs gives `#neg eig = c` for `c = 1, 2, 3`, with `sign(det) = (−1)^c` as predicted. **The discriminant works, exactly, and counts spheres with weight one.**
4. *Sensitivity law.* Implanting a pair at height `a` with radius `y₀` and halving `y₀` repeatedly, the log–log slope of `|det|` converges to `1.98165 → 1.99541 → 1.99885 → 1.99971 → 1.99993`. So sensitivity `∝ y₀²`, exactly. The mechanism is transparent in closed form: the sphere enters through the single Vandermonde factor
```
(t − t̄)² = −4(Im t)² ≈ −16 y₀² / a⁶ ,    t = (a + i y₀)⁻² ,
```
so the *relative* size of the violation is `≍ y₀²/a⁶`: quadratic in the sphere radius, and suppressed by `a⁻⁶` in the height. This is the "RH is barely true" boundary of §6 of `twistor_lift_computation.md`, now with an exact exponent rather than a heuristic.
5. *Resolution cost, and this is the bad news.* Hermite's theorem needs the *full* rank: a truncated `K×K` Hankel with `K` less than the number of atoms is a compression and can be positive definite while the full form is not. (Verified: a `6×6` Hankel built from 40 ordinates with an implanted quadruple at height 100 shows **no** negative eigenvalue — the criterion is silent, not wrong.) And the full determinant collapses super-exponentially: `log₁₀|det| = −24.2, −44.4, −71.9, −105.7, −146.7, −195.3, −250.4, −314.0, −384.7, −462.6` for `n = 3, …, 12` zeros, i.e. `log₁₀|det| ≈ −3.2 n²` (the Vandermonde has `n(n−1)/2` factors). Since `n ≍ T log T / 2π` up to height `T`, the working precision needed to certify the sign grows like `T² log²T`.

**Honest assessment of item 5.** The Hankel route is *exact* where the Second Involution Conjecture was approximate, and it is *directional* where the SIC was not — but it has the worst resolution cost of any tool in the program: quadratically many digits in the number of zeros carried, versus the classical `exp(1/y₀)` of the rate criterion. So it is an excellent conceptual and diagnostic object and a poor computational one. Two consequences: (i) it should replace the SIC as the program's statement of "what the reality defect is", (ii) it should *not* be pursued as a numerical detector.

**And the sobering context.** This territory is occupied. RH ⟺ Hankel/moment positivity of explicitly computable constants is, in substance, **Li's criterion** (`λₙ ≥ 0`; Li 1997, Bombieri–Lagarias 1999), and the truncated version is the **Jensen–Pólya / Turán** programme (Csordas–Norfolk–Varga; Griffin–Ono–Rolen–Zagier, PNAS 2019, who prove hyperbolicity of the Jensen polynomials `J^{d,n}` for each `d` and large `n` by exactly this Hankel-positivity route). So the program does not get to claim this as new. What it does get is a much better-posed question, which is the subject of the rest of this memo:

> Positivity *criteria* for RH are abundant — Weil, Li, Turán/Jensen, Hankel/moment. What is scarce, and what Connes' paragraph is asking for, is a geometric object whose **Hodge index theorem supplies** one of them. Geometry is the only known mechanism that *proves* such a positivity rather than restating it.

That is the target. Everything below is about how to aim at it.

---

## 6. What Weil's proof consumes, and where hyperkähler geometry actually fits

**Weil's mechanism, itemized.** For `C/𝔽_q` smooth projective of genus `g`, with `Z(C,T) = P(T)/((1−T)(1−qT))`, `P(T) = ∏(1−αᵢT)`:

1. **A finite-rank ℚ-structure.** `Corr(C) = Div(C×C)/≡`, finite rank; modulo degenerate correspondences it is `End(Jac C)`.
2. **A Hodge-index positivity.** The intersection form on `NS(C×C)⊗ℝ` has signature `(1, ρ−1)` (Mattuck–Tate, Grothendieck; over ℂ, the Hodge–Riemann relation in degree `(1,1)`). Consequence: Castelnuovo–Severi `D² ≤ 2d₁d₂`, equivalently `tr(D∘D') ≥ 0` — Rosati positivity on `End(Jac C)⊗ℝ`.
3. **An algebraic identity, not an inequality.** `F ∘ F' = q·Δ`, because Frobenius is purely inseparable of degree `q`. This gives `‖Fⁿ‖² = 2g qⁿ` *exactly*.

Then Cauchy–Schwarz: `|Σαᵢⁿ| = |⟨Fⁿ, Δ⟩| ≤ √(2g qⁿ)·√(2g) = 2g q^{n/2}`, for all `n`, forcing `|αᵢ| ≤ q^{1/2}`; the functional equation `α ↦ q/α` upgrades to equality. ∎

Note what each ingredient is. (2) is geometry. (3) is arithmetic, and it is an *identity*. (1) is what makes both meaningful. The program currently has none of the three.

**Statement of the deepest structural obstruction, and it is not specific to this program.** In characteristic `p`, Frobenius is simultaneously (i) the geometric avatar of complex conjugation and (ii) an actual morphism, so its graph *is* a divisor and intersection theory applies. Over ℚ, the reality involution `ι_R` is **antiholomorphic**. It is a real structure, not a correspondence; it has no divisor class; only `σ` sees it. This is why neither this program nor Connes' gets intersection theory for the second involution, and it is the precise content of "the square of the curve is missing". Two coherent responses exist, and they are genuinely different (§7).

**Now, hyperkähler geometry. Three precise statements, replacing the analogy.**

**(a) Quaternionic structure = Hodge index + the twistor 2-plane.** For a compact irreducible holomorphic symplectic `X` of dimension `2n`, the Beauville–Bogomolov–Fujiki form `q_X` on `H²(X,ℝ)` has signature `(3, b₂−3)`, with the three positive directions spanned by `Re σ, Im σ, ω` — the three Kähler forms `ω_I, ω_J, ω_K` of the hyperkähler triple, i.e. the quaternionic imaginary units. Restricted to `H^{1,1}(X,ℝ)` the signature is `(1, b₂−3)`: Lorentzian. Restricted to `NS(X)_ℝ` it is `(1, ρ−1)` — *exactly the surface Hodge-index signature Weil consumes* — **and this holds precisely when `X` is projective** (equivalently, iff some `L` has `q_X(L) > 0`; Huybrechts' projectivity criterion, GHJ Prop. 26.13). Otherwise the form is negative semidefinite with radical of dimension `≤ 1`.
So: **the passage from a Hodge-index form to a hyperkähler one is exactly the addition of a positive 2-plane, and that 2-plane is the twistor sphere.** Quaternionic geometry is the canonical enlargement of the structure Weil's proof needs — with the projectivity caveat doing real work, since it is what separates "has a Weil-shaped lattice" from "does not".

Fujiki's relation `∫_X α^{2n} = c_X q_X(α)^n` (in the perfect-matchings normalization, `c_X·(2n)!/2ⁿn!`) says every top intersection number of `H²`-classes is a polynomial in `q_X`-pairings; combined with Verbitsky's `SH ≅ Sym*H²/(x^{n+1} : q_X(x)=0)`, the whole `H²`-generated cohomology is governed by one quadratic form. The reduced LLV algebra is `𝔰𝔬(3, b₂−3)` — the signature is not a coincidence but the real form of a Lie algebra acting on the cohomology.

**(b) Connes' desired Riemann–Roch on the square is the Riemann–Roch of a K-trivial surface.** His stated requirement (AIM/Bristol 2018) is
```
dim H⁰ − dim H¹ + dim H² = ½ D•D .
```
On a surface `S`, Riemann–Roch reads `χ(O_S(D)) = ½D² − ½D·K_S + χ(O_S)`. Connes' form is the `K_S = 0` case:
- abelian surface: `K = 0`, `χ(O) = 0` ⟹ `χ(L) = ½L²` — **exactly** his formula;
- K3: `K = 0`, `χ(O) = 2` ⟹ `χ(L) = ½L² + 2` — his formula plus a constant; and this is the `n=1` case of **Huybrechts–Riemann–Roch**, `χ(L) = RR_X(q_X(L))` with `RR_X` of degree `n` (`K3^{[n]}: binom(t/2+n+1, n)`, `Kum_n: (n+1)binom(t/2+n, n)`, etc.; all coefficients positive by Jiang, J. Alg. Geom. 32 (2023)).

In dimension 2, K-trivial and simply connected *is* K3 *is* the unique irreducible holomorphic symplectic type. So **Connes' own formula is implicitly demanding that the hypothetical square of the arithmetic curve be holomorphic-symplectic-like**, and that is the sharpest technical bridge between his paragraph and your instinct. It is a genuine constraint on what to build, not a metaphor.

Note carefully what this does *not* say: HRR is a consequence of Fujiki's relation, i.e. a computational shadow of the quadratic form, and it carries no positivity that could prove RH. Jiang's theorem is positivity of the *coefficients* of `RR_X`, not definiteness of `q_X`. **HRR is a signpost about the shape of the target, not an engine.** If you go looking for leverage in hyperkähler geometry, the object to use is `q_X` and its signature, not `χ`.

**(c) Kuga–Satake is the machine that converts quaternionic data into Weil positivity.** Given a ℚ-vector space `V` of dimension `m` with a quadratic form `q` and a weight-2 Hodge structure of **K3 type** (`dim V^{2,0} = 1`, real signature `(2, m−2)`): form the even Clifford algebra `Cl⁺(V,q)`; pick an oriented orthonormal basis `{e₁,e₂}` of the positive 2-plane `P = (V^{2,0} ⊕ V^{0,2}) ∩ V_ℝ` and set `J = e₁e₂`, so `J² = −1`. Left multiplication by `J` is a complex structure on `Cl⁺(V,q)⊗ℝ`, independent of the basis chosen — *the period point of the Hodge structure becomes a complex structure on a Clifford algebra*. With the main anti-involution supplying a polarization, the output is an abelian variety `KS(V)` of dimension `2^{m−2}`, and
```
V(1) ↪ End(H¹(KS(V), ℚ))
```
is an inclusion of ℚ-Hodge structures. Consequences worth noting for this program:
- Rosati positivity on `End(KS(V))` is a *theorem*, and it is the same positivity as Weil's item (2).
- In low rank the even Clifford algebra **is a quaternion algebra**: rank 3 with signature `(2,1)` gives a quaternion algebra over ℚ; K3 surfaces with transcendental lattice of rank 3 have Kuga–Satake variety an abelian surface with quaternionic multiplication, parametrized by a Shimura curve (Morrison 1985; Paranjape 1988).
- It applies verbatim to hyperkähler manifolds via `(H²_prim(X,ℚ), ±q_X)`, signature `(2, b₂−3)` (André 1996; Soldatenkov, Adv. Math. 2020; algebraic for generalized Kummer type by Varesco–Voisin 2022).
- It is the engine of Deligne's proof of the Weil conjectures for K3 surfaces (1971/72): purity of weight 2 on `H²` of a K3 is *transferred* from Weil's positivity on `H¹` of the Kuga–Satake abelian variety.

**The takeaway, stated as sharply as I can.** Kuga–Satake is a *transfer* of positivity, not a source of it, and its input format is exactly a finite-rank ℚ-quadratic space of K3 type — precisely the format a quaternionic/hyperkähler picture produces. So:

> Your instinct is structurally correct: quaternionic geometry is the natural input format for the only machine known to manufacture Weil-type positivity. What hyperkähler geometry supplies is the **target format**, not the object. The missing step is the same missing step Connes names — construct a finite-rank ℚ-Hodge structure of K3 type attached to `Ξ` — and no one has closed it.

**Literature status, so nothing blindsides.** As of August 2026: (i) nothing in the reputable literature attempts RH for `ζ` via hyperkähler geometry, K3s, or the BBF form — the Connes–Consani corpus and Connes' Feb 2026 survey (arXiv:2602.04022) never mention them; (ii) Connes–Consani have achieved essentially every desideratum in that paragraph *except* the square: geometric explicit formula (Connes 1999, Meyer 2005), Frobenius correspondences (arithmetic site, 2014–16), divisors and RR on the curve (scaling site 2017; `Riemann–Roch for Spec ℤ`, Bull. Sci. Math. 2023; `On the Jacobian of Spec ℤ`, arXiv:2602.15941), Weil positivity at the archimedean place (Selecta 2021) — but **there is no square of the curve, no intersection form, no `H¹`, and no Hodge index**, and no paper 2021–2026 constructs one; (iii) the program's live effort has *moved away* from the Riemann–Roch strategy to prolate/spectral-triple work (Connes–Moscovici; `Zeta Spectral Triples`, arXiv:2511.22755), and the 2026 survey does not discuss the square, Castelnuovo–Severi, or the Hodge index at all. So the Riemann–Roch axis is genuinely under-attended right now — which cuts both ways: less competition, and the strong prior that it is under-attended because it is hard.

---

## 7. The fork: two coherent geometric routes

Because `ι_R` is antiholomorphic (§6), there are exactly two coherent things to do, and they use disjoint toolkits. Choosing between them is the main strategic decision.

**Route A — keep the real structure, and use real algebraic geometry's extremality theory.**
An antiholomorphic involution is what real algebraic geometry is *about*. The relevant machinery is `ℤ/2`-equivariant, not intersection-theoretic: the **Smith–Thom inequality** `Σ dim H_i(X(ℝ); 𝔽₂) ≤ Σ dim H_i(X(ℂ); 𝔽₂)`, its extremal case (**M-varieties**, maximality), the Kalinin–Viro spectral sequence, and the Harnack–Klein bound for curves.

This is directly adapted to Theorem C(3) (RH ⟺ every component of the zero locus in `Y = Q/σ` is nonorientable), and it is strictly finer than both invariants the no-go theorems killed: Smith–Thom is neither a linear functional nor a deformation-invariant integer count. The polynomial model is encouraging and completely concrete:

> For real `p` of degree `2m` with `r` real roots and `c` conjugate pairs, the real hyperelliptic curve `C_p : y² = p(x)` has genus `m−1` and `m−c` ovals. Harnack's bound is `#ovals ≤ g+1 = m`. So **all roots of `p` real ⟺ `C_p` is an M-curve (Harnack-extremal)**, and "no zero spheres" becomes "maximality of a real algebraic variety".

Harnack's bound *is* Smith–Thom for curves, so the program's dichotomy has an established geometric home with real theorems attached — in the finite-rank polynomial model, where Jensen/Hadamard truncations live.

*Caveat, stated honestly.* Maximality is the equality case of an inequality, so RH becomes "the extremal case holds" — again a positivity to be proven, not derived. But it is a *different* extremality with a different toolkit, it is finite-dimensional, and it is sensitive at the wall (maximality degenerates exactly when a conjugate pair collides on the axis, which is the de Bruijn–Newman transition). And it retires §5c of `twistor_lift_computation.md`, which hoped for a *deformation-invariant* signed count: any deformation-invariant count is blind to the DBN boundary by construction, so that hope was self-defeating and should be dropped.

**Route B — algebraize the reality involution by transferring to a symplectic setting.**
This is the Kuga–Satake route of §6(c): convert an orthogonal signature-`(2, m−2)` structure into an abelian variety where the relevant involution is the *Rosati* involution — algebraic, with positivity a theorem. This is precisely how Deligne handled K3s, and it is where quaternion algebras appear literally rather than by analogy. Higher ceiling, much higher entry cost, and the entry cost is the missing object.

---

## 8. Four candidate conjectures, ranked

Each is stated with the content test applied. The ranking is by *expected information per unit effort*, not by ambition.

---

**Conjecture I (recommended spearhead) — Hodge-index realization of Hermite, in the polynomial model.**

> For a real polynomial `p` of degree `2m` (in particular for the Jensen/Hadamard truncations `Ξ_N`), there exists a smooth projective surface `S_p` with a real structure, functorially attached to `p`, and an embedding of the Hermite–Hankel form of `p` (equivalently the Bezoutian of `(p, p′)`) as the intersection form on a sublattice of `NS(S_p)`, such that Hermite's theorem becomes the Hodge index theorem on `S_p`.

Content test: (a) not implied by RH — RH does not construct `S_p`; (b) if the construction is uniform in `N` with controlled ranks, hyperbolicity of `Ξ_N` follows from Hodge index, and RH follows by Jensen–Pólya. So: **directional.**

Why this first: it is *finite, self-contained, and checkable this month*. The objects are explicit (`y² = p(x)`, its Jacobian, the Bezoutian, `NS`), the question is a concrete lattice-theoretic one, and either answer is informative. If the realization exists, you have the template for the `ζ` case and a genuinely new observation. If it provably does not, you have learned that Hermite positivity is *not* of Hodge-index type, which redirects the whole program away from Route B and toward Route A. Either outcome is worth more than another approximation conjecture. This is also the question that uses your geometric strength most directly, and it sits precisely on Connes' axis.

First concrete sub-question, tractable by hand: for `m = 2` (quartic `p`, `C_p` of genus 1, so `S_p = C_p × C_p` an abelian surface) does the `2×2` Hankel form appear inside `NS(C_p × C_p)` with its intersection form? Note the encouraging coincidence: on an abelian surface `χ(L) = ½L²` exactly — Connes' formula.

---

**Conjecture II — equivariant maximality (Route A).**

> RH ⟺ for every `N` beyond an explicit bound, the real algebraic object attached to `Ξ_N` (concretely `C_N : y² = Ξ_N(x)`, or the quotient `Y_N` of the truncation's twistor lift) is maximal in the sense of Smith–Thom.

Content test: (a) not RH-trivial as a construction problem, though for each fixed `N` maximality is *equivalent* to hyperbolicity of `Ξ_N`, hence implied by RH — so the content is in the *mechanism*, not the statement; (b) implies RH via Jensen–Pólya. **Directional, but the statement is a reformulation; its value is that it imports a toolkit (Kalinin–Viro, Degtyarev–Kharlamov maximality theory) that has never been aimed at this.**

Honest caveat: this is a change of language plus a change of toolkit, not a new theorem. Worth one focused month, mostly reading, to establish whether maximality theory has any mechanism that could apply. The specific question to ask a real-algebraic geometer: *are there any known criteria that force maximality, as opposed to bounding it?* If the answer is "essentially none", Route A closes cheaply.

---

**Conjecture III — the Lorentzian realization (Weil-shaped; this is Connes' gap, stated in the program's own terms).**

> There exist a finite-dimensional ℚ-quadratic space `(V, q)` of signature `(1, m−1)` (or `(3, m−3)`), a positive class `h`, and classes `Δ, κ ∈ V_ℚ` attached to the zero data of `Ξ` (or of a truncation/window), such that: `q(Δ)` and `q(Δ, κ)` are given by the classical explicit-formula constants; `q(κ)` is the reality-paired sum; and `κ − Δ ⊥ h`.

Then Hodge index gives `q(κ−Δ) ≤ 0`, the arithmetic gives `≥ 0`, so `κ = Δ`, so RH.

Content test: (a) not implied by RH; (b) implies RH. **Directional — and it is the real target.** But it *is* the missing square of the curve, and it has resisted Connes and Consani for a decade. Write it down as the program's stated goal; do not plan to attack it directly.

---

**Conjecture IV — the Kuga–Satake target (Route B, highest ceiling).**

> There is a finite-rank ℚ-quadratic space `(V_N, q_N)` of K3 type (signature `(2, m−2)`) functorially attached to `Ξ_N`, whose Kuga–Satake abelian variety `A_N` carries the zero data of `Ξ_N` as an endomorphism, and under which the reality involution on the zeros corresponds to the Rosati involution on `End(A_N)`.

Then Rosati positivity forces hyperbolicity of `Ξ_N`, and RH follows in the limit.

Content test: (a) not implied by RH; (b) implies RH. **Directional, and it is the version in which the program's quaternionic character becomes literal** — the even Clifford algebra of a rank-3 or rank-4 signature-`(2,n)` form *is* a quaternion algebra, so "the right framework for `ζ` is quaternionic" would become a theorem-shaped statement rather than an aesthetic one. Highest ceiling in the program. Also the largest gap: producing `V_N` is Conjecture III with extra structure demanded.

Its value now is as a *specification*: it tells you exactly what to try to build (a K3-type Hodge structure, signature `(2, m−2)`, finite rank, ℚ-structure), which is far more specific than "find a discriminant", and it explains why the program's existing assets — real structures, a sphere of complex structures, Clifford/quaternionic algebra — are the right raw materials for that particular target.

---

## 9. Concrete next actions

In order, with the cheapest information first.

1. **Fix the involution dictionary** in both `.tex` files (§4). Half an hour; it is in the framing of the central slogan.
2. **Reframe the algebraic model as Hermite's theorem** in `zero_sphere_condensed.tex` §8. This replaces "the defect is a semialgebraic function of prime data" (no content) with "the defect's *sphere count* is the negative-eigenvalue count of an explicitly arithmetic quadratic form" (exact, directional) — and it retires the SIC as the program's headline rather than merely repairing it. Cite Hermite, and cite Li's criterion and Griffin–Ono–Rolen–Zagier honestly as the occupied classical territory, with the `y₀²/a⁶` sensitivity law and the `n²`-digit resolution cost as the program's own quantitative contribution (both certified in `lab_hankel_check.py`).
3. **Attack Conjecture I in the genus-1 case by hand.** Quartic `p`, `C_p` of genus 1, `S_p = C_p × C_p` abelian, `χ(L) = ½L²`. Does the `2×2` Hermite–Hankel form sit inside `NS(S_p)`? This is a finite computation and it is the whole program in miniature.
4. **One month of reading on Route A**, with one question: does maximality theory contain any mechanism that *forces* maximality? Ask a real-algebraic geometer directly; this is exactly the kind of question that is cheap for an expert and expensive to reconstruct.
5. **Do not** pursue the Hankel form as a numerical detector (§5, item 5), and **do not** pursue deformation-invariant signed counts (§7, Route A caveat) — both are provably self-defeating.
6. **Retire** Conjectures 10.1 and 10.2 from headline status, keeping Lemma 9.2 (oscillation) and Theorem F(a) (rate criterion) as the program's standing unconditional results, and Theorem 9.1 as the diagnosis it is.

## 10. What should stop

The program's recurring failure mode is now visible and nameable: **it keeps producing statements about whether the reality defect is computable, when RH is a statement that the reality defect vanishes.** Computability statements are RH-trivial (if RH holds the defect is zero and everything is computable) or RH-orthogonal (a formula still leaves the vanishing to be proven). No amount of tightening the estimator class escapes this, because the defect is not the obstruction — the *positivity* is.

Every tool that has ever proven such a positivity has been geometric, and has had the same three ingredients: a finite-rank ℚ-structure, a Hodge-index signature, and an arithmetic identity. The program should be reorganized around producing those, and hyperkähler geometry is a legitimate source of the second — with the first still missing and the third not yet even conjectured.

---

*Numerical claims in §5 are certified by `lab_hankel_check.py` (mpmath, 120–400 digits; ~2 min). Literature status in §6 rests on a systematic August 2026 sweep; the three "nothing exists" claims (no hyperkähler–RH literature; no square of the curve; no Hodge index on it) are negative results from that sweep and should be re-checked before any circulated draft relies on them.*
