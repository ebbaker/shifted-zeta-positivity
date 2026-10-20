# Can RH force simplicity at heat time zero?

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), reasoning effort ultra**,
verified from the parent session metadata. Two separate agents of the same
model checked local geometry and primary literature. This is internal LLM
analysis, not specialist review or a claim of methodological priority.

**Status: initial analysis and control screening completed; the chosen
target is the unproved implication RH ⇒ simplicity of every nontrivial
zeta zero. No new theta exclusion or signed surplus is proved.**

Edward Baker proposed applying the present machinery to a hypothetical
multiple zero at time zero. The discussion first distinguished an
unconditional simplicity theorem from one conditional on RH, then selected
the latter as a worthwhile goal in its own right. This note adopts that
final scope. The unconditional alternative is retained in §8, not silently
assumed in the conditional argument.

Read with the [manuscript][manuscript], [cap-at-infinity brainstorm][cap],
and [positive-threshold analytical program][psc]. The separate
[simplicity program][program] governs this track. The [result index][results],
[local geometry summary][geometry], [control catalogue][controls] and
[avoid index][avoid] apply, especially [reformulations][a01],
[control premises][a02], [scope][a07] and [unchecked imports][a16].
The discussion has one registration, [track chat 0003][history], relocated
from BW09 at Edward Baker’s request with its number and identity preserved.

## 1. The target is substantive; the reformulation is not a new theorem

