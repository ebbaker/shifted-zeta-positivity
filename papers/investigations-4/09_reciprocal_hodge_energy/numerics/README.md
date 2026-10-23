# Numerical records

22 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance; gpt-6.1-sol (Codex), effort ultra, verified from the setup turn metadata.

A small [standard-library diagnostic](01_quadratic_cut_diagnostic_20261022.py) and [receipt](01_quadratic_cut_diagnostic_20261022.json) evaluate the analytic quadratic calibration at four fixed ratios. They check signs and boundary normalization using floating arithmetic; there is no theta acquisition or certificate. The receipt records the script SHA-256 and Python version. Acquire data only after RHE-01's declared comparison. Save small reproducible scripts/receipts, including normalization, all tails, rounding, hashes and actual model/effort. Distinguish floating diagnostics from certificates and follow [LARGE_FILES.md](../../../../LARGE_FILES.md).

The [second diagnostic](02_coupled_energy_diagnostic_20261022.py) and [receipt](02_coupled_energy_diagnostic_20261022.json) use an exact heat cubic with a nonconstant factor. They compare full smooth-cover integration, real boundary reduction, separate cut/physical payments, model remainders and the sharper upper. These remain floating checks, not theta acquisition or certified quadrature.

The [actual-theta replay](03_compare_actual_theta_fiber_20261022.py),
[canonical source/cell core](rhe_actual_theta_core.py),
[root/count contract](rhe_actual_theta_contract.py),
[fixed comparison contract](03_ACTUAL_THETA_COMPARISON_CONTRACT_20261022.md)
and [small receipt](03_ACTUAL_THETA_COMPARISON_20261022.json) implement one
t=0 disk center 35 radius 8 comparison with outward Arb balls. Requires
Python and python-flint 0.9.0 (recorded FLINT 3.6.0). Run the comparison
script with an interpreter providing that package; it imports its sibling
modules and prints a fresh JSON record. Every source/root/branch/cell
test is rerun. Timings need not reproduce exactly; hashes identify sources,
and replayed arithmetic decides the signs. No external data archive is needed.

The standard-library [weighted algebra check](04_check_weighted_algebra_20261022.py) and [small receipt](04_WEIGHTED_ALGEBRA_CHECK_20261022.json) verify source-derivative polynomial coefficients and rational constants for Notes 06 and 08. Replay with `python3 04_check_weighted_algebra_20261022.py --output /tmp/rhe-weighted-algebra.json`. This is an exact algebra diagnostic, not a source acquisition, full theorem certificate or numerical integral enclosure. Prepared for Edward Baker with substantial LLM assistance; gpt-6.1-sol, effort ultra.

[Transfer algebra check](05_check_transfer_algebra_20261022.py) and [receipt](05_TRANSFER_ALGEBRA_CHECK_20261022.json) verify signed quadratic fixtures, the nonzero cosine-jet bottom-normal sign, a modulus Green identity, cutoff coefficients and the Taylor-tail ratio. Replay with `python3 05_check_transfer_algebra_20261022.py --output /tmp/rhe-transfer-algebra.json`. These finite exact checks do not acquire a theta sign or certify the analytic limits. gpt-6.1-sol, effort ultra.

The [fixed canonical bulk-lower contract](06_CANONICAL_BULK_LOWER_CONTRACT_20261022.md), [script](06_certify_canonical_bulk_lower_20261022.py) and [receipt](06_CANONICAL_BULK_LOWER_20261022.json) acquire M_phi>5.37865e-6 for the unchanged t=0 xi/8 field on D(35+2i,1), reusing the complete degree64 source oracle. One192-bit python-flint0.9 setup and no area quadrature; no physical jet floor or trace sign is acquired. Replay with an interpreter providing python-flint: `PYTHONDONTWRITEBYTECODE=1 python3 06_certify_canonical_bulk_lower_20261022.py --contract 06_CANONICAL_BULK_LOWER_CONTRACT_20261022.md --output /tmp/rhe-canonical-bulk-lower.json` from this folder. [Review 07](../reviews/07_CANONICAL_AMPLITUDE_AND_BULK_LOWER_REVIEW_20261022.md) records exact equality of26 receipt fields in a separate same-model replay. Prepared for Edward Baker with substantial LLM assistance; gpt-6.1-sol, actual effort ultra.

The signed potential has its own [fixed contract](07_SIGNED_POTENTIAL_CONTRACT_20261022.md), [script](07_certify_signed_potential_20261022.py) and [receipt](07_SIGNED_POTENTIAL_20261022.json). Its first128x64 mesh passes, preserving signed kernel moments and paying all polynomial/source errors. A separately declared [whole-rectangle bulk contract](08_WHOLE_RECTANGLE_BULK_CONTRACT_20261022.md), [script](08_certify_whole_rectangle_bulk_20261022.py) and [receipt](08_WHOLE_RECTANGLE_BULK_20261022.json) reuse exactly those cells to strengthen the lower and acquire an optional upper from proved local floors. Their combined positive trace is wider than the [direct1024-cell reference](07_DIRECT_TRACE_REFERENCE_20261022.json), whose [contract](07_DIRECT_TRACE_REFERENCE_CONTRACT_20261022.md) and [portable script](07_direct_trace_reference_20261022.py) retain complete source and denominator payments. [Note15](../notes/15_SIGNED_CANONICAL_POTENTIAL_AND_COMPLETED_TRACE_20261022.md) and [Review08](../reviews/08_SIGNED_POTENTIAL_AND_TRACE_REVIEW_20261022.md) give proofs, exact replay and scope. Prepared for Edward Baker with substantial LLM assistance; gpt-6.1-sol, actual effort ultra.

Replay from this folder with Python providing python-flint0.9 (set PYTHONDONTWRITEBYTECODE=1 if desired):

```sh
python3 07_certify_signed_potential_20261022.py --contract 07_SIGNED_POTENTIAL_CONTRACT_20261022.md --bulk-receipt 06_CANONICAL_BULK_LOWER_20261022.json --output /tmp/rhe-signed-potential.json
python3 08_certify_whole_rectangle_bulk_20261022.py --contract 08_WHOLE_RECTANGLE_BULK_CONTRACT_20261022.md --potential-script 07_certify_signed_potential_20261022.py --potential-receipt /tmp/rhe-signed-potential.json --output /tmp/rhe-whole-rectangle-bulk.json
python3 07_direct_trace_reference_20261022.py --contract 07_DIRECT_TRACE_REFERENCE_CONTRACT_20261022.md --output /tmp/rhe-direct-trace.json
```

Potential and bulk arithmetic receipts replay identically in the recorded environment; direct timing fields vary. Compact Arb decimal displays can show coarser printed radii than the internal balls; exact rational endpoints are the reporting bounds. Hashes identify inputs, while the complete ball inequalities decide the estimates. No new geometry, adaptive scan, negative theta witness or method-cost dominance.
