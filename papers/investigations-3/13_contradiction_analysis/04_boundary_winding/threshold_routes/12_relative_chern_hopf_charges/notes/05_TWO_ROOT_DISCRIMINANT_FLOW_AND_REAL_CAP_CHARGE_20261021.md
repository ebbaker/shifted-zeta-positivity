# Two-root discriminant flow and reduction to real cap signs

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. Proofs and [self-review][review] are by the
authoring assistant; no independent specialist review or novelty claim.

**Status: proved in-note under the stated isolation and phase hypotheses.**
A proper two-root heat cluster has a discriminant satisfying a scalar
linear equation with analytic coefficient, defined without dividing by
the discriminant. A quantitative bound across imaginary heat time makes
its integrating-factor primitive injective. For a real-symmetric heat
family this confines every cluster collision to real time and position,
allows at most one collision, and determines the full complex charge
from two real endpoint signs. An explicit sufficient strip width uses
complete theta moments and independently established spatial-wall floors.

This is an analytical charge bound and continuation theorem, not a new
theta simplicity result. No particular theta region is asserted to satisfy
the new wall/width hypotheses in this round. No numerical experiment is
performed. The unresolved signed endpoint information is stated in §6.

Read the [result index][results], [local heat-flow cluster][local],
[control register][controls] and [avoid index][avoid], especially
[classification][a01], [scope][a07], [hypothesis audit][a14] and
[retaining coupled terms][a12]. The classification here is a quantitative
finite-window theorem; it is not a new RH-equivalent criterion.

## 1. Contract and relation to existing work

Let H(t,z) be holomorphic near a closed product and satisfy
\[
                         H_t=-H_{zz}.                           \tag{1}
\]
Write the complex time rectangle as
\[
 D=\{t=x+iy:\ t_-<x<t_+,\ |y|<\tau\},\qquad t_-<t_+,
                                                               \tag{2}
\]
and fix a real spatial center a and radii 0<r<R. Suppose for every
t in the closed rectangle, H has exactly two spatial roots, counted
with multiplicity, in |z−a|<R, both lying in |z−a|<r, and H is
nonzero on the outer circle. Require these properties on a neighborhood
of the closed product, or with the strict margins in §4, which give the
necessary local extensions. The two roots are allowed to coincide.

Preparation gives
\[
 H(t,z)=U(t,z)P(t,z),\qquad
 P(t,z)=(z-z_1(t))(z-z_2(t)),                                    \tag{3}
\]
where P is monic with holomorphic coefficients and U is holomorphic and
nonvanishing on the spatial disk. Individual root labels need not be
single-valued. Define
\[
                  \Delta(t)=(z_1(t)-z_2(t))^2.                  \tag{4}
\]
The finite-cluster construction and identification of charge with
discriminant winding are in [Note 04, §3][n04]. On the real axis the
two-root gap equation already appears in [BW10 Note 03, §8][gap], with
its complete exterior zero sum; [BW10 Note 12, §3][energy] retains that
forcing in the general cluster energy. The published root dynamics are
in [Polymath, Proposition 3.1][polymath]. We do not claim a new real
gap equation.

The addition is a holomorphic coefficient formula that stays regular at
the collision, a complex-time phase estimate, and a complete-source
criterion for reducing complex charge to real cap signs.

## 2. A coefficient with no inverse interior gap

