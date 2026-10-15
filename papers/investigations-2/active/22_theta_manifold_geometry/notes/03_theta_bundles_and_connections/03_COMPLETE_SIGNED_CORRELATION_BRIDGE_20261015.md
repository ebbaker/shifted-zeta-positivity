# Complete signed two-source identities with all primitive endpoints

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model: **gpt-6-astra**; reasoning effort: **ultra**. This continues the [covariant theta-source construction](01_COVARIANT_SOURCE_AND_ASD_CONNECTION_20261015.md) with exact transform identities. It establishes no signed estimate or collision-exclusion result.

## 1. Exact signed kernels

Write `W_t(u)=exp(tu²)Phi(u)` and `c_j(u)=u^j cos(xu+j*pi/2)`. All integrals below are over `[0,infinity)` unless otherwise stated. The complete source, with every positive integer theta index retained, gives

\[
h_j=\int W_t(u)c_j(u)\,du.
\]

Symmetrizing the two products defining the Laguerre quantity gives

\[
\mathcal L_j=\iint W_t(u)W_t(v)K_j(x;u,v)\,du\,dv,
\]
\[
\boxed{K_j=\frac{(uv)^j}{4}\bigl((u+v)^2\cos(x(u-v))+(-1)^j(u-v)^2\cos(x(u+v))\bigr),\quad j=0,1.}
\]

Indeed `K_j=c_{j+1}(u)c_{j+1}(v)−(c_j(u)c_{j+2}(v)+c_{j+2}(u)c_j(v))/2`. The physical energy uses the distinct kernel

\[
E=\iint W_t(u)W_t(v)M(x;u,v)\,du\,dv,
\quad M=\frac12\bigl((1+uv)\cos(x(u-v))+(1-uv)\cos(x(u+v))\bigr).
\]

Neither formula introduces an auxiliary energy. In particular, both stationary branches still use `E=H²+H_x²`.

For `q=e^{4u}`, put `J_k(u)=(D^k theta)(0,iq)` and

\[
B(u)=q^2J_4(u)-3\pi^2J_0(u).
\]

The covariant source formula gives the explicit complete insertion

\[
\boxed{\mathcal L_j=\frac1{256\pi^4}\iint
 e^{t(u^2+v^2)+u+v}B(u)B(v)K_j(x;u,v)\,du\,dv.}
\]

Replacing `K_j` by `M` gives `E` with the same normalization. This is a product of section coefficients in the stated marked frame; it is not a Hermitian squared-norm identity. All spectral phases and both heat factors remain present.

For comparison, extend `W_t` evenly to the real line. The change `u=p+q, v=p−q` in the full Fourier product yields

\[
\mathcal L_j=\int_{\mathbb R}\cos(2xp)C_j(t,p)\,dp,
\]
\[
C_j(t,p)=e^{2tp^2}\int_{\mathbb R}q^2(q^2-p^2)^j e^{2tq^2}\Phi(p+q)\Phi(p-q)\,dq,\quad j=0,1.
\]

Here `Phi` denotes its even extension. `C_0` is nonnegative, but its cosine transform need not be nonnegative. `C_1` already has a signed weight. This reformulation alone is not a positivity argument.

## 2. A convergent primitive and exact lower endpoints

Use the existing theta primitive

\[
\psi(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}},\qquad
8\Phi=(\partial_u^2-1)\psi,\qquad \psi'(0)=-\frac12.
\]

The primitive and its fixed derivatives have double exponential decay. Thus all upper endpoints vanish after multiplication by the heat factor, a fixed polynomial, and the spectral phase, locally uniformly in complex `(t,x)`.

For a test function `f` of that form, the full integration-by-parts identity is

\[
\int (\psi''-\psi)f
 =\frac12 f(0)+\psi(0)f'(0)+\int\psi(f''-f).
\]

Put

\[
R_j(u)=(\partial_u^2-1)\bigl(e^{tu^2}c_j(u)\bigr),\qquad
I_j=\int\psi R_j.
\]

Every `e^{tu²}c_j(u)` is even in `u`, including odd `j`, since the factor `u^j` accompanies the corresponding sine. Its first derivative at zero vanishes. Its value at zero is one only for `j=0`. Therefore

\[
\boxed{8h_j=\frac12\delta_{j0}+I_j\quad(j\ge0).}
\]

This yields the complete signed formulas

\[
\boxed{64\mathcal L_0=I_1^2-I_0I_2-\tfrac12 I_2,\qquad
64\mathcal L_1=I_2^2-I_1I_3,}
\]
\[
\boxed{64E=\tfrac14+I_0+I_0^2+I_1^2.}
\]

The branch-0 edge term `−I_2/2` and the energy corner `1/4` cannot be dropped. Their scale is exactly the scale of the signed physical reconstruction. Branch 1 has no primitive edge term. This does not justify replacing physical `E=H²+H_x²` by the branch-1 jet norm `h_1²+h_2²` away from stationarity.

A differential form of the same statement uses

\[
Q_j=e^{t(u^2+v^2)}K_j,\qquad L_u=\partial_u^2-1,\quad L_v=\partial_v^2-1.
\]

Both `Q_j` are even separately in `u,v`; all lower-edge first derivatives vanish, `Q_j(0,0)=0`, and

\[
Q_0(0,v)=\tfrac12v^2e^{tv^2}\cos(xv),\qquad Q_1(0,v)=0.
\]

Applying the preceding one-variable identity in each variable gives

\[
\boxed{64\mathcal L_0=
\iint\psi(u)\psi(v)L_uL_vQ_0\,du\,dv
+\frac12\int\psi(v)L_v\bigl[v^2e^{tv^2}\cos(xv)\bigr]\,dv,}
\]
\[
\boxed{64\mathcal L_1=
\iint\psi(u)\psi(v)L_uL_vQ_1\,du\,dv.}
\]

