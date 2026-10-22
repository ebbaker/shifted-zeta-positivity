# Topological mass bounds and the index-theorem interface

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from the active turn metadata.

**Purpose:** use the topological integral to bound relevant analytic
integrals, independently of noncollision. This follows the user's explicit
clarification and question about Atiyah–Singer. **Status: finite-regularization
mass and bounded-weight estimates proved in-note; the exact interface to the
existing spatial Gauss-area integral is derived, with its inverse cost
retained. No theta-specific improvement or analytic-index identification.**

Use [Note 03][n3] for the full physical boundary and source constants;
[BW10 MC7–MC9][mc] already provides the nonnegative bulk density. The
[program][program] and [plan][plan] track this independent estimating task.
Read the [result index][results], [avoid index][avoid], [coupled-estimate
rule][a12], [full-target rule][a13] and [geometric-comparison rule][a03].
[Review 05][review] is contributing-agent same-model review.

## 1. The evaluated integral already available

For the physical jet G=(H,H_z), E=|G|² and delta>0, set
\[
 \omega_\delta={i\over2\pi}\partial\bar\partial\log(E+\delta^2),
 \quad\mathcal A_\delta={\operatorname{Im}(G^*dG)\over E+\delta^2},
 \quad\mathcal C_\delta={\mathcal A_\delta\wedge d\mathcal A_\delta\over4\pi^2}.
\]
The derivatives involve **both** complex heat time and spectral position.
The inherited identity, with J=H_zH_zzz-H_zz²=det_C DG, is
\[
 d\mu_\delta:=\omega_\delta^2
   ={2\delta^2|J|^2\over\pi^2(E+\delta^2)^3}\,dV\ge0,
 \qquad \mu_\delta(W)=\int_{\partial W}\mathcal C_\delta. \tag{1}
\]
For a complete regular boundary its unregularized charge is
\[
 Q=\int_{\partial W}\mathcal C.
\]
In Note 03's proper one-critical-branch window, Q=wind V; at its hypothetical
ordinary double Q=1. This is an exact evaluated invariant, not merely a
formal label for a three-form. The quadratic control independently checks
the complete boundary value; it does not supply canonical theta data.

Take the actual E floor e_0, operator bound L and full boundary area S
from Note 03 (13)–(14), or independently proved bounds with the same meaning.
Because C_delta=(E/(E+delta²))² C,
\[
 \boxed{\left|\mu_\delta(W)-Q\right|\le B_\delta,\qquad
 B_\delta=\left[1-\left({e_0\over e_0+\delta^2}\right)^2\right]
              {SL^3\over2\pi^2e_0^{3/2}}
 \le {SL^3\delta^2\over\pi^2e_0^{5/2}}.}                 \tag{2}
\]
Thus max(0,Q-B_delta)<=mu_delta(W)<=Q+B_delta. No positivity of individual
boundary faces is assumed: the bulk is nonnegative, while its complete
signed boundary value is evaluated before applying the error bound.
For Q=0 this is an O(delta²) mass bound; for Q=1 the mass tends to one.
The constants belong to the fixed paid window, not a free shrinking family.

## 2. A concrete class of integrals bounded by the invariant

For any measurable real weight 0<=w<=W_0 on W,
\[
 \boxed{0\le\int_W w\,d\mu_\delta\le W_0(Q+B_\delta).}   \tag{3}
\]
For real or complex |w|<=W_0, the same right side bounds the absolute
weighted integral. This requires no derivatives of w. It directly bounds
\[
 \int_W w\,{|H_zH_{zzz}-H_{zz}^{\,2}|^2\over(E+\delta^2)^3}\,dV
 \le {\pi^2 W_0\over2\delta^2}(Q+B_\delta)               \tag{4}
\]
for nonnegative w, with the analogous absolute-value statement for bounded
signed weights. The displayed delta^(-2) cost is retained. A constant
weight gives the mass identity and bound; it does not make the unnormalized
integral bounded uniformly as delta goes to zero at an event.

If w is bounded and continuous at each of finitely many isolated interior
events, the inherited concentration formula yields
\[
 \lim_{\delta\downarrow0}\int_Ww\,d\mu_\delta
                  =\sum_p q_p w(p),\qquad q_p=\binom{m_p}{2}
                                                               \tag{5}
\]
for the heat-family local event multiplicities covered by MC4–MC9. In the
ordinary-double window this is exactly w(0,a). Off small event neighborhoods,
E has a positive floor and the density in (1) is O(delta²); the local mass
limits and positivity prove (5). Continuity, not just measurability, is
needed for this evaluated weighted limit.

