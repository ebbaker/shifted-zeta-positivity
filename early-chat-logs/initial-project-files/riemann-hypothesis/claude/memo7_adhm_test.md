# The ADHM Test: Noncommutativity Is Available, and the Dictionary Destroys It

*Working memo #7 — August 23, 2026. Runs the test proposed after memo 6: does the ADHM construction supply the noncommutative algebra with a positive involution that memo 6 §4 found missing, and is the resulting positivity non-circular? Certified by `lab_adhm_check.py`.*

---

## 0. Result

Two questions were posed. They split.

**(a) Does the algebra fail to commute? YES.** The ADHM variety is richly noncommutative at every charge `k ≥ 2`, and the positivity it carries is structural rather than assumed. This is the first object in this program with the algebraic shape memo 6 §4 said was absent.

**(b) Is the positivity non-circular? NO — and now provably so.** Theorem §4: matching the real jumping locus to the zero set of a slice extension forces `λ = 0` and `T₁ = T₂ = T₃ = 0`, collapsing the data onto the **commutative real locus** of the ADHM variety, after which "`p` hyperbolic" is the spectral theorem for real symmetric matrices. Confirmed on 12 cases, including a correct NO for the memo-5 quartic that passes the Newton/Turán test. The proof does not use the nonlinear ADHM equations at all — the collapse is forced by the *linear* part of the reality condition, i.e. before the interesting structure is consulted.

So the noncommutativity is real but the dictionary annihilates it. Memo 6 §4 stands, re-derived from the gauge-theory side, and sharpened: **the obstruction is not that a noncommutative algebra with a positive involution is unavailable — it is that pinning the jumping locus to a slice-extension zero set is exactly the condition that kills the noncommutative directions.**

---

## 1. Why this dictionary and not another

Both sides are the canonical objects of their theories; nothing here was reverse-engineered to produce the answer.

**Upstairs.** Atiyah's quaternionic normal form for charge-`k` `SU(2)` ADHM data is

```
Δ(q) = [ T − qI_k ; λ ] ,      T ∈ H^{k×k},  λ ∈ H^{1×k},
```

with the ADHM condition that `Δ†Δ` be **real**, and regularity — the bundle is a genuine instanton — the condition that `Δ†Δ` also be **nonsingular for every q ∈ H**. That second condition is precisely *no real jumping lines*. So the real jumping locus is exactly `Z(det Δ†Δ) ⊂ H`.

**Downstairs.** For a monic real `p` of degree `k`, the zero set of the slice extension `R p` in `H` — real roots as isolated points, conjugate pairs as 2-spheres — is exactly the zero set of

```
P_p(q) := p(x₀ + i r) p(x₀ − i r) ,      r = |Im q| .
```

The invariant of `twistor_lift_computation.md` §3 is the `σ`-action on the components of a divisor in the space of lines; the ADHM reality condition is a `σ`-condition on the components of the jumping divisor. Same space, same type of invariant, opposite polarity. The question is therefore forced:

> For which `p` does there exist admissible ADHM data with `det(Δ†Δ) = P_p`?

## 2. What reality forces (derived, not assumed)

Expanding `Δ†Δ = (T − qI)†(T − qI) + λ†λ` with `T = T₀ + T₁i + T₂j + T₃k` and requiring the three imaginary blocks to vanish identically in `q` gives, symbolically for `k = 2, 3`:

- the terms **linear in `q`** vanish iff every block `T_a` is real **symmetric** (8 conditions at `k=2`, 24 at `k=3`, each of the form `T_a[i,j] − T_a[j,i] = 0`);
- the **`q`-independent** terms give the classical nonlinear equations
  ```
  [T₀,T_a] − ε_abc [T_b,T_c] + Im_a(λ†λ) = 0 ,     a = 1,2,3.
  ```

With those imposed,

```
Δ†Δ = M(q) = C + |q|² I − 2 Σ_a x_a T_a ,     C = Σ_a T_a² + Re(λ†λ) ⪰ 0.
```

