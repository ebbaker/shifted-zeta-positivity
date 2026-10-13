# What `Ξ` Becomes: a Determinant, a Biharmonic Potential, and a Set of Instanton Sizes

*Working memo #25 — August 24, 2026. Takes up two pieces of context from the previous thread: that the **product** formula is the natural one in the gauge-theoretic setting, and that other Lie groups deserve a look. Both are answered. The product reading has an exact realisation, it identifies every recurring quantity in this project with a known physical one, and the gauge group turns out to be irrelevant for a reason that is provable in two lines. Certified by `lab_product_object.py` and `lab_size_detector.py`. Primary sources: Dorey–Hollowood–Khoze–Mattis, hep-th/0206063, Eqs. (2.52), (2.57), (2.61), (2.62), (5.36).*

---

## 0. Results

### (1) The dictionary, and why the product formula is the natural one

A determinant **is** a product. The natural product object of ADHM is `det(Δ†Δ) = (det f⁻¹)²` with `f⁻¹ = 2w̄^α̇w_α̇ + Σ_n(a'_n + x_n)²` (DHKM 2.62), the `a'_n` being `k×k` Hermitian **position** matrices and `w` the `N×k` **size/orientation** data. Four exact statements:

**(a) `log|x|` is the biharmonic Green's function of `ℝ⁴`.** `□ log r = 2/r²` and `□(2/r²) = 0`, and `1/(4π²r²)` is the Laplace Green's function in four dimensions, so `□² log r = −8π²δ`. **So the logarithm of a product object on `ℝ⁴` is a biharmonic potential whose charges are the zeros of the product.** This is a second, independent place where dimension 4 is forced — the first being conformal invariance of Yang–Mills. Nothing about spheres or quaternions is used.

**(b) Osborn's identity makes the action density that potential's charge density.** DHKM record (after 2.52, proved in their Appendix C) that `−(g²/16π²)∫tr F²= (1/16π²)∫□² tr_k log f`. So

> `Yang–Mills action density = □² log det(Δ†Δ)⁻¹`, i.e. the action *is* the biharmonic charge density of `log` of the product object.

**(c) Charge 1, exactly.** With `tr_k log f = −log(|x|² + c)`, `c = 2ρ²`:

`□²(−log(r²+c)) = 96c²/(r²+c)⁴ > 0`,  `∫_{ℝ⁴} = 16π²` for **every** `c`.

Verified symbolically and to 12 digits. And the mass inside `r < 0.1` is `0.0003, 0.023, 0.500, 0.977, 0.9997` for `c = 1, 10⁻¹, …, 10⁻⁴`: the smooth density converges to `16π²δ`. **A zero-size instanton is exactly a point mass of the biharmonic potential.**

