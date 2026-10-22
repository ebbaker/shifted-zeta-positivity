# Complete physical Chern/Hopf boundary and critical-value winding

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from the active turn metadata.

**Status: CHB-04 complete as a local analytic assembly with explicit
source-parameterized geometry and boundary floors.** All physical heat
faces and the outer spatial wall reduce together to one critical-value
winding. No puncture remains in this construction. Actual theta acquisition,
a measured acquisition advantage and collision exclusion are not supplied.

This continues [Note 01][n1] and [Note 02][n2] under the [program][program]
and [plan][plan]. Read the [result index][results], [avoid index][avoid],
[collision controls][controls], [classification rule][a01] and [scope rule][a07].
The charge/discriminant identity is already in [BW12 foundations][foundations],
Theorem `f:charge-winding`; this note does not claim a new charge invariant.
The addition is the explicit two-chart assembly, physical face accounting
and quantitative interface for simplifying its integral. [Review 05][review]
is contributing-agent same-model review, not independent specialist review.

## 1. Split the closed boundary, not a pinched interior sector

Use H_tau=-H_zz and the fixed physical frame
\[
 G=(H,H_z),\quad E=|H|^2+|H_z|^2,\quad g=G/\sqrt E,\quad
 \mathcal A=-ig^*dg,\quad\mathcal F=d\mathcal A,\quad
 \mathcal C=\mathcal A\wedge\mathcal F/(4\pi^2).
\]
Let D=[-T,T]+i[-Y,Y] be a complex heat rectangle, Omega the spatial disk
|z-a|<=R, W=D times Omega, and M=boundary W with complex outward orientation.
Assume the jet is nonzero on M. Suppose, for a fixed P>0, the equation
H_z=pH has exactly one simple solution z(tau,p) in the interior of Omega
for every tau near D and |p|<=P, with strict outer-wall inequality
\[
                     |H_z|>P|H|.                         \tag{1}
\]
Require H(tau,z(tau,p))!=0 for tau near boundary D. An explicit sufficient
ordinary-double construction is proved in §4; these are not assumed
unknown root gaps. Write c(tau)=z(tau,0), V(tau)=H(tau,c(tau)), and
kappa=P²/(1+P²). Since H_z=0 on the critical branch,
\[
                         V'=-H_{zz}(\tau,c(\tau)).        \tag{2}
\]

Define the **boundary pieces**
\[
 M_- = M\cap\{|H_z|\le P|H|\},\qquad
 M_+ = \overline{M\setminus M_-},\qquad \Sigma=\partial M_-.
\]
G!=0 makes the H-chart regular on M_- and the H_z-chart regular on M_+.
By (1), M_- lies entirely in the heat faces. Uniqueness of z(tau,p) makes
it exactly the image of boundary D times the p disk. On that product
z_p=H/(H_zz-pH_z)!=0. Hence its orientation is the product of positive
heat-boundary orientation and complex p-disk orientation. M_+ includes
**the entire outer spatial wall and the complementary pieces of all four
heat faces**. The interface Sigma is a two-torus with corners at the heat
vertices, not an additional external face.

Both pieces are compact and regular even though W contains an event.
No division by H is made at that interior event. This is precisely the
change from the pinched four-dimensional sector of Note 02.

## 2. Exact seam and complete integral

On H!=0 use p=H_z/H, eta_H=Im(dH/H),
\[
 a_p={\operatorname{Im}(\bar p\,dp)\over1+|p|^2},\qquad
 \mathcal B_H=-\eta_H\wedge a_p/(4\pi^2),\qquad
 d\mathcal B_H=\mathcal C.
\]
On H_z!=0 use q=H/H_z, eta_z=Im(dH_z/H_z),
\[
 a_q={\operatorname{Im}(\bar q\,dq)\over1+|q|^2},\qquad
 \mathcal B_z=-\eta_z\wedge a_q/(4\pi^2),\qquad
 d\mathcal B_z=\mathcal C.
\]
At the seam p=P exp(i beta),
\[
 \mathcal B_H=-{\kappa\over4\pi^2}\eta_H\wedge d\beta,
 \qquad
 \mathcal B_z={1-\kappa\over4\pi^2}\eta_H\wedge d\beta.  \tag{3}
\]
Let s increase counterclockwise along boundary D. The seam orientation as
boundary of M_- is **minus ds wedge d beta**, since the outward radial
p vector is the middle vector in ds wedge d|p| wedge d beta.

