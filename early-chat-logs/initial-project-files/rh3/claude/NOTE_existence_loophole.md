# The existence loophole: status after three failed closures

**2026-08-25, revised twice the same day.** Written to answer a direct question — *is the loophole
closed?* — about whether recasting a gauge-theoretic approach to RH as an **existence statement**
("solutions with property `B` exist iff the parameter lies in region `R`") evades the round-1
screens.

**Answer: the loophole is not closed. Three attempted closures have failed, each for a different
reason, and the third failure is the informative one.** What replaces "closed" is better: the route
is *funnelled*. Every version of it that survives scrutiny arrives at the same wall rounds 2–4
reached by three other arguments — uniformity in `d`.

This note also records two genuine finds from the literature sweeps that were not previously on our
radar (§5.2), one screen worth applying to any future candidate (§5.3), and the
product-side/coefficient-side reconciliation that explains the whole "lossiness" verdict (§6).

---

## 0. Verdict

| claim | status |
|---|---|
| Screens A/B (`BRIEF` §1.4, §1.5) rule out holomorphic detectors and deformation invariants | **stands** |
| Existence statements evade Screens A/B | **stands — conceded permanently** |
| *Closure attempt 1:* "gauge-theoretic walls are linear, `∂H_d` is not" | **false** — curved walls are ordinary |
| *Closure attempt 2:* "tangent-cone degeneracy separates `H_d`" | **false and unrescuable** |
| *Closure attempt 3:* "the route terminates at Lee–Yang" | **false** — Lee–Yang has no gauge content |
| Prop. 3.1 (any wall description contains `Δ_d`) | **true, but proves less than claimed** |
| "Compact structure group ⟹ reality unconditional" | **false** |
| Marginality screen (§5.3) | **a screen, not a no-go; correctly scoped below** |

The honest summary in one line: **there is no shape obstruction, no type obstruction, and no
termination argument.** What there is, is a design constraint that every known reality mechanism
fails, plus the observation that the surviving route lands exactly where everything else lands.

---

## 1. Closure attempt 1 & 2: the shape argument (dead)

The proposal was: existence statements evade Screens A and B, but the *region* they cut out has the
wrong shape, because `∂H_d` has degenerate strata while gauge-theoretic existence regions have
full-dimensional tangent cones.

**R1. The tangent cone of `H_d` is 2-dimensional, not 1** (`g7`). The half-plane
`{c_j = 0 for j ≤ d−3, c_{d−2} ≤ 0}` lies inside `H_d`, since there
`p(z) = z^{d−2}(z² + c_{d−1}z + c_{d−2})` and the quadratic has discriminant `c_{d−1}² − 4c_{d−2} ≥ 0`.
Verified: 0 non-real cases in 24 000 samples, `d = 3…8`. My `g5` probed two one-parameter families
and I billed it as exact. At `d = 2` the tangent cone is *full*-dimensional, so the claimed
separation does not even begin until `d = 3`.

**R2. `H_d` is the preimage of a polyhedral cone under a polynomial map** (`g7`) — decisive. Hermite
(1856): all roots real **iff** the Hankel form of the Newton power sums is PSD. So
`H_d = Φ^{-1}(ℝ^d_{≥0})` with `Φ =` the leading principal minors — a polynomial map onto a
polyhedral cone. Verified: `det(Hermite Hankel) − Δ_d ≡ 0` symbolically for `d = 2…5`; PSD ⟺
real-rooted on 32 000 samples. At `d = 3`, `H_3 = Δ_3^{-1}([0,∞))` — the preimage of a half-line.

Tangent-cone dimension is not preserved under polynomial pullback. The cusp is manufactured by `Φ`.
**No property of the shape of `H_d` can obstruct a wall-type or existence-type description of it.**
This is not a survey gap; the argument is wrong on its own terms.

*(Related correction: `∂H_d` is a proper subset of `{Δ_d = 0} ∩ ℝ^d`, not equal to it — the latter
contains e.g. `(z²+1)²`.)*

---

## 2. What survives from the original screens

**Screen A.** `ℝ^d` is maximally totally real in `ℂ^d` and `H_d` has nonempty interior, so a
holomorphic function vanishing on `H_d` vanishes identically. **Correct.**

**Screen B.** `ℂ^d ∖ {Δ_d = 0}` is connected, so no locally constant invariant on the complexified
complement distinguishes `int H_d`. **Correct.**

**The concession is permanent.** An existence predicate need not extend holomorphically and need not
be locally constant. Conditional existence across real walls is ordinary — Seiberg–Witten
wall-crossing at `b₂⁺ = 1` (Okonek–Teleman, [alg-geom/9603003](https://arxiv.org/abs/alg-geom/9603003));
degree-`n−1` Hermitian–Yang–Mills walls in the Kähler cone (Clarke–Tipler,
[2304.05245](https://arxiv.org/abs/2304.05245)); semicircular Bridgeland walls (Maciocia,
[1202.4587](https://arxiv.org/abs/1202.4587)), which become PDE-existence statements via `Z`-critical
connections (Dervan–McCarthy–Sektnan, [2012.10426](https://arxiv.org/abs/2012.10426)).

---

## 3. The one theorem that survives

> **Proposition 3.1.** Let `Φ : ℝ^d → ℝ^N` be polynomial and `P = {g₁ ≥ 0, …, g_m ≥ 0} ⊆ ℝ^N` basic
> closed semialgebraic. If `H_d = Φ^{-1}(P)`, then some `g_i ∘ Φ` is divisible by `Δ_d`.

*Proof.* For `c ∈ ∂H_d`: `Φ(c) ∈ int P` would put a neighbourhood of `c` in `H_d`; so
`Φ(c) ∈ ∂P ⊆ ⋃_i {g_i = 0}`. The top stratum `Σ ⊂ ∂H_d` (one double real root, rest simple real) is
a `(d−1)`-dimensional real-analytic manifold, hence Baire, so one fixed `i` has `g_i ∘ Φ = 0` on a
relatively open `Σ₀ ⊆ Σ`. There `grad Δ_d ≠ 0` (verified, `g3`), so `V(Δ_d)` is smooth and `Σ` is a
*maximally totally real* submanifold of it; the identity theorem propagates the vanishing to all of
`V(Δ_d)`. `Δ_d` is squarefree and absolutely irreducible, so `I(V(Δ_d)) = (Δ_d)` and
`Δ_d ∣ g_i ∘ Φ`. ∎

*(First draft verified irreducibility only over `ℚ`, which is too weak. Absolute irreducibility
follows because `V(Δ_d)` is the closure of the image of the irreducible `ℂ^{d−1} → ℂ^d`,
`(a,b) ↦ coeffs of (z−a)²∏(z−b_j)`, dominant by dimension count; squarefreeness from
`gcd(Δ_d, ∂Δ_d/∂c_0) = 1`, `d = 2…7`.)*

**What it does not show.** I presented this as a rigorous circularity blade. Wrong, for three
reasons. (i) It is a general fact about semialgebraic descriptions — the proof uses nothing about
`H_d` beyond `∂H_d` being Zariski-dense in an irreducible hypersurface — and says only that the
*output description* mentions the boundary equation, not that the *inputs* smuggled it in. (ii) Its
natural witness is Hermite, where the wall functions are the coordinate functions and
`g_i ∘ Φ = det(Hermite) = Δ_d` exactly; if this convicted constructions of circularity it would
convict Hermite, Sturm and Routh–Hurwitz. (iii) Its hypotheses (exact identity, fixed `d`,
polynomial `Φ`) exclude one-sided implications, real-analytic `Φ`, and eventual statements like
Griffin–Ono–Rolen–Zagier's.

**Correct reading:** any semialgebraic wall description of `H_d` is a certificate *of Hermite type*.
The existence of a certificate was never the question — one has existed since 1856. The question is
whether a new one supplies something Hermite does not.

---

## 4. The compactness dichotomy is false

I claimed a compact structure group makes reality *unconditional*, so conditional-reality statements
cannot arise there. Counterexamples, all compact-group:

- **Wilson–Dirac in `SU(3)` lattice QCD.** `D_W` is γ₅-Hermitian (`D_W† = γ₅D_Wγ₅`) — pseudo-Hermitian,
  not Hermitian. Eigenvalues are real **or** in conjugate pairs, with a genuine transition (the
  **Aoki phase**) in continuous parameters. Conditional reality, in a gauge theory (Verbaarschot,
  [1011.5118](https://arxiv.org/abs/1011.5118); Phys. Rev. D **83** 085014).
- **Nonzero chemical potential:** `D(μ)` non-Hermitian, complex spectrum — the sign problem.
- **Transfer-matrix positivity:** self-adjoint for Wilson's action, **not** for Symanzik-improved
  actions (Lüscher–Weisz, Nucl. Phys. **B240** (1984) 349).
- **Fisher zeros** of lattice gauge partition functions in the complex `β = 1/g²` plane.

Also: holonomy eigenvalues for compact `G` are **unimodular**, not real — a small error symptomatic
of the same overreach.

**What survives.** §4(a)/(b) of the first draft are correct: Uhlenbeck's compactness theorems assume
a compact structure group throughout (CMP **83** (1982) 31–42, Thms 1.3, 1.5; Wehrheim, *Uhlenbeck
Compactness*, EMS 2004), and Taubes' `PSL(2;ℂ)` extension opens by stating the theorem "applies only
to connections on principal bundles with compact structure group," then *describes the failure*
rather than repairing it ([1205.0514](https://arxiv.org/abs/1205.0514);
[1307.6447](https://arxiv.org/abs/1307.6447), Part II withdrawn). That constrains *which* gauge
theories have existence technology. It is not a reality dichotomy.

---

## 5. Closure attempt 3: Lee–Yang — and what is actually there

### 5.1 The termination claim was wrong

I claimed the route "terminates at Lee–Yang," which is already absorbed into the De Bruijn–Newman
literature. **Lee–Yang theory has no gauge-theoretic content at any point in its 70-year
development.** Its hypotheses are ferromagnetic pair couplings `J_ij ≥ 0`, scalar spins, a
single-site measure in the Lee–Yang class, and a complex field **conjugate to a global order
parameter**. Lieb–Sokal (CMP **80** (1981) 153) reach two-component ferromagnets and need
anisotropy for `N ≥ 3` — so isotropic classical Heisenberg already has no Lee–Yang theorem, and that
is a *global* symmetry, before anything is gauged. In gauge theory **Elitzur's theorem forbids the
local order parameter Lee–Yang requires**, and the natural complex variable is `β = 1/g²`, giving
**Fisher** zeros — a different complex plane from the Lee–Yang fugacity plane. Zero locations there
are known only numerically (Meurice et al., [1210.6969](https://arxiv.org/abs/1210.6969);
[1202.2109](https://arxiv.org/abs/1202.2109)); there is no locus theorem.

The Newman–Wu survey ([1901.06596](https://arxiv.org/abs/1901.06596), Bull. AMS **57** (2020))
covers the Ising model, the lattice gas, one-component ferromagnets with arbitrary single-spin
measure, and `φ⁴` Euclidean field theory. Three independent full-text fetches confirm the words
*gauge*, *Yang–Mills*, *lattice gauge*, *QCD*, *SU(2)*, *SU(3)*, *non-abelian* and *Wilson* **do not
appear**. Your objection was exactly right.

**What does hold** is the narrower historical claim. Newman's 1976 paper says so itself: "in
mathematical physics it is closely connected with the Lee-Yang theorem of statistical mechanics and
quantum field theory," and "the results of this paper developed out of the study of certain quantum
field theoretic problems" — meaning Ising/`φ⁴`, per his 1973–75 publications. The survey adds: "the
original motivation for this result was provided more by statistical physics and Euclidean field
theory … than by analytic number theory." True, and irrelevant to gauge theory.

### 5.2 Two things that genuinely exist, and were not on our radar

Hunting for the bridge rather than against it turned up two results that are much closer to what we
wanted than anything in rounds 1–4:

**(a) A gauge/string partition function proved to be in the Laguerre–Pólya class.** For ABJM theory
the Fermi-gas rewriting (Mariño–Putrov, [1110.4066](https://arxiv.org/abs/1110.4066)) makes the grand
canonical partition function a Fredholm determinant `Ξ(κ) = det(1 + κρ)`. Kashaev–Mariño
([1501.01014](https://arxiv.org/abs/1501.01014), **CMP 338** (2015)) prove — abstract verified
verbatim — that for a large class of local del Pezzo Calabi–Yaus the operators from quantized mirror
curves are **trace class**; Laptev–Schimmer–Takhtajan ([1510.00045](https://arxiv.org/abs/1510.00045),
**GAFA 26** (2016)) supply self-adjointness, discrete positive spectrum and Weyl asymptotics.
Consequently `Ξ(κ) = ∏_n(1 + κe^{−E_n})` with `E_n` real: **all zeros on the negative real axis**,
conditional on positive mass parameters. That is a Lee–Yang/LP statement for a gauge-theoretic
partition function — and nobody in that literature has ever used the words "Lee–Yang,"
"Laguerre–Pólya," or "hyperbolic," or defined a `Λ` for the family.

**(b) An existence ⟺ total-reality theorem whose region is a cone.** Kenyon–Okounkov–Sheffield
([math/0311062](https://arxiv.org/abs/math/0311062), Duke **131** (2006)) — abstract verified
verbatim — prove "every Harnack curve arises as a spectral curve of some dimer model," and that the
space of Harnack curves of a given degree is "**homeomorphic to a closed octant**," with global
coordinates given by amoeba hole areas and tentacle distances. Dimers on the torus are brane
tilings, i.e. 4d `N=1` quiver gauge theories. So: *a physical solution with prescribed spectral data
exists iff the spectral curve is maximally real, and the maximally-real locus is a polyhedral cone.*
That is the Hermite picture of §1 R2, appearing on the physics side as a theorem.

Two further items in the same direction: Mukhin–Tarasov–Varchenko (**Annals 170** (2009) 863) prove
that hyperbolicity of a Wronskian forces a real basis, via self-adjointness with respect to the
positive-definite Shapovalov form — Hilbert–Pólya executed successfully, on a different function;
and Nekrasov–Shatashvili ([0908.4052](https://arxiv.org/abs/0908.4052)) make Bethe roots into
supersymmetric vacua, so any theorem "the Bethe roots are real for parameters in `R`" is already a
statement about reality of gauge-theory vacua.

### 5.3 The screen these suggest — and its correct strength

Every reality mechanism in the above is an **open positivity condition**: trace-class positivity
(Kashaev–Mariño), Shapovalov positive-definiteness (MTV), total positivity (Karp,
[2110.02301](https://arxiv.org/abs/2110.02301)), positive edge weights (KOS), ferromagneticity
(Lee–Yang). Each proves reality *with room to spare*, on the interior of a positivity region.

But Rodgers–Tao give `Λ ≥ 0` and RH gives `Λ ≤ 0`, so **RH ⟺ `Λ = 0`: `Ξ` sits exactly on the
boundary of the hyperbolic locus in the heat-flow direction.** Newman's dictum, made a theorem.
Hence:

> **Screen.** A mechanism that certifies hyperbolicity of `Ξ` *robustly with respect to the heat
> flow* would give `Λ < 0` and is refuted by Rodgers–Tao. So any candidate must be asked: does its
> positivity region degenerate exactly at the arithmetic point, or does it hold with room to spare
> there? Every mechanism listed above is robust at its target, and the target here is not a robust
> point.

**Scoping, honestly.** This is a screen, not a no-go theorem. Openness *within some family* is not
contradictory — `{cΞ : c > 0}` is an open family of hyperbolic functions containing `Ξ`. The screen
bites only when the mechanism's family can realize the backward heat flow. Since that is *the* flow
the entire De Bruijn–Newman apparatus is phrased through, a candidate whose family avoids it owes an
explanation. But this must be checked per candidate, not asserted.

**And it does not apply to the Jensen route.** Every `J^{d,n}` at finite `d` is hyperbolic with a
strictly positive margin (rounds 2–4 measured them). Pólya: RH ⟺ every `J^{d,n}` hyperbolic. So an
open positivity mechanism is *exactly the right shape* there — and the entire difficulty becomes
**uniformity in `d`**.

*(I attempted to support §5.3 numerically by watching the Hermite certificate degenerate on the
round-4 zeta surrogate (`g8`). The control (`g9`) refutes it: Hermite-polynomial roots, which are
comfortably hyperbolic, collapse at the same rate — `log₁₀` min eigenvalue `−1.845 → −24.664` for
He_d versus `−2.049 → −24.92` for the surrogate, `d = 4…24`. `g8` measures Hankel ill-conditioning,
not marginality, and is discarded. §5.3 rests on the theoretical argument alone.)*

### 5.4 A second screen: the separability obstruction (Burnol 2002)

Added `2026-08-26` from `ROUND11` §3.7(a). Burnol (*Sur certains espaces de Hilbert de fonctions
entières*, [math/0112254](https://arxiv.org/abs/math/0112254), Forum Math. **16** (2004) 789–840)
constructs Hilbert vectors `Y^λ_{s,k}` from the Báez-Duarte operator `U` — scale-invariant, with
multiplier `U(s) = [ζ(1−s)/ζ(s)]·[s/(1−s)]` — satisfying
`(A, Y^λ_{s,k}) = (−d/ds)^k[(s−1)/s · ζ(s)/s]`, such that **the only ones exactly perpendicular to
`A` and its contractions are the `Y^λ_{ρ,k}` with `ζ(ρ) = 0`, `k < m_ρ`**. He calls this the link
"with the so-called Hilbert–Pólya idea." The rescaled vectors `X^λ_{s,0} = Y^λ_{s,0}/√|log λ|`
become **orthonormal in the limit** `λ → 0`. And then, verbatim:

> *"The limit can not work inside `L²((0,∞))` because this is a separable space! In fact one shows
> without difficulty that the vectors `X^λ_{s,k}` weakly converge to 0 as `λ → 0`."*

> **Screen.** The Hilbert–Pólya vectors become asymptotically orthonormal and simultaneously weakly
> converge to zero. Any construction proposing a *limiting* Hilbert–Pólya space must therefore say
> explicitly how it evades separability — either by leaving `L²`, or by rescaling in a way that
> defeats the weak convergence, or by never taking the limit at all. A candidate that quietly assumes
> the limit exists inside a separable Hilbert space is refuted before it starts.

This is a structural obstruction of exactly the kind §5.3 collects, but it is stronger in one
respect: it comes from *inside* a successful construction rather than being imposed from outside,
and it is quantified — Theorem 6.20/6.30 of the same paper gives an exact spanning threshold, that
the evaluators `Z^λ_{ρ,k}` attached to the nontrivial zeros span the Sonine space `K_λ` **if and only
if `λ ≥ 1`** (and, for a Dirichlet `L`-function of conductor `q`, iff `λ ≥ 1/√q`). So the
Hilbert–Pólya shortfall is not vague: it is measured by `λ < 1`, exactly.

*(Note also, from `ROUND11` §4: the Sonin space is the joint of the live Connes architecture, and
Connes' §7.2 credits it to Burnol [9–11] — the same papers. The obstruction and the positivity both
live in the same space.)*

---

## 6. Product side and coefficient side — where the two halves of the programme meet

A question worth recording, because it exposes the mechanism behind the "lossiness" verdict of
rounds 1–2. The gauge-theoretic angle was always about **product formulas** — the Hadamard product
for `Ξ`, the ADHM determinant `det f^{-1}`, the Calogero–Moser pencil `det(z − X − tY)`. The
surviving route is the **Jensen route**, which consumes the **Taylor coefficients** `γ(n)` of `Ξ`,
i.e. the moments of `Φ`. These look like different objects. How do they reconcile?

### 6.1 They are one object in two coordinate systems

The Laguerre–Pólya class has two equivalent characterisations: a Hadamard product with only real
zeros, and a coefficient condition (every Jensen polynomial hyperbolic). Pólya's theorem *is* the
dictionary between them. So the Jensen route is not a different target — it is the coefficient-side
coordinate for the same product-side fact, and the coordinate change is classical.

The two meet explicitly in our own data. Round 3 §2: `J^{d,0}(X/d) → F(X)`, which is `Ξ` in the
variable `w = −z²`, and the degree-40 truncation's real roots recover the first three zeta zeros to
nine digits. Round 4 §2.1: the roots of `J^{d,0}` converge to `−γ_k²/d`. **The coefficient object's
roots are the zeros.** Nothing is lost passing between the descriptions.

### 6.2 The transport is cheap — measured (`g10`)

To check that the coordinate change carries no hidden cost, take a hyperbolic family by its roots,
compute coefficients exactly, round them to `p` decimals, clear denominators, and ask by **exact
Sturm count** on the resulting integer polynomial whether all roots are still real. Least such `p`:

| `d` | zeta surrogate `{−γ²}` | zeta ordinates `{γ}` | Hermite `He_d` | equally spaced | Chebyshev |
|---|---|---|---|---|---|
| 8  | 1 | 1 | 2 | 1 | 1 |
| 12 | 2 | 2 | 2 | 2 | 2 |
| 16 | 3 | 3 | 3 | 3 | 2 |
| 20 | 4 | 3 | 4 | 4 | 4 |
| 24 | 5 | 5 | 5 | 5 | 5 |
| 28 | 6 | 5 | 6 | 5 | 6 |

All five families are indistinguishable, growing like `≈ d/4.7` decimals. The zeta surrogate costs
no more than four comfortably-hyperbolic controls. **The product↔coefficient transport is generic
conditioning, linear in `d`, and is not where any difficulty lives.**

### 6.3 The asymmetry that does matter — and it is the whole verdict

The sides cost the same to convert between, but they do not *carry* the same things.

- **The product side carries which zeros there are** — locations, spacings, the log-gas/Coulomb
  structure, the De Bruijn–Newman flow. This is where geometry naturally lives: determinants,
  Hadamard shape, the CM pencil, the velocity identity `V_j = Ξ''/Ξ'`.
- **The coefficient side carries the moments of `Φ`** — and `Φ` is built from the Jacobi theta
  function, so its moments are where modularity, the Euler product and the explicit formula act.
  **The arithmetic is on the coefficient side.**

So the gauge theory was a *product-side supplier*, and the payload the programme needs is
*coefficient-side*. That is round 1's closing line — "no choice of manifold, gauge group, dimension,
or moduli space supplies rationality of the moments of `Φ`" — with the mechanism now visible. The
dictionary was not lossy because of a bad choice of correspondence. It was lossy because it was
delivering on the wrong side, and the transport, though cheap, has nothing to carry: what the
geometry supplies (log-gas equilibrium) is the universal half, and what is needed (the deviation
from it) is the arithmetic half. Round 2 §5's GUE measurement said the same thing in spacing
language — universal half free, arithmetic half not at all.

### 6.4 One consequence worth keeping

This divide vindicates the scoping of the detector paper. The velocity identity is pure product side
— the Coulomb field of the full zero multiset — and a *diagnostic* is a product-side question
("where are the zeros"). The paper is therefore on the correct side of the divide for what it
actually does, which is why its gauge-theoretic content can be honest and thin at the same time. A
*proof* is a coefficient-side question, and that is the one the geometry cannot supply.

## 7. Where this leaves the programme

Three closures attempted, three failed. What is left is not a wall but a funnel:

1. **No shape obstruction.** Certificates exist and have since Hermite 1856 (§1 R2). Prop. 3.1 says
   any wall-type description is of that type.
2. **No type obstruction.** Existence statements evade Screens A/B, the compactness dichotomy is
   false, and Lee–Yang does not terminate anything.
3. **The one genuine constraint** (§5.3) is that `Ξ` is a marginal point by theorem, which screens
   every known open-positivity mechanism from reaching it directly — but not from reaching the
   Jensen polynomials, where each object is interior.
4. **So the surviving route is the Jensen route, and its difficulty is uniformity in `d`.** Which is
   where round 2 §4 (the geometry gives log-gas equilibrium; the proof needs the arithmetic
   deviation), round 3 §2 (the margin must decay to zero by theorem; the question is the rate), and
   round 4 §2.2 (`Λ_norm ≍ −C(log d/d)⁴`, reduced to one GORZ coefficient-asymptotics derivation)
   all independently arrived.

Four arguments, four routes, one destination. That is the strongest thing this note establishes,
and it did not need any of the three failed closures to get there.

---

## 8. Revised falsification criteria

To reopen a geometric route, a construction must supply one of:

1. **Uniformity in `d`** — the entire gap between GORZ and RH;
2. **Arithmetic input** — a rigid or integral structure carrying a constraint the Hadamard product
   does not (round 1 §6.5, still the best question to ask first);
3. **A lower bound on the interaction energy `E`** — the anti-rigidity statement carrying
   Rodgers–Tao (round 2 §4);
4. or **a positivity mechanism that degenerates marginally at the arithmetic point** rather than
   holding with room to spare (§5.3).
5. or **an explicit account of how a proposed limiting Hilbert–Pólya space evades separability**
   (§5.4), if the construction takes a `λ → 0` (or equivalent) limit of asymptotically orthonormal
   vectors.

Items 4 and 5 are new. Item 4 is the one with a cheap concrete test attached: take the ABJM/mirror-curve
family of §5.2(a), define its De Bruijn–Newman constant, and determine whether its reality region is
ever attained *marginally* or always fails *abruptly*. If always abruptly, that is a clean no-go for
the whole positivity class and is worth writing up. If some family is marginal, it is the first
candidate architecture in this programme that survives its own screen.

Item 5 has a cheap test too, and it is a *negative* one: for any candidate, ask whether it names the
Hilbert space its limiting objects live in. If the answer is "a separable Hilbert space" and the
construction is a limit of asymptotically orthonormal families, it is dead on arrival by §5.4.

---

## 9. On positivity and the Weil comparison

Positivity per se is not exempt from anything: **Hermite is itself a positivity certificate** and
Prop. 3.1 applies to it verbatim. The distinction that matters is Weil's. In the function-field case
the Hodge index theorem supplies a real inequality on a **rigid integral lattice** — integrality and
rigidity are the payload, geometry is delivery. Hermite's positivity is a repackaging: the form is
built *from* the coefficients and transports nothing new.

In gauge theory the integral structures — instanton charge, Donaldson and Seiberg–Witten invariants,
Milnor–Wood bounds — are exactly the deformation invariants, which Screen B rules out. The N=4 SYM
bootstrap question (round 2 §8.3) remains the only candidate I know of that is neither obviously
imported nor obviously a repackaging.

---

## 10. Errors in this note's own drafts, for the record

Following round 3 §5 and round 4 §5:

1. **Closure attempt 2 was a logical error**: tangent-cone degeneracy cannot obstruct a wall
   description, since `H_d` is a polynomial pullback of a polyhedral cone.
2. **The tangent cone was computed wrongly**: 2-dimensional, not 1. Two path families described as
   an exact computation.
3. **`g4` presented null returns as evidence** for `d = 4,5`, and its one row of real data
   contradicted its own caption.
4. **Closure attempt 1** ("gauge-theoretic walls are linear") was wrong — HYM walls have degree
   `n−1`, Bridgeland walls are semicircles.
5. **The compactness dichotomy was overstated into falsity.**
6. **Closure attempt 3** ("terminates at Lee–Yang") was wrong: Lee–Yang has no gauge content,
   Elitzur blocks it structurally, and it is the wrong complex plane besides. Caught by the user.
7. **`g8` was refuted by its own control** (`g9`) — it measured Hankel conditioning, not
   marginality. Caught before use, which is the first time in this note that happened.
8. Irreducibility verified over `ℚ` where the proof needs `ℂ`; `∂H_d` called equal to the real
   discriminant when it is a proper subset; holonomy eigenvalues called real when they are unimodular.

**Pattern.** Items 1, 2, 3, 4, 5 and 6 are one failure mode: a structural claim asserted at a
strength the evidence did not support, with verification designed to confirm rather than to break
it. Three of the six were caught by an adversarial referee, one by the user, and only the last (7)
by a control I ran before drawing the conclusion. The corrective is mechanical and should be
standing policy for the rest of this project: **for every claim of the form "X cannot happen," run
the control that would show X happening in a case where it does.**

---

## 11. Reproduction

| script | produces |
|---|---|
| `g1_locus.py` | discriminant degree `2(d−1)` in coefficients / `d(d−1)` in roots; the `d=3` cusp |
| `g2_scaling.py` | quasi-homogeneity weights; convexity of the ordered-root chamber |
| `g3_submersion.py` | `grad Δ` and Hessian rank per stratum (used in Prop. 3.1) |
| `g4_tangentcone.py` | **superseded — null returns; see §9 item 3** |
| `g5_exact_cone.py` | **superseded — incomplete lower bound; see §9 item 2** |
| `g6_irreducible.py` | irreducibility of `Δ_d` over `ℚ`, `d = 3…7` (insufficient alone; see §3) |
| `g7_refutation.py` | R1, R2 — the half-plane in `H_d`; `det(Hermite) = Δ_d`; PSD ⟺ real-rooted |
| `g8_marginality.py` | **discarded — refuted by `g9`; see §9 item 7** |
| `g9_control.py` | the control that refutes `g8` |
| `g10_transport.py` | §6.2 — exact Sturm measurement of the product↔coefficient transport cost |

Dependencies: `numpy`, `sympy`, `mpmath`.

**Sources.** Hermite (1856); Krein–Naimark, *Lin. Multilin. Alg.* **10** (1981) 265 · Newman, Proc.
AMS **61** (1976) 245 · Newman–Wu, Bull. AMS **57** (2020),
[1901.06596](https://arxiv.org/abs/1901.06596) · Lieb–Sokal, CMP **80** (1981) 153 · Rodgers–Tao,
Forum Math. Pi **8** (2020) e6 · Burnol, [math/0112254](https://arxiv.org/abs/math/0112254), Forum Math. **16** (2004) 789–840 · Griffin–Ono–Rolen–Zagier, PNAS **116** (2019) 11103 ·
Mariño–Putrov, [1110.4066](https://arxiv.org/abs/1110.4066) · Kashaev–Mariño, CMP **338** (2015),
[1501.01014](https://arxiv.org/abs/1501.01014) · Laptev–Schimmer–Takhtajan, GAFA **26** (2016),
[1510.00045](https://arxiv.org/abs/1510.00045) · Kenyon–Okounkov–Sheffield, Duke **131** (2006),
[math/0311062](https://arxiv.org/abs/math/0311062) · Kenyon–Okounkov, Annals **163** (2006) 1019 ·
Mukhin–Tarasov–Varchenko, Annals **170** (2009) 863 · Karp,
[2110.02301](https://arxiv.org/abs/2110.02301) · Nekrasov–Shatashvili,
[0908.4052](https://arxiv.org/abs/0908.4052) · Uhlenbeck, CMP **83** (1982) 31 · Wehrheim,
*Uhlenbeck Compactness*, EMS 2004 · Taubes, [1205.0514](https://arxiv.org/abs/1205.0514) ·
Verbaarschot, [1011.5118](https://arxiv.org/abs/1011.5118) · Lüscher–Weisz, Nucl. Phys. **B240**
(1984) 349 · Meurice et al., [1210.6969](https://arxiv.org/abs/1210.6969) · Clarke–Tipler,
[2304.05245](https://arxiv.org/abs/2304.05245) · Maciocia,
[1202.4587](https://arxiv.org/abs/1202.4587) · Okonek–Teleman,
[alg-geom/9603003](https://arxiv.org/abs/alg-geom/9603003).
