# Continuation note, 16 September 2026 (end of session)

**Author: Claude Opus 5 (Anthropic).** Handoff for the next session. This
replaces the mid-session version of the same date, which was written before the
manuscript existed and whose ordered next steps are superseded by §3 below.

Read in this order: [the manuscript](../manuscript.pdf) (15 pages), then §§1--3
here, then [the open directions](OPEN_DIRECTIONS_20260916.md).

---

## 1. Where the two manuscripts stand

**This investigation, version 0.1** --- *A jump-process presentation of the
localized Weil form*, 15 pages, nine sections and an appendix. Builds clean,
recorded after a page-by-page review, snapshotted as `drafts/2026-09-16-v01`,
and `python3 validation/drafts.py check --replay` passes over 44,289 recorded
cases. It is self-contained: it inputs no shared background and cites the
companion manuscript only for the program's objective and for results quoted by
number. **Nothing in it assumes RH and nothing in it proves Weil positivity.**

**The companion investigation, version 0.6** --- three changes were made this
session: the saturation figures of Section 7.6 were corrected (the previous
version attributed them to a computation that does not produce them; see §5
below), Remark 7.12 on Suzuki's unconditional results was added, and Section 7.7
was added carrying Propositions 7.13 (the jump form) and 7.14 (the necessary
condition). It builds clean at 42 pages. **Its `BUILD_RECORD.json` is stale** and
`validation/drafts.py check` will fail there until someone reads the rendered
pages and runs `record` and `save`. That is the one outstanding human action.

---

## 2. The five facts a new session needs

**(a) The archimedean symbol is the smooth zero density.**
`b(tau^2) + w0 = 2 theta'(tau)`, so the archimedean energy together with the
contact is `int |F^|^2 dNbar`. The contact constant is not an independent object:
it is the `-log pi` inside `theta'`. Everything in Section 3 of the manuscript
follows from this, including the meaning of the `p = 13` crossing.

**(b) The target is one jump form.** `Q_L = E_{mu_L} + gamma_L ||f||^2 + P_L`
with `mu_L >= 0` carrying the archimedean density as its continuous part and the
prime atoms as its atomic part. The archimedean and prime halves are not two
channels; a source is a jump process whose jumps are the primes. This is what the
companion manuscript's two-channel exclusion asks for.

**(c) The pole term is the obstruction, in three independent ways.** It cannot
be supplied by an adjoined positive channel; it is the indefinite part under the
parity split; and it destroys the Beurling--Deny cone that the jump form
otherwise carries, by Sherman--Morrison, even in its positive half. Every
structural dead end this session traced back to it.

**(d) The margin collapses, and no method may assume otherwise.**
`min spec(Q_L; K_+)` is below `1e-9` at `L = 1` and below `1e-24` at `L = 3`.
Any hypothesis supplying a margin uniform in `L` --- a self-map into a fixed
compact subset of a cone's interior, a uniform contraction ratio, a spectral gap
--- proves something false. This is selection rule 7 and it has killed more
proposals than anything else.

**(e) Always say which direction a one-sided value certifies.** Saturation
quotients are Rayleigh quotients in a subspace, so they certify only *failure* of
a domination; Galerkin values of `alpha_L` are lower bounds, so they certify only
the direction a disproof needs. Half the care in this session went into keeping
those straight, and the one substantive error found in version 0.5 of the
companion manuscript was of exactly this kind.

---

## 3. Recommended pathway, in order

**1. Read Suzuki, arXiv:2301.00421.** Reportedly it shows the Hilbert space of
the Weil distribution *is* a de Branges space, produces a totally ordered family
of subspaces, and converts the RH criterion **from inequalities into
equalities**. That last is why it is first: the central structural problem of
this whole program is that the criterion is an inequality critical to more than
twenty digits, so no margin-based method can prove it and no finite computation
can certify it --- which is exactly why the disproof test came back with a fixed
gap. An equality formulation sidesteps that. It is also the cheapest item on the
list, one session of reading, and the single verified contact with Suzuki's work
(his Theorem 1.4 reproducing our density identity at the interval's own frequency
scale, constant included) suggests the rest connects. *Second-hand; arXiv:2606.09096
has been read directly, this one has not.*

**2. The spectral gap of the jump form.** `lambda_2(S_L)` sits near `2e-4`, is
roughly constant over `3/2 <= L <= 4`, and is where the criticality of the target
originates: the pole supplies only a rank-one cancellation of one large negative
eigenvalue and does not create the near-degeneracy. This is a well-posed
spectral-gap question about an explicit nonlocal Dirichlet form on an interval,
in a developed literature this program has not touched, and it is the ingredient
the necessary condition is missing. **One connection worth testing first:**
`N_L` is entrywise positive off the diagonal, so Birkhoff's contraction theorem
*does* apply to it, and what Birkhoff bounds is `|lambda_2|/|lambda_1|` --- which
is this gap. The cone is useless on `Q_L` and may be useful on `N_L`. That
observation is untested.

**3. Why is the ground state `cosh(x/2)`?** The ground state of an operator
assembled from the archimedean density and the prime atoms has cosine `0.9844`
rising to `0.9998` with the pole form's positive direction. Nothing forces this.
A proof would make the rank-one cancellation structural rather than numerical and
would very likely sharpen Proposition 7.1. Of everything open, this is the item
most likely to have a clean theorem behind it.

**4. Port two computations into registered checks** (item A4 of the open
directions): the smooth-basis saturation values, and the near-null band edge.
Both are quoted in the manuscripts and neither is reproducible under the
repository's conventions. Doing this closes the gap that produced the version 0.5
error in the first place.

**Why this order.** Item 1 could change what the other three are for, and costs
least. Items 2 and 3 are the two places where a numerical fact is asking for a
proof, which is the most reliable kind of open problem. Item 4 is maintenance
and can be done by a session with no context.

---

## 4. The brainstorming angles

All of it is in [OPEN_DIRECTIONS_20260916.md](OPEN_DIRECTIONS_20260916.md),
grouped and ranked. In summary:

- **Group A, ready now** --- the four items of §3 above.
- **Group B, open with a named obstruction** --- a cone adapted to the pole
  directions, with Rugh's complex-cone theory as the tool; the sharp two-scalar
  form of the necessary condition, which is exact but relocates the difficulty
  rather than reducing it; selection rule 6 for infinite prime sums, which is
  Guinand--Weil duality and stands directly in the path of the physics side; and
  the Gaiotto--Teschner spherical-vector correspondence, which converts existence
  of a positive pairing into normalizability of a solution of a `q`-difference
  system and is the strongest physics-side handle found --- but which should wait
  until rule 6 is settled.
- **Group C, closed with reasons** --- nine items, each not to be redone. The
  headline is that **every existence theorem in this subject transports positivity
  rather than creating it**; the one mechanism that manufactures it,
  Ruelle--Perron--Frobenius via Birkhoff cone contraction, is unoccupied in the
  Weil-positivity literature and is what motivated Sections 6 and 7 of the
  manuscript.
- **Group D, external work** --- Zhu arXiv:2608.24827 (borrow the tail-envelope
  reduction; discount the fitted decay law and the barrier, and note the
  reliability flags); Suzuki's numerical companion arXiv:2607.24830; Bombieri's
  index argument, which is attractive precisely because an index is an integer and
  therefore immune to the collapsing margin.
- **Group E, method notes** --- the practical lessons, including the one that cost
  the most time: never assemble `Q_L` term by term in double precision, because
  its terms are eight orders of magnitude larger than the answer.

---

## 5. What not to redo

- Do not look for a better additive split of `Q_L` into positive channels.
- Do not attempt non-constructive existence of a realization: it is exactly RH,
  and abstract operator theory applied to the target alone returns its input.
- Do not use Knaster--Tarski on operator intervals (Kadison's antilattice
  theorem), and do not look for the source at a scale-invariant RG fixed point
  (the primes fix an absolute scale).
- Do not revive the conjectured prime budget from the twisted-trace
  classification. The elementary Schur algebra is the generalized `q`-Weyl algebra
  with `P(y) = 1 + y`, verified in exact arithmetic, so its trace space is one
  dimensional and carries no arithmetic at all.
- Do not expect Krein--Langer screw continuation to help: it is Remark 3.3 of the
  companion manuscript under a different name.
- Do not test candidates by matching the terms of the target one at a time.

---

## 6. Conventions

- Research notes here, reviews in [`reviews/`](../reviews/README.md), with the
  author model named at the top of anything written by a language model.
- Check programs are standard library only, print JSON to stdout, keep a
  preserved record under `numerics/records/`, and are registered in the `CHECKS`
  dictionary of `validation/drafts.py`. There are five.
- Snapshot before replacing a manuscript version: `drafts.py save YYYY-MM-DD-vNN`.
  See [the build guide](../BUILD.md) for what `BUILD_RECORD.json` is for.
- Everything stays under 1 MiB per file; see the repository's
  [large-file policy](../../../../../../LARGE_FILES.md). Rendered pages belong in the
  ignored `build/` directory and should be deleted after a review.
- A session without delete permission in the repository folder will leave a stale
  `.git/index.lock` after any git command; remove it with `rm -f .git/index.lock`
  before the next commit.
