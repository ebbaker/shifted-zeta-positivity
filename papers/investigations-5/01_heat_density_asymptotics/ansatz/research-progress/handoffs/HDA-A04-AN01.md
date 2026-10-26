# HDA-A04-AN01 r1 — first corrected large positive time saddle

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
recurrence chat0007, thread 01a178d3-5b84-7a81-9cbe-2210fd235c35.

Parent HDA-A04. **Next owner: Analysis — Sol. READY_FOR_SOL; prepared only,
not dispatched or executed.** [Progress03][ledger] owns live status. [Overview03][overview] defines
the program. This routing update leaves the r1 mathematical request unchanged.
The author explicitly puts understanding large positive time before
bridging the two regimes and requires independence from RH.

## Inputs and conventions

Read repository AGENTS, model/reference/history/storage guidance, the
result/avoid indexes and controls12. Pin actual source versions and
model/effort before execution. Read parent Notes30--31 and their assessments,
the current ansatz overview/register, and the [discussion][discussion].
Read the Polymath v2 equation 35 normalization and DLMF 2.4(iv) with their
recorded hypotheses. The discussion is formal input to check, not a proved
remainder or independent review.

Keep H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8 and the complete canonical source.
For each arm w=(1+iz)/2 or (1-iz)/2, retain the selected branch
p=w+(t/2)alpha(p), B=1-(t/2)alpha'(p), and
S_t(w)=M(p)exp(-(p-w)^2/t)/sqrt(B) from Note30.
Use X=|x|, R=2+t+X, Lcal=log R, Ncal=1+X+t Lcal.
The target is eventual t>=t_* with t_*>=32 and **all real x**, on each
declared fixed strip with the full fixed analytic buffers.

**Do not assume RH, all-real zeros at time zero, or a value of Lambda.**
Audit imported arguments for those dependencies. Exact xi reflection and
the ordinary Dirichlet series in its convergence half-plane are available
unconditionally. No root data or target density may be used to fit a
carrier. Preserve q and K if mentioned, but physical transfer is outside
this packet.

## Bounded request

