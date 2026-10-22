# Quantitative windows at a possible double and pointwise height coverage

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded team model **gpt-6-astra
(Codex)**, reasoning effort **ultra**, supplied from the root turn metadata.
A delegated derivation in the same model family; separate same-model
checks are recorded in [Review 08][review], without specialist validation.

**Status: proved in-note, with explicit dependence on the local second
jet and complete theta moments.** Every hypothetical exact double of the
complete theta function at any finite real position admits an explicitly
specified proper two-root spacetime window, including quantitative floors
on both spatial walls and a strict phase margin. No internal separation
is assumed. The construction applies at every finite height separately;
its radii and time widths may tend to zero with height. The cap signs at
an assumed double are quantitatively opposite, so the window has charge
one. This is payment of the local geometric hypotheses, not endpoint
exclusion or a distinguishing theta sign.

The actual gain is the formula for the window in (5), not a new equivalent
criterion for simplicity. Read the [result index][results], [local heat
geometry cluster][local], [collision controls][controls] and [avoid
index][avoid], especially [target classification][a01], [matched control
premises][a02], [scope][a07] and [hypothesis auditing][a14]. The inherited
analytic consumer is [Note 05][n05]; [Note 06][n06] remains the finite
source-certified application. No new numerical acquisition is performed.

## 1. Complete source bounds and the exact-double hypothesis

Use the unchanged complete theta source and heat normalization
\[
 H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du,
 \qquad H_t=-H_{zz}.
 \tag{1}
\]
Here Phi is the full positive series in the endpoint overview; no mode
or tail is removed. For fixed positive numbers T_0,R_0 define
\[
 B_j=\int_0^\infty\Phi(u)u^j e^{T_0u^2}\cosh(R_0u)\,du,
 \qquad j=2,3.
 \tag{2}
\]
These are finite and positive. Super-exponential source decay gives
holomorphy in both complex variables, reality symmetry, differentiation
under the integral, and
\[
 |\partial_z^jH(t,z)|\le B_j
 \quad(\Re t\le T_0,\ |\Im z|\le R_0),\qquad j=2,3.
 \tag{3}
\]
For every real a this bound is independent of a: the real oscillation is
bounded by the same cosh envelope. The height dependence below enters
through the local jet, not through an omitted high-height source tail.
A future numerical evaluation of (2) must retain all omitted-mode and
exterior-integral errors, as in Notes 01 and 06.

For the principal theorem assume, conditionally,
\[
 H(0,a)=H_z(0,a)=0,\qquad
 c=\tfrac12H_{zz}(0,a)\ne0,\qquad q=|c|>0,
 \qquad a\in\mathbb R.
 \tag{4}
\]
Thus the putative endpoint has spatial multiplicity exactly two.
Neither RH nor a lower bound for a positive-time root gap is needed for
the local theorem. RH supplies the program's interpretation of this
real endpoint as a possible zeta multiple zero. The nonzero number q is
not an assumed interior joint-jet floor: H and H_z both vanish at the
center. It is precisely the nondegeneracy already included in the
phrase “exact double.” A higher multiple zero has q=0 and is outside this
theorem.

## 2. Explicit spatial and complex-time geometry

Set
\[
 \boxed{
 R=\min\{R_0/2,q/B_3\},\qquad r=R/2,\qquad
 h=\min\left\{T_0/2,\frac{qR^2}{16\sqrt2 B_2},
                         \frac{R^2}{128}\right\}.}
 \tag{5}
\]
All three numbers are strictly positive. Let
\[
 \overline D_h=\{t:|\Re t|\le h,\ |\Im t|\le h\}.
 \tag{6}
\]
In particular |t|<=sqrt(2)h<T_0 on this rectangle. The factor sqrt(2)
in (5) pays its corners; a real-time width is not silently reused as a
complex-time modulus bound.

**Theorem.** Under (1)–(4), for every t in the closed rectangle (6),
H(t,.) has exactly two roots, counted with multiplicity, inside each
circle |z-a|=r and |z-a|=R. Both walls satisfy
\[
 |H(t,z)|>\tfrac12q s^2
 \quad (|z-a|=s,\ s=r,R).
 \tag{7}
\]
Thus both outer roots lie inside the inner disk, and the entire annular
collar is zero-free. On the outer wall,
\[
 |H_z(t,z)|<3qR.
 \tag{8}
\]
Consequently the regular discriminant coefficient of Note 05 obeys
\[
 |A(t)|\le M_A:=96/R^2,\qquad
 M_Ah\le3/4<\pi/4<\pi/2.
 \tag{9}
\]
The proper two-root and phase hypotheses hold on a neighborhood of the
closed product. No root outside this cluster is discarded.

