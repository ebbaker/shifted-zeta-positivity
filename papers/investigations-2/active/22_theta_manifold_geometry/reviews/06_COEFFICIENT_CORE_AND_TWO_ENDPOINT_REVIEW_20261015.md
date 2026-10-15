# Review of the coefficient core and two-endpoint continuation

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This is an internal derivation and replay review by the coordinating assistant and independent collaborators using the same model configuration. It is not external refereeing or formal verification.

## Assessment

The bounded continuation delivers four useful results without claiming the missing theta signed-core theorem. The [updated overview](../research-overview/02_CHORD_CRITERION_AND_ARITHMETIC_BRIDGE_20261015.md) now prioritizes a coupled arithmetic estimate for the derivative-free amplitude. The direct finite scalar-shift experiment and the second-endpoint repair have been completed and found insufficient. The outer constant is genuinely improved, but remains conditional and computationally impractical. The manuscript source and existing build record are unchanged.

## 1. Exponential average and shrinking-window criterion

The [new criterion note](../notes/02_signed_turning_control/04_EXPONENTIAL_AVERAGE_AND_SHRINKING_CHORD_TARGETS_20261015.md) uses the exact identity

\[
W(x)^2-e^{-\delta}W(x)W(x+\delta)
=\int_0^\delta e^{-z}W(x)\{W(x+z)-W_x(x+z)\}\,dz.
\]

The exponential derivative and both endpoints have the correct signs. The normalized density is positive, but is not a compactly supported smooth probe; the note makes no rapid Fourier-decay claim. On the odd branch, the complete physical energy comparison is retained rather than replacing E by W² identically.

At each finite-multiplicity collision, the negative fixed-δ limit has order δ^(2r). The shrinking-window proposition compares the prescribed cutoff error with this order before taking the event limit. Its hypothesis `ε_N=o(δ_N^m)` for every fixed integer m is enough; Gaussian errors and δ_N=1/N meet it. Each fixed K_N must remain locally bounded, and the specified interval must eventually be covered. The proof does not take an unjustified simultaneous limit or assume a uniform bound in N.

An independent collaborator read the analytic argument and replayed the exact checker. All **1,620 assertions** passed for 36 signed/asymmetric heat germs, 108 certified full stationary roots and 216 whole zero-free intervals. Rational enclosures for the exponential and the odd-branch square-root-energy factor were checked. These are finite controls; the general theorem is the analytic argument in the note. No theta bound is inferred from the controls.

## 2. Complete elliptic insertion and its limitation

The [elliptic note](../notes/03_theta_bundles_and_connections/05_ELLIPTIC_SHIFT_CORE_AND_PROJECTION_OBSTRUCTION_20261015.md) was independently audited against the physical source operator. The review checked all translated fourth-jet multiplier coefficients, the zero-mode cancellation, cutoff reindexing, the finite primitive lower endpoint and corner, and the classification of fixed finite shift combinations. Separating the translated derivative pieces before heat integration would be invalid; the saved formula combines them first.

The boundary-band identity gives a Gaussian remainder multiplied by the full starting W, but leaves the signed interior form unresolved. The boundary-only conclusion is restricted to fixed bounded scalar shift combinations whose coefficients sum to one. It does not claim that coupled products, transverse restrictions, nonconstant insertions or growing ranges are impossible.

The projected recurrence and its polynomial-growth uniqueness proof give the ramp family `a_n=a_0+b|n|`. The normalization conclusion explicitly fixes a_0=1. This weaker projected law is distinguished from the full elliptic multiplier law. The exact checker also verifies finite-support rejection and both-parity heat-polynomial witnesses for the unresolved scalar form. All **481 assertions** passed independently and in the coordinator's replay. Infinite-series uniqueness and general shift classification remain analytic arguments, not consequences of a finite assertion count.

## 3. Two-endpoint collision certificate

