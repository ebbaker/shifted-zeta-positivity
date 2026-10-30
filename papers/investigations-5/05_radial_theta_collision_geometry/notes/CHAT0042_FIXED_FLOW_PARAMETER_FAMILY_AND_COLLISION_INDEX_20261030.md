# Fixed-flow parameter families and collision indices

30 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Actual recorded model **gpt-6-astra**, reasoning effort **xhigh**. Investigation05 chat0042, *Clarify signed cross-production questions*.

**Status: explanatory family construction and elementary index calculation, with a conditional boundary-transfer observation. Same-assistant derivation only; no independent review or new theta collision exclusion.** This responds to the author's proposal to fix the compression coefficient and study the physical parameter plane, rather than only individual normalized trajectories. It does not change the active research register or dispatch another chat.

Consult the [result index](../../../../result-summaries/README.md), [local collision/topology cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [control register](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), particularly [target reformulation](../../../../avoid/01_restating_the_target.md), [coordinate lifts](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. Correct distinction: parameter dependence versus loss of a common lifespan

The normalized construction has a marked family W^p(s), p=(T,A), with alpha^p(s)=2G^p(s)/D^p(s). Parameter dependence of alpha does not itself make this family discontinuous. [Note28, Sections 4-5](28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md) gives local smooth parameter dependence on compact time intervals inside a common lifespan. Differentiating a marked solution introduces

    partial_s(partial_A W^p)
    = L_(alpha^p)(partial_A W^p)
      +(partial_A alpha^p) div(v W^p).

The initial derivative is the actual derivative of W0^p. In Note28's separate running-parameter construction, the pure mark-response starts at zero; on the diagonal it must be added to the transported frequency jet. Those two derivatives must not be conflated.

At a hypothetical isolated collision p0, W^p0 has a finite maximal lifespan, while neighboring noncolliding marks have global lifespans. Local continuous dependence before the collision trajectory's endpoint does not give a bounded extension of the full family through that endpoint or uniform long-time estimates near p0. The protected denominator is valid on each regular real trajectory; it does not guarantee holomorphic continuation around a PDE singularity.

The norm-preserving real feedback has no automatically justified meromorphic extension. Continuing the literal Hermitian norm to complex parameters involves conjugation; a bilinear complexification of real squares would be a separate construction with its positivity and denominator protection rechecked. No residue of alpha is inferred here. The physical transform H itself is analytic at a collision: its zero, not a singularity of H, is the relevant event.

## 2. The concrete advantage of fixed c across the whole parameter family

Choose one c>0 independent of both T and A, and let

    L_c=Delta+c div(v dot),
    U_c(s;T,A)=P_s^c K1*[rho_T cos(Au)],
    V_c(s;T,A)=partial_A U_c(s;T,A)
                   =P_s^c K1*[-rho_T u sin(Au)].

The same linear operator and propagator act at every mark. All fixed physical parameter derivatives commute with this evolution. In particular,

    partial_T U_c = -partial_A^2 U_c,
    int (U_c,V_c) = (H,H_A).

The complete theta tail dominates all fixed parameter derivatives on compact parameter sets: derivatives add polynomial factors in u, complex A contributes at most exp(Cu), and bounded complex T contributes exp(Cu^2), all dominated by the complete double-exponential source decay. Source spatial moments are also finite because powers of |Y| become exp(Cu). Unit Gaussian preparation supplies uniform H1 budgets. Thus the finite-s family is smooth in real parameters and holomorphic under the ordinary complex parameter extension of the initial data, with the fixed real spatial semigroup acting complex-linearly. This is an advantage of a common operator; the squared energy is no longer fixed along s.

## 3. A uniform asymptotic observation retaining the physical jet

Use the preceding [fixed-compression comparison](CHAT0042_FIXED_COMPRESSION_AND_NORMALIZATION_COMPARISON_20261030.md). With

    p_c(X)=exp(-c mathcal V(X))/Z(c),
    mathcal V=(|X|^2+log(1+|X|^2))/2,
    m(T,A)=(H(T,A),H_A(T,A)),

it gives W_c(s;p)->m(p)p_c in L2. The same proof applies to each fixed parameter derivative: subtract its own stationary mass multiple, then use the zero-mass contraction and finite L1/H1/first-moment budgets. On a compact physical parameter set K these budgets have uniform finite upper bounds by Section 2. For each fixed multi-index nu,

    sup_(p in K) ||partial_p^nu[W_c(s;p)-m(p)p_c]||_2^2
    <= C_(K,nu,c) exp(-c s/2).

No lower physical mass floor enters these absolute bounds. Complex derivatives, if used, are handled by the same linear estimates on real and imaginary components. This is not relative control near a vanishing mass.

A bounded spatial observation avoiding unproved pointwise-in-X convergence is

    F_(c,s)(T,A)=<U_c(s;T,A),p_c>/||p_c||_2^2.

For real parameters this is the usual L2 pairing; its complex parameter extension uses the same real test p_c. It satisfies the physical backward heat equation, and

    (F_(c,s), partial_A F_(c,s)) -> (H,H_A)

uniformly on compact parameter sets, with absolute errors bounded by a constant times exp(-c s/4). This follows from Cauchy-Schwarz and the preceding L2 bounds. At a collision the limiting pair vanishes; nearby nonzero pairs remain. The collision can therefore be studied as a zero of the stationary projection, without a finite-s singularity of the fixed-c flow.

## 4. Local winding at a nondegenerate double collision

Let J(T,A)=(H,H_A), with physical orientation dT wedge dA, and suppose

    H(T0,A0)=H_A(T0,A0)=0,  b=H_AA(T0,A0) != 0.

Because H_T=-H_AA,

    det D_(T,A) J
    = H_T H_AA-H_A H_AT
    = -b^2 < 0

at the event. Hence the isolated zero has local real index -1: J/|J| winds once clockwise on a sufficiently small positively oriented physical loop. This is an elementary specialization of the repository's inherited index law, not a new invariant. [Note04, Section 4](04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md) and the result cluster route to the all-finite-multiplicity index -floor(k/2).

Writing H+iH_A packages this real-plane map conveniently; it does not assert that this function is holomorphic in T+iA. Its winding can be written as

    (1/(2 pi)) integral_Gamma
      (H dH_A-H_A dH)/(H^2+H_A^2),

when the jet is nonzero on Gamma.

A distinct ordinary complex residue is available at fixed T0: if H(T0,z)=(z-A0)^k g(z), g(A0)!=0, then

    H_A/H = k/(z-A0)+g'/g.

The logarithmic derivative has residue k. This counts zeros of H on that complex slice, including simple zeros, and must not be identified with the real heat-collision index. The classical input is [DLMF 1.10(iv)](https://dlmf.nist.gov/1.10#iv); the displayed local factorization proves the residue directly. It is not a residue of the feedback coefficient.

## 5. What would make this a useful topological route

For a compact physical region Omega with no jet zeros on its boundary, let

    delta_Gamma=min_(p in boundary Omega) |J(p)| > 0.

If the observed jet J_s=(F_(c,s),partial_A F_(c,s)) obeys

    sup_Gamma |J_s-J| < delta_Gamma,

the straight-line boundary homotopy is nonzero, so wind_Gamma J_s=wind_Gamma J. This follows from the uniform absolute convergence in Section 3. A boundary margin is compatible with interior collisions; using such a margin is not the assumption that the whole region is collision-free.

Under the inherited isolated finite-order real-collision hypotheses, all interior indices are negative. An independently established zero boundary winding would exclude interior collisions. This is an existing degree criterion, not new progress toward its theta-specific premise. The missing useful input is an actual estimate of the observed boundary degree or a valid deformation to a known degree with every boundary crossing controlled. The fixed operator supplies organization and analytic parameter dependence, but does not itself supply zero winding. The full mass observation int W_c equals J at every s, so merely using that observation gives exactly the original winding without improvement.

The earlier Gaussian-deformation test [Note04](04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md) proves why a positive terminal profile alone is insufficient: its exact control loses an interior collision through the time boundary. That is a scoped warning about unpaid boundary crossings, not a rejection of the current fixed-c family.

## 6. Controls and stopping scope

Prepared Gaussian-polynomial and weighted-square colliding controls satisfy the same fixed-c common-operator construction on their stated physical domains, as in the preceding fixed-compression note. At an admitted nondegenerate double event they have the same index -1 and the same vanishing stationary jet. Thus regularity in physical parameters, common evolution, and existence of winding/residue diagnostics do not discriminate theta. The premise an eventual exclusion would need is a separately proved theta boundary estimate; no such premise is supplied here, and the controls are not claimed to fail a new estimate. Other registered families retain their own moment domains, multiplicity, reflection, and threshold qualifications; no additional events or extensions are inferred.

The bounded return is the explicit parameter-family advantage, the common-lifespan correction, and a precise absolute-error-to-boundary-degree interface. No source-specific degree restriction, changed source, new parameter coverage, numerical acquisition, manuscript change, or assertion of analytic continuation of the nonlinear blow-up is made.
