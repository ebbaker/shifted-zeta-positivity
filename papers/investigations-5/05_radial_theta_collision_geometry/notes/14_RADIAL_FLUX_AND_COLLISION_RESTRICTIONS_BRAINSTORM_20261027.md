# Radial flux and possible restrictions on collisions

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Research conversation **Explore 3D Laplacian collision rules**, Investigation05 chat0004, thread `01a17fce-4841-7672-b275-325823e098f4`.

**Status: brainstorming with direct analytical derivations.** The useful immediate possibility is to use radial charge and flux to estimate the two collision observations together. The Laplacian supplies a simpler positive expression for the flux, including at positive Newman time. It also identifies why unqualified energy positivity is unavailable: the logarithmic observation has an inverse-square coupling above the radial Hardy threshold at every nonzero real frequency. Neither observation excludes a canonical collision or supplies a new certified region.

This continues [Note13][n13], the pre-lattice development in [Note01][n01] and [Note05][n05], and the discussion in [chat0002][chat2]. The [result index][results] and [avoid index][avoid] apply, particularly [collision controls][controls], [target classification][a01], [coordinate realizations][a03], [scoped conclusions][a07], and [coupled estimates][a12]. The proposed finite-domain comparison below is a possible milestone whose numerical gain must be measured. A global no-collision conclusion is the unresolved target, not an additional consequence of these identities. This note does not change the recorded count of bounded research returns.

## The collision conditions in radial variables

Retain the original theta arithmetic and notation:

\[
\Theta(r)=1+2\sum_{n\ge1}e^{-\pi n^2r^2},\qquad
Q=\Delta_3\Theta,\qquad
Q_t(r)=w_t(r)Q(r),\quad
w_t(r)=e^{t\log^2r/4}.
\]

For real t, Q_t is positive. With a real frequency a and
\(\theta=(a/2)\log r\),

\[
8\begin{pmatrix}H(t,a)\\H_a(t,a)\end{pmatrix}
=\int_1^\infty r^2Q_t(r)\,
\underbrace{r^{-1/2}
\begin{pmatrix}\cos\theta\\-(\log r/2)\sin\theta\end{pmatrix}}_{K_a(r)}\,dr.
\tag{1}
\]

A multiple real zero at a>0 requires both components to vanish. Thus the source has to cancel both an oscillating radial mode and its frequency derivative. Ordinary zeros must remain possible; a useful exclusion concerns simultaneous cancellation. Formula (1) uses the exterior r>=1. The inversion-related interior has already been incorporated in the canonical cosine observation, so it must not be added a second time.

