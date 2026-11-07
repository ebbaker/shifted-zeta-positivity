# Research overview and plan for theta observables and Newman dynamics

**Operator/imaginary-time scope clarification and branch setup — 6 November
2026.** Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra/max**, direct chat0005. The author means Hamiltonian evolution
in the imaginary-time/heat-type sense and requested a distinct branch
because the count approach already has a substantial research history.
[Branch 03](../03_operator_imaginary_time_evolution/README.md) owns the new operator question through
[its overview](../03_operator_imaginary_time_evolution/research-overview/01_OPERATOR_ITE_RESEARCH_OVERVIEW_20261106.md), [bounded plan](../03_operator_imaginary_time_evolution/research-plan/01_OPERATOR_ITE_RESEARCH_PLAN_20261106.md) and [sole TND-O register](../03_operator_imaginary_time_evolution/research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md).
The [continuation](../03_operator_imaginary_time_evolution/notes/01_OPERATOR_ITE_CONTINUATION_AND_PROMPT_20261106.md) preserves the exact baseline X² / −∂²_k /
L⁻¹X²L and leaves operator/space/target selection unactivated.

Shared TND-E01/E03 identities stay at the parent. Branch 01 retains TND-D
count work and branch 02 retains TND-A auxiliary work; no issued request
or evidence is moved or superseded. See the [dated crosswalk](../03_operator_imaginary_time_evolution/research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md).
The earlier two-branch plans below remain historical specifications,
not an instruction to impose measurement or real-time unitarity on TND-O.

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

**Shared analytical background — 6 November 2026, gpt-6-astra/max:** [The TND-E06 manuscript](../manuscript/README.md) supplies the common analytical foundation requested for both branches. [Review02](../reviews/02_SHARED_ANALYTICAL_BACKGROUND_MANUSCRIPT_REVIEW_20261106.md) distinguishes accepted E01/E02 construction results from the later direct diagnostic work and the auxiliary conditioning target, using a recorded 01:53 America/New_York status cutoff. This synthesis changes no branch evidence level or live status. The original plan/specifications below remain historical; consult each branch register for continuation.

**Current shared assessment — 6 November 2026, gpt-6.1-sol/ultra:** [TND-E03 r2 Review01](../reviews/01_TND_E03_R2_GEOMETRY_SOURCE_AND_TRANSPORT_ASSESSMENT_20261106.md) accepts parent E01 r1 within its stated geometric/spectral comparison and source-defined transport scope, without a required mathematical correction. It records the ordinary-heat versus scalar-comparator generator factor explicitly. This is internal same-model assessment with shared premises; supplied scan/encoding and physical adaptation limits remain. The shared prerequisite is now available to both branch E02 assessments; neither is activated or assessed here. [Continuation/model-change guidance](../research-progress/handoffs/03_TND_E03_R2_RETURN_AND_MODEL_CONTINUATION_20261106.md) recommends TND-A-E02/Sol for the current auxiliary continuation. The [shared register][progress] owns status; the issued request text and earlier planning/evidence snapshots below are retained historically.

**Research overview revision 5; original analytical plan r1 retained historically, with author-directed branch plans r1 and shared E03 r2.** The author has selected MC11's full angular–radial Dirac-square model on the spherical cylinder as the starting point for adapting the framework of `05_radial_theta_collision_geometry`. Understanding its Hamiltonian as naturally as possible is a leading priority. Direct representation of Newman flow through radial spectral modes and a natural auxiliary flow remain open avenues. The author now requests a research plan emphasizing analytical work that can extend to infinite order or index. [Planning decisions][planning-decisions] record the transition from the [model clarification][clarification]. Prepared on 5 November 2026 for Edward Baker with substantial LLM assistance, gpt-6-astra/max, Investigation08 chat0001.

**Original two-branch organization, 5 November 2026:** the author requested both numbered research branches, each with an overview, plan and progress file. [Direct Newman realization](../01_direct_newman_realization/README.md) owns TND-D tasks; [Hamiltonian auxiliary dynamics](../02_hamiltonian_auxiliary_dynamics/README.md) owns TND-A tasks. The [shared register][progress] owns shared TND tasks and the dated crosswalk. B01 completed comparison/branch planning; physical construction choices remain in the two branch B01 tasks. See [Decision04](../brainstorm/notes/04_TND_B01_TWO_AVENUE_DECISION_AND_BRANCH_PLANS_20261105.md).

Planning update: 5 November 2026, prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra/ultra**, chat0003. E01 remains complete at proof-author comparison scope. No E02 request was issued or executed, and no numerical work or external status update is part of this change.

## Motivation and common ground

The starting physical model is the geometric Dirac operator and its square on the complete spherical cylinder in [MC11 Section 2][manuscript]. Its radial Green response supplies the inverse angular multiplicity and recovers the theta sum. Sections 3 and 8 provide the supporting measurement dictionary and Newman observations. The central question is how the model's Hamiltonian, fields and natural evolutions connect to the theta source and the Newman family. Preparation and measurement are to be understood within that model.

