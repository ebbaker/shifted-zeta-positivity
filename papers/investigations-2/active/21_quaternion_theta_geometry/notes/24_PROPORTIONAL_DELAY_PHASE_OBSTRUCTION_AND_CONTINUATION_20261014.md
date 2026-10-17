# Proportional Gaussian delay and its stationary phase obstruction

> **Chat-history routing update, 17 October 2026.** Current histories: [Chat 13 — Continue quaternion theta geometry](../chat-histories/0013_2026-10-15T00-47-29Z_continue-quaternion-theta-geometry.json), [Chat 12 — Continue quaternion theta rewrite](../chat-histories/0012_2026-10-14T23-49-23Z_continue-quaternion-theta-rewrite.json). Use this investigation’s [local registry](../chat-histories/index.json) and [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json) for current numbers and preserved provenance; this supersedes the routing and numbering below. All future investigation 21 chats belong in this investigation’s `chat-histories/` folder.

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model: **gpt-6.1-sol**, reasoning effort **ultra**, verified
from the current session metadata. Parallel analytic derivations and an
independent internal review support this continuation of
[Note 23](23_MANUSCRIPT_INTEGRATION_AND_CROSS_TIME_CONTINUATION_20261014.md).
This is research analysis, not external peer review or formal verification.

**Result.** The predetermined rule \(\delta=t/2\) has an exact paid
complete-source representation and a bounded pilot on both current
stationary branches. However, it cannot satisfy the required retained
sign at all heights. For every fixed positive time, both genuine stationary
sets contain arbitrarily high points with
\(h_j(t,x)C_j(t/2,x)<0\). More generally every fixed proportional delay
\(\delta=\rho t\), \(0<\rho<1\), has this obstruction. The full Laguerre
forms and the absorption product are positive at these high counterexample
points. This rejects that particular global retained-sign condition; it
neither rejects the locally bounded-loss program nor settles the unknown
small-time region.

## 1. Protocol and exact identities

The protocol was declared before evaluating the new pilot:

\[
 \delta=t/2,\quad \lambda=1/2,\quad a=\pi/16,\quad b=1/4,
 \quad\mu=a^2+b^2,\quad K_0=K_1=0.
\]

Write \(h_k=\partial_x^kH\), \(E=h_0^2+h_1^2\), and, with the same
frozen centering at every time,

\[
 C_k=-h_{k+2}-2ah_{k+1}-\mu h_k,
 \qquad\mathcal L_j=h_{j+1}^2-h_jh_{j+2},\quad j=0,1.
\]

The noncompact complex Gaussian multiplier \(e^{-tz^2/2}\) gives

\[
 G_j=C_j(t/2,x),\quad R_j=C_j(t,x)-G_j,
 \quad P_j=h_jG_j,\quad Q_j=h_j(C_j-G_j/2).
 \tag{1}
\]

Only **current** stationarity \(h_{j+1}(t,x)=0\) is imposed. Then

\[
 \mathcal L_j=\mu h_j^2+\tfrac12P_j+Q_j.                 \tag{2}
\]

The heat equation \(\partial_tC_k=-C_{k+2}\) gives the signed identity

\[
 R_j=-\int_0^{t/2}C_{j+2}(t-s,x)\,ds,\qquad
 Q_j=\tfrac12P_j-
       \int_0^{t/2}h_j(t,x)C_{j+2}(t-s,x)\,ds.           \tag{3}
\]

The delayed point is generally not stationary. Formula (3) retains that
cross-time product rather than replacing it by an earlier stationary one.
At \(t=0\), the rule has zero delay and \(G=C\); all identities remain
well defined. No claim of a proper attenuation at zero delay is needed.

## 2. Complete source, independent coordinates, and all payments

Use the complete theta source of [Note 12](12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md):

\[
 \phi_n(z)=(2\pi^2n^4e^{9z}-3\pi n^2e^{5z})e^{-\pi n^2e^{4z}},
 \qquad\Phi(z)=\sum_{n\ge1}\phi_n(z).
\]

Let \(\Omega=[0,\infty)\times\mathbb N\), with integration in the first
coordinate and counting measure in the second. For \(\alpha=(u,n)\), set

\[
 z_\alpha=u+ia,\quad q_\alpha=iz_\alpha=-a+iu,
 \quad D_\alpha=u^2-b^2,
 \quad W_\alpha=e^{tz_\alpha^2+ixu}\phi_n(z_\alpha).
\]

