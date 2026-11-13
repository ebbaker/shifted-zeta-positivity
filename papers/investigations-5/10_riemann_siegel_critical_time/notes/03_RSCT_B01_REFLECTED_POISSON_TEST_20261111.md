# RSCT-B01: a reflected Poisson constraint and its unpaid arithmetic sign

11 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, RSCT chat0001. Actual backend model and reasoning effort are unavailable: the recorded model-configuration list is empty. Recommendations are not provenance.

**Status: elementary identities and a scoped failed acquisition, checked by the same assistant. No new canonical inequality or zero-exclusion region.** This is the one supporting derivation for [Decision01](../brainstorm/notes/01_RSCT_B01_ARITHMETIC_CONSTRAINT_DECISION_20261111.md). It tests two formulations, then stops at the missing signed arithmetic estimate. No numerical experiment or manuscript is started.

Read the [result index](../../../../result-summaries/README.md), especially [geometry13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) and [controls12](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), particularly [target restatement](../../../../avoid/01_restating_the_target.md), [shared premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md) and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. Fixed source and complete arithmetic expression

Retain the [overview's canonical theta source](../research-overview/01_RSCT_RESEARCH_OVERVIEW_20261111.md), \(\partial_\lambda H=-H_{zz}\), and the inherited finite-attainment reduction. Assume \(T=\Lambda\in(0,1/2]\), all zeros of \(H_T\) real, and an event at \(a>0\) of arbitrary multiplicity \(m\ge2\). No lower bound on T, preferred T log(a), or restriction to double zeros is imposed.

Here is the exact representation used, rather than a leading-saddle substitute. Set \(s_\pm(z)=(1\pm iz)/2\), \(M(s)=s(s-1)\pi^{-s/2}\Gamma(s/2)/16\), and \(f^*(s)=\overline{f(\bar s)}\). With the full contour remainder \(R_{0,N}\) of [Polymath v2 §4, (38)](https://arxiv.org/html/1904.12438v2#S4), define
\[
 r_{T,n}(s)=\pi^{-1/2}\int_{\mathbb R}e^{-v^2}M(s+\sqrt T v)n^{-s-\sqrt T v}\,dv,
\quad
 R_{T,N}(s)=\pi^{-1/2}\int_{\mathbb R}e^{-v^2}R_{0,N}(s+\sqrt T v)\,dv,
\]
\[
 U(s)=\sum_{n\le N}r_{T,n}(s)+R_{T,N}(s),\qquad
 F(z)=U(s_+(z))+U^*(s_-(z))=H_T(z).                 \tag{1}
\]
This is Polymath (35)–(39), for any fixed integer \(N\ge0\), \(T>0\), \(\Re z\ne0\). In particular it applies at \(z=a+iy\), every \(y>0\), including bounded a. The gamma factors and both complete contributions to the entire field remain present; the separate meromorphic s-functions are only used off their excluded real s-line. N stays fixed locally. Sub-Gaussian growth, locally uniformly away from that line, justifies differentiation of the Gaussian integrals:
\[
 F'(z)=\tfrac i2 U'(s_+(z))-\tfrac i2(U^*)'(s_-(z)).       \tag{2}
\]
The primes on U are s-derivatives, including the gamma factor and remainder; F' is the physical z-derivative. Off the real axis one must not replace (1) by twice the real part of one arm. No approximation error has been discarded in (1)–(2). No differentiated version of Theorem 1.3 is imported: that theorem's effective value domain is \(a\ge200,0\le y\le1,0<T\le1/2\).

## 2. First formulation: the complete-arm phase does not acquire a sign

On the real axis let \(A(x)=U(s_+(x))\). Then \(H=2\Re A\), \(H'=2\Re A'\). At a zero with \(A\ne0\), \(A=\rho e^{i\psi}\) gives \(H'=-2\rho\psi'\sin\psi\). The event forces \(\psi'=0\). If \(A=0\), that phase is undefined; the original pair of real-part equations remains the condition. This is the inherited endpoint reformulation, not a bound.

All-real product information belongs to H, not to its chosen imaginary arm component. The reduced information consisting only of H, heat evolution and \(H=A+A^*\) cannot force strict arm rotation: replacing A by \(A+iq\), with q a real-entire heat solution, preserves that information. This observation does **not** authorize changing the canonical RS arm. It identifies what a proof must add from its exact arithmetic definition.

The polynomial control already displayed in [GNP-RS Note20 §5](../../09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/20_GNP_RS_GREEN_GEOMETRY_AND_CRITICAL_TIME_20261111.md) makes the limitation concrete; the calculation here checks its full all-real time range and adds the arm choice. For any \(a,T>0\), put \(s=t-T\) and
\[
 P(t,z)=(z^2-a^2)^2-s(12z^2-4a^2)+12s^2.             \tag{3}
\]
It solves \(P_t=-P_{zz}\). For \(s>0\), its squared roots are
\(a^2+6s\pm\sqrt{8a^2s+24s^2}\), both positive and distinct, since their product is \(a^4+4a^2s+12s^2>0\). At s=0 the roots ±a are double. For \(-a^2/3<s<0\) the squared roots are nonreal; for \(s\le-a^2/3\) they are negative. Hence its all-real threshold is exactly T. Taking \(A=P/2+ic\), real nonzero c, gives \(A(T,a)=ic\), \(A_z(T,a)=0\), so the complete phase is stationary at an all-real threshold. Taking c=0 gives the arm-zero alternative. This control fails the canonical theta source, gamma arithmetic and infinite zero population. It refutes only an inference from the reduced representation/heat/product information.

**Decision on formulation 1:** no arm floor or strict phase derivative is obtained. Do not prescribe a proof of either without a new arithmetic input.

## 3. Selected formulation: complete reflected Poisson mass

The even order-one product and its paired logarithmic derivative are the inherited identities in [Polymath v2, proof of Proposition 3.1, after (33)](https://arxiv.org/html/1904.12438v2#S3). At this all-real slice, list the real zeros r with multiplicity. The imaginary part of the paired sum is absolutely convergent, giving
\[
 Q(a,y):=-y\Im\frac{F'(a+iy)}{F(a+iy)}
       =\sum_r\frac{y^2}{(a-r)^2+y^2}.                 \tag{4}
\]
All-realness ensures both that \(F(a+iy)\ne0\) and that **every summand is positive**. These are the actual extra inputs beyond Schwarz symmetry. They do not give a positive numerical lower bound for \(|F|\).

Evenness supplies multiplicity m also at −a. Define
\[
 k(a,y)=1+\frac{y^2}{4a^2+y^2},\qquad
 S(a,y)=\sum_{r\notin\{a,-a\}}\frac1{(a-r)^2+y^2},
\]
where all m copies of each event root are removed. Then the exact threshold constraint is
\[
 Q=m k+y^2 S\ \ge\ m k\ \ge\ 2k.                  \tag{5}
\]
For canonical H, S is strictly positive because further zeros exist. Multiplicities elsewhere remain in S. This is a **necessary geometric inequality**, not an arithmetic upper estimate.

The independently evaluable arithmetic expression selected for testing is the denominator-free signed quantity
\[
 \mathcal B(a,y)=2k|F|^2+y\Im(F'\overline F),\qquad z=a+iy.       \tag{6}
\]
Equations (1)–(2) give its full arithmetic definition. If \(V=U(s_+)\), \(W=U^*(s_-)\), the expression contains
\[
2k(|V|^2+|W|^2+2\Re V\bar W)
+y\Im(V'\bar V+W'\bar W+V'\bar W+W'\bar V).
\]
Here V',W' are z-derivatives. Every reflected mixed term and every remainder interaction is retained. At the event,
\[
 \mathcal B=\big((2-m)k-y^2S\big)|F|^2<0.             \tag{7}
\]
Thus an independently proved positive value of (6) at even one y would exclude that specified event. This formulation also handles a vanishing real-axis complete arm: no division by A is made.

**Classification before acquisition.** At an all-real canonical slice and fixed a>0, the existence of a y>0 with \(\mathcal B(a,y)>0\) is equivalent to a not being a multiple zero. Indeed, if H(a)≠0 then \(Q\to0\) as y→0; if a is simple, \(Q\to1\); if it is multiple, (5) forbids positivity at every y. Therefore the unrestricted all-threshold exclusion remains the inherited RH-strength endpoint problem. Checking (4)–(7) supplies no evidence for RH. A useful milestone would require a specified domain and a newly proved arithmetic margin there. None is acquired in this pass.

## 4. Value and derivative costs, without assuming a denominator floor

Let f,g approximate the **complete** F,F' at the same z, with rigorous bounds \(|F-f|\le\epsilon_0\), \(|F'-g|\le\epsilon_1\). They must include both arms, gamma/cutoff effects, truncation and evaluation errors. Define \(\mathcal B_{f,g}=2k|f|^2+y\Im(g\bar f)\). Direct expansion gives
\[
 |\mathcal B-\mathcal B_{f,g}|\le
 E_B:=2k(2|f|\epsilon_0+\epsilon_0^2)
 +y(|g|\epsilon_0+|f|\epsilon_1+\epsilon_0\epsilon_1).       \tag{8}
\]
A usable certificate would require \(\mathcal B_{f,g}>E_B\). Formula (8) is elementary conditional bookkeeping; it provides neither a favorable arithmetic value nor the error inputs. It needs no f-nonvanishing assumption. For a quotient implementation with \(|f|>\epsilon_0\), the corresponding payment is
\[
 |Q+y\Im(g/f)|\le
 y\frac{\epsilon_1+|g/f|\epsilon_0}{|f|-\epsilon_0}.        \tag{9}
\]
All-realness by itself does not pay this denominator. Multiplying by a nonconstant normalization also costs its logarithmic derivative: if F=cf, then \(F'/F=c'/c+f'/f\). The gamma carrier cannot be dropped from (6) or (9).

There is a specific small-y cancellation cost. Write \(H_T(a+w)=c_m w^m+O(w^{m+1})\), \(c_m\ne0\), and \(S_0=\sum_{r\ne\pm a}(a-r)^{-2}>0\). Isolation of a and the convergent squared reciprocal tail give \(S(a,y)\to S_0\). At an exact double event,
\[
 \mathcal B(a,y)=-|c_2|^2 S_0 y^6(1+o(1)),            \tag{10}
\]
whereas for m>2 its leading term is \((2-m)|c_m|^2 y^{2m}\). At m=2 the separate terms in (6) are of order y^4; their cancellation leaves order y^6 after removing the reflected double pair. For the **separate absolute envelope (8)**, \(\epsilon_0=o(y^4)\) and \(\epsilon_1=o(y^3)\) suffice to make its error o(y^6). This is a fixed-event sufficient accuracy condition, not a lower bound on actual RS error, a uniform-in-T estimate, or an impossibility theorem. Correlated residuals can behave differently. Merely making y small without paying both errors does not supply a usable sign.

## 5. Analytical collision-control screen

This applies the [control catalog](../../../../result-summaries/12_collision_controls_and_screening.md) analytically on each control's actual witness domain; it does not rerun its certificates. Equations (4)–(7) automatically hold for even order-at-most-one fields with the stated all-real product and nonzero origin. Consequently those premises cannot imply the opposing sign.

| Control | Outcome for this proposed acquisition; failed or unavailable canonical premise |
| --- | --- |
| Polynomial (3) | At T, Q=2k and B=0 exactly. Strict positivity and strict arm rotation fail under representation/heat/all-real information alone. Full theta source and infinite population fail. |
| Positive atomic BW-01 control | A genuine all-real threshold with infinitely many double zeros; B<0 at its event for every y>0. Positive source, heat equation and all-realness survive. Canonical theta arithmetic, full imaginary profile and eventual simplicity at threshold fail. |
| Exact finite-profile and continuous-source extensions | At their genuine all-real threshold events the same mass obstruction applies when the paired product hypotheses hold. Matching finitely many observations is insufficient; unchanged coefficients, full profile and eventual simplicity fail. |
| Euler-factor/translated controls | Certified nonreal-zero witnesses rule out deriving a universal threshold bound from their shared source properties. The witness time is not automatically an all-real event: (5) is only applied if that premise is established. Unchanged canonical coefficients fail. |
| Weighted-square, finite-tail and finite-prime-orbit controls | Their local collisions are not asserted finite all-real thresholds; the finite-tail class has no all-real time. Hence (4)'s positive measure cannot be imported at their local event. Full reflection and/or complete theta coefficients fail. |
| Reflected super-Gaussian, smooth shape and positive primitive | Shape/reflection identities do not give the missing sign. Their recorded local events alone do not establish all-realness; no threshold mass computation is claimed there. Canonical square-series arithmetic fails. |
| RH-conditional normalized endpoint | At the stated all-real time-zero endpoint, multiplicity obstructs the same strict mass bound; the construction is conditional and outside T>0 as stated. Ordinary Dirichlet arithmetic fails. No theta counterexample follows. |
| Variable-readout and heat counter-kernels | Full physical cosine readout, generator and/or canonical source fail; no common threshold assumption is invented. |
| Relaxed Green/profile populations | Exact canonical integer zero population and boundary-field identification fail. The fixed three-profile relaxation obstruction does not cover all complete-source estimates. |

For the positive-source control, the [BW-01 proof §§2–3](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md) gives \(H_q(T,z)=A(\cos(\ell z)+q)^2\), \(\ell=\arccos(-q)/20\), \(1/2\le q<1\), with a positive three-atom heat source and exact all-real threshold T. At a=20, m=2 and infinitely many other real zeros give S>0, so (7) is strictly negative. This is an exact application, with no source approximation. It does not refute a bound using the unchanged canonical theta arithmetic.

## 6. First unpaid premise and ownership

The first unpaid premise is a signed lower bound for (6), on the canonical complete arms, beating (8) at a useful y and over a declared time-height domain. Neither phase symmetry nor all-realness supplies it. No favorable canonical point, region, constant or onset was acquired. This is the bounded pass's stop condition.

[HCB's current register](../../03_heat_flow_collision_bounds/research-progress/02_POST_CALIBRATION_RESEARCH_PROGRESS_20261028.md) already owns complete first-jet acquisition and complete-population Poisson acquisition. Its [Note01 §§1–3](../../03_heat_flow_collision_bounds/notes/01_WHOLE_CLUSTER_POISSON_TRANSFER_AND_ACQUISITION_20261026.md) has the same positive Poisson measure and shrinking-scale quotient costs. Its integrated L2 descendant statistic with margin 2/3 is **not** (6), and no equivalence or automatic transfer of its constants is asserted. The overlap is acquisition and missing signed arithmetic, not identical consumers.

HCB-05's leading-pair failures concern its stated norms and tL families; they do not disprove (6). Conversely, recasting a generic first-jet floor in RSCT notation would duplicate that owner's request. [OA's post-E02 gate](../../08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md) remains unmet: this note provides no certified positive starting pair, factor floor or upper force. No sibling task is activated.

**Return:** scoped failure of acquisition from the retained representation, all-real product, and generic positive-source information. The signed complete-arithmetic route remains open. No E01 proof contract is justified; the source-specific inequality and method are still missing.
