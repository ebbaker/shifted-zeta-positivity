# Working manuscript and reading copy

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 **chat0031**, **Continue CTF-B02 Astra assessment**.

The active [TeX source](radial_deformations_and_zero_dynamics.tex) is
**Conservative Theta Flows and Collision Amplification**. The
[28-page reading copy](../../../output/pdf/radial-theta-collision-geometry/conservative-theta-flows.pdf)
contains the CTF-E05 R2 analytical consolidation: strongest direct
deadline, uniform radial feedback, complete-source theta input,
scoped kernel freedom and the final coupled residual theorem.
Section 8 lists outstanding work; Appendices A--C hold technical
coefficient, preparation and moment arguments.

[Note71](notes/71_ANALYTICAL_MANUSCRIPT_CONSOLIDATION_20261029.md) maps the
new organization and its source proofs.
[Review37](reviews/37_ANALYTICAL_MANUSCRIPT_INTEGRATION_REVIEW_20261029.md)
is a same-assistant editorial check.
[Record27](numerics/27_ANALYTICAL_MANUSCRIPT_BUILD_RECORD_20261029.json)
binds the saved TeX, reading PDF, build log, prior source version and
preservation evidence.

The local latexmk build and the desktop editor compiler both succeed.
The final local log has no warnings, undefined references, or
overfull/underfull boxes. All 28 rendered pages received full-page
visual inspection at 100 dpi; the eight pages affected by the final
copyedit were inspected again. The installed PDF matches the inspected
file. Compilation and visual checks do not validate mathematical proofs.

Open the existing TeX file in Codex for source editing and live preview.
To regenerate the local reading copy from the repository root:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
      -outdir=output/pdf/radial-theta-collision-geometry \
      -jobname=conservative-theta-flows \
      papers/investigations-5/05_radial_theta_collision_geometry/radial_deformations_and_zero_dynamics.tex

The checked integration log is
output/pdf/radial-theta-collision-geometry/ctf-e05-r2-analytical-manuscript.log.
The current reading copy and logs are ignored derived files in the
repository-root output folder. Do not place generated draft PDFs beside
the sources or create manuscript snapshot folders.

The companion [book/main.tex](book/main.tex) is unchanged. Earlier
records21--24 identify their dated source/PDF versions; record24 is the
preceding R5 integration. Their evidence remains preserved. The old main
source matches the existing Git commit identified in record27.
No new commit or tag was created by this revision.

[Continuation72](notes/72_ANALYTICAL_MANUSCRIPT_AND_MODEL_CONTINUATION_20261029.md)
gives research and model-change guidance. The next research decision is
**[B] CTF-B02 — Astra**, with a precise advantage beyond the accepted
direct uniform bound. [Progress05](research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md)
owns live status; [DRAFT_HISTORY.md](DRAFT_HISTORY.md) indexes milestones.
