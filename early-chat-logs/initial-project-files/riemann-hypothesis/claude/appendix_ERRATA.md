# Errata for `appendix_extension_uniqueness.tex`

*2026-08-23. Recorded because `PROGRAM_CLOSED.md` lists the appendix as one of four
possible standalone artifacts. **It must not be circulated with Remark A.7 as printed.***

---

## 1. Remark A.7 ("why symmetry is unavoidable") is FALSE as stated

The remark asserts:

> "Uniqueness of an extension from a slice can therefore only come from symmetry
> (§linclass) or from holomorphic geometry upstairs (§twistor) — never from
> ellipticity alone."

The supporting argument is that a slice has codimension two in `ℍ`, that
codimension-two sets are polar (removable, harmonic capacity zero) in `ℝ⁴`, and
that a first-order elliptic system in four variables is determined by data on a
codimension-*one* hypersurface. All of that is correct **for the Cauchy–Fueter
system**, and the conclusion does not follow.

**The gap.** The argument silently fixes the complex structure for which the slice
is a *complex line*, which is the right reading for slice regularity but not the
only one. `ℍ` carries a 2-sphere of compatible complex structures. Put
`J_η(q) := q·η` for a unit imaginary `η`. If `I₀ ⟂ η` then

> `ℂ_{I₀} = span{1, I₀}` is **maximally totally real** in `(ℍ, J_η)`.

The same real 2-plane is a complex line for `J_{I₀}` and totally real for `J_η`.
Verified: `⟨J(span), span⟩ = 0` exactly in the orthogonal case, and
`J(span) = span` exactly in the parallel case (`lab_totally_real.py`, Part 1).

Consequently restriction from `J_η`-holomorphic maps to `ℂ_{I₀}` is a **bijection**
on germs — uniqueness by the identity theorem for a maximally totally real
submanifold, existence by complexification of real-analytic data, with entire data
giving entire extensions. The polarity objection does not bite because `∂̄F = 0`
for a map `ℂ² → ℂ²` is **overdetermined**, not determined. So uniqueness here comes
from neither symmetry nor twistor geometry upstairs, but from ellipticity alone —
exactly what the remark says cannot happen.

**Concretely** (`η = i`, `I₀ = j`): write `q = z₁ + z₂ j` with `z₁,z₂ ∈ ℂ_i`; then
`q·i = (i z₁) + (−i z₂) j`, so `J_i` acts as `+i` on `z₁` and `−i` on `z₂`, and the
holomorphic coordinates are `(z₁, w)` with `w = conj(z₂)`. The slice `ℂ_j = {x + yj}`
is `{z₁, w both real} = ℝ²`.

For intrinsic data with stem `G`, in the coordinates `ζ_± = z₁ ± i w` the unique
extension is `A = ½(G(ζ₊)+G(ζ₋))`, `B = (1/2i)(G(ζ₊)−G(ζ₋))`, so

> `Z(F) = Z(G) × Z(G)` — always **discrete**.

And `ℂ²` is Stein, so no zero set of a holomorphic map `ℂ² → ℂ²` has a compact
positive-dimensional component: **no 2-sphere of zeros can occur**, with no symmetry
assumed. Verified for `z²±1`, `(z²+1)(z−1)`, `z³−2z` (restriction reproduces the
stem; `#Z(F) = #Z(G)²` exactly).

## 2. Suggested repair

Remark A.7's *conclusion* about the appendix's own subject matter survives; only its
scope claim is wrong. Replace the final sentence with something like:

> "Within the fixed complex structure for which the slice is a complex line — the
> setting relevant to slice regularity — uniqueness cannot come from ellipticity
> alone, and must come from symmetry (§linclass) or from holomorphic geometry
> upstairs (§twistor). Choosing instead a complex structure for which the slice is
> maximally totally real makes the `∂̄`-system overdetermined and restores
> uniqueness, at the cost of breaking the rotation group to the circle fixing that
> structure; that class is not slice-compatible and is not pursued here."

The parenthetical cost is real and is the reason the alternative class is of no use
to the surrounding programme: its symmetry group is only the circle fixing `η`,
whose fixed locus in `ℍ` is the slice `ℂ_η`, while `Z(F) = Z(G)²` has off-diagonal
points outside that locus — so even invariance of the zero *set* is unsatisfiable in
degree `≥ 2`. See `BRIEF_transverse_rigidity.md` §5 for the full statement, and
`lab_totally_real.py` for the verification.

## 3. Other items

- **Remark A.7's second sentence is fine.** The infinite-dimensional non-uniqueness
  of Proposition A.5 (the kernels `K_n(q) = (x₂ − i x₃)ⁿ`) is correct and needs no
  symmetry; only the "never from ellipticity alone" clause is wrong.
- **Not an erratum, but flagged:** Theorem A.1 (multiplicative rigidity) has **not**
  been novelty-checked and is plausibly standard in the slice-regular literature —
  it is Frobenius plus a character argument. Same for the rest of the appendix. See
  `PROGRAM_CLOSED.md`, "Updated prior on the other three artifacts".
- The unrelated sign error in `zero_sphere_condensed.tex` §8 and
  `second_involution_intro.tex` (`ι_R : γ ↦ γ̄` should be `γ ↦ −γ̄`) is recorded in
  `PROGRAM_CLOSED.md` and is not repeated here.

---

*Verification: `lab_totally_real.py`, output in `lab_totally_real_RESULTS.txt`. The
totally-real/complex-line dichotomy, the holomorphic coordinates, the extension
formula, `Z(F) = Z(G)²`, the τ-invariant, and the unsatisfiability of the symmetry
hypothesis are each checked symbolically or numerically.*
