---
research_program: COORD
secondary_programs: [PR02-CORR, PR01, PR02, PR03]
status: continuation
---

# Localized Poisson, explicit remainder constants, and the next signed estimate

> **Chat-history routing update, 17 October 2026.** Current histories: [Chat 18 — Continue Poisson obstruction study](../../chat-histories/0018_2026-10-15T05-32-27Z_continue-poisson-obstruction-study.json), [Chat 17 — Continue octonionic correlation work](../../chat-histories/0017_2026-10-15T05-14-09Z_continue-octonionic-correlation-work.json), [Chat 16 — Review octonionic simplifications](../../chat-histories/0016_2026-10-15T04-25-26Z_review-octonionic-simplifications.json). Use this investigation’s [local registry](../../chat-histories/index.json) and [relocation receipt](../../CHAT_HISTORY_RELOCATION_20261017.json) for current numbers and preserved provenance; this supersedes the routing and numbering below. All future investigation 21 chats belong in this investigation’s `chat-histories/` folder.

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6.1-sol**, reasoning effort **ultra**, verified from the current conversation’s session metadata. This is an incremental research continuation with independent internal checking, not external peer review or formal verification.

This continues [Note 41](41_POISSON_OBSTRUCTION_AND_REMAINDER_CONTINUATION_20261015.md). The finite signs through height 112, eventual strict signs for theta at least (61/24), and the explicit outer theta-five bound are unchanged. The missing theta-specific signed-energy estimate remains open.

## Results to carry forward

- [Note 42](../05_theta_correlation_kernels/42_LOCALIZED_POISSON_MODE_OBSTRUCTIONS_20261015.md), PR02-CORR, gives a smooth integrable Poisson localization with all differential and heat factors intact. A global absolute lattice bound proves uniform joint-escape control for each positive window parameter. The exterior is a complete-source (O(\varepsilon)) moment allowance, without a signed energy payment.
- The same note proves that every individual parity–Poisson mode and every finite centered rectangular packet retains a nonzero (e^{-10r}) differentiated tail. Each is globally nonintegrable under positive heat. Fixed-order modular Taylor compensation after the zero-mode addback also leaves a nonzero diagonal exponential tail. Cancellation or exact resummation must precede unbounded mode integration.
- Its expanding-box absolute axis cost is at least a constant times ((\log N)^{2j+1}\exp\{(t/2)(\log N)^2-5\log N\}) when the box is chosen for a Gaussian complete exterior. This rules out separate absolute sector budgets within the previously adopted polynomial-cutoff transfer class; it does not rule out a combined signed mechanism.
- [Note 43](../01_weighted_outer_remainders/43_EXPLICIT_WEIGHTED_REMAINDER_CONSTANT_PACKAGE_20261015.md), PR01/PR03, evaluates elementary disc thresholds, the low-index coefficient, dyadic scaling, and all imported Riemann–Siegel errors. On (L\ge100002) discs the sum error is bounded by (36138917/(16\ell)+16e^{-\ell/40}+2G_0 C_{\rm EP}e^{-\lambda\ell}), with (G_0=962773/671) and (lambda=2324691/31840000000>1/14000). The actual exponent-pair constant and the separate carrier-to-phase derivative budget remain unresolved; there is no evaluated full sign height.
- [Note 44](../02_signed_cusp_control/44_SUBPOWER_CUTOFF_TRANSFER_AND_ANALYTIC_RIGIDITY_20261015.md), PR02, proves a conditional extension: a signed all-cutoff estimate with an (E N^p\exp\{a(\log N)^2\}) cost and a Gaussian remainder still excludes every finite analytic collision multiplicity on a domain covering its predecessors. Its transferred subpower gauge is qualitatively rigid on analytic stationary germs. No theta arithmetic estimate satisfying that premise has been established.

[Review 28](../../reviews/28_LOCALIZED_POISSON_AND_EFFECTIVE_BUDGET_REVIEW_20261015.md) records independent analytic audits and deterministic replay of **260 mode/cutoff assertions** and **50 weighted-budget assertions**. These are finite exact arithmetic checks, not formal proofs or new stationary observations. The [validation receipt](../../numerics/LOCALIZED_POISSON_CONTINUATION_VALIDATION_20261015.json) records final file and replay identities.

## Next admissible arithmetic task

Freeze one **combined signed** Poisson or source-amplitude mechanism on a declared domain. The smooth identity resolves the existence of an integrable localization; repeating localization or proving only another absolute tail allowance will not supply the signed estimate.

1. Specify the exact grouping and its coefficient rules before computation. Preserve independent coordinates, full source differential factors, every heat multiplier, and joint escape. A finite global lattice rectangle or fixed-order subtraction in the rejected classes cannot be used as an integrable source.
2. Prove a stronger signed lower bound on both full stationary sets, paid by (E) with source-prescribed coefficients locally bounded through covered positive-time collisions. Either the original polynomial-cutoff/Gaussian-tail transfer or Note 44’s larger cost is sufficient if its **whole family**, full error budget, and (E) factor are proved first. Neither raw absolute sector norm currently supplies that premise.
3. The small-energy restriction (E\le\delta\Gamma^2) remains available on a domain covering all required predecessor neighborhoods. The nonzero Stirling carrier provides a scale, not a physical energy floor. Full-source bounds handle the complementary domain.
4. Only after that signed mechanism is frozen should a fresh certified pilot be run. Preserve full stationarity, both branches, derivative errors, and the original hybrid staircase whenever it is invoked. Note 40 remains a reusable baseline, not validation of a new Poisson mechanism.

For PR01/PR03, extract numerical maximal-interval constants for the five actual exponent pairs at loss (10^{-5}), with thresholds, A-process losses, and completion costs. Note 43 now isolates precisely this missing arithmetic package. Alternatively pursue the direct weighted middle-interval saving; changing an elementary constant cannot remove the recorded positive exponent at theta five halves. Do not interpret the conservative disc threshold alone as an effective sign height or a feasible finite bridge.

## Repository and chat provenance

Incremental proofs are saved in their program notes, reproducible calculations and small receipts in `numerics/`, and the internal assessment in `reviews/`. The manuscript, PDF, and build record remain authoritative for their unchanged version. No new manuscript snapshot folder, commit, or tag was created. The concise milestone is indexed in `DRAFT_HISTORY.md`.

This conversation is **history 15**, **Continue Poisson obstruction study**, thread `01a13e0c-2b80-7b31-ade4-993b86d44259`, in the explicitly authorized formal replay lane. It is distinct from Note 41’s history 14 and the earlier history 13. The [live formal-replay registry](../../chat-histories/index.json) supplies current messages, provenance, hashes, and capture times. No prior history was relocated, renumbered, or overwritten. The direct refresh and bounded exact-turn final capture remain in use because native hook activation has not been verified.