The [control note](../notes/05_control_families/03_TWO_ENDPOINT_SQUARE_COLLISION_20261015.md) reduces the two source endpoints to exact linear constraints in scaled weights. The rational formula for P3/P1 and its monotonicity give a positive convex-vertex representation and a precise high-mode mass bound in that endpoint normalization. The control then uses a mixture of vertices F3 and F4.

The certificate brackets a Wronskian root at T=1/100 in `(83.5323729,83.5323730)`, proves the Wronskian derivative positive throughout that bracket, keeps the mixture strictly between zero and one, and proves positive second x derivative. This supplies H=H_x=0 at the exact bracketed point with fixed positive coefficients. Endpoint cancellation is algebraic; a ball merely containing zero is not used as a substitute for equality. Positive normalization gives the specified primitive derivatives. The fifth source derivative is separated from zero.

The coordinator and a separate collaborator read the certificate and replayed all **26 mixed or validated assertions** at 160 bits. The replay evaluates **44 complete integrals**, combining finite-interval Acb integration with explicit real-tail allowances. Whole-bracket enclosures use derivative bounds, including a positive fourth absolute moment, rather than unvalidated point sampling. The analytic tail domination was also reviewed.

The positive infinite-tail continuation uses a nonzero endpoint elimination minor and reduced collision Jacobian. It is qualitative: no explicit allowed perturbation radius is supplied. The resulting control does not satisfy full reflection or the theta coefficient law. Its even extension is C⁴ and not C⁵. The result excludes support-only localizers plus two endpoint identities as a sufficient mechanism; it does not refute every finite endpoint hierarchy.

The historical discovery grid and its interrupted candidate refinement are explicitly separated from the default fixed-bracket replay. The reported 468 determinant sign changes are not 468 certified collisions or an exclusion theorem. No broad discovery search was needed to replay the saved certificate.

## 4. Outer-budget refinement

The [outer note](../notes/06_effective_outer_bridge/01_LOW_INDEX_BUDGET_REFINEMENT_20261015.md) was checked against Investigation 21 Notes 43 and 58. A separate collaborator verified the four low-index ranges, uniform heat-parameter envelope, integral-tail starting points, monotonicity beyond the original domain threshold, and both budget allocations. All **35 exact assertions** passed independently and on coordinator replay.

Only the low-index constant A0 is replaced by `218227/384`; the exponent-pair input, other error assignments, analytic branches, original complex-disc validity and carrier argument remain imported. The reduction factor exceeds 3,974. The reallocated sufficient log-height is conditional on the unevaluated exponent-pair constant and any validity threshold. The retained tL restriction is unchanged.

The majorant's own lower limit near `L−1=31,424,688` is a limitation of that bound, not a claim about actual positivity. The refinement does not make a practical bridge, prove a new unconditional starting height, recertify all imported analytic work, or establish a new small-time domain.

## 5. Installed replay and research decision

The [manifest](../numerics/COEFFICIENT_CORE_AND_TWO_ENDPOINT_CHECKS_20261015.json) binds installed sources and receipts, records the independent replay comparisons, and distinguishes the **2,136 exact** assertions from the **26 mixed or validated** assertions. Output-path defaults in the endpoint and outer scripts were made portable before installation; the mathematical calculations were unchanged and the installed scripts were rerun. The previously reviewed receipts were compared after excluding only source-digest and elapsed-time metadata where appropriate.

The next useful result would identify an arithmetic relation controlling the indefinite two-source amplitude form, with the complete physical observation retained. A bare theta uniqueness statement or another scalar cutoff reindexing will not meet that goal. A finite certified pilot is appropriate only after a coefficient rule and error payment are specified. This is a research priority, not a claim that a coupled representation is guaranteed to exist.

The [handoff](../notes/00_research_coordination/05_COEFFICIENT_CORE_AND_TWO_ENDPOINT_CONTINUATION_20261015.md) gives the next bounded task and stop criteria. All new analytic and numerical results remain in notes and numerics pending a separate manuscript integration. Existing manuscript bytes and historical verification records have been preserved.
