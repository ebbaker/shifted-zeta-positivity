# Review of the genuine signed heat continuation

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model read-throughs are internal checks, not independent
mathematical validation.

## Outcome and scope

The next bounded input after [Heat Note 8](../newman_collisions/notes/8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md)
now has two actual-phase estimates and a stronger relaxation obstruction.
The complete pointwise collision inequality is still open.

[Heat Note 9](../newman_collisions/notes/9_GENUINE_SIGNED_EDGE_CANCELLATION_AND_AVERAGED_PROBES_20261009.md)
removes the last \(\lfloor N^{3/4}\rfloor\) terms with explicit signed
value and scaled derivative payments \(40N^{-1/24}\) and
\(800N^{-7/24}/L\). These estimates hold throughout the stated range
\(1\le\kappa\le2\), \(0<t\le1/20\); their useful decay is asymptotic.
The core reduction pays the existing full analytic error first, then
subtracts the exact tail. It does not substitute a large positive error
majorant at the reduced cutoff or differentiate a jumping integer cutoff.

The same note proves positive mean square for the complete genuine
approximant and exact normalized heat function on the sufficient translated
range \(H_p=DLe^{2\mathfrak a/t}\), with an existential absolute \(D\)
and sufficiently small uniform time. The normalized mean squares are at
least \(1/4\) and \(1/8\), respectively. The last near-zero-frequency term
is restored before the final theorem. Physical phase and amplitude
variation, the symmetric normalizer, reflection, local complex-disk
remainders, and all possible cutoff corrections are paid. No mean-square
bound on one complex disk of radius \(H_p\) is assumed.

[Heat Note 10](../newman_collisions/notes/10_COMPLETE_MULTIPLICATIVE_PHASE_OBSTRUCTION_20261009.md)
proves an exact zero of the complete twisted joint vector for some
completely multiplicative unit-modulus twist at each sufficiently small
parameter point. It preserves all coefficients, composites, local amplitude
derivatives, derivative frequencies, and the leading phase. It strengthens
the independent-phase obstruction; it does not give an actual heat collision.
The twist can depend on the parameter point and is not shown to arise from
the genuine height orbit. No twisted heat-function remainder theorem is
asserted.

## Proof and dependency checks

The edge proof uses the explicit third-derivative estimate in
[Arias de Reyna, equation (2)](https://arxiv.org/html/2407.02094v1).
Its three terms and short-interval exception are retained. On the actual
edge, \(1/N\le f'''\le4/N\); the upper comparison uses
\(T/\pi\le2.01N^2\), which is sufficient with \(K\ge.9N\).
Partial sums are bounded by \(18N^{7/12}\). The exact coefficient and
complex multiplier variation ledgers then give the stated 40 and 800
reserves. Raw value and derivative errors have factors 80 and 400;
they must not be confused with the scaled coordinates.

The logarithmic-phase exponent-pair calculation is an upper-bound-method
budget. The endpoint requires \(p+q<1/2+\kappa/8\). The explicitly surveyed
hull in [Trudgian--Yang, Section 1.4](https://arxiv.org/html/2306.05599v3)
has minimum sum \(17/21\), which misses the threshold. This statement is
restricted to that cited hull and its closure. A growing upper bound
is not a lower bound on the true signed sum and does not rule out other
arithmetic mechanisms.

For the averaged theorem, the exact phase center matches the continuous
cutoff through its \(t\pi/(8x)\) term. Removing only the final term during
the intermediate estimate prevents division by its possibly near-zero
frequency. All difference-phase terms cost \(O(Le^{2\mathfrak a/t})\)
and all sum-phase terms cost \(O(e^{2\mathfrak a/t})\), including the
oscillatory diagonal. The first coefficient supplies a constant diagonal
floor. The complete frozen sum, and then the physical sum, are restored
using normalized \(L^2\) triangle inequalities. The freeze loss is
\(O(L^2e^{(5\mathfrak a-\kappa)/t})=o(1)\) since
\(5\mathfrak a-\kappa\le-1/16\). The small extension of the translated
parameter past \(\kappa=2\) is justified by strict ledger reserves;
only a uniform absolute prefactor is needed.

The complete curvature budget is \(|Q_t''|\le C_2e^{\mathfrak a/t}\),
including Cauchy remainder derivatives at translated centers. At a
candidate double zero it yields
\(H^{-1}\int_0^H(Q_t(x+y)/2)^2dy\le M_2^2H^4/80\).
This budget can contradict a constant mean-square lower bound only on a
scale of order \(e^{-\mathfrak a/(2t)}\), far shorter than the sufficient
range proved here. This is a deficit of this average plus absolute Taylor
conversion, not a necessary probe range theorem or a lower bound on actual
curvature at a collision.

The multiplicative proof retains the complete residual and annihilates
its cross terms by Haar orthogonality and unique factorization. Its second
moment is less than seven. The isolated primes \(N/2<p\le3N/4\) affect
only their own terms inside the cutoff. Their weighted mass, obtained by
partial summation from the classical
[prime number theorem](https://dlmf.nist.gov/27.12#E4), supplies a diverging
two-coordinate reservoir. Three cyclic groups have vanishing preconditioned
matrix discrepancies. The explicit contraction reserves then solve the
exact vector equation. Phase approximation alone does not transfer this
zero to a genuine height: the weights, cutoff, normalizer, carrier phase,
and derivative data also move.

The inherited analytic approximation input remains Polymath's effective
Riemann--Siegel theorem plus the manuscript's disk/reflection deductions.
No conjectural zeta estimate or numerical zero information is imported.
Literature novelty is not claimed; these proofs require external specialist
review before use as established research results.

## Reproducible finite record

The [standard-library checker](../numerics/check_genuine_signed_heat_input.py)
and [record](../numerics/genuine_signed_heat_input_record_20261009.json)
contain 186,693 passing exact assertions. Two fresh runs reproduce the
retained JSON byte for byte, with a SHA-256 binding to the checker source.
The checks cover polynomial exponents, third-derivative and Abel scalar
reserves, the cited hull's rational vertices, contraction margins, finite
monotone cyclic partitions, isolated primes, and formal prime-exponent
orthogonality at cutoffs 64, 128 and 256.

These are finite arithmetic checks. They certify neither imported analytic
theorems nor asymptotic prime counts, phase evolution, a huge-height heat
calculation, the complete local lower bound, collision exclusion, or RH.
The assertion count should not be read as independent mathematical evidence
for the analytic limits.

## Next admissible input

The remaining target is a uniform local signed lower bound for the actual
complete vector, or its paid retained core, conditional on both collision
coordinates being small. The explicit core thresholds in Note 9 give a
reviewable interface. Averaging alone and a lower bound valid for every
multiplicative twist do not supply that input by the mechanisms tested here.
A successful continuation must retain the genuine height correlations or
provide a sharper local-to-average transfer conditioned on a collision.

The stable manuscript is unchanged. This continuation adds notes, the small
calculation record, indexes, and a concise history entry, with no snapshot
folder, Git commit, actual collision, RH assertion, or novelty claim.
