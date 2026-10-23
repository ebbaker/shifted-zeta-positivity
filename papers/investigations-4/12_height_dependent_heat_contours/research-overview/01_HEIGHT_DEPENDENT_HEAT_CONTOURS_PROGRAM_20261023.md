# Height dependent heat contours research program

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**.

**Objective:** obtain a useful bound for the original time-zero physical cap by estimating a complete height-dependent negative-time deformation, preserving structural cancellations before taking inequalities. **Initial status:** generic identities and a conditional finite-cluster radius are inherited; a source-specific complete estimate and a demonstrated comparative gain remain open. The [progress register][progress] owns execution status.

Execution update, 23 October 2026, **gpt-6-astra (Codex), effort ultra**: HDC-01 is now specified in [Note 02](../notes/02_FINITE_BAND_GEOMETRY_AND_COMPARISON_CONTRACT_20261023.md), and HDC-02's complete expression is derived in [Note 03](../notes/03_COMPLETE_COUPLED_EXPRESSION_AND_COMPARISON_20261023.md). The full fixed-box cap retains the complement of all root disks. Boundary-only charts suffice for the deformation representation; a global event-free tube is unnecessary. The new polynomial control shows that a nonnegative real relative energy can contribute negatively after complex-time integration. Shared holomorphic coefficient models give identical signed path estimates. These scoped results have [separate same-model review](../reviews/01_FINITE_CONTRACT_AND_COUPLED_ESTIMATOR_REVIEW_20261023.md); no source-specific theta interval or useful gain is claimed. The earlier formulas below retain their stated hypotheses.

Current priority update, 23 October 2026, **gpt-6-astra, ultra**: the [second overview](02_PAIR_SPECTRUM_CURVED_CONTOURS_AND_CONDITIONAL_SIMPLICITY_PROGRAM_20261023.md) now organizes the analytical pair-spectrum, curved-contour and backward-transport program, first for RH implying simple zeros. The physical-cap objective below remains a parallel branch, with its existing contracts and statuses preserved.

## Scope and success criteria

The author's proposal has three parts: pass just to the right of zero at a small fixed positive time for each finite height cutoff; deform backward to \(t=-\epsilon(h)\); and divide the region into smaller cells transported with the heat-zero geometry so that shared faces cancel. The refined objective is to make the original integral easier to estimate through this deformation.

A useful first result is a stronger certified lower bound for a fixed \(I_0\), the same bound at lower source or verification cost, or an equally strong analytical theorem under substantially simpler hypotheses. A complete bound on event count is a later consumer. An exact rewriting or a smaller separately estimated cap is not itself the acceptance criterion. Any comparison must use the same source information and retain the complete observable.

Follow the [result index][results], [local heat-geometry summary][geometry], [avoid index][avoid] and its [classification rule][a01]. A finite bound is judged by its quantitative output. A future all-height RH or simplicity criterion must be classified separately; finite checks are not evidence for an equivalent global statement.

## Field and boundary contract

Use the unchanged canonical theta field

\[
H(\tau,z)=\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du,
\qquad H_\tau=-H_{zz},
\]

with the complete normalized theta source \(\Phi\). Write \(\tau=t+i\sigma\), \(z=x+iy\), and \(G=(H,H_z)\). The inherited physical form is

\[
\mathcal C=\frac{\mathcal A\wedge d\mathcal A}{4\pi^2},
\qquad
\mathcal A=\frac{\operatorname{Im}(G^*dG)}{|G|^2}.
\]

For a compact domain with \(G\ne0\) on its complete boundary,

\[
Q(W)=\int_{\partial W}\mathcal C
=\sum_{p\in W:G(p)=0}\binom{m_p}{2}\ge0.
\]

This counts complex joint events with local degree. A physical cap is three-dimensional and includes imaginary time; it must not be replaced silently by a real angular integral.

For the collar between \(t=-\epsilon(x)\) and \(t=0\), give both cap integrals the forward parameter orientation and let \(S_\epsilon\) be every other outward face. Define the coupled observable

\[
B_\epsilon:=I_{-\epsilon}-S_\epsilon,
\qquad I_0=B_\epsilon+Q_-\ge B_\epsilon.
\tag{1}
\]

A lower bound on \(B_\epsilon\) transfers without interior event exclusion. Exact equality requires \(Q_-=0\); an upper bound requires control of the event term. Events on the time-zero cap require excisions and their charges, or a separately justified limiting formulation.

For the original cross-zero enclosure, keep \(t=\delta_{H_{\max}}>0\) until the full boundary estimate has been established. If that full region has charge zero, it excludes its enclosed events. A limit \(\delta_{H_{\max}}\downarrow0\) must preserve boundary and population control.

