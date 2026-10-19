# Internal review: S07 observation options and bounded feasibility screens

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6.1-sol (Codex)**,
actual reasoning effort **ultra**, in a separate delegated same-model
reading. This is internal mathematical and code review, not independent
specialist human review. The reviewer wrote only temporary review/replay
artifacts; installation and repository/status changes belong to the author.

## Disposition

**Pass after two scope corrections incorporated before installation.**
The new note proves two additional failures of precisely specified assigned
payment rules. It correctly distinguishes those results from the unexecuted
signed-sampling, mixed-adjoint and winding proposals. S07-T1/T2 remain
Complete, T3 remains Waiting, T4 remains Deferred, and the note creates no
new task ID or activation.

The reviewer read the full Note 05 draft and checker, S07 Notes 03/04,
S03 Notes 03/04/07, and the earlier geometric-options assessment. A fresh
**192-bit** execution passed every assertion; the replay is
[S07_OPTIONS_REVIEW_REPLAY_192_20261019.json](../numerics/S07_OPTIONS_REVIEW_REPLAY_192_20261019.json).
The author must produce the primary and final replay records against the
installed sources. The staged replay pins the existing source notes and
checker it read; it cannot pin a Note 05 not yet installed. Identity hashes
are provenance, not mathematical proof.

## The cutoff-family floor

At either omitted sample n=3 or n=-3, the unit-interval H1 sampling bound
is |g(n)|² <= 2 integral(|g|²+|g_y|²). The minimum of 1+y² on those two
disjoint intervals is 29/4. Summing both intervals therefore gives
Y(g(0,q)) >= (29/4)a_q(3)². The previously proved Hilbert-valued base
trace applies to this same weighted H1 space, so its right side is bounded
by the p integral defining X. Integrating dq/(4q) on [1,65/64] and using
the decreasing a_q(3) gives exactly

    X² >= (29/16) log(65/64) a_(65/64)(3)².

This proof allows a p/q-dependent smooth cutoff with the stated unchanged
physical samples, provided the residual belongs to X. No p-independence
is silently assumed. Direct differentiation verifies the monotonicity:
with w=pi*q*9, q times the logarithmic derivative of a_q(3) equals
9/4+3/[2(w-3/2)]-w, which is negative for q>=1.

The narrow-transition statement also follows directly: on each interval
of length epsilon, its endpoint change costs at least a_q(3)²/epsilon
in the derivative integral. Both intervals and their minimum weight give
the stated 2[1+(3-epsilon)²]/epsilon factor. No assertion of an optimal
cutoff or optimal trace constant follows.

The replay gives assigned-payment ratios above **10.23351659** and
**215.90385680** against the complete direct tails. It therefore supports
the displayed conservative ratios 10.23 and 215.9 for this same
sqrt(20)X/Cauchy rule. This is an assigned-allowance floor, not an
actual-error lower bound or exclusion of another norm or constant.

## The original-cutoff projection/complement floor

For the original even residual h=a_q*rho, odd oscillator coefficients
vanish. On |y|>=2, q>=1, the exact polynomials P2=4v²-1 and
P4=16v⁴-24v²+3 obey the displayed leading-monomial majorants. The
resulting coefficient integrands have q powers 5/2, 7/2 and 9/2 times
exp(-2*pi*q*y²). All three decrease with q>=1 on this domain. Hence
the bounds C0,C2,C4, using the earlier positive Gaussian-moment upper
recurrence at q=1, are valid uniformly.

On the witness rectangle q in [1,17/16], |y| in [9/4,5/2], the common
Gaussian factor and polynomial majorants give the stated uniform B_*.
The replay verifies

    |Pi4 h| <= B_* < 2.30508e-11,
    h >= m > 2.31894e-8,
    m-B_* > 0.

Consequently |h-Pi4 h| >= m-B_*. The p-independent profile basis makes
Pi4 commute with the scalar exp(pi*p²*q); the complement g-Pi4 g is
exp(pi*p²*q)(h-Pi4 h), whose modulus is at least m-B_* throughout the
same p interval. Retaining only the nonnegative 4Y value term, both y
intervals, p width 1/2 and physical dq/(4q) gives exactly
(97/64)log(17/16)(m-B_*)². No unproved estimate of projection derivatives
is used in this lower bound.

The complement's assigned-payment ratios replay above **1617.1754798**
and **34118.7137238**. Adding a nonnegative projected-sector allowance
cannot repair this separate triangle rule. The note correctly leaves a
different complement estimate and signed recombination open. Its exact
projected sampling-kernel identity recombines to the original lattice sum;
the identity alone is correctly not claimed as a gain.

## Earlier coverage, recommendations and controls

The 18 October assessment already proposed constrained evaluation, mixed
adjoints and physical winding. S07-T1 supplies a valid finite fiber space
and a paid profile/base class, but expressly supplies no lift of the
corrected S02/S03 residual. S07-T2 executed only its selected whole-profile
comparison. The two new screens narrow further simple variants without
claiming the unexecuted routes have been tested.

The corrected S03 residual and its existing primitive are appropriate
objects for the proposed representation audit. S03 already provides the
independent arithmetic increment allowance <0.000854, while the separate
source-informed <0.000266448 remains stronger. These information classes
must remain distinct. Boundary winding has an existing theorem/pilot,
but no new matched bottleneck/cost comparison is performed here.

Two review corrections were incorporated: the pre-computation gate now
requires a quantitative gain beyond merely restating the primitive, so it
does not exclude a genuinely sharper estimate of that same primitive;
the warning about separate absolute payments names the specific S03
split-prefix and separate-channel variation rules, avoiding an exclusion
of every possible partial separation. The latter witnesses (>1.912087
and >4037.45136 in one cell) support exactly their recorded rule classes.

No new strict physical acceptance interface is introduced. The inherited
source-specific event and Euler controls are regression screening; the
new continuous floor proofs do not depend on their assertion counts.
These screens claim no physical sign, actual-error floor, cost benefit,
coverage extension, global real bridge or complex exterior result.