[Investigation05][radial] approaches the source through radial geometry, potentials, spectral observations and conservative evolution. Both constructions already use the product metric with sphere radius 1/2. MC11 acts on spinors, while Investigation05's generating field and elliptic operator are scalar. The task is to understand that relationship, including the physical radial coordinate, source coordinate, measures and observations, and use the new spinor model to develop the Newman interpretation.

Placing this investigation directly under `investigations-5` reflects that shared origin. It can also draw on the auxiliary-flow and collision-dynamics work without becoming a continuation of only one existing proof program. The earlier [MC11 brainstorm][origin] is the founding synthesis; its tentative nested folder proposal is superseded by the author's choice of this location.

## Background to carry forward

| Source | Contribution to this investigation | Scope to retain |
| --- | --- | --- |
| [MC11 cylinder and source manuscript][manuscript], with [AR-E04 assessment][ar04] | Angular Dirac spectrum, radial Green response, complete source/moment identities, bounded-potential comparison and signed-transfer limitations | The stated operator/source results are accepted within scope by internal LLM assessment; no growing-order determinant sign is supplied |
| [MC11 observable Note13][observables] | Conditional angular state, energy filter, measured source polynomial, Newman normalization and signed collision observations | Proof-author analytical checks only; OBS-E01 remains pending. Manuscript inclusion does not supply that assessment |
| [Investigation05 companion][book] and [its rewrite assessment][book-review] | Radial theta potential, source-defined generator, cylinder observation, inversion and the specified Newman/cylinder-heat comparison | Same-assistant analytical checking. The source-defined Newman evolution is not ordinary cylinder heat; the tested linear combination transports existing zeros on its admitted interval |
| [Conservative source diffusion, Note25][conservative] | A flow preserving the complete signed observation, with altered leading diffusion signals at a collision | This diagnostic also occurs for admitted colliding controls. Conservation alone is not an exclusion mechanism |
| [October moving-state work][moving] and [score-jet work][scores] | Normalized theta state, its Newman tangent, Ward identities, gap limits and the recorded sign change of a fitted score residual | These constructions predate the new cylinder dictionary. Their mixed oscillatory terms remain uncontrolled; a tested residual sign failure is scoped to that argument |
| [Investigation04 radial collision analysis][radial-coeff] | Sturm–Liouville representation and local collision interpretation | H is a spectral coefficient in that representation, rather than the operator's characteristic function; simplicity of the operator spectrum does not prove simplicity of H's zeros |
| [Investigation06 approach summary][auxiliary] | Lessons from auxiliary source perturbations, normalized responses and signed square-mode damping | A useful response still needs a justified consequence for the original H. The reported failures concern the specified responses and recovery scales, not all auxiliary models |
| [Newman reductions and certificates][newman-results] and [Investigation02][applications] and [Investigation03][collision-bounds] | Existing zero-dynamics consumers, threshold reductions and quantitative coverage questions | Any eventual mathematical gain must be compared with existing coverage and its exact hypotheses |

The linked proof notes and assessments determine the evidence level. This overview imports their scope without assessing their proofs again. The [result-summary index][results], particularly [theta identities][theta-results] and [collision controls][controls], provides the wider background map.

## The selected cylinder model and Hamiltonian question

With D the unit-sphere Dirac operator and Gamma its chirality, the model is

\[
C=\mathbb R_v\times S^2,\qquad g_C=dv^2+\tfrac14g_{S^2},\qquad
\mathcal D_C=-i\Gamma\partial_v+2D,\qquad
L_0=\mathcal D_C^2=-\partial_v^2+4D^2.
\]

The free operator combines the radial and angular degrees of freedom while remaining separable. L0 is the positive geometric kinetic operator whose Hamiltonian interpretation is a priority. Its Green response is a derived observation of the full model. The angular conditional ensemble is a supporting interpretation of that observation.

Investigation05 instead uses the scalar operator \(\mathcal L_{\mathrm{sc}}=1-\Delta_C\), with \(\mathcal L_{\mathrm{sc}}G_\lambda=8e^{\lambda u^2}\Phi\) and the source-defined evolution \(\partial_\lambda G_\lambda=\mathcal L_{\mathrm{sc}}^{-1}u^2\mathcal L_{\mathrm{sc}}G_\lambda\) in the canonical radial sector. The common metric does not identify the scalar and spinor operators. Relating their fields, source maps and evolutions is the proposed adaptation.

The author proposes studying the cosine observation through radial eigenfunctions as one avenue toward representing Newman flow itself. On the complete free line these are continuous generalized modes: for real k and \(D^2\chi_n=n^2\chi_n\), \(L_0[\cos(kv)\chi_n]=(k^2+4n^2)\cos(kv)\chi_n\). The identity \(-\partial_k^2\cos(kv)=v^2\cos(kv)\) explains the familiar Fourier connection to source reweighting, once the source and physical radial coordinates are related. It does not yet supply a physical Hamiltonian evolution. A natural auxiliary flow suggested by the same model remains an equally open avenue, to be compared by its interpretation and useful effect on the original observation.

## The concrete observable dictionary

### Angular energy and the theta source

Use the MC11 normalization as an initial reference model. Let D be the unit-sphere Dirac operator, \(A=D^2\), and K its angular spinor Hilbert space. The complete radius-1/2 cylinder has