`C` is a sum of squares of symmetric matrices plus a Gram matrix: **the positivity is automatic**, not an extra hypothesis. That is exactly the feature that made this worth testing.

## 3. Test (a): the variety is noncommutative

Exact witness at `k = 2`:

```
T₀ = [[0,1],[1,0]],  T₁ = diag(1,−1),  T₂ = T₃ = 0,  λ = (1, 2i)
```
satisfies all three ADHM equations exactly (residual `0.0`), with `[T₀,T₁] = [[0,−2],[2,0]] ≠ 0`. The `λ†λ` term is what makes this possible: with `λ = 0` and `k = 2` the Plücker relation forces all commutators to vanish, so the imaginary part of the `λ`-Gram is the genuine source of noncommutativity at low charge.

Census: solving the ADHM equations alone from 120 random starts gives 120/120 exact solutions at `k = 2, 3, 4`, with largest normalised commutator `max_ab |[T_a,T_b]| / |T|²` equal to `1.453, 1.611, 1.360` respectively. The noncommutative locus is not a measure-zero curiosity; it is generic.

## 4. Test (b): the theorem

> **Theorem.** Let `Δ = [T − qI ; λ]` with `Δ†Δ` real, and suppose
> `det(Δ†Δ)(q) = P_p(q)` for a monic real `p` of degree `k ≥ 1`.
> Then `λ = 0`, `T₁ = T₂ = T₃ = 0`, `T = T₀` is real symmetric, and
> `p = det(zI − T₀)`. In particular **`p` is hyperbolic**.

*Proof.* By §2, `M(q) = C + |q|²I − 2Σ x_a T_a` with all `T_a` real symmetric and `C = Σ_a T_a² + Re(λ†λ) ⪰ 0`. Restrict `q` to a slice `Π_e = {x₀ + y e}` for a unit imaginary `e`, continue `y → iη` (both sides are polynomials, so the identity persists), and set `u = x₀ + η`, `v = x₀ − η`. Then `|q|² → uv`, `P_p → p(u)p(v)`, and

```
det( uv·I − u·N − v·N̄ + C ) = p(u) p(v) ,        N = T₀ + i T_e .
```

The `uᵏvᵏ` coefficient is `1` on both sides. The `uᵏ` leading coefficient in `u` gives `p(v) = det(vI − N)`, and likewise `p(u) = det(uI − N̄)` — so `p` is the characteristic polynomial of `T₀ + iT_e` **for every unit `e`**. Comparing the coefficient of `u^{k−1}v^{k−1}`, which equals `tr C + tr N · tr N̄ − tr(N N̄)` on the left and `tr N · tr N̄` on the right,

```
tr C = tr(N N̄) = tr T₀² + tr T_e²        for every unit e.
```

The left side does not depend on `e`, so the quadratic form `e ↦ tr T_e² = Σ_ab e_a e_b tr(T_a T_b)` is constant on `S²`, forcing `tr(T_a T_b) = κ δ_ab` for `a,b ≥ 1` and `tr T_e² = κ`. But `tr C = tr T₀² + 3κ + ‖λ‖²`. Hence

```
3κ + ‖λ‖² = κ ,   i.e.   2κ + ‖λ‖² = 0 ,
```

and both terms are non-negative, so `κ = 0` and `λ = 0`. For a real symmetric matrix `tr T_a² = 0` forces `T_a = 0`, so `T₁ = T₂ = T₃ = 0`. Then `C = T₀²` and

```
det(Δ†Δ) = det( (T₀ − x₀I)² + r² I ) = Π_j [ (x₀ − τ_j)² + r² ]
```

with `τ_j` the eigenvalues of the real symmetric `T₀`, hence real. Matching against `P_p = Π_m [ (x₀ − ρ_m)² + r² ]` gives `{ρ_m} = {τ_j}`. ∎

