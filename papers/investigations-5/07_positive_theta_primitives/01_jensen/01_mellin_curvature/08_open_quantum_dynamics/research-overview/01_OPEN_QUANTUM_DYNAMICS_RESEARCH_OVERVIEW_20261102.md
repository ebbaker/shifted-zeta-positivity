# Research overview: theta source states, Hamiltonians and realizations

3 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual recorded **gpt-6-astra / xhigh**, chat `01a19f55-b2e6-75f0-a465-ad11ad5d5488`, turn `01a19fd4-54b3-7162-8b66-7971f8b92164`; same brainstorm history **0001**.

**Author-requested revision of the 2 November E00 overview.** The original E00 design has already produced E01–E03 and the continuation manuscript. This overview now specifies the upstream clock, Hamiltonian and environment questions authorized on 3 November; it does not treat the original tasks as unexecuted. Original request revisions, returns, reviews and their historical input hashes remain unchanged. The [sole MC08 progress register](../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md) owns readiness and current task disposition.

**Scope separation, 3 November 2026:** the author has created a separate [source-overlap kernel investigation](../../09_source_overlap_kernels/README.md), initially with a draft overview only. The present folder continues the Hamiltonian, clock, environment and energy interpretation. The earlier source-kernel discussion notes retain their original paths as provenance. This navigation update is by gpt-6.1-sol / ultra and selects no new model.

**Author-requested source-first continuation, 3 November 2026:** [Handoff10](../research-progress/handoffs/10_NATURAL_HAMILTONIAN_BRAINSTORM_CONTINUATION_20261103.md) now prepares natural-Hamiltonian brainstorming from f_i,g_j and the source's statistical-mechanics generating function. The old v clock and two engineered baths are not compulsory starting assumptions. The transfer/clock/full-model formulas below retain their earlier evidence as one construction; they do not select the natural source Hamiltonian. Actual continuation preparation gpt-6.1-sol / ultra.

## Research purpose and fixed mathematical observation

Investigate a natural Hamiltonian for the original theta-derived source states, or an energy-space operator with a faithful preparation/observable correspondence to those states. The current author preference starts with the primitive as an energy generating function and permits a circle or another geometry. Handoff10 supplies unselected source-spectrum, source-coordinate and joint-state starting points; a physical time, geometry or operator has not been chosen. The earlier clock/full-environment investigation below records one realization of the coefficient transfer. The [new discussion](../brainstorm/notes/03_CLOCK_FREEDOM_AND_EXPLICIT_ENVIRONMENT_20261102.md) supplied the finite quadratic-clock candidate with same-assistant checking. The later [E06 assessment](../brainstorm/reviews/01_MC08_E06_QUADRATIC_CLOCK_ASSESSMENT_20261103.md) accepts its stated finite claims with shared-premise different-model internal checking; [Derivation05](../brainstorm/notes/05_MC08_E06_QUADRATIC_CLOCK_DERIVATIONS_20261103.md) supplies the details. General physical endpoint-channel equality and infinite-generator claims remain unexecuted. This navigation update is by gpt-6.1-sol / ultra, 3 November 2026; readiness belongs only to the sole register.

Retain the complete time-zero source and its coefficients:
\[
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,\quad
F(w)=\sum_{n\ge0}c_nw^n,\quad K_v=F(vS)/F(v),\quad K_0=I.
\]
Here S is the backward shift on coefficient sites in ell2(N0), and c_n=0 for negative indices. For increasing occupations I,J of length r,
\[
A_v(I,J)=\langle I|\Gamma(K_v)|J\rangle
=\frac{v^{\sum J-\sum I}}{F(v)^r}\det[c_{j_b-i_a}].
\]
This signed amplitude, including phase, occupation order and the full scalar F(v), remains the mathematical observation. At v=0 use K_0=I. All-minor nonnegativity is the inherited RH-equivalent destination, not a result of an enlarged positive Hilbert space. The unchanged quantitative pilot is eta_k=D_(3,k-1)D_(3,k+1)/D_(3,k)^2<=k/(k+3), k>=1, or its sufficient complete Mellin-curvature comparison. Reparameterizing v cannot change eta_k.

The exact continuously monitored loss record is a feature of the existing architecture, not automatically a required observation in every replacement model. Partial trace, final environment-vacuum selection and continuous no-count conditioning must be specified separately. A probability |A|^2 cannot replace A. The existing coherent reference, p_J and q_0=(1+p_J)/2 remain the readout baseline; a changed measurement must recover the signed amplitude with its own justified normalization.

## Work sequence and model routing

