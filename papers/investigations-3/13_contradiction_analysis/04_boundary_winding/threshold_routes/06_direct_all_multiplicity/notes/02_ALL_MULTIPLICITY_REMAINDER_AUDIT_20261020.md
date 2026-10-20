# All-multiplicity audit of the centered absolute-remainder payment

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
recorded parent-session reasoning effort **ultra**, inherited by this
research subagent.

**Status: proved in-note; [separate same-model internal review][review].**
No independent specialist review. The actual
[BW-01 centered-model payment][bw01] extends to every finite multiplicity
with an explicit error of order r, using complete derivatives only
through m+2. It certifies the inherited negative degree. Its symmetric
absolute-error information cannot force degree zero. This is a scoped
obstruction to that information class, not to all boundary estimates,
and it excludes no theta event. The [result summaries][results],
[local-law summary][laws], and [patterns to avoid][avoid], especially
[classification][a01], [controls][a02], and [scope][a07], govern this use.

## 1. The unchanged physical jet at exact multiplicity m

Let m>=2, let H be real analytic with H_t=-H_xx, and suppose
H^(j)(T,a)=0 for 0<=j<m and h_m=H^(m)(T,a)!=0. Derivatives here are
spatial. Take R>0 and the full real rectangle
|t-T|<=R^2, |x-a|<=R. For a positive threshold one may choose R^2<T
to keep it at positive times. Assume complete derivative envelopes

\[
 B_{m+1}\ge\sup|H^{(m+1)}|,\qquad
 B_{m+2}\ge\sup|H^{(m+2)}|,
\quad k_j=B_j/|h_m|.
\]

Analytic theta supplies these envelopes; no lower curvature floor or
division by Hxx is used. Define the heat polynomials and their absolute
coefficient sums

\[
 P_n(\tau,y)=\sum_{k=0}^{\lfloor n/2\rfloor}
 {(-\tau)^k y^{n-2k}\over k!(n-2k)!},\qquad
 b_n=\sum_{k=0}^{\lfloor n/2\rfloor}{1\over k!(n-2k)!}.       \tag{1}
\]

Thus P_0=1, partial_y P_n=P_(n-1), and
nP_n=yP_(n-1)-2 tau P_(n-2). For 0<r<=R use s=r^2 tau, x=a+r y
and the *physical*, constantly rescaled jet

\[
 F_r(\tau,y)=\left({H(T+r^2\tau,a+ry)\over h_mr^m},
                  {H_x(T+r^2\tau,a+ry)\over h_mr^{m-1}}\right),
 \qquad Q_m=(P_m,P_{m-1}).                               \tag{2}
\]

The spatial map has positive spacetime determinant r^3. The target
map has determinant 1/(h_m^2 r^(2m-1))>0, even for negative h_m.
It preserves the physical orientation dt wedge dx. The second
component is Hx, not H^(m-1); no differentiated source replaces H.

## 2. A finite-derivative remainder for every m

Put q=floor(m/2) and d_m=1/(q+1)!. On the entire square |tau|,|y|<=1,

\[
\begin{aligned}
 |F_{r,0}-P_m|&\le e_0
   =b_{m+1}k_{m+1}r+\mathbf1_{\{m\text{ even}\}}d_m k_{m+2}r^2,\\
 |F_{r,1}-P_{m-1}|&\le e_1
   =b_m k_{m+1}r+\mathbf1_{\{m\text{ odd}\}}d_m k_{m+2}r^2.       \tag{3}
\end{aligned}
\]

**Proof.** Taylor-expand H in time through q. The terms are
(-s)^k H^(2k)(T,a+x)/k!. In each, Taylor-expand spatially through
degree m-2k. All lower coefficients vanish by the exact event, the
remaining coefficient is h_m, and its spatial remainder is at most
B_(m+1)|x|^(m+1-2k)/(m+1-2k)!. The time remainder is at most
B_(2q+2)|s|^(q+1)/(q+1)! on the same rectangle. If m is odd this is
order r^(m+1), precisely the last term in b_(m+1). If m is even it
is order r^(m+2), giving the first parity term in (3). All integration
paths stay in the given rectangle, including when s<0. Apply the
same argument to Hx, whose vanishing order at the event is m-1;
its spatial derivative of order m is H^(m+1). This gives the second
line, including its opposite parity. No derivative above m+2 is
required. This proves (3).

