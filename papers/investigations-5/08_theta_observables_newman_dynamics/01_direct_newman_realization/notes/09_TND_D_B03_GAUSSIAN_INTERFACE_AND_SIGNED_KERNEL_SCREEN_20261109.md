# B03: checked Gaussian interface and the reflection-paired sign screen

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, direct chat0007, thread
`01a1c389-3fe9-7930-8223-c935cc1920e1`. Actual backend model and reasoning
effort are unavailable in the accessible canonical capture metadata.

**Status: proof-author derivation and local checking within B03, not an
E09/E10 return or independent assessment.** The dictionary and error
transfer in Brainstorm03 (3)–(8) require no correction. The new explicit
negative-region calculation below stops one attempted proof: folding by
reflection, then discarding positive contributions and using positive
theta coefficients alone. It does not exclude an estimate retaining the
signed cancellations. No canonical collision restriction is obtained.

The [decision](../brainstorm/notes/04_TND_D_B03_R3_SIGNED_PREMISE_DECISION_20261109.md)
owns the two-approach disposition; the [sole register][progress] owns task
status. Governing sources are [plan r3][plan], [Brainstorm03][brainstorm],
the [operator Gaussian theorem][operator], and [Note07][tail] as accepted
by [E07][tail-review]. Read the [result index][results] and [avoid index][avoid],
especially [controls12][controls], [geometry13][geometry],
[theta14][theta], [classification01][a01], [screen02][a02],
[scope07][a07], [mixed terms12][a12] and [utility20][a20].

## 1. Declared class and fully paid local signal

For this decision only, consider hypothetical nondegenerate double events

\[
 \lambda_*\in[1/8,3/8],\quad k_*\in[1/2,100],\qquad
 H_{\lambda_*}(k_*)=H_{\lambda_*}'(k_*)=0,
 \quad a=H_{\lambda_*}''(k_*)\ne0.
 \tag{1}
\]

This is a finite analytical screening box, not a certified event-free box
or an assertion that an event exists. It includes the reflected control's
exact event. Evenness gives the corresponding negative-center box.
Higher multiplicities, endpoints and other centers are outside this pass.
Set \(b=|a|\), \(0<\varepsilon\le1/16\),
\(\lambda=\lambda_*-\varepsilon\), \(X=k_*\), \(v=\varepsilon\).
Then \(\lambda\in[1/16,3/8]\) and
\(\alpha=1/2-\lambda\in[1/8,7/16]\). The Gaussian integral still runs
over the **whole real line**, not just the center window.

Use half-line complete moments
\(I_j(L)=\int_0^\infty u^je^{Lu^2}\Phi(u)du\), with \(L=3/8\),
and put \(C=I_3(L)\), \(D=I_4(L)\). These are exactly half of the
operator theorem's full-line moments. Its \(\kappa=1,m=2\) case gives

\[
 A_0(\lambda_*-\varepsilon,k_*,\varepsilon)
 =-\tfrac12 b^2\varepsilon+\mathcal E(\varepsilon),
 \quad |\mathcal E|\le E_1,
 \tag{2}
\]
\[
\begin{split}
 E_1={}&\frac{22}{3}bC\sqrt{\frac2\pi}\,\varepsilon^{3/2}
 +(2bD+\tfrac{17}{4}C^2)\varepsilon^2\\
 &+\frac{11}{6}CD\sqrt{\frac2\pi}\,\varepsilon^{5/2}
 +\tfrac12D^2\varepsilon^3.
\end{split}
\tag{3}
\]

Requiring \(E_1\le b^2\varepsilon/4\) gives
\(A_0\le-b^2\varepsilon/4<0\). At each fixed event such sufficiently
small \(\varepsilon\) exist. There is no assumed lower floor on \(b\),
and no event-independent resolving radius is claimed. Complete source
moments pay the spatial exterior, so no local Taylor germ is substituted
for the whole Gaussian integral. Complex zeros are analytic continuations;
all observation parameters here are real.

## 2. One local interface check: Brainstorm03 (3)–(8)

