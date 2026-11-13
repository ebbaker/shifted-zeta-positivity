# Research overview for the height and time dependent boundary bootstrap

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and reasoning effort
are unavailable in the setup chat's recorded configurations.
**Evidence level: inherited-source synthesis and B01 conceptual selection;
the canonical E01 estimate remains unproved.**

## Primary program: analytical control over unbounded height

Seek formulas or analytically justified selection rules for the contour
and observation points across the continuum of heights \(T=|X|/2\),
with no finite upper height cutoff. Seek canonical estimates that can
support repeated contraction toward the real axis. Numerical diagnostics
and finite certificates serve this analytical program.

Contour families and observation protocols remain open to exploration:
graphs, conformal constructions, uniformly controlled local covers and
other justified strategies may be compared. Study each choice separately
and then its coupling. The initial rectangle and gain 1/16 are benchmarks,
not permanent restrictions on the program. [Note05][program] records the
author's 13 November analytical and exploratory scope revision, including
an explicit infinite-height parameterization and its unpaid obligations.

## B01 baseline — 13 November 2026

[Note03](../notes/03_GNP_BB_B01_COLLAR_COMPARISON_20261113.md) fixes
λ_X=1/L_X and 7/8<y<9/8, selects complete-field comparison with
ζ(s_λ(z)) in Re s>1, and preserves heat suppression in the entire
reflected population. Its error threshold 1/16 would give h=1/8,
buffer 1/16 and a width gain 1/16. The same data pay a complete
rectangle Green comparison; that geometry adds no arithmetic gain.
This is a feasible proof contract with conditional consumers, not an
acquired canonical error bound. [E01 r1](../research-progress/handoffs/GNP-BB-E01-r1.md)
remains a fixed analytical benchmark task, recommended GPT-6.1 Sol.
GNP-BB-B02 is now the suggested next conceptual task for the broader
analytical program; the register controls activation. This priority
change does not widen the frozen E01 request.

**Author-requested planning addition, 13 November:** GNP-BB-B02 separates
contour design from observation-point placement, then investigates their
joint use across unbounded height and successive inward steps. The later
analytical-program revision supersedes its initial finite rectangle
comparison limits; the fixed E01 r1 remains available as a baseline.

## Question and intended gain

Can quantitative information on a proved zero-free region produce a
strictly larger zero-free region for the canonical Newman field, with
the contour and observation offset varying with both height and time?
The immediate proof objective is one uniform, explicitly paid inward
step. Its design must already examine whether estimates can persist
through iteration toward the critical line, or identify the precise
barrier and possible changes of strategy. A one-step gain and a
line-reaching iteration are distinct milestones.

The [founding discussion][founding] separates a moving observation from
a moving domain, gives an elementary local extension, and identifies the
extra normal-motion term for a curved time barrier. Its polynomial
diagnostic refutes one naive localization of a global strip theorem.
These are inherited explanatory/analytical facts, not a canonical
arithmetic improvement. [The source crosswalk][crosswalk] preserves their
original homes and evidence levels.

Read the [result index][results] and [avoid index][avoid], particularly
[heat-flow results][r11], [collision controls][r12], [local geometry][r13],
[target classification][a01], [control premises][a02],
[coordinate realizations][a03] and [scoped exclusions][a07].
Obtaining all-real zeros at time zero is a target-equivalent reformulation.
A milestone must instead state a proved quantitative or asymptotic gain,
its domain and its remaining errors.

## Fixed field and coordinates

Retain the complete source and normalization of the
[parent source section][source]:

\[
 p(u)=e^u\sum_{k\ge1}e^{-\pi k^2e^{4u}},\qquad
 \Phi(u)=\frac{p''(u)-p(u)}8,\qquad
 H_\lambda(z)=\frac12\int_{\mathbb R}e^{\lambda u^2}\Phi(u)e^{izu}\,du.
\]

\[
 H_0(z)=\frac18\xi\!\left(\frac{1-iz}{2}\right),\qquad
 \partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]

Increasing \(\lambda\) means increasing Newman time. If a forward-heat
clock is introduced, its opposite sign must be stated explicitly.
Normalization by a nonzero analytic carrier is permitted for estimation;
its derivatives and harmonic boundary terms must be retained.

