# MC08-E06 r1: finite quadratic-clock derivations and exact checks

3 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual **gpt-6.1-sol (Codex), reasoning effort ultra**, public chat `01a19fdd-4e1e-7061-9ec4-141ca78368ce`, turn `01a19fde-8bbc-7272-9992-861e1ce88b68`. Configuration was read from the local session metadata. Three read-only inherited same-model support agents checked regularity, finite signs and source/inheritance; their checks share premises and are not specialist validation. This chat has its own brainstorm history **0002**.

**Type E; Handoff07 r1 executed.** The finite claims below are proved in-note in the specified class and assessed in [Review01](../reviews/01_MC08_E06_QUADRATIC_CLOCK_ASSESSMENT_20261103.md). All five frozen input hashes match; the assessment records them. No correction of a frozen source was needed. The generic completion supplies no new theta sign, neighboring-index estimate or Mellin range. General endpoint-channel equality is outside this packet; its precise comparison equation is retained below.

Read with the [result index](../../../../../../../../result-summaries/README.md), [theta/physical cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [control inventory](../../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../../avoid/README.md), especially [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [scoped exclusions](../../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [joint signed estimates](../../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). This is a representation/regularity result, not a new positivity criterion. The inherited all-sector sign reformulation remains RH-equivalent and is not supported anew by these checks.

## 1. Fixed source, clock and instrument

Retain the complete time-zero source
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},\quad
c_j=\frac1{(2j)!}\int_0^\infty u^{2j}\Phi(u)\,du,\quad F(w)=\sum_{j\ge0}c_jw^j.
\]
For arbitrary fixed \(N\ge0\), \(m=N+1\), let \(S_Ne_j=e_{j-1}\), \(S_Ne_0=0\), and
\[
K_v=F(vS_N)/F(v),\quad G_N=K'_vK_v^{-1},\quad
R_N=-(G_N+G_N^\dagger),\quad H_N=\tfrac i2(G_N-G_N^\dagger).
\]
In this note \(K_v\) is finite unless explicitly marked infinite. The scalar \(F(v)\) is complete at every cutoff. Write \(b_1=c_1/c_0>0\), \(\gamma(v)=F'(v)/F(v)\). E01 supplies analyticity, invertibility, \(\|K_v^{-1}\|<13/12\), and
\[
R_N(v)\ge(2I-S_N-S_N^\dagger)/8000,\qquad 0\le v\le1/25.
\]
Use the E02 loss instrument with \(L_\mu=\sum_j(\sqrt{R_N})_{\mu j}a_j\), coherent Hamiltonian \(d\Gamma(H_N)\), and no-count generator \(d\Gamma(G_N)\).

Let \(f(0)=0\), \(f\) nondecreasing \(C^1\), with range in the local interval. Chain rule and the unique Hermitian/dissipative split give
\[
\widetilde G=f'G_N\circ f,\quad \widetilde H=f'H_N\circ f,\quad
\widetilde R=f'R_N\circ f,\quad \widetilde L_\mu=\sqrt{f'}L_\mu\circ f.
\tag{1}
\]
The full Fock Lindblad generator is \(f'(t)\mathcal L_N(f(t))\). At \(f'=0\), all these instantaneous generators/jumps vanish; differentiability of \(\sqrt{f'}\) is not required for the continuous generator. On any interval the no-count block is
\(\Gamma(K_{f(t_2)}K_{f(t_1)}^{-1})\).
For the channel-discarded \(k\)-count density,
\[
\widetilde{\mathcal I}_{k}(\mathbf t;t_2,t_1)
=\prod_{j=1}^k f'(t_j^{\rm event})\,
\mathcal I_k(f(t_1^{\rm event}),\ldots,f(t_k^{\rm event});f(t_2),f(t_1)),
\tag{2}
\]
where \(\mathbf t=(t_1^{\rm event},\ldots,t_k^{\rm event})\) is ordered inside the observation interval. Formula (2) is an equality of densities almost everywhere, with zero value when an event derivative vanishes. Monotone absolutely continuous substitution proves the integral identity even for flat intervals: flat activity values have zero probability for continuous event times, and there are no events on a lab-time flat interval. No inverse-clock differentiability is assumed.

For \(f(t)=at\), \(a>0\), generators/rates scale by \(a\), jumps by \(\sqrt a\), and \(t\le1/(25a)\). For \(f(t)=at^2\), the factors are \(2at,\sqrt{2at}\), and
\[
0\le t\le T_a:=1/\sqrt{25a}.
\tag{3}
\]
At a corresponding activity the exact endpoint and ordered minor do not change:
\[
\langle I|\Gamma(K_v)|J\rangle
=\frac{v^{\sum J-\sum I}}{F(v)^r}\det[c_{j_b-i_a}],\quad |I|=|J|=r,
\tag{4}
\]
with negative coefficient indices zero; at \(v=0\) use \(K_0=I\) directly. A clock change supplies no signed bound or efficiency gain.

## 2. Scope of the startup obstruction

For a unit one-particle input,
\[
1-\|K_{f(t)}\psi\|^2=f(t)\langle\psi,R_N(0)\psi\rangle+O(f(t)^2).
\tag{5}
\]
If a fixed bath starts in a product vacuum, \(P\) is that vacuum subspace, and its total Hamiltonian has norm bounded near zero, Duhamel gives \(\|(I-P)U(t)P\|=O(t)\); hence vacuum leakage is \(O(t^2)\). A positive \(f'(0)\) makes (5) linear and contradicts that realization class. Merely imposing \(f'(0)=0\) is insufficient: for strictly positive finite \(R_N(0)\), a necessary scale is \(f(t)=O(t^2)\); \(f=t^{3/2}\) fails it. The selected quadratic clock meets the scale and Section 4 proves the actual finite realization.

At any later \(t_0>0\), projecting the bath to vacuum again leaves a product-vacuum state. Its fresh leakage remains \(O((t-t_0)^2)\), whereas the prescribed intermediate map has leading loss
\(f'(t_0)(t-t_0)\langle\psi,R_N(f(t_0))\psi\rangle\).
For the quadratic clock this is strictly positive for every unit input. Quadratic startup therefore preserves the later repeatedly reset vacuum obstruction to reproducing the complete original instrument with this regular fixed bath.

## 3. Joint unitary, fermion order and endpoint block

Set \(C(t)=K_{at^2}\), \(D=(I-C^\dagger C)^{1/2}\), \(E=(I-CC^\dagger)^{1/2}\) and
\[
U=\begin{pmatrix}C&-E\\D&C^\dagger\end{pmatrix},\qquad
U^\dagger=\begin{pmatrix}C^\dagger&D\\-E&C\end{pmatrix}.
\tag{6}
\]
Polynomial approximation to square root in \((I-CC^\dagger)C=C(I-C^\dagger C)\) gives \(EC=CD\), with adjoint \(C^\dagger E=DC^\dagger\). Thus both products are
\[
U^\dagger U=\begin{pmatrix}C^\dagger C+D^2&-C^\dagger E+DC^\dagger\\-EC+CD&E^2+CC^\dagger\end{pmatrix}=I,
\]
\[
UU^\dagger=\begin{pmatrix}CC^\dagger+E^2&CD-EC\\DC^\dagger-C^\dagger E&D^2+C^\dagger C\end{pmatrix}=I.
\tag{7}
\]
At zero \(C=I,D=E=0\), so \(U(0)=I\).

[Robinson, arXiv:1803.09329v1](https://arxiv.org/html/1803.09329v1), Theorems 0, 1, 2, respectively establish Julia unitarity, the defect intertwiner, and Halmos unitarity for contractions. His Halmos block is \(\left(\begin{smallmatrix}C&E\\D&-C^\dagger\end{smallmatrix}\right)\); (6) multiplies it on the right by \(\operatorname{diag}(I,-I)\). These passages were rechecked on 3 November. Clock regularity and the Hamiltonian/Fock calculations here are local work, not imported from that paper. The canonical reference is already cataloged; [source record](../../references/03_MC08_E06_ROBINSON_RECHECK_20261103.md).

The total one-particle space is \(\mathbb C_S^m\oplus\mathbb C_E^m\), with ordered basis all system modes first, then all environment modes. Factorization
\[
\mathcal F_-(\mathbb C_S^m\oplus\mathbb C_E^m)
\simeq \mathcal F_-(\mathbb C_S^m)\otimes\mathcal F_-(\mathbb C_E^m)
\]
sends \(\xi\otimes\eta\) to \(\xi\wedge\eta\), system factors first. System creation is \(a_j^\dagger\otimes I\), environment creation is \(\Pi_S\otimes b_\mu^\dagger\). The total dimension is \(2^{2m}\); the bath alone has \(m\) modes. Define exactly \(\Gamma(U)=\bigoplus_{r=0}^{2m}\wedge^rU\), with vacuum phase \(+1\). It conserves total number and parity. For every initially occupied system orbital, \(U(e_j,0)=(Ce_j,De_j)\). Selecting only system factors from the wedge gives
\[
\langle\Omega_E|\Gamma(U(t))|\Omega_E\rangle=\Gamma(C(t))
\tag{8}
\]
on every system sector \(0\le r\le m\), including vacuum. All signs in (4) and its positive normalization are retained.

## 4. Regular total Hamiltonian on the mapped compact interval

Put \(A_N=2I-S_N-S_N^\dagger\). The finite Dirichlet eigenvalues are \(2-2\cos(k\pi/(m+1))\), \(1\le k\le m\). Hence
\[
R_0:=R_N(0)=b_1A_N>0,\qquad
\lambda_{\min}(R_0)=b_1[2-2\cos(\pi/(m+1))]>0.
\tag{9}
\]
Analyticity of the finite transfer gives
\[
C=I+at^2G_N(0)+O(t^4),\quad
I-C^\dagger C=at^2R_0+O(t^4),\quad I-CC^\dagger=at^2R_0+O(t^4).
\tag{10}
\]
For positive \(v\), direct differentiation gives
\[
I-K_v^\dagger K_v=\int_0^v K_s^\dagger R_N(s)K_s\,ds
\ge v\kappa_N(12/13)^2I>0,\quad
\kappa_N=\frac{2-2\cos(\pi/(m+1))}{8000}.
\tag{11}
\]
The other defect has the same eigenvalues, since \(C^\dagger C\) and \(CC^\dagger\) have the same singular-value squares.

Define the removable continuations
\[
Q_D(t)=\frac{I-C^\dagger C}{t^2},\quad Q_E(t)=\frac{I-CC^\dagger}{t^2},\qquad Q_D(0)=Q_E(0)=aR_0.
\]
They are even real-analytic matrix functions and, on the entire fixed-\(N\) compact interval, are positive definite with lower bound \(a\kappa_N(12/13)^2I\). Positive matrix square root is smooth on positive-definite matrices: its differential solves \(\sqrt Q X+X\sqrt Q=\delta Q\), whose eigenvalue sums are positive; repeated differentiation gives higher regularity. Consequently on \(t\ge0\)
\[
D(t)=t\sqrt{Q_D(t)}=\sqrt a\,t\sqrt{R_0}+O(t^3),\quad
E(t)=t\sqrt{Q_E(t)}=\sqrt a\,t\sqrt{R_0}+O(t^3).
\tag{12}
\]
The \(Q\) argument proves continuity of derivatives, which an undifferentiated remainder alone would not prove. The odd smooth extension of \(D,E\) through zero is only a regularity device; the positive defect square roots for negative time would instead contain \(|t|\).

Thus \(U\) is continuously differentiable (indeed smooth one-sided at the endpoints), and
\[
h_{\rm tot}(t)=iU'(t)U(t)^\dagger=h_{\rm tot}(t)^\dagger,
\qquad h_{\rm tot}(0)=i\sqrt a\begin{pmatrix}0&-\sqrt{R_0}\\\sqrt{R_0}&0\end{pmatrix}.
\tag{13}
\]
Hermiticity follows by differentiating \(UU^\dagger=I\); compactness gives a finite supremum norm. Equation \(iU'=h_{\rm tot}U\) has the initial value \(U(0)=I\). Differentiating each exterior power proves
\[
i\partial_t\Gamma(U)=d\Gamma(h_{\rm tot})\Gamma(U),\qquad
\|d\Gamma(h_{\rm tot})\|\le2m\|h_{\rm tot}\|.
\tag{14}
\]
This is a normal-ordered, bounded driven Hamiltonian on the entire finite total Fock space. The reduced coherent Hamiltonian \(\widetilde H_N(0)=0\) differs from the nonzero startup exchange (13).

The finite Dirichlet gap tends to zero with \(N\). The proof supplies no uniform cutoff estimate, and does not prove such estimates impossible. The bath is driven; number/parity conservation does not imply conservation of its time-dependent energy.

## 5. Partial trace, final conditioning and the unselected channel comparison

The exact finite endpoint channel and its Kraus blocks are
\[
\Phi_{N,t}(\rho)=\operatorname{Tr}_E[\Gamma(U)(\rho\otimes|\Omega_E\rangle\langle\Omega_E|)\Gamma(U)^\dagger]
=\sum_A M_A\rho M_A^\dagger,
\quad M_A=\langle A_E|\Gamma(U)|\Omega_E\rangle.
\tag{15}
\]
It is CPTP. The final bath-vacuum outcome has \(M_\varnothing=\Gamma(C)\), success \(p(\rho)=\operatorname{Tr}(\Gamma(C)\rho\Gamma(C)^\dagger)\), and normalized conditional state obtained by dividing by \(p\). For \(|J\rangle\), \(p_J=\det[(C^\dagger C)_{J,J}]\). Its phase is fixed by (8); partial tracing sums all outcomes and does not select this branch.

The unmeasured joint propagator is \(U_2U_1^\dagger\), with intermediate vacuum block on one particle
\[
B_{21}=C_2C_1^\dagger+E_2E_1.
\tag{16}
\]
It generally differs from the original no-count ratio \(C_2C_1^{-1}\). For \(C_j=\cos\theta_j\), \(0\le\theta_1\le\theta_2<\pi/2\), the two expressions are \(\cos(\theta_2-\theta_1)\) and \(\cos\theta_2/\cos\theta_1\). Their difference is \(\sin\theta_1\sin(\theta_2-\theta_1)/\cos\theta_1\), positive when \(0<\theta_1<\theta_2\). The first has quadratic fresh leakage and the second has linear loss when \(\theta'\tan\theta>0\). Final empty bath permits earlier excursions and returns; the original all-bin-vacuum record does not.

For a later selected endpoint-channel comparison, the exact algebra is already specified. For ordered sets \(I,J,A\), define
\[
M_A|I\rangle=\sum_{J:\,|J|+|A|=|I|}
\det\begin{bmatrix}C_{J,I}\\D_{A,I}\end{bmatrix}|J\rangle.
\tag{17}
\]
Rows are ordered system then bath. Equality with the original channel \(\mathcal T_N(f(t),0)\) would require
\[
\sum_A M_A|I\rangle\langle J|M_A^\dagger
=\mathcal T_N(f(t),0)(|I\rangle\langle J|)
\tag{18}
\]
on the selected operator algebra, equivalently the finite superoperator equation \(\dot\Phi_{N,t}=f'(t)\mathcal L_N(f(t))\Phi_{N,t}\), \(\Phi_{N,0}=\mathrm{Id}\), there. Physical system density operators commute with parity, so matrix units with \(|I|-|J|\) even span the physical algebra. Requiring (18) also for odd differences is a stronger mathematical extension. Section 6 checks that distinction explicitly. Equality of just \(M_\varnothing\) proves neither (18) nor equality of full count instruments. No general even-algebra endpoint comparison or CP-divisibility theorem for the fixed bath is executed here.

## 6. Exact symbolic checks: N=0 and N=1 only

These are hand symbolic calculations, not floating samples or an all-sector proof. All expressions below hold at \(v=at^2\) and retain the complete scalar \(F(v)\).

For \(N=0\), put \(d=c_0/F(v)\), \(q=\sqrt{1-d^2}\). The joint isometry fixes vacuum and maps the occupied mode to \(d|0\rangle\Omega_E+q\Omega_S|e_0\rangle\). The Kraus blocks are \(M_\varnothing=\operatorname{diag}(1,d)\), \(M_{e_0}=q|\Omega\rangle\langle0|\). Thus vacuum is fixed, occupied population maps to \(d^2|0\rangle\langle0|+(1-d^2)|\Omega\rangle\langle\Omega|\), and vacuum/occupied coherence scales by \(d\). In particular \(G_0=-\gamma\), \(R_0(v)=2\gamma\), and \(H_0=0\); this notation \(R_0(v)\) means the cutoff-zero matrix, distinct from the startup matrix of Section 4.

For \(N=1\), in the system basis \((\Omega,|0\rangle,|1\rangle,P=|0,1\rangle)\), put
\[
C=\begin{pmatrix}d&e\\0&d\end{pmatrix},\quad d=c_0/F(v),\quad e=vc_1/F(v),\quad
D=\begin{pmatrix}x&y\\y&z\end{pmatrix}.
\]
Then \(D^2=A=I-C^TC\) gives
\[
x^2+y^2=1-d^2,\quad y(x+z)=-de,\quad y^2+z^2=1-d^2-e^2.
\tag{19}
\]
Expansion of the two initial orbitals in system-first wedge order gives the complete Kraus table (unlisted actions vanish):

| Bath outcome | Vacuum | \(\lvert0\rangle\) | \(\lvert1\rangle\) | \(P\) |
| --- | --- | --- | --- | --- |
| Empty | \(\Omega\) | \(d\lvert0\rangle\) | \(e\lvert0\rangle+d\lvert1\rangle\) | \(d^2P\) |
| \(e_0\) | 0 | \(x\Omega\) | \(y\Omega\) | \((dy-ex)\lvert0\rangle-dx\lvert1\rangle\) |
| \(e_1\) | 0 | \(y\Omega\) | \(z\Omega\) | \((dz-ey)\lvert0\rangle-dy\lvert1\rangle\) |
| \(e_0,e_1\) | 0 | 0 | 0 | \((xz-y^2)\Omega\) |

In particular the occupied-pair vacuum amplitude is \(\det C=d^2\). With
\[
Q=\begin{pmatrix}dy-ex&dz-ey\\-dx&-dy\end{pmatrix},\quad
B=QQ^T=CC^T-d^4I,\quad \det A=(xz-y^2)^2=1-2d^2-e^2+d^4,
\]
the pair population is \(d^4|P\rangle\langle P|+\sum B_{kl}|k\rangle\langle l|+\det A|\Omega\rangle\langle\Omega|\).
The exact normalization checks are \(d^4+\operatorname{tr}B+\det A=1\) and \(C^TC+D^2=I\); different number sectors give no other cross terms in \(\sum M_A^\dagger M_A\).

Writing \(c_i=Ce_i\), relevant coherences are
\[
\Phi(|i\rangle\langle j|)=|c_i\rangle\langle c_j|+A_{ji}|\Omega\rangle\langle\Omega|,
\quad \Phi(|\Omega\rangle\langle i|)=|\Omega\rangle\langle c_i|,
\quad \Phi(|\Omega\rangle\langle P|)=d^2|\Omega\rangle\langle P|.
\tag{20}
\]
For example \(\Phi(|0\rangle\langle1|)=de|0\rangle\langle0|+d^2|0\rangle\langle1|-de|\Omega\rangle\langle\Omega|\). Vacuum/pair coherence is even and is retained. For the odd operators,
\[
\Phi(|i\rangle\langle P|)=d^2|c_i\rangle\langle P|+|\Omega\rangle\langle w_i|,
\quad w_0=(-e,-d(1-d^2)),\quad w_1=(d(1-d^2),d^2e).
\tag{21}
\]
These formulas and adjoints determine every matrix unit. They expose a concrete limit of inheritance on the whole trace class. Since \(d=1-b_1v+O(v^2)\), \(e=b_1v+O(v^2)\), (21) gives, for \(O=|0\rangle\langle P|\),
\[
\Phi_v(O)=O+v[-3b_1O-b_1|\Omega\rangle\langle0|-2b_1|\Omega\rangle\langle1|]+O(v^2).
\]
In E02's ordinary odd-jump extension, \(a_0P=|1\rangle\), \(a_1P=-|0\rangle\), and \(R_1(0)=b_1\left(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\right)\) instead give
\[
\mathcal L_N(0)O=-3b_1O+b_1|\Omega\rangle\langle0|+2b_1|\Omega\rangle\langle1|.
\tag{22}
\]
Replace \(v\) by \(at^2\) for the selected clock. This exact authorized two-mode check excludes equality of these particular extensions on arbitrary odd operators. It decides no general even-algebra endpoint equality and is no correction to Note03, which asserts no such equality. E02 uses environment-first ordering, whereas this note fixes system-first ordering. Their graded swap multiplies system/bath particle sectors by (−1)^(rs). Physical even comparisons are insensitive to this ordering transport, while arbitrary odd extensions require it to be specified. Changing the grading convention is not undertaken here.

## 7. Signed readout, controls and energy distinctions

Coherently control the explicit joint unitary with a neutral flag, identity on arm 0 and \(\Gamma(U)\) on arm 1. Prepare \((|0\rangle|I\rangle+|1\rangle|J\rangle)/\sqrt2\), with equal system particle number. Final bath-vacuum selection gives the unnormalized flag matrix
\[
\frac12\begin{pmatrix}1&A^*\\A&p_J\end{pmatrix},\qquad
A=\langle I|\Gamma(C)|J\rangle,\quad q_0=(1+p_J)/2.
\]
Thus \(P(0,\pm_X)=(1+p_J\pm2\operatorname{Re}A)/4\), and \(\operatorname{Re}A=q_0E[X\mid0]\). With the usual \(Y\), \(\operatorname{Im}A=q_0E[Y\mid0]\) with positive sign. Signal normalization uses \(p_J\); flag normalization uses \(q_0\). Neither may be discarded. Inherited inverse bounds give \(p_J\ge(12/13)^{2r}\), not a uniform floor in \(r\). At vacuum \(A=p_J=q_0=1\); at \(t=0\), \(A=\delta_{IJ}\), \(p_J=q_0=1\). The two arms have the same number/parity. Coherently controlled dynamics and phase calibration are resources beyond arbitrary channel access.

For Gaussian \(F=c_0e^{\lambda w}\), \(\lambda>0\), \(G=\lambda(S-I)\), \(R=\lambda(2I-S-S^\dagger)\). The finite completion and quadratic regularity apply, retaining its known nonnegative minors. For the existing polynomial \(F_*=1+w+2w^2\), the E01 exact symbol is nonnegative on \(0\le v<1/\sqrt2\); the selected interval is inside it, and every finite startup gap is positive. The inherited negative witness remains
\[
\langle0,1|\Gamma(K_{*,v})|1,2\rangle=-v^2/F_*(v)^2<0\quad(v>0).
\tag{23}
\]
This is the previously proved witness, not a fresh cutoff-two calculation. Endpoint equality (8) and the unchanged positive normalization retain its sign. The polynomial fails canonical theta reconstruction, not the generic realization premises. Euler-factor/weighted-square changes fail canonical coefficients/weights and may fail the fixed endpoint; reflected or positive-primitive controls need not supply the arithmetic theta source. No new sign or admissibility calculation is assigned to those families. No control is claimed to be eliminated merely by generic bath regularity.

The three energies have different spaces and meanings: source \(E_n=\pi n^2\) enters the complete heat trace at \(\beta=e^{4u}\) with insertion \(P_0(\beta E)=2(\beta E)^2-3\beta E\); reduced \(\widetilde H_N=2atH_N(at^2)\) is the coherent part of the prescribed coefficient transfer; total \(h_{\rm tot}\) generates the driven joint unitary. No identification of coefficient sites with source energy eigenmodes, autonomous bath, thermal balance, or energy conservation is proved.

## 8. Finite/infinite boundary and continuation

The half-infinite endpoint contraction has the same bounded algebraic unitary completion. This fact alone supplies no differentiable joint path, bounded infinite one-particle generator, or full-Fock Hamiltonian/domain theorem. The finite regularity proof uses the shrinking gap (9). Moreover \(\sqrt{P_NRP_N}\) generally differs from \(P_N\sqrt R P_N\); at N=0,1 the diagonal of \(\sqrt{R_1}\) is \((\sqrt{2\gamma-b_1}+\sqrt{2\gamma+b_1})/2<\sqrt{2\gamma}\). Likewise \(D_N^2=P_N(I-K^\dagger K)P_N\) does not make its square root a restriction. For \(E_N^2\), even compression of the squared defect has extra omitted-column terms. No compatible joint bath restrictions follow. This does not prove reduced endpoint-channel incompatibility; that needs the separately selected comparison (18).

The original reparameterized E02 instrument retains its proved trace-class extension and particle-cap differentiability domain; the fixed-bath construction does not inherit them automatically. On an infinite full Fock space, sector bounds growing with particle number require domains even when a one-particle generator is bounded. Neither the infinite generator nor a joint collision/cutoff limit was attempted.

**Next: [B] MC08-B04 — Astra.** Consume the [assessment and inheritance table](../reviews/01_MC08_E06_QUADRATIC_CLOCK_ASSESSMENT_20261103.md), select the observation algebra/full model/energy meaning, and issue E07 only after fixing the remaining mathematical route. [Handoff08](../../research-progress/handoffs/08_MC08_E06_RETURN_AND_B04_MODEL_CONTINUATION_20261103.md) gives continuation and model-change guidance. E04 remains a separate unexecuted task. No manuscript, architecture, source or frozen request was changed.
