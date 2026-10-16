# Internal critical review of the phase boundary trace

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This is a separate same-model
mathematical reading and derivation, not independent human or specialist
refereeing. No numerical experiment or numerical certificate is part of
this review.

## Verdict and scope

The [phase boundary trace note](../notes/SONIN_PHASE_BOUNDARY_TRACE_20260929.md)
passes this internal check. Its projection formula, independently represented
boundary correction, archimedean calibration, local frequency continuation,
and Abel error estimate are justified on the stated domains. No unresolved
mathematical correction was found in those claims. The arithmetic critical
limit remains open, and the note states that limitation correctly.

The review independently checked the Fourier diagonal sign, the causal
cutoff gap, the block cancellation leading to the short boundary formula,
the gapless positive approximants, and the spectral measure in the next
error lemma. It also checked the pole-crossing obstruction and the
normalization of the local critical-line concentration. This is not an
exhaustive literature or novelty review.

## Actual projection and phase trace

For sigma greater than 1, the causal transport and its inverse preserve the
positive logarithmic half-line. The negative-half-line compression is an
invertible quotient operator, with inverse given by compressing the inverse
transport. Consequently the factorization

\[
T_\sigma=D_-T_\infty D_+^{-1}
\]

implies the stated positive lower bound for
\(T_\sigma T_\sigma^*=I-C_\sigma^2\). This does not require
compactness of the deformed cutoff. The kernel projection therefore has
the inverse factor in equation (9), and agrees with the transported Sonin
projection carrying its inverse compressed metric.

