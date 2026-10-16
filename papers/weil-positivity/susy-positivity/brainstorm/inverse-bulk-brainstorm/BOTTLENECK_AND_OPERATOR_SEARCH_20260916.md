# Where the bottleneck actually is, and what an operator search inside a fixed theory would have to do

**Author: Claude Opus 5 (Anthropic).** 16 September 2026. Brainstorm note for
Edward Baker, written in response to five proposed directions (fixed-theory
operator search, Wilson lines rather than loops, an `L`-family of operators,
non-constructive existence, perturbation theory, and the OPE).

This is a brainstorm note, not a results note. Section 2 contains one new
numerical observation, computed independently of the investigation's own check
programmes; it is labelled as numerical and is not a theorem. Everything else
is either a restatement of results already in working manuscript 0.5 (with
references) or an assessment.

Manuscript references are to
[`investigations/previous/inverse-bulk-realization/manuscript.tex`](../../investigations/previous/inverse-bulk-realization/manuscript.tex),
version 0.5.

---

## 1. The bottleneck, in five layers

It is worth separating these, because they are usually collapsed into "the
matching is hard", and they are not equally hard, and the hard one is not the
one the calculations have been aimed at.

### Layer 0 — the object to be built is unique, so there is nothing to tune

Corollary 2.2: if `Phi` is defined on `C_c^inf(R)` and `||Phi(f)||^2 = Q_L[f]`
whenever `supp f` is in `I_L`, then RH holds **and** `Phi(f) -> (F^(gamma_rho))_rho`
extends to a unitary onto the closed span of those vectors in `l^2` of the zero
multiset. The Hilbert space and the source are not free data.

The consequence people underrate: **there is no approximate version of the
target to aim at.** A candidate is not "close" or "far"; it is that map up to
unitary, or it is not a realization. This is why no inequality about `Q_L` — the
prime-free inequality (8.1) included — can decide whether a family of physically
motivated pairings contains a source. The programme is a membership question
about a family, not an estimation problem.

### Layer 1 — one interval is free; all the content is uniformity in `L`

Section 3.1: as soon as `Q_L >= 0`, the map `Phi(f) = Q_L^{1/2} f` into
`L^2(I_L)` already satisfies Definition 3.1 on that interval. Remark 3.3 is
worse: via Krein's extension theorem, positivity on one interval already yields
translation-covariant stationary positive data on that scale. So a realization
at a fixed `L`, even a translation-covariant one, carries **zero** information.

Also worth being explicit, because it bears on idea (C) below: `Q_L` is not a
family of different functionals. It is the single Weil functional `W` restricted
to functions supported in `I_L`. The `L`-dependence is a support condition on
the input, nothing else — there are no boundary conditions on the test
functions (Section 2.1: `f` in `C_c^inf(I_L)`, `F = E_L f`, and the natural
closed domain `D_{gamma,L}` of (2.11) is *supported in the closure of* `I_L`,
with no trace condition, which is forced anyway because the energy is only
logarithmically stronger than `L^2` and therefore has no trace operator at all).

### Layer 2 — the architecture is forced: a compression, not a sum of channels

Theorem 7.5: there are no complex-linear `G, S` into a common positive Hilbert
space with `||Gf||^2 = A_L`, `||Sf||^2 = B_L` and `||(G±S)f||^2 = Q_L`, at
`L = 1`, `L = 5/4`, and every sufficiently large `L`. The proof is the
elementary bound `||(G+S)f||^2 >= (||Gf|| - ||Sf||)^2`, and it fails at the
indicator of the interval by a factor tending to infinity.

Proposition 7.3: the residual cannot be repaired by adjoining further positive
channels, because on the codimension-two subspace where both pole moments
vanish it is a strictly negative multiple of `||f||^2`.

So the negative contact and the pole term must come from a subtraction that is
itself a norm: `||(1 - Pi) v||^2`, never from an added channel.

### Layer 3 — the contraction must be *critical*, at every `L`

