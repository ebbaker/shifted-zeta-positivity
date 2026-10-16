# Preserved draft snapshots

Each directory is a complete, standalone package: the TeX sources, the PDF, the
build guide, the validation tool, `BUILD_RECORD.json` pinning the reviewed
source/PDF pair, and `SNAPSHOT.json` pinning the saved files.
`validation/drafts.py save` refuses to overwrite an existing snapshot, and a
snapshot carries its own copy of the tool so it can be verified in isolation.

| Snapshot | Version | Reviewed | Contents |
|---|---|---|---|
| `2026-09-18-v01` | 0.1 | 18 September 2026 | First draft, 21 pages. The whole investigation in one place: the transfer as the primitive-Epstein scattering matrix of the rank-$(d{+}1)$ lattices at every integer $d$; the wall at $m=2$ as the zero of $a=\frac{2-m}2$, where the archimedean pole crosses, $R_\omega$ turns inner, and the poles of $K_\omega$ leave the right half-plane; complete monotonicity surviving the crossing by two groupings of the Gamma factors exchanged there; the criterion vacuous for $\omega\ge\frac12$ by the Euler product, so its content sits on exactly $m\in(1,2)$, with the Euler product its value at rank two and RH its derivative at rank one; the point count's failure as Lagrange's four-square theorem read through a binomial series; and the two failures shown not to be one fact, separated by whether the rank is an exponent or a binomial index. Six registered check programmes, 1522 cases, replayed with it. Drafted for Edward Baker by Claude Opus 5; visual review by the model only. |

These records establish file identity and build provenance, not mathematical
correctness.
