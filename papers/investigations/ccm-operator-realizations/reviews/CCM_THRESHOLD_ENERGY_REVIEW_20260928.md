# Sequential adversarial review: threshold energy obstruction

28 September 2026 (America/New_York). Prepared for Edward Baker with explicit LLM assistance. Review model: GPT-6 (Codex); the exact serving variant and configured reasoning effort are not exposed to this reviewer. A separate agent read the completed analysis after its derivation. This is a same-model-family sequential adversarial review, not independent human refereeing or formal verification. No numerical experiment, repository edit, commit, or push was performed by the reviewer.

## Scope and disposition

The completed [round-9 analysis](../notes/CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md) was read in full and checked against the inherited weighted-operator proof, weighted-tail review, threshold-index handoff, and complement/weighted-gap note. The audit sought domain failures, reversed signs, unjustified endpoint interchanges, and stronger conclusions than the argument supports.

**No material mathematical flaw was found in the stated results.** The analysis supplies a scoped obstruction to bounded endpoint sandwiches and absolute relative-form control in the specified bare energy norm. It does not exclude a one-sided upper bound, establish RH, produce an RH counterexample, or obstruct every physical threshold compression. The review is complete rather than provisional.

The arithmetic radical identity and the literal Xi normalization remain inherited research inputs. Their use and compatibility were checked; this review is not a fresh independent proof of the complete Weil criterion or every earlier arithmetic identity.

## Checks of the inherited operator input

The form domain `av in H_log` is closed with the physical L2 norm added. Compact cutoff followed by local mollification gives the stated core, even though a tends to zero. Local compactness follows from the logarithmic Fourier weight and the positive lower bound for a on a fixed compact interval. The weighted-prime norm tail then gives relative form compactness; no individual weighted shift is treated as compact on ordinary L2.

The exact threshold vectors are in the physical form domain and satisfy the operator eigenvalue equation by the polarized radical identity. Their closed physical span is reducing for H. Removing that span or the ground vector preserves the physical form domain. These facts do not require the known span to exhaust the threshold eigenspace.

A small domain distinction remains worth preserving in future use: closedness of the maximal jump-difference map alone establishes equality with the integral expression on the constructed core closure, not automatically equality of that closure with every possible maximal finite-energy domain. The sandwich-form/core proof supplies the particular domain actually used here, so this distinction does not affect round 9.

## Checks of the new results

| Claim | Adversarial check and conclusion |
|---|---|
| Exact ground removal | X is reducing for H, and the restriction of the positive a-form to V intersect X is closed and dense. Its associated operator A_X need not be obtained by an unjustified ordinary compression of A_0. B_X=A_X-C_X is valid in form sense. |
| Compact reduced family and count | Relative form compactness passes through the bounded inclusion of the restricted form space. The bijection `(A_X+delta)^(1/2)` from that form space to X gives signed inertia. The removed zero mode contributes exactly one for every `0<delta<s`. No sign assumption on C_X is used. |
| Energy density of threshold profiles | The even complex translation family is locally holomorphic into H1, hence into E, in the strip. An annihilating continuous functional has Taylor series equal to a multiple of cosh(z/2). Its boundedness on real translates forces that multiple to vanish. The Fourier product is L1 by weighted Cauchy–Schwarz; Fourier uniqueness and isolated real Xi zeros then force the functional to be zero. This is density in E, not physical L2 completeness. |
| Positive compact witness | Choosing support diameter below log 2 removes every prime autocorrelation exactly. The explicit correction imposes the cosh moment exactly and evenness removes the other pole moment. The two high-frequency packets give `(1/2)||phi||^2 log T+O(1)` for the gamma form; the rapidly vanishing correction does not alter positivity. |
| Residual sequence | Each residual divided by a is a physical form vector: it is a compact smooth vector minus a finite exact threshold combination. The moment remains zero. Radical pairings give exactly `b[v_n]=q>0`, while energy density gives `a[v_n] -> 0`. The signed C_X quotient therefore tends to minus infinity. |
| Endpoint spectral limit | For any desired negative level, first choose one fixed physical residual vector and only then take delta sufficiently small. Its denominator is `a[v_n]+delta||v_n||^2`. This proves the assertion for every sufficiently small delta, not merely along a selected sequence. No operator monotonicity is assumed. |
| Every fixed prime cutoff | The finite unweighted translation sum is bounded on L2. Applied to the energy-small residuals, that finite sum and the local multiplication term vanish, leaving tail expectation tending to `-q`. This proves the stated negative divergence for each finite P. It does not permit P to vary inside that limit. |
| Physical threshold projection | The closed known span Z is contained in the kernel of B_X, so its orthogonal projection preserves the physical form domain. On the residual sequence the Y projection is a fixed nonzero vector of positive a-energy. Hence that projection cannot be bounded in the bare energy norm. The zero quotient seminorm is a consequence of energy density. |
| Crowding and bounded-rank approximation | On each fixed finite-dimensional threshold subspace, a has a strictly positive minimum on the physical unit sphere. Congruence maps it to a trial space with Rayleigh quotients at least `alpha/(alpha+delta)`. Signed compact min–max supplies the positive eigenvalue count. Intersecting an `(r+1)`-dimensional trial space with the kernel of an arbitrary rank-at-most-r approximant proves the norm-error lower bound, even if the approximant depends on delta. |

For the analytic-density proof, uniform theta bounds are needed only on compact subsets of the complex strip: bounded real part of the translation parameter and imaginary part bounded away from plus or minus pi/4. The reviewed draft called these a “compact substrip”; the final analysis spells out the compact-subset condition in response to this review. This is a wording clarification, not a change to the proof.

## Endpoint ledger and quantifiers

The prime schedule in the ledger is valid: its exponential factor supplies `delta^(1+kappa)`, leaving `tau(P(delta))/delta -> 0` despite the polynomial prefactor. It does not conflict with the theorem for every fixed P.

The spatial schedule is also valid. With `exp(2R)=L log(1/delta)` and `cL>1`, the inherited e_R bound divided by delta tends to zero, and d_R/delta does as well. The note correctly retains the distinction between eigenfunction tail mass and an all-vector operator error.

The frequency inequality follows immediately from the Fourier weight. It controls f=av, and the note does not incorrectly convert it into a bound on v or the full prime form. Recovering v, preserving the exact moment, and controlling cross terms still require additional estimates.

Ground removal has no coupling error on the H side. Threshold removal is likewise exact for B_X, but it does not separately diagonalize A_X and C_X. The ledger correctly refuses to infer error estimates for approximate threshold projections from energy density.

The crowding result rules out a positive margin below one that is independent of delta, and rules out arbitrarily accurate uniform approximation by a fixed bounded rank. It does not prove that any of the crowded eigenvalues exceed one. Adaptive rank, one-sided comparisons, or new estimates after complete physical compression remain outside the obstruction.

## Decision

The recommendation to suspend this particular bounded-sandwich/absolute-relative-tail route is justified. The negative spectral divergence is compatible with the desired upper bound `S_delta <= I`; confusing the two signs would invalidate the research conclusion, and the analysis explicitly avoids that error.

Further work should require a concrete one-sided form estimate or a justified comparison on the physical complement Y, including its actual arithmetic and projection errors. The saved analysis meets the handoff's bounded completion rule without a numerical sweep or a claim to have resolved RH or the CCM determinant problem.
