# The explicit theta input, simplified drivers, and collision magnification

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0008.

**Status: elementary consequences proved in-note, with same-assistant checking; collision magnification remains a proposal.** This note makes the actual flow and its input explicit, proves a controlled termwise application to theta, and distinguishes source redistribution from the user's proposed direction-independent amplification of collisions. No numerical theta evolution or collision-specific instability has been established. The manuscript incorporates the proved bounded flow from [Note23](23_PROJECTED_ANNULAR_FLOW_RESPONSE_AND_LOCAL_ADJOINT_20261027.md), with the first tube comparison referred to [Note22](22_STEERED_TUBE_GREEN_IDENTITY_AND_MATCHED_COMPARISON_20261027.md).

Consult the [result index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), [target classification](../../../../avoid/01_restating_the_target.md), [coordinate-realization caution](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scope rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md). The estimates below are a bounded approximation interface, not a new collision criterion. The new research objective is recorded separately in [Brainstorm03](../brainstorm/03_DIRECTION_INDEPENDENT_COLLISION_MAGNIFICATION_20261027.md).

**Subsequent clarification in the same chat:** preservation of the entire integral is sufficient; preservation of its radial integrand is no longer required of new flows. The constructions below retain their stronger special-case scope. [Note25](25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md) gives a nontrivial direction-independent heat flow of the full signed density under the relaxed requirement. The zero-start observation below is not a statement about that different initial-value problem.

## 1. What the symbols mean and where the equation is

The original theta function and radial source are

\[
\Theta(r)=1+2\sum_{n\ge1}e^{-\pi n^2r^2},\qquad
Q_t(r)=e^{t(\log r)^2/4}\left(\partial_r^2+\frac2r\partial_r\right)\Theta(r),
\]
\[
\boxed{Q_t(r)=4\pi e^{t(\log r)^2/4}
\sum_{n\ge1}n^2(2\pi n^2r^2-3)e^{-\pi n^2r^2}.}
\tag{1}
\]

Here t is physical Newman time; s below is an independent auxiliary time. On r≥1 the source is positive. The deformed source is F_s=Q_t+G_s. Thus G is the change in the source, not the original source itself. P denotes the average over the sphere at each fixed radius.

The prototype's χ_out is a **freely selected nonnegative spatial weight**, large in angular regions to be penalized. It is not a theta function, not supplied by the collision equations, and not an indicator unless separately regularized. The original smooth theorem allows any smooth χ_out≥0 on the closed annulus D={R_0<r<R_1}. No specific χ_out was chosen or evaluated in Note23.

The flow is Note23(5):

\[
\boxed{\partial_sG=\varepsilon\Delta G
 -\chi_{\rm out}(Q_t+G)+P[\chi_{\rm out}(Q_t+G)],
\quad G_0=0,\quad G|_{r=R_0,R_1}=0.}
\tag{2}
\]

The last two terms remove the weighted source and put back its spherical average. Consequently PG remains zero and PF_s=Q_t. The full Laplacian is ∂r²+2∂r/r+Δ_{S²}/r². Equation (2) is local in its derivatives but its averaging term couples angles on the same sphere. It is a source-cost descent, with the existence, convergence and response results proved in Note23; it is not yet a collision-sensitive evolution.

## 2. Direct application to the complete theta sum

Write Π=I−P and use Note23's fixed positive operator A=−εΔ_D+Πχ_out on the zero-average subspace. Since Q_t is radial,

\[
h_t=\Pi(\chi_{\rm out}Q_t)=Q_t\Pi\chi_{\rm out},\quad
G_s=-A^{-1}(I-e^{-sA})[Q_t\Pi\chi_{\rm out}].
\tag{3}
\]

The flow therefore can be applied directly to (1). Its linear operator is independent of the theta summation index; uniform convergence on the bounded annulus permits the sum to pass through this bounded solution operator. This is an exact analytic application. It does not say that a theta-specific numerical evolution had already been run.

Here is an explicit remainder if the angular forcing is evaluated with the first N≥1 theta terms. Let Q_{t,N} denote that partial sum, 0≤t≤T, m=N+1, and

\[
q_N=\left(\frac{m+1}{m}\right)^4e^{-\pi(2m+1)R_0^2}<1,
\]
\[
R_N=\frac{8\pi^2R_1^2e^{T(\log R_1)^2/4}
 m^4e^{-\pi m^2R_0^2}}{1-q_N}.
\tag{4}
\]

