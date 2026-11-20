# AGC-E13: centered log-disk and coupled discriminant allowance

19 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI
Codex LLM assistance. Helper explicitly dispatched **gpt-6.1-sol / ultra**;
independent backend/effort attestation was unavailable to this helper.

Status: **proved in-note**, one derivation plus one author correction pass;
separate helper assessment required before acceptance. This is an analytic
constant improvement of the stated complete discriminant allowance at fixed
information. No new arithmetic source error, canonical count, zero coverage,
cost measurement or numerical certificate is acquired.

Inputs: [E13 r1](../research-progress/handoffs/AGC-E13-r1-request.md),
[B02 decision](../brainstorm/notes/03_AGC_B02_LOG_DISK_REFINEMENT_20261119.md),
[frozen B01](../brainstorm/notes/02_AGC_B01_FIXED_CELL_COMPARISON_20261119.md),
[E10 Note 04](04_AGC_E10_CONTOUR_ENDPOINT_20261119.md), and manuscript
[Sections 5](../manuscript/sections/05_arithmetic_source.tex),
[6](../manuscript/sections/06_residual_transport.tex) and
[7](../manuscript/sections/07_program.tex).

## 1. Classification, prior work and hypotheses

The [result index](../../../../result-summaries/README.md) and
[patterns index](../../../../avoid/README.md) apply. Relevant routes are
[Cluster 18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[collision controls 12](../../../../result-summaries/12_collision_controls_and_screening.md),
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../avoid/08_normalization_and_constant_slips.md) and
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Classification: a **finite conditional estimator refinement**, not an
RH-equivalent criterion. Its milestone is the strict constant comparison
below, not the existence of another representation.

The parent's [Note 52](../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/notes/52_VCD_GT_CM_JOINT_ANNULAR_ALIAS_DECISION_20261118.md)
and [manuscript Section 22](../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/manuscript/sections/22_correlated_enclosures.tex)
already retain a common logarithm with Parseval for annular quadrature
aliases. Here the input is instead the full value-error disk. No novelty
claim is made for logarithm geometry, Bessel's inequality or Parseval.

Keep B01's physical $P=P_N$, unchanged $H$, $R=P_t+P_{zz}$ and
$u=t_*-t$, so $E=H-P$ satisfies $E_u=E_{zz}+R$. Keep the fixed circle
$\Gamma:|z-X|=r$, $r<\min(A,h)$, inside its right-half-plane rectangle,
with the fixed-cutoff inequalities in B01. Nothing below assumes that
$c_P=X$, moves the contour to $c_P$, changes the source or uses a
correction center.

At the slice under consideration require:

1. $H,P$ holomorphic on a neighborhood of the closed disk; $P$ nonzero
   on $\Gamma$ with **exactly two** interior zeros counted with integer
   multiplicity.
2. A complete paid value enclosure $|E/P|\le q<1$ on $\Gamma$, for
   example from $|E|\le\varepsilon<m\le|P|$. All source, tail, boundary
   and arithmetic errors used for $\varepsilon,m$ are included.
3. The inherited contour moments and their numerical evaluation, if any,
   use this same reference, circle and count. Their quadrature and
   reference-coordinate uncertainties are paid separately.

The strict bound extends to some collar with a possibly larger bound
still below one. Hence $H$ is nonzero on the circle, Rouché gives its
count two, and the power-series branch
$\ell=\log(1+E/P)$ is single-valued on that collar. Only the original
bound $q$ on the circle is used for the constants below. No logarithm
through the interior zeros is needed.

The slice estimates need no heat equation. To apply the full time identity
or to claim a protected path, impose these gates at **every** time, with
the $C^1$ time/holomorphic spatial regularity and unchanged equations
specified in Note 04. Real gap protection additionally requires the
physical conjugation symmetry. The allowance itself permits a complex
center.

## 2. The optimal containing disk for the logarithm image

For $0\le q<1$ put

\[
\kappa=\frac12\log(1-q^2),\qquad
\eta=\operatorname{atanh}q=\frac12\log\frac{1+q}{1-q},\qquad
\lambda=-\log(1-q).
\]

Then, for the principal logarithm,

\[
\boxed{\left|\log(1+w)-\kappa\right|\le\eta
\quad\text{whenever } |w|\le q.} \tag{1}
\]

For $q=0$ this is immediate. Suppose $q>0$, set
$a=\sqrt{1-q^2}=e^\kappa$, and normalize $v=(1+w)/a$.
The disk for $v$ has center $1/a=\cosh\eta$ and radius
$q/a=\sinh\eta$. It lies in $\Re v>0$, with real endpoints
$e^{-\eta},e^\eta$. Its defining inequality is

\[
|v|^2+1\le2\cosh\eta\,\Re v.
\]

