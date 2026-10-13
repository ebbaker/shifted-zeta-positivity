# Round 10: the boundary-data architecture, a verified formula with wrong numbers, and three corrections

**2026-08-26.** Executed in response to a direct challenge to the Yang–Mills closure, which turned
into a reframing of the whole physics side. Two verification jobs and a four-agent literature sweep;
everything numerical recomputed here (scripts §10).

**Headline, in three parts.**

1. **The Dorigoni–Treilis formula is correct; `NOTE_n4_reformulation`'s numbers are not.** The
   transcription flagged as provisional in rounds 4–5 has been verified from the printed paper and by
   two independent recoveries of the residue formula, and the residue structure is now *derived*
   rather than transcribed. But the recomputation gives `Σ|β_n| = 4.03·10⁻⁶`, not `2.114`, and decay
   `e^{−0.795γ}` matching the Stirling estimate `−π/4` exactly, not `−0.674`. The qualitative
   conclusions survive and strengthen; the constant was wrong by five orders of magnitude.
2. **The architecture the programme has been looking for exists, is live, and is not in physics.** It
   is Connes–van Suijlekom's truncated Weil quadratic form: boundary datum built only from primes
   `p ≤ x`, interior object the ground state, **criticality proved at every finite cutoff by a
   theorem that never mentions zeta**, and one missing step — convergence as `x → ∞`. Every slot of
   the screen below is occupied, four of them by theorems.
3. **Three claims I made this session are wrong.** The hypertranscendence obstruction does not work.
   The Lax–Phillips contraction argument is refuted. The universality obstruction holds only in a
   restricted form. §3 gives each in full, because the failure modes are instructive.

---

## 1. The boundary-data reframing

The reframing that organises this round. Rounds 1–9 asked whether geometry could *supply* the
arithmetic. The better question, from `ROUND5` §"structural reason": in a modular function the
Fourier modes are graded by instanton number and the `ξ` factors appear **only in the constant
term** — i.e. the cusp asymptotics. Restated:

> **`ζ` is admissible as boundary data and inadmissible as field data.**

This explains the whole direction audit of round 6 — boundary data constrains the interior, so a
construction that puts `ζ` on the boundary *consumes* it. But that is not the end of the argument,
and the objection that forced this round is correct: if the boundary datum is *defined* using `ζ`,
the interior solution is determined, and if that interior object also has an **independent intrinsic
characterisation** plus a **convergence statement** on the boundary, then "property of the interior
object ⟺ RH" is a genuine reformulation, not a relabelling. Information flows one way; *translation*
goes both.

### 1.1 The five-slot screen

For any candidate:

| slot | question |
|---|---|
| 1 | **Interior** — what is it, what equation does it satisfy? |
| 2 | **Boundary** — what is it, and can it carry the critical strip? |
| 3 | **Where `ζ` enters** — geometric boundary coordinate, or spectral/auxiliary parameter? |
| 4 | **Intrinsic characterisation** — could the interior object be computed to arbitrary precision by someone who has never computed a zeta zero? |
| 5 | **Rigidity** — is there a positivity, unitarity, gap, or self-adjointness condition that *forces* the boundary asymptotics? |

Slot 4 is the Remmen test (`NOTE_n4_reformulation` §4). **Slot 5 is the only slot that can turn a
reformulation into a mechanism, and it is the one nobody had asked systematically.**

---

## 2. Verification of the Dorigoni–Treilis master formula (round 5's open item)

### 2.1 What is now confirmed

**From the printed paper** (arXiv:2307.07491v2 PDF and the JHEP PDF, no disagreement between
preprint and published):

- **Eq. (3.37)**, the Mellin–Barnes kernel, with the `1/ξ(2−2t)` **in the denominator**:

  > `U(a,b,r,s|t) = Γ((r+1−s−t)/2)Γ((r+s−t)/2)Γ((t+r−s)/2)Γ((t+r+s−1)/2) / [2π^r Γ(r) ξ(2−2t)]`
  > `                × ζ(r+1−b−t)ζ(r+1−a−b−t)ζ(t+r−b)ζ(t+r−a−b) / ζ(2r+1−a−2b)`

  (`2π^r` vs `(2π)^r` is mildly ambiguous in the raw text; irrelevant downstream.)
- **Figure 1 caption**, verbatim, recovered three times and matching thesis Figure 5.1 word for word:
  *"Schematic pole structure of U(a,b,r,s|t). … In black, we have an infinite family of poles with
  ℜ(t) = 3/4 (if Riemann hypothesis is correct) coming from the non-trivial zeroes of the Riemann
  zeta. The contour of integration, ℜ(t) = 1/2, is indicated in red."*

**The residue formula**, recovered from Treilis's IHES slides (18 Oct 2023, slide 25, "Exact strong
coupling limit") **by two agents independently, character-identical**, and matching
`NOTE_n4_reformulation` §2 exactly:

> `β(ρ) = 2 ξ(t+s₁+s₂−1) ξ(t+s₁−s₂) ξ(t+s₂−s₁) ξ(t+1−s₁−s₂)`
> `        / [ (1−t−λ)(t−λ) Γ(s₁)Γ(s₂) π^{1/2−t} Γ(t−1/2) ζ′(2t−1) ]`,  at `t = 3/4 + iγ/2`

**And now derived rather than transcribed.** With `ξ(s) = π^{−s/2}Γ(s/2)ζ(s)`:
`ξ(2−2t) = ξ(2t−1)` by the functional equation, so `Res_{t₀}[1/ξ(2−2t)] = 1/(2ξ′(2t−1))`, and at a
zero `ξ′(2t−1) = π^{1/2−t}Γ(t−1/2)ζ′(2t−1)` **exactly**. Verified to 40 digits at `n = 1…5`, plus a
contour-integral check of the residue itself (rel. diff `~10⁻⁴¹`). So the denominator in the slides'
formula *is* the residue of the printed kernel, and the transcription risk is discharged.

**Bonus: this pins the convention.** The identity holds only for `ξ(s) = π^{−s/2}Γ(s/2)ζ(s)`, not
for Riemann's `ξ` with the `s(s−1)/2` factor. Round 4–5 never fixed this, and it matters for the
numerics.

