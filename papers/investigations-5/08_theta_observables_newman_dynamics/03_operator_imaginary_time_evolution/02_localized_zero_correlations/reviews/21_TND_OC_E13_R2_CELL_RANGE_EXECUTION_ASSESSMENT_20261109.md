# E13 r2 proof and execution assessment

9 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex assistance, OC chat0010. Recorded thread GPT-6.1 Sol /
ultra. Per-turn backend and helper settings are unavailable. This is
an internal execution assessment with shared source premises.

**R1–R6 passed. The fixed projected value is certified at the inherited
winding scope.** [Request29][request], [Note22][range] and [execution23][run].

| Check | Disposition |
| --- | --- |
| R1 | Exact trace geometry gives 388 occupied singleton cells, \(u=5/32768\), \(v=15/131072\), and adjacent real gap \(5085/8192>1/2\). Summing the \(k\) gaps and nonnegative intervening widths gives index-\(k\) distance greater than \(k/2\). |
| R2 | The erf difference takes opposite extrema for its two terms. The positive gap range orders its exponential endpoints. Exact rational squared distances to both mark centers give the four mark endpoints per cell. Cross-cell sums retain both ordered mark products. The clipping uses definite Arb comparisons for resolved cases and maps both exact endpoint bounds in unresolved cases. |
| R3 | For \(q_k=e^{-k^2/16}\) the center, gap and ordered mark widths are at most \(2u/T,4u q_k,2v\). Product telescoping gives \((10u+4v)q_k/T\) per ordered pair. The \(2(N-k)\) pairs per index gap and the integral bound \(\sum q_k<2\sqrt{\pi}<4\) give ideal radius strictly below \(1261/409600\). The bound uses the acquired singleton separation. |
| R4 | Distinct cells have coefficient \(n_Cn_E\) per order. One cell has \(n_C(n_C-1)\) times a range over its full Cartesian square. Its coefficient vanishes in the certified census. Synthetic real and imaginary splits test the full square. |
| R5 | Each outward ball edge can lie up to twice its radius from the ideal endpoint. This charges \(r_L+r_U\) in the final radius. With the \(2^{-32}\) tail, the predeclared cap is \(2189688957/536870912000<41/10000<1/200\). The actual serialized radius and arithmetic allowance passed their exact rational gates. A separate source-free post-run read reconstructed the same endpoints from the saved dyadics. |
| R6 | All authorized input digests passed. The 221,300,387-byte trace had both required hashes. Exact partitions, leaves and counts matched the prior receipt, with 11,694 accepted splits. The 28 fixtures passed, including rigorous containment of the 256-bit ordered point reference and rejection of missing mark order, omitted same-cell term, nonfinite balls and both numerical boundary failures. The single worker stopped at the first successful canonical pass, in 7.77 seconds, with 452,204 total exp/erf calls and 37 pi/sqrt calls. |

The software controls compared exact point selections at cell corners
and interior points using outward reference balls wholly contained
in the evaluator intervals. Two mutation tests made the resulting
ranges disjoint from the reference balls. The separate evidence
checks rejected malformed geometry, noninteger multiplicity and
corrupted bytes. These are acceptance checks for the implemented
range evaluator. The source-free trace check imports the r1 assessed
outward windings. [R1 assessment][r1].

The selected python-flint 0.9.0 ball APIs were checked with the
installed runtime. Finite endpoints use the exact midpoint and
radius representation, so the radius test does not depend on
rounded decimal displays. The exact transcendental inputs use
dyadic points or outward rational conversions. [python-flint 0.9.0 Arb documentation](https://python-flint.readthedocs.io/en/stable/arb.html)
and [arithmetic source-use record][source].

## Collision-control premises

The [control inventory][controls] applies at the premises of the
finite measurement. Euler-factor changes lose the unchanged
theta/zeta source. Weighted-square, finite-tail and finite-prime
controls lose full normalized reflection or complete unit coefficients.
Reflected super-Gaussian, smooth shape and positive-primitive controls
lose the complete theta expansion. Atomic and finite-profile threshold
controls lose complete theta growth/profile. The theta-close
normalized endpoint control loses ordinary Dirichlet-series arithmetic.
The variable observation kernel loses the physical cosine/Newman
equation, which is separate from snapshot interval inclusion.
Fractional profiles lack a realizable integer-labelled divisor.
The tests retain collisions, complex marks and multiplicities
where those appear in an input. This is a finite projected enclosure
with its exact source and count premises. [Note22 §6][range] and
[scope rule][scope].

[request]: ../research-progress/handoffs/29_TND_OC_E13_R2_CELL_RANGE_EVALUATOR_REQUEST_20261109.md
[range]: ../notes/22_TND_OC_B10_R3_CELL_RANGES_AND_GAUSSIAN_WIDTH_20261109.md
[run]: ../numerics/23_TND_OC_E13_R2_EXECUTION_20261109.json
[r1]: 17_TND_OC_E13_R1_PROOF_AND_IMPLEMENTATION_CHECK_20261109.md
[source]: ../references/16_TND_OC_B10_R3_CELL_RANGE_SOURCE_USE_20261109.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