1. Check the formal coefficient recurrence P6--P7 in the discussion and
   derive the first correction independently:
   C2=t^2 alpha'''(p)/(32B^2)
      +5t^3 alpha''(p)^2/(192B^3).
   Correct routine algebra explicitly if needed. Define
   P2=sum_w S_t(w)(1+C2(t,w)); do not call it an exact heat solution.
2. Prove a complete amplitude-envelope field bound for H-P2 on the
   stated eventual large-t domain, uniform over x. Start with Note30's
   full canonical convolution and both reflected arms. Pay the local
   remainder, noncentral saddle region, complete omitted arithmetic,
   both connectors, middle, infinite tails and moving endpoints.
   Show the achieved rate improves the existing
   t^(3/2)/Ncal^2 bound as t tends to infinity uniformly over x.
3. A candidate, not an accepted theorem, is a local remainder
   e4=t^3/Ncal^5+t^4/Ncal^6+t^5/Ncal^7+t^6/Ncal^8,
   plus explicitly retained arithmetic and contour budgets of the
   kind in Note30 FS20. Prove it, correct it with a supported rate,
   or identify its first failed estimate. Explain whether the gain
   uses odd-moment cancellation and why that cancellation is justified
   on the actual contour, including all noncentral pieces.
4. Pay spatial derivatives through3 on fixed enlarged buffers and a
   direct first-time comparison; compute/bound the actual residual
   P2_t+P2_zz. Give the actual derivative rates and sufficient-onset
   dependence. No differentiated uncontrolled big-O or arbitrary-data
   backward-heat contraction is permitted.
5. Explain the dominant correction/error in the time-dominated,
   comparable and height-dominated balances of X and t log R. State
   separately the fixed-x limit and all-x uniform conclusion. Identify
   what would be needed for later fixed higher orders; do not start an
   all-orders or growing-order campaign within this packet.

## Acceptance, limits and record

One corrected model with a fully paid improved large-t field/jet/time
budget and residual, or a precisely documented failed estimate after a
focused attempt. Distinguish proof at symbolic sufficient onset from
an instantiated numerical onset. A smaller residual alone is not a field
comparison. If only part closes, record that exact scope.

**Analytical only:** no numerical, machine-symbolic, exact-arithmetic or
sampling campaign. Routine derivations, contour bookkeeping and source
checks are delegated to Sol. Stop at the first resistant estimate rather
than broadening the domain or silently changing the source. Escalate to
Astra only a specifically identified extra-hard obstacle with the failed
route and unpaid term.

Do not bridge toward zero, execute A08-AN01 or R05-AN08, refine the 64
switch, prove an RH criterion, or claim all-time assembly in this packet.
Their existing frozen requests/results remain intact. No new manuscript
snapshot. Save mathematics in ansatz notes/, assessment in reviews/,
append this RETURN/DISPOSITION, update the sole ledger and overview, and
refresh the affiliated research chat using its unique registration.

> Execute HDA-A04-AN01 r1. Establish the first corrected full gamma-saddle
> hierarchy as t tends to positive infinity, uniformly in real height,
> without assuming RH. Pay the complete source, arithmetic, contours,
> buffered derivatives and actual residual. Stop at the bounded improved
> estimate or its precise obstruction; leave bridging for later.

## RETURN / DISPOSITION

**26 October 2026 — AN01 r1 CLOSED at bounded requested scope.** Prepared
for Edward Baker with substantial LLM assistance, **gpt-6.1-sol (Codex),
recorded effort ultra**, ansatz chat0005, thread
`01a178fa-8a72-7f23-9a7f-47e284eab9a3`. The header's prepared-only wording
records the original request; this return and Progress03 supersede it
for live execution status. No mathematical request revision was needed.

[Note17](../../notes/17_FIRST_CORRECTED_LARGE_POSITIVE_TIME_20261026.md)
proves the stated C2 and proposed e4 scale, paying complete xi/reflection,
all omitted ordinary Dirichlet arithmetic, both connectors, middle and
infinite tails. Odd moments cancel on an actual symmetric central contour
segment; finite Gaussian-polynomial tails and genuine noncentral pieces
are paid separately. The final field bound is a complete amplitude-envelope
comparison, not a residual-only result.

At symbolic sufficient t_* and all real x, normalized field error is
O(t^-2 log^-5 t), spatial j<=3 error O(t^-2 log^(j-5)t), direct first-time
O(t^-2 log^-3 t), and actual nonzero residual O(t^-3 log^-5 t). Note17
LT26/LT28 give the exact residual. LT12–13 pay a sufficient larger
arithmetic floor explicitly; the old t>=32 absorption alone would not
pay X^-5. No numerical onset is instantiated. The full three-part budget
is retained on the joint t>=32, sufficiently-large-R domain.

[Assessment12](../../reviews/12_FIRST_CORRECTED_LARGE_POSITIVE_TIME_ASSESSMENT_20261026.md)
accepts this as **proved in-note from named inputs; same-model internal
assessment only**. [Input record](../../notes/17_FIRST_CORRECTED_POSITIVE_TIME_INPUTS_20261026.json)
pins read working-tree bytes and HEAD. No RH, initial all-real zeros,
Lambda value, root fitting, numerical/symbolic campaign, physical transfer,
bridge, higher-order execution or manuscript snapshot was used or supplied.

LT-01 audited; LT-02 complete. Broad HDA-A04 remains Partial. **Next
owner: Analysis — Sol**, prepare the bounded LT-03 fixed-order request
with finite constants, arithmetic floor, buffers and residual specified.
No resistant estimate requiring Astra arose. Regional bridges remain
for later stages.

[ledger]: ../03_LARGE_POSITIVE_TIME_HIERARCHY_RESEARCH_PROGRESS_20261026.md
[overview]: ../../research-overview/03_LARGE_POSITIVE_TIME_HIERARCHY_RESEARCH_OVERVIEW_20261026.md
[discussion]: ../../../recurrence/brainstorm/03_POSITIVE_TIME_HIERARCHIES_AND_BRIDGES_20261026.md
