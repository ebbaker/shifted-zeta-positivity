# Why `S⁴`, Whether Dimension Helps, and the Bridge We Dropped

*Working memo #23 — August 24, 2026. A decision memo, not a result memo. Answers a direct question — why is the base `S⁴`? — and in answering it finds that the §6.1 programme has been detached from RH since memo 20. No new computation.*

---

## 0. Summary

**(1) `S⁴` entered through my own patch, not through the problem.** The chain is short and worth seeing:

- memo 20 §0(4) produced an explicit source-free YM field on `ℝ⁴` with a 2-sphere in `{F⁻ = 0}`, answering §6.1 negatively;
- that counterexample was **reducible** and **infinite-energy**, so I added those two hypotheses and called the result §6.1′;
- "finite energy" plus conformal invariance in dimension 4 plus Uhlenbeck removability *is* the statement that `ℝ⁴` compactifies to `S⁴`.

So the base became `S⁴` because I ruled out my own counterexample in the cheapest available way. Then memo 22 §0(4) discovered the cost: `S⁴` carries no cohomology in the relevant degrees, so no characteristic-class obstruction can exist. **I built the bottleneck two memos before hitting it.** Nothing in RH, and nothing in the quaternionic mechanism, required `S⁴`.

**(2) The bottleneck is the sphere, not the dimension.** `Sⁿ` has cohomology only in degrees `0` and `n`. A locus of codimension `c` is dual to a class in `H^c`, which vanishes for `0 < c < n`. So:

> **On any sphere, of any dimension, no characteristic class can obstruct a positive-dimensional locus.**

Going to `S⁷` or `S⁸` changes nothing. The fix is a base **with** cohomology, and that is available in dimension 4 already and far more cheaply: `ℂℙ²`, `K3`, `T⁴`, or the ALE spaces — for which this project already holds Kronheimer and Nakajima. Donaldson theory lives there. **Dimension is the expensive way to buy what a different 4-manifold gives for free.**

**(3) Higher dimensions do offer something genuinely different, and it is the natural continuation of this project's own logic.** `ℍ → 𝕆`: the 2-sphere of imaginary quaternionic units becomes the 6-sphere of imaginary octonionic units, and the octonionic analogue of ASD is the `Spin(7)` (dim 8) or `G₂` (dim 7) instanton condition. On a `Spin(7)` 8-manifold `Λ² = Λ²₂₁ ⊕ Λ²₇` and the instanton condition is `F ∈ Λ²₂₁`; the degeneracy loci have different codimensions and there is more room. This is real, active mathematics (Donaldson–Thomas instantons; Tian; Walpuski). It is a legitimate direction. **But it inherits every screen in the brief's §8 unchanged**, and it is a large investment in new machinery.

**(4) And here is the thing that matters more than the base.** Memo 20 §0(5) showed that `SO(3)`-equivariance makes the class trivial — equivariant solutions are `B = c\hat x/r²`, zero-free — so we dropped equivariance. But **equivariance was the only bridge from "the locus contains a 2-sphere" to "`Ξ` has a non-real zero."** That is brief §1.1's entire mechanism: `F(uq\bar u) = uF(q)\bar u` turns one off-axis zero into a sphere. Drop it and a sphere in a curvature locus says nothing about `Ξ`.

> **Since memo 20, §6.1 has been a pure gauge-theory question with no connection to RH.** Memos 20–22 contain real results — the `d_AF⁻ = 0` structure theorem, the `dim ≤ 2` bound, the Fueter identification, the singular-value invariant theory, the Berry charge — and none of them is about the Riemann hypothesis. I should have flagged this when the hypothesis was dropped rather than three memos later.

This is brief §1.2 again, in the one form the brief did not anticipate: it warned that *with* equivariance the isolation property is a relabelling of hyperbolicity. The complementary fact is that *without* equivariance it is not a statement about hyperbolicity at all.

---

## 1. The screening audit I should have run

Brief §8, applied to memo 22's proposed mechanism.

