# The Locus Landscape: What a Yang–Mills Curvature Zero Set Actually Is

*Working memo #20 — August 24, 2026. First pass at brief §6.1, the gate. Answers it — negatively, for the locus it named — and in the process identifies what these loci are, which turns out to be an object the project already has expertise in. Certified by `lab_locus_landscape.py`.*

---

## 0. Results

**(1) A structural fact the brief does not state, and it changes the object.** For a source-free Yang–Mills field, Bianchi gives `d_A F = 0` and the field equation gives `d_A *F = 0`. Since `*F = F⁺ − F⁻`,

> `d_A F⁺ = 0` **and** `d_A F⁻ = 0` **separately.**

So `F⁻` is a covariantly *closed* anti-self-dual 2-form; it is automatically co-closed (`d_A^*F⁻ = −*d_A*F⁻ = *d_AF⁻ = 0`). Hence `(d_A + d_A^*)F⁻ = 0`, and `d_A + d_A^*: Ω^{even}(𝔤) → Ω^{odd}(𝔤)` is elliptic with **isomorphism** symbol. `F⁻` is a solution of a first-order Dirac-type system, not merely a tensor field.

**(2) Two consequences, both citable, both new to the project.**

- **Strong unique continuation** holds (Aronszajn). This answers **§6.2(1) affirmatively**: `F⁻ = 0` on an open set forces `F⁻ ≡ 0`.
- By **Bär's theorem** (*Zero sets of solutions to semilinear elliptic systems of first order*, Invent. Math. **138** (1999) 183–202): for a nontrivial solution, the finite-order zero set is **countably `(n−2)`-rectifiable with locally finite `H^{n−2}`**. On `ℝ⁴`:

> **`dim_H {F⁻ = 0} ≤ 2`, countably 2-rectifiable, locally finite `H²` — unless `F⁻ ≡ 0`.**

This is a *genuine* dimension theorem, unlike brief §4.6's ladder, which counted only **generic** codimensions and therefore concluded "empty" for a reason that does not bind any particular field. §4.6 should be read as excluding matching-by-dimension for a generic field, and as saying nothing about a specific one.

**(3) What the locus is — and it lands in home territory.** For an ASD 2-form `ω = f₁η₁ + f₂η₂ + f₃η₃` on `ℝ⁴`, verified symbolically:

> `dω = 0` ⟺ `∂f/∂x₀ = −curl f` and `div f = 0` ⟺ **`B = f₁i + f₂j + f₃k` is a purely imaginary Fueter-regular function.**

Equivalently on `ℂ²`: `ω = i∂\bar∂u` with `u` **harmonic**, and `{ω = 0}` is the vanishing locus of the complex Hessian of a harmonic function. So the §6.1 question is a question about **zero sets of Fueter-regular functions** — quaternionic analysis, which is where this project's expertise actually is.

**(4) §6.1 is answered — negatively — for `{F⁻ = 0}`.** There is an explicit polynomial source-free Yang–Mills field on `ℝ⁴`, neither self-dual nor anti-self-dual, whose `{F⁻ = 0}` contains a 2-sphere as its unique 2-dimensional component. Everything below verified in exact arithmetic:

```
f1 = -(5/2) x0^2 x2 - x0 x1 x3 + (1/2) x2 (|x|^2 - 1)
f2 =  (5/2) x0^2 x1 - x0 x2 x3 - (1/2) x1 (|x|^2 - 1)
f3 =  x0 (-5 x0^2 + 6 x1^2 + 6 x2^2 + 3 x3^2 - 3)/3
```
`ω = Σ f_a η_a`; `F = ω + ω⁺` with `ω⁺ = e₀₁ + e₂₃` constant self-dual; `A = a_μ dx^μ ⊗ σ₃` with `da = F` (potential computed explicitly). Then `dF = 0`, `d*F = 0`, `F⁻ = ω ≢ 0`, `F⁺ = ω⁺ ≠ 0`, and

> `{F⁻ = 0} = S² ∪ {x₀=x₁=x₂=0} ∪ {x₁=x₂=0, x₃² − (5/3)x₀² = 1}`,

with `S² = {x₀ = 0, |x⃗| = 1}` the only 2-dimensional piece. Consistent with (2): the zero set is exactly 2-dimensional, the maximum Bär allows.

**(5) The equivariant sector is sphere-free, for the trivial reason — now concretely.** An `SO(3)`-equivariant field `ℝ³ → ℝ³` must be radial, `B = φ(x₀,r)\hat x`. Radial fields are curl-free, so `∂₀φ = 0`; `div B = 0` gives `∂_r(r²φ) = 0`; hence `φ = c/r²` and **`B` has no zeros at all**. This is the predecessor's Vekua trace-term obstruction in concrete form, and it confirms the diagnosis: the equivariant class was sphere-free only because it was empty of interesting members. **Dropping equivariance is what makes spheres appear.**

