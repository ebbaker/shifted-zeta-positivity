# Exact theta superspace and a regular completion obstruction

10 October 2026. GPT-6 (Codex); exact serving variant and configured
reasoning effort unavailable. This is an analytic scout with internal
LLM checks, not independent mathematical validation.

This note tests the concrete finite-dimensional architecture requested by
[Program 04](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
It establishes exact matching and specific obstructions, not a localization
theorem for an unspecified arithmetic field theory.

## 1. A fully specified genuine theta dictionary

Take the even extension of the stable manuscript's kernel
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}}\quad(u\ge0).
\]
Set \(Z_t=H_t(0)\), \(\rho_t=e^{tu^2}\Phi_e/(2Z_t)\).
Let \(M_t(u)=\int_{-\infty}^u\rho_t(v)\,dv\), and write \(N\) and
\(\varphi\) for the standard Gaussian CDF and density. Define
\[
F_t(u)=N^{-1}(M_t(u)),\qquad
F_t'(u)=\rho_t(u)/\varphi(F_t(u))>0.
\tag{1}
\]
This is a smooth odd diffeomorphism of the line. It matches the full
theta density rather than the gamma factor or a fit to finitely many
moments. It is also a generic transformation available for every smooth
strictly positive probability density; matching alone supplies no
arithmetic rigidity.

