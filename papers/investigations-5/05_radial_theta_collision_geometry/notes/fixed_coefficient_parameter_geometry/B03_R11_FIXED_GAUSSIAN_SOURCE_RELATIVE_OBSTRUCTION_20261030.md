# B03 R11: complete Gaussian-packet payment and a fixed-model relative-error obstruction

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded **gpt-6-astra / max**, new Investigation05 **chat0052**, *Continue B03 R11 research*, thread `01a18f35-d72e-7a82-a9ec-eef93a001e1d`. [Progress06](../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md) owns live status. **Proved in-note using the named classical Hardy theorem; proof-author checking only. E02 R11 is unstarted.**

**Outcome.** A complete-source projection onto fixed Gaussian packets gives an explicit oscillatory leading term, a nonzero **model** first jet through its simple zeros, and an unconditional full residual payment. It nevertheless cannot give a uniformly relatively accurate physical first jet on
\[
 \mathcal D=\{(T,A):31/128\le T\le33/128,\ A\ge64\}.                 \tag{1}
\]
For each fixed T in this interval and every finite A0>=64, no fixed finite Gaussian-packet/Hermite model can have its true first-jet error bounded by any finite multiple of its model first jet on all A>=A0. Nor can its true error be at most q times the physical first jet there for any fixed q<1. This is an application of Hardy uncertainty to the complete theta source. It is stronger than failure of the displayed absolute payment, but supplies no collision, no effective first failing height, and no new covered theta region.

This is the requested **scoped-failure completion of B03 R11**, not a positive source-separation theorem. R9's finite simple-zero tube, R10's common-c energy floor, and E02 R10's accepted width4 estimator obstruction remain unchanged. Global B04 coverage and RH/Newman transfer remain unresolved.

## 1. Classification, predecessors, and fixed contract

The selected mechanism is a projection of the **raw complete even source**, followed by its exact Fourier/heat transform. Signed projection coefficients and all retained oscillatory terms stay together; the omitted source is paid once on the entire real line. This differs from R9/R10's finite physical jet transported from A=64 with a complete-M4 absolute core payment. No order17 input is consumed.

It also differs from [BW12 Note14](../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/14_GAUSSIAN_HERMITE_RECONSTRUCTION_AND_RESPONSE_QUOTIENT_20261021.md), which projects a positive-time residual in the observation variable and reconstructs an endpoint Taylor polynomial, and from [transport Note21](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/21_COMPLETE_THETA_GAUSSIAN_HERMITE_READOUT_20261011.md), whose Hermite readout is exact and infinite-dimensional. Neither is rejected by this note. The [S04 full-cutoff source contract](../../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md) retains a growing arithmetic sum and has its own unresolved signed core; it is not a fixed Gaussian model.

This is an estimating-class obstruction, not an RH-equivalent reformulation. Its decisive quantitative statements are the complete error constants (8), the independent model-jet floor (12), and the impossibility of **every finite** model-relative error multiplier in (14). No assertion counts or sampled signs support the unbounded claim. The mechanism/domain/stop rule were recorded in Progress06 before checks; no source integration, new moment acquisition, root finder, or degree/width/height scan is issued.

