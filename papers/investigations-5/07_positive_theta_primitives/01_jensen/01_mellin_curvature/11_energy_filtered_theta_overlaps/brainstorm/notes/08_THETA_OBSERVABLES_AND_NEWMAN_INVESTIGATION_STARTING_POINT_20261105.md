# Theta observables and a separate de Bruijn–Newman investigation

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, MC11 history0006, thread `01a1ac6b-7e6e-7ea3-86f7-0f9fd9e3a1bd`.

The cylinder model now gives an explicit route from angular energy measurements to the theta source. A separate investigation could ask how that source is physically prepared and how its signed observations behave under de Bruijn–Newman evolution. This note collects the existing results, separates two possible research objectives, and specifies a bounded opening decision. It is a starting point for a possible new investigation; no folder or research program is activated here.

This synthesis accompanies the author's requested manuscript integration, **MC11-M01 r3, E — execution**, with recommended Sol and actual Astra/max in the existing chat. The underlying observable dictionary in [Note13](../../notes/13_MC11_BR02_R1_PHYSICAL_OBSERVABLES_AND_NEWMAN_CONNECTION_20261105.md) retains proof-author status and its pending OBS-E01 assessment. Planning below uses the repository's [B/E workflow](../../../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md). A new investigation's conceptual opening would be **B — brainstorm**, recommended Astra.

| Next task | Type | Recommended model and reason | Readiness | Deliverable |
| --- | --- | --- | --- | --- |
| MC11-OBS-E01 r1 | E | Sol; the existing observable formulas and scope checks are fixed | Ready, not activated | Assessment of Note13 and any corrections needed by the manuscript |
| Proposed Newman observable investigation opening | B | Astra; choose a physical realization question or a signed-correlation mechanism | Requires the author's selection of the new investigation and objective | One explicit model or proof contract, or a scoped account of the missing premise |

## Why a separate investigation could help

MC11 studies energy filtering, source moments and growing-order signed determinants. Its current cofactor and reference-margin questions remain open. Newman evolution instead changes the source by a Gaussian factor and asks about the moving zeros of its Fourier transform. Although both use the same canonical source, the filter parameter and Newman parameter generate different families.

Two legitimate aims should be kept distinct. **Physical model development** would specify degrees of freedom, preparation, generator and measurement that reproduce the source and its evolution. It could improve the interpretation even without a zero theorem. **New mathematical control** would obtain a source-sensitive restriction on signed observations near a candidate collision. A prepared theta state is useful for the first aim; by itself it does not complete the second.

A new folder would therefore have its own question and progress register, while importing MC11's accepted response/source results and its explicitly unassessed observable extension. MC11's reserved E05 signed-determinant task should remain in MC11.

## Exact starting dictionary

Use the unchanged radius-1/2 complete cylinder, full radial line and fixed Green probe. Let
\[
A=D^2,\qquad L_0=-\partial_v^2+4A,\qquad
W=(4\sqrt A)^{-1},\qquad B_s=P_1+s(I-P_1).
\]
The angular energy levels are \(n^2\), with multiplicity \(4n\). The normalized response state and its trace are
\[
Q_s(\beta)=\operatorname{Tr}(B_sWe^{-\beta A}),\qquad
\rho_{s,\beta}=\frac{B_sWe^{-\beta A}}{Q_s(\beta)}.
\]
The complete theta constant is \(1+2Q_1(\beta)\). The effect \(B_sA^{-1/2}\) on an angular Gibbs state yields exactly \(\rho_{s,\beta}\) conditional on acceptance; the acceptance probability is \(4Q_s/Z_{\rm ang}\). This is an ideal specified measurement, with an absolute calibration and an implementation still to be supplied if an experimental model is intended.