For each boundary tau, the function
H(tau,z(tau,p))/V(tau) is nonzero on the p disk and equals one at p=0.
It has a unique holomorphic logarithm in p normalized to zero there,
continuing consistently around the heat boundary. The radial harmonic
mean argument from Note 02 therefore gives
\[
 \int_\Sigma\eta_H\wedge d\beta
       =-2\pi\oint_{\partial D}d\arg V
       =-4\pi^2 n,\qquad n=\operatorname{wind}_{\partial D}V. \tag{4}
\]
One may instead use H=tau B with a nonzero holomorphic B in the explicit
ordinary-double construction below. Neither route replaces continuous
phase lifting by principal endpoint arguments.

Stokes on the two pieces now proves
\[
 \int_{M_-}\mathcal C=\kappa n,\qquad
 \int_{M_+}\mathcal C=(1-\kappa)n,\qquad
 \boxed{\int_{\partial W}\mathcal C
     ={1\over2\pi}\oint_{\partial D}d\arg V=n.}           \tag{5}
\]
The complementary chart supplies the missing fraction; it is not zero.
The calculation is independent of P within the admissible range. It uses
the fixed physical jet frame and its actual chart transition.

## 3. Every physical face and connector

For tau on boundary D, let U_tau be the image of the p disk and let
A_tau=Omega minus its interior, oriented by complex z. Set
\[
 J(\tau)=\int_{A_\tau}\mathcal B_z,\qquad
 K(e)=\int_{e\times\partial\Omega}\mathcal B_z,            \tag{6}
\]
where e is an oriented heat edge from tau_a to tau_b and the latter
orientation is increasing edge parameter followed by counterclockwise
spatial-circle angle. These integrals are regular because H_z!=0 there.
The orientation identity for the moving annulus is
\[
 \partial(e\times A)=A_b-A_a-(e\times\partial\Omega)
                              +(e\times\partial U).
\]
Parameterization by a moving disk changes no boundary orientation. Thus
\[
 \begin{aligned}
 I_-(e)&={\kappa\over2\pi}\Delta_e\arg V,\\
 I_+(e)&={1-\kappa\over2\pi}\Delta_e\arg V
                      +J(\tau_b)-J(\tau_a)-K(e),\\
 I_{\rm heat}(e)&={1\over2\pi}\Delta_e\arg V
                      +J(\tau_b)-J(\tau_a)-K(e),\\
 I_{\rm spatial}&=\sum_{e\subset\partial D}K(e).          \tag{7}
 \end{aligned}
\]
The last line is Stokes on the actual three-dimensional spatial wall
D times boundary Omega, which lies wholly in the H_z chart. The J terms
telescope at heat corners and the K terms cancel against that retained
wall. Formula (5) follows with all five physical faces included.

The late edge t=T goes upward, top imaginary-time edge goes left, early
edge t=-T goes downward, and bottom imaginary-time edge goes right.
There is **no inner heat-circle face** in this complete W. Its absence
comes from using the second chart on a full boundary, not from discarding
the shrinking cap of Note 02. The spatial wall generally has nonzero flux;
what has been removed is the need for its separate integral in the assembled
formula. Individual physical heat faces retain their J and K terms.

## 4. An explicit complete-source ordinary-double window

