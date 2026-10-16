# Audit: finite-place thermal radiation interface

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Reviewer/model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Review type:** same-assistant mathematical and numerical audit, not an independent specialist review.

**Artifacts:** [research note](../notes/FINITE_PLACE_RADIATION_INTERFACE_TEST_20260923.md), [diagnostic](../numerics/check_finite_place_interface.py), [144-case record](../numerics/records/finite-place-interface-20260923.json).

## Assessment

The stated boundary model is sufficiently explicit to test: its thermal preparation, unchanged primitive controllers, loop geometry, unitary vertex, interconnection, initial state and coherent readout are all specified. Solving these equations produces the measured response and an ordinary energy identity. The model fails the arithmetic repetition ratio and front tests.

The more consequential result is separate from that model: the unchanged full archimedean factor multiplied by a finite Euler product has an uncancelled right-half-plane pole for every \(0<\beta<1\). It cannot be a passive causal scalar response with the required norm. This corrects a potentially misleading literal reading of the previous finite-place proposal without invalidating the thermal coefficient identity or the full modular half-shift benchmark.

## Checked arguments

1. **Finite-place preparation.** The Hamiltonian has two unbounded occupation ladders but a finite number of prime places. Its Gibbs trace converges for every positive beta. The primitive projectors are the occupation-zero projections. Their states are not truncated or analytically continued in the mathematical model.

2. **Physical delay assumption.** The chosen line element \(dy/y\) on the multiplicative interval \(1\le y\le\ell\) gives length \(\log\ell\); unit-speed transport then gives that actual delay. The note identifies this geometry as an added model assumption. It does not infer a flight delay from the thermal Hamiltonian's energy label alone.

3. **Boundary coupling.** The real vertex matrix squares to the identity and is unitary. Its primitive-controlled direct sum with the bypass is also unitary and commutes with the occupation Hamiltonian. A disconnected nonprimitive loop is initially empty. No reset occurs on repeated paths, so the primitive probability appears once, not once per traversal.

4. **Derived transfer.** Eliminating the loop fields gives \(F_\ell=(z_\ell-r_\ell)/(1-r_\ell z_\ell)\). Its poles have negative real part when \(0<r_\ell<1\). The Gibbs average is \(q_\ell+(1-q_\ell)F_\ell\); the product of the two averages is justified by the product preparation and the commuting static controllers. This is a mean amplitude, not an inclusive intensity.

5. **Coefficient normalization.** The raw direct coefficient is \(g_1=d_2d_3\), not one. The note therefore gives both raw and formally normalized echoes. The decisive repetition ratio \(g_4/g_2=r_2\) is unchanged by that normalization. At beta one, the normalized first echo is \(3/2\) and its omega tangent is \(12\log2\), against the target \(1/2\) and \((3/2)\log2\). The normalization is not claimed to preserve contraction. The normalized composite does multiply correctly; the note does not call this a failure of multiplicativity.

6. **Energy accounting.** Vertex flux minus external output is exactly the derivative of ordinary loop storage. Cascading cancels the intermediate port flux. Thermal averaging decomposes inclusive output into squared coherent mean and nonnegative signal variance. The variance is physically outgoing signal energy correlated with the controller; it is neither absorption nor an unexplained auxiliary flux. The same identity works on each finite window. Loop storage tends to zero after a finite-duration input as time grows.

7. **Identity endpoint.** Convexity and the bound \(\|F_\ell-I\|\le2\) yield norm convergence of the measured response to identity as beta tends to zero. This is consistent with the spreading Gibbs state: a response limit need not require a trace-class state limit.

8. **Fixed bounded readout proposition.** Uniform convergence of the diagonal Gibbs series on compact subsets of the beta right half-plane gives holomorphy. Equality on any real open beta interval then extends throughout that connected half-plane. Real positive-temperature expectations stay bounded by the fixed operator norm, while the centered coefficient diverges for beta tending to infinity. The scope requires a fixed bounded observable in the specified native state. It does not automatically apply to coefficients extracted by a temperature-dependent archimedean deconvolution, to a modified boundary dynamics, or to the full completed quotient.

9. **Completion pole.** At \(p=(1-\beta)/2\), \(s_+=1\) and \(s_-=1-\beta\). For \(0<\beta<1\), all gamma and Euler factors in the residue are finite and nonzero; the rational denominator has a simple zero. The resulting residue has the sign and normalization stated in the note. A passive causal scalar multiplier must be bounded and holomorphic in that half-plane, so it cannot have this pole. Extra zero-input passive output ports do not help because a measured block remains a contraction. Causal unstable responses are explicitly outside this exclusion's energy requirement.

10. **Global cancellation and endpoint.** The zero of \(1/\zeta(s_+)\) cancels the pole in the full quotient, giving \(2\xi(1-\beta)\) locally, without any assumption on nontrivial zeros. This does not prove full-family passivity. At beta one, the finite two-prime completion instead has a cubic boundary pole with coefficient \(-2/(3\log2\log3)\), whereas the full half-shift quotient has value one at zero. Adding finite primes cannot mimic analytic continuation near the pole.

11. **Finite-window correction.** A causal archimedean kernel convolved with matching initial Euler delays agrees before the first omitted prime delay. Its support follows from the beta-integral gamma kernel and the causal inverse of the rational factor; support is not passivity. A two-prime truncation first misses label 5, before label 6. The note therefore includes prime 5 for a full scalar window through log 6, while retaining the distinction from a path-resolved two-loop measurement.

## Numerical audit

The completed run has **144 passing floating controls** at 60 decimal digits using Python 3.10.0 and mpmath 1.3.0. No interval or exact-arithmetic certificate is claimed.

The program independently solves the loop boundary equations and evaluates occupation sums with a tail bound. Its time-domain diagnostic constructs paths from the boundary recursion and integrates overlaps of translated box pulses; it does not evaluate output energy from the asserted conservation identity. The variance is integrated from sector deviations rather than defined as a residual chosen to close the balance.

Checks cover the four pure controller sectors, five observation windows, three temperatures, complex-frequency readouts, coherent-versus-inclusive output, repetition and tangent failures, finite-product residues for three finite prime sets, the regular full-xi comparison and the half-shift boundary asymptotic. The fixed-readout proposition and the global pole obstruction are analytical arguments; numerical samples only check their formulas.

The record includes a SHA-256 identity for its generating program. The program uses no sibling implementation, external zero table, or downloaded numerical dataset. Large generated data are not needed. Earlier suites were not rerun merely to increase the case count.

## Remaining boundary

There is still no physical realization of the completed variable-shift response. This test supplies a valid but arithmetically unsuccessful radiation coupling, and shows why the literal finite Euler completion is an unsuitable global passive target. The revised next question is a joint boundary dynamics that preserves the global cancellation, with the existing modular one-form response as a benchmark. A finite-time comparison can be useful, but cannot substitute for deriving that dynamics.

Manuscript TeX and PDFs are unchanged by this addendum. Supporting indexes and file-identity records are updated to identify the new artifacts; the manuscript build is not reported as rerun.
