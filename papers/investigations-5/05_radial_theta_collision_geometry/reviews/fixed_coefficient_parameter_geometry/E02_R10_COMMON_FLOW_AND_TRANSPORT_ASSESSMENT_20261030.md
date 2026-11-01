# FCG-E02 R10: common-flow and fixed-transport assessment

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded **gpt-6.1-sol / ultra**, existing Investigation05 **chat0051**, *Assess R8 and signed-source work*, thread `01a18e61-b771-7d81-9290-9dad3cc07d78`. Parent reconciles two read-only same-Sol contributions. This is different-model internal assessment of the Astra/max R10 proof, with shared inherited source and analytic premises; no specialist, formal or independent source validation is claimed. Proof-author chat0050 and assessment chat0051 remain distinct.

**Disposition: all five frozen obligations accepted without mathematical correction.** The [issued packet](../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R10_COMMON_FLOW_AND_TRANSPORT_ASSESSMENT_20261030.md), [R10 proof](../../notes/fixed_coefficient_parameter_geometry/B03_R10_COMMON_FLOW_AND_FIXED_TRANSPORT_LIMIT_20261030.md), self-review and inputs remain unchanged. Eleven frozen hashes match. The upstream source-free replay reproduces every saved field except runtime; a separately arranged exact-rational reconstruction confirms the decoded moment/discriminant intervals and both final inequalities. [Evidence](../../numerics/fixed_coefficient_parameter_geometry/fcg_e02_r10_common_flow_transport_assessment_20261030.json) and [verification program](../../numerics/fixed_coefficient_parameter_geometry/verify_fcg_e02_r10.py) retain those checks. Replay metadata identifying Astra/max is the upstream program's static proof-author metadata, not this assessment's selected model.

| Frozen obligation | Disposition | Decisive finding |
| --- | --- | --- |
| 1. Finite domain, accepted input and coefficient distinction | Accept | R9's local derivative floor covers the entire union Q_rho; common c=1 is separate from exact C04 coefficients. |
| 2. Complete common carrier | Accept | Complete L/R2 and shared positive propagation give Nbar<0.508, including preparation, radial source boundary and all spatial tails. |
| 3. Explicit all-time floor | Accept | Exact rational lower energy is 1.071661652201145…e-35, hence >1e-35 for all auxiliary time on the finite tube. |
| 4. Fixed-input transport obstruction | Accept | One omitted positive budget term and the included anchor force the paid discriminant below −1.10e-18 at width4, regardless of polynomial enclosure sharpness. |
| 5. Scope, controls, provenance and continuation | Accept | Only the specified payment class is rejected; global transfer stays open, and no new acquisition or R11 research was performed. |

## 1. Physical tube and separate common coefficient

R9 establishes a local scalar derivative floor greater than 2.33769e-10 on every radius-rho ball centered on Q, with rho=1/16384 and
\(Q=[1/4-1/128,1/4+1/128]\times[64,66]\).
It therefore supplies the uniform physical mass lower bound
\(|J|\ge|H_A|>\mu=2.3e-10\) on the entire union Q_rho, including parts outside Q. No extension from sampled centers is being assumed. The maximum physical time is exactly 4225/16384, leaving positive carrier-time slack 127/16384 below T0=17/64.

The accepted carrier proof is valid for any fixed positive c after the physical mass is paid. Choosing the separate family member c=1 throughout Q_rho does not replace the exact local coefficients c1(p)=d1(p)/(1+h0²+h1²+b²). No comparison at identical c with those varying coefficients, coefficient optimization or new theta sign is claimed. The all-time quantifier is for auxiliary s; physical T remains in the finite tube.

## 2. Carrier and energy derivation

For the original raw radial source, r=exp(2u) and polar integration gives carrier mass L and second moment R2 from the complete j0/j1 moments at T0, Y0 and Y4. The source boundary r=1 belongs to that full radial measure. Unit Gaussian preparation has zero mean and second moment6, so convolution adds6L. Positivity of the same scalar propagator acting on both vector components implies |W_c|<=Sigma_c; using distinct propagators would not justify this step.

The complete384bit intervals independently decode to L approximately0.0677457631633 and R2 approximately0.1009691666006. Their rational upper endpoints satisfy L<0.067746, R2<0.100970 and
\[
 \max\{R_2+6L,3L\}<0.507443745581<0.508.
\]
The generator identity and X·v>=|X|² give N_c'<=6L−2cN_c. Thus c=1 admits the fixed bound Nbar=0.508 for all auxiliary s>=0. This uses mass conservation and complete prepared moments, without stationary convergence or a start time.

