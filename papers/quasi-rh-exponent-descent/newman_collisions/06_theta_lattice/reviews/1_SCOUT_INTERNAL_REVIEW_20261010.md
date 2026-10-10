# Internal scout review: 06_theta_lattice

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Internal LLM checks are not
independent mathematical validation.

Scope: review of [Note 1](../notes/1_ROTOR_ZERO_MODE_WARD_IDENTITY_AND_SECTOR_MISMATCH_20261010.md) and the associated
[exact checker](../numerics/check_theta_lattice_scout.py). This review was performed by
the same LLM research scout. It is an internal audit and must not be
represented as independent validation or specialist mathematical review.

## Findings

The trace insertion agrees term by term with the manuscript, including the paired nonzero modes and zero-mode annihilation. Poisson duality makes `h=e^u theta(e^{4u})` even; its derivative vanishes at zero and forces `k'(0)=-1`. Integration by parts therefore retains the affine constant one. The signs of `4txJ'` and `-4t^2J''` pass the polynomial checker, and the time-dependent operator preserves backward heat.

The half-line subtraction has super-exponential decay. The tempting even subtraction by `2 cosh u` has only exponential decay and fails the positive-time Gaussian domain; the note marks this separately. The spectator factor changes the original kernel and creates a nonzero odd endpoint derivative. Projection restores the original kernel with no surviving new constraint. The fourth readout requires the sixth `J` moment, so the scout does not claim moment closure.

The actual candidate relation has no derived sign. Any future threshold application must restore the analytic normalizer, measured quadratic payment, and higher-multiplicity coverage. These are unresolved research obligations, not checked numerical facts.

## Reproducible checks and limitations

The retained checker run passed 11 exact assertions and a fresh
repeat reproduced its small record byte for byte. The record binds its
source SHA-256. Rotor insertion, zero-mode differential identity, first four spatial derivatives, backward-heat compatibility, and formal spectator endpoint mismatch.

No actual oscillatory theta moments are numerically evaluated. Formal endpoint data do not certify a signed lower bound or the infinite trace interchange.
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

Use the affine Ward identity with a specific theta/SUSY moment constraint, retaining its endpoint constant and moments through order six. The product spectator completion cannot supply the missing sign.
No theorem beyond the stated scopes or literature-priority claim is approved
by this internal audit. Independent specialist and literature review remain
necessary before treating these results as independently validated.
