# Complete Laguerre kernels and the triple-zero limit

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort unavailable to this session
and not inferred. Analytic derivations, outward replays and parallel audits
are internal LLM work, not independent mathematical validation.

This continues the [two stationary targets](5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md).
It identifies the complete kernels whose conditional Fourier signs are
needed, proves that a first Laguerre sign cannot detect a triple locally,
and certifies a negative value of the genuine theta derivative kernel.
It proves no positive-definiteness theorem or uniform theta sign.

## 1. The exact paired theta source

Put \(m_t(u)=e^{tu^2}\Phi_e(u)\) and
\(A_t(x)=\widehat m_t(x)=2H_t(x)\), with the full Fourier convention
\(\widehat f(x)=\int_{\mathbb R}e^{ixu}f(u)\,du\). Define
\[
K_{n,t}(s)=\int_{\mathbb R}r^{2n}m_t(s+r)m_t(s-r)\,dr,
\]
\[
J_{j,t}(s)=\int_{\mathbb R}r^2(r^2-s^2)^j
 m_t(s+r)m_t(s-r)\,dr.
\tag{1}
\]
In particular \(J_0=K_1\) and \(J_1=K_2-s^2K_1\). The pair retains
the complete source, including every theta term and cross contribution:
\[
m_t(s+r)m_t(s-r)=e^{2t(s^2+r^2)}\Phi_e(s+r)\Phi_e(s-r).
\]
Theta decay makes this product Schwartz in the two variables, locally
uniformly on compact time intervals, with all fixed polynomial insertions.
Fubini, differentiation and the following changes of variables therefore
have their required full-source domains.

