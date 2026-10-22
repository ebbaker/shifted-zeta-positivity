# Endpoint charge exclusion under RH research program

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

**Purpose:** develop an independent estimate for the complete theta source
that excludes a multiple zero at heat time zero, assuming RH. The first
target is an isolated double zero. The method uses the regular two-root
discriminant equation and its complex-time charge theorem to turn signed
source information into endpoint exclusion.

This direction remains in **BW12**, as requested. Its connection to BW10
is mathematical; its notes, reviews, computations and progress stay here.
The [dedicated progress register][progress] tracks the new ECE tasks. The
[parent overview][parent-overview] and [parent register][parent-progress]
retain the broader relative-charge program and its RCH task identities.
[Assessment 07][assessment] explains the research judgment behind this
branch. No endpoint exclusion has been proved. The existing conditional
theorem and finite certificate have same-assistant reviews, not independent
specialist validation.

## First investigation update

21 October 2026, for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. [Note 07][n07] now pays the
parameterized hypothetical-double window and pointwise geometric
coverage at every finite height. [Note 08][n08] supplies a concrete
signed source-response enclosure and complete boundary/homotopy
payments. [Note 09][n09] gives the full many-root discriminant law and
its variable forcing; explicit controls rule out the naive many-root
phase/cap extension. [Review 08][r08] records internal same-model checks.

These results change the geometric and estimator prerequisites, not the
objective's open status. A positive unchanged-theta signed margin or a
strictly negative event location is still required. The program below
retains its original target and control obligations; consult the progress
register for the completed ECE-01 scope and partially paid ECE-04/05.

The signed estimator also has an actual canonical-tail specialization:
Note 08 Appendix A proves a strictly narrower discriminant interval
than the matched pointwise source envelope, with the same nonlinear
allowance. Conditional local applicability is paid; positivity of the
complete lower bound remains open. This continuation is recorded in
the endpoint progress register and Review 08.

## Selected endpoint estimate and the large time alternative

The 21 October continuation prioritizes a signed estimate at t=0, as
requested by the user. [Note 11](../notes/11_CANONICAL_QUADRATIC_RESPONSE_AND_HEAD_TAIL_CANCELLATION_20261021.md) supplies the complete
canonical quadratic estimator and quantifies the cancellation near a
hypothetical endpoint. [Note 12](../notes/12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md) rechecks infinite-time
information: current fixed-label asymptotics do not resolve the endpoint
constant, but exact Gaussian reconstruction preserves full-field
information. A useful large-time argument needs a new signed, coupled
estimate with its reconstruction errors paid. [Review 11](../reviews/11_SIGNED_RESPONSE_AND_INFINITY_TRANSFER_REVIEW_20261021.md)
records same-model internal checks. Prepared for Edward Baker with
substantial LLM assistance, gpt-6-astra, actual effort ultra. The endpoint
sign and global exclusion statuses remain open.

The finite matching-time investigation now has a [dedicated overview](03_FINITE_TIME_SIGNED_RECONSTRUCTION_PROGRAM_20261021.md) and [FTSR progress register](../research-progress/03_FINITE_TIME_SIGNED_RECONSTRUCTION_PROGRESS_20261021.md). They specify the matched signed-response comparison before any growing-time extension. The parent endpoint objective and ECE statuses are unchanged.

## Objective and classification

Use the unchanged complete theta family
\[
 H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du,
 \qquad H_t=-H_{zz},
\]
\[
 \Phi(u)=\sum_{n\ge1}
 (2\lambda_n^2e^{9u}-3\lambda_ne^{5u})e^{-\lambda_ne^{4u}},
 \qquad \lambda_n=\pi n^2.
\]
The physical position corresponding to a zeta zero
\(\rho=1/2+i\gamma\) is \(a=2\gamma\). Real heat time is denoted by
\(t\); complexifying it is an analytical device for counting events.
The real heat normalization fixes the constant 8 in the gap equation.
All charges use the complex orientation of (t,z), for which local
holomorphic intersection numbers are positive.

Under RH, the positive-time zeros are real and simple, while a multiple
zero at time zero remains possible. The desired implication is
**RH implies simplicity of every nontrivial zeta zero**. The program does
not seek to prove RH from the finite charge calculation.

Vanishing of every relevant endpoint charge is a reformulation of this
simplicity target under RH. It is stated once as the goal, not counted as
a new estimate. The admissible intermediate gains are a quantified source
bound, an independently established event location, a useful coverage
theorem, or a precise obstruction to a proposed estimate. This follows
the [target-classification rule][a01]. Consult the [result index][results],
[local heat-geometry summary][local] and [avoid index][avoid] before
extending the program.

