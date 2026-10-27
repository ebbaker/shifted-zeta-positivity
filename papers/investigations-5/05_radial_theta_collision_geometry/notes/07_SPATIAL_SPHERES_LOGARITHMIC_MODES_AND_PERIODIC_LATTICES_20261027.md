# Spatial spheres, logarithmic radial modes and periodic lattices

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Research conversation: **Review radial theta collision work**, Investigation05 chat0002, thread 01a17ee9-ed08-7271-9f66-04ac5ee516b8.

Edward Baker proposed using a genuine spatial radius for a three-dimensional lattice realization, and then asked whether the cosine in H could be absorbed into spherical geometry. This note separates the two radii, recovers an existing exact spherical representation of H, and tests fixed periodic lattice fields at an actual Euclidean radius.

**Status: exact representation identities and a scoped periodic-field obstruction, with same-assistant analytical checking.** The inverse radial marginal in Section 2 is inherited from the [10 October radial-Bessel note][prior], not a new lift. The logarithmic radial modes in Section 3 preserve the original radius. Neither representation establishes a lattice origin or excludes a collision. The periodic-field result applies to exact spherical averaging of a fixed translation-periodic field; it is not a prohibition on every construction involving lattice data.

The [result index](../../../../result-summaries/README.md), [geometric results](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md), [theta and arithmetic results](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and [avoid index](../../../../avoid/README.md) apply, especially [coordinate lifts](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [target restatements](../../../../avoid/01_restating_the_target.md) and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md). This is a representation/feasibility calculation, not a proposed RH-equivalent criterion.

## 1. The three observations and the two radii

Keep the unchanged source and normalizations

\[
A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\quad
\Theta(r)=1+2A(r),\quad Q(r)=\Theta''(r)+2\Theta'(r)/r,
\]
\[
r=e^{2u},\qquad
\Phi(u)=\tfrac14r^{5/2}Q(r),\qquad
m_t(u)=e^{tu^2}\Phi(u),\qquad
H(t,z)=\int_0^\infty m_t(u)\cos(zu)\,du.
\tag{1}
\]

Here Phi is the complete even source. All formulas below retain its full tails.

In [Note06][lattice], integrating the torus coordinates x_2,x_3 at fixed heat time s is a transverse marginal; then s=r^2 is substituted. Those integrals are not spatial spherical averages.

For a spatial field F on R^3, its spherical mean is instead

\[
\mathcal RF(r)=\frac1{4\pi}\int_{S^2}F(r\omega)\,d\omega
=\frac1{4\pi}\int_0^{2\pi}\int_0^\pi
F(r\sin\vartheta\cos\varphi,r\sin\vartheta\sin\varphi,
r\cos\vartheta)\sin\vartheta\,d\vartheta\,d\varphi.
\tag{2}
\]

The factor sin(vartheta) is the angular measure. In Sections 4–5, r in (2) is actual spatial distance, and any smoothing time is fixed independently.

A second possible geometry uses an auxiliary Euclidean radius rho=|u|. It is different from r=e^(2u): u=0 corresponds to the original sphere r=1, not the original origin. The two signs of u correspond to inversion-related original radii. Section 2 uses rho; Section 3 retains r.

## 2. The cosine does have an exact spherical representation

The normalized average of a plane wave over the sphere is

\[
\frac1{4\pi}\int_{S^2}e^{iz\rho\omega_1}\,d\omega
=\frac12\int_{-1}^{1}e^{iz\rho v}\,dv
=j_0(z\rho)=\frac{\sin(z\rho)}{z\rho}.
\tag{3}
\]

The limiting value at zero is one. This holds also for complex z by entire continuation. It is the n=0 case of [DLMF 10.54.1–2](https://dlmf.nist.gov/10.54), with [10.49.3](https://dlmf.nist.gov/10.49.E3). In particular the uniform angular measure gives sinc, and

\[
\cos(z\rho)=\partial_\rho\{\rho j_0(z\rho)\}.
\tag{4}
\]

Integration by parts therefore gives

\[
H(t,z)=-\int_0^\infty \rho m_t'(\rho)j_0(z\rho)\,d\rho
=2\pi\int_0^\infty \rho^2 R_t(\rho)j_0(z\rho)\,d\rho,
\]
\[
R_t(\rho)=-\frac{m_t'(\rho)}{2\pi\rho},\qquad
R_t(0)=-\frac{m_t''(0)}{2\pi}.
\tag{5}
\]

The boundary term vanishes at zero because it contains rho, and at infinity by the complete double-exponential source decay. Evenness makes R_t smooth at the center. The same decay justifies every displayed integral and differentiation on compact sets of finite t,z.

Equivalently,

\[
\boxed{H(t,z)=\frac12\int_{\mathbb R^3}
R_t(|v|)e^{izv_1}\,dv.}
\tag{6}
\]

Thus z is the frequency of an ordinary three-dimensional plane wave, and angular integration is exactly spherical. The density changes from m_t to its inverse radial marginal R_t. Merely replacing cos by sinc while keeping m_t would change H.

This construction and its positivity proof already occur in the [earlier note][prior], with an [internal review][prior-review]. Its axis marginal is

\[
\int_{\mathbb R^2}R_t(\sqrt{u^2+|v_\perp|^2})\,dv_\perp
=2\pi\int_{|u|}^\infty R_t(\rho)\rho\,d\rho=m_t(u).
\tag{7}
\]

The inherited proven positivity interval is 0<=t<=1/20; this note does not enlarge it. Positivity is equivalent to -Phi'(rho)/Phi(rho)>2t rho for rho>0, together with the center condition. The exact representation itself holds for all finite real t, without asserting R_t is then positive. The [replay receipt][replay] records a successful rerun of the unchanged earlier checker and an identical parsed output. Exact rational bounds and exploratory floating-point samples retain their separate statuses.

The genuine evolution is also inherited:

\[
\partial_tR_t(\rho)=\rho^2R_t(\rho)
-2\int_\rho^\infty R_t(s)s\,ds.
\tag{8}
\]

Indeed differentiating (5) gives rho^2 R_t-m_t/pi and (7) gives the integral term. Ordinary three-dimensional diffusion is not this evolution. The integral term cannot be dropped.

## 3. Retaining the original radius: z as a logarithmic radial frequency

There is an exact alternative that keeps r as the spatial distance in the original radial Poisson construction. Define

\[
Q_t(r)=e^{t\log^2r/4}Q(r),\qquad
\Psi_z(r)=r^{-1/2}\cos\!\left(\frac z2\log r\right).
\tag{9}
\]

The full-radius Mellin identity in [Note01][initial] gives

\[
\boxed{H(t,z)=\frac1{64\pi}
\int_{\mathbb R^3}Q_t(|x|)\Psi_z(|x|)\,dx.}
\tag{10}
\]

To check the constant, spherical volume contributes 4 pi r^2 dr. Then dr=2r du and r^(5/2)Q_t=4m_t give 32 pi times the full-line integral of m_t(u)cos(zu), which is 64 pi H. Near both radial endpoints the source dominates every fixed complex-z power, so no endpoint regularization is being suppressed.

These are actual radial differential modes. If h(u) is any twice differentiable function and u=log(r)/2, direct differentiation gives

\[
\Delta_3\{r^{-1/2}h(u)\}
=\frac14r^{-5/2}(h''(u)-h(u)).
\tag{11}
\]

Consequently

\[
-\Delta_3\Psi_z=\frac{1+z^2}{4r^2}\Psi_z,\qquad
\mathscr L\Psi_z=z^2\Psi_z,\quad
\mathscr L=-4r^2\Delta_3-1.
\tag{12}
\]

The operator is adapted to changes of scale. Its oscillations are equally spaced in log(r), rather than in r. In the radial space with measure r^(-2)dx, the substitution f(r)=r^(-1/2)h(log(r)/2) gives norm 8 pi times the L^2(du) norm, and conjugates the radial operator exactly to -d^2/du^2. This specifies the natural measure and the self-adjoint realization obtained from the usual full-line operator. Real-z modes are generalized modes, not square-integrable eigenvectors.

Formula (10) therefore absorbs z into the original radial geometry as a spectral observation of Q_t. The angular variables integrate out because both functions are radial; the cosine is supplied by the logarithmic radial mode, not by the angular Jacobian alone.

This does not turn an H-zero into an eigenvalue of a new discrete operator. The modes exist for every real z; an H-zero means that the source pairing with one of them vanishes. No lattice, new boundary condition, or collision-excluding spectral theorem has been constructed.

## 4. Exact spherical averaging of a fixed periodic lattice field

For the cubic lattice, a natural spatial field is the periodized Gaussian

\[
K_s(x)=s^{-3/2}\sum_{n\in\mathbb Z^3}e^{-\pi|x-n|^2/s}
=\sum_{k\in\mathbb Z^3}e^{-\pi s|k|^2}e^{2\pi i k\cdot x},
\qquad s>0.
\tag{13}
\]

Here s is fixed. Applying (3) gives the true spatial spherical mean

\[
\mathcal RK_s(r)=
1+\sum_{k\ne0}e^{-\pi s|k|^2}
\frac{\sin(2\pi|k|r)}{2\pi|k|r}.
\tag{14}
\]

Absolute convergence justifies termwise averaging. This mean is finite at r=0 and approaches one at infinity, with the nonconstant part O(1/r). A has a 1/(2r) singularity at zero and decays like exp(-pi r^2) at infinity. Subtracting the constant in (14) does not solve the exact matching problem.

The stronger statement is useful because it allows arbitrary signed periodic coefficients and singular periodic fields.

**Proposition.** Let F be a tempered distribution periodic under a fixed full-rank lattice in R^3. If its rotation average is represented by a function T in L^1(R^3), then T=0.

**Proof.** Use the Fourier convention exp(-2 pi i x dot xi), and let Lambda* be the reciprocal lattice. Periodicity gives

\[
\widehat F=\sum_{k\in\Lambda^*}c_k\delta_k
\tag{15}
\]

in tempered distributions, with at most polynomially growing coefficients. The standard periodic-distribution Fourier series is recorded in [Ivrii, Section 11.2](https://www.math.utoronto.ca/courses/apm346h1/20169/PDE-textbook/Chapter11/S11.2.html), equations 11.2.9–12, after changing his angular-frequency convention to ours.

Fourier transformation commutes with averaging over rotations. Rotation averaging each delta_k gives normalized surface measure on the frequency sphere |xi|=|k| (delta_0 when k=0). Consequently the transform of the average is supported on

\[
E=\bigcup_{k\in\Lambda^*}\{\xi:|\xi|=|k|\}.
\tag{16}
\]

This union is locally finite, closed, and has empty interior. On the other hand, the Fourier transform of an L^1 function is continuous: this follows directly by dominated convergence in its Fourier integral. A continuous function supported on E must vanish because the complement is dense. Injectivity of Fourier transformation proves T=0. The interchange with rotations is valid distributionally: polynomial coefficient growth and Schwartz decay give summable test-function bounds. This proves the proposition.

The proposition does not say F itself vanishes; its angular components can cancel in the mean. Translation of the averaging center only changes the coefficients in (15), leaving the conclusion unchanged.

It applies to both targets here:

\[
\int_{\mathbb R^3}A(|x|)\,dx
=\sum_{n\ge1}n^{-3}=\zeta(3)<\infty,\qquad
\int_{\mathbb R^3}Q(|x|)\,dx=4\pi.
\tag{17}
\]

Both are nonzero and nonnegative. The first identity follows by Tonelli and the three-dimensional Gaussian integral; the second is the exact flux normalization of Note01. Thus neither is the exact global spherical mean of a fixed periodic field. Matching Theta would imply that the periodic field minus one has spherical mean 2A, which is equally excluded.

For A the frequency mismatch is particularly explicit:

\[
\widehat{A(|\cdot|)}(\xi)
=\sum_{n\ge1}n^{-3}e^{-\pi|\xi|^2/n^2}.
\tag{18}
\]

This is a continuous strictly positive density everywhere, whereas (16) contains only discrete radii. The interchange in (18) is justified by the summable L^1 norms n^(-3).

The assumptions matter. Nonperiodic site weights, localized lattice defects, continuous mixtures of lattice scales, radius-dependent kernels, and approximation on a bounded annulus are not excluded. A parameter-dependent observation involving z is also a different construction unless it still claims an exact periodic spatial parent for A or Q.

## 5. Coulomb fields give a direct spatial diagnosis

An unneutralized infinite sum of lattice Coulomb potentials is divergent. The standard periodic alternative, with cell volume V, solves

\[
-\Delta G=4\pi\left(\sum_{v\in\Lambda}\delta_v-\frac1V\right).
\tag{19}
\]

The uniform compensating term is required by integration over a periodic cell. Put g(r)=R G(r), averaging about a lattice point, and let N(r) count lattice points strictly inside the radius. Away from lattice shell radii, the divergence theorem gives

\[
g'(r)=-\frac{N(r)}{r^2}+\frac{4\pi r}{3V}.
\tag{20}
\]

Before the first nonzero lattice distance, N=1, so

\[
g(r)=\frac1r+C+\frac{2\pi r^2}{3V}.
\tag{21}
\]

Theta instead satisfies Theta(r)=1/r+(2/r)A(1/r): the remainder is flat at zero, with no quadratic term. At a shell of radius a and multiplicity M, g' has jump -M/a^2, whereas Theta is analytic for every r>0. These are explicit local mismatches, in addition to the general proposition. Smoothed periodic charges fall under Section 4.

There is nevertheless an exact useful radial interpretation of the original profile. Set V_theta=2A=Theta-1. Then

\[
\boxed{-\Delta V_\theta=4\pi\delta_0-Q(|x|),\qquad
Q>0,\quad \int_{\mathbb R^3}Q\,dx=4\pi.}
\tag{22}
\]

Thus V_theta is the potential of a unit point charge screened by a continuous radial cloud of opposite charge density -Q/(4 pi). In this interpretation A is a potential profile and Q is the smooth screening density. Spherical integration of the Poisson equation, or Newton's shell formula, gives

\[
2A(r)=\frac1r-\left\{\frac1r\int_0^r s^2Q(s)\,ds
+\int_r^\infty sQ(s)\,ds\right\}
=\int_r^\infty\left(\frac{s^2}{r}-s\right)Q(s)\,ds.
\tag{23}
\]

This is the t=0 potential formula already present in Note01. It supports a natural radial interpretation, but deriving this particular cloud from an independently specified discrete system remains an open construction problem. Defining the cloud from A alone does not supply that origin.

## 6. What this changes, and what it does not

The user's cosine observation identifies an exact spherical Fourier representation already developed elsewhere in the repository. The new comparison makes its radius explicit and gives a direct original-radius spectral formulation, (9)–(12). It also closes the exact fixed-periodic-field spherical-average attempt for A and Q in the class of Section 4.

These are source representations, not collision criteria. The [control register](../../../../result-summaries/12_collision_controls_and_screening.md) continues to apply. More specifically, the earlier radial note constructs a smooth nonnegative radial density from the convolution of two uniform sphere measures and a radial positive bump. Its axis transform is sinc(z)^2 times the bump transform and has a double zero at z=pi. Its time-dependent inverse marginals stay nonnegative up to a prescribed positive time. This explicitly defeats an inference from spherical geometry and positive density alone. It lacks the unchanged full theta source.

The Euler-factor controls change the canonical source and conductor; weighted-square controls change its full coefficients/reflection; reflected smooth and positive-primitive controls lack the canonical square arithmetic. None is excluded by the generic cosine/sinc identity. The Gaussian-polynomial control in Note01 retains the forced boundary cancellation. The existing event certificates are not rerun or promoted to new scopes here.

For a further lattice attempt, the missing input is a concrete nonperiodic or scale-dependent lattice law whose derived density is the unchanged canonical profile. Its surviving geometry would then need to yield an independently proved estimate for the source pairing or physical jets. The present exact identities provide no such estimate.

RTC-03 has another bounded representation/feasibility return; its broader mechanism task remains open. RTC-04 still has no characteristic realization, and no status change is made to RTC-05, RTC-06 or RTC-07. No manuscript milestone or investigation closeout is claimed.

## 7. Evidence and limits

Equations (2)–(7), (10)–(12), (14), (17)–(18), and (20)–(23) are justified by the displayed elementary integrations, differentiations, full-source decay and distributional flux terms. The periodic-field proposition has a written Fourier-support proof. All checking is same-assistant; no independent mathematical review is claimed.

The selected external formulas and normalization changes are recorded in [reference annotation04][references]. The prior radial checker was replayed without modification and its parsed JSON matches the inherited record, as recorded in [the receipt][replay]. That replay concerns the earlier positivity proof on 0<=t<=1/20; it is not a numerical proof of the new periodic-field proposition. No new lattice fitting experiment or physical theta collision sampling was performed.

[prior]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/notes/1_POSITIVE_THREE_DIMENSIONAL_THETA_LIFT_AND_NONLOCAL_GENERATOR_20261010.md
[prior-review]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md
[initial]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[lattice]: 06_RANK_THREE_LATTICE_REALIZATION_AND_PROJECTION_20261027.md
[references]: ../references/04_SPHERICAL_AVERAGES_AND_PERIODIC_DISTRIBUTIONS_20261027.md
[replay]: ../numerics/07_INHERITED_RADIAL_CHECK_REPLAY_20261027.json

27 October 2026 follow-up: Edward Baker clarified that the intended task was to change the underlying lattice sum itself. [Note08](08_GENUINE_THREE_DIMENSIONAL_LATTICE_SUMS_AND_THETA_RECOVERY_20261027.md) supplies two such rank-three definitions and exact target recovery. The fixed-periodic-spatial-field obstruction above remains valid in its stated class, but does not settle that broader request or apply to Note08’s varying-heat-parameter spherical observation.