> **Verdict: the §2 formula and the §3.1 argument list (`t+2, t, t, t−2` at `λ=4, s₁=s₂=3/2`) are
> correct as recorded. The round-5 "provisional" flag on the formula is lifted.**

### 2.2 What is now known to be wrong

Recomputed at 20/30/40/60 dps (stable to 15 digits):

| `n` | `γ_n` | `\|β_n\|` recomputed | `NOTE` recorded |
|---|---|---|---|
| 1 | 14.1347 | `4.010·10⁻⁶` | 1.86 |
| 5 | 32.9351 | `1.895·10⁻¹²` | `6.6·10⁻⁴` |
| 10 | 49.7738 | `6.851·10⁻²⁰` | `6.4·10⁻¹⁰` |
| 20 | 77.1448 | `4.559·10⁻²⁸` | `1.4·10⁻¹⁶` |
| 25 | 88.8091 | `8.523·10⁻³²` | `8.1·10⁻²⁰` |

- **Decay:** `log|β_n| = −0.795 γ_n − 2.34`. The note recorded `−0.674` and explained the gap from
  the Stirling estimate `−π/4 = −0.7854` as "attributable to `1/ζ′(ρ)` and the polynomial factors."
  The corrected fit lands *on* `−π/4`. **The note's own consistency check was the tell, and it was
  read as a tolerable discrepancy rather than as a symptom.**
- **Envelope constant:** `Σ_{n≤80}|β_n| = 4.0342·10⁻⁶` over positive ordinates, `8.0685·10⁻⁶` over
  all zeros. Recorded: `2.11443250`. **Wrong by ~5–6 orders.**

**Qualitative conclusions all survive, and two strengthen:**

- **Absolute convergence** — yes, far more decisively than recorded (`e^{−πγ/4}`; the `n=80` term is
  `10⁻⁷⁰`).
- **§3.1 non-degeneracy** — confirmed, and simpler than stated. At `t = 3/4 + iγ/2` the arguments are
  `2.75+iγ/2`, `0.75+iγ/2` (twice), `−1.25+iγ/2`. `ξ` has zeros only in the critical strip; the first
  reflects to `Re = 2.75`, the third to `Re = 2.25`, both outside; the middle has `Re = 3/4`, so it
  vanishes only if `3/4+iγ/2` is itself a nontrivial zero, which under RH needs `Re = 1/2`.
  **`β(ρ) ≠ 0` for every `ρ`, unconditionally under RH.**
- **§3.3 converse** — confirmed. The poles of `1/ξ(2−2t)` sit at **both** `t = 1−ρ/2` and
  `t = (1+ρ)/2` (the functional equation maps zeros to zeros), so a zero with `σ = Re ρ > 1/2`
  contributes the dominant exponent `1−σ/2 < 3/4`. Failure of RH is visible as an *enhanced*
  envelope. The note's `t = 1−ρ/2` labelling and the paper's `t = 3/4+iγ/2` are the same pole set.
- **The proposition stands**, with the constant corrected:
  `|oscillatory part of a₀| ≤ 8.07·10⁻⁶ · τ₂^{3/4}` uniformly, over all zeros.

**Still not seen:** the paper's own §4.2 printed equation (every full-text route truncates at eq.
(4.3)–(4.5)) and thesis (5.82) (truncates in Ch. 4). Both are now non-load-bearing: the formula is
independently derived and the numerics are recomputed. Thesis Figure 5.2's caption confirms the
numerics were run for exactly `a₀(4; 3/2, 3/2)` against the first 10 zeros.

---

## 3. Three corrections to claims made this session

Recorded in full because the failure modes are more useful than the claims were.

### 3.1 The hypertranscendence obstruction does not work

**The claim I made.** `ζ` satisfies no algebraic ODE (Ostrowski 1920); the YM equations are
polynomial in the connection and its derivatives; so any symmetry reduction with finitely many
components in one variable gives a polynomial ODE system; so by differential elimination every
component satisfies an algebraic ODE; so `ζ` cannot be a field component. I presented this as a hard
no and as new to the record.

**The theorem is real, my attribution was wrong, and the argument is invalid.**

- *Attribution.* The chain is **Hölder** (Math. Ann. 28, 1886/87, for `Γ`) → **Hilbert** (1900 ICM —
  it is his *theorem*, proved from Hölder plus the functional equation, not merely an assertion) →
  **Stadigh** (Helsingfors dissertation, 1902 — the detailed execution) → **Ostrowski** (Math. Z. 8
  (1920) 241–298 — a second proof plus genuine strengthenings to algebraic *difference*-differential
  equations, and no algebraic PDE for `ζ(x,s)`). I had the order and the credit wrong.
- **The elimination step is false as stated.** One-line counterexample: the system `y₁′ − y₂ = 0` in
  two unknowns is polynomial and finite, `(ζ, ζ′)` is a solution, and `y₁ = ζ` is a component. The
  system is *underdetermined*. The correct statement needs differential dimension **zero** —
  resolved form `y′ = R(t,y)` — as a hypothesis. Ovchinnikov–Pogudin–Vo (IMRN 2022) exist precisely
  because the elimination ideal can be `{0}`.
- **Gauge freedom is fatal unless fixed.** A one-variable reduction retains residual `t`-dependent
  gauge transformations `A ↦ gAg⁻¹ + g′g⁻¹`. Starting from a flat connection you can gauge a
  component into essentially any function, hypertranscendental included. Before gauge-fixing the
  reduced system has positive differential dimension and the conclusion is simply false. And many
  integrable reductions of SDYM remain underdetermined *after* gauge-fixing.
- **The decisive counterexample is `Γ` itself.** `Γ` is hypertranscendental by Hölder, yet it appears
  as a **connection coefficient** of the hypergeometric and Bessel equations — maximally rigid
  objects. Rigidity of the equations does not confer rigidity on the transcendental functionals they
  generate. And `ζ` appearing as the scattering coefficient of a *linear* PDE on the modular surface
  (§3.2) is a second instance, inside this very programme.
