# Preliminary investigation: the useful range and singleton detector gate

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal source audit and algebraic deductions, not independent specialist
review. No new global exponent is proved.

## Outcome

Keep this as a bounded scout. The current retained polynomial can be put
into the coefficient class of the new large-value theorem, but its bound
is weaker than merely counting all available sample points at our current
frequency cap. The issue is a lack of a **useful** range, not a formal
prohibition on applying Theorem 1.1. A second route through zero detection
has two unresolved gates: eliminating the detector's exceptional zero
class and amplifying a single zero into sufficiently many large values.

The inherited [signed Mellin reduction](../../SIGNED_MELLIN_CONTINUATION_20261004.md)
retains

\[
X^{-1/5}<|t|\le T_X=X^{1/12}\log X,
\quad \mathcal A_X(s)=\sum_{AX\le n\le2BX}a_X(n)n^{-s},
\quad a_X(n)=-\sum_{d\mid n,\ d>X^{9/10}}\mu(d)\log d,
\]

and the full two-frequency kernel
\(J(t-v)=(2^{2+i(t-v)}-1)/(2+i(t-v))\).
Its Gram form is positive semidefinite but not entrywise positive.
Controlling level sets of |A_X| would be a sufficient input only after
an explicit integration bound; it does not recover the signed Gram
cancellation automatically.

## Primary theorem and exact normalization

