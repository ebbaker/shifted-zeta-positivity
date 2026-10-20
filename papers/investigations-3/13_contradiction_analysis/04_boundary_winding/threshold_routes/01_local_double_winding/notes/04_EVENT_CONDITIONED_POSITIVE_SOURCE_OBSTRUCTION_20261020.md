# BW-01: exact event cancellation does not reverse the face-pair sign

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**, reasoning effort
**ultra**, inherited from the parent session configuration.

**Status: scoped analytic obstruction, proved in-note; [separate same-model
internal review][review], not specialist review.** This tests the next BW-01 task: whether positive-source covariance
or moment inequalities, now retaining both exact event cancellations,
can supply a lower bound opposing the negative critical-value face pair
in [BW-08 Note 03][bw08]. An elementary positive atomic-source family has
a genuine positive all-real threshold, a double event at the **fixed**
height a=20, and uniformly bounded complete source moments, yet has an
exact strictly negative face pair. It passes BW-08's scalar imaginary-axis
floor at that event; its degenerating subfamily also passes the b=40
observation in the [new adaptive-height consumer][bw08all]. Its normalized curvature is unbounded below while
the event time, height, source support and moment upper budgets stay fixed.

This is not an obstruction to estimates using the unchanged complete
theta source. The control is atomic, has exponential type, and has
infinitely many simultaneous threshold collisions. It does not have
theta's positive-time eventual simplicity at its threshold or its
imaginary-axis growth at arbitrarily large heights. No theta collision,
exclusion, new covered region, later witness or computational gain is
reported. The earlier [symmetric-remainder obstruction][bw01] did not
retain the present positive-source and actual-threshold information; this
note closes a different, explicitly specified inference.

The [result summaries][results], especially [control cluster 12][controls]
and [local-law cluster 13][laws], and [patterns to avoid][avoid], especially
[classification][a01], [control premises][a02] and [scope][a07], govern
the claim. This is a counterexample to a proposed reduced-information
inference, not an RH-equivalent criterion supported by control checks.

## 1. Contract and selected information

The target is an opposing estimate for

\[
P(s)=\frac{H(T+s,c(T+s))+H(T-s,c(T-s))}{h_2},\qquad
h_j=\partial_x^jH(T,a),
\]

where c(T)=a and Hx(t,c(t))=0. The BW-08 transfer gives a negative
quadratic upper bound at hypothetical theta double events with a>=20.
The corresponding raw jet quantity, for 0<L<=ell(a), is

\[
Q_L=2h_3^2-3h_2h_4-18Lh_2^2,
\quad
\ell(a)=\frac1{4a}\log\frac{a+1}{4\pi}-\frac3{2a^2}.
\tag{1}
\]

An opposing Q_L<=0, or P(s)>=0, would contradict that transfer if proved
from applicable independent theta information. Neither is assumed here.
The class tested consists of cosine heat transforms of positive finite
measures, all-real threshold T, exact H=Hx=0 with h2!=0, a fixed event
height and complete moment upper bounds. We additionally retain the
scalar bound D_T(a)>log((a+1)/(4pi))/4 used by BW-08 at that event,
and, on the subfamily specified below, the newer bound at b=40.
We do not retain theta's exact source or its full imaginary-axis function.

All calculations below use the complete three-atom source; there are no
omitted modes, quadrature errors, cutoff crossings, or differentiated
error allowances. The checker is restricted to exact finite algebra and
rational inequalities, fixed before its execution. It tests the PDE,
event jets, critical-value substitution, second derivative, and the
factorization used to locate every future complex zero. Its rational
curvature table is an algebraic check, not a sampled theta experiment.

## 2. A positive-source family at fixed (T,20)

Fix any 0<T<=1/2 and 1/2<=q<1. Put

\[
\theta=\arccos(-q),\qquad \lambda=\theta/20,
\qquad A=(1+q)^{-2}.
\]

Thus 2pi/3<=theta<pi and pi/30<=lambda<pi/20. Define

\[
H_q(t,z)=A\left(q^2+\frac12+
2q e^{\lambda^2(t-T)}\cos(\lambda z)
+\frac12e^{4\lambda^2(t-T)}\cos(2\lambda z)\right).
\tag{2}
\]

It is exactly the heat cosine transform of the nonnegative measure on
[0,infinity)

\[
\mu_q=A\left((q^2+\tfrac12)\delta_0+
2q e^{-T\lambda^2}\delta_\lambda+
\tfrac12e^{-4T\lambda^2}\delta_{2\lambda}\right).
\tag{3}
\]

