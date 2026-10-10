# Green-kernel endpoint equivalence and conditional theta jets

10 October 2026. GPT-6 (Codex); exact serving variant and configured
reasoning effort unavailable. This derivation, replay and review are
internal LLM work, not independent mathematical validation.

This continues [Note 1](1_ROTOR_ZERO_MODE_WARD_IDENTITY_AND_SECTOR_MISMATCH_20261010.md)
and priority 3 in [Heat Note 15](../../notes/15_SIXTEEN_PROGRAM_INITIAL_RESULTS_AND_FIVE_PRIORITIES_20261010.md).
The new result identifies exactly which part of the endpoint Ward data
is generic: the entire affine/odd-endpoint hierarchy is a positive
Green-kernel lift of one fixed imaginary-height normalization. A smooth
positive double-zero control shares it. The remaining lattice coefficients
are therefore essential to any discriminating signed theorem.

## 1. Genuine theta reduction and a positive inverse dictionary

Retain the inserted rotor state and full theta coefficients from Note 1:
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}},\quad
k(u)=e^u(\vartheta(e^{4u})-1).
\]
On \(u\ge0\), \(k>0\), \(k''-k=16\Phi\),
and \(k'(0)=-1\). The rotor insertion and all its fixed polynomial
moments are trace-norm integrable on compact time/complex-height sets.
The genuine readouts are
\[
H_t(x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,\quad
J_t(x)=\int_0^\infty e^{tu^2}k(u)\cos(xu)\,du.
\]
Their generator is multiplication by \(u^2\), so
\(\partial_tH_t=-H_t''\) and \(\partial_tJ_t=-J_t''\), rather than
ordinary rotor thermal evolution.
Initial matching remains \(H_0=\xi(1/2+ix/2)/8\).

The decay conditions allow a second exact representation:
\[
\boxed{k(u)=16\int_u^\infty\sinh(v-u)\Phi(v)\,dv.}
\tag{1}
\]
Differentiate the integral twice: its first derivative is
\(-16\int_u^\infty\cosh(v-u)\Phi(v)dv\), and its second derivative
is \(k+16\Phi\). Both \(k\) and the proposed integral, together with
their first derivatives, decay faster than \(e^{-u}\) as \(u\to\infty\).
Their difference solves \(d''-d=0\), whose two exponential solutions
cannot have that decay unless the difference is zero. This specifies
the inverse domain; merely requiring decay to zero would leave an
undetermined \(e^{-u}\) homogeneous term.

At the endpoint, (1) gives
\[
-k'(0)=16\int_0^\infty\cosh(v)\Phi(v)\,dv=16H_0(i)=1.
\tag{2}
\]
Thus the endpoint constant is precisely the normalization
\(H_0(i)=1/16\), consistent with \(\xi(0)=1/2\).
It is not a separate independently positive collision observable.

## 2. The endpoint hierarchy extends beyond integer theta coefficients

For any smooth even positive spectral kernel \(\phi\), impose the
weighted derivative domain
\[
\int_0^\infty e^{T u^2+Yu}|\phi^{(j)}(u)|\,du<\infty
\quad\text{for every fixed }T,Y\ge0,\ j\ge0.
\]
Thus the kernel and its derivatives admit every fixed Gaussian
and exponential weight. The actual theta kernel and the control in
Section 4 satisfy this domain. First normalize
\(\int_0^\infty\cosh u\,\phi(u)du=1/16\), then define \(k_\phi\)
by (1) with \(\phi\) in place of \(\Phi\).
This gives
\[
k_\phi>0,\quad k_\phi'<0,\quad
k_\phi''=k_\phi+16\phi>0,\quad k_\phi'(0)=-1.
\tag{3}
\]
Since every odd derivative of \(\phi\) at zero vanishes, repeated
differentiation of \(k_\phi''-k_\phi=16\phi\) gives
\[
\boxed{k_\phi^{(2j+1)}(0)=-1\quad(j\ge0).}
\tag{4}
\]
The formal even completion \(k_\phi(u)+e^u\) has every odd jet zero
at the origin. In an analytic kernel class it extends evenly across
the origin. This endpoint reflection data, convexity and positivity
are therefore shared by the entire class (3), without an integer
lattice counting interpretation.

Two integrations by parts, with the same vanished infinity terms and
the exact endpoint (2), give for every such kernel
\[
16H_t=1+(2t-1-x^2)J_t+4txJ_t'-4t^2J_t''.
\tag{5}
\]
Its theta specialization is exact, but generic identities (1)--(5)
do not select the arithmetic coefficient sequence.

## 3. Candidate constraints and all auxiliary jets through six

Write \(a=2t-1-x^2\), \(J_j=\partial_x^jJ_t(x)\),
and \(K_j=16H_t^{(j)}(x)\). The needed explicit list is
\[
K_0=1+aJ_0+4txJ_1-4t^2J_2,
\]
\[
K_1=-2xJ_0+(a+4t)J_1+4txJ_2-4t^2J_3,
\]
\[
K_2=-2J_0-4xJ_1+(a+8t)J_2+4txJ_3-4t^2J_4,
\]
\[
K_3=-6J_1-6xJ_2+(a+12t)J_3+4txJ_4-4t^2J_5,
\]
\[
K_4=-12J_2-8xJ_3+(a+16t)J_4+4txJ_5-4t^2J_6.
\tag{6}
\]
The constant is present only in \(K_0\). At a genuine collision,
\(K_0=K_1=0\), so for \(t>0\),
\[
J_2=(1+aJ_0+4txJ_1)/(4t^2),
\quad
J_3=((a+4t)J_1-2xJ_0+4txJ_2)/(4t^2).
\tag{7}
\]
There is no corresponding determination of the last three moments.
Conditioned on \(J_0,J_1\) and (7), the Jacobian from
\((J_4,J_5,J_6)\) to \((K_2,K_3,K_4)\) is
\[
\begin{pmatrix}
-4t^2&0&0\\4tx&-4t^2&0\\a+16t&4tx&-4t^2
\end{pmatrix},
\qquad \det=-64t^6\ne0.
\tag{8}
\]
Consequently the affine Ward system allows arbitrary raw second,
third and fourth jets algebraically after both collision equations.
The checker records rational examples with the same \(t=1/20,x=1\),
\(H_2=1,H_3=0\), and respectively \(H_4=0,-4\), giving opposite
raw threshold signs \(-9,+3\). These are formal compatible jets;
they are not claimed to come from a positive kernel or theta.

At an actual collision, normalizer cancellation gives
\[
A_t^2\mathscr L(q)=
\frac1{256}(2K_3^2-3K_2K_4-9K_2^2/x^2).
\tag{9}
\]
The coefficient of \(J_6\) in this expression is
\[
\frac{12t^2K_2}{256}=\frac34t^2H_t''.
\tag{10}
\]
For an ordinary double zero it is nonzero. Thus the precise missing
auxiliary signed datum in this selected Ward combination is \(J_6\).
If \(H''=0\), the fourth-jet test is already positive at exact
multiplicity three, or zero at higher multiplicity; deflation then
introduces still higher auxiliary jets. Equation (8) is a scoped
failure of this algebraic closure, not a theorem that all arithmetic
lattice constraints fail.

## 4. A positive double-zero control with the complete same endpoint data

Take \(\varphi(u)=e^{-\cosh u}\),
\[
p_b(u)=\tfrac12\varphi(u)+\tfrac14\varphi(u-2b)
+\tfrac14\varphi(u+2b),\qquad
\phi_c(u)=s\,e^{-Tu^2}p_b(u),
\]
where \(T,b>0\) and
\[
s=\left(16\int_0^\infty e^{-Tu^2}p_b(u)\cosh u\,du\right)^{-1}.
\]
The control is smooth, even, strictly positive and
super-exponentially decaying. Its half-line heat readout at \(T\) is
\[
G_T(z)=\frac{s}{2}B(z)\cos^2(bz),\quad
B(z)=\int_{\mathbb R}e^{-\cosh u}e^{izu}\,du.
\tag{11}
\]
Choose \(x_*=\pi/(2b)\) with \(B(x_*)\ne0\). It is a genuine
ordinary double zero of this control. The spectral proof in the stable
manuscript gives all-real zeros for \(B=2K_{iz}(1)\); hence all
zeros in (11) are real. Its order bound
\(\log\max_{|z|\le r}|B(z)|=O(r\log(r+2))\) follows directly from
the same double-exponential spectral envelope.

Build \(k_{\phi_c}\) by (1). Equations (2)--(7) and every odd
endpoint jet (4) hold exactly at the control collision. It also has
the same score Ward hierarchy as Program 03.
To check that its all-real sign is compatible, write \(c=s/2\).
At the collision
\[
G_2=2cb^2B,\quad G_3=6cb^2B',\quad
G_4=c(12b^2B''-8b^4B).
\]
Consequently
\[
2G_3^2-3G_2G_4-9G_2^2/x_*^2
=36c^2b^4\left[
2(B'^2-BB'')+(4b^2/3-1/x_*^2)B^2
\right]>0.
\tag{12}
\]
The first term is nonnegative by the all-real order-less-than-two
Hadamard-product Laguerre inequality; the second is strictly positive,
since \(b x_*=\pi/2\) gives
\((4b^2/3-1/x_*^2)=(\pi^2/3-1)/x_*^2>0\).
This control therefore retains positivity, convex Green lift, all endpoint
constraints, score insertions and the required threshold sign. It is not
the integer theta kernel. Their generic conjunction cannot force the
opposite sign sought in (9).

## 5. A separate domain obstruction to isolating the rational endpoint part

At time zero, (5) gives
\[
J_0(x)=\frac{1-16H_0(x)}{1+x^2}.
\tag{13}
\]
Both apparent poles are removable in the combined expression because
\(H_0(i)=H_0(-i)=1/16\). Separating the first rational summand and
applying backward heat to it is invalid. At \(x=0\), its formal time
series has coefficients
\[
\left[e^{-t\partial_x^2}(1+x^2)^{-1}\right]_{x=0}
\sim\sum_{\ell\ge0}\frac{(2\ell)!}{\ell!}t^\ell.
\tag{14}
\]
The ratio of successive coefficients is \(4\ell+2\), so the series
has radius zero. Equivalently the rational term's even spectral
kernel is proportional to \(e^{-|u|}\), whose positive-time Newman
integral diverges. The true combined \(J_t\) remains jointly entire
because its Green kernel admits every fixed Gaussian and exponential
weight, as required in Section 2. All cancellation needed for
the domain must be retained before evolution.

## 6. Payments, cross-feed, and continuation

If auxiliary jets \(J_j\) are approximated with errors \(\epsilon_j\),
equation (6) pays raw errors
\[
\delta H_j\le\frac1{16}\{
|a+4tj|\epsilon_j+2j|x|\epsilon_{j-1}
+j(j-1)\epsilon_{j-2}+4t|x|\epsilon_{j+1}
+4t^2\epsilon_{j+2}\},\quad0\le j\le4,
\tag{15}
\]
omitting negative indices. The exact endpoint constant has no error.
For raw approximate second/third/fourth jets \(v_j\), the full
conditional quadratic payment is
\[
\Delta_H=4|v_3|\delta H_3+2(\delta H_3)^2
+3(|v_2|\delta H_4+|v_4|\delta H_2+\delta H_2\delta H_4)
+\frac9{x^2}(2|v_2|\delta H_2+(\delta H_2)^2).
\tag{16}
\]
A strictly negative value below \(-\Delta_H\) would contradict (9)
at an actual all-real-threshold candidate. None is established here.
For arithmetic evaluation via \(F_{t,N}\), retain \(H=AQ\),
all product derivatives and the complete \(j!L^j\eta_N\) payments
from Note 13. Raw and normalized payments are different dictionaries.

[Program 03 Note 2](../../03_susy_dirac_hodge/notes/2_CONDITIONAL_SCORE_JETS_AND_CERTIFIED_SIGN_CHANGE_20261010.md)
provides an actual-theta score sign change and complete residual jets.
Its candidate target still contains a signed mixed insertion. The
positive control (11) shows why combining the generic score and
endpoint identities does not by itself control that insertion or \(J_6\).

The strongest continuation is an inequality tied explicitly to the
integer theta coefficient sequence which bounds \(J_6\) conditionally
on (7), or directly constrains (9), with (15)--(16) paid. The generic
Green/endpoint mechanism is now exhausted to a sharper extent than
the first scout established. No genuine collision exclusion or
endpoint coverage is claimed.

The [checker](../numerics/check_conditional_endpoint.py) passed 25 exact
Fraction-polynomial checks, covering derivatives, (8), (10), both
formal sign examples and the rational-anchor coefficient ratios.
Its [source-bound record](../numerics/conditional_endpoint_record_20261010.json)
does not certify a theta sign; the positive-control argument and
Green domain are analytic proofs above. Source files follow
[LARGE_FILES.md](../../../../../LARGE_FILES.md).
