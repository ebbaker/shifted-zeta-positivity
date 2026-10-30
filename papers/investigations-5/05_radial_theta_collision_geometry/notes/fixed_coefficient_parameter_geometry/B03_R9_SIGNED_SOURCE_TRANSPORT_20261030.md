# B03 R9: a uniform signed-source margin across a simple-zero curve

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded **gpt-6.1-sol / ultra**, Investigation05 **chat0051**, *Assess R8 and signed-source work*, thread `01a18e61-b771-7d81-9290-9dad3cc07d78`. Parent authors the proof/certificate with two read-only same-Sol checks. This is internal work with inherited source premises, not specialist or formal independence. [Progress06](../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md) owns live status.

**Result.** For the complete physical unit theta source and literal cosine, on the fixed rectangle
\[
 Q=\{(T,A): |T-1/4|\le1/128,\quad64\le A\le66\},
\]
we obtain, uniformly,
\[
 H_A<-2.4\,10^{-10},\qquad
 D(T,A):=H_A^2-2HH_{AA}>7.4\,10^{-20}.                 \tag{1}
\]
At every time in this interval, \(H(T,64)>6.4\,10^{-10}\) and \(H(T,66)<-6.2\,10^{-11}\). There is consequently exactly one simple zero in this frequency interval, forming a real analytic zero curve. Unlike the earlier isolated scalar-positive pilot, Q actually crosses a simple zero.

At **every center in Q**, the unchanged C04 direct coefficient with **degree one and radius rho=1/16384** satisfies
\[
 d_1>6.6\,10^{-20},\qquad
 c_1=\frac{d_1}{1+h_0^2+h_1^2+b^2}>6.6\,10^{-20}.     \tag{2}
\]
The finite signed coefficient sum, independent time payment and complete tail are all paid. The same input gives a matched direct derivative floor **above 2.3e-10 on every such local ball**, so this is not a joint-information or spatial-flow advantage. It is a finite uniform signed-source bound derived from saved complete source data, not a general theta sign mechanism, an RH criterion or global coverage.

## 1. Fixed inputs and the bounded question

This pass follows the [accepted R8 assessment](../../reviews/fixed_coefficient_parameter_geometry/E02_R8_GAUSSIAN_SLACK_ASSESSMENT_20261030.md). The author explicitly requested substantive signed-source work after that assessment. Before the root certificate was evaluated, the domain Q, weighted source order 17, and consumer radius 1/16384 were recorded in Progress06. There is no center, radius or degree sweep, no root finder and no fresh quadrature. An auxiliary diagnostic initially required all four transport errors to be below 1e-12; e3 is 1.00263832004e-12. Only that reporting cap was corrected to 1.1e-12. All actual errors already entered the successful mathematical inequalities; no source, formula or parameter was changed.

Use the complete 384-bit stage of the [E01 R2 record](../../numerics/fixed_coefficient_parameter_geometry/fcg_e01_r2_adaptive_ibp_20261030.json), whose SHA-256 is
`557c57e420534e4db949e3d019d5d40077a1df8f055f6634bd2f657c4f87392c`.
It supplies h0 through h17 at (tau,a)=(1/4,64), the complete positive M4 at (T,Y)=(17/64,1/64), and the single complete X1 at (17/64,4). The signed h enclosures are read from exact binary midpoint/radius pairs. Displayed source-tail bounds are parsed as rational enclosing intervals, including their displayed radii. No two-precision reacquisition is claimed: this new certificate consumes one inherited complete stage. Its source definitions, guards and implementation retain their prior assessment.

This is a finite sufficient estimate in the sense of [avoid01](../../../../../avoid/01_restating_the_target.md). The numerical question can fail: are the error-paid signed Bernstein coefficients positive, and do they exceed all three independent C04 costs? A positive regional minimum is never assumed or defined into a constant. The calculation answers both questions on Q.

## 2. Weighted signed Taylor transport with a complete remainder

Write t=T−tau, x=A−64, s=1/128 and f_tau=exp(tau u²)Phi. For j=0,1,2,3 define
\[
 P_j(t,x)=\sum_{2m+\ell\le17-j}
 \frac{(-1)^m h_{j+2m+\ell}}{m!\ell!}t^m x^\ell.        \tag{3}
\]
Expanding the full integral for the jth frequency derivative proves (3): a time derivative inserts u², while two frequency derivatives insert −u². In particular
\(\partial_xP_0=P_1\), \(\partial_xP_1=P_2\), and \(\partial_tP_0=-P_2\). These follow exactly from the weighted cutoff; no division by a physical field occurs.

Split the **complete all-mode source** at u=1. On [0,1], every omitted monomial has source power j+2m+ell>=18 and therefore u^(j+2m+ell)<=u⁴. Absolute convergence of the exponential expansion and the complete theta decay justify integration term by term. Thus
\[
 |H^{(j)}-P_j|_{\text{core}}\le M_4 S_j,\quad
 S_j=\sum_{2m+\ell>17-j}\frac{s^m2^\ell}{m!\ell!}.       \tag{4}
\]
The saved M4 at (17/64,1/64) dominates the needed integral of u⁴ f_tau on [0,1]. Its full source contains all modes; the core is not restricted to the first eight.

