# Status through 13 September 2026

The [manuscript](manuscript.pdf) is the current account. It replaces the working
notes as the reading entry point while preserving those notes in the archive.

The manuscript accounts for work through 12 September. The latest exploratory
result is the [superspace relative boundary action](archive/notes/SUPERSPACE_RELATIVE_BOUNDARY_ACTION_20260913.md),
summarized in the final section below. It follows the covariance audit and
finite-block obstruction.

The opening introduction now explains the physical interpretation and the role
of each result. The constructions define positive static energies and their
minimized boundary responses. The auxiliary SUSY Hamiltonian organizes harmonic
states; their ordinary norms, rather than their zero auxiliary energies, are
the proposed arithmetic observables. The later superspace follow-up constructs
a canonical Hamiltonian for this relative complex, beyond the manuscript's
scope. Quadratic bulk energy is a model assumption;
nonlinear completions remain possible, subject to the scope of each obstruction.
This introductory revision changes exposition, not the numerical results or
the numbered analytic statements.

The current exposition also gives the missing connection to the overall
program: the direct central route versus accumulated shift contraction,
the gamma-ratio derivative leading to the kinetic tower, and the zeta
logarithmic derivative leading to prime delays. It explains exponential
loop coupling as a static energy ansatz motivated by the tower's logarithmic
response. The resulting residual and field tests are presented as tests of
that ansatz, with full matching and arbitrary-length coverage still open.
Background equation numbers are not used. The current manuscript and PDF
were updated in place; no additional archived draft was created.

## Established within the displayed models

- The relative gamma complex is closed, has the stated Hilbert adjoint and a
  surviving positive boundary class for every admitted input, and gives the
  exact gamma kinetic pairing. Transparent exteriors and interface cross terms
  are included. The infinite tower is a renormalized response; its raw source
  is not a vector in the unweighted direct sum.
- Primitive delay loops give the correct finite-interval return identity only
  with the escape reservoir. Mixed histories have their own Gram costs.
- The scalar derivative model's tangent does not determine its finite-coupling
  pairing. Its repetition coefficients fail exact arithmetic matching.
- For every fixed finite prime set, the exponential return generator defines
  a boundedly invertible translation multiplier and a positive relative
  response. Its logarithmic coefficients match every primitive repetition.
  An explicit continuous residual and both pole amplitudes remain.
- Fixed rational one-delay transfers cannot provide all of those repetition
  coefficients. In the one-prime range the old residual has a nonzero first
  derivative jump and infinite rank on every open input interval. Finite-rank
  boundary corrections cannot remove it.
- Compact high-frequency packets rule out completing that fixed model by
  pure relaxation of its unchanged energy, even with finitely many additional
  source amplitudes.
- A new positive splitting field has an exact all-input response. At mass
  `a = 1/2`, the choice `delta = 1/24` cancels the entire first-cusp coefficient.
  This is a genuine modification of the energy, with an explicitly computed
  differential, adjoint, minimizer, and pairing.
- The corrected residual has a fourth-order Fourier tail of strictly negative
  mean and therefore a nonzero third-derivative jump. Its compression is still
  infinite rank. Finitely many positive convex compliance splits retain this
  obstruction. A fixed positive derivative penalty restores an unmatched
  diagonal first cusp after the active shifted cusp has been canceled.

These are analytic statements proved in the manuscript, subject to the model
and parameter hypotheses stated there. They have not been independently
formalized or externally reviewed as a manuscript.

## Computations and their limits

Four programs reproduce the relative-complex and return controls, the scalar
finite-coupling comparison, the exact loop response, and the field modification.
They use explicit quadrature and exact rational arithmetic where stated, with
no Weil-matrix square root or zeta-zero input. The retained numerical records
are floating-point diagnostics, not interval enclosures.