- **Calibration.** Bournez–Pouly (ICALP 2017), following Rubel (1981): there is a **fixed** polynomial
  vector field in `d` variables such that for any continuous `f` and any error tolerance, some
  initial condition gives an **analytic** solution whose first component approximates `f` to that
  tolerance everywhere. So even the repaired argument forbids only *exact equality* with `ζ` and
  permits arbitrarily good approximation — which leaves untouched every programme that reaches `ζ` as
  a limit.

> **Net: what survives is "`ζ` is not literally a gauge-fixed field component of a
> differential-dimension-zero reduction, in the same variable." That is not a serious constraint, and
> it says nothing about determinants, tau functions, spectral determinants, monodromy, Stokes data,
> or scattering coefficients — which is where every real construction lives.** The boundary-vs-field
> distinction in §1 survives as an *observation about where `ζ` is found*, not as a theorem about
> where it can be.

### 3.2 The Lax–Phillips contraction argument is refuted

**Confirmed:** attributions (Pavlov–Faddeev 1972 — Pavlov is first author; Lax–Phillips, Annals of
Math. Studies 87, 1976), and the scattering matrix `φ(s) = ξ(2s−1)/ξ(2s)` with poles at `s = ρ/2`,
hence on `Re s = 1/4` under RH (I said the poles were at `ρ/2` but should have named the line as
`1/4`, not `1/2`). Zworski's 2017 survey states it as standard: the zeros *are* the resonances of the
Laplacian on the modular surface.

**Refuted:** the automorphic energy form is **indefinite** — Lax–Phillips, Bull. AMS 2 (1980) 264:
*"In general `E_F` is indefinite for automorphic data,"* from standing waves and exponentially
increasing solutions. So `Z(t) = P₊U(t)P₋` is **not** a contraction; they have only
`‖Z(t)‖ ≤ Ce^{ωt}`. I imported the abstract positive-energy Lax–Phillips setting (where the semigroup
*is* contractive — Baumgärtel) into the automorphic one, where it fails. Worse: **even if it were a
contraction, `Re σ ≤ 0` would give `Re ρ ≤ 1`, the trivial Euler-product bound** — not the classical
zero-free region. I overstated what a contraction would buy in the same breath as asserting it.

**The real gap, in their own words** (Bull. AMS §6, pp. 283–4): they restate RH as
`lim sup t⁻¹ log‖Z″(t)f‖_E < −1/4`, note that `2B″ + 1/2` would be skew-Hermitian exactly under RH,
and conclude: *"all that is missing is an appropriate inner product on `ℋ′_c` which makes (6.20)
skew-hermitian."*

> **So the missing ingredient is Hilbert–Pólya, unmoved — not a positivity the setup "does not
> supply." The reformulation is a correct translation whose difficulty is identical to the original.
> My conclusion was right; every reason I gave for it was wrong.**

Two further corrections. **Do not attribute a critique of Lax–Phillips to Connes**: his
absorption-spectrum choice is justified cohomologically (the `H¹` term enters the Lefschetz formula
with a minus sign, so the Pólya–Hilbert space appears as `⊖ℋ`), and math/9811068 does not engage
Lax–Phillips at all. And the community verdict is **absence rather than refutation**: Bombieri's Clay
description, Conrey's 2003 Notices survey, and Sarnak's Clay note all omit it; Sarnak mentions only
that Eisenstein series have poles at zeros "hence the zeros can in this way be thought of as
resonances." Post-1990 revivals exist and none produced new information: **Burnol** (math/0001013 —
an adelic Lax–Phillips whose *causality* is equivalent to RH for abelian `L`-functions of `K`,
recast as a Hilbert-space closure problem and explicitly related to **Nyman–Beurling**; directly
relevant to round 9), **Uetake** (Ann. Polon. Math. 92 (2007)), **Friedman–Jorgenson–Smajlović**
(Ann. Inst. Fourier 70 (2020)). Burnol's structural remark is the one to keep: *"if the Riemann
Hypothesis holds, then the scattering itself is of a trivial nature, and says absolutely nothing on
the zeros on the critical line."*

### 3.3 The universality obstruction holds only in restricted form

**Confirmed, with corrections to hypotheses.** Voronin: `K` compact `⊂ {1/2 < Re s < 1}` with
**connected complement** (not "simply connected"), `f` continuous on `K`, holomorphic inside,
**non-vanishing on all of `K`**; then the set of admissible `τ` has **positive lower density**.
**Universality on the critical line is false, not open** — Andersson (arXiv:1207.4927), obstruction
being that the Hardy `Z`-function is real while `ζ` on the line is not.

**My inference is not a theorem as stated, but a restricted version is.** What holds: if a condition
`𝒞` on holomorphic functions near a disc `K ⊂ (1/2,1)` is (a) closed under locally uniform
convergence, (b) invariant under vertical translation, and (c) fails for some non-vanishing `f`, then
`ζ|_K` does not satisfy `𝒞`. Hypothesis (b) is a real restriction: **an ODE with `s`-dependent
coefficients is not translation-invariant, so universality does not kill it on a disc.** For that one
needs Voronin's **functional independence** (arbitrary continuous `f_l`, not just polynomials —
strictly stronger than hypertranscendence, by a different route), which constrains identities holding
for *all* `s`, i.e. global relations.

**And the decisive caveat:** `ζ` *does* satisfy powerful nontrivial constraints — the functional
equation and the Euler product. Both are **nonlocal**. So the honest statement is:

> **Neither hypertranscendence nor universality touches nonlocal or infinite-order relations — which
> is exactly where every serious `ζ` programme lives.** Stated as "rigid structures cannot contain
> `ζ`" the claim is false; stated for local, closed, translation-invariant constraints it is a
> theorem and nearly vacuous.

---

## 4. The sweep: the one live architecture

### 4.1 Connes–van Suijlekom, the truncated Weil quadratic form

Every slot occupied, four by theorems. This is the item of the round.

