# The Positivity Dichotomy Is False

*Working memo #18 — August 24, 2026. Answers brief §6.3 / memo 12 §0(2) "Status of (ii)", the one item both documents flag as load-bearing and unproven. The answer is: **true at `k = 2`, and false from `k = 4` on**, with explicit counterexamples verified in exact rational arithmetic. Memo 12 §0(3) and its Screen 0″ are withdrawn. Certified by `lab_positivity_refuted.py`.*

---

## 0. Results

The object under test is memo 7's shape, with every hypothesis dropped except reality of the blocks and symmetry of `C`:

> `M(q) = C + |q|²I − 2Σ_{a=0}^{3} x_a T_a`, `T_a ∈ ℝ^{k×k}` **arbitrary**, `C ∈ ℝ^{k×k}` symmetric, and
> `det M(q) = P_p(q) := p(x_0+ir)p(x_0−ir)` **for all `q ∈ ℍ`**, `p` monic real of degree `k`.

Brief §3.7 / memo 12 §0(2) conjectured: `C ⪰ 0 ⟹ p` hyperbolic.

**(1) Theorem A — true at `k = 2`, and as an exact equivalence.**

> For `k = 2`, given the matching identity: **`C ⪰ 0` ⟺ `p` is hyperbolic.**

Proved in §1. Both directions; the proof is four coefficient identities plus the fact that the trace form on `sl(2,ℝ)` is Lorentzian.

**(2) Theorem B — false at `k = 4`. Two explicit families, verified exactly over `ℚ`.**

Let `T_1, T_2, T_3` be real `4×4`, traceless, anticommuting, with `T_a² = s²I` — a representation of the Clifford algebra `Cl_{3,0}(ℝ)`. Concretely
`T_1 = σ_3 ⊗ I`, `T_2 = σ_1 ⊗ I`, `T_3 = (iσ_2) ⊗ Y`, with `Y = [[0,1],[−1,0]]`, all real.
Let `J = I ⊗ (iσ_2)` be the complex structure in their commutant.

> **B1 (doubled pair).** `T_0 = aI`, `C = (a² + s²)I₄`. Then `C ≻ 0` and
> `p(u) = ((u−a)² + s²)²` — a **doubled** conjugate pair.
>
> **B2 (simple pairs).** `T_0 = bJ` with `s > |b|`, `C = (s² − b²)I₄`. Then `C ≻ 0` and
> `p(u) = (u² + (s+b)²)(u² + (s−b)²)` — **two simple** conjugate pairs.

Both satisfy `det M(q) = P_p(q)` **identically on `ℍ`**. Exact `sympy` verification over `ℚ`: with `a = 3/5, s = 1` (B1) and `b = 1/2, s = 3/2` (B2), `det M − P_p` expands to the integer `0`. Numerically, max relative error `4.4e−13` (B1) and `2.0e−13` (B2) over 6000 random `q ∈ ℍ`.

B2 also kills the natural weakening: **the non-real roots need not have even multiplicity.** `(u²+1)(u²+4)` has four distinct simple roots and is realised with `C = 2I₄ ≻ 0`.

**And B1 is stronger than it looks: all four of its blocks are symmetric.** `T_0 = aI`, and `σ_3⊗I`, `σ_1⊗I`, `(iσ_2)⊗(iσ_2)` are each symmetric. So B1 sits in memo 12's *most* constrained family — `T` symmetric **and** `C` symmetric PSD — and refutes that column too, not only the PSD one. (No conflict with memo 7 Theorem A, which additionally imposes the ADHM link `C = Σ_aT_a² + Re(λ†λ)` with `λ†λ ⪰ 0`; B1 has `C = ΣT_a² − 2s²I`, so it is not an ADHM datum.)

**(3) The mechanism, and it is clean.** Write `N_e = T_0 + iT_e`. The matching identity is equivalent, slice by slice, to
`det(uvI − uN_e − v\bar N_e + C) = p(u)p(v)`, and setting `R_e := C − \bar N_e N_e` this is
`det(P + R_e) = det P` with `P = (uI − \bar N_e)(vI − N_e)`. The stratum `R_e ≡ 0` is classified in §3:

