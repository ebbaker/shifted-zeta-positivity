# A depth–shift path controlled by cumulative storage

Working research, 10 September 2026. This continues the [previous investigation](../critical-path-20260910/critical_path_research.md), using the normalization of the [Weil-depth v0.3 manuscript](https://github.com/ebbaker/shifted-zeta-positivity/blob/a566944dc1be2899e37fce3d0e857516ced33d8f/papers/weil-depth/manuscript/finite_horizon_weil.tex). The author's normalization verification remains separate. The deductions below require independent mathematical review.

The useful object is the contraction defect after the whole shift evolution. A Cayley transform puts this defect into reflection-preserving coordinates, with an even small-shift expansion. Its spatial relative coupling is **exactly** the original cumulative-storage coupling. This gives a depth-and-shift step criterion that preserves the signs and directions of storage changes.

There is also a new enclosed calculation: the polynomial that previously gave a negative instantaneous generator at (L=\log7,\ \omega=10^{-11}) has **positive cumulative storage** at that same point. This is a statement about one input, not an operator contraction certificate or a successful depth extension.

## 1. What the path should preserve

Write (V=V_{\omega,L}) and

\[
D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L}.
\]

On the common core, with the limiting interpretation at shift zero, the manuscript's evolution identity gives

\[
D_{\omega,L}[f]
=2\int_0^\omega Q_{s,L}[V_{s,L}f],ds. \tag{1}
\]

The integrand can be negative at some shifts or in some directions while the integral remains positive. Requiring every (Q_{s,L}\) to be positive is a sufficient restriction on the path; it is stronger than the cumulative condition actually needed.

For the depth split (L+h=L\cup h), translation identifies the new slab with ((0,h)), and causality gives

\[
V_{\omega,L+h}=
\begin{pmatrix}X&0\\Y&Z\end{pmatrix},
\quad X=V_{\omega,L},\quad Z=V_{\omega,h}.
\]

Suppose (X,Z) are strict contractions. Define

\[
E=I-X^*X,\qquad F_{\rm out}=I-ZZ^*,\qquad
\mathcal C=F_{\rm out}^{-1/2}YE^{-1/2}.
\]

Eliminating the new input from the full defect gives

\[
S=E-Y^*F_{\rm out}^{-1}Y
=E^{1/2}(I-\mathcal C^*\mathcal C)E^{1/2}. \tag{2}
\]

Consequently the enlarged transfer is a strict contraction exactly when

\[
\boxed{\|\mathcal C\|<1.} \tag{3}
\]

The non-strict version uses (\le1), still with strictly positive diagonal defects. This criterion measures the leakage in the actual storage metrics. Replacing those metrics by their least eigenvalues can discard the cancellation we want to study.

## 2. Cumulative storage in reflection-preserving coordinates

Define, for positive shift,

\[
\mathcal Z_{\omega,L}=(I-V)(I+V)^{-1},\qquad
P_{\omega,L}=\frac{2}{\omega}\operatorname{Re}\mathcal Z_{\omega,L}. \tag{4}
\]

These are bounded operators. The inverse exists without assuming contraction: a finite-horizon Volterra convolution with locally integrable kernel is quasinilpotent. Indeed, conjugating by an exponential weight bounds its spectral radius by a weighted kernel (L^1) norm tending to zero. Similarity preserves its spectrum.

Direct multiplication proves the exact congruence

\[
\boxed{
D_{\omega,L}=\frac{\omega}{2}(I+V^*)P_{\omega,L}(I+V).
} \tag{5}
\]

Thus (P\succeq0\iff\|V\|\le1), and (P\succ0\iff\|V\|<1), where (\succ0) means a positive coercivity bound. If (P\succeq pI), then

\[
D\succeq\frac{\omega p}{2\|(I+V)^{-1}\|^2}I.
\]

The real causal kernel implies (V^*=R_LVR_L). The same identity holds for (\mathcal Z), and hence (P) commutes with reflection. It can be analyzed in separate even and odd sectors. The raw input defect (D) generally cannot.

For (\mathscr F(p)=\xi(\tfrac12+p)), the causal transfer whose real part is (P) is

\[
a_{\rm cum,\omega}(p)
=\frac{2}{\omega}\frac{1-K_\omega(p)}{1+K_\omega(p)}
=\frac{2}{\omega}
\frac{\mathscr F(p+\omega)-\mathscr F(p-\omega)}
     {\mathscr F(p+\omega)+\mathscr F(p-\omega)}. \tag{6}
\]

