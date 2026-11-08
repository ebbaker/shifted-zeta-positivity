# Green potential and logarithmic resolvent: research overview

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Explicit worker dispatch selected **gpt-6.1-sol / ultra**; this is the supplied actual selection, not independent backend verification. Root model/effort unavailable.

**Evidence level: documentation/setup and inherited internally assessed results.** This overview fixes a dictionary and a bounded next question. The [shared synthesis](../../brainstorm/notes/19_TND_O_GREEN_CORRELATION_BIFURCATION_SYNTHESIS_20261107.md), [setup request](../../brainstorm/notes/18_TND_O_E22_BIFURCATION_SETUP_REQUEST_20261107.md), [inputs40](../../research-progress/handoffs/40_TND_O_E22_BIFURCATION_INPUTS_20261107.json) and [dispatch40](../../research-progress/handoffs/40_TND_O_E22_DISPATCH_20261107.json) own the bifurcation provenance. The [sole register](../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md) owns all TND-OG live statuses. No mathematical gain follows from opening this branch.

## 1. The exact chain and its clocks

For real \(u\), define the theta formula below; its primitive integrations use \(u\ge0\):

\[
 \vartheta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},\qquad
 p(u)=\frac{e^u}{2}\{\vartheta(e^{4u})-1\}
      =e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}}.
\]

