# VCD-GT-E17 r1 — Center-averaged transverse correction

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded executor dispatch was
**gpt-6.1-sol / ultra**. Independently exposed serving-model and actual
effort metadata were unavailable to the executor.

**Proved in-note, pending separate E18 internal assessment.** This is the
fixed analytical execution of [B09 Decision17][decision] under
[E17 r1][request]. It is a quantitative intermediate estimate whose gain
is two powers of the collar parameter in an unconditioned center average.
The selected-pair application uses a separate collar premise.
[Result index][results] · [Controls12][controls] · [Avoid index][avoid] ·
[Classification01][class] · [Premises02][premises] · [Scope07][scope]

## 1. Complete canonical inputs and statement

Use the complete canonical \(H_t\), with \(H_0(z)=\xi((1+iz)/2)/8\)
and \(\partial_tH_t=-H_{zz}\). All zero sums count integer
multiplicities, including nonreal zeros. Fix \(0\le t\le1/2\), \(T\ge16\),
\(L=\log T\), \(\ell=1/L\), \(1\le a\le L\), and \(3\le R\le T/2\).
The scale \(\ell\) is fixed across the band \([T,2T]\). For arbitrary
real centers \(X\) in that band, define
\[
 \Xi_{a,R}(t,X)=\ell^2
 \sum_{\substack{\rho:\,|\rho-X|\ge a\ell\\|\Re\rho-X|\le R}}
       \frac{(\Im\rho)^2}{|\rho-X|^4}.
\]
The imported canonical bound, [TND-O Note21, (8)][moment], is
\[
 W_t(U):=\sum_{U\le\Re\rho\le2U}(\Im\rho)^2
 \le C_b\frac{U}{\log U}\qquad(U\ge8,\ 0\le t\le1/2)
 \tag{1}
\]
with one fixed \(0<b<1/2\), \(C_b=2B_b/b^2\), and closed endpoints.
The proof in that note uses canonical time-zero density and complete
convex broad-window heat transport. [Assessment07 §5][assessment]
accepts the result within its frozen scope. [Source-use06][source]
records the primary density input and its normalization.

The claimed bounds are
\[
 \frac1T\int_T^{2T}\Xi_{a,R}(t,X)\,dX
 \le \frac{C}{a^3},\qquad
 \frac1T\int_T^{2T}\Xi_{a,R}(t,X)\,dX
 \le \frac{C_0}{a}\quad\text{using only the complete count}.
 \tag{2}
\]
The constants are independent of \(t,T,a,R\). The first proof uses
(1), while the second uses the complete population bound \(C_NTL\)
for the contributing band from [TND-O Note21, (2), (9)][moment].
Here \(C_N=6A\) for that note's absolute unit-count constant \(A\).
The count also holds at time zero and with closed endpoints.
Neither proof selects a pair.

## 2. One-zero integral and the two mean bounds

For \(r_0>0\), put
\[
 I(y,r_0)=\int_{x^2+y^2\ge r_0^2}
             \frac{y^2\,dx}{(x^2+y^2)^2}.
\]
At \(y=0\) the truncated integrand is zero on its domain, so \(I=0\).
For \(m=|y|>0\) an antiderivative is
\[
 \frac{x}{2(x^2+m^2)}+\frac1{2m}\arctan(x/m).
\]
When \(0<m<r_0\), integrate over both rays outside
\((-\sqrt{r_0^2-m^2},\sqrt{r_0^2-m^2})\). With \(s=m/r_0\), this gives
\[
 I(y,r_0)=
 \frac{1}{r_0}\frac{\arcsin s-s\sqrt{1-s^2}}{s}.
\]
The numerator has derivative \(2s^2/\sqrt{1-s^2}\) for \(0<s<1\)
and value zero at \(s=0\), so
\[
 \frac{\arcsin s-s\sqrt{1-s^2}}{s^3}
 =2\int_0^1\frac{v^2\,dv}{\sqrt{1-s^2v^2}}\le\frac{\pi}{2}
 \qquad(0<s\le1).
\]
The upper bound is the integral at \(s=1\), which is finite and equals
\(\pi/2\) by the substitution \(v=\sin\theta\). For \(m\ge r_0\)
the domain is the whole line and \(I=\pi/(2m)\), which agrees with the
preceding formula at equality. For \(m<r_0\) the two radial boundary
points have zero measure, and for \(m=r_0\) the equality point \(x=0\)
has a finite integrand. Thus the closed radial cutoff gives
\[
 I(y,r_0)\le \frac{\pi}{2}
       \min\left\{\frac1{r_0},\frac{y^2}{r_0^3}\right\}
 \tag{3}
\]
for all real \(y\).

Write \(u=\Re\rho\), \(y=\Im\rho\). If \(|u-X|\le R\) at a center
in \([T,2T]\), then \(u\in[T-R,2T+R]\subseteq[T/2,5T/2]\).
The three closed dyadic bands
\([T/2,T]\), \([T,2T]\), and \([2T,4T]\) cover this set, including
its endpoints. Their scales are at least \(8\). Double counting
shared endpoints only enlarges the sum of nonnegative marks.
Since \(\log(T/2)\ge3L/4\) and \(\log(2T)\ge L\),
their combined (1) bound is at most \(\frac{11}{3} C_b T/L\).

