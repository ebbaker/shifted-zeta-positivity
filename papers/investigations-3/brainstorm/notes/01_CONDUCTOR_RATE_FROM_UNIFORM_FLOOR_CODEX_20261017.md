# Retaining the conductor dependence in the uniform floor

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Model **gpt-6-astra (Codex)**; effort **ultra**.

**Status: a deduction from the existing Project 03 propositions, with a
proof below and same-model internal checks.** This note does not independently
reprove their transport envelope, interval certificate, or one-step
approximation theorem. It inherits their named imports and review status.
There is no additional GRH assumption. Separate review of this corollary
and cross-family review of the underlying round-two chain remain advisable
before manuscript integration. No literature-wide originality is asserted.

## 1. Inputs and the information retained

Project 03's [uniform-floor note, §§1–6][floor] proves a remainder bound
E < 1/5 for every ell >= 129/5 and every h=t/2 in (0,1/8]. It proves
kappa(sigma*) <= kappa(2) < 57/100, where kappa=-zeta'/zeta, and

\[
 S_\chi(x,3,t)\ge \frac{\ell_*}{4}
             -\frac{\kappa(\sigma_*)}{2}-\frac E2,
 \qquad
 \ell_*\ge \log(q/\pi)+\psi(1).
\]

The final displayed bound in that note replaces ell* by 129/5 and then
rounds the resulting floor down to 6. Its domination arguments, however,
cover **all** ell >= 129/5; they do not upper-bound the allowed conductor.
Retaining the larger main term therefore gives, with Euler's constant gamma,

\[
 L(q)=\log(q/\pi)-\gamma,\qquad
 C(q)=\frac{L(q)}4-\frac{77}{200},
 \tag{1}
\]

\[
 S_\chi(x,3,t)>C(q)>6
 \quad(q\ge10^{12},\ x\in\mathbb R,\ 0\le t\le1/4).
 \tag{2}
\]

Here 77/200 = (57/100)/2 + (1/5)/2. At t=0 the exact Euler-product
floor is stronger, so no limit of a singular small-time expression is
needed. The source certificate gives L(10^12)>25.8, hence C(q)>1213/200>6.
The argument covers both parities and both real-height directions for
individual primitive characters, including non-even complex-character
flows in Project 01's normalization.

The second input is Project 03's [one-step strip-transfer lemma][restart].
If a real entire heat slice has squared zero-strip height Q<=1 and global
height-three floor C, define

\[
 m_C(s)=\frac{Ce^{-s/2}}{1+2C(1-e^{-s/2})}.
\]

For 3/4<c<m_C(delta), k_c=4c/3-1, it gives at the end of the step

\[
 Q_{\rm next}\le
 \max\{(Q+2/k_c)e^{-k_c\delta}-2/k_c,0\}.
 \tag{3}
\]

That lemma supplies the sine-tail approximation, compact contact argument,
heat convergence, and preservation of reality after the strip reaches
zero. Its restart section establishes order at most one, nonzeroness,
and the heat semigroup identity for the original time slices. These
conditions are part of the input here, not consequences of the scalar
recurrence alone.

## 2. Constant-floor restart limit

**Lemma.** Suppose these one-step hypotheses hold along a real entire heat
orbit for 0<=t<=T_0, its initial squared strip is at most one, and every
original time slice has floor at least C>3/4. Set

\[
 k=\frac{4C}{3}-1,\qquad
 \tau(C)=\frac{\log(1+k/2)}{k}.
 \tag{4}
\]

If tau(C)<T_0, the function at time tau(C) has only real zeros.

**Proof.** Fix T with tau(C)<T<T_0. By continuity choose c<C, c>3/4,
so close to C that T>tau(c). Since m_C(delta) tends to C as delta
decreases to zero, choose a finite integer n sufficiently large that
delta=T/n satisfies m_C(delta)>c. Apply (3) successively at the n
**original** time slices. The number n may depend on C and T.

Until the positive-part recurrence reaches zero, its explicit expression
from the larger initial value Q_0=1 is

\[
 Q_j^{\rm raw}=(1+2/k_c)e^{-k_cj\delta}-2/k_c.
\]

At j=n this is negative because T>log(1+k_c/2)/k_c. Therefore a zero
strip must have been reached by time T, and subsequent evolution preserves
reality. At no point is the original arithmetic floor assigned to an
approximant over an entire long interval: the one-step lemma pays its
short-time floor loss anew at each original slice.

