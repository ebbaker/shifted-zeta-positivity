# Assessment of the first flux and joint-moment comparison

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**. Investigation05 chat0005, **Begin radial collision research**. Same-model internal assessment, including separate subagent derivations; no independent specialist review.

**Finding.** [Note16][note] completes the first bounded RLC-01/RLC-02 contract at a modest scope. It supplies uniform canonical flux, shell and observation-tail estimates, a proved necessary moment restriction at any simultaneous zero, an explicit conservative bounded exclusion, and an exact comparison with the direct formulation. It establishes no radial estimation advantage or enlargement of a previously covered theta region. The wider collision program remains open.

## Mathematical checks

| Item | Check and conclusion |
| --- | --- |
| Complete source | The omitted n>=m terms are positive on r>=1. The geometric majorant uses all omitted squares with unchanged unit coefficients; it is not an unbounded finite-prefix substitution. |
| Arbitrary finite time slab | Absorption uses log^2 r<=4r/e^2 and completion of a square, with 0<eta<pi m^2. No small-T restriction enters. |
| Evolved flux | Both terms of the exact time-corrected formula are present. Its integral correction contributes T(beta R^2+1)/(4e beta^2) to the envelope. |
| Shell correlation | Remainders are differences of one shared decreasing tail flux; monotonicity of the time weight gives both shell bounds. Cuts are fixed. |
| Joint tail | Cauchy-Schwarz is applied to the joint projection before absolute component bounds. The physical factor is one eighth. Weighted tails for the derivative transfer are finite explicit Gaussian moments. |
| Boundary | The residual at r=1 is cE(1). A tail starting at R has phi(R)E(R). No extra interior observation or central-charge substitution occurs. |
| Coupled restriction | G''(theta)=theta(theta-sin theta)/2>0 proves the global kernel inequality. At an event a^4 P4>24P0. The coefficient 1/24 is sharp only for the stated projection. |
| Time uniformity | (P4/P0)'=(P6P0-P4P2)/P0^2>0 by the positive double integral. The endpoint moment ratio controls every t in [0,T]. |
| Explicit range | The one-square lower bound L0 and full-source upper bound U4(T) have the correct powers and factors. Their positivity proves a specified bounded exclusion with no unevaluated sign premise. No numerical height or competitive gain is claimed. |
| Direct comparator | dnu=8e^u m_t du cancels the e^-u kernel factor exactly. Source information, moments, boundaries, and tails agree in both coordinates. |
| Separate flux allowance | Integrating absolute phi proves F-D=2 integral over {phi phi'<0} E abs(phi'). For nonzero directions and omitted canonical modes this is strictly positive at a>0. This concerns nonnegative remainders and separately majorized boundary/integral terms. |
| Control | The Gaussian-polynomial event has a^4 P4/P0=123, so it passes the necessary condition. Its log-Gaussian radial tail fails the canonical envelope; other controls need the individual premise distinctions listed in the note. |

The primary derivation and separate same-model subagent derivations agree on these calculations. No numerical experiment or interval certificate was needed. Existing control certificates were used at their recorded scopes and were not rerun. The elementary arguments import no new external theorem or bibliographic priority claim.

## What this does and does not decide

The source-balance restriction is a generic positive-source estimate instantiated with canonical bounds. It is stronger as a *statement about simultaneous cancellation* than merely specifying an enclosure, but it does not establish that its height radius improves a direct zero-free estimate. The exact comparison with the second-moment positivity radius is

\[
A_4/A_2=\{6P_2^2/(P_0P_4)\}^{1/4}.
\]

Whether this exceeds one for the unchanged theta source on a specified time interval remains unproved here. No sample or uncomputed inequality is counted as an improvement.

The comparison closes only two proposed gains: improvement from changing coordinates while retaining identical source information, and improvement from separately bounding the boundary and flux integral for a nonnegative omitted source. It does not exclude coupled signed flux methods, more useful source correlations, an acquisition-cost advantage that is actually demonstrated, or event-conditioned theta identities.

The exclusion applies to all finite multiplicities at least two only in its displayed bounded range. It does not furnish the high-frequency or time-uniform exterior estimates needed for a Newman-threshold argument, or simplicity at all t=0 heights. RLC-06 therefore remains inactive for global transfer. RLC-03 was not needed and RLC-05 has no new characteristic candidate.

## Recorded decision and next step

Save this as the first bounded RLC return; leave the broad RLC-01/02 goals open. Stop optimizing the two compared implementations as routes to an intrinsic radial margin. A focused continuation may prove the actual canonical moment comparison P0P4<6P2^2, or its failure, on a declared time slab before evaluating constants. Any resulting gain would belong to the coupled projection and must be compared with known direct bounds. RLC-04 remains the structural alternative for a theta-specific event-conditioned estimate.

The [progress register][progress] records the return and uncovered obligations. The [result index][results] and [avoid index][avoid], especially [controls][controls], [coordinate realizations][a03], [scoped failures][a07], and [coupled bounds][a12], govern its interpretation. This is an incremental research return, not investigation closeout or a manuscript milestone; no new snapshot, DRAFT_HISTORY milestone, or repository-wide result-summary claim is made.

Chat0005 is registered in this investigation through the authorized history tool. Current counts, hashes and capture times belong to the [registry][history]. The real final reply must still be captured by the bounded exact-turn worker after it is sent; archive integrity is not mathematical validation.

[note]: ../notes/16_CANONICAL_FLUX_MOMENT_RESTRICTION_AND_DIRECT_COMPARISON_20261027.md
[progress]: ../research-progress/02_RADIAL_LAPLACIAN_COLLISION_RESEARCH_PROGRESS_20261027.md
[history]: ../chat-histories/index.json
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
