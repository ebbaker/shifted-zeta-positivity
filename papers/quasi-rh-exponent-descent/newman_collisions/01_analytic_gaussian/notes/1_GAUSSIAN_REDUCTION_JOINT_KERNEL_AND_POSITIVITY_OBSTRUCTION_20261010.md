# Gaussian reduction and the kernel of joint collision observations

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex). Reasoning effort: ultra, verified from this
chat's recorded configuration. Parallel LLM checks are internal checks,
not independent mathematical validation.

The imaginary Gaussian lift reproduces the genuine backward heat flow,
including its derivative and higher jets. Its joint value and derivative
observation is exactly the projection onto the first two Gaussian Hermite
components. The orthogonal complement can carry strictly positive energy
at a collision. Consequently Gaussian positivity and a positive bulk norm
alone cannot supply the missing lower bound for the collision vector.
This is a scoped obstruction to that mechanism; it is not an obstruction to
additional arithmetic relations for the genuine theta state.

The starting task is the first direction in
[Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
The targets and paid arithmetic interface are those of
[Heat Note 13](../../notes/13_RECENT_HEAT_RESULTS_AND_PATHS_FORWARD_20261009.md)
and the [stable manuscript](../../newman_collision_reductions.tex).

## 1 Exact state and time orientation

Retain the full kernel and normalization

\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}},\qquad
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\]
\[
H_0(z)=\tfrac18\xi(\tfrac12+iz/2),\qquad
\partial_tH_t=-\partial_z^2H_t.
\tag{1}
\]

For \(t>0\), set

\[
p_t(y)=(4\pi t)^{-1/2}e^{-y^2/(4t)},\qquad
f(x,y)=H_0(x+iy),\qquad P_t f(x)=\int_{\mathbb R}p_t(y)f(x,y)\,dy.
\]

Gaussian averaging of \(\cos((z+iy)u)\) gives
\(e^{tu^2}\cos(zu)\), so

\[
P_t f(x)=H_t(x).
\tag{2}
\]

