# Analytical working manuscript

25 October 2026, America/New_York. Drafted for **Edward Baker** with
substantial LLM assistance. Current consolidation/production:
**gpt-6-astra, actual effort max**, chat 0016. Original notes retain their
actual Astra/Sol model and effort attribution.

The one maintained [source](main.tex) now consolidates **Notes 42–45** in
addition to the preceding analytical results and scoped Note 38 outlook.
The checked reading copy is **92 pages**. [Note 46](../notes/46_NOTES42_45_MANUSCRIPT_CONSOLIDATION_20261025.md)
maps the integration; [Review 28](../reviews/28_NOTES42_45_CONSOLIDATION_PRODUCTION_ASSESSMENT_20261025.md)
records production and source-consistency checks.

Section 13 gives the gap-supported nonholomorphic field, exact equations,
full-support primitive/observable transfer, actual covariance, paid exterior
heat partition and shrinking-slab error. Section 14 gives finite gap/core
inputs, the constructive clipped-positive source and the effective complete
complex-buffer outer field/jet proof. The introduction, model guide, scope,
source crosswalk and acknowledgments reflect these additions.

The goal is an analytic approximation for every real height and heat time,
with useful quantitative errors, full buffers and control at |x|→infinity
and t→±infinity. The current fixed-gap theorem covers all heights on a
short time slab; fixed-width time coverage, useful full budgets, the switch
and endpoint joins remain open. HDA-17 is Partial, HDA-18 Gated and HDA-20
unfulfilled. Production is not independent specialist review.

## Build and reading copy

Run from the repository root:

~~~sh
python3 -B papers/investigations-5/01_heat_density_asymptotics/manuscript/build.py
~~~

The unchanged script exports to [the local reading copy](../../../../output/pdf/heat_density_asymptotics/heat_density_asymptotics.pdf).
Auxiliaries stay in that ignored folder's `.build/`. The
[current build record](BUILD_RECORD_20261025.json) pins all 20 TeX files,
build.py and the PDF: zero warnings, 56 resolving local links, 629 resolving
internal actions, all-page rendering and visual inspection, and selected
readable-page checks. No numerical research was run.

The [historical 24 October build record](BUILD_RECORD_20261024.json) is
preserved unchanged, including its 78-, 65-, 54-, 28- and 25-page provenance.
MI2 remains CLOSED at its original production scope; [Note 41](../notes/41_NOTE39_MANUSCRIPT_IMPLEMENTATION_20261024.md)
and [Review 22](../reviews/22_NOTE39_ANALYTICAL_INTEGRATION_PRODUCTION_ASSESSMENT_20261024.md)
record that milestone. No new snapshot folder or commit is created.

The [sole progress register](../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
owns live status. **Next: Analysis — Sol**, [HDA-18-AN04 r1](../research-progress/handoffs/HDA-18-AN04.md),
for remaining exterior constants and one complete budget. HDA-22/23 then
target fixed-width time coverage and core conditioning; HDA-24 is gated
switch-uniform assembly before parent HDA-18's two endpoint joins.
