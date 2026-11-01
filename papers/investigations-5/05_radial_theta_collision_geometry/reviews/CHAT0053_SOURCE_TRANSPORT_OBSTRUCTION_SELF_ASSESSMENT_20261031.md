# Source transport zero obstruction self assessment

31 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, effort **xhigh**, Investigation05 chat0053.

**Disposition: proved in-note, checked by the same assistant; no independent or specialist review.** This assessment covers [the source-transport proof](../notes/CHAT0053_SOURCE_TRANSPORT_UNBOUNDED_STRIP_OBSTRUCTION_20261031.md). It is not an E02 assessment of R11.

The concrete result is that the exact source-only radial transport with the raw exterior initialization and fixed logarithmic cosine observation has zeros of unbounded imaginary part at every fixed nonzero finite positive or negative time. Merely recentering the observation has the same failure. The theorem is stronger than an unsuccessful strip estimate: it contradicts every bounded-strip conclusion for these families.

## Mathematical checks

1. **Sign and normalization.** Equation \(\partial_s\rho=\operatorname{div}(v\rho)\) uses characteristic velocity \(-v\). With \(y=r^2\), \(y'=-2y(y+2)/(y+1)\), so \((y(y+2))'=-4y(y+2)\), giving the stated radius. The factor \(4\pi r^2dr/(8\pi r^3)=du\) confirms the raw source and spectral transform. Reversing time is included because the characteristic is complete.

2. **Endpoint and inverse.** \(a_s=\chi_s(0)\) vanishes only at zero time. The inverse is \(\chi_{-s}\), and \(\chi'_s=b(\chi_s)/b\) is positive. Thus \(q_s(a_s)=\Phi(0)/\chi'_s(0)>0\). This is a genuine one-sided source edge; no assertion that the transported source remains smooth after even reflection is used.

3. **Complete tail.** Differentiated theta modes satisfy the displayed summable estimates. Fixed finite flow time changes the logarithmic coordinate by at most \(|s|\), and the inverse derivatives are bounded. This pays every exponentially weighted derivative integral used in integration by parts. No finite truncation or numerical error enters.

4. **Integration by parts.** The signs in the first two terms are both negative: \(-q(a)\sin(az)/z-q'(a)\cos(az)/z^2\). The weighted \(q''\) norm bounds the remainder uniformly in each fixed horizontal strip. This uniformity is needed; a real-axis expansion alone would not prove the strip statement.

5. **Zero counting.** Fixed disjoint disks about the sine zeros fit inside any strip of positive width. Rouché gives one zero counted with multiplicity per distant disk; conjugation then forces it to be real and simple. A uniform lower bound for sine outside the disks excludes omitted distant strip zeros. The smaller \(O(1/n)\) displacement follows by evaluating the error at the zero, rather than assuming uniformity in shrinking disks. The count \(N_+(R)=|a_s|R/\pi+O_s(1)\) follows.

6. **Growth.** The gamma-integral upper bound proves order at most one. Positivity on arbitrarily far intervals proves infinite exponential type; the explicit first-mode interval supplies the sharper \((y/4)\log y+O_s(y)\) growth and exact order one. These arguments do not assume a physical mass margin or RH.

7. **Factorization.** If there were only finitely many nonreal zeros, order-one Hadamard factorization allows only a degree-one exponential. Pairing positive/negative zeros gives an even product, and evenness removes the linear exponential. The finite nonreal factor is an even polynomial. The counting integral bounds the remaining product by \(e^{O_s(y)}\) on the imaginary axis. This contradicts the independently proved infinite type. This step does not infer finite type from order one alone; the linear zero count and paired symmetry are essential.

8. **Unbounded imaginary parts.** Infinitely many nonreal zeros by itself would not suffice. The separate result that every fixed strip contains only finitely many nonreal zeros completes that implication.

9. **Recentered variant.** The derivative formula uses \(\Phi'(0)=0\) and \(b'(a)-b'(0)=\tfrac12\tanh^2(2a)>0\). Therefore \(q'(a)<0\) whenever \(s\ne0\). Weighted third derivatives give the strip-uniform nonoscillatory leading term \(-q'(a)/z^2\), leaving finitely many zeros per strip. Infinite type excludes finitely many total zeros. The recentering is a changed observation, not part of the original fixed-observation theorem.

## Scope and provenance

The antecedent method is the finite-source endpoint/growth obstruction in [Investigation3/07 round-two Note01, Section3](../../../investigations-3/07_source_measurement_audit/notes/round-2/01_REVIEW_RECONCILIATION_AND_ENDPOINT_NONREALITY_CODEX_20261017.md). The moved endpoint here leaves a sine sequence of real zeros, requiring the additional paired-product count. Hadamard's classical theorem was checked in the selected primary teaching source recorded in [reference20](../references/20_HADAMARD_FACTORIZATION_AND_TRANSPORT_SCOPE_20261031.md). No novelty survey or full review of that reference's proof was performed.

The result is a scoped obstruction, as required by [avoid07](../../../../avoid/07_scoped_exclusions_read_as_universal.md). It does not decide the zeros at \(s=0\), the physical heat collision problem, the energy-normalized flow, or other source generators. The control screen in the proof identifies which analytic premises the source controls pass or fail; no special arithmetic separation is claimed.

No bound is uniform as \(s\to0\), and no numerical location or zero trajectory is supplied. Local uniform convergence to the initial function is compatible with the failure occurring arbitrarily far out. The odd-velocity modification at the end of the note removes this endpoint obstruction only; zero-location control for that different family remains open.

**Verification performed:** analytical recomputation of the characteristic, endpoint derivatives, strip expansion, Rouché argument, growth, and product estimate. No floating experiment is needed for this conclusion and no numerical certificate is claimed. A separate assessor should focus first on strip-uniform endpoint integration and the use of even order-one factorization.
