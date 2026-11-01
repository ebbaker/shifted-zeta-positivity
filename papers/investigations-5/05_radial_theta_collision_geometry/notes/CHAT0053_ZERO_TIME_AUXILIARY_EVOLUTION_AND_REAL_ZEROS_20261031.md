# Zero time auxiliary evolution and real zeros

31 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, effort **xhigh**, Investigation05 chat0053.

**Status:** explanatory synthesis, elementary transport derivation, and a classical strip-contraction comparison. No new theta noncollision theorem or alternate Newman threshold is established. The author asks whether an auxiliary evolution at physical time zero can make all spectral zeros real, and specifically asks to include pure divergence transport without energy normalization.

Read with the [result index](../../../../result-summaries/README.md), especially [theta identities](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), particularly [reformulations](../../../../avoid/01_restating_the_target.md), [coordinate changes](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The observations below do not use a physical mass lower bound. They distinguish an invariant representation from a deformation of the spectral function itself.

## The existing conservative observation

At a fixed feedback mark, use its one common propagator for the running spectral argument z. On its regular lifespan,
\[
\partial_sj_s=\Delta_Xj_s+\alpha(s)\operatorname{div}_X(vj_s),
\qquad \mathcal H_s(z)=\int j_s(0,z;X)\,dX=H(0,z).
\]
Mass conservation holds for the complete z-dependent density. Entire dependence follows from the source's compact-spectral domination and the common propagator. Every zero and multiplicity is fixed. Reversing an admissible evolution cannot change this identity. Selecting a different feedback separately at each real frequency is not, by itself, a holomorphic evolution in complex z.

The same conclusion holds for pure divergence transport,
\[
\partial_sj=\operatorname{div}(vj),
\]
and for diffusion plus a prescribed drift coefficient. No energy constraint is needed to conserve the complete observation. This follows directly by integrating the divergence; see the [manuscript](../radial_deformations_and_zero_dynamics.tex), conservative observation and feedback sections.

## Pure divergence transport is explicit

Take the manuscript's fixed vector field
\[
v(X)=X+X/(1+|X|^2).
\]
The transport velocity is -v. Let X_s=Psi_s(X_0), with radius r_s. Then
\[
\dot r_s=-r_s(r_s^2+2)/(r_s^2+1).
\]
For y=r_s^2, y'=-2y(y+2)/(y+1), so
\[
\frac{d}{ds}\{y(y+2)\}=-4y(y+2).
\]
Thus the exact characteristic is
\[
r_s(r_0)^2=\sqrt{1+e^{-4s}r_0^2(r_0^2+2)}-1.
\]
The globally Lipschitz velocity has a flow for every finite positive or negative s. The density is its pushforward:
\[
j_s(\Psi_s(X_0))\det D\Psi_s(X_0)=j_0(X_0).
\]
This immediately proves conservation of the spectral observation when the cosine is included in j_0. Without diffusion, signed components are transported, not mixed by convolution.

For smooth decaying data, spatial energy instead obeys
\[
E'=\int d(X)|j|^2,\qquad 3\le d=\operatorname{div}v\le6.
\]
Hence E(0)e^{3s}<=E(s)<=E(0)e^{6s} for s>=0. This growth occurs regardless of cancellation of signed mass and is not the normalized flow's finite collision deadline. The same statements hold for a prescribed integrable time coefficient after replacing s by its accumulated transport time.

## Transporting the source gives a different spectral family

A genuine alternative is to transport a z-independent source, then apply a fixed spectral kernel. Start with the exact raw exterior source
\[
\rho_0(X)=\mathbf1_{r\ge1}\frac{\Phi(\log r/2)}{8\pi r^3}.
\]
No unit Gaussian preparation is inserted: preparing this amplitude and then multiplying by cosine would already change the initial transform. The raw jump is admissible for the transport pushforward.

Define
\[
\rho_s=(\Psi_s)_\#\rho_0,\qquad
F_s(z)=\int\rho_s(X)\cos(z\log|X|/2)\,dX.
\]
Then F_0(z)=H(0,z), but F_s generally differs from H(0,z). Put
\[
\chi_s(u)=\tfrac12\log r_s(e^{2u}).
\]
The complete formula is
\[
F_s(z)=\int_0^\infty\Phi(u)\cos(z\chi_s(u))\,du.
\]
Here
\[
\partial_s\chi_s=-b(\chi_s),\qquad
b(x)=\tfrac12\left(1+\frac1{1+e^{4x}}\right).
\]
Because 1/2<b<1, |chi_s(u)-u|<=|s|. The complete theta tail therefore makes F_s an even real entire function of z at each finite s, including negative s, and justifies compact-parameter differentiation. There is no origin singularity at finite time: the initial support r>=1 maps to r>=r_s(1)>0.

Its exact spectral response is
\[
\partial_sF_s(z)=z\int_0^\infty\Phi(u)b(\chi_s(u))
 \sin(z\chi_s(u))\,du.
\]
This expression does not close as the Newman equation -F_zz. It identifies the actual candidate requiring analysis, rather than importing zero reality from mass conservation or from a positive transported density. No strip contraction, eventual all-real theorem, or one-sided threshold property for this F_s has been established here. Changing the observation invalidates the earlier normalized-feedback collision theorem; it cannot be carried over without proof.

The two constructions are different:
\[
\int P_s(\rho_0 k_z)=\int\rho_0k_z,\qquad
\int(P_s\rho_0)k_z=\int\rho_0P_s^*k_z.
\]
The second permits spectral zero motion because the kernel is applied after source transport.

## Existing Gaussian comparisons

The [companion book](../book/main.tex), section on deformations of the generating field, already proves that cylinder heat gives
\[
\mathscr H_s(z)=e^{-sz^2}H(0,z).
\]
It preserves all zeros through a nonvanishing factor. Its explicitly solved combination with the transported Newman generator merely rescales and reparametrizes the original Newman zero trajectories.

[Note04](04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md) supplies a second useful comparison. At physical time zero its Gaussian relaxation has
\[
F_\rho(0,z)=e^{-(1-\rho^2)z^2/4}H(0,\rho z),
\qquad 0<\rho\le1.
\]
Every original zero z_0 is at z_0/rho. At rho=0 the limiting function is a nonzero Gaussian, but hypothetical nonreal zeros have escaped to infinity; they did not become real at a finite transport time. This is a scoped warning about this Gaussian family, not an exclusion of nonlinear source transport.

## A classical family with finite strip contraction

A known comparison is
\[
C_a(z)=\tfrac12\{H(0,z+ia)+H(0,z-ia)\}
=\int_0^\infty\Phi(u)\cosh(au)\cos(zu)\,du.
\]
It satisfies
\[
\partial_a^2C_a=-\partial_z^2C_a,\qquad
C_0=H(0,z),\qquad \partial_aC_a|_{a=0}=0.
\]
The strip bound is classical: if the initial zeros lie in |Im z|<=Delta and the function is a locally uniform limit of real polynomials with zeros in that strip, the shifted average has zeros in |Im z|<=sqrt(max(Delta^2-a^2,0)). The [checked reference](../references/19_STRIP_CONTRACTION_AND_AUXILIARY_FLOW_SCOPE_20261031.md) identifies de Bruijn's polynomial theorem in Branden--Chasse Theorem1.6. Finite shifts commute with local uniform limits, and Hurwitz transfers the zero-free exterior unless the limit vanishes identically.

For H(0,z), evenness, real symmetry, order one, and the classical critical strip give the required approximation: group its canonical product in plus/minus pairs and conjugate groups. Each partial product is a real polynomial with all its zeros in the same strip and converges locally uniformly. The source integral gives C_a(0)>0, excluding the zero limit. In this manuscript's xi((1+iz)/2)/8 normalization, Delta=1 is available without RH. Therefore C_a has only real zeros for a>=1. This is an application of a classical theorem, not a new strip estimate.

The polynomial f(z)=z^2+delta^2 illustrates the mechanism exactly:
\[
\tfrac12[f(z+ia)+f(z-ia)]=z^2+delta^2-a^2.
\]
Its imaginary zeros become real at a=delta, although the initial polynomial was not real-rooted. The example also shows why an all-real endpoint alone cannot prove reality at parameter zero.

This family is distinct from the conservative s-flow and is not an autonomous first-order semigroup in a: cos(aD)cos(bD) is not cos((a+b)D). The strip bound proves eventual reality; it does not by itself establish that the entire parameter set with all-real zeros is a half-line. No new Newman constant or backward transfer is claimed.

The potential research change is thus precise: choose a common evolution of the source whose induced entire function actually changes, then prove zero-location control for that induced function. The pure radial transport above is a concrete candidate, with an explicit source map; its required zero-location theorem remains open.


## Subsequent assessment of the source transport

31 October2026, chat0053, gpt-6-astra / xhigh, prepared for Edward Baker with substantial LLM assistance. The [next note](CHAT0053_SOURCE_TRANSPORT_UNBOUNDED_STRIP_OBSTRUCTION_20261031.md) supersedes the open-status statements above for this exact raw exterior source transport: **proved in-note, same-assistant self-check**, every nonzero finite positive or negative time gives zeros outside every bounded horizontal strip. Merely recentering the observation also fails. The earlier derivation and classical imaginary-shift comparison remain intact. [Self-assessment](../reviews/CHAT0053_SOURCE_TRANSPORT_OBSTRUCTION_SELF_ASSESSMENT_20261031.md); no independent or specialist review.
