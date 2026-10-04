# A finite-prefix obstruction to structural exponent bootstrap

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal mathematical research and checks, not independent specialist review.

This continuation of the [subpower program](README.md)
strengthens the sparse PNT countermodel in selective-loss note 06 to a
complete **dyadic**, all-real-X statement and permits any finite prefix of
the actual coefficients to remain unchanged. It concerns generic structural
hypotheses, not the actual Euler-prime sequence. No smaller global exponent
for actual primes is proved.

## The non-bootstrap theorem

Keep the normalized fixed probe g, its support [-a,a] with a=1/4, and
w(t)=t^(-1/2)g(-log t), with A=e^(-a), B=e^a. Write

\[
\mathfrak G(s)=\int_{-a}^a g(v)e^{-sv}\,dv
\]

for the minus-exponent transform; in the manuscript's plus-exponent
convention this is G(-s). The established preparation and noncancellation
facts give \(\mathfrak G(1/2)=0\) and
\(\mathfrak G(s)\ne0\) for \(0<\Re s<1/2\).

For every fixed \(0<\delta<1\), every \(0\le\delta'<\delta\), every integer
\(N_0\ge2\), every fixed nonzero real \(\gamma\), and every
\(0<\eta<1/2\), there exists a nonnegative sequence \((c_n)_{n\ge2}\) such that:

1. \(c_n=\Lambda(n)\) for every \(2\le n\le N_0\). Beyond a finite index,
   \(c_n\in\{0,\log n\}\).
2. With \(\beta=(1+\delta)/2\), its cumulative counting function satisfies
   \[
   \widetilde\psi(x)=\sum_{2\le n\le x}c_n
   =x+\eta\Re\frac{x^{\beta+i\gamma}}{\beta+i\gamma}+O(\log x).
   \tag{1}
   \]
3. Its complete arithmetic response, diagonal and dyadic variance satisfy
   \[
   \widetilde p(y)=\sum_{n\ge2}\frac{c_n}{\sqrt n}g(y-\log n),
   \qquad \widetilde D(Y)=Y^2/2+O(1),
   \tag{2}
   \]
   \[
   \widetilde V(x)=\sqrt x\,\widetilde p(\log x),\qquad
   \widetilde{\mathcal V}(X)=\int_X^{2X}|\widetilde V(x)|^2dx
   \asymp X^{2+\delta}
   \tag{3}
   \]
   for **all sufficiently large real X**. The constants and starting
   thresholds can depend on the fixed parameters and retained prefix.

In particular, this sequence obeys the global input bound
\(\widetilde{\mathcal V}(X)=O(X^{2+\delta})\) but fails
\(O(X^{2+\delta'})\). Thus PNT, the correct diagonal, the linear frame
bound, the fixed preparation identities, and arbitrary finite-prefix
information do not imply a universal rule reducing delta.

## Construction and tracking proof

Set \(N=\max(N_0,8)\), retain the actual coefficients through N, and put
\(S_N=\sum_{2\le n\le N}\Lambda(n)\). Define, for x at least N,

\[
M(x)=x+\eta\Re\frac{x^{\beta+i\gamma}}{\beta+i\gamma},\qquad
F(x)=S_N+M(x)-M(N).
\]

Because \(\beta<1\),

\[
1-\eta\le M'(x)=1+\eta\Re x^{\beta-1+i\gamma}\le1+\eta<2
\qquad(x\ge1).
\]

For each integer n>N, choose c_n=log n if S_(n-1)<F(n), and c_n=0
otherwise; then set S_n=S_(n-1)+c_n. Starting from S_N=F(N), induction
proves

\[
0\le S_n-F(n)\le\log n\qquad(n\ge N).
\tag{4}
\]

Indeed the increment d_n=F(n)-F(n-1) is in (0,2). If the previous excess
minus d_n is nonnegative, no insertion is made and the new excess stays
between zero and log n. Otherwise an insertion is made and the new excess
lies in (log n-2,log n), which is positive because n>N>=8. For real x,
F changes by less than two between adjacent integers. Consequently
\(\widetilde\psi(x)=F(x)+O(\log x)=M(x)+O(\log x)\), proving (1).

This model satisfies PNT with a power-sized error O(x^beta). In particular,
for every fixed c>0 and every fixed nonnegative function L(x)=o(log x),

\[
\widetilde\psi(x)-x=O\bigl(xe^{-cL(x)}\bigr)
\qquad(x\to\infty).
\tag{5}
\]

These are asymptotic statements with parameter-dependent thresholds;
no claim is made that every published explicit PNT constant and starting
threshold holds for the model. Equation (5) includes the usual classical
and Vinogradov-Korobov decaying factors. Such factors alone do not force
an exponent below delta for this model.

## Complete response and an exact phase lower bound

The Stieltjes kernel q_y(t)=t^(-1/2)g(y-log t) vanishes at both endpoints
of its full support [exp(y-a),exp(y+a)]. For sufficiently large y that
interval lies beyond N. Integrating against dM gives a zero continuum
main, by \(\mathfrak G(1/2)=0\), and the exact oscillatory response
\(\eta\Re[\mathfrak G(\alpha+i\gamma)e^{(\alpha+i\gamma)y}]\), where
\(\alpha=\beta-1/2=\delta/2\). Integrating the tracking error
\(\widetilde\psi-M=O(\log t)\) by parts gives

\[
\widetilde p(y)=\eta\Re\left[
\mathfrak G(\alpha+i\gamma)e^{(\alpha+i\gamma)y}\right]
+O((1+y)e^{-y/2}).
\tag{6}
\]

For this error bound, use
\(q_y'(t)=-t^{-3/2}[g'(y-\log t)+g(y-\log t)/2]\);
the resulting fixed integral is
\(\int_{-a}^a e^{v/2}|g'(v)+g(v)/2|dv\).
The complete endpoints produce no boundary term.

Let \(\lambda=2+\delta\), \(\ell=\log2\), and
\(\theta_X=\gamma\log X+\arg\mathfrak G(\alpha+i\gamma)\). With x=Xe^t,
the exact normalization gives

\[
\widetilde{\mathcal V}(X)
=\eta^2|\mathfrak G(\alpha+i\gamma)|^2X^\lambda Q(\theta_X)
+O\left(X^{3/2+\delta/2}\log X+X(\log X)^2\right),
\tag{7}
\]
\[
Q(\theta)=\int_0^\ell e^{\lambda t}\cos^2(\theta+\gamma t)dt.
\]

The first error in (7) is the integrated main/error cross term; the second
is the tracking-error square. Both are o(X^lambda), uniformly in the
rotating phase. Direct integration shows

\[
\min_\theta Q(\theta)=\frac12\left\{
\frac{e^{\lambda\ell}-1}{\lambda}
-\left|\frac{e^{(\lambda+2i\gamma)\ell}-1}
{\lambda+2i\gamma}\right|\right\}>0.
\tag{8}
\]

The strict inequality follows from the strict triangle inequality for
\(\int_0^\ell e^{\lambda t}e^{2i\gamma t}dt\): its phase is not constant
on any interval because gamma is nonzero. Its maximum is finite. Together
with noncancellation at alpha+i gamma, equations (7)-(8) prove (3) for
all sufficiently large real X, not merely along a subsequence.

## The diagonal and other retained structural estimates

For all n>N, c_n^2=log(n)c_n. A finite initial discrepancy contributes only
a constant to

\[
\widetilde A_2(t)=\sum_{\log n\le t}\frac{c_n^2}{n}
=\int_{2^-}^{e^t}\frac{\log u}{u}\,d\widetilde\psi(u)+C_N,\qquad t\ge\log N.
\]

Partial summation with \(\widetilde\psi(u)-u=O(u^\beta)+O(\log u)\)
shows \(\widetilde A_2(t)=t^2/2+C+o(1)\): the endpoint error tends to
zero and the differentiated-error integral converges because beta<1.
The exact complete-cap identity

\[
\widetilde D(Y)=\int_{-a}^a g(v)^2\widetilde A_2(Y-v)dv
\]

then proves (2), since g squared is even and has integral one.
The retained prefix changes only the constant term.

The same model also retains the following facts.

- A counting bound \(\widetilde\psi(x)\le Cx\), with a fixed finite C,
  gives the packet frame bound \(\|\widetilde S_Y\|=O(1+Y)\) and
  \(\operatorname{Tr}\widetilde S_Y=\widetilde D(Y)\), by the existing
  local packet argument. Indeed the squared coefficient mass on a log
  packet is at most C e^(2a)(y+a).
- The differential energy identity and four-trend annihilation are fixed
  kernel identities and apply unchanged to this response. They supply no
  reduction of its growth exponent.
- On the complete integer band (AX,2BX),
  \(\sum(c_n-1)^2=O(X\log X)\). The existing Poisson, alias and outer-band
  proof therefore still gives outer variance O(X^2 log X) with
  L=X^(1/11); the growing central projection supplies the exponent in (3).
- Any predetermined finite family of bounded-range arithmetic certificates
  whose quantities depend only on these finitely many coefficients is preserved by choosing N_0 beyond every integer
  active in its complete smoothing windows. The eventual starting point
  in (3) is allowed to move outward. This is not an asymptotic certificate.

The theorem deliberately assumes delta<1: beta=1 would violate PNT and
would invalidate the diagonal remainder proof. To rule out a purported
bootstrap from delta=1 to a fixed delta'<1, choose any internal exponent
\(\delta\in(\max(0,\delta'),1)\). The model satisfies O(X^3) and still
violates O(X^(2+delta')). No beta=1 endpoint construction is needed.

## What a genuine bootstrap must add

The sequence has integer support and nonnegative logarithmic weights, but
its tail support is chosen greedily; it is not the actual prime-power
support. It has no asserted Euler product for the Riemann zeta-function,
no asserted multiplicativity, and no actual-prime correlation theorem.
Thus it does not refute an improvement for the true coefficients.

It proves the narrower necessity statement: a universal exponent-descent
argument cannot use only the retained structural properties and a bound
at its input exponent. It must add an arithmetic condition that excludes
this oscillatory model, or prove an inequality using information not
implied by those properties. For actual primes, that could be a theorem
for the complete signed covariance or central projection, with a genuine
fixed power saving after every cap and exceptional contribution is
included. Positivity, finer smoothing constants, subpower PNT savings,
and additional finite certificates alone do not supply such an input.

## Source dependencies and scope

The construction and tracking are a finite-prefix extension of
[selective-loss note 06](../selective-loss-program/06_global_mechanism_tests_20261003.md), Section 4.
The preparation and noncancellation facts, and complete linear response,
are established in the fixed-probe sources and manuscript. The diagonal
and frame reductions are in that same note, Sections 1 and 3. The
four-trend and outer-frequency identities are in
[selective-loss note 09](../selective-loss-program/09_actual_error_projection_and_frequency_20261003.md),
Sections 2 and 4-5. No additional prime-distribution theorem is assumed
for this countermodel. Its comparison with subpower PNT envelopes follows
directly from beta<1. All claims here remain generic structural
obstructions, with no new assertion about zeta zero locations.
