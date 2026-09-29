# Resistance-model controls

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact variant and reasoning effort were not exposed.

These computations support the [initial research note](../notes/CCM_RESISTANCE_FORMS_AND_CHANGING_FRACTALS_20260926.md). They test specific distinctions between static harmonic compatibility, dynamic elimination, and changing geometric cutoffs. They do not compute a CCM-to-fractal embedding or use zeta-zero data.

From the repository root, using Python 3.10 or later and only its standard library:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 papers/investigations/ccm-fractal-laplacians/numerics/check_resistance_models.py --output /tmp/resistance_models_replay.json
```

The dated [record](records/resistance_models_20260926.json) binds the program by SHA-256 and records Python version, parameters, arithmetic, and results. Replay to a separate file to preserve research history. The source hash establishes code identity, not a proof of the model. Environment metadata can differ on another installation.

The program checks:

1. Exact Schur-complement compatibility of gasket energies at levels 0–2, including the \((5/3)^m\) conductance normalization.
2. Exact inverse traces and resistance bounds for explicitly specified discrete mass measures. These measures change with the graph; this is not the fixed-measure Galerkin sequence of Proposition 2.
3. The nonzero dynamic-elimination remainder at \(\omega^2=1/7\), and a massless-interior control where it vanishes.
4. The shrinking-tree counting formula against independent enumeration at 500 integer thresholds, counts at larger thresholds, and exact partial inverse traces with analytic bounds on the omitted arms.
5. Fourier-compression identities on two parity-diagonal surrogates: a stabilized even ground value gives zero defects, while an added lower even mode gives the stated stiffness and mass defects. These surrogates are not claimed to be actual Weil matrices.
6. All 11 decimal diagnostics at 32 and 64 digits, agreeing at 24 retained significant digits. Algebra and counts use exact `Fraction`/integer arithmetic and have no floating-point precision parameter.

All controls passed. The continuum trace identity, the infinite-tree construction, and the spectral asymptotic are proved in the note; finite runs are not substitutes for those proofs. The record contains small scalars and one 3-by-3 effective mass matrix, not a derived matrix archive. No large data or third-party material is stored here.


## Continuation: prescribed prime-jump geometry

The [new research note](../notes/CCM_PRIME_JUMP_GEOMETRY_OBSTRUCTIONS_20260926.md) completes the proposed fixed-support experiment at `X=13`, `L=log(13)`, and `N=4,8,16`.

[`check_prime_jump_geometry.py`](check_prime_jump_geometry.py) rebuilds the full Weil matrix through the preserved neighboring `check_mass_stiffness.py`, then uses a prescribed real sine evaluation map at nested dyadic vertices. The prime and pole contributions are retained separately; the archimedean remainder retains the original builder's regularized tail. No zeta zeros are evaluated. All finite matrices are rebuilt, not read from a saved matrix archive.

Requirements: Python 3.10 or later with `mpmath==1.3.0`. The old resistance controls above still use only the standard library. From the repository root, replay to separate temporary records:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 papers/investigations/ccm-fractal-laplacians/numerics/check_prime_jump_geometry.py --digits 80 --output /tmp/prime_jump_geometry_80_replay.json
PYTHONDONTWRITEBYTECODE=1 python3 papers/investigations/ccm-fractal-laplacians/numerics/check_prime_jump_geometry.py --digits 120 --output /tmp/prime_jump_geometry_120_replay.json
python3 papers/investigations/ccm-fractal-laplacians/numerics/compare_prime_jump_precision.py --low /tmp/prime_jump_geometry_80_replay.json --high /tmp/prime_jump_geometry_120_replay.json --output /tmp/prime_jump_precision_replay.json
```

The folded-tent witness uses direct nested multiprecision quadrature and can take several minutes. The analytic rational lower bound is proved in the note and does not depend on that quadrature. At least 80 digits are required by the program because the shifted forms have very small eigenvalues.

Saved compact records:

- [80-digit arithmetic run](records/prime_jump_geometry_80_20260926.json).
- [120-digit arithmetic run](records/prime_jump_geometry_120_20260926.json).
- [Hash-bound precision comparison](records/prime_jump_precision_comparison_20260926.json).

The new program records:

1. The observed simple-even ground gap, ground boundary magnitude, positive mass, and finite inverse trace.
2. Both reconstructed nodal Gram identities, positive off-diagonal stiffness witnesses, negative grounding row sums, and negative nodal mass witnesses.
3. A vertex-independent sine-product mass identity and its separate prime, pole, archimedean, and scalar-shift contributions.
4. Schur energy and pulled-back mass defects at all three refinements, extension coefficient extrema, and the composition defect.
5. Passing necessary inverse-trace monotonicity and inverse-spectrum interlacing diagnostics; these do not imply geometric compatibility.
6. Exact-form Fourier-compression identities, a positive grounded-path compatibility control, a positive atomic-measure identity control, and positivity of the full-line prime jump Gram.
7. The positive cross energy of two disjoint folded tents, with the prime and smooth terms separately recorded. The associated proof supplies the rational lower bound `46/16875` independently.

Both precision runs passed the numerical/algebraic controls, with maximum residuals below `7.4e-58` and `4.7e-98`. All 153 serialized numerical observables agree at the generator's 45 significant digits and pass the comparator's relative `1e-25` threshold; all 119 discrete observables agree. Precision-dependent reconstruction residuals are excluded from equality comparison and checked separately. The comparator verifies the two generator-source hashes before consuming records, records the input file hashes, and fails closed on missing or mismatched inputs.

The intended arithmetic construction **fails** its stiffness, mass, and harmonic-compatibility requirements. These failures are research results, not failed program controls. The necessary spectral tests pass. These are exploratory multiprecision calculations, not interval certificates, and do not exclude arbitrary alternative maps or all resistance geometries. See the [critical review](../reviews/PRIME_JUMP_GEOMETRY_CRITICAL_REVIEW_20260926.md) for the distinction.

No full derived matrices, large datasets, or third-party PDFs are stored here. Historical records and the neighboring Weil builder are unchanged.
