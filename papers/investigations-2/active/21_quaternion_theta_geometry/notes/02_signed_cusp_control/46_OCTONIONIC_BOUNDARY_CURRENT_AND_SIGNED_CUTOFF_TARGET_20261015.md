---
research_program: PR02
secondary_programs: [ALG, PR02-CORR, PR03]
status: proved_boundary_defect_bound_and_open_energy_payment
---

# Signed octonionic boundary compression on a spectral disc

15 October 2026, America/New_York. Analytic research note prepared
for Edward Baker with substantial LLM assistance. Recorded coordinating model
`gpt-6.1-sol`, reasoning effort `ultra`. The current-session metadata verifies this configuration. This note proves a pointwise boundary-defect lower bound and a conditional relative bound; the theta-specific energy payment remains unproved. No numerical experiment is used.

## 1. Observed current and exact boundary identity

Use the conventions of Investigation 21, Notes 15 and 35:

\[
G_j(t,z)=h_j(t,z)+\mathbf jh_{j+1}(t,z),\quad
h_j=\partial_z^jH,\quad H_t=-H_{zz},\quad
\mathbf u=\ell\mathbf j.
\]

Fix real \((t,x)\) and a positive radius \(R\). All spectral circles below
keep the heat argument fixed at the real value \(t\). Put

\[
z_\theta=x+Re^{i\theta},\qquad
\langle f\rangle=\frac1{2\pi}\int_0^{2\pi}f(\theta)\,d\theta,
\qquad q(\theta)=1-\cos2\theta=2\sin^2\theta.
\]

For a fixed physical quaternion \(a=A+\mathbf jB\), a general quaternion
\(b=C+iD+\mathbf jE+\mathbf kF\), and the declared Cayley--Dickson product,

\[
\frac12\langle\mathbf u,[a\mathbf i,b\mathbf k,\ell]\rangle
=AC+BE=\operatorname{Re}(\bar a b).
\tag{1}
\]

Indeed \([a\mathbf i,b\mathbf k,\ell]= -\ell[a\mathbf i,b\mathbf k]\),
and the \(\mathbf j\) coefficient of the quaternion commutator is
\(-2(AC+BE)\). Off the physical slice the full associator can have other
components; its projection in (1), rather than its norm, is the observed
current.

There are two useful choices of this current.

**Combined energy current.** Set

\[
\phi(\theta)=\frac12\langle\mathbf u,
 [G_0(t,x)\mathbf i,G_0(t,z_\theta)\mathbf k,\ell]\rangle
=\operatorname{Re}\{h_0(t,x)H(t,z_\theta)
                     +h_1(t,x)H_z(t,z_\theta)\}.
\tag{2}
\]

The scalar holomorphic function inside the real part has value
\(E=h_0^2+h_1^2\) and second derivative
\(h_0h_2+h_1h_3=-E_t/2\) at the centre. The elementary Fourier coefficient
identity for a holomorphic function on a disc gives

\[
\langle\phi\rangle=E,\qquad
\boxed{\frac12E_t
=-\frac4{R^2}\langle\cos2\theta\,\phi\rangle
=-\frac4{R^2}E+\frac4{R^2}\langle q\phi\rangle.}
\tag{3}
\]

The factor four follows because if \(f(\zeta)=c_0+c_1\zeta+c_2\zeta^2+\cdots\),
then \(\langle\cos2\theta\operatorname{Re}f(Re^{i\theta})\rangle
=R^2\operatorname{Re}c_2/2=R^2\operatorname{Re}f''(0)/4\).
All identities are valid at \(E=0\); no quotient has been introduced.

**Separate stationary currents.** On the full stationary set
\(S_j=\{h_{j+1}(t,x)=0\}\), for \(j=0,1\), set

\[
\phi_j(\theta)=\frac12\langle\mathbf u,
 [G_j(t,x)\mathbf i,G_j(t,z_\theta)\mathbf k,\ell]\rangle
=h_j(t,x)\operatorname{Re}h_j(t,z_\theta).
\tag{4}
\]