Take the spatial radius R_X²=2Nbar/mu. The carrier exterior mass is at most mu/2. Conserved vector mass and Cauchy–Schwarz on the spatial ball give
\[
 E_1(s;p)\ge\frac{3\mu^2}{16\pi}
       \left(\frac\mu{2\overline N}\right)^{3/2}.
\]
The inherited energy convention is the squared L2 norm, so no extra factor1/2 enters. With pi<22/7 and (3/200000)²<mu/(2Nbar), the rational lower bound is exactly
\[
 \frac{766521}{71526400000000000000000000000000000000000}
 =1.071661652201145\ldots\,10^{-35}>10^{-35}.
\]
This proves the requested uniform finite-region consequence. Positive physical mass is an input; it is never inferred backward from the energy floor. Every spatial exterior remains paid.

## 3. Why the fixed-input widening fails

For the H_A polynomial at source order17, retained indices satisfy2m+ell<=16. Its first omitted pure-frequency term is m0,ell17, with total source power18. Consequently the selected positive complete-M4 core error allowance satisfies
\(e_1(X)\ge m_4X^{17}/17!\), where m4 is the complete M4 lower endpoint. It does not follow that the actual oscillatory remainder is this large.

Every rectangle Q(X) includes its anchor. Hence any valid polynomial lower enclosure ell_D(X) is at most D_P(0,0), which equals the actual anchor discriminant and is at most its saved upper endpoint U_D. The stated physical discrepancy is a sum of nonnegative costs containing e1². Therefore
\[
 D_{\rm paid}(X)\le U_D-(m_4X^{17}/17!)^2.
\]
This reasoning holds even for an exact polynomial minimum; sharpening Bernstein conversion or subdividing that same polynomial cannot remove the error-budget obstruction. The algebraic threshold
\(X_\dagger=[(17!)^2U_D/m_4^2]^{1/34}\)
is correct, with nonpositive allowance already at equality. No numerical threshold optimization is needed.

Sign-aware decoding of the saved signed h0,h1,h2 intervals separately reconstructs U_D; it uses no upstream interval helpers. At the single prescribed X4 witness, exact rational values give

| Quantity | Display summary |
| --- | ---: |
| m4 | 2.3540277344773214e-5 |
| U_D | 1.905843126548657e-19 |
| omitted budget lower m4·4^17/17! | 1.1370064089786442e-9 |
| squared-budget / U_D | 6.783263302471535 |
| U_D minus squared-budget | −1.1021992614036461e-18 |

Thus the quoted ratio>6.78 and paid estimate<−1.10e-18 are both valid. Display values do not decide these inequalities; exact rationals do. The original finite coefficient-complement implementation needs X<66 for its geometric frequency tail. The underlying one-term infinite-tail obstruction is separate and survives a correctly extended summation implementation.

This stops only the unchanged anchor/order17/complete-M4 absolute-core payment with the stated quadratic discrepancy formula. It proves no negative actual discriminant, actual collision or negative energy at A68. New anchors, higher orders, different source splits and genuinely different signed or amplitude-relative remainder estimates remain outside the exclusion. The accepted width2 certificate remains unchanged.

## 4. Controls and evidence limits

The carrier and transport algebra are generic. At an actual control collision J=0, its required positive physical mass or derivative floor fails. Controls must use their own complete moments and actual event domains; theta's enclosures cannot be transferred. Weighted-square and finite-prime perturbations fail full theta reflection/unit coefficients; Euler-factor sources alter arithmetic; reflected, shape and positive-primitive controls lack complete theta square arithmetic. Atomic/finite-profile cases need their own admissible moments and preparation/exterior treatment. Changed kernels fail literal cosine reconstruction, conditional endpoint controls retain their hypotheses, and relaxed profiles are not physical collisions. Failure of the numerical mass premise is the load-bearing screen for this finite corollary; merely naming a missing arithmetic identity supplies no extra source sign.

This assessment checks the fixed proof and saved arithmetic. It does not independently revalidate the original quadrature, tail guards or source enclosures. The source-free replay and separately arranged reconstruction share rational arithmetic and inherited premises. R9's accepted different-model assessment is supporting evidence and remains distinct from both this R10 assessment and its proof-author self-review. There were zero new source or quadrature evaluations, root searches, domain certificates, parameter/degree/radius scans, flow optimizations or manuscript changes.

Read with the [result index](../../../../../result-summaries/README.md), [theta bookkeeping](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md) and [avoid index](../../../../../avoid/README.md), especially [shared-premise checking](../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [numerical questions](../../../../../avoid/10_numerics_ahead_of_the_question.md), [signed cancellation](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [noncircular inputs](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md).

**E02 R10 closes.** [Progress06](../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md) owns live status; [the continuation/model note](../../notes/fixed_coefficient_parameter_geometry/E02_R10_VERIFICATION_AND_MODEL_HANDOFF_20261030.md) preserves this assessment chat0051, separate from author chat0050. B03 R11 is the next conceptual option, unstarted under this request; B04 global coverage/target transfer remains gated. No new acquisition, manuscript, DRAFT_HISTORY or result-summary task is selected.
