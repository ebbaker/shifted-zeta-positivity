# Internal review of the signed Mellin continuation

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the serving variant and
configured reasoning effort are not exposed and are not inferred.
Three separate agents supplied derivations or fresh internal proof checks
using the inherited configuration. This is not independent specialist
refereeing and is not a mathematical priority assessment.

Reviewed source: [Signed Mellin continuation](../notes/SIGNED_MELLIN_CONTINUATION_20261004.md).
Existing input: the fixed-probe theorem and sixth-derivative decay in the
[manuscript](../manuscript.tex), and the exact divisor/Vaughan localization
in the [arithmetic note](../notes/MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md).

## Verdict

The stated reductions, conditional endpoint theorem, low-frequency
obstruction, and separated-channel boundary theorem pass the internal
checks below. No fixed global exponent below one is established.
The remaining signed central estimate is explicitly unproved.

## Transform, complete caps, and mean square

- The identity F(s)=G(1/2-s) follows by v=-log t and has the correct
  plus-transform convention. On Re s=1/2 its multiplier is G(-it).
- The finite coefficients a_X(n) keep all integers AX<=n<=2BX, all
  divisors d>D, prime powers, and the terminal product caps. Their capped
  response equals R_X on the shell only; it is not identified with the
  uncapped formula outside the shell or with an unrestricted polynomial
  product. Noninteger X and strict divisor cutoffs are accounted for.
- Fourier inversion has factor 1/(2pi). Conjugate symmetry makes the
  truncated response real. The finite polynomial is entire and its
  inversion uses no unproved analytic continuation of an arithmetic sum.
- At prime powers d_2^2<=d_4 follows from
  (j+1)^2<=binomial(j+3,3). Counting quadruples proves the log^3 average,
  and the lower cap n>=AX gives sum |a_X(n)|^2/n=O(log^5 X).
- The Gaussian majorant of any interval of length H produces the exact
  kernel exp(-H^2 log^2(n/m)/4). The separation
  |log(n/m)|>=|n-m|/(2BX) and row sum O(1+X/H) prove mean square
  O((H+X)S_X), uniformly in interval location. No extra log X is needed.

## Frequency bounds and signed kernel

- Plancherel is applied on the entire log-coordinate axis. Shell energy
  then has weight x^2, bounded by 4X^2, not weight x. Loss of compact
  support after frequency truncation is harmless for this inequality.
- Summing the positive and negative dyadic tail blocks gives
  X^2(log X)^5(T^(-11)+XT^(-12)). At T=X^(1/12)log X the squared
  error is O(X^2/log^7 X), and the norm is O(X/log^(7/2) X).
  The more general logarithmic threshold b>5/12 is correct.
- The shell kernel J(t-v)=(2^(2+i(t-v))-1)/(2+i(t-v)) has the correct
  sign and normalization X^2/(4pi^2). It is Hermitian and positive
  semidefinite as a Gram form, not pointwise positive. All phases and
  arithmetic signs remain.
- For the additional shrinking low band, oddness makes G(-it) purely
  imaginary and odd. Its cosine integral vanishes; the sine bound gives
  g_tau(v)=O(|v|tau^3). Complete caps bound v uniformly, and Cauchy-Schwarz
  gives energy O(X^3S_X tau^6). Thus tau=X^(-1/5) gives
  O(X^(9/5)log^5 X), and the stated b>5/6 threshold also passes.
  This removes no fixed nonzero low frequency as X tends to infinity.
- The o(X) comparison preserves every energy exponent 2+delta, delta>=0,
  including the endpoint. The same projection argument works for generic
  bounded coefficient norms; it is smoothing, not an arithmetic saving.

## Signed Mertens representation and continuum

- Abel summation of log t L(x/t) over (D,infinity) gives the positive
  boundary M(D)log D L(x/D). M(D) is the correct prefix for strict d>D
  at both integral and nonintegral D. The upper boundary vanishes.
- The substitution y=x/t gives exactly the bracket
  L(y)/y-log(x/y)L'(y). L and L' vanish at y=1/B, so no cap term is
  missing.
- With q(v)=v w'(v), D^5q=vD^6w+5D^5w is a finite measure. This uses
  five derivatives of q, not an unjustified sixth derivative. Its zero
  integral and Poisson summation give L'=O(y^(-5)); endpoint atoms are
  included. Both weighted absolute kernel integrals converge.
- The Mertens envelope gives O(epsilon_D x log x) amplitude without a
  harmonic cofactor factor. Under an assumed power t^(1-eta), weighted
  integration gives x^(1-eta)log x for 0<eta<=1/2, with constants
  depending on eta and the assumed Mertens constant. This is conditional.
- The lattice Mellin identity initially holds by absolute Fubini for
  Re s>1 and extends to Re s>-5. The removable value at s=1 is F'(1)=c_w.
  Integration by parts gives the same moment for L'/y. Summing individual
  zero-mean integrals at s=1 would be invalid because their absolute
  harmonic sum diverges. This checks the nonzero Vaughan continuum.

## Conditional endpoint and low-frequency obstruction

- A global X^(3-kappa+o(1)) bound with 0<kappa<=1 gives each fixed
  slightly larger variance exponent. The manuscript's closed-strip
  equivalence, intersection of these strips, and its endpoint converse
  supply O(X^(3-kappa)). No uniform constants along the sequence are
  required. This establishes an admissible exponent, not optimality.
- The full-real-Y dyadic Möbius block has the true Mellin identity
  integral_0^infinity Delta(Y)Y^(-z-1)dY=(2^z-1)/(z zeta(1+z)).
  Its lower endpoint is safe because Delta vanishes below 1/2.
  The multiplier's zeros have real part zero; at a nontrivial zeta zero
  shifted by minus one its real part is negative. Thus it cannot cancel
  reciprocal-zeta poles, including poles from multiple zeros.
- The central block X=Y^2 gives eta=2omega/3 under the explicitly stated
  uniform hypothesis. The variance exponent 3-4omega/3 follows from the
  manuscript theorem. A predetermined grid of full dyadic block totals
  alone does not supply the real-Y quantifier; the note records this
  caveat rather than inferring the missing hypothesis.

## Individual-channel poles and checked sources

- The complete k=1 Möbius-log channel agrees with the retained one once
  AX>D. Its true Laplace transform contains zeta'/zeta^2, and no initial
  correction occurs because log 1=0 and log 2>1/4.
- At a multiplicity-m off-critical zero its pole has order m+1 and the
  fixed probe does not cancel it. An exact energy endpoint bounds the
  true transform by O(1/epsilon), excluding a boundary pole of order
  at least two. The full cofactor multiplier zeta reduces the pole to
  the prime response's simple pole. No global Möbius zero expansion or
  replacement of the finite moving cutoff by full zeta is asserted.
- [Lee-Leong v5](https://arxiv.org/pdf/2208.06141v5), revised 9 September
  2026, Theorem 1.1, was checked for the quoted Mertens scale and its
  large thresholds. Only an eventual subpower bound is used.
- [Higher uniformity II v2](https://arxiv.org/pdf/2411.05770v2), Lemma
  3.5(iv), (3.6) and (3.8), was checked for the low-frequency hypothesis
  and W^(-3/10) mean-square saving. The stronger strip comparison is a
  deduction here, not a result attributed to those authors.

## Limits of this review

No numerical exponent fit, quadrature certificate, finite-range extension,
LaTeX recompilation, or page-layout inspection was performed or needed for
these Markdown research notes. The manuscript and all earlier numerical
records are unchanged. The outer/inner frequency estimates and exact
kernel identities do not control the surviving signed central energy.
