# Smooth windows and height-dependent collision times

6 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance from **OpenAI Codex**. The exact current model
identifier and reasoning effort are unavailable in the session metadata;
neither is inferred from earlier sessions or the recommended model.

**Task:** TND-O-B03 r3, **B — conceptual research**. The author proposes
Gaussian/bump or Poisson smoothing with a width decreasing at high zero
density, seeking collision-time bounds improving with height. One focused
analytical comparison and local consistency check. This note records exact
elementary identities, a conditional time-transfer bound, an existing
literature benchmark, and the remaining arithmetic question. It proves
no new canonical collision-time bound. No numerical campaign, separate
assessment, manuscript revision or successor execution was performed.

| Next task | Type | Recommended model | Dependency | Expected output |
| --- | --- | --- | --- | --- |
| TND-O-B03: select a smooth detector and a quantitative arithmetic target | B — conceptual research | Astra: the observable and independently accessible bound remain unsettled | This note and the E06 manuscript | One fixed window/frequency/height regime and upper-bound target, or the precise unavailable estimate |

The [sole register](../../research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md)
owns status. This continues the two-observable comparison in
[Continuation05](05_TND_O_B03_LOCALIZED_STATISTICS_CONTINUATION_AND_MODEL_CHANGE_20261106.md).
Gaussian and Poisson kernels are compared as smoothing choices within
that program, not as additional research branches.

## 1. Two different Gaussian operations

For the height weights, an admissible candidate is

\[
w_{T,h}(t)=\exp\left(-\frac{(t-T)^2}{2h^2}\right).
\tag{1}
\]

This window has height width h. It makes a sum over the entire zero set
absolutely convergent using the classical zero-count growth and the
critical strip. For each fixed a and r,

\[
\sum_j w_{T,h}(t_j)
 |e^{(\rho_j-1/2)(a+r)}|
 \le e^{|a+r|/2}\sum_jw_{T,h}(t_j)<\infty.
\]

Consequently the manuscript's reflection argument and exponential Gram
integral extend to these weights by dominated convergence. But a Gaussian
has no strictly bounded height support: the finite-window phase argument
must now pay for the tails. A smooth compact bump retains exact support
and therefore retains that argument directly.

Separately, one can smooth the auxiliary variable r of the Gram integral.
Its width is a different parameter, denoted b below; it is not automatically
equal to h or to a physical heat time.

For the original statistic, put

\[
F_{T,h,a}(r)=\sum_j w_j e^{(\rho_j-1/2)(a+r)},\qquad
E=\int_{\mathbb R}e^{-2|r|}|F_{T,h,a}(r)|^2\,dr.
\]

For every b>0 the elementary inequality

\[
e^{-2|r|}\ge e^{-2b^2}e^{-r^2/(2b^2)}
\tag{2}
\]

follows from (|r|-2b^2)^2>=0. Thus, defining the normalized Gaussian
quadratic form

\[
E_b^G=\frac1{\sqrt{2\pi}b}
\int_{\mathbb R}e^{-r^2/(2b^2)}|F_{T,h,a}(r)|^2\,dr,
\]

we have the rigorous comparison

\[
E\ge\sqrt{2\pi}b\,e^{-2b^2}E_b^G.
\tag{3}
\]

The Gaussian integral can be evaluated exactly. With reflection-invariant
height weights, the same relabeling as in manuscript Proposition 14.3 gives

\[
E_b^G=\sum_{j,k}w_jw_k
 \exp\left(a(\rho_j-\rho_k)
       +\frac{b^2}{2}(\rho_j-\rho_k)^2\right).
\tag{4}
\]

For a selected pair rho_±=1/2±d/2+i theta, its isolated squared norm is

\[
P_b^G=2w_0^2\left[1+e^{b^2d^2/2}\cosh(ad)\right].
\tag{5}
\]

These formulas simplify the kernel calculation; they do not imply
E_b^G>=P_b^G. Mixed terms can still interfere. Without further structure,
the reverse-triangle lower bound retains the background norm. A Gaussian
minorant in r also still contains large-|r| phases, so it does not by itself
give the earlier bounded-phase projection argument.

For a smooth bump 0<=chi(r)<=1 supported on [-R,R], the simpler exact
lower bound E>=integral chi(r)e^{-2|r|}|F(r)|^2 dr remains available.
If the height window is also supported in |t-T|<=h and h(a+R)<pi/2,
the positive-projection proof applies on its entire support. Gaussian
transform convenience and compact-support phase control are distinct
advantages to compare.

