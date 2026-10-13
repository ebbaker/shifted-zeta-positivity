# Yang–Mills and RH: Project Brief

**A self-contained starting document for a fresh project.** Assumes no prior context. Everything needed to resume is here or in the small document set listed in §8.

*Assembled 2026-08-24 from memos 7–17 of the RH2 project. The inherited no-go results are summarised at high level only (§2) — they matter as constraints, not as subject matter. The ADHM and full Yang–Mills situations are given in full (§§3–4), because those are what this project is about.*

---

## 0. What this project is

**The question.** Can the Riemann Hypothesis be related to a statement about the existence of a solution to the Yang–Mills equations?

**Why this and not something else.** A predecessor project tested seven ways of encoding "all zeros of a real entire function are real" in quaternionic / twistor / gauge-theoretic language. Six are closed. The seventh — an *existence* statement about full (non-self-dual) Yang–Mills — survived, and survived for a reason rather than by oversight: the results that closed the others either apply to *equational* conditions (which existence statements are not) or were proved inside a specific finite-dimensional family (which full YM is not).

**The honest prior.** Low. §5 explains exactly where the difficulty sits, and it is a real one documented by other people's theorems. But the direction is not closed, and §6 lists three specific, cheap, well-posed questions that would settle it. Two of them nobody appears to have asked.

**One thing that makes this direction unlike its predecessors.** Full YM is the only object considered so far whose solution space is genuinely infinite-dimensional. Everything else — charge-`k` ADHM data, degree-`d` polynomial truncations, rank-`r` lattices, order-`m` thickenings — was finite, and there is a structural argument (§2.6) that finite constructions probe the part of RH that is not hard.

---

## 1. The target, stated precisely

Let `Ξ` be the Riemann `Ξ`-function: real entire, with RH equivalent to all of its zeros being real. Write `ℍ = ℝ⁴`, `q = x_0 + x_1i + x_2j + x_3k`, `Im q = q − x_0`, `r = |Im q|`, and let `𝕊 = {J ∈ ℍ : J² = −1}` be the 2-sphere of imaginary units, `ℂ_J = ℝ + Jℝ` the **slice** through `J`.

The mechanism the whole programme rests on:

> **A rotationally equivariant function on `ℍ` turns a single non-real zero into a whole 2-sphere of zeros.** If `F(uq\bar u) = uF(q)\bar u` for all unit `u`, and `F(a + bI_0) = 0` with `b ≠ 0`, then `F` vanishes on the entire sphere `a + b𝕊`.

So if one has a class `𝒞` of objects in which **no member's relevant degeneracy locus can contain a 2-sphere**, and one can attach to `Ξ` an equivariant member of `𝒞`, then RH follows.

Two structural facts fix where the difficulty must sit, and both are elementary and airtight.

**(1.1) For an equivariant object, "sphere-free" *is* hyperbolicity.** Equivariance forces the axial form `F(q) = A(x_0,r) + ω·B(x_0,r)` with `A, B` real and `ω = Im q/r`. Since `1` and `ω` are `ℝ`-independent, `F(q) = 0 ⟺ A = B = 0` — a condition on `(x_0, r)` only. So the off-axis zero set is `{A = B = 0} × 𝕊`: every off-axis zero carries its whole sphere. Hence *"no sphere in the zero set"* and *"the stem has only real zeros"* are **the same statement**, relabelled.

**(1.2) So the strategy necessarily has this shape, and only this shape:**

- `𝒞` is sphere-free — a **theorem** about `𝒞`, proved from its definition (a PDE, an energy bound, a Liouville argument);
- the object attached to `Ξ` lies in `𝒞` — to be **verified**;
- therefore RH.

**The geometry supplies the implication. It can never supply the verification.** A route is worth pursuing only if the membership condition is independently accessible, and only if the sphere-free theorem is not itself a relabelling of hyperbolicity. That is the whole test, and §§3–4 are its application to the two gauge-theoretic candidates.

*(Corollary worth keeping in mind: an equivariant object is recovered exactly from its restriction to a single slice, so "equivariant and restricts to `Ξ`" determines it **uniquely**. Freedom exists only if one weakens "restricts to `Ξ`" — which is what a **transform**, as opposed to a **matching**, would do.)*

---

## 2. Inherited constraints — the short version

Six results from the predecessor project. Full statements and proofs are in the documents of §8; here is what each one forbids, because a new proposal has to clear them.

**2.1 Equations cannot cut out hyperbolicity (the one universal no-go).** Parametrise monic real polynomials of degree `d` by coefficients `a ∈ ℂ^d`, with `ℝ^d ⊂ ℂ^d` the real ones, and let `H = {a : p_a` has all roots real`}`. Then `H` is **not a complex-analytic set**: no finite collection of holomorphic functions on a connected open `U ⊆ ℂ^d` meeting `ℝ^d` has `H ∩ U` as its common zero set. *Proof:* polynomials with `d` distinct real roots form a nonempty **open** subset of `ℝ^d`; `ℝ^d` is maximally totally real in `ℂ^d`, so a holomorphic function vanishing on an open piece of it has all Taylor coefficients zero and vanishes identically; then every point of `U` would be hyperbolic. `∎`

> **Corollary A (both parities).** `H` is also not the *complement* of an analytic set — complements are open and dense, `H` has empty interior in `ℂ^d`. So genericity and non-degeneracy conditions are excluded too.
>
> **Corollary B.** No Griffiths extension obstruction, at any order, for any holomorphically-varying family, detects hyperbolicity.

**Why, in one sentence: Yang–Mills equations are equations; hyperbolicity is a region with interior.** A holomorphic equation reaches the *boundary* of hyperbolicity (`disc(p) = 0`, where two roots collide) and never hyperbolicity itself.

**Scope, which is the reason this project exists.** This excludes *characterisations* by vanishing. It does **not** exclude: (i) **existence** statements — projections of algebraic sets, which are semialgebraic and can have interior; (ii) **inequalities**; (iii) one-way implications, though those collapse for a separate reason (an analytic subset of `ℂ^d` contained in `ℝ^d` is zero-dimensional, so it can "know" only finitely many polynomials).

**2.2 Slice-restriction carries no information.** The discriminating information in the quaternionic setting is supported on the directions transverse to any single slice. Sharpest form: in the ADHM family (§3.5) the exact deficit is `det M − P_p ≥ 0` with equality exactly on `Π_e ∪ {S = 0}`, and the discriminant is `r² − t²` where `t = ⟨Im q, e⟩` — so a slice is precisely the equality locus of a Cauchy–Schwarz inequality, and a one-slice condition is evaluated exactly where the discriminant vanishes. *Status: proved in the ADHM family; a well-supported principle (five independent instances) elsewhere, not a theorem.*

**2.3 Deformation invariants fail.** Homology class of the zero divisor and Brouwer degree both weight a 2-sphere by exactly `2` — the complex count. So they cannot distinguish `Ξ` from a Davenport–Heilbronn function with implanted conjugate pairs. **Any characteristic class, degree, charge, or Thom-polynomial count is dead on arrival.** This one bites repeatedly in §4.

**2.4 No uniform separation, and it is an identity not a screen.** Define for a real polynomial the De Bruijn–Newman threshold `Λ(p) = inf{t : e^{−t∂²}p` has only real zeros`}`. Then `Λ(z² + y_0²) = y_0²/2` exactly, and `Λ/y_0² → 1/2` **universally**, independent of the other roots. Every discriminant this programme found — the ADHM transverse Hessian (`∝ σ²`), the Laguerre margin (`∝ y_0²`), the Lehmer-pair bound (`→ −Δ²/8`) — is a configuration-dependent multiple of it. So any proposal will degrade quadratically in the sphere radius *automatically*; the only live version of the constraint is that a proposal claiming a **uniform** separation is wrong.

