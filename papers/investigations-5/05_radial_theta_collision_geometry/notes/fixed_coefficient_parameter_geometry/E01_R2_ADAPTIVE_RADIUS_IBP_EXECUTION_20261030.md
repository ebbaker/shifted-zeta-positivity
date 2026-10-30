# FCG-E01 R2: completed adaptive-radius and IBP comparison

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol**, effort **ultra**, existing Investigation05 **chat0047**, *Continue FCG-E02 R2 assessment*.

**Execution complete.** The original [frozen request][packet] and [amendment A1][amend] were executed at both prescribed precisions. All 36 rule/case margins at each precision are decided. Separating the analytic radius changes the first passing degree among the issued choices; the phase-window IBP envelope gives an additional degree reduction at radius \(1/256\). No panel refinement was needed.

The [script][script] and [complete outward record][record] retain all inputs, errors, panels, cases, comparisons and costs. The [self-check][self] is internal execution checking, pending the [bounded E02 R5 assessment][assessment]. [Progress06][progress] alone owns live status.

**The manuscript was not modified.** Astra's parallel manuscript work, its integration status, manuscript files and DRAFT_HISTORY are outside this execution. Unnumbered execution filenames avoid competing for the next numbered research/manuscript note.

## 1. Fixed inputs and acquisition

The unchanged test has
\[
 (\tau,a,R)=(1/4,64,1/32),\quad
 r\in\{1/64,1/128,1/256\},\quad N\in\{1,2,4,8\}.
\]
The endpoint choices are \(U_3=41\pi/128,\ U_4=21\pi/64\), fixed at the center. Their phases are exactly \(22\pi,23\pi\).

Complete signed \(h_0,\ldots,h_{17}\), six positive moments at the three specified outer radii, and both derivative envelopes were acquired at 256 and 384 bits. Analytic quadrature uses eight modes on \([0,1]\), absolute/relative goals \(2^{-180},2^{-140}\) and \(2^{-280},2^{-240}\), with evaluation limit 200000 and depth 30 per integral. Complete omitted-mode and retained-mode exteriors are added before using the jets.

