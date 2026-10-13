# Round 7: the sweep completed — the KP hole closes, and MESH emerges as the invariant

**2026-08-26.** Completion of the round-6 sweep: the nonlinear-hyperbolicity-preserver track that died
to an API error, re-run as three sweeps covering nonlinear/algebraic preservers, Wronskians and
amoebas and quaternions, and the `q`-analogue plus the KP-flow question.

**Headline.** The KP-flow idea I raised at the end of round 6 — that the higher Wilson/KP times are
directions our marginality screen never covered — **is dead, by an elementary argument.** The
question was genuinely unasked in the literature and now has a clean negative answer. Two
independent tracks then converged on the same positive finding: **the invariant that survives both
the uniformity problem and the `q`-deformation is not real-rootedness but ROOT SEPARATION (mesh).**
That is the round's real result.

---

## 1. The KP hole: closed, negative, elementary

### 1.1 First, an exact extension of our own identity (new, verified)

Round 2's pencil identity generalizes to every KP time. With `X = diag(z_j)`,
`Y_{jk} = 2/(z_j − z_k)` off-diagonal, `Y_{jj} = Σ_{k≠j} 2/(z_j−z_k)`, and `Z = Y/2` (so
`rank([X,Z] + I) = 1`), verified symbolically in exact rational arithmetic for `k = 2,…,6` at
`N = 7` and numerically to `~4·10⁻¹⁵` at `N = 10`:

> **`det(zI − X − s·Z^{k−1}) = exp(−(s/k)·∂_z^k) p₀(z)`**

