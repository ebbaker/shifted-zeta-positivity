# Energy-filtered theta overlaps — research progress

> **Historical register as of 5 November 2026.** The author requested a new overview and corresponding progress file. Under GPT_RESEARCH_MODEL_WORKFLOW, [Register02](02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) is now MC11's sole live register and contains the task crosswalk. All task IDs, frozen requests and dated returns below are retained as historical evidence. References below to “sole live” or “current” describe the pre-migration state. Append future activations and returns only to Register02. Migration prepared for Edward Baker with substantial LLM assistance, actual gpt-6-astra/xhigh.

**4 November 2026 · Initial register, revision 1.** Prepared for Edward Baker with substantial LLM assistance from OpenAI Codex, actual model **gpt-6-astra**, reasoning effort **xhigh**. This is the investigation's sole live progress register. The [research plan](../research-overview/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md#research-plan) defines the tasks. The source notes and original chat have their existing registration in the [radial Green brainstorm](../../10_radial_green_determinants/brainstorm/chat-histories/index.json).

| Next task | Type | Recommended model | Readiness | Expected output |
| --- | --- | --- | --- | --- |
| **MC11-B01 — default next** | B — brainstorm | **Astra** for the unresolved transfer/dimension-dependent cofactor decision | **Ready after accepted E04; author selects model/effort/chat** | At most two analytical routes and one bounded E05 contract, or a scoped reason to stop |

## Starting evidence (at plan issuance)

- **Inherited inputs.** MC08 supplies the source-state pairing. The radial Green record supplies enclosures for the compact first-mode coefficients and bounds for the omitted modes and spatial exterior. The latter distinguish the compact data from the full-half-line ground-mode reference. [Source states](../../08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md) · [Green comparison](../../10_radial_green_determinants/manuscript/sections/01_green.tex) · [Input explanation](../../10_radial_green_determinants/notes/06_RGD_E02_R2_FIRST_NEXT_ORDER_RETURN_20261104.md)
- **Proof-author checks only.** The originating note derives \(D_2(0)>0\), \(\chi_2(E_n;s)<0\) for all \(n\ge2,\ 0\le s\le1\), and \(0<(D_2(0)-D_2(1))/D_2(0)<10^{-4}\). For \(q=3\) it derives \(\chi_3(E;s)/a_1(E)\to c_4(s)^2-c_3(s)c_5(s)>0\) at each fixed \(s\). E01 will assess these deductions separately from the inherited numerical inputs. [Originating calculation](../../10_radial_green_determinants/brainstorm/notes/03_SPECTRAL_FILTER_AND_TWO_ORBITAL_EXCHANGE_20261104.md)
- **Open.** The sign and size of \(D_3(1)-D_3(0)\), and the contributions from \(n=2\) and \(n\ge3\) along the common filter path. Growing-order and neighboring-shift estimates also remain open.

## Register

