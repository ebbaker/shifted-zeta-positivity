# Pair-matrix spectrum, heat evolution and endpoint multiplicity

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Separate same-model review located the inherited equations, checked the Hermite normalization and proposed the matching-spectrum estimate below; no specialist review or priority claim.

**Status: proved finite spectral implication from established heat-root dynamics; no new theta spectral upper bound.** The author recalled the earlier pair-distance eigenvalue program and asked that it be connected to RH implying almost-all simplicity. This note makes that connection explicit. It complements the earlier-negative-time count route in [Note 05](05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md), rather than assuming that a complex-root pair matrix remains positive.

Read the [result index](../../../../result-summaries/README.md), [local heat geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../avoid/README.md), [target classification](../../../../avoid/01_restating_the_target.md), [control register](../../../../result-summaries/12_collision_controls_and_screening.md), and [scoped-obstruction rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md). The prior framework is [LHCT Note 06][pair], also written in [the maintained pair-matrix section][section]. The full adjacent-gap bound is [BW10 Note 19][motion], RM5–RM13. These are inherited results, not discoveries of this continuation.

## 1. The spectral object and the Vandermonde

For N simple real roots x_i, put

\[
 \Delta=\prod_{i<j}(x_j-x_i)^2,\qquad
 W_{ij}=(x_i-x_j)^{-2},\qquad
 L_{ij}=-W_{ij}\ (i\ne j),\quad L_{ii}=\sum_{j\ne i}W_{ij}.
 \tag{1}
\]

Then L is positive semidefinite, has one constant zero mode, and

\[
 L=\tfrac12\nabla^2(-\log\Delta),\qquad
 v^TLv=\sum_{i<j}W_{ij}(v_i-v_j)^2.
 \tag{2}
\]

This is the N-mode spectral object associated with the logarithmic Vandermonde. The discriminant Delta itself is a scalar. The raw matrix of squared distances D_ij=(x_i−x_j)² is different: D=x²1^T+1(x²)^T−2xx^T has rank at most three. Its normalized spectral distribution therefore cannot count a positive fraction of collision modes. We retain the inverse-square Laplacian already used in the earlier program.

## 2. Exact evolution and what must be estimated

For a finite simple population write H=U product_i(z−x_i), and b_i=U_z/U(t,x_i). The inherited complete equations are

\[
 x_i'=2\sum_{j\ne i}(x_i-x_j)^{-1}+2b_i,
\]
\[
 W_{ij}'=-2W_{ij}\left[
 \frac4{(x_i-x_j)^2}
 -2\sum_{k\ne i,j}\frac1{(x_i-x_k)(x_j-x_k)}
 +2\frac{b_i-b_j}{x_i-x_j}\right].
 \tag{3}
\]

For a simple eigenvalue lambda_alpha with unit real eigenvector v_alpha,

\[
 \lambda_\alpha'
 =v_\alpha^TL'v_\alpha
 =\sum_{i<j}W_{ij}'(v_{\alpha,i}-v_{\alpha,j})^2.
 \tag{4}
\]

At an eigenvalue degeneracy use the compressed perturbation on its eigenspace, or a differentiable trace functional. The unit b includes every exterior root and the nonzero factor. Its contribution cannot be omitted. No general sign for each eigenvalue derivative follows from L>=0; the prior note exhibits the actual theta exterior force reversing a naive pair-energy conclusion. A time-dependent unfolding x↦nu(t)x also contributes the derivative of nu(t)^−2 to the normalized matrix.

Thus the spectral proposal requires an estimate for a distribution of eigenvalues under the **complete** evolution, not merely the known equation (4). Deterministic repulsion alone is not a theorem of sine-kernel universality.

## 3. Local multiplicities create a specific spectrum

At a real endpoint zero of multiplicity m, the local heat law gives

\[
 x_j(t)=x_*+\sqrt{2t}\,h_j+O(t),\qquad t\downarrow0,
 \tag{5}
\]

where h_j are the zeros of the monic probabilists' Hermite polynomial He_m. Hence the internal block satisfies

\[
 tL(x(t))\longrightarrow\tfrac12L(h),\qquad
 \operatorname{spec}(\tfrac12L(h))
   =\{0,\tfrac14,\tfrac24,\ldots,\tfrac{m-1}{4}\}.
 \tag{6}
\]

For a short proof of the spectrum, the Hermite differential equation implies sum_{j!=i}(h_i−h_j)^−1=h_i/2. Acting with L(h) on evaluations of a degree-k polynomial gives k/2 times its leading degree-k term, plus lower-degree terms: Taylor-expand p(h_j) about h_i in sum_j[p(h_i)−p(h_j)]/(h_i−h_j)². Evaluation of degrees 0,...,m−1 is an invertible Vandermonde basis. The resulting triangular matrix has diagonal 0,1/2,...,(m−1)/2, proving (6).

For a fixed complete finite real endpoint population, inter-cluster entries multiplied by t tend to zero. Thus, with D_0=sum_endpoint(m−1),

\[
 D_0=\lim_{t\downarrow0}\#\{\lambda(tL)>c\},\qquad 0<c<1/4.
 \tag{7}
\]

There is also the bounded continuous-filter identity

\[
 D_0=\lim_{t\downarrow0}\operatorname{Tr}\varphi(tL),
 \qquad\varphi(s)=\min(1,4s),\quad s\ge0.
 \tag{8}
\]

These are finite-population identities. On their own they are reformulations of multiplicity and do not justify exchanging height and time limits. The next estimate avoids that particular exchange.

## 4. A uniform positive-time spectral bound for the canonical field under RH

Assume RH. The canonical theta field has all real simple roots for t>0. Its complete paired product, with the summation and convergence specified in [BW10 Note 19][motion], gives for any globally adjacent roots a(t)<b(t), with g=b−a,

