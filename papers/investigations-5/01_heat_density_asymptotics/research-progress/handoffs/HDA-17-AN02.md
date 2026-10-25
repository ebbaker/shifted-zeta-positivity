# HDA-17-AN02 — sharper source allowances and peak integration

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
chat 0011, thread `01a170a3-5f6e-7aa2-9e33-bcae4835c782`.
**Parent:** HDA-17; supports HDA-18. **Request revision:** r1.
The user authorized continuation of analysis and numerics after AN01's
closed diagnostic. This is a new bounded packet; AN01 r1 is unchanged.
The progress register owns live phase/status.

## REQUEST

**Question:** Do tighter complete-source curvature/weight bounds and a
composite peak-sensitive filter resolve the dominant AN01 costs enough
to choose the next finite-source or integration change?

Read Notes 20,23,34,35, Review 18, the AN01 records and current repository
instructions/indexes. Retain H_t=-H_zz, canonical theta source, eta=1/2,
physical global q, unnormalized observables, ell=2,h=1/2, D/D+ and AN01
component targets and 80/10/10 allocation. No regulator or target change.

1. Derive a sharper continuous complete-source |Phi''| cell cap, integrated
   LC2 interpolation/nodal weights, and source contributions. Keep the
   original LC4 estimate as comparator. A continuous formula evaluated in
   floating arithmetic is not a rounding enclosure.
2. Derive direct adaptive local signed-source envelopes with r_t,r_x
   varying on the buffer, including a signed radial coefficient comparison.
   At most six exact local controls may test the new formulas; identity
   controls do not certify a source, filter or whole box.
3. Source budgets only: fixed cutoff 1.5,N=4, uniform 192/384/768 cells at t64;
   permit one 768-cell adaptive mesh chosen from an a priori positive
   curvature/weight envelope, without field zeros or a root search.
4. Field/filter comparisons: only existing t=64,x=4,y=0 and y1/2 centers,
   uniform 192 and 768 sources, plus the one adaptive 768 source. Source-cell
   Gaussian orders 8/12. Reuse the AN01 tensor 64 result where the field is
   identical; an adaptive-source tensor 64 comparison is permitted.
5. Composite filter: fixed normalized panel boundaries from quarter points
   and kernel derivative zeros through order 4; Gaussian orders 8/12 per
   panel. The rule is selected from the kernel and q/peak-scale diagnosis,
   not by a new field-root search. Retain both actual-observable and positive
   error-envelope changes and direct-vs-weak identity differences.
6. No switch-time field expansion unless the t64 source/filter gates are
   informative; otherwise retain the general adaptive source formula and
   defer numerical switch-time application. No all-height/onset computation,
   spatial splice, new source cutoff, mode sweep or precision escalation.

**Evidence:** floating diagnostic sufficient. Preserve separate source
interpolation, omitted modes, positive complete tail, nodal candidate,
later evaluator and filter categories. Integrated convex-chord weights may
supply an analytic integration upper formula, but all floating arithmetic
must remain explicitly unpaid. Samples/refinement differences are not
continuous remainder estimates.

**Budget:** 30 minutes aggregate numerical execution; stop once a method
choice or failed source/integration gate is clear. No generic large sweep.
Use 80 digits where needed; no new 120-digit checks are planned. If source
bounds still dominate after local integration, identify the cheapest
bounded source representation change rather than increasing mesh count.

**Outputs:** next numbered note, new scripts and small JSON records,
internal assessment, appended RETURN/DISPOSITION, update HDA-17 row and
current README/history links. Preserve manuscript, all prior notes/records,
AN01 request and other chat transcripts. All files below 1 MiB; no large
arrays in Git. Sol may close the diagnostic with justified disposition.

## Frozen inputs

| Input relative to repository root | SHA-256 |
| --- | --- |
| `GPT_RESEARCH_MODEL_WORKFLOW.md` | `38baa14d26c6d48a76dbe7da60c07dd798f3fe02d92a6cb243decf52ba120711` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md` | `5f478ed088e2f77f8818edadfd36b0d9b56ff4174539df86a332b181813e3152` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/23_FINITE_TRANSITION_CONTRACT_AND_LOCAL_BOUNDS_20261024.md` | `30a1ff1b59c2b74893f55230930c8795609186ca2be06a8bc2e5872090bc368d` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/34_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_20261024.md` | `daeefac6d0b47602d84312e547878612f8a97526cfa8a01a080829c9a571fc2f` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/35_WEAK_TRANSFER_BUDGET_DECISION_20261024.md` | `483abb63d9d55aede850fafab91b11a049d91c14041147d43db101f09993203e` |
| `papers/investigations-5/01_heat_density_asymptotics/reviews/18_WEAK_TRANSFER_BUDGET_ASSESSMENT_20261024.md` | `a37578fba2330408ff69962d7650d55f48c852764c15872b58a9b930fb0e81a5` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/weak_transfer_diagnostic.py` | `a4e704384c9766a72f6b643db0997eac7fb2ff0d82c54da78f8727ff11c204e2` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/weak_coefficients.py` | `1ab138c89ce7a7083a1970c70edc8211cf486218e072d342774c781b5cb4a27d` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/WEAK_TRANSFER_DIAGNOSTIC_20261024.json` | `e633391059639c7238c77842cf8d87b46b0af49a84cfc3744e8c16029e2cb6f0` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/WEAK_TRANSFER_DIAGNOSTIC_20261024_T64.json` | `97a08bec1e4e9a9ee8eff739a33645ca992452f36aa6889ba68ee04f12a6b904` |

