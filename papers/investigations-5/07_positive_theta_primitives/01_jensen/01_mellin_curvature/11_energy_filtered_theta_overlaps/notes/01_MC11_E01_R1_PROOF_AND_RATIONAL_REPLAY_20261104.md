# MC11-E01 r1 — proof checks and exact rational replay

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex), effort ultra**; thread `01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab`, turn `01a1a8e5-1f78-7db1-9405-1dfc9cf9d984`, MC11 chat0001.

**E01 r1 complete: all specified claims accepted on the inherited integration premises, without correction.** The analytical pass and [exact replay][record] assess the frozen starting derivation. They acquire no new integral and do not evaluate E02's spectral split. [Separate assessment][review] · [Live register][progress] · [Continuation/model change][handoff]

The originating filter/response derivation is Astra/xhigh; this is a different-model internal assessment of that derivation. The coordinator and one read-only proof contributor are both Sol/ultra. The saved numerical acquisition and its premises are shared, and the new replay implementation has coordinator checks. This is not independent specialist review or a fresh validation of Arb/FLINT integration.

## 1. Fixed source, filter, and overlap

The physical box has \(H=-\pi^{-1}\partial_x^2\), energies \(E_n=\pi n^2\), and filter effect \(W_s=P_1+s(I-P_1)\), \(0\le s\le1\). The amplitude is \(W_s^{1/2}\); the unnormalized accepted trace is \(e^{-\beta\pi}+s\sum_{n\ge2}e^{-\beta E_n}\). With \(\beta=e^{4u}\), applying \( (\partial_u^2-1)/8\) to \(p_E=e^{u-Ee^{4u}}\) gives
\[
\phi_E=e^u(2X^2-3X)e^{-X},\qquad X=Ee^{4u}.
\]
It is positive for the energies and half-line used. Hence \(\Phi_s=\phi_\pi+s\sum_{n\ge2}\phi_{E_n}>0\), and for \(j\ge1\),
\[
c_j(s)=b_j+s h_j,\quad b_j=a_j(\pi),\quad
h_j=\sum_{n\ge2}a_j(E_n)>0,\qquad
a_j(E)=\int_0^\infty\frac{u^{2j}}{(2j)!}\phi_E(u)\,du.
\]

For finite \(i,\ell\), the orbitals \(f_i^{(s)}=\Phi_s^{(2i)}/\sqrt{\Phi_s}\) and \(g_\ell^{(s)}=u^{2\ell}\sqrt{\Phi_s}/(2\ell)!\) belong to \(L^2(du)\). Positivity gives regularity at the origin; at infinity, each fixed derivative contributes polynomial factors in \(e^{4u}\) against double-exponential decay. The ground mode controls the denominator and the higher modes decay faster.

For \(0\le i<q\) and \(q\le\ell<2q\), transfer of \(2i\) derivatives gives \(\langle f_i^{(s)},g_\ell^{(s)}\rangle=c_{\ell-i}(s)\). Every inner endpoint term differentiates \(m_\ell=u^{2\ell}/(2\ell)!\) at most \(2i-1<2\ell\) times and vanishes. The outer endpoint vanishes by decay. Thus the ordered exterior overlap is exactly
\[
D_q(s)=\det[c_{q+j-i}(s)]_{0\le i,j<q}.
\]
No extra factorial is present under the usual exterior-inner-product convention. Filtered sources need not have canonical reflection: **only this diagonal block's pairing is accepted here**. The boundary-preserving Green interpolation adds \((1-s)\tau\delta_0\), but each block coefficient has index at least one and annihilates this atom. The statement does not extend this cancellation to blocks involving \(c_0\).

The overlap remains unnormalized. Dividing by the two wedge norms changes derivatives and fractional effects because those norms depend on \(s\). At \(s=1\), the inherited canonical generating function identifies this determinant with \(D_{q,q}\).

## 2. Propagating the saved allowance over the whole path

Use the manuscript's primitive moments
\[
x_j=\tfrac18\int_0^\infty m_jp_1,\quad
y_j=\tfrac18\int_0^\infty m_j\sum_{n\ge2}p_n,\quad
A_j=\tfrac18\int_0^2m_jp_1.
\]
The compact reference is \(c_0^*=1/16-A_0\), \(c_j^*=A_{j-1}-A_j\) for \(j\ge1\). The \(A_j\) are primitive integrals, not source moments \(a_j(E)\). The complete first-mode \(b_j\) and compact \(c_j^*\) are distinct.