The complete Jacobi identity gives \(p(-u)-p(u)=\sinh u\), \(p'(0)=-1/2\), and

\[
 \Phi(u)=\frac{p''(u)-p(u)}8
 =e^u\sum_{n\ge1}\{2r_n(u)^2-3r_n(u)\}e^{-r_n(u)},
 \qquad r_n(u)=\pi n^2e^{4u}.
\]

The full source \(\Phi\) is smooth, even and strictly positive. The reflection belongs to the **complete sum**; reflecting a finite prefix does not supply matching odd derivatives at zero. These are the inherited [source derivation, canonical reflection and bounds](../../manuscript/sections/02_source.tex) and [Note11 §3, endpoint-correct primitive dictionary](../../notes/11_TND_O_B02_CRITICAL_COEFFICIENTS_THETA_AND_RODGERS_TAO_20261106.md), reused without a fresh primary-paper check.

Define, with no normalization by \(H_\lambda(0)\),

\[
 F_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 H_\lambda(z)=\frac12\int_{\mathbb R}F_\lambda(u)e^{izu}\,du
             =\int_0^\infty F_\lambda(u)\cos(zu)\,du,
\]
\[
 H_0(z)=\frac18\xi\!\left(\frac{1+iz}{2}\right)
       =\frac18\xi\!\left(\frac12-\frac{iz}{2}\right),\qquad
 \partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]

The second xi argument uses xi reflection. The [introduction's clock](../../manuscript/sections/01_introduction.tex) is \(h(\tau,z)=H_{\lambda_0-\tau}(z)\), \(h_\tau=h_{zz}\): increasing imaginary time decreases Newman parameter. The complete source supplies entire dependence and every **fixed** source/time/position derivative on compact parameter sets. It does not supply uniformity in a growing derivative order for free.

Avoid the old notation collision by writing

\[
 J^{\rm prim}_\lambda(z)=\int_0^\infty p(u)e^{\lambda u^2}\cos(zu)\,du.
\]

[Note11(8)–(10)](../../notes/11_TND_O_B02_CRITICAL_COEFFICIENTS_THETA_AND_RODGERS_TAO_20261106.md) gives exactly

\[
 8H_\lambda=\frac12+(2\lambda-1-z^2)J^{\rm prim}_\lambda
          +4\lambda z\partial_zJ^{\rm prim}_\lambda
          -4\lambda^2\partial_z^2J^{\rm prim}_\lambda.
\]

In particular \(8H_0=1/2-(1+z^2)J^{\rm prim}_0\). The endpoint \(1/2\) is essential; primitive positivity does not sign the oscillatory transform.

The **source-space** resolvent is another object:

\[
 G^{\rm src}_\lambda=8(1-\partial_u^2)^{-1}F_\lambda
      =4\int_{\mathbb R}e^{-|u-v|}F_\lambda(v)\,dv.
\]

[Source section, related transform](../../manuscript/sections/02_source.tex) proves \(G^{\rm src}_\lambda(u)\sim8H_\lambda(i)e^{-|u|}\) and
\(16H_\lambda(z)=(1+z^2)\int G^{\rm src}_\lambda(u)e^{izu}du\) only as an absolutely convergent raw integral for \(|\Im z|<1\). Entire continuation comes from \(H\), not a wider raw strip. In general \(G^{\rm src}_\lambda\ne e^{\lambda u^2}G^{\rm src}_0\). Neither this source resolvent nor \(J^{\rm prim}\) is the Green statistic below, or the proposed zero-space logarithmic resolvent \(R\).

Thus the chain is **theta sum → endpoint-correct primitive \(p\) → complete source \(\Phi\), \(F_\lambda\) → entire \(H_\lambda\) → logarithmic potential \(\log|H_\lambda|\) → its strip Green functional**. Every arrow is an exact representation; the final useful signed upper estimate is still missing.

## 2. The inherited positive Green sum and its actual consumer

Write \(z_j=x_j+iy_j\), retaining every multiplicity. For \(0\le\lambda\le1/2\), the inherited canonical strip is \(|y_j|\le1\). Set

\[
 a=\pi/8,\quad K(t)=\frac1{16\cosh(at)},\quad
 \mathcal G(t,y)=\operatorname{atanh}\frac{\sin(ay)}{\cosh(at)}.
\]

Each boundary kernel has mass \(1/2\). Use \(J^{\rm G}\) to distinguish the old second \(J\):

\[
 J^{\rm G}_\lambda(X)=\int_{\mathbb R}K(x-X)
       \{\log|H_\lambda(x)|+\log|H_\lambda(x+8i)|\}\,dx
       -\log|H_\lambda(X+4i)|
     =\sum_{j:y_j>0}\mathcal G(X-x_j,y_j)\ge0.
\]

[Note25](../../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md) and [manuscript Green section](../../manuscript/sections/17_green_strip.tex) prove the complete identity, absolute logarithmic integrability including multiple real boundary zeros, absolute upper-zero convergence, scalar invariance and no omitted outer/harmonic term. [E16 Review09](../../reviews/09_TND_O_E16_LOCALIZED_METRICS_ASSESSMENT_20261107.md) accepts its stated scope. These properties use the complete opposite-paired product and count/tail payments; an arbitrary local inverse-Laplacian construction does not inherit the no-outer-term conclusion.

A declared upper zero with \(0<d\le y_j\le1\), \(|x_j-X|\le r\), forces

\[
 J^{\rm G}_\lambda(X)\ge m(d,r):=\frac{\sin(a)d}{\cosh(ar)}.
\]

A separately acquired **strict upper bound below \(m(d,r)\)** excludes this class. The coarse \(O(\log(3+|X|))\) upper bound does not. Boundary truncation and zero-tail errors are separate: the former has an explicit growing-height polynomial/logarithmic factor times \(e^{-aR}\), the latter an explicit count factor times \(e^{-aR}\); use the full equations in the [Green proof](../../manuscript/sections/17_green_strip.tex) before any joint limit. Continuity through collisions is inherited, but a double event gives a square-root Green signal, not the transverse \(y^2\) statistic's Lipschitz law or monotonicity.

Only at \(\lambda=0\), [Decision15](../../brainstorm/notes/15_TND_O_B04_R4_SIGNED_METRIC_COMPARISON_20261107.md), [Green prime proposition](../../manuscript/sections/17_green_strip.tex) and [E17 Review10](../../reviews/10_TND_O_E17_PRIME_BASELINE_ASSESSMENT_20261107.md) give

\[
 J^{\rm G}_0(X)=\mathcal L(X)-P(X)+\mathcal G(X,1),
\quad \mathcal L(X)=\int K(x-X)\log|\zeta(1/2-ix/2)|\,dx,
\]
\[
 P(X)=\sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\log n}
       \frac{n^{-5/2}}{1+n^{-4}}\cos\!\left(\frac X2\log n\right),
\quad |P-P_N|\le\frac23N^{-3/2}\quad(N\in\mathbb Z,\ N\ge2).
\]

Here \(\Lambda_{\rm vM}\) is von Mangoldt, not the Newman threshold. The **plus** term \(\mathcal G(X,1)\) pays the zeta pole: the factor \(s-1\) has a zero at \(z=i\), for \(s=1/2-iz/2\). Positivity yields the lower comparison \(\mathcal L\ge P-\mathcal G(X,1)\). The missing exclusion comparison has the opposite direction,

\[
 \mathcal L(X)<P(X)-\mathcal G(X,1)+m(d,r).
\]

No Euler product is assigned to nonzero Newman time. Universal \(J^{\rm G}_0=0\) is an RH-type reformulation; it is stated once, without treating checks as evidence for it.

## 3. The author's intermediate field

Use \(\partial_z=(\partial_x-i\partial_y)/2\), \(\partial_{\bar z}=(\partial_x+i\partial_y)/2\), so \(\Delta=4\partial_z\partial_{\bar z}\). For the full planar zero measure \(\nu_\lambda=\sum_{\zeta\text{ distinct}}\operatorname{mult}(\zeta)\delta_\zeta\), local factorization gives

\[
 \Delta\log|H_\lambda|=2\pi\nu_\lambda,\qquad
 R_\lambda(z):=\frac{H'_\lambda(z)}{H_\lambda(z)}
       =2\partial_z\log|H_\lambda(z)|,\qquad
 \partial_{\bar z}R_\lambda=\pi\nu_\lambda.
\]

The equalities involving zeros are distributional; \(R\) is locally integrable and has a simple pole of residue \(m_j\) at a zero of multiplicity \(m_j\). Away from zeros it is holomorphic. Solving only \(\partial_{\bar z}R=\pi\nu\) leaves a holomorphic summand; solving for the logarithmic potential leaves harmonic data. Canonical boundary/asymptotic/product information fixes that ambiguity. One cannot discard it by calling the intermediate field an inverse derivative.

The exact source route, on a zero-free domain, is

\[
 R_\lambda(z)=
 \frac{i\int_{\mathbb R}uF_\lambda(u)e^{izu}\,du}
      {\int_{\mathbb R}F_\lambda(u)e^{izu}\,du}
 =-\frac{\int_0^\infty uF_\lambda(u)\sin(zu)\,du}
          {\int_0^\infty F_\lambda(u)\cos(zu)\,du}.
\]

Source positivity bounds separate absolute moments; it does not give a lower denominator on the real boundary. If source approximations obey \(|H-\widehat H|\le\epsilon\), \(|H'-\widehat H'|\le\epsilon_1\), a contour/domain margin \(b=|\widehat H|-\epsilon>0\) pays, pointwise,

\[
 |R-\widehat H'/\widehat H|
 \le\epsilon_1/b+|\widehat H'|\epsilon/(b|\widehat H|).
\]

A lower bound for this margin must be acquired and propagated; approximation accuracy alone is insufficient. At actual zeros division is unavailable. A deflation must retain the removed residues and multiplicities, and a contour must keep a nonzero boundary margin. [Note11 §4](../../notes/11_TND_O_B02_CRITICAL_COEFFICIENTS_THETA_AND_RODGERS_TAO_20261106.md) already reuses a local contour-force interface, with its prior finite-pilot cost comparison; no contour speedup is assumed here.

The inherited product gives, locally uniformly away from zeros,

\[
 R_\lambda(z)=\sum_{\zeta\in\mathcal R_\lambda}
       \left(\frac1{z-\zeta}+\frac1{z+\zeta}\right)
     =\sum_{\zeta\in\mathcal R_\lambda}\frac{2z}{z^2-\zeta^2}.
\]

One representative of every opposite pair, with multiplicity, is required; \(H_\lambda(0)>0\) excludes a zero at zero. This product has no surviving exponential factor. Unpaired infinite sums need a convergence/renormalization prescription and cannot replace this formula silently. Subtracting a reference/background field must account for its holomorphic part and all of its poles; subtracting the unknown defect itself would assume the information sought.

Finally, on zero-free space-time patches only, the inherited heat equation gives the standard local algebra

\[
 \partial_\lambda R=-R_{zz}-2RR_z,
 \qquad \partial_\tau R=R_{zz}+2RR_z
 \quad(\lambda=\lambda_0-\tau).
\]

The first is anti-viscous Burgers in Newman time. Its nonlinear terms at poles are not assigned an unproved global distributional meaning. These representations and local dynamics are a candidate estimating interface, not a favorable signed estimate, a new literature result, or canonical zero exclusion.

## 4. What E20/E21 settled, and what they did not

| Inherited assessed result | Exact useful scope | Still unavailable |
| --- | --- | --- |
| [Note28](../../notes/28_TND_O_E20_PAID_QUADRATIC_GREEN_COMPARISON_20261107.md), accepted by [E21 Review12](../../reviews/12_TND_O_E21_SIGNED_ACQUISITION_ASSESSMENT_20261107.md) | At \(\lambda=0\), \(F_Q(z)=((s-1)/s)\zeta(s)\prod_{p\le Q}(1-p^{-s})\), \(c_Q=F_Q(X+4i)\), \(\epsilon_Q^2=\int\lvert F_Q/c_Q-1\rvert^2d\mu_X\): \(0\le J^{\rm G}_0\le\tfrac12\log(1+\epsilon_Q^2)\). Nonzero safe center, compact complete-source conversion, both remote boundaries, denominator error and valid pointwise order of limits are paid. | Small actual residual; \(\epsilon_Q^2<e^{2m}-1\) is a sufficient condition, not an acquired gain. Pole cancellation is already in \(F_Q\); do not add \(\mathcal G(X,1)\) again to this representation. |
| [Note28 §7](../../notes/28_TND_O_E20_PAID_QUADRATIC_GREEN_COMPARISON_20261107.md) | For each fixed finite Euler product, the actual squared residual has an unbounded logarithmic high-center average. | No conclusion at every individual/exceptional/defect-conditioned center; no lower bound for \(J^{\rm G}\), nor nonreal-zero existence. |
| [Note29](../../notes/29_TND_O_E20_R2_UNIFORM_EULER_LENGTH_OBSTRUCTION_20261107.md) | Uniform divergent average \(\gg_{\theta,\phi}\sqrt{\log(T/2)}-O_{\theta,\phi}(1)\), for primorial length \(P_Q\le(T/2)^\theta\), fixed \(0<\theta<17/33\), one \(Q\) throughout each interval \([T,2T]\). | No exclusion of adaptive \(Q(X)\), longer products, arbitrary coefficients/mollifiers, revised widths, or signed logarithmic cancellation. Imported moment constants were not made numerical. |
| [Decision17 §6](../../brainstorm/notes/17_TND_O_B04_R5_SIGNED_ACQUISITION_DECISION_20261107.md), accepted by [Review12 §5](../../reviews/12_TND_O_E21_SIGNED_ACQUISITION_ASSESSMENT_20261107.md) | Added Euler-control Green potential grows while fixed safe-half-plane jets converge and any prescribed finite coefficient prefix eventually agrees. This defeats stability from those incomplete observations across that enlarged class. | No nonuniqueness of analytic continuation and no failure theorem for estimates using all quantitative fixed canonical data. Controls change conductor/residue/local temperedness and lack literal theta source with uniform source/count constants. |

[Setup return40](../../research-progress/handoffs/40_TND_O_E22_BIFURCATION_RETURN_20261107.json) and [additional-source identities](../../research-progress/handoffs/40_TND_O_E22_ADDITIONAL_SOURCES_20261107.json) record the documentation boundary. [Returns36](../../research-progress/handoffs/36_TND_O_E20_PAID_QUADRATIC_COMPARISON_RETURN_20261107.json), [37](../../research-progress/handoffs/37_TND_O_E20_R2_UNIFORM_EULER_LENGTH_RETURN_20261107.json) and [38](../../research-progress/handoffs/38_TND_O_E21_SIGNED_ACQUISITION_ASSESSMENT_RETURN_20261107.json) identify the exact proof/assessment versions. No universal failure of Green methods, localized metrics or arithmetic source estimates was established.

## 5. Bounded mechanisms and required passage to the consumer

**TND-OG-B01** compares at most these two directions and one focused clarification; [the plan](../research-plan/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PLAN_20261107.md) sets its stop rule.

1. **First-order source/resolvent comparison, including integrated contour recovery.** Choose a full-source estimating norm/observable for \(R\), a justified normalization/reference or deflation and all explicit residues. Source-ratio estimation and integration along declared zero-free paths/contours (or a justified test kernel) are two modes of this one mechanism. Freeze the region and denominator treatment; retain periods, boundary zeros, holomorphic ambiguity and side/tail terms. Explain which genuinely coupled canonical information beats separate numerator/denominator bounds and survives integration as a signed upper Green margin. A stable safe-line estimate or the Green identity again is insufficient.
2. **Optional coefficient-optimized arithmetic preconditioning.** Only if useful after the primary comparison, test \(A_T(s)=\sum_{n\le N}a_nn^{-s}\), \(a_1=1\), \(|a_n|\le1\), \(N\le(T/2)^\theta\), fixed \(0<\theta<17/33\) and one polynomial per interval. The old unissued B04 r6 idea is subordinate here, not a third live task. The inherited safe-center floor is \(|A_T(5/2-it)|\ge2-\zeta(5/2)\ge1/3\); combined normalization/source payments and zeros elsewhere in the strip still require accounting. A BCR mean-square improvement alone is no localized or defect-conditioned upper comparison. Changing this coefficient class is a visible conceptual choice, not a silent E execution.

Kernels, windows, safe contours and any preconditioner are **revisable conceptual choices**, not fixed scientific commitments. A route may terminate with a precise obstruction for its declared information class. Every selected route must specify an explicit unbounded-height and source-index/radial route, account for \(d\downarrow0\) (or state the remaining uniform theorem), and any growing derivative order actually used. Pointwise finite acquisition along a parameter sequence is distinct from uniform cost, all-center coverage or residual smallness. No numerical campaign is activated.

The parent [prior-work locator20](../../brainstorm/notes/20_TND_O_PRIOR_HIERARCHY_LOCATOR_20261107.md) identifies the earlier complex-potential/Wirtinger note. Its regulated \(W=2\partial_z^2\log(|H|^2+\varepsilon^2)\) is a distinct field, not this \(R\); the locator records source identity and the limited inspection. This setup does not claim a new Wirtinger representation.

## 6. Required controls and classification

Apply the [result index](../../../../../../result-summaries/README.md), [collision controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns index](../../../../../../avoid/README.md), [target rule01](../../../../../../avoid/01_restating_the_target.md), [control-premise rule02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [coordinate caution03](../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scope rule07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). The following is the inherited screen, **not a new control experiment**.

| Control | Shared premises that cannot discriminate | Actual canonical premise absent |
| --- | --- | --- |
| Positive-source Euler-factor family | Positivity, reflection, strong fixed moments, generic logarithmic-derivative/Green identities and heat evolution | Extra \(1+c\cos(\alpha z)\) factor; unchanged full theta source/xi identity fails. E21's safe-line family changes conductor to \(p^2\), residue and tempered local roots, with nonuniform source/count constants. |
| Weighted-square and finite-prefix/tail families | Square support, positive source and their specifically matched finite endpoints/moments | Complete normalized infinite theta coefficients and full reflection conjunction; a matched prefix is not complete arithmetic. |
| Reflected super-Gaussian control | Full even reflection, positivity and positive Fourier–Gram forms, with an actual collision | Integer-square theta expansion and unchanged xi/zeta identity. |
| Smooth shape/positive-primitive controls | Smoothness, decay, positivity and the particular primitive endpoints/asymptotics recorded for each control | Exact canonical theta square coefficients; positive primitive or algebraic spectral asymptotics alone do not supply them. |
| Atomic/polynomial/variable-kernel examples, when used | Only their separately stated local algebra, moments or diagnostics | Do not silently assign a smooth canonical source, full profile, cosine/Newman observation or canonical count constants. |

Failing an exact identity does not imply failing every inequality derived from it. Generic \(\partial_{\bar z}R=\pi\nu\), Burgers and Jensen steps hold for their admissible controls and do not discriminate theta. A genuine defect prevents an admissible control from satisfying the relevant strict exclusion threshold, but a finite box away from its event need not reject it. A useful milestone is a quantitative bound or scoped obstruction; an RH-equivalent vanishing criterion and a new coordinate representation are not such a gain. Reference ownership and inspection limits are recorded [here](../references/README.md).
