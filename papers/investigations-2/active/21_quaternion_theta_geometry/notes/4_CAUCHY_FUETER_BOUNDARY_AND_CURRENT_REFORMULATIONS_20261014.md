# Cauchy Fueter boundary and current reformulations

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

The adopted independent-time lift admits a compact conjugate-Fueter heat
equation, Cauchy boundary reconstruction of its spatial jets, and signed
boundary expressions for both stationary Laguerre forms. Its two
stationary sign targets can also be combined into one condition on the
time derivative of the physical norm. These are exact reformulations;
the signed theta estimate remains the next construction task.

## Field and classical inputs

Use the [standard convention](3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md),
with t an independent real parameter,

\[
q=z_0+\mathbf jz_1,
\quad \tau=t+\overline{z_1},
\quad F(t,q)=H(\tau,z_0)+\mathbf jH_z(\tau,z_0),
\quad \bar\partial_qF=0.
\]

The real quaternion coordinates are \(q_0=a,q_1=b,q_2=c,q_3=-d\)
when \(z_0=a+ib,z_1=c+id\). All operators below use this standard
Hamilton orientation. Define the normalized conjugate operator

\[
\partial_q=\frac12(\partial_{q_0}-\mathbf i\partial_{q_1}
-\mathbf j\partial_{q_2}-\mathbf k\partial_{q_3}).
\]