Put q=U_z/U and f=H_z/H on the outer spatial circle Gamma_R, oriented
counterclockwise. Define
\[
 A(t)=\frac4{2\pi i}\int_{\Gamma_R}
             \frac{H_z(t,\zeta)}{H(t,\zeta)P(t,\zeta)}\,d\zeta.
                                                               \tag{5}
\]
This is holomorphic in time, including at a collision: neither denominator
vanishes on the integration circle. We do not define A by the quotient
(Delta'−8)/Delta, which would hide the desired regularity.

For distinct roots, the Cauchy formula and
f=q+P_z/P give
\[
 \frac{q(t,z_1)-q(t,z_2)}{z_1-z_2}
 =\frac1{2\pi i}\int_{\Gamma_R}\frac{q(t,\zeta)}{P(t,\zeta)}d\zeta
 =\frac1{2\pi i}\int_{\Gamma_R}\frac{f(t,\zeta)}{P(t,\zeta)}d\zeta.
                                                               \tag{6}
\]
The polynomial term disappears exactly because
\(\int_{\Gamma_R}P_z/P^2=-\int_{\Gamma_R}(1/P)_z=0\).
At coincident roots the divided difference extends to q_z.

At a simple spatial root, (1) gives z_i'=H_zz/H_z, hence
\[
 z_1'=\frac2{z_1-z_2}+2q(t,z_1),\qquad
 z_2'=\frac2{z_2-z_1}+2q(t,z_2).
\]
Differentiating (4) and using (6) yields
\[
                   \boxed{\Delta'=8+A\Delta.}                   \tag{7}
\]
Both sides are holomorphic, so the equality continues across collisions.
Delta cannot be identically zero: if P=(z-c(t))^2 throughout a time
neighborhood, then H_t(t,c(t))=0 while H_zz(t,c(t))=2U(t,c(t)) is
nonzero, contradicting (1). Thus the distinct-root set used in the
derivation is nonempty and dense.

At every zero t_0 of Delta,
\[
                         \Delta'(t_0)=8.                        \tag{8}
\]
Every event in this two-root cluster is consequently an ordinary double
event with local charge one. The constant 8 uses the normalization (1).
Rescaling heat time would change it.

If |H|>=delta>0 and |H_z|<=L on the whole time-dependent outer wall,
the spatial collar gives |P(t,zeta)|>=(R−r)^2 there, so
\[
                  |A(t)|\le K:=\frac{4RL}{\delta(R-r)^2}.        \tag{9}
\]
There is no factor 1/|z_1−z_2| in this bound. The cost is separation of
the cluster from its exterior and a proved wall floor, rather than
separation of its two members. These hypotheses are independent of an
interior collision: the quadratic collision control below satisfies them.

One exact cancellation can be retained in a sharper source estimate.
For any holomorphic scalar kappa(t),
\[
 A(t)=\frac4{2\pi i}\int_{\Gamma_R}
       \frac{H_z(t,\zeta)-\kappa(t)H(t,\zeta)}
            {H(t,\zeta)P(t,\zeta)}\,d\zeta,                    \tag{10}
\]
since the integral of 1/P is zero. Thus a coupled estimate on the
displayed numerator can replace L in (9). Choosing kappa is not by itself
an improvement; a complete estimate of that numerator must be supplied.

## 3. Phase control, injectivity and the charge

Choose a real t_* in the time interval and set
\[
 J(t)=\int_{t_*}^t A(s)\,ds,\quad
 \mu(t)=e^{-J(t)},\quad
 \Psi(t)=\int_{t_*}^t\mu(s)\,ds.                                \tag{11}
\]
All primitives are single-valued on the simply connected rectangle.
The integrating factor gives the exact normal form
\[
           \mu(t)\Delta(t)=\Delta(t_*)+8\Psi(t).                 \tag{12}
\]
Since mu never vanishes, the discriminant zeros are precisely the
preimages of the single value −Delta(t_*)/8 under Psi.

Now assume reality symmetry
\[
 H(\overline t,\overline z)=\overline{H(t,z)}.                    \tag{13}
\]
The real spatial center and invariant disk give the same symmetry for
P, Delta, A, J, mu and Psi. In particular A and J are real on real time.
For t=x+iy, integrate first along real time and then vertically:
\[
 \Im J(x+iy)=\int_0^y\Re A(x+is)\,ds.                           \tag{14}
\]
The precise sufficient phase condition is
\[
 \sup_{x+iy\in\overline D}
       \left|\int_0^y\Re A(x+is)ds\right|<\pi/2.               \tag{15}
\]
The simpler, explicit condition
\[
                              K\tau<\pi/2                      \tag{16}
\]
implies it. The real length t_+−t_- does not occur in (16): along the
real axis the primitive J accumulates real amplitude, not phase. This
does not say that K or the isolating spatial wall is independent of that
length; both still refer to the entire rectangle.

**Injectivity.** Condition (15) gives Re mu>0. For distinct s,t in the
closed rectangle, convexity and the fundamental theorem of calculus give
\[
 \frac{\Psi(t)-\Psi(s)}{t-s}
       =\int_0^1\mu(s+v(t-s))\,dv,
\]
whose real part is positive. Thus Psi is injective, including on the
boundary under the strict closed-domain condition. This is the standard
positive-real-derivative univalence argument; compare Theorem 1.1 of
[Nunokawa, Sokol and Thomas][univalent]. The proof is included so the
domain and strictness assumptions are explicit.

**Consequences.** Equation (12) now has at most one zero in the closed
time rectangle. Conjugation would pair any nonreal zero with a second
one, so any zero is real. At a real zero, the real monic quadratic has
a repeated root, whose position is also real. Thus all cluster events
in the rectangle, if present, occur in physical real (t,z)-space.

Assume only the two real cap conditions
\[
                       \Delta(t_-)\ne0,\qquad\Delta(t_+)\ne0.   \tag{17}
\]
No collision can then occur anywhere on the complex time boundary:
nonreal events have already been excluded, and the only real boundary
times are t_- and t_+. The spatial wall was nonzero by the isolation
contract. The relative degree on
B=D times {|z−a|<R} is therefore defined without separately assuming a
nonzero jet on all time caps.

On the real interval, mu is positive and
\[
                        (\mu\Delta)'=8\mu>0.                   \tag{18}
\]
Consequently
\[
 \boxed{\quad Q_B=\frac{\operatorname{sgn}\Delta(t_+)
                         -\operatorname{sgn}\Delta(t_-)}2
                   \ \in\{0,1\}.\quad}                         \tag{19}
\]
If both signs are positive or both negative there is no event. Negative
followed by positive gives exactly one event. Positive followed by
negative is incompatible with the hypotheses. The normalization mu does
not alter a real sign. Each event has charge one by (8), and Note 04's
degree/discriminant identity supplies the charge interpretation.

**What has been bounded.** The theorem controls all complex events in a
specified proper two-root window. It does not apply to an arbitrary
many-root domain, and it does not assert charge zero from the phase
condition alone. Injectivity controls how many times a value is attained;
it does not say that the value is omitted.

Without reality, a related statement remains: if |A|<=K on a convex time
domain, any two discriminant zeros have separation at least pi/K. If
their distance were smaller, the argument of mu along their connecting
segment would have total variation less than pi, placing it in a rotated
open half-plane and making its integral nonzero, contradicting (12).
For K=0 there is at most one zero. This ancillary separation statement
does not confine a zero to real time.

## 4. An explicit complete-theta strip width

For the complete theta source use the existing normalization
\[
 H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)du,
\]
\[
 \Phi(u)=\sum_{n\ge1}
 (2\lambda_n^2e^{9u}-3\lambda_ne^{5u})e^{-\lambda_ne^{4u}},
 \qquad\lambda_n=\pi n^2.                                     \tag{20}
\]
Every term is positive for u>=0 and the full source has super-exponential
decay. Define the finite complete moments
\[
 M_j(T,s)=\int_0^\infty\Phi(u)u^j e^{Tu^2}\cosh(su)du.           \tag{21}
\]
These use cosh rather than the slightly larger exp envelope in earlier
notes. There is no retained-mode cutoff or omitted source tail in (21).
If evaluated by a finite sum later, every omitted mode and exterior
integral must be bounded as in [Note 01][n01].

Suppose independently established positive constants d_r,d_R satisfy
\[
 |H(x,z)|\ge d_s>0\quad
 (x\in[t_-,t_+],\ |z-a|=s),\qquad s=r,R.                        \tag{22}
\]
At one real anchor, suppose the argument-principle count is two on
**both** circles. This is equivalent to two roots in the inner disk and
none in its annular collar at that anchor. The two counts are needed;
a two-root inner disk alone does not exclude additional outer roots.

The constants in (22) are inputs to be proved on the actual source,
not positive minima asserted without a proof. They concern spatial
boundaries, not an interior joint-jet floor or the gap between the roots.
They are compatible with a double event inside.

For real x and y,
\[
 |e^{iyu^2}-1|\le |y|u^2,
\]
while |cos(zu)| and |sin(zu)| are at most cosh(su) on |z−a|=s.
Thus, for |y|<=tau,
\[
 |H(x+iy,z)-H(x,z)|\le\tau M_2(t_+,s),
 \qquad |H_z(x+iy,z)|\le M_1(t_+,s).                            \tag{23}
\]
There is no extra exp(tau u^2) payment: this is a purely imaginary
heat-time lift. Complete source domination justifies the integrals and
their holomorphic differentiation.

Set
\[
 d=R-r,\quad L=M_1(t_+,R),\quad B_s=M_2(t_+,s).
\]
Then the following explicitly sufficient choice pays the isolation and
phase conditions simultaneously:
\[
 \boxed{\quad
 0<\tau<\min\left\{\frac{d_r}{B_r},
             \frac{d_R}{B_R+8RL/(\pi d^2)}\right\}.
 \quad}                                                        \tag{24}
\]
Indeed delta_s=d_s−tau B_s is positive on both circles, so the two root
counts remain fixed throughout the connected time rectangle. There are
exactly two roots in the outer disk and both stay in the inner disk.
Equation (9) gives K=4RL/(delta_R d^2), and the second bound in (24)
is exactly K tau<pi/2 after rearrangement. Conditions (13) and (20)
are compatible automatically, so §3 applies once the real cap signs
are established.

This is an explicit analytical continuation width expressed in complete
source moments and wall data. It remains positive when the internal gap
closes, provided the stated wall floors and collar remain controlled.
It is not uniform in height or time without corresponding uniform
control of those inputs. No concrete theta values of d_r,d_R or cap
signs have been proved in this round, and no new theta box is certified.

For later signed work, the exact numerator in (10) is
\[
 H_z-\kappa H=\int_0^\infty\Phi(u)e^{tu^2}
                   [-u\sin(zu)-\kappa(t)\cos(zu)]du.             \tag{25}
\]
The complete tail constraint in [BW14 Note 04][tail] may be a useful
input to such a coupled estimate. Its proved strict physical comparison
is for real parameters; we do not import that gain onto our complex
spatial/time wall without a new transfer argument. In particular the
positive tail estimate alone supplies neither (22) nor the cap sign.

## 5. Exact controls and scope

The controls below are algebraic checks, not numerical experiments.

| Heat control | Discriminant and coefficient | Consequence |
| --- | --- | --- |
| H=z^2−2t on t_-=−1/4, t_+=1/4, tau=1/4, r=1, R=2 | Delta=8t, A=0; every spatial root has modulus at most 2^(−1/4)<1. | All geometric/phase hypotheses hold. The cap signs are negative then positive, giving Q=1. This is not an excluded control. |
| H=z^2−1−2t on the same time rectangle, r=3/2, R=2 | Delta=4+8t, A=0; root modulus at most (5/2)^(1/4)<3/2. | Both cap signs positive; Q=0. |
| H=z^2+1−2t on that rectangle, r=3/2, R=2 | Delta=8t−4, A=0; the same root bound. | Both cap signs negative; Q=0 despite nonreal spatial roots on the real time interval. |
| H=z^3−(4+6t)z+2 on a spatial window containing its full fiber | Three roots and three complex spacetime events. | It fails the two-root contract. The theorem cannot be used to erase its complex events. |
| H=z^3−6tz near its triple event | Three roots; local charge 3. | It also fails the two-root contract. No claim for arbitrary multiplicity is made. |

For the first three controls the exact A=0, rather than a coarse wall
majorant for A, establishes the phase hypothesis. They lack the complete
theta source (20) but satisfy the analytic heat theorem's premises.

The [broader control register][controls] has the same logical response.
Near a real ordinary double event, a sufficiently small proper two-root
window can satisfy the wall and phase conditions, while Delta'=8 forces
negative then positive cap signs. Thus the charge theorem correctly
allows the event; its zero-charge case fails the same-sign premise.
This applies to the relevant ordinary double witnesses, not to every
global domain of those sources.

For a claimed theta-only endpoint estimate, retain the distinct source
failures: Euler-factor controls change Euler data; weighted-square and
finite-prime controls lack the unchanged full normalized coefficient and
reflection conjunction; reflected and positive-primitive controls lack
the canonical theta square expansion; the RH-conditional close endpoint
sources in [BW10 Note 05][close] lack ordinary Dirichlet-series arithmetic.
Theorem (19) itself distinguishes none of them from theta. No local
charge identity can substitute for that remaining arithmetic estimate.

## 6. What is gained and what still blocks endpoint exclusion

The gain is an analytic reduction of an entire complex-time charge
calculation to a controlled exterior coefficient and two real signs.
The coefficient is regular at a collision, and its complete-source
strip bound contains no inverse internal gap. Once its phase is
controlled, nonphysical complex-time events cannot contaminate this
two-root count. This differs from supplying a holomorphic degree-zero
reference and transferring its uniform error floor in Note 02.

The half-plane bound is on the derivative Psi'=mu. It implies
injectivity and charge at most one, **not** charge zero. The quadratic
control demonstrates the distinction exactly. Nor does the same-sign
real-cap condition get proved merely by writing it down.

For a window straddling time zero, a hypothetical endpoint double is
fully compatible with all the analytic machinery: its incoming
discriminant is negative, its outgoing discriminant is positive, and
Q=1. The known real adjacent-pair equation for theta,
\[
 \Delta'=8-4\Delta\sum_{r_j\notin\{z_1,z_2\}}
                       \frac1{(z_1-r_j)(z_2-r_j)}               \tag{26}
\]
at an all-real simple time is the real specialization of (7), not a
contradiction to it. The sum retains every exterior zero; for an
adjacent real pair it is positive. This identity and its compatible
endpoint expansion are already in BW10 Note 03.

Likewise, Q=1 in a window straddling zero does not imply a time-zero
collision: the unique event could occur at negative time. A sign change
on an entirely negative-time subinterval would locate that event there;
the at-most-one theorem would then exclude an additional endpoint event.
Such a location or signed cap input still needs an independent proof.

**Next analytical obligation.** Establish actual-theta wall floors and a
useful phase bound on a declared two-root window, and obtain signed cap
information from the unchanged source rather than source norm upper
bounds alone. Centered contour moments
\[
 S_k(t)=\frac1{2\pi i}\int_{\Gamma_R}
               (\zeta-a)^k\frac{H_z}{H}(t,\zeta)d\zeta,
 \qquad \Delta(t)=2S_2(t)-S_1(t)^2                              \tag{27}
\]
specify that scalar target without tracking individual roots. A bound
which only improves the absolute moments in (21) may widen the analytic
strip, but does not determine the missing cap sign. The signed vertical
integral in (15) and the coupled numerator (25) are the places to retain
more complete-source information in the next estimate.

This completes the analytical two-root reduction, with the scope stated
above. Actual theta exclusion, arbitrary-height coverage and the
many-root/multiple-event extension remain open. HMC-05 stays open and
HMC-06 stays gated.

[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a14]: ../../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[results]: ../../../../../../../result-summaries/README.md
[n01]: 01_BOUNDED_THETA_CHARGE_AND_DIRECT_COMPARISON_20261021.md
[n04]: 04_ANALYTICAL_SCOPE_AND_POTENTIAL_OF_RELATIVE_CHARGE_20261021.md
[gap]: ../../10_rh_implies_simple_zeros/notes/03_SIGNED_PRIME_TRANSPORT_AND_EULER_RIGIDITY_20261020.md
[energy]: ../../10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md
[close]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[tail]: ../../14_theta_source_transform_constraints/notes/04_CANONICAL_TAIL_LAPLACE_CONSTRAINT_AND_COUPLED_ENCLOSURE_20261021.md
[review]: ../reviews/05_TWO_ROOT_DISCRIMINANT_AND_CAP_REVIEW_20261021.md
[polymath]: https://arxiv.org/html/1904.12438v2#S3
[univalent]: https://www.numdam.org/item/10.1016/j.crma.2018.02.007.pdf
