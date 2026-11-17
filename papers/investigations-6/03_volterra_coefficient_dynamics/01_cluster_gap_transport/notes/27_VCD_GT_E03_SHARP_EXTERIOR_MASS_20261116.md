# VCD-GT-E03 r6 — Sharp exterior weights and finite-count barriers

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. This helper inherits the session;
actual recorded model and reasoning effort are unavailable. No independent
backend attestation or specialist review is asserted.

**Proved in-note for the stated rectangular information class; proof-author
return pending separate internal assessment.** The exact joint weight
improves Note21's allowance. With its unchanged width-one and gap bounds,
nine additional zero occurrences cannot pay the old allowance, and four
cannot pay the sharp rectangular allowance. These are necessary-count
tests, not an acquired canonical exterior manifest or magnitude theorem.
[Decision08][decision] · [E03 r6 request][request] · [Result index][results] ·
[Controls12][controls] · [Avoid index][avoid], especially [01][class],
[02][screen], [07][scope] and [12][joint].

## 1. Fixed inputs, direction and classification

Keep the complete canonical physical heat field, the counted target pair,
and the definitions of [Note21][prior]. Its order-one product gives

\[
 -K=\sum_{\rho\ {\rm exterior}}
       \frac1{(z_1-\rho)(z_2-\rho)}.
\]

The sum is absolutely convergent. The paid radius-\(8/5\) disk and the
strip make every omitted conjugate group positive. For an exterior zero
\(\rho=c+x+iy\), the contribution per occurrence after conjugate grouping
is

\[
 q(x,y,D)=\frac{x^2-y^2-D}{(x^2-y^2-D)^2+4x^2y^2}.
 \tag{1}
\]

A nonreal conjugate pair contributes \(2q\), with multiplicities counted;
a real zero contributes \(q(x,0,D)\). The reflected target pair contributes
at least
\(\kappa_0=5000/1962848636289<3/10^9\).
The fixed slab is \(0\le t\le1/10\), centered at \(a=140101/10\),
with \(|c-a|\le7/100\), \(|D|\le d=1/5\) and
\(|\Im\rho|\le\delta(t)=\sqrt{1-2t}\le1\).
[Note22][geometry] pays the geometry independently of the old measured
\(K\) and early gap positivity. Neither is used below.

For each selected disjoint conjugation-invariant exterior multiset,
excluding the target and its separately retained reflection, suppose its
count \(n_j\) and ranges \(L_j\le|x|\le U_j\) are paid on every slice.
Then

\[
 -K\ge\kappa_0+\sum_j n_j\mu(L_j,U_j;\delta,d),\qquad
 \mu=\inf_{\substack{L\le|x|\le U\\|y|\le\delta,\ |D|\le d}}q(x,y,D).
 \tag{2}
\]

The target is that the right side be at least \(59/100\).
Equation (2) is a local sufficient estimate from the previously established
divisor formula. This execution's gain is the exact finite-corner formula
and quantified acquisition-size exclusions below, not another global
reformulation or a new reality test. An actual selected divisor occupies
a smaller, possibly correlated feasible set; rectangular optimality does
not assert optimality for that divisor.

## 2. Exact rectangular minimum

**Proposition.** Let \(0\le\delta,d\), \(0<L\le U\) and
\(L^2>\delta^2+d\). Then

\[
 \boxed{\quad
 \mu(L,U;\delta,d)=
 \min_{\substack{r\in\{L,U\}\\e\in\{-d,d\}}}
 \frac{r^2-\delta^2-e}
 {(r^2-\delta^2-e)^2+4r^2\delta^2}.
 \quad} \tag{3}
\]

**Proof.** Set \(s=x^2\), \(u=y^2\), \(v=s-u-D>0\), and
\(f=v/(v^2+4su)\). The denominator is positive throughout the rectangle.
Differentiating with respect to \(u\), with \(s,D\) fixed, gives

