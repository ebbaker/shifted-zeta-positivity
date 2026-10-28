# Projected annular flow, a complete response, and the local signed adjoint

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0008, **Continue radial theta investigation**.

**Status: proved in-note using the stated classical functional-analysis inputs; same-assistant internal assessment.** The bounded LOC-03 prototype has a unique global auxiliary evolution, explicit exponential convergence, and a strict quantified decrease of the declared source-localization cost. A specified additive response realizes its preserved radial integrand on the whole exterior domain in a weak/strong elliptic sense, with radial joins accounted for. A local signed current and its adjoint are derived. No theta collision estimate or globally smooth extension of the annular evolution is asserted.

This follows the completed [LOC-02 comparison](22_STEERED_TUBE_GREEN_IDENTITY_AND_MATCHED_COMPARISON_20261027.md). These are finite-domain construction and estimate milestones, not a new RH-equivalent criterion. Interpretation follows the [result index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), [control screen](../../../../result-summaries/12_collision_controls_and_screening.md), [target classification](../../../../avoid/01_restating_the_target.md), [transported-identity caution](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), and [scope rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md). The standard inputs and their inspected passages are recorded in [reference annotation10](../references/10_PROJECTED_EVOLUTION_AND_ELLIPTIC_RESPONSE_20261027.md).

## Reading the actual flow

The equation is (5) below: ∂_sG=εΔG−(I−P)[χ(Q_t+G)], with zero initial and Dirichlet boundary values. Q_t is the full heat-weighted radial theta source; χ (called χ_out in the proposal) is a freely selected smooth nonnegative spatial penalty, not an intrinsic theta quantity. P averages over each sphere. [Note24](24_EXPLICIT_THETA_FLOW_AND_COLLISION_MAGNIFICATION_SCOPE_20261027.md) expands the equation and source sum and gives its truncation estimate.

Edward Baker subsequently relaxed the general requirement to conservation of the whole observation integral, allowing the radial integrand to change. This note remains a proved stronger special case. [Note25](25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md) develops the weaker invariant and an explicit local heat flow without a chosen direction or angular projection.

## 1. The bounded problem and its function spaces

Fix t, 1<R_0<R_1<∞, ε>0, a real radial Q=Q_t smooth on the closed annulus D={R_0<|X|<R_1}, and real χ∈C∞(D̄), χ≥0. The angular localization weight and any candidate frequency used to choose it are frozen independently of the running spectral parameter λ. Use ordinary Euclidean volume throughout this note. Let P be spherical averaging, Π=I−P, and

\[
\mathcal H=\{v\in L^2(D):Pv=0\},\quad
\mathcal V=H^1_0(D)\cap\mathcal H,\quad h=\Pi(\chi Q).
\]

P is an orthogonal projection on L²(D); it preserves the Dirichlet Sobolev space and commutes with the Dirichlet Laplacian, by spherical averaging or rotation invariance. The dense domain

\[
\mathcal D(\mathsf A)=H^2(D)\cap H^1_0(D)\cap\mathcal H,
\qquad \mathsf A v=-\varepsilon\Delta v+\Pi(\chi v)
\tag{1}
\]

defines a positive self-adjoint operator on H. Indeed the Laplacian part is self-adjoint on this reducing subspace, while Πχ restricted to H is bounded and symmetric:
⟨v,Πχw⟩=∫χvw. Its quadratic form is

\[
\mathfrak a(v,w)=\varepsilon\int_D\nabla v\cdot\nabla w+\int_D\chi vw.
\tag{2}
\]

Bounded symmetric perturbations retain the adjoint domain. The form also gives a direct Lax–Milgram construction of its inverse.

An explicit useful coercivity constant is

\[
\boxed{\gamma=\varepsilon\left[\frac{\pi^2}{(R_1-R_0)^2}+\frac2{R_1^2}\right]>0,
\qquad \mathsf A\ge\gamma I.}
\tag{3}
\]

To prove it, for each ω put ṽ(r)=rv(r,ω). Zero radial boundary traces give ∫r²|v_r|²dr=∫|ṽ_r|²dr. The one-dimensional Dirichlet Poincaré inequality supplies π²/(R_1−R_0)² times ∫r²|v|²dr. On each sphere, Pv=0 gives ∫|∇_S v|²dΩ≥2∫|v|²dΩ. Integrate in r and use r≤R_1 for the second term in (3). Nonnegative χ adds no loss. The angular eigenvalue convention is the one checked in reference annotation09.