The atom at zero has its full displayed mass in this half-line measure.
Every component solves Ht=-Hxx. The entire field is even and of order
one, and

\[
H_q(T,z)=A(\cos(\lambda z)+q)^2,\qquad H_q(T,0)=1.
\tag{4}
\]

At a=20 the zero has exact multiplicity two. This normalization fixes
the complete heat-weighted source mass at the event, and changes none
of the ratios below.

**The all-real threshold is exactly T.** Set r=e^{lambda^2(t-T)} and
y=cos(lambda z). Apart from the positive factor A, (2) is

\[
p_r(y)=r^4y^2+2qry+q^2+\tfrac12-\tfrac12r^4.
\]

For t>T, r>1. The vertex -q/r^3 lies in (-1,0). With v=r^{-2} in (0,1),
one quarter of the discriminant, divided by r^8, is

\[
\frac12-(q^2+\tfrac12)v^2+q^2v^3
=(1-v)\left(\frac{1+v}{2}-q^2v^2\right)>0.                 \tag{5}
\]

The bracket is positive because q<1 and (1+v)/2>=v^2 on [0,1].
The vertex value is therefore negative. Both endpoint values are
strictly positive: p_r(1)>0, while

\[
p_r(-1)=\tfrac12r^4-2qr+q^2+\tfrac12>(1-q)^2>0
\]

since its derivative in r is 2r^3-2q>0 for r>=1. Hence p_r has two
distinct roots in (-1,1). If cos(lambda z) lies in (-1,1), then z is
real: for z=x+iy with y!=0, the imaginary part forces sin(lambda x)=0,
and the real part would have absolute value cosh(lambda y)>1.
All zeros of H_q(t,.) are consequently real and simple for every t>T.

For t<T put d=T-t>0. Direct Gaussian integration gives

\[
H_q(t,x)=A\,\mathbb E\bigl[(\cos(\lambda x+
\lambda\sqrt{2d}\,Z)+q)^2\bigr]>0,\quad Z\sim N(0,1).
\tag{6}
\]

Indeed each cosine mode receives the exact multiplier e^{-d k^2lambda^2}.
The integrand is nonnegative and vanishes only on a discrete set, so
the expectation is strictly positive at every real x. The nonconstant
quadratic p_r has a complex root, and cos(lambda z) attains every complex
number: solve w^2-2yw+1=0 for w!=0 and take a complex logarithm.
Thus H_q(t,.) does have zeros, all nonreal, for every t<T. Equations
(4)--(6) prove the claimed global threshold without importing a
Newman-preservation theorem for this source.

## 3. Exact critical curve, face pair and jets

Let u=t-T. On

\[
|u|<\delta_q:=\frac{-\log q}{3\lambda^2},
\]

the analytic critical branch through a=20 is

\[
c(T+u)=\lambda^{-1}\arccos(-q e^{-3\lambda^2u}).             \tag{7}
\]

The branch is nondegenerate there. Substitution gives its complete value

\[
V(T+u)=A\left(q^2+\tfrac12-\tfrac12e^{4\lambda^2u}
-q^2e^{-2\lambda^2u}\right).                              \tag{8}
\]

Writing d=1-q^2>0, direct differentiation at the event gives

\[
h_2=2A\lambda^2d,\quad
h_3=-6A\lambda^3q\sqrt d,\quad
h_4=A\lambda^4(14q^2-8).                                  \tag{9}
\]

Consequently

\[
S_a=\frac{h_3^2}{9h_2^2}-\frac{h_4}{6h_2}
=\lambda^2\frac{4-q^2}{6(1-q^2)},
\qquad
\frac{V''(T)}{h_2}=-\lambda^2\frac{4+2q^2}{1-q^2}.         \tag{10}
\]

For every 0<s<delta_q, the exact signed face pair is

\[
\boxed{
P(s)=-\frac{\cosh(4\lambda^2s)-1+
2q^2(\cosh(2\lambda^2s)-1)}{2\lambda^2(1-q^2)}
\le-\lambda^2\frac{4+2q^2}{1-q^2}s^2<0.}
\tag{11}
\]

The inequality uses cosh x-1>=x^2/2. No Taylor remainder is dropped.
Moreover

\[
Q_L=12A^2\lambda^6(1-q^2)
\left(4-q^2-6(L/\lambda^2)(1-q^2)\right).                  \tag{12}
\]