(Note for exposition: when `p` has non-real roots the individual factors `(x₀−ρ_m)² + r²` are complex; only the product is real. Nothing in the argument depends on the factors being real.)

**Independently verified, and stronger than first stated.** An adversarial review pass reproduced every step and returned three strengthenings:

1. **`k ≥ 2` is not needed** — the coefficient formula and the whole chain hold at `k = 1`.
2. **The nonlinear ADHM equations are never used.** Only the *linear* part of the reality condition — symmetry of the four blocks — plus the shapes of `M` and `C` enter. The true statement is: for *any* real symmetric `T₀,…,T₃` and *any* `λ ∈ H^{1×k}`, with `C := Σ T_a² + Re(λ†λ)` and `M := C + |q|²I − 2Σ x_a T_a`, the identity `det M ≡ P_p` forces `λ = 0`, `T₁ = T₂ = T₃ = 0`, `p = det(zI − T₀)`. This is the sharpest form of the bad news: **the collapse is forced before the interesting equations are consulted.**
3. **Three slices suffice, not the sphere.** Summing the §4 relation over the three orthogonal directions `e = i, j, k` and using `tr T_e = 0` (itself part of step 3) gives the obstruction directly, so step 5's spherical-invariance argument is convenient but superfluous.

Symmetry of the `T_a` is load-bearing in exactly one place — `κ = ‖T₁‖_F² ≥ 0` — and fails for general real matrices. Positive semidefiniteness of `C` is *not* needed anywhere.

Machine verification: reality conditions and ADHM equations symbolically at `k = 2, 3`; the substitution of step 2 exactly at `k = 3`; the `u^{k−1}v^{k−1}` coefficient formula for arbitrary unrelated `B₁,B₂,B₃` at `k = 1,…,6`; steps 3 and 4 numerically on solved data (`|charpoly(T₀+iT_e) − p| ≈ 2e−12`, `tr C − tr T₀² − tr T_e² ≈ 6e−12`). Plus an **exact certificate at `k = 2` for symbolic monic `p`** (`lab_adhm_certificate.py`): the 31 coefficient equations contain 16 affine-linear ones with a unique elimination branch, and modulo those,

```
S := 2 Σ_{a≥1} tr T_a²  +  3‖λ‖²
```

is an exact rational linear combination of four of the remaining coefficient equations. Since `S` is a positive-definite quadratic form in the entries of `T₁,T₂,T₃,λ`, that is a self-contained machine proof for `k = 2` and every real monic `p`, independent of the narrative above. The `k = 3` analogue built its 109-equation system with a unique linear branch but the final ideal-membership solve did not finish in the time available — inconclusive, not negative.

## 5. Numerical confirmation

Global search (40 random starts, residual = ‖ADHM equations‖ + ‖det M − P_p‖/scale):

| k | p | hyperbolic | best residual | \|T₁..₃\| |
|---|---|---|---|---|
| 2 | `z²−1` | yes | 6.2e−15 | 9.5e−16 |
| 2 | `z²+1` | **NO** | 3.044 | 5.6e−02 |
| 2 | `(z−1)(z−2)` | yes | 2.2e−14 | 1.2e−14 |
| 2 | `z²+z+1` | **NO** | 1.752 | 3.9e−02 |
| 3 | `(z−1)(z−2)(z−3)` | yes | 6.8e−13 | 3.9e−12 |
| 3 | `(z²+1)(z−1)` | **NO** | 2.985 | 2.0e−01 |
| 4 | `(z²−1)(z²−4)` | yes | 9.2e−13 | 4.7e−13 |
| 4 | `(z²+1)(z²−1)` | **NO** | 0.558 | 1.3e−01 |
| 4 | `X⁴+10X³+26X²+22X+3` (memo 5) | **NO** | 1.0e−03 | 5.2e−03 |
| 2 | `J^{2,0}` of Ξ | yes | 7.2e−15 | 6.6e−15 |
| 3 | `J^{3,0}` of Ξ | yes | 2.4e−13 | 2.5e−12 |
| 3 | `J^{3,1}` of Ξ | yes | 2.3e−13 | 2.3e−12 |