Here the second physical coefficient of \(G_j(t,x)\) vanishes. Therefore

\[
\langle\phi_j\rangle=h_j^2,\qquad
\boxed{\mathcal L_j
=-\frac4{R^2}h_j^2+\frac4{R^2}\langle q\phi_j\rangle
\quad\text{on }S_j.}
\tag{5}
\]

For \(j=1\), this can be appreciably sharper than (3): the extra
\(h_0\operatorname{Re}H\) boundary term has zero second coefficient on
\(S_1\), but can enlarge the negative part of the combined current.
The second stationary observation remains paid by the physical energy
because \(h_1^2\le E\); the replacement of \(E\) by a four-jet ambient norm
is unnecessary.

## 2. Weighted negative mass gives the relative signed bound

For real \(v\), write \(v_-=\max(0,-v)\). Define

\[
\mathcal D_R=\langle q\phi_-\rangle,\qquad
\mathcal D_{j,R}=\langle q(\phi_j)_-\rangle.
\tag{6}
\]

Since \(q\ge0\), (3) and (5) immediately imply

\[
\boxed{\frac12E_t\ge-\frac4{R^2}(E+\mathcal D_R),}
\tag{7}
\]

\[
\boxed{\mathcal L_j\ge-\frac4{R^2}(h_j^2+\mathcal D_{j,R})
\quad\text{on }S_j.}
\tag{8}
\]

Consequently, a source-prescribed estimate

\[
\mathcal D_{j,R(t,x)}(t,x)\le\eta_j(t,x)E(t,x),\qquad j=0,1,
\tag{9}
\]

proves the desired bound

\[
\mathcal L_j\ge-\kappa_jE,\qquad
\kappa_j=\frac{4(1+\eta_j)}{R^2}.
\tag{10}
\]

The same conclusion on both stationary sets follows from
\(\mathcal D_R\le\eta E\) for the combined current. Coefficients are locally
bounded through covered candidate events if \(\eta_j\) are locally bounded
and \(R\) has a locally positive lower bound. A radius chosen to shrink
with the unknown physical energy would not establish that condition.
The domain must cover the required predecessor neighborhoods, including
the padded positive-time cusp. An estimate at a fixed positive time is
insufficient.

This is a signed result: only the negative oriented component of a
particular boundary projection is paid. It does not require an ambient
Hardy/Bergman norm, a positive full octonionic boundary field, or a bound
on tangential phase motion. Also
\(\mathcal D_R\le2\langle\phi_-\rangle\), so (7) improves the coarser estimate
\(-4(E+2\langle\phi_-\rangle)/R^2\).

The underlying eight-dimensional monogenic lift justifies use of its
genuine octonionic current. The actual reproduction takes place on the
holomorphic spectral slice, where it gives the strongest elementary
constant. An eight-dimensional harmonic ball would give
\((d+2)(d-1)/R^2=70/R^2\) under a nonnegative scalar-boundary hypothesis;
the spectral disc gives \(4/R^2\). Inflating the ambient domain therefore
does not improve the observation.

## 3. Explicit complete-source form

Write \(w_t(u)=e^{tu^2}\Phi(u)\) on \(u\ge0\), retaining the complete theta
source. Put \(a_\theta=x+R\cos\theta\), \(b_\theta=R\sin\theta\). Then

\[
\phi(\theta)=\int_0^\infty w_t(u)\cosh(b_\theta u)
\{h_0\cos(a_\theta u)-h_1u\sin(a_\theta u)\}\,du,
\tag{11}
\]

and on the respective full stationary sets,

\[
\phi_0(\theta)=h_0\int_0^\infty w_t(u)
        \cosh(b_\theta u)\cos(a_\theta u)\,du,
\tag{12}
\]