**2.5 Rationality, as a two-question screen.** Weil's argument needs a finite-dimensional `ℚ`-algebra with a positive anti-involution and definiteness proved on a `ℤ`-lattice. Ask of any proposed form: **(i) does it vary with `Ξ`'s data? (ii) is it defined over `ℚ`?** Every construction examined answers yes to exactly one — geometric forms (ADE root lattices, `−I_k`, Hirzebruch–Jung strings, the Beauville–Bogomolov form) are integral but rigid, carrying no `Ξ`-dependence; forms carrying `Ξ`-dependence (Jensen trace forms, the ADHM Gram) have entries built from the moments `M_k = ∫Φ(u)u^k du` and no known `ℚ`-structure. **No known object is in both classes.** This does not kill a proposal but caps what it can prove.

**2.6 The difficulty in RH is at `T → ∞`, and finite constructions miss it.** Newman's conjecture `Λ = 0`, with Rodgers–Tao's theorem `Λ ≥ 0`, places `Ξ` exactly on the boundary of the Laguerre–Pólya class. But `Ξ` has simple zeros and every Jensen truncation has *distinct* real roots — so each truncation is an **interior** point with positive margin. `Ξ` reaches the boundary by **accumulation**: the pair at height `T` has margin `≈ Δ_T²/8` with mean gap `Δ_T ≈ 4π/\log T → 0`, so the infimum is zero while every individual margin is positive. **Distance zero, realised by no single pair, invisible at any finite height or degree.** Every construction in the predecessor project was finite. This is the one criticism a better geometric construction would not answer — and the one thing full YM's infinite-dimensional solution space could.

**A warning about how to read §§2.2–2.5.** Two of the predecessor project's results had to be narrowed after a reader pushed on them, in both cases because a rigidity result proved inside *one finite-dimensional family* had been read as a *universal structural principle*. Only §2.1 and §1.1 are genuinely universal. Treat everything else as a heuristic with a good track record: failing one of those screens **flags** a proposal, it does not refute it, and the underlying result should be re-derived for whatever family is at hand.

---

## 3. ADHM in depth — the worked example, and why it failed

This is background, not the target. It matters because it is the only case where the programme carried a gauge-theoretic dictionary all the way to a theorem, and because the way it failed predicts what to check in the full-YM case.

### 3.1 Setup and the dictionary

Atiyah's quaternionic normal form for charge-`k` `SU(2)` ADHM data:

`Δ(q) = [ T − qI_k ; λ ]`, `T ∈ ℍ^{k×k}`, `λ ∈ ℍ^{1×k}`,

with the **ADHM condition** that `Δ†Δ` be real, and **regularity** — the datum is a genuine instanton — the condition that `Δ†Δ` also be nonsingular for every `q ∈ ℍ`. That second condition is precisely *no real jumping lines*, so the real jumping locus is exactly `Z(det Δ†Δ) ⊂ ℍ`.

The dictionary under test: for a monic real `p` of degree `k`, the zero set of the rotational extension of `p` (real roots as points, conjugate pairs as 2-spheres) is exactly the zero set of

`P_p(q) := p(x_0 + ir)·p(x_0 − ir) = ∏_m ((x_0 − ρ_m)² + r²)`.

Both sides are canonical objects of their theories; nothing was reverse-engineered. Why ADHM at all: it was the one candidate with the algebraic shape Weil's argument needs — a noncommutative algebra with a positive involution, with positivity supplied structurally.

### 3.2 What reality forces (proved, symbolically at `k = 2,3`)

> `Δ†Δ` is real for all `q` **iff** (i) all four real blocks `T_a` are **symmetric**, and (ii) the classical nonlinear ADHM equations hold:
> `[T_0, T_a] − ε_{abc}[T_b, T_c] + Im_a(λ†λ) = 0`, `a = 1,2,3`.
> And then
> `Δ†Δ = M(q) = C + |q|²I − 2Σ_{a=0}^{3} x_a T_a`, with `C = Σ_a T_a² + Re(λ†λ) ⪰ 0`.

`C` is a sum of squares of symmetric matrices plus a Gram matrix, so **the positivity is automatic**. That was read as the reason to test ADHM. §3.7 shows it is the reason the test failed.

Note (i) makes `T` quaternionic **symmetric** (`Tᵀ = T`), *not* quaternionic Hermitian — the distinction that matters in §3.6.

**Noncommutativity is available** (empirical, 100% of samples): exact witness at `k=2` with `T_0 = [[0,1],[1,0]]`, `T_1 = diag(1,−1)`, `λ = (1, 2i)`; census 120/120 exact solutions at `k = 2,3,4` with largest normalised commutator `1.453, 1.611, 1.360`. The noncommutative locus is generic, not a curiosity. (With `λ = 0` and `k = 2` the Plücker relation forces all commutators to vanish, so the imaginary part of the `λ`-Gram is the source of noncommutativity at low charge.)

### 3.3 Theorem A — matching rigidity (proved)

> Let `Δ†Δ` be real and suppose `det(Δ†Δ)(q) = P_p(q)` identically on `ℍ`, for a monic real `p` of degree `k ≥ 1`. Then `λ = 0`, `T_1 = T_2 = T_3 = 0`, `T = T_0` is real symmetric, and `p = det(zI − T_0)`. **In particular `p` is hyperbolic.**

*Proof.* Restrict `q` to a slice `Π_e = {x_0 + ye}`, continue `y → iη`, set `u = x_0 + η`, `v = x_0 − η`; with `N = T_0 + iT_e` and `T_e = Σ_{a≥1}e_aT_a`, the identity becomes

`det(uv·I − uN − v\bar N + C) = p(u)p(v)`.

The `u^k` coefficient gives `p(v) = det(vI − N)`, so `p` is the characteristic polynomial of `T_0 + iT_e` for every unit `e`. The `u^{k−1}v^{k−1}` coefficient of `det(uvI + uB_1 + vB_2 + B_3)` is `tr B_3 + tr B_1 tr B_2 − tr(B_1B_2)`, giving

`tr C = tr(N\bar N) = tr T_0² + tr T_e²` for every unit `e`.

The left side is `e`-independent, so `e ↦ tr T_e²` is constant on `S²`, forcing `tr(T_aT_b) = κδ_{ab}` and `tr T_e² = κ`. But `tr C = tr T_0² + 3κ + ‖λ‖²`, so `2κ + ‖λ‖² = 0` with both terms non-negative: `κ = 0`, `λ = 0`, and `tr T_a² = 0` for a real symmetric matrix forces `T_a = 0`. Then `C = T_0²` and `det M = ∏_j((x_0 − τ_j)² + r²)` with `τ_j` the eigenvalues of the real symmetric `T_0`, hence real. `∎`

*Verified:* every step symbolic or numeric; an exact ideal-membership certificate at `k = 2` for symbolic monic `p`; and existence tracking hyperbolicity on all 12 test cases (§7), including a correct NO for the near-miss quartic.

Three features of the proof, all of which matter later: it uses only the **linear** part of the reality condition (block symmetry) — not the nonlinear ADHM equations, and not `C ⪰ 0`; summing over `e = i,j,k` suffices, so three slices rather than the sphere; and `k ≥ 2` is not needed.

