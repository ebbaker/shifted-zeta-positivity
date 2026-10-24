# Asymptotic mean shapes and their fluctuation terms

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.


**Status:** fixed-region negative-time coefficients derived in-note;
positive-time cosine-model identities derived in-note. Small floating
checks support the algebra. No numerical theta remainder bound,
positive-time theta transfer, or independent review is claimed.
This extends HDA-03–04 beyond the [opening models][opening].

## 1. Negative time: retain the regulator before taking its final limit

Write \(t=-T\), \(\phi_j=\Phi^{(j)}(0)\), and
\[
C_T=\frac{\phi_0\sqrt\pi}{2\sqrt T},\quad
a_0=\frac{\phi_2}{4\phi_0},\quad b_0=\frac{\phi_4}{32\phi_0},
\quad B=\frac{\pi\phi_0^2}{4\epsilon^2}.
\]
The unchanged theta source is even, smooth and rapidly decaying.
On a fixed compact complex domain its endpoint expansion is
\[
H(-T,z)=C_T\left[1+\frac{a_0-z^2/4}{T}
 +\frac{b_0-3a_0z^2/4+z^4/32}{T^2}+O(T^{-3})\right]. \tag{1}
\]
The same expansion can be differentiated any fixed finite number of
spatial times with the required Taylor order. To justify uniformity,
split the integral at a fixed small positive \(u_0\). On \([0,u_0]\),
Taylor-expand the even source and cosine with uniform remainders on
the compact \(z\)-buffer and integrate powers of \(u\) against
\(e^{-Tu^2}\). The remaining integral is exponentially small in \(T\),
using source decay to absorb the bounded complex-cosine growth. The
coefficients follow from Gaussian moments. This supplies an asymptotic
remainder class, not explicit numerical constants or a growing-domain
estimate. [DLMF background][refs] is cataloged at its inspected scope.

For a fixed spatial product kernel, centered in each coordinate with
common variance \(v\), the leading strict limit is
\[
\boxed{R(-T,z)=\frac{B}{4\pi T^3}(|z|^2+2v)+O(T^{-4}).} \tag{2}
\]
A fixed centered time average has the same leading coefficient. The
constants depend on the fixed regulator and complete averaging buffer.
This is a local fixed-region statement. On such a compact region (1)
actually gives no zeros for all sufficiently large \(T\); the nonzero
term in (2) is regularization background, not nonzero zero-count mass.

The factor \(B/T\) controls whether \(\epsilon^2\) dominates the
potential denominator. A more useful leading crossover expression is
\[
R_{\rm cross}(-T,z)=
\frac{B(|z|^2+2v)}{4\pi T^3(1+B/T)^2}. \tag{3}
\]
It retains the leading constant amplitude in the denominator. A still
more faithful candidate is to average the exact density of
\(H_G=C_Te^{-z^2/(4T)}\), retaining its spatial exponential as well.
Neither is asserted uniformly through all intermediate times.

For \(z=2+i/2\), spatial halfwidths \(1/2\),
\(\epsilon=10^{-4}\), the source quadrature gives
\(\phi_0\simeq0.44669690046712346\). The observed ratios are:

| T | Actual / strict T^-3 term | Actual / crossover (3) | Actual / averaged Gaussian |
| ---: | ---: | ---: | ---: |
| 1e+08 | 0.747386774 | 0.999998964 | 0.999998978 |
| 4e+08 | 0.926017028 | 0.999999722 | 0.999999726 |
| 1.6e+09 | 0.980694423 | 0.999999929 | 0.999999930 |

The strict limit can therefore be visibly inaccurate even at \(T=10^8\)
for this regulator. The crossover correction already captures most of
that discrepancy. These ratios are floating observations, not error
certificates. The diffusive regime \(z=\sqrt T\,\zeta\) from Note 01
remains a different boundary contract; it is not covered by (1)–(3).

For later boundary matching, the source also fixes the additive and
harmonic potential data. With \(d=x^2-y^2\), \(r^2=x^2+y^2\), spatial
fourth moment \(m_4\), and temporal variance \(v_t\), the corresponding
fixed-buffer expansion is
\[
\begin{split}
U={}&\log\epsilon^2+\frac B T
 +\frac{B(2a_0-d/2)-B^2/2}{T^2}\\
&+\frac1{T^3}\left[
 B\left(a_0^2+2b_0-2a_0d+
       \frac{d^2+4vr^2+2(m_4-v^2)}8\right)
 -B^2(2a_0-d/2)+\frac{B^3}3+Bv_t\right]+O(T^{-4}). \tag{3a}
\end{split}
\]
The \(Bv_t\) term is absent without time averaging. It comes from
averaging \(B/(T+s)\) over a fixed centered temporal window. Taking
\(\Delta/(4\pi)\) of (3a) recovers (2); the potential's extra constants
cannot be recovered from the density alone.

