# How the moving spatial boundary is incorporated

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**. Clarification of existing results, not a new theorem. Conversation: **Review conserved-contour results**, brainstorm history **0009**.

The current book does prove an actual boundary varying with time and position. The phrase “fixed-offset material graphs” describes its initial positive offset and the fixed strip in which it is controlled. It does not mean the graph remains fixed. This clarifies the [results review](../reviews/12_RESULTS_ACCOMPLISHMENTS_AND_OBSTACLES_20261024.md).

Write the spatial coordinate as $z=x+iy$. In forward heat time the upper boundary is

\[
\Gamma_t^+=\{x+i b(t,x)\},\qquad b(0,x)=b_0>0.
\]

The adopted velocity is supplied by the actual theta heat field:

\[
U(t,z)=\frac{H_z(t,z)}{H(t,z)},\qquad
\frac{dZ}{dt}=U(t,Z).
\]

It depends on both time and complex position. A material point may move horizontally as well as vertically. In graph coordinates its motion is

\[
\partial_t b+\Re U(t,x+i b(t,x))\,\partial_x b
=\Im U(t,x+i b(t,x)).
\]

Thus the boundary generally bends as it moves. The horizontal transport term is essential; setting $b_t=\Im U$ alone would lose it. This graph is a real curve in the complex spatial plane; $b$ is a real function of time and horizontal position, not a holomorphic function of the full variable $z$.

[Book Theorem 3.1](../../manuscript/book.tex) uses backward duration $s=-t\ge0$ and labels initial points by $a$:

\[
\partial_s Z(s,a)=-\frac{H_z(-s,Z(s,a))}{H(-s,Z(s,a))},
\qquad Z(0,a)=a+i b_0.
\]

The labels $a$ are initial positions; $\Re Z(s,a)$ is the current horizontal position. The theorem proves that the latter remains strictly increasing in $a$, so the material curve can be rewritten as a single-valued graph. It supplies existence and uniqueness throughout $0\le s\le c/(\log Y)^2$, finite spatial containment, height-band coverage, tangent control, and $O(1/\log Y)$ displacement and slope. The upper graph moves upward as backward duration increases, including at fixed current horizontal position. Reflection supplies the lower graph, which moves downward. Material endpoints may drift; fixed initial end extensions retain coverage.

The construction is an ODE characterization with a proved approximation, rather than an elementary closed expression:

\[
Z(s,a)=a+i b_0-s\frac{F'(a+i b_0)}{F(a+i b_0)}
+O((\log Y)^{-2}),\qquad F=H(0,\cdot).
\]

The actual law preserves the full material one-form and primitive image:

\[
H(-s,Z(s,a))\,\partial_a Z(s,a)=F(a+i b_0),
\qquad P(-s,Z(s,a))=P(0,a+i b_0).
\]

Here $P(t,z)=\int_0^zH(t,w)\,dw$. Nonvanishing, needed for the velocity quotient, is obtained first from book Theorem 1.1. It is not assumed along an unknown moving tube.

The boundary is then used explicitly in book Corollary 5.4. In the forward-time notation above, its smooth counting window is

\[
\psi_Y(t,x+iy)=\eta(x)\,
\chi\!\left(\frac{y}{b(t,x)}\right).
\]

The horizontal cutoff $\eta$ covers the target height band; the even vertical cutoff $\chi$ follows the moving upper and lower graphs. The general balance retains the complete moving-window derivative $\psi_t+\nabla\psi\cdot v$, where the zero velocity is $v=H_{zz}/H_z$ at simple zeros. The book places the moving vertical transitions inside the proved zero-free corridor, so every term containing $\chi'$ vanishes at roots. Only the terms from the fixed horizontal cutoff remain. The window used for counting is therefore not a fully material closed contour: its upper and lower transitions follow the graph, while its horizontal localization retains the end currents.

The remaining resource is the earlier nonreal population plus one-sided inward end flux. The material velocity $H_z/H$ differs from zero velocity $H_{zz}/H_z$; preserving $H\,dz$ does not force zeros to move with this boundary. A fixed wall inside the same proved corridor would also remove the vertical transition flux. That observation limits the additional multiplicity gain currently extracted from motion; it does not withdraw or replace the moving-boundary theorem.

The proved construction assumes RH with multiplicities allowed, starts a fixed positive distance from the axis, and uses real time on the stated short interval. It does not yet provide a general near-axis adaptive contour or a bound making the complete collision resource small. Main Note 19 develops a near-axis comparison but supplies no new nonvanishing graph there. The alternative regularized-current-driven boundaries in [conserved_contours.tex](../../manuscript/conserved_contours.tex) remain exploratory mechanisms; the book has adopted the $H\,dz$-preserving flow.

This clarification follows the [result index](../../../../../result-summaries/README.md), [local heat-geometry summary](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../../avoid/README.md), and [shared-premise warning](../../../../../avoid/02_shape_only_arguments_and_the_controls.md). A moving regular contour is an established intermediate result; its existence is still compatible with the book's all-multiple control. No manuscript, prior review receipt, or mathematical status was changed.

## Geometry and the role of the counting function

Clarification added 24 October 2026 for Edward Baker, with substantial LLM assistance, **gpt-6-astra (Codex), effort max**. This explains the existing construction and does not add a research criterion.

The boundary is a boundary of the region being observed in the complex spatial plane. The field $H(t,z)$ remains entire in $z$; the construction does not solve the heat equation on a restricted domain with new boundary conditions. At each fixed real heat time $t$, one selects curves in that plane. Their union over time is a surface in the three real coordinates $(t,x,y)$, where $z=x+iy$. In that sense the boundary depends on both time and spatial position.

The coordinate conversion matters. In the book's normalization,

\[
H(0,z)=\frac18\xi(w),\qquad
w=\frac12+\frac{iz}{2}
=\frac{1-y}{2}+i\frac{x}{2}.
\]

Thus $x$ is twice the usual zeta ordinate, $y$ measures displacement from the critical line, and $t$ is a separate heat parameter. The real $z$ axis corresponds to the critical line at $t=0$. The critical line is therefore horizontal in this spatial drawing. A wall at $y=b_0>0$ is a positive distance from that axis. Under the coordinate conversion at $t=0$, it lies on the zeta-plane line $\Re w=(1-b_0)/2$. The conjugate lower wall lies on the other side of the critical line.

The upper graph can equivalently be described by a level-set equation

\[
B(t,z)=\Im z-b(t,\Re z)=0.
\]

Here $B$ is real valued and is not required to be holomorphic. A fixed-time cross-section is a curve; the time-dependent collection is the side of a spatial tube. This is distinct from prescribing $t=h(x)$, which samples different heat times at different heights. The current book's spatial construction uses the same time for all points of each slice. The height-graph alternative has the nonholomorphic correction recorded in [contours.tex, common time and height graphs](../../manuscript/contours.tex): $\partial_{\bar z}H(h(x),z)=-h'(x)H_{zz}(h(x),z)/2$.

The function $\psi(t,z)$ gives each spatial point a counting weight. It is real valued, between zero and one, with sufficient smoothness to differentiate along a moving zero. The concrete choice already displayed above has two factors: $\eta(x)$ selects the height band, and $\chi(y/b(t,x))$ selects a strip following the upper and lower walls. Away from the horizontal ends it has the following interpretation:

- In the core $|y|\le(1-\delta)b(t,x)$, the weight is one.
- In the buffer $(1-\delta)b(t,x)<|y|<(1+\delta)b(t,x)$, it changes smoothly between one and zero.
- Beyond that buffer, it is zero.

The geometric wall $|y|=b(t,x)$ lies within this buffer. It is not the exact support edge, and it need not be identified with a prescribed level such as $\psi=1/2$. The horizontal cutoff supplies corresponding fades at the height ends. Smooth weighting permits ordinary differentiation instead of a discontinuous jump each time a zero crosses a sharp indicator. It changes the counting observable, not the zeros or the heat field.

In particular, $\psi$ does not vanish on the real axis in the target band: it equals one there. The word “nonreal” is imposed separately in

\[
N_{\psi,\mathrm{nr}}(t)
=\sum_{\substack{H(t,z)=0\\\Im z\ne0}}m_z\psi(t,z).
\]

An interior nonreal zero of multiplicity $m_z$ contributes $m_z$; a zero in a fade contributes a fractional weight; an exterior zero contributes zero. When nonreal zeros reach the real axis, their removal from this nonreal sum is recorded by the separate collision term. It is not a disappearance caused by the cutoff.

The material boundary law preserves the complex one-form $H\,dz$ on material subarcs, equivalently the primitive value at each transported point. This gives a natural evolution coupled to the actual field. The conserved quantity is not itself a zero count or a positive population. A simple zero instead has velocity $v=H_{zz}/H_z$, obtained by differentiating $H(t,z(t))=0$. This explains why the two velocities need different formulas.

The ordinary chain rule makes the role of the window explicit:

\[
\frac{d}{dt}\psi(t,z(t))=\psi_t+\nabla\psi\cdot v.
\]

The first term measures the change of the window at a fixed spatial point; the second measures a zero's motion through it. If a whole window is transported by a vector field $u$, so that $\psi_t+u\cdot\nabla\psi=0$, the sum becomes $\nabla\psi\cdot(v-u)$. That conditional identity explains relative crossing. The book's explicit product cutoff need not satisfy a transport equation throughout its buffers: its horizontal cutoff stays fixed, and the general chain rule is the formula actually needed.

The proved zero-free corridors make the upper and lower transitions useful. There are no roots in the places where the vertical cutoff changes, so its derivatives contribute nothing when evaluated at roots. Only the height-end contributions remain. A fixed wall inside the same proved corridor would achieve that particular removal as well. The moving wall additionally supplies the proved field-preserving geometry; neither construction estimates how many nonreal zeros were inside at the earlier time.

The elementary heat solution

\[
Q(t,z)=(z-a)^2-2t
\]

makes this limitation visible. At $t<0$ its two zeros are $a\pm i\sqrt{-2t}$; at $t=0$ they form a double zero at $a$. On a finite short interval choose a smooth window equal to one on both tracks, with its spatial transitions outside them. Then the earlier nonreal count is two, the inward and outward window fluxes are zero, the final nonreal count is zero, and the real collision contributes two. The exact balance reads $0+2=2+0-0$. This is a local heat example, not the canonical theta field: it illustrates what the accounting permits, without challenging the book's theta-specific contour theorem. The existing all-multiple control in the book establishes the stronger limitation on the stated coarse contour estimates.

Consequently, the current construction produces a controlled place to count and an exact account of motion and real collisions. To turn it into a simplicity result still requires a quantitative bound on the earlier nonreal population plus one-sided inward height-end flux. The distinction between a spatial side and a height-dependent time graph, and between field conservation and zero transport, is essential to interpreting that remaining task.

## What the accounting says about RH and multiplicity

24 October 2026. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), effort max**. Interpretation of the existing book balance and its sharp endpoint bounds; no new criterion or theorem.

