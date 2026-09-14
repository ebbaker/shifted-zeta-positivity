# Continuation handoff

As of 10 September 2026. Read the manuscript for the unified argument and
CLAIMS.json for the exact record mapping.

## Fixed conventions

Working Weil-depth v0.3 at commit
a566944dc1be2899e37fce3d0e857516ced33d8f. Total input length L, centered support
(-L/2,L/2), multiplicative cutoff exp(L/2), unweighted L2, and the Fourier
convention in manuscript Section 2. A delay at equality with the horizon vanishes.

The author's normalization audit is separate and in progress. Do not promote
these working results to an audited normalization or RH proof. Do not replace
the reference builder with current upstream code without checking conventions
and revalidating all affected results.

## Established state

1. Exact hyperbolic generator identity and sufficient variable omega*kappa_L.
   The relative block inequality transports this state through a successful
   step. Elementary local extension can require exponentially tiny increments.
2. Cumulative storage and its exact reflection-preserving Cayley congruence;
   equality of the normalized spatial coupling norms; signed Schur criterion
   for simultaneous depth and positive-shift changes.
3. One exact degree-126 even polynomial has negative generator energy at
   (log7,1e-11) but positive cumulative storage, with full output retained.
4. At log8, cumulative positivity on 128 old plus 32 new polynomial inputs.
   The full central coupling has a LOWER witness c^2 > 1-1.84e-17.
   Neither statement proves unrestricted log8 positivity.
5. At a=log7, h=log(8/7)/4, Lq=(3/4)log14, the original exact rational
   continuation J_128,32 has residual factor .004 on the 128 old modes,
   allowing every new form-domain input.
6. Extending the same J by zero, the direct all-old test gives
   R*F^-1R <= .9 H_J and S >= .1 H_J. The full two-input energy is at least
   (1-sqrt(.9)) times H_J[f]+F[g-Jf], hence at least .05 times that sum.
7. A separate sign test on the spatial matrices gives Q0,Lq >=1e-33.
   It yields contraction for 0<omega<=5e-18 and all L<=Lq, with
   D >= (1-exp(-1e-33*omega)) I.
8. The earlier separate global method at L=1.98 gives floor 1e-31 and
   safe shift <=5e-17. It was not used to justify the spatial tests.

## Exact state to carry

- Completed length Lq=(3/4)log14, first increment from a=log7.
- Active generator prime powers: 2,3,4,5,7; full transfer also includes 6.
- J: rational coefficients in numerics/history/quarter-step-20260910/
  residual_128_32.json, extended by zero outside the old 128 modes.
- Verification head: 256 old plus 32 new modes; J itself remains 128-to-32.
- Profile degree 320; exterior-log degree 100; precision 6144 bits.
- Exact 512-cell arithmetic weight: norm <1.949177212012646.
- Separate partition verification: all 2,152 intervals.
- Joint complement floor >.90675864277213.
- Modified complement floor at theta=.9 >.76166054904193.
- Final errors <1.026e-55 (absolute) and <6.253e-53 (relative).

The carried metric is H_J, not A. The .1 factor does not retain 10% of A.
The .004 factor has only finite-old coverage; the full-domain factor is .9.
The .9 central factor has not been transferred directly to positive-shift
Cayley storage.

## Next experiment

Attempt another increment log(8/7)/4 beginning at Lq. This is a proposed
experiment, not a certified future step.

- Parameterize geometry in a NEW working copy. Current closure scripts fix
  the first quarter-step geometry.
- Propose a new Galerkin continuation and save exact rational coefficients.
  Endpoint matching may reduce leading logarithms, but integrate the actual
  remaining endpoint residual rather than assuming cancellation.
- Recompute active arithmetic thresholds, translated support intersections,
  disjoint-window conditions, gamma profile domain, and both tail floors.
- Retain separate old/new full-output Grams; they are needed for the enlarged
  cross-block leakage calculation.
- Test theta<1 directly in the graph form. A positive complement floor alone
  is insufficient: include all leakage back to the verification head.
- Insert any proposed absolute floor before the Schur sign test. LDL pivot
  magnitudes are not spectral floors.
- Give changed sources/results a new packet and new hashes; retain history.
  Keep all generated matrices external with dual hashes.

For a later direct cumulative test apply the same residual algebra to P_omega
at positive shift and use the finite comparison between two positive shifts.
Do not assume a bounded O(omega^2) difference P_omega-Q0: P_omega is bounded
while Q0 is unbounded.

## Remaining obligations

- Independent normalization verification of Fourier form, gamma generator,
  delay coefficients, and transfer evolution, coordinated with the author.
- Independent review of the new complement and error estimates, and an
  independent full 256-plus-32 matrix reconstruction. Package-time sign replays
  reuse saved matrices and do not discharge this obligation.
- The remaining quarter-steps to log8 with unrestricted inputs.
- Unrestricted cumulative contraction at omega=1e-11, including old depth log7.
- Quantitative control of successive transported metrics and residual factors,
  with step lengths whose sum diverges while shift tends to zero.
- Control of required verification dimensions at successive depths.

The initial 128-plus-32 closure failed a sufficient test and is retained with
its original source snapshot. It is not a negative witness for the actual form.
No shift monotonicity, unique critical curve, or all-depth recursion is proved.

## Required files

Argument review: manuscript, the five historical notes, CLAIMS.json.
Direct .9 replay: all small code/records and the spatial matrix archive only.
Spatial reconstruction: all small files; old 256-mode cache is optional.
Failed historical attempt: old 128-mode cache is optional.
A fresh rebuild requires no external matrix data.

ARCHIVES.md supplies setup, regeneration, hashes, and data-copy instructions.
The package is complete as sources and parameters; Python dependencies and
LaTeX must be installed separately.
