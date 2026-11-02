# MC02-B01: a bounded fermionic transfer and its self-adjointness obstruction

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributor `/root/mc03_response`, assigned the disjoint second-wave MC02 task; actual recorded **gpt-6-astra (Codex), reasoning effort ultra**, session `01a19a49-d2ca-7ab1-b502-4e2795ee4f33`, turn `01a19a4e-0183-7c43-8521-ed04982e31c6`. This authoring return awaits separate internal checking and is not specialist review. The worker's earlier MC03 return is frozen and supplies no premise here.

**Disposition: bounded assessment complete.** The unchanged orbital pairing has an exact realization as a bounded, number-preserving free-fermion transfer on a half-infinite lattice. Using the established coefficient-total-positivity bridge, **RH is equivalent to nonnegativity of every occupation-basis amplitude in every finite particle sector of this fixed transfer**. All arbitrary ordered minors are retained. This is an explicit physical reformulation, not a new RH criterion or a positivity proof, and no novelty is claimed.

A selected mechanism for obtaining the signs from a positive equilibrium transfer **fails for the actual canonical coefficients**: an invariant two-site Jordan block prevents this exact transfer from being self-adjoint in any positive-definite inner product containing those states. A separate exact relaxation shows that nonnegative one-particle weights and contraction bounds alone do not sign two-fermion amplitudes. Neither obstruction rules out non-Hermitian transfer methods, other physical realizations, or the required theta inequalities. **No new Mellin comparison is proved.**

| Next task | Type and recommendation | Ready / dependency | Fixed output |
| --- | --- | --- | --- |
| MC02-E01, separate checking of this frozen return | E — Sol; the formulas, finite block and interpretation are specified | Ready after coordinator allocation to another worker | Check normalization, boundedness, exterior-power domain, arbitrary-minor RH quantifiers, two-site obstruction and the exact neighboring-index consumer. Accept, correct or leave unresolved; no new search or numerical campaign. |

The single selected candidate is a **coefficient-transfer realization followed by a positive self-adjoint transfer comparison**. No second mechanism is developed. The physical reformulation is kept as a useful result even though the proposed positivity shortcut fails. Read with the [result index][results], [physical-channel lessons][physical], [controls][controls], [avoid index][avoid], [reformulation rule][reformulation], [re-realizations][rerealization], [joint estimates][joint] and [scoped exclusions][scopes].

## 1. From the unchanged two orbital families to every ordered minor

Use the complete canonical source at physical heat time zero,
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,
\]
with \(c_n=0\) for negative integers. All \(c_n>0\) for \(n\ge0\). These are ordinary coefficients, not the raw moments or \(n!c_n\).

On \(L^2((0,\infty),du)\), retain the two original families
\[
f_i=\frac{\Phi^{(2i)}}{\sqrt\Phi},\qquad
g_j=\frac{u^{2j}\sqrt\Phi}{(2j)!},\qquad i,j\ge0.
\]
For each finite pair they belong to the Hilbert space. Complete evenness removes the required odd origin boundary terms; full-source decay removes the outer boundary terms. The existing exact integration-by-parts identity is
\[
\langle f_i,g_j\rangle=c_{j-i}. \tag{1}
\]
For arbitrary strictly increasing finite lists
\(I=(i_1<\cdots<i_r)\), \(J=(j_1<\cdots<j_r)\), define
\[
C_{I,J}=\det[c_{j_b-i_a}]_{a,b=1}^r
=\langle f_{i_1}\wedge\cdots\wedge f_{i_r},
g_{j_1}\wedge\cdots\wedge g_{j_r}\rangle. \tag{2}
\]
The wedge convention has unit-norm wedges of orthonormal vectors; reversing the annihilator order gives the same determinant in the empty-vacuum CAR formula. In particular, \(r=1\) gives (1), while \(r=2\) gives
\(c_{j_1-i_1}c_{j_2-i_2}-c_{j_2-i_1}c_{j_1-i_2}\).
The rectangular pilot is \(I=(0,1,2)\), \(J=(k,k+1,k+2)\), and equals \(D_{3,k}\).

