# Local bounds for the height adapted detector

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: elementary detector deductions and internal same-model review.
No arithmetic saving or zero-free region is proved.

Use the family in the [overview](README.md), with its transform and exact
norm from [assessment equations (16)--(22)](../programs/01_signed_arithmetic_covariance/NATURAL_BOUND_ASSESSMENT_20261004.md).
These two lemmas sharpen the starting point for a local converse. They
bound a coefficient function; they do not prevent cancellation in the
full zero sum.

## Decay away from the carrier

For every real t0 and every s=beta+i gamma with 0<=beta<=1,

\[
|D_{t_0}(s)|\ll_h
\left(\frac{1+|\gamma|}{1+|t_0|}\right)^3
(1+|\gamma-t_0|)^{-10}.                                    \tag{1}
\]

The constant depends only on the fixed base probe.

Indeed, the compact extension of h has ninth distributional derivative
a finite measure, giving
|H(sigma+i u)|<=C_h(1+|u|)^(-9) uniformly for |sigma|<=1/2.
The exact norm polynomial gives N_t0>=c_h(1+|t0|)^3.
The polynomial z(z^2-1/4), with z=1/2-s, is at most
C(1+|gamma|)^3. Finally

\[
\left|\frac{2^{s+2-it_0}-1}{s+2-it_0}\right|
\ll(1+|\gamma-t_0|)^{-1}.
\]

Multiplying these bounds proves (1). Near gamma=t0 the estimate is of
order one. Far from the carrier it includes both the frequency separation
and the polynomial numerator, rather than treating all heights as if they
were central.

This is a useful input for a parameter-dependent classical comparison and
remote-zero tails. It is not yet such a comparison with all sums and
thresholds evaluated.

## A lower bound on a whole height rectangle

For |t0|>=100,

\[
\boxed{|D_{t_0}(\beta+i\gamma)|>\frac14
\quad\text{if }3/4\le\beta\le1,\quad|\gamma-t_0|\le1.}          \tag{2}
\]

Thus the detector is boundedly invertible on this rectangle. The stronger
central bound >0.36 is already recorded in the assessment.

To prove (2), put nu=gamma-t0 and I0=integral h.
Since |v|<=1/4 and |nu|<=1,

\[
\operatorname{Re}H(1/2-\beta-i\nu)
\ge\frac{31}{32}H(1/2-\beta)\ge\frac{31}{32}I_0.
\]

Here cos(nu v)>=1-(nu v)^2/2>=31/32, and evenness and positivity
of h give H(real)>=I0. Also

\[
K(\beta+i\nu)=\int_1^2y^{\beta+1}e^{i\nu\log y}\,dy,\qquad
\operatorname{Re}K(\beta+i\nu)>\frac34K(\beta),
\]

because log 2<0.7 and cos 0.7>=1-0.7^2/2>3/4.
The polynomial numerator has modulus at least |gamma|^3,
which is at least (0.99|t0|)^3.

The assessment's exact integration bounds give
I0/||h||_2>0.455, N_t0/(|t0|^3||h||_2)<1.11, and
K(beta)/q>0.89 for beta>=3/4. Consequently the lower bound is

\[
\frac{0.455\cdot0.89}{1.11}\,
\frac{31}{32}\,\frac34\,(0.99)^3
=\frac{243611999631}{947200000000}>\frac14.
\]

The estimates use only exact rational inequalities. For example,
exp(0.7)>2 follows from its degree-four positive Taylor sum, so the
bound on log 2 needs no floating approximation.

## What local inversion does and does not provide

Equation (2) permits division by D_t0 with reciprocal at most four on
the stated rectangle. The prepared transform has factor
-D_t0(s) zeta'(s)/zeta(s), so division by -D_t0 restores the
logarithmic derivative with positive multiplicity residues. Investigating
this inverse multiplier in a localized Mellin or Gaussian test may
simplify a power-sum argument.
That is a proposed use of the lemma.

A complete inverse-test proof still needs bounds off the rectangle,
physical convolution tails, the finite initial cap, and preparation zeros.
In particular D_t0(1)=0. Dividing the prepared transform restores the
pole at one, whose contribution must be handled explicitly. A global
quotient is not justified by the local reciprocal bound.
If inverse-test norms and remote-zero costs erase the central coefficient
gain, this route has not improved the detection budget.

The rectangle concerns the carrier used for one local test. An
exposed-zero argument may replace a zero by one outside the original
narrow height band. Such a proof must enlarge the covered band by a
computable amount, or prove a genuinely local replacement statement.
It cannot assume the replacement remains within the unit rectangle.

## Verification

The transform identity and norm are inherited from the assessment.
The upper decay estimate follows from finite-measure derivatives and
elementary bounds. Two same-model analyses checked the lower-bound
factors and the exact rational product. These checks establish the
displayed coefficient lemmas, not a finite certificate for zeta.
