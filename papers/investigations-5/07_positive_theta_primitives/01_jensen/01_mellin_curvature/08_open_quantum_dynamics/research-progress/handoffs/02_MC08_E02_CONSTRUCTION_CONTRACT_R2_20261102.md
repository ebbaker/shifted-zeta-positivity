# MC08-E02 construction request r2 — frozen

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; issuing model **gpt-6-astra (Codex), actual reasoning effort max**, chat `01a19dd8-047f-7212-b770-1a8bc3800761`, turn `01a19dd8-06d1-7ed3-abbe-60a30de2c163`.

| Field | Frozen request |
| --- | --- |
| ID / parent / revision | **MC08-E02 / MC08-B01 / r2** |
| Type and recommendation | **E — execution; Sol.** Architecture, equations, readout and proof route are fixed; the remaining work is bounded analytical construction and verification. |
| Readiness | Issued and Ready after B01; **not started by issuance**. E01's limited checking status carries forward. |
| Live authority | [Sole MC08 register](../01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md) |
| Main output | `notes/03_FERMIONIC_LINDBLAD_REALIZATION_YYYYMMDD.md`, a frozen return with actual model/effort, input versions, proofs, failed cases and scope |
| Next dependency | E03 separately assesses frozen E01/E02 returns; B02 waits for that assessment or a precise scoped obstruction. |

This request is immutable once issued. A later correction is an explicit new revision with a reason and crosswalk; do not overwrite r2 or its failed evidence. The [architecture note](../../notes/02_OPEN_SYSTEM_ARCHITECTURE_DECISION_20261102.md) owns the B01 reasoning. This packet owns E02's construction and acceptance requirements.

## Revision r2 before execution

This revision supersedes [the preserved r1 request](02_MC08_E02_CONSTRUCTION_CONTRACT_R1_20261102.md), SHA256 `e82659d1897c6e90c9d57a5745e216944d3d535b175b6b99551320be43617282`, solely to specify the count-record convergence topology in part B. The r1 wording required count-instrument convergence but did not fix the comparison between discrete bin records and continuous timestamps. Atomic grid times cannot converge in total variation to a continuous event-time density on the full timestamp space. **Compare both instruments after recording counts in the same time bins**, and then infer convergence for continuous test functions of event times as the bins shrink. All source, architecture, readout, finite-case and work-limit choices are unchanged. E02 had not started when this clarification was issued. B01 Note02 is retained at its original hash; current execution uses r2.

## 1. Prerequisite versions

| Input | SHA256 |
| --- | --- |
| [E01 return](../../notes/01_NO_JUMP_ADMISSIBILITY_AUDIT_20261102.md) | `21929f0b5050f699b856aaa899dd1631564aecb2a700a89fa994cbdeeb1fabf5` |
| [E01 exact record](../../numerics/MC08_E01_EXACT_BOUNDS_20261102.json) | `fba2ae5435515676f801c10b7bfe7dd62e46850d2d066fd5571048f69152fb2f` |
| [E01 limited check](../../reviews/01_MC08_E01_BOUNDED_CHECK_20261102.md) | `94f920dd1bbee9b93668348c6770f54534f1c0851b9b707db92380dfad9a4161` |
| [B01 decision r1](../../notes/02_OPEN_SYSTEM_ARCHITECTURE_DECISION_20261102.md) | `e20fa974e053b609c49c477a6f1e587b27d5e1969fe3960468eb23d0e47b85c2` |

Verify these versions and report any change before relying on it. Read root AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md and the [E01 handoff](01_MC08_E01_CONTINUATION_20261102.md). Reuse E01's source/tail proof; this task does not rerun or optimize it.

## 2. Fixed mathematical and physical contract

**Question:** Does the selected count instrument give a common fermionic realization with the exact unchanged Gamma(K_v) no-jump branch and a parity-compatible signed readout, and what precise finite/infinite and microscopic-limit theorem follows from the specified construction?

The only source is the complete canonical time-zero theta source and its original c_n and F. Domain: **0 <= a <= b <= 1/25**. H_N=span{|0>,...,|N>} has m=N+1 modes. S_N is the backward shift. Use K_(v,N)=F(v S_N)/F(v), G_N=G restricted to H_N, R_N=-(G_N+G_N†), H_N^(1)=i(G_N-G_N†)/2, B_N=sqrt(R_N), and

