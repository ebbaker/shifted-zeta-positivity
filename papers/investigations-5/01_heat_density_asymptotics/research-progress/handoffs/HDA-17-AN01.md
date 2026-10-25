# HDA-17-AN01 — instantiate the compact weak budget

**Parent:** HDA-17, supporting HDA-18. **Request revision:** r1.
**Date:** 24 October 2026, America/New_York.
Prepared for **Edward Baker**, with substantial LLM assistance.
**Request model/effort:** gpt-6-astra (Codex), actual effort xhigh, chat 0010.
**Next owner:** GPT-6.1 Sol — routine analysis plus bounded numerical work.
**Phase at handoff:** READY_FOR_SOL; the existing progress register owns
live status. This is a new bounded question, not acceptance or resumption
of the old failed trial under its old scope.

## REQUEST

**Question.** Do Note 34's weak two-order source transfers give a useful
finite-core error budget, or do kernel derivatives, amplitude bounds and
small regulator floors make the older local route preferable? Produce a
small cost/accuracy comparison that decides which transfer and which error
component to refine next. No eventual-onset guess or global assembly is
needed to answer this question. Failure within the budget is a useful return.

Read the repository AGENTS.md, LARGE_FILES.md, tools/CHAT_HISTORY.md and
revised GPT_RESEARCH_MODEL_WORKFLOW.md; the result/avoid indexes; the live
HDA-17 entry; Note 34 CJ3--CJ27 and Review 17; Note 23 LC2--LC13 and its
failed-trial section; Note 20 FB1--FB4; and the existing local-bound script
and record. Existing historical records are reference inputs, not files to
overwrite. The input manifest below pins this request.

### Established contract and delegated routine analysis

Use H_t=-H_zz, the canonical source, unnormalized observables, the exact
common regulator FB1--FB2 with eta=1/2, and K with ell=2,h=1/2.
The proposed finite observation box is D=[-8,8] x [-1/2,1/2]; source/filter
buffer D+=[-10,10] x [-1,1]. This request concerns fixed spatial averages.
It does not declare [64,128] to be an endpoint overlap or a global core.

1. Expand the positive coefficient maps CJ5--CJ14 into an auditable
   implementation and short derivation. Derive the regulator coefficients
   from the exact flat switch, including its endpoints. Sol may complete
   routine algebra, choose conservative scalar caps, and implement local
   envelopes. A local envelope is only a bound when its continuous domain
   is enclosed; sampled envelopes remain diagnostic.
2. Check the identities on F=z, F=z-a(t), and F=z^2-2t, including nonzero
   residual and spatially varying positive q. Sol owns machine-symbolic
   and exact-arithmetic checks. Use a finite set of at most 12 handpicked
   control cases; report what they check, without treating the count as
   theorem evidence. Correct a routine transcription error explicitly
   before using it; freeze an r2 if the mathematical contract changes.
3. Instantiate the source-accuracy columns A,B of CJ20 and the residual
   column C. Report the allowed `(h_1,0+h_2,0)/tau` from CJ27 after other
   budgets, or mark it unpaid. Do not invent endpoint field bounds or
   treat PE6 observable errors as those field bounds.

### Bounded diagnostic

Use the old U_s=1.5, N=4 and 192-cell source only as a baseline. Compare
at most three uniform source meshes: 192,384,768 cells. If the arithmetic
mode tail dominates, one N=8 comparison is permitted within the same work
cap; source cutoff remains fixed. Retain LC2's interpolation, omitted-mode,
complete-tail and nodal-arithmetic contributions for source orders 0,2.
Include orders 1,3 only for the old pointwise comparison or evaluator needs.

The observation set is exactly t in {64,96,128}, x in {0,4}, y in {0,1/2}
(12 observations). For t=64 compare the weak route with all overlapping
LC7--LC11 quantities on the same source data. At t=96,128 include the full
adaptive weak rows, both curvature derivatives and signed source. Do not
reuse the old pre-switch B/source simplifications there.

At each observation retain scalar-buffer and, if useful, amplitude-aware
positive-convolution diagnostic allowances. Use at most three filter
orders per direction, 16,32,64. The source/evaluator quadrature or stable
local series may use at most two refinement levels selected by Sol. Use
80 decimal digits initially when high precision is needed; a single
120-digit check at each of at most two worst cases is allowed. Stable
logarithmic/internal scaling is allowed if all physical offsets, q and
time terms are restored and the error ledger tracks it. Do not repeat the
known unstable bare error-function subtraction as a proposed evaluator.

