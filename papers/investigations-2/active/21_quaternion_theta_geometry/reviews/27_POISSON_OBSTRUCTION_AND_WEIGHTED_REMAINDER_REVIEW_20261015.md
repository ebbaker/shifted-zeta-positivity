# Poisson splitting obstruction and weighted remainder review

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This is an internal LLM review with separate parallel derivations and a coordinating audit, not external peer review or formal verification.

The continuation from Note 37 yields one exact arithmetic identity, a rigorous rejection of its unrenormalized global axis/mixed split, a sharper existing weighted-remainder bound, and six fresh bounded stationary observations. The finite sign coverage and proved outer threshold are unchanged. No blocking mathematical finding remains in the reviewed claims below.

## 1. Exact Poisson identity and the rejected split

[Note 38](../notes/05_theta_correlation_kernels/38_POISSON_PARITY_CORRELATION_AND_HEAT_OBSTRUCTION_20261015.md) was independently checked for the parity-coset substitution, Gaussian scaling, phase factor, chain-rule operator, and heat multiplier. The primitive identity is derived from the complete theta product using ordinary [Poisson summation](https://dlmf.nist.gov/1.8.E14). Its differentiated Gaussian series converges normally on compact coordinate domains. This justifies local termwise derivatives, not global termwise heat integration.

The axis source has leading tail \((9/8)e^{-10|r|}\), uniformly for bounded \(s\); the mixed source has its negative. The complete source has superexponential decay. Multiplication by \(e^{2t(s^2+r^2)}\) makes each separate axis/mixed correlation diverge for every \(t>0\). This analytically rejects the proposal to regard those sectors as separate finite global kernels. It says nothing adverse about the sign of their complete sum. Merely adding the zero-mode counterterm transfers an integrability problem to the other coordinate.

The audit checked the exact exterior constants, the positive-half-line source envelope, and all ordered integration-by-parts edge terms. The finite-box signed remainder retains the complete unsplit exterior. Its zero-loss rule is a declared test target, not a proved energy-relative estimate. The original staircase and both full stationary conditions remain required for the existing hybrid transfer theorem.

[The checker](../numerics/check_poisson_parity_heat_obstruction.py) passes 27 exact-algebra or sensitivity assertions and 12 independent primitive-identity ball comparisons at 256 bits. Both lattice evaluations include proven Gaussian tails; an omitted parity factor fails the origin comparison. A separate agent replayed the checker and reviewed the proof. These finite checks support the implementation; the analytic tail proof establishes the global obstruction.

## 2. Weighted remainder refinement

[Note 39](../notes/01_weighted_outer_remainders/39_CONVEX_DYADIC_WEIGHTED_REMAINDER_AUDIT_20261015.md) improves the existing high-index remainder from
\(O_r(\ell^{r+1}e^{-\ell/20000})\) to
\(O_r(\ell^re^{-\ell/20000})\), on the same discs and domain.

The proof preserves each interval's strict convexity before summing the dyadic grid. The extra endpoint-distance factor is summable by two geometric series per interval, uniformly for shifted grids. The possible sole grid point above one half is paid separately. Shortened blocks and blocks crossing a partition boundary remain controlled by the imported maximal-interval estimate. The comparison with the fixed boundary theta is uniform even when the physical theta grows.

The explicit geometric multiplier is less than \(962773/671<1435\). This multiplier does **not** evaluate the common imported constant \(C_r\). The low-index \(O(\Gamma/L)\) error remains, and no effective starting height is obtained. The exact five-pair bottleneck and its obstruction interval at theta five halves concern those majorants, not lower bounds for the actual exponential sum.

[The rational checker](../numerics/check_convex_dyadic_weighted_remainder.py) passes 129 assertions. A separate reviewer checked the infinite-sum argument and independently replayed those assertions. The new claim is the removal of the block-count factor, not a newly proved lower theta threshold. The crossover value already present in Note 32's checker is credited as prior evidence.

## 3. Fresh full-stationary baseline

[Note 40](../notes/03_effective_bridge/40_FIXED_THETA_STATIONARY_BASELINE_20261015.md) and [its driver](../numerics/certify_theta_stationary_baseline.py) were audited for the exact curve \(t=\theta/\log(x/(4\pi))\), the positive sign of the heat contribution in its derivative, and the need for \(h_4\) on the second stationary set. Endpoint sign changes and monotonicity certify exactly one root in each of the six **final** brackets; uniqueness throughout each initial one-unit search window is not claimed.

The run uses fresh complete-source quadrature, not values copied from an earlier certificate. Source tails and integration tails are both paid, as are spatial and temporal Taylor remainders. Centers use jets through order 17, complete moment bounds through order 18, and constant normalization across each rectangle. Endpoint normalization varies only by a strictly positive factor used for signs. The frozen coefficient is zero for both observations; there is no energy quotient.

All six stationary products are strictly positive at theta values one half, three quarters, and one. These are bounded baseline results inside the old height cover. The known starting neighborhoods are disclosed; they are not presented as an independent holdout of that older certificate. The rejected Poisson split has no numerical verdict because its required integrals are not defined. The finite-box transformed contributions also remain unevaluated.

## 4. Accepted scope and remaining work

Accepted incremental results are the exact parity identity, the positive-time global-sector obstruction, the logarithmic-factor removal, and the six certified baseline roots. Their scripts and small execution receipts are saved under `numerics/`; this review and the [continuation](../notes/00_research_coordination/41_POISSON_OBSTRUCTION_AND_REMAINDER_CONTINUATION_20261015.md) preserve the distinctions between those results.

The missing theorem is still a source-prescribed energy-relative signed bound on both full stationary sets, or the established all-cutoff logarithmic alternative, with local boundedness through covered finite positive-time collisions. A replacement Poisson mechanism must first preserve the cancellations needed for integrability in all joint source directions, then specify its signed budget and coefficient rule before a fresh mechanism pilot. No manuscript revision, new snapshot, enlarged sign domain, effective bridge, or RH conclusion is asserted.


The [continuation validation receipt](../numerics/POISSON_CONTINUATION_VALIDATION_20261015.json) binds these notes and scripts, verifies stored script/dependency hashes, replays all six endpoint and signed-product interval claims with exact rationals, and checks agreement with the independent runs. It also checks the local links and sub-1-MiB file policy. Hash identity is provenance, not a mathematical proof.
