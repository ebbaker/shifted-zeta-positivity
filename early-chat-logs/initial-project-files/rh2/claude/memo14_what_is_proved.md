# What Is Proved, and Exactly Which Reformulations of RH It Invalidates

*Working memo #14 — August 24, 2026. A high-level audit, written to be checkable. Every theorem is stated self-contained; every invalidation names the reformulation it kills and the step at which it dies; every claim is marked **proved**, **empirical** or **inherited**. No new results. If you disagree with any argument, the numbering here is meant to make it possible to say exactly where.*

---

## 0. How to read this

Memos 7–13 tested seven distinct reformulations of RH in the quaternionic / twistor / gauge-theoretic language. Five are now closed by theorems, one by a strong empirical dichotomy, one by a structural inventory. This memo separates:

- **§1** — the seven reformulations, stated precisely;
- **§2** — the theorems, stated self-contained with proofs or proof sketches;
- **§3** — the invalidation map: which theorem kills which reformulation, and at which step;
- **§4** — what is **not** invalidated (the scope limits, which matter as much as the theorems);
- **§5** — the confidence ledger.

The single most important structural fact, from which most of the rest follows:

> **Hyperbolicity is a region, not an equation.** The set of hyperbolic real polynomials of degree `d` is a closed subset of `ℝ^d` with nonempty interior. Almost every reformulation tested here tried to characterise it by an equality — a matching identity, a vanishing obstruction, a triviality condition — and equalities cut out thin sets. That mismatch, in one form or another, is what kills reformulations R2 through R7.

---

## 1. The seven reformulations

**R1 — Sphere-free class plus symmetry.** *(brief §1.1, the original strategy.)* Find a class `𝒞` of functions `ℍ → ℍ` such that no member has a 2-sphere in its zero set. Show `Ξ` admits a member of `𝒞` that is rotationally equivariant. Conclude RH, since equivariance turns one off-axis zero into a whole sphere.

**R2 — Slice matching.** *(memo 8.)* Require a geometric object built from admissible data to agree with the rotational extension of `p` on a single slice `Π_e ⊂ ℍ`, or on an infinitesimal neighbourhood of one.

**R3 — Full four-dimensional matching.** *(memo 7, ADHM.)* Require `det(Δ†Δ)(q) = P_p(q)` identically on `ℍ`, where `P_p(q) = p(x_0+ir)p(x_0-ir)` and `Δ` is quaternionic ADHM data with `Δ†Δ` real.

**R4 — Obstruction as discriminant.** *(memos 9–11; the Witten / Isenberg–Yasskin–Green / Pool / LeBrun architecture.)* Attach to `Ξ` a holomorphic bundle on a complex manifold; let RH be equivalent to the vanishing of a Griffiths extension obstruction at some order of formal neighbourhood — the shape in which Yang–Mills appears at order 3 and Bach-flatness at order 5.

**R5 — σ-type of divisor components.** *(`twistor_lift_computation.md` §3, brief §7.2.)* On the incidence quadric `Q ≅ P¹_ζ × P¹_w` with real structure `ρ(ζ,w) = (ζ̄, −1/w̄)`, let RH be equivalent to: every component of the zero divisor of the lift of `Ξ` is `ρ`-invariant.

**R6 — Weil positivity via a geometric trace form.** *(brief §6.5, memo 13.)* Realise the trace form attached to `Ξ` (or to its Jensen truncations) as the intersection form of a geometric object over `ℤ` or `ℚ`, so that definiteness becomes a Hodge-index theorem.

**R7 — Spectral-curve reality.** *(brief §7.3, memo 13 §0(5).)* Use Hitchin's monopole correspondence: a curve `S ∈ |O(2k)|` in mini-twistor space with `σ(S) = S`, `L²|_S` trivial, and `H⁰(S, L^s(k−2)) = 0`.

---

## 2. The theorems

### T1 — No free lunch **(inherited; proof is two lines)**

> Let `𝒞` be any class of functions `ℍ → ℍ` no member of which has a 2-sphere in its zero set. Suppose one proves: *if `f` is real entire and has property `P`, then `f` admits an equivariant extension in `𝒞`.* Then `P` implies `f` is hyperbolic.