The `k = 2` case is round 2's identity. So **every KP time acts on a rational-KP polynomial tau
function exactly as a generalized heat semigroup `exp(t_k ∂^k)`.** This is a small but genuine
addition to what round 4 established (that our pencil is Wilson's tau function at `t₂`).

### 1.2 And that reduction kills the idea

The question "do the higher KP flows preserve hyperbolicity?" is therefore exactly "is `e^{tz^k}` in
the Laguerre–Pólya class?" — because:

- `φ(∂_z) z^n = Σ_k binom(n,k) γ_k z^{n−k}`, which is the **reversal of the Jensen polynomial
  `J^{n,0}` of `{γ_k}`**, and reversal preserves hyperbolicity. So `φ(∂_z)` preserves hyperbolicity
  ⟹ all Jensen polynomials of `{γ_k}` are hyperbolic ⟹ (Pólya) `φ ∈ 𝓛𝓟`. The converse is
  Hermite–Poulain.
- `𝓛𝓟 = {e^{−αz²+βz+γ} z^m ∏(1 − z/x_k) : α ≥ 0, x_k ∈ ℝ}`, so **every Laguerre–Pólya function has
  order ≤ 2.**
- `e^{tz^k}` has order `k > 2` for `k ≥ 3`. Hence `e^{tz^k} ∉ 𝓛𝓟`.

> **Among the semigroups `exp(t_k ∂_z^k)`, only `k = 1` (translation) and `k = 2` with the smoothing
> sign preserve hyperbolicity. There is no room for a second one — Pólya–Schur already settled it in
> 1914.**

Explicit counterexamples, no theory needed:

- `k = 3`: `exp(t∂³)(z³ − z) = z³ − z + 6t`, discriminant `4 − 972t²`. Hyperbolic **iff**
  `|t| ≤ 2/√972 ≈ 0.0642`, then never again.
- `k = 4`: `exp(t∂⁴)z⁴ = z⁴ + 24t` — no real roots for `t > 0`, two for `t < 0`. Both signs fail.
- `k = 2`, wrong sign: `exp(+t∂²)z² = z² + 2t` fails — the heat flow's one-sidedness is exactly the
  `α ≥ 0` in the normal form.

Measured thresholds `T_k(p) = sup{t : exp(t∂^k)p hyperbolic}`, which collapse fast with degree:

| `p₀` | `k=3` | `k=4` | `k=5` |
|---|---|---|---|
| roots `−2,−1,0,1,2` | `[−0.0310, 0.0310]` | `[−0.0323, 0.0183]` | `[−0.0118, 0.0118]` |
| deg 8, equispaced | `[−0.0234, 0.0234]` | `[−0.0162, 0.0072]` | `[−0.0039, 0.0039]` |
| deg 10, Chebyshev | `[−3.5·10⁻⁵, 3.5·10⁻⁵]` | `[−6.7·10⁻⁵, 2.1·10⁻⁶]` | `≈ {0}` |

### 1.3 The hole existed and is empty — the honest verdict

Round 6 §5.3 was right in letter and useless in substance. In a `t_k` direction (`k ≥ 3`) a
hyperbolic polynomial is **interior** to a bounded interval, so the marginality screen genuinely does
not bite there. But there is no positivity mechanism to be robust in, because **the flow does not
preserve hyperbolicity at all**: you lose it at a threshold and never recover.

> **Structural contrast, worth stating flatly.** Under `t₂` the flow *acquires* hyperbolicity at a
> threshold `Λ(p)` and keeps it forever — that is what makes `Λ` a meaningful invariant and
> `RH ⟺ Λ = 0` a meaningful statement. Under `t_k`, `k ≥ 3`, the flow *loses* hyperbolicity at a
> threshold and never restores it. **The higher KP flows are anti-de-Bruijn–Newman.**

The interval also shrinks like a negative power of the degree, so in the `d → ∞` limit relevant to
`Ξ` it degenerates to `{0}` anyway. The `t₂` direction is not one option among many; it is the only
one.

**What survives as a small finding:** the identity in §1.1, and the observation that `T_k(p)` is an
apparently unstudied object (a reversed-sign analogue of `Λ`). The Hall–Ho / Jalowy–Kabluchko
root-motion and heat-flow-conjecture literature treats only `k = 2`; extending the transport picture
to `k ≥ 3`, where loss of reality is guaranteed and the threshold collapses with degree, is
untouched. Not a route to RH.

### 1.4 Corroborating negatives

- **Kasman–Milson–Gekhtman** (arXiv:2511.11813, SIGMA 22 (2026) 036) §6.3 writes down Wilson's tau
  for CM pairs and **never mentions real-rootedness, hyperbolicity, or the DBN constant.**
- **Ben-Zvi–Nevins** (math/0603722, *Flows of Calogero–Moser systems*) realizes all CM/KP flows
  geometrically and states explicitly that they work with **complexified** CM systems — no reality
  conditions anywhere.
- **The KP total-positivity literature is about the opposite question.** Kodama–Williams (Invent.
  Math. 198 (2014) 637) and Abenda–Grinevich (CMP 361 (2018) 1029) characterize *regular*
  (nonsingular) soliton solutions, i.e. `τ > 0` everywhere, i.e. **`τ` has NO real zeros**. Total
  positivity there guarantees the negation of hyperbolicity. The rational-KP/CM tau functions we care
  about are precisely the singular ones — real zeros of `τ` *are* the CM particle positions — so our
  question lives in the complement of that theory and cannot borrow from it.
- **Round 6's void confirmed:** no paper connects the de Bruijn–Newman constant or Rodgers–Tao to
  Yang–Mills, instantons, gauge theory, or any integrable hierarchy. The one place the literatures
  touch is our own pencil observation, and **"`Λ(p)` is the reality threshold of a Calogero–Moser
  pencil" appears nowhere in print.** That remains round 3's unwritten contribution.

## 2. The `q`-analogue: no, with a mechanism — and a repair

### 2.1 Why the naive `q`-Jensen polynomial cannot work

No `q`-analogue of Pólya's criterion, of the Laguerre–Pólya class, or of Jensen polynomials exists.
And there is a structural reason, verified computationally to 60 digits.

Take the naive `q`-Jensen polynomial `J^{d,n}_q(X) = Σ_j [d choose j]_q γ(n+j) X^j` and apply it to
the simplest possible input, `γ ≡ 1` — whose classical Jensen polynomials are `(1+X)^d`, maximally
hyperbolic, and whose generating function `e^z` is the canonical Laguerre–Pólya function. The result
is **exactly the Rogers–Szegő polynomial** `H_d(X;q) = Σ_j [d choose j]_q X^j`, and:

| | result |
|---|---|
| `\| \|z\| − 1 \|` over all roots, `q ∈ {0.9, 0.5, 0.1}`, `d ≤ 20` | `< 10⁻⁵⁷` — **all zeros lie exactly on `\|X\| = 1`** |
| number of real zeros | 1 if `d` odd (namely `z = −1`), 0 if `d` even |

The reason is immediate: `[d choose j]_q = [d choose d−j]_q`, so `J^{d,n}_q` is **self-inversive**
whenever `γ` is constant, and its natural zero locus is the unit circle, not `ℝ`.

> **The `q`-deformation rotates the relevant zero locus off the real line. Hyperbolicity is the wrong
> `q`-invariant, and any "`q`-Pólya criterion" phrased as hyperbolicity is dead on arrival.**

Note also that Rogers–Szegő is the `q`-analogue of the *binomial* — the object at the heart of the
Jensen polynomial — and it is the one family in the `q`-Askey scheme that is orthogonal on the unit
circle rather than on `ℝ`. Not a coincidence; it is the obstruction.

Symptom of the same thing: the naive degree-2 `q`-Jensen inequality reads
`(1+q)²γ_{n+1}² ≥ 4γ_nγ_{n+2}`, *strictly stronger* than Turán for `0 < q < 1`, while degree 3
already fails for `γ ≡ 1`. The naive hierarchy is simultaneously too strong at `d = 2` and vacuous at
`d ≥ 3`.

### 2.2 A repair that appears to work — and where it lands

Insert the Gauss weight `q^{binom(j,2)}`:

> **`J̃^{d,n}_q(X) = Σ_j [d choose j]_q q^{binom(j,2)} γ(n+j) X^j`**

For `γ ≡ 1` the `q`-binomial (Rothe–Gauss) theorem gives exactly `J̃ = ∏_{i=0}^{d−1}(1 + q^i X)` —
**hyperbolic, with roots `−q^{−i}` in geometric progression of ratio exactly `q`, i.e. log-mesh
exactly `q`.** Tested over `q ∈ {0.9, 0.5, 0.2}`, `d ≤ 13`, `n ≤ 5` at 50 digits:

| `γ(n)` | generating function | in `𝓛𝓟`? | all `J̃^{d,n}_q` hyperbolic? |
|---|---|---|---|
| `1` | `e^z` | yes | **yes** |
| `n+1` | `(1+z)e^z` | yes | **yes** |
| `1/n!` | Bessel-type | yes | **yes** |
| `n²−n+1` | `(1+z²)e^z` | **no** (zeros `±i`) | **fails, and only at `n = 0`** |
| `n!` | `1/(1−z)` | not entire | fails for all `d,n` |
| `1,−3,1,−3,…` | — | no | fails |

The non-LP-but-entire case failing *only at small shift* is exactly the signature classical Jensen
polynomials of `(1+z²)e^z` show. **Conjecture (unproven, no literature found):** `J̃^{d,n}_q`
hyperbolic for all `d,n` ⟺ the generating function lies in a `q`-deformation of `𝓛𝓟`.

**And the repair lands somewhere principled.** The Gauss weight `[d choose j]_q q^{binom(j,2)}` is the
exact *inverse* of the weight in the **Leake–Ryder `q`-multiplicative convolution**
(arXiv:1712.02499, Adv. Math. 2020), `p ⊠^q_n r = Σ_k [n choose k]_q^{−1} q^{−binom(k,2)}(−1)^k p_k
r_k x^k`. So the repaired `q`-Jensen polynomial lives naturally inside the existing framework.

### 2.3 The existing `q`-Pólya–Schur theory preserves MESH, not real-rootedness

This is the real answer to the `q` question, and it is a good one.

- **Brändén–Krasikov–Shapiro**, *Elements of Pólya–Schur theory in the finite difference setting*,
  arXiv:1204.2963. Their **Lemma 8 proves that no nontrivial finite-difference operator preserves all
  real-rooted polynomials.** So they are *forced* to work instead with `𝓗𝓟_{≥α}` = real-rooted
  polynomials of **mesh ≥ α** (minimal gap between consecutive roots). Theorem 3 is a discrete
  Hermite–Poulain theorem.
- **Lamprecht** introduced the `q`-multiplicative convolution with genuine `q`-binomials and the
  **logarithmic root mesh** (`lmesh(p) ≥ q` iff `x_{i+1}/x_i ≥ q` for positive roots).
- **Leake–Ryder** prove Lamprecht's theorem (`lmesh ≥ q` is preserved) and use it to settle the
  Brändén–Krasikov–Shapiro mesh conjecture for the additive convolution. They note explicitly that
  the `q`-multiplicative convolution **does not preserve real-rootedness in general** — it preserves
  log-mesh. `q → 1` recovers classical Grace–Szegő.

**Gap:** there is **no `q`-analogue of the Borcea–Brändén classification.** Nobody has classified
log-mesh-preserving linear operators in Borcea–Brändén style. Open and well-posed.

## 3. The round's actual result: MESH is the invariant

Two independent tracks converged, and neither was looking for the other.

| track | finding |
|---|---|
| **Uniformity in `d`** (round 6 §2.4) | The only route to `d`-uniform hyperbolicity anyone has walked is **Iskander–Jain's `δ`-Laguerre–Pólya class** — defined by a `d`-independent lower bound `δ` on root separation. Uniform *by construction*, because `H_d` never appears. |
| **`q`-deformation** (§2.3 above) | Real-rootedness is *provably* not preservable by nontrivial finite-difference operators (BKS Lemma 8). The invariant that survives is **log-mesh**. |

> **Root separation, not real-rootedness, is the invariant that survives both the uniformity problem
> and the `q`-deformation. Two unrelated obstructions force the same substitution.**

This is worth taking seriously as a design constraint. It says: stop trying to certify "all roots
real" and start trying to certify "all roots real, separated by at least `δ`," because that is the
formulation in which (a) all-degrees-at-once conclusions exist, and (b) the deformation theory is
non-trivial. The classical apparatus that would need re-deriving in mesh form is Pólya's criterion
itself.

**The obvious hard question, and I want to flag it rather than bury it:** what is the mesh of `Ξ`'s
Jensen polynomials? Round 4 measured the *margin* (`Λ_norm ≍ −C(log d/d)⁴` at the `n=0` edge, driven
by a fixed low-height collision divided by growing variance). A mesh bound would need the zeros not
to crowd — and Lehmer pairs are precisely zeta zeros that crowd. So `Ξ` plausibly has **no uniform
mesh bound at all**, which would make the `δ`-LP route inapplicable to it for a structural reason.
That should be checked before investing in this direction; it is cheap to check numerically against
the existing zero caches.

## 4. Other findings worth recording

### 4.1 The pencil threshold question — our own round-3 open problem, confirmed unaddressed

Round 3 §3.4 asked: *for which pencils `X + tY` is the spectrum real for all `t ≥ t₀`?* and guessed
this was unaddressed. **Confirmed:** searched six ways; the entire hyperbolic/definite-pencil theory
(Higham–Mackey–Tisseur; Al-Ammari–Tisseur, LAA 436 (2012) 3954; Niendorf–Voss, LAA 432 (2010)) is
**pointwise** — definiteness of a pair, existence of *some* `μ` with `P(μ) ≻ 0`, alternating
definiteness at `γ₀ > … > γ_{ℓ−1}`. **No monotone threshold in a deformation parameter is formulated
anywhere.** Nuij theory (Math. Scand. 23 (1968) 69; Kurdyka–Păunescu arXiv:1504.03665) asserts
hyperbolicity for *all* real `s`, never beyond a threshold. The nearest relative in spirit is
critical damping / overdamping in the quadratic-eigenvalue-problem literature, for structured
mechanical families only.

Partial answers obtained this round:

- **Eventual reality.** If `B` is symmetric with **distinct** eigenvalues and `A` arbitrary, there is
  `t₀` with `spec(A + tB) ⊂ ℝ` for all `t ≥ t₀`. (Substitute `λ = tν`, divide by `t^n`; at `1/t = 0`
  the roots are `B`'s eigenvalues, real and simple; the implicit function theorem continues them
  real-analytically.) Verified: 0 failures in 500 random trials at `t = 10⁸`.
- **Distinctness is essential.** With `B = diag(1,1,−1,2)`, **27% of random `A` give complex spectrum
  at `t = 10⁸`** — matching the prediction that on the repeated eigenspace one sees a `2×2` Gaussian
  block, real with probability `1/√2 ≈ 0.707`.
- **Reality is NOT monotone in `t`.** `S = {t > 0 : spec(A+tB) ⊂ ℝ}` is semialgebraic, hence a finite
  union of intervals — but not a ray. Over 400 random `4×4` instances scanning `t ∈ (0,200]`: **306
  gave one interval, 83 gave two, 8 gave three.**

> **Consequence for our own work.** The de Bruijn–Newman `Λ(p) = inf{t : spec(X+tY) ⊂ ℝ}` *is* a
> genuine one-sided threshold — hyperbolicity persists above it. But that is **not** generic pencil
> behaviour. Something about the rank-one CM condition (or equivalently the heat-flow structure) is
> what makes reality monotone. **Identifying what forces monotonicity is a well-posed question our
> notes never asked, and it is the right form of round 3 §3.4.**

Open and promising: effective bounds on `t₀` in terms of `‖A‖` and `gap(B)`. Lidskii–Vishik–Lyusternik
perturbation machinery (Moro–Burke–Overton, SIMAX 1997) is the obvious untried tool.

### 4.2 Two operations turn out to be the same operation

**The Schur–Szegő composition is exactly the MSS finite free multiplicative convolution `⊠_n`**, up
to sign convention — Kostov–Shapiro (C. R. Acad. Sci. Paris 340 (2005)) and Marcus–Spielman–Srivastava
(arXiv:1504.00350) discovered the same operation and the same real-rootedness theorem independently,
a decade apart, in two communities. Verified by comparing coefficient formulas and numerically.
**Not stated as an equivalence anywhere.** The hypergeometric-polynomial papers
(Martínez-Finkelshtein–Morales–Perales, arXiv:2309.10970, IMRN 2024) use the bridge without naming it.

Also worth having: **bilinearity buys no new existence.** Freezing one argument of any bilinear
operation gives a linear operator, so its slices are Borcea–Brändén preservers by definition — and
MSS themselves prove real-rootedness of finite free convolution *by citing Borcea–Brändén*. What
bilinearity buys is structure and uniformity in the second argument, not escape from the
classification. **The genuinely outside directions are nonlinear maps on coefficient space, slice /
pushforward constructions, and parameter-threshold questions** (which are not preserver questions at
all — §4.1).

### 4.3 Hadamard products, and Graeffe being exactly wrong for us

**Hadamard (coefficientwise) product does not preserve hyperbolicity:** `(x²−1) ⊙ (x²−1) = x²+1`.
But with a sign condition it does — derived and verified on `5·10⁵` random pairs with zero failures:
*if `p,q` are hyperbolic of degree `n` with all roots of the same sign, then `p ⊙ q` is hyperbolic
with all roots of one sign.* (Route: `p ⊙ q = p * q̂` with `*` Schur–Szegő and `q̂` the
binomial-reweighting, whose multiplier sequence is `Φ_n(x) = Σ binom(n,k)x^k/k!` — computed exactly
for `n = 2..12`, all zeros real and negative.) Two inaccessible papers (LAA 2013, PII
S0024379513005119; and PII S0021904515000118) likely contain this already and should be obtained.

**Graeffe iteration is structurally blind to exactly our case.** One Graeffe step gives an exact
criterion (`p` hyperbolic ⟺ `G(p)` has all roots real and positive), and iterating with Kurtz's
inequalities gives a working certificate — verified 200/200 on exact rational arithmetic, median 3
iterations, and 0/300 in float64 because of doubly-exponential coefficient blow-up. **But
`|z_i² − z_j²| = |z_i − z_j|·|z_i + z_j|`, so Graeffe separates *moduli* and destroys *signed*
separation, and a `±a` pair collides into a double root.** `Ξ` has a symmetric zero set `{±ρ}`. So
Graeffe certifies exactly the hyperbolic polynomials with pairwise distinct root moduli — the
complement of our case. Clean negative with a reason. (No literature uses Graeffe for hyperbolicity
certification at all; the testing literature is Dey–Plaumann arXiv:1810.04055 via Hermite forms and
SOS/SDP.)

### 4.4 MTV: our screen mis-identified what the mechanism consumes

Round 5 disqualified Mukhin–Tarasov–Varchenko (Annals 170 (2009) 863) under the marginality screen,
on the grounds that it "proves reality with room to spare." A close read says the picture is
different and more interesting.

The mechanism: the **Shapovalov form** is positive definite on the real part of an irreducible
highest-weight module; the Gaudin Hamiltonians are symmetric with respect to it when the marked
points `z_i` are real; symmetric operators on a Euclidean space have real spectrum; real spectrum
gives a real fundamental differential operator, hence a real space `V`. The marked points are the
roots of the Wronskian.

But the positivity is used **purely qualitatively — only to switch on the spectral theorem.** The
Shapovalov norms of basis vectors are explicit positive rationals *independent of the `z_i`*, so
there is no degeneration limit and no small parameter. Room to spare, and the room is irrelevant.

> **The genuinely tight inputs are elsewhere: (i) exact reality of the marked points `z_i` — the
> symmetry `S(K_iu,v) = S(u,K_iv)` requires it on the nose, and the real locus is a measure-zero
> closed subset with no open neighbourhood on which the operators are symmetric; and (ii) eigenvalue
> SIMPLICITY of the joint spectrum, which positivity does *not* supply and which is the fragile
> ingredient MTV must establish separately.**

Corroboration that the positivity is incidental: Levinson–Purbhoo (Invent. Math. 2021,
arXiv:1907.11924) prove a *generalization* of Shapiro–Shapiro by a purely topological/degree
argument, with no positive form anywhere. So round 5's screen was applied to the wrong ingredient —
which is another instance of round 6 §10's lesson about inherited screens.

**Also, a clean negative:** nobody has translated MTV-type reality theorems into
Nekrasov–Shatashvili gauge-vacua language. The Bethe/gauge literature is uniformly about *counting*
and *identifying* vacua, never about reality or positivity structure. The natural unwritten
translation: real `z_i` = real masses/Coulomb parameters, Shapovalov form = a norm on the space of
vacua, "all Wronskian roots real ⟹ `V` real" = "the critical locus of the Yang–Yang function is
totally real when the masses are real." Confidence that this is unwritten: moderate (physics
vocabulary makes negative searches less reliable).

