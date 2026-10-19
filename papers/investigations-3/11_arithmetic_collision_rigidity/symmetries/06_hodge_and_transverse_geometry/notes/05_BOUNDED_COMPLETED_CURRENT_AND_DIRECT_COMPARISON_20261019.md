# Bounded completed current and direct first-jet comparison

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**. Analytic estimates and outward Arb computation;
separate same-model internal review, no specialist human review.

## Outcome and task status

**The S06-T2 bounded comparison is complete; its benefit gate failed.**
After the T1 closure, this continuation selects a different completed
residual, one that vanishes at a physical collision. Fresh complete
four-jet acquisition estimates it without assuming the inherited Laguerre
sign. On the unchanged 64-cell pilot, both precision runs sign 60 cells;
the other four remain inconclusive. The same-data direct first-jet
certificate signs all 64 cells. On every successful current cell the
extracted physical radius is less than 0.552 times the direct radius.

The direct uniform radius is greater than **0.0190407974544** in units of
sqrt(E)/Gc. The current provides **no positive full-cover radius**: its
recorded uniform value zero denotes failure of this certificate, not a
zero of the physical energy. Stop this fixed-pilot same-ball current
comparison. No independent geometric sign mechanism, smaller complete
physical error, cost advantage, new coverage or Newman bound follows.

This is a bounded quantitative comparison and a scoped same-information
inequality, not an RH-equivalent reformulation. The repository
[result summaries][summaries] and [patterns to avoid][avoid] govern its
interpretation, particularly [collision controls][controls],
[geometric realizations][geometry], [reformulations][a1],
[scope of negative results][a7], [numerics and the question][a10],
[known-box certificates][a11] and [preserving cancellation][a12].

## Reselection after the T1 closure

The [T1 note][t1] remains unchanged. Its second centered current J2c can
be strictly positive at an actual double event, and its observation is
not generically bounded in magnitude by the first-jet energy. Repeating
that sign test would not activate T2.

Instead select T1's equation (14), retaining the complete next-Laguerre
subtraction. With hj=partial_x^j H, put

\[
 a=165+4t+x^2,\qquad \beta=\frac{2tx}{a},\qquad
 \mathcal R=\mathcal L_0-\beta\partial_x\mathcal L_0,
 \quad \mathcal L_0=h_1^2-h_0h_2.
 \tag{1}
\]

The completed-current observation is exactly

\[
 \mathcal R=\frac{64}{11ta}
 \left(J_{2c}-\frac{11t^3}{16}\mathcal L_1\right),
 \qquad \mathcal L_1=h_2^2-h_1h_3.
 \tag{2}
\]

The prefactor is positive for t>0. At every double event h0=h1=0,
both L0 and its x derivative vanish, so R=0. A complete strict R>0
certificate would therefore exclude such events. This scalar is not
pointwise equivalent to L0 and is not assumed positive from L0's old
certificate. The new input is a fresh complete enclosure of h0 through
h3. It is independent of the old **sign premise**, while using the
existing physical-source evaluator; it is not a new source identity or
arithmetic constraint.

The reselection passes the estimability prerequisite by providing that
complete four-jet input. It does not retroactively change T1's failed
current-positivity gate. T2's required quantitative advantage is tested
below and fails.

On B, monotonicity gives

\[
 \frac{1001}{50108302}\le\beta\le\frac{999}{2495417}<0.0004004.
 \tag{3}
\]

The factor a is about a million. Multiplying R by a or by its current
prefactor would create a larger displayed number, rather than a better
physical allowance. All comparisons below divide by the same fixed
physical normalizer.

## Complete signed source, cross terms and primitive edges

Let ft(u)=exp(tu squared)Phi(u), with the complete even theta source.
Its fixed derivatives and polynomially weighted products are integrable
at both cusps, locally uniformly on B. Differentiation, symmetrization and
Fubini therefore give the exact physical map

\[
 \boxed{\mathcal R=\frac18\iint_{\mathbb R^2}(u+v)^2f_t(u)f_t(v)
 \left[\cos(x(u-v))+\beta(u-v)\sin(x(u-v))\right]du\,dv.}
 \tag{4}
\]

The second term is signed and retained. The Phi product is the completed
source after the algebraic subtractions in (2). If one uses C2=A2+B2
instead, all four A2A2, A2B2, B2A2 and B2B2 terms must be recombined
before integration, as proved in T1. Their separately divergent
negative-cusp transforms are not assigned finite absolute allowances.
All completed remote currents vanish.

