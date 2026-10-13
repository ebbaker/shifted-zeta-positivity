# Pool's Ladder from the Source, Two Corrections, and the Closure of the Obstruction Route

*Working memo #11 — August 23, 2026. Follows memo 10. Reads Pool, Mem. AMS 358, directly; corrects two errors in memo 10; and closes the obstruction route (brief §7.1/§7.2) with a proof rather than a screen. Certified by `lab_holomorphic_nogo.py`.*

---

## Statement of the theorem

*Added after the fact: the original draft used the proposition of §0(3) before stating it, and left its scope implicit. Both are fixed here. §§0–7 below are unchanged apart from cross-references.*

**Setup.** Fix a degree `d`. A monic polynomial

`p(z) = z^d + a_{d-1} z^{d-1} + … + a_1 z + a_0`

is determined by its coefficient vector `a = (a_0, …, a_{d-1})`. Allow the coefficients to be complex, so the parameter space is `ℂ^d`, containing the real coefficient vectors as the subspace `ℝ^d ⊂ ℂ^d`. Call `p` **hyperbolic** if all `d` of its roots are real, and set

`H = { a ∈ ℂ^d : p_a is hyperbolic }`.

Note `H ⊂ ℝ^d` automatically, since a polynomial all of whose roots are real has real coefficients.

> **Theorem.** `H` is not a complex-analytic set. Precisely: there is no connected open `U ⊆ ℂ^d` meeting `ℝ^d`, and no finite collection of holomorphic functions `h_1, …, h_k` on `U`, such that for every `a ∈ U`
>
> `p_a` is hyperbolic  ⟺  `h_1(a) = ⋯ = h_k(a) = 0`.
>
> Informally: **hyperbolicity is not the vanishing of holomorphic functions of the coefficients.**

**Proof.** Suppose such `h_j` existed. The polynomials with `d` *distinct* real roots form a nonempty open subset `W` of `ℝ^d`, and every one of them is hyperbolic, so each `h_j` vanishes on `W ∩ U`. Now `ℝ^d` is *maximally totally real* in `ℂ^d`: at a point of `W ∩ U`, the Taylor coefficients of a holomorphic `h_j` are exactly its iterated real partial derivatives, and those all vanish because `h_j ≡ 0` on a real neighbourhood of that point. So `h_j ≡ 0` near the point, hence `h_j ≡ 0` on all of `U` by the identity theorem. The right-hand side of the biconditional then holds at every `a ∈ U`; but `U` is open in `ℂ^d`, so it contains points with non-real coefficients, and those are never hyperbolic. Contradiction. `∎`

The whole content is that `ℝ^d` is totally real in `ℂ^d`, so the holomorphic category cannot see it.

**Corollary A (both parities are dead).** `H` is also not the *complement* of a complex-analytic set. Indeed the complement in `U` of a proper analytic subset is open and dense, whereas `H` has empty interior in `ℂ^d` (it lies inside the real-dimension-`d` subspace `ℝ^d` of the real-dimension-`2d` space `ℂ^d`). So neither

- "some holomorphically-varying quantity **vanishes**", nor
- "some holomorphically-varying quantity **fails to vanish**" (a genericity or non-degeneracy condition),

can be hyperbolicity. Every condition expressible as the vanishing or non-vanishing of holomorphically-varying data is excluded.

**Corollary B (obstructions).** Let `a ↦ E_a` be a family of holomorphic bundles depending holomorphically on the coefficients, as arises from any construction attaching a bundle to `p_a` holomorphically, and let `ω(a)` be a Griffiths extension obstruction class at any order. On a stratum where the obstruction group has constant dimension, `ω` is a holomorphic section of a holomorphic vector bundle, so `{ω = 0}` is locally cut out by finitely many holomorphic functions. By the Theorem it can never be `H`. So **no extension obstruction, at any order, detects hyperbolicity.**

**Why, in one sentence.** Yang–Mills equations are *equations*; hyperbolicity is a *region with interior*. `H` is a closed semialgebraic set of full real dimension `d` inside `ℝ^d`, with a boundary. Holomorphic equations cut out sets of complex codimension `≥ 1`. The two shapes are incompatible.

**The sharpest illustration** is the discriminant. `disc(p)` *is* a holomorphic function of the coefficients, and it vanishes exactly where two roots collide — which is `∂H`, the boundary. So a holomorphic equation can detect the **boundary** of hyperbolicity and never hyperbolicity itself. That is precisely what §4's numerics show: nullity `1` on the discriminant locus, nullity `0` on `H`. It is also worth noting that `Λ ≥ 0` places `Ξ` exactly on that boundary.

