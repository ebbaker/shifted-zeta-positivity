# RTD-06: integral-budget comparison contract

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual coordinating model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**, verified from the current turn metadata.

The user asks whether the real Thom integral can be bounded below one without first proving pointwise interior nonvanishing. This is a bounded implementation/estimate comparison on inherited data, not an RH reformulation or new region. Follow [results](../../../../result-summaries/README.md), [avoid](../../../../avoid/README.md), especially [01](../../../../avoid/01_restating_the_target.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md), and [collision screening](../../../../result-summaries/12_collision_controls_and_screening.md).

## Fixed input and estimator

Retain D=[1/100,1/5] x [25,45], orientation dt wedge dx, r=10^-9 and b=1.5e-9. Retain the smooth normalized density of [Note 01](01_BOUNDED_SUPPORT_COMPARISON_CONTRACT_20261022.md), whose maximum is C=4/(e pi r²). Prior work already proves its true pullback support empty. That result is disclosed but may not be used by this consumer; prospective computational scouting, if any, is feasibility work rather than blind discovery.

Use 160-bit Arb; source modes n<=4 and u<=1 with complete omitted-mode and all-mode source-ray tails. Keep Taylor degrees L=50 in x and K=12 in t. Extend the supplier to components H through Hxxx, requiring 78 midpoint integrals (orders 0..77) and absolute moments through 79. All consumers in the comparison receive the same complete source information.

On each full-time strip Q, compute complete four-jet intervals V_j. Form the complete interval L_Q=V_2²-V_1 V_3. If the complete first-jet rectangle misses the closed radius-r disk, its compact integral is zero. Otherwise use rho(F) in [0,C] and the full outward product interval [0,C] L_Q. Multiply by the exact strip area and sum outward. No division by E or interior lower bound occurs in the uncertain-support estimate. Whole-cell range integration already includes quadrature uncertainty; no midpoint sampling may replace it. Negative interval endpoints are retained even if the simple upper bound loses cancellations.

Start with the full rectangle. Refine a strip with largest positive upper contribution by bisection in x. Stop immediately when the complete total upper endpoint is below 3/4; alternatively stop at 4095 four-jet range calls and record inconclusive. The exact consumer needs only an upper bound below 1; the stricter stopping target reserves margin. Source/quadrature setup and boundary certification are separate costs. Before drawing the K conclusion validate |F|>b over the entire boundary without using an interior nonvanishing certificate or boundary winding as an input.

After stopping, diagnose how many retained first-jet rectangles still contain the origin. A positive count demonstrates that the acquired interior information does not already supply a coordinate-separation nonvanishing cover. The proof of the numerical upper bound must not invoke these diagnostic results. Record positive unresolved contributions, accepted cells, full integral interval, boundary floor, counts, derivative work and timings. Compare with the practical full-time coordinate baseline on the identical extended supplier, charging the two extra midpoint jets and four-coordinate evaluation work transparently.

## Control and benefit gates

Distinguish three outcomes: (a) a complete upper bound below 1 that retains an origin-containing interior box answers the user's bounded logical question; (b) a smaller total acquisition/work cost than the practical direct method is a separate comparison benefit; (c) a new theta region or global estimate requires new coverage and is not supplied by this inherited box.

The exact quadratic collision integral remains1 on an enclosing regular domain, so any complete interval estimate must include1 and must not produce an upper bound below 1. Test uncertain-support and inflated-source inputs so they cannot be discarded as zero. Refuse boundary events or a failed boundary floor. Preserve Gaussian corrections and the polynomial real-degree controls from the opening, without counting their successful identities as theta evidence. Apply the [separate arithmetic controls](../../../../result-summaries/12_collision_controls_and_screening.md) with their individual failed theta-source premises; a generic area bound must also remain valid on each matching collision field.

If this budget loses to the direct method, close this specified consumer for comparative benefit without excluding signed/correlated integration or other domains and densities. Active interval treatment here means uncertain support is integrated with a nonzero allowance; it does not claim the actual theta pullback support has become nonempty. Endpoint simplicity and global RH remain outside the comparison.


## Separately fixed wider-cutoff variant

After the first fixed-radius scout, the r=10^-9 largest-upper route was observed to jump from a remaining upper allowance above one directly to zero when its last unresolved cell was separated. That branch does not meet the origin-retention gate; it is not recorded as an active integral success.

A second variant is now fixed, before its execution: **r=10^-7, b=1.5e-7**, all other source/domain/precision parameters and the 3/4 target unchanged. This is a disclosed methodological change, motivated by the r^-2 density amplification and inherited field magnitudes; it is not radius tuning hidden inside the estimator. Acquire a new complete boundary norm floor greater than b by boundary-only range subdivision. Do not import a global interior floor or the known winding into the proof. Use the same 4095-call bulk limit and diagnostics. Record the wider-cutoff boundary cost separately and compare total standalone work with the practical direct method. Its actual pullback support remains potentially empty; the claimed success is an integral bound that carries unresolved interior information.
