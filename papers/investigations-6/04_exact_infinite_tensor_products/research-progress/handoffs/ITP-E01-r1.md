# ITP-E01 r1 — weighted full-line refinement with exact cell phase

13 November 2026, America/New_York. Intended author **Edward Baker**;
substantial OpenAI Codex assistance. Request author tool selection:
**gpt-6-astra / ultra**; independent backend metadata unavailable.
Type **E**, execution selected **gpt-6.1-sol / ultra**: the architecture,
norm, observation, proof route and numerical target are now fixed.

Frozen request, parent ITP-B01. Do not overwrite with a return. Live
status owner: [ITP register](../01_INFINITE_PRODUCTS_RESEARCH_PROGRESS_20261113.md).
Verify the exact prerequisite hashes in
[input manifest](../../numerics/01_ITP_E01_R1_INPUT_MANIFEST_20261113.json).
Changed inputs must be reported, not silently substituted. Status/history
files are deliberately excluded from this frozen manifest.

Read the [decision](../../brainstorm/notes/01_ITP_B01_EXACT_CELL_PHASE_DECISION_20261113.md)
and [fixed mathematical specification](../../notes/01_ITP_B01_FIXED_TRANSFER_TARGET_20261113.md),
the branch plan/overview/reference guide, inherited Brainstorm 02 §§5–8,
self-check, source chapter and root workflows. The specification fixes
all equations and normalizations; no favorable rank or signed margin is
assumed. Existing controls are applied analytically, not numerically rerun.

## Task and acceptance

Derive the weighted L1 cell-average estimate, its exact sinc readout, and
full-line/finite-cutoff transfer on 0<=lambda<=1/2, x in R, |y|<=8.
Prove uniform prepared-amplitude convergence and the exact local ratio
telescoping connection without asserting a global operator-norm product.
Use h=2^-L, complete-source masses on cells [jh,(j+1)h), Fourier factor
1/2 and reverse clock tau=1/2-lambda.

Target: V_8<=868 and, at U=2,L=30,

    sup |H_lambda(z)-A_(L,U)(lambda,z)|
      <= h exp(8h)V_8/4 + T_8(U) <= 10^-6.

Derive the proposed elementary complete-source bounds, tail constant and
all quantifiers. Prove the center-point phase baseline's fixed-L all-real-
height error floor Z_lambda/2, while direct integration of the selected
piecewise-constant density has exactly the selected network's value.
This comparison does not establish a speed advantage.

Success is the theorem with explicit constants and the complete target
allowance, correctly scoped aliasing comparison, and all arithmetic/time
qualifications. A precise failed allowance or invalid frozen premise is
also a completed return. Bounds are allowances, not measured errors.

## Finite scope and correction

One analytical derivation and at most one bounded correction pass. If the
first tuple fails because of a routine constant issue, allow U<=3,L<=34
on the same strip and time range. No new architecture, normalization,
weighted norm, source or observation. Algebra, compatible gauge notation,
and elementary estimates with their hypotheses are routine. The proof
route is cell double integrals, the inherited derivative envelope,
elementary exponential inequalities and exact phase integration.

No numerical campaign, cell-mass computation, dense array, rank fitting,
TT-SVD or benchmark. At most ten scalar diagnostic evaluations may be
recorded if needed, but theorem inequalities require proof or outward
rounding; diagnostic values are not certification. No source PDF or
large regenerated data is to enter the repository.

Record exact-source and arithmetic errors as zero only for the ideal
mathematical construction. Give the specified optional computed mass and
readout error budgets without claiming achievement. Keep time projection
distinct from exact finite-level time evolution: P_h does not commute with
u^2. Keep growing gate support and coefficient-acquisition cost visible.
No uniform lower source floor, rank bound, gamma-normalized error,
relative error near zeros or Green-log estimate may be inferred.

Check each catalog control's actual shared/missing premises as in the
decision. Smooth colliding densities can satisfy the theorem, so no
failed approximation premise is manufactured. Atomic controls fail the
density hypothesis, and changed kernels fail the literal readout. Any
negative result retains the specified point-phase lattice class.

If a new arithmetic theorem, topology, domain or scientific consumer is
required, record the precise missing premise and return to ITP-B01.
Do not silently change the request to secure a favorable result.

## Outputs and continuation

Own only branch04. Save derivation in notes, a concise return in handoffs,
only necessary small records in numerics, and update the sole register and
DRAFT_HISTORY. Do not edit parent/shared files or capture chats. Preserve
this request and its inputs. Record actual tool-selected model/effort
separately from unavailable backend metadata, errors and deviations.
Completed E01 makes the already declared ITP-E02 assessment ready on Sol
6.1 / Ultra: one report, with at most one bounded response check, assessing
the complete request/return without changing its consumer or premises.