| Symbol | Meaning |
| --- | --- |
| \(X\), or \(x\) for a varying boundary coordinate | Longitudinal Newman coordinate; zeta height is \(T=\lvert X\rvert/2\) |
| \(y\) | Transverse coordinate of a point or zero |
| \(\lambda\) | Newman heat time |
| \(n\) | Bootstrap iteration; distinct from physical time and the source index \(k\) |
| \(a_n(\lambda,X)\) | Half-width of the region in which zeros are still allowed |
| \(b_n(\lambda,X)\) | Observation offset in \(X+ib_n(\lambda,X)\) |
| \(\eta_n=b_n-a_n>0\) | A chosen observation buffer, when using the upper zero-free exterior |
| \(D\), \(\Gamma=\partial D\) | Analysis domain and its integration contour |
| \(p=X+ib\in D\) | Interior observation point; separate from the contour and the allowed-zero boundary |
| \(B\) | Thickness of a fixed horizontal analysis strip |

At time zero, \(z=X+ib\) corresponds to \(s=(1+b)/2-iX/2\).
The critical line is therefore the real axis of the Newman plane.
At nonzero \(\lambda\), the field is deformed; it is not ordinary zeta
evaluated at a different coordinate.

The proposed enclosure is

\[
 H_\lambda(x+iy)=0\ \Longrightarrow\
 |y|\le a_n(\lambda,x),\qquad
 0\le a_{n+1}(\lambda,x)\le a_n(\lambda,x).
\]

The zero-free exterior expands as the allowed band shrinks. Real zeros
remain permitted. An initial global bound is
\(a_0(\lambda,x)=\sqrt{\max(1-2\lambda,0)}\) for
\(0\le\lambda\le1/2\), using the canonical strip at zero and the
uniform de Bruijn theorem. Its source and scope are recorded below.

## Parameter domains and quantifiers

The program covers arbitrary real heights, with no finite upper cutoff.
A proof may split into a uniform theorem for every \(X\ge X_0\), its
symmetry counterpart and a separately covered compact region. Height
blocks or local rectangles are analytical devices whose estimates must
be uniform over the stated continuum; favorable samples do not suffice.
Specify a common heat time, a declared time interval or a heat curve.
A theorem on a curve is not a theorem on a time slab or at time zero.

Each claimed step must specify whether its enclosure is global in \(x\)
or restricted to \(I\). A bounded contour retains side boundaries; a
global Green integral needs its remote boundary estimates. A time
propagation additionally needs initial containment, side entry and
multiple-contact control. An asymptotic onset may depend on fixed
parameters, but its dependence on iteration number must be stated.

For repeated contraction at each fixed height, every required step must
remain applicable there. An onset \(X_n\) escaping to infinity may prevent
this. Track this issue from the first design pass, alongside boundary
separation and losses as the allowed width approaches zero.

The published evolved-RS domain \(0<\lambda\le1/2,\ 0\le y\le1,\ X\ge200\)
is the domain of Polymath's Theorem 1.3, not an automatic theorem at
offset \(4\) or at time zero. Wider-strip estimates are separate inherited
HDA inputs. See the [source-use index][refs] and [lower-offset discussion][lower].

## Boundary prediction and domain dependence

The integration contour Γ=∂D, interior observation p=X+ib, and
allowed-zero boundary y=a are distinct choices. The kernel couples
the first two; it does not force either to coincide with the zero
boundary. [Note04](../notes/04_GNP_BB_CONTOUR_AND_OBSERVATION_CLARIFICATION_20261113.md)
spells out their positions and the auxiliary disks in the current request.

For \(u_\lambda=\log|H_\lambda|\), a fixed strip \(0<y<B\), and \(0<b<B\),

\[
 \mathcal P_{\lambda,B}^{(b)}(X)=
 \int_{\mathbb R}P_{0,B}^{(b)}(x-X)u_\lambda(x)\,dx+
 \int_{\mathbb R}P_{B,B}^{(b)}(x-X)u_\lambda(x+iB)\,dx,
\]

\[
 P_{0,B}^{(b)}(v)=\frac{\sin(\pi b/B)}
 {2B[\cosh(\pi v/B)-\cos(\pi b/B)]},\qquad
 P_{B,B}^{(b)}(v)=\frac{\sin(\pi b/B)}
 {2B[\cosh(\pi v/B)+\cos(\pi b/B)]}.
\]

Their masses are \(1-b/B\) and \(b/B\). The complete
[Green identity][green] at the original \(B=8,b=4\), and the
[general-offset calculation][lower], give the defect

