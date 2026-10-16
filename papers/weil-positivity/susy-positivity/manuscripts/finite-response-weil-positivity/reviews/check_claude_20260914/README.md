# Independent checks for review_claude_20260914.md

New implementations (numpy / scipy / mpmath / sympy); nothing here imports the paper's
or the earlier review's scripts. Run from this directory with Python 3:

    python3 chk1_explicit_formula.py        # normalization of Q_L against 300 zeta zeros (~3 min; zeros cached in zeros_300.json)
    python3 chk2_boundary_identity.py       # kernel image sum, column/entry formulas, tails, shift and pole entries (~10 min)
    python3 chk2b_boundary_identity.py      # T_L = b(H_N) + K_L on sin^4(pi x/L) at L = 1, 1.3, 2.5 (~2 min)
    python3 chk3_operator_and_schur.py      # cosine-basis assembly of W_L; prime/pole bounds, cutoff, parity, Galerkin enclosures, S_1 and S_2 (~5 min)
    python3 chk4_highprec_spectrum.py       # 50-digit spectra of W_K, S_1, S_2 (~2 min)
    python3 chk5_rational_and_asymptotics.py# exact Fraction checks of Sections 12-13, tail constants, asymptotics (~5 s)
    python3 chk6_nearnull_mechanism.py      # zero sums and Fourier concentration of the near-null eigenvectors (~5 s; reads chk3 source)

`*.out` are the transcripts of the runs recorded in the review; `*.json` the machine-readable
results; `results_summary.json` collects them. Everything is a diagnostic or an exact rational
identity check, not an interval-arithmetic certificate. Compression eigenvalues are upper bounds
for the true ones; double-precision eigenvalues below 1e-14 are noise (the mpmath values are not).