## 2. The first isotropic negative-time covariance is smaller and nonzero

Set \(d=x^2-y^2\), \(r^2=x^2+y^2\). Expanding
\(S=\log(|H|^2+\epsilon^2)\) from (1) gives, for the terms needed below,
\[
\begin{split}
S_x&=-\frac{Bx}{T^2}
 +\frac{(B/2)xd+(B^2-4a_0B)x}{T^3}+O(T^{-4}),\\
S_y&= \frac{By}{T^2}
 -\frac{(B/2)yd+(B^2-4a_0B)y}{T^3}+O(T^{-4}).
\end{split} \tag{4}
\]
The remainders here hold with the spatial derivatives needed below on
fixed compact buffers. Let the two independent spatial shifts have
variance \(v\) and fourth moment \(m_4\). Then
\[
\boxed{Q(-T,z)=-\frac{2B^2}{T^5}
                  \{v r^2+m_4-v^2\}+O(T^{-6}),} \tag{5}
\]
\[
\boxed{\Delta Q(-T,z)=-\frac{8B^2v}{T^5}+O(T^{-6}).} \tag{6}
\]
These are fixed-width, fixed-regulator expansions. The \(T^{-4}\)
variances of \(S_x\) and \(S_y\) cancel because the spatial variances
are equal. With unequal variances, the earlier term
\(B^2(v_x-v_y)T^{-4}\) is present.

For verification of (5), let \(X,Y\) denote the shifted coordinates.
Independence and symmetry imply
\[
\begin{split}
\operatorname{Cov}(X,X^3)&=3x^2v+m_4,\\
\operatorname{Cov}(X,XY^2)&=v(y^2+v),
\end{split}
\]
with the corresponding exchanged formulas. Substituting (4) into the
two variances gives (5); their identical linear corrections involving
\(a_0\) cancel. Differentiate (5) to obtain (6). Fixed centered time
averaging changes only subsequent orders: its variance contribution
starts at \(T^{-6}\). For time-only averaging, (5) has zero leading
coefficient and the next order must be analyzed separately.

The local gradient closure of [Note 04][closure] gives
\[
Q_\nabla=-\frac{2B^2v}{T^5}(r^2+2v)+O(T^{-6}). \tag{7}
\]
Hence its leading difference from (5) is the spatial constant
\(-2B^2(m_4-3v^2)T^{-5}\) for \(Q-Q_\nabla\).
It affects the potential equation but disappears under \(\Delta\).
Thus this closure captures the leading **density** fluctuation
contribution (6) even when the kernel's fourth moment is not Gaussian.
This does not make the complete potential evolution correct to that order.
The retained density contribution is
\(-\Delta Q/(8\pi)=B^2v/(\pi T^5)+O(T^{-6})\).

For the contract kernel, \(v=\ell^2/11\), \(m_4=3\ell^4/143\).
A separate control uses \(\epsilon=1\), \(\ell=1/2\), \(z=2+i/2\)
to reach this regime at more moderate times. Observed ratios to (5)–(6):

| T, with epsilon = 1 | Q / leading (5) | Laplacian Q / leading (6) |
| ---: | ---: | ---: |
| 1000 | 0.826269310 | 0.817384803 |
| 4000 | 0.952949143 | 0.950309707 |
| 16000 | 0.987993841 | 0.987304535 |

The controlled limit is supported by convergence; none of these three
finite times is labeled an asymptotically exact numerical certificate.
The \(\epsilon=1\) control is explicitly separate from the primary
\(10^{-4}\) pilot. Computing explicit derivative remainder constants
is still required before numerical boundary tolerances can be certified.

## 3. A whole-period cosine mean with its exact covariance

For the slice model \(H=M\cos(Lz)\), \(M,L>0\), set
\(\eta=\epsilon/M\), \(Y=Ly\), \(a=\sinh^2Y+\eta^2\), and
\(d_a=\sqrt{a(a+1)}\). A mean over one real period \(\pi/L\) gives
\[
U_c=2\log M+2\operatorname{arsinh}\sqrt a-2\log2,
\quad (U_c)_y=\frac{L\sinh(2Y)}{d_a}, \tag{8}
\]
\[
R_c=\frac{L^2\eta^2}{2\pi}
\frac{2a(a+1)+1-\eta^2(2a+1)}{d_a^3},
\qquad (U_c)_{yy}=4\pi R_c. \tag{9}
\]
The period mean of the logarithm follows by integrating
\(\langle(a+\cos^2X)^{-1}\rangle=1/d_a\) in \(a\), with its large-
\(a\) constant. This supplies a direct derivation of (8).

