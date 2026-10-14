# Octonionic heat lift and signed associator targets

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**,
verified in the current turn metadata. Parallel LLM algebra, differential,
and exact-arithmetic checks supported this investigation.

The quaternion theta jet admits an explicit globally real analytic,
eight-dimensional left monogenic extension that preserves external heat
evolution. Fixed quaternionic twists also express the physical collision
energy and both stationary signs as oriented octonionic associators.
These are exact constructions. They do not yet give a new theta inequality:
the same structures occur for strictly positive, even, analytic sources
whose heat transforms have positive-time collisions. The useful next
target is a source-specific lower bound for the radial heat residual,
retaining its complete arithmetic cancellation.

The height-100 certificates and manuscript remain the baseline. This note
develops the octonionic continuation proposed after
[Note 14](14_SUMMARY_AND_CONTINUATION_20261014.md); it changes neither their
scope nor the remaining collision region in
[Note 13](13_NORMALIZED_SIGN_TARGET_IN_THE_COLLISION_CUSP_20261014.md).

## 1. Conventions and the existing jet family

Write octonions as quaternion pairs, with the extra unit on the left:

\[
(a,b)=a+\ell b,\qquad
(a,b)(c,d)=(ac-d\bar b,\bar a d+cb),\qquad
\overline{(a,b)}=(\bar a,-b).
\tag{1}
\]

Quaternion units satisfy \(\mathbf i\mathbf j=\mathbf k\). Every product
with three octonionic factors has its parentheses specified. Set

\[
[A,B,C]=(AB)C-A(BC),\qquad
\langle A,B\rangle=\operatorname{Re}(\bar A B),\qquad
\mathbf u=\ell\mathbf j.
\tag{2}
\]

