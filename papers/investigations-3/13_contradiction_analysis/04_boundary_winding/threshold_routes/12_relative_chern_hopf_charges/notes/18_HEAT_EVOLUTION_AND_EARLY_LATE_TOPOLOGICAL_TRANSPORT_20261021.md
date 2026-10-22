# Heat evolution of connections and early to late topological transport

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

**Classification:** exact differential identities, boundary conservation
and analytic collision controls. These extend the interpretation in
[Note 17][n17]. They relate early and late observations under explicit
boundary and transport conditions; they supply no new theta exclusion.
The connection evolves continuously, while its integer boundary charge
is preserved whenever the normalized boundary map remains defined.

## 1 Specify what evolves

Write the complex heat coordinate as tau and use a real shift s to compare
windows at different heat times:

\[
 G_s(\tau,z)=\binom{H(s+\tau,z)}{H_z(s+\tau,z)},\qquad
 \dot G_s=-\partial_z^2G_s.
 \tag{1}
\]

Let M be a fixed smooth closed oriented three-dimensional boundary in
complex (tau,z)-space. Suppose G_s is nonzero on M for every s in a
compact interval. All following derivatives and integrals are then
well defined. This condition permits interior events; it is a condition
on the whole moving boundary. Holomorphy of H alone does not imply it.

Put E_s=G_s^*G_s, g_s=G_s/sqrt(E_s), P_s=g_s g_s^*. Exterior
differentiation d below is on M, while a dot is partial_s. The phase
connection, its curvature and its temporal component are

\[
 \mathcal A_s=-i g_s^*dg_s,
 \qquad\mathcal F_s=d\mathcal A_s,
 \qquad\chi_s=-i g_s^*\dot g_s.
 \tag{2}
\]

The star denotes Hermitian transpose. Forms A, F and chi are real.
The convention is the one in Note 17: holonomy along a closed loop gamma
is exp(-i integral_gamma A).

## 2 Exact evolution of the connection and loop phase

Define the real one-form

\[
 \mathcal J_s=-i\{\dot g_s^*dg_s-dg_s^*\dot g_s\}
 =-\frac{2\operatorname{Im}
       ((G_{s,zz})^*(I-P_s)dG_s)}{E_s}.
 \tag{3}
\]

Then direct differentiation gives

\[
 \boxed{\dot{\mathcal A}_s=d\chi_s+\mathcal J_s,
 \qquad \dot{\mathcal F}_s=d\mathcal J_s.}
 \tag{4}
\]

Indeed subtract d(-i g^* dot g) from partial_s(-i g^*dg); the two
mixed derivative terms cancel and leave the first expression in (3).
The component of dot g parallel to g contributes only a real product
to dot g^*dg. The remaining component is
(I-P)dot G/sqrt(E). Substitution of dot G=-G_zz proves the second
expression in (3). In the same convention
chi=-Im(G^*G_zz)/E. These calculations retain the backward-heat sign.

For a fixed closed loop gamma in M,

\[
 \frac d{ds}\oint_\gamma\mathcal A_s
     =\oint_\gamma\mathcal J_s.
 \tag{5}
\]

Thus an individual loop's phase generally changes under heat flow. Its
change is the mixed heat/spatial curvature flux; it is not an integer
topological invariant. The same statement applies to moving loops after
pulling everything back to a fixed parameterized loop.

A fallback estimate is explicit. If ||G||>=delta_G>0,
||G_zz||<=M_2 and ||dG||<=M_1 on the loop, in a declared background
metric, then

\[
 \left|\frac d{ds}\oint_\gamma\mathcal A_s\right|
 \le\frac{2\operatorname{length}(\gamma)M_2M_1}{\delta_G^2}.
 \tag{6}
\]

These derivative bounds can be supplied by complete theta moments on a
compact domain. The jet floor remains a substantive boundary input.
Equation (6) is a generic absolute allowance, not a sharper signed theta
estimate and not a floor near an unknown endpoint event.

There is an exact example of changing holonomy. Take H(t,z)=z^2−2t,
real t, and the complex spatial loop z=exp(i theta). Its jet never
vanishes on that loop because |H_z|=2. Nevertheless,

\[
 \mathcal A(\partial_\theta)
 =\frac{6-4t\cos(2\theta)}{5+4t^2-4t\cos(2\theta)}.
 \tag{7}
\]

At t=0 this is 6/5, while at t=1/2 it is identically 1. The loop
integrals are 12 pi/5 and 2 pi, with different holonomies. This checks
that regular heat evolution need not preserve a Berry phase. Here only
the jet, not H alone, is required nonzero on the loop.

## 3 Integer boundary charge is conserved

