# TND-D-E03 r1: complete high-count localization and signed-phase oscillation

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **E — execution**, frozen request **TND-D-E03 r1**. Requested and actual worker: **gpt-6.1-sol / ultra**. Actual settings were independently verified in the worker's local rollout `turn_context`, thread `01a1afd1-c30a-7ef0-8e40-fdc521a43a95`, turn `01a1afd1-c316-79d3-a555-8eddffaed70c`; source `/Users/ebbaker/.codex/sessions/2026/11/06/rollout-2026-11-06T02-45-22-01a1afd1-c30a-7ef0-8e40-fdc521a43a95.jsonl`. Agreement with the requested labels is not the evidence for the actual labels.

**Disposition: the r1 target is proved at proof-author level, pending the separately assigned E04 internal assessment.** The proof establishes a uniform second centered moment, compact-real-parameter cosine asymptotics, and both limiting signs in the literal count sectors. It excludes eventual one-sign sectors at each fixed nonzero real readout parameter. It supplies no collision exclusion, physical estimating gain, novelty claim or new access assumption.

The [frozen request][request], [input manifest][inputs] and [B02 decision][decision] fix the question. All seven manifest entries matched their complete SHA-256 and byte counts when consumed; manifest SHA-256 `13fa30a0ff764cedb863448313279ad4bfb32b6e3f517c7194de2a77c032f27a`. In particular the decision SHA-256 was `d1fef9e92bdf9de322036eca2fabe15032ab123b596a73b5221ef5f8843419ef`, and the request SHA-256 was `59e0519d4dae40f4a9a592be6e78ef8bd0f529586e7bc935c0b261f3a523b27f`. The decision's navigation-only issue does not alter the consumed mathematics; its frozen bytes were left intact. The complete-source/state inputs retain [E01][e01]/[E02][e02]'s existing internal conditional status. Only the count dictionary verified in section 1 below is consumed from the later [Note04][note04] and manuscript [section 5][count]; their other diagnostics are not assessed here.

**Finite work record:** one proof pass, reusing the existing B02-S1 feasibility derivation as expressly permitted by r1 rather than repeating it; one local correction/check pass documented in section 6. No numerical scan, imported theorem, recursive delegation, manuscript, registry or other shared-file edit. Primary Astra owns handoffs, integration and public chat capture. This note was returned for installation at the assigned Note06 path.

## 1. Count normalization from the unchanged signed amplitudes

Keep the complete radial source, its smooth full-line even extension and the accepted normalization

\[
 F_\lambda(v)=e^{\lambda v^2}\Phi(v),\quad
 H_\lambda(k)=\int_0^\infty e^{\lambda r^2}\Phi(r)\cos(kr)\,dr,
 \quad Z_\lambda=2H_\lambda(0).
 \tag{1}
\]

With fixed \(\gamma>0\), \(0\le t\le T=1/\gamma\), let \(\lambda(t)=1/2-\gamma t\). The initial radial vector is \(f_{1/2}(v)=Z_{1/2}^{-1/2}e^{v^2/4}\sqrt{\Phi(v)}\). The original Kraus operators and interaction-frame output vector are

\[
 K_j(t,0)=U(t)e^{-\gamma tX^2/2}
 \frac{(\sqrt{\gamma t}\,X)^j}{\sqrt{j!}},\qquad
 b_j(t,v)=e^{-\gamma tv^2/2}
 \frac{(\sqrt{\gamma t}\,v)^j}{\sqrt{j!}}f_{1/2}(v).
 \tag{2}
\]

For \(t>0\) this retains the sign of \(v^j\), including odd counts. Its squared modulus is exactly

\[
 |b_j(t,v)|^2=
 \frac{(\gamma t)^j}{j!Z_{1/2}}
 v^{2j}e^{\lambda(t)v^2}\Phi(v).
 \tag{3}
\]