Existence tracks hyperbolicity on all 12 cases, and on every solved case the data lands on `T₁ = T₂ = T₃ = 0`, `λ = 0` (max `|T₁..₃| = 3.9e−12`, max `|λ| = 1.1e−06`) — the theorem's conclusion, found independently by the optimiser.

Moments validated as before: `4M₀ = 0.4971207782` against `ξ(½) = 0.4971207174`, rel. err. `1.2e−07`.

An independent counterexample hunt was also run over the *larger* space in which the nonlinear ADHM equations are **not** imposed — strictly bigger than the theorem permits — at `k = 2,…,5`, on `z²+1`, `(z−1)²+1`, `(z−2)(z²+1)`, `z(z²+1)`, `(z²+1)(z²+4)`, `(z−1)(z−2)(z²+1)`, `z(z²−1)(z²+1)`. Relative residual floors `6e−03` to `2e−01`; hyperbolic controls `1e−15` to `7e−13` with `T₁,T₂,T₃` and `λ` driven to `~1e−06`. Ten to twelve orders of magnitude separate the two regimes in every case.

The memo-5 quartic is the informative row. Its conjugate pair sits at imaginary part `±0.0088` after normalisation — barely non-hyperbolic — and it **passes** the Newton/first-Turán test (`Σρ² = e₁² − 2e₂ = 1.130 > 0`). The ADHM matching nonetheless returns NO, with a residual floor of `1.0e−03`: ten orders above the hyperbolic cases, and continuously degrading with sphere radius, exactly the `j_ℓ(λy₀) → 0` behaviour predicted in `twistor_lift_computation.md` §5a and §6. So the ADHM condition is *strictly stronger* than the Turán hierarchy — but only because it is equivalent to the conclusion.

## 6. Where the discriminating power sits

Worth recording, because it is the one positive structural finding. Matching only on the **real axis** is satisfiable for non-hyperbolic `p`: take `k = 2`, `T₀ = 0`, `T₁ = diag(1,−1)`, `T₂ = T₃ = 0`, `λ = 0`, so `C = I` and

```
det M(x,0,0,0) = (x² + 1)²        for p = x² + 1, NOT hyperbolic.
```

More than that: this datum agrees with `P_p` on the **entire 2-plane** `{x₂ = x₃ = 0}` (max difference `1.8e−15`). It is simply the `x₀ ↔ x₁` rotation of the `p = x² − 1` solution, and a single slice cannot tell which axis is the real one. Moving to a different slice at the same `(x₀, r)` breaks it immediately (max difference `1.96`).

So the discriminating power is not "off the real axis" — it is **off any single slice**. It is carried by the full 2-sphere of complex structures. That is the same conclusion the appendix reached from the uniqueness side and the twistor note reached from the divisor side, now visible in a third, independent setting.

And axial symmetry alone is strictly weaker than the matching condition, which is worth recording because it was the obvious thing to try. Take `k = 4` and a real-symmetric anticommuting Clifford triple `T_a² = I` (`a = 1,2,3`), `T₀ = 0`, `λ = 0`, so `C = 3I`. Then (`lab_adhm_clifford.py`)

```
det M = [ (x₀² + (r−1)² + 2)(x₀² + (r+1)² + 2) ]² ,
```

a genuine polynomial in `(x₀, r²)` — it passes the obvious invariance test — yet it is not of the form `Π((x₀−ρ)² + r²)`: matching would force `ρ₁+ρ₂ = 0` and `ρ₁²+ρ₂² = 2`, hence `ρ₁ρ₂ = −1`, against the constant term's demand `ρ₁ρ₂ = +1`. It also fails the §4 relation directly: `tr C = 12` but `tr T₀² + tr T_e² = 4`. Note this ansatz *violates* the nonlinear ADHM equations (anticommuting `T_a` make `Im(T†T) ≠ 0`), which is a second reason it is excluded — but the point stands that the sphere-shape condition is doing work beyond axial symmetry.