| slot | content |
|---|---|
| 1 **Interior** | The ground state `η_x` (lowest eigenvector) of the truncated Weil quadratic form on `L²([−L/2, L/2])`, `L = log x`. A linear eigenvalue problem. |
| 2 **Boundary** | The Weil distribution `𝒟 = 𝒟_∞ + 𝒟_pole + 𝒟_prime` on the interval `[0, log x]`, with cutoff `x` acting as a scale parameter. **Carries the critical strip**: `η̂_x(z)` is entire, and "on the critical line" *is* "`z` real". |
| 3 **Where `ζ` enters** | **It does not enter the input.** Input is `{log p : p ≤ x}`, `p^{−m/2}`, the archimedean digamma term `h₊(τ) = −log π + Re Ψ(1/4 + iτ/2)`, and the pole term. Zeros come **out**. Direction: **produces**. |
| 4 **Intrinsic** | **Yes, verified twice independently.** Connes gets the first 50 zeros to `2.6·10⁻⁵⁵`–`10⁻³` from primes `< 13`; Groskin's independent implementation (arXiv:2605.20224) reports first-zero error falling to `~1.5·10⁻¹⁶⁸` at `c = 67`, and `γ₁…γ₁₀` to 307–329 matching digits at `c = 100`. Nobody needed a zero to do this. |
| 5 **Rigidity** | **A proved theorem at every finite cutoff.** Connes–van Suijlekom, *Comm. Math. Phys.* **406**:312 (arXiv:2511.23257): for a real distribution `𝒟` on `[0,L]` whose associated quadratic form is a lower-bounded self-adjoint operator with simple isolated lowest eigenvalue and even eigenfunction `ξ`, **all zeros of `ξ̂` lie on the real line**. Criticality is *forced* by positivity plus self-adjointness, with RH not assumed. |

**The single missing step, quoted** (Connes, arXiv:2602.04022 §5): *"What we do not know is that,
when we increase the upper limit, which was x = 13 here, the corresponding set of zeros will converge
towards the zeros of zeta. This is something which at this point is not proved."* Groskin: *"If the
convergence holds, RH follows by Hurwitz's theorem applied to the Mellin transforms — but the
convergence itself is unproven."*

**Honest calibration, and it matters.** The CvS criticality theorem **never mentions zeta** — it holds
for *any* lower-bounded real even kernel. So it is cheap in the sense that it does not know it is
about `ζ`; all the arithmetic is injected by taking `𝒟` to be the truncated Weil distribution, and
all the difficulty is in the limit. Groskin also reports that his own empirical convergence-rate fit
`|log₁₀ λ_min| ≈ 13.24 c^{0.634}` is **falsified at `c = 100` by 49 orders of magnitude** — even the
numerics do not yet suggest the convergence law.

**Relation to the record.** Round 6 recorded Connes' extremisation numerics and the unproved
convergence step. What round 6 did *not* have: the CvS theorem that supplies slot 5, the independent
Groskin implementation, or the recognition that this is the architecture the programme's own screen
selects for. Round 6 filed it as "Connes' 2026 position is that the live route is analytic"; it is
better filed as **the only known instance of the boundary-data architecture with rigidity.**

### 4.2 Deninger — the same architecture, the complementary failure

| slot | content |
|---|---|
| 1 | Reduced leafwise cohomology `H̄^i(X,ℝ)` of a foliated dynamical system `(X, φ^t, ℱ)`, flow conformal on `Tℱ` with factor `e^t`; infinitesimal generator `Θ`. |
| 2 | No boundary. Closed orbits ↔ closed points of `Spec 𝔬`, lengths `log p`. |
| 3 | **Spectrally, and as an output**: `ζ̂_K(s) = ∏_i det_∞((s−Θ)/2π \| H^i_dyn)^{(−1)^{i+1}}` — zeta as a regularised characteristic polynomial. |
| 4 | **Yes** — the system would be defined purely geometrically, primes entering as periodic orbits. Best slot-4 score found, conditional on the object existing. |
| 5 | **Genuine, and of exactly the right type**: on `H̄¹`, `Θ = α/2 + S` with `S` skew-symmetric w.r.t. the leafwise inner product, so all `ρ ∈ Sp¹(Θ)` have `Re ρ = α/2`; with `α = 1`, RH follows. **An inner product forcing skew-symmetry** — i.e. Hilbert–Pólya, but with a mechanism. |

**Status, updated.** Deninger, arXiv:1807.06400, now *constructs* dynamical systems whose periodic
orbits correspond to closed points of arithmetic schemes (via sheafified rational Witt vectors, after
Kucharczyk–Scholze) — but **infinite-dimensional**, forced, since `α = 1` cannot hold for manifolds.
**Álvarez López–Kim–Morishita (arXiv:2410.20758) have proved Deninger's conjectured determinant
formula** — for surface bundles over `S¹` with Anosov/Axiom-A suspension flows, and minimal `ℝ`-Lie
foliations with dense leaves. **Neither class contains `Spec ℤ`.** So: *the trace formula is now
proved exactly where the arithmetic is absent.* Morishita (arXiv:2508.15971) builds a Galois-
equivariant map from Deninger's systems to Connes–Consani's adelic spaces; no RH progress claimed.

> **The useful asymmetry, worth filing separately in the ledger: Deninger lacks the object
> (cohomology + trace formula with fixed points) while having the inequality mechanism for free.
> Connes–Consani have the trace formula semi-locally and lack the inequality (Weil positivity).
> Two different failure modes of the same architecture.**

Also in this family: **Meyer** (math/0311468, Duke 127 (2005)) constructs unconditionally a *virtual*
representation of the idele class group whose character is the Weil distribution, with zeros as
eigenvalues of finite algebraic multiplicity, and proves the spectrum lies in the critical strip.
Because it is *virtual* — a formal difference `π₊ ⊖ π₋` — there is no positive Hilbert space and
nothing to force reality. Meyer's own words: *"Since I have not been able to do this computation, I
have developed an alternative spectral interpretation that is no longer directly related to the
Riemann Hypothesis."*

---

## 5. AdS₃/CFT₂: right dimension, occupied slot 5, provably RH-insensitive

The area where the geometric boundary finally has the right dimension. Three genuine papers, all
from the harmonic-analysis-on-`SL(2,ℤ)\ℍ` lineage.

