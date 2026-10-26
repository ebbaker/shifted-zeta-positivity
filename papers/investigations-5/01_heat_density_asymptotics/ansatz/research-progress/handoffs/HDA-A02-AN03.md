# HDA-A02-AN03 r1 — evolution-guided negative-time asymptotic correction

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**,
ansatz chat0002, thread 01a17600-b15f-7f52-8713-31fa13599341.

Parent **HDA-A02**. Next owner **Analysis — Sol**. Primary next packet,
prepared, not dispatched. The [sole register](../02_EVOLUTION_ASYMPTOTICS_RESEARCH_PROGRESS_20261025.md)
owns live phase/status. The author asks to use evolution equations and
their errors to understand intermediate negative times, while retaining
all regimes and the regulator transition near64. A03-AN01 stays intact.

## Priority amendment, 25 October 2026

The author now prioritizes controlled asymptotic estimates across all times.
This packet moves from supplementary to **primary next**, while A03-AN01
is retained as deferred supporting work. The frozen mathematical request
below is unchanged. See [Overview02](../../research-overview/02_EVOLUTION_ASYMPTOTICS_RESEARCH_OVERVIEW_20261025.md)
and the current register. Amendment: gpt-6-astra, recorded effort max,
ansatz chat0002. Prepared only; no dispatch.

## Read first

Follow repository AGENTS.md, LARGE_FILES.md, GPT_RESEARCH_MODEL_WORKFLOW.md,
REFERENCE_WORKFLOW.md and tools/CHAT_HISTORY.md. Read:

- [Note08](../../notes/08_EVOLUTION_RESIDUAL_AND_NEGATIVE_TIME_MODES_20261025.md),
  separating its identities from its proposed construction.
- Ansatz Note03 CB8--13; Note04 CS4/CS26--28; Note05 FN5--10 and
  FN20--26; Note06 NB16--24; their assessments and current manuscript.
- Parent Note14 VE4--12, Note31 PE33--39 and Note34 CJ22--27 for actual
  observable equations; Note42 GS7--12 if introducing a spatial cutoff.
- Result summaries11/12 and avoid01/02/05/07/08/12/16. Pin current inputs.

## Frozen bounded analytical request

First work on t=-T, \(1\le T\le2\), sufficiently large X, and the full
fixed charts \(|\Re z-X|\le\ell+2\), \(|\Im z|\le1+h+2\), with an
extra analytic unit. Preserve complete canonical H, H_t=-H_zz, its exact
xi anchor, physical q, fixed K and actual signed observable definitions.
No RH, simplicity or positivity of an unknown remainder may be assumed.

**A. Derive the first useful correction from evolution.** Use the existing
short corrected arithmetic model F_N as baseline. Derive an explicit first
negative-time correction using the product-residual or amplitude/phase
equations in Note08 EV4--6. Match the canonical initial gamma/RS data,
retaining a further RS term if needed. Keep frozen cutoffs, exact adjacent
transfers and all growing mode populations.

Seek a fixed-order explicit formula whose natural gamma-scale field,
spatial j<=3 and first time allowance improves \(C|G|X^{-3/4}\).
The acceptance target is a named \(o(|G|X^{-3/4})\) error;
\(|G|X^{-5/4}\) up to specified logarithms is a work target, not a
promised theorem. Routine algebra, branches, constants and onsets are
delegated to Sol.

An unevaluated full Duhamel correction reconstructs the heat evolution
of the starting data and does not count as simplification. Compare the
new expression with the existing Gaussian-moment/correction-integral
representation. A shorter fixed-order expression may still retain all
N arithmetic modes; fewer modes would be a separate claim.

**B. Interpret the evolving modes at their actual scope.** Recheck EV7--9,
the individual damping \(e^{-Tk_n^2}\), relative weights, cutoff
population and signed total with the correction. Quantify the residual
using the complete population before discarding terms. An absolute shell
bound is not a leading asymptotic for H. The fixed-n
\(T\log^2X\) damping and \(T\log X\) relative-weight scales answer
different questions; neither alone establishes a universal transition.

