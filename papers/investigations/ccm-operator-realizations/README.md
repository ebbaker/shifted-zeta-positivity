# CCM operator realizations

Started: 26 September 2026.

This investigation studies alternative geometric and physical realizations of the Connes–Consani–Moscovici spectral operators. A useful realization should preserve the arithmetic input, account for the Hilbert-space metric, and improve control of the ground state or the normalized spectral determinant as cutoffs increase.

The first continuation derives a finite mechanical system with positive mass and stiffness matrices from the even and odd Weil forms. It also gives an inverse-square spectral trace criterion for compactness of the entire spectral functions and identifies a possible Gaussian contribution from the unmodified Fourier tail in a joint cutoff limit. These are finite algebraic deductions and conditional convergence criteria; the general simple-even ground-state condition and the identification of the limit with the Riemann Xi function remain open.

## Research record

- [Founding note: metric transport and the chiral realization](notes/CCM_SPECTRAL_OPERATORS_AND_CHIRAL_REALIZATION_20260926.md).
- [Continuation: boundary mechanics and determinant control](notes/CCM_BOUNDARY_MECHANICS_AND_DETERMINANT_CONTROL_20260926.md).
- [Numerical reconstruction and checks](numerics/README.md).
- [Initial derivation check](reviews/INITIAL_DERIVATION_CHECK_20260926.md).

The founding note was copied from `papers/susy-positivity/investigations/wilson-loewner/notes/`. Its only change is the relative link to the earlier project bridge sweep, adjusted for the new location. The original remains in place.

Incremental research belongs in `notes/`, numerical programs and small records in `numerics/`, and reviews in `reviews/`. No manuscript or draft snapshot is part of this initial investigation. The repository's [large-file policy](../../../LARGE_FILES.md) applies.

## Next research question

Can the pair of forms
\[
\mathsf M=J^\dagger(W_+-\varepsilon I)J,
\qquad
\mathsf K=W_--\varepsilon I
\]
be realized in a common geometric energy space that yields a bound for
\(\operatorname{tr}(\mathsf K^{-1}\mathsf M)\) uniform in the relevant cutoffs, together with an arithmetic identification of the resulting spectral functions?

Here \(J\) is inverse differentiation with zero endpoint value in the even sector. A positive finite mechanical representation alone does not fix the sign of the unshifted Weil ground energy.