\[
 J_{\lambda,B}^{(b)}(X)=
 \mathcal P_{\lambda,B}^{(b)}(X)-u_\lambda(X+ib)
 =\sum_{\zeta_j\ {\rm in\ strip}}m_jG_B(X+ib,\zeta_j)\ge0.
\]

Putting \(b=b_n(\lambda,X)\) into this formula changes the observation
while retaining the fixed strip. If the boundary follows a graph, use
its actual harmonic measure. For a bounded regular domain \(D\) without
boundary zeros, and a nonzero observation \(p\in D\),

\[
 J_{\lambda,D}(p)=
 \int_{\partial D}u_\lambda(\zeta)\,d\omega_D^p(\zeta)-u_\lambda(p)
 =\sum_{\zeta_j\in D}m_jG_D(p,\zeta_j).
\]

This identity is a representation. In an already zero-free domain it
equals zero; extension across its boundary requires further quantitative
information. A boundary zero has zero Green weight, so a target being
excluded must be kept inside the domain with the appropriate buffer.

## An infinite-height contour and observation parameterization

For a proved positive enclosure \(a_n(\lambda,x)\), one exploratory
family, at fixed \(\lambda\), is
\[
 \begin{aligned}
 \Gamma_n^\lambda
 &=\{x+i(1-\theta_n-r_n^-)a_n:x\in\mathbb R\}
   \ \cup\ \{x+i(1+r_n^+)a_n:x\in\mathbb R\},\\
 p_n^\lambda(X)&=X+i(1+\epsilon_n(\lambda,X))a_n(\lambda,X).
 \end{aligned}
\]
All contour coefficients are evaluated at \((\lambda,x)\), with
\(0<\theta_n<1\), \(0<r_n^-<1-\theta_n\) and
\(0<\epsilon_n<r_n^+\). The region between the graphs contains the
observation and target \((1-\theta_n)a_n\le y\le a_n\) strictly inside.
Conjugation supplies the lower-half-plane counterpart. Coefficients can
vary analytically with height; [Note05][program] gives an illustrative
logarithmic profile and allows other explicit or implicit selection rules.
These expressions describe geometry, not a proved contraction.

An integral over this unbounded contour needs a proved exhaustion limit
and all end and growth contributions. A uniformly controlled family of
local contours covering every height is another admissible strategy.
Use one fixed heat time within each contour calculation; a schedule
\(\lambda(X)\) selects a family of such calculations, not a spatially
varying heat parameter inside one analytic field.

## Separate contour and observation investigation

**GNP-BB-B02 — B, recommended GPT-6 Astra.** Explore which contour and
observation protocols can support analytical estimates over unbounded
height and potentially remain effective toward the line. Read Notes03–05;
the [sole register][progress] records the separate workstreams. The
earlier cap on alternative rectangles and offsets is superseded.

| Workstream | Explore | Comparison requirement |
| --- | --- | --- |
| Contour | Height-dependent graphs, conformal constructions, local covers or another justified family | Hold the observation rule, field, clock and target fixed within each comparison; account for harmonic measure, derivative domains, every boundary and infinite-height contribution |
| Observation point | Explicit height laws, analytical error balancing, or selection from previously proved bounds | Hold the contour family and target fixed; control buffers, floors, weights and coverage at every height, including any multiple-observation rule |
| Joint strategy and iteration | Compatible combinations and changes of strategy as the band narrows | Recompute the full budget, derive a supported gain and examine its recurrence, onset growth and limiting domain |

Seek formulas or well-posed analytical protocols, rather than a list of
chosen numerical positions. Compare field gain \(h-\eta\), with
\(h=m/(2M)\) and full segment coverage, or the complete Green margin
\(g_K-(\widehat J+E)\) for the same target. Include independent carrier
nonvanishing and every canonical representation, logarithmic, boundary
and remainder cost. A geometric improvement alone is not a proved gain.

For a possible iteration \(a_{n+1}\le(1-\theta_n)a_n\), investigate
whether the proved steps stay valid and force the product of contraction
factors to zero at each fixed height. Divergence of \(\sum_n\theta_n\)
is one sufficient test, not an assumed premise. The current coarse
absolute allowance stops at \(y>3/4\); overcoming that specific
estimating barrier is part of strategy exploration.

**Decision boundary.** One analytical design pass ends with a supported
route and a fixed next proof contract, or a precise bottleneck plus
well-scoped alternatives. There is no preset quota of contour shapes or
observation protocols. Stop at that decision boundary and separate later
execution; do not turn exploration into an unlimited numerical search.
Apply the control screen to changed premises. E01 r1 and its inputs stay
frozen; a different execution contract must be explicitly revisioned.

