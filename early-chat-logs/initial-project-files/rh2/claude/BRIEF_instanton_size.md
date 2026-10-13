# The Instanton-Size Reading of Hyperbolicity

**A self-contained brief.** Assumes no prior context: everything used is stated and, where short, proved. Covers one approach only — the identification of the Riemann `Ξ`-function with a Yang–Mills determinant via its *product* representation — and carries it to a verdict.

*Assembled 2026-08-24. Certified by `lab_product_object.py`, `lab_size_detector.py`, `lab_detector_class.py`. Primary source for the gauge theory: N. Dorey, T. J. Hollowood, V. V. Khoze, M. P. Mattis, "The Calculus of Many Instantons", Phys. Rept. **371** (2002) 231–459, hep-th/0206063 — cited below as **DHKM** with equation numbers.*

---

## 0. Summary and verdict

The approach: `Ξ` has a Hadamard **product** over its zeros, and the natural product-shaped object of instanton theory is the determinant `det(Δ†Δ)` of the ADHM matrix. Matching them turns out to be exact enough to build a complete dictionary, and the dictionary identifies the imaginary part of a zero of `Ξ` with the **scale size** of an instanton.

**What the approach delivers.** A single parameter accounts for six phenomena that had been recorded separately; a two-line proof of a matching-rigidity theorem valid for every topological charge and every classical gauge group; a reformulation of RH as a statement about instanton sizes shrinking like `1/\log T`, which is the first version of the target that is not finite-dimensional; and a proof that the choice of gauge group cannot matter.

**What it does not deliver, and why not.** The criterion it produces — "every instanton size vanishes" — is *correct and complete* and therefore not refuted by the one universal no-go in this subject (§1.4). It fails instead on **circularity**: the geometric hypothesis is a relabelling of hyperbolicity. Circularity alone is not disqualifying, because every serious attack on RH is a criterion plus a verification (§6.2). What is disqualifying is *where* the relabelling lands. The instanton size is a **free modulus** — unconstrained precisely because Yang–Mills is conformally invariant in dimension four — so no equation, bound, or quantisation in the theory bears on whether it vanishes. And the one known mechanism that makes the size determinate, a noncommutative deformation, **bounds it away from zero** (§6.4): it forces non-real zeros rather than forbidding them.

> **Verdict: not viable as a route to a proof.** Not because it resembles earlier failures, but because the geometry's only handle on the answer is a parameter the geometry deliberately leaves free.

---

## 1. The problem, and the one constraint that binds every approach

### 1.1 The target

Let

`Ξ(z) = 4∫_0^∞ Φ(u)\cos(zu)\,du`,  `Φ(u) = Σ_{n≥1}(2π²n⁴e^{9u/2} − 3πn²e^{5u/2})e^{−πn²e^{2u}}`,

the Riemann `Ξ`-function: real, entire, of order 1. The Riemann Hypothesis is equivalent to

> **all zeros of `Ξ` are real** — `Ξ` is *hyperbolic*.

A real entire function is hyperbolic iff every one of its Jensen polynomials is. With `M_k = ∫_0^∞Φ(u)u^k\,du > 0`, `b_m = 4M_{2m}/(2m)!`, `γ(m) = m!\,b_m`, the Jensen polynomials are `J^{d,n}(X) = Σ_{j=0}^d\binom{d}{j}γ(n+j)X^j`, and **RH ⟺ every `J^{d,n}` is hyperbolic** (Pólya). So the problem reduces to hyperbolicity of a family of real polynomials whose coefficients are explicit moments. Calibration: `4M_0 = 0.4971207782` against `ξ(1/2) = 0.4971207174`.

### 1.2 Sum versus product

`Ξ` admits two canonical representations, and they behave very differently under any geometric dictionary.

- **The sum form** — the Taylor/moment expansion `Σ b_m w^m` with `w = −z²`, and its truncations `J^{d,n}`. Coefficients are the natural data.
- **The product form** — the Hadamard product `Ξ(z) = Ξ(0)∏_ρ(1 − z²/γ_ρ²)`. Zeros are the natural data.

