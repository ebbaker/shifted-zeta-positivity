# Imaginary gluing stability and the remaining height obstruction

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

The full angular defect of the imaginary theta law at one theta scale
controls physical value and derivative errors uniformly on real spectral
height and on \(0\le t\le1\). Combined with the
[central theta estimate](5_COMPLETE_THETA_CENTRAL_ESTIMATE_20261014.md),
it proves a stable bounded norm gap. The error bound is absolute;
arbitrarily small nonzero defects still allow remote joint zeros.

## Full angular defect at a declared theta scale

Let \(c_n\) be a bounded real sequence with \(c_{-n}=c_n,c_0=1\), and put

\[
\Theta_c(r,y)=\sum_{n\in\mathbb Z}c_n
e^{-\pi n^2r+2\pi iny},\qquad r>0,
\]
\[
E_c(r,y)=e^{-\pi r}
\left[\Theta_c(r,y+ir)-e^{\pi r-2\pi iy}\Theta_c(r,y)\right].
\]

Bounded coefficients ensure normal convergence on the angular lines
used below. Reindexing the complete series gives

\[
E_c(r,y)=\sum_{n\in\mathbb Z}(c_n-c_{n+1})
e^{-\pi(n+1)^2r}e^{2\pi iny}.
\]

At the single theta scale r=1, Parseval and symmetry yield

\[
\boxed{D^2:=\int_0^1|E_c(1,y)|^2\,dy
=\sum_{m\ge1}|d_m|^2w_m,}
\quad d_m=c_m-c_{m-1},\quad
w_m=e^{-2\pi m^2}+e^{-2\pi(m-1)^2}.
\tag{1}
\]

Every Fourier coefficient and tail is retained. This is not a finite set
of angular observations or an estimate uniform over all theta scales.
Exact D=0 forces all \(c_n=1\), using the normalization c_0=1.

For the balanced field
\(\mathcal B_c(0,z)=e^{\pi z^2/2}\Theta_c(1,z)\), the same norm is

\[
D^2=\int_0^1 e^{-\pi(1+y^2)}
\left|\mathcal B_c(0,y+i)-e^{\pi/2-\pi iy}\mathcal B_c(0,y)\right|^2dy.
\tag{2}
\]

Thus the balanced gauge is paid exactly. The convention matches the
[imaginary-gluing program](../../02_angular_jacobi_gluing/reviews/CONTINUATION_AND_BRAINSTORM_BRIEF_20261013.md)
at u=0. If bounded coefficients are relaxed, a separate L²-trace
hypothesis is needed on the shifted line; D finite alone does not imply
normal convergence there.

## Separate half-line physical observation

Define

