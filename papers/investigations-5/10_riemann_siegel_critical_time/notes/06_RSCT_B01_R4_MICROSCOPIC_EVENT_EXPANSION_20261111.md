# RSCT-B01 r4: microscopic event expansion and the complete population cost

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0002. Actual backend model and reasoning effort are unavailable in the recorded configuration (`model_configurations: []`); recommendations are not provenance.

**Status: proved in-note from named inherited approximation inputs; same-assistant checking only.** This bounded pass pays the complete field at distance β/log(a/(4π)) from the real axis, including analytic errors after subtracting the event's value and derivative. It also computes the asymptotic size of the specified termwise absolute allowance. That allowance grows despite event subtraction. **This is a lower bound on an upper allowance, not on the actual signed field or its error.** No canonical event is excluded, no finite onset is instantiated and no E01 execution packet is issued.

Read the [result index](../../../../result-summaries/README.md), [cluster11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [controls12](../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../avoid/README.md), specifically [classification01](../../../../avoid/01_restating_the_target.md), [premises02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [separate bounds12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). [Decision04](../brainstorm/notes/04_RSCT_B01_R4_MICROSCOPIC_DECISION_20261111.md) records the bounded return.

## 1. One changed geometry, one inherited consumer

Keep the canonical theta source, H_0(z)=ξ((1+iz)/2)/8 and H_T=-H_zz. Set
\[
 L=\log(a/(4\pi)),\quad T=c/L,\quad 1/2\le c\le1,
 \quad z=a+w/L,\quad N=\lfloor e^{L/2}\rfloor.                 \tag{1}
\]
Here a tends to infinity; c is in the stated compact interval. Time and N are fixed in every spatial differentiation. The eventual objective still includes every 0<T≤1/2, a>0 and multiplicity m≥2. No premise locates a hypothetical positive threshold in this band.

R3's fixed-height matrix test is stopped. Its formula m≤L/(4∑1/b_j)+O(1) is **not** substituted at b_j=β_j/L: that error and its floors were proved only for fixed geometry. We instead use the complete value approximation directly and test the already defined denominator-free Poisson consumer of [Note03 §§3–4](03_RSCT_B01_REFLECTED_POISSON_TEST_20261111.md). There is no growing matrix or unproved conditioning estimate in this pass.

Classification: the all-domain existence of a favorable Poisson value is the previously stated endpoint reformulation, not new progress. The present numerical quantities are an O(a^(-3/4)) local acquisition error and the coefficient/exponent of the **allowance** in (8)–(10). Event subtraction alone is an identity. The all-real hypothesis is used only for the consumer, not to manufacture an arithmetic floor.

## 2. Complete two-arm approximation on a microscopic disk

Use [HDA Ansatz Note04 CS3/CS6](../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md) and its [Assessment03](../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md), at their inherited internal evidence level. The exact reflected heat representation remains [Polymath v2 §4 (35)–(39)](https://arxiv.org/html/1904.12438v2#S4). This is not a fresh independent proof of HDA, nor an extension of Polymath Theorem 1.3's derivative domain.

Use A, Θ, w_n and the exact-gamma correction R_N from [GNP-RS E01 E2, E9–E11](../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/03_GNP_RS_E01_UNIFORM_OUTER_BASELINE_PROOF_20261111.md):
\[
 A(T,z)=\frac{\pi^{1/4}}{16}z^{7/4}
 e^{-\pi z/8+T(L(z)^2-\pi^2/4)/16},\quad L(z)=\Log(z/(4\pi)),
\]
\[
 \Theta(T,z)=\frac z4(L(z)-1)+\frac{\pi T L(z)}{16}+\frac{7\pi}8,
 \quad \nu(z)=z/2+\pi T/8,
\]
\[
 F_N(T,z)=A(T,z)\sum_{n\le N}w_n(T,z)\cos(\Theta(T,z)-\nu(z)\log n)
                  +e^{-\pi^2T/64}R_N(z),
\quad w_n=n^{-1/2}e^{T[(\log n)^2-L(z)\log n]/4}.             \tag{2}
\]
The normalization A is holomorphic and nonzero on the local chart, with the branch continued from positive a. It is not the full field or a real-axis arm floor. Both reflected populations are retained by the cosine. R_N retains G=[M(s_+)M(s_-)]^(1/2), the fractional-cutoff correction and its removable apparent poles, exactly as in the cited input; none is dropped.

Fix any R>1 independently of a,c and work first on |w|≤2R. For L≥2R this maps into the already declared fixed target r=1,b=9. Retain its enlarged source buffers and full Gaussian exterior from GNP-RS §3.1; no new shrinking source domain is assumed. Since Im Θ(a+w/L)=Im(w)/4+O_R(1/(aL²)), the ratio (|C_+|+|C_-|)/|A| is bounded by a constant depending only on R. Thus CS6 gives a holomorphic normalized error bounded by C_R a^(-3/4). Cauchy on the larger disk supplies its w-derivatives on |w|≤R. This differentiates a holomorphic error, not a real-line bound or the moving floor.

Define real frozen data
\[
 d_n=n^{-1/2}\exp\{c[(\log n)^2-L\log n]/(4L)\},\quad
 \lambda_n=\frac14-\frac{\log n}{2L}\in[0,1/4],
 \quad\phi_n=\Theta(T,a)-(a/2+\pi T/8)\log n,
\]
\[
 P_a(w)=\sum_{n\le N}d_n\cos(\phi_n+\lambda_n w),\quad
 K_a(w)=\frac{e^{-\pi^2T/64}R_N(a+w/L)}{A(T,a+w/L)},\quad
 q_a=P_a+K_a,\quad f_a(w)=\frac{H_T(a+w/L)}{A(T,a+w/L)}.     \tag{3}
\]
The heat phase πT log n/8 and the quadratic heat weight are frozen at their actual values, not removed. On the larger disk, uniformly in n≤N,
\[
 w_n(T,a+w/L)/d_n=1+O_R((aL)^{-1}),\qquad
 \Theta(T,a+w/L)-\nu(a+w/L)\log n
       =\phi_n+\lambda_n w+O_R((aL^2)^{-1}).
\]
Indeed L(z)-L=O_R(1/(aL)), Θ_z=L(z)/4+πT/(16z), and Θ_zz=O(1/a). The population bound ∑d_n=O(e^{δL}), δ=1/4-c/16≤7/32, proved in §4, pays the *sum* of freezing errors by O_R(a^(-25/32)/L), hence by O_R(a^(-3/4)) after a finite onset. Cauchy also pays these holomorphic freezing errors. Consequently
\[
 \boxed{\sup_{|w|\le R}|\partial_w^j(f_a-q_a)|\le C_R a^{-3/4},
                     \qquad j=0,1,2.}                    \tag{4}
\]
Constants and onset remain finite and uninstantiated. The correction is retained even though the same provider and Cauchy give
\[
 |\partial_w^jK_a|\le C_R a^{-1/4}e^{-cL/16},\quad j\le2. \tag{5}
\]
For (5), R_N/A(0,z)=O_R(a^(-1/4)) and e^(-π²T/64)A(0,z)/A(T,z)=e^(-T L(z)²/16). All bounds are uniform in fractional-cutoff position.

## 3. Use the local event equations before estimating

Assume a real event of multiplicity m≥2 at a. Then f_a(0)=f_a'(0)=0 because A is nonzero; primes now denote w-derivatives. Define
\[
 S_a(w)=q_a(w)-q_a(0)-wq_a'(0).
\]
Taylor's integral remainder applied to the analytic error in (4) gives
\[
 f_a(w)=S_a(w)+r_a(w),\quad
 |r_a(w)|\le C_R a^{-3/4}|w|^2,\quad
 |r_a'(w)|\le C_R a^{-3/4}|w|,\qquad |w|\le R.           \tag{6}
\]
This also proves q_a(0),q_a'(0)=O(a^(-3/4)) under the event. Formula (6) uses just two necessary equations, valid for every m≥2; it does not assume m=2 or impose the remaining m−2 equations. It explicitly retains the complete signed combination
\[
 S_a(w)=\sum_{n\le N}d_n
 [\cos(\phi_n+\lambda_nw)-\cos\phi_n+\lambda_nw\sin\phi_n]
 +K_a(w)-K_a(0)-wK_a'(0).                                \tag{7}
\]
The physical derivatives are H_z/A=(A_z/A)f_a+L f_a'. No nonzero lower bound for f_a, S_a or the event curvature has been inferred.

## 4. Exact asymptotic of the specified absolute allowance

Prior-work boundary: the [collision manuscript](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex), labels `prop:absmass` and `sc:derivativemass`, already proves the same exponential terminal-block scale and its first-derivative penalty, on compact subsets of 0<c<4. [S04 Note01](../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md) already pays a phase-retaining local first jet; [S04 Note03](../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/03_UNIFORM_LOCAL_RESIDUAL_TRANSFER_AND_CUTOFF_PAYMENT_OBSTRUCTION_20261019.md) distinguishes accurate local residuals from a positive anchor. Neither the scale nor microscopic RS approximation is claimed as a new general discovery. Here the extension is the full fixed-k coefficient, the two-event-equation subtraction, and its specific Poisson consumer payment in the present band and normalization.

For each **fixed** nonnegative integer k put M_k=∑_{n≤N}d_n λ_n^k. Uniformly in 1/2≤c≤1,
\[
 \boxed{M_k=\frac{2k!}{L^k}e^{(1/4-c/16)L}
                    (1+O_k(L^{-1})).}                  \tag{8}
\]
Here λ_n^0=1 including a possible zero λ_N. This statement concerns positive coefficient moments, not an oscillatory sum.

Proof: the summand extended to 1≤x≤e^(L/2) is nonnegative and decreasing: d(log d(x))/d(log x)=−1/2−c/4+c log(x)/(2L)≤−1/2, and λ(x) decreases. Integral comparison including the final fractional interval gives a sum/integral discrepancy O_k(1). Substitute v=L/2−log x into the integral to obtain exactly
\[
 \frac{e^{\delta L}}{(2L)^k}
   \int_0^{L/2}v^k e^{-v/2+cv^2/(4L)}\,dv.
\]
On this interval −v/2+cv²/(4L)≤−3v/8. The difference from e^(-v/2) is at most v² e^(-3v/8)/(4L). Integration gives O_k(1/L), and extending the limiting integral to infinity has exponentially small cost. Its value is 2^(k+1)k!, by elementary repeated integration by parts. The O_k(1) discretization error is smaller than the stated relative error, uniformly since δ≥3/16. This proves (8).

At w=iβ, fixed β>0, the single bracket in (7) equals
\[
 \cos\phi_n[\cosh(\beta\lambda_n)-1]
 +i\sin\phi_n[\beta\lambda_n-\sinh(\beta\lambda_n)].
\]
Its maximum modulus over a free real phase is cosh(βλ_n)−1: for x≥0, cosh x−1≥sinh x−x≥0. Thus the termwise phase-insensitive allowance is exactly
\[
 U_\beta:=\sum_{n\le N}d_n[\cosh(\beta\lambda_n)-1]
 =\frac{2\beta^2}{L^2}e^{\delta L}(1+O_\beta(L^{-1})).      \tag{9}
\]
Similarly the derivative allowance is
\[
 V_\beta:=\sum_{n\le N}d_n\lambda_n\sinh(\beta\lambda_n)
 =\frac{4\beta}{L^2}e^{\delta L}(1+O_\beta(L^{-1})).        \tag{10}
\]
To check the remainders, use bounded βλ_n≤β/4 and the Taylor remainder bounds O_β(λ_n^4); (8) gives M_4/M_2=O(L^(-2)). Both (9) and (10) diverge uniformly in c. Subtracting two event jets saves L² relative to M_0 but leaves the full near-cutoff population.

These are the actual sizes of the *specified allowances*. The canonical φ_n are correlated and are not freely variable. The termwise maximizers need not satisfy q_a(0),q_a'(0)≈0 or any canonical event. No lower bound on |S_a|, a signed quadratic form or any actual approximation error follows. The calculation stops the estimate that discards the remaining phase relations and seeks a bounded residual using these allowances alone. It does not exclude a better bound using those relations, a regrouping of modes, or more event information. Nor is (8) uniform when k grows with L.

## 5. Complete Poisson acquisition: small error, unpaid sign

Take y=β/L, z=a+iy, k_a=1+y²/(4a²+y²) and
\[
 d_a=2k_a+\frac\beta L\Im\frac{A_z(T,z)}{A(T,z)},\qquad
 \mathcal D_a(g)=d_a|g(i\beta)|^2+
                    \beta\Im[g'(i\beta)\overline{g(i\beta)}].       \tag{11}
\]
This is precisely Note03's B/|A|² when g=f_a, not a new exclusion criterion. The real carrier drift has not been omitted:
\[
 A_z/A=7/(4z)-\pi/8+T L(z)/(8z),\qquad
 d_a=2k_a+O_\beta(a^{-2}L^{-2}).
\]
At an all-real event of arbitrary m≥2, the exact paired product gives
\[
 -y\Im(H_T'/H_T)=m k_a+y^2\sum_{r\ne\pm a}\frac1{(a-r)^2+y^2},
\quad
 \mathcal D_a(f_a)=[(2-m)k_a-y^2\sum_{r\ne\pm a}
       ((a-r)^2+y^2)^{-1}]|f_a(i\beta)|^2<0.               \tag{12}
\]
All copies at both a and −a are removed from that sum. Other multiple zeros remain. Strictness uses the canonical remaining zero population and all-realness; (4)–(10) do not need these assumptions.

For |f_a−S_a|≤ε_0 and |f_a'−S_a'|≤ε_1 at iβ, direct expansion pays
\[
 |\mathcal D_a(f_a)-\mathcal D_a(S_a)|\le
 |d_a|(2|S_a|\epsilon_0+\epsilon_0^2)
 +\beta(|S_a'|\epsilon_0+|S_a|\epsilon_1+\epsilon_0\epsilon_1).
                                                               \tag{13}
\]
By (5), (6), (9), (10), this is
\[
 O_\beta\left(a^{-3/4}e^{\delta L}/L^2+a^{-3/2}\right)=o(1),       \tag{14}
\]
uniformly in c. In particular its slowest power is a^(-17/32)/L². This is an **absolute normalized error**; it is not relative accuracy near a multiple zero or a certified positive margin. No quotient or matrix inversion has been formed.

The first unpaid premise is the **sign and useful margin of the actual correlated expression** D_a(S_a), under the canonical phases and the two event equations. The positive value term and the signed derivative cross term cannot be ordered by (9)–(10). Their triangle estimates supply no positive lower margin. Better approximation accuracy alone does not supply that arithmetic sign. We stop here rather than relabel the required sign as an executable proof method.

The r3 shortcut cannot be imported: at y=β/L the formal ordinary-zeta argument has real part (1+y)/2+c/4→1/2+c/4<1, outside the absolutely convergent series/Euler product used there ([DLMF 25.2.1, 25.2.6, 25.2.11](https://dlmf.nist.gov/25.2)). Also |C_+/C_-|=exp(−2 Im Θ)→e^(−β/2), not zero. These are failed premises of that shortcut, not a theorem forbidding every zeta comparison in this strip. Even a small fixed carrier ratio would not pay the growing reflected population by itself.

## 6. Analytical controls, ownership and return

Apply [controls12](../../../../result-summaries/12_collision_controls_and_screening.md) on actual witness domains, without rerunning numerical certificates. The [BW-01 positive three-atom family](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md), with q=1/2 and frequency ℓ=2π/3 as in r2/r3, has H(T,z)=(4/9)(cos(ℓz)+1/2)² and genuine all-real double events at a_j=1+3j. Choose each source member's T=c/log(a_j/(4π)). At y=β/L_j it satisfies both event equations, the exact subtraction identity and the negative sign (12). Thus those geometric premises do not force the opposing sign even at microscopic distance. It fails canonical theta coefficients/completion, full profile and eventual simplicity at threshold. It is **not** assigned (3), (8) or the canonical error estimates.

| Control class | Screen / premise failed |
| --- | --- |
| Polynomial heat event of Note03 | Both event equations and all-realness hold; with only the pair ±a its B is zero. Complete theta source and infinite population fail. |
| Euler-factor / translated | Unchanged canonical coefficients and the approximation (3) fail. A nonreal witness time is not automatically an all-real threshold event. |
| Weighted-square, finite-tail, finite-prime orbit | Complete coefficients and/or full reflection fail; local events do not supply all-realness, and finite-tail controls have no all-real time. |
| Reflected super-Gaussian, smooth shape, positive primitive | Canonical square-series arithmetic fails; the recorded local collision alone supplies no all-real slice for (12). |
| Finite-profile atomic and continuous compact-source thresholds | Event subtraction remains valid; exact theta coefficients, full growth and eventual threshold simplicity fail. |
| RH-conditional endpoint | Conditional time-zero construction, failed ordinary Dirichlet arithmetic; no unconditional positive-time theta inference. |
| Variable readout and heat counter-kernels | Literal cosine readout, source and/or physical heat generator fail. |
| Relaxed profile/zero populations | Exact canonical integer zero population and full simultaneous field identification fail; not physical events. |

[HCB's register](../../03_heat_flow_collision_bounds/research-progress/02_POST_CALIBRATION_RESEARCH_PROGRESS_20261028.md) retains general first-jet/Poisson acquisition. This is a local complete-provider acquisition and a specified allowance calculation, not an unconditioned first-jet floor opening a duplicate HCB task. [BW-10 Note04](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/04_ZERO_DEFLATION_AND_RATIONAL_RESOLUTION_20261020.md) owns prior rational-resolution/absolute-prime-cost work; no time-zero RH assumption is imported. HDA/GNP-RS retains provider ownership. [OA's restart gate](../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md) stays parked.

**Return:** r4 complete with a paid microscopic event expansion, an absolute o(1) consumer error, and a scoped failure of termwise absolute residual control. No new zero-exclusion region, independent provider audit, finite onset, numerical research, agents or manuscript. The remaining choice is conceptual: acquire a signed correlation using the actual phases and event information, or select a materially different mechanism. A fixed-k extension of (8), smaller error constants, or simply requesting positivity of (11) does not settle that choice. See the [continuation/model-change note](01_RSCT_CONTINUATION_AND_PROMPT_20261111.md).
