# Correlated current support and manuscript synthesis

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed in this session and are not inferred. Derivations and
parallel cross-audits are internal LLM checks, not independent mathematical
validation.

The working manuscript
[Microlocal observations, coherent currents, and finite zero atlases](../microlocal_coherent_currents_and_zero_atlases.tex)
consolidates microlocal Notes 1–5 after reading the
[prime-torus manuscript](../../09_prime_phase_torus/prime_phase_torus_signed_reductions.tex)
and [Heat Note 22](../../notes/22_SIGNED_PAIR_TRANSFORMS_AND_STATIONARY_REFLECTION_20261010.md).
It preserves the explicit imported complete-disk approximation interface,
all physical derivatives, complete coherent interference, and the finite
scope of the four certified windows. It also derives the following support
refinement. None of the existing certificates uses that refinement.

## Sharp current support on the correlated first-jet body

At a real center let the complete physical sum and its spatial derivative be
\(S=u+iv_0\), \(S'=u'+iv_1\), and let
\(\mathcal J=-\Im(S'\overline S)=u'v_0-uv_1\).
Under the full holomorphic error disk with radius \(1/L\) and positive
majorant \(\eta\), a genuine joint zero requires the Schwarz–Pick condition

\[
s^2+|r|\le1,\qquad s=2u/\eta,\quad r=2u'/(L\eta).
\]

This follows by applying Schwarz–Pick to
\((Q-F)(x+\zeta/L)/\eta\), which has modulus at most one.
At a joint zero its value and derivative are \(-s,-r\).

For the fixed actual imaginary quadratures, put
\(A=L|v_0|\), \(B=|v_1|\). Then

\[
\begin{split}
\max_{s^2+|r|\le1}|Lv_0r-v_1s|
&=\max_{0\le y\le1}\{A(1-y^2)+By\}\\
&=h(A,B),
\end{split}
\]

where

\[
h(A,B)=
\begin{cases}
A+B^2/(4A),&A>0,\ B\le2A,\\
B,&A=0\text{ or }B\ge2A.
\end{cases}
\]

For fixed \(y=|s|\), take \(|r|=1-y^2\) and choose signs to align
the two terms. The concave scalar polynomial has its maximum at
\(y=B/(2A)\) if that lies in \([0,1]\), otherwise at \(y=1\).
The case \(A=0\) is direct. Thus every genuine joint zero requires

\[
|\mathcal J|\le\frac\eta2 h(L|\Im S|,|\Im S'|).
\]

This is no larger than the earlier rectangular support payment
\(\eta(L|\Im S|+|\Im S'|)/2\). It requires no division by \(S\).
Its sharpness concerns support of the stated necessary body with those
actual imaginary quadratures fixed. It does not assert that maximizing
real coordinates are attainable by genuine arithmetic states. The fact
that all four quadratures come from the same sum does not invalidate an
upper bound on a larger necessary body.

An interval implementation can use monotonicity in \(A,B\) and outward
upper bounds, with a safely evaluated branch or the rectangular bound
when a branch cannot be decided. No new numerical current certificate is
claimed here.

## Carrier value and carrier motion

A fixed common phase rotation leaves \(\mathcal J\) invariant. For a
height-dependent rotation \(\widetilde S=e^{i\chi(x)}S\), however,

\[
\widetilde{\mathcal J}=\mathcal J-\chi'(x)|S|^2.
\]

Therefore only the phase value cancels from the pair product. The
physical carrier motion remains in \(\Omega\) and \(\lambda_N\) in
the block/current formulas. The manuscript prints this distinction.

## Finite evidence and limitations

Fresh replays of the scout, complete small rectangle, complete M=22066
atlas, and the three newer cutoff atlases pass and are byte-identical to
their retained records. The directed-multiplication override in Note 3
is used as the arithmetic foundation for the adverse block too. A
supplementary corrected-interval division of its complete-certificate
block current by the rebuilt genuine \(w_M^2\) verifies the displayed
normalized negative block bound. The manuscript review records the details.

The four full-window zero counts remain 13, 12, 12 and 13, conditional
on the explicit imported full-disk interface. Derivative acceptance alone
already excludes joint zeros in their surviving strips; the current and
Schur predicates additionally retain their respective signed information.
The new support formula is an analytical consequence and is not an
additional observed exclusion. No uniform shrinking-time sign, cutoff-cell
bridge, opposite threshold inequality or RH conclusion is supplied.