### 3.4 Theorem A's errata — and this is the important part

The theorem is correct. Its **interpretation** was wrong in a way that matters directly for full YM.

> **Counterexample once symmetry is dropped (exact).** For the shape `M(q) = C + |q|²I − 2Σ_a x_aT_a` with `T_a, C` arbitrary real: take `T_0` = **any** real matrix with characteristic polynomial `p` (the companion matrix will do), `T_1 = T_2 = T_3 = 0`, `λ = 0`, `C = T_0²`. Then
> `M(q) = T_0² − 2x_0T_0 + (x_0² + r²)I = (T_0 − x_0I)² + r²I`,
> so `det M = ∏_j((x_0 − τ_j)² + r²) = P_p` — **for every real monic `p`, hyperbolic or not.**

Verified symbolically at `k = 2` for symbolic coefficients (`det M − P_p → 0`) and numerically to `10⁻¹³` across the test set. Walking the proof of §3.3 on this datum: the trace relation holds (`−2 = −2 + 0` for `p = z²+1`), `κ = 0` holds, `λ = 0` holds, `T_{1,2,3} = 0` holds, `C = T_0²` holds exactly — and **the only step that fails is the last one, "`T_0` real symmetric, hence its eigenvalues are real."** For `p = z²+1` the datum is `T_0 = [[0,−1],[1,0]]`, `C = −I`, eigenvalues `±i`. The counterexample even satisfies the nonlinear ADHM equations exactly (they are vacuous when `T_{1,2,3} = 0`, `λ = 0`).

**Three consequences.**

1. **Theorem A is the spectral theorem for real symmetric matrices and nothing else**, and the symmetry it needs comes from ADHM's reality condition specifically. So it **does not transfer to a class with a different reality condition** — it never closed the full-YM direction.
2. The nonlinear ADHM equations are not merely unused in the proof; they are **irrelevant**. The entire content is the linear part.
3. `C ⪰ 0` is not inert. See §3.7.

### 3.5 Theorem B — the one-slice relaxation, and the exact deficit (proved)

> With `Δ†Δ` real, the relaxed condition `det(Δ†Δ) = P_p` **on a single slice `Π_e`** holds iff
> `λ = 0`, `T_a = e_aS` (`a = 1,2,3`) with `S := T_e` real symmetric, `[T_0, S] = 0`, `C = T_0² + S²`,
> together with invariance of the joint spectrum `{(τ_j, σ_j)}` of `(T_0, S)` under `σ ↦ −σ`; and then `p(v) = ∏_j(v − τ_j − iσ_j)`.
>
> **Every** real monic `p` of degree `k` arises. The relaxed condition has no discriminating power, and the data is forced commutative and `ℂ_e`-valued.

*Forward direction.* The trace relation holds for the single `e`. With `g_{ab} = tr(T_aT_b)` (`a,b ≥ 1`) the Frobenius Gram matrix, `g ⪰ 0`, it reads `tr g + ‖λ‖² = eᵀge ≤ λ_max(g) ≤ tr g`, forcing `λ = 0`, `rank g ≤ 1`, and `e` a top eigenvector, so `g = κ·eeᵀ`; then `‖T_a − e_aT_e‖_F² = 0`. Substituting into the ADHM equations, `[e_bS, e_cS] = 0` leaves `e_a[T_0,S] = 0`, and `|e| = 1` gives `[T_0,S] = 0`. `∎`

**And the exact deficit formula, which is the most quotable thing in the ADHM work.** Inside this family, diagonalise `(T_0, S)` jointly with eigenvalues `τ_j, σ_j`, and set `t = ⟨Im q, e⟩`, `r = |Im q|`, `B_j = (x_0 − τ_j)² + r² + σ_j²`. Then

`det M(q) = ∏_j (B_j − 2tσ_j)`,  `P_p(q) = ∏_j (B_j − 2rσ_j)`,

**differing only in `t` versus `r`.** Pairing conjugate roots turns each into a product over pairs of `B² − 4sσ²` with `s = t²` on the left and `r²` on the right, and `B² − 4r²σ² = ((x_0−τ)² + (r−σ)²)((x_0−τ)² + (r+σ)²) ≥ 0`, so every factor is positive and strictly decreasing in `s` on `[0, r²]`. Cauchy–Schwarz gives `t² ≤ r²` with equality exactly when `Im q ∥ e`. Hence

> `det M(q) ≥ P_p(q)` on all of `ℍ`, with equality exactly on `Π_e ∪ {S = 0}`.

So the discriminant is `r² − t²`, weighted by the imaginary parts of the roots — supported entirely on the transverse sphere directions, vanishing identically on the slice. **A slice is the equality locus of a Cauchy–Schwarz inequality, so a one-slice condition is blind by construction.**

*Verified:* formula error `~10⁻¹⁴` over 4000 random points of `ℍ` per case; minimum deficit `+2.6e−03` for `z²+1`, `+6.9e−03` for `(z−1)((z+2)²+9)`, `+3.0e−04` for the near-miss quartic; fraction of points with positive deficit `1.000` in every non-hyperbolic case and `0.000` in hyperbolic ones. Independent exact rational check over 4000 configurations up to `k = 8`: zero violations.

**Thresholds.** One slice plus one *finite* off-slice point already forces `S = 0` (best residual `0.42` versus `3×10⁻¹⁵` for the slice alone). Two non-parallel slices suffice but are far from minimal. The forcing is **not uniform**: for two slices at angle `θ`, the best residual attainable by `S ≠ 0` data scales as `O(θ²)` — measured `2.1e−04` at `θ = 10⁻²`, `2.0e−14` at `10⁻⁷`.

**And the threshold is infinitesimally sharp.** The deficit depends on `q` only through `(x_0, t, ν²)` where `ν` is the distance to the slice, so it is **even** in `ν` with no constant term, and

`det M − P_p = 4ν² · R_0 Σ_p σ_p² ∏_{q≠p}(B_{q,0}² − 4t²σ_q²) + O(ν⁴)`

with every factor strictly positive. So order 0 empty, order 1 empty (*by evenness* — there is no linear transverse term at all), order 2 collapse. **Scope caveat, and it is important:** this is a **rigidity** statement about a finite-dimensional polynomial family, not a claim that infinitesimal data detects zeros. The chain is `2`-jet `= 0 ⟹ S = 0 ⟹ T_0` symmetric `⟹` real spectrum `⟹` hyperbolic, and the last three steps are algebra. And one step outside the family it fails at every order at once: §3.4's datum has deficit **identically zero on all of `ℍ`** with `p` non-hyperbolic.

### 3.6 The spectrum places no constraint (empirical)

The most faithful reading of the original programme is that zero-sphere structure is *native* to quaternionic linear algebra: right-eigenvalue classes of a quaternionic matrix are 2-spheres unless real. So one might hope the ADHM equations force real spectrum, with no matching condition at all.

They do not. Quaternionic **Hermitian** matrices have real spectrum (verified: 200 random Hermitian `3×3`, `max|Im| = 1.4e−15`), but ADHM reality gives quaternionic **symmetric**, and over 150 admissible data at each of `k = 2,3,4` the fraction with a non-real class was `1.00`, median `|Im|/‖T‖` of `1.41, 1.57, 1.77`. **Zero spheres are permitted freely; the class supplies no isolation, hence nothing to contradict.**

