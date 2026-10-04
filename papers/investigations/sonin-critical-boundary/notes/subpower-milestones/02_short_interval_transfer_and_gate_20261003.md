# A complete-cap short-interval transfer and its exponent budget

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and configured reasoning effort are not exposed and are not inferred.
Internal same-model research and analytic audit, not independent specialist review.

This continuation of the [subpower program](README.md) proves a useful arithmetic gate: a fixed relative power saving in an unconditional short-interval Chebyshev mean square transfers to the existing full-cap variance. The known Saffari–Vaughan input passes the range and endpoint tests but supplies only a subpower relative saving. It therefore does not establish a global delta below one. The limitation concerns the tested input and this absolute mean-square transfer; it does not exclude a sharper signed covariance argument.

## 1. Exact centering and the complete coordinate band

Use the existing real zero-extended weight w, supported in [A,B], where A=exp(-1/4), B=exp(1/4). Its established properties include

\[
\int_{\mathbb R}w(t)dt=0,\qquad \|w\|_2^2=1,\qquad w\in C_c^2(\mathbb R).
\]

Write

\[
V(x)=\sum_{n\ge2}\Lambda(n)w(n/x),\qquad
\mathcal V(X)=\int_X^{2X}|V(x)|^2dx.
\]

Let X be real and sufficiently large, and choose real h with 1<=h<=AX. Define the symmetric interval error

\[
D_h(t)=\psi(t+h/2)-\psi(t-h/2)-h,
\qquad
S_{A,B}(X,h)=\int_{AX}^{2BX}|D_h(t)|^2dt.
\]

The short-interval response is

\[
V_h(x)=\frac1h\int_{\mathbb R}w(t/x)D_h(t)dt,
\qquad X\le x\le2X.
\]

Finite Fubini gives the exact identity

\[
V_h(x)=\sum_{n\ge2}\Lambda(n)\overline w_{x,h}(n),\qquad
\overline w_{x,h}(n)=\frac1h\int_{-h/2}^{h/2}w((n+u)/x)du. \tag{1}
\]

Indeed the count in the difference of psi is over (t-h/2,t+h/2]; for each n its inverse set of t is [n-h/2,n+h/2), whose endpoints have zero Lebesgue measure. The density term is exactly zero because int w(t/x)dt=x int w=0. No integer rounding or additional centering error occurs, including noninteger X and h.

Every original response V(x) retains all integers Ax<=n<=Bx. Their union as x ranges over the complete shell is [AX,2BX], so both original physical caps remain. The approximation (1) also includes the expanded band [Ax-h/2,Bx+h/2]; these extra atoms are included in the error estimate below, rather than discarded.

## 2. An unconditional approximation error

Taylor's formula with integral remainder and symmetry of the u average imply, for every real n,

\[
|\overline w_{x,h}(n)-w(n/x)|
\le\frac{h^2}{24x^2}\|w''\|_\infty. \tag{2}
\]

The linear term integrates to zero. This uniform inequality also covers the two ends of the support because w is a C^2 zero extension. The difference vanishes outside the expanded coordinate band. Unconditional Chebyshev, psi(T)<=C_psi T for T>=2, therefore gives

\[
|V_h(x)-V(x)|
\le\frac{h^2}{24x^2}\|w''\|_\infty\psi(Bx+h/2)
\ll_g \frac{h^2}{x}.
\]

This bound takes the absolute value of every approximation error before summation; it requires no prime cancellation. Consequently

\[
\int_X^{2X}|V_h(x)-V(x)|^2dx\ll_g h^4/X. \tag{3}
\]

## 3. The short-interval mean-square gate

Cauchy–Schwarz, int w(t/x)^2dt=x, and support in [Ax,Bx] yield

\[
|V_h(x)|^2
\le \frac{x}{h^2}\int_{Ax}^{Bx}|D_h(t)|^2dt
\le\frac{x}{h^2}S_{A,B}(X,h).
\]

Integrating x over the whole shell and combining with (3) gives

\[
\boxed{\mathcal V(X)\ll_g
\frac{X^2}{h^2}S_{A,B}(X,h)+\frac{h^4}{X}.} \tag{4}
\]

All quantities here use the actual von Mangoldt weights. The gate is unconditional, uniform in the displayed real-X/h range, and includes every original cap and every extra atom introduced by averaging.


