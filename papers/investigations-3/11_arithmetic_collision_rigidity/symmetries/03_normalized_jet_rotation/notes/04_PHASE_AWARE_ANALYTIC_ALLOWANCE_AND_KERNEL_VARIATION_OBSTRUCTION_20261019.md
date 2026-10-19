# S03-T2: analytic residual allowance and a kernel-variation obstruction

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**, verified from session metadata. Delegated same-model
mathematical analysis and a separate internal reviewer; no specialist
human review.

**Outcome.** On the fixed real pilot B, the complete residual increment
satisfies **`|I_r| < 0.812260`** using only the existing complete analytic
disk envelope, real symmetry and the explicit phase. Independent endpoint
radii from exactly those inputs pay `0.8274692795...`; the allowance
decreases by more than **1.8381%**. No new physical-source coefficients are
used. This is a reusable analytic-only estimate, the explicitly permitted
bounded branch of S03-T2. It does not explain the much stronger observed
arithmetic cancellation: the existing source-informed `0.000266448`
allowance remains the strongest retained residual bound.

A direct attempt at [Note 03's filtered functional][n03] is also screened:
keeping midpoint subtraction signed but paying parameter variation by
absolute shifted-channel kernel derivatives assigns **more than 4037.45136
to one existing spatial cell**. That payment rule fails decisively. This
is not a lower bound on the actual residual or on actual quadrature error.

The [result summaries][summaries] and [patterns to avoid][avoid] were read,
in particular [theta bookkeeping][theta], [collision controls][controls],
[target reformulations][a01], [scoped exclusions][a07] and [preserving
cancellation][a12]. Classification: **proved analytic-only bound with
outward-evaluated constants, plus a proved scoped payment obstruction**.
No physical sign, noncollision premise or unknown physical jet angle is
an input.

## Fixed object, information and metric

Keep B=`[1/100,1/5] x [999,1001]`, anchor `a=999`, full analytic
`f=(G_8-Chat_8)/A`, `Q=H/A`, `r=Q-f`, `omega=theta_x<0` and the
normalizer/branches of [S02-T2][s02]. The analytic cutoff stays 8. The
varying-center frozen family is not substituted for this single analytic
residual. All spatial derivatives hold time, contour and cutoffs fixed.

The primary metric is a uniform upper allowance for the **complete**
normalized increment

\[
 I_r(t,x)=\int_a^x e^{-i\theta}\omega
  \left(r+\frac{r_{xx}}{\omega^2}
          -\frac{\omega_xr_x}{\omega^3}\right)dy
 =i\{Z_r(t,x)-Z_r(t,a)\},\quad
 Z_r=e^{-i\theta}(r-i r_x/\omega).                         \tag{1}
\]

The equality is the exact previously proved primitive, not an estimate.
The new estimate below retains the relative phase of its two endpoints.
It neither loads nor evaluates the complete-source residual polynomial
from [Note 02][n02]. Thus its comparison class is **the imported complete
radius-1/2 analytic envelope plus real symmetry and explicit phase data**.
The complete theta approximation theorem supplies the envelope; the new
refinement is generic analytic geometry within that information class.

Use the full S02 matched bound
`eta < 0.226299245884` on the radius `R=1/2` disk about every real center
of B. Its arithmetic residual, correction continuation and all omitted
terms are already paid. The same inherited 32-by-128 closed rational
cover gives

\[
 \omega_* >1.0939342474342,\quad
 \Omega_* <1.0944720823929,\quad
 \Omega_{1,*}<0.000250248995215,                             \tag{2}
\]

where `omega_* <= |omega| <= Omega_*` and
`|omega_x| <= Omega_1,*`. The [new checker][checker] reconstructs these
whole-cell bounds, validates S02's producer/source pins and consumes the
192/256-bit matched complete envelope. Precision changes replay the
interval arithmetic, not the imported analytic theorem.

## Endpoint phase gives a smaller complete allowance

At any real center, let `u=r/eta` and `v=-r_x/(eta omega)`.
Real symmetry makes both coordinates real. Schwarz-Pick on the centered
disk implies

\[
 |u|\le1,\qquad |v|\le k(1-u^2),\quad
 k=(R|\omega|)^{-1}.
\]

Put `K=max(1,(R omega_*)^(-1))`. The jet lies in the fixed ellipse

\[
 E_K=\{(u,v):u^2+(v/K)^2\le1\},                            \tag{3}
\]

because `u^2+(1-u^2)^2<=1` on `[-1,1]`. In particular the usual
independent endpoint norm payment is `B_ind=2 eta K`.

Write `delta=|theta(t,x)-theta(t,a)|`. The support of `E_K` in a unit
direction `(cos phi,sin phi)` is
`h(phi)=sqrt(cos^2 phi+K^2 sin^2 phi)`. Rotation by the two known phases
in (1) gives a support sum `h(phi)+h(phi+delta)` for their difference
(the ellipse is centrally symmetric). Cauchy-Schwarz and the elementary
double-angle identity give, uniformly in the support direction,

\[
 (h(\phi)+h(\phi+\delta))^2
 \le2\{h(\phi)^2+h(\phi+\delta)^2\}
 \le2\{1+K^2+(K^2-1)|\cos\delta|\}.
\]

Taking the largest unit-direction projection proves

\[
 |I_r|\le B_{\rm ell}(\delta)
 :=\eta\sqrt{2\{1+K^2+(K^2-1)|\cos\delta|\}}.              \tag{4}
\]

No endpoint independence is assumed: allowing every pair of ellipse
members enlarges the admissible residual class. Unlike adding two
circumradii, (4) retains the known endpoint rotation. The absolute cosine
is essential once `delta>pi/2`.

Near the anchor, use the complete Cauchy defect estimate instead. With

\[
 D=1+\frac{2}{R^2\omega_*^2}
        +\frac{\Omega_{1,*}}{R\omega_*^3},
 \qquad |I_r|\le\eta D\delta,                              \tag{5}
\]

the second inequality follows by integrating in the monotone phase
coordinate. It uses `|r_x|<=eta/R`, `|r_xx|<=2eta/R^2` on every real
center; it does not assume an unforced heat equation for r.

Fix the single phase split `delta0=23/50`, without a grid search. The
whole path has `0<=delta<=2 Omega_* <2.188945<pi-delta0`. For
`delta<=delta0`, apply (5); for `delta>=delta0`, (4) has
`|cos delta|<=cos delta0`. Consequently

\[
 |I_r|\le\min\left(B_{\rm ind},\max\left\{
 \eta D\delta_0,
 \eta\sqrt{2[1+K^2+(K^2-1)\cos\delta_0]}\right\}\right).
                                                               \tag{6}
\]

The exact interval record gives the near allowance `<0.800040098` and
far allowance `<0.812259370`, hence the stated **`0.812260`** uniform
complete bound. The ratio to the same-input independent allowance is
`<0.981618762`. This compares certified upper allowances, not exact
suprema or the actual approximation error.

| Information and payment | Uniform complete increment allowance |
| --- | ---: |
| Same analytic-only inputs, independent endpoint radii | `<0.827470` |
| Same analytic-only inputs, phase-aware (6) | **`<0.812260`** |
| Additional complete-source inputs, independent endpoints (Note 02) | `<0.002011747` |
| Additional complete-source inputs, correlated prefix (Note 02) | `<0.000266448` |

The last two are separate information classes. The new allowance is not
the strongest existing error. No new anchor estimate, evaluated physical
consumer, matched cost gain or coverage follows merely from (6).

## What the envelope-only information cannot supply

The real entire residual `r(t,z)=1/5` lies in the uniform disk-envelope
class above. At the full endpoint,

\[
 |I_r(t,1001)|=\frac25
    \left|\sin\frac{\theta(t,1001)-\theta(t,999)}2\right|
 \ge\frac25\sin\omega_* >0.3553758.                       \tag{7}
\]

Here the phase half-gap lies in `[omega_*,Omega_*]`, contained in
`(0,pi/2)`, by (2). Thus an estimate valid for **every residual in this
envelope-only class** cannot reach either source-informed threshold.
This is not a lower bound for the actual theta residual. The constant
generally fails the fixed approximation's prescribed normalized heat
forcing and exact complete theta-source identity. Those premises remain
available to an arithmetic estimate. No optimality claim for (6) is made.

## A direct filtered-kernel variation rule fails

For a separate attempt at Note 03 (7), freeze its `d=pi/8-4log(1000)/1000`,
source cutoff `m=12`, and `U=2`. Write `P=e^(-i theta)/(A omega)`,
`zeta=u+id`, `q=i zeta-b`, `mu=omega_x/omega`,

\[
 K_+=e^{t\zeta^2+iy\zeta}\Phi_{<12}(\zeta),\qquad
 \Gamma_+=q^2-b_x-\mu q+\omega^2.
\]

On the real slice `K_- Gamma_-` is the conjugate of `K_+ Gamma_+`.
The retained source in the complete integrand is
`S=(1/2) int_0^2 P(K_+ Gamma_+ + K_- Gamma_-)du`.
The same external complex P multiplies both channels; it is not conjugated.
The complete contour identity precedes truncation. No reflection of a
finite source is assumed here.

Consider precisely a midpoint rule that evaluates the source/arithmetic/
correction **zero-order discrepancy together and signed**, but pays its
spatial variation with separate nonnegative source and approximation
derivative bounds. For the source it chooses

\[
 M_S(C)\ge\sup_{(t,y)\in C}\frac12\int_0^2
 \bigl(|\partial_y(PK_+\Gamma_+)|
       +|\partial_y(PK_-\Gamma_-)|\bigr)du.                 \tag{8}
\]

If remainders enter as independent complex error disks, the integrated
midpoint Lipschitz payment for a spatial cell of width h is
`h^2 M_S(C)/4`, before its other costs. This follows by integrating
`M_S|y-y_mid|`. It is a payment the method assigns, not the actual
midpoint quadrature error. Signed midpoint values cannot cancel that disk.

At fixed contour the product rule is

\[
 \partial_y(PK_+\Gamma_+)=PK_+B,\quad
 B=(q-i\omega-\mu)\Gamma_++\Gamma_{+,y},
\]
\[
 \Gamma_{+,y}=-2b_xq-b_{xx}-\mu_xq+\mu b_x+2\omega\omega_x,
 \qquad \mu_x=\omega_{xx}/\omega-\mu^2.                    \tag{9}
\]

The [independent elementary checker][kernelchecker] encloses the whole
closed source interval `59/100<=u<=3/5` at `t=21/200,y=1000`.
Reverse triangle on square 1 versus squares 2–11 gives
`|Phi_<12|>82.74632047`; also `|B|>1.41213364` and

\[
 |Pe^{t\zeta^2+i1000\zeta}|
 =\frac{e^{t(u^2-d^2)-1000d}}{A|\omega|}>113222501.
\]

These formulas avoid a wide oscillatory phase image. Integration over
width `1/100` with the full channel factor `1/2` proves
`M_S(C)>66149603` on a closed cell containing that point. The square
index here differs from the arithmetic Dirichlet index: this does not
contradict annihilation of arithmetic mode n=1.

The existing spatial cell `[63999/64,1000]` has `h=1/64`, so already

\[
             h^2M_S(C)/4 >4037.45136.                      \tag{10}
\]

This excludes **the separate-channel absolute-kernel derivative payment
(8) with independent remainder disks**, even after signed midpoint
recombination. The other cells, time variation, arithmetic/correction
evaluation and both physical tails only add costs in this rule. The
positive retained-kernel lower witness does not discard or estimate the
tails; their eventual payment cannot repair (10).

It does not exclude signed integration of differentiated kernels,
coefficientwise recombined Taylor models, endpoint primitives, different
contours or a uniform arithmetic mechanism. It bounds neither the signed
source derivative nor the complete functional from below. This differs
from Note 03's separate-prefix obstruction, which split the zero-order
source and approximation themselves.

## Complete error ledger, checks and decision

For (6), the imported eta already includes the complete arithmetic/source
residual, finite correction continuation, mode/contour tails and
normalization on every declared disk. Reconstructing its matched producer
pins is part of the checker. No extra source quadrature, source truncation,
Taylor truncation or cutoff transition is introduced. The fixed closed
cover pays phase variation and outward rounding throughout B, including
the anchor and partial final intervals through the uniform phase split.
Adding Note 03 (8)'s physical tails again to (6) would double count them:
that ledger belongs to a direct evaluation of its finite-source functional,
which this positive estimate does not perform.

Both new inequalities replay at 192/256 bits. A separate same-model
reader [reviews the proof and replays 192 bits][review]. The new allowance
helper is checked with its own polynomial-event disk allowance, an exact
oscillator, zero error, invalid inputs, a long-phase fallback and an
absolute-cosine mutation. At `H=x^2-2(t-tc)`, `A=1`, `theta=x`,
`f=2cos x`, anchor -1/event 0, the actual increment has modulus `sqrt(5)`
and cancels the exact H anchor; the paid helper rejects strict propagation.
The kernel checker compares (9) against independently differentiated
series at three source nodes; the written product rule, not sampling,
proves (9). Its lower inequality covers the whole source-u interval.

The [fresh source-specific controls][controlrecord] reject five event boxes
and the Euler negative-Laguerre witness using their own source errors.
They screen the unchanged downstream signed consumer; the new generic
upper-bound helper has the separate controls just described. The legacy
control producer retains source-version date 18 October; execution was
19 October. Finite-prime/weighted-square controls lack full normalized
theta reflection and unchanged coefficients; reflected/shape/primitive
controls lack the unchanged integer-square expansion; Euler controls alter
level-one data; generic polynomial/counter-kernel controls lack the theta
source. None receives theta's eta without a valid own-source bound.

**S03-T2 is Complete for its bounded analytic-only allowance and scoped
failed direct-estimate branch.** Its strict same-information allowance
gate passes. The arithmetic explanation sought by G3, a stronger
recombined estimate of Note 03 (7), and height-uniform residual control
remain open. S03-T3 can now compare the resulting fixed-box analytic
allowance and the retained stronger source-informed calibration with the
strongest direct consumer, including anchors and information costs.
S04-T3 still lacks a height-uniform input. EXT-01 remains conditional:
this result supplies no strongest-consumer or coverage advantage. The
real bridge `(1001,exp(2000))` and global complex exterior remain open.
No manuscript snapshot is created.

[n03]: 03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md
[n02]: 02_CORRELATED_ARITHMETIC_RESIDUAL_AND_PAID_TRANSPORT_20261018.md
[s02]: ../../02_cutoff_reflection/notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[checker]: ../numerics/check_phase_residual_allowance.py
[kernelchecker]: ../numerics/check_kernel_variation_obstruction.py
[review]: ../reviews/04_PHASE_ALLOWANCE_AND_KERNEL_OBSTRUCTION_INTERNAL_REVIEW_20261019.md
[controlrecord]: ../numerics/S03_T2_SOURCE_CONTROLS_20261019.json
