# TND-OG-E03 r1 — assemble the direct signed-log upper certificate

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Actual backend identifier and effort
are unavailable in accessible session metadata.

**Type E; recommend Sol6.1**, effort selected by the author. The field,
local estimate, proof route, constants and completion test below are
fixed. **READY, UNACTIVATED at issue.** This request is the sole selected
successor of B02, not a new mechanism-selection task or a numerical pilot.
The [sole register](../01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md)
owns live status. The [input manifest](09_TND_OG_E03_INPUTS_20261108.json)
binds immutable sources; do not edit them to repair the proof.

## Objective and fixed scope

Prove a fully paid, one-sided finite-source upper approximation to the
actual time-zero canonical Green potential, with an explicit error
tending to zero. Reuse [Note04](../../notes/04_TND_OG_B02_ONE_SIDED_BOUNDARY_LOG_ACQUISITION_20261108.md)
(3)–(18), auditing their use. This is an acquisition theorem: **a favorable
value below the defect margin is not its success condition** and must not
be claimed without new evidence.

Fix the literal complete theta source, \(H_0=\xi(s)/8\),
\[
 s=\tfrac12-iz/2,\quad F=(s-1)\zeta(s)/s=D_0H_0,\quad
 D_0=16\pi^{s/2}/[s^2\Gamma(s/2)],\quad
 a=\pi/8,\quad K(u)=1/[16\cosh(au)].
\]
No preconditioning polynomial, new zero measure, shifted Newman time,
zero-free comparison field, boundary lower modulus or zero simplicity
assumption. The source approximant may have zeros. No numerical execution,
manuscript production or sibling modification is authorized by this packet.

## 1. Recheck the local input and derive its full logarithmic tail

Use the exact constants B=26/3, kappa=log(27/26), c0, M_v, A_v, n_v,
C_v and E_v(delta) of Note04. Its one-dimensional sublevel estimate is
required; the sibling's area estimate is not a substitute.

The following deliberately coarse constants fix a candidate closed tail:
\[
 L_0=\log(26/c_0),\quad N_0=2+L_0/\kappa,\quad
 C_{\log}=\log26+2B e^{51\kappa}N_0^2,\quad q=e^{-a}.
 \tag{E1}
\]
Prove from Note04(17)
\[
 \int_{v-1/2}^{v+1/2}|\log|F(x)||\,dx
 \le C_{\log}[1+\log(1+|v|)]^2.
 \tag{E2}
\]
The intended proof uses
\(M_v\le26(1+|v|)\),
\(n_v\le N_0[1+\log(1+|v|)]\), and \(A_v/n_v\le\kappa\).
Justify the elementary inequality \(N_0\ge1/\kappa\).

For integer R>=1, prove the complete single-boundary absolute tail
\[
 \int_{|x-X|>R}K(x-X)|\log|F(x)||\,dx
 \le {\cal T}(X,R)
 :=\frac{C_{\log}}4e^{-aR}
 [1+\log(|X|+R+2)]^2\frac{1+q}{(1-q)^3}.
 \tag{E3}
\]
Cover both sides by unit intervals centered at \(X\pm(k+1/2)\),
k>=R, and use \(K(u)\le e^{-a|u|}/8\).
For S=|X|+R+2,
\(1+\log(S+j)\le(1+\log S)(1+j)\);
the geometric moment is
\(\sum_{j\ge0}q^j(1+j)^2=(1+q)/(1-q)^3\).
Retain the height factor in joint limits. This is a tail for F's exact
logarithm, not a full-line bound for the finite source approximant.

## 2. Compact envelope and complete source payment

For a compact boundary approximation satisfying
\(\sup_{|x-X|\le R}|F-\widehat F|\le\delta\), 0<delta<=1, define
\[
 {\cal I}_{X,R,\delta}
 =\int_{X-R}^{X+R}K(x-X)\log(|\widehat F(x)|+\delta)\,dx,
\]
\[
 {\cal E}_{X,R}(\delta)=
 \sum_{k=0}^{R-1}
 \frac{{\cal E}_{X+k+1/2}(\delta)+
       {\cal E}_{X-k-1/2}(\delta)}{16\cosh(ak)}.
 \tag{E4}
\]
Prove that the compact envelope minus the exact compact logarithmic
integral lies in [0,E_(X,R)]. The actual signed logarithmic integral
must be retained; do not replace it by separate positive/negative
absolute bounds, a quadratic moment or a harmonic baseline.