| | Benjamin–Chang 2208.02259 | BCFR 2505.18314 | Perlmutter 2509.21672 |
|---|---|---|---|
| interior | scalar projection of a Narain torus partition function | `Z^scalars_p − Z^gravity_{j=0}` | completed `Λ_𝒵(s)`, a self-dual **degree-4** `L`-function attached to any 2d CFT torus partition function |
| boundary | cusp `y → 0`, **1 real dimension** | same | the `s`-plane (a copy of `ℂ`) — but the Rankin–Selberg variable |
| where `ζ` | spectral (Eisenstein `s`); zeros are poles picked up by a contour shift | same | **both**: `ζ(2s)` in the Eisenstein normalisation, *and* — for the compact free boson — the attached `L`-function **is a product of two Riemann zetas** times an analytic factor |
| intrinsic | **yes**, strongly | **yes** | **yes** — Dirichlet coefficients are degeneracy differences in the CFT spectrum |
| rigidity | ≈ 0, self-declared | **negative** — the residues `δ_k` are **not sign-definite**, so bootstrap positivity cannot be turned on the zeta terms | **non-trivial: the only producer found** |

**The Benjamin–Chang exercise is unsolved, and this is now checked rather than assumed.** Their
sentence, verbatim from three sources: *"it would be extremely interesting if there were a physical
reason why the scalar partition function, with the first two leading terms subtracted off, had to
scale as `T^{c/2−3/4}`. This would give a 'physics explanation' of the Riemann hypothesis. We leave
this problem as an exercise to the reader."* All 25 citing papers were enumerated and checked; only
two engage the zeta structure, and neither attempts the envelope. **Connes' Feb 2026 survey contains
no CFT, bootstrap, holography, or `AdS₃` content at all** — the person best placed to connect
bootstrap positivity to Weil positivity has not.

**Structural reason it stays unsolved in this form:** the two rigidity sources are both closed.
Positivity is killed by BCFR's sign-indefiniteness — and the working technology in the area applies
functionals that **annihilate** the `y^{(1+z_k)/2}` terms, i.e. deliberately removes the zeta content
to get usable bounds. Unitarity constrains the *light* spectrum, while the `O(e^{−2πΔ_gap T})` tail
is exponentially suppressed at high `T` and cannot see a power-law envelope. The envelope is the
growth rate of a contour-shift residue sum, not an asymptotic of any physically bounded quantity.

**Perlmutter's mechanisms, and why they cannot reach RH as stated.** Genuine physics → arithmetic:
spectral gap ⟹ global zero-**density** bound; modular invariance ⟹ the zero sum rule
`Σ_ρ 1/ρ = ℓ₁/ℓ₀ − φ` with `φ = log(8π²) + 2γ_E − 1 ≈ 4.52`; RMT universality ⟹ subconvexity. He
explicitly does not assume RH. But: a density bound **counts** zeros rather than **locating** them,
and the sum rule is **provably RH-insensitive** — by his own eq. (4.38), `B < ∞` for any self-dual
order-one `L`-function *regardless* of whether the zeros lie on the line. **So the architecture is
right and the arithmetic produced is real, but nothing yet produces a location statement.**

**Two follow-ups this identifies.**

1. **Is the compact-free-boson "analytic factor" zero-free?** (§10.2 of 2509.21672, which every fetch
   failed to reach.) If yes, there is a specific `c = 1` CFT whose attached degree-4 `L`-function has
   exactly the (doubled) Riemann zeros, and every physics-derived constraint in that paper becomes a
   statement about `ζ`. This is the only identified path from 2d CFT to the Riemann zeta itself.
2. **Bootstrap positivity vs Weil positivity — nobody has looked.** Two independent searches found
   nothing connecting the modular bootstrap's semidefinite-programming positivity or extremal
   functionals to Weil's explicit-formula positivity or the Weil quadratic form. Both frameworks are
   literally "positivity of a functional applied to a spectral density." BCFR tells us exactly why
   the naive version fails, which is useful information for building a non-naive one. **Given §4.1,
   this is the seam where the two live architectures could meet.**

**One correction to our own record:** Benjamin–Chang contains **no comparison to N=4 SYM**. The
non-cancellation of the `Λ` factors is printed; the "unlike N=4" framing is ours, and should be
attributed to us.

---

## 6. p-adic and adelic: dies on dimension, with one inert curiosity

**The generic obstruction is slot 2 and it is decisive.** In p-adic AdS/CFT the bulk is a
`(q+1)`-regular Bruhat–Tits tree and the boundary is `ℙ¹(ℚ_q)`: compact, totally disconnected,
**topological dimension 0**. No complex-analytic direction anywhere in the geometry. The complex
variable carrying the zeta argument is the **conformal weight `Δ`** — a label on bulk field content,
i.e. slot-3 auxiliary. The critical strip lives in the space of masses, and nothing in the geometry
constrains complex `Δ`.

**The one notable finding.** Gubser–Knaute–Parikh–Samberg–Witaszczyk (arXiv:1605.01061, CMP 352
(2017) 1019) §4.1 *does* assemble over all primes and reach the global completed zeta: they define
`ζ_𝔸(s) = π^{−s/2}Γ(s/2)ζ(s)`, note `ζ_𝔸(s) = ζ_𝔸(1−s)`, and state that *"its non-trivial zeros are
the same as the non-trivial zeros of `ζ(s)`."* Then they do nothing with them — the product is
labelled "naive", it diverges, the zeros sit at unphysical complex `Δ`, and no follow-up paper picks
it up. **Zeros visible and inert.**

**Freund–Witten is a consumer, decisively — my flagged "rare producer" candidate is dead.** The exact
statements are `A₄^{(∞)}∏_p A₄^{(p)} = 1` and `Γ_∞(z)∏_p Γ_p(z) = 1`. The mechanism is fully exposed
by the two identities invoked: the completed functional equation `ζ_∞(x)ζ(x) = ζ_∞(1−x)ζ(1−x)` and
the Euler product `∏_p ζ_p(z) = ζ(z)`. Since the Veneziano kinematic arguments satisfy
`(−1−s) + (2+s) = 1`, every local factor is a ratio `ζ_v(x)/ζ_v(1−x)`, and the product collapses by
Riemann and Tate. **The adelic product formula is the functional equation of the completed zeta,
rearranged in a physics costume.** Three further nails: the distributivity step is an *assumption*
that **fails for the 5-point amplitude** (arXiv:2211.01611); the product converges nowhere; and the
rigorous version (Vladimirov–Sapuzhak) replaces the bad step by a regularisation *built on Tate's
thesis* — more arithmetic input, not less. Freund's own 2017 retrospective never mentions zeta zeros.
Slot 5 is *negative*: the only zero-sensitive condition available (analyticity of the adelic
amplitude) would demand a zero-free region strictly stronger than RH, and is imposed on a
nowhere-convergent product.