Each omitted summand is bounded by 8π²R_1²e^{T(log R_1)²/4}n⁴e^{-πn²R_0²}. The ratio of successive majorants is at most q_N for n≥m. Therefore 0≤Q_t−Q_{t,N}≤R_N throughout the stated domain. No numerical value of π or quadrature certificate is needed for this analytic bound.

Define the angular-variation factor

\[
V_\chi^2=4\pi\int_{R_0}^{R_1}r^2
 P[(\Pi\chi_{\rm out})^2]\,dr,
\quad
\gamma=\varepsilon\left[\frac{\pi^2}{(R_1-R_0)^2}+\frac2{R_1^2}\right].
\]

If G_s^{(N)} uses Q_{t,N} only in (3), then

\[
\boxed{\|G_s-G_s^{(N)}\|_{L^2(D)}
\le\frac{1-e^{-\gamma s}}{\gamma}R_NV_\chi.}
\tag{5}
\]

Indeed the forcing error is (Q_t−Q_{t,N})Πχ_out, and A≥γ. The exact factor V_χ measures the chosen weight's angular variance; it is zero for a radial weight. For Note23's additive response, the corresponding U error is at most μ⁻² times (5). For its local affine signed functional S_η, it is at most ||k_η|| times (5), while its canonical radial background is held fixed.

One can keep **F_s^{(N)}=Q_t+G_s^{(N)}** with the complete Q_t in the radial background. Then PF_s^{(N)}=Q_t exactly even though the auxiliary evolution's angular forcing is approximated. Equation (5) measures the difference from the intended exact evolution. It is not a statement that Q_{t,N} equals Q_t or that a finite source truncation by itself preserves the physical transform.

## 3. What happens on simplifying or removing the drive

A simpler trial equation discussed in this chat was

\[
\partial_sG=\varepsilon\Delta G-\nu G
 +\nu w(r)Q_t(r)[n(r)\cdot\omega],\qquad \nu>0,
\tag{6}
\]

with zero initial and radial boundary values. Here ν is a relaxation rate, w a radial window, and n a prescribed unit direction. Its forcing has zero spherical average, so the projection can be omitted. Because the forcing occupies only the first spherical harmonic sector, writing G=V(s,r)·ω reduces (6) to three copies of

\[
\partial_sV=\varepsilon\left(V_{rr}+\frac2rV_r-\frac2{r^2}V\right)
 -\nu V+\nu wQ_t n.
\tag{7}
\]

This gives a simple directional redistribution model. It does not identify collisions, and no numerical theta test of (6) was run before the user redirected the question toward amplification of collisions without a prescribed direction.

Deleting the last term of (6) gives damped heat flow. With G_0=0, uniqueness gives G_s=0 for every s. With nonzero zero-average initial data it smooths and damps that data. This statement concerns G: applying damped heat directly to the full Q_t would generally change the radial integrand. Likewise, a radial χ_out makes the original forcing h_t vanish and leaves its zero-start solution stationary.

There is a useful scope statement behind this observation. Suppose a deterministic source evolution is uniquely solvable, commutes with every spatial rotation, starts from radial Q_t, and preserves PF_s=Q_t. Applying a rotation gives another solution with the same initial data, so uniqueness makes F_s radial. Its preserved average then forces F_s=Q_t. This excludes nontrivial angular source redistribution under **that conjunction of assumptions**. It does not exclude changing a radial auxiliary response, adding a spectral state, using nonradial initial data, or an evolution outside that class. In particular it is not an obstruction to the user's broader collision-magnification proposal.

## 4. Collision magnification is a different objective

The user clarified that the intended feature to magnify is a collision, H(T,a)=H_a(T,a)=0, without necessarily assigning a spatial direction. This condition concerns the spectral response. It is not a zero of Q_t, which is positive on r≥1. A chosen source penalty does not automatically detect the simultaneous spectral cancellation.

Keeping the complete radial integrand fixes H and its physical derivatives. It still permits an auxiliary response or geometry to develop a pronounced feature at such an event. A useful new flow would have to establish a collision-sensitive amplification law and a separately justified bound from the canonical theta source. Both are open. A generic magnifier would also magnify the known colliding controls; the eventual source estimate must distinguish them in its stated domain.

The manuscript records the projected flow as a proved baseline, with its actual equation and explicit theta input, and treats collision-sensitive dynamics as an open objective. The first multiplicative comparison remains a scoped limitation, not a reason to impose a preferred direction on every later construction. [Review14](../reviews/14_PROJECTED_FLOW_MANUSCRIPT_AND_COLLISION_SCOPE_20261027.md) assesses this return. No positive-threshold contradiction, improved theta exclusion, or independent specialist review is claimed.
