# Shifted-zeta research program

These six manuscript folders form one research program built around
Suzuki's shifted screw functions and the associated shifted-zeta canonical
systems. They approach the same structure through time-domain criteria,
inverse spectral theory, the detection of hypothetical spectral defects,
and positivity of finite-window operators. Each paper keeps its own
version, verification record, and release status.

## How the papers fit together

The conceptual starting point is **psi-omega-margin** (Paper 1): it studies
what the shifted screw function says about zero-free half-planes, including
the size of the margin and the length of observation needed to detect a
failure. **Omega-string** (Paper 2) develops the corresponding inverse
spectral family and explains the significance of its RH endpoint.
**Defect-depth** (Paper 3) connects these viewpoints by asking how a
hypothetical off-line zero would become detectable in the time-domain and
spectral descriptions. Its finite Ihara-zeta laboratory supplies a model
in which to investigate those mechanisms.

The operator side starts with **first-slab-positivity**, which studies the
prime-free interval through total horizon `log 2`. **Weil-depth** extends
finite-window positivity certificates through `log 7`, where prime-power
delays enter. **Storage-depth** continues this work past `log 7` using
spatial continuation and residual control. It also records the limitations
of that certificate strategy and a conditional scheme for further depth.
The finite-horizon results do not establish positivity at every length.

Thus there are two useful reading paths:

1. **Concepts and detection:** psi-omega-margin → omega-string → defect-depth.
   Start with the concise Paper 1 if you want a shorter entry point.
2. **Positivity and its limits:** first-slab-positivity → weil-depth → storage-depth.
   Each paper's README and status record describe its results and open review.

These are reading paths, not a claim that every result in a later paper
depends on every earlier one. The manuscripts and their status records
give the actual assumptions and cross-citations.

## Manuscripts and current status

This inventory records the existing stages as of 11 September 2026. The
first-slab preprint is at release stage; no repository release tag or DOI
exists yet. All five other manuscript folders remain working drafts.

| Paper | Role | Current version and status |
|---|---|---|
| [psi-omega-margin](psi-omega-margin/README.md) — Paper 1 | Time-domain margins and quantitative criteria for zero-free half-planes; full paper and concise companion. | Working drafts, 21 and 9 pages; [status](psi-omega-margin/STATUS.md). |
| [omega-string](omega-string/README.md) — Paper 2 | The shifted-zeta inverse spectral family and its RH endpoint. | Working draft v5, 13 pages; [status](omega-string/STATUS.md). |
| [defect-depth](defect-depth/README.md) — Paper 3 | Detection of hypothetical spectral defects, connecting the first two papers; finite Ihara laboratory. | Working draft v1, 15 pages; [status](defect-depth/STATUS.md). |
| [first-slab-positivity](first-slab-positivity/README.md) | Archimedean first-slab positivity, an off-center Weil generator, and a radial energy identity. | Release-stage preprint v1.0, 24 pages; [status](first-slab-positivity/VERIFICATION_STATUS.md). |
| [weil-depth](weil-depth/README.md) | Two-sided finite-window Weil certificates through total horizon `log 7`. | Working draft v0.4, 22 pages; [status](weil-depth/STATUS.md). |
| [storage-depth](storage-depth/README.md) | Residual-controlled spatial continuation of finite-horizon positivity past `log 7`. | Working draft v0.3, 21 pages; [status](storage-depth/STATUS.md). |

## Verification, code, and archives

- [Statement blueprint](../../blueprint/README.md),
  [machine-readable ledger](../../statements/README.md), and
  [verification records](../../verification/README.md): currently centered
  on the first-slab preprint; other papers carry their own status records.
- [Certificate-code release gate](../../code/README.md): the primary
  first-slab Arb certificate bundle is not yet in the public tree.
  Per-paper reproduction scripts remain with their manuscripts.
- [Research notes](../../notes/README.md) and
  [references](../../references/README.md): shared background and provenance.
- [Weil-depth archives](weil-depth/ARCHIVES.md) and
  [storage-depth archives](storage-depth/ARCHIVES.md): locations and hashes
  of large derived data outside git. The `szp-archive` layout is unchanged.

For Weil-depth and storage-depth, current sources are under `manuscript/`,
reproduction code under `numerics/`, and earlier drafts and review records
under `archive/`. Their current package manifests include the documentation
updates made for this move; historical snapshots retain their original bytes.

Build and reproduction commands in a paper's README still run from that
paper's directory. For example, from the repository root the storage-depth
build is now `make -C papers/shifted-zeta/storage-depth`. See the
[all-papers index](../README.md) for citation policy and the release checklist.

## Relationship to the other folders

[SUSY positivity](../susy-positivity/README.md) draws on lessons from this
program but is organized separately around the search for a global positive
factorization. Its ongoing research notes remain in its own background
archive. The earlier [RH detector](../misc/rh-detector/README.md) belongs to
the miscellaneous collection and predates the Suzuki program.

Before this reorganization these six folders lived directly under `papers/`.
When an older manuscript or archived record cites `papers/<slug>/`, its
current location is `papers/shifted-zeta/<slug>/`. Paper slugs, manuscript
versions, and historical commit references retain their meaning.

[All papers and projects](../README.md) · [Repository overview](../../README.md)