\[
L_0=-\partial_v^2+4A,\qquad W=(4\sqrt A)^{-1},\qquad
B_s=P_1+s(I-P_1),\quad 0\le s\le1.
\]

Here \(P_1\) projects onto the lowest angular shell. The levels of A are \(n^2\), with multiplicity \(4n\). The radial Green diagonal supplies W, whose weight cancels that multiplicity. The filtered angular response is

\[
Q_s(\beta)=\operatorname{Tr}_K(B_sWe^{-\beta A})
=e^{-\beta}+s\sum_{n\ge2}e^{-\beta n^2},\qquad
\rho_{s,\beta}=\frac{B_sWe^{-\beta A}}{Q_s(\beta)}.
\]

The complete theta constant is \(\vartheta_3(0,e^{-\beta})=1+2Q_1(\beta)\). The missing zero mode is explicit in the additive 1. In these units the angular contribution to \(L_0\) is \(4A\), so its inverse temperature is \(\beta/4\).

Note13 specifies an ideal preparation: begin with the angular Gibbs state \(e^{-\beta A}/Z_{\mathrm{ang}}\), and condition on the effect \(F_s=B_sA^{-1/2}\). Its eigenvalues are 1 on the first shell and s/n thereafter. The acceptance probability is \(4Q_s/Z_{\mathrm{ang}}\), and the conditional state is \(\rho_{s,\beta}\). This specifies an operator-level measurement protocol, including the calibration needed to recover the absolute response; a detector implementation has not been derived. It uses the compact angular system, since the full noncompact cylinder has no normalized finite-temperature Gibbs state.

For source coordinate \(u\ge0\), set \(\beta=\pi e^{4u}\). The first two energy moments give

\[
\mathcal O_\beta=2\beta^2A^2-3\beta A,\qquad
\Phi_s(u)=e^uQ_s(\beta)\langle\mathcal O_\beta\rangle_{\rho_{s,\beta}}.
\]

The operator is positive on this source range, where \(\beta\ge\pi\). The source derivative uses the cubic polynomial \(-8\beta^3A^3+30\beta^2A^2-15\beta A\). Thus the source and its logarithmic slope have explicit energy-observable meanings. Their recovery is a scan over angular damping; it does not identify that control parameter with the physical radial coordinate.

### The Newman transform and collision observations

Fix the complete source \(s=1\), and write \(\Phi=\Phi_1\). Its canonical expression is

\[
\Phi(u)=\sum_{n\ge1}\left(2\pi^2n^4e^{9u}-3\pi n^2e^{5u}\right)
e^{-\pi n^2e^{4u}}.
\]

The complete theta identity extends it as a smooth positive even source. In the inherited normalization,

\[
H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du,\qquad
H_0(z)=\frac18\xi\!\left(\frac{1+iz}{2}\right),\qquad
\partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]

Substituting the energy formula makes H an exact signed scan of angular responses. The complete source tail controls the integrals and finite derivatives on compact parameter sets. Definitions and the normalization crosswalk are recorded in [Note13][observables] and the existing [reference guide][references].

The earlier moving-state construction uses

\[
Z_\lambda=H_\lambda(0)>0,\qquad
\mu_\lambda(v)=\frac{e^{\lambda v^2}\Phi(v)}{2Z_\lambda},\qquad
\psi_\lambda(v)=\sqrt{\mu_\lambda(v)}.
\]

For position operator X and real Fourier parameter a, the two relevant observations are

\[
\frac{H_\lambda(a)}{Z_\lambda}=\langle\cos(aX)\rangle_\lambda,\qquad
\frac{\partial_aH_\lambda(a)}{Z_\lambda}=-\langle X\sin(aX)\rangle_\lambda.
\]

A multiple real zero is simultaneous vanishing of these signed expectations. A nondegenerate double event additionally has \(H_{\lambda,aa}(a)\ne0\); higher multiplicities require more derivatives. The first expectation is also a phase-sensitive momentum-kick amplitude in the pure state \(\psi_\lambda\). A squared amplitude discards its sign. These are cancellations of observations, not collisions of the known angular energy levels.

The normalized Newman tangent is

\[
\partial_\lambda\psi_\lambda
=\tfrac12\bigl(v^2-\langle X^2\rangle_\lambda\bigr)\psi_\lambda.
\]

This multiplies by \(v^2\) and normalizes, whereas the free radial operator differentiates in v. Encoding \(\psi_\lambda\) in a fixed angular shell gives an admissible cylinder state by Note13's domain argument, but does not explain how that state is produced or how this evolution is implemented. Positive-increment multiplication by \(e^{\delta\lambda X^2/2}\) is unbounded on the full Hilbert space, so that particular operation cannot be globally rescaled into a bounded success operator. Other state-specific preparations, controllers or enlarged models remain possible subjects for discussion.

The parameter distinctions are part of any future model:

| Symbol | Meaning |
| --- | --- |
| v, X | Radial position and its operator |
| u | Source coordinate |
| beta | Angular damping, with beta = pi exp(4u) in the source scan |
| s | Angular shell-filter strength |
| lambda | Newman source-reweighting parameter |
| tau | Physical or proper-time evolution parameter of a specified model |
| a | Real Fourier observation parameter |

