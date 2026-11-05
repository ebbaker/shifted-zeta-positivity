# RGD-E04 r5: reciprocal proof, constants and scope checks

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6.1-sol (Codex), effort ultra**,
chat0006, thread 01a1a7f8-9f05-7120-8691-d40d5b3b3333, turn
01a1a7f9-4113-7df0-bbf7-fd8a5ee71964.
Type **E**, supporting the [frozen r5 assessment][packet].

**All twelve obligations are accepted within their stated scopes,
without mathematical correction.** [Review08][review] owns the assessment
disposition; this note records reusable checks, not a second research
mechanism. One analytical pass was completed; no correction pass was needed.
The six frozen inputs retain their recorded sizes and SHA-256 hashes.
Three read-only Sol/ultra contributors checked proof, scope and source
passages; the coordinator checked and wrote the return. This is
different-model internal assessment of Astra/ultra work with shared
premises, not independent specialist review.

## 1. Duality, orientation and the fixed-k error

In [Note10][input] (3), let I={0,...,r−1} and J={k,...,k+r−1}
in the (r+k)-square unit upper triangular Toeplitz matrix. The Jacobi
sign is (−1)^(sum I+sum J)=(−1)^(rk). The complementary inverse rows
are J-complement={0,...,k−1}, and columns are
I-complement={r,...,r+k−1}. Inverse entries are
(−1)^(r+j−i) h_(r+j−i); their factored sign is also (−1)^(rk).
Thus the signs cancel and the original row normalization supplies c0^r.
Negative indices stay zero at every stage. For k=0, the original
triangular determinant is c0^r and the dual empty determinant is 1.

At a simple positive zero α_l, the actual reciprocal residue is
−c0/C′(−α_l)=−A_l α_l. Successive real crossings give
sgn A_l=(−1)^(l−1). The inverse-node Vandermonde has sign
(−1)^(k(k−1)/2) and denominator ∏α_l^(k−1), canceling the product
of residue signs. This yields exactly the positive margin (6).
The exponential coefficient representation requires r≥k−1.

Scaling entry (i,j) by ρ^(r+j−i) multiplies a k-square determinant
by ρ^(kr)>0. Its reference factors as U diag(A_l β_l^(−r)) V.
The Cauchy estimate for the complete analytic G gives
norm-infinity of the scaled residual at most kM. Rows of U-inverse
are the Lagrange coefficient vectors, with absolute row sums u_l.
The identity V=diag(β_l^(−(k−1))) U-transpose J gives
norm-infinity of V-inverse at most ∑β_l^(k−1)u_l≤ku_*.
Thus (8)–(10) have the correct orientation and k² factor.

For Q=scaled-B-inverse times scaled-error, norm-infinity Q≤δ_r≤1/2.
The real matrices I+tQ are nonsingular for 0≤t≤1, so their determinants
remain positive. The eigenvalue bound gives
|det(I+Q)|≥(1−δ_r)^k, proving (11) without a Hermitian assumption.
The ceiling in (12) enforces δ≤1/2, including when log(2B_k)<0.
The recurrence δ_(r+1)=β_k δ_r concerns the chosen majorant.
The actual error norm need not satisfy this equality.

For the zero-free factor F, max-bound L≥1 follows from F(0)=1.
Applying Harnack to U0−Re log F gives
−2U0 t/(S−t)≤Re log F≤2U0 t/(S+t).
Both unequal denominators are needed. They imply the stated residue
floors/ceilings and the complete triangle allowance (17).

## 2. Finite-zero premise and every initialization constant

The [source record][refs] distinguishes the published Platt–Trudgian
abstract, which includes simplicity, from the archived arXiv v1 abstract.
Odlyzko §2, printed pp.7–8 / PDF pp.8–9, orders zeros with multiplicity
and supplies the first two ordinates and ordinary counting equations.
Bounded reinspection of those passages supports the stated inputs;
the external computational certificates were not replayed.

For z=−(2s−1)², |z|=4γ²+(2σ−1)². Therefore every zero in radius1600
comes from |γ|≤20. The finite-height result and first two ordinates
give exactly one simple positive mapped zero α=4γ1² in (784,900).
The functional-equation pair maps to one zero, preserving local
multiplicity away from s=1/2. No trivial xi zeros are added.

The complete source estimate in Note07 uses
Φ_n/Φ_1≤2n⁴ exp[−(n²−1)t], t=πe^(4u), and
n⁴≤16^(n−1), n²−4≥5(n−2), n≥2. Its geometric sum is at most
64e^(−3t)<1. Together with Φ1≤2π²e^(9u−πe^(4u)),
this gives Note10 (18), including every source mode.

With S=1600 and a=(9+40)/4=49/4, the substitution t=πe^(4u)
gives C(S)≤π^(2−a)Γ(a). For all t≥0,
t^(45/4)≤t^11+t^12; hence Γ(49/4)≤11!+12!<2^49.
Since π^(2−a)<1, (19) follows. The primitive estimate uses
e^(4u)≥1+4u, n²≥1+3(n−1), and a denominator at least 4π−1.
It yields d0<1/4 and therefore c0=1/16−d0/8>1/32,
with no approximate moment substituted.

The constants in (21) follow analytically:

| Quantity | Paid inequality |
| --- | --- |
| Zero-free max-bound | L<(9/7)2^54<2^55, so U0=55 exceeds log L |
| Lower residue exponent | 110α/(1600+α)<198/5<40 |
| Upper residue exponent | 110α/(1600−α)<990/7<142 |
| Contour exponent | 110·1200/(1600−1200)=330 |
| Circle denominator | 1200/α−1>1/3 |
| Complete residual | M<3e^330+3e^142<6e^330 |
| Relative allowance constant | M/A<6e^370<e^372 |

