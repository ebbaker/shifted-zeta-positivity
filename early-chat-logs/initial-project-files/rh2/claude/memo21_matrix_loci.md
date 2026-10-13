# The 3×3 Curvature Matrix: Invariant Theory and a Structure Theorem

*Working memo #21 — August 24, 2026. Screens the matrix loci of `F⁻` for `SU(2)`, as memo 20 §2 proposed. Corrects brief §4.6, proves a structure theorem for the ADHM curvature, and produces the first canonical 2-dimensional locus of an irreducible finite-energy Yang–Mills field. Certified by `lab_matrix_loci.py`.*

---

## 0. Results

**(1) The invariant theory, which the brief had wrong.** For `SU(2)`, both `Λ²₋` and `𝔤` are 3-dimensional, so `F⁻` is a field of `3×3` real matrices `M_{ai} = ⟨F⁻, η_a ⊗ T_i⟩`. There is **no canonical isomorphism** between the two `ℝ³`s, so trace, symmetry and eigenvalues of `M` are meaningless. The actual group is

> gauge: `M ↦ M Rᵀ` (`R ∈ Ad SU(2) = SO(3)`);  frame: `M ↦ Q M` (`Q ∈ SO(3)` acting on `Λ²₋`),

with `Q, R` **independent**. So the complete pointwise invariants are the **singular values** `σ₁ ≥ σ₂ ≥ σ₃ ≥ 0` together with `sign(det M)`. The corrected ladder:

| locus | invariant | codim | dim in `ℝ⁴` |
|---|---|---|---|
| `det F⁻ = 0` | `σ₃ = 0` | 1 | 3 |
| **repeated singular value** | `σ_i = σ_j` | **2** | **2 — sphere dimension** |
| `rank ≤ 1` | `σ₂ = σ₃ = 0` | 4 | empty |
| all singular values equal | `σ₁=σ₂=σ₃` | 5 | empty |
| `F⁻ = 0` | all `σ = 0` | 9 | empty |

> **Brief §4.6 is wrong where it says "for `SU(2)` no curvature rank locus is ever 2-dimensional … so no such locus can be a union of 2-spheres, before any analysis."** It tabulated only *rank* loci. The repeated-singular-value locus is canonical, gauge- and frame-invariant, and has codimension 2. **`SU(2)` has a sphere-dimensional canonical locus after all**, and §6.2(2)'s "`U(2)` is the single exception" no longer holds.

**(2) A structure theorem for the ADHM curvature.** Atiyah's ADHM curvature formula has the shape `F_{μν} = Σ_{j,l} f_{jl} c_j σ̄_{μν} \bar c_l` with `f` the real symmetric `k×k` matrix `(Δ†Δ)^{-1}` and `c_j` quaternions. Reading this as a map `T: Im ℍ → Im ℍ` and diagonalising `f = Σ_m μ_m u_m u_mᵀ`, with `d_m = Σ_j (u_m)_j c_j`:

> **`T = Σ_{m=1}^{k} ν_m R_m`** — a real linear combination of **at most `k` scaled rotations** of `Im ℍ`.

**Corollary (proved).**
- `k = 1`: `T = νR` is **conformal**, so `σ₁ = σ₂ = σ₃` everywhere.
- `k = 2`: `T Tᵀ = (ν₁²+ν₂²)I + ν₁ν₂(S + Sᵀ)` with `S = R₁ᵀR₂ ∈ SO(3)`, and `S + Sᵀ` has eigenvalues `2, 2\cos θ, 2\cos θ`. **A repeated singular value is forced at every point.**
- `k ≥ 3`: no degeneracy generically.

Verified numerically on random combinations (`k=1,2`: max min-gap `≤ 1.2e−15` over 3000 draws; `k=3,4`: `≈ 0.47`) **and on the explicit instantons**: 't Hooft/JNR charge 1 and 2 give min-gap `≈ 2e−16` at random points, charge 3 and 4 give `6e−02` and `1.6e−01`. All exactly anti-self-dual (`‖F⁺‖ ≲ 1e−15`).

**(3) So charge ≤ 2 instantons lie identically inside the degeneracy stratum.** For them the locus is everything and carries no information. This is a sharp, concrete demonstration that **generic-codimension reasoning is unreliable here** — the actual solutions sit in strata of codimension 5 (`k=1`) and 2 (`k=2`) that a generic count would call empty or thin. Brief §4.6's caveat should be promoted to a warning.

**(4) Symmetry forces the degeneracy too — and it does so exactly where a sphere could have come from.** Verified:

- **Collinear centres** (residual `SO(3)` rotating the orthogonal `ℝ³`): degenerate **everywhere**, at every charge tested.
- **Coplanar centres** (residual `SO(2)`): degenerate **exactly on the 2-plane containing the centres** — off it the gap is `1e−03` to `4e−02`. A genuine 2-dimensional canonical locus, but a **plane**: non-compact, no sphere.
- **Charge 4, centres spanning a 3-plane** (no continuous residual symmetry): a genuine 2-dimensional locus spread through the region, with **no symmetry explanation**. Topology not determined here.

> **The trade-off, in its cleanest instance yet.** An `SO(3)`-invariant 2-dimensional subset of `ℝ⁴` *is* a union of 2-spheres. So the only symmetry that could deliver a sphere by pure equivariance is `SO(3)` — and `SO(3)` symmetry collapses the locus to everything. Weaker symmetry (`SO(2)`) gives a 2-dimensional locus, but its fixed-point set is a **plane**, not a sphere. **Every symmetric route to a sphere is self-defeating**, for the same structural reason the brief's §3 records: the constraint that forces the locus to be interesting is the constraint that destroys it.

---

## 1. Screening the locus

| screen | verdict for `{σ_i = σ_j}` |
|---|---|
| **canonical?** | yes — gauge- and frame-invariant, no choices |
| **right dimension?** | yes — codimension 2, the first such locus found for `SU(2)` |
| **§2.1** | passes: a "no closed component" statement is topological, not a holomorphic equation |
| **§2.3** (deformation invariants) | **bites, partially.** The locus is a degeneracy locus of a bundle map, so its homology class is a Thom polynomial in the characteristic classes and any *count* is a deformation invariant, dead on arrival. But **topology is not determined by the class**, so a "no closed 2-dimensional component" theorem is not excluded |
| **§1.2** (sphere-free theorem + verifiable membership) | undecided — this is the open question |
| **existence side** | the locus is nonempty and 2-dimensional for charge ≥ 3 with coplanar or generic centres |

**The live question, sharpened again:**

> **§6.1″.** For an irreducible finite-energy `SU(2)` Yang–Mills connection of charge `k ≥ 3`, can the repeated-singular-value locus of `F⁻` have a **closed** 2-dimensional component?

Everything found so far is non-compact (planes, or unbounded surfaces). Nothing rules a closed component out.

---

## 2. What would settle it

Two concrete routes, both within reach.

1. **The nematic picture.** Where a repeated singular value occurs, `M Mᵀ` degenerates from biaxial to uniaxial: `M Mᵀ = σ²I + (σ₁²−σ²)nnᵀ` with a **director** `n ∈ ℝP²`. Off the locus one has a genuine biaxial frame; on it the frame degenerates. This is exactly the structure of defects in nematic liquid crystals, where the defect set carries a `ℤ₂` (Berry-phase) charge from `π₁(ℝP²) = ℤ₂`. **If the `ℤ₂` charge of a closed component must vanish, and if a nonzero charge is forced by the ADHM data, a closed component is excluded.** That is a genuine mechanism, it is topological rather than a relabelling, and it does not go through equivariance.
2. **Trace out the charge-4 locus.** Numerically continue the surface from the points already found and determine its components and compactness. Mechanical, and it would either produce a closed component (closing §6.1″ negatively) or supply evidence for the theorem.

Route 1 is the one worth doing first: it is the first candidate mechanism in this project that is neither an equation (§2.1), nor a characteristic number (§2.3), nor a relabelling of hyperbolicity (§1.1).

---

## 3. Honesty notes

**Proved here:** §0(1)'s invariant theory (elementary); §0(2)'s corollary for `k = 1, 2` (two lines of linear algebra, given the ADHM curvature formula).
**Assumed, not re-derived:** Atiyah's ADHM curvature formula `F = Σ f_{jl} c_j σ̄ \bar c_l`. The structure theorem depends entirely on it and it should be checked against Atiyah's *Geometry of Yang–Mills Fields* before circulation. Its consequences were verified independently on explicit 't Hooft/JNR instantons, which is strong corroboration but not a substitute.
**Measured:** everything in §0(2)–(4). All instantons used were checked to be exactly anti-self-dual (`‖F⁺‖ ≲ 1e−15`).
**Not established:** anything about `k ≥ 3` topology, and anything about non-self-dual finite-energy fields (no explicit examples exist — brief §6.2(3)).
**Novelty:** the `k ≤ 2` degeneracy is the kind of fact that is probably known to the instanton community; it should be assumed known until checked. The invariant-theory correction to §4.6 is internal bookkeeping.
