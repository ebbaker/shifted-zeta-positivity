# Continuation after the v0.2 review

9 September 2026. The previous `log(7)` target is completed. Begin with the
v0.2 manuscript, `REVIEW_20260909.md`, `STATUS.md`, and `numerics/README.md`.
The original guide is preserved under `numerics/background/ORIGINAL_CONTINUATION_WEIL_DEPTH_20260909.md`.

## Established results

| Total horizon | Central floor | Maximum shift | Decay coefficient |
|---|---:|---:|---:|
| `9/5` | `1e-26` | `3e-14` | `5e-27` |
| `log(7)` | `1e-34` | `3e-18` | `5e-35` |

Each row means `Q_(0,L) >= m I` and `||V_(omega,L)|| <= exp(-decay*omega)`
through that horizon and shift interval. Reflection has lower bound
`1-exp(-decay*omega)` and cumulative storage has lower bound
`1-exp(-2*decay*omega)`. Compression covers all shorter horizons. Retain the
stronger first row where it applies.

Both cases pass a full direct-Arb construction and a separately written
implementation with a different reflection-moment assembly. All head/full-Gram
entries overlap; independently saved Schur matrices replay. This is a
machine-assisted record, not human or formal verification.

## Exact conventions and the completed calculation

`L` is total input length, the centered input is `(-L/2,L/2)`, autocorrelation
support is `[-L,L]`, and Suzuki's cutoff is `a=exp(L/2)`.
At `L=log(7)` the 7-delay is zero almost everywhere. Generator indices are
2,3,4,5; the transfer includes 6; reflected ordered pairs are (2,2), (2,3), (3,2).

The proposed initial parameters succeed: `N=128`, `M=220`, 1792 bits,
floor `1e-34`. The tail floor exceeds `0.60748624181467`; profile error is
below `9.342e-42`; total analytic Schur error is below `3.737e-37`.
Both 64-dimensional LDL tests pass. Diagnostic required tail floors are
about 0.59479118 and 0.58991735, close to the available floor. These
floating-point diagnostics do not decide positivity.

The new generator constant is `C_log7 < 13.541169 < 14`.
The exact continuation check is
`1e-34-(14/3)*(3e-18)^2 = 5.8e-35 > 5e-35`.
The old `C<11` is not valid at the new endpoint.

## Next experiment: log(8)

1. Start with a new output directory and a prospective tail/profile/error
   budget. Generator indices will be 2,3,4,5,7; endpoint delay 8 vanishes.
   The builder accepts `0<L<3`, which does not imply positivity there.
2. Choose a target floor and profile degree from the new budget. Do not assume
   `N=128` or `M=220` suffices. Inspect relative coupling before enlarging N;
   increase profile degree for analytic error and precision for ball uncertainty.
3. Implement the paper's proved smaller leakage error
   `epsilon_r=(abs(a-m)+2*kappa_r)*eta+eta^2`, with a checked upper bound
   `kappa_r >= ||(I-P) Q_tilde P_r||`. An outward upper bound on
   `sqrt(trace(E_r))` suffices. Compare on both certified cases first.
   Existing certificates retain the conservative error with coefficient 40000.
4. After a complete pass, derive a new horizon-specific continuation bound.
   The revised analyzer can use explicit rational inputs or choose a conservative
   shift. Preserve matrices, hashes, complete pivots, trace and remainder checks,
   and an independent comparison.

## Recursion strategies

The paper now factors the complete new defect for `V=[[X,0],[Y,Z]]`.
With invertible old and appended defects, the decisive normalized coupling is
`C=(I-ZZ*)^(-1/2) Y (I-X*X)^(-1/2)`. Contraction is equivalent to `||C||<=1`;
strict inequality supports the next inverse-based update. The missing theorem
is an arithmetic estimate that preserves this condition at successive depths.
Retain full defect factors and input/output maps. The paper gives an exact
counterexample showing that equal old minimum eigenvalues can yield opposite
update signs when coupling meets different directions.

The degree-space alternative inserts a finite buffer before the far tail.
Two Schur eliminations retain the cross-Gram between head-to-tail and
buffer-to-tail columns. With the same scalar tail floor, this reorganizes the
existing larger-head test; a stronger estimate requires a proved structured
tail lower bound or sharper remainder control.

For longer horizons, validated Taylor/Chebyshev pieces can replace one
origin-centered gamma profile. Keep the logarithmic kernel exact and account
for every new piecewise-polynomial breakpoint and reflected overlap. This can
address the radius-3 model restriction; it does not establish coercivity.

## Open qualifications

- No central certificate beyond `log(7)` is asserted here.
- No storage induction from the preceding slab alone has been proved.
- The diagonal all-depth implication is valid, but the required infinite
  sequence has not been constructed. No RH or zero-free-region result follows.
- The earlier second-slab shift gap and primary-Arb first-slab audit remain
  separate unresolved tasks.
- Candidate weak vectors, NumPy eigenvalues and quadrature controls are
  diagnostics. Sign decisions require Arb matrix enclosures, the infinite-tail
  proof and the analytic profile remainder.