> `R_e = 0` for every unit `e` **iff** `[T_0, T_a] = 0`, `{T_a, T_b} = 0` for `a ≠ b`, `T_1² = T_2² = T_3² =: Ω`, and `C = T_0² + Ω`.
> Every such datum matches, with `p = charpoly(T_0 + iT_e)`.

So `C = T_0² + Ω`, and with `T_0` scalar, **hyperbolicity is decided by `sign(Ω)` while positivity of `C` is decided by `T_0`**:

| | `Ω = +s²I` (Clifford, `Cl_{3,0}`) | `Ω = −s²I` (quaternionic) |
|---|---|---|
| `spec(T_e)` | `±s` (real) | `±is` (imaginary) |
| `p`, for `T_0 = aI` | roots `a ± is` — **non-hyperbolic** | roots `a ∓ s` — **hyperbolic** |
| `C = a²I + Ω` | `(a²+s²)I ≻ 0` **always** | `(a²−s²)I ⪰ 0` iff `|a| ≥ s` |

> **`C ⪰ 0` and hyperbolicity are logically independent in this stratum.** Positivity is supplied by `T_0`; hyperbolicity is supplied by the sign of `T_e²`. They are different data. That is the whole refutation.

**(4) Why memo 12's search missed it, exactly.** The matching forces `tr T_a = 0` for `a ≥ 1` (the `u^{k−1}` coefficient makes `tr N_e` real). Then `Ω ≻ 0` requires three traceless anticommuting real involutions (after rescaling by `Ω^{−1/2}`, which is legitimate since `Ω` is central in the algebra they generate).

- **`k` odd:** a real involution on `ℝ^k` has eigenvalues `±1` with odd total multiplicity, so its trace is odd — never `0`. **Impossible.**
- **`k = 2`:** the trace form `⟨X,Y⟩ = tr(XY)` on `sl(2,ℝ)` has signature `(2,1)`; three orthogonal vectors of common norm `κ = 2s² > 0` would span a 3-dimensional positive-definite subspace. **Impossible** — and this is the same computation that drives Theorem A.
- **`k = 4`:** `Cl_{3,0}(ℝ) ≅ M_2(ℂ)` has minimal real module `ℝ⁴`. **First possible dimension.**

Memo 12 searched `k = 2` and `k = 3` only. Both are immune for structural reasons. The table in memo 12 §0(2) is correct; its extrapolation to general `k` was not.

**(5) What this does to the programme.**

- **Memo 12 §0(3) — "structural positivity is not a resource but the trap" — is withdrawn.** A class supplying positivity does *not* automatically force the conclusion.
- **Memo 12 §6, Screen 0″ (positivity audit), is withdrawn** in its "therefore circular" form. Its *procedure* (drop every other hypothesis and test the positivity alone) is still the right thing to do; its *verdict* was wrong.
- **Memo 12 §4's reason (2) for closing full Yang–Mills is void.** Reasons (1) — memo 11's holomorphic no-go — and (3) — the degeneracy locus is where the object fails to exist (Pool Thm IV.5) — stand untouched. Full YM is not closed by positivity.
- **But this does not open anything either, and the honest reading is a downgrade, not an upgrade.** Brief §6.3 anticipated "if it fails outside that shape, the matching reading reopens." It fails *inside* the ADHM shape, at `k = 4`, and what it shows is that the class `{matching, C ⪰ 0}` **is not sphere-free**: B1 and B2 are members whose degeneracy locus contains genuine 2-spheres. By brief §1.2 the sphere-free property is exactly what a route needs as a *theorem about the class*, and `C ⪰ 0` is now known not to supply it. The diagnosis moves from "circular" to "contentless". Contentless is the more ordinary failure, and the more final one.
- **Net:** one wrong reason for closure removed, one plain reason for closure installed, and one real theorem gained (Theorem A).

---

## 1. Theorem A, and its proof