Set $\rho=\tanh(\eta/2)$ and $\xi=(v-1)/(v+1)$. Since
$\cosh\eta=(1+\rho^2)/(1-\rho^2)$, the last inequality is exactly
$|\xi|\le\rho<1$. On this disk,

\[
\log v=2\operatorname{atanh}\xi
=2\sum_{n\ge0}\frac{\xi^{2n+1}}{2n+1}.
\]

The series branch agrees with the principal logarithm in the right
half-plane. Therefore

\[
|\log(1+w)-\kappa|
=|\log v|
\le2\operatorname{atanh}|\xi|
\le2\operatorname{atanh}\rho=\eta,
\]

proving (1). The two real inputs $w=\pm q$ attain $\pm\eta$ after
centering. Thus any disk containing this logarithm image has radius at
least $\eta$, and (1) supplies a minimum-radius disk, centered at
$\kappa$. This is an optimal *containing disk*, not a claim that the
logarithm image fills the disk.

Constants integrate to zero in both inherited contour moments. Removing
$\kappa$ therefore costs no center or discriminant term. For $0<q<1$,

\[
0<\eta<\lambda,\qquad
\lambda-\eta=-\kappa=-\tfrac12\log(1-q^2)>0. \tag{2}
\]

## 3. Coupled negative modes retain the complete square

Parametrize the unchanged circle by $z=X+re^{i\theta}$ and put
$f(\theta)=\ell(X+re^{i\theta})-\kappa$. Define its two negative
Fourier coefficients by

\[
a_1=\frac1{2\pi}\int_0^{2\pi}f(\theta)e^{i\theta}\,d\theta,\qquad
a_2=\frac1{2\pi}\int_0^{2\pi}f(\theta)e^{2i\theta}\,d\theta.
\]

The contour logarithm is continuous, so these integrals and Bessel's
inequality apply. Orthogonality and (1) give the common constraint

\[
\boxed{|a_1|^2+|a_2|^2
\le\frac1{2\pi}\int_0^{2\pi}|f(\theta)|^2\,d\theta
\le\eta^2.} \tag{3}
\]

No assumption that only two Fourier modes are present is made.
For the inherited moments of Note 04,

\[
I_0=\frac1{2\pi i}\oint\ell\,dz=ra_1,\qquad
I_1=\frac1{2\pi i}\oint(z-c_P)\ell\,dz
=r^2a_2+(X-c_P)ra_1.
\]

Consequently the **full** discriminant error, including the center square,
is

\[
\boxed{\Delta D:=D_H-D_P
=-r^2a_2+(c_P-X)ra_1-\frac{r^2a_1^2}{4}.} \tag{4}
\]

This reuses manuscript Section 7's endpoint identity. In particular the
last term is the complex square $a_1^2$, not $|a_1|^2$ in the identity.
Its absolute contribution is paid in the allowance below.

Set

\[
\zeta=\frac{c_P-X}{r},\qquad d=|\zeta|,\qquad
F(\eta,d)=\max_{0\le x\le\eta}
\left\{\sqrt{\eta^2-x^2}+dx+\frac{x^2}{4}\right\},\qquad
F(0,d)=0.
\]

Then (3)–(4), with $x=|a_1|$, prove

\[
\boxed{|\Delta D|\le B_{\rm joint}:=r^2F(\eta,d).} \tag{5}
\]

The maximum exists on a compact interval. It is also the **exact maximum
for the abstract two-coefficient ball (3)**. For $d>0$, write
$\zeta=de^{i\phi}$ and choose
$a_1=-xe^{i\phi}$,
$a_2=\sqrt{\eta^2-x^2}\,e^{2i\phi}$. All three terms in
$-a_2+\zeta a_1-a_1^2/4$ then have the same phase. For $d=0$ use
any $\phi$. This proves attainment at every scalar $x$, including the
maximizer.

The abstract ball relaxes the actual pointwise logarithm-image constraint,
analyticity, count and physical source conditions. Thus this exact
coefficient-ball maximum is **not** claimed sharp for the full
$|E/P|\le q$ class or for theta. Its use as an upper allowance is valid
without realizability of its maximizers.

## 4. Centered maximum, general offset and large eta

For $d=0$ put $y=\sqrt{\eta^2-x^2}\in[0,\eta]$. The objective is

\[
y+\frac{\eta^2-y^2}{4}
=1+\frac{\eta^2}{4}-\frac{(y-2)^2}{4}.
\]

Therefore

\[
\boxed{
F(\eta,0)=
\begin{cases}
\eta,&0\le\eta\le2,\\
1+\eta^2/4,&\eta\ge2.
\end{cases}} \tag{6}
\]

