# Continuation note, 15 September 2026

**Author: Claude Opus 5 (Anthropic).** Handoff for a new session on the
inverse-bulk investigation. Read this first, then the two notes it points at.

## 1. State of the investigation

Working manuscript **0.3** (35 pages). Versions 0.1, 0.2 and 0.3 are preserved
in [`drafts/`](../drafts/README.md); `python3 validation/drafts.py check --replay`
passes with seven check programmes and 1,475 cases. The replay takes about a
minute — `check_mirror_subtraction.py` is about 50 s and
`check_explicit_formula.py` about 13 s; the other five are instant.

What changed on 15 September, from a review of version 0.1:

- **0.2** added the spectral form of the target (Corollary 2.2) and the
  exclusion of the gamma-plus-prime architecture (Proposition 7.3, Lemma 7.4,
  Theorem 7.5), plus the spectral-realization literature and two check
  programmes.
- **0.3** added the mirror prime reference and the prime-free subtraction form
  (Section 7.5: Proposition 7.7, Theorem 7.8, Corollary 7.9, Remark 7.10),
  the prime-free target (8.1) and Problem 8.2.

Supporting material: [review of 0.1](../reviews/review_claude_opus_5_20260915.md),
[exclusion note](INTERFERENCE_BOUND_AND_TWO_CHANNEL_EXCLUSION.md),
[subtraction-form note](MIRROR_REFERENCE_AND_SUBTRACTION_FORM.md).

## 2. The three facts a new session needs

**(a) The target is tiny compared with its terms.** By the explicit formula
`Q_L[f] = sum over zeros of |F^(gamma)|^2`. For a smooth input on `I_4` the
four terms of (2.9) are 3.40, −8.06, 9.11, −4.46 and their sum is 1.4e−7.
Matching the terms one at a time is not a weaker version of matching the
total.

**(b) Additive architectures are dead.** For any two channels,
`||sqrt(t) G f + t^{-1/2} S f||^2 >= 0` gives `t A + B/t + C >= 0` for all
`t > 0`. With `A = K` and `B = sum_p B_{r_p,d_p}` this fails: at `L = 5/4`,
`f = 1_{I_L}`, `t = 13/10`, the value is −0.293 while `Q_L[f] = +0.077`. It
also fails at `L = 1` and for all large `L`, and letting the channels absorb
constants and a share of the poles does not rescue it (section 5 of the
exclusion note; this part is numerical, not a theorem).

**(c) The subtraction form is the way through.** The mirror reference
`wt_{r,d}(z) = d r (1-r)/(1+r) |1+z|^2/|1-rz|^2` has the same prime atoms with
the opposite sign and contact `2dr/(1+r) < 2dr/(1-r)`. Hence

```
Q_L = A_L - sum_p Bt_{r_p,d_p},
A_L = K[E_L f] + (w0 + sum_p kappat_p) ||f||^2 + P_L[f],
```

with `A_L` free of prime translations. Weil positivity on `I_L` is exactly
`sum_p Bt_p <= A_L`, i.e. `||Pi_L|| <= 1` for
`Pi_L = A_L^{-1/2}(sum Bt_p) A_L^{-1/2}` — a compression, which (b) does not
constrain.

## 3. What to do next, in order

1. **Prove the prime-free inequality (8.1)**:
   `K[E_L f] + (w0 + sum_{p<e^L} kappat_p) ||f||^2 + P_L[f] >= 0`.
   Primes enter only through the constant. Galerkin margins are 0.26 at
   `L = 1` rising to 22 at `L = 5`, so there is real slack, unlike `Q_L`.
   Start with `L <= log 2`, where the constant is just `w0` and there are no
   primes at all, and see whether the compressed-scaling-action argument of
   Connes-Consani (arXiv:2006.13771) delivers it. This is the most likely
   place to get a genuine theorem.
2. **Settle Remark 7.10**: does the elementary `q`-Weyl representation produce
   the mirror weight? The required output state is `(1 - zeta)/(1 + r zeta)` —
   same denominator as Lemma 6.1, numerator sign reversed. The three obvious
   routes are blocked (see the remark); either find a fourth or prove the
   elementary representation cannot do it, which would be an informative
   exclusion in its own right.
3. **A certified lower bound on `lambda_min(Q_L)`** at `L = 1, 5/4, 3/2` by
   interval arithmetic. It would confirm unconditional local Weil positivity
   there, turn the numerical part of (b) into a theorem, and give every future
   candidate an immediate kill test.
4. **The pole mechanism**, still unaddressed: `P_L` is rank two with one
   negative direction, and every pairing in the manuscript is positive by
   construction. Which protected sector admits an exactly rank-two indefinite
   correction — ghost or BRST sector, a boundary condition that is not
   reflection positive, a rank-two defect projection?

## 4. Things not to redo

- Do not look for a better additive split of `Q_L` into positive channels.
  That is Theorem 7.5 and the numerics of section 5 of the exclusion note.
- Do not test candidates by matching the terms of (2.9) one at a time; use the
  interference bound (7.9) first, it is cheap and kills most proposals.
- The dressed Schur identity (Theorem 6.2) is correct and does not need
  rechecking; what it lacked was a way to be completed.

## 5. Working conventions in this investigation

- Reviews go in [`reviews/`](../reviews/README.md), research notes here, with
  the author model named at the top of anything written by a language model.
- Revise the manuscript only after the investigation settles; snapshot the
  current version with `validation/drafts.py save YYYY-MM-DD-vNN` before
  replacing it, and never touch an existing snapshot.
- Check programmes are standard library only, print JSON to stdout, and have a
  preserved record under `numerics/records/`; add new ones to the `CHECKS`
  dictionary in `validation/drafts.py`.
- Everything stays under 1 MiB per file; see
  [LARGE_FILES.md](../../../../../LARGE_FILES.md). Rendered PDF pages belong in
  the ignored `build/` directory, not in the package. There are stale render
  directories in `build/review/` and `build/review2/` that can be deleted.