The [primitive bridge][bridge] gives 8hj=Ij+(1/2)delta_j0. Writing
kappa=I0+1/2, the complete lower-boundary formula is

\[
 64\mathcal R=I_1^2-\kappa I_2
                  -\beta(I_1I_2-\kappa I_3).
 \tag{5}
\]

Consequently, relative to the polynomial with kappa replaced by I0,

\[
 \mathcal R-\mathcal R_{\rm bulk}
                  =\frac{-I_2+\beta I_3}{128}.
 \tag{6}
\]

Both signed lower-edge terms remain. The corner coefficient is exactly
zero after the complete subtractions; it is not discarded. The full-line
physical evaluation below implements this completed observation, not its
half-line bulk in isolation.

## Frozen acquisition and complete error

The [comparison contract][contract] was frozen before the first result.
Keep

\[
 B=[1/100,1/5]\times[999,1001],\qquad
 G_c=1000^{7/4}e^{-125\pi},\qquad V_j=h_j/G_c.
\]

Use precisely the existing S06 four-by-sixteen closed cover: time cuts
1/100+19k/400, k=0,...,4, and spatial cuts 999+k/8, k=0,...,16.
No failed cell is refined and no domain is extended.

The producer extends the original [complete contour evaluator][base]
without changing that source. Both 192- and 256-bit runs freshly acquire
midpoint orders 0 through 51, using spatial degree 24, time degree 12,
retained square modes 1 through 11, first omitted mode 12, U=2 and the
frozen contour d=pi/8-4log(1000)/1000. The fixed normalizer, contour and
cutoff are not differentiated. Every Vj for j=0,...,3 pays its own
quadrature/rounding, Taylor, omitted-mode and retained-source tail.

The extra derivative requires order 51 in the midpoint polynomial and
order 53 in the common positive moment. In particular,
j+l+2k<=3+24+24=51, and the time remainder may require
j+l+2(K+1)<=53. The majorant 1+(u+d) to the power 53 controls every
needed derivative. The [frozen-contour tail theorem][tail], equation (1),
applies to every integer j>=0; its j=3 instance is evaluated explicitly.
Its B,P and retained-source tangent conditions are rechecked through
order 53. No h3 error is borrowed from an order-two bound.

All acquisition integrals retain the original tolerances and bounded
resources: absolute tolerance 1e-13, relative tolerance 1e-30, at most
200000 integral evaluations/depth 30, and 60 seconds/two million setup
callbacks. The 52 midpoint quadratures, higher moment and all tails are
charged. Timing is diagnostic only.

Each complete interval is an outward polynomial image mj enlarged by
its component allowance epsilon_j. For

\[
 B_{ij}=|m_i|\epsilon_j+|m_j|\epsilon_i+\epsilon_i\epsilon_j,
\]

an additional explicit approximation-error ledger for
\(r=\mathcal R/G_c^2\) is

\[
 \boxed{\epsilon_r=B_{11}+B_{02}
                       +|\beta|(B_{12}+B_{03}).}
 \tag{7}
\]

On each cell, use suprema of the nominal images and beta. Polynomial
image rounding and cell variation remain in the interval images. The
actual current test uses the complete Vj balls directly, so (7) is
recorded for diagnosis and is **not subtracted a second time**.
No midpoint propagation of the current or h3 requiring an unpaid h4
bound is used.

## Matched physical observation and comparison theorem

For the normalized complete jet, define

\[
 w=(-V_2+\beta V_3,\;V_1-\beta V_2),\qquad
 r=(V_0,V_1)\cdot w.
 \tag{8}
\]

If a complete cell enclosure gives r>=ell>0 and an independently paid
M>=sup norm(w), Cauchy--Schwarz gives the physical allowance

\[
 \sqrt E/G_c\ge C:=\ell/M.
 \tag{9}
\]

The direct comparator on exactly the same Cartesian first-jet balls is

\[
 D=\sqrt{\operatorname{dist}(0,V_0)^2+
                    \operatorname{dist}(0,V_1)^2}.
 \tag{10}
\]

The reported lower endpoint is a conservative lower certificate for this
exact Cartesian minimum. Both methods
receive the same fresh four-jet data and the same cover. C is set to zero
when the strict residual sign is not certified; this is a failure marker.

