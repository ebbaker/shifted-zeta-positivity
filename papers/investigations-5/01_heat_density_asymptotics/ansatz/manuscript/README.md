# Maintained ansatz manuscript

25 October 2026. Prepared for **Edward Baker** with substantial LLM
assistance, **gpt-6-astra (Codex), recorded effort max**, ansatz chat0002.

[main.tex](main.tex) is the editable maintained draft. The current
rewrite organizes large-height asymptotics around error evolution,
amplitude/phase corrections, canonical arithmetic initial data and
regime-dependent stability. It retains the bounded results in Notes03--06
and treats the fine t=64 regulator transition as supporting work.

Open this folder in the Codex LaTeX editor for source and live preview.
To generate the portable local reading copy, run from the repository:

    python3 papers/investigations-5/01_heat_density_asymptotics/ansatz/manuscript/build.py

The [reading PDF](../../../../../output/pdf/heat_density_ansatz/heat_density_ansatz.pdf)
and intermediate files belong in the ignored root output/pdf tree under
LARGE_FILES.md. The build uses latexmk and the standard packages in
main.tex. Generated working PDFs do not belong in this source directory.

Current production identity:
[BUILD_RECORD_20261025_A02_AN06.json](BUILD_RECORD_20261025_A02_AN06.json).
AN06 integrates Note12/Review09 in Section6.4, Proposition6.2 and explicit
endpoint/onset Appendix A. For every declared fixed 0<tau<=T<=B, field,
spatial j<=3 and first-time errors are C(tau,B,r,b)|G|X^-5/4, and actual
residual/residual_z is C(tau,B,r,b)|G|X^-7/4. All modes, K=1 RS data,
exact transfer and bounded integral remain. Constants degenerate at zero
or infinite time; outer allowances still grow at fixed T.

The 33-page build has no warnings; all pages were rendered and inspected,
and all 85 inherited math blocks remain verbatim. [Note13](../notes/13_AN06_MANUSCRIPT_INTEGRATION_20261025.md)
and [Assessment10](../reviews/10_AN06_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261025.md)
record scope and checks; [Note14](../notes/14_CHAT0003_RESEARCH_SUMMARY_20261025.md)
is the whole-chat next-session summary. Integration: gpt-6.1-sol, effort
ultra, chat0003, for Edward Baker with substantial LLM assistance.
The [AN04 build record](BUILD_RECORD_20261025_A02_AN04.json) is historical:
Section6.3/Proposition6.1 remains unchanged at its [1,2] scope.

The [evolution rewrite record](BUILD_RECORD_20261025_EVOLUTION_REWRITE.json)
is historical.
See [Note09](../notes/09_EVOLUTION_MANUSCRIPT_AND_PRIORITY_REVISION_20261025.md)
and [Assessment06](../reviews/06_EVOLUTION_MANUSCRIPT_REWRITE_ASSESSMENT_20261025.md)
for scope and checks. Compilation, layout inspection and hashes establish
production quality and identity, not mathematical validity.

Earlier build records remain historical: the opening draft, A01-AN01,
A01-AN02, A02-AN01 and
[A02-AN02](BUILD_RECORD_20261025_A02_AN02.json). The
[draft history](../DRAFT_HISTORY.md) links the corresponding notes and
assessments. Maintain the source in place; future milestones may point
to commits/tags without creating snapshot folders.

The current [overview](../research-overview/02_EVOLUTION_ASYMPTOTICS_RESEARCH_OVERVIEW_20261025.md)
and [progress register](../research-progress/02_EVOLUTION_ASYMPTOTICS_RESEARCH_PROGRESS_20261025.md)
govern the next work. The rewrite is synthesis and reprioritization;
the previous theorem and review statuses are unchanged.

The original [1,2] correction, older stronger growing-order theorem and
through-zero join keep their scopes. The new fixed compact family does
not extend those joins or transfer to physical observables. Same-model
internal analytical assessment only; a successful build does not validate
a proof. Next prepared work is [A08-AN01](../research-progress/handoffs/HDA-A08-AN01.md)
on [1/2,1], not an executed positive-time extension.
