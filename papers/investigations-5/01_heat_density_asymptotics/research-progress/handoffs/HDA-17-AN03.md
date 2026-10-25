# HDA-17-AN03 — positive cubic-Hermite finite source

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from session metadata; chat **0011**, thread
`01a170a3-5f6e-7aa2-9e33-bcae4835c782`.
**Parent:** HDA-17, supports HDA-18. **Request revision:** r1.
The author explicitly requested continuing the positive cubic-Hermite
source approximation, including explicit remainder bounds at the same
points. The sole progress register owns live phase/status. AN01/AN02 stay
closed at their original scopes.

## REQUEST

**Question:** Does a positivity-preserving cubic-Hermite finite source
reduce the dominant source budget sufficiently at the existing t=64 points,
with an informative same-mesh and comparable-storage-cost comparison?

Retain the canonical theta source, cutoff 1.5, four arithmetic modes,
H_t=-H_zz, unnormalized observables, exact physical common regulator,
eta=1/2, ell=2,h=1/2, and AN01 targets/80-10-10 allocation. Read repository
instructions/indexes, Notes 20/23/34--36, Review 19 and the AN02 evidence.
No manuscript/prior numerical record or old request may be overwritten.

1. Derive a continuous complete Phi^(4) cap, cubic Hermite interpolation
   remainder and separate value/derivative endpoint-mode remainders.
   Integrate positive absolute cardinal shapes against AN02 convex chord
   weights 8/12. A linear fallback uses its second-derivative remainder.
2. Define the finite source by stored nonnegative Bernstein coefficients.
   If a cubic cell fails coefficient nonnegativity, use its degree-elevated
   linear interpolant. Include exact stored-coefficient construction
   discrepancy separately from nodal-value and nodal-derivative arithmetic.
   Underflowed coefficients are not positive source tails; retain all tails.
3. Exactly check at most 8 handpicked polynomial controls: cubic reproduction,
   quartic remainder factor, endpoint perturbations and fallback positivity.
4. Source/field trials: uniform 192 Hermite; adaptive 384 and adaptive 768
   Hermite, using the same source-only AN02 density/pilot 4096/floor 0.05
   rule at those cell counts. No field/zero data selects source nodes.
   Compare adaptive 384 Hermite's 770 nodal values/slopes with linear 768's 769
   values; adaptive 768 supplies the same-mesh comparison. Retain actual
   coefficient/quadrature costs and fallback counts/ranges.
5. Field/filter observations are exactly t=64,x=4,y=0 and 1/2 for each
   source. Reuse the fixed AN02 composite geometry, Gaussian 8/12 per panel,
   and source Gaussian 8/12. Compute both weak and selected direct observable
   source-rule refinement, positive-envelope changes and direct/weak checks.
   Retain all 91 externally targeted local rows. No switch-time expansion.
6. Give an explicit local-series/ideal-Gauss source-evaluator truncation
   allowance where tractable, distinct from later rounding and filter
   integration. Use 80 digits for selected nodal arithmetic checks; no new
   120-digit escalation. Never promote a candidate allowance to certified.

**Evidence:** routine inequalities proved in-note; floating diagnostic
sufficient for cost/accuracy. Exact nonnegative stored coefficients prove
positivity of that chosen polynomial source, not accuracy of canonical
nodal data. Keep source interpolation, omitted values, omitted derivatives,
complete tail, nodal-value/derivative candidates, coefficient construction,
source-ledger arithmetic, evaluator truncation/rounding and filter errors
separate. Continuous source inequalities and sampled observable/filter
agreement do not accept the continuous D box or time interval.

**Work cap:** 30 minutes aggregate numerical execution; only the stated
sources, observations and two refinement levels. Stop once the source
comparison and next unpaid error are clear. No source cutoff/mode sweep,
new root search, regulator change, gamma onset, endpoint field guess or
spatial/global splice. A positive sampled source budget may justify a
later bounded certification question, not automatic HDA-17 acceptance.

