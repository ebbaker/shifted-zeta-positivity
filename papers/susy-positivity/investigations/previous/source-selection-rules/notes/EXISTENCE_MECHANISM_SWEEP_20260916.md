# A broad sweep of existence mechanisms, and the one that manufactures positivity

**Author: Claude Opus 5 (Anthropic).** 16 September 2026. A deliberately wide
survey, run to make sure no existence route is being overlooked before any one of
them is pursued. Continues
[the fixed-point note](FIXED_POINTS_AND_THE_MARGIN_20260916.md).

**Provenance warning, which matters for how to read this.** Sections 2 to 8 rest
on a literature sweep carried out by five subagents. I have **not** read most of
the cited papers myself; theorem statements are as reported to me, and a few
carry explicit reliability flags (§7). Everything I have verified personally is
marked. Treat the citations as leads to check, not as established.

---

## 0. The headline, in three sentences

Across the whole survey, **every existence theorem in this subject transports
positivity rather than creating it**: de Branges' inverse spectral theorem,
Krein-Langer continuation, Osterwalder-Schrader reconstruction and RG
constructions all take positivity in and give positive structure out. The one
mechanism in mathematics that *manufactures* positivity from an operator is
**Ruelle-Perron-Frobenius / Birkhoff cone contraction**, where the positive
object is the leading eigenvector of a positive map and exists because the map
contracts the Hilbert projective metric. That mechanism appears nowhere in the
Weil-positivity literature, and our `||Pi_L|| <= 1` formulation is the first
thing in this programme shaped to receive it.

---

## 1. The taxonomy

Two axes. **What existence principle** is invoked, against **what is
characterised self-consistently** (since a fixed point needs something to find).

| Principle | Manufactures positivity? | Needs | Status here |
|---|---|---|---|
| Banach contraction | no | complete metric, strict contraction | open; obstructed by the collapsing margin (§7) |
| Schauder / Ky Fan / Kakutani | no | compact convex set, continuous self-map | set now exists (classified trace cones); no candidate map |
| Markov-Kakutani / Ryll-Nardzewski | no | commuting affine maps on compact convex | the classical route to invariant means and traces; untried here |
| Knaster-Tarski | no | complete lattice | blocked on operator intervals (Kadison); **open on de Branges chains** (§4) |
| Krein-Rutman / **Ruelle-Perron-Frobenius** | **YES** | positive map of a cone, finite projective diameter | **unoccupied; the one real opening** (§2) |
| Topological degree / index | no, but sidesteps | deformation invariance | Bombieri's Theorem 8 (§5) |
| Variational compactness | no | weak compactness, lower semicontinuity | Bombieri's Theorems 3-4: the published precedent |
| Inverse spectral (de Branges, Krein) | no — transports | input certified Nevanlinna / Hermite-Biehler | §3; the certification is RH-equivalent |
| Krein-Langer continuation | no — transports | a screw function on a finite interval | §3; **equals Remark 3.3, already known vacuous** |
| Separation / duality | n/a | — | the tool actually matched to a membership question |

| What could be characterised self-consistently | Verdict |
|---|---|
| The source `Phi` | nothing to find: unique up to unitary (Cor 2.2) |
| The contraction `Pi_L` | nothing to find: given by a formula |
| A twisted trace | **linear** conditions; separation fits, not fixed points |
| A spherical vector in a `q`-difference system | **genuinely self-consistent** (§6) |
| An RG-invariant state | invariant, not a fixed point; and the primes fix an absolute scale |
| A transfer-operator eigenvector | genuinely self-consistent — but attached to the *wrong* zeta (§2) |
| The zero measure via the explicit formula | self-dual by construction; no information |
| Nyman-Beurling: distance to a subspace | both target and subspace explicit; not self-consistent |

---

## 2. The one mechanism that manufactures positivity

Birkhoff's theorem: a linear map taking a cone into itself with **finite
projective diameter** `Delta` contracts the Hilbert projective metric with ratio
`tanh(Delta/4) < 1`, so by Banach it has a unique positive leading eigenvector.
This is how Ruelle-Perron-Frobenius produces the Gibbs state, and it is the only
place I have found where a positive object is an *output* rather than an input.

