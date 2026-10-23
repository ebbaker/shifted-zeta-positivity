# Growing complex caps and the Vandermonde phase

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**, checked against this turn's metadata. Same-assistant derivation and self-review only.

**Status: proved in the new maintained manuscript, within its stated geometry and asymptotic regime.** This continuation implements the user's request for a separate readable paper organized around the physical topological formula, the Vandermonde contribution to the terminal cap, and moving boundaries. The existing catalogue manuscript is preserved. The additional manuscript is a maintained sibling, not a snapshot:

- [PDF](../manuscript/topological_zero_transport/main.pdf)
- [Source and guide](../manuscript/topological_zero_transport/README.md)
- [Literature and proof self-review](../reviews/04_TOPOLOGICAL_TRANSPORT_LITERATURE_AND_PROOF_REVIEW_20261023.md)

The [result index](../../../result-summaries/README.md), [heat-geometry summary](../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../avoid/README.md), [target classification](../../../avoid/01_restating_the_target.md), [coupled estimates](../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [distinct targets](../../../avoid/13_a_factor_is_not_the_target.md), and [literature discipline](../../../avoid/16_unchecked_imports_and_novelty_claims.md) govern this work. This is a quantitative analytic milestone, not an RH-equivalent criterion or an event-exclusion theorem.

## 1. The physical formula stays the central object

For G=(H,H_z), A=Im(G* dG)/|G|², and C=A∧dA/(4π²), the complete event-domain identity is

\[
\boxed{I_0=\frac{k_\epsilon}{2\pi}\operatorname{Im}
 \int_{T-iY}^{T+iY}d\log(\Delta\mathscr U)
 +J_++J_-+R-Q,\qquad
 Q=\sum_p\binom{m_p}{2}.}
\]

Here k_epsilon=epsilon²/(1+epsilon²), Delta is the squared Vandermonde of the terminal tracked roots, and script-U is the product of the remaining analytic factor evaluated at those roots. The initial cap is forward-oriented; the upper and lower imaginary-time faces and the remaining spatial/joining faces are outward-oriented. Every external three-face is included.

The exact scalar is D=product H_z(tau,z_j(tau))=(-1)^(m(m-1)/2) Delta script-U. A common fixed projective radius |H/H_z|=epsilon gives exactly zero side flux on each regular root tube. It does not remove the imaginary-time faces or the joining complement. The real one-dimensional angular integral from [Note 11](11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md) is a different observable and is not substituted for I_0.

The new paper includes the local heat degree, the sphere-volume normalization, the exact phase reduction by harmonic averaging, and the complete transport theorem. These ingredients were already present in the archive or are classical; they are not the new quantitative gain.

## 2. The linear-population Vandermonde estimate

For c_j=c_1+(j-1)pi and w_j=c_j+delta_j with |delta_j|<=eta<=pi/8, the continuous logarithm obeys

\[
\left|\log\frac{\Delta(w)}{\Delta(c)}\right|
\le\frac{4(m-1)}\pi\eta+\frac{8m}{9}\eta^2\le2m\eta.
\]

The important operation is to sum the linear term before taking absolute values:

\[
\sum_{i<j}\frac{\delta_j-\delta_i}{j-i}
=\sum_j\delta_j(H_{j-1}-H_{m-j}),\qquad
\sum_j|H_{j-1}-H_{m-j}|\le2(m-1).
\]

The quadratic logarithm remainder costs sum_(d=1)^(m-1)(m-d)/d²<=m pi²/6. This avoids both a quadratic population cost and the harmonic logarithm in the naive pairwise phase bound. It is an elementary estimate with declared constants; neither constant optimality nor priority is claimed.

## 3. Growing-rank complex-time caps from the unchanged source

Let 4pi exp(4L)=2TL+9 and kappa=8TL-2T+36. The existing full-source concentration proof gives
E[|U-L|^j exp(a|U-L|/L)]=O_a(kappa^(-j/2)) for fixed a and j=1,2,3. The manuscript reproves the tail and normalization estimates, retaining every theta index.

The useful refinement is geometric. The disks surrounding clock roots have bounded imaginary part even when their real centers grow. The trigonometric error therefore contains exp(a), with a fixed, instead of exp(pi K). On |Im w|<=a, |w|<=Z, and |s|<=Y, the full finite bound is

\[
|\partial_w^j F-e^{isL^2}\partial_w^j\cos w|
\le e^a\left[\sum_{k=1}^j\binom jk\frac{M_k}{L^k}
 +\frac{ZM_1}{L}+Y(2LM_1+M_2)\right],
\]

where F=H(T+is,w/L)/H(T,0) and M_k are the weighted complete moments. Taking Z<=pi K+1 makes the error

\[
e_T=O_Y\left(\frac{K+1+L^2}{L\sqrt\kappa}\right)=o(1)
\quad\text{when }K=o(L\sqrt\kappa).
\]

Uniform Rouché disks then give actual disjoint inverse caps, fixed rank labels, and a near-one logarithm for
H_z/[H(T,0)L(-sin s_j)exp(isL²)]. Thus, for a consecutive block of m<=K roots and epsilon=r/L, 0<r<1/4,

\[
\frac{I_{T,m}}m=\frac{r^2YL^2}{\pi(L^2+r^2)}
 +O_Y\left(\frac{r^2e_T}{L^2}\right),\qquad
\frac{|I_{T,m}^{\Delta}|}m=O_Y\left(\frac{r^2e_T}{L^2}\right).
\]

The analytic factor supplies the leading r²Y/pi per root. This is a bound on that extra contribution, not permission to omit it. The large phase YL² is continuously lifted; principal endpoint arguments would give a false formula after winding.

For Y_T=S/L², the full cap per root is O(L^-2), even for the growing population. The unnormalized cap need not tend to zero unless the population is restricted further, for example m=o(L²).

## 4. Edge asymptotics and the distinction between two boundaries

For a fixed 0<theta<1, hold the population fixed on each interval [theta T,T] and use the same physical radius epsilon=r/L_T throughout its tubes. The source estimates are uniform on that interval, so the inverse disks patch to holomorphic regular tubes. The exact identity J_+=J_-=(I_thetaT-I_T)/2 gives

\[
\frac{J_\pm}{m}
=\frac{r^2Y(L_{\theta T}^2-L_T^2)}{2\pi(L_T^2+r^2)}
 +O_{Y,\theta}(r^2e_T/L_T^2)
=-\frac{r^2Y\log(1/\theta)}{4\pi L_T}+o(L_T^{-1}).
\]

This is a proved relative bound on complete imaginary-time faces of a late regular tube. Since L_T~log T/4, it is O(1/log T) per root. For K=floor(sqrt(kappa)), the spatial extent K/L also tends to infinity: the result covers a joint large-heat and growing-height regime. It is not a fixed-heat, all-height estimate.

For a fixed event core, the situation differs. If |G|>=b and ||DG||<=D on its initial, joining and local spatial faces, then their total absolute flux is <=BY, with B=D³(4pi R²+4pi Ra)/(2pi²b³). Real symmetry and degree give the exact allocation

\[
J_+=J_-=(Q-I_T-R_T^{\rm all})/2,\qquad |R_T^{\rm all}|\le BY.
\]

With Y=S/L², the two imaginary-time faces tend to Q/2 with error O((B+m)/L²). At fixed admissible Y they have the nonzero limits stated in manuscript Theorem 5.1. These estimates characterize the surviving contribution; since they contain Q, they are not an independent bound on Q. Core constants have not been bounded uniformly as height grows.

## 5. Literature and controls

The new manuscript has 17 external references plus the research archive, with the relevant comparisons in its introduction. The [review](../reviews/04_TOPOLOGICAL_TRANSPORT_LITERATURE_AND_PROOF_REVIEW_20261023.md) records the search scope and source access. Major overlaps include classical degree/Hopf transgression, resultant-discriminant identities, heat-zero motion, caloric multiple-zero isolation, and integration of a Hopf form along fibers. The narrower candidate contribution is the physical boundary estimate uniform over growing canonical populations and its complete flux allocation. The search is not a proof of novelty, and no improved RH or Newman-constant bound is obtained.

The [small diagnostic record](../numerics/TOPOLOGICAL_CAP_CHECKS_20261023.json) has 105 adversarial/random Vandermonde cases, a direct quadratic disk pullback, a phase-winding control, and saddle-reference checks. Maximum direct-cap discrepancy was about 8.62e-11; these are floating checks, not theta computations or interval certificates. The proof does not depend on them.

The quadratic heat event retains charge one with a small terminal cap and zero projective sides. A stationary sine root population retains a nonzero cap entirely in its analytic factor. The generic identities accept the [collision controls](../../../result-summaries/12_collision_controls_and_screening.md). Euler-factor controls alter the source, weighted-square/finite-prime controls lack the unchanged normalized reflection or coefficients, reflected/positive-primitive controls lack the canonical square expansion, and close positive endpoint controls need not have ordinary Dirichlet arithmetic. The actual asymptotic proof only uses the explicit source bounds; it does not claim to reject every noncanonical source with analogous concentration.

**Next task:** obtain a height-dependent upper bound for the complete early attachment/imaginary-time contribution, and an independently useful lower bound for the fixed initial cap. A relative event budget is an acceptable goal. Neither the real early layer of Note 11 nor this full physical early boundary is closed by the present late estimates.