Here is an entirely rational evaluated upper bound for S_j. Let
\[
 a_m=s^m/m!,\ b_\ell=2^\ell/\ell!,\quad
 A=\sum_{m=0}^{32}a_m,\ B=\sum_{\ell=0}^{64}b_\ell,
\]
\[
 a_*={s^{33}\over33!}(1-s/34)^{-1},\quad
 b_*={2^{65}\over65!}(1-2/66)^{-1}.
\]
Decreasing factorial ratios give
\[
 S_j\le\sum_{\substack{m\le32,\ell\le64\\2m+\ell>17-j}}
 a_mb_\ell+a_*(B+b_*)+Ab_*.                           \tag{5}
\]
The final terms cover the complement of that finite index rectangle, including its corner; no infinite-index remainder is omitted.

For each saved jet k let E_k be its `source_upper + mode_upper`, with both taken at their rational upper endpoints. The first term pays the retained eight modes beyond u=1; the second pays omitted modes over the whole half-line and hence also beyond u=1. Let E4plus be the corresponding complete exterior payment for the saved M4. Since tau+s<17/64 and j<=3, on u>=1 the actual derivative exterior is bounded by E4plus. The finite polynomial's exterior is bounded term by term using E_(j+2m+ell). Hence the complete error is
\[
 e_j=M_4\overline S_j+E_{4,+}
 +\sum_{2m+\ell\le17-j}{s^m2^\ell\over m!\ell!}E_{j+2m+\ell}.
                                                               \tag{6}
\]
This deliberately overpays omitted-mode exterior contributions; it drops none. Both signs of t are covered. The exact rational record gives
\[
 e_0<1.905\,10^{-15},\quad e_1<1.624\,10^{-14},\quad
 e_2<1.313\,10^{-13},\quad e_3<1.003\,10^{-12}.          \tag{7}
\]

## 3. Retain the signed discriminant before bounding it

Form the polynomial \(D_P=P_1^2-2P_0P_2\) **before** taking interval bounds. Separately bounding the two products would lose the useful gap on this rectangle. Transform t=−s+2sv, x=2w and convert the complete signed polynomials to tensor Bernstein form on [0,1]². If a_jk are power coefficients, the Bernstein coefficient at (i,l) of tensor degree (d,n) is
\[
 B_{i\ell}=\sum_{j\le i,k\le\ell}a_{jk}
 {\binom ij\over\binom dj}{\binom\ell k\over\binom nk}.
                                                               \tag{8}
\]
The Bernstein basis is nonnegative and sums to one. Taking the lowest lower coefficient and highest upper coefficient therefore encloses the polynomial throughout Q. All coefficient formation and conversion use exact rational interval arithmetic. Repeated jet occurrences are enclosed conservatively, not treated as independent measurements. There is no subdivision or sampled sign test.

Convenient outward summaries of the polynomial bounds are:

| Polynomial | Lower | Upper |
| --- | ---: | ---: |
| P0 | −6.484e-11 | 6.425e-10 |
| P1 | −4.217e-10 | −2.410e-10 |
| P2 | −1.274e-11 | 1.328e-10 |
| P3 | −3.098e-13 | 1.732e-10 |
| D_P | 7.4554e-20 | 1.9078e-19 |

D_P has tensor degree (16,32); the four P_j have degrees (8,17), (8,16), (7,15), (7,14). Let C_j be the maximum magnitude of the exact certified P_j range. Pay the full discrepancy
\[
 \epsilon_D=2C_1e_1+e_1^2+
 2(C_0e_2+C_2e_0+e_0e_2).                              \tag{9}
\]
Equations (6)–(9) give **D>7.43719e-20**, implying (1). This is an evaluated lower bound for the actual signed source ingredients, not the name of their unknown difference.

Restricting P0 to x=0 and x=2 and retaining e0 proves the endpoint signs in the return. Equation (7) and the upper Bernstein coefficient of P1 give H_A<−2.4e-10. The intermediate value theorem and strict monotonicity give existence and uniqueness of a zero in (64,66) at every time in the interval. Nonzero H_A and real analyticity give the simple real analytic zero curve. No zero coordinates were acquired or needed.

## 4. Pay the unchanged coefficient at every center

Now recenter at any p in Q, writing h_j=H^(j)(p), b=h2, B=|b|, eta=|h1| and D0=h1²−2bh0. These are the actual center jets, not the P_j values. Define rho=1/16384, N=1 and
\[
 \delta=4-\rho,\quad X_1=\int_0^\infty u e^{(17/64)u^2+4u}\Phi(u)du.
\]
Uniformly p_T+rho<17/64. The general-N complete kernel bound accepted in R8 therefore applies at all these real centers with the same X1. We use its simpler discarded-Gaussian payment at degree one; no new Gaussian value or primitive payment is needed.

