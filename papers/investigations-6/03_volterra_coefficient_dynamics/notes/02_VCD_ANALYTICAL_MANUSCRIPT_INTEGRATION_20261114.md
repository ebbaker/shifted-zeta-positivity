# VCD-E03 manuscript integration

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Recorded dispatch **gpt-6.1-sol /
ultra**. Separate backend attestation unavailable. The task integrates
[TN6-E04 r1](../../research-progress/handoffs/TN6-E04-r1.md) from the
[30-entry frozen input manifest](../../numerics/14_TN6_E04_MANUSCRIPT_INPUTS_20261114.json).

The [draft](../manuscript/main.tex) integrates the all-degree coefficient
envelope and normalized monic norm product **proved in-note** and
**accepted without correction within scope** in the existing same-worker
assessment. This is an intermediate approximation estimate, evaluated by
an explicit bound in degree and heat time under
[avoid 01](../../../../avoid/01_restating_the_target.md). The equal-coefficient
theta series enters via its score; the weighted-square collision witnesses
show that the resulting score estimate is insufficient for collision
exclusion. See the [result index](../../../../result-summaries/README.md),
[cluster 18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[avoid index](../../../../avoid/README.md),
[control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## Source map

| Manuscript | Source and treatment |
| --- | --- |
| §2 | [Complete source chapter](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex), reflection, differentiation and full-line \(1/2\); [E01 proof](01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md), §§1 and 3, for tails and recurrence. |
| §3 | [Founding height discussion](../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md), §§2–4, for the fixed/moving distinction and Volterra convention. The draft proves differentiability via finite Gram systems, differentiates monic orthogonality and derives the entrywise Lax sign from the moving polynomial column. |
| §4 | E01 §§1–4 and the [E02 assessment](../reviews/01_VCD_E02_ENVELOPE_ASSESSMENT_20261113.md) supply the score, confinement constant, integration by parts, Jensen and product. The manuscript states the common positive locally absolutely continuous density lemma and its exact hypotheses. The finite-time norm comparison integrates the same differential identity. |
| §5 | [Fixed Jacobi-chain proof](../../02_jacobi_chain_height_flow/notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md), §§1–2, supplies the Hermite–Gaussian scalar factor. Its derivation is included to exhibit precisely where the norm product and \(Z_*/2\) enter. |
| §§6–7 | E01 §5 and the [B01 screen](../brainstorm/notes/01_VCD_B01_LOGARITHMIC_ENVELOPE_DECISION_20261113.md) govern the collision scope. The draft applies its general lemma to the actual three- and four-square classes. |

The manuscript proves the Lax identity entrywise and on finite sequences
for the banded commutator. Self-adjoint realizations used in the scalar
readouts come separately from transporting the multiplication operator
at each time. Neither an evolution on a common unbounded operator
domain nor a globally well-posed infinite initial-value problem is
inferred from the commutator. The
[reference passage record](../references/01_VCD_MANUSCRIPT_SOURCE_PASSAGES_20261114.md)
identifies inspected sources. No numerical run was part of this integration.

## Actual control screen

The [control catalog](../../../../result-summaries/12_collision_controls_and_screening.md)
and the specific comparisons of E01 §5 were used analytically. The
certificates for the pre-existing witnesses were not rerun.

| Family | Pass, failed premise or scoped check |
| --- | --- |
| Positive three- and four-square controls | Pass the same envelope at their validated collisions. The positive weights cancel in each score, the even extension is locally absolutely continuous, and the factor \(u\) kills the junction term. Complete equal coefficients and full modular reflection are absent from these controls. |
| Three-atom source | The positive full-line density and score are absent. At its event \(\beta_1+\beta_2=1>B_1\), since \(\cosh(4)>14\). The finite coefficient evolution remains regular. |
| Euler-factor translates | The unchanged theta summand scores are absent. For \(c=1/2,p=23,\lambda=0\), the second moment increases by \((\log23)^2/12>3/4>B_0\), verifying an actual failure for that prime and time. Other primes are untested here. |
| Reflected super-Gaussian | Its logarithmic derivative grows polynomially, so the displayed exponential confinement inequality fails at large \(|u|\). Its coefficient inequality is untested. |
| Smooth shape and positive-primitive controls | The exact square summand score is absent. The catalog constructs these witnesses for sufficiently small positive damping. Their satisfaction of the weaker confinement and coefficient bounds remains untested. |
| Finite-prime square sources | Full canonical reflection is missing. The score and domination can persist for bounded positive weights with an admissible even locally absolutely continuous extension. |
| Finite-profile threshold families | Atomic examples lack a positive density and score. Triangular compact extensions lack a globally positive density for \(V=-\log w\). Those failures do not decide their individual coefficient inequalities. |
| RH-conditional endpoint controls | Ordinary Dirichlet arithmetic and the unchanged theta summand formula are absent. The construction retains its RH hypothesis. Its coefficient comparison is untested. |
| Varied readout with fixed amplitude | The score and recurrence are identical. The altered observation lacks the literal cosine and its Newman equation. |
| Actual-profile positive-measure relaxation | Its measure of admissible heights does not supply the positive full-line theta density, modewise score or physical Fourier field. The relaxation is not a tested coefficient deformation. |

The [internal assessment](../reviews/02_VCD_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md)
records the review. Sharp asymptotics, growing-index stability and the
transfer to source-distinguishing signed observables remain open.

The bounded cross-manuscript response made the time-zero normalizing
identity explicit through the primitive endpoint and the split theta
Mellin integral. It also specifies that sharp depth and certified
coefficient precision remain open while the fixed-chain result gives
a sufficient depth with exact coefficients.