The accepted angular ensemble is complete: its per-state weights are
\(r_m=e^{-\pi m^2}/(4mQ_1(\pi))\), with both angular signs and \(2m\) states per sign, so \(\operatorname{Tr}R=\sum_{m\ge1}4mr_m=1\). The count operator is radial and introduces no new angular multiplicity. In the interaction frame the output is \(|b_j\rangle\langle b_j|\otimes R\). Since \(Q_t=U(t)XU(t)^*\), bounded real functional calculus and trace cyclicity give

\[
\begin{aligned}
 P_j(t)&=\frac{(\gamma t)^j}{j!Z_{1/2}}
 \int_{\mathbb R}v^{2j}e^{\lambda(t)v^2}\Phi(v)\,dv,\\
 d_j(t,k)&=\frac{(\gamma t)^j}{j!Z_{1/2}}
 \int_{\mathbb R}v^{2j}e^{\lambda(t)v^2}\Phi(v)\cos(kv)\,dv,
 \qquad |d_j(t,k)|\le P_j(t).
\end{aligned}
 \tag{4}
\]

The complete angular trace is exactly one. The full-line factors of two, by evenness, cancel between the numerator and denominator. Thus, for every finite \(j\ge1\), real \(k\) and \(t>0\),

\[
 \frac{d_j(t,k)}{P_j(t)}
 =\mathbb E_{\nu_{j,\lambda(t)}}\cos(kr),\qquad
 \nu_{j,\lambda}(dr)=
 \frac{r^{2j}e^{\lambda r^2}\Phi(r)\,dr}
 {\int_0^\infty r^{2j}e^{\lambda r^2}\Phi(r)\,dr}.
 \tag{5}
\]

Here \(P_j(t)>0\): the source is strictly positive and the prefactor in (4) is positive. Equation (5) changes neither the physical normalization nor the absolute scale of (4).

For every fixed \(j\) and \(t>0\), \(b_j\) is a scalar multiple of \(v^jf_{\lambda(t)}\), hence is Schwartz by E01. Every fixed full-spectrum graph payment follows from the same complete binomial identity, for each integer \(p\ge0\):

\[
\begin{aligned}
 &\sum_{m\ge1}4mr_m\int_{\mathbb R}
 (\xi^2+4m^2)^{2p}|\widehat b_j(\xi)|^2\,d\xi\\
 &=\frac1{Q_1(\pi)}\sum_{\ell=0}^{2p}\binom{2p}{\ell}4^{2p-\ell}
 \|P^\ell b_j\|_2^2\sum_{m\ge1}m^{4p-2\ell}e^{-\pi m^2}<\infty.
\end{aligned}
 \tag{6}
\]

The angular tails are the actual Gaussian sums over \(m>N\), and radial spectral tails are bounded, for each fixed \(j,\ell,M\) and \(L>0\), by \(L^{-2M}\|P^{\ell+M}b_j\|_2^2\). Thus every finite count retains the complete radial spectrum and angular shells/signs. No constant in (6) is asserted uniform as \(j\to\infty\); the growing-order result below has its own scalar proof. At \(t=0\) use the original convention \(b_0=f_{1/2}\), \(b_j=0\) for \(j>0\).

## 2. Full-source comparability and the theorem

On \(r\ge0\), write \(x=\pi e^{4r}\). The unchanged source is

\[
 \Phi(r)=e^r\sum_{n\ge1}(2n^4x^2-3n^2x)e^{-n^2x}.
 \tag{7}
\]

All terms are positive for \(x\ge\pi\). Put

\[
 \kappa=2-3/\pi>0,\quad
 S=\sum_{n\ge1}n^4e^{-\pi(n^2-1)}<\infty,\quad
 c_-=\pi^2\kappa,\quad c_+=2\pi^2S.
\]

Keeping the first term as a positive lower bound and bounding the entire sum above gives

\[
 \kappa e^r x^2e^{-x}\le\Phi(r)\le2S e^r x^2e^{-x},
 \quad\text{hence}\quad
 c_-e^{9r-\pi e^{4r}}\le\Phi(r)\le c_+e^{9r-\pi e^{4r}}.
 \tag{8}
\]

The upper estimate uses \(e^{-(n^2-1)x}\le e^{-\pi(n^2-1)}\) and pays all \(n\ge1\); Gaussian summability makes \(S\) finite. This is not a replacement by a finite theta prefix. E01/E02 already pay the same matching source exponents. Only their zero-order bound is used in the new growing-\(j\) proof.

