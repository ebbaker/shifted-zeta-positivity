# MC02-E01: separate review of the bounded fermionic transfer

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewer `/root/review_thermal_fermion`, actual recorded **gpt-6.1-sol (Codex), reasoning effort ultra**, verified from own rollout `01a19a53-8e12-7bd0-ae29-5de242d6c4b0`, turn `01a19a53-8e26-7d42-903c-91c9afc93375`. The author's specified session `01a19a49-d2ca-7ab1-b502-4e2795ee4f33`, turn `01a19a4e-0183-7c43-8521-ed04982e31c6`, was checked and records **gpt-6-astra / ultra**. This is a separate **cross-model internal LLM review**, sharing the source, accepted baseline and inherited references. It is not independent specialist review.

**Disposition: accept the frozen claims at their stated scope without mathematical correction. MC02-E01's bounded review is complete.** The construction is one bounded number-preserving fermionic transfer carrying all finite ordered coefficient minors up to positive factors. Its all-sector entrywise positivity is exactly the established RH reformulation. The actual canonical two-site Jordan block proves the stated obstruction to making this exact transfer self-adjoint in a positive metric retaining the required states. No theta amplitude estimate, continuous Mellin bridge or curvature improvement follows.

## Frozen scope and evidence

The [request r1](../numerics/MC02_E01_REVIEW_REQUEST_R1_20261101.json), SHA-256 `3cf7a19b92d5ffa2e1d890620e39764e6fed426233ed0288e374b49f0ce207e6`, fixes one analytical review and one rational support replay. The return hash was verified before its contents were opened:

- [Return01](../notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md): `61207dbe824e5a67794d7c3be1811a95c1c69fa8006c4c7cc8d703a867706901` — match.
- [Exact support program](../numerics/mc02_exact_transfer_check.py): `643e3382c939751900e7389fa5d9b9fb929933686b61d07e011ffd0dd2c38b12`.
- [Inherited Mellin assessment](../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md): `ee4280708b43d4d080fe98c128d58c0180f0ba0851b730bd859c2a899f84d9de`.
- [RH normalization note](../../../../notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md): `c5715d555194f7099f6b823e6701d8c4138e702062716ec30ed469a96c513223`; [source record](../../../../references/04_RH_FORMULATION_SOURCES_20261101.md): `38e44a03382300ade81bb73669e7c2988cfb43b8e23f17bb88d0c926a2d96dd1` — both agree with the return's input table.

The checker was read before one replay with exact `fractions.Fraction` arithmetic. There was no theta coefficient acquisition, root test, scan or numerical campaign. Only this review file was written; the frozen return, evidence and live registers were not edited.

