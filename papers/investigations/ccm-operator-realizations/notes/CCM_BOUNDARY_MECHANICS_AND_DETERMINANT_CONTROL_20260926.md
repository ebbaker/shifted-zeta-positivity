# CCM boundary mechanics and determinant control

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact model variant and reasoning-effort setting are not exposed in this session.

Status: continued research with proofs of finite algebraic deductions, a conditional analytic criterion, and exploratory numerical checks. No priority claim is made for the elementary transformations. This note does not establish the missing CCM hypotheses or RH.

Predecessor: [metric transport and a finite chiral realization](CCM_SPECTRAL_OPERATORS_AND_CHIRAL_REALIZATION_20260926.md).

## 1. Result of this continuation

The finite modified CCM spectrum can be realized as the normal-mode frequencies of a mechanical system whose mass and stiffness are
\[
\boxed{\mathsf M=J^\dagger T_+J,\qquad \mathsf K=T_-},
\qquad T_\pm=W_\pm-\varepsilon I.
\]
The map \(J\) is a fixed inverse derivative with a zero endpoint condition. It depends on the circle and Fourier cutoff, not on the Weil ground vector. Once the least eigenvalue \(\varepsilon\) is known, this pair can be constructed without evaluating that vector.

This yields a positive pair under the finite CCM simple-even assumptions, an exact entire-function determinant formula, and a concrete quantity
\[
\tau_{\lambda,N}
=\operatorname{tr}(\mathsf K^{-1}\mathsf M)
 +\sum_{n>N}\left(\frac{L}{2\pi n}\right)^2
\]
that controls the growth of the normalized spectral function on every complex compact set.

The numerical checks show why this quantity matters: very accurate agreement with the first zeta zero can coexist with a visible error in \(\tau\). The calculation below also shows that the unmodified Fourier tail can leave a Gaussian factor in a joint limit.

## 2. Input, basis, and assumptions

