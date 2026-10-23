# Derivative-weighted reciprocal energy with complete all-height bounds

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified by the parent chat from its recorded
turn configuration. The separate proof audit is an internal same-model
check, not independent specialist review.

**Status: analytic bounds proved below; no RH or simplicity exclusion.**
A derivative numerator changes the integral decisively: on the normalized
cover its differential is exact, and its complete energy has a uniform
upper bound even through multiple zeros. For the canonical theta field,
a finite disk bound holds uniformly at every real height. A whole
horizontal strip also has a finite explicit complete-source bound, with
all source derivative tails paid. These are bounds for a different
integral from the manuscript's unweighted reciprocal energy.

The most directly reusable finite consumer is the compact-cutoff
observable in Section 6: a field approximation error epsilon pays its
entire model error by 64 pi epsilon/9, independently of radius, root
locations and multiplicities. The existing actual-theta Taylor contract
already gives an error below 3.10e-19 for this new observable without
another source acquisition. This is a model-error bound, not a completed
quadrature interval for the observable.

Read the [result index](../../../../result-summaries/README.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), particularly patterns
[01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../avoid/08_normalization_and_constant_slips.md) and
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
This is a quantitative estimating milestone, rather than an equivalent
simplicity criterion. No numerical certificate or method-cost ordering
is asserted.

## 1. The exact derivative payment

Let H be nonzero and holomorphic near a bounded piecewise smooth domain
Omega. Define the full two-sheet energy

