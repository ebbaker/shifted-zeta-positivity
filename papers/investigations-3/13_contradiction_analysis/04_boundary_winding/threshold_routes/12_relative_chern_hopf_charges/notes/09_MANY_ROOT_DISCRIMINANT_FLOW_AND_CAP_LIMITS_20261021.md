# Many-root discriminant flow and the limit of real-cap reduction

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded parent session configuration:
**gpt-6-astra (Codex), reasoning effort ultra**; this delegated analysis
inherits that configuration. No independent specialist review or novelty
claim is made.

**Status: proved in-note for a proper finite heat cluster.** The
many-root discriminant has an exact evolution equation with a regular
complete-exterior coefficient and an explicit wall bound containing no
inverse internal gap. For three roots, its integrating-factor form is
strictly increasing on real time unless it is constant and nonzero, so
there is at most one real collision time on each real interval in the
time domain. That event can carry charge
three, and other complex-time events need not be absent. Explicit cubic
and quartic heat controls disprove the direct extension of Note 05's
phase-and-two-cap-sign charge formula to arbitrary multiplicity.

This is a structural part of ECE-05 and a precise screen of one proposed
extension. It supplies no signed theta estimate and does **not** complete
ECE-05's source-estimate transfer or exclude a theta endpoint.

Read with the [result index][results], [control register][controls] and
[avoid index][avoid], especially [classification][a01], [matched control
premises][a02] and [scoped conclusions][a07]. The gain is the explicit
regular coefficient bound and the resolved limitation of the inherited
consumer; an equivalent endpoint sign is not presented as progress.

## 1. Proper-cluster contract and notation

Let H be holomorphic on a neighborhood of the closed product of a simply
connected bounded complex-time domain D with piecewise smooth boundary
and a spatial disk |z-a|<R,
and satisfy
\[
                         H_t=-H_{zz}.                         \tag{1}
\]
For every time in the closed time domain, require exactly m>=2 spatial
roots counted with multiplicity in the outer disk, all in |z-a|<r<R,
and a nonzero outer wall. Assume strict margins or a neighborhood
extension sufficient to make these statements hold near the closed
product. When real statements are used, take a real center a, a
conjugation-invariant time domain and reality symmetry of H. No internal
root gap is assumed.

The monic cluster polynomial and nonvanishing factor are
\[
 P(t,z)=\prod_{i=1}^{m}(z-z_i(t)),\qquad H=UP,\qquad
 q=U_z/U,\qquad f=H_z/H.
                                                               \tag{2}
\]
P has single-valued holomorphic coefficients; root labels may be
multivalued. The construction by contour moments is inherited from
[Note 04, Section 3][n04]. The quotient U is holomorphic and nonzero
throughout the spatial disk. Thus q is a holomorphic record of the
entire exterior contribution, including any nonzero entire factor; it
is not a finite truncation of an exterior-root sum.

Write N=m(m-1)/2 and define
\[
 \mathfrak D=\prod_{i<j}(z_i-z_j)^2,
 \qquad
 \mathfrak T=\sum_{i<j}
       \prod_{\substack{k<\ell\\(k,\ell)\ne(i,j)}}
                       (z_k-z_\ell)^2.                        \tag{3}
\]
An empty product is one. Both expressions are symmetric polynomials
in the roots, hence holomorphic functions of the coefficients of P,
including at collisions. On the simple-root set only,
\(\mathfrak T=\mathfrak D\sum_{i<j}(z_i-z_j)^{-2}\).
The polynomial definition (3), rather than the latter quotient,
defines it at an event.

## 2. The regular many-root equation

**Theorem.** Under this contract,
\[
 \boxed{\quad \mathfrak D'=8\mathfrak T+\mathcal B\mathfrak D,\qquad
 \mathcal B(t)=\frac{2}{2\pi i}\oint_{|\zeta-a|=R}
             \frac{H_z(t,\zeta)}{H(t,\zeta)}
             \frac{P_{zz}(t,\zeta)}{P(t,\zeta)}\,d\zeta.
       \quad}                                                  \tag{4}
\]
The coefficient is holomorphic through every internal collision. For
any holomorphic scalar kappa(t), H_z may be replaced in (4) by
H_z-kappa H. If the complete wall bounds are
\[
 |H|\ge\delta>0,\qquad |H_z-\kappa H|\le L_\kappa,
                                                               \tag{5}
\]
then
\[
 \boxed{\quad |\mathcal B|\le
 \frac{2R\,m(m-1)L_\kappa}{\delta(R-r)^2}.\quad}                \tag{6}
\]
There is no inverse internal root gap. The spatial collar, wall floor,
root counts and complete numerator bound remain inputs that must be
paid for the actual source.

