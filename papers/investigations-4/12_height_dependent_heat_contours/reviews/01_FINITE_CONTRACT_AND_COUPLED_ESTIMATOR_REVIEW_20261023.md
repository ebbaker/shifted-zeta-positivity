# Review of the finite contract and complete coupled estimator

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. This record consolidates the authoring assistant's checks and a separate same-model reviewer agent's read-only audit. It is not cross-model or specialist review.

**Assessment: HDC-01 is complete as a specification and HDC-02 as a conditional exact expression. No canonical-theta input acquisition or comparative gain has been completed.** Sources are [Note 02](../notes/02_FINITE_BAND_GEOMETRY_AND_COMPARISON_CONTRACT_20261023.md) and [Note 03](../notes/03_COMPLETE_COUPLED_EXPRESSION_AND_COMPARISON_20261023.md). HDC-03 and HDC-04 retain their open status in the [sole register](../research-progress/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md).

## Mathematical audit

| Item | Finding |
| --- | --- |
| Observable and population | One fixed box, x in [26,46], spatial imaginary width 2, epsilon=delta=Y=10^-4. Target includes the entire cap, not only disks. All complex roots are included; the population count remains unacquired. |
| Noncircularity | Only complete boundary regularity is needed for the primary lower transfer. Optional inverse charts are certified on boundary time patches. No global tube, interior gap, all-real interval or RH is used to establish its own continuation. |
| Physical density | The four determinant coefficients and six other-face signs are correct. Only E appears in the denominator. The graph correction is f+epsilon' r. |
| Source tails | The geometric ratios in Note 02 (9) majorize all positive source terms on u>=0. Both mode and integral tails remain required; no numerical error allowance is claimed without evaluating them. |
| Independent geometry inputs | The boundary Lipschitz floor, all-root argument-principle population, Rouché chart criterion and Cauchy formula for a are valid. The latter cancels root poles with multiplicity and does not divide by pair gaps. |
| Complete reference identity | The unordered-pair coefficient is 8. Fixed reference spacings introduce no time derivatives. Linear terms, relative energy and the analytic factor are retained together. Exterior information remains in the analytic unit or complete root jets. |
| Complement | J is a defined signed physical chain. Shared faces cancel; uncovered cap pieces, spatial walls and transitions remain. It is not declared negligible. |
| Fractional disk charge | When both edge atlases exist, the argument principle gives disk difference k_rho Q and complement difference (1-k_rho)Q. At rho=.01, k_rho=1/10001. This is bookkeeping, not independent information about Q or J. |
| Transverse Taylor estimate | The factor k_rho Y^3/(6 pi) is correct. Real type of the symmetric product suffices; positive real gaps are an additional premise needed to use V>=0. |
| Polynomial sign control | The coefficients 384, −3584, 30208 and the explicit even-series tail bound are correct. The complete relative-energy contribution is negative for 0<Y<=.01 despite real-slice positivity in the event-free slab. |
| Comparison scope | Shared finite holomorphic coefficient models have equal path functionals. Uniform triangle allowances pay path length, twice the direct scalar allowance at epsilon=Y. Full-estimator domination additionally requires the stated regular geometry and matched complementary bound. This is not a universal no-go theorem. |
| Boundary events | The original target fails its regular-boundary premise at an event; punctured alternatives retain spherical pieces and do not assign automatic half charges. |

The separate reviewer found no mathematical blocker. One requested clarification—finite residual basis in the correlated-coefficient comparison—was incorporated before delivery. The original brainstorm formulas were not found to have a sign error; this round specifies their domain and full-cap complement more precisely.

## Reproducible checks and limitations

The standard-library [script](../numerics/01_check_boundary_and_relative_energy_20261023.py) and [small record](../numerics/01_BOUNDARY_AND_RELATIVE_ENERGY_CHECKS_20261023.json) use integers and exact rational arithmetic. They check 400 real determinant identities, 12 complex reference decompositions, 39 polynomial path identities, 12 polynomial-control series coefficients, two endpoint-radius rejections and nine sine material derivatives. A rational tail bound verifies the negative sign at Y=1/100; the analytic proof supplies the full interval down to zero. The record also checks k_rho=1/10001 and its complementary fraction.

These computations are finite algebra diagnostics, not interval evaluations of theta. The proofs carry the assertions beyond their test instances. No source jets, boundary minima, root counts, projective atlas, complete cap value, runtime advantage, height assembly or collision exclusion was acquired. The published source-control screen is a premise audit, not an unperformed rerun of every published control certificate.

The useful next action is exactly the fixed-source acquisition specified in Note 03, Section 6. Repeating the shared-coefficient identity or reporting a small disk cap without its complementary faces would not advance the stated comparison. This conclusion is scoped under [avoid 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), with the known [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md) and [coupling rule](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) retained.

Delivery validation: 137 local Markdown links resolved, display/inline math delimiters balanced, the installed diagnostic replay reproduced its JSON record byte-for-byte, and the record matched the installed script hash. Research artifacts are individually below 20 KiB. These are record-integrity checks, not additional mathematical certification.
