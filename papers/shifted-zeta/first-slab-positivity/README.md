# Archimedean first-slab positivity for shifted zeta canonical systems

**An off-center Weil generator and a radial energy identity**

Edward Baker — preprint, version 1.0, 5 September 2026.

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
<!-- Add the actual Zenodo concept-DOI badge after deposit. -->

## What this is

A computer-assisted positivity result for the prime-free first slab (depth
`L ≤ log 2`) of Suzuki's shifted zeta Hankel system. For every shift
`0 < ω ≤ 1/2` and every `0 < L ≤ log 2`, the finite-section Hankel operator
`H_{ω,L}` satisfies `‖H_{ω,L}‖ < 1`, i.e. `I ± H_{ω,L} ≻ 0`. The proof combines

- an exact decomposition of the shift generator, `Q_{ω,L} = Q_{0,L} + C_{ω,L}`,
  where `Q_{0,L}` is the classical compact-window Weil form and `C_{ω,L}` is a
  compact integral operator with an explicit kernel;
- an Arb-certified interval computation (512 parity–shift boxes, 16 Legendre
  modes per sector) closed by analytic tail bounds, giving
  `Q_{ω,L} ⪰ 6.1159·10⁻⁴ · I` on the logarithmic form domain;
- a shift-energy identity `I − V*V = 2∫₀^ω V_s* Q_s V_s ds` that turns
  generator positivity into strict contractivity.

The result is prime-free and finite-depth. It proves neither the Riemann
hypothesis nor a new zero-free region; see Section 1.5 of the paper.

## Contents of this repository

| File | Purpose |
|---|---|
| `first_slab_positivity.pdf` | The preprint (24 pages). |
| `first_slab_positivity.tex` | LaTeX source (single file, `pdflatex`; no external bibliography). |
| `VERIFICATION_STATUS.md` | What has been independently checked, by what means, and what has not. Mirrors Section 13 of the paper. |
| `CITATION.cff`, `.zenodo.json` | Citation and Zenodo deposit metadata. |
| `LICENSE.md` | CC BY 4.0 notice for this folder; licensing by material type is in `../../../LICENSE`. |

The certificate and audit scripts (Investigations 7, 12, 13, 14 in the paper's
Appendix B) are **not** part of this deposit. They are available from the
author on request, and a separate code release with pinned environments and
archived logs is planned once the repository items listed in
`VERIFICATION_STATUS.md` are complete.

## Disclosure

This manuscript reports computer-assisted mathematics and was prepared with
substantial language-model assistance. The author is responsible for its
content. It has been through two adversarial referee-style review rounds with
independent numerical recomputation of every reported constant and one
clean-room reimplementation of the certificate; it has **not** yet had
line-by-line human verification of the central analytic steps. The deposit
fixes a citable version of the argument while that verification proceeds.
Please read `VERIFICATION_STATUS.md` before relying on any statement.

## Building the PDF

```bash
latexmk -pdf first_slab_positivity.tex
```

Requires a standard TeX Live with `amsmath`, `amsthm`, `mathtools`,
`booktabs`, `enumitem`, `hyperref`, `microtype`, `xcolor`, `url`.

## How to cite

This folder is part of the single repository *shifted-zeta-positivity*
(<https://github.com/ebbaker/shifted-zeta-positivity>). No release has been
tagged and no DOI exists yet. Until then, cite the folder at the commit you
read (hash from `git rev-parse HEAD` or the folder's GitHub permalink):

> E. Baker, *Archimedean first-slab positivity for shifted zeta canonical
> systems: an off-center Weil generator and a radial energy identity*,
> preprint v1.0, 2026, in: *shifted-zeta-positivity*,
> <https://github.com/ebbaker/shifted-zeta-positivity>, folder
> `papers/shifted-zeta/first-slab-positivity/`, commit ⟨hash⟩.

After the first release, cite instead the **version** DOI of the release that
contains the version you read together with the folder path, or the paper's
own Zenodo record (deposited with this folder's `.zenodo.json` as metadata and
linked to the repository record). The DOIs will appear in this file and in
`CITATION.cff` (`preferred-citation.doi`) when they exist; the manuscript
version and the repository release version are separate identifiers.

`CITATION.cff` in this folder carries the same data; the statement inventory
with per-statement verification status is `../../../blueprint/first-slab/statements.md`.

## Contact

Edward Baker — edwardbaker86@gmail.com

[Shifted-zeta program](../README.md) · [All manuscripts](../../README.md)
