# Positive endpoint: currents, time derivatives and actual covariance

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from chat 0007's session metadata. Thread
`01a17067-eabc-7872-abc9-d9319b53bc41`.

**Status: proved in-note; same-assistant review only.** This continues
[Note 30][saddle] and supplies its missing positive evolution comparison.
The same implicit gamma saddle, physical regulator and fixed spatial
average give current, density-time, potential-time, forcing/source and
actual covariance errors `O(t^-1/2)`, uniformly over all real heights at
sufficiently large positive time. Spatial derivatives needed by the
adaptive equations are included. Both curvature derivatives and the
model's nonzero heat residual remain in those equations.

A second result covers every fixed compact time interval `[32,T]`,
including the flat regulator switch at 64. The outer current and actual
covariance errors are `O_T(log^2 X/X^2)`; the time-dependent terms have
the weaker but vanishing error `O_T(log^2 X/X)`. The switch derivative
is paid, rather than assumed bounded uniformly in height.

This completes the stated eventual endpoint comparison in HDA-16 and
the stated outer-model comparison in HDA-19. It does not construct an
all-time approximation: HDA-17's informative finite input and HDA-18's
joining theorem remain. Onsets and constants are not numerically
instantiated. [Review 13][review] is a same-assistant analytical rereading,
not HDA-20's distinct-reviewer audit. No numerical or machine-symbolic
execution, manuscript integration or new snapshot was performed.

Read the [result index][results], [heat-flow results][geometry],
[collision controls][controls] and [avoid index][avoid], especially
[classification][a01], [scope][a07] and [separate bounds][a12]. This is
an approximation milestone, with no RH or simplicity conclusion.

## 1. Physical contract and the comparison theorem

Retain the canonical source and `H_t=-H_zz` from Note 30 FS1, with
`H(0,z)=xi((1+iz)/2)/8`. Write `P=P_*` for FS3--FS4:

\[
\mathcal M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\quad
\alpha=\mathcal M'/\mathcal M,\quad
p=w+\frac t2\alpha(p),\quad B=1-\frac t2\alpha'(p),
\]
\[
\mathcal S_t(w)=\mathcal M(p)e^{-(p-w)^2/t}B^{-1/2},\qquad
P(t,z)=\mathcal S_t((1+iz)/2)+\mathcal S_t((1-iz)/2).
\tag{PE1}
\]

Use exactly the large right-half-plane branch and square root near 1
proved there, on the full buffered strip. This is not a claim of an
entire continuation through every saddle branch. Set

\[
X=|x|,\quad \mathcal L=\log(2+t+X),\quad N=1+X+t\mathcal L,
\quad e=\frac{t^{3/2}}{N^2},\quad d=\frac t{N^3},\quad A=e\mathcal L^2.
\tag{PE2}
\]

Here `A` is an error allowance, not the analytic carrier. Throughout,
`q=epsilon_g^2`, `r=log q` are the unchanged regulator of [Note 20][global].
Fix `ell,h>0`, an observation strip `|y|<=Y`, and
`K=k_ell k_h`, with `k(v)=(315/256)(1-v^2)^4 1_{|v|<=1}`.
All estimates use the full support and a fixed enlargement of
`|Re z-x|<=ell+2`, `|Im z|<=Y+h+2`. Every intersecting zero collar
and its larger analytic disk are included. Constants may depend on
these fixed data, but not on real x or sufficiently large t.
There is no moving filter, time average or mass normalization.

For `F=H,P`, retain the actual observables

\[
D_F=|F|^2+q,\quad S_F=\log D_F,\quad w_F=q/D_F,\quad
\rho_F=\frac{q|F_z|^2}{\pi D_F^2},\quad
j_F=\frac{qF_{zz}\overline{F_z}}{\pi D_F^2},
\tag{PE3}
\]
\[
U_F=K*S_F,\quad W_F=K*w_F,\quad R_F=K*\rho_F,\quad J_F=K*j_F,
\]
\[
Q_F=K*((S_F)_x^2-(S_F)_y^2)-((U_F)_x^2-(U_F)_y^2).
\tag{PE4}
\]

The vector current is `(Re j,Im j)`. Let `square=partial_x^2-partial_y^2`
and define, as in [Note 14][adaptive],