Use the literal finite, even reflected theta source and radial cutoff
already defined in OG Note02(22):
\[
 \widehat H(z)=\tfrac12\int_{-V}^{V}\Phi_{N_{\rm src}}(u)e^{izu}\,du,\quad
 \delta_H=\tfrac12[5C_2(N_{\rm src}){\cal Q}+B_0{\cal Q}^{>V}].
 \tag{E5}
\]
Check the source definition and its complete arithmetic/radial error;
do not infer matching odd derivatives of a reflected finite prefix.
Take \(\widehat F=D_0\widehat H\) and use the inherited compact bound
with A=1,
\[
 {\cal B}(X,R)=16\pi^{9/4}
 \exp\{9/4+\pi^2[81+(|X|+R)^2]/192\},\qquad
 \sup_{|x-X|\le R}|F-\widehat F|\le {\cal B}\delta_H.
 \tag{E6}
\]
Pay any future certified field-evaluation error additively in delta.
No full-boundary use of B is permitted. The local lemma requires
holomorphy only of the exact F, not of noisy evaluation data.
The chosen positive delta can exceed the actual field error.

## 3. Prime baseline, sign and completion inequality

Keep precisely the inherited time-zero identity
\[
 J_0^{\rm G}(X)=\int_{\mathbb R}K(x-X)\log|F(x)|\,dx-P(X)+G(X,1),
\]
\[
 P_Q(X)=\sum_{2\le n\le Q}
 \frac{\Lambda_{\rm vM}(n)}{\log n}
 \frac{n^{-5/2}}{1+n^{-4}}\cos((X/2)\log n),\qquad
 |P-P_Q|\le\beta_Q=\tfrac23Q^{-3/2},
 \tag{E7}
\]
where Q>=2 is an integer. Verify the plus pole term and the absence
of a second correction from q(s). There is no newly truncated upper
boundary or safe-center value: those are already eliminated by (E7).

Define
\[
 U_{R,Q,\delta}(X)
 ={\cal I}_{X,R,\delta}+{\cal T}(X,R)-P_Q(X)+\beta_Q+G(X,1).
 \tag{E8}
\]
The main acceptance condition is the complete two-sided error statement
\[
 \boxed{0\le U_{R,Q,\delta}(X)-J_0^{\rm G}(X)
 \le{\cal E}_{X,R}(\delta)+2{\cal T}(X,R)+2\beta_Q.}
 \tag{E9}
\]
All constants are explicit; no unproved numerical onset or hidden
all-center error is allowed.

Prove the following finite choices for each prescribed X and tolerance h>0:
first R with T<=h/6, then Q with beta<=h/6, then delta with E<=h/3,
and finally N_src,V and field arithmetic meeting (E6). Smaller fixed
allocations are allowed to reserve later integration/rounding error.
For a prescribed sequence |X| tending to infinity or d tending to zero,
repeat these choices with h chosen from the actual margin
\(m(d,r)=\sin(\pi/8)d/\cosh(\pi r/8)\).
This is finite acquisition per tuple, not a common cutoff or useful
complexity bound.

Give the elementary common-M version on each fixed compact center interval,
if claimed, with the same complete tail/source payments. This does not
establish small values at every center or authorize a height scan.

Future evaluations must provide a directed upper value
\(U\le\overline U\le U+\eta_{\rm eval}\), paying field, finite prime,
G, compact integration and arithmetic errors explicitly. Then
the upper error in (E9) increases by eta_eval. The regularized integrand
is continuous for continuous \(\widehat F\); a quadrature existence
argument may retain its 1/delta sensitivity. Do not claim a numerical
integration, affordable cost, or automatic cancellation at finite precision.

## 4. Scope and control acceptance

- Classify (E9) as an acquisition theorem. The additional inequality
  \(\overline U<m(d,r)\) remains an unpaid value condition, not a result
  of the source cutoff choice.
- Recheck OG Note01's square-root family, the E02 short-polynomial
  obstruction, the sibling harmonic-baseline floor and every relevant
  family in controls12 using Note04's table. No numerical replay is needed.
- A generic defective field must retain its positive Green response.
  Do not give it the canonical Euler anchor/P unless it actually has them.
- Retain all multiplicities. No growing derivative order is used.
- No lower bound on J, nonreal-zero existence, RH, or a uniform
  critical-line zero-free margin follows.

## Outputs, finite limit and stopping rule

One proof note in notes, one proof-author check in reviews, one exact
return in research-progress/handoffs, source-use updates if necessary,
the sole register update and a continuation/model-change note. Preserve
this request r1 and its frozen inputs. Work only within the TND-OG branch;
leave parent/sibling research, manuscripts, shared result summaries,
existing chat JSON and historical manifests unchanged.

Allow one bounded correction cycle for constants, signs, ordinary
domain estimates or conservative budget allocations, recorded additively.
A failure of the local line estimate, an indispensable new arithmetic
smallness hypothesis or a required change of observable/source is a
**B02 r2 trigger**; record the exact failed clause and stop that dependency.
Do not turn an absence of a favorable computed value into such a failure:
none was required.

Stop at (E9), its honest failed clause, or the one allowed correction.
No automatic new mechanism, numerical campaign or manuscript integration.
If completed, a separate claim-level assessment can be specified next;
it is not issued or activated by this request. A model change alone
does not constitute independent specialist review.