### 3.7 The positivity dichotomy — the load-bearing conjecture (empirical, unproven)

Searching the shape `M(q) = C + |q|²I − 2Σ_a x_aT_a` over nested families, `k = 2,3`:

| `p` | `T` gen, `C` gen | `T` gen, `C` sym | `T` gen, `C` sym **PSD** | `T` **sym**, `C` sym |
|---|---|---|---|---|
| `z²−1` (hyp) | 3.6e−15 | 3.4e−15 | 3.6e−15 | 1.4e−14 |
| `z²+1` (NOT) | **1.4e−14** | **1.2e−14** | **0.618** | **0.978** |
| `z²+z+1` (NOT) | **1.3e−14** | 0.140 | **0.316** | **0.645** |
| `(z−1)((z+2)²+9)` | **1.4e−14** | — | **1.17** | **1.83** |

> `C ⪰ 0` **alone** — with the four blocks completely unconstrained — forces hyperbolicity, with 13 orders of separation. Symmetry of the `T_a` independently forces it. Neither is necessary given the other; both are sufficient.

**The conjecture.** In a matching-style dictionary, **structural positivity is not a resource but the trap**: a class supplying positivity automatically forces the conclusion (circularly), and a class not supplying it is contentless (every real monic `p` is realised, by §3.4). This is the feature that recommends a class for a Weil-type argument and the feature that makes it circular.

**Status: unproven, verified only in the ADHM shape at `k = 2,3`.** This is the single most important open item for the present project, because it is what would close full YM if it generalises — and full YM does supply structural positivity (the action density). A proof, or a counterexample outside the ADHM shape, decides a lot.

### 3.8 The reading, and one defect worth remembering

Within the family the matching condition allows, "`p` hyperbolic" is exactly "`S = 0`", i.e. "`T_0 + iS` is **self-adjoint**". So the relaxation lands on the **Hilbert–Pólya statement**, with no new input from the geometry.

And `λ = 0` in both theorems means the last row of `Δ` vanishes, so the matched data is **not a regular ADHM datum** — it sits outside the instanton moduli space proper, not merely on its commutative locus. That is expected, since a nonempty jumping locus is exactly what was requested. It is also the first instance of a pattern that recurs in full YM (§4.3): **the degeneracy locus one wants to match is precisely where the gauge-theoretic object fails to exist.**

---

## 4. Full Yang–Mills in depth

### 4.1 The ambitwistor correspondence, order by order

**Setup.** Ambitwistor space `𝔸` is the space of complex null geodesics of complexified Minkowski space, realised as the quadric `Z·W = 0` inside `ℙ𝕋 × ℙ𝕋* = ℙ³ × ℙ³*`. It has complex dimension 5 and is a **hypersurface** — codimension 1 — so its conormal bundle is `N* = O(−1,−1)` (the defining section is bidegree `(1,1)`; do not import `O(−2,−2)` by analogy with a degree-2 hypersurface in `ℙ³`). For a spacetime point `x`, `L_x = τ^{-1}(x) ≅ ℙ¹ × ℙ¹`, the quadric of null rays through `x`.

**The extension theory.** For a bundle `E^{(n)}` on the `n`-th formal neighbourhood `U^{(n)}`: an extension to `U^{(n+1)}` exists **iff** the obstruction `η ∈ H²(U'', End E ⊗ (N*)^{n+1})` vanishes; and if it does, `H¹` of the same sheaf acts transitively on the set of extensions. **`H²` is the obstruction group and `H¹` is the ambiguity group** — an easy and consequential thing to get backwards.

**The ladder** (Pool, Mem. AMS 358, §V, read directly; also Buchdahl 1985 and Eastwood 1987):

| order | obstruction `H²(U'', End E(−m,−m))` | ambiguity `H¹(…)` | verdict |
|---|---|---|---|
| 1 | `0` (Thm IV.4c) | `≅ Γ(U, End E[−1,−1])` (IV.4a) | **unobstructed, non-unique** |
| 2 | `≅ Γ(U, End E[−1,−1])` (IV.4d) | `0` (IV.4b) | **unique** |
| 3 | `≅ Γ(U, ker d)` = axial currents (IV.4e) | — | **obstruction `= *J = D(*F)`** |

And the order-2 rigidity has a sharper mechanism than "unobstructed": the order-1 ambiguity group and the order-2 obstruction group are **the same group**, and Pool's **Lemma V.1** says the connecting homomorphism between them is the **identity**. So exactly one first extension has vanishing second obstruction, and since `H¹(U'', End E(−2,−2)) = 0` that second extension is then unique. The first-order ambiguity is spent exactly cancelling the second-order obstruction; §V.3's fourteen pages of Čech bookkeeping exist to prove that one word.

**Two more statements from Pool that matter here.**

- **Theorem V.3 (the curvature).** `H¹(L_x, End E|_{L_x} ⊗ ⊙²N*_x) ≅ Ω²_M ⊗ End E|_x`, and `F(x)` is the class representing the **difference between two canonical second-order extensions** of `E|_{L_x}` — the restriction of `E` and the restriction of the trivial bundle. So **curvature is second-order data on a `ℙ¹ × ℙ¹`**, and it is a difference of extensions (an `H¹`), not an obstruction (an `H²`).
- **Theorem IV.5 (the generalized Ward correspondence).** A one-to-one correspondence between holomorphic bundles `E → U'' ⊂ 𝔸` such that `E|_{τ^{-1}(x)}` is **trivial for every `x ∈ U`**, and pairs `(E, A)` with `A` a holomorphic connection on `U`.

**For calibration**, the gravitational analogue runs further: fifth-order formal neighbourhoods ⟺ vanishing Bach tensor, sixth order (algebraically general) ⟺ conformally Einstein (LeBrun). So "which order" is a genuinely discriminating invariant in this subject, not a formality.

### 4.2 What this says about the obstruction reading

**Source-free YM *is* the third-order extension condition.** So "RH ⟺ the bundle extends to third order" is exactly the shape §2.1 excludes, by Corollary B. That part is closed, universally, and it is worth being clear that it closes the *natural* reading — the one that made Witten 1978 attractive in the first place ("existence free, field equation as obstruction to extension").

**A correction worth carrying forward.** It is tempting to say full YM offers a nonzero current `*J` as an extra handle that self-dual theory lacks. It does not. The YM equations *with* current are `D_AF = 0`, `D_A(*F) = *J`; **source-free** YM has `*J = 0`; and Pool's Theorem V.4 says the third-order obstruction **is** `*J`. So a YM solution has zero current by definition — the current is the obstruction to *being* a YM field, and a connection with `*J ≠ 0` is the order-0 object, where there is no isolation of any kind.

**The genuine advantage of full YM over self-dual is therefore not an extra field.** It is simply that `{D^*F = 0} ⊋ {F = *F}`, and the former is much bigger. Which brings us to the thing this project is actually about.

### 4.3 The freedom — real, and the one thing that answers §2.6

**Determined versus overdetermined.** After Coulomb gauge-fixing (`d^*A = 0`), the system `d_A^*F_A = 0` is a **determined** second-order quasilinear elliptic system for `A`, so local solutions on a domain `Ω ⊂ ℝ⁴` are parametrised by boundary data — an infinite-dimensional family. The ASD equations are **overdetermined** (first order, 3 equations for 4 unknowns modulo gauge), which gives finite-dimensional moduli: `8k − 3` for charge-`k` `SU(2)` on `S⁴`.