**C. Prove solution error separately from residual cancellation.** Supply
field, spatial derivatives through three, direct first time error and
actual residual. If Duhamel is used, state function classes, initial and
forcing bounds, complex buffers, localization commutators, full tails and
the carrier-normalized stability estimate. A whole-line supremum
contraction is not an outer-relative chartwise estimate.

Convert the result to the outer envelope. At fixed T a finite algebraic
improvement need not offset \(\exp(T\log^2(X/(4\pi))/16)\). Record the
remaining allowance if that target still fails. Scope the failure to this
method, without claiming impossibility of a short resummed formula.
Record how the new residual enters parent PE37--39; a new physical
transfer theorem is outside this packet, and its first unpaid consumer
should be named.

## Outputs, evidence and stop rule

Analytical only: no sampling, fitting, symbolic execution, exact-arithmetic
campaign or interval runs. Housekeeping is allowed. Do not expand to T>2,
through-zero joins, growing time, the regulator layer or a full observable
campaign without a distinct scope.

Stop after one explicit correction with a proved gain and two-scale
comparison, or at the first precise failed initial, coefficient, population
or stability estimate after a focused attempt. Residual improvement alone
must remain labeled as such. Escalate to Astra only if the named mechanism
remains resistant, with its attempted bound and evidence.

Save mathematics/input manifests in notes/, assessment in reviews/, and
small work records in numerics/, all under ansatz/. Record actual model,
effort and thread. Append return/disposition; update the existing register
and unique chat history. Integrate the manuscript only with assessed
results. Preserve A03-AN01, earlier conclusions and historical requests.
No automatic dispatch, model change or manuscript snapshot.

## Return / disposition

**25 October 2026 — CLOSED at bounded gain/two-scale scope.** Returned by
Analysis — Sol, **gpt-6.1-sol, recorded effort ultra**, ansatz chat0003,
thread `01a17626-abf5-7a90-9ba2-7a2395254aee`.

[Note10](../../notes/10_FIRST_NEGATIVE_TIME_EVOLUTION_CORRECTION_20261025.md)
derives the explicit arithmetic correction
`h exp(T beta²)[1+gamma(T+2T² beta²)]`, matching exact gamma initial
modes, and retains K=1 RS data plus exact adjacent transfers in a bounded
correction integral. On the full fixed charts, 1<=T<=2, field, spatial
j<=3 and direct first time errors improve to **C |G|X^-5/4**, without
log losses; actual residual and its first spatial derivative are
**C |G|X^-7/4**. Canonical initial mismatch, full population and all tails
are paid independently of residual cancellation.

Acceptance is in the **fixed-order Gaussian-moment/retained-RS-integral
class**, not an integral-free elementary correction of every part of F_N.
The evaluated mode correction is not a full unevaluated Duhamel term.
The remaining outer-relative allowance is
`X^-5/4 exp(TL²/16)`, still growing at every fixed T: a failure of this
finite-order allowance, not an actual error lower bound or no-go theorem.
Parent PE37--39 residual forcing is identified; its first unpaid consumer
is a regulator-uniform weak/collar transfer for this model.

[Assessment07](../../reviews/07_FIRST_NEGATIVE_CORRECTION_ASSESSMENT_20261025.md)
records same-model internal analytical acceptance only; the
[work record](../../numerics/AN03_ANALYTICAL_WORK_RECORD_20261025.json)
binds provenance. No numerical/symbolic execution, physical transfer,
onset evaluation, useful cost theorem or specialist review.

HDA-A02 remains **Partial**; parent HDA-17 Partial, HDA-18 Gated and
HDA-20 unfulfilled are unchanged. A03-AN01 is preserved. Next owner
**Analysis — Sol**, [AN04 r1](HDA-A02-AN04.md), assessed-result manuscript
integration, prepared and not dispatched. No resistant mechanism requires
Astra for this routine follow-through.
