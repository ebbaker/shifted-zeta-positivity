# Preserved draft snapshots

Each directory is a complete, standalone package: the TeX sources, the PDF, the
build guide, the validation tool, `BUILD_RECORD.json` pinning the reviewed
source/PDF pair, and `SNAPSHOT.json` pinning the saved files.
`validation/drafts.py save` refuses to overwrite an existing snapshot, and a
snapshot carries its own copy of the tool so it can be verified in isolation.

| Snapshot | Version | Reviewed | Contents |
|---|---|---|---|
| `2026-09-17-v01` | 0.1 | 17 September 2026 | First draft, 25 pages. A self-contained report of the investigation so far, with a pedagogical introduction running from Weil's criterion through the shifted family as an all-pass filter and the dichotomy, the Wilson-line and Loewner proposals, the factorization $K_\omega=B_b\widehat K_\omega$ with $\widehat K_\omega$ completely monotone ("a positive measure minus twice its exponential moving average"), the dictionary for its pieces (Bessel additivity, Hecke comb, forced Blaschke factor, modular surface at $\omega=\frac12$), and the contraction margin at $L=\log3$ with the second-order theory of the defect and the first-order tail. Drafted for Edward Baker by Claude Fable 5.1; visual review by the model only. |

These records establish file identity and build provenance, not mathematical
correctness.