For $\eta\le2$ the maximizing $a_1$ has magnitude zero. For $\eta>2$
it has magnitude $\sqrt{\eta^2-4}$. The formula $F=\eta$ must not be
continued beyond $\eta=2$.

For every $d\ge0$ and $\eta\ge0$, Cauchy–Schwarz gives

\[
\sqrt{\eta^2-x^2}+dx\le\eta\sqrt{1+d^2},
\]

and hence the explicit general-offset bound

\[
\boxed{F(\eta,d)\le
U_{\rm C}(\eta,d):=\eta\sqrt{1+d^2}+\eta^2/4.} \tag{7}
\]

When $0<\eta<2$, concavity of the square root gives
$\sqrt{\eta^2-x^2}\le\eta-x^2/(2\eta)$. Completing the square, with
no restriction on the unconstrained maximizing $x$, gives

\[
\begin{aligned}
\sqrt{\eta^2-x^2}+dx+x^2/4
&\le\eta+dx-\frac{2-\eta}{4\eta}x^2\\
&\le\eta+\frac{\eta d^2}{2-\eta}.
\end{aligned}
\]

Thus a second explicit bound is

\[
\boxed{F(\eta,d)\le
U_{\rm P}(\eta,d):=\eta+\frac{\eta d^2}{2-\eta},
\qquad0<\eta<2.} \tag{8}
\]

The best of (7) and (8) is available without scalar optimization. The
exact scalar maximum (5) is no larger than either upper bound; it may
be used when rigorously evaluated. At $\eta=0$ use zero. At
$\eta=2$ or $\eta>2$ use (5) or (7); (8) is not applicable. For a
centered circle (6) evaluates (5) even when $\eta>2$.

These bounds include general complex $c_P$ through $d$ and retain the
fixed center $X$. If the reference center is enclosed rather than known,
a paid upper bound on $|c_P-X|/r$ is sufficient: the objective and both
upper bounds are nondecreasing in $d$. A paid upper bound for $q$
likewise gives a valid $\eta$, since the coefficient balls are nested.
For a count-two reference in the disk, convexity also gives $d<1$,
but no such simplification was needed in the proof.

## 5. Strict comparison with both inherited baselines

The strongest allowance explicitly proved in E10 Note 04 is

\[
B_{\rm E10}=r^2\left\{\lambda\sqrt{1+d^2}+\frac{\lambda^2}{4}\right\}.
\]

It already improves on the earlier independent-moment sum

\[
B_{\rm sep}=r^2\left\{(1+d)\lambda+\frac{\lambda^2}{4}\right\},
\qquad B_{\rm E10}\le B_{\rm sep}.
\]

For **every** $0<q<1$, $r>0$ and $d\ge0$, (2), (5) and (7) yield

\[
\boxed{
B_{\rm joint}
\le r^2U_{\rm C}(\eta,d)
<B_{\rm E10}
\le B_{\rm sep}.} \tag{9}
\]

The middle inequality is strict because
$s\sqrt{1+d^2}+s^2/4$ is strictly increasing for $s\ge0$ and
$\eta<\lambda$. This already proves a strict improvement at the same
$q$, circle, reference center and count for all offsets and all
$\eta>0$. Using (8) or the exact maximum can improve it further.
For $q=0$ all three allowances vanish, as they must.

This is a comparison of **complete discriminant-transfer allowances**:
the shared center contribution and full nonlinear square have both
been included. If an identical finite additive allowance $C$ pays
reference evaluation, quadrature or other unchanged errors on both
sides, then $C+B_{\rm joint}<C+B_{\rm E10}$ still holds. It supplies
no missing $C$, source norm, denominator floor, reference gap or count.
It does not assert the actual discriminant error is reduced, or
that either allowance is sharp for the full source class.

For the requested finite comparison, take the theorem subcase
$q=1/2$, $c_P=X$. Then

\[
\eta=\tfrac12\log3<2,\quad\lambda=\log2,\quad
B_{\rm joint}=\tfrac12r^2\log3,\quad
B_{\rm E10}=B_{\rm sep}
=r^2\left(\log2+\frac{(\log2)^2}{4}\right). \tag{10}
\]

There is even an elementary exact rational factor comparison:

\[
\boxed{B_{\rm joint}<\frac{17}{25}B_{\rm E10},} \tag{11}
\]

so this complete allowance is reduced by **more than 32 percent**.
No floating calculation is needed. Indeed the positive
$\operatorname{atanh}$ series gives

\[
\log2
>2\left(\frac13+\frac{1}{3\cdot3^3}\right)
=\frac{56}{81}>\frac{69}{100}.
\]

For $\eta=\operatorname{atanh}(1/2)$, bounding the denominators in
the tail strictly by their first value gives

