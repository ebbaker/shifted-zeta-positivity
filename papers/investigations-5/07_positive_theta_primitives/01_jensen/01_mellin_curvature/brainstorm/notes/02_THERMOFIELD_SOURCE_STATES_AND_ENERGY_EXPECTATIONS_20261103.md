# Thermofield source states and energy expectations

3 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance: **gpt-6-astra (Codex), recorded reasoning effort xhigh**. Chat `01a1a455-6c1d-7aa2-9723-43ab36704924`, turn `01a1a459-9b76-7c81-906a-979776e168e8`; unique Mellin-curvature history **0004**.

**Status and purpose.** Author-requested brainstorming, saved outside MC08. Exact identities below are derived here or explicitly inherited; they have same-assistant algebraic checking only. They supply a state/observable correspondence and a narrowly scoped incompatibility, not a new determinant sign estimate, an RH result, a selected physical dynamics, or a new investigation launch. No numerical campaign or execution task is issued. This discussion does not revise the earlier open-quantum-dynamics contracts.

The starting references are [Handoff10](../../08_open_quantum_dynamics/research-progress/handoffs/10_NATURAL_HAMILTONIAN_BRAINSTORM_CONTINUATION_20261103.md), [source-state Note08](../../08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md), and the [MC01 thermal dictionary, especially Sections 2–6](../../01_circle_thermal_trace/notes/01_THERMAL_SOURCE_IDENTITY_RETURN_20261101.md). Baker's [2020 paper, equations (2.1)–(2.4)](https://arxiv.org/pdf/2001.02713v1#page=3) supplies the thermofield starting point; see the [checked reference record](../references/01_BAKER_THERMOFIELD_2020.md).