A conserved contour count at one time, with zeros counted with multiplicity, cannot distinguish two simple zeros from one double zero. The heat balance adds information by tracking how nonreal branches meet the real axis. At a real zero of multiplicity \(m\), the local heat expansion forces exactly \(2\lfloor m/2\rfloor\) nonreal branches immediately before the event. A simple real zero has a locally real backward continuation; a double has two nonreal backward branches; a triple has two nonreal branches and one real branch. Thus the real/nonreal accounting contains a quantitative multiplicity charge. It is not a complete reconstruction of multiplicities: the charges for a double and a triple are both two.

For a target real endpoint site where the window equals one, the collision charge is fully counted, including an event at the right time endpoint. The book defines
\[
D=\sum_{\text{multiple target sites}}(m-1),\qquad
M=\sum_{\text{multiple target sites}}m,
\]
and proves
\[
D\le R,\qquad M\le\frac32R,\qquad
R=N_{\psi,\mathrm{nr}}(-S)+\mathcal F_{\psi,\mathrm{nr}}^+.
\]
An \(R<2\) estimate excludes any multiple real target endpoint. These are the existing bounds in [book.tex, sharp endpoint bounds](../../manuscript/book.tex), not deductions from conservation of \(H\,dz\) alone. In the acquired window the inward flux reduces to the height-end term, but the earlier nonreal population remains.

The exact balance separates two different questions:
\[
N_{\psi,\mathrm{nr}}(0)+B_\psi
=N_{\psi,\mathrm{nr}}(-S)
+\mathcal F_{\psi,\mathrm{nr}}^+
-\mathcal F_{\psi,\mathrm{nr}}^-.
\]
RH asks for the absence of nonreal endpoint zeros, with complete height coverage. RH allows real multiple zeros. Conditional simplicity assumes endpoint reality and seeks to exclude multiple events precisely at \(t=0\). The collision sum \(B_\psi\) includes that endpoint, as well as earlier real collision events. Nonreal branches may have collided at a negative time and already split into simple real zeros by zero time; consequently a positive resource does not establish an endpoint multiple zero. The bound is a sufficient upper-budget route, not an equivalence.

The generic finite balance does not require RH. The current fixed-offset theta nonvanishing and material-wall theorem does assume RH, so that theorem cannot be used as an independent premise to prove RH. An RH application would require independently justified geometry and a bound forcing the terminal nonreal population to vanish. Under RH, the current simplicity application instead needs a useful estimate on the complete earlier-population-plus-inward-flux resource. Neither follows merely from conservation or regularity of the outer wall.

The author's observation therefore identifies the weakness of the currently controlled quantities, but multiplicity is present in the accounting itself. The outstanding task remains to prove a sufficiently strong actual-theta estimate for the quantity feeding that accounting. The current [arithmetic progress register](../../research-progress/04_ARITHMETIC_INSIDE_CONSERVED_CONTOURS_PROGRESS_20261023.md) retains this as open.

