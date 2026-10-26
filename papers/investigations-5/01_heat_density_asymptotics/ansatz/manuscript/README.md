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
[BUILD_RECORD_20261025_EVOLUTION_REWRITE.json](BUILD_RECORD_20261025_EVOLUTION_REWRITE.json).
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