---

## 1. Why the counterexample does not close §6.1

Two caveats, and they are the useful output of this memo:

- **It is reducible.** The holonomy lies in `u(1) ⊂ su(2)`. Every rigidity theorem in the subject (brief §4.4) concerns irreducible connections; reducible ones are the degenerate stratum where nothing is expected to hold.
- **It has infinite energy.** `|F|²` is a polynomial of degree 6, so `∫_{ℝ⁴}|F|² = ∞`. The gap theorems, Uhlenbeck removability, and the whole finite-energy apparatus are inapplicable — and by conformal invariance, finite energy on `ℝ⁴` would put us on `S⁴`, where the theorems bite.

So the honest reading is not "the gate is closed" but "the gate as worded was too weak." **The sharpened question:**

> **§6.1′.** Let `A` be an **irreducible, finite-energy** source-free Yang–Mills connection on `ℝ⁴` (equivalently, by Uhlenbeck, on `S⁴`). Can `{F⁻ = 0}` contain a closed 2-dimensional component?

This is well-posed, is not answered by anything found so far, and both hypotheses are doing visible work. Note also that for `SU(2)` the generic count in §4.6 says `{F⁻=0}` is empty, and Bär says any non-generic occurrence is at most 2-dimensional — so the target is a thin, structured set of exceptional fields, which is the right shape for a rigidity theorem.

---

## 2. The landscape, as it now stands

| locus | what is now known |
|---|---|
| `{F⁻ = 0}` | Dirac-type; SUCP holds; `dim_H ≤ 2`, countably 2-rectifiable. **Can be a 2-sphere** (§0(4)) for a reducible infinite-energy field. Open for irreducible finite-energy — **§6.1′** |
| `{F⁺ = 0}` | identical by orientation reversal |
| `{F = 0}` | `F⁺` and `F⁻` both vanish; SUCP applies to each, so empty interior; generic codimension 18 |
| rank loci of `F⁻` | for `SU(2)`, `F⁻` is a field of `3×3` real matrices (both `Λ²₋` and `𝔤` are 3-dimensional); brief §4.6's ladder gives generic dimensions, and Bär does **not** apply to them directly since a rank condition is not a zero set of a Dirac solution. **Unstudied.** The `3×3` matrix structure (determinant, eigenvalue-collision discriminant, symmetric/skew split) is richer than "rank" and has never been looked at here |
| jumping locus | empty over the domain by Pool Thm IV.5 — unchanged |
| the current `*J` | zero for any YM solution — unchanged |

**The one genuinely unexplored item** is the last-but-one row. For `SU(2)`, `F⁻` is a `3×3` real matrix field, and the canonical loci of a matrix field are not just rank loci: there is `det F⁻ = 0` (a hypersurface), the discriminant locus where eigenvalues collide (codimension 2 for real symmetric, codimension 3 for general real — i.e. **potentially 2-dimensional**), and the locus where `sym(F⁻)` degenerates. The eigenvalue-collision locus of a real symmetric `3×3` field has codimension 2 in general — exactly sphere dimension — and it is the locus that the whole classical theory of *conical intersections* is about. None of this has been screened.

---

## 3. What this changes about the goal

The user's reframing — the target is *criteria for ruling out off-axis zeros*, and spheres/equivariance are not necessarily the right category — is supported by §0(5). Equivariance was not a neutral packaging choice: it is exactly what made the class trivial. The sphere then had to be imposed by hand, and Proposition 1 of the transverse-rigidity brief made that circular.

What §0(3) offers instead is a **non-equivariant** home for the same question. The objects are Fueter-regular functions, the loci are their zero sets, and the constraint that is actually available (`dim ≤ 2`, rectifiable) is a theorem rather than a relabelling. Whether anything stronger is available for irreducible finite-energy fields is §6.1′.

---

## 4. Honesty notes

**Proved / verified exactly here:** §0(1) (two lines of algebra); §0(3) (symbolic, both the `curl` form and the Fueter form); §0(4) (Fueter equations, `dF = 0`, `d*F = 0`, `F⁻`, `F⁺`, the potential, and the zero set, all in exact rational arithmetic); §0(5).
**Inherited, not verified here:** Bär's theorem and Aronszajn unique continuation. Bär's statement was read from the arXiv version directly; the application to `(d_A + d_A^*)` uses only that its symbol is an isomorphism, which is standard.
**Not established:** anything about irreducible finite-energy fields. §6.1′ is open, and nothing in this memo bears on it beyond making it the right question.
**Novelty:** §0(1) is certainly known to gauge theorists (it is two lines) though the brief did not have it. The Fueter identification in §0(3) is classical in the guise "closed ASD 2-forms = purely imaginary monogenic functions"; it should be assumed known. §0(4)'s explicit example is the kind of thing that could be in the literature; not searched.