Also checked and empty: Heydeman–Marcolli–Saberi–Stoica–Vasudevan (no zeta at all);
Hung–Li–Melby-Thompson; Bhattacharyya et al.; Huang–Jepsen (single place by construction);
Manin–Marcolli hep-th/0201036 (**wrong zeta** — Selberg, not Riemann; and the Selberg RH is trivial
via the trace formula, so there is nothing to force); Dragovich's zeta strings (pure consumer, zeta
inserted as input); Berkovich-space holography (no such correspondence with zeta content exists);
arithmetic Chern–Simons theory (Kim) — a genuine physics→arithmetic **producer**, but what it produces
is class-field-theoretic (Hilbert symbols, reciprocity), not analytic. **Architecturally interesting:**
Huang–Stoica–Yau (arXiv:2001.01721) prove `∏_v G_v(x,y) = 1` for Vladimirov-derivative Green's
functions — an identity among intrinsic interior objects, one per place, equivalent to a global
functional equation. Right shape, and a functional equation is not RH; direction ambiguous enough to
merit a closer read than a sweep allows.

---

## 7. Primon gas and Bost–Connes: pole-only, and the reason is structural

Both **produce** arithmetic — and only `ζ`'s abscissa of convergence.

- **Primon gas** (Julia; Bakas–Bowick JMP 32 (1991) 1881; Spector CMP 1990): `Z(β) = ∏_p(1−p^{−β})^{−1}
  = ζ(β)`; the Hagedorn divergence **is** the pole at `s = 1`; the Möbius function is `(−1)^F`. Slot 2
  admits only real `β > 1` — **nothing that can carry a critical strip**. Schumayer–Hutchinson's
  §III.E is about Bose–Einstein condensation and the pole; the review has no Bost–Connes and no
  Connes-trace-formula section at all, so it is not a source on either.
- **The Lee–Yang route is closed in print.** The obvious hope — `Z(β) = ζ(β)`, so Fisher zeros are
  zeta zeros, so RH is "all Fisher zeros on `Re β = 1/2`" — is a relabelling, and Contucci–Knauf state
  why it cannot be repaired: *"there exist versions of the Lee-Yang theorem predicting zerofree half
  planes in the inverse temperature plane, unfortunately these theorems cannot be applied to the
  above spin chain, since its interaction includes multi-body terms."* The Euler-product structure is
  **inherently multi-body** (an integer is a multi-particle state), and there is no finite-volume
  polynomial to run Lee–Yang on. This is a clean general no-go for the family, and it complements
  `NOTE_existence_loophole` §5.1's finding that Lee–Yang has no gauge content.
- **Bost–Connes** (Selecta Math. 1 (1995) 411): `𝒜 = C(Ẑ) ⋊ ℕ^×`, `Hε_k = log k · ε_k`,
  `Z(β) = ζ(β)`, phase transition with symmetry breaking at `β = 1`, extremal KMS states for `β > 1`
  a torsor over `Ẑ^*`, class-field-theory isomorphism intertwining Galois action with symmetries,
  fabulous states valued in `ℚ^cycl`. **Genuine arithmetic rigidity — pointed at Hilbert's twelfth
  problem, not RH.** Three linked reasons slot 5 is empty: `ζ` enters only as `Tr(e^{−βH})`, so the
  only visible feature is the abscissa of convergence (hence the transition at the *pole*); KMS
  states are indexed by **real** `β` and there is no analytic continuation of a *state*; and the
  arithmetic payload is values of states on the arithmetic subalgebra, an abelian class-field datum
  with no known map to the zero set. The one attempt to extract a zero statement (Planat–Solé–Omar,
  J. Phys. A 44 (2011) 145203) recovers **Nicolas' criterion** — imported wholesale from elementary
  number theory and dressed in BC language. Relabelling.

> **BC is the warm-up for the *space* (the adele class space), not for the zeros. The bridge to the
> zeros is a different construction — §4.1.**

---

## 8. The built-from ledger: every "Riemann operator", classified

The single most useful negative product of the sweep. Applying slot 4 bluntly:

| proposal | verdict |
|---|---|
| Berry–Keating `H = xp` (SIAM Rev. 41 (1999) 236) | **neither** — analogy at the level of the *smoothed* counting function; their own words, "an **(unknown)** hermitean operator"; primes enter as periodic orbits of period `log p`, consumed from the explicit formula |
| Sierra–Rodríguez-Laguna (PRL 106 (2011) 200201); Sierra–Townsend (PRL 101 (2008) 110201) | **neither** — spectrum aligns with **average** Riemann zeros |
| Sierra, Symmetry 2019 / arXiv:1601.01797 | **built-from**, self-admitted — the self-adjoint extension is tuned via the phase of `ζ(1/2+iE)`; *"one needs to fine tune a parameter to see each individual zero"* |
| Bender–Brody–Müller (PRL 118 (2017) 130201) | **built-from, tautologically** — eigenfunctions are Hurwitz zetas `ψ_z(x) = −ζ(z, x+1)` and the boundary condition `ψ_z(0) = 0` **is** `ζ(z) = 0`. Critiqued by Bellissard (arXiv:1704.02644: the strategy "does not actually work") |
| LeClair–Mussardo (JHEP 2024); LeClair (arXiv:2406.01828) | **built-from** — the quantisation condition is `ϑ(t_n) + arg ζ(1/2+δ+it_n) = (n−3/2)π`, i.e. Riemann–von Mangoldt rearranged and called a Bethe ansatz |
| Suo (PRA 112 (2025) L060201) | **built-from**, admitted in the abstract; eigenstates not normalisable |
| Yakaboylu (arXiv:2408.15135) | **built-from** — the zero set appears as a parameter in the spectral formula |
| Connes `D_χ` (Selecta 1999) | **produces** — canonically defined, zeros come out; but only the **critical** zeros (absorption spectrum), non-critical ones being resonances, so off-line zeros yield no contradiction. Connes' own diagnosis: *"the shortcoming of this construction is in the artificial weight `ρ(x)` … but only sees the zeros which are on the critical line"* |
| Meyer (Duke 2005) | **produces**, unconditionally, and sees **all** zeros — but virtual, hence no positivity, hence nothing to force |
| **Connes–van Suijlekom (2025/26)** | **produces, with criticality proved at finite cutoff** — §4.1 |