\[
L_{\mu,N}=\sum_j(B_N)_{\mu j}a_j,\quad
H_{\mathcal F,N}=\sum_{i,j}(H_N^{(1)})_{ij}a_i^\dagger a_j.
\]

Normal ordering fixes vacuum energy zero. Ordered occupation states use increasing creation indices. The full scalar gamma(v)=F'(v)/F(v) in G_N is not truncated with N. Do not add attenuation or phase offsets. The same dynamics works for all r,I,J. Couplings may be dense over the N+1 abstract modes; no spatial locality, finite range or uniform locality of sqrt(R) is required or may be inferred.

The Lindblad convention is L rho L† - {L†L,rho}/2. E01's sqrt(R) jump within the one-particle space is an admissibility input, **not** the full channel being lifted here. Prosen's factor-two convention must be converted explicitly if cited.

The selected measurement is ideal unit-efficiency loss counting, with count times retained and the reservoir-channel identity discarded. The unobserved-label jump is

\[
\mathcal J_{R_N}\rho=\sum_{j,k=0}^N(R_N)_{kj}a_j\rho a_k^\dagger.
\]

No coherent sum of distinct detector labels, diffusive unraveling, inefficient no-click postselection or arbitrary Kraus rephasing is allowed. Fermion loss changes system number/parity; even exchange conserves total number/parity. The coherent flag is a neutral qubit; both reference and signal contain the same r fermions.

## 3. Required analytical return

### A. Finite-mode dynamics and the entire count instrument

For every finite N, prove norm-continuous coefficients, existence of the unique two-parameter CPTP propagator, and CP divisibility by a bounded jump expansion or equivalent finite-dimensional proof. Do not claim a homogeneous semigroup. Verify

\[
\sum_\mu L_{\mu,N}^\dagger L_{\mu,N}=d\Gamma(R_N),\qquad
G_{{\rm nj},N}=d\Gamma(G_N),\qquad
M_{0,N}(b,a)=\Gamma(K_{b,N}K_{a,N}^{-1}).
\]

Give the CP maps for a record of k ordered count times by inserting J_R between no-jump maps and integrating as appropriate. Sum over all records to recover the channel. Each loss lowers particle number by one; for inputs with at most r particles the jump expansion stops after r jumps. Preserve off-diagonal density operators as well as populations. Trace preservation and phase conventions need proofs, not just covariance equations.

### B. One Hermitian collision construction and its error

Use exactly B01 equations (3)-(4): m fresh vacuum fermion modes per bin; environment-first Fock ordering; Hermitian exchange

\[
W_N=\sum_\mu(b_\mu^\dagger\Pi_E\otimes L_{\mu,N}
                  +\Pi_Eb_\mu\otimes L_{\mu,N}^\dagger),\quad
U_{N,h}(v)=e^{-i(h I_E\otimes H_{\mathcal F,N}(v)+\sqrt h W_N(v))}.
\]

Measure total outgoing occupation, erase channel identity and discard the bin. Show the vacuum block is I+h dGamma(G_N)+O_N(h^(3/2)), the one-emission blocks are -i sqrt(h)L_mu+O_N(h), and multi-emission outcomes have no first-order probability contribution. Derive the first-order reduced map I+h L_N+o_N(h).

Obtain a finite-N local remainder and an accumulated trace-norm/map-norm error tending to zero on the fixed interval. A bound of the form C_N sqrt(delta)+C'_N omega_N(delta), where delta is the largest bin width and omega_N is a stated coefficient modulus of continuity, suffices; better order is optional. Constants may depend on N. Prove the corresponding no-count product converges to the **exact** Gamma(V_N). For count records fix a partition pi and compare the collision outcome n=(n_1,...,n_M) with the continuous Lindblad count instrument integrated over exactly n_l jumps in each matching bin. Both have the same discrete record space, with total count at most N+1 (or r on a particle cap). Require an induced trace-class-to-direct-sum-trace-class bound

