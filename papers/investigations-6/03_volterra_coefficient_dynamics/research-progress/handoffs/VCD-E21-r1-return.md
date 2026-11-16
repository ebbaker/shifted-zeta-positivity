# VCD-E21 r1 — Complete error probability law return

16 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex assistance. Recorded dispatch **gpt-6.1-sol / ultra**.
Separate backend model and effort attestation unavailable.

**Complete, proved in-note.** [Note 20][note] executes the [frozen E21
request][request]. All seven pinned input SHA-256 hashes match. The
note SHA-256 is
`483ad9c88c8a07d833903e941dda5e9bc9520e94e8b64e99713c0c9b119002a9`.
The correction pass tightened the source pointers and control scope.
The requested equality, normalization, moment constants and complex
domain are confirmed without a mathematical correction.

At \(\lambda=0\) with the unchanged complete theta source, for every
\(N\ge1\) and \(z\in\mathbb C\),
\[
 F(z)-G_N(z)=(-1)^N\Big(\prod_{j=1}^N\beta_j\Big)
                    \frac{z^{2N}}{(2N)!}\,\mathbb E e^{izX_N}.
\]
Here \(X_N\) is the uniform simplex combination of the independently
drawn \(U\sim\nu_N=P_N^2\mu/h_N^*\) and the doubled Gauss nodes. Grouping
the node coordinates gives Dirichlet parameters \((1,2,\ldots,2)\).
The proof matches Hermite data directly at all multiplicities, obtains
the simplex integral by monomial division and beta integration,
and uses absolute exponential moments for integration and the entire
extension. \(X_N\) is even with mean zero. With \(M=2N+1\) and
\(S_p=\operatorname{tr} J_N^p\),
\[
 \begin{aligned}
 \mathbb E X_N^2&=\frac{2(m_2+S_2)}{M(M+1)},\\
 \mathbb E X_N^4&=\frac{24m_4+24m_2S_2+12S_2^2+12S_4}
                        {M(M+1)(M+2)(M+3)},\\
 m_2&=\beta_N+\beta_{N+1},\\
 m_4&=\beta_N\beta_{N-1}+(\beta_N+\beta_{N+1})^2+\beta_{N+1}\beta_{N+2}.
 \end{aligned}
\]
The independent \(N=1\) integral has the coefficient \(-\beta_1/2\)
at order two and moment factors \(1/6,1/15\) as predicted. The physical
[E15][e15] kernel comparison to \(\ell=0\) has the same left side and
the same first omitted walk. Its combined signed transport equals the
entire remainder above on this specialization.

The weighted-square controls share the exact-law hypotheses and the
E01 weighted cosh bound and envelope. They fail full canonical reflection
and complete equal square coefficients, which the proof leaves unused.
[Note 20 §5][note] records the control-by-control premises. The complex
phase allowance belongs to E22, and a margin that would exclude theta
zeros remains open.

The online de Boor PDF confirms §1 (16), p. 50, the polynomial knot
continuity statement in §2 Proposition 21, p. 51, the derivative
data for repeated knots in §7 Proposition 35 (36), p. 58, the
leading-coefficient definition in §7 Definition 37, p. 59, and the
ordinary-volume simplex formula §9 (52), p. 64, with the repeated-knot
formula discussed immediately below. The reference addendum can extend
the [passage record][ref] with these exact locations. The note derives
the required exponential case elementarily. [De Boor PDF][deboor]

[request]: VCD-E21-r1.md
[note]: ../../notes/20_VCD_E21_COMPLETE_ERROR_PROBABILITY_LAW_20261116.md
[e15]: ../../notes/13_VCD_E15_SHARED_MEMORY_EQUIVALENCE_20261116.md
[ref]: ../../references/04_QUADRATURE_ERROR_PHASE_PASSAGES_20261116.md
[deboor]: https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf
