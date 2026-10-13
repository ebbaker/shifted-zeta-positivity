# Isolated Zeros and Transverse Rigidity — v2

**A self-contained brief for the quaternionic / gauge-theoretic approach to RH.**

*v1 assembled 2026-08-23 from working memos 6–8, `twistor_lift_computation.md`, `appendix_slice_extension_uniqueness.tex` and the lab code. v2 assembled 2026-08-24, folding in memos 9–15. Written to stand alone. All results carry their status (proved / empirical / inherited / withdrawn).*

---

## Changelog from v1

Read this first if you know v1.

| section | change |
|---|---|
| **§1.5 (new)** | The equational no-go theorem. Hyperbolicity is not the vanishing of holomorphic functions of the coefficients. This is now the cheapest and most powerful screen in the document. |
| **§2.7 (new)** | The transverse jet order is exactly **2**: order 0 and order 1 carry no information, order 2 collapses. The transverse Hessian is identified as the Fubini–Study metric on the sphere of complex structures. And: no slice is `ρ`-real, so the σ-type invariant is not jet-detectable at any order. |
| **§3.5 (new)** | The rigidity/existence trade-off is localised: **positivity is the trap**. `C ⪰ 0` alone forces the collapse with everything else dropped. |
| **§4.4** | **Errata.** Two claims in v1's "stronger than first stated" are wrong or misleading. The collapse theorem is exactly the spectral theorem for real symmetric matrices, and there is a closed-form counterexample once symmetry is dropped. |
| **§6.4** | **Demoted.** "No uniform separation" is not a screen; it is an identity. Every discriminant in this family is a configuration-dependent multiple of `y_0²/2`. |
| **§6.5** | **Rewritten** as the rationality *dichotomy*, which is a screen rather than an observation. |
| **§7** | All of §7.1, §7.2, §7.3 are now **closed**. |
| **§8** | Three new screens (0, 0″, 8′), two restatements (1′, 1″), one demotion (§6.4's). Screen 0 goes first. |
| **§9.2** | `Λ(p)`, the De Bruijn–Newman threshold, added as the canonical instrument — it dominates `L_1`, `P_m` and Turán. Four new shielded test cases. `L_1 >` Turán established. |
| **§10** | Status: the geometric route is closed a second time, by a one-line argument independent of any construction. One method-level criticism added that applies even to proposals clearing every screen. |

---

## 0. Scope

This document collects everything from the quaternionic RH work that is **not** about slice regular functions, plus the small number of slice-regular results that survive as constraints.

The slice-regular investigation was a detour; its own conclusion was that it could not contribute, because `ℍ` has no commutative subalgebra larger than a slice, so `ℂ → ℍ` cannot do the work that `ℝ → ℂ` does. Three things from that period are load-bearing and are carried as **inherited constraints** (§6): multiplicative rigidity (§6.1), the linear no-go (§6.2), and the Vekua trace term (§2.3).

**The one substantive positive result of the whole arc is §2**: a structural principle about *where* information about reality of zeros lives, now with five independent derivations, one exact formula, and (new in v2) an exact jet order. **§§1.5, 3.5, 6.5 and 8 are the negative results**, and after memos 9–15 they are the part of the document with the most use left in it: they make it cheap to stop.

---

## 1. The strategy

### 1.1 The idea

Let `Ξ` be the Riemann `Ξ`-function, real entire, with RH equivalent to all its zeros being real. Identify `ℍ` with `ℝ⁴`, write `q = x_0 + x_1i + x_2j + x_3k`, `Im q = q − x_0`, `r = |Im q|`, `𝕊 = {J ∈ ℍ : J² = −1}` the 2-sphere of imaginary units, `ℂ_J = ℝ + Jℝ` the **slice** through `J`.

> Find a class `𝒞` of functions `ℍ → ℍ` in which **no member has a 2-sphere in its zero set**. Show `Ξ` admits a member of `𝒞` that is **rotationally symmetric**. Conclude RH.

The mechanism: symmetry turns a single off-axis zero into a whole sphere. If `F(uq\bar u) = uF(q)\bar u` and `F(a + bI_0) = 0` with `b ≠ 0`, then `F` vanishes on `a + b𝕊`, which `𝒞` forbids.

### 1.2 The logical skeleton

**Symmetry cannot be dropped from the argument, only from the class.** Without it, a member of `𝒞` extending `Ξ` from a slice simply has `Ξ`'s non-real zeros as isolated points on that slice; no contradiction.

**For a symmetric member, "isolated zeros" *is* the conclusion, not a step toward it.** An equivariant `F` has the axial form `F(q) = A(x_0,r) + ωB(x_0,r)` with `ω = Im q/r`, so its off-axis zero set is `{A = B = 0} × 𝕊` — a union of spheres, automatically. Membership in a sphere-free class therefore says exactly "no off-axis zeros."

So the entire content sits in **existence**.

### 1.3 Proposition 1 (no free lunch) — **proved**

> Let `𝒞` be any class of functions `ℍ → ℍ` no member of which has a 2-sphere in its zero set. Suppose one proves: *if `f` is real entire and has property `P`, then `f` admits an equivariant extension in `𝒞`.* Then `P` implies `f` is hyperbolic.

*Proof.* If `f` has a zero `a+ib`, `b ≠ 0`, any equivariant extension vanishes on `a + b𝕊`, contradicting the defining property of `𝒞`. So no such extension exists, so `P` fails. `∎`

**Scope — read this before using Proposition 1 (corrected in v2, memo 16 §1).** Proposition 1 is a statement about *theorems of a quantified form*. It is **silent on the single-function approach**: if one exhibits, for `Ξ` alone, an equivariant member of `𝒞` by any means, RH follows and Proposition 1 says nothing. v1's phrase "criterion factory, not a proof mechanism" is wrong on two counts — it overstates the proposition, and *every* serious attack on RH is a criterion plus a verification (Weil positivity, Hilbert–Pólya and Li's criterion all are). Being a criterion is not the defect; being a **circular** criterion is.

**What is load-bearing is §1.2's identity, not Proposition 1.** For an equivariant `F = A + ωB`, `F(q) = 0 ⟺ A = B = 0` — a condition on `(x_0,r)` only — so the off-axis zero set is `{A = B = 0} × S²` and *every* off-axis zero carries its whole sphere. Hence **"sphere-free" and "the stem has only real zeros" are the same statement**, relabelled. That applies to the single-function version exactly as much as to the quantified one.

**And there is no freedom to search over.** An equivariant `F` is recovered exactly from its restriction to one slice (verified to `0.00e+00` over 500 random points), so "equivariant, and restricts to `Ξ` on a slice" forces `F = RΞ` uniquely. The question is one yes/no about one predetermined object: **is `RΞ ∈ 𝒞`?** Freedom returns only on weakening "restricts to `Ξ`" — prescribing `F` on `ℝ` alone leaves an infinite-dimensional family (appendix Prop. A.5) — which is exactly what §7.1 proposed.

**So the correct use of Proposition 1 is as a diagnostic.** The strategy, however executed, ends at "`𝒞` sphere-free (a theorem about `𝒞`) plus `RΞ ∈ 𝒞` (to be verified) ⇒ RH": the geometry supplies the implication and can never supply the verification. Proposition 1 catches the failure mode where the implication is a triviality — which it did three times (§4.4, §4.5, §5) — but in each case the *closing* argument was the specific computation. **Proposition 1 closed nothing.** A route is still worth pursuing only if the condition `RΞ ∈ 𝒞` is independently accessible: a growth bound, a positivity of `Φ`, a self-adjointness, a Fredholm-determinant representation.