**(d) The point masses cancel, and only a nonzero size buys the cancellation.** For 't Hooft data (`a'` diagonal at centres `X_i`, all `w_i` aligned so `2w̄w = 2ρρᵀ` is rank one) the matrix-determinant lemma gives, verified to `3.2e−15` over 400 random points at `k ≤ 5`:

> `det f⁻¹ = φ(x)·∏_i |x − X_i|²`,  `φ = 1 + Σ_i 2ρ_i²/|x−X_i|²` — the 't Hooft `φ`.

Near a centre `φ ~ 2ρ_i²/|x−X_i|²`, so the two logarithmic singularities of `log φ + Σ log|x−X_i|²` **cancel**: measured `log det f⁻¹ → −0.4764241928` against the predicted `log(2ρ_0²∏_{i>0}d_i) = −0.4764241970`. With every size set to zero, `φ ≡ 1`, the cancellation switches off, and `□² log det f⁻¹` is `16π²Σ_iδ(x−X_i)` — `k` point charges and no field.

### (2) The size dictionary — this is the substantive item

For `k = 1` with a real centre, `det f⁻¹ = (x_0−X)² + r² + 2ρ²`. Compare brief §2.5's `B_j = (x_0−τ_j)² + r² + σ_j²`, where `σ_j = Im(root)` by Theorem B (`p(v) = ∏(v − τ_j − iσ_j)`). So

> **`Im(root) = √2 · (instanton size)`.**

Everything the project has repeatedly bumped into is now one quantity:

| project object | is |
|---|---|
| `Im(ρ)` of a zero | `√2 ×` the instanton scale size |
| `λ = 0` / `w = 0`, forced in Theorems A **and** B | every instanton has **zero size** |
| "the matched datum is not a regular ADHM datum" (§3.8) | it is a point on the small-instanton boundary |
| `Λ(z²+y_0²) = y_0²/2` (§6.4) | `Λ = ρ²`, the size squared — verified to 8 digits |
| Rodgers–Tao `Λ ≥ 0` | `ρ² ≥ 0`. Automatic. |
| Newman's conjecture `Λ = 0` | the configuration sits **exactly on** the small-instanton boundary |
| §2.6's "difficulty is at `T → ∞`, invisible at finite degree" | sizes `→ 0` only in the limit; every finite truncation is interior |

The last row is worth spelling out. The mean gap at height `T` is `Δ_T ≈ 4π/\log T` and the Lehmer-pair bound gives margin `≈ Δ_T²/8`, so under this dictionary the zero at height `T` corresponds to an instanton of size `ρ_T ≈ π√2/\log T`. **RH becomes a statement about an infinite-charge configuration whose sizes shrink like `1/\log T`** — an accumulation on the Uhlenbeck boundary, which is precisely the object no finite-dimensional construction can be.

### (3) The roots exist only on the commuting locus

`det[Σ_n(a'_n+x_n)²] = 0` at a real `x` iff the four Hermitian `a'_n` have a common eigenvector with eigenvalues `−x_n` — i.e. iff `−x` is a **simultaneous eigenvalue**. Searched over `x ∈ ℝ⁴`, 25 restarts:

| `a'_n` | `k=2` | `k=3` | `k=4` |
|---|---|---|---|
| commuting | `−1.3e−14` | `−2.7e−13` | `−1.0e−12` |
| generic non-commuting | `1.5e+01` | `1.0e+03` | `3.3e+04` |

> **The roots of the product object are the simultaneous eigenvalues of the ADHM position matrices. Non-commuting positions give a product object with no real roots at all.**

And since `det f⁻¹ = det[2w̄w + Σ(a'_n+x_n)²] ≥ det[Σ(a'_n+x_n)²]` for `w̄w ⪰ 0`, with equality identically iff `w = 0`:

> **"`det Δ†Δ` is a product of `k` real quadratic factors" ⟺ `w = 0` and `[a'_m, a'_n] = 0` ⟺ `k` point-like instantons at `k` points of `ℝ⁴`.**

That is brief Theorem 4 (§4.4), **re-proved in two lines from a matrix inequality, for every charge and every classical gauge group**, replacing the `SU(2)` quaternionic trace computation. It also explains §4.3's noncommutativity census: matching forces commutativity because commutativity is what makes the roots exist.

### (4) Different Lie groups: provably irrelevant

`w` is `N×k` and enters `f⁻¹` **without `x`**. So `N` changes only the constant term. Verified for `N = 2,3,4,6` and `k = 1,2,3`: `deg_x det f⁻¹ = 2k` in every case, while `dim M_k = 4kN` grows.

> **The shape of the product object is set by the charge `k` alone. A larger gauge group buys moduli, not factors.** And §0(3) is entirely a statement about `k×k` Hermitian matrices and a PSD perturbation, so it is *identical* for `SU(N)`, `Sp(N)`, `SO(N)`. ADHM has no exceptional-group case at all (DHKM §I), so classical groups are the whole field.

This closes the Lie-group question rather than leaving it open: it is not that other groups were untried, it is that the argument does not see the group.

### (5) The detector the dictionary hands us is exactly memo 24's admissible shape

The functional the geometry produces is the **total size squared**, `Σ_iρ_i² = ½Σ_ρ Im(ρ)²`. On `p = z² + a` with `a` real: roots `±√(−a)`, `Σ|ρ|² = 2|a|`, `s_2 = Σρ² = −2a`, so

> `Σ_ρ Im(ρ)² = 2·ReLU(a)`.

Continuous, non-negative, vanishing **exactly** on the hyperbolic region, with its kink **on the discriminant** — and not real-analytic. That is precisely the object memo 24 §0(3) proved a detector must be, and precisely what brief §1.5 says no holomorphic function can be. Its analytic part `s_2` is Turán's inequality, which is why Turán is only necessary. Run on the standard test set it is complete (near-miss quartic `6.6e−03`; both shielded cases caught).

**And it is not a polynomial in the coefficients.** `Σ|ρ|² = Σρ·σ(ρ)` involves the conjugation pairing, which is not permutation-symmetric — the `2|a|` above is the witness. So:

> **The geometry computes exactly the quantity the coefficients cannot.** The symmetric functions give the power sums (hence the Bezoutian, memo 24 §0(4)); the geometry gives `Σ Im²`; the gap between them is the whole problem.

### (6) The one place where scale-breaking would matter — and where it fails

The sizes are **free moduli** precisely because Yang–Mills is conformally invariant in dimension 4. Turn on a scalar VEV and Derrick's theorem applies: DHKM (5.36) gives the bosonic instanton effective action `g̃(Ṽ,Ṽ) = 8π² tr_k(w̄^α̇φ⁰φ⁰w_α̇)`, quadratic in `w` and in the VEV — `∝ ρ²|v|²` for one instanton. Under `Im(root) = √2ρ` that is `∝ |v|²·Im(root)²/2`.

> **Brief §6.4's universal `y_0²/2` law is the instanton effective action in a Higgs background**, with `|v|²` the configuration-dependent constant whose five-order-of-magnitude spread §6.4 measured.

That is a satisfying identification and it is also the closure. `Σρ_i² = 0` is the vanishing of a sum of squared norms — an equality case of a structural positivity, with the positivity being `|w|² ≥ 0`. Screen 0″ fires exactly: the class supplies positivity, and the positivity **is** the conclusion. `Λ ≥ 0` becomes automatic and `Λ = 0` becomes the entire content, with the geometry contributing nothing to it.

---

## 1. Screening verdict

| screen | verdict on the product/determinant reading |
|---|---|
| **0** equational or regional? *[universal]* | regional — `Σρ² = 0` is an equality case of an inequality, not a holomorphic vanishing. **Passes.** |
| **0″** positivity audit *[heuristic]* | **Fails, decisively.** The positivity is `w̄w ⪰ 0`, and it alone gives the conclusion (§0(3)). This is the ADHM dichotomy in its purest instance: the positivity is literally `Im(root)² ≥ 0`. |
| **2** deformation-invariant? *[universal]* | passes — `Σ Im²` is a non-analytic chamber object, not a class or an index (§0(5)). |
| **3** uniform separation? *[universal]* | passes — the margin *is* `y_0²/2` (§0(6)), which §6.4 says is automatic. |
| **9** circularity *[universal]* | **Fails.** `Σρ_i² = 0 ⟺ w = 0 ⟺` hyperbolic is a relabelling. |

So the product reading is not a new route. What it is, is an **explanation**: it identifies every recurring quantity in three years of this project with one physical parameter, and it says why the trade-off recurred. `λ = 0`, `S = 0`, `Λ = y_0²/2`, "outside the moduli space", "positivity is the trap" and "the difficulty is at `T → ∞`" are six descriptions of the instanton scale size.

---

## 2. What this opens, and one correction to memo 23

**Opened, in a limited way.** §0(2) reformulates RH as a statement about the accumulation of instanton sizes on the Uhlenbeck boundary, with an explicit rate `ρ_T ~ π√2/\log T`. That is the first version of the target in this project that is *not* a finite-dimensional matching problem, so brief §10's method-level criticism does not immediately apply to it. What would be needed is something that **constrains** the sizes — and §0(6) says the only known mechanism (a VEV) supplies a constraint that is circular.

**Correction to memo 23 §0(2).** That memo concluded dimension buys nothing, on the grounds that spheres carry no cohomology in the relevant degrees. For the *locus/topology* reading that stands. For the *size* reading it does not: the size is a free modulus **because** the action is conformally invariant in dimension 4, and in any other dimension, or with any scale-breaking term, it is determined rather than free. That is the first substantive reason in this project to leave dimension 4. It is not a recommendation — a determined size is a *fixed number*, not a detector, and one still has to make it carry `Ξ`'s data — but the earlier verdict was too broad and should not be quoted as covering this.

**And one thing that is now cheap.** §0(3) reduces the whole matching theorem to `det(D + W) ≥ det D`. Whether that inequality survives on the *non-commuting* locus — where the product object has no real roots — is the natural sharpening: it would say that a non-hyperbolic target requires non-commuting positions, giving a dictionary between conjugate pairs and commutator norms. `lab_product_object.py` Part 3 has the machinery.

---

## 3. Honesty notes

**Verified from primary sources:** DHKM (2.52) and its derivation; the canonical form (2.57) with (2.61) and (2.62); Osborn's identity as they state it after (2.52) (their Appendix C proof was not read); the constrained-instanton discussion of §IV.4 and the effective action (5.36).
**Proved here:** §0(1a) (three lines of radial calculus plus the standard `ℝ⁴` Green's function); §0(1c) exactly; §0(3)'s inequality (`det(D+W) ≥ det D` for `W ⪰ 0`, `D ≻ 0`, equality iff `W = 0`) and its consequence, which is a genuine generalisation of brief Theorem 4 to all charges and all classical groups; §0(4)'s degree count; §0(5)'s `2·ReLU(a)` identity and the non-symmetry of `Σ|ρ|²`.
**Measured:** §0(1d) (`3.2e−15` at `k ≤ 5`), the concentration table, §0(3)'s search, §0(4)'s degrees, §0(5)'s test set, §0(6)'s `Λ = ρ²` to 8 digits.
**Dictionary-level, not a theorem:** `Im(root) = √2ρ` is exact inside the charge-1 / commuting-diagonal family where brief §2.5's `B_j` applies. Beyond that family it is a correspondence read off matching shapes, and the `ρ_T ~ π√2/\log T` rate inherits that status — it is a translation of the Lehmer-pair bound, not a derivation. §0(6)'s identification of `y_0²/2` with the instanton effective action is likewise a shape match with the right parametric dependence, not a computed equality.
**Novelty:** Osborn's identity, the biharmonic Green's function of `ℝ⁴`, the 't Hooft `φ` as a determinant factor, and `det(D+W) ≥ det D` are all standard. The identification of the project's `y_0²/2` law with the instanton scale is the only thing here that is ours, and it is a dictionary, not a result.
**What was not done:** the `(d,n)` Bezoutian margin map offered at the end of memo 24. §0(2) makes it more interesting than it was — it would measure the `1/\log T` size law directly — but it is still instrumental.
