# Theta Fock norm, paid coefficient tails, and the joint observation kernel

10 October 2026. Model: GPT-6 (Codex); exact serving variant and configured
reasoning effort unavailable. Algebraic cross-checks are internal LLM checks.

This bounded scout follows [Program 02 in Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md)
and [Heat Note 13](../../notes/13_RECENT_HEAT_RESULTS_AND_PATHS_FORWARD_20261009.md).
It uses a direct holomorphic embedding, rather than the unitary Bargmann
transform of the real-axis function. Those are different states.

## 1. Genuine data, domain, and time orientation

Let \(\Phi_e\) be the full even extension of
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}}\quad(u\ge0).
\]
It is positive, even, and super-exponentially decaying. Put
\[
d\nu_t(u)=e^{tu^2}\Phi_e(u)\,du,\qquad
f_t(z)=\tfrac12\int_{\mathbb R}e^{izu}\,d\nu_t(u)=H_t(z).
\tag{1}
\]
The factor \(1/2\) makes this precisely the manuscript's half-line
cosine integral, hence \(f_0(z)=\xi(1/2+iz/2)/8\).
The bounded first instance uses width \(a=1\), comparison width \(a'=2\),
and \(1/25\le t\le1/20\), \(1\le\kappa\le6/5\),
\(x=4\pi e^{\kappa/t}\). General widths are kept in the formulas to make
their scale dependence explicit. For real \(t\), define
\[
\|f\|_a^2=(\pi a)^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2/a}\,d^2z.
\]
On every compact time interval, all integrals below and all finite
time/spatial derivatives are dominated by the theta decay. Thus
\[
\partial_t f_t=-\partial_z^2f_t,\qquad
c_j'(t)=-(j+2)(j+1)c_{j+2}(t),\quad
f_t(z)=\sum_{j\ge0}c_j(t)z^j.
\tag{2}
\]
The Fock generator is a lowering operator with a minus sign. A number
operator contraction does not reproduce (2). No general bounded backward
heat semigroup on all of \(\mathcal F_a\) is asserted.

## 2. An exact theta norm and a paid Fock truncation

Gaussian integration gives
\[
\langle e^{iuz},e^{ivz}\rangle_a=e^{auv}\quad(u,v\in\mathbb R).
\]
With the inner product linear in its first entry, Fubini yields the exact
identity
\[
\boxed{\|H_t\|_a^2=\tfrac14\int_{\mathbb R^2}
e^{auv}\,d\nu_t(u)d\nu_t(v)
\le H_{t+a/2}(0)^2<\infty.}
\tag{3}
\]
The inequality uses \(uv\le(u^2+v^2)/2\). Absolute integrability needed
for Fubini follows from that same bound applied before interchange. This
also proves norm convergence without needing an unquantified order estimate.

