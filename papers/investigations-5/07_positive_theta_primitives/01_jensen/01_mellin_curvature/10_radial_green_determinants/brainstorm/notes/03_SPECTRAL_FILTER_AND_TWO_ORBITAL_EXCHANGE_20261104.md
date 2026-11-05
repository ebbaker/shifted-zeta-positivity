# Restoring the excited box levels and tracking the exchange sign

4 November 2026. Prepared for Edward Baker with substantial LLM assistance from OpenAI Codex, recorded model **gpt-6-astra**, reasoning effort **xhigh**. Analytical brainstorm follow-up to [the energy-response note](02_HILBERT_SPACE_AND_ENERGY_RESOLVED_CANCELLATION_20261104.md). The inequalities in this note have proof-author checks only. They reuse the investigation's saved coefficient enclosures.

## 1. An energy filter on the physical Hilbert space

Use MC08's Dirichlet box realization on \(L^2(0,1)\) with \(H=-\pi^{-1}\partial_x^2\), eigenfunctions \(\sqrt{2}\sin(n\pi x)\), and \(E_n=\pi n^2\). Let \(P_1\) project onto its ground level. At inverse temperature \(\beta=e^{4u}\) insert the effect
\[
 W_s=P_1+s(I-P_1),\qquad 0\le s\le1.
\]
An energy-selective filter with amplitude operator \(W_s^{1/2}\) retains the ground level with probability one and accepts each excited level with probability \(s\). Its **unnormalized** accepted heat trace is
\[
 Z_s(\beta)=\operatorname{Tr}(W_s e^{-\beta H})
 =e^{-\beta\pi}+s\sum_{n\ge2}e^{-\beta\pi n^2}.
\]
Keep this trace's total weight when forming \(p_s(u)=e^u Z_s(e^{4u})\) and \(\Phi_s=(p_s''-p_s)/8\). Write \(\Phi_s=\Phi_1^{\rm mode}+s\sum_{n\ge2}\Phi_n^{\rm mode}\), where for any box energy \(E\),
\[
 \phi_E(u)=e^u(2X^2-3X)e^{-X},\qquad X=Ee^{4u},\qquad \Phi_n^{\rm mode}=\phi_{E_n}.
\]
All these densities are positive on the half-line. The filter parameter can be varied at fixed temperature. The integration over \(u\) below uses a family of such temperatures. [MC08 natural Hamiltonians, seeds A/C](../../../08_open_quantum_dynamics/research-progress/handoffs/10_NATURAL_HAMILTONIAN_BRAINSTORM_CONTINUATION_20261103.md) · [Fixed-temperature box interpretation](../../../brainstorm/notes/05_FIXED_TEMPERATURE_DETERMINANT_AND_RADIAL_GREEN_20261104.md)

## 2. From the trace to the signed overlap

In the second space, \(L^2((0,\infty),du)\), prepare
\[
 f_i^{(s)}=\frac{\Phi_s^{(2i)}}{\sqrt{\Phi_s}},\qquad
 g_\ell^{(s)}=m_\ell\sqrt{\Phi_s},\qquad
 m_\ell=\frac{u^{2\ell}}{(2\ell)!}.
\]
For the diagonal block take \(0\le i<q\) and \(\ell=q,\ldots,2q-1\). Integration by parts gives \(\langle f_i^{(s)},g_\ell^{(s)}\rangle=c_{\ell-i}(s)\), where \(c_j(s)=\int m_j\Phi_s\). All boundary terms vanish for these pairings even when \(s<1\): \(\ell>i\) gives enough zeros of \(m_\ell\) at the origin, and the modes decay at infinity. The boundary-preserving Green reference also carries the endpoint atom \((1-s)\tau\delta_0\) along this interpolation, where \(\tau=\sum_{n\ge2}(4E_n-1)e^{-E_n}/8\). Every coefficient index in this block is at least one, so the continuous density alone yields its exact entries.

Antisymmetrizing these preparations gives the real, unnormalized overlap
\[
 D_q(s)=\left\langle\bigwedge_{i=0}^{q-1} f_i^{(s)},\
                        \bigwedge_{j=0}^{q-1}g_{q+j}^{(s)}\right\rangle
       =\det M_q(s),\qquad M_q(s)_{ij}=c_{q+j-i}(s).
\]
Here \(x\) in the box eigenfunctions is the spatial coordinate, while \(u\) labels temperature in a source orbital. The index \(q\) counts antisymmetrized source orbitals. If energy labels are wanted on these same states, MC08's lift is
\((T_s\psi)(u,n)=\sqrt{w_n(s)\phi_{E_n}(u)/\Phi_s(u)}\,\psi(u)\), with \(w_1=1,\ w_{n\ge2}=s\). Summing over \(n\) proves it is an isometry. Varying \(s\) changes both preparations, which is important when differentiating the overlap. Normalizing the two wedges introduces two \(s\)-dependent norms; the sign agrees, but the derivative and fractional-loss bounds below apply to the unnormalized overlap. At the canonical endpoint MC08's separate coefficient-space experiment recovers the sign through its reference-arm probability difference, with amplitude \(v^{q^2}D_q(1)/F(v)^q\) on its prescribed activity interval. [Source states](../../../08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md) · [MC08 readout, equations 19–20](../../../08_open_quantum_dynamics/notes/03_FERMIONIC_LINDBLAD_REALIZATION_20261102.md)

## 3. The entire restoration at two orbitals

