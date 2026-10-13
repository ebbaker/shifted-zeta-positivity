# Screening the Weil-Positivity Route

*Working memo #19 — August 24, 2026. Screens the one candidate memo 18 §5 left standing: Weil's explicit-formula positivity as the definition of `ζ` that natively supplies an inequality. Verdict in §0. Certified by `lab_weil_positivity.py`.*

---

## 0. Verdict

**Weil positivity passes every screen that killed the earlier directions, and it is still not a route this project can take — because it is a *criterion*, not a *mechanism*.**

Unpacked:

1. **It passes §2.1 and both corollaries** — the only universal no-go the project has. Weil positivity is an *inequality* and a **closed** condition. §2.1 excludes characterisations by vanishing; Corollary A excludes *open* conditions (genericity, non-degeneracy, slope stability). A closed condition with empty interior is exactly what the hyperbolic locus `H` is. **First candidate in the programme to clear both parities.**
2. **It is in the right variable.** Weil's form lives on `ℝ*_+` with the involution `g ↦ g^*`, `g^*(x) = \bar g(1/x)/x` — inversion. That is the multiplicative shape memo 18 §6 identified as the one the gauge machinery natively implements, and the first candidate here that is not in the additive/Jensen variable.
3. **And there is a real point of contact with our own results.** Bombieri–Lagarias require the zero multiset to be closed under `ρ ↦ \barρ` and `ρ ↦ 1−ρ`. Memo 18's **Theorem D** says that `C = λI` in the ADHM shape *forces* closure under `ρ ↦ λ/ρ` — which is `ρ ↦ 1−ρ` in the multiplicative variable. **The ADHM shape supplies the hypothesis of Bombieri–Lagarias for free.** That is the only place the project's machinery and the Weil route touch, and it is not nothing.
4. **§2.5, the rationality screen, bites exactly as it always has.** Ask the two questions of Weil's form: *(i) does it vary with `ζ`'s data?* **Yes** — emphatically, it is built from the primes. *(ii) Is it defined over `ℚ`?* **No** — the local terms carry `\log p` and `Γ'/Γ`. One out of two, like every other object the project has examined. And here the missing half is not an oversight: supplying a `ℤ`-structure for the adele class space *is* the open problem in Connes' programme. The project should not expect to resolve it as a side item.
5. **§1.2 is the decisive one, and it fails.** The programme's template needs a class `𝒞` with a **sphere-free theorem** and an independently verifiable membership condition. Weil positivity has no such class: the positivity *is* the RH statement, restated. There is nothing for the equivariance mechanism to bite on. **Adopting this route means abandoning the quaternionic/sphere apparatus that has been the project's engine and joining a different, heavily-worked programme.**
6. **No gauge-theoretic realisation exists.** A literature sweep found nothing connecting Weil's quadratic functional to a Yang–Mills energy, an index, or an eta invariant. That is consistent with memo 12 §0(5) ("no candidate transform carrying `Ξ`'s data to a YM field") and it is still true.

**But the screening produced a genuinely useful by-product**, and it belongs in the brief regardless of the verdict on the route:

> **The Li instrument is the second complete discriminant the project has, and the first one that is cheap.** On the §7 test set it detects every non-hyperbolic case, **including both shielded cases** — the ones built specifically to defeat `L_1` and the pointwise graded family. See §2.

And one clear negative that should stop anyone from reaching for `λ_n` at height:

> **The Li shadow degrades with height; `Λ` does not.** §3.

---

## 1. What Weil positivity actually says

