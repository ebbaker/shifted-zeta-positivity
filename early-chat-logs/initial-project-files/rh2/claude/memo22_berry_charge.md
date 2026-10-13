# The ℤ₂ Berry Charge of the Degeneracy Locus

*Working memo #22 — August 24, 2026. Follows memo 21 §2's proposed mechanism. The charge is real and measurable, it distinguishes two kinds of degeneracy — and it does **not** obstruct a 2-sphere. The memo says why, and why that closes the topological route on `S⁴` in general. Certified by `lab_berry_charge.py`.*

---

## 0. Results

**(1) The invariant exists and is nontrivial.** Where the three singular values of `M = F⁻` are simple, the SVD `M = Σ_i σ_i u_i v_iᵀ` fixes each *pair* `(u_i, v_i)` only up to a simultaneous sign flip. So the `i`-th singular pair is a point of `(S² × S²)/ℤ₂`, whose fundamental group is `ℤ₂`, and transport around a loop carries a **ℤ₂ monodromy**.

Measured on the generic locus (charge-4 't Hooft, centres spanning a 3-plane, no continuous symmetry), at three locus points, three radii each (`0.05, 0.025, 0.012`), 720–2880 steps:

> **Berry sign `= −1` on exactly the two degenerate pairs, `+1` on the third.** Identical for the `u` and `v` frames. No ordering swaps. Control loops — one displaced so as not to link, one tangent to the locus — both give `+1`.

That is the classical Herzberg–Longuet-Higgins conical-intersection signature, and it confirms the locus is **essential**: it cannot be removed by a small perturbation.

**(2) The charge separates two kinds of degeneracy.** On the symmetry-forced locus of memo 21 §0(4) — the charge-3 coplanar case, where the locus is the 2-plane containing the centres — the Berry sign is `+1` at every radius. The loop there is an `SO(2)` orbit and the singular values are *constant* along it. So:

> **conical degeneracy → charge `−1` (essential); symmetry-forced degeneracy → charge `+1` (removable).**

That is a genuine structural invariant and it was not available before. It also retroactively explains memo 21 §0(4): the symmetric configurations produce loci that are large but *uncharged*.

**(3) But it does not obstruct a 2-sphere, and the reason is decisive.** Suppose `Σ₀ ≅ S²` were a closed component of the locus in `S⁴`. By Alexander duality `H₁(S⁴ ∖ Σ₀; ℤ₂) ≅ H̃¹(Σ₀; ℤ₂) ⊕ …` — concretely `H₁(S⁴∖S²) = ℤ`, so mod 2 the linking circle is **nontrivial**. A `ℤ₂` class can therefore take the value `−1` on it with no contradiction. Equivalently: the `w₁` of the eigenline bundles is dual to a "branch cut" 3-chain bounded by `Σ₀`, and since `H₃(S⁴, Σ₀; ℤ₂)` accommodates it, the cut always exists.

**So memo 21 §2's proposed mechanism fails.** Stated plainly so it is not re-attempted.

**(4) And the failure generalises — the whole topological route is empty on `S⁴`.** Every candidate obstruction of this type lives in the cohomology of the base:

- `[Σ] ∈ H₂(S⁴; ℤ₂) = 0` — the locus is always a `ℤ₂`-boundary, so no class obstructs it;
- `w₂` constraints live in `H²(S⁴; ℤ₂) = 0`, and for `Σ₀ = S²`, `H²(S⁴∖Σ₀; ℤ₂) = 0` too;
- the only relation among the three charges is `w₁(ℓ₁) + w₁(ℓ₂) + w₁(ℓ₃) = w₁(Λ²₋) = 0`, which the measured pattern `[−1, −1, +1]` already satisfies.

> **`S⁴` is cohomologically too simple for a characteristic-class obstruction to exist.** Any theorem forbidding a closed component must therefore be **analytic** — a Weitzenböck/Bochner argument, or a structural fact about the ADHM data — not topological. That redirects the effort, and it is the most useful thing in this memo.

**(5) A new structural fact, found on the way.** For a finite-energy instanton the field is asymptotically BPST-like, hence *conformal* (`σ₁ = σ₂ = σ₃`, memo 21 §0(2) with `k = 1`). Measured along rays: `min-gap/σ₁ = 0.100, 0.028, 0.0055, 0.0011, 0.0002, 0.0000` at `|x| = 3, 6, 12, 25, 60, 150`.

> **The degeneracy locus accumulates at the point at infinity.** On `S⁴` the locus is compact (a closed subset of a compact manifold) and passes through that point — which is moreover a point where *all three* singular values coincide, the codimension-5 stratum. The locus is therefore tethered to a conformal point rather than being a free-floating surface.

---

## 1. Where this leaves §6.1″

> **§6.1″.** For an irreducible finite-energy `SU(2)` Yang–Mills connection of charge `k ≥ 3`, can the repeated-singular-value locus of `F⁻` have a closed 2-dimensional component?

Still open, but the search space has narrowed usefully:

- **topology will not settle it** — §0(4);
- the locus is **compact** on `S⁴` and **passes through at least one conformal point** — §0(5);
- it is **essential** (`ℤ₂`-charged) wherever the degeneracy is conical — §0(1);
- and the configurations with enough symmetry to *force* a spherical locus instead make it uncharged and large — memo 21 §0(4), now explained by §0(2).

The honest reading: the pattern across memos 20–22 is the brief's §3 trade-off yet again, in a new costume. Every structure rich enough to *have* a sphere-dimensional canonical locus is either symmetric (locus uncharged and too big) or generic (locus charged, but the base too simple to obstruct anything).

---

## 2. What would actually move it

1. **The analytic route.** `F⁻` is a covariantly closed ASD 2-form (memo 20 §0(1)), so it satisfies a Weitzenböck identity on a flat base: `∇*∇F⁻ + {F⁺, F⁻} = 0`. The degeneracy locus is where the *Gram matrix* `⟨F⁻_a, F⁻_b⟩` has a repeated eigenvalue. Deriving an equation for that Gram matrix from the Weitzenböck identity, and asking whether a compact component of its degeneracy set is compatible with the maximum principle, is the natural next computation. Unlike everything in this memo it is not topological, and §0(4) says that is now required.
2. **Verify Atiyah's curvature formula.** Memo 21's structure theorem rests on it and it is still unchecked (§3).

---

## 3. Honesty notes

**Measured here:** everything in §0(1), (2), (5). The Berry transport is a direct continuity-matched transport of the actual SVD frames with two independent controls, stable across a factor of 4 in radius and 4 in step count.
**Argued, not computed:** §0(3) and §0(4), which are standard algebraic topology (Alexander duality on `S⁴`) applied to the measured invariant. They should be checked by someone who does this for a living before being relied on.
**Not verified:** Atiyah's ADHM curvature formula, which memo 21 §0(2) depends on. The upload provided was Atiyah's five-page 1977 conference talk *Geometry of Yang–Mills fields* (Springer Lecture Notes in Physics), **not** the 1979 *Lezioni Fermiane* monograph of the same title, and does not contain the ADHM normal form or the curvature formula. Memo 21's structure theorem therefore remains corroborated only by its consequences, which were verified independently on explicit instantons.
**Negative result to keep:** the `ℤ₂` mechanism proposed in memo 21 §2 does not work. §0(3)–(4) record why, so it is not re-attempted.
