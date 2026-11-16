# Signed gap transport for unresolved zero clusters

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and reasoning effort
are unavailable in the recorded configuration.

**Research overview; canonical signed estimate unproved.** Edward has
selected this route for the first setup session. A research plan and
progress register are deliberately deferred. The inherited local
calculations have same-assistant checking, not specialist validation.

## Question and ownership

Can the complete theta source relate an incoming real pair's separation
to its subsequent exterior interaction strongly enough to preserve
reality when physical heat time is decreased? The useful regime includes
clusters that can be counted on an outer contour even when individual
roots and root slopes cannot yet be separated.

This branch owns that physical-time question. The
[parent discussion28](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md)
owns the common comparison of routes; the siblings own
[degree contraction](../../02_degree_nonreality_contraction/README.md)
and [multiscale bounds](../../03_multiscale_collision_bounds/README.md).
Parent VCD-B07/E25 retain their recorded status. Future task IDs here use
VCD-GT; they will receive a sole branch register when planning begins.

## Fixed objects and inherited evidence

Keep the complete canonical source and literal Fourier observation:

\[
W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
Z_\lambda=\int_{\mathbb R}W_\lambda(u)\,du,\qquad
F_\lambda(z)=Z_\lambda^{-1}\int_{\mathbb R}W_\lambda(u)e^{izu}\,du,
\qquad G_{N,\lambda}(z)=(e^{izJ_N(\lambda)})_{00}.
\]

Here J_N is the N-site canonical Jacobi truncation. Its eigenvalues are
source quadrature nodes, not zeros of F. The parent
[manuscript](../../manuscript/README.md) supplies the normalization,
coefficient bounds and signed quadrature error. In particular,
[synthesis23](../../notes/23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md)
records the reviewed E21/E22/E24 error results; those estimates alone do
not supply the canonical model margin or zero count.

Initially fix I=[u,v] within [0,1/2], a real-centered circle Gamma with
uniform positive boundary modulus, and exactly two enclosed F zeros,
counting multiplicity. Their coordinates are

\[
c=(z_1+z_2)/2,\qquad D=((z_1-z_2)/2)^2.
\]

Conjugation symmetry makes c,D real. D>0 means distinct real zeros,
D<0 a nonreal conjugate pair, and D=0 a real double zero. No reality
throughout I is built into the cluster hypothesis. Count and boundary
margin must be supplied, not inferred from approximation accuracy.

[Manuscript §10.4](../../manuscript/sections/cluster_resolution.tex),
Propositions 10.4–10.6, gives uniform compact approximation, contour
coordinate bounds |D_N-D|<=d_N->0, and D'(T)=2 at an isolated double
event. These are conditional local analytical statements. Increasing N
improves resolution at fixed lambda; it does not change the physical
field. G_N is not assumed to satisfy the exact heat equation of F.

## The transport identity and the missing estimate

On the isolated cluster neighborhood write

\[
F_\lambda(z)=((z-c)^2-D)A_\lambda(z),\qquad
h_\lambda=A_{\lambda,z}/A_\lambda,
\qquad
K=\frac{h_\lambda(c+\sqrt D)-h_\lambda(c-\sqrt D)}{2\sqrt D}.
\]

A is holomorphic and nonvanishing. The divided difference extends to
K=h_z(c) when D=0. The exact equation
F_lambda=-F_zz-m2 F and differentiation at a simple root give
r'=F_zz/F_z. Subtracting the two velocities proves

\[
D'=2+4KD.
\]

The symmetric expression extends through a double event. Its derivation
and relation to the pre-existing local force identity are in
[discussion28 §2](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md).
No global all-real exterior population is required.

With W(t)=exp(4 integral_t^v K(s) ds), integration gives

\[
W(u)D(u)=D(v)-\mathcal C(u,v),\qquad
\mathcal C(u,v)=2\int_u^v W(t)\,dt.
\]

Thus an independently acquired lower bound L_v<=D(v) and upper bound
B>=C(u,v), with L_v>B, preserve positive D throughout I. Equality
allowed at the left endpoint preserves D(u)>=0 without demanding
endpoint simplicity. A constant K<=M gives the sufficient payment
(exp(4M(v-u))-1)/(2M), interpreted as 2(v-u) for M=0.

