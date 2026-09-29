# Numerical reconstruction of the boundary mechanical system

`check_mass_stiffness.py` constructs Fourier matrices directly from the prime, pole, and regularized archimedean terms of the Weil distribution in CCM, arXiv:2511.22755v1, equations (3.13)–(3.18) and (5.1)–(5.3). The archimedean contribution beyond the support endpoint is included analytically. Selected matrix entries are also reconstructed from the correlation formula without using the divided-difference matrix assembly.

The program checks the boundary integration map, weighted self-adjointness, the mass/stiffness identity, the finite characteristic determinant, and the normalized Fourier/determinant identity. It records inverse spectral moments including the free Fourier tail. Zeta zeros enter only the final diagnostic comparison, never the matrix construction.

These are exploratory multiprecision computations, not interval certificates. `first_frequencies` lists frequencies of the finite mechanical block. The full spectrum also contains the untouched Fourier frequencies; in particular, the full third positive spectral value can differ from the third finite-block frequency at small cutoffs.

## Reproduction

Use Python with `mpmath==1.3.0` installed in the chosen environment. From this investigation folder:

```bash
python3 numerics/check_mass_stiffness.py
python3 numerics/check_mass_stiffness.py --digits 160 --case 13,24 --output numerics/records/precision_check_160_20260926.json
```

The default run uses 120 decimal digits for `(prime-power cutoff, N)` equal to `(2,4)`, `(5,8)`, `(13,8)`, `(13,16)`, and `(13,24)`. The cutoff is \(X=\lambda^2\), and the logarithmic circle length is \(L=\log X\).

## Small records

- [Primary 120-digit run](records/mass_stiffness_20260926.json).
- [160-digit check of the largest case](records/precision_check_160_20260926.json).
- [Comparison of the 21 saved observables](records/precision_comparison_20260926.json).

The records include input parameters, runtime versions, the program's SHA-256 hash, selected eigenvalues and moments, and reconstruction residuals. Matrices are regenerated and are not saved. Research interpretation is in the [continuation note](../notes/CCM_BOUNDARY_MECHANICS_AND_DETERMINANT_CONTROL_20260926.md).

## Continuation round 2: strings, graph Dirac operators, and cutoff drift

[`check_string_realization.py`](check_string_realization.py) imports the preserved Weil builder and reconstructs the positive mass/stiffness pair. It constructs a string using a specified cyclic force, retaining both the force port `b=e_1` and the displacement port `b=M e_1`. The first bead mass is normalized to one in both cases. Cyclicity is an additional one-string condition: numerical Lanczos breakdown raises an error instead of silently dropping unobserved modes. The note explains the direct-sum construction when cyclicity fails; the program does not implement that restart.

The checks cover both energy congruences, the explicit graph Dirac unitary, the Green kernel, the inverse-square trace as a first mass moment, determinants and port responses, signed fixed-bath residues, and the exact change in both energy forms under Fourier inclusion. It includes passive-interlacing, soft-oscillator, and escaping-mass controls. **No zeta zeros are evaluated by this program.**

Run from this investigation directory with `mpmath==1.3.0` available to Python:

```bash
python3 numerics/check_string_realization.py
python3 numerics/check_string_realization.py --digits 160 --output numerics/records/string_realization_160_20260926.json
python3 numerics/compare_string_precision.py
```

The full default cases are `(X,N) = (2,4), (5,8), (13,8), (13,12), (13,16)`, where `L=log(X)`. Repeat `--case X,N` to select cases. A full Weil matrix is assembled at the largest requested `N` for each `X`, then compressed for the smaller cases. `--output` can point to a temporary file when replaying historical runs.

The comparison uses the standard library, verifies both generator-source hashes before consuming the records, and fails with a regeneration instruction if an input is absent or stale. It compares numerical observables separately from precision-dependent residuals. In the saved runs, **504 observables agree at all 45 retained significant digits**. Maximum scaled reconstruction residuals are below `8.85e-92` and `2.20e-130`, respectively. This is not interval certification, and the common implementation can share errors between runs.

