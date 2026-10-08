# A carrier centered full von Mangoldt spectral reduction

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model analysis and cross-review are internal checks, not
independent specialist refereeing or formal proof verification.
Repository base: `62ac139771ae317f6e4b624765783c6856739d8f`, with the
existing working-tree investigation notes read in their current state.

This note gives an exact carrier-centered complex signed correlation for
the original prepared scalar, an entire spectral-tail estimate, and an
effective density-cancellation remainder. It combines these deductions
with the existing effective Vaughan comparison. The retained arithmetic
inequality is open. The spectral constant can be bounded using fixed-kernel
norms but has not been numerically evaluated; this is not a completed
numerical detector certificate or a new zero-free region.

## Definitions and inherited comparison

Use the fixed zero extension of \(h(v)=(1-16v^2)^8\) on
\([-1/4,1/4]\), \(T=|t|\ge100\), \(q=7/3\),
\(A=e^{-1/4}\), \(C=2e^{1/4}\), and the existing normalization
\(N_t=\|-h_t'''+h_t'/4\|_2\), where \(h_t=e^{itv}h\).
The [height-uniform comparison](../gaussian_localization/HEIGHT_UNIFORM_VAUGHAN_REDUCTION_20261004.md)
proves the following identities and derivative estimates. Define

\[
A_t(v)=\frac{-h'''-3it h''+(3t^2+1/4)h'
                  +i(t^3+t/4)h}{N_t},\qquad
a_t(u)=u^{-1/2}A_t(-\log u),
\]
\[
L_t(u)=\int_1^2y a_t(u/y)\,dy,\qquad
\ell_t(u)=u^{-it}L_t(u),\qquad
D_t(s)=\frac1q\int\ell_t(u)u^{s-1}\,du.
\tag{1}
\]

Preparation gives \(D_t(1)=0\). With
\(K(s)=(2^{s+2}-1)/(s+2)\) and
\(c_t=\int w_t(u)\log u\,du\), the exact continuum is

\[
c_tK(1-it)=\int\ell_t(u)\log u\,du=qD_t'(1).
\tag{2}
\]

Take real \(U\ge2\) and \(U^2\le AX\), and put

\[
H=X/U^2,\qquad Z=CX/U,\qquad Y=X/U,\qquad
A_U(m)=\sum_{d\mid m,\ d>U}\mu(d),\quad
M_1(U)=\sum_{d\le U}\mu(d)/d.
\]

All lower arithmetic cutoffs are strict; upper caps are weak.
No real parameter is rounded inside a kernel or integral. The full
von Mangoldt comparison is

\[
\mathcal J_t(X;U)=D_t'(1)M_1(U)
 +\frac1{qX}\sum_{m>U,n>U}A_U(m)\Lambda(n)\ell_t(mn/X),
\]
\[
|\lambda_t(X)-\mathcal J_t(X;U)|
\le E_V:=2^{59}T^7X^{-7}
       [(1+\log X)U^7+U^{14}].
\tag{3}
\]

The hypotheses of the saved comparison hold: \(U\le X\) and
\(U<AX\) follow from \(U\ge2\) and \(U^2\le AX\).
The full support \(AX\le mn\le CX\) and every terminal
partial block remain in (3). Every prime power remains in \(\Lambda\).

## Exact cancellation of the density

Set \(\psi(x)=\sum_{n\le x}\Lambda(n)\) and
\(E_\psi(x)=\psi(x)-x\), with right-continuous values. Define

\[
P_t(v)=\int_v^\infty\ell_t(s)\,ds,\qquad f_t(v)=P_t(v)/v.
\]

Both functions have support in \([A,C]\), since \(\int\ell_t=0\).
Integration by parts gives \(\int f_t=qD_t'(1)\). Splitting
\(d\psi=dx+dE_\psi\) in (3) yields exactly

\[
\mathcal J_t=Q_t+R_t,
\qquad Q_t=\frac1{qX}\sum_{m>U}A_U(m)
       \int_{(U,\infty)}\ell_t(mx/X)\,dE_\psi(x),
\tag{4}
\]
\[
R_t=-\frac1{qY}\sum_{d\le U}\mu(d)r_{f_t}(Y/d),\qquad
r_{f_t}(y)=\sum_{k\ge1}f_t(k/y)-y\int f_t.
\tag{5}
\]

To see the sign and the cancellation, the density term is
\(q^{-1}\sum_{m>U}A_U(m)P_t(m/Y)/m\).
For \(m>U\), complementing divisors gives
\(A_U(m)=-\sum_{d\mid m,d\le U}\mu(d)\).
The added terms \(m\le U\) vanish because \(m/Y\le U^2/X\le A\).
Thus the density is
\(-[qY]^{-1}\sum_{d\le U}\mu(d)\sum_k f_t(dk/Y)\).
Its continuum is exactly \(-D_t'(1)M_1(U)\), leaving (5).
The continuum was canceled by an exact identity, rather than dropped.

The saved derivative bounds imply a new effective remainder bound.
They give \(\|D^j\ell_t\|_{\rm TV}\le3\,2^{67}T^j\) for
\(0\le j\le6\), and \(\|D^7\ell_t\|_{\rm TV}\le2^{74}T^7\).
Product differentiation gives

\[
\|D^8 f_t\|_{\rm TV}\le
8!A^{-9}\|P_t\|_1
+\sum_{j=0}^6\frac{8!}{(j+1)!}A^{-(8-j)}
                  \|D^j\ell_t\|_{\rm TV}
+A^{-1}\|D^7\ell_t\|_{\rm TV}.
\tag{6}
\]

Here \(\|P_t\|_1<(C-A)\|\ell_t\|_1<9\,2^{67}\).
The first term is below \(2^{90}<2^{67}T^7\). In the middle sum,
successive terms in descending \(j\) have ratio at most
\(7/(AT)<7/75\). Its coefficient sum is therefore below
\(16T^6\); the contribution is below
\(48\,2^{67}T^6<2^{67}T^7\). The last term is below
\((4/3)2^{74}T^7\). Consequently

\[
\|D^8 f_t\|_{\rm TV}<2^{75}T^7,
\qquad |r_{f_t}(y)|\le
\frac{\|D^8 f_t\|_{\rm TV}}{1209600}y^{-7},
\]
\[
\boxed{|R_t|<2^{54}T^7H^{-8}.}
\tag{7}
\]

The eighth-order Poisson constant is
\(2\zeta(8)/(2\pi)^8=1/1209600<2^{-20}\), and \(q>2\).
These arguments use total variation for complex measures. They do not
assume infinite smoothness. The primitive gains the derivative needed
for the eighth-order calculation; its highest input is \(D^7\ell_t\).

## The exact spectrum centered at the carrier

Aggregate the cofactor before inversion:

\[
\mathscr K_t(v)=\sum_{k\ge1}\ell_t(kv),\qquad
B_t(z)=\int_A^C L_t(u)u^{z-1}\,du.
\]

For each fixed \(t\), seventh-order Poisson summation gives
\(\mathscr K_t(v)=O_t(v^6)\) as \(v\downarrow0\), and
\(\mathscr K_t=0\) for \(v\ge C\). Its Mellin transform,
continued from \(\Re s>1\), is

\[
\int_0^C\mathscr K_t(v)v^{s-1}\,dv
       =\zeta(s)B_t(s-it),\qquad \Re s>-6.
\tag{8}
\]

There is a removable pole at \(s=1\), since
\(B_t(1-it)=\int\ell_t=0\). Define the continued multiplier
\(W_t(\xi)=\zeta(1+i\xi)B_t(1+i(\xi-t))\). Its value is

\[
W_t(0)=B_t'(1-it)=c_tK(1-it)=qD_t'(1).
\tag{9}
\]

Set \(\mathcal L=1+\log(Z/U)\), \(\mathsf L=1+\log Z\),
and define finite transforms

\[
\mathcal M_t(\nu)=\sum_{U<d\le Z}\frac{\mu(d)}d
                 (d/U)^{-it}(d/U)^{-i\nu},
\]
\[
\mathcal E_t(\nu)=\sum_{U<n\le Z}\frac{\Lambda(n)}n
                 (n/U)^{-it}(n/U)^{-i\nu}
 -\int_0^{\log(Z/U)}e^{-i(t+\nu)x}\,dx.
\tag{10}
\]

Using \(A_U=\mu_{>U}*1\) in (4) and then Mellin inversion gives

\[
\boxed{Q_t=\frac{e^{it\log H}}{2\pi q}\int_{\mathbb R}
 W_t(t+\nu)e^{i\nu\log H}
       \mathcal M_t(\nu)\mathcal E_t(\nu)\,d\nu.}
\tag{11}
\]

Both variables in the pre-inversion Stieltjes formula
\([qX]^{-1}\sum_{d>U}\mu(d)\int_{(U,\infty)}
\mathscr K_t(dx/X)\,dE_\psi(x)\)
may be capped at \(Z\). At either upper equality the product is at
least \(C\), so the kernel is zero. Lower atoms at \(U\) remain
excluded. Inversion is justified by absolute convergence of the
multiplier and finite total variation of the capped arithmetic measure.
Thus product endpoints are dealt with before spectral truncation.

The integral is a signed product of two complex transforms. It has no
fixed-carrier negative-frequency conjugacy and no automatic positivity.
Replacing \(\mathcal M_t\mathcal E_t\) by an absolute square, doubling
the positive half-line, or omitting \(e^{it\log H}\) changes the scalar.

## Uniform treatment of the removable pole

The coefficients of \(A_t\) in the four fixed functions
\(h,h',h'',h'''\) have sum of absolute values below four.
The sixth measure derivative of \(a_t\), and the seventh measure
derivative of \(L_t\), therefore have carrier-independent bounds.
For the latter use

\[
L_t'(u)=2L_t(u)/u+[a_t(u)-4a_t(u/2)]/u.
\]

In logarithmic coordinates \(F_t(x)=e^xL_t(e^x)\), both
\(D^7F_t\) and \(D^7(xF_t)\) are finite measures with uniform
variation bounds. Fourier integration by parts gives

\[
|B_t(1+i\nu)|+|B_t'(1+i\nu)|
       \le C_h(1+|\nu|)^{-7}.
\tag{12}
\]

The constant can be obtained from the zeroth and seventh variation
norms of the finitely many fixed amplitude kernels. It has not been
numerically evaluated in this opening note.

For \(|\xi|\ge1\), Euler summation gives
\(|\zeta(1+i\xi)|\ll\log(2+|\xi|)\). For \(|\xi|\le1\),
\(\zeta(1+i\xi)-1/(i\xi)\) is bounded and

\[
B_t(1+i(\xi-t))
=i\xi\int_0^1B_t'(1+i(\theta\xi-t))\,d\theta.
\]

The frequencies \(\theta\xi-t\) and \(\xi-t\) differ by at most
one, so (12) applies with an absolute comparison factor. This proves
the global bound, including the continued value at \(\xi=0\),

\[
\boxed{|W_t(t+\nu)|\le C_{\rm sp}
    \log(2+|t+\nu|)(1+|\nu|)^{-7}.}
\tag{13}
\]

There is no polynomial height loss in (13); the explicit logarithmic
height dependence remains. The pole lies at \(\nu=-t\), rather than
at the center of the new band.

## The entire discarded spectral range

For any interval \(I\) of length \(B\ge1\) and coefficients
\(|b_n|\le b\), the elementary finite-polynomial estimate is

\[
\int_I\left|\sum_{U<n\le Z}\frac{b_n}n(n/U)^{-i\nu}\right|^2
 d\nu\ll b^2(B/U+\mathsf L\mathcal L).
\tag{14}
\]

The diagonal is bounded by \(b^2B\sum_{n>U}n^{-2}\ll b^2B/U\).
Each pair is bounded using \(2/\log(n/m)\) and
\(\log(n/m)\ge(n-m)/n\). Summing \(1/(m(n-m))\) bounds all
off-diagonal terms by \(O(b^2\mathsf L\mathcal L)\).
The location of \(I\) and coefficient phases do not enter the bound.
Thus carrier twists can be retained without paying a power of \(T\).

Apply (14) to \(\mu(n)\) and \(\Lambda(n)\), using
\(|\Lambda(n)|\le\log Z\). Cauchy–Schwarz bounds their product
integral by \(O(\mathsf L(B/U+\mathsf L\mathcal L))\).
The density transform in (10) must instead be handled with

\[
\int_{\mathbb R}\left|\int_0^{\log(Z/U)}
             e^{-i(t+\nu)x}\,dx\right|^2d\nu
                   =2\pi\log(Z/U).
\tag{15}
\]

This is Plancherel, invariant under the frequency shift. Its product
with \(\mathcal M_t\) on \(I\) is at most
\(O(((B/U+\mathsf L\mathcal L)\mathcal L)^{1/2})\), absorbed
by the preceding bound. The unshifted shortcut \(2/|\nu|\) would
be invalid near \(\nu=-t\).

For \(\Omega\ge1\), let \(\mathcal C_{t,\Omega}(X;U)\) denote
(11) with integral over \([-\Omega,\Omega]\). Multiplying (13)
by these product bounds on positive and negative dyadic intervals gives

\[
\boxed{|Q_t-\mathcal C_{t,\Omega}|
\le E_{\rm sp}:=C_*\log(2+T+\Omega)
 \left[\frac{\mathsf L}{U}\Omega^{-6}
       +\mathsf L^2\mathcal L\Omega^{-7}\right].}
\tag{16}
\]

Here \(C_*\) depends only on the fixed probe and absolute elementary
constants, and is independent of \(t,X,U,\Omega\). Dyadic logarithms
grow at most linearly with the dyadic index and are absorbed by the
convergent geometric sums. Equation (16) pays for the entire tail,
including a pole neighborhood outside the central band.
The constant is constructive but has not been numerically evaluated.

## A conditional interface on the saved detector interval

Combining (3), (7), and (16) gives the uniform comparison

\[
\boxed{|\lambda_t(X)-\mathcal C_{t,\Omega}(X;U)|
 \le E_V+2^{54}T^7H^{-8}+E_{\rm sp}.}
\tag{17}
\]

For the existing scalar detector, take integer \(N\ge10\),
\(T+1<e^N\), \(a_N=(8e)^{-N}/256\),
\(24(N+1)\le\log X\le208N\), and \(r=a_NX^{-1/4}\).
The saved cutoff is

\[
U=2^{-5}\sqrt{X/T}\,r^{1/14},\qquad
H=2^{10}T r^{-1/7}.
\]

The existing note proves all cutoff hypotheses and \(E_V\le2^{-10}r\).
The new density calculation gives

\[
|R_t|<2^{-26}T^{-1}r^{8/7}<2^{-32}r.
\tag{18}
\]

Choose a cap with \(E_{\rm sp}\le\varepsilon r\), where
\(0<\varepsilon<1-2^{-10}-2^{-32}\). Such a finite cap exists
by (16). A sufficient independent arithmetic inequality is then

\[
|\mathcal C_{t,\Omega}(X;U)|
\le(1-2^{-10}-2^{-32}-\varepsilon)r
\tag{19}
\]

for every carrier and continuous physical scale required by the saved
detector. To invoke that detector, also require
\(N\ge\max(10,\lceil\mathcal Q(T)\rceil)\) throughout the carrier
band, where \(\mathcal Q\) is its prescribed guard-band zero-count
upper bound. It would imply \(|\lambda_t(X)|\le r\) on that interval.
The Gaussian detector's remaining hypotheses and scope must still be
used exactly as stated in the
[explicit finite-window note](../gaussian_localization/EXPLICIT_CONSTANTS_AND_FINITE_WINDOW_20261004.md).
No such arithmetic bound or numerical choice of the spectral cap is
established here. Identities hold pointwise for real moving cutoffs;
no fixed-cutoff Mellin transform is reused with \(U=U(X)\).

## Verification and remaining work

The [internal review](../../../reviews/height_adapted_zero_detection/arithmetic_centered_at_carrier/INITIAL_REVIEW_20261004.md)
checks the exact continuum, density sign and effective bound, both
carrier twists, pole continuation, full-\(\Lambda\) factor, endpoints,
and translated mean-square argument. The
[numerical checks](../../../numerics/height_adapted_zero_detection/arithmetic_centered_at_carrier/README.md)
test finite algebra with complex polynomial kernels and formal prime-log
coefficients, rational constant budgets, and floating phase identities.
They do not numerically certify Mellin inversion, the global analytic
tail, the true prepared kernel norms, or a signed arithmetic saving.

The next calculation is to evaluate \(C_*\) and then attempt a complete
signed block estimate for (19). Preserve the density, both factor ranges,
and terminal product caps. The inherited
[arithmetic closure audit](../../programs/01_signed_arithmetic_covariance/ARITHMETIC_CLOSURE_ATTEMPT_20261004.md)
shows that exact identities transmit coherent zero modes; factoring out
the carrier does not supply cancellation beyond those identities.