**Reduction to a two-variable identity.** Restrict `q` to the slice `Π_e = {x_0 + ye}`, continue `y → iη`, set `u = x_0+η`, `v = x_0−η`. Then `x_0²+y² = uv` and `−2x_0T_0 − 2yT_e = −uN_e − v\bar N_e` with `N_e = T_0 + iT_e`. Since `ℍ = ⋃_e Π_e`, matching on `ℍ` is equivalent to

  `det(uv·I − uN_e − v\bar N_e + C) = p(u)p(v)` for every unit `e`.  (1.1)

**The `k = 2` coefficient conditions.** Expanding (1.1) at `k = 2` with `p(u) = u² − su + d` gives eight conditions, all verified symbolically:

| monomial | condition |
|---|---|
| `u²v`, `uv²` | `tr N_e = s` (so `tr T_0 = s`, **`tr T_e = 0`**) |
| `u²`, `v²` | `det N_e = d` |
| `uv` | `tr C = tr(N_e \bar N_e) = tr T_0² + tr T_e²` |
| `u`, `v` | `tr(N_e C) = s(tr C − d)` |
| `1` | `det C = d²` |

**Step 1 — `κ = 0`.** The `uv` condition makes `e ↦ tr T_e²` constant on `S²`, so `tr(T_aT_b) = κ δ_{ab}` for `a,b ≥ 1`. The `T_a` are traceless real `2×2`, i.e. elements of `sl(2,ℝ)`, on which `tr(XY)` has Gram `diag(2,2,−2)` in the basis `h, m, J` — signature `(2,1)`. If `κ ≠ 0` the Gram of `(T_1,T_2,T_3)` is `κI_3`, nonsingular, so they are a basis, and the form would have signature `(3,0)` or `(0,3)`. Hence **`κ = 0`**.

**Step 2 — `d = det T_0`.** For `2×2`, `det(X+iY) = det X − det Y + i(tr X tr Y − tr(XY))`. With `tr T_e = 0`, `det T_e = −½ tr T_e² = −κ/2 = 0`, and reality of `det N_e = d` forces `tr(T_0T_e) = 0`. So `d = det T_0`, and `tr C = tr T_0² = s² − 2d`.

**Step 3 — the inequality.** `C` is symmetric `2×2` with `tr C = s² − 2d` and `det C = d²`. If `C ⪰ 0` then `tr C ≥ 2√(det C) = 2|d|`, so `s² − 2d ≥ 2|d|`.
 - `d > 0`: gives `s² ≥ 4d`, so `disc(p) = s² − 4d ≥ 0`.
 - `d ≤ 0`: `disc(p) = s² − 4d ≥ 0` outright.

Either way **`p` is hyperbolic**.

**Converse.** If `p` has real roots `ρ_1, ρ_2` then `tr C = ρ_1² + ρ_2² ≥ 0` and `det C = (ρ_1ρ_2)² ≥ 0`, and a symmetric `2×2` with non-negative trace and determinant is PSD. `∎`

**Corollary (the spectrum of `C` is pinned at `k = 2`).** `spec(C) = {ρ_1², ρ_2²}`. So `C` real symmetric already forces each `ρ_j²` real — every root of `p` is real *or purely imaginary* — and `C ⪰ 0` then forces `ρ_j² ≥ 0`, i.e. `ρ_j ∈ ℝ`. This is the spectral-mapping argument that also disposes of memo 12's companion-matrix counterexample (there `C = T_0²`, and `T_0² ⪰ 0` symmetric forces `spec(T_0) ⊂ ℝ` directly). **At `k = 2` the whole conjecture is the spectral theorem again — which is why it was never going to generalise.**

---

## 2. Theorem B, the counterexamples

Both are `R_e ≡ 0` data, so the verification is one line: `R_e = 0` makes (1.1) read
`det((uI − \bar N_e)(vI − N_e)) = det(uI − \bar N_e)·det(vI − N_e) = p(u)p(v)`,
using that `p` real gives `det(uI − \bar N_e) = \overline{det(\bar u I − N_e)} = p(u)`.