\[
 (g^2)'=8-4g^2\sum_{r\ne a,b}\frac1{(a-r)(b-r)}\le8.
 \tag{9}
\]

Every summand is positive by global adjacency. The sum is absolutely convergent; it retains the exterior roots. If the pair descends from one multiple endpoint, g(0)=0, and therefore

\[
 g(t)^2\le8t\quad(t>0).
 \tag{10}
\]

The cited source gives a strict improvement for positive roots using their mirrors, and explicitly extends this bound to adjacent subpairs of higher-multiplicity events. Only the weaker (10) is needed here. It is not obtained by setting the finite exterior unit b to zero.

Take a finite set of endpoint roots including every label at each selected multiple site; follow all its N descendants to positive time. Build L_N(t) using just these selected roots, while deriving (9) from the full root system. From each endpoint multiplicity m select floor(m/2) disjoint adjacent descendant pairs. They remain globally adjacent at positive time. Dropping every other edge of L_N leaves a matching Laplacian L_match with

\[
 L_N\succeq L_{\rm match},\qquad
 \lambda_{\rm nonzero}(L_{\rm match})=2/g^2\ge1/(4t).
\]

The minimum–maximum principle gives, for **every** positive time in the tracked interval,

\[
 \#\{\lambda(L_N(t))\ge1/(4t)\}
 \ge\sum_{\text{endpoint sites}}\lfloor m/2\rfloor.
 \tag{11}
\]

Since the nonsimple endpoint mass M_0=sum_{m>=2}m is at most three times the sum on the right,

\[
 \boxed{\frac{M_0}{N}
 \le\frac3N\#\{\lambda(L_N(t))\ge1/(4t)\}
 \le\frac3N\operatorname{Tr}\varphi(tL_N(t)).}
 \tag{12}
\]

Likewise D_0 is at most twice the spectral count. The matching proof gives a uniform implication without choosing t small enough to resolve each unknown endpoint cluster. It counts multiplicities; it does not assume they are doubles. Extra small gaps between distinct endpoint roots may also produce large eigenvalues, which only weakens this upper bound for M_0.

This identifies a specific sufficient research target: for a source-prescribed time t=t_T>0 and the descendants of a population covering all but o(N(T)) endpoint labels, prove

\[
 \frac1N\#\{\lambda(L_N(t_T))\ge1/(4t_T)\}\longrightarrow0,
 \quad\text{or the stronger bounded-filter upper bound in (12).}
 \tag{13}
\]

Then RH implies almost-all simplicity. Coverage error is added at the root-count stage. An N-mode matrix built from a cut that splits a multiple endpoint cluster requires a separate error for those labels.

A smooth bounded version is useful for differentiating under heat evolution:

\[
 F_t=4tL_N(t)(I+4tL_N(t))^{-1},\qquad
 \boxed{M_0/N\le6\operatorname{Tr}F_t/N.}
 \tag{14}
\]

Each eigenvalue above the threshold contributes at least 1/2 to F_t, proving (14). Thus a source upper bound Tr F_(t_T)=o(N) is another precise sufficient target. This filter saturates at one instead of assigning arbitrarily large weight to an exceptionally small gap. It is comparable to the continuous filter in (12), up to constants.

## 5. Scale, controls and the independent research task

Let nu_T be the local mean density and set L_tilde=L_N/nu_T². The threshold in (13) is 1/(4t_T nu_T²). One possible sufficient route is t_T nu_T²→0 together with uniform tightness of the empirical spectral distributions of L_tilde along these times. That tightness is a missing theorem: it must not be inferred from real-rootedness or generic heat regularity. An inverse-square trace bound would be stronger than a bounded spectral-tail estimate and may demand unnecessary control of rare tiny gaps.

The existing large-heat fixed-rank clock theorem in [LHCT Note 06][pair] does not cover this joint microscopic-time/growing-height regime. Nor does the positive-time high-height approximation at heights exp(C/t) automatically help: its t times mean-density-squared scale is not small there. A negative smoothing step could still be useful if it makes a new complete estimate easier, but complex-root inverse-square matrices are not Hermitian positive semidefinite. The positivity in (11)–(12) belongs to the real positive-time population; any bridge from the negative contour must be proved.

For H=z²−2t, tL has eigenvalues 0,1/4, exactly detecting the double. For H=z³−6tz it has 0,1/4,1/2. The equality model for the general local spectrum is the Hermite heat polynomial. These controls pass the spectral identities and retain their endpoint multiplicities, so a claimed universally vanishing spectral tail would fail. The stationary sine heat field has fixed simple roots and tL→0 for every fixed finite population, consistently with zero endpoint defect.

The broader controls obey the equations when their relevant real-root hypotheses hold. As in BW10 Note 19, all-real global dynamics must not be assigned to weighted-square or reflected controls without proof. RH-conditional close endpoint controls retain their large collision modes; their failure of ordinary Dirichlet arithmetic is recorded in the control register, not used as a substitute for an estimate.

Equations (7)–(8) are exact multiplicity reformulations; (12) is a finite sufficient transfer with a uniform threshold. Neither is an independent theta spectral bound or a new RH-conditional simplicity proportion. The concrete next analytical task is to estimate the upper spectral tail or bounded filter in (13), keeping the complete force in (3), and to compare the information needed with the projected near-zero pair bound of Note 05. Full PCC is not a prerequisite for either consumer.

[pair]: ../../11_late_heat_caps_and_charge_transport/notes/06_PAIR_DISTANCE_MATRICES_AND_FORCED_HEAT_DISSIPATION_20261022.md
[section]: ../../manuscript/zero_count_heat_transport/sections/06_pair_matrices.tex
[motion]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