### 1.4 Where to aim

The productive form is a class whose **existence theorem is cheap** and whose **isolation property is a theorem**. Nonlinear self-duality is the natural home for that shape — existence from a PDE/twistor correspondence, isolation from a Liouville or energy argument — which is why the Yang–Mills excursion was not a wrong turn. §7 records what became of it.

### 1.5 The equational no-go — **proved** (new in v2)

This is the cheapest result in the document and it does the most work. It should be applied before anything else.

**Setup.** Fix `d`. Parametrise monic polynomials of degree `d` by their coefficient vector `a = (a_0,…,a_{d−1})`, allowing complex coefficients, so the parameter space is `ℂ^d` with the real ones as `ℝ^d ⊂ ℂ^d`. Let `H = {a ∈ ℂ^d : p_a` has all roots real`}`. Note `H ⊂ ℝ^d` automatically.

> **Theorem.** `H` is not a complex-analytic set. There is no connected open `U ⊆ ℂ^d` meeting `ℝ^d` and no finite collection of holomorphic `h_1,…,h_k` on `U` such that for all `a ∈ U`:
>
> `p_a` is hyperbolic  ⟺  `h_1(a) = ⋯ = h_k(a) = 0`.

*Proof.* Polynomials with `d` distinct real roots form a nonempty open `W ⊆ ℝ^d`, all hyperbolic, so each `h_j` vanishes on `W ∩ U`. But `ℝ^d` is maximally totally real in `ℂ^d`: the Taylor coefficients of a holomorphic function at a point of `W` are its iterated *real* partial derivatives, all of which vanish there. So `h_j ≡ 0` near that point, hence on `U` by the identity theorem. Then every `a ∈ U` would be hyperbolic — false, since `U` contains points with non-real coefficients. `∎`

> **Corollary A (both parities).** `H` is also not the *complement* of an analytic set: complements of proper analytic subsets are open and dense, while `H` has empty interior in `ℂ^d`. So neither the vanishing **nor** the non-vanishing of holomorphically-varying data can be hyperbolicity — genericity and non-degeneracy conditions are excluded too.

> **Corollary B (obstructions).** For a holomorphic family `a ↦ E_a` of holomorphic bundles and a Griffiths extension obstruction `ω(a)` at any order, `{ω = 0}` is locally cut out by holomorphic functions on any stratum of constant obstruction-group dimension, so it can never be `H`. **No extension obstruction, at any order, detects hyperbolicity.**

**Why, in one sentence.** Yang–Mills equations are *equations*; hyperbolicity is a *region with interior*. Equations cut out sets of complex codimension `≥ 1`.

**The illustration.** `disc(p)` *is* holomorphic in the coefficients and vanishes exactly where two roots collide — on `∂H`. So a holomorphic equation reaches the **boundary** of hyperbolicity and never hyperbolicity itself. (Verified: on the discriminant locus of monic quartics the polynomial-identity test finds nullity exactly `1`, first at degree `6`, the null vector *being* the discriminant; on `H` itself, nullity `0` at every degree tested, quartics and sextics alike.)

**Scope — what this does not exclude.** Three things, and they are where §§3.5, 6.5 had to do separate work.

- **Existential conditions.** "∃ admissible data with `det M = P_p`" (§4) is the projection of an algebraic set, hence semialgebraic, and semialgebraic sets *can* have interior. Untouched by §1.5.
- **Inequalities.** `L_n ≥ 0`, `det M − P_p ≥ 0`, `c_2 > 0` are all regional and all survive.
- **One-way implications.** `{h = 0} ⊆ H` is consistent with `h` holomorphic — but only barely: an analytic subset of `ℂ^d` contained in `ℝ^d` has no complex tangent directions, hence is **zero-dimensional**. So an analytic sufficient condition can "know" only finitely many polynomials, which means the construction encodes the answer. That is §1.3 again.

---

## 2. The transverse-sphere principle

### 2.1 Statement

> **Principle.** In the quaternionic setting, all information distinguishing real zeros from zero spheres is supported on the directions **transverse to any single slice** — the 2-sphere of complex structures — and vanishes identically on each slice.

**Working test:** *if a proposed condition can be stated slice by slice, it carries no information about reality of zeros.* Five independent derivations follow. See §8 screen 1′ for the correct statement of this test, which v1 got slightly wrong.

### 2.2 Instance A — equivariance makes isolation the conclusion

§1.2. Equivariance forces the axial form; the sphere directions are quotiented out; what remains is a problem in the half-plane `(x_0, r)` where "no off-axis zero" is verbatim hyperbolicity.

### 2.3 Instance B — the Vekua trace term *(inherited)*

For equivariant `F = A + ωB` of class `C¹` off `ℝ`, the left Cauchy–Fueter operator acts by

`𝒟F = (A_{x_0} − B_r − (2/r)B) + ω(A_r + B_{x_0})`.

The coefficient `2` is the **transverse dimension count**. Holomorphic data on a slice satisfies the *uncorrected* Cauchy–Riemann system, and subtracting gives `(2/r)B ≡ 0`, hence `B ≡ 0`, hence `F` constant:

> **No nonconstant holomorphic function admits an equivariant Fueter-regular extension.** The equivariant extension problem into `ker 𝒟` is *empty*.

*Practical use:* for any candidate class defined by a linear PDE, write the equivariant reduction and check whether the `1/r` trace term can be absorbed. Five minutes.

### 2.4 Instance C — the `σ`-type of divisor components

On the incidence quadric `Q ≅ ℂℙ¹_ζ × ℂℙ¹_w` with real structure `ρ(ζ,w) = (ζ̄, −1/w̄)`, the zero divisor of a lifted real entire function decomposes into components indexed by the zeros. Homologically nothing distinguishes the cases: two real zeros and one conjugate pair both give class `2[ruling]`. What differs is the **action of the real structure on the components** — real zeros give `σ`-invariant components, conjugate pairs give `σ`-swapped pairs. So

`RH ⟺ every component of the zero locus of \tildeΞ in Y = Q/σ is nonorientable.`

Equivalently, in the value-curve picture: real zeros are crunode-type real nodes, conjugate pairs acnode-type. The invariant is not homological and not a deformation invariant — it changes exactly when zeros collide on the axis. See §2.7(c) for why it is nevertheless unreachable.

### 2.5 Instance D — the exact deficit `r² − t²`

Let `T_0, S` be commuting real symmetric `k×k` matrices, jointly diagonalised with eigenvalues `τ_j, σ_j`; let `e ∈ ℝ³` be a unit vector with slice `Π_e`; set `t = ⟨Im q, e⟩`, `r = |Im q|`, `B_j = (x_0−τ_j)² + r² + σ_j²`. Then

`det M(q) = ∏_j (B_j − 2tσ_j)`,  `P_p(q) = ∏_j (B_j − 2rσ_j)`,

**differing only in `t` versus `r`.** Pairing conjugate roots turns each into a product over pairs of `B² − 4sσ²` with `s = t²` on the left and `r²` on the right, and

`B² − 4r²σ² = ((x_0−τ)² + (r−σ)²)((x_0−τ)² + (r+σ)²) ≥ 0`,

so every factor is positive and strictly decreasing in `s` on `[0, r²]`. Cauchy–Schwarz gives `t² ≤ r²` with equality exactly when `Im q ∥ e`, i.e. exactly on `Π_e`. Hence

> `det M(q) ≥ P_p(q)` on all of `ℍ`, with equality exactly on `Π_e ∪ {S = 0}`.

**A slice is precisely the equality locus of a Cauchy–Schwarz inequality.** A one-slice condition is therefore **blind by construction**, not merely weak.

