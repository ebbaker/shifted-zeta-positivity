# Code

Per-paper reproduction code lives **next to each paper**, not here:

| Paper | Code | What it covers |
|---|---|---|
| `papers/psi-omega-margin/code/` | `c1`–`c8` + `README.md`, `requirements.txt` | closed forms, prime-side asymptotics, series identity, windows, Dirichlet section |
| `papers/omega-string/` | `fig_density.py`, `v1_identities.py`, `v2_thmE_kasahara.py` | Figure 1, residue lemma and Fourier block, Theorem E tables, Kasahara dual curve, endpoint length |
| `papers/defect-depth/code/` | `lab_ihara_core.py`, `lab_ihara_experiments.py` + `README.md`, `requirements.txt` | the finite Ihara-zeta laboratory (rounds 1–5) behind Paper 3 |
| `papers/rh-detector/code/` | `h1`, `h3`, `h4`, `d1`, `d4`, `v1` + `zeros1001.json`, `beta_zeros.json`, `README.md`, `requirements.txt` | every table and section of the detector paper |
| `verification/first-slab/scripts/` | two recomputation scripts | independent checks of the first-slab preprint (not certificates) |

This directory holds only what has no paper home yet:

```
code/
├── README.md
└── certificates/
    └── first-slab/     README.md only — release gated, see below
```

All code is MIT-licensed (see the dual-license notice in `../LICENSE`).
Python; `mpmath`, `numpy`, `scipy`, `sympy`; multi-precision throughout. Each
paper's `code/requirements.txt` pins its own environment;
`../environment/requirements.txt` covers the verification scripts.

## Not here yet, and why

**`certificates/first-slab/`** — the primary Arb certificate
(`investigation12_offcenter_weil_generator.py` with the inherited
`project_support/investigation7_first_slab_certificate.py`), the clean-room
audit (`investigation14_independent_generator_audit.py`), the diagnostics
(`investigation13_operator_diagnostics.py`), their `verify_*` scripts and the
result CSVs (724 / 783 / 1360 rows). Appendix B of the preprint documents the
commands and expected summaries. **Release gate** (items D1–D5 of
`../verification/first-slab/CHECKLIST.md`):

- [ ] D1 re-derive the inherited Investigation 7 tail majorants
- [ ] D2 the interval `LDLᵀ` and box-construction code read by someone other than its author
- [ ] D3 full primary-vs-audit row diff
- [ ] D4 version-pinned rerun in clean environments with archived logs and manifests
- [ ] D5 fix the stale sentences in the Investigation 12/14 write-ups (checklist items 0.1, 0.2, 0.5)

Until then the code is available from the author on request. It additionally
needs `python-flint` (Arb); the version is recorded at code release.

**Still unrecovered** (ran only in session workspaces): the round-6 inline
runs for Paper 3 (amplitude certification, `s₀` scan, unscaled real-ζ suite,
envelope bracketing — a pre-release item in `papers/defect-depth/STATUS.md`),
the Herglotz-peeling reconstruction for Paper 2, and the scripts of the closed
geometry/physics routes listed in `../MANIFEST.md`.