## Inherited analytical consumers

These are the two consumers compared in B01. They are available starting
points for B02, whose strategy exploration is not restricted to them.

**Normalized-field extension.** For \(F_\lambda=H_\lambda/C_\lambda\)
with nonvanishing analytic \(C_\lambda\), prove
\(|F_\lambda(x+ib_n)|\ge m>0\) and \(|F_\lambda'|\le M\), \(M>0\),
on a full inward segment of length \(h\). Then

\[
 |F_\lambda(x+i(b_n-s))|\ge m-Ms\quad(0\le s\le h).
\]

The choice \(h=m/(2M)\) retains a floor \(m/2\), if that entire segment
is covered by the derivative estimate. To improve the known enclosure,
require \(h>\eta_n\) and \(b_n-h\ge0\); the gained width is \(h-\eta_n\).
With approximation \(A\) and rigorous value/derivative errors,

\[
 m=|A(x+ib_n)|-E_0>0,\qquad
 M=\sup_{\rm segment}|A'|+E_1.
\]

This generic elementary lemma is inherited from [Note13 §4][founding].
The new work would be canonical, uniform estimates that pay its strict
buffer inequality. Nonvanishing alone supplies no rate.

**Complete Green comparison.** For a compact target \(K\subset D\),
away from \(p\) and the boundary, define
\(g_K=\inf_{\zeta\in K}G_D(p,\zeta)>0\). A proved upper allowance
\(\widehat J+E<g_K\) excludes a zero in \(K\).
Here \(E\) pays all field/logarithmic, boundary, side, tail, quadrature
and domain-approximation errors that occur. Curving the contour may alter
both the signal and the costs. Compare the complete allowance on a common
domain; a larger Green kernel by itself is not an arithmetic gain.

A complete-boundary Rouché comparison requires a proved zero count for
the approximant and a strict full-boundary modulus margin. B01 treated
it as a same-data check on its chosen domain. B02 may explore its use
or another analytical strategy with its complete hypotheses and costs.

For either route, retain both RS arms, integer cutoff, correction and
remainder. At lower offsets, absolute convergence of an infinite ordinary
Dirichlet series cannot replace the complete finite representation.
Regularization or deflation must pay the exact changes to the observable,
including center-log corrections or complete zero-count/factor errors.
[Note12][lower] supplies these inherited cautions.

## Time evolution and the baseline to improve

For a global constant width \(A\) at time \(\lambda_0\), de Bruijn's
theorem gives width at most
\(\sqrt{\max(A^2-2\Delta\lambda,0)}\) at
\(\lambda_0+\Delta\lambda\), \(\Delta\lambda>0\).
In this normalization it implies
\(\Lambda\le\lambda_0+A^2/2\).
See [Polymath v2, Theorem 3.2][polymath], as checked in the
[inherited branch-use record][rsrefs].

Before the zero-width endpoint, pure classical contraction preserves
\(Q=\lambda+A^2/2\). A proved additional squared-width reduction
\(\delta>0\) would lower that upper bound by \(\delta/2\), while the
nonnegative-width condition remains valid. A local height gain need not
lower the global supremum \(A\). Time-zero conclusions do not follow by
running a positive-time contraction backward.

For a simple zero \(z_j=x_j+iy_j\), the heat equation gives

\[
 z_j'=\frac{H_{zz}}{H_z}(z_j),\qquad
 \frac d{d\lambda}\{y_j-a(\lambda,x_j)\}
 =y_j'-a_\lambda-a_xx_j'.
\]

A curved time barrier must account for the horizontal term and multiple
zeros. Polymath's Proposition 3.1 and Theorem 1.2/Proposition 3.3 provide
specific root dynamics and barrier precedents; they are not a theorem
for every graph \(a(\lambda,x)\). [Note13 §§5–7][founding] and its
[exact polynomial record][polynomial] screen the naive pointwise
substitution of \(a_0(x)\) into the global contraction law.

## Inherited evidence and limits

| Input | Recorded evidence and permitted use |
| --- | --- |
| Complete source, heat equation and original Green identity | Parent analytical proofs with inherited/internal assessment scope; fixed normalization and complete growth/boundary payments |
| Lower-offset kernels, local extension and variable-boundary discussion | Same-assistant explanatory/analytical deductions in sibling brainstorm Notes12–13; no canonical inward improvement |
| Polynomial diagnostic | Exact rational algebra, same-assistant checks; refutes only pointwise localization of the global strip law |
| B10 short-window estimate | Audited and integrated inherited-input theorem at \(c=1\), \(b=4\), thickness eight; [audit][audit], [assessment][assessment], [live section][b10] |
| Published strip contraction and barrier method | Version-pinned selected passages inherited through the source-use records; no fresh full-paper review in this setup |

B10 applies on \(\lambda(X)=1/L_X\), \(L_X=\log(X/(4\pi))\), with
block-constant \(P_U=\lfloor L_U^2\rfloor\) and
\(U^{17/81+\rho}\le\ell\le U\), fixed \(0<\rho\le47/162\).
Its residual-mean error is \(O_\rho(L_U^{-3/2})\), Green mean is
\(O_\rho(L_U^{-1/3})\), and fixed-positive-threshold exceptional proportion
is \(O_{h,\rho}(L_U^{-1})\). The onset is unevaluated.
These averaged statements do not supply a boundary floor, cover every
center, or transfer automatically to changed offsets, domains or clocks.

## Controls and unresolved decisions

Use [cluster12][r12] and the inherited
[Note13 §8 premise screen][founding]. Euler-factor controls fail exact
theta arithmetic/completion; weighted-square controls fail unit theta
coefficients and full reflection; reflected super-Gaussian controls lack
the full integer-square source; smooth positive-primitive controls lack
the complete theta arithmetic source. Finite-prime controls fail full
reflection and complete arithmetic agreement. The polynomial diagnostic
has no theta source. Generic Green or local-extension identities may hold
for these fields and do not themselves distinguish theta.

B01 selected the canonical input for the baseline; E01 must still prove
its estimate. B02 explores analytical contour and observation rules over
unbounded height. Its design must address whether gains can accumulate,
whether height onsets remain usable through iteration, how compact
heights and boundary contacts are covered, and which time domain the
result actually reaches. Merely taking
\(a_n\to0\) as a desired conclusion is not a mechanism. A limit
\(a(X)\to0\) only at infinite height does not exclude finite-height
nonreal zeros.

Numerical work may support constants, diagnostics and compact-region
certificates attached to an analytical tail theorem. It cannot replace
an all-height estimate or establish an iteration limit from samples.

The [plan][plan] preserves B01's completed scope and defines the revised
B02 analytical exploration above. The [GNP-BB register][progress] is the sole task-status
owner; [continuation][continuation] is a dated handoff snapshot.

[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[r13]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[source]: ../../manuscript/sections/02_source.tex
[green]: ../../manuscript/sections/05_green.tex
[lower]: ../../01_riemann_siegel_evolution/brainstorm/notes/12_GNP_RS_LOWER_TRANSVERSE_OFFSET_AND_LOG_OBSERVATION_20261113.md
[founding]: ../../01_riemann_siegel_evolution/brainstorm/notes/13_GNP_RS_HEIGHT_AND_TIME_DEPENDENT_STRIP_BOOTSTRAP_20261113.md
[polynomial]: ../../01_riemann_siegel_evolution/numerics/21_GNP_RS_VARIABLE_STRIP_DIAGNOSTIC_20261113.json
[audit]: ../../01_riemann_siegel_evolution/notes/31_GNP_RS_B10_PREINTEGRATION_PROOF_AUDIT_20261112.md
[assessment]: ../../01_riemann_siegel_evolution/reviews/16_GNP_RS_B10_PREINTEGRATION_ASSESSMENT_20261112.md
[b10]: ../../manuscript/sections/10d_short_window_means.tex
[rsrefs]: ../../01_riemann_siegel_evolution/references/README.md
[polymath]: https://arxiv.org/html/1904.12438v2#S3
[refs]: ../references/README.md
[crosswalk]: ../notes/02_GNP_BB_SETUP_AND_SOURCE_CROSSWALK_20261113.md
[plan]: ../research-plan/01_GNP_BB_RESEARCH_PLAN_20261113.md
[progress]: ../research-progress/01_GNP_BB_RESEARCH_PROGRESS_20261113.md
[continuation]: ../notes/01_GNP_BB_CONTINUATION_AND_PROMPT_20261113.md
[program]: ../notes/05_GNP_BB_ANALYTICAL_PROGRAM_AND_SELECTION_PROTOCOLS_20261113.md
