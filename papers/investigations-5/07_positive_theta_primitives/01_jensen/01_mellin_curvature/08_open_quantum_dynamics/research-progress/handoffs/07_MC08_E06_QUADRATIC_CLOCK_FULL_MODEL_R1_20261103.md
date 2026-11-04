# MC08-E06 r1: quadratic clock and explicit finite full-model verification

3 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual recorded **gpt-6-astra / xhigh**, chat `01a19f55-b2e6-75f0-a465-ad11ad5d5488`, turn `01a19fd4-54b3-7162-8b66-7971f8b92164`; same brainstorm history **0001**.

**Type E — execution; recommended Sol.** The algebraic model, proof route and evidence standard are fixed. This is a separately executed internal analytical check of Astra's Note03, not a specialist review or an instruction to switch models automatically. Parent MC08-B03; next conceptual consumer MC08-B04. Live readiness belongs only to the [sole MC08 register](../01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md).

| Next work | Type / recommended model | Dependency | Deliverable |
| --- | --- | --- | --- |
| MC08-E06 r1, default | E / Sol: fixed formulas and six checks below | Ready on the frozen source inputs | Accept/correct/precise gap for each claim and an inheritance table |
| MC08-B04 | B / Astra: observation and full-model/energy choice | Consume E06 disposition | One architecture specification and a bounded next E request, or a reasoned decision that more conceptual work is required |

## Fixed inputs and question

Can the Note03 quadratic-clock finite completion supply the claimed exact endpoint amplitudes and a regular driven total Hamiltonian, at every fixed cutoff, while accurately separating the reduced instrument, partial trace, startup obstruction and infinite-domain limitations?

| Frozen input | SHA256 |
| --- | --- |
| [03_CLOCK_FREEDOM_AND_EXPLICIT_ENVIRONMENT_20261102.md](../../brainstorm/notes/03_CLOCK_FREEDOM_AND_EXPLICIT_ENVIRONMENT_20261102.md) | `d9b674e0504033aeb1b5f471624ce1a66148154ba598a22869de283240b9010a` |
| [01_NO_JUMP_ADMISSIBILITY_AUDIT_20261102.md](../../notes/01_NO_JUMP_ADMISSIBILITY_AUDIT_20261102.md) | `21929f0b5050f699b856aaa899dd1631564aecb2a700a89fa994cbdeeb1fabf5` |
| [02_OPEN_SYSTEM_ARCHITECTURE_DECISION_20261102.md](../../notes/02_OPEN_SYSTEM_ARCHITECTURE_DECISION_20261102.md) | `e20fa974e053b609c49c477a6f1e587b27d5e1969fe3960468eb23d0e47b85c2` |
| [03_FERMIONIC_LINDBLAD_REALIZATION_20261102.md](../../notes/03_FERMIONIC_LINDBLAD_REALIZATION_20261102.md) | `23c2852f9b0e0c2c97790d27dc29a636c656e175e71ad1f880b7fd4dc73c7a0d` |
| [02_OPEN_QUANTUM_DYNAMICS_ASSESSMENT_20261102.md](../../reviews/02_OPEN_QUANTUM_DYNAMICS_ASSESSMENT_20261102.md) | `cea5f11762619f3001cfc7f2e6f64d3db9a779c87171179c15fea45fc9e80f4b` |

The revised [overview](../../research-overview/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_OVERVIEW_20261102.md) is navigation, not a new proved premise. This r1 packet is frozen once issued. If an input differs, identify the change and its effect before relying on it; do not silently rewrite frozen notes. The prior overview's historical hashes in E01 remain records of its old revision.

## Equations and domain

Keep complete F, coefficient-site S_N, K_(v,N)=F(vS_N)/F(v), the established local interval 0<=v<=1/25, G_N, R_N and H_N. Keep arbitrary fixed N>=0 and all its particle sectors, a symbolic a>0, v=a t^2, and 0<=t<=1/sqrt(25a). Define C=K_(at^2,N), D=sqrt(I-C^dagger C), E=sqrt(I-CC^dagger), U=[[C,-E],[D,C^dagger]], and h_tot=i U' U^dagger. Specify the ordered factorization of F_-(C^m_S plus C^m_E), m=N+1, with environment vacuum and normal-ordered Gamma(U) vacuum phase +1. The observable is the complete signed vacuum-branch amplitude, not its square.

## Six bounded analytical obligations