**Proof.** For w with |w|=s<=R, Taylor's integral remainder at time zero,
using (3), gives
\[
 |H(0,a+w)-cw^2|\le B_3s^3/6\le qs^2/6.
 \tag{10}
\]
For a complex t in (6), integrate H_t=-H_zz along the straight path
v t, 0<=v<=1. Its real part stays below T_0, so
\[
 |H(t,a+w)-H(0,a+w)|\le|t|B_2
 \le\sqrt2hB_2\le qR^2/16=qr^2/4.
 \tag{11}
\]
At either s=r or s=R, combining (10)–(11) yields
\[
 |H(t,a+w)-cw^2|
 \le qs^2/6+qr^2/4\le5qs^2/12<qs^2.
 \tag{12}
\]
Rouche's theorem therefore gives exactly two roots inside *each* circle,
with no zeros on either circle. The same inequality gives the stronger
floor 7qs^2/12, which implies (7). At the outer circle it gives
37qR^2/48, but the weaker common bound (7) is sufficient. Counting both
circles is essential: it excludes additional roots in the collar.

Differentiate the spatial Taylor expansion once, with its independent
integral remainder, and then integrate H_zt=-H_zzz in time:
\[
 \begin{split}
 |H_z(t,a+w)|
 &\le 2qR+\tfrac12B_3R^2+\sqrt2hB_3\\
 &\le\left(\tfrac52+\frac{\sqrt2}{128}\right)qR<3qR,
 \qquad |w|=R.
 \end{split}
 \tag{13}
\]
Here R B_3<=q and h<=R^2/128 were used together; no additional time
majorant is needed.

Apply Note 05's complete contour formula to the resulting monic
quadratic P and zero-free unit U. On the outer circle, |P|>=(R-r)^2.
With delta_wall=qR^2/2 and L=3qR, its bound is
\[
 |A|\le\frac{4RL}{\delta_{\rm wall}(R-r)^2}
       =\frac{96}{R^2}.
 \tag{14}
\]
The last restriction in (5) gives (9). The strict positive floors and
the strict phase margin persist after a sufficiently small enlargement
of the closed rectangle, by compactness and continuity. Holomorphy is
global. The same argument-principle counts then continue to that
neighborhood, meeting Note 05's boundary contract. This proves the
claim. ∎

The coefficient bound includes the complete H on its contour. It has
no factor 1/|z_1-z_2|. Its explicit inverse square R is an exterior-collar
cost. The source-paid choice R<=q/B_3 guarantees this collar without
assuming an independent exterior-zero separation. It can be much smaller
than the maximal actual collar; no optimality is claimed. Dividing by q
in the construction is legitimate only for an exact double. It does
not amount to a uniform lower bound for q across heights or sources.

## 3. Cap margins and the charge of the hypothetical event

The selected scalar observable is the existing complete contour
quantity
\[
 S_k(t)=\frac1{2\pi i}\oint_{|\zeta-a|=R}
          (\zeta-a)^k\frac{H_z}{H}(t,\zeta)\,d\zeta,
 \qquad \Delta(t)=2S_2(t)-S_1(t)^2.
 \tag{15}
\]
It is holomorphic despite individual root labels possibly branching.
The theorem pays its whole contour and its regular transport coefficient.
It does not supply a signed lower estimate distinguishing theta from a
colliding control.

Under (4), Delta(0)=0. The inherited exact equation
Delta'=8+A Delta and reality symmetry give, on real time,
\[
 \Delta(t)=8\int_0^t
          \exp\left(\int_s^t A(v)\,dv\right)\,ds.
 \tag{16}
\]
For K=M_A define
\[
 L_K(x)=\frac8K(1-e^{-Kx}),\qquad
 U_K(x)=\frac8K(e^{Kx}-1),\qquad x\ge0,
 \tag{17}
\]
with their continuous values 8x when K=0. The coefficient norm bounds
the real exponential in (16), hence
\[
 L_K(h)\le\Delta(h)\le U_K(h),\qquad
 -U_K(h)\le\Delta(-h)\le-L_K(h).
 \tag{18}
\]
In particular both real caps have explicit nonzero margins. We also have
the simpler lower margin L_K(h)>=8h e^{-Kh}>0. Note 05 now implies
\[
                         Q_{D_h\times\{|z-a|<R\}}=1.
 \tag{19}
\]
The unique event is the assumed one at (0,a), and all complex time caps
are event-free. This sign calculation is an audit of the construction:
any proposed use of these same premises to obtain charge zero would be
incorrect. A smaller absolute coefficient bound only narrows the
quantitative interval in (18); it does not reverse either sign.

