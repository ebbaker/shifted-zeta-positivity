# MC04-B01: logarithmic-dilation Ward identity for the signed theta insertion

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributor /root/mc04_ward, actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**, verified from worker session 01a19a49-e72d-7902-8f13-adf50b8aa74f, turn 01a19a49-e74a-7a23-ac10-efb3c7f23e13. This is a bounded B assessment under [parallel packet r1][packet], not its separate review.

**Disposition: bounded assessment complete; exact inserted identity and scoped nonclosure proved in-note, separate checking pending.** A logarithmic-dilation Ward equation exposes the mixed response whose lower bound would pay the complete Mellin curvature. It retains the derivative of the signed insertion. A pointwise closure of its residual by any fixed polynomial in the Mellin observable is impossible for the complete theta source. No Gaussian curvature allowance, integrated neighboring-index allowance, new determinant sign, or RH result is proved. The physical formulation is an exact finite-particle Schwinger–Dyson problem, without a claim of novelty or a local dynamical QFT.

| Next task | Type and recommendation | Readiness | Frozen checking contract |
| --- | --- | --- | --- |
| MC04-E01: check this return | E — Sol; fixed algebra, endpoint and scope verification | Ready after coordinator freezes this file; different worker required | Check (4), (6), all boundaries, full-source asymptotics (9)–(10), Gaussian normalization and scope. Accept, correct or leave unresolved; no numerical campaign or new candidate. |

## 1. Inputs, choice and classification

Inputs are the [local overview][overview] and [sole register][progress], accepted [source/sign review][signreview], initial [Mellin assessment][initial], [comparative review][comparative], [route note][routes], [physical note][physical], [parent overview][parent] and [source inspection record][sources]. Exact launch versions and the existing dirty tree are recorded in [the coordinator manifest][launch]; the branch support record lists the selected input hashes and recheck results. No new sibling result is assumed. The complete source, physical time zero, factorial normalization and signed \(h_3\) are unchanged.

The two fields considered were ordinary dilation \(v(u)=u\) and logarithmic dilation \(v(u)=u\log u\). Ordinary dilation has \(XT=6\), so its first Ward equation fixes a virial expectation rather than a coefficient of \(M'\). **Select only \(v(u)=u\log u\)**: it has \(XT=T\), exposing \(M'\) directly. No third field, hierarchy iteration, quadrature or coefficient acquisition was attempted.

Classification:

- (4) and (6) are exact generic identities, specialized to the complete theta source and proved for all \(s\ge0\).
- (7) reformulates the already proposed Gaussian sufficient comparison; it is not an acquired estimate.
- (10) proves an obstruction to the specified pointwise finite-polynomial closure only. It does not exclude integrated closure, nonpolynomial observables, inequalities, or other Ward identities.
- The physical dictionary gives a usable response identity, not a positivity theorem or an all-order RH equivalence.

Read with the [result index][results], particularly [physical-channel lessons][channels], [theta inputs][theta] and [controls][controls], and the [avoid index][avoid], particularly [reformulations][target], [re-realizations][rereal], [joint signed estimates][joint] and [scoped exclusions][scope].

## 2. Complete observable and undivided residual

