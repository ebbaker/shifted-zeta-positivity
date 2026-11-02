# MC06-E01: separate review of the circle SUSY response and protected-class obstruction

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewer `/root/review_ward_susy`, actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**. Verified from reviewer rollout session `01a19a55-0995-7e60-9282-84ec086e4d16`, turn `01a19a55-09a9-7cc0-9daa-fd9f2055fd75`. This is fixed **E — execution**, request r1. The reviewer owns this file only and has not changed the frozen return.

**Disposition: accept the exact spectral/observable dictionary, the nonzero graded Ward residual, and the scoped fixed protected-insertion obstruction.** Section 2 below makes the closed operator domains explicit; it is a clarification of the return's sufficient common-core convention, with no change to any displayed source or Ward formula. The result is a useful unprotected physical formulation and a precise failure of the selected protected class. It supplies no Mellin estimate, new determinant sign or universal obstruction to topological approaches.

This is a different-worker, different-model **internal LLM review** of Astra/ultra work. The author's configuration was checked in its own rollout. Both passes share the unchanged canonical source, accepted source/sign baseline and inherited normalization; this is not independent specialist review. No second theory, new candidate or numerical campaign was introduced.

## Frozen inputs and evidence

The [r1 checking request](../numerics/MC06_E01_REVIEW_REQUEST_R1_20261101.json) fixes the [MC06-B01 return](../notes/01_PROTECTED_OBSERVABLE_FEASIBILITY_RETURN_20261101.md). Its bytes were checked at entry and after review:

| Input | SHA-256 |
| --- | --- |
| MC06-B01 return | `bb9590f2dcecc46665574d25e221eba19224bec86a0d31ad10355a6361496b34` |
| Launch manifest | `501acdcfa663b5eb4959c348095a4e79c70053907660b599f3585862a526f60a` |
| Initial Mellin assessment | `ee4280708b43d4d080fe98c128d58c0180f0ba0851b730bd859c2a899f84d9de` |
| Accepted source/sign Review01 | `c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe` |

The launch's mathematical baseline hashes still match. Live progress-register changes were not absorbed as mathematical premises. The author configuration was verified for session `01a19a49-e72d-7902-8f13-adf50b8aa74f`, turn `01a19a4f-2ad8-7863-9b61-978dfd7e15fb`: **gpt-6-astra / ultra**.

