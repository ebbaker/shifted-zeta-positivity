# HMC-06 gate and endpoint limit review

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from the current turn metadata.
Separate-chat, same-model internal assessment; no specialist or independent
cross-model validation. [Chat 0007](../chat-histories/0007_2026-10-21T14-09-42Z_review-hmc-06-progress-blockers.json).

**Assessment:** HMC-06 is correctly gated. HMC-05 has quantified a
universal endpoint profile and its error, but has no estimate separating
the unchanged theta source from the applicable collision controls.
A singular limit at infinite heat time is real at the level of phase
density, yet it also occurs for pairs initially distinct. A direct
nonconcentration argument remains a possible logical route only if its
new estimate retains and uses the assumed multiple birth.

This assessment follows the [result index](../../../../../../../result-summaries/README.md),
[collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md),
[heat summary](../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and [avoid index](../../../../../../../avoid/README.md), especially
[reformulations](../../../../../../../avoid/01_restating_the_target.md),
[shared control premises](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[geometric re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## Progress and the remaining mathematical input

| Work | Supported status | Consequence for HMC-06 |
| --- | --- | --- |
| [Note 19](../notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md) | Complete root-tail payment, both velocities, rank-dependent enclosure, finite-time width bound, moving deflation | HMC-01 is proved in-note and HMC-03 has a bounded deliverable. Multiple births remain compatible with the estimates. |
| [Note 20](../notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md) | Differentiated fixed-label saddle estimates and eventual shrinking | No finite collision or regular terminal jet follows from a gap tending to zero at infinity. |
| [Note 21](../notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md) | HMC-04 complete for its bounded product tubes, with paid trace and derivative errors | The corrected four-dimensional observation reduces exactly to the planar one and supplies no additional sign. |
| [Note 22](../notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md) | Complete-source error around the Hermite tube profile, uniform for bounded transverse scale at each fixed event | Matching controls share the leading profile. HMC-05's separating estimate is still absent. |

The [manuscript](../manuscript/main.tex) consolidates Notes 15–18 rather
than the later HMC derivations. Its approximation constant retains squared
multiplicities, its heat transition retains their excess, and its declared
arithmetic-transfer classes pay a nonzero repair cost. Those conclusions
are consistent with the HMC obstruction. The complete scaled-tail theorems
remain substantial internal premises warranting independent analytic
review. They are not premises of Notes 19–22, so that separate verification
issue is not the immediate HMC-06 gate.

This review read the full manuscript, Program/Progress 02, Notes 19–22,
Reviews 19–21, and the relevant endpoint-control and parent-progress
material. It is a dependency and gate assessment of the approximation
manuscript, not a fresh proof audit of every estimate in Notes 15–18.

## What the shrinking cap does and does not imply

The accompanying [Note 23](../notes/23_CAP_PHASE_CONCENTRATION_AND_FINITE_TIME_BASELINE_20261021.md)
distinguishes three objects: the spatial cap phase, a closed space-time
collision index, and the limiting phase measure. Every adjacent simple
pair has cap phase \(\pi\), including a pair already distinct at time zero.
An outer block of \(m\) roots has \((m-1)\pi\) regardless of common birth.

For a fixed positive pair under RH, the cap shrinks to zero and its phase
measure tends to \(\pi\delta_0\). The product identity gives the exact
stationary-point lower bound \(\rho(x_*)\ge8/g^2\). In the large-time
cosine model, the peak has height \(L_t^2\), width \(L_t^{-2}\), and
integral \(\pi\). Thus divergence is forced by the established assumptions;
it cannot itself contradict them. It concerns an infinite-time limit, not
a new finite-time zero of \(H+iH_x\).

A different expression for the same integral could be useful if it
proved a stronger estimate under the multiple-birth hypothesis. Merely
showing that the integral stays finite, changing to the phase variable,
or writing the same density in rescaled coordinates does not prove
nonconcentration. A generic prohibition of this limit would also exclude
the ordinary fixed adjacent caps which the same analysis covers.

## How to sharpen the next bounded comparison

Note 23 CP9 proves that the exact quadratic control already satisfies

\[
I^{\rm quad}_{r\sqrt{2t}}(t)
=\pi(1+r^2)-r^2\sqrt{2t}+O_r(t),
\]

with an explicit one-sided remainder. Therefore a negative correction
after subtracting only \(\pi(1+r^2)\) would not by itself distinguish
theta. Subtract the exact finite-time quadratic observation before
interpreting a correction as additional source information.

For an isolated double, the complete scaled germ begins

\[
p_\tau=\operatorname{He}_2+
\alpha\tau\operatorname{He}_3+
\beta\tau^2\operatorname{He}_4+O(\tau^3),\quad
\alpha=\frac{H_{xxx}(0,a_0)}{3H_{xx}(0,a_0)},\quad
\beta=\frac{H_{xxxx}(0,a_0)}{12H_{xx}(0,a_0)}.
\]

This follows from Note 22's complete Taylor expansion. The existing
deflation identity gives \(S_0=\alpha^2-2\beta\). Its nonnegativity under
RH is generic product information. Neither these coefficients nor a new
formula for their contribution supplies an arithmetic sign by itself.
The next useful calculation must retain the actual endpoint shifts and
physical denominator, establish the first surviving source-dependent
term with an error smaller than the claimed separation, and compare it
with the close positive endpoint controls before theta quadrature.
The present \(O(\tau\log(1/\tau))\) error does not resolve a coefficient
at scale \(\tau\), still less one at scale \(\tau^2\).

## Coverage and choice of contradiction

A direct exclusion of the original endpoint can complete HMC-06 without
forcing a later collision. A route through infinity instead needs a
justified terminal contour or measure argument; no regular terminal
physical jet is furnished by the current saddle limit.

Uniform constants over all heights and multiplicities are not invariably
necessary. A local proof may fix an arbitrary finite event, retain its
nonzero leading coefficient and finite event-dependent constants, and
choose a sufficiently small time depending on that event. If the signed
contradiction works for every such event, this can give all-height
coverage. This does not authorize a uniform numerical threshold or an
exchange of limits. For \(m>2\), all other birth roots and their singular
interactions must still be retained; the isolated-double calculation
does not provide that extension.

HMC-03 turning-time refinements, a numerical late-time onset, and more
generic contour identities are not prerequisites for that direct local
route. The immediate missing input remains a quantitative estimate from
unchanged theta arithmetic that the relevant controls fail.

## Quaternionic and octonionic surface assessment

The product-tube equality in Note 21 does not settle every possible
higher-dimensional surface. The original Investigation 21 material has
several distinct constructions:

- [Note 35](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/35_REFLECTED_LIFT_AND_PHYSICAL_REDUCTIONS_20261015.md)
  gives exact octonionic monogenic lifts and associators. Their physical
  signed coefficient is the existing real determinant; its norm loses
  the sign. These generic reductions do not add a theta restriction.
- [Note 50](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md)
  gives closed self-dual forms and a polarized Stokes flux. HMC-04 tests
  one concrete moving product-domain consumer of those forms.
- [Notes 60](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/60_HYPERKAHLER_LIFTS_AND_COLLISION_DEGENERACY_20261015.md)
  and [61](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/61_JET_SURFACES_REAL_GAUSS_MAP_AND_ORIENTED_TURNING_20261015.md)
  construct actual metrics and the immersed jet surface \((P,H,w)\).
  Its real dimension is four; coassociative and Cayley inclusions hold
  on its regular locus. Physical-energy metrics degenerate at a joint
  zero. The ever-immersive enlarged graph changes the energy coefficient.
- [Note 62](../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/62_THETA_JET_BUNDLE_AND_SEMIFLAT_HYPERKAHLER_GEOMETRY_20261015.md)
  puts the actual theta source in a jet bundle over an elliptic family,
  with a nonflat local semi-flat metric. This carries arithmetic data
  absent from the arbitrary-holomorphic-function construction.

Note 23 CP10–CP13 calculates the physical curve's induced length in the
cosine model: the coordinate cap tends to zero but the amplitude-normalized
image is a narrow half-ellipse with length tending to two. Thus neither
surface shrinkage nor a vanishing boundary measure follows just from
\(b-a\to0\). A geometric integral needs its own measure, form norm and
physical-trace comparison.

The actual calibrated surface can branch at a collision. For example
\(H=z^2-2t\) yields a cusp at zero time while its regular surface patches
have the same complex/Cayley calibration. Calibration alone therefore
does not supply the missing regularity theorem. This is a statement about
these constructions and controls, not a prohibition of other geometric
estimates.

Note 61's marked real Gauss map is a more targeted consumer of the
author's nonconcentration idea. Its **one-sided** modulus excludes
positive quarter-turn concentration before a finite collision, while
allowing negative turning on all-real caps. Centering the local
predecessor calculation at \(T=0\) would use \(t<0\) to test an original
multiple endpoint. The angle is \(\arg(H+iH_x)\) for even multiplicity
and \(\arg(H_x+iH_{xx})\) for odd multiplicity. The latter has its own
nonvanishing requirement and denominator, which cannot silently be
replaced by \(H^2+H_x^2\). The required source bound, its domain and
both parity branches must be established; neither RH on \(t\ge0\)
nor calibration alone supplies it.

Some connection work proposed in Note 62 was subsequently completed on a
marked cover: Investigation 22's
[ASD metric and physical-restriction note](../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md)
gives an adapted connection and the transverse lower-jet commutators.
Its natural physical-path and external two-source pullbacks are flat.
Thus the next missing step is not merely constructing a connection:
it is a quantitative use of transverse or global arithmetic information
that survives the full physical weight
\(\exp(t(\log y)^2/16)\), oscillatory Mellin phase and all boundary terms.
The Jacobi theta heat connection is a different evolution.

The originals above, Investigation 21 Note 63 and Review 34, the
hypercomplex result summary, and the stated Investigation 22 continuation
were read for this addendum. The calibration inclusions were also checked
against [Lotay Propositions 6.5(b) and 7.3(a)](https://arxiv.org/html/1810.08709).
There is no claim here of a complete audit of every quaternionic or
octonionic note in the portfolio.

## Verification and disposition

The three existing exact-algebra replays were rerun successfully in this
chat without changing their scripts or previous receipts. They check
finite polynomial identities, not the analytic tails or theta exclusion.
The classical normalization and paired-root import were checked against
[Polymath Proposition 3.1](https://arxiv.org/html/1904.12438v2#S3), and the
Hermite convention against [DLMF 18.12.16](https://dlmf.nist.gov/18.12.E16).

The mathematical gate status remains HMC-05 open and HMC-06 gated.
Note 23 and this assessment clarify the next comparison and the author's
infinite-time singularity question. They do not amend the manuscript's
claims or assert a new original-zero exclusion.
