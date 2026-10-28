# Radial Darboux systems preserving the physical observation

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0006, **Review radial collision progress**, thread `01a18012-c543-7320-ab04-91728654f3ba`.

**Status: exploratory construction with exact identities proved here and same-assistant checking.** A continuous family of forced radial equations with an additional radial potential has exactly the same physical observation H and the same spectral multiplicities. An explicit integral is independent of the deformation parameter. The ordinary complete energy identity is also transported, with its forcing and boundary terms retained. No stronger collision estimate is established.

Edward Baker proposed deforming a three-dimensional system while retaining the relevant integral and radial form. This is distinct from the identical-information estimator comparison in [Note16][n16] and the changed-observation Gaussian deformation in [Note04][n04]. Equality of representations does not preclude discovering a useful estimate in one of them. This construction makes one such alternative precise without declaring the broader radial program unsuccessful.

The [result index][results] and [avoid index][avoid] apply, especially [controls][controls], [target classification][a01], [coordinate comparisons][a03] and [scoped conclusions][a07]. This is a representation and a comparison of exact identities, not an acquired criterion excluding collisions. The next consumer would be a genuinely stronger estimate for the transformed forced response.

## 1. The unchanged observation and a classical transformation

Use [Note01][n01]'s complete source and selected response on x>=0:

\[
x=\log r,\quad \lambda=a^2/4>0,\quad
g_t(x)=4e^{tx^2/4}\Phi(x/2),
\]
\[
Y''+\lambda Y=g_t,\qquad Z=Y_\lambda,
\qquad B=Y'(0)=-8H(t,2\sqrt\lambda).
\tag{1}
\]

Primes mean x derivatives. Y is the specified Volterra response; it and its parameter derivatives decay faster than every fixed exponential at infinity. Fix any finite time slab 0<=t<=T, any compact positive lambda range, and any finite deformation range 0<=kappa<=K. The statements also hold pointwise at every finite real time and positive lambda. No theta coefficients are modified in the defining source g_t.

For kappa>=0 set

\[
w=\kappa\tanh(\kappa x),\quad A=\partial_x-w,
\quad w'+w^2=\kappa^2,\quad w(0)=0,
\]
\[
U_\kappa=AY,\qquad V_\kappa=AZ=(U_\kappa)_\lambda,
\qquad h_\kappa=Ag_t.
\tag{2}
\]

This is the classical Darboux construction with nonvanishing seed cosh(kappa x). The [reference annotation][ref] records the checked factorization convention in Kravchenko and Torba, Section 3.1, equations (42)-(43). The forced equations, physical map and comparisons below are derived directly here; no spectral simplicity theorem is imported.

Factorization gives

\[
(\partial_x+w)(\partial_x-w)=\partial_x^2-\kappa^2,
\]
\[
(\partial_x-w)(\partial_x+w)=\partial_x^2-\kappa^2+2w'.
\]

Consequently

\[
U_\kappa''+(\lambda+2w')U_\kappa=h_\kappa,
\qquad
V_\kappa''+(\lambda+2w')V_\kappa=-U_\kappa,
\tag{3}
\]

where 2w'=2kappa^2 sech^2(kappa x). These are still forced equations. Their selected tails are the transformed original tails, not a new unspecified decay condition. The reverse identity

\[
Y=\frac{g_t-(\partial_x+w)U_\kappa}{\lambda+\kappa^2}
\tag{4}
\]

has no singular denominator in the stated physical range. At kappa=0, U_0=Y' is the differentiated free realization; (4) recovers Y. Thus the continuous family starts from that exact reformulation of the original response.

## 2. The boundary value and an integral are preserved exactly

Since w(0)=0 and w is independent of lambda,

\[
\boxed{U_\kappa(0)=B=-8H(t,2\sqrt\lambda),\qquad
V_\kappa(0)=B_\lambda.}
\tag{5}
\]

The physical first jet is therefore

\[
H(t,a)=-U_\kappa(0)/8,\qquad
H_a(t,a)=-aV_\kappa(0)/16.
\]

All finite positive-frequency multiplicities are unchanged. A multiple event becomes the pair of Dirichlet values U_kappa(0)=V_kappa(0)=0 in every member of the family, at the same time and frequency.

The auxiliary deformation itself has the explicit local evolution

\[
\partial_\kappa U_\kappa
=-\frac{\partial_\kappa w}{\lambda+\kappa^2}
 [g_t-(\partial_x+w)U_\kappa],\qquad
\partial_\kappa h_\kappa=-(\partial_\kappa w)g_t.
\]

Here partial_kappa w=tanh(kappa x)+kappa x sech^2(kappa x), which vanishes at x=0. This directly explains the fixed boundary observation along the deformation. No bounded semigroup on an unspecified function space is asserted.

An explicit conserved integral removes any reliance on unknown boundary data. Write c=lambda+kappa^2 and

\[
p_\kappa(x;\lambda)=
\frac{\sqrt\lambda\sin(\sqrt\lambda x)+w(x)\cos(\sqrt\lambda x)}{c}.
\tag{6}
\]

Then p_kappa(0)=0, p_kappa'(0)=1 and

\[
p_\kappa''+(\lambda+2w')p_\kappa=0,
\qquad p_\kappa'+wp_\kappa=\cos(\sqrt\lambda x).
\]

One integration by parts proves

\[
\boxed{\int_0^\infty p_\kappa(x;\lambda)
        [g_t'(x)-w(x)g_t(x)]\,dx
 =-\int_0^\infty g_t(x)\cos(\sqrt\lambda x)\,dx
 =-8H(t,2\sqrt\lambda).}
\tag{7}
\]

The lower boundary is zero because p_kappa(0)=0. The outer boundary vanishes by the complete source tail and bounded oscillatory kernel. Parameter derivatives are justified on the declared compact sets by the same source domination. The integral is exactly independent of kappa; its lambda derivatives are preserved as well. Source and test solution both change, with their changes coupled by the operator factorization.

## 3. The three-dimensional radial form and physical time

Put psi_kappa(r)=r^(-1/2)U_kappa(log r), r>=1. Direct differentiation gives

\[
\Delta_3[r^{-1/2}u(\log r)]
=r^{-5/2}(u''-u/4).
\]

Thus (3) is the genuine radial equation

\[
\boxed{\left[\Delta_3+
\frac{(1+a^2)/4+2\kappa^2\operatorname{sech}^2(\kappa\log r)}{r^2}
\right]\psi_\kappa(r)
=r^{-5/2}h_\kappa(\log r).}
\tag{8}
\]

The ordinary three-dimensional radial Laplacian and rotational symmetry remain. An additional radial potential changes with kappa. This deforms the forced observation equation, rather than asserting that the original normalized Poisson potential solves an unchanged equation.

Since Q_t=r^(-5/2)g_t(log r), its transformed forcing is explicitly

\[
r^{-5/2}h_\kappa(\log r)
=r\partial_r Q_t+(5/2-w(\log r))Q_t.
\tag{9}
\]

It need not be positive or retain Q_t's Kelvin parity: g_t is even and h_kappa is odd in x. Formula (7) already represents the complete physical observation on the exterior; no second interior copy is added. The coefficients use the specified source and kappa, with no unknown zeros or H-dependent boundary conditions.

Physical Newman time has its complete transformed law:

\[
\partial_tg_t=\frac{x^2}{4}g_t,\qquad
\partial_t h_\kappa=\frac{x^2}{4}h_\kappa+\frac{x}{2}g_t.
\tag{10}
\]

The extra source term is essential. Kappa labels an auxiliary deformation, not physical time; no radial heat-diffusion law is being substituted. Equation (7) preserves the original physical equation H_t=-H_aa.

## 4. What the complete energy identity retains

For real parameters define

\[
I=\int_0^\infty(Y^2+g_tZ)\,dx
=Y(0)B_\lambda-BZ(0),
\]
\[
I_\kappa=\int_0^\infty(U_\kappa^2+h_\kappa V_\kappa)\,dx.
\]

The full transformed boundary values are

\[
U_\kappa'(0)=g_t(0)-cY(0),\qquad
V_\kappa'(0)=-Y(0)-cZ(0).
\]

Applying the Wronskian identity to (3) therefore gives

\[
\boxed{I_\kappa=cI-Y(0)B-g_t(0)B_\lambda.}
\tag{11}
\]

It can also be checked without a Wronskian: integration by parts gives
integral (AY)^2=c integral Y^2-integral g_tY-Y(0)B and
integral (Ag_t)(AZ)=c integral g_tZ+integral g_tY-g_t(0)B_lambda.
The cross terms cancel. Every boundary at infinity vanishes, and w(0)=0 pays the lower multiplier terms.

At an event, I_kappa=cI=0. Thus the basic transformed energy identity and its kappa derivatives give no additional scalar compatibility condition there. This is a comparison of these complete identities only. A new estimate using the changed potential, source correlations or localization has not been tested or excluded.

## 5. Control and next analytic question

The exact Note01 control at lambda=6 is

\[
g_*=(16x^4+24)e^{-x^2},\quad
Y_*=(4x^2+4)e^{-x^2},\quad Z_*=-e^{-x^2}.
\]

It transforms to

\[
U_{\kappa,*}=[-8x^3-4w(x)(x^2+1)]e^{-x^2},\qquad
V_{\kappa,*}=[2x+w(x)]e^{-x^2}.
\tag{12}
\]

Both boundary values remain zero. Moreover g_*'<0 for x>0 because
g_*'=-16x[2(x^2-1)^2+1]e^(-x^2). Hence h_kappa,*<0,
U_kappa,*<0 and V_kappa,*>0 on x>0 for every kappa>=0, while their complete norm-plus-forcing integral is zero. These signs and the smooth radial potential cannot by themselves exclude a collision. The control lacks the unchanged theta arithmetic and canonical tails.

The other [registered controls][controls] likewise retain their observations whenever the stated differentiability and tail assumptions hold: Euler-factor controls change source/conductor; weighted-square and finite-prime controls change coefficients or full reflection; reflected smooth/primitive controls lack the complete square source; endpoint perturbations change ordinary Dirichlet arithmetic. Atomic sources are outside the present classical derivative formulation and would require distributional definitions. No control is claimed to fail (7) or (11), and no external control certificate was rerun.

The bounded next question is whether one specified kappa or a controlled range permits a stronger *complete* estimate for h_kappa V_kappa at the canonical event conditions, after comparison with its pullback through (2) and (4). Its exact theta premise and comparison constant must be identified before numerical work. The potential and the boundary-vanishing transformed forcing provide concrete quantities to investigate; neither has yet supplied that gain. Changing kappa merely to reproduce (11) is already decided.

This is an exploratory RLC-04 input, with possible RLC-03 support only for a selected estimate. RLC-05 has not acquired a homogeneous characteristic determinant, and RLC-06 has no additional exclusion range. No new manuscript milestone, snapshot or repository-wide result-summary claim is made. The [assessment][review] records the same-assistant verification scope.

[n01]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[n04]: 04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md
[n16]: 16_CANONICAL_FLUX_MOMENT_RESTRICTION_AND_DIRECT_COMPARISON_20261027.md
[review]: ../reviews/10_RADIAL_DARBOUX_DEFORMATION_SELF_ASSESSMENT_20261027.md
[ref]: ../references/08_DARBOUX_FACTORIZATION_AND_RADIAL_DEFORMATION_20261027.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
