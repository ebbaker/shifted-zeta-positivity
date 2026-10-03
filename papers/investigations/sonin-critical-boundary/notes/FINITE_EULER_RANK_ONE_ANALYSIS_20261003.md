# First-prime boundary analysis: full leakage Grams and residual control

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning
effort are not exposed. This is an internal analytic derivation with a
floating-point formula check, not independent specialist refereeing or a
numerical sign certificate.

This continues the rank-one question in
[the boundary identity note, equation (21)](FINITE_EULER_BOUNDARY_IDENTITY_20261003.md).
It does **not** settle that question. Its concrete result is an explicit
finite-matrix route to bounding the *full* residuals in
[the boundary residual certificate](FINITE_EULER_BOUNDARY_RESIDUAL_CERTIFICATE_20261003.md),
including the spatial complement of a step-function trial space. In
particular it identifies an essential distinction between compressing
\(C^2\) and squaring a compression of \(C\). All formulas below apply
to complex columns and require no additive parity restriction.

The general mean-functional Schur criterion is already in
[the finite Mellin defect note, Sections 3--4](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_FINITE_MELLIN_DEFECT_20260929.md).
It is reused, not counted as a new result. Negativity on the zero-mean
subspace and bounded mixed terms remain separate obligations. The new
work here concerns the actual cosine/Euler operator needed to test them.

## 1. The exact one-prime expansion

Use positive-axis coordinates \(\mathcal H=L^2(0,\infty;dx)\), with
\(\chi=1_{(0,1)}\) and \(P=1_{(1,\infty)}\). The logarithmic unitary is
\((Wf)(t)=e^{t/2}f(e^t)\). At exponent \(1/2\), for a prime \(p\), put
\[
(B_n f)(x)=2\int_0^\infty\cos(2\pi p^nxy)f(y)\,dy,
\qquad n=-1,0,1,\ldots.
\]
These are scaled cosine transforms and
\(\|B_n\|=p^{-n/2}\). The transport identity gives
\[
\mathcal F_p=-p^{-1}B_{-1}+(1-p^{-1})\sum_{n\ge0}B_n.
\tag{1}
\]
This is the operator-norm expansion established in
[the place-addition note, Section 9](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md).
For \(N\ge0\), truncate before \(n=N\), and denote the resulting
operator by \(\mathcal F_{p,N}\). Then
\[
\|\mathcal F_p-\mathcal F_{p,N}\|
\le\tau_N:=(1+p^{-1/2})p^{-N/2}.
\tag{2}
\]
Set \(C=\chi\mathcal F_p\chi\), \(T=\chi\mathcal F_pP\), and use
\(C_N,T_N\) for their truncated analogues. Thus both truncation errors
are at most \(\tau_N\). The inherited strict gap supplies
\[
A=I-C^2\ge gI,\qquad c:=\|C\|\le\sqrt{1-g}<1.
\tag{3}
\]
One may use the transported certified archimedean bound
\(g=((1-p^{-1/2})/(1+p^{-1/2}))^2(57/10^6)\), provided the cited
prolate certificate is included in the numerical evidence. No sharper
gap is inferred from a sampled eigenvalue here.

All following truncation estimates are in operator norm. They never
assume that the exact \(C\) is Hilbert--Schmidt; in fact it is not at
this critical one-prime exponent.

## 2. Closed formulas for whole-output Grams

For an input interval \(J_j=(a_j,b_j)\subset(0,\infty)\), let
\(h_j=b_j-a_j\) and \(e_j=1_{J_j}/\sqrt{h_j}\). The endpoint \(a_j=0\)
is allowed. Direct integration gives, on \(0<x<1\),
\[
(B_ne_j)(x)=
\frac{\sin(2\pi p^n b_jx)-\sin(2\pi p^n a_jx)}
{\pi p^n x\sqrt{h_j}},
\tag{4}
\]
with its continuous limiting value at zero. Define the real even function
\[
J(z)=z\operatorname{Si}(z)+\cos z-1,
\qquad
I(u,v)=\tfrac12\{J(u+v)-J(u-v)\}.
\tag{5}
\]
Integration by parts and the product-to-sum formula give
\[
J(z)=\int_0^1\frac{1-\cos(zx)}{x^2}\,dx,
\qquad
I(u,v)=\int_0^1\frac{\sin(ux)\sin(vx)}{x^2}\,dx.
\tag{6}
\]
Consequently the **full** inner product on \((0,1)\) is
\[
\langle\chi B_me_i,\chi B_ne_j\rangle
=\frac{1}{\pi^2p^{m+n}\sqrt{h_ih_j}}
\sum_{\xi\in\{a_i,b_i\}}\sum_{\eta\in\{a_j,b_j\}}
\varepsilon_i(\xi)\varepsilon_j(\eta)
I(2\pi p^m\xi,2\pi p^n\eta),
\tag{7}
\]
where \(\varepsilon_j(b_j)=1\) and \(\varepsilon_j(a_j)=-1\).
Unlike a sampled matrix product, (7) includes the entire output interval.
Input intervals may lie below or above 1; hence the same formula handles
both \(C_N\) and \(T_N\).

