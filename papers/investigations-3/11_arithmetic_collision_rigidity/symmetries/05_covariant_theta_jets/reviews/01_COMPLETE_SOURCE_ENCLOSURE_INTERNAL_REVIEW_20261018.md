# S05 internal assessment of the complete-source enclosure component

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from this turn's metadata. Internal review by the
authoring assistant and two separate same-model agents; no independent
model or specialist human review.

The [note][note] and [retained computation][numerics] support a bounded
source-enclosure result. They do not establish that the covariant basis is
intrinsically faster, or that the new source ranges improve a signed
spectral calculation. Keep the [program guide][guide], [result summaries][summaries],
and [avoidance patterns][avoid] as the scope reference; specifically
[theta identities][s14], [controls][s12], [generic lifts][a03],
[status words][a06], [scoped exclusions][a07], and [cancellation][a12].

| Item assessed | Disposition |
| --- | --- |
| Covariant-to-mode algebra | Exact coefficient combination through source derivative eight agrees with the existing direct recurrence; zero lattice terms cancel before evaluation. This is a consistency check of known identities. |
| Complete infinite tails | The geometric majorant uses upper rectangle endpoints for polynomial factors and lower endpoints for Gaussian decay. All required ratios contract. The proof covers every omitted mode. |
| Taylor remainder | Correct for r=0,1,2: source orders seven and other odd endpoints vanish analytically; the complete derivative-eight bound pays `M8*h^(8-r)/(8-r)!`. |
| Coefficient uncertainty | Endpoint even coefficients through order six retain their tails and rounding; the cell derivative-eight tail is included before the absolute bound. |
| Fair baseline | Imports the existing expanded `source_jet` at zero heat parameter, with identical source cells, eight modes, precision, and full tails. It also reports a stronger fused-Horner comparison. |
| Local gate | Passes for all three source derivatives on every declared small real cell at 192 and 256 bits. |
| Whole source cover | Fused Horner is tighter on all real cells; shifted order two is wider on 34/64 cells. No uniform complex second-derivative improvement is claimed. |
| Special cases | Exact odd endpoints are analytically justified; a finite weighted square mode with nonzero odd endpoint rejects their unjustified reuse. Negative real arguments use full-source reflection. Shifted cells are on `Im u=pi/16`, not a tested whole strip. |
| Regression controls | Five existing event boxes reject the old strict tests, and the separate Euler negative-Laguerre witness rejects a global signed-margin test. These do not test the new analytic tail proof. |
| Cost and usefulness | Local interval gain is demonstrated. Cold setup needs endpoint derivatives through six and a complete derivative-eight cell bound. No matched runtime or downstream spectral improvement has been measured. |

For `[0,1/1024]`, conservative radius improvements against the actual
expanded baseline exceed 894.47, 7.29, 2394.90. Against the stronger fused
baseline they still exceed 694.40, 1.63, 639.05. These are reductions in
interval dependency, not physical point-error factors. Higher precision
repeats the strict inequalities; the repeat is a sensitivity check and does
not upgrade the analytic claim.

An additional same-model audit independently recomputed the four Taylor
rows and checked the retained 192-bit enclosures at 17 points per cell
using 384 bits and ten modes. Finite containment samples support the
implementation check; the tail and Taylor derivations establish coverage.

The most important limitation is the transfer back to the physical field.
The established spectral evaluator uses source values on a shifted contour
and spectral powers of `u`; the new strongest comparison is near a real
source endpoint and concerns source derivatives. Absolute integration of
the value remainder at `h=1/64` already costs about `4e-11` before the rest
of the integral is handled. No comparison with the consumer's required
physical allowance is won here. Enlarging the scan would not repair that
missing transfer estimate.

The local ladder does not distinguish weighted collision controls, and
parity is shared by reflected colliding sources. The optimization has no
positivity implication. The missing theta-specific premises by family are
explicitly retained in the note and [Review 14][r14]; analytic controls
without effective boxes are not assigned invented numerical events.

**Decision:** accept the component as a local complete-source enclosure
improvement with same-model review. Retain the narrower real endpoint
Taylor evaluator for a named source-boundary consumer, with direct or fused
evaluation available elsewhere. Require a paid, cancellation-preserving
spectral handoff or a measured consumer cost comparison before another
quantitative milestone. The global bridge and complex exterior remain open.

[note]: ../notes/01_COMPLETE_SOURCE_JETS_AND_FIXED_POINT_ENCLOSURES_20261018.md
[numerics]: ../numerics/README.md
[guide]: ../../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[r14]: ../../../reviews/14_HODGE_AND_MODULAR_SYMMETRY_ASSESSMENT_20261018.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[s14]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[s12]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a03]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a06]: ../../../../../../avoid/06_status_stronger_than_the_evidence.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
