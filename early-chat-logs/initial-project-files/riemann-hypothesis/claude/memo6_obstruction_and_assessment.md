# The Obstruction, Checked; and an Assessment of the Program

*Working memo #6 — August 23, 2026. Completes the check flagged in `memo5_lorentzian_test.md` §5, and answers the question of whether the geometric program should continue. Certified by `lab_tower_check.py`.*

---

## 0. Result of the check

The obstruction is real, and it is worse than a rank count. Three findings, in increasing order of severity.

1. **The hyperkähler tower's rank spectrum is sparse.** It supplies a definite form at only 7 of the first 40 ranks.
2. **The realization target is vacuous over ℝ.** Signature is a complete invariant of a real quadratic form, so "realize the trace form geometrically" asks for nothing.
3. **In the commutative case the mechanism is circular.** "The trace form of a commutative algebra with trivial involution is definite" *is* the statement that the algebra is totally real — i.e. the conclusion, not a consequence of anything.

Finding 3 is decisive, is independent of every geometric choice, and explains at a deeper level than the earlier diagnoses why every conjecture in this program came out RH-trivial or RH-orthogonal. §4.

---

## 1. The rank spectrum of the hyperkähler tower

By Verbitsky, `SH^{2k} = Sym^k H²` for `k ≤ n`, and the harmonic decomposition with respect to `q_X` gives `Sym^k V = ⊕_j q^j · H^{k−2j}` with
```
dim H^m = C(b+m−1, m) − C(b+m−3, m−2),    b = b₂ .
```
The Hodge–Riemann relations are definite exactly on the primitive pieces `H^m`, so these are the ranks at which the tower supplies a definite form. For the four known deformation types:

| type | `b₂` | `dim H^m`, `m = 0…9` |
|---|---|---|
| `Kum_n` | 7 | 1, 7, 27, 77, 182, 378, 714, 1254, 2079, 3289 |
| `OG6` | 8 | 1, 8, 35, 112, 294, 672, 1386, 2640, 4719, 8008 |
| `K3^[n]` | 23 | 1, 23, 275, 2277, 14674, 78430, 361790, 1480050, … |
| `OG10` | 24 | 1, 24, 299, 2576, 17250, 95680, 457470, 1937520, … |

Ranks in `1…40` that are reachable: **`{1, 7, 8, 23, 24, 27, 35}`** — seven of forty. RH needs hyperbolicity of `J^{d,n}` for *every* `d`, i.e. a definite form of every rank.

