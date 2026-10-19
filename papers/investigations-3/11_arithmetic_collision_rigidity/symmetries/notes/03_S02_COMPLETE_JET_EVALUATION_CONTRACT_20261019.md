# S02-T2 complete jet evaluation contract

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6.1-sol (Codex), actual reasoning effort ultra**, verified from session metadata. Internal LLM work and delegated audit; no specialist review.

## Domain, objects and metric

Execute S02-T2 on B=[1/100,1/5] x [999,1001] only. C is a separate unactivated stage. Keep N=8, R=1/2 and the S02-T1 uniform Q-disk allowances, validated against current source pins. Evaluate the selected disk-wise frozen correction and the full analytic correction through order two on every cell of the existing S03 32-time by 128-space closed rational cover (4096 cells). Do not refine this cover after seeing the result. A diagnostic on the inherited 40 source-consumer cells may document coarse geometry limitations, without becoming a coverage or cost comparison.

Primary evaluation: complete paid phase-scaled first-jet radius and residual allowance in the SAME coordinates J=(Q,-Qx/omega), with signed omega. Compare both formulas on the same cells using the same exact source information. Use the strongest existing analytic-only direct bound >0.967290 as a reference, and separately the source-informed direct bound >1.336516 with its additional complete-source data. Freshly build one complete-source midpoint setup per retained precision and evaluate it on the same 4096 cells as an additional source-informed comparison. Include every acquisition and error component. No timing or factor-two performance objective is selected.

Secondary tests: closed-cell joint Schur first-jet exclusion, physical Laguerre L0 and the existing L0-E/100 margin. Pay the exact physical normalizer return, and report independent-error-box and justified joint-disk payments separately. A failure means this particular allowance/test is inconclusive, not that theta violates the sign. A passing old B is regression validation. Continue only for a complete paid-error, matched-cost or coverage advantage over the strongest applicable reference; otherwise retain a documented limited-use interface and stop. No extension is activated by evaluating this box.

## Frozen center and whole-cell propagation

Hold the correction center X fixed during local z differentiation, even when X is an interval ranging over a cell. Reuse the stable finite P/Px/Pxx sum and theta phase representation. Recenter phase using its true omega derivative where useful. Record true range width plus outward evaluation rounding separately from the uniform analytic residual allowance; do not describe a whole-cell image radius as rounding error alone.

Let q=B_t exp(-kX)/A(X), u=q J8'(X), h=k+b, k=pi/8 and b=(log A)_x. The selected local jet family f satisfies d_X f0=f1-u and d_X f1=f2+h u. Therefore W=f0-i f1/omega obeys d_X W=i omega(W-Rloc)-u(1+i h/omega), with Rloc=f0+f2/omega^2-omega_x f1/omega^3. Use this complete derivative if applying midpoint propagation. The uncorrected S03 propagation identity is valid for the coherent full formula, not for the changing-center frozen jet family. The diagonal jet-family derivative defects must be exported.

For physical return use (H,Hx,Hxx)/A=(Q,Qx+bQ,Qxx+2bQx+(b^2+b_x)Q). The exact normalized Laguerre form is Qx^2-Q Qxx-b_x Q^2. Joint disk bounds may use Hardy coefficient constraints and real Schur coefficients, but their complete linear and quadratic payments must be proved in the note and tested on exact polynomial controls. The basic box tests remain visible as an independent conservative comparison.

## Export, replay and storage

Export a source-pinned reusable closed-cell evaluator and documented semantics for direct and S03 consumers. S03's shared analytic residual receives the FULL coherent formula and eta_an; frozen data are for local disk tests and require their derivative defects. Do not propagate normalized residuals or a center-varying family by the heat equation.

Retain 192/256-bit summary records, separate internal replay/review and source-specific event controls through the new acceptance functions. Full per-cell jet tables are regenerable derived data: store them externally, record stored and canonical-content hashes, provide a hash-checking loader with the repository's normal-path then S02_JET_ARCHIVES fallback, and document regeneration in ARCHIVES.md. Keep code, small 32-slab ledgers, archive guide and identity records below 1 MiB. Preserve this conversation's unique existing registration.

Follow the [result summaries](../../../../../result-summaries/README.md), [avoid index](../../../../../avoid/README.md), [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md), [preserving cancellation](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [normalization](../../../../../avoid/08_normalization_and_constant_slips.md), [scope](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [target-reformulation rule](../../../../../avoid/01_restating_the_target.md). This is a bounded quantitative evaluation, not a global criterion.