For each integer \(j\ge1\), let \(a_j>0\) be the unique solution

\[
 \frac{2j}{a_j}=4\pi e^{4a_j},\qquad
 j=2\pi a_je^{4a_j},\qquad
 M_j=\frac j{a_j},\qquad s_j=M_j^{-1/2}.
 \tag{9}
\]

**Theorem.** There are finite constants \(C_1,C_2\) and an integer \(J\), independent of \(j,\lambda,t,k,\gamma\), such that for \(j\ge J\),

\[
 \sup_{|\lambda|\le1/2}\mathbb E_{\nu_{j,\lambda}}|r-a_j|
 \le C_1\sqrt{a_j/j},\qquad
 \sup_{|\lambda|\le1/2}\mathbb E_{\nu_{j,\lambda}}(r-a_j)^2
 \le C_2a_j/j.
 \tag{10}
\]

For each finite \(K\), every real \(|k|\le K\) and every physical \(0<t\le T\),

\[
 \left|\frac{d_j(t,k)}{P_j(t)}-\cos(ka_j)\right|
 \le KC_1\sqrt{a_j/j}\longrightarrow0.
 \tag{11}
\]

For each fixed real \(k\ne0\) and every \(0<t\le T\),

\[
 \limsup_{j\to\infty}\frac{d_j(t,k)}{P_j(t)}=1,\qquad
 \liminf_{j\to\infty}\frac{d_j(t,k)}{P_j(t)}=-1.
 \tag{12}
\]

In particular, both signs occur infinitely often in the literal \(d_j(t,k)\). The subsequences realizing the two limits can be chosen independently of \(t\).

## 3. Complete centered-exponent proof

Fix \(j\) and abbreviate \(a=a_j\), \(M=j/a\), \(s=M^{-1/2}\). For \(r>0\) set

\[
 q_j(r)=2j\log r-\pi e^{4r},\qquad
 f_{j,\lambda}(r)=q_j(r)+\lambda r^2+9r.
\]

For \(h=r-a>-a\), (9) yields the exact identity

\[
 q_j(a+h)-q_j(a)
 =2j[\log(1+h/a)-h/a]
 -\frac M2[e^{4h}-1-4h].
 \tag{13}
\]

The logarithmic bracket is nonpositive. Write \(c_0=4e^{-4}\). Taylor's integral remainder and \(e^{-4u}-1+4u\ge3u\) for \(u\ge1\) give

\[
 q_j(a+h)-q_j(a)\le
 \begin{cases}
 -4Mh^2,&h\ge0,\\
 -c_0Mh^2,&-1\le h\le0,\\
 -\tfrac32M|h|,&-a<h\le-1.
 \end{cases}
 \tag{14}
\]

The half-line origin is included by the limiting zero density for \(j\ge1\). These are global interval estimates, not a local asymptotic expansion.

As \(j\to\infty\), (9) gives \(a\to\infty\) and \(M=2\pi e^{4a}\). Choose \(J\) large enough that every \(j\ge J\) satisfies

\[
 a\ge1,\qquad M\ge(a+9)^2/c_0.
 \tag{15}
\]

Exponential growth supplies such a fixed \(J\), with no computed cutoff. Since \(c_0<1\), (15) implies \(M\ge16\), \(M\ge2/c_0\), \(M\ge2a\), \(M\ge a^2\) and \(s\le1/4\).

For \(h\ge-1\), uniformly for \(|\lambda|\le1/2\),

\[
 \lambda(2ah+h^2)+9h\le(a+9)|h|+\tfrac12h^2,
\]

and completed squares give

\[
 (a+9)|h|\le\tfrac14c_0Mh^2+
 \frac{(a+9)^2}{c_0M},\qquad
 \tfrac12h^2\le\tfrac14c_0Mh^2.
\]

With \(c_1=c_0/2=2e^{-4}\), (14)--(15) therefore imply