A finite version for one event p is useful. Let |w|<=W_0 and let
omega_w(rho) bound |w(x)-w(p)| on a neighborhood U_rho. If an actual
E>=e_rho>0 and |J|<=J_max hold on W minus U_rho, put
\[
 D_{\rho,\delta}={2\delta^2\operatorname{Vol}(W\setminus U_\rho)
                         J_{\max}^2\over\pi^2e_\rho^3}.
\]
Splitting the weighted integral and using (2) gives
\[
 \left|\int_Ww\,d\mu_\delta-w(p)Q\right|
 \le\omega_w(\rho)(Q+B_\delta)
                   +2W_0D_{\rho,\delta}+W_0B_\delta.      \tag{6}
\]
The exterior floor and modulus of continuity are additional paid inputs,
not consequences of a boundary floor alone.

Two limitations matter. A singular weight such as E^(-1) is not covered
by a uniform W_0 near an event. And for C¹ weights, exact weighted Stokes is
\[
 \int_Ww\,d\mu_\delta
   =\int_{\partial W}w\mathcal C_\delta-\int_Wdw\wedge\mathcal C_\delta.
                                                               \tag{7}
\]
The derivative term cannot be discarded. Equations (3)–(6) avoid doing so
by using the positive bulk measure directly.

## 3. The existing BW10 Gauss-area integral: exact comparison and cost

[BW10 Note 24, GA1][gauss] uses the spatial density
\[
 g_2={|D|^2\over E^2},\qquad D=HH_{zz}-H_z^2,
 \qquad d\mu_t^{\rm Gauss}=g_2\,dA_z.
\]
This is not the four-dimensional determinant J in (1). Let
K_delta be the complex Hermitian Hessian of log(E+delta²). Its spatial entry
and determinant are
\[
 (K_\delta)_{z\bar z}
 ={\mathcal N_\delta\over(E+\delta^2)^2},\quad
 \mathcal N_\delta=|D|^2+\delta^2(|H_z|^2+|H_{zz}|^2),
 \quad \det K_\delta={\delta^2|J|^2\over(E+\delta^2)^3}.    \tag{8}
\]
These follow from the two-vector Gram determinant identity. In particular
\[
 \left.\omega_\delta\right|_{\tau=\mathrm{constant}}=\gamma_\delta\,dA_z,
 \qquad \gamma_\delta={(K_\delta)_{z\bar z}\over\pi}.
\]
Where the spatial entry is positive, define the Schur complement
\[
 s_\delta=(K_\delta)_{\tau\bar\tau}
       -{|(K_\delta)_{\tau\bar z}|^2\over(K_\delta)_{z\bar z}}
       ={\delta^2|J|^2\over(E+\delta^2)\mathcal N_\delta}. \tag{9}
\]
Then **exactly**
\[
              d\mu_\delta={2\over\pi}s_\delta\gamma_\delta\,dV.
                                                               \tag{10}
\]
A proved s_delta>=c_delta>0 gives the concrete comparison
\[
 \int_W\gamma_\delta\,dV
       \le {\pi\over2c_\delta}(Q+B_\delta).               \tag{11}
\]
This bounds spatial regularized curvature **averaged over complex heat
area**. It is not automatically a bound on one fixed-time slice; transferring
an average to such a slice requires another estimate.

The existing ordinary-double contract already supplies such a lower bound
**uniform across W for each fixed delta>0**. Using the constants of Note 03,
put
\[
 M_0=D_2(d+R^2/2),\quad U_0=M_0^2+\epsilon_1^2,
 \quad j_0=37h^2/64,
\]
\[
 N_\delta^+=(M_0D_2+\epsilon_1^2)^2+
                   \delta^2(\epsilon_1^2+D_2^2),\qquad
 c_\delta={\delta^2j_0^2\over(U_0+\delta^2)N_\delta^+}>0. \tag{12}
\]
Taylor expansion at tau=0 and the heat equation give |H|<=M_0, hence
E<=U_0 and N_delta<=N_delta^+. Also epsilon_2<=h/8, while J_0 R<=h/4
implies epsilon_1 D_3<=epsilon_1 C_0<=3h²/16. Therefore
\[
 |J|\ge(h-\epsilon_2)^2-\epsilon_1D_3\ge37h^2/64=j_0.
\]
Moreover N_delta>=delta²|H_zz|²>=49delta²h²/64>0, so the Schur
complement is defined throughout W. Substitution into (9) proves (12)
and makes (11) an explicit finite-delta bound. This lower bound across W is distinct from a positive lower bound
independent of delta.

