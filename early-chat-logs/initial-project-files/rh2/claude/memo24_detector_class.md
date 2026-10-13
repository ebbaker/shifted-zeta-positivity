# What a Detector of Off-Axis Zeros Can Be

*Working memo #24 — August 24, 2026. Two things: the ADHM curvature formula is now verified from a primary source, discharging memo 21's one open assumption; and the programme is re-scoped as the user directed — spheres and equivariance dropped, the only target being a criterion for non-real zeros. Under that scope a classification theorem is available, it is three lines, and it says exactly which topological detectors are possible. Certified by `lab_detector_class.py` and `lab_jensen_bezoutian.py`.*

---

## 0. Results

**(1) Atiyah's ADHM curvature formula — verified, from Dorey–Hollowood–Khoze–Mattis rather than Atiyah.** Neither Atiyah's *Lezioni Fermiane* nor Donaldson–Kronheimer was obtainable, but neither is needed. DHKM, *The Calculus of Many Instantons* (hep-th/0206063), Eq. **(2.52)**, derived there in four lines from the null-space projector:

> `F_mn = 4 g⁻¹ Ū b σ_mn f b̄ U`,  `f = (Δ̄Δ)⁻¹` a Hermitian `k×k` matrix, `Δ = a + b x`.

With the canonical form for `b` (their **(2.57)**, `b^β_{(u+iα)j} = (0 ; δ^β_α δ_ij)`, together with the identity **(2.61)** `b̄_α b^β = δ_α^β 1_k`), the `b`'s simply extract the lower `2k` block, so

> `F_mn = 4g⁻¹ Σ_{i,j} f_{ij} · c_i σ_mn c̄_j`,  `c_i :=` the `i`-th instanton block of `Ū` (an `N×2` matrix).

For `SU(2)`, `N = 2`, and DHKM note after (2.58) that the gauge index is then carried by the same undotted spinor index — so `c_i` **is a quaternion**. That was the one step memo 21 assumed without proof. With `f` real symmetric, diagonalising `f = Σ_m μ_m u_m u_mᵀ` and setting `d_m = Σ_i (u_m)_i c_i` gives

> `T = Σ_{m=1}^{k} ν_m R_m`,  `ν_m = μ_m|d_m|²`, `R_m ∈ SO(3)`,

which is memo 21 §0(2) verbatim. **Memo 21's structure theorem is no longer an assumption**, and its corollaries (`k=1` conformal; `k=2` a forced repeated singular value; `k≥3` generic) stand on a derivation rather than on numerical corroboration alone. Memo 22 §3's "not verified" item is closed.

**(2) Re-scoping.** Spheres and equivariance are dropped by instruction. That is not a small edit to the screens; it changes which of them are live:

| still unconditional | dead with equivariance |
|---|---|
| brief §1.5 / screen 0 (equational no-go, both parities) | §1.1–1.2 (sphere-free *is* hyperbolicity, relabelled) |
| screen 2 (deformation invariants) — and see §0(3) | §2.2 (instance A) |
| screen 3 (`Λ ≥ 0`, no uniform margin) | §2.3 / screen 6 (the Vekua `2/r` trace term) |
| screen 4 (multiplicative rigidity) | screen 1′'s slice clause, and §2.7(c)'s closure of §2.4 |
| §3.5 / screen 0″ (positivity is the trap) | §5 (the symmetry hypothesis being unsatisfiable) |
| screen 9 (circularity) | the whole memo 20–22 locus programme (memo 23 §0(4)) |

Notably **§2.4 reopens**. The `σ`-type of divisor components — real zeros give `ρ`-invariant components, conjugate pairs `ρ`-swapped pairs — is the one invariant this project ever found that is not deformation-invariant. §7.2 closed it by combining §2.7(c) with §1.5, but §2.7(c) only forbids reading it off a **finite-order jet along one slice**, which was an equivariance-era requirement. Dropped, it is admissible again. §0(4) says what it turns into.

**(3) The classification theorem. This is the substantive item, and it answers the question directly.** Fix `d ≥ 2`; let `P_d ≅ ℂ^d` be the monic degree-`d` polynomials, `Δ ⊂ P_d` the discriminant hypersurface, `H ⊂ ℝ^d` the hyperbolic locus.

