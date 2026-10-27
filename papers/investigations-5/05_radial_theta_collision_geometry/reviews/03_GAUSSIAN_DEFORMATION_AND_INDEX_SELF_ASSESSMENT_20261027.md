# Gaussian source deformation and index transport: self-assessment

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0001, thread 01a17e9c-bfd5-7782-a76f-b2a2eaa82417.

**Scope: same-assistant analytical assessment of [Note04][note] and its exact rational replay. This is not independent mathematical review.** RTC-05 has a first bounded return: complete Gaussian source deformation and collision-index transport, plus an exact control exposing its missing upper-time crossing. No independent canonical zero-degree constraint is obtained.

## Analytical audit

1. **Source and normalization.** The convolution integrates the whole even source against the Gaussian with mean rho*v and variance (1−rho²)/2. It includes the full integer-square source before reflection and integration. Total source mass is preserved. At rho=0 the source is Z exp(−u²)/sqrt(pi), and its half-line transform is H(0,0) times the displayed positive Gaussian factor. There is no lost factor of two.
2. **Convergence scope.** The canonical source has every Gaussian moment. The quadratic convolution inequality and a compact positive source interval prove the intermediate Gaussian tail rate. This rate is specific to that all-Gaussian-moment input; it is not assigned to the Gaussian-polynomial control, whose own finite domain is checked separately. The common slab t<1 suffices for the construction. A larger finite-rho domain is used explicitly only where Delta>0, including the finite-rho identity at t=1.
3. **Observation formula.** Completing the Gaussian square gives Delta^(-1/2) exp(−(1−rho²)a²/(4 Delta)) H(rho² t/Delta,rho a/Delta). The same formula at imaginary a fixes the evolving radial mass. Compact higher source moments can be bounded at c<c'<1 by the exact formula at a=0, so formal differentiation is not left without a convergence payment.
4. **Positive terminal anchor.** The estimate cos(Au)≥1−A²u²/2 uses the complete positive source. Its finite rho cutoff depends only on H(0,0), M2(c), c and R. It does not assume a lower bound for an unknown vanishing jet. The resulting positive region belongs to the deformed field; the proof does not transfer it to rho=1.
5. **Two time variables.** The source generator is (1/2)partial_u²+partial_u(u·). Its observed generator is X=2t(t−1)partial_t+(2t−1)a partial_a+t−a²/2. The commutator [B,X]=(4t−2)B is retained; claiming a zero commutator on arbitrary functions would be wrong. At fixed t the auxiliary evolution is forward parabolic, with the opposite ordinary-double index in the (s,a) plane from the physical (t,a) plane.
6. **Multiplicity and variable matrices.** The coordinate determinant is rho³/Delta³>0. The physical jet is transformed by a lower-triangular matrix with positive diagonal, times a positive scalar. Its contraction through that same matrix class justifies global boundary degree transport despite its dependence on the boundary point. Local multiplicity and the inherited index −floor(m/2) are preserved for every finite m.
7. **Faces and endpoints.** The exact event orbits have increasing t and a while t<1/2. Lower-time entries, upper-time exits and right-frequency exits all remain in the ledger; the left wall is paid by positivity. The strict c<1/2 domain excludes tangencies for this flow. The note states how corner crossings and enlarged-domain tangencies are counted without double counting. Collision flux under the deformation is distinguished from ordinary-root wall flux in the physical time direction.
8. **Global limit.** At positive rho the full open slab map is a diffeomorphism. A hypothetical event approaches (1,0), precisely where the Gaussian heat transform ceases to be an ordinary finite integral. The finite-rho value at (1,0) diverges as rho^(-1). Source normalization and Kelvin symmetry do not remove this cap. Choosing orbit-following frequency walls retains the temporal exits.
9. **Radial bookkeeping.** The source integral Z is conserved, but M_(rho,t)=16 F_rho(t,i) changes. Both the potential's infinity constant and its central charge use that same M. The positive even intermediate sources have elementary Kelvin covariance; this does not restore their lost canonical square expansion.
10. **Exact control and complete walls.** The original Gaussian-polynomial control has only one positive-frequency common zero in its heat domain, at t=1/4 and a²=24. On the chosen box its transformed event exits at rho²=5/9 through t=3/8, a²=30. The quadratic root polynomial, its value 3203/8192 at the bounding point, and derivative floor 27165/256 prove all possible deformed real roots have a²<35. Thus a=6 stays strictly positive throughout the deformation, not just at sampled endpoints. The lower time face has no roots; the upper face changes from two to none exactly at the crossing. The inherited wall formula then gives degrees −1 and 0.

## Evidence and scope

The [checker][checker] passed, producing the [record][record]. It checks multivariate rational identities by polynomial arithmetic, full differential-operator composition, the source Gaussian equation, inverse event trajectories, the control heat equation and the exact rational endpoint inequalities. The reported degrees use the inherited physical wall theorem together with the proved polynomial root classification. They are not floating polygon estimates.

The source convergence and boundary-degree arguments remain analytical proofs. The finite replay does not establish an all-height theta bound, locate a canonical collision, independently validate the inherited index theorem or supply specialist review. Primary Gaussian normalizations and internal degree inputs are recorded in the [reference annotation][refs].

## Decision and remaining work

The tested inference from a positive Gaussian endpoint to zero original degree fails with the full boundary terms restored. This is a scoped obstruction to this contraction-and-smoothing homotopy, not a universal failure of source deformations or global index arguments. The exact transport is a heat symmetry; it does not add an arithmetic sign.

Keep RTC-05 open beyond this first return. A further attempt needs a concrete non-Gaussian construction or an independently acquired signed canonical boundary estimate, with a declared information gain. Repeating the same Gaussian endpoint argument with omitted cap or face crossings would not be new work. No numerical theta campaign, manuscript milestone or investigation closeout is justified by this result alone.

[note]: ../notes/04_GAUSSIAN_SOURCE_DEFORMATION_AND_COLLISION_INDEX_TRANSPORT_20261027.md
[checker]: ../numerics/03_check_gaussian_index_transport_20261027.py
[record]: ../numerics/03_GAUSSIAN_INDEX_TRANSPORT_CHECKS_20261027.json
[refs]: ../references/02_GAUSSIAN_NORMALIZATION_AND_INHERITED_INDEX_INPUTS_20261027.md