For the specified smooth complex bump at `L = 1`, the fine-resolution defects
are approximately `Q - Z = -0.0008460031` and
`Q - Z_modified = -0.0008905513`. The positive field raises the response by
about `0.0000445482`. These values suggest failure of a further independent
positive addition for the chosen models; a rigorous sign exclusion from this
particular witness still requires a controlled enclosure. The analytic jump
and packet obstructions do not depend on certifying these numerical signs.

The current replay summary is in
[numerics/records/manuscript-replay.json](numerics/records/manuscript-replay.json).
Replay agreement verifies the recorded computations in the tested environment;
it does not certify quadrature tails or promote diagnostics into theorems.

## What remains open

The full Weil form has not been realized as this positive boundary norm. No
Ward identity determines the required coupling, contact, pole terms, or full
regular kernel. Arithmetic input is prescribed to the loop construction rather
than selected by topology. Compatibility under increasing support, transparent
gluing of the coupled system, and an all-prime or infinite-length limit remain
separate requirements. The finite-prime inverse bound is not uniform.

## Manuscript's next mathematical investigation, 12 September

Section 15 gives the next concrete test: derive one coupled two-mass system or
one nontrivial source modification from a positive bare action. Compute the
entire pairing before imposing any desired asymptotics. In a diagonal mass
description, the first two cancellation conditions already force a mixture of
relative softening and stiffening; the all-stiffening family cannot suffice.

At `L = 3/4`, match the contact and every active singular coefficient, then the
entire regular kernel and both pole amplitudes. A nonzero jump, residual,
negative bare mode, signed contribution, or loss of arbitrary-input coverage
is a stopping result for that proposal. A successful first-prime identity must
then survive `L = 5/4`, including prime 3, and above `log(4)`, including the
second prime-2 repetition and mixed endpoint histories. A separate useful task
is to turn the existing negative bump diagnostic into an interval certificate.

The preserved [continuation notes](archive/README.md) contain the historical
handoff details. They have not been edited to match this summary.

## Follow-up: quantum covariance investigation, 13 September 2026

The [quantum ground-state note](archive/notes/QUANTUM_GROUND_STATE_CORRELATIONS_20260913.md)
contains a subsequent investigation, separate from the current manuscript.
It gives an explicit Gaussian vacuum realization of the gamma tower and two
positive coupled mass models replacing its first two loop channels. Two fields
cancel the inverse-square, inverse-fourth, and inverse-sixth residual terms;
a third auxiliary field also cancels the inverse-eighth term. The surviving
inverse-eighth and inverse-tenth coefficients, respectively, are strictly
negative in the stated one-prime regime. Their derivative jumps retain an
infinite-rank residual, so neither model gives the full Weil pairing.

An exact shifted moment determinant excludes matching the first five residual
coefficients by any positive mass-matrix realization of the stated frequency
form with only those two original channels replaced. This restriction does not
cover all quantum models. The couplings are spatially nonlocal and prescribed;
the Gaussian correlations also admit classical positive realizations. No
quantum advantage exclusive to quantization, new positivity interval, or
arithmetic selection principle is claimed.

The new [calculation](numerics/check_quantum_covariance.py) and
[diagnostic record](numerics/records/quantum-covariance-diagnostics.json) are
separate from the four historical replay jobs. Exact rational identities support
the polynomial sign certificates; normal-mode and high-precision checks are
diagnostics, not interval enclosures. The manuscript source and PDF are unchanged.

## Follow-up audit and finite-block obstruction, 13 September 2026

The [new audit](archive/notes/QUANTUM_COVARIANCE_AUDIT_AND_FINITE_BLOCK_OBSTRUCTION_20260913.md)
independently verifies the gamma covariance normalization and domain, the two-
and three-field responses and sign certificates, and the residual jump and
infinite-rank arguments. The previous diagnostic record replays exactly in the
current environment. The earlier reference to positive cross correlations is
corrected: the displayed off-diagonal covariance is negative, while the matrix
is positive as a quadratic form. The finite-regulator displacement identity is
valid; an infinite displaced ground-state vector in the original Fock space
needs an additional summability condition, which the flat-kinetic gamma tower
fails for every nonzero input.