Let \(r_j(s)=x_j-A_j+s y_j\). The inherited analytical energy and spatial bounds give \(0\le r_j(s)\le B_j(2)+E_j=T_j\), uniformly on the filter path. Green transfer with the untruncated source gives
\[
c_j(s)=c_j^*+r_{j-1}(s)-r_j(s),\qquad j\ge1.
\]
Also \(h_j=y_{j-1}-y_j>0\) by source positivity and
\[
|c_j(s)-c_j^*|\le T_{j-1}+T_j,\qquad
0<h_j\le E_{j-1}+E_j\le T_{j-1}+T_j.
\]
The looser sum bound is intentional; it covers both uses with the same saved allowance. It does not require treating the individual primitive differences as positive.

The [replay][code] reconstructs all six compact balls from their serialized dyadics, then \(c_0^*,\ldots,c_5^*\). It reconstructs both tails, retains the nonzero spatial exterior, and rounds their sums upward to the saved \(2^{-384}\) grid. Exact division by the lower endpoint of \(c_j^*\) gives allowances strictly below \(\epsilon=1/40000\), \(1\le j\le5\). The largest is the saved \(j=1\) allowance, about \(2.46623\times10^{-5}\); this reading is not an enclosure endpoint. Therefore
\[
|c_j(s)-c_j^*|\le\epsilon c_j^*,\qquad 0<h_j\le\epsilon c_j^*.
\]
No quadrature error is added again: it is already contained in the imported compact balls. The replay trusts those balls and the inherited bounds on \(E_j,B_j\); it does not reproduce their integration or transcendental evaluation.

The same reconstruction checks \(0<c_0^*<1/16\), \(c_1^*>1/3000\), and
\[
t_j=\frac{(c_0^*)^{j-1}c_j^*}{(c_1^*)^j},\qquad
t_2\in[.465,.466],\quad t_3\in[.135,.137],\quad
t_4\in[.028,.029],\quad t_5\in[.004,.005].
\]
Every decimal in these boxes denotes an exact rational.

## 3. Two-orbital sign and total fractional loss

