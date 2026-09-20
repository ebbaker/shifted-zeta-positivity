# Preserved draft snapshots

Each directory is a complete, standalone package: the TeX sources, the PDF, the
build guide, the check programs and their records, `BUILD_RECORD.json` pinning
the reviewed source/PDF pair, and `SNAPSHOT.json` pinning the saved files.
`validation/drafts.py save` refuses to overwrite an existing snapshot, and a
snapshot carries its own copy of the tool so it can be verified in isolation.

| Snapshot | Version | Reviewed | Contents |
|---|---|---|---|
| `2026-09-16-v01` | 0.1 | 16 September 2026 | First complete draft: the density identity, the jump form, the symbol split, the Perron--Frobenius structure and its obstruction, the necessary condition and its disproof test, and the nine selection rules. |

These records establish file identity and build provenance, not mathematical
correctness.