Introduce two real commuting variables \(u,b\) and Grassmann variables
\(\psi,\bar\psi\). Choose the orientation
\(\int d\bar\psi\,d\psi\,\bar\psi\psi=1\), and the nilpotent derivation
\[
Qu=\psi,\quad Q\psi=0,\quad Q\bar\psi=ib,\quad Qb=0.
\]
For \(V=\bar\psi(F_t(u)-ib/2)\), the full action is
\[
S_{\lambda,t}=\lambda QV
=\lambda\{b^2/2+ibF_t(u)-\bar\psi F_t'(u)\psi\},
\qquad \lambda>0.
\tag{2}
\]
No determinant sign is hidden: the chosen fermion orientation gives
\(+\lambda F_t'\). With measure \(du\,db/(2\pi)\,d\bar\psi\,d\psi\),
first perform the Berezin integral and then the real Gaussian \(b\)
integral. The effective bosonic density is
\[
p_{\lambda,t}(u)=\sqrt{\lambda/(2\pi)}F_t'(u)
e^{-\lambda F_t(u)^2/2},\qquad
\int_{\mathbb R}p_{\lambda,t}=1.
\tag{3}
\]
At \(\lambda=1\), (1) makes \(p_{1,t}=\rho_t\) exactly.

This ordering is part of the definition. Before the \(b\) integration
the \(u,b\) integral is oscillatory and not absolutely integrable;
its two integrations cannot be freely interchanged. A regulator
\(|u|\le R\) followed by this Gaussian integration and \(R\to\infty\)
gives the same (3). The resulting endpoint terms vanish because
\(F_t(\pm R)\to\pm\infty\). Real contours and orientation are fixed.
For polynomially growing observations every reduced integral converges
on compact time and positive-\(\lambda\) intervals. Theta's
super-Gaussian tails imply \(|F_t^{-1}(v)|\le C(1+|v|)\) outside a
compact set, which suffices after changing variables to \(v=F_t(u)\).

## 2. Exact evolution and all spatial readouts

The intended observation is
\[
\mathcal H_{\lambda,t}(x)=Z_t\int p_{\lambda,t}(u)\cos(xu)\,du.
\]
At \(\lambda=1\), it gives \(H_t\), and in particular
\(H_0=\xi(1/2+ix/2)/8\). For \(j=0,\dots,4\),
\[
\partial_x^j\mathcal H_{1,t}(x)=
Z_t\mathbb E_{\rho_t}[u^j\cos(xu+j\pi/2)].
\tag{4}
\]
These are fixed-time derivatives. All tail terms vanish by theta decay.
From \(\dot\rho_t=(u^2-\mu_2)\rho_t\) and
\(\dot Z_t=\mu_2Z_t\), one obtains
\[
\partial_t\mathcal H_{1,t}=-\partial_x^2\mathcal H_{1,t}.
\tag{5}
\]
Thus the exact Newman sign comes from the moving arithmetic state and
normalization. If the superspace state is presented by (2), its action
contains the moving map \(F_t\). Suppressing its time derivative would
not reproduce (5). At \(\lambda\ne1\) no same heat equation is asserted.

## 3. A deformation identity with a strict jet mismatch

The partition function in (3) is independent of \(\lambda\). The
collision observation is not. For an admissible differentiable \(f\),
integrating a total \(u\)-derivative gives
\[
\partial_\lambda\mathbb E_{p_\lambda}f
=-\frac1{2\lambda}\mathbb E_{p_\lambda}
\left[f'(u)\frac{F_t(u)}{F_t'(u)}\right].
\tag{6}
\]
Indeed
\(\partial_\lambda p_\lambda=(1-\lambda F_t^2)p_\lambda/(2\lambda)\);
the same quantity is
\(\sqrt{\lambda}(2\lambda)^{-1}
\partial_u[F_t\varphi(\sqrt{\lambda}F_t)]\).
The boundary term vanishes after the prescribed bosonic reduction.
For the physical characteristic function,
\[
\partial_\lambda C_{\lambda,t}(x)=
\frac{x}{2\lambda}\mathbb E_{p_\lambda}
\left[\sin(xu)\frac{F_t(u)}{F_t'(u)}\right].
\tag{7}
\]
A nontrivial new mismatch is visible without numerical approximation:
\[
\boxed{\partial_\lambda C_{\lambda,t}''(0)
=\lambda^{-1}\mathbb E_{p_\lambda}
\left[u\,F_t(u)/F_t'(u)\right]>0.}
\tag{8}
\]
Oddness and strict monotonicity make \(uF_t(u)>0\) away from zero;
the density and \(F_t'\) are positive. The expectation is finite by
the preceding tail argument. Thus even the second spatial jet is
changed by the localization deformation. Partition-function protection
cannot protect the genuine value/derivative/jet observation.

## 4. No regular completion with the prescribed bosonic component

In this quartet a general even observation has the form
\[
\mathcal O=f(u,b)+\bar\psi\psi\,g(u,b).
\]
Its closure condition is exactly
\[
Q\mathcal O=(\partial_uf+ibg)\psi=0.
\tag{9}
\]
If \(f,g\) are regular at \(b=0\), evaluating (9) there gives
\(\partial_uf(u,0)=0\). Consequently there is no regular \(Q\)-closed
completion retaining \(f(u,0)=\cos(xu)\) for \(x\ne0\).
The formal choice \(g=-\partial_uf/(ib)\) has a pole on the real
integration contour and lies outside the chosen observation domain.

This is restricted to the specified quartet, regular observables, and
the specified bosonic-component requirement. It does not exclude a
different supercharge, additional fields, boundary observables, or an
equivariant construction. Those would need a new exact dictionary.

## 5. A finite arithmetic block: exact but only spectator protection

To test the other proposed interface, fix
\(I=\{1,2,3,4,6,9\}\subseteq\{n\le N\}\). Use the genuine Note 8 data,
\[
a_n=\log w_n+i\phi_n,\quad
w_n=e^{t\log^2n/4-(1/2+t\alpha_r/2)\log n},\quad
\phi_n=\theta_t+(x-t\alpha_i)\log n/2.
\]
For each sector \(n\), take the same action (2) with \(F(u)=u\);
its reduced partition integral is one. Give that sector the
\(Q\)-inert observation \(2\operatorname{Re}e^{a_n(t,x)}\).
The finite sum reduces exactly to \(F_{t,I}=2\sum_Iw_n\cos\phi_n\),
with every determinant and orientation as in (3).

At fixed time and fixed set \(I\), the first four derivatives are exactly
\[
F_{t,I}^{(j)}=2\operatorname{Re}\sum_Ie^{a_n}\mathcal B_j(a_n',\dots,a_n^{(j)}),
\tag{10}
\]
where
\[
\mathcal B_0=1,\quad\mathcal B_1=a',\quad
\mathcal B_2=a''+(a')^2,\quad
\mathcal B_3=a'''+3a'a''+(a')^3,
\]
\[
\mathcal B_4=a''''+4a'a'''+3(a'')^2+6(a')^2a''+(a')^4.
\]
The first derivative therefore retains both amplitude drift and phase
motion. This algebraic protection also holds for every freely assigned
sector coefficient or multiplicative twist. It imports the arithmetic
sum as an external observation and gives no relation among its terms.
The small set \(I\) is not the genuine heat function. Only the full
fixed-cutoff sum \(F_{t,N}\), together with Note 13's
\(j!L^j\eta_N\) payments and measured quadratic payment, has the
existing approximation interface.

## 6. Result and next task

The full theta superspace reduction is exact, with an explicit action,
orientation, contour and ordered-integral domain. Its physical heat
observable changes under the deformation, as the strict identity (8)
proves. The regular completion obstruction (9) identifies exactly where
the attempted protection fails. The finite-sector version is protected
but provides only a re-encoding of arbitrary coefficients.

No signed candidate consequence, new theta arithmetic relation, or
collision exclusion is established. A next localization task should
exhibit a different admissible protected observation whose completed
bosonic reduction still equals the required jets and whose Ward identity
constrains them. Making the partition function's invariant value one
does not address this missing step.

This derivation uses no imported localization theorem. The earlier
Witten example in Note 14 supplies context, not a theorem applied to
theta. Files follow [LARGE_FILES.md](../../../../../LARGE_FILES.md).