For M diffeomorphic to S^3 with the specified orientation, the
[manuscript's Hopf formula][intro] gives

\[
 Q_s=\frac1{4\pi^2}\int_M\mathcal A_s\wedge\mathcal F_s
     =\deg(g_s)\in\mathbb Z.
 \tag{8}
\]

It is constant under the nonvanishing-boundary hypothesis of Section 1.
This is homotopy invariance of degree, not a new heat-specific theorem;
see [Hatcher, Section 2.2, page 134][hatcher]. There is also a direct
differential proof suited to the transport question.

On the cylinder of parameters define
A_total=A_s+chi_s ds. Its curvature is

\[
 F_{\rm total}=\mathcal F_s+ds\wedge\mathcal J_s.
\]

It is the pullback of the Hopf curvature from CP^1, a real two-dimensional
target. Therefore F_total wedge F_total=0, which implies
J_s wedge F_s=0. On the closed three-manifold, integration by parts gives

\[
 \dot Q_s=\frac1{2\pi^2}
       \int_M(d\chi_s+\mathcal J_s)\wedge\mathcal F_s=0.
 \tag{9}
\]

The exact term integrates to zero and the other integrand vanishes.
This special pullback structure matters: a general evolving U(1)
connection need not have a constant Chern-Simons integral.

For a moving physical domain Omega_s with isolated holomorphic events,
the same degree statement has the crossing interpretation

\[
 Q_{\rm late}-Q_{\rm early}
   =\sum_{\rm entering}q_p-\sum_{\rm leaving}q_p,
 \qquad q_p=\binom{m_p}{2},
 \tag{10}
\]

when crossings are isolated and endpoints avoid events. Persistent
boundary events require a different domain or a separately justified
limiting argument. The positive local weights are inherited from the
[cluster theorem][foundations]. An event can leave a moving window;
charge conservation does not force it to remain in that window.

For example, use G_s=(z^2−2(tau+s),2z) on
Omega={|tau|<r, |z|<R}. Its only common zero is (tau,z)=(-s,0),
with local charge one. For 0<=s<r the boundary degree is one; for
s>r it is zero. At s=r the common zero is on the boundary, precisely
where normalized transport fails. A zero-charge later window cannot be
pulled back through that crossing by asserting continuity of H.

## 4 Comparing early and late faces requires every side face

There is a complementary fixed-spacetime flux formula. Away from common
zeros, let

\[
 \mathcal C=\frac1{4\pi^2}\mathcal A\wedge d\mathcal A.
\]

Then dC=0 by the same Hopf pullback argument. For a bounded four-dimensional
region W in complex heat spacetime, with nonzero boundary jet and isolated
interior events, excise small balls around those events and apply Stokes.
If the oriented boundary is late face minus early face plus side faces,

\[
 \boxed{I_{\rm late}-I_{\rm early}+I_{\rm side}
       =\sum_{p\in W}q_p,\qquad I_\Sigma=\int_\Sigma\mathcal C.}
 \tag{11}
\]

For example, take W=[t_-,t_+] times [-eta,eta] times a spatial disk,
using real and imaginary heat coordinates and complex z. The sides
include both imaginary-time faces and the outer spatial wall. The
individual face integrals are generally not integer invariants; their
oriented sum is. Gauge changes can move corner contributions between
faces, while the closed-boundary total is unchanged. All faces must use
compatible data and orientations.

An ordinary fixed-real-time spatial slice has real dimension two. It
does not, by itself, carry this three-dimensional Hopf boundary invariant.
One must retain the extra boundary directions or use a different
invariant. The [real spacetime wall-flux theorem][realflux] supplies such
a different observation, counting real-root births with weights floor(m/2).
Its wall terms are essential and its weights are not the complex q_p.

For a proper two-root complex rectangle satisfying Note 05's phase
condition, the existing reduction makes (11) especially concrete:

\[
 Q=\tfrac12\{\operatorname{sgn}\Delta(t_+)
                    -\operatorname{sgn}\Delta(t_-)\}.
 \tag{12}
\]

Both cap discriminants must be nonzero. This allows one event as well
as none; putting an unknown double on the initial cap would violate a
hypothesis. The bounds remain meaningful for a window enclosing that
event with caps on either side.

## 5 Marked monodromy can carry early information to a late fiber

Suppose a proper finite root cluster has no collision along a path beta
from a regular early time t_0 to a regular later time T. Continuation
gives an identification P_beta of its labeled roots. If M_0 is the
permutation obtained around a loop gamma based at t_0, transport the
loop to T by first following beta backwards, then gamma, then beta
forwards. Its monodromy is

\[
 \boxed{M_T=P_\beta M_0P_\beta^{-1}.}
 \tag{13}
\]

Thus the cycle type of the root permutation is preserved. For an
ordinary double, Delta has a simple zero, and sqrt(Delta) changes sign
around a small complex-time loop. The permutation is a transposition.
A later base point retains that exchange when the marked loop is
retained, even though its roots are simple.

For regular spectral covers w^2=H, Gauss-Manin transport gives the
analogous conjugation of homology monodromy, with the finite boundary
contract in [BW13 Note 01][period]. Root permutations and homology
monodromy are different representations. In particular, the local
two-branch-point cover is an annulus: a Dehn twist fixes its sole
H_1 generator. One must not infer a nontrivial action on this one-dimensional
homology merely from the root exchange. Relative cycles, periods or a
larger marked fiber can retain further information, with their own
boundary and source requirements.

Moving the base point does not move the whole winding loop into an
arbitrarily late regular neighborhood. A complex-time loop winding around
zero cannot be deformed wholly into Re t>0 while preserving that winding
and avoiding zero. Thus late-slice asymptotics do not automatically
compute the transported monodromy. The entire continued loop is part
of the data.

## 6 Regular positive-time topology does not decide the endpoint

The exact heat family

\[
 H_C(t,z)=z^2-2t-C/4,\qquad C\ge0,
 \qquad\Delta_C(t)=8t+C
 \tag{14}
\]

has two simple real roots at every t>0 for every C. At C=0 it has an
endpoint double; at C>0 its endpoint roots are distinct. On any declared
finite positive time interval, a sufficiently large fixed spatial disk
contains both roots and its regular spectral cover is an annulus in
either case. Ordinary root counting also gives two, including multiplicity,
on the endpoint disk. These observations do not separate the two cases.

The exact affine transport does separate them:

\[
 \Delta_C(T)-8T=C=\Delta_C(0).
\]

For the general isolated pair, [Note 12][n12] gives

\[
 \Delta(0)=\mu(T)\Delta(T)-8\int_0^T\mu(s)ds,
 \qquad\mu(t)=\exp\!\left(-\int_0^t a(s)ds\right).
 \tag{15}
\]

This retains endpoint information as a continuous signed quantity, not
as an integer topological class. Recovering its strict sign requires
accuracy in the complete coupled difference.

There is an equally explicit degeneration of fixed-slice topology. For
C=0 the projective rational map on the compactified spatial sphere is
[Z:W] mapping to [Z^2−2tW^2:2ZW]. It has degree two for t>0. At t=0
cancelling the common factor Z gives [Z:2W], of degree one. The resulting
slice maps do not form a continuous family at (t,z)=(0,0): for z=0,
t>0 the direction is [1:0], whereas the cancelled endpoint direction is
[0:1]. Homotopy invariance is not violated. The normalized family has
lost its regularity at the endpoint.

Similarly, BW13's quadratic vanishing-cycle period is 2 pi i t and
approaches zero while the positive-time homology class remains nonzero.
The cycle can shrink at the limiting singular fiber. A proof that rules
out this degeneration for theta needs a quantified source restriction;
smoothness of the unnormalized heat field is insufficient.

## 7 A concrete continuation test

There are two useful finite tests of the user's idea. One can specify
a family of closed boundaries, establish the degree at a later end,
and prove that the complete jet stays nonzero on the entire swept
boundary. Alternatively, one can estimate the complete boundary sum
in (11); an independent bound below one forces its nonnegative integer
charge to be zero. These are conditional consumers. The substantive
milestone is the source estimate that pays the boundary or flux without
assuming the desired internal root gap. The later reference must be a
proved complex-window statement, not merely simplicity on a real slice.

For a monodromy test, specify the marked complex-time loop and a
theta-source constraint that determines its permutation or period
behavior independently of local collision assumptions. Retain all
continuation paths and boundaries. Abstract preservation of the
conjugacy class is a dictionary, not that missing determination.

Passing from positive t to zero, or from finite T to infinity, needs
control of normalization, boundary motion, disappearing cycles and any
escape to infinity. No such uniform theta estimate follows from the
identities above. They support a finite-window investigation and do not
change FTSR-06 or FTSR-07.

Read with the [result index][results], [collision controls][controls] and
[avoid index][avoid], especially [target classification][a01],
[geometric lifts][a03] and [scoped conclusions][a07]. The polynomial
controls verify the generic transport mechanism and lack canonical
theta arithmetic. Stronger arithmetic controls retain their separate
preservation lists. No new inequality distinguishing theta from them is
claimed here. The calculations are analytic authoring-assistant checks;
there is no new theta numerical acquisition or independent review.

[n17]: 17_PARALLEL_TRANSPORT_CONNECTIONS_AND_COLLISION_CONTROLS_20261021.md
[n12]: 12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md
[intro]: ../manuscript/introduction.tex
[foundations]: ../manuscript/foundations.tex
[period]: ../../13_spectral_covers_and_periods/notes/01_NODAL_PERIOD_VARIATION_AND_FOUR_JET_COMPARISON_20261021.md
[realflux]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[hatcher]: https://pi.math.cornell.edu/~hatcher/AT/ATch2.pdf
