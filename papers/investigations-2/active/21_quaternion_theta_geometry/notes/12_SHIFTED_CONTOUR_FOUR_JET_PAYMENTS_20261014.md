# Shifted-contour payments at arbitrary heights

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
The parent session verified its current recorded configuration; this
analytic subtask inherits that configuration.

This note removes one computational obstruction in Notes 8--10. A fixed
compensated theta truncation gives an algebraic absolute error while the
physical observation can be exponentially small. The complete even
source admits a contour shift whose four-jet errors carry the same
exponential factor as the usual gamma scale. The resulting estimates are
absolute after an explicit normalization. They do **not** prove the
remaining stationary sign or a positive lower bound for the observation.

## 1. The complete-source contour identity

Write alpha_n=pi n^2 and

\[
\phi_n(z)=(2\alpha_n^2e^{9z}-3\alpha_ne^{5z})
e^{-\alpha_ne^{4z}},\qquad \Phi(z)=\sum_{n\ge1}\phi_n(z).
\]

This series and all its derivatives converge normally on compact subsets
of the strip |Im z|<pi/8. To verify evenness there, set
Theta(z)=exp(z) theta(exp(4z)), where
theta(s)=sum_(n in Z) exp(-pi n^2 s). Jacobi's theta transformation gives
Theta(z)=Theta(-z), and direct differentiation gives

\[
\Phi(z)=\frac1{16}(\Theta''(z)-\Theta(z)).
\tag{1}
\]

Consequently Phi is even in this strip and satisfies Schwarz reflection.
In particular Phi(iy) is real for real |y|<pi/8. These statements concern
the complete source; the individual phi_n are not even.

Let h_k=partial_x^k H, 0<=t<=tau, tau<=1/2, x>=0, and
0<a<pi/8. For every integer k>=0, Cauchy's theorem gives

\[
\boxed{h_k(t,x)=e^{-ax}\Re\int_0^\infty
(i(u+ia))^k e^{t(u+ia)^2}\Phi(u+ia)e^{ixu}\,du.}
\tag{2}
\]

Indeed the omitted left vertical segment has parametrization z=iy.
Every factor in (iz)^k exp(tz^2)Phi(z)exp(ixz) is then real, whereas
dz=i dy. Its real part is zero for every k. The right vertical segment
tends to zero: cos(4y)>=cos(4a)>0 on that segment, and the source's
double exponential decay dominates every polynomial and exp(tR^2).
This also justifies every differentiated half-line integral.

No vertical-segment cancellation is asserted for a finite raw theta
sum. Formula (2) is established for the complete source first, and the
horizontal source is then truncated with a paid error.

## 2. An explicit complete-index payment

Put c=cos(4a)>0, m=N+1, alpha=pi m^2, beta=c alpha, and

\[
\rho=\left(\frac{m+1}{m}\right)^4
e^{-\pi c(2m+1)},\qquad \lambda=4\beta-9,
\]
\[
S_k(\lambda,b)=\sum_{r=0}^k
\binom kr b^{k-r}\frac{r!}{\lambda^{r+1}}.
\tag{3}
\]

Assume rho<1, lambda>0, and 8 beta>=tau. The contribution of all
indices n>=m to (2) has absolute value at most

\[
\boxed{E_{N,k}=e^{-ax}
\frac{(2\alpha^2+3\alpha)e^{-\beta}}{1-\rho}
S_k(\lambda,a).}
\tag{4}
\]

For n>=m the ratios of alpha_n^r exp(-c alpha_n exp(4u)), r=1,2,
are at most rho, uniformly for u>=0. Also

\[
|e^{t(u+ia)^2}|\le e^{\tau u^2},\qquad
|u+ia|^k\le(u+a)^k,
\]
\[
\tau u^2+9u-\beta e^{4u}
\le-\beta-(4\beta-9)u-(8\beta-\tau)u^2
\le-\beta-\lambda u.
\tag{5}
\]

The first inequality uses exp(4u)>=1+4u+8u^2. Bounding exp(5u)
by exp(9u), summing the geometric index series, and integrating (5)
proves (4). It pays the entire omitted theta sum on the whole horizontal
half-line, for every t in the stated interval. Dropping exp(-ta^2)<=1
only makes the payment larger.

## 3. A complete integration-tail payment

Fix U>=0 and put

\[
b=\pi c e^{4U},\quad
\rho_U=16e^{-3b},\quad
\lambda_U=4b-9-2\tau U,\quad
L_U=\tau U^2+9U-b.
\tag{6}
\]

Assume rho_U<1, lambda_U>0, and 8b>=tau. The contribution of the
**entire** theta source on u>=U in (2) is at most

\[
\boxed{E_{U,k}=e^{-ax}
\frac{(2\pi^2+3\pi)e^{L_U}}{1-\rho_U}
S_k(\lambda_U,U+a).}
\tag{7}
\]

For u>=U the index ratios are at most rho_U, using their largest
possible value at n=1 and u=U. For
L(u)=tau u^2+9u-pi c exp(4u), one has L''(u)<=0 on this half-line,
and L'(U)=-lambda_U. Hence
L(U+v)<=L_U-lambda_U v. Integrating (U+a+v)^k proves (7).

Therefore the finite approximation

\[
P_{N,U,k}(t,x;a)=e^{-ax}\Re\int_0^U
(i(u+ia))^k e^{t(u+ia)^2}
\sum_{n=1}^N\phi_n(u+ia)e^{ixu}\,du
\tag{8}
\]