| screen | verdict on the `ℤ₂` Berry charge |
|---|---|
| **0** equational or regional? *[universal]* | regional — a topological non-existence claim, not a vanishing condition. **Passes.** |
| **2** deformation-invariant? *[universal]* | The charge **is** a deformation invariant (a homotopy invariant of the frame map on the complement). Screen 2 kills its use as a *discriminant*. It does not literally kill its use in an *isolation theorem*, which is what memo 22 attempted — so the screen was not violated, but it was close enough that I should have written the distinction down before computing. |
| **1″** is the invariant `ρ`-local? *[universal]* | Not applicable — no `ρ`, because no equivariance. Which is §0(4): the screen is inapplicable precisely because the bridge is gone. |
| **7** rigidity/existence *[heuristic]* | **Fails, and this is the substantive one.** Memos 20–22 are three more instances of brief §3: symmetric enough to force a sphere-dimensional locus ⟹ locus uncharged and too big (memo 21 §0(4), memo 22 §0(2)); generic enough to be charged ⟹ base too simple to obstruct (memo 22 §0(4)). |

**And the closest prior art was already closed.** Brief §2.4's `σ`-type of divisor components is the one topological invariant this programme found that is *not* deformation-invariant — real zeros give `σ`-invariant components, conjugate pairs `σ`-swapped pairs, so `RH ⟺ every component of the zero locus in `Y = Q/σ` is nonorientable`. That is the correct shape. It was closed by §2.7(c): `ρ` acts antipodally on the `w`-sphere, no Ruling-B line is `ρ`-invariant, so no finite-order jet along a slice can see it — and §7.2 records the direction as closed.

> **The topological family is the most thoroughly closed family in this project, not the least.** Screen 0 kills the holomorphic/equational branch in one line; screen 2 kills the deformation-invariant branch; §2.7(c) kills the one survivor. A preference for topology over analysis is, on this project's own evidence, a preference for the direction carrying *more* accumulated negative results.

---

## 2. The options, stated plainly

**(a) Stop.** `PROGRAM_CLOSED.md` stands, and brief §10's method-level criticism — every object built here is finite, and `Λ = 0` puts the difficulty entirely in the `T → ∞` tail — applies to memos 18–22 exactly as it applied to everything before them.

**(b) Rebuild the bridge.** Find something connecting a gauge-theoretic locus to reality of zeros *without* equivariance. This is brief §7.4(3): a property `P` of `Ξ` that is analytically natural and independently provable. There is no candidate, and this is the wall.

**(c) Continue as gauge theory, correctly labelled.** §6.1′ is a decent open question in its own right and the last three memos made real progress on it. On a base with cohomology (`ℂℙ²`, `K3`, ALE) the characteristic-class route reopens; in dimension 7 or 8 the octonionic analogue is the natural continuation of the quaternionic logic. Either is legitimate mathematics. Neither is RH unless (b) is solved.

**(d) The Weitzenböck computation** (memo 22 §2). Small, self-contained, and — per §1 above — in the branch with fewer prior closures rather than more. But it inherits §0(4): whatever it proves is a fact about YM fields, not about `Ξ`.

My reading: **(b) is the only one of these that is about RH**, and it has no candidate. Everything else is a choice about what to work on instead.

---

## 3. Honesty notes

**No computation in this memo.** Everything is either a re-reading of the predecessor brief (§§1.1, 1.2, 2.4, 2.7c, 3, 6.3, 7.2, 7.4, 8, 10) or an accounting of memos 20–22.
**Corrections to my own work:** memo 20 §1 introduced the finite-energy hypothesis without noting that it forces the base to `S⁴`; memo 22 §0(4) then reported that as a discovery. Memos 20–22 should carry a note that they are gauge theory, not RH, from the point equivariance was dropped.
**What stands from memos 20–22 regardless:** `d_AF⁺ = d_AF⁻ = 0` separately; `dim_H{F⁻=0} ≤ 2` via Bär; the Fueter identification of closed ASD 2-forms; the `M ↦ QMR^T` invariant theory and the singular-value ladder; the measured `ℤ₂` charge and its separation of conical from symmetry-forced degeneracy. All are correct and none is about `Ξ`.
