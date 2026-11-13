# Analytical program over unbounded height and open selection protocols

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model and reasoning effort
are unavailable in this chat's recorded configurations.
**Status: author-requested program revision and illustrative geometry;
no new canonical estimate or contraction theorem.**

## Purpose and classification

The primary program is analytical: seek an explicit contour family and
observation rule covering the continuum of zeta heights \(T=|X|/2\),
without a finite upper height cutoff, and estimates that could support
repeated contraction toward the line. Numerical work may diagnose a
specific estimate, check constants, or certify a bounded remaining
region; it must support this analytical program.

Read the [result index][results] and [avoid index][avoid], especially
[heat-flow results][r11], [collision controls][r12],
[target classification][a01], [control premises][a02] and
[scoped exclusions][a07]. The formulas below specify candidate geometry
and sufficient iteration tests. They do not acquire their canonical
premises. A milestone requires a proved estimate with its actual gain
and domain, not just another formulation of the desired conclusion.

This revises the planned GNP-BB-B02 scope. It supersedes the earlier
restriction to two alternative rectangles, two offsets and one joint
pair. Different strategies and selection protocols remain available.
The [sole register][progress] owns task states; the [plan][plan] sets
the next decision boundary. B01 and frozen E01 r1 retain their scope.

## An explicit contour family extending to infinite height

At a fixed heat time \(\lambda\), suppose a positive enclosure
\(a_n(\lambda,x)\) is already proved on the claimed height domain.
For a full-line starting bound one may use
\(a_0(\lambda,x)=\sqrt{1-2\lambda}\), \(0\le\lambda<1/2\),
with the inherited theorem and normalization in the overview.
Choose real functions \(\theta_n,r_n^-,r_n^+,\epsilon_n\) satisfying
\[
 0<\theta_n<1,\qquad 0<r_n^-<1-\theta_n,\qquad
 0<\epsilon_n<r_n^+.
\]
All quantities may depend on \((\lambda,x)\). One upper-collar family is
\[
 \begin{aligned}
 \gamma_n^-(\lambda,x)
   &=x+i(1-\theta_n(\lambda,x)-r_n^-(\lambda,x))a_n(\lambda,x),\\
 \gamma_n^+(\lambda,x)
   &=x+i(1+r_n^+(\lambda,x))a_n(\lambda,x),\qquad x\in\mathbb R,\\
 \Gamma_n^\lambda&=\gamma_n^-(\lambda,\mathbb R)
                       \cup\gamma_n^+(\lambda,\mathbb R),\\
 p_n^\lambda(X)&=X+i(1+\epsilon_n(\lambda,X))a_n(\lambda,X).
 \end{aligned}                                                     \tag{1}
\]
Let \(D_n^\lambda\) be the open region between the two graphs. The
proposed target at each height is
\[
 K_{n,X}^\lambda=
 \{X+iy:(1-\theta_n(\lambda,X))a_n(\lambda,X)\le y\le a_n(\lambda,X)\}.
                                                                    \tag{2}
\]
Thus the contour, observation and target are distinct, and each finite
target lies strictly inside the collar. The point lies above the old
enclosure. Lower-half-plane coverage uses conjugation; even choices in
\(x\) also respect the canonical height symmetry. Required regularity,
distance bounds and source estimates must be proved for a chosen rule.

Equation (1) is an explicit parameterization over all real \(x\), not a
successful choice of its coefficient functions. B02 must supply usable
formulas or an analytical selection rule for them from previously proved
information. Defining them through the unknown zeros or an assumed
zero-free continuation would be circular.

For example, a smooth height profile available for exploration is
\[
 q_\beta(x)=\bigl[1+\log(1+(x/x_*)^2)\bigr]^{-\beta},
 \qquad x_*>0,\quad\beta\ge0.                                      \tag{3}
\]
It is defined at every finite height and has no upper cutoff. Choices
such as \(\theta_n=d_nq_\beta\), \(\epsilon_n=e_nq_\beta\),
\(r_n^\pm=c_n^\pm q_\beta\), with
\(d_n,c_n^\pm,e_n>0\), \(d_n+c_n^-<1\), \(e_n<c_n^+\),
satisfy the displayed geometry conditions. Their coefficients may
depend on \(n,\lambda\). This is only an illustrative family: constant,
other height laws, implicit selection rules and different contour
representations remain open. No arithmetic advantage is asserted for (3).

For a contour integral, first close the two graphs at \(x=\pm R\).
An infinite-domain identity needs a proved exhaustion limit, including
the vertical end contributions, logarithmic growth and any normalization
terms. Vanishing end terms must be established, not assumed. A local
cover with uniform analytical estimates and proved overlap coverage is
an alternative way to reach every height.

Every such integral uses **one fixed \(\lambda\)**. If an observation
schedule uses \(\lambda=\lambda(X)\), freeze that value throughout its
entire contour calculation. Integrating \(H_{\lambda(x)}\) along a
single spatial contour does not preserve the analytic Green identity.
A theorem along a heat curve is not a theorem at one common time.

## Explore the contour and observation separately, then together

