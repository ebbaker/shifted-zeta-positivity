# RTD-01: fixed first comparison contract

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Coordinating model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**, verified from current turn metadata. This contract is recorded before the new comparator run; the inherited pilot and its replay were already inspected.

## Classification and scope

This is a finite estimator comparison on an already certified theta rectangle. It is not an RH criterion, new exclusion region, or endpoint simplicity estimate. Follow the [result index](../../../../result-summaries/README.md), [local-geometry cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../avoid/README.md), [reformulation rule](../../../../avoid/01_restating_the_target.md), [scoped-exclusion rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [known-coverage warning](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md), and [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md).

Use the unchanged physical source and the supplier/tail proof in [Investigation 22 Note 06](../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md). Domain, precision and information are fixed:

- D=[1/100,1/5] x [25,45], orientation dt wedge dx; midpoint (21/200,35).
- 160-bit Arb; modes n<=4, source cutoff u=1, complete omitted-mode and u>=1 tails.
- Spatial Taylor degree 50, time degree 12. First-jet supplier: midpoint jets through 75, moment remainder through 77. No tail is discarded.
- Support radius r=10^-9; collar radius b=3/(2*10^9). Validate |F|>b on the complete boundary. These radii will not be tuned after comparison.

For s=|y|^2/r^2, let g(s)=exp[-s/(1-s)] for 0<=s<1 and zero for s>=1. Choose the fixed smooth density

\[
\rho_r(y)=\begin{cases}
\dfrac{g(s)}{\pi r^2(1-s)^2},&s<1,\\
0,&s\ge1.
\end{cases}
\]

It is nonnegative, smooth, supported in the closed radius-r disk inside B_b, and has integral one since -g'(s)=g(s)/(1-s)^2 and g(0)=1. Density amplitude and gradient scale as r^-2 and r^-3 respectively; no numerical normalizer is required.

## Consumers and payments

Run the inherited complete boundary winding with its practical polygon implementation and the adaptive full-time interior-strip baseline. Do not introduce an artificially expensive two-dimensional baseline. All consumers share exactly the same first-jet information, tails and interpolation uncertainty.

For the compact consumer, enclose the complete first jet on full-time strips, bisecting x. Reject a strip only if its complete range misses the closed target disk. If every strip rejects, rho(F) is identically zero and the signed bulk integral is exactly [0,0]; Hxx and Hxxx, nonlinear multiplication and integration are then unnecessary. The same cells pay a boundary floor if their margins exceed b; charge that work once. Also show the boundary-first accounting if the boundary floor was acquired separately.

If support is encountered or the floor cannot be paid, report the support-only attempt inconclusive rather than silently substituting zeros or changing r. Active-cell integration is a distinct follow-up, needing jets through 77 and moments through 79 at these Taylor degrees, and full cutoff/product/quadrature errors.

Record source setup, individual enclosure counts, accepted cells, full-domain minimum margin, boundary floor, exact or complete interval outputs, and implementation timings separately. Existing baseline evidence is 698 boundary enclosures (464 ranges +234 vertices; optional root cross-checks are additional) and 255 interior ranges. Replay the actual source instead of interpreting a receipt hash as arithmetic proof.

## Success and stop rules

A new exclusion needs a complete upper bound below one and the entire boundary/source contract. A comparison benefit means either a stricter complete allowance or strictly fewer complete first-jet acquisitions than the practical interior baseline on identical coverage. Report arithmetic work and time separately from acquisitions. This is the inherited low-height machinery rectangle, already certified by the inherited pilot and classified within established Polymath/Platt–Trudgian coverage in [prior Review 16, §9](../../../investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) and avoid/11; no new coverage is expected here. For Cartesian range boxes, support rejection already implies coordinate-separation direct exclusion, so a first-jet acquisition gain against that matched rule is ruled out structurally before this run. The run tests implementation and complete cost accounting.

The inherited strip floor already exceeds the chosen support radius. Therefore this is a deliberately bounded implementation/control check with an anticipated support-empty result, not an exploratory search for theta positivity. If the compact result is [0,0] on the same interior cells, close this specified support-rejection consumer as a source of comparative benefit. Do not close active signed integration, other densities or domains.

Controls must recover the exact compact mass one for H=x^2-2t on a regular event-enclosing target preimage and preserve the Gaussian boundary correction: I_lambda=1-exp(-lambda R^2), not one. Check higher finite multiplicity real weights floor(m/2), a collision-free field, and refusal of boundary events. Catalogue the named arithmetic control families and the theta premise each fails; do not pretend a finite theta box contains every control's event. Positive-time coverage misses t=0.
