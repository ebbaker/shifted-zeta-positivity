# J-B08 initial evaluation: the odd-velocity flow and its return-direction obstruction

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Contributor **`/root/branch05`**, actual recorded **gpt-6-astra (Codex), reasoning effort ultra**; child runtime identity `01a199a2-23a9-7242-a397-bf490dab72e9`, confirmed in local `turn_context`. Parent research chat `01a1999e-49d4-7a52-9e8a-95b0c5c430f1`; its unique registration and all shared records are owned by the coordinator. This is an inherited-source, same-model analytical contribution, not independent specialist review. The coordinator suggested the particularly simple atomic control in Section 4; the worker checked its moments and implications.

**J-B08 is complete as a bounded conceptual assessment of one candidate.** The odd logarithmic velocity preserves the required full reflection, has an explicit globally defined source path, and gives exact moment/Jensen evolution. For each fixed degree and shift, rescaled Jensen polynomials approach a simple-root Laguerre polynomial as auxiliary time tends to positive infinity. This is a generic changed-source fact. The useful return to theta would run in the opposite direction, and generic backward hyperbolicity preservation fails already at degree two, including for smooth strictly positive even sources. The actual theta orbit is not a counterexample; its reverse-direction mixed-moment estimate remains unproved.

**Disposition:** retain the exact flow/limit as a tool; stop the generic backward-preservation mechanism for this velocity. A theta-specific return theorem requires genuinely new signed information. No new canonical coefficient range, arbitrary-order/small-shift result, or RH conclusion is obtained. The accepted physical-time-zero order-three source pair and normalized comparison, and the negative origin curvature, are unchanged. No root sampling, flow simulation or numerical campaign was performed.

## 1. One path, complete reflection and global existence

Select precisely the candidate at the end of [Investigation05 chat0053](../../../../05_radial_theta_collision_geometry/notes/CHAT0053_SOURCE_TRANSPORT_UNBOUNDED_STRIP_OBSTRUCTION_20261031.md):
\[
v(u)=\frac14\tanh(2u),\qquad
\psi_s(u)=\frac12\operatorname{arsinh}(e^{s/2}\sinh(2u)),\qquad
\partial_s\psi_s=v(\psi_s),\quad \psi_0(u)=u.                 \tag{1}
\]
For every finite real s, this is an odd smooth increasing diffeomorphism of the real line, fixes zero, has inverse psi_(-s), and satisfies the group law. Its derivative is
\[
\psi_s'(u)=\frac{e^{s/2}\cosh(2u)}{\sqrt{1+e^s\sinh^2(2u)}}>0.
\]
Define the pushforward of the full even canonical source by
\[
\Phi_s(u)=\Phi(\psi_{-s}(u))\psi_{-s}'(u),\qquad u\in\mathbb R.
                                                               \tag{2}
\]
It satisfies
\[
\partial_s\Phi_s+\partial_u(v\Phi_s)=0,
\qquad \int_0^\infty\Phi_s(u)\,du=c_0.                       \tag{3}
\]
The velocity sign in (3) is fixed by the actual characteristic in (1). This is **auxiliary** source transport, not physical Newman time, and not a conservative evolution of a determinant density. Only the source mass is invariant; its higher moments and coefficient determinants change.

Oddness of psi and evenness of its derivative make Phi_s even. Thus every odd source derivative at zero vanishes, at every finite s; the first-endpoint defect of the old raw radial flow is absent. Since |v|<=1/4,
\[
|\psi_s(u)-u|\le |s|/4.                                      \tag{4}
\]
On a compact s interval, the explicit diffeomorphism and its inverse have controlled fixed-order derivatives. The original complete theta derivative bounds therefore retain double-exponential decay after a bounded shift of u. This pays every fixed polynomial moment, fixed source derivative, and parameter differentiation below, uniformly on compact s intervals. There is no lower boundary flux because v(0)=0; every polynomially weighted outer flux vanishes by the full tail. Equations (1)–(2) give existence independently of any polynomial root or determinant sign.

The obstruction in chat0053 applies to its **different** raw exterior field, fixed logarithmic observation and explicitly recentered variant. We do not transfer that theorem to (1). Full reflection repairs its failed endpoint premise; it does not itself prove root preservation.

## 2. Exact moment and Jensen evolution, with the unclosed quantities exposed