No Gram substitution is made. The two orbital families differ, and the known negative region of the corresponding order-three spatial insertion remains part of these exact overlaps.

## 2. A bounded transfer on a specified lattice

Let
\[
F(z)=\sum_{n\ge0}c_nz^n,
\qquad v>0,\qquad p_n(v)=\frac{c_nv^n}{F(v)}.
\]
The source transform is entire, so \(F(v)<\infty\); \(p_n>0\) and \(\sum p_n=1\). The parameter \(v\) is a freely chosen positive coefficient scale, not physical heat time, thermal inverse temperature or the continuous Mellin parameter.

On the one-particle Hilbert space \(\ell^2(\mathbb N_0)\), let the backward shift satisfy \(Se_0=0\), \(Se_j=e_{j-1}\) for \(j\ge1\). Define
\[
\boxed{K_v=\sum_{n\ge0}p_n(v)S^n=\frac{F(vS)}{F(v)}.} \tag{3}
\]
This series converges absolutely in operator norm because \(\|S^n\|\le1\) and \(\sum p_n=1\). Thus \(\|K_v\|\le1\), and
\[
\langle e_i,K_ve_j\rangle=
\frac{c_{j-i}v^{j-i}}{F(v)},\qquad i,j\ge0. \tag{4}
\]
The negative-index convention is essential. On kets the transfer makes a nonnegative long-range left step, with loss at the left boundary. Each row sums to one and each column sums to at most one. No infinite-dimensional diagonal similarity is used to prove boundedness; the norm-convergent series (3) supplies it directly.

Equation (4) is also the exact pairing of the rescaled original orbitals
\(v^{-i}f_i\) and \(v^jg_j/F(v)\). This is an equality of finite matrix elements, not a claim that either infinite orbital family is an orthonormal basis or that its analysis map is bounded or unitary.

For each finite \(r\), \(\bigwedge^rK_v\) is a bounded contraction on the fermionic \(r\)-particle space. On full number-preserving Fock space,
\[
\mathcal F_-\bigl(\ell^2(\mathbb N_0)\bigr)
=\bigoplus_{r=0}^\infty\bigwedge^r\ell^2(\mathbb N_0),\qquad
\Gamma(K_v)=\bigoplus_{r=0}^\infty\bigwedge^rK_v
\]
is also a contraction, with the vacuum block equal to one. There is no Bogoliubov mixing, infinite current construction, filled-sea limit or unproved implementability assumption here. Boundedness follows sector by sector and then by the Hilbert direct sum.

For the fixed increasing-order occupation basis \(|I\rangle\), exterior algebra gives
\[
\boxed{\langle I|\Gamma(K_v)|J\rangle
=\frac{v^{\sum_bj_b-\sum_ai_a}}{F(v)^r}\,C_{I,J}.} \tag{5}
\]
All factors outside \(C_{I,J}\) are strictly positive. This is a completely specified **one-step free-fermion transfer theory**, generally non-Hermitian and long range. It does not assert a local interacting action, unitary real-time dynamics, a self-adjoint Euclidean Hamiltonian, or topological protection.

## 3. The RH reformulation and what it contributes

