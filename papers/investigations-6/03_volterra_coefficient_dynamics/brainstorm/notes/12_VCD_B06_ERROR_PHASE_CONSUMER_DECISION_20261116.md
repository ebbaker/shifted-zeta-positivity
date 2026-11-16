# B06 — retain the phase of the complete E15 error

16 November2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Lead actual model/effort unavailable. Fixed proof/assessment helpers explicitly dispatched gpt-6.1-sol/ultra, without separate backend attestation. Chat0003 third research turn.

**Conceptual selection and proposed quantitative claims, not a zero theorem.** Read the [result index](../../../../../result-summaries/README.md), [cluster18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [avoid index](../../../../../avoid/README.md), [classification01](../../../../../avoid/01_restating_the_target.md), [controls02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [separate bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [control catalog12](../../../../../result-summaries/12_collision_controls_and_screening.md). B05's actual-source exclusions remain unchanged.

## Two candidates and selection

1. **Complete quadrature-error phase, selected.** Specialize exact E15 transport to the physical tail k_N and ell=0, so its left side is F-G_N with G_N=e0^T exp(izJ_N)e0. Instead of separately bounding the three convolution factors, represent the entire signed error by the classical confluent interpolation remainder. The proposed factor is F-G_N=L_N E_N, with L_N=(-1)^N h_N^* z^(2N)/(2N)!, h_N^*=product beta_j, and E_N the characteristic function of an explicit symmetric error probability law. Its variance and fourth moment should shrink like log²N/N and log⁴N/N². The complete-source cosh moment in E01 should then control its complex phase uniformly in the critical strip. This is a quantitative phase estimate for the actual aggregate error, not just a change of its coordinates.
2. **Coercivity along a kernel homotopy, deferred.** For k_tau=ell+tau(k-ell), E15 differentiates to a signed formula for d_tau|f_tau|². An integrable lower logarithmic-derivative bound would prevent a zero. Without an independently acquired bound it simply shifts nonvanishing into an unknown homotopy response and can fail even if the endpoints are nonzero. No such canonical bound is available here, so do not issue an identity-only task or present this as progress.

A first-order kernel correction with an absolute quadratic remainder was also considered as a way to implement candidate1, but computing a richer finite closure already supplies the whole modeled difference. Merely truncating that known difference adds an error. The chosen route instead estimates the phase of the exact physical aggregate remainder. This is implementation screening, not a third live candidate or a universal exclusion.

## Exact law to prove in E21

Work at lambda=0 with the unchanged complete Phi and literal F. Let mu=Phi/Z, P_N monic, h_N^*=integral P_N²dmu, and nu_N=P_N²mu/h_N^*. Let x_1,...,x_N be the simple real eigenvalues of J_N; they are the Gauss nodes. Independently take U~nu_N and uniform barycentric weights S on the simplex with2N+1 coordinates. Form X_N=S_0 U+sum_j(S_(j,1)+S_(j,2))x_j. Then E_N(z)=E exp(izX_N) is the proposed complete error factor. Repeated knots each have multiplicity2; S_0 has parameter1 and the grouped node weights parameter2. The source is not replaced by this auxiliary law.

Writing M=2N+1, m2=beta_N+beta_(N+1), m4=beta_N beta_(N-1)+(beta_N+beta_(N+1))²+beta_(N+1)beta_(N+2), S2=tr(J_N²), S4=tr(J_N⁴), the proposed exact moments are
EX_N²=2(m2+S2)/[M(M+1)],
EX_N⁴=[24m4+24m2 S2+12S2²+12S4]/[M(M+1)(M+2)(M+3)].
Verify N=1 and all normalization/sign/domain issues. Tie the law to the literal E15 transport by equality of their exact left sides; do not claim a new source or a general arbitrary-kernel identity.

## Quantitative phase estimate to prove in E22

E01 proves the stronger inherited input E_(nu_N)cosh(4U)<=2N+12, not merely the coefficient envelope B_j=arcosh²(2j+12)/16. Thus for0<=t<=4, E exp(tU)=E cosh(tU)<=(2N+12)^(t/4), using symmetry and log-convexity/Holder.

Separate X_N=S_0 U+(1-S_0)V_N, S_0~Beta(1,2N), with independent V_N the Dirichlet(2,...,2) average of the Gauss nodes. For t L/(2N)<1, where L bounds max|x_j|, the paired node symmetry should give
E exp(t V_N) <= product_j(1-t x_j/(2N))^(-2)
<=exp{t² S2/[4N²(1-t² L²/(4N²))]}.
Derive the first inequality from simplex moments and nonnegative even coefficients; do not apply an invalid reciprocal-moment series to the unbounded U. Convexity after the Beta split, rather than multiplying separate large norms, should yield for0<=Y<=1
E exp(2Y X_N)<=C_N(Y):=(2N+12)^(Y/2)/(2N+1)+[2N/(2N+1)]exp{Y² S2/[N²(1-Y² L²/N²)]}.
For N=1, the node contribution is exactly1 and L=S2=0. For N>=2 use the deterministic Lbar=arcosh(2N+8)/2, which should satisfy Lbar<N, and S2bar=2(N-1)B_(N-2). Prove the denominator positive. C_N remains bounded and tends to1 for fixedY<=1.

Symmetry and Taylor's integral remainder give
|E_N(z)-1|<=|z|²/2 * sqrt(2 C_N(Y) EX_N⁴), |Im z|<=Y<=1.
Use m2<=B_N, m4<=3B_(N+1)², S2<=S2bar, S4<=Lbar² S2bar to make this fully explicit in N,Y. Aim for O_Y(|z|² log²(N+1)/N), uniformly even when Re z grows. Thus the relative error factor tends to1 on |z|=o(sqrtN/logN), within that strip. Any corrected constants/domain must be reported, not hidden.

## Signed consumer and remaining margin

Let C_N(z)=G_N(z)+L_N(z); use a distinct letter from the exponential allowance in the proof to avoid collision. The paid disk is |F-C_N|<=|L_N| epsilon_N. Pointwise |C_N|>|L_N|epsilon_N excludes a zero; on a closed contour it transfers zero count by the already-checked Rouche theorem. Equivalently for z!=0, any F zero must satisfy |G_N/L_N+1|<=epsilon_N. This retains the known phase of the leading error, unlike |F-G_N|<=|L_N|(1+epsilon_N). It permits finite approximants to have nonreal zeros. The consumer uses finite coefficients, an explicit degree-only budget and a modeled modulus, not the unknown phase of F.

For real x, E_N(x)>=1-x² EX_N²/2. On its explicit positive range, F-G_N has sign(-1)^N for x!=0. Consecutive even/odd quadratures can therefore bracket F on the common range. This gives a signed test at modeled real sample points; no unperformed numerical scan is authorized, no global real-zero statement follows.

A contour margin or a controlled zero geometry for C_N remains unpaid. The new theorem is judged by its explicit phase budget and range, not by restating existence of a successful contour. The law is generic for Gauss quadrature, and the quantitative envelope/cosh input also holds for the weighted-square controls discussed in E01; hence a further canonical margin is essential. Nonreal-zero controls must not be said to fail the phase estimate if they share its premises. Full score/arithmetic still fail in those controls, but that distinction is not consumed by this selected estimate. Other catalog families keep E01's exact pass/fail/untested scope. E07 nonreal zeros and smooth E10/E12 properties must remain separate.

Freeze E21 for the exact error law/moments and E22 for its quantitative phase/consumer. They may run in parallel: E22 treats the explicitly stated law as its object and makes the F identification conditional until E21's final proof is pinned in an addendum. A separate E23 assessment follows both completed returns. No manuscript revision, coefficient acquisition or numerical campaign.