The single compressed matrix entry is equally explicit. For an output
interval \((a,b)\) and input interval \((c,d)\),
\[
\langle e_{(a,b)},B_ne_{(c,d)}\rangle
=\frac{2}{k\sqrt{(b-a)(d-c)}}
\{\operatorname{Si}(kbd)-\operatorname{Si}(kad)
-\operatorname{Si}(kbc)+\operatorname{Si}(kac)\},
\quad k=2\pi p^n.
\tag{8}
\]
Summing (8) with the coefficients in (1) gives the finite compression;
double-summing (7) gives the whole-output Gram. Both are finite sums of
elementary functions and \(\operatorname{Si}\) for fixed \(N\).
Outward arithmetic, particularly through cancellation in (5), is still
required to turn their evaluations into a certificate.

## 3. The missing compression term is a positive leakage Gram

Let \(E:\mathbb C^d\to\chi\mathcal H\) synthesize orthonormal step
functions on a partition of \((0,1)\), and write \(Q=EE^*\). Put
\[
D=E^*CE,\qquad H=E^*C^2E,\qquad R=(I-Q)CE.
\]
Then
\[
\boxed{H=D^2+R^*R,\qquad E^*AE=I-H.}
\tag{9}
\]
Thus \(I-D^2\) is generally not the compression of the actual boundary
operator \(I-C^2\) to be inverted. It omits the positive matrix \(R^*R\).
This omission is unrelated to increasing arithmetic precision in the
entries of \(D\).

For \(C_N\), define \(D_N,H_N,R_N\) in the same way and set
\[
G_N=H_N-D_N^2=R_N^*R_N\ge0.
\tag{10}
\]
Equations (7)--(8) compute every entry, including the leakage. In exact
arithmetic, no diagonalization or square root of \(G_N\) is needed:
for any coefficient matrix \(Z\),
\[
\|R_N Z\|_{\rm HS}^2=\operatorname{tr}(Z^*G_NZ).
\tag{11}
\]
For later use put \(c_N=c+\tau_N\) and
\(\delta_N=\tau_N(2c+\tau_N)\). Then
\[
\|D-D_N\|\le\tau_N,\quad
\|H-H_N\|\le\delta_N,\quad
\|A-(I-C_N^2)\|\le\delta_N.
\tag{12}
\]
A sharper way to transfer leakage norms is
\[
\|RZ\|_{\rm HS}\le
\sqrt{\operatorname{tr}(Z^*G_NZ)}+\tau_N\|Z\|_F.
\tag{13}
\]
It avoids an artificial square-root loss from separately bounding the
errors in \(H\) and \(D^2\).

## 4. The analogous source leakage for the crossing block

Let \(E_+:\mathbb C^{d_+}\to P\mathcal H\) synthesize orthonormal
steps in \((1,e^L)\). Set
\[
J_N=E^*T_NE_+,\qquad H_{+,N}=E_+^*T_N^*T_NE_+,\qquad
G_{+,N}=H_{+,N}-J_N^*J_N\ge0.
\tag{14}
\]
The same formulas (7)--(8), with input endpoints above 1, compute these
matrices. If \(R_{+,N}=(I-Q)T_NE_+\), then
\(G_{+,N}=R_{+,N}^*R_{+,N}\).

For a finite-rank approximation to the source crossing operator, write
\[
X_0=E_+UV^*E^*,\qquad
f=TE_+U,\quad g=CEV.
\tag{15}
\]
Here \(U,V\) can be rectangular and complex. The target associated with
\(X_0\) is
\(K_0=2\Re\langle g,A^{-1}f\rangle_{\rm HS}\), exactly retaining
the inverse metric. Define truncated sources
\(f_N=T_NE_+U\) and \(g_N=C_NEV\).

Let \(Y=Ey\), \(Z=Ez\) be arbitrary primal and dual approximations,
with coefficient matrices \(y,z\) of the appropriate size. Put
\[
\begin{split}
\alpha_N={}&\|J_NU-(I-H_N)y\|_F,\\
\eta_N={}&
\sqrt{\operatorname{tr}(U^*G_{+,N}U)}
+\sqrt{\operatorname{tr}((D_Ny)^*G_N(D_Ny))}
+c_N\sqrt{\operatorname{tr}(y^*G_Ny)},\\
\beta_N={}&\|D_NV-(I-H_N)z\|_F,\\
\theta_N={}&
\sqrt{\operatorname{tr}((V+D_Nz)^*G_N(V+D_Nz))}
+c_N\sqrt{\operatorname{tr}(z^*G_Nz)}.
\end{split}
\tag{16}
\]
Then the **full-space**, untruncated residuals obey
\[
\boxed{
\begin{split}
\|f-AY\|_{\rm HS}
&\le\sqrt{\alpha_N^2+\eta_N^2}
+\tau_N\|U\|_F+\delta_N\|y\|_F=:r_N,\\
\|g-AZ\|_{\rm HS}
&\le\sqrt{\beta_N^2+\theta_N^2}
+\tau_N\|V\|_F+\delta_N\|z\|_F=:s_N.
\end{split}}
\tag{17}
\]