> **This asymmetry is the structural reason there is no "`8k − 3`" for full Yang–Mills, and it is the only place in the whole programme that answers §2.6's criticism.** Every other object considered was finite; this one is not.

*(Status: folklore. The ellipticity contrast is solid; I found no citable theorem for the infinite-dimensionality statement, and confirming or refuting it is one of the cheap tasks in §6.)*

**Non-self-dual solutions exist, abundantly.** Yau's Problem 117 — that every YM field on `S⁴` is `(anti-)self-dual` — is **false**:

- **Sibner–Sibner–Uhlenbeck** (PNAS **86** (1989) 8610): infinitely many finite-action non-minimal critical points on `S⁴`, by min–max over a topologically nontrivial loop of connections, via the correspondence between `SU(2)`-invariant instantons on `S⁴` and monopoles on hyperbolic `ℋ³`.
- **Bor** (CMP **145** (1992) 393): existence proved by minimising YM *within* a symmetric class, plus a proof that the linearised self-duality equation admits no solution with those symmetries.
- **Sadun–Segert** (Bull. AMS **24** (1991) 163, Thm 1 and Cor. 2): a non-self-dual `SU(2)` YM connection on **every** bundle over `S⁴` with `c₂ ≠ ±1`.
- **Parker** (Duke **66** (1992), Cor. 5.2): the same by equivariant Morse theory.
- **Sadun** (CMP **163** (1994) 257): a two-real-parameter family, with index `= rt`, nullity `= 12` independent of `(r,t)`, and fractional Chern number `c₂ = (r² − t²)/8`.

Also relevant: `ℝ⁴` and `S⁴` are the same problem for finite energy — YM is conformally invariant in dimension 4 and Uhlenbeck's removable-singularity theorem extends a finite-energy YM field across the point at infinity.

### 4.4 The cost — and it is documented by other people's theorems

The programme needs **isolation as a theorem about the class** (§1.2). Here is what the subject supplies.

> **Every rigidity theorem in Yang–Mills theory has the form "small ⟹ (anti-)self-dual, or flat".** Bourguignon–Lawson–Simons, Bourguignon–Lawson, Min-Oo, Dodziuk–Min-Oo, Gerhardt, Nakajima, Feehan I, Feehan II, Feehan's discreteness theorem, Gursky–Kelleher–Streets, Vieira. **Not one isolates a non-self-dual solution.**

The key statements:

- **Bourguignon–Lawson (CMP 79 (1981) 189).** Any **weakly stable** YM field on `S⁴` with `G = SU(2), SU(3)` or `U(2)` is self-dual or anti-self-dual. Pointwise version (Thm D): `‖F_A⁺‖_{L^∞(S⁴)} < √3 ⟹ A` is ASD.
- **Gursky–Kelleher–Streets (CMP 361 (2018)) — the sharp explicit gap.** On the round `S⁴` with `G ⊂ SO(E)`, any YM connection with `F⁺ ≢ 0` satisfies
> `∫|F|² ≥ 8π²|κ| + 16π²`
  — at least **two charge-one instanton actions** above the Bogomolny minimum. Restated as `δ = 2` by Dayaprema–Waldron, who upgrade it to a flow statement (the YM flow retracts `{𝒴ℳ < 4π²(|κ|+2)}` onto the instanton moduli space) and note it is **consistent with all known examples**.
- **Feehan (discreteness).** On a closed oriented 4-manifold with any smooth metric, the set of critical values of the YM energy is **closed and discrete**, and there is `ε > 0` with `‖F_A^{+}‖_{L²} < ε ⟹` ASD. General but non-explicit.
- **Taubes (CMP 91 (1983) 235).** Morse index `i ≥ 2(|κ| + 1)` at a non-minimal YM connection. **No non-minimal YM connection on `S⁴` is a local minimum.**
- **Gursky–Kelleher–Streets (CMP 376 (2020)).** `i(∇) + ν(∇)` is bounded **above** by a linear function of the energy — and **below** likewise on Sadun's family. The non-self-dual sector becomes *more* unstable with energy.

**Three quantitative aggravations.**

1. **The gap is additive, not multiplicative.** `16π²` regardless of charge, so the relative gap `2/|κ| → 0`. The theorems isolate the ASD **stratum** and get no stronger where the freedom is.
2. **Non-self-dual solutions are not isolated from each other.** Sadun's is a continuous two-parameter family.
3. **They are deep saddles, increasingly so.** Index `= rt` grows without bound with `index/|c₂| = O(1)`.

**And the decisive item.** In Sadun's family — the standard construction of non-self-dual YM fields on `S⁴` — the solutions are parametrised partly by the **holonomy around a 2-sphere** `S₊ ⊂ S⁴`, a singular orbit of the `SO(3)` action, and the family includes connections with a holonomy singularity along exactly that 2-sphere (classification: Sibner–Sibner, CMP 1992).

> The programme needs "**no 2-sphere in the degeneracy locus**" as a theorem about the class. In the very sector where full Yang–Mills has its freedom, a 2-sphere is the **standard** degeneracy locus rather than a forbidden one.

### 4.5 No positivity in the holomorphic setting, and stability is dead

The ambitwistor correspondence is an equations-only correspondence — no action functional is part of it. When an action *is* written on ambitwistor space, it is indefinite: Mason–Skinner's `S[A,G] = ∫tr(F∧G − (ε/2)G∧*G)` is a Chalmers–Siegel first-order action with an auxiliary field, built for BCFW recursion, with **no Bogomolny bound and no energy**. And in split signature LeBrun–Mason record that solutions are *generically non-analytic or only finitely differentiable* — regularity is lost, and there is no removable-singularity theorem and no gap theorem.

The one inequality-shaped condition native to the holomorphic category is **slope stability** (Hitchin–Kobayashi / Donaldson–Uhlenbeck–Yau): `μ(F) < μ(E)` for all subsheaves. It survives §2.1's Theorem — but **not Corollary A**: stability is an *open* condition in holomorphic families, so `{a : E_a` stable`}` has nonempty interior in `ℂ^d`, while `H` has **empty** interior there. **Excluded on parity grounds.**

> **The dichotomy: the holomorphic setting has the freedom but no positivity; the real/Euclidean setting has the positivity but its theorems all conclude self-duality.**

### 4.6 Screening the candidate degeneracy loci — and the dimension ladder