**The pattern, stated flatly:** every proposal claiming the individual zeros as an exact spectrum has
`ζ = 0` or `arg ζ` inside its definition. Every honestly zero-free proposal reproduces only the
smoothed counting function `N̄(E) = (E/2π)log(E/2πe) + 7/8` — the Weyl term, an archimedean
gamma-factor fact carrying no information about zero locations. **There is no middle ground in the
literature except §4.1.**

Two entries not previously on our radar, both worth knowing:

- **Hartnoll–Yang, arXiv:2502.02661**, *The Conformal Primon Gas at the End of Time*: BKL dynamics
  near a spacelike singularity maps to a particle in half the modular fundamental domain;
  modular-invariant states define odd automorphic `L`-functions; the dilatation-basis wavefunction
  *"is proportional to the `L`-function along the critical axis and hence vanishes at the nontrivial
  zeros, realising suggestions by Connes and Berry-Keating."* **Produces** — but the emergence is
  Riemann's own 1859 `θ`-integral representation of `ξ`, restated in conformal-quantum-mechanics
  language. Slot 5 empty. An elegant realisation of the absorption-spectrum picture with no added
  rigidity. *(Medium confidence — abstract truncated; worth a proper read.)*
- **Wei et al., Nature Communications (2026)**, arXiv:2511.11199: a probe qubit on a system with
  `E_n = log n`; the amplitude reproduces `η(s) = (1−2^{1−s})ζ(s)`, measured on a five-qubit NMR
  processor. Slot 2 is the first in this family that **can** carry the strip (`(β,t)` spans two real
  dimensions, `s = β + it`). But `ℒ` *is* `η(s)` up to normalisation, so its Fisher zeros are `ζ`'s by
  construction, and the `N → ∞` limit destroys any finite-volume Lee–Yang structure. **A quantum
  algorithm for numerically verifying RH, not a reformulation.**

---

## 9. Consequences for the ledger

### 9.1 Corrections to this session's claims

1. The hypertranscendence obstruction **does not work** (§3.1). Attribution was also wrong:
   Hilbert 1900 / Stadigh 1902, strengthened by Ostrowski 1920.
2. The Lax–Phillips contraction argument is **refuted** (§3.2); the correct gap is the missing inner
   product, i.e. Hilbert–Pólya. Do not attribute a Lax–Phillips critique to Connes.
3. The universality obstruction holds only for **local, closed, translation-invariant** constraints
   (§3.3), and `ζ`'s own constraints are nonlocal. Universality on the critical line is **false**,
   not open.
4. Freund–Witten is a **consumer**, not the rare producer I suggested (§6).
5. `Σ|β_n| = 4.03·10⁻⁶`, not `2.114`; decay `−π/4`, not `−0.674` (§2.2).

### 9.2 Corrections to earlier rounds

6. **Round 5's "provisional" flag on the DT formula is lifted** — the formula is verified and now
   derived. But **round 5's headline numerical fact was wrong**, and the note's own Stirling
   consistency check was the symptom that got explained away rather than chased. *Standing rule
   reinforced: when a computed constant disagrees with a crude structural estimate, chase it.*
7. **Round 6 filed Connes' extremisation as "Connes' current position"; it should be filed as the
   only known instance of the boundary-data architecture with a proved rigidity slot** (§4.1). The
   CvS theorem and Groskin's independent implementation were not in the record.
8. **Deninger was never in the record at all**, and belongs there as the complementary failure mode
   to Connes–Consani (§4.2): lacks the object, has the inequality.
9. Benjamin–Chang contains **no N=4 SYM comparison**; that framing is ours (§5).
10. The `ROUND5` "arithmetic is in the zero mode, classical solutions in the nonzero modes" statement
    is sound as an **observation**, but the attempt to upgrade it to a theorem via hypertranscendence
    fails (§3.1). Keep it as an observation.

### 9.3 The screen, revised

`NOTE_existence_loophole` §8's four falsification criteria stand. Round 8's degeneration screen
stands. Add:

> **Slot-5 screen.** For any candidate reformulation, ask whether some positivity, unitarity, gap, or
> self-adjointness condition *forces* the boundary asymptotics — and demand that the forcing theorem
> be stated without reference to `ζ`. `AdS₃/CFT₂` fails it (positivity killed by sign-indefinite
> residues). Perlmutter passes it and produces RH-*insensitive* arithmetic. Connes–van Suijlekom
> passes it with a proved theorem, and the whole difficulty relocates to a limit.

> **Anti-tautology screen, sharpened.** "Could someone compute this object to arbitrary precision
> having never computed a zeta zero?" §8 shows this single question classifies the entire
> Riemann-operator literature correctly, and that all but three entries fail it.

---

## 10. What to do next

1. **Perlmutter §10.2: is the compact-free-boson analytic factor zero-free?** The only identified path
   from 2d CFT to the actual Riemann zeta. Blocked only by fetch truncation on a 73-page paper.
   Cheap. **Highest value per unit effort in this round's output.**
2. **Bootstrap positivity vs Weil positivity.** Unworked by anyone, including Connes. Both are
   positivity of a functional on a spectral density; BCFR tells us why the naive version fails; §4.1
   gives the target. This is where the two live architectures could meet.
3. **Read Burnol, math/0001013.** An adelic Lax–Phillips whose causality is RH-equivalent, recast as
   a Hilbert-space closure problem and *explicitly related to Nyman–Beurling* — which round 9 made
   the programme's one live route. This connection was not known to us.