### 4.5 Karp's conjecture, and Harnack total reality as extremality

**Karp** (arXiv:2110.02301, now published: Selecta Math. 30 (2024), Paper No. 1) **Conjecture 1.6**,
verbatim: for `V ∈ Gr_{k,n}(ℝ)`, *"If all complex zeros of `Wr(V)` lie in `[−∞,0]`, then `V` is
totally nonnegative"*; strictly, totally positive. **It does concern complex zeros** — the hypothesis
is hyperbolicity of the Wronskian with a sign condition, and the conclusion is *positivity* of the
whole Plücker vector. This is the cleanest existing example of a nonlinear (determinantal /
differential) operation in a higher-dimensional space inducing a hyperbolicity condition that
certifies structure on a slice.

**Harnack curves: total reality as an extremality condition.** The equivalent characterizations of a
simple Harnack curve (Mikhalkin, Annals 151 (2000) 309; Mikhalkin–Rullgård, IMRN 2001; collected in
Lang arXiv:1504.07256 Thms 1.14–1.17) are worth having because they are a *different flavour* of
certificate from a positive form:

1. **the amoeba map is at most 2-to-1** — the only collapsing is complex conjugation, i.e. the
   projection loses nothing beyond conjugation;
2. **maximal amoeba area** among curves with the same Newton polygon (sharp bound `π²·Area(Δ)`);
3. maximal total logarithmic curvature;
4. **the logarithmic Gauss map is totally real**: `γ⁻¹(ℝP¹) = ℝ𝒞` — the same statement-form as
   Shapiro–Shapiro;