## 2. Poisson terminology and the variable in which it is used

For continuous smoothing, the Poisson kernel is

\[
P_h(u)=\frac1\pi\frac{h}{u^2+h^2},\qquad
\widehat P_h(\xi)=e^{-h|\xi|}
\tag{6}
\]

with Fourier convention integral e^{-i xi u}P_h(u)du. It has a natural
connection with harmonic extension and resolvent estimates. It is an
alternative height window, with algebraic instead of Gaussian tails.
A Poisson distribution for zero counts would instead be an additional
probabilistic model; neither smoothing choice assumes that model.

There is a specific obstruction to replacing e^{-2|r|} by a bare Poisson
kernel in the auxiliary integral. Already one off-line reflected pair
has |F(r)|^2=4w_0^2 cosh^2(d(a+r)/2), which grows exponentially as
|r| tends to infinity when d>0. Its integral against P_b(r) diverges.
This excludes that undamped replacement only. Poisson smoothing in zero
height, damping, or a different resolvent observable are not excluded.

## 3. The exact heat convolution supplies the space-time scale

For Newman normalization partial_lambda H=-H_zz, reverse duration
s=lambda_*-lambda obeys the forward heat equation. For the complete
theta source and s>0,

\[
H_{\lambda_*-s}(z)=\frac1{\sqrt{4\pi s}}
\int_{\mathbb R}e^{-u^2/(4s)}H_{\lambda_*}(z+u)\,du.
\tag{7}
\]

This identity follows by inserting the source cosine transform and
integrating the Gaussian, which multiplies frequency q by e^{-s q^2}.
Superexponential source decay justifies Fubini at each fixed complex z
and finite time. The real displacement has variance 2s.

For zeta ordinate T, the mean spacing is

\[
\Delta(T)\sim\frac{2\pi}{\log(T/(2\pi))}.
\tag{8}
\]

The H-coordinate is x=2T, so its mean spacing is 2Delta(T). A height
window h(T)=m(T)Delta(T), with m fixed or slowly growing, suggests a
physical heat scale of order h(T)^2, up to this fixed factor of two in
space. Thus fixed m suggests log(T)^(-2); a mesoscopic m tending to
infinity pays m(T)^2 but averages more zeros. This is a scale calculation,
not a bound on zeros or on collision times. A positive Gaussian kernel
convolves a signed or complex field; absolute upper bounds alone do not
prevent the resulting field from vanishing.

The density in (8) is an averaged statement. It does not provide uniform
O(1) zero counts in every mean-spacing window, nor a bound on transverse
distance from the critical line. Those require additional information.

## 4. An explicit conditional bridge to collision time

Assume the manuscript's two-root tube persists from a positive double
collision at lambda_* to time zero, with its nonvanishing region and
simple labeling. Set u(s)=y(s)^2 and use the exact coefficient k(s).
Then

\[
u(s)=2\int_0^s
 \exp\left(-4\int_r^s k(q)\,dq\right)dr.
\tag{9}
\]

Suppose a canonical statistical estimate independently gives
y(lambda_*)<=D(T), and complete-path analysis gives, for every
0<=r<=lambda_*,

\[
\int_r^{\lambda_*}k(q)\,dq\le A(T).
\tag{10}
\]

Putting s=lambda_* in (9) proves

\[
\boxed{\lambda_*\le\tfrac12 e^{4A(T)}D(T)^2.}
\tag{11}
\]

In particular, D(T)<=C h(T) and A(T)<=A_0 would yield
lambda_*<=C^2 e^{4A_0}h(T)^2/2. This proves the implication precisely;
neither canonical hypothesis is obtained from a choice of smoothing width.
The final ordinate also has to be related to the event height by midpoint
control. A local zero-free-width estimate cannot be used as a global strip
estimate without the relevant spatial barrier or continuation argument.

One can instead use k<=K on the whole path. For K>0, (9) gives
u(lambda_*)>=(1-e^{-4K lambda_*})/(2K). If 2K D(T)^2<1, inversion gives

\[
\lambda_*\le
 -\frac{\log(1-2K D(T)^2)}{4K}.
\tag{12}
\]

For K=0 the bound is D(T)^2/2. If K<=kappa/h(T)^2 and D(T)<=C h(T),
the scale h(T)^2 follows from (12) only when 2kappa C^2<1. At or above
that threshold the displayed saturating lower bound supplies no finite
time bound. This makes explicit why density-scaled exterior forces cannot
be ignored when inferring a squared-spacing clock.

