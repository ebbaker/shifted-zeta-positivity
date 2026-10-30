# E02 R9: assessment of the uniform signed-source transport certificate

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded **gpt-6-astra / max**, existing Investigation05 **chat0050**, thread `01a18e52-fa91-7b61-b31b-b311eee675f8`. This is a different-model internal assessment of the Sol/ultra R9 proof and implementation. The assessor did not author R9, but all checking shares the complete source inputs and inherited analytical premises. It is not specialist, formal or independent source-validation evidence. No subagents or new chat registrations were used.

**Disposition: accept all seven fixed obligations without mathematical correction.** The [issued packet](../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R9_SIGNED_TRANSPORT_ASSESSMENT_20261030.md), [R9 proof](../../notes/fixed_coefficient_parameter_geometry/B03_R9_SIGNED_SOURCE_TRANSPORT_20261030.md) and every frozen input remain unchanged. R9 supplies a finite uniform signed-source margin on
\[
 Q=[1/4-1/128,1/4+1/128]\times[64,66],
\]
including exactly one simple real analytic zero curve. It does not supply a height/time-uniform source estimate, efficient asymptotic cover or RH/Newman transfer.

## Seven-obligation disposition

| Obligation | Disposition and evidence |
| --- | --- |
| 1. Complete weighted transport | **Accept.** The cutoff j+2m+ell≤17 preserves dx P0=P1, dx P1=P2 and dt P0=−P2 exactly. All omitted powers are at least18, so u^k≤u^4 on the complete all-mode core [0,1]. Absolute convergence justifies expansion and integration. The full factorial complement is paid by the two geometric tails, including their corner. The independent checker verifies the three polynomial identities by symbolic jet index and rational coefficient, not by treating interval overlap as identity. |
| 2. Exterior and inputs | **Accept.** Every exterior is retained-mode source_upper plus whole-line omitted-mode mode_upper. The original acquisition implementation was inspected: it integrates modes1..8 on [0,1], adds their exterior and the full omitted-mode tail, and uses symmetric errors for signed jets. On u≥1, j≤3 and T≤33/128 make the saved positive M4 exterior at17/64,1/64 a valid bound for the actual derivative exterior. Its linear weight is extra domination; no frequency-shift exponential is needed on this real domain. All ten frozen hashes match. Binary intervals and displayed tail midpoint/radii are decoded as rationals, retaining their upper radii. One complete384bit stage and one X1 are reused. |
| 3. Signed Bernstein/discriminant | **Accept.** Products are formed before range enclosure. Tensor Bernstein degree(16,32) is correct; the nonnegative partition-of-unity basis proves uniformity without subdivision or sampling. A separately written direct monomial-to-Bernstein conversion combines signed affine weights before interval multiplication. Its ranges lie within the supplied ranges and reproduce the claimed conservative inequalities. The full discrepancy includes both quadratic error terms and all mixed terms. |
| 4. Simple-zero curve | **Accept.** H_A<−2.4e−10 and the opposite endpoint signs hold for every time in the closed time interval. Strict frequency monotonicity and the intermediate value theorem give exactly one zero in (64,66); the implicit function theorem and analyticity give a simple real analytic curve, extending locally through the two time endpoints. No zero coordinate or root search is asserted. |
| 5. Unchanged C04 consumer | **Accept.** At every center of Q, g10=−h1h3 and g01=0, with finite payment rho|h1h3| and separate2b²rho. For rho=1/16384, the direct degree-one polynomials and the two rational moment constants are correct. Uniform centerT+rho<17/64 permits one common X1 even on local balls protruding beyond Q. The complete coefficient tail is paid. The exact normalization retains c1>6.6e−20; no primitive rule is used at N1. |
| 6. Matched comparison/controls | **Accept.** The derivative polynomial is h1−h3t+bx and its complete tail is X1 rho² Ah. It yields |H_A|>2.3e−10 on every local ball, including its parts outside Q. The scalar test alone proves separation with the same inputs, so no joint-information or spatial-flow advantage is claimed. Controls use their own source, complete moment domain and event-containing ball; their actual collisions force failure of the signed margin/derivative floor. |
| 7. Provenance, correction, continuation | **Accept.** The failed e3<1e−12 diagnostic and corrected1.1e−12 report cap are recorded transparently. The actual e3 entered the mathematical costs throughout; no proof/domain/radius/source change resulted. Same-Sol proof-author checks were not E02 R9. This different-model assessment closes the fixed packet, retaining shared premises and the finite/global distinction. Chat0050 remains distinct from R9-author chat0051. |

