# Assessment of the connection to BW10 and the proof direction

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.
Same-assistant mathematical assessment; no independent specialist review.

**Judgment:** BW12 now warrants a focused analytical branch within the
BW10 heat-motion program. It has a usable scalar reduction, explicit
source payments and a successful finite theta application. These are
substantive reasons to prioritize further work on it among the geometric
approaches reviewed here. They do not establish superiority over every
other route, computational superiority, or proximity to a simplicity
proof. The missing arithmetic sign remains the decisive obligation.

This assessment compares [BW12 Notes 05][n05] and [06][n06] with the
[BW10 manuscript][manuscript], [heat-motion register][hmc], and Notes
[19][motion], [21][tube], [22][profile] and [25][charge]. It does not
upgrade their internal review status. See the [result index][results],
[local geometry cluster][local], [control register][controls] and
[avoid index][avoid], especially [target classification][a01],
[matched premises][a02], [scope][a07] and [hypothesis audit][a14].

## 1. The charge measures exactly the manuscript's endpoint excess

Under the manuscript's RH hypothesis, let rho=1/2+i gamma range over
**distinct** nontrivial zeros of both signs, with multiplicity m_rho.
Let q_rho be the local complex heat-jet charge at (0,2 gamma), and set
q_rho=0 at a simple zero. The inherited local multiplicity formula gives
\[
 q_\rho=\binom{m_\rho}{2}.
\]
The manuscript defines
\[
 K=\sum_\rho\frac{m_\rho^2}{|\rho|^2},\qquad
 Z=\sum_\rho\frac{m_\rho}{|\rho|^2}.
\]
Termwise substitution therefore gives
\[
 \boxed{K-Z=2\sum_\rho\frac{q_\rho}{|\rho|^2}.}                  \tag{1}
\]
Finiteness is inherited from the manuscript's multiplicity-weighted
zero-count bound. No interchange of regularized curvature integrals or
new global Chern integral is used. Equivalently, for physical heights
x=2 gamma of both signs, the weight is 8/(1+x^2).

Thus BW10's weighted multiplicity excess and BW12's local charges measure
the same endpoint defect. Equation (1) is an exact bookkeeping bridge,
not an opposing upper bound or a new simplicity criterion. The local
integer gap does not make the weighted sum an integer: high endpoint
charges have small weights. An arbitrary fixed positive upper bound on
K-Z would not exclude every sufficiently high multiple zero.

Also q_rho is an **endpoint-local** charge. It must not be confused with
the total Q_B of a larger spacetime window, which may include an allowed
negative-time event. Q_B=0 excludes all endpoint events inside; Q_B=1
does not by itself place the event at time zero.

## 2. What the two-root theorem contributes

| BW10 component | BW12 addition | Remaining qualification |
| --- | --- | --- |
| Real root motion and complete exterior tails | The same gap equation extends as Delta'=8+A Delta with A holomorphic through an isolated double. | On a simple real pair A=-4 S_ext; this is not a new real root equation. |
| Relative Chern/Hopf detector in Note 25 | A phase-controlled theorem bounds the full complex event count by one and reduces it to real cap signs. | A detector has become an applicable finite theorem, but the phase bound allows charge one. |
| Moving tubes and heat-scale trace profiles | A contour estimate for the exterior coefficient avoids dividing by the vanishing internal gap or an interior physical energy floor. | Exterior separation and spatial wall floors must still be proved. No height-uniform floor follows. |
| Complete-source signed estimate sought in HMC-05 | One finite set of wall, phase and cap data is now interval-certified for actual theta. | The certified cap gaps exceed 12; it does not treat an unknown shrinking endpoint gap. |

The real root law has the normalization used in
[Polymath, Proposition 3.1][polymath]. BW12's added work is the analytic
exterior coefficient, complex-time phase argument and paid source
application. This makes it a useful extension of HMC-01 and Note 25,
and a possible alternative way to discharge HMC-05's exclusion need.
It need not reproduce the particular tube correction proposed in HMC-05.
It must nevertheless supply its own independently established sign.

In the earlier matched finite implementations direct exclusion was
stronger and cheaper. Note 06 made no matched cost claim. The favorable
research judgment here concerns analytical structure and tractability,
not a reversal of those comparisons or a ranking of every sibling route.

## 3. Why regularity of A does not yet give endpoint exclusion