This works for every T strictly above tau(C). Let T decrease to tau(C).
Heat continuity on compact sets, nonzeroness, and Hurwitz in each open
half-plane prove reality at the endpoint. No infinite composition of
approximants, conductor-uniform approximation radius, or confinement
hypothesis for the original character flow has been assumed. QED.

## 3. Explicit conductor consequence

With (1), write

\[
 k(q)=\frac{L(q)}3-\frac{227}{150},\qquad
 T(q)=\frac{\log(1+k(q)/2)}{k(q)}.
 \tag{5}
\]

The constant 227/150 equals 1+(4/3)(77/200). The function
log(1+k/2)/k decreases for k>0: its derivative has numerator
k/(k+2)-log(1+k/2)<0. As C(q)>6,

\[
 0<T(q)<\frac{\log(9/2)}7<\frac14.
\]

The last strict inequality follows already by the positive Taylor lower
bound e^(7/4)>1+7/4+(7/4)^2/2+(7/4)^3/6>9/2. In fact the comparison
with the existing 43/200 benchmark also follows exactly:

\[
 \sum_{j=0}^{7}\frac{(301/200)^j}{j!}-\frac92
 =\frac{10360897549575881}{3072000000000000000}>0.
\]

Hence log(9/2)/7<43/200. Thus the entire restart argument stays inside
the interval certified by the existing floor, and the comparison with
0.215 does not rely on the floating diagnostic below.

Consequently, from the cited source propositions,

\[
 \boxed{\Lambda_\chi\le
 \frac{\log(1+\tfrac12[\tfrac13(\log(q/\pi)-\gamma)-227/150])}
 {\tfrac13(\log(q/\pi)-\gamma)-227/150}
 \qquad(q\ge10^{12}).}
 \tag{6}
\]

For orientation only, ordinary floating evaluation at q=10^12 gives about
0.2130631631. This decimal is not a new outward-rounded certificate; (6)
is the exact expression justified by the argument. It is already below
the existing 0.215 benchmark if the inherited analytic inputs are accepted.

As q tends to infinity,

\[
 T(q)=\frac{3\log\log q-3\log6}{\log q}
       +O\!\left(\frac{\log\log q}{(\log q)^2}\right).
 \tag{7}
\]

This improves the **rate furnished by these repository arguments** from
Project 01's O((log q)^(-4/7)) to O(log log q/log q). Dobner's named
nonnegativity theorem gives the corresponding two-sided conclusion
0<=Lambda_chi<=T(q). The upper bound itself does not need that lower-bound
theorem. A conductor limit does not prove GRH for any fixed character.

## 4. Controls, provenance and next decision

This is a quantitative milestone under [avoid 01][a01], not an RH-equivalent
criterion. Its control screen is the one in [summary 12][s12] and the
uniform-floor note: the Euler-factor control's altered logarithmic
coefficient violates the zeta coefficient majorant; the weighted-square,
reflected, smooth and positive-primitive controls lack the required
primitive-character arithmetic and partial-sum bounds. No common shape
property has been promoted into (2). The general restart lemma would
apply to any control meeting its actual strip and floor hypotheses;
those hypotheses must be measured or proved for that control itself.

This rate was suggested in a [public MathOverflow question][mo] before
this assessment, with positive-time counting and confinement left open.
That discussion is provenance, not a premise or proof of (6). The
argument here uses the repository's uniform arithmetic transport and
finite original-slice restart. It supplies no priority claim. The primary
import [Cardon, Theorem 1.5][cardon] was checked for the strip-decreasing
operator statement; [Dobner][dobner] is the nonnegativity source. This is
not a complete new audit of those papers.

The next task is a focused analytic review of the retained-conductor
domination and endpoint passage, followed, if accepted, by a short
corollary in the existing 01/03 manuscript chain. A new numerical family
sweep is unnecessary for this rate. Further development should lower the
certified conductor threshold, improve the comparison with an explicit
estimate, or prove a materially stronger asymptotic rate.

[floor]: ../../03_effective_outer_remainders/notes/round-2/01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md
[restart]: ../../03_effective_outer_remainders/notes/round-2/02_RESTARTED_STRIP_COMPARISON_CODEX_20261017.md
[a01]: ../../../../avoid/01_restating_the_target.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[mo]: https://mathoverflow.net/questions/515667/do-de-bruijn-newman-constants-of-dirichlet-l-functions-tend-to-0-as-the-cond
[cardon]: https://arxiv.org/html/1401.0237v2
[dobner]: https://arxiv.org/html/2005.05142v2
