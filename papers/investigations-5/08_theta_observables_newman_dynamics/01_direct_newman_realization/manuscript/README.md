# Conditional Newman dynamics: analytical manuscript

6 November 2026. Drafted for **Edward Baker** with substantial LLM assistance, **gpt-6-astra / max**, direct-branch chat0003. Task **TND-D-E05**.

[main.tex](main.tex) is the single evolving manuscript. The [reading PDF](../../../../../output/pdf/08_theta_observables_newman_dynamics/direct_newman_realization/conditional_newman_dynamics.pdf) is generated under the repository's ignored `output/pdf/` directory. The initial build has 18 pages. Future revisions should edit these sources and record notable milestones in [DRAFT_HISTORY.md](../DRAFT_HISTORY.md), without creating snapshot folders.

The [parent manuscript](../../manuscript/main.tex) supplies the common background. This paper develops the direct branch systematically, from the complete preparation and count instrument to the absolute readout, count-sector calculus, local collisions, exact colliding control and outstanding tasks. All mathematical results are derived analytically; no numerical experiment is used.

| Manuscript source | Development and principal inputs |
| --- | --- |
| [Introduction](sections/01_introduction.tex) | Question, main identities, assumptions and separate evidence levels |
| [Preparation](sections/02_preparation.tex) | Concise cylinder/Green background; complete theta bounds, square-root recurrence and full energy moments from [E01 Note02](../notes/02_TND_D_E01_R1_CONDITIONAL_QUADRATURE_REALIZATION_20261106.md) |
| [Instrument](sections/03_instrument.tex) | Bounded signed Kraus operations, complete count sum, aggregation, conjugated domains and no-count strong law from E01 |
| [Observation](sections/04_observation.tex) | Conditional source, success calibration and density-cosine readout from E01; covariance and state motion from [Collision Note04](../notes/04_TND_D_B02_COLLISION_DYNAMICS_RECONNAISSANCE_20261106.md) |
| [Count calculus](sections/05_count_calculus.tex) | Signed moments, generating identity, transfer laws from Note04; a locally derived all-count kernel consequence of the same instrument |
| [Collisions](sections/06_collisions.tex) | Double-event balances and fold, singular root tracking, observation variance, source sectors and higher-order heat polynomial from Note04 |
| [Control](sections/07_control.tex) | Exact reflected colliding witness, its own admissible square-root domains and the premise-by-premise limitation |
| [Outstanding tasks](sections/08_outstanding.tex) | Source-specific mechanism discovery, bounded analytical consequences, multiplicities/ranges, supplied physical access and later assessment |

The realization retains its existing [internal E02 assessment](../reviews/01_TND_D_E02_CONDITIONAL_REALIZATION_ASSESSMENT_20261106.md). Later collision/count diagnostics retain proof-author status. The [integration check](../reviews/02_TND_D_E05_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261106.md) checks this synthesis and production; it is not independent specialist review. B02's mechanism/target choice remains open, and E03 remains unissued.

## Rebuild

From the repository root, with TeX Live's `latexmk`, `pdflatex`, BibTeX and `plainurl.bst` available:

```sh
bash papers/investigations-5/08_theta_observables_newman_dynamics/01_direct_newman_realization/manuscript/build.sh
```

[build.sh](build.sh) combines the branch manuscript, parent internal, canonical MC11 and branch measurement bibliographies in the ignored build directory, then resolves citations and cross-references with `latexmk`. The canonical bibliography files remain at their existing homes. A generated combined bibliography and build intermediates do not belong in the manuscript source folder.

[BUILD_RECORD.json](BUILD_RECORD.json) identifies the source files, bibliography inputs and PDF checked for this milestone. The [source-use record](../references/02_TND_D_E05_MANUSCRIPT_SOURCE_USE_20261106.md) distinguishes fresh primary passage checks from inherited assessments. The [input record](../research-progress/handoffs/06_TND_D_E05_MANUSCRIPT_INPUTS_20261106.json), [return](../research-progress/handoffs/06_TND_D_E05_MANUSCRIPT_RETURN_20261106.json) and [sole progress register](../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md) preserve task provenance.