The edge term agrees with `−I_2/2` because `c_2(v)=−v²cos(xv)`. The energy kernel has `M(0,0)=1` and `M(0,v)=cos(xv)`; its two lower edges combine to `I_0`, while its corner is `1/4`. These identities enumerate all four edges and the corner; none are tacitly discarded.

The heat multiplier remains in every `R_j`. Explicitly, with `theta_j=xu+j*pi/2`,

\[
R_j=e^{tu^2}\left[
\left(j(j-1)u^{j-2}+(2t(2j+1)+4t^2u^2-x^2-1)u^j\right)\cos\theta_j
+\left(2jx u^{j-1}+4txu^{j+1}\right)\cos(\theta_j+\pi/2)
\right],
\]

where terms with zero prefactor are omitted, so the formula is polynomial and regular at `u=0` for `j=0,1`.

## 3. Base connection and vertical commutators

The original Chern connection has zero pullback to `gamma(u)=(tau=ie^{4u},z=0)`. For the manuscript's ASD correction `b=2*pi*q³/3`, the pullback is

\[
\gamma^*\widehat A=a(u)du,\qquad a(u)=4\pi e^{12u},\qquad a'(u)=48\pi e^{12u}.
\]

Consequently physical coefficient differentiation is

\[
\partial_u=\widehat\nabla_u-a(u).
\]

For example, the primitive operator must be written as

\[
\partial_u^2-1=
\widehat\nabla_u^2-2a\widehat\nabla_u+(a^2-a'-1).
\]

Keeping only `nabla²` would change the physical source. The large positive-looking `a²` term is accompanied by the connection and derivative terms; it is not an independent favorable contribution.

On the product of the two physical paths, the external tensor-product connection is `a(u)du+a(v)dv`; its curvature vanishes. Its potential is `pi(e^{12u}+e^{12v})/3`. Thus a new signed tangential curvature term does not arise solely by putting this two-source coefficient product into the ASD connection. Ambient curvature remains present in mixed directions and in commutators involving vertical jets.

Those commutators must be evaluated before restricting to `z=0`. Let `V=4q partial_q` at fixed `p,z`, and let `s=Im(z)/q`. This `V` is a chart-local field near the zero section, not a globally specified horizontal field on the lattice quotient. For both the original connection and this base-rescaled connection,

\[
[\nabla_V,D]=-4\pi i s,\qquad
\partial_z(-4\pi i s)=-2\pi/q.
\]

Since higher `z` derivatives of the multiplication coefficient vanish,

\[
[\nabla_V,D^k]
 =-4k\pi i s D^{k-1}-\frac{k(k-1)\pi}{q}D^{k-2}.
\]

In particular

\[
\boxed{[\nabla_V,D^k]\big|_{z=0}
 =-\frac{k(k-1)\pi}{q}D^{k-2}\big|_{z=0}.}
\]

The first commutator vanishes on the zero section, but the higher-jet commutators do not. Restricting before differentiating would lose precisely these terms.

A convenient independent way to retain them is the covariant-jet generating function, at fixed `q`:

\[
\sum_{k\ge0}J_k(u)\frac{w^k}{k!}
 =\exp\left(\frac{\pi w^2}{2q}\right)\vartheta(w,iq).
\]

The theta heat equation and `q'=4q` give the exact coefficient recurrence

\[
\boxed{J_k'=\frac q\pi J_{k+2}-(2k+1)J_k
 -\frac{k(k-1)\pi}{q}J_{k-2}.}
\]

Terms with zero prefactor are omitted. The base scalar `a` cancels when covariant differentiation is converted back to coefficient differentiation. Applying the recurrence to the complete source yields the useful differentiated formulas

\[
\boxed{\Phi'=\frac{e^u}{16\pi^3}
 (q^3J_6-15\pi^2qJ_2),}
\]
\[
\boxed{\Phi''=\frac{e^u}{16\pi^4}
 (q^4J_8-45\pi^2q^2J_4+30\pi^4J_0).}
\]

All terms are required. For instance, the large constant theta index cancels in the complete expressions; splitting the two pieces of `B` at the upper endpoint before using their cancellation is invalid at positive physical heat time.

## 4. What this calculation establishes and leaves open

The bridge now has an explicit two-source coefficient kernel, the actual physical-energy kernel, a convergent primitive transfer with every lower endpoint, and base/vertical differentiation formulas. It establishes exact identities for the complete arithmetic source, not a signed inequality. Positivity of `psi` or of the diagonal source is insufficient to determine the signs of the cosine kernels or their physical-energy ratios. A useful next estimate must control these complete signed expressions relative to `E` uniformly along the full stationary predecessors, including the branch-0 primitive edge and the energy corner. No claim of a new theta sign domain or RH progress follows solely from the identities.

The [standard-library checker](../../numerics/check_theta_signed_bridge.py) passes 59 exact assertions and verifies finite polynomial/exponential identities and the finite covariant-jet recurrences. It does not certify infinite theta convergence, numerical signs, any uniform estimate, or collision exclusion; the convergence and endpoint justifications are analytic arguments above.

The [metric-freedom note](02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md) gives an ASD representative with unit norm and zero connection on the physical path. The [inner-profile note](../02_signed_turning_control/01_INNER_TURNING_PROFILE_20261015.md) identifies the angular concentration this bridge must control. Standard theta heat and modular-reflection identities are recorded by [DLMF 20.13](https://dlmf.nist.gov/20.13) and [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32); the normalizations here are derived from the stated theta series and the manuscript.
