# Horizontal wall acquisition and the remaining endpoint count

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**. HCB chat0001, same thread `01a17aca-de9a-7533-9bb8-8ee0e9bdb282`.

**Status: proved in-note under RH from the named classical inputs, with
separate-agent same-model internal review; no specialist validation.**
For the unchanged family of [Note03][n03], both horizontal sides now have
an asymptotic lower bound throughout the entire time interval. The full
wall and exact integer count remain unacquired. No finite-height
certificate or favorable Poisson second moment is claimed. No priority
claim is made for the classical kernel or heat identities; the gain is
their quantified application on the frozen consumer domain.

This is a bounded acquisition estimate under [avoid01][a01], judged by
its exponent and domain, not an RH-equivalent simplicity criterion.
Read the [result index][results], [collision controls][controls] and
[avoid index][avoid], particularly [scope][a07] and [unchecked
imports][a16]. Checked primary passages, versions and external reading
copies are recorded in the [reference catalog][refs]; [Review03][review]
states the actual review scope. No research numerical or machine-symbolic
experiment or certificate replay was executed.

## 1. Family and return

Keep, without moving the wall,
\[
 X=4\pi e^m,\quad L=m\ge16,\quad u=L(z-X),\quad\tau=tL^2,
 \quad \tau_X=X^{-1/4},\quad y=\sqrt{\tau_X},
\]
\[
 \Gamma=\partial([-4,4]+i[-2,2]),\quad
 \mathcal B=[-6,6]+i[-3,3],\quad
 h_X(\tau,u)=H(\tau/L^2,X+u/L)/A_X,
 \tag{1}
\]
where \(A_X=A_o(0,X)>0\) is frozen. Use exactly Note03's completed
holomorphic arithmetic model \(f_X\) and declared buffer allowance
\(e_{\rm src}=C_0B_XX^{-3/4}\), with positive fixed \(C_0\),
\(1\le B_X=O(1)\). Its constants and onset remain uninstantiated.
RH supplies real zeros for the canonical field at every nonnegative
time; it supplies no endpoint nonvanishing assumption.

**Proposition 1 (horizontal acquisition).** Under RH, for every
\(\epsilon>0\) and all sufficiently large integers \(m\),
\[
 \inf_{\substack{0\le\tau\le\tau_X\\ |\Re u|\le4,
                         \,|\Im u|=2}}|h_X(\tau,u)|
 \ge X^{-1/2-\epsilon}. \tag{2}
\]
The same conclusion, with an arbitrarily slightly larger exponent loss,
holds for \(f_X\). Equivalently both have the lower bound
\(X^{-1/2-o(1)}\) on these two sides, uniformly in real time.
This is not a certificate for every \(m\ge16\).

**Proposition 2 (exact remaining geometry).** At every time in (1),
\[
 \inf_{u\in\Gamma}|h_X(\tau,u)|
 =\min\left\{
 \inf_{|c|\le4}|h_X(\tau,c+2i)|,
 |h_X(\tau,-4)|,|h_X(\tau,4)|\right\}. \tag{3}
\]
Thus whole-interval real endpoint floors, plus an exact initial count,
remain the full-wall acquisition problem. Equations (2)–(3) do not
evaluate those real endpoint values.

## 2. A shrinking-offset initial modulus estimate

Write \(T=X/2\). At the bottom horizontal edge the zeta coordinate is
\(s=1/2+a+iq\), where \(a=1/L\) and
\(q=T+c/(2L)\), \(|c|\le4\). Completion and conjugation give the
same modulus on the upper edge. Set
\[
 K_a(v)=\tfrac12\log\frac{4+v^2}{a^2+v^2}.
\]
Direct integration and monotonicity on each half-axis give
\[
 K_a(0)=\log(2/a),\quad
 \int_{\mathbb R}K_a=\pi(2-a),\quad
 \operatorname{TV}(K_a)=2\log(2/a). \tag{4}
\]
The RH Hadamard product, compared between real parts \(1/2+a\) and
\(5/2\), and Stirling's formula give
\[
 \log|\zeta(1/2+a+iq)|
 =\frac{2-a}{2}\log\frac q{2\pi}
       -\sum_\gamma K_a(q-\gamma)+O(1). \tag{5}
\]
All positive and negative ordinates occur with multiplicity. This is
the elementary identity underlying [Carneiro–Chandee, §2, (2.1)][CC].
Its derivation is uniform for \(0<a\le1\): the gamma parameters stay
in a fixed compact interval of real parts, the anchor
\(|\zeta(5/2+iq)|\) is bounded above and below, and the product ratio
is exact. We use this uniform identity, rather than substituting
\(a=1/L\) into an estimate whose constants depend on fixed \(a\).

