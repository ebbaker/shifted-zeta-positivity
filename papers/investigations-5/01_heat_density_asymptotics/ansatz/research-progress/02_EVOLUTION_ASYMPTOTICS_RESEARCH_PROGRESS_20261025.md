# Research progress: evolution-driven asymptotics across time

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Ansatz chat0002, thread `01a17600-b15f-7f52-8713-31fa13599341`.

**Sole live ansatz ledger.** This supersedes
[Progress01](01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md) for
current priorities and execution phases; its historical returns remain
intact. [Overview02](../research-overview/02_EVOLUTION_ASYMPTOTICS_RESEARCH_OVERVIEW_20261025.md)
owns the current objective and acceptance contract. The
[parent register](../../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
continues to own parent HDA statuses and the separate source-cost queue.

## Current disposition

The author prioritizes **understanding and bounding the large-height
asymptotics for all times**, using the evolution equations with explicit
error terms. The immediate next deliverable is a negative-time evolution
correction and proved improvement. Compact positive-time coverage and
joint positive/negative time-height limits have the same primary research
priority. Fine t=64 analysis remains important supporting work.

| ID | Research status | Execution phase / owner | Next bounded output or dependency |
| --- | --- | --- | --- |
| HDA-A01 | Complete only at AN01--AN02 bounded analytical scope | CLOSED; Sol, gpt-6.1-sol, ultra, chat0001; same-model assessment | Preserve Notes03--04. No all-time or physical-transfer completion is inferred. |
| HDA-A02 | Partial: chartwise [-2,0] and two accuracy scales proved in-note; general compact-negative and shorter outer-scale formulas open | **READY_FOR_SOL — Analysis, Sol; primary next**, AN03 r1 prepared, not dispatched. AN01--AN02 closed. | [AN03](handoffs/HDA-A02-AN03.md): one explicit evolution correction on 1<=T<=2 with a proved natural-scale gain, actual residual and outer-scale conversion, or a precise failed estimate. |
| HDA-A08 | Open: compact positive-time coverage and uniform joining | Primary field-estimate queue; Analysis, Sol; no new frozen packet yet | Pay 1/2<t<32 and declared compact-time overlaps with the signed crossover and parent t>=32 input. Derive field/jet/time/residual bounds from canonical data. |
| HDA-A04 | Partial: inherited full gamma saddle | Primary joint-limit queue; Analysis, Sol; not dispatched | Establish useful uniform time-height ranges and matching. Lambert-W simplification is optional supporting work, not the acceptance condition. |
| HDA-A05 | Open: joint negative-time/height asymptotics | Primary joint-limit queue; Analysis, Sol; not dispatched | Identify and bound the overlap between compact-negative arithmetic evolution and the large-T Gaussian endpoint. |
| HDA-A06 | Open: physical transfer and full assembly for these ansatze | Follows usable estimates on each domain; Analysis, Sol; not dispatched | Transfer field and residual bounds to actual physical observables; pay regulator/covariance and all joining defects, then prove the domain union. |
| HDA-A03 | Partial: inherited coarse regulator layer | **DEFERRED_SUPPORTING**; Analysis, Sol; AN01 r1 remains prepared, not dispatched | [AN01](handoffs/HDA-A03-AN01.md): corrected named one-arm comparisons on 63<=t<=65 and center shifts at the rounding scale. Mathematical scope unchanged. |
| HDA-A07 | Candidate family only | Deprioritized supporting analysis | Gaussian-polynomial core and ancillary central models; earlier parent core packet remains unexecuted. |

HDA-A08 is a new ownership entry for an already documented gap, not a
newly discovered obstruction or a result. Priority labels rank work;
phase labels do not certify mathematics. Work has not been dispatched.

## Accepted evidence carried forward

| Completed packet | Result and error scope | Source / assessment |
| --- | --- | --- |
| HDA-A01-AN01 | Corrected carrier on [32,33], field and spatial j<=3 at E_o (1+log^(4+j)X)/X², first time at E_o (1+log^6X)/X²; corrected signed real-axis crossover. | [Note03](../notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md), [Assessment02](../reviews/02_CALIBRATION_AND_REAL_BRIDGE_ASSESSMENT_20261025.md) |
| HDA-A01-AN02 | Fixed-cutoff complex remainder and signed full-buffer crossover, delta=X^-3/4 exp(t_- L²/16)<=C X^-1/4 on \(\lvert t\rvert L\le8\); spatial and direct time bounds. | [Note04](../notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md), [Assessment03](../reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md) |
| HDA-A02-AN01 | Short gamma-scale allowance C abs(G) X^-3/4 on 1<=T<=2; separate finite outer-scale model at C E_o exp(-L²/4), j<=3 and first time, exactly zero model heat residual on frozen charts. | [Note05](../notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md), [Assessment04](../reviews/04_FIXED_NEGATIVE_TIME_ASSESSMENT_20261025.md) |
| HDA-A02-AN02 | Extension to 4/L<=T<=2, paying complex-kernel and inverse-time costs; full chartwise [-2,0] join with j<=3 at C E_o X^-1/4 Lambda^j, time at C E_o X^-1/4 Lambda², residual at C E_o X^-1/4 Lambda. | [Note06](../notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md), [Assessment05](../reviews/05_NEGATIVE_BRIDGE_AND_TIME_JOIN_ASSESSMENT_20261025.md) |

L=log(X/(4pi)), Lambda=1+L. The last row's uniform allowances are
weaker than its pointwise weighted bounds. Its actual residual persists
near zero and vanishes for TL>=8; only the derivative-of-cutoff part is
overlap-supported. All four outputs retain **proved in-note from named
inputs, same-model internal assessment only**. No numerical onset, useful
cost theorem, independent review or full physical transfer was supplied.
[Note07](../notes/07_CHAT0001_RESEARCH_SUMMARY_20261025.md) is the detailed
whole-round summary; the frozen packets and returns remain historical.

## This reply: integration and reprioritization

[Note08](../notes/08_EVOLUTION_RESIDUAL_AND_NEGATIVE_TIME_MODES_20261025.md)
provided exact forced-error, amplitude/phase and observable equations,
and the exact heat-damped rewriting of the short negative-time model.
It is source-based synthesis, not a new accepted asymptotic theorem.

The [maintained manuscript](../manuscript/main.tex) is now organized
around those identities, canonical initial matching, separate residual
and solution error, and regime-dependent stability. It retains the
previous bounded theorem statements and gives an explicit all-time
coverage map. [Note09](../notes/09_EVOLUTION_MANUSCRIPT_AND_PRIORITY_REVISION_20261025.md)
and [Assessment06](../reviews/06_EVOLUTION_MANUSCRIPT_REWRITE_ASSESSMENT_20261025.md)
record the integration and its limits. The current
[build record](../manuscript/BUILD_RECORD_20261025_EVOLUTION_REWRITE.json)
records production checks only.

Queue change authorized by the author's latest instruction: A02-AN03
moves from supplementary to primary next; A03-AN01 moves from next to
deferred supporting. Both frozen mathematical requests remain intact,
with dated navigation/priority notices. The older overview and register
are explicitly superseded, not erased or silently rewritten.

## Acceptance and open boundaries

For A02-AN03 the next quantitative target is a named o(|G|X^-3/4)
field/jet/time allowance on 1<=T<=2. |G|X^-5/4 times stated logarithms
is only a proposed work target. Retain all modes, the correction and
canonical initial error. A smaller residual alone does not establish
this target. Conversion to the outer envelope must show the remaining
exp(T L²/16) loss. The packet may close with a precisely scoped failed
estimate after a focused attempt; it must not report an actual error
lower bound or a universal impossibility from an inadequate allowance.

The wider first-priority boundary comprises arbitrary compact-negative
intervals, the missing intermediate positive range, uniform overlaps,
joint positive and negative limits, and useful bounds with time/height
dependence. The subsequent consumer boundary comprises physical transfer,
spatial assembly, the fine regulator center/rounding law, and useful cost.

No new bound, numerical computation, independent specialist review,
RH/noncollision/simplicity result, or parent-status promotion is recorded
by this rewrite. Parent **HDA-17 Partial, HDA-18 Gated and HDA-20
unfulfilled** remain. Consult the [result index](../../../../../result-summaries/README.md),
[heat-flow cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
the [avoid index](../../../../../avoid/README.md), especially
[separate bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status discipline19](../../../../../avoid/19_status_files_that_lag_the_findings.md).
The overview records the explicit control-premise screening.

## Handoff and history

Next owner: **Analysis — Sol**, [HDA-A02-AN03 r1](handoffs/HDA-A02-AN03.md).

> Continue HDA-A02-AN03 r1 under Overview02 and Progress02. Derive one
> explicit negative-time evolution correction on 1<=T<=2 and prove an
> improved natural-scale field/jet/time error, with its actual residual
> and honest outer-scale conversion. Retain all arithmetic modes and
> canonical initial corrections; stop at the first precise unpaid estimate.

Manual handoff only. Execution should pin current inputs, record actual
model/effort and failed routes, update this register and save the return
in the existing packet. Request a new bounded scope before expanding the
packet to other times or a numerical campaign.

The [ansatz histories](../chat-histories/README.md) contain chat0001 for
the four completed packets and chat0002 for this review, evolution
discussion and rewrite. Their identities, hashes, counts, provenance and
public-source prefixes are checked in the
[verification record](../chat-histories/VERIFICATION_20261025_EVOLUTION_REWRITE.json).
Parent chat0022 retains its unique parent registration. The current
reply's unsent final text is captured by the bounded exact-turn follow-up,
not manufactured in advance; later refreshes legitimately change hashes.