\[
\phi_1(\theta)=-h_1\int_0^\infty u w_t(u)
        \cosh(b_\theta u)\sin(a_\theta u)\,du.
\tag{13}
\]

These integrals converge uniformly on compact \((t,x,R)\) sets with
bounded positive \(R\), by the complete theta source decay. They retain
the heat factor and all source-index interactions. The negative part in
(6) must be taken **after** summing/integrating the full source; replacing
it by the sum of negative parts changes the proposed arithmetic
hypothesis and can destroy its scale. This construction avoids the
nonintegrable globally separated Poisson modes of Note 42, but it does
not prove their needed signed cancellation.

The elementary absolute source allowance only yields, for example,
\(\mathcal D_{j,R}\le |h_j|\int_0^\infty u^jw_t(u)\cosh(Ru)\,du\).
That has the \(\sqrt E\) scale and does not establish (9).

## 4. Cutoff stability without retained stationarity

Suppose a holomorphic approximation \(h_{j,N}\) has a proved uniform
spectral-circle error

\[
\sup_\theta |h_j(t,z_\theta)-h_{j,N}(t,z_\theta)|\le\epsilon_{j,N}.
\]

Retain the full real prefactor \(h_j(t,x)\) and full stationarity
\(h_{j+1}(t,x)=0\), and define

\[
\mathcal D_{j,R,N}=\langle q\{h_j(t,x)
                       \operatorname{Re}h_{j,N}(t,z_\theta)\}_-\rangle.
\]

The negative-part map is 1-Lipschitz, \(\langle q\rangle=1\), and
\(|h_j|\le\sqrt E\) on \(S_0\cup S_1\), whence

\[
|\mathcal D_{j,R}-\mathcal D_{j,R,N}|
\le\sqrt E\,\epsilon_{j,N}.
\tag{14}
\]

Thus an all-cutoff family
\(\mathcal D_{j,R,N}\le a_N E+b_N\) gives

\[
\mathcal L_j\ge-\frac4{R^2}
\{(1+a_N)E+b_N+\sqrt E\,\epsilon_{j,N}\}.
\tag{15}
\]

For every \(\gamma_N>0\), the last term is at most
\(\gamma_NE/2+\epsilon_{j,N}^2/(2\gamma_N)\). Therefore a Gaussian circle
tail and a polynomial or Note-44 subpower cutoff cost would feed the
existing conditional transfer theorem, provided the whole family and
its source rules are proved first. Equation (14) does not assert that an
arbitrary holomorphic approximation preserves the original hybrid
staircase. If that staircase is used, its paired holomorphic
complexification and uniform complex-circle tail must be established
with all original boundaries and source terms retained.

## 5. The original staircase admits a paid holomorphic boundary extension

The complex-circle approximation in Section 4 can be supplied by the
original hybrid staircase without inventing a different source cutoff.
Fix \(0<a<\pi/8\), \(0\le t\le T<\infty\), and write
\[
\phi_n(\zeta)=(2\pi^2n^4e^{9\zeta}-3\pi n^2e^{5\zeta})
e^{-\pi n^2e^{4\zeta}},\qquad
V_N=\tfrac12\log N,
\]
\[
\psi_{a,N}(t,y)=e^{t(y+ia)^2}
\sum_{n\le Ne^{-2y}}\phi_n(y+ia),\qquad 0\le y\le V_N.
\]
For integer \(N\ge1\), define the entire function of the spectral variable
\[
\mathscr H_N(t,z)=\frac12\int_0^{V_N}
\left\{\psi_{a,N}(t,y)e^{(-a+iy)z}
+\overline{\psi_{a,N}(t,y)}e^{(-a-iy)z}\right\}dy.
\tag{17}
\]
The conjugation refers to real \(t\). On the real line, its \(j\)-th
spectral derivative is exactly the original retained physical jet:
\[
\partial_z^j\mathscr H_N(t,x)
=e^{-ax}\Re\int_0^{V_N}
(-a+iy)^j\psi_{a,N}(t,y)e^{ixy}\,dy=h_j^{(N)}.
\]
The complete version, integrating to infinity and keeping every index,
equals \(H(t,z)\). It agrees on the real line by the complete-source
contour identity in [Note 12](../12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md),
and equality extends to complex \(z\) by entireness. The complete-source
vertical cancellation is used only before separating its theta indices.