Read the [result index](../../../../../result-summaries/README.md), especially [theta bookkeeping](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../avoid/README.md), especially [classification](../../../../../avoid/01_restating_the_target.md), [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [preserving cancellation](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [noncircular inputs](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md), and [unchecked imports](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## 2. Complete source bounds, with no omitted arithmetic or exterior

Use the unchanged [source normalization](../01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md): for u>=0,
\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                    e^{-\pi n^2e^{4u}},\qquad \Phi_e(u)=\Phi(|u|),
\]
\[
 f_T(u)=e^{Tu^2}\Phi_e(u),\qquad
 H(T,A)=\tfrac12\int_{\mathbb R} f_T(u)e^{iAu}\,du,
 \qquad J=(H,H_A).                                           \tag{2}
\]
Every half-line mode is positive. Put v=e^(4u)>=1. Since n^4<=16^(n-1) and n^2-1>=3(n-1),
\[
 0<\Phi(u)\le
 \frac{2\pi^2e^{9u-\pi e^{4u}}}{1-16e^{-3\pi e^{4u}}}
 <20e^{9u-3e^{4u}}<e^{-24u^2}.                               \tag{3}
\]
For the constants, pi>3, pi<22/7, e^3>20 give 16e^(-9)<1/500 and
2(22/7)^2/(1-1/500)<20. The last inequality uses
e^(4u)>=1+4u+8u^2 and 20e^(-3)<1. Even extension gives the same bound at the other end. Thus the complete weighted squared source mass satisfies
\[
 S:=\int_{\mathbb R}e^{u^2}\Phi_e(u)^2du<\sqrt{\pi/47}.        \tag{4}
\]
For Hardy's theorem we need more than a single Gaussian. Keeping the fourth Taylor term of e^(4u), for every a>0 and every T<=T_+=33/128,
\[
 0<f_T(u)\le C_a e^{-a u^2},\qquad
 C_a=\exp\!\left(\frac{(a+T_+-24)_+^2}{128}\right).            \tag{5}
\]
Indeed 9u-3e^(4u)+(T+a)u^2 is at most
-3-3u+(a+T_+-24)u^2-32u^4, and Bx-32x^2<=B_+^2/128 for x=u^2. The factor 20e^(-3) is less than one. This pays **every Gaussian rate** with a displayed constant; it is not an assumed complex-contour asymptotic or a claim about H's pointwise lower size.

We also need an independent nonzero source input. For 0<=u<=1/16, the n=1 mode alone gives
\[
 \Phi(u)>9e^{-5}>1/27.                                      \tag{6}
\]
Here e^(1/4)<4/3, pi e^(1/4)<88/21<5, pi(2pi-3)>9, and e<3. Thus the source cannot vanish. Using positive modes for these source majorants/lower bounds does not split or sign the final oscillatory field.

## 3. A signed finite projection and its complete error

Fix the weighted Hilbert space X=L2(R,e^(u^2)du). One specific hierarchy of even source packets is
\[
 V_N=\operatorname{span}\{u^{2k}e^{-32u^2}\cosh(8u):0\le k\le N\},
 \quad N=0,1,\ldots .
\]
These are finite Hermite combinations of two shifted Gaussians centered at +/-1/8. The basis is linearly independent. Let g_N be the orthogonal projection of the **whole** Phi_e onto V_N and r_N=Phi_e-g_N. With basis psi_k, its exact coefficients are G^(-1)c, where
\[
 G_{kl}=\int e^{u^2}\psi_k\psi_l\,du,\qquad
 c_k=\int e^{u^2}\Phi_e\psi_k\,du.
\]
G is strictly positive definite and its entries are Gaussian moments. The c_k are complete source integrals, not a truncated square expansion; the solution coefficients may have either sign. No coefficient has been numerically acquired here.

Define
\[
 \widetilde H_N(T,A)=\tfrac12\int e^{Tu^2}g_N(u)e^{iAu}\,du,
 \quad E_N=H-\widetilde H_N,
 \quad \rho_N=\|r_N\|_X.
\]
Pythagoras gives rho_N^2=S-c^t G^(-1)c and, unconditionally,
\[
 0\le\rho_N\le S^{1/2}<(\pi/47)^{1/4}.                      \tag{7}
\]
The difference in this identity is an **error norm**, not a positive physical margin. Its sign is justified by projection, and no small value is assumed. A future numerical subtraction would require outward errors for the complete S, c and G. For rounded coefficients v the correct squared residual is S-2c^t v+v^tGv; exact-projection orthogonality may not be assigned to v.

For j=0,1,2, Cauchy--Schwarz on the entire real line yields
\[
 |\partial_A^j E_N(T,A)|\le
 \epsilon_{j,N}:=\frac{\rho_N}{2}
 \left[\frac{\Gamma(j+1/2)}{\kappa_0^{j+1/2}}\right]^{1/2},
 \qquad \kappa_0=1-2T_+=31/64.                               \tag{8}
\]
Replacing rho_N by (pi/47)^(1/4) is a fully explicit conservative payment requiring no acquisition. The three Gaussian integrals are sqrt(pi)/sqrt(kappa0), sqrt(pi)/(2 kappa0^(3/2)), and 3sqrt(pi)/(4 kappa0^(5/2)). In particular
\[
 \|J-\widetilde J_N\|\le
 B_N=(\epsilon_{0,N}^2+\epsilon_{1,N}^2)^{1/2},
 \qquad \widetilde J_N=(\widetilde H_N,\partial_A\widetilde H_N).
                                                                    \tag{9}
\]
This pays all source modes, both infinite source rays, the entire time interval, and both jet components. No finite upper boundary, cut-off transition, or separate exterior has been dropped. There is no auxiliary spatial-flow step in this mechanism. The transform obeys the same physical heat equation because its source coefficients are independent of T.

For the discriminant D=H_A^2-2HH_AA, the complete additional payment, if desired, is
\[
 |D-\widetilde D_N|\le
 2|\widetilde H_{N,A}|\epsilon_1+\epsilon_1^2
 +2|\widetilde H_N|\epsilon_2+2|\widetilde H_{N,AA}|\epsilon_0
 +2\epsilon_0\epsilon_2.                                    \tag{10}
\]
All mixed terms remain in the exact signed leading discriminant before the residual is bounded. No positive discriminant or first-jet theta margin follows from these formulas alone.

## 4. Explicit leading wave and a denominator that is actually paid

For N=0 put g_0(u)=a_0 exp(-32u^2)cosh(8u). Then
\[
 a_0=C_0/D_0>1/810,\quad
 C_0=\int\Phi_e(u)e^{-31u^2}\cosh(8u)du,\quad
 D_0=\frac12\sqrt{\pi/63}(1+e^{64/63}).
\]
For the lower bound, (6) and exp(-31u^2)>1/3 on |u|<=1/16 give C0>1/648. Also sqrt(pi/63)<1/4 and exp(64/63)<e^2<9 give D0<5/4. These are full-source and elementary Gaussian estimates, independent of H or J.

Write b=32-T, so 4063/128<=b<=4065/128. Completing the square gives the exact leading wave
\[
 \widetilde H_0(T,A)=m(T)e^{-A^2/(4b)}\cos(4A/b),\qquad
 m(T)=\frac{a_0\sqrt\pi}{2\sqrt b}e^{16/b}>1/6480.             \tag{11}
\]
Its zeros A_k=b*pi*(2k+1)/8 are simple. Let theta=4A/b. The normalized first jet is the matrix [[1,0],[-A/(2b),-4/b]] applied to (cos(theta),sin(theta)). Its smallest singular value is at least its determinant magnitude divided by its Frobenius norm. Therefore throughout (1), including every model zero,
\[
 \|\widetilde J_0(T,A)\|\ge
 \frac{4m(T)e^{-A^2/(4b)}}{\sqrt{b^2+A^2/4+16}}
 >\frac{e^{-32A^2/4063}}{1620\sqrt{1040+A^2/4}}.               \tag{12}
\]
This is a proved, explicit **model-amplitude** floor, not an assumed minimum of the theta first jet. A physical conclusion would still require B0 smaller than that floor, or another correctly paid signed error comparison. In particular neither H nor J has been used as an unproved denominator. Scalar H is unavailable across R9's accepted simple-zero curve.

## 5. Why even a perfect signed remainder cannot rescue a fixed Gaussian model

We use the strict Hardy uncertainty theorem in the checked [primary-source annotation](../../references/18_HARDY_UNCERTAINTY_AND_FIXED_GAUSSIAN_SCOPE_20261030.md): for the angular-frequency Fourier transform, Gaussian bounds with exponents a and d and ad>1/4 force the function to be zero. This is classical, not a new theorem of this investigation. The constant Fourier normalization in (2) does not change the threshold.

**Lemma.** For each fixed real finite T, H(T,A) admits no bound C exp(-d A^2), with C finite and d>0, on an entire tail A>=A0.

*Proof.* The derivation of (5) works with any fixed finite T as its upper endpoint, so f_T has every Gaussian source bound. Evenness extends a hypothetical one-sided Fourier bound to both tails; continuity supplies a larger finite constant on the compact remainder. Choose a>1/(4d). Since the unitary Fourier transform of f_T is 2H/sqrt(2pi), Hardy forces f_T=0, contradicting (6). No theta zero theorem or claimed exponential asymptotic is imported. *End proof.*

For every fixed N, exact Gaussian transformation shows that tilde H_N and its first derivative are a Gaussian exp(-A^2/(4b)) times finite polynomials multiplying cos(4A/b) and sin(4A/b). More generally the following theorem applies to any fixed finite sum of polynomial-weighted shifted or modulated Gaussians, with heat integrability on the declared domain. At each fixed T its first jet has a bound
\[
 \|\widetilde J(T,A)\|\le C_T(1+A)^{d_T}e^{-\delta_T A^2},
 \qquad\delta_T>0.                                         \tag{13}
\]
The constants, degree and packets may depend on T, but cannot depend on the observation height A. This property, rather than positivity or the fitting algorithm, is the scope of the argument.

**Theorem (fixed Gaussian first-jet obstruction).** Fix T in (1). For every finite K>=0 and A0>=64 there is an A>=A0 such that
\[
 \|J(T,A)-\widetilde J(T,A)\|>K\|\widetilde J(T,A)\|.           \tag{14}
\]
Also, for every 0<=q<1 and finite A0>=64 there is an A>=A0 such that
\[
 \|J(T,A)-\widetilde J(T,A)\|>q\|J(T,A)\|.                    \tag{15}
\]
*Proof.* If (14) failed on a tail, the triangle inequality would give |H|<=||J||<=(K+1)||tilde J||. Absorb the polynomial in (13) into exp(delta_T A^2/2); the lemma is contradicted. If (15) failed, the reverse triangle inequality would give (1-q)||J||<=||tilde J||, with the same contradiction. Both statements use inequalities, so possible physical or model collisions never create a division by zero. *End proof.*

For the explicit paired Gaussian, (12) makes its model-relative error ratio well-defined everywhere, and (14) says its supremum on **every** height tail is infinite. It does **not** say the ratio tends to infinity along every sequence, or that a physical zero is a collision. Equation (15) excludes a uniform strict relative approximation, not every physical-relative estimate with constant at least one.

For the selected projection, rho_N is strictly positive: otherwise the complete source would equal a finite Gaussian packet, contradicting the lemma after transformation. Thus the fixed payment B_N in (9) is positive, while the model jet tends to zero. That payment consequently rejects all sufficiently large heights at each fixed T. The stronger (14)--(15) show that this is not solely a weakness of Cauchy--Schwarz: no evaluation of the **true signed remainder** can establish the prohibited uniform relative inequalities for that fixed model. The proof does not locate a numerical rejection onset, and none was searched for.

## 6. Controls, scientific scope, and disposition

The complete-source constants (3)--(8) and coefficient floor in Section 4 belong to the unchanged unit theta source. For another source they must be proved anew. The Gaussian transform, projection identity and singular-value calculation are generic and do not distinguish theta from a colliding source.

| Control family from the repository register | Premise/claim it does not inherit |
| --- | --- |
| Euler-factor controls | Unchanged unit theta arithmetic/source, hence this coefficient and source envelope; an altered source may separately meet the generic Hardy hypotheses. |
| Weighted-square and finite-prime controls | Full normalized theta reflection and unchanged coefficients; theta's source constants cannot be assigned to their event boxes. |
| Reflected super-Gaussian, smooth shape, positive-primitive controls | Complete unit theta square expansion. Those with nonzero super-Gaussian sources **do satisfy the generic obstruction**, which is compatible with their collisions. No control fails every premise of that generic theorem. |
| Atomic and finite-profile controls | Atomic sources are outside the weighted L2 projection class. Continuous compact variants require their own norm and can satisfy the generic Hardy obstruction; no event is excluded. |
| Changed observation kernels | Literal cosine/Fourier reconstruction (2). |
| Conditional endpoint controls | Their original existence hypotheses and their own source data remain necessary. If they satisfy Hardy's hypotheses, the obstruction applies without contradicting an event. |

At any actual admissible control collision J=0, a **successful positive** triangle certificate ||tilde J||>B is impossible because its true error equals ||tilde J||. The present work never claims such a certificate for theta on (1). Controls therefore screen the intended positivity consumer without being misused as tests of the classical uncertainty theorem.

**Retain:** full weighted source payment, exact paired-wave leading term, independently paid model jet, and the fixed-model obstruction. **Stop:** acquisition or finite-degree optimization intended to make this fixed Gaussian class uniformly relatively accurate on (1). **Outside the stop:** finite height intervals; an infinite Gaussian expansion; height-dependent families that lose the uniform Gaussian envelope; non-Gaussian signed models; error estimates used for a different, non-relative purpose. In particular R8's Gaussian *error weight* is not a Gaussian approximation to the physical field and is unaffected.

Even an adaptive model fails if its entire first jet still has one bound C exp(-d A^2), d>0, on a height tail. Escaping that envelope is a **necessary design condition**, not an error estimate or positive amplitude. Merely allowing more parameters does not prove the next mechanism works.

**B03 R11 is complete with proof-author checking.** See the [self-review](../../reviews/fixed_coefficient_parameter_geometry/B03_R11_FIXED_GAUSSIAN_SELF_REVIEW_20261030.md), [source-free bookkeeping record](../../numerics/fixed_coefficient_parameter_geometry/fcg_b03_r11_gaussian_obstruction_checks_20261030.json), [fixed E02 R11 assessment](../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R11_FIXED_GAUSSIAN_ASSESSMENT_20261030.md), and [continuation/model handoff](B03_R11_RETURN_AND_MODEL_HANDOFF_20261030.md). Internal author checking does not constitute a different-model assessment, specialist review, or formal proof. No manuscript, DRAFT_HISTORY, source acquisition, or global target transfer is supplied.
