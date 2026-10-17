# Manuscript integration review

> **17 October 2026 — history routing update.** Historical formal-replay routing below is superseded. Chats [17](../chat-histories/0017_2026-10-15T10-16-48Z_continue-quaternion-theta-geometry.json), [18](../chat-histories/0018_2026-10-15T11-51-01Z_continue-theta-manifold-research.json) now use this investigation's [local registry](../chat-histories/index.json), as recorded in the [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json). Original identities, provenance and public messages are preserved. All future Investigation 22 chats belong in this local history folder.

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This is an internal mathematical and document review, not external refereeing or formal verification.

The revised [manuscript](../manuscript/theta_manifold_geometry.tex) prioritizes the fixed-endpoint chord theorem, cutoff transfer, complete source identities, and arithmetic discrimination. Its [31-page reading copy](../../../../../output/pdf/theta_manifold_geometry.pdf) replaces the initial export. The [build record](../manuscript/BUILD_RECORD.json) binds the current source and PDF and retains the initial build identity. No manuscript snapshot, commit, or tag was created in this integration.

## Principal checks

| Result | Integration and review finding |
| --- | --- |
| Fixed-endpoint chord law | The analytic heat polynomial is positive throughout a fixed two-variable neighborhood; its leading term dominates the uniform remainder. This proves whole-interval zero-freeness, not merely endpoint signs. The fixed positive endpoint produces a strictly negative limit after division by the square root of starting physical energy. |
| Exclusion and sharpness | Both parity branches use `E(t,x)` at the full stationary start. The interval length and error rule are uniform through the event. The exact quadratic control permits a √E loss, and also a bounded loss paid by endpoint energy, so neither replacement proves exclusion. |
| All-cutoff transfer | Every sufficiently large integer cutoff is required, with locally uniform threshold and coefficients. Sub-Gaussian cost is sufficient. Gaussian cost is sufficient for the chord under a strict uniform rate gap; the `exp(O(sqrt(log(1/E))))` rounding factor is retained. Equality of rates admits the collision control. |
| Inner and parabolic profiles | Compact inner limits and the quarter-turn law are kept distinct. No unproved global weak limit is asserted. The odd-branch jet/physical energy factor away from the center remains visible. |
| Source geometry and signed reconstruction | The base-only ASD classification and path-normalized representative correct the original cusp-growth interpretation. Flat path restriction is distinguished from transverse commutators. Bilocal kernels, common normalization, primitive lower-edge and corner terms, and the complete heat multiplier all remain explicit. |
| Arithmetic control | The first source endpoint and positive square-support localizers coexist with a validated non-theta double collision. Quoted intervals match the saved certificate. The extension to all-positive weights is qualitative, without an invented perturbation radius. The source is not even in u. |
| Reflection rigidity | Evenness, polynomial growth, Schwartz-topology differentiation, all Gaussian moments, Fourier injectivity and local Gaussian division justify the distribution argument. The endpoint-normalized source-reflection corollary fixes coefficients; no physical sign follows from uniqueness alone. |
| Exploratory limitations | Period-two sectors are summarized only with their precise separate-budget obstruction. Exponential spectral cost does not refute a coefficient merely locally bounded at each finite event. Fiber-norm, compact-completion and Pick-type proposals remain in Overview 02 and the linked strategy note. |

The turning and source fragments received an independent analytic audit from the arithmetic collaborator; the arithmetic fragment received an independent audit from the connection collaborator. The coordinator read the complete fragments, checked their consistency with the existing manuscript, and rewrote the abstract, introduction, research program and verification appendix around the final results. No mathematical correction was required by these cross-checks.

## Computation and provenance

The eleven existing checkers cover **6,897 overlapping exact assertions** and **123 validated or mixed assertions**. These are scope counts, not theorem counts. General analytic claims retain their written proofs. During this integration, 34 digest comparisons across 30 distinct research files confirmed that the prior checkers, relevant notes and saved receipts remain unchanged. The arithmetic collaborator also independently replayed the 160-bit weighted-square certificate: all 50 assertions passed and all mathematical output fields matched the saved receipt. No new theta sign certificate is claimed.

The [connection/profile manifest](../numerics/CONNECTION_BRIDGE_AND_INNER_TURNING_CHECKS_20261015.json) and [arithmetic/contour/chord manifest](../numerics/ARITHMETIC_CONTOUR_CHORD_CHECKS_20261015.json) remain historical records. Statements there that the manuscript was then unchanged describe those earlier checkpoints. They were not rewritten to conceal the present revision. The current build record is the source of truth for the reading copy.

## Document and handoff checks

The manuscript compiles in the desktop compiler and with the terminal export compiler. The final export has no warnings, undefined references, or overfull/underfull boxes. Its 151 labels are unique; every reference and all citations resolve, with 17 bibliography entries. All 31 pages were individually visually inspected at 100 dpi. The coordinator additionally inspected the opening, main chord theorem and complete-source kernel pages. No clipping, overlap, missing glyphs, unresolved reference markers or defective theorem displays remained.

Links to research records in the exported PDF are relative to `output/pdf` and were checked against the installed repository destinations. The original overview is now [Overview 01](../research-overview/01_RESEARCH_OVERVIEW_20261015.md); its former filename is a compatibility pointer. [Overview 02](../research-overview/02_CHORD_CRITERION_AND_ARITHMETIC_BRIDGE_20261015.md) gives the current priorities, exploratory assessments and next-chat starting point. Existing linked research notes and archived public messages were not rewritten during numbering.

The [chat-history checkpoint](../numerics/CHAT_HISTORY_VERIFICATION_20261015.json) separately verifies the canonical registration and captured public-text prefix. This conversation retains formal-replay identity 18 under the standing local instruction; the earlier investigation-creation chat retains identity 17 in this investigation. Final reply capture follows the exact-turn workflow after the reply is actually sent.

The central unresolved statement is still a complete-theta chord estimate with error `o(sqrt(E(start)))`, or another sufficient estimate, together with the required event and spectral coverage. The manuscript presents a sharper route to that statement, not a proof that theta satisfies it.