The modular and Kelvin inputs are [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32) and Axler–Bourdon–Ramey, [Proposition 4.6](https://www.axler.net/HFT.pdf), printed p.62. These passages were revisited for this discussion. Their existing [reference annotation][refs] retains the canonical PDF provenance. The calculations below are direct consequences, not imported collision theorems.

## A simpler flux that survives positive Newman time

Use the normalized potential from Note01 and define its outward tail-charge factor

\[
S_t(r)=\int_r^\infty s^2Q_t(s)\,ds
       =-r^2\mathcal T_t'(r).
\tag{2}
\]

Then S_t>0 and S_t'=-r^2Q_t<0. The ordinary outward flux of the potential is -4 pi S_t. At time zero the flux is particularly simple:

\[
\boxed{S_0(r)=4\pi r^3\sum_{n\ge1}n^2e^{-\pi n^2r^2}.}
\tag{3}
\]

The difference of the n^4 and n^2 terms in the source has become a single positive n^2-weighted Gaussian sum. At general time, integration by parts in (2) gives

\[
\boxed{
S_t(r)=w_t(r)S_0(r)
+\frac t2\int_r^\infty
\frac{\log s}{s}w_t(s)S_0(s)\,ds.}
\tag{4}
\]

The outer boundary w_t S_0 vanishes by Gaussian decay. Equation (4) is valid at finite real t; **both displayed terms are positive on r>=1 when t>=0**. It retains the correction caused by the time weight. Substituting only w_t S_0 would be incorrect for nonzero t.

The full exterior observation can also be written with this one decreasing flux:

\[
16H(t,a)=2S_t(1)-
\int_1^\infty r^{-3/2}S_t(r)
\{\cos\theta+a\sin\theta\}\,dr,
\tag{5}
\]

\[
16H_a(t,a)=-\int_1^\infty r^{-3/2}S_t(r)
\left\{\left(1-\frac{\log r}{2}\right)\sin\theta
+\frac{a\log r}{2}\cos\theta\right\}\,dr.
\tag{6}
\]

To derive (5), write 8H=-integral k_a S_t', where
k_a=r^(-1/2) cos(theta), and integrate once. The lower endpoint is S_t(1), and the upper endpoint vanishes. Differentiation in a gives (6). The boundary normalization is fixed by Kelvin symmetry:

\[
2S_t(1)=\mathcal T_t(1),\qquad
S_t(0+)=M_t=16H(t,i).
\]

These are two different quantities; S_t(1) must not be replaced by M_t. Integrating (5) again through the potential returns Note01's primitive description. The gain here is the simpler positive flux and its shell masses, not a new simplicity theorem.

## A bounded test using the charges of logarithmic shells

Fix a compact time-frequency rectangle before evaluating anything. Choose radii 1=R_0<R_1<...<R_N, with enough resolution for the phases throughout that rectangle. Gauss' law gives the exact charge factor in each shell:

\[
q_j(t)=\int_{R_j}^{R_{j+1}}r^2Q_t(r)\,dr
=S_t(R_j)-S_t(R_{j+1})>0.
\tag{7}
\]

Because the measure in (7) is positive, its contribution to (1) lies in

\[
q_j(t)\,\operatorname{conv}\{K_a(r):R_j\le r\le R_{j+1}\}.
\tag{8}
\]

Here conv denotes the convex hull. Sum these sets and include a rigorous enclosure for the entire outer tail. If the resulting set excludes the origin, simultaneous vanishing is impossible on the declared parameters. An explicit separating direction gives a scalar inequality involving H and H_a together.

This gives a concrete consumer for flux estimates: how much of the two-component cancellation is compatible with the actual theta charge in successive shells? Equations (3)-(4) provide the complete canonical charge, with Gaussian tails and unchanged unit coefficients. Adjacent charges share endpoint fluxes, so their uncertainty should remain coupled. The shell boundaries and the tail also have to be treated uniformly on the chosen parameter rectangle.

The same method can be expressed in u. A change of coordinates cannot improve the best estimate from identical information. The comparison must therefore use the same source, parameter domain, and tail/rounding budget. A worthwhile return would be a larger certified margin, reduced evaluation cost, or a precise demonstration that this flux representation loses to direct two-jet integration. Monotonicity of S_t alone is not enough. Equations (5)-(6) also show why separately bounding the boundary term and every integral can be expensive at high frequency.

## Why the standard energy argument does not apply automatically

The radial observation mode obeys

\[
\Psi_a(r)=r^{-1/2}\cos\left(\frac a2\log r\right),\qquad
\left(-\Delta_3-\frac{1+a^2}{4r^2}\right)\Psi_a=0.
\tag{9}
\]

There is an elementary way to see the relevant energy threshold without importing a spectral theorem. Let f(r)=r^(-1/2)v(log r), with v smooth and compactly supported. After removing the common angular factor 4 pi,

\[
\boxed{
\int_0^\infty
\left(r^2|f'|^2-\frac{1+a^2}{4}|f|^2\right)dr
=\int_{\mathbb R}\left(|v'|^2-\frac{a^2}{4}|v|^2\right)dx.}
\tag{10}
\]

Indeed f'=r^(-3/2)(v'-v/2), and the cross term integrates to zero for compact support. At a=0 this gives the radial Hardy inequality with constant 1/4. For a!=0, a sufficiently long plateau in v makes the right side negative. Thus the shifted operator relevant to the physical mode is not nonnegative on unrestricted annuli. The mode itself also lacks the compact-support and finite-energy hypotheses of this calculation.

On a Dirichlet annulus of logarithmic width L, the elementary interval Poincare inequality instead gives the lower bound

\[
\left(\frac{\pi^2}{L^2}-\frac{a^2}{4}\right)
\int |v|^2dx.
\tag{11}
\]

This suggests local estimates when |a|L<2 pi, but it applies to functions vanishing at both annular endpoints. The physical response does not acquire these boundary conditions by restriction. Cutoff derivatives, interface terms and forcing must be paid before (11) has a collision application. The resulting localization scale is proportional to 1/|a| in logarithmic radius.

## Two more ambitious mechanisms

**Use the candidate event in a coupled forced equation.** Note01 supplies

\[
Y_{xx}+\lambda Y=g_t,\quad
Z_{xx}+\lambda Z=-Y,\quad
g_t(x)=4e^{tx^2/4}\Phi(x/2),\quad \lambda=a^2/4,
\]

with selected tails and Z=Y_lambda. A multiple zero imposes Y_x(0)=Z_x(0)=0. Its complete identity is

\[
0=\int_0^\infty Y^2dx+\int_0^\infty g_tZ\,dx.
\tag{12}
\]

An event-conditioned Rellich or Pohozaev identity, or a localized source-dependent comparison, could constrain the cancellation in (12). A useful calculation must use the complete canonical source quantitatively. Positivity of g_t, positivity of Y, or an arbitrary scalar multiplier cannot do this: the explicit control in Note01 realizes (12), and Note05 proves a sign change for its tested modular integrand on theta itself. This leaves different coupled identities and signed estimates open. No favorable sign for an uncomputed term is proposed here.

**Construct a genuine homogeneous characteristic problem.** A real scalar Sturm-Liouville problem with positive weight and separated, parameter-independent boundary conditions has a norm identity preventing multiple characteristic zeros. The radial Laplacian is a natural starting operator, but H is currently a source coefficient, not its characteristic determinant. One would need an operator and domain specified from theta, plus an identity D_t(a)=c_t(a)H(t,a), with c_t nonzero on the claimed domain and the complete spectral boundary terms checked. H-dependent coefficients or boundary conditions would assume the target. This remains a long-term construction problem rather than an available consequence of (9).

The global-index route in Note04 likewise still needs a bound on the complete physical boundary. Conservation of total radial charge does not supply that bound: the charge changes with M_t, and oscillatory cancellations can change while positive source geometry remains regular.

## Collision controls and the scope of the proposals

The reason geometric positivity is insufficient can be expressed directly. For any suitable positive even source m(u), set

\[
Q_m(r)=4r^{-5/2}m(\tfrac12\log r).
\tag{13}
\]

It has the same positive radial source and Kelvin covariance. With the source tails required in Note01, it also has the same normalized Poisson construction and decreasing tail flux. Consequently the exact positive control

\[
\Phi_*(u)=(64u^4+6)e^{-(4+T)u^2},\qquad T>0,
\]

inherits this geometry, while

\[
H_*(T,a)=\frac{\sqrt\pi}{16}
\left(\frac{a^2}{4}-6\right)^2 e^{-a^2/16}
\]

has double zeros at a=+/-2sqrt(6). Its heat-integral domain is Re(t)<T+4. It is a local control, not a claim about a finite all-real threshold. It fails the unchanged theta coefficients and canonical tails. The exact control algebra and event are already recorded in Note01; they are not new numerical evidence here.

The remaining [registered controls][controls] give the following premise screen. This uses their recorded results; it does not claim to rerun their certificates.

| Control | Premise missing from a canonical flux estimate or limitation of the comparison |
| --- | --- |
| Euler-factor controls | The source and conductor change; broad positivity, completion and heat evolution do not distinguish them |
| Finite weighted-square and finite-tail controls | Unit coefficients and full reflection fail; matched finite endpoints do not repair this, and their local events are not finite all-real thresholds |
| Finite-prime-compatible controls | Selected arithmetic identities survive, but full normalized reflection and the complete canonical coefficients do not |
| Reflected smooth and positive-primitive controls | Positive radial geometry and the auxiliary channel survive; the complete integer-square theta source does not |
| Finite-profile atomic or compact controls | Full theta arithmetic, profile growth and eventual-simplicity inputs are absent; atomic sources need measure versions of the formulas |
| RH-conditional endpoint perturbations | Their prescribed closeness and completion do not preserve the ordinary canonical Dirichlet arithmetic |

The uncomputed numerical margin in (8), rather than its convexity alone, would have to distinguish a control. No control fails the generic convex enclosure statement. Likewise, failure of these controls to be theta does not establish that the canonical estimate has a favorable margin.

The recommended next calculation is the bounded shell-charge comparison in (7)-(8), retaining both observations and measuring its complete cost against direct integration. The harder structural question is whether theta supplies a coupled identity under the two event boundary conditions that rules out the forcing cancellation. These are separate tasks; the flux simplification makes the first concrete without claiming to solve the second.

[n01]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[n05]: 05_MODULAR_WRONSKIAN_WEIGHT_AND_CANONICAL_SIGN_OBSTRUCTION_20261027.md
[n13]: 13_RADIAL_LAPLACIAN_CONTINUATION_20261027.md
[chat2]: ../chat-histories/0002_2026-10-27T19-50-22Z_review-radial-theta-collision-work.json
[refs]: ../../04_three_regime_heat_flow_dynamics/references/03_RADIAL_LAPLACIAN_AND_KELVIN_REFERENCES_20261027.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