Replacing the first three or four original channels permits six or eight
consecutive moment matches using four or five positive Gaussian fields.
Exact rational moment matrices exclude the next match. More generally, an
explicit polynomial annihilating any finite block of N original masses gives
a negative shifted moment quadratic form at order 2N+1 for every q > 1.
This excludes matching through that order by any positive mass spectral
measure with those finite moments, irrespective of auxiliary dimension.

A separate theorem addresses interval compression without assuming phase-wise
matching: every finite-dimensional positive mass matrix analytic in the
one-prime phase, with frequency sI + M and fixed derivative-observable strength,
leaves an infinite-rank residual on every open interval. Factorial gamma
coefficients force a negative required odd moment at a finite order; the first
nonzero diagonal mean yields a derivative jump. The explicit new models have
inverse-fourteenth and inverse-eighteenth residuals with nonzero thirteenth
and seventeenth derivative jumps.

The classical auxiliary minimization gives the same responses. Larger finite
blocks therefore postpone the obstruction in this class, without establishing
a quantum advantage, a useful norm bound, full Weil positivity, or a new
positivity interval. Further work must control the complete residual and poles,
or change the observable, dispersion, or infinitely many original channels
with justified domains and convergence.

The [new checker](numerics/check_quantum_block_obstruction.py),
[diagnostic certificates](numerics/records/quantum-block-obstruction-diagnostics-20260913.json),
and [validation record](numerics/records/quantum-block-audit-validation-20260913.json)
are separate from all prior records. The manuscript, background, and historical
notes and records remain unchanged by this pass.

## Follow-up: superspace action and boundary Ward identity, 13 September 2026

The [new superspace note](archive/notes/SUPERSPACE_RELATIVE_BOUNDARY_ACTION_20260913.md)
quantizes each relative channel with one bosonic and two fermionic fields on
a positive Fock Hilbert space. It specifies the nilpotent charge, physical
adjoint, nonnegative Hamiltonian, one-coordinate cohomological superspace
action, and open coherent-state boundary conditions. Prepared source states
are harmonic fermionic ground states. Their complete Hermitian pairing
reproduces the gamma channel, including its contact.

A Ward identity protects that pairing under changes to the massive bulk
frequencies with the relative differential, Hilbert metric, and source classes
fixed. An unprepared boundary insertion is not protected at finite time.
A common channel preparation rate leaves its infinite-tower response
divergent. Choosing rates proportional to squared channel mass yields the
analytic bound

    0 <= Z_(T,lambda) - K <= 4 exp(-T/4)/(1-exp(-6T)) I.

This controls preparation uniformly on the full logarithmic form domain.
It is not a bound on the missing arithmetic correction.
A common-rate model also converges if its preparation time grows with the
channel cutoff: its error is at most exp(-T) times the sum of channel
weights, which grows as log N. The note distinguishes these source-norm
and convergence issues from superpotential non-renormalization, which does
not generally protect a Hermitian boundary metric.

At fixed first-prime coupling, the same construction gives the earlier
exponential-loop response. The arithmetic coupling changes the differential
and harmonic projection, and its pairing derivative is explicitly nonzero.
The residual's diagonal derivative jump and infinite rank survive. Protected
bulk deformations, smooth finite-time preparation terms, and net finite-rank
boundary corrections cannot complete this model to the full Weil target.
The protected response still equals the classical relative minimum energy.

The [checker](numerics/check_superspace_boundary_pairing.py),
[diagnostics](numerics/records/superspace-boundary-pairing-diagnostics-20260913.json),
and [validation record](numerics/records/superspace-boundary-validation-20260913.json)
are new. Exact finite Grassmann and rational identities are distinguished from
floating-point Fock, heat-kernel, and first-prime diagnostics. The continuum
claims and preparation bound are proved in the note. No full arithmetic
positivity or quantum-exclusive advantage is claimed. Further construction
must change the boundary pairing data or relative complex and derive the
complete response. The manuscript, background, brainstorming material, and
preceding notes and records are preserved.