\[
 f_{j,\lambda}(a+h)-f_{j,\lambda}(a)
 \le1-c_1Mh^2\qquad(h\ge-1).
 \tag{16}
\]

For \(h=-u\), \(1\le u<a\), the perturbation obeys
\(\lambda(-2au+u^2)-9u\le au\). Thus (14) and \(M\ge2a\) give

\[
 f_{j,\lambda}(a-u)-f_{j,\lambda}(a)\le-Mu
 \qquad(1\le u<a).
 \tag{17}
\]

Equation (17) pays the entire left tail, whose interval length grows with \(a\); (16) pays the entire unbounded right tail.

For the positive normalizer, restrict to \(0\le h\le s\). The elementary bounds

\[
 \log(1+y)-y\ge-y^2/2\quad(y\ge0),\qquad
 e^{4h}-1-4h\le8eh^2\quad(0\le h\le1/4)
\]

show that the two terms on the right of (13) are at least \(-1\) and \(-4e\), respectively. The perturbation is at least \(-ah-h^2/2\ge-3/2\). Consequently, with \(D=3+4e\),

\[
 f_{j,\lambda}(a+h)-f_{j,\lambda}(a)\ge-D\quad(0\le h\le s).
\]

By (8), the normalizing integral \(N_{j,\lambda}\) in (5) satisfies

\[
 N_{j,\lambda}\ge c_-e^{f_{j,\lambda}(a)}e^{-D}s.
 \tag{18}
\]

For \(p=1,2\), put \(A_p=\int_{\mathbb R}|z|^pe^{-c_1z^2}\,dz<\infty\). Splitting the whole numerator at \(h=-1\), then applying (16)--(17), gives

\[
\begin{aligned}
 &\int_0^\infty |r-a|^p r^{2j}e^{\lambda r^2}\Phi(r)\,dr\\
 &\quad\le c_+e^{f_{j,\lambda}(a)}
 \left[eA_pM^{-(p+1)/2}+\int_1^a u^pe^{-Mu}\,du\right]\\
 &\quad\le c_+e^{f_{j,\lambda}(a)}
 [eA_p+\Gamma(p+1)]M^{-(p+1)/2}.
\end{aligned}
 \tag{19}
\]

For the last line, extending the far-left integral to \([0,\infty)\) bounds it by \(\Gamma(p+1)M^{-(p+1)}\), which is at most the displayed term for \(M\ge1\). Here \(\Gamma(2)=1\) and \(\Gamma(3)=2\), so only elementary exponential integrals are involved.

Dividing (19) by (18) proves (10), for example with explicit finite constants

\[
 C_p=\frac{c_+}{c_-}e^D[eA_p+\Gamma(p+1)],\qquad p=1,2.
 \tag{20}
\]

The constants are deliberately coarse. They are uniform in \(|\lambda|\le1/2\) and all \(j\ge J\). Since \(M=2\pi e^{4a}\to\infty\), \(s\to0\). The growing-order proof uses the fixed zero-order comparability (8) and the inequalities (13)--(19), not order-uniform consequences of finite-order Schwartz estimates.

## 4. Cosine phase and exact derivative translation

The real cosine is Lipschitz: \(|\cos(kr)-\cos(ka)|\le|k||r-a|\). Equations (5) and (10) prove (11), uniformly on every compact real \(k\) set and the complete physical lambda slab.

For continuous positive \(j\), implicit differentiation in (9) gives

\[
 \frac{da}{dj}=\frac{a}{j(1+4a)}<\frac1{4j}.
\]

The centers are strictly increasing and unbounded, and their integer increments satisfy

\[
 0<a_{j+1}-a_j<\tfrac14\log(1+1/j)\le\frac1{4j}\longrightarrow0.
 \tag{21}
\]

Fix \(k\ne0\). For the targets \(b_m^+=2\pi m/|k|\), let \(j_m^+\) be the first index with \(a_{j_m^+}\ge b_m^+\). For large \(m\),

\[
 0\le a_{j_m^+}-b_m^+\le a_{j_m^+}-a_{j_m^+-1}\to0,
 \quad\text{so}\quad \cos(ka_{j_m^+})\to1.
\]

