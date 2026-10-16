# Genuine-trace results integrated into the live manuscript

Date: 21 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided identity).
Effort setting: not exposed in this session; not inferred.
Status: internal manuscript integration and reproducibility checks; not an independent mathematical or physics review.

## What changed

At Baker's request, the genuine-growing-trace calculation is now in the
live manuscript and supplementary information. No new dated draft was
saved, no version number was advanced, and the archived version 0.5 and
all earlier snapshots are unchanged. Both current documents identify
themselves as an unarchived live revision of version 0.5, dated
21 September 2026.

Main Section 5 states the fixed-theory question and the independently
specified observable: the actual planar Loewner trace, completed by a
straight return chord, in pure Euclidean SU(N) Yang--Mills. It explains
tip cancellation, the first two insertion equations, the linear-driver
short-time response, and the specific Makeenko--Migdal closure question.
The introduction, abstract, outlook and statement ledger now foreground
this physical question. Arithmetic matching remains a later task.

Supplementary Section S13 supplies the field/action conventions,
fixed positive field-flow resolution, quantum regularity assumptions,
ordered-matrix proofs, implicit linear-driver trace, convergent local
series, and the explicit curvature-moment remainder inequality. It also
retains the transverse four-dimensional insertion, finite-N product
expectations and the field-flow response kernel needed in a
Schwinger--Dyson reduction. A scalar-coupled N=4 extension is not assumed.
Sections S1--S12 retain their numbering; diagnostics and provenance are
now S14 and S15.

The new field identities are exact for the specified smooth connections.
The quantum expectation identities and short-time bound are conditional
on the stated regularity and finite moments. They retain the original
interacting measure. No Gaussian substitution, closed scalar evolution,
unflowed continuum theorem, or arithmetic transfer realization is claimed.

The earlier arithmetic overview contained stale descriptions of the
bounded append as still open. Main Section 9.4 and SI S9.5 now cite the
subsequent internal bound below 0.951 at the designated parameters, while
leaving its proof in the critical-path investigation and preserving its
outstanding specialist-review status. The finite diagnostic near 0.802
is still identified as a diagnostic, not an all-input upper bound.
Manuscript separation of the arithmetic results remains deferred.

## Sources and checks

The derivation and its research handoff remain unchanged:

- [Research calculation](GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md).
- [Research continuation](RESEARCH_CONTINUATION_AFTER_GROWING_TRACE_20260921.md).
- [Reproducible diagnostic](../numerics/check_growing_trace_hierarchy.py).
- [Small diagnostic record](../numerics/records/growing-trace-hierarchy-20260921.json).

Both live documents build independently with their local TeX inputs.
The main PDF has 24 pages and the supplement 46. The final build logs
contain no undefined references, multiply defined labels or overflow
warnings. All rendered pages were inspected for layout; the new equations,
proofs and status table received additional inspection. This is a visual
and source-identity review, not specialist review of the mathematics.

The separate NumPy growing-trace diagnostic was rerun successfully to a
temporary output; the resulting parsed JSON equals the preserved record.
It checks deterministic geometry and finite matrix transport, not a
quantum measure. The original four-program replay remains 299 cases.
The live BUILD_RECORD binds the new TeX dependencies and the additional
program/record without changing historical snapshot records. The broader
package inventory is refreshed separately.

No third-party PDFs or large derived data were added. Rendering images
and authoring intermediates remain outside the repository. The current
PDFs are each below 1 MB.

## Next-session handoff

Continue from the specific derivative moment in the two-equation
hierarchy, following the existing research handoff. A finite-regulator
Schwinger--Dyson calculation should retain the transverse insertion,
finite-N products and (at positive field-flow time) the flow response.
It should state whether these terms close in an explicitly defined
observable family or identify a quantified residual. A change of return
path or endpoint contraction is a new observable within the same theory
and needs its own derived evolution.

Keep updating the live sources as research develops. Do not create a
new dated draft snapshot unless Baker requests it. Preserve the separate
arithmetic investigation, its review status, and all historical notes.