5. topological maximality in the Smith–Thom sense (an M-curve with a specific oval configuration).

> **Total reality is equivalent to an extremality/maximality condition on the projection.** That is
> directly the user's "operations nontrivial off the projection" idea appearing as a theorem, and it
> is *not* a positivity certificate — which matters, because every mechanism the marginality screen
> kills is a positivity certificate.

**Citation corrections to our notes:** KOS and KO were swapped. *Dimers and amoebae* is
Kenyon–Okounkov–Sheffield, Annals 163 (2006) 1019–1056, arXiv:math-ph/0311005. *Planar dimers and
Harnack curves* is Kenyon–Okounkov, Duke 131 (2006) 499–524, arXiv:math/0311062. The closed-octant
result is KO's.

### 4.6 Tropical: a real necessary condition, and a warning

**Positive finding.** Rincón–Vinzant–Yu, *Positively hyperbolic varieties, tropicalization, and
positroids*, arXiv:1907.08545, Adv. Math. 383 (2021). For hypersurfaces, positively hyperbolic ⟺ the
defining polynomial is stable (Prop. 2.2). **Theorem 4.6:** if `X` is positively hyperbolic then the
linear subspace parallel to any maximal face of `trop(X)` is spanned by `0/±1` vectors whose supports
form a **non-crossing partition**. **Theorem 6.1:** for a loopless matroid, the Bergman fan is the
tropicalization of a positively hyperbolic variety ⟺ the matroid is a **positroid**. So the tropical
shadow of hyperbolicity is forced into a positroidal combinatorial shape — a genuine tropical
*necessary* condition.