\[
b=r_t+\tfrac12(r_{xx}+r_x^2),\quad \mathcal B_F=bw_F,
\quad C_F=\Delta S_F/(4\pi)-\rho_F,
\]
\[
\mathcal S_F=(1-2w_F)(r_t\rho_F+\nabla r\cdot\mathbf j_F).
\tag{PE5}
\]

Bars on these last quantities mean convolution with K. They are the
actual regulator forcing, curvature correction and signed current
source; no product of filtered means replaces a correlation.

**Positive endpoint theorem.** There are `T_*,C`, with `T_*>=128`,
such that for every `t>=T_*`, real x and `|y|<=Y`, the following
absolute differences between H and P have the indicated bounds:

| Quantity | Spatial derivatives included | Error |
| --- | --- | --- |
| U, W | every multi-index of order at most 4 | C e |
| R, averaged C | every order at most 2 | C e |
| J, actual Q | every order at most 2, in particular Delta Q | C A |
| U_t, W_t, R_t, averaged C_t | every order at most 2 | C A |
| averaged B, actual averaged source S | every order at most 2 | C A |

\[
\sup_{x\in\mathbb R,\ |y|\le Y}\{\text{each error in the last three rows}\}
\le C t^{-1/2}.
\tag{PE6}
\]

Indeed `N>=t mathcal L`, so `A<=t^-1/2` exactly. The static rows
retain `C/(sqrt(t) log^2(2+t))`. These are absolute comparisons, including
where an observable vanishes, not relative errors or an assertion that
the covariance has either sign. The model equation defects specified
in Section 8 are separately bounded by `C d`, hence by
`C/[t^2 log^3(2+t)]`. No error is propagated from that residual.

## 2. Derivative input and root motion from the complete field estimate

Write
`C_t(z)=|mathcal S_t((1+iz)/2)|+|mathcal S_t((1-iz)/2)|`
for the carrier sum in this section only. Note 30 FS7 and FS33--FS34
give, on an enlarged analytic buffer,

\[
|H-P|\le Ce\,C_t(z),\qquad
\mathcal E:=(\partial_t+\partial_{zz})P,\qquad
|\mathcal E|\le Cd\,C_t(z).
\tag{PE7}
\]

Both reflected arms, all arithmetic modes, the middle, connectors and
infinite ends have already been paid in that field estimate. Nothing
is truncated further here. The exact retained residual is