4. **Rewrite `NOTE_n4_reformulation` §3.2** with the corrected constant, and §2 with the derivation
   replacing the transcription caveat. The proposition survives; the "explicit constant `2.1145`"
   selling point becomes `8.07·10⁻⁶`.
5. **Do not pursue:** the hypertranscendence route to a no-go; p-adic/adelic holography as a bridge
   to global `ζ`; Freund–Witten; the primon-gas/Lee–Yang route (closed in print by Contucci–Knauf);
   any further "Riemann operator" of the built-from type.

---

## 11. Reproduction

| script | produces |
|---|---|
| `v_residue.py` | §2.1 — functional-equation check, pole locations, the `ξ′(2t−1) = π^{1/2−t}Γ(t−1/2)ζ′(2t−1)` identity to 40 digits, contour-integral residue check |
| `n1_residues.py` | §2.2 — `β_n` table, convergence sums, decay fit |
| `n2_checks.py` | §2.2 — precision stability, §3.1 non-degeneracy, §3.3 converse exponents, envelope constant |

Dependencies: `mpmath`, `numpy`.

**Retrieval note, for anyone repeating this.** WebFetch truncates every long PDF at a fixed depth —
`2307.07491` at eq. (4.3)–(4.5), the Treilis thesis in Ch. 4, Perlmutter at §4.3, Connes 2602.04022
at §6.4 — and the summarising model will sometimes emit **fluent, entirely fabricated** content for
sections it cannot see. Two such incidents were caught this round (a fake "§4.2" of 2307.07491; a
fake INSPIRE citation list from a malformed query) and discarded. Diagnostic prompts ("what is the
highest equation number you can see?") are the reliable defence. Also: a single "not found" from these
fetches is worthless as evidence of absence — one paper returned a false negative on a sentence two
other fetches recovered verbatim.

## 12. Principal sources

Dorigoni–Treilis [2307.07491](https://arxiv.org/abs/2307.07491) (JHEP 11 (2023) 102), eq. (3.37) and
Fig. 1 · Treilis, Durham thesis [etheses 15640](https://etheses.dur.ac.uk/15640/), §5.6 and Fig. 5.2 ·
Treilis, IHES seminar 18 Oct 2023, slide 25 · **Connes–van Suijlekom**
[2511.23257](https://arxiv.org/abs/2511.23257) (Comm. Math. Phys. 406:312) · Connes
[2602.04022](https://arxiv.org/abs/2602.04022) (J. Open Math. Problems 2(1) 1–52) · Groskin
[2605.20224](https://arxiv.org/abs/2605.20224) · Connes–Consani
[2006.13771](https://arxiv.org/abs/2006.13771) · Connes–Consani–Moscovici
[2310.18423](https://arxiv.org/abs/2310.18423) · Connes [math/9811068](https://arxiv.org/abs/math/9811068) ·
Deninger [math/0505354](https://arxiv.org/abs/math/0505354),
[1807.06400](https://arxiv.org/abs/1807.06400) · Álvarez López–Kim–Morishita
[2410.20758](https://arxiv.org/abs/2410.20758) · Morishita
[2508.15971](https://arxiv.org/abs/2508.15971) · Meyer
[math/0311468](https://arxiv.org/abs/math/0311468) (Duke 127 (2005) 519) · Benjamin–Chang
[2208.02259](https://arxiv.org/abs/2208.02259) (JHEP 11 (2022) 143) · Benjamin–Chang–Fitzpatrick–Ramella
[2505.18314](https://arxiv.org/abs/2505.18314) (JHEP 09 (2025) 042) · Perlmutter
[2509.21672](https://arxiv.org/abs/2509.21672) · Gubser et al.
[1605.01061](https://arxiv.org/abs/1605.01061) (CMP 352 (2017) 1019) · Freund–Witten, Phys. Lett. B
199 (1987) 191, and [2211.01611](https://arxiv.org/abs/2211.01611) (Nucl. Phys. B 991 (2023) 116094) ·
Huang–Stoica–Yau [2001.01721](https://arxiv.org/abs/2001.01721) · Bost–Connes, Selecta Math. 1 (1995)
411 · Connes–Marcolli [math/0501424](https://arxiv.org/abs/math/0501424) · Contucci–Knauf, *The Low
Activity Phase of Some Dirichlet Series* · Hartnoll–Yang
[2502.02661](https://arxiv.org/abs/2502.02661) · Wei et al.
[2511.11199](https://arxiv.org/abs/2511.11199) (Nature Commun. 2026) · Lax–Phillips, *Scattering
Theory for Automorphic Functions*, Ann. Math. Studies 87 (1976), and Bull. AMS 2 (1980) 261 ·
Pavlov–Faddeev, Zap. Nauchn. Sem. LOMI 27 (1972) 161 · Burnol
[math/0001013](https://arxiv.org/abs/math/0001013) · Uetake, Ann. Polon. Math. 92 (2007) 99 ·
Friedman–Jorgenson–Smajlović, Ann. Inst. Fourier 70 (2020) 915 · Zworski, Bull. Math. Sci. 7 (2017) 1 ·
Hölder, Math. Ann. 28 (1886/87) 1 · Hilbert, ICM 1900 · Stadigh, Helsingfors 1902 · Ostrowski, Math.
Z. 8 (1920) 241, transl. [2211.02088](https://arxiv.org/abs/2211.02088) · Nagoshi, Bull. Austral.
Math. Soc. 93 (2016) 388 · Ovchinnikov–Pogudin–Vo, IMRN 2022 no. 16, 12342 · Rubel, Mathematika 30
(1983) 74 · Bournez–Pouly, ICALP 2017 · Matsumoto
[1407.4216](https://arxiv.org/abs/1407.4216) · Andersson
[1207.4927](https://arxiv.org/abs/1207.4927) · Conrey–Li
[math/9812166](https://arxiv.org/abs/math/9812166) · Bombieri, Sarnak, Clay RH descriptions · Conrey,
Notices AMS 50 (2003) 341 · Bellissard [1704.02644](https://arxiv.org/abs/1704.02644)