Read with the [result summaries](../../../../../../../result-summaries/README.md), specifically [theta identities](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [patterns to avoid](../../../../../../../avoid/README.md), specifically [reformulations](../../../../../../../avoid/01_restating_the_target.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [circular assumptions](../../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md).

## 1. The original mixed amplitudes

Use the complete source at physical heat time zero:
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad c_k=\int_0^\infty\frac{u^{2k}}{(2k)!}\Phi(u)\,du.
\]
Set \(c_k=0\) for negative integers. In \(\mathfrak h_u=L^2((0,\infty),du)\), put
\[
\chi=\sqrt\Phi,\quad m_j(u)=\frac{u^{2j}}{(2j)!},\quad
f_i=\frac{\Phi^{(2i)}}{\chi},\quad g_j=m_j\chi.
\tag{1}
\]
Complete-source evenness, rapid decay, and integration by parts give
\[
\langle f_i,g_j\rangle=\int_0^\infty m_j\Phi^{(2i)}\,du=c_{j-i}.
\tag{2}
\]
At zero, each boundary term has an odd derivative of either the even source or the even monomial; at infinity it vanishes by decay. When \(i>j\), the differentiated polynomial vanishes. These arguments use the full reflected source; they are not automatically true for an individual thermal mode.

For increasing finite lists \(I=(i_1,\ldots,i_r)\), \(J=(j_1,\ldots,j_r)\), use the exterior-product convention whose coordinate Slater determinant has factor \(1/\sqrt{r!}\). Then
\[
F_I=\bigwedge_a f_{i_a},\quad G_J=\bigwedge_b g_{j_b},\qquad
D_{I,J}:=\det[c_{j_b-i_a}]=\langle F_I,G_J\rangle.
\tag{3}
\]
With \(M^f_I=(\langle f_{i_a},f_{i_b}\rangle)\), and similarly \(M^g_J\), the normalized overlap is
\[
\langle\widehat F_I,\widehat G_J\rangle=
\frac{D_{I,J}}{\sqrt{\det M^f_I\det M^g_J}},
\tag{4}
\]
when both wedges are nonzero. Squaring this overlap changes the target and loses its sign.

## 2. The primitive is a thermofield normalization

Let \(h|n\rangle=E_n|n\rangle\), \(E_n=\pi n^2\), \(n\ge1\), and
\[
\beta=e^{4u},\quad Q(\beta)=\operatorname{Tr}e^{-\beta h},\quad p(u)=e^uQ(e^{4u}).
\tag{5}
\]
A geometric realization is the Dirichlet interval operator \(h=-\pi^{-1}\partial_x^2\) on \((0,1)\), with domain \(H^2\cap H^1_0\). Alternatively, use one representative of each nonzero circle pair for \(-\pi\partial_x^2\) on a circle of circumference \(2\pi\). The common heat trace alone does not choose between these geometries.

Baker's equation (2.3), in this spectrum, is
\[
|\mathrm{TFD}_\beta\rangle=Q(\beta)^{-1/2}
\sum_{n\ge1}e^{-\beta E_n/2}|n\rangle_L|\bar n\rangle_R,
\quad \rho_\beta=\frac{e^{-\beta h}}{Q(\beta)}.
\tag{6}
\]
The bar fixes the conjugate-copy convention. Partial trace over the right copy gives \(\rho_\beta\); a left observable satisfies \(\langle O_L\rangle_{\mathrm{TFD}}=\operatorname{Tr}(\rho_\beta O)\), whenever the expectation exists. No many-body approximation from the rest of the paper is used here.

Define the unnormalized fiber vector
\[
|B(u)\rangle=e^{u/2}\sum_n e^{-\beta E_n/2}|n,\bar n\rangle.
\]
Then \(\|B(u)\|^2=p(u)\). Thus the scalar primitive is the norm squared of a thermofield amplitude, or equivalently a scaled partition function. It is not itself a trace-one density matrix.

The complete source obeys
\[
\Phi=\frac{p''-p}{8}
=e^u\operatorname{Tr}\big[P_0(\beta h)e^{-\beta h}\big],
\qquad P_0(x)=2x^2-3x.
\tag{7}
\]
In particular,
\[
\frac{\Phi(u)}{p(u)}
=\langle\mathrm{TFD}_\beta|P_0(\beta h_L)|\mathrm{TFD}_\beta\rangle
=2\beta^2\langle h^2\rangle_\beta-3\beta\langle h\rangle_\beta.
\tag{8}
\]
Writing \(U_\beta=\langle h\rangle_\beta\), this is
\(2\beta^2(U_\beta^2+\operatorname{Var}_\beta h)-3\beta U_\beta\).
The energy mean and fluctuations both enter. Equation (8) is already an exact energy-observable expectation, with a polynomial observable rather than the mean of \(h\) alone.

For \(u\ge0\), \(\beta E_n\ge\pi>3/2\), so define
\[
|\Omega(u)\rangle=P_0(\beta h_L)^{1/2}|B(u)\rangle,
\qquad \|\Omega(u)\|^2=\Phi(u).
\tag{9}
\]
Its normalized version \(|\omega_u\rangle=|\Omega(u)\rangle/\sqrt\Phi\) purifies
\[
\rho_u^\Phi=\frac{P_0(\beta h)e^{-\beta h}}{Z_\Phi(\beta)},
\qquad Z_\Phi(\beta)=e^{-u}\Phi(u).
\tag{10}
\]
This is a filtered Gibbs state of the original \(h\). Algebraically it is Gibbs for
\(h_{\mathrm{eff}}(\beta)=h-\beta^{-1}\log P_0(\beta h)\), which is temperature dependent. That identity supplies no separately selected fixed Hamiltonian. A purification by itself also does not choose a dynamics on the doubled space; \((h_L-h_R)|\mathrm{TFD}_\beta\rangle=0\), for example, is not the desired determinant energy.

## 3. Redefining the response orbitals without changing the determinant

Use the inherited source-response polynomials
\[
P_{k+1}(x)=4xP_k'(x)+(1-4x)P_k(x),\qquad
R_i(x)=\frac{P_{2i}(x)}{P_0(x)}.
\tag{11}
\]
Then
\[
\Phi^{(2i)}(u)=e^u\sum_nP_{2i}(\beta E_n)e^{-\beta E_n},\qquad
r_i(u):=\frac{\Phi^{(2i)}}\Phi
=\langle\omega_u|R_i(\beta h_L)|\omega_u\rangle.
\tag{12}
\]
In particular \(R_0=1\) and
\(P_2=32x^4-224x^3+330x^2-75x\). These higher response observables need not be positive.

Work in
\(\mathcal K=L^2((0,\infty),du;\mathcal H_E\otimes\overline{\mathcal H_E})\).
The isometry \((T\psi)(u)=\psi(u)\omega_u\) sends
\[
(Tf_i)(u)=r_i(u)\Omega(u),\qquad
(Tg_j)(u)=m_j(u)\Omega(u).
\]
There is also a different, useful preparation:
\[
\widetilde f_i(u)=R_i(\beta h_L)\Omega(u),\qquad
\widetilde g_j(u)=m_j(u)\Omega(u).
\tag{13}
\]
It exposes the energy label instead of replacing its response by the conditional mean. Direct calculation gives
\[
\boxed{\langle\widetilde f_i,\widetilde g_j\rangle
=\int_0^\infty m_j(u)e^u\sum_nP_{2i}(\beta E_n)e^{-\beta E_n}\,du
=c_{j-i}.}
\tag{14}
\]
Consequently the wedges of the new orbitals have precisely the unnormalized overlap (3).

The change in norms is essential, not an error to suppress. With \(\Pi_u=|\omega_u\rangle\langle\omega_u|\),
\[
\Pi\widetilde f_i=Tf_i,\qquad
\|\widetilde f_i\|^2-\|f_i\|^2
=\int_0^\infty\Phi(u)\operatorname{Var}_{\rho_u^\Phi}(R_i(\beta h))\,du\ge0.
\tag{15}
\]
The added component is orthogonal to every lifted \(g_j\), so the mixed overlaps stay fixed. More generally the Gram-matrix increment is an integrated covariance matrix. Normalized wedge amplitudes must therefore use the new Gram determinants. No assertion that (13) is the original isometry, or that it preserves transition probabilities, is made.

Nor is \(\widetilde f_i\) simply \(\partial_u^{2i}\Omega\): differentiating a norm squared produces cross terms. Formula (11) differentiates the full thermal weight, and preserves those terms in the response observable.

## 4. Exact expectation values for coefficients and determinants

The field \(\Psi(u)=\Omega(u)/\sqrt{c_0}\) is a normalized vector in \(\mathcal K\), since \(\int\Phi=c_0\). Let \(U\) be multiplication by \(u\) and \(X=e^{4U}h_L\). Their joint spectral calculus gives
\[
\boxed{\frac{c_{j-i}}{c_0}
=\langle\Psi|m_j(U)R_i(X)|\Psi\rangle.}
\tag{16}
\]
The real multiplier defines a self-adjoint observable on its maximal multiplication domain. All finite response and moment orders in (13)–(16) are integrable: \(P_0\) has no zero on \([\pi,\infty)\), the response grows only polynomially in \(X\), and the thermal exponential dominates both the energy sum and the source tail. This does not prove a new differential Hamiltonian domain theorem.

An equivalent description using the ordinary, unfiltered thermofield field is useful. Put \(b_0=\int_0^\infty p(u)du\), \(\Psi_p=B/\sqrt{b_0}\). Then
\[
\frac{c_{j-i}}{b_0}
=\langle\Psi_p|m_j(U)P_{2i}(X)|\Psi_p\rangle.
\tag{17}
\]
For \(i=0\), this is an expectation of the nonnegative observable \(m_j(U)P_0(X)\). The filtered construction moves its square root into the wavefunctions, exactly the sort of redistribution between state and operator contemplated by the author.

For \(r\) independent copies, define the commuting, real multiplier
\[
\mathcal E_{I,J}=\frac1{r!}
\det_{a,k}[R_{i_a}(X_k)]\,
\det_{b,k}[m_{j_b}(U_k)].
\tag{18}
\]
Then the exact signed determinant is
\[
\boxed{D_{I,J}=c_0^r
\langle\Psi^{\otimes r}|\mathcal E_{I,J}|\Psi^{\otimes r}\rangle.}
\tag{19}
\]
For clarity, expanding both determinants and integrating each copy independently produces \(r!\det[\langle\widetilde f_{i_a},\widetilde g_{j_b}\rangle]\); this proves the factor in (18). Equivalently this is Andreief's identity for the joint positive measure
\(e^uP_0(\beta E_n)e^{-\beta E_n}du\) with a sum over \(n\). The determinant's antisymmetry has been converted to a symmetric product of two alternating observables. Repeated spectral labels are allowed; one must not impose a new distinct-energy occupation constraint on the source Slater problem.

Equation (19) is a genuine single expectation of a self-adjoint observable, and retains the sign. Calling a chosen energy scale times \(\mathcal E_{I,J}\) a Hamiltonian is mathematically possible, but it is an order- and index-dependent many-copy interaction. Its naturalness, lower bound and dynamical role do not follow from the formula. In particular it is not the free many-particle Hamiltonian \(\sum_k h_k\). The source integration also combines different \(\beta\)'s: \(\Psi\) is a normalizable purification field, not an asserted single-temperature equilibrium of a fixed Hamiltonian on \(\mathcal K\).

There is no need to treat a formal diagonal density in a continuous \(u\) basis as trace class: \(|\Psi\rangle\langle\Psi|\) is an actual rank-one trace-class density operator. Conditional thermal expectations suffice for (16)–(19).

At \(r=2\), \(I=(0,1)\), \(J=(k,k+1)\), the determinant is \(c_k^2-c_{k-1}c_{k+1}\). Conditionally averaging the spectral labels in (18) produces the source-coordinate interaction
\[
\frac12[r_1(u_2)-r_1(u_1)]
\frac{(u_1u_2)^{2k}(u_2^2-u_1^2)}{(2k)!(2k+2)!}.
\tag{20}
\]
The accepted canonical \(r_1'=R'>0\) makes this multiplier nonnegative. This recovers a known order-two sign using an additional source property, not thermal-state positivity alone. At higher order the derivative determinant can change sign, as the existing order-three source analysis already records; (20) supplies no all-order argument.

## 5. What can and cannot be gained just by relabeling states

A universal conversion of any real mixed overlap into an energy expectation is
\[
|\Xi_{I,J}\rangle=\frac{|0\rangle\widehat F_I+|1\rangle\widehat G_J}{\sqrt2},
\quad H_{\mathrm{anc}}=\varepsilon\sigma_x\otimes I,
\]
\[
\langle\Xi_{I,J}|H_{\mathrm{anc}}|\Xi_{I,J}\rangle
=\varepsilon\frac{D_{I,J}}{\sqrt{\det M^f_I\det M^g_J}}.
\tag{21}
\]
This bounded two-level Hamiltonian has energies \(\pm\varepsilon\). It proves that an energy representation exists, but does not explain theta or supply a sign. Adding \(\varepsilon I\) makes it nonnegative only at the cost of a known offset that must be subtracted.

A more restrictive proposal fails already in the first two original states: there is no self-adjoint \(H\), with \(g_0,g_1\) in its domain, satisfying \(Hg_i=f_i\) for both \(i=0,1\). Self-adjointness would require
\[
\langle g_0,Hg_1\rangle=\langle Hg_0,g_1\rangle,
\quad\text{but these values are}\quad c_{-1}=0\quad\text{and}\quad c_1>0.
\tag{22}
\]
This excludes only the same-label assignment with these cross pairings. It does not exclude index-dependent preparations, different left/right observables, a non-diagonal density, a thermal response construction, or a different many-body Hamiltonian.

The third seed from Handoff10, \(H_\Phi^{\rm formal}=-\partial_u^2+\chi''/\chi\), still makes \(\chi\) a formal zero-energy state. Its Neumann endpoint is suggested by complete-source evenness. Its closed realization and response-state domains remain separate work. Such a ground-state construction applies to broad positive-source classes; its positivity alone does not turn the cross determinant into a positive energy. Its excitation spectrum has not been identified with \(\pi n^2\).

## 6. Control screen, classification and preferred next question

This is a representation study, not a proposed sufficient criterion. The following is an analytical premise screen against the existing controls, not a re-run of their certificates or a new numerical sign test.

| Control | What survives here; precise missing theta premise |
|---|---|
| Gaussian source and coefficient surrogates | Generic overlap/ancilla constructions survive. A Gaussian lacks the literal complete square-spectrum reconstruction (5)–(7); coefficient-only controls need not have any canonical source realization. No new sign is inferred for a surrogate. |
| MC01 one-mode thermal comparison | Has a positive filtered thermofield state and the response recurrence, but lacks the full spectrum/reflection. MC01's negative confluent third response defeats positivity-only pointwise transfer; it says nothing adverse about the complete integrated theta determinant. |
| Weighted-square and finite-prime square-source perturbations | Positive weighted thermal amplitudes and response observables survive. They fail unchanged unit weights and full normalized reflection; finitely matched endpoints do not restore all integrations by parts. |
| Euler-factor controls | Positive-source purification and generic overlap encodings survive, but the literal unchanged theta spectral reconstruction does not. No value of a new Mellin inequality has been computed. |
| Reflected super-Gaussian, smooth-shape/positive-primitive and source-compatible finite-profile or endpoint controls | Their applicable positivity/evenness/matched-data features do not specify the complete unit-weight theta heat trace. Some preserve reflection or selected source data, but not the full conjunction; their atomic variants also lack the smooth derivative-state setting. Generic purification cannot exclude them. |

No claim that a positive-time collision falsifies a time-zero fixed-order determinant is made. The reason to retain the complete thermal spectrum is to expose possible additional relations, not to declare that merely specifying theta proves the sign.

Among the handoff seeds, the preferred next starting point is the **geometric square-spectrum Hamiltonian together with the thermofield response preparation (13)**. They form one coherent route: the heat trace explains the primitive, the filter explains the source, and the response operators explain the actual cross-overlaps. The source-coordinate ground-state operator remains an alternative, with no selected spectral correspondence.

The concrete next conceptual question is whether the determinant observable (18), or an equivalent preparation retaining its sign and normalization, arises from one source-defined interaction, susceptibility, or variational comparison whose structure is shared across orders. An independently obtained lower bound or response relation would be useful; defining its positivity to be the desired determinant would only restate the target. We have not selected a new fixed physical Hamiltonian, nor excluded one. The present gain is the explicit state redefinition, its projection/norm accounting, and the precise distinction between thermal energy observables and a Hamiltonian that generates the state.

Chat history is kept in [Mellin-curvature chat-histories](../../chat-histories/README.md), registration 0004. No existing chat is moved or renumbered.
