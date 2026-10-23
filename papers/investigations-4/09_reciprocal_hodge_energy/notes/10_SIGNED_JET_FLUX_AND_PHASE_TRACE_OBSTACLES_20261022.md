# Signed jet flux and the remaining physical phase trace payment

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified by the parent chat. Internal same-model
analysis; no specialist review, negative theta certificate, or exclusion.

**Outcome:** the derivative-weighted energy does enter an exact signed
physical trace formula after replacing the phase density Q/E by its
amplitude-weighted version Q/sqrt(E). All top and side payments can be
eliminated by a declared cutoff, leaving a signed modulus potential
minus a nonnegative derivative-weighted bulk mass. A complete upper on
the bulk mass gives a *lower* bound on the signed trace. A negative-trace
witness instead needs an upper bound, available from the signed modulus
potential or from a separately paid lower bulk mass. No negative value
has been established for canonical theta.

The signed potential has a root-free linear source-error bound. The full
half-domain trace does not inherit the whole-plane cutoff Lipschitz
bound: an exact all-real positive-time quadratic family has a logarithmic
trace sensitivity. Thus the original unweighted phase and BW10 physical
transverse remainder still need their own denominator and trace payment.

Read the [result index](../../../../result-summaries/README.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), especially patterns
[01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../avoid/08_normalization_and_constant_slips.md) and
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
The finite source-to-potential error bound is the quantitative milestone;
the exact sign implication is a diagnostic, not a new RH result.

## 1. The physical jet supplies a holomorphic modulus potential

At a fixed real heat time let H be real entire, and extend the physical
jet to the spatial complex plane by

\[
 J(z)=H(z)+iH_z(z),\qquad u(z)=|J(z)|,
 \quad E(x)=H(x)^2+H_x(x)^2,
 \quad Q(x)=H_x(x)^2-H(x)H_{xx}(x).                    \tag{1}
\]

Write z=x+iy. At physical points with E>0,

\[
 \partial_yu(x,0)=\frac{Q(x)}{\sqrt{E(x)}},\qquad
 \rho(x)=-\partial_x\arg J(x)=\frac{Q(x)}{E(x)}.       \tag{2}
\]