The source is reconstructed by the energy observable
\[
\mathcal O_\beta=2\beta^2A^2-3\beta A,\qquad
\Phi_s(u)=e^uQ_s(\beta)\langle\mathcal O_\beta\rangle_{\rho_{s,\beta}},
\quad \beta=\pi e^{4u}.
\]
For \(u\ge0\), this operator is positive. The first source derivative uses the cubic energy polynomial \(-8\beta^3A^3+30\beta^2A^2-15\beta A\). Consequently the logarithmic source slope in the old Newman score can be written as a ratio of measured energy moments. These are the concrete connections supplied by Note13, not an all-order signed bound.

For the Newman family fix **s=1** and use the complete, even source \(\Phi=\Phi_1\):
\[
H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du,
\qquad H_0(z)=\frac18\xi\!\left(\frac{1+iz}{2}\right),
\qquad \partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]
Substitution of the energy observable gives H as a signed, weighted parameter scan. It does not make \(\lambda\) the angular inverse temperature or the cylinder's evolution time. If
\[
m_j(\lambda)=\int_0^\infty\frac{u^{2j}}{(2j)!}e^{\lambda u^2}\Phi(u)\,du,
\]
then \(m_j(0)=c_j(1)\) and \(\partial_\lambda m_j=(2j+2)(2j+1)m_{j+1}\). This is the direct connection to the coefficient problem. The complete source tail controls every fixed parameter derivative; no finite spectral truncation is the target.

Keep the variables separate:

| Variable | Role |
| --- | --- |
| v | Radial position on the cylinder |
| tau | Physical or proper-time evolution associated with the cylinder operator |
| beta | Angular damping or scaled inverse temperature |
| u | Source coordinate, related to beta by beta = pi exp(4u) |
| s | Shell-filter strength |
| lambda | Newman source-reweighting parameter |
| a | Real Fourier observation parameter |

## Earlier Newman work to carry forward

The following is a reading map to the directly relevant prior work, not a new review of the entire Newman portfolio. Its internal LLM assessment levels and imported premises remain those of the linked sources.

| Prior work | Reusable result | Boundary that matters for a new investigation |
| --- | --- | --- |
| [Moving theta state and Ward identities, 10 October](../../../../../../../../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/1_MOVING_THETA_GROUND_STATE_WARD_RESIDUAL_AND_GAP_LIMIT_20261010.md) | Exact normalized theta state, its Newman tangent, a positive supersymmetric operator and signed integration-by-parts identities | The instantaneous Hamiltonian annihilates the state and does not generate its nonzero Newman tangent. The gap estimate only supplies a small-frequency zero-free window. |
| [Conditional score jets, 10 October](../../../../../../../../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/2_CONDITIONAL_SCORE_JETS_AND_CERTIFIED_SIGN_CHANGE_20261010.md) | Explicit score-jet hierarchy and a certified change of sign of the fitted Gaussian-score residual on the stated time interval | Generic positivity and a scalar residual norm leave mixed oscillatory score moments unpaid. The sign-change result excludes the tested one-sign residual argument, not every source-sensitive estimate. |
| [Collision mechanisms in the radial representation, 27 October](../../../../../../../../papers/investigations-5/04_three_regime_heat_flow_dynamics/notes/21_COLLISION_MECHANISMS_IN_THE_RADIAL_REPRESENTATION_20261027.md) | An exact Sturm–Liouville representation of the source's spectral coefficient; local collision diagnostics; possible boundary/transfer questions | H is a spectral coefficient in this immediate operator, not its characteristic function. Eigenvalue simplicity therefore does not directly imply simplicity of H's zeros. |
| [Conservative source diffusion, 27 October](../../../../../../../../papers/investigations-5/05_radial_theta_collision_geometry/notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md) | An explicit local diffusion preserving the full signed observation, with extra decay of the leading source signals at a collision | The same diagnostic works for colliding controls. Conservation and the changed decay rate do not themselves exclude an event. |
| [Theta generator and cylinder heat assessment, 28 October](../../../../../../../../papers/investigations-5/05_radial_theta_collision_geometry/reviews/21_BOOK_REWRITE_ASSESSMENT_20261028.md) | Checked source-defined Newman generator and its stated combination with cylinder heat | The tested constant nonnegative combination transports existing zeros; it supplies no additional exclusion. Nonlinear or coupled constructions lie outside that scoped finding. |
| [Newman result summary](../../../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md) | Routes to collision reductions, complete-source finite certificates and the corrected asymptotic interface | Many finite windows validate machinery within already known coverage. Their existence is not a new global collision bound. |