**Warning.** Allamigeon–Gaubert–Skomra (arXiv:1801.02089, J. Symbolic Comput. 2019) prove **the
tropical analogue of the Helton–Nie conjecture is TRUE**, whereas the classical conjecture is false
(Scheiderer). So the obstructions that break the classical spectrahedral world are *invisible*
tropically. Tropicalization may lose exactly the information the problem turns on.

**Clean negatives:** no tropical Pólya/Jensen criterion and no tropical Laguerre–Pólya class exist —
the nearest structure is M-convexity of Lorentzian supports (Brändén–Huh, Annals 192 (2020)). And no
one has connected the KOS/KO Harnack total-reality result to any zeta or `L`-function question or to
Pólya/Jensen criteria; the two literatures have essentially no citation overlap. **Confidence: high.**

### 4.7 Quaternions: the observation Stage 0 should have made

The zero-set structure theorem is confirmed. For slice-regular `f` on a ball in `ℍ` with **real
coefficients** (equivalently *slice-preserving*, Ghiloni–Perotti Trans. AMS 369 (2017) 4725, Lemma
2.2: the zero set is *circular*), `f ≢ 0`: `V(f)` consists of **isolated real points and isolated
2-spheres `x + yS`, `y ≠ 0`** (Gentili–Stoppato, Michigan Math. J. 56 (2008) 655), with the spheres
in bijection with the conjugate pairs of non-real zeros of the complex restriction.

