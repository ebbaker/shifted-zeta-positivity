# E06 r1 uniform-midpoint feasibility at X=30

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual backend and reasoning effort are
unavailable in the accessible capture metadata. **Interval-certified
scalar outcome, with internal proof/code-author checking: recipe exceeds
cap.**

## Fixed question and outcome

[Request18][request] tests the sufficient error allowances of the literal
finite reflected theta source at Newman time zero with
\((X,d,r)=(30,1/2,1)\). It uses \(h=m(d,r)/4\), where
\(m(d,r)=\sin(\pi/8)d/\cosh(\pi r/8)\), and a cap of \(10^6\)
uniform midpoint panels. This is a finite cost diagnostic under
[avoid01][target] and a calibration in the known region under
[avoid11][known]. The [result index][results] and [patterns index][avoid]
route to [the heat/Green cluster][heat] and [the collision controls][controls].

All scalar searches resolved at **128 bits**. The first successful
cutoffs were \(R=66,\ Q=32,\ N_{\rm src}=34,\ V=29/16\), with
\(\delta=2^{-4533}\). All earlier tested \(R,N_{\rm src},j=16V\)
candidates were rigorously rejected. The ceilings defining the 132
values \(n_v\) are resolved and range from 108 to 163. The maximum in
F2 occurs at \(v=95.5\), with \(n_v=163\).

| Quantity | Directed enclosure or exact value |
| --- | --- |
| \(T(30,66)\) | \((0.00296748,0.00296749)\) |
| \(\beta_{32}\) | \((0.00368284,0.00368285)\) |
| \(h_a/6\), budget for each of \(T,\beta\) | \((0.00369750,0.00369751)\) |
| \(-\log_2\delta_*\) | \((4532.1783,4532.1784)\) |
| \(E(2^{-4533})\) | \((0.00020329,0.00020330)\) |
| \(h_a/3\) | \((0.00739500,0.00739501)\) |
| Base-two log of arithmetic source bound in F4 | \((-4824.807,-4824.806)\) |
| Base-two log of radial source bound in F4 | \((-5635.553,-5635.552)\) |
| Base-two log of each F4 budget \(\delta/2\) | \(-4534\) |
| Each symmetric evaluation radius \(e_{\rm quad}=e_{\rm node}=e_{\rm prime/G}=e_{\rm arith}\) | \((0.00277312,0.00277313)\) |

The analytical width is at most \(E+2T+2\beta\le h_a\).
F4 leaves \(\mathcal B\delta_H\le\delta/2\) because \(\delta_H\)
is half the sum of its two error terms. The evaluation width is
\(\eta_{\rm eval}=h/2\), with a total symmetric radius \(\eta_{\rm eval}/2\).

## Which allowance fails

Write \(L_1=aH/16,\ L_2=L_{\rm hat}/(16\delta)\) as in F5, and
\(C=2R^2/e_{\rm quad}\) as in F6. The record encloses the terms
separately and combines them by a base-two log-sum.

| Quantity | Directed enclosure |
| --- | --- |
| \(\log_2 L_1\) | \((6.2689,6.2690)\) |
| \(\log_2 L_2\) | \((5231.2791,5231.2792)\) |
| \(\log_2 C\) | \((21.5830,21.5831)\) |
| \(\log_2(C(L_1+L_2))\) | \((5252.8622,5252.8623)\) |
| \(\log_2(10^6)\) | \((19.9315,19.9316)\) |
| \(\log_2 e_F\) | \((-4544.5387,-4544.5386)\) |
| \(b_F\) | \((5245.8259,5245.8260)\) |