## Proof and numerical evidence

For an omitted term of H^(j), the real-parameter absolute source factor is
\(u^{j+2m+\ell}|t|^m|x|^\ell/(m!\ell!)\).
On [0,1] its power is at least18 and hence at most u^4. The complete positive M4 pays that whole core. Outside [0,1], the actual H^(j) and the finite polynomial are estimated separately, exactly as R9(6); paying a whole-line omitted-mode tail again is conservative rather than a missing contribution. The actual signed jets already include both source complements.

Let A=sum(a_m), B=sum(b_l), with the issued finite index bounds. The omitted rectangle has upper payment
\((A+a_*)(B+b_*)-AB=a_*B+Ab_*+a_*b_*\).
This independently reconstructs the original expression a_*(B+b_*)+Ab_*. All four resulting rational transport errors agree exactly with the saved record.

For the independent Bernstein conversion, the coefficient of the mth time monomial at time Bernstein index i is computed directly as
\[
 \alpha_{im}=s^m\sum_{k=0}^{\min(i,m)}
 (-1)^{m-k}2^k\binom mk\frac{\binom ik}{\binom dk},
\]
and the corresponding frequency factor is
\(2^\ell\binom j\ell/\binom n\ell\).
These exact rational weights are summed before applying interval coefficients. This differs from the original implementation's sequence of interval affine expansion followed by basis conversion; it avoids importing the original conversion code. Both enclose the same physical polynomial. The separately written arithmetic is still not independent validation of the source intervals.

Writing H^(j)=P_j+r_j with |r_j|≤e_j gives exactly
\[
 |D-D_P|\le2C_1e_1+e_1^2+
 2(C_0e_2+C_2e_0+e_0e_2).
\]
The square and mixed-error terms cannot be dropped. This is an error bound on a signed polynomial whose Bernstein lower endpoint was formed first.

The conservative results from the original certificate remain:

| Quantity | Accepted bound |
| --- | ---: |
| Actual discriminant throughout Q | >7.43719e−20 |
| Uniform degree-one d1 | >6.67031e−20 |
| Exact normalized c1 | >6.6e−20 |
| Independent time cost | <2.155e−24 |
| Finite signed F1 | <4.484e−24 |
| Complete direct tail | <7.663e−21 |
| Local scalar derivative floor | >2.33769e−10 |

The original checker replay reproduced every saved field exactly except its measured runtime, finishing in about3.70seconds. The [separate assessment checker](../../numerics/fixed_coefficient_parameter_geometry/verify_fcg_e02_r9.py) finished in about1.16seconds and passed its symbolic and rational checks; its [exact record](../../numerics/fixed_coefficient_parameter_geometry/fcg_e02_r9_signed_transport_assessment_20261030.json) retains exact endpoints, hashes and provenance. These are local verification costs, not a complexity or matched-speed result. There were **zero new source/quadrature evaluations, no parameter sweep and no root finding**. The initial e3 cap is indeed too small: the exact value lies strictly between1e−12 and1.1e−12.

## Scope and next decision

The quantitative signed inequalities distinguish the present finite theta region; positivity, heat algebra and Bernstein conversion are generic. Weighted-square/finite-prime controls fail full unit-coefficient reflection; Euler-factor controls change the arithmetic, and their negative-Laguerre witnesses do not themselves locate collisions; reflected/smooth/positive-primitive controls lack the complete theta square arithmetic. Atomic/finite-profile controls require their own admissible moments and exteriors; changed kernels fail literal cosine reconstruction; conditional endpoints retain their RH premise. No theta numerical input is transferred to any control. Naming an absent identity is not itself a proof that a generic derived bound discriminates that control.

**E02 R9 is complete.** The finite rectangle already has the required uniform source gap and actual simple-zero crossing; scanning adjacent centers is not needed to finish that result. The author's request for further appropriate work permits a bounded analytical follow-through: first extract a common fixed-flow consequence from these accepted bounds, then test the explicitly fixed R9 transport payment's ability to widen its interval without new source information. This does not start a source acquisition or a global coverage claim. B04's global height/time and target-transfer obligations remain open.

Follow [Progress06](../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md), the [result index](../../../../../result-summaries/README.md), [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../../avoid/README.md), especially [shared-premise checking](../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped conclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [numerical questions](../../../../../avoid/10_numerics_ahead_of_the_question.md) and [complete signed payments](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