For \(E\ge4\pi>25/2\), logarithmic differentiation yields
\[
-(\log\phi_E)'=F(X)=4X-9-\frac{12}{2X-3},\quad
F'(X)=4+\frac{24}{(2X-3)^2}>0,\quad
F(25/2)=445/11>40.
\]
Write \(J_m=\int_0^\infty u^m\phi_E/m!\). Integrating \(-\phi_E'\ge40\phi_E\) against \(u^m/m!\), \(m\ge1\), gives \(40J_m\le J_{m-1}\); both endpoints vanish. Since \(a_j=J_{2j}\), two recursions give \(a_2/a_1\le1/1600\).

The exact coefficient floor is
\[
\frac{c_3(s)}{c_2(s)}>
\frac{1-\epsilon}{1+\epsilon}\frac{.135}{.466}\frac{16}{3000}
=\frac{359991}{233005825}>\frac1{700}>\frac1{800}
\ge\frac{2a_2(E)}{a_1(E)}.
\]
Consequently, in
\[
\chi_2(E;s)=2c_2(s)a_2(E)-c_3(s)a_1(E)-c_1(s)a_3(E),
\]
the first exchange term already exceeds the direct term and the last term is strictly negative. This proves \(\chi_2(E_n;s)<0\) for every excited level and every \(s\in[0,1]\).

With \(R=c_1^*c_3^*/(c_2^*)^2=t_3/t_2^2\le5480/8649<16/25\),
\[
\frac{D_2(0)}{(c_2^*)^2}\ge(1-\epsilon)^2-(1+\epsilon)^2R
\ge\frac{5069269683169}{13838400000000}>\frac7{20}>0.
\]
At fixed order, the moment sums converge absolutely, the cofactors are bounded on \([0,1]\), and the derivative is a finite polynomial in those entries. Thus differentiation and integration of the response sum are justified without matrix invertibility. Integrating the exact derivative retains every mixed term:
\[
0<D_2(0)-D_2(1)
\le\int_0^1[c_3(s)h_1+c_1(s)h_3]ds
\le2\epsilon(1+\epsilon)c_1^*c_3^*.
\]
The replay gives
\[
0<\frac{D_2(0)-D_2(1)}{D_2(0)}
<\frac{5480137}{60543000000}
<\frac{40001}{437500000}<10^{-4}.
\]
The last coarse upper bound is about \(9.143086\times10^{-5}\), a conservative consequence rather than a measured loss. Positivity of the endpoint follows from this reference floor and loss bound, within an already-known fixed positivity range.

## 4. Three-orbital corner and high-energy limit

For \(I_h(E)=\int m_hp_E\), Green transfer gives \(8a_j=I_{j-1}-I_j\), \(j\ge1\). Setting \(v=4Eu\), the rescaled integral for \(I_h\) converges to \(\int_0^\infty v^{2h}e^{-v}/(2h)!\,dv=1\). For \(E\ge1\), the tangent bound on \(e^{v/E}\) dominates its integrand by \(v^{2h}e^{-3v/4}/(2h)!\). Dominated convergence therefore gives
\[
a_j(E)\sim\frac{e^{-E}}{8(4E)^{2j-1}},\qquad
\frac{a_j(E)}{a_1(E)}\longrightarrow0\quad(j>1).
\]

The only index-one entry of \(M_q=[c_{q+j-i}]\) is \((q-1,0)\). Its cofactor is \((-1)^{q-1}D_{q-1,q+1}\). The replay verifies the relevant permutation minors directly: at \(q=2\) it is \(-c_3\), and at \(q=3\),
\[
\operatorname{cof}_{20}M_3=\det\begin{pmatrix}c_4&c_5\\c_3&c_4\end{pmatrix}
=c_4^2-c_3c_5.
\]
At each fixed \(s\), the cofactor response formula thus gives
\[
\lim_{E\to\infty}\frac{\chi_3(E;s)}{a_1(E)}=c_4(s)^2-c_3(s)c_5(s).
\]
Factoring \(S=(c_1^*)^8/(c_0^*)^6>0\), the entire-path lower bound is
\[
\frac{c_4(s)^2-c_3(s)c_5(s)}S
\ge(1-\epsilon)^2(.028)^2-(1+\epsilon)^2(.137)(.005)
=\frac{158282480099}{1600000000000000}>0.
\]
Hence sufficiently high levels raise the overlap at each fixed filter setting. No explicit finite-energy cutoff, sign for \(n=2\), value of \(D_3(0)\), or sign of the complete \(D_3(1)-D_3(0)\) is supplied by E01.

## 5. Evidence, controls, and continuation

This is a **finite-order signed estimate**, not an RH-equivalent criterion. The useful outputs are its signed response and quantitative loss, rather than another realization of the target. The frozen request's five SHA-256 values all match; the [record][record] binds them, the new code hash, exact fractions, and the 87 checks. One replay took 0.004677291 seconds as reported by its timer, with zero integrand evaluations and zero corrections. Counts and precision are audit details, not proof of the analytical premises.

To reproduce the arithmetic from the repository root, use a fresh output path:

```sh
python3 papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/numerics/mc11_e01_r1_exact_replay.py --repo . --output /tmp/MC11_E01_R1_REPLAY_fresh.json
```

The checker refuses changed frozen inputs or an existing output file. No replay of the upstream integration is needed for this saved-data check.

The [result index][results] and [theta cluster][theta] locate the inherited results; [avoid/01][a01] and [avoid/05][a05] delimit reformulation and review claims. The [collision screen][controls] and [avoid/02][a02] apply as follows:

| Control | Premise not retained; conclusion of this screen |
| --- | --- |
| Weighted integer squares | Complete unit weights are changed. The gap-based single-level slope may survive, but the imported coefficient and margin bounds are not established for those weights. No computed failure of their inequalities is claimed. |
| Euler-factor source | The unchanged canonical box trace and source formula are not retained; the saved canonical input payment cannot simply be imported. |
| Reflected shape control | Reflection and positivity do not supply the literal unit-square trace or the saved coefficient payment. |
| Smooth positive-primitive control | Positive primitives and matching endpoints/asymptotics do not supply that trace or its quantitative moment bounds. |

Sources satisfying the same slope and coefficient inequalities share the fixed-order conclusions. Positive-time collisions in the controls do not contradict these time-zero bounds. The radial algebraic negative-diagonal examples have no asserted realization by this trace. No growing-order, neighboring-shift, or general impossibility conclusion is made; see [avoid/07][a07].

**Next: [E] MC11-E02 — Sol.** Use the accepted premises to split the three-orbital response into \(n=2\) and \(n\ge3\) along the same common \(s\) path, within the existing contract. The [handoff][handoff] lists the frozen versions, limits, acquisition gate, and model-change instructions. E03 remains conditional; B01 has no E01 structural gap to resolve.

[record]: ../numerics/MC11_E01_R1_EXACT_REPLAY_20261104.json
[code]: ../numerics/mc11_e01_r1_exact_replay.py
[review]: ../reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md
[progress]: ../research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md
[handoff]: ../research-progress/handoffs/01_MC11_E01_RETURN_AND_E02_MODEL_CONTINUATION_20261104.md
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