## 7. What this does and does not change

**Changed.** Memo 6 §4's diagnosis was "the input supplies a commutative algebra with trivial involution, so the positivity is the conclusion." That was correct but under-explained: it left open whether a better-chosen input would supply noncommutativity. It would — ADHM does, generically. The real obstruction is one level down: **the requirement that the geometry's degeneracy locus be the zero set of a slice extension is itself a rigidity condition, and it is strong enough to force the geometry back onto its commutative locus.** Any construction that attaches a geometric object to `Ξ` by matching zero loci should now be expected to fail this way, and can be tested for it cheaply — compute what the matching forces, before computing what the positivity gives.

**Unchanged.** Memo 6 §3 and §6 are untouched. Even had the test come out the other way, the entries of any ADHM data built from `Ξ` are moments of `Φ`, and rationality — not finiteness, not noncommutativity — is the missing half of the only mechanism known to prove such positivities. Nothing here bears on that.

**Also unchanged:** the softness findings. Charge `k` and the degree of the jumping divisor are deformation invariants, and `twistor_lift_computation.md` §4 already showed that homology class and quaternionic winding both weight spheres by 2. The route was always going to have to land on the `σ`-equivariant component type, and that is precisely what the theorem shows cannot be reached by this dictionary.

## 8. Assessment

The test was worth running and it returned a clean, proved answer in one session, which is the outcome that was hoped for: the strongest remaining hope for circumventing memo 6 §4 is now closed by a theorem rather than by a heuristic.

What would have to be different for a gauge-theoretic route to survive: the correspondence between `Ξ` and the geometric object would have to be something other than an equality of zero loci — a *transform* rather than a *matching*, in the same sense that the Fueter map is a transform rather than an extension (appendix §4, Corollary A.11). Every matching-style dictionary tried in this program has now failed for the same structural reason, three times over and from three independent directions. That is a strong enough pattern to treat as a general finding rather than a run of bad luck.

`PROGRAM_CLOSED.md` stands, and its item 5 is strengthened: the commutative-case circularity is no longer just a property of the input, it survives replacing the input by the most promising noncommutative alternative.

**On the §4 theorem's novelty: assume it is known until checked.** `PROGRAM_CLOSED.md`'s novelty lesson applies with force here. The statement is a rigidity result about determinantal representations of real polynomials by symmetric pencils, and that circle of ideas is heavily worked — the classical direction (a definite symmetric determinantal representation forces hyperbolicity) is the content of the Lax conjecture and Helton–Vinnikov, and quaternionic-ADHM linear algebra has been studied since 1978. Our statement is a converse-flavoured rigidity within a specific pencil family, which is exactly the kind of thing that turns out to be a corollary of something in the literature. It has **not** been novelty checked. Treat it as an internal certification of a no-go, not as a result. If it were ever to be checked, the sweep should cover: Helton–Vinnikov and the Lax conjecture literature; determinantal representations of hyperbolic polynomials; Atiyah's *Geometry of Yang–Mills Fields* and the ADHM regularity condition; and real jumping lines / Barth's theorem.

---

*Certified by `lab_adhm_check.py` (quaternionic matrix algebra with cross-checked symbolic and numeric layers; reality conditions and ADHM equations derived symbolically at k = 2, 3; noncommutativity census; the identity chain of §4 verified symbolically and numerically; 12-case existence search), with `lab_adhm_certificate.py` (exact ideal-membership certificate at k = 2 for symbolic monic p) and `lab_adhm_clifford.py` (the axially-symmetric-but-unmatchable Clifford ansatz of §6). The theorem of §4 is a proof, not a computation; it was reproduced and strengthened by an independent adversarial review pass, which found no counterexample in a search space strictly larger than the theorem's hypotheses.*