\[
 \partial_u f=
 \frac{v^2-4s(s-D)}{(v^2+4su)^2}<0.
 \tag{4}
\]

Indeed \(0<v\le s-D\), and its numerator is at most
\(-(s-D)(3s+D)<0\), since \(s>d\ge|D|\).
Thus the minimum uses \(u=\delta^2\).

For fixed \(s,u\), regard \(f\) as a function of \(v\):

\[
 \frac{d}{dv}\frac{v}{v^2+4su}
   =\frac{4su-v^2}{(v^2+4su)^2}.
\]

On a positive interval this derivative either has constant sign or changes
from positive to negative. Hence there is no interior minimum, and the
minimum over \(D\in[-d,d]\) is at an endpoint. For each such endpoint,

\[
 \partial_s f=
 \frac{4u(u+D)-v^2}{(v^2+4su)^2}.
 \tag{5}
\]

Its numerator decreases strictly with \(s\), since \(v>0\), so again
there is no interior minimum. The endpoints are \(s=L^2,U^2\), proving
(3). The argument includes \(\delta=0\), \(d=0\) and \(L=U\), with
coincident corners interpreted once. Both signs of \(D\) were retained.

The old weight

\[
 m(L,U)=\frac{L^2-\delta^2-d}
 {(U^2+\delta^2+d)^2+4U^2\delta^2}
\]

is a valid lower bound for every point of this same rectangle. Consequently
\(\mu\ge m\). This comparison follows from their proved directions,
without an assumption that the improvement is strict on every rectangle.

## 3. Exact optimal weights at the frozen initial width

Fix \(\delta=1,d=1/5\), and write \(h=1+d=6/5\).

**Old allowance.** Increasing \(U\) with \(L\) fixed increases its
denominator. Therefore its largest possible per-occurrence value is found
among \(L=U=\sqrt s\), \(s>h\). Put \(r=s-h>0\); then

\[
 m(\sqrt s,\sqrt s)
 =\frac{r}{r^2+4(h+1)r+4h(h+1)}.
\]

Its derivative has the sign of \(4h(h+1)-r^2\), so the unique maximum is
at \(r=2\sqrt{h(h+1)}\), with value

\[
 M_{\rm old}=\frac1{4(h+1+\sqrt{h(h+1)})}
             =\frac5{44+4\sqrt{66}}
             =0.0653627635310009\ldots.
 \tag{6}
\]

**Sharp rectangular allowance.** At any allowed horizontal location,
the rectangle contains the corner \(y=1,D=d\). Thus

\[
 \mu(L,U;1,1/5)\le\sup_{s>h}
          \frac{s-h}{(s-h)^2+4s}.
\]

With \(r=s-h\), the derivative of \(r/(r^2+4r+4h)\) has the sign
of \(4h-r^2\). Its maximum occurs at \(s_*=h+2\sqrt h\), and equals

\[
 M_{\rm sharp}=\frac1{4(1+\sqrt h)}
             =0.1193063937629153\ldots.
 \tag{7}
\]

This upper cap on the available lower weight is attained by the
degenerate horizontal rectangle \(L=U=\sqrt{s_*}\). To check the other
\(D\) endpoint, let \(v=s_*-1-d=2\sqrt h\). At \(D=-d\), the
numerator variable is \(v+2d\), and

\[
 \frac{v+2d}{(v+2d)^2+4s_*}
 -\frac{v}{v^2+4s_*}
 =\frac{2d\,[4s_*-v(v+2d)]}
 {((v+2d)^2+4s_*)(v^2+4s_*)}>0,
\]

because \(4s_*-v(v+2d)=4\sqrt h(2-d)>0\).
The \(D=d\) corner is therefore the smaller one, and (3) proves
attainment of (7).

Here **a degenerate horizontal rectangle is not a count-one
conjugation-invariant zero region**. Rectangular sharpness permits
\(y=\pm1\); such nonreal zero occurrences must appear in conjugate pairs
when they belong to an actual real entire divisor. No canonical placement,
multiplicity or physical heat evolution attaining either optimum is claimed.

