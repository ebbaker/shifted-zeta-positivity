# MC05-B01 return: source heat, Schur nonclosure and an oscillator formulation

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributor `/root/mc01_thermal` in its disjoint second-wave assignment; actual recorded **gpt-6-astra (Codex), ultra**, child `01a19a49-f8de-7770-a4ee-ec2acf3ace08`, turn `01a19a49-f900-7ae0-8f31-61b472611c01`. This is a contributing same-model assessment, **pending separate checking**. MC01's new return is not an input.

**Disposition: bounded assessment complete.** The canonical source heat deformation yields an exact nonlinear evolution of the Schur times and an explicit higher-coefficient term in the neighboring rectangular ratio. A smooth positive-source perturbation proves that this evolution has no universal closure from a finite coefficient prefix, even while preserving the accepted strict source signs and canonical exterior tails. No theta-specific inequality for the rectangular ratio or complete Mellin curvature is acquired.

The same selected deformation has a concrete physical interpretation: an explicitly normalizable even single-oscillator state, a one-sided quadratic annihilation flow, and an RH-equivalent statement about the location of that state's coherent-state probability zeros. This is an exact physical reformulation, not a new sign estimate, novelty claim or local interacting field theory.

## 1. Selection and evidence categories

This executes [MC05-B01 r1](../research-progress/01_SCHUR_TODA_STRUCTURE_RESEARCH_PROGRESS_20261101.md) from [Continuation05](../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md). Compare exactly two candidates:

1. The elementary Schur-time shift \(F(w)\mapsto e^{aw}F(w)\). Its multiplier is zero-free, so it cannot supply independent real-zero initial data: the zero set is unchanged. This is an immediate limitation of that candidate, not an obstruction to every hierarchy time.
2. The actual source heat deformation \(\Phi_\tau(u)=e^{\tau u^2}\Phi(u)\). **Select this candidate.** Its exact coefficient dynamics, rectangular consumer, finite-closure obstruction and oscillator representation are worked below. The target remains the complete source at \(\tau=0\); the deformation is a probe of a proposed integrable/physical mechanism, not a replacement of the target. Mellin tilt \(s\) is distinct from \(\tau\).

| Claim | Classification and status before separate checking |
| --- | --- |
| Source heat and Schur-time equations (1)–(4) | Exact identities, generic for the stated integrable source class and specialized to theta |
| Rectangular-ratio derivative (6) | Exact identity isolating an additional higher-coefficient obligation; no sign supplied |
| Finite-prefix nonclosure | Scoped theorem for a neighborhood of positive smooth even sources with the stated preserved data; not a theorem excluding theta-specific closure |
| Oscillator normalizability and flow | Exact construction and analytical identity on the actual theta orbit |
| RH via Husimi zeros | Equivalent physical reformulation, stated once; no supporting numerical checks or new proof |
| Gaussian Mellin bound | Unproved everywhere, including the first \(s\in[0,2]\) slab |

The [launch manifest](../../numerics/PARALLEL_PHYSICAL_LAUNCH_RECORD_20261101.json) freezes the common inputs and commit. The [local record](../numerics/MC05_B01_HEAT_SCHUR_RECORD_20261101.json) gives exact read hashes, the additional primary-source inspection, support-code hash and this frozen return's hash. No sibling assessment is a premise. The [result index](../../../../../../../result-summaries/README.md), [theta-identity lessons](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../../../../avoid/README.md), [reformulation rule](../../../../../../../avoid/01_restating_the_target.md), [re-realization warning](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scoped-exclusion rule](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) govern the interpretation.

## 2. The actual source deformation fixes the coefficient generator

For real \(\tau\), retain the full canonical series inside
\[
b_n(\tau)=\int_0^\infty u^{2n}e^{\tau u^2}\Phi(u)\,du,
\qquad c_n(\tau)=\frac{b_n(\tau)}{(2n)!},\qquad
F_\tau(w)=\sum_{n\ge0}c_n(\tau)w^n.
\]
The double-exponential tail makes these integrals and their fixed derivatives finite for every real \(\tau\). For \(n\ge0\),
\[
\boxed{\dot c_n=(2n+2)(2n+1)c_{n+1},\qquad
\partial_\tau F_\tau=(4w\partial_w^2+2\partial_w)F_\tau.} \tag{1}
\]
Negative coefficients remain zero by convention. Differentiating a negative-index zero does not create an endpoint contribution; the algebraic formula in (1), extended with \(c_n=0\) for \(n<0\), also gives zero there. These identities come directly from source multiplication, not from integrating noninteger powers by parts.