The shell-filter family at s=1 and the Newman-weighted family at lambda=0 both use the canonical source, but they are different deformations. General filtered sources do not automatically retain full theta reflection.

## Overall goals

**Understand the cylinder Hamiltonian from its geometry.** Develop the physical meaning of the Dirac-square operator, its radial and angular kinetic terms, spinor structure and natural evolution. Use that model to adapt Investigation05's scalar field and Newman interpretation. Explain the roles of the first-order factor, squared operator and Green observation; preparation and measurement should follow the physical interpretation being considered.

**Explain the appearance of the canonical source.** Identify which parts follow from the angular spectrum, geometry or dynamics, which are externally chosen filters, and which insert theta information directly. A prescribed theta wavefunction is a legitimate model input when labeled as such; understanding how it arises would be an additional achievement. A changed potential, coupling or geometry in this investigation would be a new model choice, not a revision of MC11's accepted fixed model.

**Compare direct Newman representation with a natural auxiliary flow.** Study the author's radial-eigenfunction avenue for the cosine kernel and ask how Newman flow acts in the resulting representation. Also consider a natural auxiliary evolution from the cylinder Hamiltonian or a justified extension, following Investigation05's perspective. Neither is preselected. Keep the exact connection to H and distinguish physical time, angular damping and Newman time.

**Look for useful mathematical information in the observations.** The source-score formula connects energy moments to the earlier Ward hierarchy. Radial geometry may provide another way to relate the signed value and derivative observations. The question is whether either structure makes a concrete identity, quantitative estimate or collision diagnostic accessible that was not available from generic positivity alone. A physical-model result can be valuable before any exclusion theorem; a claim about zeros needs its own source-sensitive argument and stated parameter range.

**Place any later result in the existing zero-dynamics problem.** A local response, bounded noncollision region, all-height statement and global Newman-threshold conclusion are different outcomes. Existing reductions can explain the consequence of a future estimate once its scope is known. No global target is being replaced by a newly named criterion here.

## Analytical scope and evidence

The author's priority is analytical progress that can extend to infinite order or index. The physical object is the complete angular–radial cylinder model. The following requirements govern every task:

- **Complete angular spectrum:** work with all n>=1, both Dirac signs and the correct multiplicities. A channel calculation must use symbolic arbitrary n, with bounds sufficient for any claimed infinite angular sum.
- **Complete radial spectrum:** use the continuous spectral resolution on the full line, with the even cosine sector where appropriate. A finite box, boundary condition or confining potential is a new model choice, not a harmless discretization.
- **General derivative or moment order:** where such an order occurs, seek an identity, recurrence or estimate for arbitrary finite order, recording its dependence on that order. Finitely many checked cases do not supply an induction or an infinite-order theorem.
- **Separate quantifiers:** a statement for each finite order is different from a uniform bound as the order grows. Likewise compact-parameter control, an infinite angular sum, an infinite Taylor expansion and an all-height result need their own convergence or uniformity arguments. No dimension-free bound is demanded when an explicit order-dependent bound suffices.
- **Preserve the source and observation:** use the complete canonical source, its actual cosine kernel, normalization, endpoints and tails. Keep u, v, beta, lambda and physical time distinct until an explicit map relates them. Source integrals may be entire where generating-field integrals initially converge only in a strip.
- **Analytical work first:** symbolic checks may verify an identity valid for arbitrary indices. A finite numerical experiment requires a later bounded request stating the general hypothesis, what it decides and its stop rule. No numerical campaign, finite-mode fit or sequence of low-order determinants is part of this plan.

The physical interpretation is a legitimate outcome before a zero theorem. Reuse established operator and source results instead of repeating their proofs. Label a new interpretation, a new identity, a quantitative gain and a scoped failed mechanism separately. A criterion equivalent to the target is classified once under [avoid/01][a01]; its reformulation is not evidence for it. The [result index][results], [Newman cluster][newman-results], [control cluster][controls] and [patterns index][avoid] govern the mathematical claims, including [numerics before a question][a10] and [tests of known coverage][a11].

## Research plan

**Historical plan r1 and current crosswalk.** The original single-route sequence below is preserved as issued. The author-directed split on 5 November 2026 replaces its unissued E02/B02/E04/E05 follow-through with the two branch plans; the shared E03 specification is revised explicitly to r2 below. Current status belongs only to the designated shared/branch registers. Original B01 remains readable as the completed comparison specification.

**Plan r1, 5 November 2026.** The [sole progress register][progress] owns live status, activation and returns. This overview owns the scientific plan and task specifications. The recommendations follow [GPT_RESEARCH_MODEL_WORKFLOW][workflow]; the author chooses the actual model, effort and chat. Planning does not activate later research or dispatch work.

The opening discussion **TND-B00** is complete at its planning scope: the author selected the Dirac-cylinder model, Hamiltonian priority, two flow avenues and general-index analytical standard. The Hamiltonian and flow questions themselves remain open in the tasks below.

