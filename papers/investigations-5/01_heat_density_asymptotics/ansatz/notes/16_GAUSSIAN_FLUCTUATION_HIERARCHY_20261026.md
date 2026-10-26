# A recurrence for the Gaussian fluctuation hierarchy

26 October 2026, America/New_York. Prepared for **Edward Baker**, with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Ansatz chat0004, thread 01a1765a-5c4e-7dd1-9de8-d70dd1725e34.

**Status:** exact algebraic reorganization, derived below; no new
asymptotic remainder theorem or independent assessment. No numerical,
machine-symbolic, exact-arithmetic, sampling or interval campaign.

The author requests terms indexed by increasing fluctuations, with
explicit relations between levels, and permits a continuous parameter
or smoothing scale if natural. We use the existing continuous Gaussian
scale T=-t and a discrete order j for departures from the tangent
exponential. The continuous generating parameter below encodes the same
grading. This develops [Note15](15_GENERALIZED_TRANSFORMS_AND_HEAT_COMPONENT_HIERARCHIES_20261026.md).

## 1. Base field and fluctuation coefficients

Fix the real chart center X, cutoff N=floor(sqrt(X/(4pi))), and d=z-X.
All chart parameters stay fixed under spatial/time differentiation.
For each arm epsilon=+1,-1 use the exact definitions

\[
w_\epsilon(z)=(1+\epsilon iz)/2,\quad
M(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)/16,\quad
h_{\epsilon n}(z)=M(w_\epsilon(z))n^{-w_\epsilon(z)}.
\]

Put b_epsilon,n=h_epsilon,n(X), lambda_epsilon,n=(log h_epsilon,n)'(X).
The only arithmetic sum required to generate the hierarchy is

\[
U_{\epsilon,0}(T,d)
=\sum_{n=1}^{N}b_{\epsilon n}
 e^{\lambda_{\epsilon n}d+T\lambda_{\epsilon n}^{\,2}}.
\tag{FH1}
\]

Let ell_epsilon(z)=log M(w_epsilon(z)), choosing an analytic branch on
the existing high-height chart. Define

\[
\kappa_{\epsilon,r}=\ell_\epsilon^{(r)}(X),\quad r\ge2.
\tag{FH2}
\]

These are independent of n because the logarithm of its arithmetic
factor is affine in z. For each fixed r the sectorial gamma inputs give
kappa_epsilon,r=O_r(X^(1-r)). Write gamma=kappa2, eta=kappa3,
zeta=kappa4 when suppressing epsilon. The exact local factorization is

\[
h_{\epsilon n}(X+q)
=b_{\epsilon n}e^{\lambda_{\epsilon n}q}
\exp\left(\sum_{r\ge2}\frac{\kappa_{\epsilon,r}}{r!}q^r\right).
\tag{FH3}
\]

The sum here converges locally, on the analytic log-gamma chart.
Fluctuation order counts the powers X^-1 in its coefficients:
kappa_r has weight r-1. It does not count arithmetic terms, nor assert
that these complex coefficients are cumulants of a probability law.

## 2. One operator incorporates the smoothing

Define

\[
\boxed{\mathcal Q_T=d+2T\partial_d.}
\tag{FH4}
\]

For k_T(d-q)=(4pi T)^(-1/2)exp(-(d-q)^2/(4T)),
Q_T k_T(d-q)=q k_T(d-q). Thus Gaussian evolution converts
multiplication by q into Q_T, for both full and fixed-window integrals.
No boundary integration by parts is used in this identity.

For a frozen exponential,

\[
\mathcal Q_T^m e^{\lambda d+T\lambda^2}
=\partial_\lambda^m e^{\lambda d+T\lambda^2}.
\tag{FH5}
\]

The induction step uses commutation of Q_T with partial_lambda.
Equivalently, Q_T is Gaussian evolution's multiplication operator.
The smoothing width is sqrt(2T); the moment polynomials also contain
the displaced argument d+2T lambda.

For L=partial_T-partial_d^2,

\[
[L,\mathcal Q_T]=2\partial_d-2\partial_d=0.
\tag{FH6}
\]

Consequently Q_T preserves exact heat solutions.

## 3. The hierarchy and its recurrence

