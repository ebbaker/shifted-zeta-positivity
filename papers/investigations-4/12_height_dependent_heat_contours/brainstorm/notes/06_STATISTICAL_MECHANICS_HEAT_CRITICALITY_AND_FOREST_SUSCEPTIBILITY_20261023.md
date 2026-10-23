# Brainstorm: statistical mechanics, heat criticality and forest susceptibility

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **xhigh**.

**Status: brainstorm and continuation brief.** The finite identities below are elementary consequences of the existing forest formula; the physical interpretation and proposed research questions do not establish a new theta estimate, thermodynamic phase transition, RH, or a simplicity theorem. This note opens no new investigation or task register.

## Purpose and the author's intuition

The author approaches the heat-flow picture through statistical mechanics: zeros leaving the real axis resemble bubbles forming as a system crosses a critical point; inverse-gap matrices resemble quantities built from pair correlations; and the divergence of collision curvature suggests critical scaling. The question is whether this vocabulary can guide a useful systematic investigation, beyond providing a different description of known identities.

A future chat can start from this note alone. Its first objective should be to identify one observable and one complete-source inequality that the analogy makes easier to estimate, or to explain precisely why the proposed observable adds no information. Begin analytically; computations should answer a stated diagnostic question.

The shorter originating discussion is [HDC Note 17][dictionary]. The originating chat remains uniquely registered as [HDC history 0003][chat]; this brainstorm note does not relocate or copy that archive. A new chat should retain its own identity and follow the repository's [history workflow][history].

## 1. Separate the three possible transitions

For the canonical field, with normalization H_t=-H_zz,

\[
 H(t,\cdot)\text{ has only real zeros}\quad\Longleftrightarrow\quad t\ge\Lambda.
\]

Rodgers and Tao proved Lambda>=0. Thus every negative time already has some nonreal zeros, unconditionally. RH would locate the boundary at Lambda=0. Reality at zero still allows multiple real zeros, so simplicity is an additional endpoint question. It is the conjugate nonreal pairs, or the events producing them when time runs backward, that can play the role of bubbles; zeros themselves remain present on both sides.

The local double model is

\[
 H(t,z)=(z-x_*)^2-2(t-t_*).
\]

Above t_* its two roots are real, at t_* they collide, and below t_* they form a nonreal conjugate pair. The separation has square-root scaling. This is a local analytic bifurcation with a precise normal form.

A global all-real threshold need not be attained by a collision at a finite height. Conditional on all zeros at zero being real and simple, every fixed compact region with a zero-free enclosing boundary has a sufficiently small negative-time interval on which its roots remain real and simple. Nonreal zeros at negative times tending to zero must then escape every fixed compact region. This suggests a **criticality-at-infinity picture**, conditional on those endpoint assumptions.

A thermodynamic phase transition is a third notion: a singularity of a specified limiting free energy or related observable. A local root collision, the global threshold Lambda, and a thermodynamic singularity must be related by a theorem before being identified. Heat time is a deformation parameter; a physical temperature interpretation requires a specified model.

Primary orientation: [Rodgers-Tao][rt] and [Newman-Wu, especially Sections 2.4-2.6][nw]. Newman-Wu Section 2.5 explicitly connects the Fourier-transform question with Lee-Yang partition functions and Euclidean field theory.

## 2. An exact statistical-mechanical dictionary already available

Fix distinct real root positions x_1,...,x_N and write

\[
 L=\sum_{i<j}\frac{(e_i-e_j)(e_i-e_j)^T}{(x_i-x_j)^2},
 \qquad \Delta=\prod_{i<j}(x_i-x_j)^2.
\]

For a>0 the existing forest identity gives

\[
 Z(a)=\det(I+aL)
 =\sum_F a^{k(F)}m(F)\prod_{\{i,j\}\in E(F)}(x_i-x_j)^{-2},
\]

where k(F)=|E(F)|, the sum includes all spanning labeled forests and isolated vertices, and m(F)=product_C |C|. The latter factor counts choices of one distinguished root in each tree component. This is a positive partition function on rooted forests with edge activity a and fixed inverse-square gap weights. It is an instance of the classical weighted [matrix-forest theorem][forest], rather than a new theta-specific ensemble.

The manuscript uses D=Delta Z and G=a partial_a D. Since Delta is independent of a, multiplying by Delta changes neither the normalized forest probabilities nor the logarithmic a derivatives. It clears the determinant's gap denominators, allowing the result to be written in the prepared polynomial's coefficients. See [HDC Note 11][coefficient] for the coefficient error theorem and its denominator conditions.

Set theta=log a, and let K be the forest edge count. Normalizing the finite forest weights gives

\[
 q_a=\partial_\theta\log Z=\mathbb E_a[K],
 \qquad
 \chi_a:=\partial_\theta^2\log Z
       =\operatorname{Var}_a(K).
\]

With lambda_j the eigenvalues of L,

\[
 q_a=\sum_j\frac{a\lambda_j}{1+a\lambda_j},
 \qquad
 \boxed{\chi_a=\sum_j\frac{a\lambda_j}{(1+a\lambda_j)^2}.}
\]