Thus Q_L>0 exactly when L<S_a. This is a direct signed calculation on
the complete source, not a conclusion inferred from independent absolute
derivative bounds. In particular, retaining exact H=Hx=0 does not force
the opposite sign.

## 4. Passing the two selected BW-08 imaginary-axis observations

For this source the imaginary-axis observation at T is explicitly

\[
D_T(b)=\frac{d}{db}\log H_q(T,ib)
=\frac{2\lambda\sinh(\lambda b)}{\cosh(\lambda b)+q}.
\]

At b=20, theta>=2pi/3>2 and lambda>1/10, hence

\[
D_T(20)\ge2\lambda\tanh(\theta/2)>\frac3{20}
>\frac14\log\frac{21}{4\pi}.                              \tag{13}
\]

For the first strict comparison use tanh(1)>3/4, since e^2>7.
For the last use pi>3 and log(7/4)<3/5; the latter follows already
from 1+3/5+(3/5)^2/2+(3/5)^3/6>7/4. These bounds are uniform in q.
They also give

\[
0<\ell(20)<\frac3{800}<\frac1{120}<S_a,                  \tag{14}
\]

where positivity of ell(20) is the proved BW-08 bound, and the last
inequality follows from lambda>1/10 and
(4-q^2)/(6(1-q^2))>=5/6. Therefore every member passes the specific
necessary scalar restrictions used at this event, including Q_L>0
for each 0<L<=ell(20). Their negative face pairs agree with the
BW-08 consumer.

The [adaptive-height continuation][bw08all] chooses b=40 at a=20,m=2.
Restrict now to 99/100<=q<1. An alternating cosine-series lower bound
gives

\[
\cos3>\sum_{j=0}^7\frac{(-1)^j3^{2j}}{(2j)!}
=-\frac{355168841}{358758400}>-\frac{99}{100}.
\]

Since cosine is decreasing on (0,pi), theta=arccos(-q)>3 and
lambda>3/20. Consequently

\[
D_T(40)\ge2\lambda\tanh(20\lambda)
>\frac3{10}\tanh3>\frac{297}{1000}
>\frac14\log\frac{41}{4\pi}.                              \tag{15}
\]

Here tanh3>99/100 follows from e^6>199. For the last comparison,
pi>157/50 yields 41/(4pi)<1025/314, while the first six positive
terms of the exponential series give exp(297/250)>1025/314.
The checker verifies these rational bounds; its pi lower bound uses
the same Machin/alternating-series method as BW-08.

The newer coefficient at this event therefore satisfies

\[
0<L_2(20)=\frac1{800}+\frac1{160}\log\frac{41}{4\pi}
-\frac1{500}
<\frac{267}{40000}<\frac1{120}<S_a.                         \tag{16}
\]

Thus the degenerating subfamily passes **both** selected imaginary-axis
observations and has Q_L>0 for every 0<L<=L_2(20). The unboundedness in
section 5 persists on this restricted subfamily. It screens the original
and the new adaptive-height BW-01 consumers, not just the old coefficient.

The qualification **at the selected b=20 and b=40** is essential. D_T(b)<=2lambda is bounded
for this family, whereas the theta floor in BW-08 grows logarithmically
as b tends to infinity. This control therefore fails the all-height
version of that floor. The note does not rule out a consumer exploiting
the whole imaginary-axis profile or theta growth together with additional
arithmetic information.

## 5. A uniform moment budget still permits an unbounded normalized loss

For a complete source moment M_j(b)=integral e^{b u^2}u^j dmu_q(u),
let beta=pi/10 be a common support upper bound. Since M_0(T)=1,
for every fixed Delta>=0 and every integer j>=0,

\[
M_j(T+\Delta)\le e^{\Delta\beta^2}\beta^j,                 \tag{17}
\]

where beta^0=1. These are common bounds for the entire source, every
spatial derivative, and every finite order; there is no omitted tail.
Nevertheless, with T and a=20 fixed,

\[
S_a\longrightarrow+\infty,\qquad
V''(T)/h_2\longrightarrow-\infty\quad(q\uparrow1).         \tag{18}
\]

Here lambda tends to pi/20 and h2 tends to zero through positive values.
Thus no finite upper bound on S_a or lower bound on V''(T)/h2 depending
only on these common moment budgets and (T,a) can hold throughout the
stated class. Equivalently, for every finite K there is a member and a
nonempty interval 0<s<delta_q on which P(s)<-K s^2. The interval may
shrink as q approaches one; a fixed time radius is not claimed.

