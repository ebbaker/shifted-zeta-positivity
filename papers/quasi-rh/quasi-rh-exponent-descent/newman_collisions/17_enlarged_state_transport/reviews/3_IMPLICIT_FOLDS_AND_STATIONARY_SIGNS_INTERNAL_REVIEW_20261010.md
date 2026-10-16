# Internal review: implicit heat folds and stationary signs

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort unavailable to this session
and not inferred. Root checks and parallel agents are internal LLM review,
not independent mathematical validation.

## Scope and finding

Reviewed the new implicit-chart section of the
[working manuscript](../enlarged_state_transport_and_heat_flow.tex),
[Note 4](../notes/4_COORDINATE_INVARIANCE_AND_IMPLICIT_HEAT_FOLDS_20261010.md),
[Note 5](../notes/5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md),
and the unified [exact checker](../numerics/check_heat_transversality.py)
and [record](../numerics/HEAT_TRANSVERSALITY_RECORD_20261010.json).
No remaining mathematical defect was found within this scope.

The continuation establishes a conditional local theorem, not a genuine
theta inequality or an RH proof. The two stationary-set signs use physical
derivatives through order three and exclude every finite multiplicity on
an open positive-time domain. Their global input is stronger in coverage
than a fourth-jet test at an ordinary threshold candidate. No cost
improvement, first-jet estimate or new genuine stationary-set cover is
claimed.

## Proof audit

1. Passive state changes preserve Cq when the observation transforms with
   the state. Time-preserving spatial charts and nonzero scalar
   normalizations preserve a joint physical value/slope zero. General
   charts must retain the transformed physical spatial vector and heat
   coefficients.
2. At an ordinary double, Ht=-Hxx is nonzero. The graph jets are
   tau''=1, tau'''=-2H3/H2 and tau''''=8(H3/H2)^2-2H4/H2. The full
   Jacobian of (H,Hx) has determinant -Hxx^2. Its invertibility isolates
   and preserves a perturbed collision, rather than excluding it.
3. The fold form 3tau''''-5(tau''')^2>=2g is exactly the imported
   signed fourth-jet threshold inequality divided by H2^2. It contains
   no extra theta sign. A Morse chart requires variable heat coefficients;
   discarding them would give a false coordinate contradiction.
4. For multiplicity 2r, the quotient h^-r Fx(T-h,a+hy) extends
   analytically because every nonzero term has h exponent at least r.
   Its limit is F_(2r)y/(r-1)!+F_(2r+1)/r!. The y derivative is nonzero,
   giving the printed critical curve by IFT. Its value times curvature
   has positive leading coefficient F_(2r)^2/[r!(r-1)!].
5. Even multiplicities contradict HHxx<=0 on Hx=0. Odd multiplicities
   apply the same lemma to Hx and contradict HxHxxx<=0 on Hxx=0.
   Positive-time openness and predecessor coverage are necessary;
   a single-time sign or an uncovered boundary cannot use this proof.
6. With A=2H and beta frozen spatially, the complete source targets equal
   -beta^2 A A'' and -beta^2 A'A''' on the separate stationary sets.
   The signs of both identities and the x^2+4beta coefficient are correct.
7. The product payments include both linear errors and their product.
   Note 5 reconstructs the physical jets of H=G/b through order three,
   retaining all normalizer coefficients. It correctly warns that a
   normalized stationary set generally differs from the physical one,
   and that a fixed absolute error need not resolve a vanishing precursor
   product.

Two parallel agents audited the stationary proof independently of the
root integration. One small correction was made before final replay:
the quadruple-control leading heat polynomial includes its Gaussian
factor K4. The record now explicitly labels this polynomial as divided
by K4. The positive triple control was then added and checked exactly.

## Verification and limits

The unified standard-library replay passed **1,819 exact assertions**.
The saved JSON equals a fresh root replay exactly. The checker source
SHA-256 is
`943c8a2b97c8d9f45bc66c6971ae2c3668517fbf57970e4107f32265d48fe676`.
Its finite checks include Gaussian double/triple/quadruple Fourier
identities and multiplicities, fold jets through order six, nonlinear
coordinate composition, source-perturbation derivatives, stationary
heat-polynomial controls of both parities, varied rational precursor
coefficients, frozen-beta dictionaries, physical normalizer jets and
product-error payments. The analytic IFT existence and remainder argument
is a written proof; finite replay alone does not establish it.

The standalone manuscript compiled successfully with the desktop editor's
built-in compiler. Internal labels are unique and all internal references
resolve. The saved repository source is required to match the compiled
staged source byte for byte before committing. The native editor is
requested for the repository source after saving; a queued UI request
does not by itself establish that its panel is visible.

The controls are positive even Gaussian preparations with smooth pure
lifts on bounded time intervals. They do not share the genuine theta
arithmetic source or its all-time decay regime. The quartic's bounded
threshold behavior is proved in the existing manuscript; no global
threshold theorem is asserted for the triple or quadruple controls.
The exact records do not establish a theta sign, a third-jet approximation
cost, a stationary-set cover, an improved uniform transport estimate,
or the parent imported approximation and no-escape inputs.

The next substantive checkpoint is a genuine theta proof of both signed
targets on a stated predecessor region, with all physical, normalization,
cutoff and endpoint payments, or an independent uniform first-jet source
estimate. No new RH conclusion follows from this continuation.