This identifies the bump suggested by the author as an exact fluctuation response to log activity. It measures modes near a lambda=1; q measures a smooth cumulative count of modes at or above that scale. A bump alone suppresses arbitrarily large collision modes and does not retain the current uniform multiplicity comparison without further spectral information.

There is also an exact auxiliary occupancy description:

\[
 \mathbb E_a[s^K]=\frac{Z(as)}{Z(a)}
 =\prod_j\left((1-p_j)+p_js\right),
 \qquad p_j=\frac{a\lambda_j}{1+a\lambda_j}.
\]

Thus K has the distribution of a sum of independent Bernoulli variables with these parameters. This concerns spectral occupancies and the total edge count; individual forest edges need not be independent. The logistic occupancy factors offer a direct bridge to familiar statistical-mechanical language.

## 3. Two checks that should guide the investigation

**A frozen forest ensemble has no positive-activity singularity at finite N.** Z(a)>0 and is analytic for a>0. Moreover, each susceptibility summand is at most 1/4, and L has a constant zero mode, so

\[
 0\le\frac{\chi_a}{N}\le\frac{N-1}{4N}<\frac14.
\]

This bound is uniform over positive a and distinct real configurations. Consequently the susceptibility per root for this particular frozen-configuration, log-activity response cannot diverge merely by taking a growing-system limit. It does not exclude a singularity in another observable, another parameterization, or a limit involving moving or colliding roots. It is a useful constraint on what an eventual critical-point claim could mean.

**Varying heat time also moves the roots.** For the manuscript observable let A(t)=4tL(x(t)) and Q=(I+A)^(-1). Direct differentiation and cyclicity of trace give

\[
 q'(t)=\operatorname{Tr}\left((4L+4tL')Q^2\right),
\]

hence

\[
 \boxed{tq'(t)=\chi_{4t}+4t^2\operatorname{Tr}(L'Q^2).}
\]

The first term is the positive frozen-configuration susceptibility. The second records root motion and has no sign supplied by the forest identity. For a selected finite population its computation must retain the complete exterior force in the root dynamics. This decomposition is finite calculus, not a complete-theta bound or a monotonicity theorem.

Also distinguish Z(a), an ensemble constructed from a root configuration, from the original theta field H(t,z). An exact statistical interpretation of Z does not construct H as a Lee-Yang spin partition function.

## 4. Pair correlations, stiffness and the singular scale

The logarithmic Vandermonde gives an exact stiffness matrix:

\[
 L=-\tfrac12\operatorname{Hess}_x\log\Delta,
 \qquad
 v^TLv=\sum_{i<j}\frac{(v_i-v_j)^2}{(x_i-x_j)^2},
 \qquad
 \operatorname{Tr}L=2\sum_{i<j}(x_i-x_j)^{-2}.
\]

The trace is an inverse-square moment of pair separations. A pair-correlation measure records separation statistics, while L also retains the labels and collective modes. A divergence of L can result from a single closing gap; it is not by itself a divergence of a bulk correlation length.

For the double model centered at t=0, the squared gap is 8t and the nonzero eigenvalue is 1/(4t). The raw curvature diverges, while q_(4t)=1/2 remains finite. For a multiplicity-m Hermite birth, the scaled spectrum 4tL is 0,1,...,m-1 and q tends to m-H_m. The scaling extracts the collision signature rather than removing the collision.

For comparisons at growing height T, declare a local density nu_T and the dimensionless scale s_T=4t_T nu_T^2. A source-prescribed clock and endpoint coverage are necessary. Choosing t_T after resolving the unknown endpoint gaps would restate the target. Existing late-time estimates can place q in a saturated regime even for simple zeros; consult [HDC Note 10][spectrum] before treating a large q as a unique criticality signal.

## 5. Existing project work to read before reopening

| Route | Existing material and its role |
| --- | --- |
| Deterministic logarithmic gas and pair statistics | [LHCT Note 07, Section 4][relaxation] gives finite heat-polynomial energy relaxation, Hermite equilibrium and the exterior-force term. It distinguishes this deterministic evolution from stochastic Dyson/GUE statistics. |
| Lee-Yang source preparation | [Investigation 2/13][lee] preserves the earlier stability/Jensen/Lee-Yang preparation program; it is deferred without a qualifying source preparation. |
| Spin and quartic realizations | [Investigation 3/05][stable] and [result cluster 17][stable-summary] record constructive attempts and scoped obstructions. Specified independent-spin and quartic classes are excluded; general statistical-mechanical realizations are not universally excluded. |
| Forest coefficients and collision conditioning | [HDC Note 11][coefficient] and [the current manuscript][manuscript] give the exact coefficient route, stable double neighborhoods, higher-collision limitations and heat-scale error costs. |
| Bubbles crossing a finite observation window | [Brainstorm Note 04][flux] and [the open-boundary continuation][flux-next] separate earlier nonreal mass, one-sided inflow and real births. Those finite identities do not supply the missing negative-time theta resource bounds. |

