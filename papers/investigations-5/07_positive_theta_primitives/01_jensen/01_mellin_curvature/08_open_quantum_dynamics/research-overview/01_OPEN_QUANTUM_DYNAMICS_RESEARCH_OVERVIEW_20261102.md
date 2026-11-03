# Research overview for open quantum dynamics of the theta transfer

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**, verified from this chat's turn metadata. **MC08-E00** is planning/documentation only; the research tasks below have not been executed.

## Purpose and placement

This direction asks whether the exact theta fermionic transfer can be realized as a conditioned part of open quantum dynamics, and whether the structure of that realization yields useful information about its signed occupation amplitudes. It owns continuous parameter evolution, Lindblad and quantum-trajectory realizations, Hermitian environments, divisibility, and preservation of the original observable.

The folder is a sibling of [02 Fermionic correlators](../../02_fermionic_correlators/README.md). MC02 owns the established Slater/transfer representation and its reviewed obstruction; MC08 uses that baseline to study dynamics. [03 Connected Mellin response](../../03_connected_mellin_response/README.md) owns the continuous signed-response language, and [05 Schur and Toda structure](../../05_schur_toda_structure/README.md) owns the coefficient algebra. New dynamics must return to the same coefficients and amplitudes.

The [local progress file](../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md) is the sole live register for MC08. It contains the task contracts, dependencies and next prompt. Research readiness is recorded there, not duplicated here.

| Default next task | Type | Recommended model and reason | Deliverable |
| --- | --- | --- | --- |
| MC08-E01, exact no-jump admissibility audit | E | Sol: generator, positivity condition and analytical test are specified | A justified positive-v interval and exact construction conditions, or a scoped failed condition; explicit infinite-mode limits |
| Later design decision MC08-B01 | B | Astra: choose a common realization and its physical restrictions | One selected architecture and a frozen construction contract |

Recommendations do not change the author's selected model or effort and do not authorize dispatching agents or starting another chat.

## The physical distinction that fixes the problem

Tracing an environment out of unitary system-environment evolution produces a reduced density matrix. With a fixed initially uncorrelated environment, the resulting system map is completely positive and trace preserving (CPTP). It is generally non-unitary while preserving Hermiticity of the density matrix. A Lindblad equation is an additional dynamical structure: arbitrary reduced evolutions need not form a semigroup or admit completely positive intermediate propagators.

A non-Hermitian effective Hamiltonian naturally governs a **conditioned trajectory**, such as evolution with no detected environmental jump. Averaging all trajectories, including jumps, restores the density-matrix master equation. The exact amplitude K_v is therefore first proposed as a no-jump operator, not as the whole trace-preserving channel. The distinction follows the inspected Castin–Dalibard–Mølmer equations (1)–(8) and Section 2 in the [source record](../../../../references/12_OPEN_QUANTUM_DYNAMICS_SOURCES_20261102.md).

Fix the measurement instrument, ordered occupation basis and phase convention. Different Kraus decompositions or unravelings can describe the same channel while changing the selected conditional amplitude. Complete positivity alone cannot determine that amplitude's sign.

## Fixed mathematical baseline and desired output