For m=2 this is exactly BW-01's
e0=(7/6)k3 r+(1/2)k4 r^2 and e1=(3/2)k3 r.
For m=3 it gives e0=(25/24)k4 r and
e1=(7/6)k4 r+(1/2)k5 r^2. The parity switch prevents incorrectly
carrying the quadratic time remainder unchanged to all orders.

## 3. An explicit all-m boundary margin

For fixed m the continuous Q_m has no boundary zero. Indeed a common
zero P_m=P_(m-1)=0 with tau!=0 would, by the recurrence in (1),
force P_0=0. At tau=0 the common zero is only y=0.

A deliberately crude explicit lower bound on the full square boundary is

\[
 \mu_m:=\min_{\partial[-1,1]^2}|Q_m|\ge
 \ell_m:={1\over2[2m^2(m+2)]^{m-1}}>0.                    \tag{4}
\]

To check (4), set epsilon=1/(4m^2), L=2m^2(m+2). If |tau|>=epsilon,
the recurrence implies

\[
 |P_{j-1}|+|P_{j-2}|\le
 L(|P_j|+|P_{j-1}|)\quad(2\le j\le m).
\]

Starting from |P_1|+|P_0|>=1 gives |Q_m|>=1/(sqrt(2)L^(m-1)).
If |tau|<epsilon on the boundary, then |y|=1. With n=m-1, comparison
to the k=0 term in P_n gives

\[
 |P_n(\tau,\pm1)|\ge {2-\exp(n(n-1)|\tau|)\over n!}
 \ge {2\over3n!}>{1\over2n!}.
\]

Here n!/(n-2k)!<=[n(n-1)]^k, n(n-1)|tau|<=1/4 and
exp(1/4)<=1/(1-1/4)=4/3. Since L^(m-1)>=(m-1)!, both cases imply
(4). The case n=1 has an empty tail and satisfies the same bound.
This is a complete boundary proof; the smallness of ell_m is not a
claim that the true margin is comparably small.

Let eta=sqrt(e0^2+e1^2). If eta<ell_m, straight-line homotopy from
Q_m to F_r has no zero anywhere on the boundary and

\[
 \min_{\partial[-1,1]^2}|F_r|\ge\ell_m-\eta>0,
 \qquad W(\partial D_r)=-\lfloor m/2\rfloor.                 \tag{5}
\]

The degree in (5) is the [inherited physical Hermite index][index],
not a new all-multiplicity index theorem. A fully explicit sufficient
choice, with zero-denominator terms omitted, is

\[
 0<r\le\min\left\{R,
 {\ell_m\over4(b_m+b_{m+1})k_{m+1}},
 \sqrt{{\ell_m\over4d_m k_{m+2}}}\right\}.                 \tag{6}
\]

Then eta<=e0+e1<=ell_m/2. The radius depends on m and the first
nonzero derivative. It is not uniform as m increases or h_m tends
to zero. An arbitrarily high but finite multiplicity still has a
positive analytic radius. For theta, H(T,0)>0 ensures that a spatial
slice is not identically zero, so an isolated zero has finite order.

## 4. Full-source errors and the limit of the old budget

For the unchanged positive theta source in the [predecessor][predecessor],
the exact full moments

\[
 M_j(b)=\int_0^\infty u^j e^{bu^2}\Phi(u)\,du,
 \qquad b=T+R^2>0,
\]

are valid B_j. Their finiteness follows from double-exponential source
decay. Thus (3) already has a complete analytic source payment. No
Taylor series in infinitely many unbounded numerical derivatives is
assumed. The required orders m+1 and m+2 change with m; the old BW-01
budget restricted to j<=6 cannot silently supply m>=5.

For completeness an order-dependent finite-source budget can be made
explicit. Set J=m+2, choose U>=1 so that

\[
 D_J=4\pi e^{4U}-2bU-9-J/U>0,\qquad16\pi e^{4U}\ge2b.
\]

Then every real derivative moment with 0<=j<=J has all-mode exterior
u>=U bounded by

\[
 \mathcal T_J(b,U)=
 {2\pi^2 U^J e^{bU^2+9U-\pi e^{4U}}\over
 D_J(1-16e^{-3\pi e^{4U}})}.                              \tag{7}
\]

