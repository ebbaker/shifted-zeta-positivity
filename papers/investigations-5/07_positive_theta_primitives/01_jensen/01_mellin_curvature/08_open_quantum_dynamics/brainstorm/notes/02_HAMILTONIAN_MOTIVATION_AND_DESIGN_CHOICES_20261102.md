# MC08-B03: why the Hamiltonian was defined from the transfer

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded **gpt-6-astra / max**, chat `01a19f55-b2e6-75f0-a465-ad11ad5d5488`, turn `01a19f62-c6e4-7d41-92ba-0e58c455b5ef`; same brainstorm history **0001**.

**Scope:** the author is considering revisiting MC08's Hamiltonian and asks for its detailed motivation. This note reconstructs the design logic, derives the formula, and identifies what is fixed versus chosen. It does not choose or execute a replacement architecture, propose a new signed criterion, or complete E04. The algebraic clarifications have same-assistant checking only.

## 1. The original question was an inverse realization problem

The starting object was the reviewed coefficient transfer
\[
K_v=F(vS)/F(v),\qquad K_0=I,
\quad F(w)=\sum_{n\ge0}c_nw^n,
\]
with c_n the unchanged theta source moments and S the backward shift on coefficient sites. Its exterior powers give
\[
\langle I|\Gamma(K_v)|J\rangle
=\frac{v^{\sum J-\sum I}}{F(v)^r}\det[c_{j_b-i_a}].
\]
The reason to preserve K_v was exact access to all these original signed minors using one one-particle map. The complete scalar F(v) makes K_v a contraction, and the empty-vacuum block is fixed to +1. Those were mathematical and observation requirements.

The [continuous-v discussion](../../../brainstorm/notes/01_CONTINUOUS_V_EVOLUTION_AND_HERMITIAN_SCOPE_20261102.md) then asked whether this family could be a continuous evolution. Activity v naturally weights displacement. Promoting it to an evolution clock is a modeling choice; v is not the inverse temperature beta, the theta coordinate u, or Mellin tilt s.

The [MC08 overview](../../research-overview/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_OVERVIEW_20261102.md), under its first analytical test, already specifies H=i(G-G†)/2 and the loss condition. Thus the later [B01 architecture decision](../../notes/02_OPEN_SYSTEM_ARCHITECTURE_DECISION_20261102.md) did not select H by comparing candidate energy spectra. It inherited this H from the exact no-count requirement and selected the fermionic loss/environment architecture implementing it.

This is the motivation: construct open dynamics whose specified conditional amplitude is exactly K_v. The hoped-for usefulness was a physical setting for comparing the original signed amplitudes, with quantum dynamics and response tools available. Identifying a thermodynamic energy spectrum was not the selection principle.

## 2. Exact continuous evolution fixes G

If psi(v)=K_v psi(0) and K_v is invertible, then
\[
\partial_v\psi=G(v)\psi,\qquad G(v)=K'_vK_v^{-1}.
\]
Direct differentiation gives
\[
G(v)=SF'(vS)F(vS)^{-1}-\gamma(v)I,
\qquad \gamma(v)=F'(v)/F(v).
\]
It is the unique generator of that complete operator path in the chosen fixed basis and clock. It is not a guessed effective Hamiltonian. On the infinite space the bounded inverse and norm continuity are available on the established local interval; no unrestricted large-v statement follows.

The original transfer is generally nonunitary. Already its two-site restriction for v>0 is
\[
K_{v,1}=F(v)^{-1}\begin{pmatrix}c_0&vc_1\\0&c_0\end{pmatrix}.
\]
This nontrivial Jordan block cannot be an exponential of a self-adjoint Hamiltonian at a fixed real or imaginary time, or become self-adjoint in a positive definite metric. More generally any real-time closed Hermitian evolution on this same space has a unitary endpoint. This led to the conditional open-system interpretation. The obstruction does not exclude a larger system or a different time-dependent imaginary-time construction.

## 3. The no-count requirement fixes H and the total loss operator