Thresholds are predeclared to compare costs, not to certify the samples:
for U,W,R,C,J,U_t,W_t,R_t,C_t,averaged B and actual averaged source S,
use 1e-4 at order zero and `1e-4 max(1,L_alpha)` for their listed spatial
derivatives. For Q use 1e-3 at order zero and
`1e-2 max(1,L_alpha)` at orders one and two, with a separate 1e-2 target
for Delta Q. These are a new diagnostic contract, not a change to Note 23.
Use CJ21's 80/10/10 allocation and report each category even when unresolved.
Nodal arithmetic in the source ledger is distinct from later evaluation
arithmetic. Never call an unproved candidate rounding allowance certified.

**Evidence standard:** floating diagnostic is sufficient for this request.
A continuous enclosure is welcome only if attainable within the same
budget; label its exact box and arithmetic. Samples/refinement agreement
alone do not prove the D box or the interval between times. Report retained
rounding/filter uncertainty and do not count underflow as a zero tail.

**Work limit and stopping:** at most the cases/refinements above and 30
minutes aggregate numerical execution. Stop earlier once the transfer
choice and dominant obstacle are clear. If scalar bounds are hopeless,
try one local-envelope comparison before stopping; no large mesh/sweep is
required. If source/rounding/filter gates fail, preserve the failure and
state the cheapest bounded next change. Escalate only a specific extra
high difficulty analytical issue; ordinary algebra, implementation or
moderate estimates stay with Sol. No full gamma saddle/onset computation,
new root search, regulator change, global splice or arbitrary precision
escalation is in scope.

### Outputs and allowed writes

- A new research note in notes/ with the next unused number, containing
  the routine derivation, input interpretation and decision.
- A new clearly named script and small JSON record in numerics/; keep
  every file below 1 MiB and large regenerable arrays outside Git.
- An assessment in reviews/ stating model/reviewer scope accurately.
- Append this packet's RETURN and DISPOSITION, update its live ledger row,
  and capture only this Sol chat under its own identity in chat-histories/.
- Update current README links where needed. Do not modify the manuscript,
  prior numerical records, historical request, or another chat's transcript.

For each reported error distinguish source interpolation, omitted modes,
complete tail, nodal arithmetic, evaluator arithmetic/truncation and filter
integration. Record actual runtime/environment and hashes. Give max
allowance/target ratios, bottleneck rows and failed cases; no big table of
samples without a decision. Sol may close this bounded request with its
own justified disposition. HDA-17 remains unaccepted unless a continuous
full contract has actually been paid; HDA-18's spatial join remains open.

**Author's pasteable prompt:**

> Continue HDA-17-AN01 r1 using the revised Sol-first workflow. Derive the
> remaining routine coefficients and run the bounded weak-transfer versus
> local-transfer diagnostic. Keep failures and all error categories, save
> notes/progress/history, and record your own disposition. Escalate only a
> specifically identified extra high difficulty analytical bottleneck.

## Input manifest

Filled at handoff with Git HEAD and SHA-256 of the exact working-tree
inputs. These hashes identify inputs; they do not validate their claims.

Git HEAD at handoff: `db79f03d5b2c5017c05c614ea6fee7ec3dfdeb0e`. The following working-tree hashes
are authoritative for this request (the live ledger/history are not frozen):

| Input, relative to repository root | SHA-256 |
| --- | --- |
| `GPT_RESEARCH_MODEL_WORKFLOW.md` | `38baa14d26c6d48a76dbe7da60c07dd798f3fe02d92a6cb243decf52ba120711` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/34_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_20261024.md` | `daeefac6d0b47602d84312e547878612f8a97526cfa8a01a080829c9a571fc2f` |
| `papers/investigations-5/01_heat_density_asymptotics/reviews/17_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_SELF_REVIEW_20261024.md` | `e42f763f0409103944b5e2d341d3d12b44198163df050a2517e0bb0cc70ce550` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md` | `5f478ed088e2f77f8818edadfd36b0d9b56ff4174539df86a332b181813e3152` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/23_FINITE_TRANSITION_CONTRACT_AND_LOCAL_BOUNDS_20261024.md` | `30a1ff1b59c2b74893f55230930c8795609186ca2be06a8bc2e5872090bc368d` |
| `papers/investigations-5/01_heat_density_asymptotics/notes/31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md` | `c0973ef063f07d356b93a8af446d823fcc800f638212547c7d98c52f77ed4acd` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/finite_transition_local_bounds.py` | `c57bc853da8f9eabaf3808c2df9932c4895e2ace105216635e23b7adf53e30f3` |
| `papers/investigations-5/01_heat_density_asymptotics/numerics/FINITE_TRANSITION_LOCAL_BOUNDS_20261024.json` | `783cc38041895b1512cddf6c4841b5ff00f9d1c45cc8b9979a2301c49e23db55` |