The classical inputs are harmonicity and Cauchy--Fueter reproduction,
with its left/right multiplication order. Primary references are
[Sudbery, Sections 3 and 4](https://dougsweetser.github.io/Q/Stuff/pdfs/Quaternionic-analysis.pdf)
and [Frenkel and Libine, Theorem 9](https://arxiv.org/pdf/0711.2699).
The spherical moment formulas below are differentiated consequences of
the harmonic Poisson formula, also given in Frenkel and Libine,
Theorem 34. The additional identities are derived for the declared lift.

## Conjugate Fueter evolution and one fixed field

Since \(\partial_q+\bar\partial_q=\partial_{q_0}\), every regular
field satisfies \(\partial_qF=\partial_{q_0}F\). Real derivatives
commute with \(\bar\partial_q\). Thus, for the adopted field,

\[
G_m:=\partial_q^mF=\partial_{q_0}^mF
=h_m+\mathbf jh_{m+1},
\qquad h_m=\partial_z^mH(\tau,z_0),
\qquad \bar\partial_qG_m=0.
\]

Here holomorphy in \(z_0\) identifies the q_0 derivative with the
componentwise spectral derivative. The heat equation becomes

\[
\boxed{\bar\partial_qF=0,\qquad
\partial_tF=-\partial_q^2F.}
\tag{1}
\]

Regularity alone does not impose the original jet relation. The pair
constraint \(V=U_{z_0}\), the dependence on \(\tau=t+\overline{z_1}\),
and the theta trace remain part of the declared state.

There is also exact translation equivariance:

\[
\boxed{F(t,q)=F(0,q+\mathbf jt).}
\tag{2}
\]

Thus, putting \(\mathcal F(q)=F(0,q)\), the existing RH endpoint becomes

\[
\boxed{\mathrm{RH}\iff
\mathcal F(x+\mathbf js)\ne0
\quad(x\in\mathbb R,\ s>0).}
\tag{3}
\]

This is a zero-free positive j half-plane for one explicitly defined
entire Fueter-regular field. It is a consequence of the chosen lift;
external Newman time is still independent in (1). The scalar coordinate
of that half-plane is spectral x, not Newman time.

## Cauchy boundary reconstruction and a residual formula

Fix real t and a bounded domain \(\Omega\subset\mathbb H\) with smooth
boundary. Let n(p) be its outward unit normal, represented as a quaternion,
and let q be in its interior. For

\[
E(r)=\frac{\overline r}{2\pi^2|r|^4},
\]

the left Cauchy--Fueter formula is

\[
\boxed{F(t,q)=\int_{\partial\Omega}
E(p-q)n(p)F(t,p)\,dS_p.}
\tag{4}
\]

The order is kernel, normal, field. E is the fundamental kernel for
the unnormalized operator \(D=2\bar\partial_q\); the fundamental
kernel for \(\bar\partial_q\) is 2E, but (4) retains the displayed E.

Stokes and the same kernel give the Borel--Pompeiu form for any
quaternion-valued \(C^1\) field A near the closure of \(\Omega\):

\[
A(q)=\int_{\partial\Omega}E(p-q)n(p)A(p)\,dS_p
-2\int_\Omega E(p-q)\bar\partial_pA(p)\,dV_p.
\tag{5}
\]

This is a direct residual extension of (4), derived from the classical
Stokes formula. It retains the regularity defect of an approximation
rather than treating approximate boundary data as an exact regular field.
The kernel is locally integrable in four dimensions. No derivative of
the singular volume kernel is asserted here.

## Spatial jets as boundary operators

For q in a compact interior set, differentiating (4) is legitimate.
Define

\[
K_m(p;q)=\bigl(\partial_{q_0}^{\,m}E(p-q)\bigr)n(p),
\qquad
A_m(t,q)=\int_{\partial\Omega}K_m(p;q)F(t,p)\,dS_p.
\]

Then \(A_m=G_m\). At real \(q=x\), these are
\(A_m=h_m(t,x)+\mathbf jh_{m+1}(t,x)\). In particular,

\[
\mathscr L_j(t,x)=\operatorname{Re}
\bigl(\mathbf j\overline{A_j(t,x)}A_{j+1}(t,x)\bigr),
\qquad j=0,1.
\tag{6}
\]

Expanding the products gives the nonlocal signed boundary form

\[
\mathscr L_j(t,x)=\operatorname{Re}\!\left[
\mathbf j\iint_{\partial\Omega\times\partial\Omega}
\overline{F(t,p)}\,\overline{K_j(p;x)}
K_{j+1}(r;x)F(t,r)\,dS_p\,dS_r\right].
\tag{7}
\]

Quaternion conjugation reverses the first product's order. The kernel
in (7) is a signed quadratic observation, not a positive square. This
gives a concrete nonlocal boundary class for the next arithmetic estimate.
The full boundary trace of the genuine theta lift is the source constraint;
replacing it by arbitrary regular data admits the polynomial control.

## Spherical moments make the boundary target explicit

For a ball of radius R centered at real x, let

\[
\langle g\rangle=\frac1{2\pi^2}\int_{S^3}g(\omega)\,dS_\omega,
\qquad B(\omega)=F(t,x+R\omega).
\]

At the center, the Cauchy kernel times the outward normal is a positive
scalar, so (4) reduces to \(A_0=\langle B\rangle\).
Differentiating harmonic Poisson reproduction with the sphere fixed gives

\[
\boxed{
A_0=\langle B\rangle,\qquad
A_1=\frac4R\langle\omega_0B\rangle,\qquad
A_2=\frac6{R^2}\langle(4\omega_0^2-1)B\rangle.}
\tag{8}
\]

The constants 4 and 6 are for real dimension four. Formula (6) now
expresses both stationary forms using only the first three boundary
moments. Stationarity is \(P_0A_1=0\) or \(P_0A_2=0\), where
\(P_0(A+\mathbf jB)=A\). The physical energy is \(|A_0|^2\).
The negative-loss target is therefore the corresponding signed moment
correlation bounded below by \(-K|A_0|^2\).

For \(M=\sup_{\partial B_R}|F|\), the elementary estimates from (8) are
\(|A_1|\le4M/R\) and \(|A_2|\le18M/R^2\).
They are upper derivative bounds; they do not supply the required lower
sign or bounded-loss ratio through a cancellation of \(A_0\).

Boundary points generally involve complex Newman time
\(\tau=t+\overline{z_1}\). Real-time signs are not automatic boundary
signs on this sphere. Because the complex pair is holomorphic in
\((z_0,w)\), w=\(\overline{z_1}\), componentwise two-variable complex
Cauchy on a polydisc is an alternative reproduction formula. It carries
the same data; the quaternion formula does not introduce extra source
information. Perotti's harmonic-plus-boundary regularity criterion
([Corollary 3](https://arxiv.org/pdf/math/0612092)) is another possible
boundary formulation, with a complex-coordinate conversion required
before using his N and T operators in this right-coefficient convention.

## Both stationary signs as one norm evolution condition

On the physical real slice,

\[
\mathcal E(t,x)=|F(t,x)|^2=H^2+H_x^2,
\qquad
\partial_t\mathcal E=-2(HH_{xx}+H_xH_{xxx}).
\]

Therefore

\[
H_x=0\Rightarrow\partial_t\mathcal E=2\mathscr L_0,
\qquad
H_{xx}=0\Rightarrow\partial_t\mathcal E=2\mathscr L_1.
\]

The two sufficient stationary signs are exactly the single constrained
condition

\[
\boxed{\partial_t\mathcal E\ge0
\quad\text{where }H_xH_{xx}=0.}
\tag{9}
\]

Likewise a single nonnegative locally bounded K gives both loss bounds
if

\[
\partial_t\mathcal E\ge-2K\mathcal E
\quad\text{where }H_xH_{xx}=0.
\tag{10}
\]

Conversely take K=\(\max(K_0,K_1)\) from the two original bounded-loss
coefficients. Domain and predecessor coverage are unchanged. In the declared quaternion notation,
\(P_0F=\tfrac12(F-\mathbf iF\mathbf i)\), so the stationary union is
\((P_0\partial_qF)(P_0\partial_q^2F)=0\) on the real slice.
This norm-time criterion is distinct from vertical convexity of the total
norm, which remains insufficient.

## Conserved signed currents and harmonic positivity

For each regular jet \(G_j\), all components are harmonic. Define the
imaginary-quaternion-valued current

\[
J_\mu^{(j)}=\operatorname{Im}
\bigl(\overline{G_j}\,\partial_{q_\mu}G_j\bigr).
\]

Direct differentiation gives

\[
\sum_{\mu=0}^3\partial_{q_\mu}J_\mu^{(j)}
=\operatorname{Im}\!\left(
\sum_\mu|\partial_{q_\mu}G_j|^2+\overline{G_j}\Delta_4G_j\right)=0.
\tag{11}
\]

On the real physical slice,
\([J_0^{(j)}]_{\mathbf j}=-\mathscr L_j\).
The flux through a closed boundary vanishes, but conservation does not
fix the sign of an individual oriented component. Formula (11) is an
exact current candidate whose signed transverse contributions must be
controlled by theta information.

For the total norm, harmonicity instead gives

\[
\Delta_4|F|^2=2\sum_\mu|\partial_{q_\mu}F|^2
=4\bigl(|H_z|^2+2|H_{zz}|^2+|H_{zzz}|^2\bigr)\ge0.
\tag{12}
\]

Where \(|F|^2>0\), the special holomorphic pair in \((z_0,\tau)\)
also gives

\[
\Delta_4\log|F|^2
=\frac{4\bigl(|\mathscr L_0|^2+|\partial_z\mathscr L_0|^2\bigr)}{|F|^4},
\qquad
\partial_z\mathscr L_0=H_zH_{zz}-HH_{zzz}.
\tag{13}
\]

Formula (13) follows from the two-variable complex logarithmic norm
identity for the pair (H,\(H_z\)), not generic Fueter regularity alone.
It squares away the needed orientation and is undefined at joint zeros.
Subharmonic norms and logarithmic norms permit zeros.

## Limits of inverse and degree shortcuts

Pointwise inversion does not preserve Fueter regularity. For the simple
backward-heat control H(\(\tau,z\))=z, the lift is
\(F=z_0+\mathbf j\), everywhere nonzero. Nevertheless

\[
F^{-1}=\frac{\overline{z_0}-\mathbf j}{1+|z_0|^2},
\qquad
\bar\partial_q(F^{-1})=
\frac{1+\mathbf j\overline{z_0}}{(1+|z_0|^2)^2}\ne0.
\tag{14}
\]

Thus the ordinary complex reciprocal and logarithmic-derivative Cauchy
argument cannot be imported unchanged. For the general failures of
product closure and isolated-zero behavior see Sudbery's introduction.
Conjugation also turns left regularity into right regularity for the
conjugate operator, not the same operator; a homogeneous bilinear Stokes
formula for \(\overline F\,nF\) would omit a volume term.

For this declared lift there is a precise Jacobian observation:

\[
\det_{\mathbb R}(d_qF)=-|\mathscr L_1(\tau,z_0)|^2.
\tag{15}
\]

The complex determinant of the pair (H,\(H_z\)) in (\(z_0,\tau\))
is \(\mathscr L_1\). The quaternion output coordinates reverse the
imaginary component of \(H_z\), accounting for the minus orientation.
A double physical collision has \(\mathscr L_1=H_{xx}^2\ne0\),
so it is a nondegenerate zero of the full quaternion map. Nondegeneracy
of quaternion zeros does not exclude the scalar collision.

## Control check and next arithmetic task

For \(P(\tau,z)=z^2-2\tau+1\), the lift satisfies all the above
regularity and reproduction identities. At real center x its moments are

\[
A_0=x^2-2t+1+2\mathbf jx,\qquad
A_1=2x+2\mathbf j,\qquad A_2=2,
\]

giving \(\mathscr L_0=2x^2+4t-2\) and \(\mathscr L_1=4\).
At x=0 and \(t<1/2\), (9) fails; at \((1/2,0)\), the physical
field vanishes despite \(\det d_qF_P=-16\).

The [exact polynomial checker](../numerics/check_fueter_boundary_identities.py)
and [small execution record](../numerics/FUETER_BOUNDARY_IDENTITY_CHECKS_20261014.json)
check the lift, first three spherical moments, and control observations
with rational arithmetic. They are consistency checks, not theta
certificates. The [internal review](../reviews/2_CAUCHY_FUETER_REFORMULATIONS_INTERNAL_REVIEW_20261014.md)
records the analytic checks and source conventions.

The next task is to choose a bounded predecessor domain and prove a
theta-specific signed boundary correlation or current estimate sufficient
for (9) or (10). The sphere formula keeps the exact mixed signs, while
the current formula isolates the oriented physical component. Absolute
Cauchy estimates and generic regularity do not make that estimate.
