# Continuation note, 15 September 2026

**Author: Claude Opus 5 (Anthropic).** Handoff for a new session on the
inverse-bulk investigation. This supersedes the earlier handoff of the same
date, which is preserved in git at commit `3d63aa7`; its ordering of next
steps was wrong and section 3 below explains why. Read this, then the notes it
points at.

## 0. Status update, later on 15 September 2026

**Both items 1 and 2 of section 3 below are closed. Section 3's ordered list
should be read as superseded by this section.**

**Item 2 — Remark 7.10 — is settled, affirmatively.** The mirror weight is
reachable: one negative magnetic insertion applied to an admissible electric
preparation at the same fixed `q`, with the dressing of Lemma 6.1 and the sign
of its first Pochhammer factor reversed. More generally the reachable output
states are exactly the functions analytic on a disk of radius greater than one,
so the `(1+zeta)` that `u_-` supplies constrains nothing, and weight-matching
inside a positive sector is cheap and carries little information. See
[MIRROR_DRESSING_AND_REACHABLE_STATES_20260915.md](MIRROR_DRESSING_AND_REACHABLE_STATES_20260915.md)
and `numerics/check_mirror_dressing.py`.

**Item 1 — the ghost pair — should be struck.** The specification asks for a
structure that a realization cannot have and does not need. A realization
compatible in `L` is, by Corollary 2.2, evaluation on the zeros in a positive
`l^2`, which has no null vectors at all; and under the subtraction form the
pole term sits inside `A_L`, which is positive by Yoshida below `log 2`, by
Proposition 8.1 above `log 7`, and by RH everywhere. Its negative direction is
rank one, bounded by `2(sinh(L/2) - L/2)`, and nowhere near binding: below
`log 2` the binding direction of `A_L` is *even*, where the pole form is
positive, and above it admitting the negative direction costs three per cent of
the margin at `L = 1`. Section 8.2 of the manuscript needs a correction; see
[POLE_TERM_NEEDS_NO_MECHANISM_20260915.md](POLE_TERM_NEEDS_NO_MECHANISM_20260915.md),
section 5, for exactly which sentences.

**What replaces them, and it is smaller than the first half of Problem 8.3.**
That first half — realize `A_L` as a positive source norm — can be dropped too.
Splitting the pole form by parity, (2.17), and letting the constant sit on
whichever side its sign puts it on gives, at every `L`,

```
 Q_L = K_+ - T_L,
 K_+[f] = K[E_L f] + (c_L)_+ ||f||^2 + 2 |<cosh(x/2),f>|^2,
 T_L[f] = (c_L)_- ||f||^2 + 2 |<sinh(x/2),f>|^2 + sum_p Bt_p[E_L f],
```

with `K_+` manifestly a norm — explicit source
`Gf = (b^{1/2}(D)E_L f, (c_L)_+^{1/2} f, sqrt2 <cosh(x/2),f>)` — and `T_L`
manifestly positive term by term. So Weil positivity on `I_L` is the single
domination `T_L <= K_+`, the dominating side is an object one can actually
build, and **no unproved positivity enters the presentation at all**. The
construction problem is now exactly: exhibit the contraction. See
[GAMMA_COMPRESSION_PRESENTATION_20260915.md](GAMMA_COMPRESSION_PRESENTATION_20260915.md)
and `numerics/check_gamma_compression.py`.

The surviving necessary condition from the discarded pole-sector test is
Proposition 2.4's involution, and nothing else. Item 3 of section 3 (what to
compute in a candidate model: a spectral measure, not a term-by-term match)
stands unchanged.

**Item 4 stays parked, and for a better reason than before.** The compact
window `log 2 < L < log 7` is the range on which `A_L >= 0` is known only from
RH, which briefly looked like a prerequisite for constructing a source for
`A_L`. In the presentation above `A_L` never appears, so (8.1) is not a
prerequisite for anything in the construction programme. It remains an
interesting question about `A_L` and nothing is waiting on it.

**All three results are now in the working manuscript**, version 0.5:
Section 6.5 and Corollary 7.10 for the reachable states and the mirror
dressing, Section 7.6 for the compression, and the revision of Section 8.2
withdrawing the indefinite-metric claim, with Problem 8.3 restated as the
single compression. Version 0.4 is preserved in `drafts/2026-09-15-v04`.