For each derivative order and precision, 1024 real interval panels enclose the entire range on \(u=U_jv\), including the Jacobian and actual phase weights. The signed finite \(\Phi_8,\Phi'_8\) and \(D_{j,8}\) are formed before the absolute value. These nonanalytic cores are never passed to Acb analytic quadrature.

The complete missing-mode correction to each absolute core is symmetric. Whole-line \(I_j\) additionally pays the retained exterior and a second whole-mode upper bound; that conservative duplicate is recorded explicitly. \(W_j\) pays its full complex-neighborhood boundary, its original-form exterior and its own omitted modes. No center-phase boundary cancellation is assumed on the neighborhood.

All actual guards pass. Both precision stages' 24 shared analytic inputs, envelope intervals and 36 fixed margins overlap. All signs and strict improvement questions were decided at 1024 panels, so the optional 2048 step was not used.

## 2. Derivative-envelope gain

Both \(I_j\) and \(W_j\) are rigorously below the original moment bound, and \(W_j<I_j\) at both precisions. Thus \(W_j\) is the certified minimum in \(\mathcal U_j=\min(M_j,I_j,W_j)\).

The following widened intervals include both precision stages:

| Order | Moment \(M_j\) | Whole-line \(I_j\) | Phase-window \(W_j=\mathcal U_j\) |
| --- | --- | --- | --- |
| 3 | [1.218, 1.219] × \(10^{-4}\) | [2.017, 2.480] × \(10^{-5}\) | [1.233, 1.627] × \(10^{-5}\) |
| 4 | [2.363, 2.364] × \(10^{-5}\) | [3.913, 5.032] × \(10^{-6}\) | [2.386, 3.304] × \(10^{-6}\) |


Exact endpoint comparisons imply
\[
 \mathcal U_3/M_3<0.134,\qquad \mathcal U_4/M_4<0.140.
\]
These are improved paid derivative envelopes, not new lower bounds for a theta discriminant or evidence of global coverage.

## 3. All fixed margins and minimum passing degrees

A is the coupled-radius moment rule; B keeps the outer \(R=1/32\) with moment bounds; C keeps that same outer radius with the IBP minimum. Every entry below is an outward enclosure for the exact defined \(d_N\), widened to include both precisions. Full \(F_N,M_G,T_N,\Gamma_N,c_N\) and consumer intervals are in the record.

| Radius | Degree | A margin | B margin | C margin |
| --- | --- | --- | --- | --- |
| 1/64 | 1 | [-3.251, -3.250] × \(10^{-15}\) | [-3.251, -3.250] × \(10^{-15}\) | [-4.336, -3.287] × \(10^{-16}\) |
| 1/64 | 2 | [-2.032, -2.031] × \(10^{-15}\) | [-2.032, -2.031] × \(10^{-15}\) | [-2.710, -2.053] × \(10^{-16}\) |
| 1/64 | 4 | [-7.110, -7.109] × \(10^{-16}\) | [-7.110, -7.109] × \(10^{-16}\) | [-9.473, -7.172] × \(10^{-17}\) |
| 1/64 | 8 | [-6.966, -6.965] × \(10^{-17}\) | [-6.966, -6.965] × \(10^{-17}\) | [-9.133, -6.872] × \(10^{-18}\) |
| 1/128 | 1 | [-1.605, -1.604] × \(10^{-15}\) | [-4.514, -4.513] × \(10^{-16}\) | [-6.004, -4.549] × \(10^{-17}\) |
| 1/128 | 2 | [-1.003, -1.002] × \(10^{-15}\) | [-1.466, -1.465] × \(10^{-16}\) | [-1.940, -1.465] × \(10^{-17}\) |
| 1/128 | 4 | [-3.509, -3.508] × \(10^{-16}\) | [-1.322, -1.321] × \(10^{-17}\) | [-1.599, -1.166] × \(10^{-18}\) |
| 1/128 | 8 | [-3.429, -3.428] × \(10^{-17}\) | [1.045, 1.046] × \(10^{-19}\) | [1.786, 1.814] × \(10^{-19}\) |
| 1/256 | 1 | [-7.971, -7.970] × \(10^{-16}\) | [-9.104, -9.103] × \(10^{-17}\) | [-1.198, -0.903] × \(10^{-17}\) |
| 1/256 | 2 | [-4.981, -4.980] × \(10^{-16}\) | [-1.485, -1.484] × \(10^{-17}\) | [-1.815, -1.330] × \(10^{-18}\) |
| 1/256 | 4 | [-1.743, -1.742] × \(10^{-16}\) | [-1.580, -1.579] × \(10^{-19}\) | [1.438, 1.551] × \(10^{-19}\) |
| 1/256 | 8 | [-1.694, -1.693] × \(10^{-17}\) | [1.901, 1.902] × \(10^{-19}\) | [1.902, 1.903] × \(10^{-19}\) |


Every positive/nonpositive decision uses the appropriate endpoint; there are no zero-crossing unresolved margins. The smallest certified passing degree **among \(1,2,4,8\)** is:

| Inner radius | A: coupled moment | B: separate-radius moment | C: separate-radius IBP |
| --- | --- | --- | --- |
| \(1/64\) | None through 8 | None through 8 | None through 8 |
| \(1/128\) | None through 8 | 8 | 8 |
| \(1/256\) | None through 8 | 8 | 4 |

All twelve shared-input differences \(\Gamma_B-\Gamma_C\) are rigorously positive at both precisions. Exact C cannot be worse than B by its minimum definition; the recorded difference formulas also establish strict numerical improvement here. At \(1/256\), this improvement changes a nonpositive B margin at degree 4 into a positive C margin. At \(1/128\), it improves the degree-8 margin without changing the first passing issued degree. No conclusion concerns degrees beyond eight.

## 4. Amended formula-derived degree-one ball

The complete center discriminant is positive:
\[
 D=|h_1^2-2h_2h_0|\approx1.9058431265\,10^{-19}.
\]
Amendment A1's sharp quadratic payment was used for both B and C:
\[
 r_{\rm quad}=\min\{R/2,\tau/2,\,
 D/(L_0+\sqrt{L_0^2+16MD/R^2})\}.
\]
Both precision stages enclose:

| Rule | Outward sharp-radius enclosure |
| --- | --- |
| B | [8.4593, 8.4594] × \(10^{-5}\) |
| C | [2.3160, 2.6591] × \(10^{-4}\) |


C's certified lower endpoint exceeds B's upper endpoint; their ratio is greater than 2.7. These are radii licensed by the particular quadratic payment, not optimal true noncolliding radii.

For reproducibility, downward dyadic rounding is interpreted here as the largest **power-of-two radius** no greater than C's confirmed positive lower endpoint. The endpoint itself is also retained exactly in binary in the record. This single rounding gives
\[
 \boxed{r_{\rm derived}=1/8192,\qquad N=1.}
\]
The next power \(1/4096\) exceeds that certified lower endpoint. The actual derived-ball evaluation verifies \(d_1>1.80\,10^{-19}\) and \(d_1-D/2>0\), so the amended theorem's \(d_1\ge D/2\) is confirmed. This is explicitly a data-derived ball, separate from the twelve fixed cases, with no search through radii.

## 5. Matched consumers and representative consequence

The positive C cases give the following scalar tests. Negative floors mean these sufficient component tests fail; they do not imply a scalar zero.

| Positive C case | Scalar-H floor | Scalar-derivative floor |
| --- | --- | --- |
| r=1/128, N=8 | [-4.557, -1.876] × \(10^{-10}\) | [-1.272, -0.963] × \(10^{-7}\) |
| r=1/256, N=4 | [3.671, 4.342] × \(10^{-10}\) | [-6.324, -4.785] × \(10^{-8}\) |
| r=1/256, N=8 | [3.671, 4.342] × \(10^{-10}\) | [-6.324, -4.785] × \(10^{-8}\) |
| Derived r=1/8192, N=1 (384-bit) | [6.420, 6.421] × \(10^{-10}\) | [-1.567, -1.086] × \(10^{-9}\) |


At \(r=1/128,N=8\), the joint certificate passes while both of these simple component floors are negative. At \(1/256\), and on the derived ball, the scalar-\(H\) floor is already positive. This distinguishes the correlated allowance from those component tests without asserting superiority over all direct methods.

The exact direct strip receives the identical row and \(\Gamma_N\), so it supplies at least \(\mu=d/K\). No spatial-flow or coordinate separation advantage is claimed.

The prescribed representative is **C, \(r=1/128,N=8\)**: the largest fixed radius with a positive C case and its least certified issued degree. Its confirmed conservative bounds are
\[
 c>1.78\,10^{-19},\qquad \mu>4.25\,10^{-10}.
\]
The same inputs give \(1+B_2^{\rm upper}/\mu^{\rm lower}<361\), so the certified integer C01 comparison constant is **361**, at spatial coefficient \(c=1\). Its positivity remains eventual under the accepted compact-uniform derivative convergence, with no acquired start time.

Only after this representative was confirmed were the four common carrier inputs acquired at \(T=17/64\), orders \(0,1\), and \(Y=0,4\). They give \(L<0.068,\ R_2<0.101\), and, using the representative's exact defined positive coefficient,
\[
 \overline N=\max\{R_2+6L,3L/c\}<1.14\,10^{18}.
\]
The complete scalar-carrier theorem then yields
\[
 \boxed{E_c(s;p)>2.7\,10^{-62}\quad(s\ge0,\ p\in B_{1/128}).}
\]
The lower \(c,\mu\) and upper carrier endpoints are conservative inputs to this bound; they are not substitute equation coefficients. An exact rational squared comparison with \(\pi<22/7\) verifies the reporting floor. Unit preparation contributes \(6L\), and the full spatial exterior is paid.

## 6. Cost, controls and disposition

Runtime was Python 3.10.0, python-flint 0.9.0, FLINT 3.6.0. The acquisition used **28 distinct analytic integrands, 52 analytic calls and 31700 callbacks**, with maximum 732 callbacks per integral. There were **four 1024-panel acquisitions, totaling 4096 range evaluations**. Source acquisition took **1.430110 seconds** locally; individual analytic calls totaled about 1.079388 seconds, and the timed IBP panel component about 0.1877175 seconds. The latter is not an end-to-end matched benchmark of all IBP overhead. Shared center inputs are counted once per precision, not once per consumer. Smaller bounds and degrees do not establish runtime savings.

The source-specific controls retain their actual event balls and valid envelopes. A ball containing an actual collision rejects any valid margin; shrinking away removes that collision test. The weighted-square event near 44.13 is not placed at this center 64 and is not an all-real threshold. Euler negative-Laguerre witnesses and relaxed profile measures are not physical event locations. Atomic sources need not admit this derivative-integral IBP method.

This is a completed finite comparison: separate radii and IBP improve the paid allowances and, in one fixed radius case, the required issued degree. It does not prove an efficient global radius schedule, universal center-discriminant sign, actual theta zero crossing or RH/Newman gain. The exact primitive remainder identity was checked algebraically, not implemented as a competing quadrature route. Earlier accepted C04 revisions and scoped R4 limits remain intact.

**Next: [E] FCG-E02 R5 — Sol**, the [bounded proof-and-data assessment][assessment]. The [continuation/model handoff][next] preserves chat0047 and the manuscript exclusion. No manuscript, integration, coverage or milestone work is selected by this return.

[packet]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R2_ADAPTIVE_RADIUS_IBP_COMPARISON_20261030.md
[amend]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E01_R2_A1_RADIUS_RULE_20261030.md
[script]: ../../numerics/fixed_coefficient_parameter_geometry/execute_fcg_e01_r2.py
[record]: ../../numerics/fixed_coefficient_parameter_geometry/fcg_e01_r2_adaptive_ibp_20261030.json
[self]: ../../reviews/fixed_coefficient_parameter_geometry/E01_R2_ADAPTIVE_RADIUS_IBP_SELF_CHECK_20261030.md
[assessment]: ../../research-progress/handoffs/fixed_coefficient_parameter_geometry/FCG-E02_R5_ADAPTIVE_RADIUS_IBP_ASSESSMENT_20261030.md
[progress]: ../../research-progress/06_FIXED_COEFFICIENT_PARAMETER_GEOMETRY_RESEARCH_PROGRESS_20261030.md
[next]: E01_R2_CONTINUATION_AND_MODEL_HANDOFF_20261030.md