Orthogonality of monomials gives
\[
\|H_t\|_a^2=\sum_{j\ge0}a^jj!|c_j(t)|^2,\qquad
c_{2k}=\frac{(-1)^k}{(2k)!}\int_0^\infty u^{2k}e^{tu^2}\Phi(u)\,du,
\quad c_{2k+1}=0.
\tag{4}
\]
Fix \(a'>a\), and truncate at degree \(m\), \(T_m=\sum_{j=0}^m c_jz^j\).
The extra width pays the full tail:
\[
\|H_t-T_m\|_a
\le (a/a')^{(m+1)/2}H_{t+a'/2}(0)=:\epsilon_m.
\tag{5}
\]
At the selected widths this is
\(\epsilon_m=2^{-(m+1)/2}H_{t+1}(0)\).
Because odd coefficients vanish, truncation at degree \(2k\) allows the
sharper exponent \(k+1\) on \(a/a'\). Formula (5) is an absolute
representation payment, not a signed arithmetic estimate.

At a fixed real height, bounded evaluation pays
\[
|H_t(x)-T_m(x)|\le e^{x^2/(2a)}\epsilon_m,
\quad
|H_t'(x)-T_m'(x)|
\le e^{x^2/(2a)}\sqrt{1/a+x^2/a^2}\,\epsilon_m.
\tag{6}
\]
These bounds can be very expensive in the shrinking-time sector where
\(x=4\pi e^{\kappa/t}\). Increasing \(m\) until a desired tolerance is met
is a valid finite-height payment; (6) is not an efficient uniform
high-height certificate. Direct normalized comparison divides by \(A_t(x)\)
and retains \(Q_t'=A_t^{-1}(H_t'-bH_t)\), \(b=\partial_x\log A_t\).
For higher jets use
\[
Q_t^{(j)}=A_t^{-1}\sum_{r=0}^j\binom jr
d_{j-r}H_t^{(r)},\quad d_0=1,\quad d_{k+1}=d_k'-bd_k.
\]
Derivative evaluation bounds of any finite order follow from the same
reproducing kernel; no normalization derivative can be discarded.

## 3. Exact joint kernel geometry

For real \(x\), value and derivative kernels are
\[
k_0(z)=e^{zx/a},\qquad k_1(z)=(z/a)e^{zx/a}.
\]
Their Gram matrix and determinant are
\[
G=e^{x^2/a}
\begin{pmatrix}1&x/a\\x/a&1/a+x^2/a^2\end{pmatrix},
\qquad \det G=e^{2x^2/a}/a>0.
\tag{7}
\]
Let \(\Pi_x\) project onto their span. Inverting (7) gives
\[
\boxed{\|\Pi_xf\|_a^2=e^{-x^2/a}
\left(|f(x)|^2+a|f'(x)-xf(x)/a|^2\right).}
\tag{8}
\]
Consequently the exact missing energy is
\[
\|f\|_a^2=e^{-x^2/a}
\left(|f(x)|^2+a|f'(x)-xf(x)/a|^2\right)
+\|(I-\Pi_x)f\|_a^2.
\tag{9}
\]
The factor multiplying the observations in (8) is part of the geometry;
positive determinant does not constrain the final term in (9).
The even subspace still contains \((z^2-x^2)^2\) in this kernel.

## 4. Testing an actual coefficient restriction

A concrete candidate restriction is (4): evenness, alternating Taylor
coefficients, and positive even moment Hankel matrices. These properties
do hold for the genuine theta kernel. They do not exclude a common
real zero for the larger positive-kernel class.

Use the smooth positive control already derived in the Gaussian scout:
\[
\varphi(u)=e^{-\cosh u},\quad
p_b(u)=\tfrac12\varphi(u)+\tfrac14\varphi(u-2b)
+\tfrac14\varphi(u+2b),\quad
q_{T,b}(u)=e^{-Tu^2}p_b(u).
\]
Its backward heat flow at \(T>0\) is
\[
J_T(z)=\int_{\mathbb R}p_b(u)e^{izu}\,du
=B(z)\cos^2(bz),\quad B(z)=\int_{\mathbb R}\varphi(u)e^{izu}\,du.
\tag{10}
\]
For any \(x_*=\pi/(2b)\) with \(B(x_*)\ne0\), \(J_T\) has an exact
double zero. Its initial kernel is positive, even, smooth and
super-exponentially decaying. Therefore (3)--(6) apply at every width,
and its Taylor coefficients have precisely the alternating-moment sign
pattern in (4). Moment Gram matrices remain positive. At the collision
its nonzero state has zero observed projection in (8).
This is a test of that coefficient restriction, not a theta collision.

The quartic threshold control also lies in every Fock space and prevents
an inference from (7) to a threshold-jet sign. At a genuine collision,
normalizer terms cancel to give the exact interface
\[
2q_3^2-3q_2q_4-(18b'+9/x^2)q_2^2
=A_t^{-2}\{2H_t'''{}^2-3H_t''H_t''''-9H_t''{}^2/x^2\}.
\tag{11}
\]
Neither (3) nor (8) fixes the mixed second/fourth product's sign.

## 5. Result and continuation

The scout supplies an exact theta Hilbert representation, an explicit
coefficient truncation payment, and a sharp identity identifying the
unobserved energy. It disproves a universal positive-norm or
alternating-coefficient coercivity argument in the stated class.
It establishes no theta-specific angle estimate or collision exclusion.

The next useful task would constrain \((I-\Pi_x)H_t\) conditional on
the two vanishing observations using an independently derived
theta relation. A reproducing-kernel upper bound or an improved coefficient
tail alone does not provide that relation. The large loss in (6) is a
separate practical reason to prefer a centered, actual-height representation.

The kernel conventions agree with the classical Bargmann architecture
cited in Note 14: [Bargmann, 1961](https://doi.org/10.1002/cpa.3160140303).
The DOI landing page was inaccessible in this scout's source check; no
statement here depends on uninspected text from that paper. Equations
(3)--(11) were derived directly. Storage follows
[LARGE_FILES.md](../../../../../LARGE_FILES.md); no large data were produced.