This is an even expression in the shift. On a sufficiently far right Laplace line, differentiating on compactly supported smooth inputs gives

\[
a_{\rm cum,\omega}
=a_0+\omega^2\left(\frac{a_0''}{6}-\frac{a_0^3}{12}\right)+O(\omega^4),
\qquad a_0=2\mathscr F'/\mathscr F. \tag{7}
\]

Primes on (a_0) denote derivatives in (p). Equivalently, if the causal generator is (A_\omega=A_0+\omega^2A_2+\cdots), the coefficient is (A_2/3-A_0^3/12), before taking the real part. This extra cubic transport term is absent from the instantaneous generator criterion. Equation (7) is an expansion on a common smooth core, not an operator-norm estimate or a claim that (A_0^3) is defined on every ground state.

There is a substantial analytic caveat: (P_{\omega,L}) is bounded for each positive shift, whereas (Q_{0,L}) is unbounded. Therefore one cannot assert a bounded-operator (O(\omega^2)) difference (P_\omega-Q_0). In particular, no uniform relative convergence on the entire central energy space follows from (7). A verified comparison between two **positive** shifts avoids this issue.

Also, (V) is compact: approximate its locally integrable causal kernel in (L^1) by bounded kernels, whose finite-horizon operators are Hilbert–Schmidt. Consequently (P_{\omega,L}=(2/\omega)I+\text{compact}). This supplies a useful spectral structure, but no efficient tail bound as (\omega\downarrow0) by itself.

## 3. The same relative coupling, exactly

Let (R_X=(I+X)^{-1}), (R_Z=(I+Z)^{-1}). In the same depth split,

\[
P_{\omega,L+h}=\begin{pmatrix}A&B^*\\B&F\end{pmatrix},
\quad A=P_{\omega,L},\quad F=P_{\omega,h},
\quad B=-\frac{2}{\omega}R_ZYR_X. \tag{8}
\]

The diagonal forms have the two useful orientations

\[
A=\frac{2}{\omega}R_X^*ER_X,
\qquad F=\frac{2}{\omega}R_ZF_{\rm out}R_Z^*. \tag{9}
\]

It follows that

\[
\boxed{
\|F^{-1/2}BA^{-1/2}\|
=\|F_{\rm out}^{-1/2}YE^{-1/2}\|.
} \tag{10}
\]

To check this without commuting noncommuting factors, set

\[
U=\sqrt{2/\omega}\,F^{-1/2}R_ZF_{\rm out}^{1/2},\qquad
W=\sqrt{2/\omega}\,E^{1/2}R_XA^{-1/2}.
\]

Equations (9) make (U,W) unitary, and the left normalized cross block is (-U\mathcal C W). The Cayley change therefore preserves the complete relative-coupling information. It does not strengthen the contraction property; it provides coordinates compatible with reflection and the even shift expansion.

## 4. An inequality for a simultaneous depth and shift step

Fix a proposed depth extension (h). At a reference positive shift (a), suppose its diagonal forms (A_a=P_{a,L}) and (F_a=P_{a,h}) are coercive. The full enlarged form need not yet be positive. Let (B_a) be its cross block and set

\[
\mathcal K=F_a^{-1/2}B_aA_a^{-1/2}.
\]

For a candidate new shift (b>0), define the oriented relative changes

\[
\begin{aligned}
H_A&=A_a^{-1/2}(A_b-A_a)A_a^{-1/2},\\
H_F&=F_a^{-1/2}(F_b-F_a)F_a^{-1/2},\\
H_B&=F_a^{-1/2}(B_b-B_a)A_a^{-1/2}.
\end{aligned} \tag{11}
\]

The enlarged form at (b), normalized using the reference diagonal forms, is exactly

\[
\begin{pmatrix}I+H_A&(\mathcal K+H_B)^*\\
\mathcal K+H_B&I+H_F\end{pmatrix}.
\]

It is coercive if and only if (I+H_F\succ0) and

\[
\boxed{
I+H_A-(\mathcal K+H_B)^*(I+H_F)^{-1}(\mathcal K+H_B)\succ0.
} \tag{12}
\]

This is the principal continuation inequality. It retains an increase in storage, a decrease in leakage, and their directions. It allows a shift change to rescue an extension whose reference coupling is already too large.

A simpler sufficient version is

\[
\boxed{
\|\mathcal K+H_B\|^2<(1+\alpha)(1+\varphi),
\quad H_A\succeq\alpha I,\quad H_F\succeq\varphi I,
\quad\alpha,\varphi>-1.
} \tag{13}
\]

For a conservative check, one can replace this by