**B1.** `T_a = s·(σ_3⊗I, σ_1⊗I, (iσ_2)⊗Y)`, `T_0 = aI₄`, `C = (a²+s²)I₄`.
`T_e² = s²I` for every unit `e` (anticommutation), so `\bar N_e N_e = T_0² + T_e² + i[T_0,T_e] = (a²+s²)I = C` — real, symmetric, `e`-independent, positive definite. `T_e` is `s` times a traceless involution, `spec(T_e) = {s,s,−s,−s}`, so `spec(N_e) = {a ± is}` each twice and `p(u) = ((u−a)²+s²)²`.
*Exact check (`a = 3/5, s = 1`):* `C = (34/25)I₄`, `det M − P_p ≡ 0` over `ℚ`, `p` roots `3/5 ± i` each of multiplicity 2.

**B2.** Same `T_a`; `T_0 = bJ` with `J = I⊗(iσ_2)` in the commutant, `J² = −I`.
`\bar N_e N_e = T_0² + T_e² = (s² − b²)I = C`, positive definite for `s > |b|`. `J` and `T_e` commute with joint spectrum `(±i, ±s)`, so `spec(N_e) = {i(±b ± s)}` — four *simple* purely imaginary values — and `p(u) = (u²+(s+b)²)(u²+(s−b)²)`.
*Exact check (`b = 1/2, s = 3/2`):* `C = 2I₄`, `p = (u²+1)(u²+4)`, `det M − P_p ≡ 0` over `ℚ`.

**Why `C` cannot be made symmetric for a general `T_0`.** The commutant of an irreducible `Cl_{3,0}(ℝ)` module `ℝ⁴` is `ℂ = {aI + bJ}`. Then `C = T_0² + s²I = (a² − b² + s²)I + 2ab·J`, and `J` is skew, so **`C` symmetric ⟺ `ab = 0`** — exactly the two branches B1 and B2. This is also why the complex roots in B1 sit off the imaginary axis but are doubled, while those in B2 are simple but purely imaginary: within one irreducible block you get one or the other, not both.

**The contrast case, for the record.** Taking instead `T_a = L_a` (left multiplication by `i,j,k` on `ℍ = ℝ⁴`), `Ω = −I`, commutant `= ℍ` acting by right multiplications `R_μ`. `C = R_μ² − I` is symmetric iff `μ` is real or purely imaginary. Real `μ = a`: `C = (a²−1)I`, `p` hyperbolic with roots `a ∓ 1`. Purely imaginary `μ`: `C = −(1+|μ|²)I ≺ 0`, `p` non-hyperbolic with roots `±1 ± i|μ|`. Verified numerically to `1.2e−13` over 4000 points. **This family reproduces memo 12's phenomenon with all four blocks nonzero and `κ = −4 ≠ 0`** — the §3.4 companion-matrix datum is not the only contentless family, merely the `T_{1,2,3} = 0` corner of a much larger one.

---

## 3. The `R ≡ 0` stratum, classified

**Proposition.** `C = \bar N_e N_e` for every unit `e` **iff** `[T_0,T_a] = 0` (`a ≥ 1`), `{T_a,T_b} = 0` (`a ≠ b`), `T_1² = T_2² = T_3² =: Ω`, and `C = T_0² + Ω`.

*Proof.* `\bar N_e N_e = T_0² + T_e² + i[T_0,T_e]`. `C` real forces `[T_0,T_e] = 0` for every `e`, hence `[T_0,T_a] = 0`. `C` independent of `e` forces `T_e² = C − T_0²` independent of `e`; expanding `T_e² = Σ_a e_a²T_a² + Σ_{a<b}e_ae_b\{T_a,T_b\}` and taking `e` along the axes gives `T_a² = Ω` common, and then the anticommutators must vanish. Conversely all of this makes `R_e = 0`. `∎`

`Ω` is central in the algebra generated by the `T_a` (`T_bT_a² = T_a²T_b` by anticommuting twice), so when `Ω ≻ 0` the rescaled `Ω^{−1/2}T_a` are anticommuting involutions and one has a genuine `Cl_{3,0}(ℝ)` representation. Combined with `tr T_a = 0`, this is what forces `4 | k`.

