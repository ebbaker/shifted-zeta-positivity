# Hamiltonian heat evolution of theta amplitudes

One evolving manuscript, drafted for **Edward Baker**, 6 November 2026.
Prepared with substantial assistance from **gpt-6-astra (Codex), actual
recorded effort max**. Task **[E] TND-A-E05**; this is an analytical
synthesis of the branch's accepted conditional response, using the
parent manuscript as background. No snapshot folder is created.

## Reading and rebuilding

- Editable entry: [main.tex](main.tex).
- Local reading copy: [Hamiltonian auxiliary dynamics PDF](../../../../../output/pdf/08_theta_observables_newman_dynamics/02_hamiltonian_auxiliary_dynamics/hamiltonian_auxiliary_dynamics.pdf).
- Build and identity record: [BUILD_RECORD.json](BUILD_RECORD.json).
- Mathematical and production checks: [Review02](../reviews/02_TND_A_E05_MANUSCRIPT_PRODUCTION_REVIEW_20261106.md).
- Source-use record: [Source-use05](../references/05_TND_A_E05_MANUSCRIPT_SOURCE_USE_20261106.md).
- Integration note: [Note03](../notes/03_TND_A_E05_ANALYTICAL_MANUSCRIPT_SYNTHESIS_20261106.md).

From the repository root, with a TeX distribution providing `latexmk`,
pdfLaTeX, BibTeX, and the packages used in `main.tex` on `PATH`:

```sh
bash papers/investigations-5/08_theta_observables_newman_dynamics/02_hamiltonian_auxiliary_dynamics/manuscript/build.sh
```

The script writes the PDF, temporary bibliography, and all build products
only to repository-root `output/pdf/08_theta_observables_newman_dynamics/02_hamiltonian_auxiliary_dynamics/`.
That location is ignored by Git. No generated PDF belongs in this
manuscript folder, regardless of size; see [LARGE_FILES.md, rule 8](../../../../../LARGE_FILES.md).
The PDF's identity is recorded separately from the editable-source list
in `BUILD_RECORD.json`; it is not a file to commit. Byte identity across
different TeX distributions or build times is not asserted.

## Development and evidence boundary

The manuscript derives, in order, the complete cylinder spectrum, Green
weight, theta source and normalization, prepared graph identities,
weighted heat evolution, calibrated response and mixed derivatives,
then zero preservation, conjugated dynamics, and inverse attenuation.
It ends with outstanding tasks. No numerical premise is used.

The principal proof is [E01 Note01](../notes/01_TND_A_E01_R1_COMPLETE_SPECTRUM_RESPONSE_20261106.md),
accepted within its supplied-apparatus scope by [E02 Review01](../reviews/01_TND_A_E02_REALIZATION_ASSESSMENT_20261106.md).
Shared geometry and source inputs retain the parent assessment's scope.
The [parent manuscript](../../manuscript/main.tex) is background; its
direct-instrument development is not imported as an auxiliary theorem.
The new exposition of the Mellin normalization is an elementary local
derivation of the inherited absolute factor, not a new zeta theorem.

[B02 Decision02](../brainstorm/notes/02_TND_A_B02_FIRST_JET_CONDITIONING_DECISION_20261106.md)
and the [E03 frozen request](../research-progress/handoffs/07_TND_A_E03_R1_FROZEN_REQUEST_20261106.md)
are described as pending work. The first-jet map is an immediate
derivative of the established response; sharp recovery constants are
not asserted as completed. E03 and E04 retain their previous status.
Review02 is a local editorial and production check by the manuscript
authoring model, not independent specialist review or formal verification.

Current routing remains in the [sole branch progress register](../research-progress/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_PROGRESS_20261105.md).
Notable manuscript milestones belong in [DRAFT_HISTORY.md](../DRAFT_HISTORY.md).
