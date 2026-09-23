# Internal audit of the bounded WZW arithmetic-readout test

**Numerical correction, later on 23 September 2026:** the transformed prime-free kernel correction integral in the diagnostic used `exp(-2*v)` instead of `exp(-(3-2*omega)*v)`. The written convolution formula was correct. The implementation and record have been corrected and the complete suite replayed successfully. See the [modular-scattering note, Section 8](../notes/MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) for the derivation, independent regressions and scope; the analytical exclusions are unchanged.


23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Review status:** same-assistant analytical and numerical audit. This is not an independent specialist review.

Reviewed artifacts: [research note](../notes/BOUNDED_ARITHMETIC_READOUT_TEST_20260923.md), [diagnostic program](../numerics/check_boundary_readout.py), and [record](../numerics/records/boundary-readout-20260923.json).

The candidate is a ground-normalized Euclidean collar on the full affine boundary module with a fixed preparation and reflected readout. It is a specific local sewing building block, not the general slit map with the pilot's four marked boundary fields. The report does not claim to have constructed that missing map.

## Analytical audit

1. The collar scalar is derived from its stated ground-channel reference. Dividing exp[-s(L0-c/24)] by that matrix element yields exp[-s(L0-h)]. The positive spectrum gives contraction and the strong identity limit. Finite-dimensional level spaces give compactness at every positive s, while the unbounded level spectrum excludes an operator-norm identity limit. No cutoff inference is used for these statements.

2. The compressed energy identity includes both propagation loss and output outside the prepared subspace. Omitting the latter would be incorrect for a general isometry. The spectral integral justifies the identity for arbitrary Hilbert vectors without assuming that their derivative at s=0 exists.

3. The causality exclusion is an operator argument on the fixed scalar L2 interval. Self-adjointness supplies the reverse triangular condition, forcing commutation with all cut projections and hence multiplication. Compactness would then force zero, inconsistent with the collar's strictly positive quadratic form. This excludes the specified fixed reflected collar class, not all positive-norm, chiral, asymmetric or scattering constructions. The supplementary claim about distinct fixed contractive input/output maps follows from equality in Cauchy--Schwarz when RJ=I.

4. The primary packet is defined by the translated highest-weight insertion. Its norm follows from the global sl(2) algebra. It is an infinite, invariant subspace inside the full affine module, not an assertion that the module has only one state per level. Character degeneracies and primary matrix-element weights are kept distinct. The raw field-smearing Gram operator is not identity; inverse Gram normalization is unbounded, and the note does not treat it as an already implemented physical spatial input map.

5. The cylinder kernel includes the two conformal Jacobians and the factor lambda^(2h). Matching the arithmetic spacing sets lambda=2, leaving a gap 3/8 and relative weights (3/8)_n/n! for the selected primary. An external scalar or common energy offset cannot repair the residue ratios. The spin-one comparison is explicitly a different sector and still has the wrong unshifted gap.

6. The Cartan-source comparison is a matrix-element control. Charges +/-1/2 give the cosh factor, but no identification with arithmetic shift or Loewner time is derived. Decay is checked only on the displayed primary tower in the stated range. This extra source calculation is not misrepresented as the logarithmic derivative of the collar transfer.

7. The gamma and full first-window comparisons preserve the hard-cutoff contact and remaining rational pole. The collision and large-p mismatches are analytical. The susceptibility is tested only as a proposed source building block; it is not assumed to be the physical shift generator. Finite local or rational additions cannot repair its missing 1/u behavior.

8. The first-transfer delay coefficient is c2=(2^omega-2^(-omega))/sqrt(2). Its derivative is sqrt(2)*log(2)*cosh(omega*log(2)); the logarithmic generator has the negative sign. On log(2)<L<log(3) the finite-shift arithmetic kernel is the prime-free kernel plus c2 times its log(2) translate. Smoothness of the selected physical kernel away from zero excludes both the generator atom and this delayed fractional singularity. No assertion is made that every WZW readout must share that smoothness.

## Numerical audit

All 60 controls passed: 13 exact rational and 47 floating. The comparison mechanisms include a conformal map versus a descendant series with a stated truncation bound, a beta expression versus transformed quadrature, an energy derivative integrated independently, and an arithmetic finite-shift formula differentiated numerically. Positive expected gaps are used for the mismatching cases, so a passing diagnostic does not mean arithmetic matching succeeded.

The forward arithmetic pairing of unit indicator inputs on (0,.02) and (.03,.05), at omega=.25, is approximately 0.11571873508141131. The reverse pairing is zero by causal support. At p=100000 the primary susceptibility is approximately 0.0010757373774586895 while the complete prime-free generator is approximately 9.675083398565052, illustrating their different asymptotics.

The near-delay mass calculation is only a diagnostic: the analytical local smoothness argument proves absence of an atom. The program uses ordinary floating arithmetic and is not a validated quadrature or infinite-dimensional positivity certificate. It requires Python 3 and NumPy and records the program hash and environment. The pre-existing 72 WZW and 60 arithmetic-source controls are separate and are not changed or counted as part of this run.

The result is a bounded negative test with useful positive controls. Further physical work requires a different oriented readout and a specified origin for arithmetic delays; it is not justified merely by adding more descendants to the tested primary preparation.