Gauge theory's canonical scalar invariants are **determinants**: `det(Δ†Δ)`, Fredholm determinants, partition functions. A determinant is a product over eigenvalues. So if a dictionary is to send a canonical object of one theory to a canonical object of the other, it must be the product form that maps. This is the premise of the present approach, and §3–§4 show it is the right one: the match is exact, not approximate.

### 1.3 What a detector must be

A *detector* is a function `D` of the data of a real polynomial (or entire function) with `D = 0` (or `D ≥ 0`, or `D` taking a distinguished value) exactly on the hyperbolic locus. Two constraints on the shape of `D` are needed below; both are elementary and both are universal.

### 1.4 Constraint I — hyperbolicity is not a complex-analytic set

Fix `d`. Parametrise monic degree-`d` polynomials by their coefficient vector, allowing complex coefficients, so the parameter space is `P_d ≅ ℂ^d` with the real ones forming `ℝ^d ⊂ ℂ^d`. Let `H = {a : p_a` has all roots real`}`, so `H ⊂ ℝ^d`.

> **Theorem.** There is no connected open `U ⊆ ℂ^d` meeting `ℝ^d` and no finite family of holomorphic functions `h_1,…,h_m` on `U` with `H ∩ U = \{h_1 = ⋯ = h_m = 0\}`.

*Proof.* Polynomials with `d` distinct real roots form a nonempty **open** subset `W` of `ℝ^d`, all hyperbolic, so each `h_j` vanishes on `W ∩ U`. But `ℝ^d` is maximally totally real in `ℂ^d`: the Taylor coefficients of a holomorphic function at a point of `W` are its iterated *real* partial derivatives, all of which vanish there. So `h_j ≡ 0` near that point and hence on `U`. Then every point of `U` would be hyperbolic — false, since `U` contains points with non-real coefficients. `∎`

**Corollary (both parities).** `H` is not the complement of an analytic set either: complements of proper analytic subsets are open and dense, while `H` has empty interior in `ℂ^d`. Genericity and non-degeneracy conditions are excluded too.

**In one sentence:** field equations are *equations*; hyperbolicity is a closed region with nonempty interior in a real parameter space. A holomorphic equation reaches the *boundary* of hyperbolicity — `\mathrm{disc}(p) = 0`, where two roots collide — and never hyperbolicity itself.

### 1.5 Constraint II — no deformation invariant, and no complex-side chamber invariant

- `P_d ≅ ℂ^d` is **connected**. So any quantity invariant under continuous deformation of the polynomial is constant, and cannot have `H` as a level set. This excludes every characteristic class, index, degree, charge, winding number and Thom polynomial, in any ambient space, for any construction.
- `P_d ∖ \{\mathrm{disc} = 0\}` is **also connected** (the complement of a proper algebraic hypersurface in an irreducible variety). So a quantity merely *locally constant on the complex discriminant complement* is constant too — braid-monodromy and complex chamber invariants are excluded as well. Certified: `z² + a` with `a = e^{iθ}`, `θ: π → 0`, joins `z²−1` (two real roots) to `z²+1` (none) with `\min|\mathrm{disc}| = 4`; at `d = 4` an imaginary detour joins `z⁴−5z²+4` to `z⁴+5z²+4` with `\min|\mathrm{disc}| = 3217`. The same interpolation kept **real** must cross the discriminant (`\min|\mathrm{disc}| = 7.8\text{e}{-}28`).
- `ℝ^d ∖ \{\mathrm{disc} = 0\}` is **disconnected**, and `\{p : d` distinct real roots`\}` is a union of its connected components — a real root can leave `ℝ` only by colliding with another. `H` is its closure.

> **A detector must be an invariant of the real structure that jumps across the real discriminant, and must not extend to the complex parameter space — not holomorphically (§1.4), and not even locally constantly.**