Set \(r_0=a\ell\). Tonelli exchanges the nonnegative zero sum and
center integral. For each contributing occurrence use \(x=u-X\),
retain the radial cutoff, and extend the center integral to the
whole line by dropping the horizontal and band cutoffs. This is
an upper bound with the original closed horizontal cutoff. Thus
\[
 \frac1T\int_T^{2T}\Xi_{a,R}(t,X)\,dX
 \le\frac{\ell^2}{T}\sum_{T/2\le u\le5T/2}I(y,r_0)
 \le\frac{\pi\ell^2}{2T(a\ell)^3}
       \frac{11C_b T}{3L}
 =\frac{11\pi C_b}{6a^3}.
 \tag{4}
\]
For the comparator, use the identical first inequality in (4) and the
first bound inside the minimum in (3). The complete count
\(\#\{\rho:T/2\le u\le5T/2\}\le C_NTL\) gives
\[
 \frac{\ell^2}{T}\sum_{T/2\le u\le5T/2}I(y,r_0)
 \le \frac{\pi\ell^2 C_NTL}{2T(a\ell)}
 =\frac{\pi C_N}{2a}.
 \tag{5}
\]
This comparison uses the same observable, averaging band, normalization,
and cutoffs. Both proofs are slice-wise and uniform over the closed
heat slab. They require no differentiation of cutoffs, root tracking,
or simplicity.

## 3. Signed near sum for an independently isolated pair

Let \(c,D\) be real and take the conjugation-invariant selected pair
\(z_\pm=c\pm\sqrt D\). At \(D=0\) these are two occurrences of the
same double. Assume \(|D|\le d\ell^2\), \(d\ge0\), and an independently
paid exterior collar \(|\rho-c|\ge a\ell\) for all exterior
occurrences, with \(a^2>d\). The algebra holds at any real \(c\).
For the center-band application use \(c\in[T,2T]\). For an exterior
occurrence write \(w=\rho-c=x+iy\), \(r^2=|w|^2\), and
\(\delta=d/a^2<1\). Its signed interaction is
\[
 q=\Re\frac1{(z_+-\rho)(z_--\rho)}
   =\Re\frac1{w^2-D}
   =\frac{r^2-D-2y^2}{|w^2-D|^2}.
\]
The identity \(|w^2-D|^2=(r^2-D)^2+4Dy^2\) follows by expanding
the squared modulus. Subtraction gives
\[
 q=\frac1{r^2-D}
 -\frac{2y^2(r^2+D)}
        {(r^2-D)((r^2-D)^2+4Dy^2)}.
 \tag{6}
\]
Indeed the numerator of the difference is
\(4Dy^2+2y^2(r^2-D)=2y^2(r^2+D)\).
For either sign of \(D\), the collar gives \(|D|\le\delta r^2\).
Thus each \(r^2\pm D\) is at least \((1-\delta)r^2>0\), and
\(|w^2-D|\ge r^2-|D|\ge(1-\delta)r^2\).
The squared modulus bound covers the subtracted \(4|D|y^2\) term
when \(D<0\). Also \(r^2+D\le(1+\delta)r^2\). In particular,
\[
 0\le\frac1{r^2-D}-q
 \le C_\delta\frac{y^2}{r^4},\qquad
 C_\delta=\frac{2(1+\delta)}{(1-\delta)^3}.
 \tag{7}
\]
At \(D=0\), (6) is \(q=r^{-2}-2y^2/r^4\), with equality in the
upper bound of (7) for \(\delta=0\). The formulas retain both separated real and
conjugate pairs without dividing by their internal gap.

Let \(S_R=\sum_{\rho\ {\rm exterior},\,|x|\le R}q\), with one term
per occurrence. Both target roots satisfy
\(|z_\pm-c|=\sqrt{|D|}\le\sqrt d\,\ell<a\ell\) and are omitted by
the cutoff in \(\Xi_{a,R}(t,c)\). All nearby exterior terms meet the
cutoff, including equality. The two sums have the same occurrences,
and (7) gives
\[
 \ell^2 S_R
 \ge \ell^2\sum_{\rho\ {\rm exterior},\,|x|\le R}\frac1{r^2-D}
        -C_\delta\Xi_{a,R}(t,c).
 \tag{8}
\]
This is a pointwise comparison with the actual transverse sum at \(c\).

## 4. Rate, exceptional measure and direct comparison

For \(a=L^\eta\) with \(0<\eta<1\) fixed, the physical collar
\(a\ell=L^{\eta-1}\) shrinks and the allowances in (4) and (5)
are respectively \(O(L^{-3\eta})\) and \(O(L^{-\eta})\). The
improvement concerns the dependence on a growing normalized radius.
For fixed \(a\), both upper bounds are \(O(1)\) in height.
There is no assertion about sharpness or numerical onset.

At each fixed time and for \(h>0\), Markov gives only
\[
 \big|\{X\in[T,2T]:\Xi_{a,R}(t,X)>h\}\big|
 \le \frac{C T}{a^3 h}
\]
in Lebesgue measure. Averages over selected pair centers would require
a separately specified conditioning measure and denominator. A growing
count-two collar must be acquired independently before using (8) at
that radius. These estimates leave the fixed-collar selected-pair
\(o(1)\) loss, quantitative radial lower mass, full \(M\) sign,
incoming anchor, and signed integrated cost open.

Give the direct evaluator the complete source, contours, collar and
pair coordinates, canonical count and transverse moment, the radial
decomposition, [Note33's far estimate][far] on its declared domain,
and any independently paid incoming value. It also gets the deflated
segment identity and its normalized jet formula at a double from
[Note24][jet], including the vertical segment when \(D<0\). The
same input proves (4)–(8) directly. No transport-specific information
or evaluation-cost gain is established.

## 5. Control replay

The additional quantitative input in (4) is (1). It is acquired here
through the complete source and can agree with a different divisor.
The checks below use the documented families and preserve the earlier
collisions. [Controls12][controls] · [Decision17 §5][decision] ·
[Note33 §6][far] · [Note34 §4][counts]

| Control | Premise and scope |
| --- | --- |
| Quadratic and even quartic | Can pass the local pair and collar premises. Their finite divisor lacks the canonical growing count law. An upper population or second-moment bound alone need not exclude such a divisor. |
| Euler-factor translates | Change the complete theta field and fail the canonical endpoint count discrepancy in the documented class. The upper transverse moment in (1) remains untested for that modified flow. |
| Weighted-square, finite-source, finite-score and finite-prime | Fail the full reflected unit-weight theta identity. The documented endpoint-defective classes also fail the fixed-strip premise. Finite endpoints or score rows do not establish the inherited heat-time moment theorem. |
| Reflected super-Gaussian | Retains reflection but fails order at most one in the documented class. The canonical population and moment are unassigned. |
| Smooth shape and positive-primitive | Retain the stated positivity/primitive properties with changed arithmetic. Their canonical strip, count and transverse moment transfer remain untested. |
| Fixed-event atom and compact-profile controls | Fail the full theta source identity and the canonical \(X\log X\) count law in their finite-type classes. Finite profiles do not supply a canonical count-two tube. |
| RH-conditional endpoint mergers | Retain their RH hypothesis and changed ordinary Dirichlet arithmetic. Exact canonical count and heat-time moment transfer remain untested. |
| Varied observation kernels and fractional-profile relaxation | Fail respectively the physical cosine/Newman readout and the complete integer zero divisor. |

**Note34's identical-count controls.** For their fixed-slice divisors
\(F_{\pm,c}\), deleting occurrences from \(H_0\) decreases the
nonnegative moment in each band \([U,2U]\). All real insertions
contribute zero. Of the nonreal ones, only the pair at positive real
part \(c+2/\log c\) can enter such a band for \(U\ge8\). The pair adds
at most \(24/(\log c)^2\le3/2\) for \(c\ge e^4\). Since \(U/\log U\)
is increasing on \([8,\infty)\), both modified divisors satisfy the
same form of (1) on their fixed slices with the uniform constant
\(C_b+(3/2)\log(8)/8\). They also satisfy the complete count upper
bound. Hence the unconditioned \(a^{-3}\) conclusion itself applies
to these slices. Along the sequence in Note34 with \(H_0(c)\ne0\),
the unchanged theta identity fails. Positive Fourier-source
representation and a common physical heat-time tube remain unpaid.

For the selected double of either control, take \(T=c\), \(R=3\),
\(a=1\), \(D=0\). The only nearby exterior group lies at
\(x=2\ell\). For the conjugate insertion \(y=\pm2\sqrt3\,\ell\),
its normalized radial contribution is \(1/8\), and its
\(\Xi_{a,R}\) is \(3/32\). Equation (6) gives the exact near value
\(1/8-2(3/32)=-1/16\). The real insertion gives normalized radial
contribution \(1/2\), \(\Xi_{a,R}=0\), and near value \(1/2\).
The full-divisor errors remain those of Note34. These fixed-slice
analytic divisors show that the shared count, paid fixed collar and
broad transverse upper moment do not imply a favorable signed near
value at the designated center. The calculation concerns these
controls and gives no sign for the canonical selected-pair sum.

[request]: ../research-progress/handoffs/VCD-GT-E17-r1.md
[decision]: ../brainstorm/notes/17_VCD_GT_B09_SOURCE_NEAR_FIELD_DECISION_20261117.md
[source]: ../references/06_VCD_GT_TRANSVERSE_MOMENT_SOURCE_USE_20261117.md
[counts]: 34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md
[far]: 33_VCD_GT_E12_UNIFORM_SIGNED_FAR_EXTERIOR_20261117.md
[jet]: 24_VCD_GT_FOURIER_GROUPING_AND_DEFLATED_CURVATURE_20261116.md
[moment]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/21_TND_O_E11_BROAD_WINDOW_TRANSVERSE_DENSITY_20261107.md
[assessment]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/reviews/07_TND_O_E13_ASSEMBLED_LOCALIZATION_ASSESSMENT_20261107.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[class]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
