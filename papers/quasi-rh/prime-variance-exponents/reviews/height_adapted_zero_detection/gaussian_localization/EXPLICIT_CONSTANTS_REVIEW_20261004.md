# Internal review of explicit Gaussian constants and finite windows

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is internal same-model cross-review, not independent specialist
refereeing. The research note remains subject to mathematical review.

Reviewed artifact:
[Explicit constants and finite window](../../../notes/height_adapted_zero_detection/gaussian_localization/EXPLICIT_CONSTANTS_AND_FINITE_WINDOW_20261004.md).
The opening investigation's exact Mellin identity, pole-subtracted
convolution, PNT moment, and Kolesnik--Straus application are inherited;
this review concentrates on making their constants effective.

## Findings

The continuation supplies effective bounds for the full inverse transform
and all four omitted-physical budgets. With \(b=3/4\), \(|t|\ge100\),
\(N\ge\max(10,\lceil\mathcal Q(|t|)\rceil)\), the original linked
spectral samples and revised physical intervals give the conditional gate

\[
\sup_{y\in[24(N+1),208N]}e^{y/4}|\lambda_t(e^y)|
\le (8e)^{-N}/256
\]

throughout a candidate carrier band. The inverse norm is at most 32 and
the four remainder allowances sum to less than \((8e)^{-N}/4\), so
this arithmetic hypothesis would contradict the zero-side response.
The hypothesis itself has not been established.

The following points were checked in separate same-model analyses and
reconciled in the saved note.

1. **Effective transform lower bound.** The Sturm energy identity remains
   valid when its upper boundary value is nonzero. The imaginary part has
   coefficient \(|x\nu|/8\). A core radius \(\min(1,8/|z|)\) and the
   exact moment \(1/304\) yield denominator 608 in the refined lower
   bound. The nineteenth-power tail is weaker than the endpoint asymptotic
   but has an explicit coefficient and is adequate after Gaussian damping.
2. **Contour and derivative constants.** Central-frequency bounds and the
   shell reciprocal give \(P_{9/16}\le4e^{9k/256}/\sqrt k\) and
   \(P_{13/4}\le(11/10)e^{25k/4}/\sqrt k\) for \(k\ge8\).
   Cauchy's derivative estimate uses a radius \(1/8\) inside the inverse
   pole-free strip. The overlap at \(|\nu|=127/8\) is covered explicitly
   by comparing the central bound with the polynomial tail. The uniformly
   valid preparation coefficient \(15/512\) follows from the endpoint
   minimum of \(a/4-a^3\).
3. **Physical inverse norm.** Exact Gaussian moments give squared majorants
   below \(16^2,16^2,128^2\), including the tails. The Fourier convention
   gives \(\|q\|_1\le\sqrt{\|\psi\|_2\|\psi'\|_2}\) with constant
   one. This yields \(M<32\). It does not eliminate the restored pole.
4. **Physical baseline and pole.** Exact polynomial derivative bounds give
   \(B_h=33/4\). Positive coefficients of the endpoint-polynomial ratio
   after translation by \(t^2=10000\) prove the reciprocal pole bound
   \(|D_t'(1)|^{-1}<|t|^{13}/(5\cdot10^{11})\) throughout \(|t|\ge100\).
   The companion source checks all coefficients with rational arithmetic.
5. **Zero counts and endpoints.** Theorem 1.1 of
   [Bellotti--Wong v2](https://arxiv.org/html/2412.15470v2) supplies both
   bounds with the v2 constants. Taking the left limit at the lower guard
   endpoint retains every boundary zero and multiplicity. Conjugation
   covers negative carriers. The global constant 12 follows from the
   same theorem, including the low-height seed \(\mathcal N(5)\le3\),
   without importing a numerical zero table. The bounds on the expression
   \(\mathcal Q\) are not lower bounds for the actual cluster size.
6. **All-height errors.** Early and late ratios decrease in the sample
   parameter and then in \(N\); the explicit base \(N=10\) suffices.
   The pole has much larger exponential slack. The count expression also
   gives \(\log(1+|t|)<N\), controlling the fixed-minus-one remainder.
   Each of the four errors is below \(\eta_N/16\). The covering interval
   contains every continuous sample interval \([6k,26k]\).

## Corrections made during review

The inverse constants are asserted for \(k\ge8\), not \(k\ge1\).
Every sample used in the continuation has \(k\ge44\). The Cauchy-tail
overlap and uniform preparation minimum are now stated explicitly.
The final arithmetic gate includes every carrier and the complete physical
interval; it is not replaced by a finite set of arithmetic samples.

## Reproducible check scope

The [numerics directory](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
contains a standard-library source and a small record. It uses exact
fractions, rational Taylor remainders for exponentials and logarithms,
Machin's formula with alternating-series remainders for pi, and outward
decimal presentation. Nested logarithm inputs are rounded outward before
the next series to keep the calculation small. No floating result decides
a sign or a ceiling.

The checks cover rational probe norms and moments, derivative maxima,
endpoint-polynomial coefficient positivity, inverse coefficients, Gaussian
moment and tail inequalities, finite-budget base checks, and four example
guard-count ceilings. The examples are parameter certificates from a
published count theorem, not computations of the actual zeta zero set.
The proofs for all heights and sample counts are the analytic arguments
in the note, not extrapolations from those examples. The source hash
identifies the replay source; it is not a proof step.

The record gives \(N=41\), \(\mathcal Q\in
[40.507495483735023800,40.507495483735023801]\), and cover
\([1008,8528]\) at \(|t|=3\cdot10^{12}\). That scale remains enormous
for direct prime enumeration. No new zero exclusion follows without the
independent arithmetic hypothesis. Before any such claim, review the
complete arithmetic reduction and compare against established zero-free
results and verified finite heights.
