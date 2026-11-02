# J-B04: complete-density heat and a theta-quantile conservative diffusion

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributor **`/root/branch03`**, actual recorded **gpt-6-astra (Codex), reasoning effort ultra**; child session `01a1999e-f934-71c1-a990-74eb3cb9b33a`, inherited from coordinator session `01a1999e-49d4-7a52-9e8a-95b0c5c430f1`. Child turn metadata was checked. This is a same-model analytical contribution with shared source inputs, not independent specialist review. The coordinator owns the comparative assessment and all shared records; this worker performs no chat registration.

**J-B04 is complete as a bounded conceptual assessment.** One explicit theta-based conservative flux is constructed and solved globally, without assuming a determinant sign. It gives exponential convergence to a multiple of the full theta product density. The exact limit of total negative mass is nevertheless the negative part of the conserved determinant integral. Thus a spectral gap improves mixing but supplies no independent sign estimate. The specific inference “theta-dependent conservative diffusion plus a mixing rate proves positivity” fails; this does **not** exclude other fluxes or a further source-specific estimate for this flux.

**Disposition:** useful as a shared comparison tool; the selected mixing-only sign mechanism stops here. The missing theta input is a coercive estimate on the actual signed orbit, specified below. No new coefficient range or higher-order canonical sign is proved, and no numerical campaign was performed. The accepted global \(R'>0,K>0\), normalized order-three comparison and negative origin curvature \(C\) are unchanged. Order four is a mechanism pilot inside the inherited known positivity baseline, not a new positivity claim.

## 1. Fixed question, normalization and inputs

The question is whether, at \(r=4,k=1\), one can derive
\[
N(s):=\int f_s^-\longrightarrow0,
\qquad \int f_s=M=F_{4,1}D_{4,1},
\quad F_{4,1}=2!4!6!8!,                         \tag{1}
\]
from the complete canonical source at **physical time zero**, using conservation and quantitative theta information independent of the desired sign. Auxiliary time \(s\) does not change the physical source.

Use \(c_n=(2n)!^{-1}\int_0^\infty u^{2n}\Phi(u)\,du\), \(c_n=0\) for \(n<0\), and \(D_{r,k}=\det[c_{k+j-i}]\). Raw moments and \(\gamma_n=n!c_n\) are not substituted for \(c_n\). The symmetric full-orthant density is
\[
f_0(\mathbf u)=\frac1{4!}
 \left(\prod_{j=1}^4u_j^2\right)V(\mathbf u^2)
 \det[\Phi^{(2i)}(u_j)]_{i=0}^3,
\qquad \mathbf u\in U=(0,\infty)^4.             \tag{2}
\]
Both alternating factors change sign under a coordinate interchange, so their product is symmetric. The integral on \(U\) is \(4!\) times the ordered-chamber integral before the displayed factor. Therefore \(\int_U f_0=M\), exactly as in Note14 (3). This is the **whole** determinant density; no signed sector or tail is discarded. Node-collision sets are ordinary interior sets of \(U\), not artificial boundaries. There is no collision-face flux to omit.

The inherited integration-by-parts identity uses all odd endpoints required through \(\Phi^{(6)}\), which vanish for the full even source. The \(u_j^2\) factor also vanishes on a zero-coordinate face. We do not infer a sign of \(f_0\) or of \(N(0)\) from uncomputed derivative determinants.

Selected input versions (working-tree inputs, not a claim that they are committed):

| Input | SHA-256 |
| --- | --- |
| [Branch brief](README.md) | `619bd4307b7cc89aceffac6a64557578ec0fe3c58f9bdccbc996da16a7712524` |
| [Note14](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) | `d8b9160e158317462d75a59d7535f500898cfb51345284d33287cf24eafd14f0` |
| [Note15 request](../15_CONTINUATION_PARALLEL_BRANCH_EVALUATION_20261101.md) | `2d2fd23efd67b019c484ec551f779f1feaf4ffe08046ba457de6d5a3b1ec1f1a` |
| [Accepted Review01](../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md) | `c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe` |
| [Investigation05 Note25](../../../../05_radial_theta_collision_geometry/notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md) | `321d557080ef06abb3e8a70f85872f1e10980881a91fc47806d54ab9b050e11b` |

The root research/model/large-file/history rules, ideas and live register, result/avoid indexes and relevant control, theta, target, shared-premise, scope, numerics and joint-estimate passages govern this return. Existing unrelated working-tree changes are preserved. No new literature theorem is imported: the new heat construction and its estimate are derived below from an explicit elementary kernel and cosine expansion. No common reference-catalog addition is needed.

## 2. Ordinary product heat: a sign-independent benchmark

For comparison take the exact Note14 lift to \((\mathbb R^3)^4\), with \(R_j=|X_j|\), \(u_j=\log R_j/2\), and
\[
\rho(X)=\mathbf1_{R\ge1}\frac{\Phi(u)}{8\pi R^3},
\quad
\widetilde f_0(\mathbf X)=\frac1{4!}
 \prod_j[u_j^2\rho(X_j)]\,V(\mathbf u^2)
 \det\left[\frac{\Phi^{(2i)}(u_j)}{\Phi(u_j)}\right]_{i=0}^3.
                                                               \tag{3}
\]
The spherical Jacobian gives \(\rho(X)dX=\Phi(u)du\) after angular integration, so \(\int\widetilde f_0=M\), and the lift preserves the full positive and negative masses. Complete theta decay gives \(\widetilde f_0\in L^1\) and \(B_1:=\int|\mathbf X|\,|\widetilde f_0|<\infty\). The density is zero if any \(R_j<1\); the ambient domain is all of \(\mathbb R^{12}\), not just the exterior after evolution.

Independent heat in each spatial copy is
\[
\widetilde f_s=G_s^{(12)}*\widetilde f_0,
\quad J=-\nabla\widetilde f_s,
\quad\int\widetilde f_s=M.
\]
The unit-mass positive kernel defines an \(L^1\)-continuous global mild solution without a sign assumption or initial boundary compatibility. No sphere at \(R_j=1\) is an evolving boundary. The full-space integral includes any mass crossing it, and integrable heat-kernel derivatives justify the outer conservation limit.

The one-direction Gaussian derivative has \(L^1\)-norm \(1/\sqrt{\pi s}\). Integrating translations along the line segment from 0 to \(Y\), then applying Fubini, gives
\[
\|\widetilde f_s-MG_s^{(12)}\|_1\le\frac{B_1}{\sqrt{\pi s}}.
\]
Since the negative-part map is 1-Lipschitz,
\[
\left|\int\widetilde f_s^- -(-M)_+\right|
 \le\frac{B_1}{\sqrt{\pi s}}.                    \tag{4}
\]
This is the audited Note14 benchmark, rederived here to make the comparison exact. It does not require or imply a known sign of \(M\).

## 3. One explicit theta-based conservative flux

Normalize the **complete** source and use its cumulative distribution:
\[
q(u)=\frac{\Phi(u)}{c_0}>0,
\quad Q(u)=\int_0^u q(v)\,dv,
\quad y_j=Q(u_j),
\quad p(\mathbf u)=\prod_{j=1}^4q(u_j).          \tag{5}
\]
Then \(Q:[0,\infty)\to[0,1)\) is increasing, \(Q(\infty)=1\), and \(d\mathbf y=p\,d\mathbf u\). Only the known positive scalar \(c_0\) is inverted; there is no inverse determinant or sign-dependent coefficient.

Define \(h_s(\mathbf y)=f_s(\mathbf u)/p(\mathbf u)\). The selected local conservative flux on the full orthant is
\[
\boxed{J_j=-\frac{p}{q(u_j)^2}
                 \partial_{u_j}\!\left(\frac{f_s}{p}\right),
\qquad \partial_sf_s+\sum_{j=1}^4\partial_{u_j}J_j=0.}     \tag{6}
\]
The diffusion coefficient grows in the far tail. Global existence is **not** asserted from a bounded-coefficient theorem; the exact change of variables resolves it. Indeed \(\partial_{u_j}=q(u_j)\partial_{y_j}\) and \(p/q(u_j)\) is independent of \(u_j\), whence
\[
-\partial_{u_j}J_j=p\partial_{y_j}^2h_s.
\]
Thus (6) is exactly Neumann heat on the unit cube:
\[
\partial_sh_s=\Delta_{\mathbf y}h_s,
\qquad \partial_{y_j}h_s=0\quad(y_j=0,1).        \tag{7}
\]
It is a conservative diffusion, not smooth invertible transport.

### Existence, endpoints and the complete tail

For \(s>0\), let \(g_s(t)=(4\pi s)^{-1/2}e^{-t^2/(4s)}\) and
\[
k_s(y,z)=\sum_{m\in\mathbb Z}
 [g_s(y-z+2m)+g_s(y+z+2m)].
\]
The absolutely convergent image sum is positive, has unit integral in either variable on \([0,1]\), and has zero normal derivative at both endpoints. Its product in four variables defines
\[
h_s(\mathbf y)=\int_{[0,1]^4}
 \prod_{j=1}^4 k_s(y_j,z_j)h_0(\mathbf z)\,d\mathbf z,
\qquad f_s=p\,h_s(Q(\mathbf u)).                \tag{8}
\]
Reflection and periodic extension reduce approximate-identity convergence to the usual Gaussian argument. This gives a global \(L^1\)-continuous solution; the Fourier cosine coefficients below also give uniqueness in that continuous mild class. Neither existence nor conservation assumes \(M\ge0\).

At positive \(s\), (8) is smooth up to the closed cube. In original coordinates,
\(J_j=-(p/q_j)\partial_{y_j}h_s\), which vanishes at \(u_j=0\) and at \(u_j\to\infty\) by the Neumann condition. For the integrated outer flux, \(p/q_j\) is the unit-mass density in the other coordinates, so this limit retains the complete tail rather than losing it in a pointwise argument. Equivalently, integration on boxes whose \(Q\)-images approach the cube gives zero total limiting boundary flux. The coordinate endpoint at infinity is included by the specified no-flux condition. This choice of conservative realization is part of the flow, not an inferred automatic boundary behavior of an unspecified operator.

For the actual datum,
\[
h_0=\frac{c_0^4}{4!}\prod_j u_j^2 V(\mathbf u^2)
        \det[\Phi^{(2i)}(u_j)/\Phi(u_j)]_{i=0}^3.           \tag{9}
\]
It belongs to \(L^2(d\mathbf y)=L^2(p\,d\mathbf u)\). To check the tail, each fixed ratio \(\Phi^{(m)}/\Phi\), \(m\le6\), has at most exponential growth in \(u\) from the full convergent theta series and its first-mode tail; for example a bound \(C_m e^{4mu}\) holds beyond a fixed compact interval. The remaining factors in (9) are polynomial in the \(u_j\). Squaring (9) therefore gives a polynomial times \(\prod_j e^{C u_j}\), while \(p\) decays double-exponentially. This is integrable. On compact intervals \(\Phi\) has a positive minimum, so the ratios have no pole; collision sets produce zeros in the determinant and no division by a Vandermonde occurs here. At zero all factors are smooth and even. This establishes the norm without any new derivative-sign premise or numerical test.

## 4. Quantitative gain and the precise failure of the sign inference

The normalized cosine functions on \([0,1]\), \(e_0=1\) and \(e_n=\sqrt2\cos(n\pi y)\), form the separated basis. Integration by parts with (7) gives
\[
h_s=M+\sum_{\mathbf n\ne0}a_{\mathbf n}
 e^{-\pi^2|\mathbf n|^2s}\prod_j e_{n_j}(y_j),
\qquad M=\int h_0\,d\mathbf y.
\]
Parseval and \(|\mathbf n|^2\ge1\) show
\[
\boxed{\|f_s-Mp\|_1
 =\|h_s-M\|_{L^1(d\mathbf y)}
 \le e^{-\pi^2s}\|h_0-M\|_{L^2(d\mathbf y)}.}             \tag{10}
\]
The Fourier derivation proves the needed spectral estimate directly; no unverified functional-inequality theorem is being imported. Conservation, contraction and (10) imply
\[
\boxed{\left|N(s)-(-M)_+\right|
 \le e^{-\pi^2s}\|h_0-M\|_2,
\qquad \lim_{s\to\infty}N(s)=(-M)_+.}                    \tag{11}
\]
The norm in (10) is finite independently of the unknown sign. A wholly sign-free upper allowance is \(\|h_0-M\|_2\le\|h_0\|_2\), by orthogonal projection onto constants. Thus even a fully paid rate and prefactor do not remove the unresolved \((-M)_+\) term.

**What changed from the brief:** we now have an explicit complete-theta flux with an independently constructed global solution, all boundary terms paid, and exponential mixing rather than the whole-space \(s^{-1/2}\) comparison. **What did not change:** for this flux, \(N(s)\to0\) is exactly equivalent to \(M\ge0\). Theta dependence of the coefficients and an improved rate do not make the stationary mean positive. The comparison does not measure implementation cost or show a numerical advantage.

For a regular zero level of \(h_s\), integration over its negative region gives the exact dissipation
\[
-N'(s)=\int_{\{h_s=0\}}|\nabla_{\mathbf y}h_s|\,dS
       =:\mathcal I(s),                                  \tag{12}
\]
with no cube-boundary term. Smooth convex approximation gives contraction at singular levels; a future quantitative inequality must handle those times as well. The **unclosed conceptual estimate** is
\[
\mathcal I(s)\ge\lambda(s)N(s)\quad\text{for the actual datum (9)},
\qquad \int_0^\infty\lambda(s)\,ds=\infty,               \tag{13}
\]
or a comparably effective orbit estimate deduced from full theta identities without using \(M\ge0\). The spectral gap in (10) controls the fluctuation around the conserved mean, not (13).

There is a precise obstruction to deducing (13) for arbitrary signed data from this operator: \(f_0=-p\) is stationary, has \(N=1\), and has \(\mathcal I=0\). This is an operator-level counterexample, **not** a claimed theta determinant datum or a counterexample to its sign. Restricting to the actual determinant datum requires an additional restriction proved from theta, not merely renaming the datum. No such restriction has been proved in this assessment.

Strictness is a further issue. Taking \(h_0=\cos(\pi y_1)\) gives \(M=0\) and \(N(s)=e^{-\pi^2s}/\pi\to0\), yet the conserved mass is not positive. This explicitly rules out inferring strict positivity just from negative-mass decay. A surviving positive-mass lower bound or a valid comparison to the positive \(k=0\) anchor would still be required. Neither is supplied by this fixed-\(k\) flow.

## 5. Small indices, growing order and control screen

For arbitrary finite \(r,k\), replace (2) by \(r!^{-1}\prod u_j^{2k}V(\mathbf u^2)\Delta_r\), use \(p_r=\prod q(u_j)\), and apply the same construction on \([0,1]^r\). Fixed derivative ratios through \(2r-2\) and all polynomial factors are integrable in \(L^2(p_r)\). The first nonzero cube eigenvalue is still \(\pi^2\), but the initial norm, derivative estimates and the unproved nodal inequality depend on \(r,k\). This uniform formal mixing rate does not control their sign. No large-\(k\) assumption is needed for existence or (11), including \(k=1\); no small-index positivity is gained. Separate flows at different \(k\) preserve different means and do not prove the signed-averaging comparison to \(k=0\).

| Control or class | Actual premise check and consequence |
| --- | --- |
| Gaussian | Positive smooth source and fixed-derivative ratio bounds suffice for the quantile flow. Its known positive determinant baseline is a normalization check, not theta evidence. |
| Euler-factor sources | Positive even rapid-decay versions admit the same construction with their own \(q\); modified arithmetic fails literal canonical reconstruction. No higher-order determinant sign is assigned. |
| Weighted-square and finite-prime sources | Where positive and sufficiently decaying they admit quantile diffusion for any given integrable signed density. Missing full reflection can invalidate the determinant identity (2), through unpaid odd endpoints; the diffusion does not repair it. Altered coefficients also fail complete theta arithmetic. |
| Reflected smooth/super-Gaussian and positive-primitive sources | The quantile construction works whenever positivity and the displayed \(L^2\) condition hold. Full reflection/primitive positivity does not supply (13); these controls fail unchanged canonical arithmetic. |
| Atomic examples | Outside the strictly positive smooth-density assumptions for the diffeomorphism (5). Smooth approximations require their own derivative/integrability accounting. |
| Positive-time collision witnesses | Not counterexamples to this time-zero finite-order pilot. No collision sign is inferred; they screen only the premises actually asserted. |
| Negative stationary datum \(-p\) | Satisfies the chosen operator's existence, boundary, conservation and mixing hypotheses. It fails the additional “actual determinant datum” restriction, and shows those generic hypotheses cannot imply (13). |

The exact theta series fixes the quantile coordinate, but the proof of (10) uses only its positive density and integrability. It does not use an arithmetic constraint on the evolved nodal geometry. This is the precise information gap. The result respects [the control cluster](../../../../../../result-summaries/12_collision_controls_and_screening.md), [target classification](../../../../../../avoid/01_restating_the_target.md), [scope](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [joint signed estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 6. One next action and stopping boundary

**Next: [B] actual-orbit coercivity decision — Astra.** This is a recommendation, not a new dispatched task. Keep (6), \(r=4,k=1\), the full datum (9), and physical time zero fixed. The concrete deliverable is a proof of one quantitative theta-derived inequality implying (13), or an explicit demonstration that a selected proposed inequality still needs the unknown mean sign. Track the complete nodal dissipation and full tail; identify the theta hypothesis that the relevant generic controls do not supply. Require a separate strict-positive-mass argument if strict \(D_{4,1}>0\) is claimed. The conceptual choice is which genuinely signed arithmetic relation could control that interface.

Stop after one proposed inequality fails that information test; do not substitute more mixing-rate estimates, derivative acquisition, simulations or low-order coefficient scans. Do not issue an E task unless this B step fixes a finite expression, independent bound, method and acceptance test. Given the exact comparison (11), this continuation has lower priority than a branch that already supplies a plausible independent sign inequality. The flux remains available as a shared analytical benchmark, without treating the unsolved estimate as a result.