| Task | Type / recommended model and reason | Dependency and deliverable |
| --- | --- | --- |
| MC08-B03 | B — Astra: natural Hamiltonian and state/energy correspondence remain conceptual | Current source-first discussion prepared in [Handoff10](../research-progress/handoffs/10_NATURAL_HAMILTONIAN_BRAINSTORM_CONTINUATION_20261103.md); no candidate selected |
| MC08-E06 | E — Sol: specified clock/dilation verification | Completed finite-scope assessment linked above; retained as earlier realization evidence |
| MC08-B04 | B — Astra: the earlier two-bath observation/model choice | Preserved optional r0; it does not restrict the source-first B03 discussion |
| MC08-E07 | E — Sol: execute the route once B04 fixes it | Reserved follow-through only; not an issued research contract until its observable, topology, estimates and stop test are frozen |
| MC08-E04 | E — Sol: existing scoped B02 check | Separate historical verification option under Handoff05; not a prerequisite for E06 |

MC08-B03 remains the parent source-dependent energy-response investigation, now explicitly revised to source-first natural-Hamiltonian brainstorming. The earlier clock/full-model sequence remains available evidence rather than a prerequisite selecting the new operator; no signed mechanism is complete. These labels recommend manual routing; they neither change the author's model nor launch another chat or agent.

## 1. Clock freedom: scaling versus quadratic startup

