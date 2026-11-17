# E15 r1 — identical horizontal counts, opposite interaction signs

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex assistance. Executor dispatched **gpt-6.1-sol / ultra**.
Independent serving model and effort metadata are unavailable.

**Proved in-note for a fixed-slice analytic-divisor class, pending
separate internal assessment.** The [four frozen pins][request] match.
The two fields in [Decision16][decision] have the same complete
horizontal counting measure and the same isolated target double.
Their normalized deflated interactions tend to \(1/2\) and \(-1/16\).
This is the scoped count-only obstruction under
[classification01][class], [premise screening02][screen], and
[scope07][scope]. See the [result index][results], [controls12][controls],
[avoid index][avoid], and [joint estimates12][joint].

## 1. Exact division and replacement

Let \(c\ge e^4\), \(\ell=1/\log c\), \(r=2\ell\), and let \(H_0\) be
the complete canonical time-zero field. Its zero occurrences have
\(|\Im\rho|\le1\), and \(H_0\) is real even entire of order at most one.
The background may contain complex zeros. [Note21 §1][divisor]

Let \(\mathcal E_c\) be the multiset of **all** zero occurrences in the
closed bands \(|\Re\rho-c|\le3\) or \(|\Re\rho+c|\le3\). The bands are
disjoint. Each is covered by six closed unit intervals in the horizontal
coordinate. The inherited unit count gives
\(\#\mathcal E_c=O(\log c)\), with an absolute constant independent of
\(c\). Conjugation and negation preserve the multiset, including the
multiplicities. [TND-O Note18 §1, (4)][shell]

Define
\[
 P_c(z)=\prod_{\rho\in\mathcal E_c}(z-\rho),\qquad
 B_c(z)=H_0(z)/P_c(z).
\]
Since the full multiplicity at each point of \(\mathcal E_c\) is
removed, every apparent pole is removable and the quotient is nonzero
at those points. Its divisor is exactly the complement of
\(\mathcal E_c\) in the divisor of \(H_0\). No background zeros on the
band edges remain. The polynomial \(P_c\) is real by conjugation and
even by grouping \(\rho,-\rho\) with equal multiplicities. Thus \(B_c\)
is real even. For fixed \(c\) and \(|z|\) sufficiently large each
\(|z-\rho|\ge1\) in the denominator, so \(|B_c(z)|\le|H_0(z)|\)
there. This preserves order at most one, as does multiplication by
either of the fixed-degree polynomials below.

Set
\[
\begin{aligned}
 F_+(z)&=B_c(z)(z^2-c^2)^2(z^2-(c+r)^2)^2,\\
 F_-(z)&=B_c(z)(z^2-c^2)^2
       \big((z-(c+r))^2+3r^2\big)\big((z+(c+r))^2+3r^2\big).
\end{aligned}
\]
Both are real even. Each inserts a double at \(c\) and at \(-c\).
At each real part \(\pm(c+r)\), \(F_+\) inserts a real double and
\(F_-\) inserts one conjugate pair of imaginary heights
\(\pm\sqrt3\,r\). These inserted groups have real parts in the erased
bands, with \(r<3\) and \(\sqrt3\,r<1\), so the complete new divisors
lie in the width-one strip. All inserted groups are distinct. The
nearest exterior group to \(c\) is at distance \(r=2\ell\) for \(F_+\)
and \(2r=4\ell\) for \(F_-\). Background points have horizontal
distance \(>3\), and the reflected insertions are at distance at least
\(2c\). Accordingly the open disk \(|z-c|<\ell\) has count two and
the common closed collar \(\ell\le |z-c|\le3\ell/2\) is zero-free.

## 2. Exact matched counts and the uniform cumulative law

Write \(\nu_0\) for the locally finite counting measure on the real
parts of all \(H_0\) zeros, with multiplicity. Projecting the two
complete divisors gives the same measure
\[
 \nu_\pm=\nu_0-\sum_{\rho\in\mathcal E_c}\delta_{\Re\rho}
        +2\big(\delta_c+\delta_{-c}+\delta_{c+r}+\delta_{-(c+r)}\big).
 \tag{1}
\]
Thus horizontal counts agree for every Borel set, with any endpoint
convention. Every closed unit count is at most the inherited
\(A\log(2+|u|)\) count plus eight, so a single absolute constant
suffices for all \(c\) and all real interval starts \(u\).

The uniform cumulative input at time zero follows from the
inherited positive-time count in
[Source-use05][source]. Use \(N_t(X)=\#\{\rho:0<\Re\rho\le X\}\)
with multiplicity, and \(g_0(X)=\frac{X}{4\pi}\log\frac{X}{4\pi}
-\frac{X}{4\pi}+\frac{11}{8}\). For each fixed \(X>4\pi\) take
\(X-\varepsilon\) and \(X+\varepsilon\) on horizontal-coordinate
lines free of time-zero zeros. There are such brackets for arbitrarily
small \(\varepsilon>0\) because the strip makes the projected divisor
locally finite. The left line \(\Re z=0\) is zero-free by the positive
cosh integral for \(H_t(iy)\). The horizontal edges at
\(\Im z=\pm2\) are zero-free by the strip. Local uniform convergence of
\(H_t\) to \(H_0\) and the argument principle stabilize each bracket's
count as \(t\downarrow0\). Apply the positive-time estimate to the two
brackets, take \(t\downarrow0\), and then squeeze \(N_0(X)\) as
\(\varepsilon\downarrow0\). The absolute error constant is independent
of \(X\) and of the brackets. In particular a zero at the cutoff
\(X\) does not have to persist on one chosen side for positive times.
This gives \(N_0(X)=g_0(X)+O(\log(2+X))\). The same bound on bounded
\(X\), including \(X=4\pi\), follows from the inherited unit count and
the continuous extension of \(g_0\) at zero.

By (1), the correction to \(N_0(X)\) is zero for \(0\le X<c-3\).
For \(X\ge c-3\) it has size at most \(\#\mathcal E_c+8=O(\log c)\),
which is \(O(\log(2+X))\) uniformly in \(c\). Hence both fields satisfy
\[
 N_\pm(X)=g_0(X)+O(\log(2+X))\qquad(X\ge0)
 \tag{2}
\]
with an absolute error constant, including cuts inside or at the
erased band. The law counts nonreal occurrences as well as real ones.
The endpoint argument uses only \(g(X,t)\to g_0(X)\) on fixed
brackets. It uses neither the positive-time coefficient in \(g\) nor
the new far-term estimate requested in E12.

## 3. Complete interaction and exact limits

At the designated double \(D=0\), [Note21 §1, (1)][divisor] gives
the unchanged sign convention
\[
 M_\pm(c)=\sum_{\rho\in Z(F_\pm)\setminus\{c,c\}}
                         (c-\rho)^{-2}.
 \tag{3}
\]
The zeros in (3) are occurrences, and precisely the two at \(c\)
are deflated. Each sum is absolutely convergent. In fact the common
background contribution has the inherited shell bound
\[
 \sum_{\rho\in Z(B_c)} |c-\rho|^{-2}
 \le 2A\sum_{h=3}^{\infty}
              \frac{\log(2+c)+\log(h+2)}{h^2}
 =O(\log c).
 \tag{4}
\]
For each integer \(h\ge3\), the shell
\(h\le |\Re\rho-c|<h+1\) fits into two closed unit intervals,
whose starts have magnitude at most \(c+h+1\). The unit count applies
to the complete \(H_0\) divisor and thus to its retained subset.
Every retained point is in one of these shells, and
\(|c-\rho|\ge |c-\Re\rho|\). This verifies (4) with an absolute
constant and includes the remote negative-height population.
Conjugation makes the background sum in (3) real. [TND-O Note18 §3,
(12)–(14)][shell]

The double at \(-c\) contributes \(1/(2c^2)\). Each of the two
occurrences at real part \(-(c+r)\) contributes in absolute value
at most \((2c+r)^{-2}\). Thus all reflected insertions cost
\(O(c^{-2})\). At positive real part \(c+r\), the two real occurrences
contribute \(2/r^2\), and the conjugate pair contributes exactly
\[
 \frac1{(r+i\sqrt3\,r)^2}+\frac1{(r-i\sqrt3\,r)^2}
   =\frac{2(r^2-3r^2)}{(r^2+3r^2)^2}=-\frac1{4r^2}.
\]
The complete sums therefore satisfy
\[
 \boxed{
 \ell^2 M_+(c)=\frac12+O((\log c)^{-1}),\qquad
 \ell^2 M_-(c)=-\frac1{16}+O((\log c)^{-1}).
 }\tag{5}
\]
The constants are uniform in \(c\). Their signs are opposite for all
sufficiently large \(c\), with unevaluated onset. For the sharp cut
of [Decision15][tail-decision], any \(r\le R\le3\) includes just the
two exterior occurrences at \(c+r\) in the nearby sum. Consequently
\(\ell^2S_R\) equals \(1/2\) or \(-1/16\) exactly, even though the
horizontal projection agrees outside the cut as well.

## 4. Scope, control screen, and direct comparison

In the fixed-slice class consisting of the real even entire fields
with the displayed order, strip, count, and collar data, those data
cannot imply a nonnegative near-field sign or an \(o(1)\) upper
allowance for the negative part of \(\ell^2S_R\). Equation (5) also
rules out recovery of the sign of the full normalized interaction
from those data. The decisive difference is the exterior transverse
mark. For both fields the unchanged theta identity fails along any
unbounded choice of \(c\) with \(H_0(c)\ne0\): the inserted zero
\(F_\pm(c)=0\) cannot come from multiplication of \(H_0\) by a
nonzero normalization. Such \(c\) are available because the real
zeros are discrete. The construction proves (1)–(5) for all large
\(c\), whether or not \(H_0(c)=0\). Positive Fourier-source
representation and a common physical heat-time tube are unpaid
premises. The count-only obstruction leaves source-sensitive or
time-correlated near estimates open. Decision15's canonical far-tail
estimate concerns a different part of the sum.

The inherited classifications in [Decision15's control replay][tail-controls]
and [Note21 §6][divisor] are retained. Quadratic and even quartic
examples and the fixed-event finite-atom or compact finite-profile
classes lack the canonical \(X\log X\) cumulative main term. The
documented nonzero quadratic-exponential and reflected super-Gaussian
classes fail order at most one. The endpoint-defective weighted-square,
finite-source, finite-score, and finite-prime classes fail the finite
strip at their stated scope. The modified Euler-factor counts fail the
canonical time-zero discrepancy, including when width one survives.
The damped smooth-shape and positive-primitive controls retain their
untested strip and count premises, and the RH-conditional merger
retains its RH hypothesis and untested exact cumulative law. The varied
observations and fractional-profile relaxation respectively lack the
literal field equation and integer divisor. E15's own examples pay the
projected count more strongly through exact equality, with the
source and time-domain limitations above.

The direct deflated-jet evaluator receives the same inputs. At the
double let \(A_\pm=F_\pm/(z-c)^2\), nonzero on the counted collar
disk. Direct differentiation yields
\[
 -(\log A_\pm)''(c)
 =\left(\frac{F_\pm'''(c)}{3F_\pm''(c)}\right)^2
   -\frac{F_\pm''''(c)}{6F_\pm''(c)}
 =M_\pm(c).
\]
With the full fields or these jets it distinguishes the two signs.
With only their shared count and collar information it faces the same
counterexample. This comparison uses no transport advantage or incoming
gap claim.

[request]: ../research-progress/handoffs/VCD-GT-E15-r1.md
[decision]: ../brainstorm/notes/16_VCD_GT_B08_IDENTICAL_COUNT_SCOPE_DECISION_20261117.md
[tail-decision]: ../brainstorm/notes/15_VCD_GT_B07_NEAR_FAR_COUNT_DECISION_20261117.md#frozen-target-and-useful-rate
[tail-controls]: ../brainstorm/notes/15_VCD_GT_B07_NEAR_FAR_COUNT_DECISION_20261117.md#control-premise-replay-before-execution
[divisor]: 21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md
[source]: ../references/05_VCD_GT_UNIFORM_COUNT_SOURCE_USE_20261117.md
[shell]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[class]: ../../../../../avoid/01_restating_the_target.md
[screen]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
