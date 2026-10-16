# Manuscript split and prescribed-evolution program

20 September 2026. Prepared for Edward Baker.

**Model:** OpenAI GPT-6 (Codex).
**Reasoning effort:** the configured effort level is not exposed to the
assistant in this session; no level is inferred.

**Status:** editorial restructuring with inherited mathematical identities,
not a new physical realization or positivity theorem.

## The manuscript pair

[The exposition](../manuscript.tex) is now organized around the hypothesis
that the exact shifted-zeta differential equation can prescribe the effective
evolution of a normalized Wilson boundary observable. The main line is:
arithmetic normalization; exact shift and defect equations; the Wilson
realization and closure problem; existing restrictions; cumulative positive
amplitudes; and depth--shift continuation.

[Supplementary information](../supplementary-information.tex) is the standalone
technical companion. This is an appropriate working title because the
document supplies the detailed tools cited by the exposition, while making no
separate claim of a complete construction. The two papers share version 0.3
and are archived together.

| Unified version 0.2 material | Version 0.3 placement |
|---|---|
| Section 1: broad introduction and results | Rewritten as the program introduction; literature context and key restrictions remain in the exposition |
| Section 2.1--2.2: central form, decay rates and local term | Exposition Section 2; repeated conventions in SI S1 for independent reading |
| Section 2.3: shifted transfer and generator | Exposition Section 3, expanded around both boxed evolution equations; SI S1 retains the causal reference |
| Section 2.4: full factorization and fractional-dimension test | SI S1.4, cited from the exposition |
| Section 3: free angular kernel and Gaussian model | SI S2; implications summarized in exposition Section 5 |
| Sections 4--5: contour geometry and exact variation | SI S3--S4; the essential insertion formula stays in exposition Section 4 |
| Sections 6--7: chiral projectors and endpoint tests | SI S5--S6; scoped endpoint obstruction stays visible in exposition Section 5 |
| Sections 8--9: reflection, smooth join and bulk response | SI S7--S8; positive-pairing requirements and scope stay in exposition Sections 5--6 |
| Section 10: ledger and next calculation | Recast as exposition Section 8; missing-response terms preserved in SI S8.4 |
| Diagnostic and provenance appendices | SI S10--S11, with a separate exposition disclosure |

SI S9 reproduces the inherited Schur, Cayley and joint depth--shift criteria
from the storage-depth background. This lets the exposition state the gluing
constraint without carrying the detailed block algebra.

## Boundaries of the new hypothesis

The arithmetic ODE is an exact input. Its interpretation as a Wilson--Loewner
construction is an inverse realization problem. No real Loewner driver,
physical boundary transfer, insertion closure, uniqueness class or
cumulative norm factorization has yet been constructed. The manuscript
distinguishes these obligations from the formal resemblance of two
first-order transport equations.

The critical path is a schedule for controlling estimates toward unbounded
length and zero shift. It is not asserted to be a true contraction boundary.
The main paper retains the diagonal implication, the separate spatial
gluing requirement and the danger of finite-depth accumulation.

The initial norm and all endpoint normalizations are fixed arithmetic
L2 norms. The companion's positive free reflected kernel has not been
identified with the cumulative defect and does not vanish at zero shift.

## Continuation

Develop a specific normalized boundary operator before choosing a proposed
driver. Use the full Wilson insertion, including endpoints, to compare its
effective generator with the fixed local, gamma, pole and prime-power terms.
Then test an independently specified accumulated norm identity or one
complete spatial gluing step.

The [critical-path investigation](../../critical-path/README.md) remains the
home for new continuation research. It was not populated in this editing
task. The [original shift-flow note](SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md)
remains the conceptual source, and the earlier notes remain historical.

The unified 0.1 and 0.2 snapshots are preserved byte-for-byte. The updated
[build guide](../BUILD.md) and portable validator record both current PDFs
and their source dependencies, while continuing to verify the old archives.