**Nothing like it exists in this subject.** Three independent searches returned no
application of Krein-Rutman, cone spectral radius, or the Hilbert projective
metric to Weil positivity, the explicit formula, or any RH-equivalent criterion.
The Hilbert-metric literature touches zeta only through **Ruelle** zeta functions
of hyperbolic dynamics (Liverani's Birkhoff-cone transfer operators), and the
transfer-operator route to *Riemann* zeros is likewise absent: Mayer's operator
and Lewis-Zagier period functions give a genuine eigenvalue-one self-consistency,
but for the **Selberg** zeta and the Maass spectrum; the Riemann zeros enter the
modular surface only through the scattering determinant `xi(2s-1)/xi(2s)`, as an
explicitly known factor that the cone machinery does not single out. The
Gauss-Kuzmin-Wirsing operator has a genuine Perron-Frobenius fixed point (the
Gauss measure) and zeta appears only in its matrix entries.

**What it would take here, stated precisely.** Our formulation is already the
right shape: `Q_L = K_+ - T_L` with `T_L <= K_+` equivalent to
`||Pi_L|| <= 1`, i.e. a **spectral radius bound for a positive map**. To use the
mechanism one needs a model supplying a positive map `mathcal L` of a cone with
`Q_L[f] = <v, (1 - mathcal L) v>`; then Weil positivity is
`spec-rad(mathcal L) <= 1`, and Birkhoff supplies the critical eigenvector.

**And it comes with a quantitative prediction that can be tested now.** Birkhoff
says the contraction ratio is `tanh(Delta/4)`, which tends to 1 exactly as the
projective diameter `Delta` of the image diverges — that is, as the image touches
the boundary of the cone. Our margin collapses (§7). So:

> **Testable.** Compute the projective diameter of `Pi_L`'s image in the natural
> cone and check whether `tanh(Delta_L/4)` tracks `1 - lambda_min(L)`. If it
> does, the Birkhoff picture and the Landau-Widom picture of §7 are two
> descriptions of one phenomenon, and the cone framing has earned its place.

For complex/indefinite forms the tool is Rugh's complex-cone theory
(*Cones and gauges in complex spaces*, Ann. Math. 171 (2010) 1707-1752).

**Caveat I want on record.** Krein-Rutman produces the eigenvector *given* the
operator; it does not decide the value of the spectral radius. So this mechanism
does not by itself prove `||Pi_L|| <= 1`. Its value is that it is the only route
in which positivity is produced rather than assumed, and that it predicts the
observed criticality. That is worth something and it is not a proof strategy yet.

---

## 3. Everything else transports positivity

- **de Branges' inverse spectral theorem.** For every Nevanlinna function there
  is an essentially unique Hamiltonian with that Weyl coefficient; with trace
  normalization the correspondence is a bijection. Genuinely non-constructive
  (the proof runs through the ordering theorem, producing no formula), and
  positivity `H(t) >= 0` is automatic. **But the input must already be certified
  Nevanlinna, and for zeta that certification is RH-equivalent.** De Branges' own
  positivity route is dead as stated: Conrey-Li exhibit the 34th zero violating
  the required condition by `-5.4e-69`. Lagarias has only the converse:
  RH implies the structure function.
- **Krein-Langer screw-function continuation.** Every screw function on a finite
  interval extends to all of `R`, so a local positive-definite kernel yields a
  global nonnegative spectral measure, non-constructively and **non-uniquely**.
  The Weil kernel is exactly of this form. This looked like the most promising
  item in the sweep — and it is **the manuscript's own Remark 3.3**, where Krein's
  extension theorem is already noted to supply stationary positive data on each
  scale while "only its compatibility as `L` grows carries arithmetic
  information". The general theorem has a name; the conclusion is unchanged. The
  non-uniqueness is the whole problem: continuation gives *an* extension, not the
  zeta one.
- **Osterwalder-Schrader and RG.** Reflection positivity is preserved by
  reflection-symmetric block-spin maps and therefore propagates to a fixed point,
  but it is always an input. No theorem was found obtaining reflection positivity
  *as* a fixed point of an RG map.

---

## 4. The order-theoretic opening that Kadison does not block

The fixed-point note blocked Knaster-Tarski at the operator level: by Kadison's
antilattice theorem the self-adjoint part of a C*-algebra is an anti-lattice, so
`[0, K_+]` is not a lattice. That argument does **not** reach the object the
subject actually orders.

The **de Branges ordering theorem** says the de Branges subspaces of a given
space form a **totally ordered chain** — and Suzuki, *On the Hilbert space derived
from the Weil distribution* (arXiv:2301.00421), reportedly proves that the
Hilbert space `H_W` of the Weil distribution **is** a de Branges space, produces a
totally ordered family of subspaces indexed by `t >= 0`, and converts the RH
criterion from inequalities into **equalities**. That is the only genuinely
order-theoretic structure the sweep found in this subject, and it is a chain,
which is what order-theoretic fixed point arguments need.

Worth checking directly, because if the ordered family is complete in the
lattice sense then monotone methods are live on it.

---

## 5. The index opening

Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers,
I* (Rend. Lincei 11 (2000) 183-233), Theorem 8: **the number of negative
eigenvalues of `H(Gamma;t)` equals the number of distinct complex conjugate pairs
in `Gamma`** — i.e. the count of zeros off the line — proved by continuous
deformation of the zero set with symmetries preserved. That is a
deformation-invariant index, the only topological argument in the subject.

It suggests a route that is not a positivity proof at all: **compute a signature
or index that is invariant under deformation and show it vanishes.** Indices are
integers, so an index argument is immune to the collapsing margin of §7, which is
its main attraction. Bombieri's Theorems 3 and 4 (attainment of the infimum by
weak compactness) are separately the published precedent for a non-constructive
object-producing step in this subject.