Proposition 7.14 (and it is a genuinely good reduction): at every `L`,

```
 Q_L = K_+ - T_L
 K_+[f] = K[E_L f] + (c_L)_+ ||f||^2 + 2 |<cosh(x/2), f>|^2      (a norm, explicit source)
 T_L[f] = (c_L)_- ||f||^2 + 2 |<sinh(x/2), f>|^2 + sum_p Bt_p    (positive term by term)
```

so Weil positivity on `I_L` is the single domination `T_L <= K_+`, and no
unproved inequality enters. But `||Pi_L|| = 1 - lambda_min(Q_L; K_+)` and the
domination is *saturated*: the manuscript records `1 - 1.9e-7` at `L = 1` and
`1` to within `1e-15` at `L = 3/2, 2, 3`, with the eigenvalues piling up at one
on a subspace that grows with `L`.

**This is the bottleneck.** Not "produce a contraction" — the dilation theorem
hands you one the moment `||Pi|| <= 1`, which is the statement being proved.
The requirement is a mechanism that produces a contraction whose norm is
*exactly* one to within `1e-15` at every `L` simultaneously. Any mechanism with
a margin — a gap, a mass, a regulator, a coupling that can be dialled — is
producing a false statement, because a uniform strict contraction would prove
something stronger than RH. The mechanism has to be critically tuned by
something the theory does not get to choose, for a continuum of `L`.

### Layer 4 — matching a weight inside a positive sector is cheap, so most "evidence" is worthless

Proposition 6.5 / Section 6.5: the states reachable by one magnetic insertion in
the elementary Schur representation are **exactly** the functions analytic on a
disk of radius greater than one. The mirror prime reference is among them
(Corollary 7.13), at the same fixed `q`. So the operator that appeared to be
supplying arithmetic structure constrains nothing — it is a change of weight in
a positive sector, and the space of achievable weights is essentially everything.

This is the result that should govern how the next candidate is judged. An
exhibited weight identity is not evidence unless it is accompanied by a reason
the representation could *not* have produced a different weight.

### The one-sentence version

**The primes are not the hard part, and they are where the effort has gone.**
The prime references — positive and mirror — are exactly realized, at one fixed
`q`, for every prime (Theorem 6.2, Corollary 7.13). What is missing is a
mechanism that is *critically* tuned, in one space, at every `L`; and by
Corollary 2.2 the only thing that can tune it that finely is the zeros.

---

## 2. A new numerical observation: the critical subspace is the sub-`gamma_1` band

I rebuilt `K_+`, `T_L` and `Q_L` from scratch (independent of
`numerics/check_gamma_compression.py`) on a basis of `m = 400` indicator cells
on `I_L`, using the Toeplitz structure of the gamma energy, and diagonalized the
generalized problem `(Q_L, K_+)`.

**Cross-check.** `max |Q_L - (K_+ - T_L)| < 1e-15` at every `L` tested, from a
separate implementation. Proposition 7.14's identity is confirmed independently.
`lambda_min(Q_L; K_+) = 1.9e-6` at `L = 1` against the manuscript's `1.9e-7`;
for `L >= 3/2` my values (`|lambda| < 2e-6`, sometimes slightly negative) are at
my quadrature noise floor and are consistent with the manuscript's "`1` to
within `1e-15`" but do not confirm it. Only the identity is confirmed to high
precision; the `L = 1` discrepancy is a factor of ten and one of the two numbers
is wrong — worth resolving, since it is the manuscript's headline saturation
figure.

**The observation.** Take the lowest generalized eigenvectors — the critical
directions of `Pi_L` — and measure what fraction of `|F^(tau)|^2` lies below
`tau = gamma_1 = 14.1347...`, the height of the first nontrivial zero:

| `L` | mode 0 | mode 4 | mode 9 | mode 60 | mode 200 |
|---|---|---|---|---|---|
| 2 | 0.9996 | 0.987 | 0.179 | 0.167 | 0.069 |
| 3 | 1.0000 | 0.9985 | 0.975 | 0.018 | 0.159 |
| 4 | 1.0000 | 0.9994 | 0.996 | 0.023 | 0.003 |

The near-null directions are essentially bandlimited below the first zero;
generic directions have a few per cent of their mass there. The count of modes
with more than 90 % of their mass below `gamma_1` is

| `L` | 1 | 1.5 | 2 | 2.5 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|---|
| in-band modes | 3 | 4 | 7 | 9 | 11 | 16 | 20 | 21 |
| `L*gamma_1/pi` | 4.5 | 6.8 | 9.0 | 11.3 | 13.5 | 18.0 | 22.5 | 27.0 |

i.e. the Nyquist count of `I_L` at bandwidth `gamma_1`, to within about 25 %
(the deficit is spectral leakage from the sharp interval and the 90 % cutoff).
Counts at a fixed eigenvalue threshold grow faster than linearly — roughly
`e^{cL}` with `c` between 0.4 and 0.6 depending on threshold, which is the
`sqrt(X) = e^{L/2}` scale of `sum_{p<X} kappat_p ~ 4 sqrt(X)` — but that fit is
crude and threshold-dependent and I would not rely on it.

**Why this matters.** It is not a surprise — it is Corollary 2.2 made visible,
since `Q_L[f] = sum_rho |F^(gamma_rho)|^2` is tiny exactly when `F^` avoids every
`gamma_rho`, and the cheapest way to avoid all of them is to live below the
lowest one. But it converts an abstract rigidity statement into a **cheap,
falsifiable diagnostic for a candidate mechanism**:

> Given any proposed physical compression, compute the frequency content of its
> near-null directions. If the band edge is not at `14.13`, the candidate is
> dead — and you learn this without matching a single prime.

It also relocates the difficulty. The primes live in the *bulk* of the spectrum
of `Pi_L`; the criticality lives in the low band, and what sets the band edge is
the first zero. A construction that is good at primes is working on the part of
the problem where nothing is marginal. This is, I think, the sharpest available
answer to "where is the bottleneck really".

Reproduction: the scripts are scratch and not in the repo. If this is worth
keeping it should become a repo check programme under the investigation's
conventions (standard library only, JSON to stdout, record under
`numerics/records`, registered in `validation/drafts.py`), which would require
replacing `numpy`/`scipy` by hand-rolled Toeplitz assembly and Jacobi
diagonalization. That is a half-day of work and I think it is worth it, because
the band-edge test is reusable against every future candidate.

---

## 3. What the target already tells you about the operator, before you pick a theory

Three fingerprints. All are necessary conditions, all are cheap, and none of
them is currently written down as a selection test in the investigation.

### 3.1 The archimedean part is *marginal*: a `Delta = 1/2` kernel with unit coefficient

`ngamma(r) = e^{-r/2}/(1 - e^{-2r})` satisfies `ngamma(r) ~ 1/(2r)` as `r -> 0`.
So by (2.5)

```
 K[F] = (1/2) int int |F(x)-F(y)|^2 ngamma(|x-y|) ~ (1/4) int int |F(x)-F(y)|^2 / |x-y|
```

near the diagonal: the Gagliardo seminorm at the **borderline exponent**
`1 + 2s = 1`, i.e. `s = 0`, which is exactly why the multiplier is
`b(tau^2) = log|tau| + O(1)` with coefficient **one** (2.12).

So the smearing kernel of the source must be marginal — the `Delta = 1/2` case
in one dimension — and its coefficient is fixed, not free. Any candidate whose
smeared two-point function has a power-law short-distance behaviour, or a
logarithm with the wrong coefficient, is excluded at the level of the OPE,
before any arithmetic. This is the sharpest thing the OPE has to say here, and
it is a real constraint on which operator in a fixed theory could possibly work.

### 3.2 The archimedean channel spectrum is `{2n + 1/2}` with unit residues

