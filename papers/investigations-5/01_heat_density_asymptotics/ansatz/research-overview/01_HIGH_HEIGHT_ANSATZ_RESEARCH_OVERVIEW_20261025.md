# Research overview: large-height heat-density ansätze across time

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.
Chat0022, thread 01a17572-5411-7f32-9a12-7d1ba46ad679.

## Author's objective and priority

Develop a good analytical formula for the large-height region as a
function of **every real heat time**, allowing different formulas around
transitions and outside them. The displayed solution should be simple;
the error estimate may be complicated. Invest the main analytical effort
in high-height amplitude, phase, arithmetic corrections and matching.
The Gaussian-polynomial central approximation remains a supporting
direction, rather than the next priority.

The [working manuscript](../manuscript/main.tex) is the maintained draft.
[Ansatz Note01](../notes/01_REGIME_BY_REGIME_SOLUTION_ANSATZE_20261025.md)
is the original catalogue; [Note02](../notes/02_HIGH_HEIGHT_PRIORITY_AND_DRAFT_SCOPE_20261025.md)
records the new emphasis. The [ansatz progress register](../research-progress/01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md)
owns only this branch's tasks. The
[parent register](../../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
continues to own parent HDA statuses and the weak-filter cost queue.
This division implements the author's explicit request for a new
overview and corresponding progress document, without duplicating task
ownership.

## What already exists

The parent manuscript, through Notes54–55, supplies a finite analytical
all-time/all-height construction with the full physical tuple, declared
buffers, one source per target accuracy and both time-endpoint error
limits. [Summary62](../../notes/62_CHAT0021_RESEARCH_SUMMARY_20261025.md)
records Notes58–61: positive source compression, finite evaluator/filter
errors, free-onset exact phase selection and polynomial additional
accuracy-bit cost at a fixed descriptor/query box.

Those results do not give a short low-parameter high-height formula
uniformly through zero time or useful uniform height cost. Their in-note
and internal review statuses remain; the full independent inherited-chain
audit is outstanding. HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled
are unchanged.

The opening ansatz draft calibrated the leading elementary cosine
against the parent linear gamma carrier and proposed a heat-weighted
finite sum. The continuations in Notes03--04 now prove its first compact-positive
correction and a retained-correction signed-time field comparison on
full fixed complex buffers, with spatial jets and a direct time bound.
[Note05](../notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md)
adds bounded fixed-negative-time results on 1<=T<=2: a short gamma-scale
formula and a separate finite representation at outer-carrier precision.
[Note06](../notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md) extends
the latter and joins it through zero, paying a full negative interval [-2,0].
Physical transfer and the larger all-time program remain open.

## Mathematical contract

Preserve the complete canonical source and normalization

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\quad
H_t=-H_{zz},\quad H(0,z)=\xi((1+iz)/2)/8.
\]

Write z=x+iy, X=|x| and ell_X=log(X/(4pi)). Zeta height is X/2.
Retain the parent's physical epsilon_g, q=epsilon_g², fixed K=k_ell k_h,
actual signed covariance and joining/regulator defects. Initial physical
target strip is |y|<=1; every proof also pays the full averaging,
root-collar and holomorphic differentiation buffers it uses.

A field estimate is scaled by a positive carrier envelope, never divided
by a cosine that vanishes. Keep two distinct targets:

1. Correct amplitude and unwrapped phase, with normalized field and
   spatial/time errors. An exponentially small absolute field error can
   be inadequate here.
2. Unnormalized physical U,W,R,J,Q and the remaining parent tuple, with
   direct transfer estimates. A pre-switch density tending to zero does
   not settle the underlying arithmetic field.

All-times coverage means fixed-time asymptotics, compact-time uniformity,
and separately stated joint time/height limits. Onsets and constants
must display time dependence. No single universal height cutoff for all
real time is assumed.

## Main candidate and the missing arithmetic

The leading positive-time outer model is

\[
F_o=A_o\cos\Theta_o,\qquad
A_o=\frac{\pi^{1/4}}{16}X^{7/4}
 \exp[-\pi X/8+(t/16)(\ell_X^2-\pi^2/4)],
\]
\[
\Theta_o=X(\ell_X-1)/4+\pi t\ell_X/16+7\pi/8.
\]

Here A_o is the full cosine amplitude, twice one carrier's amplitude.
The parent linear model supports the leading reduction on fixed
32<=t<=T. Published small-positive-time input is separate. A uniform
extension to zero or negative time is not supplied.

At t=0 the correct starting point is the Riemann–Siegel sum with about
sqrt(X/(4pi)) terms. Near zero, investigate

\[
F_{\rm arith}=A_o\sum_{n\le N}
n^{-1/2}\exp\{(t/4)[(\log n)^2-\ell_X\log n]\}
\cos\{\Theta_o-(X/2+\pi t/8)\log n\}.
\]

