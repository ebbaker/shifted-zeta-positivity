# Initial research program for theta volterra integrability

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6.1-sol`; reasoning effort: ultra.
Status: initialized, awaiting Claude review. No recurrence-coefficient run,
new Darboux invariant or signed certificate is reported by this note.

This project develops [brainstorm card 14](../../../brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#14-orthogonal-polynomial-volterra-flow-and-integrable-transformations).
Its objective is a transformation tied to the actual theta preparation
that constrains its physical observation beyond generic integrability.

## Actual source generator and Jacobi observation

Use the complete even extension of
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}},\qquad u\ge0.
\]
For \(m_t=e^{tu^2}\Phi_e\), the source generator is multiplication by
\(u^2\), and \(H_t(x)=\frac12\int e^{ixu}m_t(u)du\). This fixed projection
gives backward heat \(\partial_tH=-\partial_x^2H\). Complete theta decay
pays polynomial and Gaussian-weighted moments on compact time intervals.

Let \(p_n\) be monic orthogonal polynomials for \(m_t(u)du\), with norms
\(h_n\). Evenness gives
\[
up_n=p_{n+1}+a_np_{n-1},\qquad
a_n=h_n/h_{n-1}>0\ (n\ge1),\quad a_0=0.
\]
In the orthonormal basis, the selfadjoint Jacobi operator \(J_t\) has
off-diagonal entries \(\sqrt{a_n}\). Its spectral measure at \(e_0\) is
\(\rho_t=m_t/(2H_t(0))\), so
\[
C_t(x)=H_t(x)/H_t(0)=\langle e_0,e^{ixJ_t}e_0\rangle.
\]
Gaussian exponential moments ensure moment determinacy and justify this
source-selected spectral realization.

## Established seed and the missing statement

Differentiating norms and using orthogonality yields
\[
\partial_t\log h_n=a_{n+1}+a_n,\qquad
\dot a_n=a_n(a_{n+1}-a_{n-1}).
\]
This is the actual theta Volterra flow recorded in the brainstorm. On the
polynomial core, integration by parts gives
\(D+D^*=W_t'(J_t)\), with \(W_t=-\log\rho_t\) and differentiation matrix
\(D\) in the orthonormal basis. Its matrix elements retain the complete
nonpolynomial theta score. The basis changes with time and its derivative
must enter a proposed Lax or observation intertwiner.

[Clarkson–Jordaan–Loureiro](https://arxiv.org/html/2504.08522) provide
orthogonal-polynomial and Volterra context for a polynomial Freud weight.
Their particular source/string equations are not theta equations. The
[existing finite matrix scout](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/14_integrable_lax/notes/1_MATRIX_HEAT_LIFT_AND_COMPACT_THETA_REMAINDER_20261010.md)
also shows that a universal rank-one heat commutator survives a prescribed
positive-time collision.

Seek an independently defined Darboux, Christoffel, contiguous or Lax
transformation preserving actual source preparation and forcing either a
regular nonzero value-and-slope source identity or the two
[stationary sign restrictions](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md).
A transform must specify its altered measure, spectral observation, endpoints
and generator. This is the missing arithmetic constraint, not a consequence
of \(a_n>0\).

## First bounded task and stopping condition

Enclose full theta moments through degree 16 on a declared small time box.
Recover \(a_1,\ldots,a_8\) and a small score/string matrix block, recording
Hankel determinant conditioning and all omitted tails. Check recurrence,
norm evolution, the orthonormal square-root convention, and the source
integration-by-parts identity independently. Repeat the same diagnostic
for the smooth positive collision control.

Continue if one non-generic theta relation survives complete source payment
and leads to a named conditional observation estimate. Only then choose a
transformation and compute its heat defect, changed initial data, and zeros
introduced or removed by its factors. Stop if the diagnostic returns only
positive recurrence coefficients, generic string relations or universal
Volterra integrability.

A finite Jacobi block needs its next coefficient and is not a closed
invariant heat system. Setting that coefficient to zero manufactures a
closure. A Darboux coefficient defined by \(H_x/H\) is singular at the
collision being investigated. Finite matrix representations can avoid that
chart, but require a regular physical reduction and honest cutoff payment.
No conclusion about global collision exclusion or RH follows from this
initialization.