**Achievable `p` in this stratum at `k = 4`, with `C ⪰ 0`:** exactly `((u−a)²+s²)²` and `(u²+(s+b)²)(u²+(s−b)²)` with `s ≥ |b|`, plus the hyperbolic `Ω ≺ 0` branch. Block sums with `T_{1,2,3} = 0` blocks (where `T_0` symmetric, `C = T_0² ⪰ 0`, `p` hyperbolic) give products with any hyperbolic factor.

**Theorem C (the general member — this closes the question left open above).** The corollary above wrongly assumed `Ω` scalar. `Ω = T_a²` need only be **central in the algebra the `T_a` generate**, and for an irreducible `Cl_{3,0}(ℝ)` module on `ℝ⁴` that centre is `ℂ = {αI + βJ}`. Allowing `Ω` a `J`-component gives the full family:

> Identify `ℂ ≅ {αI + βJ}` inside the commutant. For `z, w ∈ ℂ` with `z² + w² ∈ ℝ_{>0}`, set
> `T_0 = z`,  `T_a = M_a·w`,  `C = (z²+w²)·I₄`.
> Then `C ≻ 0` and `det M(q) = P_p(q)` **identically on `ℍ`**, with
> `p(u) = (u−ρ_1)(u−\barρ_1)(u−ρ_2)(u−\barρ_2)`,  `ρ_1 = z + iw`,  `ρ_2 = z − iw`,  and `ρ_1ρ_2 = z²+w² = λ`.

Writing `z = a+bJ`, `w = σ+τJ`, the reality of `z²+w²` is `ab + στ = 0` and `λ = a²−b²+σ²−τ²`. B1 is `b = τ = 0` and B2 is `a = τ = 0`; the general member has **four simple non-real roots with real parts `a∓τ`, off the imaginary axis whenever `a ≠ ±τ`.**

**Exact integer instance.** `z = 3+i`, `w = 3−i` (so `ab+στ = 3−3 = 0`, `λ = 16`):

```
T_0 = [[3,1,0,0],[-1,3,0,0],[0,0,3,1],[0,0,-1,3]]      C = 16·I_4  (positive definite)
T_1 = [[3,-1,0,0],[1,3,0,0],[0,0,-3,1],[0,0,-1,-3]]    p = (u²-8u+32)(u²-4u+8)
                                                        roots 4±4i, 2±2i  — four SIMPLE roots
```
`det M(q) − P_p(q)` expands to the integer `0`. **So a simple conjugate pair with nonzero real part is realisable with `C ≻ 0`.** There is no residual protection of that kind.

**Theorem D (what the residual constraint actually is).** Suppose `C = λI` is scalar. Setting `v = 0` in (1.1) gives `det(λI − uN_e) = p(0)p(u)`, and the left side is `u^k p(λ/u)`. Hence

> `u^k·p(λ/u) = p(0)·p(u)` — the root multiset of `p` is invariant under `ρ ↦ λ/ρ`, and `p(0)² = λ^k`.

At `k = 4` this reads `c_0 = λ²` and `c_1 = λc_3`: a **codimension-one** condition. It is exactly the pairing `ρ_1ρ_2 = λ` of Theorem C, and it is what makes the achievable non-hyperbolic locus 3-dimensional inside the 4-dimensional space of monic quartics — confirmed independently by walking the solution variety and doing PCA on the `p` reached (singular values `0.79, 0.37, 0.11, 0.0009`; the hyperbolic control returns the full `4`).

**This constraint is useless for the programme, and it is worth saying why.** It is not a hyperbolicity condition — it permits simple off-axis conjugate pairs, as Theorem C shows. What it constrains is *which* `p` can be attached to a gauge object at all. A Jensen polynomial of `Ξ` will essentially never be `λ`-self-reciprocal, so the dictionary fails at the **membership** step, not at the isolation step. That is brief §1.2 exactly: the geometry supplies the implication and never the verification.