| X | N | Finite inverse-square trace | Force-port string length | Displacement-port string length | Force-port trace fraction beyond string coordinate 1,000,000 |
|---:|---:|---:|---:|---:|---:|
| 2 | 4 | 0.008244951309 | 0.0398418 | 1.70727 | 0 |
| 5 | 8 | 0.01182612890 | 1.99549e7 | 1234.03 | 0.404429 |
| 13 | 8 | 0.01147998257 | 9.15481e12 | 119.515 | 0.633101 |
| 13 | 12 | 0.01320942955 | 2.07829e20 | 16898.3 | 0.752996 |
| 13 | 16 | 0.01439075815 | 6.72454e25 | 1.98780e6 | 0.845890 |

The table is the finite string sector; records also retain the free Fourier tail and full inverse-square trace. The two ports preserve the spectrum and trace but change the string geometry. The evidence does not establish either convergence or failure of convergence. Mixed rank-one residue signs occur for all tested cases except `(2,4)`; their obstruction concerns a passive realization with the **same free Fourier bath**, not all passive systems.

- [120-digit string record](records/string_realization_120_20260926.json).
- [160-digit string record](records/string_realization_160_20260926.json).
- [Hash-checked precision comparison](records/string_precision_comparison_20260926.json).
- [Continuation note and proofs](../notes/CCM_STRINGS_GRAPH_DIRAC_AND_CUTOFF_OBSTRUCTIONS_20260926.md).
- [Critical review](../reviews/STRING_REALIZATION_CRITICAL_REVIEW_20260926.md).

Each new computation record is below 50 KB. It stores only the small string coefficients, selected observables, parameters, source hashes, and diagnostics; dense Weil matrices and intermediate factorizations are regenerated in memory. No external matrix archive is needed for this round. Hash agreement identifies these saved files and source versions, not the truth of a mathematical claim or portable bit-for-bit arithmetic.

## Continuation round 3: energy-defined ports at fixed support

[`check_energy_ports.py`](check_energy_ports.py) extends the fixed L=log13 sequence to N=8,12,16,24,32 and compares four prescribed ports: the force e1, the displacement M e1, the fixed analytic profile M f with f_n=2^(1-n), and the inverse-energy displacement M K^(-1) M e1. Every reconstruction fixes the first bead mass to one. The arithmetic builder and earlier reconstruction programs remain unchanged; no zeta zeros are evaluated.

From this investigation directory, with the same mpmath 1.3.0 dependency:

```bash
python3 numerics/check_energy_ports.py --digits 120 --output numerics/records/energy_ports_120_20260926.json
python3 numerics/check_energy_ports.py --digits 160 --output numerics/records/energy_ports_160_20260926.json
python3 numerics/compare_energy_port_precision.py
python3 numerics/check_energy_port_controls.py
```

Use `--cutoffs 8 16 24 32` to select a sequence; the default includes 12 as well. The generator requires an explicit output path, so replay can target temporary storage. It records absolute first-moment tails at five radii, fractions, 50/90/99 percent trace quantiles, masses, positions, finite odd gaps, Fourier mass tails, and the full inverse trace including the free tail. The Fourier mass tails are finite observations, not certified infinite-tail error bounds.

The independent reconstructions at 120 and 160 decimal digits agree on all **1,177 observables at all 45 saved significant digits**. The largest scaled reconstruction residuals are below **7.76e-76** and **1.11e-115**. Checks include both energy congruences, the port-invariant mass and first-position formulas, Lanczos orthogonality/intertwining, determinant and response, and the earlier implementation at N=8. Numerical cyclicity failure raises an error without discarding modes. These checks are not interval certificates.

At N=32 the fractions of the inverse trace beyond string coordinate one million are:

| Port | Trace-tail fraction | Total mass |
|---|---:|---:|
| Force | 0.953224 | 11.97493 |
| Displacement | 0.138144 | 1.084165 |
| Smooth displacement | 0.137510 | 1.179041 |
| Inverse-energy displacement | 0.198662 | 1.013518 |

Stable total mass is insufficient to infer first-moment tightness. The exact rational control uses masses (1,2/R) at positions (1,R): first mass and position stay one, the total mass tends to one, but two units of inverse trace escape. It checks the determinant and first-port response with the standard library, independently of mpmath. The note proves the formulas for every R>1.

- [120-digit record](records/energy_ports_120_20260926.json).
- [160-digit record](records/energy_ports_160_20260926.json).
- [Hash-checked precision comparison](records/energy_port_precision_comparison_20260926.json).
- [Exact rational controls](records/energy_port_exact_controls_20260926.json).
- [Proofs and interpretation](../notes/CCM_ENERGY_PORTS_AND_FIXED_SUPPORT_LIMIT_20260926.md).
- [Critical review](../reviews/ENERGY_PORTS_AND_FIXED_SUPPORT_REVIEW_20260926.md).