The targets \(b_m^-=(2m+1)\pi/|k|\) produce indices \(j_m^-\) with \(\cos(ka_{j_m^-})\to-1\). Since the target spacing is fixed and the increments in (21) vanish, the indices in each subsequence are eventually distinct. Equation (11) makes the two normalized-trace subsequences converge to \(1\) and \(-1\), uniformly in \(|\lambda|\le1/2\). The bound \(|d_j/P_j|\le1\) from (4) then proves the exact limsup and liminf in (12). Strict positivity of \(P_j(t)\) transfers the signs to \(d_j\), with subsequences independent of physical \(t>0\).

For each finite \(j\), the inherited differentiated source integrals give the exact scalar identity

\[
 \frac{(-1)^j\partial_k^{2j}H_\lambda(k)}
 {\partial_\lambda^jH_\lambda(0)}
 =\frac{\int_0^\infty r^{2j}e^{\lambda r^2}\Phi(r)\cos(kr)\,dr}
 {\int_0^\infty r^{2j}e^{\lambda r^2}\Phi(r)\,dr}.
 \tag{22}
\]

Its denominator is strictly positive. Combining (22) with the independently proved growing-\(j\) estimate yields, uniformly for \(|\lambda|\le1/2\) and real \(|k|\le K\),

\[
 \frac{(-1)^j\partial_k^{2j}H_\lambda(k)}
 {\partial_\lambda^jH_\lambda(0)}
 =\cos(ka_j)+O_K(\sqrt{a_j/j}).
 \tag{23}
\]

For each fixed \(\lambda\) in this slab and fixed real \(k\ne0\), the ratio in (23) has limsup \(1\) and liminf \(-1\). Thus the signed even derivatives \((-1)^j\partial_k^{2j}H_\lambda(k)\) have both signs infinitely often. This is an order-asymptotic statement at a fixed readout parameter; no new statement about zeros or their multiplicity follows. No infinite derivative-order series is differentiated or summed.

## 5. Endpoints, control screen and direct baseline

At \(t=0\), \(P_j=d_j=0\) for \(j>0\) and the physical quotient is undefined. Its scalar source expression in (5) has a limit as \(t\downarrow0\), but that is not a nonzero-count event at time zero. The terminal physical endpoint \(t=T\), corresponding to \(\lambda=-1/2\), is included. The normalized estimate is uniform for \(0<t\le T\), without a positive lower bound on the absolute count masses as \(t\downarrow0\). There is no infinite-time or \(\gamma\downarrow0\) conclusion.

At \(k=0\), the ratio is exactly one for \(t>0\), and no negative sign occurs. The sign conclusion is for each fixed nonzero real \(k\); it supplies no uniform finite sign index near zero. The bound (11) is uniform on each fixed compact real \(k\) interval, with a constant proportional to its radius, and supplies no all-height estimate uniform over \(k\in\mathbb R\). Complex analytic continuation remains distinct from a bounded real cosine measurement.

The [reflected control][control] satisfies the generic preparation/count laws and has its already recorded exact interior double event at \(\lambda=1/4\), \(k=\pi/4\). Its quartic-exponential source fails the upper half of the exact canonical comparability (8), so the center/scale theorem above does not apply to it. No claim is made that its signed count traces have only one sign or that it cannot have its own high-order oscillation. The proof applies to every positive source satisfying (8) with fixed positive constants; it does not use exact integer-square arithmetic beyond establishing (8). Neither canonical uniqueness nor a separating collision premise has been obtained. The B02 decision records the other controls and their precise source/domain limitations; none is newly audited here.

The direct scalar baseline is exactly (22): the same source-tail proof gives the same theorem without the count representation. The result is a rigorous asymptotic diagnostic and a scoped obstruction to eventual one-sign **literal** count sectors for theta at fixed \(k\ne0\). It does not exclude phase-dependent patterns, correlated cancellations, finite-sector estimates or other analytical mechanisms. It neither prohibits \(d_0=\partial_kd_0=0\) nor establishes an actual canonical collision. It does not estimate the probability weight of the positive and negative subsequences.

