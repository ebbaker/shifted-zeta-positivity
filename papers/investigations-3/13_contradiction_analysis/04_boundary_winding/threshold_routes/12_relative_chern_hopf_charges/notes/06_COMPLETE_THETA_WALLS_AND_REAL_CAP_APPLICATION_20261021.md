# Complete theta walls and a real cap charge application

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata. The proof,
implementation and [internal review][review] are by the same assistant.
No independent specialist review or novelty claim.

**Status: proved in-note with a finite interval-certified source application.**
The previously unpaid wall, root-count, phase and real-cap hypotheses of
[Note 05][n05] now hold for the complete theta family on the fixed window
\[
 \begin{split}
 D&=\{t:|\Re t|<1/100,\ |\Im t|<1/100\},\\
 B&=D\times\{z:|z-71/2|<10\}.
 \end{split}                                                     \tag{1}
\]
There are exactly two spatial roots, counted with multiplicity, in the
outer disk for every time in the closed rectangle, and both lie in the
inner disk of radius 8. The source calculation proves
\[
 |A|<3.489078,\qquad K\tau<0.034891<\pi/2,\qquad
 \Delta(-1/100)>144,\quad\Delta(1/100)>144.                        \tag{2}
\]
Consequently **the relative charge is zero on (1)**. This closes the
first finite application of the analytical two-root theorem. It does
not provide an arbitrary-height estimate or settle endpoint simplicity.

The [declared plan][plan] fixes the geometry, method and stop before
source acquisition. The [script][script] and small [receipt][receipt]
carry the complete source payments. This is an application-feasibility
calculation, not a new speed comparison. Read the [result index][results],
[local geometry cluster][local], [control register][controls] and
[avoid index][avoid], especially [classification][a01], [matched
controls][a02], [scope][a07], [question before numerics][a10] and
[hypothesis audit][a14]. The numerical milestone is (2), not a claim
that finite checks support an RH-equivalent assertion.

## 1. A wall estimate retaining the coupled numerator

Use the unchanged complete theta source and backward heat normalization
of Note 05, equations (1) and (20):
\[
 H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du,\qquad H_t=-H_{zz}.
                                                               \tag{3}
\]
This is also the normalization in [Polymath, equations (3)–(4)][polymath].
The tail and Taylor arguments below apply directly to (3); no RH or
zero table is an input.

For a proper two-root cluster write H=UP and
\(P=(z-z_1)(z-z_2)\). Note 05 proves, including at a collision,
\[
 \Delta'=8+A\Delta,\qquad
 A=\frac4{2\pi i}\int_{|\zeta-a|=R}
       \frac{H_z-\kappa H}{HP}\,d\zeta.                          \tag{4}
\]
Here a=71/2, R=10, and the fixed subtraction is \(\kappa=-3/10\).
The subtraction changes no integral: \(\int d\zeta/P=0\) for a monic
quadratic, whether or not its roots coincide. All exterior forcing
remains in H. We use neither a truncated exterior-zero sum nor a bound
on the inverse internal gap.

Partition the outer circle into N equal counterclockwise arcs. If
\(d_k>0\) is a lower bound for |H| and \(n_k\) an upper bound for
\(|H_z-\kappa H|\) on the whole kth arc and all times in the closed
rectangle, while both roots stay within radius r<R, then
\[
 \boxed{|A|\le \frac{4R}{(R-r)^2}\frac1N
                    \sum_{k=0}^{N-1}\frac{n_k}{d_k}.}           \tag{5}
\]
Indeed |P|>=(R-r)^2, each arc has length 2pi R/N, and the integral
triangle inequality gives (5). This retains spatial variation in the
ratio instead of replacing it by its maximum. The numerator coefficients
are formed before taking their absolute values. The remaining triangle
inequalities still discard phase around the spatial contour; no exact
contour cancellation beyond the scalar subtraction is asserted.