## 4. Count-budget failures, with strict rational checks

Let \(N=\sum_j n_j\) count all additional selected occurrences, excluding
the target and reflected pair. For the old allowance, \(N\le9\) implies

\[
 \kappa_0+\sum_j n_jm(L_j,U_j)
 \le\kappa_0+9M_{\rm old}<\frac{59}{100}.
 \tag{8}
\]

An exact rational check is available without trusting decimal rounding:
\((2031/250)^2<66\), so \(M_{\rm old}<625/9562\). Therefore

\[
 \frac{59}{100}-\left(\frac3{10^9}+\frac{5625}{9562}\right)
 =\frac{8289985657}{4781000000000}>0.
 \tag{9}
\]

The exact radical value gives
\(9M_{\rm old}=0.5882648717790081\ldots\); (9) is the strict proof,
not that rounded display. Thus **at least ten additional occurrences are
necessary for this old allowance**.

For the sharp rectangular allowance, \(N\le4\) gives

\[
 \kappa_0+\sum_jn_j\mu_j
 \le\kappa_0+4M_{\rm sharp}
 <\frac3{10^9}+\frac12<\frac{59}{100},
 \tag{10}
\]

using \(\sqrt{6/5}>1\). Hence **at least five additional occurrences
are necessary for this sharp rectangular allowance**. Its abstract
five-occurrence cap exceeds the target: since \(\sqrt{6/5}<11/10\),

\[
 5M_{\rm sharp}>\frac{25}{42}>\frac{59}{100}.
 \tag{11}
\]

This does not show five actual occurrences suffice. Their independently
paid locations, count parity, multiplicities, shared \(D\), and time
evolution still constrain the feasible weights. Widely separated groups
usually have unequal and smaller weights. No candidate manifest is created
by the necessary count thresholds.

These failures apply to the **displayed mirror-plus-selected-groups
allowances with the fixed rectangular bounds**. They are not upper bounds
on the actual total exterior mass: all omitted groups remain favorable and
may contribute substantially. They do not apply unchanged to narrower
vertical bounds, real selected zeros, or stronger correlated information.
For a uniform full-slab target, contraction of the strip at later times
cannot remove the \(t=0\) width-one test. Sharper independently paid
\(D(0)\) or other endpoint information changes the rectangle and is a
different allowance.

## 5. A count-one region supplies extra reality information

Suppose a selected exterior region is invariant under conjugation,
has zero-free boundary, and contains exactly one zero **counted with
multiplicity** on every slice. Conjugation gives equal multiplicity at
conjugate zeros. A nonreal zero would therefore give at least two
occurrences; a repeated real zero would also give at least two. The unique
zero is real and simple on each slice, without choosing a label through
a collision. If \(|x|\le U\), \(|D|\le d\), and the exterior separation
ensures \(x^2>D\), its contribution satisfies

\[
 q(x,0,D)=\frac1{x^2-D}\ge\frac1{U^2+d}.
 \tag{12}
\]

This can improve (3) because the count has paid \(y=0\). Only the selected
zero is proved real; the remainder continues to use Note21's strip and
conjugate grouping. A region containing one conjugate pair has count two
and does not meet this premise. No such exterior singleton count has been
acquired in this branch. The radius-\(8/5\) certificate counts only the
target pair, so it supplies none of the additional occurrences in (8)–(12).

## 6. Controls and same-information comparison

The full premise audit in [Note21 §6][premise-table] is inherited, with the
following explicit consequences for this estimate. These are analytical
screens; no old control certificates or canonical source arrays were rerun.

