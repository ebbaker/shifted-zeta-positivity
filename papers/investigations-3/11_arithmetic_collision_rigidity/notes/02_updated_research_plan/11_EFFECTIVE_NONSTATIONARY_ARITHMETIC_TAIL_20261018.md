# An effective nonstationary arithmetic tail on near-boundary contours

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual reasoning
effort ultra**, verified from the current execution metadata. Derivation,
implementation and parallel checks are same-model internal work; no
independent specialist review is claimed.

This continues [overview 02][plan] after the bounded pilot's failed
performance gate and the unclosed global consumer in [Note 10][global].
The [result-summary index][summaries] and [patterns-to-avoid index][avoid]
govern its classification, particularly [target classification][target],
[collision controls][controls] and [preserving cancellation][pairing].

**New analytic result.** Oscillation in the omitted square modes improves
the manuscript's arithmetic tail by a factor of order `log(x)/x` along its
near-boundary family. The improved envelope-relative tail tends to zero
for every `a>0, b*>1/(4*pi)`; the earlier additional condition
`a*(4*pi*b*-1)>3/4` is unnecessary for this improved estimate. An explicit
uniform example and a bounded retained-integral cost measurement are given
below. This is an approximation estimate, not an RH-equivalent criterion
or a complete-field lower bound.

## 1. Frozen-contour theorem

Use the manuscript's complete reflected-source representation and its
approximation `Htilde_{m,d}`; complete reflection precedes truncation. Let
`0<d<pi/8`, `T,Y>=0`, `m>=1` be an integer, and write

\[
 c=\cos(4d),\quad s=\sin(4d),\quad \lambda_n=\pi n^2,\quad
 B=4c\lambda_m-9-Y,\quad P=4s\lambda_m-x-2Td.
\]

Assume `B>0`, `8c*lambda_m>=T`, and `P>0`. For an integer `j>=0`, set

\[
 Q_j=\sum_{k=0}^j {j\choose k}\frac{d^{j-k}k!}{B^k},\qquad
 S=\sum_{n=m}^{\infty}(2\lambda_n^2+3\lambda_n)e^{-c\lambda_n}.
\]

For `0<=t<=T`, `z=x+iy`, `|y|<=Y`, the new bound is

\[
 \boxed{\left|\partial_z^j(H-\widetilde H_{m,d})(t,z)\right|
       \le e^{-dx}\frac{2S}{P}Q_j.} \tag{1}
\]

All derivatives freeze `m,d`. If the manuscript's geometric-ratio
condition also holds, its old bound is `e^{-dx} S_geo Q_j/B`, and the new
bound with the same `S_geo` has ratio exactly `2B/P` to that bound.
The minimum of the two is valid. A failed `P>0` condition rejects the
nonstationary estimate; it does not reject the original absolute estimate.

**Proof.** On the upper shifted half-line separate each mode into its
degree-nine and degree-five exponentials, with constant coefficients
`2*lambda_n^2` and `-3*lambda_n`. Including `e^{t(u+id)^2}` and the
complex spectral factor, their positive amplitudes, apart from those
coefficients and `e^{-dx}`, are

\[
 g(u)=\exp\{t(u^2-d^2)+(r-y)u-c\lambda_ne^{4u}\},
 \qquad r\in\{9,5\}.
\]

Their phases have derivative
`theta'(u)=x+2td-4s*lambda_n*e^{4u}=-p(u)`.
Thus `p(u)>=P>0` and `p'(u)>0`. Moreover

\[
 (\log g)''=2t-16c\lambda_ne^{4u}\le0,\qquad
 (\log g)'(0)\le-B.
\]

Consequently `g` decreases and `g(u)<=g(0)e^{-Bu}`. For derivative `j`,
the complex polynomial factor is `(-d+iu)^j`, whose magnitude is at most
`(u+d)^j` and whose derivative has magnitude at most
`j(u+d)^{j-1}`. Integrating once by parts against `e^{i theta}` bounds
the integral by

