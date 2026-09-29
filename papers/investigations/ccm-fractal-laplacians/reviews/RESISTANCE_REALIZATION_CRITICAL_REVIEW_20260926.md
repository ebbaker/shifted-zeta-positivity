# Critical review: resistance forms and changing fractals

Date: 26 September 2026.

Model: GPT-6 (Codex). Exact variant and reasoning effort are not exposed.

Scope: same-agent adversarial review of the [initial note](../notes/CCM_RESISTANCE_FORMS_AND_CHANGING_FRACTALS_20260926.md) and [exact controls](../numerics/README.md). This is not independent peer review. Existing CCM notes were treated as working derivations; relevant primary-source pages were inspected directly.

## Strongest claim and verdict

The strongest unconditional model claim is that a compact weighted resistance tree can have frequency counting of order \(T\log T\), a trace-class inverse Laplacian, and compatible geometric approximants. It survives the checks below. Consequently a rejection of all fractal candidates based on the fixed gasket exponent would be invalid.

The strongest CCM claim is conditional: identifying **both** CCM forms with nested subspaces of a single grounded resistance system would turn their inverse trace into a geometric quantity and give trace-norm determinant convergence. The missing arithmetic identification is not supplied by the model. This is a useful target, not a solution of CCM's remaining hypotheses.

## 1. Compactness, finite mass, and domains

For \(r_n=n^{-a}\), \(0<a<1\), small arms accumulate only at the root, giving total boundedness and completeness in the path resistance metric. The measure has total mass \(\sum n^{-(2-a)}<\infty\). Total resistance length is infinite; compactness is not being confused with finite total edge length. The example therefore lies outside finite-total-length metric-graph Weyl estimates.

The full energy form is regular and Markov: on each interval it is the usual derivative energy, contractions decrease it, and finite-arm piecewise-linear functions approximate continuous functions. Finite energy gives continuity at the root by the resistance inequality. Grounding that root imposes a Dirichlet boundary condition. The resulting operator domain includes the weighted square-summability of the second derivatives, not merely an \(H^2\) condition on every separate arm. This summability is necessary for an infinite direct-sum operator.

The box-dimension calculation uses covering bounds in the resistance metric, whereas Hausdorff dimension one follows from countable stability on the constituent intervals. These are distinct geometric dimensions, and neither is being equated to the spectral counting exponent. The isospectral variation of \(a\) is therefore consistent with the stated dimension change.

The root boundary condition decouples the dynamics. Connected topology is not evidence of interaction between arms. This is a substantial limitation of the example as an arithmetic candidate and is stated in the note. There is no implicit Kirchhoff coupling. The construction is a resistance tree with infinitely many scales, not the standard self-similar fractal Laplacian.

## 2. Frequencies, trace, and arithmetic object types

The differential equation on arm \(n\) gives squared eigenvalues \(\pi^2(k+1/2)^2/(r_nm_n)\); \(r_nm_n=n^{-2}\) yields (5.3). Its normalized sine functions form a complete direct-sum basis. For any finite spectral window there are finitely many pairs, so no hidden finite accumulation of eigenvalues occurs.

The trace agrees in two calculations: integration of \(s\rho_n\) along arms, and summation of reciprocal squared frequencies. Both give \(\pi^2/12\). The cosine product converges normally because of the same reciprocal-square summability. The finite-arm inverse difference is positive with exactly the omitted-arm trace, justifying the trace-norm statement (5.8). This is stronger than finite spectral agreement.

Counting pairs \(n(2k+1)\le2T/\pi\) gives the difference of two divisor sums. The leading logarithm follows from the hyperbola identity; it is not inferred by fitting the computed values. Related divisor-counting quantum graphs are already in Endres–Steiner. No novelty or zeta-zero realization follows from this resemblance.

The model's spectral zeta function contains \(\zeta(2s)^2\), but the zeros of that meromorphic function are not eigenvalues of the underlying Laplacian. The note explicitly prevents this object-type error. Changing \(a\) leaves the entire frequency spectrum unchanged, further demonstrating why spectral agreement alone does not explain geometry or arithmetic.

## 3. Resistance trace theorem: hidden assumptions audited

