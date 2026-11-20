# AGC-E16 r0: exact finite-Euler preflight return

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Explicit helper dispatch: **gpt-6.1-sol,
reasoning effort ultra**; independent serving-backend attestation is
unavailable. **Type E**, bounded execution of the preflight recorded in
the [sole register](../01_AGC_RESEARCH_PROGRESS_20261119.md). The root
authorized B04's one correction pass to include the source's correlated
two-carrier ellipse estimator. No numerical evaluation, phase sampling,
code-based mathematical calculation or parameter campaign was performed.

**Return:** the eight surviving prime coefficients alone have total
weighted magnitude **strictly greater than 21/20** at the actual
endpoint. Thus the anchor-one coefficientwise triangle allowance is
negative before the second branch, correction and complete source error
are paid. The correlated ellipse allowance also loses: its prime cost is
strictly greater than `(21/20)(1-g)`, against anchor `1-g`, for every
`0<=g<1`. This is a scoped failure of the declared estimating class,
not a zero of the arithmetic reference or theta field. E16 r1 and
Note17 remain reserved for B04's frozen request.

Read [result summaries](../../../../../result-summaries/README.md),
[patterns](../../../../../avoid/README.md),
[Controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
and patterns [01](../../../../../avoid/01_restating_the_target.md),
[02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
Classification under pattern01: a numerical-threshold analytical
obstruction for a fixed lower-bound implementation, not an
RH-equivalent reformulation or a positive-margin acquisition.

## Exact normalization and convolution

Use manuscript [Section5](../../manuscript/sections/05_arithmetic_source.tex)
without changing its carrier, branches or coefficients. At

\[
t=\frac1{10},\qquad x_0=14000+\sqrt{24/25},\qquad y=\frac15,
\]

put

\[
s=\frac35-\frac{i x_0}{2},\quad
s_{\rm eff}=s+\frac1{20}\alpha(s)=\sigma+i\tau,
\quad b_n=\exp(\log^2n/40),
\]

\[
A_N=\sum_{n=1}^N b_n n^{-s_{\rm eff}},\qquad
E=\prod_{p\in\{2,3,5\}}(1-b_p p^{-s_{\rm eff}}),\qquad
D=30.
\]

The letter `E` here is the finite Euler multiplier, not the source
error. Set `lambda_1=1` and

\[
\lambda_d=\prod_{p\mid d}(-b_p)\quad(d\mid30).
\]

The **exact finite** convolution is

\[
EA_N=\sum_{k=1}^{30N}\beta_{k,N} k^{-s_{\rm eff}},\qquad
\beta_{k,N}=\sum_{\substack{d\mid(k,30)\\k/d\le N}}
                    \lambda_d b_{k/d}.                    \tag{1}
\]

The cutoff indicator is essential: coefficients with `k>N` cannot use
an untruncated `b_k` term. The heat weights are not multiplicative;
no Euler-product identity for the complete series is being asserted.

At the endpoint, `N=33`. Indeed `14000<x0<14001` and
`25/8<pi<22/7` give

\[
33^2<\frac{x_0}{4\pi}+\frac1{160}<34^2.
\]

Consequently, for

\[
\mathcal P=\{7,11,13,17,19,23,29,31\},
\]

only `d=1` occurs in (1), so

\[
\boxed{\beta_{p,33}=b_p>0\quad(p\in\mathcal P).}          \tag{2}
\]

In contrast, the coefficients at `2,3,5` cancel exactly, since both
corresponding original indices are present.

## The actual exponent is below 4/5

Write `T=x0/2`. Direct substitution in Section5's alpha formula gives

\[
\Re\alpha(3/5-iT)
=\frac{3/10}{T^2+9/25}-\frac{2/5}{T^2+4/25}
  +\frac12\log\frac{\sqrt{T^2+9/25}}{2\pi}.
\]

The first two terms have negative sum. Also
`sqrt(T^2+9/25)<7001`, `2pi>6`, and
`e^8>(5/2)^8>7001/6`. Hence

\[
\Re\alpha(s)<4,\qquad
\boxed{\sigma=\frac35+\frac1{20}\Re\alpha(s)<\frac45.}   \tag{3}
\]

Only elementary inequalities are used here; no rounded alpha value is
an input.

## An exact rational lower bound for the prime mass

Let `P_j(u)=sum_{h=0}^j u^h/h!`. For each row in the following table,
all entries are rational:

| p | r with log(p)>r | v with r/5+r^2/40>v | k with P4(v)/p>k/1000 |
| --- | --- | --- | --- |
| 7 | 19/10 | 47/100 | 228 |
| 11 | 23/10 | 59/100 | 163 |
| 13 | 5/2 | 13/20 | 147 |
| 17 | 14/5 | 3/4 | 124 |
| 19 | 29/10 | 79/100 | 115 |
| 23 | 31/10 | 43/50 | 102 |
| 29 | 33/10 | 93/100 | 87 |
| 31 | 17/5 | 193/200 | 84 |

For a compact verification of the logarithm column, first

\[
e<\frac{1957}{720}+\frac1{4410}<\frac{68}{25}.
\]

Here `1957/720=P6(1)` and the remaining exponential series is bounded
by `(1/7!)/(1-1/8)=1/4410`. For the successive rows, take

\[
(a,m)=(2,1),(3,2),(3,2),(3,1),(3,1),(4,3),(4,2),(4,2).
\]

Then `a=ceil(r)` and the following exact rational inequalities verify
every logarithm entry:

\[
e^r=\frac{e^a}{e^{a-r}}
 <\frac{(68/25)^a}{P_m(a-r)}<p.                         \tag{4}
\]

The `v` column follows by substituting `r`; the last column follows by
substituting `v` into the displayed quartic, or cross-multiplying its
positive rational denominators. For clarity, the eight last-column
inequalities are exactly

\[
\begin{array}{ll}
P_4(47/100)>1596/1000,&P_4(59/100)>1793/1000,\\
P_4(13/20)>1911/1000,&P_4(3/4)>2108/1000,\\
P_4(79/100)>2185/1000,&P_4(43/50)>2346/1000,\\
P_4(93/100)>2523/1000,&P_4(193/200)>2604/1000.
\end{array}                                                   \tag{5}
\]

Using (3), positivity of the logarithms and the positive exponential
series,

\[
\begin{split}
\sum_{p\in\mathcal P}|\beta_{p,33}|p^{-\sigma}
&>\sum_{p\in\mathcal P}b_p p^{-4/5}\\
&=\sum_{p\in\mathcal P}\frac1p
   \exp\left(\frac{\log p}{5}+\frac{\log^2p}{40}\right)\\
&>\frac{228+163+147+124+115+102+87+84}{1000}
 =\boxed{\frac{21}{20}}.                                  \tag{6}
\end{split}
\]

Every inequality in the summation is strict. Therefore exact equality
of the rational comparison sum to `21/20` causes no endpoint issue.
The first-branch anchor-one allowance alone is strictly below `-1/20`.
The other convolved coefficients, the entire reflected branch,
retained correction and complete source allowance are additional
nonnegative payments and cannot repair it.

## Authorized correction pass: correlated two-carrier cost

Selected-primary-source reading on 19 November: Polymath v2,
[Section8.5, equations(96)--(98), Lemma8.5](https://arxiv.org/html/1904.12438v2#S8.SS5),
with definitions(14)--(19) and source bounds(20)--(24). The source's
equation(79) is explicitly a heuristic, not an exact multiplicative
identity. Its numerical constants for `t=.2` are not imported here.

Set

\[
\kappa=\frac t2\{\alpha(s_+(z))-\overline{\alpha(s_-(z))}\},
\qquad g=|\gamma|.
\]

After paying `n^(-kappa)-1` separately, conjugation of the second
polynomial gives the exact real-coefficient convolution

\[
\alpha_{k,N}=\sum_{\substack{d\mid(k,30)\\k/d\le N}}
             \lambda_d(k/d)^y b_{k/d},\qquad\alpha_{1,N}=1.
\]

This convention puts any common factor bounding `|gamma|` into `g`,
so the source's factor `1.03` is not also inserted into these alpha
coefficients. At the retained primes,

\[
\alpha_{p,33}=p^y b_p\ge b_p=\beta_{p,33}.
\]

For `0<=g<1`, the corresponding ellipse cost per coefficient is

\[
c_{k}(g)=\max\left(
 |\beta_k-g\alpha_k|,
 \frac{1-g}{1+g}|\beta_k+g\alpha_k|\right).
\]

Its anchor is `1-g`. Since the retained alpha and beta coefficients
are positive and `alpha_p>=beta_p`,

\[
c_p(g)\ge\frac{1-g}{1+g}(\beta_p+g\alpha_p)
       \ge(1-g)\beta_p.
\]

Equation(6) therefore proves

\[
\boxed{1-g-\sum_{k\ge2}c_k(g)k^{-\sigma}
       <-\frac{1-g}{20}<0.}                                \tag{7}
\]

The separately paid kappa discrepancy, retained leading correction and
complete source error only decrease this signed allowance. If `g>=1`,
the anchor `1-g` is already nonpositive and this positive-anchor
ellipse proof does not apply. Thus the retained-prime block defeats
both the original preflight class and this source-conditioned
correlated correction before any other payment is evaluated.

## Controls, scope and disposition

This is a canonical coefficient-mass lower bound, not an assertion
that finite Euler relations force theta nonvanishing. The Controls12
premise screen remains explicit:

| Control | Premise that fails for the unchanged imported theta reference |
| --- | --- |
| Euler-factor | Unchanged complete canonical coefficients and theta source |
| Weighted-square | All theta weights and complete normalized reflection |
| Reflected super-Gaussian | Exact integer-square theta expansion |
| Smooth shape/positive primitive | Complete arithmetic square expansion |
| Finite-prime orbit | Unchanged complete coefficients and full reflection; the selected-prime identities alone survive |
| Finite-profile/atomic threshold | Complete theta arithmetic and full theta growth/profile data |
| RH-conditional close source | Ordinary theta Dirichlet-series arithmetic |

These source-premise failures do not assert a control fails every
derived inequality. At any actual included zero `H=0`, a valid complete
enclosure gives `|Q_val|<=V_val`; a complete paid margin therefore
cannot be positive. The generic exact collision
`H=P=z^2-2(t-T)` even has zero source error: its strict value margin
fails at the event. No universal collision exclusion is inferred.

**Disposition:** r0 completion condition met with (6), strengthened by
(7). No new prime set, phase information, physical source, time target,
or numerical packet was chosen. A later B04-issued E16 r1 may formalize
its requested interval or tail interfaces; this return does not execute
that unissued target. Shared indexes, manuscript, progress register and
chat history remain under the root's ownership.
