# Hamiltonian construction: equations and finite startup energies

3 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual **gpt-6.1-sol (Codex), reasoning effort ultra**, chat `01a19fdd-4e1e-7061-9ec4-141ca78368ce`, turn `01a1a008-e326-7792-b6a3-08c61b641927`, brainstorm history **0002**. One read-only inherited same-model agent checked the displayed block, finite startup-energy and bath-frame algebra; this is support for this exposition, not independent review.

**Status:** equations requested by the author, expanding the already accepted E06 construction. The block multiplication, finite startup eigenvalues and bath-unitary freedom are elementary explanatory deductions, with same-execution algebraic checking only. They are not a separately assessed B04 model/energy selection. No infinite-generator analysis, numerical campaign or E07 request is executed.

## 1. Source energy and the prescribed transfer

The source spectrum is already specified on positive circle modes:
\[
L_+|n\rangle=E_n|n\rangle,\quad E_n=\pi n^2,\quad n\ge1.
\]
For \(\beta=e^{4u}\), \(P_0(x)=2x^2-3x\),
\[
\Phi(u)=e^u\sum_{n\ge1}P_0(\beta E_n)e^{-\beta E_n},\qquad
c_j=\frac1{(2j)!}\int_0^\infty u^{2j}\Phi(u)\,du,\qquad F(w)=\sum_{j\ge0}c_jw^j.
\tag{1}
\]
These are the existing reviewed source identities, not a new source model. The coefficient sites are different labels. At fixed \(N\ge0\), \(m=N+1\), set \(S_Ne_j=e_{j-1}\) for \(j\ge1\), \(S_Ne_0=0\), so
\[
K_{v,N}=\frac{F(vS_N)}{F(v)}
=\frac1{F(v)}\sum_{j=0}^{N}c_jv^jS_N^j,\qquad K_{0,N}=I.
\tag{2}
\]
The numerator terminates by nilpotence; the scalar denominator stays complete. Thus finite N is a coefficient-space cutoff, not a cutoff of the source spectrum in (1).

The chosen transfer is useful because for increasing occupied sets I,J of size r,
\[
\langle I|\Gamma(K_{v,N})|J\rangle
=\frac{v^{\sum J-\sum I}}{F(v)^r}\det[c_{j_b-i_a}],\qquad v>0,
\tag{3}
\]
with negative coefficient indices zero, and K_0=I directly at zero. The construction begins with this phase-calibrated amplitude requirement.

## 2. Reduced coherent Hamiltonian forced by the transfer

On the established interval 0<=v<=1/25, K is invertible. The equation psi(v)=K_v psi(0) forces
\[
\psi'=G_N(v)\psi,\qquad
G_N=K'_vK_v^{-1}
=S_NF'(vS_N)F(vS_N)^{-1}-\gamma(v)I,\quad \gamma=F'/F.
\tag{4}
\]
For a no-count step M_0=I+G_N dv+o(dv) and count steps M_mu=sqrt(dv) L_mu+o(sqrt(dv)), probability completeness yields
\[
G_N+G_N^\dagger+\sum_\mu L_\mu^\dagger L_\mu=0.
\]
Thus the Hermitian/dissipative decomposition in the Schrödinger convention hbar=1 is
\[
R_N=-(G_N+G_N^\dagger),\qquad
H_N=\frac i2(G_N-G_N^\dagger),\qquad
G_N=-iH_N-\tfrac12R_N.
\tag{5}
\]
E01/E03 supply the substantive source-paid statement
\(R_N(v)\ge(2I-S_N-S_N^\dagger)/8000\ge0\).
The splitting is unique once the fixed basis, entire transfer path, clock and phase convention are fixed. Positivity does not follow from merely writing (5).

For explicit hopping coefficients, put
\[
\log(F(w)/c_0)=\sum_{n\ge1}b_nw^n,\qquad b_1=c_1/c_0=:q>0.
\]
Then
\[
G_N=\sum_{n\ge1}n b_n v^{n-1}(S_N^n-I),
\]
\[
H_N=\frac i2\sum_{n\ge1}n b_n v^{n-1}[S_N^n-(S_N^\dagger)^n],
\quad
R_N=\sum_{n\ge1}n b_n v^{n-1}[2I-S_N^n-(S_N^\dagger)^n].
\tag{6}
\]
In G/R the scalar terms include the entire series even when shift powers vanish. H's shift terms terminate at n=N. Individual b_n need not be positive.

For v=at², a>0,
\[
\widetilde G_N(t)=2atG_N(at^2),\quad
\widetilde H_N(t)=2atH_N(at^2),\quad
\widetilde R_N(t)=2atR_N(at^2).
\tag{7}
\]
On system Fock space the coherent Hamiltonian and loss jumps are
\[
\mathbb H_{\rm red,N}(t)=d\Gamma(\widetilde H_N(t)),\qquad
\widetilde L_{\mu,N}(t)=\sqrt{2at}\sum_j(\sqrt{R_N(at^2)})_{\mu j}a_j.
\tag{8}
\]
The no-count generator is dGamma(tilde G), not -i times the coherent Hamiltonian alone.

For N=1,
\[
K_{v,1}=\frac1{F(v)}\begin{pmatrix}c_0&vc_1\\0&c_0\end{pmatrix},\quad
G_1=\begin{pmatrix}-\gamma&q\\0&-\gamma\end{pmatrix},\quad
H_1=\frac q2\begin{pmatrix}0&i\\-i&0\end{pmatrix},\quad
R_1=\begin{pmatrix}2\gamma&-q\\-q&2\gamma\end{pmatrix}.
\tag{9}
\]
The reduced one-particle instantaneous energies for the quadratic clock are +/-at q. They vanish at startup. This H is selected by the desired conditional transfer; no diagonal pi n² on coefficient sites was imposed.

## 3. One selected total system–environment Hamiltonian

E06 supplies an explicit regular joint model for every fixed N and a>0 on 0<=t<=1/sqrt(25a). Put
\[
C(t)=K_{at^2,N},\quad D(t)=(I-C^\dagger C)^{1/2},\quad E(t)=(I-CC^\dagger)^{1/2},
\]
\[
U(t)=\begin{pmatrix}C&-E\\D&C^\dagger\end{pmatrix}
\quad\text{on }\mathbb C_S^m\oplus\mathbb C_E^m.
\tag{10}
\]
The defect identity EC=CD and its adjoint prove both unitary products; U(0)=I. This is the previously source-checked Halmos completion with its specified sign conversion. It is a choice of full joint path implementing C, not the only joint path allowed by C.

The total one-particle Hamiltonian is then forced by the Schrödinger equation for this chosen U:
\[
i\dot U=h_{\rm tot,N}U
\quad\Longrightarrow\quad
h_{\rm tot,N}=i\dot U U^\dagger.
\tag{11}
\]
Differentiating UU†=I proves Hermiticity. Multiplication gives all four blocks explicitly:
\[
\boxed{
h_{\rm tot,N}=i\begin{pmatrix}
\dot C C^\dagger+\dot E E&\dot C D-\dot E C\\
\dot D C^\dagger-\dot C^\dagger E&\dot D D+\dot C^\dagger C
\end{pmatrix}.}
\tag{12}
\]
Here dot C=2at G_N(at²)C. At t>0, derivatives of the positive square roots are specified without a commuting-matrix assumption by the Sylvester equations
\[
D\dot D+\dot D D=-(\dot C^\dagger C+C^\dagger\dot C),
\quad E\dot E+\dot E E=-(\dot C C^\dagger+C\dot C^\dagger).
\tag{13}
\]
The defects are positive definite for positive time at each fixed N, so these equations have unique Hermitian solutions. One may not generally replace them with scalar square-root differentiation.

With system-first ordering, the total Fock Hamiltonian is
\[
\mathbb H_{\rm tot,N}(t)=d\Gamma(h_{\rm tot,N}(t))
=\sum_{\alpha,\beta=1}^{2m}(h_{\rm tot,N})_{\alpha\beta}f_\alpha^\dagger f_\beta,
\tag{14}
\]
where f contains the system and bath CAR modes in that order. It generates Gamma(U), preserves total particle number/parity and has vacuum energy/phase zero/+1. The initial bath is vacuum, and
\[
\langle\Omega_E|\Gamma(U(t))|\Omega_E\rangle=\Gamma(C(t)).
\tag{15}
\]
Keeping no environment factors in the exterior product proves (15), hence the exact signed amplitudes (3). The full reduced channel instead traces over all bath outcomes. Its continuous monitored record is not identified with the old loss instrument.

## 4. Startup exchange and its finite energies

At zero activity,
\[
G_N(0)=q(S_N-I),\quad R_N(0)=q A_N,\quad A_N=2I-S_N-S_N^\dagger>0.
\]
For the quadratic clock,
\[
C(t)=I+at^2G_N(0)+O(t^4),\quad
D(t)=\sqrt a\,t\sqrt{R_N(0)}+O(t^3),\quad
E(t)=\sqrt a\,t\sqrt{R_N(0)}+O(t^3).
\]
E06 proves smoothness by factoring D=t sqrt(Q_D), E=t sqrt(Q_E), with both Q(0)=aR_N(0)>0. Thus (12) has the regular startup value
\[
\boxed{h_{\rm tot,N}(0)=\begin{pmatrix}0&-iB_N\\iB_N&0\end{pmatrix},\quad B_N=\sqrt{aR_N(0)}.}
\tag{16}
\]
In combined CAR notation its Fock lift is the exchange
\[
\mathbb H_{\rm tot,N}(0)=i\sum_{\mu,j}(B_N)_{\mu j}
[b_\mu^\dagger a_j-a_j^\dagger b_\mu],
\tag{17}
\]
where B_N is real symmetric and b_mu denotes combined bath modes, including the parity string in an ordinary tensor representation. The two terms are adjoints with opposite imaginary coefficients, so the operator is Hermitian. The vanishing initial reduced coherent Hamiltonian does not imply a vanishing total exchange Hamiltonian.

