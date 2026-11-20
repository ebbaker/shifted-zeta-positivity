# Two approximations, two limits, and the role of K(T)

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. The captured source for this chat supplies no
per-turn model or reasoning-effort configuration. [Public discussion](../../chat-histories/0004_2026-11-20T18-21-26Z_explain-zero-approximation-cutoff.json).

Status: explanatory synthesis of the existing formulas and their stated
domains. No new estimate, criterion, computation, or research milestone.
This supplements [Note 08](08_EZ_WHY_THE_INVERSE_HAS_A_CUTOFF_20261120.md)
and the previous conversation linked there. Portfolio routing:
[result summaries](../../../../../../result-summaries/README.md), especially
the [explicit-position entries in cluster 18](../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
and [patterns](../../../../../../avoid/README.md), especially
[classification](../../../../../../avoid/01_restating_the_target.md),
[scope](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
and [the structural question before numerics](../../../../../../avoid/10_numerics_ahead_of_the_question.md).

## The expansion is centered at the origin

The series Y(q) is built at q=0, corresponding to x=0. K(T) is introduced
afterward by the error and counting proof. It is a rank, not a physical
height; the corresponding height is x_{K(T)}(T). The coefficients of Y
come from the heated source and do not depend on a selected cutoff K.

Three different objects must remain separate: the exact local inverse Y,
an approximation to Y such as its cubic resummation Y_3, and a sufficient
range on which both the zero labels and approximation errors are proved.
K(T) describes the third object. It is neither an identified singularity
of Y nor an observed turning point in the error of Y_3.
[Counted inverse](../../manuscript/anchors.tex) ·
[Range and errors, Note 11 §3](../../notes/11_EZ_GROWING_INVERSE_WINDOW_20261120.md).

## Why increasing heat time helps the inverse approximation

**Coordinate clarification, 20 November 2026.** The mound is a description
of the source density as a function of the integration variable u:
\[
 \rho_T(u)=\frac{e^{Tu^2}\Phi(u)}{H_T(0)},\qquad u\ge0,
 \qquad a=\int_0^\infty u\rho_T(u)\,du.
\]
It is not a description of the field as a function of the height x.
The mean a and the exact position of the density's maximum need not
coincide; the large-time source is concentrated near its mean.

Write the normalized field as
\[
 F_T(x)=\frac{H_T(x)}{H_T(0)}
       =\int_0^\infty\rho_T(u)\cos(xu)\,du
       =\mathbb E_T\cos(xU),\qquad
 a=\mathbb E_T U,
\]
where U has the normalized heated half-line source as its density.
For an ideal Gaussian density on the **whole u-line**, the exact transform
identity is
\[
 \rho_G(u)=\frac1{\sqrt{2\pi}\sigma}
               e^{-(u-a)^2/(2\sigma^2)},\qquad
 \int_{-\infty}^{\infty}\rho_G(u)\cos(xu)\,du
       =e^{-\sigma^2x^2/2}\cos(ax).
\]
The source mound is centered at u=a, while the transformed envelope is
centered at x=0. Translating the Gaussian source changes the oscillation
frequency in x rather than translating the field to x=a. Indeed u=a+v
factors e^{ixu} as e^{iax}e^{ixv}. The centered Gaussian's transform is
real and positive, giving the displayed cosine after taking the real part.
This full-line identity is an illustration, not an exact replacement of
the canonical half-line source; its approximation errors are the subject
of Note 11. More generally U=a+(U-a) gives the same exact phase factor
for the actual source, with the centered transform supplying the remaining
amplitude and phase.

If all the source mass were at a single point a, this would be exactly
cos(ax), with zeros q_k/a, q_k=(k-1/2)pi. The actual source has width
sigma_T, with sigma_T^2=Var_T(U) asymptotic to 1/kappa at large T.
The Gaussian model gives an envelope exp(-sigma_T^2 x^2/2); odd cumulants
beyond the mean correct the phase and move the zeros. The series Y
inverts that phase. Thus it translates the shape and asymmetry of the
source into departures from the equally spaced reference zeros.

Across one source width, the angle xU changes by about x sigma_T.
Increasing T narrows the source and improves its Gaussian approximation.
Increasing x at fixed T instead magnifies the angle spread. The two
operations change the approximation problem in different ways, even
though both may be described loosely as going to a larger parameter.
The actual theorem allows a slowly growing standardized frequency; it
does not require x sigma_T to remain smaller than one.

An absolute error in an integral must be compared with its oscillatory
amplitude to control its phase. Dividing an absolute error by the Gaussian
envelope costs a factor exp(x^2/(2 kappa)). Note 11 pays precisely this
kind of cost: on a standardized disk of radius r it obtains the relative
error
\[
 E=O\bigl(\kappa^{-1}(1+r^6)e^{r^2/2}\bigr),\qquad
 r=\tfrac12\sqrt{\log\kappa}.
\]
The improving source approximation still wins over this amplification
on that growing disk. Taking a smaller interval inside the inverse disk
leaves room for both position and adjacent-gap bounds. Converting its
phase budget to a zero count gives
\[
 q_k\le\frac{a\sqrt{\kappa\log\kappa}}8,
 \qquad
 K(T)=\left\lfloor\frac{a\sqrt{\kappa\log\kappa}}{8\pi}
                    +\frac12\right\rfloor .
\]
The numerical fraction comes from the proof's margins, not a demonstrated
physical transition. Larger T gives an expanding block of zeros with a
shrinking uniform error bound. That statement does not say that, at one
fixed T, the cubic gets better as one proceeds through that block.
[Note 11 §§1–3](../../notes/11_EZ_GROWING_INVERSE_WINDOW_20261120.md).

## Why a different formula improves with height

For the explicit amplitude, phase, and arithmetic suppression mechanism,
see the expanded [Note 10](10_EZ_HIGH_HEIGHT_AMPLITUDE_PHASE_AND_SUPPRESSION_20261120.md).

For fixed 0<t<=1/2, Polymath describes the high field by two explicit
conjugate terms. Writing one as A_t(x) exp(i phi_t(x)), this gives
\[
 H_t(x)=2A_t(x)\{\cos\phi_t(x)+O(x^{-ct})\},\qquad A_t(x)>0.
\]
Here the error is already measured relative to the oscillatory amplitude.
The proof suppresses the remaining arithmetic terms increasingly as
t log x grows. Thus high zeros approach the successive crossings of this
different phase. The local phase slope is asymptotic to log(x/(4pi))/4,
so the spacing is asymptotic to 4pi/log x; the positional error divided by
the spacing tends to zero. This contrasts with the leading large-T
spacing pi/a in the growing origin window. It is a change of asymptotic
description of the same field, not a contradiction.
[Polymath, Proposition 9.1, Lemma 9.2 and the proof after (104)](https://arxiv.org/html/1904.12438v2#S9).

The quoted quantitative Polymath statement is in its stated time range.
It cannot simply be substituted at T=1000. The branch's fixed-positive-time
discussion and its unresolved common-time comparison are recorded in
[Note 16](../../notes/16_EZ_ASSESSED_ANCHOR_CONTINUATION_20261120.md).
Neither K(T) nor its adjacent rank is known to be the onset of a high-tail
formula at that time.

## The inverse coordinate has a separate limitation

For the literal half-line transform B_T=H_T+iS_T, at each fixed finite T,
\[
 B_T(x)=i\Phi(0)/x+O_T(x^{-2}).
\]
Eventually B_T stays in the upper half-plane. Its real part can cross zero
repeatedly while its continuous argument returns to the same value at
each such zero. Those crossings cannot all be labeled by successive
levels q_k of this one argument. The obstruction concerns that phase
coordinate, not the existence of high-zero approximations or resummations
in other coordinates. K(T) does not identify where that behavior starts.
[Note 04](../../notes/04_EZ_HALF_LINE_PHASE_OBSTRUCTION_20261120.md).

## Why the program wants a counted block

The explicit positions supply adjacent gaps and contributions to the
interaction with other zeros. Together with a bound for the unlocated
exterior, these are inputs to the gap equation and backward motion in
heat time. K(T) measures how much of the divisor can be supplied at once
with a common proof. The work is not centered on predicting the single
zero at K(T), and a useful approximation beyond K(T) is compatible with
everything proved so far. The remaining tasks include joining descriptions
at a common time and carrying the gap bounds farther backward.
[Complete exterior](../../notes/09_EZ_COMPLETE_ANCHOR_FROM_ZERO_FORMULAS_20261120.md) ·
[Current time estimate and scope](../../notes/15_EZ_SINGLE_ANCHOR_GAP_CURVATURE_20261120.md).

This explanation inherits, rather than changes, the
[collision-control screen](../../notes/11_EZ_GROWING_INVERSE_WINDOW_20261120.md#5-scope-and-controls).
Concentration, positive source weights, and a local inverse are not
collision-exclusion hypotheses. The quantitative window uses the complete
canonical theta envelope. Euler-factor and weighted-square controls change
its source coefficients; reflected, smooth and primitive-compatible
controls do not supply its canonical arithmetic expansion; finite-data
variants do not supply the complete source; changed-observation controls
fail the literal cosine readout. A control may still satisfy analogous
local inequalities on its own disk, without acquiring global backward
protection. See the [catalogue](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [premise rule](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md).