## The exact connection to BW10

For a distinct endpoint zero of multiplicity \(m_\rho\), let \(q_\rho\)
be the local complex heat-jet charge of \(G=(H,H_z)\) at \((0,2\gamma)\).
The inherited local intersection formula gives
\[
 q_\rho=\binom{m_\rho}{2},
\]
including zero at a simple zero. With BW10's convention of summing over
distinct zeros of **both ordinate signs**, its two masses satisfy
\[
 K=\sum_\rho\frac{m_\rho^2}{|\rho|^2},\qquad
 Z=\sum_\rho\frac{m_\rho}{|\rho|^2},\qquad
 \boxed{K-Z=2\sum_\rho\frac{q_\rho}{|\rho|^2}.}
\]
The last identity is termwise bookkeeping using the finite weighted sums
in [BW10's manuscript, Section 1][manuscript]; it does not interchange
curvature limits or construct a new global Chern integral. The local
charge normalization is in [BW10 Note 25, Section 2][bw25].

This identifies the exact multiplicity excess that an endpoint exclusion
would remove from BW10's approximation and heat estimates. The weighted
sum is not an integer: a high zero has a small weight. A fixed positive
upper bound on \(K-Z\) therefore cannot use the local integer gap to
exclude all high multiple zeros.

Keep \(q_\rho\), the charge of a small endpoint neighborhood, distinct
from \(Q_B\), the total charge of a larger complex spacetime window. A
window can contain an allowed negative-time event. Charge zero on a
window containing the endpoint excludes that endpoint event; charge one
does not identify its time.

| BW10 material | Input to this direction | Obligation that remains |
| --- | --- | --- |
| [Manuscript, Sections 1 and 9][manuscript] | The weighted multiplicity excess and the missing opposing arithmetic estimate. | The charge identity supplies no upper bound. The manuscript's substantial approximation theorems are not premises of the local BW12 calculation. |
| [Note 19][bw19] | Complete exterior-root forcing, finite-time bounds and the isolated-double expansion. | On a simple real pair the coefficient below is \(A=-4S_{\rm ext}\). All exterior terms must remain present. |
| [Note 20][bw20] | Eventual shrinkage of each fixed adjacent gap. | Shrinkage toward zero only at infinite time need not produce a second finite collision. |
| [Notes 21][bw21] and [22][bw22] | Paid moving-tube observations and the universal heat-scale profile shared by matching controls. | Their profile does not distinguish theta at an endpoint. This branch can seek a different signed source quantity. |
| [Note 25][bw25] | Multiplicity-selective relative Chern/Hopf charge. | A detector becomes an exclusion only after an independent upper estimate or zero-charge argument. |

The [BW10 heat-motion overview][bw-overview] and [register][hmc] provide
the surrounding program. HMC-05 remains open and HMC-06 remains gated.
Work here can supply an alternative input to that exclusion problem
without reproducing the particular tube correction proposed there.

## The available two-root theorem

[BW12 Note 05][n05] proves the following finite-window reduction. Let
\[
 D=\{t:t_-<\Re t<t_+,\ |\Im t|<\tau\},\qquad t_-<0<t_+,
\]
and choose a real spatial center \(a\) and radii \(0<r<R\). Require
holomorphy and reality symmetry on a neighborhood of the closed product.
For every time in the closed rectangle, the outer disk must contain
exactly two roots counted with multiplicity, both in the inner disk,
with a nonzero spatial wall. These requirements allow the two roots to
coincide. They do not require an interior joint-jet floor.

Write \(H=UP\), with \(U\) nonvanishing and \(P\) monic quadratic,
and define the single-valued holomorphic discriminant
\(\Delta=(z_1-z_2)^2\). Individual root labels need not be single-valued.
Then
\[
 \Delta'=8+A\Delta,\qquad
 A(t)=\frac4{2\pi i}\oint_{|\zeta-a|=R}
       \frac{H_z(t,\zeta)-\kappa(t)H(t,\zeta)}
            {H(t,\zeta)P(t,\zeta)}\,d\zeta,
\]
where any holomorphic scalar \(\kappa(t)\) gives the same integral.
The coefficient is regular through a double zero. Its definition retains
the full exterior contribution; it is not the singular quotient
\((\Delta'-8)/\Delta\).

If \(|H|\ge\delta_{\rm wall}>0\) and
\(|H_z-\kappa H|\le L_\kappa\) on that entire outer wall, a sufficient
bound is
\[
 |A|\le M_A:=\frac{4R L_\kappa}{\delta_{\rm wall}(R-r)^2}.
\]
Here \(M_A\) denotes the coefficient bound called \(K\) in Notes 05–06;
it is unrelated to BW10's weighted multiplicity mass \(K\). No inverse
internal root gap occurs. A spatial collar and quantitative wall floor
still have to be established for the actual source.

The sufficient phase condition \(M_A\tau<\pi/2\), or the sharper
vertical phase condition in Note 05 equation (15), makes the
integrating-factor primitive injective. Every event in the window is
real, there is at most one, and each event has charge one. If the two
real cap discriminants are nonzero, all complex time-boundary events
are excluded as a consequence, and
\[
 Q_B=\frac{\operatorname{sgn}\Delta(t_+)
                -\operatorname{sgn}\Delta(t_-)}2\in\{0,1\},
 \qquad B=D\times\{|z-a|<R\}.
\]
Equal cap signs give zero; negative then positive gives one. Positive
then negative is incompatible with the hypotheses. In the endpoint
application the outgoing sign is positive; obtaining the necessary
incoming information is a separate source problem.

The exact theorem includes strict closed-boundary margins. Two spatial
counts are needed when using nested circles: count two on the inner
circle alone does not exclude an extra root in the collar. Note 05
equation (24) gives a sufficient complex-time width from independently
proved real-wall floors and complete source moments. A real-parameter
source estimate cannot be moved onto a complex wall without paying that
transfer.

## What the complete theta application establishes

[Note 06][n06] and its [interval receipt][receipt] establish the first
actual-source application without RH or a zero table as input:

| Quantity | Certified finite statement |
| --- | --- |
| Time and spatial geometry | \(\lvert\Re t\rvert,\lvert\Im t\rvert\le0.01\), center \(71/2\), inner radius 8, outer radius 10. |
| Spatial counts | Exactly two roots in each disk throughout the closed time rectangle. |
| Complete wall floors | Inner \(>8.36937\times10^{-7}\); outer \(>7.57583\times10^{-7}\). |
| Coefficient and phase | \(\lvert A\rvert<3.489078\), \(M_A\tau<0.034891<\pi/2\). |
| Real caps | Both discriminants \(>144\), from two simple real roots in disjoint sign brackets at each cap. |
| Charge | \(Q_B=0\) on the declared product. |

The calculation uses 4,146 complete source integrals, retaining omitted
modes, exterior source tails and errors over whole arcs and complex times.
It demonstrates that the theorem's conditions can be paid. The cap gaps
exceed 12, so it does not address an unknown gap tending to zero.

The coupled numerator \(H_z+(3/10)H\) improves the coefficient bound,
but the uncentered bound also passes the phase condition on this window.
That improvement was not necessary for this charge decision. Earlier
matched comparisons in [Notes 01][n01] and [03][n03] favored direct
exclusion; this application makes no new comparative-cost claim.

## The missing source information

Set \(J(0)=0\), \(J'=A\). The existing scalar equation gives
\[
 e^{-J(t)}\Delta(t)=\Delta(0)+8\int_0^t e^{-J(s)}\,ds.
\]
For every real-symmetric holomorphic coefficient \(A\), this scalar
equation admits the initial-value solution
\[
 \Delta(t)=8e^{J(t)}\int_0^t e^{-J(s)}\,ds.
\]
It has a double event at zero and positive discriminant for positive
real time. This observation concerns the scalar equation; it does not
claim that every such coefficient is realized by theta. It shows why
coefficient regularity or a tighter absolute phase bound alone cannot
exclude the endpoint. At an isolated double, the expansion is
\(\Delta=8t+4A(0)t^2+O(t^3)=8t-16S_0t^2+O(t^3)\), already present
in BW10 Note 19.

Two existing representations identify where an independent estimate
could act. Centered contour moments satisfy
\[
 S_k(t)=\frac1{2\pi i}\oint_{|\zeta-a|=R}
           (\zeta-a)^k\frac{H_z}{H}(t,\zeta)\,d\zeta,
 \qquad \Delta(t)=2S_2(t)-S_1(t)^2.
\]
Alternatively, for a positive real cap \(t_*\), define
\[
 \mathcal D(t_*)=
 e^{-J(t_*)}\Delta(t_*)-8\int_0^{t_*}e^{-J(s)}\,ds
 =\Delta(0).
\]
The latter is simply the endpoint integration constant in the preceding
identity. Its positivity is the endpoint target expressed in transport
variables, not a new independent criterion. A useful bound must derive
a positive margin from other proved complete-source information, retaining
the cancellation between its terms. Separate absolute bounds may lose
precisely the information being sought; see [the coupled-estimate
pattern][a12].

## Candidate analytical routes

**Incoming-cap sign.** Prove \(\Delta(t_-)>0\) from the complete source
on an admissible negative cap, with \(\Delta(t_+)>0\) at the outgoing
cap. The charge theorem then gives zero. The contour moments allow this
question to be posed without choosing individual complex root labels.
The estimate must not assume two distinct real incoming roots or an
endpoint gap floor in order to prove the desired sign.

**Negative-time event location.** Independently establish an event on
a strictly negative-time subinterval of the same proper phase-controlled
window. Its at-most-one count then excludes another event at zero. A
charge-one result on a window straddling zero does not supply this
location. Any source or numerical enclosure must leave a strict positive
distance between the event-time enclosure and zero.

**Control of the endpoint integration constant.** Derive a coupled
source bound for \(\mathcal D(t_*)\), or an equivalent expression, with
a proved positive remainder margin. The outgoing discriminant and the
integrating factor have to be controlled together. Merely deriving the
identity above, or a bound also satisfied by a collision, does not meet
this target.

These are alternative ways to supply the missing signed information;
success in all three is unnecessary. The first research round should
select one expression after a control and error audit. Retain complete
theta data in \(H\), the exterior contribution in \(A\), and the source
correlations in \(H_z-\kappa H\). Positive moment bounds remain useful
for errors and wall transfer, but do not by themselves determine a cap
sign or the endpoint integration constant.

## Controls and interpretation

The [control register][controls] and [matched-premise rule][a02] apply
to the actual proposed inequality, not just to its notation. A source
can fail the literal theta formula and still satisfy an inequality
derived from it. Naming the missing arithmetic premise is therefore
necessary but does not establish quantitative separation.

| Control | Required response of this program |
| --- | --- |
| \(H=z^2-2t\) | Proper two-root geometry and phase control hold, but \(\Delta=8t\), \(A=0\), and the crossing charge is one. A claimed zero-charge estimate must fail its sign premise. |
| Shifted quadratic controls in Notes 05–06 | The positive/positive and negative/negative cap cases have charge zero. A valid method can accept a collision-free control window. |
| Cubic and higher Hermite births | A window containing the whole birth fails the two-root contract. Omitting the additional roots is not a multiplicity reduction. |
| [BW10 close normalized endpoint sources][bw05] | Under RH they can have an endpoint double and simple all-real positive-time zeros while remaining arbitrarily close in the stated source norm. Ordinary Dirichlet-series arithmetic fails; a fixed source-distance tolerance alone cannot separate them. |
| Euler-factor controls | Euler data change. Positivity, evenness and the heat equation still do not determine the desired sign. |
| Weighted-square and finite-prime controls | The unchanged normalized coefficient/reflection conjunction fails. These controls must not be assigned an all-real heat slice that they do not possess; local analytic comparisons remain meaningful. |
| Reflected, smooth and positive-primitive controls | Their separately recorded shared properties do not impose the canonical theta square expansion. Preserve each family's actual hypothesis list when comparing it. |
| Fixed-event atomic controls | Complete moment upper budgets and selected imaginary-axis floors can coexist with a genuine all-real threshold event. These controls fail canonical theta arithmetic, the full profile and eventual simplicity at the threshold. |

Near ordinary double events, matching analytic controls can satisfy the
wall and phase hypotheses and correctly retain charge one. Their source
values are not the measured values of the finite theta application. A
new estimate must state which quantitative conclusion fails on each
relevant collision domain, or explain why its hypotheses are inapplicable.
The previous screening results are scoped to their retained information;
they do not exclude every future theta-specific argument. See
[scope][a07] and [hypothesis auditing][a14].

## From a local double result to the full target

**Height coverage.** An estimate for a declared low pair is a bounded
result. A proof needs a quantified procedure covering every endpoint
height, with dependence on wall floors, exterior separation, time widths
and error budgets stated. Height-dependent local windows are allowed;
a single universal positive gap or wall floor is not an assumed input.
The close endpoint controls specifically warn against a fixed positive
source-tolerance argument at all heights.

A common negative-time slice with every theta zero real is unavailable:
the threshold property together with the proved \(\Lambda\ge0\) rules
it out. Separate local windows may have negative caps depending on the
height and cluster. This is a consequence of [Rodgers and Tao's
theorem][rt], not an obstruction to such local windows.

**Higher multiplicities.** At an \(m>2\) birth, a selected outgoing pair
does not form a proper isolated two-root cluster through time zero.
The other birth roots contribute singular exterior terms, as BW10
Note 19 RM17 records. A many-root discriminant theorem, or a separately
justified reduction preserving the relevant source estimate and charge,
must retain those roots. The inherited local charge \(\binom m2\)
supplies the detector but not the new exclusion bound.

**Assembly.** The cleanest intended endpoint argument is local: cover
each hypothetical endpoint event by an admissible neighborhood and
exclude it. A global exhaustion is optional and would require its own
boundary and convergence proof. Allowed negative-time events must remain
distinct from the endpoint charges in the weighted identity. No
cancellation between positive local holomorphic charges is available.

## Work sequence and completion requirements

1. **Make the next window and source observable precise.** State which
   endpoint hypotheses are conditional, which walls and counts are paid,
   and which constants stay regular as the internal gap tends to zero.
   The contract must admit the ordinary-double control.
2. **Prove and screen one signed estimate.** Specify a cap margin, an
   event-time separation from zero, or an explicit lower bound for the
   endpoint integration constant. Give its complete error and tail
   payments and the control response. This is the immediate substantive
   research priority.
3. **Apply the charge theorem with its full boundary contract.** State
   exactly which isolated double endpoints are excluded. A bounded
   exclusion is not promoted to arbitrary height by notation.
4. **Address height and multiplicity coverage.** Keep these as separate
   obligations so that success in the two-root problem does not conceal
   the many-root gap.
5. **Review the assembled implication.** Audit the source estimate,
   normalization, boundary orientation, quantifiers and retained exterior
   terms. Preserve the distinction between internal LLM assessment and
   independent specialist review.

The [progress register][progress] assigns ECE task identifiers and records
the evidence required to change their status. A new numerical run should
answer one specified unresolved question with a predeclared geometry,
precision, source budget and stopping condition. Repeating a charge-zero
certificate for another known separated pair would extend bounded
coverage, not meet the endpoint-sign objective. Numerical speed remains
a separate possible benefit, not a condition for analytical continuation.

New derivations belong in this investigation's notes/, assessments in
reviews/, and computations with small replay records in numerics/.
Preserve the [existing chat registration][history] and the
[large-file policy][large]. Record substantive milestones in
[DRAFT_HISTORY.md][draft-history]; create no manuscript snapshot folders.

[progress]: ../research-progress/02_ENDPOINT_CHARGE_EXCLUSION_PROGRESS_20261021.md
[parent-overview]: 01_RELATIVE_CHERN_HOPF_CHARGES_PROGRAM_20261021.md
[parent-progress]: ../research-progress/01_RELATIVE_CHERN_HOPF_CHARGES_PROGRESS_20261021.md
[assessment]: ../reviews/07_BW10_INTEGRATION_AND_PROOF_DIRECTION_ASSESSMENT_20261021.md
[n01]: ../notes/01_BOUNDED_THETA_CHARGE_AND_DIRECT_COMPARISON_20261021.md
[n03]: ../notes/03_TWO_ZERO_THETA_BOUNDARY_AND_DIRECT_COMPARISON_20261021.md
[n05]: ../notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
[n06]: ../notes/06_COMPLETE_THETA_WALLS_AND_REAL_CAP_APPLICATION_20261021.md
[receipt]: ../numerics/REAL_CAP_THETA_APPLICATION_20261021.json
[manuscript]: ../../10_rh_implies_simple_zeros/manuscript/main.tex
[bw-overview]: ../../10_rh_implies_simple_zeros/research-overview/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRAM_20261021.md
[hmc]: ../../10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[bw05]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[bw19]: ../../10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[bw20]: ../../10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[bw21]: ../../10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[bw22]: ../../10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[bw25]: ../../10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
[rt]: https://arxiv.org/abs/1801.05914
[history]: ../chat-histories/0002_2026-10-21T19-24-03Z_continue-chern-hopf-charge-research.json
[large]: ../../../../../../../LARGE_FILES.md
[draft-history]: ../DRAFT_HISTORY.md
[n07]: ../notes/07_QUANTITATIVE_ENDPOINT_WINDOWS_AND_HEIGHT_COVERAGE_20261021.md
[n08]: ../notes/08_SIGNED_DISCRIMINANT_RESPONSE_AND_EVENT_DISPLACEMENT_20261021.md
[n09]: ../notes/09_MANY_ROOT_DISCRIMINANT_FLOW_AND_CAP_LIMITS_20261021.md
[r08]: ../reviews/08_ENDPOINT_CHARGE_OPENING_ROUND_REVIEW_20261021.md