## RETURN — Sol

Pending.

## DISPOSITION — Sol

Pending.


## RETURN — Sol, 24 October 2026

**Actual model/effort:** gpt-6.1-sol (Codex), ultra, verified from session
metadata; chat 0011, thread `01a170a3-5f6e-7aa2-9e33-bcae4835c782`.
**Revision:** r1 unchanged. All ten frozen inputs match. Original pending
placeholders above are superseded by this appended return/disposition.

[Note 36](../../notes/36_SOURCE_CURVATURE_AND_PEAK_INTEGRATION_20261024.md)
proves continuous signed-cubic Bernstein and midpoint/Phi^(3) source caps,
positive convex-chord LC2 weights, and direct adaptive signed-source and
companion curvature/time envelopes. Six exact selected controls pass,
including nonzero E_z and source-transfer inequalities. The formulas do
not certify floating arithmetic or theta accuracy.

[Source code](../../numerics/source_accuracy_improvements.py),
[diagnostic](../../numerics/source_peak_diagnostic.py),
[controls](../../numerics/check_source.py) and
[record](../../numerics/SOURCE_PEAK_DIAGNOSTIC_20261024.json) retain every
source category, positive tail logarithm, full local row, cap-attribution
comparison, source/filter indicators, work count, runtime and hashes.
Source cutoff 1.5,N=4, uniform 192/384/768 budget tables and one source-only
adaptive 768 mesh respect the request. Field observations are only the six
allowed t=64,x=4,y=0 or 1/2 cases. Composite Gaussian 8/12 uses 16384/36864
points; source Gaussian 8/12 is separate. No t=96 field computation or
additional precision escalation was performed.

The order-zero interpolation allowance improves 24.37 times from old
uniform 768 to adaptive 768. The latter's interpolation allowances for
orders 0--3 are [1.04980e-4,4.23706e-5,1.92557e-5,9.34631e-6].
At adaptive 768,y=0 the Delta Q allowance is 16.4538 against 0.008, ratio 2056.73;
at y=1/2 it is 4.90773, ratio 613.466. This remains the scale-setting source
failure. Actual filter indicators are below allocation: maximum weak
ratio 0.00320013 and selected direct ratio 0.786370. The adaptive positive
filter indicator is 1.01162 at y=0, still slightly unpaid, versus 0.069752
at y=1/2. No refinement indicator is an integration enclosure.

New source-ledger arithmetic, the nodal candidate and all later rounding
remain unpaid. Weak-only source-rule indicators do not pay the direct
four-jet evaluator. Complete numerical local maps are t=64/pre-switch only;
the adaptive source/companion formulas are analytical inputs, not a full
switch-time implementation. Full-map guards/scope labels and work/direct
metrics were added after calculation without changing executed t=64
arithmetic; both executed/delivered main-source hashes are retained.

Main execution 132.472860 seconds, exact controls 0.385188 seconds,
conservative aggregate debit 142.473 seconds, within 30 minutes. All
artifacts below 1 MiB, no large arrays stored. [Review 19](../../reviews/19_SOURCE_CURVATURE_AND_PEAK_ASSESSMENT_20261024.md)
includes a separate same-model subagent audit; no independent specialist
review, manuscript edit, old-record replacement, commit or snapshot.

## DISPOSITION — Sol, 24 October 2026

**AN02 r1 CLOSED — completed bounded floating diagnostic with retained
failure; routine continuous bounds proved in-note.** Source interpolation
is now the main obstacle at the sampled points. Retain the tighter source
bounds, source-only mesh and composite filter. HDA-17 remains Partial,
HDA-18 Gated and HDA-20 unchanged. Continuous D/time coverage, rounding,
filter remainders, endpoint field/residual data and CJ27 joins remain unpaid.

**Next: Analysis and numerics — Sol.** Freeze a bounded positive
cubic-Hermite source comparison with complete fourth-derivative remainder,
canonical nodal values/derivatives and linear fallback when Bernstein
positivity is unavailable. Compare fixed cost at the same t=64 points,
preserve all source/arithmetic categories and reuse composite integration.
No broad switch-time or mesh expansion, and no Astra escalation, is
warranted for this tractable next deliverable.