This established representation is the rescaled formula in
[Polymath Section 4](https://arxiv.org/html/1904.12438v2#S4).
The derivations below concern its domains, observation kernel, and scope.

An admissible analytic class consists of entire functions \(F\) such that,
on each compact real \(x\)-interval, every fixed derivative satisfies
\(\lvert F^{(j)}(x+iy)\rvert\le C_{a,j}e^{y^2/(4a)}\) for every
\(a>0\). This class is sufficient for every Gaussian integral and
integration by parts used here; ordinary unweighted transverse \(L^2\)
is not assumed. Section 4 gives such bounds for the genuine theta state.

In the fixed-field interface, \(\partial_t f=0\) and the reduction moves.
Since \(\partial_t p_t=\partial_y^2p_t\), and holomorphicity gives
\(f_y=if_x\), integration by parts yields

\[
(\partial_tP_t)f=P_t f_{yy}=-\partial_x^2P_t f.
\tag{3}
\]

In the evolving-field interface,

\[
U(t,x,y)=H_t(x+iy),\qquad U_t=U_{yy}=-U_{xx},\qquad U_y=iU_x,
\quad U(t,x,0)=H_t(x).
\tag{4}
\]

Thus the enlarged generator is forward transverse diffusion on a restricted
analytic class. The mode \(e^{ikx-ky}\) is amplified and is not in
unweighted transverse \(L^2\). A contraction theorem on that space does
not apply to this mode. Neither interface is isotropic diffusion in two
real coordinates.

## 2 The joint observation and its kernel

Write \(d\mu_t(y)=p_t(y)dy\), \(A=A_t(x)>0\),
\(b=\partial_x\log A_t(x)\), and \(L=\log(x/(4\pi))\).
Use \(x>4\pi\), so \(L>0\), as in the working rectangle below.
Spatial derivatives fix time and hold the observation scale \(L\) at its
chosen center. Since \(f_x=-if_y\), integration by parts gives

\[
H_t'= -\frac{i}{2t}P_t(yf).
\tag{5}
\]

For \(Q_t=H_t/A_t\), the genuine vector is exactly

\[
\mathcal W=\left(\frac{Q_t}2,\frac{2Q_t'}L\right)
=\int_{\mathbb R}p_t(y)f(x,y)
\left(\frac1{2A},\frac{-iy/t-2b}{LA}\right)dy.
\tag{6}
\]

The drift \(-bH_t\) is retained. Real symmetry
\(f(x,-y)=\overline{f(x,y)}\) makes both coordinates real. The same
triangular map shows

\[
\mathcal W=0\quad\Longleftrightarrow\quad P_t f=P_t(yf)=0.
\tag{7}
\]

On \(L^2(\mu_t)\), with inner product
\(\langle g,h\rangle=\int g\overline h\,d\mu_t\), this kernel is
\(\operatorname{span}\{1,y\}^{\perp}\). The Gram matrix of the
coefficient kernels printed in (6), using \(\int k_i\overline{k_j}\), is

\[
G=\frac1{A^2}
\begin{pmatrix}
1/4&-b/L\\
-b/L&4(b^2+1/(2t))/L^2
\end{pmatrix},\qquad \det G=\frac1{2tL^2A^4}>0.
\tag{8}
\]

Their independence establishes two independent observations. It does not
remove the infinite-dimensional observation kernel. More precisely, if
\(\Pi_t\) is orthogonal projection onto \(\operatorname{span}\{1,y\}\),

\[
\|\Pi_t f\|^2=|H_t|^2+2t|H_t'|^2,
\qquad
\|f\|^2=|H_t|^2+2t|H_t'|^2+\|(I-\Pi_t)f\|^2.
\tag{9}
\]

This is the exact missing term in a proposed reverse Jensen argument.
Positive bulk energy can lie entirely in the last term.

## 3 Higher jets and the unresolved signed relation

Let \(s=2t\), and define the variance-\(s\) Hermite polynomials by

\[
\exp(ry-sr^2/2)=\sum_{j\ge0}h_j(y)r^j/j!,\qquad
\mathbb E_t(h_jh_k)=\mathbf1_{j=k}j!s^j.
\]

For example, \(h_2=y^2-s\), \(h_3=y^3-3sy\), and
\(h_4=y^4-6sy^2+3s^2\). Repeated Gaussian integration by parts gives

\[
H_t^{(j)}(x)=(-i)^j(2t)^{-j}P_t(h_jf),\qquad
\|f\|_{L^2(\mu_t)}^2
=\sum_{j\ge0}\frac{(2t)^j}{j!}|H_t^{(j)}(x)|^2.
\tag{10}
\]

The second equality follows by completeness of Hermite polynomials in
Gaussian \(L^2\). Growth bounds justify the integrations and ensure
finite norm. A collision eliminates only degrees zero and one; the norm
identity contains no sign information on the mixed product of degrees two
and four.

At a collision, putting \(h_j^*=H_t^{(j)}(x)\), the normalized jets are

\[
q_2=h_2^*/A,\qquad q_3=(h_3^*-3bh_2^*)/A,
\quad q_4=(h_4^*-4bh_3^*+6(b^2-b')h_2^*)/A.
\]

Consequently the necessary all-real-threshold test in Heat Note 13 becomes

\[
2q_3^2-3q_2q_4-(18b'+9/x^2)q_2^2
=A^{-2}\left(2(h_3^*)^2-3h_2^*h_4^*-9(h_2^*)^2/x^2\right)\ge0.
\tag{11}
\]

The normalizer terms cancel exactly at a collision. Gaussian norm positivity
does not force the opposite sign in (11). Time evolution also retains
\(\partial_tH_t^{(j)}=-H_t^{(j+2)}\); a fourth-jet system requires
fifth and sixth jets and is not closed by (10).

## 4 A closed rectangle and explicit Gaussian tail payments

Use one closed rectangle in the parameters of the existing shrinking sector:

\[
\mathcal R=\{1/25\le t\le1/20,\quad1\le\kappa\le6/5\},\qquad
L=\kappa/t\in[20,30],\quad x=4\pi e^L\in[X_-,X_+],
\quad X_\pm=4\pi e^{20},\ 4\pi e^{30}.
\tag{12}
\]

The \(x\) and \(L\) entries are ranges on this parameter rectangle,
not new independent coordinates. This scout is not uniform down to zero
time. Every spatial derivative is taken at fixed time and cutoff, rather
than along \(x(t,\kappa)\).

For \(u\ge0\), each theta summand is positive, and
\(n^4\le16^{n-1}\), \(n^2-1\ge3(n-1)\) imply

\[
0<\Phi(u)\le4\pi^2e^{9u-\pi e^{4u}}
\le4\pi^2e^{-\pi}e^{-(4\pi-9)u-8\pi u^2}.
\tag{13}
\]

Indeed \(\sum n^4e^{-\pi(n^2-1)}\le(1-16e^{-3\pi})^{-1}<2\),
and \(e^{4u}\ge1+4u+8u^2\). Define, for \(0<a<8\pi\),

\[
M_j(a)=\int_0^\infty u^je^{au^2}\Phi(u)du\le
B_j(a):=2\pi^2e^{-\pi}(8\pi-a)^{-(j+1)/2}\Gamma((j+1)/2).
\tag{14}
\]

For every \(a>0\), the integral defining \(M_j(a)\) remains finite
by the first bound in (13). The explicit bound \(B_j(a)\) uses
\(a<8\pi\). Young's inequality gives

\[
|H_0^{(j)}(x+iy)|\le M_j(a)e^{y^2/(4a)}.
\tag{15}
\]

For \(t<a<8\pi\), define the directly truncated jets
\(H_{j,R}=\int_{-R}^Rp_t(y)H_0^{(j)}(x+iy)dy\). Completing the
Gaussian square pays their tails:

\[
|H_t^{(j)}-H_{j,R}|\le
E_j(t,R):=B_j(a)\sqrt{\frac a{a-t}}
\operatorname{erfc}\left(R\sqrt{\frac{a-t}{4at}}\right).
\tag{16}
\]

Here and below use \(a=1\). Uniformly on \(\mathcal R\),

\[
E_j(t,R)\le B_j(1)\sqrt{20/19}\,e^{-19R^2/4}.
\tag{17}
\]

Also (15) gives
\(\|f\|^2\le B_0(1)^2(1-2t)^{-1/2}\), proving the theta field
belongs to every Gaussian Hilbert space used in this note.

No spectral contour is moved in (13)–(17). These payments deliberately
preserve a simple absolute envelope, whose normalization cost can be large.

## 5 Normalization and complete arithmetic errors

Use precisely the manuscript normalizer, with principal logarithms,

\[
s_z=(1-iz)/2,\qquad
m_0(s)=\Log s+\Log(s-1)-\frac s2\log\pi+
\log\frac{\sqrt{2\pi}}{16}+
\left(\frac s2-\frac12\right)\Log\frac s2-\frac s2,
\]
\[
\alpha(s)=\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi},\qquad
m_t=m_0+t\alpha^2/4,\qquad
A_t(z)=\exp\{(m_t(s_z)+m_t(1-s_z))/2\}.
\tag{18}
\]

The positive real axis and its radius-one neighborhoods in (12) avoid
every logarithmic cut. On that axis let \(\alpha=\alpha_r+i\alpha_i\).
Direct evaluation of (18) gives

\[
\log A_t(x)=\frac78\log(1+x^2)+\frac14\log\pi-\log32-\frac14
-\frac x4\arctan x+\frac t4(\alpha_r^2-\alpha_i^2),
\]
\[
\alpha_i=\frac{3x}{1+x^2}-\frac12\arctan x,\qquad
A_t(x)\ge e^{-\pi x/8-4}\ge e^{-\pi X_+/8-4}=:A_*.
\tag{19}
\]

For the lower bound use \(|\alpha_i|<1\) on (12), \(t\le1/20\),
\(\arctan x\le\pi/2\), and the nonnegative logarithmic and
\(\alpha_r^2\) terms.

Retain every normalization derivative. Put

\[
d_m=A_t\partial_x^m(A_t^{-1}),\qquad d_0=1,\qquad
d_{m+1}=d_m'-bd_m.
\]

Then for every fixed \(j\),

\[
q_j=A^{-1}\sum_{r=0}^j\binom jr d_{j-r}H_t^{(r)},\qquad
q_{j,R}=A^{-1}\sum_{r=0}^j\binom jr d_{j-r}H_{r,R},
\]
\[
|q_j-q_{j,R}|\le
\varepsilon_j(t,x,R):=A^{-1}\sum_{r=0}^j\binom jr|d_{j-r}|E_r(t,R).
\tag{20}
\]

For an explicit uniform bound, on \(|z-x|\le1\) set
\(h=(x-1)/2\). Both \(s_z,1-s_z\) have real parts in \([0,1]\)
and imaginary parts of modulus at least \(h\). Thus
\(|\alpha|<17\), \(|\alpha'|\le1/h\), and

\[
|\alpha(s_z)-\alpha(1-s_z)|
\le\pi/2+3/h+1/(4h^2),\qquad
|b(z)|\le\pi/8+(3+17t)/(4h)+1/(16h^2)<1/2.
\]

Integration of \(b\) along a radius and Cauchy's inequality therefore give
\(|d_m(x)|\le m!e^{1/2}\). With

\[
C_j=e^{1/2}\sqrt{20/19}\,j!\sum_{r=0}^j\frac{B_r(1)}{r!},\qquad
C=\max_{0\le j\le6}C_j,
\]
\[
\varepsilon_j\le C_j\exp(\pi X_+/8+4-19R^2/4).
\tag{21}
\]

For example the fully specified fixed radius

\[
R^2=\frac4{19}\left(\pi X_+/8+24+\max(0,\log C)\right)
\tag{22}
\]

makes every \(\varepsilon_j\le e^{-20}\) for \(0\le j\le6\).
This radius is very large because the absolute envelope (15) discarded the
real-height decay that normalization removes. Formula (22) is a rigorous
payment. The following paid contour refinement gives a much smaller radius.

Put \(X=X_+\), \(\theta=\pi/8-1/X\), and \(q=8/X\). The full
theta kernel is holomorphic and even in \(|\Im u|<\pi/8\), because
its series converges there locally uniformly and theta modularity gives
evenness. Explicitly, if \(\Theta(r)=\sum_{n\in\mathbb Z}e^{-\pi n^2r}\),
the identity \(\Theta(r)=r^{-1/2}\Theta(1/r)\) makes
\(F(u)=e^u\Theta(e^{4u})\) even on the real line. Direct differentiation
gives \(\Phi=(F''-F)/16\). Hence \(\Phi\) is even there, and the
identity extends to the strip by analyticity. For \(0\le v\le\theta\),
\(\cos(4v)\ge\cos(4\theta)=\sin(4/X)\ge8/(\pi X)>0\).
The vertical sides of the full-line spectral contour therefore vanish
by double-exponential decay, even with any fixed polynomial and exponential
weights. Shifting the full spectral line upward by \(i\theta\) gives

\[
H_0^{(j)}(x+iy)=\frac12\int_{\mathbb R}
[i(u+i\theta)]^j\Phi(u+i\theta)
e^{i(x+iy)(u+i\theta)}du.
\tag{22a}
\]

This is a spectral contour movement; the Gaussian \(y\) integration is
unchanged. The shift is fixed on the whole rectangle, so no derivative of
\(\theta\) is introduced. To pay its kernel envelope define

\[
I_m(q)=\frac12\sum_{\ell=0}^m\binom m\ell
\Gamma((\ell+1)/2)(2/q)^{(\ell+1)/2}.
\]

For \(v\in[n-1,n]\), \(n\le v+1\) and
\(n^2\ge(1+v^2)/2\). Integration over these unit intervals proves
\(\sum_{n\ge1}n^m e^{-qn^2}\le e^{-q/2}I_m(q)\).
For \(u\ge0\), apply this bound with \(qe^{4u}\), using
\(I_m(qe^{4u})\le e^{-2u}I_m(q)\), to obtain

\[
|\Phi(u+i\theta)|\le C_\theta e^{7u}
\exp[-(4/X)e^{4u}],\qquad
C_\theta=2\pi^2I_4(q)+3\pi I_2(q).
\tag{22b}
\]

Evenness and real symmetry give the same absolute bound at \(-u+i\theta\).
Let \(v_0=\tfrac14\log(X/4)\), \(d=v_0+\pi/8\), and set

\[
D_j=C_\theta e^{7v_0}\left[v_0d^j e^{v_0^2}
+\frac{e^{2v_0^2-1/4}}2\sum_{\ell=0}^j\binom j\ell d^{j-\ell}
3^{-(\ell+1)/2}\Gamma((\ell+1)/2)\right].
\tag{22c}
\]

This bounds \(\int_0^\infty(u+\theta)^j|\Phi(u+i\theta)|e^{u^2}du\).
To see it, split at \(v_0\). On the first part replace \(u\) by
\(v_0\) in the positive factors. On the second write \(u=v_0+w\),
use \(u^2\le2v_0^2+2w^2\), \(e^{4w}\ge1+4w+8w^2\), and
\(3w\le3w^2+3/4\). The remaining integrand is bounded by
\(e^{2v_0^2-1/4}(w+d)^j e^{-3w^2}\), whose integral is the sum
in (22c). Equations (22a)–(22c) and \(|y|u\le u^2+y^2/4\) yield

\[
|H_0^{(j)}(x+iy)|\le e^{-\theta x}D_j e^{y^2/4}.
\tag{22d}
\]

The pointwise normalizer bound (19) now gives
\(e^{-\theta x}/A\le e^{4+x/X}\le e^5\). Combining the same Gaussian
tail integration and Cauchy normalization payment as before,

\[
\varepsilon_j\le e^{5.5}\sqrt{20/19}\,j!
\sum_{r=0}^j\frac{D_r}{r!}\,e^{-19R^2/4}.
\tag{22e}
\]

All constants admit generous elementary bounds. Since \(X<16e^{30}\),
\(v_0<8\), \(d<9\), and
\(\Gamma((\ell+1)/2)\le4\) for \(0\le\ell\le6\),
one has \(C_\theta<e^{85}\) and

\[
D_j<e^{85+56}\left[8\cdot9^6e^{64}+2\cdot10^6e^{128}\right]
<e^{285}\qquad(0\le j\le6).
\]

For \(C_\theta\), the sharper gamma bound \(\Gamma\le2\) through
\(\ell=4\) gives \(I_4(q)<512e^{75}\) and
\(I_2(q)<32e^{45}\), so
\(C_\theta<16384e^{75}+384e^{45}<e^{85}\).
Using \(j!\le720\) and \(\sum1/r!<e\), the prefactor in (22e) is
less than \(e^{300}\). Hence the practical fixed cutoff

\[
\boxed{R=9\quad\Longrightarrow\quad
|q_j-q_{j,9}|<e^{-84}\quad(0\le j\le6,\ (t,\kappa)\in\mathcal R).}
\tag{22f}
\]

The tail payment is rigorous; numerical quadrature and its rounding errors
have not been certified by this statement. The refinement supplies no new
signed arithmetic restriction.

The existing arithmetic approximant has the fixed integer cutoff

\[
N=\lfloor\sqrt{e^L+t/16}\rfloor,\qquad
|q_j-F_{t,N}^{(j)}(x)|\le j!L^j\eta_N,
\quad \eta_N\le\bar\eta:=5e^{-\kappa(\kappa+4)/(16t)}.
\tag{23}
\]

This is the imported complete disk error from Heat Notes 8 and 13, including
normalizer conversion, reflection, and natural-cutoff changes. No new
error theorem for a truncated theta series is substituted. On (12),
\(\bar\eta\ge5e^{-39/4}\), so (22) and (22f) pay Gaussian jet errors well below
this common upper envelope. This comparison does not assert a positive
lower bound on the actual error \(\eta_N\).

A genuine collision requires
\(|(F_{t,N}/2,2F_{t,N}'/L)|^2\le17\eta_N^2/4\). The truncated
Gaussian vector instead has coordinate errors
\((\varepsilon_0/2,2\varepsilon_1/L)\) from the genuine vector.
Comparing its jets with the finite approximant pays
\(\varepsilon_j+j!L^j\eta_N\). These are different representations
of the same genuine state; use the payment corresponding to the quantity
actually evaluated.

For any approximation \(v_j\) with \(|q_j-v_j|\le\delta_j\),
\(j=2,3,4\), the full quadratic threshold payment is

\[
\Delta(v,\delta)=4|v_3|\delta_3+2\delta_3^2
+3(|v_2|\delta_4+|v_4|\delta_2+\delta_2\delta_4)
+|\gamma|(2|v_2|\delta_2+\delta_2^2),\quad\gamma=18b'+9/x^2.
\tag{24}
\]

Use \(\delta_j=\varepsilon_j\) for Gaussian jets or
\(j!L^j\eta_N\) for the full arithmetic sum. A negative approximate
expression must be strictly less than \(-\Delta\) to contradict the
necessary all-real sign. A small Gaussian tail alone supplies no such sign.

## 6 Finite Gaussian reductions retain boundary flux

For fixed \(R\), the truncated value satisfies

\[
\partial_tH_{0,R}=-\partial_x^2H_{0,R}
+[p_t'f-p_tf_y]_{-R}^{R}.
\tag{25}
\]

The flux has magnitude at most

\[
\frac{2e^{-\beta R^2}}{\sqrt{4\pi t}}
\left(\frac{RB_0(1)}{2t}+B_1(1)\right),\qquad
\beta=(1-t)/(4t).
\tag{26}
\]

If \(R=R(t)\) moves, add
\(R'(t)[p_t(R)f(x,R)+p_t(-R)f(x,-R)]\). The radius in (22) is fixed.
For the derivative extracted from the truncated value, (5) becomes

\[
\partial_xH_{0,R}=-i[p_tf]_{-R}^{R}
-\frac{i}{2t}\int_{-R}^{R}yp_tf\,dy.
\tag{27}
\]

Thus directly truncated jets in (16) include the boundary correction when
expressed through moments. If using the moment-only derivative estimator,
its error relative to the full derivative is at most
\(B_0(1)e^{-\beta R^2}/((1-t)\sqrt{\pi t})\).
No boundary term is silently removed. The full-line terms vanish by (15).
The contour envelope (22d) also pays these boundary terms with the factor
\(e^{-\theta x}D_j\) in place of \(B_j(1)\). In particular at \(R=9\),
the normalized flux in (25) and the normalized derivative boundary term
are both less than \(e^{-92}\) on (12): use \(t\ge1/25\),
\(D_0,D_1<e^{280}\) (the preceding elementary bound with \(j\le1\)),
\(e^{-\theta x}/A\le e^5\), and
\(\beta R^2\ge384.75\).

For \(Q_R=H_{0,R}/A_t\), the complete normalized equation is

\[
\partial_tQ_R=-Q_R''-2bQ_R'
-(b'+b^2+\partial_t\log A_t)Q_R
+A_t^{-1}[p_t'f-p_tf_y]_{-R}^R.
\tag{27a}
\]

This keeps the moving normalizer as well as the finite boundary flux.

## 7 Analytic and positive kernel controls

The manuscript's even quartic, with \(\delta=t-T\), is

\[
P_t(z)=z^4-(2a^2+12\delta)z^2+a^4+4a^2\delta+12\delta^2,
\quad T>0.
\]

It obeys backward heat, has all-real threshold \(T\), and
\(P_T(a)=P_T'(a)=0\). In the Gaussian lift at that collision,

\[
P_0(a+iy)=h_4(y)-4a^2h_2(y)-4ia\,h_3(y),\qquad s=2T,
\]
\[
\mathbb E_T|P_0(a+iY)|^2
=128T^2(a^4+6a^2T+3T^2)>0.
\tag{28}
\]

This even analytic state has zero observations and strictly positive bulk
energy. Choosing \(T\) in (12) and \(a=4\pi e^{\kappa/T}\) places the
control at a point of the same rectangle. It is not a theta spectral kernel.
Its jets \(P_2=8a^2,P_3=24a,P_4=24\) saturate the forced-mirror
threshold test.

To check that positivity of a smooth rapidly decaying spectral kernel does
not repair the argument, let

\[
\varphi(u)=e^{-\cosh u},\quad
B(z)=\int_{\mathbb R}\varphi(u)e^{izu}du=2K_{iz}(1),
\]
\[
p_a(u)=\tfrac12\varphi(u)+\tfrac14\varphi(u-2a)
+\tfrac14\varphi(u+2a),\quad q_{T,a}(u)=e^{-Tu^2}p_a(u).
\]

The kernel \(q_{T,a}\) is even, smooth, strictly positive, and
double-exponentially decaying. Its flow

\[
J_t(z)=\int_{\mathbb R}e^{tu^2}q_{T,a}(u)e^{izu}du
\quad\text{satisfies}\quad J_T(z)=B(z)\cos^2(az).
\tag{29}
\]

At \(x_*=\pi/(2a)\) with \(B(x_*)\ne0\), it has an exact double zero,
with jets

\[
J_2=2a^2B,\qquad J_3=6a^2B',\qquad J_4=12a^2B''-8a^4B.
\tag{30}
\]

There are such choices in (12): select a point with
\(B(4\pi e^{\kappa/T})\ne0\), possible because the zeros of the nonzero
entire function \(B\) are discrete, and then put \(a=\pi/(2x_*)\).
Its Gaussian lifted field is in \(L^2(\mu_T)\), by the same
super-exponential growth argument, and is nonzero there while both
observations vanish.

The manuscript's spectral proof shows that all zeros of \(B\) are real:
if \(K_{iz}(1)=0\), the decaying function \(v(r)=K_{iz}(e^r)\) on
\(r\ge0\) satisfies \(-v''+e^{2r}v=z^2v\), with \(v(0)=0\), so
integration against \(\overline v\) gives \(z^2>0\). Thus (29) is
also all-real at the collision time. The control does not use theta
coefficients or assert monotonicity of \(q_{T,a}\). The manuscript's
separate kernel \(\varphi^{(4)}+324\varphi\) provides the stronger
monotone-kernel threshold control under its printed hypotheses.

## 8 Scoped stopping result and continuation

There is no positive constant \(c\) giving
\(|H_t|^2+2t|H_t'|^2\ge c\|f\|^2\) on the admissible even analytic
class, or on all even strictly positive smooth spectral kernels with
super-exponential decay. Equations (28) and (29) provide nonzero states in
the observation kernel. The same obstruction survives the nonvanishing
normalizer in (6). It also defeats a positive average of squared lifted
value and derivative if that quantity is proposed as a pointwise lower
bound: the quartic has both observations zero while
\(\mathbb E_T|P_0'(a+iY)|^2=128T(a^4+9a^2T+6T^2)>0\).

This completes the first scout's stated stopping alternative in Heat Note
14. Exact reduction, finite-tail payments, and a precise failure of the
tested Gaussian norm mechanism are established. No new theta-specific
signed conditional inequality is established.

A next bounded task should specify one actual-theta restriction on
\(P_t(h_jf)\) conditional on (7), and test its consequence for (11) with
(24). Alternatively it could control the remaining Hermite energy strongly
enough to yield the collision-conditioned short-probe upper bound requested
in Heat Note 13. Merely improving (17) or making (22) practical would refine
the representation without supplying that arithmetic implication. Higher
multiplicities and parameter coverage remain separate obligations.