There is also a **scoped same-information dominance theorem**. Let K be
the Cartesian jet/coefficient set supplied to the consumer. Choose an
allowed pair (V0,V1) attaining its least norm D, and any allowed remaining
coordinates. A residual lower bound valid on all of K and the paid upper
bound M obey ell<=r<=D M at that point. Therefore C<=D. In particular,
if both first-jet balls contain zero, a valid residual range contains zero.

This proves dominance for this scalar-to-energy extraction using the
same Cartesian data. It does not prove optimality of the original source
acquisition, a lower bound for all current methods, or impossibility of a
different coupled estimate that retains information lost by projection
to these balls. The direct comparator already wins here; sharper direct
consumers remain available. S03's 1.3898732635 reference uses a different
phase-scaled norm and is not numerically compared with (9) or (10).

## Bounded results and stopping decision

Both precision runs give:

| Quantity | Result |
| --- | --- |
| Independently signed residual cells | 60 of 64 |
| Inconclusive residual cells | The last spatial cell [8007/8,1001] in each of the four time slabs |
| Direct first-jet cells certified | All 64 |
| Positive uniform current radius | None; recorded failure value 0 |
| Uniform direct physical radius | >0.0190407974544 |
| Current/direct radius on every successful current cell | <0.552 |
| Largest complete component allowance, V0 through V3 | <5.171e-12, <4.020e-12, <3.607e-12, <3.363e-12 |
| Largest extra residual approximation allowance | <2.906e-12 |

The four failed intervals straddle zero. Their lower endpoints range
from about -0.000504 to -0.0000128. **The four failures are enclosure
failures, not negative physical residual values.** The recorded source
approximation payment is much smaller than those deficits; the two
precision runs leave all four failures in place. Cell enclosure width,
rather than a demonstrated new arithmetic sign obstruction, accounts
for this failure of the declared test.

The setup uses 177137 callbacks at 192 bits and 177241 at 256 bits;
order 51 alone uses 3441/3443 callbacks. There is no matched-cost or
speed advantage. No further mesh or source-precision adjustment is
motivated by this comparison: even a sharper valid scalar enclosure on
the same Cartesian data cannot beat its exact direct norm comparator.

The [two small records][numerics] preserve all 64 cells, exact dyadic
midpoints/radii and bound endpoints, four-component error ledgers,
normalized residuals, and per-cell current/direct comparisons.
Whitespace-compacted records have the same parsed mathematical objects
as their full pretty-printed executions. The duplicate full replays stay
outside the repository; the [review receipt][receipt] records their
identity and comparison. Hashes identify data; the arithmetic proves the
stated equalities and inequalities.

## Control screening and review

Actual event controls have h0=h1=0, so (8) gives r=0 for their own event
jets, regardless of h2,h3. A strict positive residual test therefore
rejects an event-containing domain when its input enclosure is valid.
The reflected source is convergent for the completed differential map
and fails canonical theta square arithmetic. Weighted-square controls
have their own certified events and fail full canonical reflection;
their raw theta primitive completion is not imported. Smooth shape and
positive-primitive controls screen generic sign premises without supplying
an uncomputed damping certificate. Euler's negative-Laguerre witness is
kept separate: negative L0 at a noncollision point does not force r<=0,
and no such implication is claimed.

The [separate same-model review][review] checks the complete error,
higher-order tail applicability, normalization, exact residual and
physical map, same-information theorem, source-specific controls,
invalid-input behavior and fresh replays at both precisions. This is an
internal mathematical/code review and separate execution of the author
implementation, not an independently implemented quadrature library or
specialist human assessment.

**Disposition:** T2's bounded attempt and comparison are finished;
the physical-benefit gate is not passed. The general S06 objective of
an independently useful signed arithmetic/geometric estimate remains
open. A new attempt needs a different information source, a correlated
source/current estimate or a specific cheaper complete acquisition.
The real bridge, complex exterior and EXT-01 status remain unchanged.

[t1]: 03_SECOND_TRANSVERSE_COMPLETION_AND_CURRENT_FEASIBILITY_20261019.md
[contract]: 04_S06_T2_BOUNDED_CURRENT_COMPARISON_CONTRACT_20261019.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a1]: ../../../../../../avoid/01_restating_the_target.md
[a7]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a11]: ../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[base]: ../../../numerics/high_height_consumer/high_height_consumer.py
[tail]: ../../../notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md
[bridge]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md
[numerics]: ../numerics/README.md
[review]: ../reviews/05_BOUNDED_COMPLETED_CURRENT_INTERNAL_REVIEW_20261019.md
[receipt]: ../numerics/S06_T2_INTERNAL_REVIEW_20261019.json