To calculate the covariance at any such slice, continue it by the exact
fixed-frequency heat solution \(M(t)=M_0e^{L^2t}\). Then
\[
(U_c)_t=2L^2\left(1-\frac{\eta^2}{d_a}\right),
\]
and the exact filtered potential equation gives
\[
\boxed{Q_c=4\pi R_c+(U_c)_y^2-4L^2+
                   \frac{4L^2\eta^2}{d_a}.} \tag{10}
\]
The covariance depends only on the slice, so this proves (10) for any
positive \(M,L\) at a frozen time. It does **not** prove that arbitrary
functions \(M(t),L(t)\) generate an exact heat field.
At \(y=0\),
\[
Q_c(0)=\frac{2L^2(1+2\eta^2)}{\eta\sqrt{1+\eta^2}}-4L^2
       =\frac{2L^2}{\eta}-4L^2+O(L^2\eta). \tag{11}
\]
The microscopic covariance is large near the line when the regulator
layer is narrow. Dropping it because the density is averaged is incorrect.
The new execution record checks (8)–(10) against 12 direct period
quadratures; the largest covariance discrepancy is below
\(1.1\cdot10^{-14}\). The earlier record checks (9) and its mass.

As \(\eta\downarrow0\), at fixed \(L\),
\[
R_c\rightharpoonup(L/\pi)\delta_0(y),\qquad
Q_c\rightharpoonup4L\delta_0(y). \tag{12}
\]
The first limit follows from concentration and transverse mass \(L/\pi\).
For the second, use (10): \((U_c)_y^2-4L^2\) and
\(4L^2\eta^2/d_a\) are uniformly bounded on compact \(y\)-sets and
converge to zero almost everywhere. Dominated convergence removes them.
This is a distributional transverse statement; the full spatial density
is the product with Lebesgue measure in \(x\), with infinite global mass.

## 4. Additional spatial or time averaging changes the covariance again

Let \(G\) be a further fixed positive average in \((t,y)\), applied
after the fixed-frequency period mean, and put \(V=G U_c\),
\(\bar R=G R_c\). The law of total covariance gives the exact correction
\[
\boxed{Q_{\rm total}=G Q_c-
          \{G[(U_c)_y^2]-(V_y)^2\}.} \tag{13}
\]
The mean \(x\)-gradient vanishes in each cell; the additional variance
of the mean \(y\)-gradient enters with a minus sign. In particular,
merely applying the new filter to \(Q_c\) loses a necessary term.
Equation (13) includes time averaging without averaging the parameters
first. It also makes clear how a history-dependent correction can arise.

For a fixed transverse kernel \(k_h\) in the limit (12),
\[
\bar R(y)=\frac L\pi k_h(y),\quad
V_y=2L(k_h*\operatorname{sgn})(y),\quad
Q_{\rm total}=4Lk_h(y)+(V_y)^2-4L^2. \tag{14}
\]
This is an explicit smooth average shape with a matching fluctuation
term in the cosine model. It preserves absolute zero intensity. It is
a more appropriate broad-average starting point than assuming the
small-window expansion remains accurate over an entire period.

For actual large-positive-time theta, the anticipated
\(L(t)\sim(\log t)/4\) would suggest intensity \(L(t)/\pi\), but
transferring (8)–(14) still requires uniform complex-field/carrier
estimates, source-tail control, the chosen number of periods and
moving-period/time-average commutators. The sibling fixed-label saddle
result does not pay those costs. No positive-time theta boundary value
has been certified in this round.

## 5. Consequence for a future boundary problem

The negative-time data should specify (2), (5), the source-fixed
harmonic/additive part of \(U\), and a remainder budget. The positive
end should specify a coarse mean shape together with (10) or (13) and
a theta transfer error. Both ends must use compatible regulators,
spatial scales and domains. The current work does not yet make that
boundary problem well posed; no reduced solution has been produced.
The [regulator bridge][regulator] separates these regularized statements
from claims about the actual averaged zero measure.

[opening]: 01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md
[closure]: 04_GRADIENT_CLOSURE_AND_ACTUAL_THETA_PILOT_20261024.md
[regulator]: 06_REGULATOR_BIAS_FOR_SMOOTHED_ZERO_COUNTS_20261024.md
[refs]: ../references/README.md
