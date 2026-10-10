# Analytic checkpoint

This scout is analytic. No theta quadrature, spectral-gap computation,
or numerical zero search is claimed. Equations (7), (9), (10), and
(11)--(12) in the first note are the checkable outputs.

Any future gap computation must certify the infinite-line tail, operator
domain, spectral ordering, and parameter dependence. A finite matrix
eigenvalue alone is not a lower bound for \(\lambda_t\). No dataset was
generated; repository large-file rules therefore require no archive.

## Conditional continuation

    python3 /absolute/path/to/03_susy_dirac_hodge/numerics/check_conditional_score.py

This checks three exact conditional polynomial identities and encloses
the genuine theta score residual on two intervals, uniformly in
\(0\le t\le1/20\). It uses the source-bound moment enclosure in
15_lee_yang/numerics/theta_spin_screen_record_20261010.json, verifies its
source hash, and fails closed if that input is absent.

Replay on 10 October 2026 passed. The beta interval is contained in
(86.39010,86.56254); the optimized Fisher defect is strictly greater
than 0.00012. The output record is bound to the checker and input record.
These are shell/bulk certificates with analytically paid theta tails,
not collision signs or zero-free certificates.