---

## 6. The physics-side opening

Gaiotto-Teschner (arXiv:2406.09171) reportedly state a **one-to-one
correspondence between positive traces on the algebras `A_q` and unitary
representations of `D_q` containing a spherical vector**, the spherical vector
being cut out by the difference-operator system `W_a |1> = W~_a |1>`.

That is the strongest existence handle found anywhere in this literature, because
it converts existence of the positive pairing into **existence of a normalizable
solution of a `q`-difference system** — a genuinely self-consistent object, and
exactly the kind of thing contraction and continuation arguments produce. It also
connects to material already in the sibling manuscript: Section 5.2 works with
the spherical vector's difference equation (5.9), `phi_0(q^2 v)/phi_0(v)`, and
treats it as an obstacle rather than as an existence handle.

Everything else on the physics side settles existence by writing the answer down.
EKRS prove existence by explicit integral formulas plus a pointwise sign
condition (Prop. 4.4) and an explicitly parametrised semialgebraic cone
(Thm. 4.6) — **not**, as I had guessed, by the discrete-Painleve recurrences,
which are downstream of an already-constructed trace. Klyuev-Vulakh
(arXiv:2507.19447, SIGMA 22 (2026) 033) is **not** a numerical bootstrap: traces
form a finite-dimensional vector space and the positive ones a convex cone of
real dimension `m/2 - 1`, with a *unique* positive trace for `m = 4`. Gaiotto-
Teschner's positivity itself is their Conjecture (1.3), verified in examples.
Ambrosino-Gaiotto's RG spectrum generator satisfies intertwining/cocycle
conditions — the Schur pairing is **equivariant under** the flow, not a fixed
point **of** it, confirming the exclusion in the fixed-point note from a second
direction.

Only one proved existence of a positive solution to a self-consistency condition
turned up anywhere: Guillarmou-Kupiainen-Rhodes-Vargas on the Liouville bootstrap
— and there positivity comes from a probabilistic construction, not a fixed point.

---

## 7. External corroboration, and a correction to my own numbers

Zhu, *Weil positivity in compact windows* (arXiv:2608.24827), independently finds
the same collapse and gives it a name.

**What is solid there:** Theorem 1.1, a reduction that drops the symbol's tail
past a threshold using the total prime-comb mass `A_L = sum_{log n < 2L} 2 Lambda(n)/sqrt n`
as an envelope, leaving a finite Legendre block with errors below `1e-100`. And
`A_L ~ 4 e^L` by the prime number theorem.

**The upper bounds, which bear on my §5 table.** Certified unconditionally in
interval arithmetic from the geometric side alone, with sine-basis trial
functions: `lambda*(0.8) <= 2.27e-17`, `lambda*(2.0) <= 3.19e-283`.

**So my own measurement is a very weak upper bound.** Zhu normalizes against
`||f||_2^2` while I normalize against `K_+`, so the two are not the same quantity
and no direct comparison is available. But his trial functions are far better
adapted than my polynomial basis, and the gap at `L = 2` is of order `10^266`.
**My §5 table stands as correct upper bounds and should not be read as measuring
the true margin.** The qualitative conclusion — that the margin collapses and that
no method may assume a uniform-in-`L` one — is if anything strengthened.

