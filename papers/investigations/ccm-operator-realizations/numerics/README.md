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