At a fixed regular point with D!=0 and J!=0, (9) has positive order delta².
The natural inverse comparison therefore costs order delta^(-2) there.
At delta=0 the curvature is pulled back from CP^1 and has rank at most one;
its square vanishes off events. This rank loss explains the cost rather
than removing it. A comparison uniform as delta tends to zero requires
a different paid hypothesis, weight or normalization. The formula is an identified interface,
not an already established improvement over the direct Gauss-area bound.

**Scoped controls.** The exact heat field H=z has E=1+|z|²,
g_2=(1+|z|²)^(-2)>0, but J=0 and mu_delta=0 for every delta. Consequently
there is no universal domination of the spatial Gauss area by this bulk
mass across all holomorphic heat fields. Conversely H=z²-2tau at
(tau,z)=(1/2,i) has D=0 and J=-4, excluding the reverse unweighted
pointwise domination. A constant nonzero heat field has arbitrary scalar
amplitude and zero bulk mass. These controls lack canonical theta
arithmetic; they do not rule out additional theta-specific comparisons.

## 4. What an Atiyah–Singer route would add

The current proof uses relative degree/local intersection multiplicity,
Chern–Weil forms and Stokes. [Whitehead's Hopf integral formula][whitehead]
is the background normalization; it is not an elliptic-operator construction.

The original [Atiyah–Singer paper][as] identifies the index of an elliptic
operator with topological data. To use such an analytic-index realization
here, one must specify an operator and symbol class, a Fredholm domain and
boundary conditions, and prove that its local index density gives the
particular analytic integral being estimated. No such identification for
this physical jet observation has been made in the current work.

Our window has a boundary (and corners). The original [Atiyah–Patodi–Singer
paper, introduction and boundary-value construction][aps] explains the
spectral boundary contribution and global boundary conditions. Invoking
that theorem would require paying those data, compatible collar geometry
and corner treatment, or a justified doubling construction. It would not
by itself delete a boundary correction or dominate an unrelated integrand.
Also distinguish an elliptic operator's heat-kernel parameter from the
physical backwards heat variable tau in H_tau=-H_zz.

This does not close an index route. It specifies its acceptance contract:
identify the exact operator/integral bridge and a boundary correction with
a useful bound. Until then, (2)–(12) are concrete estimating tools available
without that additional construction. No literature-priority claim is made.

## 5. Next estimating task and same-information comparison

The user wants topology to help bound the project's existing integrals,
not only to exclude events. The new CHB-07 task therefore proceeds
independently of the simplicity gates:

1. Select a named target integral, with its dimension, weight, domain,
   normalization and direction of estimate. The BW10 GA1 interface in
   (8)–(11) is the first concrete candidate; scalar and arithmetic norms
   require their own bridges.
2. Test a weight or coherent estimate that pays the Schur-complement
   inverse cost, or show a scoped failure. Do not infer a fixed-time bound
   from a complex-time average or drop the mixed entry of K_delta.
3. Give the direct method the same critical trace, source moments, window,
   source tails and rounding. Measure the complete bound, not just the
   simplified integrand. Parameterized geometry is not actual acquisition.
4. If an index approach is proposed, supply the operator, exact density
   comparison and full boundary payment before calling it an estimate.

The finite-height moving-contour proposal is audited in Note 03 §7.
Preserving total spatial multiplicity does not exclude a collision, but
that observation does not diminish the independent use of (2)–(12) as
bounds on their specified analytic integrals.

[n3]: 03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[program]: ../research-overview/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PROGRAM_20261022.md
[plan]: ../research-progress/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PLAN_AND_PROGRESS_20261022.md
[review]: ../03_heat_transport_and_charges/reviews/05_COMPLETE_BOUNDARY_AND_INTEGRAL_BOUNDS_REVIEW_20261022.md
[results]: ../../../result-summaries/README.md
[avoid]: ../../../avoid/README.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a13]: ../../../avoid/13_a_factor_is_not_the_target.md
[a03]: ../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[mc]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[gauss]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md
[whitehead]: https://arxiv.org/pdf/0912.4974
[as]: https://annals.math.princeton.edu/1968/87-3/p05
[aps]: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps001.pdf