| ID and purpose | Type and recommended model | Dependency and readiness at plan issue | Deliverable and completion standard |
| --- | --- | --- | --- |
| [TND-E01](#tnd-e01) — geometric Hamiltonian and complete spectral comparison | E — Sol; operators, comparison and derivation route are fixed | Complete at proof-author comparison scope; [Note02][e01-return] | Complete resolutions, domains, source chain and adaptation gaps; new statements await E03 |
| [TND-B01](#tnd-b01) — Hamiltonian interpretation and first flow contract | B — Astra; the physical meaning and useful evolution remain conceptual | E01 return, retaining its evidence level | Compare the direct Newman and auxiliary avenues; select one bounded analytical follow-through or identify the unresolved premise |
| [TND-E02](#tnd-e02) — full-spectrum realization of the selected flow | E — Sol; execute the route fixed by B01 | Reserved until B01 issues an executable request | One general-index evolution/observation theorem or a scoped failure of the specified construction |
| [TND-E03](#tnd-e03) — assess the Hamiltonian and flow derivations | E — Sol; proof and domain obligations are fixed by the returns | E01 and E02 returns; exact consumed inputs identified | Claim-by-claim internal assessment, corrections and retained scope |
| [TND-B02](#tnd-b02) — select an analytical consequence | B — Astra; choose what the model makes easier to prove | E03 disposition and a usable model or precisely scoped limitation | One target with an analytical route, order/index dependence and a consequence for the original observation, or a reason to stop that route |
| [TND-E04](#tnd-e04) — prove the selected estimate or relation | E — Sol; fixed theorem and proof method from B02 | Reserved; no executable estimate has been selected | A proof on the declared complete family, or the exact unpaid/failed premise |
| [TND-E05](#tnd-e05) — assess and integrate the analytical result | E — Sol; fixed proof assessment and propagation | E04 return | Assessed result, scoped conclusion and concise integration into the research record |

The default dependency sequence is **E01 → B01 → E02 → E03 → B02 → E04 → E05**. This is a research outline, not a promise that every stage will become executable. A scoped failure may complete an E task. B01 may leave both avenues open while issuing one common missing-lemma task; it need not commit the whole investigation to one flow. If E01 exposes a consequential model ambiguity, retain its completed derivations and take that ambiguity to B01 before the dependent work.

### TND-E01

**Geometric Hamiltonian and complete spectral comparison — request r1. Type E; recommended Sol.** The objective and method are fixed: derive the geometric and spectral comparison of the existing cylinder operators, then identify the precise map required by the Newman interpretation. Inputs are MC11's [operator derivations][mc-free], [selected cylinder contract][mc-contract], [source derivations][mc-source], [assessment][ar04] and manuscript Section 2; Investigation05's [companion source][book-source] and [assessment][book-review]; and the [author clarification][clarification]. Reuse their accepted results with attribution. Note13's pending assessment is not a prerequisite for this baseline.

Use the fixed radius-1/2 complete product cylinder, its spinor Hilbert space and metric-volume conversion, D and Gamma, L0, and the scalar operator Lsc=1-Delta_C. Keep the current free operator and calibrated Green response. The proof route is the product spin connection/Dirac square, angular separation, radial Fourier resolution and the existing source map.

Use smooth compactly supported spinor sections with finite angular support as the computational core and reuse the accepted self-adjoint realizations of the cylinder Dirac operator and L0. Justify the scalar comparator's realization and any additional domain assertion. For the source transforms retain the canonical Phi on arbitrary compact real lambda intervals, with the polynomial insertions needed at each finite order. Distinguish compact complex-z convergence of the source transform from the initial strip |Im z|<1 for the G-field integral. The comparison is on the complete radial line and all n>=1 throughout.

1. Derive the geometric kinetic and curvature terms with consistent conventions, checking any additional geometric identity against a primary source. Explain L0 as a positive kinetic Hamiltonian up to an explicitly stated physical unit factor. Distinguish its first-order Dirac factor, unitary evolution, Euclidean heat evolution and resolvent without selecting an additional interaction.
2. Give the complete radial spectral transform and inverse, including the even cosine normalization and channel dispersion for arbitrary n. Compare with the scalar spherical-harmonic channels of Lsc. Reuse the established self-adjoint domains; justify any additional domain assertion. Generalized modes are not normalizable radial eigenstates.
3. Trace the existing chain from the full radial Green response to Q1, the source map and Investigation05's scalar G. Record every supplied substitution, measure, endpoint and boundary condition. State exactly what remains unproved about identifying the source coordinate with physical radial position or obtaining a scalar field from spinor data.
4. On the appropriate source class, place the radial kinetic action beside multiplication by the squared source coordinate and the transported Newman generator. Give the relevant relations for arbitrary finite derivative order, using accepted complete-source majorants where available and stating order dependence. This comparison must not assert a bounded positive-Newman-time operator on all L2 or a global unitary realization that has not been derived.

**Output and completion:** one dated analytical note in `notes/`, with a table of inherited, newly derived and unresolved statements, and proof-author checks. Completion is a full-spectrum comparison and an explicit adaptation question, not a collision estimate. Preserve pending observable claims as such. **Work limit:** one fixed comparison of these two operators, one derivation pass and one local correction pass; no model survey or numerics. Ordinary algebra, normalization and domain refinements are allowed. A changed source, geometry, readout, interaction or proposed physical law returns to **B01**. The source claims remain at their existing review levels; new claims await E03.

### TND-B01

**Hamiltonian interpretation and first flow contract — Type B; recommended Astra.** Consume E01 with its proof-author qualifications. The unresolved choice is how the geometric Hamiltonian can explain the Newman deformation or support a useful auxiliary dynamics. Compare at most two concrete constructions: one pursuing the author's direct radial spectral avenue, and one auxiliary flow motivated by the same Hamiltonian or a clearly declared extension.

For the direct avenue, specify the evolved object, generator, time parameter, source/readout map and the relation producing the Newman equation. Distinguish a natural physical interpretation from conjugating the known scalar flow into new notation. For the auxiliary avenue, specify its purpose and whether it preserves H, preserves zeros through a nonvanishing factor, permits recovery, or yields a justified comparison. Use Investigation05's heat/linear benchmarks and the [auxiliary-flow lessons][auxiliary] with their original scopes.

**Output and completion:** one concise note in `brainstorm/notes/` selecting a first bounded follow-through, a common missing lemma, or an explicit unresolved choice. A selected construction must specify its complete spectral/index range, domains, supplied theta data, observation and analytical method, plus the evidence that would count as success. Physical explanation alone is permitted if named as that outcome. Issue **E02 for Sol** only when these items are fixed; an available source-sensitive estimate is not required in advance. **Work limit:** the two named avenues and one conceptual comparison; at most one motivated extension in the selected next request. A third mechanism or changed objective needs a dated B01 revision. No potential fitting, numerical search or automatic execution follows this discussion.

### TND-E02

**Full-spectrum realization of the selected flow — Type E; recommended Sol; conditional specification.** B01 must first freeze one generator/construction, field space, source and observation, parameter domain, proof method and completion test. It must also enumerate precisely which E01 and external claims the derivation consumes. Until then this task is reserved, not executable.

Carry out that analytical construction for the complete angular and radial spectra. Prove the evolution/observation relation and the convergence, domain and endpoint statements it actually needs. Where derivatives or moments are used, provide a formula or recurrence for arbitrary finite order with sufficient bounds for the claimed interchanges and limits. Pay an infinite sum or expansion explicitly rather than inferring it from the existence of each finite derivative. Identify normalized-state terms and any conditioning or controller assumptions if the selected model uses them.

**Output and completion:** one analytical note proving the declared representation/flow statement or locating a precise obstruction in its specified class. If an exact construction is replaced by an approximation, B01 must authorize its norm, uniformity and error target before execution. **Work limit:** one frozen construction, one proof pass and one local correction pass, with no added parameter sweep. Routine refinements within the fixed method remain E work; a structural source/operator/observation change returns to **B01**. A representation theorem does not by itself establish a signed bound.

### TND-E03

**Current request r2 — shared E01 assessment only. Type E; recommended Sol.** The author requested separate direct and auxiliary branches, each with its own realization assessment. Consume E01 Note02, its frozen input/return records and the exact inherited MC11/Investigation05 evidence versions. Audit E01's product geometry and curvature/unit conventions, complete signed Dirac and scalar spectra, Fourier/cosine normalization, maximal domains, source/readout chain, endpoints, arbitrary finite-order bounds, and the kinetic/Newman distinction. Identify every consumed premise and retain pending external observable claims as pending.

**Output/completion:** one shared review in reviews/, with claim-by-claim accepted-within-scope, conditional, correction-needed or failed dispositions and a reusable input-version record. This does not assess an unexecuted branch construction or close MC11 tasks. **Limit:** one assessment and one local correction check. Routine proof repairs remain with E01; a changed physical model goes to the relevant branch B01. Record actual model/effort and shared-premise provenance. This request is ready from E01 but unactivated; freeze actual input hashes at activation. Branch E02 assessments depend on this shared disposition for their inherited E01 claims.

**Historical r1 specification (superseded only as a joint assessment request):**

**Hamiltonian and flow assessment — Type E; recommended Sol.** Once the E01/E02 statements are fixed, check their exact versions against the inherited inputs. Assess geometry and spinor/scalar distinctions, self-adjoint or stated evolution domains, generalized spectral normalization, complete sums, arbitrary-order quantifiers, parameter distinctions, source/readout transfer and scope of any obstruction.

**Output and completion:** one review in `reviews/` accepting, correcting or rejecting each material claim. Distinguish source-independent representation facts from any canonical estimate. A consumed Note13-only statement must receive a declared local proof/check or rely explicitly on its completed MC11 assessment; an unresolved premise stays conditional. This task does not close MC11-OBS-E01 or alter any MC11 status. **Work limit:** one assessment and one local correction cycle. Routine repairs remain with E01/E02; a changed model or flow returns to **B01**. Identify actual reviewer model and shared premises; internal LLM assessment is not specialist independence.

### TND-B02

**Select an analytical consequence — Type B; recommended Astra.** From the E03 disposition, ask what statement about the original theta observation becomes more accessible through the model. A suitable target could be a general-order signed identity with a separately estimable term, an explicit order-dependent error or conditioning bound, a source-sensitive restriction on a stated domain, or a matched analytical improvement over direct evaluation. Repeating the known Fourier/Newman identity is not that gain.

**Output and completion:** one `brainstorm/notes/` decision giving the target, physical consequence, complete index/order range, intended quantitative scale, analytical method and distinguishing source input. Classify it as physical interpretation, intermediate estimate, diagnostic or target-equivalent reformulation. Apply the [registered controls][controls] and the counter-kernels in [Newman reductions][newman-results] to the actual premises, naming what each relevant control fails. For exclusion, the claimed estimate must reject a control on a domain containing its witness; generic positivity or literal naming of theta is insufficient. If a bounded estimate is proposed, compare with existing coverage and same-information methods.

**Work limit:** at most two analytical mechanisms for one stated target. Freeze **E04 for Sol** only if a tractable proof route and finite work limit emerge. Otherwise record the missing input or a scoped stop without inventing a theorem to execute. A model change returns to **B01**. MC11's growing-order determinant task E05 remains outside this investigation unless a later author decision expressly changes that scope.

### TND-E04

**Selected analytical estimate or relation — Type E; recommended Sol; reserved.** This becomes executable only with B02's explicit theorem, input versions, parameter/index range, proof method and success scale. Prove that statement for the declared complete family. State dependence on every growing index; retain signed cancellations, all boundary terms and complete error costs. An asymptotic result needs its quantified regime and remainder; a finite constant is evaluated only when the selected consequence requires it.

**Output and completion:** a proof note, or an exact account of the failed estimate/unpaid term within the fixed method. Conditional conclusions retain their named hypotheses. **Work limit:** one theorem or recurrence family and one local repair pass, as narrowed by the issued request; no finite-case campaign or silent enlargement of the target. Ordinary analytical refinements remain E work. A new estimating mechanism or changed target returns to **B02**, and a model change to **B01**.

### TND-E05

**Assessment and integration — Type E; recommended Sol.** Assess the exact E04 proof, quantifiers, order dependence, complete limits, controls and claimed consequence. Compare any proposed gain with its declared baseline. **Output and completion:** one review and a concise integration of the assessed result into this overview, the sole progress register and DRAFT_HISTORY. Update the result/pattern indexes only when their milestone requirements are met, retaining source status words. Manuscript production is a separate author-selected action.

**Work limit:** one assessment and one correction/integration cycle; no new proof mechanism or numerical campaign. A changed estimate returns to **B02**; routine proof corrections stay with **E04**. Completion may be acceptance within scope, a narrower result or a scoped rejection. Record actual model/effort and review independence accurately.

## Execution and record keeping

At activation, freeze the selected request revision and exact consumed source versions; a small record belongs in `research-progress/handoffs/` when needed. Preserve issued requests and append returns rather than overwriting failed evidence. Each return records actual model/effort, identities or estimates proved, the precise index/parameter scope, unresolved premises, status and next B/E task. The author controls task activation and model choice; this plan does not create chats or agents.

Analytical derivations go in `notes/`, conceptual decisions in `brainstorm/notes/`, assessments in `reviews/`, and code/small numerical records in `numerics/` only when authorized by a bounded request. Follow the [reference workflow][reference-workflow], reusing the existing catalogs and keeping reading PDFs outside Git. The existing source notes and MC11/Investigation05 registers remain in place. Keep one evolving overview and sole progress file per shared/branch task family, with concise milestones in DRAFT_HISTORY and no manuscript snapshots. The parent owns TND, the direct branch TND-D, the auxiliary branch TND-A, and the operator/imaginary-time branch TND-O.

**Historical continuation at revision 5 issuance:** consult the two branch registers for TND-D-B01 and TND-A-B01. Shared **TND-E03 r2 — Sol** was ready and unactivated. The issued E01 request above is preserved, with exact activation text in its [input record][e01-inputs]. No branch execution request is issued by this overview.


## E01 comparison return — 5 November 2026

[Note02][e01-return] derives L₀=∇*∇+2 and states its conventional kinetic unit factor. Complete spinor channels have k²+4n², multiplicity 4n; scalar channels have k²+(2ℓ+1)², multiplicity 2ℓ+1. The full radial Fourier integral, signed Dirac projectors, cosine normalization and scalar domains are explicit. The supplied Green response recovers Q₁ and, through the external β(u) scan and scalar inverse, Φ and G_λ. This is a construction from spectral-response data, with physical spinor-field/state preparation and v=u still unresolved. Radial kinetic action is diagonal in k, whereas Newman multiplication differentiates in k; arbitrary finite-order compact-λ tail bounds justify that comparison. The source transform is entire, while the raw G integral initially has |Im z|<1.

These are inherited identities and new proof-author comparison results with same-model supporting checks, not a new physical flow, collision estimate or E03 assessment. The [continuation][e01-continuation] returns the precise physical field/map/time choice to B01; pending external observable claims remain pending.

## Controls and inherited limitations

The [collision-control register][controls] distinguishes the hypotheses that different sources share with theta. Positive weighted-square controls retain applicable energy and positive-source constructions but change the canonical coefficients and full reflection. Euler-factor controls retain positive even sources while changing the arithmetic. Reflected and smooth positive-source controls share substantial regularity and positivity without the unit-square arithmetic source. Atomic controls have characteristic functions but do not automatically satisfy the smooth wavefunction domains above.

A correct physical realization may also realize such controls. An exclusion argument must identify and use an additional premise that distinguishes the canonical source. Identifying theta exactly and obtaining a useful signed estimate about theta remain different accomplishments. The existing [coordinate-realization caution][a03], [target-classification rule][a01], [shape/control caution][a02] and [scoped-exclusion rule][a07] give the relevant standards within the [patterns index][avoid].

The prior score residual failure, transported-zero benchmark and pair-damping failures retain their stated classes. They help avoid repeating particular unsuccessful arguments; they do not prohibit general coupled dynamics, different observations or new source-sensitive estimates. The physical and mathematical assumptions of any future proposal should be tested together, including all preparation, normalization, boundary and complete-tail terms it uses.

## Organization and provenance

This is the evolving overview and plan, revised after the author's Hamiltonian/flow clarification and request for general-index analytical work. Issuing the plan is not a new proof or assessment. MC11's pending OBS-E01 and reserved E05 remain in MC11. Investigation05 and Investigation06 keep their existing tasks and live registers. The main MC11 manuscript and all issued source notes are referenced in place.

The [README][readme] gives folder navigation. The [research model workflow][workflow] governs the classified tasks above, and the [shared progress register][progress] contains shared continuation, return records and links to the branch status owners. The initial [brainstorm continuation][continuation] is historical where it deferred planning or recommended B00 as next. The founding conversation retains MC11 history0006; this planning chat is uniquely registered as Investigation08 history0001, with both identities documented in the [history guide][history]. Record actual model and effort in subsequent notes and reviews. The [large-file policy][large] applies; no manuscript snapshot or generated PDF is part of this planning milestone.

[manuscript]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/manuscript/main.tex
[radial]: ../../05_radial_theta_collision_geometry/README.md
[origin]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/brainstorm/notes/08_THETA_OBSERVABLES_AND_NEWMAN_INVESTIGATION_STARTING_POINT_20261105.md
[ar04]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/reviews/05_MC11_AR_E04_R1_MODEL_SOURCE_AND_SCOPED_TRANSFER_ASSESSMENT_20261105.md
[observables]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/13_MC11_BR02_R1_PHYSICAL_OBSERVABLES_AND_NEWMAN_CONNECTION_20261105.md
[book]: ../../05_radial_theta_collision_geometry/book/README.md
[book-review]: ../../05_radial_theta_collision_geometry/reviews/21_BOOK_REWRITE_ASSESSMENT_20261028.md
[conservative]: ../../05_radial_theta_collision_geometry/notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[moving]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/1_MOVING_THETA_GROUND_STATE_WARD_RESIDUAL_AND_GAP_LIMIT_20261010.md
[scores]: ../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/2_CONDITIONAL_SCORE_JETS_AND_CERTIFIED_SIGN_CHANGE_20261010.md
[radial-coeff]: ../../04_three_regime_heat_flow_dynamics/notes/21_COLLISION_MECHANISMS_IN_THE_RADIAL_REPRESENTATION_20261027.md
[auxiliary]: ../../06_auxiliary_collision_flows/notes/06_APPROACH_SUMMARY_AND_GOALS_FOR_NEXT_BRAINSTORM_20261029.md
[newman-results]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[applications]: ../../02_heat_flow_rh_applications/README.md
[collision-bounds]: ../../03_heat_flow_collision_bounds/README.md
[results]: ../../../../result-summaries/README.md
[theta-results]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[references]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/README.md
[continuation]: ../notes/01_BRAINSTORM_CONTINUATION_20261105.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[avoid]: ../../../../avoid/README.md
[readme]: ../README.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[history]: ../chat-histories/README.md
[large]: ../../../../LARGE_FILES.md

[clarification]: ../brainstorm/notes/02_DIRAC_CYLINDER_HAMILTONIAN_PRIORITY_20261105.md

[progress]: ../research-progress/01_THETA_OBSERVABLES_AND_NEWMAN_DYNAMICS_RESEARCH_PROGRESS_20261105.md
[planning-decisions]: ../brainstorm/notes/03_ANALYTICAL_RESEARCH_PLAN_DECISIONS_20261105.md
[mc-free]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/05_MC11_AR_E01_R1_ALL_INDEX_OPERATOR_AND_GREEN_DERIVATIONS_20261105.md
[mc-contract]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/06_MC11_BR01_R1_FROZEN_CYLINDER_MODEL_AND_ANALYTIC_CONTRACT_20261105.md
[mc-source]: ../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/08_MC11_AR_E03_R1_SOURCE_MEMBERSHIP_AND_ENDPOINT_PAIRINGS_20261105.md
[book-source]: ../../05_radial_theta_collision_geometry/book/main.tex
[reference-workflow]: ../../../../REFERENCE_WORKFLOW.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[a11]: ../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md

[e01-return]: ../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md
[e01-continuation]: ../research-progress/handoffs/01_TND_E01_R1_RETURN_AND_MODEL_CONTINUATION_20261105.md
[e01-inputs]: ../research-progress/handoffs/01_TND_E01_R1_INPUT_VERSIONS_20261105.json