\[
\sup_{\|\rho\|_1\le1}\sum_{\mathbf n}
\|\mathcal I^{\pi}_{\mathrm{coll},\mathbf n}(\rho)
 -\mathcal I^{\pi}_{\mathrm{Lind},\mathbf n}(\rho)\|_1
 \le C_N\sqrt\delta+C'_N\omega_N(\delta)\longrightarrow0.
\]

Define the modulus and constants actually used. Sum/integrate over unobserved channel labels. One-bin Kraus expansions and contractivity of the record-valued CPTP maps provide the fixed telescoping route. This is stronger than averaged-channel convergence and includes the zero-count record. On each finite jump sector, derive the resulting convergence against bounded continuous functions of ordered event times, using the shrinking bin diameters. **Do not claim total-variation convergence between exact continuous timestamps and point masses placed on grid times.** Repeat the argument with the controlled Hamiltonian/loss needed for part C, or give a direct finite-dimensional extension.

An exact finite-h identity is not requested. Identify the effective coupling h^(-1/2), unlimited temporal bath size as delta tends to zero, and absence of a fixed bounded closed-reservoir realization under B01's short-time hypotheses. Do not invoke a Markov approximation as an already-paid theorem for a particular laboratory reservoir. This task proves one prescribed ideal collision limit, not hardware feasibility or an unbounded-field dilation theorem.

### C. The signed observation, including its success factors

For ordered I,J of length r, prepare (|0>|I>+|1>|J>)/sqrt(2); control H_F,N and every L_mu,N by Q_1. The reference arm is identity with the same vacuum phase. Verify the no-count block is Q_0 tensor I + Q_1 tensor Gamma(K_(v,N)), and

\[
p_J=\|\Gamma(K_{v,N})|J\rangle\|^2
 =\det[(K_{v,N}^\dagger K_{v,N})_{J,J}],\quad
q_0=(1+p_J)/2,\quad
\operatorname{Re}A_v=q_0\mathbb E[X\mid0]=P(0,+_X)-P(0,-_X).
\]

Track the imaginary-part/Y convention, all basis/permutation phases and the positive factor v^(sum J-sum I)/F(v)^r. Explain same-number state preparation and the extra controlled-dynamics resource; an arbitrary channel black box does not determine a controlled Kraus phase. Check that the no-count bath record does not mark the reference arm. Include vacuum r=0, v=0, and the signal probability bound p_J >= (12/13)^(2r), with no uniform-in-r success floor or efficient-estimation assertion.

### D. Exact compatibility, mode limit and particle domain

The fixed route is B01 equation (10), **not** compression of square roots. For M>=N show that the generator on operators supported in F(H_N) agrees with the N-mode generator: G_M restricts to G_N; annihilation above N vanishes; the R_M block is R_N. Infer exact restriction of the no-jump maps, channel-discarded count instruments and full propagators. Do not identify individual channel-resolved jumps or finite microscopic collision unitaries across cutoffs.

Extend the consistent contractions from the dense union of finite-mode trace classes to the vacuum Fock representation over ell^2. Prove complete positivity, trace preservation, two-parameter composition and trace-norm continuity; these cannot be replaced by formal use of an unbounded Lindblad expression. On the subspace of trace class supported in at most r particles, derive

\[
\|\mathcal L(v)\|_{1\to1}\le2r\|G(v)\|+r\|R(v)\|\le8rA_*.
\]

Use these spaces as a common invariant differentiability domain, without claiming it is the maximal domain or a graph core. Identify the infinite jump map through consistent finite-mode limits (or the equivalent bounded annihilation row on a particle cap). Explain its continuity in v without a spectral gap for sqrt(R). The physical density operators commute with total fermion parity; a mathematical CPTP extension to other trace-class operators is not a license to prepare forbidden parity superpositions.

Prove the statewise, uniform-in-time cutoff estimate

\[
\|\mathcal T(b,a)\rho-\mathcal T_N(b,a)(\Pi_N\rho\Pi_N)\|_1
 \le\|\rho-\Pi_N\rho\Pi_N\|_1\to0
\]

with unnormalized compressed input and natural embedding. Give the analogous particle-cap approximation. Retain Gamma(V) as a bounded no-jump contraction on full Fock space; do not assume a bounded full-Fock derivative or inverse. No operator-norm convergence uniform over all states, infinite-density state representation, or interchange of collision and mode limits is requested.