> **Hence: `f` is hyperbolic ⟺ `V(f)` contains no 2-spheres ⟺ `dim V(f) = 0`. Real-rootedness becomes
> a *topological* condition on a zero set in four dimensions — and the sphere's radius `|y|` is
> exactly the imaginary part, so it is a *quantitative* detector, not a yes/no test.**

This is the Stage-0 geometry with the right observation attached. Stage 0 failed because it tried to
use the *symmetry* (free, hence tautological); the content is in the sphere radii. And the analytic
apparatus to exploit it exists and has never been pointed this way:

- **Perotti, *A four dimensional Jensen formula*, arXiv:1902.06485** — a genuine Jensen formula for
  slice-regular functions relating the value and first two derivatives at a real point, the integral
  mean over a **3-sphere**, and the disposition of the zeros.
- **Gentili–Vignozzi**, *The Weierstrass factorization theorem for slice regular functions over the
  quaternions*, Ann. Global Anal. Geom. 40 (2011) 435 — quaternionic canonical products.

Jensen's formula plus canonical products is precisely the engine classical Laguerre–Pólya theory runs
on. **Nobody has run it in the quaternionic setting where hyperbolicity is topological.** That is a
genuine and specific gap.

Two more useful facts: on the real-coefficient subalgebra the `★`-product *coincides with the
pointwise product* and is commutative — a strong reduction. And the **normal function**
`N(f) = f ★ f^c` is always slice-preserving with circular zero set, so it is the natural
hyperbolicity-relevant scalar attached to arbitrary slice-regular data. Also: **Fueter regularity is
the wrong category** — `q^n` is not Fueter regular for `n ≥ 2`, so Fueter theory cannot host a theory
of polynomial roots at all; zero sets there are 3-dimensional. Slice regularity is the only category
in which "hyperbolic = no spheres" is even a statement.

