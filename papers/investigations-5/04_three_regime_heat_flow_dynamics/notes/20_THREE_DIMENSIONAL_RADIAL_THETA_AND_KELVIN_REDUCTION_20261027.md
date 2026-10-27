# Three dimensional radial theta and Kelvin reduction

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Chat0006, thread `01a17e68-028c-7472-8317-c38eefa4c2f0`. Edward Baker proposed interpreting the source variable geometrically and reusing earlier dimensional-reduction results after the parameter identity in [Note19][n19].

**Status: exact elementary radial dictionary and a feasibility assessment.** Direct differentiation, theta modularity, and a complete radial Green identity give the statements below. This is an internal analytical check, with no numerical research, specialist validation, literature-priority claim, new signed margin, or collision exclusion. The [result index][results], particularly [geometric realizations][geometry] and [theta identities][arithmetic], and the [avoid index][avoid], particularly [generic lifts][a03], [scope][a07], and [coupled estimates][a12], retain their stated scopes.

## The source selects a three dimensional radial operator

The natural Euclidean radius for the Gaussian expression is

\[
r=e^{2u},\qquad u=\tfrac12\log r,
\qquad A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\quad r>0.
\tag{1}
\]

Regard A(|y|) as a radial profile on R^3 minus the origin. This retains the original one-dimensional integer-square index n; it is not a replacement by a sum over Z^3. For radial functions,

\[
\Delta_d f=f''+\frac{d-1}{r}f',\qquad
\Delta_d e^{-\pi n^2r^2}
 =(4\pi^2n^4r^2-2d\pi n^2)e^{-\pi n^2r^2}.
\]

The coefficient of the second source term forces d=3 in this Gaussian radial construction:

\[
\boxed{\Phi(u)=\frac12r^{5/2}\Delta_3 A(r),\qquad r=e^{2u}.}
\tag{2}
\]

Indeed the two terms on the right are 2 pi^2 n^4 r^(9/2) and -3 pi n^2 r^(5/2), times the Gaussian. These are exactly the original e^(9u) and e^(5u) terms. All differentiations converge locally uniformly for r>0.

The old primitive is psi(u)=r^(1/2)A(r). Direct conjugation gives