Exactly, not asymptotically: `ngamma(r) = sum_{n>=0} e^{-a_n r}`, `a_n = 2n + 1/2`
(2.2). Read as a transfer-matrix / Kallen-Lehmann decomposition in the separation
`r`, that is a discrete spectrum of level spacing 2 starting at 1/2, with
**every residue equal to one** — so the operator applied to the vacuum has equal
overlap with every level, and the sum of residues diverges, which is the
short-distance divergence of 3.1.

The offset `a_n / 2 = n + 1/4` is the quarter shift, which the manuscript
already notes the real Gaussian sphere boundary module supplies (Section 4). So
this fingerprint is not idle: it says *why* the sphere direction is the right
place to look for the archimedean half, and it gives a one-line rejection test
for anything else.

Caveat, and it is the manuscript's own (Section 3.1): the arithmetic coordinate
`x` is not automatically Euclidean time. Reading `ngamma` as a channel spectrum
assumes an identification that has to be supplied by the model.

### 3.3 The source must be unbounded relative to the input `L^2` norm

Proposition 3.4: `Q_L[f_N] / log N -> ||chi||^2` for `f_N = chi e^{iNx}`, so no
source of the form `Phi(f) = int f(x) V_x Omega dx` with `V_x` unitary — and no
finite direct sum of such — can match. This is the same fact as 3.1 seen from
the Fourier side.

---

## 4. Assessment of the five ideas

### (A) Fix the theory, search for the operator inside it

**This is already what the Schur direction does**, and the result is a warning
rather than an encouragement. The search there is over electric dressings
`D_{q,a}` and magnetic insertions at one fixed `q`, and Section 6.5 shows the
reachable set is *everything analytic past the unit circle*. So in the one place
where "fix the theory, vary the operator" has been carried out concretely, the
operator search turned out to be too flexible to carry information, and what
actually bit was the architecture exclusion (Theorem 7.5), which no choice of
operator can evade.

**The version of your idea that is not already dead** is to change *what* is
being searched for. Layer 2 says the missing object is not a state and not a
weight — it is a **projection or compression**. States in a protected sector are
cheap; projections are not. A projection in a protected algebra is rigid: its
trace is constrained, it has to commute with the algebra's symmetries, and
Proposition 2.4 already forces it to commute with the reflection involution
`J`. So:

> Search a fixed theory not for an operator whose expectation value is the Weil
> form, but for a **projection or conditional expectation** whose compression of
> a known positive form is it.

Concretely, the objects to enumerate in the Schur/RG setting are: the Weyl
constraint and projection of the conformal `SU(2)` benchmark (already flagged at
(8.8), and the one place in the manuscript where a projection appears
naturally); BRST or cohomological projections; interface and gluing kernels;
charge-neutral line words. That is a small, finite list — which is exactly the
rigidity you were hoping for, and you do not get it from the state side.

### (B) Wilson lines rather than Wilson loops

**Right instinct, and the reason is stronger than the one you gave.** It is not
the periodicity. The test functions carry no boundary conditions at all, so
nothing in the target asks for or forbids a periodic geometry.

What actually killed the Wilson-loop benchmark (Section 5.1) is that the Wilson
operator acts as `W = 2 cos(theta)`, whose spectrum is **bounded**, confined to
`[-2, 2]`. Two consequences, both fatal: the kernel
`int e^{2ir cos(theta)} dnu_q(theta)` is *entire* in `r`, so it cannot have
separated atoms at `± m log p`; and the pairing is bounded in `||f||_{L^2}`,
which contradicts Proposition 3.4 (§3.3 above).

So the criterion your instinct is reaching for is: **the operator's spectral
variable must be unbounded.** Line operators in the Schur setting do satisfy
this — the quantum torus `X_gamma X_eta = q^{<gamma,eta>} X_{gamma+eta}` on the
charge lattice has unbounded generators and multiplicative difference actions,
which is also the natural home for repeated translations. So lines are a
genuine improvement over loops, for a checkable reason, and it is worth
restating that reason in the manuscript because "loops failed" currently reads
as an accident of one benchmark.