For source definitions and the heat sign, use Rodgers–Tao's corrected [version 5 introduction, equations (1)–(4)](https://arxiv.org/html/1801.05914v5#S1). For reading-copy provenance and the related universal-factor background, see the [existing source reference record](../../../../../../../../papers/investigations-5/05_radial_theta_collision_geometry/references/14_NEWMAN_FLOW_AND_SOURCE_PERTURBATION_REFERENCES_20261028.md). The [MC11 reference catalog](../../references/README.md) records the passages and archived versions reused for Note13. Bounds from different source normalizations should not be transferred without conversion.

## The collision is a pair of signed observations

The earlier normalized state is
\[
Z_\lambda=H_\lambda(0),\qquad
\mu_\lambda(v)=\frac{e^{\lambda v^2}\Phi(v)}{2Z_\lambda},\qquad
\psi_\lambda=\sqrt{\mu_\lambda}.
\]
An explicit additional encoding into the cylinder uses \(\Psi_\lambda=\psi_\lambda\chi\), with a fixed unit angular eigenspinor. The full-line state has the finite derivatives needed for the cylinder domain. This does not prove that the Green-response experiment prepares it, and it differs from simply zero-extending the source vectors on a half-line.

For radial position X and a real observation parameter a,
\[
\frac{H_\lambda(a)}{Z_\lambda}=\langle\cos(aX)\rangle_\lambda,
\qquad
\frac{\partial_aH_\lambda(a)}{Z_\lambda}=-\langle X\sin(aX)\rangle_\lambda.
\]
The first expectation also equals the real return amplitude of the momentum kick \(e^{iaX}\). A multiple real zero is simultaneous cancellation of these two expectations. It is not a collision of the cylinder's known energy levels. Measuring only a squared amplitude would lose the relevant sign.

The normalized evolution is
\[
\partial_\lambda\mu_\lambda=(v^2-\langle X^2\rangle_\lambda)\mu_\lambda,
\qquad
\partial_\lambda\psi_\lambda=\tfrac12(v^2-\langle X^2\rangle_\lambda)\psi_\lambda.
\]
It multiplies by the squared source coordinate and renormalizes. The free radial Hamiltonian differentiates in that coordinate. A positive-time increment would formally multiply the wavefunction by \(e^{\delta\lambda X^2/2}\), which is unbounded; it is not a bounded success operator on the whole Hilbert space. Negative increments admit a bounded conditioning filter. The scope of this observation is that particular global filter implementation, not every state-specific or enlarged preparation.

## Two possible opening questions

**Physical realization.** Can the specified cylinder system, with an explicitly declared controller or ancilla if necessary, prepare the canonical radial profile and implement a finite interval of its Newman reweighting while retaining the signed observation? A useful return would name the Hilbert space, generator or instrument, initial state, domain, normalization, success probability when conditioned, and exact observed quantity. Any new potential, coupling or source coordinate must be declared. A source-dependent prepared state is allowed as a model choice, but the amount of theta information inserted into the preparation must be explicit. This objective need not claim collision exclusion to be worthwhile.

**Signed source correlations.** Does the complete unit-square angular response imply an additional relation among the two collision observations and their next derivatives? The new energy-moment formula for the logarithmic source slope is a concrete entry into the old Ward residual hierarchy. A useful return would state an inequality or closed identity with its parameter range and a derivation that uses more than generic positivity or an assumed sign of H. It must retain the actual oscillatory mixed terms and complete source tail. Merely replacing the source score by its energy-moment expression supplies a dictionary, not this estimate.

