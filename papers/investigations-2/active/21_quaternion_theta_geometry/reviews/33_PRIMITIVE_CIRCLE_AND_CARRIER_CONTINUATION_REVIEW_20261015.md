# Review of the primitive control circle losses and carrier budget

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the session metadata. Independent internal LLM checks are described below; this is not external refereeing or formal verification.

The three continuation results in Notes 56–58 pass the analytic and exact-arithmetic checks recorded here. The positive primitive control substantially strengthens the earlier source-shape example, the circle calculation quantifies cancellation discarded by a sufficient bound, and the outer calculation closes the previously open carrier-derivative budget. None proves the missing theta stationary estimate or enlarges the established sign domains.

## Positive primitive control

[Note 56](../notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md) was checked by the coordinating agent and an independently prompted reviewer. The checks covered the normalized Green primitive, uniqueness with super-Gaussian decay, all endpoint boundary terms, the exact signed reconstruction, convexity after applying the heat multiplier, and the control source's decay and concavity.

In particular, the inequality \(-\phi'(v)\ge4v\phi(v)\) gives
\[
u\int_u^\infty\cosh(v-u)\phi(v)\,dv\le\phi(u)/4+\psi(u)/32.
\]
This verifies the signs and constants in the strict-convexity proof. Normalization gives \(\psi'(0)=-1/2\); even forcing gives every odd endpoint derivative, and hence every algebraic asymptotic coefficient. These coefficients do not determine the physical cancellation or constitute a convergent expansion.

The Gaussian polynomial, its discriminant, the exact double-zero curvature, and the nonzero implicit-function Jacobian were rederived. The persistence argument holds for sufficiently small positive damping, with Gaussian domination on a compact time neighborhood; it does not supply a numerical damping threshold. The normalized source preserves the collision. The stationary adverse pole and the extension of the rational-nonclosure argument are valid for that fixed positive damping parameter.

The [checker](../numerics/check_positive_primitive_collision_control.py) and [receipt](../numerics/POSITIVE_PRIMITIVE_COLLISION_CONTROL_CHECKS_20261015.json) report **seven passing algebra check groups**, including calculations in \(\mathbb Q(\sqrt{10})\). The coordinating replay reproduced the receipt bytes. These groups contain multiple assertions; they are not represented as seven independently validated infinite-dimensional analytic claims.

## Circle defect and radius scale

[Note 57](../notes/02_signed_cusp_control/57_CIRCLE_DEFECT_MULTIPLICITY_AND_RADIUS_20261015.md) was checked independently by the outer-budget reviewer and the coordinator. The exact excess identity, sign normalization for either sign of the leading jet, positivity of both limiting boundary masses, and the compact-radius uniformity all check. The odd branch uses \(E/h_1^2=1+O(s^2)\), rather than an incorrect exact equality.

The general analytic-field statement now explicitly requires holomorphy on the full circles and nearby time slices. This was the one precision clarification identified in review. The entire theta field satisfies it for every finite radius; a merely local germ does not automatically allow arbitrary radii.

The heat-polynomial profile, weighted Fourier projection, higher-multiplicity large-radius limit, and elementary double/triple-collision formula were rederived. The fixed-radius and shrinking-radius regimes are separate arguments. The radius involving an unknown event is a diagnostic and is not offered as a source-prescribed locally bounded parameter.

The [checker](../numerics/check_circle_defect_collision_profile.py) and [receipt](../numerics/CIRCLE_DEFECT_COLLISION_PROFILE_CHECKS_20261015.json) give **240 passing exact rational assertions**, covering \(r=1,\ldots,12\), both physical branches, perturbed predecessor leading terms and a Laurent-polynomial Fourier projection. A coordinating replay reproduced the receipt bytes. The proof covers every finite multiplicity; the finite checker does not establish that quantifier by testing.

## Complete carrier error

[Note 58](../notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md) was independently audited by the circle-analysis reviewer and the coordinator. Both rederived the three chain rules for \(\log Q\), including the shifted zeta argument and all heat terms. The estimates remain uniform when \(tL\) grows. The explicit half-plane \(\Re w\ge9/8\) is inherited from the actual Note 43 geometry.

The logarithmic zeta bounds \((65,1028,24603)\) follow from the Euler series and an integral-plus-maximum bound. The ensuing bounds \((34,260,3100)\) for the carrier logarithmic derivatives give the phase error \(409/L\). Adding the prior replacement allowance yields \(1728B_C(L)+409/L\). The two full Laguerre envelopes and physical energy inequality follow under the stated \(1/8\) total-error condition.

All six \(1/48\) budget shares in the conditional height formula were checked, including the integers \(749376582912\) and \(663552\). The [checker](../numerics/check_carrier_phase_budget.py) and [receipt](../numerics/CARRIER_PHASE_BUDGET_CHECKS_20261015.json) give **43 passing exact rational and polynomial assertions**. The independent reviewer and coordinator replayed it; the coordinating replay reproduced the original receipt bytes.

The conclusion remains conditional on the actual maximal-interval exponent-pair constants, their specified positive loss and any validity threshold. Setting the imported constant to one would be unjustified. The new work closes the separate elementary carrier budget; it does not evaluate the imported arithmetic package, cross the five-halves middle interval, or close the finite bridge.

## Preservation and scope

The manuscript source and its build record were unchanged by this continuation. Their SHA-256 identities remain:

| File | SHA-256 |
| --- | --- |
| `manuscript/quaternion_theta_geometry.tex` | `ec9cca0a31e4e15f77559db4447fd61a572994b486c8955d0ddd689c059d3c61` |
| `manuscript/BUILD_RECORD.json` | `d35ea783bea0c175975d136e7febfb25719bfc8314cdf0cd42f970fbb0105aab` |

The numerical receipts bind their checker source hashes. A matching hash identifies bytes and does not certify a mathematical theorem. No new theta quadrature, stationary-root enclosure or sign region is asserted; the earlier interval certificates were not rerun. All new files are small source or execution records under the repository's large-file policy. [Note 59](../notes/00_research_coordination/59_PRIMITIVE_CONTROLS_AND_COMPLETED_PHASE_BUDGET_CONTINUATION_20261015.md) records the resulting research target and conversation identity.

Reproduce the finite checks from the investigation directory:

```sh
python3 numerics/check_positive_primitive_collision_control.py > /tmp/positive-primitive-replay.json
python3 numerics/check_circle_defect_collision_profile.py --output /tmp/circle-defect-replay.json
python3 numerics/check_carrier_phase_budget.py --output /tmp/carrier-phase-replay.json
```