The identity \(\operatorname{tr}\mathcal L^{-1}=\int R(x,o)d\mu\) uses the grounded Green kernel. It requires a genuine resistance form, a meaningful point boundary, dense definition in the chosen \(L^2\) space, and a closed form. Compact resistance diameter and finite mass give finite trace. The note states these requirements instead of asserting them for an arbitrary fractal or for the Weil form.

The zero-mass condition at the grounded vertex avoids a missing coordinate in the form domain. If several points are grounded, the relevant diagonal is resistance to that set. A general Dirichlet form in spectral dimension two or greater may have no bounded point evaluations and need not satisfy this trace formula. The proposition should not be extended to such forms without replacing its hypotheses.

The coercivity estimate concerns the positive Laplacian frequency ground value. It does not prove the original Weil ground energy is positive, even, or simple. The shift invariance \(W\mapsto W+cI\) prevents recovery of that sign.

## 4. Is the proposed CCM map circular?

The Gram identities (6.1) are necessary data, not an existence theorem. At finite dimension they restate the desired equality of two forms. The extra content comes from obtaining these identities in a specified geometric system with compatible maps, and then applying the geometric trace and projection estimates. Those requirements have not been shown for CCM.

The finite operator is a Galerkin Laplacian. Without invariance of the subspace it is not the restriction of the unbounded Laplacian. Abstract chiral doubling recovers signs of the finite frequencies but does not construct a local geometric Dirac operator or transport the spectral-triple algebra.

The prime contribution does have a direct jump-energy identity. The factor two and scalar offset follow from unitarity of translation on the zero-extended ambient line. This only treats the prime part, with the archimedean and pole terms still present. Turning its jumps into graph edges does not prove the full energy is Markov or define a compact resistance completion. Positive definiteness of the shifted Fourier matrices is weaker than all of these assertions.

No numerical eigenvalues, let alone zeta zeros, determine the shrinking-tree parameters. Nevertheless choosing a model merely for its desired counting order is not an arithmetic explanation; the note labels it as a positive control. The concrete next test begins with prescribed prime-power coefficients and would allow the chosen construction to fail.

## 5. Moving cutoffs and frequency dependence

The fixed-fractal counting obstruction assumes two-sided bounded pure-power estimates. It does not follow from a limiting spectral dimension alone. The tree has frequency dimension one with a logarithmic correction, and is the required control showing that the stronger blanket obstruction fails.

The common-space convergence proof fixes \(L\) and requires nested energy subspaces with one measure. Gasket computations use varying discrete measures and are not evidence of that hypothesis. Passing to growing support needs additional identifications and bounds; common names for different fractals supply neither. Uniform inverse traces give compactness of entire-function families but not uniqueness or identification with Xi.

The Fourier-compression defects are derived by compressing the same unshifted form and using the explicit inverse derivative. They obstruct the naive coordinate inclusion only when the ground shift changes, not arbitrary harmonic embeddings. A stable-ground surrogate gives exactly zero defects; an added lower even mode gives the predicted nonzero defects. Neither surrogate is represented as a CCM matrix.

The dynamic Schur complement is exact only away from interior poles, and its expansion needs \(|\omega^2|\eta<1\). With block-diagonal mass, the first derivative gives precisely the harmonic-extension mass. Higher powers are generally present and were checked with exact rational arithmetic. A massless-interior control eliminates them. Cross-mass terms would change the formula and have not been silently ignored in a general claim.

The determinant contains the eliminated interior factor as well as the boundary response. Similarly the original CCM determinant includes the untouched Fourier tail. The note retains its possible Gaussian joint-limit contribution. Neither finite geometric equivalence nor accurate low frequencies licenses removing those factors.

Finally, a decreasing *probe frequency* is distinct from a family whose lowest eigenfrequency tends to zero. The latter forces the reciprocal-square trace to diverge and defeats the proposed uniform determinant bound in that normalization. The converse implication is not asserted.

## Verification status and remaining gap

All finite controls passed with exact rational or integer arithmetic. The decimal presentation was recomputed at 32 and 64 digits. These computations distinguish mechanisms and check normalizations; they are not interval certificates for CCM or evidence of convergence of its arithmetic matrices.

The main unresolved task is to derive a compatible resistance geometry and mass measure from the full arithmetic pair, without inverse spectral fitting. Until that is done, the new tree and trace formulas are rigorous controls and conditional tools. The separate simple-even hypothesis and Xi identification remain open even if that geometric step eventually succeeds.