Assume H(0,a)=H_z(0,a)=0, h_2=H_zz(0,a)!=0, and h=|h_2|. On a fixed
ambient polydisk |tau|<=d_*, |z-a|<=r_*, let D_j bound |partial_z^j H|
for j=2,3,4. D_2>=h>0. Fix P>0 and define
\[
 C_0=D_3+PD_2>0,\quad C_1=D_4+PD_3,\quad
 J_0=D_3+D_4+{4C_0\over3h}(D_2+D_3)>0,\quad
 \alpha=\min(1,h/(4C_0)),
\]
\[
 \boxed{R={1\over2}\min\left(r_*,{d_*\over\alpha},
           {h\over4(C_0+C_1)},{h\over2J_0}\right),\quad
 d=\min\left(\alpha R,{hR^2\over32D_2}\right),\quad
 T=Y=d/2.}                                                \tag{8}
\]
All these parameters are positive. The heat rectangle has |tau|<=d/sqrt2<d,
so its complex corners are paid. Put
\[
 \epsilon_1=D_2R+D_3d,\quad \epsilon_2=D_3R+D_4d,\quad
 \theta=(\epsilon_2+P\epsilon_1)/h\le1/8,\quad
 \delta_F=h(1-\theta)\ge7h/8.                             \tag{9}
\]
Taylor/heat bounds give |H_z|<=epsilon_1 and |H_zz-h_2|<=epsilon_2
on the product. For F_p=H_z-pH, the map z -> z-F_p/h_2 is a uniform
theta-contraction. Its center displacement is at most d C_0/h<=R/4,
so it maps the closed spatial disk into the disk of radius 3R/8. It has
one zero, with F_{p,z} nonzero. The unique solutions form a holomorphic
graph in both parameters. On the outer wall,
\[
 |F_p|\ge(h-\epsilon_2-P\epsilon_1)R-dC_0
                \ge5hR/8.                               \tag{10}
\]
This is uniform in |p|<=P. Minimizing |H_z-pH| over that disk proves
|H_z|-P|H|>=5hR/8, a quantitative version of (1).

As in Note 02,
\[
 H(\tau,z(\tau,p))=\tau B(\tau,p),\quad B(0,p)=-h_2,
 \quad |B+h_2|\le\epsilon_2+
       {\epsilon_1C_0\over\delta_F}\le J_0R\le h/4.       \tag{11}
\]
Here z_tau is bounded by C_0/delta_F; integration of
H_tau+H_z z_tau along the radial heat segment gives (11). Thus B is
nonzero, V=tau B(tau,0), and its only zero in D is the simple zero at zero.
Since every common jet zero lies on the critical branch, the center is
the unique event in W. The heat boundary is regular, and (5) gives n=1.

The same parameters pay BW12's **proper two-root** geometry. For s=R/2,R,
\[
 |H(\tau,a+w)-(h_2/2)w^2|
       \le D_3s^3/6+dD_2\quad (|w|=s).
\]
Since D_3R<=h/8 and dD_2<=hR²/32, the right side is less than h s²/4.
Rouche gives exactly two H zeros inside each circle and
\[
                   |H|>hs^2/4\quad (|w|=s).              \tag{12}
\]
Both roots lie inside R/2; the annular collar is zero-free. No internal
root separation was assumed. Strict margins persist on a neighborhood
of the closed physical window, as required for the chart construction.

**Relation to existing geometry.** [BW12 Note 07][bw12-window] already pays
proper two-root windows at hypothetical ordinary doubles. Its Taylor
bounds also imply one H_z zero, counted with multiplicity, on each spatial
disk: on its outer wall, |H_z-2c(z-a)|<2|c|R. That zero is therefore simple.
Its bounds |H_z|>(3/2-sqrt2/128)|c|R and |H|<=(59/48)|c|R² also allow
Rouche for H_z-pH when PR<=1. The present constants are a convenient
stronger contract giving quantitative derivative, graph and boundary
floors; they are not a claim that the earlier geometric existence was unpaid.

