# E08 r1 literal-source acquisition pilot

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Exact-turn local provenance records
**gpt-6.1-sol / ultra**. Implementation helpers inherited the turn's
model settings. The [author assessment][review] is internal.

**All four fixed cases are interval-certified pilot passes.**
[Request26][request] and [Inputs26][inputs] bound the procedure and
the 27 verified input files. [Record09][record] holds all coefficient
enclosures, the exact dyadic polynomial data, derivative error
allowances through order seven, contour/count records, factor and
gamma enclosures, subdivisions, and timings. All cases stopped at
128 bits. No alternate source supplied any field value or root.

## Direct comparator

At \(c=30\) the degree-64 polynomial is accompanied by the directed
source error \(\epsilon_0<3.00\,10^{-25}\) throughout radius \(3/2\).
The four complete edges of \(D=[29,31]+i[1/2,1]\) have
\(|p|>5.33\,10^{-5}\) and certified winding **zero**. The rectangle
lies strictly in the approximation disk since its corners have
distance at most \(\sqrt{2}\). Rouché transfers the winding to \(H_0\)
and the same strict modulus inequality pays the boundary. This
direct acquisition excludes zeros on the closed \(D\) at time zero.
The target lies in the established verification region, so the
result is a calibration. The direct comparator used no root solver,
gamma evaluation or Green tail.

## Patch certificates

All three patches pass at \(A=1/2,\ s=3/8\). The two occupied disks
each have radius \(2^{-24}\) and winding 1. The small counts equal
the outer count in each patch. Their centers are exact real dyadics,
approximately \(28.26945028346939\) and \(96.01030176233432\) in
physical coordinates. The record stores the exact centers in
coordinates relative to the patch center. Conjugation and count one
also certify that the enclosed roots are real and simple. Patch 132
has a complete zero count of zero.

| Patch | Outer / cluster count | Strict lower \(\mu_0\) | Strict upper \(e_0/\mu_0\) | Strict upper \(\lambda\) | Strict upper \(H\) | Strict upper \(B\) |
| --- | --- | --- | --- | --- | --- | --- |
| 128, \(c=113/4\) | 1 / 1 | \(2.54\,10^{-5}\) | \(7\,10^{-8}\) | 3.055 | 19.19 | 101 |
| 132, \(c=121/4\) | 0 / 0 | \(7.81\,10^{-5}\) | \(2\,10^{-26}\) | 0.334 | 18.74 | 14 |
| 263, \(c=383/4\) | 1 / 1 | \(4.90\,10^{-16}\) | \(4.34\,10^{-7}\) | 4.550 | 68.25 | 149 |

The most demanding patch has a small absolute regular-factor floor,
but passes the charged relative error gate \(e_0/\mu_0\le1/1024\).
Every small contour margin exceeds its patch's uniform \(\epsilon_0\).
The lower small-circle polynomial moduli exceed \(3.64\,10^{-12}\)
and \(1.71\,10^{-22}\), respectively. The synthetic divided-difference
values at each endpoint and midpoint satisfy the absolute radius
bound \(2^{-17}\mu\). Each of the six log-gamma endpoint enclosures
also fits radius \(2^{-17}\). No other outer radius or higher
precision tier was needed. Rejected subdivisions and earlier source
refinements remain counted in Record09.

## Measured work at the fixed cases

The same literal-source construction, \(N_{\rm src}=8,V_{\rm src}=2\),
degree 64, and arithmetic are charged to both consumers. Source
refinement starts at 32 panels. Each tested dyadic grid contributes
to the work count, including earlier grids whose error was too wide
for the chosen coefficient-refinement target. The implementation
uses coefficient-error refinement targets \(2^{-80}\) at radius
\(3/2\) for the direct case and \(2^{-92}\) at radius 1 for the
patches, which also need tiny-circle margins. These are refinement
choices. The actual acceptance gates use the directed source and
contour errors, and the timing difference includes the chosen refinements.

| Case | Cold seconds | Coefficient seconds | Warm residual seconds | Source panels tested / final grid | Contour tests | Candidate iterations |
| --- | --- | --- | --- | --- | --- | --- |
| Direct | 0.5905 | 0.5881 | 0.00234 | 480 / 256 | 4 | 0 |
| Patch 128 | 1.2101 | 1.2025 | 0.00753 | 992 / 512 | 30 | 53 |
| Patch 132 | 1.2320 | 1.2289 | 0.00307 | 992 / 512 | 1 | 0 |
| Patch 263 | 2.4928 | 2.4871 | 0.00573 | 2016 / 1024 | 34 | 61 |

Warm residual is the observed case wall time minus time in coefficient
acquisition, a conservative proxy when the validated polynomial is
already owned. It includes driver checks and small setup costs. It
is separate from the directly timed contour, root, floor, and
gamma/factor stages in Record09. The direct contour itself took
about \(0.00022\) seconds after its source data were available.
There was no cross-center polynomial reuse or second warm run.
The record also counts series exp and sin/cos calls, 65-integrand
panel work, contour polynomial calls and translations, Newton calls,
and synthetic/Horner steps. Counts inside FLINT are unavailable.

Total measured case wall time was about 5.53 seconds. The three
patch times cannot be multiplied up into a full-cover timing claim.
The cold direct comparator and the cold patches use different
centers and contours. They are charged the same provider and
validation policy. If one consumer already owns a shared polynomial
or contour, its acquisition cost belongs to both.

## Scope and continuation

The conditional formula checks are in [Review13][review]. The
[result index][results], [heat/Green cluster11][heat], [controls12][controls]
and [avoid index][avoid] distinguish this finite acquisition from a
value or RH criterion. The tested premises and collision controls
are recorded in Review13, following [avoid02][a02] and [avoid07][a07].
The direct result already pays \(D\); later Green integration at
this center would acquire a reusable observable in a known region.

Only the three fixed patch certificates have been acquired. The
other 261 patches, complete product integration and its finite
arithmetic, and the signed upper endpoint for \(J(30)\) remain open.
No full-cover contract has been issued. [Continuation17][cont]
describes when a separately authorized fixed execution would be useful.

[request]: ../research-progress/handoffs/26_TND_OG_E08_LITERAL_SOURCE_ACQUISITION_PILOT_REQUEST_20261110.md
[inputs]: ../research-progress/handoffs/26_TND_OG_E08_INPUTS_20261110.json
[record]: ../numerics/09_TND_OG_E08_DIRECTED_PILOT_20261110.jsonl
[review]: ../reviews/13_TND_OG_E08_INTERFACE_AND_CERTIFICATE_CHECK_20261110.md
[cont]: ../continuation-notes/17_TND_OG_E08_RESULTS_AND_MODEL_CHANGE_20261110.md
[results]: ../../../../../../result-summaries/README.md
[heat]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