An explicit positive lower bound on |h2| would remove this particular
unboundedness conclusion, as ordinary quotient estimates already show.
It would not establish the contrary sign: the single q=1/2 member
already has h2>0 and the exact negative pair (11). The degeneration in
(18) strengthens the quantitative scope; it is not needed to refute
nonnegative P or nonpositive Q_L in this class.

The event equations also explain why a covariance proof cannot simply
copy BW-08's imaginary-axis step. For a positive event measure nu write

\[
C_j=\int u^j\cos(au)\,d\nu,\qquad
B_j=\int u^j\sin(au)\,d\nu.
\]

Then H=Hx=0 means C0=B1=0, while h2=-C2, h3=B3, h4=C4. The relevant
quadratic is B3^2+C2 C4, whose mixed factor has no covariance sign
under the positive measure nu. Multiplication by cos(au) creates a signed
measure with total mass zero; it is not an admissible probability measure
for the monotone-covariance argument. All genuine moment/Gram and
Cauchy inequalities for a positive nu hold for (3), including after
imposing C0=B1=0, so none can legitimately prove a conclusion refuted by
(11)--(16). No impossibility of a more source-specific moment calculation
is inferred.

## 6. Control audit, comparison and stopping scope

| Control | Relevant shared premise; failed premise of the full theta task |
| --- | --- |
| Family (2) | Positivity, fixed event, exact cancellations, every moment-positivity inequality, actual positive threshold, future simplicity, order one, and the event's scalar floor; q>=99/100 also passes the adaptive b=40 floor. It fails unchanged theta source, smooth density, theta growth and eventual simplicity at the threshold itself. |
| Quadratic/Hermite/even quartic | Retain local heat geometry or a positive threshold as stated in their own sources; fail the present positive measure/source specification, and fail full theta arithmetic. No theta moments are assigned to them. |
| Positive-kernel q and q_(T,a) | Retain their documented positivity/decay/threshold; canonical theta source fails. The present exact formulas are not assigned to those different sources. |
| Weighted-square controls | Retain positivity, selected square support/endpoints and local events; fail full reflection and, by the finite-source audit, have no all-real heat time. They are outside this threshold subclass. |
| Finite-prime orbit controls | Retain specified finite arithmetic and local events; full normalized reflection fails and no all-real threshold is supplied. |
| Reflected/smooth/positive-primitive controls | Retain their documented shape, reflection or auxiliary positivity; unchanged normalized theta square expansion fails. No uncomputed threshold or jet sign is asserted. |
| Euler-factor controls | Actual positive thresholds are known in their stated class and they pass BW-08's scalar floor; unchanged theta coefficients fail. No location, multiplicity or numerical jet at their thresholds is invented. |

The matched direct test is the same Q_L in (1) with exact event jets.
It accepts the control collision, as must the critical-face test. This
is a logical comparison of retained information, not a runtime comparison
or a claim that boundary methods cannot obtain better information.

**Stop the proposed opposing-sign argument when its inputs are only
positive-source/Gram inequalities, exact event cancellation, generic
all-real-threshold facts, moment upper budgets, and the selected
imaginary-axis floors at b=20 and b=40.** The class contains the complete controls above.
This conclusion does not close BW-01, BW-08, estimates using the unchanged
theta coefficients, a full imaginary-axis-profile argument, or a different
signed arithmetic observation. No required theta exclusion task has been
marked complete by this stop.

The [exact checker][checker] and [small receipt][receipt] verify finite
algebra underlying the proof. They do not certify a theta value or a
new zero-free domain. Source hashes bind the version checked, not its
mathematical validity. Parent Git revision is
b39c6cc9b4756bc14c2e500e327169db88571d1f; the ongoing research tree includes
uncommitted notes.

[bw08]: ../../08_deflated_jet_hierarchy/notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md
[bw08all]: ../../08_deflated_jet_hierarchy/notes/04_ALL_HEIGHT_MULTIPLICITY_JET_BOUND_20261020.md
[bw01]: 03_PAIRED_FACE_REMAINDER_OBSTRUCTION_20261019.md
[review]: ../reviews/02_EVENT_CONDITIONED_SOURCE_REVIEW_20261020.md
[checker]: ../numerics/check_event_conditioned_positive_source.py
[receipt]: ../numerics/EVENT_CONDITIONED_POSITIVE_SOURCE_20261020.json
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[laws]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