The lower endpoint for the prescribed count argument exceeds the cap
before taking a ceiling. The term \(L_2\) dominates through the coupling
of the F2 local-log tolerance to the F5 \(1/\delta\) factor. Even the
retained \(L_1\) term alone gives \(\log_2(CL_1)>27.8519\) at these
cutoffs. Reducing only the derivative term while retaining that kernel
term and cost factor cannot make the screen pass. The F7 node-error
allowance is about \(9.07\times 10^{-1369}\), derived using a total
positive midpoint weight at most \(R/8\). Its \(b_F\) is a resolution
diagnostic for the sufficient bound.

The [record][record] gives exact dyadic endpoints, individual center
requirements, rejected-search comparisons and execution time. The
[replay script][script] uses python-flint/Arb. The [author check][check]
documents the interval conventions and one correction to the presentation
of the rejected-search comparisons.

## Scope and controls

The negative result covers the Request18 **specified uniform-midpoint
sufficient allowance at this tuple**. Actual integration error, optimal
algorithmic cost, the signed Green value, and new zero exclusion are
unresolved. No field, \(U\), panels, primes or sibling census were evaluated.
The inherited E03 acquisition theorem and E05 acceptance govern the
existence claim. [Avoid07][scope] governs the negative conclusion.

For the analytical screen under [controls12][controls] and [avoid02][shape],
retain the premise map in [Note06 §9][acq], [Note07 §5][assess] and
[Note09 §5][b04]. The relevant distinctions for the frozen calculation are:

| Control class | Canonical premise missing or changed |
| --- | --- |
| Fixed/growing Euler factors | The conductor-one coefficients and exact prime baseline change. |
| Weighted squares, finite theta/zero tails and finite-prime orbits | They lack the complete normalized theta coefficients and reflection conjunction. |
| Reflected super-Gaussian, smooth shape and positive primitive | They lack the literal arithmetic square expansion and xi/zeta identity. |
| Fixed-event atoms and finite-profile variants, including continuous extensions | They lack the full coefficients and profile, with eventual simplicity absent where the source specifies it. |
| RH-conditional normalized endpoint perturbations | Ordinary Dirichlet-series arithmetic fails even with the preserved completion and functional equation. |
| Variable readouts and three-profile relaxations | Respectively the full physical cosine/Newman readout or the integer divisor and complete source constraints are missing. |
| Counter-kernels and smooth-density replacement | The counter-kernels lack the literal transform and anchor. The density replaces discrete primes by a continuous measure. |
| Two-channel exclusion | Its stated norm-factorization architecture and support are outside this recipe. |

Generic logarithmic and integration bounds can apply to other fields
with their own constants. A positive-time event stays at its own time.
Neither this allowance failure nor an eventual finite pass would give a
shape-based exclusion.

## Stop and continuation

E06 ends at the failed F5–F6 allowance with F1–F4 paid in the scalar
screen. [Continuation13][cont] proposes B05 to decide whether a
different local-log/integration estimate is worth pursuing against a
matched direct exclusion cost. It leaves B05 unissued and unactivated.

[request]: ../research-progress/handoffs/18_TND_OG_E06_SINGLE_TUPLE_FEASIBILITY_REQUEST_20261108.md
[record]: ../numerics/05_TND_OG_E06_DIRECTED_SCALAR_RECORD_20261110.json
[script]: ../numerics/e06_single_tuple_feasibility.py
[check]: ../reviews/09_TND_OG_E06_FEASIBILITY_AUTHOR_CHECK_20261110.md
[cont]: ../continuation-notes/13_TND_OG_E06_RESULTS_AND_MODEL_CHANGE_20261110.md
[acq]: 06_TND_OG_E03_COMPLETE_SIGNED_LOG_ACQUISITION_20261108.md
[assess]: 07_TND_OG_E05_ASSESSMENT_CALCULATIONS_20261108.md
[b04]: 09_TND_OG_B04_GREEN_MASS_RESOLUTION_AND_VALUE_DECISION_20261108.md
[results]: ../../../../../../result-summaries/README.md
[heat]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[target]: ../../../../../../avoid/01_restating_the_target.md
[shape]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[known]: ../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