The comparison verifies all three generator hashes and fails closed on stale records. A deliberate stale-hash control was rejected. Each new JSON file is below 105 KB and stores only small reconstruction/diagnostic records. No dense matrix archive is saved. Agreement of hashes establishes file/source identity, not the mathematical claims or portability of arithmetic results.

## Continuation round 4: an exact odd-tail certificate and block diagnostics

[`certify_odd_tail.py`](certify_odd_tail.py) uses only Python's standard library and exact rational interval arithmetic. At L=log13 it certifies the unshifted odd Fourier compression above mode 4096 is at least 2/5. It also encloses two matrix-entry witnesses proving that a scalar norm Schur lower test based on that tail bound fails at every threshold 0<=s<2/5. This is not a certificate of the full odd-sector gap or a negative direction of the actual Weil form.

The same program proves the numerical constants for a uniform |b_n|<2 bound and evaluates analytic finite-rank coupling remainders. For coupling from modes 1..4096 to modes above 8192, 128 expansion terms give rank at most 256 and error below 6.91e-77. The intermediate rows remain part of the next matrix test. Exact rational endpoints and parameters are in the small certificate record.

Run from this investigation directory:

```bash
python3 numerics/certify_odd_tail.py
```

No external arithmetic package is needed for that certificate. Floating-point interval inputs, zero-containing divisors, and execution with assertions disabled are rejected. The analytic proof in the note is part of the certificate: the program checks its constants, not an arbitrary infinite matrix supplied as input.

[`check_odd_blocks.py`](check_odd_blocks.py) separately builds both finite parity blocks from closed digamma/trigamma formulas. It checks both against the preserved defining-distribution quadrature at N=4 and evaluates odd/even Ritz data through N=64. These results require mpmath 1.3.0 and are multiprecision diagnostics, not interval eigenvalue certificates. No zeta zeros are evaluated.

```bash
python3 numerics/check_odd_blocks.py --digits 120 --output numerics/records/odd_blocks_120_20260926.json
python3 numerics/check_odd_blocks.py --digits 160 --output numerics/records/odd_blocks_160_20260926.json
python3 numerics/check_odd_blocks.py --compare numerics/records/odd_blocks_120_20260926.json numerics/records/odd_blocks_160_20260926.json --output numerics/records/odd_block_precision_comparison_20260926.json
```

Default cutoffs are 8,16,32,64. An explicit `--output` is required for diagnostic runs and comparisons; it may point to temporary storage. The comparison verifies all three generator-source hashes and rejects a stale record. All **60 saved observables agree at all 45 retained significant digits**, with maximum identity residuals below **8.12e-121** and **7.83e-161**.

At N=64 the finite odd gap is about 5.70e-55. The cross block to modes 65..128 has Frobenius norm about 1.15, but its squared norm on the lowest odd Ritz vector is about 7.98e-55. This finite-window observation illustrates the directional cancellation lost by a scalar norm. It does not certify the infinite residual or the continuum gap. The structured-remainder identity is checked on finite windows against a bound derived analytically for the entire infinite tail.

- [Rational tail and scalar-obstruction certificate](records/odd_tail_certificate_20260926.json).
- [120-digit block diagnostics](records/odd_blocks_120_20260926.json).
- [160-digit block diagnostics](records/odd_blocks_160_20260926.json).
- [Hash-checked comparison](records/odd_block_precision_comparison_20260926.json).
- [Proofs and the exact remaining Schur gate](../notes/CCM_ODD_TAIL_CERTIFICATE_AND_STRUCTURED_SCHUR_20260926.md).
- [Critical review](../reviews/ODD_TAIL_AND_SCHUR_REVIEW_20260926.md).

Only small records are saved; all new JSON files are below 25 KB. No dense 4096-mode matrix is assembled or archived. The complete matrix Schur certificate, including an enclosed even trial energy and verified far Gram-series sums, remains to be done.

## Continuation round 5: exact controls for the bounded infinite-L audit

[`check_infinite_l_audit.py`](check_infinite_l_audit.py) uses only standard-library rational and integer arithmetic. It checks the ground-coefficient rank-one inverse-trace formula by exact matrix inversion, and the normalized determinant by elimination at 20 rational spectral parameters. Four coefficient configurations include a constant ground and signed coefficients; they are algebra controls, not claimed arithmetic Weil examples.