The classical detectors are of exactly this type: the **Bezoutian** signature (Hermite: `\mathrm{rank}` of the Hankel matrix of Newton sums `= \#`distinct roots, `\mathrm{signature} = \#`distinct **real** roots) and the **De Bruijn–Newman threshold** `Λ(p) = \inf\{t : e^{−t∂_z²}p` is hyperbolic`\}`, with `Λ(p) ≤ 0` iff `p` is hyperbolic. Both are complete. Keep them in view: §4 will land on a third member of the same family.

---

## 2. The gauge-theoretic side

### 2.1 ADHM data

Instantons — anti-self-dual Yang–Mills connections on `ℝ⁴` of finite action — are classified by the ADHM construction. In DHKM's conventions, for gauge group `SU(N)` and topological charge `k`, let

`Δ_{λ i \dotα}(x) = a_{λ i\dotα} + b^{β}_{λ i}x_{β\dotα}`,  `λ = 1,…,N+2k`, `i = 1,…,k`,

with `x` written quaternionically (DHKM 2.8–2.9, 2.45). The gauge field is built from the `N`-dimensional null space `U` of `\bar Δ` (2.47–2.49), and the construction closes iff

`\barΔ^{\dotα}Δ_{\dotβ} = δ^{\dotα}_{\dotβ}(f^{-1})`,  `f` a Hermitian `k×k` matrix (DHKM 2.50).

Using the residual `U(N+2k)×GL(k,ℂ)` freedom, `b` can be put in canonical form (DHKM 2.57), which satisfies `\bar b_α b^β = δ_α^β 1_k` (2.61) and splits the remaining data as

> `a = \binom{w_{u i\dotα}}{(a'_{αα})_{ij}}`,  `w` an `N×k` block, `a'_n` four `k×k` **Hermitian** matrices (DHKM 2.58–2.60),

subject to the ADHM constraints `\vecτ^{\dotα}_{\dotβ}(\bar a^{\dotβ}a_{\dotα}) = 0` (2.65). Then

> **`f^{-1} = 2\bar w^{\dotα}w_{\dotα} + Σ_{n=1}^{4}(a'_n + x_n 1_k)²`** (DHKM 2.62).

The two blocks have clean meanings. The `a'_n` are the **position** matrices: on the commuting locus their simultaneous eigenvalues are the instanton centres. The `w` block carries the **scale sizes** and gauge orientations; `|w_i|²` is (twice) the squared size of the `i`-th instanton. Regularity of the datum — that it is a genuine instanton rather than a singular limit — is exactly that `f^{-1}` is nowhere singular.

### 2.2 The product object

`\barΔΔ` is `f^{-1}` tensored with the `2×2` spinor identity, so `\det(Δ†Δ) = (\det f^{-1})²`, and

> the natural product-shaped scalar of the theory is `\det f^{-1}(x)`, a polynomial in `x ∈ ℝ⁴` of degree `2k`.

This is the object to be matched against `Ξ`'s Hadamard product.

### 2.3 The curvature and the action, from a primary source

DHKM derive the field strength in four lines from the null-space projector:

`F_{mn} = 4g^{-1}\bar U\, b\,σ_{mn} f\,\bar b\, U` (DHKM 2.52), `f = (\barΔΔ)^{-1}`.

With canonical `b` this reads `F_{mn} = 4g^{-1}Σ_{i,j}f_{ij}\,c_i σ_{mn}\bar c_j` with `c_i` the `i`-th instanton block of `\bar U` (an `N×2` matrix); at `N = 2` DHKM's index convention makes the gauge index the same undotted spinor index, so each `c_i` is a **quaternion**. And immediately after (2.52), quoting an identity of Osborn proved in their Appendix C:

> **`-\tfrac{g²}{16π²}∫ \mathrm{tr}_N F_{mn}² = \tfrac{1}{16π²}∫ □²\,\mathrm{tr}_k \log f`.**

So the Yang–Mills action density is `□²` of the logarithm of the product object. §3 shows what that means.

---

## 3. Three exact facts

