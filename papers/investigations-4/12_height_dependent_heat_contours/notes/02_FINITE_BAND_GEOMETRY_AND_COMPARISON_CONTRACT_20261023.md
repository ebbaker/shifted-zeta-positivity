# One finite-band physical-cap contract

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Derivations by the authoring assistant with separate same-model checks; no specialist review.

**Status: HDC-01 complete as a specification, not as a theta certificate.** This note fixes one observable, its entire boundary, an independently checkable input interface, and an equally informed direct comparator. [Note 03](03_COMPLETE_COUPLED_EXPRESSION_AND_COMPARISON_20261023.md) derives the complete expression to estimate. No numerical lower bound or favorable theta margin is asserted.

This is a finite quantitative milestone under [avoid 01](../../../../avoid/01_restating_the_target.md), not an RH-equivalent criterion. Read the [result index](../../../../result-summaries/README.md), [local heat geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../avoid/README.md), [coupled-estimation rule](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md). The [sole progress register](../research-progress/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md) distinguishes this completed contract from its unacquired inputs.

## 1. Freeze the field, geometry, and observable

Use the unchanged normalized source

\[
 H(\tau,z)=\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du,
 \quad
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
 \quad H_\tau=-H_{zz}.
\]

The normalization is the one in [Rodgers–Tao, equations (1)–(4)](https://arxiv.org/html/1801.05914). Write \(\tau=t+i\sigma\), \(z=x+iy\), and orient spacetime by \(dt\wedge d\sigma\wedge dx\wedge dy\). Fix, before any source acquisition,

\[
 A=26,\quad B=46,\quad b=2,\quad
 \epsilon=\delta=Y=10^{-4},\quad \rho=10^{-2},
\]
\[
 \Omega=[A,B]+i[-b,b],\qquad
 D=[-\epsilon,\delta]+i[-Y,Y],\qquad W=D\times\Omega.
 \tag{1}
\]

These are trial parameters, not certified safe widths. Here height is the real H-coordinate, twice the zeta ordinate at time zero. No high-height asymptotic is invoked in this low finite band. The constant backward width avoids an unpaid slope term. A changed parameter tuple defines a new recorded comparison, rather than silently changing the observable after seeing a result.

Let \(G=(H,H_z)\),

\[
 \mathcal A=\frac{\operatorname{Im}(G^*dG)}{|G|^2},\qquad
 \mathcal C=\frac{\mathcal A\wedge d\mathcal A}{4\pi^2}.
\]

The target is the **entire fixed-box cap**

\[
 I_0=\int_{\{t=0,\ |\sigma|\le Y,\ z\in\Omega\}}\mathcal C,
 \tag{2}
\]

with forward orientation \(d\sigma\wedge dx\wedge dy\). It includes the spatial complement of all selected root disks. It is neither a real angular integral nor just a sum over real zero trajectories.

The cap population means **every zero of \(H(\tau,\cdot)\) inside \(\Omega\), with multiplicity**, including nonreal zeros. Its size \(N\) is to be acquired by the wall procedure below; this note does not claim a count from a picture of real zeros. The fixed-box integral does not require a count to be defined. The optional factorization method requires that count, and never substitutes a chosen real subpopulation for it.

Keep the positive face \(t=\delta\) in the auxiliary cross-zero domain W. The primary lower-bound calculation uses \(W_-=[-\epsilon,0]\times[-Y,Y]\times\Omega\). Its validity requires regularity on \(\partial W_-\), including the internal t=0 face, not merely regularity on \(\partial W\). An eventual \(\delta\downarrow0\) is a separate task. No positive-time anchor or conclusion follows from choosing a positive number \(\delta\).

## 2. Complete faces and endpoint events

The following table gives outward orientations on W_-; every coordinate integral has increasing limits.

| Face | Outward orientation | Contribution |
| --- | --- | --- |
| t=0 | \(+d\sigma\,dx\,dy\) | \(I_0\) |
| t=−epsilon | \(-d\sigma\,dx\,dy\) | \(-I_{-\epsilon}\) |
| sigma=+Y / −Y | \(-dt\,dx\,dy\) / \(+dt\,dx\,dy\) | Both included in \(S_\epsilon\) |
| x=B / A | \(+dt\,d\sigma\,dy\) / \(-dt\,d\sigma\,dy\) | Both included in \(S_\epsilon\) |
| y=+b / −b | \(-dt\,d\sigma\,dx\) / \(+dt\,d\sigma\,dx\) | Both included in \(S_\epsilon\) |

Corners have zero three-dimensional measure. Shared cell faces cancel as oriented physical chains, before evaluation or inequalities. Computational cells must have matching physical interfaces. A gap between patches, a change of radius, a mismatched population, or an exposed attachment annulus is not a shared face and must be retained. No smooth cutoff is used in this first contract; adding one later introduces its derivative terms.

Assume an independently established floor \(|G|\ge g_\partial>0\) on \(\partial W_-\). The inherited degree theorem then gives

\[
 I_0=\underbrace{I_{-\epsilon}-S_\epsilon}_{B_\epsilon}+Q_-,
 \qquad Q_-=\sum_{p\in\operatorname{int}W_-:G(p)=0}\binom{m_p}{2}\ge0.
 \tag{3}
\]

No interior gap floor, real-root interval, or interior first-jet floor is assumed. The physical degree counts complex joint events. Isolatedness of heat multiple zeros is classical; [Papanicolaou–Kallitsi–Smyrlis, Theorem 4.1](https://ejde.math.txstate.edu/Volumes/2021/44/papanicolaou.pdf) uses forward heat, changed here by \(t\mapsto-\tau\). The local degree and normalization are proved in the inherited [boundary derivation](../../manuscript/topological_zero_transport/boundary.tex).

If a boundary floor cannot be certified, this parameter tuple is **unverified**, not event-free. If a boundary joint zero actually occurs, the unpunctured target (2) is not assigned a value by this contract. To study it, declare small four-dimensional balls, retain their inward-oriented spherical pieces on the punctured domain, and keep the deleted cap pieces and all local contributions. For a fully interior excision of degree q, its inner boundary contributes −q. An event on a cap intersects a sphere in only a portion; its contribution is not automatically half an integer. Recovering an unpunctured or one-sided limiting observable requires a separate local limit theorem. In particular, an event at t=0 cannot be removed by calling the right face \(0^+\).

## 3. A direct formula without projective denominators

Set \(H_j=\partial_z^jH\), and

\[
 E=|H_0|^2+|H_1|^2,\quad L=H_1^2-H_0H_2,\quad
 N_*=H_2^2-H_1H_3,\quad M=H_1H_2-H_0H_3.
\]

Define real functions

\[
 f=\frac{\Re(L\overline{N_*})}{2\pi^2E^2},\quad
 p=\frac{\Im(L\overline{N_*})}{2\pi^2E^2},\quad
 r=\frac{\Re(M\overline{N_*})}{2\pi^2E^2},\quad
 s=\frac{\Im(M\overline{N_*})}{2\pi^2E^2}.
\]

Then, wherever E>0,

\[
 \boxed{\mathcal C=f\,d\sigma\wedge dx\wedge dy
 -p\,dt\wedge dx\wedge dy
 +r\,dt\wedge d\sigma\wedge dy
 -s\,dt\wedge d\sigma\wedge dx.}
 \tag{4}
\]

**Proof.** The normalized sphere-volume formula evaluated on three vectors a,b,c is
\(\det_{\mathbb R}(G,d_aG,d_bG,d_cG)/(2\pi^2E^2)\), in real target coordinates \((\Re H,\Im H,\Re H_z,\Im H_z)\). Substitute
\(G_t=(-H_2,-H_3)\), \(G_\sigma=iG_t\), \(G_x=(H_1,H_2)\), \(G_y=iG_x\). The four real determinants are respectively \(\Re(L\overline{N_*})\), \(-\Im(L\overline{N_*})\), \(\Re(M\overline{N_*})\), \(-\Im(M\overline{N_*})\), proving (4). The accompanying exact-arithmetic record checks these determinant identities independently of heat examples.

Consequently \(I_t=\int_{-Y}^Y\int_A^B\int_{-b}^b f(t,\sigma,x,y)\,dy\,dx\,d\sigma\), and the **whole** other-face sum is

\[
\begin{aligned}
 S_\epsilon={}&\int_{-\epsilon}^0\int_A^B\int_{-b}^b
 [p(t,Y,x,y)-p(t,-Y,x,y)]\,dy\,dx\,dt\\
 &+\int_{-\epsilon}^0\int_{-Y}^Y\int_{-b}^b
 [r(t,\sigma,B,y)-r(t,\sigma,A,y)]\,dy\,d\sigma\,dt\\
 &+\int_{-\epsilon}^0\int_{-Y}^Y\int_A^B
 [s(t,\sigma,x,b)-s(t,\sigma,x,-b)]\,dx\,d\sigma\,dt.
\end{aligned}\tag{5}
\]

Only jets through order three are needed to evaluate these densities. Zeros of L or \(H_z\) away from E=0 are harmless in (4). Thus projective-chart degeneration does not force a spurious singularity into the direct baseline. For future smooth graphs t=−epsilon(x), (4) gives the forward cap density **f+epsilon'(x)r**, evaluated on the graph. This does not remove its other faces or provide an estimate for them.

## 4. Optional root charts only where they are needed

For the phase estimator, cover the open broken time path

\[
 \gamma:\ -iY\longrightarrow-\epsilon-iY\longrightarrow-\epsilon+iY\longrightarrow iY
 \tag{6}
\]

by finitely many certified patches. On each patch require disjoint inverse charts
\(q=H/H_z\), \(|q|\le\rho\), around the selected simple zeros, lying strictly inside \(\Omega\). The common fixed radius is the proposed rho in (1); it is not guaranteed to work. Charts are required on neighborhoods of these boundary edges, **not over the interior of the time rectangle**. Use the same rule for optional direct charts on \(v=[-iY,iY]\).

A sufficient certificate uses a spatial disk on a time patch: certify one H-zero counted with multiplicity and a uniform wall inequality

\[
 \inf_{\partial D_j}|H|>\rho\sup_{\partial D_j}|H_z|.
 \tag{7}
\]

Rouché then gives exactly one zero of H−qH_z for every \(|q|\le\rho\). Counting multiplicity makes it simple. Its holomorphic dependence gives the inverse chart, and H_z there cannot vanish, since that would be a multiple zero of H inside the one-simple-root disk. This proves chart existence from wall data. Matching charts must agree on overlaps; otherwise retain the transition region in the complement. It does not continue those disks across an unknown interior collision.

The projective wall has zero physical flux only on an actual regular chart with constant radius. If no useful chart is certified, (4)–(5) still specify the full problem. The complete signed complement J in Note 03 contains every part of the three-dimensional faces not accounted for by the certified disks. Its value is not assumed small or zero.

## 5. Source inputs and their current status

| Input | Independent acquisition route | Status in this note |
| --- | --- | --- |
| Complete canonical source, heat identities, real symmetry | Displayed theta series and integral, with absolute convergence on compact complex domains | Available analytic formulas |
| Joint enclosures for H0,…,H3 on the physical boundary; quadrature errors | One shared source truncation and correlated coefficient/Taylor data, including both tails below | Not acquired for (1) |
| Boundary floor g_partial | Finite boundary cover using correlated first-jet centers and derivative budgets | Not acquired; required for the original cap |
| Spatial H wall floor over D, population N | Uniform nonvanishing on D×boundary(Omega), plus one argument-principle count | Optional for (4), required for all-root factorization; not acquired |
| Root disks, H_z floors, radius rho, matching atlas | Boundary-patch Rouché tests (7), validated roots and containment | Optional; not acquired |
| Analytic factor/exterior derivatives | Outer-wall Cauchy formula below, or retain them implicitly in complete root jets | Analytic interface available; constants unacquired |
| Complex-time remainder / complement J | Joint source quadrature on every remaining face, with geometric and rounding errors | Unacquired; no real-axis substitution |
| K'' for optional transverse Taylor reduction | Differentiated complete root jets, through spatial order seven, with paid charts/denominators | Optional, unacquired; not required for boundary line quadrature |
| Negative-time all-real interval, uniform pair gap, RH | No source in this contract | Not assumed |

For all points in (1), the finite moment budgets

\[
 M_k=\int_0^\infty u^k e^{\delta u^2+bu}|\Phi(u)|\,du
\]

bound \(|\partial_\tau^a\partial_z^cH|\le M_{2a+c}\). First-derivative control for the four-jet densities uses jets through order five. At a boundary-cell center c with coordinate half-widths \(r_t,r_\sigma,r_x,r_y\), for example,

\[
 \|G\|\ge\|G(c)\|-(r_t+r_\sigma)\sqrt{M_2^2+M_3^2}
 -(r_x+r_y)\sqrt{M_1^2+M_2^2}.
 \tag{8}
\]

Use the lower endpoint of a certified center norm. This is a boundary test and imposes no interior floor. It is a conservative acquisition method; sharper signed data are shared with both estimators.

If the computation keeps n≤n0 and u≤U0, the jet error includes both
\(\int_0^{U_0}u^ke^{\delta u^2+bu}\sum_{n>n_0}|\Phi_n(u)|du\) and
\(\int_{U_0}^\infty u^ke^{\delta u^2+bu}|\Phi(u)|du\), as well as finite quadrature and rounding errors. Explicit convergent majorants are

\[
 0<\Phi(u)\le\frac{2\pi^2e^{9u-\pi e^{4u}}}{1-16e^{-3\pi}},\quad u\ge0,
\]
\[
 \sum_{n>n_0}|\Phi_n(u)|\le
 \frac{2\pi^2(n_0+1)^4e^{9u-\pi(n_0+1)^2e^{4u}}}{1-q_{n_0}},\quad
 q_{n_0}=\left(\frac{n_0+2}{n_0+1}\right)^4e^{-\pi(2n_0+3)}<1.
 \tag{9}
\]

These follow by dropping the negative source summand and bounding successive positive terms by a decreasing geometric ratio. Their integrals still require validated evaluation; no numerical tail budget is claimed here. Truncation is an approximation to the complete source, never a replacement field asserted to have theta's zero geometry.

To obtain exterior information without an interior pair gap, let \(\Gamma=\partial\Omega\), certify \(|H|\ge m_w>0\), \(|H_z|\le L_w\) there for every tau in D, and count N at one anchor by \((2\pi i)^{-1}\oint H_z/H\). The wall floor keeps N constant through interior collisions. Power sums from \((2\pi i)^{-1}\oint z^kH_z/H\) and Newton identities define the monic polynomial P of all these roots. For \(U=H/P\), \(a=\partial_z\log U\) is analytic in the interior and

\[
 a(\tau,z)=\frac1{2\pi i}\oint_\Gamma
 \frac{H_z(\tau,\zeta)/H(\tau,\zeta)}{\zeta-z}\,d\zeta,
 \quad
 |\partial_z^r a|\le\frac{|\Gamma|}{2\pi}\frac{r!L_w}{m_wd^{r+1}}
 \tag{10}
\]

at distance at least d from the wall. Residues cancel all root poles, including multiplicities, leaving a. Thus this input does not divide by an interior gap. Differentiating the wall ratio supplies time derivatives. For the basic estimator, the combined root-jet formula in Note 03 avoids separate bounds on a entirely.

## 6. Matched comparison and controls

Both methods receive the same complete source oracle, precision, signed correlations, Gaussian smoothing identity, wall data, and any acquired atlas or factorization. The direct baseline is a rigorous lower bound for (2), using (4) or an equally informed root reduction **plus its full complement**. The deformed method bounds (4)–(5) jointly and transfers by (3). Include all data acquisition costs, even checks made over faces absent from the direct cap. Report total source evaluations, precision, subdivisions, wall/atlas work, wall-clock time, final intervals and all errors. Reused input costs and marginal evaluation costs should be reported separately.

Acceptance is a strictly improved complete lower bound, equal strength at less verified cost, a simpler applicable theorem, or a proved failure confined to the specified estimator class. No theta comparison is reported until both bounds and their costs are acquired. In particular, lower source amplitude at negative time is not itself success for a normalized phase integral.

The full collision-family screen is logical here, not a new numerical rerun of published certificates. All generic identities admit the controls. Unchanged complete arithmetic is missing for Euler-factor, reflected and positive-primitive modifications; full reflection and the complete normalized sequence are missing for finite weighted-square sources; finite-prime controls fail full reflection and simultaneous complete arithmetic; RH-conditional normalized endpoint controls fail ordinary Dirichlet-series arithmetic. These distinctions permit a future theta-specific estimate but do not prove that a weak bound derived from them rejects a control. See the [control register](../../../../result-summaries/12_collision_controls_and_screening.md) for exact preservation lists.

Elementary checks are required on event-containing domains: \(H=(z-36)^2-2\tau\) has a time-zero boundary event and invalidates the unpunctured regular-cap premise; \(H=(z-36)^2-2(\tau+\epsilon/2)\) has one interior negative-time event and gives \(B_\epsilon=I_0-1\), not equality; a quadratic shifted to a later positive time prevents automatic later continuation. The sine heat field retains a nonzero analytic-factor contribution even though its gaps are constant. Note 03 adds a polynomial example disproving a positive-sign shortcut for the complete relative-energy contribution.

HDC-01 ends with a fixed, testable contract. HDC-02 is the exact coupled expression in Note 03; HDC-03 must acquire the above theta data before HDC-04 can report a numerical comparison. This session starts no broad height sweep and proves no decreasing height schedule.