For a possibly complex multiplier \(k\), define

\[
 F_j(k)=e^{-ax}\Re\int_\Omega W_\alpha q_\alpha^jk_\alpha\,d\nu(\alpha).
\]

Then \(h_j=F_j(1)\), \(C_j=F_j(D)\), and (1) uses

\[
 k^P_\alpha=D_\alpha e^{-tz_\alpha^2/2},\qquad
 k^Q_\alpha=D_\alpha(1-\tfrac12e^{-tz_\alpha^2/2}).
\]

The exact signed polarization for either product is

\[
\boxed{\begin{aligned}
 h_jF_j(k)=\frac{e^{-2ax}}4\Re\iint_{\Omega^2}\big[&
 (k_\alpha+\overline{k_\beta})W_\alpha\overline{W_\beta}
       (q_\alpha\overline{q_\beta})^j\\
 &+(k_\alpha+k_\beta)W_\alpha W_\beta(q_\alpha q_\beta)^j
 \big]d\nu(\alpha)d\nu(\beta).
\end{aligned}}                                                     \tag{4}
\]

Indeed \(\Re A\Re B=\frac12\Re(A\overline B+AB)\); averaging under
coordinate exchange gives (4). The two integration coordinates and the
two arithmetic indices are independent. Both Hermitian and bilinear
terms are required. In particular, the Hermitian term conjugates the
second complex multiplier. Substituting a real multiplier identity here
without that conjugation changes the observation.

The contour identity is established for the complete source before
truncation. On \(z=iy\), the physical jet factors, \(\Phi(iy)\),
\(e^{-tz^2/2}\), and the residual polynomial
\((z-ia)^2-b^2\) are all real; the vertical differential is imaginary.
The left segment therefore has zero real contribution. The complete
source decays doubly exponentially on the right vertical segment, so its
contribution tends to zero. This does not assert evenness of an individual
raw theta term or discard a finite-source contour correction.

Here convergence and tails can be paid explicitly. Put
\(c=\cos(4a)=\cos(\pi/4)\), \(\rho_0=16e^{-3\pi c}<1\). For
\(0\le t\le1/2\), the index-ratio estimate gives

\[
 \sum_{n\ge1}|W_{(u,n)}||q_{(u,n)}|^k
 \le\frac{2\pi^2+3\pi}{1-\rho_0}(u+a)^k
       e^{u^2/2+9u-\pi c e^{4u}}.                            \tag{5}
\]

Every polynomial moment is integrable. Thus the products in (4), their
parameter derivatives used below, and the time integral in (3) converge
absolutely; Fubini and conjugation are justified.

For any retained set \(A\subset\Omega\), let

\[
 M_{A,k}=\int_A|W||q|^k\,d\nu,\qquad
 T_k=\int_{\Omega\setminus A}|W||q|^k\,d\nu.
\]

Since \(|e^{-tz^2/2}|\le M:=e^{a^2/4}\), the retained and omitted
multiplier masses satisfy, for \(X=A\) or \(\Omega\setminus A\),

\[
 B_X^P\le M(M_{X,j+2}+b^2M_{X,j}),\qquad
 B_X^Q\le(1+M/2)(M_{X,j+2}+b^2M_{X,j}),                    \tag{6}
\]

where \(M_{\Omega\setminus A,k}=T_k\). The inequalities use
\(|u^2-b^2|\le u^2+b^2\le|q|^2+b^2\).
If both product factors are truncated to \(A\), their error is at most

\[
 e^{-2ax}\{M_{A,j}B_{\Omega\setminus A}
                  +T_jB_A+T_jB_{\Omega\setminus A}\}.       \tag{7}
\]

The three terms pay retained–omitted, omitted–retained, and
omitted–omitted sectors. For the standard retained rectangle \(A=[0,U]\times\{1,\ldots,N\}\),
Note 12's full-index and full-integration bounds supply the \(T_k\),
using their stated hypotheses and overpaying the intersection of the
two omitted regions. The same upper payment works if \(A\) contains
that rectangle; other sets require their own tail bounds. No pair sector is discarded. Quadrature and Taylor
errors are additional. Alternatively use \(W_t e^{-tz^2/2}=W_{t/2}\)
and directly pay the complete earlier-time field, as the pilot does.