On a proper two-root window choose J'=A and a real base point. The
integrating factor gives
\[
 e^{-J(t)}\Delta(t)
 =e^{-J(t_*)}\Delta(t_*)+8\int_{t_*}^t e^{-J(s)}\,ds.             \tag{2}
\]
Bounds on A control the transport and, with the phase condition, its
injectivity. They do not by themselves determine the integration constant.
At the scalar ODE level, every real-symmetric holomorphic A admits the
initial-value solution
\[
 \Delta(t)=8e^{J(t)}\int_0^t e^{-J(s)}\,ds,
 \qquad J(0)=0.                                                 \tag{3}
\]
It has Delta(0)=0, Delta'(0)=8 and Delta(t)>0 for positive real t.
Under the phase hypothesis it has just the allowed real event at zero.
This is a scoped observation about the scalar equation, not a claim
that every such A is realized by the complete theta source.

At an isolated double, A(0)=-4 S_0 and (3) gives
\[
 \Delta(t)=8t+4A(0)t^2+O(t^3)
          =8t-16S_0t^2+O(t^3),                                 \tag{4}
\]
exactly BW10 Note 19's endpoint expansion. A bound on this coefficient
that the matching controls also satisfy would not supply a new exclusion.
The signed source information must constrain the actual solution of (2),
including its constant or its event location, rather than only regularize
the universal event profile.

The three quadratic controls from Note 06 make this distinction concrete:
the same wall and phase consumer permits charges 1,0,0. The event case
fails equal nonzero cap signs. Near their ordinary double events the
broader source controls can also satisfy the local analytic theorem;
they are not assigned the theta application's measured source values.
Euler factors change Euler data; weighted-square and finite-prime
controls fail the unchanged normalized coefficient/reflection conjunction;
reflected and smooth/primitive controls lack the canonical source; BW10's
close positive endpoint controls fail ordinary Dirichlet-series arithmetic.
These different failures must not be combined into one preservation list.

## 4. A concrete place in a proof program

For an isolated endpoint double under RH, the outgoing real pair is
simple and has positive discriminant. In a properly isolated window
with the phase condition, either of the following independently proved
inputs could finish the local exclusion:

- a positive incoming discriminant at a negative cap, giving zero
  total charge by the theorem;
- an already established event on an entirely negative-time subinterval,
  using up the at-most-one count and excluding an additional endpoint event.

These are receiving specifications for a source estimate, not newly
proved theta inequalities or new independent criteria. The first must
not assume real distinct incoming roots as a premise at the very place
where their reality is to be proved. The second needs actual event
location, not only a charge-one count on a window straddling zero.

The window sizes can depend on height and cluster geometry. A common
negative-time slice with *all* theta zeros real is unavailable:
[Rodgers–Tao][rt] proves Lambda>=0, whereas all-real zeros at a negative
time would imply Lambda<0 by the defining threshold property. This
prevents an overly strong global incoming-cap target. It does not
prevent separate height-dependent negative-time neighborhoods of
individual simple endpoint zeros.

Higher multiplicities require a further theorem. At an m>2 birth a
chosen pair does not form a proper isolated two-root cluster through
time zero; the remaining birth roots destroy that collar, as BW10
Note 19 RM17 already records. One cannot infer all-multiplicity simplicity
by applying the two-root result to every adjacent outgoing pair. A
many-root discriminant or another justified reduction must retain all
these roots and their positive charges.

Nor does HMC-02's eventual gap shrinkage supply a second finite event.
A gap may increase from zero, have a positive maximum and approach zero
only at infinite time. Combining that behavior with an at-most-one
finite-event theorem gives no contradiction.

## 5. Research recommendation

Prioritize a bounded analytical investigation of the actual source
sign in a window that remains valid through a possible double. Retain
the complete exterior contribution and the source correlations in the
contour numerator. The next accepted milestone should be a new signed
bound or location estimate that a matching collision control fails for
a named reason. Another charge-zero certificate around a known separated
pair would validate coverage, but would not meet that near-event goal.

The existing result supports a plausible boundary-charge proof route
that could bypass forcing a later positive-time collision. It has not
yet demonstrated a mechanism that does so for theta. HMC-05 and RCH-07
remain open, HMC-06 remains gated, and arbitrary-height/multiplicity
coverage remains separate work. The weighted identity (1) gives a clear
interface to the main BW10 manuscript without importing that manuscript's
substantial approximation theorems as premises of the local charge
calculation.

[n05]: ../notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
[n06]: ../notes/06_COMPLETE_THETA_WALLS_AND_REAL_CAP_APPLICATION_20261021.md
[manuscript]: ../../10_rh_implies_simple_zeros/manuscript/main.tex
[hmc]: ../../10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[motion]: ../../10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[tube]: ../../10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[profile]: ../../10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[charge]: ../../10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a14]: ../../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
[polymath]: https://arxiv.org/html/1904.12438v2#S3
[rt]: https://arxiv.org/abs/1801.05914
