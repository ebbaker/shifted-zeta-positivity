# Energy-filtered theta overlaps

This investigation studies signed theta determinants through the energy-filtered box source and an angular/radial model. The new direction asks whether spherical Dirac modes, radial Green responses and a possible confining potential explain the source and provide analytic estimates that extend to arbitrary determinant order.

Start with the [angular and radial research overview](research-overview/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_OVERVIEW_20261105.md) and its [research plan](research-overview/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_OVERVIEW_20261105.md#research-plan). The plan separates the analytic assessment of the Green identities, conceptual model selection, source reconstruction and the all-order signed estimate. Numerical or low-index work is allowed only to test a written all-order hypothesis; no finite-order survey is planned.

The [sole current progress register](research-progress/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) carries both the new tasks and the existing MC11-B01/E05 continuation. The [previous register](research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md) is historical. The [original overview](research-overview/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md) retains the box model, fixed-order comparison and earlier contracts. Functions of the source coordinate are called **auxiliary source functions** unless an actual physical preparation is specified; see the [terminology note](brainstorm/notes/03_MC11_THERMAL_PARAMETER_AND_ORBITAL_TERMINOLOGY_20261104.md).

**Next: [E] MC11-AR-E01 — Sol**, the fixed analytic assessment of the angular Dirac/Green construction for all angular indices. MC11-BR01 then selects geometry, boundary, potential and observable. The inherited [B] MC11-B01 all-order cofactor decision remains a separately selectable alternative after E04. Edward Baker chooses the actual model, effort and chat under [GPT_RESEARCH_MODEL_WORKFLOW](../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md).

Overview02 and register migration: 5 November 2026, prepared for Edward Baker with substantial LLM assistance, actual **gpt-6-astra / xhigh**. The new model formulas retain proof-author status pending AR-E01.

At determinant order two, every excited level lowers the unnormalized overlap and the fractional loss from restoring the full spectrum is less than \(10^{-4}\); [E01](reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md) assessed that starting result. At order three, every excited level raises it throughout the filter path. The fractional increase is about \(1.340206\times10^{-5}\), and the first excited level supplies more than 99.99997573% of the gain. [E04](reviews/02_MC11_E04_R1_THREE_ORBITAL_RETURN_ASSESSMENT_20261104.md) now accepts the finished E02/E03 return without correction, within the canonical source and common-path premises. Both assessments are internal LLM reviews; E04 is same-assistant/same-model, with shared numerical premises and no specialist independence.

The [original research plan](research-overview/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md#research-plan) defines the evidence behind that completed order-three comparison. Its accepted results motivate the new analytic program; they establish no law across determinant orders.

## Sources

- **Box source and auxiliary representation.** The box spectrum generates the theta source. Derivative and moment functions in an auxiliary Hilbert space give its signed exterior-product pairing. [MC08 source states](../08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md)
- **Analytic comparison.** The Green identity retains the endpoint term and bounds the effects of omitted modes. [Radial Green manuscript](../10_radial_green_determinants/manuscript/radial_green_determinants.tex)
- **Origins.** The discussion that led to this folder and its three analytical notes are archived in the radial Green brainstorm. [Notes](../10_radial_green_determinants/brainstorm/notes/) · [Registered chat](../10_radial_green_determinants/brainstorm/chat-histories/0001_2026-11-04T22-28-53Z_please-read-the-manuscript-papers-investigations-5-07-posi.json)

4 November 2026. Prepared for Edward Baker with substantial LLM assistance from OpenAI Codex, recorded model **gpt-6-astra**, reasoning effort **xhigh**.

## E01 return and continuation

MC11-E01 r1 is complete without correction. [Research note](notes/01_MC11_E01_R1_PROOF_AND_RATIONAL_REPLAY_20261104.md) · [Exact replay record](numerics/MC11_E01_R1_EXACT_REPLAY_20261104.json) · [Assessment](reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md) · [Continuation and model-change packet](research-progress/handoffs/01_MC11_E01_RETURN_AND_E02_MODEL_CONTINUATION_20261104.md) · [This investigation's chat histories](chat-histories/README.md).

**E01 handoff (historical): [E] MC11-E02 — Sol**, the bounded same-path three-orbital spectral split. The E02 return below now establishes the E03 gate. E01 update: 4 November 2026, prepared for Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol / ultra**.

## E02 return and next acquisition

[Note02](notes/02_MC11_E02_R1_COMMON_PATH_SPECTRAL_SPLIT_20261104.md) and the [exact spectral-split record](numerics/MC11_E02_R1_SPECTRAL_SPLIT_20261104.json) retain E02's bounded calculation and its inconclusive first-excited/net intervals. E04 now accepts this bounded return within scope; the original calculation used Sol/ultra author checks with shared numerical premises.

**E02 handoff (historical): [E] MC11-E03 — Sol.** The five-moment acquisition gate was met, with useful target widths and a response sensitivity bound in the [continuation/model-change packet](research-progress/handoffs/02_MC11_E02_RETURN_AND_E03_MODEL_CONTINUATION_20261104.md). E03 is now complete as recorded below. E02 update: 4 November 2026, prepared for Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol / ultra**.

## E03 acquisition and completed spectral comparison

[Note03](notes/03_MC11_E03_R1_FIRST_EXCITED_ACQUISITION_AND_RETURN_20261104.md) and the [validated acquisition/replay record](numerics/MC11_E03_R1_FIRST_EXCITED_ACQUISITION_20261104.json) supply the five first-excited source moments. All width goals passed on the first 384-bit acquisition, no refinement. Both spectral groups reinforce; the higher group remains below \(5.402\times10^{-40}\). Source spatial and full energy tails are paid.

**E03 handoff (historical): [E] MC11-E04 — Sol**, assessment of the fixed finished E02/E03 return under the [continuation/model-change packet](research-progress/handoffs/03_MC11_E03_RETURN_AND_E04_MODEL_CONTINUATION_20261104.md) and [frozen versions](research-progress/handoffs/03_MC11_E04_R1_INPUT_VERSIONS_20261104.json). E03 had author checks at issuance; the E04 acceptance below is now current. No specialist review has occurred. E03 update: 4 November 2026, prepared for Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol / ultra**.

## E04 acceptance and inherited conceptual continuation

[E04 Review02](reviews/02_MC11_E04_R1_THREE_ORBITAL_RETURN_ASSESSMENT_20261104.md) accepts all specified signs, magnitudes, pointwise scopes and complete error payments without correction. [Supporting Note04](notes/04_MC11_E04_R1_RECONSTRUCTION_AND_ERROR_ACCOUNTING_20261104.md) and the [exact review record](numerics/MC11_E04_R1_ASSESSMENT_REPLAY_20261104.json) retain the analytical and separately written arithmetic reconstruction. No integration was repeated; all frozen inputs are unchanged.

**E04 handoff (retained alternative): [B] MC11-B01 — Astra**, the existing bounded analytical transfer decision, under the [continuation/model-change packet](research-progress/handoffs/04_MC11_E04_RETURN_AND_B01_MODEL_CONTINUATION_20261104.md). B01 is ready and unstarted; E05 remains reserved until B01 supplies a contract. E04 update: 4 November 2026, prepared for Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol / ultra**.