\[
 W(H;\Omega)=2\int_\Omega\frac{|H'(z)|^2}{|H(z)|}\,dA_z.
 \tag{1}
\]

At isolated zeros use the locally integrable continuation. If
H(z)=a(z-z0)^m(1+O(z-z0)), then its density is
m^2|a||z-z0|^{m-2}(1+O(|z-z0|)); hence (1) is locally finite for every
m>=1. More precisely its mass on radius epsilon is

\[
 W(H;D(z0,\epsilon))=4\pi m|a|\epsilon^m
                         +O(\epsilon^{m+1}).               \tag{2}
\]

Off the zeros, elementary complex differentiation gives

\[
 \Delta|H|=\frac{|H'|^2}{|H|}.                             \tag{3}
\]

This identity holds distributionally through every zero, without a
point mass. To verify this, remove radius-epsilon disks around the finitely
many zeros in a compact test region and integrate by parts. The normal
flux on each small circle is O(epsilon^m), while the other test-function
boundary term is O(epsilon^{m+1}); both tend to zero. The volume density
is locally integrable by (2). Thus no unrecorded defect is discarded.

If H has no zero on the boundary, Green's formula therefore gives

\[
 W(H;\Omega)=2\int_{\partial\Omega}\partial_n|H|\,ds
 \le2\int_{\partial\Omega}|H'|\,ds
 \le2\operatorname{length}(\partial\Omega)
                       \sup_{\partial\Omega}|H'|.         \tag{4}
\]

Here |partial_n|H||<=|H'|. Boundary zeros can be handled by excision and
limits; for the explicit disk bound one may first use slightly larger
zero-free circles and then pass down to the requested radius. Thus

\[
 \boxed{W(H;D(C,R))\le4\pi R
                     \sup_{|z-C|\le R}|H'(z)|.}           \tag{5}
\]

This constant is sharp in the declared boundary-norm class: for
H=a(z-C)^m, both sides equal 4 pi m |a| R^m. For H=z^2-2t the right side
is 8 pi R^2, uniformly in t, and equality holds at its double endpoint.
This explicitly demonstrates collision compatibility.

On the normalization of w^2=H(z), including a singular fiber, the
holomorphic identity dH=2w dw gives

\[
 \eta=\frac{H'(z)\,dz}{w}=2\,dw,\qquad
 \frac i2\int_X\eta\wedge\bar\eta=W(H;\Omega).            \tag{6}
\]

Thus this is a complete exact-differential energy. It has no hidden
transverse period. For an entire multiplier A, the differential
eta_A=2A(w^2)dw has an entire primitive in the w-plane, hence is globally
exact on the normalized cover. Its energy is at most
sup_{H(Omega)}|A|^2 times W. Multipliers with poles or a restricted domain
require separate singularity and primitive analysis; no such case is
used here.

The numerator requirement is explicit. If an arbitrary holomorphic
numerator N has order k at an m-fold zero of H, then
2 integral |N|^2/|H| is locally finite exactly when 2k+2>m. Taking
N=H' satisfies this inequality for every m>=1. Taking N=1 is the
manuscript's original integral and fails at m>=2.

## 2. Uniform finite disks for the unchanged canonical source

Use the manuscript's exact normalization

\[
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
 \quad
 \Phi(u)=\sum_{n\ge1}\lambda_ne^{5u}
                 (2\lambda_ne^{4u}-3)e^{-\lambda_ne^{4u}},
 \quad\lambda_n=\pi n^2.                                \tag{7}
\]

For real |t|<=S and |Im z|<=Y, complete differentiation and positivity
of the full half-line source yield

\[
 |H_z(t,z)|\le M_{1,Y}(S):=
 \int_0^\infty u e^{Su^2+Yu}\Phi(u)\,du.                  \tag{8}
\]

The manuscript's [effective complete-source tail appendix](../manuscript/reciprocal_hodge_energy/sections/09_source_tails.tex)
supplies a finite-head plus all-mode and all-ray enclosure for this exact
moment. For every real center C,

\[
 \boxed{W(H_t;D(C,R))\le4\pi R M_{1,R}(S)
                       \quad(|t|\le S).}                \tag{9}
\]

The constants are independent of real height C, root count, separation,
orders of vanishing and a putative collision time. No RH assumption,
interior lower bound or canonical-source replacement is used.

## 3. A finite whole-strip bound

Fix Y>0 and put S_Y={z:|Im z|<Y}. Let g_t be the complete smooth even
source e^{tu^2}Phi(u), with Phi extended by its *complete* reflection.
For real y, set k_{t,y}(u)=u g_t(u)e^{-yu} on the entire real line. Then

\[
 H_z(t,x+iy)=\frac i2\int_{\mathbb R}k_{t,y}(u)e^{ixu}\,du.
                                                               \tag{10}
\]

Define

\[
 D_{2,Y}(t)=\int_0^\infty e^{Yu}
 \{2|g_t'|+u|g_t''|+2Y(g_t+u|g_t'|)+Y^2u g_t\}\,du.     \tag{11}
\]

Evenness, two integrations by parts on the *whole* line and absolute
integrability of these derivatives give, uniformly for |y|<=Y,

\[
 |H_z(t,x+iy)|\le
 \min\{M_{1,Y}(S),D_{2,Y}(t)/x^2\}.                        \tag{12}
\]

The second expression is used for x!=0. In detail,
k''=e^{-yu}(2g'+ug''-2y(g+ug')+y^2ug); hence
||k''||_1<=2D_{2,Y}. All boundary terms at infinity vanish by the source's
super-exponential decay. There is no boundary at u=0 on the full line;
the canonical proof uses the complete smooth even reflected source.
The weaker sufficient condition is k in W^{2,1}(R), which can be checked
separately for another source. In particular, a continuous smooth
half-line source with integrable first two derivatives has an even
extension that may have a corner at zero; k(0+)=k(0-)=0 and
k'(0+)=k'(0-)=g(0), so two integrations by parts still have no zero-endpoint
payment. Such a source has not thereby acquired full theta reflection.

Writing M=M_{1,Y}(S) and D=D_{2,Y}(t), direct integration of
min(M,D/x^2), split at |x|=sqrt(D/M), gives

\[
 \int_{\mathbb R}|H_z(t,x+iY)|\,dx\le4\sqrt{MD}.          \tag{13}
\]

For a rectangle [-L,L]+i[-Y,Y], apply (4). At a boundary zero remove a
small disk, including only the portion lying in the rectangle; the
new circular-arc flux is O(epsilon^m), while the removed straight-edge
length tends to zero and its integrand is bounded by |H_z|. Corner zeros
have the same estimate. Thus the boundary identity and upper remain
valid, with normal derivatives taken off the finitely many boundary
zeros. The two vertical-edge payments tend to zero by the uniform
x^{-2} part of (12). Real symmetry gives equal top and bottom absolute
bounds. Exhausting the strip and retaining its two physical boundaries
therefore gives

\[
 \boxed{W(H_t;S_Y)\le16\sqrt{M_{1,Y}(S)D_{2,Y}(t)}.}       \tag{14}
\]

All infinitely many spatial zeros are included by monotone exhaustion;
no claim about their number, location or simplicity is necessary.

As a complete analytic normalization check, take the Gaussian source
g(u)=exp(-u^2), whose cosine transform is
H(z)=(sqrt(pi)/2)exp(-z^2/4). Direct integration gives

\[
 W(H;S_Y)=2\pi Y e^{Y^2/4}.                              \tag{14a}
\]

The top-boundary formula gives the same result: on y=Y,
partial_y|H|=(Y/2)|H| and integral_R |H(x+iY)| dx=
pi exp(Y^2/4); the bottom boundary contributes the same positive amount.
This verifies both physical strip boundaries and the factor two from
the cover. It is an analytic check, not theta evidence or certification.

## 4. Complete effective source derivative budgets

Formula (11) must be paid from the unchanged complete source; finiteness
of its unsigned zeroth moments alone does not pay its derivatives.
Differentiating g_t gives the following uniform upper for |t|<=S:

\[
 D_{2,Y}(t)\le\mathcal D(S,Y):=
 \int_0^\infty e^{Su^2+Yu}
    \{P_0(u)\Phi(u)+P_1(u)|\Phi'(u)|+u|\Phi''(u)|\}\,du,
                                                               \tag{15}
\]

where

\[
 P_0(u)=2Y+(6S+Y^2)u+4SYu^2+4S^2u^3,
 \qquad P_1(u)=2+2Yu+4Su^2.                               \tag{16}
\]

For v=lambda_n e^{4u}, the exact complete-mode derivatives are

\[
 \Phi_n'=\lambda_ne^{5u-v}(-8v^2+30v-15),
 \quad
 \Phi_n''=\lambda_ne^{5u-v}(32v^3-224v^2+330v-75).         \tag{17}
\]

Consequently all terms in (15) admit positive complete upper bounds
using only the following generalized moments (j<=3, 1<=d<=4):

\[
 T_{j,d,a}(S)=\sum_{n\ge1}\lambda_n^d
   \int_0^\infty u^j e^{Su^2+a u-\lambda_ne^{4u}}\,du.    \tag{18}
\]

Specifically let

\[
\begin{aligned}
 B_0(j)&=2T_{j,2,Y+9},\\
 B_1(j)&=8T_{j,3,Y+13}+30T_{j,2,Y+9}+15T_{j,1,Y+5},\\
 B_2(j)&=32T_{j,4,Y+17}+224T_{j,3,Y+13}
                      +330T_{j,2,Y+9}+75T_{j,1,Y+5}.
\end{aligned}                                             \tag{19}
\]

All T arguments include S. Then a fully positive explicit payment is

\[
 \mathcal D(S,Y)\le\widehat D(S,Y):=
 2YB_0(0)+(6S+Y^2)B_0(1)+4SYB_0(2)+4S^2B_0(3)
       +2B_1(0)+2YB_1(1)+4SB_1(2)+B_2(1).                \tag{20}
\]

Replacing D in (14) by this upper bound yields a uniform all-height,
all-multiplicity, bounded-time complete-source estimate.

For explicit truncation errors split (18) into modes n<=N on [0,U],
all omitted modes on [0,infinity), and retained modes on [U,infinity).
Set k=N+1,

\[
 \rho_{k,d}=((k+1)/k)^{2d}e^{-\pi(2k+1)},\qquad
 b_k=4\lambda_k-a.
\]

For d<=4, rho_{k,d}<=256e^{-3pi}<1. If b_k>0 and S<=8lambda_k,
the complete omitted-mode payment is

\[
 L_{j,d,a}(S;N)=
 \frac{\lambda_k^d e^{-\lambda_k}j!}
      {(1-\rho_{k,d})b_k^{j+1}}.                          \tag{21}
\]

For each retained n, put b_n(U)=4lambda_n e^{4U}-a-2SU.
If b_n(U)>0 and S<=8lambda_n e^{4U}, its exterior ray payment is

\[
 R_{n,j,d,a}(S;U)=\lambda_n^d
 e^{SU^2+aU-\lambda_ne^{4U}}
 \sum_{h=0}^j\binom jh\frac{U^{j-h}h!}{b_n(U)^{h+1}}.     \tag{22}
\]

The finite head plus (21) plus the sum of (22) is a complete upper
bound for (18). Proof: geometrically sum the ratios of consecutive
positive mode kernels, then use e^{4u}>=1+4u+8u^2 exactly as in the
manuscript's tail appendix. On an exterior ray write u=U+v and use the
same inequality for v. The factors lambda_n^d are constant in u and
only change the consecutive-mode ratio. For fixed S,Y and the finite
set of j,d,a in (19), sufficiently large N,U satisfy all conditions and
make all tails arbitrarily small. Finite heads still require honest
quadrature enclosures if numerical values are requested. No such values
or claimed cost advantage are part of this note.

## 5. Scope, sibling consumers and collision controls

These bounds give a source-controlled answer for derivative-weighted
reciprocal cover energy. The manuscript, Notes 01--04, and targeted
searches in I4 and BW09/BW10 showed no earlier Delta|H| or
|H_z|^2/|H| estimate. This is a repository duplication screen, not a
literature novelty claim: the elementary identity itself is classical.

The cubic cutoff in Section 6 is inherited from the
[I4/07 weighted-Green program, W2](../../07_weighted_green_integrals/research-overview/01_WEIGHTED_GREEN_INTEGRALS_PROGRAM_20261022.md),
whose [Note 02](../../07_weighted_green_integrals/notes/02_PAIRED_THETA_RESIDUAL_AND_MATCHED_DIRECT_COMPARISON_20261022.md)
already records the corresponding signed-kernel norm. That program's
potential is log(|H|^2+|H_z|^2), whose completed Laplacian retains
multiplicity atoms and whose regular-path error analysis pays a jet
floor. The potential here is |H|, which has no such atom and is
Lipschitz in the field. Thus (24)--(27) are a different consumer and do
not improve that program's completed mass or its same-data tie.

The BW09 physical angular integrals instead use
J(t,x)=H(t,x)+iH_x(t,x),
partial_x arg J=-Q/(H^2+H_x^2),
Q=H_x^2-HH_{xx}, on real spacetime. Its Gaussian-cap and localized
signed energies likewise have their own real-line weights and signed
terms ([BW09 Note 05](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/05_TOPOLOGICAL_ALTERNATIVES_AND_ENERGY_OBSERVATIONS_20261020.md)
and [Note 06](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/06_HEAT_FLOW_CONTOURS_AND_GAUSSIAN_CAP_ENERGY_20261020.md)). These are not spatial holomorphic instances
of (1). The bound here supplies no sign or paid direct comparison for
them. Their existing complete Gram or Plancherel formulas remain
available to the matched direct estimator.

BW10's [completed-ratio energy (Note 15)](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md),
physical signed turning ([Note 21](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md),
[Note 22](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md),
[Note 23](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/23_CAP_PHASE_CONCENTRATION_AND_FINITE_TIME_BASELINE_20261021.md)),
and Gauss-area density
|HH_{zz}-H_z^2|^2/(|H|^2+|H_z|^2)^2
([Note 24](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md)) also have different
numerators and denominators. A comparison that divides by |H_z|^2 to
recover the original reciprocal energy restores exactly the dangerous
critical-point payment. No such denominator-floor estimate is proved.

The local identities and disk bound are shared by all nonzero holomorphic
collision controls, including z^2-2t. Thus there is no failed premise
that could turn this disk bound into an exclusion. The full-strip
argument additionally requires an even smooth source with the displayed
integrable derivatives. Euler-factor translated smooth sources satisfy
this analytic premise; they change canonical arithmetic. Reflected
super-Gaussian and smooth positive-primitive controls also satisfy it;
they lack unchanged canonical square coefficients. Weighted-square and
finite-prime controls satisfy the local/disk statement and can meet the
whole-strip W^{2,1} hypothesis by the explicit zero-endpoint check above;
they fail unchanged normalized complete reflection. None gains that
reflection just by using an even extension in a Fourier integral.
Atomic cosine controls can satisfy the disk
bound but fail the whole-line source-derivative L1 hypothesis; they are
not tests of (14). BW10's close smooth endpoint controls preserve these
analytic bounds while failing ordinary Dirichlet-series arithmetic.
The exact preservation lists remain those in result-summary 12.

The useful gain is a complete uniform upper for this weighted integral,
including an entire horizontal strip; the original logarithmically
divergent unweighted energy and the sibling signed or ratio consumers
remain open on their existing gates. Finiteness of this derivative-weighted
integral does not distinguish simple, multiple, real or nonreal zeros.

## 6. A root-free compact-cutoff consumer and its source error

Let psi>=0 be compactly supported and C^2, with H holomorphic on a
neighborhood of its support. The exact distribution identity (3) gives

\[
 W_\psi(H):=2\int\psi\frac{|H'|^2}{|H|}\,dA
                =2\int|H|\Delta\psi\,dA.                 \tag{23}
\]

Both integrals are finite, including arbitrary multiple zeros. On the
right retain the signed Delta psi; replacing it everywhere by its
absolute value needlessly discards the exact cancellation. If P is a
holomorphic approximant and sup_supp(psi)|H-P|<=epsilon, then

\[
 \boxed{|W_\psi(H)-W_\psi(P)|
                 \le2\epsilon\|\Delta\psi\|_{L^1}.}      \tag{24}
\]

This follows from ||H|-|P||<=|H-P| directly in (23). No root, unit,
branch, coefficient of a deflation, or derivative error is needed for
this particular source-to-consumer transfer. The equality (23), applied
to P as well, remains available to a matched direct estimator. If
P=0 identically define its observable to be zero.

For a disk centered at C with radius R reuse the explicit C^2 cutoff
from the I4/07 weighted-Green program linked in Section 5:

\[
 \psi_R(z)=(1-|z-C|^2/R^2)_+^3.
\]

With s=|z-C|^2/R^2, differentiation inside s<1 gives

\[
 \Delta\psi_R=\frac{12}{R^2}(1-s)(3s-1),\qquad
 \|\Delta\psi_R\|_1=\frac{32\pi}{9}.                    \tag{25}
\]

The first and second derivatives match zero at s=1, so there is no
boundary measure. For the norm, dA=pi R^2 ds and the sign changes at
s=1/3; integrating the two polynomial pieces gives
12pi(8/27)=32pi/9. In particular

\[
 \boxed{|W_{\psi_R}(H)-W_{\psi_R}(P)|
                      \le\frac{64\pi}{9}\epsilon,}
 \quad
 0\le W_{\psi_R}(H)\le\frac{32\pi}{9}
                               \sup_{D(C,R)}|H|.         \tag{26}
\]

For the upper bound use integral Delta psi=0 and bound only its positive
part in (23). The polynomial integrand on the right of (23) is bounded
and continuous even across zeros, making this a useful independent
acquisition contract. A full interval still needs the finite-polynomial
modulus integral and coefficient-ball propagation; (26) pays only the
complete source replacement error.

The existing actual regular theta fiber [Note 04, Section 3](04_ACTUAL_REGULAR_THETA_FIBER_COMPARISON_20261022.md)
has t=0, C=35, R=8 and a degree-64 Taylor oracle with all coefficient
balls retained. Its complete disk source error is epsilon_H<1.384e-20.
Consequently (26) gives

\[
 |W_{\psi_8}(H_0)-W_{\psi_8}(P_{64})|<3.10\times10^{-19}.
                                                               \tag{27}
\]

This is a new declared integral consumer for an existing complete source
contract, with no new source evaluation. Coefficient balls and the
signed finite integral remain to be enclosed if an actual value is
wanted. It neither updates the original reciprocal-energy intervals nor
asserts a source-error advantage over a direct method using the same
identity. Its quantitative gain is the collision-stable transfer bound,
not a simplicity exclusion.