## 2. Existence, regularity, convergence, and cost reduction

The unique solution of the proposed evolution is

\[
G_s=-\mathsf A^{-1}(I-e^{-s\mathsf A})h,
\quad \partial_sG_s=-e^{-s\mathsf A}h,
\quad G_0=0.
\tag{4}
\]

It belongs to C([0,∞);D(A))∩C¹([0,∞);H), where D(A) has the graph norm, and solves

\[
\partial_sG=\varepsilon\Delta G-\Pi[\chi(Q+G)],
\quad G|_{\partial D}=0,\quad PG=0.
\tag{5}
\]

The spectral calculus for the positive self-adjoint A proves (4), its graph continuity via AG=−(I−e^{-sA})h, and uniqueness by the difference energy. This is an actual solution theorem, not a dissipation identity conditional on an unspecified smooth solution.

For smooth data, G_s is smooth up to the spatial boundary for every s>0. One way to see this is G_s=G_∞−e^{-sA}G_∞, with G_∞=−A^{-1}h: elliptic regularity bootstraps the stationary term, and the analytic semigroup plus elliptic regularity smooths the other term. The averaging term preserves every spatial Sobolev order on this smooth annulus. Smoothness at the corner s=0, ∂D requires compatibility: if h has nonzero boundary trace, ∂_sG(0)=−h in L² cannot also be the zero differentiated boundary trace. We make no such corner claim. Taking χ supported away from the radial faces is a sufficient way to satisfy all initial compatibility orders for the zero initial datum.

For

\[
\mathcal E(G)=\frac12\int_D\chi(Q+G)^2
+\frac\varepsilon2\int_D|\nabla G|^2,
\tag{6}
\]

direct differentiation for s>0, followed by continuity/integration to zero, proves

\[
\frac{d\mathcal E}{ds}=-\|\partial_sG\|_2^2,
\quad \mathcal E(G)=\mathcal E(0)+\langle h,G\rangle+\tfrac12\mathfrak a(G,G),
\tag{7}
\]
\[
G_\infty=-\mathsf A^{-1}h,\quad
\mathcal E(G_\infty)=\mathcal E(0)-\tfrac12\langle h,\mathsf A^{-1}h\rangle,
\tag{8}
\]
\[
\|G_s-G_\infty\|_2\le e^{-\gamma s}\|G_\infty\|_2,
\quad
\mathcal E(G_s)-\mathcal E(G_\infty)
\le \tfrac12 e^{-2\gamma s}\langle h,\mathsf A^{-1}h\rangle.
\tag{9}
\]

In particular, writing M_s=∫χ(Q+G_s)²,

\[
M_s\le M_0-\langle h,\mathsf A^{-1}(I-e^{-2s\mathsf A})h\rangle.
\tag{10}
\]

Thus M_s<M_0 for every s>0 if h≠0. For the positive canonical Q this condition is precisely that χ is not radial almost everywhere. This does **not** claim that M_s itself is monotone; the sum (6) is monotone. At equilibrium the exact source-cost decrease is

\[
M_0-M_\infty=\langle h,\mathsf A^{-1}h\rangle
+\varepsilon\|\nabla G_\infty\|_2^2.
\tag{11}
\]

The inverse in these expressions has a concrete variational lower bound. Every v∈V with a(v,v)>0 gives

\[
\langle h,\mathsf A^{-1}h\rangle
\ge\frac{|\langle h,v\rangle|^2}{\mathfrak a(v,v)}.
\tag{12}
\]

This follows by optimizing 2τ⟨h,v⟩−τ²a(v,v). For smooth nonzero h take v=ηh with a nonnegative interior radial bump η chosen where h is nonzero; then ⟨h,v⟩>0. Equations (3), (9), and (12) are quantitative finite-domain returns. They hold for arbitrary smooth marginals and are not collision bounds. No positivity of Q+G is required or proved.

## 3. Radial joins and a complete exterior response

Let E={r>1}; use P and Π also on E. Denote zero extension from D to E by J_D. Since G_s∈H¹₀(D), J_DG_s∈H¹₀(E), and

\[
F_s=Q_t+J_DG_s,\qquad PF_s=Q_t.
\tag{13}
\]

For smooth positive-s data the source is continuous across both artificial faces, but its normal derivative need not match. In distributions,

\[
\Delta(J_DG)=J_D(\Delta G)-(\partial_NG)\,\delta_{\partial D}.
\tag{14}
\]