Let \(H_n=c_n/c_0\) and
\[
G_\tau(w)=\log(F_\tau(w)/c_0(\tau))=\sum_{m\ge1}t_m(\tau)w^m.
\]
This is the formal logarithm at zero; no zero-free global logarithm is assumed. Since \(c_0>0\),
\[
\dot H_n=(2n+2)(2n+1)H_{n+1}-2H_1H_n, \tag{2}
\]
\[
\partial_\tau G=4w(G_{ww}+G_w^2)+2G_w-2t_1. \tag{3}
\]
Coefficient comparison gives the exact hierarchy
\[
\boxed{\dot t_m=2(m+1)(2m+1)t_{m+1}
+4\!\sum_{a+b=m+1\atop a,b\ge1}ab\,t_at_b,\quad m\ge1.} \tag{4}
\]
For example \(\dot t_1=12t_2+4t_1^2\), \(\dot t_2=30t_3+16t_1t_2\). Thus physical source heat is not a translation in the first Schur time. The next connected coefficient enters at every order. Calling (4) a Toda flow would not provide a finite reduction, an independent positive initial condition or a sign-preserving theorem.

Jacobi–Trudi still gives \(D_{r,k}(\tau)=c_0(\tau)^r s_{(k^r)}(\mathbf t(\tau))\), and Desnanot–Jacobi remains exact. Those generic identities do not remove the extra data in (4). The nonlinear theta source ODE is a relation before integration; no unproved finite closure of these integrated coefficients is inferred from it.

## 3. The rectangular consumer exposes its next unpaid coefficient

At \(\tau=0\), accepted order-three positivity allows logarithms of the finite determinants below. By continuity those logarithms also exist on a possibly \(k\)-dependent neighborhood of zero; no global heat-parameter positivity is assumed. Differentiating a determinant gives
\[
\dot D_{r,k}=\sum_{i,j=0}^{r-1}\operatorname{Cof}_{ij}
(2(k+j-i)+2)(2(k+j-i)+1)c_{k+j-i+1}. \tag{5}
\]
All coefficients in this section have the same heat parameter. For \(r=3\), the highest new coefficient in \(\dot D_{3,k}\) is \(c_{k+3}\). It occurs only by differentiating the upper-right entry. Its positive cofactor sign gives
\[
[c_{k+3}]\dot D_{3,k}=(2k+6)(2k+5)
\det\begin{bmatrix}c_{k-1}&c_k\\c_{k-2}&c_{k-1}\end{bmatrix}
=(2k+6)(2k+5)D_{2,k-1}.
\]
Here the bracket means the coefficient when the lower coefficients are held fixed. Consequently, for
\[
\eta_k=\frac{D_{3,k-1}D_{3,k+1}}{D_{3,k}^2},\qquad k\ge1,
\]
\[
\boxed{\partial_\tau\log\eta_k\big|_{\tau=0}
=(2k+8)(2k+7)\frac{D_{2,k}}{D_{3,k+1}}c_{k+4}
+\mathcal R_k(c_0,\ldots,c_{k+3}).} \tag{6}
\]
The lower rational expression is fixed explicitly by (5): it is
\(\dot D_{3,k-1}/D_{3,k-1}+\dot D_{3,k+1}/D_{3,k+1}-2\dot D_{3,k}/D_{3,k}\)
with just the displayed \(c_{k+4}\) term subtracted. This is a finite algebraic prescription, not a new unknown function. The coefficient of \(c_{k+4}\) is strictly positive using accepted lower-order inputs. Equation (6) does not determine the sign of the full derivative.

The exact connection with the unchanged Mellin comparison is
\[
Q_{3,k}=B_{3,k}\eta_k,\qquad
B_{3,k}=\frac{(2k+6)(2k+5)}{2k(2k-1)}.
\]
Thus the proposed Gaussian estimate requires \(\eta_k\le k/(k+3)\) at \(\tau=0\). Equation (6) supplies no such upper bound, and no independent heat-time starting bound was obtained. The factorials and the distinction between \(c_n\) and \(b_n\) have not disappeared. No carrier partition function or squared amplitude replaces the signed \(M_3\) in this comparison.

The [finite exact checker](../numerics/mc05_b01_heat_cofactor_check.py) verifies the two upper-right cofactor cases \((r,k)=(3,1),(3,2)\). The general formula is proved by the unique position of the largest index, not extrapolated from those two checks.