For a nondecreasing C1 clock v=f(t), f(0)=0 and f(t)<=1/25,
\[
\widetilde G(t)=f'(t)G(f(t)),\quad
\widetilde H(t)=f'(t)H(f(t)),\quad
\widetilde R(t)=f'(t)R(f(t)),\quad
\widetilde L_\mu(t)=\sqrt{f'(t)}L_\mu(f(t)).
\]
The same scaling holds for the lifted Fock Hamiltonian and full Lindblad generator; event-time densities acquire their Jacobians. A constant rescaling f(t)=a t changes energies and rates, while preserving the path, corresponding amplitudes, and relative coherent/loss strengths.

The selected nonlinear case for assessment is **f(t)=a t^2, a>0**, on 0<=t<=1/sqrt(25a). It gives
\[
\|K_{at^2}\psi\|^2=1-at^2\langle\psi,R(0)\psi\rangle+O(t^4).
\]
This removes the startup contradiction with quadratic leakage from a regular total Hamiltonian and an initial product vacuum. It is not a regular clock diffeomorphism at t=0. The earlier obstruction continues to apply to clocks with f'(0)>0 in its original class. At later times with f'>0, repeatedly projecting a fixed bath to vacuum still creates a new product-state quadratic leakage law; hence the entire continuous no-count instrument is not recovered merely by quadratic startup.

E06 checked these statements on the fixed interval; its finite-scope assessment is linked above. It does not optimize clocks, enlarge the activity range or use a coordinate change as a signed estimate.

## 2. Three Hamiltonians with different roles

| Operator | Hilbert space and role | Required distinction |
| --- | --- | --- |
| L_+=diag(pi m^2), m>=1, and dGamma(L_+) | Positive circle modes and their energy-mode Fock space | Supplies the theta heat trace and filtered source; no identification with coefficient-site creators |
| tilde H_N(t)=2at H_N(at^2), and dGamma(tilde H_N) | Coefficient-site system space and its Fock lift | Coherent part of the prescribed reduced no-count generator; zero at startup |
| h_tot,N(t)=i U_N'(t)U_N(t)^dagger, and dGamma(h_tot,N) | Full system plus environment one-particle space and its Fock lift | Generates the proposed exact joint unitary; its startup exchange need not vanish |

The total Hamiltonian is not obtained just by multiplying the old reduced H by 2at. It includes interactions with explicit environment degrees of freedom. A decomposition into system energy, reservoir energy and interaction, choice of frame, drive/work terms and observable to call energy must be stated by B04. The candidate is driven/time dependent; autonomous energy conservation, a thermal reservoir, and a pi m^2 spectral interpretation are not assumed. Scalar or frame changes must be tracked through the calibrated signed observation.

## 3. Explicit candidate full space and unitary

At cutoff N let m=N+1, h_S,N=C^m and h_E,N=C^m. The one-particle space is a **direct sum** h_S,N plus h_E,N; the many-body space is F_-(h_S,N plus h_E,N), of dimension 2^(2m). An ordered Fock factorization gives the system/environment tensor product with fermion parity conventions fixed. The environment starts in vacuum.

Set C_N(t)=K_(at^2,N), retaining the complete scalar F, and
\[
D_N=(I-C_N^\dagger C_N)^{1/2},\quad
E_N=(I-C_N C_N^\dagger)^{1/2},\quad
U_N=\begin{pmatrix}C_N&-E_N\\D_N&C_N^\dagger\end{pmatrix}.
\]
The standard defect identity verifies unitarity and U_N(0)=I. The proposed exact vacuum block is
\[
\langle\Omega_E|\Gamma(U_N(t))|\Omega_E\rangle=\Gamma(C_N(t)).
\]
The full unconditioned channel is explicitly the partial trace of Gamma(U_N)(rho tensor vacuum)Gamma(U_N)^dagger. Equality of this channel with the old MC08 endpoint channel, on a stated observable algebra, is not inferred just from equality of vacuum blocks. Matching the continuous record is a still stronger condition.

The finite-N regularity calculation uses R_N(0)>0:
\[
D_N(t)=\sqrt a\,t\sqrt{R_N(0)}+O(t^3),\quad
E_N(t)=\sqrt a\,t\sqrt{R_N(0)}+O(t^3),
\]
\[
h_{\rm tot,N}(0)=i\sqrt a
\begin{pmatrix}0&-\sqrt{R_N(0)}\\\sqrt{R_N(0)}&0\end{pmatrix}.
\]
Strictly positive defects at positive t follow by integrating K_v^dagger R_N(v)K_v. E06 audits smoothness and boundedness on the mapped compact interval for each fixed N. These are Note03 deductions awaiting separate checking, not already accepted by E03.

For a fixed bath, the system block between t1 and t2 is C_2 C_1^dagger+E_2 E_1, generally not C_2 C_1^(-1). The scalar cosine example in Note03 gives an exact distinction. Final emptiness allows prior departures and returns; the existing fresh-bin no-count record does not.

## 4. Existing stream and inheritance boundary

The reviewed E02 architecture has m new vacuum fermion modes per bin. Its exact bin unitary is exp[-i(h H_F,N+sqrt(h) W_N)] with explicit Hermitian exchange W_N. A finite sequence is a full known model. The target reduced channel, count instrument and phase-calibrated no-count operator are recovered in its fixed-N h->0 limit. This consumes unbounded temporal bath resources and h^(-1/2) couplings. E02 does not construct a single regular finite reservoir or prove convergence of total unitaries to a common infinite-bath Hamiltonian.

E01/E02 remain accepted at their stated scope by E03; B02's fixed-cone result remains proof-author checked with separate E04 pending. A revised clock reparameterizes the old reduced instrument, but a new full bath does not inherit its measurement history by default. In particular no source dependence, cutoff theorem, phase convention, locality assertion or energy law may be imported solely because both constructions contain K_v.

## 5. Infinite Hilbert space is a separate analytical gate

The natural endpoint candidate is h_S=ell2(N0), h_E another copy, and F_-(h_S plus h_E). The bounded contraction K_v supplies defect operators and a unitary block completion at each endpoint. This alone does not supply a regular total generator or its full-Fock domain.

The following must be addressed by B04's chosen route before E07 is issued:

- Whether finite U_N approximate that infinite U in the needed topology. Defect square roots generally do not restrict exactly across cutoffs, even though the backward-shift K_N do.
- Which differentiability and domain statements are needed for h_tot and dGamma(h_tot), and which particle caps or finite-energy assumptions make them meaningful.
- How the gapless infinite R and the shrinking finite Dirichlet gap affect square-root derivatives. A finite-N positive-gap proof does not pass uniformly by notation.
- What convergence of partial traces, conditioned amplitudes and the signed observation is required, separately from a full joint-unitary or generator limit.
- Whether fixed-N suffices for a genuinely bounded pilot and, if so, how that scope is kept distinct from all finite minors and the infinite-space claim.

The original E02 trace-class system extension concerns its selected stream instrument. It is not automatically the extension theorem for this fixed-bath completion.

## 6. Controls, completion and documentation

This phase is a representation/design assessment, not a new positivity criterion. The Gaussian and F_*=1+w+2w^2 controls both admit the generic completion. The polynomial's known negative minor survives; it fails the unchanged theta source premise rather than unitarity or clock regularization. Weighted-square/Euler modifications fail the canonical spectral weights/reconstruction, and reflected shape controls need not supply the complete square-spectrum source. No uncomputed inequality is assigned to them. Any later energy-response premise must specify what additional theta information it uses and its signed consumer.

E06 returns an explicit claim-by-claim acceptance, correction or scoped gap after one analytical pass and at most one local correction. B04 compares only the existing stream and the fixed-bath completion at this stage, chooses the observation and energy specification, and freezes one finite/infinite-space route for E07 or records why no route is ready. A new source-energy model requiring a different representation is a named conceptual return, not a silent alteration of this contract.

Save new discussion notes and assessments under brainstorm/notes and brainstorm/reviews, computations only under numerics if later authorized by a concrete consumer, and this chat's public history under brainstorm/chat-histories. Preserve frozen earlier returns and manuscript sources. No manuscript snapshot, broad numerical scan or simulation is part of this plan.

Read with [the result index](../../../../../../../result-summaries/README.md), especially [theta identities and bookkeeping](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [the avoid index](../../../../../../../avoid/README.md), particularly [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
