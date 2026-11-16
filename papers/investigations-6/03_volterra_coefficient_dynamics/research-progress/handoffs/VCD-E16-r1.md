# VCD-E16 r1 — quantitative upper allowance after midpoint calibration

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex assistance. Type E, parent B04 decision09. Explicit dispatch gpt-6.1-sol/ultra; separate backend attestation unavailable. Lead actual model/effort unavailable. One fixed proof and one correction pass; no numerical campaign.

Fix time-zero canonical mu, real even h in L-infinity(mu), ||h||<=eta, and delta F(w)=integral h exp(iwu)dmu. Assume integral u^k h dmu=0 for k<=2L, L>=0, and delta F^(j)(a)=0 for j<=r, r>=0, at a=z*/2, z*=x+iy, x*y nonzero. These derivative matches follow from E12's c_0 midpoint-jet calibration whenever that construction is used. Derive all claims directly, without depending on an unfinished E12 proof.

For rho>|z*| define B_{rho,a}(w)=rho(w-a)/(rho^2-conjugate(a)w), and A={a,-a,conjugate(a),-conjugate(a)}. Prove
|delta F(w)| <= eta F(i rho) (|w|/rho)^(2L+2) product_{v in A}|B_{rho,v}(w)|^(r+1), for |w|<rho.
Use evenness/real-entire symmetry, exponential moments, removable quotient zeros, and the maximum-modulus principle checked in references02 §Quantitative midpoint calibration. Prove each disk factor has boundary modulus one and interior modulus<1. This is a standard finite Blaschke-factor argument; no novelty claim for the complex-analytic method. State that the bound is continuous at the specified zeros.

At w=z*, give theta_rho(z*)=product_{v in A}|B_{rho,v}(z*)| in (0,1), and thus the factor theta_rho(z*)^(r+1) improvement over the SAME moment-only disk bound. May simplify the quartet product algebraically; do not weaken correctness to obtain a neat number. Derive the ordinary moment-series alternative eta sum_{p>=L+1}|w|^(2p)m_(2p)/(2p)! and note one can take the minimum. No claim that the disk bound always beats that alternative. For fixed z*,rho,eta, the allowance decays geometrically with L or r. Growing rho or height must pay F(i rho); no uniform rate is inferred.

Interpret as an upper radius for any E12-type achievable displacement disk whose perturbations all obey the SAME ||h||<=eta and fixed calibrations. It coexists with each fixed instance's positive local rank-two radius and supplies no uniform lower bound. It gives no zero-free result or value-phase information: an actual closure/source model with those calibration/tolerance premises and a lower Fourier/model modulus are additional unpaid inputs. Exact c_0 is full-chain data, not acquired from a finite head. State the literal normalization and that score b, arithmetic, other c_n and finite tail tests are unused in this upper estimate. Screen control premises with the inherited catalog/E13 distinctions.

Own only notes/14_VCD_E16_CALIBRATION_UPPER_BOUND_20261116.md and research-progress/handoffs/VCD-E16-r1-return.md. No shared register/navigation/reference/chat edits. Include date, Edward Baker, LLM assistance and actual dispatch metadata; preserve source scope.

## Pinned inputs
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/11_VCD_E13_MIDPOINT_AUDIT_20261116.md` SHA-256 `689a7d228dd4e5722cdb9734f9895c176d0bf442dfaccb5e1193013a4283620f`
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/04_VCD_E04_TAIL_FOUNDATIONS_20261116.md` SHA-256 `116f29472c162272fa554a564f1c88ea02573ee27bd43ee36c2e8e9eefc63880`
- `papers/investigations-6/03_volterra_coefficient_dynamics/brainstorm/notes/09_VCD_B04_CALIBRATION_RADIUS_DECISION_20261116.md` SHA-256 `2e26a01de78930d0ecb9c1a6e058c34897037bc27ae06b5747657288d583ebba`
- `papers/investigations-6/03_volterra_coefficient_dynamics/references/02_INDUCTION_SOURCE_PASSAGES_20261116.md` SHA-256 `a64d69c2b16532caa66e700466c7336d7a73ff483462edc1695675e56d13fd64`