## 4. A precise finite-closure obstruction, including the accepted local signs

Fix \(N\ge1\) and a compact interval \([a,b]\subset(0,\infty)\). Choose a nonzero nonnegative \(\psi\in C_c^\infty((a,b))\) and define on the half-line
\[
\delta\Phi=\frac{d^{2N+2}\psi}{du^{2N+2}}.
\]
Extend it evenly; it is identically zero near zero and outside a compact set. For \(\Phi_\epsilon=\Phi+\epsilon\delta\Phi\), repeated integration by parts has no boundary terms and gives exactly
\[
\delta c_n=0\quad(0\le n\le N),\qquad
\delta c_{N+1}=\epsilon\int_a^b\psi(u)\,du. \tag{7}
\]
The derivative order is even, so the sign is positive. Because \(\Phi\) has a positive minimum on the perturbation support, sufficiently small positive and negative \(\epsilon\) retain positivity. They also retain smooth evenness, the identical origin germ and the identical canonical exterior tails.

More strongly, the accepted \(R'>0\) and \(K>0\) survive for sufficiently small \(|\epsilon|\). On a fixed compact interval containing the support and lying away from zero, the original strict inequalities have positive minima. Their expressions depend continuously on a finite jet of a positive source (through order seven for \(K\)); the perturbation is small in that finite jet norm after multiplying by sufficiently small \(\epsilon\). Outside that interval the source is exactly unchanged. This is a compact continuity argument, not an uncomputed assertion that every old collision control has increasing \(R\).

The finite prefix \(t_1,\ldots,t_N\) is unchanged, but \(\delta t_{N+1}=\delta c_{N+1}/c_0\). Equation (4) therefore gives
\[
\delta\dot t_N=2(N+1)(2N+1)
\frac{\epsilon\int\psi}{c_0}\ne0. \tag{8}
\]
Hence **no deterministic universal finite-prefix closure of (4) follows from these finite coefficients, positive smooth even source, identical exterior tails, and the qualitative strict \(R'/K\) signs alone**. The altered source is not canonical theta: its global square-spectrum/modular identity is absent. A theta-specific relation using that additional infinite information is not excluded.

For the actual consumer, take \(N=k+3\). Then \(\eta_k\) and every coefficient in the prefactor and lower expression of (6) are unchanged, while
\[
\delta\left(\partial_\tau\log\eta_k\right)
=(2k+8)(2k+7)\frac{D_{2,k}}{D_{3,k+1}}
\epsilon\int\psi. \tag{9}
\]
This proves nonuniqueness of the derivative from that data. It does **not** prove that its sign can be reversed by an arbitrarily small perturbation, rule out a useful inequality, or exhibit a collision. The actual complete theta source fixes every coefficient; the missing step is a usable independent constraint on them, not an ambiguity in the canonical definition.

## 5. The same deformation defines a normalizable quantum oscillator state

The selected source heat flow admits a direct physical dictionary beyond naming a determinant identity. Let \(\{|m\rangle:m\ge0\}\) be the one-mode oscillator number basis and \(a|m\rangle=\sqrt m|m-1\rangle\). Define the unnormalized even vector
\[
|\chi_\tau\rangle=\sum_{n\ge0}\frac{b_n(\tau)}{\sqrt{(2n)!}}|2n\rangle
=\sum_{n\ge0}\sqrt{(2n)!}\,c_n(\tau)|2n\rangle. \tag{10}
\]
It is a genuine Hilbert-space vector, not a formal Fock symbol. Tonelli gives
\[
\begin{aligned}
\mathcal N_\tau^2:=\|\chi_\tau\|^2
&=\sum_{n\ge0}\frac{b_n(\tau)^2}{(2n)!}\\
&=\int_0^\infty\!\int_0^\infty
 e^{\tau(u^2+v^2)}\Phi(u)\Phi(v)\cosh(uv)\,du\,dv\\
&\le\left[\int_0^\infty e^{(\tau+1/2)u^2}\Phi(u)\,du\right]^2<\infty.
\end{aligned} \tag{11}
\]
Here \(\cosh(uv)\le e^{uv}\le e^{(u^2+v^2)/2}\). The last integral is finite for every finite real \(\tau\) by the complete double-exponential theta tail. Also \(\mathcal N_\tau>0\). Set \(|\psi_\tau\rangle=|\chi_\tau\rangle/\mathcal N_\tau\).

For real-amplitude normalized coherent states \(|u\rangle\), an equivalent convergent Bochner integral is
\[
|\chi_\tau\rangle=\frac12\int_0^\infty
\Phi(u)e^{(\tau+1/2)u^2}(|u\rangle+|-u\rangle)\,du. \tag{12}
\]
This is a coherent superposition of even coherent-state pairs, not a positive classical mixture. The same complete theta source supplies its amplitude. The source tail bounds its vector norm integral, and all fixed extra powers of \(u\) are still integrable.

In the Segal–Bargmann, or stellar, convention
\(\mathcal B_\psi(z)=\sum_m\psi_m z^m/\sqrt{m!}\), the unnormalized entire function is exactly
\[
\mathcal B_\tau(z)=\sum_{n\ge0}c_n(\tau)z^{2n}
=F_\tau(z^2)=\int_0^\infty e^{\tau u^2}\Phi(u)\cosh(zu)\,du. \tag{13}
\]
This convention and the coherent-state/Husimi relationship are inspected in Chabaud–Markham–Grosshans, [arXiv:1907.11009v3, Definition 1 and (1)–(3)](https://arxiv.org/pdf/1907.11009v3), PDF p.2. The present state, normalization and heat identities are derived explicitly here; no theorem about finite stellar rank is applied to theta.

The inherited normalization is \(H(0,x)=\xi(1/2+ix/2)/8\). Analytic continuation gives
\[
\mathcal B_0(z)=\frac18\xi((1+z)/2). \tag{14}
\]
For a coherent-state amplitude \(\alpha\in\mathbb C\), the normalized state's Husimi function is
\[
Q_{\psi_0}(\alpha)
=\frac{e^{-|\alpha|^2}}{\pi\mathcal N_0^2}
\left|\mathcal B_0(\overline\alpha)\right|^2. \tag{15}
\]
The conjugation is part of the convention; it does not change the imaginary axis. Therefore the exact physical restatement is
\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
\text{all zeros of }Q_{\psi_0}\text{ lie on the imaginary quadrature axis }\Re\alpha=0.} \tag{16}
\]
Equivalently the coherent-state probability is strictly positive off that axis. Nonnegativity of \(Q\) is automatic and proves none of this zero-location statement. Equation (16) is a reformulation with infinitely many phase-space locations, not a finite experimental criterion. The original signed determinant remains the Mellin consumer in Section 3; its replacement by the square in (15) would change that question.

The state construction supplies an exact quantum-state setting, observable and all-domain normalizability proof. It makes quantum-optical zero geometry available as a language/toolset to investigate, but no zero-confinement theorem, physical preparation protocol or novelty in the literature is claimed.

## 6. Exact oscillator dynamics and the missing positivity-preserving direction

Equation (1), or the coherent-state eigenvalue \(a^2|\pm u\rangle=u^2|\pm u\rangle\), gives
\[
\boxed{\partial_\tau|\chi_\tau\rangle=a^2|\chi_\tau\rangle,
\qquad \partial_\tau\mathcal B_\tau=\partial_z^2\mathcal B_\tau.} \tag{17}
\]
All fixed powers of \(a^2\) are defined on these vectors: add the corresponding powers of \(u,v\) in (11), still dominated by the source tails. Differentiation in vector norm follows from (12). Thus the unbounded generator is used on an explicit invariant analytic orbit, not asserted to generate a bounded semigroup on the whole oscillator Hilbert space.

This is a **one-sided, nonunitary quadratic flow**. The normalized vector obeys
\[
\partial_\tau|\psi_\tau\rangle
=(a^2-\operatorname{Re}\langle\psi_\tau,a^2\psi_\tau\rangle)|\psi_\tau\rangle.
\]
The expectation is real here. Unitary squeezing instead involves the adjoint creation term as well: its generator has the form \((\zeta a^2-\bar\zeta a^{\dagger2})/2\), as displayed in the same primary paper, PDF p.3. Adding that term would change (1) and the source orbit. No unitary or trace-preserving quantum-channel conclusion is imported for (17).

Even positive coefficients and a legitimate oscillator orbit do not justify carrying real-zero/axis confinement backward. A fixed exact polynomial example under (1) is
\[
F_\tau(w)=(1+2\tau+12\tau^2)+(1+12\tau)w+w^2. \tag{18}
\]
At \(\tau=0\), its discriminant is \(-3\); at \(\tau=1\), it is \(109\), and both roots of \(w^2+13w+15\) are negative. Thus \(F_1(z^2)\) has purely imaginary zeros while \(F_0(z^2)\) does not. Both describe finite, normalizable even Fock vectors; their displayed ordinary coefficients are positive. The [exact checker](../numerics/mc05_b01_heat_cofactor_check.py) records this finite witness.

**This is only a positive-coefficient polynomial/finite-Fock control.** It cannot be the complete moment transform of a positive half-line density, because its higher moments vanish. It proves no failure on the canonical theta orbit and no claim about a smooth-source collision. It does establish why a generic physical Hilbert space or a quadratic-flow label supplies no reverse positivity theorem. Together with (7)–(9), the selected mechanism stops at a precise initial-data/closure obligation rather than an assumed positive Toda cone.

## 7. Boundary and control accounting

The source heat family and oscillator construction cover all finite real \(\tau\). Their existence is not an \(s\)-Mellin curvature bound. Original coefficient identities and the target remain at \(\tau=0\). The signed order-three carrier/insertion representation from the frozen baseline is retained in \(Q=B\eta\); no new real-\(s\) integration by parts is required. The comparison is unpaid on \([0,2]\), every remaining compact Mellin interval and unbounded \(s\). No spatial or parameter tail estimate for that comparison was acquired.

At zero, smooth evenness and \(u^{2n}\) integrability justify (1); fixed logarithmic Mellin insertions remain integrable as in the baseline. Full double-exponential tails justify all coefficient sums, source derivatives in \(\tau\), Fock norms and parameter differentiation on compact \(\tau\) sets. The perturbation proof has compact support away from zero, so it adds neither origin nor tail boundary terms. All collision-face factors in the original \(M_3\) remain unchanged; no divided factor is removed in this branch.

| Control/family | Claim-specific screen |
| --- | --- |
| Gaussian | Gives the inherited Gaussian determinant normalization. A Gaussian source does not automatically define (10) without a width condition: (11) uses the stronger actual theta tail. It is not used as a Hilbert-space counterexample outside its convergence domain. |
| Two-point association relaxation | Does not realize this coefficient/source orbit; continues to screen association-only inference about \(M_3\), not the new exact oscillator construction. |
| Compact perturbation (7) | Preserves the named finite prefix, smooth even positivity, exact exterior tails and strict \(R'/K\) signs by proof. Fails literal canonical spectrum/source identity. Establishes finite-prefix nonclosure only; no collision or sign reversal claimed. |
| Quartic finite-Fock witness (18) | Passes the exact heat generator, Hilbert normalizability and the displayed positive coefficients; fails a positive full moment-source realization. Screens generic reverse flow claims only. |
| Modified Euler-factor | Changes the complete arithmetic/source identity. Heat/coefficient algebra remains generic; suitable shifted double-exponential tails also permit (10). No quantitative Mellin sign is assigned. |
| Weighted-square / finite-prime perturbations | Change unit spectral weights and in the cited controls fail full normalized reflection; finite-source instances still permit the oscillator construction by their tails. Generic heat/Schur identities do not exclude them. |
| Reflected super-Gaussian / shape / positive-primitive controls | Do not supply the literal canonical square expansion. Algebra (1) holds where heat moments exist. Fock normalizability must be checked from the particular control's tail; it is not assigned to the entire family without that check. No curvature sign is inferred from its positive-time collision. |

The physical-axis criterion is the full zero-location problem, whereas the known PF-infinity formulation requires **all finite Toeplitz minors**. The finite rectangles in this pilot are only a selected family; no theorem upgrading them to all minors is silently assumed. Classical heat-flow and fermionic/integrable descriptions can be useful without proving the theta specialization lies in the positive cone.

## 8. Stop and next recommendation

The new usable algebra is the source-compatible Schur-time evolution and the explicit higher-coefficient term (6), with the scoped nonclosure proof (7)–(9). The physical return is the normalizable theta oscillator state (10)–(15), its exact one-sided quadratic dynamics, and the axis-confinement reformulation (16). Neither return bounds the complete signed Mellin response. This completes one selected mechanism; it does not authorize a coefficient campaign, hierarchy truncation, quantum simulation or another conceptual search round.

**Next: [E] MC05-E01 — Sol**, separate fixed checking: verify (1)–(9), including the perturbation's preserved signs and its exact scope; replay only the two cofactor cases and quartic witness; check (10)–(17), all factorials, coherent-state conjugation, \(\xi\) scaling, norm/domain proof and nonunitary-versus-squeezing distinction. Check the source inspection limits and all-minor qualification. Accept these exact identities/reformulation/scoped obstruction, correct them, or mark a named issue unresolved. No claim to the Gaussian bound is an acceptance condition.
