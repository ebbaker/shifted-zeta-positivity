# S05 complete-source enclosure comparison

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**. Outward Arb/Acb
computations and exact integer algebra; same-model internal review.

[check_covariant_source_enclosures.py](check_covariant_source_enclosures.py)
compares the existing expanded `source_jet(...,t=0)` with coefficient-combined
Horner evaluation and modular fixed-point Taylor evaluation of the complete
source and its first two **source** derivatives. Requires python-flint 0.9.0.

From the repository root, write fresh outputs outside the checkout:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics/check_covariant_source_enclosures.py --repo . --output /tmp/S05_SOURCE_192.json --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics/check_covariant_source_enclosures.py --repo . --output /tmp/S05_SOURCE_256.json --bits 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

Retained records:

- [192-bit comparison](S05_COMPLETE_SOURCE_ENCLOSURES_192_20261018.json).
- [256-bit comparison](S05_COMPLETE_SOURCE_ENCLOSURES_256_20261018.json).
- [Baseline algebra, signed-bridge, and control regression](S05_BASELINE_REGRESSION_20261018.json).

The local Taylor comparison passes for source orders 0,1,2 on
`[0,1/64]`, `[0,1/256]`, `[0,1/1024]`, including infinite mode tails and
eighth-derivative remainders. At the smallest cell, enclosing-radius ratios
against the actual expanded baseline exceed 894.47, 7.29, 2394.90.
Fused Horner is not uniformly tighter for the second derivative on the
shifted line; 34 of the 64 cells become wider.

The source bounds cover whole cells analytically. Overlap and point checks
are additional diagnostics. Endpoint odd zeros come from the known full
modular identity. The geometric tail theorem is proved in the [note][note];
the finite exact checks do not prove infinite modularity. Every point
coefficient and derivative-eight cell bound includes its complete tail.
Rounding stays inside the outward ball operations. There is no quadrature,
source-integral truncation, or physical whole-cell propagation in this task.

For the regression record, rerun these existing checkers to fresh paths:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/check_hodge_modular_rotation.py --output /tmp/S05_LADDER.json
python3 papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_signed_bridge.py --output /tmp/S05_BRIDGE.json
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/S05_CONTROL_RECEIPTS --output /tmp/S05_CONTROLS.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The combined retained regression record identifies this replay's actual
model/effort and embeds the original checker receipts. Their historical
authoring configurations are preserved and are not this replay's settings.
The five event rejections and separate Euler witness are existing
source-specific interface checks, not a new source-evaluator exclusion test.

Each comparison record pins its executing script and imported source files.
Hashes identify bytes; they do not prove the mathematics. Whole-run timings
are diagnostics, not matched-accuracy speedup measurements. The component
does not claim a smaller physical `H,Hx,Hxx` error or new coverage. A useful
spectral handoff remains unpaid; follow [the assessment][review]. All
retained files are below 1 MiB; no bulk derived data are generated.

[note]: ../notes/01_COMPLETE_SOURCE_JETS_AND_FIXED_POINT_ENCLOSURES_20261018.md
[review]: ../reviews/01_COMPLETE_SOURCE_ENCLOSURE_INTERNAL_REVIEW_20261018.md


## S05-T1 consumer-fit audit and shifted-acquisition probe

19 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. [Note 02](../notes/02_SOURCE_CONSUMER_FIT_AND_SHIFTED_ACQUISITION_SELECTION_20261019.md)
records the real-parity no-fit decisions and the selected finite factoring
candidate. Requires Python with python-flint0.9.0. From repository root:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics/probe_shifted_source_consumer_fit.py --repo . --output-dir /tmp/S05_T1_PROBE --bits 192 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics/audit_source_consumer_budgets.py --repo . --output /tmp/S05_T1_BUDGET_192.json --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The probe reacquires only j=0 with three algebraically identical forms on
S01's exact contour, modes1..11 and original tolerances. Factoring while
retaining the common exponential improves the coefficient radius; moving
that exponential inside each mode worsens quadrature despite narrower
source-cell ranges. No real parity, infinite-source tail, other50 midpoint
coefficients or physical consumer is imported into this finite probe.
The S01 historical complete ledger's producer and every source pin are
verified before using it for the conditional feasibility scale. Source
and code pins fail closed. A separate audit evaluates S06 endpoints and
analytic L1 moments afresh; real local-range budget share is zero.

