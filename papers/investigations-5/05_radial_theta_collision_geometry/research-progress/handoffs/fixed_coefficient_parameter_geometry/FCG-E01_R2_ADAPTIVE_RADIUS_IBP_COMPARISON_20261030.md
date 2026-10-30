# Frozen execution request: FCG-E01 R2 adaptive-radius and IBP comparison

Issued 30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Issuing model **gpt-6-astra**, actual effort **max**, existing Investigation05 **chat0048**.

| Field | Bounded contract |
| --- | --- |
| Task / parent | **FCG-E01 R2**, execute **FCG-B03 R5 / C04 R3** |
| Type / model | **E — execution; Sol**, because formulas, source, finite cases, arithmetic route and completion tests are specified |
| Question | Do a separate outer analytic radius and the phase-aligned IBP envelope lower the paid remainder or the minimum passing degree on the fixed radii? What degree-one radius does the explicit rule certify? |
| Fixed center / outer radius | \(\tau=1/4,a=64,R=1/32\); no source value or root bracket selected this dyadic center |
| Fixed inner radii / degrees | \(r=1/64,1/128,1/256\); \(N=1,2,4,8\); evaluate the complete finite comparison, not just the first positive cell |
| Source boundaries | \(U_3=41\pi/128\), \(U_4=21\pi/64\), frozen at the center, not functions of the varying physical parameter |
| Physical setting | Complete theta source and literal cosine; original drift, unit preparation, full spatial domain |
| Evidence | Outward complete-source enclosures at 256 and 384 bits; exact algebra checks; all mode, source, parameter and any spatial tails paid |
| Live register | [Progress06][progress] only; ready/unstarted at issue |
| Stop | One fixed comparison and derived-radius return, within the limits below; no added center, zero search, arbitrary radius tuning or degree beyond eight |

## 1. Proof and implementation checks before relying on the formulas

Inspect [Note26][proof] and [self-assessment09][self]. Check its complex-parameter IBP endpoint signs, \(a-R\) denominator, phase envelopes (9), boundary payment (11), Cauchy sum (14), exact coefficient, degree/radius monotonicity and degree-one radius (19). The complete primitive remainder identity (20)–(22) is part of the conceptual record; check its lower endpoint cancellation algebraically, but do not implement a competing primitive quadrature route in this request.

Routine algebra corrections preserving the scientific contract are E work and must be recorded separately; an unresolved mathematical premise or a new envelope/reference returns to B03. This execution self-check is not a separate accepted E02 assessment.

## 2. Shared complete inputs

Reuse the existing real-source implementation as a precedent, not as unexamined complete data. Acquire the signed center jets \(h_0,\ldots,h_{17}\) at \((1/4,64)\), with modes \(1,\ldots,8\) on \([0,1]\) and complete complementary tails from Note16 and Note26(26)–(27). These cover every degree in the request. Keep the exact cancellations in \(q_{00},q_{01},q_{02},q_{10}\) and \(g_{00},g_{01}\); use the full signed jet products before absolute values.

Acquire positive moments \(M_3(\rho),M_4(\rho)\) at \(\rho\in\{1/32,1/64,1/128\}\), where the source weight is \(e^{(\tau+\rho)u^2+\rho u}\). The \(\rho=1/32\) pair also supplies the fixed-outer-radius baseline. No theta root, stationary limit or assumed positive minimum enters any input.