### 3.1 `\log|x|` is the biharmonic Green's function of `ℝ⁴`

For a radial `F(r)` in `ℝ⁴`, `□F = F'' + 3F'/r`. Then `□\log r = -r^{-2} + 3r^{-2} = 2/r²`, and `□(2/r²) = 6r^{-4} - 6r^{-4} = 0`. Since `1/(4π²r²)` is the Laplace Green's function of `ℝ⁴`,

> **`□²\log|x| = -8π²δ(x)`,  hence `□²\log∏_i|x − X_i|² = -16π²Σ_iδ(x − X_i)`.**

**So the logarithm of a product object on `ℝ⁴` is a biharmonic potential whose point charges sit at the zeros of the product.** Combined with §2.3, the Yang–Mills action density *is* that potential's charge density. This is a second, independent reason the dimension must be four — the first being conformal invariance of the Yang–Mills functional — and it involves no quaternions and no symmetry assumption.

### 3.2 Charge one, exactly

For `k = 1` centred at the origin, `\mathrm{tr}_k\log f = -\log(|x|² + c)` with `c = 2ρ²`, `ρ` the scale size. Writing `s = r² + c` and using `□(1/s) = -8c/s³`, `□(1/s²) = (8r² - 16c)/s⁴`:

> **`□²\bigl(-\log(r²+c)\bigr) = 96c²/(r²+c)⁴ > 0`,  and `∫_{ℝ⁴} = 16π²` for every `c > 0`.**

Verified symbolically and numerically to 12 digits (`157.913670417` against `16π²`). The density is smooth and strictly positive, and its total is exactly one unit of topological charge, independent of the size. As `c → 0` the mass inside `r < 0.1` is

| `c` | `1` | `10^{-1}` | `10^{-2}` | `10^{-3}` | `10^{-4}` |
|---|---|---|---|---|---|
| fraction of `16π²` | `0.0003` | `0.023` | `0.500` | `0.977` | `0.9997` |

> **A zero-size instanton is exactly a point mass `16π²δ` of the biharmonic potential.**

### 3.3 The 't Hooft factorisation, and what a nonzero size buys