- **(a) `P_d` is connected.** So any quantity invariant under continuous deformation of the polynomial is *constant*, and no such quantity can have `H` as a level set. **This kills every characteristic class, index, degree, charge, winding number and Thom polynomial, in one line** — and it kills them in any ambient space, for any construction, with no appeal to Davenport–Heilbronn. Brief screen 2 was tagged *[universal]* on the strength of two computations; it now has a proof.
- **(b) `P_d ∖ Δ` is connected** (the complement of a proper algebraic hypersurface in an irreducible variety). So any quantity merely *locally constant on the complex discriminant complement* is also constant. **This kills wall-crossing and braid-monodromy invariants too, as long as they are defined over `ℂ`.** Certified by explicit paths: `z² + a` with `a = e^{iθ}`, `θ: π → 0`, joins `z²−1` to `z²+1` with `min|disc| = 4`; and at `d = 4` a random imaginary detour joins `z⁴−5z²+4` to `z⁴+5z²+4` with `min|disc| = 3217`. The same interpolation kept **real** crosses the discriminant (`min|disc| = 7.8e−28`).
- **(c) `ℝ^d ∖ Δ_ℝ` is disconnected, and `{p : d` distinct real roots`}` is a union of its connected components** — a real root can leave `ℝ` only by colliding with another, which means crossing `Δ_ℝ`. `H` is its closure.

> **A detector of non-real zeros must be an invariant of the *real* structure that jumps across the real discriminant, and it must not extend to the complex parameter space — not holomorphically (§1.5), and not even locally constantly (b).**
>
> This is the exact analogue of §1.5 in the topological category, and it is the reason memos 20–22 could not have worked: any charge, class or index of a gauge-theoretic object is a deformation invariant, so by (a) it is blind before any computation.

**(4) The admissible class is nonempty, and the project already owned two members without labelling them.** Invariants of the right type are **signatures** and real chamber indices. The classical complete one is the **Bezoutian**: `H_{ij} = s_{i+j}`, `s_k = Σ_ρ ρ^k` the Newton power sums. Hermite: `rank H = ` #distinct roots, `sig H = ` #distinct **real** roots. Run against the brief's §9.2 test set:

| `p` | `sig` | `rank` | verdict |
|---|---|---|---|
| `z²−1`, `(z−1)(z−2)`, `(z²−1)(z²−4)` | `2, 2, 4` | `2, 2, 4` | HYP ✓ |
| `z²+1`, `z²+z+1`, `(z²+1)(z−1)`, `(z²+1)(z²+4)`, `(z−1)((z+2)²+9)` | `0, 0, 1, 0, 1` | `2,2,3,4,3` | not hyp ✓ |
| **near-miss quartic** `X⁴+10X³+26X²+22X+3` | `2` | `4` | **not hyp ✓** (Turán passes it) |
| **`(z²−1)(z²+100)`** shielded | `2` | `4` | **not hyp ✓** (`L₁` fails it) |
| **`(z²−1)(z²−4)(z²+400)`** shielded | `4` | `6` | **not hyp ✓** (`L₁` fails it) |

Hermite's identity held in every case. So the project has **two complete instruments** — `Λ(p)` and `sig(Bezoutian)` — and by §0(3) that is not a coincidence: both are chamber invariants of `ℝ^d ∖ Δ_ℝ`, which is the only admissible kind.

**And this is what §2.4 becomes.** The `σ`-type is the conjugation action on the zero set; the Bezoutian signature computes that action *from the coefficients* by Newton's identities, without locating a zero. The project's own non-deformation-invariant topological detector, made computable, **is** Hermite's criterion. The circle closes, and it closes onto classical territory.

**(5) But brief §6.4 is not escaped, and the margin law is exact.** The certifying eigenvalue of the Bezoutian, with background roots `±1,±2,±3,±4` and one implanted pair of radius `y₀`:

`|λ_neg|/‖H‖ = 2.11e−7, 9.99e−9, 1.91e−9, 4.49e−10, 1.11e−10, 2.75e−11, 6.88e−12, 1.72e−12, 4.30e−13` for `y₀ = 2^{−1} … 2^{−9}`,

local exponents `4.40, 2.38, 2.09, 2.02, 2.006, 2.001, 2.0004, 2.0001` — **exponent exactly 2**, and `|λ_neg|/(‖H‖y₀²) → 1.8027e−6`. §6.4's identity holds for the complete detector as it did for every partial one.

**(6) `Ξ` itself, and §2.6 measured inside the detector.** At 140 digits with 24 moments, `sig(Bezoutian(J^{d,0})) = d` — i.e. `J^{d,0}` hyperbolic — for every even `d ≤ 24`, extending the brief's `d ≤ 14`. The margin:

| `d` | 2 | 6 | 10 | 14 | 18 | 22 | 24 |
|---|---|---|---|---|---|---|---|
| `\|λ_min\|/‖H‖` | `1.6e−2` | `1.4e−9` | `1.0e−16` | `6.1e−24` | `3.3e−31` | `1.7e−38` | `3.6e−42` |

`log₁₀` is linear in `d` with slope `−1.80`: **certifying `J^{d,0}` needs about `1.8d` digits.** Every finite `d` is certifiable and the cost is exponential in `d`, with no uniform margin at any `d`. That is brief §2.6 — the difficulty lives in the tail — now visible *inside the only known complete detector* rather than inferred from `Λ = 0`.

---

## 1. Where this leaves the reframed target

The target is now clean: **compute a chamber invariant of `Ξ`'s zero set without locating the zeros.** §0(3) says nothing else can work; §0(4) says the classical answer is the Bezoutian signature, which is computable from the moments; §0(6) says it certifies every truncation and never uniformly.

**Screen 8′ (rationality) can now be relocated, and this is the useful consequence.** For a polynomial with rational coefficients the Bezoutian is *automatically* rational — the Newton sums are integer polynomials in the coefficients. So brief §6.5's dichotomy ("no known object varies with `Ξ` **and** is defined over `ℚ`") is **not a defect of the form**. The form is in both classes by construction. The wall is that `Ξ`'s coefficients `b_m = 4M_{2m}/(2m)!`, `M_k = ∫Φ(u)u^k du`, have no known `ℚ`-structure.

> **The missing ingredient is arithmetic, not geometric.** No choice of manifold, group, dimension or moduli space supplies rationality of the moments of `Φ`. That is why every geometric construction in this project answered "yes" to exactly one half of §6.5 — the half it could reach.

Stated that way, §6.5 stops being a screen to run against future proposals and becomes a reason not to make geometric proposals at all.

---

## 2. What would actually move it, given §0(3)

Only two shapes remain admissible, and they are the two the subject already knows.

1. **A real chamber invariant of `Ξ` computed by other means.** Concretely: a proof that the infinite Bezoutian of `H(w) = Ξ(√−w)` is positive semidefinite, or that `Λ ≤ 0`. Both are equivalent to RH. This is the Jensen/Turán/Laguerre hierarchy and the de Bruijn–Newman programme — well-trodden, and by §0(3) it is *where the only admissible detectors live*, which is a reason to expect the traffic rather than to avoid it.
2. **Arithmetic input on the moments.** §1. Nothing in this project bears on it.

**And one thing that is now cheap and worth knowing.** §0(6) measures the margin for `J^{d,0}`. Griffin–Ono–Rolen–Zagier prove hyperbolicity of `J^{d,n}` for `n ≥ c e^d`. Measuring the Bezoutian margin as a function of **both** `d` and `n` would locate where their asymptotic regime begins numerically, and would say whether the `1.8d`-digit law is an `n = 0` artifact or uniform in `n`. That is a day's work, is purely instrumental, and does not require any new geometry.

---

## 3. Honesty notes

**Verified from a primary source:** §0(1). DHKM (2.52), (2.57), (2.61) and the remark after (2.58), read directly from the uploaded PDF. The derivation of (2.52) is theirs and takes four lines; the specialisation to quaternionic `c_i` at `N = 2` is mine and rests on their index convention. Memo 21's numerics remain the independent corroboration.
**Proved here:** §0(3)(a) and (b) are one-line topology (a locally constant function on a connected space is constant; the complement of a proper hypersurface in an irreducible variety is connected). (c) is standard. All three are **elementary — assume they are known**; the content is the classification they combine into, not any one of them.
**Measured:** §0(4) (Hermite on the test set), §0(5) (exponent 2, nine radii), §0(6) (`J^{d,0}` hyperbolic to `d = 24`, margin slope `−1.80`).
**Not a theorem:** §1's relocation of §6.5 is a reading, not a proof. It says no *known* geometric construction can supply rationality of the `M_k`; it does not prove none can.
**Correction to memo 23:** §2's option list should have had a fifth entry — re-scope to detection without equivariance, which is what happened. And its option (c) (continue as gauge theory on a base with cohomology) is now excluded as an *RH* route by §0(3)(a), independently of the bridge problem: cohomology of the base is a deformation invariant either way.
**What did not get done:** the charge-4 locus trace proposed in memo 21 §2. Under §0(3)(a) it cannot bear on RH, so it was not run.
