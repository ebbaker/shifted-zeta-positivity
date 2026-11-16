# Exact Jacobi-chain height flow

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and effort
are unavailable in recorded configurations. **Scientific overview; no
research execution.** The subsequent branch-planning request is implemented
in the [research plan](../research-plan/01_JACOBI_CHAIN_RESEARCH_PLAN_20261113.md)
and [sole JCH register](../research-progress/01_JACOBI_CHAIN_RESEARCH_PROGRESS_20261113.md).
JCH-B01 selects the first useful target; no theorem or norm is selected here.

## Scientific question

Can one exact infinite chain generate a useful continuous family of Newman
wavefunctions, with a recursive description of how the state propagates
as height grows? The purpose is to understand the structure of that
evolution and its signed return amplitude. The chain's existence is the
inherited starting point; useful theta-dependent transport or transfer
information remains open.

This is branch 02 of the
[broader program](../../research-overview/01_TENSOR_NETWORK_PROGRAM_OVERVIEW_20261113.md).
It owns fixed-basis height evolution, the associated wavefunction and its
single-excitation MPS encoding. The chain-site index is polynomial degree,
not a sample of height or a QTT resolution bit.

## Complete source and exact realization

Use the complete [GNP source](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex),
with
\(W_\lambda=e^{\lambda u^2}\Phi\),
\(H_\lambda(z)=\frac12\int W_\lambda(u)e^{izu}du\), and
\(H_0(z)=\xi(1/2-iz/2)/8\). Initially
\(0\le\lambda\le1/2\), \(\tau=1/2-\lambda\), and \(z=x+iy\).
Real height \(x\) is twice zeta height; imaginary time decreases \(\lambda\).

Set \(Z_*=\int W_{1/2}\) and \(d\mu_*=W_{1/2}du/Z_*\).
The complete orthonormal polynomials satisfy

\[
 up_n=a_{n+1}p_{n+1}+a_np_{n-1},\quad a_0=0,
\]

and identify multiplication by \(u\), with its domain, with a
self-adjoint Jacobi operator \(J_*\). The inherited exact formulas are

\[
 v(\tau,z)=e^{-\tau J_*^2}e^{izJ_*}e_0,\qquad
 H_{1/2-\tau}(z)=\frac{Z_*}{2}\langle e_0,v(\tau,z)\rangle,
\]
\[
 \partial_xv=iJ_*v,\qquad \partial_\tau v=-J_*^2v.
\]

These statements and the prepared-vector domains are derived in
[Brainstorm 02 §§2–3](../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md).
The physics precedent is Chin et al., §3, Theorem 3.1; the
[reference-use record](../references/README.md) preserves the inspected
version and limits. Its bounded-support chain asymptotics are not imported
for the full-line theta measure.

The fixed weighted-space wavefunction corresponds in Lebesgue space to
\(\sqrt{W_{1/2}/Z_*}\,e^{-\tau u^2+izu}\). Its readout above is essential;
changing to the earlier source-amplitude wavefunction does not preserve
the same inner product by notation alone. Complex heights are defined on
the prepared analytic vectors, not by claiming \(e^{izJ_*}\) is a bounded
operator on every vector.

## Recursive structure and the MPS

The generator for height is nearest-neighbor, while its square has range
two. A finite height step \(e^{i\delta J_*}\) need not be banded. Encoding
\(v_n\) as the amplitude of a single excitation at site \(n\) yields
an exact bond-two MPS on infinitely many sites; the explicit cores and
state-norm convergence are in the source note, equation (7). The entries
still contain all the amplitudes \(v_n\), so the small bond dimension
does not provide an algorithm or a closed formula for those amplitudes.

At fixed imaginary time, every fixed component tends to zero as real
height tends to infinity, while total norm stays positive and constant.
Thus no fixed finite prefix approximates this state uniformly at all
heights. A height-dependent propagation estimate could explain how a
limiting family should grow. No propagation rate has yet been derived.

There is room to examine continuous transport, compatible discrete height
steps and alternative bases. The unit-circle sampling variation in the
source note §7 is related context, with its aliasing limitation retained;
it is not a finite scalar recurrence for the complete field.

## Open structural questions

The broad questions are how the theta couplings determine propagation,
whether a useful recursive or asymptotic description of the amplitudes
exists, and which norms preserve information about the signed return
amplitude. A useful outcome might be a controlled growth law for the
relevant chain region, a new transfer identity, or a precise limitation
of a particular encoding. These are possible outcomes, not scheduled tasks
or assumed estimates.

The full operator has real spectrum across the source coordinate, so
\(\|e^{i\delta J_*}-I\|=2\) for nonzero \(\delta\), despite strong
continuity and analytic prepared-state motion. Any near-identity proposal
must specify its topology. The inherited exclusion of a finite constant
matrix realization applies only to autonomous finite-dimensional linear
transport, not infinite chains or variable tensors.

## Controls, evidence and neighboring branches

The source discussion has exact identities and a
[same-assistant analytical check](../../../investigations-5/brainstorm/reviews/02_EXACT_HEIGHT_SELF_CHECK_20261113.md).
No independent review, useful theta transport rate or signed-field bound
is imported. The regular chain of \(2+2e^{\lambda-T}\cos x\) still has
a positive-time double zero. It fails the full theta profile/arithmetic,
infinite support and eventual threshold simplicity. The complete catalog
premise screen is in the source note §8.

Read the [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md),
[controls 12](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid 01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
These formulas are representations; self-adjointness is not a zero-sign
estimate for their boundary amplitude.

[Branch 03](../../03_volterra_coefficient_dynamics/README.md) owns coefficient
dynamics in the moving basis. [Branch 04](../../04_exact_infinite_tensor_products/README.md)
owns scale products, and [branch 01](../../01_qtt_newman_flow/README.md)
owns its QTT approximation questions. Their estimates could later be
combined through explicitly matched source and observation maps.

Use the [shared continuation prompt](../../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
for JCH-B01's first question selection under the new plan. The plan creates
task identities without activating research; no execution packet is issued
by this overview or its planning update.