Take 't Hooft data: `a'_n` diagonal with entries `-X_{i,n}` (so `Σ_n(a'_n + x_n)² = \mathrm{diag}(|x - X_i|²)`), and all `w_i` aligned, so `2\bar w w = 2ρρ^{\mathsf T}` is rank one. The matrix-determinant lemma gives

> **`\det f^{-1} = φ(x)·∏_i|x − X_i|²`,  `φ = 1 + Σ_i 2ρ_i²/|x − X_i|²`** — the classical 't Hooft `φ`.

Verified to `3.2\text{e}{-}15` over 400 random points at each `k ≤ 5`. Now read the two factors against §3.1. The product `∏|x - X_i|²` contributes `-16π²Σδ(x - X_i)`. Near a centre, `φ ∼ 2ρ_i²/|x - X_i|²`, so `\logφ` contributes exactly the opposite point mass. **The singularities cancel**: measured `\log\det f^{-1} → -0.4764241928` as `x → X_0` against the predicted `\log(2ρ_0²∏_{i>0}d_i) = -0.4764241970`. What remains is the smooth positive density of §3.2.

Set every size to zero. Then `φ ≡ 1`, the cancellation switches off, and

> `□²\log\det f^{-1} = 16π²Σ_iδ(x - X_i)`: `k` bare point charges and **no field at all**.

This is the mechanism of the whole approach in one line. A nonzero size is precisely what converts point charges into a smooth Yang–Mills field.

---

## 4. The dictionary

### 4.1 The identification

For `k = 1` with a real centre `X`, writing `x = (x_0, \vec x)` and `r = |\vec x|`,

`\det f^{-1} = (x_0 - X)² + r² + 2ρ².`

The matching family of the product dictionary produces factors of exactly the shape `B_j = (x_0 - τ_j)² + r² + σ_j²` where `τ_j + iσ_j` is a root of the target polynomial — i.e. `σ_j` is the imaginary part of a zero. Comparing,

> **`\mathrm{Im}(\text{zero}) = \sqrt2 \,·\, (\text{instanton scale size})`.**

### 4.2 What the identification absorbs

Every recurring quantity in the gauge-theoretic attack on hyperbolicity becomes one parameter.

| quantity | is |
|---|---|
| `\mathrm{Im}(ρ)` for a zero | `\sqrt2 ×` the instanton scale size |
| `w = 0`, forced by every matching-rigidity theorem | every instanton has **zero size** |
| "the matched datum is not a regular ADHM datum" | it lies on the small-instanton boundary of moduli space |
| `Λ(z² + y_0²) = y_0²/2`, the De Bruijn–Newman threshold | `Λ = ρ²`, the size squared — verified to 8 digits |
| Rodgers–Tao's theorem `Λ ≥ 0` | `ρ² ≥ 0`. Automatic, and empty. |
| Newman's conjecture `Λ = 0` | the configuration sits **exactly on** that boundary |
| the instanton effective action in a Higgs background, DHKM (5.36) `8π²\,\mathrm{tr}_k(\bar w φ⁰φ⁰ w) ∝ ρ²|v|²` | the universal `y_0²/2` law, with `|v|²` its configuration-dependent constant |

### 4.3 The reformulation of RH

The mean gap between zeros at height `T` is `Δ_T ≈ 4π/\log T`, and the Lehmer-pair bound gives margin `≈ Δ_T²/8`. Translating through §4.1, the zero at height `T` corresponds to an instanton of size

> `ρ_T ≈ π\sqrt2/\log T`.

So RH becomes a statement about an **infinite-charge configuration whose scale sizes shrink like `1/\log T`** — an accumulation on the boundary of the Uhlenbeck compactification of instanton moduli space. This is the only version of the target in this line of work that is not a finite-dimensional matching problem. It does not answer the objection that finite constructions probe the easy part of the problem, but it is the first statement of the right shape to.

### 4.4 The detector the dictionary hands us

The functional the geometry produces is the total size squared, `Σ_iρ_i² = \tfrac12Σ_ρ\mathrm{Im}(ρ)²`. On `p = z² + a` with `a` real: the roots are `±\sqrt{-a}`, so `Σ|ρ|² = 2|a|` while `Σρ² = -2a`, giving

> **`Σ_ρ\mathrm{Im}(ρ)² = |a| + a = 2\,\mathrm{ReLU}(a)`.**

Continuous, non-negative, vanishing *exactly* on the hyperbolic region, kink exactly on the discriminant, and **not real-analytic** — precisely the shape §1.5 requires and §1.4 permits. Its analytic part `Σρ²` is Turán's inequality, which is why Turán is only *necessary*. On a standard test set it is complete, catching both the barely-non-hyperbolic quartic `X⁴+10X³+26X²+22X+3` (`6.6\text{e}{-}03`) and shielded cases that defeat the Laguerre certificate.

And `Σ|ρ|² = Σ_ρ ρ·\barρ` is **not a symmetric function of the roots** — the pairing with the conjugate is not permutation-invariant, and `2|a|` is the witness. So:

> **The geometry computes exactly the quantity the coefficients cannot.** Symmetric functions give the power sums, hence the Bezoutian; the geometry gives `Σ\mathrm{Im}²`; the gap between them is the entire problem.

---

## 5. The matching theorem, in general form

The dictionary makes the rigidity theorem trivial, and general.

Write `f^{-1} = W + D(x)` with `W = 2\bar w^{\dotα}w_{\dotα} ⪰ 0` (independent of `x`) and `D(x) = Σ_n(a'_n + x_n)²`. Since `\det(D + W) = \det D·\det(1 + D^{-1}W)` and `D^{-1}W` is similar to `D^{-1/2}WD^{-1/2} ⪰ 0`:

> **(a)** `\det f^{-1} ≥ \det D` pointwise, with equality identically iff `W = 0`, i.e. iff `w = 0`.

Next, `\det D(x) = 0` at a real `x` iff the Hermitian matrices `a'_n + x_n` have a common null vector, i.e. iff `-x` is a **simultaneous eigenvalue** of `(a'_1,…,a'_4)`. Certified by direct search over `x ∈ ℝ⁴`, 25 restarts:

| `a'_n` | `k=2` | `k=3` | `k=4` |
|---|---|---|---|
| commuting | `-1.3\text{e}{-}14` | `-2.7\text{e}{-}13` | `-1.0\text{e}{-}12` |
| generic non-commuting | `1.5\text{e}{+}01` | `1.0\text{e}{+}03` | `3.3\text{e}{+}04` |

> **(b)** The roots of the product object are the simultaneous eigenvalues of the position matrices. Non-commuting positions give a product object with **no real roots at all**.

Combining:

> **Theorem.** `\det(Δ†Δ)` is (the square of) a product of `k` real quadratic factors `∏_i|x - X_i|²` **iff** `w = 0` and `[a'_m, a'_n] = 0` — iff the datum is `k` point-like, zero-size instantons at `k` points of `ℝ⁴`.

This holds for every charge `k`. It also holds for **every classical gauge group**: `w` is `N×k` and enters `f^{-1}` *without* `x`, so `N` affects only the constant term. Verified: `\deg_x\det f^{-1} = 2k` for `N = 2,3,4,6` and `k = 1,2,3`, while `\dim\mathcal M_k = 4kN` grows. The argument above is entirely a statement about `k×k` Hermitian matrices plus a positive semidefinite perturbation, so it is identical for `SU(N)`, `Sp(N)`, `SO(N)`; and ADHM has no exceptional-group case at all.

> **The gauge group cannot matter. A larger group buys moduli, not factors.**

This closes the "try a different Lie group" question rather than leaving it open — not because other groups were tried and failed, but because the argument does not see the group.

---

## 6. The verdict, and what kind of failure it is

### 6.1 Three kinds of screen

Screening criteria for proposals of this sort divide into three logically distinct classes, and conflating them is the commonest error in reading a result like this one.

| type | what it says | consequence of failing |
|---|---|---|
| **A — impossibility** | no object of this *kind* can ever detect hyperbolicity (§1.4, §1.5) | **refuted.** The family is closed permanently. |
| **B — circularity** | the object *does* detect hyperbolicity, correctly and completely, but the detection is a relabelling | **not refuted.** The work has been moved, not done. |
| **C — heuristic flag** | family-specific patterns with a good track record | **flagged**, not refuted. |

### 6.2 Which fired

The instanton-size reading **passes** every Type A screen. `Σρ_i² = 0` is not the vanishing of a holomorphically-varying quantity — it is an equality case of an inequality on a real parameter, so §1.4 does not touch it. And `Σ\mathrm{Im}²` is a non-analytic real chamber object, not a class or an index, so §1.5 does not touch it either. **The approach is not refuted.** That is a genuine and slightly surprising outcome: most gauge-theoretic proposals die at §1.4 in one line.

What fires is Type B. `Σρ_i² = 0 ⟺ w = 0 ⟺` hyperbolic is a relabelling, and the positivity carrying it — `|w|² ≥ 0` — is *literally* `\mathrm{Im}(\text{root})² ≥ 0`.

Circularity by itself is not disqualifying, and it is important to be clear about this. **Every serious attack on RH is a criterion plus a verification, and every one of them is a relabelling at the criterion stage:** Weil positivity `⟺` RH; Hilbert–Pólya self-adjointness `⟺` reality of the spectrum; Li's criterion `⟺` RH; `Λ ≤ 0 ⟺` RH; the Bezoutian being positive semidefinite `⟺` RH. Being a criterion is not the defect. Being a *useless* criterion is.

### 6.3 What separates a useful relabelling from a useless one

One thing: whether the membership condition is **independently accessible** — whether some other body of mathematics can supply it. Weil positivity is a useful relabelling in the function-field case because the Hodge index theorem on a surface over `𝔽_q` supplies the inequality from a completely different direction, on a rigid integral lattice. The relabelling moved the problem somewhere that had its own tools.

Applied here: **is there an independent route to "every instanton size vanishes"?**

No, and the reason is structural rather than circumstantial. The scale size is a **free modulus** of the theory. That is not an artefact of the ADHM parametrisation; it is conformal invariance of `∫|F|²` in dimension four, which makes the action of an instanton independent of its size. There is no equation constraining a size, no bound, no quantisation, no selection principle — the entire content of the moduli space is that these parameters are unconstrained. So the relabelling lands on the most structureless data in the theory. Of all the places a criterion could be moved to, this is the worst.

### 6.4 The one mechanism that fixes the size points the wrong way

Since the size is free *because* the action is scale invariant, any scale-breaking makes it determinate. Two mechanisms exist and neither helps.

- **A Higgs vacuum expectation value.** Derrick's theorem applies, and DHKM (5.36) give the bosonic instanton effective action as `8π²\,\mathrm{tr}_k(\bar w^{\dotα}φ⁰φ⁰w_{\dotα}) ∝ ρ²|v|²`. This *is* the universal `y_0²/2` law of §4.2, so it explains that law — but `Σρ_i² = 0` remains an equality case of a structural positivity, i.e. still `\mathrm{Im}² ≥ 0`. Circular, and now visibly so.
- **A noncommutative deformation.** The ADHM constraints become `\vecτ(\bar a a) = \vecζ`, with `\vecζ` the anti-self-dual part of the noncommutativity parameter (DHKM §on non-commutative spacetime). At `k = 1` the `a'` contribution to the traceless part vanishes identically, leaving `\vecτ(\bar w w) = \vecζ` and hence `|w|² ≥ |\vecζ|`. The small-instanton singularity is resolved and sizes are **bounded away from zero** (Nekrasov–Schwarz). Under §4.1 that reads `\mathrm{Im}(\text{root})² ≥ |\vecζ|`:

> **the deformation that makes the size determinate forbids it from vanishing** — it *forces* non-real zeros instead of forbidding them.

That is the rigidity/existence trade-off in its sharpest instance: the structure needed to constrain the discriminating parameter is the structure that makes the desired conclusion impossible.

### 6.5 Leaving dimension four

For completeness, since §3.1 and §6.3 both turn on dimension four: in dimension `d`, `∫|F|²` scales as `ρ^{d-4}`, so away from `d = 4` the size is driven to `0` or `∞` rather than to an interior value. A pure Yang–Mills functional never fixes a size at a finite nonzero value in any dimension; only a second scale (a vacuum expectation value, a higher-order term, a deformation parameter) does, and §6.4 covers those. So the observation that "the size is free only because `d = 4`" is true but does not point anywhere: it identifies scale-breaking, not dimension, as the operative variable, and scale-breaking is already exhausted.

---

## 7. What survives

Three things, none of them a route to a proof.

1. **The screens become predictive.** One can now say in advance why a gauge-theoretic proposal of this family will fail: it will end by asking a modulus to vanish. Six previously separate observations — the forced `w = 0`, the forced commutativity, `Λ = y_0²/2`, "outside the moduli space", "structural positivity is the trap", "the difficulty is at `T → ∞`" — are one parameter seen six ways.
2. **A small theorem.** §5 generalises matching rigidity to every charge and every classical gauge group, from a two-line matrix inequality, replacing computations that were specific to `SU(2)` and to quaternionic symmetry. The novelty prior should be that `\det(D+W) ≥ \det D` applied to ADHM data is known.
3. **A reformulation.** §4.3's `ρ_T ∼ π\sqrt2/\log T` accumulation on the Uhlenbeck boundary is worth recording as a statement about `Ξ` in gauge-theoretic language, independent of whether anything can be proved from it.

And one statement of where the difficulty actually is, which this approach sharpens rather than solves. The Bezoutian of a polynomial with rational coefficients is automatically rational — the Newton sums are integer polynomials in the coefficients. So the classical obstruction to a Weil-style argument is not a defect of the quadratic form: the form varies with the data *and* is defined over `ℚ` by construction. The obstruction is that `Ξ`'s coefficients `b_m = 4M_{2m}/(2m)!` have no known `ℚ`-structure.

> **The missing ingredient is arithmetic, not geometric.** No choice of manifold, gauge group, dimension, or moduli space supplies rationality of the moments of `Φ`.

---

## 8. Status of every claim

**Verified from a primary source.** DHKM (2.52) and its derivation; the canonical form (2.57) with (2.61) and (2.62); the splitting (2.58)–(2.60) with `a'_n` Hermitian; Osborn's identity as DHKM state it after (2.52) (their Appendix C proof was not read); the constrained-instanton discussion of §IV.4 and the effective action (5.36); the noncommutative modification of the constraints.

**Proved here.** §1.4 and its corollary. §1.5's three connectivity statements (a locally constant function on a connected space is constant; the complement of a proper hypersurface in an irreducible variety is connected). §3.1 (three lines of radial calculus plus the standard `ℝ⁴` Green's function). §3.2 exactly, including the `16π²` normalisation for every `c`. §5(a) (`\det(D+W) ≥ \det D` for `W ⪰ 0`, `D ≻ 0`, equality iff `W = 0`) and the theorem it yields. §5's degree count. §4.4's `2\,\mathrm{ReLU}(a)` identity and the non-symmetry of `Σ|ρ|²`. §6.4's `k = 1` bound `|w|² ≥ |\vecζ|`.

