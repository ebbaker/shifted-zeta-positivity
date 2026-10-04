# Verification status

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
All proof reviews here are internal same-model checks, not independent
specialist refereeing.

| Item | Check and status | Record |
| --- | --- | --- |
| Probe normalization, moments, support, and sixth derivative | Exact polynomial arithmetic independently reconstructed; full analytic proof in draft | [Certificate replay](reviews/CERTIFICATE_REPLAY_20261003.md) |
| Noncancellation and both directions of exponent equivalence | Fresh internal proof pass; plus-transform signs, true transform, contour bounds, zero multiplicities, delta=0/1 and closed boundaries checked | [Core review](reviews/CORE_PROOF_REVIEW_20261003.md) |
| Arithmetic support, centering, approximation constants, exponent conversion | Fresh review of complete draft | [Arithmetic review](reviews/ARITHMETIC_REVIEW_20261003.md) |
| Generic model | Prefix tracking, rotating-phase lower bound for all real X, and fixed diagonal correction checked | [Arithmetic review](reviews/ARITHMETIC_REVIEW_20261003.md) |
| Primary arithmetic references | Johnston–Yang, Platt–Trudgian, Hasanalizade–Shen–Wong and Saffari–Vaughan verified against primary texts; bibliography and theta/psi distinction checked | [Source review](reviews/SOURCES_REVIEW_20261003.md) |
| Finite variance generator | Temporary replay matched retained record byte-for-byte; original rational audit passed | [Certificate replay](reviews/CERTIFICATE_REPLAY_20261003.md) |
| Existing outward zeros and published high verification | Imported, not independently regenerated in this drafting session | [Original outward package](../investigations/sonin-critical-boundary/numerics/selective_loss_quadratic_target_20261003/README.md) |
| LaTeX source | Native desktop compiler reports success; source requested in built-in editor | [Final review](reviews/MANUSCRIPT_REVIEW_20261004.md) |
| Visual page-by-page layout and final page count | Not independently inspected; native compile tool returns no PDF or page count, and computer-use access to Codex is unavailable | [Final review](reviews/MANUSCRIPT_REVIEW_20261004.md) |
| First fixed global actual-prime exponent below one | Open; not claimed | [Manuscript](manuscript.tex) |
| Actual-prime exponent descent | Open; not assumed | [Manuscript](manuscript.tex) |

All recorded finite bounds apply to every real X in their stated intervals.
They do not establish a global quadratic estimate. Source and certificate
identifiers, completed checks, and final-source details are collected in the
[final manuscript review](reviews/MANUSCRIPT_REVIEW_20261004.md).