satisfies |h_k-P_(N,U,k)|<=E_(N,k)+E_(U,k). The bounds deliberately
overpay the intersection n>N,u>U. A validated finite quadrature radius
is added separately. This statement applies in particular to all four
jets k=0,1,2,3 required by the stationary Laguerre forms.

## 4. A moving contour with explicit gamma-scale errors

For x>=41 choose

\[
a_x=\frac\pi8-\frac1x,\qquad c_x=\sin(4/x).
\tag{9}
\]

Then 0<a_x<pi/8, c_x>=2/x, and
exp(-a_x x)=e exp(-pi x/8). With ell=log x and any fixed p>0, take

\[
m=\left\lceil\sqrt{\frac{x}{2\pi}(p\ell+32)}\right\rceil,
\quad N=m-1,\qquad
U=\frac{\ell+2\log(\ell+8)}4.
\tag{10}
\]

Here beta>=p ell+32 and m^2>=2x/pi. Since
log(1+1/m)<=1/m,

\[
-\log\rho\ge\frac{4\pi m}{x}-\frac4m
\ge\frac{2\pi m}{x},\qquad
\frac1{1-\rho}\le1+\frac{x}{2\pi m}.
\tag{11}
\]

All hypotheses of (4) hold. In particular, for every fixed k,

\[
e^{\pi x/8}E_{N,k}
=O\!\left(x^{5/2-p}(\log x)^{3/2}\right),\qquad x\to\infty.
\tag{12}
\]

The constant may depend on p and k. The growing geometric denominator
has been included: treating 1/(1-rho) as an absolute constant would give
an incorrect power of x. To obtain a specified polynomial error after
normalization, increase p accordingly.

The complete integration tail in (7) is smaller than every negative
power of x after the same normalization. Indeed
b>=2pi(ell+8)^2 and U<=ell/2+2. Using pi>3 and tau<=1/2 gives

\[
L_U\le-\frac{47}{8}\ell^2-\frac{181}{2}\ell-364.
\tag{13}
\]

The hypotheses rho_U<1, lambda_U>0, 8b>=tau are immediate from these
same bounds, while S_k(lambda_U,U+a_x) grows at most polynomially in
ell. Equations (9)--(13) thus provide a genuinely all-height family of
**absolute** four-jet payments at the exp(-pi x/8) scale. The source
cutoff and integration domain both vary explicitly; no fixed truncation
is silently reused at arbitrary heights.

One must form each physical jet by (2) with x fixed and only then select
a=a_x. Differentiating the finite adaptive approximation (8) introduces
derivatives of a_x, N(x), and U(x); that is not a way to obtain its
physical jets. If C_k=exp(pi x/8)h_k, the correct exact relations are

\[
\partial_t C_k=-C_{k+2},\qquad
\partial_x C_k=C_{k+1}+\frac\pi8 C_k.
\tag{14}
\]

For a whole spatial cell [X,Y], 41<=X<Y, freeze the contour at a_Y
and choose N,U from (10) with x=Y. All hypotheses then hold uniformly
on the cell, and the normalized exponential prefactor is
exp((pi/8-a_Y)x)=exp(x/Y)<=e. Thus the same payment formulas at Y
give uniform normalized four-jet bounds on the complete closed cell.
The retained finite integral still needs validated interval or Taylor
evaluation in t,x. This freezing avoids differentiating an adaptive
cutoff and makes overlapping finite-cell implementations explicit.

## 5. What remains for stationary signs

Because the normalization is positive, genuine stationary conditions
are C_1=0 and C_2=0, respectively, and

\[
\mathscr L_j(H)=e^{-\pi x/4}
(C_{j+1}^2-C_jC_{j+2}).
\tag{15}
\]

Suppose validated quadrature gives paid normalized jets
|C_k-p_k|<=epsilon_k. At a genuine stationary point C_(j+1)=0,

\[
\mathscr L_j(H)\ge e^{-\pi x/4}
\left[-p_jp_{j+2}-|p_j|\epsilon_{j+2}
-|p_{j+2}|\epsilon_j-\epsilon_j\epsilon_{j+2}\right].
\tag{16}
\]

To use a retained finite Laguerre expression instead, also subtract
epsilon_(j+1)^2 as in Note 8. This is a signed target with explicit
error payments, not a proof that its right-hand side is positive.
No division by |F|, H, a curvature, or an unknown stationary amplitude
has been introduced.

The new family is suitable for arbitrarily high **finite** validated
cells and can replace fixed-order compensation there. A global conclusion
still requires a theta-specific stationary estimate valid at every
possible collision height, an equivalent locally bounded-loss estimate,
or an analytic coverage theorem controlling every moving cell. Numerical
payments and finite replay cannot establish either missing assertion.

The accompanying
[checker](../numerics/check_shifted_contour_payments.py) and
[small execution record](../numerics/SHIFTED_CONTOUR_PAYMENT_CHECKS_20261014.json)
verify all payment hypotheses and numerical sizes in 256-bit Arb/Acb
arithmetic with python-flint 0.9.0. With p=12, the sampled heights
41,100,1000,10^6,10^12 require N=22,37,135,5610,7606860, respectively;
the last figures only evaluate the analytic tail formulas, not millions
of source terms. The k=0 normalized index payments range from below
1.18*10^(-66) at height 41 to below 5.22*10^(-287) at height 10^12.
All four jet payments are stored separately.

Eight paid shifted and unshifted four-jet enclosures agree at x=41,
t=0,1/2 using N=8,U=3/2,a=pi/16 for the shifted route. Every normalized
finite-quadrature radius is below 8.8*10^(-54), with the analytic omitted
domains paid separately. These comparisons test the implementation;
they are not stationary sign certificates or all-height evaluations.