Consequently the zero-extended annular evolution would contain the additional term +ε(∂_NG)δ_{∂D} if its Laplacian were written on all of E. We do not call it an unforced global smooth evolution. Its spherical mean, including this interface term, is zero.

Here is a complete response that uses F_s itself, without differentiating its extension or prescribing elliptic Cauchy data. Fix μ>0. On the zero-average subspace of L²(E), let

\[
\mathsf K_\mu=-\Delta_E^D+\mu^2,\quad
U_s=-\mathsf K_\mu^{-1}J_DG_s,
\quad f_s=\psi+U_s,
\tag{15}
\]

where ψ=r^{-1/2}Y is the original selected radial tail response. The inverse is defined by the coercive form ∫(|∇U|²+μ²U²) on H¹₀(E)∩ker P. Lax–Milgram gives existence and uniqueness even on this unbounded domain, because μ>0 controls the L² norm. Rotation invariance gives PU_s=0. In particular,

\[
\|U_s\|_2\le\mu^{-2}\|G_s\|_2,\qquad
\|\nabla U_s\|_2\le\mu^{-1}\|G_s\|_2.
\tag{16}
\]

Local elliptic regularity, including the smooth r=1 boundary, gives H² locally up to that boundary and across the artificial faces. Since J_DG_s is H¹, local H³ regularity also holds. Away from the faces the positive-s solution is smooth. No jump in normal response flux is introduced: (15) is one global weak equation, with no surface forcing. Finite H¹ norm is the selected outer condition; an unproved backward radial Cauchy construction is not used.

Define the actual response operator

\[
\boxed{\mathcal L_\lambda=\Delta+\frac{\lambda+1/4}{r^2}P-\mu^2\Pi.}
\tag{17}
\]

It is nonlocal in angle through P. Such a change of equation satisfies the radial-integrand invariant imposed for this construction. On its radial component it is the old operator; on its zero-average component it is Δ−μ². Equations (13)–(17) prove

\[
\mathcal L_\lambda f_s=F_s,\quad Pf_s=\psi,
\quad P[(r\partial_r+1/2)f_s]_{r=1}=B(t,\lambda).
\tag{18}
\]

The averaged normal derivative is zero for U_s, as follows by differentiating PU_s=0 in its boundary collar. Since G_s and K_μ are independent of running λ,

\[
\partial_\lambda f_s=\zeta,\quad
\mathcal L_\lambda\zeta=-\psi/r^2,
\quad P[(r\partial_r+1/2)\zeta]_{r=1}=B_\lambda.
\tag{19}
\]

The spectral right-hand side is −ψ/r², **not** −f_s/r²: ∂_λL_λ=r^{-2}P. Every finite spectral derivative of the observation is retained. The prescribed radial part and the coercive selection of the zero-average part give uniqueness in this selected response class; no homogeneous spectral assertion is made for the radial channel.

Finally, \(\mathcal J_s(t,z;r,\omega)=\frac18r^{3/2}F_s\cos(z\log r/2)\) has the original radial density as its average at every radius (with its continuous representative). The construction is at fixed physical t. Repeating it for Q_t gives the same physical observation; (5) is auxiliary evolution, not a claim that the extended source obeys the original pointwise physical-time multiplier law.

## 4. The local signed current and its adjoint

The response variation is exactly

\[
\delta U=-\mathsf K_\mu^{-1}J_D\delta G.
\tag{20}
\]

Use the real current j=f_s∇ζ−ζ∇f_s, and let V=(λ+1/4)/r². Subtracting the actual equations gives, almost everywhere and distributionally,

\[
\operatorname{div}j=-[D_0+\sigma U_s+\zeta J_DG_s],
\quad D_0=\psi^2/r^2+Q_t\zeta,
\quad \sigma=\psi/r^2+(V+\mu^2)\zeta.
\tag{21}
\]

The (V+μ²) term is essential: the projected potential in (17) does not cancel pointwise on an angular tube. Whole-sphere averaging eliminates both additional terms and recovers the radial identity. This is how the extra geometry can affect a local balance while preserving the full one.

For a real smooth compact cutoff η supported inside D, define

\[
\mathcal S_\eta(G)=\int_E\eta[D_0+\sigma U+\zeta J_DG]\,dV.
\tag{22}
\]

There is an exact cutoff identity S_η(G)=∫_E∇η·j. Thus the transition current remains present. Alternatively a finite tube indicator defines the same volume functional and its outward boundary flux, with no asserted zero side data.

The local functional is affine, with the following **derived** Hilbert-space gradient:

\[
\mathcal S_\eta(G)=\mathcal S_\eta(0)+\langle k_\eta,G\rangle_{L^2(D)},
\]
\[
\boxed{k_\eta=\Pi_DJ_D^*\left[\eta\zeta-
\mathsf K_\mu^{-1}\Pi_E(\eta\sigma)\right].}
\tag{23}
\]

Here J_D^* is restriction. To check the sign, insert (20) into δS: self-adjointness of K_μ^{-1} transfers it from J_DδG to Π_E(ησ); the source term gives +ηζ. The outer projection implements the constraint PδG=0. A finite indicator is also allowed in (23), since its products are L²; its boundary identity is understood weakly.

This supplies an actual adjoint problem, K_μp=Π_E(ησ), with zero inner trace and finite H¹ norm. If η is radial then k_η=0. For the physical residual built only from B and B_λ the variation is also identically zero, by (18)–(19). Decreasing a local source cost cannot change those invariant observations.

One explicit allowance is

\[
|\mathcal S_\eta(G_s)-\mathcal S_\eta(0)|
\le\|k_\eta\|_2\,\frac{1-e^{-\gamma s}}{\gamma}\|h\|_2,
\quad
\|k_\eta\|_2\le\|\Pi_DJ_D^*(\eta\zeta)\|_2+
\mu^{-2}\|\Pi_E(\eta\sigma)\|_2.
\tag{24}
\]

On the energy ball a(G,G)≤R² the exact variation range is
\([-R\sqrt{\langle k_\eta,A^{-1}k_\eta\rangle},R\sqrt{\langle k_\eta,A^{-1}k_\eta\rangle}]\).
This follows from Cauchy–Schwarz in the A form and is attained in the directions ±A^{-1}k_η when k_η≠0. It is a quantitative budget, not a canonical sign estimate.

Along the **source** flow (4),

\[
\frac{d}{ds}\mathcal S_\eta(G_s)=-\langle k_\eta,e^{-sA}h\rangle.
\tag{25}
\]

The dissipation (7) assigns no sign to (25). This pinpoints the missing link: a useful application must estimate this signed coupling with the canonical data and pay the complementary current. Optimizing (6) alone does not establish it. No numerical optimization is launched before that question is selected.

## 5. Controls, verification, and continuation

All of (1)–(25) hold for smooth radial sources on the stated domains. The Gaussian-polynomial double event from Note22 survives (18)–(19) exactly. The source cost can decrease strictly for that colliding control too. The smooth Euler-factor, weighted-square, finite-prime, reflected, shape, and primitive controls likewise retain their observations; their failed canonical premises are in [Brainstorm01's table](../brainstorm/01_RADIAL_INTEGRAND_PRESERVING_DEFORMATIONS_AND_COLLISION_LOCALIZATION_20261027.md). None fails a hypothesis of this generic bounded theorem on an admissible smooth slice. Atomic sources are outside this smooth-source setup; no numerical collision certificates were rerun. There is no claim that merely lacking theta's exact marginal causes failure of an unproved signed inequality.

[Review13](../reviews/13_TUBE_COMPARISON_AND_PROJECTED_FLOW_SELF_ASSESSMENT_20261027.md) checks the signs, spaces, coercivity, corner regularity, join term, averaged boundary observation, projected spectral derivative, and adjoint. The [small check record](../numerics/14_TUBE_AND_PROJECTED_FLOW_CHECKS_20261027.json) covers exact control algebra and floating differential/geometry diagnostics only; it is not a numerical simulation or certification of the infinite-dimensional flow. No manuscript edit or build is included in this return.

**Next bounded question:** choose a finite tube/cutoff and canonical parameter box, and compare the exact local functional (22), its complementary boundary/cutoff current, and the adjoint allowance (23)–(24) against the same radial information. In particular test whether any usable signed relation between k_η and h is supplied by the full theta source. A positive source-cost reduction is already proved and should not be counted again as a collision gain. If the complete local comparison reduces to the same radial information, record that limitation for this particular response operator before adding more geometry.

The proof of the bounded flow and its exterior response is now available for LOC-01/03. LOC-04's theta-specific estimate and LOC-05's time, height, multiplicity, and tail coverage remain open. There is no positive-threshold contradiction.

This session is uniquely registered as chat0008, thread `01a1806f-45ba-7f42-ba76-f552c6ac0210`, in the investigation's [registry](../chat-histories/index.json). Preserve chat0007 and all earlier identities. Begin/end future replies with the standing history workflow, using the actual current turn id for the bounded final capture.
