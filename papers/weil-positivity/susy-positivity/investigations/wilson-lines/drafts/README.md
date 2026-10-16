# Preserved draft snapshots

Each directory is a complete, standalone package: the TeX sources, the PDF, the
build guide, the check program and its record, `BUILD_RECORD.json` pinning the
reviewed source/PDF pair, and `SNAPSHOT.json` pinning the saved files.
`validation/drafts.py save` refuses to overwrite an existing snapshot, and a
snapshot carries its own copy of the tool so it can be verified in isolation.

| Snapshot | Version | Reviewed | Contents |
|---|---|---|---|
| `2026-09-17-v01` | 0.1 | 17 September 2026 | First draft, 18 pages: the causal generator written out and its three factors identified with the three terms of the target, the invisibility of the pole term on the imaginary axis, the abelian obstruction, the shift as a hyperbolic rotation, the endpoint variation and its flatness and trace obstruction, the primes as the atoms of the connection, and three proposed necessary conditions. |
| `2026-09-17-v02` | 0.2 | 17 September 2026 | 29 pages. Adds the all-pass identification and its four consequences (group delay, resonance, the flux identity, and the reason the shift flow is abelian); the contraction region, the graded criterion and the disproof reading; the zero-placement precision behind the generator boundary and the positive-real reading of the Cayley coordinate; the explicit endpoint algebra and the linkage of the two remaining problems; and revised conditions, including the bilinear-endpoint form and the conformality/scale trade. Checks grow from 70 to 206 cases. |

| `2026-09-17-v03` | 0.3 | 17 September 2026 | 30 pages. Corrects Section 9.4: the transformation that destroys the prime atoms is dilation in $x$, which is not a Möbius map, so the argument that conformal invariance forbids the target was wrong. The Weil form is exactly invariant under dilation in $r$ and inversion --- the residual conformal group of a ray with one end pinned --- and positivity is invariant along a conformal orbit (Proposition 9.6). Upgrades the principal-series remark to a symmetry match, and adds Remark 8.8 recording that flatness concerns the two-parameter slice and not the space of contours. |

These records establish file identity and build provenance, not mathematical
correctness.

## Endpoint continuation baseline

`2026-09-18-v08-endpoint-baseline` preserves the current **version 0.8, 47-page**
source/PDF/check package before endpoint-matter work. It is a new snapshot of the
existing version, not manuscript version 0.9. All older snapshots remain intact.
The snapshot tool's inherited generic title text is not the manuscript title;
use the saved TeX/PDF title. Its hashes verify the files as saved.

The intervening snapshots omitted from the older table are also preserved:

| Snapshot | Version | Pages |
|---|---|---|
| `2026-09-17-v04` | 0.4 | 37 |
| `2026-09-17-v05` | 0.5 | 43 |
| `2026-09-17-v06` | 0.6 | 46 |
| `2026-09-17-v07` | 0.7 | 46 |
| `2026-09-17-v08` | 0.8 | 47 |