Indeed u_y=Re(iJ' conjugate(J))/|J|, and
Im(J' conjugate(J))=HH_{xx}-H_x^2=-Q. Thus u_y is a signed
amplitude-weighted physical phase density. It retains Q's sign, but it
is not the phase density rho or its topological cap integral.

The distributional identity from [Note 08](08_DERIVATIVE_WEIGHTED_ENERGY_AND_GLOBAL_STRIP_BOUND_20261022.md)
is

\[
 \Delta u=\mu_J:=\frac{|J'|^2}{|J|},\qquad
 W_J(\Omega)=2\int_\Omega\mu_J\,dA.                    \tag{3}
\]

No point mass is hidden at a zero of J. Every finite multiplicity is
locally integrable. The canonical complete-source moments give

\[
 |J_z(t,x+iy)|\le M_{1,Y}(S)+M_{2,Y}(S)
       \quad(|t|\le S,\ |y|\le Y).                    \tag{4}
\]

Consequently W_J on every fixed finite rectangle has an explicit source
upper independent of an interior E floor. This uses J as a holomorphic
spatial function; J is not holomorphic in the real spacetime (t,x) plane.

## 2. Complete upper-half-strip Green formula

Fix a real center C, half-width L>0 and height h>0. Let
Omega=(C-L,C+L) x (0,h). Choose real C^2 functions psi(x), chi(y) with
psi=psi'=0 at x=C+-L and

\[
 \chi(0)=1,\qquad \chi'(0)=\chi(h)=\chi'(h)=0.
\]

Put phi(x,y)=psi(x)chi(y). Green's second identity, with the outward
bottom normal -partial_y, gives

\[
 \boxed{T_\psi(J):=\int\psi(x)\frac{Q(x)}{\sqrt{E(x)}}\,dx
       =P_\phi(J)-M_\phi(J),}                          \tag{5}
\]
\[
 P_\phi(J)=\int_\Omega |J|\Delta\phi\,dA,
 \qquad M_\phi(J)=\int_\Omega\phi\frac{|J'|^2}{|J|}\,dA.
                                                               \tag{6}
\]

The side and top terms vanish because both phi and its normal derivative
vanish there. At the bottom phi=psi and phi_y=0; hence
integral(phi Delta u-u Delta phi)=-integral psi u_y, giving (5).
For chi'(0) not zero one must add the bottom term
chi'(0) integral psi u(x,0) dx to the right of (5). It is zero only by
the declared cutoff choice.

At boundary zeros of J, excise small disks. The added arc flux is
O(epsilon^m) for an m-fold zero. The removed straight-edge integral
converges because |u_y|<=|J'|. Thus (5) remains valid through arbitrary
physical jet zeros, with the trace understood almost everywhere. No
endpoint positivity or common-zero exclusion is assumed.

For psi,chi>=0 with both bounded by one, M_phi>=0 and

\[
 P_\phi(J)-\tfrac12W_J(\Omega)
                  \le T_\psi(J)\le P_\phi(J).           \tag{7}
\]

This states the direction of the energy payment. A source upper on W_J
improves the lower endpoint in (7). To prove a negative-Q witness via
an upper endpoint, the simplest sufficient certificate is
P_phi(J)<0; alternatively retain a separately paid lower M_phi.
If psi changes sign, the exact formula (5) remains valid, but positivity
cannot be dropped: only |T-P|<=||phi||_infinity W_J/2 follows directly.

For the rectangle and canonical source, the complete boundary bound is

\[
 W_J(\Omega)\le4(2L+h)
                      [M_{1,h}(S)+M_{2,h}(S)].           \tag{8}
\]

Its perimeter is 4L+2h, and (8) is twice the boundary derivative-norm
payment. Every physical bottom, top and side is charged in this upper,
even though their cutoff-weighted terms vanish in (5). Root gaps,
critical-value floors and real-root assumptions are absent.

The generic absolute trace bound
|T_psi|<=||psi||_1 sup_physical|J'| is also available to the matched
direct method. Formula (7) does not automatically improve that bound.
The possible useful signed information lies in a complete P_phi and a
correlated/lower M_phi, not merely another generic derivative upper.

## 3. A scale-independent complete source-error payment

For any holomorphic approximant Jhat with
sup_Omega |J-Jhat|<=epsilon_J,

\[
 \boxed{|P_\phi(J)-P_\phi(\widehat J)|
                   \le\epsilon_J\|\Delta\phi\|_1.}       \tag{9}
\]

Keep the signed Delta phi in the finite integral; use its absolute norm
only to pay the approximation error. This bound needs neither a root
count nor a lower |J|. Unlike (9), no universal linear source-error bound
for the full T or M_phi is claimed.

An explicit nonnegative C^2 cutoff is

\[
 \psi(x)=\left(1-\frac{(x-C)^2}{L^2}\right)_+^3,
 \qquad \chi(y)=\left(1-\frac{y^2}{h^2}\right)^3
                       \quad(0\le y\le h).              \tag{10}
\]

Both choices satisfy all boundary conditions above. Direct integration
and variation of the first derivatives give

\[
 \|\psi\|_1=\frac{32L}{35},\quad
 \|\psi''\|_1=\frac{384}{25\sqrt5 L},\quad
 \int_0^h\chi\,dy=\frac{16h}{35},\quad
 \int_0^h|\chi''|\,dy=\frac{192}{25\sqrt5 h}.
\]

For example chi''=-6(1-s^2)(1-5s^2)/h^2, s=y/h; its only interior
sign change is 1/sqrt5, and its derivative has total variation
192/(25sqrt5 h). Since Delta phi=psi''chi+psi chi'',

\[
 \boxed{\|\Delta\phi\|_1\le
  \frac{6144}{875\sqrt5}\left(\frac hL+\frac Lh\right).} \tag{11}
\]

The bound is invariant under common spatial dilation. Its minimum in
this declared family is the square choice L=h. This is a bound for the
signed potential error, not an optimized physical trace estimate.

As a no-new-acquisition consumer, use the canonical t=0 disk C=35,R=8
from [Note 04](04_ACTUAL_REGULAR_THETA_FIBER_COMPARISON_20261022.md),
choose L=h=4sqrt2 and Jhat=P_64+iP_64', retaining every coefficient ball.
The existing complete Taylor tails give epsilon_H<1.384e-20 and

\[
 \epsilon_{H'}=\frac{33}{4}\epsilon_H,
 \qquad \epsilon_J\le\epsilon_H+\epsilon_{H'}
                  <1.2802\times10^{-19}.
\]

The ratio follows exactly from the declared rho=1/2, outer radius16,
N=65 geometric tails. Thus

\[
 |P_\phi(J)-P_\phi(\widehat J)|<8.05\times10^{-19}.       \tag{12}
\]

This pays only the complete analytic source replacement. The signed
finite-modulus quadrature, coefficient balls, and any lower bulk mass
still need their own enclosures. No sign of P_phi or T has been acquired.

## 4. Why the half-domain trace is not Lipschitz at a collision

For the elementary holomorphic functions f_a(z)=z-ia, a>0, on a fixed
real interval [-R,R], the field error from f_0 is exactly a, whereas

\[
 \int_{-R}^R\partial_y|f_a(x,0)|\,dx
       =-2a\operatorname{arsinh}(R/a)
       =-2a\log(1/a)+O(a).                              \tag{13}
\]

The f_0 trace is zero almost everywhere. This disproves a uniform
Lipschitz estimate for the normal modulus trace from a field sup error.
It does not contradict the whole-plane compact-cutoff bound: the latter
has no bottom boundary trace. In (5), the half-domain bulk mass shares
the logarithmic sensitivity and cannot simply be assigned that stronger
whole-plane error budget.

The same obstruction occurs within an exact physical all-real heat
family. Take H(t,z)=z^2-2t and set a=2t>0. Then

\[
 J_a(z)=z^2-a+2iz,\quad
 \frac{Q_a(x)}{\sqrt{E_a(x)}}=
 \frac{2(x^2+a)}{\sqrt{(x^2-a)^2+4x^2}}.                \tag{14}
\]

For a smooth compact psi identically one near zero,

\[
 T_\psi(J_a)-T_\psi(J_0)=2a\log(1/a)+O(a),\qquad
                 \|J_a-J_0\|_\infty=a.                 \tag{15}
\]

For completeness, split the real interval into |x|<=a, a<|x|<delta
and its exterior, with delta fixed inside the psi=1 region. The inner
part is O(a), because the trace integrand is bounded by |J_a'|. On the
exterior ordinary differentiation in a gives O(a). In the middle,
expanding the square root of
D_a^2=D_0^2-2ax^2+a^2 gives the trace difference

\[
 \frac a{|x|}
 +O\left(a|x|+\frac{a^2}{|x|}+\frac{a^3}{|x|^3}\right).
\]

The remainder integrates to O(a), while the two main pieces integrate
to 2a log(1/a)+O(a). The expansion is uniform for a<=|x|<=delta because
|(-2ax^2+a^2)/D_0^2| stays below a fixed constant less than one for small
a. All t>0 slices have two simple real roots; the limit has the endpoint
double. Thus all-real positive-time evolution alone does not restore the
missing Lipschitz trace estimate.

## 5. Original phase and sibling remainder obligations

The source-to-trace relation above controls
T_psi=integral psi sqrt(E) rho, not integral psi rho. Dividing the weight
by sqrt(E) in order to recover rho changes phi and Delta phi and restores
inverse-E and derivative payments. A bound on W_J alone cannot supply
those. Scaling H by lambda>0 scales W_J, P_phi and T_psi by lambda,
while rho and every phase increment remain unchanged. Canonical
normalization forbids changing the actual field, but this model shows
that any homogeneous-energy-to-phase comparison needs an additional
amplitude input; that input has not been proved by changing the formula.

[BW09 Note 03](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/03_ROOT_FOLLOWING_WALLS_AND_CAP_COUNT_20261020.md)
counts cap turns of the unweighted phase. Its exact pi budget is not
replaced by T_psi. A strictly negative T for nonnegative psi would imply
Q<0 somewhere, as does the already documented localized signed-Q
consumer in [BW09 Note 05](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/05_TOPOLOGICAL_ALTERNATIVES_AND_ENERGY_OBSERVATIONS_20261020.md).
The condition P_phi<0 is one sufficient way to get that witness; it is
not known for the canonical source and is stronger than merely asking
T<0 because M_phi>=0 may mask a negative T.

[BW10 Note 21, MT12](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md)
uses the physical denominator E(t,x) in a transverse average of
Q(t,x,y). That numerator is built from |H|^2, whereas (5) uses |J|.
Its exact signed remainder therefore does not become (5). The complete
trace and moving-wall payments in MT12--MT14, the heat-scale comparisons
of [Note 22](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md),
phase concentration of [Note 23](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/23_CAP_PHASE_CONCENTRATION_AND_FINITE_TIME_BASELINE_20261021.md),
and Gauss curvature density of [Note 24](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md)
retain their own denominator obligations. No signed arithmetic trace or
uniform endpoint modulus is obtained here.

Every nonzero real-entire holomorphic collision control satisfies (1)--(7)
with its own source and boundary constants. The quadratic in (14)--(15)
already has the relevant all-real positive-time regime. Euler-factor,
weighted-square/finite-prime, reflected/primitive and close endpoint
controls are not excluded by these generic identities; their separate
failed canonical premises remain those in the linked control catalogue.
No control has been granted an unchanged complete-theta moment value.

All identities and potential-source observations transfer to the equally
informed direct estimator. The useful addition is the complete signed
amplitude-weighted trace formula, its one-sided direction, the explicit
source-error consumer (12), and the exact obstacle (15). A beneficial
complete theta sign or matched numerical advantage remains open.
