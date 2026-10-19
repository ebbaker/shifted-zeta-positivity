# S03-T3 calibrated consumer internal review

19 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Separate delegated reviewer: gpt-6.1-sol (Codex), actual reasoning effort ultra as recorded by the root session. Same-model internal proof/code review and independently launched replay; no independent specialist review.

**Disposition: pass for the bounded comparison and stopping decision.** The real pilot remains B=[1/100,1/5] x [999,1001], anchor 999, unchanged 32x128 closed cover, full coherent analytic cutoff 8 approximation. The strongest complete-source direct certificate is stronger than the calibrated pointwise first-jet certificate. Scalar calibrated transport is weaker still. The analytic-only scalar allowance is inconclusive on this cover. This is an existing-box comparison, without a new residual theorem, new coverage, all-height input or matched-cost advantage.

The reviewer read the repository AGENTS.md, LARGE_FILES.md, result-summaries/README.md, avoid/README.md, the S03-T3 fixed comparison contract, inherited Note 02 and the current producer. The relevant controls/scope/normalization/cancellation cautions remain applicable. The calculation is a quantitative finite comparison, not an RH-equivalent criterion.

## Proof and code checks

Let W_h=h-i h_x/omega and Z_h=exp(-i theta)W_h. With nominal physical anchor polynomials p0,p1, the code uses a0=chi*p0 and a1=chi*(p1-b*p0), evaluated at999. Its oscillator has W_g=exp(i(theta-theta_a))*(a0-i*a1/omega_a), so R_g=0 and W_g'=i*omega*W_g with the prescribed negative omega. The current full f, including every correction-profile derivative, is retained. The calibrated first-jet error is exactly the inherited anchor uncertainty plus the inherited complete residual increment allowance, each charged once. Evaluating the nominal coefficients on a time interval creates interval image width; that width is not confused with the source-to-nominal anchor uncertainty.

The general derivative W_h'=h_x-i*h_xx/omega+i*h_x*omega_x/omega^2 is implemented with the correct sign and normalization. On a closed spatial cell of halfwidth h, the lower bound |W(midpoint)|-h*sup|W'| is valid for every fixed t in the closed time slab. The implementation gives the analytic, calibrated and complete-source routes both that directly differentiated vector bound and the established generic |omega|*(|W|+|R|) bound, retaining whichever is sharper along with the raw cell rectangle bound. Specialized complex-rectangle norm bounds are used consistently. This common enclosure improvement is not an arithmetic cancellation gain.

For the complete-source direct route, source.enclose() returns complete physical order0,1,2 jet balls. The normalization Q0=chi*V0, Q1=chi*(V1-b*V0), Q2=chi*(V2-2*b*V1+(b^2-b_x)*V0) is correct. Those complete balls justify the derivative propagation and already pay quadrature, Taylor, omitted-mode and source tails. The separately printed source-error diagnostic is not subtracted again. The derivative of the exact calibrated approximation is known from its definition; using it does not assert a second-jet residual bound.

The scalar consumer pays the analytic-only anchor error plus the T2 analytic-only increment for its own information class. Its source-informed alternatives instead pay the inherited source anchor or nominal-anchor error plus the same retained correlated residual increment. The signed primitive Z_f-2 cancels the n=1 constant exactly and preserves the full correction before taking interval norms. No zero residual anchor is assumed.

At exact nominal vectors, triangle inequality proves |D_a|-|Delta_f|<=|D_a+Delta_f|, so scalar transport cannot beat the corresponding exact calibrated pointwise disk consumer with the same nominal anchor ball and residual disk. This is scoped to those envelopes. It does not prove numerical interval implementations must order the same way, nor exclude other set-valued transport or a future demonstrated cost gain.

## Provenance and replay

The export obtains all 26 exact dyadic anchor coefficients from the pinned 192-bit correlated record. It retains the full inherited physical error ledger, per-time-slab uncertainty/increment allowances, original acquisition precision/callback count, historical residual preparation and original source/code/record pins. Initial export requires the historical stored setup hash. Later consumption checks the canonical mathematical setup hash, omitting observational acquisition times/callbacks while retaining exact source coefficients, radii, tails, parameters and analytic source pins. Runtime verifies the nominal anchor coefficients, slab allowances and error ledger against their pinned original record. The reviewer independently verified that observational time/callback mutations preserve this canonical hash, while mutations of a midpoint mantissa, quadrature-radius exponent, analytic note pin or retained-mode parameter change it. Both 192/256 consumers use the same historical 192-bit source setup. There is no second source quadrature in these runs.

