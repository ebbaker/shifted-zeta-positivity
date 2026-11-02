# Research overview: Circle thermal trace

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

**First assessment: MC01-B01 — B, recommended Astra at the author’s selected higher effort (ultra if chosen and available).** This is a recommendation, not the actual preparation setting or an automatic model change. Current readiness and later findings belong only in the [local progress register](../research-progress/01_CIRCLE_THERMAL_TRACE_RESEARCH_PROGRESS_20261101.md). The [parallel continuation](../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) fixes the common baseline, controls, ownership and return format.

**Research question:** Can the exact circle spectrum and theta reflection supply a quantitative identity for the reconstructed source that improves the signed response estimate?

## Background: from a particle spectrum to the coefficients

For a particle on a circle of circumference \(2\pi\), choose
\(L=-\pi\,d^2/dx^2\). Its periodic modes have energies \(\pi n^2\), and
\[
\vartheta(\beta)=\operatorname{Tr}e^{-\beta L}
=\sum_{n\in\mathbb Z}e^{-\pi\beta n^2},\qquad \beta>0.
\]
The complete theta primitive and source used here are
\[
p(u)=\tfrac12e^u[\vartheta(e^{4u})-1],\qquad
\Phi(u)=\tfrac18(p''(u)-p(u)),\qquad
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du.
\]
The zero-mode subtraction, differential reconstruction and factorial
normalization are part of the problem. Thermal parameter \(\beta\), source
coordinate \(u\), Mellin tilt \(s\), and physical heat time are distinct.
The investigation remains at physical time zero.

The theta transformation
\(\vartheta(\beta)=\beta^{-1/2}\vartheta(1/\beta)\) connects the small- and
large-temperature-parameter regimes. These exact identities are starting
data, with the source conventions in [Note04](../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md) and the
[theta differential-closure note](../../../../notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md). An ordinary thermal trace is
not a topological index. Its positive spectral weights do not sign the
source derivative determinant.

## Bounded research approach

Compare at most two concrete candidates: a differentiated theta/reflection
identity and a thermal spectral-cumulant relation. Choose one and carry it
through \((p''-p)/8\). Display the resulting identity or inequality for the
unchanged \(\Phi\) and its derivatives, then identify its exact consumer in
\((\log M_3)''\). A relation controlling only the primitive or the carrier
must include the missing transfer to the signed insertion.

The first aim is a useful source-level constraint, not a reconstruction of
the whole particle theory. Retain all integer-square modes. If a leading
mode or finite truncation enters an argument, give a differentiated error
bound and prove that it is adequate after reconstruction and integration.
Include the origin and full reflection endpoints; asymptotics alone do not
cover them. A thermal variance inequality can change its character after
differentiation, so its transfer must be proved rather than inferred.

## What counts as a result

Return one source-derived relation together with a proved contribution to
the complete response bound, or a precise calculation showing why the
selected relation leaves a particular signed term uncontrolled. A useful
conditional result names the additional inequality and its domain. Merely
recovering the known heat trace, reflection or source formula completes no
new mathematical objective.

If a bound works only for \(u\ge U\), distinguish that spatial tail from
the large-\(s\) Mellin range. Integration couples them: a spatial source
estimate does not automatically provide a relative bound for a nearly
cancelling determinant.

## Controls and known limits

The unchanged integer-square spectrum together with full normalized theta
reflection is absent from the modified Euler-factor, weighted-square,
reflected and positive-primitive controls in [the control index](../../../../../../../result-summaries/12_collision_controls_and_screening.md).
Identify the exact failed premise for the candidate being used; simply
recognizing theta is not a sign estimate. Thermal positivity, rapid decay
and a few endpoint conditions alone are insufficient screens. Finite-square
controls especially prevent treating a truncation as the complete source.
No positive-time collision in a control is automatically a counterexample
to the present time-zero, fixed-order comparison.

## Interfaces and reading

Offer any verified source identity to the other branches only with its
precise hypotheses and version. They must be able to proceed from the
frozen baseline without it. Start with [Note04, Section 1](../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md),
[the parent overview](../../research-overview/01_MELLIN_CURVATURE_RESEARCH_OVERVIEW_20261101.md), [the closure note](../../../../notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md) and the
[physical-source records](../../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md).

## Ownership, return and evidence standards

Own source reconstruction and thermal identities. Leave orbital comparison to MC02-B01, direct Mellin asymptotics to MC03-B01 and inserted ensemble integration by parts to MC04-B01.

Save the bounded return under `notes/01_THERMAL_SOURCE_IDENTITY_RETURN_YYYYMMDD.md`, using the actual local date and next unused number. Include one selected mechanism, exact inputs, a worked result or precise missing obligation, the covered domain, controls and one next B/E recommendation. Save small computations in `numerics/` and a separate assessment in `reviews/`. A finite execution campaign remains gated until its own contract is fixed. See the [local register](../research-progress/01_CIRCLE_THERMAL_TRACE_RESEARCH_PROGRESS_20261101.md) for acceptance and stopping conditions.

Use the [result index](../../../../../../../result-summaries/README.md) and [avoid index](../../../../../../../avoid/README.md), especially [controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). Existing internally reviewed results retain their review qualifications; preliminary deductions stay preliminary. Consult the [common references](../../../../references/README.md) and [import checks](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md) before using a new theorem. A finished assessment is distinct from a proved parent inequality.