With \(h_*=H_{1/2}(0)\), the fixed count law is
\[
 d_j=\frac{(-\alpha)^j}{j!h_*}H_\lambda^{(2j)},\qquad
 d_j''=-r_jd_{j+1},\quad r_j=(j+1)/\alpha,
 \quad c_j=j!h_*/\alpha^j.
\]
Substituting \(H^{(2j)}=(-1)^jc_jd_j\) and its first derivative gives
\[
 A_{2j}=c_j^2\int w_v[(d_j')^2+r_jd_jd_{j+1}],
 \quad
 A_{2j+1}=c_j^2\int w_v[r_j^2d_{j+1}^2+r_jd_j'd_{j+1}'].
 \tag{4}
\]
Both signs, factorials and the factor \(h_*^2\) are correct. In particular
\(S_\alpha=A_0/h_*^2\). These divisions require \(\alpha>0\);
the scalar definition of \(A_n\) remains available at \(\alpha=0\).
Products of traces are analytical products of expectations, not joint
probabilities of two different count outcomes in one trial.

For \(H=H_\lambda\) and the exact retained reconstruction \(\widehat H\),
two integrations by parts give
\[
 A_0(H)=2\int w_v(H')^2-\tfrac12\int w_v''H^2.
 \tag{5}
\]
The full source and every fixed retained count have bounded real
derivatives of the needed orders; hence all Gaussian boundary terms vanish.
With \(|H-\widehat H|\le\eta_0\),
\(|H'-\widehat H'|\le\eta_1\), \(|H|\le I_0(L)\),
\(|H'|\le I_1(L)\), the product-difference bound proves
\[
 |A_0(H)-A_0(\widehat H)|\le
 2\eta_1(2I_1(L)+\eta_1)
 +\frac{\eta_0}{v}(2I_0(L)+\eta_0)=:\mathcal D_N.
 \tag{6}
\]
Here \(\|w_v''\|_1\le2/v\); in fact it equals
\(4e^{-1/2}/(\sqrt{2\pi}\,v)\). This optional constant sharpening
does not remove the inverse-variance cost and is not a new sign result.

The accepted Note07 supplies, for its admissible eventual \(N\),
\[
 \eta_0=\frac{h_* B_{N+1}^{(0)}}{1-Q_N},\qquad
 \eta_1=\frac{h_*\sqrt{B_{N+1}^{(0)}B_{N+1}^{(2)}}}{1-Q_N}.
 \tag{7}
\]
Its constants remain conservative and unevaluated. All omitted counts,
theta indices and radial tails are included. Numerical retained-term,
normalization and integration errors would be additional payments; no
such evaluation is made here. At \(v=\varepsilon\), sufficient small-error
requirements at a fixed event include
\(\eta_0=o(b^2\varepsilon^2/I_0(L))\) and
\(\eta_1=o(b^2\varepsilon/I_1(L))\). The full inequality (6), not these
order labels, would have to be used for any actual consequence.

The exact identities are a dictionary, (2) is an inherited diagnostic,
and (6) is an acquisition bound. None is an independent signed premise.
A lower enclosure for \(A_0\) above the negative margin in (2) is still
unpaid. The same scalar source calculation has exactly (4)–(7).

## 3. Tested source premise: can reflection and positive square weights sign the paired kernel?

This is the primary B03 attempt, not a third approach. The independent
source facts available for it are complete reflection and
\[
 F_\lambda(u)=e^{\lambda u^2+u}
 \sum_{n\ge1}P_0(n^2\rho(u))e^{-n^2\rho(u)},\quad
 P_0(s)=2s^2-3s,\quad \rho(u)=\pi e^{4u},\quad u\ge0.
 \tag{8}
\]
All displayed summands are positive. The [operator section][operator]
already derives the complete reflected quadratic form
\[
 A_0=\iint_{(0,\infty)^2}F_\lambda(p)F_\lambda(q)K_{X,v}(p,q)\,dp\,dq,
 \tag{9}
\]
\[
 K_{X,v}=\tfrac14\left[
 (p-q)^2e^{-v(p+q)^2/2}\cos X(p+q)
 +(p+q)^2e^{-v(p-q)^2/2}\cos X(p-q)\right].
 \tag{10}
\]
Thus (9) is reused, not claimed as a new representation. The attempted
technical lemma is nonnegativity after this particular reflection pairing,
or a sufficiently small negative-part payment after discarding the
positive part. These are stronger technical routes to a sign, not new
RH-equivalent criteria. We test them on the unchanged complete source.

**Pointwise failure and explicit negative mass.** For every \(X>0\), set
\(r=\pi/X\). On
\[
 \mathcal R_X=\{0\le p\le r/6,\quad5r/6\le q\le7r/6\},
\]
both \(X(q-p)\) and \(X(q+p)\) lie between \(2\pi/3\) and
\(4\pi/3\), so both cosines are at most \(-1/2\). Also
\(|p\pm q|\le4r/3\) and
\((p-q)^2+(p+q)^2\ge25r^2/18\). Consequently
\[
 K_{X,v}(p,q)\le-\frac{25r^2}{144}e^{-8vr^2/9}<0
 \quad\text{on }\mathcal R_X.
 \tag{11}
\]
This defeats pointwise positivity of the actual paired integrand, including
each positive theta-index pair. It does **not** assert that an integrated
index block or the complete integral is negative.

Define the exact positive and negative contributions
\[
 \mathcal P=\iint F_\lambda(p)F_\lambda(q)(K_{X,v})_+\,dp\,dq,
 \quad
 \mathcal N=\iint F_\lambda(p)F_\lambda(q)(K_{X,v})_-\,dp\,dq.
\]
Both are finite: \(|K|\le(p^2+q^2)/2\), paid by \(I_0I_2\).
The complete signed answer is \(A_0=\mathcal P-\mathcal N\).
Writing \(m_{\lambda,r}=\min_{0\le u\le4r/3}F_\lambda(u)>0\),
the rectangle's area \(r^2/18\) gives
\[
 \mathcal N\ge\frac{25r^4}{2592}
       e^{-8vr^2/9}m_{\lambda,r}^2>0.
 \tag{12}
\]
No tail or mixed term is omitted: a positive subintegral lower-bounds
\(\mathcal N\), not \(A_0\). In particular this is not a finite-source
substitution for the physical model.

One completely explicit, deliberately crude uniform floor on the declared
box follows from (8). Put \(R=8\pi/3\) and
\(m_0=P_0(\pi)\exp[-\pi e^{4R}]\). Since \(\lambda\ge0\), the first
positive theta term gives \(F_\lambda(u)\ge m_0\) on \([0,R]\).
For \(X\in[1/2,100]\) and \(0\le v\le1/16\),
\[
 \mathcal N\ge\mu:=\frac{25}{2592}
       (\pi/100)^4e^{-2\pi^2/9}m_0^2>0.
 \tag{13}
\]
The extremely small constant is an analytic floor, not a useful numerical
cutoff. Only its strict positivity is used.

**Scoped consequence.** If the only retained information about the positive
contribution is \(\mathcal P\ge0\), even knowing \(\mathcal N\) exactly
gives only \(A_0\ge-\mathcal N\). Every valid negative-part upper payment
\(B\ge\mathcal N\) satisfies, along the resolving path at a fixed event,
\[
 \frac{B}{b^2\varepsilon}\ge
 \frac{\mu}{b^2\varepsilon}\longrightarrow\infty.
 \tag{14}
\]
Thus this specific sign-discarding estimate cannot produce a vanishing
event-scale loss or contradict (2) for all sufficiently small
\(\varepsilon\). No curvature floor is assumed. This is not a theorem
that the actual defect is large, that every finite resolving time fails,
or that another paired/signed estimate cannot work. Retaining a correlated
lower payment for \(\mathcal P\) can change the comparison and is outside
this obstruction. Merely requiring the desired bound on
\(\mathcal P-\mathcal N\) would restate the target, not supply a premise.

## 4. Analytical controls and the premises they actually test

The [control register][controls] supplies the inherited certificates and
status qualifications. This pass rechecks the reflected witness
analytically and applies the new kernel calculation; it does not rerun
Arb certificates or audit every control's physical state domains.

For the reflected control, at \(\lambda_*=1/4\),
\(H^*_{1/4}(k)=cF(k)(1+\cos4k)\),
\(F(k)=\int_0^\infty e^{-u^4}\cos(ku)du\).
Its exact event is \(k_*=\pi/4\), with
\(a^*=16cF(\pi/4)>0\). Indeed the standard elementary estimate in the
[direct control proof][control-proof] is
\(F(k)\ge M_0(1-k^2/4)>0\) for \(|k|<2\).
Its own complete moments pay (2)–(3), so its resolving \(A_0\) is negative.
It shares the count and Gaussian interface; it fails literal theta
arithmetic and canonical tail comparability. No canonical constants are
assigned to it. The tested pointwise kernel lemma fails already for theta.

| Control family | Used generic interface and failed canonical premise; domain qualification |
| --- | --- |
| Euler-factor sources | Smooth positive-source/count identities survive with their own constants; conductor-one/unit canonical arithmetic fails. Their recorded negative Laguerre witnesses at \(\lambda=.2\) remain negative under sufficiently narrow Gaussian averaging by continuity. This is not a new double-event location certificate. |
| Three-/four-weighted squares | Half-line moments pay scalar heat/Gaussian formulas; complete unit weights/full reflection fail. The three-square double at \(.25,44.13\ldots\) lies in (1). The four-square event at \(.01,83.53\ldots\) is outside this time box and is not purportedly rejected here. Smooth full-line state domains are not assumed. |
| Reflected super-Gaussian | Exact in-box witness above; canonical expansion and tail fail, while the generic interface holds. |
| Smooth log-concave / positive-primitive | Applicable shape, reflection and moment properties survive; exact theta expansion fails. Their source-specific implicit damping thresholds are not numerically certified here. No fresh in-box location claim. |
| Finite-source / finite-prime changes | Literal complete coefficients or full reflection fail. Known high-gap events need not lie below 100. Approximation with a paid full-source remainder is distinct from substituting these sources. |
| Atomic / finite-profile | Complete Fourier moments may suffice for the scalar formulas; smooth square-root/operator domains may fail. Full theta arithmetic, full profile and eventual simplicity fail as recorded. No transfer of a smooth-state construction is made. |
| RH-conditional normalized endpoint | Ordinary Dirichlet arithmetic fails; its time-zero doubles are outside (1). Endpoint simplicity is not a consequence sought here. |
| Variable observation kernels | Literal cosine or its Newman equation fails; (4), (9) need not describe the changed observation. |
| Actual-theta finite-profile relaxation | Fractional slack measures are not physical integer zero divisors; passing finitely many profiles is not a full-source joint bound. |

Naming the absent canonical source identity never proves failure of an
unproved inequality. These controls reject generic positivity as the
missing signed premise; they do not reject future quantitative theta use.
The even/odd count dictionary and error bound pass wherever each source's
own moment assumptions apply, as exact identities and bounds should.

## 5. Comparison and disposition

The direct scalar baseline uses the same complete source, same reflection
pairing, same Gaussian, same normalization, same count-tail information
and same signed correlations. Equations (9)–(14) apply identically.
No physical or computational advantage is established. Neither improving
the constant in (6) nor certifying more absolute moments changes this
comparison or supplies the required sign.

The secondary Green-acquisition option was checked only at the r3 gate:
\(R_N=\int\tau_N(\alpha u^2)\cos(ku)d\mu_*\) is the identical scalar
omitted kernel before any grouping. The existing absolute bound substituted
into OG therefore gives the same compact multiplier error and the same
logarithmic error modulus. No new correlated enclosure, cost comparison
or favorable Green upper value was supplied. This is a missing-input
disposition, not a general impossibility theorem for correlated remainders.

**B03's bounded r3 decision is complete with a scoped stop and no E09
contract.** The primary attempt lacks a signed correlation estimate that
survives the exact negative-part comparison; the secondary lacks a
distinct useful acquisition comparison. E09/E10 remain unissued. The
direct branch remains open. No manuscript milestone or investigation
closure has occurred, so this note is not promoted into the result index.
Continuation and model routing are in [Note10][continuation].

[progress]: ../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md
[plan]: ../research-plan/03_DIRECT_NEWMAN_REALIZATION_RESEARCH_PLAN_R3_20261109.md
[brainstorm]: ../brainstorm/notes/03_TND_D_CROSS_BRANCH_RESEARCH_BRAINSTORM_20261109.md
[operator]: ../../03_operator_imaginary_time_evolution/manuscript/sections/16_gaussian_laguerre.tex
[tail]: 07_TND_D_E06_COMPLETE_COUNT_TAIL_20261106.md
[tail-review]: ../reviews/04_TND_D_E07_COMPLETE_COUNT_TAIL_ASSESSMENT_20261106.md
[control-proof]: ../manuscript/sections/07_control.tex
[continuation]: 10_TND_D_AFTER_B03_CONTINUATION_AND_MODEL_CHANGE_20261109.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../avoid/20_volume_without_a_gain.md
