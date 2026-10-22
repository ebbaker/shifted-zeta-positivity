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
