# MC08-E03: separate assessment of local open quantum dynamics

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Reviewer task **/root/mc08_e03_review**, actual inherited configuration **gpt-6.1-sol (Codex), reasoning effort ultra**. The parent verified that configuration from its local turn_context; the collaboration configuration is inherited. The reviewer was assigned in a separate context after the E02 freeze and did not participate in constructing E02. Own subagent session/turn identifiers were not exposed and are not inferred. The coordinating public chat is 01a19d66-56e2-7ff2-a549-03561c41f801, public turn 01a19de8-de85-7393-b47c-1c650ee88588; those are parent identifiers, not the reviewer's own. One read-only same-model supplemental checker, /root/mc08_e03_review/e03_bound_check, rechecked B/D during this assessment.

**Disposition: accept frozen E01 r1 and E02 r2 at their stated scopes, without mathematical correction. MC08-E03 is complete.** E01 pays the nonzero interval \(0\le v\le1/25\) directly on the infinite one-particle space. E02 satisfies all four r2 obligations: finite-mode count instrument; prescribed fixed-mode collision limit with an induced record-valued trace-norm bound; calibrated same-number signed readout; and exactly compatible vacuum-Fock trace-class extension with a particle-cap differentiability domain. No correction pass was requested or used.

This is a **separate same-model internal LLM assessment with shared frozen inputs and inherited premises**, not cross-model independence or specialist validation. Acceptance is of the written realization and convergence results. It supplies no new theta minor sign, neighboring-index estimate, real-Mellin comparison or RH progress.

## 1. Scope, preservation and exact input versions