Read with the [result index](../../../../../../../result-summaries/README.md), especially [physical channels](../../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md), [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [theta identities](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../../../avoid/README.md), especially [reformulations](../../../../../../../avoid/01_restating_the_target.md), [shared-premise checks](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [normalization](../../../../../../../avoid/08_normalization_and_constant_slips.md) and [unchecked imports](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## Original orbitals, transfer and exterior powers

The complete source is positive on the half-line. For any fixed i and j, its derivative/tail bounds imply \(f_i,g_j\in L^2\); the inverse source in \(|f_i|^2\) can be bounded using the positive first-mode lower bound, leaving a double-exponential tail. Repeated integration by parts gives \(c_{j-i}\) when j>=i. When j<i the polynomial is eventually annihilated; its only possibly nonzero lower endpoint terms multiply odd source derivatives at zero and vanish by complete evenness. Thus negative coefficient indices are zero for a justified endpoint reason. No truncation is declared even.

The normalized exterior-product convention gives exactly the determinant of these pairings for arbitrary finite increasing I,J, with no r! multiplier. This is an overlap between two different orbital families, not a Gram positivity argument. The finite matrix-element rescalings by \(v^{-i}\) and \(v^j/F(v)\) are valid without asserting bounded analysis maps or an infinite diagonal similarity.

The entire generating sum has \(F(v)<\infty\) for every v>0. Therefore \(\sum p_nS^n\) is absolutely norm-convergent and has norm at most one. Its upper-triangular matrix entry is \(p_{j-i}\), with the zero convention for j<i. Rows sum to one and columns to at most one, consistently with left-boundary loss on kets. This proof uses the backward shift in the specified direction.

For each finite r, the restriction of the tensor power to antisymmetric tensors gives \(\|\wedge^r K_v\|\le\|K_v\|^r\le1\). The direct sum has supremum norm one because of the vacuum block. It is defined on all of the stated Fock Hilbert space. No infinite-particle configuration, filled sea, invertibility, or Bogoliubov implementability is required. Expanding a finite wedge proves
\[
\langle I|\Gamma(K_v)|J\rangle
=F(v)^{-r}v^{\sum J-\sum I}\det[c_{j_b-i_a}],
\]
including both arbitrary row and column lists and the positive scaling factors. The proposed free-fermion interpretation is therefore a specified mathematical transfer theory; it carries no additional local Hamiltonian or reflection-positivity assertion.

## Primary normalization and RH quantifiers

The review freshly inspected the primary [Katkova v1 HTML](https://arxiv.org/html/math/0505174v1), equations (3)–(6), Definition 2, Theorem ASWE and Theorem C. The printed source uses the same canonical Phi and gives \(b_n=8\,2^{2n}c_n\). Consequently
\[
F(z)=\tfrac18\xi(\tfrac12+\tfrac12\sqrt z),
\]
with no square-root ambiguity because xi is even about 1/2. This is entire of order 1/2 with positive constant coefficient. Under RH its zeros are all negative real; its genus-zero product is of the required Laguerre–Pólya positive type. Conversely the stated ASWE/Theorem C characterization of the **entire** coefficient generating function gives that zero property from PF-infinity.

Definition 2 is all finite minors of the one-sided upper-triangular Toeplitz matrix. Thus all increasing I,J and every finite r in the return are the correct quantifiers. One fixed v>0 suffices because every rescaling factor is strictly positive, and then the equivalent statement holds for every v>0. Entrywise nonnegativity in this fixed occupation basis is distinct from positive semidefiniteness and reflection positivity. No restriction to rectangles, fixed order or asymptotic displacement is smuggled into the equivalence.

This is selected primary-statement verification, not a new audit of the original ASWE proof. It corroborates the existing checked source record; no new reference-catalog entry is needed. The earlier Alexandrov–Zabrodin finite-CAR reading record was read; the finite wedge identities needed here were derived directly, so no infinite-current theorem is imported.

## Jordan obstruction and exact relaxation

On \(E=\operatorname{span}(e_0,e_1)\), higher shift powers vanish, so the actual restriction is \(B=dI+bN\) with d>0 and b=vc1/F(v)>0. For a positive Hermitian G, the (1,2) equation in \(GB=B^*G\) is \(\alpha b=0\); positive definiteness gives \(\alpha>0\). This is a direct contradiction, independent of other entries or conditioning. If a full positive inner product retained both states and made K symmetric, its restricted bilinear form would satisfy the same identity on invariant E. Thus the scope covers that exact transfer and those states even when no bounded similarity is postulated.

It does not exclude a compression/dilation with extra states, products of distinct transfers, non-Hermitian methods or a different physical realization. In particular, the Gaussian PF-infinity sequence has c1>0 and the same Jordan obstruction. Self-adjointness of this transfer is therefore not necessary for the desired coefficient signs, and the obstruction supplies no evidence against RH. The return preserves these limits.

For the sole rational relaxation F*=1+z+2z^2 at v=1, the replay gives normalizer 4, weights (1/4,1/4,1/2), unscaled minor -1 and two-particle amplitude -1/16. It proves that these generic nonnegative one-particle contraction properties do not sign antisymmetrized amplitudes. The illustrative commutator sample is 3/4=alpha*b. Its sample G is not positive definite; the return correctly uses it only to check algebra. The universal positive-metric obstruction rests on the symbolic argument above, not on that sample. The polynomial relaxation fails unchanged canonical reconstruction and is not a theta counterexample.

## Mellin consumer and disposition

For rectangles, \(\sum J-\sum I=rk\). Hence \(a_{r,k}=v^{rk}D_{r,k}/F(v)^r\), and both positive scalings cancel from the neighboring ratio. The inherited factorial budget at r=3 is
\[
B_{3,k}=\frac{(2k+6)(2k+5)}{2k(2k-1)}\quad(k\ge1).
\]
Its Gaussian comparison factor is \((2k+5)/(2k-1)\), so division gives exactly the unpaid amplitude ratio bound k/(k+3), including the first nontrivial index k=1. The separate k=0 triangular anchor remains untouched. Neither \(|a_{r,k}|\le1\) nor the Jordan calculation bounds this neighboring quotient with its small denominator.

The continuous bra/ket representation and its full signed curvature retain the centered-square covariance and squared-covariance payment. Changing v has not been identified with changing the real Mellin tilt s. The lattice construction consequently gives no extension to noninteger coefficient indices or curvature estimate. The obligations on [0,2], other compact ranges and unbounded s are all still open. The control table correctly withholds uncomputed time-zero signs: altered square sources may fail the endpoints needed for orbital IBP, while the generic discrete coefficient encoding needs only its own convergence hypotheses. Positive-time collisions do not decide the present finite-order condition.

**Classification:** (1)–(5) and (9)–(10) are exact representations/identities; (6) is an existing RH equivalence in a concrete bounded physical representation; (7) is a proved obstruction for the specified self-adjoint realization; (8) is a finite information-class obstruction; (11) is an unproved estimate. The organizational value of one transfer carrying all finite sectors is accepted without promoting it to positivity progress.

**Corrections:** none required. **Unresolved issues in the fixed exact claims:** none identified, subject to the explicit inherited primary-theorem status. **Unproved research target:** the stated amplitude comparison and complete real-Mellin Gaussian curvature bound. Stop after MC02-E01. No new campaign or follow-through task is issued; the coordinator alone updates registers, references and history.