Indeed u^j<=u^J<=U^J exp(J(u-U)/U), and the resulting exponent for
mode n is concave with negative derivative at U. Its tangent gives
the reciprocal slope bound. The ratio of successive mode majorants
is at most 16 exp(-3pi exp(4U)). The dropped negative term of each
theta mode makes this an upper bound.

For omitted n>N on [0,U], put v=N+1, q0=exp(-2pi v) and
P(q0)=1+11q0+11q0^2+q0^3. A common complete upper bound is

\[
 \mathcal E_{N,J}(b,U)=
 2\pi^2 U^{J+1}e^{bU^2+9U}
 v^4 e^{-\pi v^2}{P(q_0)\over(1-q_0)^5}.                 \tag{8}
\]

This follows from (v+k)^4<=v^4(k+1)^4,
(v+k)^2>=v^2+2vk, and the exact sum of (k+1)^4 q0^k.
The retained finite integral plus its outward quadrature error plus
(7) and (8) therefore bounds M_j. The two omitted regions are disjoint.
These are existence and error formulas, not newly acquired theta
moment values. Their potentially poor cost is not evaluated here.

If physical component data have additional complete allowances
delta0,delta1, their normalized payment is

\[
 \eta_{\rm eval}=
 \sqrt{(\delta_0/(|h_m|r^m))^2+
        (\delta_1/(|h_m|r^{m-1}))^2}.                    \tag{9}
\]

It must be added where such data are used. Fixed absolute errors
become worse as r shrinks, increasingly so at high m. A numerical
approximation to h_m, uncertain T or a, or approximate lower-order
event cancellation needs its own full error propagation. None is
silently paid by (3), and none was numerically acquired in this task.

## 5. The precise obstruction and controls

For any nonnegative e0,e1, the information consisting solely of Q_m
and the symmetric component bounds in (3) includes Q_m itself.
That model has negative degree -floor(m/2). Hence no theorem valid
for every admitted boundary field can infer winding zero from this
information. When eta<mu_m every admitted curve has the same negative
degree; if the allowance is larger, Q_m still refutes a universal
zero-degree conclusion. The matched direct first-jet consumer also
cannot exclude its exact center event from these same reduced data.
This is an information comparison, not a runtime benchmark.

The obstruction covers all finite m for this *centered Hermite model
with symmetric absolute remainder payment*. It does not cover a
consumer retaining additional signed arithmetic constraints, source
identities, correlated residuals excluding the model, or a different
event-free domain. The genuine theta source is more information than
the moments retained in (3). Increasing m, derivative order, or
precision within the same information class does not supply the
missing incompatible signed theta estimate.

The [exact checker][checker] and [receipt][receipt] use asymmetric
heat-polynomial controls P_m+P_(m+1)+P_(m+2), with their own derivative
envelopes, to check the parity formulas on the finite range m=2,...,12.
Negative multiples give the same absolute payments. The all-m proof
is Sections 1--3, not that finite replay. Pure P_m has zero remainder
and supplies the counterexample inside every admitted uncertainty
class. No source integral is assigned to a polynomial.

The required [source-family screens][controls] retain their earlier
distinctions. Positive-kernel and Euler controls share heat flow and
own-source envelopes where finite; unchanged theta coefficients fail.
Weighted-square and finite-prime controls share local event and partial
arithmetic information, but full reflection or complete unchanged
coefficients fail; no finite all-real threshold is inferred. Reflected
smooth and positive-primitive controls share their established local
events and positivity, but not the complete normalized theta square
expansion. Smooth-density/two-channel auxiliary positivity does not
itself supply an exact physical event of every order. These are premise
screens, not newly invented numerical high-multiplicity events.

**Completed task:** the selected BW-01 estimate no longer depends on
Hxx!=0; its finite-derivative error and its symmetric-information
obstruction now cover every exact finite multiplicity. **Still open:**
an arithmetic boundary estimate for theta that can force the opposite
degree. No exclusion or uniform numerical coverage is claimed.

[bw01]: ../../01_local_double_winding/notes/03_PAIRED_FACE_REMAINDER_OBSTRUCTION_20261019.md
[checker]: ../numerics/check_all_multiplicity_remainders.py
[receipt]: ../numerics/ALL_MULTIPLICITY_REMAINDER_CONTROLS_20261020.json
[results]: ../../../../../../../result-summaries/README.md
[laws]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[index]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[predecessor]: ../../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex

[review]: ../reviews/01_ALL_MULTIPLICITY_REMAINDER_REVIEW_20261020.md