Sections 1 to 5 below are otherwise unchanged and remain the handoff, with
section 3's ordering superseded as above. Note that section 1's description of
the state of the investigation refers to version 0.4.

## 1. State of the investigation

Working manuscript **0.4** (37 pages). Versions 0.1 to 0.4 are preserved in
[`drafts/`](../drafts/README.md); `python3 validation/drafts.py check --replay`
passes with eight check programmes and 80,141 cases, in about forty seconds.

What changed on 15 September, across three sessions:

- **0.2** added the spectral form of the target (Corollary 2.2) and the
  exclusion of the gamma-plus-prime architecture (Proposition 7.3, Lemma 7.4,
  Theorem 7.5).
- **0.3** added the mirror prime reference and the prime-free subtraction form
  (Section 7.5), the prime-free target (8.1) and Problem 8.2.
- **0.4** added Section 2.5 — the pole form as a hyperbolic pair and the
  involution every source carries — rewrote Section 8.2 on that basis, settled
  (8.1) outside a compact window, and added an author field and a preparation
  note on the use of a language model.

Supporting material: [review of 0.1](../reviews/review_claude_opus_5_20260915.md),
[exclusion note](INTERFERENCE_BOUND_AND_TWO_CHANNEL_EXCLUSION.md),
[subtraction-form note](MIRROR_REFERENCE_AND_SUBTRACTION_FORM.md),
[prime-free note](PRIME_FREE_ARCHIMEDEAN_INEQUALITY_20260915.md).

## 2. The five facts a new session needs

**(a) The target is tiny compared with its terms.** By the explicit formula
`Q_L[f] = sum over zeros of |F^(gamma)|^2`. For a smooth input on `I_4` the
four terms of (2.9) are 3.40, −8.06, 9.11, −4.46 and their sum is 1.4e−7.
Matching the terms one at a time is not a weaker version of matching the total.

**(b) Additive architectures are dead.** For any two channels,
`||sqrt(t) G f + t^{-1/2} S f||^2 >= 0` gives `t A + B/t + C >= 0` for all
`t > 0`, and with `A = K`, `B = sum_p B_{r_p,d_p}` this fails at `L = 5/4`,
`f = 1_{I_L}`, `t = 13/10` (value −0.293 against `Q_L[f] = +0.077`). Letting
the channels absorb constants and a share of the poles does not rescue it.

**(c) The subtraction form is the way through.** The mirror reference
`wt_{r,d}` has the same prime atoms with the opposite sign and a smaller
contact, so `Q_L = A_L − sum_p Bt_p` with `A_L` free of prime translations.
Weil positivity on `I_L` is exactly `||Pi_L|| <= 1` for a compression `Pi_L`,
which (b) does not constrain.

**(d) The pole form is a hyperbolic pair, and every source carries an
involution.** In the coordinates `u = Fhat(i/2)`, `v = Fhat(−i/2)` — the
evaluations at the two poles of `zeta`, at `s = 1` and `s = 0` —

```
P_L[f] = 2 Re( u conj(v) ),
```

off-diagonal, signature `(1,1)`, with each pole evaluation a null vector. The
negative direction is not carried by either pole but by their antisymmetric
combination. And if `||Phi(f)||^2 = Q_L[f]` then there is a unitary `J` with
`J Phi(f) = Phi(f(−·))`, `J^2 = 1`, whose `+1` and `−1` eigenspaces carry the
positive and negative directions of the pole form; for a realization
compatible in `L` that `J` is the functional-equation involution
`rho <-> 1 − rho` of the zeros. This is Lemma 2.3 and Proposition 2.4.

**(e) The prime-free inequality (8.1) is settled outside a compact window, and
it was never a discriminating test.** `A_L = Q_L + sum_p Bt_p` with `Bt_p >= 0`,
so (8.1) follows from RH and cannot fail unless RH does — unlike the
interference bound of (b), which could fail and did. For `L <= log 2` it *is*
the Weil criterion and is Yoshida's Theorem 1; for `L >= log 7` it is
Proposition 8.1 here; the window `log 2 < L < log 7` is open and is analysis,
not construction.

## 3. What to do next, in order

