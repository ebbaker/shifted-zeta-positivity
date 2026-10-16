# First-slab certificate code (not yet released)

The interval-arithmetic certificate behind Theorem B of the
[preprint](first_slab_positivity.tex) is not in this repository yet. What it
consists of, how it is run, and the expected summaries are documented in
Appendix B of the preprint. Available from the author on request:
edwardbaker86@gmail.com.

The code consists of the primary Arb certificate
(`investigation12_offcenter_weil_generator.py` with the inherited
`project_support/investigation7_first_slab_certificate.py`), the clean-room
audit (`investigation14_independent_generator_audit.py`), the diagnostics
(`investigation13_operator_diagnostics.py`), their `verify_*` scripts and the
result CSVs (724 / 783 / 1360 rows). Appendix B of the preprint documents the
commands and expected summaries. **Release gate** (items D1–D5 of
[verification/CHECKLIST.md](verification/CHECKLIST.md)):

- [ ] D1 re-derive the inherited Investigation 7 tail majorants
- [ ] D2 the interval `LDLᵀ` and box-construction code read by someone other than its author
- [ ] D3 full primary-vs-audit row diff
- [ ] D4 version-pinned rerun in clean environments with archived logs and manifests
- [ ] D5 fix the stale sentences in the Investigation 12/14 write-ups (checklist items 0.1, 0.2, 0.5)

**Status (9 Sept 2026).** The code and result tables have been recovered from
the project workspace and packaged as a review candidate outside this
repository, with a hash manifest, the original per-investigation dependency
pins (`python-flint==0.9.0` for the Arb generator) and a 5 September 2026
full-regeneration record whose output hashes match the recovered CSVs. On 9 Sept 2026 all
three computations were regenerated in a fresh pinned environment and produced
byte-identical tables ([verification/CERTIFICATE_RERUN_20260909.md](verification/CERTIFICATE_RERUN_20260909.md));
the stored-table verifiers (`verify_investigation1{2,3,4}_results.py`) pass on
the recovered tables (724 / 90 / 783 + 1360 rows; minimum Weyl–Schur margins
`6.116350109501e-4` even, `5.261670009275e-2` odd; audit margin
`6.116514636999e-4`). None of that closes D1–D5: hash agreement and passing
table checks establish file identity and repeatability, not the correctness of
the inherited analytic bounds, and the historical write-ups (Investigation
12 §4, §8.4; Investigation 14's opening list and §9) still carry the stale
sentences of D5. Until the gate is passed the code is available from the
author on request.

The certificate, once released, belongs in this folder beside the preprint,
like the `numerics/` folders of Weil-depth and storage-depth. The
[verification records](verification/README.md) and the
[statement blueprint](blueprint/README.md) are also here.

Moved here on 16 October 2026 from the repository-root `code/` folder
(`code/README.md` and `code/certificates/first-slab/README.md`). Its
per-paper code table duplicated the papers' own READMEs, and its list of
scripts that ran only in session workspaces is kept in
[MANIFEST.md](../../../../MANIFEST.md) ("Not present anywhere"); see the
[relocation record](../../../REORGANIZATION_20261016.md). The earlier text is
in the repository history.

[First-slab preprint](README.md) · [Shifted-zeta program](../README.md)