The [result index][results] and [patterns to avoid][avoid] govern the interpretation. In particular, read [target reformulations][a01], [shape-only controls][a02], [normalization slips][a08], [numerics before structure][a10], [coupled estimates][a12], and [scoped exclusions][a07]. This note is an explanatory dictionary and a set of questions, not a new sufficient criterion counted as research progress.

## 6. A bounded plan for a future chat

1. **Choose one meaning of criticality.** Specify whether the observable concerns loss of reality, endpoint multiplicity, close-pair density, or a limiting free-energy response. State the conditional assumptions. Do not combine these into one unnamed transition.
2. **Audit the two derivatives.** Start from the displayed frozen-response and complete heat-response identities. Determine whether the root-motion term admits a useful cancellation, comparison with a matched reference, or source representation. A formal energy identity alone is not the desired estimate.
3. **Choose one controlled asymptotic regime.** Fix the finite population, its completeness rule, a source-prescribed height/time clock and the normalization. If a thermodynamic limit is proposed, define its free energy and order of limits. Check compatibility with the uniform bound on chi_a/N.
4. **Screen the proposed diagnostic on the controls below.** Decide what it detects and what it cannot distinguish before substantial numerics. A method based on a local profile shared by collision controls must identify the extra theta-specific input.
5. **Write one useful analytical deliverable.** Aim for a complete-source inequality with a paid error, a precise missing estimate tied to named available source data, or a scoped limitation on the chosen observable. If the calculation only renames q, a crossing count, or the unknown endpoint geometry, record that outcome without promoting it to a new mechanism.

Possible focused questions: Does the forest representation help preserve correlated numerator/denominator errors? Can the full heat-response term be compared with an independently controlled reference? Can a window of spectral activity separate a collision signature from the dense simple-root background on a prescribed microscopic clock? Which canonical arithmetic feature would distinguish the answers from generic heat systems? These are questions, not established advantages.

## 7. Minimum calibration controls

- **Double and Hermite heat births:** H=z^2-2t and higher heat polynomials must retain their genuine collision signatures. They satisfy the generic real heat geometry.
- **A simple close pair:** H=z^2-r^2-2t, r>0, has simple endpoint roots but q(t)=2t/(r^2+4t). When r^2 is small compared with the chosen t, it can resemble the double. This tests a claim of uniform discrimination.
- **An entire threshold model:** H=e^t cos z+1 has simple real roots for t>0, double real roots at zero, and nonreal pairs for t<0. It realizes the qualitative phase picture with an atomic source and no theta arithmetic. Thus that picture alone does not imply endpoint simplicity.
- **A simple clock field:** H=e^t sin z keeps equally spaced simple roots. Its finite spectral diagnostic depends on time and density even though its root geometry is stationary.
- **The [registered source controls][controls]:** apply each proposed bound only where its own hypotheses hold. Euler-factor controls change the canonical Dirichlet coefficients; weighted-square controls lack full reflection and have no all-real heat time; reflected/positive-primitive controls do not acquire a global real-root interval by analogy; RH-conditional normalized endpoint controls share real descendant geometry while failing ordinary Dirichlet-series arithmetic. A sparse added double screens an all-simple conclusion but does not automatically defeat a density-one claim.

No new computation is required for these elementary calibrations. If a later calculation is warranted, use it to check a sign, normalization, scaling prediction or declared estimate; save small receipts and keep generated PDFs out of research folders under [the storage policy][large]. A future claim of advantage must compare the same source information, target and completed error budget.

[agents]: ../../../../../AGENTS.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
[a10]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[large]: ../../../../../LARGE_FILES.md
[history]: ../../../../../tools/CHAT_HISTORY.md
[dictionary]: ../../notes/17_STATISTICAL_MECHANICS_AND_FOREST_RESPONSE_20261023.md
[chat]: ../../chat-histories/0003_2026-10-23T20-35-30Z_clarify-e-i-in-l-x.json
[coefficient]: ../../notes/11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md
[spectrum]: ../../notes/10_EXACT_COLLISION_SPECTRUM_AND_GLOBAL_REDUCTION_20261023.md
[manuscript]: ../../manuscript/spectral_forest.tex
[relaxation]: ../../../11_late_heat_caps_and_charge_transport/notes/07_PCC_WEIGHTED_MOMENTS_AND_CAP_PHASE_SCREEN_20261022.md
[lee]: ../../../../investigations-2/active/13_stability_jensen_lee_yang/README.md
[stable]: ../../../../investigations-3/05_constructive_stable_models/README.md
[stable-summary]: ../../../../../result-summaries/17_constructive_stable_model_obstructions.md
[flux]: 04_OPEN_BOUNDARIES_ZERO_FLUX_AND_BACKWARD_WIDTH_20261023.md
[flux-next]: 05_CONTINUATION_ANALYTIC_OPEN_BOUNDARY_FLUX_20261023.md
[rt]: https://arxiv.org/abs/1801.05914
[nw]: https://arxiv.org/html/1901.06596v2
[forest]: https://arxiv.org/abs/math/0602575