**Measured.** §3.2's concentration table; §3.3's factorisation (`3.2\text{e}{-}15` at `k ≤ 5`) and singularity cancellation (agreement to `4\text{e}{-}9`); §5's simultaneous-eigenvalue search; §4.2's `Λ = ρ²` to 8 digits; §4.4's test set; §1.5's explicit complex paths.

**Dictionary-level, not theorems.** `\mathrm{Im}(\text{root}) = \sqrt2ρ` is exact inside the charge-one and commuting-diagonal families where the `B_j` shape applies; beyond them it is a correspondence read off matching shapes. §4.3's `ρ_T ∼ π\sqrt2/\log T` inherits that status — it is a translation of the Lehmer-pair bound, not a derivation. §4.2's identification of `y_0²/2` with the instanton effective action is a shape match with the right parametric dependence, not a computed equality.

**Novelty.** Osborn's identity, the biharmonic Green's function of `ℝ⁴`, the 't Hooft `φ` as a determinant factor, `\det(D+W) ≥ \det D`, and Nekrasov–Schwarz resolution are all standard. The identification of the `y_0²/2` law with the instanton scale size is the only item here that appears to be new, and it is a dictionary rather than a result. Assume everything else is known until checked.

**Not done.** No independent derivation of Osborn's identity. No test of whether §5(a)'s inequality has content on the non-commuting locus, which would give a dictionary between conjugate pairs and commutator norms. No `(d,n)` map of the Bezoutian margin, which would measure §4.3's `1/\log T` law directly.

---

## 9. Reproduction

| file | certifies |
|---|---|
| `lab_product_object.py` | §3.1 (symbolic), §3.2 (symbolic and numeric), §3.3 (factorisation and cancellation), §5(b) (the simultaneous-eigenvalue search), §5's degree count |
| `lab_size_detector.py` | §4.4 (`2\,\mathrm{ReLU}`, the test set), §4.2's `Λ = ρ²` |
| `lab_detector_class.py` | §1.5's connectivity paths, and the Bezoutian signature as a complete detector on the standard test set |

Dependencies: `numpy`, `sympy`, `mpmath`, `scipy`. Searches are multi-start Nelder–Mead; the ten-to-fifteen-order gap between the commuting and non-commuting rows in §5 is the signal, not the absolute value.