The exact signed coefficient algebra gives
\[
 g_{10}=-h_1h_3,\quad g_{01}=0,\quad
 F_1=\rho|h_1h_3|.                                    \tag{10}
\]
For n=2 the direct remainder polynomials are exactly
\[
 p_b=\rho^2(2u^2+3u^3+u^4),\quad
 p_h={\rho^2\over2}(u^3+2u^4+u^5).
\]
Paying each u^k by X1 (k−1)!/delta^(k−1), retaining the positive Gaussian slack as available domination, gives
\[
 \widehat T_1\le X_1\rho^2[B A_b+\eta A_h],\quad
 A_b={2\over\delta}+{6\over\delta^2}+{6\over\delta^3},\quad
 A_h={1\over\delta^2}+{6\over\delta^3}+{12\over\delta^4}. \tag{11}
\]
This pays the full absolute coefficient tail, not only the real function remainder. It works at N=1; the primitive common-X1 degree restriction is irrelevant to this direct calculation.

Use the physical ranges P_j±e_j from (6) to enclose B, eta and |h3| on Q. The exact record gives these safe upper caps for the **three separate costs**:

| Cost | Upper bound |
| --- | ---: |
| independent 2b²rho | 2.155e-24 |
| signed finite sum F1 | 4.484e-24 |
| complete direct tail | 7.663e-21 |

Their subtraction from the signed discriminant lower bound proves **d1>6.67031e-20**, and its exact normalization proves (2). In particular the common-limit margin from R8 satisfies d_infinity>=d1>6.6e-20 uniformly at these centers. The formerly missing signed gap has been supplied on Q only. The exact row and inherited all-time carrier theorem apply to each local ball with its own exact constant c1; this does not change the coefficient definition or supply a global physical-target transfer.

## 5. Matched direct derivative and actual controls

On a local radius-rho ball around any p in Q, the scalar derivative's degree-one polynomial is h1−h3 t+b x. With precisely the same complete source information its tail is bounded by X1 rho² A_h. Hence
\[
 |H_A(p+(t,x))|\ge\inf_Q|h_1|
 -\rho(\sup_Q|h_3|+\sup_Q|b|)-X_1\rho^2 A_h
 >2.33769\,10^{-10}.                                  \tag{12}
\]
This also covers portions of these local balls lying just outside Q. The matched direct strip has the usual at-least-as-strong row information; the simple scalar derivative test already proves separation. No flow-based advantage, minimal successful degree, optimal radius or favorable acquisition complexity is claimed. Q is a genuinely larger certified set containing simple zeros, but it is still a finite positive-time calculation.

The quantitative data used in (1)–(12) are those of complete theta. Generic transport, Bernstein conversion and the row identity can also be applied to controls with their own source moments and exterior bounds. On an event-containing ball an actual control collision forces its correctly computed d1<=0 and its scalar derivative floor to fail. No theta enclosure is assigned to a control.

The [control register](../../../../../result-summaries/12_collision_controls_and_screening.md) gives the distinct failed premises: weighted-square and finite-prime perturbations lack complete unit-coefficient reflection; Euler-factor sources change the complete arithmetic coefficients, and their negative-Laguerre witnesses do not alone locate a collision ball; reflected super-Gaussian, smooth-shape and positive-primitive sources lack complete theta square arithmetic. Atomic/finite-profile cases need their own admissible moments and exterior treatment; changed kernels fail literal cosine/heat reconstruction, conditional endpoint examples keep their RH premise, and relaxed measures are not physical events. The present signed numerical inequalities, rather than generic source positivity or a named identity, exclude an event only on the declared region. This does not prove theta unique among sources passing this finite test.

## 6. Evidence and continuation boundary

The [standalone checker](../../numerics/fixed_coefficient_parameter_geometry/check_fcg_b03_r9_signed_transport.py) and [small exact record](../../numerics/fixed_coefficient_parameter_geometry/fcg_b03_r9_signed_transport_20261030.json) carry input/script hashes, exact rational bounds, complete error payments and the diagnostic correction. The execution took about four seconds locally, with no source calls or quadrature; this is one measured certificate cost, not a complexity law or matched speed claim. Binary signed input enclosures, parsed positive-tail interval endpoints and inherited quadrature/guard correctness remain dependencies. Parent and two same-Sol contributors checked the proof and implementation; a separately issued E02 R9 assessment remains next, not already completed.

Read with the [result index](../../../../../result-summaries/README.md), [theta identities/bookkeeping](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [avoid index](../../../../../avoid/README.md), particularly [shared-premise reviews](../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped conclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [numerics after the question](../../../../../avoid/10_numerics_ahead_of_the_question.md), [signed cancellation](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [noncircular constants](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md). No manuscript, DRAFT_HISTORY, new snapshot or result-index promotion is requested. [The continuation/model handoff](B03_R9_RETURN_AND_MODEL_HANDOFF_20261030.md) records the next bounded assessment and the remaining global gap.