[Guth–Maynard v2, Theorem 1.1](https://arxiv.org/pdf/2405.20552v2)
states, for 1-bounded complex coefficients on n~N and 1-separated t_r in
[0,T] with \(|\sum b_nn^{it_r}|\ge V\),

\[
R\le T^{o(1)}\bigl(N^2V^{-2}+N^{18/5}V^{-4}
+TN^{12/5}V^{-4}\bigr). \tag{1}
\]

Proposition 12.1 addresses \(T^{5/6}\le N\le T\), \(V=N^\sigma\),
\(\sigma\ge7/10\), and gives in particular

\[
R\lesssim N^{2-2\sigma}+T^{1/2}N^{3-4\sigma}
+T^{(30\sigma-21)/5}N^{(46-60\sigma)/5}. \tag{2}
\]

The source's Theorem 1.2 bounds zero counts by
\(T^{15(1-\sigma)/(3+5\sigma)+o(1)}\).
Section 13.1 separates Type I zeros, which produce a large value of a
short truncated-Möbius detector, from Type II zeros, whose count is
\(\ll T^{2-2\sigma}(\log T)^{O(1)}\). The source does not exclude
an individual Type II zero. These are source statements; the following
budget and singleton tests are our deductions.

For a dyadic block of the actual retained polynomial, set
\(C_X=\max(1,\max_{n\sim N}|a_X(n)|)=X^{o(1)}\), and
\(b_n=C_X^{-1}a_X(n)(N/n)^{1/2}\). Then |b_n|<=1 and

\[
\mathcal A_{X,N}(1/2+it)
=C_XN^{-1/2}\sum_{n\sim N}b_nn^{-it}. \tag{3}
\]

The divisor bound proves the displayed subpower bound for C_X. Hard caps
are implemented by zero coefficients, and reflection/translation of the
t interval changes only coefficient phases. Thus coefficient signs and
the two sides of the frequency interval do not prevent applying (1).
What fails is its numerical strength at N comparable to X. Factorwise
use would additionally require a valid treatment of the coupled product
cap.

## Fresh exponent calculation

At V=N^(3/4), (1) gives
\(R\le T^{o(1)}(N^{1/2}+N^{3/5}+TN^{-3/5})\).
Write N=X^nu and T=X^tau, suppressing subpower factors. Compare its
exponent with the classical
\(N^{1/2}+TN^{-1/2}\) estimate and the elementary R<=1+T.

| Actual/current scale | nu | tau | New bound exponent | Classical exponent | Counting exponent |
| --- | --- | --- | --- | --- | --- |
| Full retained polynomial | 1 | 1/12 | 3/5 | 1/2 | 1/12 |
| A balanced factor | 1/2 | 1/12 | 3/10 | 1/4 | 1/12 |
| A factor of length X^(1/3) in K=3 HB | 1/3 | 1/12 | 1/5 | 1/6 | 1/12 |

Here the new exponent is
\(\max(\nu/2,3\nu/5,\tau-3\nu/5)\).
All three rows are weaker than counting. Making some factors short does
not bound the complete product or its continuum mismatch.

More generally, for nu<tau the classical dominant exponent is
\(\tau-\nu/2\); the new estimate is strictly smaller precisely when
\(\nu<10\tau/11\), aside from endpoints/subpower factors. This derives
the 10/11 useful threshold. The often quoted 5/6 is a convenient range,
not the whole improving range of (1). For the current tau=1/12, one
would need \(\nu<5/66\) for this improvement. A K=3 identity does not
make all relevant factors that short. Formula (2), at sigma=3/4,
has largest term T^(1/2) on its stated range, giving a further improvement
when N<T; our existing N>T rows still do not enter that range.

Artificially enlarging T to include the same few low-frequency values
does not add samples forced by the arithmetic. It increases the upper
bound in (1). Shorter physical windows or regrouped products therefore
need a new complete norm/remainder analysis before this comparison can
change. Every fixed nonzero low frequency remains in the retained annulus.

## Fresh singleton obstruction and the exact missing amplification

Suppose a hypothetical zero lies at beta+i*gamma with beta>b and gamma
of size T. A Type I detector supplies at least one large value. Even if
its normalized threshold is \(N^{\sigma-o(1)}\), with sigma<1, the
first term in (1) is \(N^{2-2\sigma+o(1)}\); it grows, rather than
tending below one. Likewise the stated density and Type II upper bounds
have positive exponents. Integer-valued zero counts therefore cannot be
forced to vanish by these inequalities alone.

The useful hypothetical lemma must be more specific than 'a zero gives a
large value'. For a **single common** 1-bounded polynomial of length
N=T^nu, one forbidden zero would need to force a 1-separated set W with

\[
|W|\ge T^{\eta-o(1)},\quad
\eta>
\max\{\nu(2-2\sigma),\nu(18/5-4\sigma),
1+\nu(12/5-4\sigma)\}, \tag{4}
\]

or the analogous exponent from (2), with coefficient-normalization
losses included. Inequality (4) would contradict (1). At the source's
illustrative N=T^(4/5), sigma=3/4, the right side is 13/25; a lone
sample is far short of it. For parameters where the right side exceeds
one, even filling the entire frequency interval cannot satisfy (4).

Simple continuity does not produce the missing set. On a normalized
dyadic block, remove the harmless N^(it) phase and put
\(\widetilde D(t)=\sum b_n(n/N)^{it}\). Then
\(|\widetilde D'(t)|\le(\log2)\sum|b_n|\ll N\).
A value of size V only guarantees persistence over a neighborhood of
radius comparable to V/N. For V=N^sigma with sigma<1 this is less than
one, providing no new 1-separated point. This is a bound on what this
continuity argument guarantees, not an upper bound on the actual level
set. A multiple zero also does not yield multiple separated ordinates.

Before applying (4), the hypothetical forbidden zero must be shown to
enter the common detector at all; the source's Type II classification
does not provide that. Alternatively the new lemma must handle the
Type II mechanism separately with a genuine singleton exclusion.

Assessment: no presently audited theorem closes either gate. Permit a
further scout only if it identifies a concrete arithmetic amplification
mechanism or a new range transformation with complete caps and low
frequencies. Broad searches for better density exponents and additional
finite zero checks are not the next investigation for the fixed-strip
goal. Programs 01, 02, and 03 remain more promising by readiness and
specificity of their unresolved signed input.