**Clean negative on the literature:** no credible work connects quaternionic or Clifford function
theory to `ζ`, RH, or hyperbolicity. The one paper claiming otherwise — Tang, MDPI *Symmetry* 17(7)
1134 (2025), *"From Complex to Quaternions: Proof of the Riemann Hypothesis…"* — was read and is
fatally flawed: the symmetrized regularization is a different function with no argument that its
zeros converge to `ζ`'s, the `λ → 0` limit is never justified, the claimed convexity is asserted
(Speiser applies to `|ξ|²`, not the regularized variant), the pole at `s = 1` is unaddressed, **and
the quaternionic content is decorative — it plays no role in the argument.** Do not cite.

## 5. Corrections and status

**Corrections to round 6 and this session:**

1. **Round 6 §5.3's KP-flow lead is dead** (§1). The hole in the marginality screen is real and
   empty. I raised it with more enthusiasm than it deserved; the refutation is Pólya–Schur 1914 plus
   an order count, and I should have run that check before flagging it.
2. **Round 5's MTV disqualification targeted the wrong ingredient** (§4.4). The positivity is
   incidental; reality of the marked points and eigenvalue simplicity are the tight inputs.
3. **KOS / KO citations were swapped** in round 5 and round 6 (§4.5).
4. **My total-positivity-via-amplituhedron suggestion is now doubly dead** — round 6 §3.1 killed it
   for `Φ`, and Karp's corpus confirms no coefficient-sequence or Pólya-frequency content exists on
   the gauge side.

**Live after two rounds of sweeping**, in order of how well-posed they are:

1. **Mesh as the invariant** (§3), with the caveat that `Ξ` may have no uniform mesh bound — check
   numerically first, it is cheap.
2. **What forces monotonicity of reality in the CM pencil** (§4.1), given that generic pencils are
   non-monotone. This is the correct form of round 3 §3.4.
3. **Quaternionic Jensen formula + Weierstrass products applied to hyperbolicity** (§4.7).
4. **Jensen polynomials of gauge-theoretic counting sequences** (round 6 §5.1), starting with: is the
   Heim–Neuhauser–Ono Hessenberg matrix totally nonnegative?
5. **The Chern–Simons → Nyman–Beurling chain** (round 6 §5.2).
6. Write up `Λ(p)` as the reality threshold of a CM pencil — still unwritten, still nobody else's
   (§1.4).

**Not verified / open loops:** `Φ > 0` from scratch; the two inaccessible Hadamard papers; journal ref
for Brändén–Krasikov–Shapiro; MSS PTRF volume/pages; Scheiderer arXiv:2509.17121 (*Smooth
hyperbolicity cones are second-order cone representable* — if correct, a major recent advance,
title-only).

**Venue flags:** arXiv:2608.19240 (Stodolsky) self-declares as an "AI Research Artifact" in its
comments field — thematically on point for the non-monotonicity question, not to be relied on.
arXiv:2608.08682 (Holland) and Planat (preprints.org) are unrefereed and both weaker than Kim–Lee.
Tang, MDPI *Symmetry* — see §4.7.
