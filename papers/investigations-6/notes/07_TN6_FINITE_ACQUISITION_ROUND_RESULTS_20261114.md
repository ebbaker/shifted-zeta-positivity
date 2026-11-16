# TN6 finite coefficient acquisition: round results

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Decision worker explicitly
dispatched **gpt-6-astra / ultra**; execution worker **gpt-6.1-sol / ultra**.
Coordinator backend/effort are unavailable. Dispatch selections do not
independently attest the worker backend or runtime effort.

**Status: E02 complete; E03 accepted the finite certificate at the issued scope.**
The sole live state is the [parent register](../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md).
This note summarizes one finite acquisition, not another computational run.
The [separate internal assessment](../reviews/02_TN6_E03_ACQUISITION_ASSESSMENT_20261114.md)
accepted it without requesting correction. One unchanged replay matched
the scientific payload, decisions and counts. Shared sources and the same
selected Sol model do not supply independent specialist review.

## What was acquired

[TN6-B02](../brainstorm/notes/02_TN6_B02_FINITE_COEFFICIENT_ACQUISITION_DECISION_20261114.md)
selected parity-separated moment/LDL acquisition from the complete theta
source. [E02 r1](../research-progress/handoffs/TN6-E02-r1.md) fixed
17 even moments through degree 32, 16 positive coupling enclosures,
N=16 sites, base lambda=1/2, 0<=tau<=1/2, |x|<=8 and normalized absolute
tolerance 10^-8 in units of H_(1/2)(0)=Z_*/2. The first eight source
terms on [0,2] are an integration device; outward bounds restore the
omitted arithmetic and spatial tails.

The [execution proof and record](06_TN6_E02_CERTIFIED_COEFFICIENT_ACQUISITION_20261114.md),
[compact return](../research-progress/handoffs/TN6-E02-r1-return.md),
[exact-rational certificate](../numerics/09_TN6_E02_R1_CERTIFICATE_20261114.json)
and [generator](../numerics/execute_tn6_e02_r1.py) record a complete pass
at 256 bits after the 128-bit attempt failed its coefficient-width gate.
All pivots and couplings were already positive at 128 bits, but positivity
alone did not pay the required error. The ladder stopped at 256 bits;
512 bits and an implementation correction were not used.

| Allowance, normalized by H_(1/2)(0) | 128-bit attempt | 256-bit successful attempt | Frozen cap |
| --- | ---: | ---: | ---: |
| Uniform chain truncation Q | about 1.51424e-25 | about 1.51423e-25 | 5e-9 |
| Coefficient uncertainty 9 delta | about 1.79059e-7, failed | about 1.38427e-46 | 2e-9 |
| Normalization uncertainty eta_Z | about 3.99430e-30 | about 3.47199e-68 | 1e-9 |
| Largest numerical readout radius | not reached | below 1.740e-77 | 1e-9 |
| Largest direct-integral radius | not reached | below 3.812e-68 | 1e-9 |

Displayed decimals summarize the exact outward rational values; they are
not replacements for the certificate. The exact nominal symmetric matrix
with zero diagonal gives an **ideal scalar function** with normalized
absolute error below **1.515e-25 uniformly on this domain**. Numerical
rounding is separately enclosed at nine points, tau={0,1/4,1/2} and
x={0,4,8}; their totals are also below 1.515e-25. No continuum statement
about an unevaluated floating implementation is inferred from nine samples.

All nine independently integrated complete-source enclosures overlap the
chain enclosures after the proved allowance is included. The largest
enclosed midpoint discrepancy is about 7.77e-27 in physical units. It
occurs at tau=1/2,x=8 and is covered by the physical error allowance
below 9.465e-27. Overlap is a consistency check, not the source of the
error theorem. The Gaussian-quadrature identity is retained.

## Conditioning and recorded work

At 256 bits the certified infinity-norm condition upper bounds for the
diagonally scaled even/odd Gram blocks are below 6.94e7 and 2.02e7.
Their positivity and these diagnostics concern this finite complete-source
matrix. They do not supply a conditioning law as N grows. The128-bit
failure is a failure of the fixed interval procedure and allowance;
it is not a lower bound on the best attainable error at that precision.

The original numerical process used **20,020 callbacks**, **160,160 mode
evaluations** and about **1.986 seconds**, including the unsuccessful
precision attempt. Instrumented chain acquisition plus nine readouts took
about 1.288 seconds, versus 0.535 seconds for the nine direct integrals.
The comparison includes record-writing overhead in the phase totals;
single-call timings have different accounting scopes. The direct route
also returned much narrower intervals than the common acceptance target.
These are one-run measurements of the fixed implementations, not an
optimized comparison or a speed law. No chain speed advantage is claimed.

## Scope and controls

This is a finite **numerical enclosure milestone**, classified under
[avoid 01](../../../avoid/01_restating_the_target.md); it adds acquired
inputs and paid readouts to the earlier analytical bounds. It is not an
RH-equivalent criterion. Read the [result index](../../../result-summaries/README.md)
and [avoid index](../../../avoid/README.md), especially the
[tensor-bound cluster](../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[collision controls 12](../../../result-summaries/12_collision_controls_and_screening.md)
and [patterns 02](../../../avoid/02_shape_only_arguments_and_the_controls.md),
[05](../../../avoid/05_same_model_reviews_and_shared_premises.md),
[07](../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[20](../../../avoid/20_volume_without_a_gain.md).

The actual control screen is in the B02 decision. Its three-atom and
smooth quartic witnesses have collisions inside this finite domain while
generic accurate readout remains possible; atomic Gram rank can terminate.
Other modified sources fail the literal theta expansion and its tail
payment, and changed kernels fail the prescribed observation. These
premises prevent importing this certificate into the controls. They do
not turn approximation into noncollision. No signed-field, zero-exclusion,
relative-error, increasing-height, tensor-rank acquisition or asymptotic
efficiency result is obtained here.

The remaining decision is whether a specified reuse workload warrants
another finite benchmark. The [model/continuation note](08_TN6_CONTINUATION_AND_MODEL_HANDOFF_20261114.md)
carries the assessed disposition. The historical
[first-round handoff](05_RESEARCH_CONTINUATION_AND_MODEL_HANDOFF_20261114.md)
remains unchanged because it is a pinned E02 input.