Put
\[
\beta=\pi\cos(4a)>0,\qquad c_a=\beta/2,
\]
\[
Q_j(T,R,a)=\int_0^\infty(a+y)^j e^{Ty^2+Ry}
\sum_{n\ge1}
(2\pi^2n^4e^{9y}+3\pi n^2e^{5y})
e^{-c_a n^2e^{4y}}\,dy.
\tag{18}
\]
Then, uniformly on \(|z-x|\le R\),
\[
\boxed{|h_j(t,z)-\partial_z^j\mathscr H_N(t,z)|
\le e^{-a(x-R)}Q_j(T,R,a)e^{-c_aN^2}.}
\tag{19}
\]
Indeed, the omitted staircase region is exactly \(n^2e^{4y}>N^2\).
Extract \(e^{-c_aN^2}\) from
\(e^{-\beta n^2e^{4y}}\), and retain the remaining factor in (18).
Both conjugate branches have the same bound and their half factors pay
their sum. The spectral derivatives cost at most \((a+y)^j\).
The heat factor has modulus at most \(e^{Ty^2}\), and the spectral
factor is at most \(e^{-a(x-R)}e^{Ry}\).

The constants \(Q_j\) are finite and locally bounded for finite \(T,R\)
and fixed \(a\) in its open strip. For \(S=n^2e^{4y}\), use
\[
e^{-c_aS}\le
e^{-(c_a/2)n^2}e^{-(c_a/2)e^{4y}}.
\]
The resulting index sums converge and the remaining integral is
dominated by a polynomial times
\(\exp\{Ty^2+(R+9)y-(c_a/2)e^{4y}\}\).
A varying contour \(a\) would need to remain locally inside
\((0,\pi/8)\). No staircase edge is differentiated or suppressed:
only \(z\)-derivatives are taken, and the source domain is unchanged.

There is now a fully specified analytic cutoff target. Suppose, on both
full \(S_j\) in a declared predecessor-covering domain, one proves for
**every** integer \(N\ge N_{0,j}\ge8\),
\[
\mathcal D_{j,R,N}
\le \alpha_j\mathfrak C_{j,N}E+B_j e^{-d_jN^2},
\quad
\mathfrak C_{j,N}=N^p e^{\sigma_j(\log N)^2},
\tag{20}
\]
where \(p\ge0\) is fixed, \(\alpha_j,B_j,\sigma_j\ge0\),
\(d_j>0\), and all coefficients, inverse rates, \(N_{0,j},R,1/R\)
are source-prescribed and locally bounded through covered finite events.
Here the retained boundary current uses the **full** real factor \(h_j\)
and \(\partial_z^j\mathscr H_N\) on the circle.

Equations (14), (19), and Young's inequality with parameter one give
\[
\boxed{
\mathcal L_j\ge
-\frac4{R^2}(\alpha_j+\tfrac32)\mathfrak C_{j,N}E
-\frac4{R^2}
\left\{B_j+\tfrac12e^{-2a(x-R)}Q_j(T,R,a)^2\right\}
e^{-\min(d_j,2c_a)N^2}.}
\tag{21}
\]
The absorption uses \(\mathfrak C_{j,N}\ge1\).
Thus (20), if proved for the actual theta source, feeds either the
original polynomial transfer (\(\sigma_j=0\)) or the
[subpower transfer of Note 44](44_SUBPOWER_CUTOFF_TRANSFER_AND_ANALYTIC_RIGIDITY_20261015.md).
No observed energy denominator or energy floor enters any coefficient.