A direct infinitesimal derivation avoids treating the splitting as an arbitrary symmetrization. At a fixed finite cutoff, let the no-count measurement operator be
\[
M_0=I+G\,\delta v+o(\delta v),
\]
and let count channels have leading operators M_mu=sqrt(delta v) L_mu. Preservation of total probability, summed over no count and all counts, requires
\[
M_0^\dagger M_0+\sum_\mu M_\mu^\dagger M_\mu=I+o(\delta v).
\]
The coefficient of delta v gives
\[
G+G^\dagger+\sum_\mu L_\mu^\dagger L_\mu=0,
\qquad R:=\sum_\mu L_\mu^\dagger L_\mu=-(G+G^\dagger)\ge0.
\]
The remaining anti-Hermitian part is norm preserving. In the real-time convention psi'=-iH psi with hbar=1, it must be -iH. Hence
\[
\boxed{H=\frac i2(G-G^\dagger),\qquad G=-iH-\frac12R.}
\]
Equivalently the effective, non-Hermitian Hamiltonian is H_eff=iG=H-iR/2, and H is its Hermitian part. The factor i is required by the Schroedinger convention. The Hermitian part of G itself is -R/2; it describes attenuation.

The same convention is in [Castin–Dalibard–Molmer, equation (4), with (5)–(11)](https://arxiv.org/html/0805.4002v1), reinspected on this turn. This is already a cataloged primary source; the application to the theta generator is the repository's construction. The displayed infinitesimal derivation is elementary and does not import a new reservoir or infinite-domain theorem.

The norm identity is
\[
\frac{d}{dv}\|\psi\|^2=-\langle\psi,R\psi\rangle.
\]
H exists algebraically for any bounded G. The substantive admissibility issue was R>=0 for the actual source at every intermediate activity. Endpoint contractivity of K_v alone is insufficient. [E01](../../notes/01_NO_JUMP_ADMISSIBILITY_AUDIT_20261102.md), accepted at its stated scope by [E03](../../reviews/02_OPEN_QUANTUM_DYNAMICS_ASSESSMENT_20261102.md), proves
\[
R(v)\ge(2I-S-S^\dagger)/8000\ge0,
\qquad 0\le v\le1/25.
\]
This is a source-paid local realization result. The splitting formula itself is not that result.

## 4. Why the Hamiltonian looks like hopping

Write log(F(w)/c_0)=sum_(n>=1) lambda_n w^n and alpha_n(v)=n lambda_n v^(n-1). Then
\[
\begin{aligned}
G&=\sum_{n\ge1}\alpha_n(S^n-I),\\
H&=\frac i2\sum_{n\ge1}\alpha_n(S^n-(S^\dagger)^n),\\
R&=\sum_{n\ge1}\alpha_n(2I-S^n-(S^\dagger)^n).
\end{aligned}
\]
The sum for R is positive on the proved interval; no positivity of every alpha_n is required or asserted. The coefficients are real, so H has purely imaginary hopping entries and zero diagonal in the coefficient basis. No on-site spectrum pi j^2 was an input. All theta dependence still enters through the coefficients of F, so this is source-dependent, but it is not the circle Hamiltonian expressed in an established new basis.

At v=0, alpha=c_1/c_0>0 gives
\[
G(0)=\alpha(S-I),\qquad
H(0)=\frac{i\alpha}{2}(S-S^\dagger),\qquad
R(0)=\alpha(2I-S-S^\dagger).
\]
The exact cancellation displays the design:
\[
-iH(0)-R(0)/2
=\frac\alpha2(S-S^\dagger)
 -\alpha I+\frac\alpha2(S+S^\dagger)
=\alpha(S-I).
\]
Coherent motion and conditional loss together produce the required directed generator. Neither component alone gives that transfer. At this endpoint the positive discrete-Laplacian form occurs in R, as a loss rate, while H supplies the complementary coherent motion. Using a positive Laplacian as an imaginary-time energy would be a different physical interpretation and would not automatically recover K_v.

The [previous energy primer](01_FOCK_ENERGIES_AND_THETA_TRANSFER_20261102.md)'s zero-mean observation now has an explanation: for a site occupation J, expectation of dGamma(H) is sum_(j in J) H_jj=0. The finite two-site eigenvalues nevertheless are +/-alpha/2. Off-diagonal energies and zero site means are compatible with a legitimate Hamiltonian. They are not evidence of an algebraic defect; they show that site populations are not the energy eigenmodes. The vacuum zero is a fixed normal-ordering and phase convention, not a proof of ground-state energy or thermal equilibrium.

## 5. What B01 selected on Fock space

Once the one-particle H and R were fixed, B01 chose a number-conserving quadratic coherent Hamiltonian and linear annihilation jumps:
\[
\mathbb H=d\Gamma(H),\quad B=\sqrt R,\quad
L_\mu=\sum_j B_{\mu j}a_j.
\]
Then the CAR give
\[
\sum_\mu L_\mu^\dagger L_\mu=d\Gamma(R),\qquad
-i\mathbb H-\tfrac12\sum_\mu L_\mu^\dagger L_\mu=d\Gamma(G).
\]
This reproduces every exterior power wedge^r K using the same model for every particle sector. Quadratic structure and linear loss were useful because they preserve the one-particle-to-determinant relation, lower particle number after counts, and admit the cutoff and counting construction. Interactions or gain terms would require a fresh demonstration of the exact amplitude identity; they were not introduced merely to obtain a more elaborate energy theory.

The physical architecture selected fresh vacuum modes, ideal counting, dense mode couplings and controlled coherent reference readout. The exact finite-mode instrument has a prescribed collision limit; it is not an exact regular finite reservoir. Its enlarged interaction conserves number and parity. No theta-energy resonance, bath at inverse temperature beta, or thermal detailed-balance condition was imposed. H(v) is generally time dependent and need not conserve system energy along the monitored evolution.

## 6. Which choices are open to reconsideration?

| Ingredient | Status within the old construction |
| --- | --- |
| Original coefficients and determinant observable | Inherited mathematical target |
| Backward-shift coefficient encoding K_v | A selected exact representation of that target |
| Activity v used as real-time clock | A modeling choice |
| Whole path, fixed occupation basis and calibrated no-count phase | Fixed by the realization contract |
| H=i(G-G†)/2 and R=-(G+G†) | Forced after the preceding choices |
| Linear loss, vacuum stream and counting arrangement | Selected architecture; it is not the only possible quantum completion |
| Identification with the source energies pi m^2 | Not made or proved |

For the exact fixed G, a replacement H+Delta H would require R+Delta R with Delta R=-2i Delta H. If both changes are self-adjoint, this forces both to vanish. Thus arbitrary new energy levels cannot be offset by changing a positive loss matrix while leaving the same phase-calibrated no-count path intact. The same uniqueness applies on finite Fock cutoffs once the full no-count generator is fixed. Different factorizations R=sum L†L can remain, and the total unconditioned channel alone has additional unraveling freedoms. Those are not a contradiction: this uniqueness fixes the amplitude instrument, not just its average channel.

Several qualifications matter before interpreting this as a universal restriction:

- A different path to a chosen endpoint need not have the same G or H.
- A different clock v(t) gives H_lab=dot(v) H and jumps sqrt(dot(v)) L for an increasing schedule. The original construction therefore does not fix an independent laboratory energy scale.
- A real scalar attenuation multiplying K changes R, not the antisymmetric part defining H. It must be restored in amplitude readout.
- Scalar energy shifts introduce phases. In one-particle space H -> H+epsilon(v) I gives K -> exp(-i integral epsilon) K, and in sector r the phase is multiplied by r. These phases can be calibrated in a redesigned readout, but are excluded by the old exact-phase convention. Adding a scalar to the whole Fock Hamiltonian instead shifts the vacuum phase too.
- A time-dependent frame introduces a connection term into H and changes the represented observables. An enlargement or a different conditioning rule can also change the effective construction. None establishes equivalence to the circle energy model without a new correspondence.

**Assessment:** the formula was well motivated for the specified realization problem. The energy interpretation was downstream of the desired transfer. If the next physical principle is to come directly from the circle spectrum E_m=pi m^2, the substantive reconsideration is whether the coefficient transfer should be prescribed as the dynamics at all, or should instead be recovered as an observable of a model whose energy is chosen first. This identifies a design question for discussion; no new Hamiltonian or proof route is selected here.

Read with [the result index](../../../../../../../../result-summaries/README.md), especially [theta identities and bookkeeping](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and [the avoid index](../../../../../../../../avoid/README.md), especially [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scoped exclusions](../../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). No representation is promoted to a signed estimate. Existing review statuses and frozen manuscripts/returns are preserved; current task status stays in the [sole MC08 register](../../research-progress/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md).
