# Radial Laplacian collision research program

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Program established in Investigation05 chat0004, **Explore 3D Laplacian collision rules**.

**Priority and purpose.** This is the primary research program for Investigation05. At Edward Baker's request it supersedes the earlier [RTC overview][old-overview] in research priority. The earlier files and mathematical results remain intact. The new [RLC progress register][progress] governs current tasks; the [handoff][handoff] specifies the next session. This is a new planning document, not a new collision theorem.

The objective is to obtain **analytic restrictions on collisions of the unchanged theta heat flow by using its three-dimensional radial Laplacian, flux and boundary equations**. The first route develops source-specific estimates for the two collision observations together. A second route seeks an analytic contradiction under the hypothetical event boundary conditions. A homogeneous characteristic realization is a longer-term alternative. Numerical work supports proofs, normalization checks and explicit constants; it does not lead the program.

The starting point is [Note14][n14], following [Note13][n13] and the founding [Note01][n01]. No new higher-rank lattice, quaternionic field, or change of source is required. The original integer-square coefficients and full theta reflection are retained throughout.

## Outcomes and the distinction between identities and restrictions

A useful outcome may be an analytic exclusion on a stated parameter domain, a quantitative necessary condition that restricts a collision's location or source balance, a sharper complete source-to-observation estimate, or a proved obstruction for a precisely specified attempted estimate. A bounded result is valuable without settling the global threshold problem.

Every proposal must identify its consumer: what statement about H, H_a, a candidate event, or a complete physical boundary follows from the estimate? Rewriting H=H_a=0 as a different vanishing condition is a representation, not a restriction. A sufficient criterion is not acquired merely because its implication has been proved. A global characteristic realization is an aspirational sufficient mechanism; no equivalence of the existence of such an operator with RH is asserted.

Use the [result index][results], especially [collision controls][controls], [local collision geometry][geometry], [theta arithmetic][arithmetic] and [geometric realizations][lifts], with the [avoid index][avoid]. Apply [target classification][a01], [control screening][a02], [coordinate-lift comparisons][a03], [scoped conclusions][a07], [complete coupled estimates][a12] and [noncircular hypotheses][a14] before presenting a proposed mechanism as progress.

## Canonical objects and the domains of the claims

Keep

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad H_t=-H_{zz},\qquad r=e^{2u},\quad x=\log r=2u,
\]

\[
\Theta(r)=1+2\sum_{n\ge1}e^{-\pi n^2r^2},\quad
Q=\Delta_3\Theta,\quad
\Phi(u)=\tfrac14r^{5/2}Q(r),\quad
Q_t=w_tQ,\quad w_t=e^{t\log^2r/4}.
\tag{1}
\]

The physical time law is multiplication, partial_t Q_t=(log^2 r/4)Q_t. It is not radial heat diffusion. Source radius r, logarithmic coordinate x, observation frequency a, and Newman time t must remain distinct.

For real t use the normalized potential and tail charge

\[
M_t=16H(t,i),\qquad
\mathcal T_t(r)=M_t+\int_r^\infty(s^2/r-s)Q_t(s)\,ds,
\qquad S_t(r)=-r^2\mathcal T_t'(r)=\int_r^\infty s^2Q_t(s)\,ds.
\tag{2}
\]

They satisfy Q_t(r)=r^(-5)Q_t(1/r), T_t(r)=r^(-1)T_t(1/r), and the full-space distributional equation Delta T_t=Q_t-4 pi M_t delta_0. In particular, S_t(0+)=M_t, S_t(infinity)=0 and 2S_t(1)=T_t(1). The unit sphere is the boundary u=0; it is not the spatial origin. The central charge, constant at infinity and exterior boundary value are not interchangeable.

For a>0 put theta=(a/2)log r and define

\[
\mathbf K_a(r)=r^{-1/2}
\begin{pmatrix}\cos\theta\\-(\log r/2)\sin\theta\end{pmatrix},
\qquad
8\begin{pmatrix}H(t,a)\\H_a(t,a)\end{pmatrix}
=\int_1^\infty \mathbf K_a(r)r^2Q_t(r)\,dr.
\tag{3}
\]

