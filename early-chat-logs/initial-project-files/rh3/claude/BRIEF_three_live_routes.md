# Brief: three live routes, deepened and screened

**2026-08-26.** Deep-dive and initial screening of items 3–5 from `ROUND7` §5. Written to be
self-contained enough to open a new thread on. Two of the three were screened this session with fresh
computation; one was screened by argument and has a single specific technical question left.

**Verdicts up front, because two of them changed:**

| # | route | verdict after screening |
|---|---|---|
| 4 | Jensen polynomials of gauge-theoretic counting sequences | **Screened and largely closed.** Entry point dead by theorem; main target dead by computation. Yields a small publishable measurement and a worked counterexample, not a route. |
| 5 | Chern–Simons → Nyman–Beurling chain | **Chain is dead** (one wrong-direction arrow, two species mismatches). **But it decomposes**, and the surviving half — retarget from Pólya to Nyman–Beurling — is the most promising thing in this brief. |
| 3 | Quaternionic Jensen formula + Weierstrass products | **Not closed, low expected value, one specific checkable question.** Survives the marginality screen, which is unusual and the reason to keep it. |

---

# Route 4 — Jensen polynomials of gauge-theoretic counting sequences

## 4.1 What the route was

Round 6 §5.1 established a clean void: **nobody has studied Jensen polynomials, Turán inequalities, or
hyperbolicity for any gauge-theoretic counting sequence** — Nekrasov `Z_k`, Donaldson–Thomas,
Pandharipande–Thomas, Gopakumar–Vafa, Vafa–Witten. The technology is mature, the asymptotics are
available from modularity and wall-crossing, and the intersection is empty.

The hope was specific: not that a gauge sequence would *supply* `Ξ`'s coefficients (round 1 closed
that — no manifold, group, dimension or moduli space supplies the moments of `Φ`), but that a gauge
sequence might carry a **transportable mechanism for uniformity in `d`**, which round 6 §2 identified
as the entire remaining gap. Mechanisms travel better than objects.