Here u_*=1 for k=1. Since β=α/1200<3/4 and
log(4/3)>1/4, δ_r<e^(372−r/4)≤e^(−3)<1/2 for r≥1500.
The residue floor A>e^(−40), c0>1/32 and α<900 then give

\[
 D_{r,1}>\frac{e^{-40}}{2\cdot28800^r},\qquad r\ge1500.
\]

This is an initialized analytical bound using named published finite-zero
inputs. It is not a new numerical certificate, improved threshold,
new positivity range or all-index result.

## 3. The two growing-index stops have different meanings

For a fixed N-pole reference, Q_N H_N=P_(N−1). Thus its coefficient
recurrence begins at m=N, using zero negative coefficients. In the last
column m=r+k−1−i≥r≥N; the N required preceding columns exist if k>N.
Their exact linear combination vanishes. Therefore the reference
determinant is zero for r≥N,k>N, even when k>r+1.
Rank≤N for the entire matrix is only used when r≥k−1.
The complete determinant can still receive nonzero residual contributions.

For the defined triangle/Harnack allowance, interpolation of
(x−1/2)^(k−1) yields
1≤2^(1−k)∑_i 1/∏_(j≠i)|β_i−β_j|≤2^(1−k) k u_*.
The kth residue term also gives
Mhat/a-minus≥β_k/(1−β_k). Consequently

\[
 \widehat\delta_r\ge
 4^{k-1}\frac{\beta_k^{r+1}}{1-\beta_k}.
\]

Ordinary zero counting gives n(R)~sqrt(R) log R/(8π).
A persistent relative gap between consecutive radial moduli R_j
would contradict this asymptotic at two interior radii of that gap;
therefore R_(j+1)/R_j→1. In any valid packet,
R_k=α_k<ρ<S<R_(k+1), forcing β_k→1 along any unbounded sequence
of valid packets. Such a sequence is not assumed to exist.
If k/r≥c>0, then (r+1)/k is bounded and
liminf k^(−1)log δhat_r≥log4>0. This proves divergence of
the specified allowance in its domain r≥k−1.

For polynomial E(z)=∏(1+z/α_i), the reciprocal partial fractions are
exact and G=0, while (17) remains positive and can fail as ρ approaches
α_k. Thus allowance failure is not actual error growth. It does not
exclude cancellation-sensitive residue estimates or other references.

## 4. Control screen and Green normalization

Let g_t be the full-line probability density of the symmetric Gaussian
mixture with means ±a and variance 2t. The explicit half-line source
Φ(u)=2s[g_σ(u)+εg_β(u)] has the transform in Note10 (27).
Its chosen s gives C_ε(1)=1/16. Cosh contributes simple negative real
zeros, while the exponential factor contributes exactly (28).
Their moduli tend uniformly to infinity as ε decreases to zero.
For any prescribed finite cosh-zero prefix, choose S before the next
cosh zero and ε small enough that all nonreal zeros lie outside S.
This supplies a finite P_k(S) while the entire function still has
nonreal zeros.

For p(u)=8∫_u^∞sinh(v−u)Φ(v)dv, differentiation gives
p′=−8∫_u^∞cosh(v−u)Φ(v)dv, p″−p=8Φ and p′(0)=−1/2.
The Gaussian tails justify integration by parts and give
C_ε(z)=1/16+(z−1)P(z)/8, with P the cosh transform of p.
Thus positivity and the Green endpoint normalization are retained.
This is an off-axis-zero control, not a certified positive-time collision.

The [repository control screen][controls] was applied at premise level:
Euler-factor controls change the exact arithmetic source; weighted-square
and finite-source controls lose its unit-weight infinite square sum/full
reflection; reflected and positive-primitive controls lack its arithmetic
square expansion; finite-prime/profile controls omit the complete identity;
BW-01 is atomic; RH-conditional endpoint controls change Dirichlet
arithmetic and packets containing added doubles fail simplicity; variable
kernels change the observation equation. These source differences do not
establish failure of P_k(S). The conditional fixed-k theorem can hold for
non-theta sources and is not a global discriminator.

## 5. Evidence level and continuation

The six frozen repository inputs and all four external PDF reading
copies match the existing receipts. Source checks are bounded passage
checks; hashes identify bytes. The matching kenan.works mechanism is
attributed using primary-page indexed text because direct access again
returned HTTP502. Its notebooks and reported coverage remain unaudited.
Sra v3, Appendix C Lemma C.15, concerns continuous densities Θ and Λ;
it supplies no imported theorem about D_(r,k).

Under [result summaries][results] and [avoid][avoid], especially
[01][a01], [05][a05], [07][a07], [11][a11], [12][a12] and [16][a16],
the result is acceptance of a conditional estimate, initialization and
two scoped stops. No criterion has been promoted to RH evidence.
No numerical work or correction was needed.

Park this finite-pole/triangle-payment route for growing indices.
The [continuation/model-change note][next] proposes the next
**B02 r3 — B/Astra** decision: a nonzero growing-dimension reference
margin with a paid correlated residual, or a scoped stop. It does not
activate that research or a new E task.

[packet]: ../research-progress/handoffs/15_RGD_E04_R5_RECIPROCAL_COMPARISON_ASSESSMENT_20261104.md
[review]: ../reviews/08_RGD_E04_R5_RECIPROCAL_COMPARISON_ASSESSMENT_20261104.md
[input]: 10_RGD_B02_R2_RECIPROCAL_POLE_INDUCTION_AND_SCOPED_STOP_20261104.md
[refs]: ../references/02_RECIPROCAL_COMPARISON_AND_FINITE_ZERO_SOURCES_20261104.md
[next]: ../research-progress/handoffs/16_RGD_E04_R5_RETURN_AND_MODEL_CONTINUATION_20261104.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