## 2. Complete source Taylor bounds on entire arcs and times

Set N=256, T=tau=1/100 and eta=3/200, so |t|<=sqrt(2)/100<eta on
our time rectangle. On either circle s=8 or 10 use anchors
\[
 z_{s,k}=a+s e^{2\pi i k/N},\qquad
 h_s=2\pi s/N.
\]
Every point on the full arc from anchor k to anchor k+1 has
\(|w|=|z-z_{s,k}|\le h_s\). Its straight chord from the anchor
lies inside the disk, hence has |Im z|<=10. Define complete positive
majorants, with the exponential envelope used in [Note 01][n01],
\[
 M_j=\int_0^\infty\Phi(u)u^j e^{u^2/100+10u}\,du
                   \qquad (8\le j\le17).                       \tag{6}
\]
These are slightly larger envelopes than Note 05's cosh moments.

Write \(c_{j,k}=\partial_z^jH(0,z_{s,k})\). With j=0 or 1,
multivariate Taylor expansion to total degree seven gives
\[
 \partial_z^jH(t,z_{s,k}+w)
 =\sum_{p+\ell\le7}\frac{(-t)^p w^\ell}{p!\ell!}
                  c_{j+2p+\ell,k}+\mathcal E_{j,k},
                                                               \tag{7}
\]
\[
 |\mathcal E_{j,k}|\le R_{j,s}:=
 \sum_{p+\ell=8}\frac{\eta^p h_s^\ell}{p!\ell!}M_{j+2p+\ell}.
                                                               \tag{8}
\]
To prove (8), apply the one-variable Taylor integral remainder to
\(v\mapsto\partial_z^jH(vt,z_{s,k}+vw)\), 0<=v<=1. The mixed
heat derivatives contribute \((-1)^p\partial_z^{j+2p+\ell}H\).
Complete source domination by (6) bounds each derivative; the integral
remainder and binomial coefficients give exactly 1/(p!ell!). Along the
path Re(vt)<=T and |Im(z_{s,k}+vw)|<=10. No extra real heat factor
for Im(t) is inserted. Source decay justifies all derivatives.

The complete complex coefficient enclosures are acquired for 0<=j<=15.
Conjugation gives the lower half of each circle from its upper half at
time zero. This is used only for anchor data. Bounds (7)–(8) separately
cover all complex times, including both signs of Im(t).

For coefficient enclosures C, use upper/lower modulus bounds and set
\[
 \begin{split}
 E_{0,k}&=R_{0,s}+
  \sum_{1\le p+\ell\le7}\frac{\eta^p h_s^\ell}{p!\ell!}
                       |C_{2p+\ell,k}|_{\rm up},\\
 d_k&=|C_{0,k}|_{\rm low}-E_{0,k},\\
 D_{j,k}&=C_{j+1,k}-\kappa C_{j,k},\\
 n_k&=|D_{0,k}|_{\rm up}+R_{1,s}+|\kappa|R_{0,s}
  +\sum_{1\le p+\ell\le7}\frac{\eta^p h_s^\ell}{p!\ell!}
                     |D_{2p+\ell,k}|_{\rm up}.
 \end{split}                                                     \tag{9}
\]
Thus d_k and n_k pay the full products of each circular arc with the
closed time rectangle. Acquisition error is retained in C and D. The
subtraction does not pretend that separately acquired interval errors
are correlated; it retains the cancellation of their enclosed values.
The two Taylor remainder bounds for the numerator are combined safely.

Each coefficient uses Acb integration of the first four modes over
u in [0,1]. The inherited [tail proof][n01] and helper bound every n>=5
mode over [0,infinity) and the retained-mode integral over [1,infinity).
Their common envelope here is T=1/100, Y=10 and the actual derivative
order. The positive moments use the same complete tails. The source
integrands are entire, so the integration callback meets the analytic
contract in the [python-flint documentation][acb].

## 3. Spatial root counts without assuming interior exclusion