For computed physical values \(\widetilde h,\widetilde G,\widetilde B\)
with errors \(e_h,e_G,e_B\), the corresponding final product payments are

\[
 |hG-\widetilde h\widetilde G|
 \le e_h|\widetilde G|+e_G|\widetilde h|+e_he_G,
\]

and the same formula with \(G\) replaced by \(B=C-G/2\), with
\(e_B\le e_C+e_G/2\). This includes the error–error cross term and
requires no energy denominator.

## 3. Moving delay and genuine stationary transport

The rule moves with time. Its correct derivatives are

\[
 \partial_tG_j=-\tfrac12C_{j+2}(t/2,x),\qquad
 \partial_xG_j=C_{j+1}(t/2,x),\qquad
 (\partial_t+\partial_x^2)G_j=\tfrac12C_{j+2}(t/2,x).        \tag{8}
\]

Thus \(G\) does not satisfy the same time equation as a fixed-delay
observation. No derivative of the contour parameter or centering occurs
in this protocol because \(a,b\) are fixed.

On a regular **current** branch \(x=\xi(t)\) with
\(h_{j+1}=0\), \(h_{j+2}\ne0\), implicit differentiation gives

\[
 \xi'=h_{j+3}/h_{j+2},\qquad \frac{d}{dt}h_j(t,\xi(t))=-h_{j+2}.
\]

Writing superscript minus for evaluation at \((t/2,\xi(t))\),

