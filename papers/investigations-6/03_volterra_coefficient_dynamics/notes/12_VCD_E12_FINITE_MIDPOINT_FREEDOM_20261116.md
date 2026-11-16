# VCD-E12 r1 — Complex midpoint remainder with finite calibration

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded task dispatch **gpt-6.1-sol / ultra**.
Separate runtime model and effort attestation unavailable.

**Complete, proved in-note.** This is a source-information diagnostic in
the smooth compact-multiplier class of the [frozen request][request] and
[B04 decision][b04]. The finite measurements leave an open disk of
possible omitted contributions at the prescribed point. See the
[result index][results], [coefficient cluster][cluster],
[control catalog][catalog], [avoid index][avoid] and patterns
[01][a01], [02][a02] and [07][a07].

## 1. Finite measurements and two independent targets

Fix integers \(L\ge N\ge1\) and \(r\ge0\), a point \(z_*=x+iy\) with
\(x\ne0\) and \(0<|y|<4\), and the canonical time-zero measure
\(d\mu=\Phi\,du/Z\), where \(Z=\int_{\mathbb R}\Phi\).
Set \(V=-\log\Phi\). Keep the exact canonical symbols
\(V'=8\pi\sinh(4u)+b(u)\) and \(b\) from [E06 §2][e06].
Both symbols are odd, \(b\) is bounded, and
\(e^{-4u}V'(u)\to4\pi\) at positive infinity.
The real orthonormal polynomial \(q_n\) for \(\mu\) has parity \(n\)
and positive leading coefficient.

For a measure \(\sigma\) in the class under consideration, let
\[
 F_\sigma(z)=\int_{\mathbb R}e^{izu}\,d\sigma(u),\qquad
 c_{\sigma,n}(z)=\int_{\mathbb R}q_{\sigma,n}(u)e^{izu/2}\,d\sigma(u).
\]
All exponential moments exist by the theta tails and the bounded
multipliers. On each compact \(z\)-set the differentiated integrands
are dominated by a polynomial times \(e^{C|u|}\) for some finite
\(C\), so these formulas give the entire functions and their
derivatives. The polynomials are complete in \(L^2(\sigma)\):
orthogonality of \(f\in L^2(\sigma)\) to all of them makes every
Taylor coefficient of \(\int\bar f(u)e^{izu}\,d\sigma(u)\) vanish.
This transform is entire by Cauchy–Schwarz and the exponential
moments. Fourier uniqueness for finite measures then gives \(f=0\).
Applying the bilinear Parseval identity of [E13 §§1–2][e13] to
\(e^{izu/2}\) yields the full-chain formula
\[
 F_\sigma(z)=\sum_{n\ge0}c_{\sigma,n}(z)^2,qquad
 R_{\sigma,N}(z)=F_\sigma(z)-\sum_{n<N}c_{\sigma,n}(z)^2.
\]
The square sum is absolutely convergent by Hermitian Parseval,
which gives \(\sum_n|c_{\sigma,n}(z)|^2=
\int e^{-(\operatorname{Im}z)u}\,d\sigma(u)\).

Let \(X=C_c^\infty(0,\infty;\mathbb R)\) and identify a member with
its even extension \(h(u)=g(|u|)\). This is smooth and vanishes near
zero. Collect the real measurement functionals in a finite linear map
\(A:X\to\mathbb R^m\) using integration against \(h\,d\mu\) of
the following symbols.

- \(u^k\) for \(0\le k\le2L\).
- \(V'q_iq_j\) and \(bq_iq_j\) for \(0\le i,j\le L\).
- The real and imaginary parts of
  \(B_{nj}(u)=q_n(u)(iu/2)^j e^{iz_*u/2}\) for
  \(0\le n<N\) and \(0\le j\le r\).

The complex target functional is \(T(h)=\int\cos(z_*u)h(u)\,d\mu(u)\).
These tests see only the even parts of the symbols. In the polynomial
measurements odd powers vanish, and in the score measurements the
symbols vanish upon symmetrization when \(i+j\) is even. In the jet
measurements the even part on \(u>0\) is
\[
 B_{nj}^{+}(u)=q_n(u)(iu/2)^j\,
      \frac{e^{iz_*u/2}+(-1)^{n+j}e^{-iz_*u/2}}{2}.
\]
The integral of each evenized symbol against \(h\,d\mu\) is twice
its integral against \(g\,d\mu\) on \((0,\infty)\).

Suppose a nonzero real combination of the two components of \(T\)
lies in the real span of the rows of \(A\). Write the combination
as \(\operatorname{Re}(\alpha T)\) with \(\alpha\ne0\). Bump
testing against \(g\in X\) then gives, for all \(u>0\),
\[
 \operatorname{Re}(\alpha\cos(z_*u))
   =P(u)+V'(u)Q(u)+b(u)S(u)+E(u).                         \tag{1}
\]
Here \(P\) is an even real polynomial, \(Q,S\) are odd real
polynomials, and \(E\) is a finite real combination of real and
imaginary parts of the evenized jet symbols. These are polynomial
multiples of \(e^{\pm iz_*u/2}\) and their conjugates.
Continuity and the strictly positive density justify the pointwise
equality. Any nonzero difference at a positive point has a
constant, nonzero sign on a neighborhood there, where a nonnegative
bump gives a nonzero integral.

Put \(v=|y|\). For some finite integer \(d\) the bound
\(|E(u)|=O((1+u)^d e^{v u/2})\) holds, while \(P+bS\) has
polynomial growth. If \(Q\ne0\), divide (1) by
\(u^{\deg Q}e^{4u}\) and let \(u\to+\infty\).
The \(V'Q\) term tends to \(4\pi\) times the nonzero leading
coefficient of \(Q\). All other terms tend to zero since \(v<4\),
a contradiction. Thus \(Q=0\).

Write \(s=\operatorname{sgn}(y)\). The identity
\[
 \cos(z_*u)=\tfrac12 e^{vu-isxu}+\tfrac12 e^{-vu+isxu}
\]
implies that a sequence \(u_k\to+\infty\) with
\(\operatorname{Re}(\alpha e^{-isxu_k})=|\alpha|\) satisfies
\[
 e^{-vu_k}\operatorname{Re}(\alpha\cos(z_*u_k))
     \longrightarrow |\alpha|/2.
\]
Such positive peaks recur because \(x\ne0\). With \(Q=0\), the
right side of (1) divided by \(e^{vu_k}\) tends to zero, giving
the contradiction.

If \(T(\ker A)\) were a proper real subspace of \(\mathbb C\),
a nonzero linear form \(\operatorname{Re}(\alpha\,\cdot)\)
would annihilate it. The rule \(Ah\mapsto\operatorname{Re}(\alpha T(h))\)
would then be well defined on \(\operatorname{ran}A\).
Extending it linearly to \(\mathbb R^m\) would give the dependence
just excluded. This step allows redundant rows of \(A\).
Choose fixed even extensions \(h_1,h_2\) from \(\ker A\) with
\(T(h_1)=1\) and \(T(h_2)=i\).

## 2. Exact matches and attainable disk

For real \(\eta=(\eta_1,\eta_2)\), set
\(H_\eta=\eta_1h_1+\eta_2h_2\) and
\(d\nu_\eta=(1+H_\eta)d\mu\).
The zeroth moment constraint gives mass one. Take \(\|H_\eta\|_\infty<1/2\)
to ensure strict positivity. The source \(\Psi_\eta=(1+H_\eta)\Phi\)
equals \(\Phi\) on a neighborhood of zero and on both real tails.
In particular it has the entire smooth reflection jet.

Every moment through degree \(2L\) agrees by \(Ah_1=Ah_2=0\).
The Gram matrix of \(1,u,\ldots,u^L\) uses precisely moments from
that range. It is positive definite by positivity of the density,
so orthonormalization with positive leading coefficients gives
\(q_{\nu_\eta,j}=q_j\) for \(j\le L\). The link \(a_j\)
is the ratio of leading coefficients of \(q_{j-1}\) and \(q_j\),
so the links agree through \(a_L\).
The remaining rows of \(A\) now give the exact integrals of the
unchanged canonical \(V'\) and \(b\) against every \(q_iq_j\)
for \(i,j\le L\) and the exact derivatives of the full-chain
amplitudes \(c_{\nu_\eta,n}^{(j)}(z_*)\) for \(n<N,\ j\le r\).
Using the common polynomials makes these jet constraints linear
in the multiplier.

The literal exponential Fourier readout reduces to its cosine
part by evenness. Using \(j=0\) among the preserved jets in the
bilinear formula gives
\[
 R_{\nu_\eta,N}(z_*)-R_{\mu,N}(z_*)
   =F_{\nu_\eta}(z_*)-F_\mu(z_*)=\eta_1+i\eta_2.              \tag{2}
\]
Thus the response is the restriction of an invertible real-linear
map \(\mathbb R^2\to\mathbb C\).

For a prescribed own-to-canonical score tolerance \(\delta>0\),
put
\[
 K_0=\sum_{j=1}^2\|h_j\|_\infty,\qquad
 K_1=\sum_{j=1}^2\|h_j'\|_\infty,\qquad
 K_u=\sum_{j=1}^2\|u h_j'\|_\infty,\qquad
 \rho=\min\{1/(2K_0),\ \delta/(2K_1),\ 1/(8K_u)\}.
\]
The three constants in the denominators are finite and positive
since each test direction is nonzero, smooth and compactly supported
away from zero. For \(|\eta|_2<\rho\), the sup norms of
\(H_\eta,H_\eta',uH_\eta'\) are at most \(|\eta|_2\) times their
respective constants. The tilted source has own score
\[
 V_{\Psi_\eta,\lambda}'=V_\lambda'-\frac{H_\eta'}{1+H_\eta},
 \qquad V_\lambda' = V'-2\lambda u .
\]
Its own-score distance is less than \(\delta\). Moreover the
perturbation to \(uV_\lambda'\) is bounded in absolute value by
\(2|\eta|_2 K_u<1/4\). The [manuscript confinement proof][ms]
gives \(uV_\lambda'\ge -27/4\) and \(\cosh(4u)<4\) for
\(|u|\le1/2\), and \(uV_\lambda'\ge e^{4|u|}\) for
\(|u|\ge1/2\), uniformly on \(0\le\lambda\le1/2\).
Hence the canonical slack above \(\cosh(4u)-11\) is at least
\(1/4\) everywhere. The perturbed score still satisfies that
confinement bound. The tilted sources coincide off the test
supports before normalization, so the required tails and
integrability for the confinement lemma are preserved. It gives
\[
 \beta_{\Psi_\eta,j}(\lambda)+\beta_{\Psi_\eta,j+1}(\lambda)
    \le\frac{\operatorname{arcosh}^2(2j+12)}{16},
 \qquad j\ge0,\quad 0\le\lambda\le1/2.
\]
The score tolerance and envelope hold throughout the time band.
The exact probability calibration is at \(\lambda=0\).
By (2) the open disk of displacements of radius \(\rho\) is
attained. This gives a nonzero displacement in every direction
from the canonical value. The radius is for the fixed data
\(L,N,r,z_*,\delta\) and the two constructed functions.

## 3. Disconnected tail jets

Use the [E04][e04] realization of the disconnected Jacobi tail
\(J^{[N]}\), rooted at \(e_N\). Its entire fixed-vector response is
\(k_N(w)=\langle e_N,e^{iwJ^{[N]}}e_N\rangle\).
Both sources have complete polynomials and the same logarithmic
envelope, so the tail self-adjointness and power-series arguments
of E04 §§2, 4 apply. Its derivative of order \(p\) at zero is
\(i^p\langle e_N,(J^{[N]})^p e_N\rangle\), a weighted sum of
length-\(p\) return walks. A walk using an edge beyond \(a_L\)
must reach site \(L+1\) and return, so has length at least
\(2(L-N+1)\). Thus the jets agree through order
\(2(L-N)+1\), including all odd orders in that range, which
vanish because each step reverses site parity. At the first
even order beyond this range the extra monotone return walk
contributes \((-1)^{L-N+1}\prod_{j=N+1}^{L+1}a_j^2\)
relative to the compression to sites \(N,\ldots,L\).
That contribution involves \(a_{L+1}\), beyond the matched
prefix, so the prefix alone gives no equality at that order.
In particular, when \(L=N\), it pays only \(k_N(0)=1\) and
\(k_N'(0)=0\) before the first even derivative. The same
prefix-based guarantee applies to the rescaled response
\(k_N(z/2)\), with the factor \(2^{-p}\) in the \(p\)-th derivative.

## 4. Source distinctions and scope

For \(\eta\ne0\) the response in (2) is nonzero, hence
\(H_\eta\ne0\). Pointwise equality of own and canonical scores
would force \(H_\eta'=0\) everywhere, which is incompatible
with a nonzero compactly supported test. These sources also
fail the constant square-source arithmetic in [E10 §2][e10].
In that class the proposed representation on \(u>0\) uses
the same mode functions \(s_m\) with constant coefficients and
converges absolutely at one positive point. The least changed
coefficient would give a nonzero limit of
\((\Psi_\eta-\Phi)/s_k\) on the positive tail by the mode ratio
bound and dominated convergence of E10. This contradicts exact
tail equality. Using all canonical coefficients would give
\(\Phi\) on the whole half-line, contradicting \(H_\eta\ne0\)
and evenness.

The source and readout premises screen the existing catalog as
follows. These are comparisons of the stated premises, using
the cited controls at their established scopes.

| Control | Relevant premise comparison |
| --- | --- |
| Euler-factor translates | Exact real theta tails and bounded own-to-canonical score difference fail. The time-zero normalized second moment also changes. |
| Weighted-square examples and finite-prime orbit controls | Full canonical reflection fails. Their checked finite measurements and collision claims retain their own scopes. |
| Finite-source changes, including E07 | E07's finite square-mode changes fail full smooth reflection. Its proved nonreal zeros concern that class. The joint \(b\) and midpoint calibration here is a separate test. |
| Reflected super-Gaussian | Exact theta tails and bounded difference from the exponential canonical score fail. |
| Smooth shape and positive-primitive controls | Canonical square-source arithmetic fails. The sufficiently small damping sources in the E07 screen also fail bounded own-to-canonical score difference. |
| Finite atoms and compact triangular extensions | Strictly positive smooth full-line density fails. |
| RH-conditional normalized endpoint control | Ordinary Dirichlet series arithmetic fails. Preserving the leading tail is weaker than equality on both real tails. Its zero statement retains the RH hypothesis. |
| Fixed amplitude with variable observation | The varied observation fails the literal Fourier readout. |
| Actual-profile positive-measure relaxation | The relaxation supplies no such positive full-line source with its literal Fourier readout. |

[E07 and its catalog screen][e07] supply the finite square-source
comparison. [E10][e10] supplies the compact-multiplier method and
changes the next adjacent score defect while retaining lower
ones. Here all score entries for the listed indices are fixed,
and the varied quantity is the complex omitted contribution.
The zeros of the smooth controls remain open. The displacement
disk concerns deviations from the canonical remainder. It gives
no sign assertion for the remainder itself and no inference of
a zero at any prescribed point.

The obstruction is to exact determination of \(R_N(z_*)\) from
the listed finite data in this smooth compact-multiplier class.
The full function \(c_{\sigma,0}(z)=F_\sigma(z/2)\) already
determines the readout, and no rate in growing degree, quantitative
source-distinguishing constraint, or zero estimate follows from
the radius. Further mechanism decisions belong to [B04][b04].

[request]: ../research-progress/handoffs/VCD-E12-r1.md
[b04]: ../brainstorm/notes/07_VCD_B04_JOINT_MIDPOINT_INFORMATION_DECISION_20261116.md
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[e04]: 04_VCD_E04_TAIL_FOUNDATIONS_20261116.md
[e06]: 06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md
[e07]: 07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md#3-catalog-screen
[e10]: 10_VCD_E10_SMOOTH_NEXT_DEFECT_FREEDOM_20261116.md
[e13]: 11_VCD_E13_MIDPOINT_AUDIT_20261116.md
[ms]: ../manuscript/main.tex