Two cautions. First, an unbounded spectral variable is necessary, not
sufficient, and Layer 4 says the deformation freedom of a line is almost
certainly too large to be informative. Second — and this is the useful part —
**what you cannot deform is the trace.** The line is soft; the twisted trace
`T(rho(a) b)` is fixed by the theory. If the arithmetic is anywhere, it is in
the trace, not in the choice of line. That also points at (D) below.

### (C) A family of operators giving the Weil term for different `L`

Two things to disentangle here, and I think the idea as stated over-counts the
freedom.

`W` is one functional and `Q_L` is its restriction to `C_c^inf(I_L)`. The
correlations `<F, U_r F>` vanish for `|r| >= L` automatically for zero-extended
`f`, so the prime sum truncates by itself; nothing in the model has to know
about `L`. A candidate that produces `W` produces every `Q_L` at once, and
compatibility in `L` is then not an extra condition to arrange, it is automatic.

Conversely, if a proposed family is *not* compatible — different `Phi_L` with no
common restriction — then by Layer 1 it proves nothing, because `Q_L^{1/2}`
already works at each `L` separately and Krein even makes it stationary. So:
an `L`-family buys freedom only in the regime where it is worthless, and in the
regime where it would be worth something it is unique by Corollary 2.2.

**What is left, and it is worth something.** The `L`-dependence that is real is
in `Pi_L`: the constant `c_L` is a step function jumping at `L = log p`, the
prime set changes, and the near-null dimension grows (§2). So if a deformation
parameter of a Wilson line is going to track anything, the honest question is
whether it can track the *growth of the critical subspace*, not whether it can
reproduce `Q_L` at each `L`. That is a much sharper target and §2 now gives it a
measurable signature: band edge fixed at `gamma_1`, dimension growing at the
measured rate. A deformation family whose near-null dimension grows at a
different rate is excluded, cheaply.

### (D) Existence proofs without explicit computation

**The best of the five, with one trap.**

The trap: pure existence is circular. Corollary 7.9 already produces `V` and `P`
from the dilation theorem the moment `||Pi|| <= 1` — and `||Pi|| <= 1` *is* the
Weil criterion. So an existence argument that uses only positivity and abstract
operator theory establishes nothing that is not assumed.

The escape: the content is not "an operator exists" but "an operator exists
**in this algebra**". A non-constructive proof is worth everything if what it
establishes is *membership in a specified physical sector*, using independently
known structure of that sector — faithfulness of the twisted trace, generators
of its positive cone, a density or approximation theorem, a classification.

That is a real and tractable literature-driven project, and the manuscript
already cites the right entry points: the classification results for positive
twisted traces on protected algebras (Etingof-Klyuev-Rains-Stryker and Klyuev,
cited at Section 3.3 as `EKRS`, `Klyuev`). If those classifications are complete
enough on some family, then "the required positive form lies in the classified
family" is a membership statement provable without exhibiting the form. I would
put a session into reading exactly how complete they are. This is the one idea
on your list that could produce a theorem without a construction.

### (E) Perturbation theory plus a conjecture about the full answer

**Fatal as a route to the identity, valuable as a filter.**

Fatal because of two facts already in hand. First, the cancellation: for a
smooth input on `I_4` the four terms of (2.9) are `3.40, -8.06, 9.11, -4.46` and
their sum is `1.4e-7`. A perturbative expansion would have to reproduce a
quantity eight orders of magnitude below the terms it is built from, and by
Corollary 2.2 that quantity is `sum_rho |F^(gamma_rho)|^2`, which is not visible
at any finite order of a generic scheme. Second, Theorem 7.5: **every term can
be matched exactly while no realization exists.** Term-by-term perturbative
agreement is precisely the failure mode already proved fatal.

Valuable because Section 8.2 asks the right question of a candidate — extract a
**spectral measure or density of states** and ask whether it is the zero
counting measure — and the *leading* density of states is exactly what
perturbation theory computes well. So:

