# Compact correction and a revised positive main term

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Exact serving variant and configured reasoning effort are not exposed and are not inferred. The lead and separate same-model agents checked the operator regrouping. This is internal research, not specialist refereeing.

The new positive correction directions do not prevent a revised main term. At the fixed first-prime window, the existing kernel formulas give a compact operator on the source space. Its positive spectral part is an explicit candidate to subtract from B. The resulting positivity inequality is unproved and is stronger than Weil positivity; this note separates the established construction from that research target.

## Scope and exact identity

Take I=(-1/2,1/2), S={2}, and exponent 1/2. For smooth prepared sources F supported in I, the [finite Euler identity](FINITE_EULER_BOUNDARY_IDENTITY_20261003.md) gives

\[
Q[F]=B[F]-K[F],\qquad B[F]=\|C_F\Pi\|_{\mathrm{HS}}^2\ge0.
\]

The mean-zero condition may additionally be imposed. Let H be the L2(I) closure of the chosen smooth prepared source class. All claims about B and Q below are made on that smooth class; no unproved closed realization of B is used.

Adding a nonnegative form J to B while preserving Q requires adding the same J to K. It does not improve the comparison. Instead seek a nonnegative form R with

\[
K[F]\le R[F]\le B[F].
\]

Then B_new=B-R and Q=B_new+(R-K) are both sums of nonnegative terms. Constructing R without using Q is straightforward here; proving R at most B is the new obligation.

## Compactness on the source space

The [translated resonance note, Sections 1 and 2](FIRST_PRIME_TRANSLATED_RESONANCE_20261003.md) establishes

\[
K[F]=\int_{\mathbb R}\kappa_F(u)k(u)\,du,
\qquad k(u)=e_1(|u|)+r(|u|),
\]

where e1 is the first-return kernel and

\[
r(u)=\Re\operatorname{Tr}(R_\mathrm{ret} P U_u\chi),
\quad R_\mathrm{ret}=C^3(I-C^2)^{-1}T\in\mathfrak S_1.
\]

The function r is continuous and bounded by the trace norm of R_ret. The factor two occurs in the positive-half-line integral, not in the even kernel k. The first-return kernel has only finitely many logarithmic singularities on a bounded difference interval, with e1(u)=O(u(1+|log u|)) near zero. Hence k belongs to L2(-1,1).

Define the real symmetric integral operator on L2(I) by

\[
(A_KF)(x)=\int_I k(y-x)F(y)\,dy.
\]

It is selfadjoint and Hilbert-Schmidt, since

\[
\|A_K\|_{\mathrm{HS}}^2
=\int_{-1}^{1}(1-|u|)|k(u)|^2\,du<\infty.
\]

Fubini's theorem gives K[F]=<F,A_KF>. Thus the original smooth correction has a bounded extension to L2(I). Compress A_K to H, writing A=E_H A_K|_H. This remains compact and selfadjoint and represents K on the admissible sources. Compactness is asserted in the variable F, not the profile h before applying the unbounded preparation operator.

The infinite-positive-index result implies that A has infinitely many positive eigenvalues on the prepared mean-zero space. Compactness implies that those eigenvalues tend to zero. These statements are compatible: an infinite number of positive directions does not require a positive lower bound on their strengths. The functional-analytic step is the standard [spectral theorem for compact selfadjoint operators, MIT Lecture 22](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/57596554e180e442c9487f580303147b_MIT18_102s21_lec22.pdf); the compact kernel realization above is a deduction from the investigation's formulas.

## An exact spectral modification

Use the positive and negative spectral parts

\[
A=A_+-A_-,\qquad A_+,A_-\ge0,
\quad K_\pm[F]=\langle F,A_\pm F\rangle.
\]

These are quadratic forms. In particular K_plus is not the scalar function max(K[F],0). Set

\[
\boxed{B_\mathrm{new}[F]=B[F]-K_+[F].}
\]

Then exactly

\[
Q[F]=B_\mathrm{new}[F]+K_-[F].
\]

The proposed sufficient estimate is B at least K_plus. It is not a consequence of the definition and is generally stronger than Q at least zero: it discards the helpful contribution K_minus. No positive trace or squared-norm representation of B_new has been established. Such a representation, or a direct domination bound, would be genuine additional work.

## A finite approximation with an infinite tail allowance

For any eta>0, compactness supplies a finite-rank selfadjoint A_N on H with ||A-A_N|| at most eta. A concrete certification can use a square-integrable approximation to the kernel, whose L2 error bounds the operator norm; the logarithmic singularities must be retained in this error estimate. Compression to H is contractive.

Writing (A_N)_plus for the positive spectral part of the finite-rank approximation, define

\[
R_{N,\eta}[F]
=\langle F,(A_N)_+F\rangle+\eta\|F\|_2^2.
\]

Then R_N_eta is nonnegative and K at most R_N_eta. Therefore

\[
B[F]\ge R_{N,\eta}[F]
\quad\Longrightarrow\quad
Q[F]=(B-R_{N,\eta})[F]+(R_{N,\eta}-K)[F]\ge0.
\]

The eta times norm-squared term has infinite rank. Keeping it is essential and avoids contradicting the obstruction to finite-rank penalty domination. The comparison B at least R_N_eta is not established by checking only the finite matrix: the complementary source space and mixed terms also need control. In particular, a trace over finitely many state-space trial vectors is compact as a form on the fixed source interval, even though it need not have finite rank there. Each map F to F convolved with a trial vector y is Hilbert-Schmidt from L2(I) to the output space, with squared Hilbert-Schmidt norm |I| times ||y|| squared. Thus this finite-state trace alone cannot dominate eta times the identity on the whole infinite-dimensional source space.

For comparison, subtracting just the first return K1 from B leaves the exact higher-return correction K-K1. Its trace-class physical operator and continuous source kernel improve regularity, but do not give its sign or prove B-K1 positive.

## Research implication

This construction provides a precise way to accommodate the positive correction and a bounded first target: build a certified approximation to the source correction at L=1, bound its remaining operator norm, and seek a simultaneous lower bound for B covering the finite positive part and the tail allowance. The [two-packet calculation](TWO_PACKET_WEIL_SCALE_20261003.md) supplies evidence that the known resonant examples are small relative to B, but does not bound the largest positive direction or mixed terms. No quantitative spectral approximation or comparison certificate is supplied here.

Everything in this note concerns the fixed first-prime window. A result relevant to the full Weil criterion would still need a support-adapted extension through growing prime sets. No uniform compactness estimate, spectral tail rate, or positivity result for that extension is asserted.


Subsequent continuation: the [local outcome](REVISED_B_LOCAL_OUTCOME_20261003.md)
now proves Q>=B/9000 at L=1 on the prepared mean-zero class using an
independent arithmetic certificate. The unweighted positive-part comparison
proposed above remains open.