\[
\|\mathcal K\|+\|H_B\|
<\sqrt{(1-\|H_A\|)(1-\|H_F\|)}, \tag{14}
\]

provided both relative diagonal changes have norm below one. But (14) discards precisely the signed improvements a critical-path argument hopes to exploit. Equation (12), or a weak-subspace version with a rigorous complementary bound, is the preferable research target.

For unchanged shift, (12) reduces to (I-\mathcal K^*\mathcal K\succ0). Then

\[
P_{a,L+h}\succeq(1-\|\mathcal K\|)(A_a\oplus F_a). \tag{15}
\]

This is an inequality that survives a depth extension, conditional on the required relative-coupling bound. The unproved part is supplying that bound along a sequence of extensions with unbounded total depth.

## 5. What “critical path” means quantitatively

At fixed (L,h), suppose the largest singular value (c(\omega)=\|F_\omega^{-1/2}B_\omega A_\omega^{-1/2}\|>0) is simple. Choose its corresponding vectors (x,y) in the original spaces so that

\[
A_\omega[x]=F_\omega[y]=1,\quad
\langle y,B_\omega x\rangle=c,
\quad B_\omega x=cF_\omega y,\quad B_\omega^*y=cA_\omega x.
\]

Differentiating the extremal quotient gives

\[
\boxed{
c'=\operatorname{Re}\langle y,B_\omega' x\rangle
-\frac c2\big(A_\omega'[x]+F_\omega'[y]\big).
} \tag{16}
\]

Thus the relevant balance is **the change in cross coupling minus the relative replenishment of the two storage terms, evaluated in the active singular directions**. Differentiating the smallest old storage eigenvalue alone does not determine it. Shift differentiation at positive shift is legitimate in operator norm for these locally integrable kernels and their logarithmic derivatives.