On \(\Omega_3=\{0<u_1<u_2<u_3\}\), set
\[
z_j=u_j^2,\quad q=\prod_jz_j,\quad T=\log q=2\sum_j\log u_j,
\quad R=\Phi''/\Phi,
\]
\[
\Delta(\mathbf u)=\det[\Phi^{(2i)}(u_j)]_{i=0,1,2;\ j=1,2,3},
\qquad G=V(\mathbf z)\Delta,
\]
\[
w_s=q^s\Bigl(\prod_j\Phi(u_j)\Bigr)V(\mathbf z)V(R(\mathbf u)),
\quad
h=\frac{\Delta}{(\prod_j\Phi(u_j))V(R(\mathbf u))},
\quad
M(s)=\int_{\Omega_3}q^sG=\int_{\Omega_3}hw_s.                \tag{1}
\]
Accepted \(R'>0\) makes \(w_s>0\); the accepted order-three signed-averaging input gives \(M(s)>0\) for real \(s\ge0\). Neither makes \(hw_s\) a positive measure. The negative origin region of \(h\) is retained. Only the integer coefficient identity \(M(k)=(2k)!(2k+2)!(2k+4)!D_{3,k}\), \(k\ge0\), is used.

Define
\[
v(u)=u\log u,\qquad X=\sum_{j=1}^3v(u_j)\partial_{u_j},
\]
\[
I_z=\sum_{a<b}\frac{z_b\log z_b-z_a\log z_a}{z_b-z_a},
\qquad
I_R=\sum_{a<b}
\frac{v(u_b)R'(u_b)-v(u_a)R'(u_a)}{R(u_b)-R(u_a)},
\]
\[
L_\Phi=\sum_jv(u_j)\frac{\Phi'(u_j)}{\Phi(u_j)},\qquad
J=Xh+h(I_z+I_R+L_\Phi).                                  \tag{2}
\]
These are smooth on the open chamber. For integration the definition is the **undivided product**
\[
w_sJ=q^sXG,\qquad N(s)=\int_{\Omega_3}q^sXG.               \tag{3}
\]
No division by \(h\), or positive replacement for \(h\), is made. Its zeros are harmless. Formula (3) fixes the face interpretation without estimating separate singular quotients. Expanding \(X\Delta\) differentiates each column in turn and uses source derivatives only through order five: one fixed derivative required by this field, not an escalating campaign.

## 3. Inserted Ward equation and complete curvature consumer

Directly,
\[
\operatorname{div}v=3+\tfrac12T,\qquad X(q^s)=sTq^s,\qquad
X\log V(\mathbf z)=I_z,\qquad X\log V(R(\mathbf u))=I_R.
\]
Integrating \(\sum_j\partial_{u_j}\{v(u_j)hw_s\}\), with Section 4's boundaries, yields
\[
\boxed{(s+\tfrac12)M'(s)+3M(s)+N(s)=0,\qquad s\ge0.}       \tag{4}
\]
A carrier-only equation replaces \(h\) by \(1\) and deletes \(Xh\), changing the amplitude.

Let \(Z=\int w_s\), \(E_s\) denote expectation under \(w_s/Z\), \(A=E_sh=M/Z\), and
\[
\ell(s)=M'(s)/M(s)=E_s(hT)/A,\qquad
\mathcal C_3(s)=(\log M)''(s).
\]
In particular \(\ell\) is **not** the carrier mean \(E_sT\). Since \(J\) is independent of \(s\),
\[
N'(s)=\int_{\Omega_3}T w_sJ,\qquad
\left(\frac{N}{M}\right)'=\frac{E_s[(T-\ell)J]}{A}.         \tag{5}
\]
Dividing (4) by \(M\), then differentiating once, gives
\[
\boxed{\mathcal C_3(s)=
\frac{-\ell(s)-A(s)^{-1}E_s[(T-\ell(s))J]}{s+\tfrac12}.}   \tag{6}
\]
This equals the packet's full carrier-variance-plus-two-signed-covariances expression: both differentiate the same \(M\). The specific surviving obligation for the Gaussian comparator is
\[
\boxed{\frac{E_s[(T-\ell(s))J]}{A(s)}
\ \ge-\ell(s)-(s+\tfrac12)\kappa_3(s),\qquad s\ge0.}        \tag{7}
\]
Equation (7) is exactly equivalent to the proposed pointwise envelope under (6). This return establishes its residual and normalization, **not its inequality**. Carrier positivity and monotonicity of \(h\) do not determine the mixed sign of \((T-\ell)J\). The field \(v\) changes sign at \(u=1\), and \(J\) includes the insertion variation. Separate absolute bounds would discard joint cancellation.

## 4. Origin, faces, full spatial tails and \(s=0\)

Use bounded cutoffs, then remove them in the undivided formula. Equivalently work on the symmetric full orthant and divide by \(3!\).

**Origin.** The complete source and fixed derivatives are bounded near zero; its even derivatives are smooth functions of \(u^2\). Hence \(G\) is locally bounded, with additional Vandermonde zeros. With any fixed \(m\) logarithmic insertions the origin flux is bounded by a constant times \(u^{2s+1}|\log u|^{m+1}\), tending to zero uniformly on compact subsets of \(s\ge0\). Differentiated integrands are dominated by finite sums of \(u^{2s}|\log u|^m\), integrable also at \(s=0\). No positive-\(h\) assumption or deleted origin interval enters.

**Coincident nodes.** On a positive face \(u_a=u_b\), \(v(u_a)=v(u_b)\), so the field is tangent. Both \(V(\mathbf u^2)\) and \(\Delta\) vanish, giving at least quadratic vanishing of \(G\). The same local factorization near a common origin follows from evenness. Thus no face flux remains. Divided expressions in (2) are shorthand; the product (3) is what is integrated.

**Infinity.** For fixed \(m\le5\), the complete theta series gives
\(\Phi^{(m)}(u)=O(e^u e^{4(m+2)u}e^{-\pi e^{4u}})\).
Expanding \(\Delta\) and \(X\Delta\) into six products supplies an integrable majorant in all mixed configurations; fixed powers of nodes, \(u\log u\), and logarithmic insertions are dominated by this decay. This pays the entire spatial tail, not just a common-node ray.

These bounds justify (4), its one \(s\) derivative, and the two derivatives of \(M\), locally uniformly for every \(s\ge0\). They establish identities on that full domain. They prove no inequality on \([0,2]\), any remaining compact slab or the unbounded \(s\)-tail. The spatial ray below is only a closure test, not a large-\(s\) estimate.

## 5. Worked obstruction to finite-polynomial closure

The simplest hoped-for closure is \(J=(a+bT)h\). More generally consider precisely
\[
J(\mathbf u)=P(T(\mathbf u))h(\mathbf u),                  \tag{8}
\]
where \(P\) is any fixed finite-degree real polynomial. This would replace the new insertion by finitely many derivatives of \(M\). The complete theta source **does not satisfy (8)**.

To prove this with the full spectrum, set \(\xi=\pi e^{4u}\). The canonical series gives
\[
\Phi^{(m)}(u)=e^u\sum_{n\ge1}P_m(n^2\xi)e^{-n^2\xi},
\quad P_0(y)=2y^2-3y,\quad
P_{m+1}(y)=(1-4y)P_m(y)+4yP_m'(y).
\]
The polynomial \(P_m\) has degree \(m+2\) and leading coefficient \(2(-4)^m\). For \(\xi\ge1\), the entire \(n\ge2\) sum is \(O_m(\xi^{m+2}e^{-4\xi})\): use the convergent sum \(\sum_{n\ge2}n^{2m+4}e^{-(n^2-4)}\). This controls every required derivative through \(m=5\). Consequently
\[
\frac{\Phi'}{\Phi}=-4\xi+9+O(\xi^{-1}),\quad
R=16\xi^2+O(\xi),\quad R'=128\xi^2+O(\xi),\quad
\frac{\Phi^{(4)}}{\Phi}=256\xi^4+O(\xi^3).                \tag{9}
\]
The same finite polynomial formulas differentiate the remainders once where needed.

Fix distinct constants \(a_1<a_2<a_3\), and take \(u_j=t+a_j\), \(t\to\infty\). The \(\xi_j\) have fixed distinct ratios. The leading numerator in \(h\) is \(16\cdot256\,V(\boldsymbol\xi^2)\), while its denominator is \(16^3V(\boldsymbol\xi^2)\). These are equal and nonzero on this ray. The differentiable remainders therefore give
\[
h(t+\mathbf a)=1+O(e^{-4t}),\qquad
Xh(t+\mathbf a)=O(t\log t\,e^{-4t}).
\]
Here \(I_z=O(\log t)\), \(I_R=O(t\log t)\), whereas
\[
L_\Phi=-4\sum_j\xi_j u_j\log u_j+O(t\log t).
\]
Thus
\[
\boxed{\frac{J(t+\mathbf a)}{h(t+\mathbf a)}
\sim-4\pi e^{4t}t\log t\sum_{j=1}^3e^{4a_j},
\qquad T(t+\mathbf a)=6\log t+O(t^{-1}).}                 \tag{10}
\]
The first expression cannot be a fixed polynomial in the second, proving the obstruction. The quotient is used only on this tail ray, where \(h\to1\), not to define the integrated residual. Allowing finite coefficients chosen separately at a fixed \(s\) cannot repair the same pointwise mismatch.

This is not a no-go theorem for Ward methods. It leaves enlarged systems, nonpolynomial source observables, integrated cancellations and the lower bound (7) open. Gaussian models likewise need not satisfy (8), despite their exact solvability. The selected equation has not closed in elementary Mellin moments; the Gaussian-envelope mechanism has not been refuted.

## 6. Gaussian normalization and controls

For \(\Phi_G=e^{-au^2}\), \(a>0\), \(R=4a^2u^2-2a\), \(h=1\), and
\[
I_R=I_z,\qquad J_G=2I_z-a\sum_jz_j\log z_j.
\]
Direct determinant composition gives
\[
M_G(s)=16a^{-3s-3/2}\prod_{j=0}^2\Gamma(s+j+\tfrac12).
\]
Indeed, factor \(\mu_j=\frac12a^{-s-j-1/2}\Gamma(s+j+1/2)\) from column \(j\) of the moment matrix. The remaining rows are \(1\), \(4a(s+j)\), \(16a^2(s+j)(s+j-1)\), with determinant \(128a^3\). This proves \((\log M_G)''=\kappa_3\), including \(s=0\). Equation (4) retains the same normalization with the displayed \(J_G\). Equality is a check, not theta evidence.

| Control | Premise and actual screening result |
| --- | --- |
| Gaussian | Satisfies the generic Ward hypotheses and gives equality. Its \(h=1\) removes theta's insertion variation; unchanged theta reconstruction is absent. |
| Two-point association relaxation | No smooth particle-coordinate density or source derivative determinant: it does not realize the Ward construction. It still blocks replacing the mixed estimate by association alone. |
| Euler-factor sources | Smooth even rapidly decaying sources retain the undivided identity. They lack the unchanged square-spectrum reconstruction in (9). Their \(R'>0\), positive-carrier interpretation and quantitative residual bound are untested here. |
| Weighted-square / finite-square sources | Half-line Ward integration can apply because \(v(0)=0\); it does not need all odd reflection endpoints. These controls lack the complete unchanged spectrum and full reflection. Their \(R'>0\) and \(M(s)>0\) hypotheses are untested. |
| Reflected super-Gaussian and smooth shape / positive-primitive sources | Smoothness and differentiated decay permit the undivided identity; literal theta reconstruction is absent. Positive-carrier applicability and the residual inequality are untested. |

No smooth control is excluded just by deriving a Ward identity. The source-specific asymptotic excludes (8) for theta, not a possible sign estimate. A positive-time collision does not determine this time-zero finite-order comparison.

## 7. Physical meaning and remaining obligation

The positive carrier is a three-particle equilibrium model with dimensionless action
\[
S_s=-sT-\sum_j\log\Phi(u_j)
-\sum_{a<b}\log(z_b-z_a)-\sum_{a<b}\log(R(u_b)-R(u_a)),
\qquad w_s=e^{-S_s}.
\]
The target is its signed insertion \(h\), not the partition function alone. The field \(v=u\log u\) generates \(u\mapsto u^{e^\epsilon}\). Its change-of-variables equation is a finite-dimensional Schwinger–Dyson/Ward identity, not physical heat evolution or a newly constructed local interacting theory. The source \(s\) couples to \(T\); (6) writes the target susceptibility as the mixed response of this deformation and the unchanged insertion.

This is a concrete tool interface: an applicable stress/response inequality must control \(J=Xh+h(I_z+I_R+L_\Phi)\) jointly and imply (7). A carrier loop equation misses \(Xh\), and a finite polynomial in \(T\) cannot replace \(J/h\) pointwise. Those are structural outputs; neither pays a curvature margin. The finite-particle representation is generic, and no novelty survey establishes a new RH reformulation here. A fixed-order pilot does not establish the full all-order criterion.

The existing [Borodin primary source, Section 2](https://arxiv.org/html/math/9804027v1) was re-opened for biorthogonal-ensemble context. No scaling limit, Hermitian-kernel theorem or positivity theorem is imported. All new calculations above are explicit. No new reference-catalog entry or PDF is needed.

**Next: [E] MC04-E01 — Sol.** Complete the frozen separate check in the opening table. Afterwards park this selected closure route unless a distinct source-derived lower bound for (7) is proposed as a new B task. This return issues no numerical campaign or additional assessment.

[packet]: ../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md
[overview]: ../research-overview/01_BIORTHOGONAL_ENSEMBLES_RESEARCH_OVERVIEW_20261101.md
[progress]: ../research-progress/01_BIORTHOGONAL_ENSEMBLES_RESEARCH_PROGRESS_20261101.md
[launch]: ../../numerics/PARALLEL_PHYSICAL_LAUNCH_RECORD_20261101.json
[signreview]: ../../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md
[initial]: ../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md
[comparative]: ../../../reviews/02_PARALLEL_BRANCH_EVALUATION_REVIEW_20261101.md
[routes]: ../../notes/03_IDEAS_AND_POSSIBLE_ROUTES_20261101.md
[physical]: ../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md
[parent]: ../../research-overview/01_MELLIN_CURVATURE_RESEARCH_OVERVIEW_20261101.md
[sources]: ../../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md
[results]: ../../../../../../../result-summaries/README.md
[channels]: ../../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[target]: ../../../../../../../avoid/01_restating_the_target.md
[rereal]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[joint]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scope]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
