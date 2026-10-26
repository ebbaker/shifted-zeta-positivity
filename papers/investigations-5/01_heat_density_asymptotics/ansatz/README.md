# Large-height heat-density ansätze

25 October 2026. Prepared for **Edward Baker** with substantial LLM
assistance, **gpt-6-astra (Codex), actual effort max**.

This branch develops simple analytical field and density formulas with
accurate large-height asymptotics across real heat time. Different
regimes and complicated error estimates are allowed.

- [Maintained manuscript source](manuscript/main.tex)
- [Generated reading PDF](../../../../output/pdf/heat_density_ansatz/heat_density_ansatz.pdf)
- [Research overview](research-overview/01_HIGH_HEIGHT_ANSATZ_RESEARCH_OVERVIEW_20261025.md)
- [Research progress](research-progress/01_HIGH_HEIGHT_ANSATZ_RESEARCH_PROGRESS_20261025.md)
- [Next-chat handoff: HDA-A03-AN01 r1](research-progress/handoffs/HDA-A03-AN01.md)
- [Whole-chat research summary](notes/07_CHAT0001_RESEARCH_SUMMARY_20261025.md)
- [Negative bridge and time join](notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md)
- [Bridge and time-join assessment](reviews/05_NEGATIVE_BRIDGE_AND_TIME_JOIN_ASSESSMENT_20261025.md)
- [Fixed negative-time representations](notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md)
- [Fixed negative-time assessment](reviews/04_FIXED_NEGATIVE_TIME_ASSESSMENT_20261025.md)
- [Complex remainder and full buffered crossover](notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md)
- [Buffered crossover assessment](reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md)
- [Corrected carrier and signed real-axis bridge](notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md)
- [Internal assessment](reviews/02_CALIBRATION_AND_REAL_BRIDGE_ASSESSMENT_20261025.md)
- [Ansatz chat histories](chat-histories/README.md)
- [Original ansatz catalogue](notes/01_REGIME_BY_REGIME_SOLUTION_ANSATZE_20261025.md)
- [High-height priority and draft scope](notes/02_HIGH_HEIGHT_PRIORITY_AND_DRAFT_SCOPE_20261025.md)
- [Primary references and inspection scope](references/README.md)
- [Draft history](DRAFT_HISTORY.md)

The PDF is a local generated reading copy and may need rebuilding in a
fresh checkout. Follow [the build guide](manuscript/README.md).
The draft distinguishes inherited results, exact anchors, candidate
formulas and open uniform estimates; it is not a new all-time theorem.

Next owner: **Analysis — Sol**. Pasteable prompt:

> Continue HDA-A03-AN01 r1 and its live progress entry. Prove a corrected
> one-arm comparison on 63<=t<=65 and quantify the named regulator-center
> changes using the exact physical sensitivity and rounding scale. Keep
> the analytical-only limits and stop at any precise unpaid consumer.

Chat0022 retains its unique parent-investigation history; it is not
re-registered here. New ansatz-specific conversations should use this
branch's affiliation when registering their own histories.


Continuation, 25 October: gpt-6.1-sol, actual effort ultra, ansatz chat0001.
The first compact outer correction and signed real-axis bridge were
proved-in-note with same-model assessment at AN01. The complex-buffer
and time gaps recorded at that stage are closed by Note04 below;
physical transfer remains open.


AN02 continuation, 25 October: Note04 closes the complex-buffer gap
without epsilon loss and pays signed spatial jets and direct time error
through zero. HDA-A01 closes only at this bounded analytical scope;
all-real-time coverage and physical transfer remain open.

HDA-A02-AN01 continuation, 25 October: **gpt-6.1-sol, recorded effort ultra**.
Note05 closes the bounded 1<=T<=2 packet at two separate scales: a short
gamma-scale formula and a larger finite outer-scale representation,
with buffered field/jet/time errors. HDA-A02 remains Partial; next AN02
is the bridge toward zero, prepared without dispatch. Review is same-model.

HDA-A02-AN02 continuation, 25 October: **gpt-6.1-sol, recorded effort ultra**.
Note06 pays the shrinking-to-fixed bridge and full chartwise negative
interval [-2,0], including all kernel/derivative/join defects. Note07
summarizes this chat's complete four-packet progress. Both A02 packets
close at bounded scope; broader A02 remains Partial. Next A03 packet
is prepared without dispatch; review remains same-model only.
