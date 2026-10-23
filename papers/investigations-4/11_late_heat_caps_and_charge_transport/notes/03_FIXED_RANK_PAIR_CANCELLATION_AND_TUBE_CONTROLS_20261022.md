# Fixed-rank pair cancellation and exact projective-tube controls

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**. Status: **proved in-note; separate same-model internal review**. No independent specialist review.

This note proves a quantitative limitation of the optional pair-statistics
route: for every fixed finite consecutive theta-root cluster, the
inverse-square pair term diverges like a positive constant times L^2,
while the complete discriminant derivative is negative and only of order
1/kappa. The exterior holomorphic unit therefore cancels the large pair
term. The result is about the actual canonical late-time field, using the
existing differentiated saddle theorem; it is not a growing-population
theorem and does not estimate a complex-time cap. An exact quadratic
control then checks the root-tube cap and its attachment obligation.

Read the [result index][results], [avoid index][avoid],
[collision controls][controls], [target classification][a01],
[scope rule][a07] and [coupled-error rule][a12]. The target classification
is a quantitative finite-rank milestone and a scoped limitation on
separate pair/unit estimation, not an RH-equivalent criterion.

## 1. Fixed population and physical statistic

Fix integers ell>=0 and m>=2, and put K=ell+m. For all sufficiently large
real t, let x_j(t), ell+1<=j<=ell+m, be the indicated positive theta roots.
The [differentiated saddle theorem][saddle] proves their simplicity and
rank identification unconditionally. Let

\[
 s_j=(j-\tfrac12)\pi,\qquad
 4\pi e^{4L}=2tL+9,\qquad
 \kappa=8tL-2t+36,\qquad L'=2L/\kappa.
\]

On a local proper neighborhood of this finite cluster, factor

\[
 H(\tau,z)=U(\tau,z)\prod_{j=\ell+1}^{\ell+m}(z-x_j(\tau)),
 \qquad b_j=U_z/U(\tau,x_j(\tau)).
\]

Only a local regular-time factorization is needed. No infinite zero
product or unregularized global pair sum is used. Put

\[
 \Delta=\prod_{i<j}(x_j-x_i)^2,\quad
 D=\Delta'/\Delta,\quad
 P=8\sum_{i<j}(x_j-x_i)^{-2},\quad
 B=4\sum_{i<j}\frac{b_j-b_i}{x_j-x_i}.
 \tag{1}
\]

The inherited exact heat identity is D=P+B. Its physical inverse-square
weight and fixed population are explicit. The gaps here have scale 1/L;
normalizing their empirical distribution does not change the L^2 factor
in P.

## 2. A finite bound and its asymptotic consequence

Use the actual finite saddle allowances with this K and a fixed
0<beta<pi/4. In the notation of that theorem, let

\[
 e=\arcsin\epsilon_0,\qquad E=\mathcal E_K(t),
 \qquad |Lx_j-s_j|\le e,\qquad
 |x_j'+s_jL'/L^2|\le E.
 \tag{2}
\]

All finite conditions of the source theorem are retained; in particular
e<beta<pi/4. Define