## 4. A directly checkable off-event version

The same estimates give an event-permitting contract without asserting
that an exact double has already been located. At any real center a put
c_0=H(0,a), c_1=H_z(0,a), c_2=H_zz(0,a)/2, q=|c_2|>0.
Choose 0<r<R<=R_0 and h>0 with sqrt(2)h<=T_0. For s=r,R define
\[
 d_s=qs^2-|c_0|-s|c_1|-B_3s^3/6-\sqrt2hB_2.
 \tag{20}
\]
If d_r,d_R>0, both spatial counts are exactly two throughout the closed
rectangle, by the same Rouche comparison with c_2(z-a)^2. The floors
are at least d_s. Furthermore
\[
 L=|c_1|+2qR+B_3R^2/2+\sqrt2hB_3,
 \qquad K=\frac{4RL}{d_R(R-r)^2}
 \tag{21}
\]
is a valid coefficient bound. If Kh<pi/2, the full two-root phase
consumer applies. The signs of (15) on the real caps remain to be
established independently; they are not part of assumptions (20)–(21).

These are finite inequalities in complete source jets and moments. They
can in principle be evaluated with outward-rounded source enclosures.
A lower enclosure for q and upper enclosures for the error terms are
needed; exact event equalities cannot be inferred from an inconclusive
interval. This note supplies no such numerical claim at an unknown
candidate event. The exact-double recipe (5) proves that these geometric
inequalities have strictly feasible local values whenever (4) holds,
including at arbitrarily small internal root separation.

## 5. What height coverage is now paid

Choose T_0,R_0 once. The moments B_2,B_3 in (2) then apply to **every
finite real center a**. For every a satisfying (4), the formula (5)
returns positive radii and a positive time width. Thus there is no
uncovered finite-height regime for the *existence of a quantified local
two-root geometry*. This is a universal, parameterized implication,
not a numerical scan and not a claim that any theta double exists.

No positive infimum of q(a), R(a) or h(a) over all hypothetical high
doubles is proved. In fact, the decay of this particular prescription
can be made explicit. Put f(u)=u^2 Phi(u) and
C=||f'||_1/2<infinity. Integration by parts, with the complete source
and its decaying derivative, gives for every a!=0
\[
 q(a)=\tfrac12\left|\int_0^\infty f(u)\cos(au)\,du\right|
      \le C/|a|.
 \tag{22}
\]
Consequently along any hypothetical unbounded sequence of exact doubles,
this recipe satisfies R<=C/(B_3|a|) and
h<=C^3/(16 sqrt(2) B_2 B_3^2 |a|^3), so its windows shrink.
These are upper bounds on the conservatively selected widths, not
asymptotics of theta gaps or an obstruction to a better window rule.
An absolute source error budget fixed independently of height need not
resolve q or the signed cap margin at those scales.

On a bounded real interval the zero set of H(0,.) is finite, since the
entire function is nonzero identically (H(0,0)>0). Consequently the
constructed windows for the exact doubles in that interval, if any,
have a positive minimum radius and time width. That compactness statement
does not compute the minima or identify those doubles. Across unbounded
height no uniform compactness conclusion is available.

A future exclusion theorem does **not** need one common negative time
cap for all heights. It can work pointwise, provided its signed estimate
is proved for every possible a and all dependencies in (5), or for some
other fully paid window at that a. A sign theorem that only holds above
a fixed window size, at a fixed positive q, or on a finite list of caps
would leave a regime uncovered. Establishing source signs uniformly over
this parameterized contract is still the substantive ECE-04 obligation.

This distinction avoids demanding a height-independent collar that the
logical argument does not require, while retaining every actual
quantifier needed to assemble an all-height exclusion. Higher
multiplicity is separate: q=0 makes the present formula inapplicable,
and the remaining birth roots cannot be treated as a bounded exterior
for a selected pair.

## 6. Optional event-time enclosure from coefficient information

