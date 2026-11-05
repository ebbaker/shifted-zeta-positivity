# Which energy levels lower the fermionic overlap?

4 November 2026. Prepared for Edward Baker with substantial LLM assistance from OpenAI Codex, recorded model `gpt-6-astra`, reasoning effort `xhigh`. Brainstorm discussion drawing on MC08. The level-response calculation below has an analytical self-check only.

## The physical choice

MC08 distinguishes two questions. Its open-system construction starts with a prescribed coefficient transfer and reproduces the signed amplitude for a specified measurement. Its source-state construction starts with the actual orbitals \(f_i=\Phi^{(2i)}/\sqrt\Phi\) and \(g_j=m_j\sqrt\Phi\), where \(m_j=u^{2j}/(2j)!\). Their antisymmetric many-particle overlap gives \(D_{r,k}\), using the ordered lists \(i=0,\ldots,r-1\) and \(j=k,\ldots,k+r-1\). The permutation signs describe exchange in those preparations. In the source heat trace, \(E_n=\pi n^2\) labels a one-particle energy and \(u=\log(\beta)/4\) labels inverse temperature. Assigning one distinct box energy to each of the \(r\) orbitals would change the observable. [MC08 source states](../../../08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md) · [Fixed-temperature interpretation](../../../brainstorm/notes/05_FIXED_TEMPERATURE_DETERMINANT_AND_RADIAL_GREEN_20261104.md)

I would pursue the source-and-energy construction in seed C of the MC08 natural-Hamiltonian handoff. How does the signed overlap change when one energy level gains a little weight in the source heat trace? This is a response of the unnormalized overlap, with all other weights fixed. The parameter changes the spectral weight, with no physical time evolution assumed. MC08 already exhibits hops with opposite exchange signs depending on the occupied sites crossed. The remaining issue is the size of the competing contributions after they are combined. [Natural-Hamiltonian handoff](../../../08_open_quantum_dynamics/research-progress/handoffs/10_NATURAL_HAMILTONIAN_BRAINSTORM_CONTINUATION_20261103.md) · [Signed hops](../../../08_open_quantum_dynamics/notes/04_SIGNED_COMPARISON_DECISION_20261102.md)

## What the energy observable should measure

Write \(\Phi_n\) for the contribution of level \(n\) and \(\rho_n(u)=\Phi_n(u)/\Phi(u)\). MC08's isometry \(T\psi(u,n)=\sqrt{\rho_n(u)}\,\psi(u)\) preserves the orbitals' overlaps. Projecting the two *fixed* lifted states onto level \(n\) gives the integral of \(m_j\rho_n\Phi^{(2i)}\). Changing that level's source weight changes both preparations. Differentiating their mixed pairing gives the integral of \(m_j\Phi_n^{(2i)}\). Already for \(i=1\) the difference of integrands is
\[
 m_j\bigl((\rho_n\Phi)''-\rho_n\Phi''\bigr)
 =m_j(2\rho_n'\Phi'+\rho_n''\Phi).
\]
These terms sum to zero over the complete energy resolution because \(\sum_n\rho_n=1\). They matter when asking what one level contributes. This gives a reason to keep the actual temperature-dependent preparations in a physical explanation. [MC08 energy responses](../../../08_open_quantum_dynamics/notes/06_THETA_ENERGY_LEVELS_AND_FERMIONIC_LABELS_20261102.md)

## A directional sign at two particles

Let \(b_j\) be the coefficients at the source about which we perturb, either the complete source or the full-half-line boundary-preserving first mode. The diagonal uses only indices \(j\ge1\), so the reference atom at zero gives no contribution. Put \(p_E(u)=e^{u-Ee^{4u}}\), \(\Phi_E=(p_E''-p_E)/8\), and \(a_j(E)=\int_0^\infty m_j\Phi_E\). Increasing the weight at energy \(E=\pi n^2\) by \(s\) changes the diagonal's entries from \(b_j\) to \(b_j+s a_j(E)\). At two particles the response is
\[
 \left.\frac{dD_{2,2}}{ds}\right|_0
 =2b_2a_2(E)-b_3a_1(E)-b_1a_3(E).
\]
At sufficiently high energy the response is strictly negative. Here is the scale that decides it. For fixed \(j\ge1\),
\[
 a_j(E)\sim\frac{e^{-E}}{8(4E)^{2j-1}}\qquad(E\to\infty).
\]
Indeed, with \(I_h=\int m_h p_E\), Green transfer gives \(8a_j=I_{j-1}-I_j\); the test and its first derivative vanish at zero. In \(I_h\) set \(v=4Eu\). After extracting \(e^{-E}(4E)^{-2h-1}\), the normalized integrand tends to \(v^{2h}e^{-v}/(2h)!\), and is bounded by \(v^{2h}e^{-3v/4}/(2h)!\) for \(E\ge1\). Hence the derivative divided by \(a_1(E)\) tends to \(-b_3<0\). This explains how a positive spectral level can lower the overlap. Its weight concentrates near \(u=0\), giving the greatest relative response to the lowest moment in the block, which enters the exchange term. The magnitude is exponentially small. The argument concerns sufficiently high levels one at a time.

For any **fixed** \(q\ge2\), the same calculation identifies the leading cofactor. The only entry of \([b_{q+j-i}]_{0\le i,j<q}\) with coefficient index one is its bottom left corner. Expanding the first derivative in cofactors and dividing by \(a_1(E)\) therefore yields
\[
 \lim_{E\to\infty}
 \frac{\partial_s D_{q,q}(b+s a(E))|_{s=0}}{a_1(E)}
 =(-1)^{q-1}D_{q-1,q+1}(b).
\]
This formula also covers a zero cofactor, in which case it leaves the leading nonzero sign open. The limit gives neither a uniform tail cutoff as \(q\) grows nor the effect of restoring the entire omitted spectrum.

**Next question.** Relative to the first-mode reference, can the signed response summed over \(n\ge2\) be bounded against the reference determinant, with explicit control over the levels before the asymptotic applies? If that estimate works, the terms with two or more insertions remain to be paid. If the reference margin or cofactors cannot be controlled as \(q\) grows, the physical picture still explains a direction of cancellation at fixed order. The two-particle mechanism also occurs for other positive base sources with \(b_3>0\); a theta-specific gain would have to use the complete unit-weight sum or reflection. Weighted square controls change those weights, shifted Euler controls change the source, and abstract shape and matched-Gram controls omit the exact arithmetic or the derivative preparations. [Previous brainstorm](01_RESULTS_AND_NEXT_DIRECTION_20261104.md) · [Matched-Gram control](../../../09_source_overlap_kernels/notes/01_KERNEL_MECHANISM_SELECTION_20261103.md) · [Result index](../../../../../../../../result-summaries/README.md) · [Collision controls](../../../../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns to avoid](../../../../../../../../avoid/README.md) · [Re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