Keep a common field, time domain and proposed target when comparing
choices. Vary the contour while fixing the observation rule; then vary
the observation rule on the chosen fixed domain. Finally assess their
coupling with a fresh complete budget.

Possible strategies include graph collars, conformal images of a strip,
families of overlapping local domains, and level contours of an
independently controlled analytic comparison function. Possible selection
protocols include a prescribed height law, analytical balancing of
competing errors, and selection from rigorous bounds already available
at that stage. Implicit or adaptive rules must have proved existence,
coverage and regularity wherever they are used. A rule choosing several
observations at one height must also prove that they cover the target.

This list is exploratory. A different shape, carrier, kernel or protocol
can be considered within the same canonical problem when its exact
changes and costs are recorded. Favorable sampled positions do not
define a rule valid for every real height. A changed physical source,
evidence standard or scientific target needs a dated scope revision.

## What an analytical gain must pay

For field extension, put \(\eta_n=\epsilon_na_n\). The inherited consumer
requires a value floor \(m_n\), derivative bound \(M_n\), and full
segment coverage. A proposed gain \(\delta_n=\theta_na_n\) needs
\[
 h_n=\frac{m_n}{2M_n}\ \ge\ \eta_n+\delta_n,\qquad
 b_n-h_n\ge0.                                                     \tag{4}
\]
For the Green consumer, use the observation and local target at the
same height, and acquire
\[
 \widehat J_n(X)+E_n(X)
 <g_n(X):=\inf_{\zeta\in K_{n,X}^\lambda}
                  G_{D_n^\lambda}(p_n^\lambda(X),\zeta).             \tag{5}
\]
The infinite-domain version of (5) requires the exhaustion just described.
Do not replace these local targets by the entire unbounded target set
with one fixed observation and assume a positive uniform Green floor.

The substantive work is the complete canonical estimate in (4) or (5):
both finite RS arms, correction and remainder where that representation
is used; carrier nonvanishing; floors for logarithms; all side and remote
terms; and losses as the collar approaches the real axis. Another
representation may be explored if its complete replacement costs are
supplied. B01's \(1/16\) gain is a first-step benchmark, not a prescribed
gain at every depth. Its coarse absolute payment requires \(y>3/4\);
[Note03 §5][baseline] gives that scoped limitation. A line-reaching route
must identify what sharper information or changed strategy overcomes it.

## Infinite height and repeated contraction are separate requirements

An asymptotic lemma must cover **every** \(X\ge X_0\), with explicit
parameter dependencies, and name the remaining compact-height obligation.
The full program also covers that compact region. Defining (1) for all
\(x\) does not itself prove estimates there.

If a proved step yields
\(a_{n+1}(\lambda,X)\le(1-\theta_n(\lambda,X))a_n(\lambda,X)\),
then a sufficient iteration test at each fixed height is
\(\sum_n\theta_n(\lambda,X)=\infty\), with \(0<\theta_n<1\) and every
step valid there. Indeed,
\(\prod_{j<n}(1-\theta_j)\le\exp(-\sum_{j<n}\theta_j)\to0\).
This elementary test is a design requirement, not an acquired
contraction estimate. Uniform convergence across heights is stronger
and requires corresponding uniform bounds.

If the available onset \(X_n\) escapes to infinity, the estimates may
stop applying at any fixed height; that does not prove contraction to
the line there. Track onset growth, shrinking collars, observation
floors and all accumulated losses. The limit \(X\to\infty\) does not
replace the limit in iteration at each fixed height. Similarly, a
positive-time result or the curve \(\lambda(X)=1/L_X\) does not supply
the time-zero conclusion; any time-zero passage needs its own estimates.

## Control screen and numerical support

The parameterization and generic consumers do not distinguish theta
from the collision controls. The canonical-source distinctions in
[Note03 §5][baseline] remain the inherited premise screen: Euler-factor
controls fail unchanged theta arithmetic; weighted-square and finite-tail
controls fail full unit coefficients/reflection; reflected and smooth
primitive controls fail complete theta arithmetic; finite-prime controls
fail full reflection/agreement; atomic/finite-profile controls fail the
full canonical source/profile; normalized endpoint controls fail ordinary
Dirichlet arithmetic; variable-readout controls fail the actual cosine
field. Reflection rigidity requires its full conjunction of assumptions.
New selection or estimating rules must repeat the relevant
[cluster12][r12] screen and name their actual discriminating premise.
No control is excluded merely by drawing (1).

Numerics are subordinate: a diagnostic must identify the analytical
question it can resolve, and any finite certificate must name the
analytical theorem covering the unbounded tail. Sampled contraction,
fitted height laws and finite zero checks do not prove (4), (5), an
infinite-height tail or an iteration limit. No numerical campaign is
activated by this planning revision.

[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[baseline]: 03_GNP_BB_B01_COLLAR_COMPARISON_20261113.md
[progress]: ../research-progress/01_GNP_BB_RESEARCH_PROGRESS_20261113.md
[plan]: ../research-plan/01_GNP_BB_RESEARCH_PLAN_20261113.md