The proposed statement is
\[
 \boxed{\quad \mathrm{RH}\ \Longrightarrow\
 \zeta'(\rho)\ne0\quad\text{at every nontrivial zero }\rho.\quad} \tag{1}
\]
Simplicity is not an established consequence of RH in the literature
checked for this note. [Bui–Heath-Brown](https://arxiv.org/abs/1302.5018)
prove a proportion of at least
\(19/27\) simple under RH; this is a historical theorem, not a claim about
the best current proportion. [Gao–Zhao](https://arxiv.org/abs/2208.06922)
explicitly assume both RH and simplicity in their negative-moment theorem.
More recent work continues
to distinguish these assumptions. See the primary references in §9.
An all-zero theorem (1) would therefore be a substantial result.

This is a scoped literature check, not an exhaustive novelty search.
Neither heat-flow splitting nor the observation that a later collision
would contradict RH is claimed as new. Also, a proportion tending to one
would still leave room for exceptional multiple zeros; (1) excludes every
exception. No logical independence of RH and simplicity is asserted.

## 2. Exact statement in the manuscript's normalization

Retain the unchanged theta source:
\[
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\qquad
 H_t=-H_{zz},\qquad
 8H(0,z)=\xi\!\left(\frac12+\frac{iz}{2}\right).
 \tag{2}
\]
Write \(x\) for the real spatial coordinate and \(t\) for heat time;
a zeta ordinate \(\gamma\) corresponds to \(x=2\gamma\). Thus
“\(T=0\)” means zero **heat time**, not zeta ordinate zero.
Since \(H(t,0)>0\), an event can be taken at \(a>0\) by evenness.

At \(s_a=1/2+ia/2\), the elementary gamma/polynomial factor in
\(\xi(s)=C(s)\zeta(s)\) is nonzero. Therefore
\[
 H(0,a)=H_x(0,a)=0
 \quad\Longleftrightarrow\quad
 \zeta(s_a)=\zeta'(s_a)=0.                         \tag{3}
\]
Critical-line simplicity alone is equivalently
\(H(0,x)^2+H_x(0,x)^2>0\) for every real \(x\); without RH this says
nothing about off-line zeros. With RH it is the full target (1).
The energy reformulation is classified as an equivalent target,
not an achieved estimate.

Under RH all zeros of \(H(0,\cdot)\) are real. Classical heat-flow
preservation gives all-realness at every \(t\ge0\). Moreover no real
multiple zero can occur at \(t>0\): its local splitting would give
nonreal zeros at a slightly earlier, still positive time. Rodgers–Tao's
\(\Lambda\ge0\) then identifies the endpoint as \(\Lambda=0\).
That lower bound is not needed for the preceding later-event exclusion.

The contradiction contract is consequently
\[
 \mathrm{RH}+\{H(0,a)=H_x(0,a)=0\}
 \ \xRightarrow[\text{missing theta estimate}]{}\
 \{H(R,b)=H_x(R,b)=0\text{ for some }R>0\}.         \tag{4}
\]
The right-hand event is impossible under RH. Merely obtaining nonreal
zeros at negative time is consistent with \(\Lambda=0\).

## 3. The local geometry transfers, including every multiplicity

Let the putative zero at \((0,a)\) have exact order \(m\ge2\), and put
\(h_j=\partial_x^jH(0,a)\), \(c=h_m/m!\ne0\). The analytic heat equation
gives
\[
 H(t,a+y)=cP_m(t,y)+\text{terms of higher parabolic weight},
 \qquad
 P_m(t,y)=\sum_{k=0}^{\lfloor m/2\rfloor}
 \frac{m!(-t)^k y^{m-2k}}{k!(m-2k)!}.              \tag{5}
\]
Here \(y\) has weight one and \(t\) weight two. The manuscript's
appendix proves that the physical jet \(J=H+iH_x\), oriented by
\(dt\wedge dx\), has an isolated zero with
\[
                    \operatorname{ind}_{(0,a)}J=-\lfloor m/2\rfloor .
 \tag{6}
\]
For small positive \(t\), the cluster consists of \(m\) simple real
zeros; for negative \(t\), only \(m\bmod2\) remain real and the others
are nonreal. Polymath Proposition 3.1 independently supplies the
Hermite-root splitting. Nothing here distinguishes zero time from any
other real event time.

For a double zero the inherited expansion is particularly explicit:
\[
 x_\pm(t)=a\pm\sqrt{2t}+\frac{2h_3}{3h_2}t+O(t^{3/2}),
 \qquad
 (x_+(t)-x_-(t))^2=8t+O(t^2).                    \tag{7}
\]
It describes a perfectly consistent emerging pair. Better local
quadratic approximation does not force a second event. The ordinary
assumption \(h_2\ne0\) must not replace the full \(m\ge2\) target.
For instance \(P_3=y^3-6ty\) has adjacent gap squares \(6t\), so a
universal use of the double-zero coefficient eight would be wrong.

## 4. What a surplus would have to prove

For an ordinary double event choose the two local simple walls and
continue them to a finite regular cap, paying all continuation and
boundary hypotheses. The manuscript gives
\[
 M_{\rm cap}=(N+1)\pi,\qquad
 W_{\rm strip}=-N/2,\qquad N\ \text{even},          \tag{8}
\]
where \(N\) is the number of simple cap zeros strictly between the walls.
The walls contribute zero phase. Under RH, there are no later events;
with those finite wall hypotheses the two roots remain adjacent, so
\(N=0\) and \(M_{\rm cap}=\pi\).

An **independent complete-source lower bound**
\(M_{\rm cap}>\pi\), derived under the putative event and RH, would
contradict this conclusion. The endpoint/middle version remains
\[
 M_{\rm ends}\ge\pi-\eta,\qquad M_{\rm mid}>\eta.   \tag{9}
\]
Every signed deficit, source remainder and cut-location error must be
included. Equations (8)–(9) identify the missing estimate; writing them
at \(T=0\) does not establish it.

For an \(m\)-fold event, following the **outermost** two local roots
changes the baseline. At a small bottom time there are \(m-2\) interior
roots. If the two outer walls remain finite and simple, and the top cap
has \(N\) interior simple roots, then
\[
 M_{\rm bottom}=(m-1)\pi,\quad
 W_{\rm strip}=-\frac{N-(m-2)}2,\quad
 M_{\rm top}-(m-1)\pi=[N-(m-2)]\pi.               \tag{10}
\]
Proof: each root-to-root lobe contributes \(-\pi\); subtract the bottom
phase and use the zero wall phases. The event-index formula makes
\(N-(m-2)=2K\), where \(K\) is the sum of later collision charges.
Thus the required strict surplus is
\[
                    M_{\rm top}>(m-1)\pi,        \tag{11}
\]
not \(>\pi\) for an outer \(m\)-root cluster. Under RH, \(K=0\).
Alternatively one can select an adjacent subpair, with baseline \(\pi\),
but its strip does not enclose the whole initial event and must not be
assigned the ordinary initial index \(-1\).

A contour through the initial event still has an undefined physical
winding. Truncation, a paid connector, or a multiplicity-appropriate
regularization is required. No lower bound for \(h_m\) is supplied.

The fixed-index cosine limit in Brainstorm 01 does not change this
accounting: adjacent labels give \(\pi\); a cluster of \(m\) consecutive
labels gives \((m-1)\pi\). Sending time to infinity does not provide a
surplus. Global wall identification is still a separate obligation.

## 5. What is gained by working at zero under RH

The potential advantage is the **combination** of two exact structures.
At zero, the source has no unknown heat tilt, and (2) gives the actual
zeta function and its derivatives. RH makes its complete zero product
real-rooted and rules out every positive-time event. The former
positive-threshold setting had all-realness but no time-zero zeta
identity at its unknown \(T>0\).

This also removes a coverage question: the contradiction starts from
the supposed finite-height multiple zero itself; no theorem asserting
that a threshold must be attained is needed. However, the height \(a\),
multiplicity \(m\), and first nonzero derivative remain uncontrolled.
The old boxes \(a\in[1001,1002]\), \(T\approx0.1\), give no coverage of
this new problem.

RH permits Laguerre–Pólya and real-zero product identities, with the
appropriate convergence and deflation at the repeated root. Their
nonstrict signs allow multiplicity. For example
\(Q=H_x^2-HH_{xx}\ge0\) still gives \(Q(0,a)=0\) at a repeated root.
Strictness cannot be inserted as though RH already proved it.
Similarly, absolute convergence of the Euler product for
\(\Re s>1\) does not license a termwise prime expansion at \(s_a\).
Any transfer to the critical line needs its actual analytic justification.

### A direct event-exclusion consumer already available

The Gaussian identity in [Note 06][gaussian] requires no all-realness.
With \(f(y)=H(s,a+y)\), \(G_s(y)=(4\pi s)^{-1/2}e^{-y^2/(4s)}\),
\[
 D_s:=s\int_{\mathbb R}G_s(f')^2-\int_{\mathbb R}G_s f^2
 =-h_0^2-sh_1^2+
   \sum_{n\ge3}\frac{n-2}{2}\frac{(2s)^n}{n!}h_n^2. \tag{12}
\]
At a putative multiple zero, \(D_s\ge0\); for the bounded nonzero theta
cap it is strictly positive, since equality would force a quadratic.
A fully paid estimate \(D_s\le-\delta<0\) instead proves
\(h_0^2+sh_1^2\ge\delta\), directly excluding the original event.
RH may be used as extra input to that estimate in the chosen track.

The statement “for each \(a\), some sufficiently small \(s\) has
\(D_s<0\)” is equivalent to first-jet nonvanishing: at a nonevent the
first two terms dominate as \(s\downarrow0\), while at an event they
vanish. It is not a weaker milestone. A useful task needs a declared
scale or analytic scale rule, a complete bound and an advantage over
the matched direct first-jet estimate. The previous failed fixed
Gaussian comparison is not reopened by changing the target's name.

## 6. The decisive time-zero controls

The controls must satisfy the actual zero-time assumptions they screen.

**Exact bounded atomic control.** \(A(t,x)=1+e^t\cos x\) has an ordinary
double zero at \((0,\pi)\), all zeros real at zero, simple real zeros at
every positive time, and no later collision. Its source is a positive
measure at frequencies zero and one. Its root cap has decrease exactly
\(\pi\); its Gaussian deficit is
\[
 D_s=1+s\sinh(2s)-\cosh(2s)>0\quad(s>0).
 \tag{13}
\]
Indeed \(D_0=D'_0=0\) and \(D''_s=4s\sinh(2s)>0\).
Thus generic positivity, heat flow and all-realness at zero do not yield
the needed opposing sign. The missing premise is the unchanged theta
source, not future simplicity.

**Arithmetic control at the exact endpoint.** For any prime \(p\), set
\(b_p=\tfrac12\log p\) and use the existing Euler-factor construction
at \(c=1\), from the [Euler-factor source manuscript][euler]:
\[
 \Phi_{1,p}(u)=\Phi(u)+\tfrac12[\Phi(u+b_p)+\Phi(u-b_p)],
 \qquad
 H^{1,p}(0,x)=H(0,x)(1+\cos(b_px)).
 \tag{14}
\]
It has real zeros of multiplicity at least two at
\(x=(2k+1)\pi/b_p\). Under RH for \(H(0,\cdot)\), the product in
(14) is all-real at zero. Local backward splitting and all-real
preservation give its threshold exactly zero and simple all-real slices
for every \(t>0\). This is a control family, not the original theta field.

Its source remains positive, even, smooth and rapidly decreasing; its
associated Dirichlet series is
\[
                  \zeta(s)(1+\sqrt p\,p^{-s})^2.  \tag{15}
\]
It preserves the other Euler factors and has a functional equation
with the adjusted conductor. It fails **unchanged zeta coefficients and
the conductor-one completion**. Consequently an argument using only
“RH-like all-realness, an Euler product, a functional equation and the
heat equation” is still insufficient. A proposed distinguishing
inequality must actually be tested on this control; merely noting that
its source differs is not a quantitative exclusion.

The remaining catalogue is screened within its stated scope:

| Control | What transfers; which premise is missing |
| --- | --- |
| Quadratic and arbitrary-jet cubic | Local events and phase identities transfer at zero; they lack the complete theta source. The quadratic keeps the ordinary half-turn. |
| \(P_m\), especially \(P_4\) | All multiplicities transfer and require (10); polynomial controls lack theta's source. |
| Two-event quartic | A later event is detected; its first event is not its all-real threshold, so it fails the conditional all-real-at-zero contract if recentered there. |
| Weighted-square and finite-prime controls | Their supplied local events screen generic source estimates; they fail full theta reflection. They do not supply an all-real slice or finite threshold. |
| Reflected, smooth and positive-primitive controls | They screen the shared shape/reflection/primitive information; they lack the unchanged normalized theta square expansion. No unsupported zero-time all-realness is assigned to them. |

Time-translating a generic source to put its event at zero does not
preserve all its arithmetic identities. The exact zero-time construction
(14) avoids that ambiguity.

## 7. Initial assessment and the next analytical decision

The conditional track is worth distinguishing from the existing program:
it targets a substantive open implication and offers exact time-zero
arithmetic together with RH's global real-zero information. Its finite
event, all-multiplicity accounting and strongest immediate control are
now explicit.

No contradictory theta estimate has yet emerged. In particular, neither
local splitting, nonnegative Laguerre quantities, ordinary cap
concentration nor the unchanged fixed-index cosine limit excludes the
initial multiplicity. This excludes those deductions from the stated
information; it is not a no-go theorem for theta-specific estimates.

The next bounded analytical task is to identify **one quantitative
consequence of the exact time-zero arithmetic plus RH** which the
\(c=1\) Euler-factor control fails, and carry it into either the complete
signed cap budget or the direct deficit (12). The phase-surplus
consumer is the primary route; the Gaussian consumer is a comparison,
not an automatic second campaign. The [parallel program][program]
sets the gates. No numerical scan is part of this opening.

## 8. Preserved alternative: what an unconditional route would need

Without RH, one later event only implies that \(\Lambda\) is at least
that event time; it is not a contradiction. A direct estimate in (12)
would still suffice without RH if its proof used no RH input. Another
possibility is to force an event strictly beyond a known upper bound
such as \(\Lambda\le0.2\), recorded by Platt–Trudgian. Equality with the
upper bound would not suffice.

A repeatable successor theorem would also suffice, subject to a
substantial extra premise: the event at zero must produce an event at
\(t_1>0\), and the theorem must apply to **every descendant event**,
at every multiplicity, producing a strictly later one.
For completeness, an infinite chain is impossible even without a
uniform lower bound on successive time increments. If \(t_1>1/2\),
there is already a contradiction. Otherwise Polymath Theorem 1.5 confines
nonreal zeros to \(|\Re z|<\exp(2C/t_1)\), for an absolute sufficiently
large \(C\), uniformly over \(t_1/2\le t\le1/2\).
If a real multiple event occurred arbitrarily far out
at \(T\ge t_1\), its nonreal predecessors at times \(>t_1/2\) would
contradict that confinement. Events are therefore in a compact rectangle
for \(t_1\le t\le1/2\). Their closed set and local isolation make it
finite, and no event occurs above \(1/2\).

This proves only the logical closure of a hypothetical repeatable
mechanism. Such a successor estimate has not been supplied; one proved
only for threshold events would not meet its hypotheses. The exact
time-zero arithmetic advantage also cannot silently be reapplied at
positive descendant times. This stronger alternative is not the selected
initial track.

## 9. Primary references checked

- H. M. Bui and D. R. Heath-Brown, *On simple zeros of the Riemann
  zeta-function*, Bull. London Math. Soc. 45 (2013), 953–961.
  [Paper](https://arxiv.org/abs/1302.5018);
  [published article](https://doi.org/10.1112/blms/bdt026).
- P. Gao and L. Zhao, *Lower bounds for negative moments of
  \(\zeta'(\rho)\)*, Mathematika 69 (2023), 1081–1103.
  [Paper](https://arxiv.org/abs/2208.06922);
  [published article](https://doi.org/10.1112/mtk.12219).
- H. M. Bui, A. Florea and M. B. Milinovich, *Negative discrete moments
  of the derivative of the Riemann zeta-function*, §1.
  [Preprint](https://arxiv.org/abs/2310.03949).
- D. H. J. Polymath, *Effective approximation of heat flow evolution of
  the Riemann \(\xi\) function, and a new upper bound for the de
  Bruijn–Newman constant*, Proposition 3.1 and Theorem 1.5.
  [Paper](https://arxiv.org/abs/1904.12438).
- B. Rodgers and T. Tao, *The de Bruijn–Newman constant is non-negative*.
  [Paper](https://arxiv.org/abs/1801.05914).
- D. Platt and T. Trudgian, *The Riemann hypothesis is true up to
  \(3\cdot10^{12}\)*, Corollary 2.
  [Paper](https://arxiv.org/abs/2004.09765).

[manuscript]: ../../09_expanding_contour_later_collision/manuscript/main.tex
[cap]: ../../09_expanding_contour_later_collision/brainstorm/01_CAP_AT_INFINITY_20261020.md
[psc]: ../../09_expanding_contour_later_collision/research-overview/03_ANALYTICAL_PHASE_SURPLUS_PROGRAM_20261020.md
[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[gaussian]: ../../09_expanding_contour_later_collision/notes/06_HEAT_FLOW_CONTOURS_AND_GAUSSIAN_CAP_ENERGY_20261020.md
[history]: ../chat-histories/0003_2026-10-20T18-25-04Z_analyze-simple-zero-contradiction.json
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a16]: ../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[euler]: ../../../../../../investigations-2/active/19_euler_factor_controls/manuscript/euler_factor_controls.tex