The [sole progress register](../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md), its E03 entry, and [frozen E02 request r2](../research-progress/handoffs/02_MC08_E02_CONSTRUCTION_CONTRACT_R2_20261102.md) govern this bounded analytical review. The root AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md and LARGE_FILES.md were read. The review follows the [result index](../../../../../../../result-summaries/README.md), [theta/physical cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [control inventory](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md), particularly [reformulations](../../../../../../../avoid/01_restating_the_target.md), [generic re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [control discipline](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [shared-premise review](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

The following SHA256 values were recomputed and match the issued versions:

| Frozen input | SHA256 |
| --- | --- |
| [E01 Note01](../notes/01_NO_JUMP_ADMISSIBILITY_AUDIT_20261102.md) | 21929f0b5050f699b856aaa899dd1631564aecb2a700a89fa994cbdeeb1fabf5 |
| [E01 exact support program](../numerics/mc08_e01_exact_bounds.py) | 0650394605d7fea6af5b27941d3fa458660f20fe18148dfce1604d546ab2ed8e |
| [E01 exact record](../numerics/MC08_E01_EXACT_BOUNDS_20261102.json) | fba2ae5435515676f801c10b7bfe7dd62e46850d2d066fd5571048f69152fb2f |
| [E01 limited checking record](01_MC08_E01_BOUNDED_CHECK_20261102.md) | 94f920dd1bbee9b93668348c6770f54534f1c0851b9b707db92380dfad9a4161 |
| [B01 Note02](../notes/02_OPEN_SYSTEM_ARCHITECTURE_DECISION_20261102.md) | e20fa974e053b609c49c477a6f1e587b27d5e1969fe3960468eb23d0e47b85c2 |
| [E02 request r2](../research-progress/handoffs/02_MC08_E02_CONSTRUCTION_CONTRACT_R2_20261102.md) | a95b693ac7a34a99d5fc45316672148f75ef7bb139ebcd7ce3fb39ec8820ae41 |
| [E02 Note03](../notes/03_FERMIONIC_LINDBLAD_REALIZATION_20261102.md) | 23c2852f9b0e0c2c97790d27dc29a636c656e175e71ad1f880b7fd4dc73c7a0d |

The underlying versions were also checked: MC02 transfer 61207dbe824e5a67794d7c3be1811a95c1c69fa8006c4c7cc8d703a867706901; separate MC02 assessment 9f7a265228c203d5e3bcc27813a3690b8f9c4ee327f933fcde4301ec0f5a9d0e; continuous-v discussion ca1a8445165cd36d515e81f319824162158851118ab42382780054d6f5da8928; MC08 overview cd337511861cb72380b02a8afc76b15654fa495023f0b90609dda3a0d4a7e88a; source record 12 1ec1f662627653edc9e9e8ccca38a06fc5c252628d46c72ffb5e391e9407359a; E01 handoff 019256a0a93462ae66050018bed2a84d9196fd1d018bc0885fe301d8abea96f7. No mismatch was found.

After reading the support program, the reviewer reran it once with standard-library exact rational arithmetic. Its fresh stdout is **byte-for-byte identical** to the stored JSON and has the same fba2ae...52fb2f hash. No new support file was written. This replay checks the finite rational inequalities and polynomial identity, not the source identity or infinite-dimensional proofs. Those were checked analytically below. No quadrature, theta truncation, mode/angle scan, trajectory campaign or precision escalation was performed. Only this review file is written by this assessment; frozen inputs and live progress are preserved.

## 2. E01: complete source, zero angle, inverse and one-particle completion

**Source normalization and tails accepted.** Differentiating one term of \(\psi=e^u\sum_m e^{-\pi m^2e^{4u}}\) twice gives \((\psi''-\psi)/8=\Phi\), with exactly the stated factors 2 and 3. Jacobi inversion gives \(\vartheta'(1)=-\vartheta(1)/4\), hence \(\psi'(0)=-1/2\) for the complete sum. The classical transformation was freshly inspected at [NIST DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32), with \(z=0,\tau=iy\). The endpoint is not assigned to a truncated theta series.

The integrations by parts give \(c_0=1/16-J_0/8\), \(c_1=(2J_0-J_2)/16\), and \(F(4)=1/16+3C/8\). The same double-exponential majorants justify termwise differentiation and the outer boundary terms. For the upper bounds, the envelope \(e^{-\pi m^2}e^{-(4\pi m^2-1)u}\), summed over all \(m\), pays the entire tail. The integrals are \(1/a\), \(2/a^3\), and \(a/(a^2-4)\), so \(a>11\) and \(\sum e^{-\pi m^2}<1/19\) give the stated \(J_0,J_2,C\) bounds. The lower bound retains only the first mode on \([0,1/16]\); \(\pi e^{4u}<9/2\) and \(e^{9/2}<100\) give \(J_0>1/1600\). The rational exponential estimates and all resulting fractions were replayed exactly.

In particular \(b_1>1/1000\), \(q_4<320/8073<1/25\), and \(|b_n|\le1/(24\,4^n)\) follow. Strict zero-freeness on the closed radius-four disk supplies a genuine analytic neighborhood, so the stated logarithm and Cauchy estimate are legitimate. The norm derivative and inverse formula for \(G\) follow from convergent power series; no endpoint contraction is substituted for instantaneous dissipativity. The inverse estimate can be made explicit:
\[
 \|K_v^{-1}\|
 \le \frac{F(v)/c_0}{1-\|(F(vS)-c_0I)/c_0\|}
 <\frac{26/25}{24/25}=\frac{13}{12}.
\]
The same analytic inverse preserves every finite backward-shift subspace.

**Half-infinite positivity and zero angle accepted.** Fourier expansion on finite sequences gives the stated Toeplitz quadratic form, and norm convergence extends it to all of \(\ell^2\). The inequality
\[
 1-\cos n\theta\le n^2(1-\cos\theta)
\]
pays every possibly negative logarithmic coefficient against the first term. The endpoint coefficient tail is exactly \(2650133/3073907232<7/8000\); thus \(b_1-\text{tail}>1/8000\). Dominated convergence pays the zero-angle quotient with the same \(n^3|b_n|v^{n-1}\) majorant. The relative comparison with \(2I-S-S^\dagger\) does not assert a strictly positive spectral gap: the symbol vanishes at zero, and normalized Hardy/Poisson kernels approach that spectral edge.

The constants \(\|G\|,\|H\|\le2A_*\), \(\|R\|\le4A_*\) follow by summing \(\sum n|b_n|v^{n-1}\le A_*\). Polynomial approximation to \(\sqrt{x}\) on the common compact spectral interval proves norm continuity of \(\sqrt R\), including at the gapless edge. The one-particle no-jump propagator \(V(b,a)=K_bK_a^{-1}\) is a contraction on every intermediate interval by differentiating its squared norm. The bounded trace-class jump expansion converges in map norm; every term is CP, including under finite amplification. The trace identity, bounded ODE uniqueness and interval splitting prove TP and two-parameter composition directly on the infinite one-particle space.

E01's one-particle jump \(\sqrt R\) is correctly kept distinct from E02's particle-loss row. The radius/large-v discussion is scoped correctly: a root inside the shift spectral disk gives a kernel, and a boundary root gives approximate null vectors by truncated unit-modulus eigenvectors and the norm-convergent power series. This obstructs the specified bounded-invertible generator continuation, not every unbounded evolution or enlarged-system model. The proof does not cover \(v=1\), and does not claim failure there.

## 3. E02 A: finite-mode dynamics and the entire instrument

**Accepted.** With the stated CAR and increasing creation order,
\[
 \sum_\mu L_\mu^\dagger L_\mu=d\Gamma(R_N),\qquad
 -iH_{F,N}-\tfrac12d\Gamma(R_N)=d\Gamma(G_N)=D_N.
\]
The coefficient of \(a_j\rho a_k^\dagger\) is \(R_{kj}\), not \(R_{jk}\). This is also the coefficient supplied by the annihilation-row construction in D. The complete scalar \(\gamma=F'/F\) stays on every diagonal even when higher shift powers vanish.

Exterior-power differentiation proves the exact no-jump operator on each sector, with vacuum \(+1\). Inserting the incoherently summed jump map between no-jump propagators yields the CP density for every ordered count-time record. Each loss lowers both surviving particle indices in a density matrix unit; operators with at most \(r\) particles on either side therefore give zero beyond \(r\) jumps. This argument preserves off-diagonal operators and sector coherences, rather than replacing the density equation by a population equation.

The finite jump expansion solves the bounded time-dependent equation. Its trace derivative vanishes on all trace-class operators by cyclicity. CP, TP, uniqueness, composition and CP divisibility follow without a homogeneous-semigroup assertion. Conditional normalization is correctly distinguished from the full instrument/channel.

For conventions, the reviewer freshly inspected [Castin--Dalibard--Mølmer v1, (2), (4)--(11), Section 2](https://arxiv.org/html/0805.4002v1), [Prosen v3, Section 2 (1)--(6), Section 2.1 (20)--(23)](https://arxiv.org/html/0801.1257v3), and [Rivas--Huelga--Plenio v2, (1)--(2)](https://arxiv.org/html/0911.4270v2). Prosen's jump convention converts with \(L_{\rm here}=\sqrt2 L_{\rm Prosen}\). His subsequent operator-space simplification is restricted to even operators; E02 instead proves its maps directly on the whole trace class. These are selected-passage checks, not full-paper/theorem audits. No unbounded, time-dependent infinite-mode or laboratory-reservoir theorem is imported.

## 4. E02 B: collisions, arbitrary trace norm, records and time resolution

**Accepted, including the constants.** Environment-first ordering gives
\[
 W(\Omega_E\otimes f)=\sum_\mu|\mu\rangle\otimes L_\mu f,\qquad
 \langle\Omega_E|W^2|\Omega_E\rangle=d\Gamma(R_N).
\]
The two exchange terms are adjoints. Each exchanges one particle and is even in total fermion parity. With chronological bin ordering, earlier parity strings cancel between the two odd factors, and future bins are vacuum. Thus the leading emission is \(-i\sqrt hL_\mu\) with the frozen convention.

The review independently reconstructed \(d=H_0=2mA_*\), \(j=4mA_*\), \(\ell=2\sqrt{A_*}\), \(w=4m\sqrt{A_*}\). The row norm of \(B_N\), CAR annihilator norm, and particle bound \(m\) pay these bounds. The exponential remainder in E02 (9) is valid for \(h\le1\): the mixed quadratic term costs \(wH_0h^{3/2}\), the Hamiltonian square costs \(H_0^2h^2/2\), and the remaining series costs \(e^cc^3h^{3/2}/6\).

There is no vacuum-to-one-emission block of \(H\) or \(W^2\). Consequently E02 (10)'s stronger \(O(h^{3/2})\) one-emission remainder is justified. The \(q=2^m-m-1\) higher-occupation blocks each have amplitude \(O(h)\), hence map/probability \(O(h^2)\). Comparing the Kraus maps gives precisely the vacuum, \(m\) single-emission and \(q\) multi-emission terms in \(C_c\). For the frozen Lindblad instrument, the vacuum Taylor remainder gives \((2+d)d^2e^d/2\), the one-jump integral gives \(2dj\), and the higher-count tail gives \(j^2e^j/2\). These are valid conservative \(C_L\) terms, including when \(m=1,q=0\).

**Arbitrary operators are covered.** A record-valued CPTP map has a unital CP dual into the bounded record observables. The CP Schwarz inequality and trace duality imply contraction on the complex trace class, not only Hermitian inputs. For a CP trace-nonincreasing subinstrument, the corresponding subunital bound applies. Hence all record extensions used for telescoping are contractions on off-diagonal inputs as required. The auxiliary Euler maps are used only in the local comparison; their failure to sum to TP is not used in telescoping.

The count-register generator is bounded at fixed \(N\) even on its infinite register. Its shifted jump operators have the same summed loss operator because the forward shift is an isometry. Thus its propagator is CPTP, and Duhamel gives the local time-dependent error \(h\omega_N(\delta)\). The modulus
\[
 \omega_N(\delta)=\sup_{|s-t|\le\delta}
 [2\|D_N(s)-D_N(t)\|+\|\mathcal J_N(s)-\mathcal J_N(t)\|]
\]
tends to zero, with \(\omega_N\le m(2\omega_G+\omega_R)\). This uses linear dependence on \(R\) through the annihilation row; it requires no Lipschitz or gap estimate for \(\sqrt R\).

Both instruments are compared on exactly the same vector of bin counts. Summing local bounds with \(\sum h_l^{3/2}\le T\sqrt\delta\), \(\sum h_l^2\le T\delta\le T\sqrt\delta\) proves E02 (14) in the stated induced trace-class-to-record-space norm. Its constants \(C_N=(C_c+C_L)/25,\ C'_N=1/25\) work on every permitted interval. The separately proved no-count amplitude estimate (15) fixes the phase, which averaged-channel convergence would not fix.

For closed-simplex continuous tests, use the coordinate-maximum-distance modulus; each representative changes every ordered coordinate by at most \(\delta\). For bounded continuous tests only on the open strict simplex, compact exhaustion away from the endpoints and diagonals is necessary. The bound \(\|\mathcal I_{N;k}(\mathbf t)\|\le j^k\) pays the omitted exact-instrument volume; matching-bin convergence pays the corresponding collision omission. Uniform continuity on the remaining compact set finishes the argument. This validates weak event-time convergence, including multi-count bins, and makes no atomic-versus-continuous total-variation claim.

Controlling \(H_F,L_\mu,D\) by \(Q_1\) does not increase any bound and leaves the \(Q_0\) arm and its bins exactly unchanged. The same proof therefore covers the flag coherences used in C.

The physical limitation is paid explicitly: duration-\(h\) coupling is \(h^{-1/2}W\), with fresh vacuum modes in every bin. The continuum assertion is fixed-\(N\), with unlimited temporal bath resources. For a locally bounded total Hamiltonian and initial product vacuum, leakage is \(O(v^2)\), whereas the target has a nonzero linear survival loss. This excludes only that regular fixed-vacuum realization class. The collision proof is not a Markov approximation theorem for a selected laboratory reservoir, an exact finite-\(h\) identity or a joint microscopic mode limit.

## 5. E02 C and finite hand checks: sign, phase, parity and success

**Accepted.** After no count, the unnormalized flag matrix is
\[
 \tfrac12\begin{pmatrix}1&A^*\\A&p_J\end{pmatrix}.
\]
Thus \(q_0=(1+p_J)/2\), \(P(0,\pm_X)=(1+p_J\pm2\operatorname{Re}A)/4\). For the displayed Pauli \(Y\), \(P(0,\pm_Y)=(1+p_J\pm2\operatorname{Im}A)/4\); the imaginary-part sign is positive. The determinant expression for \(p_J\) is the column-wedge norm. The signal normalization \(p_J\), flag normalization \(q_0\), and ordered-amplitude factor \(v^{\sum J-\sum I}/F(v)^r\) are retained separately. Negative coefficient indices mean zero, as in the frozen MC02 baseline.

The inverse restriction gives \(p_J\ge(12/13)^{2r}\). The vacuum has \(A=p_J=q_0=1\); at \(v=0\), \(T=I\), so \(A=\delta_{I,J}\) and both survival probabilities are one. There is no signal-success floor uniform in \(r\) or efficient-estimation conclusion.

The reviewer checked each required finite case directly:

| Case | Reconstructed check |
| --- | --- |
| \(N=0,r=0,1\) | Vacuum fixed; occupied amplitude \(c_0/F(v)\); \(G_0=-\gamma\), \(R_0=2\gamma\), loss rate \(2\gamma\). Full \(F\), not \(c_0\), normalizes the occupied sector. |
| \(N=1,r=1,2\) | \(K_1=\left(\begin{smallmatrix}d&e\\0&d\end{smallmatrix}\right)\), \(G_1=\left(\begin{smallmatrix}-\gamma&\alpha\\0&-\gamma\end{smallmatrix}\right)\), \(\wedge^2K_1=d^2\). The CAR signs are \(a_0\lvert0,1\rangle=\lvert1\rangle,\ a_1\lvert0,1\rangle=-\lvert0\rangle\). The pair-density jump has positive \(\alpha\) cross terms, whereas \(\mathcal J(\lvert0\rangle\langle1\rvert)=-\alpha\lvert\Omega\rangle\langle\Omega\rvert\). |
| \(N=2,r=2\) | For \(I=(0,1),J=(1,2)\), \(\Gamma_2K_2\lvert1,2\rangle=(e^2-df)\lvert0,1\rangle+ed\lvert0,2\rangle+d^2\lvert1,2\rangle\). Hence \(A=v^2(c_1^2-c_0c_2)/F^2\) and \(p_J=(e^2-df)^2+e^2d^2+d^4\). Substitution into both flag probabilities agrees. The lower-mode \(G,R\) blocks and the same matrix units restrict exactly. |
| Gaussian, arbitrary \(a>0\) | \(F=c_0e^{aw}\), \(K=e^{av(S-I)}\), \(G=a(S-I)\); the generator is constant and the vacuum phase remains \(+1\). |
| Polynomial \(1+w+2w^2\) | The exact all-coefficient symbol identity and its positive factors give dissipativity on the stated interval. In the same readout \(A=-v^2/F_*^2\), \(p_J=(1+v^2+v^4)/F_*^4\), and \(P(0,+_X)-P(0,-_X)=A<0\) for \(v>0\). |

Here \(d=c_0/F,\ e=vc_1/F,\ f=v^2c_2/F,\ \alpha=c_1/c_0\). These are convention checks supporting general proofs, not a finite-sample proof for all sectors.

Same-number arms respect parity, including odd \(r\); number-preserving controlled mode preparations can map a chosen ordered Slater state to either arm while calibrating the known determinant/permutation phase. The neutral flag does not require a vacuum-to-odd-particle superposition. Ideal no count leaves the identical vacuum record on both arms; the separate amplitude limit preserves its phase. Coherent controlled dynamics is an extra resource and is not determined by an arbitrary CPTP channel black box.

## 6. E02 D: exact restrictions, full instrument and domain

**Accepted.** For a lower-mode supported operator, \(D_M=d\Gamma(G_M)\) preserves the support, since the backward-shift invariant restriction of \(G_M\) is \(G_N\). The right term \(\rho D_M^\dagger\) preserves it as the adjoint of \(D_M\rho^\dagger\), even though \(G_M^\dagger\) alone need not preserve the ket subspace. In the jump map, a high annihilation index kills the corresponding ket or bra. The retained \(R_M\) block is exactly \(R_N\). Thus the no-jump maps, summed-channel count instrument and full channel restrict exactly, by the bounded equations/trajectory formulas. Neither \(\sqrt{R_N}=P_N\sqrt RP_N\) nor compatibility of individual detector jumps or finite collision unitaries is assumed.

On a cap of at most \(r\) particles, the annihilation row has norm at most \(\sqrt r\). Its dual gives
\[
 \mathcal J_R^*X=\mathfrak a^\dagger(R\otimes X)\mathfrak a,\quad
 \|\mathcal J_R-\mathcal J_{R'}\|_{1\to1}\le r\|R-R'\|.
\]
This confirms the transpose convention, continuity and cutoff-independent cap estimate. With \(\|d\Gamma_r(G)\|\le r\|G\|\), it proves \(\|\mathcal L(v)\|\le2r\|G\|+r\|R\|\le8rA_*\). The cap trace identity ensures TP of its bounded jump expansion, which stops after \(r\) jumps. This is a bounded generator on each cap, not on full Fock space.

Finite-mode trace classes have dense union because \(\Pi_N\to I\) strongly and two-sided compression converges in trace norm. Exact compatibility and contraction give a unique extension. At every finite amplification positivity passes through trace-norm limits; trace and composition also pass by continuity. Finite-mode approximation plus contraction gives statewise joint time continuity.

The instrument has the same argument with target \(\bigoplus_{k\ge0}L^1(\Delta_k;\mathfrak T)\), including its zero-count atom. This is the classical record predual with integrated trace norm. The finite-mode instruments are consistent contractions into this fixed space, so their completion is CP, integrates to the channel, and retains concatenation. On caps it agrees with the explicit trajectory densities. In particular no infinite-count atom is needed for a vacuum-Fock density operator, even if its expected number is infinite: approximation and total trace preservation account for the whole record probability. No bound on that expectation is inferred.

By exact restriction, the cutoff difference is simply \(\mathcal T(b,a)(\rho-\Pi_N\rho\Pi_N)\). Contraction proves the stated unnormalized-input estimate with constant one, uniformly in the allowed endpoints. The same reasoning gives particle-cap and record-valued estimates. These are statewise statements, with no all-state operator-norm rate.

Each \(\mathfrak T_r\) is invariant, norm-continuous coefficients give the endpoint derivatives there, and their union is dense. This proves the declared common differentiability domain without asserting maximality or a graph core. Finally \(\Gamma(V)=\bigoplus_r\wedge^rV\) is a bounded contraction with vacuum \(+1\); finite-particle approximation proves strong continuity. Neither its full-Fock derivative nor its full-Fock inverse is assumed bounded. The mathematical extension to odd operators does not authorize physical parity superpositions.

## 7. Control interpretation, remaining limitations and disposition

The polynomial is decisive: it passes dissipativity, the same selected instrument and the same signed observation but retains a negative minor. It fails canonical theta reconstruction. Therefore CP, loss counting, fermion antisymmetry and the coherent flag do not sign arbitrary ordered minors.

The remaining families retain the [standing inventory's](../../../../../../../result-summaries/12_collision_controls_and_screening.md) separate failed premises: Euler-factor changes alter the canonical coefficients/normalization data; weighted-square and finite-prime changes alter canonical weights and may fail full reflection; reflected and positive-primitive controls can preserve specified shape/endpoints while failing the complete arithmetic square expansion. The assessment accepts this screening only at those named premises. It neither assigns them uncomputed time-zero signs nor declares failure of their own generic small-\(v\) dissipativity. Theta's paid constants are not transferred to modified sources. A different unraveling or uncontrolled Kraus phase fails the fixed instrument/readout contract.

**Required corrections: none. Unresolved gaps in A--D at the issued r2 scope: none identified.** Acceptance remains limited to the vacuum Fock representation, the local interval, unrestricted dense mode couplings, ideal unit-efficiency counting, calibrated coherent control and a collision limit taken at each fixed mode cutoff. Spatial locality, a bounded regular closed reservoir, hardware feasibility, a uniform particle-success floor, a bounded full-Fock generator/inverse, a maximal-domain/core theorem, all-state cutoff rates and interchange of microscopic/mode limits are not established.

The unpaid scientific step remains a source-dependent signed comparison with its actual denominator and index/domain quantifiers. The accepted representation is not such an estimate; \(v\) remains activity, not Mellin tilt or source heat time. E03 stops here. The coordinator may integrate this disposition and the already declared **Next: [B] MC08-B02 — Astra** decision into the sole register; no B02 work or numerical campaign was started by this review.
