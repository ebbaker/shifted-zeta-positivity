# Fixed-flow correlation: selected classical formula checks

30 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance; actual **gpt-6-astra / xhigh**, Investigation05 chat0043.

This extends the existing **NIST Digital Library of Mathematical Functions** source identity in [sources.json](sources.json) and the existing `NISTDLMFThetaRadial2026` entry in [sources.bib](sources.bib). It creates no duplicate source or PDF.

- [DLMF 1.8.14](https://dlmf.nist.gov/1.8.E14), including the preceding hypotheses, was read online: the stated sufficient assumptions are C² regularity and integrability of f and |f''| on the line. Shifted Gaussians satisfy these assumptions. This supports the classical Poisson step in the inherited two-coordinate product identity.
- [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32), with the preceding principal-square-root convention, was rechecked. At zero elliptic argument and τ=iy, y>0, it supplies theta inversion. The same-nome addition formulas in §20.7(ii) were inspected as context only; they are not used as an identity for two arbitrary independent nomes.

The exact parity lattice change, differentiated product factor 4096 and positive-time split limitations are checked in the repository's [Note38](../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/38_POISSON_PARITY_CORRELATION_AND_HEAT_OBSTRUCTION_20261015.md) and [Note42](../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/42_LOCALIZED_POISSON_MODE_OBSTRUCTIONS_20261015.md), not imported as a DLMF sign theorem. Their full-plane split obstruction retains its original weight and domain.

Used by the [FCG-B01 comparison](../notes/fixed_coefficient_parameter_geometry/01_COLLISION_SIGNATURE_COMPARISON_20261030.md), §2. Its overlap kernel, collision law, and missing relative sign estimate are separate calculations or research obligations. No theta exclusion, whole-chapter audit, or literature-priority claim follows from these selected checks. Online reference retrieved 30 October 2026; no artificial PDF retained.
