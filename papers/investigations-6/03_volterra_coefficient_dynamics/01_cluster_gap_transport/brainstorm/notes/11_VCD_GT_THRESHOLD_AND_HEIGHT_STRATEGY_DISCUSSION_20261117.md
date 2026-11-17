# The local threshold and strategies across height

17 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and reasoning effort
are unavailable in this chat's recorded configuration. Chat0005, thread
`01a1ea30-1034-7b71-ab17-02eafef8fa22`, turn
`01a1ea47-264b-7be2-9db6-0f32f6a2e833`.

Edward selects the broader positivity objective and asks what 0.59 means,
what the direct-evaluation cost comparison establishes, and what different
proof strategies the exterior viewpoint might support as height varies.
This is an explanatory discussion and comparison of possible strategies;
it issues no research packet or new height theorem. The exact scalar
arithmetic below uses established inputs and acquires no source values.

Read the [result index](../../../../../../result-summaries/README.md),
especially [cluster18](../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../../../avoid/README.md), especially
[01](../../../../../../avoid/01_restating_the_target.md),
[02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[09](../../../../../../avoid/09_round_floors_and_fitted_laws.md),
[11](../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
and [12](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
The comparison identity and rescaling below are reorganizations of existing
algebra, not new positivity results. A future height estimate must be judged
by its independently proved inputs, domain and numerical constants or rates.

## Why 0.59 keeps appearing

Let M=-K, let [u,v] be a paid count-two tube, and set Delta=v-u. The
physical law and its backward identity are

    D' = 2 - 4 M D,
    W(t) = exp(-4 integral_t^v M(s) ds),
    W(u) D(u) = D(v) - 2 integral_u^v W(t) dt.

If M(t)>=kappa>=0 throughout the interval, the cost is bounded above by

    B_kappa(Delta) = (1-exp(-4 kappa Delta))/(2 kappa),
    B_0(Delta) = 2 Delta.

A lower anchor L_v<=D(v) with L_v>B_kappa(Delta) establishes a positive
margin over this tube. The cost decreases strictly with kappa, directly
from its integral expression. A stronger exterior interaction makes the
backward cost smaller. Negativity of K alone supplies no quantitative
margin: at a double D=0 the exact law still has D'=2.

Here Delta=0.1 and the already certified lower anchor is 0.17873684703.
The following rounded displays come from exact rational Taylor brackets:

| Uniform lower bound kappa on -K | Upper-cost formula B_kappa | Lower-anchor difference, approximately |
| --- | ---: | ---: |
| 0 | 0.200000000000 | -0.021263152970 |
| 0.57 | 0.178838368565 | -0.000101521535 |
| 0.58 | 0.178494721287 | +0.000242125743 |
| 0.59 | 0.178151971243 | +0.000584875787 |

The unique scalar break-even value against this lower anchor lies strictly
between 0.5729515 and 0.5729516, approximately 0.572951516. This is a
threshold for this constant allowance and this anchor, not a necessary
pointwise bound on the true M. A nonconstant signed profile can do better.
[Arithmetic code](../../numerics/vcd_gt_threshold_discussion.py) and
[small record19](../../numerics/19_VCD_GT_THRESHOLD_DISCUSSION_20261117.json).

The original [Decision05](05_VCD_GT_B05_UNIFORM_SIGNED_CERTIFICATION_20261116.md)
explicitly says to try -59/100 and that an enclosed upper K bound at most
-58/100 may also succeed. The actual diagnostic had K near -0.60, making
0.59 a convenient conservative target. Later work retained it as the
same finite acquisition benchmark. It is neither a universal constant nor
an optimal threshold. The occurrence of 19/32=0.59375 elsewhere is also
separate: [Note19](../../notes/19_VCD_GT_E03_MATCHED_GAP_MINIMUM_20261116.md)
derives that number as a lower bound on D' from two-sided drift and radius
data. The latest exterior certificate happens also to exceed 19/32;
this does not identify those two different bounds.

## What the local cost comparison means

[Synthesis16](../../notes/16_VCD_GT_CANONICAL_SIGNED_GAP_SYNTHESIS_20261116.md)
compares a time-zero row requiring 65 distinct xi evaluations with a fine
transport source grid requiring 196673 evaluations at 33 times. Both receive
already paid collar and angular information. This is not a measured ratio
of complete independent algorithms, a uniform asymptotic complexity claim,
or an exclusion of analytical transport strategies.

The direct route encloses D(0) from the actual field and shared contour
geometry. The transport route uses a later gap and interaction information
over a time interval to infer an earlier gap. At t=0 the source is directly
xi; the chosen positive-time implementation uses a Gaussian convolution.
That helps explain the local evaluation disparity without establishing an
unavoidable cost law for all implementations or heights.

With the same controlled tube, D(0)>0 already propagates qualitative reality
forward: a first forward zero of D would need D'<=0, contrary to D'=2
there. [Continuation17 section 2](../../notes/17_VCD_GT_RESEARCH_CONTINUATION_20261116.md#2-the-bottleneck-and-the-direct-baseline)
records this baseline. Thus changing the advertised output from endpoint
reality to whole-slab reality does not create an exclusive transport gain.
The direct method can also use all exterior counts, scalar envelopes and
joint estimates obtained by the transport analysis.

The meaningful broader distinction is the burden of proof. Repeated
pointwise field evaluation settles bounded examples. A uniform structural
estimate could settle a family without evaluating every target gap. The
exterior acquisition has not yet made this transition: its target data
already have positive D, and its real brackets were themselves acquired
by field evaluation. A slower local demonstration can nevertheless expose
an inequality that is more useful analytically. No implication of either
kind follows from operation counts alone.

## The height variables that replace a fixed threshold

For a fixed positive length scale ell at each selected height, put

    z=a+ell X,  t=u+ell^2 tau,
    Dhat=D/ell^2,  Mhat=ell^2 M.

Then exactly dDhat/dtau=2-4 Mhat Dhat. The invariant quantities for the
constant comparison are

    q=L_v/(2 Delta),  eta=4 kappa Delta,
    q > (1-exp(-eta))/eta.

Consequently kappa, the incoming gap and the time interval must be scaled
together. Asking for -K>=0.59 at every height would preserve the pilot's
units rather than its comparison problem. No fixed positive normalized
margin is asserted: a valid positivity argument may have margins tending
to zero. Strict D(0)>0 also proves pair simplicity; reality alone allows
D(0)=0. A global RH objective must not silently add a uniform gap floor or
time-zero simplicity requirement.

At time zero the zero-counting main term suggests a nominal mean-spacing
scale proportional to 1/log(height). This is a scale convention, not a
claim about each gap, each short window, or each positive heat time.
The primary-source inspection below records the scope of this comparison.

The current favorable-remainder proof has a concrete scaling obstacle.
For an exterior occurrence c+x+iy, its grouped per-occurrence weight is

    (x^2-y^2-D)/((x^2-y^2-D)^2+4 x^2 y^2).

Positivity follows when x^2>y^2+D. A global width-one strip suffices with
the pilot's enlarged empty disk. In a shrinking neighborhood of size ell,
the same vertical allowance becomes 1/ell in scaled units and no longer
pays nearby-group positivity. The existing two-zero disk of fixed radius
8/5 is not a height-uniform geometry theorem. A broader argument must
establish suitable transverse control, handle nearby signed groups
together, or work with larger counted clusters. Selecting some real
exterior roots alone does not justify dropping an uncontrolled complex
remainder. This identifies a missing hypothesis, not impossibility of a
height-dependent estimate.

## Possible advantages and proof architectures

The useful feature of a paid favorable exterior sum is monotonicity:
independent lower counts and upper distances give a lower mass, and
additional favorable uncounted zeros cannot spoil it. Exact root identities
or very accurate root positions are unnecessary. This may replace delicate
field cancellation with robust inequalities about groups of zeros, provided
the counts, geometry and remainder are obtained independently.

Three possible architectures deserve comparison in further discussion:

1. **Local counts and distances on the relevant scale.** Prove lower
   counts in several disjoint ranges around every relevant target cluster,
   then use the established grouped weights. These counts must hold near
   exceptional close pairs, not merely for most centers or on average.
   The incoming gap and allowed time length remain part of the same test.
   This is an unproved acquisition target, not a new sufficient-criterion
   milestone.
2. **An integrated interaction estimate.** Bound the actual weighted time
   cost using correlations of gap, center and exterior population, instead
   of imposing a single worst constant kappa. The 512-cell success shows
   that retaining time information can matter locally. A useful theorem
   would need to estimate the joint quantity without simply rewriting
   the unknown early gap. No signed canonical estimate of this scope is
   supplied here.
3. **A contradiction on the already real side of a hypothesized positive
   threshold.** Under an assumed Lambda>0, all-real information at t>Lambda
   is legitimate; assuming it at t=0 would be circular. This may simplify
   exterior signs and permit a collective count or energy argument. It
   still needs a new quantitative contradiction or uniform continuation
   mechanism for exceptional clusters. Existing uniform exterior localization
   does justify a finite multiple collision at any fixed positive threshold,
   as explained below; it does not provide a height bound uniform as that
   threshold tends to zero. The Rodgers–Tao negative-threshold estimates do
   not become positive-threshold estimates by changing the time label.

These architectures can be combined with direct evaluation on a bounded
height range. The necessary unbounded-height remainder remains a theorem,
not a finite scan. Mean density alone gives neither the local conditional
counts nor a successful incoming-gap budget. The methods also need not
remain separate: a useful exterior theorem becomes available to a direct
proof using the same information.

There is already useful positive-time exterior information. Polymath
Theorem 1.5(i)–(ii), checked below, places sufficiently high zeros on the
real axis and near a regular sequence, with onset of shape exp(C/t).
For t>=b>0 this gives a common finite exceptional range, but its size
grows as b decreases. Thus the strategic difficulty is the joint limit
of small positive time and increasing height, not arbitrary height at
one fixed positive time.

The repository's [positive-threshold analysis](../../../../../investigations-5/02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md),
section 3, and [collision manuscript](../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex),
Proposition “A positive threshold entails a finite collision,” already
combine that uniform exterior input with compactness. If Lambda=T>0,
nonreal zeros as t increases to T have a subsequence approaching a finite
real multiple zero. This is an established reduction in those sources,
not a new result of this discussion. The multiplicity is at least two,
not necessarily exactly two: a complete argument needs higher clusters
or a justified reduction to pairs. A positive-time bulk spacing conclusion
alone cannot exclude such a finite exceptional event.

## Control screen for this discussion

The exact comparison itself applies to controls and is no discriminator.
The [small arithmetic run](../../numerics/19_VCD_GT_THRESHOLD_DISCUSSION_20261117.json)
rechecks the quadratic margin -1/10 and the quartic heat identity; at its
double the quartic is (z^2-a^2)^2 and has no additional exterior real
brackets. A genuine target double gives zero exact endpoint margin when
the backward interval ends at that double, regardless of favorable K.

The [Note30 premise table](../../notes/30_VCD_GT_E03_REAL_BRACKETS_AND_MOVING_BOUNDARIES_20261116.md#7-controls-comparison-and-scope)
and [Note21 full screen](../../notes/21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md#6-screening-the-used-premises)
apply as follows. This is a reapplication of their proved classifications;
no large source-control certificate was rerun.

| Control | Premise verdict for a proposed height extension |
| --- | --- |
| Quadratic and even quartic | Extra exterior real-count premise fails; sign alone does not pay passage. |
| Nonzero Gaussian-factor and reflected super-Gaussian | Order-at-most-one premise fails. |
| Specified weighted-square, finite-source/score and finite-prime endpoint-defective classes | Global finite-strip premise fails; finite matched measurements do not restore it. |
| Euler-factor translates | Order and physical heat law survive; some have width one. Required local geometry, counts and magnitude remain untested, not automatically false. |
| Damped smooth-shape and positive-primitive controls | Share order/physical flow; relevant strip, counted geometry and quantitative lower mass remain untested. |
| Reflection rigidity and four-family comparison | Keep their scoped arithmetic distinctions; they supply no additional quantitative height estimate. |
| BW-01 and finite-profile threshold controls | An all-real region above their own threshold does not pay descent below it; proposed local counts and budgets require separate tests. |
| RH-conditional endpoint merger | Retains its RH premise; a double at the target endpoint has zero exact margin. An unnecessary simplicity demand would fail there. |
| Changed observation and fractional-profile relaxation | Respectively lack the literal physical heat equation or a genuine integer divisor. |
| Four- and five-atom examples of Note24 | Fail the frozen width-one strip; their shared algebra still prevents inferring a new signed estimate merely from positive weights. |

In particular, a proposal using the all-real side of a threshold must still
distinguish finite-threshold collision controls quantitatively. Merely
sharing heat flow, real zeros at later times, or average density is not
the missing canonical estimate.

## Primary-source inspection

Rodgers and Tao, *The de Bruijn–Newman constant is non-negative*,
[arXiv:1801.05914v5](https://arxiv.org/pdf/1801.05914v5), 3 July 2021:
online PDF introduction, printed pp.2–4, checked on 17 November 2026 for
H0=xi((1+iz)/2)/8, the all-real threshold statement, and the zero-counting
main term used to identify a nominal spacing scale. Their argument and
nearby real-zero counting discussion operate under Lambda<0; no theorem
from their negative-time regime is imported into positive-threshold descent.
This is selected-passage inspection, not full-proof validation.

The existing external PDF at
`/Users/Shared/szp-archive/height-dependent-heat-contours/references/1801.05914v5.pdf`
was rechecked: 503405 bytes, SHA-256
`376bb2c1ab941cd5b035546835c5481f2d026767b8e830a48cd5565114a1ec91`.
The [canonical catalog](../../../../../investigations-5/02_heat_flow_rh_applications/references/sources.json)
retains the new use and earlier provenance; no duplicate PDF or article
record is created.

D. H. J. Polymath, *Effective approximation of heat flow evolution of the
Riemann xi function, and a new upper bound for the de Bruijn–Newman
constant*, [arXiv:1904.12438v2](https://arxiv.org/pdf/1904.12438v2),
4 August 2019: introduction and Theorem 1.5(i)–(iv), printed pp.9–10,
checked online on 17 November 2026. For 0<t<=1/2 the constants are
absolute; reality and clock localization apply beyond exp(C/t).
Part (iv)'s cumulative and unit-interval counts do not supply lower
counts in every shrinking window around a selected close pair.
No numerical value of C, t=0 exterior theorem, or full proof audit is
claimed. The existing external copy
`/Users/Shared/szp-archive/height-dependent-heat-contours/references/1904.12438v2.pdf`
was rechecked: 2158176 bytes, SHA-256
`60d0d2d381227d32f98535a5c43dedb86e333a9006d6819f0bdebdd734085603`.
