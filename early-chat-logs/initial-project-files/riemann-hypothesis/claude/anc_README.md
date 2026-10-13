# Ancillary code for "The zero-sphere program for the Riemann Hypothesis and the Second Involution Conjecture"

Author: Edward B. Baker III (edwardbaker86@gmail.com), August 2026.

This directory contains the complete numerical laboratory certifying every
computational claim in the paper. All scripts are plain Python 3.

## Requirements

    python3 (>= 3.10), numpy, scipy, mpmath, matplotlib

Install with: `pip install numpy scipy mpmath matplotlib`

## Contents

Libraries:

- `xi_lib.py` — the completed zeta function Xi(x) via Riemann's cosine
  transform (with derivatives), the Davenport–Heilbronn function Xi_DH,
  the Laguerre detector L1, and the l-graded sector energies E_l.
- `explicit_formula.py` — the Guinand–Weil explicit formula in rotated
  coordinates on the Gaussian test family h_{c,lambda}; zero side, prime
  side, archimedean and pole terms; Z(c,lambda).
- `si_lib.py` — the Second Involution laboratory (paper §§8–9): Z(c,lambda)
  on both sides at sigma=1, lambda*=log 2; the windowed reality defect D(c);
  the Fourier–Bohr coefficients B_n of the prime part of F(c)=Re Z(c,log 2).

Drivers (each prints its certification and is independent of the others):

- `run_validation.py` (~5 min) — certifies the extension and the DH control:
  cosine-transform Xi vs mpmath xi to <= 8e-10 relative (1e-14 for x<=20);
  Xi vanishing at the first ordinate to the quadrature floor; Xi_DH real and
  even to 1e-16 relative; the three classical DH off-line zeros recovered by
  Newton iteration (spheres (a, y0) = (85.699348, 0.308517),
  (114.163343, 0.150830), (166.479306, 0.074356), matching Spira); the DH
  on-line ordinates in [74, 97] by bisection.  [Paper §5]
- `run_experiments.py` (~4 min) — Laguerre positivity for Xi (min relative
  margin 0.173 on [0,52]); L1[Xi_DH] < 0 exactly inside the predicted windows
  |x-a| < y0 at the first two DH spheres, positive on the control stretch
  [78,82]; sector-energy scaling E_l ~ y0^{2l} (log–log slopes
  2.000/4.000/6.000 for l=1,2,3), E_1 = 0 exactly on real ordinates, and the
  per-sphere E_1 values for the three DH spheres. Produces `lab_results.pdf`.
  [Paper §6]
- `run_bridge.py` (~3 min; ~2 min extra on first run to compute and cache
  250 zeros in `zeros.pkl`) — certifies the explicit formula on the Gaussian
  family at five (c,lambda) configurations to 1e-8..1e-10; the rate
  experiment (zeta flat at rate -0.0003; DH with its first sphere at fitted
  rate 0.3085 vs true 0.30852); the Gegenbauer identity
  sinh(2z)/2z = sum (2l+1) i_l(z)^2 to 3e-14. Produces `bridge_results.pdf`.
  [Paper §7, Theorem F]
- `run_si_check.py` (~2 min; requires `zeros.txt`, see below) — the Second
  Involution certifications: (V1) zero side vs prime side of Z(c, log 2) to
  2.7e-14 at c in {30, 100, 250, 500}; (V2) uniform oscillation of
  F = Re Z(., log 2): min osc >= 2.01 over 32 windows spanning [0,1160] and
  osc = 2.89/3.25/2.49 at c = 1e4/1e5/1e6 from the prime side, against the
  proof's effective bound B2/8 = 0.0676; (V3) the adaptive-encoding theorem
  end to end on a synthetic Euler-product-free multiset carrying the
  conjugate quadruple ±100.0745 ± 0.25i: the defect (sup D = 0.125) is
  recovered from two samples to worst error 1.8e-15, with correct zeros in
  the defect-free regions. Prints ALL PASS.  [Paper §§9–10: the
  adaptive-encoding theorem and the uniform oscillation lemma; note the demo
  uses the comfortable windows [c-15, c+15] with empirical r = 2 and the
  variant encoder, as stated in the paper's numerics section §11.]
- `make_zeros.py` (~5 min) — regenerates `zeros.txt` (the first 800 positive
  zero ordinates at 25 digits via mpmath.zetazero). A precomputed copy of
  `zeros.txt` is included, so this only needs to be run to re-derive it from
  scratch.

Data:

- `zeros.txt` — first 800 positive ordinates of the zeta zeros, one per
  line, 20 significant digits (input to `run_si_check.py`; regenerate with
  `make_zeros.py`).

## Reproducing everything

    python3 run_validation.py
    python3 run_experiments.py
    python3 run_bridge.py
    python3 run_si_check.py      # uses the included zeros.txt

Total runtime is roughly 15 minutes on commodity hardware. Every number
quoted in the paper's numerics sections appears verbatim in the output of
exactly one of these scripts.
