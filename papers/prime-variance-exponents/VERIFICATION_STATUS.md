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
| Möbius small-divisor elimination | Proved O(X^(9/5)(log X)²) discarded energy at d≤X^(9/10); remaining cofactors O(X^(1/10)); limiting 11/12 cutoff also checked | [Arithmetic localization review](reviews/ARITHMETIC_LOCALIZATION_REVIEW_20261004.md) |
| Balanced Vaughan reduction | Proved quadratic or strictly subquadratic remainder with explicit logarithmic continuum; no saving for retained sum claimed | [Arithmetic localization review](reviews/ARITHMETIC_LOCALIZATION_REVIEW_20261004.md) |
| Sixth-order short-interval reconstruction | Peano kernel, endpoint atoms, cap estimate, and exponent budget checked; gives O(X) norm error at h=X^(11/12) | [Reconstruction note](notes/HIGHER_ORDER_SHORT_INTERVAL_RECONSTRUCTION_20261004.md), [second review](reviews/MOBIUS_PILOT_REVIEW_20261004.md) |
| Actual-coefficient cofactor and Vaughan pilot | Independent sieve/divisor/weight checks and quadrature refinement passed; finite floating diagnostic, not certification | [Numerical package](numerics/mobius_reduction_20261004/README.md), [review](reviews/MOBIUS_PILOT_REVIEW_20261004.md) |
| Modern Type II input | Exact primary theorem/ranges audited; polynomial hypothesis needed for a power saving remains unproved | [Source audit](notes/BILINEAR_INPUT_SOURCE_AUDIT_20261004.md) |
| Capped Mellin localization | Gaussian mean-square and Plancherel proof give outer energy O_g(X²(log X)^5(T^(-11)+XT^(-12))); T=X^(1/12)log X gives o(X) norm error | [Continuation](notes/SIGNED_MELLIN_CONTINUATION_20261004.md), [review](reviews/SIGNED_MELLIN_CONTINUATION_REVIEW_20261004.md) |
| Exact signed Mertens representation | Hard-cutoff Abel boundary, derivative measure, uniform kernel integrals and nonzero continuum moment checked; known envelopes give subpower only | [Continuation](notes/SIGNED_MELLIN_CONTINUATION_20261004.md), [review](reviews/SIGNED_MELLIN_CONTINUATION_REVIEW_20261004.md) |
| Conditional exponent endpoint | Proved: X^(3−κ+o(1)) for a quadratically equivalent response implies O(X^(3−κ)), 0<κ≤1; no positive κ established | [Continuation](notes/SIGNED_MELLIN_CONTINUATION_20261004.md), [review](reviews/SIGNED_MELLIN_CONTINUATION_REVIEW_20261004.md) |
| Low-frequency Type II obstruction | Proved conditional real-block t=0 Mellin criterion implying a fixed strip; full real-block/partial-block quantifiers explicit | [Continuation](notes/SIGNED_MELLIN_CONTINUATION_20261004.md), [review](reviews/SIGNED_MELLIN_CONTINUATION_REVIEW_20261004.md) |
| Separated cofactor endpoints | Higher-order reciprocal-zeta poles checked; exact individual-channel energy bound excludes off-critical boundary zeros, beyond the signed-response requirement | [Continuation](notes/SIGNED_MELLIN_CONTINUATION_20261004.md), [review](reviews/SIGNED_MELLIN_CONTINUATION_REVIEW_20261004.md) |

All recorded finite bounds apply to every real X in their stated intervals.
They do not establish a global quadratic estimate. Source and certificate
identifiers, completed checks, and final-source details are collected in the
[final manuscript review](reviews/MANUSCRIPT_REVIEW_20261004.md).

The subsequent [initial delta investigation](notes/INITIAL_DELTA_INVESTIGATION_20261004.md)
adds research notes and a small diagnostic package. It does not change the
manuscript or its previously recorded compilation state, and does not
claim a smaller global delta. Its promising initial result is the proved
elimination of large arithmetic sectors below the quadratic energy scale.

The [signed Mellin continuation](notes/SIGNED_MELLIN_CONTINUATION_20261004.md)
adds checked analytic reductions and conditional endpoint/obstruction
statements. It changes no manuscript source or compilation record and
adds no numerical certificate. The signed central estimate and the first
global exponent below one remain open.

The [project overview](notes/PROJECT_OVERVIEW_20261004.md) and ten program
charters synthesize prior work and identify prospective inputs. Their
[internal planning review](reviews/PROJECT_OVERVIEW_REVIEW_20261004.md)
checks status distinctions, exponent budgets, primary-source conventions
and local links. This is research organization, not a new proof,
certificate, manuscript change or compilation event.
