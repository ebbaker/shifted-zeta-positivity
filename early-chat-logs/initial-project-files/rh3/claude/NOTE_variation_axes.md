# Two variation axes for the Ψ_ω / bulk dictionary: boundary topology and positivity/analyticity class

**2026-08-29.** Conversation-driven synthesis (user's question: could varying the boundary
topology, or the positivity/analyticity class, make the bulk side of a holography-like
correspondence yield something *for free* about the boundary datum?). Status: structural
observations and a queued-check list. **No new numerics this session.** Every claim below is
either (a) already verified in a cited round/note, (b) a proof-sketch-level observation flagged
as such, or (c) an explicitly open check. Filed behind the ROUND19 freeze — physics directions
resume only after human review of the two papers; nothing here touches Paper 1 or Paper 2.

**Addendum, same day.** §3 assesses an external proposal memo supplied by the user
(`Variants_of_data.md`, provenance outside this session): four of its six avenues are new
relative to §§1–2, two coincide with existing items; the queue in §4 is updated accordingly.

**Summary.** Both axes obey the same conservation law the programme keeps rediscovering:
*criticality relocates, it is never created.* The boundary-topology axis is bracketed by three
tested points in the record (torus, totally disconnected, adelic), all location-blind or worse,
while its two historical successes (function fields, Selberg zeta) share an anatomy — compact
geometry with a fixed-point/trace structure — whose archimedean absence is exactly why ROUND10
crowned Connes–van Suijlekom. The class-variation axis is *priced by a theorem* on the boundary
side (losslessness) and fails at the existence step on the bulk side (Pontryagin widening). The
one live variation found is local ↔ global: an unconditional-window + Kreĭn-extension
formulation that is the Ψ_ω-native version of the CvS truncation shape, with two open checks
before it is well-posed. Three cheap concrete checks are queued for the follow-on pipeline.

---

## 1. Axis I — varying the boundary topology

### 1.1 The mechanism, stated precisely