## Height dependence and moving cells

The first research contract should use one finite band \(h\in[h_1,h_2]\), with \(h\) the real \(H\)-coordinate, and declare the spatial imaginary width, imaginary-time thickness, projective radii, right face and negative left face. A piecewise-constant \(\epsilon\) by height band is an acceptable first geometry if all joining faces are retained.

The candidate microscopic normalization is

\[
\ell(h)=\tfrac14\log\frac{h}{4\pi},
\qquad \epsilon(h)=\frac{c(h)}{\ell(h)^2}.
\tag{2}
\]

Use (2) for \(h>4\pi\). It is a proposed scale, not a proved safe width. Individual gaps and surrounding interactions can force much smaller values. A decreasing envelope is useful only after positive local margins have been independently established. A smooth graph adds \(dt=-\epsilon'(x)\,dx\) to the physical pullback.

On an actual projective chart, transport \(q=H/H_z\) by

\[
\frac{dz}{d\tau}
=\frac{H_zH_{zz}-HH_{zzz}}{H_z^2-HH_{zz}}.
\tag{3}
\]

This agrees with zero motion at \(H=0\). Constant-\(|q|\) sides have zero flux, but the chart can fail at \(H_z^2-HH_{zz}=0\) away from a collision. Complementary charts, imaginary-time faces and exposed joining pieces remain. Shared physical faces cancel before estimates; an assumed globally regular root-tube covering cannot be used as its own noncollision proof.

## The renormalization mechanism to test

For a finite simple cluster with \(H=U\prod_j(z-z_j)\), set

\[
\mathscr D=\prod_jH_z(\tau,z_j),\qquad a=\partial_z\log U.
\]

The [founding derivation][brainstorm] gives

\[
K_{\mathscr D}:=\frac{d}{d\tau}\log\mathscr D
=8\sum_{j<k}(z_k-z_j)^{-2}+\mathcal B_U,
\tag{4}
\]

\[
\mathcal B_U=
2\sum_{j<k}\frac{a(\tau,z_k)-a(\tau,z_j)}{z_k-z_j}
+\sum_j\bigl(a(\tau,z_j)^2-3a_z(\tau,z_j)\bigr).
\]

The finite triple-interaction cancellation is already derived and algebraically checked. The research task is to estimate the complete expression for theta. For positive reference separations \(r_{jk}\), the real pair term decomposes as

\[
\frac1{d^2}=\frac1{r^2}-\frac{2(d-r)}{r^3}
+\frac{V(d/r)}{r^2},\qquad
V(u)=u^{-2}-1+2(u-1)\ge0\quad(u>0).
\tag{5}
\]

Choose the reference independently of unknown collision distances. Sum its linear corrections with localization and exterior terms before bounding them. If the reference evolves, include its derivatives. For complex time use the analytic expression, with a proved continuation bound; real convexity supplies no general phase positivity.

On a regular real-symmetric flat band, with real roots at real time, actual root disks of common fixed projective radius \(\rho\), and a nonvanishing holomorphic source product across \(t+i[-Y,Y]\), the inherited cap reduction and transverse Taylor bound are

\[
I_t=\frac{k_\rho}{\pi}\int_0^Y\Re K_{\mathscr D}(t+i\sigma)\,d\sigma,
\quad
\left|I_t-\frac{k_\rho Y}{\pi}K_{\mathscr D}(t)\right|
\le\frac{k_\rho Y^3}{6\pi}
\sup_{0\le\sigma\le Y}|K_{\mathscr D}''(t+i\sigma)|.
\tag{6}
\]

Here \(k_\rho=\rho^2/(1+\rho^2)\). This is an interface between real interaction estimates and the physical cap; its derivatives, nonvanishing domain and connecting faces still need payment. The principal target is a complete lower bound for (1), not one favorable term of (4) or (6).

## Direct comparison and independent inputs

Give direct estimation the same complete theta source, Gaussian smoothing formula, signed correlations, analytic continuation data, spatial-wall floors and critical-value or discriminant reductions. Compare a completed bound, its information requirements and its cost.

For a proper two-root cluster, let \(P\) be its monic quadratic factor, \(\Delta\) its squared root gap and \(\Delta_0=\Delta(\delta)\). The [existing scalar equation][two-root] is

\[
\Delta'=8+A\Delta,\qquad
A=\frac4{2\pi i}\oint_{\Gamma_R}\frac{H_z}{HP}\,dz.
\]

The wall formula remains regular at an interior collision. With independently verified two-root isolation and \(|A|\le K\), the founding note derives the sufficient radius

\[
|\tau-\delta|<T_K(\Delta_0),\qquad
T_K(\Delta_0)=K^{-1}\log(1+K|\Delta_0|/8),
\tag{7}
\]

with \(T_0=|\Delta_0|/8\). A rectangle needs
\(\sqrt{(\delta+\epsilon)^2+Y^2}<T_K\).
Use this as a survival comparator, not as a substitute for the cap comparison when the objective is only a lower bound for \(I_0\).

Required theta inputs may include complete source tails, correlated jet estimates, wall minima, fixed population counts, analytic-factor derivatives, gap or discriminant enclosures at the anchor, and bounds across imaginary time. State how each is obtained. No negative-time all-real interval, RH, GUE or uniform gap bound is available by default. A conditional theorem may use a stated hypothesis, but its scope must remain explicit.

## Controls and acceptance

Use the [collision-control register][controls] and [premise rule][a02]. The generic identities admit colliding controls. The proposed quantitative inequality must be tested on a domain containing the control's event, not rejected merely because its source differs.

| Control | Canonical-source premise absent |
| --- | --- |
| Euler-factor modifications | Unchanged theta source and arithmetic coefficients |
| Finite weighted-square sources | Full reflection and the complete normalized coefficient sequence |
| Reflected and positive-primitive sources | Unchanged arithmetic square expansion |
| Finite-prime compatible perturbations | Full reflection and simultaneous complete arithmetic beyond the fixed selected constraints |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic |

The quadratic \(H=z^2-2\tau\) tests whether a proposed shrinking width falsely crosses a collision at zero. The sine heat solution tests whether the analytic factor has been lost. A shifted quadratic with a later positive event tests any claim that a negative collar automatically extends to all later times.

The first completed comparison should report the direct lower bound \(L_{\rm direct}\) and deformed lower bound \(L_{\rm deform}\) on the same \(I_0\), or a precise analytical comparison if neither is evaluated numerically. Record total error, source precision, geometry and cost. Continue a specified mechanism for a strict useful gain, a new applicable estimate, or a precise diagnostic. If it only transfers the original unknown sign, record that scoped outcome under [avoid 07][a07]; do not infer a universal obstruction.

## Later applications and records

After a useful finite estimate, assemble height bands while controlling changing populations, joins, slopes and error accumulation. A positive-time event bound can then use

\[
Q_+\le I_T+S_+-L_{\rm deform}.
\]

Exclusion requires a complete upper bound strictly below one. Reality at zero also needs a real-root anchor and population control; zero charge alone permits simple nonreal zeros. All-height conclusions, higher multiplicities and the \(0^+\) limit require their own coverage theorems.

Use the [README][readme] for the background and external reading path. Keep derivations, computations and assessments in their respective folders. Existing brainstorm notes and their self-review retain their source paths and same-assistant status. The [milestone history][history] records concise changes; opening this program creates no manuscript milestone or new mathematical claim.

[progress]: ../research-progress/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md
[readme]: ../README.md
[history]: ../DRAFT_HISTORY.md
[brainstorm]: ../../../brainstorm/investigations-4/notes/02_MOVING_COLLAR_MATERIAL_ENERGY_AND_HEIGHT_DEPENDENT_EPSILON_20261023.md
[two-root]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md

## RH-conditional density-one objective and pair spectrum

23 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**. The author added RH implying almost-all simplicity as a worthwhile intermediate objective and specifically recalled tracking pair-matrix eigenvalues. [Note 05](../notes/05_EARLIER_TIME_PAIR_COUNTS_AND_DENSITY_ONE_SIMPLICITY_20261023.md) supplies a complete earlier-time projected-pair-to-multiplicity bridge. [Note 06](../notes/06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md) uses the existing Vandermonde Hessian and full adjacent-gap dynamics to bound endpoint multiplicity mass by a positive-time large-eigenvalue count, or six times a bounded resolvent trace. These real-time consumers avoid the physical imaginary-time cap requirements; neither has its new theta statistical upper estimate.

The primary new analytical target is an upper bound for the fraction of large pair-matrix eigenvalues at a source-prescribed microscopic heat time as height grows. Full PCC is stronger than needed. Track complete populations, retain the exterior force and specify the unfolding scale. Unrestricted adaptive earlier times and fixed-population limiting identities are classified as reformulations; neither is counted as progress toward a new simplicity proportion. [Note 04](../notes/04_PAIR_STATISTICS_AS_A_ONE_SIDED_CONTOUR_INPUT_20261023.md) separately identifies the one-sided positive real pair lower bound relevant to the original cap objective.
