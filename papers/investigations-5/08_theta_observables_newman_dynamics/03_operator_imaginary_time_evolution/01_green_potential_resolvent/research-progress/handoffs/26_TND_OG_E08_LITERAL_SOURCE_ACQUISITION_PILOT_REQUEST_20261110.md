# TND-OG-E08 r1 — bounded literal-source conditioning pilot

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model/effort are not recorded in
chat0009. **Type E; recommended GPT-6.1 Sol at the author's selected
effort. READY, UNACTIVATED.** The mathematical route, inputs, finite cases
and failure consequences are fixed by B05 r2. No model change or task
dispatch is performed by issuing this request.

Parent: TND-OG-B05 r2. [Note14][note] is the mathematical specification;
[Inputs26](26_TND_OG_E08_INPUTS_20261110.json) freezes it and the inherited
sources. The [sole register][progress] owns live status. This is a
calibration/cost pilot, not a full Green-value or exclusion campaign.

## Question and four fixed cases

Can the Note14 literal-source polynomial and contour scheme acquire
root counts/radii, a regular-factor floor and useful log curvature within
the following finite limits? What does direct exclusion on the same D
cost using precisely the same source and arithmetic?

| Case | Center and domain | Requested conclusion |
| --- | --- | --- |
| Direct comparator | c=30, polynomial error on radius 3/2; D=[29,31]+i[1/2,1] | Strictly zero-free target boundary and integer winding zero, or the exact failed/unresolved gate. No roots need be isolated. |
| Patch 128 | c=113/4; I=[28,57/2] | All Note14 root, floor, lambda and H gates for one of A=1/2,3/4,1. No root count or simplicity is presumed. |
| Patch 132 | c=121/4; I=[30,61/2] | Same. |
| Patch 263 | c=383/4; I=[191/2,96] | Same; this is a fixed high-end conditioning test, not a choice based on measured success. |

The patch indices are zero-based in Note14 (2). Run the direct comparator
first, then the patches in displayed order. A mathematical or resource
failure in one case does not erase its record or authorize substituting
another center. Continue the other cases within their independent caps
unless an analytic defect invalidates the common method.

## Stage A: check the fixed interface before field evaluation

Re-derive Note14 (3)-(9), (14)-(16), the exact rational panel/root
arithmetic, and the direct Rouché comparator. Check all supplied input
identities; distinguish changed history guides from mathematical changes.
The current proof-author check is not an independent assessment.

Required adversarial checks: omitted-root polynomial z(z-1/4), boundary
root z-1, repeated-knot deflation of z^2 and z^2+eta, n=0, approximate
knots that are not roots, and an intentionally understated coefficient
error. The certificate checker must reject missing counts, zero boundary
margin, uncharged errors and non-enclosing intervals. Verify the singular
primitive b=0 limits only if primitive code is introduced; this pilot
does not need that implementation.

One additive elementary correction cycle is allowed, with a separate
note and explicit affected formulas. Do not silently edit the frozen
request or its proof. A structural change to the source, floor argument,
quadrature or target returns to B05 r3 and stops dependent field work.

## Stage B: the fixed provider and acquisition algorithm

1. Keep Newman time zero and the literal reflected theta half-integral.
   Fix N_src=8, V_src=2 and polynomial degree 64. No xi/zeta, RS,
   inherited zero table, provider substitution or complete-census shortcut
   may supply the field, roots or floor. Known verification only labels
   the interpretation as calibration.
2. Use 65 real-centered source coefficient integrals (13) per case.
   Use the degree-15 midpoint Taylor integrator (16), with interval
   order-16 derivatives on each positive-u panel. Start with 32 equal
   panels on [0,2]; dyadic subdivision and reuse of source jets are
   allowed. Track every coefficient radius, including coefficient
   rounding, and evaluate the directed errors (14)-(15) through k=7.
3. Use interval/ball arithmetic at **128, 256, 512 bits**, stopping on
   success or the caps below. Choose exact dyadic polynomial coefficients.
   Coefficient rounding and derivative-bound inflation are paid, not
   guessed from precision. Increasing precision may not reduce the fixed
   truncation/Taylor radius; report that floor when it blocks progress.
4. On each patch test A=1/2,3/4,1 in order, s=A-1/8. Compute complete
   outer winding counts. If n>4 that radius fails this recipe. For n>0,
   use polynomial-root candidates only to propose disjoint dyadic-center
   cluster disks with radii from **2^-24, 2^-32, 2^-40**. Group unresolved
   roots when possible. Each accepted small disk must have a strict
   Rouché margin and a positive integer count; sum counts to the outer
   count and verify strict containment in radius s. No exact individual
   multiplicity or simple-root assumption is required.