**Proof.** At a simple root, differentiation of H(t,z_i)=0 gives
\[
 z_i'=\frac{H_{zz}(t,z_i)}{H_z(t,z_i)}
      =2\sum_{j\ne i}\frac1{z_i-z_j}+2q(t,z_i).                 \tag{7}
\]
This is the complete motion law, consistent with
[BW10 Note 19][bw19]. For d_ij=z_i-z_j,
\[
 \frac{z_i'-z_j'}{d_{ij}}=
 \frac4{d_{ij}^2}
 -2\sum_{k\ne i,j}\frac1{(z_i-z_k)(z_j-z_k)}
 +2\frac{q(t,z_i)-q(t,z_j)}{d_{ij}}.                            \tag{8}
\]
The three contributions belonging to any unordered triple in the
double sum cancel exactly:
\[
 \frac1{(x-z)(y-z)}+
 \frac1{(x-y)(z-y)}+
 \frac1{(y-x)(z-x)}=0.                                        \tag{9}
\]
Thus logarithmic differentiation gives
\[
 \frac{\mathfrak D'}{\mathfrak D}
   =8\sum_{i<j}\frac1{d_{ij}^2}
      +4\sum_{i<j}\frac{q(t,z_i)-q(t,z_j)}{d_{ij}}.             \tag{10}
\]
The q divided differences extend holomorphically. By Cauchy's formula,
\[
 \begin{aligned}
 4\sum_{i<j}\frac{q(t,z_i)-q(t,z_j)}{z_i-z_j}
 &=\frac4{2\pi i}\oint q(t,\zeta)
       \sum_{i<j}\frac1{(\zeta-z_i)(\zeta-z_j)}d\zeta\\
 &=\frac2{2\pi i}\oint q(t,\zeta)\frac{P_{zz}}P(t,\zeta)d\zeta.
 \end{aligned}                                                \tag{11}
\]
Here P_zz/P=2 sum_(i<j) 1/((zeta-z_i)(zeta-z_j)). Replacing
q=f-P_z/P in (11) introduces the rational integral of
P_z P_zz/P^2. It is zero: all its finite poles lie inside the circle,
and the rational function is O(zeta^-3) at infinity, so its total
residue is zero. This proves the coefficient formula (4), without
omitting any exterior term. Likewise P_zz/P=O(zeta^-2), so its
circle integral is zero and the subtraction of kappa is exact.

All denominators on the circle stay nonzero. The contour expression
for B is therefore holomorphic in time. Multiply (10) by D and use
the polynomial T to obtain (4) first on the simple-root set and then
by holomorphic continuation. That set is dense: the local heat
splitting at every spatial zero has distinct Hermite leading roots,
as recalled in Section 3; the finitely many zeros in one fiber can
all be separated by taking a sufficiently small nonzero time
increment. In particular D is not identically zero.

Finally, each wall distance |zeta-z_i| is at least R-r, giving
|P_zz/P|<=m(m-1)/(R-r)^2. The contour length is 2 pi R. Applying
(5) to (4) gives (6). This argument retains the two-root collar
power rather than bounding P_zz and 1/P separately. For m=2,
T=1 and (4)-(6) are exactly the equation and wall bound of
[Note 05][n05].

### Conditional complete-theta payment at a full birth

The geometric contract is quantitatively available conditional on any
specified finite-order endpoint event, although it supplies no sign that
would exclude that event. Use the complete theta normalization and
moments of [Note 05, Section 4][n05]. Fix T_0,R_0>0 and put
\[
 B_j=M_j(T_0,R_0)
   =\int_0^\infty\Phi(u)u^j e^{T_0u^2}\cosh(R_0u)\,du.
\]
Suppose the exact spatial multiplicity at (0,a), a real, is m, and set
\[
 q_m=|\partial_z^mH(0,a)|/m!>0,\quad
 R=\min\{R_0/2,(m+1)!q_m/(4B_{m+1})\},\quad r=R/2,
\]
\[
 h=\min\{T_0/2,\ q_m r^m/(4\sqrt2 B_2)\}.
                                                               \tag{G1}
\]
All constants are positive and finite for the complete source. For
s=r or R, spatial Taylor's formula on |z-a|=s bounds the remainder
after the leading degree-m term by B_(m+1) s^(m+1)/(m+1)!, which
is at most q_m s^m/4. For |Re t|,|Im t|<=h, the complete derivative
bound |H_t|<=B_2 along the straight time segment gives
\[
 |H(t,z)-H(0,z)|\le\sqrt2 h B_2\le q_m r^m/4.
\]
The combined error is at most q_m s^m/2, strictly smaller than the
leading monomial's modulus q_m s^m. Rouche gives exactly m roots
on both disks throughout the closed rectangle and wall floors
\[
 \delta_s\ge q_m s^m/2,\qquad s=r,R.                            \tag{G2}
\]
Taking kappa=0 and |H_z|<=B_1 in (6) gives
\[
 |\mathcal B|\le\frac{16m(m-1)B_1}{q_m R^{m+1}}.                \tag{G3}
\]
This retains every source mode and tail through the complete moments.
It assumes the stated event and its nonzero order-m derivative; it
does not assume a positive internal gap. The dependence on q_m,
m and the derived R,h is explicit and can deteriorate with height.
No lower bound for q_m at unknown theta events, numerical values of
these parameters, discriminant sign, or time-boundary event exclusion
is established by (G1)-(G3). In particular these are event-compatible
wall payments, not a contradiction to the hypothesized event.

## 3. Birth order and charge

At an isolated multiplicity-m event (t_0,z_0), set s=t-t_0 and
choose a local square root s=rho^2. The inherited heat splitting is
\[
 z_i(t_0+\rho^2)=z_0+\sqrt2\lambda_i\rho+O(\rho^2),             \tag{12}
\]
where lambda_i are the distinct roots of the monic probabilists'
Hermite polynomial He_m. For clarity, this follows from the
weight-m part of the heat Taylor series:
\[
 e^{-s\partial_z^2}(z-z_0)^m
       =(2s)^{m/2}\operatorname{He}_m((z-z_0)/\sqrt{2s}).        \tag{13}
\]
Higher initial spatial Taylor terms have strictly larger parabolic
weight, so analytic root continuation in rho gives (12). The
standard simple real Hermite roots can equivalently be obtained
from their Gaussian orthogonality. These are the same inherited
normalization and local splitting used in [BW10 Note 25][bw25].
Consequently
\[
 \mathfrak D(t)=d_m s^N+O(s^{N+1}),\qquad
 d_m=2^N\prod_{i<j}(\lambda_i-\lambda_j)^2>0.                   \tag{14}
\]
The error has integer order because D is holomorphic in s. Equation
(4) and holomorphy of B then imply
\[
 \mathfrak T(t)=\frac{N d_m}{8}s^{N-1}+O(s^N).                 \tag{15}
\]
For m>2 the forcing vanishes at the full birth. The constant forcing
8 responsible for the two-root univalence proof is absent.

If D is nonzero on the entire complex time boundary, the complete
product-domain charge is the inherited finite-cluster formula
\[
 Q_{D\times\{|z-a|<R\}}=
 \frac1{2\pi i}\oint_{\partial D}\frac{\mathfrak D'}{\mathfrak D}dt
 =\frac8{2\pi i}\oint_{\partial D}\frac{\mathfrak T}{\mathfrak D}dt.
                                                               \tag{16}
\]
The integral of B vanishes because B is holomorphic on D. This does
not make the exterior contribution irrelevant: it affects D, T and
their event locations through (4). Formula (16) cannot be evaluated
by discarding B from that evolution. The full birth contributes N,
as required by the local intersection formula. Simultaneous distinct
spatial events add their individual charges.

For a real-symmetric cluster the cap signs of D can encode only the
parity of the intervening real charge, even if all events are known
to be real. They cannot recover N from a sign change when N>1, and
they do not detect an even N birth. Conjugate nonreal event pairs
also contribute even total charge without being read by two real
cap signs. Boundary nonvanishing in (16) remains an independent
condition unless another theorem supplies it.

## 4. The cubic real-time result and its complex-time limit

For m=3, write the depressed polynomial
\[
 P(t,z)=(z-c(t))^3+p(t)(z-c(t))+q_0(t).
\]
Use q_0 for the constant coefficient to distinguish it from U_z/U.
Then
\[
 \mathfrak D=-4p^3-27q_0^2,\qquad \mathfrak T=9p^2.             \tag{17}
\]
The second identity also follows without root selection: T is a
translation-invariant symmetric homogeneous polynomial of degree
four, hence a constant times p^2; roots (-1,0,1) give the constant 9.

On a real interval in D, normalize the integrating factor at a real
point and set mu=exp(-integral B)>0. Equations (4) and (17) give
\[
                         (\mu\mathfrak D)'=72\mu p^2\ge0.     \tag{18}
\]
If p is not identically zero, its real zeros are isolated, so the
integral of the right side over every nontrivial real subinterval is
strictly positive. Thus mu D is strictly increasing and there is at
most one real collision time. If p is identically zero, mu D is
constant and nonzero, since D cannot be identically zero, so there
are no collisions. A real collision can be an ordinary double with
charge one or a triple with charge three. Neither option excludes
the endpoint.

One conditional route does transfer: an independently established real
event at a strictly negative time in the same proper three-root interval
excludes a second real event at time zero. It uses the one-real-location
bound (18), regardless of possible nonreal events elsewhere in the
complex window. No such negative-time theta event or isolating interval
is proved here; a charge-three window alone does not locate one.

This real result does not extend to the full complex window merely
from a small bound on |B|. In general
\[
 (\mu\mathfrak D)'=8\mu\mathfrak T,
                                                               \tag{19}
\]
and a half-plane condition on mu does not put mu T in a half-plane.
Even for a cubic, p^2 need not have positive real part at nonreal time.
For m>=4, T need not be nonnegative even on real time, as the
quartic control below shows. This distinguishes the valid cubic
real-time corollary from an invalid assertion that all higher
multiplicities share a real monotonicity obstruction.

## 5. Exact controls for the failed extension

**Cubic with three event times.** Take
\[
 H(t,z)=z^3-6tz+2,\quad
 D=\{t:|\Re t|<1,\ |\Im t|<1\},\quad a=0,\ r=4,\ R=5.
                                                               \tag{20}
\]
It satisfies H_t=-H_zz and reality symmetry. On |z|=4 and the
closed time rectangle,
\[
 |6tz-2|\le24\sqrt2+2<64=|z^3|.
\]
Rouche therefore gives three roots strictly within the inner disk
throughout the rectangle; the outer disk has the same three roots
and a nonzero wall. All margins are strict. Here U=1 and B=0, so
any condition on the phase accumulated by B is satisfied exactly.
Nevertheless
\[
 \mathfrak D(t)=864t^3-108,\qquad
 \mathfrak T(t)=324t^2,                                      \tag{21}
\]
and the three simple event times are
\[
 \tfrac12,\qquad-\tfrac14+\tfrac{\sqrt3}{4}i,\qquad
 -\tfrac14-\tfrac{\sqrt3}{4}i.
\]
At each event z=1/(2t), so |z|=1 and the spatial multiplicity is
two. None lies on the product boundary. Thus the total charge is
three. The real cap discriminants are D(-1)=-972 and D(1)=756;
Note 05's sign-difference expression would give one, which is false
for this many-root window. This control fails the original theorem's
two-root premise. It does not refute that theorem.

**Quartic endpoint invisible to cap parity.** Take the Hermite birth
\[
 H(t,z)=z^4-12tz^2+12t^2                                    \tag{22}
\]
on the same time rectangle, with r=5 and R=6. The inner-wall bound
\[
 |12tz^2-12t^2|\le300\sqrt2+24<625=|z^4|
\]
gives the proper four-root cluster. Again B=0. Its roots are
\(\pm\sqrt{(6+2\sqrt6)t},\ \pm\sqrt{(6-2\sqrt6)t}\), and
\[
 \mathfrak D(t)=1{,}769{,}472\,t^6,\qquad
 \mathfrak T(t)=1{,}327{,}104\,t^5.                            \tag{23}
\]
The unique event is the quadruple endpoint (0,0), carrying charge
six. Both real cap discriminants are positive and all time-boundary
discriminants are nonzero. Thus same-sign caps plus perfect exterior
phase control do not imply zero many-root charge. T changes sign
on the real axis. This event also satisfies all-real simple spatial
roots for positive real time, so that endpoint feature cannot repair
the invalid consumer.

For every m, the full Hermite family e^(-t partial_z^2)z^m gives
D=d_m t^N and T=N d_m t^(N-1)/8. It admits a proper finite window
by taking the spatial radius large enough. It retains the endpoint
charge N while B=0. The quadratic member gives D=8t and charge one,
recovering the required Note 05 control. The shifted quadratic
noncrossing controls still have charge zero in their original
windows; nothing here changes that decision.

These are exact algebraic checks, not a theta numerical experiment.
The broader [control register][controls] has the same logical
response: any isolated local heat cluster of the listed sources
satisfies (4), with its own complete exterior factor. Euler-factor
controls change Euler data; weighted-square and finite-prime controls
lack the full normalized coefficient/reflection conjunction and are
not assigned an all-real heat slice; reflected, smooth and
positive-primitive controls lack the canonical theta expansion;
BW10's close normalized endpoint controls fail ordinary Dirichlet
arithmetic. Fixed-event atomic controls also fail canonical theta
arithmetic, the full profile and eventual threshold simplicity.
No one of these source failures is a hypothesis of (4), so the
present identity distinguishes none of them from theta. The explicit
cubic and quartic examples suffice to refute precisely the proposed
many-root phase/cap consumer.

## 6. Centered variance is not a substitute for the discriminant

A useful check on constants, and a warning against a second shortcut,
is provided by the centered quadratic moment
\[
 c=\frac1m\sum_i z_i,\qquad
 V=\sum_i(z_i-c)^2=\frac1m\sum_{i<j}(z_i-z_j)^2.
\]
The complete root motion gives, with holomorphic continuation,
\[
 V'=2m(m-1)+4\sum_i(z_i-c)q(t,z_i).                            \tag{24}
\]
Each unordered internal pair contributes 4 to the derivative;
there are N such pairs. The source term retains q=U_z/U, and its
sum is single-valued and regular even at repeated roots. At a full
m birth V=0 and the source sum is zero, hence
\[
                     V=2m(m-1)(t-t_0)+O((t-t_0)^2).           \tag{25}
\]
This real sign transition is compatible with every Hermite birth.
It gives no contradiction.

Over complex roots V can also vanish without a collision. The cubic
(20) has V=12t, so V(0)=0 while D(0)=-108 is nonzero. On an all-real
fiber, V=0 does force full coalescence, but that fiber premise cannot
be silently imposed on an unknown negative cap. Nor does V>0 rule
out a partial collision in a larger cluster. Thus a centered moment
alone cannot inherit the discriminant's event set or charge.

## 7. ECE status and the remaining transfer obligation

The finite many-root **structural extension** is proved in (4)-(6):
it retains all roots of a birth, pays its exterior coefficient by
a complete wall bound, and reproduces the charge N. It avoids the
singular selected-pair exterior terms recorded in BW10 Note 19,
RM17. The cubic real-location corollary (18) is an additional scoped
consequence. No common negative-time all-real slice is assumed.

The scoped negative result is exact: **proper many-root isolation,
reality symmetry, arbitrarily small exterior phase, and the two real
cap signs do not determine the full charge by Note 05's formula.**
Even same positive cap signs permit a charge-six endpoint. This is
not an impossibility theorem for many-root charge estimates, other
boundary consumers, additional source information or theta-specific
arguments.

ECE-05 remains open for exclusion and transfer of the actual signed
source estimate. An eventual two-root source estimate must be shown
to control the full polynomial forcing T, the complete boundary
winding, or another genuinely multiplicity-sensitive observable;
applying it independently to outgoing pairs loses the other birth
roots. No such quantitative theta input is supplied here. ECE-02,
ECE-03, ECE-04 and ECE-06 receive no completion claim from this note.

[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[n04]: 04_ANALYTICAL_SCOPE_AND_POTENTIAL_OF_RELATIVE_CHARGE_20261021.md
[n05]: 05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
[bw19]: ../../10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[bw25]: ../../10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md

[review]: ../reviews/08_ENDPOINT_CHARGE_OPENING_ROUND_REVIEW_20261021.md