The review follows the [result index](../../../../../../../result-summaries/README.md), especially [physical channels](../../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md), [theta identities](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../../../avoid/README.md), especially [target reformulations](../../../../../../../avoid/01_restating_the_target.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [shared-premise checks](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [normalization](../../../../../../../avoid/08_normalization_and_constant_slips.md) and [unchecked imports](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## 1. Exact Fourier-block calculation and source match

Use normalized states `|n,0⟩=e^{inx}/√(2π)` and `|n,1⟩=e^{inx}dx/√(2π)`, for every integer `n`. On their two-state block, in degree order `(0,1)`,
\[
Q_n=\begin{pmatrix}0&0\\i\sqrt\pi n&0\end{pmatrix},\quad
Q_n^\dagger=\begin{pmatrix}0&-i\sqrt\pi n\\0&0\end{pmatrix},\quad
H_n=\pi n^2I,\quad N_n=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]
Thus `Q²=0`, `{Q,Q†}=πΔ` and all degrees and energy scales agree with the return. At `n=0` both states are harmonic and both are removed by `P_exc`. Each positive energy has the two modes `n,-n` **in each degree**; the harmonic eigenspace has only one state in each degree. No degeneracy is omitted.

For `β>0`, `y^N=diag(1,y)` and the excited trace is
\[
\mathscr Z_{\rm exc}(\beta,y)
=(1-y)\sum_{n\ne0}e^{-\pi\beta n^2}.
\]
This is an actual degree-one polynomial in `y`. Differentiation at `y=1` therefore gives
\[
-\partial_y\mathscr Z_{\rm exc}|_{y=1}
=\vartheta(\beta)-1
=\operatorname{Str}(-NP_{\rm exc}e^{-\beta H}).
\]
The minus sign in `O=-NP_exc` and the two copies `n,-n` are both needed. The protected denominator is zero; no normalized expectation is available or used.

For any twice differentiable scalar `Θ`, the chain rule with `β=e^{4u}` yields
\[
\frac18(\partial_u^2-1)\left(\tfrac12e^u\Theta(e^{4u})\right)
=e^u\left(\beta^2\Theta''+\tfrac32\beta\Theta'\right).
\]
With `Θ=θ-1`, each pair `n,-n` contributes
\[
e^u(2\lambda_n^2\beta^2-3\lambda_n\beta)e^{-\beta\lambda_n},
\qquad \lambda_n=\pi n^2,
\]
which is exactly the stated complete canonical source. The operator reconstruction has the correct `H²` and negative `(3/2)H` terms. Harmonic constants would be killed by this reconstruction, but the explicitly subtracted trace is the one actually matched. There is no primitive/source or factorial substitution.

## 2. Domains and legitimate trace operations

The return's periodic `H¹` convention is sufficient as a common Sobolev domain for its first-order core calculations. To specify the **closed** de Rham operators precisely, use
\[
D(Q)=H^1(S^1;\Lambda^0)\oplus L^2(S^1;\Lambda^1),
\]
\[
D(Q^\dagger)=L^2(S^1;\Lambda^0)\oplus H^1(S^1;\Lambda^1),
\qquad D(H)=H^2(S^1;\Lambda^0\oplus\Lambda^1).
\]
Taking `H¹` in both summands describes a common core, not the full closed domain of either nilpotent operator. Fourier polynomials are a common invariant algebraic core and their graph closures give the operators above. On this realization `Q²=0` is also a domain-valid assertion: `Qf` has only degree one and automatically lies in `D(Q)`. This clarification prevents reading the sufficient-domain shorthand as a claim about maximal domains; it does not alter the proof.

For the displayed bounded `O`, every product required by the Ward identity is a finite polynomial in the Fourier momentum times the heat factor. Its trace is absolutely convergent because
\[
\sum_{n\in\mathbb Z}|n|^m e^{-\pi\beta n^2}<\infty
\quad(\beta>0)
\]
for each fixed `m`. Finite symmetric Fourier cutoffs commute with `Q,Q†,H,N,P_exc`, so all algebraic identities first hold on finite-dimensional spaces, and their trace limits follow by this summable bound. No unsupported cyclicity of unbounded operators is needed.

For the more general admissible insertion class, “absolutely convergent operator heat traces” must retain its usual trace-class meaning. An explicit sufficient formulation is
\[
\sum_{\lambda}e^{-\beta\lambda}\|B|_{E_\lambda}\|_1<\infty
\quad\text{for every }\beta>0.
\]
Bounded insertions and polynomial energy growth satisfy it. Under this formulation polynomial energy factors are harmless: their extra growth can be absorbed into half of the positive heat parameter. This condition concerns the actual operator traces before graded cancellations, rather than assigning a trace by cancelling two divergent series. The frozen return already works with convergent operator traces and includes the bounded/polynomial classes; no enlargement by conditional trace summation is accepted here.

On `u≥0`, `β≥1`; fixed thermal derivatives and source derivatives converge locally uniformly. The `u=0` endpoint is regular, complete theta evenness remains exact, and the `u→∞` differentiated sums decay doubly exponentially. These facts pay the coefficient integrals. No limit at `β=0` is used.

## 3. The graded Ward sign and failure of closure

On the Fourier core, `NQ=Q` and `QN=0`, hence
\[
[Q,N]=-Q,\qquad [Q,y^N]=(1-y)Q,\qquad
[Q,O]=QP_{\rm exc}=Q.
\]
The fugacity at `y=1` is `Q`-closed; its derivative is not. In particular the degree fugacity is not a charge commuting with the selected supercharge away from the protected point.

For an even admissible insertion `O`, held fixed when differentiating `β`, finite-dimensional graded cyclicity gives
\[
\begin{aligned}
\operatorname{Str}([Q,O]Q^\dagger e^{-\beta H})
&=\operatorname{Str}(QOQ^\dagger e^{-\beta H})
-\operatorname{Str}(OQQ^\dagger e^{-\beta H})\\
&=-\operatorname{Str}(OQ^\dagger Qe^{-\beta H})
-\operatorname{Str}(OQQ^\dagger e^{-\beta H})\\
&=-\operatorname{Str}(OH e^{-\beta H}).
\end{aligned}
\]
The first minus sign comes from moving the odd `Q` past the odd product `OQ†`; ordinary ungraded cyclicity would give the wrong conclusion. The trace-class limit in Section 2 justifies this equality for the stated insertion. Differentiating the actual trace therefore gives exactly
\[
\Theta'_{\rm exc}(\beta)
=\operatorname{Str}(QQ^\dagger e^{-\beta H})
=-2\sum_{n\ge1}\pi n^2e^{-\pi\beta n^2}<0.
\]
`QQ†` acts on degree one, explaining its negative supertrace. Setting this residual to zero would erase the nonzero excited-spectrum response needed for reconstruction.

The reconstructed insertion `O(β²H²-(3/2)βH)` remains even and generally unclosed because the energy polynomial commutes with `Q`. Its explicit `β` dependence must also be differentiated in subsequent variations. Neither compactness nor a formal invocation of the index removes these terms. This is a failure of observable closure in the selected model, with no anomaly or spatial boundary required.

## 4. The precise protected class really cancels

Let `B` be fixed and independent of `β`, even, preserving each complete `H` eigenspace, commuting with `Q` on the Fourier core, and satisfying actual heat-trace admissibility as above. It need not be self-adjoint, and it may mix `n` and `-n` within one positive-energy eigenspace.

For `λ>0`, the restriction `Q_λ:E_λ^0→E_λ^1` is invertible. The even block restrictions satisfy
\[
Q_\lambda B^0_\lambda=B^1_\lambda Q_\lambda,
\qquad B^1_\lambda=Q_\lambda B^0_\lambda Q_\lambda^{-1}.
\]
Their finite-dimensional ordinary traces are equal, including the full degeneracy. Thus their graded contributions cancel separately at every positive energy. Summing the admissible heat trace gives
\[
\operatorname{Str}(BP_{\rm exc}e^{-\beta H})=0,
\]
while the unsubtracted trace is the fixed difference of the two harmonic traces. A constant `Θ` produces `p=(1/2)e^uΘ`, annihilated by `(∂_u²-1)/8`. Therefore every insertion in this exact class reconstructs the zero source.

The canonical `Φ` is nonzero: on `u≥0`, every displayed `n≥1` source summand is positive because `πn²e^{4u}>3/2`. A protected replacement consequently fails already at `r=1`, before any higher determinant or Mellin condition is considered. The actual `O=-NP_exc` is outside the cancelled class precisely because `[Q,O]≠0`, and gives the exact match.

This proves the scoped obstruction, with its quantifiers intact. It does not cover arbitrary explicit `β` dependence, a different supercharge or complex, equivariant compensation, boundaries, interacting theories, enlarged observables or four-dimensional moduli constructions. It is not a theorem that every protected representation of theta is impossible.

## 5. Coefficient and two-copy conventions

The functional `L_n` has exactly the original `(2n)!` denominator, and `L_n=0` at negative indices is a stipulated coefficient convention, not an integral continued to negative powers. With the reconstructed source, `L_n[Θ_exc]=c_n` for every nonnegative integer `n`.

At `r=1`, the determinant is `D_{1,k}=c_k`; in particular `c_0>0`. At `r=2`, antisymmetrization gives
\[
D_{2,k}=c_k^2-c_{k-1}c_{k+1},\qquad D_{2,0}=c_0^2.
\]
The relative minus sign and the zero convention at `c_{-1}` are correct. This is not an adjoint overlap or automatically a squared norm. The baseline `R'>0` gives the already established order-two positivity; it is not newly obtained from supersymmetry. At arbitrary fixed `r`, the permutation formula is the determinant expansion in `r` independent copies, with no extra `r!`.

The resulting dictionary is an antisymmetrized product of integrated thermal responses. It does not identify determinant order with differential-form degree, or exhibit a new local multipoint field operator. The original `h_3`, its negative region and the full signed Mellin curvature remain unchanged. `s`, thermal `β`, source coordinate `u` and physical heat time remain different parameters.

A bounded standard-library exact support replay verified the paired-energy reconstruction polynomial `2ξ²-3ξ` and the zero/positive/negative Fourier-block nilpotence, Hamiltonian, commutator and graded Ward signs. The universal block proof is given above; the finite checks are supporting arithmetic only. No quadrature, source sampling, coefficient campaign or new numerical artifact was created.

## 6. Controls, literature limits and accepted consequence

| Control | Review finding |
| --- | --- |
| Gaussian | Does not have the selected literal unchanged circle-spectrum reconstruction. Its curvature equality supplies no transfer theorem here. |
| Euler-factor sources | Fail the exact unchanged source match. The generic pairing cancellation gives no new bound on their complete responses. |
| Weighted-square / finite-square sources | A changed energy weight can be encoded in `O=-Nw(H)P_exc`; it changes the observable and generally leaves `[Q,O]=w(H)Q≠0`. The unchanged weight premise fails. |
| Reflected super-Gaussian and smooth-shape / positive-primitive sources | Do not equal the stipulated trace/reconstruction; another realization is not excluded. Generic Hilbert-space positivity and supersymmetric doubling do not bound their signed response. |
| Two-point association relaxation | Has no claimed matched circle realization; it continues to screen association-only estimates rather than the exact dictionary. |

A positive-time collision does not contradict a time-zero finite-order theorem, and source identification alone provides no curvature allowance. The Gaussian bound remains unpaid on `[0,2]`, the other compact values and the unbounded Mellin tail; spatial/thermal decay is not a substitute for a large-`s` estimate.

The reference to Witten's [1982 paper](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf) is historical context. The author's support record limits its evidence to indexed passages and reports failed direct retrieval; no full-paper reading, archived local copy or imported localization theorem is assumed. The review's attempted web open supplied no readable text. The circle pairing theorem and all operative formulas were proved explicitly above, so no claim depends on filling that access gap from memory. The coordinator's [new parallel-source note](../../../../references/07_PARALLEL_PHYSICAL_ASSESSMENT_SOURCES_20261101.md) and its receipts preserve these limited inspection claims; the original frozen physical-source note need not be rewritten.

The surviving formulation has concrete physical content: the complete square spectrum comes from a fixed compact circle before the coefficients are supplied, the degree-fugacity response recovers its excited thermal trace, and the thermal reconstruction gives the exact canonical source. Protection cancels that same excited spectrum, whereas differentiation transverse to the protected point retains it. This response/protection distinction is useful independently of the missing inequality.

**Accepted:** the source and multi-copy response construction, nonzero `Q` commutator, graded Ward residual, `r=1/r=2` normalization, and protected-class cancellation with its exact scope. **Clarification:** use the closed domains and genuine trace-class admissibility in Section 2; no source or Ward formula changes. **Unresolved:** no new Mellin allowance or sign mechanism is supplied. No Donaldson identification, novelty, RH consequence or all-theory no-go result is accepted or claimed. The fixed E check is complete; shared integration belongs to the coordinator.