*Proof.* If `f` has a zero `a+ib`, `b ≠ 0`, any equivariant extension vanishes on the whole sphere `a + b𝕊`, contradicting the defining property of `𝒞`. So no such extension exists, so `P` fails. `∎`

**Consequence, correctly scoped (see memo 16 §1).** T1 is about *theorems of this quantified form* and is **silent on the single-function approach**. What is load-bearing is instead the identity behind it: for an equivariant `F = A + ωB`, `F = 0 ⟺ A = B = 0`, so the off-axis zero set is `{A=B=0} × S²` and **"sphere-free" and "the stem has only real zeros" are the same statement**. Moreover an equivariant `F` is determined by its restriction to one slice, so "equivariant and restricts to `Ξ`" forces `F = RΞ` — there is nothing to search over. T1's real use is as a *diagnostic*: it catches the failure mode where the implication `RΞ ∈ 𝒞 ⟹` hyperbolic is a triviality. It closed nothing by itself.

### T2 — The jet-order theorem **(proved; symbolic verification in `lab_jet_order.py`)**

Setting: memo 8's family, where the matching condition on one slice forces `T_a = e_aS` (`a=1,2,3`) with `S` real symmetric commuting with `T_0`. Write `Im q = t e + n` with `n ⊥ e`, `ν = |n|` the distance to the slice `Π_e`, and let `τ_j ± iσ_j` be the roots of `p`.

> The deficit `det M − P_p` is an **even** polynomial in `ν` with no constant term. Its lowest nonvanishing order is `ν²`:
>
> `det M − P_p = 4ν² · R_0 Σ_p σ_p² ∏_{q≠p}(B_{q,0}² − 4t²σ_q²) + O(ν⁴)`,
>
> with `R_0 = ∏_{real roots}(A + t²) > 0` and each `B_{q,0}² − 4t²σ_q² = (A_q+(t−σ_q)²)(A_q+(t+σ_q)²) > 0`. Hence the `ν²` coefficient is `> 0` unless every `σ_p = 0`.

*Why.* Within the family, `Σ_{a≥1} x_a T_a = tS`, so `M` depends on `q` only through `(x_0, t, ν²)` while `P_p` depends only on `(x_0, t²+ν²)`. Evenness and transverse isotropy are immediate; pairing conjugate roots makes corresponding factors differ by exactly `4ν²σ²`, and telescoping gives the formula.

**Consequence.** The ladder is: the slice itself carries no information (every real monic `p` is realised); the **first** infinitesimal neighbourhood carries none either, by evenness in `ν`; the **second** already forces `S = 0`. No intermediate order.

**Scope (see memo 16 §2).** This is a **rigidity** statement about one finite-dimensional polynomial family, not a claim that infinitesimal data detects zeros. The chain is `2-jet = 0 ⟹ S = 0 ⟹ T_0` symmetric `⟹` real spectrum `⟹` hyperbolic, and the last three steps are algebra. One step outside the family it fails at *every* order simultaneously: T5's datum has deficit identically zero on all of `ℍ` with `p` non-hyperbolic. So "any object must place its discriminant at order `≥ 2`" is **withdrawn**; the order structure must be re-derived for each new family.

### T3 — The transverse Hessian, and the reality of slices **(proved; `lab_q_normal_form.py`)**

(a) In the twistor coordinates of `twistor_lift_computation.md` — `η(w) = (w+j)^{-1}i(w+j)`, `q = x + y·η(w)`, `ζ = x+iy` — a slice `Π_e` is the **Ruling-B line** `{w = w_0}` of `Q`, and

> `ν² = r² − t² = y² sin²θ = 4y² · g_FS(dw,dw) + O(|dw|⁴)`,

so T2's transverse Hessian is a positive **Hermitian** form on the normal bundle of a Ruling-B line — a multiple of the Fubini–Study metric on the sphere of complex structures. The rank-2 isotropy observed in T2 is the `U(1)`-invariance of the round metric; the "2" is one complex dimension.

(b) `ρ` acts **antipodally** on the `w`-sphere (`η(−1/w̄) = −η(w)`), so it maps `{w = w_0}` to `{w = −1/w̄_0}`, whose complex structure is exactly antipodal. Since `w_0 = −1/w̄_0` needs `|w_0|² = −1`:

> **No Ruling-B line is `ρ`-invariant.** Equivalently: no slice is real. By contrast `ρ(L_ζ) = L_{ζ̄}`, so a Ruling-A line is `ρ`-invariant exactly when `ζ` is real — which is the σ-type invariant.

**Consequence.** The σ-type invariant compares a point with its `ρ`-image, which lies on a *disjoint* Ruling-B line at finite distance. **No finite-order jet along a single slice can see it, at any order.** T2's order-2 collapse works by a different mechanism — the ADHM blocks are globally real by hypothesis — not because a jet detects σ-type.

### T4 — The equational no-go **(proved; three lines)**

Setting: monic real polynomials of degree `d`, parametrised by coefficients `a ∈ ℂ^d` with `ℝ^d ⊂ ℂ^d` the real ones. `H = {a : p_a` has all roots real`}`; note `H ⊂ ℝ^d` automatically.

> **Theorem.** `H` is not a complex-analytic set. There is no connected open `U ⊆ ℂ^d` meeting `ℝ^d` and no finite set of holomorphic `h_1,…,h_k` on `U` with, for all `a ∈ U`: `p_a` hyperbolic `⟺ h_1(a) = ⋯ = h_k(a) = 0`.

*Proof.* Polynomials with `d` distinct real roots form a nonempty open `W ⊆ ℝ^d`, all hyperbolic, so each `h_j` vanishes on `W ∩ U`. But `ℝ^d` is maximally totally real in `ℂ^d`: the Taylor coefficients of a holomorphic function at a point of `W` are its iterated *real* partial derivatives, all of which vanish. So `h_j ≡ 0` near that point, hence on `U`. Then every `a ∈ U` would be hyperbolic — false, since `U` contains points with non-real coefficients. `∎`

> **Corollary A (both parities).** `H` is also not the *complement* of an analytic set: complements of proper analytic subsets are open and dense, while `H` has empty interior in `ℂ^d`. So neither the vanishing **nor** the non-vanishing of holomorphically-varying data can be hyperbolicity — genericity and non-degeneracy conditions are excluded too.

> **Corollary B (obstructions).** If `a ↦ E_a` is a holomorphic family of holomorphic bundles and `ω(a)` a Griffiths obstruction at any order, then on a stratum of constant obstruction-group dimension `ω` is a holomorphic section, so `{ω = 0}` is locally cut out by holomorphic functions and can never be `H`.

**Why, in one sentence.** Yang–Mills equations are *equations*; hyperbolicity is a *region with interior*. Equations cut out sets of complex codimension `≥ 1`.