## RETURN — Sol

Pending. Record actual model/effort, date, chat identity, request revision,
input matches or deviations, evidence paths, failed cases, runtime and
remaining errors. Do not overwrite the request above.

## DISPOSITION — named owner

Pending. Sol may accept a bounded input, retain a diagnostic/scoped failure,
or specify the next tractable task. An Astra return is not automatic.


## RETURN — Sol, completed 24 October 2026

**Actual model/effort:** gpt-6.1-sol (Codex), ultra, verified from session
metadata. **Chat:** 0011, `01a170a3-5f6e-7aa2-9e33-bcae4835c782`.
**Request:** r1 unchanged. All eight frozen input hashes match; HEAD remains
`db79f03d5b2c5017c05c614ea6fee7ec3dfdeb0e`. The original pending placeholders
above are superseded by this appended return and disposition.

[Note 35](../../notes/35_WEAK_TRANSFER_BUDGET_DECISION_20261024.md) supplies
flat-switch/endpoints, explicit positive coefficient triples, the A/B/C
accuracy table interpretation and unpaid CJ27 ratio. Twelve selected exact
rational differential controls pass, including residual, varying positive
q and a double event. The nonzero residuals have E_z=0; no arbitrary-jet
or theta certificate is implied. No mathematical contract correction.

[Diagnostic code](../../numerics/weak_transfer_diagnostic.py),
[coefficient maps](../../numerics/weak_coefficients.py),
[exact controls](../../numerics/exact_controls.py), and the
[small index record](../../numerics/WEAK_TRANSFER_DIAGNOSTIC_20261024.json)
retain all requested observations, meshes 192/384/768, filter 16/32/64 and
source-rule 6/10 levels. The index hashes three per-time records, each below
1 MiB. It records actual environment, input/code hashes and all six error
categories. Logarithmic complete tails remain positive. No N=8 run was
needed. The retained numerical execution is 53.7824 seconds; exact controls
rerun in 0.313443 seconds. A conservative 240-second debit for interrupted
implementation work/small checks keeps aggregate numerical execution
below five minutes, within the 30-minute limit.

**Result:** weak transfer helps some density/time rows near peaks, but is
not a uniformly better whole-norm choice. The fair 192-cell t64 worst local
source allowance/(80% target) is 6.20380e6, versus weak 1.41932e7; covariance
is limiting. An alternate tight frozen 768-cap comparison at an existing
point retains local's advantage on covariance/source. Across all times the
largest weak ratio is 1.97354e11, scalar 2.43698e12. Source interpolation
is dominant; omitted modes/cutoff are negligible. Actual filter refinement
has maximum change/(10% target) 5275.90 for Delta Q at t=96,x=4,y=1/2,768 cells;
positive-allowance filter integration is independently unresolved. Nodal
candidate ratio 0.106694 is sampled, not certified. Later evaluator changes
are small but rounding/truncation remains unpaid. No continuous D box or
interval between times is enclosed.

Two implementation errors were corrected before retention: factor 4 in
the Lambert-W argument and the shared scalar cap's +3 error requirement.
Interrupted outputs were discarded and corrections/budget debit retained.
The mathematical request/source/regulator/targets did not change.
[Review 18](../../reviews/18_WEAK_TRANSFER_BUDGET_ASSESSMENT_20261024.md)
includes a separate same-model subagent audit, not specialist independence.

## DISPOSITION — Sol, 24 October 2026

**AN01 r1 CLOSED — completed bounded floating diagnostic with retained
failure.** No source/filter/rounding acceptance or positive CJ27 cutoff
allowance is claimed. Endpoint field errors and residuals remain unpaid;
PE6 observable errors are not substituted. HDA-17 remains Partial, HDA-18
Gated, HDA-20 unchanged. The manuscript and prior records/request text are
unchanged. This chat alone is captured under its unique history identity.

**Next owner: Analysis and numerics — Sol.** Improve interpolation and
peak-sensitive positive/filter integration at the existing bad points,
retain componentwise weak gains, and derive the direct adaptive local
signed-source transfer before a broader switch-time diagnostic. No extra
high difficulty escalation is needed for that deliverable. Spatial
compatibility remains a separate open issue.
