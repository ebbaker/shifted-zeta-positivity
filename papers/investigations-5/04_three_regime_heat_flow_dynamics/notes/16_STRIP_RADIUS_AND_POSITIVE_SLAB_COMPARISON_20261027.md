# Strip radius, matched precision, and a moving contour on positive slabs

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.
Chat0005, thread `01a17e41-99d3-79c1-b932-2bae84ad0d47`.

**Status: proved in-note analytical comparison for the declared source
Taylor family; internal same-model checks.** A fixed shift reduces the
retained-mode allowance but does not reduce the optimized leading number
of Taylor entries. On each fixed slab b>0 a contour approaching the strip
edge yields a further logarithmic improvement in the sufficient number
of unaggregated mode coefficients. This is a data ledger, not a runtime,
bit-complexity, or optimality theorem. No field lower margin is acquired.

[Note15][n15] supplies every finite error and coefficient payment, including
both arms and physical H_x. [Note14][n14] requested this comparison.
The fixed-shift mode coefficient and earlier moving-contour tail in
[arithmetic-rigidity Note06][ar06] are inherited. The new return pays
quadrature radius and positive-time normalization together. Apply the
[result index][results], [controls][controls], [avoid index][avoid],
[classification][a01], [scope][a07] and [coupled-estimate rule][a12].
No literature-priority claim is made. See [Review07][review].

## 1. What is being compared

Let X=A+Delta tend to infinity, with Delta fixed, and fix
0<b<=B<=1/2. Use the same targets |E_j|/W_t(x)<=epsilon, j=0,1,
on [b,B] x [A,X], with W from Note15 (8) and fixed epsilon>0.
The same conclusions hold for the exact positive gamma modulus after
paying its bounded asymptotic ratio; the finite replay uses W exactly.

Every box freezes its contour shift sigma, retained K, frequency cutoff V,
source disks, quadrature nodes and order. This also applies when these
parameters are selected as functions of the **box endpoint X**. No
sigma'(x), cutoff derivative, or model-switch term is suppressed inside
a box. The direct physical first-jet consumer uses no unknown event
amplitude, no multiplicity hypothesis, and no all-real-zero assumption.

Put alpha=pi/8, g=alpha-sigma, c=sin(4g)=cos(4sigma).
For a fixed strip-safe radius ratio 0<rho<=1 let delta=rho g.
Take half-cell ratio 0<theta<1. The ledger T=Jq counts paired derivative
entries in Note15 (6); L=K T counts their individual theta-mode
contributions before source derivatives are aggregated. Both conjugate
arms are charged by the same convention in both methods. Fixed real
operation factors are not represented by this ledger.

## 2. Fixed shifts: the apparent order gain and radius cost

For each fixed sigma<alpha, the sharp mode test of Note15 (4) has
logarithm

\[
 gX-\pi c M^2+O_{b,B,\sigma}(\log^2X+\log M),\qquad M=K+1.
\]

Consequently the least integer passing this **upper-bound test**, or a
sufficient schedule with an O(log^2 X) numerator allowance, satisfies

\[
 M\sim\sqrt{\frac g{\pi\sin4g}}\sqrt X.                    \tag{1}
\]

This is not a necessary approximation length. The inherited raw value
is g=alpha,c=1, giving M~sqrt(X/8). At sigma=pi/16 the coefficient
of X in M^2 is sqrt(2)/16. Sending a fixed shift towards alpha *after*
the fixed-shift height limit gives coefficient 1/(4pi), a count ratio
sqrt(2/pi) relative to the raw schedule. This constant gain was already
identified in ar06; it is not a new research claim here.

The frequency test (2)-(3) permits V=(1/4)log X+O_sigma(1). Retaining the
same t in the source and W before taking the supremum gives

\[
 \log\mathcal M_j=(g+\delta)X+O_{b,B,\sigma,\rho}(\log X)
\]

for these schedules. Indeed t[(V+delta)^2-log^2(A/(4pi))/16]=O_B(log X).
Hence Note15 (7), with its explicit ceiling, gives

\[
 J\sim\frac{\log X}{8\theta\rho g},\quad
 q\sim\frac{(1+\rho)gX}{2\log(1/\theta)},
\]
\[
 \boxed{T=Jq\sim
 \frac{1+\rho}{16\theta\rho\log(1/\theta)}X\log X.}       \tag{2}
\]

The g cancels. Optimizing this leading ledger coefficient gives
rho=1 and theta=1/e, with T~(e/8)X log X for every fixed shift,
including raw sigma=0. The endpoint rho=1 is legitimate for the retained
finite source, as explained in Note15. This is optimization of the
displayed strip-safe sufficient ledger, not a lower bound for every
quadrature scheme; the finite source is entire and other bounds can
also examine disks outside this class.

At one *common* feasible disk delta, shifting lowers q's leading
numerator by sigma X. Comparing that order alone to raw disks fixed
at Note13's convenient 1/16 would hide the equally available raw radius.
The complete comparison therefore records no leading gain in T.

## 3. Precision can change the best shift

If log(epsilon^(-1))/X tends to p>=0, the leading mode-test coefficient
becomes (g+p)/(pi sin4g), while raw uses (alpha+p)/pi. For a fixed
positive shift the former is smaller precisely when

\[
 p<\frac{\alpha\sin4g-g}{1-\sin4g}.                        \tag{3}
\]

For p>0 the unique minimizer in 0<g<alpha satisfies
tan(4g)=4(g+p); the derivative of tan(4g)-4g is strictly positive.
At p=0 the infimum is at g down to zero. Large requested precision
pushes the minimizing shift back towards zero. Thus even the mode
allowance has no universal same-shift advantage for every target.

