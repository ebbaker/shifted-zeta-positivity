# Shared symmetry numerics

19 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), actual effort ultra**. These are bounded internal
research records, with no specialist human review. The older
`SEVEN_PROGRAM_REVIEW_REPLAY_20261018.json` and
`RESEARCH_PLAN_CONTROL_SCREEN_20261018.json` retain their original status
and provenance.

## GEO-T1: fixed-B boundary winding and optimized direct comparison

[Contract](../notes/05_GEO_T1_MATCHED_WINDING_COMPARISON_CONTRACT_20261019.md),
[result](../notes/06_GEO_T1_WINDING_AND_DIRECT_COMPARISON_20261019.md),
[internal review](../reviews/01_GEO_T1_WINDING_DIRECT_INTERNAL_REVIEW_20261019.md).
Closed B=[1/100,1/5]x[999,1001], unchanged complete physical theta jets with
fixed positive Gc. Both consumers pass; winding degree0 uses7accepted
segments/10complete three-jet calls/zero source vertex calls, and direct
certification uses3full-time strips/7calls. Both pay identical complete
errors and fresh acquisition. The factor-two cold-cost gate fails. B was
already covered; stop this bounded comparison, without a global claim.

- [192-bit comparison](GEO_T1_COMPARISON_192_20261019.json) and
  [256-bit comparison](GEO_T1_COMPARISON_256_20261019.json): exact setup
  dyadics, complete quadrature/Taylor/mode/source error ledgers, source pins,
  full boundary partitions, rational polygon, degree, exact direct cover and
  observed timings. The source acquisition is fresh at each precision;
  separate per-method caches start empty. Mathematical content excludes
  timing and callback observations, as defined by the comparison producer.
- [Fresh reviewer192 replay](GEO_T1_REVIEW_REPLAY_192_20261019.json): separate
  acquisition agrees exactly with primary192 mathematical content, not
  necessarily timings. Cross-precision mathematical hashes are not expected
  to agree because precisions/enclosures differ.
- [192-bit actual-helper/direct controls](GEO_T1_WINDING_CONTROLS_192_20261019.json)
  and [256-bit controls](GEO_T1_WINDING_CONTROLS_256_20261019.json): all36checks
  pass; each polynomial source supplies its own complete interval jet.
  Collision degrees -1,-1,-2 reject, boundary events/uncertainty remain
  inconclusive, and nonvanishing linear/constant first jets pass. Actual
  direct-consumer tests retain the heat event and uncertainty as inconclusive.
- [Source regression](GEO_T1_SOURCE_CONTROLS_20261019.json): five source-own
  surrounding-event jets reject in inherited interfaces and in the actual
  new strict-coordinate separator; Euler is a negative-Laguerre signed
  witness. These are not whole-boundary certificates for those sources.
  The inherited producer hardcodes18October; `source_script_date` preserves
  that field and the outer date/execution timestamp record this run.
- [Exact wall-flux replay](GEO_T1_WALL_FLUX_REPLAY_20261019.json): unchanged
  heat-polynomial and moving-wall checker, including tangencies and odd
  crossings. Its original authoring record is nested separately from this
  run's actual model/effort/date. No new theta certificate follows from it.
- [File identities](../reviews/GEO_T1_FILE_IDENTITIES_20261019.json) identify
  these installed bytes; hashes are provenance, not proof.

The [helper](winding_helpers.py) requires exact rational domains and a
whole-segment physical first-jet encloser. It validates all four oriented
faces before building a rational polygon from incident strict halfplanes.
The [comparison](compare_winding_direct.py) checks the frozen contract and
source hashes before fresh acquisition. It gives both methods the
intersection of two valid Horner images, each with the full error, and
includes all direct midpoint calls. The
[control checker](check_winding_controls.py) imports the actual two
implementations, rather than substituting a mock acceptance decision.

## Reproduction

From the repository root with Python3.10+ and python-flint0.9.0 available,
write fresh outputs to a new temporary directory. Run the two source
acquisitions sequentially if interpreting timings; simultaneous source
integrations distort that metric. Example output location `/tmp/geo-t1-replay`
should exist before the inherited regression commands.

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/numerics/compare_winding_direct.py --repo . --precision 192 --output /tmp/geo-t1-replay/comparison192.json
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/numerics/compare_winding_direct.py --repo . --precision 256 --output /tmp/geo-t1-replay/comparison256.json
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/numerics/check_winding_controls.py --precision 192 --output /tmp/geo-t1-replay/controls192.json
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/numerics/check_winding_controls.py --precision 256 --output /tmp/geo-t1-replay/controls256.json
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/geo-t1-replay/source-receipts --output /tmp/geo-t1-replay/source-controls.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_spacetime_wall_flux.py --output /tmp/geo-t1-replay/wall-flux.json
```

The saved source regression additionally feeds every `event_jet_enclosures`
list in `screen.event_rejections` to `winding_helpers.strict_separator`,
requiring `None`. Those displays are outward complete source-own balls;
no whole-boundary evaluator for the altered source is fabricated. The
wrapper adds actual execution provenance while preserving the inherited
producer date. The wall-flux wrapper retains its entire original producer
record, including its authoring date/model, under `source_authoring_record`.

The comparison's exact saved polygon can be independently replayed with
`polygon_from_halfplanes` and `polygon_winding`; direct coverage can be
checked from the exact accepted t,x intervals. A fresh source replay checks
more than the saved polygon's combinatorics. Read the result's scope before
reusing any record: no new signed estimate, S07-T3 input, region extension
or universal boundary-method cost limitation is established.


## UAR-01 contract checks

[Contract](../notes/07_UAR01_CORRECTED_RESIDUAL_AND_TRANSITION_CONTRACT_20261019.md), [review](../reviews/02_UAR01_CONTRACT_INTERNAL_REVIEW_20261019.md), and [source-pinned receipt](UAR01_CONTRACT_CHECK_20261019.json). Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**, 19 October 2026. The standard-library [checker](check_uar01_contract.py) uses exact rational fixtures for profile/jump algebra, signed prefixes, forcing and guards. These checks do not prove imported analytic theorems or a theta residual estimate. No unchanged acceptance replay is presented as a new consumer validation.

From the repository root:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/numerics/check_uar01_contract.py --repo . --verify papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/numerics/UAR01_CONTRACT_CHECK_20261019.json
```

Verification fails closed on changed/missing pinned sources. A changed source needs assessment before producing a new receipt with `--write-record`, `--model` and `--effort`; a new hash does not validate changed mathematics.
