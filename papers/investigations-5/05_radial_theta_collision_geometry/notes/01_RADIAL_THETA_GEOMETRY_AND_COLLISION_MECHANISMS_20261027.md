# Radial theta geometry and possible collision mechanisms

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Founding conversation: **Review three-regime heat-flow notes**, thread `01a17e68-028c-7472-8317-c38eefa4c2f0`, already registered as chat0006 in Investigation04.

**Status: initial analytical development, with elementary identities and scoped control calculations proved in-note; structural collision mechanisms remain proposals.** This investigation begins from Edward Baker's suggestion that the source variable could arise from higher-dimensional geometry, and his request to reconsider the collision argument itself as well as improve signed estimates. The natural Gaussian radius is r=e^(2u). The theta source becomes a weighted radial Laplacian in dimension three, and reflection becomes Kelvin inversion. These facts provide an exact setting in which to investigate boundary, oscillation and global collision-index arguments.

The present development goes beyond the founding [Note20][prior20] and [Note21][prior21]: it fixes the time-dependent radial potential and its boundary data, derives a forced boundary-value realization of H, and computes the forcing term in its Wronskian identity. An explicit positive Gaussian-polynomial control shows exactly why that term cannot be dropped. No canonical collision exclusion, new covered region, or improvement in the Newman constant is obtained. Proofs and verification are internal same-assistant work, with no literature-priority claim.

The [result index][results], particularly [local geometry][geometry], [theta identities][arithmetic], [geometric realizations][lifts] and [controls][controls], and the [avoid index][avoid] apply. Keep [target classification][a01], [shape controls][a02], [coordinate lifts][a03], [scoped conclusions][a07], and [coupled terms][a12] attached to their actual hypotheses.

## 1. Canonical field and the research question

Use the unchanged source and normalization

