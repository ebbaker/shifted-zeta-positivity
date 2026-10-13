# Initial research program for rank two theta addition

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (`gpt-6.1-sol`), Codex; reasoning effort ultra, verified
from the recorded session configuration. Status: initialized, awaiting
Claude review. This initializes an exact identity test; no new factorization,
signed bound, numerical enclosure or RH theorem is claimed.

## Actual two-source state and observation

The genuine even source is \(m_t(u)=e^{tu^2}\Phi_e(u)\), with
\(H_t(x)=\tfrac12\int e^{ixu}m_t(u)\,du\). Quadratic observations
already contain the two-source state \(m_t(u)m_t(v)\). Its Newman
generator is multiplication by \(u^2+v^2\), and its physical projections
produce products of \(H\) and its fixed-time derivatives with the exact
Fourier and polynomial insertions.

The initial target can be one complete paired kernel,
\[
J_{j,t}(s)=\int r^2(r^2-s^2)^j m_t(s+r)m_t(s-r)\,dr,
\qquad j=0\ \text{or}\ 1.
\]
With the existing convention its Fourier response \(\widehat J_{j,t}(2x)\) is
\((H^{(j+1)})^2-H^{(j)}H^{(j+2)}\). On the relevant stationary sets these
responses connect to the two established collision-excluding signs.
This represents an existing quadratic observation. It adds no spectator
rotor or independent physical preparation to the scalar source.

## Established lattice seed and objective

In the full integer theta sums set \(a=n+m\), \(b=n-m\). The indices
have the same parity, so both the even-even and odd-odd cosets remain.
For positive source scales \(r_1,r_2\),
\[
r_1n^2+r_2m^2=
\big[(r_1+r_2)(a^2+b^2)+2(r_1-r_2)ab\big]/4.
\]
The resulting rank-two form is positive definite. In the physical integral
\(r_1=e^{4u}\), \(r_2=e^{4v}\) vary independently; the cross term
cannot be discarded. Classical addition and modular transformations with
characteristics supply established identity seeds. The objective is a
complete two-coset identity that exposes a new source-selected correlation
or structured factorization of the actual paired response.

## First bounded task

Choose \(J_0\) or \(J_1\), one modular generator, and a compact source
region with a declared tail. Write the full lattice expression before
transforming it. Transport all derivative insertions from the actual theta
source into the coupled quadratic form. Keep zero axes, zero-mode
subtractions, parity characteristics, modular factors and endpoint terms.
Derive the resulting two-coset integral before testing its sign. The first
deliverable is an exact physical reduction, a domain and convergence proof,
and the precise quadratic or integral-kernel inequality that remains.

## Validation and decision criteria

Verify the lattice bijection and both coset normalizations exactly. Use
the equal-scale addition formula only as a calibration; agreement at
\(r_1=r_2\) does not justify the unequal-scale integral. Compare the
transformed projection with the direct full-source kernel, restoring any
physical normalizer derivatives. Absolute majorants must justify lattice
summation, differentiation and integration in the declared order.

A small rigorous negative Gram minor can refute a proposed global
factorization; a positive finite matrix is not a proof of it. Positivity
of the lattice form guarantees convergence, not the sign of the
oscillatory Fourier response. Continue if the parity coupling yields a
nonredundant relation or a useful conditional factorization. Record an
exact obstruction if a mixed term or transformed endpoint prevents it.
Stationary equations belong to the complete response, never separately
to each coset. Any global extension still needs tails, cutoff transitions
and both multiplicity-relevant signs.

## Starting records

- [Brainstorm card 9](../../../inactive/brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#9-rank-two-theta-addition-and-the-two-source-parity-decomposition).
- [Complete paired kernels](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/7_COMPLETE_LAGUERRE_KERNELS_AND_TRIPLE_ZERO_LIMIT_20261010.md).
- [Full angular source](../../../../quasi-rh-exponent-descent/newman_collisions/notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md).
- [DLMF addition formula](https://dlmf.nist.gov/20.7.E14), [modular characteristics](https://dlmf.nist.gov/21.5), and [Riemann product identities](https://dlmf.nist.gov/21.6).