### Scope: what the theorem does not cover

Stated explicitly, because the limits are where the other memos had to do separate work.

- **Excluded:** any route whose discriminant is "this holomorphically-varying class or function vanishes (or is nonzero)". That is exactly the Witten/IYG/Pool obstruction shape, i.e. brief §7.1 and §7.2, and by Corollary A also every genericity/non-degeneracy condition of the same type.
- **Not excluded: existential conditions.** Memo 7's matching condition is "∃ admissible `(T, λ)` with `det M = P_p`" — the projection of an algebraic set, hence semialgebraic, and semialgebraic sets *can* have interior. This theorem says nothing about it. That is why memo 7 needed its own argument and why memo 12's positivity dichotomy is a separate result rather than a corollary of this one.
- **Not excluded: inequalities.** `L_n ≥ 0` (memo 10), `det M − P_p ≥ 0` (memo 8), `c_2 > 0` (memo 9) are all regional and all survive. Consistent — and the reason the surviving redirect in §5 is the CR category, where inequalities are native.

---

## 0. Result

**Three things. The third is the one that matters.**

**(1) Pool's ladder, from the primary source, with exact groups.** Memoir 358 §V is exactly the order-by-order treatment memo 10 hoped for, and it is fully readable. Every "unconfirmed" flag from memos 9–10 on the ambitwistor side is now closed:

| order `m` | obstruction group `H²(U", End E(−m,−m))` | ambiguity group `H¹(U", End E(−m,−m))` | verdict |
|---|---|---|---|
| 1 | `0` (Thm IV.4c) | `≅ Γ(U, End E[−1,−1])` (Thm IV.4a) | **unobstructed, non-unique** |
| 2 | `≅ Γ(U, End E[−1,−1])` (Thm IV.4d) | `0` (Thm IV.4b) | **unique** — see the mechanism below |
| 3 | `≅ Γ(U, ker d: Ω³⊗End E → Ω⁴⊗End E)` = axial currents (Thm IV.4e) | — | **obstruction `= *J = D(*F)`** (Thm V.4) |

And the mechanism for order-2 rigidity is sharper than "unobstructed": the order-1 ambiguity group and the order-2 obstruction group are *the same group*, `Γ(U, End E[−1,−1])`, and **Lemma V.1 says the connecting homomorphism between them is the identity.** So exactly one first-order extension has vanishing second obstruction, and since `H¹(U", End E(−2,−2)) = 0` that second extension is then unique (Theorem V.2). The first-order ambiguity is spent exactly cancelling the second-order obstruction. Pool's §V.3 — fourteen pages of Čech bookkeeping — exists to prove that one word, "identity".

**Theorem V.3 is the one that speaks to this programme.** The curvature is *second-order data on a `P¹ × P¹`*:

> `H¹(L_x, End E|_{L_x} ⊗ ⊙²N*_x) ≅ Ω²_M ⊗ End E|_x`, with `L_x = τ⁻¹(x) ≅ P₁ × P₁`,

and `F(x)` is the class representing the **difference between two canonical second-order extensions** of `E|_{L_x}` — the restriction of `E → U"` and the restriction of the trivial bundle. Pool also checks `H¹(L_x, End E ⊗ N*) = H²(L_x, End E ⊗ N*) = 0`, so the first-order extension on a single `L_x` is unique. That is exactly the rung and exactly the surface memo 10 §0(1) identified. Second-order normal data on `P¹ × P¹` **is** curvature, and it is a difference of extensions (an `H¹`), not an obstruction (an `H²`).

**(2) Two corrections to memo 10.** Both matter, and one withdraws a claim.

- **`H²` is the obstruction group; `H¹` is the ambiguity group.** Pool §V.2, quoting the standard theory: `E⁽ⁿ⁾` extends iff `η ∈ H²(U", End E ⊗ (N*)^{n+1})` vanishes, and then `H¹` of the same sheaf acts transitively on extensions. **Memo 10 §0(5) computed `H¹` and read it as the obstruction group.** On `Q = P¹ × P¹` the two have *disjoint* vanishing patterns — `h¹(O(a,b)) ≠ 0` iff the rulings enter with opposite signs, `h²(O(a,b)) ≠ 0` iff *both* `a, b ≤ −2` — so memo 10's conclusions invert. Symmetric twists `O(−c,−c)`, which memo 10 called obstruction-free, are the *only* ones with a nonzero obstruction group. **Memo 10's "the route is dead below degree 6" is withdrawn**: with the correct group, nothing is excluded on dimension grounds at any order (see §2).
- **`N* = O(−1,−1)` for ambitwistor space,** not `O(−2,−2)`. Pool §V.2: "using the easily calculated isomorphism `N* = O(−1,−1)`". The reason is that `A = {Z·W = 0}` is a **(1,1)-divisor** in `P³ × P³*`, so its defining section lies in `O(1,1)`. Memo 10 imported `O(−2,−2)` by analogy with a degree-2 hypersurface. `O(−2,−2)` *is* correct for our incidence quadric `Q ⊂ CP³`, which genuinely is a degree-2 hypersurface — but the two settings carry different conormal weights and their numerologies must not be mixed.