These are alternatives for the first conceptual task, rather than a commitment to pursue both. The default opening should decide which objective the author wants the new investigation to serve, compare at most these two routes using the inherited results, and freeze one bounded follow-through. A route can complete with a precisely stated missing premise. Repeated positive representations, additional low-order samples or a renamed collision criterion are not the completion condition for a signed-estimate objective.

## Controls and evidence boundaries

Read the [result index](../../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../../avoid/README.md), [re-realization caution](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [target classification](../../../../../../../../avoid/01_restating_the_target.md) and [scope caution](../../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). The [collision-control register](../../../../../../../../result-summaries/12_collision_controls_and_screening.md) supplies the relevant comparisons:

- Positive weighted-square and finite-tail controls retain the applicable energy-weighting and positive-source construction, while changing unit coefficients and full canonical reflection. Their recorded events do not imply a finite all-real Newman threshold.
- Euler-factor controls retain positive even source states and signed Fourier observations, while changing the arithmetic source.
- Reflected super-Gaussian, smooth-shape and positive-primitive controls preserve their stated positivity and regularity properties, but lack the complete unit-square arithmetic source. The generic normalized-state observation still permits their collisions.
- Atomic controls support characteristic functions and signed expectations as measures; they do not automatically satisfy the smooth wavefunction and H-squared domain assumptions above.

A physical realization that also realizes these controls can still be a correct model. A claimed exclusion theorem must identify which extra premise distinguishes theta and prove its quantitative consequence. The literal canonical source identifies the object under study; it is not itself a new sign estimate. A new investigation would not inherit acceptance merely by citing MC11: Note13 remains proof-author work pending OBS-E01, and each older source keeps its own assessment status.

## Proposed folder and opening contract

If the author chooses a separate sibling investigation, a descriptive candidate is
`12_theta_observables_newman_dynamics/` under the current Mellin-curvature directory. The name and next number should be checked again when it is actually created. Its purpose would be **theta observables, source preparation and Newman dynamics**, with growing-order determinant transfer remaining in MC11. No directory with this candidate name has been created by this note.

The initial structure can follow the repository's existing `research-overview/`, `research-progress/`, `notes/`, `reviews/`, `references/` and `chat-histories/` convention. Create numerical work only after an explicit analytical question and bounded numerical contract. Import the accepted source/response and this note through links and version records rather than duplicating their proof files. Keep one live progress register for the new investigation. Preserve each existing chat's unique registration; this chat remains MC11 history0006 unless an explicit relocation is requested.

The first **B task, recommended Astra**, should have the following fixed limits:

1. Read Note13, its eventual OBS-E01 return, the current MC11 manuscript and the directly relevant prior sources above. State which premises are accepted, proof-author or proposed.
2. Select the physical-realization objective or the signed-correlation objective. Keep the complete theta source and Rodgers–Tao normalization fixed.
3. Compare at most the two named routes. Record all new degrees of freedom or model assumptions, the observed quantities, and the actual generator or target estimate.
4. Apply the controls to those particular premises. Return one usable contract or a scoped missing-premise decision; no numerical campaign, whole-program theorem or unrequested model change.
5. If the route is fixed, issue an **E task for Sol** with exact formulas, domains, error obligations, deliverable and stop rule. Keep conceptual selection separate from execution.

A possible starting prompt, after the author selects and opens the new investigation, is:

> Read the root research instructions, MC11 Note13 and its current assessment, the updated MC11 manuscript, and this Newman brainstorm. Begin a bounded B task to choose between a concrete preparation/evolution model and a source-sensitive signed-observation estimate. Preserve the complete source, parameter distinctions, normalization, physical measurement and control hypotheses. Return one explicit follow-through contract for Sol, or the precise premise that remains missing. Do not infer collision exclusion from state positivity or from the existence of a representation.

