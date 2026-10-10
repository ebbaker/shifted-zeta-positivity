# Internal scout review: 07_automorphic_scattering

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Internal LLM checks are not
independent mathematical validation.

Scope: review of [Note 1](../notes/1_EISENSTEIN_EXTRACTION_HEAT_COMMUTATOR_AND_SPECTRAL_SLICE_20261010.md) and the associated
[exact checker](../numerics/check_automorphic_scout.py). This review was performed by
the same LLM research scout. It is an internal audit and must not be
represented as independent validation or specialist mathematical review.

## Findings

The source constant term is correctly scaled by `sigma=s/2`. The extraction annihilates the outgoing power and retains the full `s(s-1)/2` polynomial, with continuation at resonant parameters rather than division by zero. The first spectral-heat completion commutator contains both the first and second polynomial derivatives.

The exact incoming heat field is explicitly a coefficient lift, not a full automorphic eigenwave under geometric evolution. The cusp-gauge conjugation produces the printed drift and multiplication terms; the matching generator is shifted in `partial_s`. Eigenvalue differentiation gives the nonzero spectral-wave residual. At physical heat height, `sigma=1/4+ix/4`, so its energy has imaginary part `x/8`; positivity of the self-adjoint modular Laplacian cannot be used on this generalized slice as if it were the unitary radiation slice.

No global Gaussian evolution of the meromorphic uncompleted coefficient is asserted. Full theta heat or the completed entire coefficient supplies the well-defined heat state. The raw spatial readouts include completion and gauge factors through order four. An independently justified positive pairing on this channel is still missing. These restrictions concern the examined extraction, not every automorphic construction.

## Reproducible checks and limitations

The retained checker run passed 19 exact assertions and a fresh
repeat reproduced its small record byte for byte. The record binds its
source SHA-256. Completed incoming extraction, heat/completion commutator, cusp-gauge drift, eigenwave residual, and critical-line modular eigenvalue.

The checker verifies algebra, not a Maass–Selberg identity, Eisenstein domains, a positive flux theorem, or any heat-collision sign.
The formal checks do not certify the imported analytic theorems, limiting
interchanges, uniform asymptotics, actual collision signs, or RH. Their
counts are not a measure of the depth or likelihood of the proposed route.
All files obey the source/small-record convention in `LARGE_FILES.md`.

## Milestones and disposition

| Milestone | Status |
| --- | --- |
| Exact representation | Established in the stated finite or full-kernel domain |
| Additional identity or scoped obstruction | Established as printed in Note 1 |
| Paid signed collision exclusion | Not established |
| Coverage sufficient for an endpoint conclusion | Not established |

Find a positive pairing valid on the required nonunitary slice or a different exact extraction that remains in a positive channel, before studying further cusp couplings.
No theorem beyond the stated scopes or literature-priority claim is approved
by this internal audit. Independent specialist and literature review remain
necessary before treating these results as independently validated.
