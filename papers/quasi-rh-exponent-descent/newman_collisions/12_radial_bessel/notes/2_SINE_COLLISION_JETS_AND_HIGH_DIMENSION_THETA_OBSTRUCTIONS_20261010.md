# Sine collision jets and finite limits on radial theta geometry

10 October 2026. Prepared with substantial LLM assistance. Model: GPT-6
(Codex); the exact serving variant and configured reasoning effort are not
exposed and are not inferred. Checks are internal, not independent
mathematical review.

This continuation of [the positive three-dimensional lift](1_POSITIVE_THREE_DIMENSIONAL_THETA_LIFT_AND_NONLOCAL_GENERATOR_20261010.md)
has three results. The radial sine observation gives a clean signed
collision test with mirror coefficient 27. The genuine theta density
cannot be a nonnegative mixture of centered Gaussians, because its
squared-radius log-convexity determinant is negative. Its unique radial
inverse in dimension 11 is negative at the center throughout
\(0\le t\le1/20\), so no exact positive rotation-invariant realization
exists in any integer dimension at least 11. These statements constrain
two proposed shape mechanisms; they do not exclude genuine collisions.

## 1. A candidate-preserving sine observation

Use exactly the genuine state and nonlocal flow of Note 1:
\[
 m_t(u)=e^{tu^2}\Phi_e(u),\qquad
 R_{3,t}(r)=-\frac{m_t'(r)}{2\pi r},\qquad
 H_t(x)=2\pi\int_0^\infty r^2R_{3,t}(r)
                 \frac{\sin(xr)}{xr}\,dr.
\tag{1}
\]
Set
\[
 S_t(x)=\int_0^\infty rR_{3,t}(r)\sin(xr)\,dr
       =\frac{xH_t(x)}{2\pi},\qquad
 B_t(x)=\frac{xA_t(x)}{2\pi},\qquad Q_t=S_t/B_t.
\tag{2}
\]
Every derivative below is a raw \(x\) derivative at fixed time. The
normalizer \(A_t\) is the actual analytic factor of the collision
reduction, positive on the real axis, rather than a modulus substituted
on a complex neighborhood. Work locally at a positive candidate
\(x\ne0\), where \(B_t\ne0\). Then
\[
 H_t=H_t'=0\quad\Longleftrightarrow\quad S_t=S_t'=0.
\tag{3}
\]
Multiplication by \(x\) is therefore safe for this joint observable.
It also adds an origin zero, which matters for the threshold mirror test.

Write \(S_j=\partial_x^jS_t(x)\). At (3), product differentiation gives
\[
 H_2=\frac{2\pi}{x}S_2,\quad
 H_3=\frac{2\pi}{x}\left(S_3-\frac{3S_2}{x}\right),\quad
 H_4=\frac{2\pi}{x}\left(S_4-\frac{4S_3}{x}
                                      +\frac{12S_2}{x^2}\right).
\tag{4}
\]
The actual normalized target of [Heat Note 12](../../notes/12_THRESHOLD_COLLISION_JETS_AND_PAID_LAGUERRE_TEST_20261009.md)
is
\[
 \mathcal L(q)=2q_3^2-3q_2q_4-
 \left(18\partial_x^2\log A_t+\frac9{x^2}\right)q_2^2,
 \qquad q_j=Q_t^{(j)}(x).
\tag{5}
\]
At an exact collision its product-rule identity is
\(A_t^2\mathcal L=2H_3^2-3H_2H_4-9H_2^2/x^2\).
Substitution of (4) cancels the mixed \(S_2S_3/x\) terms and yields
\[
 \boxed{B_t^2\mathcal L(q)
      =2S_3^2-3S_2S_4-\frac{27}{x^2}S_2^2.}
\tag{6}
\]
The sign of this expression is necessary nonnegative at an all-real
threshold double collision. Positivity of \(R_{3,t}\) does not itself
fix that sign: the moments are signed oscillatory integrals,
\[
 S_j=\int_0^\infty r^{j+1}R_{3,t}(r)
                          \sin(xr+j\pi/2)\,dr.
\tag{7}
\]
In particular \(S_2=-\int r^3R\sin(xr)\),
\(S_3=-\int r^4R\cos(xr)\), and \(S_4=\int r^5R\sin(xr)\).
The positive radial lift remains an exact representation of the signed
problem, rather than a new coercivity theorem.

For a collision of multiplicity \(m\ge2\), retain all vanishing lower
jets. Let \(\mathcal E_m(q)\) denote the full deflated necessary test,
\[
 \mathcal E_m(q)=\frac{q_{m+1}^2}{(m+1)^2}
 -\frac{2q_mq_{m+2}}{(m+1)(m+2)}
 -\left(\partial_x^2\log A_t+\frac{m}{4x^2}\right)q_m^2.
\tag{8}
\]
Since \(\partial_x^2\log B_t=\partial_x^2\log A_t-1/x^2\),
the exact sine version is
\[
 B_t^2\mathcal E_m(q)=
 \frac{S_{m+1}^2}{(m+1)^2}
 -\frac{2S_mS_{m+2}}{(m+1)(m+2)}
 -\frac{m+4}{4x^2}S_m^2.
\tag{9}
\]
Equation (6) is 18 times (9) for \(m=2\). Multiplicities three and four
use sine jets through five and six. A fourth-jet test alone remains
vacuous at multiplicity at least four. The replay verifies (9) as a
polynomial identity for \(m=2,\ldots,6\).

## 2. Cutoff endpoints and paid transfer remain explicit

For \(U\ge1\), put \(S_t^U=\int_0^U rR_{3,t}(r)\sin(xr)\,dr\).
The corresponding theta-axis cutoff is not just \(2\pi S_t^U/x\):
\[
 \int_0^U m_t(u)\cos(xu)\,du
 =\frac{m_t(U)\sin(xU)}{x}+\frac{2\pi}{x}S_t^U(x).
\tag{10}
\]
Every derivative of this endpoint must be retained when comparing the
two finite observations. The nonlocal generator in Note 1 is unchanged.

The established bound
\(R_{3,t}(r)\le150\exp(tr^2+13r-\pi e^{4r})\), \(r\ge1\),
gives, uniformly for \(0\le t\le T=1/20\),
\(|\operatorname{Im}z|\le Y=1\), and \(0\le j\le6\),
\[
 |S_t^{(j)}(z)-(S_t^U)^{(j)}(z)|
 \le \frac{150U^{j+1}
       \exp(TU^2+(13+Y)U-\pi e^{4U})}
      {4\pi e^{4U}-2TU-(13+Y)-(j+1)/U}.
\tag{11}
\]
The denominator is positive already at \(U=1\). The logarithm of the
envelope has negative decreasing derivative on \([U,\infty)\), which
proves this integral-tail estimate. Normalized errors follow from the
complete product rule
\[
 (Q_t-S_t^U/B_t)^{(j)}
 =\sum_{k=0}^j\binom jk (B_t^{-1})^{(k)}
       (S_t-S_t^U)^{(j-k)}.
\tag{12}
\]
Thus the same holomorphic-interface and measured quadratic payment from
Heat Note 12 apply. Equation (6) is an exact-candidate identity. It must
not be imposed directly on an approximate finite candidate without
paying its lower-jet defects and normalizer products. No exponentially
small oscillatory value is certified by evaluating the full transform
at modest precision in this continuation.

## 3. The genuine theta density fails a Gaussian-mixture shape test

A useful stronger property than radial positivity would be
\[
 f_t(v):=m_t(\sqrt v)=\int e^{-av}\,d\nu_t(a),\qquad v\ge0,
\tag{13}
\]
with \(\nu_t\) a nonnegative finite measure on \([0,\infty)\).
This would realize the one-dimensional density as a nonnegative mixture
of centered Gaussians. Where the first two moments of the measure exist,
Cauchy--Schwarz gives
\[
 f_t(v)f_t''(v)-f_t'(v)^2\ge0.
\tag{14}
\]
The same necessary inequality holds even for a positive mixture over
real \(a\) whenever these integrals are finite. If the moments were
initially not assumed finite, the finite smooth derivatives of (13) at
zero force them for \(a\ge0\), by monotone difference quotients.

Even smoothness gives
\[
 f_0(0)=\Phi(0),\quad f_0'(0)=\frac{\Phi''(0)}2,
 \quad f_0''(0)=\frac{\Phi^{(4)}(0)}{12}.
\tag{15}
\]
Since \(f_t=e^{tv}f_0\), its determinant at zero is independent of time:
\[
 f_t(0)f_t''(0)-f_t'(0)^2
 =\frac{\Phi(0)\Phi^{(4)}(0)}{12}
       -\frac{\Phi''(0)^2}{4}
 \in[-38.050,-38.048].
\tag{16}
\]
This contradicts (14). Hence (13) is impossible for every time, including
the full scout range. Positive scalar normalization does not change the
sign. This result concerns the exact genuine density and positive
mixtures; it makes no claim against complex Gaussian decompositions,
analytic Gaussian germs, or a different observable.

## 4. A negative central inverse in dimension 11

An exact positive radial realization in successively higher dimensions
is another possible shape constraint. Integrating out two coordinates
of a radial density gives
\[
 R_{d-2,t}(r)=2\pi\int_r^\infty R_{d,t}(s)s\,ds,
 \qquad R_{d,t}=-\frac{1}{2\pi r}\partial_rR_{d-2,t}.
\tag{17}
\]
Starting with the axis marginal \(R_{1,t}=m_t\), the unique odd-dimensional
Schwartz radial inverse is
\[
 R_{2k+1,t}(r)=\left(-\frac1{2\pi}\right)^k
          \left(\frac1r\partial_r\right)^k m_t(r),
 \qquad
 R_{2k+1,t}(0)=
 \frac{(-1)^k m_t^{(2k)}(0)}{(2\pi)^k(2k-1)!!}.
\tag{18}
\]
The center formula follows directly from the even Taylor expansion:
\((r^{-1}\partial_r)^k r^{2k}=2^kk!\).
Even smoothness removes the apparent origin singularities. The theta
decay makes every such inverse Schwartz; (17) can be integrated back
without a boundary ambiguity.

For \(k=5\), the genuine tenth jet is
\[
\begin{aligned}
 m_t^{(10)}(0)={}&\Phi^{(10)}(0)+90t\Phi^{(8)}(0)
 +2520t^2\Phi^{(6)}(0)+25200t^3\Phi^{(4)}(0)\\
 &+75600t^4\Phi''(0)+30240t^5\Phi(0).
\end{aligned}
\tag{19}
\]
The certificate encloses it on the entire time interval by
\[
 3.3580\cdot10^{11}<m_t^{(10)}(0)<3.3688\cdot10^{11},
 \qquad -36403<R_{11,t}(0)<-36287.
\tag{20}
\]
In particular the inverse is strictly negative at the center. It cannot
be a nonnegative density. This also rules out any positive finite
rotation-invariant measure with the same axis marginal: its radial
characteristic function is fixed by that marginal, and Fourier
uniqueness forces the smooth inverse (18). Equivalently, the prescribed
characteristic function is Schwartz on each finite-dimensional space,
so a representing measure necessarily has this density. A positive
rotation-invariant realization in any integer \(d\ge11\) would project
to one in dimension 11, giving a contradiction.

This is a finite upper obstruction, not a classification of the allowed
dimensions. Note 1 proves dimension 3; dimensions 4 through 10 have not
been certified here. The statement is about positive rotation-invariant
realizations with the exact axis marginal. It does not rule out signed,
anisotropic, constrained analytic, or supersymmetric representations.

## 5. Reproducible center certificates

For the \(n\)-th theta summand at the center, define integer polynomials
\[
 P_0(a)=2a^2-3a,\qquad P_{j+1}(a)=P_j(a)+4a(P_j'(a)-P_j(a)).
\]
Termwise differentiation gives
\[
 \Phi^{(j)}(0)=\sum_{n\ge1}e^{-\pi n^2}P_j(\pi n^2),
 \quad \deg P_j=j+2.
\tag{21}
\]
The replay sums \(n=1,\ldots,5\) by outward Decimal arithmetic of
precision 60. It encloses \(\pi\) by rational Machin alternating-series
bounds, and positive exponentials by 300-term Taylor sums plus geometric
tails; reciprocal intervals enclose negative exponentials. No floating
transcendental call or unvalidated center sample enters (16) or (20).

For \(C_j\) the sum of the absolute polynomial coefficients, the
remaining infinite theta series has the absolute bound
\[
 \left|\sum_{n\ge6}e^{-\pi n^2}P_j(\pi n^2)\right|
 \le \frac{C_j\pi^{j+2}6^{2j+4}e^{-36\pi}}
 {1-(7/6)^{2j+4}e^{-13\pi}}.
\tag{22}
\]
Indeed \(a\ge1\) implies \(|P_j(a)|\le C_ja^{j+2}\), and the
successive ratio of \(n^{2j+4}e^{-\pi n^2}\) decreases from \(n=6\).
For \(j=10\), (22) is less than \(4.763\cdot10^{-12}\); lower jets
have smaller payments. All intervals in (19) use \(t\in[0,0.05]\)
without an unjustified monotonicity assumption.

See [the checker](../numerics/check_radial_center_obstructions.py),
[retained record](../numerics/CENTER_OBSTRUCTIONS_CHECK_RECORD_20261010.json),
and [scoped internal review](../reviews/2_RADIAL_CONTINUATION_INTERNAL_REVIEW_20261010.md).
The checked obstructions concern the genuine theta kernel. They are not
independent validation of the analytic collision theory.

## 6. The next bounded signed task

The dimension-three sine expression (6) is the useful surviving target.
A new theta-specific property must control its oscillatory signed
moments, preserve (3), and transfer through (10)--(12). Positive Gaussian
mixing and positivity in arbitrarily high radial dimension cannot supply
that property. Testing the exact inverses in dimensions 5, 7 and 9 is a
bounded geometry classification task, but even success would still need
a separate candidate-conditioned sign argument. The available positive
radial controls remain the visibility tests. No RH or positive-time
collision exclusion is claimed.
