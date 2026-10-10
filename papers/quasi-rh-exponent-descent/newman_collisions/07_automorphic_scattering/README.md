# Automorphic coefficient extraction and heat compatibility

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Internal LLM checks are not
independent mathematical validation.

This investigation implements direction 07 of
[Heat Note 14](../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
Does a completed modular Eisenstein coefficient provide an exact heat-amplitude channel with a surviving positive observability theorem?

The initial result gives exact zero-time xi extraction and prints three obstacles for this channel: completion does not commute with spectral heat; fixed eigenwaves are not preserved by that heat; and the xi critical-line slice is off the unitary modular spectral slice.

| Item | Exact architecture |
| --- | --- |
| Enlarged state and arithmetic data | Completed Eisenstein constant coefficient, and its entire completed incoming cusp field `V_t=e^{qs/2} Xi_t(s)` |
| Generator and orientation | Exact spectral generator `(partial_s-q/2)^2/4` on the incoming lift; ordinary modular Laplacian heat does not intertwine |
| Reduction map | Horocycle constant-term extraction, the completed operator `E_s`, then `exp(-qs/2)` in the evolving incoming field |
| Domain | Meromorphic generalized Eisenstein family for the zero-time extraction; entire completed incoming coefficient for the heat lift; no square-integrable eigenstate claim on the selected slice |
| Admissible state class | The specific modular Eisenstein arithmetic coefficient with its completion and selected spectral coordinate |
| Intended collision implication | A boundary pairing or observability theorem valid on the exact heat channel and critical-line slice, excluding common value/derivative vanishing |

[Note 1](notes/1_EISENSTEIN_EXTRACTION_HEAT_COMMUTATOR_AND_SPECTRAL_SLICE_20261010.md) gives the derivation and scoped results.
The [numerical guide](numerics/README.md) records the exact finite checks;
the [internal review](reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md) records
what they do and do not establish.

Find a positive pairing valid on the required nonunitary slice or a different exact extraction that remains in a positive channel, before studying further cusp couplings.

This scout reaches exact representation and the stated additional identity
or obstruction. It does not establish a paid signed collision exclusion,
RH, or a literature-priority claim. Endpoint coverage and independent
specialist review remain outstanding.

The stable manuscript is [newman_collision_reductions.tex](../newman_collision_reductions.tex).
Follow [LARGE_FILES.md](../../../../LARGE_FILES.md); these are sources and
small deterministic records, with no large derived dataset or manuscript
snapshot created.