1. **Clock transformation.** Derive G_t=f'G, H_t=f'H, R_t=f'R and L_t=sqrt(f')L for nondecreasing C1 f, including f'=0 and count-time Jacobians. Specialize to at and at^2. Check endpoint/minor invariance and the mapped local interval. Establish exactly which startup loss argument depends on f'(0)>0; retain the later-time, repeatedly reset vacuum limitation. Do not infer a bound from slowing the clock.
2. **Unitary and Fock construction.** Verify both unitary products using the defect intertwiner; check U(0)=I, the total one-particle direct sum and its Fock factorization, total number/parity, and the environment-vacuum block Gamma(C) on every finite particle sector. Recheck the standard source attribution to Robinson Theorems 0–2; the time regularity argument is local work, not an imported theorem.
3. **Regular total Hamiltonian.** At each fixed N, check strict positivity of R_N(0), both defect expansions, the startup h_tot, and positive-time defects via the integral of K^dagger R K. Prove the differentiability/continuity needed for a bounded h_tot on the mapped compact interval, or identify a precise failed step. Confirm dGamma(h_tot) generates Gamma(U) in finite dimension. Distinguish this total exchange energy from the vanishing initial reduced coherent H_t. Do not assume uniformity in N.
4. **Partial trace, conditioning and records.** Write the full finite reduced channel as a partial trace and identify the final vacuum branch with its success probability and phase. Check the intermediate block C_2 C_1^dagger+E_2 E_1 and compare it with C_2 C_1^(-1); use the scalar cosine example with angles in [0,pi/2). Do not infer equality of full endpoint channels from equality of a single Kraus block, and do not assume equality of complete count instruments. Determining general endpoint-channel equality is outside this packet; record the exact equation/algebra that a later selected comparison would need, including physical parity versus arbitrary odd operators.
5. **Finite/infinite and energy inheritance.** Produce a table of existing E02/E03 statements that reparameterize, statements requiring a new proof for the fixed bath, and statements not claimed. Identify the finite-gap dependence, noncompatibility of square-root compressions, and full-Fock generator/domain issues. Do not attempt the infinite generator or joint collision/cutoff limit. Identify which of source energy, reduced coherent generator and total driven energy each formula concerns.
6. **Controls and conventions.** Perform only exact symbolic checks N=0 and N=1, including vacuum, one-particle states, the occupied two-particle state, and relevant coherences. Use the existing Gaussian and negative polynomial controls, retaining their known signs and distinct source premises. Check full F normalization, t=0 phases and the signed-reference reconstruction with both success factors. These checks support the general proof and do not replace it.

## Limits, allowed corrections and completion

One analytical pass, the fixed symbolic cases above, and at most one local correction followed by rechecking affected claims. No trajectory simulation, theta quadrature, spectrum scan, clock optimization, larger activity interval, general reservoir search, all-order sign test or infinite-space theorem. Routine notation/sign/normalization corrections may be reported in a separate correction note; do not edit the frozen author input. An architecture, source, observation, topology or proof-strategy change goes to MC08-B04 before further dependent work.

Save the assessment under brainstorm/reviews with the next unused number and actual execution date; save any needed correction derivation under brainstorm/notes. Record actual model/effort, checked input hashes, proof and source scopes, and an accept/correct/gap disposition for each obligation. Use explicit finite N and time domains. The result must let B04 decide what exact full model is actually available and which inherited claims it would retain. A precise failure completes this E task; no wider search is authorized by failure.

Update the sole register with the return and link; do not create another live ledger, edit earlier request revisions or execute E04 incidentally. This turn issued the contract only; E06 has not been performed.

Read with [the result index](../../../../../../../../result-summaries/README.md), especially [theta identities and bookkeeping](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and [collision controls](../../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [the avoid index](../../../../../../../../avoid/README.md), particularly [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [scoped exclusions](../../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [joint signed estimates](../../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## Pasteable next prompt

> Complete [E] MC08-E06 — Sol, request r1 in Handoff07. Verify the quadratic clock, finite system-plus-environment unitary, regular total Hamiltonian, exact endpoint Fock amplitudes, and the distinction from the old count instrument. Follow all six fixed obligations and the one-pass/one-correction limit. Preserve the complete theta source, all phase/normalization factors and finite-versus-infinite qualifications. Return accept/correct/precise gap and an inheritance table for B04; do not select a new architecture or execute an infinite-domain or numerical campaign. Preserve this chat's unique history if continuing here; a genuinely new chat gets its own appropriate registration.
