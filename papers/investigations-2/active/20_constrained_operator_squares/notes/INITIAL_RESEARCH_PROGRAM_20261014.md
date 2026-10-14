# Initial program for constrained operator squares

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: gpt-6-astra (Codex), reasoning effort **ultra**.

The objective is an operator identity or estimate with a concrete
consequence beyond reformulating a known positive operator. The original
notes explored several consequences without completing one. The first
stage should preserve those possibilities while assigning a bounded test
to each.

## Common mathematical contract

Declare the Hilbert space, adjoint and operator domains. Distinguish
ordinary dissipative heat, first-order Dirac evolution, similarity
conjugation, Gaussian averages of conjugations, and backward Newman time.
A positive square of a generator does not by itself imply positivity of
an oscillatory matrix element.

Retain normal-ordering contractions, boundary values, source tails and
dynamical residuals before completing a square. All source-dependent
coefficients must be constructed from known input; taking the unknown
square root of the desired positive quantity is not a construction.

## First theorem and quantum use case

The [finite-time identities](RESIDUAL_CORRECTED_HEAT_TRAJECTORY_IDENTITIES_20261014.md)
are the first exact seed. For an approximate path u and A=A*,
r=u'+Au measures the evolution defect. Its integrated defect and the
terminal value supply explicit corrections to the two diagonal integrals
in Heat Quantum. Including these corrections gives the exact energy and
norm of the integrated trial state.

Next derive computable bounds for those corrections from quantities
available to the intended approximation. The first experiment should use
a small interacting fermion model with an exact-diagonalization reference
and a declared particle-number sector. Compare:

- the uncorrected diagonal heat quotient;
- the Rayleigh quotient of the integrated trial state;
- a certified residual-based upper enclosure for that quotient;
- direct variational optimization at a matched evaluation budget.

Use the same initial family, energy shift, finite time, quadrature
tolerance and state representation. Count the cost of residuals and
overlaps. A scalar or finite-matrix algebra check validates normalization,
not a correlation-energy advantage.

Pass if the method gives a useful certified energy bound, a demonstrable
cost advantage, or a sharp limitation explaining when the approximation
loses its variational meaning. Stop an implementation if evaluating the
correction simply reinstates a more expensive version of the original
problem without a distinct benefit. The exact identities are elementary;
literature comparison and a nontrivial advantage are needed before a
novelty or paper claim.

## Theta use case

For j=0,1, follow a differentiable stationary curve of
the j-th derivative of the unnormalized H. The exact seed is

\[
 \mathscr L_j(H;t,x_s(t))
 =\frac12\frac{d}{dt}
 [\partial_x^jH(t,x_s(t))]^2,
 \qquad \partial_x^{j+1}H(t,x_s(t))=0.
\]

Seek an explicit constrained identity of the shape

\[
 \mathscr L_j
 =\|\mathcal A_j\Psi_t\|^2
 +H^{(j+1)}M_j+\mathcal D_{\rm gluing,j}+E_j .
\]

Declare the domain and a finite-complexity ansatz before fitting it.
Full imaginary Jacobi gluing should eliminate the displayed defect for
genuine theta; the remaining square must pay every negative remainder.
The complete paired source, including cross sectors, must remain intact.
The exclusions in 06 continue to apply to separate positive-sector
factorizations.

Begin with j=0 on one declared compact cell. Test the identity on both
genuine theta and a control with a certified negative stationary margin.
The control must violate a displayed hypothesis or retain a quantitatively
sufficient defect. Passing j=0 is a first gate; j=1 remains necessary for
the broader all-multiplicity criterion.

Pass if a new source-derived identity gives a complete sign or a strictly
better controlled remainder. An algebraic square generator, a positive
integrated energy, a finite positive sample, or a factorization that drops
the cosine multiplier does not pass. A local success still needs global
time/height coverage and the existing continuation hypotheses before any
RH conclusion.

## Corrected smoothing machinery

Rebuild the 2017 density-smoothing argument using the heat semigroup
composition law and, where an operator implementation is wanted, Gaussian
averages of translation conjugations. A single similarity preserves
products; heat smoothing generally does not. The proposed finite-spin
trace formula must be independently checked rather than used to erase
this discrepancy. Preserve independent smoothing on the two density
factors and the normal-order subtraction.

The first source audit is in the
[three-note review](../reviews/THREE_SOURCE_NOTES_REVIEW_20261014.md).
Its corrections are a starting point, not a new global positive theorem.

## Possible paper endpoints

A quantum paper would need a residual-bound theorem with a useful
approximation or benchmark. A theta paper would need a source-specific
constrained factorization, a meaningful new estimate, or a rigorous
obstruction to a precisely stated operator class. A general methods paper
would need a nontrivial theorem connecting these constructions and at
least one demonstrated application.

The 2017--2018 notes need not be forced into a single manuscript.
Choose an endpoint after the first bounded tests. Do not write a
manuscript merely to package definitions and reformulations.

## Bounded continuation on 14 October 2026

Prepared for Edward Baker with substantial LLM assistance by `gpt-6.1-sol`
(Codex), reasoning effort **ultra**. The
[bounded decision](../reviews/BOUNDED_PROGRAM_AND_DIRAC_CONTINUATION_REVIEW_20261014.md)
records a useful interaction-specific quantum enclosure and its cost
limitation, the corrected Gaussian smoothing reconstruction, and rigorous
obstructions to local stationary multiplier squares. Certified stationary
boxes test both physical derivative levels and the positive-time Euler
control. These address the first bounded tests; the source-specific theta
positivity gate, scalable quantum advantage and novelty assessment remain
open. Continue the theta branch through the full nonlocal imaginary gluing,
rather than the now excluded full-core local multiplication class.
