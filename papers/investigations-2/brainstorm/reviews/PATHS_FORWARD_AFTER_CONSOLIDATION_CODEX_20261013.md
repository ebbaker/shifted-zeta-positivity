# Paths forward after consolidation

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6-astra` (Codex), reasoning effort **ultra**.

This is a brainstorming assessment following the
[consolidation](../../PORTFOLIO_CONSOLIDATION_20261013.md), not a change to
current program status or a claim of a new RH mechanism. Completed results
and reopening conditions remain in the investigation guides. The concrete
proposals below distinguish analytic observations from unexecuted tests.

## Judgment and allocation

The useful next question is whether an estimate can exploit the exact
cancellations which the completed investigations show are indispensable.
There are two distinct RH-facing bets: complete signed remainder estimates
using 01/18, and a quantitative use of full imaginary Jacobi gluing in 02.
Neither is currently a proved mechanism. The latest automorphic formula
does not by itself make 18 the strongest one.

| Objective | Candidate | First deliverable |
| --- | --- | --- |
| Improve an actual theta certificate | Matched 01/18 experiment | A positive paid reserve or cheaper complete certification on one preselected difficult cell |
| Exploit a structural hypothesis the generic controls lack | 02 full-gluing multiplier | One explicit low-complexity identity with bounded endpoints and tails |
| Obtain a short analytic control theorem | 19 local collision branch | An implicit-function proof with a computable remainder; no global-constant identification |
| Complete the existing bounded task | 19 fixed negative witness | Outward negative raw Laguerre value for the selected control |
| Pursue independent arithmetic progress | 08 exact unit branch | A signed estimate before support enlargement, uniform in the relevant scales |

Recommended execution order: finish the fixed 19 certificate, run the
matched 01/18 comparison, and admit a new 02 execution only once a concrete
multiplier ansatz is written. The short local theorem in 19 can accompany
its control work. Keep 08 as a separate arithmetic option, not a claimed
transfer to the ordinary Newman heat flow. This ranking does not reopen
any program automatically.

## 1. A matched 01/18 experiment

Fix a compact time-height cell, source normalization, target tolerance and
baseline calculation before choosing the new representation. Prefer a
cell where the existing separate error envelopes are inconclusive; another
easy low-height certificate would give little information.

The targets are the complete conditional forms

\[
\mathscr L_0(H)=H_x^2-HH_{xx}\quad\text{on }H_x=0,
\qquad
\mathscr L_1(H)=H_{xx}^2-H_xH_{xxx}\quad\text{on }H_{xx}=0.
\]

Both must be addressed by a proposed paired-sign mechanism. A cheaper
complete first-jet exclusion is an alternative practical deliverable,
provided its scope is stated separately.

Write a proposed approximation as \(H=M+R\). At a physical stationary
point, \(R^{(j+1)}=-M^{(j+1)}\), and the target is

\[
\mathscr L_j(H)=-(M^{(j)}+R^{(j)})(M^{(j+2)}+R^{(j+2)}),\quad j=0,1.
\]

This suggests estimating the joint feasible values of the remainder jets
subject to stationarity. Independent absolute bounds discard precisely
the correlation that might provide an improvement. The question is
whether either representation provides a useful rigorous joint bound.

In 01, retain the complete signed Riemann--Siegel/Mordell remainder and
its derivatives, including endpoints and normalization terms. The
[Polymath heat-flow paper](https://arxiv.org/abs/1904.12438) provides an
established source for effective heat-flow approximations, not a proof of
the proposed correlated estimate.

In 18, retain enough automorphic modes and their cross contributions to
bound the complete conditional forms. Its existing examples already show
substantial cancellation: at one reported height the first two mode
contributions to the full first Laguerre form are about 1.85 and -1.15
times the answer. A positive first mode therefore cannot settle the task.

**Pass:** the complete estimate certifies a cell the baseline misses, or
reduces complete certification cost at the same accuracy. Every omitted
mode, source tail and reconstruction error is paid. A local success must
then be investigated for a uniform height/time estimate before any global
claim.

**Stop:** the new expression merely reproduces main term plus remainder,
or the omitted-mode payment consumes the reserve. Agreement of two
evaluations and positivity of one constituent do not pass this test.

## 2. A specific full-gluing question for 02

The [02 continuation brief](../../active/02_angular_jacobi_gluing/reviews/CONTINUATION_AND_BRAINSTORM_BRIEF_20261013.md)
shows why correction positivity, stable Volterra recovery and scalar
transport do not control the physical cancellation. Full imaginary Jacobi
gluing remains an additional hypothesis violated by its nearby collision
controls. Its coefficient recurrence is \(c_{n+1}=c_n\), with the genuine
normalization giving all coefficients equal to one.

A concrete speculative next ansatz is a quadratic certificate modulo
that recurrence and the physical stationary equation. Schematically,

\[
Q_j=\sum_\ell |B_\ell|^2
 +\sum_n(c_{n+1}-c_n)C_n
 +H^{(j+1)}D_j+E_j,\qquad j=0,1,
\]

where \(Q_j\) represents the complete physical Laguerre form. This is a
template to derive, not an established identity. Use a declared finite
range and degree for the multipliers. The recurrence terms and stationary
term would vanish for the genuine admissible field on the target locus;
the remaining squares must exceed a rigorous bound on the complete
boundary and tail term \(E_j\).

The essential test is whether the lattice relation can create a usable
positive reserve at the scale of the physical sum. Build the multiplier
before heat integration, or account explicitly for the moving periods and
gauges when integrating it. A finite mode truncation cannot silently stand
in for full preparation.

**First test:** a fixed low-complexity multiplier class on one declared
cell, compared with the existing scalar value/slope enclosure. Replacing
the source by a control must either violate a displayed hypothesis or
leave an explicit nonzero defect term; the same argument must not certify
a control at its known collision.

**Stop:** source uniqueness alone, an unrestricted multiplier hiding the
unknown answer, division by the unknown joint physical norm, an unbounded
angular continuation cost, or a polynomial relative gap against the
correction transform. The last is already excluded by the Schwartz versus
algebraic-tail calculation. Failure of this particular ansatz would not
prove that full gluing is exhausted.

## 3. A local theorem available in 19

The [exact control flow](../../active/19_euler_factor_controls/notes/1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md)
suggests a short rigorous route to its formal expansion. The following is
an analytic proof outline, not a new outward numerical certificate or a
completed explicit-remainder theorem.

Fix \(0<c<1\), put \(a=\tfrac12\log p\),
\(\varepsilon=a^{-2}\), \(t=\varepsilon\tau\),
\(x=\sqrt\varepsilon\,\xi\), and normalize the exact control flow by
\(H_{\varepsilon\tau}(0)\). Denote it by \(F(\varepsilon,\tau,\xi)\).
Evenness of \(H_t\) makes the resulting expression analytic in
\(\varepsilon\) near zero despite the square roots. The denominator is
nonzero near \(\varepsilon=0\), since \(H_0(0)>0\).

At zero,

\[
F(0,\tau,\xi)=1+ce^\tau\cos\xi.
\]

For \(l=\log(1/c)\), the Jacobian of \((F,F_\xi)\) with respect to
\((\tau,\xi)\) at \((0,l,\pi)\) is \(\operatorname{diag}(-1,1)\).
The analytic implicit-function theorem gives a unique nearby ordinary
double-zero branch. Using \(H_0''(0)/H_0(0)=-S_2/2\), its first
derivatives give

\[
T_*(c,p)=\frac{l}{a^2}-\frac{S_2l^2}{a^4}+O_c(a^{-6}),\qquad
X_*(c,p)=\frac\pi a-\frac{S_2\pi l}{a^3}+O_c(a^{-5}).
\]

At an ordinary double zero, the equation \(H_t=-H_{xx}\) gives a local
quadratic factor with off-real zeros immediately before the collision.
Consequently the local branch supplies \(\Lambda_{c,p}\ge T_*\).
This uses no RH assumption and does not give an upper bound for
\(\Lambda_{c,p}\).

**Deliverable:** write the analytic argument in full, obtain computable
Taylor/remainder bounds uniform for \(c\) in one compact subinterval of
\((0,1)\), and, if desired, connect this branch to the initial lowest
multiplier pair by a bounded continuation/Rouche argument. Until that
identification is proved, use \(T_*\), not the tracked-pair label \(T_0\).
Neither identification would show that it is the globally last collision.

The existing fixed witness \((p,c,t)=(41,1/2,0.2)\) remains the easiest
bounded certificate. Select its real evaluation point for a resolvable
negative **raw** Laguerre margin; closeness to the collision makes the raw
margin shrink even though its normalized ratio diverges.

An optional improvement to future screens is to match a hypothesis the
candidate proof actually uses. For example,
\(c_p=\operatorname{sech}(\delta a)\) puts the inserted time-zero zeros
exactly at \((2k+1)\pi/a\pm i\delta\). With \(0<\delta<1\), they fit
inside the usual unconditional strip in this normalization. This is an
exact calibration of the inserted zeros, not a claim about their global
collision time. The fixed-c expansion above does not apply uniformly to
this varying-c family. Such controls still insert low-height zeros and
cannot impersonate genuine low-height zero verification.

## 4. The independent arithmetic option: 08

The [unit-sector program](../../active/08_cusp_unit_sector_saving/notes/INITIAL_RESEARCH_PROGRAM_20261013.md)
has a different obstruction. Retain one exact \(B=1\) branch, its
reflected partner, phases and preimage-dependent support before replacing
them by a positive enlargement. Determine whether the signed expression
produces cancellation that disappears in the enlarged coefficient
\(\tau_{\rm div}(r)\mathbf1_{f'\mid k'}\).

The first useful result is either a rigorously improved normalized unit
return or an exact explanation of the surviving obstruction. A finite
sign pattern alone is insufficient: a substantive estimate must be
uniform in the moving scales and include outside factors. Stop if the
full calculation restores the same nonnegative coefficient and the same
row/product ratio. This remains an arithmetic track; no bridge from the
cubic-theta problem to ordinary Newman heat positivity has been proved.

## 5. A bounded new literature lead

Planat and Sole's August 2026 preprint
[Second-Level Concavity of the Riemann Xi Kernel](https://arxiv.org/abs/2608.19160)
claims a second-level kernel concavity result, with one proof using a
nonlinear Jacobi ODE and a finite cone certificate. The paper expressly
does not claim RH. Its proof and supplied certificates have not been
independently replayed in this investigation.

There is a simple screen for the relevance of the stated concavity. Use
\(r\) for squared source position and \(\tau\) for Newman time:

\[
s_\tau(r)=e^{\tau r}s(r),\quad
f_\tau=(s_\tau')^2-s_\tau s_\tau''=e^{2\tau r}f(r),\quad
(\log f_\tau)''=(\log f)''.
\]

Thus this concavity alone is invariant under Gaussian heating and cannot
distinguish the collision threshold. The nonlinear theta ODE with its
specific modular data is stronger information than a finite linear jet
dictionary, so it merits a limited audit as a possible source of useful
multipliers. A transfer theorem to the oscillatory physical forms is
still missing. Do not reopen the portfolio on the strength of the
concavity statement alone.

## Scope of this brainstorming pass

No numerical experiment, certificate replay or new global sign proof was
performed for these proposals. The exact local observations and candidate
tests above refine what should be tried next. They preserve the completed
obstructions, the distinction between local and global zero claims, and
the current explicit reopening conditions.