The optimized strip-safe Taylor coefficient, with rho=1, changes to
e(2+p/g)/16. For p>0 it is smallest at raw g=alpha. These statements
concern the declared upper-bound schedules and retain all lower-order
terms through Note15's finite tests.

## 4. A stronger schedule on each fixed positive-time slab

Positive time offers a different balance. Choose constants

\[
 0<\zeta<b/16,\quad
 Q>\max\{9/(4\pi),\ B/(8\pi),\ 2/\pi\},
\]
\[
 g(X)=\zeta\frac{\log^2X}{X},\quad
 \sigma(X)=\alpha-g(X),\quad c=\sin4g,
 \quad M=\left\lceil\sqrt{Q/c}\right\rceil,\quad K=M-1.   \tag{4}
\]

Require 0<g<alpha, a finite test. Then c M^2>=Q, so the mode rates
beta_M>=4pi Q-9>0 and 8pi c M^2>B hold. Let a_Q=2pi Q-4>0.
Since log(1+1/M)<=1/M,

\[
 \log r_M\le-a_Q/M-\pi Q/M^2<0,\quad
 (1-r_M)^{-1}\le1+M/a_Q.
\]

Thus the entire mode coefficient in either physical jet component is
at most a fixed constant times M^5. This is an explicit bound, not an
assumed nonvanishing denominator. Moreover

\[
 M\sim\sqrt{\frac{Q}{4\zeta}}\frac{\sqrt X}{\log X}.
\]

Dividing (4) of Note15 by the same W gives the uniform normalized error

\[
 E_{K,j}/W\le
 \exp\{(\zeta-b/16)\log^2X+O_{b,B,Q,\zeta}(\log X)\}
 \longrightarrow0.                                      \tag{5}
\]

The bound includes the polynomial M^5 and x^(-7/4) factor. Both
derivatives satisfy it. Fixed precision is allowed; more generally
log(epsilon^(-1))=o(log^2 X) is allowed. A precise finite application
must still test Note15's inequality at its actual tolerance.

### Frequency and quadrature do not erase this gain

Choose C>=0 with 2pi zeta e^(4C)>B/16, and set
V=(1/4)log X+C. The direct frequency gate holds eventually because

\[
 L_V=(\pi c/2)e^{4V}
       \sim2\pi\zeta e^{4C}\log^2X,
 \quad BV^2+10V=(B/16)\log^2X+O(\log X).
\]

Use this direct gate, rather than the convenient but looser onset
V>=(1/2)log(2(B+10)/eta_sigma). In (3) of Note15 the full-source
constant grows at most polynomially in 1/c. Its normalized logarithm
is bounded by

\[
 [\zeta-b/16-2\pi\zeta e^{4C}]\log^2X+O(\log X),         \tag{6}
\]

which is strictly negative. This pays the whole frequency tail.

With delta=rho g and theta fixed, the coupled quadrature envelope is

\[
 \log\mathcal M_j=(1+\rho)\zeta\log^2X+O(\log X).
\]

Therefore the explicit q of Note15 satisfies q=O(log^2 X), whereas
J=O(X/log X). For the least order selected by that bound the leading
T coefficient is again (2). Consequently

\[
 \boxed{T=O(X\log X),\quad
 K=O(\sqrt X/\log X),\quad L=KT=O(X^{3/2}).}              \tag{7}
\]

The equally informed raw sufficient schedule has
K=O(sqrt X), T=O(X log X), L=O(X^(3/2)log X). Thus (7) saves one
logarithm in this complete source-data ledger. The first-jet target is
the same, with all four error allocations retained.

This comparison is stronger than merely shrinking a summable local
error. It is also narrower than a computational speedup: aggregating
source derivatives, convolution in derivative order, finite arithmetic
and evaluation may cost more than KT. In particular a naive Leibniz
implementation can introduce additional q factors.

## 5. Conditioning, controls, and zero-time limits

The coefficient allowance in Note15 (11) remains finite and explicit.
For this moving schedule its kernel bound satisfies
log Z_j=(1+rho)zeta log^2 X+O(log X). The required scaled source
coefficient precision is thus exp(-O(log^2 X)) at fixed slab parameters,
after the finite number of entries is paid. This does not certify that
precision in an implemented evaluator or supply a field lower margin.

All limits in (4)-(7) are for **fixed b>0**, fixed B and box width, then
X to infinity. Zeta must be below b/16. Constants, crossover and source
conditioning deteriorate as b decreases. This is not a uniform result
at zero, nor an exclusion of each positive threshold. It neither changes
the canonical exterior onset exp(C/b) nor supplies its missing constants.

The fixed-cutoff endpoint comparisons and source controls are screened in
Note15. Euler-factor or other colliding even analytic sources can admit
their own accurate completed approximations; accurate source evaluation
is compatible with a collision. The unchanged theta coefficients specify
the evaluated field, not a separating inequality. No source-control
collision is rejected by the ledger result.

CE-02 gains a complete matched analytical acquisition comparison; CE-07
gains an explicit fixed-positive-slab schedule with nonuniform b dependence.
Effective coefficient evaluation and the physical first-jet lower margin
remain open. CE-04/06 gain no exclusion and CE-05 gains no energy saving.
See [the assessment][review] and [the continuation][next].

[n14]: 14_SECOND_RETURN_AND_NEXT_CANONICAL_CALCULATION_20261027.md
[n15]: 15_MATCHED_RAW_AND_SHIFTED_SOURCE_ERROR_BUDGET_20261027.md
[ar06]: ../../../investigations-3/11_arithmetic_collision_rigidity/notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md
[review]: ../reviews/07_RAW_SHIFTED_SOURCE_COMPARISON_REVIEW_20261027.md
[next]: 17_RAW_SHIFTED_RETURN_AND_IMPLEMENTATION_CONTRACT_20261027.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