**(3) The obstruction route is closed, by a theorem.** This supersedes the screen, and it does not depend on which rung, which bundle, or which order. (Statement, proof, corollaries and scope are in *Statement of the theorem* above; the paraphrase below is kept for continuity.)

> **Proposition (holomorphic obstructions cannot detect hyperbolicity).** Parametrise monic real polynomials of degree `d` by their coefficients, `a ∈ Cᵈ`, and let `H ⊂ Rᵈ` be the hyperbolic locus. Suppose hyperbolicity of `p_a` were equivalent, on some connected open `U ⊆ Cᵈ`, to the vanishing of finitely many holomorphic functions `h₁,…,h_k` on `U` — which is what "the order-`m` obstruction class vanishes" means once the obstruction bundle is trivialised on a stratum of constant dimension. Then each `h_j` vanishes on `H ∩ U`, which contains a nonempty **open subset of `Rᵈ`** (the polynomials with `d` distinct real roots form an open set). But `Rᵈ` is **maximally totally real** in `Cᵈ`, so a holomorphic function vanishing on an open subset of it has all Taylor coefficients zero and vanishes identically. Hence every `a ∈ U` would be hyperbolic — false. `∎`

**The corollary is the point, and it is structural rather than technical:**

> The Yang–Mills equations are **equations**. Hyperbolicity is an **inequality region with nonempty interior in a real parameter space**. An equational condition cut out holomorphically cannot be a full-dimensional real region. So the "existence free, equation = obstruction to extension" shape — the thing that made Witten 1978 attractive, and the shape brief §1.4/§7.1 identified as the only productive one — **cannot carry reality of zeros, at any order, for any holomorphic family.**

This is the same fact as `appendix_ERRATA` §1, used in the opposite direction. There, `ℝ²` sitting maximally totally really inside `ℂ²` makes the `∂̄`-system *overdetermined* and hands you uniqueness for free. Here, `Rᵈ` sitting maximally totally really inside `Cᵈ` means the holomorphic category cannot *see* it at all. The programme has now met the totally-real dichotomy twice, from both sides.

**(4) What survives, and where it points.** Reality must enter through `ρ` — not as a symmetry the object happens to possess, but as part of the data whose vanishing is tested. Combined with memo 10 §0(3) (the σ-type invariant is not jet-local at any order, because `ρ` moves a Ruling-B line to the antipodal one) this closes brief §7.1 and §7.2 as stated. The one redirect that survives is the **CR category**, where inequalities are native — see §5. It is a redirect, not a lead, and it does not touch §6.5.

---

## 1. Pool's ladder, exact

Setting (Pool §II.1, §V.1): `A = {([Z^a],[W_a]) : Z^a W_a = 0} ⊂ P × P*`, a quadratic hypersurface, `dim 5`; `L_x = τ_A⁻¹(x) ≅ P₁ × P₁` for `x ∈ M`; `U" = τ⁻¹(U)`; `I` the ideal sheaf of `A` in `P × P*`; `N* = I/I²`; `U⁽ᵏ⁾` the `k`-th order neighbourhood.

The general theorem Pool quotes (§V.2, from Griffiths and Manin):

> **(a)** `E⁽ⁿ⁾` over `U⁽ⁿ⁾` extends to `E⁽ⁿ⁺¹⁾` over `U⁽ⁿ⁺¹⁾` **iff** the obstruction `η(E⁽ⁿ⁾) ∈ H²(U", End E ⊗ (N*)ⁿ⁺¹)` vanishes.
> **(b)** If `η(E⁽ⁿ⁾) = 0`, then `H¹(U", End E ⊗ (N*)ⁿ⁺¹)` acts transitively on the set of extensions.