*Verified:* formula error `~10⁻¹⁴` over 4000 random points per case; minimum deficit `+2.6×10⁻³` for `z²+1`, `+6.9×10⁻³` for `(z−1)((z+2)²+9)`, `+3.0×10⁻⁴` for the memo-5 quartic; fraction of points with positive deficit `1.000` in every non-hyperbolic case and `0.000` in hyperbolic ones. Independent exact rational check over 4000 configurations up to `k=8`: zero violations.

### 2.6 What the principle rules out

- Any condition of the form "the object restricts to `Ξ` on a slice", however the object is defined.
- Any condition imposed on a fixed complex structure.
- Any invariant computed from one 2-plane of data — including "the real axis of a second slice", since `Π_e ∩ Π_{e'} = ℝ`.

### 2.7 Instance E — the exact jet order, and the two rulings — **proved** (new in v2)

**(a) The order is exactly 2.** Write `Im q = te + n` with `n ⊥ e` and `ν = |n|` the distance to `Π_e`. Inside the family of §4.5, `Σ_{a≥1}x_aT_a = tS`, so `det M` depends on `q` only through `(x_0, t, ν²)` and `P_p` only through `(x_0, t²+ν²)`. Consequently the deficit is **even** in `ν` and **isotropic** in the transverse 2-plane, and

`det M − P_p = 4ν² · R_0 Σ_p σ_p² ∏_{q≠p}(B_{q,0}² − 4t²σ_q²) + O(ν⁴)`,

with every factor strictly positive. So:

| condition | what it forces |
|---|---|
| the slice `Π_e` itself | nothing — every real monic `p` (§4.5) |
| the **1st** infinitesimal neighbourhood | **still nothing** — there is no linear transverse term at all |
| the **2nd** infinitesimal neighbourhood | `S = 0`, i.e. `p` hyperbolic — total collapse |

**Two is the answer and there is nothing between one and two.** Searched over the full admissible data: for non-hyperbolic `p`, residuals `2.3e−15` (slice), `1.7e−12` (1st neighbourhood — still satisfiable), `4.37` (2nd — dead). The 2nd-order jet is a *stronger* constraint than a single finite off-slice point (`4.37` vs `0.44`).

**Scope — this is rigidity, not detection (corrected in v2, memo 16 §2).** The theorem never locates a zero. The chain is `2nd transverse derivative = 0 ⟹ S = 0 ⟹ T_0` real symmetric `⟹` spectrum real `⟹ p` hyperbolic, and the last three arrows are **algebra**. Local implies global here only because the family is finite-dimensional and polynomial. **One step outside it the result fails at every order at once:** the datum `T_0 = ` companion matrix of `p` (not symmetric), `T_1=T_2=T_3=0`, `λ=0`, `C = T_0²` has deficit **identically zero on all of `ℍ`** (§4.4 errata; global relative sup `10⁻¹⁴`) with `p` non-hyperbolic — so even the full global matching condition does not force hyperbolicity once block symmetry is dropped. Accordingly:

- *order 0 empty* — proved for this family (§4.5); a well-supported principle elsewhere, not a theorem;
- *order 1 empty* — proved for this family only, via **evenness** of the deficit in `ν`, which follows from `M` depending on `q` through `(x_0,t,ν²)`. A general family's deficit need not be even;
- *order 2 collapse* — proved for this family only.

**Withdrawn:** memo 9 §5's "whatever object is built from `Ξ`, the reality information must appear at transverse order `≥ 2`". The defensible version is the bulleted one above, and it must be **checked** for each new family rather than assumed. (Parts (b) and (c) below are unaffected: (b) is a coordinate identity, (c) is a statement about `ρ` alone.)

**(b) The Hessian is the Fubini–Study metric.** In `twistor_lift` coordinates (`η(w) = (w+j)^{-1}i(w+j)`, `q = x + y·η(w)`, `ζ = x+iy`), a slice `Π_e` is the **Ruling-B line** `{w = w_0}` of `Q`, whose normal direction is one *complex* dimension, and

`ν² = r² − t² = y² sin²θ = 4y² · g_FS(dw,dw) + O(|dw|⁴)`.

So the transverse Hessian is a positive **Hermitian** form on the normal bundle of a Ruling-B line. The rank-2 isotropy is the `U(1)`-invariance of the round metric on the sphere of complex structures — and the "2" of §2.3's trace term is one complex dimension, not a coincidence.

**(c) No slice is real, so §2.4's invariant is unreachable.** `ρ` acts **antipodally** on the `w`-sphere (`η(−1/w̄) = −η(w)`, verified to `2.3e−16`), mapping `{w = w_0}` to `{w = −1/w̄_0}` with exactly antipodal complex structure; `w_0 = −1/w̄_0` needs `|w_0|² = −1`. So:

> **No Ruling-B line is `ρ`-invariant.** Since the σ-type invariant is a statement about how `ρ` permutes **Ruling-A** components, and `ρ` moves the base line to a *disjoint* line at finite distance, **no finite-order jet along a single slice can see it, at any order.**

The order-2 collapse in (a) works by a different mechanism — the ADHM blocks are globally real by hypothesis — not because a jet detects σ-type. Two mechanisms; only one is local. Consequence: any proposal whose discriminant is the σ-type must be a two-antipodal-fibre object, not a thickened slice.

---

## 3. The rigidity / existence trade-off

> **Observed regularity.** Across the classes tried, the constraint that forces zero isolation and the constraint that destroys existence of the symmetric member are *the same constraint*. There is no intermediate regime.

Instances, with nothing in common but the ambient `ℍ`:

1. **Fueter/Vekua** (§2.3). Class rigid enough to be interesting; equivariant member does not exist at all.
2. **ADHM matching** (§4.4). Class genuinely noncommutative and carrying structural positivity; the matching condition collapses the data onto its commutative real locus, and hyperbolicity becomes the spectral theorem.
3. **Totally-real complexification** (§5). Isolation is *free* (Stein), existence and uniqueness both hold, no symmetry assumed — and then the only available symmetry hypothesis is unsatisfiable.
4. **Jets** (§2.7a). Order 1 empty, order 2 collapse. The trade-off holds at the level of jets too.
5. **Full Yang–Mills / gravity** (§7.1). In both the self-dual and full correspondences the degeneracy locus is *where the gauge-theoretic object fails to exist*: a genuine Yang–Mills field has no jumping locus on its domain. Sphere-free for a trivial reason; symmetric member not in the class. This is §2.3's situation again.

**Quantitatively** (from §2.5): one slice gives no constraint and one slice plus a single point gives total collapse, both driven by `r² − t²`, so they switch on together.

### 3.5 The trade-off, localised: positivity is the trap — **empirical** (new in v2)

v1 attributed the trade-off to "the class". It can be localised to a single hypothesis. Searching the shape `M(q) = C + |q|²I − 2Σ_a x_aT_a` over nested families (`k = 2,3`):

| `p` | `T` gen, `C` gen | `T` gen, `C` sym | `T` gen, `C` sym **PSD** | `T` **sym**, `C` sym |
|---|---|---|---|---|
| `z²−1` (hyp) | 3.6e−15 | 3.4e−15 | 3.6e−15 | 1.4e−14 |
| `z²+1` (NOT) | **1.4e−14** | **1.2e−14** | **0.618** | **0.978** |
| `z²+z+1` (NOT) | **1.3e−14** | 0.140 | **0.316** | **0.645** |
| `(z−1)((z+2)²+9)` (NOT) | **1.4e−14** | — | **1.17** | **1.83** |