Honest weight of this: it rules out the hyperbolic tower *as such*, but it is not decisive on its own, because other families do have growing ranks (for `C` of genus `g`, the Rosati form on `End⁰(Jac C)` has rank up to `4g²`, which is exactly how Weil's proof covers all genera). So one could reasonably answer "use a different family." Findings 2 and 3 are what close that door.

## 2. The trace forms, computed

Using `Ξ(z) = 4∫₀^∞ Φ(u)cos(zu)du = Σ a_m z^{2m}`, so that `b_m := (−1)^m a_m = 4M_{2m}/(2m)!` with `M_k = ∫Φ(u)u^k du > 0`, the function `H(w) = Ξ(√(−w)) = Σ b_m w^m` has positive coefficients and only real negative zeros iff RH. Jensen polynomials of `γ(m) := m! b_m`:
```
J^{d,n}(X) = Σ_{j=0}^d C(d,j) γ(n+j) X^j ,     RH ⟺ every J^{d,n} hyperbolic (Pólya).
```
Setup validated: `4M₀ = 0.497120778` against `ξ(½) = 0.4971207174` (rel. err. `1.2×10⁻⁷`, quadrature-limited); all `b_m > 0`.

Trace forms of `ℝ[X]/(J^{d,n})` for `d = 2…6`, `n = 0, 1, 3`: **all positive definite, zero negative eigenvalues, no nonreal roots** — consistent with the known Turán/Jensen results and with RH. The machinery works.

And here is the Gram matrix of `Tr(x²)` on `ℝ[X]/(J^{3,0})`:
```
[            3.0     -148.316459531      8198.41310255 ]
[ -148.316459531      8198.41310255     -491246.442633 ]
[  8198.41310255     -491246.442633      31057072.6951 ]
```
The `(1,1)` entry is `Tr(1) = d = 3`, as it must be. Everything else is a power sum of roots of a polynomial whose coefficients are `γ(m) = 4·m!·M_{2m}/(2m)!` — moments of Riemann's kernel. These are transcendental-looking reals carrying no known ℚ-structure, and no conjectural one either.

## 3. Why that makes the realization target vacuous

Over ℝ, **signature is a complete invariant of a quadratic form**: any two positive definite forms of the same rank are isometric. So the target of memo 5 §4(a) — "realize the trace form as the negated intersection form on the orthocomplement of a hyperbolic plane in a Lorentzian lattice" — asks for nothing at all once the form is only defined over ℝ. There is no discriminant to match, no Hasse–Witt invariant, no genus. The construction would be free and would prove nothing.

The mechanism only has content over ℚ. Weil's Hodge index theorem is a statement about a **ℤ-lattice** (`NS`), producing definiteness of a **ℚ-form** (Rosati on `End⁰(Jac C)`). That is what makes the definiteness a theorem rather than an observation.

**And this splits memo 4's ingredient (1) into two halves that come apart.** I wrote there that Weil's proof needs "a finite-rank ℚ-structure." Finite rank is available for ζ — Connes stresses in the 2026 survey that RH reduces to positivity of quadratic forms involving only finitely many primes, and his "letter to Riemann" recovers 50 zeros using primes `< 13`. Rationality is not available, and is not the kind of thing one finds by looking harder: the entries are moments of `Φ`. **The missing half is rationality, not finiteness.** That is a sharper statement of the gap than "the square of the curve is missing," and it is the reason geometry contributes nothing until an arithmetic object is *constructed*.

## 4. The decisive finding: commutativity makes the mechanism circular

Line up the two situations.

**Weil.** The algebra is `End⁰(Jac C)` — **non-commutative** — with the Rosati anti-involution `†`, which is a **positive** involution. The arithmetic input is an *identity relating an element to its involute*:
```
F ∘ F† = q · 1 ,
```
Frobenius being purely inseparable of degree `q`. Then `‖F^n‖² = 2g qⁿ` exactly, and Cauchy–Schwarz on `⟨F^n, Δ⟩` gives the bound. The positivity of the trace form is a theorem (Hodge index); the content is carried by `F`, which is **not** `†`-fixed.

**This program.** The zero multiset with the reality involution yields `A = ℝ[X]/(p)` — **commutative** — with the **trivial** involution. And then:

> For a commutative étale algebra with trivial involution, `A ⊗ ℝ ≅ ℝ^r × ℂ^c` and the trace form has signature `(r+c, c)`. So "the trace form is positive definite" ⟺ `c = 0` ⟺ `A` is totally real ⟺ `p` is hyperbolic.

The positivity *is* the conclusion. There is nothing to derive. Worse, the geometric hypothesis one would want to impose is itself equivalent to the conclusion: if `A ⊂ End⁰(B)` is commutative and fixed by a positive involution, then `Tr(x²) > 0` for `x ≠ 0`, so `A` is totally real. Embedding `A` into a geometric algebra with trivial Rosati already presupposes what we set out to prove.

**So the two-involutions framing, which looked like it was handing us Weil's structure, hands us the degenerate case of it.** Weil's argument needs a non-commutative algebra and an element not fixed by the involution; the reality involution on a zero multiset gives neither. This is the same failure that produced Theorem 9.1, Conjecture 10.1 and Conjecture 10.2 — restatement masquerading as mechanism — now identified at its root rather than case by case.

**What a Weil-shaped attack actually requires**, stated in algebra rather than geometry, which is where it is sharpest:

1. a finite-dimensional **ℚ**-algebra `A` with a positive anti-involution `†`;
2. a distinguished `F ∈ A`, **not** `†`-fixed, with an arithmetic identity `F F† = q·1`;
3. definiteness of the trace form proved independently — by Hodge index on a ℤ-lattice.

The program has none of the three, and §3 shows the input blocks (1) at the first step.

---

## 5. Assessment: does the program make sense?

Separating the two questions that get conflated.

### Is the geometric route to RH worth continuing? No.

Six independent findings from this session, each sufficient on its own:

1. Slice regularity contributes nothing, and the program proved this three times over (Theorem D, Theorem E, and the uniqueness appendix, whose multiplicative-rigidity theorem shows the fiberwise triviality is *forced* by Frobenius).
2. The twistor lift's zero divisor is the exact degeneracy case of Castelnuovo–Severi, and the appendix's incidence rigidity shows the product form is forced by the definition — not a fixable modelling choice.
3. Every conjecture the program formulated was RH-trivial or RH-orthogonal, with a structural cause: computability statements about the defect cannot have directional content when RH is a vanishing statement.
4. The Lorentzian/Hodge–Riemann bridge reduces *exactly* to the first Turán inequality — already a theorem for `Ξ` (Csordas–Norfolk–Varga), and provably strictly weaker than hyperbolicity.
5. The trace-form realization target is vacuous over ℝ.
6. The input supplies no ℚ-structure, and rationality — not finiteness — is the missing half of the only mechanism known to prove such positivities.

Finding 6 is the one that matters most, because it is independent of every geometric choice. It says: **no amount of better geometry helps until an arithmetic object exists, and constructing that object is the whole problem** — the central open problem of the Connes–Consani programme, unsolved in a decade, and one their own live effort has moved away from (the Feb 2026 survey does not discuss the square of the curve, Castelnuovo–Severi, or the Hodge index at all).

### Is there real mathematics here worth publishing? Yes — four items.

None depends on RH, and each has an identifiable referee.

1. **The uniform oscillation lemma.** Unconditional: `F(c) = Re Z(c, log 2)` has positive oscillation on every window of every fixed length at every height, with effective constants. Content: *the prime-2 term of the explicit formula is never drowned by the archimedean drift.* Analytic number theory, short note.
2. **The quantifier-loophole observation.** The most transferable thing the arc produced, and it travels well beyond RH: a specification with an existential quantifier over continuum-valued sample parameters, ranging *after* the instance, is satisfiable by encoding — an information channel opens before the estimator is consulted. This is the uniform/non-uniform distinction rediscovered in a fresh setting, and it is a genuine cautionary result for anyone writing approximation conjectures.
3. **The Lorentzian/Turán reduction** (memo 5 §1–2). That the Lorentzian condition on Jensen polynomials is exactly the first Turán inequality, with explicit counterexamples (`X⁴+10X³+26X²+22X+3`, Newton ratios `2.327, 1.366, 1.442`, one conjugate pair) and a decay rate in the degree. Closes a direction that looks attractive from both sides.
4. **The extension-uniqueness appendix.** Three uniqueness theorems, machine-verified, with a real audience in the slice-regular community, which actively cares which extension is canonical.

### If RH stays the goal

Then the honest reading of this session is that the productive attack surface for an outside contributor is not the geometric one — and the evidence is the program's own yield. In eleven years the geometric frame produced two no-go theorems and a relabeling; the *analytic* work of the last week produced an unconditional oscillation lemma, a recurrence lower bound, and a diagnosis. The results came from the side that was not the original plan.

Keeping RH as the headline via the geometric route means working on the construction of an arithmetic object, in competition with people who have spent a decade on it, with no publishable intermediate results. That is a legitimate choice, but it should be made knowing that is what it is.

Keeping RH as the goal via the *effective-analytic* route — oscillation and equidistribution results for explicit-formula data, effective Turán-type inequalities for `Ξ`'s Taylor coefficients, quantitative Jensen–Pólya work — means results that accumulate, referees who can check them, and a demonstrated ability to produce them. It is the same target reached by a road that pays as it goes.

---

*Certified by `lab_tower_check.py` (rank spectrum, moment computation, Jensen polynomials, trace-form signatures, Gram matrix), building on `lab_hankel_check.py` and `lab_lorentzian_test.py`. The commutativity argument of §4 is a proof, not a computation: it is Sylvester's law applied to `A ⊗ ℝ ≅ ℝ^r × ℂ^c`, plus the standard fact that the fixed subalgebra of a positive involution is totally real (Albert's classification).*
