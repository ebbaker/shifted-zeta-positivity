# Radial Laplacian and Kelvin source references

27 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

Used by [Note20](../notes/20_THREE_DIMENSIONAL_RADIAL_THETA_AND_KELVIN_REDUCTION_20261027.md). Selected passages were checked; no full book or chapter audit is claimed. The application to the unchanged theta source is derived in Note20.

## Harmonic Function Theory

Sheldon Axler, Paul Bourdon, Wade Ramey, *Harmonic Function Theory*, second edition, Springer, 2001. Author-hosted PDF dated **17 July 2020** on its title page: [primary PDF](https://www.axler.net/HFT.pdf).

Checked Chapter 4, printed pages 61–63: definition of the Kelvin transform and Proposition 4.6. For a C^2 function away from the origin, Kf(x)=|x|^(2-d)f(x/|x|^2) and Delta Kf=K(|x|^4 Delta f). In dimension three its radial specialization is Delta Kf(r)=r^(-5)(Delta f)(1/r). This does not assert smoothness at the origin or positivity of a physical transform. Note20 derives its radial Gaussian and boundary identities directly.

Retrieved 27 October 2026 from the author-hosted URL above. Reading copy retained outside Git:

- Path: `/Users/Shared/szp-archive/three-regime-heat-flow-dynamics/references/Axler_Bourdon_Ramey_Harmonic_Function_Theory_2e_20200717.pdf`
- Bytes: 2258926
- SHA-256: `4e64124f7e36993ee784e575a024505f99d484ccf959d2d3864eae9232af8bf1`

The hash identifies this copy only.

## Theta modular transformation

The canonical DLMF record remains [Reference02](02_DLMF_GAMMA_AND_ZETA_IDENTITIES_20261026.md). This inspection adds [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32), with theta argument zero and lattice parameter i r^2, r>0. The principal square root is then r. The resulting identity is Theta(r)=r^(-1)Theta(1/r). The passage was checked on 27 October 2026. DLMF remains an online reference; no artificial PDF was created.