Combined with `N* = O(−1,−1)` and Theorem IV.4 (the cohomology of `O(−k,−k)` on `U"`, proved via the relative deRham sequence and the Leray spectral sequence), the ladder is forced. Pool's own words at each rung:

- **Order 1.** "Since we know from the last chapter that `H²(U", O(−1,−1)) = 0` we use this to see that `H²(U", End E ⊗ (N*)) = H²(U", End E(−1,−1)) = 0` … Thus all the obstructions to first extension vanish, and `H¹(U", End E(−1,−1))` operates transitively on the set of first extensions. It is easy to verify that this action is also effective." So: **exists, non-unique, ambiguity `≅ Γ(U, End E[−1,−1])`.**
- **Order 2.** The obstruction lives in `H²(U", End E(−2,−2)) ≅ Γ(U, End E[−1,−1])` — the *same* group as the order-1 ambiguity. The connecting homomorphism of `0 → I²/I³ → I/I³ → I/I² → 0` induces an endomorphism of `Γ(U, End E[−1,−1])`, and **Lemma V.1: that endomorphism is the identity.** Theorem V.2 then reads: "there is exactly one first extension for which the obstruction to second extension vanishes. Furthermore, since `H¹(U", End E(−2,−2)) = 0`, there is a unique second order extension." So: **unique, by exact cancellation.**
- **Order 3.** "The obstruction to third order extension lies in `H²(U", End E(−3,−3))`, which … is isomorphic to `Γ(U, ker D : End E ⊗ Ω³ → End E ⊗ Ω⁴)`, the set of axial Yang-Mills currents." Theorem V.4: the image of that obstruction is `*J = D(*F)` exactly. So: **obstructed, obstruction = the current.**
- **Curvature, order 2, on `P¹ × P¹`.** Theorem V.3 and equations (5.10)–(5.11), quoted in §0(1) above.

Two things Pool does **not** settle, so they stay open: the ≥4th-order obstructions in the non-abelian case (Buchdahl's "at most `N²` for a bundle of rank `N`" is the only statement located, and its identification is still unread), and anything about real structures or equivariance. Pool's Theorem IV.4(b) is transcribed by OCR as "`H¹(U", O(−k,−k)) = 0, k ≥ 1`", which contradicts (a) at `k = 1`; the proof of Theorem V.2 uses it only at `k = 2`, so read it as `k ≥ 2`.

## 2. The corrected numerology on `Q`

With the right group, and `N* = O(−2,−2)` for our `Q ⊂ CP³`:

```
h^1(Q, O(a,b)) = h0(a) h1(b) + h1(a) h0(b)     nonzero iff opposite signs
h^2(Q, O(a,b)) = h1(a) h1(b)                   nonzero iff BOTH a,b <= -2
```

so for symmetric twists, `h¹(O(−c,−c)) = 0` and `h²(O(−c,−c)) = (c−1)²`: **rigid and genuinely obstructed**, the exact opposite of what memo 10 asserted. For the lift bundle `E = O ⊕ O(−d,0)` (whose `End` contains `O(d,0)`, `O(−d,0)` and `O` twice), at order `m` the twist is `O(−2m,−2m)`:

| summand of `End E` | obstruction group `h²` at order `m` | nonzero when |
|---|---|---|
| `O` | `(2m−1)²` | every `m ≥ 1` |
| `O(−d,0)` | `(d+2m−1)(2m−1)` | every `m ≥ 1` |
| `O(d,0)` | `max(2m−d−1,0)·(2m−1)` | `2m ≥ d+2` |

Nothing is excluded at any order. Memo 10's degree-6 threshold was an artifact of the wrong group and is withdrawn. (A nonzero group still does not mean a nonzero *class* — a trivial bundle extends trivially — so this table by itself neither opens nor closes anything. §3 is what closes it.)

One incidental observation worth recording, since it is the `Q`-analogue of Pool's cancellation: for the `O(d,0)` direction, `h¹ ≠ 0` iff `d ≥ 2m` and `h² ≠ 0` iff `d ≤ 2m−2`. These are complementary, and both vanish exactly at `d = 2m−1`. So `d` odd with `m = (d+1)/2` is a rigidity point in that direction, and the Yang–Mills rung `m = 3` corresponds to `d = 5`. Recorded, not pursued — §3 makes it moot.

## 3. The no-go

The theorem is stated and proved in *Statement of the theorem* above, with its two corollaries and its scope; §0(3) paraphrases it. Three points on its scope, because the strength of a no-go is the fine print.

**It does not need the obstruction to be a single function, or the extendability locus to be closed.** The hypothesis is only that hyperbolicity is *locally equivalent to the simultaneous vanishing of finitely many holomorphic functions of the parameters*. Every version of "the obstruction class vanishes" has that form on a stratum where the relevant cohomology dimensions are constant, and so does "some order-`n` extension has vanishing order-`(n+1)` obstruction" (the ambiguity acts affinely, so lying in the image is again a holomorphic linear condition). Dimension jumping only fragments the parameter space into strata; the argument applies on each stratum containing an open piece of `Rᵈ`, and the top stratum does.

**It does need the family to be holomorphic in the parameters.** For the lift `F̃ = F × id` it is: `Z(F̃) = pr₁*(Z(F))`, so the ideal sheaf and `O(Z)` depend holomorphically on the coefficients of `F`. That the Čech construction of the Griffiths obstruction (`ξ_{αβγ} = I − g_{αβ}g_{βγ}g_{γα}`, Pool §V.2) varies holomorphically with holomorphically-varying transition functions is standard deformation theory and is not separately verified here.

**A cheaper special case, worth having on its own.** For the product-type lift the natural line bundle is `O_Q(Z(F̃)) = pr₁* O_{P¹}(d)` — a *pullback*, whose isomorphism class depends only on `d = deg F` and not on the roots at all. So any invariant of the line bundle alone is blind before one even asks about obstructions. The divisor as a subscheme does remember the `ζ_i`, and `ρ` fixes a component `{ζ = ζ_i}` iff `ζ_i` is real; but "real" is not a holomorphic condition, which is the proposition again.

## 4. Verification

The proposition is an identity-theorem argument, so what is worth testing is its concrete consequence: **the hyperbolic locus is not contained in any proper hypersurface.** `lab_holomorphic_nogo.py` Part 3 samples the locus and asks for polynomial identities, with the discriminant locus as a positive control.

| locus (monic quartics, 1200 samples) | `K=2` | `K=3` | `K=4` | `K=5` | `K=6` |
|---|---|---|---|---|---|
| hyperbolic — nullity | 0 | 0 | 0 | 0 | 0 |
| discriminant (repeated root) — nullity | 0 | 0 | 0 | 0 | **1** |

The control behaves exactly as it must: nullity `1` first appearing at `K = 6`, the degree of the quartic discriminant, and the null vector *is* the discriminant — verified independently by evaluating the closed-form discriminant on the same samples (`max |disc| = 1.8e−07` against a coefficient scale of `46.6`). The separation is unambiguous in the singular values: on the discriminant locus the smallest relative singular value at `K = 6` is `1.16e−17`, seven orders below the next (`8.0e−11`); on the hyperbolic locus the spectrum bottoms out at `7.0e−10` with no gap — a double-precision conditioning floor, not a null vector. Hyperbolic sextics behave the same way (nullity 0 through `K = 4`, 210 monomials), so it is not a degree-4 accident.

Part 4 checks the converse-flavoured consistency: every discriminant this programme has actually found to work is non-holomorphic in the coefficients, as the proposition requires — memo 9's `c₂` is built from `σ_p = Im ρ_p`; memo 8's deficit and memo 10's Laguerre conditions are inequalities, the latter an infimum over real `x`. Nothing that works is the vanishing of a holomorphic function, and by §3 nothing that works could be.

## 5. What this closes, and the one redirect

**Closed.** Brief §7.1 ("a transform, with reality of zeros appearing as an output") and §7.2 ("a non-product bundle whose jumping divisor's σ-type is the invariant), *in the holomorphic category*. Memo 10 §0(3) closed the jet-locality half; §3 closes the equational half. Together: there is no holomorphic bundle-theoretic construction, at any order of thickening, whose extension obstruction is reality of zeros. The Witten/IYG/Pool shape is the wrong shape, and now for a stated reason rather than by pattern-matching to four previous failures.

That is a real loss. It was the last live lead in the brief, and it is the third mechanism (after the `1/r` trace term and the `Z(F) = Z(G)²` dimension count) to kill an approach for a reason having nothing to do with the previous two.

**The redirect, labelled as speculation.** The no-go is about the *holomorphic* category. Inequalities and full-dimensional real regions are native to the **real/CR** category, and that category is already in use for exactly this correspondence: Mason–Skinner replace the third-order holomorphic thickening by a smooth bundle on a real slice with `∂̄_a² = O((Z·W)⁴)`, and Borsten–Jurčo–Kim–Macrelli–Sämann–Wolf (arXiv:2408.16727) build a CR ambitwistor space `R⁴ × CP¹ × CP¹` whose reality acts antipodally on both factors — free, for the same reason `ρ` is free, and handling the supersymmetric case "without invoking higher formal neighborhoods". Our `(Q, ρ)` is the mixed variant of their structure, and Pool's `L_x⁽ⁿ⁾` is literally "`P¹ × P¹` with normal jets".

So the shape that is *not* excluded is: a `ρ`-equivariant CR object on the antipodal pair of Ruling-B lines with second-order normal data, with the discriminant an **inequality** on that data rather than the vanishing of a class. Note what that costs: an inequality on CR data is not an obstruction, so Proposition 1 of the brief applies again at full strength — one is back to building a hyperbolicity criterion, not a mechanism. And §6.5 is untouched: nothing in the CR category supplies a `Q`-structure either. The honest summary is that the redirect converts a closed direction into a direction that is merely subject to the programme's original objection.

## 6. Revised screening checklist

Two new screens, and one restatement, all cheap. Offered as a drop-in for brief §8; the numbering continues its list.

> **0. Equational or regional?** Write down whether the proposed condition is the *vanishing* of something or an *inequality*. Hyperbolicity is a closed region with nonempty interior in a real parameter space. If the proposal's condition is the vanishing of a holomorphically-varying quantity — an obstruction class, a cohomology class, a determinant identity, a curvature — it cannot cut out that region (§3). **Stop.** This screen is the cheapest in the list and it kills the entire holomorphic bundle-theoretic family in one line.
>
> **1′. Slice-statable? (restated.)** Read as: *is the condition determined by the restriction of the geometric object to a Ruling-B line (a slice), or by its normal 1-jet along one?* If so it carries no information — memo 9 (the 1-jet clause) and memo 10 §4 (the ruling clause, which also rescues the classical Laguerre/Turán/Jensen hierarchies from being wrongly discarded by the old wording).
>
> **1″. Is the invariant `ρ`-local?** If the discriminating invariant is the σ-type of divisor components, it compares a point with its `ρ`-image, which lies on the *antipodal* Ruling-B line. No finite-order jet along a single line reaches it, at any order (memo 10 §0(3)). The object must be the antipodal pair, or `Q` itself with descent.

Screen 0 is now the first thing to run, ahead of everything else in §8.

## 7. Status

Memos 9–11 have, between them: pinned the transverse jet order at exactly 2 and identified its Hessian as a Fubini–Study form on the normal bundle of a Ruling-B line; established the ambitwistor ladder from primary sources with exact groups; found that our discriminant sits in the curvature slot rather than the equation slot; and then shown that the equation slot could never have held it.

**Net: the geometric route is closed a second time, and this time the closing argument is one line long and does not depend on any construction.** `PROGRAM_CLOSED.md` stands, brief §6.5 is untouched, and the only thing memos 9–11 add to the positive side of the ledger is instrumental — the `L₁ >` Turán calibration, the radius-grading law, the four shielded test cases, and the `y₀²`/`σ²` degradation confirmed twice by independent routes.

**Novelty status: assume known.** §3 is the identity theorem for holomorphic functions restricted to a maximally totally real subspace — an undergraduate argument, and the observation that hyperbolicity is semialgebraic-with-interior while obstruction-vanishing is analytic is the kind of thing that is standard in real algebraic geometry. If any of memos 9–11 were to be circulated, §3 is the item most likely to be folklore and the one whose framing (as the reason the ambitwistor analogy fails) is the only part plausibly worth stating.

**Errata carried forward.** Memo 10 §0(5) and its §5 point 3 are withdrawn per §2 above; memo 10's `lab_obstruction_groups.py` computes the ambiguity group, not the obstruction group, and its "READING" paragraph should be disregarded. The script is retained for the `h¹` table itself, which is correct as a table.

---

*Certified by `lab_holomorphic_nogo.py`: Part 1, the `h¹`/`h²` Künneth tables on `P¹ × P¹` and their disjoint vanishing patterns; Part 2, the corrected obstruction groups for `E = O ⊕ O(−d,0)`; Part 3, the hyperbolic-locus identity test at degrees 4 and 6 with the discriminant locus as positive control (null vector verified against the closed-form quartic discriminant); Part 4, the holomorphy audit of the programme's working discriminants. The Proposition of §0(3) is a proof, not a computation. All statements about Pool are quoted from Mem. AMS 358 read directly; the ≥4th-order non-abelian obstructions and any treatment of real structures are NOT in Pool and remain open.*
