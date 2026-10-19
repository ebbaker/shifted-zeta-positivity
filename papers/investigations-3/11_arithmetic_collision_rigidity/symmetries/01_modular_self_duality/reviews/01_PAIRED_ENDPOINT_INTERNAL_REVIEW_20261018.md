# Internal review of the S01 opening comparison

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual reasoning
effort ultra**, verified from the parent turn metadata. Two parallel
same-model readers checked the mathematics and controls. This is internal
LLM review, not independent specialist review.

**Assessment: the bounded complete-error gate passes.** The
[research note][note] proves a paired-endpoint remainder estimate for the
same finite shifted theta approximation as the existing evaluator. The
[192-bit comparison][record] and [256-bit fresh replay][replay] strictly
reduce its complete added errors for orders 0, 1 and 2 on
`[1/100,1/5] x [999,1001]`. The mode-error estimates also hold throughout
the fixed spectral neighborhood `|Im z|<=1`. No complete complex-wall
comparison, new signed lower bound or new exclusion region is claimed.

The [program guide][guide] is suitable for this start. Although its default
quantitative priority is S02, it explicitly assigns S01 a bounded paired
remainder task and permits a different selected mechanism. The user's
request selects S01. The [result-summary index][summaries] and [avoid
index][avoid] were reviewed; the relevant screens are [collision controls][controls],
[reformulations][target], [scoped conclusions][scope] and [signed pairing][pairing].

## Mathematical checks

- The complete modular reflection precedes arithmetic truncation. A
  finite source is never treated as reflection invariant; its vertical
  boundary in the general half-line contour identity is explicit.
- Both phases and derivative factors `(-d +/- iu)^j` are retained.
  Their source-zero endpoints pair to a sine even when the spectral
  variable is complex. No real-part substitution is made off the axis.
- Positive phase gaps, amplitude monotonicity, log-concavity and remote
  boundary decay justify integration by parts. The remainder coefficient
  is `2 Q_j-d^j`, rather than an unpaid second endpoint payment.
- Signed endpoints are summed before taking one absolute value. The
  infinite arithmetic remainder after n=23 is bounded by a geometric
  series derived from the positive mass; it is not silently truncated.
- The comparison with the stronger modewise baseline retains common
  heat damping and individual denominators. The pairing saving is
  distinguished from those independent refinements.
- The physical-to-fixed-normalizer factor is exactly
  `1000^(9/4) exp(d-tau d^2)`. No height-dependent normalizer is
  differentiated. Mode and contour cutoffs remain frozen.
- The full evaluator comparisons share the exact midpoint polynomial,
  quadrature radii, source tail, whole-box Taylor error and subsequent
  image rounding. Thus the improvement is not merely a smaller isolated
  mode allowance compared with an unpaid calculation.

One draft typo was found and corrected: `B>190.59` applied to Y=0, while
the stated complex neighborhood Y=1 requires `B>189.59`. The exact
outward values in both records are correct.

## Replays and scope

The small checker independently repeats tail constants at 192/256 bits,
and the separate full replay repeats quadrature at 256 bits with its own
unchanged common costs. The rational endpoint allowance 29/125 is checked
at both precisions; separately rounded endpoint upper endpoints are not
claimed to be identical mathematical numbers.

The non-even source fixture checks the compulsory vertical segment through
two spectral derivatives at a complex point. Five invalid parameter cases
are rejected. The [fresh source-specific control replay][control-record]
rejects five event boxes and the separate Euler negative-Laguerre witness.
The controls use their own errors; they do not certify the analytic theorem.

Finite-prime and finite weighted-square controls lack complete reflection.
Reflected smooth and super-Gaussian controls retain reflection but lack the
unchanged theta arithmetic data; Euler-factor sources alter those data.
The improvement itself can have analogues for other sources and therefore
does not establish arithmetic collision rigidity. The low retained modes
can be stationary and fall outside this tail argument.

The paid error decreases by about 14.8%, 7.2% and 3.0% in the primary
complete comparison. The manuscript, its finite certificates, the real
gap `(1001,exp(2000))` on the stated time slab and the missing global
complex exterior retain their prior status. No performance milestone is
claimed from the setup timings. Continue with a bounded S02/S03 use of
the smaller error; re-evaluate the endpoint allowance on every new domain.

The adjacent [file identity manifest][manifest] records hashes and sizes
of this opening round's mathematical note, code, small evidence records
and numerical guide. It identifies bytes; it does not certify mathematics.

[note]: ../notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md
[record]: ../numerics/PAIRED_MODULAR_TAIL_20261018.json
[replay]: ../numerics/PAIRED_MODULAR_TAIL_REPLAY_256_20261018.json
[control-record]: ../numerics/S01_MODULAR_CONTROLS_20261018.json
[manifest]: S01_OPENING_FILE_IDENTITIES_20261018.json
[guide]: ../../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[target]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[pairing]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