Use the complete canonical theta source at source heat time zero:
\[
c_n=\frac{1}{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,\qquad
F(w)=\sum_{n\ge0}c_nw^n,\qquad c_n=0\quad(n<0).
\]
On ell^2(N_0), S|0>=0 and S|j>=|j-1>. For v>0,
\[
K_v=F(vS)/F(v),\qquad \|K_v\|\le1,\qquad K_0=I.
\]
For increasing finite lists I,J of length r,
\[
A_v(I,J)=\langle I|\Gamma(K_v)|J\rangle
=\frac{v^{\sum J-\sum I}}{F(v)^r}\det[c_{j_b-i_a}]. \tag{1}
\]
All-sector nonnegativity at one fixed positive v is the existing RH-equivalent formulation. This is stated once as the classification, not a new criterion or evidence for RH.

A concrete quantitative consumer is the fixed-order comparison
\[
\frac{A_{3,k-1}(v)A_{3,k+1}(v)}{A_{3,k}(v)^2}
\le\frac{k}{k+3},\qquad
A_{3,k}(v)=\langle0,1,2|\Gamma(K_v)|k,k+1,k+2\rangle,\quad k\ge1. \tag{2}
\]
State denominator positivity and the exact covered k range. This sufficient comparison is stronger than the bare next-determinant sign condition; changing it requires a named new target. A local positive-v realization is enough to represent all the coefficient signs, but no finite mode/particle cutoff replaces the full quantifiers in (1). Success at order four is a quantitative pilot within known finite-order positivity.

The parameter v is a jump-length activity. It is not source heat time, inverse temperature or the real Mellin tilt s. Any claim about the complete Mellin curvature requires an explicit bridge to the original M_3(s), with normalization, negative insertion and tails retained. A response in v alone is not that bridge.

## Existing evidence and unresolved claims

- The [MC02 return](../../02_fermionic_correlators/notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md) and [separate internal review](../../02_fermionic_correlators/reviews/01_MC02_E01_SEPARATE_REVIEW_20261101.md) accept the bounded transfer and the fixed-positive-metric Jordan obstruction at their stated scope. They prove no new Mellin comparison.
- The [basic explanation](../../brainstorm/03_FERMIONIC_TRANSFER_FROM_BASICS_20261102.md) fixes all finite-sector and positive-v quantifiers.
- The [continuous-v discussion](../../brainstorm/notes/01_CONTINUOUS_V_EVOLUTION_AND_HERMITIAN_SCOPE_20261102.md) derives the parameter generator, local logarithmic interpolation, large-v limitations and a generic unitary dilation. It has same-assistant checks only and remains an input to audit, not a separately reviewed Lindblad result.
- A fixed-time unitary dilation is generic for contractions. Separate endpoint dilations do not supply one common environment, continuous dynamics, locality or a sign theorem.

Read the [result index](../../../../../../../result-summaries/README.md), especially [theta physical assessments](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../../../avoid/README.md), especially [reformulations](../../../../../../../avoid/01_restating_the_target.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## First analytical test for a no-jump realization

Where F(vS) has a bounded inverse,
\[
G(v)=K'_vK_v^{-1}
=SF'(vS)F(vS)^{-1}-\frac{F'(v)}{F(v)}I. \tag{3}
\]
This inverse exists near zero; on every finite invariant mode truncation it exists for each finite v. Finite truncations do not establish invertibility on the infinite space at arbitrary v.

Use hbar=1 and the convention
\[
\dot\rho=-i[H,\rho]
+\sum_\mu\left(L_\mu\rho L_\mu^\dagger
-\tfrac12\{L_\mu^\dagger L_\mu,\rho\}\right).
\]
The unnormalized no-jump state has generator
\[
G_{\rm nj}=-iH-\tfrac12R,\qquad R=\sum_\mu L_\mu^\dagger L_\mu\ge0.
\]
Thus the exact condition for a bounded instantaneous realization of G is
\[
R(v)=-[G(v)+G(v)^\dagger]\ge0,\qquad
H(v)=\frac{i}{2}[G(v)-G(v)^\dagger]. \tag{4}
\]
For bounded norm-continuous G on a finite interval, (4) permits a one-particle completion with L=sqrt(R). The research task must justify the interval and regularity; it must not assume them from ||K_v||<=1. That endpoint bound concerns evolution from zero, whereas (4) concerns every infinitesimal intermediate step. In a finite-dimensional regular setting, the corresponding full Lindblad propagators are CPTP and divisible. A time-independent semigroup is a separate stronger specification.

At zero, with alpha=c_1/c_0>0, direct algebra gives
\[
G(0)=\alpha(S-I),\quad
R(0)=\alpha(2I-S-S^\dagger)\ge0,\quad
H(0)=\frac{i\alpha}{2}(S-S^\dagger).
\]
There is no strictly positive spectral gap for R(0) on the half-infinite space. A bare continuity argument does not establish (4) for positive v.

One fixed analytical route for MC08-E01 is to audit the shift-symbol reduction. If
\[
\log(F(w)/c_0)=\sum_{n\ge1}b_nw^n,
\]
then, inside its analytic disk,
\[
G(v)=\sum_{n\ge1}n b_n v^{n-1}(S^n-I).
\]
The candidate sufficient bound
\[
\sum_{n\ge2}n^3|b_n|\,v^{n-1}\le b_1 \tag{5}
\]
uses |1-cos(n theta)|<=n^2(1-cos theta) to control the Hermitian part uniformly in the boundary angle. MC08-E01 must verify the Toeplitz-form argument and give an explicit positive interval using a zero-free disk and coefficient/tail bounds. Equation (5) is a proposed audit route, not a recorded theta certificate. The zero-angle limit must be treated analytically rather than sampled.

## A common fermionic model and its Hermitian environment

If (4) is established, test a quadratic Hamiltonian and linear loss operators on finite mode sets:
\[
H_{\mathcal F}(v)=d\Gamma(H(v)),\qquad
L_\mu(v)=\sum_j B_{\mu j}(v)a_j,\qquad B^\dagger B=R.
\]
The intended identity is
\[
\sum_\mu L_\mu^\dagger L_\mu=d\Gamma(R),\qquad
G_{{\rm nj},\mathcal F}=d\Gamma(G),\qquad
U_{{\rm nj},r}(v,0)=\bigwedge^rK_v. \tag{6}
\]
Verify conventions, sector normalization and initial conditions. Loss trajectories can change particle number; the conditioned no-jump operator preserves each sector and keeps the original vacuum convention. Quadratic open-fermion methods such as Prosen's third quantization are relevant here, with his factor-two jump convention explicitly converted.

A microscopic Hermitian reservoir or repeated-interaction construction must reproduce the chosen instrument and record its approximations. Specify environment preparation, coupling range, measurement, time dependence, success probability and system-size dependence. A Markov reservoir limit is not automatically an exact finite-dimensional closed Hamiltonian realization. Infinite-mode and arbitrary-finite-particle limits need domain and convergence estimates; a finite covariance calculation is not enough.

The existing Jordan block forbids a fixed metric that makes the original transfer Hermitian. It does not forbid a Hermitian coherent component H plus jump terms, or a larger Hermitian system. Those are the intended objects here.

## Observable preservation and quantum-information tools

The measured quantity must retain the real signed matrix element in (1), including its positive scalar prefactor. A transition probability gives |A|^2 and loses the required sign. Specify a coherent reference and interference readout, keeping any fermion-parity superselection constraint. Conditional normalization must be tracked through the no-jump success probability.

For each proposed tool, record the exact object it constrains and the additional bridge to (1) or (2):

| Tool | Potential role | Obligation before claiming a theta consequence |
| --- | --- | --- |
| Kraus maps and unitary dilation | Realize each endpoint and fix an instrument | Preserve phase/basis information and provide a common family if needed |
| Lindblad trajectories and CP divisibility | Identify valid local-in-time noise and conditional propagation | Prove (4), regularity and the specified parameter domain |
| Quadratic fermionic evolution and third quantization | Organize one dynamics across sectors | Verify (6), conventions and mode/particle limits |
| Trace-distance, fidelity or entropy monotonicity | Bound distinguishability or response | Derive an explicit inequality for the original signed amplitude or ratio; positivity of states is insufficient |
| Noncrossing path or real-cone preservation | Possible mechanism for ordered amplitude signs | Obtain the required locality/order property from unchanged theta data; generic complete positivity does not imply it |

MC08-B02 compares at most two specific mechanisms and selects one for a worked return. No broad machinery survey, uncontrolled hierarchy or numerical scan replaces that choice.

## Controls and classification of possible gains

| Control or comparison | What it tests and the failed premise |
| --- | --- |
| F_*(w)=1+w+2w^2 | Positive contraction and endpoint Kraus completion coexist with a two-fermion amplitude -v^2/F_*(v)^2<0. It fails unchanged theta reconstruction. This rules out an inference from generic channel positivity. Test any proposed stronger generator premise explicitly. |
| Gaussian F(w)=c_0 exp(a w), a>0 | Exact directed semigroup and known positive minors provide a normalization comparison. It retains the same Jordan obstruction. This is not evidence for the canonical theta estimate. |
| Euler-factor, reflected and smooth positive-primitive sources | Generic coefficient dynamics and endpoint dilations survive where generating sums converge; unchanged theta coefficients fail. No uncomputed intermediate-rate or minor sign is assigned. A positive-time collision does not alone determine a time-zero minor. |
| Weighted-square and finite-prime modifications | Canonical weights fail; full evenness or orbital endpoint conditions may also fail. Discrete constructions remain available under their own convergence assumptions. |
| Arbitrary CPTP completions and different unravelings | Detect loss of the selected instrument, basis or signed readout. Positivity of a Choi matrix is not total nonnegativity of K. |

Use the [standing control inventory](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [control discipline](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md). Naming a missing exact-source identity does not prove that a derived bound discriminates a control.

A valid local Lindblad realization is a physical-realization result. A source-dependent bound, new covered parameter range, explicit convergence guarantee or scoped obstruction is a separately stated analytical result. The unknown theta minor signs are not improved by a generic realization alone. Record each gain in its actual class.

## Work products and stopping conditions

Save derivations in notes, computations and small records in numerics, and reviews in reviews; use the actual date and next unused number. Every return records actual model/effort, input versions, source normalization, exact domain, controls, limits and one next B/E recommendation. The [common bibliography](../../../../references/README.md) remains canonical.

Stop the selected attempt when it has a worked conclusion or a precise unpaid obligation. Failure of (4) closes only the specified exact no-jump parameterization on the stated domain. Alternatives such as memory, another time parameter or explicit positive scalar attenuation require a B decision and a changed contract; attenuation must be recovered in the original observable and is generic by itself. Large-v noninvertibility and unbounded-generator issues cannot be bypassed by finite cutoffs.

The planning packet creates no new manuscript snapshot, starts no computation or delegated research, and does not change frozen MC02 results. This chat retains its unique [brainstorm history registration](../../brainstorm/chat-histories/index.json); future new branch chats register here when launched. Use [GPT research workflow](../../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md) and [chat-history workflow](../../../../../../../tools/CHAT_HISTORY.md).