The computed d_k are positive on both circles. In particular the true
H(0,z) image of each full circular arc stays in a disk centered at
H(0,z_{s,k}), with radius E_{0,k}<|H(0,z_{s,k})|. The polygonal chord
between its endpoint values stays in that same zero-free convex disk.
Straight interpolation therefore gives a zero-avoiding homotopy from
the actual spatial boundary curve to the polygon.

The script encloses each principal argument of
\(C_{0,k+1}/C_{0,k}\), checks its real part is positive, and sums
these increments. This produces an enclosure of the actual polygonal
winding, rather than an unverified sum of sampled phases. Both windings
lie strictly between 3/2 and 5/2 and contain 2. Since they are integers,
both spatial root counts are exactly two. The counterclockwise spatial
orientation is used throughout.

All-time wall nonvanishing keeps both counts constant on the connected
time rectangle. Equal counts imply that the annular collar contains no
roots and both outer-disk roots remain strictly within radius 8.
Only now is the proper-cluster formula (4) applied. A spatial double
root is allowed by these counts and by the entire construction.

## 4. Certified values and cap signs

The outward-rounded reported bounds are:

| Quantity | Inner circle s=8 | Outer circle s=10 |
| --- | ---: | ---: |
| Complete all-time wall floor | >8.36937e-7 | >7.57583e-7 |
| Maximum E_0 / anchor modulus | <0.337413 | <0.159600 |
| Spatial root count at t=0 | 2 | 2 |
| Remainder R_0 | <1.035760e-16 | <5.942818e-16 |
| Remainder R_1 | <3.303953e-17 | <1.893174e-16 |
| Mean coupled ratio bound | <0.455778 | <0.348908 |

With R=10 and R-r=2, formula (5) gives
\[
 K<3.489078,\qquad K\tau<0.03489078,
 \qquad \pi/2-K\tau>1.53590.                                    \tag{10}
\]
The same outer-wall data also give the following comparison:

| Payment from the same source jets and wall floors | Upper bound for the modulus of A |
| --- | ---: |
| Maximum uncentered ratio on the arcs | 7.915456 |
| Arc average of the uncentered ratio | 5.211239 |
| Arc average of H_z+(3/10)H divided by the wall floor | 3.489078 |

All three payments pass the phase condition. The coupled numerator
sharpens the bound by about 33% relative to the averaged uncentered
payment; it is **not necessary for the zero-charge conclusion in this
example**. These are comparisons of proved majorants, not measurements
of the true maximum |A| or optimality claims. No extra source values are
acquired for the comparison.

For each real cap t=−1/100 and +1/100, complete source integration gives
the signs at z=28,29,41,43 as +,−,−,+, respectively. For readability,
the exact receipt enclosures are contained in these coarse intervals:

| t | H(t,28) | H(t,29) | H(t,41) | H(t,43) |
| --- | --- | --- | --- | --- |
| −.01 | (2.5711,2.5712)e-5 | (−5.0470,−5.0469)e-5 | (−1.6993,−1.6992)e-6 | (7.2181,7.2182)e-7 |
| +.01 | (2.4612,2.4613)e-5 | (−5.1237,−5.1236)e-5 | (−1.6742,−1.6741)e-6 | (7.3246,7.3247)e-7 |

The intermediate value theorem supplies one real root in each of
(28,29) and (41,43), both inside the inner disk. The total root count
two then proves there are exactly these two roots, each simple. Their
gap is greater than 12, so both cap discriminants exceed 144. This sign
proof does not require numerically locating a critical point or dividing
by an unknown internal gap.

Note 05 now applies: the integrating-factor primitive has positive real
derivative, every possible event is real, and at most one event can
occur. The two positive cap signs give Q_B=0. In fact a positive left
cap alone, followed by the real monotonicity in Note 05, suffices in this
proper phase-controlled window; the right cap was also acquired to
check the declared two-cap contract. The nonzero complex time caps are
a consequence of the theorem, not additional assumed boundary data.