The scalar center is already used in [MC03 Return01, section 2, equation (3)][prior-saddle], with the sharper Gaussian scale \(\sigma^2=a^2/[2j(1+4a)]\). That work's proved limit concerns a fixed ordered box in an order-three signed determinant problem; its complete signed-chamber allowances remain unpaid. The [higher-order comparison][prior-scope] preserves those quantifiers. The present note supplies an elementary positive scalar concentration proof over the complete radial integration domain, uniformly on the physical lambda slab, and its count-sign consequence. It is not a new saddle, does not pay those signed determinant allowances, and does not strengthen any higher-order or full-chamber claim. These two references are attribution/context only, not additional proof premises; their hashes are appended below without changing the frozen r1 manifest.

The [result index][results], [control cluster][controls] and [patterns index][avoid], especially [target classification][a01] and [re-realization][a03], govern this interpretation. No estimating gain over direct source analysis, novelty or RH claim is attached to the new asymptotic. All original spectra, complete source tails, literal cosine, absolute calibration and supplied-loader qualifications remain unchanged. The mathematical nonzero-count traces remain analytical quantities: physical access after nonzero counts is not assumed or newly licensed.

## 6. Local check and return boundary

The single local correction/check pass verified the coefficient \(M/2\) in (13), the middle-interval \(e^{-4}\) factor, the growing far-left interval and unbounded right tail, the lower-normalizer factor \(s\), and the uniform payment of \(\lambda r^2+9r\) omitted from the center equation. It also checked the full theta-tail constants, the signed Kraus amplitudes and complete angular trace, full-line factors of two, finite-count graph payment, strictly positive masses only for \(t>0\), the \(k=0\) exception, terminal endpoint, eventually distinct subsequences and the \((-1)^j\) derivative sign. The explicit limsup/liminf statements use both subsequence limits and the bound by one. No construction or target correction was needed.

There were no deviations or failed cases within r1. The remaining unpaid claims are unchanged: nonzero-count experimental access, an intrinsic theta loader, a physical estimating gain, finite-count signed margins, probability weight of the asymptotic subsequences, collision exclusion and global simplicity/RH. No successor problem is selected here.

Context-only source receipt: MC03 Return01 SHA-256 `8d2727fbdde5c87673ecf61a1efba40b9072f2108ed299c6b162d3cf19235183`; higher-order comparison SHA-256 `e9c81bc53ba0d7cb2d6a87533dd8255bf55da13b3fb2906a30c8727766fe195c`. The latter's actual path is `papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/brainstorm/02_HIGHER_ORDER_EXTENSION_AND_METHOD_COMPARISON_20261102.md`, outside the MC03 subfolder. The primary's shorthand path was resolved read-only; no source file changed.

**Next: [E] TND-D-E04 — fresh Sol / ultra**, one claim-by-claim internal assessment and local correction check of this theorem and its specifically consumed count dictionary, followed by primary integration. Other Note04 diagnostics and external task statuses remain unchanged.

[request]: ../research-progress/handoffs/08_TND_D_E03_R1_REQUEST_20261106.md
[inputs]: ../research-progress/handoffs/08_TND_D_E03_R1_INPUTS_20261106.json
[decision]: ../brainstorm/notes/02_TND_D_B02_SOURCE_SCORE_AND_COUNT_PHASE_DECISION_20261106.md
[e01]: 02_TND_D_E01_R1_CONDITIONAL_QUADRATURE_REALIZATION_20261106.md
[e02]: ../reviews/01_TND_D_E02_CONDITIONAL_REALIZATION_ASSESSMENT_20261106.md
[note04]: 04_TND_D_B02_COLLISION_DYNAMICS_RECONNAISSANCE_20261106.md
[count]: ../manuscript/sections/05_count_calculus.tex
[control]: ../manuscript/sections/07_control.tex
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[prior-saddle]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/03_connected_mellin_response/notes/01_COMPLETE_MELLIN_RESPONSE_RETURN_20261101.md
[prior-scope]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/brainstorm/02_HIGHER_ORDER_EXTENSION_AND_METHOD_COMPARISON_20261102.md