**Outputs:** next numbered research note, clearly named scripts/small JSON
record, internal assessment, appended RETURN/DISPOSITION, current ledger/
README/history links and concise DRAFT_HISTORY milestone. All files below
1 MiB; no large derived arrays or new manuscript snapshot. Sol may record
the bounded disposition; escalate only a named extra high difficulty issue.

## Frozen inputs

| Input relative to root | SHA-256 |
| --- | --- |
| `GPT_RESEARCH_MODEL_WORKFLOW.md` | `38baa14d26c6d48a76dbe7da60c07dd798f3fe02d92a6cb243decf52ba120711` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md` | `5f478ed088e2f77f8818edadfd36b0d9b56ff4174539df86a332b181813e3152` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/23_FINITE_TRANSITION_CONTRACT_AND_LOCAL_BOUNDS_20261024.md` | `30a1ff1b59c2b74893f55230930c8795609186ca2be06a8bc2e5872090bc368d` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/34_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_20261024.md` | `daeefac6d0b47602d84312e547878612f8a97526cfa8a01a080829c9a571fc2f` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/36_SOURCE_CURVATURE_AND_PEAK_INTEGRATION_20261024.md` | `1ba6d0404da43b28d2080cdbe3a39c629eb62b532a2c536a9556e59374035e44` |
| `papers/investigations-5/01_heat_density_asymptotics/reviews/19_SOURCE_CURVATURE_AND_PEAK_ASSESSMENT_20261024.md` | `15b77431f92ff83aedc67ff532cdc6dce1ac92f0d6ee0aab9edeef88d719a908` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/source_accuracy_improvements.py` | `ba1b01fdf391600a29978e01801939b1daf3bfb68def309a0d20d95e03bbdd9d` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/source_peak_diagnostic.py` | `66e5ae365a8e03b0afea5c2de950790c12e30f54beef697ebb7b2627f4d49ace` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/SOURCE_PEAK_DIAGNOSTIC_20261024.json` | `4ca139f2db505e5824881468c7909a72d040a533ebf2d35cf04869e8faa0b0e3` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/weak_coefficients.py` | `1ab138c89ce7a7083a1970c70edc8211cf486218e072d342774c781b5cb4a27d` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/weak_transfer_diagnostic.py` | `a4e704384c9766a72f6b643db0997eac7fb2ff0d82c54da78f8727ff11c204e2` |

## RETURN — Sol

Pending.

## DISPOSITION — Sol

Pending.


## REQUEST ADDENDUM — r2, directional gradient caps

24 October 2026, America/New_York; gpt-6.1-sol, actual effort ultra,
chat 0011. The r1 request and evidence above remain frozen. This revision
adds one routine positive-envelope comparison after r1's best source row
missed its 80% allocation by 10.5073%. Source, physical field, regulator,
normalization, targets and 80/10/10 allocation are unchanged.

**Question:** can a tighter valid cap on each physical potential-gradient
component remove that conservative Delta Q overrun with the same Hermite
source and observations?

For the exact ideal-Gauss 12 field G and error radius bars=d_source+d_eval12,
use LC8's frozen gradient-error envelope d_i(bars). The old universal cap
G_i bounds both H and G; the additional pointwise cap
|S_(G),i|+d_i(bars) also bounds both. Take the smaller before applying the
same LC9/10 positive convolutions. Keep x and y caps separate, form products
after the full-support convolution, and preserve the actual signed Q.
All field/gradient arithmetic and continuous filter integration stay unpaid.

Numerics are limited to the same adaptive 768 source at t=64,x=4,y=0,1/2,
with the same composite 8/12 geometry and primary source Gauss 12. Reuse r1
source/evaluator errors and source-rule 8/12 evidence. No new source mesh,
precision, mode count, filter level or test point is allowed. The total
AN03 numerical cap remains 30 minutes. Derive/audit the inequality before
execution; source allowance success at samples still cannot accept HDA-17.

Save a new supplemental script and small record, leaving the r1 record
unchanged. The final note/review and appended disposition should distinguish
r1 and r2. Keep only covariance rows as the added comparison; inherit all
other r1 rows unchanged. Stop after these two observations.

Frozen r1 input:

| Input relative to root | SHA-256 |
| --- | --- |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/POSITIVE_HERMITE_DIAGNOSTIC_20261024.json` | `bf134ed8ba5edc941b13cc32522b5aa433a77f4c50ff880c3d089b17288d3d89` |