The complete integral in (3) already incorporates inversion through the canonical cosine formula. Do not add the interior contribution again. Every real zero of multiplicity at least two satisfies the two conditions in (3). H(t,0)>0 eliminates a=0 for real t. For a>0 the variable lambda=a^2/4 preserves finite multiplicity.

Start with symbolic compact parameter sets, such as 0<=t<=T_+ and 0<a_-<=a<=a_+. Positivity arguments below use t>=0 unless explicitly extended. Bounds uniform on a compact set are not automatically uniform as t approaches zero or a tends to infinity. An all-height statement cannot use an unweighted positive constant floor for |H|+|H_a|: both observations decay with real frequency at a fixed time. A useful global comparison needs its actual height dependence and a noncircular normalization.

An arbitrary local event, an event at a hypothetical positive all-real threshold, and a possible multiple zero at t=0 are different applications. RLC-06 owns their transfer. No current task assumes the conclusion of a threshold or endpoint-simplicity theorem.

## What is already available

| Input | Source and evidence | Role in this program |
| --- | --- | --- |
| Radial dictionary, Kelvin potential, physical observation and time law | Note01, with its same-assistant assessment | Fixed normalization and source geometry |
| Forced boundary realization and complete Wronskian | Note01; exact positive-source collision control | Identifies the forcing cancellation to be controlled |
| Finite nonlinear canonical theta system | Note05 | Source-coordinate information that may enter an estimate; no finite physical spectral closure follows |
| Modular multiplier obstruction | Note05, same-assistant analytic proof and rational source bounds | The tested normalized scalar weight neither changes the complete integral nor has an everywhere favorable canonical integrand on its stated regime |
| Gaussian deformation and complete index transport | Note04 | Boundary crossings remain necessary; a positive changed-source endpoint does not force zero original degree |
| Positive flux formula and radial Hardy calculation | Note14, direct in-note derivations, same assistant | Starting identities for RLC-01 through RLC-03; no measured estimate gain or collision exclusion |

The seven bounded RTC-03 returns remain in the [historical register][old-progress]. Their count is not transferred to RLC. Note14 is the program's brainstorming foundation, not an eighth RTC return or a completed analytic exclusion.

## RLC-01 Canonical flux estimates and complete observation transfer

**Goal.** Turn the simpler flux into a controlled analytic input for the collision observations, with every time, boundary and tail cost explicit.

The starting identities from Note14 are

\[
S_0(r)=4\pi r^3\sum_{n\ge1}n^2e^{-\pi n^2r^2},
\qquad
S_t(r)=w_t(r)S_0(r)+\frac t2\int_r^\infty
\frac{\log s}{s}w_t(s)S_0(s)\,ds.
\tag{4}
\]

Both terms in the second expression are nonnegative on r>=1, t>=0, and the first is strictly positive. The integral correction vanishes at t=0 and is positive at t>0. This removes the difference of polynomial weights in the original source, while retaining the correction from physical time.

Develop bounds for S_t, differences S_t(R)-S_t(U), and the weighted tails actually needed by both components of (3). State the range of t, r, a and any source truncation index. Derive uniform differentiation and integration justifications from the complete Gaussian sum and the integral in (4). Absolute bounds for separate terms are allowed only when their complete cost is compared with a coupled alternative.

With k_a(r)=r^(-1/2)cos((a/2)log r), the exact transfer is

\[
8H=S_t(1)+\int_1^\infty S_t k_a'\,dr,
\qquad
8H_a=\int_1^\infty S_t\,\partial_a k_a'\,dr.
\tag{5}
\]

A flux approximation or source modification must retain the boundary difference at r=1 in the first component and the common interior residual in both. Keep adjacent shell differences correlated through their shared endpoint flux. Treat any missing tail analytically before claiming a physical bound.

**Deliverable.** A proof note giving an applicable uniform flux-and-observation estimate, including a matched direct-u comparison. Re-deriving (4)-(5) is an audit, not a new deliverable. A proved dominance or exact failure of a specified proposed estimate is an acceptable scoped return. This work supplies RLC-02 and the source bounds needed by RLC-03/04.