The proposed entry point was Heim–Neuhauser with Appendix B by Ken Ono
([arXiv:2606.15394](https://arxiv.org/abs/2606.15394)), *Dominant zeros of Nekrasov–Okounkov
polynomials*: they prove `NO_n(z)` has a unique zero of maximal modulus, real, negative and simple,
by realizing the zeros as eigenvalues of an explicit `(n−1)×(n−1)` nonnegative primitive Hessenberg
matrix `M_n^h` and applying Perron–Frobenius. They explicitly do **not** prove full real-rootedness
or any total-positivity statement. My question was: **is `M_n^h` totally nonnegative, and is
`{A_{n,k}}` a Pólya frequency sequence?** — since they got one real zero from mere *nonnegativity*,
and all real zeros would need *total* positivity.

## 4.2 The entry point collapses to one question, and the answer is no

**The two questions are the same question.** By **Aissen–Schoenberg–Whitney–Edrei**, a finite
nonnegative sequence is a Pólya frequency sequence **iff** its generating polynomial has only real
nonpositive zeros. So `{A_{n,k}}_k` is PF ⟺ `Σ_k A_{n,k}x^k` — which *is* the Nekrasov–Okounkov
polynomial — has only real nonpositive roots. And a totally nonnegative matrix has all eigenvalues
real and nonnegative, so `M_n^h` totally nonnegative would force the same conclusion.

**So the whole entry point reduces to: are the Nekrasov–Okounkov polynomials real-rooted? They are
not.**

Computed from the Nekrasov–Okounkov generating function. Using
`−Σ_k log(1−q^k) = Σ_M (σ(M)/M)q^M`, the D'Arcais polynomials satisfy
`∏_k(1−q^k)^{−u} = Σ_n P_n(u)q^n`, and `NO_n(z) = P_n(1−z)`, so real-rootedness is the same question
for both. Exact rational arithmetic for the coefficients, then **exact Sturm counts** on the
integer-cleared polynomials (all squarefree, so counts are exact):

| `n` | degree | distinct real roots | verdict |
|---|---|---|---|
| 8 | 8 | 8 | all real |
| 9 | 9 | 9 | all real |
| **10** | **10** | **8** | **NOT all real** |
| 11 | 11 | 11 | all real |
| 12 | 12 | 10 | not all real |
| 14 | 14 | 12 | not all real |
| 15 | 15 | 13 | not all real |
| 20 | 20 | 16 | not all real |
| 25 | 25 | 21 | not all real |
| 30 | 30 | 22 | not all real |

The first failure is exact and exhibitable:

```
P_10(u) = u(u+1)(u^8 + 134u^7 + 6496u^6 + 147854u^5 + 1709659u^4
                 + 10035116u^3 + 28014804u^2 + 29758896u + 6531840) / 3628800
```

with the degree-8 factor contributing two complex-conjugate pairs. Numerical roots at 60 digits agree
with the Sturm counts throughout.

> **Conclusion.** `{A_{n,k}}` is not a Pólya frequency sequence and `M_n^h` is not totally
> nonnegative, for every `n ≥ 10`. The Heim–Neuhauser–Ono Perron–Frobenius result is not the first
> step of a total-positivity ladder; it is the whole ladder. **This question is closed, and I could
> have closed it in round 6 by running the computation instead of proposing it.**

*(Caveat on one link: I am relying on round 6's report of Heim–Neuhauser–Ono's theorem that the
eigenvalues of `M_n^h` are exactly the zeros of `NO_n`. If that is a one-way inclusion rather than an
equality the Hessenberg half needs re-checking, though the PF half stands on ASWE alone.)*

## 4.3 But that was the wrong object — so I ran the right screen

Worth separating clearly, because round 6 conflated two things:

- **(a) Nekrasov–Okounkov / D'Arcais polynomials in the *parameter* `z`.** Roots studied by
  Heim–Neuhauser–Ono. Not real-rooted (§4.2). This is a polynomial in a deformation parameter, *not*
  a Jensen polynomial of a counting sequence.
- **(b) Jensen polynomials of an actual *counting sequence*.** `J^{d,n}(X) = Σ_j binom(d,j) a(n+j)X^j`
  for `a(n)` an enumerative invariant. **This is what route 4 actually targets**, and (a) says nothing
  about it.

So I screened (b) on the most canonical available sequence: the Vafa–Witten / K3 rank-1 case, i.e.

> `a(n) = [q^n] ∏_{k≥1}(1−q^k)^{−24}` — the `η^{−24}` coefficients, the generating function behind
> Johnston–Males ([arXiv:2204.05465](https://arxiv.org/abs/2204.05465), Proc. Edinb. Math. Soc. 66
> (2023) 845).

Sanity-checked: `a(0..4) = 1, 24, 324, 3200, 25650`. All hyperbolicity tests below are **exact Sturm
counts on integer polynomials** (the `a(n)` are integers, so `J^{d,n}` has integer coefficients),
cross-checked numerically.

### Result 1 — the threshold `N(d)` is zero at low degree, far better than the partition function

Smallest `n` with `J^{d,n}` hyperbolic, verified to persist for the next 25 shifts:

| `d` | `N(d)` for VW/K3 | `N(d)` for `p(n)` (Larson–Wagner) |
|---|---|---|
| 2 | 0 | — |
| 3 | 0 | **94** |
| 4 | 0 | **206** |
| 5 | 0 | **381** |
| 6–8 | 0 | — |

So the VW sequence is *much* better behaved than `p(n)` at low degree — hyperbolic at every shift
where `p(n)` needs `n ≥ 94` even at `d = 3`.

### Result 2 — and then it fails, at `d = 13`

Exact hyperbolicity of the `n = 0` edge column (round 4 established this is the global worst case for
`Ξ`):

| `d` | 2–12 | **13** | 14 |
|---|---|---|---|
| VW/K3 `J^{d,0}` | hyperbolic | **NOT hyperbolic** | not hyperbolic |

At `d = 13`: degree 13, **9 distinct real roots**, two complex-conjugate pairs at
`−0.38145 ± 0.02859i` and `−0.26921 ± 0.01729i`. Exact Sturm count and 80-digit numerics agree.

> **Therefore the entire function `Σ_n a(n)z^n/n!` built from the Vafa–Witten/K3 sequence is NOT in
> the Laguerre–Pólya class.**

### Result 3 — and `Ξ` is qualitatively different

Normalized De Bruijn–Newman margins at the `n = 0` edge, against the exact Hermite benchmark
`Λ(H̃_d) = −1/(2(d−1))`:

| `d` | `Λ_norm` (VW/K3) | ratio to Hermite | `Λ_norm` (`Ξ`, round 4) | ratio to Hermite |
|---|---|---|---|---|
| 4 | `−4.652e−2` | 0.279 | | |
| 6 | `−1.342e−2` | 0.134 | | |
| 8 | `−5.785e−3` | 0.081 | `−3.484e−2` | **0.488** |
| 10 | `−3.076e−3` | 0.055 | | |
| 12 | `−1.860e−3` | 0.041 | | |
| 13 | **0 (fails)** | — | | |
| 16 | — | — | `−6.877e−3` | 0.096 |
| 24 | — | — | `−2.378e−3` | 0.057 |
| 40–80 | — | — | hyperbolic, decaying `≍ (log d/d)⁴` | |

At `d = 8` the VW margin is a sixth of `Ξ`'s. Then it collapses to zero by `d = 13`, while `Ξ`'s
`J^{d,0}` is verified hyperbolic to `d = 80` (round 4's 200-digit run) with a polynomially decaying
margin.

## 4.4 Screening verdict

**The hope was a transportable uniformity mechanism. The screen shows the nearest gauge-theoretic
sequence does not have the property to transport.** It is not merely that no one has proved
uniformity for it — the property is *false* for it, at `d = 13`.

This is a genuine negative rather than an absence of evidence, and it also removes the motivating
analogy: whatever makes `Ξ`'s Jensen polynomials hyperbolic at `d = 80` is not something the VW/K3
sequence shares.

**What survives, and it is small but real.** Per round 6, nobody has done Jensen polynomials for any
gauge-theoretic counting sequence. This screen is therefore a new measurement, and it is
publishable-shaped as a short note: *the VW/K3 Jensen polynomials are hyperbolic for every shift at
`d ≤ 8`, hyperbolic at the `n = 0` edge for `d ≤ 12`, and fail at `d = 13`* — which locates
Johnston–Males's asymptotic theorem precisely and exhibits a second worked example (after `p(n)`) of
"for each `d`, all large `n`" holding while "all `d`, all `n`" fails. Effort: days. Bearing on RH: none.

**Honest scope of the negative.** I screened one sequence — the canonical rank-1 `η^{−24}` case.
Johnston–Males treat three families (`α_{1,r}`, `α_{2,p}`, `α_{3,p}`), and DT, PT, GV and Nekrasov
`Z_k` sequences are untested. The negative is strongly suggestive, not exhaustive. If anyone wants to
continue this route, the cheap next step is to run the same exact-Sturm scan on the other
`η`-quotient families and on a DT or Nekrasov series, and see whether any of them survives past
`d = 13`. My expectation is that none does, and the reason is that none of them has a functional
equation.

---

# Route 5 — the Chern–Simons → Nyman–Beurling chain

## 5.1 The chain as drawn in round 6

> Chern–Simons Stokes constants (integers, conjecturally DT invariants; Garoufalidis–Gu–Mariño)
> → resurgence → **quantum modular forms** (Garoufalidis–Zagier,
> [2111.06645](https://arxiv.org/abs/2111.06645), SIGMA 20 (2024) 055)
> → **McSpirit–Rolen** ([2505.00799](https://arxiv.org/abs/2505.00799)): `L`-function functional
> equations are the computational input to Stokes constants of quantum modular forms
> → **Bettin–Conrey** (Algebra & Number Theory 7 (2013) 215–256,
> [1111.0931](https://arxiv.org/abs/1111.0931)): quantum-modular-type period functions carry
> **Vasyunin sums**
> → Vasyunin sums are exactly the objects in the **Nyman–Beurling–Báez-Duarte–Vasyunin criterion for
> RH**

Every link is published; no paper traverses more than two.

## 5.2 Screening: the chain does not compose

Three defects, and the first is fatal as drawn.

**(i) One arrow points the wrong way — at the load-bearing joint.** McSpirit–Rolen make `L`-function
functional equations the **computational input** to Stokes constants. That link runs
`L-function → Stokes data`. To produce RH you need `Stokes data → L-function`. **A chain with an
arrow reversed at its critical joint does not compose.** Whether the McSpirit–Rolen dictionary is an
*equivalence* (hence invertible) or a one-way computation is the single fact that decides whether
route 5's chain has any life at all, and it is a one-afternoon read. My expectation, from the
framing "computational input," is that it is one-way.

**(ii) Species mismatch at the same joint.** McSpirit–Rolen is a number-theory paper about *Zagier's
examples* of quantum modular forms, not about the ones Chern–Simons produces. The Garoufalidis–Zagier
objects `Φ_α(ℏ)` are matrix-valued with entries in `Q̄[[ℏ]]`, attached to hyperbolic knots. Nothing
establishes that these are in the class McSpirit–Rolen's dictionary applies to.

**(iii) Species mismatch at the next joint too.** Bettin–Conrey's objects are what they themselves
call **"imperfect quantum modular forms"** — "nearly an example of what Zagier calls a quantum modular
form," differing by a **non-smooth correction term**. So the object carrying the Vasyunin sums is not
a quantum modular form in the sense the previous link produces.

**(iv) The first link is conjectural.** Integrality of the Stokes constants, and their identification
with DT invariants, is **conjectural** — numerically verified for `4₁` and `5₂` only.

> **Verdict on the chain: dead as a chain.** Five links, of which one is conjectural, two join
> different species, and one runs backwards. This is not a case of "nobody has connected them"; it is
> a case of the links not being connectable as stated.

## 5.3 But the route decomposes, and the surviving half is the best item in this brief

Two things in route 5 are independent of the chain and both are worth having.

### (a) The genuine card: quantum modularity is where physics *produces* arithmetic

This is not rhetorical. The quantum modular form was **invented** because Chern–Simons asymptotics
demanded an object that did not exist — Zagier 2010, out of the Kontsevich–Zagier series and the
asymptotics of quantum invariants. Compare every other physics/RH contact in rounds 1–7, all of which
*consume* known arithmetic:

| contact | direction |
|---|---|
| Vafa–Witten Turán inequalities (Johnston–Males) | consumes GORZ |
| Remmen amplitudes; Duhr–Kshirsagar deflation | consumes Hermite–Biehler; **works for any real-rooted entire function**, so no arithmetic content either way |
| Angelantonj et al. string DOS | consumes RH (RH ⟹ convergence rate) |
| Dorigoni–Treilis `1/ξ(2−2t)` poles | consumes RH (to place a contour) |
| N=4 Eisenstein spectral decomposition | `ξ` cancels; no arithmetic at all |
| **quantum modularity / Chern–Simons** | **produces** |

That asymmetry is the one structural reason to keep any physics route alive at all, and it survives
the chain's collapse.

### (b) The reframing: retarget from Pólya to Nyman–Beurling

This is the actionable half, and it does not depend on Chern–Simons in any way.

**Nyman–Beurling–Báez-Duarte:** RH holds **iff** the span of `{ρ(θ/x) : θ ∈ (0,1)}` is dense in
`L²(0,∞)` (with `ρ` the fractional-part function, in the Báez-Duarte formulation a specific
approximation problem with explicit Vasyunin-sum Gram matrix entries).

Why this is the right target to consider switching to, and why it should have been on the list in
round 6:

1. **It is a density statement in a Hilbert space, not a hyperbolicity statement about polynomials.**
   Physics is made of Hilbert spaces and approximation problems. Route 3's and route 4's obstacles are
   both obstacles *to certifying hyperbolicity*; they do not apply here.
2. **It sidesteps the quantifier-order problem entirely.** Round 6 §2.2's finding — that RH is the
   single vertical line `n = 0, d → ∞` that every known Jensen wedge misses by construction — is a
   fact about the Pólya formulation. Nyman–Beurling has no `d`.
3. **It sidesteps the round-6 §3 kernel no-go.** That no-go kills every criterion stable under
   Gaussian slack. Nyman–Beurling is a density statement about a specific `ζ`-built family; it is
   exactly critical, with no slack parameter to be stable in.
4. **The finite-dimensional truncations have a known structure with an *integral* flavour** — the
   Gram matrices are Vasyunin cotangent sums, i.e. arithmetic objects, and Bettin–Conrey give exact
   convergent-series formulas for the second moment of `ζ` on the critical line in that context. This
   is the closest thing in the whole survey to "an integral structure with a definiteness question,"
   which round 6 §6 identified as where lattice technology would have to enter.
5. **It has structural kinship with Connes' current best route.** Round 6 §6: Connes' finite-prime
   Weil-form extremizers provably lie on the critical line, and the unproved step is convergence.
   Nyman–Beurling has the same shape — finite truncations behave, the limit is the difficulty. Two
   independent programs converging on "the finite object is fine, the limit is the problem" is
   information about where the difficulty actually is.

**Screening it honestly, including against itself:**

- **Davenport–Heilbronn control.** Does the criterion distinguish RH-true from RH-false? Nyman–Beurling
  is built from `ζ` specifically via the fractional-part kernel, so it is not generic in the way the
  N=4 reformulation was (round 5 flagged that one as passing D–H trivially, hence uninformatively).
  **This looks like it passes the control informatively — but that must be verified, not assumed.**
  It is the first thing to check.
- **The honest counterweight.** Nyman–Beurling is a *known* equivalence with a long literature and
  decades of effort (Báez-Duarte, Balazard, Saias, Burnol, Bettin–Conrey), and it has not yielded.
  Sarnak's warning applies with full force: *"There have been many equivalences of RH… Without their
  having led to any new information about the zeta function… it is difficult to know if such
  equivalences constitute any real progress."* Switching criteria is not progress by itself. **The
  question that would make it progress is: does any physical or geometric structure supply the
  approximation/density statement Nyman–Beurling needs?** That is the round-1 question in a new
  formulation, and it is the one to ask first rather than last.

## 5.4 What to do, in order

1. **Read McSpirit–Rolen and determine the arrow direction** — one-way computation or invertible
   dictionary. This decides the chain, and it is cheap. Expect one-way.
2. **Independently: read the Nyman–Beurling / Báez-Duarte literature properly**, which this project
   has never done, and run the Davenport–Heilbronn control against it.
3. **Then** the substantive question: is there a physical or geometric source for the density
   statement? Do not build anything before answering it.

---

# Route 3 — quaternionic Jensen formula and Weierstrass products

## 3.1 The observation, restated precisely

Confirmed in round 7 §4.7. For a slice-regular `f` on a ball in `ℍ` with **real coefficients**
(equivalently *slice-preserving*: Ghiloni–Perotti, Trans. AMS 369 (2017) 4725, Lemma 2.2 — the zero
set is *circular*), `f ≢ 0`, the zero set consists of **isolated real points and isolated 2-spheres
`x + yS`, `y ≠ 0`** (Gentili–Stoppato, Michigan Math. J. 56 (2008) 655), with the spheres in bijection
with conjugate pairs of non-real zeros of the complex restriction. Hence:

> **`f` is hyperbolic ⟺ `V(f)` contains no 2-spheres ⟺ `dim V(f) = 0`.** Real-rootedness becomes a
> *topological* condition on a zero set in four dimensions, and the sphere radius `|y|` is exactly the
> imaginary part — so it is a **quantitative** detector, not a yes/no test.

And the analytic apparatus exists and has never been pointed this way:

- **Perotti**, *A four dimensional Jensen formula*, [arXiv:1902.06485](https://arxiv.org/abs/1902.06485)
  — relates the value and first two derivatives at a real point, the integral mean over a **3-sphere**,
  and the disposition of the zeros.
- **Gentili–Vignozzi**, *The Weierstrass factorization theorem for slice regular functions over the
  quaternions*, Ann. Global Anal. Geom. 40 (2011) 435 — quaternionic canonical products.

Jensen's formula plus canonical products is exactly the engine classical Laguerre–Pólya theory runs on.

## 3.2 Screening: the Stage-0 tautology, and why it does not quite close

**The negative.** This is where Stage 0 died, and the mechanism recurs. For a real-coefficient `f`,
the restriction `f|_{L_I}` is the *same* complex function for every `I ∈ S`. So the quaternionic zero
set is **determined** by the complex slice data, and every invariant computed from `V(f) ⊂ ℍ` is a
function of the complex zeros. The sphere radii are `|Im ρ|`. "No spheres" is "no non-real zeros"
written in four dimensions. Prop. 3.1 of `NOTE_existence_loophole` applies: it is a certificate of
Hermite type, and the existence of a certificate was never the question.

**Why it nonetheless survives, and this is the reason to keep it.** Re-deriving the screens rather
than inheriting them (round 6 §10):

- **Marginality / the round-6 §3 Gaussian-slack no-go.** That no-go kills any criterion stable under
  `K ↦ e^{−εu²}K`. The criterion "`V(f)` contains no 2-spheres" is *exactly equivalent* to
  hyperbolicity, so it inherits `Λ = 0` exactly and has **no slack to be stable in.** Round 6 §3
  concluded that *only exactly-critical criteria can possibly work.* This one is exactly critical.
  **It is not screened out — and almost everything else is.**
- **Screens A and B.** A topological condition on a 4-dimensional zero set is neither holomorphic on
  `ℂ^d` nor locally constant on the complexified discriminant complement. Not screened out.
- **Faithfulness.** What does Rodgers–Tao's `Λ ≥ 0` become? "The spheres cannot all shrink to points
  under backward heat flow." That is not trivial in the way `ρ² ≥ 0` was. It passes, weakly.

So: tautological in the certificate sense, but it is the *right shape* under the one screen that has
been doing real work. That combination is unusual enough to be worth the specific check below rather
than a dismissal.

## 3.3 The one specific question that decides it

Everything turns on whether the four-dimensional apparatus carries information the one-dimensional
apparatus does not.

> **Does Perotti's four-dimensional Jensen formula, specialized to a real-coefficient slice-regular
> function, reduce to the classical Jensen formula, or does it carry extra terms?**

My prediction, and I want it on record as a prediction: **it reduces.** The reasoning: a 3-sphere in
`ℍ` centred at a real point fibres over the 2-sphere `S` of imaginary units with circle fibres inside
each slice `L_I`; since `f|_{L_I}` is the same function for every `I`, the 3-sphere mean of `log|f|`
should average to the circle mean, which is classical Jensen.

**But the formula's stated shape argues against my prediction**, which is why this is worth an hour
rather than a dismissal: Perotti's formula involves **the value and the first two derivatives** at the
real point, which is strictly more data than classical Jensen uses. Either those extra terms vanish
identically on the real-coefficient locus — in which case route 3 is closed cleanly — or they do not,
and they are the only place content can hide. **This is a one-afternoon check: get the paper, specialize
to real coefficients, see whether the derivative terms survive.**

## 3.4 If it reduces: the one remaining formulation, and it is the user's idea

If the 4D Jensen formula collapses on the real-coefficient locus, the only way to get content is to
**leave that locus** — which is exactly "operations nontrivial off the projection."

The vehicle is the **normal function** `N(f) = f ★ f^c`, which is always slice-preserving (hence
real-coefficient, hence has circular zero set) even when `f` is not. So the well-posed version is:

> Is `Ξ`, or a `Ξ`-related object, the normal function of a slice-regular `f` with **non-real**
> coefficients — and does the structure of `f` constrain `V(N(f))`?

Two useful facts for anyone taking this up: on the real-coefficient subalgebra the `★`-product
*coincides with the pointwise product* and is commutative, a strong reduction; and
`V(N(f)) ⊇ ⋃_{x∈V(f)} S_x` (Ghiloni–Perotti Cor. 4.6(2)), so `N` circularizes.

**Screening this sub-route, honestly and negatively:** `N(f)` has degree `2·deg f` in the polynomial
case, so `Ξ = N(f)` requires `Ξ` to admit a `★`-square-root-like factorization — and there is no
canonical way to split a zero multiset in half. I do not currently see this getting off the ground,
and I am recording that rather than dressing it up. It is the right *formulation* of the user's idea
in this setting; I have no candidate `f`.

## 3.5 Screening verdict

**Not closed; low expected value; one cheap decisive check.** Rank it below route 5(b) and above
route 4. The reasons to keep it on the list are exactly two: it is the only route in the brief that
is *exactly critical* rather than robust, and the deciding question costs an afternoon.

The reason not to invest beyond that: nothing on the quaternionic side is rigid, integral, or
arithmetic. The sphere radii are `|Im ρ|`, a function of the complex data. Round 1's screening
question — *what on the geometric side is rigid, integral, or arithmetic, and which constraint on the
zeros does it carry?* — gets the answer "nothing," which is the same answer it got for ADHM.

**Also worth recording:** no credible work connects quaternionic or Clifford function theory to `ζ`,
RH, or hyperbolicity. The one paper claiming otherwise (Tang, MDPI *Symmetry* 17(7) 1134 (2025)) was
read and is fatally flawed, with the quaternionic content decorative — it plays no role in the
argument. Do not cite it.

---

# Consolidated ranking, and what I would open the next thread with

1. **Route 5(b) — retarget to Nyman–Beurling.** The most promising item here, and it is a *reframing*
   rather than a construction, so it is cheap to evaluate. First actions: read the Báez-Duarte /
   Bettin–Conrey literature (which this project has never touched), run the Davenport–Heilbronn
   control, and then ask the round-1 question in the new formulation: what physical or geometric
   structure could supply a density statement?
2. **Route 3's deciding check** — specialize Perotti's 4D Jensen formula to real coefficients. One
   afternoon, binary outcome.
3. **Route 5(a) — the McSpirit–Rolen arrow direction.** One read, decides the chain, expect it to
   close.
4. **Route 4 — closed as a route.** Optionally write up the VW/K3 Jensen measurement as a short
   standalone note (days, no RH bearing), and optionally extend the exact-Sturm scan to the other
   `η`-quotient families and a DT or Nekrasov series to firm up the negative.

**Standing methodological note, since it bit again this round.** Route 4's entry point was a question
I *proposed* in round 6 and could have *answered* in round 6 with twenty lines of sympy. The rule from
round 6 §10 — re-derive an inherited screen before applying it — needs a companion for the generation
stage: **before proposing a computational question, check whether it is computable now.**

## Reproduction

| script | produces |
|---|---|
| `no_screen.py` | §4.2 — D'Arcais/NO polynomial roots to `n = 30`, exact coefficients, 60-digit roots |
| `verify.py` | §4.2 — exact Sturm counts and the `n = 10` factorization |
| `jensen_vw.py` | §4.3 Result 1 — `N(d) = 0` for `d ≤ 8`, VW/K3 sequence, exact |
| `margin_vw2.py` | §4.3 Results 2–3 — exact `n = 0` edge scan to `d = 28`, normalized DBN margins |
| `check13.py` | §4.3 — independent confirmation of the `d = 13` failure (Sturm + discriminant + 80-digit roots) |

Dependencies: `sympy`, `mpmath`. All hyperbolicity verdicts are exact Sturm counts on integer
polynomials; margins are 300-digit bisection on the heat-flowed normalized polynomial.