Write \(a_j(E)=\int m_j\phi_E\), \(b_j=a_j(\pi)\), and \(h_j=\sum_{n\ge2}a_j(E_n)\). On this diagonal \(c_j(s)=b_j+sh_j\). The direct and exchanged assignments give
\[
 D_2(s)=c_2(s)^2-c_1(s)c_3(s),\qquad
 D'_2(s)=\sum_{n\ge2}\chi_2(E_n;s),
\]
\[
 \chi_2(E;s)=2c_2(s)a_2(E)-c_3(s)a_1(E)-c_1(s)a_3(E).
\]
Each \(\chi_2\) is the partial derivative for increasing that particular spectral weight at the current preparation. Evaluating along \(s\) retains the quadratic term \(s^2(h_2^2-h_1h_3)\) of the determinant exactly.

**Every excited box level lowers this overlap along the whole path.** For \(E\ge4\pi\) direct differentiation gives
\[
 -(\log\phi_E)'=4X-9-\frac{12}{2X-3}>40,\qquad X=Ee^{4u}\ge4\pi>25/2.
\]
Integrating \(-\phi_E'\ge40\phi_E\) against \(u^m/m!\) for \(m\ge1\) bounds each normalized moment by the previous moment divided by 40. Applying it twice yields \(a_2(E)/a_1(E)\le1/1600\).

For the other half of the comparison take the compact reference coefficients \(c_j^*\) from the [existing exact record](../../numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json). Its entrywise allowance \(\epsilon=1/40000\) gives, for \(1\le j\le5\),
\[
 |c_j(s)-c_j^*|\le\epsilon c_j^*,\qquad 0<h_j\le\epsilon c_j^* .
\]
For the first bound the omitted primitive moments are the first-mode spatial exterior plus \(s\) times the higher-mode moments. For the second bound \(h_j=y_{j-1}-y_j>0\) in the manuscript's notation. Both are covered by the saved \(T_{j-1}+T_j\) payment. In particular the full-half-line reference \(b_j\) at \(s=0\) is distinguished from \(c_j^*\). [Green comparison](../../manuscript/sections/01_green.tex) · [Input boxes and verification](../../notes/06_RGD_E02_R2_FIRST_NEXT_ORDER_RETURN_20261104.md)

Use \(t_j=(c_0^*)^{j-1}c_j^*/(c_1^*)^j\). The recorded \(c_1^*>1/3000,\ 0<c_0^*<1/16,\ t_2\in[.465,.466],\ t_3\in[.135,.137]\) imply
\[
 \frac{c_3(s)}{c_2(s)}
 >\frac{1-\epsilon}{1+\epsilon}\frac{.135}{.466}\frac{16}{3000}
 >\frac1{700}>\frac1{800}\ge\frac{2a_2(E)}{a_1(E)} .
\]
Thus even one of the two exchange contributions \(c_3(s)a_1(E)\) exceeds the direct gain \(2c_2(s)a_2(E)\). The remaining exchange contribution is strictly positive and enters with a minus sign. This proves \(\chi_2(E_n;s)<0\) for all \(n\ge2\) and \(0\le s\le1\).

**How much is lost?** Set \(R=c_1^*c_3^*/(c_2^*)^2=t_3/t_2^2\le.137/.465^2<16/25\). Then \(D_2(0)/ (c_2^*)^2\ge(1-\epsilon)^2-(1+\epsilon)^2R>7/20\). Integrate the exact derivative and use the upper bounds for \(h_j\):
\[
 0<D_2(0)-D_2(1)
 \le\int_0^1(c_3(s)h_1+c_1(s)h_3)\,ds
 \le2\epsilon(1+\epsilon)c_1^*c_3^* .
\]
Consequently \(0<(D_2(0)-D_2(1))/D_2(0)<10^{-4}\). This is a conservative upper bound on the loss. It gives a directional comparison in an already-positive case.

## 4. What changes at three orbitals and beyond

At any fixed \(q\), the exact derivative for one level is
\[
 \chi_q(E;s)=\sum_{i,j=0}^{q-1}
 \operatorname{cof}_{ij}M_q(s)\,a_{q+j-i}(E),\qquad
 D_q(1)-D_q(0)=\int_0^1\sum_{n\ge2}\chi_q(E_n;s)\,ds.
\]
For fixed \(q\) the sums of each entry converge and the cofactors are bounded on the compact path. This formula includes mixed effects through the \(s\)-dependent cofactors and needs no invertibility assumption. The previous note proves \(a_j(E)/a_1(E)\to0\) for fixed \(j>1\). The sole index-one entry is at the bottom left. Hence the high-level response divided by \(a_1(E)\) tends to \((-1)^{q-1}D_{q-1,q+1}(c(s))\).

At \(q=3\) the limiting cofactor is **positive**. It equals \(c_4(s)^2-c_3(s)c_5(s)\). After extracting the common positive scale \((c_1^*)^8/(c_0^*)^6\), a lower bound is
\[
 (1-\epsilon)^2(.028)^2-(1+\epsilon)^2(.137)(.005)>0
\]
from the same record. Thus sufficiently high box levels *raise* the three-orbital overlap at fixed \(s\). The sign and size of the complete three-orbital restoration, including the lowest excited levels, are the next questions. The two-orbital argument works through the coefficient ratios and the spectral gap. Other sources satisfying the same inequalities would share it. Reweighted square controls lose the canonical coefficient payment, Euler shifts change the source, and shape controls lack its square spectrum. A growing-order comparison would require corresponding bounds on the signed sum of cofactors.

The referenced coefficient enclosures were read from the saved record, and their stated box memberships and the rational comparisons used above were checked with exact fraction arithmetic. No new quadrature or independent assessment was performed. [Portfolio result index](../../../../../../../../result-summaries/README.md) · [Control scope](../../../../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns to avoid](../../../../../../../../avoid/README.md) · [Separate absolute bounds](../../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
