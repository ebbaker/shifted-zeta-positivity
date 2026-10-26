# Research progress: large-height heat-density ansätze

> **Superseded for live planning, 25 October 2026.** The author requested
> evolution-driven asymptotic estimates across all times as the top priority.
> The current document is [Evolution Asymptotics Research Progress 20261025](02_EVOLUTION_ASYMPTOTICS_RESEARCH_PROGRESS_20261025.md);
> earlier priorities, phase labels and returns below are historical.
> Updated by gpt-6-astra, recorded effort max, ansatz chat0002.

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
chat0022.

This is the sole live ledger for the **ansatz branch**, created at the
author's request. The [overview](../research-overview/01_HIGH_HEIGHT_ANSATZ_RESEARCH_OVERVIEW_20261025.md)
owns its objective and contracts. The
[parent progress register](../../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
owns parent HDA statuses and unrelated tasks; its entries link here
instead of duplicating the branch queue.

## Current direction

Large height for all real times is now the first priority. Different
formulas are allowed in distinct regimes; complex errors may accompany
simple ansätze. Amplitude, phase, arithmetic corrections and matching
take precedence over central-source optimization.

| ID | Research status | Execution phase / owner | Next deliverable |
| --- | --- | --- | --- |
| HDA-A01 | Complete at bounded AN01--AN02 analytical scope: compact correction and buffered signed crossover; wider program open | CLOSED — Sol, gpt-6.1-sol, ultra, ansatz chat0001; same-model assessment only | [Note04](../notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md), [Assessment03](../reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md), [AN02 return](handoffs/HDA-A01-AN02.md). |
| HDA-A02 | Partial: bounded negative interval [-2,0] proved chartwise; broader compact-negative/short-formula program open | AN01--AN02 CLOSED — Sol, gpt-6.1-sol, ultra, same-model only; supplementary AN03 READY_FOR_SOL — Analysis, Sol, not dispatched | [Note06](../notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md), [Assessment05](../reviews/05_NEGATIVE_BRIDGE_AND_TIME_JOIN_ASSESSMENT_20261025.md), [AN02 return](handoffs/HDA-A02-AN02.md). General compact endpoints remain open. Supplementary [AN03 r1](handoffs/HDA-A02-AN03.md): evolution-guided finite-order correction and natural/outer-scale comparison. |
| HDA-A03 | Partial, inherited coarse layer only | READY_FOR_SOL — Analysis, Sol; prepared, not dispatched | [AN01 r1](handoffs/HDA-A03-AN01.md): corrected one-arm comparison on 63<=t<=65 and named regulator-center shifts at the actual rounding scale. |
| HDA-A04 | Partial, inherited full saddle only | Not dispatched — Analysis, Sol | Joint positive-time/height matching; assess optional Lambert-W replacement. |
| HDA-A05 | Open | Not dispatched — Analysis, Sol | Joint negative-time/height scales and overlap with the Gaussian endpoint. |
| HDA-A06 | Open | Depends on earlier regime results | Domain-union, overlap and complete observable/error theorem. |
| HDA-A07 | Candidate family only | Deprioritized by author — supporting analysis | Gaussian-polynomial core and ancillary models; earlier parent AN09 retained unexecuted. |

Phase labels are not theorem completion statuses. The opening handoff
was executed in ansatz chat0001 with gpt-6.1-sol, actual effort ultra.
Parallel same-model analytical checks were used; no new user-owned chat,
model change, numerical execution or next-packet dispatch was performed.

## Evidence at opening

- [Ansatz Note01](../notes/01_REGIME_BY_REGIME_SOLUTION_ANSATZE_20261025.md):
  complete original family catalogue, including the Gaussian-polynomial
  and Lambert-W candidates.
- [Note02](../notes/02_HIGH_HEIGHT_PRIORITY_AND_DRAFT_SCOPE_20261025.md):
  author priority, normalization checks, arithmetic crossover proposal,
  distinctions among time regimes and source-reading scope.
- [Maintained manuscript](../manuscript/main.tex):
  leading outer calibration, classical t=0 anchor, formal heat-weighted
  sum, exact negative-time identity, regulator layer and remaining models.
- [Reference record](../references/README.md):
  exact primary sections inspected and limits of imports.
- [Production assessment](../reviews/01_OPENING_MANUSCRIPT_PRODUCTION_ASSESSMENT_20261025.md)
  and [build record](../manuscript/BUILD_RECORD_20261025.json):
  compilation/layout and source identity, not independent mathematical
  validation.

## Open boundaries

The parent t>=32 compact-time carrier estimate and the published
0<t<=1/2 input are distinct ranges. The gap, uniform approach to zero,
negative-time continuation, growing cutoffs and full buffered derivatives
are not closed by the opening draft. The parameter t log X is motivated
by fixed arithmetic modes; it is not a proved universal crossover law.
The inherited regulator profile has O(1) absolute error and is not
promoted to higher accuracy or a current/covariance theorem.

Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain. The
parent weak-filter height-cost task is preserved. This branch's first
handoff supersedes the earlier core-first recommendation as the next
task for this author-requested ansatz program.

## Continuation discipline

Read the frozen packet and current inputs before execution. Save new
mathematics in ansatz/notes/, assessments in ansatz/reviews/, and any
authorized code/small work records in ansatz/numerics/. Record actual
model/effort and failed attempts. Update this ledger, the maintained
draft when warranted, and the unique chat history. This conversation
retains parent chat0022; future ansatz-specific chats register in the
ansatz affiliation without moving or duplicating existing histories.


## 25 October continuation — AN01 return

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**, ansatz chat0001. Note03 CB4--13
complete the compact outer calibration on 32<=t<=33, including the true
first correction, buffered spatial jets and direct time derivative.
CB27 proves a corrected real-axis field comparison on |t| log(X/(4pi))<=8.
The correction is retained, the growing mode population and all Gaussian
tails are paid, and a fixed chart cutoff handles threshold crossings.
This is proved-in-note from named imports with same-model assessment only.

CB28 is the exact unpaid complex-buffer remainder. CB29 preserves the
failed absolute real-line Gaussian route. No full signed buffered field,
jet/time, physical covariance or all-real-time theorem is accepted.
Constants/onsets are not numerically instantiated. The next bounded
deliverable is AN02 r1, Analysis — Sol. Parent statuses are unchanged.
The unique current history is in [ansatz/chat-histories](../chat-histories/README.md).


## 25 October continuation — AN02 return

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**, same ansatz chat0001. Note04 CS3
proves CB28 with the exact X^-3/4 exponent, on arbitrary fixed complex
buffers and uniformly across the frozen cutoff. The top-edge Dirichlet
tail and weighted maximum principle avoid an epsilon loss. CS6--7
pay full signed-time buffered field, j<=3 spatial jets and a direct
first time derivative. The unified field allowance is
delta=X^-3/4 exp(t_- L_X^2/16)<=C X^-1/4 for |t|L_X<=8.

Both heat signs use their exact source identities. Frozen tail constants
determine a sufficiently large fixed V_b before the initial charts are
enlarged; the full mode count and all genuine/artificial Gaussian tails
are paid. The actual model residual proves the time bound through zero.
No independent specialist review or numerical onset is supplied.

AN02 and HDA-A01 close at this bounded analytical scope. All-time assembly,
physical transfer and useful cost remain open; parent HDA statuses are
unchanged. Next Analysis — Sol is HDA-A02-AN01 r1, prepared without dispatch.

## 25 October continuation — HDA-A02-AN01 return

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, recorded effort ultra**, ansatz chat0001. [Note05](../notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md)
FN5 proves the existing short arithmetic formula on 1<=T<=2 with
O(|G|X^-3/4) field, spatial j<=3 and direct first time errors. This is
natural gamma-scale control; its failed outer-relative allowance is
preserved in FN10. No correction dominance or actual-H lower bound follows.

FN25--26 supply a distinct finite outer-scale representation with
K=ceil L_X RS terms, J=ceil(3L_X) common gamma-curvature terms and
V=8L_X. All modes and exact cutoff transfers are retained. Its errors
are C E_o exp(-L_X^2/4), with exact model heat residual zero. Growing
Gamma(K/2), all mode curvature and genuine/artificial tails are paid.
The bounded correction integral remains; useful cost is not proved.
[Assessment04](../reviews/04_FIXED_NEGATIVE_TIME_ASSESSMENT_20261025.md)
is same-model only; no numerics, evaluated onset or specialist review.

AN01 closes at its frozen bounded scope; HDA-A02 is Partial. Next
**Analysis — Sol**, [AN02 r1](handoffs/HDA-A02-AN02.md), is prepared,
not dispatched: extend to 4/L_X<=T<=2 with explicit small-T kernel
losses and join to Note04 on 4<=T L_X<=8. The full [-2,0] interval is
a target, not an accepted result. Physical transfer and parent HDA-17
Partial, HDA-18 Gated and HDA-20 unfulfilled are unchanged.

## 25 October continuation — HDA-A02-AN02 return

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, recorded effort ultra**, same ansatz chat0001.
[Note06](../notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md)
NB16--17 extend the unchanged finite Note05 model to 4/L_X<=T<=2,
with field, spatial j<=3 and direct first time errors C E_o exp(-L_X^2/4).
The transverse kernel cost exp(b^2/(4T)), original T^-1/2 normalization,
all inverse-time derivative factors, growing-order constants, exact
cutoff transfers and all tails are paid. No numerical onset is supplied.

NB20--24 join to Note04 on 4<=T L_X<=8 and yield full chartwise
[-2,0] errors: spatial j<=3 at C E_o X^-1/4 Lambda_X^j,
time at C E_o X^-1/4 Lambda_X^2, actual residual at
C E_o X^-1/4 Lambda_X. Only the chi' defect is overlap-supported;
the full residual persists near zero and vanishes for T L_X>=8.
The weighted pointwise estimates are sharper. [Assessment05](../reviews/05_NEGATIVE_BRIDGE_AND_TIME_JOIN_ASSESSMENT_20261025.md)
accepts these results with same-model internal assessment only.

AN02 and the AN01--AN02 bounded negative-time scope close. HDA-A02
remains Partial for general compact endpoints/short formulas; physical
transfer and all-time assembly remain open. The author's requested
[whole-chat summary](../notes/07_CHAT0001_RESEARCH_SUMMARY_20261025.md)
records Notes03--06 and all four packets. Next **Analysis — Sol** is
[HDA-A03-AN01 r1](handoffs/HDA-A03-AN01.md), prepared without dispatch.
No change to parent HDA-17 Partial, HDA-18 Gated or HDA-20 unfulfilled.


## Evolution-equation discussion — 25 October 2026, ansatz chat0002

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, recorded effort max**. The author asks to use the evolution
equations and their errors to understand intermediate negative times,
retaining the regulator transition and all large-height regimes.
[Note08](../notes/08_EVOLUTION_RESIDUAL_AND_NEGATIVE_TIME_MODES_20261025.md)
maps existing residual/observable identities, records the exact forced
error and amplitude/phase equations, and rewrites the short negative-time
model as heat-damped arithmetic modes. This is interpretation and exact
algebra, not a new accepted asymptotic or physical-transfer result.

Supplementary **HDA-A02-AN03 r1 — Analysis, Sol** is prepared, not
dispatched. It seeks one explicit evolution correction with an improved
natural-scale error and an honest outer-scale comparison, or a precise
failed estimate. Existing HDA-A03-AN01 stays prepared and unchanged;
the new packet does not replace its regulator-center work. No automatic
dispatch, numerical execution, model change or manuscript milestone.
HDA-A01's bounded completion, HDA-A02 Partial and parent HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled remain unchanged.