The uncorrected sum remains insufficient at the requested negative
edge. Note04 adds an analytic fixed-cutoff RS correction and proves its
bounded signed-time comparison, including the whole mode population. The scale tau=t ell_X controls each fixed
mode, but a finite set of modes does not control the growing cutoff
population. No universal critical tau or universal one-variable crossover
profile is assumed.

## Regimes and workstreams

| Priority | Branch task | Required mathematical gain |
| --- | --- | --- |
| 1 | HDA-A01: high-height calibration and arithmetic bridge | Pin normalization/branches and the first correction; establish a signed small-time finite-sum comparison, initially abs(t) ell_X<=8, or identify the exact failed estimate. |
| 2 | HDA-A02: negative-time high-height representation | Use the exact forward Gaussian convolution of H(0); prove compact negative-time tail formulas and retain the whole smoothing window and cutoff crossings. |
| 3 | HDA-A03: regulator layer | Improve field-to-density transfer and exact recentering near t_c(X); separate the O(1) shape theorem from higher accuracy and direct time/current/covariance claims. |
| 4 | HDA-A04: joint positive time/height | Match the outer cosine to the supported full gamma saddle; test Lambert W only with its own branch, field and residual estimates. |
| 5 | HDA-A05: joint negative endpoint | Determine scales and overlaps with the large-negative-time Gaussian without substituting a fixed-time asymptotic into a joint limit. |
| 6 | HDA-A06: full piecewise assembly | Produce a domain-union and matching theorem with the complete physical observable inventory and all defects. |
| Supporting | HDA-A07: core and ancillary catalogue | Retain the Gaussian-polynomial candidate and earlier clock/local-peak/covariance models; central optimization follows the high-height work. |

The number 8 in the first bounded crossover window is a work boundary,
not a conjectured transition constant. No numerical campaign is launched
by this overview.

## Two transitions that must remain separate

The arithmetic crossover concerns the field near t=0 as height increases.
The regulator transition concerns epsilon_g relative to one gamma-arm
amplitude near the chosen switch t=64. Its exact center satisfies
b(t_c,X)=log(epsilon_g/A_arm)=0; its shift is of order 1/log X,
while its rounding width is of order 1/(X log X).

The inherited layer profile is
omega[k_h(y-d)+k_h(y+d)]/(2pi), d=b_+/omega, with O(1) absolute
error. Preserve the exact center when resolving its narrow window.
Neither an elementary-amplitude substitution nor changing from a
one-arm to a full-cosine amplitude is innocuous at higher accuracy.
The switch is part of the measurement protocol, not a discontinuity
of H or an intrinsic critical time.

## Acceptance and review

A regime is accepted only with its actual domain, nonvanishing envelope,
normalization/branch choice, arithmetic and contour remainder, buffered
jet/time estimates, and the stated consumer. Classify each displayed
formula as exact, inherited, derived within stated hypotheses, formal,
or open. Do not differentiate big-O allowances. Pay gamma curvature
and determinant corrections alongside Stirling corrections; arithmetic
terms can dominate nominal inverse-height corrections.

Before claiming a full result, demonstrate that the regime union covers
the intended all-time domain and that the overlaps agree at the requested
precision. Retain multiple-zero possibilities wherever simple collars
have not been established. Independent specialist review remains a
separate obligation.