| Control family | Shared, failed or untested premise for the present claim |
| --- | --- |
| Exact even quartic in Note21 | Shares order, strip, geometry and the physical heat equation; its only exterior group is the reflection, so it has no additional selected mass. It collides and fails the strict passage budget. Equations (3), (8) and (10) remain valid. |
| Earlier nonzero Gaussian-factor controls | Fail the order-at-most-one premise; the quadratic exponential supplies a curvature term absent from the divisor formula. The earlier shifted quadratic also lacks the global reflected pair. |
| Euler-factor translates | Share order and the real even physical heat field. Initial extra zeros fail width one when their offset exceeds one; otherwise strip contraction applies. This tube's enlarged count, additional groups and useful mass remain untested. |
| Three/four weighted-square controls | Share real even physical heat and order one. Their nonzero odd endpoint defect makes zeros escape every horizontal strip in the documented class. Finite endpoint matching does not pay the strip. |
| Finite-source measurement and canonical-score controls | The specified nonzero finite positive changes share order and physical heat but fail a global finite strip by the endpoint/growth proof; finite measurement agreement does not change that conclusion. |
| Finite-prime orbit controls | The documented bounded positive orbit changes have the same endpoint-based strip failure; their high-gap events do not supply this prescribed tube or selected counts. |
| Reflected super-Gaussian | Shares a real even physical heat field but fails order at most one; its positive super-Gaussian component gives super-order-one growth. |
| Damped smooth-shape and positive-primitive controls | Share the stated order bound and physical heat field; a common strip, enlarged target-only disk and usable additional mass are untested. Their undamped Gaussian precursor instead fails order one. |
| Reflection rigidity / four-family comparison | The normalized reflection-plus-square-comb conjunction identifies theta within the specified coefficient class. It supplies no new quantitative selected-group count; the distinct family failures are those above. |
| BW-01 and finite-profile threshold controls | Compact or finite-atomic sources give order at most one and physical heat; their threshold-time reality does not establish this earlier slab's strip, local count or mass budget. |
| RH-conditional normalized endpoint merger | Retains its RH hypothesis and shares the relevant order/strip in that conditional setting. Remote added doubles do not pay this tube's selected groups; a qualifying tube beginning at an added double has zero exact passage margin. |
| Changed observation kernel | Does not inherit the literal cosine/Newman equation or this field's counted divisor. |
| Actual-theta fractional-profile relaxation | Does not furnish the multiplicity-counted integer divisor needed in (1)–(2). |
| Five-atom double control in Note24 | Shares positive weights, reflection, order one and a physical atomic heat embedding; fails width one since its extra zeros have height \(\operatorname{arcosh}2>1\). Its negative deflated numerator does not refute (2)–(3). |
| Four-atom undeflated-Laguerre control in Note24 | Its positive undeflated expression is not the premise in (2). It has zeros with \(\cos z=(-9-\sqrt{89})/4<-4\), hence imaginary height greater than one, and fails the frozen strip at that slice. No selected-group count or useful deflated mass is supplied. |

Source equality alone is not used to declare a control rejected by a new
quantitative inequality. Any changed field satisfying the divisor, strip,
count and range premises obeys the same bound. A collision control can
satisfy the structural estimate while failing the strict incoming-cost
premise required for passage.

The direct method receives all shared source values, strip, geometry,
count/range information and any future singleton counts. Its already
established interval minimum is the early endpoint, as in [Note19][minimum].
This proof pass neither tightens that endpoint enclosure nor establishes an
evaluation-cost advantage. It stops the nine-occurrence old allowance and
four-occurrence sharp allowance before acquisition. A future request still
needs literal exterior groups, an independent full-time count method,
plausible sufficient total lower mass, and a bounded acquisition contract.

[decision]: ../brainstorm/notes/08_VCD_GT_B06_SHARP_MASS_FEASIBILITY_DECISION_20261116.md
[request]: ../research-progress/handoffs/VCD-GT-E03-r6.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[class]: ../../../../../avoid/01_restating_the_target.md
[screen]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[prior]: 21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md
[geometry]: 22_VCD_GT_E04_JOINT_STRIP_GEOMETRY_20261116.md
[premise-table]: 21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md#6-screening-the-used-premises
[minimum]: 19_VCD_GT_E03_MATCHED_GAP_MINIMUM_20261116.md