This elementary bound records exactly what a coefficient norm can say
about location once a real event is known to exist. Suppose a proper
phase-controlled window contains an event at s<t_* and
|A|<=K on [s,t_*]. Put delta=Delta(t_*)>0 and d=t_*-s. Then
\[
 L_K(d)\le\delta\le U_K(d).
 \tag{23}
\]
If 0<delta_-<=delta<=delta_+ and K delta_+<8, inversion gives
\[
 \frac{\log(1+K\delta_-/8)}K
 \le d\le
 -\frac{\log(1-K\delta_+/8)}K.
 \tag{24}
\]
Thus the event lies in
\[
 \left[t_*+\frac{\log(1-K\delta_+/8)}K,
       t_*-\frac{\log(1+K\delta_-/8)}K\right].
 \tag{25}
\]
For K=0 the continuous limiting interval is
[t_*-delta_+/8,t_*-delta_-/8]. If K delta_+>=8, the coefficient
norm supplies no finite upper duration by this inversion; the known
window itself may still supply one. Event existence must be supplied by
cap signs or another argument before (25) is called an event enclosure.

The scalar bounds are sharp for the information class |A|<=K, since
constant coefficients A=+K and A=-K attain the two extremes. This
statement makes no claim that those coefficients are realized by theta.
A strict negative-time conclusion would require actual cap data strong
enough to put the upper endpoint of (25) below zero. For the assumed
endpoint double, (18) prevents that conclusion from its actual data.
This is a location consumer, not an independent signed source estimate.

## 7. Controls, task disposition and remaining work

The quadratic heat control H_c(t,z)=(z-a)^2-2t+c has A=0 and
Delta=8t-4c. At c=0 the generic Taylor proof applies using B_2=2 and any positive B_3
as valid derivative majorants (its third derivative is zero), and its exact caps
are -8h,+8h, giving charge one. Since it is not a theta source, the
literal moments (2) are not assigned to it. Replacing B_j in the proof
by valid positive derivative upper bounds gives the same geometric result;
for this quadratic choose any positive B_3 upper bound, rather than
substituting zero into the displayed ratio q/B_3. At c=-1
or +1, any proper window with h<1/2 has respectively both discriminants
positive or both negative and charge zero. The exact-double hypothesis
(4) fails for those two variants at the stated center; no contrary cap
sign is inferred from the exact-double corollary.

The normalized close endpoint controls in [BW10 Note 05][bw05] provide
the stronger all-real endpoint comparison. They are positive, even,
rapidly decaying sources with an exact double, all-real zeros for t>=0
and simple zeros for t>0, under the hypotheses recorded there. Their
own source moments and exact-double second jets therefore pay the same
local window proof, and their endpoint window also has charge one.
Their failure is ordinary Dirichlet-series arithmetic and the unchanged
complete theta identity; positivity and positive-time simplicity are
not failed premises. Uniformly close moment budgets do not establish a
uniformly close local q or a common window size.

Euler-factor controls alter the theta arithmetic; weighted-square and
finite-prime controls do not preserve the complete normalized theta
reflection-and-coefficient conjunction; reflected and smooth
positive-primitive controls lack the canonical theta source. At any
ordinary double where their own complete derivative bounds exist, the
local geometry proof accepts them and correctly retains charge one.
They must not be assigned the theta moments or theta source values.
Controls without an all-real heat slice only test this local statement,
which uses no global all-real input. Cubic birth controls fail the exact
two-root premise; the present construction does not apply to them.

The resulting task disposition is precise:

- **ECE-01:** the hypothetical exact-double quantitative window is
  complete in the parameterized scope (2)–(9), with the existing
  discriminant observable (15). Equation (20) provides a checkable
  near-event contract without an assumed internal gap. No unknown
  theta event or new source value is certified.
- **ECE-04:** pointwise geometric coverage of all finite heights is
  proved. Coverage and assembly of a distinguishing signed estimate
  remain open; no common positive width is asserted or required.
- **ECE-02 and ECE-03:** unchanged. The actual cap signs under the
  double hypothesis are the compatible signs in (18), not an
  independent contradiction. Endpoint exclusion remains unproved.
- **ECE-05 and ECE-06:** unchanged. Higher multiplicities and the final
  RH-conditional simplicity implication are not supplied by this
  two-root construction.
- **ECE-07:** the formulas, strict margins, controls and quantifiers
  above need linked internal review. No specialist review is claimed.

The next signed calculation can now state its required parameter range
against an explicit event-permitting window instead of leaving local
wall existence qualitative. Improvements to (5) would count as sharper
geometric estimates; they would not, on their own, complete ECE-02.

[n05]: 05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
[n06]: 06_COMPLETE_THETA_WALLS_AND_REAL_CAP_APPLICATION_20261021.md
[bw05]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a14]: ../../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md

[review]: ../reviews/08_ENDPOINT_CHARGE_OPENING_ROUND_REVIEW_20261021.md
