# Internal review of paid dual kernels and moment-relaxation loss

10 October 2026. GPT-6 (Codex); exact serving variant and configured
reasoning effort unavailable. This is internal LLM review, not independent
mathematical validation.

Reviewed [Note 3](../notes/3_PAID_DUAL_KERNELS_AND_ACTUAL_FREQUENCY_RELAXATION_LOSS_20261010.md),
its [checker](../numerics/check_paid_dual_kernels.py), and
[source-bound record](../numerics/paid_dual_kernel_record_20261010.json).
Earlier notes and checkers are preserved.

The dual coordinates are exactly `X_0` and `Z_1=Y_1+(d/c)X_1`.
The first-derivative candidate bounds `Z_1` by
`(L+|A|) eta_N/(2c)`; replacing it by zero or by `Y_1=0` would lose
the drift. The modification `e^T Lambda e+2e^T B u` pays all square,
mixed, and higher-moment cross terms. The sufficient negative bound
includes that payment and the full measured `widehat Delta/(4c^6)`;
the latter retains `E_j`, `j! L^j eta_N`, and exact `gamma`.

The pair derivation was checked independently by expanding products of
the real features. `D_s=(C_mn-C_nm)/2` has the required sign. It is
antisymmetric, and its difference sine factor is also antisymmetric, so
the complete ordered-pair contribution generally survives. Both sine
terms are necessary for nonzero generic dual coefficients. Grouping by
reduced ratio and divisor product retains the same actual height and
every diagonal and block/complement pair. The finite regrouping tests
use powers of one common unit-complex frequency, rather than independent
prime phases. Their logs are formal exact scale coordinates; no huge
height is inferred from them.

The Hilbert construction retains the prescribed weights and actual
phases in `G,C,F,H`. The projection of `1` has squared norm
`1-z^T G^{-1}z`; Cauchy--Schwarz yields
`(m-v)(m-v)^T <= E H` in positive-semidefinite order. The subsequent
norm-ball optimization enlarges the *constant coefficient vector* to
arbitrary real Hilbert vectors. Those vectors need not be positive
coefficient states and are not asserted to be actual orbit states.
When `H>0`, congruence preserves the inertia `(2,1)` of `Q_*`;
its `2 x 2` determinant is `-9/4` for every normalizer. The sharp
relaxed maximum is therefore positive. Singular Grams require projection
onto their range; the note states that exception explicitly.

The actual-height rank certificate is stronger than a formal check.
At `N=22066`, `kappa=1`, `t=1/(2 log N)`, `x=4 pi N^2`,
five selected actual nodes have a certified positive feature determinant
between `155000000` and `156000000`, of width less than `1e-30`.
The complete positive-weight Gram is consequently positive definite,
as is its Schur complement. This height is a genuine finite arithmetic
state, not a candidate. It establishes that the scoped norm-relaxation
loss is present for genuine data at that state, without asserting it
at every candidate or throughout the sector.

Interval arithmetic imports Program 13's unchanged
[check_block_current.py](../../13_microlocal_phase_space/numerics/check_block_current.py).
The own checker binds its SHA-256 and fails before import if it changes.
It locally overrides integer interval powers with exact `Fraction`
endpoint powers and outward Decimal division. This avoids relying on
the general `Context.power` correct-rounding guarantee; the imported
source stays unchanged. The determinant endpoints are unchanged by this
strengthening of the enclosure provenance.
The formulas use the same analytically reduced carrier, exact time and
height, `mu=Omega/c`, and drift. Determinant summation uses outward
Decimal intervals over all 120 permutations. Positive prescribed
weights suffice for rank; no full Gram quadrature is silently claimed.

The coefficient control at `T log 2=(2k+1)pi` preserves the actual
carrier for *every* angle. Its coefficients are deliberately changed
to `1,2,1`, with other indices initially zero. `M_0=M_1=0` gives both
exact finite candidates for any amplitude drift. The positive threshold
formula requires `mu!=log 2` and `Gamma<3 log^2 2`; it is uniform over
the carrier. Fixed reweighting of actual summands yields the local
factor `(1+r)^2`, so the raw multiplier convention is retained. The
full-support perturbation is valid only when its displayed two-column
determinant is nonzero and at fixed finite cutoff. It is not a small
perturbation of the prescribed complete coefficient vector, nor a
genuine heat collision, nor an all-real entire-function control.

The retained checker passes **495 exact assertions** and the actual
interval rank assertions. A fresh replay reproduces the record byte for
byte. Local links, math delimiters, and source sizes were checked. No
new negative signed arithmetic estimate is certified. Independent
specialist validation, higher multiplicity, and endpoint coverage remain
open; the useful new checkpoint is the paid dual criterion (5).

A second internal LLM agent independently rederived the dual signs,
Gram-ball optimum and control scope. It found no algebraic issue and
identified the imported integer-power guarantee concern, which the local
override above addresses. This extra internal check is not independent
human mathematical validation.