The existing [RH-formulation note][rh-note] and its [primary-source record][rh-source] identify the ordinary coefficient sequence as the PF-infinity target. The normalization can be checked explicitly against Katkova's equations (3)–(6): her coefficients satisfy \(b_n=8\cdot4^n c_n\), so
\[
F(z)=\tfrac18\xi\left(\tfrac12+\tfrac12\sqrt z\right).
\]
Evenness removes the square-root ambiguity. Positive geometric scaling and a positive overall factor do not change signs of Toeplitz minors. For this entire order-one-half function, the classical ASWE/Theorem C bridge gives the already established equivalence with all negative-real zeros. The inspected source is [Katkova, *Multiple positivity and the Riemann zeta-function*, version 1, Definition 2, Theorem ASWE and Theorem C](https://arxiv.org/html/math/0505174v1).

Combining that bridge with (5), stated once with the full quantifiers,
\[
\boxed{\mathrm{RH}\ \Longleftrightarrow\
\langle I|\Gamma(K_v)|J\rangle\ge0
\quad\text{for every finite }r\ge1
\text{ and all increasing }I,J\subset\mathbb N_0.} \tag{6}
\]
**Any one fixed \(v>0\) suffices.** If (6) holds for one such \(v\), (5) gives all coefficient minors and hence it holds for every \(v>0\). This is entrywise positivity in a specified occupation basis, not positive semidefiniteness of the operator and not ordinary reflection positivity of a state.

The nontrivial organizational value is that the entire RH family now lives in the sectors of one explicitly constructed bounded transfer: no separate physical model is invented for each minor, and the amplitude signs are the signs generated by fermionic antisymmetrization of a nonnegative one-particle step distribution. The physical question is whether theta's particular step weights remove all of these determinant signs. The required answer remains exactly the original all-minors condition; the reformulation is not counted as progress proving it. No originality or literature-priority claim is made.

The two free-fermion realizations complement one another. In (2), theta appears in the source-derived external wavefunctions on a continuous half-line. In (3)–(6), the same finite amplitudes appear in a bounded lattice transfer. Neither construction supplies an independent all-sector sign theorem. Restricting (6) to rectangles, to any fixed particle number, or to large displacement would lose quantifiers and would require an additional applicable theorem to recover RH. No such replacement is used here.

## 4. Actual-theta obstruction to a self-adjoint transfer mechanism

The selected positivity mechanism asks whether this exact transfer can be regarded as \(e^{-\tau H}\), \(\tau>0\), for a self-adjoint Hamiltonian in some positive Hilbert metric, so that standard positive-equilibrium transfer arguments become available. It already fails on the **actual** two-site invariant subspace
\(E=\operatorname{span}\{e_0,e_1\}\).

Indeed (3) gives
\[
K_v|_E=B=\begin{pmatrix}d&b\\0&d\end{pmatrix},
\qquad d=\frac{c_0}{F(v)}>0,\quad b=\frac{vc_1}{F(v)}>0. \tag{7}
\]
Suppose an inner product on this subspace has positive-definite Hermitian matrix
\(G=\begin{pmatrix}\alpha&z\\\bar z&\delta\end{pmatrix}\), with \(\alpha>0\), and makes \(B\) self-adjoint. Then \(GB=B^*G\). Its \((1,2)\) entry requires
\[
\alpha b+zd=dz,\qquad\text{hence}\quad\alpha b=0,
\]
a contradiction. Equivalently, a nontrivial finite Jordan block cannot be self-adjoint in a positive-definite inner product.

This also excludes a positive Hilbert metric on the full state space that both contains \(e_0,e_1\) as finite-norm states and makes this exact \(K_v\) self-adjoint: its restriction to the invariant subspace would satisfy the same impossible identity. An unbounded metric excluding those states would discard required amplitudes and is outside the claimed matching.

**Scope.** The obstruction is to a *single exact self-adjoint transfer* equal to (3), including a change to any positive-definite metric retaining the two-site states. It does not exclude a product of different transfers, a time-dependent construction, a larger dilation with extra states, a different reflection pairing of external fields, or a non-Hermitian/chiral realization. It is not an obstruction to total positivity: the Gaussian coefficient sequence also has \(c_1>0\), satisfies the same Jordan obstruction, and is PF-infinity. Thus the obstruction cannot be read as evidence against RH.

## 5. Why a positive one-particle contraction does not pay the signs

Even without self-adjointness, one might hope that \(p_n\ge0\), \(\sum p_n=1\), and \(\|\Gamma(K_v)\|\le1\) control the required amplitudes. A finite exact relaxation disproves that inference.

Take the generating polynomial \(F_*(z)=1+z+2z^2\) and \(v=1\). Its one-particle weights are \((1/4,1/4,1/2)\), hence its transfer is a nonnegative contraction by exactly the same proof as (3). But
\[
\langle 0,1|\Gamma(K_*)|1,2\rangle
=\det\begin{pmatrix}1/4&1/2\\1/4&1/4\end{pmatrix}
=-\frac1{16}. \tag{8}
\]
The underlying unscaled minor is \(1^2-1\cdot2=-1\). This is an algebraic transfer relaxation, not a theta source, a smooth-source collision control, or a counterexample to any accepted theta sign. Its failed premise is the unchanged canonical coefficient reconstruction. It shows precisely that the generic operator properties proved above do not supply the needed fermionic signs.

The same distinction applies to a Cauchy–Schwarz estimate for the original overlap. Such a bound controls its absolute magnitude; it does not sign it, give a positive lower bound, or compare neighboring ratios with a small denominator. Squaring the amplitude would remove the sign by changing the observable and is not done.

## 6. Exact consumer for the Mellin pilot

Write the actual rectangular amplitude
\[
a_{r,k}(v)=\langle 0,\ldots,r-1|\Gamma(K_v)|k,\ldots,k+r-1\rangle
=\frac{v^{rk}}{F(v)^r}D_{r,k}. \tag{9}
\]
The positive rescaling cancels from the neighboring ratio. At \(r=3\), \(k\ge1\), the original integer Mellin identity therefore gives
\[
Q_{3,k}=B_{3,k}
\frac{a_{3,k-1}(v)a_{3,k+1}(v)}{a_{3,k}(v)^2},\qquad
B_{3,k}=\frac{(2k+6)(2k+5)}{2k(2k-1)}. \tag{10}
\]
Consequently the sufficient integrated Gaussian comparison would require
\[
\frac{a_{3,k-1}(v)a_{3,k+1}(v)}{a_{3,k}(v)^2}
\le\frac{k}{k+3}. \tag{11}
\]
This is the precise missing amplitude estimate for the selected operator. The contraction bound only supplies \(|a_{r,k}|\le1\); it does not imply (11). No quantitative bound on (11) follows from the Jordan calculation or from merely reconstructing the exact weights.

The complete real-Mellin observable remains
\[
M_3(s)=\langle F_3,e^{s\widehat T}B_3\rangle,\quad
\widehat T=2\sum_j\log u_j,
\]
with distinct continuous-space bra and ket. Its exact response retains
\[
\mathcal C_3=
\operatorname{Var}_sT+
\frac{\operatorname{Cov}_s(h_3,(T-E_sT)^2)}{E_sh_3}
-\left(\frac{\operatorname{Cov}_s(h_3,T)}{E_sh_3}\right)^2.
\]
Nothing in (3) identifies variation of \(v\) with variation of \(s\). Extending (9) formally to noninteger indices would not supply that bridge and is not attempted. The negative insertion is unchanged. The pointwise Gaussian bound, its triangularly integrated bound, and the weaker exact next-determinant sign condition retain their original hierarchy.

## 7. Domains, controls and disposition

All source orbitals and CAR products in (1)–(2) use only finite indices, with complete endpoint and tail payments inherited from the accepted representation. The discrete transfer (3) is bounded on the whole one-particle Hilbert space, and the direct sum on Fock space is bounded on its full Hilbert domain. Infinite particle configurations or a filled Fermi sea are not included; RH requires arbitrarily large **finite** sectors, which are included. The invariant two-site argument is finite and needs no asymptotic or discretization.

No statement here proves the curvature comparison for \(s\in[0,2]\), any other compact range, or the unbounded range. All coefficient indices, including the separate triangular \(k=0\) anchor, remain in their original normalization. No source derivatives or numerical campaigns are escalated.

| Control | Premise and scope |
| --- | --- |
| Gaussian source | Gives the known normalized equality case and PF-infinity; it nevertheless has the same Jordan obstruction. This separates nonnegative fermionic amplitudes from self-adjointness of this chosen transfer. |
| Polynomial relaxation (8) | Passes nonnegative one-particle weights and all contraction constructions; fails the all-minor sign already in a two-particle amplitude. It lacks canonical source reconstruction. |
| Euler-factor controls | The generic orbital construction applies under the same smooth-even decay hypotheses; unchanged theta coefficients fail. Their all-sector amplitude signs are not assigned here. A positive-time collision alone gives no time-zero minor sign. |
| Weighted-square / finite-prime controls | They change the canonical weights; full evenness or the required origin endpoints may fail, so (1) cannot be imported wholesale without retaining boundary terms. A coefficient-transfer construction still applies when its coefficient generating sum is finite and positive. No derivative-ratio monotonicity or all-minor outcome is asserted. |
| Reflected super-Gaussian and smooth positive-primitive controls | Generic finite orbital and transfer encodings survive where their integrability hypotheses hold; unchanged theta reconstruction fails. Encoding them is not a successful discriminating screen. No uncomputed transfer inequality is assigned. |
| Two-point association relaxation | Continues to defeat association-only Mellin arguments, but is not a common Toeplitz/orbital realization; it is not used to infer anything about (6). |

The new mathematical obstruction is precisely (7), and the physical reformulation is (3)–(6). No source-specific signed estimate survives from the attempted positive-equilibrium mechanism. Keeping this distinction follows the author's request to preserve useful physical formulations even when they do not advance the Mellin comparison.

## 8. Frozen support and inputs

The [finite exact checker][check] and [record][record] retain the one declared relaxation (8), positive rescaling and an illustrative rational commutator evaluation. The universal metric obstruction is the symbolic proof in Section 4, not inferred from a sampled metric. The script performs no theta evaluation, coefficient acquisition, precision sweep, root test or numerical campaign.

Actual launch inputs were checked against the [parent frozen record][launch] and were unchanged. The additional existing RH-normalization note and source record are hashed below; no sibling return supplied a mathematical premise.

| Input | SHA-256 |
| --- | --- |
| Local overview | `2286592673dcd573790e828550f24d8fc343f98dfd77fc13514dfebcde0815ce` |
| Initial Mellin assessment | `ee4280708b43d4d080fe98c128d58c0180f0ba0851b730bd859c2a899f84d9de` |
| Parent physical Note04 | `f4ff6338794cf359bf06ea6ec17867fd5aef44910de1796b3c26396f8fb5b720` |
| Continuation05 | `7cfa21664fe85e64749a7fc4e32c420300b8d91590f0dc62da35cf3816e677d7` |
| Existing RH-formulation note | `c5715d555194f7099f6b823e6701d8c4138e702062716ec30ed469a96c513223` |
| Existing RH-source record | `38e44a03382300ade81bb73669e7c2988cfb43b8e23f17bb88d0c926a2d96dd1` |

Katkova version 1 was reinspected in primary HTML for coefficient normalization, arbitrary-minor quantifiers and Theorem C; its full proof was not independently audited. The existing Alexandrov–Zabrodin finite-CAR reading record was reused; a fresh HTML request timed out, and no new infinite-current theorem is imported. The bounded transfer and exterior-power arguments here are given directly. The coordinator alone maintains common references and public history.

**Next: [E] MC02-E01 — Sol**, separate checking of the frozen formulas and scopes above. No second branch mechanism or new research campaign is launched by this return. Any later physical proposal must add an independently justified theta constraint beyond the equivalent all-sector positivity in (6), and must specify a consumer such as (11).

[results]: ../../../../../../../result-summaries/README.md
[physical]: ../../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[reformulation]: ../../../../../../../avoid/01_restating_the_target.md
[rerealization]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[joint]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scopes]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[rh-note]: ../../../../notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md
[rh-source]: ../../../../references/04_RH_FORMULATION_SOURCES_20261101.md
[check]: ../numerics/mc02_exact_transfer_check.py
[record]: ../numerics/MC02_B01_EXACT_RECORD_20261101.json
[launch]: ../../numerics/PARALLEL_PHYSICAL_LAUNCH_RECORD_20261101.json
