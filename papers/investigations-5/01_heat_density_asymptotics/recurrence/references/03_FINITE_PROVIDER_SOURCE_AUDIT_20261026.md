# Primary-source check for the finite-provider construction

26 October 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**.
Recurrence chat0003. This is a selected-passage check, not a full reading
or independent specialist validation. No third-party PDF is added.

**NIST Digital Library of Mathematical Functions**, online edition 1.2.8,
release date 2026-09-15 as displayed, retrieved 2026-10-26.

- [5.8, Infinite Products](https://dlmf.nist.gov/5.8), specifically
  [5.8.1](https://dlmf.nist.gov/5.8.E1) and
  [5.8.2](https://dlmf.nist.gov/5.8.E2): Euler limit excludes nonpositive
  integers; the reciprocal-gamma product is the classical input for
  Note09 P6. Only Re z_gamma=1/4 is used. The logarithmic branch is fixed
  analytically in the right half-plane. The tail bounds and finite work
  estimates in Note09 are derived there, not supplied by DLMF.
- [5.4, Special Values](https://dlmf.nist.gov/5.4) and
  [5.5.1, recurrence](https://dlmf.nist.gov/5.5.E1): factorial and
  half-integer moment constants reduce to sqrt(pi) and exact factorials.
  Only these special values/recurrence are used for the finite majorants.
- [5.7, Series Expansions](https://dlmf.nist.gov/5.7): inspected the
  small-variable log-gamma/digamma formulas and their radius restrictions.
  They are not applied to the large imaginary gamma argument. No
  large-argument precision theorem is imported from this section.
- [3.5(v), Gauss Quadrature](https://dlmf.nist.gov/3.5.v): positive-weight
  and polynomial-exactness framework rechecked. The shared
  [AN02 source audit](02_RS_EVALUATION_SOURCE_AUDIT_20261026.md) owns
  the preceding reading record. Note09 additionally proves the rational
  Legendre/root/weight construction and its own very conservative work
  bounds; a DLMF numerical root routine is not assumed.
- [18.16, Zeros](https://dlmf.nist.gov/18.16), selected Jacobi and Legendre
  navigation passages inspected. No asymptotic zero-spacing theorem is
  imported. Note09 derives a deliberately weak separation from a
  nonzero integer resultant and exact orthogonality.

Use [Note09](../notes/09_FINITE_PROVIDER_ALGORITHMS_20261026.md), especially
P6--7 and P9--12, for the actual hypotheses and error derivations. The
existing PartII coefficient-identity/PartI access qualifications in
[Audit02](02_RS_EVALUATION_SOURCE_AUDIT_20261026.md) remain unchanged.
No preliminary PartII precision inequalities are used. Earlier canonical
heat/RS comparison sources retain their established reading scope.

The local [bibliography](references.bib) adds only the newly used DLMF
infinite-product entry; the earlier shared Gauss bibliography/annotation
continues to be linked rather than duplicated. DLMF is an online reference,
so no artificial PDF copy or download manifest is required.