To verify the spatial-complement terms, decompose \(C_N\) against
\(Q\oplus(I-Q)\). Its lower-left block is \(R_N\), and its lower-right
block \(C_{N,\perp}\) has norm at most \(c_N\). Therefore
\[
(I-Q)C_N^2E=R_ND_N+C_{N,\perp}R_N.
\tag{18}
\]
For the primal residual add the source complement \(R_{+,N}U\).
For the dual residual combine its source complement \(R_NV\) with
\(R_ND_Nz\). Orthogonality of \(Q\) and \(I-Q\) gives the square
roots in (17); (2) and (12) give its last two terms. This proves (17)
without evaluating fourth powers of \(C\), and without assuming that a
small compressed residual controls its omitted rows.

## 5. A completely finite center and error budget

The companion primal-dual certificate can now be evaluated with the finite
center
\[
k_N=2\Re\left\{
\operatorname{tr}((D_NV)^*y)
+\operatorname{tr}\bigl(z^*[J_NU-(I-H_N)y]\bigr)
\right\}.
\tag{19}
\]
The difference from the same corrected center formed with exact operators
is at most
\[
e_N=2\tau_N(\|V\|_F\|y\|_F+\|z\|_F\|U\|_F)
+2\delta_N\|z\|_F\|y\|_F.
\tag{20}
\]
Combining (17) with that certificate yields
\[
\boxed{|K_0-k_N|\le e_N+2g^{-1}r_Ns_N.}
\tag{21}
\]
All terms on the right are finite-matrix expressions, explicit Euler tails,
and an independently justified gap. Numerical interval errors must be
retained in each term. The candidate solves may use \(I-H_N\); positive
definiteness of that finite matrix is not needed for the identity if
arbitrary \(y,z\) are used and their residuals are bounded as above.

Finally, if \(\|X-X_0\|_1\le\varepsilon_X\), the full correction has
the additional error
\[
|K[X]-K_0|\le\frac{2c}{\sqrt g}\varepsilon_X.
\tag{22}
\]
The companion note supplies one explicit smooth-source nuclear
approximation. Its finite smooth mode functions may be projected onto
the step spaces here after the unitary coordinate change: a positive
logarithmic mode \(v(t)\) becomes \(u^{-1/2}v(\log u)\) for
\(u>1\), and a reflected negative mode \(w(z)\) becomes
\(u^{-1/2}w(-\log u)\) for \(e^{-L}<u<1\), both zero outside
their supports. Equivalently the physical crossing kernel is
\((uv)^{-1/2}\Re\kappa_F(\log(u/v))\).
For a finite expansion
\(X_f=\sum_j a_j|v_j\rangle\langle w_j|\), with unit norm modes,
\[
\|X_f-Q_+X_fQ\|_1
\le\sum_j|a_j|
\bigl(\|(I-Q_+)v_j\|_2+\|(I-Q)w_j\|_2\bigr).
\tag{23}
\]
This follows by splitting each rank-one difference in its two factors and
using contractivity of the projections. The squared mode errors are
\(1-\|E_+^*v_j\|^2\) and \(1-\|E^*w_j\|^2\), so they can be
integrated exactly or enclosed. Physical support endpoints should be
partition endpoints; one must not ignore the jumps of individually
zero-extended mode functions. Equation (23), added to the nuclear tail,
makes the change of trial basis explicit rather than treating a
Hilbert--Schmidt source error as a trace-norm error.

## 6. What this establishes and leaves open

Equations (7), (9), and (17)--(23) give an analytic, full-tail route to
certifying the actual first-prime boundary correction. They close a
specific error-control gap in a raw compressed-cosine diagnostic.
They do not assert that the bounds will be numerically sharp at any
chosen dimension. The inherited gap is small, and a useful sign enclosure
may need substantially better trial vectors or a sharper certified gap.

As a [reproducible formula audit](../numerics/finite_euler_leakage_formula_check.py),
direct floating-point quadrature of three instances
of (7), including \(n=-1\) and input intervals above 1, agreed within
\(3\cdot10^{-16}\). For \(p=2\), four nonnegative dyadic terms and six
uniform step cells, a separate 500-node Gauss calculation of \(H_N\)
agreed within \(2.1\cdot10^{-14}\); its leakage trace was approximately
0.334878. These are ordinary quadrature checks, not certified enclosures
of the infinite operator or of a correction sign.

The next numerical obligation is to use these full leakage Grams, outward
function evaluation, a nuclear source tail, and the true inverse metric
in a single error budget for a specified prepared mean-zero source at
\(L=1\), \(S=\{2\}\). A positive certified correction would falsify
the proposed mean bound. A negative correction for finitely many sources
would only pass those tests. Neither result by itself would prove the
all-source rank-one inequality, its mixed-term control, or the weaker
support-adapted Weil comparison.
