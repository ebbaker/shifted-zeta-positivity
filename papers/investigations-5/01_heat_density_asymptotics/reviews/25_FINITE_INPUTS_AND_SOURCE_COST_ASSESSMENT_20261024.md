# Finite inputs and positive-source cost: internal assessment

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from parent turn metadata. Chat 0015, thread
`01a1711d-376c-7de3-929c-60ec4065bddc`.

**Disposition: HDA-18-AN02 r1 completed as bounded analysis, with a
constructive source-size upper bound and the unpaid FI23 gate retained.**
[Note 44](../notes/44_FINITE_INPUTS_CLIPPED_SOURCE_AND_OUTER_GATE_20261024.md)
and its [manifest](../notes/44_FINITE_INPUTS_MANIFEST_20261024.json)
record the proof and starting versions. No finite model-gap index or
numerical source is accepted. HDA-17 Partial, HDA-18 Gated and HDA-20
unfulfilled are unchanged.

This assessment includes main-assistant derivation and several separate
same-model analytical subagent checks: source construction/cost, finite
model/regulator coefficients, independent source/cost audit, and a short
check of the unified core source coefficient. They share premises and
are not independent specialist review. Read the
[result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md)
and [avoid index](../../../../avoid/README.md), particularly
[shared review](../../../../avoid/05_same_model_reviews_and_shared_premises.md)
and [scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## Evidence and mathematical findings

- The fixed finite template is J=[95,97],t0=96,ell=h=Y=1,Y_b=4, with the
  unchanged physical eta. This selects theorem parameters and accepts
  neither an outer onset nor a particular X.
- FI1–FI8 express the gamma-model jet, time, actual-root-speed, gap and
  residual caps by a finite branch chart's alpha-derivative bounds. FI5
  pays the quadratic vertical real-phase variation; c0=1/2 is safe under
  FI6. Full branch/collar validation remains explicit, not presumed.
- FI9–FI10 give a concrete smooth flat cutoff and test partition with
  explicit first/second/third derivative caps. All Note 43 partition,
  nonholomorphic, component heat, curvature and actual covariance terms
  remain consumers; a source construction does not replace those rows.
- FI11–FI15 pay the real-regulator-saddle bracket, core floor, switch
  derivative, physical coefficient weights and polynomial-kernel norms.
  The explicit floor e_c=E_eta exp(-R_c^2/452) is used only in the compact
  core. FI15a/b correctly factors the core primitive/tuple errors by
  4varepsilon/e_c^2 with fixed covariance caps and support area <=4.
- FI16's positive clipping is a pointwise contraction relative to the
  complete nonnegative Phi. It preserves the fourth-order Hermite
  remainder and yields at most four pieces per source cell. The clipped
  source's compact integral is entire and exactly heat; source corners
  cause no spatial/time differentiation issue.
- FI17's B4=2^20 bound is for the complete source on the whole half-line,
  with a finite rational first-mode/tail certificate. It is not a sampled
  finite-mode derivative cap. FI18–FI19 pay interpolation, omitted nodal
  values/slopes, nodal arithmetic and the complete source tail separately,
  totaling 29varepsilon/64. Exact rational polynomial construction and
  clipping add no further source error, while field/filter arithmetic
  remains separate.
- The finite data algorithm evaluates exp(-A_hat) at a rational approximate
  argument and propagates |A-A_hat| through the derivative bound. It does
  not assume a P-bit input interval gives a P-bit exact composite-output
  interval. Certified upper integers replace undecidable exact boundary
  comparisons in the ceiling formulas. These clarifications were applied
  before installation; no correction to prior source notes was needed.
- FI20 is a conservative description-size upper bound, including algebraic
  root descriptors/isolation intervals. It implies no efficient runtime.
  Nodal arithmetic/root isolation/field evaluation have distinct work
  costs. M=varepsilon^-1/4 exp(O(log^2 log(1/varepsilon))) is a sufficient
  cell bound, not an optimality or unaffordability lower bound.

The finite mathematical obligation still unpaid is FI23: a full analytic
buffer bound on max_(j<=3)|partial_z^j(H-P)|/(L^j A), even if the source
error is zero. Notes 30–31 provide eventual O_J(X^-2) estimates but no
finite C,c,b0,R_* and Cauchy-circle constants for this acceptance test.
This is an uninstantiated comparison debit, not a false estimate or an
impossibility of finding a gap. FI8's exact small residual does not supply
solution accuracy. Pure exterior/collar/weighted/signed-pole constants
remain further acceptance obligations.

## Bounded arithmetic record

[Script](../numerics/finite_input_rational_bounds.py) and
[record](../numerics/FINITE_INPUT_RATIONAL_BOUNDS_20261024.json): **five
exact-rational scalar checks passed**, no failures. They check the complete
fourth-derivative rational majorant, its mode ratio, kernel derivative
coefficient sums, beta' ceiling and regulator-saddle bracket arithmetic.
One execution, **0.0001837501 seconds**, within the two-minute packet cap.
No theta/source nodes, gamma values, field values, mesh/precision search,
interval campaign or continuous theorem certificate. The source recipe
and its finite nodal algorithm were derived and not executed.

## Research disposition

AN02 r1 is CLOSED at this recorded analytical scope; its original request
is frozen and return appended. The existing register and chat 0015 history
are updated. AN01 remains closed at its full-support analytical scope.
The manuscript, DRAFT_HISTORY, earlier source notes, frozen diagnostics
and parent statuses remain unchanged.

**Next: Analysis — Sol**, [HDA-18-AN03 r1](../research-progress/handoffs/HDA-18-AN03.md).
Make the full complex-buffer FS20 estimate effective on J=[95,97], with
explicit branch/contour/Cauchy constants, or return one exact failed
component. This is routine finite-input follow-through unless a named
structural bound resists the focused attempt. No theta execution, new
chat or automatic Astra escalation is dispatched.