**The decay law.** `-ln lambda*(L) ~ 2 pi^2 N(T*)/ln N(T*)` with `T* = 2 pi e^{2L}`.
The constant is **fitted, not derived**, on four points `L = 1.4 ... 2.0`, and
the paper says so; at `L = 0.8` the law is off by seven orders of magnitude. The
`2 pi^2` is meant to echo the Landau-Widom plunge rate for time-band-limiting
operators (`pi^2` of log-decay per mode beyond the Shannon number, divided by
`ln c`), doubled for the `±gamma` count.

**The barrier is narrower than its abstract.** Theorem 1.4 bounds the cost of
**Theorem 1.1's own envelope method** — `T# > 2 pi e^{A_L}` with `A_L ~ 4 e^L`,
hence doubly exponential. The paper's own Remark 1.5 concedes that converting
this into a lower bound on the cost of an *arbitrary* certificate is open. So
"the positivity route cannot reach RH unassisted" is the author's gloss, not a
theorem. Its Remark 1.6 names the escape: one must show the phases `(t log p)_p`
cannot align — a simultaneous-Diophantine statement about `{log p}`.

**Reliability.** Preprint only, unrefereed. v1 was posted under a different author
name with the same headline constant. The certified bounds are one author's
`mpmath` error accounting, not Arb or a proof assistant, and a replication attempt
is apparently in progress with unknown outcome. Read the reduction idea, which is
good and independent of provenance; do not lean on the constants.

---

## 8. What the sibling investigation appears to be missing

Manuscript 0.5 cites Suzuki, *Weil's quadratic form via the screw function*
(arXiv:2606.09096) **only for the normalization of the Weil functional** in
Section 2.1 — I have checked `references.tex` and the citation myself. According
to the sweep that paper also proves, unconditionally: that the localized Weil
form is `<A_a v, v>` for a self-adjoint `A_a` built from a screw function; that
the least Rayleigh quotient `lambda_a` is continuous in `a`; that the lowest
eigenvalue is **positive and simple**; and self-adjoint extension results — with a
conjecture that the eigenfunction transforms converge to `xi`. A companion
numerical paper (arXiv:2607.24830) reports `lambda_1(a)` strictly positive and
superexponentially decaying, smooth through the first prime threshold, with an
archimedean law `lambda_k(a) = log(1/a) + log(k - 1/2) + B_0 + O(a)` to 30 digits.

If those hold as reported they bear directly on Section 7.6 and on selection
rule 7, and the investigation should be building on them rather than citing the
paper for a normalization. **Reading that paper properly is the first thing to
do.**

---

## 9. Ranked next steps

1. **Read Suzuki arXiv:2606.09096 and arXiv:2607.24830 in full** (§8). Cheapest,
   most likely to change what we do, and the manuscript already cites the first.
2. **Test the Birkhoff prediction** (§2): compute the projective diameter of
   `Pi_L`'s image and check `tanh(Delta_L/4)` against `1 - lambda_min(L)`. This is
   a computation we can do with what is already built, and it decides whether the
   cone framing is more than vocabulary.
3. **Port the margin computation** and adopt Zhu's sine-basis trial functions
   (§7); our polynomial basis is off by hundreds of orders of magnitude.
4. **Check Suzuki arXiv:2301.00421's ordered family of de Branges subspaces**
   (§4) for lattice completeness. If it is complete, monotone fixed-point methods
   are live where Kadison blocked them.
5. **Follow the spherical-vector correspondence** (§6): does existence of the
   source reduce to normalizability of a solution of the `q`-difference system?
6. **Look at Bombieri's index argument** (§5) as a route immune to the margin.
7. **Not** Nyman-Beurling as a fixed-point problem: both target and subspace are
   explicit, and no link between `d_N` and the localized form's least eigenvalue
   is known.

## 10. Status

- §1's taxonomy and the screening judgements are **mine**, and are assessment.
- §2's Birkhoff prediction is **mine** and untested.
- The claim that the cone/Hilbert-metric reading is absent from the literature
  rests on three independent negative searches; negative search results are weak
  evidence and should be treated as such.
- §3, §4, §5, §6 and §8 report theorem statements **I have not verified**. The one
  thing I checked personally is that manuscript 0.5 cites Suzuki only for the
  normalization.
- §7's account of Zhu is second-hand from a careful reading by a subagent,
  including its own reliability flags. Nothing there should be relied on until
  the paper is read directly.
- §3's identification of Krein-Langer continuation with Remark 3.3 is **mine**,
  and I am confident in it.