Read the [result index](../../../../../result-summaries/README.md),
especially [11: corrected Riemann–Siegel interface](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[12: collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [13: local geometry](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md).
Read the [avoid index](../../../../../avoid/README.md), especially
[01](../../../../../avoid/01_restating_the_target.md),
[02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[05](../../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../../avoid/08_normalization_and_constant_slips.md),
[12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
[16](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md)
and [19](../../../../../avoid/19_status_files_that_lag_the_findings.md).

The canonical arithmetic/gamma identity fails for the Euler-factor,
finite-square, reflected super-Gaussian, smooth-shape, positive-primitive
and counter-kernel controls in their respective ways. The quantitative
source-specific comparison must exploit that difference. Gaussian shape,
positivity, symmetry and leading zero density by themselves are not
collision or RH information. This program is an approximation task,
not a restatement of an RH-equivalent criterion.

## AN01 continuation (historical)

25 October continuation for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), actual effort ultra**, ansatz chat0001.
[Note03](../notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md)
proves the corrected outer carrier on 32<=t<=33, including full-buffer
jets and a direct time derivative, and a corrected **signed real-axis
field** bridge on |t| log(X/(4pi))<=8 with O(A_o X^-1/4) error.
The gamma determinant/curvature, retained RS correction, growing mode
population, cutoff crossings and full Gaussian tails are paid.
[Assessment02](../reviews/02_CALIBRATION_AND_REAL_BRIDGE_ASSESSMENT_20261025.md)
records same-model internal acceptance only. This does not promote the
opening candidate to a full complex or physical-observable theorem.

The exact missing estimate is Note03 CB28, the zero-time fixed-cutoff
complex RS remainder on the full declared buffers. The naive complex
Gaussian bound fails uniformly through zero; CB29 preserves its factor
and scope. **Analysis — Sol**, following
[HDA-A01-AN02 r1](../research-progress/handoffs/HDA-A01-AN02.md), should
prove that estimate or a sufficient specified epsilon-loss version and
then pay buffered consumers. AN01 is closed at its permitted bounded
partial-return scope; HDA-A01 is Partial. Escalate only if a specific
mechanism resists that focused Sol attempt. No numerical campaign or
automatic dispatch is authorized by this update.


## HDA-A01-AN02 continuation (historical)

25 October, **gpt-6.1-sol, actual effort ultra**, same ansatz chat0001.
[Note04](../notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md)
now proves the previously open CB28 with no epsilon loss. Its fixed-N
model has full buffered signed-time field/jet/time estimates on |t|L_X<=8,
with delta=X^-3/4 exp(t_- L_X^2/16)<=C X^-1/4. The positive-side
field allowance is X^-3/4. [Assessment03](../reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md)
records same-model internal acceptance only; constants/onsets remain
unevaluated. The earlier subsection describes the AN01 historical gap,
which is closed by this continuation.

HDA-A01 is complete at the bounded AN01--AN02 analytical scope. The next
deliverable is **Analysis — Sol**, [HDA-A02-AN01 r1](../research-progress/handoffs/HDA-A02-AN01.md),
one fixed negative-time window 1<=T<=2 with all growing-order/contour
and mode-heat-curvature errors paid. This is prepared, not dispatched.
The fixed-order shrinking-time bound cannot simply be substituted at
fixed T. The physical tuple, all-time coverage, useful cost and independent
specialist review remain separate; parent HDA statuses are unchanged.

## HDA-A02-AN01 continuation (historical)

25 October, for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, recorded effort ultra**, same ansatz chat0001.
[Note05](../notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md)
FN5 proves the short corrected arithmetic model on 1<=T<=2 with
O(|G|X^-3/4) field, spatial j<=3 and direct first time errors. FN10
retains the failure of that bound after outer-carrier conversion.
FN25--26 instead construct a finite growing-order representation with
all those errors C E_o exp(-L_X^2/4). Both growing RS constants and
all arithmetic heat curvature are paid. A bounded correction integral
remains; this is not a short elementary formula or a useful-cost theorem.
[Assessment04](../reviews/04_FIXED_NEGATIVE_TIME_ASSESSMENT_20261025.md)
is same-model internal only. Constants/onsets are not instantiated.

AN01 closes at its bounded scope; HDA-A02 remains Partial. Next
**Analysis — Sol**, [HDA-A02-AN02 r1](../research-progress/handoffs/HDA-A02-AN02.md),
is prepared, not dispatched. Prove the bridge 4/L_X<=T<=2, including
exp(b^2/(4T)) and derivative losses, then join to Note04 on
4<=T L_X<=8. This targets [-2,0] on full buffers, with actual joining
time defects; that interval is not already accepted. No T>2, physical
tuple transfer or all-time theorem follows. Parent HDA statuses remain.

## Current result and next bounded continuation after HDA-A02-AN02

25 October, for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, recorded effort ultra**, same ansatz chat0001.
[Note06](../notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md)
extends the unchanged finite model to 4/L_X<=T<=2 at E_o exp(-L_X^2/4)
accuracy, including spatial j<=3 and first time. Gaussian rescaling
pays normalization; exp(b^2/(4T)) and all derivative factors are retained.
Growing RS constants, all-mode curvature, exact cutoff and all tails
are paid uniformly. The finite model retains exact heat residual zero.

Its paid overlap with Note04 supports a time-only join on [-2,0].
Spatial errors are C E_o X^-1/4 Lambda_X^j; first time error is
C E_o X^-1/4 Lambda_X^2. The actual residual is bounded by
C E_o X^-1/4 Lambda_X, persists in the crossover layer, and vanishes
above T L_X=8. Weighted estimates are sharper. [Assessment05](../reviews/05_NEGATIVE_BRIDGE_AND_TIME_JOIN_ASSESSMENT_20261025.md)
is same-model only. No numerical onset or useful-cost claim is supplied.

Both HDA-A02 packets close at their bounded scopes; HDA-A02 remains
Partial. [Note07](../notes/07_CHAT0001_RESEARCH_SUMMARY_20261025.md)
summarizes all Notes03--06 and four completed packets in this chat.
Next **Analysis — Sol**, [HDA-A03-AN01 r1](../research-progress/handoffs/HDA-A03-AN01.md),
is prepared, not dispatched: corrected one-arm comparison on a bounded
regulator-switch neighborhood and named center shifts under the exact
physical sensitivity. General compact-negative endpoints, physical
transfer, independent specialist review and all-time assembly remain
open; parent statuses are unchanged.