**The open estimate is a useful canonical comparison between L_v and
the complete signed interaction cost.** Bounded K alone is insufficient.
Absolute value bounds can discard the cancellation needed for this
comparison. A sequence of arbitrarily small successful time steps does
not establish that the total descent reaches zero.

The most relevant possible inputs are a relation between the incoming
gap and the variation of the exterior drift, or a signed integral
estimate derived from the complete source/score identities. Neither is
presently proved. All-degree source identification is not a quantitative
bound for this cost; source positivity and the coefficient envelope are
shared with collision controls.

## What can be reused, and what would count as a gain

The contour projection of F_z/F extracts h, and a second divided
difference extracts K without an inverse internal gap. If the outer
contour length is L, its distance from an inner convex region is b>0,
and |log(F/G_N)|<=B_N on its collar, the inherited scalar-log transfer
gives |h_z-h_(N,z)|<=L B_N/(pi b^3). Evaluating at the model's own
cluster coordinates also requires the center/discriminant errors;
the transfer at common arguments does not pay those automatically.

Read the Rodgers–Tao branch
[note02 §§3–5](../../../../investigations-5/02_heat_flow_rh_applications/rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md)
and [note03 §§4–6](../../../../investigations-5/02_heat_flow_rh_applications/rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md).
That finite two-root pilot is **interval-certified** at its stated
compact scope. Its source error was negligible; its absolute model-unit
curvature payment was much larger than an equally informed direct
root-jet comparison. It gives no growing-height exclusion. Repeating
that pilot at higher precision is not the proposed gain.

A worthwhile advance would be a specified signed estimate with its
complete source inputs and geometry, useful where separated root jets
are unavailable, or a scoped obstruction identifying exactly which
information cannot supply it. An additional generic identity or a
smaller approximation error is not by itself such an advance.

Literature ownership remains in the [parent catalog](../../references/README.md)
and its [zero-dynamics passage record](../../references/03_CANONICAL_SCORE_FOURIER_PASSAGES_20261116.md).
The inherited Rodgers–Tao v5 passage, PDF §4/Theorem 11/(56), concerns
simple real zeros in Lambda<t<=0. It is background, not a theorem across
a hypothetical collision. This setup performs no new literature audit.

## Classification and collision controls

Use the [result index](../../../../../result-summaries/README.md), specifically
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and [approximation18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
and the [avoid index](../../../../../avoid/README.md), especially
[01](../../../../../avoid/01_restating_the_target.md),
[02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[03](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
and [15](../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md).

The identity and its finite-interval implication are conditional local
calculus. An unquantified demand for successful transport of all zeros
down to time zero would repackage the reality target; it is not an
independent estimate or evidence for RH.

The analytical screen in [discussion28 §5](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md)
applies in full. The quadratic heat collision has K=0, a regular outer
contour, and a positive late gap, but exhausts its budget at the event.
Weighted-square events share the local hypotheses; full reflection and
a finite all-real global anchor fail for those controls. Reflected and
smooth positive-source events lack unchanged theta arithmetic. Euler
and finite-profile threshold controls show that a real late slice and
finite source observations do not suffice; unchanged arithmetic/full
profile premises fail as recorded in controls12. Finite-head/score
controls fail the full canonical identities, while matching the chosen
finite data. RH-conditional endpoint controls retain their RH premise
and fail ordinary Dirichlet arithmetic; they screen unjustified endpoint
simplicity. Changed observation kernels or abstract profile relaxations
fail, respectively, the physical heat/Fourier premise or actual-field
premise. No unproved theta inequality is claimed to have been tested on
these families, and no numerical control certificates were rerun.

## Decisions left for setup

The [continuation note](../notes/01_VCD_GT_SETUP_CONTINUATION_20261116.md)
will guide creation of the plan and sole register. They should specify
the first bounded conceptual comparison, its available canonical inputs,
the direct comparator and the output needed before an execution request.
Larger clusters, changing contours, high-height coverage and accumulation
of descent steps remain separate obligations. No finite first collision
may simply be assumed to exist globally. Analytical work is primary;
any later numerical work must answer a declared supporting question.
