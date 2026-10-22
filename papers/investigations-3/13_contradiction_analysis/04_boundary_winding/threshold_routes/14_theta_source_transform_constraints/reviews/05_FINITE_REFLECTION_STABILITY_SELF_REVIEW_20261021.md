# Project review and finite-reflection stability audit

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. This is the authoring assistant's review,
not independent specialist validation.

Reviewed the program README, overview, progress register, Notes 01–04
and their recorded assessments before deriving [Note 05][note]. The
relevant comparators are the existing modular-cancellation theorem,
complete shifted evaluator, S01 paired-tail estimate, and Investigation
07's already established finite-source measurement controls.

## Project assessment

The earlier results retain their stated scopes. Note 01 constrains a
finite-endpoint relaxation but does not outperform direct canonical
coefficients. Note 02's reflection-adjoint equality is for its pointwise
error class. Note 03 explains why a common quantitative analytic bound
changes that class. Note 04 supplies such a bound for the actual tail
and proves a strict monotone-envelope improvement, without a complete
field sign. This review does not replay their earlier interval records
or upgrade their review status.

The selected continuation uses the head and that same full tail in the
estimating step. Note 05 proves a quantitative finite-reflection
approximation theorem and identifies its accuracy cost. It completes
an analytic stability subtask. It does not complete TST-03 as an
arithmetic collision discriminator or TST-05 as physical exclusion.

## Mathematical audit of Note 05

**Source domain and constant.** On |v|<=R<pi/8,
Re(exp(4v))>=exp(-4R)cos(4R)>0. The complete square-mode sum therefore
converges normally on a neighborhood of the disk. Its geometric
majorant is conditional on the explicitly displayed q_R<1; finite
initial terms can be paid if necessary. Full reflection gives
D_m=-(R_m(v)-R_m(-v)), so the factor two in B_m is necessary.
The tail is not treated as even. Note 04's |p_m|<4 is not extended
past its stated half-plane; the full mode series supplies the larger
analytic domain.

**Connector normalization and sign.** The exact residual is
H-A=P_tail-(C_m-C_(m,M)). The truncated connector starts with
-S_m'(0) integral s*exp(-t*s^2-z*s) ds, and A subtracts that
negative quantity. Thus the inverse-square head term cancels. The
Taylor coefficient in (8) is S_m^(2r+1)/(2r+1)!, not twice it:
the odd defect's factor two cancels the connector's factor one-half.
Heat is kept exact. In particular the inverse-fourth-power term is
S_m'''(0)+6t*S_m'(0), agreeing with the heat-weighted endpoint
expansion.

**Cauchy remainder and shared derivatives.** M odd Taylor terms leave
first possible degree p=2M+1, including M=0. Oddness gives denominator
1-(s/R)^2. Spectral differentiation supplies (-s)^j and no derivatives
of the subsequently chosen contour or cutoff. The covector payment
contains |ell_0-ell_1*s|, preserving the common connector. All finite
segments and unbounded rays are paid; complex heat time costs
exp(T*d^2), and bounded imaginary spectral height is retained in K_j.

**Rate theorem and its restriction.** The upper disk-class allowance
and the monomial lower example differ by a fixed multiplicative factor,
so their exponential rates agree. The saddle is s=c when c<=d and
the endpoint s=d when c>=d. For p=o(x), choosing a fixed arbitrarily
small positive source interval proves the zero exponential rate without
an invalid uniform saddle approximation. The lower example varies the
revealed Taylor data and is not a lower bound for theta's actual defect
with its particular coefficients. This restriction is stated explicitly.

**Moving disk and mode count.** With R=pi/8-a*log(x)/x, the disk
majorant includes exp(-4R); dropping its limiting exp(-pi/2) would
give an incorrect exponent. The complete summation factor 1/(1-q_R)
contributes sqrt(x)/log(x). The Taylor-remainder denominator contributes
x/log(x), and the endpoint Laplace integral contributes another
1/log(x). These give the x^(7/2)/(log x)^3 prefactor in (22).
The integer ceiling in k changes the exponential by 1+o(1).
All checks are eventual, uniformly for bounded T,Y and fixed j;
no effective onset or acquisition conditioning is asserted.

**Precision payment.** A fixed uncertainty in the first odd Taylor
coefficient gives an inverse-square worst-case value allowance. Growing
M alone cannot change that. The accuracy statement concerns independent
absolute-error payments, not all correlated or adaptively acquired data.

## Exact checks and limitations

The standard-library [checker][checker] compares the formal Taylor
series of each source mode against an independently implemented
repeated-derivative recurrence, using exact rational polynomial
coefficients through order nine. It also compares the connector's
heat and spectral derivative signs with the cosine endpoint expansion,
and checks the conservative exponent arithmetic for the displayed
near-boundary schedule. The [receipt][receipt] records the actual
runtime and script hash.

These checks passed. They check transcription and normalization; they
are not a theta numerical experiment, an interval certificate, a proof
of the analytic quantifiers, or independent review. No new theta
values, zero boxes, event witnesses, or coverage were acquired.

## Comparison, controls and decision

For the same retained head and contour, the exact shifted approximant
already removes C_m. Finite Taylor subtraction only adds the nonnegative
allowance F to the common tail payment. Replacing that common payment
by S01's stronger bound does not change the comparison. The result is
a quantitative rate for finite reflection data, not an evaluator win.

The finite-prime controls can preserve any fixed endpoint list, but the
complete reflection defect C_A in Note 05 (26) is not zero for those
controls. That is the missing premise here. Reflected controls lack
the canonical square-tail bound; they also demonstrate that accurate
approximation and full reflection alone do not preclude a collision.
The disk monomial used to prove the class-level rate is not presented
as a physical collision control. No preservation lists are combined.

**Disposition: retain as proved in-note, with same-assistant review.**
Update the project status and archive this chat. The next substantive
sign question is the complete shifted arithmetic jet, conditioned on
the simultaneous head–tail matching equations. More finite connector
terms or a smaller tail allowance alone do not establish that sign.
The original arithmetic discriminator and physical exclusion remain
open. There is no manuscript milestone or investigation closure to
promote into the repository-wide result summaries.

[note]: ../notes/05_FINITE_REFLECTION_JETS_AND_HEAD_TAIL_STABILITY_20261021.md
[checker]: ../numerics/check_finite_reflection_algebra.py
[receipt]: ../numerics/FINITE_REFLECTION_ALGEBRA_20261021.json