---

## 4. Numerical record

Best RMS residual of `(det M − P_p)/⟨|P_p|⟩` over 76 sample points of `ℍ`, `C = LLᵀ` so PSD is structural, `T_a` free.

| `k` | `p` | roots | `C ⪰ 0` best | reading |
|---|---|---|---|---|
| 2 | `z²+1` | simple pair | `4.4e−02` | **plateau** — Theorem A |
| 3 | `(z−1)((z+2)²+9)` | simple pair | `3.4e−02` | **plateau** — odd `k` is immune (§0(4)) |
| 3 | `(z−1)(z−2)(z−3)` | 3 real | `1.4e−15` | hyperbolic control |
| 4 | `(z²+1)²` | doubled pair | `2.9e−15` | **solved** (B1) |
| 4 | `((z−.6)²+1)²` | doubled pair | `4.7e−15` | **solved** (B1) |
| 4 | `(z²+1)(z²+4)` | 2 simple pairs | `8.9e−06` | **solved exactly** (B2); optimiser slow |
| 4 | near-miss quartic | simple pair, off-axis | `8.7e−08` | inconclusive (see §3) |
| 4 | `(z−1)(z−2)(z²+1)` | simple pair, off-axis | `1.3e−05` | inconclusive |
| 4 | `(z−1)(z−2)(z−3)(z−4)` | 4 real | `1.6e−15` | hyperbolic control |

The `k = 2` and `k = 3` plateaus sit `13` orders above the hyperbolic controls; the `k = 4` doubled-pair rows sit *at* the controls. That is the refutation visible in one table.

**The near-miss quartic rows are worthless as evidence and should not be quoted.** It is `Λ = 3.9e−05` from hyperbolic, and the hyperbolic stratum is fully achievable, so a tiny residual is expected whether or not it is reachable. The question it was meant to probe is settled instead by Theorem C.

**Homotopy record (`C = I` fixed, `T_a` free).** Continuing `ρ = re^{iθ}` at `r = 1.618` from `θ = 90°` (B2, roots on the imaginary axis) down to `θ = 57.5°`, solving at each step:

| `θ` | roots of `p` | RMS |
|---|---|---|
| `90.0°` | `±1.618i, ±0.618i` | `2.6e−15` |
| `75.0°` | `0.419±1.563i, 0.160±0.597i` | `4.8e−14` |
| `60.0°` | `0.809±1.401i, 0.309±0.535i` | `8.3e−14` |
| `57.5°` | `0.869±1.365i, 0.332±0.521i` | `3.1e−13` |

Machine precision throughout, with `C = I ≻ 0` and four simple roots moving continuously off the imaginary axis. Independent check of the `θ = 60°` datum on 10 000 fresh `q` at a wider scale: max relative error `2.9e−10`.

`C` symmetric but unconstrained reaches `2.9e−15` at `k = 2` on `z²+1`, reproducing memo 12.

---

## 5. Errata to memo 12 and to the brief

- **Memo 12 §0(2)**: the claim "`C ⪰ 0` alone forces hyperbolicity" holds at `k = 2` (now a theorem) and is **false for `k ≥ 4`**. The `k = 2,3` table is correct as data; the generalisation is not.
- **Memo 12 §0(3)** and **§6 Screen 0″**: withdrawn as stated. Positivity is neither the resource nor the trap; it is simply not decisive.
- **Memo 12 §4 reason (2)**: void.
- **Brief §3.7**: replace with Theorem A + Theorem B.
- **Brief §6.3**: resolved. Outcome: the matching reading of full YM is no longer closed *by positivity*, but the ADHM shape with `C ⪰ 0` is now known **not to be sphere-free**, which closes it more plainly. The one residual constraint (Theorem D) is a reciprocality condition, not a hyperbolicity condition, and constrains membership rather than isolation.
- **Memo 12 §0(2), fourth column** ("symmetry of the `T_a` independently forces hyperbolicity"): also false for `k ≥ 4`. B1 has all four blocks symmetric.
- **This memo's own §3 corollary**, as first written, assumed `Ω = T_a²` scalar. It need only be central in the algebra generated; Theorem C is the corrected general statement.
- **Brief §10 "What is empirical"**: `§3.7` moves out of "empirical, load-bearing" and into "false, with a `k = 2` theorem salvaged".

