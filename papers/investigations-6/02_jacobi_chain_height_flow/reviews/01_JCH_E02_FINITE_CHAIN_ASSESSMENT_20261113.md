# JCH-E02 r1 — Scalar finite-chain proof assessment

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The execution dispatch selected
**gpt-6.1-sol / ultra**. Actual backend model and effort unavailable.
**Disposition: accepted with the original scope and practical limitations.**
This is a separate internal assessment by the E01 worker sharing its
sources. It is neither independent specialist review nor a certificate.

The [E02 request][request] has SHA-256
`3c6786e5be5fcbfa7dd793baeaee7f4965ba9ff9a577093ffd11b44aebcb3bf2`.
All four entries in its freeze and all nine source entries in the pinned
E01 manifest matched. The [E01 request][e01], [return][return] and
[derivation][proof] were checked in their frozen versions.

| Item | Check and disposition |
| --- | --- |
| R1 source and clocks | In the fixed polynomial basis \(e_0\) maps to \(1\) for the probability measure \(\mu_*\). The scalar spectral expectation multiplied by \(Z_*/2\) restores the original field. The exact multiplier is \(e^{-\tau u^2}\), giving \(\partial_\tau H=H_{xx}\) and \(\partial_\lambda H_\lambda=-H_{\lambda,xx}\). The readout uses real \(x\) and nonnegative \(\tau\), where the functional calculus is bounded. The higher moment used below leaves the calculation on the same physical interval. |
| Finite rule and omitted coupling | The tridiagonal determinant recursion gives \(P_N\). The eigenvector recurrence forces a nonzero first component, so the real eigenvalues are simple and the weights positive. Conjugation by parity makes the finite scalar measure even. A walk hitting \(N\) and returning has length at least \(2N\). This proves exactness through \(2N-1\); at degree \(2N\) the walk over the omitted edge contributes \(\prod_{j=1}^N a_j^2\). The leading-coefficient identity gives this same product as \(h_N\) with \(h_0=1\). |
| Full-line interpolation | For each \(u\) outside the nodes, subtract the interpolant and a multiple of \(P_N^2\) to force a zero at \(u\) and double zeros at the nodes. Repeated real Rolle then finds a \(2N\)-th derivative zero on the finite convex hull of those points. A bound on that derivative of the cosine function applies regardless of which side of the node range contains \(u\). Coincident points satisfy the interpolation equalities directly. \(P_N^2\) has finite integral, so the pointwise bound yields the integrated \(h_N\lvert s\rvert^{2N}/(2N)!\). |
| R2 and endpoints | Averaging \(s=x+\sqrt{2\tau}G\) against cosine gives the multiplier before integration. Fubini uses bounded cosine and finite measures. After expansion, the even Gaussian moments give coefficient \((2\tau)^k(2k)!/[2^k k!(2k)!(2N-2k)!]\) in \(x^{2N-2k}\), as requested. \(\tau=0\) gives pure height, \(x=0\) gives \(\tau^N/N!\), and both zero give equal scalar values. \(J_1=0\) has exact scalar \(Z_*/2\) and R2 allowance \(Z_*a_1^2(x^2/2+\tau)/2\). |
| R3 and R4 | \(u^N\) is a valid competitor for the monic norm and \(u^{2N}\le N!e^{u^2}\). At the rectangle corner each reindexed coefficient has \((N)_j\le N^j\) and \(T_0=1/2\), hence the factor \(\cosh(X\sqrt{2N})\) and \(C_*=Z_*M_1/2\). With \(y=\sqrt N\), \(Ly^2-by\ge d\) implies \(C_*e^{-LN+b\sqrt N}\le\epsilon\). The nonnegative root cutoff works if \(X=0\) or \(d=0\); the common zero case uses \(N\ge1\). |
| Boundary and comparison | The discarded rank-one boundary term in the compressed square is \(\Pi_NJ_*(1-\Pi_N)J_*\Pi_N=a_N^2\lvert e_{N-1}\rangle\langle e_{N-1}\rvert\). The frozen scalar evolves \(J_N^2\). Projecting the exact state would retain its \(e_0\) coefficient identically. The same \(N\)-node Gaussian quadrature gives exactly the same weights, nodes, normalization and \(\tau,x\) output, so no acquisition or evaluation gain is established. |

The [control screen][screen] and [catalog][controls] preserve each
failure of the theta premises. The direct three-atom check gives
\(e^{-\tau}p/(1-p)=1\) at \(\tau=1/2-T\), so the exact three-node value
and its first derivative vanish at \(\pi\), with second derivative
\(2\). The finite chain terminates and has zero scalar defect there.
Atomic fixed-event and finite-profile families also terminate when
their full signed-coordinate support is used. Compact continuous
extensions keep the required moments. Euler-factor sources have
unchanged Gaussian integrability but changed arithmetic coefficients.
Even extensions of weighted squares meet the integration hypotheses
while full smooth reflection fails. The reflected super-Gaussian
and smooth shape/primitive sources preserve the required moments
without canonical square arithmetic. Each fixed finite-prime-orbit
source retains enough domination and lacks full reflection. Conditional
endpoint controls keep their conditional status and lack ordinary
Dirichlet-series arithmetic. These bounds apply at a witness when it
lies in the chosen box. The changed observation-kernel control fails
the cosine/Newman premise even with the same source measure.

The surviving result is an absolute approximation on the frozen real
rectangles. At a control zero the estimate forces the absolute bound
to dominate the approximate value, even with exact scalar output.
A relative lower margin remains unpaid. In practice the required
enclosures cover \(a_1,\ldots,a_N,Z_*,M_1\) as applicable, or a direct
upper enclosure for \(Z_*M_1/2\) if using R3. Source-tail integration,
moment-to-coefficient conditioning and finite evaluation rounding
remain part of certification. The proof does not acquire them.
No correction is requested, so the optional response check is unused.
There is no surviving prerequisite for completing this assessment.

The [results index][results] and [avoid index][avoid], especially
[classification][a01], [control-premise rule][a02] and [scope][a07],
guide this intermediate estimate and its limitations.

[request]: ../research-progress/handoffs/JCH-E02-r1.md
[e01]: ../research-progress/handoffs/JCH-E01-r1.md
[return]: ../research-progress/handoffs/JCH-E01-r1-return.md
[proof]: ../notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md
[screen]: ../notes/01_JCH_B01_SOURCE_AND_CONTROL_SCREEN_20261113.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