\[
\Phi(u)=\sum_{n\ge1}
 (2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad H_t=-H_{zz}.
\tag{1}
\]

The complete even continuation of Phi is used whenever u ranges over R. On u>=0 each displayed summand is positive. Theta reflection supplies evenness, and its tails justify the finite parameter differentiations below. The completed sum must precede any use of reflection; a one-sided finite sum does not inherit all its endpoint identities.

The preceding [energy calculation][energy] gives, at an event of multiplicity m,

\[
E(T+\tau)=\frac{m(m-1)}{16\tau}-2\kappa_m\gamma+O(\tau),
\qquad \kappa_m=m(m-1)/16.
\]

The bounded analytic correction cannot reduce this logarithmic coefficient. The new program keeps that tested route paused and asks whether canonical source geometry supplies a different reason an event cannot occur. It does not reopen more orders of the same bounded local expansion.

For the positive-threshold application, T=Lambda>0 is a contradiction hypothesis. A finite multiple event is supplied by the existing canonical exterior reduction, whose hypotheses remain in the [positive-threshold analysis][threshold]. Arbitrary local events, global all-real thresholds, and possible multiple zeros at t=0 are different settings. A result in one is not silently transferred to another.

## 2. The radial Laplacian selected by the source

Set

\[
r=e^{2u},\qquad A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\qquad
\Theta(r)=1+2A(r).
\]

Regard these as radial profiles on R^3 minus the origin; the integer index remains one-dimensional. Since

\[
\Delta_d e^{-\pi n^2r^2}
 =(4\pi^2n^4r^2-2d\pi n^2)e^{-\pi n^2r^2},
\]

we obtain

\[
\boxed{\Phi(u)=\tfrac12r^{5/2}\Delta_3A(r)
             =\tfrac14r^{5/2}Q(r)},\qquad Q=\Delta_3\Theta.
\tag{2}
\]

This retains the original square coefficients. Replacing the sum by a lattice in Z^3 would be a different source. The earlier primitive psi(u)=r^(1/2)A(r) obeys

\[
(\partial_u^2-1)\psi=4r^{5/2}\Delta_3A=8\Phi.
\tag{3}
\]

Thus the derivative identity motivating the discussion is exactly a radial operator conjugation. Here u is a logarithmic radius. This is distinct from treating |u| itself as a Euclidean radius.

Theta modularity and three-dimensional Kelvin covariance give

\[
\Theta(r)=r^{-1}\Theta(1/r),\qquad
Q(r)=r^{-5}Q(1/r).
\tag{4}
\]

The primary ingredients are DLMF 20.7.32 and Axler–Bourdon–Ramey Proposition 4.6; their previously checked passages and PDF provenance are linked in the [reference guide][refs]. Equation (4) turns the evenness of Phi into spherical inversion symmetry.

Theta approaches 1 at infinity and 1/r at zero. Consequently

\[
\Delta_{\mathbb R^3}\Theta=Q(|y|)-4\pi\delta_0,
\qquad \int_0^\infty Q(r)r^2dr=1.
\tag{5}
\]

The point source is essential. Positivity of Q for r>=1 follows termwise and extends to r>0 by (4). Smoothness and flat decay of Theta-1/r at zero follow from modularity. These facts justify the flux calculation in (5).

## 3. Physical observation and exact radial time evolution

Changing variables, with no truncation, gives

\[
H(t,z)=\frac18\int_1^\infty e^{(t/4)\log^2r}r^{3/2}Q(r)
 \cos\left(\frac z2\log r\right)dr
 =\frac1{16}\int_0^\infty r^{3/2+iz/2}Q_t(r)dr,
\tag{6}
\]

where

\[
Q_t(r)=e^{(t/4)\log^2r}Q(r),\qquad
\partial_tQ_t=\tfrac14\log^2r\,Q_t,
\qquad Q_t(r)=r^{-5}Q_t(1/r).
\tag{7}
\]

Both representations converge locally uniformly for finite complex t,z. The observation is Mellin-type. The radial source evolves by multiplication, not ordinary radial diffusion. It is positive for real t and remains smooth through any candidate collision time. A physical collision does not itself create a singularity in Q_t.

For comparison, applying the exterior Green identity directly to Theta-1 reproduces the earlier primitive reconstruction. With J(t,z)=integral_0^infinity exp(tu^2)psi(u)cos(zu)du,

\[
8H=\tfrac12+(2t-z^2-1)J+4tzJ_z-4t^2J_{zz}.
\]

The lower boundary at r=1 contributes exactly 1/2. Dropping it changes the source normalization. This first Green step alone does not strengthen the old estimate.

## 4. A canonical time-dependent Kelvin potential

The formal inverse Laplacian in the founding discussion can be made explicit. For real t define

\[
M_t=\int_0^\infty s^2Q_t(s)ds=16H(t,i)>0,
\tag{8}
\]

and choose the potential with rapidly decaying remainder at infinity:

\[
\boxed{\mathcal T_t(r)=M_t+
 \int_r^\infty\left(\frac{s^2}{r}-s\right)Q_t(s)ds.}
\tag{9}
\]

To prove the mass identity, substitute r=e^(2u) and use the even source: the full integral becomes 8 integral_R exp(tu^2+u)Phi(u)du, which is 16H(t,i). Also M_0=1 by (5), and M'_t=16 integral_0^infinity u^2 exp(tu^2)Phi(u)cosh(u)du>0.

Direct differentiation of (9) gives

\[
r^2\mathcal T_t'(r)=-\int_r^\infty s^2Q_t(s)ds,
\qquad \Delta_3\mathcal T_t=Q_t.
\tag{10}
\]

Inversion in (7) implies integral_0^infinity sQ_t(s)ds=M_t. Thus

\[
\mathcal T_t(r)=M_t/r+o(1)\ (r\downarrow0),\qquad
\mathcal T_t(r)-M_t=o(r^{-1})\ (r\to\infty).
\]

Kelvin covariance shows that K T_t-T_t is radial harmonic away from zero. The two displayed asymptotics force both coefficients of its form c_0+c_1/r to vanish. Hence

\[
\mathcal T_t(r)=r^{-1}\mathcal T_t(1/r),\quad
\mathcal T_0=\Theta,\quad
\Delta_{\mathbb R^3}\mathcal T_t=Q_t-4\pi M_t\delta_0.
\tag{11}
\]

The chosen condition at infinity fixes the harmonic ambiguity. Adding c(1+1/r) preserves Kelvin symmetry but introduces a 1/r tail at infinity; it changes the specified potential. The natural boundary constant and central charge are M_t, not a silently fixed 1. For real t one may normalize by M_t without changing physical zeros, but division by M_t is not asserted globally in complex time.

Let K denote the linear map in (9). Its exact potential evolution is

\[
\partial_t\mathcal T_t=K[\tfrac14\log^2r\,Q_t].
\tag{12}
\]

This fixes the nonlocal generator and its boundary rates: M'_t at infinity and M'_t/r at the origin. No bounded semigroup on an unspecified function space is claimed.

There is also an exact, time-adapted positive primitive. For u>=0 put

\[
\psi_t^{\rm rad}(u)=\tfrac12r^{1/2}(\mathcal T_t(r)-M_t),\qquad
\mathcal J_t(z)=\int_0^\infty\psi_t^{\rm rad}(u)\cos(zu)du.
\]

Then (2), (10), and the Kelvin boundary derivative at r=1 give

\[
(\partial_u^2-1)\psi_t^{\rm rad}=8e^{tu^2}\Phi,
\quad (\psi_t^{\rm rad})'(0)=-M_t/2,
\]

and integration by parts yields

\[
\boxed{\mathcal J_t(z)=
 \frac{8[H(t,i)-H(t,z)]}{1+z^2}.}
\tag{13}
\]

The apparent poles at z=+/-i are removable. For real a and t, J_t(a)>0 because cosh(u)-cos(au)>0 for u>0. This positivity follows for any suitable positive even source. The primitive here is generally different from exp(tu^2)psi(u) used in the earlier differential reconstruction. It resolves a boundary normalization and gives a useful exact auxiliary channel; it does not by itself exclude a double zero. The [positive-primitive controls][controls] remain relevant.

## 5. The homogeneous spectral operator and what its zeros mean

On L2([1,infinity),dr) set

\[
L=-\frac d{dr}\left(r^2\frac d{dr}\right),\qquad
k_a(r)=r^{-1/2}\cos\left(\tfrac a2\log r\right).
\]

Then L k_a=(1+a^2)k_a/4 and k_a'(1)+k_a(1)/2=0. Under the unitary change x=log r, (Uf)(x)=exp(x/2)f(exp x),

\[
ULU^{-1}=-\partial_x^2+\tfrac14
\]

with the Neumann condition at x=0. This is the usual half-line realization with continuous spectrum [1/4,infinity). For real a, k_a is a generalized eigenfunction, not an L2 eigenfunction. Formula (6) makes H a spectral coefficient of r^2Q_t, not the characteristic function of this fixed operator. The spectrum of L does not move with the zeros of H.

For comparison, a regular real scalar equation -(pY')'+qY=lambda wY, p,w>0, with a parameter-independent left boundary condition and normalization, and characteristic function F(lambda)=Y(c,lambda), has at a real eigenvalue

\[
p(c)Y'(c,\lambda)F'(\lambda)
 =\int_b^c wY^2dx>0.
\tag{14}
\]

This follows by differentiating the equation and using the complete Green boundary form. It excludes multiple characteristic zeros. A source-derived realization of this kind would be a different collision proof, but (6) is not such a realization. Singular or spectral-parameter-dependent boundaries need their own boundary terms. A global realization proving all positive-time physical zeros real and simple would already settle the desired positive-threshold question; it is an unconstructed structural objective, not a smaller established milestone.

## 6. A forced boundary equation whose boundary derivative is exactly H

The source-to-boundary connection can nevertheless be made exact without inserting unknown zeros. Define

\[
g_t(x)=4e^{tx^2/4}\Phi(x/2),\quad x\ge0,\qquad
\lambda=a^2/4,
\]

and, with the entire limiting value at lambda=0,

\[
Y(t,x;\lambda)=\int_x^\infty
 \frac{\sin(\sqrt\lambda(s-x))}{\sqrt\lambda}\,g_t(s)ds.
\tag{15}
\]

Its derivatives decay faster than every fixed exponential at infinity, locally uniformly in the parameters. The integral specifies this tail condition; merely requiring decay at complex lambda could leave decaying homogeneous solutions. Direct differentiation gives

\[
Y_{xx}+\lambda Y=g_t,\qquad
B(t,\lambda):=Y_x(t,0;\lambda)
 =-\int_0^\infty g_t(s)\cos(\sqrt\lambda s)ds
 =-8H(t,2\sqrt\lambda).
\tag{16}
\]

Evenness of H makes the last expression entire in lambda. A nonzero real event a>0 has lambda>0, and

\[
B_\lambda=-\frac{16}{a}H_a.
\tag{17}
\]

Thus a physical double zero is exactly a double zero of this boundary residual. The construction uses the full source and is inhomogeneous. At H=0, Y satisfies a Neumann condition, but it still solves the forced equation, so it is not an eigenfunction of the homogeneous half-line operator.

Differentiate (16) in lambda. With W=Y Y_{\lambda x}-Y_xY_\lambda,

\[
W_x=-Y^2-g_tY_\lambda.
\]

All outer boundary terms vanish by the actual source tails. Therefore, for real t,lambda,

\[
\boxed{Y(0)B_\lambda-BY_\lambda(0)
 =\int_0^\infty Y^2dx+\int_0^\infty g_tY_\lambda dx.}
\tag{18}
\]

At a double zero both boundary terms on the left vanish. The forcing term must then cancel the positive norm. That is the exact term absent from the naive eigenvalue-simplicity argument. It cannot be discarded or assigned a favorable sign because g_t is positive.

For lambda>0 its coupled source form is explicit. Put omega=sqrt(lambda) and

\[
C_t(\lambda)=\int_{0\le x\le s<\infty} g_t(x)g_t(s)
 \frac{\omega(s-x)\cos(\omega(s-x))-\sin(\omega(s-x))}
      {2\omega^3}\,ds\,dx.
\tag{19}
\]

This is exactly the second integral in (18); absolute convergence follows from the tails. At lambda=0 use -(s-x)^3/6. This identifies a complete forcing term, not an independently acquired theta sign. Equation (18), including its event specialization, is a reformulation of the boundary residual identity and is not counted as an exclusion criterion with supporting evidence.

Higher multiplicities have an exact derivative hierarchy. Set Y_j=partial_lambda^j Y. Then

\[
(\partial_x^2+\lambda)Y_j=-jY_{j-1}\quad(j\ge1),
\qquad B_j=(Y_j)_x(0).
\tag{19a}
\]

At a spatial zero of multiplicity m with a>0, B_0 through B_(m-1) vanish because a -> lambda is locally invertible. This is an inhomogeneous hierarchy, not a closed homogeneous finite-jet system. No double-zero reduction of an exclusion theorem is assumed.

The actual t derivative remains forced: (partial_x^2+lambda)Y_t=(x^2/4)g_t, with the differentiated tail condition. No homogeneous radial heat equation is substituted.

### Exact transfer system and time compatibility

Because the canonical g_t is positive for real t, define q_t(x)=partial_x log g_t(x). It is an independently specified source coefficient, not a function of unknown physical zeros. Its time dependence is particularly simple:

\[
q_t(x)=q_0(x)+tx/2,\qquad q_t(0)=0.
\]

The actual state has the closed spatial transfer system

\[
\partial_x\begin{pmatrix}Y\\V\\g_t\end{pmatrix}
 =\begin{pmatrix}0&1&0\\-\lambda&0&1\\0&0&q_t\end{pmatrix}
  \begin{pmatrix}Y\\V\\g_t\end{pmatrix},\qquad V=Y_x.
\tag{19b}
\]

Equivalently, (partial_x-q_t)(partial_x^2+lambda)Y=0, with the original source amplitude and tail condition retained. This scalar third-order homogenization is noncircular, but generic: every positive smooth source admits it. Its real third-order leading term changes sign under formal adjoint, so it is not the scalar self-adjoint second-order problem used in (14). Multiplying by another operator does not automatically preserve the physical boundary function or remove its derivative terms. The transfer system supplies an exact starting point, not a simplicity theorem.

There is also a complete response evolution, beyond the forced equation for Y_t:

\[
\boxed{Y_t=\frac{x^2}{4}Y+x\partial_xY_\lambda
                 -\frac32Y_\lambda-\lambda Y_{\lambda\lambda}.}
\tag{19c}
\]

To verify it, write A=partial_x^2+lambda. Then A(x^2Y/4)=x^2g_t/4+xY_x+Y/2, A(x partial_xY_lambda)=-xY_x-2lambda Y_lambda-2Y, A Y_lambda=-Y, and A Y_lambdalambda=-2Y_lambda. Their displayed combination gives x^2g_t/4=A Y_t. Both sides obey the selected super-exponential tail condition, so their homogeneous difference vanishes. At x=0, differentiation gives

\[
B_t=-\lambda B_{\lambda\lambda}-\tfrac12B_\lambda,
\tag{19d}
\]

exactly the physical backward heat equation under a=2sqrt(lambda). Thus (19b)-(19c) are compatible higher-variable dynamics with the correct boundary reduction. They do not alter the universal local collision unfolding, and the lambda derivatives do not form a closed finite jet in time. The useful next question is what additional canonical relation or current these equations support beyond their validity for generic sources.

## 7. An exact positive control for the missing Wronskian term

This control tests the proposed use of positivity in (18), not theta's full arithmetic. Let h(x)=exp(-x^2), freeze the positive source

\[
g_*(x)=(\partial_x^2+6)^2h(x)
       =(16x^4+24)e^{-x^2}>0.
\tag{20}
\]

At lambda=6, the rapidly decaying solution and its derivative with respect to lambda while g_* is held fixed are

\[
Y_*=(\partial_x^2+6)h=(4x^2+4)e^{-x^2}>0,
\qquad (Y_\lambda)_*=-h.
\tag{21}
\]

Both have zero Neumann derivative at zero, so B=B_lambda=0. Equivalently, integration by parts in the Gaussian cosine transform gives

\[
\int_0^\infty g_*(x)\cos(\sqrt\lambda x)dx
 =\frac{\sqrt\pi}{2}(\lambda-6)^2e^{-\lambda/4}.
\tag{22}
\]

The boundary residual has an exact double zero. All half-line boundary integrations are valid because the odd Gaussian derivatives vanish at zero. In (18),

\[
\int_0^\infty Y_*^2dx
 =\frac{27\sqrt\pi}{2\sqrt2},\qquad
\int_0^\infty g_*(Y_\lambda)_*dx
 =-\frac{27\sqrt\pi}{2\sqrt2}.
\tag{23}
\]

This verifies the complete cancellation. Even positivity of both the source and the forced response does not repair the generic Wronskian argument.

For a prescribed T>0, this can be embedded in the local backward-heat family with positive even source

\[
\Phi_*(u)=(64u^4+6)e^{-(4+T)u^2}.
\]

At t=T its field equals sqrt(pi)(a^2/4-6)^2 exp(-a^2/16)/16 and has exact double zeros at a=+/-2sqrt(6). The integral is defined for Re(t)<T+4. This is a local positive-time collision control; no global finite Newman threshold or canonical all-time growth is asserted. It lacks the integer-square theta expansion, canonical completion and double-exponential tails.

This closes only the attempt to remove the forcing term using positivity of g and Y in the displayed forced equation. It does not rule out a theta-specific closure of that term, a different operator, or a global collision argument.

## 8. Earlier tools and the remaining structural choices

There are two distinct three-dimensional source constructions. The earlier [radial inverse marginal][oldradial] has

\[
m_t(u)=e^{tu^2}\Phi(u),\quad
R_t(\rho)=-m_t'(\rho)/(2\pi\rho),\quad
H(t,z)=\tfrac12\int_{\mathbb R^3}e^{izv_1}R_t(|v|)dv.
\]

Its positivity is proved in the source note for 0<=t<=1/20, and its generator is rho^2 R-2 integral_rho^infinity R(s)s ds. Its Euclidean radius rho is not r=e^(2u). Its Bessel projection and boundary bookkeeping are reusable if that route is selected; its positivity control prevents a generic radial-positivity argument.

The [geometric summary][lifts] supplies signed Hodge/Green identities, source-constrained trace methods, and exact quaternionic and octonionic lifts. Those constructions do not automatically change the physical generator or remove forcing. The immediate question in (18) is already scalar and radial, so a higher lift should be introduced only for a concrete source equation or current it adds.

The [local geometry summary][geometry] supplies the alternative global-index route. At a double event the physical map (t,a)->(H,H_a) has Jacobian determinant -H_aa^2<0. General multiplicity m has inherited real index -floor(m/2). All collisions therefore contribute with the same sign. An independently established zero boundary degree on a controlled region would exclude interior events, but Kelvin symmetry itself does not supply that degree. The reflected events at a and -a have equal indices. Any source-derived deformation has to retain moving walls, boundary zeros and source forcing.

For every sufficiently decaying even source m, Q_m(r)=4r^(-5/2)m(log(r)/2) has the same weight-five Kelvin covariance. Positive even controls share this part of the dictionary. The [control register][controls] distinguishes their missing premises: weighted-square/finite-tail controls lack a global all-real heat time; reflected and positive-primitive controls lack the canonical square arithmetic; Euler-factor threshold controls alter the conductor/source. No single missing property is assigned to every control.

## 9. Research priorities and first bounded return

The program has three possible mechanisms: a source-derived characteristic or nodal realization; a global continuation/index argument; and improved coupled Green estimates if a concrete consumer warrants them. The first two change the collision argument itself. None is yet established for the canonical source.

The next bounded task is to analyze the exact forcing in (18) using the complete theta coefficients and their radial Gaussian equations. Each underlying mode satisfies (partial_r+2 pi n^2 r)exp(-pi n^2r^2)=0; the physical source contains its prescribed differential combination. Derive the full commutators, time multiplier and boundary terms before summing. Determine whether the combined theta identities add a collision-relevant relation to the exact generic transfer system (19b), or leave a residual requiring genuinely new arithmetic information. Simply deriving the logarithmic derivative q_t or the third-order homogenization again is not that relation. A finite jet truncation is not a closed system unless its residual is retained.

A useful return is an independently derived closure relation, a bound or invariant on a declared domain that changes the collision implication, or a precise obstruction for the selected construction. Reproducing B=-8H, (18), radial positivity, or the same local Hermite polynomial is not that return. Keep the control (20) alongside the calculation to identify where canonical information first matters. A direct numerical campaign is not the first task.

The [overview][overview] specifies the research tasks; the [progress register][progress] distinguishes completed exact diagnostics from open exclusion mechanisms. No task ownership or status in the sibling investigations is changed by opening this program.

[prior20]: ../../04_three_regime_heat_flow_dynamics/notes/20_THREE_DIMENSIONAL_RADIAL_THETA_AND_KELVIN_REDUCTION_20261027.md
[energy]: ../../04_three_regime_heat_flow_dynamics/notes/10_COUPLED_CURVATURE_AND_ENERGY_BUDGET_20261027.md
[threshold]: ../../02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[refs]: ../references/README.md
[overview]: ../research-overview/01_RADIAL_THETA_COLLISION_RESEARCH_OVERVIEW_20261027.md
[progress]: ../research-progress/01_RADIAL_THETA_COLLISION_RESEARCH_PROGRESS_20261027.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[arithmetic]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[lifts]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[oldradial]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/notes/1_POSITIVE_THREE_DIMENSIONAL_THETA_LIFT_AND_NONLOCAL_GENERATOR_20261010.md

[prior21]: ../../04_three_regime_heat_flow_dynamics/notes/21_COLLISION_MECHANISMS_IN_THE_RADIAL_REPRESENTATION_20261027.md
