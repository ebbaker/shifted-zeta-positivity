# Self-review of the BW-08 imaginary-axis bound

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing and authoring model:
**gpt-6-astra (Codex)**; actual reasoning effort **max**.
This is a same-assistant self-review, not independent implementation,
cross-model assessment or specialist review.

**Assessment: accept the restricted necessary-condition estimate and its
finite-time transfer. No collision exclusion or winding certificate is
accepted.** The source is [Note 03][note], SHA-256
`722d8edf4d88af75daa921ef4931b598c7be5ee7c82134b6124d1a54149bc0a2`,
over Git parent `b39c6cc9b4756bc14c2e500e327169db88571d1f` with
uncommitted research additions. The [contract][contract] predates the
exact runs; the [record][record] hashes the contract, note, checker and
reused sources. Source identity does not constitute a mathematical review.

## Mathematical audit

1. **The zero-sum subtraction is correct.** The two positive roots at a
   contribute 2/a^2 to D_T(a)/a, whereas the two unremoved roots at -a
   contribute 1/(2a^2) to S_a. Thus the subtraction is 3/(2a^2).
   Every other paired-root difference is positive. Order one rules out a
   quadratic exponential term; evenness removes the linear prefactor.
   The exact-double and all-real assumptions are used here, not inferred.

2. **The positive-source argument is not a hidden RH assumption.**
   D_T(b) is an expectation of u*tanh(bu), and its time derivative is
   the covariance with u^2. Both increase on u>=0. The complete source
   gives convergence for all finite real T,b. Monotonicity requires no
   statement about real zeros at time zero.

3. **The explicit lower bound has the right normalization and full tail.**
   H(0,ib)=xi((1+b)/2)/8 gives the factor 1/2 in the logarithmic
   derivative. The digamma lower bound cancels the 1/sigma term.
   The decreasing-integrand bound for the entire von Mangoldt series is
   valid for sigma>=3. Its correction is strictly less than
   1/(sigma-1), since (sigma+2)2^(-sigma)<=5/8. The analytic comparison
   at a=20 and monotonicity prove improvement for all a>=20.

4. **The physical observation has a paid positive time range.**
   The rectangle inequalities keep Hxx away from zero and force Hx
   to cross each spatial interval exactly once. The critical points
   lie on the selected time faces. Direct differentiation gives
   V'''=-H6+3H3H5/H2-3H3^2H4/H2^2+H3^4/H2^3; the displayed K
   bounds its absolute value after normalization. Two Taylor remainders
   cost K*s^3/3. The cap 3C/(2K) leaves a strict negative pair.
   This observation covers two selected points, not a whole contour.

5. **The numerical interface is scoped to what was actually done.**
   No theta quadrature was performed. Exact complete moments justify the
   analytic constants; the inherited N=4,U=1 budget is offered only for
   b<1. The product error through order four includes both cross terms
   and square errors. Parameter errors need moments through order six.
   A nonzero lower bound for h2 is explicitly required for a numerical
   radius. A future boundary acquisition still owes position and value
   errors; the note does not claim to have acquired it.

## Verification and controls

The standard-library checker passed four exact polynomial cases and the
finite-time quartic check. Polynomial coefficients and root sums give
the same S and D; substitution into the finite heat flow reproduces the
second and third critical-value derivatives. Negative multiplication
preserves the normalized algebra. Four hypothetical-height coefficient
enclosures use rational series and outward rounding; at a=1000 the new
deflated bound divided by the mirror bound exceeds 2185.86526617.
This ratio measures that coefficient only.

The quartic at a=20 fails the scalar floor, but the degree-eight
all-real slice has a double event and passes it. More decisively for
the source screen, Euler-factor controls have
D_0^(c,p)=D_0+c*alpha*sinh(alpha*b)/(1+c*cosh(alpha*b))>D_0;
positivity propagates their floor to T>=0. They fail the literal xi
identity but not the derived lower bound. This prevents a claim of
universal control separation. Other families are screened against
their actual source, product and all-real premises, without numerical
events invented for existence constructions.

## Accepted scope and remaining obligation

The result is an explicit strengthening of a necessary fourth-jet bound
for T>0, a>=20 and multiplicity exactly two, together with a finite
BW-01 time-face transfer. It does not use threshold minimality beyond
the all-real slice. It does not cover higher multiplicities, prove
zero winding, acquire a new theta region, improve Lambda, or establish
an evaluation-cost advantage. Event-dependent constants are permitted;
no uniform measured radius is available.

Record BW-08's first bounded task as complete in this restricted sense.
Continue only with a specified opposing estimate (an upper bound on Q_L
or a lower bound on the face pair), or a different information source;
reproducing the necessary bound is not a next
exclusion task. The [shared progress register][progress] should keep
the incompatible sign, global coverage and multiplicity obligations open.

[note]: ../notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md
[contract]: ../notes/02_IMAGINARY_AXIS_CONTRACT_20261019.md
[record]: ../numerics/IMAGINARY_AXIS_CONTROLS_20261019.json
[progress]: ../../../research-progress/01_THRESHOLD_BOUNDARY_WINDING_PROGRESS_20261019.md