For the IBP envelopes use exactly Note26(4), with
\[
 D_j=e^{\tau u^2}
   \{j u^{j-1}\Phi+2\tau u^{j+1}\Phi+u^j\Phi'\},\quad j=3,4.
\]
Form this full signed derivative inside the core before its absolute value. Evaluate both its whole-line IBP bound \(I_j\) and phase-window bound \(W_j\), retaining the boundary value, complex phase variation, and exterior. Then enclose \(\mathcal U_j=\min(M_j,I_j,W_j)\). Save each constituent separately, including which strict comparisons the intervals establish.

## 3. Fixed acquisition route and complete errors

Use 256-bit arithmetic with analytic-integral absolute tolerance \(2^{-180}\), relative tolerance \(2^{-140}\); confirm at 384 bits with \(2^{-280}\), \(2^{-240}\). Per analytic integral retain the existing limits of 200000 evaluations and depth 30. Source truncation is always eight modes; increasing it is not part of this packet. Check every tail guard outwardly.

For the positive but nonanalytic core expressions containing \(|D_j|,|\sin|,|\cos|\), **do not pass them to an analytic Acb integrator**. Use 1024 equal real interval panels in the coordinate \(u=U_jv\), \(0\le v\le1\), at each precision. Enclose the full range on each panel and multiply by its width to obtain lower/upper Riemann sums. Enclose the Jacobian \(U_j\), exponential, trigonometric and absolute-value operations outwardly. Arbitrary fixed-panel coarse lower bounds may be clipped to zero for nonnegative integrands.

Both \(I_j\)'s finite core and \(W_j\)'s finite core use these panels, with their respective weights. Use the generalized positive majorants in Note26(25)–(27) to pay the retained-mode exterior, all omitted modes and endpoint omitted modes. In particular, the error from finite signed \(D_{j,M}\) obeys
\(\big||D_j|-|D_{j,M}|\big|\le|D_j-D_{j,M}|\).
Add that error symmetrically to its finite-core integral, while retaining nonnegative physical tails where applicable. Bound \(S_j,C_j\le e^{Ru}\) only for tails; use their phase dependence in the core. Do not assign theta tail constants to a changed source.

The whole-mode bound is over the entire half-line; the retained-mode source exterior is a disjoint complement. If separate core/exterior estimates conservatively pay an omitted-mode bound more than once, record the extra payment explicitly instead of calling it a cancellation or an unpaid term. For endpoint tails, use the exact first omitted component and geometric ratio at the endpoint, with an interval-safe ratio below one.

If the 1024-panel widths prevent deciding the specific IBP-versus-moment improvement or a requested margin, allow **one refinement to 2048 panels** for the affected \(j\), at both precisions. No other panel refinement, contour change, tolerance change or added precision. Record every actually used stage. Total source acquisition cap: **20 minutes**, excluding ordinary documentation. An enclosure that remains unresolved is an admissible terminal return.

## 4. Three payment rules and twelve fixed cases

For each fixed \((r,N)\), compute:

1. **A — coupled moment rule:** original Note16 formula with outer radius \(2r\), corresponding complete moments and tail factor \((N+3)/2^N\).
2. **B — separate-radius moment rule:** outer \(R=1/32\), its original positive moments, and \(T_N(r/R)\).
3. **C — separate-radius IBP rule:** the same \(R\), with \(\mathcal U_3,\mathcal U_4\) and the same \(T_N(r/R)\).

Save the finite coefficient sum, \(M_G\), tail, \(\Gamma_N,d_N,c_N\), and positive/nonpositive/unresolved status for each rule and case. Do not infer exact rejection from a negative lower bound: rejection requires a nonpositive upper bound or an exact analytic obstruction. Report the least **certified** passing degree among the fixed choices and any uncertainty about a lower degree.

Use shared-input difference formulas, such as
\(\Gamma_B-\Gamma_C=(M_{G,B}-M_{G,C})T_N\), to avoid unnecessary interval cancellation. Exact C cannot be worse than B; a rounded inconclusive comparison must be labelled as such. Neither must dominate A at every radius. The intended gain is an improved payment rule, not a claim of superiority over an optimal consumer of identical information.

If \(|D_0|\) has a strictly positive certified lower bound, enclose Note26(19)'s \(r_*\) for B and C. For C only, choose **the largest dyadic radius no greater than the positive certified lower endpoint of \(r_*\)** from the confirmed 384-bit inputs. This is one deterministic downward rounding, not a search through radii. Report it as a *data-derived degree-one ball*, separately from the fixed-case table. Check its actual \(d_1\) and \(d_1\ge |D_0|/2\) by the theorem and/or an outward algebraic enclosure. If the center discriminant remains unresolved, report no derived ball and do not move the center.

## 5. Matched direct, scalar and C01 consumers

All consumers receive the same complete acquired information. The direct strip has the same row and \(\Gamma_N\); it supplies at least the coefficient's \(\mu=d/K\). For each positive C case report the two scalar lower bounds Note26(23); if either passes, state that explicitly. Do not call a positive small ball evidence of a joint-information advantage merely because the formula contains both jet components.

For a single representative positive C case, choose the largest fixed radius with any positive C degree, and then the smallest certified passing degree there. If no fixed C case is positive but the formula-derived ball exists, use that degree-one ball. With this representative, compute \(B_2=|b|+r(\mathcal U_3+\mathcal U_4)\) and a certified integer \(C\ge1+B_2/\mu\) for the inherited eventual C01 comparison at spatial coefficient one. Retain the compact-uniform derivative-limit dependency and lack of an acquired start time.

Only after a representative positive case is confirmed, acquire the four carrier moments \(j=0,1\) at \((T,Y)=(17/64,0),(17/64,4)\). This common containing-domain carrier is valid for all fixed and formula-derived radii here. Pay its complete tails and \(6L\) preparation term, then report one conservative all-time floor for the representative's **exact defined positive coefficient**, using Note26(17). No spatial cutoff may be left unpaid. If no representative exists, do not acquire carrier data.

## 6. Return and consequence

Return actual model/effort, date, all input hashes, code and small outward records in the affiliated numerics folder, derivations in notes and an execution self-check in reviews. Preserve existing proof, accepted records and frozen requests. Update Progress06 and the actual chat history, then give a model-change continuation.

Report: (i) strict or unresolved derivative-envelope reductions; (ii) all twelve three-rule cases and degree/radius tradeoffs; (iii) the optional formula-derived radius; (iv) matched direct/scalar/C01 comparisons and one conditional carrier consequence when acquired; (v) complete errors, actual runtime, integrand/panel counts and incremental IBP cost. The same center jets are shared; do not count them three times or claim computational savings from bounds alone.

A positive sign is not the only completion: a smaller tail with no degree change, no measured improvement, exact failed margins, or unresolved enclosures within the cap are meaningful returns. A fixed E02 assessment of the actual proof/data should be specified after execution. New conceptual issues return to B03; do not widen this task into high-frequency coverage, a new source/reference or a manuscript.

## Frozen inputs

The hashes identify the issued sources, not their mathematical correctness. Live progress, navigation, continuation and growing histories are mutable context. Report a mismatch instead of editing the issued request.

| Repository-relative source | SHA-256 |
| --- | --- |
| `papers/investigations-5/05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/26_ADAPTIVE_RADIUS_AND_PHASE_ALIGNED_IBP_B03_R5_20261030.md` | `d450a8ccb05ce40e8e567a9585002d047406698775140f18606def71b31fa56b` |
| `papers/investigations-5/05_radial_theta_collision_geometry/reviews/fixed_coefficient_parameter_geometry/09_ADAPTIVE_RADIUS_IBP_B03_R5_SELF_ASSESSMENT_20261030.md` | `9fdfefac92da1409297747b8cef9a1e6396c1d2b7b86a3da30b299aae848bbe7` |
| `papers/investigations-5/05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/16_QUADRATIC_HEAT_BEZOUT_COEFFICIENT_B03_R3_20261030.md` | `2d9ef8d6b1abb9dc8ee6dcf8f414bc185258922fcb0ba2a97164b84cdca2c1ce` |
| `papers/investigations-5/05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/12_REGIONAL_MOMENT_COEFFICIENT_AND_COMMON_FLOW_LIMITS_B03_R2_20261030.md` | `ede3a35d5eff3e388550482898ad917f827dd35a9bb400d5a1efd8de721f1948` |
| `papers/investigations-5/05_radial_theta_collision_geometry/reviews/fixed_coefficient_parameter_geometry/03_FCG_E02_R2_REGIONAL_COEFFICIENT_ASSESSMENT_20261030.md` | `b4d7df60e80be977dd361289db225e6d10302bd9727bf76db90c98f46732e923` |
| `papers/investigations-5/05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/22_FIXED_DEGREE_TAIL_AND_QUADRATIC_TIME_LIMITS_B03_R4_20261030.md` | `20ea11a487c2b408e223e735b461f871a439bfbce3fffe5b79b001a723f058e9` |
| `papers/investigations-5/05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/24_E02_R4_VERIFICATION_NOTES_20261030.md` | `d742d7ce0cf2ae5c6f8c3bce97dd854b7e106ac127534d44f23512cba2250577` |
| `papers/investigations-5/05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/25_CONTINUATION_AFTER_E02_R4_AND_MODEL_HANDOFF_20261030.md` | `333a4655843fe092650cc34ea317ecb88c2e083feca62483a5203a4cd80b3d1e` |
| `papers/investigations-5/05_radial_theta_collision_geometry/reviews/fixed_coefficient_parameter_geometry/08_FCG_E02_R4_COEFFICIENT_LIMITS_ASSESSMENT_20261030.md` | `36d882bf0fccb8aa022310fa18729be6a0e858786a289d226be2f21b8dd64c6b` |
| `papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md` | `faba3bd78b3a78f527c97f6d4c933eee85b7f64a2061dc3a136e78a0b80a98ee` |
| `papers/investigations-5/05_radial_theta_collision_geometry/notes/fixed_coefficient_parameter_geometry/03_POISSON_LOCALIZATION_AND_RELATIVE_LOSS_B02_20261030.md` | `33283b95eb1497821c9eccc02ba230f174554f71bf95a12d1dfb7f22d28b014a` |
| `papers/investigations-5/05_radial_theta_collision_geometry/numerics/fixed_coefficient_parameter_geometry/execute_fcg_e01_r1.py` | `af4a74dac5b39835611ae6e82591dc073b533167b2881db58f10b154f230fa0e` |
| `result-summaries/12_collision_controls_and_screening.md` | `116d99af6515c30d4ecc4a6485da35932d0e5062e7cb5d949f7c1f5f1b5a9e92` |

[progress]: ../../06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[proof]: ../../../notes/fixed_coefficient_parameter_geometry/26_ADAPTIVE_RADIUS_AND_PHASE_ALIGNED_IBP_B03_R5_20261030.md
[self]: ../../../reviews/fixed_coefficient_parameter_geometry/09_ADAPTIVE_RADIUS_IBP_B03_R5_SELF_ASSESSMENT_20261030.md

Follow the [model workflow](../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md), [result index](../../../../../../result-summaries/README.md), [collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../../../avoid/README.md), particularly [scope](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [separate bounds](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [noncircular constants](../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md), and the [history workflow](../../../../../../tools/CHAT_HISTORY.md).
