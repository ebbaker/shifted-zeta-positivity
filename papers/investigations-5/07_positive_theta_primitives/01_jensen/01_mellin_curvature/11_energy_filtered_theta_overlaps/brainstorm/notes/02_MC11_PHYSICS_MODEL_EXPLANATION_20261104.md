# Thermal model and auxiliary representation of theta determinants

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6-astra (Codex), reasoning effort xhigh**, recorded for this turn. Thread `01a1a9d4-3d44-7472-ae0f-54705423d86b`, MC11 history0002. Explanatory continuation of [the progress summary](01_MC11_PROGRESS_AND_OPEN_QUESTIONS_20261104.md); this note reconstructs the existing model and introduces no new estimate or assessment.

**Terminology revised 4 November following the author’s objection.** See [the distinction between thermal parameters and auxiliary source functions](03_MC11_THERMAL_PARAMETER_AND_ORBITAL_TERMINOLOGY_20261104.md). The particle in a box supplies the canonical square-energy spectrum. Two families of auxiliary source functions give an exterior-product representation of the determinant. The box states live in position x; the source functions depend on u, which labels inverse temperature. The equations do not identify these functions as physical one-particle orbitals or their pairing as a measured quantum amplitude.

## The box and the filter

Take one free quantum particle between hard walls at x=0 and x=1. In the chosen units,
\[
H=-\pi^{-1}\frac{d^2}{dx^2},\qquad E_n=\pi n^2,\qquad n=1,2,\ldots,
\]
with Dirichlet boundary conditions. The square spectrum is the reason a theta sum appears. At inverse temperature beta, level n carries the unnormalized Boltzmann weight exp(-beta E_n).

An energy-selective filter always accepts the ground level and accepts every excited level with probability s. Its effect is
\[
W_s=P_1+s(I-P_1),\qquad 0\le s\le1.
\]
The accepted thermal weight is
\[
Z_s(\beta)=\operatorname{Tr}(W_s e^{-\beta H})
=e^{-\beta\pi}+s\sum_{n\ge2}e^{-\beta\pi n^2}.
\]
At s=0 only the ground level passes; at s=1 all levels pass. The Hamiltonian and energies stay fixed. Changing s changes spectral acceptance and does not describe time evolution or an increase in particle number. The calculation retains the accepted weight instead of dividing by Z_s to normalize it. [MC11 overview](../../research-overview/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md)

## From thermal weights to a source

Set beta=exp(4u), with u>=0, and form
\[
p_s(u)=e^uZ_s(e^{4u}),\qquad
\Phi_s(u)=\frac{p_s''(u)-p_s(u)}8.
\]
This specified transform of the heat trace produces the positive source used by the investigation. It is not an arbitrary choice of a thermal observable: it is the source entering the Riemann xi representation when the complete unit-weight spectrum is restored.

The coefficients are moments over the temperature coordinate,
\[
c_j(s)=\int_0^\infty\frac{u^{2j}}{(2j)!}\Phi_s(u)\,du.
\]
Thus the overlap combines the thermal data over beta>=1. It is not just a determinant of energy eigenfunctions at one temperature. Here u is neither box position nor laboratory time.

## Two function families from the same source

In the auxiliary source Hilbert space L²((0,infinity),du), use
\[
f_i^{(s)}(u)=\frac{\Phi_s^{(2i)}(u)}{\sqrt{\Phi_s(u)}},
\qquad
g_\ell^{(s)}(u)=\frac{u^{2\ell}}{(2\ell)!}\sqrt{\Phi_s(u)}.
\]
The f family uses even derivatives of the source; the g family uses polynomial weighting of its square root. Their labels count derivative or moment order, not box energies. These functions provide an auxiliary Hilbert-space representation; no physical preparation protocol or source-space energy interpretation is established by these formulas.

For the diagonal blocks used in MC11, integration by parts gives
\[
\langle f_i^{(s)},g_\ell^{(s)}\rangle=c_{\ell-i}(s),
\qquad 0\le i<q,\quad q\le\ell<2q.
\]
The index range ensures the required lower-endpoint cancellations even along the filtered path. Form exterior products of the two ordered lists of q source functions:
\[
F_q=f_0\wedge\cdots\wedge f_{q-1},\qquad
G_q=g_q\wedge\cdots\wedge g_{2q-1}.
\]
Their overlap is exactly
\[
D_q(s)=\langle F_q,G_q\rangle
=\det[c_{q+j-i}(s)]_{0\le i,j<q}.
\]
An order-three result therefore concerns two exterior products, each containing three auxiliary source functions. The physical heat trace supplying the source remains a one-particle trace. Physical fermionic states in this auxiliary space would require a separately specified realization. [Original source-state explanation](../../../08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md)

## Why positive weights can give a negative response

The determinant pairs two different function families. It is a cross-pairing, not a squared norm. Exterior algebra supplies alternating permutation signs. At order two,
\[
D_2=\det\begin{pmatrix}c_2&c_3\\c_1&c_2\end{pmatrix}
=c_2^2-c_1c_3.
\]
The two determinant terms have opposite signs. Increasing every coefficient does not determine which product grows faster. This explains algebraically how adding a positive spectral contribution can lower the determinant; identifying it with a physical exchange process requires additional justification.

MC11 computes the unnormalized real exterior-product pairing in a fixed ordering. A normalized pairing would divide by ||F_q|| ||G_q||. Its squared modulus has the mathematical form of a projection probability, but a physical probability interpretation requires specified preparations and a measurement. Those norms also depend on s, so the computed change in D_q does not directly give the change in the normalized pairing.

## The question the model makes precise

Increasing one level's weight changes the common source and therefore both source-function families. MC11 computes the response of their determinant under that change. The response is not the result of projecting two fixed physical states onto one energy level. When all excited weights rise together, the cofactors are evaluated along the same path, retaining the mixed effects of the levels. [Energy-response explanation](../../../10_radial_green_determinants/brainstorm/notes/02_HILBERT_SPACE_AND_ENERGY_RESOLVED_CANCELLATION_20261104.md)

The fixed-order findings summarized in Note01 say that the excited spectrum lowers the order-two determinant and raises the order-three determinant, with the first excited level dominating the latter gain. The latter is the E03 return submitted for the parallel E04 assessment. The calculation identifies the spectral dependence of the competing signed terms; extending their quantitative control to increasing order and neighboring shifts remains open.

For context and scope, see the [result index](../../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../../avoid/README.md), especially [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [joint estimates](../../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The Hilbert-space interpretation preserves the signed determinant; positivity of the heat trace alone does not supply the missing determinant estimates.
