# Self review of the flat Dirac lattice representation

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Same-assistant review; independent specialist review remains open.

[Note12](../notes/12_FLAT_QUATERNION_DIRAC_AND_DYADIC_LATTICE_H_20261027.md) gives an exact representation with the standard flat quaternion Dirac operator and one Gaussian exponential field. It addresses the user's operator, radius and parameter requests, but retains a prescribed dyadic parity weight and supplies no first-order quaternionic evolution or collision estimate.

## Algebra and shell recovery

- D_X uses left multiplication and e_i e_j+e_j e_i=-2 delta_ij, so D_X^2=-Delta_X. There is no shifted sphere operator in this calculation.
- The decomposition m=2^j v is unique when v is not wholly even. Its supported union is not an additive lattice. The note explicitly distinguishes the ambient lattice from this support.
- For imaginary v, v^{-1}=-v/|v|^2. Multiplication by exp(I_v a) has scalar part sin(a)/|v|, with the positive sign used in equation (9).
- The character is unchanged by v -> -v, so the quaternion vector part cancels. The odd-shell Jacobi coefficient 2h chi4(h) cancels both the inverse norm and sin(pi h/2). The remaining phase is cos(zu), with no extra sine term on odd h.
- The infinite shell identity and decomposition A=sum_j P(2^j r) come from Note08. The new note does not claim them as newly discovered results.
- The n=3 shell needs its nonaxial contribution. This distinguishes the construction from a torus average that removes all transverse modes.

## Spatial observation and boundaries

The field is defined on the exterior of the unit ball with actual r=|X|. Its phase uses the direction X/r, so it is not the same flat heat equation obtained by interpreting the phase variable as a Cartesian torus coordinate. The note preserves this distinction.

The sphere measure has total mass one. Its mean is 4A/pi, not A. Combining that factor with Phi=(1/2)r^{5/2}Delta_3 A, du=dr/(2r), and dX=4 pi r^2 dr d sigma gives the coefficient -1/64 in the D_X^2 integral. The angular Laplacian integrates to zero on S^2; it is not dropped pointwise.

For the formula with no summand derivatives, g''-g=B g, where B=2t-1+(2tu+Iz)^2. The lower endpoint has psi'(0)=-1/2. The g' psi term has zero quaternion scalar coefficient, including under complex-linear continuation. These facts give +1/16. The measure conversion gives 1/256 in the spatial integral. Neither completion cost is hidden.

There is no lattice zero site, touching-site singularity or r=0 boundary in the integration region. The Gaussian majorant controls all needed derivatives and all compact complex parameter sets. Complex continuation uses the scalar coefficient in H tensor C, not complex real-part extraction.

## First order claims and comparison tests

The field satisfies the Newman parameter equation termwise because of its explicit exp(tu^2+Izu) factor. No Fueter regularity is asserted. The real-axis calculation (partial_t+D_X)exp(q)=-2exp(t) is a scoped check of the ordinary quaternion exponential. It is not an exclusion of all quaternionic solutions or all observations of them.

The simpler torus construction and the proposed transverse magnetic modification both reduce by Fourier orthogonality to the zero transverse mode. Only that elementary series identity is recorded. A magnetic Dirac heat kernel or index theorem is not claimed to have been verified or used. The selected parabolic-Dirac reference supplies flat-operator background only; its extended formulas are not imported.

Quaternions shorten the primitive's inverse-times-exponential expression, but the spatial kernel lies in a fixed complex slice. The current calculation gives no benefit from noncommutativity. It replaces the earlier two Gaussian fields with one field having dyadic arithmetic; it does not establish overall simplicity or faster computation.

## Verification and research scope

[Checker10](../numerics/10_check_flat_dirac_dyadic_lattice_20261027.py) checks nine exact anticommutator identities, 900 complete scale/shell pairs through squared radius 225, and 15 rational square coefficients. The finite enumeration contains 2046 supported sites. It tests the literal quaternion exponential at three parameter choices.

[Record10](../numerics/10_FLAT_DIRAC_DYADIC_LATTICE_CHECKS_20261027.json) also compares the original H integral, the completed exponential-field integral, and the full spatial Laplacian integral. The latter retains the angular Laplacian before quadrature. The grids are 96 radial by 18x36 angular and 144 radial by 26x52 angular, with 132 lattice sites of norm at most 6 and u truncated at 1.2. Across five real/complex parameter pairs and both grids, the maximum difference is 2.321e-14. Increasing the grid does not monotonically reduce floating error; no interval bound or convergence-rate claim is inferred.

The written Jacobi, domination, integration-by-parts and spherical-averaging arguments prove the infinite equalities. The numeric record checks their normalization. Existing collision controls are not rerun or promoted: this return proposes no favorable sign or exclusion mechanism. The appropriate next question is whether the dyadic character or the completion can be derived from a standard geometric structure, with the full observation cost counted.
