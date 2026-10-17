# Source-measurement audit: numerics

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Initialization model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

Reproducible code, parameters and small execution records.

**Round-one bounded replay completed 17 October 2026.** See
[code and small records](round1/README.md) and
[the numerical note](../notes/round1/03_BOUNDED_REPLAY_AND_POSITIVE_FEASIBILITY_CODEX_20261017.md).
The six observations, 24 conditioning combinations and 32 feasibility cases
have independent floating production and interval verification. The
[opening note, Section 5](../notes/round1/01_OPENING_ANALYTIC_AUDIT_AND_REPLAY_CONTRACT_CODEX_20261016.md)
fixes the six conditioning cases, equality/positive-feasibility cases, absolute
error units, precision comparison, resource limit and stopping answer for the
independent replay. Contract recorded 16 October 2026 by **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**. Execution and validation used the same recorded
configuration on 17 October 2026. No expanded grid or threshold check ran.

Before each run, state the question, domain, baseline, accuracy, resource
limit and stopping answer. Distinguish floating diagnostics from
outward-rounded certificates. Record parameters, environment and actual
model/effort; a replay or hash does not prove the mathematical implication.

Follow [LARGE_FILES.md](../../../../LARGE_FILES.md). Keep regenerable large
outputs external, with a tracked guide and small hash-bound records when
first needed; no large archive is created by this setup.

The [concrete onset calculation](round1/CONCRETE_ONSET_BUDGET.json) is a
separate fixed analytic budget for [Note 05](../notes/round1/05_CONCRETE_NORMALIZED_ONSET_BUDGET_CODEX_20261017.md).
It supplies the conservative sufficient threshold 3915 without new
physical-height evaluations. Recorded 17 October 2026, **gpt-6.1-sol**, effort **ultra**.