An explicit version uses the already proved Chebyshev constant C_psi=4 log 2 from [selective-loss note 05](../selective-loss-program/05_quadratic_target_and_finite_sign_20261003.md), equation (6). Set

\[
C_{\rm app}=\frac{(4\log2)(B+A/2)}{24}\|w''\|_\infty.
\]

Then |V_h(x)-V(x)|<=C_app h^2/x, and the integral of its square is at most C_app^2 h^4/(2X). Using |a+b|^2<=2|a|^2+2|b|^2 gives

\[
\boxed{\mathcal V(X)\le
\frac{3X^2}{h^2}S_{A,B}(X,h)+C_{\rm app}^2\frac{h^4}{X}.}
\tag{4a}
\]

If a direct estimate for the signed projection is available, define Q_h(X)=integral_X^{2X}|V_h(x)|^2 dx. The reverse triangle inequality gives

\[
\boxed{\left|\sqrt{\mathcal V(X)}-\sqrt{Q_h(X)}\right|
\le C_{\rm app}\frac{h^2}{\sqrt{2X}}.}
\tag{4b}
\]

At h=X^(3/4), this norm error is C_app X/sqrt(2). Hence, for every fixed delta>=0,

\[
Q_{X^{3/4}}(X)=O(X^{2+\delta})
\quad\Longleftrightarrow\quad
\mathcal V(X)=O(X^{2+\delta}).
\tag{4c}
\]

This is an equivalence of growth bounds, not equality of leading coefficients. Finite Fubini also gives the complete signed covariance

\[
Q_h(X)=\frac1{h^2}\int_{AX}^{2BX}\int_{AX}^{2BX}
D_h(t)D_h(u)W_X(t,u)\,dt\,du,
\quad W_X(t,u)=\int_X^{2X}w(t/x)w(u/x)dx.
\tag{4d}
\]

The kernel is positive as a Gram form, while its cross terms retain their signs. A bound for this projection can be a weaker hypothesis than a bound for the raw S mean square. These identities introduce no new arithmetic power saving by themselves.

For h=X^tau, 0<tau<1, a candidate input

\[
S_{A,B}(X,h)\ll Xh^2 X^{-\kappa}L(X),
\qquad \kappa>0,\quad L(X)=X^{o(1)}, \tag{5}
\]

would give

\[
\mathcal V(X)\ll_g X^{3-\kappa}L(X)+X^{4\tau-1}. \tag{6}
\]

Hence it proves every delta>max(0,1-kappa,4tau-3). When 4tau-1<=3-kappa, the absolute approximation error is subordinate. An unbounded L does not justify the endpoint delta=1-kappa. For example, tau=3/4 makes the approximation O(X^2), so any kappa in (0,1] survives at the corresponding open exponent. The candidate (5) is not proved here.

## 4. Primary-source audit of the available arithmetic input