Equation (1) is the Cayley--Dickson convention described in
[Baez, Section 2.2](https://math.ucr.edu/home/baez/octonions/node5.html).
The associator and alternativity conventions are in his
[preliminaries](https://math.ucr.edu/home/baez/octonions/node2.html).
All special jet and extension formulas below are derived with (1).

Use real quaternion coordinates

\[
q=x_0+\mathbf i x_1+\mathbf j x_2+\mathbf k x_3,
\qquad z=x_0+\mathbf i x_1,\qquad \tau=t+x_2+\mathbf i x_3.
\]

This agrees with the adopted \(q=z_0+\mathbf jz_1\) convention, since
\(z_1=x_2-\mathbf i x_3\). Put

\[
h_m=\partial_z^mH(\tau,z),\qquad
G_m=h_m+\mathbf jh_{m+1},\qquad F=G_0.
\tag{3}
\]

The complete theta family is jointly entire and satisfies
\(H_\tau=-H_{zz}\). With the unnormalized operators
\(D_q=\partial_{x_0}+\mathbf i\partial_{x_1}
+\mathbf j\partial_{x_2}+\mathbf k\partial_{x_3}\) and
\(\bar D_q=\partial_{x_0}-\mathbf i\partial_{x_1}
-\mathbf j\partial_{x_2}-\mathbf k\partial_{x_3}\), the established lift gives

\[
D_qG_m=0,\quad \bar D_qG_m=2G_{m+1},\quad
\partial_tG_m=-G_{m+2},
\tag{4}
\]
\[
\partial_{x_0}G_m=G_{m+1},\quad
\partial_{x_1}G_m=G_{m+1}\mathbf i,\quad
\partial_{x_2}G_m=-G_{m+2},\quad
\partial_{x_3}G_m=-G_{m+2}\mathbf i.
\tag{5}
\]

On the physical slice \(q=x\), all \(h_m\) are real. Then
\(F=h_0+\mathbf jh_1\), \(F_x=G_1\), \(F_{xx}=G_2=-F_t\), and

\[
E=|F|^2=h_0^2+h_1^2,\qquad
L_j=h_{j+1}^2-h_jh_{j+2}\quad(j=0,1).
\tag{6}
\]

## 2. A full octonionic monogenic extension

Let \(r=y_0+\mathbf i y_1+\mathbf j y_2+\mathbf k y_3\), and identify
the eight-dimensional argument with \(p=q+\ell r\). Set
\(e_0=1,e_1=\mathbf i,e_2=\mathbf j,e_3=\mathbf k\). The standard left
operator in this orthonormal basis is

\[
\mathcal D_8=\sum_{\mu=0}^3e_\mu\partial_{x_\mu}
+\sum_{\mu=0}^3(\ell e_\mu)\partial_{y_\mu}.
\]

For a pair-valued field \((A,B)\), direct use of (1) gives

\[
\mathcal D_8(A,B)=
\left(D_qA-\sum_\mu B_{y_\mu}\bar e_\mu,
\bar D_qB+\sum_\mu A_{y_\mu}e_\mu\right).
\tag{7}
\]

Consequently, simply extending \((G_m,G_{m+2})\) constantly in \(r\)
has defect \((0,2G_{m+3})\); two left regular components do not suffice.
There is nevertheless an explicit correction:

\[
\boxed{\mathcal O_m(t,q,r)=
\left(G_m(t,q)-\frac12G_{m+3}(t,q)\bar r,
G_{m+2}(t,q)\right).}
\tag{8}
\]

**Proposition.** For every \(m\ge0\), (8) is globally real analytic,
\(\mathcal D_8\mathcal O_m=0\), and

\[
\partial_{x_0}\mathcal O_m=\mathcal O_{m+1},\qquad
\partial_t\mathcal O_m=-\mathcal O_{m+2},\qquad
\mathcal O_m(t,q,0)=(G_m,G_{m+2}).
\tag{9}
\]

**Proof.** Right quaternion multiplication by the fixed \(\bar r\)
commutes with \(D_q\), so the first component of (7) vanishes. The
second is
\(2G_{m+3}-\tfrac12\sum_\mu G_{m+3}\bar e_\mu e_\mu=0\).
Associativity is used only inside the quaternion components. Equations
(4)--(5) prove (9), and the original joint entireness gives real
analyticity everywhere. The extension uses \(h_4\) away from \(r=0\)
already for \(m=0\); it does not close a finite four-jet dynamical system.

More generally, any pair of left Fueter-regular quaternion fields
\(A(q),B(q)\) has the extension
\((A-\tfrac12 B_{x_0}\bar r,B)\). Thus this construction adds no
compatibility condition on the initial pair beyond its existing
quaternion regularity. The component derivation is essential; formulas
for products of arbitrary octonion-valued fields cannot be imported from
associative quaternion analysis without checking parentheses. For the
general operator framework see
[Kauhanen and Orelma](https://arxiv.org/abs/1701.08698).

On the physical trace, \(\mathcal O_0=(F,G_2)\) lies in
\(\operatorname{span}_{\mathbb R}\{1,\mathbf j,\ell,\ell\mathbf j\}\),
an associative quaternion subalgebra. Its norm is
\(E+h_2^2+h_3^2\), which can remain positive when \(F=0\).

## 3. Associators that retain collision energy and orientation

For embedded quaternions \(a,b\), (1) immediately yields

\[
[a,b,\ell]=\ell\overline{ab-ba}=-\ell(ab-ba).
\tag{10}
\]

The final equality uses the fact that a quaternion commutator is pure
imaginary. For physical pairs \(a=A+\mathbf jB\), \(b=C+\mathbf jD\)
with real coefficients, quaternion multiplication then gives

\[
\boxed{[a\mathbf i,b\mathbf i,\ell]
=-2\mathbf u(AD-BC),\qquad
[a\mathbf i,b\mathbf k,\ell]=2\mathbf u(AC+BD).}
\tag{11}
\]

For example \(a\mathbf i=A\mathbf i-B\mathbf k\) and
\(b\mathbf k=D\mathbf i+C\mathbf k\); their commutator is
\(-2\mathbf j(AC+BD)\), proving the second identity. Right
multiplication by the fixed units preserves quaternion left regularity.
The added \(\ell\) direction makes these nonzero octonionic
associators, while their values remain determined by the original real
dot products and determinants.

Define the physical observables

\[
\mathcal A_E=[F\mathbf i,F\mathbf k,\ell]=2\mathbf u E,
\tag{12}
\]
\[
\mathcal A_j=[G_j\mathbf i,G_{j+1}\mathbf i,\ell]
=2\mathbf u L_j\quad(j=0,1),
\tag{13}
\]
\[
\mathcal A_t=[F\mathbf i,F_t\mathbf k,\ell]
=\mathbf u E_t.
\tag{14}
\]

In particular \(\mathcal A_E=0\) if and only if \(F=0\). This avoids
the loss of the collision detector in the total doubled norm. At
\(h_1=0\), \(\mathcal A_t=\mathcal A_0\); at \(h_2=0\),
\(\mathcal A_t=\mathcal A_1\).

Let \(\mathcal C_{\mathbf u}=\{s\mathbf u:s\ge0\}\), a specified
oriented ray rather than an order on the octonions. Both stationary signs
are precisely

\[
\mathcal A_t\in\mathcal C_{\mathbf u}
\quad\text{where }h_1h_2=0.
\tag{15}
\]

The sufficient bounded-loss condition is

\[
\boxed{\mathcal A_t+K\mathcal A_E\in\mathcal C_{\mathbf u}
\quad\text{where }h_1h_2=0,}
\tag{16}
\]

with \(K\ge0\) locally bounded through every candidate joint zero.
Indeed its oriented coefficient is \(E_t+2KE\). Norms alone would
replace \(L_j\) by \(|L_j|\) and erase the required orientation.

For comparison, the untwisted associator \([G_0,G_1,\ell]\) vanishes
on the physical slice, but its actual spectral normal derivative satisfies

\[
\left.\partial_{x_1}[G_0,G_1,\ell]\right|_{q=x}
=-2\ell\mathbf i L_1.
\tag{17}
\]

To verify this, differentiate the commutator in (10), use (5), and compute
\([G_1\mathbf i,G_1]+[G_0,G_2\mathbf i]=2\mathbf iL_1\).
This is another geometric realization of the same signed quantity, not
an independent sign restriction.

## 4. The complete source retains the original oscillatory kernel

On the physical slice write \(w_t(u)=e^{tu^2}\Phi(u)\) and
\(v_x(u)=\cos(xu)-\mathbf j u\sin(xu)\). Then

\[
F=\int_0^\infty w_t(u)v_x(u)\,du,\qquad
F_t=\int_0^\infty u^2w_t(u)v_x(u)\,du.
\tag{18}
\]

All integrals and products below converge absolutely on compact real
parameter sets. Trilinearity of the associator, (11), and symmetrization
give

\[
\mathcal A_t=\mathbf u\int_0^\infty\!\int_0^\infty
w_t(u)w_t(v)(u^2+v^2)
\{\cos(xu)\cos(xv)+uv\sin(xu)\sin(xv)\}\,du\,dv.
\tag{19}
\]

Likewise, direct trigonometric expansion gives

\[
L_j=\frac14\int_0^\infty\!\int_0^\infty
(uv)^j w_t(u)w_t(v)
\{(u+v)^2\cos(x(u-v))
+(-1)^j(u-v)^2\cos(x(u+v))\}\,du\,dv.
\tag{20}
\]

Equations (19)--(20) retain every source cross term. The octonionic
identities do not turn these oscillatory kernels into positive kernels.
Replacing the full source by diagonal theta indices or taking absolute
values before the cancellations would change the target.

## 5. Collision controls and a structural limitation

The even backward-heat polynomial \(H(t,z)=z^2-2(t-T)\), for any
\(T>0\), has a double collision at \((T,0)\). At that point
\(F=0\), \(G_2=2\), \(G_3=0\), so the full extension has
\(\mathcal O_0=2\ell\), while \(\mathcal A_E=0\).
On its stationary predecessor \(x=0,t=T-\delta\),

\[
E=4\delta^2,\qquad L_0=-4\delta,\qquad
\mathcal A_t=-8\delta\mathbf u.
\tag{21}
\]

Any coefficient in (16) must satisfy \(K\ge1/\delta\), violating
local boundedness at the collision. The cubic control
\(H=z^3-6(t-T)z\) similarly has, at \(x=0,t=T-\delta\),
\(h_2=0\), \(E=36\delta^2\), \(L_1=-36\delta\), and the same
necessary divergence. These controls satisfy the lift and all associator
identities exactly.

The obstruction persists with a strictly positive, even, entire source
with superexponential decay. Let

\[
\rho(v)=\frac{2e^{-v^4}}{\Gamma(1/4)},\qquad
\rho_\varepsilon(v)=\varepsilon^{-1}\rho(v/\varepsilon),
\]
\[
\Phi_\varepsilon(u)=
2\{\rho_\varepsilon(u-1)+\rho_\varepsilon(u+1)\}
+\{\rho_\varepsilon(u-2)+\rho_\varepsilon(u+2)\},
\qquad\varepsilon>0.
\tag{22}
\]

Its half-line mass is 3. The heat cosine transform equals

\[
H_\varepsilon(t,z)=
2\int_{\mathbb R}\rho(v)e^{t(1+\varepsilon v)^2}
\cos(z(1+\varepsilon v))\,dv
+\int_{\mathbb R}\rho(v)e^{t(2+\varepsilon v)^2}
\cos(z(2+\varepsilon v))\,dv.
\tag{23}
\]

Quartic decay dominates the compact-parameter quadratic and linear
exponents, so (23) is jointly entire in \((t,z,\varepsilon)\), including
\(\varepsilon=0\), and satisfies backward heat. At zero it is
\(2e^t\cos z+e^{4t}\cos2z\), with a real double collision at
\(T_0=\log2/3,x_0=\pi\). There \(H_{xx}=-6e^{T_0}\ne0\), and
the Jacobian of \((H,H_x)\) with respect to \((t,x)\) has determinant
\(-H_{xx}^2\ne0\). The real analytic implicit-function theorem gives
nearby real positive-time double collisions for every sufficiently small
\(\varepsilon>0\). Since (23) is even in \(\varepsilon\), their locations
differ from \((T_0,\pi)\) by \(O(\varepsilon^2)\).

For positive \(\varepsilon\), (22) is strictly positive on the real
line, even, entire in \(u\), and has quartic superexponential real-axis
decay. Thus positivity, evenness, joint heat entireness, full octonionic
monogenic extension, and the associator identities together do not force
collision exclusion. The theta-specific modular and arithmetic structure
must enter a further estimate. This is an analytic existence control;
no numerical value of a sufficient \(\varepsilon\) is asserted.

## 6. A focused source estimate to pursue

Choose an explicit real centering function \(\lambda(t,x)\ge0\), and
retain the complete quaternionic heat residual

\[
R_\lambda=F_t-\lambda F
=\int_0^\infty(u^2-\lambda)w_t(u)v_x(u)\,du.
\tag{24}
\]

By (11)--(14),

\[
\mathcal A_t=\lambda\mathcal A_E
+[F\mathbf i,R_\lambda\mathbf k,\ell],\qquad
E_t=2\lambda E+2\operatorname{Re}(\bar F R_\lambda).
\tag{25}
\]

A **proposed sufficient theta lemma**, still unproved, is

\[
\operatorname{Re}(\bar F R_\lambda)\ge-B(t,x)E
\quad\text{on }h_1h_2=0,
\tag{26}
\]

where \(B\ge0\) is prescribed independently of an unknown norm and
\(K=\max(0,B-\lambda)\) is locally bounded through every candidate
collision. This proves (16). The stronger bound
\(|R_\lambda|^2\le B^2E\) also suffices, but (26) needs control only
of the negative radial component; phase motion need not be bounded in
absolute value. All formulations avoid division by \(F\) at its possible
zeros.

Centering alone is algebraically equivalent to the original radial-energy
loss inequality. It helps only if the theta source permits a new estimate
of the signed residual in (26); no such estimate is established here.

The original normalized oscillator proposal is compatible with this
algebra: for \(\Psi=e^{\pi x/8}F\) and
\(\mathscr R=(\partial_x^2+\omega^2)\Psi\), with real
\(\omega(t,x)\), the difference
\([\Psi\mathbf i,\Psi\mathbf k,\ell]B^2
-[\mathscr R\mathbf i,\mathscr R\mathbf k,\ell]\) lies in
\(\mathcal C_{\mathbf u}\) exactly when
\(|\mathscr R|^2\le B^2|\Psi|^2\). This is a possible stronger witness,
not an additional consequence of octonionic regularity.

The next analytic calculation should derive (24) from the complete-source
shifted contour or a shared paired arithmetic expansion, choose
\(\lambda\) from its actual principal heat growth, and estimate the
signed pairing in (26) before taking absolute values. Every retained
cross term and derivative remainder must remain. A possible collision
still requires coverage of the padded region
\(0<t\le1/2,\ |x|>100,\ t\log|x|<C'\), with \(C'>C\); an estimate
only at fixed positive time or only at sample points is insufficient.
No choice \(B=|R_\lambda|/|F|\) establishes the needed boundedness.

## 7. Validation and working files

The standard-library exact checker
[check_octonion_jet_identities.py](../numerics/check_octonion_jet_identities.py)
and its small
[execution record](../numerics/OCTONION_JET_IDENTITY_CHECKS_20261014.json)
check the declared multiplication, norm composition, physical subalgebra,
signed and energy associators, transverse derivative, differential lift,
and polynomial collision controls. Replay from the numerics directory:

```sh
python3 check_octonion_jet_identities.py --output /tmp/inv21-octonion-replay.json
```

The [internal review](../reviews/10_OCTONIONIC_LIFT_AND_ASSOCIATOR_INTERNAL_REVIEW_20261014.md)
assesses the derivation and replays the checker. Exact algebra checks do
not establish (26), a new theta numerical certificate, or an RH proof.
The positive-source perturbation argument is justified analytically in
Section 5, not by finite sampling. The current manuscript and existing
finite-height certificate records are unchanged.
