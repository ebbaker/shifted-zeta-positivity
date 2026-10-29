# Classical inputs for conservative feedback and diffusion contraction

28 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0009. Selected passages only; no full source audit or novelty claim.

[Note28](../notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md) supplies its own feedback equation, parameter accounting, local construction, Fourier splitting and collision deadline. These references identify the classical tools.

## John K. Hunter

**Notes on Partial Differential Equations**, revision 18 June 2014. [Author PDF](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf). The existing external reading copy and hash in [annotation10](10_PROJECTED_EVOLUTION_AND_ELLIPTIC_RESPONSE_20261027.md) are reused.

Checked Lemma5.50, printed p.154, and the proof of Lemma5.51 including (5.42), printed p.155: heat smoothing from L2 to a fractional Sobolev domain makes the Duhamel map contractive for a locally Lipschitz nonlinearity. Note28 verifies its specific H1-to-L2 map directly and uses the integrable time singularity of exponent1/2. The polynomial equation in Hunter's Theorem5.49 has additional Sobolev restrictions; that theorem is not applied with an invalid exponent. Section5.B.4, Theorem5.71, printed p.171, fixes Plancherel. Note28 uses the unnormalized forward transform, so its frequency integrals carry (2pi)^(-3).

## Andreas Eberle

**Reflection couplings and contraction rates for diffusions**, arXiv:1305.1233v3, 2 June 2014. [Version read](https://arxiv.org/abs/1305.1233v3), [versioned PDF](https://arxiv.org/pdf/1305.1233v3), [related publication DOI](https://doi.org/10.1007/s00440-015-0673-1). Version4, 19 October 2015, was identified but not read.

Checked the introduction on printed pp.1–2, equation(1.1) and its discussion of synchronous coupling for convex confinement. This is context for a classical contraction argument. Note28 gives the short pathwise proof with diffusion coefficient sqrt(2), drift -alpha(s)v, and lower monotonicity constant7/8. Its extension to a signed two-component density uses the common positive transition kernel; no nonconvex reflection-coupling theorem is imported. The nonlinear feedback and finite collision deadline are not asserted to be results of this paper.

External reading copy: `/Users/Shared/szp-archive/radial-theta-collision-geometry/references/Eberle_1305.1233v3.pdf`; 320109 bytes; SHA-256 `81c0c67a4798b20aadbbacb0fdb13277a6aa4ee943de90c2d819d2a2021dfcd0`. Retrieved 28 October 2026. The hash identifies the versioned PDF, not correctness of the argument. No third-party PDF is placed in Git.

## Uniform-feedback comparison, 29 October 2026

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra / actual effort max**, chat0031. For
[Note67](../notes/67_UNIFORM_FEEDBACK_DIRECT_COMPARISON_B02_R10_20261029.md),
selected online passages were checked in the existing NIST DLMF:
[1.14.1](https://dlmf.nist.gov/1.14.E1) (unitary Fourier convention),
[1.14.8](https://dlmf.nist.gov/1.14.E8) (Parseval for absolutely and square
integrable functions), and [4.19.1--2](https://dlmf.nist.gov/4.19)
(sine/cosine series). Retrieval: 29 October 2026.

Iteration in three coordinates and conversion to the unnormalized
forward transform yields the (2 pi)^(-3) factor in Note67. Its real
global cosine inequality is proved directly, not inferred by arbitrary
series truncation. The weighted Fourier estimate, theta moment payment
and elementary sliding-interval proof are derived in that note; no
external feedback or uniform-Gronwall theorem is imported. This is not
a chapter audit, priority search or new PDF acquisition. The earlier
Hunter and Eberle reading/version records remain unchanged.
