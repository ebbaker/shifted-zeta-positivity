# Averaged collision bounds across approximation scales

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and reasoning effort
are unavailable in the recorded configuration.

**Research overview; canonical averaged estimate unproved and setup
deferred.** The inherited local calculations have same-assistant checking
only. No plan, progress register, research execution or numerical
campaign is created by this overview.

## Question and fixed objects

Can the complete source bound the total contribution of near-collisions
over heat time more sharply than a genuine collision permits? The aim
is to identify a useful averaged estimate, rather than require a
pointwise separation bound at every resolution.

Keep the complete canonical source and its physical readouts:

\[
F_\lambda(z)=\frac{\int_{\mathbb R}e^{\lambda u^2}\Phi(u)e^{izu}\,du}
 {\int_{\mathbb R}e^{\lambda u^2}\Phi(u)\,du},\qquad
G_{N,\lambda}(z)=(e^{izJ_N(\lambda)})_{00}.
\]

Initially fix a compact heat-time interval I within [0,1/2] and a
real-centered contour enclosing exactly two F zeros, with a uniform
positive boundary modulus. Define the squared half-separation D and
its contour-moment approximation D_N as in
[manuscript §10.4](../../manuscript/sections/cluster_resolution.tex).
Take a positive uniform error allowance d_N->0 with |D_N-D|<=d_N
throughout I. Degree N changes the resolution, while lambda changes
the actual physical field. No exact physical heat equation is imposed
on the moving finite readout G_N.

## Known local behavior and candidate averaged estimate

[Note27](../../notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md)
records the conditional cluster approximation and the exact double-event
slope D'(T)=2. Hence, at an isolated interior double event,

\[
D(\lambda)=2(\lambda-T)+O((\lambda-T)^2).
\]

The unresolved time set |D_N|<=d_N has width O(d_N) locally. Such a
shrinking set is consistent with a genuine collision and does not
exclude one.

The starting observable from
[discussion28 §4](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md)
is

\[
Q_N=\int_I\frac{d\lambda}{|D_N(\lambda)|+d_N}.
\]

If |D(lambda)|<=C|lambda-T| for |lambda-T|<=delta inside I, then

\[
Q_N\ge\frac2C\log\left(1+\frac{C\delta}{2d_N}\right).
\]

Indeed |D_N|+d_N<=|D|+2d_N on that interval. The lower bound is an
elementary conditional consequence of the local event law; it is not
an assertion that a canonical event exists.

It follows that an independent estimate

\[
Q_N=o\!\left(\log\frac{r_0}{d_N}\right)
\]

for fixed r_0>0 would exclude such an event in this fixed tube. A
uniform upper bound for Q_N would suffice. Conversely, if D has no zero
on the compact interval, its positive minimum modulus makes Q_N bounded
for all sufficiently large N. Thus the proposed bound is a local
noncollision criterion, not evidence that the source satisfies it.
A pair that stays nonreal throughout I also has bounded Q_N; an
independent real incoming anchor is necessary to infer reality.

## What additional information is needed

The logarithm reflects the accumulation of contributions from successive
scales of small separation. A useful proof must limit that accumulation
using information beyond local analyticity, the heat equation and
approximation accuracy. Possible sources of such an estimate include a
controlled signed energy balance with paid boundary terms, or a
canonical bound for the time spent in successive separation ranges.
Neither mechanism is selected or established here.

Any proposed scale decomposition must retain the entire positive
observable, its cutoffs and the resolution error. An O(d_N) occupation
bound at the finest unresolved scale is insufficient. Bounds valid only
at a fixed distance from a hypothetical collision are also insufficient.
Changing or enlarging the tracked cluster requires count bookkeeping;
one cannot omit difficult subintervals or double-count clusters and
still claim a bound for Q_N on the original interval.

The parent signed error results in
[synthesis23](../../notes/23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md)
control approximation, not this reciprocal observable's denominators.
The [gap-transport sibling](../../01_cluster_gap_transport/README.md)
could eventually supply a useful signed balance, but its missing source
estimate is not an available input. The
[degree-contraction sibling](../../02_degree_nonreality_contraction/README.md)
asks a different question at fixed heat time.

## Prior energy work and the scope of a possible gain

Read the Rodgers–Tao branch
[note02 §§3–7](../../../../investigations-5/02_heat_flow_rh_applications/rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md)
and [note03](../../../../investigations-5/02_heat_flow_rh_applications/rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md).
Their ordered two-root energy is 2/(z_2-z_1)^2=1/(2D) on a real
simple pair. The exact quadratic heat control has energy proportional
to 1/(lambda-T), despite regular exterior drift and excellent contour
approximation. Q_N regularizes the corresponding divergence; it is not
identical to that energy and must not inherit its estimates without
checking normalization, signs and time domains.

The finite canonical pilot is **interval-certified** on its stated
compact family, with no new zero coverage or uniform endpoint bound.
The corrected literature argument consumes additional hypotheses and
specific truncated/renormalized energies. None is silently identified
with Q_N. Reference ownership and inspected passages stay in the
[parent catalog](../../references/README.md) and its linked Rodgers–Tao
records. This setup reuses those records and performs no new inspection.

A substantive return would give a justified canonical upper estimate
beating the logarithmic event scale under independently checkable
premises, or a scoped obstruction to a specified estimating method.
Deriving another event detector or verifying the quadratic scaling again
does not supply that upper estimate.

## Classification and collision controls

Use the [result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and [approximation18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md);
also the [avoid index](../../../../../avoid/README.md), especially
[01](../../../../../avoid/01_restating_the_target.md),
[02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[03](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and
[14](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md).

The local logarithmic lower bound and the conditional exclusion are
inherited calculus. The upper estimate is unproved. Requiring successful
collision exclusion over every height and relevant time, together with
the necessary anchoring/coverage, would repackage the global reality
objective; finite checks do not support that unquantified assertion.

Apply the full analytical screen in
[discussion28 §5](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md).
For an isolated double event in any actual control field admitting the
stated approximation, the displayed logarithmic lower bound applies,
so the proposed sublogarithmic upper estimate fails on that event tube.
This is a consequence of the event, not a numerical control rerun.
The polynomial model lacks a positive canonical source. Weighted-square
controls lack full reflection and any finite all-real global anchor;
reflected/smooth positive controls lack unchanged theta arithmetic.
Euler-factor controls alter ordinary Dirichlet coefficients and their
threshold certificate is not itself a specified local double event.
Finite-profile threshold controls lack full arithmetic/profile premises;
atomic ones do not support an infinite Jacobi refinement, while their
continuous extensions retain the stated source-specific scope. Finite
prime/head/score controls lack full canonical identities; smooth
next-defect freedom alone is not a collision assertion. RH-conditional
endpoint controls retain RH and fail ordinary Dirichlet arithmetic;
endpoint simplicity is a separate target. Changed kernels or abstract
profile relaxations fail the physical heat/observation or actual-field
premise. Merely noting these absent theta identities does not establish
the desired upper estimate for theta.

## Later setup and boundaries

Future tasks use VCD-MC and receive a sole branch register when Edward
starts this route. Parent VCD-B07/E25 retain their present ownership.
Planning must select a concrete averaged estimate, its complete inputs,
time domain, boundary terms and meaningful comparison before assigning
an execution task. Higher-multiplicity clusters, endpoints and increasing
heights need separate treatment; no finite global first event is assumed.
Analytical work is primary, with any bounded computation serving a
predeclared supporting question.
