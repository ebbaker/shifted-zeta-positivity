# Three regime dynamics research notes

26 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), actual recorded effort max**.

The opening discussion remains in [brainstorm](../brainstorm/README.md).
Subsequent analytical work, 26 October 2026, prepared for Edward Baker
with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**:

| Note | Deliverable and scope |
| --- | --- |
| [01 buffered response](01_BUFFERED_RESPONSE_AND_RESOLUTION_20261026.md) | Fixed-window O(tau^2) remainder, multiplicity-dependent regulator allowance, source transfer and conditional growing-window payments |
| [02 Dobner budget](02_DOBNER_COMPLETE_CONDITIONAL_BUDGET_20261026.md) | Explicit finite-prime recurrence and complete conditional witness-height construction; seed data and imported constants remain inputs |
| [03 small-time seeds](03_SMALL_TIME_CANONICAL_SEEDS_AND_WITNESS_ENVELOPE_20261026.md) | Analytical finite-family count/wall/location for0<tau<=1 and uniform source-derived upper envelope exp exp(C_d tau^{-3}); imported approximation constants remain uninstantiated |
| [04 direct seed lattice](04_DIRECT_DOBNER_SEED_LATTICE_20261026.md) | Exactly one seed per lattice disk for tau>=32; deletes recurrence in transport on fixed[32,C] |
| [05 narrower small-time seeds](05_NARROW_SMALL_TIME_DOBNER_SEEDS_20261027.md) | Actual O(sqrt(tau)) seed strip, constant scaled count/floor, complete sharper tail/recurrence and exp exp(C_d/sqrt(tau)) witness envelope |
| [06 chat0001 summary](06_CHAT0001_RESEARCH_SUMMARY_20261027.md) | All five analytical deliverables in Research three-regime heat flow, current best bound, evidence, limits and bounded handoff |
| [03 canonical allowance failure](03_CANONICAL_FIXED_STRIP_ALLOWANCE_FAILURE_20261026.md) | Source-defined count upper bound; regulator-optimized failure of a polynomial raw-error budget and fast-height failure of the separate global source-majorant gate |

See [Review01](../reviews/01_OPENING_RESPONSE_AND_BUDGET_REVIEW_20261026.md)
and the [sole progress register](../research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md).
[Review02](../reviews/02_DOBNER_CANONICAL_SEED_ACQUISITION_REVIEW_20261026.md)
checks the Dobner continuation. These are analytical results with internal
same-model review. Note03 now gives a source-derived upper envelope;
no numerical certificate, lower escape rate or regime exclusion is supplied.

The [Note03 review](../reviews/02_CANONICAL_ALLOWANCE_FAILURE_REVIEW_20261026.md) records separate read-only
same-model checks. Its negative result concerns the specified sufficient
allowance, not the actual response error or every growing-window method.

27 October 2026 update, prepared for Edward Baker with substantial LLM
assistance, **gpt-6.1-sol, actual effort ultra**: [Review03](../reviews/03_NARROW_SMALL_TIME_DOBNER_REVIEW_20261027.md)
checks the narrower-seed result and chat0001 summary. The older small-time
exponent remains a valid baseline; Note05 gives the current improved
asymptotic envelope, without a calibrated numerical crossover.
