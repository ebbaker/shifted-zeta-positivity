# Statistical mechanics, the heat threshold and the forest response

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **xhigh**.

**Status: explanatory dictionary and elementary finite identities; no new theta estimate, phase-transition theorem or simplicity result.** The author suggested a boiling/nucleation picture for the heat threshold and related inverse-gap spectra to critical pair statistics. This note records the exact connections and distinguishes finite collision geometry from a thermodynamic singularity. The manuscript is not changed by this note.

Read the [result index](../../../../result-summaries/README.md), [patterns to avoid](../../../../avoid/README.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), and the rules on [reformulations](../../../../avoid/01_restating_the_target.md) and [scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md). The dictionary below is not an independent mechanism or source estimate.

## 1. The established threshold and the local bubble picture

For the canonical normalization H_t=-H_zz, all zeros of H(t,.) are real exactly when t>=Lambda. Rodgers and Tao proved Lambda>=0. Consequently, every t<0 has some nonreal zeros, unconditionally. RH is equivalent to Lambda=0 in conjunction with that theorem. Reality at t=0 permits multiple real zeros; excluding them is the additional simplicity question.

The elementary double model is H(t,z)=(z-x_*)^2-2(t-t_*). It has two real roots above t_*, a real double at t_*, and a conjugate nonreal pair below t_*. This describes a local collision; it is not a theorem that a canonical event occurs at t=0. If the endpoint zeros are all real and simple, every fixed compact region with a zero-free enclosing boundary has a sufficiently small collision-free negative-time neighborhood. Nonreal zeros at times approaching zero can then escape every bounded spatial region. Thus a global threshold at zero need not be attained by a collision at a finite zero ordinate.

Primary sources: [Rodgers-Tao](https://arxiv.org/abs/1801.05914); [Newman-Wu, Sections 2.4-2.6](https://arxiv.org/html/1901.06596v2). Section 2.5 of the latter explicitly treats partition functions, Lee-Yang systems and Euclidean field theory. Heat time is a deformation parameter; identifying it with a physical temperature requires a specified model.

## 2. An exact partition function at a fixed real configuration

Fix distinct real x_i and the inverse-square Laplacian L. For a>0 let

\[
 Z(a)=\det(I+aL)
 =\sum_F a^{k(F)}\left(\prod_{C\in\operatorname{comp}(F)}|C|\right)
       \prod_{\{i,j\}\in E(F)}(x_i-x_j)^{-2},
 \qquad k(F)=|E(F)|.
\]

The sum is over spanning labeled forests, including isolated vertices. The factor product_C |C| counts choices of one distinguished root in each tree. This is a positive partition function on rooted forests with edge activity a and fixed gap weights. It is an instance of the classical weighted [matrix-forest theorem, Chebotarev-Shamis](https://arxiv.org/abs/math/0602575), not a new statistical ensemble specific to theta. The [manuscript's forest proposition](../manuscript/spectral_forest.tex) uses D=Delta Z; Delta is independent of a and cancels in the normalized forest measure.

Set theta=log a and normalize the displayed weights to a probability distribution. Differentiation of this finite sum gives

\[
 q_a=\partial_\theta\log Z=\mathbb E_a[k],
 \qquad
 \partial_\theta q_a=\partial_\theta^2\log Z
       =\operatorname{Var}_a(k).
\]

Since Z=product_j(1+a lambda_j), the response also equals

\[
 \boxed{\operatorname{Var}_a(k)
 =\sum_j\frac{a\lambda_j}{(1+a\lambda_j)^2}.}
\]

The bump discussed in the chat is therefore exactly the fluctuation response of forest edge count to log activity. Its summand peaks at a lambda=1 and tends to zero at both ends. In statistical-mechanical terminology this is a susceptibility for the edge-count observable. All derivatives here hold x and L fixed. For the manuscript q(t), a=4t and L=L(x(t)); its total time derivative contains additional root-motion terms.

For fixed finite N and distinct real roots, Z(a)>0 and is analytic for positive a, so this ensemble has no singular transition as a varies there. A thermodynamic phase transition would require a specified growing-system limit and a limiting singularity; these identities do not provide one. The collision endpoint also changes L, so its singular limit is a different issue from differentiating a at a fixed configuration.

## 3. What the inverse-square matrix measures

L is a deterministic stiffness/Hessian matrix of the logarithmic Vandermonde energy. In particular

\[
 \operatorname{Tr}L=2\sum_{i<j}(x_i-x_j)^{-2}.
\]

Thus its trace is an inverse-square moment of the finite pair separations. A pair-correlation measure records separation statistics; L additionally retains the labels and collective eigenmodes. Near the double model at t_*=0, the squared gap is 8t and the nonzero pair eigenvalue is 1/(4t). Its divergence is local collision curvature. The dimensionless filter 4tL extracts the finite signature q=1/2. This need not imply divergence of a bulk correlation length or of a thermodynamic susceptibility.

## 4. Existing project routes and the remaining information

- [LHCT Note 07, Section 4](../../11_late_heat_caps_and_charge_transport/notes/07_PCC_WEIGHTED_MOMENTS_AND_CAP_PHASE_SCREEN_20261022.md) proves the deterministic logarithmic-energy relaxation for full finite heat polynomials and retains the exterior force for selected clusters. It distinguishes deterministic Hermite equilibrium from stochastic Dyson/GUE statistics.
- [Stability, Jensen and Lee-Yang preparation](../../../investigations-2/active/13_stability_jensen_lee_yang/README.md) is the earlier source-preparation program, currently deferred.
- [Constructive stable models](../../../investigations-3/05_constructive_stable_models/README.md), summarized in [result cluster 17](../../../../result-summaries/17_constructive_stable_model_obstructions.md), investigates spin and quartic preparations and records exclusions of specified families. Those exclusions do not cover every interacting statistical-mechanical realization.

The forest identities apply to every distinct real finite configuration, including descendants of Hermite collision controls. The normalized endpoint controls share the generic real heat geometry while failing ordinary Dirichlet-series arithmetic; weighted-square and reflected controls are not assigned an unproved all-real global interval. These observations follow the linked control register: the statistical-mechanical dictionary does not select the unchanged theta source or supply the missing microscopic upper estimate. Its concrete explanatory gain is to identify the previously discussed bump with a finite forest variance.