With Fourier measure \(dt/(2\pi)\), the positive-half-line projection
has kernel \(\pi\delta(t-s)-i\operatorname{pv}(t-s)^{-1}\).
The phase-difference kernel consequently has diagonal
\(i\overline v v'=-\phi'\). Thus the *negative* smoothed trace of
\(\mathcal Q_\sigma\) equals the integral of \(\phi'_\sigma\).
The derivative is

\[
\gamma(t)+2\Re(\zeta'/\zeta)(\sigma+it)
=\gamma(t)-2\sum_{p,m\ge1}(\log p)p^{-m\sigma}
  \cos(mt\log p),
\]

which gives exactly the stated prime weights and sign. The absolute Euler
coefficient sum justifies the interchange at sigma greater than 1, and
compact source support leaves every active prime power in the finite sum.

The smoothing proof is adequate: Schwartz Hankel kernels have trace-class
off-diagonal blocks, and the displayed commutator identity makes the
smoothed phase difference trace class. Compact spectral localization gives
a smooth nuclear kernel whose trace is its diagonal integral. Removing
the localizers uses trace-norm convergence of already trace-class
operators. No trace is assigned to either unsmoothed projection separately.

## Independent correction and short boundary formula

The block identity

\[
\mathcal Q=
\begin{pmatrix}-L&T^*C\\ CT&C^2\end{pmatrix},\qquad
\Pi=L-T^*C^2(I-C^2)^{-1}T
\]

fixes all four boundary contributions and their signs. The positive return
term is bounded above by \(L\). Smoothed cutoff blocks are trace class;
the return sandwich is therefore trace class by positive domination.
Equation (19) is an independently specified operator correction, rather
than a definition by arithmetic subtraction.

The simplification to equation (2) is also valid. Real structure makes
the projection's frequency density even, so replacing the source multiplier
by its even part does not alter the scalar form. That multiplier commutes
with the involution. In the two-cutoff coordinates the commutation equation
is

\[
sD_0-As=CB+BC.
\]

The crossing block \(B\) is trace class. The diagonal products with
\(C^2\) are trace class by the smoothed block identities. Multiplication
by \(C^2s^{-1}\), bounded-factor cyclicity, and commutation of \(C\)
with \(s\) give the diagonal trace
\(2\operatorname{Tr}(C^3s^{-1}B)\). Adding the crossing traces gives
\(2\Re\operatorname{Tr}(Cs^{-1}B)\), as claimed. This cancellation
does not discard the small-cutoff diagonal or the positive return term.

The source crossing operator has kernel
\(1_{x>0>y}\kappa_{F,e}(x-y)\). For support length \(L\), its
nonzero region satisfies \(-L<y<0<x<L\) and \(x-y<L\).
The inverse cutoff factor is bounded at each fixed sigma greater than 1;
no uniform critical bound follows from that fact.

The return-series bound in (21b) is correct. The omitted bounded factor is
\(C^{2N+3}(I-C^2)^{-1}T\). Multiplication by its adjoint reduces its
squared norm to the supremum of
\(\lambda^{2N+3}/(1-\lambda)\) on the spectrum of \(C^2\).
This gives \(c^{2N+3}/\sqrt{1-c^2}\), before the factor
\(2\|X_F\|_1\). No deformed cutoff eigenbasis is needed.

The archimedean limit of the boundary expression follows directly from
operator-norm convergence and the fixed trace-class crossing operator.
Expansion in the real archimedean cutoff eigenbasis gives precisely the
coefficient \(\lambda_n/\sqrt{1-\lambda_n^2}\). The crossing overlap
has the same orientation as the audited \(U_{-t}\) epsilon kernel.
Thus the limit is \(+E_\infty\), with no added pole or contact term.

## Gapless continuation and the next error lemma

On any fixed vertical line, numerator and denominator of the phase ratio
have equal zero or pole orders at real frequencies. Their ratio has a
smooth real-parameter extension locally. Hence a compact smooth frequency
multiplier \(b\) satisfies \(bv_\sigma\in C_c^\infty\), and the
same commutator proof applies without a global derivative bound.
The local finiteness of \(\nu_\sigma\) follows from
\(0\le\Pi_\sigma\le L_\sigma\) and the finite smoothed trace of
\(L_\sigma\). Absolute continuity at each fixed sigma follows from
the orthonormal-basis and Tonelli representation; singular limiting measures
remain possible.
The stronger local statement \(b(D)\Pi_\sigma\in\mathfrak S_1\)
also follows immediately from \(b(D)L_\sigma\in\mathfrak S_1\)
and \(L_\sigma\Pi_\sigma=\Pi_\sigma\).

The positive frequency-cutoff family (26a) is finite for every indicated
parameter, since \(\widehat F b_N\) is compact smooth. Its monotone
limit in \(N\) is the full source trace, possibly infinite. The note
correctly distinguishes this infinite-rank spectral cutoff from an
ambient finite-rank projection: strong projection collapse does not force
the fixed-window trace to vanish.

The Abel approximants in (23) are positive contractions decreasing strongly
to the actual intersection projection. At a spectral value \(\alpha\)
of \(T^*T\), their multiplier is
\((1-r)(1-\alpha)/(1-r+r\alpha)\). It is 1 on the kernel and
converges to zero elsewhere. The corresponding positive return traces
converge monotonically under the smoothed \(L\) bound. The note correctly
does not substitute the squared Hilbert--Schmidt norm of the nonidempotent
Abel approximant for its positive sandwich trace.

For the polar factor in Section 7, the full return operator is
\(V^*C^2V\). Its smoothed spectral measure is finite, and its mass at
1 is zero because the final space of \(V\) excludes
\(\ker(I-C^2)\). The difference of the Abel approximant and the
projection has multiplier

\[
V^*\frac{(1-r)C^2}{1-rC^2}V.
\]

Consequently equation (30) has exactly the stated integrand and cutoff-tail
bound. This proves fixed-sigma error convergence. It supplies no uniform
estimate as sigma approaches the critical line. Retaining the unsimplified
boundary blocks in the gapless case also avoids silently dropping a
possible negative-half-line intersection at \(C^2=1\).

## Concentration and unresolved arithmetic obligations

A critical-line zero of multiplicity \(m\) contributes
\(2m\epsilon/(\epsilon^2+(t-\gamma)^2)\), with
\(\epsilon=\sigma-1/2>0\), to the phase derivative. Its normalized
distributional limit is \(m\delta_\gamma\). Finite-window analytic
factorization and the functional equation remove the remaining smooth
background. This proves the claimed local phase-bulk limit, not a limit
for the positive projection measure. Differentiating the endpoint phase
itself would give zero and would lose this concentration.

The zeta pole contributes
\(-2(\sigma-1)/((\sigma-1)^2+t^2)\); its paired trace jumps by
\(+2a(0)\) from the right side of sigma equal to 1 to the left side.
Pole-neutral compact sources need not have \(a(0)=0\). Thus the
finite arithmetic deformation cannot be identified with the phase bulk
below 1 by continuing the Euler-series calculation unchanged. Off-line
zero crossings require their own residue terms.

The remaining obligations are therefore substantive and separate:
control the full local boundary contribution, control source-weighted
frequency tails, and identify the continued trace with the complete
arithmetic form including crossing residues. The proposed cutoff spectral
tail estimate is a concrete next step, not a proof of those obligations.
Strong convergence of the projections or cutoffs alone proves none of
the required trace convergence statements.