For integer m>=0 use the original conventions
\[
b_m(s)=\int_0^\infty u^{2m}\Phi_s(u)\,du
      =\int_0^\infty\psi_s(u)^{2m}\Phi(u)\,du,
\quad c_m(s)=\frac{b_m(s)}{(2m)!},\quad\gamma_m(s)=m!c_m(s).
\]
The unambiguous notation b_m means the moment of u^(2m), not the moment of u^m. For m>=1, differentiating the pushforward, or integrating (3) by parts with both endpoints retained, gives
\[
\boxed{b_m'(s)=\frac m2\int_0^\infty
          u^{2m-1}\tanh(2u)\Phi_s(u)\,du.}                 \tag{5}
\]
Also b_0'=0. Set
\[
a(u)=\frac{v(u)}u=\frac{\tanh(2u)}{4u},\quad a(0)=\frac12,
\qquad
\delta_m(s)=\frac{m!}{(2m)!}\int_0^\infty u^{2m}a(u)\Phi_s(u)\,du.
\]
Then gamma_m'=2m delta_m. For fixed d,n>=0 define
\[
P_s(X)=J_s^{d,n}(X)=\sum_{j=0}^d\binom dj\gamma_{n+j}(s)X^j,
\qquad Q_s(X)=\sum_{j=0}^d\binom dj\delta_{n+j}(s)X^j.
\]
The exact polynomial equation is
\[
\boxed{\partial_sP_s=2(n+X\partial_X)Q_s.}                 \tag{6}
\]
It contains a different family of mixed moments. In particular, (6) is not an established repulsive second-order equation in P alone.

This failure of a finite moment closure is a concrete information issue. For any finite N>=m>=1, the function u^(2m-1)tanh(2u) is not in the span of 1,u^2,...,u^(2N) on the half-line: its large-u leading power is the odd power 2m-1, whereas a nonzero polynomial in u^2 has an even leading degree. Thus the mixed integral in (5) is not determined on the class of positive smooth even sources by that finite moment list. To see this without an unsupported formal series, choose compactly supported smooth perturbations away from zero annihilating the N+1 polynomial moment functionals but not this extra functional. Such a perturbation exists by finite-dimensional linear algebra: otherwise the extra functional would be in their span on every compact test space, forcing the pointwise identity just ruled out. Add or subtract a sufficiently small multiple on its compact support from a strictly positive even base, then reflect. Positivity, all odd endpoints and the unchanged tails survive, the finite moment list is identical, and the mixed moment differs.

This excludes a universal autonomous finite-moment closure on that source class. It does **not** exclude an additional identity special to the exact theta orbit, a nonlocal equation, or inequalities involving Q. Formally expanding tanh into an unbounded power series would not close (6), and no such exchange or derivative campaign is used.

