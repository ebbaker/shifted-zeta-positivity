# ITP-E02 r1 — Assessment of the exact-cell strip transfer

13–14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Recorded dispatch **gpt-6.1-sol /
ultra**; independent backend metadata unavailable. **Same-worker internal
analytical assessment** using the E01 source and branch premises. The
[frozen assessment request](../research-progress/handoffs/ITP-E02-r1.md),
its four pinned files and the 22 entries of its nested manifest all matched.

**Accepted as proved in-note for the stated exact-source approximation
and center-phase comparison.** No mathematical correction or response
check is required. The [E01 proof](../notes/02_ITP_E01_EXACT_CELL_PHASE_TRANSFER_20261113.md)
and [return](../research-progress/handoffs/ITP-E01-r1-return.md) meet the
frozen request at the original tuple.

1. **Cell constant and topology.** A derivative point at distance \(t\)
   from the left cell edge has pair measure \(2t(h-t)\) in the double
   integral. Dividing by \(h\) gives a kernel bounded by \(h/2\).
   Multiplying by the weight ratio \(e^{8h}\) gives the weighted
   prepared-amplitude estimate. The \(1/2\) in the literal Fourier
   transform brings the field coefficient to \(he^{8h}/4\). Local ratios
   telescope in scale order on integer slabs, with positive denominators
   there and gate support through the \(k\)-th bit at level \(k\). The
   weighted source estimate justifies the whole-line passage uniformly
   in time, with no uniform floor across slabs needed.
2. **Derivative and tail arithmetic.** The derivative of one theta term
   gives the polynomial \(-8r^3+30r^2-15r\), with coefficient sum 53.
   The \(n=2\) contribution to \(C_3(0)\) is \(64e^{-3\pi}<1/8\), and
   each subsequent ratio is bounded by \((3/2)^6e^{-15}<1/2\). The
   quadratic \(23u^2/2-3u+3/2\) has minimum \(30/23\), which proves the
   exponential domination used after differentiation. Reflection and
   the Jacobian \(d\rho/(4\rho)\) give \(V_8<8(106)+2(10)=868\). The
   cutoff proof splits the true integral and pays its exterior once. Its
   tail integrates \(\rho e^{-\rho/2}\) with coefficient \(B_0/4\),
   since the Fourier factor cancels the double half-line tail. For
   \(U=2\), \(\rho_U>64\) gives \(T_8(2)<330/2^{32}\). At \(L=30\), the
   cell term is \(<1736/2^{32}\). Their sum is \(<2066/2^{32}<5\cdot10^{-7}\).
3. **Literal field and comparison.** Centering the cell integral yields
   exactly \(\operatorname{sinc}(zh/2)\). Absolute convergence of the
   sums on fixed strips follows by comparing cell-center and in-cell
   weights. The field bound applies for arbitrary real \(x\) and
   \(|y|\le8\). Phase product convergence on compact \(z\) sets alone has a
   weaker quantifier. At \(x_k=2\pi k/h\) the point phases are identical
   across all cells up to the common sign \((-1)^k\). Since the exact
   integrable source has integrable first derivative and vanishes at
   infinity, the true field decays along this sequence. The limit of the
   actual errors is \(Z_\lambda/2\) at each fixed level and time. The
   matched direct integration baseline has the exact cell network value.
4. **Time and costs.** Projecting the exact source at each time gives
   the derivative \(-P_h(u^2W)\) in reverse time. Multiplication of a
   positive step density by \(u^2\) is different inside a cell. The
   finite scheme therefore supplies projected samples of the source
   orbit. The ideal allowance excludes numerical source or contraction
   errors, which are zero only in the exact construction. The proposed
   future mass and readout terms each spend at most \(2.5\cdot10^{-7}\)
   if established on the same domains. The \(2^{32}\) formal cells,
   acquisition of their complete masses and growing supports remain
   visible. No realized cost, rank advantage or relative accuracy is
   established.
5. **Controls and interpretation.** The E01 table distinguishes
   weighted regularity, the positive local ratio hypothesis, canonical
   theta arithmetic and the literal observation. In particular the
   reflected quartic and damped Gaussian-polynomial witnesses retain
   weighted regularity and can satisfy the generic projection theorem
   at their collisions. Atomic witnesses lack the density premise.
   Triangular extensions recover weighted regularity while admitting
   zero-mass cells. Finite-square and finite-prime witnesses lack the
   complete coefficient/reflection conjunction, and the variable-kernel
   witnesses lack the literal observation. The RH-conditional endpoint
   witness remains conditional and lacks ordinary Dirichlet arithmetic.
   The actual-profile relaxed measure is a zero-profile object, outside
   the stated density input. The screen does not assign the same theta
   constant to the controls. See the
   [result index](../../../../result-summaries/README.md),
   [controls 12](../../../../result-summaries/12_collision_controls_and_screening.md)
   and [avoid index](../../../../avoid/README.md), especially
   [the control-premise rule](../../../../avoid/02_shape_only_arguments_and_the_controls.md)
   and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

This closes the declared ITP task sequence at the approximation milestone.
Any signed, relative or Green-log consumer would require a separate
premise and scope decision. No numerical replay or new mathematical
input was used.