\[
(\partial_u^2-1)[r^{1/2}A(r)]
 =4r^{5/2}\left(A''+\frac2rA'\right),
\]

so (2) is exactly consistent with Phi=(psi''-psi)/8. It is an operator-level dimensional reduction, not a new equation assumed for the canonical field.

## Theta reflection is Kelvin symmetry in dimension three

Use the complete theta profile

\[
\Theta(r)=\sum_{n\in\mathbb Z}e^{-\pi n^2r^2}=1+2A(r).
\]

The classical modular transformation, with the theta parameter i r^2, gives

\[
\Theta(r)=r^{-1}\Theta(1/r).
\tag{3}
\]

For dimension three the Kelvin transform of a radial profile is Kf(r)=r^(-1)f(1/r). Thus Theta is Kelvin invariant. Its classical Laplacian covariance is

\[
\Delta_3(Kf)(r)=r^{-5}(\Delta_3f)(1/r).
\]

For Q(r)=Delta_3 Theta(r), defined away from the origin, this gives

\[
Q(r)=r^{-5}Q(1/r),\qquad
\boxed{\Phi(u)=\frac14r^{5/2}Q(r).}
\tag{4}
\]

Multiplying the covariance by r^(5/2) makes it invariance under u -> -u, recovering Phi's evenness. The two classical inputs are checked in the [reference annotation][reference]: DLMF 20.7.32 and Axler–Bourdon–Ramey, Proposition 4.6. The combination (1)–(4) is derived here without a novelty claim.

The origin is essential. Theta(r)~1/r at zero and Theta(r)->1 at infinity. Therefore this is a singular radial profile, not a smooth positive harmonic function on all R^3. In distribution notation,

\[
\Delta_{\mathbb R^3}\Theta=Q(|y|)-4\pi\delta_0.
\tag{5}
\]

The difference Theta(r)-1/r is smooth and flat at zero, by (3) and Gaussian decay. This proves the stated contact term using Delta(1/r)=-4 pi delta_0. Also Q>0 for r>=1 by the termwise Gaussian formula, and hence for all r>0 by (4). The flux check is

\[
\int_0^\infty Q(r)r^2dr
 =[r^2\Theta'(r)]_0^\infty=1.
\]

It verifies the 4 pi total mass of the ordinary radial density Q and its compensation by the point source. An argument discarding that source would change the global problem.

## Exact physical observation and heat evolution

Changing variables in the original half-line transform yields

\[
\boxed{H(t,z)=\frac18\int_1^\infty
 e^{(t/4)\log^2r}r^{3/2}Q(r)
 \cos\left(\frac z2\log r\right)dr.}
\tag{6}
\]

Equivalently, using (4),

\[
H(t,z)=\frac1{16}\int_0^\infty
 e^{(t/4)\log^2r}r^{3/2+iz/2}Q(r)dr.
\tag{7}
\]

These converge locally uniformly for finite complex t,z. Gaussian decay at infinity and its Kelvin counterpart at zero pay both endpoints. The physical observation is a weighted Mellin transform of this radial source. It is not its ordinary three-dimensional Fourier transform.

With Q_t(r)=exp[(t/4)log^2 r]Q(r), the exact radial source evolution is

\[
\partial_tQ_t=\tfrac14\log^2r\,Q_t.
\tag{8}
\]

It gives H_t=-H_zz directly through (6) or (7). A putative evolution of a potential satisfying Delta Theta_t=Q_t requires the conjugated operator Delta^(-1)[(log^2 r/4)Delta], together with its harmonic/boundary data. Ordinary radial diffusion cannot be substituted for (8). The Kelvin covariance of Q_t survives because log^2 r is invariant under inversion.

## The first Green calculation returns the known primitive identity

This checks what the most immediate geometric manipulation actually buys. On r>=1 put T(r)=Theta(r)-1 and

\[
k_{t,z}(r)=e^{(t/4)\log^2r}r^{-1/2}
                 \cos\left(\frac z2\log r\right).
\]

Subtracting 1 is required before integration by parts: T decays, while Theta approaches 1. For every finite outer radius R, radial Green gives

\[
\int_1^R k\,\Delta_3T\,r^2dr
 =[r^2(kT'-Tk')]_1^R+\int_1^R T\,\Delta_3k\,r^2dr.
\tag{9}
\]

As R tends to infinity the outer term vanishes. At r=1, modularity gives Theta'(1)=-Theta(1)/2, while k(1)=1 and k'(1)=-1/2. Thus the full lower-boundary contribution is exactly 1/2:

\[
8H=\frac12+\int_1^\infty T(r)\Delta_3 k_{t,z}(r)r^2dr.
\tag{10}
\]

Returning to u, define J(t,z)=integral_0^infinity exp(tu^2)psi(u)cos(zu)du. Evaluation of Delta_3 k gives

\[
8H=\frac12+(2t-z^2-1)J+4tzJ_z-4t^2J_{zz}.
\tag{11}
\]

This is precisely the [existing positive-primitive reconstruction][primitive]. The radial Green reformulation by itself supplies no stronger estimate. It does expose exactly where an improved correlated or boundary estimate would need to enter.

## Earlier tools that can be reused

There are two different three-dimensional constructions; their variables and observation maps must remain distinct.

| Existing capability | Applicability here | Scope to preserve |
| --- | --- | --- |
| [Positive radial inverse marginal][radial] | For m_t(u)=exp(tu^2)Phi_e(u), R_t(rho)=-m_t'(rho)/(2 pi rho) has axis marginal m_t and an exact Fourier/Bessel observation giving H. It is positive on 0<=t<=1/20 in the source note. | Its radius rho is separate from r=exp(2u). Its exact generator contains a Volterra term; its positive radial collision control rules out generic positivity as the desired discriminator. |
| [Sine jets and cutoff payments][sine] | Supplies complete projection/derivative and endpoint accounting if the inverse-marginal version is used. | Its higher-dimension and Gaussian-mixture exclusions concern that inverse-marginal family. They do not exclude the different singular theta profile A(r) in (1). |
| [Signed Hodge and geometric estimates][geometry] | Reuse polarized Green identities, localization weights, and explicit physical-observation payments. | A norm or ambient volume cannot replace the signed Mellin observation. Existing sharp constants have their own measures and domains. |
| [Constrained physical-trace analysis][trace] | Identifies the need for source/PDE restrictions or stronger norms before passing from ambient information to the physical observation. | The generic first-order trace obstruction has a stated class; it does not exclude all theta-specific estimates. |
| [Theta primitive and arithmetic bookkeeping][arithmetic] | Keeps the full normalized lattice, source reconstruction, and boundary contribution available. | Positive auxiliary transforms and modular identities alone have not supplied the missing physical sign. |

Fueter, quaternionic, octonionic, and curved-bundle realizations remain valid dictionaries in the geometric summary. The immediate source operator here is already scalar and radial in three dimensions; no added ambient geometry is needed to establish (2)–(11).

## Control screen and a bounded analytical next question

Kelvin covariance alone is still a reformulation of reflection. For any even source m(u), the profile

\[
Q_m(r)=4r^{-5/2}m(\tfrac12\log r)
\]

obeys Q_m(r)=r^(-5)Q_m(1/r). Positive even colliding controls therefore share positivity and this covariance. Those properties cannot alone imply absence of a joint zero. The integer-square Gaussian expansion of Theta is the additional canonical information that a successful estimate would have to use quantitatively. Different established controls fail different full-source premises, as recorded in [the control register][controls]; no common preservation list is asserted.

The suggested next bounded task is to test one weighted, signed Green or observation estimate for this **specific** theta profile on inversion-paired annuli, with the actual physical kernel from (6), both jets, and every boundary/cutoff contribution. Compare its complete allowance or lower margin with the existing one-dimensional estimate on the same symbolic time-height domain. A useful return would be a sharper physical estimate or a precise failed-estimate comparison. Reproducing (11), a positive bulk norm, or a formal higher-dimensional realization is not that return.

This is a reasonable source-level analytical option after the energy pause. It preserves the earlier tools and their controls, while keeping the arithmetic estimate as the decisive test. No larger program, new task dispatch, or exclusion claim is established by this note.

[n19]: 19_AUXILIARY_SOURCE_SCALE_DERIVATIVE_IDENTITY_20261027.md
[reference]: ../references/03_RADIAL_LAPLACIAN_AND_KELVIN_REFERENCES_20261027.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[arithmetic]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../avoid/README.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[primitive]: ../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md
[radial]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/notes/1_POSITIVE_THREE_DIMENSIONAL_THETA_LIFT_AND_NONLOCAL_GENERATOR_20261010.md
[sine]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/notes/2_SINE_COLLISION_JETS_AND_HIGH_DIMENSION_THETA_OBSTRUCTIONS_20261010.md
[trace]: ../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/notes/02_ZERO_FORM_GREEN_IDENTITY_AND_PHYSICAL_TRACE_OBSTRUCTION_20261018.md

## Subsequent scope clarification

Edward Baker requested examining changes to the collision argument itself as well as sharper signed estimates. [Note21](21_COLLISION_MECHANISMS_IN_THE_RADIAL_REPRESENTATION_20261027.md) broadens the recommendation accordingly: it derives the immediate Sturm operator, identifies why H is a spectral coefficient rather than its characteristic function, and separates possible Wronskian or global continuation mechanisms from the unchanged local energy argument. No new exclusion is claimed.