For r>=1 define commuting operators

\[
\mathcal D_{\epsilon,r}
=\frac{\kappa_{\epsilon,r+1}}{(r+1)!}\mathcal Q_T^{r+1}.
\tag{FH7}
\]

Define the fluctuation levels from FH1 by the triangular recurrence

\[
\boxed{
j\,U_{\epsilon,j}
=\sum_{r=1}^{j}r\,\mathcal D_{\epsilon,r}
 U_{\epsilon,j-r},\qquad j\ge1.
}
\tag{FH8}
\]

Every level is generated from earlier ones; no additional arithmetic
sum is needed. The first terms are

\[
\begin{aligned}
U_1&=\mathcal D_1U_0,\\
U_2&=(\mathcal D_2+\tfrac12\mathcal D_1^2)U_0,\\
U_3&=(\mathcal D_3+\mathcal D_1\mathcal D_2
                    +\tfrac16\mathcal D_1^3)U_0.
\end{aligned}
\tag{FH9}
\]

In the local shape coefficients,

\[
\begin{aligned}
U_1&=\frac{\gamma}{2}\mathcal Q_T^2U_0,\\
U_2&=\left(\frac{\eta}{6}\mathcal Q_T^3
              +\frac{\gamma^2}{8}\mathcal Q_T^4\right)U_0,\\
U_3&=\left(\frac{\zeta}{24}\mathcal Q_T^4
       +\frac{\gamma\eta}{12}\mathcal Q_T^5
       +\frac{\gamma^3}{48}\mathcal Q_T^6\right)U_0.
\end{aligned}
\tag{FH10}
\]

Thus j=1 resolves curvature; j=2 includes the next logarithmic shape
derivative and repeated curvature; j=3 includes the next derivative,
its lower-order mixed contribution, and three curvature factors.
Every product at level j has coefficient weight X^-j.

For a proof of FH8 introduce a formal marking parameter s:

\[
\mathcal U_\epsilon(s)
=\exp\left(\sum_{r\ge1}s^r\mathcal D_{\epsilon,r}\right)U_{\epsilon,0}
=\sum_{j\ge0}s^jU_{\epsilon,j}.
\tag{FH11}
\]

All D_r commute at fixed T, hence

\[
\partial_s\mathcal U_\epsilon
=\left(\sum_{r\ge1}r s^{r-1}\mathcal D_{\epsilon,r}\right)
\mathcal U_\epsilon.
\tag{FH12}
\]

Comparing coefficients gives FH8. Each coefficient is a finite
polynomial, so the recurrence is exact without any infinite-series
convergence claim. More explicitly it is the sum over nonnegative
integers k_r with sum(r k_r)=j of
product(D_r^k_r/k_r!) applied to U0.

Each such product has polynomial degree sum((r+1)k_r), between j+1
and 2j for j>=1. This explains why polynomial degree is not the desired
fluctuation index: gamma^2 Q^4 belongs to level2, whereas zeta Q^4
belongs to level3. From FH6,

\[
(\partial_T-\partial_d^2)U_{\epsilon,j}=0
\quad\hbox{for every finite }j.
\tag{FH13}
\]

## 4. Continuous scale and continuous fluctuation strength

T is already the natural continuous smoothing variable. Setting E=u^2
in the canonical cosine representation gives the exact Laplace form

\[
H(-T,z)=\int_0^\infty e^{-TE}
\frac{\Phi(\sqrt E)\cos(z\sqrt E)}{2\sqrt E}\,dE.
\tag{FH14}
\]

The weight at E=0 is integrable. For general z this spectral integrand
is not a positive measure. Increasing E means shorter spatial
wavelength; increasing T suppresses it more strongly.

The generating parameter can also be made an actual continuous
fluctuation deformation on the fixed initial window. With A(q) the
exponential factor in FH3, define

\[
A_s(q)=\exp\!\left(\frac{\log A(sq)}s\right),\quad 0<s\le1,
\qquad A_0(q)=1.
\tag{FH15}
\]

