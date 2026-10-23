# Localized root-cover energy and analytic manuscript extensions

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

**Subsequent completion, 22 October 2026:** [Note 09](09_SHARP_C2_DIVISOR_STABILITY_20261022.md) proves the fixed-disk C² candidates with a stronger bias coefficient; [Note 10](10_GROWING_CLOCK_WINDOWS_20261022.md) extracts the growing spatial clock corollary. The historical text below is retained; its candidate/open or fixed-rank-only wording describes the earlier checkpoint. Continuation provenance: gpt-6-astra, effort max; same-assistant self-review only.

**Status: proved in the maintained manuscript under the hypotheses below; internal same-model reviews only.** This note records the analytic extensions and their relation to the earlier transport and reciprocal-Hodge work. The complete proofs are in [Zero Counts, Heat Transport, and Localized Hodge Energy](../manuscript/zero_count_heat_transport/main.tex), with [reader guide](../manuscript/zero_count_heat_transport/README.md), [review](../reviews/01_ZERO_COUNT_HEAT_TRANSPORT_MANUSCRIPT_REVIEW_20261022.md), [program](../research-overview/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRAM_20261022.md), and [progress](../research-progress/04_ZERO_COUNT_HEAT_TRANSPORT_AND_HODGE_PROGRESS_20261022.md). There is no mathematical priority claim, independent specialist review, RH conclusion, or endpoint-simplicity result.