## RLC-02 Analytic restrictions from joint shell cancellation

**Goal.** Prove that the canonical charges of logarithmic shells cannot meet both collision cancellations on a declared domain, or derive a quantitative restriction on when they could.

For fixed radii 1=R_0<...<R_N, the shell charge is

\[
q_j(t)=S_t(R_j)-S_t(R_{j+1})>0.
\tag{6}
\]

Its contribution to (3) lies in q_j times the convex hull of K_a on that shell. This enclosure is generic; it is not a separating theorem for theta. The analytic work is to combine canonical bounds on the q_j, shared flux constraints, oscillatory phase and the complete tail into an independently proved separation.

One possible proof format chooses an explicit real direction v(t,a), or finitely many directions on a proved domain cover, and obtains a positive lower bound for v dot (H,H_a). Choose directions from declared source/phase information or an approximant with controlled error, not from an assumed nonzero physical pair. Keep the two kernels together before taking absolute values. A different analytic comparison is welcome if its consumer and cost are clearer.

The radii may be selected to follow logarithmic phase, but frequency-dependent or time-dependent cuts need their endpoint derivatives whenever differentiation is used. A fixed partition on each declared parameter domain avoids introducing those terms. Prove any covering argument over the entire intervals, not just at sampled points.

**Deliverable.** Prefer an analytic theorem with an explicit domain and margin, a source-balance restriction that excludes a specified collision range, or an improved complete signed estimate with a quantified advantage. A positive interval-enclosed constant may support the theorem after its analytic reduction. A finite grid or an unevaluated separation condition does not complete this task.

Compare with direct integration of the same two observations under the same source information, domain and tail budget. If the radial proof is only the same inequality in new coordinates, record that conclusion and stop that variant. RLC-02 is the first main collision route, not a prerequisite for the alternative RLC-04 route.

## RLC-03 Local energy estimates with paid interfaces

**Goal.** Determine whether short-annulus coercivity can improve an identified observation or forced-response estimate after all interface and cutoff costs are included.

The physical mode solves (-Delta_3-(1+a^2)/(4r^2))Psi_a=0. Note14 derives, for f=r^(-1/2)v(log r) with compact support,