*Certified by `lab_positivity_refuted.py`: Part 1, symbolic derivation of all eight `k = 2` coefficient conditions and the `sl(2,ℝ)` Gram; Part 2, exact `ℚ`-arithmetic verification of B1 and B2 (`det M − P_p` expands to `0`) plus `6000`-point numerical checks; Part 3, the quaternionic contrast family; Part 4, the PSD-constrained searches of §4. Parts 1–3 are exact; Part 4 is a search and is labelled inconclusive where it is.*

---

## 6. What the shape of Theorem D actually says (added after §5)

Two exact statements, both inside Theorem C's family, both verified symbolically.

**(a) The residual constraint is a functional equation, not a hyperbolicity condition.** Theorem D says the roots pair as `ρ ↦ λ/ρ`. Substituting `ρ = e^{s}` and `λ = e` turns that pairing into `s ↦ 1 − s`. So what `C = λI` imposes on `p` is exactly a functional equation in the multiplicative variable.

**(b) Symmetry of the blocks is the RH condition — for the circle, not the line.** Within Theorem C (`T_0 = z`, `T_a = M_a w`, `C = (z²+w²)I`, `z = a+bJ`, `w = σ+τJ`):

> `T_0 − T_0ᵀ = 2bJ` and `T_a − T_aᵀ = 2τ·M_aJ`, so **all four blocks are symmetric ⟺ `b = τ = 0`**. And `ρ_2 − \barρ_1 = 2(ib + τ)`, so
>
> **all blocks symmetric ⟺ `ρ_2 = \barρ_1` ⟺ `|ρ|² = a² + σ² = λ` ⟺ every root lies on the circle of radius `√λ`** — equivalently, the pairing `ρ ↦ λ/ρ` coincides with `ρ ↦ \barρ`.

Under `ρ = e^s`, `λ = e`, that circle is `Re s = 1/2`.

**The dictionary this produces.**

| ADHM shape | arithmetic |
|---|---|
| `C = λI` forces `ρ ↦ λ/ρ` (Thm D) | the functional equation `s ↦ 1−s` |
| generic member of Thm C (`b, τ ≠ 0`) | functional equation **without** RH |
| all four blocks symmetric | `|ρ| = √λ`, i.e. **RH** |
| B1 (`b = τ = 0`) | the RH locus; B2 (`a = τ = 0`) is the `Re s = 0` degeneration |

**The reading.** The ADHM/gauge determinant natively implements the **multiplicative** form of RH — a modulus condition on a circle, with symmetry of the data as the RH hypothesis — which is the *function-field* shape: `P(T) = ∏(1 − α_iT)`, functional equation `α ↦ q/α`, RH `|α_i| = √q`, and Weil's proof by positivity of an intersection form (brief §2.5). The predecessor project has instead been feeding it the **additive** form: Jensen polynomials and hyperbolicity, roots on a *line*. Memo 7's Theorem A ("symmetry ⟹ real roots") and this section ("symmetry ⟹ roots on a circle") are the same phenomenon read in two incompatible variables, and they agree only on their intersection `ρ = ±√λ`.

**That is a better diagnosis of the programme's failures than §3.7 ever was:** the collapses were not all positivity artefacts, they were a shape mismatch. It also says where a non-redundant construction would have to live — the Frobenius/Euler-product definition of `ζ`, not the theta/Mellin one.

**And the honest limit of the observation.** `ρ = e^s` is not injective, so a degree-`k` polynomial in `ρ` corresponds to a `2πi`-periodic set of `s`-zeros. That is exactly right for a function-field zeta, whose zeros *are* periodic with period `2πi/\log q`. Riemann's zeros are not periodic, and there is no `q`. So the alignment is a statement about shape, not a route: it says the machinery is built for the case where RH is already a theorem.