The computation uses 4,146 complete integrals: 2 times 129 anchors
times 16 jets, ten complete moments, and eight real-cap values. The
receipt records precision, callbacks, elapsed time, enclosures and hashes.
It contains no large derived arrays. Regenerated-array hashes identify
this run's data and are not proof steps or portability guarantees.

## 5. Collision controls and scope

The same Taylor-wall and spatial-winding consumer is applied to
\(H_c(t,z)=(z-71/2)^2-2t+c\), with c=0,−1,+1, on the same circles
and time rectangle. High-order remainders vanish exactly. Each has count
two on both circles and passes the paid phase bound. Its exact A=0 and
\(\Delta=8t-4c\) give:

| c | Left and right cap discriminants | Charge |
| --- | --- | ---: |
| 0 | −2/25, +2/25 | 1 |
| −1 | 98/25, 102/25 | 0 |
| +1 | −102/25, −98/25 | 0 |

Thus the actual geometry and phase consumer admit a collision. The
charge-zero case fails on the event control because its cap signs differ.
The negative/negative case also confirms that zero charge does not imply
real spatial roots without an additional real-root input.

The [broader controls][controls] keep their precise failed premises.
Euler-factor controls alter the theta Euler data. Weighted-square and
finite-prime controls fail the conjunction of unchanged coefficients
and complete normalized reflection. Reflected and smooth/positive-primitive
controls lack the canonical theta source. The close endpoint sources in
[BW10 Note 05][close] fail ordinary Dirichlet-series arithmetic. None is
assigned this run's theta source values or error bounds. Near their
ordinary double events, the generic two-root theorem may apply and
correctly return charge one; its same-sign case then fails. The cubic
three-root controls fail the two-root contract.

The positive source majorants alone did not provide our cap signs or
wall floors: complete oscillatory source values did. These finite values
can distinguish this particular theta window while controls collide on
different windows. This is not a new qualitative property distinguishing
theta from every colliding family.

## 6. Disposition and next obligation

RCH-09 records this completed finite application. RCH-07 is now partially
met: source-paid walls, phase and signs exist for one declared window;
the source-specific estimate at arbitrary height or near a possible
endpoint double remains open. RCH-08 retains its proved-in-note status.

This is a wider spatial disk than Note 03's thin box, but it is still
a well-separated low-height pair. The gap lower bound 144 is not a
model of a shrinking endpoint gap. A generic phase bound may remain
regular at a double while the sign information degenerates; the c=0
control proves that this possibility is real.

The next analytical step should address that degeneration: control the
complete-source signed discriminant or the location of a unique event
in a proper two-root window without assuming a positive gap at the
candidate time. A proved event on an entirely negative-time subinterval
could exclude a second endpoint event by Note 05, but no such new theta
location estimate is supplied here. Many-root windows and height-uniform
wall/collar control also remain open. HMC-05 remains open and HMC-06 gated.

Do not launch routine mesh refinement or a wider height scan from this
successful application. Any further calculation should first specify
which unresolved sign/location estimate or coverage question it decides.
The [internal review][review] audits the proofs and the implementation;
it does not turn same-assistant validation into independent review.

[n01]: 01_BOUNDED_THETA_CHARGE_AND_DIRECT_COMPARISON_20261021.md
[n05]: 05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
[plan]: ../numerics/REAL_CAP_APPLICATION_PLAN_20261021.json
[script]: ../numerics/certify_real_cap_application.py
[receipt]: ../numerics/REAL_CAP_THETA_APPLICATION_20261021.json
[review]: ../reviews/06_COMPLETE_THETA_REAL_CAP_APPLICATION_REVIEW_20261021.md
[close]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a14]: ../../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
[polymath]: https://arxiv.org/html/1904.12438v2#S1
[acb]: https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral
