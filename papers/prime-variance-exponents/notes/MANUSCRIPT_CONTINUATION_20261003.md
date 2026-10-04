# Manuscript continuation for prime variance exponents

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
The source results and this scope received internal same-model checks,
not independent specialist refereeing. No mathematical priority claim.

## Purpose of the next session

Write a new, concise, self-contained manuscript in
`/Users/ebbaker/Documents/shifted-zeta-positivity/papers/prime-variance-exponents/manuscript.tex`.
Suggested title: **Prime response variance exponents and the Riemann hypothesis**.
Its central program is to decrease a global variance exponent delta in
[0,1] for one explicitly fixed prepared prime response. The fixed-exponent
theorem identifies the corresponding zero strip; bounds along exponents
tending to zero are equivalent to RH.

This session prepares that manuscript; it is not a request to solve the
first open power-saving estimate before drafting. Use the preliminary
results below to explain what is established, what can improve
systematically in a finite range, and what additional arithmetic the
global program still needs. No fixed global delta below one and no
actual-prime exponent-descent rule have been established.

The new paper should stand on its own for a reader familiar with basic
analytic number theory. Reprove its probe properties, equivalence and
arithmetic reductions inside the paper. State standard zeta inputs
precisely and cite primary sources. Do not make the reader reconstruct
the argument from the Sonin manuscript or unpublished research notes.

## The central statement and its quantifiers

Fix the existing probe once, including its zero extension:

\[
a=\tfrac14,\qquad
h(v)=(1-16v^2)^8\mathbf1_{|v|<a},\qquad
g_0=-h'''+\tfrac14h',\qquad g=g_0/\sqrt\nu,
\]
\[
\nu=\|g_0\|_2^2
=\frac{146640624550936576}{37921101075},\qquad
A=e^{-a},\quad B=e^a,\quad
w(t)=t^{-1/2}g(-\log t).
\]

Extend w by zero outside [A,B]. Define

\[
p_g(y)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(y-\log n),
\quad
V_g(x)=\sum_{n\ge2}\Lambda(n)w(n/x)
=\sqrt x\,p_g(\log x),
\]
\[
\mathcal V_g(X)=\int_X^{2X}|V_g(x)|^2dx.
\]

Every sum is locally finite. Retain the complete support windows; over
the whole shell all active integers lie in [AX,2BX]. At a boundary the
weight is zero, so endpoint inclusion conventions do not change the sum.
The preparation gives integral w=0 and integral w squared=1.

The main theorem should be:

\[
\boxed{\quad\mathcal V_g(X)=O(X^{2+\delta})
\quad\Longleftrightarrow\quad
|\Re\rho-\tfrac12|\le\tfrac\delta2
\text{ for every nontrivial zero }\rho,\quad}
\qquad 0\le\delta\le1.
\]

The variance estimate holds for every sufficiently large real X.
For each fixed delta its constant and starting threshold may differ.
For positive delta the strip is closed: zeros on its boundary are
permitted. The symmetric form follows from the functional equation;
the forward argument first excludes zeros to the right of the strip.

State the following corollaries immediately after the theorem:

- Delta=1 is an unconditional baseline. Delta=0 is equivalent to RH.
- RH is equivalent to proving the variance bound for every positive
  delta in (0,1], or just for some positive sequence delta_j tending
  to zero. No uniform constants or uniform starting thresholds are needed.
- A single fixed delta<1 already proves a fixed zero-free strip at
  every height. For example, delta=0.99 excludes Re rho>0.995.
  These illustrative smaller exponents have not been attained.
- If useful, define the optimal exponent as the infimum of admissible
  deltas in [0,1]. It equals 2 sup_rho(Re rho-1/2); this is a translation
  of the theorem, not a computation of that supremum.

The full RH conclusion needs exponents approaching zero. A sequence of
improvements with a positive limiting delta proves only the associated
fixed strip. Numerical slopes or finite ranges do not supply the global
quantifiers above.

## A short self-contained proof route

Use only the plus-exponent convention
G(z)=integral g(v) exp(zv)dv throughout the new manuscript. Some source
notes use the opposite convention; there G_minus(s)=G(-s). Translate
their signs explicitly when importing a formula.

**Probe and noncancellation.** Prove that g is real, odd, normalized and
C^4 after zero extension, and that its mean and two exponential moments
at plus/minus one half vanish. Integration by parts gives

\[
G(z)=\frac{z(z^2-1/4)}{\sqrt\nu}H(z),\qquad
H(z)=\int_{-a}^a h(v)e^{zv}dv,
\]
\[
\frac{H(z)}{H(0)}
=\sum_{k\ge0}\frac{(z^2/64)^k}{(19/2)_k k!}.
\]

Avoid a long Bessel-function detour. An elementary energy argument
proves the needed zero location. If f=H/H(0) and f(z_0)=0, set
u(t)=f(z_0t). The displayed series gives

\[
(t^{18}u')'=\frac{z_0^2}{16}t^{18}u,
\quad u(0)=1,\quad u'(0)=0,\quad u(1)=0.
\]

Multiply by conjugate u and integrate on [0,1]. Vanishing boundary
terms give a strictly negative real value for z_0 squared. Thus every
zero of H is nonzero and purely imaginary. In particular G(-s) is
nonzero for 0<Re s<1/2. The preparation zero at s=1/2 cancels the
pole of zeta and cancels no nontrivial zero to the right of its line.

**Transform decay and the complete explicit formula.** The function g
and its derivatives through order four vanish at the endpoints. Its
piecewise fifth derivative has endpoint jumps, so its sixth
distributional derivative is a finite measure with endpoint atoms.
Distributional integration by parts gives

\[
G(\sigma+it)=O_g((1+|t|)^{-6}),\qquad |\sigma|\le\tfrac12.
\]

Combine this with the standard count N(T)=O(T log T). For y>a the
complete linear explicit formula is

\[
p_g(y)=-\sum_\rho m_\rho G(1/2-\rho)e^{(\rho-1/2)y}
       -\sum_{k\ge1}G(2k+1/2)e^{-(2k+1/2)y}.
\]

Include both signs of ordinates and all multiplicities. The pole at one
is canceled; the trivial-zero terms remain. State the smoothing or
contour argument that justifies this formula for the C^4 probe and show
absolute, locally uniform convergence of the nontrivial sum. A standard
explicit-formula citation is appropriate, but the resulting linear
formula and its hypotheses must be visible in the paper. Handle the
initial compact interval with the original finite arithmetic sum.

**Forward implication by logarithmic shells.** This is shorter than
introducing a second RH criterion through Hardy norms or weighted energy.
The exact change of variables gives

\[
\int_{\log X}^{\log(2X)}|p_g(y)|^2dy
=\int_X^{2X}\frac{|V_g(x)|^2}{x^2}dx
\le X^{-2}\mathcal V_g(X).
\]

Under the assumed exponent, the shell with X=2^j has energy O(2^{j delta}).
Shellwise Cauchy–Schwarz bounds its contribution to the true Laplace
integral by a constant times 2^{j(delta/2-Re s)}. This geometric sum
converges locally uniformly for Re s>delta/2, including delta=0;
the same domination justifies holomorphy there. Since a<log 2,
p_g(y)=0 for 0<=y<log 2-a and every translated packet lies above zero.
Thus the integral from zero includes its complete transform without
an initial endpoint correction. On Re s>1/2, direct termwise
integration and the absolutely convergent Dirichlet series give

\[
P_g(s)=\int_0^\infty e^{-sy}p_g(y)dy
=-G(-s)\frac{\zeta'}{\zeta}(1/2+s).
\]

Uniqueness of meromorphic continuation identifies this expression with
the holomorphic true transform in the larger half-plane. A zero
rho=beta+i gamma with beta-1/2>delta/2 would leave the nonzero residue
-m_rho G(1/2-rho), contradicting holomorphy. Use functional-equation
symmetry to obtain the symmetric closed strip.

**Converse and endpoints.** Under the strip assumption, absolute
summability of the nontrivial coefficients bounds their sum by a
constant times exp(delta y/2). The trivial contribution is bounded for
y>=1. Hence p_g(y)=O(exp(delta y/2)), V_g(x)=O(x^((1+delta)/2)), and
integration gives the exact variance exponent 2+delta, with no extra
logarithm. This argument allows strip-boundary zeros. If cumulative
energy J(Y) is mentioned, delta=0 gives J(Y)=O(1+Y), not O(1).
Do not assert convergence at an exponential-weight boundary. Finally,
intersect the strips for delta_j tending to zero to obtain RH.

## Preliminary results to carry into the new paper

Include the following relevant results with brief proofs and exact scope.
The source links below identify the detailed derivations and internal
reviews; they are drafting inputs rather than replacements for proof.

**Unconditional baseline.** With E(t)=psi(t)-t and
M_w=integral_A^B u|w'(u)|du, integration by parts gives
V_g(x)=-integral_A^B E(xu)w'(u)du. If |E(t)|<=t r(t) throughout
[AX,2BX], then

\[
\mathcal V_g(X)\le\frac73 M_w^2X^3
\left(\sup_{AX\le t\le2BX}r(t)\right)^2.
\]

The already checked Johnston–Yang Theorem 1.4 yields

\[
\mathcal V_g(X)=O_g\left(
X^3(\log X)^{3.602}
\exp\left[-0.3706\frac{(\log X)^{3/5}}{(\log\log X)^{1/5}}\right]
\right).
\]

This is an application of known PNT estimates, still at global delta=1.
Retain the exact supremum if giving an explicit range. A decaying
subpower factor on X cubed does not supply a fixed exponent improvement.

**Finite quadratic variance certificates.** For every real X in the
displayed ranges, the existing rational transfer establishes

\[
\mathcal V_g(X)<38X^2\ (e\le X\le10^{99}),\quad
\mathcal V_g(X)<40X^2\ (e\le X\le10^{100}),\quad
\mathcal V_g(X)<72X^2\ (e\le X\le10^{102}).
\]

Derive these from |p_g(y)|<=b+R_H exp(y/2), y>=1, where the existing
outward records prove b<4.96 and R_H<1.56e-51 at H=3*10^12. Integrating
over the complete shell gives

\[
\mathcal V_g(X)\le\tfrac32b^2X^2+
\tfrac45(2^{5/2}-1)bR_H X^{5/2}+\tfrac73R_H^2X^3.
\]

The input is published finite-height critical-line verification together
with the certified low-zero mass and an unconditional high-zero allowance.
The linear tail has R_H=O(H^-5 log H), not the twelfth-power decay of an
autocorrelation. For a fixed admissible ceiling and low cutoff, the
certified range scales as H^10/(log H)^2 along verified heights.
That supplies a systematic finite-range milestone, not a global delta=0.

Give the analytic transfer in the main text and place the exact
polynomial constants, source hashes and rational budgets in a short
certificate appendix. Link the existing reproducibility packages; do
not duplicate a large zero cache or claim the old outward calculations
were independently regenerated in the new session.

**Short-interval arithmetic reduction.** For 1<=h<=AX define

\[
D_h(t)=\psi(t+h/2)-\psi(t-h/2)-h,\qquad
S(X,h)=\int_{AX}^{2BX}|D_h(t)|^2dt,
\]
\[
V_h(x)=h^{-1}\int w(t/x)D_h(t)dt,\qquad
C_{\rm app}=\frac{(4\log2)(B+A/2)}{24}\|w''\|_\infty.
\]

Prove exact centering by finite Fubini, then use symmetric Taylor
averaging and elementary Chebyshev to include every atom in the
expanded support band. The resulting unconditional bounds are

\[
\mathcal V_g(X)\le3X^2S(X,h)/h^2+C_{\rm app}^2h^4/X,
\]
\[
\left|\sqrt{\mathcal V_g(X)}-\sqrt{Q_h(X)}\right|
\le C_{\rm app}h^2/\sqrt{2X},\quad
Q_h(X)=\int_X^{2X}|V_h(x)|^2dx.
\]

Write out the exact signed covariance

\[
Q_h(X)=h^{-2}\int_{AX}^{2BX}\int_{AX}^{2BX}
D_h(t)D_h(u)W_X(t,u)dt\,du,
\quad W_X(t,u)=\int_X^{2X}w(t/x)w(u/x)dx.
\]

At h=X^(3/4), Q_h and the original variance have precisely the same
admissible exponents 2+delta for delta>=0; the norm error is O(X).
This is the principal open arithmetic formulation for the paper.
The Gram kernel is positive as a form, but its cross terms retain their
signs and should not be bounded individually by absolute values.

A proposed raw estimate S(X,h)<=C Xh^2 X^(-kappa)L(X), with
h=X^tau and L=X^(o(1)), gives every
delta>max(0,1-kappa,4tau-3). At tau=3/4 the support and averaging error
is already O(X^2). An unbounded L does not justify the frontier endpoint.
The checked Saffari–Vaughan input gives only a subpower saving and leaves
delta=1. State that limitation briefly; its long source audit can remain
in a note or appendix. Do not treat a theta lemma silently as a psi lemma.

**Why a descent rule is an additional theorem.** Retain a concise
proposition or appendix showing that the current generic controls
cannot force delta downward. For each 0<delta<1 one can keep any finite
prefix of actual coefficients, then greedily choose nonnegative
coefficients zero or log n tracking

\[
\widetilde\psi(x)=x+\eta\Re\frac{x^{\beta+i\gamma}}{\beta+i\gamma}
+O(\log x),\quad \beta=(1+\delta)/2,\quad\gamma\ne0,
\quad0<\eta<\tfrac12.
\]

The prepared response has variance of exact order X^(2+delta) for every
sufficiently large real X, with a strictly positive minimum of the
rotating-phase shell integral. It keeps PNT and relevant preparation and
diagonal controls and defeats every smaller exponent. Prove the finite
prefix tracking and the phase minimum if stating the proposition.
Once the retained prefix is fully included, the exact diagonal identity
has only a fixed prefix correction; its asymptotic remains Y^2/2+O(1).
These sequences are not the actual Euler-prime sequence; the result
neither disproves RH nor rules out a prime-specific improvement.
Avoid importing frame-operator machinery just to list extra retained
properties. The model's role is to identify the additional arithmetic
information needed by a genuine descent mechanism.

## Suggested organization and scope

Aim for approximately 12–16 pages including short appendices and
references; retain necessary proof rather than obeying an arbitrary
page limit. A useful order is:

1. Introduction, fixed variance, main theorem and the delta-to-zero goal.
2. Prepared probe, elementary noncancellation and transform decay.
3. Proof of the exponent and zero-strip equivalence, including endpoints
   and the RH corollary along decreasing exponents.
4. Unconditional baseline and finite quadratic bounds, clearly separated
   by their quantifiers.
5. Short-interval averaging and the exact signed covariance, with a
   table translating a proposed saving into an admissible delta.
6. First global milestone and the need for additional prime arithmetic.
7. Short appendices for certificate constants and the generic model
   proof if these would otherwise interrupt the main exposition.

Omit Sonin operators, exact projection survival, finite Euler transport,
Schur complements, the selective-loss positive-square split, centered
negative index and seven-source Gram matrices. The long singular-series
decomposition, fitted-error diagnostics and additive-frequency
localization are also unnecessary for the equivalence or retained
preliminary results. Mention the parent investigation in at most a short
provenance paragraph. An optional closing sentence may point to signed
prime-pair or frequency projections as alternative methods, without
developing another equivalent RH condition.

Keep the introduction and abstract about the exponent program. Describe
the result as a focused quantitative reformulation and research program,
without an unverified novelty claim or a claim of a new zero-free strip.
The first actual-prime saving, however small, would be the first global
milestone. A rule repeatedly improving a proved exponent is a separate
open problem, not an assumed property of the program.

## Source reading order

All links are relative to this continuation note. Read the first four
program notes before touching the much longer parent manuscript.

| Source | Use in the new manuscript |
| --- | --- |
| [Baseline and fixed exponent theorem](../../investigations/sonin-critical-boundary/notes/subpower-milestones/01_baseline_and_exponent_budget_20261003.md) | Central statement, endpoints and known PNT transfer |
| [Short interval transfer and signed projection](../../investigations/sonin-critical-boundary/notes/subpower-milestones/02_short_interval_transfer_and_gate_20261003.md) | Main arithmetic reduction and exponent budget |
| [Finite variance theorem](../../investigations/sonin-critical-boundary/notes/subpower-milestones/03_finite_range_variance_20261003.md) | Continuous finite bounds and verified-height range law |
| [Generic structural obstruction](../../investigations/sonin-critical-boundary/notes/subpower-milestones/04_structural_nonbootstrap_20261003.md) | Concise model proposition and limitations of bootstrap |
| [Program ledger](../../investigations/sonin-critical-boundary/notes/subpower-milestones/MILESTONES.md) | Distinguish established transfers, finite results and open global targets |
| [First investigation review](../../investigations/sonin-critical-boundary/reviews/SUBPOWER_FIRST_INVESTIGATION_REVIEW_20261003.md) | Mathematical and certificate checks; one corrected prefix qualifier |
| [Earlier program review](../../investigations/sonin-critical-boundary/reviews/SUBPOWER_MILESTONES_PROGRAM_REVIEW_20261003.md) | Fixed exponent and baseline source audit |
| [Parent manuscript](../../investigations/sonin-critical-boundary/manuscript.tex) | Only prepared polynomial, transform series, nonvanishing proof and relevant classical bibliography |
| [Complete response note](../../investigations/sonin-critical-boundary/notes/selective-loss-program/04_complete_response_and_signed_pairs_20261003.md) | Linear explicit formula and causal support, when needed |
| [Linear tail and low zero certificate derivation](../../investigations/sonin-critical-boundary/notes/selective-loss-program/05_quadratic_target_and_finite_sign_20261003.md) | Linear constants, multiplicities, zero-count completeness and trivial tail |
| [Finite variance numerical package](../../investigations/sonin-critical-boundary/numerics/subpower_finite_variance_20261003/README.md) | Small rational transfer, input hashes and exact budgets |
| [Original outward numerical package](../../investigations/sonin-critical-boundary/numerics/selective_loss_quadratic_target_20261003/README.md) | Imported 192/256-bit zero mass and derivative constants |

The primary arithmetic inputs already audited in those notes are
[Johnston–Yang, Theorem 1.4](https://arxiv.org/pdf/2204.01980),
[Platt–Trudgian, Theorem 1](https://arxiv.org/pdf/2004.09765),
[Hasanalizade–Shen–Wong, Corollary 1.2](https://arxiv.org/pdf/2107.06506),
and [Saffari–Vaughan, Section 6](https://aif.centre-mersenne.org/item/10.5802/aif.649.pdf).
Verify the final bibliography against primary texts. The low-zero count
and enclosure APIs are documented in
[FLINT acb_dirichlet](https://flintlib.org/doc/acb_dirichlet.html).

At handoff the repository HEAD is
`4c5605edff32dc505c16046362d1700d262990e7`, but the recent subpower notes
and certificate package include uncommitted working-tree files. Read
the actual paths; checking out that commit alone does not recover all
the results. The parent manuscript SHA-256 is
`1529eadf01166945528254f3b5a78f405b06479e04de484ce10f11fd837b408d`.
The finite variance record SHA-256 is
`7576708c6cd4e0e9be89d7551d1386ef77b9c972908f55d50f864b9c4afc6b26`.
If sources changed, reconcile the new content before reproducing claims.

## Deliverables and verification for the next session

Create the new root manuscript.tex and keep it as the single editable
source. Use author Edward Baker or Drafted for Edward Baker, as appropriate
to his attribution preference, and include a clear acknowledgement of
substantial LLM assistance and the limits of internal review. Keep the
mathematical paper free of chat chronology and model workflow details.

Use notes/ for later derivations, reviews/ for proof and manuscript checks,
and numerics/ for small reproduction scripts or records. Follow the
repository [large file policy](../../../LARGE_FILES.md); keep large
regenerable data and third-party PDFs outside git. Reference the existing
certificates instead of copying every parent investigation file. The
paper's analytic proof should be self-contained even when its reproducible
numerical input is supplied by a linked certificate package.

Record notable manuscript milestones in DRAFT_HISTOR.md at the new root,
using the filename specified by the project instructions: date, topic,
commit or tag when available, why it matters, and linked note or review.
Do not create draft snapshot folders. Update the new README with the
draft's scope and verified status once the draft exists.

Have a fresh proof pass check transform signs, both directions of the
theorem, delta=0 and delta=1, closed strip boundaries, multiplicities,
support caps, the short-interval error and exponent conversion. Replay
the existing finite variance generator into a temporary output and
compare its record; no new large numerical computation is required.
Save a concise review with the model and effort level actually available.

In a Codex desktop session, open the new saved source in the built-in
LaTeX editor and use its compile_latex_document diagnostic tool after
editing. Fix errors within the tool's repair limits; opening a preview
alone does not confirm compilation. This current session leaves the
already open Sonin manuscript in place. The future drafting session is
explicitly authorized to create and open the new manuscript in its new
folder. Do not install a TeX distribution or create a separate replacement
source merely to check the draft when the built-in compiler is available.

The session is complete when the new manuscript has coherent full proofs,
the preliminary results have their correct status, the bibliography and
reproduction links resolve, the finite certificate replay passes, and
compilation succeeds or a concrete compiler limitation is reported.
No proof of an unachieved global delta reduction is required to complete
this manuscript-writing task.

## Recommended platform

**Use Codex for the next drafting session in the local repository.**
This is a practical recommendation for this task: it combines LaTeX
editing, precise source selection, certificate replay and review of file
changes in the workflow already used here. It is not a claim that the
Codex interface has intrinsically better mathematical reasoning.

Current [official OpenAI guidance](https://learn.chatgpt.com/docs/use-chatgpt)
says ChatGPT Work and Codex have overlapping capabilities, including
research and documents; their desktop interfaces differ in the technical
detail they expose. [Local project guidance](https://learn.chatgpt.com/docs/projects)
also supports folder access when the task has the appropriate local
environment. ChatGPT Work is therefore a reasonable alternative when
configured with the repository sources. Ordinary Chat is useful for
discussing the argument or revising prose; an optional fresh ChatGPT pass
can challenge the exposition and proof, but remains an LLM review.

Whichever interface is used, choose an available model and reasoning
setting suitable for difficult proof checking, and record the actual
configuration rather than inferring it. Attach this continuation note
and ensure the session can read the original notes and certificates.
Avoid transferring the entire long Sonin chat as its primary context.

## Suggested first message for the new session

Read this continuation note and the listed four subpower research notes.
Write the concise self-contained manuscript described here in
`/Users/ebbaker/Documents/shifted-zeta-positivity/papers/prime-variance-exponents/manuscript.tex`.
Center it on the equivalence between the fixed prepared-prime variance
bound O(X^(2+delta)), delta in [0,1], and the corresponding closed zero
strip, with RH as the limit of exponents tending to zero. Include the
relevant baseline, finite variance bounds, signed short-interval reduction
and generic obstruction. Reprove the core arguments and keep irrelevant
Sonin machinery out of the paper. Distinguish proved transfers, finite
certificates and open global estimates. Add the author and LLM
acknowledgement, obtain a fresh internal proof review, replay the small
certificate, and compile the new saved source. Preserve the parent project.
