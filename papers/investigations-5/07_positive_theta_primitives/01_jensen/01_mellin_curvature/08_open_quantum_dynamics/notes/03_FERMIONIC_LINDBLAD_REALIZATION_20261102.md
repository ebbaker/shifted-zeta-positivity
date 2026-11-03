# MC08-E02 r2: fermionic loss instrument, collision limit and signed readout

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual authoring model **gpt-6.1-sol (Codex), reasoning effort ultra**, verified in chat `01a19d66-56e2-7ff2-a549-03561c41f801`, turn `01a19de8-de85-7393-b47c-1c650ee88588`. Two read-only same-model author-support subtasks checked the collision estimates and finite/readout algebra. They are not the separate E03 reviewer.

**E02 disposition: positive completion of contract r2 at its specified scope; proved in-note.** Parts A--D below establish one channel-discarded loss-count instrument with unchanged no-jump operator \(\Gamma(K_bK_a^{-1})\), a Hermitian fresh-vacuum collision approximation at each fixed mode cutoff with an explicit record-valued error, a same-number signed readout, and an exactly compatible trace-class extension to vacuum Fock space. The positive interval remains \(0\le a\le b\le1/25\). No new theta minor sign, neighboring-index comparison or real-Mellin bound follows. The negative polynomial control passes the dynamical premises and is retained in the same instrument.

This author return is frozen for **MC08-E03**, a separate internal assessment requested by the author. E03's disposition belongs in the [sole live register](../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md) and its assessment file; it is not supplied by this author declaration.

## 1. Fixed inputs, conventions and elementary norm lemma

The [r2 request](../research-progress/handoffs/02_MC08_E02_CONSTRUCTION_CONTRACT_R2_20261102.md) is the governing contract. All its prerequisite hashes were verified before use:

| Input | SHA256 |
| --- | --- |
| [E01 return](01_NO_JUMP_ADMISSIBILITY_AUDIT_20261102.md) | `21929f0b5050f699b856aaa899dd1631564aecb2a700a89fa994cbdeeb1fabf5` |
| [E01 exact record](../numerics/MC08_E01_EXACT_BOUNDS_20261102.json) | `fba2ae5435515676f801c10b7bfe7dd62e46850d2d066fd5571048f69152fb2f` |
| [E01 limited check](../reviews/01_MC08_E01_BOUNDED_CHECK_20261102.md) | `94f920dd1bbee9b93668348c6770f54534f1c0851b9b707db92380dfad9a4161` |
| [B01 decision](02_OPEN_SYSTEM_ARCHITECTURE_DECISION_20261102.md) | `e20fa974e053b609c49c477a6f1e587b27d5e1969fe3960468eb23d0e47b85c2` |
| E02 request r2 | `a95b693ac7a34a99d5fc45316672148f75ef7bb139ebcd7ce3fb39ec8820ae41` |