**The explicit formula** (Connes–Consani's normalisation, read directly): for suitable test functions,

`f(i/2) − Σ_{1/2+iγ ∈ Z} f(ρ_γ) + f(−i/2) = Σ_v W_v(f)`,

`Z` the non-trivial zeros, `v` running over the places of `ℚ`.

**Weil's criterion.** `RH ⟺ Σ_v W_v(g ⋆ g^*) ≤ 0` for `g ∈ C_c^∞(ℝ*_+)` with `\hat g(±i/2) = 0`. (Sign conventions differ between sources; this is the one in Connes–Consani, which I read.) It is a quadratic form evaluated on convolutions `g ⋆ g^*` — i.e. **an algebra with a positive anti-involution**, which is exactly the algebraic shape brief §2.5 says a Weil-type argument needs.

**Li's criterion** (the countable shadow). `λ_n = \frac{1}{(n-1)!}\frac{d^n}{ds^n}[s^{n-1}\logξ(s)]\big|_{s=1} = Σ_ρ[1 − (1−1/ρ)^n]`, and `RH ⟺ λ_n ≥ 0` for all `n ≥ 1`. **Bombieri–Lagarias**: for any multiset closed under `ρ ↦ \barρ` and `ρ ↦ 1−ρ`, `Re ρ = 1/2` for all `ρ` ⟺ `λ_n ≥ 0` for all `n`. The Möbius map `s ↦ 1 − 1/s` carries the critical line to the **unit circle** — the same multiplicative picture as memo 18 §6.

---

## 2. The polynomial shadow, and the test-set run

For a real monic `p` of degree `k` with roots `ρ_j`, hyperbolicity is "all roots on `ℝ`". Take the Cayley map adapted to `ℝ` with a free base point `μ > 0`,

`w_j = (ρ_j − iμ)/(ρ_j + iμ)`,

which sends `ℝ` to the unit circle and carries complex conjugation to `w ↦ 1/\bar w`. Define

> `lam_n(p) := Σ_j Re[1 − w_j^n] = k − Re Σ_j w_j^n`.

**Proposition.** `lam_n(p) ≥ 0` for every `n ≥ 1` ⟺ `p` is hyperbolic.
*Proof.* (⇐) all `|w_j| = 1`, so `|Σ_j w_j^n| ≤ k`. (⇒) a non-real root forces a partner with `|w| > 1`; `Re(w^n)` reaches `≈ +|w|^n` along a subsequence, so `lam_n → −∞`. `∎`

**Run against §7.** `μ = 1/2` (mirroring Li's base point `s = 1`); `Λ` reimplemented from its definition and revalidated against every entry of the brief's table.

| `p` | `Λ` (normalised) | brief | `max|w|` | detect `n*` | `lam_{n*}` |
|---|---|---|---|---|---|
| `z²−1` (hyp) | `−5.000e−01` | `−0.5` | `1.00000` | none | `+1.4e−08` |
| `(z−1)(z−2)` (hyp) | `−3.125e−02` | `−0.031` | `1.00000` | none | `+1.7e−05` |
| `(z²−1)(z²−4)` (hyp) | `−3.352e−02` | `−0.034` | `1.00000` | none | `+3.4e−05` |
| `z²+1` | `+5.000e−01` | `0.5` | `3.00000` | **1** | `−1.333` |
| `z²+z+1` | `+3.750e−01` | `0.375` | `2.34752` | **1** | `−0.3077` |
| `(z²+1)(z−1)` | `+3.690e−01` | `0.369` | `3.00000` | **1** | `−0.9333` |
| `(z²+1)(z²+4)` | `+1.748e−01` | `0.175` | `3.00000` | **1** | `−1.600` |
| `(z−1)((z+2)²+9)` | `+2.554e−01` | `0.255` | `1.25911` | **6** | `−0.2722` |
| **near-miss quartic** | `+3.885e−05` | `3.88e−05` | `1.01935` | **43** | `−0.5521` |
| `(z²−1)(z²+100)` **shielded** | `+1.699e−01` | `0.170` | `1.10526` | **7** | `−0.4682` |
| `(z²−1)(z²−4)(z²+400)` **shielded** | `+1.008e−01` | `0.101` | `1.05128` | **13** | `−0.1926` |

Three things worth recording.

- **It catches the shielded cases, cheaply.** `n* = 7` and `13`. Those two were constructed precisely because "some other zero is always closer to every real point", which defeats `L_1` and the whole pointwise graded family `Σ_ρ(x−ρ)^{−2m}`. **Li is not a pointwise criterion** — it is a statement about the multiset of Cayley images — so shielding has no purchase on it. That is a structural immunity, not luck.
- **It catches the near-miss quartic** at `n* = 43`, i.e. it is strictly stronger than Turán (which the quartic passes) and than `L_1`.
- **It has no margin on the hyperbolic side.** For hyperbolic `p` all `|w_j| = 1`, so `lam_n = k − Re Σ w_j^n` and `n·θ` equidistributes: `inf_n lam_n = 0`, never attained. The controls reach `1.4e−08` by `n = 20000`. So `Λ` is a *signed distance* and Li is a *one-sided* test — an important difference in kind if either is to be used as a discriminant.

---

## 3. Instrument comparison at height — the §2.6 question

`Λ` and Li are both non-uniform (§2.4 is respected: at fixed `n`, `lam_n` for `p = z²+y_0²` is a constant multiple of `y_0²`, the ratio converging to `−1600` at `n = 10` as `y_0 → 0`). The interesting difference is in **height**.

Take a conjugate quadruple at height `±a` with off-line part `b`: `p = ((z−a)²+b²)((z+a)²+b²)`.

| `a` | `b` | `Λ` | `log max|w|` | `n*` | `lam_{n*}` |
|---|---|---|---|---|---|
| 1 | 0.1 | `4.976e−03` | `7.95e−02` | 7 | `−5.74e−01` |
| 3 | 0.1 | `4.997e−03` | `1.08e−02` | 19 | `−8.41e−02` |
| 10 | 0.1 | `5.000e−03` | `9.97e−04` | 63 | `−7.66e−03` |
| 30 | 0.1 | `5.000e−03` | `1.11e−04` | 188 | `−2.83e−04` |
| 100 | 0.1 | `5.000e−03` | `1.00e−05` | 628 | `−5.78e−05` |
| 10 | 0.01 | `5.000e−05` | `9.98e−05` | 377 | `−9.65e−04` |

> **`Λ` is height-independent** — `b²/2` throughout, confirming §2.4's universality claim in a case the brief did not test. **Li is not.** The Cayley image of a zero at height `a` sits only `≈ b/a²` off the unit circle, so the detection order grows like `a` and the depth at detection collapses like `b/a²`.

**Consequence, and it is the practical point of this memo.** As a *fixed global sequence*, `λ_n` is the wrong instrument for the regime §2.6 says is hard. To detect a violation at height `T` one needs `n ≳ T²/b` — which is why Li coefficients are useless for numerical verification of RH at height, and why they cannot answer §2.6 either. **The escape is the test-function form**: in `Σ_v W_v(g⋆g^*) ≤ 0` one *chooses* `g`, and can localise it at height `T`. That is a real structural advantage of Weil positivity over its own countable shadow, and it is the reason to quote the continuous criterion rather than `λ_n`.

---

## 4. The screens, one by one

| screen | verdict |
|---|---|
| **§1.1** equivariance identity | not engaged — Weil positivity is not an equivariant-object statement |
| **§1.2** class + sphere-free theorem + verifiable membership | **FAILS.** No class, no sphere-free theorem. It is the conclusion restated, not a mechanism |
| **§2.1** equations cannot cut out hyperbolicity | **passes** — an inequality, not a vanishing condition |
| **§2.1 Cor. A** genericity/openness excluded | **passes** — a *closed* condition; this is where slope stability died |
| **§2.1 Cor. B** Griffiths obstructions | not applicable |
| **§2.2** slice restriction carries no information | not applicable |
| **§2.3** deformation invariants weight a sphere by 2 | **passes** — the form varies continuously with the zeros; it is not a characteristic number |
| **§2.4** no uniform separation | **respected** — quadratic in the sphere radius at fixed `n` (measured) |
| **§2.5** rationality, two questions | **(i) yes, (ii) no.** One out of two, as always. Caps what it can prove |
| **§2.6** the difficulty is at `T → ∞` | **the `λ_n` shadow fails** (§3). The test-function form is the right object and is not finite-dimensional, so it passes *in kind* |
| **Screen 0″** positivity audit (procedure, per memo 18) | drop everything else and ask whether the positivity alone forces the conclusion: here it *is* the conclusion, so the audit returns "circular by construction" — but that is what a criterion is, not a defect |

---

## 5. Where this leaves the programme

**The honest summary.** Weil positivity is a live route to RH — the live route, pursued by Connes and Consani for twenty-five years — and it is a route in the correct variable, with the correct algebraic shape, that clears the one universal no-go this project owns. It is also a route to which **the sphere mechanism contributes nothing**, because there is no class for a sphere-free theorem to be about. The project can adopt it only by becoming a different project.

**What is worth keeping regardless of that decision:**

1. **Add the Li instrument to §7.** It is complete on the test set, structurally immune to shielding, and cheap. It should sit beside `Λ` in the instrument list, with the caveats in §2 and §3 attached: one-sided, no margin on the hyperbolic side, and height-degrading.
2. **`Λ` is height-independent.** Measured here for the first time (§3). This strengthens §2.4 and is worth stating in the brief.
3. **Theorem D supplies the Bombieri–Lagarias hypothesis.** The single point of contact. If anyone later wants a gauge-theoretic object with a Li/Weil-shaped criterion attached, the ADHM shape with `C = λI` already enforces the functional-equation closure that criterion requires. That is a fact about our own construction, and it was not visible before memo 18 §6.

**What I would *not* do:** try to realise Weil's quadratic functional as a Yang–Mills energy. There is no candidate in the literature, no candidate here, and the shape mismatch is severe — the form lives on test functions on the idele class group, and the gauge energy lives on connections. Building the bridge is the whole of the open problem, not a step in it.

---

## 6. References

**Read directly for this memo:** Connes–Consani (the Selecta PDF), the Li-criterion statements on Wikipedia and MathWorld, and Nazardonyavi–Yakubovich (arXiv:1304.7895) for the generalised Bombieri–Lagarias statement.
**Cited but not read:** Li 1997, Bombieri–Lagarias 1999, Weil 1952, Bombieri 2000, Connes 1999. The `λ_n`/Bombieri–Lagarias statements above were cross-checked against two independent secondary sources and re-derived in the polynomial shadow from scratch, but the primary papers should be read before any of this is circulated.

- X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory **65** (1997) 325–333.
- E. Bombieri, J. C. Lagarias, *Complements to Li's criterion for the Riemann Hypothesis*, J. Number Theory **77** (1999) 274–287.
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Univ. Lund (1952).
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I*, Rend. Accad. Naz. Lincei (2000).
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. **5** (1999) 29–106.
- **A. Connes, C. Consani, *Weil positivity and trace formula, the archimedean place*, Selecta Math. **27** (2021), arXiv:2006.13771.** — read directly; the source for §1's statement of the criterion, the support conditions on `g`, and the Sonin-space compression results.
- S. Nazardonyavi, S. Yakubovich, *Generalized Bombieri–Lagarias' theorem and generalized Li's criterion*, arXiv:1304.7895.

---

## 7. Honesty notes

**Proved here:** the Proposition of §2 (the polynomial shadow is a complete criterion). Elementary.
**Measured here:** everything in the §2 and §3 tables, at 60 digits. `Λ` was reimplemented from its definition and reproduces all eleven brief §7 entries, which is an independent revalidation of the brief's own table.
**Asserted on secondary sources:** the exact form of Li's criterion and of Bombieri–Lagarias. See §6.
**Not established:** any connection between Weil's quadratic functional and a gauge-theoretic energy. Searched for; nothing found. This memo makes no claim that one exists.
**A correction to my own working:** an earlier run of the §7 table used `z³+3z²+5z−13` for `(z−1)((z+2)²+9)`, which is `z³+3z²+9z−13`. The table above is the corrected run and matches the brief exactly.

---

## 8. What "joining the programme" would mean, and one update to §2.5

### 8.1 The architecture, and the specific gap

Weil's function-field proof needs: a smooth projective curve `C` over `𝔽_q`; the surface `\bar C × \bar C`; the graph of Frobenius as a divisor; **Riemann–Roch on the surface**; and the resulting positivity `D·D ≤ 0` for degree-zero divisors. The explicit formula becomes an intersection-theory identity, with the right-hand side the intersection with the diagonal.

For `ℚ`, Connes and Consani propose the adele class space `X_ℚ = ℚ^× \ 𝔸_ℚ / \hat ℤ^×`, realised as the points of the **arithmetic site** `(ℕ^×, ℤ_max)` and its extension the **scaling site** over `ℝ^max_+`. The trace formula on `X_ℚ` reproduces Weil's explicit formula, with the zeros appearing as an *absorption* spectrum.

The missing ingredient, in Connes' own words:

> "At this point, what is missing is an intersection theory and a Riemann–Roch theorem on the square of the arithmetic site."

with two named obstructions: the archimedean distribution `κ(u)` violating the monotonicity `N(q) ≤ N(q^r)` expected of a counting function, and the absence of Serre duality / any adequate `H^j` for `j ≠ 0`. Riemann–Roch holds on the scaling site for individual tropical curves; it is the **square** that is missing. The line of work is very much live — *Riemann–Roch for Spec ℤ* (2023, 2024), *On the Jacobian of Spec ℤ* (2026), *On the absolute geometry of Spec ℤ* (2026), *Zeta zeros and prolate wave operators* (2025), *Zeta spectral triples* (with Moscovici, 2026).

### 8.2 Does this project add anything to it?

**On the bottleneck: no.** The gap is intersection theory and Riemann–Roch in characteristic one. This project has never built a cohomology theory, never worked with the adele class space, and has no characteristic-one geometry. Its three assets do not reach:

- the **equivariance/sphere mechanism** has no role — there is no equivariant object and no sphere;
- the **no-go screens** (§§2.1–2.6) are about the *matching* strategy — attaching a finite-dimensional gauge object to a polynomial proxy for `Ξ` — and say nothing about spectral realisations;
- the **instruments** (`Λ`, Jensen, and now Li) are standard and are not what is blocking anyone.

Adopting the route would mean starting the relevant expertise from zero on a problem that two very strong people have worked for twenty-five years. That is a legitimate choice, but it is a change of project, not a continuation.

### 8.3 The one thing that is new — and it is a correction to our own books

Brief §2.5 states: *"No known object is in both classes"* — geometric forms are integral but rigid; forms carrying `Ξ`-dependence have no `ℚ`-structure. **Memo 18's Theorem C makes that false.** Verified exactly:

- The frame `M_1, M_2, M_3, J` consists of **integer** `4×4` matrices; the `ℤ`-algebra they generate has rank `8` in `M_4(ℤ)` and is closed under multiplication — an **integral order**.
- The **transpose is a positive anti-involution** on it: `M_aᵀ = M_a`, `Jᵀ = −J`, `tr(XXᵀ) > 0`.
- The parameters lie in `ℤ[i]` inside the commutant. At `z = 3+i`, `w = 3−i`: every one of `T_0, T_1, T_2, T_3, C` is an **integer matrix**, `C = 16·I₄` is integral and positive definite, and `p(u) = u⁴ − 12u³ + 72u² − 192u + 256 ∈ ℤ[u]`.
- And the datum **varies**: `(z,w)` gives a 3-parameter family, over which `p` sweeps a 3-dimensional set.

So this is an object in **both** of §2.5's classes: an integral order with a positive anti-involution, a definite integral form, *and* genuine dependence on the polynomial. That is the configuration §2.5 says nobody has.

**And it does not help — which is the point.** The definiteness available is `λ = z²+w² > 0`, which holds on the *whole* family, while the RH-shaped conclusion (`|ρ| = √λ`, i.e. all roots on the circle) holds only on the sub-family `b = τ = 0`, i.e. `z, w ∈ ℤ ⊂ ℤ[i]` — equivalently, by memo 18 §6, exactly where the blocks are symmetric:

| `z` | `w` | `λ` | roots | `|ρ|² = λ`? |
|---|---|---|---|---|
| `3+i` | `3−i` | 16 | `4±4i, 2±2i` | **no** |
| `3` | `3` | 18 | `3±3i` | yes |
| `5` | `1` | 26 | `5±i` | yes |

> **Definiteness of the integral form does not select the RH locus.** §2.5's screen should be restated: being in both classes is *necessary* and demonstrably *not sufficient*, and the obstruction is not rationality — it is that the natural positivity is orthogonal to the conclusion. That is memo 18's lesson again, now in the one place where Weil's algebraic prerequisites are all actually met.

This is a contribution to *this* project's bookkeeping. It is not a contribution to Connes' programme, and it should not be advertised as one.
