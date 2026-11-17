# Assessment of the finite physical Jacobi heat defect

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. The reviewer and proof helper
were dispatched as **gpt-6.1-sol / ultra**. Separate backend attestation
and the lead's actual recorded settings are unavailable. The reviewer
authored E02 and assessed E01, both prerequisites of this proof. This is
a separate internal assessment of E03 r1 with shared prerequisites,
without specialist independence.

**Accepted within the frozen E03 r1 scope without mathematical
correction.** The pinned proof hash is
9e5323bfbc564bc0451b78e1aea4aeee9fb9355b29047467f827f5ccb9a6a828.
Its six original source hashes also match. The review checks the
finite defect, its sector bound, its exact contour contribution and
the scope of the matched cost comparison. The fixed-event followthrough
has its own request and lies outside this assessment.
[Assessment request][e05] [Execution request][e03] [Pinned proof][proof]
[B01 contract][b01] [Result index][results] [Avoid index][avoid]
[Shared-premise review pattern][shared]

## 1. Commutator, determinant and low degrees

The complete even normalized source has \(P_1(s)=s\) and \(h_0^*=1\).
Hence \(Z_\lambda'/Z_\lambda=\beta_1\), with a plus sign for
\(\beta_1\) when the heat operator is brought to the left. The sign
of the Volterra law for the tilted source is
\(\dot a_j=a_j(\beta_{j+1}-\beta_{j-1})/2\), where
\(a_j=\sqrt{\beta_j}\).
[Parent manuscript][manuscript]

For \(j\) indexing edge \((j-1,j)\), the two matrix products
in \([B,J_N]_{j-1,j}\) have terms
\(a_j\beta_{j+1}/2\) and \(a_j\beta_{j-1}/2\).
The first product loses the outgoing \(\beta_N\) on the
last retained edge. Since the derivative of its matrix entry with
respect to \(\beta_{N-1}\) is \(1/(2a_{N-1})\), the repair coefficient
is exactly \(\beta_N\beta_{N-1}\). Third-off-diagonal terms cancel
in pairs. Taking the exponential derivative in the commutator
direction gives \([B,f]_{00}=a_1a_2f_{20}\) when \(N\ge3\),
and 0 when \(N=2\). In both cases
\(-(J_N^2 f)_{00}+\beta_1 f_{00}\) cancels that entry.
This leaves (1) with its recorded positive last-edge prefactor.
[Pinned proof §1][proof]

The off-diagonal inverse cofactors contain the successive \(a_j\)
factors with positive sign and trailing determinant 1 or \(w\).
The two last-edge contributions to the \(00\) inverse derivative
are equal, cancelling the \(1/2\) from differentiation of the link.
With the prefactor from (1) this yields \(h_N^*w/P_N(w)^2\).
The \(N=2\) second cofactor reduces to the diagonal
\(\mathcal R_{00}=w/P_2\) because its link product is empty.
At \(N=1\), \(P_1(w)=w\) gives a simple residue equal to
\(h_1^*=\beta_1\), agreeing with \(G_1=1\). The retained-edge
derivative and the counted model pair have no \(N=1\) usage.
[Pinned proof §1][proof]

For \(N=2\), \(\dot a_1=a_1\beta_2/2\) gives
\(R_2=-a_1\beta_2 z\sin(a_1z)/2\). Grouping the four uniform
simplex coordinates into two pairs yields a \(\mathrm{Beta}(2,2)\)
weight, and rescaling to \([-1,1]\) gives density \(3(1-w^2)/4\).
Its transform is \(3(\sin t-t\cos t)/t^3\), with \(t=a_1z\).
The operator \(1+(t/3)\partial_t\) turns this into \(\sin t/t\).
The two cosine zeros on any fixed counted contour locally scale
as \(a_1^{-1}\), so \(\dot D_2=-\beta_2D_2\).
The residues \(\beta_2z_j/2\) of \(R_2/G_2\) give exactly this
contribution in (7), and the heat part has zero discriminant
contribution because \(G_2''/G_2=-\beta_1\).
[Pinned proof §§2–3][proof]

## 2. Phase and physical time

For \(q=2N\) doubled knots, the probability simplex yields the
normalized moment \(k!A_k/(q)_k\). The coefficient of \(w^{-1}\)
in \(w^\ell/P_N(w)^2\) first occurs at \(\ell=q-1\). One
\(z\)-derivative divided by \(i\) inserts \(w\), lowering the
prefactor to \((iz)^{q-2}/(q-2)!\) and adding
\(z\chi_N'/(q-1)\). Thus (3) has phase \((-1)^{N-1}\) and the
denominator \((2N-2)!\). The argument derives the particular
simplex formula by its coefficient series and uses the recorded
classical passage as background.
[Pinned proof §2][proof] [Passage record][passage]

Reflection pairs the knots. The second and fourth moments come
from \(A_2=S_2\) and \(A_4=(S_2^2+S_4)/2\), explaining the 2 and
12 in (4). Pairing the exponential product and using
\((q)_k\ge q^k\) gives (5). The centered estimate for \(\chi_N\)
costs \(|z|^2/2\), and that for \(\chi_N'\) costs \(|z|\)
against the same weighted second moment. Cauchy–Schwarz and
symmetry bound that moment by the square root of twice the
fourth moment times the one-sided exponential moment.
Substitution of \(t=2Y\) and \(q=2N\) yields exactly (6),
including \(1/(2N-1)\) and the positive denominator.
The inherited adjacent-link bound is uniform for
\(\lambda\in I\subset[0,1/2]\); \(\bar L_N<N\) makes the
exponent valid throughout \(0\le Y\le1\). The estimated phase
error is \(O(|z|^2\log^2(N+1)/N)\), with relative phase control
only where the allowance is below one. No differentiability
of the E01 error bound or model heat equation is assumed.
[Pinned proof §2][proof] [E01 assessment][e01review]

## 3. Signed margin and integration ledger

Contour time differentiation gives
\(\dot D_N=-(2\pi i)^{-1}\oint_\Gamma(z-c_N)\dot G_N/G_N\,dz\).
The scalar potential vanishes under this integral. The heat term
extracts 2 from the quadratic part and \(4D_NK_N\) from
\(2(z-c_N)Q_N'/Q_N=4+4D_N/Q_N\). The remainder enters with
the minus sign defining \(r_N\) in (7). At \(D_N=0\) the
identity simply reads \(\dot D_N=2+r_N\).
Both the physical and model contour derivatives require the
outer modulus floor and remain finite through pair merger.
The E02 transfer in (8) preserves its own counted-pair and
collar hypotheses and both denominator costs.
[Pinned proof §§3–4][proof] [E02 proof][e02]

With \(W_N'=-4K_NW_N\), the signed residual enters positively
when recovering the physical margin from \(W_N(x)D_N(x)\)
in (9), as it does for the difference \(D-D_N\) in (10).
The latter's extra interaction term is bounded using
\(|D|\le(\rho-b)^2\). The bound for
\(|\mathcal C-\mathcal C_N|\) uses \(e^{E_K}-1\) before
time integration, retaining the time-dependent weight.
Substitution of the exact model identity in the left-hand
expression of (11) reduces that expression to
\(L_v-\mathcal C_N(u)-\mathfrak T_N^+(u)\).
Thus the identities permit a different computation of model
terms but supply no gain by themselves. In the exact quadratic
control with zero defect the strict inequality is saturated
at the event, as required by the physical time orientation.
[Pinned proof §§4, 6][proof]

The evaluation ledger keeps the inner signed primitive error
inside the exponential, and pays the product error for the
signed residual against the computed weight. Formula (13)
follows from three differences in order: numerator,
denominator, center. The reciprocal error uses
\(m_N(m_N-\gamma_G)\) and the center error uses the
approximate denominator lower bound \(m_N-\gamma_G\).
The factor \(g=2\rho-b\) bounds the original center offset
on \(\Gamma\). Contour integration, time quadrature or
interpolation, exponent evaluation, and the two model endpoint
values have separate enclosures. In particular neither time
integration is justified by a finite set of model samples.
No published coefficient values, incoming gap or canonical
collision-free slab enter this proof.
[Pinned proof §4][proof]

## 4. Rate comparison and scope

The retained head needs the actual links through \(\beta_{N-1}\).
The finite residual adds just \(\beta_N\), with the physical
coefficient derivatives eliminated by the Volterra law. The
same actual links buy \(G_{N+1}\) at that time. The residual
phase uses retained nodes only, while its degree-only envelope
needs no actual links. The exact next-head error uses
\(\beta_{N+1}\) through its amplitude and the complete measure
through its phase. Bounding \(\beta_{N+1}\) by
\(B_N-\beta_N\) or \(B_N\) allows the comparison at the same
prefix. Equality of these coefficient counts is pointwise in
time. Acquiring usable time-slab enclosures remains separate
from acquiring coefficients at an endpoint.
[Pinned proof §5][proof] [E01 assessment][e01review]

For (15), the two exact prefactors divide to
\(\Pi_N/(\beta_{N+1}|z|^4)\). The two phase disks give the
two-sided ratio on fixed nonzero compact sets when \(p,q_*<1\).
This compares actual residual and field error at a point.
The contour and time comparison is instead between the
specified uniform upper allowances. In (17) and (18) the
matched geometry makes \(C_\Gamma=Lg/(2\pi)=\rho(2\rho-b)\)
cancel. The residual contour denominator contributes \(1/m_N\).
Writing \(\delta_+=m_{N+1}\eta\) gives the floor ratio and
\(\eta/[-\log(1-\eta)]\) in (19). The remaining ratio of field
budgets keeps \(\Pi_N/(\overline\beta Z_*^4)\) and the
factor \((1+p)/(1+q_*)\). A bound \(M\) on \(K_N\) gives
the factor \(Q_\Delta(M)=\int_0^\Delta e^{4Mt}\,dt\),
including the limit \(\Delta\) at zero.
[Pinned proof §5][proof]

With comparable modulus floors, a fixed circle in the paid
strip, \(0<\eta\le1/2\), bounded \(M\), and
\(\overline\beta=B_N\), the allowance ratio has order
\(\Delta N^4/\log^2(N+1)\) for large \(N\).
The specified hypotheses keep \(Q_\Delta(M)/\Delta\) and
\(\eta/[-\log(1-\eta)]\) bounded above and below when
\(\Delta>0\). This rate includes the elapsed time even for
short slabs. It imposes no corresponding lower bound on
\(\mathfrak R_N\), its evaluation cost, or the sign of the
physical margin. The direct comparator pays the next head's
own count, collar and buffer. Direct source evaluation pays
the separate mass and Fourier numerator budgets, combined
by the normalization inequality stated in §5. The signed
model contribution, transfer and endpoint costs remain to be
enclosed for an actual comparison.
[Pinned proof §5][proof]

The analytical screen respects the recorded control scopes.
Weighted-square controls can pass the uniform law and envelope
yet collide, while missing unchanged canonical arithmetic.
The Euler witness supplies neither a family-wide coefficient
failure nor a counted local pair. The reflected, smooth and
primitive controls have their separate confinement verdicts,
and atomic laws retain the necessary positive-norm degree
restriction. Finite-prime and score matches do not imply
fixed-region events. RH-conditional endpoint controls retain
RH and fail ordinary Dirichlet arithmetic. Changed kernels and
profile relaxations lack the specified physical observation
or field. No control witness was recomputed. The accepted
limitation concerns the norm-only allowances (16)–(19) with
their stated data and geometry. Canonical acquisition and a
signed improvement over the matched direct comparison remain
open.
[Pinned proof §6][proof] [Controls catalog][controls]

[e05]: ../research-progress/handoffs/VCD-GT-E05-r2.md
[e03]: ../research-progress/handoffs/VCD-GT-E03-r1.md
[proof]: ../notes/05_VCD_GT_E03_PHYSICAL_MODEL_DEFECT_20261116.md
[b01]: ../brainstorm/notes/01_VCD_GT_B01_SIGNED_DEFECT_DECISION_20261116.md
[manuscript]: ../../manuscript/main.tex
[passage]: ../../references/04_QUADRATURE_ERROR_PHASE_PASSAGES_20261116.md
[e01review]: 02_VCD_GT_E01_TIME_EXTENSION_ASSESSMENT_20261116.md
[e02]: ../notes/04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[shared]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