\[
 \frac{dP_j}{dt}=-h_{j+2}G_j
       +h_j(-\tfrac12C_{j+2}^-+\xi'C_{j+1}^-),             \tag{9}
\]

\[
 \frac{dQ_j}{dt}=-h_{j+2}B_j+h_j\left[-C_{j+2}+\xi'C_{j+1}
          +\tfrac14C_{j+2}^- -\tfrac12\xi'C_{j+1}^-\right]. \tag{10}
\]

These formulas are only for regular branches; they do not divide by
\(h_{j+2}\) at branch creation. A different \(x\)-dependent delay or
moving centering would add its chain-rule terms. Pointwise formulas do
not authorize treating those parameters as frozen during transport.

## 4. Theta-specific obstruction for every fixed proportional delay

**Theorem.** Fix \(t_0\in(0,1/2]\), \(0<\rho<1\), and fixed finite real
centering parameters \(a,b\). Set \(\tau=(1-\rho)t_0>0\) and
\(\delta=\rho t_0\). For each \(j=0,1\), there are sequences
\(x_n\to\infty\) of genuine current stationary points
\(h_{j+1}(t_0,x_n)=0\) with

\[
 h_j(t_0,x_n)C_j(\tau,x_n)<0.                              \tag{11}
\]

There are also such sequences with the opposite strict sign. On every
sufficiently high current stationary point, for every fixed
\(\lambda\in[0,1]\),

\[
 h_j(t_0,x)\{C_j(t_0,x)-(1-\lambda)C_j(\tau,x)\}>0.        \tag{12}
\]

Both full Laguerre forms are positive at all sufficiently high points.
In particular, no choice of the loss in the absorption inequality repairs
the failed exact retained condition (11).

**Proof.** Use the analytic carrier already established in
[Notes 17](17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md)
and [19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md).
Put \(s=(1+ix)/2\), \(L=\log(x/(4\pi))\), \(\omega=L/4\), and

\[
 \alpha(s)=\frac1{2s}+\frac1{s-1}+\frac12\operatorname{Log}\frac{s}{2\pi},
 \quad Q_v=M_0(s)e^{v\alpha(s)^2/4}\zeta(s+v\alpha(s)/2),
 \quad A_v=2|Q_v|.
\]

For each of the fixed positive times \(v=t_0,\tau\), the earlier theorem
applies for all sufficiently large \(x\) and gives the four **physical**
jets

\[
 h_k(v,x)=A_v\omega^k
       \{\cos(\phi_v+k\pi/2)+O_{t_0,\rho}(L^{-1})\},
 \quad k=0,1,2,3,\qquad \phi_v=\arg Q_v.                   \tag{13}
\]

Continuous phases exist there and \(\phi_{t_0}'=\omega+O(1)>0\).
There is no derivative of the approximate arithmetic cutoff in (13).
The exact carrier quotient is

\[
 \frac{Q_{t_0}}{Q_\tau}
 =e^{\delta\alpha(s)^2/4}
   \frac{\zeta(s+t_0\alpha(s)/2)}{\zeta(s+\tau\alpha(s)/2)}.
\]

As \(x\to\infty\),
\(\alpha(s)=L/2+i\pi/4+O(1/x)\), while the two zeta arguments have
real parts \(1/2+vL/4+O(1/x)\to\infty\). Their Dirichlet series
therefore tend to 1, with logarithms tending to zero. Choosing continuous
phases consistently gives

\[
 D:=\phi_{t_0}-\phi_\tau=\frac{\delta\pi L}{16}+o(1),
 \qquad r:=\frac{A_\tau}{A_{t_0}}
 =\exp\{-\delta L^2/16+\delta\pi^2/64+o(1)\}.             \tag{14}
\]

At a current stationary point set \(\psi=\phi_{t_0}+j\pi/2\).
Equation (13) gives \(\sin\psi=O(1/L)\), and therefore
\(\cos\psi=\pm(1+O(L^{-2}))\). The earlier point is not assumed
stationary. The leading term of its residual is

\[
 C_j(\tau,x)=A_\tau\omega^{j+2}
                 \{\cos(\psi-D)+O(1/L)\};
\]

the fixed \(2a\) and \(\mu\) terms are lower order. Consequently,

\[
 \frac{h_j(t_0,x)C_j(\tau,x)}
      {A_{t_0}A_\tau\omega^{2j+2}}
       =\cos D+O(1/L),                                  \tag{15}
\]

\[
 \frac{h_j(t_0,x)C_j(t_0,x)}{A_{t_0}^2\omega^{2j+2}}
       =1+O(1/L).                                       \tag{16}
\]

The small amplitude \(A_\tau\) does not change the sign in (15).
For (12), the normalized expression is
\(1+O(1/L)-(1-\lambda)r\{\cos D+O(1/L)\}\to1\).

It remains to populate the signs with actual stationary points.
For each sufficiently large integer \(k\), consider
\(|\psi-k\pi|\le\pi/6\). The two endpoint signs of
\(h_{j+1}/(A_{t_0}\omega^{j+1})=-\sin\psi+O(1/L)\) are opposite.
Throughout this window,
\(h_{j+2}/(A_{t_0}\omega^{j+2})=-\cos\psi+O(1/L)\) has one strict
sign. Thus precisely one current stationary point occurs in each window,
and \(h_j\ne0\) there. Only jets through order 3 are needed for both
values of \(j\).

Now take logarithmic bands

\[
 \left|L-\frac{16(2n+1)}\delta\right|\le\frac8{3\delta}. \tag{17}
\]

The leading phase in (14) lies within \(\pi/6\) of \((2n+1)\pi\).
For all large \(n\), \(\cos D\le-1/2\) throughout the band. Each
band contains whole phase windows of both types: its length in \(x\)
grows exponentially, and \(\psi'\sim L/4\). Equation (15) is strictly
negative at their genuine stationary points. Bands centered at
\(L=32n/\delta\) instead give strictly positive products. This proves
both sequences. Finally, all these points eventually lie in Note 19's
already favorable outer region, where \((h_0,h_1)\ne(0,0)\) and both
full Laguerre forms are strictly positive. \(\square\)

For the declared half-time rule, (14) reads
\(D=\pi t_0L/32+o(1)\) and
\(r=\exp\{-t_0L^2/32+t_0\pi^2/128+o(1)\}\).
This is an asymptotic obstruction, without an evaluated first
counterexample height. It is not a new certificate in the unresolved
moving small-time cusp.

A useful distinction from the sharp-endpoint obstruction is size. On
either stationary set, (13) gives
\(E=A_{t_0}^2\omega^{2j}(1+O(1/L))\). Hence the diagnostic quotient is

\[
 \frac{P_j}{E}=r\omega^2\{\cos D+O(1/L)\}\longrightarrow0. \tag{18}
\]

It alternates sign but becomes negligible relative to energy at fixed
positive time. This quotient diagnoses the failure on a proved nonzero
outer region; it does not define a loss near a candidate collision.

## 5. Bounded pilot and verification

The [new exact-rational driver](../numerics/check_proportional_gaussian_source_filter_pilot.py)
and [compact record](../numerics/PROPORTIONAL_GAUSSIAN_SOURCE_FILTER_PILOT_20261014.json)
use the same trusted complete-source certificate as Note 22. The domain is
\(0\le t\le1/2\), with one genuine unique current \(h_1=0\) point in
\((101,102)\) and one genuine unique current \(h_2=0\) point in
\((103,104)\) for every time. The eight predeclared closed slabs are
\([k/16,(k+1)/16]\), \(k=0,\ldots,7\); even slabs are development and
odd slabs holdout. Every prescribed branch/slab pair is evaluated.

**All 16 cases certify \(P_j>0\) and \(Q_j>0\), with the prescribed
\(K_j=0\).** In the constant branch normalization
\(Z_k=e^{\pi x_c/8}h_k\), and the same normalization for \(C,G,B\),
conservative lower bounds over all eight slabs are:

| Current branch | \(Z_j\widehat G_j\) | \(Z_j\widehat B_j\) |
| --- | ---: | ---: |
| \(h_1=0\), \(101<x<102\), \(x_c=101.5\) | \(>8108\) | \(>3999\) |
| \(h_2=0\), \(103<x<104\), \(x_c=103.5\) | \(>4100\) | \(>2025\) |

The enclosure for \(h_jR_j\) is strictly positive on slabs 2–7 for
both branches and **undecided** on slabs 0–1 for both branches. Those four
crossings establish neither a zero nor a failed condition. At the exact
endpoint \(t=0\), \(R=0\) by (1). Favorable \(P,Q\) suffice for the
pilot's direct product criterion; a separate favorable complement is
unnecessary.

The original paid endpoint Taylor bounds show opposite current derivative
signs at each spatial boundary, and the original whole-cell
\(h_{j+2}\) enclosure has one strict sign. This certifies the unique
current branch throughout each closed slab, independently of the delayed
field. The source record and both original generating sources are hash
bound by the new driver; its exact partition, orders, normalization, and
required jet-array lengths are checked.

For current slab \(k\), earlier time \(t/2\) lies in original slab
\(p=\lfloor k/2\rfloor\). With current and earlier-center displacements
\(d,d^-\), respectively,

\[
 d^-=d/2+\epsilon_k,
 \quad\epsilon_k=\begin{cases}-1/64&k\text{ even},\\1/64&k\text{ odd},\end{cases}
 \quad |d|\le1/32,\quad |d^-|\le1/32.                     \tag{19}
\]

The driver substitutes (19) by the exact binomial theorem into the
original tensor Taylor polynomial (space order 12, time order 8), then
forms current-minus-earlier coefficient arrays **before** ranging the
common space and time variables. It uses only the original physical
center jets through order 28. This keeps the polynomial correlation;
interval evaluation and independent errors may still overestimate it.
The earlier point is never assumed stationary.

If \(p_{k,r}\) denotes the sum of the original spatial and temporal
jet payments, the corresponding residual payment is

\[
 e_{k,j}=p_{k,j+2}+2a_{\rm upper}p_{k,j+1}
                    +\mu_{\rm upper}p_{k,j}.
\]

The payments for \(G,R,B=C-G/2\) are respectively
\(e_{p,j}\), \(e_{k,j}+e_{p,j}\), and
\(e_{k,j}+e_{p,j}/2\). This is valid because the earlier affine range
stays inside its original paid cell. All original center quadrature,
complete-index, integration, space, and time errors remain included.
Current stationarity additionally intersects the residual with
\(C_j=-h_{j+2}-\mu h_j\), using only the current whole-cell jets.
Products multiply complete integrated observations, preserving all source
cross terms. No physical energy floor or fitted loss is used.

These 16 finite cases cover some times absent from Note 22's fixed-delay
pilot but stay inside the already certified height-104 region. They are
not an extension of the height cover or a collision estimate.

## 6. Consequences and next objective

The complete-source Gaussian removes the artificial sharp endpoints, but
a pure proportional delay does not preserve the exact favorable retained
sign at all heights. This conclusion applies even though the absorption
condition is eventually favorable with zero loss. The finite pilots
measure a genuine local correlation and cannot establish the global sign.
The same slice argument excludes every height-independent rule
\(\delta(t)\) that has \(0<\delta(t_0)<t_0\) at even one positive
time. It includes a positive constant delay whenever both comparison
times are positive.

The same proportional rule can still be investigated on a declared inner
domain, using the already proved full Laguerre signs outside it. The
fixed-time high-height obstruction does not rule out that domain-wise
argument. Its remaining obligations are the unknown moving small-time
region and the finite transition strip, with losses locally bounded
through candidate collisions.

A different candidate can control phase displacement as height grows. For
example, the smooth rule proposed here before any evaluation

\[
 \delta(t,x)=\frac{t}{2(1+t\log(1+x^2))}
\]

satisfies \(0\le\delta\le t/2\) for real \(x\) and bounds
\(\delta\log x\) at large \(x\). This is a proposed investigation
rule, not a proved signed estimate; bounded carrier phase alone does not
control the arithmetic phase in the moving small-time region. Its
\(t\)- and \(x\)-derivatives must be retained in any transport argument.
Another possibility is a prescribed signed loss for the retained product
as well as for absorption. If
\(P\ge-K^GE\) and \(Q\ge-K^QE\), (2) gives
\(\mathcal L_j\ge-(K^Q+K^G/2)E\). Both losses still have to remain
locally bounded through every candidate collision, without an observed
energy denominator.

The immediate unresolved task is therefore a comparison confined to the
unknown cusp, a phase-controlled delay, or a combined signed estimate,
together
with regular-branch and branch-creation payments. No result here extends
the finite height cover beyond 104 or changes the manuscript's current
proved outer and bounded-domain claims.

## 7. Provenance and reproduction

The [identity checker](../numerics/check_proportional_delay_identities.py)
and [20-check receipt](../numerics/PROPORTIONAL_DELAY_IDENTITY_CHECKS_20261014.json)
verify the full complex polarization for both \(j\), controls that detect
missing conjugation, the physical residual multiplier, signed
recombination, the stationary ideal, half-time transport, all three
omitted-pair sectors, and the exact dominant gamma phase and amplitude.
The additional conditional collision control checks only the linear
identity \(Q_{\rm lin}+P_{\rm lin}/2=-A^2\) for
\(P_{\rm lin}=Ag\), \(Q_{\rm lin}=-A^2-Ag/2\); it does not assert
a theta collision or establish a loss bound there. These finite checks
do not prove the asymptotic theorem, whose proof is Section 4.

The [affine audit driver](../numerics/audit_proportional_delay_affine_transport.py)
and [receipt](../numerics/PROPORTIONAL_DELAY_AFFINE_AUDIT_20261014.json)
reproduce the independent 1,200 rational point evaluations of the common
Taylor transport against direct nested evaluation. These check polynomial
algebra using midpoint coefficients, not source quadrature or theta signs.

The [internal review](../reviews/18_PROPORTIONAL_DELAY_PHASE_OBSTRUCTION_REVIEW_20261014.md)
records separate analytic and numerical audits and independent replay.
Run from this investigation's `numerics/` directory, using the standard
Python library:

```sh
python3 check_proportional_delay_identities.py /tmp/inv21-delay-identities.json
python3 check_proportional_gaussian_source_filter_pilot.py \
  --record THETA_CENTERED_RESIDUAL_100_104_20261014.json \
  --original-driver certify_phase_centered_residual.py \
  --contour-source check_shifted_contour_payments.py \
  --output /tmp/inv21-proportional-delay-pilot.json
python3 audit_proportional_delay_affine_transport.py \
  --pilot-driver check_proportional_gaussian_source_filter_pilot.py \
  --output /tmp/inv21-delay-affine-audit.json
```

No new manuscript snapshot, manuscript revision, commit, or tag is part of
this continuation. The existing manuscript remains the integrated
Notes 19–22 version; this note and its review are the next research record.
All new permanent files remain below 1 MiB.

This chat is newly registered as number **10** in the explicitly required
formal replay lane, thread `01a13d07-4714-7f83-a8f5-700a61bc5e0e`, archive
[0013_2026-10-15T00-47-29Z_continue-quaternion-theta-geometry.json](../chat-histories/0013_2026-10-15T00-47-29Z_continue-quaternion-theta-geometry.json).
The preceding chat's number 9 and identity remain unchanged. The UTC
archive date is 15 October; the author's local date is 14 October.
The current turn is `01a13d07-7043-7671-8147-91397afab46e`.
The explicit refresh and bounded exact-turn final capture remain in use;
native completion-hook activation has not been verified.
