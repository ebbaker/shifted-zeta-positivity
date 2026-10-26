# AN04: integration of the first negative-time correction

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
verified from this turn's metadata. Ansatz chat0003, thread
`01a17626-abf5-7a90-9ba2-7a2395254aee`.

**Status: assessed-result manuscript integration and production checks;
no new mathematical estimate or review-status promotion.** Execution of
[HDA-A02-AN04 r1][packet] is complete. [Note10][n10] and [Review07][r07]
remain the analytical source and same-model internal assessment of the
bounded theorem. The [input manifest][inputs] pins the current working
tree at this turn's start; the [production assessment][review] and
[build record][build] describe the resulting manuscript.

## Integrated result and its limits

The maintained [manuscript source][tex] now includes Section6.3, **One
evaluated correction at fixed order**, with Proposition6.1:

- Equation6.9 evaluates the gamma-mode correction
  `h exp(T beta²)[1+gamma(T+2T² beta²)]`.
- Equations6.10--6.13 retain K=1 canonical RS initial data, exact
  adjacent arithmetic transfer, the bounded real-data correction integral,
  all N modes and the resulting model.
- Equations6.14--6.16 state field/j<=3 and first time errors
  `C |G|X^-5/4` and actual residual/residual_z `C |G|X^-7/4`, uniformly
  for 1<=T<=2 on full fixed complex charts with an extra analytic unit.
- The proof separates canonical initial matching from residual
  cancellation. It includes the complete mode population, transverse
  n/height cancellation, weighted complex Gaussian moments, true and
  artificial tails, fixed-margin Cauchy and direct first-time control.
- Equation6.24 gives the equivalent elementary-arm correction including
  the initial gamma phase and slope terms. The RS integral remains.
- Equation6.25 states the remaining outer allowances
  `X^-5/4 exp(TL²/16)` and `X^-7/4 exp(TL²/16)`. Their growth at fixed T
  limits those bounds; it is not an actual error lower bound or a
  universal obstruction to short resummation.

The old growing-order outer-scale comparison and its zero frozen-chart
residual remain intact and stronger at their stated scale. The new
fixed-order result is not an integral-free short formula, reduced mode
count, useful-cost theorem or physical transfer.

Section8 inserts the actual residual into parent PE37--39's potential,
density and current forcings. It explicitly names the first unpaid
consumer: a regulator-uniform weak/collar comparison for this model and H,
including the actual signed Q. No simple-root collar or inherited
positive-time transfer is presumed. Physical q, fixed K, normalization,
xi anchor and joining defects are unchanged.

The abstract, LLM acknowledgement, opening objective, remaining-negative
limits, coverage table, acceptance paragraph, continuation priorities and
internal bibliography now reflect the accepted bounded result. Statements
that AN03 was an unproved future target were removed from current prose;
the historical frozen packet and earlier sources remain.

## Production and preservation checks

The existing build entry completed successfully with latexmk/pdfLaTeX:
**29 pages, no build warnings and no unresolved reference markers**.
The reading PDF is only in the ignored root output/pdf/heat_density_ansatz
folder. Its exact path, source/PDF hashes, byte sizes and build identity
are in the build record. No new snapshot or colocated manuscript PDF.

All 29 pages were rendered and inspected in contact sheets, with readable
page inspection of the title/acknowledgement, contents, new correction
and proof (pages14--16), physical forcing (page21) and coverage table
(page24). No clipping, overlap or missing glyph was found. The contents
still fit on one page; the coverage table and page numbering remain clear.

All **73 pre-existing equation/align/gather/proposition blocks** were
found verbatim in the integrated source. Notes03--10, Review07, retained
A03-AN01 and the standing instructions were not edited. Hashes and link
checks establish identity and navigation, not mathematical correctness.
The source-diff review was internal and same-model; no specialist or
cross-model review is claimed. No numerical or machine-symbolic research
campaign was performed.

## Disposition and continuation

Close **AN04** at faithful integration/build scope. The theorem remains
**proved in-note from named classical inputs, same-model internal
analytical assessment only**. HDA-A02 remains **Partial**; parent
HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled are unchanged.

This is an approximation result, not an RH-equivalent criterion. Both
the [result index][results], especially [heat-flow11][r11] and
[controls12][controls], and the [avoid index][avoid], especially
[shared-premise review05][a05], [scope07][a07], [separate-bounds12][a12]
and [status19][a19], govern interpretation. The manuscript's control
screen preserves Note10's named failed canonical arithmetic/completion
premises; heat evolution identities themselves exclude none.

**Next deliverable — Analysis, Sol:** [AN05 r1][next], a separate compact
negative-time family with declared fixed endpoints and explicit
endpoint/buffer dependence of allowances and onsets. It is prepared,
not executed or dispatched. This integration establishes no larger
time domain. Routine endpoint/kernel bookkeeping does not currently
justify Astra escalation. A03-AN01 remains preserved supporting work.

The unique chat0003 history is refreshed through the shared recorder;
the final answer is captured by the bounded exact-turn worker after
completion, not written into the archive in advance.

[packet]: ../research-progress/handoffs/HDA-A02-AN04.md
[n10]: 10_FIRST_NEGATIVE_TIME_EVOLUTION_CORRECTION_20261025.md
[r07]: ../reviews/07_FIRST_NEGATIVE_CORRECTION_ASSESSMENT_20261025.md
[inputs]: 11_AN04_INTEGRATION_INPUTS_20261025.json
[review]: ../reviews/08_AN04_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261025.md
[build]: ../manuscript/BUILD_RECORD_20261025_A02_AN04.json
[tex]: ../manuscript/main.tex
[next]: ../research-progress/handoffs/HDA-A02-AN05.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a19]: ../../../../../avoid/19_status_files_that_lag_the_findings.md
