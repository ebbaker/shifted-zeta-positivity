# MC04-E01: separate review of the inserted logarithmic-dilation Ward identity

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewer `/root/review_ward_susy`, actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**. Verified from reviewer rollout session `01a19a55-0995-7e60-9282-84ec086e4d16`, turn `01a19a55-09a9-7cc0-9daa-fd9f2055fd75`. This is fixed **E — execution**, request r1; the reviewer owns this file only.

**Disposition: accept the exact identities and the stated finite-polynomial pointwise nonclosure obstruction. No mathematical correction is required.** The return gives a useful finite-particle response formulation and isolates a precise unestimated mixed response. It proves neither the Gaussian curvature envelope nor a neighboring-index allowance. The whole quantitative target remains open, including `[0,2]` and the unbounded Mellin-parameter tail.

This is a different-worker, different-model **internal LLM review** of Astra/ultra work. The author's model and effort were independently read from the cited author turn's local rollout metadata. Author and reviewer share the canonical source, accepted source/sign review and launch baseline; this is not independent specialist review. No baseline interval certificate was rerun and no new numerical campaign or candidate was introduced.

## Frozen inputs and scope

The [r1 checking request](../numerics/MC04_E01_REVIEW_REQUEST_R1_20261101.json) identifies the [frozen return](../notes/01_INSERTED_ENSEMBLE_IDENTITY_RETURN_20261101.md). Its bytes were checked at entry and after review:

| Input | SHA-256 |
| --- | --- |
| MC04-B01 return | `088c8c59427af7fee108066a17d0fac7d6a2ee62a0c43ac3dc7843baaae6b0d3` |
| Launch manifest | `501acdcfa663b5eb4959c348095a4e79c70053907660b599f3585862a526f60a` |
| Initial Mellin assessment | `ee4280708b43d4d080fe98c128d58c0180f0ba0851b730bd859c2a899f84d9de` |
| Accepted source/sign Review01 | `c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe` |

The manifest's mathematical baseline files still match their launch hashes. The known live progress registers have changed; those changes were not used as mathematical inputs. The author configuration was verified for session `01a19a49-e72d-7902-8f13-adf50b8aa74f`, turn `01a19a49-e74a-7a23-ac10-efb3c7f23e13`: **gpt-6-astra / ultra**.