The goal of the programme is a positive physical system whose source norm is
the Weil form. By Corollary 2.2 a compatible realization is unitarily
equivalent to the evaluation map on the zeros, so **no inequality about `Q_L`
can decide whether an independently motivated family of pairings contains such
a source.** The previous handoff put two analysis items first; that was the
wrong order. The construction items come first.

1. **The pole mechanism, now a specification rather than a list.** Find a
   protected sector containing a two-dimensional subspace with a split inner
   product whose two null vectors are the `s = 0` and `s = 1` evaluations,
   exchanged by a unitary involution acting on the rest as `rho <-> 1 − rho`,
   with the subtraction confined to its `−1` eigenspace. This is a ghost pair
   with its pairing fixed. Candidates worth testing in that order: a BRST or
   ghost sector of the Schur construction; the Weyl constraint of the conformal
   `SU(2)` benchmark (8.8), whose neutral term and projection are already
   flagged; a boundary condition in sphere quantization that is not reflection
   positive. The test is cheap and comes before any arithmetic matching: does
   the sector's twisted trace have a rank-two split part exchanged by a
   reflection?
2. **Remark 7.10, the mirror weight in the elementary `q`-Weyl
   representation.** The required output state is `(1 − zeta)/(1 + r zeta)` —
   the state of Lemma 6.1 with the numerator sign reversed. Three routes are
   blocked in the remark; find a fourth or prove the elementary representation
   cannot do it. A clean negative answer would say the mirror references need a
   different protected sector than the one producing the positive references,
   which is itself a construction constraint.
3. **What to compute in a candidate model** (Section 8.2): a spectral measure
   or density of states, and whether it is the zero counting measure. Not a
   term-by-term match of (2.9).

Parked, deliberately:

4. The compact window `log 2 < L < log 7` for (8.1). The most promising tool is
   the interior Dirichlet form discarded in Proposition 8.1: for `L <= 3.5` it
   dominates the `1/|x−y|` energy, whose mean-zero spectral gap on an interval
   is **scale invariant** — one universal constant, computable once, usable at
   every `L`. Worth a short session if someone wants the inequality closed, but
   it constrains no candidate theory.
5. A certified lower bound on `lambda_min(Q_L)`. The true values are near
   `1e−6` at `L = 1` and far smaller beyond; [arXiv:2608.24827](https://arxiv.org/abs/2608.24827)
   claims `8.9e−18 <= lambda_min <= 2.27e−17` at `L = 1.6` by certified
   computation. Read that before duplicating it. It is unrefereed and its
   author changed between versions, but its attribution of the `log 2` window
   to Yoshida is correct.

## 4. Things not to redo

- Do not look for a better additive split of `Q_L` into positive channels.
  That is Theorem 7.5 and section 5 of the exclusion note.
- Do not re-prove (8.1) for `L <= log 2`. It is Yoshida, Theorem 1, and the
  paper is in the project files as `Yoshida.pdf`.
- Do not pursue the compressed scaling action of Connes-Consani for (8.1).
  Their functional excludes the pole terms and their hypothesis is exactly
  `P_L = 0`, which is the one thing a source norm cannot discard.
- Do not test candidates by matching the terms of (2.9) one at a time; use the
  interference bound (7.9) first, it is cheap and kills most proposals.
- The dressed Schur identity (Theorem 6.2) is correct and does not need
  rechecking.

## 5. Working conventions in this investigation

- Reviews go in [`reviews/`](../reviews/README.md), research notes here, with
  the author model named at the top of anything written by a language model.
- Snapshot the current version with `validation/drafts.py save YYYY-MM-DD-vNN`
  before replacing it, and never touch an existing snapshot. Record a build
  with `validation/drafts.py record` and an honest visual-review note.
- Check programmes are standard library only, print JSON to stdout, have a
  preserved record under `numerics/records/`, and are registered in the
  `CHECKS` dictionary of `validation/drafts.py`. There are eight.
- Everything stays under 1 MiB per file; see
  [LARGE_FILES.md](../../../../../../LARGE_FILES.md). Rendered pages belong in the
  ignored `build/` directory and should be deleted after a review.
- Git in the desktop workspace cannot delete files unless the session has been
  granted deletion in the repository folder; without it every git command
  leaves a stale `.git/index.lock` and the next one reports that another git
  process is running. There is also no committer identity configured there.