Then log A_s(q)=sum_{r>=1}s^r kappa_(r+1)q^(r+1)/(r+1)!.
At s=0 only the tangent exponential remains; at s=1 the exact local
gamma factor is restored. The quotient has a removable singularity at
s=0. For the existing window |q|<=V inside the analytic log-gamma disk,
its bounded heat integral is an actual continuous family.

Its Taylor coefficients obey FH8 with the bounded-window version of
U0. FH1 uses the elementary whole-line exponential transform, so
replacing those bounded coefficients by FH1's versions requires the
same kind of polynomial-tail payment as Note05. FH11 is not asserted
to be a globally convergent infinite operator sum on the whole line.

This separates continuous smoothing T, continuous fluctuation strength
s, and discrete fluctuation order j, while relating them in one formula.
For the current finite ansatz, FH8 is the simplest working definition.

## 5. Relation to AN03 and the existing growing-order formula

On an individual carrier,

\[
\frac{\gamma}{2}\mathcal Q_T^2 e^{\lambda d+T\lambda^2}
=\frac{\gamma}{2}\big((d+2T\lambda)^2+2T\big)
 e^{\lambda d+T\lambda^2}.
\tag{FH16}
\]

At d=0 its relative correction is gamma(T+2T^2 lambda^2), exactly
AN03's evaluated factor at the center. AN03's compact formula
re-centers beta and gamma at each target z; its spatial differentiation
therefore differs from the frozen-X hierarchy and gives its estimated
nonzero residual. FH13 applies to the frozen hierarchy.

The original Note05 polynomial-degree truncation is
sum_{m<=J} a_epsilon,m Q_T^m U_epsilon,0. FH8 groups the same Taylor
monomials by sum(r k_r), instead of by sum((r+1)k_r).
Finite truncations consequently differ. The old bound at J=ceil(3L)
cannot be transferred by simply renaming J as j.

With the unchanged bounded RS completion I_X,K, define

\[
F_X^{[p,K]}(-T,z)
=\sum_{\epsilon=\pm1}\sum_{j=0}^{p}U_{\epsilon,j}(T,z-X)
+\mathcal I_{X,K}(T,z),\qquad
E_X^{[p,K]}=H-F_X^{[p,K]}.
\tag{FH17}
\]

Then the requested relation between consecutive approximations and
errors is exact:

\[
F_X^{[p+1,K]}=F_X^{[p,K]}+\sum_\epsilon U_{\epsilon,p+1},
\qquad
E_X^{[p+1,K]}=E_X^{[p,K]}-\sum_\epsilon U_{\epsilon,p+1}.
\tag{FH18}
\]

All finite F have zero heat residual with fixed chart data. Error
smallness still requires comparison to canonical initial data. The
RS hierarchy remains independent:
I_X,K+1-I_X,K is the bounded heat transform of its next real RS term;
the exact cutoff transfer is already included and cancels in this
difference. Refining gamma fluctuations alone does not refine that
source remainder.

Nominal X^-j coefficient order is not yet a uniform field-error rate.
The powers of d+2T lambda and T, the arithmetic population, complex
buffers, growing j constants, and retained RS error all matter.
For example first curvature has dimensionless size measured by
|gamma| times (|d+2T lambda|^2+2T). A larger smoothing time can change
the balance; no all-time ordering or monotonic error reduction follows.

## 6. Scope and bounded continuation

This is a useful organizational identity requested by the author,
not an RH criterion or a new quantitative milestone. Carry the
[result index][results], [heat-flow cluster][r11],
[collision controls][r12], [avoid index][avoid],
[reformulations][a01] and [termwise bounds][a12].
The heat-operator identity applies to all suitable initial sources.
The Euler-factor, weighted-square, reflected and smooth-shape controls
therefore also have it; they fail the unchanged canonical gamma-zeta
initial-data premise, not FH6. No collision exclusion is inferred.

**Next owner: Analysis — Sol**, [HDA-A02-AN07 r1][packet], prepared only.
Validate the first two fluctuation levels as an asymptotic truncation
on the existing [1,2] slab, with a matched retained RS order and full
field/jet/time errors. This is the immediate follow-up to the author's
new focus. A08-AN01 remains prepared for subsequent positive-time work.
No manuscript integration or source-domain extension is made here.

[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[packet]: ../research-progress/handoffs/HDA-A02-AN07.md