In AdS/CFT the "free lunch" from boundary topology has a definite shape: fix the boundary
manifold, and the bulk owes (i) existence of a regular filling and (ii) competition among the
distinct topologies that fill the same boundary. Hawking–Page is (ii) for `S¹ × S³`; the
Maloney–Witten sum over the `SL(2,ℤ)` family of fillings of a torus boundary
([0712.0155](https://arxiv.org/abs/0712.0155)) is (ii) made into a partition-function
computation; Cardy growth is modular invariance — i.e. the boundary topology — handing the bulk
a constraint for free. So the mechanism exists. The question is whether any of its outputs is
**location-sensitive** for zeros rather than count-sensitive.

### 1.2 The record already brackets this axis at three points

| boundary topology | tested in | outcome |
|---|---|---|
| torus (modular bootstrap) | Perlmutter 2509.21672, BCFR — ROUND10 §5, ROUND11 | arithmetic produced is real but **location-blind**: density bounds count zeros, and the sum rule is provably RH-insensitive (finite for any self-dual order-one L-function wherever the zeros sit) |
| totally disconnected, dim 0 (`ℙ¹(ℚ_q)`, p-adic AdS/CFT) | ROUND10 §6 | **slot-2 failure** of the five-slot screen: no complex-analytic direction anywhere in the geometry; the critical strip is exiled to the conformal weight, i.e. auxiliary field data |
| adelic assembly of all places (Freund–Witten; Gubser et al. §4.1) | ROUND10 §6 | pure **consumer** — the adelic product formula is the completed functional equation in costume; Gubser et al.'s global zeros are "visible and inert" |

Bracket: the boundary must be topologically rich enough to carry a complex-analytic direction
(the strip), yet every known "free" output of boundary topology is location-blind. The BCFR
sign-indefiniteness result (ROUND10 §5) is the standing mechanism for the blindness.

### 1.3 Two existence proofs of the mechanism — and their shared anatomy

The mechanism "topology of the geometry gives zero locations for free" has exactly two known
successes, and they are the two proved RHs:

1. **Weil's function-field RH.** Zeros become Frobenius eigenvalues; their location follows from
   a positivity statement (Castelnuovo–Severi / Hodge index) about the **intersection topology
   of `C × C`**. Topology gives location, literally.
2. **Selberg zeta of a compact hyperbolic surface.** The compact topology supplies a trace
   formula making the zeros spectral; the Selberg RH is near-trivial modulo the finitely many
   real exceptional zeros from small eigenvalues (cf. ROUND10's Manin–Marcolli entry: "the
   Selberg RH is trivial via the trace formula, so there is nothing to force").

Shared anatomy: **compact geometry + fixed-point/trace structure.** The archimedean place of
`Spec ℤ` is precisely what refuses to bound such a geometry, and this is why ROUND10 headline 2
crowned the Connes–van Suijlekom truncated Weil form as the one live architecture: it is the
only known construction where a finite-cutoff geometry yields criticality **for free** — proved
at every cutoff by a theorem that never mentions zeta — with one missing convergence statement.
The strongest form of the boundary-topology idea *is* the CvS architecture.

### 1.4 The ω-string is already a holography — an exact one, which is why nothing is free

The papers' framework is a boundary/bulk dictionary one dimension down: boundary datum = screw
function / spectral measure, bulk = Kreĭn string `m_ω`. But the map is a **bijection** (Kreĭn's
correspondence), so nothing needs to be, or can be, given for free: *admissibility of the
boundary datum is the criterion.* RH is the statement that the ω → 0 boundary datum still fills
in as a string. The bulk does undergo a Hawking–Page-shaped event at the endpoint — ROUND19's
length collapse (`L_ω = ∞` for ω > 0 vs `L_ξ = B(0) = 0.04621…` under RH, a.c. → pure point) —
but its direction matters: it is **downstream** of RH, a reformulation of the boundary
condition, not an independent bulk mechanism that could force it.

### 1.5 Queued checks (cheap, well-posed, unexplored)

1. **Conductor as the boundary-size dial.** Dirichlet ω-strings are already pipeline
   (ROUND19); add: how do string length and bulk laws vary with conductor? The margin
   computation (PROGRESS §2) showed ζ is the most marginal member of its family; the
   string-geometry face of that ordering has not been computed.
2. **The c = 1 orbifold branch.** The compact free boson is the one CFT whose L-function
   carries the (doubled) Riemann zeros, and its analytic factor's zeros stay on-line for a
   structural reason — high-frequency coefficient dominance, made physical by Cardy growth
   (NOTE_freeboson §5). Varying the *target* topology along the orbifold branch of the c = 1
   moduli space (and to the isolated points) is exactly "a variant topology of the system that
   had the property." Does the zeta-carrying structure and the on-line analytic factor
   persist? Much of the machinery in `p1_freeboson.py` / `p2b_lattice.py` transfers.
3. **Maloney–Witten location-sensitivity.** Among observables of the `SL(2,ℤ)` family of
   fillings of the torus boundary, is any location-sensitive rather than count-sensitive?
   Expected answer no, by the same BCFR sign-indefiniteness mechanism — but the record does
   not yet contain the check.

---

## 2. Axis II — varying the positivity/analyticity class

### 2.1 Boundary side: priced by losslessness; the productive direction is *weakening*

NOTE_oneside_criterion Theorem 1 + §8 is a no-free-lunch theorem for exactly this move: the
transport of exponents through the Ψ_ω dictionary is an exact isomorphism, and every formal
operation inside the family — shifting ω, integrating, smoothing by any positive kernel,
averaging in ω — **provably cannot improve an exponent**. Positivity of the smoothing kernel is
itself the enforcement (Prop. 3 there): a kernel able to cancel a violating pole would need
zeros filling the strip, and no positive measure has such a transform (Bochner). "Any gain must
inject new arithmetic."

But class variation has already paid twice **in the other currency — weaker sufficient
targets**: the pointwise → L¹ weakening (RH ⟺ Ψ⁻ ∈ L¹, the provably right topology against
Fejér-type conspiracies), and the "Weil positivity with exponential defect" problem P2,
formally weaker than anything the positivity programme aims at, any solution to which buys the
first zero-free half-plane.

The *upward* direction — requiring the boundary datum to inhabit a class strictly stronger than
the RH-equivalent one — has a decisive historical failure: de Branges' positivity conditions,
shown by Conrey–Li ([math/9812166](https://arxiv.org/abs/math/9812166), IMRN 2000) to fail for
ζ. The conductor result (PROGRESS §2: ζ is the most marginal member) is the programme's own
quantitative face of the same fact: ζ inhabits exactly the critical class and nothing stronger.

### 2.2 Bulk side: the class ladder, and the Pontryagin existence failure (new observation)

The natural ladder of bulk realizations:

| boundary class | bulk realization |
|---|---|
| Stieltjes | Kreĭn strings (current bulk; bijective) |
| Nevanlinna/Herglotz | canonical systems (de Branges; also Eckhardt–Kostenko indefinite strings) |
| generalized Nevanlinna `N_κ` | Pontryagin-space realizations, κ negative squares (Kreĭn–Langer) |

The hope the widening suggests: make the bulk *always* exist, then compute its index by
bulk-side means — indefinite spectral theory does have index machinery (oscillation counts,
negative-mass counts) that never mentions zeta. Violating zero-quartets are what contribute
non-real poles / negative squares to `q_ω`, so RH becomes "the ω → 0 bulk has index zero."

**The instructive failure (proof-sketch level, flagged):** the widened bulk does **not** always
exist. A `Π_κ` realization requires κ finite — i.e. *finitely many* zeros with
`Re ρ > ½ + ω` — and no known result delivers this for any ω ∈ (0, ½): density bounds give
count upper bounds growing in `T`, never a finite total; the actual count is 0 under RH and
unbounded in the alternative nobody can exclude. So **bulk existence in the indefinite class is
itself an unproven zero-distribution statement of Siegel-finiteness type.** The widening
converts "where are the zeros" into "does the bulk exist" — the same one-way information flow
as ROUND10's boundary-data reframing (translation goes both ways; information does not). And
even granting existence, the index is computed *from* the boundary datum; without an
independent bulk-side characterisation (slots 4–5 of the five-slot screen) the reformulation is
a relabelling. Cautionary specimen already on the wall: the refuted Lax–Phillips contraction
argument (ROUND10 §3) — a definite → contraction class trade of the same family.

### 2.3 The live variation: local ↔ global (the window-extension problem)

One class variation does hand over something unconditional, and it is the local↔global axis
rather than definite↔indefinite. Ingredients, all in hand:

- **Unconditional windows.** Ψ_ω ≥ 0 on `[0, t₊(ω)]` with `t₊` explicit and the endpoint law
  `t₊ ≈ 0.72(½−ω)⁻²` (PROGRESS §1; Paper 1 Prop. window).
- **Local inverse theory.** The boundary datum on `[0, T]` determines the string on a
  corresponding initial segment (Kreĭn–de Branges locality; the Gelfand–Levitan item already in
  the ROUND19 pipeline computes it).
- **Free continuation.** A finite string segment continues to a full string trivially — keep
  laying down positive mass — and every bulk continuation induces a screw continuation of the
  boundary datum.

So the bulk gives, for free: *every unconditional window is fillable, and every filling
continues.* RH is then the statement that **the arithmetic continuation of the boundary datum
is one of the screw continuations** — all criterion content compressed into the germ at
`t = ∞`, which is the margin paper's own verdict ("the criterion's open content lives entirely
in the tail") reached from the bulk side. Structural identity worth recording: this is the
**same move as Connes–van Suijlekom with the truncation taken in time `t` instead of in primes
`p ≤ x`** — positivity for free at every finite cutoff, one missing extension/convergence
statement. It is the Ψ_ω-native instance of the CvS shape, and it plugs into the frozen papers'
machinery (GL inversion, the window tables) rather than requiring a new architecture.

**The concrete question it opens.** Kreĭn's extension theory *parametrizes* the set of
continuations from a window. Ask, numerically first: as `T` grows, how does the arithmetic
continuation sit inside the parametrized extension set — interior point, boundary point,
extreme point? A uniform structural answer (e.g. extremality) would be a new kind of statement
about the boundary datum obtained from bulk-side structure.

### 2.4 Two open checks before §2.3 is well-posed

1. **Pointwise vs kernel-PSD on windows.** The window theorem controls *pointwise* positivity;
   the extension theory needs the screw **kernel** PSD on `[0,T]²` — strictly stronger locally
   (globally they coincide: Suzuki Thm 1.7 vs Thm 1.1). Define
   `T_psd(ω) := sup{T : screw kernel of Ψ_ω is PSD on [0,T]²}`; RH ⟺ `T_psd = ∞` at the
   critical member. Open: unconditional lower bounds on `T_psd(ω)`, and whether it tracks
   `t₊(ω)`. A finite-section computation (Gram matrices on growing windows) probes this
   immediately; the CvS finite-cutoff positivity is the prime-side hint that windowed PSD may
   hold at substantial `T` unconditionally.
2. **Source pull: screw-function extension from an interval.** For positive-definite functions
   on `(−a, a)`, extension to ℝ is Kreĭn's classical theorem (1940). The screw/helical analogue
   on `[0, T]` — existence of extensions, and the parametrization — is Kreĭn–Langer territory
   (helical-function continuation; also their 1985 screw-function papers), but the exact
   statement has **not been pulled and verified this session**. The trivial-continuation
   argument via the string segment (§2.3) sketches existence; the parametrization needs the
   literature before anything is asserted.

### 2.5 Verdict: the two currencies

Varying the positivity/analyticity class **cannot** manufacture location information — the
losslessness theorem closes the boundary side, and the Pontryagin existence failure plus the
one-way-flow law close the bulk side. It **can** buy: (i) weaker sufficient targets (L¹, defect
positivity), and (ii) unconditional finite regimes with the RH content isolated in a single
extension/convergence statement (windows in `t`; CvS in `p ≤ x`). Currency (ii) is where the
window-extension problem of §2.3 lives, and it is the first physics-adjacent direction found
that runs inside the existing framework.

---

## 3. External proposal set (2026-08-29), assessed

Six avenues in the memo. Items 5 (universality control across self-dual `L`) and 6 (ω-flow
index) are already covered: item 5 is substantially PROGRESS §2 + the ROUND19 pipeline entry
(adopt its sharper organizing split — UV ↔ gamma factor, IR ↔ `F′/F(½+ω)` — into the conductor
check, §1.5(1)); item 6 is the same crossing `ω = β−½` as §2.2's Pontryagin index, and the
memo's own skepticism ("repackaging of zero counting") matches §2.2's relabelling verdict —
revisit only inside the graph laboratory below, where spectral flow meets genuine topology, as
the memo itself concludes. Its self-correction (Cayley transforms add no topology; the spectral
`u`-line is not a spatial conformal boundary) agrees with §1.4. The four new avenues:

### 3.1 Riccati radial response and the literal bulk action (new; low cost)

**Proposal.** With `dm_ω = r_ω dx`, the string equation `y'' + z r_ω y = 0` gives, for the
cutoff response `R(x,z) = y'/y`, the radial Riccati flow `∂_x R = −R² − z r_ω(x)` — the same
equation that evolves holographic two-point functions radially (holographic Wilsonian RG:
Heemskerk–Polchinski [1010.1264](https://arxiv.org/abs/1010.1264), Faulkner–Liu–Rangamani
[1010.4036](https://arxiv.org/abs/1010.4036); radial Hamilton–Jacobi, Papadimitriou–Skenderis).
Identify `q_ω` = boundary value of `R`; ask whether the string derives from an explicit
quadratic 1+1d bulk action.

**Assessment.** The action question answers itself: a Kreĭn string *is*, by origin, the
inhomogeneous vibrating string, `S = ½∫dt [∫(∂_t u)² dm_ω(x) − ∫(∂_x u)² dx]` — local,
quadratic, position-dependent kinetic coupling. So the literalization is bookkeeping, and the
avenue's genuine content is two things the memo doesn't state. (i) **A radial monotone.**
Holographic c-theorems descend from bulk energy conditions; the string-side analogue of an
energy condition is positivity of `dm_ω` — i.e. the criterion itself sits exactly where the
energy condition sits ("RH as the energy condition of the ω-bulk" — slogan-level, flagged; the
precise question is whether some functional of `R(x,z)` is unconditionally monotone along the
flow with the criterion as its endpoint statement). (ii) **A caveat:** `dm_ω` is not absolutely
continuous — ROUND19's bulk has embedded atoms — so the smooth `r_ω(x)` presentation fails and
the flow must be run in measure/transfer-matrix (impedance) form. Standard, but it means the
"radial ODE" picture is the generic-point description only. Verdict: cheap dictionary upgrade
plus one real question (the monotone); physics-side, behind the freeze.

### 3.2 Metric-graph / matrix-Weyl laboratory (new; the continuum topology experiment)

**Proposal.** Replace the half-line by a network of ω-strings with several boundary vertices;
the scalar `q_ω` becomes a matrix Weyl / Dirichlet-to-Neumann function `M_ω(z)`; compare trees,
single loops, theta graphs at matched local edge data and ask which boundary observables detect
`b₁`.

**Assessment.** Sound, and the right continuum version of the §1 question — it converts "which
free outputs of topology are location-sensitive" into a decidable inverse-problem setting with
a rigorous base (boundary control recovers metric trees, Belishev; cycles are invisible to the
`M`-function alone and become visible through magnetic-flux dependence, Kurasov — so the
literature already knows *exactly which* boundary data see `b₁`). By the conservation law it
injects no arithmetic; its value is discovering the invariant to hunt in the Selberg case.
Sequence it after the finite laboratory of §3.4, which is the same experiment with everything
exact.

### 3.3 Selberg ω-strings (new as a construction; deepest; one obstruction the memo misses)

**Proposal.** Build `q_{ω,X}` from `Z_X′/Z_X(½+ω+w)/w` for a hyperbolic surface `X` and
decompose it as spectral + topological, the second part carrying `χ(X), g, n_cusp`.

**Obstruction (gating, not in the memo).** `Z_X` has order 2: the Weyl law
`N(r ≤ T) ~ (Area/4π)T²` makes `Σ r_n⁻²` diverge, so the screw/Hadamard normalization behind
Ψ_ω fails as-is — `B(0) = ∞`, and the Kotani-length statement degenerates. An adapted
normalization (one further subtraction/integration — precisely §2.1's licence to weaken the
class, or second-order screw theory) must be built first. Concrete, probably surmountable,
and it is the first work item of this avenue.

**Payoffs (three, underestimated by the memo).** (i) The spectral/topological decomposition is
essentially automatic: topology enters through the trivial zeros — multiplicity `−χ(2k+1)` at
`s = −k` — i.e. through the completed gamma-factor block; and by Kasahara the string's UV law
is gamma-factor-controlled, giving a candidate theorem: **the reconstructed bulk's UV
coefficient is proportional to χ(X)** — exactly the "topological invariant readable in the
bulk" phenomenon §1 was looking for. (ii) Selberg RH is a theorem (trace formula /
self-adjointness), so admissibility at ω = 0 is *guaranteed* and the construction
reverse-engineers the solved case: what does the bulk of a system where Hilbert–Pólya holds
look like, compared against ζ's? (iii) The framework's Siegel-blindness lands exactly on the
small eigenvalues `λ ∈ (0, ¼)` — real zeros in `(½,1)`, invisible to the criterion by
Prop. 9.5, and *realized* here by actual surfaces (the Fejér/shielding extremals of
NOTE_oneside §5 become geometric objects). Moreover their number is topologically bounded: at
most `2g−2` eigenvalues of a closed genus-`g` surface lie below ¼ (Otal–Rosas, `λ_{2g−2} > ¼`;
**source-pull flag**). So **the criterion's blind spot has cardinality bounded by a topological
invariant** — a precise, provable instance of "boundary topology ⟹ statement about the
criterion." Verdict: the eventual target, as the memo says; order-2 normalization first.

### 3.4 Ihara finite laboratory (new; best cost/insight ratio — queue it first)

**Proposal.** For finite graphs, Bass's determinant formula
`ζ_X(u)⁻¹ = (1−u²)^{−χ(X)} det(I − Au + Qu²)` puts the Euler characteristic explicitly in the
zeta; the RH-analogue is exactly the Ramanujan property. Define the ω-broadened spectral data,
build the Herglotz response, and explore exhaustively.

**Assessment.** Everything in the chain Ψ_ω → q_ω → σ_ω → m_ω becomes **finite and exact**: a
rational Herglotz function corresponds to a finite beaded string via the Stieltjes continued
fraction, so each graph yields an explicit finite bulk. Extra framing the memo omits:
Ramanujan ⟺ the nontrivial spectrum stays inside the spectrum of the universal covering tree —
the RH-analogue is *literally* a quotient-vs-universal-cover statement, so the laboratory
natively contains a bulk/boundary-topology comparison and reconnects to §1.2's p-adic row from
the working side (the Bruhat–Tits tree as bulk succeeds here because everything is spectral
and finite). First experiment: matched-degree families with `b₁ = 0, 1, 2`; compute the finite
ω-strings; classify bead statistics into local vs `χ`-sensitive; then perturb a Ramanujan
graph past the bound and watch how the violating eigenvalue manifests in the bulk — the finite
analogue of a violating zero's bulk signature. The §2.2 / memo-item-6 index question is
*decidable* here: spectral flow at ω-crossings is finite-dimensional and exactly computable.
Pure finite spectral graph theory + numerics — arguably not even behind the physics freeze.

### 3.5 Priority within the proposal set

Ihara laboratory (§3.4) → Riccati/action write-out with the monotone question (§3.1) → Selberg
order-2 normalization, then Selberg ω-strings (§3.3) → metric-graph `M`-function laboratory
(§3.2), informed by what the Ihara lab says is worth measuring. The memo's own two-track plan
(Riccati ∥ graph lab) is sound; the reordering above just puts the exact finite version before
the continuum one.

---

## 4. Relation to the frozen plan

Nothing here changes the ROUND19 ordering (human review of Papers 1–2 first). Queue additions
for the follow-on pipeline, in rough order of cost:

| item | cost | section |
|---|---|---|
| Ihara/Ramanujan finite laboratory (`b₁ = 0,1,2` families, finite ω-strings) | low (finite numerics) | §3.4 |
| finite-section probe of `T_psd(ω)` vs `t₊(ω)` | low (numerics, existing machinery) | §2.4(1) |
| Riccati/action write-out + radial-monotone question | low (bookkeeping + one question) | §3.1 |
| c = 1 orbifold-branch check | low–medium (extends `p1/p2b` scripts) | §1.5(2) |
| Kreĭn–Langer screw-extension source pull | low (literature) | §2.4(2) |
| Selberg order-2 normalization (gating item for §3.3) | medium (analysis) | §3.3 |
| conductor dependence of string geometry | medium (extends Dirichlet ω-strings item) | §1.5(1) |
| metric-graph `M_ω` laboratory | medium (after Ihara lab) | §3.2 |
| arithmetic continuation vs extension set (GL-based) | medium–high | §2.3 |
| Selberg ω-strings: bulk UV ∝ χ; blind spot ≤ 2g−2; Hilbert–Pólya reverse-engineering | high (after gating item) | §3.3 |
| Maloney–Witten location-sensitivity sweep | medium (literature + argument) | §1.5(3) |
| Pontryagin index note (negative result, worth recording) | low (write-up of §2.2) | §2.2 |

## 5. Sources

Internal: `ROUND10_boundary_data.md` (five-slot screen; boundary-data reframing; torus/p-adic/
adelic verdicts; CvS headline; Lax–Phillips refutation) · `ROUND19_endpoint_length_and_freeze.md`
(length collapse; freeze; pipeline) · `NOTE_oneside_criterion.md` (losslessness Thm 1; L¹ Thm 2;
smoothing Prop 3; problem P2) · `PROGRESS_psi_omega_next_steps.md` (windows, endpoint law,
conductor marginality) · `NOTE_freeboson_Lfunction.md` (c = 1 zero set; dominance criterion) ·
`PAPER_psi_omega_margin.tex` (tail verdict; integrated criterion).

External (cited, not re-verified this session): Maloney–Witten
[0712.0155](https://arxiv.org/abs/0712.0155) · Conrey–Li
[math/9812166](https://arxiv.org/abs/math/9812166) (IMRN 2000) · Kreĭn 1940 (pd-function
extension); Kreĭn–Langer `N_κ` realization theory and helical-function continuation
(**exact statements pending the §2.4(2) source pull**) · Eckhardt–Kostenko, indefinite strings
(Invent. Math. 204 (2016)) · Weil, function-field RH via Castelnuovo–Severi · Selberg trace
formula (compact case) · standard Hawking–Page / Cardy statements.

For §3 (all cited from memory this session, **none re-verified — source pulls due with the
respective work items**): Heemskerk–Polchinski [1010.1264](https://arxiv.org/abs/1010.1264) ·
Faulkner–Liu–Rangamani [1010.4036](https://arxiv.org/abs/1010.4036) · Papadimitriou–Skenderis
(radial Hamilton–Jacobi holographic renormalization) · Belishev (boundary control on metric
trees); Kurasov (graph `M`-functions; magnetic boundary control for cycles) · Bass determinant
formula (Bass 1992; expositions: Kotani–Sunada, Stark–Terras) · Ramanujan ⟺ universal-cover
spectrum (Grigorchuk–Żuk; LPS for existence) · Selberg zeta order/divisor and trivial-zero
multiplicities `−χ(2k+1)` (Sarnak, *Determinants of Laplacians*; D'Hoker–Phong) · Otal–Rosas,
`λ_{2g−2} > ¼` for closed hyperbolic genus `g` · external memo `Variants_of_data.md`
(user-supplied, 2026-08-29).