For positive ordinates write the Riemann–von Mangoldt formula as
\(N(v)=M(v)+S(v)+R(v)\), with
\(M'(v)=(2\pi)^{-1}\log(v/(2\pi))\) and \(R(v)=O(1/v)\).
For Stieltjes integrals, take \(N\) right continuous and use the
matching right limit of \(S\) at an ordinate. The bound below extends
to those limits; endpoint count formulas later assume nonzero endpoints
and are independent of this convention.
Negative ordinates and positive ordinates outside \([q/2,3q/2]\)
contribute \(O(\log q/q)\) to the sum in (5). Indeed
\(K_a(w)\ll(1+w^2)^{-1}\) for \(|w|\ge1\), uniformly in \(a\le1\),
and the usual count bound is \(N(v)=O(v\log(v+3))\).

On the central interval,
\[
 \int_{q/2}^{3q/2}K_a(q-v)\,dM(v)
 =\frac{2-a}{2}\log\frac q{2\pi}+O(\log q/q). \tag{6}
\]
To see the uniform error, use
\(|M'(v)-M'(q)|\ll |v-q|/q\) and
\(\int_0^{q/2}wK_a(w)\,dw\ll\log q\), then use the mass in (4)
to extend the constant-density integral to the whole line. The main
term in (6) cancels the first term of (5).

Integration by parts, including the two central-interval boundary
terms, gives
\[
 \left|\int_{q/2}^{3q/2}K_a(q-v)\,dS(v)\right|
 \le 2\log(2/a)\sup_{q/2\le v\le3q/2}|S(v)|. \tag{7}
\]
The boundary terms and the interior variation together have coefficient
exactly \(2K_a(0)\); they are not dropped. The \(R\)-payment is
\(O(\log(2/a)/q)\).

[Carneiro–Chandee–Milinovich, Theorem 2][CCM] proves under RH
\[
 |S(v)|\le\frac14\frac{\log v}{\log\log v}
 +O\!\left(\frac{\log v\,\log\log\log v}
                       {(\log\log v)^2}\right). \tag{8}
\]
Since \(a=1/L\) and \(\log q=L+O(1)\), (5)–(8) imply uniformly
\[
 \log|\zeta(1/2+1/L+iq)|\ge-(1/2+o(1))\log q. \tag{9}
\]
The explicit gamma/polynomial completion factor divided by \(A_X\)
has modulus bounded above and below by positive constants on these
microscopic edges. Therefore
\[
 \inf_{|c|\le4}|h_X(0,c\pm2i)|\ge X^{-1/2-o(1)}. \tag{10}
\]
No source cancellation has been replaced by a positive arithmetic
diagonal, and multiplicities have not been excluded in this argument.

## 3. Relative heat comparison throughout the interval

This step uses a shrinking-offset proof; an inherited fixed physical
offset theorem alone would not justify it. Under RH the initial field
has the even canonical product
\[
 H(0,z)=H(0,0)\prod_{\rho>0}(1-z^2/\rho^2),
 \qquad \rho=2\gamma. \tag{11}
\]
The factors include multiplicities. The field is even of order one,
so no quadratic exponential factor occurs. The Riemann–von Mangoldt
formula supplies the unit-interval upper count
\(\#\{\rho\in[Y,Y+1]\}\ll\log(Y+3)\).

Pair the positive and negative roots before summing. For
\(z=X+u/L\), \(|\Re u|\le4\), \(1\le|\Im u|\le3\),
\[
 \partial_u\log h_X(0,u)=\frac1L\sum_{\rho>0}
       \left(\frac1{z-\rho}+\frac1{z+\rho}\right)=O(L). \tag{12}
\]
Here roots below \(X/2\) contribute \(O(L)\) before the prefactor,
as do roots above \(2X\), by the paired bounds \(O(1/X)\) and
\(O(X/\rho^2)\). Roots in \([X/2,2X]\) in the nearest physical
unit interval contribute \(O(L^2)\); the other intervals contribute
\(O(L\sum_{j\le2X}j^{-1})=O(L^2)\). This proves (12) with constants
independent of \(m\), without a gap assumption.

For real \(|c|\le4\), put \(x=X+c/L\). For \(b>0\), the same product gives
\[
 \partial_b\log|h_X(0,c+ib)|
 =\frac1L\sum_{r=\pm\rho}
       \frac{b/L}{(x-r)^2+(b/L)^2}>0. \tag{13}
\]
Unit-interval grouping of this positive sum yields, for \(b\ge1\),
\[
 \partial_b\log|h_X(0,c+ib)|
 \ll\log(X+b/L+3)(L^{-1}+b^{-1})
 \ll L+\log(2+b). \tag{14}
\]
For example, separate distances up to \(b/L+1\) from the farther
dyadic ranges; use the unit count in the former and the quadratic
Poisson denominator in the latter. The logarithmic growth in height
is summable in the outer ranges. This justifies (14) even for the
unbounded imaginary shifts used next.

Take \(u=c+2i\) and real \(v\). If \(B=|2+v|\le2\), (13) and
conjugation give \(|h_X(0,u+iv)/h_X(0,u)|\le1\). If \(B>2\),
integrate (14) from 2 to \(B\), noting \(B-2\le|v|\). In both cases
\[
 \left|\frac{h_X(0,u+iv)}{h_X(0,u)}\right|
 \le\exp\{C|v|[L+\log(4+|v|)]\}. \tag{15}
\]
This uses modulus monotonicity when the shift crosses the real axis;
it never takes an analytic logarithm across possible real zeros.
For \(|v|\le1\), (12) does give a local analytic logarithm, hence
\[
 \left|\frac{h_X(0,u+iv)}{h_X(0,u)}-1\right|
 \le e^{CL|v|}-1. \tag{16}
\]

The complete source and Gaussian moment-generating identity give exactly
\[
 h_X(\tau,u)=\frac1{\sqrt{4\pi\tau}}
      \int_{\mathbb R}e^{-v^2/(4\tau)}h_X(0,u+iv)\,dv.
 \tag{17}
\]
Absolute interchange follows from the theta source's decay faster than
every Gaussian. Its normalization has variance \(2\tau\), consistent
with \(\partial_\tau h_X=-\partial_u^2h_X\).
Integrating (16) over \(|v|\le1\) costs
\(O(L\sqrt\tau)e^{O(L^2\tau)}\).
For \(|v|>1\), use (15) and
\(|v|[L+\log(4+|v|)]\ll(L+1)v^2\). Since \(\tau_XL\to0\),
the Gaussian absorbs this entire tail for all sufficiently large \(X\),
giving \(O(e^{-c_0/\tau})\). Thus
\[
 \sup_{\substack{0\le\tau\le\tau_X\\|c|\le4}}
 \left|\frac{h_X(\tau,c\pm2i)}{h_X(0,c\pm2i)}-1\right|
 =O(L\sqrt{\tau_X})=o(1). \tag{18}
\]
Together with (10), this proves Proposition1. Subtracting the complete
buffer allowance \(e_{\rm src}=O(X^{-3/4})\) transfers this horizontal
floor to \(f_X\). Evaluation error must be paid separately in a finite
implementation. No source error has been refined by increasing bits.

## 4. Real endpoint reduction and exact count formula

At each nonnegative time, RH and real-zero preservation give an even
real-zero product for \(H(t,\cdot)\). The source gives the growth bound
\(\log\max_{|z|\le r}|H(t,z)|=O(r\log(r+3)+t\log^2(r+3))\)
on bounded nonnegative time intervals, by its double-exponential tail.
Thus its order is at most one; positivity of \(H(t,0)\) rules
out a zero there. Applying (13)'s positivity at that time shows that
each vertical side has minimum modulus at its real midpoint. This
proves Proposition2. For the arithmetic model we only infer
\(\inf_\Gamma|f_X|\ge\inf_\Gamma|h_X|-e_{\rm src}\); its own zeros
need not be real.

There is an exact initial endpoint identity. For real \(u\), put
\(q=X/2+u/(2L)\). With the [DLMF Hardy-Z convention][DLMF],
\[
 h_X(0,u)=-C_X(u)Z(q),\quad
 C_X(u)=(q^2+\tfrac14)\pi^{-1/2}
     |\Gamma(\tfrac14+iq/2)|X^{-7/4}e^{\pi X/8}>0,
 \tag{19}
\]
\[
 C_X(u)=\tfrac12 e^{-\pi u/(8L)}
             (1+O((LX)^{-1})),\qquad |u|\le4. \tag{20}
\]
This follows directly from \(H(0,z)=\xi((1+iz)/2)/8\), since
\(s(s-1)=-(q^2+1/4)\), and Stirling's formula. In particular the
two prescribed values \(Z(T\pm2/L)\), and their time-evolved
endpoint counterparts, are actual missing data. Positivity off the
critical line does not prevent a zero at one of these real crossings.

If both endpoints are nonzeros and remain so in the interval, the count
is constant and its initial value is exactly
\[
 n_m=N(T+2/L)-N(T-2/L). \tag{21}
\]
The argument principle with the continuously unwrapped theta phase gives
\[
 n_m=\frac{\vartheta(T+2/L)-\vartheta(T-2/L)}\pi
                  +S(T+2/L)-S(T-2/L), \tag{22}
\]
and the gamma expansion gives
\[
 \Delta\vartheta/\pi=2/\pi+O((LT^2)^{-1}). \tag{23}
\]
The zeta-ordinate interval has length \(4/L\), not \(8/L\).
[Goldston–Gonek, Theorem1][GG], or twice (8), yields only
\[
 0\le n_m\le2/\pi+(1/2+o(1))L/\log L. \tag{24}
\]
Its ambiguity grows; it cannot isolate an integer. Real endpoint signs
would determine only its parity, because the count includes even
multiplicities. No fixed population such as two has been acquired.
Neither (19) nor the cited RH estimates prove that the prescribed
endpoints are nonzeros. No claim is made that acquisition at this
particular sequence is impossible.

## 5. Consequences for the specified coefficient fallback

The horizontal relative error bound supplied here is at most
\(X^{-1/4+o(1)}\). Note03's fixed-rank sufficient target is
\(o(X^{-(2n+1)/16})\). This estimate leaves room for \(n=1\), but
does not justify the \(n=2\) target \(o(X^{-5/16})\). It does not
prove that the true horizontal floor or actual source error is that
unfavorable. More cancellation or a sharper integrated consumer could
do better. J's unknown real joint-jet lower bound is not supplied by
this off-axis estimate.

There is also a necessary limitation of **Note03's particular binomial
fallback test**, with its retained declared allowance. Retain its
\(R=\sqrt{20}\), \(\kappa=12/(\pi\sqrt{20})\), \(\mu=1/24\),
\(a=\kappa[-\log(1-\eta)]\), \(\eta=e_{\rm src}/m_X\).
Its nonnegative majorant satisfies \(C_n(a)\ge a\), even when
quadrature/encoding radii vanish. Therefore \(d_0\ge R^na\), and
the second test in Note03(11) forces
\[
 a\le K_n y^{n+1/2},\quad
 K_n=\frac{\pi\mu}
 {2nR^n\sqrt{20\pi}
 (\sqrt{n+2/3+\mu}+\sqrt{n+2/3})}. \tag{25}
\]
This uses its exact rationalized
\(E_*={\mu}/[\sqrt{20\pi y}
(\sqrt{n+2/3+\mu}+\sqrt{n+2/3})]\).
Since \(a\ge\kappa\eta\), any accepted floor must obey
\[
 m_X\ge(\kappa/K_n)e_{\rm src}y^{-n-1/2}. \tag{26}
\]
For all \(n\ge6\), \(K_n\le K_6\) and \(y^{-n-1/2}\ge X^{13/16}\).
The *declared allowance* \(e_{\rm src}\ge C_0X^{-3/4}\) then
forces \(m_X\ge cX^{1/16}\).

But [Chandee–Soundararajan, Theorem1.1][CS] gives under RH
\(|Z(T+2/L)|\le X^{o(1)}\). Equations (19)–(20) and the source
comparison imply
\[
 m_X\le |f_X(0,4)|\le X^{o(1)}, \tag{27}
\]
contradicting (26) for sufficiently large \(m\). Thus this specified
binomial fallback cannot accept a population of six or more at large
height. This is an exact consequence of its finite acceptance test,
not an inference that a sufficient little-o rate is universally
necessary. The lower bound on the *allowance* is never a lower bound
on the actual approximation error. The result excludes neither
canonical walls nor sharper source bounds, coefficient-sensitive
majorants, integrated transfer, or different clocks. It does not prove
that the actual population is at most five.

## 6. Controls and next dependency

The product/heat comparison uses all-real initial zeros with the
canonical count and growth estimates. Polynomial Hermite/double
controls satisfy the relevant product/heat reasoning and can still
have endpoint collisions; (2) excludes no such event. Euler-factor
controls with extra nonreal zeros need not meet RH's all-real premise,
and every altered control fails the unchanged canonical source premise
used in (5), (8), (19) and the named zeta estimates. Weighted-square,
finite-tail, reflected, positive-primitive, finite-prime/profile and
RH-conditional theta-close controls retain exactly the qualifications
listed in [control cluster12][controls]; no generic inequality here
rejects an admissible colliding control merely by its name. At an
actual real endpoint zero the remaining vertical floor is zero, as it
must be. No control certificate was rerun.

**HCB-02 remains Partial, with a new actual horizontal acquisition.**
The next missing estimate is
\(\inf_{0\le\tau\le\tau_X}|h_X(\tau,\pm4)|\), quantitatively
strong enough after source subtraction, plus the exact integer in
(21). A simple replacement by a free two-arm model or a rounded
average count would not acquire these inputs. For \(n\ge6\), the
specified fallback itself must be changed before seeking its floor.

The frozen family has not been replaced or sampled. No finite numerical
cases/tolerances/resource caps have been selected, and no campaign
has begun. Future finite execution must first instantiate all source
constants, the endpoint/argument protocol and continuous time bounds,
coefficient and integral tolerances, same-source J/direct comparator,
and explicit failure/resource stop rules. The [sole register][progress]
tracks these dependencies and preserves the original HDA/HDC/RT owners.

[n03]: 03_MICROSCOPIC_WALL_PAYMENT_AND_POISSON_BUDGET_20261026.md
[review]: ../reviews/03_HORIZONTAL_WALL_AND_COUNT_INTERNAL_REVIEW_20261026.md
[refs]: ../references/01_MICROSCOPIC_WALL_PRIMARY_SOURCES_20261026.md
[progress]: ../research-progress/01_COLLISION_BOUNDS_RESEARCH_PROGRESS_20261026.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a16]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[CC]: https://arxiv.org/pdf/1008.4970v1
[CCM]: https://arxiv.org/pdf/1309.1526v1
[GG]: https://arxiv.org/pdf/math/0511092v1
[CS]: https://arxiv.org/pdf/0908.2008v1
[DLMF]: https://dlmf.nist.gov/25.10
