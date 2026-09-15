I am continuing work on the inverse-bulk realization investigation in my
shifted-zeta-positivity repository, at
`papers/susy-positivity/investigations/inverse-bulk-realization`.

Start by reading, in this order:

1. `notes/CONTINUATION_20260915.md` — the handoff note; it states where things
   stand and what to do next.
2. `notes/MIRROR_REFERENCE_AND_SUBTRACTION_FORM.md` — the current direction.
3. `notes/INTERFERENCE_BOUND_AND_TWO_CHANNEL_EXCLUSION.md` — why the previous
   architecture was abandoned, so you don't re-propose it.
4. Section 7.5 and Section 8 of `manuscript.tex` (or `manuscript.pdf`), which
   are where those results now live.

Background for the programme as a whole is in
`papers/susy-positivity/background_section.tex`, `PROGRAM_OVERVIEW.md` and
`brainstorm/INVERSE_BULK_AND_DEFECT_DIRECTIONS.md`. The manuscript is
deliberately self-contained and must not depend on them.

**The task.** Work on item 1 of section 3 of the continuation note: prove, or
determine the obstruction to, the prime-free archimedean inequality

  K[E_L f] + (w0 + sum_{p < e^L} kappa-tilde_p) ||f||^2 + P_L[f] >= 0,

where K is the gamma energy, P_L the rank-two pole form, w0 = psi(1/4) - log pi,
and kappa-tilde_p = 2 (log p) p^{-1/2} / (1 + p^{-1/2}). Begin with L <= log 2,
where no primes are active and the statement reduces to
K + w0 ||f||^2 + P_L >= 0. Look hard at whether the compressed-scaling-action
argument of Connes and Consani (arXiv:2006.13771) gives it with the constant we
need; that paper obtains archimedean Weil positivity from the trace of a scaling
action compressed to the orthogonal complement of cutoff projections, which is
the same mechanism we need here.

If that stalls, switch to item 2: whether the elementary q-Weyl representation
can produce the mirror weight (Remark 7.10 of the manuscript). A clean negative
answer is as useful as a positive one.

**How to work.** Verify claims numerically before believing them, and tell me
when a numerical result is evidence rather than proof. Please push back if you
think the direction is wrong. Do not modify the manuscript yet — save findings
as a new dated research note in `notes/`, with "Claude Opus 5" or whichever
model you are named at the top, and add any check programme to `numerics/`
following the existing conventions (standard library only, JSON to stdout, a
preserved record, registered in the CHECKS dictionary of
`validation/drafts.py`). We will fold results into the manuscript once they
settle.

For context on how the previous session worked: it reviewed manuscript 0.1,
found that the architecture the investigation was heading toward could not be
completed, and replaced it with the subtraction form now in 0.3. I would like
the same standard — check the algebra independently, say plainly what is proved
and what is only numerical, and prefer a sharp negative result to a vague
positive one.