5. Certify circles by polynomial arc enclosures and a consistent winding
   calculation. Polynomial translation to a cluster center, interval
   Horner, additional arithmetic guard bits within the selected tier,
   and caching are ordinary implementation choices. Preserve their costs
   and errors. Never replace a failed certificate with sampled arguments.
6. Compute mu0,V0,e0,e1,e2,mu,V,lambda,H and B. The required gates are
   **e0<=mu0/1024, lambda<=32, H<=256**, with root radii<=2^-24 and
   n<=4. Acquire endpoint log|D0| using interval gamma/loggamma and the
   13/128 interpolation payment. D0 is only a known multiplier; gamma
   calls do not authorize a different provider for H0.
7. Form the regular polynomial by synthetic deflation. Enclose it at
   each patch endpoint and midpoint, including any coincident knot.
   Demonstrate that relative evaluation radius <=2^-17 mu can be met,
   or report the failed radius. Charge coefficient growth and arithmetic.
   This checks local factor-evaluation feasibility; do not allocate the
   67584 full-cover integration panels.
8. For c=30 acquire the same polynomial source data, now use A=3/2 for
   its error, and certify the four sides of D with winding zero. Retain
   nonzero boundary margins. It needs no root isolation or Green tail.

## Finite resource limits and accounting

Per case, across all precision tiers, radii and failed attempts:

- **Five minutes of numerical runtime**, including coefficient acquisition,
  candidate computation, contour checking and gamma/factor checks. Four
  cases total at most twenty minutes; code preparation and Stage A are
  separate. Do not restart a timed-out case with a fresh budget.
- At most **4096 live source panels per precision attempt**, dyadic depth
  at most 12 from the 32-panel initial grid, and **32768 source-panel
  evaluations in total**. Recomputations count; a vector evaluation of
  all 65 coefficient integrands is one panel evaluation, and record its
  actual scalar/jet work separately.
- At most **65536 tested contour arcs/segments in total**, including
  rejected tests and rectangle sides, and subdivision depth at most 24.
- At most 100 iterations per polynomial-root candidate solver invocation,
  at most one such invocation per precision tier. Counts, not solver
  convergence, decide acceptance. No general root finder on H0.
- No new package installation is needed if a suitable installed certified
  runtime is available; if absent, report the environment limitation.
  Large traces stay outside Git under LARGE_FILES.md, with a small
  hash-bound record and replay instructions.

Record wall time by coefficient, contour, root, floor and gamma/factor
stage, peak precision, all attempted radii, total source/jet/polynomial
calls, scalar operation counts when instrumentable, and reused input.
Give the direct consumer identical shared setup for the same charge.
Report cold acquisition and warm incremental work separately. Do not
claim a measured speedup from 264 versus one source center or from
extrapolating the three patch times. The full cost ledger is Note14 (18).

## Required return and decision consequences

Return per-case **certified pilot pass**, **specified gate failure**, or
**inconclusive at cap**, with all enclosures and exact integer counts.
Separate proof-assessment status from numerical status. For a gate that
fails, say whether a directed inequality proves failure of this sufficient
recipe or only whether available bounds fail to certify success.

Save code and small execution records in numerics, calculations and scope
in notes, assessment in reviews, and a return in handoffs. Include actual
date, author/LLM provenance, exact model/effort if recorded, input hashes,
runtime and unresolved premises. Refresh the registered chat and arrange
its actual exact-turn final capture using tools/CHAT_HISTORY.md.

- If all patches pass: a local acquisition/cost pilot is complete. A later
  full-cover/integration contract is still required; **do not** automatically
  activate it or infer the other 261 patches pass.
- If direct passes first: record that exclusion on D is already acquired.
  Any subsequent Green value on this D is calibration/observable reuse.
- If a patch fails: identify the exact contour, source, root-matching,
  relative floor or log-range inequality and its measured cost. A changed
  design is **[B] TND-OG-B05 r3 — GPT-6 Astra**, conditional on that return.
- If an implementation cap is inconclusive: preserve partial verified
  data; no higher precision, larger source cutoff, extra center or sweep.

No complete J(30), favorable signed value, new exclusion territory,
uniform-height cost theorem, manuscript revision or successor execution
is requested. Stop at this bounded pilot and its disposition.

[note]: ../../notes/14_TND_OG_B05_R2_CONTOUR_CONDITIONING_AND_COST_20261110.md
[progress]: ../01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md