It also checks the central-binomial divisibility and size inequalities used in the prime-norm obstruction for n=1..128, giving 256 integer checks. The proof for all n is in the [audit note](../notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md); checking finitely many integers is not substituted for that proof. The program does not evaluate zeta zeros, build a Weil matrix, or certify an infinite-L limit.

From this investigation directory:

```bash
python3 numerics/check_infinite_l_audit.py
```

Use `--output` with a temporary path to replay the saved record. The [small JSON record](records/infinite_l_audit_controls_20260926.json) includes parameters, exact values, check counts, and the program's SHA-256 hash. No external package or data file is needed. All checks use explicit exceptions and remain active when Python assertions are disabled.

No arithmetic support sweep was performed for this audit. Its conclusions are analytic method limitations and conditional comparison estimates; the [review](../reviews/INFINITE_L_BOUNDED_AUDIT_REVIEW_20260926.md) separates those claims from the unresolved arithmetic ground-state comparison.

## Continuation round 6: Xi proxy and low even cluster

The [ground-selection diagnostic](../reviews/CCM_XI_GROUND_DIAGNOSTIC_20260928.md) compares the projected analytic Xi kernel with the actual finite even ground for a bounded set of supports and cutoffs. It does not construct the finite prolate candidate, use zeta zeros, or certify an infinite tail. At every tested point the proxy Rayleigh quotient exceeds the second even eigenvalue, so the raw residual/separation gate cannot be used. First-four-mode weights show why tiny higher-mode coefficients can dominate the residual while the first excited mode dominates the profile error.

Scripts and small records are grouped in [ground-selection-20260928/](ground-selection-20260928/README.md). The targeted 90/130-digit repeats agree to at least 20 relative decimal digits. A defining-form check verifies the support-generalized builder on small blocks; separate quadratures verify the candidate normalization. These are floating checks, not interval certificates. The N=32 to64 comparison at X=13 changes the moment and worsens the profile distance, so no cutoff convergence is asserted.

The main analytic result is the [continuum ground-selection criterion](../notes/CCM_GROUND_SELECTION_TARGET_20260928.md), not an extrapolation of this table. The continuum residual there is uncentered; the diagnostic residual is centered at the finite Rayleigh quotient.

## Continuation round 7: derivative cluster and finite complement

The [new diagnostic](../reviews/CCM_DERIVATIVE_CLUSTER_DIAGNOSTIC_20260928.md) uses only X=13 and N=32,64, with trial spaces prescribed by the analytic k and its second and fourth derivatives. Integration-by-parts endpoint terms are included. It compares plain Ritz selection with full finite Schur elimination and the required harmonic-lift mass. The 130/160-digit runs agree on all retained observable strings at 45-digit serialization, excluding roundoff checks. These remain floating diagnostics.

The small records and portable scripts are in [cluster-selection-20260928/](cluster-selection-20260928/README.md). The correction cancels roughly 18–28 decimal orders of the trial block norm. Its use of the full finite inverse explains the excellent lifted approximation but is not an independently proved complement estimate. No infinite Fourier or growing-support conclusion is drawn. The [analytic continuation](../notes/CCM_BOUNDARY_SELECTION_AND_COMPLEMENT_20260928.md) supplies separate boundary-selection and limit-order theorems.

## Continuation round 8: bounded prime-return check

The [prime-return diagnostic](../reviews/CCM_PRIME_RETURN_DIAGNOSTIC_20260928.md) evaluates the complete prime-power sum required for eight prescribed central return windows, with X=20,100,1000,10000 and T=1/2,1. It checks the continuous comparison, the Stieltjes integration-by-parts identity, and a finite prime-counting error-envelope bound. It builds no Weil matrix and uses no zeta-zero data.

Portable scripts and small records are in [weighted-tail-20260928/](weighted-tail-20260928/README.md). The 80/110-digit runs agree at the 45-digit serialization of retained observables, apart from working precision and roundoff checks. These are floating diagnostics, not interval or uniform-in-X certificates. The whole-line results are proved analytically in the [round-8 continuation](../notes/CCM_WEIGHTED_TAIL_AND_DISCRETE_OBSTRUCTION_20260928.md), rather than inferred from these samples.