Primary source: Saffari–Vaughan, *On the fractional parts of x/n and related sequences. II*, Ann. Inst. Fourier 27(2) (1977), [publisher PDF](https://aif.centre-mersenne.org/item/10.5802/aif.649.pdf).

Lemma 5 (6.2), printed page 19, assumes N(sigma,T)<<T^{C(1-sigma)}(log T)^B, C>=2, T>=2; only 1/2<=sigma<=1 is needed here. Lemma 6 (6.19), page 24, gives h^2 U exp[-c(log U/loglog U)^{1/3}] for the additive theta mean square when U>=3 and U^{1-2/C+epsilon}<h<=U, with fixed epsilon>0. The proof first establishes the relative psi version in (6.12)–(6.18), concluding immediately before section 6.2 on page 24; its additive averaging argument (6.21), page 25, applies identically to psi. Page 28 invokes Huxley's unconditional C=12/5, giving the range U^{1/6+epsilon}<h<=U. The RH alternatives are (6.4), (6.20).

These original formulas were checked visually against the downloaded PDF. The lemma statements use theta; the psi version comes from their proof.

For completeness, the additive psi transfer can be proved directly. Write I(u,v)=psi(u+v)-psi(u)-v. For 2h<=v<=3h,

\[
I(u,h)=I(u,v)-I(u+h,v-h).
\]

Square with |a-b|^2<=2|a|^2+2|b|^2, integrate u over [U,2U] and v over [2h,3h], and suppose h<=U/6. Both resulting bands are contained in u in [U,3U], v in [h,3h]. Changing v=theta u then gives

\[
h\int_U^{2U}|I(u,h)|^2du
\le12U\int_{h/(3U)}^{3h/U}\int_U^{3U}|I(u,\theta u)|^2du\,d\theta. \tag{7}
\]

Cover [U,3U] by [U,2U] and [2U,4U]. Whenever the source's relative psi bound holds uniformly on this theta band at both base points, (7) implies

\[
\int_U^{2U}|I(u,h)|^2du
\ll\frac{U}{h}U^3 r(U)\int_{h/(3U)}^{3h/U}\theta^2d\theta
\ll Uh^2 r(U),
\quad r(U)=\exp[-c(\log U/\log\log U)^{1/3}].
\]

For the specific h=X^{3/4} and U a fixed multiple of X, the smallest theta is comparable to X^{-1/4}, comfortably above the relative theorem's U^{-3/4} threshold when epsilon=1/12 and C=12/5. The largest theta tends to zero. Thus this derivation verifies the required psi estimate directly, without treating the prime-only lemma statement as a psi statement.

To apply the psi estimate here, substitute u=t-h/2. The resulting integration band is [AX-h/2,2BX-h/2], contained in [AX/2,2BX] for h<=AX. It is covered by the three dyadic intervals [U_j,2U_j], U_j=2^j AX/2, j=0,1,2, because 4AX>2BX. Thus no endpoint strip is omitted. With h=X^{3/4}, choose, for example, epsilon=1/12; all U_j are fixed multiples of X, and the source range U_j^{1/4}<h<=U_j holds for all sufficiently large real X. Summing their nonnegative interval integrals gives

\[
S_{A,B}(X,X^{3/4})\ll_g
Xh^2\exp[-c_g(\log X/\log\log X)^{1/3}]. \tag{8}
\]

Constants and the starting threshold are allowed to depend on the fixed weight and epsilon. There is no exceptional-set contribution to discard: the cited result already estimates the complete mean square.

Substituting (8) into the proved gate (4) yields

\[
\boxed{\mathcal V(X)\ll_g
X^3\exp[-c_g(\log X/\log\log X)^{1/3}]+X^2.} \tag{9}
\]

The exponent delivered is delta=1. The relative saving is X^{-o(1)}, not X^{-\kappa} for any fixed positive kappa, since (log X/loglog X)^{1/3}=o(log X). This audited route does not improve the stronger Johnston–Yang baseline already transferred in the subpower program.

## 5. What zero density does and does not buy in this audit

Changing the density exponent C changes the admissible length threshold 1-2/C. It does not, by itself, change the tested estimate's subpower relative factor into a fixed power saving. A density upper bound that grows with T permits a fixed number of zeros arbitrarily close to Re s=1; it is not a fixed zero-free strip. The source's zero-free input (6.17) has width tending to zero with height and leads to the factor in (8).

For this prepared probe, the project's noncancellation theorem already proves that a global variance exponent below three would exclude a fixed right-hand strip of zeros. A high fixed zero cannot be ignored because its transformed coefficient is small: that coefficient remains nonzero and its exponential mode matters at sufficiently large X. The mean-square gate can test stronger arithmetic inputs, but the audited density/short-interval theorem supplies no such new zero-location information. No claim is made that all signed short-interval covariance methods must fail.

## 6. Recommended next obligation

Keep (4a) as a reusable exponent test. Before pursuing a new short-interval result, require either (5) with a genuine fixed kappa after centering and all bands, or a direct estimate of the exact signed covariance (4d) that improves on the absolute Cauchy–Schwarz step. Formula (4c) shows exactly how the signed covariance would translate to delta. Shorter admissible intervals, almost-all asymptotics, or stronger logarithmic factors alone do not pass the raw mean-square gate. In particular, tau=3/4 separates the arithmetic issue from support and approximation errors: all those errors are already on the X^2 scale.

Related local records: [selective-loss note 09](../selective-loss-program/09_actual_error_projection_and_frequency_20261003.md), sections 2 and 4–6; [selective-loss note 06](../selective-loss-program/06_global_mechanism_tests_20261003.md), section 7; and the [baseline note](01_baseline_and_exponent_budget_20261003.md), sections 1 and 3. This note provides a new transfer calculation and an input limitation, not a proved subunit delta or an exponent-descent rule.
