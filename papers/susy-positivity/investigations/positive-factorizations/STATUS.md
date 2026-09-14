# Status: working draft 0.2

11 September 2026. Not released or independently reviewed. No RH or new
zero-free-region claim. See [round 3](INVESTIGATION_round3.md) for the latest
manuscript investigation and [the manuscript](manuscript.pdf) for proofs.
This ledger describes v0.2 at its original date. The subsequent
[round-4 review](archive/progress-reports/REVIEW_round4_20260911.md) proves a
shift-uniform odd gamma factor in its stated range and a positive even
mean-zero subspace; the remaining even scalar and full completion stay open.
See the [program overview](../../PROGRAM_OVERVIEW.md) for the current direction.

| Result | Current verification |
|---|---|
| Small-window full factor, `L<=1/4`, `0<=omega<=1/2` | Analytic proof; round-1 floating-point identity checks replayed |
| Positive kinetic auxiliary tower and graded realization | Analytic proof; round-2 diagnostics replayed; operator domains await specialist review |
| Pairwise obstruction at `L=2/3` | Analytic reduction and exact rational sign certificate replayed |
| Finite-network Schur restriction and coherent toy model | Proofs and round-2 controls; no unrestricted continuum-limit theorem |
| Complete central odd gamma factor, `L<=7/10`, floor `1/100` | New analytic construction, exact rational scalar interval cover, independent quadrature identities |
| First-prime stabilization and negative edge remainder at `L=1` | New exact rational certificate on the unit linear input |
| First-prime parity/cap-reflection identity | Direct derivation and full-translation numerical controls of both signs |
| Whole-line `L2` closability obstruction | Written proof; not an obstruction on every possible input topology |
| Complete even-sector factor, shift-uniform parity factor, joint first-prime positive model | Open |
| Global arithmetic selection rule / all-depth positivity | Open |

Validation records are in `checks/round1`, `checks/round2`, and `checks/round3`.
The first two diagnostic JSON files are preserved historical outputs; the
third records the original round-3 environment. All three are historical
outputs. `manifest.json` now separates those historical checks from current
file hashes and links the [fresh reorganization verification](../../archive/REORGANIZATION_20260912.md). A successful checker does not independently
validate the analytic reduction that supplies its inequalities.

AI assistance was used for derivation, coding, verification, and writing.
Independent mathematical, domain, and priority reviews remain outstanding.