**Scope gate:** A–D are required for a positive E02 completion at this contract's scope. If a specified step fails after the bounded diagnosis below, return the exact gap and the proved finite scope; do not silently promote the full-Fock or reservoir claim. Such a failed return can complete the execution task, but is not a positive realization acceptance.

## 4. Finite checks and control cases

These are algebra/convention checks supporting the general proof, not samples proving all N or r. Do them by hand or in one small exact script; no theta quadrature is needed.

| Case | Required check |
| --- | --- |
| N=0; r=0,1 | Vacuum fixed; one occupied mode has no-jump amplitude c_0/F(v) and loss rate 2 gamma(v). Keep the full scalar F. |
| N=1; r=1,2 | Nontrivial hopping/loss interference; determinant of K_N is (c_0/F)^2; verify a_0|0,1>=|1> and a_1|0,1>=-|0>, including off-diagonal density terms. |
| N=2; r=2 | I=(0,1), J=(1,2) gives v^2(c_1^2-c_0c_2)/F(v)^2; check both the flag probabilities and cutoff compatibility. No new theta sign is inferred. |
| Gaussian F=c_0 exp(a w), a>0 | Constant generator and known directed-semigroup normalization; arbitrary positive a remains symbolic. |
| Polynomial F_*=1+w+2w^2 | Reuse E01's dissipativity proof on 0<=v<=1/25, and retain A=-v^2/F_*(v)^2<0 in the **same** instrument/readout. This is mandatory negative control. |

Screen Euler-factor, weighted-square, finite-prime, reflected and positive-primitive controls by the premise table in B01 and the [standing control inventory](../../../../../../../../result-summaries/12_collision_controls_and_screening.md). Do not import theta's paid constants to modified sources or infer that failure of exact reconstruction means failure of generic local dissipativity. No new control scan or collision computation is issued.

## 5. Work limits, permitted choices and stopping rule

Perform **one analytical construction** using A–D. One bounded correction pass for a normalization, ordering, continuity or remainder estimate is allowed. Routine choices include a convenient particle-cap notation, a conservative remainder constant, and direct algebra versus a small exact check of the finite cases above.

No parameter optimization, finite-size scan, trajectory Monte Carlo, theta integration, minor survey, precision escalation, extra reservoir family or signed-comparison search is authorized by this request. There is no numerical resource budget. Do not rerun E01's source proof unless a concrete inconsistency is found.

Return to **B01**, with a dated revision proposal, if completion requires changing the source, normalization, activity parameter, jump instrument, parity resources, physical architecture or target. If the fixed compatibility or collision route has an unresolved mathematical premise after the correction pass, preserve that gap and return the achieved scope instead of improvising an alternative. A sign mechanism belongs to **B02**, after review; it is not an extension of E02.

## 6. Outputs and acceptance

Write the return in `notes/03_FERMIONIC_LINDBLAD_REALIZATION_YYYYMMDD.md`. Any small exact support belongs in `numerics/`, with provenance and a record; unnecessary code is not a deliverable. Update only E02's entry and dated return in the sole register, local navigation/milestone history, and this chat's registered history using the repository tool. Preserve E01, B01, this r2 request, existing reviews and unrelated work. Reference updates follow the shared Jensen lock; no third-party PDFs enter Git.

The return must state actual model/effort and dates, input hashes, which of A–D were proved, the fixed cases, explicit errors/continuity bounds, finite versus infinite scope, unpaid obligations and deviations. A positive completion requires the full proofs, with the negative control and signed readout intact. A failed completion needs a precise failed step and its implication for the next decision. Either disposition is frozen for E03; this execution is not its own separate assessment.

Use the [result index](../../../../../../../../result-summaries/README.md) and [theta assessment cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), the [avoid index](../../../../../../../../avoid/README.md), especially [generic re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [control discipline](../../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), and [scoped exclusions](../../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). No construction or finite check is evidence for a new theta sign bound.

**After the frozen return: [E] MC08-E03 — Sol, separate checker.** Inspect the exact versions, domains, phase/parity choices, collision remainders, cutoff compatibility and claims. No automatic dispatch is part of r2.