An independent 192-bit execution reproduced every mathematical run field in the primary192-bit output exactly after removing only consumer_seconds. The reviewer did not reuse the primary output as an input. Producer hash at replay:5df0d372c4a06e628a406d84d6c32ff8fc1e888dee7f5963da5e9024adcdcc2e. Anchor export hash:3d2ed5f61daceb133347ee4fa9b7c062cec10e171c1a313a165590955f28ec4e.

The replay gives paid normalized real first-jet lower bounds:

| Consumer | Lower bound |
| --- | ---: |
| Analytic-only direct | >0.97252956036 |
| Analytic-only scalar | >-0.096724565; inconclusive |
| Source-informed uncalibrated scalar | >1.12807101641 |
| Source-informed calibrated scalar | >1.12886596528 |
| Source-informed uncalibrated pointwise | >1.38504846899 |
| Source-informed calibrated pointwise | >1.38593515763 |
| Complete-source raw direct | >1.34739469605 |
| Complete-source direct with midpoint propagation | >1.38987326350 |

Each run uses 4096 cells, 8224 full-jet evaluations, 4096 source-cell and 4096 source-midpoint evaluations, 8224 stable primitive evaluations, and zero complete-source quadratures. These combined-run counts and observational timings do not establish an accuracy-matched cost benefit for any route. The complete calibrated phase-jet error remains <0.000266447954, and the complete-source phase-error diagnostic is <2.348122e-10.

The calibrated consumer beats the raw source rectangle implementation but loses to the strongest source direct consumer given the same midpoint propagation. Calling that raw comparison a strongest-consumer gain would be incorrect. The source direct certificate's enclosure improvement is reusable evaluation information; it is not a new S03 arithmetic estimate and does not activate an extension. Stop this bounded comparison as contracted.

## Controls and continuation-note assessment

The reviewer read the complete control producer and record, then independently launched its final campaign. The independent control run passes all seven actual implementation mutants and all seven altered-input contracts, all 26 exact dyadic imports, off-center spatial/time normalizer checks, exact heat-event and nonconstant-phase oscillator fixtures, nonzero anchor uncertainty and the source-payment fixture. Five fresh source-specific event boxes reject strict first-jet acceptance using their own data; the Euler negative-Laguerre witness correctly rejects the signed test while its nonzero first jet is allowed to pass. No theta allowance is transferred to another source.

The constant source-ball fixture exercises the actual run() payment branch with a mocked exact constant jet family. It is a source-error bookkeeping test, not theta data, a heat-event certificate or primary-box evidence. It confirms that already-paid complete source balls receive no second source-error subtraction. Its in-memory double-payment mutant is detected.

Review caught a control-only nonfinite diagnostic: python-flint real-ball exponentiation x**2 can give nan on a zero-centered ball. The final controls replace those diagnostic squares by conservative finite products and explicitly reject nonfinite source jets, paid margins and signed diagnostic values before reporting them. The independent relaunch confirms the polynomial diagnostic is finite and all required event/witness outcomes remain valid. This issue never affected the primary producer, which uses the appropriate products for its relevant normalizer/phase squares. Final control producer hash: 1ffdd297f5a28f4c2ed1dc12a7104d6641688eaf7af63af0003863c925d5a372.

The continuation note was checked against both 192/256 runs. Its common weak decimal bounds, anchor uncertainty, physical-return error and cost counts are conservative for both. It correctly distinguishes actual source errors from evaluation ranges, the real first-jet bound from nominal second derivatives and complex bounds, raw source performance from the strongest matched consumer, finite old-box validation from new coverage, and same-model internal review from specialist review. The prescribed stopping decision is warranted. No blocking mathematical, code, control or claim-scope finding remains.

The root executor remains responsible for storing the final control/review records and updating the lane tracker, README and draft history.


Evidence: [consumer ledger](../numerics/S03_CALIBRATED_CONSUMERS_20261019.json), [independent consumer replay](../numerics/S03_CALIBRATED_REVIEW_REPLAY_192_20261019.json), [control record](../numerics/S03_T3_CONTROLS_20261019.json), [independent control replay](../numerics/S03_T3_CONTROLS_REVIEW_REPLAY_20261019.json). Read the [result summaries](../../../../../../result-summaries/README.md) and [patterns to avoid](../../../../../../avoid/README.md), especially [collision screens](../../../../../../result-summaries/12_collision_controls_and_screening.md), [scoped conclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [normalization](../../../../../../avoid/08_normalization_and_constant_slips.md).