The [result index](../../../result-summaries/README.md), [avoid index](../../../avoid/README.md), [collision controls](../../../result-summaries/12_collision_controls_and_screening.md), and patterns [01](../../../avoid/01_restating_the_target.md), [12](../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [13](../../../avoid/13_a_factor_is_not_the_target.md) apply. The gains are explicit identities, constants, and scoped estimates; the unproved signed-boundary task is not renamed as a theorem.

## 1. Exact low-value powers and root-cover energies

Let Omega be a bounded connected planar domain with finitely many piecewise smooth Jordan boundary components, and let f be holomorphic near its closure. Suppose b=min_boundary |f|>0, and let N count interior zeros with multiplicity. The homotopy f−sw shows that f has valence N over every target value |w|<b. The holomorphic area formula consequently gives, for p>0 and 0<epsilon<b,

\[
 \int_{\Omega\cap\{|f|<\epsilon\}}|f'|^2|f|^{p-2}\,dA
       =\frac{2\pi}{p}\epsilon^pN. \tag{1}
\]

Near an m-fold zero the density is O(|z-a|^(mp-2)), so (1) is locally finite for every m>=1. In particular

\[
 W_{<\epsilon}=2\int_{|f|<\epsilon}\frac{|f'|^2}{|f|}\,dA
          =4\pi\epsilon N,\qquad W\ge4\pi bN. \tag{2}
\]

On the normalization of w^q=f, q>=1, the exact differential eta_q=q dw is regular even over a multiple zero. Its energy over |w|^q<epsilon is

\[
 \mathcal E_{q,<\epsilon}
 =q\int_{|f|<\epsilon}|f'|^2|f|^{2/q-2}\,dA
 =\pi q^2\epsilon^{2/q}N. \tag{3}
\]

The q=2 case is precisely (2). Disconnected normalizations are allowed. The monomial f=az^m attains the full-energy bound for every m. **The localized energy permits every finite multiplicity; its exact count is not a collision exclusion.** These statements refine the earlier full-energy count bound by localizing the entire target disk below the paid boundary floor. They are applications of degree and area, not a new integer-valued period. See the [localized-energy proofs](../manuscript/zero_count_heat_transport/sections/02_localized_energy.tex).

## 2. Compact regularization, scalar optimality, and localization bias

Use the radial potential

\[
 v_{\epsilon,p}(r)=
 \begin{cases}(r/\epsilon)^p/p,&r\le\epsilon,\\
 \log(r/\epsilon)+1/p,&r\ge\epsilon.
 \end{cases}
\]

Its distributional measure is

\[
 \mu_{\epsilon,p}(f)=\frac1{2\pi}\Delta v_{\epsilon,p}(|f|)
 =\frac{p}{2\pi\epsilon^p}|f'|^2|f|^{p-2}
                      \mathbf1_{|f|<\epsilon}\,dA. \tag{4}
\]

There is no level-interface measure or point mass at fixed epsilon. Below b the total mass is exactly N, and the measures converge weakly to the multiplicity divisor as epsilon decreases to zero. For psi in C_c^2 and |f−g|<=eta on its support,

\[
 |\langle\mu_{\epsilon,p}(f)-\mu_{\epsilon,p}(g),\psi\rangle|
 \le
 \begin{cases}
 \eta\|\Delta\psi\|_1/(2\pi\epsilon),&p\ge1,\\
 \eta^p\|\Delta\psi\|_1/(2\pi p\epsilon^p),&0<p<1.
 \end{cases} \tag{5}
\]

The p>=1 scalar potential has global Lipschitz constant 1/epsilon. This is optimal among the specified radial profiles that are C^1 for positive r and match log r plus a constant outside epsilon: their radial derivative at epsilon is already 1/epsilon. It is not an optimality assertion about all algorithms or integrated estimates. The root-cover exponent p=2/q puts q=2 at the boundary of the displayed Lipschitz and Holder regimes.

If disjoint root disks have paid unit floors |f(z)|>=c_j|z-a_j|^(m_j), and epsilon lies below the field minimum on their complement, then

\[
 |\langle\mu_{\epsilon,p}(f),\psi\rangle-
                  \sum_jm_j\psi(a_j)|
 \le\operatorname{Lip}(\psi)
             \sum_jm_j(\epsilon/c_j)^{1/m_j}. \tag{6}
\]

For fixed such geometry with maximum multiplicity M, combining (5)–(6) gives upper rates O(eta^(1/(M+1))) for p>=1, and O(eta^(p/(pM+1))) for 0<p<1, with the corresponding balanced epsilon choices. These are fixed-geometry upper bounds, not uniform control through arbitrary collisions. A smooth logarithmic potential has field-error constant 1/(2epsilon), but it loses exact total mass and requires the explicit boundary variation error epsilon² V_boundary/(b²+epsilon²). See [regularization](../manuscript/zero_count_heat_transport/sections/03_regularization.tex).

## 3. Which charges and cover data are transported

For a proper spatial domain, ordinary complex multiplicity is conserved. For real backward heat flow, with regular time caps and full signed wall crossings,

\[
 N_b-N_a+Q_{\rm left}-Q_{\rm right}
             =2\sum_{\rm interior\ events}\lfloor m/2\rfloor. \tag{7}
\]

The complex-time discriminant instead has residue binom(m,2). The manuscript proves the local Hermite splitting, all boundary orientations, preparation by contour moments, and the discriminant/boundary-degree identity. A multiple zero on a time-zero cap requires an explicit endpoint term; replacing it by its ordinary multiplicity cannot detect the difference between it and its simple descendants. See [transport](../manuscript/zero_count_heat_transport/sections/04_zero_transport.tex).

For a disk base, the normalized q-fold cover has

\[
 \chi(X_q)=q-\sum_j(q-\gcd(q,m_j)). \tag{8}
\]

At q=2 this is 2−B_odd, and its excess over a regular fiber with N simple zeros is N−B_odd=2 sum floor(m_j/2). The excess occurs at the normalized singular fiber, not permanently between the two regular complex fibers. The reciprocal differential dz/w has poles at multiple zeros and amplitude-dependent residues, whereas 2 dw remains regular. Pair positions alone do not fix their unnormalized physical periods or energies; the analytic unit and amplitude remain necessary. See [cover geometry](../manuscript/zero_count_heat_transport/sections/05_cover_geometry.tex).

## 4. Elementary full-source theta clock and cumulative cancellation

The manuscript gives a new self-contained proof route for its fixed-rank application rather than importing the stronger earlier differentiated saddle result. It retains the complete canonical source

\[
 \Phi(u)=2\pi^2e^{9u-\pi e^{4u}}\mathfrak b(u),\qquad
 1-3/(2\pi)\le\mathfrak b(u)\le(1-16e^{-3\pi})^{-1}.
\]

For L>=2, put t=(4 pi e^(4L)−9)/(2L), kappa=16 pi e^(4L)−2t, and c_*=(4e)^-1. A Gaussian upper estimate near/right of the saddle, a separate bound on the entire left interval, and an explicit normalization lower bound prove

\[
 \mathbb E_t|U-L|\le
 \frac{e\mathfrak b_+}{\mathfrak b_-}
 \left(\frac1{c_*\sqrt\kappa}
       +\frac{L^2\sqrt\kappa}{2}e^{-c_*\kappa/16}\right)
       =O(\kappa^{-1/2}). \tag{9}
\]

A real C^1 Fourier comparison then identifies exactly the first K positive real roots and proves their simplicity and location error |Lx_j−(j−1/2)pi|=O_K((L sqrt(kappa))^-1). The inverse-square matrix of y_i=Lx_i/pi consequently tends to its finite clock matrix with that same operator error. The physical matrix error after subtracting its order-L² reference is O_K(L/sqrt(kappa)). No RH hypothesis is used for these late roots, and no growing-rank uniformity is claimed.

For a fixed block of m roots, with A_m=sum_(d=1)^(m-1)(m-d)/d², the complete heat identity and location theorem yield

\[
 \log\Delta(T)=-m(m-1)\log L(T)+C_m+o(1),
\]
\[
 \int_{T_0}^T P_{\rm pair}\,dt
       \sim\frac{8A_m}{\pi^2}TL(T)^2,
\]
\[
 \int_{T_0}^T B_{\rm ext}\,dt
       =-\int_{T_0}^T P_{\rm pair}\,dt
                    -m(m-1)\log L(T)+O(1). \tag{10}
\]

**The cumulative cancellation theorem does not differentiate an uncontrolled asymptotic remainder.** It integrates the exact forced discriminant identity and uses the location asymptotic only at the endpoints. It proves E=−log Delta tends to positive infinity and that the integrated exterior-to-pair ratio tends to −1. It does not prove eventual pointwise positivity of E' from these data. The [theta proof](../manuscript/zero_count_heat_transport/sections/08_theta_concentration.tex) and [pair dynamics](../manuscript/zero_count_heat_transport/sections/06_pair_matrices.tex) specify every normalization and force term.

## 5. Control screen, numerical role, and open tasks

The generic identities admit exact quadratic and cubic heat events and the applicable broader collision controls. No control is rejected by the localized count alone. The complete canonical-source theorem is not assigned to a source that changes its premises: Euler-factor controls alter the source, weighted-square and finite-prime controls lack full reflection, and reflected/positive-primitive controls lack the unchanged integer-square expansion. Qualitative late regularity nevertheless does not exclude a past event. This is a scoped limitation on the proposed inference, not a universal obstruction to theta estimates.

Only the supporting appendix imports [RHE Note 04's existing finite-disk certificate](../09_reciprocal_hodge_energy/notes/04_ACTUAL_REGULAR_THETA_FIBER_COMPARISON_20261022.md). It has not been rerun. Its localized-energy illustration is deduced from its recorded count and boundary floor; none of the analytic proofs depends on that appendix.

The manuscript/preparation tasks ZHM-01–08 are complete in their declared scope. The open tasks ZHM-09–11 are a complete centered exterior-residual estimate, improved integrated stability under additional analytic information, and a stronger signed estimate for a fully specified physical boundary. The missing source-specific estimate has not been removed by introducing another count or cover. The maintained program remains in the base of investigations-4, while the original conversation remains in home 11's unique archive 0001.