\[
\mathcal E=-\sum_{w=(1\pm iz)/2}\mathcal S_t(w)
\left\{\frac{t\alpha'''(p_t(w))}{16B^3}
 +\frac{5t^2(\alpha''(p_t(w)))^2}{64B^4}\right\}.
\tag{PE8}
\]

The logarithmic derivatives of each carrier are `O(mathcal L)`.
Consequently its modulus changes by a bounded factor on disks of radius
`c/mathcal L`. Apply Cauchy's derivative formula on those disks to the
**holomorphic difference in PE7**, keeping its complete bound on the
circle. For fixed `j<=3`,

\[
|\partial_z^j(H-P)|\le C_j e\mathcal L^j C_t(z),\qquad
|\partial_z^jF|\le C_j\mathcal L^j C_t(z),\quad F=H,P.
\tag{PE9}
\]

This is an analytic derivative estimate on a full disk, not
differentiation of a real-axis asymptotic error. The derivative-transfer
input is [Cauchy's formula, DLMF 1.9.31][cauchy]; its contour
hypotheses are supplied by FS7's holomorphic buffer. Time derivatives
below use the exact equations `H_t=-H_zz`, `P_t=-P_zz+mathcal E`.

Let `omega=Theta_{*,x}(t,x) asymp mathcal L`. The collars from FS22
have radii comparable to `1/omega`, O(omega) population on a fixed
horizontal support, and one real simple root of each field. Denote
paired roots by a for H and c for P. Choose their concentric analytic
buffers a fixed factor larger, still disjoint. Then

\[
|a-c|\le Ce/\omega,\quad
|F_z(\text{its root})|\ge c_1 A_X\omega,
\quad v_F:=\frac{F_{zz}(\text{its root})}{F_z(\text{its root})},
\]
\[
|v_H|+|v_P|\le C,\qquad |v_H-v_P|\le Ce\omega.
\tag{PE10}
\]

To check the bounded residue, write `P=2 mathcal A_* cos Theta_*`.
At a P root,
`v_P=2(mathcal A_*)_z/mathcal A_*+Theta_{*,zz}/Theta_{*,z}=O(1)`
by FS22. Compare H's first and second derivatives at a with P's at c
using PE9 and the third-derivative bound along the displacement segment.
The second-derivative error divided by the slope is `O(e omega)`;
the first-derivative relative error is O(e). Enlarge the onset so
`e omega<1`. This proves PE10 rather than assuming bounded velocities.

Implicit differentiation at a simple root now gives the actual motion:

\[
a'=v_H,\qquad c'=v_P-\frac{\mathcal E(t,c)}{P_z(t,c)},\qquad
|a'-c'|\le C(e\omega+d/\omega).
\tag{PE11}
\]

The algebraic residue `v_P` is not exactly the model root velocity.
Their difference is retained. These local tracks exist on a common
time neighborhood of each observation; no integer population cutoff
or static root-position allowance is differentiated.

On the complement of the collars,
`|P|>=c C_t(z)` and `|H|>=c C_t(z)`. The stronger carrier-sum floor
follows directly from `|cos Theta|/cosh(Im Theta)` outside fixed
phase disks; FS22 changes those disks into the physical collars.
It avoids an exponential loss across the transverse buffer.

Inside a larger collar put

\[
h_F=F_{zz}/F=\frac{v_F}{z-\text{root}_F}+g_F(z).
\]
\[
|g_F|\le C\omega^2,\qquad |g_H-g_P|\le Ce\omega^2.
\tag{PE12}
\]

Both g's are analytic. On the collar boundary PE9 and the field floor
bound `h_H-h_P` by `Ce omega^2`. Subtract the two pole terms, using
PE10 and `|a-c|<=Ce/omega`; the same bound holds for the g difference
on the boundary. The maximum principle proves PE12 inside. The
individual bound is obtained in the same way. This step is the needed
pole/regular-part separation; h_F itself is not bounded at a root.

## 3. A regularized-pole comparison with no regulator floor

For `m=0,1,2` define the smooth quantities

\[
V_{m,F}=w_F^m(1-w_F)h_F
       =w_F^m\frac{F_{zz}\overline F}{D_F},\qquad
Z_m=w_P^m\frac{\mathcal E\overline P}{D_P}.
\tag{PE13}
\]

The fractions on the right specify the values at zeros. For every
positive q, however small or spatially variable, the full support obeys

\[
\boxed{\|V_{m,H}-V_{m,P}\|_{L^1}\le Ce\mathcal L^2,
\qquad \|Z_m\|_{L^1}\le Cd.}
\tag{PE14}
\]

Here and below L1 uses planar area. The potential and weight comparison
from Note 28 JT14, applied with Note 30's collars, is also retained:

\[
\|S_H-S_P\|_{L^1}+\|w_H-w_P\|_{L^1}\le Ce.
\tag{PE15}
\]

**Proof of the new pole estimate.** On a scaled collar, with
`u=omega(z-c)`, write
`P/A_X=u B(u)` and `H/A_X=(u-e_0)C(u)`. The units are bounded above
and below, `|B-C|<=Ce`, and `|e_0|<=Ce`. These bounds hold on the
larger disk by the analytic-unit argument of JT13.
For `f=(u-a)b(u)` and `Q(u)=q/A_X^2>0`, put

\[
\mathcal P_m[f](u)=\frac1{u-a}
\left(\frac{Q}{|f|^2+Q}\right)^m
\frac{|f|^2}{|f|^2+Q}.
\tag{PE16}
\]

Uniformly in the positive function Q,

\[
\int|\mathcal P_m[(u-e_0)C]-\mathcal P_m[uB]|\,dA_u
\le Ce(1+|\log e|).
\tag{PE17}
\]

To prove it, remove disks of radius `C_2 e` about both centers. Their
contribution is O(e), since each pole is bounded by `1/|u-a|`.
On the complement interpolate the root along its segment and the unit
by `B exp(s log(C/B))`; the unit logarithm is O(e) and remains bounded.
Q is held fixed pointwise, so no derivative of Q occurs. The weight
`w^m(1-w)` and its derivative with respect to `log|f|` are bounded by
constants depending only on m. Differentiating the interpolated pole
therefore costs at most
`C e(|u-a_s|^-2+|u-a_s|^-1)`. Radial integration from `C_2 e` to the
fixed collar radius proves PE17. Constants may be enlarged to cover
the harmless case when the excluded disks overlap. This establishes
a uniform modulus of continuity; a regulator-dependent logarithm
has not been hidden in the constant.

Restore physical area and sum the O(omega) collars. The pole translation
cost is `Ce(1+|log e|)`, and the residue difference costs `Ce omega`,
because the total L1 norm of the unweighted simple-pole kernels is O(1).
The regular parts in PE12 cost `Ce omega^2`: their differences have that
bound, and multiplying a regular part by a changed weight costs the
same bound using PE15 and the Lipschitz dependence of `w^m(1-w)` on w.
On the complement, PE9 and the relative field floor give the same
`Ce mathcal L^2` bound directly. Finally
`1+|log e|<=C mathcal L`, since `N<=C(2+t+X)log(2+t+X)` and t>=32.
This proves the first half of PE14.

For the second half, `mathcal E/P` has residue at most `Cd/omega`
at a P root and an analytic regular part bounded by Cd. The boundary
estimate follows from PE7 and the carrier-sum floor, then the maximum
principle applies as in PE12. Multiplication by `w^m(1-w)` removes
the pole at the root, and its L1 norm is bounded by that of the pole.
The full collar sum and the exterior give Cd. No derivative of the
residual or reciprocal power of the regulator is required.

## 4. Pay the physical regulator coefficients on the whole height axis

At late time the exact regulator has

\[
r=2\log M_0-2\log\kappa-x^2/\kappa,\qquad
r_x=-2x/\kappa,\quad r_{xx}=-2/\kappa,
\]
\[
r_t=2L^2-3\kappa'/\kappa+x^2\kappa'/\kappa^2,
\quad r_{xt}=2x\kappa'/\kappa^2,\quad
r_{xxt}=2\kappa'/\kappa^2,
\tag{PE18}
\]
\[
4\pi e^{4L}=2tL+9,\quad \kappa=8tL-2t+36,\quad
\kappa'=8L+16tL/\kappa-2=O(L).
\]

The physical mass M_0 is Note 30's source saddle mass, distinct from
the gamma factor in PE1. Its derivative follows from stationarity:
`(log M_0)'=L^2-kappa'/(2kappa)`. Thus PE18 does not differentiate
an asymptotic mass estimate.

Choose a sufficiently large fixed B0 as in FS27. On `X/kappa<=B0`,
all required spatial coefficients `grad r, Delta r, grad r_t, Delta r_t`
are bounded on the fixed buffer, and

\[
|r_t|+|b|\le C\mathcal L^2.
\tag{PE19}
\]

PE14--PE15 can therefore be multiplied by these coefficients directly.
In the complementary region use the separately proved FS26 mass anchor
and FS27, not an independent bound on the large log M_0. They give

\[
\lambda=\frac{\sup_{|u-x|\le\ell+2}\epsilon_g(t,u)}{A_X}
\le Ce^{-cX},\qquad |\log\lambda|\le C(1+X^2).
\tag{PE20}
\]

Here `t<=C(1+X)` and `mathcal L<=C log(2+X)`. The regulator
coefficients in PE18 and their required products have polynomial
growth in X. On each collar put `a_e=C lambda/omega` and use
`w_F<=a_e^2/(|z-root_F|^2+a_e^2)`. The exterior has `w_F<=C lambda^2`.
Elementary radial integrals then give

\[
\int w_F\le C\lambda^2\left[1+\frac{1+|\log\lambda|}{\omega}\right],
\]
\[
\int |w_F h_F|\le C\left\{
\omega^2\lambda^2\left[1+\frac{1+|\log\lambda|}{\omega}\right]
+\lambda\right\}.
\tag{PE21}
\]

For the pole term use
`int w/|z-a| <= C a_e` on each disk and PE10's bounded residue.
The regular term uses PE12. For `w_P mathcal E/P` the corresponding
allowance is bounded by `C d` times the bracket in PE21 with the
regular coefficient omega^2 replaced by 1 and the pole coefficient
lambda replaced by lambda/omega. The formulas also bound every
additional factor w and `(1-w)` in absolute value.

Thus every polynomially weighted L1 term involving w, `w h_F` or
`w_P mathcal E/P` that is used below is exponentially small in this
region (with an additional factor d in the residual case). These
exponentials can be absorbed into e or A: here
`N<=C(1+X)log(2+X)` and t has an eventual positive lower bound.
The estimates do not declare the density a zero measure when the
regulator is unresolved.

## 5. Direct time derivatives, current and differentiated curvature

Define `chi_F=w_F(1-w_F)`. Set `Z_m=0` for the exact H field and
use PE13 for P. Direct differentiation of PE3 using the respective
field equation gives the identities

\[
(S_F)_t=-2\Re V_{0,F}+r_t w_F+2\Re Z_0,
\]
\[
(w_F)_t=r_t\chi_F+2\Re V_{1,F}-2\Re Z_1,
\]
\[
(\chi_F)_t=r_t\chi_F(1-2w_F)
 +2\Re(V_{1,F}-2V_{2,F})-2\Re(Z_1-2Z_2).
\tag{PE22}
\]

All expressions are smooth at the zeros. PE14--PE21 prove

\[
\|\delta S_t\|_{L^1}+\|\delta w_t\|_{L^1}
+\|\delta\chi_t\|_{L^1}\le CA,
\tag{PE23}
\]

where delta means H minus P. This includes the large physical amplitude
derivative `2L^2`, both root-motion poles and the model residual.
Moving up to two spatial derivatives onto K proves the potential-time
and filtered-weight-time rows of PE6.

For any holomorphic F the exact current identity is

\[
\boxed{\pi j_F=\partial_{\bar z}V_{0,F}
                 +(\partial_{\bar z}r)V_{1,F},\qquad
\partial_{\bar z}=(\partial_x+i\partial_y)/2.}
\tag{PE24}
\]

Indeed `partial_bar h_F` vanishes off the roots, and
`partial_bar(1-w)=-w(1-w)partial_bar r+qF conjugate(F_z)/D_F^2`.
The right side is smooth by PE13, so the identity extends across the
roots with no omitted point mass. Equivalently, direct differentiation
of `F_zz conjugate(F)/D_F` proves it without distributions.
Pairing with a test and integrating its first term by parts now yields
`|partial^gamma(J_H-J_P)|<=CA` for `|gamma|<=2`.
The r coefficient is bounded in PE19's regime and paid by PE21 in
the complementary regime. This avoids dividing by F_z at stationary
points between roots.

Use the exact weak density identity, with a fixed compactly supported
test psi,

\[
4\pi\langle\rho_F,\psi\rangle
=\int S_F\Delta\psi+2\int w_F\nabla r\cdot\nabla\psi
+\int\{w_F\Delta r+\chi_F|\nabla r|^2\}\psi.
\tag{PE25}
\]

Differentiate this identity itself at fixed physical coordinates:

\[
\begin{split}
4\pi\langle(\rho_F)_t,\psi\rangle={}&\int (S_F)_t\Delta\psi
+2\int\{(w_F)_t\nabla r+w_F\nabla r_t\}\cdot\nabla\psi\\
&+\int\{(w_F)_t\Delta r+w_F\Delta r_t
+(\chi_F)_t|\nabla r|^2
+2\chi_F\nabla r\cdot\nabla r_t\}\psi.
\end{split}
\tag{PE26}
\]

For each finite t,x the regulator is positive on the compact support,
so this differentiation is legitimate by ordinary smoothness.
Uniform bounds then follow from PE23 in the bounded-coefficient regime
and the individual PE21 bounds in the other regime. In particular,
with `||psi||_(2)` denoting the sum of sup norms through order two,

\[
|\langle\delta\rho_t,\psi\rangle|\le CA\|\psi\|_{(2)}.
\tag{PE27}
\]

Use `psi=partial^gamma K`, `|gamma|<=2`, to obtain the density-time
row. The same reasoning in PE25, without time differentiation, extends
FS6 to spatial derivatives of R through order two at error Ce.
Subtracting rho from `Delta S/(4pi)`, or directly using the remaining
terms of PE25, gives averaged C and its spatial derivatives through
order two at error Ce, and their time derivatives at error CA.
Thus both `partial_t averaged C` and `square averaged C` are paid.

The kernel is C3 with bounded weak derivatives through order four;
there is no boundary delta in those derivatives. The pairings above
extend to these tests by smoothing or weak integration by parts. No
fifth kernel derivative is used: PE26 needs at most two test derivatives
on top of `|gamma|<=2`. This is why the derivative orders in PE6 are
specified rather than left implicit.

Finally `overline B_F=K*(b w_F)`. PE19 times PE15, and PE21 on the
other region, give its error CA through two spatial derivatives,
including the required `Delta overline B`.

## 6. Compare the actual signed covariance before taking absolute values

Put `G_F=(S_F)_x^2-(S_F)_y^2`. The elementary identities
`square |F|^2=4 Re(F_zz conjugate(F))` and
`square log D+(log D)_x^2-(log D)_y^2=(square D)/D` give

\[
\boxed{G_F=4\Re V_{0,F}-\square S_F+(r_{xx}+r_x^2)w_F.}
\tag{PE28}
\]

This is a **spatial identity for the actual squared gradients** of
each given field. It uses no heat equation, chosen covariance, time
residual or closure assumption. It retains the angular cancellation
of the simple-pole square. Bounding the two positive gradient squares
separately would introduce a regulator-dependent logarithm.

PE14, PE15 and the two regulator regimes give, for `|gamma|<=2`,

\[
|\partial^\gamma K*(G_H-G_P)|\le CA.
\tag{PE29}
\]

The term involving square S moves two further derivatives onto K,
so the maximum kernel order is again four. To pay the subtraction of
the squared filtered gradients, observe that

\[
\|\nabla S_F\|_{L^1(\Omega)}\le C\mathcal L,
\qquad |\partial^\gamma U_F|\le C\mathcal L\quad(1\le|\gamma|\le3).
\tag{PE30}
\]

For the first claim use
`grad S=(2 Re L_F,-2 Im L_F)+w grad r`, where
`L_F=F_z conjugate(F)/D_F`. Outside the collars `|F_z/F|<=C omega`.
Inside, `F_z/F=1/(z-root)+b_F'/b_F`, with the analytic-unit derivative
bounded by C omega on the smaller disks. The simple pole is integrable;
their total L1 contribution is O(1). The regulator term is bounded in
PE19's regime and exponentially small by PE21 in the other. Transfer
the remaining derivatives to K to get the second claim.

PE30 and the static derivative differences `Ce` imply

\[
|\partial^\gamma\{(U_H)_x^2-(U_H)_y^2
                  -(U_P)_x^2+(U_P)_y^2\}|\le Ce\mathcal L,
\quad |\gamma|\le2.
\tag{PE31}
\]

Subtract PE31 from PE29. This proves

\[
\boxed{|\partial^\gamma(Q_H-Q_P)|\le CA\quad(|\gamma|\le2),
\quad |Q_H-Q_P|+|\Delta Q_H-\Delta Q_P|\le CA.}
\tag{PE32}
\]

Thus Q is the covariance in PE4 throughout the proof. PE28 is a way
to estimate its existing signed integrand; Q has not been defined to
make a density equation hold. The physical additive potential is
retained, and PE15 supplies its source-derived normalization.

## 7. The signed current source and the residual density correction

For a general holomorphic F satisfying `F_t=-F_zz+E_F`, direct
differentiation gives

\[
(\rho_F)_t+\operatorname{div}\mathbf j_F
=\mathcal S_F+\mathcal D_{E_F},
\]
\[
\mathcal D_{E_F}
=\frac{2q\Re((E_F)_z\overline{F_z})}{\pi D_F^2}
 -4\rho_F\Re\frac{E_F\overline F}{D_F}.
\tag{PE33}
\]

H has `E_H=0`; P has `E_P=mathcal E`. A pointwise bound on PE33
is not used at narrow peaks. Vary PE25 with `delta F=E_F`, holding
q fixed, to obtain its equivalent weak expression. For P it is

\[
\begin{split}
4\pi\langle\mathcal D_{\mathcal E},\psi\rangle={}&
2\Re\int Z_0\Delta\psi-4\Re\int Z_1\nabla r\cdot\nabla\psi\\
&-2\Re\int\{Z_1\Delta r+(Z_1-2Z_2)|\nabla r|^2\}\psi.
\end{split}
\tag{PE34}
\]

PE14 in the bounded-coefficient regime and the residual version of
PE21 elsewhere prove

\[
|\langle\mathcal D_{\mathcal E},\psi\rangle|
\le Cd\|\psi\|_{(2)}.
\tag{PE35}
\]

Now use PE33 for the already defined sources in PE5. The independent
current, density-time and residual estimates give

\[
|\partial^\gamma K*(\mathcal S_H-\mathcal S_P)|\le CA,
\quad |\gamma|\le2.
\tag{PE36}
\]

For the divergence term use PE24 with the differentiated test; the
maximum total derivative order is `|gamma|+2<=4`. This estimates the
actual signed source through its exact identity, without replacing it
by products of means or asserting a small integral of its absolute
value. The distinction matters already for a linear zero and constant
spatial q, as recorded in Note 16 AT23.

## 8. Complete model equations, traces and inner differentiated overlap

For P the exact fixed-filter equations are

\[
(U_P)_t=-\tfrac12\{\square U_P+(U_P)_x^2-(U_P)_y^2+Q_P\}
 +\overline{\mathcal B}_P+2\Re K*Z_0,
\qquad \Delta U_P=4\pi(R_P+\overline C_P),
\tag{PE37}
\]
\[
\begin{split}
(R_P)_t={}&-\tfrac12\square R_P
-\frac1{8\pi}\Delta\{(U_P)_x^2-(U_P)_y^2+Q_P\}
+\frac1{4\pi}\Delta\overline{\mathcal B}_P\\
&-\partial_t\overline C_P-\tfrac12\square\overline C_P
+\frac1{2\pi}\Delta\Re K*Z_0,
\end{split}
\tag{PE38}
\]
\[
(R_P)_t+\operatorname{div}\mathbf J_P
=\overline{\mathcal S}_P+K*\mathcal D_{\mathcal E}.
\tag{PE39}
\]

H obeys the corresponding formulas with the two residual corrections
zero. PE14 and PE35 bound each displayed model correction by Cd,
including spatial derivatives through order two where used. The
comparison theorem pays every term of the investigation's P3a--P5a.
It does not claim that P is an exact heat solution or derive solution
closeness from small equation defects: closeness comes from PE7 and
the proved nonlinear transfers.

U, its normal spatial derivative and the normal current on any
observation boundary within the full buffered domain inherit these
bounds. No harmonic datum, fitted mass or unknown theta root is added
to the model. A moving observation boundary would require its own
transport identity; none is included silently.

On [Note 19][inner]'s buffered window `|x|<=X_in(t) asymp kappa^(1/3)`,
both comparisons use the same physical q. Let `R_L,J_L` denote its
explicit finite-phase clock observables, with the existing source/collar
gates. The triangle inequality now gives, in addition to FS31,

\[
\|J_P-J_L\|_{\rm inner}
+\|(R_P)_t-(R_L)_t\|_{\rm inner}
\le C t^{-1/2}+C L\kappa^{-7/6}=O(t^{-1/2}).
\tag{PE40}
\]

This is an actual differentiated overlap, coarser than the inner theorem
but tending to zero absolutely. The global rate need not be smaller than
the inner transport scale L/kappa; Notes 16/19 retain the sharper inner
information. It does not assert a potential/covariance
theorem for an inner clock that has not supplied those observables.
At late time P itself covers the whole height axis, so no spatial splice
with that clock is necessary for the positive endpoint.

## 9. Compact-time outer evolution, including the flat switch

The field, collar and pole estimates PE7--PE17 hold for t>=32 and
sufficiently large `t+X`, as in Note 30. Fix a finite T>=32 and let
`32<=t<=T`, `X>=X_T`, with all fixed buffers. Then
`e=O_T(X^-2)`, `d=O_T(X^-3)`, `omega asymp log X` uniformly.
Write the exact global regulator as

\[
r(t,x)=a(t)-\beta(t)x^2,\qquad
\beta=0\ (t\le64),\qquad \beta=\chi(t)/\kappa(t)\ (t>64),
\tag{PE41}
\]

where a is smooth and chi is exactly the switch in Note 20 FB2.
All derivatives of a and beta needed here are bounded on `[32,T]`.
This fact alone would not give a decreasing time-error bound, since
`r_t=a'-beta' x^2`. The flat switch supplies the stronger estimate

\[
|\beta'|\le C_T\beta\{1+\log_+^2(1/\beta)\}\quad(\beta>0),
\qquad \beta'=0\quad(\beta=0).
\tag{PE42}
\]

For completeness, put `v=(t-64)/64`. Then
`chi'=chi(1-chi)[v^-2+(1-v)^-2]/64`.
Near v=0, `log(1/chi)=v^-1+O(1)` and kappa is bounded above and
below. This proves PE42 there. On the remaining compact interval beta
has a positive lower bound, so smoothness proves it after increasing
`C_T`; near 128 the other flat endpoint is harmless. If T<=64 both
sides vanish. No finite switch-layer center is replaced by a leading
asymptotic approximation.

On `beta X<=B0`, monotonicity of
`u(1+log^2(1/u))` for `0<u<=1` gives, for large X,

\[
|\beta'|\le C_T\frac{1+\log^2 X}{X},\quad
|r_t|\le C_T X\log^2 X,\quad
|\nabla r_t|\le C_T\log^2 X.
\tag{PE43}
\]

The harmless case beta=0 has bounded r_t and is included.
Spatial coefficients `grad r,Delta r` remain bounded. Thus PE22--PE27
cost `O_T(log^2 X/X)` here, rather than a nonvanishing estimate from
the crude bound on beta'. On `beta X>B0`, FS27--FS28's compact-time
argument gives `lambda<=C_T exp(-cX)` after choosing B0 sufficiently
large. All time/spatial regulator coefficients grow only polynomially
in X on the fixed slab, so PE21 pays them. The residual corrections
remain `O_T(X^-3)`.

Consequently the compact-time outer theorem is:

| Quantities, with the derivative orders of PE6 | Uniform error on `[32,T]`, `X>=X_T` |
| --- | --- |
| U, W, R, averaged C | `C_T X^-2` |
| J and actual Q, including Delta Q | `C_T log^2 X/X^2` |
| U_t, W_t, R_t, averaged C_t, averaged B and actual source S | `C_T log^2 X/X` |
| The retained model equation corrections | `C_T X^-3` |

**(PE44)** Constants may depend on T; this is
not an unquantified exchange of the compact-time and late-time limits.
Together PE6 and PE44 supply both endpoint and compact positive-time
outer evolution. Before the spatial regulator switch, Note 25's
separate fixed-floor tails remain available. A finite-height core is
still required for an all-time assembly.

## 10. Checks, scope and the next analytical consumer

The hand derivation was checked against two elementary local fields.
For `F=z`, PE24 gives j=0 and, at spatially constant q, PE28 reads
`S_x^2-S_y^2=-square S`, preserving the singular angular cancellation.
For `F=z-a(t)` with spatially constant q, `F_zz=0` but
`E_F=-a'`. PE11 gives its actual root velocity, PE22 gives
`S_t=r_t w-2 Re(a' conjugate(F)/D)`, and PE33 supplies the translated
density through its residual term. This checks why the model root
velocity cannot silently replace the algebraic current residue.
These are written algebraic checks, not machine verification or a
theta validation campaign.

The source-specific premises remain Note 30's unchanged canonical
completion, full reflection and ordinary Dirichlet coefficients.
Euler-factor controls alter the completion; weighted-square/finite-tail
controls lack those unchanged coefficients and full reflection;
reflected, smooth and positive-primitive controls lack the canonical
gamma-times-zeta identity; finite-prime orbit controls lack full
reflection; atomic/finite-profile controls lack the completed xi source;
RH-conditional normalized endpoints lack the ordinary Dirichlet-series
input. The new pole and covariance identities are generic on domains
with the stated simple-root/analytic-unit bounds. They may hold for
controls on such domains, and do not exclude their collisions elsewhere.

HDA-16 is complete **at the eventual endpoint direct-comparison scope**
of Notes 26 and 31. HDA-19 is complete **at the stated outer/late-time
comparison scope** of Notes 30 and 31. Neither label supplies numerical
onsets, distinct review, transition acceptance or a global theorem.
HDA-04/05/06 retain their broader unresolved obligations; HDA-18 remains
gated by the finite input and joining analysis. The finite-cutoff
potential obstruction of Note 25 and the rejected Note 23 trial remain
in force at their original scopes.

**Next: Analytical — Astra, HDA-17/HDA-18.** Specify and prove the
all-time joining contract using the negative endpoint, the full-saddle
positive endpoint, the compact-time outer estimates PE44 and a finite
core. Identify one finite source/jet error budget that makes every
joining, curvature, forcing and actual-covariance term informative.
This is now the missing structural input; a larger numerical mesh is
not yet an assignment. Any splice of fields or observables must pay
its own derivative and covariance terms rather than infer them from
the endpoint errors. HDA-20's distinct-reviewer audit is separately ready.

[saddle]: 30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md
[adaptive]: 14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md
[inner]: 19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md
[global]: 20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[review]: ../reviews/13_POSITIVE_EVOLUTION_AND_COVARIANCE_SELF_REVIEW_20261024.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[cauchy]: https://dlmf.nist.gov/1.9.E31