Read with the [result index](../../../../../../../result-summaries/README.md), especially [theta identities](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [physical-channel lessons](../../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md) and [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../../../avoid/README.md), especially [target reformulations](../../../../../../../avoid/01_restating_the_target.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [shared premises](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [normalization](../../../../../../../avoid/08_normalization_and_constant_slips.md) and [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## Undivided identity and its curvature consumer

Keep the return's definitions `G=V(u²)Δ`, `q=∏u_j²`, `T=log q`, `X=Σu_j log(u_j)∂_{u_j}` and `M=∫q^sG`. On the open chamber, the product rule gives
\[
XG=\frac{w_s}{q^s}\{Xh+h(I_z+I_R+L_\Phi)\}.
\]
Thus `w_s J=q^s XG` is exactly correct. It differentiates the insertion, uses source derivatives only through order five, and makes no division by `h`. Its zeros and negative region remain in the problem.

Since `div v=3+T/2` and `X(q^s)=sTq^s`, the complete divergence is
\[
\operatorname{div}(v q^sG)
=q^sXG+\bigl(3+(s+\tfrac12)T\bigr)q^sG.
\]
The vanishing boundary flux established below therefore yields
\[
(s+\tfrac12)M'+3M+N=0,\qquad N=\int q^sXG.
\]
There is no factor of `3!`: all expressions here use the ordered chamber. Full-orthant derivation gives the same equation after dividing every integral by `3!`.

Let `ℓ=M'/M`, `A=M/Z>0`. Local dominated differentiation gives
\[
\left(\frac NM\right)'
=\frac{N'M-NM'}{M^2}
=\frac{E_s[(T-\ell)J]}A.
\]
Differentiating the divided Ward equation consequently gives exactly
\[
(\log M)''
=\frac{-\ell-A^{-1}E_s[(T-\ell)J]}{s+\tfrac12}.
\]
The sign and the denominator are correct at `s=0` as well as at positive `s`. In particular `ℓ=E_s(hT)/A` is generally different from the carrier mean.

For an independent algebraic comparison, write `m=E_sT`. Then
\[
\frac{M''}{M}-\left(\frac{M'}M\right)^2
=\operatorname{Var}_sT
+\frac{\operatorname{Cov}_s(h,(T-m)^2)}A
-\left(\frac{\operatorname{Cov}_s(h,T)}A\right)^2.
\]
Expansion of the centered square verifies equality to the complete baseline consumer. All three terms are retained. Since `s+1/2>0`, the return's lower bound on `A^{-1}E_s[(T-ℓ)J]` is **exactly equivalent** to the proposed pointwise Gaussian envelope. It is an equivalent residual target, not a newly proved inequality.

## Boundary and differentiation audit

The undivided formulation is sufficient throughout; no separate estimate of a potentially singular quotient is required.

- **One or more nodes at zero.** Complete-source evenness makes each even derivative a smooth function of `z=u²` near zero. The alternating determinant has a factor `V(z)`, so locally `G=V(z)²F(z)` with `F` smooth. In particular it is bounded. At a coordinate cutoff `u=ε`, the flux contains `ε^{2s+1}log ε`, with at most a fixed extra power of `|log ε|` after Mellin differentiation. It tends to zero uniformly for `s` in compact subsets of `[0,∞)`. Integrands involve `u^{2s}|log u|^m`, which is integrable also at `s=0`. The same argument handles several nodes tending to zero; the unused Vandermonde vanishing only improves it.
- **Positive collision faces.** The field has equal components at equal nodes and is tangent to the face. Also both alternating factors vanish, so `G` vanishes at least quadratically. The `V(z)²F(z)` representation includes multiple collisions on bounded sets, including collisions meeting the origin. No collision flux survives.
- **All mixed spatial tails.** Expanding `Δ` and `XΔ` into their finitely many products reduces each term to one fixed derivative of `Φ` in each coordinate, of order at most five. For large `u`, each is bounded by `C_m exp((4m+9)u-πe^{4u})`. Vandermonde factors, their derivatives, `u log u`, and the fixed powers of `T` contribute only fixed polynomial, exponential and logarithmic weights. Combining the bounded near-origin pieces with the one-variable tail bounds gives a product majorant on every configuration, including some nodes small while others escape. A simultaneous-node ray alone is not used for integrability.

These bounds justify the Ward identity, one derivative of `N`, and two derivatives of `M`, locally uniformly in `s≥0`. They also give finite carrier integrals and inserted moments. Positivity of `M(s)` for real `s≥0` is an inherited signed-averaging premise, explicitly identified in the baseline; integer positivity alone is not being substituted for it. No evenness of a finite theta truncation is assumed.

This establishes the identities on the whole stated parameter domain. It does **not** provide a bound uniform as `s→∞`, a sign estimate on `[0,2]`, or any other curvature allowance.

## Complete-source pointwise nonclosure

The recurrence
\[
P_{m+1}(\xi)=(1-4\xi)P_m(\xi)+4\xi P_m'(\xi),\qquad
P_0=2\xi^2-3\xi
\]
is correct. It gives degree `m+2` and leading coefficient `2(-4)^m`. For `ξ≥1`, the complete remainder beyond `n=1` is bounded by a constant times `ξ^{m+2}e^{-4ξ}`; the finite constant is supplied by the convergent weighted sum over `n≥2`. The recurrence also controls the once-differentiated remainders required by `Xh`. Thus the return uses the complete spectrum, rather than silently replacing it by its first mode.

On `u_j=t+a_j` with fixed distinct increasing `a_j`, put `ξ_j=πe^{4(t+a_j)}`. Their ratios stay distinct and fixed. The determinant `det[1,R,Φ⁽⁴⁾/Φ]` has leading term `4096 V(ξ²)`, and `V(R)` has the same leading term. Uniform differentiable expansion on this fixed-ratio ray gives
\[
h=1+O(e^{-4t}),\qquad Xh=O(t\log t\,e^{-4t}).
\]
The other terms obey `I_z=O(log t)`, `I_R=O(t log t)` and
\[
L_\Phi=-4\pi e^{4t}t\log t\sum_j e^{4a_j}+O(e^{4t}\log t)+O(t\log t).
\]
Consequently the displayed asymptotic for `J/h` is correct, while `T=6log t+O(t^{-1})`. Eventually `h` is bounded away from zero, so taking this quotient on the ray is legitimate.

A polynomial of fixed finite degree in `T` has at most a fixed power of `log t` growth there; it cannot equal this exponential expression. This proves the precise obstruction to
\[
J=P(T)h
\]
pointwise for any fixed finite polynomial `P`, including coefficients selected separately at a fixed `s`.

The proof does not exclude an integrated relation, an inequality, nonpolynomial source observables, enlarged systems or other vector fields. It does not refute the Gaussian envelope. A spatial ray is not an asymptotic analysis of the Mellin integrals as `s→∞`.

## Gaussian normalization, controls and physical scope

For `Φ_G=e^{-au²}`, direct differentiation gives `R=4a²u²-2a`, `h=1`, `I_R=I_z` and
\[
J_G=2I_z-a\sum_jz_j\log z_j.
\]
Let `x_j=s+j` and factor
\[
\mu_j=\tfrac12a^{-s-j-1/2}\Gamma(s+j+\tfrac12)
\]
from column `j` of the moment matrix. The remaining rows are `1`, `4ax_j`, `16a²x_j(x_j-1)`. Their determinant is `128a³`, because the polynomial leading coefficients multiply to `64a³` and `V(s,s+1,s+2)=2`. This gives exactly
\[
M_G(s)=16a^{-3s-3/2}\prod_{j=0}^2\Gamma(s+j+\tfrac12),
\qquad (\log M_G)''=\kappa_3(s).
\]
At `s=0` it also agrees with the triangular anchor `48c_0³`. This checks the absolute constant, Gaussian Ward insertion, factorial conventions and curvature normalization; it supplies no theta comparison.

A fixed exact replay with Python standard-library integer polynomials and `Fraction` verified the `P0`–`P5` leading data and the Gaussian moment determinant as a polynomial in `s`. No quadrature, source sampling, precision scan or external numerical record was created. The proof above is analytical and does not depend on finite test cases.

The claim-specific control screen is retained at its actual scope:

| Control | Review finding |
| --- | --- |
| Gaussian | Generic Ward identity applies and curvature equality holds; its constant insertion removes theta's signed insertion variation. |
| Two-point association relaxation | Does not realize the smooth source/chamber Ward construction. It still defeats association-only inference of the comparison. |
| Euler-factor sources | Smooth undivided Ward identities can persist. Literal unchanged theta reconstruction fails; carrier positivity and the quantitative residual estimate remain untested here. |
| Weighted-square / finite-square sources | The logarithmic field has zero endpoint flux without requiring every odd reflection endpoint. Unchanged full spectrum/reflection fails, and `R'>0`, real-tilt positivity and the residual bound are not asserted. |
| Reflected super-Gaussian, smooth-shape and positive-primitive sources | Appropriate smooth decay permits generic identities; canonical reconstruction fails. No uncomputed carrier or curvature sign is attributed to them. |

The action and the flow `u↦u^{e^ε}` correctly interpret the calculation as a finite-dimensional Schwinger–Dyson/Ward response with the signed observable inserted. This is a useful physical formulation even though its mixed response remains unestimated. It is not physical heat flow, a new local QFT, an automatic positive-state susceptibility or a determinant sign theorem. Borodin's [Section 2](https://arxiv.org/html/math/9804027v1) was reopened for terminology only; no scaling, self-adjointness or positivity theorem is imported into this proof.

**Accepted:** the undivided inserted equation, complete curvature consumer, endpoint/tail justification, full-source finite-polynomial pointwise nonclosure and Gaussian normalization. **Corrections:** none. **Unresolved:** the inequality equivalent to the Gaussian envelope, on all its required domains; no neighboring-index or all-order gain follows from this review. The fixed E check is complete. Shared statuses and any next conceptual decision belong to the coordinator.