For the derivative-level Laguerre expressions
\[
\mathscr L_j(A)=(A^{(j+1)})^2-A^{(j)}A^{(j+2)},
\]
symmetrization of the double Fourier integral gives the multiplier
\(\tfrac12(u-v)^2(-uv)^j\). With \(u=s+r\), \(v=s-r\), the absolute
Jacobian is two. Thus
\[
\boxed{\mathscr L_j(A;x)=4\widehat J_{j,t}(2x).}
\tag{2}
\]
All \(J_j\) are even and real, so this is a cosine integral. Since
\(A=2H\), \(\mathscr L_j(H;x)=\widehat J_{j,t}(2x)\).
The powers of \(r^2-s^2\) are derivative-level indices. In particular
\(\mathscr L_1(A)\) is the first Laguerre expression of \(A'\), not
the second generalized Laguerre coefficient of \(A\).

The exact research targets can consequently be stated as
\[
\widehat J_{0,t}(2x)\ge0\quad\hbox{on }A_t'(x)=0,
\qquad
\widehat J_{1,t}(2x)\ge0\quad\hbox{on }A_t''(x)=0,
\tag{3}
\]
on the required positive-time predecessor neighborhood. These are exactly
the stationary signs of Note 5. Global Fourier nonnegativity would be a
stronger sufficient input.

## 2. Which positivity matters

For a real even Schwartz kernel \(J\), its Fourier transform is
nonnegative at every real frequency exactly when \(J\) is positive
definite as a translation kernel:
\[
\sum_{a,b}c_a\overline{c_b}J(s_a-s_b)\ge0
\]
for every finite set of real points and complex coefficients. The forward
direction follows from Fourier inversion and the integral of
\(\widehat J(\xi)|\sum_a c_ae^{-i\xi s_a}|^2\); the converse is the
usual integrable-kernel Fourier criterion.

Pointwise \(J_0(s)>0\) is automatic for a positive density. It does not
imply the desired pointwise sign of \(\mathscr L_0(A;x)\). Instead it
supplies the dual generic fact that \(\mathscr L_0\), as a function of
frequency, is positive definite. A positive-definite function can take
negative values. The unknown condition is positive definiteness of the
source kernel \(J_0\), or the weaker conditional Fourier sign in (3).
This distinction is the same observation gap that a positive lifted norm
does not resolve.

Nor must a kernel be pointwise nonnegative to be positive definite. For a
Gaussian source \(m(u)=e^{-au^2}\),
\[
J_1(s)=\left(\frac{3}{4a}-s^2\right)J_0(s),\qquad
\mathscr L_1(A;x)=A(x)^2
 \left(\frac1{4a^2}+\frac{x^2}{8a^3}\right)>0.
\]
This kernel is negative in its tails while its Fourier response is
positive. A negative source-kernel value therefore does not refute (3).

The canonical weighted-autocorrelation approach is classical.
[Csordas, Theorem 3.7](https://arxiv.org/pdf/1309.0055v2) relates generalized
Laguerre expressions to positive definiteness of all canonical kernels
under its admissibility and log-concavity hypotheses. Its Open Problems
4.7 and 4.11 discuss the first theta Laguerre sign and the same polynomial-
weighted kernel family. That discussion supplies no low-order sign theorem
for our targets. These statements were checked in the printed PDF; no
claim about a later resolution is inferred. Our constants in (2) are
derived directly for \(A=2H\), rather than imported from another
normalization. No novelty claim is made for the classical kernel identity.

## 3. The second source sign is independent

The existing [Heat Note 12](../../notes/12_THRESHOLD_COLLISION_JETS_AND_PAID_LAGUERRE_TEST_20261009.md)
already records the first identity in the exact hierarchy
\[
(\partial_t+\partial_x^2)\mathscr L_j=2\mathscr L_{j+1}.
\tag{4}
\]
From the paired source, \(\partial_tK_n=2s^2K_n+2K_{n+1}\), hence
\(J_1=\partial_tJ_0/2-2s^2J_0\), which gives the same identity.
This is a relation between the two signs, not a positivity closure.

Let \(s=t-T\), \(y=x-a\), and suppose an analytic heat solution has an
exact triple at \((T,a)\). If \(c=H_{xxx}(T,a)/6\ne0\), its heat Taylor
series gives, with \(w=|y|+\sqrt{|s|}\),
\[
H=c(y^3-6sy)+O(w^4),\quad
H_x=c(3y^2-6s)+O(w^3),\quad H_{xx}=6cy+O(w^2).
\]
The weighted remainder estimates follow by grouping the convergent heat
series by spatial weight one and time weight two. Therefore
\[
\mathscr L_0(H)=c^2(3y^4+36s^2)+R,\qquad |R|\le Mw^5
\tag{5}
\]
in some neighborhood. Since
\((|y|+\sqrt{|s|})^4\le8(y^4+s^2)\), the leading term is at least
\(3c^2w^4/8\). For sufficiently small nonzero \(w\) within the original remainder
neighborhood, (5) is strictly positive; for example
\(w<3c^2/(16M)\) pays a positive margin
\(3c^2w^4/16\). Omit the bound involving \(M\) if the remainder vanishes.

Thus **every analytic exact triple is surrounded by a neighborhood where
the first Laguerre expression is nonnegative**. At the same time, applying
Note 5's predecessor lemma to \(H_x\) forces
\(H_xH_{xxx}>0\) on an earlier \(H_{xx}=0\) branch. The positive even
Gaussian triple control in [Note 4](4_COORDINATE_INVARIANCE_AND_IMPLICIT_HEAT_FOLDS_20261010.md)
has this local property while retaining a positive pure lift. No global
Laguerre sign for that Gaussian control is asserted.

The exact cubic heat solution \(H=y^3-6sy\) makes the limitation especially
clear:
\[
\mathscr L_0=3y^4+36s^2\ge0\quad\hbox{everywhere},\qquad
\mathscr L_1=18y^2+36s<0\quad\hbox{at }y=0,\ s<0.
\]
The second stationary target is a genuine additional obligation in this
two-level argument, even if a first sign could be measured perfectly.

Descending from a later time does not repair the gap automatically.
With \(P_\tau\) the forward Gaussian heat semigroup, the valid Duhamel
formula on a domain where the convolutions are justified is
\[
\mathscr L_0(t)=P_{T-t}\mathscr L_0(T)
 -2\int_t^T P_{s-t}\mathscr L_1(s)\,ds.
\tag{6}
\]
A nonnegative second source is subtracted. Terminal nonnegativity alone
does not establish the needed earlier-time sign.

## 4. A complete genuine-theta kernel obstruction

The [outward kernel checker](../numerics/check_theta_laguerre_kernel.py)
encloses the full \(J_{1,t}(0.3)\) for the entire interval
\(0\le t\le1/20\):
\[
\boxed{-1.824617\cdot10^{-9}<J_{1,t}(0.3)
 <-1.683363\cdot10^{-9}<0.}
\tag{7}
\]
This refutes an attempted proof through pointwise positivity of \(J_1\).
It does not refute positive definiteness or the conditional Fourier sign.
The argument \(0.3\) is a source-kernel coordinate, not a physical
height at which a stationary sign has been tested.

The replay uses 2,048 outward interval cells on \(0\le r\le1\), the
evenness factor two, and the actual pair
\(e^{2t(s^2+r^2)}\Phi(s+r)\Phi(|s-r|)\). Theta terms 1, 2 and 3 enter
each factor; every omitted term is paid by
\[
\sum_{n\ge4}n^m e^{-\pi n^2e^{4u}}
\le\frac{4^m e^{-16\pi e^{4u}}}
 {1-(5/4)^m e^{-9\pi e^{4u}}},\qquad m=2,4.
\tag{8}
\]
The finite-interval integral is enclosed by its cell ranges times their
widths, so no unproved quadrature remainder is used.

For the remaining tail use the complete theta envelope
\(\Phi(u)\le C e^{-8\pi u^2}\), \(C=4\pi^2e^{-\pi}\), \(u\ge0\).
Drop the negative theta part, use \(n^4\le16^{n-1}\) and
\(n^2-1\ge3(n-1)\), then bound the geometric ratio
\(16e^{-3\pi}<1/2\). Finally
\(e^{4u}\ge1+4u+8u^2\) and \(4\pi>9\) give the envelope.
Let \(k=2(8\pi-1/20)\), \(R=1>s=0.3\). Since the kernel tail is
nonnegative and \(r^2(r^2-s^2)\le r^4\), its full payment is at most
\[
2C^2e^{-k(s^2+R^2)}
\left(\frac{R^3}{2k}+\frac{3R}{4k^2}+\frac{3}{8k^3R}\right)
 <1.069295\cdot10^{-25}.
\tag{9}
\]
This follows by integration by parts twice and the Gaussian Mills bound.
All exponential and polynomial operations use 60-digit directed Decimal
intervals and the retained corrected integer-power implementation. The
[small record](../numerics/THETA_LAGUERRE_KERNEL_RECORD_20261010.json)
contains every directed endpoint and the two imported source hashes.

## 5. The same obstruction in the genuine theta tail

There is also a non-effective analytic tail statement. Uniformly for time
in a compact real interval, as \(s\to+\infty\),
\[
K_1(s)\sim\frac{\pi^3}{32}e^{2ts^2+12s-2\pi e^{4s}},\qquad
K_2(s)\sim\frac{3\pi^2}{1024}e^{2ts^2+8s-2\pi e^{4s}}.
\tag{10}
\]
Hence \(K_2/K_1\sim3e^{-4s}/(32\pi)\) and
\(J_1(s)\sim-s^2K_1(s)<0\).

Indeed \(\Phi(v)=2\pi^2e^{9v-\pi e^{4v}}[1+O(e^{-4v})]\).
On \(|r|\le s/2\), both arguments are at least \(s/2\); the paired
source is
\(4\pi^4e^{18s+2ts^2}e^{-\lambda\cosh(4r)+2tr^2}
[1+O(e^{-2s})]\), \(\lambda=2\pi e^{4s}\).
Set \(q=\sqrt{8\lambda}\,r\). The inequality
\(\cosh(4r)-1\ge8r^2\) supplies an integrable dominating Gaussian
after removing \(e^{-\lambda}\). Its weighted Gaussian moments give
(10). The same geometric theta bound also gives the sharper envelope
\(\Phi_e(v)\le4\pi^2e^{9|v|-\pi e^{4|v|}}\).
On \(|r|>s/2\), it bounds the paired source by
\[
C_T\exp\{18\max(s,|r|)+2T(s^2+r^2)-\pi e^{4(s+|r|)}\}
\quad(|t|\le T).
\]
The double-exponential term absorbs polynomial and Gaussian growth, giving
an outer integral \(O(e^{-c e^{6s}})\), negligible relative to (10).
This proves the equivalences without claiming an effective starting
height or rate. The bounded statement (7) has its separate full payment.

## 6. Next analytic checkpoint

The target is a positive-definite representation of the complete kernels,
or a weaker conditional Fourier estimate (3), using genuine theta
coefficients or modular gluing and retaining all cross terms. A successful
argument must allow the signed \(J_1\) source while controlling its Fourier
response. The [bounded stationary calibration](6_PAID_GENUINE_THETA_STATIONARY_SIGNS_20261010.md)
tests the desired physical signs directly. It does not prove either
kernel positive definite, a uniform sign or global parameter coverage.

The [exact algebra replay](../numerics/check_laguerre_kernel_algebra.py)
checks the polynomial hierarchy, autocorrelation symbols and controls.
Analytic remainder and tail arguments are written proofs; exact finite
identities alone do not establish the theta targets.
