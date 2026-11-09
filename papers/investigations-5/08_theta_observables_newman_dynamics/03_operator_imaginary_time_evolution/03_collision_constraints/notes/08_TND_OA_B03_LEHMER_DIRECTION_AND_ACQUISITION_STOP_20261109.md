# Lehmer data and the direction of the required force bound

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, existing OA chat0002. Actual model
identifier and reasoning effort are unavailable in the registry.

**TND-OA-B03 — B, completed: park the present finite-pair acquisition cycle.**
The algebra and polynomial control below are **proved in-note, with
proof-author self-check only**. No canonical field evaluation, root search,
certificate replay or numerical acquisition was performed. A fixed
[E02 assessment](../research-progress/handoffs/05_TND_OA_E02_LEHMER_SCREEN_ASSESSMENT_REQUEST_20261109.md)
is issued for Sol. E01's accepted theorem is unchanged.

This is an information-direction diagnostic and a source-readiness
decision, not an RH criterion or an impossibility result for signed
force bounds. Read the [result index](../../../../../../result-summaries/README.md),
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../../../avoid/README.md), especially
[classification01](../../../../../../avoid/01_restating_the_target.md),
[control02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[numerics10](../../../../../../avoid/10_numerics_ahead_of_the_question.md)
and [known-region11](../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md).

## 1. One candidate and what its sources actually supply

The one candidate is the classical first Lehmer pair
\(\{\gamma_{6709},\gamma_{6710}\}\), near zeta ordinate 7005,
as identified in Stopple's *Lehmer Pairs Revisited*, v2, §3/Figure 1.
In this branch's normalization its \(H_0\) roots are
\(a=2\gamma_{6709},b=2\gamma_{6710}\), near physical height 14010.
The intended consumer would be an E01 survival comparison for the
positive-time descendants of this pair, ending at Newman time zero.
No positive starting time, root enclosure or parameter box is fabricated.

The bounded inspection used the existing auxiliary-flow survey
[DY02–DY03](../../../../06_auxiliary_collision_flows/lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md#dy02),
the HDC external-reading pointers, and their primary sources. This is
not an exhaustive search for every published heat-zero certificate.
The [source-use record](../references/03_TND_OA_B03_LEHMER_SOURCE_USE_20261109.md)
identifies versions, passages, reading copies and limitations.

The inspected close-pair sources supply time-zero evidence and
Lehmer diagnostics. Stopple explicitly assumes RH throughout.
Csordas–Odlyzko–Smith–Varga (COSV), in the corrected 1993 paper,
use a gap and an exterior sum to obtain a lower bound on the Newman
constant; their Theorem 1.1 is not a positive-time survival certificate.
No numerical data for COSV's different high pair are selected as a
second candidate here.

Keep the time and scale conventions separate:
\[
H_0(x)=\frac18\Xi(x/2),\qquad
\widehat H_t(\gamma)=4H_{4t}(2\gamma)
\tag{1}
\]
for the heat integral written in Stopple §2. The second identity follows
by changing its integration variable \(u=2v\).
Thus its ordinate and heat variables are \(x=2\gamma,\lambda=4t\).
No numerical Newman-constant bound is transferred across conventions.

E01 requires \(0<\Delta\le\lambda_s\le1/2\), with actual simple roots
at the initial slice \(H_{\lambda_s}\). A root pair at \(H_0\) is not
that starting data: taking \(\lambda_s=0\) permits no positive \(\Delta\).
Following it from zero into negative Newman time changes the accepted
domain. The implicit-function theorem gives some local real continuation
of a simple real pair, but no specified radius or advantage over a
direct continuation from that fact alone.

## 2. The focused clarification: an upper exterior sum is a lower force bound

At one real-simple-pair slice, write \(q=(b-a)^2>0\), and use E01's
deflated logarithmic derivative \(g=U_x/U\). For this section only,
assume every exterior zero \(\rho\) is real and outside \([a,b]\),
and the product representation gives
\[
g_x(x)=-\sum_{\rho\ne a,b}\frac1{(x-\rho)^2}.
\tag{2}
\]
This holds for the relevant finite real-rooted polynomials, and for
the order-one canonical product under the additional all-real premise.
The sums converge absolutely and uniformly on the pair segment:
there is a positive distance to every remaining zero locally, and
the squared reciprocal tail is summable. These premises are not
imported unconditionally for theta at time zero or below an unknown
positive threshold.

Define the endpoint sum in physical \(x\) units,
\[
G=\sum_{\rho\ne a,b}
\left\{\frac1{(a-\rho)^2}+\frac1{(b-\rho)^2}\right\},
\qquad
S=\sum_{\rho\ne a,b}
\frac1{(a-\rho)^2(b-\rho)^2}.
\tag{3}
\]
Integrating (2) over the pair and dividing by \(b-a\) gives
\[
B=-\sum_{\rho\ne a,b}\frac1{(a-\rho)(b-\rho)}.
\]
Termwise subtraction, justified by the stated convergence, yields
\[
\boxed{G+2B=qS\ge0,\qquad -G/2\le B\le0.}
\tag{4}
\]
Indeed each difference is
\((a-b)^2/((a-\rho)^2(b-\rho)^2)\), and each product
\((a-\rho)(b-\rho)\) is positive. The upper bound is strict if an
exterior zero exists, without providing a quantitative strict margin.
Under \(x=2\gamma\), \(G_\gamma=4G_x\) and
\(q_\gamma=q_x/4\), so \(qG\) is invariant.

Consequently an upper allowance \(G\le G_*\) implies
\[
B\ge-G_*/2,
\qquad
q'=-8-4qB\le-8+2G_*q.
\tag{5}
\]
E01's survival consumer instead uses \(B\le b\), giving
\(q'\ge-8-4bq\). Reversing the first inequality in (5) would be an
error. No uniform-in-time \(G_*\) is asserted by reading a time-zero
Lehmer value. The familiar exterior upper sum is suited to controlling
how much the exterior can delay a collision; it does not by itself pay
the favorable upper force required here.

Equation (4) does not forbid obtaining an upper \(B\) by additional
information. Lower contributions from specified exterior zeros,
appropriate geometry, or direct source jets could supply information
that an upper \(G\) alone does not. Their data and, where used, the
all-real premise must be paid. Under the latter premise \(B\le0\) is
already available; no new arithmetic sign follows from renaming it.
The negative square in E01's direct transfer remains a valid route
without that product premise, but its favorable value is unacquired.

## 3. Exact heat control: the small-gap test is not a survival barrier

Consider the even polynomial heat solution
\[
h(\tau,z)=z^4+(12\tau-5)z^2+12\tau^2-10\tau+4,
\qquad h_\tau=h_{zz}.
\tag{6}
\]
At \(\tau=0\), its roots are \(-2,-1,1,2\); select \(a=1,b=2\).
The exterior roots are \(-1,-2\), so direct rational arithmetic gives
\[
q=1,\quad
G=\frac14+\frac19+\frac19+\frac1{16}
 =\frac{77}{144}<\frac45,\quad
B=-\frac16-\frac1{12}=-\frac14,\quad
S=\frac5{144}.
\tag{7}
\]
Thus \(G+2B=5/144=qS\). In particular \(B>-G/2\), so the
incorrect reverse inequality already fails at this regular slice.
The same small-gap/exterior-sum inequality used to define a Lehmer
pair is satisfied as an algebraic diagnostic for this polynomial.
This is not an application of a theorem about the canonical theta field.

The quadratic in \(w=z^2\) has discriminant
\[
\mathcal D(\tau)=96\tau^2-80\tau+9.
\]
Its first zero is
\[
T=\frac{10-\sqrt{46}}{24},\qquad \frac18<T<\frac14.
\tag{8}
\]
For \(0\le\tau<T\), both \(w\)-roots are positive and distinct:
their sum is \(5-12\tau>0\), their product is
\(12\tau^2-10\tau+4>0\), and \(\mathcal D>0\).
At \(T\), (6) equals \((z^2-r^2)^2\), where
\[
r^2=\frac{\sqrt{46}}4,\qquad h_{zz}(T,r)=2\sqrt{46}>0.
\]
The positive pair therefore has a nondegenerate double collision;
just after \(T\), \(\mathcal D<0\). On the entire real-pair side
the exterior is the negative pair, and
\[
B(\tau)=-\frac1{2a(\tau)b(\tau)}<0.
\tag{9}
\]
A favorable force sign delays but does not eliminate the collision.
The change \(F_\lambda(z)=h(1/4-\lambda,z)\) places this local
collision at positive Newman time \(1/4-T\), with
\(\partial_\lambda F=-F_{zz}\). It does not make the polynomial a theta source.

This control tests the generic product/heat inference, not E01's
fully paid strict survival theorem. At the event an application of
that theorem cannot have all its strict premises. No particular
uncomputed parameter-box floor is declared to fail.

## 4. Source, comparison and control gates

| B03 requirement | Outcome for the one candidate |
| --- | --- |
| Documented pair | The first Lehmer pair is identified at Newman time zero. |
| Actual positive starting slice and its enclosures | Not supplied by the inspected records; neither a time radius nor initial E01 constants are acquired. |
| Complete source model on the new chart | E01 has general source-error formulas, but no evaluated floor or force here. The RT/HDC certificate around \(x=36\), radius 11, is not a certificate near \(x=14010\). |
| Strongest direct comparator | The time-zero pair is already documented; inspected root/jet diagnostics do not furnish a matched positive-time survival or cost comparison. No measured gap against direct acquisition is established. |
| B02 redundancy screen | Cannot be evaluated without honest \(Q_\pm,D,\Delta\). A missing tuple is not a failed screen or evidence of advantage. |
| Favorable signed estimate | The endpoint exterior upper sum has the lower-force direction (5); the required upper bound remains unpaid. |
| Finite execution contract | Not issued: choosing arbitrary start times or a scan would precede a demonstrated useful comparison. |

The [controls12 inventory](../../../../../../result-summaries/12_collision_controls_and_screening.md)
continues to apply. This is an analytical premise audit; no old
control certificates were rerun:

| Control family | Premise not available for the proposed canonical import |
| --- | --- |
| Euler-factor | Unchanged canonical coefficients/completion; matching some time-zero zeros does not supply their heat descendants. |
| Weighted-square | Full reflection and unit coefficients; the documented controls also lack an all-real heat time. |
| Reflected super-Gaussian | Canonical integer-square source arithmetic. |
| Smooth-shape, positive-primitive and earlier counter-kernels | Complete theta source, despite the named common qualitative properties. |
| Finite-source and finite-prime orbit | Full source/reflection; documented finite-source controls do not have an all-real heat time. |
| Fixed-event and finite-profile threshold | Full profile, theta coefficients and eventual simplicity. |
| RH-conditional endpoint control | Ordinary Dirichlet-series arithmetic; its real positive-time descendants can satisfy generic all-real product identities and still have an endpoint double. |
| Variable kernel | Literal cosine observation and physical Newman equation. |
| Actual-profile measure relaxation | A complete integer zero divisor with the stated canonical product. |

One must not assign an unverified all-real premise to every control,
or say all controls fail (4): the polynomial (6) satisfies it and
collides. Altered sources do not inherit the named pair's numerical
data. No theta-specific signed estimate has been acquired that would
screen every control by a new quantitative margin.

## 5. Disposition and restart condition

**Park the present finite-pair acquisition cycle.** The single inspected
replacement does not supply the positive-time starting certificate or
an unmet quantitative comparison, and the suggested exterior upper sum
has the wrong bound direction for the survival consumer. This is a
scoped evidence gap for this candidate and these inspected records,
not a proof that no useful canonical case exists.

E01 remains accepted; B02's stopped pilot is not reopened. The next
fixed task is E02's analytical assessment of (1), (4)–(5), (6)–(9)
and this source-use scope. It is E / Sol, not numerical research.
No automatic B04 case search is proposed. Reopen acquisition only
after new evidence names a positive starting pair/domain, a comparison
with a specific unmet bound, and a credible complete-source budget.
See [Continuation09](09_TND_OA_AFTER_B03_CONTINUATION_AND_MODEL_CHANGE_20261109.md).