\[
\eta
=\frac12+\frac1{24}+
\sum_{n\ge2}\frac{(1/2)^{2n+1}}{2n+1}
<\frac12+\frac1{24}+\frac15
\sum_{n\ge2}(1/2)^{2n+1}
=\frac{11}{20}.
\]

Thus

\[
\frac{17}{25}
\left(\log2+\frac{(\log2)^2}{4}\right)
>\frac{17}{25}\frac{32361}{40000}
=\frac{550137}{1000000}
>\frac{11}{20}>\tfrac12\log3,
\]

which proves (11). These are symbolic allowance constants, not acquired
theta values. A centered special case at one slice does not authorize
recentering the frozen circle or assert $c_P(u)=X$ along the cell.

## 6. Direct/transport scope and collision controls

Note 04 proves that on every identical exact admissible path,

\[
\Delta D(u)=\Delta D(0)-\int_0^u K(v)\,dv
=-I_1(u)-I_0(u)^2/4,
\]

where $K$ includes the joint quotient, center difference and reference
defect. Hence exact extrema of these readouts over an identical full
admissible path set agree. **The exact full transport functional cannot
beat the direct functional on that identical set.** The improved allowance
(5) is equally available to the direct endpoint comparator and to full
transport. It refines their shared estimator, without separating their
underlying exact information.

This statement does not compare the cost of acquiring data or exclude
time-correlated estimates, boundary/heat acquisition, better anchors,
signed readouts, or tighter feasible sets from additional observations.
Those data must be passed to both comparators. No universal inequality
between a slice-only value box and a transport relaxation retaining
extra temporal information is asserted.

For real-gap continuation, at every time require all gates of §1 and a
complete strict margin

\[
D_P(u)-C(u)-r^2F(\eta(u),d(u))>0. \tag{12}
\]

An endpoint margin alone is insufficient. The sign of $D_P$ is not an
output of the logarithm geometry.

The quadratic control from Note 04 has
$H=P=(z-X)^2+2(u-U)$, $0<U<r^2/2$. It satisfies $E=R=0$,
$q=\eta=0$, count two and contour clearance, while
$D_H=D_P=2(U-u)$ reaches zero at the event. The new allowance remains
zero; the failed premise is the strict reference margin (12), not any
approximation estimate. The refinement therefore preserves this collision.

The detailed Cluster 12 premise screen in Note 04 §7 carries over
unchanged, since only the allowance for the same error disk has been
refined. In particular:

| Relevant control class | Quantitative or structural premise that is not supplied |
| --- | --- |
| Euler-factor; weighted-square; reflected super-Gaussian; smooth-shape and positive-primitive controls | Preserved positivity, reflection, support or endpoint properties do not acquire (12). At any count-two isolated collision, a valid allowance cannot make it strict. |
| Finite-source measurements and finite-prime orbit controls | Finite matching and small source distance do not supply the time-uniform height-dependent strict margin; it fails at the local double event. Documented finite-square controls also lack a global all-real anchor. |
| Atomic, fixed-event and finite-profile threshold controls | Finite profiles and upper moments do not provide (12). Count two must be separately acquired when other events or zero occurrences are present. |
| RH-conditional normalized endpoint controls | A fixed positive source tolerance is not the required height-dependent margin at escaping time-zero doubles; the construction's RH assumption and endpoint location do not refute an unconditional positive-time fixed-cell theorem. |
| Fixed amplitude with changed observation kernel | The unchanged physical heat equation fails unless the nonzero prepared forcing is retained. Zero raw mismatch is not the complete source payment. |

More formally, at a counted double event $D_H=0$. Any valid transfer
bound gives $D_P\le|D_P|=|\Delta D|\le C+B_{\rm joint}$, so (12)
cannot hold there. If a collision cannot be enclosed with count two,
that acquisition gate fails instead; no conclusion is imported from a
larger or fractional divisor. Reflection rigidity is not a collision
witness, and static divisor surgery supplies no common heat path.
Literal changed arithmetic is not used as a substitute for naming
the missing quantitative margin.

The exclusion just stated is confined to the displayed local allowance
and physical-path hypotheses. It is not an obstruction to estimates
using the unchanged complete theta source or to new temporal acquisition.

## 7. Correction record and next action

One proof and one author correction pass were used. The correction pass
checked branch consistency in the Cayley normalization; Fourier signs
and radius factors in (3)–(4); attainability only for the abstract
coefficient ball; the $\eta=0,2$ and $\eta>2$ cases; the unconstrained
completion of the square in (8); comparison against E10's stronger
square-root baseline as well as the earlier sum; and the exact rational
factor in (11). No numerical campaign was performed.

Separate helper assessment must check this note before acceptance.
The next canonical step remains acquisition of the frozen source value
budget, contour/count/denominator/reference-gap inputs and complete
all-time errors; the refined constant alone does not supply any of them.