**Canonical acquisition.** The exact field remains the complete source
H=integral_0^infinity Phi(u) exp(tau u²) cos(zu)du. For a real center a,
D_j may be obtained from complete moments with weight exp(d_*u²+r_*u),
using [Note 01 §4][n1] and its linked finite mode/ray ledger. At nonzero
real base time, include that time in the quadratic exponential. Pay finite
quadrature, all omitted modes/rays, outward rounding, and simultaneous
value/jet data from the same unchanged source. A paid lower h and upper
D_j can be used, with inward parameter choices. Exact event matching is
a conditional hypothesis, not a numerically observed theta event. There
is no uniform all-height radius or no-collision assertion.

## 5. Whole-boundary floor and regulator allowance

Let eta_B be the upper bound in (11), b=h-eta_B>0,
v_*=min(T,Y)b, and m_*=5hR/8. On a heat face, |V|>=v_*. Along a spatial
segment from c(tau), convexity of Omega gives
\[
 |H(\tau,z)-V(\tau)|\le D_2|z-c|^2/2,\qquad
 |H_z(\tau,z)|\ge(h-\epsilon_2)|z-c|.
\]
Splitting at |z-c|=sqrt(v_*/D_2), and using (10) on the spatial wall, gives
\[
 E\ge e_0:=\min\left(m_*^2,{v_*^2\over4},
                 {(h-\epsilon_2)^2v_*\over D_2}\right)>0
                     \quad\hbox{on all of }M.             \tag{13}
\]
This is an E floor, not a floor for sqrt(E). No interior floor is asserted.
Let
\[
 L=(D_3^2+2D_2^2+\epsilon_1^2)^{1/2},\qquad
 S=4\pi R^2(T+Y)+8\pi RTY.                               \tag{14}
\]
L bounds the real operator norm of DG via its complex Frobenius norm;
S is the Euclidean three-volume of the complete boundary. The normalized
sphere volume formula gives |C|_comass<=L³/(2pi² e_0^(3/2)). Consequently,
with k=E/(E+delta²) and C_delta=k²C,
\[
 \left|\int_M\mathcal C_\delta-n\right|
 \le B_\delta:=\left[1-\left({e_0\over e_0+\delta^2}\right)^2\right]
                    {SL^3\over2\pi^2e_0^{3/2}}
 \le {SL^3\delta^2\over\pi^2e_0^{5/2}}.                  \tag{15}
\]
The bound is valid across both chart axes; corner strata have zero
three-volume. [Note 04][n4] turns this into bounds on the nonnegative
bulk integral and specified weighted versions. Finite-delta individual
faces still need their amplitude correction; (7) is unregularized.

## 6. Quadratic evaluation and direct comparator

For H=z²-2tau, take R=1, T=Y=1/16, P=1/4, kappa=1/17. These parameters
satisfy the needed geometry directly; (8) is sufficient, not necessary.
The explicit graph from Note 02 gives V=-2tau. Write s=|tau|,
a_R=1+R²/4 and D_R(s)=sqrt((a_R+s²/R²)²-s²). Direct integration of B_z
on the outer circle gives
\[
 K(e)={1\over4\pi}\int_e
       \left[1+{s^2/R^2-a_R\over D_R(s)}\right]d\arg\tau. \tag{16}
\]
For completeness, q=z/2-tau/z and eta_z=darg z on that circle. Averaging
Im(conj(q)dq)/(1+|q|²) over its angle yields (16). At fixed tau, J(tau)=0:
a constant joint rotation makes tau real, then conjugation preserves the
annulus, preserves B_z as a pulled-back two-form and reverses its orientation.
All four edges of the square give the same K and the same heat-face flux.

| Contribution | Value for the stated quadratic window |
| --- | --- |
| Central piece of each heat face | 1/68 exactly |
| Entire heat face | 1/4-K(e) |
| Spatial wall | 4K(e), generally nonzero |
| Whole boundary | 1 exactly |

The [reproducible control][checks] evaluates K(e) approximately
0.000794445554866028. A separate direct pullback quadrature of every face
gives total 0.9999999999999489 at its finer resolution. These are floating
diagnostics, not interval-certified errors or theta data; the exact identity
is proved above. The script also checks the complete quadratic geometry.