## RETURN / DISPOSITION APPENDIX — Sol, r1 and r2

24 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, gpt-6.1-sol (Codex), actual effort ultra, chat 0011.
The preceding request/r1 input table/pending placeholders and r2 addendum
remain an unchanged prefix. This appendix supplies the completed return.

**Result:** complete Phi^(4) cell cap and all-mode tail; positive cubic
Hermite coefficients with linear fallback; separate endpoint value/slope
mode and arithmetic ledgers; exact stored-coefficient construction ledger;
positive chord integration and explicit ideal-Gauss source-evaluator
truncation inequality. Eight exact-rational polynomial control families
passed. [Note 37](../../notes/37_POSITIVE_HERMITE_SOURCE_AND_REMAINDERS_20261024.md)
and [Review 20](../../reviews/20_POSITIVE_HERMITE_SOURCE_ASSESSMENT_20261024.md)
hold the derivation and internal same-model assessment.

R1 compares uniform 192, adaptive 384 and adaptive 768 at exactly t=64,x=4,
y=0,1/2. Adaptive 768 reuses AN02's exact nodes and lowers its same-mesh
zeroth interpolation allowance about 1963 times to 5.34704e-8, with 1538
nodal values/slopes versus 769 linear values. The storage-matched 384
case retains a fallback-dominated allowance and source ratio 161.689.
Best r1 Delta Q at y=0 is 0.00884058 versus the 0.008 source allocation,
ratio 1.10507. That r1 failure and all its evidence remain unchanged.

R2 changes only valid directional common-gradient caps for covariance
rows on the same adaptive 768 source/observations. Source and observable
values are unchanged. All 91 sampled source rows fit their allocations;
worst ratio **0.688748481**, Delta Q at y=0, allowance **0.00550998785**.
At y=1/2 it is 0.00179015, ratio 0.223769071. Largest mapped ideal-Gauss
truncation/evaluator-allocation ratio is 1.40143e-8. Weak/direct filter
indicator ratios are 0.000823813/0.140097 and the positive-envelope
indicator is 0.00444251. These remain floating diagnostics.

Evidence: [immutable r1 record](../../numerics/POSITIVE_HERMITE_DIAGNOSTIC_20261024.json),
[r2 supplement](../../numerics/HERMITE_DIRECTIONAL_CAPS_20261024.json),
[source module](../../numerics/hermite_source.py),
[main diagnostic](../../numerics/positive_hermite_diagnostic.py),
[cap comparison](../../numerics/hermite_directional_caps.py),
[exact controls](../../numerics/check_hermite.py),
[control record](../../numerics/HERMITE_CONTROLS.json).
All eleven frozen inputs, script hashes and r2's inherited-r1 hash match.
R1 main runtime 106.444440 seconds, r2 38.597589 seconds; conservative
aggregate numerical debit 160.042 seconds, below the 1800-second limit.
All artifacts remain below 1 MiB; no manuscript, snapshot or commit.

**Disposition:** r1 CLOSED — completed bounded floating diagnostic with
retained source overrun. R2 CLOSED — informative sampled source allowances,
explicit routine remainder proofs, arithmetic/integration unaccepted.
Nodal/transcendental, source-ledger and evaluator rounding, continuous
filter integration, domain/time coverage, endpoint fields/residuals and
joins remain unpaid. HDA-17 Partial; HDA-18 Gated; HDA-20 unchanged.

**Next: Analysis and numerics — Sol.** A later bounded packet should
certify arithmetic and one fixed-point filter integral for the frozen
768 source at the worst observation before widening coverage. Preserve
the 384 storage comparator and r1 overrun. No named extra high difficulty
analytical bottleneck requires Astra here.
