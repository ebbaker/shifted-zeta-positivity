# Sharp C² weighted-divisor stability on controlled disks

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**, verified from this turn's metadata.

**Status: proved in-note and integrated into the maintained manuscript; same-assistant self-review only.** This completes the fixed-geometry task specified by [Continuation 08](08_CONTINUATION_SHARP_DIVISOR_STABILITY_AND_GROWING_CLOCK_WINDOWS_20261022.md), including its candidates C1 and C2. It is a quantitative analytic milestone, not an RH-equivalent criterion. The general weak-information and merging-cluster questions are not closed.

The [result index](../../../result-summaries/README.md), [heat-geometry cluster](../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../avoid/README.md), and patterns [01](../../../avoid/01_restating_the_target.md), [12](../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [16](../../../avoid/16_unchecked_imports_and_novelty_claims.md), and [20](../../../avoid/20_volume_without_a_gain.md) govern this continuation. The gain is the exponent and explicit constants below. [Review 02](../reviews/02_DIVISOR_STABILITY_AND_GROWING_WINDOWS_SELF_REVIEW_20261022.md) audits the proofs and scope; the separate [clock-window note](10_GROWING_CLOCK_WINDOWS_20261022.md) extracts the spatial corollary.

## 1. Exact harmonic reproduction, including the cutoff contract

Let D=D(a,R), R>0, with f holomorphic on a neighborhood of its closure, and exactly one zero there, at a of multiplicity m≥1. Set b=min∂D|f|>0. For p>0 and 0<ε<b, use the manuscript's compact measure

\[
 d\mu_{\varepsilon,p}(f)=\frac{p}{2\pi\varepsilon^p}
 |f'|^2|f|^{p-2}\mathbf1_{|f|<\varepsilon}\,dA.
\]

Its mass is m. Its support is compactly contained in D. For any real harmonic h on a neighborhood of the closed disk,

\[
 \boxed{\int_Dh\,d\mu_{\varepsilon,p}(f)=m h(a).} \tag{1}
\]

**Proof.** Choose a holomorphic q near the closed disk with h=Re q. For |w|<b define

\[
 T_q(w)=\frac1{2\pi i}\oint_{\partial D}
           q(z)\frac{f'(z)}{f(z)-w}\,dz.
\]

The denominator stays nonzero on the contour, so the trace is holomorphic in w. The residue theorem identifies it with the sum of q over all preimages, with multiplicities, and T_q(0)=m q(a). The weighted area formula gives

\[
 \int_Dq\,d\mu_{\varepsilon,p}(f)
 =\frac{p}{2\pi\varepsilon^p}\int_{|w|<\varepsilon}
                    |w|^{p-2}T_q(w)\,dA_w=T_q(0).
\]

The last step uses the angular mean of a holomorphic function and the radial integral p ε⁻ᵖ∫₀ᵋrᵖ⁻¹dr=1. Boundedness of q and the exact mass justify absolute integrability. No root labels, inverse-branch continuation or simplicity assumption enters. Taking real parts proves (1).

The area formula ignores the finite critical-value set, which has planar measure zero. There is no extra measure on a nonregular cutoff level: the compact potential and its first derivative match there, and its composition with f is C¹,¹ near |f|=ε. At an m-fold zero the small-circle flux is O(r^(mp)), so it has no atom for fixed ε. These are precisely the manuscript's already proved distributional conventions. The same trace argument on a disk with several zeros reproduces the sum of their harmonic values. Thus, for f=z²−1 on |z|<2, ε=1 is an allowed critical cutoff and gives h(1)+h(−1). In particular the z² trace is 2(1+w), whose radial average is 2. No regular-value hypothesis is needed.

## 2. The improved bias and the regularized-field comparison

Assume the acquired floor |f(z)|≥c|z−a|ᵐ throughout the closed disk, with c>0. For every preimage of w,
|z−a|≤(|w|/c)^(1/m). Applying the weighted area formula to |z−a|² therefore gives

\[
 \int_D|z-a|^2\,d\mu_{\varepsilon,p}(f)
 \le m\frac{p}{p+2/m}(\varepsilon/c)^{2/m}. \tag{2}
\]

For a real C² test ψ on a neighborhood of the closed disk, subtract its real affine Taylor polynomial at a. Equation (1) cancels that polynomial exactly; the Hessian remainder is bounded by half its operator norm times |z−a|². Hence

\[
 \boxed{\left|\int_D\psi\,d\mu_{\varepsilon,p}(f)-m\psi(a)\right|
 \le\frac m2\|D^2\psi\|_{\infty,D}
       \frac{p}{p+2/m}(\varepsilon/c)^{2/m}.} \tag{3}
\]

This proves C1 with the sharper coefficient p/(p+2/m). Equality holds for f=c(z−a)ᵐ, c>0, and ψ=|z−a|², so the coefficient is attained in this class.

For finitely many disjoint root disks, add (3) with their own m_j,c_j. To compare with the divisor in an ambient domain Ω, retain the positive floor of |f| on the compact complement of the disk interiors and take ε below it. The measure then has no omitted mass. For ψ∈C_c²(Ω), a field error η known on supp ψ costs η‖Δψ‖₁/(2πε) when p≥1. The resulting estimate against the exact divisor of f has form

\[
 A\eta/\varepsilon+B\varepsilon^{2/M},\qquad M=\max_jm_j.
\]

With fixed geometry, fixed p≥1, and small η, ε=η^(M/(M+2)) gives **O(η^(2/(M+2)))**. For 0<p<1, the analogous choice ε=η^(pM/(pM+2)) gives O(η^(2p/(pM+2))). The zero-free case has zero bias for small ε. These are bounds on the regularized approximate field versus the exact divisor, not optimal rates for direct divisor perturbation. The earlier Lipschitz-based upper rates remain true but are weaker for these C² tests.

## 3. Direct theorem with complete cluster data

Retain D,f,m,c,b, and let g be holomorphic near the closed disk, with

\[
 \|f-g\|_{\infty,\overline D}\le\eta<b.
\]

Then g has exactly m interior zeros ζ_ν, with multiplicities, and

\[
 \boxed{\left|\sum_{\nu=1}^m\psi(\zeta_\nu)-m\psi(a)\right|
 \le |\nabla\psi(a)|R\log\frac b{b-\eta}
 +\frac m2\|D^2\psi\|_{\infty,D}(\eta/c)^{2/m}.} \tag{4}
\]

**Proof.** The classical Rouché theorem preserves the complete count. At every zero of g, c|ζ−a|ᵐ≤|f(ζ)|≤η, which gives the stated cluster radius. On ∂D, write g/f=1+u with |u|≤η/b<1. Compactness gives a thin collar where f≠0 and |u|<1; the principal series defines a single-valued holomorphic λ=log(1+u) there. Its boundary values obey
|λ|≤−log(1−η/b). No logarithm throughout D is asserted.

The residue theorem, followed by integration by parts along the circle, gives

\[
 S:=\sum_\nu(\zeta_\nu-a)
 =\frac1{2\pi i}\oint_{\partial D}(z-a)(g'/g-f'/f)\,dz
 =-\frac1{2\pi i}\oint_{\partial D}\lambda\,dz.
\]

The boundary length is 2πR, so |S|≤R log[b/(b−η)]. Sum the real Taylor formula at a: its linear part is ∇ψ(a)·S, rather than a sum of absolute displacements. The quadratic remainders have sum at most (m/2)‖D²ψ‖∞(η/c)^(2/m). This proves (4). When η=0 the statement is immediate. No floor for the analytic unit of g and no separation among its descendants is used.

For disjoint disks D_j, add the local right sides, retaining every R_j,b_j,c_j,m_j,η_j. This compares complete divisors in their union. A comparison on a larger Ω also requires exclusion of new g zeros on its complement, for example by a field error smaller than the corresponding |f| floor. Merely adding the local estimates does not provide that exclusion.

## 4. Exponent, norm and exact controls

Fix the geometry and 0<θ<1; restrict η≤θb. Since log[b/(b−η)]≤η/((1−θ)b), equation (4) gives **O(η^min(1,2/m))** uniformly for tests in a bounded C² norm ball on the disk (value, gradient and real Hessian norms). This is a fixed-reference estimate at a multiplicity-m zero, not a uniform claim across all moving cluster geometries.

| Control | Exact check and implication |
| --- | --- |
| m≥2; f=zᵐ, g=zᵐ−η on the unit disk; ψ=|z|² | c=b=1, error exactly η, centroid zero, and discrepancy mη^(2/m). The exponent cannot be increased over this declared class. |
| m=1; f=z, g=z−η; ψ=Re z | Discrepancy exactly η. This calibrates the exponent one. |
| Translated cluster f=zᵐ, g=(z−d)ᵐ, d>0 small | The exact unit-disk error is (1+d)ᵐ−1: the triangle upper is attained at z=−1. The linear test Re z has discrepancy md and zero Hessian. A centroid allowance is necessary. |
| Complex η replaced by τ | For g=zᵐ−τ, the radius is |τ|^(1/m), the quadratic discrepancy is m|τ|^(2/m), and for m≥2 the centroid remains zero. No reality condition is used. |
| Nonconstant analytic unit | For f=e^(λz)zᵐ and g=e^(λz)(zᵐ−τ) on |z|<R, c=e^(−|λ|R), b=Rᵐe^(−|λ|R), and η=e^(|λ|R)|τ|. If |τ|<Rᵐe^(−2|λ|R), (4) applies and the same explicit roots verify its allowances. No unit of g is acquired. |
| Common amplitude A≠0 | c,b,η multiply by |A|. Both ratios in (4) are unchanged; the divisor itself is unchanged. |
| Boundary approach | For zᵐ−τ on the unit disk, |τ|=1 puts roots on the boundary. The strict margin η<b is a real requirement for count preservation. The divergent logarithmic allowance as η approaches b is not claimed sharp. |
| Merging reference clusters | For f_d=z²−d², the disk centered at d of radius d/2 has m=1, c=3d/2 and b=3d²/4. Those constants vanish as d→0. A uniform merging theorem requires a different cluster contract. |
| Critical cutoff | f=z²−1, disk radius 2, ε=1 checks the trace identity at a critical level, as in §1. |

The polynomial tests can be extended smoothly with compact support in a fixed larger disk, equal to the displayed tests near the closed unit disk, independently of η. Thus the sharp exponent remains a statement in a fixed compact C²-test class. It is not minimax optimality for every zero-finding algorithm, and (4)'s constants are not asserted optimal.

The generic theorem passes every applicable [collision control](../../../result-summaries/12_collision_controls_and_screening.md): it allows arbitrary multiplicity. It supplies neither a sign nor an exclusion. For the separate canonical clock claim, Euler-factor controls change the displayed source; weighted-square and finite-prime controls fail full reflection; reflected/positive-primitive controls lack the unchanged square expansion; normalized endpoint controls fail ordinary Dirichlet arithmetic. These premise differences are not favorable theta estimates.

## 5. Matched-information comparison with primary literature

The following is a bounded source comparison, not a comprehensive originality search. The proof above uses only classical area, residue, Rouché and Taylor arguments and is self-contained.

| Primary source and checked location | Contract and relation to this result |
| --- | --- |
| [Simon, Introduction to Geometric Measure Theory](https://web.stanford.edu/class/math285/ts-gmt.pdf), Chapter 2 §3, (3.4)–(3.5), printed pp. 53–54 | The weighted area formula counts inverse images with their weights. After constant valence is established, it supplies the trace integral in §1. The localized energy identity is a specialization of this classical mechanism. |
| [Beauzamy, 1999](https://doi.org/10.4153/CMB-1999-001-6), Theorems 1 and 4, especially printed p. 7; §3 | Polynomial coefficient perturbation in Bombieri norm gives a nearby-root estimate with multiplicity-sensitive exponent 1/m. On |z|≤R, coefficient error ε_B gives field error at most ε_B(1+R²)^(n/2), by the paper's evaluation inequality. A complete boundary/unit contract still must be supplied to use (4). Nearby-root displacement and a smooth sum over the entire cluster are different outputs. |
| [Barlet, Fonctions de type trace, 1983](https://aif.centre-mersenne.org/item/10.5802/aif.915.pdf), printed pp. 43–44 | The opening problem is a smooth function summed over fibers of a proper finite holomorphic map. It explicitly notes continuity without general differentiability and gives fractional-power trace behavior. The trace viewpoint and branching singularities are classical; (4) is an explicit finite C² estimate with disk boundary conditioning. No theorem from the later sheaf-theoretic argument is imported. |
| [Parusiński–Rainer, On the continuity of the solution map for polynomials](https://www.mat.univie.ac.at/~armin/publ/continuity_gen.pdf), Theorem 1.1 and §11.1 | Cᵈ convergence of degree-d coefficient curves yields Sobolev convergence of unordered roots; §11.1 identifies root multisets with probability measures and the normalized matching metric with W₂. Those are parameter-curve and transport metrics. For zᵐ−η, the root probability measure has W₂ distance η^(1/m) to δ₀, while its quadratic-test discrepancy is η^(2/m). This elementary comparison explains the differing exponents without claiming a better W₂ rate. |
| [Phong–Sturm, 2000](https://www.maths.tcd.ie/EMIS/journals/Annals/152_1/phong.pdf), §2, Theorem 1, printed pp. 281–282 | Rational-integral estimates retain degree, root-location and exponent conditions and use a hierarchy of cluster scales. This is pertinent to a future uniform merging-cluster or singular-energy task. None of its stronger uniformity is imported here. |

Demailly's divisor-current comparison remains background from Note 08; attempts to retrieve the author-hosted text in this round timed out, so no new statement is attributed to it. All displayed results are proved above. **The result is characterized as a useful explicit specialization; no novelty claim is made.**

## 6. Completed scope and next step

ZHM-10's specified fixed-disk C² target is complete at this internal checkpoint: harmonic reproduction, the attained radial bias coefficient, the direct estimate, local-to-finite-cluster addition, conditioning, and sharp exponent controls. The manuscript's weaker support-only field theorem is retained; (4) does not improve it under identical information.

The immediate bounded spatial extraction is [Note 10](10_GROWING_CLOCK_WINDOWS_20261022.md). ZHM-09's complete centered exterior residual and ZHM-11's all-face signed physical-boundary estimate remain open. A broader stability continuation should first declare a weaker acquisition contract or quantitative cluster geometry and a norm. Specialist review of this compact proof core is recommended before broader expansion; none has been requested or obtained. No numerical sweep, new RH claim, manuscript snapshot, commit, or tag is part of this round.