## 5. Existing height-dependent benchmark and earlier Gaussian work

Polymath, arXiv 1904.12438v2, Theorem 1.5, gives absolute C,c such that
for 0<t<=1/2, zeros with x>=exp(C/t) are real and lie near a regular grid;
the corresponding high-index disks each contain one simple zero. The
constants are uniform in t. Its proof is in Section 9. By taking a
sufficiently generous absolute constant to cover the disk/index threshold,
one obtains real/simple high zeros in a region of the form t>=C'/log x.
This already supplies a height-dependent positive-time benchmark of order
1/log x. A uniform log(x)^(-2) result would improve this scale and is not
implied just by smooth localization. No claim that this paper is the
latest or optimal bound is made.

Primary passages freshly inspected:
[Theorem 1.5 and Section 9](https://arxiv.org/html/1904.12438v2),
including the explicit uniformity of constants. The existing canonical
Polymath2019 bibliography record is reused. No new third-party PDF is
added to Git.

The repository already has an
[RH fixed-offset Gaussian theorem](../../../../../../papers/investigations-4/12_height_dependent_heat_contours/brainstorm/notes/18_RH_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_THEOREM_20261023.md)
and its
[internal review](../../../../../../papers/investigations-4/12_height_dependent_heat_contours/brainstorm/reviews/09_FIXED_OFFSET_GAUSSIAN_AND_CONTOUR_REVIEW_20261023.md).
The theorem controls H(-s,z)/(F(z)e^{s(F'/F)^2}) for s<=c/log^2 Y on a
fixed positive-offset strip, assuming initial RH. Its relative Gaussian
tail and complex-moment calculations are useful methodological inputs.
Initial RH, the fixed offset, negative Newman time and nonzero denominator
are material hypotheses; that result does not already give the required
unconditional shrinking-offset positive-collision estimate. Its all-multiple
control also prevents a simplicity inference from the coarse bounds alone.

## 6. Classification, controls and next question

Equations (2)–(7) are generic analytic identities/comparisons. Equations
(11)–(12) are conditional quantitative intermediate estimates with unproved
canonical inputs. A target D(T)=O(1/log T) is an asymptotic strip-narrowing
target, not a proof that every zero is on the critical line. A resulting
collision-time envelope tending to zero still leaves finite-height events
and event/cluster coverage to be addressed. No all-window vanishing
criterion is presented as a new restriction.

The polynomial pair has k=0 and attains lambda_*=d^2/2, so the transfer
constant is consistent. It does not satisfy theta arithmetic or an imposed
high-height D(T) bound. The smooth positive and reflected controls share
generic Gaussian/Gram positivity while lacking canonical square weights;
weighted-square controls lack complete reflection; Euler-factor controls
alter the canonical arithmetic. No selected arithmetic upper estimate has
yet been proved, and none of these controls is claimed to satisfy or fail
such an unstated estimate. See the
[result index](../../../../../../result-summaries/README.md),
[control cluster](../../../../../../result-summaries/12_collision_controls_and_screening.md),
[patterns index](../../../../../../avoid/README.md),
[target classification](../../../../../../avoid/01_restating_the_target.md),
[shape controls](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scope discipline](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

Recommended refinement: keep smooth compact localization as the exact
phase-control benchmark, examine a Gaussian height window and Gaussian
auxiliary minorant as the analytically explicit candidate, and write the
full local upper-bound/tail requirement in mean-spacing coordinates.
The central question is whether that canonical estimate can force
D(T)<=C h(T) with constants compatible with (11) or (12). Prefer a useful
proved mesoscopic range over an unsupported microscopic claim. A fixed
execution contract and Sol follow-through should be proposed only once
the observable, arithmetic route and completion test have been selected.

**Next: [B] TND-O-B03 — Astra:** select the Gaussian/bump window regime and
one independently accessible quantitative bound; retain the Poisson kernel
as a height-smoothing comparator. No new execution task is activated.

## Recording limits

This note is in the writable working checkout. The original checkout
remains unchanged. An incremental patch accompanies the note; the earlier
manuscript patch is preserved. Current thread
01a1b3e3-155c-7210-84b2-2bbe86a0d0d7 is still unregistered and its actual
source transcript is not exposed; history capture was skipped. No
registration, transcript or model metadata was fabricated. The reasoning
above has same-assistant analytical checking only.