\[
\int_0^\infty\left(r^2|f'|^2-\frac{1+a^2}{4}|f|^2\right)dr
=\int\left(|v'|^2-\frac{a^2}{4}|v|^2\right)dx.
\tag{7}
\]

On a Dirichlet interval of logarithmic width L the lower constant is pi^2/L^2-a^2/4. It is positive when |a|L<2 pi. The selected physical response does not automatically satisfy Dirichlet conditions on arbitrary shell boundaries.

Choose one real consumer from RLC-02 or RLC-04. Specify the function, measure, domain and cutoff. Derive the full localized Green or energy identity before estimating it. Include forcing, traces at both interfaces, derivatives of cutoffs and of moving interfaces, and the reconstruction back to the physical observation. Show how the costs scale as L is shortened; narrowing an annulus can increase derivative costs enough to erase the coercive gain.

**Deliverable.** A complete analytic inequality with a gain after these payments, or a scoped proof that the selected localization cannot improve the matched direct estimate. Do not pursue this track merely to restate the Hardy inequality. It is a supporting analytic tool, not a claim that an arbitrary positive radial operator forbids collisions.

## RLC-04 Theta information under the event boundary conditions

**Goal.** Find an additional analytic restriction on the forced response that uses the complete theta source and the hypothetical event conditions together.

Use Note01's tail-selected Volterra solutions, with

\[
g_t(x)=4e^{tx^2/4}\Phi(x/2),\quad
Y_{xx}+\lambda Y=g_t,\quad
Z_{xx}+\lambda Z=-Y,\quad Z=Y_\lambda,
\]

\[
B=Y_x(0)=-8H(t,2\sqrt\lambda),\qquad
Y(0)B_\lambda-BZ(0)=\int Y^2dx+\int g_tZ\,dx.
\tag{8}
\]

At a multiple event, Y_x(0)=Z_x(0)=0 and the two integrals in (8) cancel. Merely requiring that they not cancel restates the target. Seek a distinct identity, source-dependent bound, or compatibility obstruction whose input can be established without evaluating an assumed nonzero H or H_a.

Candidate operations include a fully coupled dilation/Rellich identity, a source-sensitive comparison using the nonlinear theta system in Note05, or a localized identity supplied by RLC-03. Select one candidate and identify the precise extra source premise it uses. The generic three-component transfer system and finite nonlinear source coordinates are already available; they do not constitute a new physical closure by themselves.

Retain spectral-parameter differentiation of forcing, coefficients, weights and boundaries. Keep the selected tails; ordinary decay at a complex parameter may not uniquely choose the response. Test the exact Gaussian-polynomial control before optimizing a proposed sign, and check the other relevant registered families at their actual hypotheses. If a normalized scalar multiplier only differentiates the old Wronskian, compare its complete boundary form with Note05 before continuing.

**Deliverable.** A proved restriction under candidate-event conditions with its domain and canonical input identified, or a precise obstruction to the chosen mechanism. A smaller unpaid estimate is useful only if an independent analytic gain is demonstrated; renaming the same signed forcing integral is not that gain. This track may proceed after RLC-01 even if the shell route fails.

## RLC-05 Homogeneous characteristic realization

**Goal.** Test a concrete operator construction in which a physical H-zero would be a characteristic zero of a homogeneous problem with a usable simplicity identity.

This is exploratory and presently has no candidate. Before beginning a calculation, specify the operator from source data, its Hilbert space, domain, boundary conditions, and the proposed map D_t(a)=c_t(a)H(t,a). The factor c_t must be nonvanishing on the claimed domain. A characteristic function must be distinguished from a source coefficient, a scattering coefficient or a positive auxiliary channel.

If invoking scalar Sturm-Liouville simplicity, verify its positive weight, actual eigenfunction domain, normalization and separated boundary conditions. Spectral dependence in a boundary or coefficient produces derivative terms that cannot be dropped. Self-adjointness alone does not imply simplicity for every multidimensional or matrix problem.

**Deliverable.** An exact candidate with all hypotheses checked, or a scoped reason that the candidate cannot represent the physical characteristic function. Do not define coefficients using unknown zeros, insert H itself as a boundary condition, or treat an arbitrary inverse spectral fit as an independent construction. No new lattice or quaternionic lift is required; reintroduce one only to solve a specified obstruction in this exact construction.

## RLC-06 Multiplicity and parameter-range assembly

**Goal.** Convert a result from RLC-02, RLC-04 or RLC-05 into exactly the physical conclusion its proven coverage supports.

Record the time interval, frequency range, endpoints, normalization and all constants. An exclusion of H=H_a=0 rules out every finite multiplicity at least two at a>0; an argument proved only for a nondegenerate double event needs a separate higher-multiplicity extension. Do not replace one statement by the other.

For a positive-threshold application, read and check the inherited canonical exterior/finite-event reduction in the [positive-threshold note][threshold] and Note01 before importing it. Combine bounded-height work with the actual exterior result, including its dependence on time and any effective cutoff. Cover all remaining time ranges required by the contradiction argument. A bound valid at each fixed positive time need not have a cutoff uniform as t decreases to zero.

If a global-index argument becomes useful, pay both time faces, both frequency walls, tangencies and any limiting cap. Note04's Gaussian deformation preserves hypothetical events until they cross those boundaries; radial charge conservation cannot replace the missing physical boundary estimate.

**Deliverable.** A precisely scoped corollary or an explicit list of uncovered ranges and hypotheses. Endpoint simplicity at t=0 is a separate task requiring its own argument. Finite-domain success must not be promoted to an RH or Newman-bound conclusion without the full transfer.

## RLC-07 Supporting verification and research records

This track accompanies every analytic return. It is not a separate numerical campaign.

1. State the analytic question, consumer, domain and expected output before computing. Appropriate uses include exact differential-algebra checks, testing a proposed estimate against an explicit control, and rigorous enclosure of a finite constant in an already derived theorem.
2. Keep exploratory floating-point values separate from interval-certified constants and from proofs of convergence, sign or uniformity. Sampling cannot establish a universal inequality or the absence of an unsampled collision.
3. Do not optimize a grid, shell partition or precision before the complete analytic budget exists. If a computation cannot resolve a declared analytic uncertainty, defer it.
4. Save proofs in notes/, assessments in reviews/, and scripts and small records in numerics/. State author, date, actual model/effort, dependencies, domain, gain and unproved obligations. Same-assistant checking is not independent specialist review.
5. Preserve the [reference workflow][reference-workflow], [large-file policy][large-files] and [chat workflow][history-workflow]. Do not create manuscript snapshot folders. Add a concise DRAFT_HISTORY entry only at an actual manuscript or investigation milestone; this planning reset is recorded in the progress log.

The control screen from Note14 remains the minimum starting point. Gaussian-polynomial controls share the generic forced equation and radial geometry but fail theta arithmetic and tails. Euler-factor controls change source and conductor. Weighted-square and finite-prime controls retain selected arithmetic but fail full canonical coefficients/reflection. Reflected smooth and positive-primitive controls retain geometry and auxiliary positivity but lack the full square source. Finite-profile atomic/compact controls lack theta growth and arithmetic, with measure formulations needed for atoms. RH-conditional endpoint perturbations change ordinary Dirichlet arithmetic. Identify the actual failed premise of each relevant control; no single broad property distinguishes every family. In particular, no control fails the generic shell-convexity statement itself.

## How the parts fit together and what happens first

| Part | Supplies | Consumed by | Initial priority |
| --- | --- | --- | --- |
| RLC-01 | Canonical flux and complete analytic observation bounds | RLC-02, and source bounds for RLC-03/04 | Start here; existing identities are inputs |
| RLC-02 | Joint cancellation restrictions from source charges and phase | RLC-06 | First main analytic route |
| RLC-03 | Local coercivity with paid forcing and interfaces | RLC-02 or RLC-04 | Start only for an identified estimate |
| RLC-04 | Event-conditioned canonical compatibility or signed estimate | RLC-06 | Main structural alternative after the common setup |
| RLC-05 | Candidate homogeneous characteristic mechanism | RLC-06 | Deferred until a concrete candidate is specified |
| RLC-06 | Exact multiplicity and range transfer | Physical collision or threshold statement | Activate when an applicable result exists |
| RLC-07 | Controls, verification, references and provenance | Every part | Continuous support |

The first bounded return should join RLC-01 to RLC-02: derive a complete analytic flux-to-two-observation comparison, apply actual theta shell/tail information, and compare its full allowance with the direct formulation on the same symbolic domain. The return may be a gain or a precise failure of that comparison. It must go beyond the identities already in Note14. The [handoff][handoff] gives an executable sequence and the [progress register][progress] records which obligations remain open.

[progress]: ../research-progress/02_RADIAL_LAPLACIAN_COLLISION_RESEARCH_PROGRESS_20261027.md
[handoff]: ../notes/15_RADIAL_LAPLACIAN_COLLISION_PROGRAM_HANDOFF_20261027.md
[old-overview]: 01_RADIAL_THETA_COLLISION_RESEARCH_OVERVIEW_20261027.md
[old-progress]: ../research-progress/01_RADIAL_THETA_COLLISION_RESEARCH_PROGRESS_20261027.md
[n01]: ../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[n13]: ../notes/13_RADIAL_LAPLACIAN_CONTINUATION_20261027.md
[n14]: ../notes/14_RADIAL_FLUX_AND_COLLISION_RESTRICTIONS_BRAINSTORM_20261027.md
[threshold]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[arithmetic]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[lifts]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
[reference-workflow]: ../../../../REFERENCE_WORKFLOW.md
[large-files]: ../../../../LARGE_FILES.md
[history-workflow]: ../../../../tools/CHAT_HISTORY.md