The finite startup energies follow exactly from (16). The sine eigenvectors
\[
w_k(j)=\sqrt{\frac2{m+1}}\sin\frac{(j+1)k\pi}{m+1},\quad j=0,\ldots,m-1,
\]
satisfy
\[
A_Nw_k=\lambda_kw_k,\quad \lambda_k=2-2\cos\frac{k\pi}{m+1},\quad k=1,\ldots,m.
\]
Hence the total one-particle startup energies are
\[
\boxed{\varepsilon_{k,\pm}(0)=\pm\sqrt{a q\left(2-2\cos\frac{k\pi}{m+1}\right)}.}
\tag{18}
\]
Indeed the normalized vectors (w_k, +/-i w_k)/sqrt(2) have the displayed +/- energies. For N=0 they are +/-sqrt(2aq); for N=1 they are +/-sqrt(aq) and +/-sqrt(3aq). In Fock space an occupied set of these energy eigenmodes has energy equal to their sum; normal ordering fixes the empty set at zero. Negative eigenvalues mean vacuum zero is a phase/reference convention, not a ground-state assertion. These are finite startup equations only, not the spectrum at all times or an infinite-generator theorem.

## 5. Why energy meaning remains a choice

The source energies E_n=pi n² in (1) and the startup energies (18) belong to different operators and different mode spaces. The latter depend explicitly on clock scale a and the coefficient ratio q. A physical or mathematical correspondence must be stated; it does not follow from a relabeling of the modes.

There is explicit freedom even after C is fixed. For a differentiable bath unitary V_E(t) with V_E(0)=I, put
\[
W(t)=I_S\oplus V_E(t),\qquad \widehat U(t)=W(t)U(t).
\]
Its system block remains C, and Gamma(V_E) fixes the bath vacuum, so (15) remains unchanged. Its generator is
\[
\widehat h=i\dot W W^\dagger+W h_{\rm tot,N}W^\dagger.
\tag{19}
\]
If interpreted as a passive moving frame, states and observables must be transported too; if interpreted as a new active drive in the same fixed frame, it is another physical Hamiltonian with the same endpoint vacuum amplitude. This equation illustrates why the amplitude condition alone does not uniquely fix microscopic energies. It selects no alternative architecture here.

Even in a time-independent finite system,
\[
\langle I|e^{-it h}|J\rangle
=\sum_\alpha e^{-it\varepsilon_\alpha}
\langle I|\varphi_\alpha\rangle\langle\varphi_\alpha|J\rangle.
\tag{20}
\]
Both eigenvalues and eigenvector overlaps enter. In the driven case the propagator is the time-ordered exponential of the full h(t), not simply the exponential of its instantaneous energy list. Therefore finite-energy analysis should include the energy observable, couplings and target matrix elements before selecting a needed limit theorem.

## Continuation and scope

The construction is an inverse realization: complete theta source -> prescribed K -> reduced G,H,R; then a chosen full U -> driven h_tot. E06 validates that finite realization at its specified local interval. It does not establish a source-spectrum selection principle or a new signed estimate. A meaningful energy-first B04 would identify which energy observable/response and which relation to the complete source can contribute additional information about the original signed consumer.

Read [E06 Derivation05](05_MC08_E06_QUADRATIC_CLOCK_DERIVATIONS_20261103.md), [Assessment01/inheritance](../reviews/01_MC08_E06_QUADRATIC_CLOCK_ASSESSMENT_20261103.md), [energy-priority Note06](06_ENERGY_PRIORITY_FINITE_LIMITS_AND_INDIRECT_ROUTES_20261103.md), and [Handoff08](../../research-progress/handoffs/08_MC08_E06_RETURN_AND_B04_MODEL_CONTINUATION_20261103.md). Read also the [result index](../../../../../../../../result-summaries/README.md), especially [theta/bookkeeping](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and [avoid index](../../../../../../../../avoid/README.md), especially [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [normalization conventions](../../../../../../../../avoid/08_normalization_and_constant_slips.md). Source attribution and original source PDF receipts remain in their existing records; no new literature theorem is imported here.

**Next: [B] MC08-B04 — Astra, energy-first**, under the existing bounded contract. No model is switched automatically. Preserve history 0002 on continuation; actual future model/effort belongs in its metadata. The [sole MC08 register](../../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md) owns readiness. No frozen input, manuscript or issued request was edited for this exposition.