> Use perturbation theory to compute the leading density of states of a
> candidate and compare with `(1/2pi) log(tau / 2pi)`. If the leading density is
> wrong, stop.

That is cheap, it is a genuine discriminant, and it is the perturbative
calculation worth doing. It just is not a step toward the identity.

### (F) Operator product expansions

**Genuinely useful and the least exploited, but it is structurally half of the
problem, and the half that is not the bottleneck.**

What the OPE controls is the coincident limit, and §3.1 and §3.2 above are
exactly what it gives: a marginal `Delta = 1/2` kernel with unit coefficient,
and an exact channel spectrum `{2n + 1/2}` with unit residues. Those are two
sharp, cheap selection rules on which operator in a fixed theory could work, and
they are not currently written down anywhere in the investigation. Getting them
into the candidate-selection battery is worth doing this week.

What the OPE *cannot* see is the primes. They are atoms at fixed non-coincident
separations `x - y = ± m log p` (Section 2.3 makes exactly this distinction: the
gamma kernel is smooth off the diagonal, the prime contribution has atoms). A
short-distance expansion has nothing to say about them. Atoms at fixed
separations are the signature of a *periodic-orbit or trace-formula* mechanism,
with `log p` as primitive periods — a different physical structure entirely.

And that is worth stating plainly, because it sharpens Theorem 7.5 into a
structural statement rather than a calculation:

> The two halves of the target naturally call for two different physical
> mechanisms — an OPE/short-distance mechanism for the archimedean part, a
> periodic-orbit mechanism for the primes — and Theorem 7.5 forbids them from
> being two channels. One object has to do both. That is the architecture
> problem in one sentence.

---

## 5. Suggested order of work

Cheap and reusable first. Items 1-3 are a **candidate test battery**; running a
new candidate through it should take an afternoon, not a session.

1. **Write down the battery.** Necessary conditions a candidate must pass,
   cheapest first: (i) commutes with `x -> -x` (Proposition 2.4); (ii) unbounded
   relative to input `L^2` (Proposition 3.4) — this is the one that kills bounded
   spectral variables, i.e. Wilson loops; (iii) marginal short distance with
   unit log coefficient (§3.1); (iv) channel spectrum `{2n + 1/2}` with unit
   residues (§3.2); (v) interference bound (7.9); (vi) leading density of states
   equals the zero density (§4E); (vii) critical contraction with near-null band
   edge at `gamma_1` (§2). Items (iii), (iv), (vi), (vii) are new.
2. **Turn §2 into a repo check programme** under the investigation's conventions,
   and resolve the factor-of-ten discrepancy in `lambda_min` at `L = 1` while
   doing it.
3. **Read EKRS and Klyuev for completeness of the classification** of positive
   twisted traces (§4D). This is the only route on the list that could give a
   theorem without a construction.
4. **Enumerate the projections**, not the states, available in the Schur/RG
   setting (§4A): the Weyl constraint and projection of (8.8) first, then BRST
   or cohomological projections, then interface kernels. Test each against the
   battery.
5. Leave the prime side alone. It is done, at one fixed `q`, in both signs
   (Theorem 6.2, Corollary 7.13), and Section 6.5 says further weight-matching
   carries no information.

## 6. What is proved, and what is not

- Layers 0-4 of §1 are all theorems in manuscript 0.5, referenced above.
- §2's identity cross-check is exact (a finite matrix identity, `< 1e-15`, from
  an independent implementation). §2's band-edge observation and all counts are
  **numerical**, on a 400-cell Galerkin discretisation, with a quadrature noise
  floor near `1e-6`; the growth-rate fit is crude and threshold-dependent and
  should not be quoted. The disagreement with the manuscript's `lambda_min` at
  `L = 1` is unresolved.
- §3.1 and §3.2 are elementary consequences of (2.2) and (2.5)-(2.12); §3.2's
  reading of `ngamma` as a channel spectrum assumes an identification of the
  arithmetic coordinate with Euclidean time that the manuscript explicitly does
  not make.
- §4 is assessment, not result.