**The sharpest illustration.** `disc(p)` *is* holomorphic in the coefficients, and vanishes exactly where two roots collide — i.e. on `∂H`. So a holomorphic equation reaches the **boundary** of hyperbolicity and never hyperbolicity itself. Verified: on the discriminant locus of monic quartics the identity test finds nullity exactly `1` first at degree `6` (the discriminant's degree), with the null vector *being* the discriminant; on `H` itself, nullity `0` at every degree tested, for quartics and sextics alike.

### T5 — Memo 7's collapse is exactly the spectral theorem **(proved; symbolic for symbolic `p`)**

> For the shape `M(q) = C + |q|²I − 2Σ_a x_aT_a` with `T_a, C` arbitrary real: take `T_0` any real matrix with characteristic polynomial `p` (e.g. the companion matrix), `T_1=T_2=T_3 = 0`, `λ = 0`, `C = T_0²`. Then `M(q) = (T_0 − x_0I)² + r²I`, so `det M = ∏_j((x_0−τ_j)² + r²) = P_p` — **for every real monic `p`, hyperbolic or not.**

Verified symbolically at `k=2` for symbolic coefficients (`det M − P_p → 0`) and numerically to `10⁻¹³` across the test set. Walking memo 7 §4.4's proof on this datum: the trace relation, `κ = 0`, `λ = 0`, `T_{1,2,3}=0` and `C = T_0²` all **hold**; the only step that fails is the last, *"`T_0` real symmetric, hence its eigenvalues are real."* The counterexample even satisfies the nonlinear ADHM equations exactly.

**Consequence.** Memo 7's theorem is the spectral theorem for real symmetric matrices and nothing else, and the symmetry it needs is ADHM's reality condition specifically. It therefore does **not** transfer to a class with a different reality condition — so it never closed the full-Yang–Mills direction, contrary to what memos 9–11 assumed.

### T6 — The positivity dichotomy **(empirical, unproven)**

Searching the same shape over nested families, at `k = 2,3`:

| `p` | `T` gen, `C` gen | `T` gen, `C` sym | `T` gen, `C` sym **PSD** | `T` **sym**, `C` sym |
|---|---|---|---|---|
| `z²−1` (hyp) | 3.6e−15 | 3.4e−15 | 3.6e−15 | 1.4e−14 |
| `z²+1` (NOT) | **1.4e−14** | **1.2e−14** | **0.618** | **0.978** |
| `z²+z+1` (NOT) | **1.3e−14** | 0.140 | **0.316** | **0.645** |
| `(z−1)((z+2)²+9)` | **1.4e−14** | — | **1.17** | **1.83** |

> `C ⪰ 0` alone, with the four blocks completely unconstrained, forces hyperbolicity — 13 orders of separation. Symmetry of the `T_a` independently forces it. Neither is necessary given the other; both are sufficient.

**Consequence, stated as a dichotomy.** In a matching-style dictionary, **structural positivity is not a resource but the trap**: a class supplying positivity automatically forces the conclusion (circularly), and a class not supplying it is contentless (every real monic `p` is realised). This localises brief §3's rigidity/existence trade-off to a specific hypothesis for the first time. It also closes full Yang–Mills *because* it is a gauge theory: the action density is exactly such a positivity.

**Status.** Empirical. `k = 2,3`, three non-hyperbolic targets, 25 random starts per family, plateaus at `0.3–1.2` against `10⁻¹⁵` controls. A proof is the sharpest open item in memos 9–13.

### T7 — The ALE existence condition is linear; `∂H` is not **(proved; primary source now in hand)**

Kronheimer's Theorem 1.1 supplies an ALE hyperkähler structure with prescribed Kähler classes `α_1,α_2,α_3` under the nondegeneracy condition which, in his own words (§4), *"just says that the `α_i` do not all lie in the kernel of any one root"*. By his Proposition 2.8 the bad set is a union of **codimension-3 real linear subspaces** `ℝ³ ⊗ D_θ`, one per root, and by his Proposition 4.1 the period map `σ : Z → 𝔥` is a **linear isomorphism**.

> So the only discriminant the ALE existence theorem can express is a finite union of *linear* conditions on the periods. But `∂H` is contained in the discriminant hypersurface, which is **irreducible of degree `2(d−1)` and never a product of linear forms** (verified symbolically for `d = 2,3,4,5`). No finite union of linear subspaces has `H` as its closure.

Also confirmed from Kronheimer §4, verbatim: the exceptional set's intersection matrix is *"the negative of a Cartan matrix"*, `H²(X_ζ;ℤ)` **is the root lattice**, and the `Σ·Σ = −2` classes are the roots.

---

## 3. The invalidation map

| reformulation | killed by | the step at which it dies |
|---|---|---|
| **R1** sphere-free + symmetry | **T1** | The geometry contributes only "equivariant + sphere-free ⇒ real", a triviality. All weight rests on the hypothesis `P`, which must be at least as strong as hyperbolicity. Not fatal, but it means the route is a criterion factory unless `P` is independently provable. |
| **R2** slice matching | **T2** | Order 0 and order 1 are *satisfiable for every real monic `p`* — so they carry no information at all. Order 2 forces `S = 0`. The condition is either empty or the conclusion; there is no order in between. |
| **R3** full 4D matching | **T5 + T6** | T5: memo 7's collapse is the spectral theorem, so "existence ⇒ hyperbolic" is Sylvester's law in disguise (brief screen 9, circularity). T6: and the hypothesis actually doing the work is `C ⪰ 0`, i.e. exactly the structural positivity the class was chosen for. |
| **R4** obstruction as discriminant | **T4 + Cor B** | An obstruction class is a holomorphically-varying quantity; its vanishing locus is analytic; `H` is not. Dead at *every* order, for *every* bundle, in *every* one of the ladders (Yang–Mills at 3, Bach at 5, conformal-Einstein at 6). |
| **R5** σ-type of divisor components | **T3(b) + T4** | T3(b): σ-type is not detectable by any finite-order jet along a slice, because `ρ` moves the base line to the antipodal one. T4: and as a global holomorphic condition, "`ζ_i` real" is not analytic — reality is not a holomorphic predicate. |
| **R6** Weil positivity geometrically | **T7 + the rationality dichotomy** | Every geometric form on offer is integral but **rigid** (ADE root lattices, `−I_k`, Hirzebruch–Jung strings, the Beauville–Bogomolov form): entries are fixed small integers carrying no `Ξ`-dependence. Every form carrying `Ξ`-dependence (Jensen trace forms, the ADHM Gram, T2's Hessian) has entries built from the moments `M_k = ∫Φ(u)u^k du` and no known `ℚ`-structure. No known object is in both classes. |
| **R7** spectral-curve reality | **T4 + Cor A** | The three Hitchin conditions split: `σ(S)=S` is a totally real linear slice (right shape, but imposed by hand — no information); `L²|_S` trivial is a holomorphic vanishing (dead by T4); `H⁰(S,L^s(k−2))=0` is a genericity condition (dead by Cor A). |

**Two remarks on the map.** First, T4 is doing most of the work, and it is the cheapest theorem here — three lines. That asymmetry is worth noticing: the programme spent a long time on constructions before checking whether the *shape* of the target condition was achievable at all. Second, R2 and R3 die by mechanisms with nothing in common (jet order; positivity), and R4–R7 die by one mechanism (analytic vs. regional). The first pair are facts about quaternionic algebra; the second group is a fact about `ℝ^d ⊂ ℂ^d`.

---

## 4. What is NOT invalidated

This section matters as much as §3, and it is where I would most want disagreement surfaced.

**(a) T4 excludes characterisations, not sufficient conditions.** T4 says no holomorphic system cuts out `H` *exactly*. A one-way implication is not excluded: `{h = 0} ⊆ H` is perfectly consistent with `h` holomorphic. And a proof of RH needs only a sufficient condition satisfied by `Ξ`.

*But the loophole collapses.* An analytic set contained in `ℝ^d` has no complex tangent directions (`ℝ^d` is totally real, so it contains no complex line), hence is **zero-dimensional** — a discrete set of points. So any analytic sufficient condition for hyperbolicity can "know" only finitely many polynomials at a time, which means the construction encodes the answer rather than deriving it. That is T1 again.

**(b) T4 does not exclude existential conditions.** Memo 7's matching condition is "∃ admissible `(T,λ)` with `det M = P_p`" — the projection of an algebraic set, hence semialgebraic, and semialgebraic sets *can* have interior. T4 says nothing about R3, which is why R3 needed T5 and T6.

**(c) T4 does not exclude inequalities.** `L_n ≥ 0`, `det M − P_p ≥ 0`, `c_2 > 0` are all regional and all survive. This is why the one surviving redirect is the **CR category**, where inequalities are native — and why the classical hierarchies (Laguerre, Turán, Jensen) are untouched by anything here.

**(d) T2 and T3 are statements about a specific family**, namely memo 8's `R1` family inside quaternionic ADHM data. They are proved there and nowhere else. The *interpretation* — "information lives on the transverse sphere directions" — is an extrapolation supported by five independent instances, not a theorem about all classes.

**(e) T6 is not proved.** If it is false, R3 reopens in the form: a class with structural positivity that nonetheless does not force hyperbolicity.

**(f) Nothing here touches the arithmetic side.** brief §6.5 is untouched, and none of T1–T7 says anything about whether a `ℚ`-structure could exist — only that no known construction supplies one together with `Ξ`-dependence.

**(g) One genuine gap.** Full Yang–Mills supplies a degree of freedom self-dual theory lacks: a nonzero current `*J`. "`*J = 0`" is equational and dead by T4, but an *inequality* on the current or on the action density is regional, hence outside T4, outside T3, and untested. It is a gap rather than a lead — there is no candidate transform from `Ξ`'s data, T1 applies, and by T6 an inequality on a positive quantity is the shape that collapses — but it is not closed.

---

## 5. Confidence ledger

**Proved (rigorous, with symbolic or exact verification):**

- T1 — no free lunch. Two lines; inherited from brief §1.3.
- T2 — the jet-order theorem, including that order 1 is empty for a structural reason.
- T3(a) — `ν² = 4y²g_FS + O(ν⁴)`; T3(b) — `ρ` is free, no slice is real.
- T4 — the equational no-go, with Corollaries A and B.
- T5 — the companion-matrix counterexample, symbolic for symbolic `p` at `k=2`.
- T7 — the ALE condition is linear; the discriminant is irreducible and non-linear.

**Empirical (strong, unproven):**

- T6 — `C ⪰ 0` alone forces hyperbolicity. `k = 2,3`; 13 orders of separation.
- The Laguerre index grades by sphere radius (`n_first(y_0)` monotone: `1,1,1,1,2,3,5,7,8,8` for `y_0 = 0.01 … 30`); no `L_n` counterexample at degree 4 or 6 (optimiser walks to the hyperbolic boundary, margins `9.2e−14` and `1.6e−12` at pair radii `1.1e−08`, `1.2e−05`).
- `L₁` is strictly stronger than Newton/first-Turán on the standard test set (memo-5 quartic: `Σρ² = 1.1298 > 0` but `min_x L₁ = −4.52e−06`).

**Inherited, not verified here:**

- Csordas–Varga, that `L_n ≥ 0` for all `n` characterises the Laguerre–Pólya class.
- Rodgers–Tao, `Λ ≥ 0`; Polymath15, `Λ ≤ 0.22`.
- The ambitwistor ladder (Witten/IYG; Buchdahl; Eastwood; Pool read directly, so this one is primary-sourced); the gravity ladder (LeBrun, via the Atiyah–Dunajski–Mason review — order numbers 5 and 6 confirmed, the Bach / Eastwood–Dighton split unconfirmed).
- brief §6.1 (multiplicative rigidity), §6.2 (the linear no-go), §6.3's degree computation.

**Withdrawn:**

- Memo 10 §0(5) — computed `H¹` (the ambiguity group) and read it as `H²` (the obstruction group). Its "dead below degree 6" is void.
- Memo 7 §4.4's item 3 — "symmetry is load-bearing in exactly one place" is wrong; see T5.
- Memo 7 §4.4's "positive semidefiniteness of `C` is not needed anywhere" — true of that proof, misleading as a claim; see T6.

---

## 6. The logical map, on one page

```
                         RH  =  "Xi is hyperbolic"
                                     |
             +-----------------------+------------------------+
             |                                                |
      GEOMETRIC ROUTES                              CLASSICAL ROUTES
   (build an object from Xi)                    (inequalities on Xi itself)
             |                                                |
   +---------+---------+                          Laguerre L_n >= 0
   |                   |                          Turan / Newton
 MATCHING           OBSTRUCTION                   Jensen hyperbolicity
 (equality of      (vanishing of a                       |
  loci/dets)        cohomology class)             untouched by T1-T7,
   |                   |                          but supply no geometry,
   |                   +-- R4, R5, R7             so T1 applies: criterion
   |                       killed by T4 + Cor A/B factories, and §6.5
   |                       ("equations cannot cut  (rationality) is the cap
   |                        out a region")
   |
   +-- R2 slice matching  -- killed by T2
   |     order 0: empty.  order 1: empty.  order 2: collapse.
   |
   +-- R3 full matching   -- killed by T5 + T6
   |     the collapse IS the spectral theorem; the load-bearing
   |     hypothesis is positivity, which is what made the class
   |     attractive in the first place
   |
   +-- R6 Weil positivity -- killed by T7 + the rationality dichotomy
         integral-but-rigid  vs.  Xi-dependent-but-real;
         nothing is in both classes

  SURVIVING SHAPES (not routes):
    * inequalities on CR / real data                 (outside T4)
    * an inequality on the Yang-Mills current        (outside T4, T3; untested)
    * anything supplying a Q-structure that also varies with Xi
      (nothing known; this is brief §6.5, now stated as a two-question screen)
```

---

*No computations in this memo; every number is quoted from memos 9–13 and their results files. The theorem statements are self-contained restatements, not new proofs. Where a proof is one or two lines it is given in full so it can be checked here rather than by cross-reference.*