\[
\phi_n(u)=(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\quad \Phi_c^+(u)=\sum_{n\ge1}c_n\phi_n(u),\quad u\ge0,
\]
\[
H_c(t,x)=\int_0^\infty e^{tu^2}\Phi_c^+(u)\cos(xu)\,du.
\]

For perturbed coefficients, the even extension of this half-line source
need not be smooth at zero and need not equal the full prepared-field
projection. Modular reflection may fail. The stability theorem concerns
this explicitly defined observation. If all coefficients are positive,
the half-line source and its even extension are positive.

## Absolute transfer to all four physical jets

Write \(h_j=\partial_x^jH\) and \(\Delta h_j=\partial_x^j(H_c-H)\).
Since \(c_n-1=\sum_{m\le n}d_m\),

\[
\Delta h_j=\sum_{m\ge1}d_m B_{jm},\qquad
B_{jm}=\sum_{n\ge m}\int_0^\infty
e^{tu^2}\phi_n(u)u^j\cos(xu+j\pi/2)\,du.
\]

For \(0\le t\le1\), use
\(e^{4u}\ge1+4u+8u^2\) to obtain

\[
|B_{jm}|\le A_{jm}:=\sum_{n\ge m}b_{jn},\qquad
b_{jn}=\frac{2\pi^2n^4j!e^{-\pi n^2}}{(4\pi n^2-9)^{j+1}}.
\]

The omitted quadratic exponent is nonpositive because
\(t-8\pi n^2<0\). Cauchy--Schwarz against the exact weights in (1)
now gives the complete estimate

\[
\boxed{|\Delta h_j(t,x)|\le DC_j,
\qquad C_j^2=\sum_{m\ge1}\frac{A_{jm}^2}{w_m},
\quad j=0,1,2,3.}
\tag{3}
\]

This holds uniformly for every real x and \(0\le t\le1\).
Absolute convergence justifies the regrouping.

For explicit constants set

\[
a_j=\frac{2\pi^2j!}{(4\pi-9)^{j+1}},\quad
\rho_0=4e^{-3\pi},\quad \rho_j=e^{-3\pi}\ (j\ge1),
\quad r_*=e^{-4\pi}.
\]

Since \(b_{jn}\le a_j n^{2-2j}e^{-\pi n^2}\), the ratio test gives
\(A_{jm}\le a_jm^{2-2j}e^{-\pi m^2}/(1-\rho_j)\).
Using \(w_m\ge e^{-2\pi(m-1)^2}\),

\[
C_0\le\frac{a_0e^{-\pi}}{1-\rho_0}
\sqrt{\frac{1+11r_*+11r_*^2+r_*^3}{(1-r_*)^5}},
\]
\[
C_j\le\frac{a_je^{-\pi}}{(1-\rho_j)\sqrt{1-r_*}},
\qquad j=1,2,3.
\]

Elementary estimates \(3<\pi<22/7\) and \(e^3>20\) prove

\[
\boxed{C_0<\frac12,\qquad C_1<\frac18,
\qquad C_2<\frac1{12},\qquad C_3<\frac1{12}.}
\tag{4}
\]

The same four rational bounds in (4) also bound the genuine jets, since
\(|h_j|\le A_{j1}\le a_je^{-\pi}/(1-\rho_j)\). Expanding the two
quadratic Laguerre forms and retaining every error product therefore yields

\[
\boxed{|\mathscr L_0(H_c)-\mathscr L_0(H)|
\le\frac{11}{192}(2D+D^2),}
\]
\[
\boxed{|\mathscr L_1(H_c)-\mathscr L_1(H)|
\le\frac5{288}(2D+D^2).}
\tag{5}
\]

These transfer a separately proved signed margin. They do not supply
that margin or a loss divided by the physical norm.

## A robust bounded gap from the two estimates

Suppose \(D\le1/30000\). The central theorem and (3)--(4) give

\[
\boxed{|H_c(t,x)+\mathbf j\partial_xH_c(t,x)|
>\frac1{240000}\quad(0\le t\le1,\ |x|\le8).}
\tag{6}
\]

For \(|x|\le1\), the scalar component exceeds
\(1/50-D/2>1/100\). For \(1\le|x|\le8\), the slope magnitude exceeds
\(1/120000-D/8\ge1/240000\).
Also \(H_{c,xx}<-1/180000\) on \(|x|\le5\).
Evenness makes x=0 the only first stationary point in that interval,
and the second stationary set is empty. At the origin
\(H_c>3/125-D/2>1/50\), so
\(\mathscr L_0(H_c;t,0)>1/9000000\).
This is a local quantitative use of the full angular defect, not an
all-height perturbation theorem.

## Why arbitrarily small defects can still hide remote collisions

Fix \(T\in(0,1)\), and perturb only c_1,c_2 while retaining
\(c_n=1\) otherwise. Let
\(K_n(x)=\int_0^\infty e^{Tu^2}\phi_n(u)\cos(xu)\,du\).
Put \(\alpha_n=\pi n^2\). The endpoint derivatives are

\[
b_n=\phi_n'(0)=\alpha_ne^{-\alpha_n}P_1(\alpha_n),
\qquad
e_n=\phi_n^{(3)}(0)=\alpha_ne^{-\alpha_n}P_3(\alpha_n),
\]
\[
P_1(q)=-8q^2+30q-15,
\quad P_3(q)=-128q^4+1440q^3-4232q^2+3270q-375.
\]

Integration by parts, including the heat factor's endpoint derivatives, gives

\[
K_n(x)=-b_nx^{-2}+(e_n+6Tb_n)x^{-4}+O(x^{-6}),
\quad K_n'(x)=2b_nx^{-3}-4(e_n+6Tb_n)x^{-5}+O(x^{-7}).
\]

Consequently the value-slope matrix for n=1,2 has determinant

\[
\det\begin{pmatrix}K_1&K_2\\K_1'&K_2'\end{pmatrix}
=8\pi^2e^{-5\pi}P(\pi)x^{-7}+O(x^{-9}),
\]
\[
P(q)=-113400q+907200q^2-2570400q^3
+3081600q^4-1520640q^5+245760q^6.
\]

The rational check gives \(P(\pi)>0\). Choose an unbounded sequence of
sufficiently large X with \(H(T,X)\ne0\); such a sequence exists since
H(T,\(\cdot\)) is nonzero entire. Solve this matrix system with right side \(-(H(T,X),H_x(T,X))\).
The genuine theta transform and its slope are Schwartz; the inverse
matrix grows only polynomially. Thus its coefficient changes a_X,b_X
tend to zero faster than every inverse power of X. The source with
\(c_1=1+a_X,c_2=1+b_X\) is positive for large X and has an exact joint
zero at \((T,X)\), with a nonzero coefficient change and \(D_X>0\), while

\[
D_X^2=a_X^2w_1+(b_X-a_X)^2w_2+b_X^2w_3\longrightarrow0.
\tag{7}
\]

These are half-line/even-extension controls, not genuine modular sources.
They fail exact imaginary gluing and smooth modular reflection at the
origin: the same nonzero determinant makes the first and third odd
endpoint jets of the change independent, so they cannot both vanish.
They do show that no fixed positive defect tolerance can imply
physical nonvanishing at all real heights in the class used for (3).
The local theorem (6) is unaffected because these collisions move outside
its bounded domain. No effective threshold X is asserted.

## Boundary substitution identifies the required arithmetic compensation

Substitute the full source into the spherical Fueter boundary formula of
[Note 4](4_CAUCHY_FUETER_BOUNDARY_AND_CURRENT_REFORMULATIONS_20261014.md).
Each fixed-frequency integrand is already Fueter-regular; reproduction
acts before source integration. Thus the boundary radius cancels exactly.
For \(g_{n,t}(u)=e^{tu^2}\phi_n(u)\), the signed target is precisely

\[
\mathscr L_j(t,x)=\frac14\sum_{n,m\ge1}\iint_{(0,\infty)^2}
g_{n,t}(u)g_{m,t}(v)(uv)^j
\left[(u+v)^2\cos x(u-v)
+(-1)^j(u-v)^2\cos x(u+v)\right]du\,dv,
\quad j=0,1.
\tag{8}
\]

Full theta reflection forces
\(\sum_n\phi_n^{(2k+1)}(0)=0\) for every k. In particular
\(\sum_n b_n=0\). For each fixed n with b_n nonzero, the separate
channel has the eventually negative diagonal form

\[
\mathscr L_j(H_{n,t})
=-(j+2)((j+1)!)^2b_n^2x^{-2j-6}+O(x^{-2j-8}).
\tag{9}
\]

A diagonal-positive or first-index-dominance proof cannot supply a
global sign. Full off-diagonal compensation is essential. Finite
uncompensated theta truncations also introduce algebraic endpoint tails
that are absent from the complete Schwartz transform.

A concrete bounded-height refinement is to subtract those known odd
endpoint jets before truncating indices. For example, let
\(\beta_0(u)=ue^{-u^2}\), and define

\[
\widetilde g_n=g_{n,t}-b_n\beta_0,
\quad \sum_n\widetilde g_n=e^{tu^2}\Phi(u),
\quad \widetilde g_n'(0)=0.
\]

More generally subtract K odd jets using rapidly decreasing odd
\(\beta_k\) with \(\beta_k^{(2\ell+1)}(0)=\delta_{k\ell}\) for
k,\(\ell<K\), and set

\[
\widetilde g_n=g_{n,t}-\sum_{k=0}^{K-1}g_{n,t}^{(2k+1)}(0)\beta_k.
\]

Such test functions exist as odd polynomials times a Gaussian, by a
triangular jet interpolation. The full heated source has every odd
endpoint jet zero, so the complete compensated sum is still the original
source. The tail \(R_N=\sum_{n>N}\widetilde g_n\) then admits

\[
\left|\int_0^\infty u^jR_N(u)\cos(xu+j\pi/2)\,du\right|
\le |x|^{-2K}\bigl\|(u^jR_N)^{(2K)}\bigr\|_1,
\quad j=0,1,2,3,\quad x\ne0.
\tag{10}
\]

This is an integration-by-parts error bound retaining every omitted
theta index. The compensated individual channels need not satisfy heat
evolution; they are a signed quadrature decomposition at each real t.
No positivity of the adjusted channels is assumed. Finite K improves
bounded-height error control but still supplies algebraic, not global
physical-relative, bounds.

## Checks and next construction target

The [exact constant checker](../numerics/check_theta_gluing_defect_constants.py)
and [execution record](../numerics/THETA_GLUING_DEFECT_CHECKS_20261014.json)
verify (4), the polynomial determinant sign, and the transfers in (5)--(6).
The [internal review](../reviews/3_THETA_SPECIFIC_ESTIMATES_INTERNAL_REVIEW_20261014.md)
records the source-class and domain audit.

The central norm estimate and full-angular stability are established on
their stated domains. A collision-excluding estimate at unknown heights
still requires a complete signed control of (8), or a loss regular through
joint zeros, using the full arithmetic state. Neither absolute defect
stability nor Cauchy averaging supplies that remaining sign.
