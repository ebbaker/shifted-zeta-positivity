# Theta coefficients: primary-source comparison

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is an internal source comparison and algebraic check, not independent
specialist validation or formal verification.

**Finding:** the inspected cusp matrices, coefficient phases, conjugation
convention, support and coefficient bound match the declared primary
reference. This comparison supplies no blanket validation of the October 5
fixed-ray transformation or its uniformity.

## Exact sources and access

- **O5:** [October 5 `build/paper2.tex`, pinned commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex).
  SHA-256: `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
  Line references below use this file.
- **DR:** Alexander Dunn and Maksym Radziwiłł,
  [*Bias in cubic Gauss sums: Patterson's conjecture*, arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
  version dated 14 May 2024. Read directly on 12 October 2026:
  Sections 1.2, 5.1–5.3, and Appendix A, especially equations (1.7),
  (5.4)–(5.16) and Lemma 5.2/Corollary 5.1.
- **Patterson:** [*A cubic analogue of the theta series*, J. Reine Angew.
  Math. 296 (1977), 125–161](https://doi.org/10.1515/crll.1977.296.125).
  DR identifies Theorem 8.1, Table II (p. 129), and Table III (p. 151).
  The publisher fetch returned HTTP 405; the linked EuDML record returned
  HTTP 403. The original Patterson text was **not** independently read.
  The comparison below is with DR's primary-paper presentation, not a
  claimed direct check of Patterson's proof. No third-party PDF was
  added to the repository.

## Dictionary that was actually checked

Write `L(a)=[[1,0],[a,1]]` and
`e_check(z)=exp(2*pi*i*(z+conj(z)))`. DR's `d_j` are coefficients of
the **unconjugated** functions `F_j=theta(gamma_j w)`; O5's `d_sigma`
are coefficients of their conjugates. Thus the two `d` notations are
not interchangeable.

| O5 object | Matching DR object | Exact locators |
| --- | --- | --- |
| `gamma_0=I` | `gamma_1=I` | O5 `eq:theta-cusp-representatives`, 1762–1765; DR §5.1 before (5.9) |
| `gamma_+=L(omega)` | `gamma_10=L(omega)` | Same locations |
| `gamma_-=L(omega^2)` | `gamma_19=L(omega^2)` | Same locations |
| `t_0(ell)=tau(ell)` | `d_1(ell)` | O5 `eq:cusp-fourier-coefficients`, 3108–3112; DR Appendix A, row 1 |
| `t_+(ell)=omega*tau_2(omega*ell)*e_check(ell)` | `d_10(ell)` | Same O5 equation; DR Appendix A, row 10 |
| `t_-(ell)=omega^2*tau_1(omega^2*ell)*e_check(ell)` | `d_19(ell)` | Same O5 equation; DR Appendix A, row 19 |
| `d_sigma(ell)=conj(t_sigma(-ell))` | `conj(d_j(-ell))` | O5 `eq:conjugate-cusp-coefficients`, 3114–3119; DR (5.16) |

The constants also agree: `3^(5/2)/2 * v^(2/3)` occurs for the
identity representative; the other two listed representatives have no
constant term. See O5 `eq:cusp-coefficient-definition`, 1768–1776,
and DR (5.6), (5.15).

DR (5.7), (5.8), (5.13), (5.14) use primary `c,d`, with `c`
squarefree in the Eisenstein ring. No coprimality condition `(c,d)=1`
is imposed. The unit branches of `tau_1` and `tau_2` differ, including
their signs and ninth-root phases. They cannot be replaced by one
unqualified common coefficient sequence.

## Algebraic checks of the normalization and phases

These are calculations performed for this audit from the definitions,
rather than additional results imported from DR.

First, `lambda=1+2*omega=i*sqrt(3)` gives

\[
e_{\rm O5}(z)=\check e(z/\lambda).
\]

For the O5 sextic-symbol normalization, restrict to primary squarefree
`n` with `(n,6)=1`, as required in O5 lines 361–365 (and automatically
under `(n,S)=1`). Changing variables in the finite cubic Gauss sum gives

\[
\gamma_2^{\rm O5}(n)
=\left(\frac{\lambda}{n}\right)_3\widetilde g^{\rm DR}(n)
=\chi_n(\lambda)^2\widetilde g^{\rm DR}(n).
\]

Consequently, on O5's coefficient domain `(nb,6)=1`, the coefficient
at `ell=lambda^(-3)*n*b^3`, after conjugating theta, is

\[
3^{5/2}|b|\widetilde g^{\rm DR}(n)
=3^{5/2}|b|\overline{\chi_n(\lambda)^2}\gamma_2^{\rm O5}(n).
\]

This checks O5 `eq:intro-theta-coefficients`, lines 361–365, against
the `m=-3` case; using identical names for the two additive characters
without this change of variables would lose a cubic phase.
The ordinary cubic Gauss sums used in the dual coefficient bound below
also allow the prime above 2. That wider cubic domain does not extend
the O5 sextic-symbol notation to the norm-4 prime.

Conjugating the two nonidentity rows explicitly gives

\[
d_+(\ell)=\omega^2\overline{\tau_2(-\omega\ell)}\check e(-\ell),
\qquad
d_-(\ell)=\omega\overline{\tau_1(-\omega^2\ell)}\check e(-\ell).
\]

For a small exact sign check, set the primary squarefree and cube
factors equal to 1. Since `lambda^4=9`, direct substitution gives

\[
t_-(1/9)=9,\quad t_+(-1/9)=9,\quad
t_-(-1/9)=t_+(1/9)=0;
\]

therefore `d_-(-1/9)=9` and `d_+(1/9)=9`. This checks both the
frequency reversal and the noninterchangeability of the two cusp
sequences. It does not test any asymptotic estimate.

The translation/inversion labels in O5 lines 3097–3101 can also be
checked without assuming that different representatives are aliases.
Put `T(a)=[[1,a],[0,1]]` and `E=[[0,-1],[1,0]]`. Exact multiplication
gives

\[
T(\omega)E\gamma_-^{-1}
=\begin{pmatrix}-1&-1\\1&0\end{pmatrix},\qquad
T(-\omega)E\gamma_+^{-1}=E.
\]

Both right-hand matrices are in `SL_2(Z)`. Under the imported
automorphy law whose multiplier is 1 on that subgroup, these equalities
justify precisely the stated `+omega -> -` and `-omega -> +` choices.
They do not identify all 27 cusp representatives with one another.

## Support and the constant 27

For the coefficient bound, use the primitive finite cubic Gauss-sum
identity `abs(g(a,n))=sqrt(N(n))=abs(n)` when `n` is squarefree and
`(a,n)=1`. This permits the norm-4 prime as a cubic-character prime;
no squarefreeness of the rational integer `N(n)` is required.

After canceling `abs(n)` against the denominator in the coefficient
formula, the two infinity-cusp branches have magnitudes

\[
3^{k/2+2}|b|\quad(m=3k-4,\ k\ge1),\qquad
3^{k/2+5/2}|b|\quad(m=3k-3,\ k\ge0).
\]

Dividing these by `3^(m/6)*abs(b)` gives respectively `3^(8/3)`
and `27`. The two other cusps are supported at `m=-4`; their
magnitude is at most `9*abs(b)`, giving the ratio `3^(8/3)<27`.
All other coefficients are zero. Unit rotations, the additive phases
and conjugation preserve magnitudes. Hence

\[
|d_\sigma(u\lambda^mnb^3)|\le27\,3^{m/6}|b|,
\qquad m\ge-4,
\]

with `n,b` primary and only `n` squarefree. This verifies O5
`eq:theta-support`, `eq:theta-coefficient-bound`, lines 1859–1868,
and the arithmetic comparison at lines 3120–3142. No restriction
`(n,b)=1` is introduced by this derivation.

## Hypothesis boundary and remaining obligation

The imported automorphy is on `Gamma_2`, with the cubic multiplier
defined in DR (5.4); it is trivial on `SL_2(Z)`. The displayed
coefficient and automorphy inputs do not assume GRH. DR's later
GRH-dependent results are not inputs to this comparison.

DR Lemma 5.2 and Corollary 5.1 require a primary modulus `r` and
Fourier support on classes coprime to `r`. O5 explicitly allows
nonunit fixed frequencies, so those statements alone cannot justify
its extension (O5 lines 3033–3036). The reduced-denominator
construction, local Fourier branches, multiplier calculation and
uniformity as moving primes vary must still be checked in O5 itself.
The angular Mellin transform and its entire continuation are likewise
separate obligations. Agreement of the coefficient dictionary does
not settle those steps or establish the family power saving.
