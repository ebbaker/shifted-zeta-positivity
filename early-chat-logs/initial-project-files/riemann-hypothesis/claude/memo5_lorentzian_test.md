# Testing the Hodge–Riemann Bridge: A Negative Result, and the Rank Obstruction It Exposes

*Working memo #5 — August 23, 2026. Tests the direction proposed in `memo4_geometric_reformulation.md` §8 (Conjecture I). Certified by `lab_lorentzian_test.py`.*

---

## 0. Result

**The bridge as conceived does not exist, and the reason is a rank mismatch that is worth more than the bridge would have been.**

In the setting relevant to Jensen polynomials, the Lorentzian / Hodge–Riemann signature condition reduces *exactly* to Newton's inequalities, i.e. to the **first Turán inequality**. Hyperbolicity implies it; it does not imply hyperbolicity; and the gap widens with degree. Since the first Turán inequality for `Ξ` is already a theorem (Csordas–Norfolk–Varga), the Lorentzian condition is not merely too weak in principle — in this case it is already known, and already known to be far from RH.

That answers the question the direction was chosen to answer, and it explains why the two literatures (Brändén–Huh Lorentzian polynomials; Griffin–Ono–Rolen–Zagier Jensen–Pólya) have never been connected: the signature condition points the wrong way.

What survives is sharper than what we started with. §3–§5.

---

## 1. The reduction, and why it is exact

Let `p(X) = Σ a_j X^j` have degree `d` and positive coefficients, and homogenise to the bivariate form `h(x,y) = y^d p(x/y)`. Then `p` is hyperbolic (all roots real) iff `h` is hyperbolic in Gårding's sense.

For a bivariate form with nonnegative coefficients, the Brändén–Huh Lorentzian condition is: every `(d−2)`-fold derivative is a `2×2` quadratic form with at most one positive eigenvalue, i.e. non-positive determinant. Writing the normalised coefficients
```
c_j := a_j / binom(d, j) ,
```
the `(d−2)`-fold derivatives run over consecutive triples and the condition is
```
c_j² ≥ c_{j−1} c_{j+1}     for all j = 1, …, d−1 ,
```
i.e. **log-concavity of the normalised coefficients = Newton's inequalities = the first Turán inequality.** (The support is an interval, so M-convexity is automatic and imposes nothing.)

So in the univariate setting the entire Lorentzian/Hodge–Riemann apparatus collapses to one classical inequality. That is the reduction; it is exact, not an approximation.

## 2. The test

`lab_lorentzian_test.py`, sampling log-concave normalised coefficient sequences directly (`c_j = exp(concave)`, so Newton holds by construction) and then testing hyperbolicity:

| `d` | Newton samples | also hyperbolic | fraction |
|---|---|---|---|
| 2 | 40000 | 40000 | 1.0000 |
| 3 | 40000 | 39992 | 0.9998 |
| 4 | 40000 | 39471 | 0.9868 |
| 5 | 40000 | 37759 | 0.9440 |
| 6 | 40000 | 35425 | 0.8856 |
| 7 | 40000 | 32856 | 0.8214 |
| 8 | 40000 | 30450 | 0.7612 |
| 9 | 40000 | 27802 | 0.6950 |
| 10 | 40000 | 25189 | 0.6297 |

**Control** (the implication that does hold): 20000 polynomials with prescribed real negative roots, checked against Newton — **0 violations**. So `hyperbolic ⟹ Newton`, as expected, and the failure is entirely in the converse.

**Explicit counterexample, smallest clean one found:**
```
p(X) = X⁴ + 10X³ + 26X² + 22X + 3
normalised c = (3, 5.5, 13/3, 2.5, 1)
Newton ratios c_j²/(c_{j−1}c_{j+1}) = 2.3269, 1.3657, 1.4423     — all ≥ 1, Newton holds
```
yet `p` has one conjugate pair of roots. Confirmed at 60 digits (`max|Im root| = 0.057499729`) and **independently by the trace form**: the `4×4` Hankel/trace form of `ℝ[X]/(p)` has exactly one negative eigenvalue and negative discriminant, matching Hermite. A second: `X⁵ + 13X⁴ + 24X³ + 21X² + 8X + 1`, Newton ratios `1.219, 1.148, 1.055, 2.817`, one conjugate pair with `max|Im| = 0.615`.

Note `d = 2` and `d = 3`: at `d = 2`, Newton *is* equivalent to hyperbolicity (`a_1² ≥ 4a_0a_2` is the discriminant), which is why the condition looks promising at first and why the failure only becomes visible at `d ≥ 3`. This is the trap the direction was designed to detect.

## 3. Diagnosis: it is a rank mismatch

Line up the three objects by the rank of the quadratic form each controls.

| condition | form | rank | strength |
|---|---|---|---|
| Lorentzian / Hodge–Riemann (bivariate) | Hessian after `d−2` derivatives | **2** | first Turán inequality |
| higher Turán inequalities | intermediate Hankel minors | `3, …, d−1` | intermediate |
| Hermite / trace form | trace form of `ℝ[X]/(p)` | **`d`** | ⟺ hyperbolicity |

Hyperbolicity of a degree-`d` polynomial is a **rank-`d`** signature condition. Lorentzian geometry supplies **rank-2** conditions. The gap between them is precisely the gap between the first Turán inequality and the full Hermite criterion — which is exactly the territory the Jensen–Pólya programme has to cross, and exactly what makes it hard.

So the failure is not that the analogy was loose. It is that the analogy was *rank-2*, and the problem is rank-`d`.

## 4. The question that survives, correctly posed

> **Is there a geometric object whose Hodge–Riemann relations in *all* degrees produce the full rank-`d` trace-form positivity, rather than only the rank-2 conditions?**

Two refinements make this concrete, and both come out of the failed test.

**(a) The target is a definite form on a quotient, not the Lorentzian form itself.** I had this wrong in memo 4 §8. A rank count kills the direct identification immediately: the trace form of `ℝ[X]/(p)` is *definite* when the hyperbolicity we want holds (signature `(d,0)`), whereas a Hodge-index form is *Lorentzian* (signature `(1, ρ−1)`); a definite form is not a Lorentzian one. But Weil's mechanism never identifies them either. There, the Lorentzian form on `NS(C×C)` induces, on the quotient by the degenerate correspondences (the hyperbolic plane `⟨f₁,f₂⟩`), a **positive definite** form — the Rosati form. So the correct target is:

> realize the trace form of `ℝ[X]/(p)` as the negated intersection form on the orthogonal complement of a hyperbolic plane inside a Lorentzian lattice.

That is a completely concrete lattice-theoretic statement, and it is the right shape: definite form of rank `ρ−2` sitting inside a Lorentzian lattice of rank `ρ`.

**(b) The rank count then rules out every fixed surface, and that is the real finding.** We need `ρ − 2 = d`, i.e. Picard number `ρ = d + 2` growing with the degree. But:
- an abelian surface has `ρ ≤ 4` (so `d ≤ 2`);
- `C × C` for `C` of genus `g` has `ρ = 2 + rk End(Jac C)`, generically `3` (so `d ≤ 1`);
- even a hyperkähler fourfold of `K3^[n]` type has `b₂ = 23`, hence `ρ ≤ 21`, so `d ≤ 19`.

Every *fixed* variety has bounded Picard number and therefore caps the degree. Since RH needs all `d`, **no single surface or fixed variety can supply the object. It has to be a tower of unbounded rank.**

This is a genuine narrowing, and it is the first time the hyperkähler material becomes load-bearing rather than decorative. A tower of growing-rank forms all controlled by one quadratic form is exactly what hyperkähler cohomology provides: by Verbitsky's theorem the subalgebra generated by `H²` is
```
SH ≅ Sym* H²(X,ℚ) / (x^{n+1} : q_X(x) = 0) ,
```
so the Hodge–Riemann relations in degree `k` are signature conditions on `Sym^k H²` — a tower of forms of growing rank, all governed by the single BBF form `q_X`, with the reduced LLV algebra `𝔰𝔬(3, b₂−3)` acting. Structurally that is the right shape. Whether it can be matched to the trace-form tower is now a well-posed question in lattice theory and representation theory rather than an analogy.

**The obstruction to check first, honestly.** The two towers grow at different rates: the trace-form tower has rank `d` in degree `d`, while `Sym^k H²` has rank `binom(b₂+k−1, k)`, growing polynomially in `k` of degree `b₂−1`. A match therefore cannot be an isomorphism of towers; at best the trace form is a distinguished sub-quotient in each degree. Identifying which sub-quotient — or proving none is available — is the next concrete step, and it is a finite computation in low degree.

## 5. Next actions

1. **Compute both towers explicitly for `d = 3, 4, 5`** and compare signatures, ranks, and available sub-quotients. Cheap, and it either produces a candidate or kills the shape.
2. **Test refinement (a) directly in the smallest case:** for a quartic `p`, is the rank-4 trace form realizable as the negated intersection form on the orthocomplement of a hyperbolic plane in *some* Lorentzian lattice of rank 6 — and if so, is that lattice the Néron–Severi group of anything? The lattice question is elementary; the geometric-realizability question is the content.
3. **Record the negative result.** The reduction of §1 and the counterexample of §2 are worth a short note in their own right: *the Lorentzian/Hodge–Riemann signature condition on Jensen polynomials is exactly the first Turán inequality, hence strictly weaker than hyperbolicity, with explicit counterexamples and a decay rate in the degree.* It closes a direction that looks attractive from both sides, which is a service to anyone else who notices the two literatures sitting next to each other.
4. **Do not** pursue Lorentzian polynomials further as a route to hyperbolicity of `Ξ`'s Jensen polynomials. The reduction of §1 is exact, so there is nothing left to hope for in that particular apparatus.

---

*Certified by `lab_hankel_check.py` (trace-form signature machinery) and `lab_lorentzian_test.py` (this memo: the reduction test, the decay table, the counterexamples, and the `hyperbolic ⟹ Newton` control). The high-precision confirmation of both counterexamples used mpmath at 60 digits with independent trace-form cross-check.*
