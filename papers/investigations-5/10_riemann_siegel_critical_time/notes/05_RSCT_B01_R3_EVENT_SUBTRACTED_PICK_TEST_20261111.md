# RSCT-B01 r3: event subtraction, signed arithmetic and a fixed-height matrix limit

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0001. Actual backend model and reasoning effort are unavailable in the recorded configuration. Type B; the task recommendation is GPT-6 Astra/ultra, not verified provenance.

**Status: proved in-note from named inherited approximation inputs; same-assistant checking only.** The selected relation is positivity of the complete logarithmic-derivative matrix after subtracting the entire ±a event. Its signed arithmetic acquisition gives a conditional multiplicity cap
\[
 m\le \frac6{13}\log(a/(4\pi))+O(1)
\]
on the declared shrinking-time band. More decisively, the exact canonical matrix passes this necessary test for every fixed proposed multiplicity at sufficiently large centers, whether or not a real event exists there. **This is a scoped failure of the fixed-height matrix exclusion test, not construction of a canonical collision or a realizing zero configuration.** No new event region is excluded; constants and onset remain uninstantiated.

This is the one supporting derivation for [Decision03](../brainstorm/notes/03_RSCT_B01_R3_EVENT_BACKGROUND_DECISION_20261111.md). Read the [result index](../../../../result-summaries/README.md), [cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [controls12](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), particularly [classification01](../../../../avoid/01_restating_the_target.md), [premises02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [separate bounds12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. Objects, domain and choice

Keep the complete canonical theta source, H_0(z)=ξ((1+iz)/2)/8 and ∂_T H=−H_zz. The exact evolved reflected expression is [Polymath v2 §4 (35)–(39)](https://arxiv.org/html/1904.12438v2#S4), reproduced with its full remainder in [Note03](03_RSCT_B01_REFLECTED_POISSON_TEST_20261111.md). Both arithmetic arms and the exact gamma/correction terms remain part of the field. We never divide by an individual real-axis arm.

Set
\[
 L=\log(a/(4\pi)),\quad T=c/L,\quad \tfrac12\le c\le1,
 \qquad b=(4,6,8),\quad z_j=a+ib_j.                       \tag{1}
\]
T is fixed throughout spatial differentiation. The arithmetic estimates hold at every sufficiently large center a in (1), without all-realness. For their event consumer, assume T is the positive canonical threshold, all zeros of H_T are real, and a>0 is a zero of arbitrary multiplicity m≥2. Evenness supplies multiplicity m at −a. No assumption puts an arbitrary threshold in (1); all other time-height regimes remain uncovered.

R2 obtained a signed background requirement R<−1/36, but its kernel changes sign. Here we select one alternative relation: the positive matrix of the **event-deflated** logarithmic derivative. Unlike a scalar diagonal test, it retains cross-correlations of three complete arithmetic observations. It is a necessary relation, not a new RH-equivalent criterion or an assertion that finite positivity characterizes the threshold. Its quantitative cap and its inability to reject a fixed m are what is tested.

## 2. Exact relation between event and background

At an all-real slice put h(z)=−H_T′(z)/H_T(z). Evenness, order one and H_T(0)>0 give the paired product and logarithmic derivative in [Polymath v2, proof of Proposition 3.1 after (33)](https://arxiv.org/html/1904.12438v2#S3). Pair ±r in h; the matrix below converges absolutely because ∑r≠0 r⁻²<∞. With zeros counted with multiplicity,
\[
 M_{ij}:=\frac{h(z_i)-\overline{h(z_j)}}{z_i-\overline{z_j}}
       =\sum_r\frac1{(z_i-r)(\overline{z_j}-r)}.           \tag{2}
\]
This is a Gram matrix, hence positive semidefinite. No interpolation theorem is imported: the displayed sum proves the claim directly. Define
\[
 u_j=\frac1{ib_j},\qquad v_j=\frac1{2a+ib_j},\qquad
 E=uu^*+vv^*.
\]
Removing all m copies at each event location gives the exact necessary relation
\[
 \boxed{M_{\rm bg}=M-mE\succeq0.}                        \tag{3}
\]
All other zeros, including any other multiple zeros, remain in M_bg. The deflated function and field are
\[
 H_{\rm bg}(z)=H_T(z)/(z^2-a^2)^m,\qquad
 h_{\rm bg}=h+\frac m{z-a}+\frac m{z+a}.
\]
The plus signs here are essential: h itself has residues −m. Consequently
\[
 p_{\rm bg}(y):=\Im h_{\rm bg}(a+iy)
 =\Im h(a+iy)-m\left(\frac1y+\frac{y}{4a^2+y^2}\right)\ge0.
                                                               \tag{4}
\]
At the sample heights p_bg(b_j)=b_j(M_bg)_jj; (3) also retains the off-diagonal restrictions.

There is an exact connection to r2, rather than a change of background object. Since d_y log|H_T(a+iy)|=Im h(a+iy), its noncentral sum is
\[
 \begin{split}
 R&=W-m[K(0)+K(2a)]\\
  &=\int_4^6 p_{\rm bg}(y)\,dy-\int_6^8p_{\rm bg}(y)\,dy,\\
 K(d)&=\tfrac12\log\frac{(d^2+36)^2}{(d^2+16)(d^2+64)}.
 \end{split}                                                  \tag{5}
\]
The sums/integrals interchange by the paired product and uniform convergence off the real axis. Positivity of p_bg does not order the two integrals. The previous negative R requirement is therefore compatible with (4). A finite matrix only checks necessary sample restrictions, not the entire positive zero measure underlying (5).

## 3. Pay the complete field and the spatial derivative

Use exactly the nonvanishing carrier C_− of [Note04 (3)](04_RSCT_B01_R2_SIGNED_THREE_HEIGHT_ESTIMATE_20261111.md):
\[
 \begin{split}
 g(z):=\log C_-(T,z)
  ={}&\log(\pi^{1/4}/32)+\tfrac74\Log z-\tfrac{\pi z}8
       +\tfrac T{16}(L(z)^2-\pi^2/4)\\
     &-\tfrac{iz}4(L(z)-1)-\tfrac{i\pi T L(z)}{16}
       -\tfrac{7\pi i}8,\qquad L(z)=\Log(z/(4\pi)).
 \end{split}                                                  \tag{6}
\]
Branches agree with the upper-half-plane convention; V=H_T/C_− is holomorphic near each sample. This elementary carrier is not an exact gamma factor. The complete error behind it is inherited from [HDA Ansatz Note04 CS3/CS6](../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md) and [Assessment03](../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md), used in [GNP-RS E01 §§3–4, E9–E19](../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md). Their stated internal evidence levels are retained; the whole inherited proof chain is not independently revalidated here. Polymath Theorem 1.3's printed y≤1 region is not enlarged.

R2 paid point values. To obtain h, use the closed disks |z−z_j|≤1/2 inside the HDA fixed target r=1,b=9. Keep N=N_a=⌊√(a/(4π))⌋ fixed on this chart, including at a fractional-cutoff crossing. Keep the same enlarged source buffers and Gaussian exterior required by CS6. Write
\[
 s^0(z)=\frac{1-iz}2+\frac c4-\frac{i\pi T}8,\quad
 Z(z)=\zeta(s^0(z)),\quad \Delta=V-Z.
\]
On the disks, 7/2≤Im z≤17/2 and Re s^0≥9/4. E13–E17 extend by their explicit inequalities as follows; constants are newly enlarged for this compact range, not reused as identical numerical values:

| Contribution to Δ | Uniform payment |
| --- | --- |
| Entire growing reflected population | O(a^((1−y)/4))=O(a^(−5/8)) |
| Retained correction, including true gamma factors | O(a^(−(y+1)/4))=O(a^(−9/8)) |
| Full CS6 normalized field error | O(a^(−3/4)) |
| Removing the dominant quadratic heat weight | T D₂/4, where D_k=∑n≥2 n^(−9/4)(log n)^k |
| Dominant Dirichlet tail | (4/5)N^(−5/4)=O(a^(−5/8)) |
| Shift T(L(z)−L)/4 in the zeta argument | D₁T|L(z)−L|/4=O(1/(aL)) |

For detail, |Re z−a|≤1/2 permits replacing powers of Re z by powers of a with fixed factors; |L(z)−L|≤18/a after a finite onset. Also log n≤L/2≤Re L(z) for n≤N. Thus the heat-weighted dominant summands have modulus at most n^(−9/4), and |w_n|≤n^(−1/2) for the reflected arm. The population constant is the finite maximum of the E14 envelope for 7/2≤y≤17/2 with the fixed-chart factors included. The correction coefficient is bounded on the same compact fractional-cutoff neighborhood as CS3. These facts justify every row on the whole disks, not by interpolation of endpoint values.

Absorb L a^(−5/8) into a finite enlarged constant after the inherited onsets. There is a finite C_Δ, independent of a,c in (1), such that
\[
 \sup_{|z-z_j|\le1/2}|\Delta(z)|\le C_\Delta/L,
 \qquad |\Delta'(z_j)|\le2C_\Delta/L.                    \tag{7}
\]
The second bound is Cauchy's estimate on the holomorphic difference V−Z. It is not differentiation of a real-line big-O, a floor, the time T=c/L, or a piecewise approximant.

For the denominator payment, [DLMF 25.2.1 and 25.2.6](https://dlmf.nist.gov/25.2) give
\[
 |Z-1|\le 2^{-9/4}+\int_2^\infty x^{-9/4}dx
  =\frac{13}{5\,2^{9/4}}<\frac34,
 \qquad |Z'|\le D_1/2=:B_Z.
\]
Thus |Z|>1/4. The gate C_Δ/L≤1/8 ensures |V|>1/8 throughout each disk. In particular,
\[
 \left|\frac{V'}V-\frac{Z'}Z\right|
 \le \frac{C_h}{L},\qquad C_h=(16+32B_Z)C_\Delta.          \tag{8}
\]
This pays the derivative and both denominators before forming the matrix.

## 4. Signed arithmetic matrix and its retained bulk

Put σ_j=(1+b_j)/2+c/4, ν=a/2+πT/8. Logarithmic differentiation of the absolutely convergent [Euler product, DLMF 25.2.11](https://dlmf.nist.gov/25.2#E11), only in Re s>1, yields
\[
 P_j=\sum_{n\ge2}\Lambda_{\rm vM}(n)n^{-\sigma_j}e^{i\nu\log n},
 \qquad h(z_j)=-g'(z_j)-\frac i2P_j+\epsilon_j,
 \quad |\epsilon_j|\le C_h/L.                            \tag{9}
\]
It is ordinary zeta that has this Euler product, after comparison with the complete heat field; no Euler product is asserted for H_T. The heat phase and the complete prime-power series are retained. Substitution into (2) first gives the **signed** relation
\[
 M_{ij}=\frac{-g'(z_i)+\overline{g'(z_j)}}{i(b_i+b_j)}
       -\frac{P_i+\overline{P_j}}{2(b_i+b_j)}+\mathcal E_{ij},
 \qquad |\mathcal E_{ij}|\le\frac{2C_h}{L(b_i+b_j)}.       \tag{10}
\]
Together with (3), this is the selected arithmetic relation between the event and its complete background. In particular, the cross terms are not replaced by three unrelated diagonal bounds.

Direct differentiation of (6) gives
\[
 g'(z)=\frac7{4z}-\frac\pi8+\frac{T L(z)}{8z}
       -\frac{iL(z)}4-\frac{i\pi T}{16z}.
\]
Uniformly at the three fixed heights, −g′(z_j)=π/8+iL/4+O(a⁻¹). Since Λ_vM(n)≤log n and σ_j≥5/2, the P_j are uniformly bounded. It follows, now bounding the assembled signed matrix, that
\[
 \boxed{M=\frac L2 C+O_{\rm op}(1),\qquad C_{ij}=\frac1{b_i+b_j}.}
                                                               \tag{11}
\]
The error is a Hermitian matrix with a finite uniform operator bound B. For example take three times a uniform entry bound from (10), including carrier remainder and C_h/L. No sign of a prime cosine is assumed. The exact canonical samples, not merely the asymptotic approximant, satisfy (11).

The matrix C is strictly positive: α* C α=∫₀∞|∑α_j e^(−b_j t)|²dt, and distinct b_j make the exponentials independent. Its smallest eigenvalue μ>0 is a fixed number. Therefore M is positive definite whenever Lμ/2>B. All constants, the floor gate, the inherited buffer onsets, and this last gate are finite but not numerically instantiated.

## 5. Optimized event cap and failure for fixed multiplicity

For positive definite M, (3) is equivalent to
\[
 m\le\mathfrak m(a,c):=
 \frac1{\lambda_{\max}(M^{-1/2}EM^{-1/2})}.              \tag{12}
\]
This is the largest real formal event weight allowed by this matrix, not a statement that the weight is realized by zeros. The reflected vector v remains in E. From (11),
\[
 M^{-1}=\frac2L C^{-1}+O_{\rm op}(L^{-2}),\quad
 \|v\|^2=O(a^{-2}).
\]
Let r_j=1/b_j, so u=−ir. The following elementary Cauchy-matrix identity avoids a numerical inverse:
\[
 r^tC^{-1}r=2\sum_j\frac1{b_j}.                          \tag{13}
\]
Indeed, write x=C⁻¹r and f(z)=∑x_j/(z+b_j). Since f(b_i)=1/b_i, the rational function 1−zf(z), with its value one at zero, is
\[
 1-zf(z)=(-1)^q\prod_{j=1}^q\frac{z-b_j}{z+b_j}.
\]
Differentiate at zero to obtain f(0)=2∑1/b_j. Here q=3. A rank-one eigenvalue and the O(a⁻²/L) norm of the reflected rank-one term give
\[
 \lambda_{\max}(M^{-1/2}EM^{-1/2})
 =\frac4L\sum_j\frac1{b_j}+O(L^{-2})+O(a^{-2}/L).
\]
For 4,6,8, ∑1/b_j=13/24, hence
\[
 \boxed{\mathfrak m(a,c)=\frac6{13}L+O(1).}               \tag{14}
\]
The constants are uniform in c. The single sample b=4 would give L+O(1); using all correlations improves that coefficient, but neither bound approaches two.

The stronger stopping fact does not need inversion. For any **fixed** positive integer m,
\[
 \lambda_{\min}(M-mE)\ge L\mu/2-B-m\|E\|>0             \tag{15}
\]
at every sufficiently large center. Here ||E||≤∑b_j⁻²+3/(4a²). Equation (15) follows from the actual canonical arithmetic (9)–(11), independently of whether H_T(a)=0. Thus the selected necessary condition passes even a proposed double event at all large centers in the band. It supplies no contrary inequality for the negative background in (5). This does **not** prove a simultaneous realizing background for all observations, a real divisor at a, or a positive threshold. It only stops exclusion by (3) at these fixed heights.

For interpretation, the leading C is the Gram matrix for rational zero kernels. Its exact continuum integral is
\[
 \int_{\mathbb R}\frac{dd}{(d+ib_i)(d-ib_j)}
   =\frac{2\pi}{b_i+b_j}.
\]
The minimum integral of the nonnegative squared rational kernel with unit response at d=0 is 2π/(rᵗC⁻¹r)=π/(∑1/b_j). Multiplying by the leading density L/(4π) gives (14)'s L/(4∑1/b_j). This is an algebraic reading of the carrier bulk, not an assumption of a uniformly spaced actual zero set. R2 canceled bulk and lost kernel positivity; this test keeps positivity and pays a bulk that grows with L.

The algebra of (13) applies to any finite distinct fixed positive heights. The asymptotic non-exclusion proof applies when a complete logarithmic-derivative comparison giving h(a+ib_j)=π/8+iL/4+O(1) has separately been proved. Here that comparison has been acquired only for 4,6,8 and their fixed buffers. No uniform theorem for growing sample counts, shrinking heights, or centers approaching the real axis follows.

## 6. Controls, ownership and bounded return

The [BW-01 positive three-atom threshold family](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md), reused in [r2 §6](04_RSCT_B01_R2_SIGNED_THREE_HEIGHT_ESTIMATE_20261111.md), is an exact analytical control. At q=1/2, ℓ=2π/3 its threshold field is (4/9)(cos(ℓz)+1/2)². At a_j=1+3j it has actual double events. Choosing each source member's T=c/log(a_j/(4π)) puts arbitrarily high events in (1). Its paired all-real product gives M_bg≽0 exactly; it also passes r2's W<4/255<1/6. Thus positivity and the signed-background requirement are compatible at an actual heat threshold. This control fails unchanged theta arithmetic/completion, full profile growth and eventual simplicity at threshold; it is not claimed to satisfy (9) or (11). The separate canonical calculation (15), rather than a false transfer of its coefficients, tests our arithmetic matrix.

The rest of [controls12](../../../../result-summaries/12_collision_controls_and_screening.md) is screened by premises, without new numerical runs:

| Control class | Premise failed or inference unavailable here |
| --- | --- |
| Euler-factor/translated | The canonical coefficient sequence and complete normalized field; its physical heat/reflection structure is not enough for (9). |
| Weighted-square, finite-tail, finite-prime orbit | Complete coefficient sequence and/or full reflection; many have no all-real heat time, so their local collisions do not test (3)'s threshold hypothesis. |
| Reflected super-Gaussian, smooth shape, positive primitive | Canonical square-series arithmetic; a certified local event alone does not establish an all-real threshold. |
| Atomic, finite-profile and continuous compact-source threshold families | Unchanged theta coefficients, full profile growth and eventual simplicity at threshold; they do retain the exact geometric Gram positivity at their all-real events. |
| RH-conditional endpoint controls | Conditional hypothesis and time-zero domain; failed ordinary Dirichlet arithmetic. No unconditional positive-time canonical conclusion transfers. |
| Variable observation/heat counter-kernels | Literal cosine readout, source or physical generator; not this fixed H_T. |
| Relaxed actual-profile measures | Exact integer canonical zero population and simultaneous full field; feasibility is not a physical event. The same realization distinction is essential in interpreting (15). |

The general Herglotz/multiplicity observation already appears in [BW-10 Review08](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/08_RECIPROCAL_PRECISION_AND_KERNEL_REVIEW_20261020.md): a multiple zero gives allowed positive spectral mass. [BW-10 Note04](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/04_ZERO_DEFLATION_AND_RATIONAL_RESOLUTION_20261020.md) owns earlier rational-resolution/prime-cost work. We claim neither a new general simplicity criterion nor a transfer of its time-zero RH assumptions. The present contribution is the complete positive-time acquisition and coefficient (14), plus the explicit fixed-sample failure (15).

[HCB's register](../../03_heat_flow_collision_bounds/research-progress/02_POST_CALIBRATION_RESEARCH_PROGRESS_20261028.md) retains general first-jet/Poisson acquisition; [GNP-RS E01](../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md) and HDA retain the provider; [OA's gate](../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md) remains parked. None is reactivated or assigned this result.

**Return:** complete this bounded r3 pass with the derived conditional cap and scoped fixed-height failure. No numerical research, agents, manuscript, new zero coverage, independent validation or executable E01 request. A future authorized conceptual pass must add event-sensitive information beyond this finite necessary matrix, or pay a new resolving geometry. Neither sharper bounded prime constants nor more accurate errors at the same three fixed heights remove its leading L C/2. A growing/shrinking sampling scheme is not yet a tractable contract: its provider, conditioning and prime cost would need new uniform estimates. See [Decision03](../brainstorm/notes/03_RSCT_B01_R3_EVENT_BACKGROUND_DECISION_20261111.md) and the [continuation](01_RSCT_CONTINUATION_AND_PROMPT_20261111.md).