Small retained records contain aggregate128-cell diagnostics, exact
dyadics, coefficient errors, source identities and complete-budget context.
The regenerable per-cell table is not versioned. Elapsed times are
diagnostics, not measured speedups; no factor-two cost result is claimed.

- [192-bit fit probe](S05_T1_SHIFTED_SOURCE_FIT_192_20261019.json)
- [256-bit fit probe](S05_T1_SHIFTED_SOURCE_FIT_256_20261019.json)
- [192-bit budget audit](S05_T1_BUDGET_AUDIT_192_20261019.json)
- [256-bit budget audit](S05_T1_BUDGET_AUDIT_256_20261019.json)
- [Separate192 replay](S05_T1_SHIFTED_REVIEW_192_20261019.json)
- [Separate256 replay](S05_T1_SHIFTED_REVIEW_256_20261019.json)
- [Separate192 budget replay](S05_T1_BUDGET_AUDIT_REVIEW_192_20261019.json)
- [Precision, metadata and stale-source guards](S05_T1_REVIEW_GUARDS_20261019.json)
- [Fresh inherited controls](S05_T1_CONTROLS_20261019.json)
- [Internal assessment](../reviews/02_SOURCE_CONSUMER_FIT_INTERNAL_REVIEW_20261019.md)

The existing replay_nonstationary_controls.py command above reproduces
the control screen with fresh paths. Its retained producer date is
18 October; this execution was19 October. Five source-specific event boxes
and the separate Euler witness reject in the unchanged consumer. No new
acceptance interface or new covered physical domain is introduced.


## S05-T2 complete shifted acquisition and physical consumer

19 October 2026. For Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. [Note 03](../notes/03_COMPLETE_SHIFTED_ACQUISITION_AND_CONSUMER_COMPARISON_20261019.md)
records the complete added-error gate. Requires python-flint0.9.0.
Reproduce allthree acquisitions and bothdeclaredselectors on the fixed B
domain, including all51 coefficients, common payments and physical cells:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics/compare_complete_shifted_source_consumers.py --repo . --output-dir /tmp/S05_T2_REPLAY --bits 192 256 --comparison-contract papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/notes/04_S05_T2_COMPARISON_CONTRACT_20261019.md --expected-source-pins papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics/S05_T2_COMPLETE_SHIFTED_SOURCE_192_20261019.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

Eachsetup retains the original60-second/2-million-callback budget,
integral1e-13/1e-30 tolerances, fixedcontour,modes1..11 and degrees24/12.
The comparison uses the original40closedcells and adaptiveconsumer.
Allacquired midpoint/radius tuples and complete error ledgers are saved.
The mathematical approximationerror epsilon and outward polynomialimage
are distinct; both are paid in the returnedphysicalenclosure.

- [192-bit fullcertificate](S05_T2_COMPLETE_SHIFTED_SOURCE_192_20261019.json)
- [256-bit fullcertificate](S05_T2_COMPLETE_SHIFTED_SOURCE_256_20261019.json)
- [Compact separate verification/guards receipt](S05_T2_INDEPENDENT_REVIEW_20261019.json)
- [Fresh source-specific actual-consumer controls](S05_T2_CONTROLS_20261019.json)
- [Separate same-model assessment](../reviews/03_COMPLETE_SHIFTED_CONSUMER_INTERNAL_REVIEW_20261019.md)

Duplicate fullfreshreview outputs remain regenerable outside the repository.
The compact receipt records stored and canonicalnumeric hashes, exact
rational ledger checks, output-containment checks, sourcepins and35guards.
Hashes identify data; checked arithmetic proves the recorded inequalities.
To reproduce its verification after the fullreplay above:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics/review_complete_shifted_source_comparison.py --repo . --producer papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics/compare_complete_shifted_source_consumers.py --comparison-contract papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/notes/04_S05_T2_COMPARISON_CONTRACT_20261019.md --reports-dir papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics --replay-dir /tmp/S05_T2_REPLAY --work-dir /tmp/S05_T2_GUARDS --output /tmp/S05_T2_VERIFICATION.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

Fresh controls run check_paired_consumer_controls.py in S01/numerics with
fresh work/output paths; it replays fiveeventboxes/Euler through actual
signed_cell, paired invalidsettings and non-even boundaryorders0..2.
No theta constants are assigned to altered sources. No newacceptance
interface, coverage or Newman bound. The selector charges allthree
acquisitions; one-run times are diagnostic and earn no factor-two costclaim.
Every retained file is below1MiB; no bulkduplicate replaydata are versioned.