Retain the complete canonical time-zero theta coefficients \(c_n=(2n)!^{-1}\int_0^\infty u^{2n}\Phi(u)\,du\), \(F(w)=\sum c_nw^n\), and the backward shift. On \(\mathfrak h_N=\operatorname{span}\{e_0,\ldots,e_N\}\), \(m=N+1\), put
\[
K_{v,N}=F(vS_N)/F(v),\quad G_N=G|_{\mathfrak h_N},\quad
R_N=-(G_N+G_N^\dagger),\quad H_N=\tfrac i2(G_N-G_N^\dagger),\quad B_N=\sqrt{R_N}.
\]
Here \(H_N\) denotes the Hermitian one-particle matrix, not the mode space. The scalar \(F(v)\) and \(\gamma=F'/F\) are **never truncated**. Ordered states are \(a_{j_1}^\dagger\cdots a_{j_r}^\dagger\Omega\), \(j_1<\cdots<j_r\). Set
\[
L_{\mu,N}=\sum_j(B_N)_{\mu j}a_j,\quad H_{F,N}=d\Gamma(H_N),\quad D_N=d\Gamma(G_N).
\]
Normal ordering fixes vacuum energy zero and no-jump vacuum phase \(+1\).

E01 supplies norm-continuity, \(R\ge0\), exact contractions \(V(b,a)=K_bK_a^{-1}\), \(\|K_v^{-1}\|<13/12\), and, with
\[
A_*=[96(1-1/100)^2]^{-1},\qquad
\|G\|,\|H\|\le2A_*,\quad\|R\|\le4A_*.
\tag{1}
\]
Its theta source/tail proof is reused, not recomputed. Square roots are norm-continuous by uniform polynomial approximation on a common bounded spectral interval; no positive spectral gap is assumed.

We use trace norm for all trace-class operators, including off-diagonal matrix units. A CP trace-preserving map, including a record-valued instrument viewed as a map into a direct sum or direct integral of trace classes, has induced trace norm one. To see the bound on arbitrary operators, its dual is unital CP: the CP Schwarz inequality gives \(\|T^*X\|\le\|X\|\), and trace duality gives contraction. The same argument applies to a trace-nonincreasing CP map with subunital dual. For an instrument density this can also be read directly from its Stinespring map into the classical-record direct integral. These facts justify the norm bounds and telescoping below without restricting to positive inputs.

The [result index](../../../../../../../result-summaries/README.md), specifically [theta physical assessments](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and [avoid index](../../../../../../../avoid/README.md), specifically [generic re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [control discipline](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), fix the interpretation. This is a physical-realization and convergence result. The all-sector sign formulation remains the inherited RH-equivalent statement, not an estimate acquired by this construction.

## A. Finite-mode dynamics and the complete count instrument

The CAR and \(B_N^\dagger B_N=R_N\) give, with the indices kept explicit,
\[
\sum_\mu L_{\mu,N}^\dagger L_{\mu,N}
=\sum_{j,k}(R_N)_{jk}a_j^\dagger a_k=d\Gamma(R_N),
\quad -iH_{F,N}-\tfrac12d\Gamma(R_N)=D_N,
\tag{2}
\]
\[
\mathcal J_N(v)\rho=\sum_\mu L_{\mu,N}\rho L_{\mu,N}^\dagger
=\sum_{j,k}(R_N)_{kj}a_j\rho a_k^\dagger,
\quad\mathcal L_N(v)\rho=D_N\rho+\rho D_N^\dagger+\mathcal J_N(v)\rho.
\tag{3}
\]
These are bounded norm-continuous maps on the finite Fock trace class. On each \(r\)-particle sector, differentiation of an exterior power gives
\[
\partial_b\bigwedge^r V_N(b,a)=d\Gamma_r(G_N(b))\bigwedge^rV_N(b,a).
\]
Initial value and uniqueness therefore identify the no-jump operator on every sector, including the vacuum:
\[
M_{0,N}(b,a)=\Gamma(V_N(b,a)),\qquad
\mathcal V_N(b,a)\rho=M_{0,N}(b,a)\rho M_{0,N}(b,a)^\dagger.
\tag{4}
\]
It is a contraction since \(D_N+D_N^\dagger=-d\Gamma(R_N)\le0\).

For \(a<t_1<\cdots<t_k<b\), define the count-density CP map
\[
\mathcal I_{N;k}(\mathbf t;b,a)
=\mathcal V_N(b,t_k)\mathcal J_N(t_k)\mathcal V_N(t_k,t_{k-1})
\cdots\mathcal J_N(t_1)\mathcal V_N(t_1,a).
\tag{5}
\]
The zero-count term is \(\mathcal V_N(b,a)\). Formula (5) sums detector labels **incoherently**, retaining their common count time. Integrating over measurable sets of ordered times supplies the entire count instrument. Each Kraus factor at a jump lowers system particle number by one. Thus (5) vanishes for \(k>r\) on operators supported in at most \(r\) particles, and for \(k>m\) on the full finite-mode trace class. This also covers coherences between different particle sectors, not just populations.

Sum (5) and its time integrals. Variation of constants gives the unique solution of \(\dot\rho=\mathcal L_N\rho\). Every term is CP. Cyclicity and (2) give \(\operatorname{Tr}\mathcal L_N\rho=0\), so the sum is trace preserving. Splitting ordered trajectories at an intermediate time gives composition of the channel and concatenation of its count instrument. Hence the evolution is CPTP and CP-divisible on every intermediate interval; it is generally time dependent, with no homogeneous-semigroup claim. The conditional no-count state is (4) divided by its trace, not the whole channel.

Our convention is \(L\rho L^\dagger-\{L^\dagger L,\rho\}/2\), matching [Castin--Dalibard--Mølmer, equations (2), (4)--(8), Section 2](https://arxiv.org/html/0805.4002v1). For comparison, [Prosen, Section 2 equation (1)](https://arxiv.org/html/0801.1257v3) uses \(2L_P\rho L_P^\dagger-\{L_P^\dagger L_P,\rho\}\); our jump is \(\sqrt2L_P\). Those passages were re-inspected. No third-quantization, time-dependent infinite-domain or reservoir theorem is imported from them; the constructions here are proved directly.

## B. Hermitian collisions and a matching-bin instrument error

Use exactly the frozen environment-first convention. Each bin has \(m\) fresh vacuum fermion modes, parity \(\Pi_E\), and
\[
W_N=\sum_\mu(b_\mu^\dagger\Pi_E\otimes L_{\mu,N}
+\Pi_Eb_\mu\otimes L_{\mu,N}^\dagger),\quad
U_{N,h}(v)=e^{-i(hI_E\otimes H_{F,N}(v)+\sqrt h W_N(v))}.
\tag{6}
\]
\(W_N\) is Hermitian and conserves total fermion number and parity. The leading emission has the stipulated sign, since
\[
W_N(\Omega_E\otimes f)=\sum_\mu|\mu\rangle\otimes L_{\mu,N}f,
\quad \langle\Omega_E|W_N^2|\Omega_E\rangle=d\Gamma(R_N).
\tag{7}
\]
In particular \(b_\mu^\dagger\Pi_E\Omega_E=|\mu\rangle\), and \(\Pi_Eb_\mu|\nu\rangle=\delta_{\mu\nu}\Omega_E\). The parity operators must not be dropped before this sign check. Chronologically ordering retained bins before the system gives the same local exchange: parity strings from earlier bins cancel in the even exchange, and future bins are still vacuum.

Here are explicit conservative constants, uniform in \(v\) at each fixed \(N\). Write \(A=A_*\), and set
\[
d=H_0=2mA,\quad j=4mA,\quad \ell=2\sqrt A,\quad w=4m\sqrt A,
\]
which bound respectively \(\|D_N\|,\|H_{F,N}\|,\|d\Gamma(R_N)\|=\|\mathcal J_N\|_{1\to1},\max_\mu\|L_{\mu,N}\|,\|W_N\|\). For the last bound use \(\|a(f)\|=\|f\|\), each row of \(B_N\) has norm at most \(\sqrt{\|R_N\|}\), and \(\|W_N\|\le2\sum_\mu\|L_{\mu,N}\|\). Define
\[
c=w+H_0,\quad E=wH_0+\tfrac12H_0^2+e^c c^3/6,\quad q=2^m-m-1.
\tag{8}
\]
For \(0<h\le1\), expansion of the exponential through degree two gives
\[
\|U-[I-i\sqrt h W-ihH-hW^2/2]\|\le Eh^{3/2}.
\tag{9}
\]
Indeed \(\|\sqrt hW+hH\|\le c\sqrt h\); its third-order remainder is at most \(e^cc^3h^{3/2}/6\), and the omitted mixed and \(H^2\) terms cost at most \((wH_0+H_0^2/2)h^{3/2}\).

For outgoing-bin occupation state \(\sigma\), let \(C_\sigma=\langle\sigma|U|\Omega_E\rangle\). Equations (7)--(9) imply
\[
\|C_0-(I+hD_N)\|\le Eh^{3/2},\quad
\|C_\mu+i\sqrt h L_{\mu,N}\|\le Eh^{3/2},\quad
\|C_\sigma\|\le h(w^2/2+E)\ (|\sigma|\ge2).
\tag{10}
\]
The one-emission estimate is stronger than requested: \(H\) and \(W^2\) have no vacuum-to-one-emission block. Measuring total occupation gives CP maps \(\mathcal C_{h,n}\rho=\sum_{|\sigma|=n}C_\sigma\rho C_\sigma^\dagger\). The sum is trace preserving. Multiple emissions have no first-order probability or map-norm contribution, by the last bound in (10).

For a local comparison only, introduce the CP auxiliary maps
\[
\mathcal E_{h,0}\rho=(I+hD_N)\rho(I+hD_N)^\dagger,\quad
\mathcal E_{h,1}\rho=h\mathcal J_N\rho,\quad\mathcal E_{h,n}=0\ (n\ge2).
\]
They need not sum to a trace-preserving map and are never used as telescoping propagators. Using
\(\|A\rho A^\dagger-B\rho B^\dagger\|_1\le\|A-B\|(\|A\|+\|B\|)\|\rho\|_1\), (10) gives
\[
\|\mathcal C_h-\mathcal E_h\|_{1\to\ell^1(\mathfrak T)}\le C_c h^{3/2},\quad
C_c=E(2+d)+mE(2\ell+E)+q(w^2/2+E)^2.
\tag{11}
\]
The vacuum block uses \(\|C_0\|\le1\); each single-emission error is at most \(E(2\ell+E)h^2\); the \(q\) remaining Kraus maps cost at most \(q(w^2/2+E)^2h^2\). Replacing \(h^2\) by \(h^{3/2}\) yields (11).

Freeze the Lindblad coefficients at the bin's left endpoint. Its no-count operator is \(e^{hD_N}\). This and \(C_0\) are contractions. Its one-count map is \(\int_0^h\mathcal V(h-t)\mathcal J_N\mathcal V(t)dt\); higher-count maps are the ordered integrals. Dissipativity gives \(\|e^{tD_N}-I\|\le dt\) and \(\|\mathcal V(t)-I\|\le2dt\). Consequently its count instrument \(\mathcal I_h^{\rm fr}\) satisfies
\[
\|\mathcal I_h^{\rm fr}-\mathcal E_h\|\le C_L h^2,\quad
C_L=(2+d)d^2e^d/2+2dj+j^2e^j/2.
\tag{12}
\]
The terms pay respectively the vacuum Taylor error, the one-count integral versus \(h\mathcal J_N\), and \(\sum_{k\ge2}(jh)^k/k!\). In particular summing outcomes gives the first-order reduced map \(I+h\mathcal L_N+o_N(h)\).

To pay time dependence, define
\[
\omega_N(\delta)=\sup_{|s-t|\le\delta}
\{2\|D_N(s)-D_N(t)\|+\|\mathcal J_N(s)-\mathcal J_N(t)\|_{1\to1}\}.
\tag{13}
\]
It tends to zero, with \(\omega_N\le m(2\omega_G+\omega_R)\). The jump-map bound, including its linear dependence on \(R\), is proved in D below. Thus no spectral-gap estimate for the square root is needed here. To compare exact and frozen **count** instruments within a bin, append a count register \(n\in\mathbb N_0\). On its diagonal trace-class direct sum the bounded generator is
\[
(\widehat{\mathcal L}(t)\boldsymbol\rho)_n
=D_N(t)\rho_n+\rho_nD_N(t)^\dagger+\mathcal J_N(t)\rho_{n-1},\qquad\rho_{-1}=0.
\]
It is a CPTP evolution: equivalently use forward count-shift tensored with each \(L_\mu\), whose isometry preserves the same summed loss operator. Duhamel and contractivity bound exact versus frozen by \(h\omega_N(\delta)\). The infinite register avoids an artificial loss at its upper boundary; inputs have at most \(m\) actual counts.

For any partition \(\pi\) of \([a,b]\), mesh \(\delta\le1\), compare the collision record \(\mathbf n\) and the exact instrument integrated over exactly \(n_l\) jumps in each **same bin**. Extend successive record maps blockwise to preserve past records. They are CPTP contractions, so telescoping (11)--(13), with \(T=b-a\), gives the required uniform bound on arbitrary trace-class inputs:
\[
\boxed{\sup_{\|\rho\|_1\le1}\sum_{\mathbf n}
\|\mathcal I^\pi_{{\rm coll},\mathbf n}\rho-
\mathcal I^\pi_{{\rm Lind},\mathbf n}\rho\|_1
\le T[(C_c+C_L)\sqrt\delta+\omega_N(\delta)]\longrightarrow0.}
\tag{14}
\]
Thus contract r2's constants can be taken as \(C_N=(C_c+C_L)/25\), \(C'_N=1/25\). They may grow with \(N\); no uniform microscopic cutoff bound is claimed.

The no-count **amplitude and phase** need a separate statement, since channel convergence alone cannot fix a Kraus phase. Put \(\omega_D(\delta)=\sup_{|s-t|\le\delta}\|D_N(s)-D_N(t)\|\). A local amplitude comparison and telescoping the actual contraction blocks give
\[
\left\|\prod_l C_{0,l}-\Gamma(V_N(b,a))\right\|
\le T[(E+d^2e^d/2)\sqrt\delta+\omega_D(\delta)]\longrightarrow0.
\tag{15}
\]
Time ordering is chronological from right to left. This keeps the fixed vacuum phase.

For event-time tests on a fixed \(k\le m\) sector, assign each bin's counts to its representative, repeated in sorted order. On the compact closed ordered simplex, a bounded continuous \(f\) has a modulus \(\omega_f(\delta)\to0\). The error of its weighted output map is at most
\[
\|f\|_\infty T[(C_c+C_L)\sqrt\delta+\omega_N(\delta)]+\omega_f(\delta).
\tag{16}
\]
This proves weak event-time convergence; coincident grid representatives are allowed in the approximants. If tests are instead defined only on the open strict simplex, choose distinct representatives inside each bin. Bounded continuous tests there follow by first restricting to a compact set separated from the boundaries/diagonals: its omitted exact-instrument norm is at most \(j^k\) times the omitted volume, tending to zero; the matching-bin bound controls the collision omission. Uniform continuity on the remaining compact set then gives (16) with that tail allowance. There is no total-variation assertion between atomic grid timestamps and an exact continuous timestamp law.

For the controlled flag in C replace \(H_{F,N},L_\mu,D_N\) by \(Q_1\otimes H_{F,N},Q_1\otimes L_\mu,Q_1\otimes D_N\). Their norms and the constants above do not increase. The \(Q_0\) arm has identity collision dynamics and leaves every bin vacuum, so (9)--(16) apply directly to the controlled instrument, including coherences.

The physical bin Hamiltonian over duration \(h\) is \(I\otimes H_{F,N}+h^{-1/2}W_N\). It uses \(m\) new vacuum modes per bin and unbounded temporal bath resources as \(\delta\to0\). This is the prescribed ideal collision limit at fixed \(N\), not an exact finite-\(h\) identity, a regular bounded closed-reservoir realization, hardware feasibility or a joint collision/mode limit. Under B01's initial-product/fixed-vacuum and locally bounded total-Hamiltonian hypotheses, probability outside vacuum is \(O(v^2)\), while the target has nonzero linear loss. The selected singular stream does not contradict that scoped obstruction.

## C. Signed readout, both success factors and parity

For increasing \(I,J\subset\{0,\ldots,N\}\) of the same length \(r\), prepare
\[
\Psi_{\rm in}=(|0\rangle|I\rangle+|1\rangle|J\rangle)/\sqrt2
\]
with a neutral qubit and calibrated phase. Control \(H_{F,N}\) and **every** \(L_{\mu,N}\) by \(Q_1\). Then \(\sum\widetilde L_\mu^\dagger\widetilde L_\mu=Q_1\otimes d\Gamma(R_N)\), and the no-count generator is \(Q_1\otimes D_N\). From zero its exact block is
\[
\widetilde M_0=Q_0\otimes I+Q_1\otimes\Gamma(K_{v,N}).
\tag{17}
\]
Write \(T=\Gamma(K_{v,N})\), \(A=\langle I|T|J\rangle\), and
\[
p_J=\|T|J\rangle\|^2
=\det[(K_{v,N}^\dagger K_{v,N})_{J,J}],\quad
q_0=(1+p_J)/2.
\tag{18}
\]
The determinant is the squared norm of the wedge of the selected columns. The unnormalized flag density matrix after no count is exactly
\[
\tfrac12\begin{pmatrix}1&A^*\\ A&p_J\end{pmatrix}.
\]
Thus
\[
P(0,\pm_X)=\frac{1+p_J\pm2\operatorname{Re}A}{4},\quad
\operatorname{Re}A=q_0 E[X\mid0]=P(0,+_X)-P(0,-_X).
\tag{19}
\]
For \(Y=\left(\begin{smallmatrix}0&-i\\i&0\end{smallmatrix}\right)\), \(|+_Y\rangle=(|0\rangle+i|1\rangle)/\sqrt2\), the sign is positive:
\(\operatorname{Im}A=q_0E[Y\mid0]\), with \(P(0,\pm_Y)=(1+p_J\pm2\operatorname{Im}A)/4\). The theta amplitude is real in the fixed convention. For \(v>0\) it remains
\[
A_v(I,J)=\frac{v^{\sum J-\sum I}}{F(v)^r}\det[c_{j_b-i_a}],
\tag{20}
\]
with the original positive prefactor and no permutation reordering of the measurement basis. Signal postselection normalizes by \(p_J\), whereas the flag experiment normalizes by \(q_0\); these are different probabilities. The inverse bound from E01 gives
\[
\| (\bigwedge^rK_{v,N})^{-1}\|\le(13/12)^r,\qquad
p_J\ge(12/13)^{2r}.
\tag{21}
\]
There is no positive signal-success floor uniform in \(r\) and no efficient-estimation claim. At \(r=0\), \(A=p_J=q_0=1\). At \(v=0\), use \(T=I\) directly: \(p_J=q_0=1\), \(A=\delta_{I,J}\).

Both arms have the same fermion number and hence the same parity, including odd \(r\). Number-preserving controlled mode operations prepare them, with any known wedge permutation sign compensated in the flag phase. The no-count reservoir is the **same vacuum** on both arms and does not mark the arm; (15) proves this statement with its calibrated phase in the collision limit. Loss changes system number/parity; the even exchange conserves total number/parity. These controlled couplings are extra physical resources. Access to an arbitrary CPTP channel alone does not determine its coherently controlled Kraus phase. A probability \(|A|^2\) is not the required signed observation.

## D. Exact cutoff compatibility and the vacuum-Fock extension

For \(M\ge N\), \(G_M\) leaves \(\mathfrak h_N\) invariant and restricts to \(G_N\). Its second quantization similarly leaves \(\mathcal F(\mathfrak h_N)\) invariant. If \(\rho\) is supported on this subspace, then \(a_j\rho a_k^\dagger=0\) when either index exceeds \(N\), and the retained block of \(R_M\) is \(R_N\). Equations (3)--(5), initial values and bounded uniqueness give **exact restriction** of no-jump maps, the channel-discarded count instrument, and full propagators. This works on off-diagonal operators as well as populations. It uses cancellation in \(D=d\Gamma(G)\); \(H\) alone need not preserve the cutoff. Individual detector-label jumps, \(\sqrt{R_N}\), and finite collision unitaries are not identified across cutoffs.

Here is a uniform particle-cap construction making both continuity and the unbounded-domain limitation precise. Let \(Q_r\) project onto at most \(r\) particles in \(\mathcal F_-(\ell^2)\), and let \(\mathfrak T_r=Q_r\mathfrak TQ_r\). On this space \(D_r=d\Gamma(G)|_{\le r}\) is bounded by \(r\|G\|\). The annihilation row
\[
\mathfrak a f=\sum_{j\ge0}e_j\otimes a_j f,
\qquad\|\mathfrak a f\|^2=\langle f,\mathcal N f\rangle\le r\|f\|^2
\]
is bounded. Define
\[
\mathcal J_R\rho=\operatorname{Tr}_{\ell^2}
[(\sqrt R\otimes I)\mathfrak a\rho\mathfrak a^\dagger(\sqrt R\otimes I)].
\tag{22}
\]
It is CP, maps into the \((r-1)\)-particle cap, agrees with the finite-mode jump map, and obeys \(\|\mathcal J_R\|\le r\|R\|\). Its dual is \(\mathcal J_R^*X=\mathfrak a^\dagger(R\otimes X)\mathfrak a\), so
\[
\|\mathcal J_R-\mathcal J_{R'}\|_{1\to1}\le r\|R-R'\|.
\tag{23}
\]
This proves the modulus used in (13) and norm-continuity without a gap for \(\sqrt R\). The trace identity \(\operatorname{Tr}\mathcal J_R\rho=\operatorname{Tr}(d\Gamma_r(R)\rho)\) follows from the same row. Consequently the norm-continuous particle-cap generator satisfies the requested bound
\[
\boxed{\|\mathcal L(v)\|_{\mathfrak T_r\to\mathfrak T_r}
\le2r\|G(v)\|+r\|R(v)\|\le8rA_*.}
\tag{24}
\]
It is defined on all \(\mathfrak T_r\); the associated bounded ODE and jump series agree with the finite-mode maps on their dense union. Equation (23) and \(\|d\Gamma_r(G-G')\|\le r\|G-G'\|\) prove its norm-continuity. There are no domain ambiguities on a cap. The cap is invariant under all trajectories, and its jump series stops after \(r\) jumps.

Now let \(\Pi_N\) be the Fock projection onto \(\mathcal F(\mathfrak h_N)\). These increase strongly to identity. Their trace classes have dense union: \(\Pi_N\rho\Pi_N\to\rho\) in trace norm, by finite-rank approximation. Exact compatibility and contractivity therefore extend the finite-mode maps uniquely to all vacuum-Fock trace class. Positivity at every finite matrix amplification is preserved by trace-norm limits, so the extension is CP; trace continuity gives trace preservation. Composition passes from the dense union to its completion. For a fixed finite-mode input the time dependence is continuous; approximation by such inputs and contraction prove trace-norm continuity in \((b,a)\) for every trace-class input. This proves a two-parameter CPTP evolution directly, without using a formal unbounded Lindblad formula as a theorem.

The complete instrument extends as well. For fixed \([a,b]\), take the disjoint union of the ordered time simplexes for \(k=0,1,\ldots\), with Lebesgue measure for \(k\ge1\) and the zero-count atom. Finite-mode instruments (5) are consistent contractions into the Banach direct integral of trace classes, whose norm is the integrated sum of trace norms. Complete this consistent action by the same density argument. It remains CP and integrates to the extended channel; instrument composition and count statistics agree by continuity. On a particle cap its densities are precisely (5) with (22), and there are at most \(r\) counts. This construction covers arbitrary trace-class inputs without asserting a bounded full-Fock generator or infinite expected particle number control.

For every \(\rho\), natural embedding gives the statewise, uniform-in-time estimate
\[
\boxed{\|\mathcal T(b,a)\rho-
\mathcal T_N(b,a)(\Pi_N\rho\Pi_N)\|_1
\le\|\rho-\Pi_N\rho\Pi_N\|_1\longrightarrow0.}
\tag{25}
\]
The compressed input is unnormalized. Likewise \(\mathcal T^{\le r}\) on \(\mathfrak T_r\) obeys
\(\|\mathcal T\rho-\mathcal T^{\le r}(Q_r\rho Q_r)\|_1\le\|\rho-Q_r\rho Q_r\|_1\to0\).
The same estimates hold with the record-valued norm for the instruments. They give no rate without an input tail bound and no operator-norm convergence uniformly over all states.

The union \(\bigcup_r\mathfrak T_r\) is a dense invariant common differentiability domain: bounded ODE uniqueness on each cap gives \(\partial_b\mathcal T(b,a)\rho=\mathcal L(b)\mathcal T(b,a)\rho\) and the analogous lower-endpoint derivative there. No maximal-domain or graph-core claim is made. The full no-jump contraction is \(\Gamma(V)=\bigoplus_{r\ge0}\wedge^rV\), matching finite-mode actions by density. It is strongly continuous, as follows from finite-particle approximation and uniform contraction, but need not have a bounded full-Fock derivative or bounded full-Fock inverse. The mathematical CPTP extension on odd trace-class operators is not permission to prepare parity-forbidden superpositions: physical density matrices commute with total fermion parity, a property preserved by this evolution.

Collision spacing was sent to zero at fixed \(N\) in B; D is a **separate mathematical compatibility/trace-class limit**. No interchange of those limits, infinite-density representation or infinite-mode microscopic reservoir theorem has been used.

## 2. Required finite cases and controls, checked symbolically

These are exact hand algebra checks supporting the general proof, not samples proving it. No numerical program, theta quadrature, parameter grid or precision campaign was needed. Write \(d_0=c_0/F(v)\), \(e=vc_1/F(v)\), \(f=v^2c_2/F(v)\), \(\alpha=c_1/c_0\).

- **N=0, r=0,1.** \(G_0=-\gamma\), \(R_0=2\gamma\), \(H_0=0\), \(L_0=\sqrt{2\gamma}\,a_0\). Vacuum is fixed; occupied-mode amplitude is \(d_0\), population loss rate \(2\gamma\). In particular \(F(v)\) has not been replaced by \(c_0\).
- **N=1, r=1,2.** \(K_1=\left(\begin{smallmatrix}d_0&e\\0&d_0\end{smallmatrix}\right)\), \(G_1=\left(\begin{smallmatrix}-\gamma&\alpha\\0&-\gamma\end{smallmatrix}\right)\), \(R_1=\left(\begin{smallmatrix}2\gamma&-\alpha\\-\alpha&2\gamma\end{smallmatrix}\right)\). CAR gives \(a_0|0,1\rangle=|1\rangle\), \(a_1|0,1\rangle=-|0\rangle\), and \(\wedge^2K_1=d_0^2\). Explicitly \(\mathcal J(|0,1\rangle\langle0,1|)=2\gamma(|0\rangle\langle0|+|1\rangle\langle1|)+\alpha(|0\rangle\langle1|+|1\rangle\langle0|)\), while \(\mathcal J(|0\rangle\langle1|)=-\alpha|\Omega\rangle\langle\Omega|\). The latter input is an off-diagonal matrix unit, not a positive state. These check interference and the transpose in (3).
- **N=2, r=2.** \(K_2=\left(\begin{smallmatrix}d_0&e&f\\0&d_0&e\\0&0&d_0\end{smallmatrix}\right)\) and \(\Gamma_2K_2|1,2\rangle=(e^2-d_0f)|0,1\rangle+ed_0|0,2\rangle+d_0^2|1,2\rangle\). Thus \(A=v^2(c_1^2-c_0c_2)/F(v)^2\), \(p_J=(e^2-d_0f)^2+e^2d_0^2+d_0^4\). Inserting these into (19) checks both flag probabilities without inferring a new theta sign. The retained 0,1 block of \(G_2,R_2\) is exactly that above, checking cutoff compatibility on the same matrix units.
- **Gaussian, arbitrary symbolic a>0.** \(F=c_0e^{aw}\) gives \(K_v=e^{av(S-I)}\), \(G=a(S-I)\), and the constant loss generator. The finite checks use \(d_0=e^{-av}\), \(e=av e^{-av}\); the vacuum stays \(+1\). Known Gaussian signs supply a comparison, not theta signs.
- **Mandatory polynomial control.** For \(F_*=1+w+2w^2\), E01's exact symbol proves dissipativity throughout the selected interval. The same instrument gives \(\Gamma_2K_*|1,2\rangle=F_*(v)^{-2}[-v^2|0,1\rangle+v|0,2\rangle+|1,2\rangle]\). Hence \(A_*=-v^2/F_*(v)^2<0\) for \(v>0\), \(p_*=(1+v^2+v^4)/F_*(v)^4\), and \(P(0,+_X)-P(0,-_X)=A_*\). This control fails canonical theta reconstruction, **not** the selected dynamical or readout premises.

The remaining [standing collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md) retain B01's exact premise screening. Euler-factor sources change canonical coefficients/normalization identities; weighted-square and finite-prime changes alter weights and can fail full reflection; reflected and smooth positive-primitive sources may preserve selected endpoints but fail the complete theta square expansion. No theta-paid interval is imported to them, no failure of their generic local dissipativity is inferred from failure of exact reconstruction, and no time-zero minor sign is inferred from a positive-time collision. A changed unraveling or unknown controlled phase fails the selected measurement/readout contract even if its channel is the same.

## 3. Scope, deviations and continuation

**A, B, C and D are proved at contract r2's scope.** The main quantitative outputs are the matching-bin instrument estimate (14), the phase-preserving no-count bound (15), and the exact statewise cutoff estimates (25), with the explicit constants and moduli above. Coefficients retain E01's paid domain. All finite cases were checked by hand. One analytical construction sufficed; no architecture change, source change, attenuation, extra observable, numerical campaign or correction pass was required for the author return.

The unresolved work is a source-dependent signed estimate. Generic loss dynamics and CPTP positivity do not provide it, as the negative control shows. No spatial locality, uniform-in-particle success floor, bounded full-Fock generator, exact finite closed bath, joint microscopic infinite-mode limit, new neighboring-index ratio or Mellin-curvature range is claimed. v remains jump-length activity, not source heat time or Mellin tilt.

The authorized next step is **[E] MC08-E03 — Sol, separate checker**, on the frozen E01 and this E02 return with the unchanged B01/r2 inputs. It must assess source bounds, phases/parity, record-valued errors, exact cutoff compatibility, domains and controls; same-model author-support checking does not substitute for it. Once that assessment is integrated, the planned continuation is **[B] MC08-B02 — Astra**, selecting at most two candidate source-dependent mechanisms and returning one worked signed comparison or a reasoned stop. It carries no numerical budget. Current routing and the eventual model-change handoff belong to the sole progress register.
