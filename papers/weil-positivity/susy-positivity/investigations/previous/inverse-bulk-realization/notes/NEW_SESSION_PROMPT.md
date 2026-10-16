I am continuing work on the inverse-bulk realization investigation in my
shifted-zeta-positivity repository, at
`papers/susy-positivity/investigations/previous/inverse-bulk-realization`.

Start by reading, in this order:

1. `notes/CONTINUATION_20260915.md` — the handoff note. **Read section 0
   first**: both of the ordered items in its section 3 are now closed, and
   section 0 says what replaces them.
2. `notes/POLE_TERM_NEEDS_NO_MECHANISM_20260915.md` — why the pole term needs
   no ghost pair, what the corrected construction target is, and which
   sentences of Section 8.2 are wrong.
3. `notes/GAMMA_COMPRESSION_PRESENTATION_20260915.md` — the presentation the
   construction target now refers to.
4. `notes/MIRROR_DRESSING_AND_REACHABLE_STATES_20260915.md` — why the Schur
   side's open question is closed, and why weight-matching inside a positive
   sector is cheap and carries little information.
5. `notes/INTERFERENCE_BOUND_AND_TWO_CHANNEL_EXCLUSION.md` — why the earlier
   architecture was abandoned, so you don't re-propose it.
6. Sections 2.5, 6.5, 7.4-7.6 and 8 of `manuscript.tex` (or `manuscript.pdf`).

Background for the programme as a whole is in
`papers/susy-positivity/background_section.tex`, `PROGRAM_OVERVIEW.md` and
`brainstorm/INVERSE_BULK_AND_DEFECT_DIRECTIONS.md`. The manuscript is
deliberately self-contained and must not depend on them.

The working manuscript is at version 0.5; version 0.4 and earlier are
preserved in `drafts/`. Everything settled so far is folded in, so the notes
and the manuscript agree.

**The task, in order of preference.**

1. *The construction target.* Exhibit the compression. With
   `K_+[f] = K[E_L f] + (c_L)_+ ||f||^2 + 2|<cosh(x/2),f>|^2` as the source side
   — manifestly a norm, explicit source
   `Gf = (b^{1/2}(D)E_L f, (c_L)_+^{1/2} f, sqrt2 <cosh(x/2),f>)`, and the gamma
   part is the field energy of Appendix A — the whole of Weil positivity on
   `I_L` is `T_L <= K_+` for the manifestly positive
   `T_L[f] = (c_L)_- ||f||^2 + 2|<sinh(x/2),f>|^2 + sum_p Bt_p[E_L f]`.
   What a candidate model must now produce is a positive contraction on the
   gamma source's own Hilbert space representing `T_L`. Sphere boundary modules
   and charge-neutral Schur RG/interface preparations are the two standing
   candidate families; any source must be reflection covariant by
   Proposition 2.4. Expect no cheap win: `||Pi||` is saturated, and that is
   unchanged by the reformulation. A clean negative about a named family is as
   useful as a positive.

2. *The compact window `log 2 < L < log 7`*, if the construction stalls. It is
   the range on which `A_L >= 0` is known only from RH. Nothing in the
   construction programme now depends on it. The most promising tool
   is the interior Dirichlet form discarded in Proposition 8.1: for `L <= 3.5`
   it dominates the `1/|x-y|` energy, whose mean-zero spectral gap on an
   interval is scale invariant — one universal constant, computable once, usable
   at every `L`.

**Do not** look for a ghost pair, a BRST doublet or an indefinite-metric sector
for the pole term; do not look for a better additive split of `Q_L`; do not
pursue Connes-Consani for (8.1); do not re-prove (8.1) below `log 2`; do not
test candidates by matching the terms of (2.9) one at a time, and do not credit
a candidate for reproducing a prime weight in a positive sector. Section 4 of
the continuation note and section 0's update give the reasons.

**How to work.** Verify claims numerically before believing them, and tell me
when a numerical result is evidence rather than proof — Galerkin minima in a
subspace are one-sided and certify nothing about positivity. Please push back if
you think the direction is wrong; the last two sessions both ended by
contradicting the handoff that set them up, and that was the useful part. Save
findings as a new dated research note in `notes/`, with "Claude Opus 5" or
whichever model you are named at the top, and add any check programme to
`numerics/` following the existing conventions (standard library only, JSON to
stdout, a preserved record, registered in `CHECKS` when the build record is next
regenerated).

For context on how the previous sessions worked: one reviewed manuscript 0.1
and found that the architecture the investigation was heading toward could not
be completed, replacing it with the subtraction form now in 0.3; the next
settled the prime-free inequality outside a compact window; the last answered
Remark 7.10 affirmatively, found that the pole-sector item it was meant to serve
rested on a false premise, and replaced the construction target with one
compression of the gamma energy. I would like the same standard — check the
algebra independently, say plainly what is proved and what is only numerical,
and prefer a sharp negative result to a vague positive one.