The same-information direct method may use the critical graph and this
identity. It may also use the existing proper-cluster discriminant Delta.
In this ordinary-event window, V and Delta each have only one simple zero,
and V/Delta extends to a nonvanishing holomorphic unit with central value
-h_2/8. Their windings are equal. Thus no new topological information or
arithmetic margin is claimed; the gain is the completed integral reduction.

## 7. A contour between neighboring zeros: what is conserved

The user proposed enclosing all zeros below a height with a moving boundary
that stays between neighboring zeros, preserving topology and total
multiplicity. The argument-principle count N=sum m is indeed constant
under a zero-free contour homotopy. It does **not** imply simplicity:
merging two simple zeros into a double leaves N unchanged. Multiplicity
excess sum(m-1) counts something different and is not automatically conserved.

A control with exterior neighbors is the exact heat polynomial, A>0,
\[
 H_\tau(z)=z^4-(A^2+12\tau)z^2+2A^2\tau+12\tau^2.         \tag{17}
\]
For real 0<t<=A²/64 its four zeros are real and simple, with squared
positive roots
\[
 y_\pm={A^2+12t\pm\sqrt{A^4+16A^2t+96t^2}\over2}.
\]
Here y_+>=A² and 0<y_-<=2t+12t²/A²<=35A²/1024<A²/4.
The fixed circle |z|=A/2 therefore stays between the inner pair and the
outer neighbors. It encloses N=2 at every such time and at t=0, where
the inner pair is a double zero. A fixed boundary is a valid special case
of a moving one. This control has the real-root feature relevant to the
proposed implication, but lacks the canonical theta source; it is not a
counterexample to RH-to-simplicity with additional arithmetic premises.

The **full spacetime** boundary nevertheless has charge one. For complex
|tau|<=A²/64, its other critical points satisfy
|z|²>=13A²/32>A²/4, while the central critical value is
V(tau)=2tau(A²+6tau), with only the simple zero at zero. On the spatial
circle the complete floor is |H|>=109A⁴/1024>0. The product heat rectangle
T=Y=A²/128 therefore has Q=1 by (5), although the spatial count stays two.
For an explicit chart certificate on that circle, |H_z|>=5A³/16 and
|H|<=403A⁴/1024. Thus P=1/(2A) satisfies (1); Rouche gives exactly one
simple root of H_z-pH for every |p|<=P, since H_z has only its central
critical root inside. The heat-boundary graph has H!=0 because the only
common jet zero in the product is its interior center.
These statements and the heat equation are checked exactly in [the control][checks].

Proving **zero complete swept collision charge** would exclude interior
multiple events under the inherited properness and positive local-weight
hypotheses. Showing that a later real slice has simple zeros does not prove
that the surrounding complex three-boundary has zero charge. Its reference
charge, imaginary-time faces and spatial wall must all be controlled.
This is the precise additional task for a finite-height moving-boundary
exclusion route; it is separate from the useful integral bounds in Note 04.

[n1]: 01_CHERN_HOPF_PROJECTIVE_SIDES_AND_LOCAL_SECTORS_20261022.md
[n2]: 02_CHERN_HOPF_PHYSICAL_TIME_SECTOR_REDUCTION_20261022.md
[n4]: 04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md
[program]: ../research-overview/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PROGRAM_20261022.md
[plan]: ../research-progress/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PLAN_AND_PROGRESS_20261022.md
[review]: ../03_heat_transport_and_charges/reviews/05_COMPLETE_BOUNDARY_AND_INTEGRAL_BOUNDS_REVIEW_20261022.md
[checks]: ../03_heat_transport_and_charges/numerics/CHB_FULL_BOUNDARY_CHECKS_20261022.json
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../avoid/01_restating_the_target.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[foundations]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/manuscript/foundations.tex
[bw12-window]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/07_QUANTITATIVE_ENDPOINT_WINDOWS_AND_HEIGHT_COVERAGE_20261021.md