Write \(L=2\log\lambda\), and use the Fourier basis
\[
V_n(x)=L^{-1/2}\exp(2\pi i n(x+L/2)/L),
\quad -L/2\le x\le L/2,
\quad |n|\le N.
\]
The finite Weil matrix \(W\) commutes with reflection. Its parity blocks are \(W_+\) on a space of dimension \(N+1\), and \(W_-\) on a space of dimension \(N\). Assume the least eigenvalue \(\varepsilon\) of the full matrix is simple and has even eigenvector \(g\). Then
\[
T_+=W_+-\varepsilon I\ge0,\quad\ker T_+=\mathbb Cg,
\qquad T_-=W_--\varepsilon I>0.
\]
The boundary functional \(\ell\) does not vanish on \(g\); normalize \(\ell(g)=1\). The CCM operator is \(A=D_0-(D_0g)\ell\), with \(A^\dagger T=TA\). These are the input facts from [CCM, Section 5](https://arxiv.org/html/2511.22755v1) and the matrix mechanism in [Connes–van Suijlekom, Section 5](https://arxiv.org/html/2511.23257v1).

Take the orthonormal parity basis
\[
c_0=V_0,\qquad c_n=(V_n+V_{-n})/\sqrt2,
\qquad s_n=(V_n-V_{-n})/\sqrt2.
\]
The odd basis functions are imaginary-valued; the matrix coordinates below are real. Put \(d_n=2\pi n/L\). In this basis,
\[
D_0=\begin{pmatrix}0&R^\dagger\\R&0\end{pmatrix},
\quad R=(0\ \operatorname{diag}(d_1,\ldots,d_N)),
\quad
\ell_+(a)=\frac{a_0+\sqrt2\sum_{n=1}^N a_n}{\sqrt L}.
\]
The functional vanishes on the odd space. None of the following finite deductions assert the simple-even condition uniformly in the cutoffs.

## 3. A boundary gauge with an explicit integration map

Every even quotient class modulo \(g\) has a unique representative in
\(F=\ker\ell_+\), namely \(f-g\ell_+(f)\). Moreover
\(R:F\to E_-\) is an isomorphism: the only even vector annihilated by \(R\) is the constant, whose endpoint value is nonzero.

The inverse \(J:E_-\to F\) has the explicit coefficients
\[
(Jy)_0=-\sqrt2\sum_{n=1}^N\frac{y_n}{d_n},
\qquad (Jy)_n=\frac{y_n}{d_n}\quad(n\ge1).
\]
Thus \(RJ=I\) and \(\ell_+J=0\). On functions this is inverse differentiation with an endpoint condition:
\[
(Jh)(x)=-i\int_x^{L/2}h(t)\,dt.
\]
For odd \(h\), the result is even and vanishes at both endpoints.

This part already has a geometric description independent of the arithmetic metric. The Dirichlet Poincare inequality and the explicit columns of \(J\) give
\[
\|J\|\le\frac{L}{\pi},\qquad
\operatorname{tr}(J^\dagger J)=3\sum_{n=1}^N d_n^{-2}
\longrightarrow\frac{L^2}{8}\quad(N\to\infty).
\]
The finite norm estimate follows by applying \(\|f\|_2\le(L/\pi)\|f'\|_2\) to \(f=Jh\). These bounds alone do not control the arithmetic metric.

## 4. Exact mechanical realization

Define
\[
\mathsf M=J^\dagger T_+J,\qquad\mathsf K=T_-.
\]
Both are positive definite. Positivity of \(\mathsf K\) follows from simplicity of the full ground state. If \(y^\dagger\mathsf M y=0\), then \(Jy\in\mathbb Cg\); but \(\ell Jy=0\) and \(\ell g=1\), so \(Jy=0\), hence \(y=0\).

Represent the even quotient by \(Jy\), and retain the odd vector \(v\). The induced operator has the form
\[
\mathscr D=
\begin{pmatrix}0&Q\\I&0\end{pmatrix},
\qquad Q=R(I-g\ell_+)R^\dagger.
\]
Indeed, \(A(Jy)=y\) in the odd sector. For an odd input, project \(R^\dagger v\) to the boundary gauge and then apply \(R\) to obtain its even coordinates.

The quotient metric is \(\operatorname{diag}(\mathsf M,\mathsf K)\). Weighted self-adjointness now states
\[
\mathsf M Q=\mathsf K,
\qquad Q=\mathsf M^{-1}\mathsf K.
\]
Consequently the positive eigenvalues \(\omega_j\) of the quotient satisfy
\[
\boxed{\mathsf K q_j=\omega_j^2\mathsf M q_j}.
\]
They are precisely the normal-mode frequencies of
\[
\mathsf M\ddot q+\mathsf Kq=0,
\qquad
\mathcal L(q,\dot q)
=\tfrac12\dot q^t\mathsf M\dot q-\tfrac12q^t\mathsf Kq.
\]
The corresponding mechanical energy is positive. Its matrices can be dense; a local differential or nearest-neighbor physical model has not been obtained.

Flattening the metric yields another explicit version of the founding note's chiral matrix:
\[
\mathscr B=
\begin{pmatrix}
0&\mathsf M^{-1/2}\mathsf K^{1/2}\\
\mathsf K^{1/2}\mathsf M^{-1/2}&0
\end{pmatrix}.
\]
The coupling is invertible. Thus, under the full finite CCM assumptions, this quotient has no zero mode. The generic possibility of zero singular values mentioned in the founding note is excluded here by the boundary functional and derivative structure.

A second equivalent pencil avoids integration in its numerator:
\[
S=RT_+R^\dagger
=\mathsf K\mathsf M^{-1}\mathsf K>0,
\qquad Sy=\omega^2\mathsf K y.
\]
To verify the identity, use the odd-even block of \(TA=A^\dagger T\):
\(\mathsf K R(I-g\ell_+)=RT_+\), and multiply by \(R^\dagger\).

Every construction here is unchanged by \(W\mapsto W+cI\), \(\varepsilon\mapsto\varepsilon+c\). Therefore the mechanical realization still does not determine the sign of the original ground energy.

## 5. Determinant formula and the necessary free tail

The finite quotient determinant is
\[
\det(\mathscr D-zI)
=\frac{\det(z^2\mathsf M-\mathsf K)}{\det\mathsf M}
=\prod_{j=1}^N(z^2-\omega_j^2).
\]
The unreduced \((2N+1)\)-dimensional matrix has the additional factor \(-z\) from the inserted ground vector.

Combining this identity with CCM's regularized determinant for the free circle gives the entire function normalized at the origin:
\[
\boxed{
F_{\lambda,N}(z)
=\frac{\widehat g(z)}{\widehat g(0)}
=\frac{\sin(Lz/2)}{Lz/2}
\frac{\det(I-z^2\mathsf K^{-1}\mathsf M)}
 {\prod_{n=1}^N(1-z^2/d_n^2)}.
}
\]
The apparent poles at free frequencies are removable. The absence of a quotient zero mode, together with the free tail's nonzero value at zero, ensures \(\widehat g(0)\ne0\). Equivalently,
\[
F_{\lambda,N}(z)
=\prod_{j=1}^N(1-z^2/\omega_j^2)
 \prod_{n>N}(1-z^2/d_n^2).
\]
The second product cannot be dropped when comparing determinants or Taylor coefficients. It is the spectrum outside the modified Fourier sector, and can enter even the first few full spectral values when \(N/L\) is small.

The mechanical model realizes the modified operator spectrum. A full spectral-triple realization would additionally have to specify the algebra representation; the boundary quotient does not automatically inherit multiplication by every circle function.

## 6. Inverse spectral moments as a convergence criterion

Define
\[
a_k(\lambda,N)
=\operatorname{tr}\big((\mathsf K^{-1}\mathsf M)^k\big)
 +\sum_{n>N}d_n^{-2k}\quad(k\ge1).
\]
The matrix \(\mathsf K^{-1}\mathsf M\) is similar to a positive Hermitian matrix. Thus these quantities are sums of positive reciprocal powers of squared frequencies. In a neighborhood of zero,
\[
\log F_{\lambda,N}(z)
=-\sum_{k\ge1}\frac{a_k(\lambda,N)}{k}z^{2k}.
\]
In particular, \(\tau=a_1=-F''(0)/2\).

For every complex \(z\), the product representation proves
\[
\boxed{|F_{\lambda,N}(z)|\le \exp(\tau_{\lambda,N}|z|^2)}.
\]
Apply \(|1-z^2/t^2|\le\exp(|z|^2/t^2)\) to every factor; the reciprocal-square series converges.

**Conditional criterion.** Along a cutoff sequence satisfying the finite CCM assumptions, suppose \(\sup\tau_{\lambda,N}<\infty\). If the normalized functions can be identified with \(\Xi(z)/\Xi(0)\) in the limit on a real interval, then they converge locally uniformly on the whole complex plane to that function. Here pointwise convergence at every point of an interval suffices.

Proof: the displayed bound gives a normal family. Every convergent subsequence has an entire limit agreeing with \(\Xi/\Xi(0)\) on the interval; the identity theorem identifies that limit. Uniqueness of all subsequential limits gives convergence of the whole sequence. Hurwitz applied in each open half-plane then excludes nonreal zeros of \(\Xi\), since each approximant is zero-free there and the entire limit is nonzero.

An equivalent sufficient route is convergence, for every \(k\ge1\), to the local target coefficients
\[
a_k^\Xi=-k\,[z^{2k}]\log(\Xi(z)/\Xi(0)).
\]
Convergence for \(k=1\) supplies the uniform bound. If \(\tau\le C\), positivity gives \(a_k\le C^k\); the logarithmic series therefore converge on a common small disk, after which the same normal-family argument applies.

This is a repackaging of the missing analytic control, not a verification of it. Its benefit is that the quantities to estimate are traces of a concrete mass/stiffness pair rather than pointwise errors in an explicitly normalized ground vector. Matching any finite number of moments does not establish the criterion.

For fixed \(L\), a basic sufficient estimate can be written down. If, uniformly in \(N\),
\[
\mathsf K\succeq\kappa I,\qquad
T_+\preceq C\,\operatorname{diag}(1,\log3,\log4,\ldots,\log(N+2)),
\]
then
\[
\operatorname{tr}(\mathsf K^{-1}\mathsf M)
\le\frac{C}{\kappa}\left(\frac{L}{2\pi}\right)^2
 \sum_{n=1}^N\frac{2+\log(n+2)}{n^2}.
\]
The series converges. This conditional estimate distinguishes Fourier-cutoff control at fixed support from the harder problem of controlling the constants as the support grows. These uniform assumptions have not been established in this note.

## 7. A Gaussian can survive the joint cutoff limit

Let
\[
U_{L,N}(z)=\prod_{n>N}\left(1-\frac{L^2z^2}{4\pi^2n^2}\right).
\]
If \(N\to\infty\) and \(L^2/N\to c\in[0,\infty)\), then
\[
\boxed{U_{L,N}(z)\longrightarrow
\exp\left(-\frac{c z^2}{4\pi^2}\right)}
\]
locally uniformly on the complex plane.

For a fixed compact set, the largest \(|L^2z^2/(4\pi^2n^2)|\) tends to zero. The first term of the logarithmic expansion converges using \(\sum_{n>N}n^{-2}\sim N^{-1}\). All higher terms tend to zero, bounded by a constant times \(L^4\sum_{n>N}n^{-4}=O(L^4/N^3)\).

Consequences:

- \(L^2/N\to0\) makes the known free tail disappear.
- \(N\sim\alpha L^2\) leaves \(\exp(-z^2/(4\pi^2\alpha))\).
- Merely moving the first free frequency to infinity, \(N/L\to\infty\), is not sufficient to make its entire product tend to one.

A known nonvanishing Gaussian factor does not change zero locations, but it changes normalized Taylor coefficients and the asserted determinant limit. It must be tracked. This observation does not contradict CCM's staged limit, which first sends \(N\to\infty\) at fixed \(L\).

## 8. Numerical reconstruction and results

The [program](../numerics/check_mass_stiffness.py) builds the Weil matrix from its defining distribution using multiprecision quadrature. It retains the archimedean tail term, checks selected off-diagonal entries by direct correlation integrals, and constructs both the original rank-one modification and the new mass/stiffness pair. Zeta zeros are used only for the diagnostic errors below.

The primary run used 120 decimal digits. The parameters are \(X=\lambda^2\), \(L=\log X\), and \(N\). The table's frequency is from the finite mechanical sector.

| \(X\) | \(N\) | Least Weil eigenvalue, approximately | Absolute error of first finite frequency against first zeta zero | \(\tau\), including free tail |
|---:|---:|---:|---:|---:|
| 2 | 4 | \(1.73553\times10^{-3}\) | \(2.62657\times10^{-1}\) | 0.0109384554462371 |
| 5 | 8 | \(4.57014\times10^{-15}\) | \(1.64885\times10^{-11}\) | 0.0195364238217430 |
| 13 | 8 | \(7.67439\times10^{-23}\) | \(4.17618\times10^{-17}\) | 0.0310630231986285 |
| 13 | 16 | \(8.56863\times10^{-35}\) | \(1.99036\times10^{-30}\) | 0.0244874970388259 |
| 13 | 24 | \(3.07456\times10^{-43}\) | \(3.45322\times10^{-39}\) | 0.0227234068191501 |

Direct differentiation of the completed zeta function at the origin gives
\[
a_1^\Xi=0.0231049931154189707889338104303390\ldots.
\]
For \(X=13,N=24\), the first frequency is accurate to about 38 decimal places, while \(\tau\) has a relative discrepancy of about 1.65 percent. At \(X=13,N=8\), the first unmodified Fourier frequency is approximately 22.05; it precedes the third finite-block frequency. This explains why the finite frequencies must not be read as the entire sorted spectrum.

The maximum scaled algebraic reconstruction residual over the primary run was below \(3.5\times10^{-79}\). Checked identities include weighted self-adjointness, \(RJ=I\), \(\ell J=0\), \(RT_+R^\dagger=\mathsf K\mathsf M^{-1}\mathsf K\), the finite quotient characteristic determinant, and the normalized Fourier/determinant formula at three complex points.

A preliminary 60-digit run was insufficient for the larger case \(X=13,N=16\): a characteristic-determinant residual was about \(1.9\times10^{-27}\), exceeding the chosen \(10^{-30}\) check threshold. Increasing precision resolved that check. These calculations are exploratory and are not interval-certified eigenvalue or zero enclosures.

The largest case was recomputed at 160 digits. All 21 saved observables agree with the primary run at the 45 significant digits retained in the records; the largest reconstruction residual in that rerun was below \(3.5\times10^{-119}\). This is a precision-stability check, not an interval certificate.

The small records are [the primary run](../numerics/records/mass_stiffness_20260926.json), [the 160-digit check](../numerics/records/precision_check_160_20260926.json), and [the precision comparison](../numerics/records/precision_comparison_20260926.json). They include the first three inverse moments and all residuals; full matrices are regenerated rather than stored.

## 9. What remains to investigate

The finite realization is now explicit enough to test proposed geometric systems against two forms, with a fixed integration map connecting the parity sectors. A candidate should explain both \(J^\dagger T_+J\) and \(T_-\), and supply quantitative control as \(L\) grows.

The next focused problem is to derive a trace comparison for
\(\operatorname{tr}(T_-^{-1}J^\dagger T_+J)\) with support dependence that could remain bounded along an appropriate cutoff sequence. An additional arithmetic identity is needed to identify the local spectral function or all its inverse moments with \(\Xi\).

For a continuum formulation, operator domains, endpoint traces, and positivity/coercivity of the limiting forms must be proved. The finite boundary gauge supplies a candidate construction; it does not justify those passages to the limit. The original simple-even ground-state condition remains an input throughout.
