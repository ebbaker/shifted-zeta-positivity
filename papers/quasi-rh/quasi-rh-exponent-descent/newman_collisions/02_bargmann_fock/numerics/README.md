# Exact algebra checkpoint

Run from any directory:

    python3 /absolute/path/to/02_bargmann_fock/numerics/check_fock_gram.py

The standard-library script checks the normalized Gram determinant,
matrix inverse, and projection quadratic form at rational widths and
heights using exact fractions. It does not evaluate theta moments or
certify a zero-free region. The analytic norm and tail proofs are in the
scout note. No generated dataset or library dependency is required.

Replay on 10 October 2026: PASS, 9 exact rational Gram/inverse/projection
cases. This validates the finite algebra, not the analytic theta proof.