The staircase construction and Gaussian-circle payment (17)–(19) are
proved here. The **signed** boundary estimate (20) is not. This is the
remaining arithmetic premise, not an assumption that cutoff stability
itself establishes.

## 6. Sharpness, controls, and the remaining theta obligation

The constant four in (7) cannot be improved under boundary nonnegativity,
even on \(S_0\). At a fixed time, consider the even polynomial

\[
P_n(z)=1+2\sum_{k=1}^n\left(1-\frac{k}{n+1}\right)(z/R)^{2k}.
\]

It has \(P_n(0)=1\), \(P_n'(0)=0\), and nonnegative boundary real part:
\(\operatorname{Re}P_n(Re^{i\theta})\) is the Fejér kernel at angle
\(2\theta\). Its stationary value is
\(-P_n(0)P_n''(0)=-4n/((n+1)R^2)\). Its exact polynomial backward-heat
extension is \(e^{-(t-t_0)\partial_z^2}P_n(z)\). Letting \(n\to\infty\)
shows sharpness.

For the double collision control
\(H(t,z)=z^2-2(t-T)\), at \(t=T-\delta,x=0\),

\[
E=4\delta^2,\qquad
\phi_0(\theta)=2\delta(2\delta+R^2\cos2\theta),
\]

and dominated convergence gives

\[
\frac{\mathcal D_{0,R}}{E}
\sim\frac{R^2}{2\delta}\left(\frac1\pi+\frac14\right)
\quad(\delta\downarrow0).
\tag{16}
\]

Indeed the two relevant elementary averages are
\(\langle(-\cos2\theta)_+\rangle=1/\pi\) and
\(\langle\cos^22\theta\,1_{\cos2\theta<0}\rangle=1/4\).
The cubic control \(H=z^3-6(t-T)z\) at the same predecessor has
\(E=36\delta^2\), \(\phi_1=6\delta(6\delta+3R^2\cos2\theta)\), and
exactly the same asymptotic ratio. Thus the criterion correctly rejects
both polynomial stationary collision mechanisms.

There is also a useful limit on the criterion itself: it is stronger
than the original signed lower bound. At a time slice with
\(H(z)=\varepsilon-z^2\), \(x=0\), the stationary sign
\(\mathcal L_0=2\varepsilon\) is favorable, but
\(\mathcal D_{0,R}/E\to\infty\) as \(\varepsilon\downarrow0\) for a fixed
radius. Paying all negative boundary mass can discard a compensating
positive weighted mass. It is a concrete sufficient mechanism, not an
equivalent reformulation claimed to be automatically easier.

What remains is a theta-specific proof of (9), or directly a lower bound
for the signed weighted integral \(\langle q\phi_j\rangle\), with
source-prescribed coefficients and predecessor coverage. The octonionic
monogenic lift, Dirac identities, positive Hilbert-space norms, and
boundary reproduction alone do not supply that source estimate. The
explicit formulas above identify exactly the oriented quantity such a
proof would have to control.


## 7. Analytic status and related work

[Note 47](../04_octonionic_reductions/47_ORIENTED_CURRENT_AND_ACCRETIVE_SOURCE_CERTIFICATES_20261015.md)
proves an unconditional averaged signed-current bound and separates
unrestricted angular heat motion from the radial loss.
[Note 48](../05_theta_correlation_kernels/48_E8_CHARACTER_PROJECTION_AND_SIGNED_HEAT_SECTORS_20261015.md)
gives an exact finite E8-character source realization, while showing why
untwisted positivity and separate auxiliary norms do not pay (9) or (20).
[Review 29](../../reviews/29_OCTONIONIC_SIGNED_BOUND_ANALYTIC_REVIEW_20261015.md)
records independent analytic checking, including (17)–(21).
No numerical experiment, new pointwise sign domain, or collision exclusion
is asserted. The actual theta energy-relative boundary estimate remains open.