A level curve (c=1-\eta) is a possible continuation guide, with positive slack (\eta). Where both parameter derivatives exist and (c_\omega\ne0), its formal slope is (\omega'(L)=-c_L/c_\omega). This is a diagnostic, not a proved global differential equation: depth changes move arithmetic delays, operator-norm depth derivatives can fail, and leading singular values can cross. The finite-step inequality (12) remains the robust statement. At a repeated top singular value, all active directions must be controlled, rather than selecting one favorable vector.

An actual proof path must deliver

\[
L_{j+1}=L_j+h_j,\quad \sum_jh_j=\infty,\quad
\omega_j\downarrow0,\quad P_{\omega_j,L_j}\succeq0. \tag{17}
\]

Strict inequalities with slack are convenient for the inverses during the recursion. A uniform positive slack or a uniform lower storage bound is not required by the manuscript's final diagonal argument. Local continuability alone does not prove (17); allowable increments can have a finite sum.

The “edge” analogy also needs a distinction. Suzuki's work with the same shifted xi quotient records its innerness unconditionally for (\omega\ge1/2), and for every positive shift under RH. Thus the full transfer has an unconditional contractive anchor at shift (1/2), through the half-plane multiplier interpretation. Under RH, cumulative contraction is not expected to fail across a nonzero finite-depth boundary. A useful path would control **degenerating margins and coupling** while approaching infinite depth and zero shift. It need not be a unique boundary between true and false finite-depth positivity. See [Suzuki (2012), §1.4 and Proposition 1.2](https://www.kurims.kyoto-u.ac.jp/~kenkyubu/bessatsu/open/B34/pdf/B34_023.pdf). No monotonicity of the finite-depth coupling in shift is assumed here.

## 6. Enclosed comparison on the previously saved vector

Let (f) be the exact real polynomial given by the rational even Legendre coordinates in [the previous witness record](../critical-path-20260910/generator_witness_log7.json), of degree 126, on (L=\log7). The earlier calculation enclosed

\[
-2.999\times10^{-27}
<\frac{Q_{10^{-11},L}[f]}{\|f\|^2}
<-2.998\times10^{-27}.
\]

The new full-output calculation gives

\[
\boxed{
8.717034818878968\times10^{-38}
<\frac{D_{10^{-11},L}[f]}{\|f\|^2}
<8.717034818878970\times10^{-38}.
} \tag{18}
\]

Equivalently, its stored energy divided by (2\omega) is approximately (4.358517409439484\times10^{-27}). At shift (10^{-13}), the same normalized quantity is approximately (6.805580073330289\times10^{-28}), close to its central quotient (6.801901746095492\times10^{-28}).

These bounds retain every output mode. They do not use (I-(\Pi V\Pi)^*(\Pi V\Pi)), whose positivity could be an artifact of throwing output away. Nevertheless, only this particular input was tested. A direction that minimizes cumulative storage can rotate with shift; positivity for this fixed vector neither bounds (\|\mathcal C\|\) nor establishes contraction at (10^{-11}).

### Kernel construction and remainder

Write the archimedean impulse as

\[
\kappa^\gamma_\omega(t)=\frac{(2\pi)^\omega}{\Gamma(\omega)}t^{\omega-1}G_\omega^V(t).
\]

For (\alpha=1/2-\omega,\ \beta=1/2+\omega), put

\[
g(t)=e^{t/2}(\sinh t/t)^{\omega-1},\qquad
y_c(t)=\omega\int_0^1 v^{\omega-1}e^{ct(1-v)}g(tv)\,dv.
\]

The rational factor of the gamma transfer gives exactly

\[
G_\omega^V(t)=g(t)-4t\big(\alpha y_\alpha(t)+\beta y_{-\beta}(t)\big).
\]

Its series coefficients can be evaluated stably even at tiny positive shifts:

\[
y_{c,0}=1,\qquad
y_{c,j}=\frac{\omega g_j+c y_{c,j-1}}{\omega+j}.
\]

On (|z|=3<\pi), the product for (\sinh z/z) implies

\[
|z/\sinh z|\le3/\sin3<24.
\]

For (0<\omega\le1/2), it follows that (|g|<120), (|y_c|\le120e^{3|c|}), and

\[
|G_\omega^V(z)|\le120+1440e^3<32768.
\]

Truncating this analytic profile at degree (M), Cauchy's coefficient estimate and Young's convolution inequality give the full operator error

\[
\delta_\gamma\le
\frac{(2\pi L)^\omega}{\Gamma(\omega)}
\frac{32768(L/3)^{M+1}}{(M+1+\omega)(1-L/3)}.
\]

The full arithmetic transfer contains all (n<e^L), including composite mixed-prime terms. Since their coefficients (b_\omega(n)) are positive,

\[
\delta\le\Big(\sum_{\log n<L}b_\omega(n)\Big)\delta_\gamma
\]

bounds the full transfer error. At (L=\log7), the calculation includes (n=1,2,3,4,5,6); the endpoint (n=7) has zero action.

The polynomial input gives a model gamma output (u^\omega p(u)), (u=x/L). Every pair of delayed outputs is integrated exactly in terms of polynomial coefficients and moments

\[
J_k(d,\ell)=\int_0^\ell t^{k+\omega}(t+d)^\omega\,dt.
\]

An enclosed hypergeometric expression initializes (J_0), and integration by parts gives

\[
J_{k+1}=\frac{\ell^{k+\omega+1}(\ell+d)^{\omega+1}-d(k+\omega+1)J_k}{k+2\omega+2}.
\]

All arithmetic uses Arb balls, with sufficient precision for the unstable cases (d/\ell>1). If (r=\|\widetilde V f\|^2/\|f\|^2), the exact squared-norm ratio differs by at most (2\delta\sqrt r+\delta^2).

The first run used degree 220 and 6144 bits; an increased-degree replay used degree 240 and 7168 bits. The replay transfer error is below (1.906\times10^{-54}), and its squared-norm error is below (3.812\times10^{-54}). The outward-rounded bound (18) contains that error.

Independent numerical cross-checks compared the profile against the original gamma beta integral, and the complete constant-input norm at (L=\log3,\omega=1/4) against direct quadrature. Differences were below (5\times10^{-66}). A noncommuting block example also checked (5) and (10). Those are checks of the implementation, not additional mathematical certificates.

## 7. The next concrete target

The natural next depth test is (L=\log7\) with (h=\log(8/7)<\log2). The new diagonal slab then has no arithmetic delays of its own, while the full extension introduces the delay at (\log7).

Use the existing all-operator contraction at a certified small shift as the reference. For each proposed new shift, retain the weak directions of (A_a) and the dominant singular directions of (\mathcal K), evaluate the **signed** changes in (11), and attempt to enclose the Schur residual in (12). Bound the complement with full-output estimates. Do not carry old-depth positivity to a different shift without this comparison, or infer the coupling norm from a compressed transfer.

The first milestone is a validated depth extension using cumulative storage at a shift where the instantaneous-generator route is unavailable. A useful numerical path would then need a verified control on successive coupling changes. The all-depth theorem still requires proving that such steps reach unbounded depth as the shift tends to zero. No such extension, coupling upper bound, or all-depth path has been certified in this packet.