| candidate | verdict |
|---|---|
| real **jumping locus** | **empty** over the domain, by Theorem IV.5 — the correspondence *requires* triviality on every `L_x` to produce a connection. Asking for a nonempty one is asking for the object not to be a YM field. (Same defect as ADHM's `λ = 0`, §3.8.) |
| the **current** `*J` | zero for any YM solution (§4.2). |
| `{F⁻ = 0}` | `F⁻` is a section of `Λ²₋ ⊗ 𝔤`, rank `3·dim𝔤 = 9` for `SU(2)`; generic zero set has codimension `9 > 4`, i.e. **empty**. |
| `{F = 0}` | rank 18. Empty. |
| **rank-drop loci of `F⁻`** | see the ladder below; and their classes are Thom polynomials in characteristic classes (Fehér–Némethi–Rimányi), hence deformation invariants, hence §2.3. |
| **slope stability** | dead by Corollary A (§4.5). |
| the **gap used as a criterion** | `∫|F|² < 8π²|κ| + 16π² ⟹ F⁺ ≡ 0 ⟹` ASD `⟹` back inside ADHM, where §3.3 already gives hyperbolicity from the matching alone. The energy hypothesis is redundant; the loop closes. |

**The dimension ladder.** The zero set of the rotational extension of `Ξ` is a union of **2-spheres** (one per conjugate pair) and **points** (one per real zero). Any locus proposed to match it must be able to be 2-dimensional. For `F⁻` a `3 × d` matrix of functions (`d = dim 𝔤`), the rank loci have codimension `(3−r)(d−r)`:

| `G` | `d` | `rank ≤ 0` | `rank ≤ 1` | `rank ≤ 2` |
|---|---|---|---|---|
| `SU(2)`, `SO(3)` | 3 | 9 → empty | 4 → **points** | 1 → **hypersurface** |
| `U(2)` | 4 | 12 → empty | 6 → empty | **2 → 2-dimensional** |
| `SU(3)` | 8 | 24 → empty | 14 → empty | 6 → empty |
| `SO(4)` | 6 | 18 → empty | 10 → empty | 4 → points |

> For `SU(2)` — the case the whole programme has used — **no curvature rank locus is ever 2-dimensional.** They are empty, points, or a hypersurface. So no such locus can *be* a union of 2-spheres, before any analysis. And both non-empty ones are dead anyway: the 0-dimensional one is a characteristic number (§2.3), the hypersurface can contain spheres so supplies no isolation.

**`U(2)` is the single exception:** `dim 𝔲(2) = 4`, so `{rank F⁻ ≤ 2}` has codimension `(3−2)(4−2) = 2` — a genuinely **2-dimensional** canonical locus, which *can* be a union of 2-spheres. And `U(2)` is inside Bourguignon–Lawson's stability hypothesis.

*Caveat.* These are **generic** codimensions. For a particular YM field a locus can be larger than generic. So the ladder **excludes matching by dimension** but does **not** supply an isolation theorem, which would need the reverse: a proof that the locus can never be 2-dimensional for *any* member of the class.

---

## 5. Where the difficulty sits

Stated once, as clearly as possible, because it is what the project has to beat.

> **Full Yang–Mills buys existence at exactly the cost of isolation.** The freedom is real — determined rather than overdetermined ellipticity, infinite-dimensional local solution space, and the only answer in the programme to §2.6's finiteness criticism. The cost is that every isolation theorem in the subject concludes self-duality, so the analytic tools live exactly and only in a neighbourhood of the stratum where the freedom isn't. And in the non-self-dual sector, 2-spheres are where the known solutions live rather than something forbidden.

This is the same rigidity/existence trade-off that closed every earlier direction. What is different is that here it is instantiated by an **external literature** at the level of a whole PDE theory, rather than by our own matrix computations inside one finite-dimensional family.

**But it is a structural obstacle, not a theorem.** "No isolation theorem exists" is a statement about the literature, not about mathematics. Nobody appears to have asked the question in §6.1. That is the gap this project is aimed at.

---

## 6. The open questions, ranked

### 6.1 The gate (a genuinely new question)

> **Is there a canonical locus of a source-free Yang–Mills field on `ℝ⁴` whose topology is constrained — in particular, one that provably cannot contain a 2-sphere component?**

A literature search found nothing: no structure theorem, no dimension bound, no topological constraint on `{F⁻ = 0}`, on the rank loci beyond their characteristic classes, or on any other canonical subvariety of a YM field. This is the decision point for the whole project.

### 6.2 Three tractable sub-questions, cheapest first

1. **Unique continuation for `F⁻`.** Does `F⁻ = 0` on an open set imply `F⁻ ≡ 0` for a source-free YM connection? Not stated either way in anything found. For real-analytic metrics YM connections are real-analytic in a suitable gauge, so `{F⁻ = 0}` is a *real*-analytic subvariety — which bounds its dimension but gives no topological constraint. A day's work, and it is the gate to any of the loci being well-behaved.
2. **The `U(2)` slot.** Compute `{rank F⁻ ≤ 2}` for Sadun's family, or for a `U(2)` equivariant ansatz. Is it ever a 2-sphere? If it is, the direction closes by the same mechanism as everything else. If it provably never is, that is the isolation theorem and it unlocks the direction. **This is the highest-value item.**
3. **The energies of the known non-self-dual solutions.** Nobody has published a numerical action for *any* SSU / Sadun–Segert / Bor / Parker solution; Dayaprema–Waldron's "consistent with the known examples" is an assertion without numbers. Sadun's reduced ODE system is explicit and integrable numerically. Recovering one action value would test the sharp GKS bound directly and is entirely self-contained.

### 6.3 The item that would settle a lot either way

**Prove or refute §3.7** — that `C ⪰ 0` alone forces hyperbolicity. If it generalises beyond the ADHM shape, full YM closes too, since the YM action density is exactly such a positivity. If it fails outside that shape, the matching reading of full YM reopens. Either outcome is worth having, and this is a self-contained algebra problem.

### 6.4 Two things to check before trusting the framing

- **The infinite-dimensionality of the local YM solution space** (§4.3) is folklore here. Confirm with a citable theorem or refute.
- **Gursky–Kelleher–Streets Corollary 1.2's displayed constant** was reconstructed from their normalisation and independently corroborated by Dayaprema–Waldron's `δ = 2`, but not read off the PDF. Verify before quoting.

---

## 7. Instruments and the test set

Any proposed discriminant must be run against these. Established over the predecessor project; the first two items are the ones to use.

**`Λ(p)`, the De Bruijn–Newman threshold — the canonical instrument.** `Λ(p) = inf{t : e^{−t∂²}p` has only real zeros`}`, computable in closed form. It is a **complete signed distance**: `Λ(p) ≤ 0` iff `p` is hyperbolic, on every case tested. `Λ(z² + y_0²) = y_0²/2` exactly.

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
| **the near-miss quartic** `X⁴+10X³+26X²+22X+3` | `+3.88e−05` | `−4.52e−06` | **`+1.130` (PASSES)** |
| `(z²−1)(z²+100)` *shielded* | `+0.170` | **`+0.0198` (FAILS)** | `−1.980` |
| `(z²−1)(z²−4)(z²+400)` *shielded* | `+0.101` | **`+5.35e−07` (FAILS)** | `−1.975` |

**The near-miss quartic is the single most useful test.** Roots (normalised) `−1`, `−0.254256 ± 0.008822i`, `−0.025679`. It is barely non-hyperbolic and it **passes** the Newton/first-Turán test, so any discriminant that accepts it is at most as strong as Turán, which is a theorem for `Ξ` and provably strictly weaker than hyperbolicity.

**The two shielded cases are the second most useful.** A conjugate pair for which some other zero is always closer to every real point. They defeat the pointwise graded family `Σ_ρ(x−ρ)^{−2m}` entirely and defeat `L_1`, while `Λ` catches them.

**`Ξ` itself.** `Ξ(z) = 4∫_0^∞ Φ(u)cos(zu)du` with `Φ(u) = Σ_{n≥1}(2π²n⁴e^{9u/2} − 3πn²e^{5u/2})e^{−πn²e^{2u}}`. With `M_k = ∫_0^∞ Φ(u)u^k du > 0`, `b_m = 4M_{2m}/(2m)!` and `γ(m) = m!b_m`, the Jensen polynomials `J^{d,n}(X) = Σ_j C(d,j)γ(n+j)X^j` satisfy **RH ⟺ every `J^{d,n}` hyperbolic** (Pólya). Validation to reproduce: `4M_0 = 0.4971207782` against `ξ(1/2) = 0.4971207174`, relative error `1.2e−07`, all `b_m > 0`. At 60 digits with 40 moments, `J^{d,n}` verified hyperbolic for `d ≤ 14`, `n = 0,1`. Normalise roots (dividing by the largest modulus is a harmless dilation).

---

## 8. Documents to include in the new project

Tiered. The essential set is small enough to read in an afternoon.

### Essential — carry these over

| document | why |
|---|---|
| **`PROJECT_YM_BRIEF.md`** (this file) | the entry point |
| `memo7_adhm_test.md` | ADHM Theorem A in full, with the noncommutativity census and the 12-case search |
| `memo8_slice_relaxation.md` | ADHM Theorem B, the deficit formula, the slice ladder |
| `memo12_nogo_verification.md` | **the ADHM errata** — the companion-matrix counterexample and the positivity dichotomy. Do not read memo 7 without this. |
| `memo17_full_ym.md` | the full-YM assessment this brief summarises |
| `memo14_what_is_proved.md` | the theorem audit: what is proved, empirical, inherited, withdrawn |
| `memo16_scope_corrections.md` | **which results are universal and which are family-specific.** Read before trusting any screen. |
| `lab_qalg.py`, `lab_adhm_num.py` | quaternionic algebra and the numeric layer everything else imports |
| `lab_adhm_check.py`, `lab_adhm_relax.py` | the ADHM derivations and the slice ladder |
| `lab_nogo_verify.py` | the counterexample and the three-family search |
| `lab_ym_landscape.py` | the freedom/isolation tables and the dimension ladder |
| `lab_dbn_distance.py` | `Λ(p)`, the canonical instrument |
| `Lab_Tower_Check.py` | moments and Jensen polynomials — needed for any test against `Ξ` |
| `MEMO_65_358.E.pdf` | Pool's Memoir. The primary source for §4.1 and the only one read directly. |

### Useful — include if convenient

`BRIEF_transverse_rigidity_v2.md` (the full inherited picture, including the screening checklist with universal/heuristic tags); `memo11_holomorphic_nogo.md` (the one universal no-go, stated and proved); `memo15_boundary.md` (the `Λ = 0` analysis behind §2.6); `memo9_jet_order.md` + `lab_jet_order.py` (the jet-order theorem, with its scope correction appended); `twistor_lift_computation.md` (the incidence quadric `ℙ¹ × ℙ¹` coordinates and the σ-type invariant — relevant background since Pool's `L_x` is the same surface).

### Leave behind

`memo10_order_ladder.md` (superseded by memo 11 and memo 17); `memo13_gravity.md` and everything gravitational (`lab_ade_rigidity.py`, `Kronheimer.pdf`, `LeBrun.pdf`, `Nakajima.pdf`, `BF01228345.pdf`) — that direction is closed and the user's own judgement was that it is too complicated to be worth it; `lab_totally_real.py`, `lab_laguerre_grade*.py`, `lab_obstruction_groups.py`, `lab_holomorphic_nogo.py`, `lab_q_normal_form.py`, `lab_ade_rigidity.py`, `lab_jensen_margin.py`, `lab_equivariance_freedom.py`, `lab_jet_scope.py`, `appendix_*` — all closed directions or one-off verifications, summarised where they matter.

---

## 9. References

Marked **[free]** where a legitimate full text was reachable, **[paywalled]** otherwise. The paywalled ones you may want to add are flagged **★** by priority.

### 9.1 The ambitwistor correspondence — the core of §4.1

- **★★★ R. Pool, *Yang–Mills fields and extension theory*, Mem. Amer. Math. Soc. **358** (1987), 63 pp.** — *already in the project.* The primary source for the order-by-order ladder, Lemma V.1, Theorems IV.5, V.2, V.3, V.4.
- N. P. Buchdahl, *Analysis on analytic spaces and non-self-dual Yang–Mills fields*, Trans. Amer. Math. Soc. **288** (1985) 431–469. **[free, ams.org]** Griffiths obstruction machinery; "current = obstruction to third order".
- M. G. Eastwood, *Supersymmetry, twistors, and the Yang–Mills equations*, Trans. Amer. Math. Soc. **301** (1987) 615–635. **[free, ams.org]** The abelian ladder cohomologically; the `𝒩 ↔` order dictionary.
- **★★ E. Witten, *An interpretation of classical Yang–Mills theory*, Phys. Lett. B **77** (1978) 394–398.** **[paywalled]** The origin. Note his abstract's "second-order Yang-Mills field equations" means the PDE order, not a neighbourhood order.
- **★★ J. Isenberg, P. B. Yasskin, P. S. Green, *Non-self-dual gauge fields*, Phys. Lett. B **78** (1978) 462–464.** **[paywalled]** The independent discovery; "reality and currentless conditions".
- L. Mason, D. Skinner, *An ambitwistor Yang–Mills Lagrangian*, hep-th/0510262. **[free]** The indefinite action; the `(Z·W)^{-4}` measure.
- M. Atiyah, M. Dunajski, L. J. Mason, *Twistor theory at fifty*, Proc. R. Soc. A **473** (2017) 20170530, arXiv:1704.07464. **[free]** The best modern survey; the gravity ladder.
- **★ Yu. I. Manin, *Gauge Field Theory and Complex Geometry*, Grundlehren **289**, Springer (2nd ed. 1997).** **[paywalled]** Ch. 2 is the Radon–Penrose transform; the invariant form of the obstruction theory.
- **★ R. S. Ward, R. O. Wells Jr., *Twistor Geometry and Field Theory*, CUP (1990), Ch. 10.** **[paywalled]** The standard textbook account.

### 9.2 Non-self-dual Yang–Mills solutions — the premise of §4.3

- **★★★ L. Sadun, *A symmetric family of Yang–Mills fields*, Comm. Math. Phys. **163** (1994) 257–291.** **[paywalled]** **The single most important reference for this project.** The two-parameter family; index `= rt`, nullity `= 12`; `c₂ = (r²−t²)/8`; and the **holonomy around the 2-sphere `S₊`** which is §4.4's decisive point.
- **★★★ L. M. Sibner, R. J. Sibner, *Classification of singular Sobolev connections by their holonomy*, Comm. Math. Phys. (1992).** **[paywalled]** The classification of the 2-sphere holonomy singularities.
- L. Sadun, J. Segert, *Non-self-dual Yang–Mills connections with nonzero Chern number*, Bull. Amer. Math. Soc. **24** (1991) 163–170. **[free, ams.org]** Theorem 1 and Corollary 2.
- **★★ L. Sadun, J. Segert, *Non-self-dual Yang–Mills connections with quadrupole symmetry*, Comm. Math. Phys. **145** (1992) 363–391.** **[paywalled]**
- **★★ L. M. Sibner, R. J. Sibner, K. Uhlenbeck, *Solutions to Yang–Mills equations that are not self-dual*, Proc. Natl. Acad. Sci. USA **86** (1989) 8610–8613.** **[nominally free but blocked; ★ if you can get it]** The first construction.
- **★★ G. Bor, *Yang–Mills fields which are not self-dual*, Comm. Math. Phys. **145** (1992) 393–410.** **[paywalled]**
- T. H. Parker, *A Morse theory for equivariant Yang–Mills*, Duke Math. J. **66** (1992) 337–356. **[free, users.math.msu.edu]** Condition C; Cor. 5.2.
- G. Bor, R. Montgomery, *SO(3) invariant Yang–Mills fields which are not self-dual*, preprint (1989). **[free, cimat.mx]** The cohomogeneity-one ansatz and the reduced ODEs — the concrete starting point for §6.2(3).

### 9.3 Energy gaps and stability — the obstacle of §4.4

- **★★★ M. Gursky, C. L. Kelleher, J. Streets, *A conformally invariant gap theorem in Yang–Mills theory*, Comm. Math. Phys. **361** (2018), arXiv:1708.01157.** **[free]** The sharp explicit gap. Verify Corollary 1.2's displayed constant directly.
- A. Dayaprema, A. Waldron, *Parabolic gap theorems for the Yang–Mills energy*, arXiv:2412.21050. **[free]** The `δ = 2` restatement and the flow retraction.
- J.-P. Bourguignon, H. B. Lawson Jr., *Stability and isolation phenomena for Yang–Mills fields*, Comm. Math. Phys. **79** (1981) 189–230. **[free, projecteuclid]** Weak stability `⟹ (A)SD`; Theorem D.
- J.-P. Bourguignon, H. B. Lawson, J. Simons, *Stability and gap phenomena for Yang–Mills fields*, Proc. Natl. Acad. Sci. USA **76** (1979) 1550–1553.
- M. Min-Oo, *An `L₂`-isolation theorem for Yang–Mills fields*, Compositio Math. **47** (1982) 153–162. **[free, numdam]** And J. Dodziuk, M. Min-Oo, same volume, 165–169. **[free, numdam]**
- P. Feehan, *Energy gap for Yang–Mills connections, I & II*, Adv. Math. **312** (2017), arXiv:1412.4114 and arXiv:1502.00668; and *Discreteness for energies of Yang–Mills connections over four-dimensional manifolds*, arXiv:1505.06995. **[all free]** The general non-explicit gap and the discreteness of critical values.
- **★★ C. H. Taubes, *Stability in Yang–Mills theories*, Comm. Math. Phys. **91** (1983) 235–263.** **[paywalled]** The index bound `i ≥ 2(|κ|+1)`.
- M. Gursky, C. L. Kelleher, J. Streets, *Index-energy estimates for Yang–Mills connections and Einstein metrics*, Comm. Math. Phys. **376** (2020) 117–153, arXiv:1901.04539. **[free]** Index bounded by energy, both ways.
- M. Vieira, *Gap theorems in Yang–Mills theory for complete four-dimensional manifolds with positive Yamabe constant*, arXiv:2406.06853. **[free]**
- **★ C. H. Taubes, *A framework for Morse theory for the Yang–Mills functional*, Invent. Math. **94** (1988) 327–402.** **[paywalled]** Unread; the natural place to look for §6.2's structure questions.
- C. LeBrun, L. J. Mason, *Global anti-self-dual Yang–Mills fields in split signature and their scattering*, J. reine angew. Math. (2006), math-ph/0505039. **[free]** Why the holomorphic/split setting has no positivity and loses regularity.

### 9.4 ADHM background

- **★ M. F. Atiyah, *Geometry of Yang–Mills Fields*, Lezioni Fermiane, Pisa (1979).** **[paywalled]** The quaternionic normal form of §3.1 and the regularity condition.
- **★ M. F. Atiyah, V. G. Drinfeld, N. J. Hitchin, Yu. I. Manin, *Construction of instantons*, Phys. Lett. A **65** (1978) 185–187.** **[paywalled]** The original.
- **★ S. K. Donaldson, P. B. Kronheimer, *The Geometry of Four-Manifolds*, OUP (1990).** **[paywalled]** §2.3 for the gap in the charge-normalised form; the standard reference for the moduli theory.
- C. H. Taubes, *Path-connected Yang–Mills moduli spaces*, J. Differential Geom. **19** (1984) 337–392. **[free, projecteuclid]**
- For the determinantal-representation circle that §3.3 sits in (and the novelty question): the Lax conjecture and Helton–Vinnikov literature on hyperbolic polynomials and symmetric determinantal representations. **Not yet surveyed — §3.3 has never been novelty-checked and the prior should be that it is known.**

### 9.5 The RH side — needed only for §§2.4, 2.6 and §7

- B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum of Math. Pi **8** (2020) e6, arXiv:1801.05914. **[free]**
- D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn–Newman constant*, Res. Math. Sci. **6** (2019) art. 31, arXiv:1904.12438. **[free]** `Λ ≤ 0.22`.
- C. M. Newman, *Fourier transforms with only real zeros*, Proc. Amer. Math. Soc. **61** (1976) 245–251. **[free, ams.org]** Remark 2, p. 250 — the "only barely so" dictum. ⚠️ His sign conventions differ from the modern ones and the reachable transcriptions are internally inconsistent; check a printed page.
- **★ G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant `Λ`, and the Riemann Hypothesis*, Constr. Approx. **10** (1994) 107–129.** **[paywalled]** The Lehmer-pair criterion. ⚠️ Unresolved: whether their `Δ` is in `x = 2γ` units or `γ` units — a factor of 4 in `Λ`.
- **★ G. Csordas, A. Ruttan, R. S. Varga, *The Laguerre inequalities with applications to a problem associated with the Riemann hypothesis*, Numer. Algorithms **1** (1991) 305–329.** **[paywalled]** The `L_1` certificate method.
- M. Griffin, K. Ono, L. Rolen, D. Zagier, *Jensen polynomials for the Riemann xi-function*, Adv. Math. (2022); PNAS **116** (2019). **[free versions exist]** Hyperbolicity of `J^{d,n}` for `n ≥ ce^d`.

---

## 10. Honesty notes

**What is proved, and airtight:** §1.1 (the equivariance identity); §2.1 and its corollaries; §3.2, §3.3, §3.4, §3.5 (all with symbolic verification); the dimension ladder of §4.6 as a generic-codimension count.

**What is empirical:** §3.6 and §3.7. §3.7 is load-bearing and unproven, and §6.3 asks for it.

**What is inherited and not verified here:** §2.3's degree computation; the Laguerre–Pólya characterisation via `L_n ≥ 0`; `Λ ≥ 0` and `Λ ≤ 0.22`; everything in §4.4 (nine papers, cited individually — the point of §4.4 is precisely that it is *not* our mathematics).

**What is folklore:** the infinite-dimensionality of the local YM solution space (§4.3). The determined/overdetermined contrast is solid; the conclusion is not cited.

**What was withdrawn from the predecessor project, so you do not re-derive it:** the claim that full YM was closed (it was not); the claim that a nonzero current is an extra handle (it is not — §4.2); "symmetry is load-bearing in exactly one place" in ADHM Theorem A (it is load-bearing at the spectral step too — §3.4); "positive semidefiniteness of `C` is not needed anywhere" (true of that proof, misleading as a claim — §3.7); and a jet-order screen stated as universal when it is family-specific (§3.5's caveat).

**Novelty: assume everything here is known until checked.** §3.3 is a rigidity result about determinantal representations of real polynomials by symmetric pencils, and that circle — Lax conjecture, Helton–Vinnikov, hyperbolic polynomials — is heavily worked; ADHM linear algebra has been studied since 1978. §3.5's deficit formula is the kind of identity that falls out of routine axial-monogenic computations. §2.1 is the identity theorem for holomorphic functions on a maximally totally real subspace. Each needs a literature sweep before circulation, and the prior should be that it comes back known.

**The single most useful habit from the predecessor project:** run every new proposal against §7's test set before building anything, and ask of every screen whether it is universal or family-specific before treating a failure as a refutation.