\[
 \frac{g(0)d^j}{p(0)}+
 \int_0^\infty\left\{
 \frac{(-g')(u+d)^j+jg(u+d)^{j-1}}p
 +\frac{g(u+d)^j p'}{p^2}\right\}\,du.
\]

The terms containing `j` vanish when `j=0`. With
`h=g(u+d)^j`, the integrand equals
`-(h/p)' + 2j*g(u+d)^{j-1}/p`. This identity does not require `h`
to decrease. The remote boundary vanishes, so the displayed bound is at
most

\[
 \frac{2g(0)}{p(0)}\left[d^j+
 j\int_0^\infty (u+d)^{j-1}e^{-Bu}\,du\right]
 =\frac{2g(0)}{p(0)}Q_j.
\]

The lower half-line replaces `y` by `-y`, reverses the phase, and has
polynomial factor `(-d-iu)^j`; the same proof applies. Since
`g(0)=e^{-td^2-c*lambda_n}<=e^{-c*lambda_n}`, summing both source
monomials and both half-lines, with their factor `1/2`, proves (1).
All boundary limits and exchanges are justified by the original
superexponential integrable majorants. No stationary-phase approximation
or discarded vertical segment is used.

## 2. Gaussian summation and an explicit uniform onset

The following version avoids a geometric ratio near one. Put `p=pi*c`,
`q=p*m^2`, and suppose `q>=1`. If `eta>0` satisfies

\[
 4\pi s n^2-x-2Td\ge\eta n^2\qquad(n\ge m),
\]

the same proof, retaining the denominator for each mode, gives

\[
 |\partial_z^j(H-\widetilde H)|
 \le e^{-dx}Q_j\frac{e^{-q}}\eta
 \left[4\pi^2\left(m^2+\frac m{2p}+\frac1{4p^2m}\right)
       +6\pi\left(1+\frac1{2pm}\right)\right]. \tag{2}
\]

Indeed, `u^2 exp(-p*u^2)` is decreasing for `u>=m` when `q>=1`.
Bounding its discrete tail by its first term plus its integral, integrating
that integral once by parts, and using
`int_m^infinity exp(-p*u^2)du <= exp(-q)/(2pm)` gives the first bracket.
The same first-term-plus-integral argument gives the second bracket.
Thus (2) estimates an infinite tail, not a finite truncation of that tail.

Choose, at each observation point,

\[
 d(x)=\pi/8-a\log(x)/x,\qquad
 m(x)=\lceil\sqrt{b_*x}\rceil,\qquad
 G_0(x)=x^{7/4}e^{-\pi x/8}.
\]

These remain frozen when taking spectral derivatives. For an explicit
onset `X>=e^2`, define `L=log X`,

\[
 v=4aL/X,\quad \kappa=1-v^2/6,\quad \sigma=1-v^2/2,\quad
 M=1+(b_*X)^{-1/2},\quad \alpha=4\pi a\kappa b_*,
\]
\[
 \eta=4\pi\sigma-1/b_*-T\pi/(4b_*X).
\]

Require `v<pi/2`, `kappa>0`, `eta>0`,
`q_*:=4*pi*a*kappa*b_*L>=1`, `8q_*>=T`, and
`B_*:=4q_*-9-Y>0`. If

\[
 \pi/8+1/B_*<1,\qquad
 (\pi/8)^2+\pi/(4B_*)+2/B_*^2<1,
\]

then `Q_j<=1` for `j=0,1,2` throughout `x>=X`. Taylor inequalities
`sin v>=v-v^3/6` and `cos v>=1-v^2/2`, and monotonic decrease of
`log x/x` for `x>=X`, imply

\[
 p\ge4\pi a\kappa\log x/x,\quad q\ge\alpha\log x,
 \quad \sqrt{b_*x}\le m\le M\sqrt{b_*x}.
\]

Also `x<=n^2/b_*` and `2Td<=T*pi/4`, so the required phase
denominator is at least `eta*n^2`. Substituting these inequalities in
(2) gives the uniform explicit bound

\[
 \boxed{\frac{|\partial_z^j(H-\widetilde H_{m(x),d(x)})|}{G_0(x)}
 \le C_X\frac{x^{a-1/4-\alpha}}{\log x},\quad j=0,1,2,\ x\ge X,} \tag{3}
\]

where

\[
\begin{split}
 C_X={}&\frac{4\pi^2M^2b_*L}{\eta\sqrt X}
 +\frac{\pi M\sqrt{b_*}}{2\eta a\kappa}
 +\frac1{16\eta a^2\kappa^2\sqrt{b_*}L}\\
 &+\frac{6\pi L}{\eta X^{3/2}}
 +\frac3{4\eta a\kappa\sqrt{b_*}X}.
\end{split}
\]

The quantities `log x/sqrt x`, `log x/x^(3/2)` and `1/x` decrease
on this range, which justifies each substitution by its value at `X`.
If `a-1/4-alpha<0`, the right side of (3) decreases too.
The [scalar certificate][scalar] evaluates these sufficient conditions
with outward Arb arithmetic; the proof establishes the entire unbounded
range rather than extrapolating a table of heights.

For `a=4`, `T=1/2`, `Y=1`, the 192-bit scalar replay gives:

| b* | Uniform onset X | C_X (rounded upward) | Power a-1/4-alpha | Uniform error / G0 for j=0,1,2 |
| --- | --- | --- | --- | --- |
| 1/8 | 1000 | 0.320352 | approximately -2.52039318 | below 2e-9 |
| 1/10 | 20000 | 0.162628 | approximately -1.27649565 | below 6e-8 |
| 1/10 | 100000 | 0.106429 | approximately -1.27654540 | below 4e-9 |

For the first row, the unrounded onset bound is below
`1.273826e-9`, `eta>4.4864`, `B_*>163.25`, `Q1<0.399` and
`Q2<0.160`. These bounds hold uniformly for `0<=t<=1/2`, `|Im z|<=1`
and all `x>=X`; the enclosures and exact parameters are in the record.
The rounded C_X and approximate exponent in the table are descriptive;
only the outward interval expression in the record is consumed.

For comparison the Gaussian-summed *absolute* estimate follows from
`B_n>=delta*p*n^2`, where `delta=4-(9+Y)/q_*>0`. Its uniform envelope
has constant `C_abs=C_X*eta/(8*pi*a*kappa*delta)`, power
`a+3/4-alpha`, and denominator `(log x)^2`. This gives bounds below
`2.188e-9`, `7.206e-7`, and `2.219e-7` for the same three rows.
Thus even the weaker absolute estimate can be made effective; the phase
estimate supplies the better decay exponent.

Asymptotically, the same bounds with their actual varying constants give

\[
 \frac{|\partial_z^j(H-\widetilde H)|}{G_0(x)}
 =O\!\left(\frac{x^{-1/4+a(1-4\pi b_*)}}{\log x}\right)
\]

for every fixed `j`. To justify the precise exponent, use
`p~4*pi*a*log(x)/x`,
`p*m^2=4*pi*a*b_*log(x)+o(1)` and a phase coefficient bounded
away from zero. The Gaussian bracket in (2) is
`O(x^(3/2)/log(x))`, while `Q_j=O(1)`. The `o(1)` in the exponential
uses `m^2=b_*x+O(sqrt(x))` and the sine remainder
`O((log(x)/x)^3)`; a fixed `kappa<1` alone would not justify the precise
asymptotic exponent. The exponent is negative whenever
`a>0` and `b_*>1/(4*pi)`. This improves the previous bound by
`log x/x`; it says nothing about a lower bound on the complete field.

## 3. Retained integrals: bounded measurement and full errors

The separate [point evaluator][evalcode] and [execution record][evalrecord]
measure the retained integral at `t=1/10`, heights `1000` and `10000`,
`j=0,1,2`, with `a=4`, **`b_*=1/4`**, `U=2` and 160-bit Arb/Acb.
This conservative mode choice is different from the uniform example in
Section 2. The declared target was total error below `1e-8*G0` per
component, with a 30-second/200000-callback limit per three-component
case. At height 1000 a second frozen contour `d-1/x` supplies a replay.
No further heights or parameter search were run.

After dividing by `G0`, the integrand uses the exact algebraic factor
`exp((pi/8-d)x)/x^(7/4)=x^(9/4)*exp(offset)` and retains all source
modes in the integrand before integration. The real part is the exact
conjugate pairing for real `t,x`; the imaginary part is retained in the
record as a diagnostic, not treated as a physical component. In particular
its large size near height 1000 is paid for by outward quadrature rather
than ignored. The derivative factors are `(i(u+id))^j`, with all
parameters and the comparison envelope frozen.

Each returned enclosure contains the full physical derivative divided by
`G0`. Its error comprises the quadrature's outward radius, the original
manuscript arithmetic-mode tail, and the retained-source tail beyond `U`.
For the latter the checker verifies, for each retained mode,

\[
 D_{n,j}=4c\lambda_ne^{4U}-9-2TU-j/(U+d)>0,
 \quad16c\lambda_ne^{4U}>2T,
\]

and pays the concave-tangent bound

\[
 e^{-dx}\sum_{n<m}\frac{(2\lambda_n^2+3\lambda_n)(U+d)^j
       e^{TU^2+9U-c\lambda_ne^{4U}}}{D_{n,j}}.
\]

All arithmetic in the integral and these payments is outward. The new
nonstationary estimate is also printed as a diagnostic; the point
certificate conservatively consumes the older proven mode bound. There
is no whole-cell propagation: these are point enclosures only.

| Height and contour | Retained modes | Three-component time | Callbacks | Largest total error / G0 |
| --- | --- | --- | --- | --- |
| 1000, d | 15 | about 0.581 s | 10277 | below 2.527e-12 |
| 1000, d-1/x | 15 | about 0.568 s | 10145 | below 2.708e-12 |
| 10000, d | 49 | about 14.37 s | 83022 | below 3.737e-11 |

All components pass, and both height-1000 contour enclosures intersect
for every derivative. Quadrature dominates; the mode and source tails
are explicitly included in the record. These are measured finite costs,
not a complexity law or a matched speed comparison. They do not reopen
Stage 2's failed performance gate or close Stage 4's finite bridge.

## 4. Control screen, status and next mathematical input

The control catalogue is applied to the premises rather than to small
decimals. Finite-prime orbit and weighted-square controls fail the complete
normalized analytic reflection used before the shift; omitted seam terms
prevent using this representation for them. Reflected super-Gaussian,
smooth-shape, positive-primitive, Euler-factor, `q` and `q_{T,a}` controls
fail the unchanged normalized theta square-source expansion, its phase
`lambda_n=pi*n^2`, or both. Smooth-density and two-channel classes have
neither this complete source contract nor a resulting physical signed
estimate. No conclusion is extended to those classes.

A [fresh control replay][controlrecord] re-executes the published
three-square, four-square, reflected-source and Euler-factor checkers,
then applies the existing source-specific interface to all five
surrounding event boxes (including the polynomial and `q_{T,a}` events).
All five reject strict first-jet and signed margins; the Euler-factor
negative-Laguerre witness separately rejects the signed gate. These are
failure-interface checks inherited from the pilot, not numerical evidence
for the new unbounded-range theorem. The scalar checker also rejects
actual frozen-contour parameters with nonpositive phase gap, insufficient
amplitude decay, zero shift or boundary shift, and compares its direct
Gaussian bound with (3) at the declared onset and two nearby heights.

Status: (1)–(3) are **proved in-note**, with scalar interval certificates
and parallel same-model proof checks; the retained-integral examples are
**interval-certified point evaluations**, subject to their analytic error
contract and interval implementation. [Review 10][review] records precise
checks and source identities. A global positive jet margin, an effective outer
nonvanishing theorem, and a feasible complete global bridge remain open.
Next work should consume this tail in a signed estimate or justify a
better retained-integral strategy by a bounded comparison; merely reducing
this already subdominant tail does not close the physical margin.

[plan]: ../../research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md
[global]: 10_GLOBAL_CONSUMER_AND_COVERAGE_LEDGER_20261018.md
[summaries]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[target]: ../../../../../avoid/01_restating_the_target.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[pairing]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scalar]: ../../numerics/EFFECTIVE_NONSTATIONARY_TAIL_20261018.json
[evalcode]: ../../numerics/bounded_near_boundary_evaluator.py
[evalrecord]: ../../numerics/NEAR_BOUNDARY_POINT_EVALUATION_20261018.json
[review]: ../../reviews/10_EFFECTIVE_NONSTATIONARY_TAIL_AND_POINT_EVALUATOR_REVIEW_20261018.md

[controlrecord]: ../../numerics/NONSTATIONARY_CONTROL_REPLAY_20261018.json
