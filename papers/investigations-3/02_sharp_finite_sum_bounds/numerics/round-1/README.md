# Round one sharp finite sum pilots

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**.
Full-history same-model subagents assisted; these checks are not independent
or cross-model review. The tail adapter was preserved byte for byte after
execution; its header describes the subagent's locally visible metadata.
The root session's recorded configuration also appears in
[REQUIRED_GATE_SET.json](REQUIRED_GATE_SET.json).

The [proof and budget ledger](../../notes/round-1/01_SHARP_WEIGHT_CONTRACT_AND_FEASIBILITY_20261017.md)
gives the analytic scope and open obligations. No complete Newman bound or
full finite-lane nonvanishing certificate is supplied here.

| Artifact | Meaning |
| --- | --- |
| [Sharp pilot](certify_sharp_pilot.py) and [record](SHARP_PILOT_RECORD_20261017.json) | Outward lower bound near .00177552691 for one row, N=690988, y=y0, t=.157 |
| [Budget adapter](check_t157_tail_budget.py) and [positive record](TAIL_T157_M600000_RECORD.json) | Complete error allowance <3e-7 and OV-free all-index tail budget with head 600000 |
| [Inherited-head diagnostic](TAIL_T157_M153814_RECORD.json) | The unchanged head does not close the same budget at the lower time |
| [Required gate set](REQUIRED_GATE_SET.json) | Declared replacement of historical target/floor/OV-containing checks, with reasons retained in the full records |
| [Exact transfer example](check_transfer_counterexample.py) and [record](TRANSFER_COUNTEREXAMPLE_RECORD_20261017.json) | The old generic plain-weight gate need not imply normalized sharp-weight transfer; this is not a theta counterexample |
| [Row run plan](PILOT_RUN_PLAN.md) and [tail run plan](PLAN.md) | Scope, resource caps, exploratory provenance and stopping rules |

Run from the repository root, writing disposable replay records outside
the tree:

```sh
python3 papers/investigations-3/02_sharp_finite_sum_bounds/numerics/round-1/certify_sharp_pilot.py --repo . --selftest --output /tmp/sharp-pilot-replay.json
python3 papers/investigations-3/02_sharp_finite_sum_bounds/numerics/round-1/check_t157_tail_budget.py --repo . --head 153814 --output /tmp/sharp-tail-negative-replay.json
python3 papers/investigations-3/02_sharp_finite_sum_bounds/numerics/round-1/check_t157_tail_budget.py --repo . --head 600000 --output /tmp/sharp-tail-positive-replay.json
python3 papers/investigations-3/02_sharp_finite_sum_bounds/numerics/round-1/check_transfer_counterexample.py --output /tmp/sharp-transfer-replay.json
```

All scripts use the Python standard library. The row and tail scripts
refuse changes to their hash-pinned canonical audit helpers. The tail
adapter records every exact source substitution; it retains failed legacy
comparisons and explicitly replaces only those whose changed mathematical
role is justified in the ledger. Its conversion from displayed decimal
bounds adds an outward last-place guard. Runtime, interpreter/environment
fields where supplied, and source hashes identify these executions;
wall times and memory are machine dependent.

The new row weight uses integer arithmetic and conservative error bounds.
For errors in B,A,g,c, first bound the error in gA; absolute values and max
are 1-Lipschitz. The multiplier c=(1-g)/(1+g) is enclosed directly. The
G^-sigma scalar error is also taken directly from interval widths, rather
than assumed to satisfy the table relative-error construction. The
inherited positive CS accumulation allowance 1e-35 is conservative for the
45-digit arithmetic and fewer than 3,840,000 additions used here.

The committed records are small. No large regenerable dataset, full row
corpus or third-party document is stored. The whole-strip transfer is certified below. Finite-row floors, seams
and a justified producer contract remain required before a full campaign.

## Completed active branch transfer

The [bounded implementation note](../../notes/round-1/02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md)
now certifies the full four-leg transfer at t=.157, y in
[sqrt(.0350708),sqrt(.686)]. This is same-model internal work,
**gpt-6.1-sol (Codex), effort ultra**, prepared for Edward Baker,
17 October 2026. Finite row floors/coverage remain open.

- [Interval engine](check_sharp_y_transfer_gate.py),
  [first plan](GATE_RUN_PLAN_20261017.md), and
  [first record](SHARP_Y_TRANSFER_GATE_RECORD_20261017.json): three full
  smaller legs and complete largest-leg prefix 0–171; the original
  largest-leg box-budget stop remains visible.
- [Completion wrapper](complete_sharp_y_transfer_gate.py),
  [completion plan](GATE_COMPLETION_PLAN_20261017.md), and
  [completion record](SHARP_Y_TRANSFER_COMPLETION_RECORD_20261017.json):
  complete largest-leg suffix 172–242, restarting pattern 172 from its full
  root. The exact prefix/suffix partition supplies the four-leg conclusion.
- [Separate arithmetic checker](check_gate_arithmetic.py) and
  [record](GATE_ARITHMETIC_CHECK_RECORD_20261017.json): direct 110-digit
  comparisons, exact adverse control rejection, and feasible-integer
  trimming checks; this is a same-model check, not independent review.
- [Floating scout](scout_sharp_y_transfer_gate.py),
  [plan](FLOAT_PLAN.md), and [record](FLOAT_GATE_SCOUT_RECORD_20261017.json):
  sampled diagnostics only; no floating sign supplies certified coverage.

The interval engine preserves h=log N and v=log(n/N), every possibly active
branch and all zero-containing numerator intervals. It uses analytic
singleton and exact-prime cases, with proofs in the note. A hash of accepted
leaves identifies a run; outward comparisons establish the signs. No
extremal slack is inferred from the stopping rule or counts.

Replay with outputs outside the repository. The completion wrapper uses
the preserved first record in this folder and checks its exact complete
prefix; it does not reuse partially completed work for pattern 172.

```sh
python3 papers/investigations-3/02_sharp_finite_sum_bounds/numerics/round-1/check_sharp_y_transfer_gate.py --output /tmp/sharp-gate-first-replay.json
python3 papers/investigations-3/02_sharp_finite_sum_bounds/numerics/round-1/complete_sharp_y_transfer_gate.py --output /tmp/sharp-gate-completion-replay.json
python3 papers/investigations-3/02_sharp_finite_sum_bounds/numerics/round-1/check_gate_arithmetic.py --output /tmp/sharp-gate-arithmetic-replay.json
python3 papers/investigations-3/02_sharp_finite_sum_bounds/numerics/round-1/scout_sharp_y_transfer_gate.py --output /tmp/sharp-gate-float-replay.json
```

Runtime caps are deliberate: a slower host may leave a run incomplete.
Report that stop; do not interpret it as a failed mathematical inequality.
The committed completion record and first record together describe the
executed cover. All new sources and records are small; no row corpus or
large derived data is created.