At a simple root x_i(s), the equation gives only
\[
\dot x_i=-\frac{2[nQ_s(x_i)+x_iQ_s'(x_i)]}{P_s'(x_i)}.          \tag{7}
\]
There is no signed pair-repulsion term available from (7) alone. For every finite s the leading coefficient gamma_(n+d)(s) is strictly positive, so degree d is retained; all coefficients are positive, hence any real roots are negative. Equation (7) does not extend through multiple roots without additional information.

## 3. The known limit is at positive auxiliary infinity

Let L_s=s/4 for s>0. For every fixed u>0,
\[
\frac{\psi_s(u)}{L_s}\longrightarrow1\qquad(s\to+\infty).
\]
For s>=4, (4) gives 0<=psi_s(u)/L_s<=1+u. The theta source has every polynomial moment, so dominated convergence gives, for each fixed m,
\[
\frac{b_m(s)}{L_s^{2m}}\longrightarrow c_0.                \tag{8}
\]
There is no atom at zero in the source measure, so the exceptional u=0 does not alter the integral. Consequently, for each fixed pair d,n,
\[
\begin{aligned}
L_s^{-2n}J_s^{d,n}(X/L_s^2)
&\longrightarrow c_0\sum_{j=0}^d\binom dj
                  \frac{(n+j)!}{(2n+2j)!}X^j\\
&=\frac{c_0n!}{(2n)!}\,{}_1F_1\left(-d;n+\tfrac12;-X/4\right).
\end{aligned}                                                       \tag{9}
\]
The convergence is coefficientwise, hence uniform on every compact X set. The factorial equality follows from
\((2n+1)_{2j}=4^j(n+1/2)_j(n+1)_j\), retaining the distinction between c and gamma.

[DLMF 18.5.12](https://dlmf.nist.gov/18.5.E12) identifies the right-hand polynomial, up to a positive constant, with \(L_d^{(n-1/2)}(-X/4)\). Its parameter is greater than -1; the Laguerre row of [Table 18.3.1](https://dlmf.nist.gov/18.3#T1) gives the positive orthogonality weight on (0,infinity), and [DLMF 18.2(vi)](https://dlmf.nist.gov/18.2.vi) gives simple zeros in that interval. Therefore the limit in (9) has d distinct negative real zeros. Only these selected primary passages were inspected; no broader chapter or root-flow theorem is imported.

Choose disjoint real intervals around those d roots on which the limiting polynomial has opposite endpoint signs. Coefficient convergence preserves those signs for sufficiently large s. The degree remains exactly d, so the approximating polynomial has all d roots real, distinct and negative. This proves
\[
\boxed{\text{For each fixed }d,n,\text{ there is }S_{d,n}<\infty
\text{ such that }J_s^{d,n}\text{ is hyperbolic for all }s\ge S_{d,n}.} \tag{10}
\]
Positive rescaling of X and multiplication by a positive scalar do not change real-rootedness. For d=0 the assertion is trivial. No effective S_(d,n), uniform all-degree S, or finite-time all-Jensen hyperbolic source is asserted. A uniform start time is not required for an all-degree proof: a valid backward-preservation argument for each fixed pair from its own S_(d,n) would suffice. The missing ingredient is that return theorem, not uniformity of the thresholds. This changed-source concentration fact uses positivity, absence of an origin atom and moments, not theta arithmetic. It is not the classical large-coefficient-shift theorem and does not advance canonical small-shift hyperbolicity at s=0.

To use (10) to reach theta, one must propagate **backward** from a large positive s to zero. That direction cannot be supplied by a generic source-transport preservation theorem, as the next section proves.

The other endpoint does not supply a free starting family. As s tends to negative infinity, psi_s(u) tends to zero and b_m(s) tends to zero for m>=1, by domination by u^(2m) for s<=0. Thus J_s^(d,0) tends to the constant c_0, while n>0 gives the zero polynomial: degree is lost. A degenerate limiting polynomial cannot justify forward hyperbolicity of nearby polynomials. If this loss is removed by scaling, arcsinh(z)<=z gives instead
\[
e^{-ms}b_m(s)\longrightarrow
\int_0^\infty\left(\tfrac12\sinh(2u)\right)^{2m}\Phi(u)\,du,          \tag{11}
\]
whose domination follows from the complete theta tail. The resulting moment sequence has no proved Jensen hyperbolicity here. Equation (11) is a description of the same path's endpoint, not a second candidate flow.

## 4. An exact quadratic direction test and a smooth backward counterexample

This finite calculation tests the direction of (1), not the actual theta sign. For any nondegenerate positive source with the stated moments set
\[
\kappa(s)=\frac{b_0(s)b_2(s)}{b_1(s)^2}.
\]
Writing E_m for expectation against u^(2m)Phi_s/b_m, equation (5) gives
\[
\frac d{ds}\log\kappa=4(E_2a-E_1a).                      \tag{12}
\]
The function a is strictly decreasing on u>0, since
\[
a'(u)=\frac{2u\operatorname{sech}^2(2u)-\tanh(2u)}{4u^2}<0.
\]
For z>0 the numerator sign follows from sinh(z)cosh(z)>z, whose difference has positive derivative. Tilting E_1 by u^2 gives
\[
E_2a-E_1a=\frac{\operatorname{Cov}_{E_1}(u^2,a(u))}{E_1u^2}<0,       \tag{13}
\]
for a distribution on at least two distinct positive radii. The covariance sign follows directly by averaging
\((U^2-V^2)(a(U)-a(V))<0\) over independent copies, so no association theorem is imported. In particular kappa decreases strictly with **increasing** s. For the Jensen quadratic
\[
J_s^{2,0}(X)=b_0+b_1X+\frac{b_2}{12}X^2,
\qquad \operatorname{disc}=b_1^2\left(1-\frac\kappa3\right).        \tag{14}
\]
This gives forward preservation for this quadratic once kappa<=3. It gives no all-degree theorem and works against the desired reverse direction.

For an exact boundary example, take half-line mass
\[
\mu=\frac89\delta_1+\frac19\delta_{\sqrt{10}}.
\]
Its moments are b_0=1, b_1=2, b_2=12, so J^(2,0)=(1+X)^2 and kappa=3. The two tilted weights give
\[
E_2a-E_1a=\frac{10}{27}\big(a(\sqrt{10})-a(1)\big)<0.     \tag{15}
\]
Transport the two radii by (1). By (12)–(15), for sufficiently small epsilon>0 the polynomial at s=epsilon has two simple negative real roots, while at s=-epsilon it has a nonreal conjugate pair. Running this same source flow backward for 2epsilon therefore loses hyperbolicity. The multiple root at zero is handled by the explicit discriminant rather than the singular simple-root formula (7).

Atoms alone do not satisfy the classical smooth endpoint assumptions. The counterexample has a smooth version without claiming that an arbitrary smoothing preserves an exact double root. Fix one sufficiently small epsilon for which the two endpoint discriminants have strict opposite signs. Approximate the two atoms by nonnegative smooth unit-mass bumps supported near their strictly positive radii; extend evenly across zero and add a sufficiently small positive multiple of Phi/c_0, adjusting the bump weights to retain total half-line mass one. The resulting source is strictly positive, smooth, fully even, and has complete theta-type tails outside a compact set. The transported b_0,b_1,b_2 at the two fixed times converge to the atomic values, because psi_(plus/minus epsilon) is continuous on the compact bump supports and the added theta mass has finite moments. Their strict discriminant signs therefore persist. Hence backward preservation fails also in this smooth positive even class. No exact-zero retuning or numerical root search is needed. These sources fail the unchanged canonical source/arithmetic premise; no failure on the actual theta orbit has been shown.

This negative result is distinct from chat0053's raw-transport obstruction. It concerns only generic backward hyperbolicity preservation for the reflection-compatible velocity (1), already at (d,n)=(2,0); it is not an unbounded-strip claim or a prohibition on all source flows.

## 5. The remaining theta obligation and the full small-shift scope

The three ingredients now have sharply different statuses:

| Ingredient | Outcome |
| --- | --- |
| Exact path to theta at s=0, with full odd-endpoint compatibility and finite-time existence | Established by (1)–(5). |
| Known hyperbolic comparison at large positive time | Established for each fixed d,n by (8)–(10); the threshold depends on the pair. |
| Propagation from that comparison back to zero | Generic preservation contradicted; no canonical theta-specific replacement estimate is proved. |

For a prospective double root x<0 with P=P'=0 and P''!=0, the local expansion is
\[
(X-x)^2\sim-2\,\frac{\partial_sP(s,x)}{P''(s,x)}\,\Delta s.
\]
For reverse time tau=-s, the infinitesimal inward condition for keeping a double pair real is
\[
\frac{2(nQ+xQ')(x)}{P''(x)}\ge0.                          \tag{16}
\]
The control above has the opposite sign. For the actual theta orbit, an estimate proving the appropriate boundary condition would need to constrain the mixed source moments in Q using theta information that the controls do not provide. Merely assuming (16) restates the local root-preservation obligation; it is not an acquired estimate. Even a proof at ordinary doubles would still need compatibility at higher multiplicities, continuity through the boundary, and a global continuation argument on the finite interval down to zero. All of these remain unpaid.

At any fixed finite s, positive leading coefficients remove degree loss as a finite-time issue, but they do not prevent root collisions. Limits at plus/minus infinity require the scalings already stated and cannot be silently substituted for a finite starting time. Fixed small n, especially n=0 with arbitrary d, remains open. The triangular determinant identity D_(r,0)=c_0^r is a different assertion and does not fill this gap. The r/k and d/n indices and the c/gamma/raw-moment normalizations remain separate.

## 6. Controls, sources and bounded disposition

Read with the [result index](../../../../../../result-summaries/README.md), [theta cluster](../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [control cluster](../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../avoid/README.md), especially [target classification](../../../../../../avoid/01_restating_the_target.md), [shape-only premises](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [same-model checks](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [numerics before a question](../../../../../../avoid/10_numerics_ahead_of_the_question.md), and [joint estimates](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

| Control/class | Actual premise and scope |
| --- | --- |
| Gaussian | Positive/even/moment hypotheses give this path and the fixed-pair limit. The nonlinear transport is not asserted to remain Gaussian or to preserve all its Jensen polynomials. It lacks theta arithmetic. |
| Euler-factor, reflected smooth/super-Gaussian, positive-primitive sources | With full reflection and finite moments they share the moment evolution and generic positive-time concentration argument. They fail unchanged canonical reconstruction; no uncomputed intermediate Jensen sign is assigned to any named control. |
| Weighted-square and finite-prime sources | Missing complete reflection is not repaired merely by using an odd velocity; it preserves the evenness of inputs that already have it. Where full evenness fails, arbitrary-order endpoint formulas retain the defect. Changed coefficients also fail the canonical premise. |
| Atomic boundary control and smooth versions in Section 4 | Directly refute generic backward preservation for the selected velocity. The atoms fail smoothness; the explicitly described smooth versions satisfy positivity, all odd endpoints and rapid tails but fail exact theta arithmetic. |
| Previously recorded positive-time collisions | Not used as counterexamples to a time-zero finite-order theta assertion. The failure here is proved from the actual auxiliary flow and a separate source control. |

The all-Jensen criterion is the existing RH-equivalent destination, not a new criterion. The fixed-pair asymptotic and the scoped reverse-direction counterexample are bounded facts about this chosen changed-source path. No canonical new sign is inferred from their coexistence.

**Next: [B] theta-specific reverse-direction estimate decision — Astra, deferred to the coordinator's priorities.** If this path is retained, freeze the pilot (d,n)=(3,0), the generator (1), and a prospective negative double root with P''!=0. Select one actual theta identity or quantitative inequality and determine whether it supplies the sign in (16) for the complete mixed moments, without assuming hyperbolicity at zero. The output must be an independent signed bound with its source hypotheses and full tails, or a precise failed comparison. The pilot tests a method inside the known low-degree baseline. Stop after that one proposed estimate fails the information test; do not replace the unclosed mixed-moment problem by a flow simulation, root scan or increasing-degree campaign. Higher multiplicities and all-degree propagation remain separate even if the pilot passes. No numerical E contract is ready. The generic backward-preservation claim for this velocity should not be pursued further.

## 7. Reading, input versions and provenance

The worker read the root AGENTS/model/large-file/chat-history rules; the branch brief, Note15, Note14, ideas/live register, accepted Review01 and the relevant raw-transport note passages; and the required result/avoid material. Historical inputs and all shared records are untouched. The return derives (1)–(16) analytically; the only imported root fact is the classical Laguerre property, with primary passages inspected online on 1 November 2026:

- DLMF 18.5.12: finite Laguerre/confluent-hypergeometric normalization.
- DLMF Table 18.3.1: Laguerre orthogonality on (0,infinity), weight exp(-x)x^alpha, and alpha>-1.
- DLMF 18.2(vi), opening zero statement: degree-d orthogonal polynomials have d simple zeros in their interval of orthogonality.

These links are given in Section 3. This is selected-passage inspection, not full-paper or independent theorem verification. The existing common `NISTDLMF` catalog entry can receive this follow-up record; no new article, PDF, or local numerical record is needed. The coordinator alone makes catalog updates.

| Input | SHA-256 |
| --- | --- |
| [Branch brief](README.md) | `5db46cf4b04a07458ebcfde4a59a4a66168d0aead22280be50107a0cf5453ebd` |
| [Note14](../14_HIGHER_ORDER_SIGNED_AVERAGING_AND_RADIAL_FLOW_FEASIBILITY_20261101.md) | `d8b9160e158317462d75a59d7535f500898cfb51345284d33287cf24eafd14f0` |
| [Note15](../15_CONTINUATION_PARALLEL_BRANCH_EVALUATION_20261101.md) | `2d2fd23efd67b019c484ec551f779f1feaf4ffe08046ba457de6d5a3b1ec1f1a` |
| [Accepted Review01](../../reviews/01_J_E03_GLOBAL_SIGN_AND_SIGNED_AVERAGING_ASSESSMENT_20261101.md) | `c13e63e7c017285932e75d2add333b8d683e5ed3b9a096f6e20e31e88e0a2dfe` |
| [chat0053 source-transport note](../../../../05_radial_theta_collision_geometry/notes/CHAT0053_SOURCE_TRANSPORT_UNBOUNDED_STRIP_OBSTRUCTION_20261031.md) | `8c388de9e456a33825e06c53671fd46da56827748e2b466e11fb110779e06c49` |