> **`C ⪰ 0` alone — with the four blocks completely unconstrained — forces hyperbolicity**, with 13 orders of separation. Symmetry of the `T_a` independently forces it. Neither is necessary given the other; both are sufficient.

**The dichotomy.** In a matching-style dictionary, **structural positivity is not a resource but the trap**: a class supplying positivity automatically forces the conclusion (circularly), and a class not supplying it is contentless (every real monic `p` is realised — see §4.4's errata for the closed form). §4.2 celebrated ADHM's automatic positivity as *"exactly the feature that made this worth testing"*. It is exactly the feature that made the test fail.

This closes full Yang–Mills *because* it is a gauge theory: the action density `tr(F ∧ *F)` is precisely such a positivity. **Status: empirical**, `k = 2,3`, three non-hyperbolic targets, plateaus at `0.3–1.2` against `10⁻¹⁵` controls. A proof is the sharpest open item in the document.

---

## 4. Gauge theory: the ADHM results

### 4.1 Setup

Atiyah's quaternionic normal form for charge-`k` `SU(2)` ADHM data: `Δ(q) = [T − qI_k ; λ]`, `T ∈ ℍ^{k×k}`, `λ ∈ ℍ^{1×k}`, with the **ADHM condition** that `Δ†Δ` be real, and **regularity** that `Δ†Δ` be nonsingular for every `q` — precisely *no real jumping lines*, so the real jumping locus is `Z(det Δ†Δ) ⊂ ℍ`.

The **dictionary** under test: for monic real `p` of degree `k`, the zero set of the rotational extension of `p` is exactly the zero set of `P_p(q) := p(x_0+ir)p(x_0−ir) = ∏_m((x_0−ρ_m)² + r²)`. Both sides are canonical objects of their theories.

Why ADHM: it was the one candidate with the algebraic shape Weil's argument needs — a noncommutative algebra with a positive involution and positivity supplied structurally.

### 4.2 Proposition 2 — what reality forces — **proved** (symbolic at `k = 2,3`)

> `Δ†Δ` is real for all `q` **iff** (i) all four real blocks `T_a` are **symmetric**, and (ii) `[T_0,T_a] − ε_{abc}[T_b,T_c] + Im_a(λ†λ) = 0`, `a = 1,2,3`. And then
> `Δ†Δ = M(q) = C + |q|²I − 2Σ_{a=0}^{3} x_aT_a`, `C = Σ_a T_a² + Re(λ†λ) ⪰ 0`.

`C` is a sum of squares of symmetric matrices plus a Gram matrix: **the positivity is automatic.** (v1 read this as the reason to test ADHM. §3.5 shows it is the reason the test failed.) Note (i) makes `T` quaternionic *symmetric*, **not** quaternionic Hermitian — the distinction that matters in §4.7.

### 4.3 Proposition 3 — noncommutativity is available — **empirical (100% of samples)**

Exact rational witness at `k=2`: `T_0 = [[0,1],[1,0]]`, `T_1 = diag(1,−1)`, `T_2 = T_3 = 0`, `λ = (1, 2i)` satisfies all three ADHM equations exactly with `[T_0,T_1] ≠ 0`. Census: 120/120 exact solutions at `k = 2,3,4`, largest normalised commutator `1.453, 1.611, 1.360`. The noncommutative locus is generic.

### 4.4 Theorem 4 — matching rigidity — **proved, with errata**

> **Theorem.** Let `Δ†Δ` be real and suppose `det(Δ†Δ)(q) = P_p(q)` identically on `ℍ`, for monic real `p` of degree `k ≥ 1`. Then `λ = 0`, `T_1 = T_2 = T_3 = 0`, `T = T_0` is real symmetric, and `p = det(zI − T_0)`. In particular **`p` is hyperbolic**.

*Proof.* Restrict `q` to a slice, continue `y → iη`, set `u = x_0+η`, `v = x_0−η`; with `N = T_0 + iT_e` the identity becomes `det(uvI − uN − v\bar N + C) = p(u)p(v)`. The `u^k` coefficient gives `p(v) = det(vI − N)`. The `u^{k−1}v^{k−1}` coefficient gives `tr C = tr(N\bar N) = tr T_0² + tr T_e²` for every unit `e`. The left side is `e`-independent, so `e ↦ tr T_e²` is constant on `S²`, forcing `tr(T_aT_b) = κδ_{ab}`. But `tr C = tr T_0² + 3κ + ‖λ‖²`, so `2κ + ‖λ‖² = 0` with both terms non-negative: `κ = 0`, `λ = 0`, and `tr T_a² = 0` for real symmetric `T_a` forces `T_a = 0`. Then `C = T_0²` and `det M = ∏_j((x_0−τ_j)² + r²)` with `τ_j` real. `∎`

*Verification:* every step symbolic or numeric; an exact ideal-membership certificate at `k=2` for symbolic monic `p`; existence tracking hyperbolicity on all 12 test cases including a correct NO for the memo-5 quartic.

#### Errata to v1 (new in v2)

v1's "Independently verified, and stronger than first stated" contained three items. Two need correction.

> **The closed-form counterexample.** For the shape `M(q) = C + |q|²I − 2Σ_a x_aT_a` with `T_a, C` arbitrary real: take `T_0` = any real matrix with characteristic polynomial `p` (the companion matrix), `T_1=T_2=T_3=0`, `λ=0`, `C = T_0²`. Then `M(q) = (T_0 − x_0I)² + r²I`, so `det M = ∏_j((x_0−τ_j)² + r²) = P_p` — **for every real monic `p`, hyperbolic or not.** Verified symbolically at `k=2` for symbolic coefficients and numerically to `10⁻¹³` on the whole test set.

Walking the proof above on this datum: the trace relation, `κ = 0`, `λ = 0`, `T_{1,2,3} = 0` and `C = T_0²` **all hold**. The only step that fails is the last, *"`T_0` real symmetric, hence its eigenvalues are real."* For `p = z²+1` the datum is `T_0 = [[0,−1],[1,0]]`, `C = −I`, eigenvalues `±i`. So:

- **v1's item 2** ("the nonlinear ADHM equations are never used") is correct but under-strong: the counterexample *satisfies* them exactly. They are irrelevant, not merely unused.
- **v1's item 3** ("symmetry of the `T_a` is load-bearing in exactly one place — `κ = ‖T_1‖_F² ≥ 0`") is **wrong**. Symmetry is load-bearing in a second, decisive place: the final spectral step. Without it the entire chain including `κ` goes through and the conclusion is false.
- **v1's "positive semidefiniteness of `C` is not needed anywhere"** is true of this proof and misleading as a claim about the theorem: `C ⪰ 0` is independently sufficient with all symmetry dropped (§3.5), and on present evidence is the more robust hypothesis.

**Net reading.** Theorem 4 *is* the spectral theorem for real symmetric matrices, and the symmetry it needs comes from ADHM's reality condition specifically. It therefore does **not** transfer to a class with a different reality condition — it never closed the full-Yang–Mills direction. §3.5 is what closes that.

### 4.5 Theorem 5 — the one-slice relaxation — **proved**

> With `Δ†Δ` real, `det(Δ†Δ) = P_p` **on a single slice `Π_e`** holds iff `λ = 0`, `T_a = e_aS` (`a=1,2,3`) with `S := T_e` real symmetric, `[T_0,S] = 0`, `C = T_0² + S²`, together with invariance of the joint spectrum `{(τ_j,σ_j)}` of `(T_0,S)` under `σ ↦ −σ`; and then `p(v) = ∏_j(v − τ_j − iσ_j)`.
>
> **Every** real monic `p` of degree `k` arises. The relaxed condition has no discriminating power, and the data is forced commutative and `ℂ_e`-valued.

*Proof of the forward direction.* The trace relation holds for the single `e`. With `g_{ab} = tr(T_aT_b)` (`a,b ≥ 1`) the Frobenius Gram matrix, `g ⪰ 0`, it reads `tr g + ‖λ‖² = e^T g e ≤ λ_max(g) ≤ tr g`, forcing `λ = 0`, `rank g ≤ 1` and `e` a top eigenvector, so `g = κ ee^T`; then `‖T_a − e_aT_e‖_F² = 0`. Substituting into the ADHM equations, `[e_bS, e_cS] = 0` leaves `e_a[T_0,S] = 0`, and `|e| = 1` gives `[T_0,S] = 0`. `∎`

The `σ`-invariance is needed for sufficiency, since `[T_0,S]=0` makes the identity read `\bar p(u)p(v)`. It forces `tr S = 0`. Counterexample without it: `k=2`, `T_0 = 0`, `S = diag(1,2)`.

### 4.6 Proposition 6 — the deficit and the one-point threshold — **proved**

The formula of §2.5 lives in exactly this family. Consequences:

- **One slice plus one off-slice point forces hyperbolicity.** `p = z²+1`: best residual `0.42` with one point, `3×10⁻¹⁵` with the slice alone.
- Two non-parallel slices suffice, for the right reason: `S' = (e·e')S` forces `e' = ±e`, and `Π_{−e} = Π_e`.
- **The forcing is not uniform.** For two slices at angle `θ`, the best residual attainable by `S ≠ 0` scales as `O(θ²)`: `2.1×10⁻⁴` at `θ = 10⁻²`, `2.0×10⁻¹⁴` at `10⁻⁷`.
- **And it is infinitesimally sharp** (new in v2): the threshold is not one finite point but the *second-order jet*; see §2.7(a).

### 4.7 Proposition 7 — the spectrum places no constraint — **empirical**

Quaternionic **Hermitian** matrices have real spectrum (verified: 200 random Hermitian `3×3`, `max|Im| = 1.4×10⁻¹⁵`), but ADHM reality gives quaternionic **symmetric**, and over 150 admissible data at each of `k = 2,3,4` the fraction with a non-real right-eigenvalue class was `1.00`, median `|Im|/‖T‖` of `1.41, 1.57, 1.77`. Zero spheres are permitted freely; the class supplies no isolation, hence nothing to contradict.

### 4.8 Reading

Within the family the matching condition allows, "`p` hyperbolic" is exactly "`S = 0`", i.e. "`T_0 + iS` is **self-adjoint**". So the relaxation lands on the **Hilbert–Pólya statement**, with no new input from the geometry. And `λ = 0` in both Theorems 4 and 5 means the last row of `Δ` vanishes, so the matched data is not a *regular* ADHM datum — it sits outside the instanton moduli space proper. §3(5) records that this is structural to the correspondence rather than an ADHM artifact.

---

## 5. The totally-real complexification

This section corrects an error in the earlier work and supplies the purest instance of §3. It is unchanged from v1 and is recorded in full in `appendix_ERRATA.md`.

`ℍ` carries a 2-sphere of compatible complex structures. With `J_η(q) := qη`, if `I_0 ⊥ η` then `ℂ_{I_0}` is **maximally totally real** in `(ℍ, J_η)` — the same real 2-plane, a complex line for `J_{I_0}` and totally real for `J_η`. So restriction from `J_η`-holomorphic maps to `ℂ_{I_0}` is a **bijection** on germs: uniqueness by the identity theorem, existence by complexification. The codimension-two objection fails because `\bar∂F = 0` for `ℂ² → ℂ²` is **overdetermined**.

With `η = i`, `I_0 = j`: `q = z_1 + z_2 j`, holomorphic coordinates `(z_1, w)` with `w = \bar z_2`, and the slice `ℂ_j` is `{z_1, w` both real`} = ℝ²`. For intrinsic data with stem `G`, in `ζ_± = z_1 ± iw` the unique extension has

`Z(F) = Z(G) × Z(G)` — **always discrete.**

And independently: `ℂ²` is Stein, so **no 2-sphere can occur in the zero set of any holomorphic map `ℂ² → ℂ²`.** Isolation is free, with no symmetry assumed.

**Why it fails.** `R_u(q) = uq\bar u` is `J_η`-holomorphic iff `u ∈ ℂ_η`: the class is preserved only by the **circle** fixing `η`, whose fixed locus in `ℍ` is the slice `ℂ_η`. Imposing invariance of the zero *set*: a `U(1)`-orbit is connected, `Z(F)` is discrete, so every point of `Z(F)` must be fixed, i.e. `Z(F) ⊆ {w=0}`. But `Z(F) = Z(G)×Z(G)` has off-diagonal points with `w = (ρ−ρ')/2i ≠ 0` whenever `|Z(G)| ≥ 2`.

> **The symmetry hypothesis is unsatisfiable for any `G` of degree `≥ 2`, RH or no RH.**

The failure is not about noncommutativity or PDE trace terms — it is a dimension count between the zero set and the fixed locus of the available symmetry group. Three unrelated mechanisms, one outcome.

**A note new in v2.** The totally-real dichotomy appears twice in this document, in opposite directions: here, `ℝ² ⊂ ℂ²` being totally real makes the `\bar∂`-system *overdetermined* and hands you uniqueness for free; in §1.5, `ℝ^d ⊂ ℂ^d` being totally real means the holomorphic category cannot *see* the hyperbolic locus at all. Same fact, opposite use.

---

## 6. Inherited constraints

### 6.1 Multiplicative rigidity — **proved**

> Let `T` assign to every real entire `f` a function `Tf : ℍ → ℍ` such that `T` is a unital `ℝ`-algebra homomorphism into `ℍ`-valued functions with **pointwise** operations, `T(id)(q) = q`, and `f ↦ Tf(q)` sequentially continuous for locally uniform convergence. Then `T` is the rotational (slice) extension.

No equivariance, regularity or measurability assumed. The reason is Frobenius: for fixed `q` the image of `ev_q ∘ T` is a commutative subalgebra of `ℍ`, hence lies in a single slice.

**Consequence:** any class arising as the image of a product-preserving extension *operator* is slice regular. Kills functional-calculus constructions outright. *Novelty unchecked and plausibly standard.*

### 6.2 The linear no-go — **inherited**

Every operator in the classified family of equivariant *linear* extensions is injective in `f`, and no continuous linear functional of any of them distinguishes on-axis from off-axis zeros. Transferable form: **any discriminating functional must be nonlinear in the extension.** *Proved in the slice-regular/Fueter setting; the general claim is an extrapolation.*

### 6.3 Softness — deformation invariants fail — **inherited**

Two independent computations show natural topological invariants weight a zero sphere by exactly `2`:

- the homology class of the zero divisor on `Q`: a pair of real zeros and a conjugate pair both give `2[ruling]`;
- the Brouwer degree of `f/|f|` on a boundary sphere: local degree `m` at a real zero of multiplicity `m`, `2m` at a zero sphere. So the winding counts `r + 2s` — the complex count again.

Both are **deformation invariants**, which is why they fail: they cannot distinguish `Ξ` from a Davenport–Heilbronn-style function with implanted conjugate pairs. The `σ`-equivariant component type of §2.4 is the minimal refinement that is *not* deformation-invariant.

**Screening rule:** if the proposed invariant is deformation-invariant, it is dead on arrival.

### 6.4 "Barely true" — **demoted from a screen to an identity** (revised in v2)

Under the De Bruijn–Newman flow a conjugate pair collides on the axis and splits into two real zeros as `t` increases; `Λ ≥ 0` (Rodgers–Tao) says `Ξ` sits exactly at the closure of the sphere-free region, and Newman's conjecture `Λ = 0` is *"a quantitative version of the dictum that the Riemann hypothesis, if true, is only barely so."*

v1 listed this as a consistency requirement: every discriminating functional must be merely non-strictly positive in the limit, degrading continuously as sphere radius `→ 0`. **That is not a screen. It is an identity.** Define, for a real polynomial `p`, the DBN threshold

`Λ(p) := inf{ t : H_t` has only real zeros `}`, `H_t = exp(−t ∂²_z) p`.

Then `Λ(z² + y_0²) = y_0²/2` **exactly** (verified to 10 digits), and:

| quantity | law |
|---|---|
| `Λ(p)` for an implanted pair of radius `y_0` | `→ y_0²/2`, **universally** — measured `0.4997, 0.4999, 0.4991, 0.4998, 0.4977` across five different real backgrounds |
| Lehmer-pair lower bound on `Λ`, small-gap limit | `→ −Δ²/8` |
| §2.7(a)'s transverse Hessian `c_2` | `∝ σ_p²` |
| `min_x L_1` (§9.2) | `∝ y_0²`, constant to six digits over 2.5 decades; but `|L_1|/y_0²` varies by **five orders of magnitude** with the background |

> Every discriminant in this family is a configuration-dependent multiple of the De Bruijn–Newman distance to the boundary, `y_0²/2`. So §6.4 is satisfied *automatically* by anything of this shape, and has no screening power. What remains true and useful: a proposal claiming a **uniform** separation is wrong.

And one design constraint does survive, sharpened: `Λ = 0` means the margin for `Ξ` in the flow direction is exactly `0`, so **no strict inequality with a uniform positive margin can certify `Ξ`.** A working certificate must be an equality case, or measure a direction transverse to the heat flow.

### 6.5 Rationality — the wall, restated as a dichotomy (revised in v2)

Weil's argument needs (a) a finite-dimensional **`ℚ`**-algebra with a positive anti-involution, (b) a distinguished element with an arithmetic identity `FF† = q·1`, (c) definiteness of the trace form proved independently, by Hodge index on a `ℤ`-lattice. Finite rank is available for `ζ`; **rationality is not.**

v1 said "rationality is missing", which is answerable "no" for everything and therefore uninformative. The gravitational-instanton inventory sharpens it into a screen. Every construction to hand falls into exactly one of two classes:

| object | form varies with `Ξ`? | over `ℚ`? |
|---|---|---|
| ADE root lattice (ALE gravitational instanton) | **no** | yes |
| `−I_k` (ALF compactification) | **no** | yes |
| Hirzebruch–Jung string (toric Ricci-flat) | **no** | yes |
| `A_∞` (Anderson–Kronheimer–LeBrun, infinitely many centers) | **no** | yes |
| Beauville–Bogomolov form `q_X` | **no** | yes |
| trace form of `J^{d,n}` | yes | **no** |
| ADHM `C = ΣT_a² + Re(λ†λ)` | yes | **no** |
| §2.7's transverse Hessian `c_2` | yes | **no** |

> **The rationality wall is exactly the statement that no known construction is in both classes.** Class (a) has rationality without content — entries are fixed small integers (`0, ±1, 2`) carrying no `Ξ`-dependence. Class (b) has content without rationality — entries are power sums of roots of polynomials whose coefficients are the moments `M_k = ∫Φ(u)u^k du`. Weil's argument needs *one object with both*.

**And the geometric side is worse than "rigid".** Kronheimer's ALE classification supplies a definite `ℤ`-lattice of *every* rank (`A_d` for every `d`, so the rank gap in the compact hyperkähler Hodge–Riemann tower — only `{1,7,8,23,24,27,35}` of the first 40 ranks — does **not** apply here), with `H²(X;ℤ)` literally the root lattice and intersection form `−(`Cartan matrix`)`. But the form has **zero moduli**: it is fixed by `Γ` alone, all continuous data living in the periods, and the period map `σ : Z → 𝔥` is a **linear isomorphism** (Kronheimer Prop. 4.1). The existence condition is the complement of a finite union of **codimension-3 real linear subspaces**, one per root (Prop. 2.8), i.e. *"the `α_i` do not all lie in the kernel of any one root"*. Whereas `∂H` is contained in the discriminant hypersurface, which is **irreducible of degree `2(d−1)` and never a product of linear forms** (verified for `d = 2,3,4,5`). No finite union of linear subspaces has `H` as its closure. Even the infinite-rank case (`A_∞`, with an *infinite-dimensional* moduli of metrics) keeps the form rigid.

---

## 7. Directions — all closed

### 7.1 Transform, not matching — **closed**

v1's most promising shape: rather than matching zero loci, find a **transform** carrying `Ξ`'s data to a geometric object, with reality of zeros read off as an output. The model is Fueter's theorem, and the concrete candidate was the Penrose/Ward direction — a holomorphic bundle on twistor space built from `Ξ` by an integral transform, with the reality of zeros read off the `σ`-type of its jumping divisor.

**Closed, three ways.**

1. **The obstruction reading is dead in the holomorphic category** — §1.5, Corollary B. The ambitwistor ladder, now primary-sourced from Pool's Memoir 358 §V, is: order 1 unobstructed but non-unique; order 2 unobstructed and **rigid** (the order-1 ambiguity group and the order-2 obstruction group are the same group `Γ(U, End E[−1,−1])`, and Lemma V.1 says the connecting map between them is the **identity**, so exactly one first extension has vanishing second obstruction and the second is then unique); order 3 obstructed, with the obstruction *equal to the Yang–Mills current* `*J = D(*F)`. Curvature is second-order data on `L_x ≅ ℙ¹ × ℙ¹` (Theorem V.3) — the same rung and the same surface as §2.7. The gravity ladder is longer and identical in shape: 5th order ↔ Bach-flat, 6th (algebraically general) ↔ conformally Einstein. All equational, all dead.
2. **The matching reading dies on positivity** — §3.5.
3. **The degeneracy locus is where the object fails to exist** — §3(5). Pool's Theorem IV.5 requires `E|_{τ^{-1}(x)}` trivial for **every** `x ∈ U` to produce a connection; that is "no jumping over `U`".

### 7.2 Zero-divisor symmetry in a bundle setting — **closed**

v1's open question: a construction attaching to `Ξ` a holomorphic bundle on `Q` or `ℂℙ³`, **not of product type**, whose jumping divisor's `σ`-type encodes reality of zeros. Closed by §2.7(c) (σ-type is not jet-local, at any order) and §1.5 (as a global holomorphic condition, "`ζ_i` real" is not analytic — reality is not a holomorphic predicate).

### 7.3 Nonlinearity, and Hitchin's spectral curves — **closed**

v1 flagged Hitchin's monopole spectral curves as "structurally closer to what is wanted than ADHM" and untested. Now tested. The three conditions on a curve `S ∈ |O(2k)|` in mini-twistor space split exactly along this document's axis:

| condition | type | verdict |
|---|---|---|
| `σ(S) = S` | totally real linear slice — `ℝ`-linear, not holomorphic | the right shape, but imposed by hand: carries no information |
| `L²|_S` trivial | complex-analytic vanishing (a point of `Jac(S)`) | dead by §1.5 |
| `H⁰(S, L^s(k−2)) = 0` | genericity / non-vanishing | dead by §1.5 Corollary A |

### 7.4 What would count as progress

In order of value, revised:

1. **A proof of §3.5** — that `C ⪰ 0` alone forces hyperbolicity. It is the sharpest available form of the circularity diagnosis and the only unproved load-bearing claim in the document.
2. **An object passing both halves of §6.5's dichotomy** — an integral form that varies with `Ξ`'s data. Nothing in 4-manifold topology is of that kind (Donaldson's diagonalization and Witt's characterisation of root lattices both point away), and nothing in the gravitational-instanton literature. This is the wall.
3. **A property `P` of `Ξ`** (§1.3) that is analytically natural and independently provable. Positivity of `Φ` alone is insufficient — there are positive kernels whose cosine transforms have complex zeros.
4. **Negative results that close a direction cheaply**, using §8. Most of this document is of that kind, and §1.5 is the cheapest one in it.
5. **One genuine gap, not a lead.** Full Yang–Mills supplies a nonzero current `*J`, which self-dual theory lacks. "`*J = 0`" is equational and dead; an *inequality* on the current or on the action density is regional, hence outside §1.5, outside §2.7, and untested. But there is no candidate transform, §1.3 applies, and by §3.5 an inequality on a positive quantity is the shape that collapses.

---

## 8. Screening checklist

Apply in this order. Each step is minutes of work. Screens **0**, **0″** and **8′** are new in v2; **1′** and **1″** restate v1's screen 1, which was slightly wrong.

**Read the scope tags.** Screens marked **[universal]** rest on facts independent of any class or family — a proposal failing one is *refuted*. Screens marked **[heuristic]** rest on results proved only inside a specific family; they are cheap and have been right every time, but a proposal failing one is *flagged*, not refuted, and the underlying result should be re-derived for the new family. Conflating the two is the mistake memo 16 documents.

**0. Equational or regional?** *[universal]* Is the proposed condition the *vanishing* (or non-vanishing) of something, or an *inequality*? Hyperbolicity is a closed region with nonempty interior in a real parameter space. If the condition is the vanishing of a holomorphically-varying quantity — an obstruction class, a cohomology class, a determinant identity, a curvature, a triviality condition — it cannot cut out that region (§1.5). Genericity conditions fail too (Corollary A). **Stop.** *This is the cheapest screen in the list and it kills the entire holomorphic bundle-theoretic family in one line.*

**0″. Positivity audit.** *[heuristic — verified only in the ADHM shape at `k = 2,3`]* If the class supplies positivity structurally — a PSD Gram, a sum of squares, an energy or action density, a Hodge-index form — then drop *every other* condition the class imposes and ask whether that positivity alone already forces the conclusion. In the ADHM shape it does, with the blocks completely unconstrained (§3.5). If it does, the argument is circular whatever else the class contributes; and if it does not, check whether the class without positivity is contentless, which in the ADHM shape it is. **Structural positivity is the feature that recommends a class for a Weil-type argument and the feature that makes it circular. Expect both.**

**1′. Slice-statable?** *[heuristic — the 1-jet clause is proved only for the family of §4.5]* Is the condition determined by the restriction of the geometric object to a **Ruling-B line** (a slice), or by its **normal 1-jet** along one? If so it carries no information (§2, §2.7a). **Stop.** *The two qualifications matter: v1's wording would have discarded the classical Laguerre/Turán/Jensen hierarchies, which use jets along Ruling A — the stem's own derivatives — and are perfectly informative about `f`. The principle is about what the geometry adds, not about what is knowable.*

**1″. Is the invariant `ρ`-local?** *[universal]* If the discriminating invariant is the `σ`-type of divisor components, it compares a point with its `ρ`-image, which lies on the *antipodal* Ruling-B line. No finite-order jet along a single line reaches it, at any order (§2.7c). The object must be the antipodal pair, or `Q` itself with descent.

**2. Deformation-invariant?** *[universal]* If the discriminating invariant is a homology class, a degree, a charge or a divisor degree, it weights spheres by 2 and fails Davenport–Heilbronn (§6.3). **Stop.**

**3. Uniform separation claimed?** *[universal]* If the proposal claims a bounded-below discriminant, it contradicts `Λ ≥ 0` (§6.4). It is wrong. *(But do not credit a proposal for degrading correctly: by §6.4 everything in this family does, automatically.)*

**4. Multiplicative?** *[universal]* If the class is the image of a product-preserving extension operator, it is slice regular (§6.1). **Stop.**

**5. Linear functional?** *[heuristic]* If the discriminant is a continuous linear functional of the extension, it cannot separate (§6.2). Reformulate nonlinearly.

**6. Trace term.** *[heuristic]* If the class is defined by a linear PDE, write the equivariant reduction `A(x_0,r) + ωB(x_0,r)` and check whether the `1/r` transverse trace term can be absorbed. If not, the symmetric member does not exist (§2.3).

**7. Rigidity/existence.** *[heuristic]* Ask separately: does the class forbid spheres, and does the symmetric (or symmetric-zero-set) member exist? Expect these to fail together (§3). If a proposal claims both, look for the dimension count between the zero locus and the fixed locus of the available symmetry group (§5), and run screen 0″.

**8′. Rationality dichotomy.** *[heuristic]* Ask two questions of the proposed object's form: **(i) does it vary with `Ξ`'s data?** and **(ii) is it defined over `ℚ`?** Weil's argument needs both, and every construction examined answers yes to exactly one (§6.5). This does not kill a proposal but caps what it can prove — and it tells you which half is missing.

**9. Circularity.** *[universal]* Write down what the geometric hypothesis is equivalent to. If it is equivalent to hyperbolicity by a spectral theorem or by Sylvester's law, it is a restatement (§4.4, §4.8).

---

## 9. Reference data and reproduction

### 9.1 `Ξ`, its moments, and the Jensen polynomials

`Ξ(z) = 4∫_0^∞ Φ(u)cos(zu)du`, `Φ(u) = Σ_{n≥1}(2π²n⁴e^{9u/2} − 3πn²e^{5u/2})e^{−πn²e^{2u}}`.

With `M_k = ∫_0^∞ Φ(u)u^k du > 0` and `b_m = 4M_{2m}/(2m)!`, the function `H(w) = Ξ(\sqrt{−w}) = Σ_m b_m w^m` has positive coefficients and only real negative zeros iff RH. With `γ(m) = m!b_m`, the Jensen polynomials are `J^{d,n}(X) = Σ_{j=0}^d C(d,j)γ(n+j)X^j`, and **RH ⟺ every `J^{d,n}` hyperbolic** (Pólya).

Validation to reproduce: `4M_0 = 0.4971207782` against `ξ(1/2) = 0.4971207174`, relative error `1.2×10⁻⁷` (quadrature-limited), all `b_m > 0`. At 60 digits with 40 moments, `J^{d,n}` verified hyperbolic for `d ≤ 14`, `n = 0,1`, with normalised minimum root gaps `1.00, 0.49, 0.31, …, 0.062` — running **2–9% tighter** than the Hermite attractor of the same degree, consistently.

Caution: the roots span many orders of magnitude, so normalise (dividing all roots by the largest modulus is a dilation of `q` and harmless).

### 9.2 Standard test set, and the canonical instrument

**The instrument to use is `Λ(p)`** (new in v2). It is a *complete signed distance*: `Λ(p) ≤ 0` iff `p` is hyperbolic, on every case tested — where `L_1`, `P_m` and Turán are all merely necessary and can fail outright.

| `p` | `Λ(p)` | `min_x L_1` | Turán `Σρ²` |
|---|---|---|---|
| `z²−1` (hyp) | `−0.500` | `+2.00` | `+2.000` |
| `(z−1)(z−2)` (hyp) | `−0.031` | `+0.125` | `+1.250` |
| `(z²−1)(z²−4)` (hyp) | `−0.034` | `+0.531` | `+2.500` |
| `z²+1` | `+0.500` | `−2.00` | `−2.000` |
| `z²+z+1` | `+0.375` | `−1.50` | `−1.000` |
| `(z²+1)(z−1)` | `+0.369` | `−1.95` | `−1.000` |
| `(z²+1)(z²+4)` | `+0.175` | `−0.625` | `−2.500` |
| `(z−1)((z+2)²+9)` | `+0.255` | `−0.934` | `−0.692` |
| **memo-5 quartic** | `+3.88e−05` | `−4.52e−06` | **`+1.130` (PASSES)** |
| `(z²−1)(z²+100)` *(new)* | `+0.170` | **`+0.0198` (FAILS)** | `−1.980` |
| `(z²−1)(z²−4)(z²+400)` *(new)* | `+0.101` | **`+5.35e−07` (FAILS)** | `−1.975` |

**Also new in v2, and worth keeping:**

- **`L_1` is strictly stronger than Newton/first-Turán.** The memo-5 quartic `X⁴+10X³+26X²+22X+3` passes Turán (`+1.130`) and fails `L_1` (`−4.52×10⁻⁶`, which equals `f(a)²·(−2/y_0²)` exactly). Any new discriminant should now be asked to beat `L_1`, not Turán.
- **Four new shielded test cases** — a conjugate pair for which some other zero is always closer to every real point. These defeat the *pointwise* graded family `P_m(x) = Σ_ρ (x−ρ)^{−2m}` entirely (undetected to `m = 8`), while `L_n` catches them at `n = 3,5,7,8` for degrees `4,6,8,10`.
- **The Laguerre index grades by sphere radius.** With a fixed real background at `±1,±2,±3,±4` and one implanted pair of radius `y_0`, the first `n` with `L_n < 0` is monotone: `y_0 ≤ 0.5 → n=1`; `0.9 → 2`; `1.5 → 3`; `3 → 5`; `6 → 7`; `≥12 → 8`. Crossover where `y_0` passes the nearest-real-root distance. A single-index test is therefore radius-selective.
- **`L_n` completeness:** adversarial search over non-hyperbolic quartics and sextics finds no counterexample; the optimiser walks to the hyperbolic boundary (margins `9.2e−14` and `1.6e−12` at pair radii `1.1e−08`, `1.2e−05`). The binding constraint at the optimum is `n = 1`.

**Reference results.** ADHM matching (§4.4) residuals: hyperbolic `10⁻¹⁵` to `10⁻¹²`; non-hyperbolic `0.56` to `3.04`; memo-5 quartic `1.0×10⁻³`. Existence tracked hyperbolicity on all 12 cases.

### 9.3 Code inventory

| file | contents |
|---|---|
| `lab_qalg.py` | quaternionic matrix algebra over sympy |
| `lab_adhm_num.py` | fast numeric layer: ADHM residual, `C`, `det M`, `P_p`, search |
| `lab_adhm_check.py` | §4.2–4.4; noncommutativity census; 12-case existence search |
| `lab_adhm_certificate.py` | exact ideal-membership certificate for Theorem 4 at `k=2` |
| `lab_adhm_clifford.py` | the axially-symmetric-but-unmatchable Clifford ansatz |
| `lab_adhm_relax.py` | §4.5–4.7 and §2.5 |
| `lab_totally_real.py` | §5 in full |
| `Lab_Tower_Check.py` | moments, Jensen polynomials, trace forms and signatures |
| `lab_jet_order.py` | **§2.7(a)** — the jet-order theorem, symbolic and numeric |
| `lab_q_normal_form.py` | **§2.7(b,c)** — the Fubini–Study identification; `ρ` free; no real slice |
| `lab_laguerre_grade{,2,3}.py` | **§9.2** — `L_n`/`P_m`, shielded cases, radius grading, completeness search |
| `lab_obstruction_groups.py` | `h¹(Q,O(a,b))` table *(its "reading" paragraph is withdrawn — it computes the ambiguity group, not the obstruction group)* |
| `lab_holomorphic_nogo.py` | **§1.5** — corrected cohomology, and the hyperbolic-locus identity test |
| `lab_nogo_verify.py` | **§4.4 errata** — the companion-matrix counterexample; the three-family search |
| `lab_ade_rigidity.py` | **§6.5** — ADE forms, the rank comparison, discriminant irreducibility |
| `lab_dbn_distance.py` | **§6.4, §9.2** — `Λ(p)`, its `y_0²/2` anchor and universality |
| `lab_jensen_margin.py` | **§9.1** — `J^{d,n}` gaps against the Hermite attractor at 60 digits |

Dependencies: `sympy`, `mpmath`, `numpy`, `scipy`. Searches are least-squares from many random starts; the ten-to-twelve-order gap between hyperbolic and non-hyperbolic residuals is the signal, not the absolute residual.

---

## 10. Status and honesty notes

**Proved.** Proposition 1; Proposition 2 (symbolic at `k=2,3`); Theorem 4 (exact certificate at `k=2`) *with the errata of §4.4*; Theorem 5; Proposition 6's inequality; §2.7(a) the jet-order theorem; §2.7(b,c); §1.5 and its two corollaries; §5; §6.5's linearity and irreducibility statements; §6.4's `Λ(p) = y_0²/2` anchor.

**Empirical.** Proposition 3's census; Proposition 7; **§3.5** (the load-bearing one); §9.2's radius grading and `L_n` completeness.

**Inherited, not verified here.** §6.1, §6.2, §6.3's degree computation, §2.4; Csordas–Varga on `L_n ≥ 0` characterising Laguerre–Pólya; Rodgers–Tao `Λ ≥ 0`; Polymath15 `Λ ≤ 0.22`.

**Withdrawn.** `lab_obstruction_groups.py`'s reading (wrong cohomology group); v1 §4.4's items on symmetry and on `C ⪰ 0`; v1 §6.4 as a screen.

**Novelty: assume everything here is known until checked.** §1.5 is the identity theorem for holomorphic functions on a maximally totally real subspace. Theorem 4 is a rigidity result about determinantal representations by symmetric pencils — heavily worked territory. §5 is elementary several-complex-variables. §2.5 and §2.7(a) are routine axial-monogenic computations. §6.1 is Frobenius plus a character argument. §6.4's `Λ(p)` is the obvious finite-dimensional analogue. Each item needs a literature sweep before circulation, and the prior should be that it comes back known.

**Programme status.** The geometric route was closed by the author on 2026-08-23 on effort grounds. It is now closed a second time, by §1.5 — a three-line argument independent of any construction, which shows the shape of the target condition was never achievable. `PROGRAM_CLOSED.md` stands.

**One method-level criticism, added in v2, which applies even to a proposal clearing every screen in §8.** `Λ = 0` locates the difficulty in RH entirely in the `T → ∞` tail: `Ξ`'s position on the boundary of the Laguerre–Pólya class is realised by no single pair of zeros, only in the limit, and is invisible at any finite height or degree — every Jensen truncation is an *interior* point with positive margin. Every object this programme built is finite: charge-`k` ADHM data, degree-`d` truncations, rank-`r` lattices, order-`m` thickenings. **They are all structurally probing the part of the problem that is not hard.** That is not a statement about quaternions, twistors, or positivity, and it is the one criticism here that a better geometric construction would not answer.

**The single most valuable thing in this document is §8**, and within §8, screen 0. Most of the results below it are negative, each closed a direction in under a day, and the checklist is what made that possible.