| ID | Status on 4 November | Dependency, model and scope of return |
| --- | --- | --- |
| MC11-B00 | **Complete — planning** | Astra selected the signed three-orbital comparison and the evidence required before acquisition. Outputs are plan revision 1 and this register. |
| MC11-E01 | **Complete — accepted without correction** | Sol/ultra assessed all requested claims with inherited integration premises; one proof pass and exact replay. [Assessment](../reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md) |
| MC11-E02 | **Complete — bounded return accepted by E04** | Sol/ultra: every \(n\ge3\) level raises the overlap throughout the path; \(L_2,\Delta_3\) remain inconclusive. One calculation and one regrouping, no new integration. [Note02](../notes/02_MC11_E02_R1_COMMON_PATH_SPECTRAL_SPLIT_20261104.md) |
| MC11-E03 | **Complete — validated return accepted by E04** | Sol/ultra: all five goals met in one 384-bit acquisition, no refinement. Both groups reinforce; first excited level supplies >99.99997573% of the gain. [Note03](../notes/03_MC11_E03_R1_FIRST_EXCITED_ACQUISITION_AND_RETURN_20261104.md) |
| MC11-E04 | **Complete — accepted within scope, no correction** | Sol/ultra same-assistant/same-model assessment; all 18 frozen hashes match, analytical pass and separate exact reconstruction pass. [Review02](../reviews/02_MC11_E04_R1_THREE_ORBITAL_RETURN_ASSESSMENT_20261104.md) |
| MC11-B01 | **Ready, unstarted — normal transfer decision** | Astra assesses transfer across orders or resolves the failed premise. Return one scoped decision and an E05 contract if warranted. [Contract](../research-overview/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md#mc11-b01) |
| MC11-E05 | Reserved, unspecified | Sol executes only after B01 defines the route, finite scope and evidence standard and the author selects it. |

## MC11-E01 request r1

This request follows MC11-B00, plan revision 1. The recommended model is Sol for this E task. Edward Baker chooses the model, effort and chat. The following inputs identify the versions used to prepare the request.

| Frozen input | SHA-256 |
| --- | --- |
| [Source-state pairing](../../08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md) | `96ffcc2943608870d5b8426fd217ce5ad515a05f06ff73f97c1d1295b71eec5a` |
| [Green and boundary comparison](../../10_radial_green_determinants/manuscript/sections/01_green.tex) | `0822d1d731da513ff62c6c7fa4ec8dfcd794c7212847dc2e39256efcfc015a60` |
| [Energy-response note](../../10_radial_green_determinants/brainstorm/notes/02_HILBERT_SPACE_AND_ENERGY_RESOLVED_CANCELLATION_20261104.md) | `7b1cfcf6bdc9edd3e09b8143e70491c795f8d1cf011a7acec104f8a416824a10` |
| [Spectral-filter derivation](../../10_radial_green_determinants/brainstorm/notes/03_SPECTRAL_FILTER_AND_TWO_ORBITAL_EXCHANGE_20261104.md) | `6a54482efcf3e586df878b097a450bb2584e75b5888a77c214105ec1f63ac928` |
| [Saved coefficient enclosures](../../10_radial_green_determinants/numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json) | `9ddc5881df258c3dbdfe611bf0c620c74cbd1292e0628d0e00dbca30a4e06e9a` |

Use the canonical energies \(\pi n^2\), filter \(W_s=P_1+s(I-P_1)\), and the real unnormalized diagonal overlap. Perform the checks specified in the [E01 plan](../research-overview/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md#mc11-e01) in one pass, with exact rational replay and at most one local correction. A changed input requires a recorded version decision before it is used. Save a review in this investigation's `reviews/` and append the return here. Include date, actual model and effort, input versions, accepted or failed claims, reproducible arithmetic, corrections, and the consequence for E02. Keep the original request and source evidence intact. If a physical or mathematical premise must change, refer that issue to B01.

For later returns, put analytical derivations in `notes/`, code and small execution records in `numerics/`, and assessments in `reviews/`. Record source, arithmetic, truncation and rounding assumptions where applicable. Keep one writer for this register; check the latest entry before appending. [Model workflow](../../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md) · [Review provenance](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md) · [Chat-history workflow](../../../../../../../tools/CHAT_HISTORY.md)

## Original E01 continuation prompt (historical)

> Read GPT_RESEARCH_MODEL_WORKFLOW.md, the energy-filtered theta overlaps plan and its live progress register. Complete [E] MC11-E01 r1 on Sol within its stated limits. Check the two-orbital loss and the three-orbital high-energy sign against the frozen inputs. Save the assessment and update the register with exactly which premises E02 may use.

## MC11-E01 activation · 4 November 2026

Author requested E01 r1 in thread `01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab`. Actual recorded model **gpt-6.1-sol**, effort **ultra**. One analytical proof pass with a read-only same-model contributor and exact rational replay of frozen inputs; no new quadrature. The coordinator owns this register and all saved returns. The chat is uniquely registered as MC11 chat0001. E02 remains unstarted pending the assessed premises.

## MC11-E01 r1 return · 4 November 2026

**Complete, accepted within scope; no local correction or changed input.** Actual **gpt-6.1-sol / ultra**, MC11 chat0001. All five frozen hashes matched. The originating Astra/xhigh derivation received a different-model internal assessment; a read-only Sol/ultra contributor supplied the single analytical proof pass, and the coordinator wrote the exact replay. Numerical acquisition premises remain shared; no specialist review is implied.

- **Accepted individually:** filter/source and unnormalized diagonal overlap; finite-order Hilbert membership; direct endpoint cancellation for the used indices; whole-path moment and excited-tail allowances through moment five; every excited level's negative two-orbital response at every filter setting; positive full-half-line ground reference and strict fractional loss below \(10^{-4}\); corner cofactor sign/indexing, high-energy limit and strict positive three-orbital limiting cofactor.
- **Exact evidence:** one standard-library rational replay, 87 checks passed, zero new integrals/moments, zero corrections. The two-orbital fractional loss is strictly below \(5480137/60543000000<40001/437500000<10^{-4}\). The scaled three-orbital corner lower factor is \(158282480099/1600000000000000>0\). These are conservative bounds, not measured effects.
- **E02 premises:** all accepted claims are available with the unchanged canonical spectrum, common filter path, full half-line, compact-vs-full reference distinction and inherited integration/tail enclosures. No E01 structural gap triggers B01. Filtered arbitrary-block pairings and normalized-wedge derivatives were not accepted.
- **Still open:** \(L_2,L_{\ge3},\Delta_3\), a finite-energy positive-response cutoff, a numerical positive \(D_3(0)\) lower bound, growing-order and neighboring-shift estimates. E02 has not begun; E03 remains conditional.

Evidence: [research note](../notes/01_MC11_E01_R1_PROOF_AND_RATIONAL_REPLAY_20261104.md), [assessment](../reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md), [checker](../numerics/mc11_e01_r1_exact_replay.py), [small exact record](../numerics/MC11_E01_R1_EXACT_REPLAY_20261104.json), [continuation and model-change packet](handoffs/01_MC11_E01_RETURN_AND_E02_MODEL_CONTINUATION_20261104.md). This chat is uniquely registered in [MC11 chat-histories](../chat-histories/index.json); original radial Green brainstorming retains its earlier registration.

## E02 continuation prompt (used for this return)

**Next: [E] MC11-E02 — Sol.** Read the E01 return and continuation packet, then execute the existing E02 r1 contract: collect and integrate the five cofactor weights along the same path, bound the \(n=2\) and \(n\ge3\) contributions and their sum from existing data, and pay the complete tail. Use one calculation and one regrouping, with no acquisition unless a subsequent E03 activation satisfies its documented gate. Return an inconclusive interval with its precise cause when that is the result. The packet includes a pasteable prompt and model-change provenance.

## MC11-E02 activation · 4 November 2026

Author activated E02 r1 in the existing MC11 chat0001, thread `01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab`, turn `01a1a8f3-323b-7ca1-aa36-acb844ed67ff`; actual **gpt-6.1-sol / ultra**. Source, common filter path, half-line and unnormalized observable remain fixed. Reuse E01 premises and frozen inputs; one exact/outward calculation and one regrouping, only the five order-three moments and spectral groups n=2 and n>=3, no quadrature. A read-only same-model contributor checks algebra and analytic tail inequalities; the coordinator owns computation, files and the sole register.

## MC11-E02 r1 return · 4 November 2026

**Complete as a bounded execution return; E04 assessment pending.** Actual **gpt-6.1-sol / ultra**, MC11 chat0001, turn 01a1a8f3-323b-7ca1-aa36-acb844ed67ff. All inherited frozen input hashes matched. The coordinator and read-only algebra/tail contributor are Sol/ultra; this is author checking with shared integration premises, not specialist review.

The [research note](../notes/02_MC11_E02_R1_COMMON_PATH_SPECTRAL_SPLIT_20261104.md), [code](../numerics/mc11_e02_r1_spectral_split.py) and [174,547-byte exact record](../numerics/MC11_E02_R1_SPECTRAL_SPLIT_20261104.json) retain the calculation. One exact/outward calculation and one slope-ratio regrouping were used; 36 checks passed, zero quadrature evaluations and no new moments. The common \(b,h\) cofactor polynomials integrate exactly, and \(\sum_jh_jK_j=D_3(b+h)-D_3(b)\) passes formal expansion.

| Returned quantity | Conservative rigorous bound | Disposition |
| --- | --- | --- |
| \(L_2\) | \([-1.087\times10^{-32},1.335\times10^{-32}]\) | Sign unresolved |
| \(L_{\ge3}\) | \(0<L_{\ge3}<5.402\times10^{-40}\) | Strictly positive |
| \(\Delta_3\) | \([-1.087\times10^{-32},1.335\times10^{-32}]\) | Sign unresolved |
| \(D_3(0)\) | \(1.66142398817\times10^{-28}<D_3(0)<1.66142398818\times10^{-28}\) | Strictly positive full-half-line reference |
| \(\Delta_3/D_3(0)\) | \([-6.540\times10^{-5},8.033\times10^{-5}]\) | Signed interval containing zero |

Whole-path gradient bounds also prove \(\chi_3(\pi n^2;s)>0\) for every \(n\ge3\), all \(s\in[0,1]\). This is stronger than the inherited fixed-\(s\) high-energy limit. Both groups use the unchanged common path. Reinforcement/opposition remains undetermined because the \(n=2\) sign is unknown. The complete infinite \(n\ge3\) group, ground spatial exterior and imported compact uncertainty are paid.

**E03 gate met, acquisition not started.** The uncertainty is localized to the five \(a_j(4\pi)\) inputs. Useful absolute half-width targets, in order \(j=1,\ldots,5\), are \(8.8483\times10^{-15},3.6456\times10^{-18},1.5020\times10^{-21},6.1887\times10^{-25},2.5498\times10^{-28}\). Their response-radius payment is \(<2.4980\times10^{-38}\), versus current cofactor payment \(<5.7997\times10^{-38}\). A midpoint weighted response of magnitude \(>8.352\times10^{-38}\) would decide the net sign with these targets and the full tail. The note/record demonstrate feasibility with retained-bound-set examples; they are not actual or asserted realizable source moments and forecast no actual sign.

No structural change triggers B01. No new canonical positivity range, growing-order or neighboring-shift comparison follows. The inconclusive interval is a limit of the specified moment bounds, not a zero response or a general obstruction.

## E03 continuation prompt (used for this return)

**Next: [E] MC11-E03 — Sol.** Follow the [E02/E03 continuation and model-change packet](handoffs/02_MC11_E02_RETURN_AND_E03_MODEL_CONTINUATION_20261104.md): acquire only the five first-excited source moments, at 384 bits with one acquisition and at most one subdivision refinement, include the \(n=2\) spatial tail, retain the separate complete \(n\ge3\) bound, and replay the same common-path cofactor calculation. Return all intervals for E04, even if inconclusive. E04 may alternatively assess E02 alone if the author defers acquisition. B01 interprets the assessed result or handles a named structural premise change.

## MC11-E03 activation · 4 November 2026

Author activated E03 r1 in MC11 chat0001, thread `01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab`, turn `01a1a988-130d-7d12-a635-ee7f7a94ed96`; actual **gpt-6.1-sol / ultra**. All E02 consumed input/code hashes match. Enclose only the five n=2 source moments on [0,2] plus a rigorous full spatial exterior, using 384-bit Arb/FLINT, the inherited five-segment cover and tolerance 2^-320. One acquisition, at most one midpoint subdivision refinement at the same precision; routine resource caps 180 seconds and 200000 callbacks. Preserve every attempt and stop at the stated cap. Replay the unchanged common-path cofactor polynomials with h=A+H and the existing complete n>=3 tail. A read-only same-model contributor checks the source-tail derivation/callback adaptation; coordinator owns the acquisition, files and sole register. No E04 disposition or B01 interpretation is performed in this task.

## MC11-E03 r1 return · 4 November 2026

**Complete — all goals met on the first acquisition; E04 assessment pending.** Actual **gpt-6.1-sol / ultra**, MC11 chat0001, turn 01a1a988-130d-7d12-a635-ee7f7a94ed96. Source, common path, half-line and unnormalized overlap unchanged. All consumed E02/inherited input and code hashes matched.

The [research note](../notes/03_MC11_E03_R1_FIRST_EXCITED_ACQUISITION_AND_RETURN_20261104.md), [acquisition/code verifier](../numerics/mc11_e03_r1_first_excited_acquisition.py), and [113,111-byte record](../numerics/MC11_E03_R1_FIRST_EXCITED_ACQUISITION_20261104.json) retain the finished calculation. Actual environment: Python 3.12.14, python-flint 0.9.0, FLINT 3.6.0, 384 bits. The 25 compact source integrals used 1,991 callbacks and 0.022567542 seconds. Every width target was met; no subdivision refinement or precision change occurred. A new \(n=2\) source spatial-tail proof/ball and upward payment cover the exterior beyond 2; E02's complete \(n\ge3\) majorant is retained separately.

The five full source moment half-widths are below \(6.346\times10^{-105},5.557\times10^{-106},3.044\times10^{-97},3.849\times10^{-99},3.029\times10^{-101}\), respectively. A standard-library saved-data verifier reproduced all 121 checks and the exact propagation, with no integration rerun. It trusts the identified Arb integration and constant evaluations.

| Returned quantity | Conservative rigorous bound | Disposition |
| --- | --- | --- |
| \(L_2\) | \(2.22665020868\times10^{-33}<L_2<2.22665020869\times10^{-33}\) | Strictly positive |
| \(L_{\ge3}\) | \(0<L_{\ge3}<5.402\times10^{-40}\) | Strictly positive |
| \(\Delta_3\) | \(2.22665020\times10^{-33}<\Delta_3<2.22665075\times10^{-33}\) | Strictly positive |
| \(D_3(0)\) | \(1.66142398817\times10^{-28}<D_3(0)<1.66142398818\times10^{-28}\) | Strict positive reference, unchanged |
| \(\Delta_3/D_3(0)\) | \(1.34020588635\times10^{-5}<\Delta_3/D_3(0)<1.34020621148\times10^{-5}\) | Fractional increase |

Both groups reinforce. The full higher group contributes less than \(2.427\times10^{-7}\) of the gain, so the first excited level accounts for more than 99.99997573%. The final net interval width is governed by the higher-group allowance, not the new quadrature widths.

A whole-path source/cofactor bound also gives \(2.2266193\times10^{-33}<\chi_3(4\pi;s)<2.2266811\times10^{-33}\), all \(0\le s\le1\). Combined with E02's \(n\ge3\) result, every excited box level raises this three-orbital overlap throughout the path. This is proved by a pointwise interval, not inferred from an integrated sign.

The coordinator implemented/acquired and replayed the enclosures. A read-only Sol/ultra contributor checked the entire callback, source-tail normalization and proof; these are same-model author checks with shared premises. E04 is not yet performed. No new positivity range, growing-order, neighboring-shift or RH conclusion is made. No source/manuscript/snapshot was changed.

## E04 continuation prompt (used for this return)

**Next: [E] MC11-E04 — Sol.** Follow the [E03/E04 continuation and model-change packet](handoffs/03_MC11_E03_RETURN_AND_E04_MODEL_CONTINUATION_20261104.md) and [frozen input versions](handoffs/03_MC11_E04_R1_INPUT_VERSIONS_20261104.json). Assess the finished E02/E03 calculation in one pass, at most one local correction, no new quadrature or scan. Reconstruct source normalization, finite integration and source spatial tail, the unchanged higher-level allowance, common-path integrated cofactors/cubic identity and exchange-sign mutation, all signs/magnitudes and whole-path claims. Save the claim-by-claim assessment. B01 follows the assessed return or resolves a named substantive premise failure; it is not begun here.

## MC11-E04 activation · 4 November 2026

Author activated E04 r1 in MC11 chat0001, thread `01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab`, turn `01a1a9d5-044d-7ee1-a1e3-7a415581b884`; actual **gpt-6.1-sol / ultra**. All 18 frozen E04 inputs matched. One analytical assessment pass with a read-only same-model contributor and a separately written exact saved-data reconstruction; at most one local correction. No new quadrature, precision change, spectral/order scan or B01 work. The coordinator owns review, evidence and this sole register. Assessment remains same-assistant/same-model with shared Arb/source premises; no specialist independence is implied.

## MC11-E04 r1 return · 4 November 2026

**Complete — all specified claims accepted within scope, no correction.** Actual **gpt-6.1-sol / ultra**, MC11 chat0001, turn 01a1a9d5-044d-7ee1-a1e3-7a415581b884. All 18 frozen input hashes matched; the acquisition and earlier source/failed-inconclusive evidence remain unchanged.

[Review02](../reviews/02_MC11_E04_R1_THREE_ORBITAL_RETURN_ASSESSMENT_20261104.md) gives the claim-by-claim disposition. [Note04](../notes/04_MC11_E04_R1_RECONSTRUCTION_AND_ERROR_ACCOUNTING_20261104.md), the [separate checker](../numerics/mc11_e04_r1_assessment_replay.py) and [58,097-byte exact record](../numerics/MC11_E04_R1_ASSESSMENT_REPLAY_20261104.json) retain the evidence. The existing verifier reproduced 121 checks; the new cofactor/product reconstruction passed 124, with no imported execution-script math helpers and no new quadrature. One analytical pass with a read-only same-model contributor found no gap. An elementary source-tail estimate independently verifies the \(2^{-384}\) retained spatial payment.

Accepted separately: source normalization/entire integrand, 25-segment acquisition/widths and resource accounting, actual-tail interval orientation, ground spatial exterior, complete \(n\ge3\) energy allowance, five collected gradients and integrated mixed terms, common-path cubic identity, true determinant exchange-sign mutation, group signs/magnitudes, strict reference floor, fractional effect, first-level dominance and whole-path pointwise signs. The original E02 zero-straddling result remains accepted as a limit of its older inputs.

The accepted numerical return is \(2.22665020\times10^{-33}<\Delta_3<2.22665075\times10^{-33}\), with fractional increase between \(1.34020588635\times10^{-5}\) and \(1.34020621148\times10^{-5}\). Both groups reinforce, and \(L_2/\Delta_3>0.9999997573\). Every excited level raises the three-orbital unnormalized overlap for all \(0\le s\le1\). The full source/spatial allowances remain paid.

This is **same-assistant/same-model internal assessment**, with identified shared Arb/source premises, not independent specialist review. No new positivity range, RH conclusion, growing-order or neighboring-shift estimate is accepted. No substantive discrepancy requires an early B01 premise revision; the normal B01 transfer decision is now ready.

## Current continuation prompt

**Next: [B] MC11-B01 — Astra.** Follow the [E04/B01 continuation and model-change packet](handoffs/04_MC11_E04_RETURN_AND_B01_MODEL_CONTINUATION_20261104.md) and the unchanged B01 plan. The assessed groups reinforce: decide which bounds on the leading and remaining cofactors could persist beyond order three. Compare at most two analytical routes on paper, consuming existing results and collision controls; account for neighboring shifts in a Mellin-curvature use. Name the cofactor sum and dimension-dependent margin for a growing-order claim. Return one precise E05 contract for Sol, with source, observation, finite limits and acceptance test, or a scoped reason to stop. B01 is unstarted; E05 stays reserved. Edward Baker selects the actual model, effort and chat.