\[
 A_1(e)=\sum_{d=1}^{m-1}\frac{m-d}{\pi d-2e},\qquad
 R=4\bigl(eL'/L+LE\bigr)A_1(e),
\]
\[
 P_- =8L^2\sum_{d=1}^{m-1}\frac{m-d}{(\pi d+2e)^2},
 \qquad
 P_+ =8L^2\sum_{d=1}^{m-1}\frac{m-d}{(\pi d-2e)^2}.
 \tag{3}
\]

Then

\[
 \boxed{|D+m(m-1)L'/L|\le R,\qquad P_-\le P\le P_+.}
 \tag{4}
\]

Consequently the exterior-unit contribution has the complete finite
enclosure

\[
 -m(m-1)L'/L-R-P_+\le B
 \le-m(m-1)L'/L+R-P_-.
 \tag{5}
\]

**Proof.** For a pair i<j, write d_ij=(j-i)pi and
L(x_j-x_i)=d_ij+delta_ij, where |delta_ij|<=2e. The derivative of the
unscaled gap x_j-x_i is
-(d_ij)L'/L^2+eta_ij with |eta_ij|<=2E. Therefore

\[
 \left|\frac{x_j'-x_i'}{x_j-x_i}+\frac{L'}L\right|
 \le\frac{2eL'/L+2LE}{d_{ij}-2e}.
\]

Summing twice gives the first assertion of (4); counting the m-d pairs
at label distance d gives (3). The gap bounds give the second assertion
of (4), and D=P+B gives (5). This derivation differentiates the roots
using the established velocity estimate; it does not differentiate an
uncontrolled location remainder.

The saddle theorem gives e=O_K(1/(L sqrt(kappa))),
E=O_K(1/(L kappa^(5/4))), and L'/L=2/kappa. Hence, with
A_m=sum_(d=1)^(m-1)(m-d)/d^2,

\[
 \boxed{
 D=-\frac{2m(m-1)}\kappa+O_K(\kappa^{-5/4}),\qquad
 P=\frac{8A_m}{\pi^2}L^2\left[1+O_K\!\left(
             \frac1{L\sqrt\kappa}\right)\right].}
 \tag{6}
\]

In particular D<0 eventually, while P tends to positive infinity. More
precisely,

\[
 B=-P-\frac{2m(m-1)}\kappa+O_K(\kappa^{-5/4}),\qquad
 \frac{|D|}{P}\sim
 \frac{\pi^2m(m-1)}{4A_m\kappa L^2}.
 \tag{7}
\]

Thus a pair law accurate to relative o(1) does not resolve this sign.
For worst-case independent symmetric perturbations about the exact P
and B values, preserving this negative sign requires their total
perturbation radius to be less than |D|, which is of order 1/kappa.
Equivalently, if those perturbation radii are specified relatively to
the individual order-L^2 terms, their sum must be of order
1/(kappa L^2) or smaller. This condition-number statement concerns the
specified separate symmetric perturbations; it is not a necessity
theorem for arbitrary shifted or one-sided enclosures, a lower bound
on the actual coupled error, or an exclusion of every possible method.

Equation (6) supplies an actual finite-rank weighted statistic, but does
not provide a growing-rank estimate, small-gap uniform integrability,
outer-zero tails for an infinite population, or complex-time phase.
The direct cap argument can bypass this optional route.

## 3. Exact quadratic q tubes and the pinch threshold

For the ordinary-double control H=z^2-2tau, use the physical jet
G=(H,H_z) and q=H/H_z=z/2-tau/z. The inverse branches are exactly

\[
 z_\pm(\tau,q)=q\pm\sqrt{q^2+2\tau}.
 \tag{8}
\]

On a simply connected heat rectangle with t>=t_0>0, the branches are
holomorphic and disjoint for |q|<=epsilon whenever epsilon^2<2t_0.
Indeed q^2+2tau is nonzero there, has a holomorphic square root, and
z_+z_-=-2tau is nonzero. The derivative dz/dq=z/(z-q) is also nonzero.
The images of the closed q disks are therefore regular embedded disks,
H_z never vanishes on them, and the projective-circle side has zero
curvature and zero Chern–Hopf flux.

At q=0, H_z=2z_\pm=+/-2 sqrt(2tau). With
kappa_epsilon=epsilon^2/(1+epsilon^2), the exact forward cap formula on
t=T and -Y<=s<=Y is

\[
 I_{T,\pm}=\frac{\kappa_\epsilon}{2\pi}
   \Delta_s\arg H_z(T+is,z_\pm(T+is,0))
 =\frac{\kappa_\epsilon}{2\pi}\arctan(Y/T).
 \tag{9}
\]

To check the first equality directly, in the H_z chart write
A=eta_z+a_q and C=eta_z wedge da_q/(4pi^2). The nonzero holomorphic
ratio H_z(tau,z_\pm(tau,q))/H_z(tau,z_\pm(tau,0)) has a logarithm on
the q disk. Angular averaging kills its exact q-dependent logarithm in
the cap integral, while the disk integral of da_q is 2pi kappa_epsilon.
The orientation is increasing s followed by complex q orientation.

The combined two-root cap is therefore

\[
 \boxed{I_T^{\rm tubes}=\frac{\kappa_\epsilon}{\pi}
                           \arctan(Y/T).}
 \tag{10}
\]

For this tube pair, the early cap and the two imaginary-time faces
balance (10) exactly because there is no event in t>=t_0. This does not
transport the event at tau=0 into the two root disks. The inverse map
loses regularity at q=+/-i sqrt(2tau), the two critical values of q(z).
Consequently a fixed epsilon disk first meets a branch point at the
real time tau=epsilon^2/2 when continued backward. A fixed positive
q-radius disk bundle cannot reach the double in this chart.

This is a fiberwise failure, not necessarily a singularity of the full
three-dimensional level side: at those branch points q_tau=-1/z is
nonzero. The total level hypersurface can remain smooth while its
spatial-fiber topology changes. A continuation allowing that change
needs a new attachment analysis and does not retain the assumed two
disjoint univalent disk fibers.

The quadratic control therefore accepts a small or vanishing distant
root-tube cap and zero projective-side flux while retaining the ordinary
event's full linking charge one. A joining piece, chart complement, or
initial/linking cap carries the missing charge. This is a specific
control of the proposed root-tube attachment, not a universal
obstruction to other complete geometries.

## 4. Control scope and LHCT status

The cosine heat control has simple clock roots and a nonzero physical
cap, so separation alone cannot set a reference flux to zero. The
quadratic calculation above checks the exact q-tube orientation and
backward pinch. The inherited projective shell retains its shrinking
inner-cap flux. These three controls do not have the unchanged complete
theta source.

The differentiated saddle input used in (6) has source-specific complete
theta allowances. Euler-factor controls change that source; weighted
square and finite-prime controls fail its full source reflection;
reflected super-Gaussian and positive-primitive controls lack its
unchanged integer-square expansion. Close positive endpoint controls
can share qualitative saddle concentration but fail ordinary
Dirichlet-series arithmetic. No new late-time law is assigned to any
control. In particular the present cancellation theorem is not claimed
to distinguish theta from every such control.

The [internal review][review] checks these constants and scopes. LHCT-04 is **partial in a proved fixed-rank scope**: its actual weighted
statistic and exterior-unit cancellation are now quantified. The
statistical-to-cap bridge remains unproved and is unnecessary for a
direct complex-time jet estimate. No LHCT-05 complete boundary payment,
LHCT-06 exclusion margin, or LHCT-07 coverage theorem follows.

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[saddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md

[review]: ../reviews/03_FINITE_TUBES_CAPS_AND_CLOSURES_INTERNAL_REVIEW_20261022.md
