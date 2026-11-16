# ITP-E03 internal analytical manuscript assessment

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Recorded worker dispatch
**gpt-6.1-sol / ultra**. Independent backend metadata unavailable.

**Accepted as an analytical draft within the frozen scope.** This is a
same-worker check of [the integrated manuscript](../manuscript/main.tex)
against [the original proof](../notes/02_ITP_E01_EXACT_CELL_PHASE_TRANSFER_20261113.md)
and its [prior assessment](01_ITP_E02_EXACT_CELL_PHASE_ASSESSMENT_20261114.md).
It shares their source and mathematical premises and has no independent
specialist review. The
[integration note](../notes/03_ITP_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md)
records the complete proof map and the collision-control screen.

1. **Complete source.** At zero argument and lattice parameter \(it\),
   Jacobi's identity uses the positive square root \(\sqrt t\).
   Applying \(\partial_u^2-1\) to the reflected primitive yields smooth
   evenness. Termwise differentiation gives \(2r^2-3r\) and positivity
   for \(u\ge0\). For the Mellin split the elementary term integrates to
   \(1/(s-1)-1/s\), giving \(1/2\) after multiplication by \(s(s-1)/2\).
   The primitive boundary derivative is \(-1/2\) and \(t=\exp(4u)\)
   contributes the factor \(8\) in the integral with both reflected
   powers. These constants give \(H_0(z)=\xi(1/2-iz/2)/8\).
2. **Mass preparation and topology.** Child masses add to the parent.
   Column norms in the source-dependent splitting isometry are one,
   and distinct columns have disjoint child support. Appending the
   uniform reference bit, in contrast, sends the normalized indicator
   of a parent to the same function represented by its two children.
   This identifies the common Hilbert space with \(L^2(\mathbb R,du)\).
   The cell vector with components \(\sqrt{m_{L,j}}\) represents
   \(\sqrt{P_hW_\lambda}\), and the root inequality controls its
   squared weighted \(L^2\) error by the weighted density error.
   Local source products are justified by compact interval minima,
   parent oscillations and exact telescoping. The proof uses no
   uniform relative gate bound across the spatial tail.
3. **Cell phase and field error.** Local phase products converge
   uniformly for \(z\) on compact sets. Conditional integration on
   the cell gives the entire sinc term exactly. Absolute local
   uniform convergence of the sum follows from the genuine
   exponentially weighted complete masses, including the half-cell
   weight change. The derivative kernel \(2(t-a)(a+h-t)/h\) has
   maximum \(h/2\). The weight ratio is at most \(e^{8h}\) and the
   Fourier factor adds another \(1/2\). Splitting the true integral
   at the aligned cutoff pays the exterior once. The estimate of
   the integral uses \(|e^{izu}|\le e^{8|u|}\) and permits every
   real \(x\).
4. **Variation and tail.** The differentiated source polynomial has
   coefficient sum 53, and the first polynomial has sum 5. The \(n=2\)
   term of \(C_3(0)\) is \(<1/8\) and subsequent terms have successive
   ratio \(<1/2\). The quadratic used for \(\rho/2-u^2/2-9u\) has
   minimum \(30/23\). Reflection and the factor \(1/(4\rho)\) give
   \(V_8\le8B_1+2B_0<868\). Reflection cancels the \(1/2\) in the
   field tail. At \(U=2\), \(\rho_2>64\) gives the tail allowance
   \(330/2^{32}\), and \(L=30\) gives cell allowance \(1736/2^{32}\).
   Their sum \(2066/2^{32}\) is strictly below \(5\cdot10^{-7}\).
5. **Limits of the comparison and arithmetic.** At the alias
   frequencies the full-line center-point lattice has common
   modulus \(Z_\lambda/2\), while the derivative estimate forces
   the exact field to decay to zero. The comparison is scoped to
   that fixed-level lattice and supremum over all real heights.
   Exact step-density integration yields the same value as the
   tensor readout. Reverse-time differentiation of the projected
   source uses \(P_h(u^2W)\). Each future error term spends at most
   \(10^{-6}/4\) if proved on the stated domain. The branch has only
   exact definitions for the \(2^{32}\) formal masses and the
   computation remains unpaid. The challenges section retains this
   distinction and gives the required rank, global relative gate,
   time and signed-field questions.

The integrated proofs preserve the original status and numerical
allowances. No mathematical correction or numerical run was required.
Build details and file identities are in the
[build record](../numerics/02_ITP_E03_MANUSCRIPT_BUILD_20261114.json).
