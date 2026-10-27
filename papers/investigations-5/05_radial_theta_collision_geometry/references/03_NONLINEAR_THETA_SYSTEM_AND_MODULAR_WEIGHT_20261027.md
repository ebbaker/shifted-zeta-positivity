# Nonlinear theta system and modular weight references

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

## Differential equations for the theta constants

Yurii V. Brezhnev, Simon L. Lyakhovich and Alexey A. Sharapov, *Dynamical systems defining Jacobi's theta-constants*, Journal of Mathematical Physics **52** (2011), 112704. [DOI](https://doi.org/10.1063/1.3662961); [arXiv version4](https://arxiv.org/abs/1012.1429v4), revised 2 December 2011; [versioned PDF](https://arxiv.org/pdf/1012.1429v4). Metadata and selected passages checked on 27 October 2026.

The input to [Note05][note] is Proposition1, equation(8), printed page4, for the three theta constants and Weierstrass eta. Equation(5) gives Jacobi's fourth-power relation, and equation(6), printed page3, fixes E2=12 eta/pi^2. The equations apply to the canonical theta series in the upper half-plane. Note05 restricts to tau=i exp(2x), retains the canonical initial data and algebraic relation, and performs the source-coordinate rescaling explicitly. The article's remarks after equation(8) distinguish differential identities from unrestricted dynamical-system solutions; this qualification is retained.

Only these defining relations and normalizations are used. No Hamiltonian, Nambu, spectral positivity, collision exclusion or theta-response inequality is imported. The rest of the article has not been audited for this use. The nonlinear equations are established literature, not claimed new here.

The public PDF reading copy is outside Git at `/Users/Shared/szp-archive/radial-theta-collision-geometry/references/1012.1429v4.pdf`, 380044 bytes, SHA-256 `110381b3cca21251c26f6aecf14cd51b38af11a56960ab7525c204ae3e66b848`. It was retrieved from the versioned PDF URL above on 27 October2026 and verified to have a PDF signature. The hash identifies that file and does not validate its claims. The stable links permit reading without this machine's archive.

## Modular and series normalizations

NIST DLMF [20.7.5](https://dlmf.nist.gov/20.7.E5) supplies theta_3^4=theta_2^4+theta_4^4. Equations [20.7.31](https://dlmf.nist.gov/20.7.E31), [20.7.32](https://dlmf.nist.gov/20.7.E32) and [20.7.33](https://dlmf.nist.gov/20.7.E33), at zero elliptic argument and positive imaginary lattice parameter, give the interchange of theta2/theta4 and the theta3 inversion factor. These selected formulas were checked online on 27 October2026. The full theta3 series normalization is inherited from the [circle annotation](01_CIRCLE_HEAT_AND_JACOBI_NORMALIZATIONS_20261027.md), DLMF20.2.3.

Note05 derives mu(-x)=1-mu(x), the weight normalization, and K(-x)=exp(x)K(x). The latter, combined with the differential system, supplies the value eta(0)=3 in the note's scaled E2 notation. No separate quasi-modular transformation formula is needed. These are selected-passage checks, not a chapter audit; DLMF remains an online reference without an artificial PDF copy.

## Internal antecedents and limitations

The generic forced identity and exact Gaussian cancellation come from [Note01](../notes/01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md). [Note03](../notes/03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md) already leaves nonlinear scalar theta identities outside its finite linear circle-space obstruction. The 13 October [portfolio review, Section5](../../../investigations-2/brainstorm/reviews/PATHS_FORWARD_AFTER_CONSOLIDATION_CODEX_20261013.md) already identifies nonlinear theta equations as a possible source of multipliers while retaining the missing transfer to oscillatory physical forms. Note05 implements one particular multiplier and does not claim priority for the broader idea or rely on the concavity preprint discussed there.

The [joint source-current note](../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/09_JOINT_SOURCE_CURRENT_AND_POLYNOMIAL_OBSTRUCTION_20261015.md) explains how a valid source current can leave the same unknown boundary observation. The new scalar multiplier's exact equality is proved directly, with its own canonical sign obstruction. The source-control premises are those in the [control register](../../../../result-summaries/12_collision_controls_and_screening.md).

[note]: ../notes/05_MODULAR_WRONSKIAN_WEIGHT_AND_CANONICAL_SIGN_OBSTRUCTION_20261027.md
