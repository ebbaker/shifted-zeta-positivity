# A possible contraction of nonreality under Jacobi refinement

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and reasoning effort
are unavailable in the recorded configuration.

**Research overview; canonical contraction unproved and setup deferred.**
This document identifies a route and its missing input. It is not a
research plan, live register, or executed proof task. Parent discussion28
has same-assistant checking only.

## Scientific question and fixed setting

Can adding canonical Jacobi coefficients force the nonreal part of an
identified Fourier-zero cluster toward zero, with an error smaller than
the restoring contribution? This would strengthen approximation to a
statement about the geometry of the limiting field.

At fixed real physical heat time lambda, initially in [0,1/2], retain

\[
F_\lambda(z)=\frac{\int_{\mathbb R}e^{\lambda u^2}\Phi(u)e^{izu}\,du}
 {\int_{\mathbb R}e^{\lambda u^2}\Phi(u)\,du},\qquad
G_{N,\lambda}(z)=(e^{izJ_N(\lambda)})_{00},
\]

with the complete theta source and its canonical N-site Jacobi matrix.
No Jensen-polynomial replacement or changed observation kernel is part
of the route. The zeros of the orthogonal polynomial q_N are source
nodes; their interlacing and the phase arg(q_(N-1)+i q_N) do not count
the zeros studied here.

Fix a conjugation-symmetric contour that isolates two F zeros, counted
with multiplicity, and has a positive boundary modulus. For sufficiently
large N, a strict boundary comparison identifies the corresponding
two-zero G_N cluster. Contour moments supply c_N,D_N and c,D with

\[
D=((z_1-z_2)/2)^2,\qquad |D_N-D|\le d_N\longrightarrow0.
\]

See [manuscript §10.4](../../manuscript/sections/cluster_resolution.tex)
and [note27](../../notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md).
The contour, its count and its margin are genuine premises. Refinement
does not identify a cluster across arbitrary contour changes for free.

## Available results and the proposed extra estimate

[Synthesis23](../../notes/23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md)
records the internally accepted complete signed error representation,
phase estimate and equal-prefix comparison. The fixed-simple-zero
corollary in [note26](../../notes/26_VCD_FIXED_ZERO_STABILIZATION_AND_PHASE_20261116.md)
gives an alternating displacement with shrinking ratio for a chosen
simple real limiting zero. It is conditional on that zero and is not
uniform over increasing zero index or near a multiple zero.

For a two-zero model cluster define

\[
u_N=(-D_N)_+=\max(0,-D_N).
\]

When D_N<0, this is the square of the imaginary half-separation. A
candidate induction is

\[
u_{N+1}\le(1-a_N)u_N+e_N,\qquad
0<a_N\le1,\quad e_N\ge0,\quad
\sum_N a_N=\infty,\quad e_N/a_N\longrightarrow0.
\]

These conditions force u_N->0 and hence D>=0. For any epsilon>0,
eventually e_N<=epsilon a_N; then (u_N-epsilon)_+ contracts by the
product of 1-a_N, which tends to zero. This elementary implication is
in [discussion28 §3](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md).
The canonical inequality itself is **not established**.

One may instead compare N with N+2, or an explicitly selected subsequence,
if the parity of the signed error makes that the appropriate step.
The same divergent-gain and smaller-error requirements would apply along
that subsequence. The known alternating displacement does not prove such
a contraction. A summable sequence of gains can leave an initial defect,
and arbitrarily rapid convergence can converge to a nonreal pair.

## Where a substantive lemma would have to enter

Contour increments of log(G_(N+1)/G_N), on a justified zero-free collar,
give exact increments of cluster moments and hence D_N. This is a
starting representation. A useful estimate must extract a restoring
signed contribution from the **actual canonical update**, and pay its
complete tail and any change in contour or degree-dependent information.
Bounds only on the absolute increment do not supply that sign.

Possible decisions for later planning include one-degree versus
two-degree comparison, and whether to use the exact update directly or
a correction whose cost is compared with the next physical head.
These are unresolved choices, not active tasks. The parent E24
equal-prefix comparison must be retained when a correction consumes an
additional coefficient. E08's full-score source characterization does
not by itself provide a conditioned quantitative gain; E07's finite-data
controls and E10's smooth next-defect freedom keep their distinct scopes.

A successful bounded return could identify a genuine signed update
estimate with nonvacuous gain/error conditions, or show precisely why a
specified information class cannot do so. Restating limiting reality as
an induction hypothesis is not a result.

## Classification and analytical control screen

Read the [result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and [approximation18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md);
also the [avoid index](../../../../../avoid/README.md), specifically
[01](../../../../../avoid/01_restating_the_target.md),
[02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[03](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[13](../../../../../avoid/13_a_factor_is_not_the_target.md), and
[14](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md).

The induction is a sufficient conditional mechanism. Demanding such
control for an exhaustion of all clusters would reach the full reality
target; no numerical support for that global assertion is proposed.
The complete inherited screen is [discussion28 §5](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md).

On any colliding control's earlier slice with an isolated conjugate
pair, a convergent model has u_N->-D>0. Consequently the proposed
inequality and its gain/error conditions cannot all hold there. This is
a logical test of the mechanism, not a measured failure of a particular
canonical update estimate. Weighted-square controls fail full reflection;
reflected/smooth positive controls fail unchanged theta arithmetic;
Euler-factor controls change ordinary Dirichlet coefficients; finite
head/prime/score controls fail the full source identities despite matching
selected data. Those distinctions do not automatically give the needed
sign for theta. Atomic models have terminating chains and do not furnish
an infinite-degree test; continuous controls retain their stated scope.
Finite-profile threshold controls fail full arithmetic/profile premises.
RH-conditional endpoint controls fail ordinary Dirichlet arithmetic and
retain their RH assumption. Changed kernels and abstract profile
relaxations fail the physical-observation and actual-field premises.
No control certificates were rerun, and smooth next-defect freedom is not
upgraded to a collision theorem.

The proposed conclusion D>=0 allows a double real zero. Excluding an
interior heat collision would require application on both time sides;
reality at one endpoint is not simplicity. Clusters containing more
than two zeros need additional symmetric coordinates, and all-height
coverage needs separate bounds. The source moment Gram matrix is not a
positivity certificate for these Fourier-zero coordinates.

## Ownership and later setup

This branch owns degree induction at fixed physical time, using future
prefix VCD-NC. It does not move parent VCD-B07/E25 or duplicate their
status. [Gap transport](../../01_cluster_gap_transport/README.md) owns
physical-time transport; [multiscale bounds](../../03_multiscale_collision_bounds/README.md)
owns an averaged alternative. Shared theory stays in the parent.

Reuse the [parent reference catalog](../../references/README.md) and
[bibliography](../../references/induction.bib); this opening imports no
new external theorem or literature inspection. When Edward starts this
route, write its bounded plan and sole progress register before research
execution, classify its conceptual and fixed tasks, and record the
specific signed estimate to be tested. Numerical evidence, if later
authorized for a bounded question, remains supporting evidence.
