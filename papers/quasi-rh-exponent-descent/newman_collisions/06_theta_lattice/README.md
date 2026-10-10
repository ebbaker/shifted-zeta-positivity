# Theta lattice rotor reduction and endpoint Ward identities

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Internal LLM checks are not
independent mathematical validation.

This investigation implements direction 06 of
[Heat Note 14](../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
Can lattice duality supply a signed candidate-conditioned relation for the genuine theta readout after reduction?

The initial result is an affine theta Ward identity, including the exact zero-mode endpoint constant, and an explicit spectator-rotor coefficient and odd-endpoint mismatch. The identity uses genuine theta data but presently has no excluding sign.

| Item | Exact architecture |
| --- | --- |
| Enlarged state and arithmetic data | Trace-class inserted rotor state on `ell^2(Z)`, parameterized by the logarithmic coordinate `u`, with the full theta sum |
| Generator and orientation | Multiplication by `u^2` in Newman time; ordinary rotor thermal time has a different generator |
| Reduction map | Trace followed by `integral_0^infty exp(tu^2) cos(xu) du`; raw derivative uses `-u sin(xu)` |
| Domain | Trace-norm integrable insertions and every fixed polynomial moment on bounded time and complex-height sets; full theta reflection retained |
| Admissible state class | The actual untwisted theta lattice and declared sector projections; arbitrary coefficient twists are not assumed |
| Intended collision implication | A candidate-conditioned signed relation among the exact `J` moments that contradicts the paid normalized threshold jet inequality |

[Note 1](notes/1_ROTOR_ZERO_MODE_WARD_IDENTITY_AND_SECTOR_MISMATCH_20261010.md) gives the derivation and scoped results.
[Note 2](notes/2_GREEN_KERNEL_ENDPOINT_EQUIVALENCE_AND_CONDITIONAL_JETS_20261010.md)
derives a positive Green-kernel inverse, identifies the endpoint constant
with \(H_0(i)=1/16\), and proves the complete endpoint hierarchy is shared
by a smooth positive double-zero control. Its candidate Jacobian isolates
the uncontrolled sixth auxiliary jet. The new result strengthens the
generic-Ward obstruction; an integer-theta coefficient inequality remains
open.
The [numerical guide](numerics/README.md) records the exact finite checks;
the [internal review](reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md) records
what they do and do not establish.

The [continuation review](reviews/2_GREEN_ENDPOINT_INTERNAL_REVIEW_20261010.md)
checks the Green inverse domain, normalized control, and conditional
sixth-jet obstruction.

Use the affine Ward identity with a specific theta/SUSY moment constraint, retaining its endpoint constant and moments through order six. The product spectator completion cannot supply the missing sign.

This scout reaches exact representation and the stated additional identity
or obstruction. It does not establish a paid signed collision exclusion,
RH, or a literature-priority claim. Endpoint coverage and independent
specialist review remain outstanding.

The stable manuscript is [newman_collision_reductions.tex](../newman_collision_reductions.tex).
Follow [LARGE_FILES.md](../../../../LARGE_FILES.md); these are sources and
small deterministic records, with no large derived dataset or manuscript
snapshot created.
