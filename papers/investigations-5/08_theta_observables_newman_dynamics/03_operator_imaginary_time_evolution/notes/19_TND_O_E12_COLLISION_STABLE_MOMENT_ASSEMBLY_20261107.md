# E12 r1: collision-stable moment assembly and the local kink law

7 November 2026 UTC; 6 November 2026 America/New_York. Prepared for
**Edward Baker** with substantial OpenAI Codex assistance. Tool-selected
executor dispatch configuration: **gpt-6.1-sol, ultra**, retained for
this follow-up. This records configuration selection, not independent
verification of the serving backend.

**Task:** TND-O-E12 r1, Type E, under frozen
[request23](../research-progress/handoffs/23_TND_O_E12_REQUEST_20261107.md),
[inputs23](../research-progress/handoffs/23_TND_O_E12_INPUTS_20261107.json)
and [B06 Decision09](../brainstorm/notes/09_TND_O_B06_COLLISION_CROSSING_ASSEMBLY_DECISION_20261107.md).
All eleven frozen byte counts and SHA-256 hashes matched before work.
The exact [E08 note](17_TND_O_E08_LOCALIZED_TRANSVERSE_CALCULUS_20261107.md),
[E09 assessment](../reviews/06_TND_O_E09_LOCALIZED_CALCULUS_ASSESSMENT_20261107.md)
and completed [E10 note](18_TND_O_E10_CANONICAL_MODULUS_AND_SHARPNESS_20261107.md)
retain their stated scope and versions.

**Result, proved in-note:** the same complete canonical moment is
globally Lipschitz on \([0,1/2]\), with exactly the E10 constant
\[
 \boxed{|Q_{X,R}(\beta)-Q_{X,R}(\alpha)|
 \le M_{X,R}|\beta-\alpha|,\qquad
 M_{X,R}=344A^2\|\chi\|_{(2)}R^{-2}\log^2(2+X)}
 \tag{1}
\]
for \(X\ge10,\ 0<R\le1\), where
\(\|\chi\|_{(2)}=\|\chi\|_\infty+\|\chi'\|_\infty+\|\chi''\|_\infty\).
All multiplicities are included. Its complete paired interaction
formula holds almost everywhere and after integration; the first
distributional derivative has no collision atom. For a multiplicity
\(m\) cluster at \(z_0=x_0+iy_0\),
\[
 \boxed{q'_+(\lambda_0)-q'_-(\lambda_0)
       =m(m-1)\Delta f(x_0,y_0).}
 \tag{2}
\]
No global simple labeling, uniform event separation or uniform
Hermite remainder is assumed.

| Declared next task | Type / model | Required dependency and output |
| --- | --- | --- |
| TND-O-E13 | E — Sol | Separate claim-level assessment of the assembled fixed results |
| TND-O-B05 | B — Astra | Decide a genuine collision consumer with an independently acquired mass or flux input |

Only this note and
[return23](../research-progress/handoffs/23_TND_O_E12_RETURN_20261107.json)
are worker-owned outputs. The independent E10 r2 endpoint-moment proof
is not used. No shared register, history, manuscript or earlier output
is edited.

## 1. Object, inherited estimate and time orientation

Retain
\[
 H_0(z)=\tfrac18\xi(\tfrac12+iz/2),\qquad
 \partial_\lambda H=-H_{zz},\qquad s=\lambda_*-\lambda.
 \tag{3}
\]
The complete source makes \(H\) jointly entire in time and position.
For real \(0\le\lambda\le1/2\), all zeros lie in \(|\Im z|\le1\).
They are counted with multiplicity, opposite pairing and conjugation
symmetry. Fix
\[
 a(x)=\chi((x-X)/R),\quad f(x,y)=a(x)y^2,\quad
 Q(\lambda)=\sum_jf(x_j(\lambda),y_j(\lambda)),
 \tag{4}
\]
where \(\chi\in C_c^2([-1,1])\), \(0\le\chi\le1\),
\(X\ge10,\ 0<R\le1\). The sum is finite at each time.

E10 proved \(|Q_\lambda|\le M_{X,R}\) on intervals with simple
relevant roots. Its absolute constant \(A\ge1\) simultaneously pays
the canonical unit-count and safe-line-resolvent bounds, including
time zero. The number \(344A^2\) in (1) is unchanged here. Hermite
constants, event numbers and root gaps will not enter it.

The E08 kernel, for distinct \(z_j,z_k\), is
\[
 K_{jk}=
 \frac{(f_y(z_j)-f_y(z_k))e-(f_x(z_j)-f_x(z_k))d}{d^2+e^2}
 =\int_0^1
  \frac{2a(x_t)e^2-a''(x_t)y_t^2d^2}{d^2+e^2}\,dt,
 \tag{5}
\]
where \(d=x_j-x_k,\ e=y_j-y_k\), and \((x_t,y_t)\) is the
straight chord. The mixed Hessian terms cancel. In the present
Newman time its simple-root formula is
\[
 Q_\lambda=-2\sum_{j<k}'K_{jk};
 \tag{6}
\]
the sign is opposite to \(Q_s\). The grouping in (6) remains E08's
full opposite-pair grouping, not arbitrary rearrangement.

## 2. Continuity of the complete moment, including support crossings

Fix \(\lambda_0\in[0,1/2]\). Choose vertical lines just outside
\([X-R,X+R]\), within a fixed positive collar, avoiding the finitely
many zero coordinates at time \(\lambda_0\). Together with
\(\Im z=\pm2\), they bound a rectangle whose boundary is zero-free
at that time. Joint analyticity and compactness of the boundary
preserve nonvanishing there for nearby real parameters.

The argument principle preserves the finite total multiplicity
inside. Small disjoint disks around its time-\(\lambda_0\) roots,
followed by Rouché's theorem, show that this root multiset varies
continuously, with multiplicity. Equivalently, zeros in each disk
remain arbitrarily close to its center as the time tends to
\(\lambda_0\). The rectangle has a horizontal collar around the
support, so all roots outside it contribute zero for nearby times.
The sum of the continuous \(f\) over its finite root multiset
therefore proves
\[
 Q(\lambda)\longrightarrow Q(\lambda_0).
 \tag{7}
\]

At the two time endpoints this is inward continuity. No single
rectangle is required to have a zero-free boundary for every time.
When a simple root crosses a support endpoint, the globally
zero-extended \(C^2\) weight already supplies its continuous
contribution and chain rule. Such crossings introduce no indicator
term and need not be counted or separated as events.

## 3. Finiteness of relevant multiple-zero events

Use the fixed closed padded spatial box
\[
 K_{X,R}=\{z:|\Re z-X|\le R+1,\ |\Im z|\le2\}.
\]
Define the set of repeated-zero points in space and real time,
\[
 \mathcal E_{X,R}=
 \{(\lambda,z)\in[0,1/2]\times K_{X,R}:
                     H_\lambda(z)=H_{\lambda,z}(z)=0\}.
 \tag{8}
\]
This is closed and compact. Every nonzero entire slice has isolated
zeros of finite multiplicity; \(H_\lambda(0)>0\) ensures that no
slice is identically zero.

At any point \((\lambda_0,z_0)\) of multiplicity \(m\ge2\), the
freshly checked Polymath Proposition 3.1(ii) gives an isolating disk
with exactly \(m\) roots and, for \(\tau=\lambda-\lambda_0\),
\[
 z_j(\lambda_0+\tau)
   =z_0+\sqrt{2\tau}\,h_j+O(|\tau|),\qquad 1\le j\le m,
 \tag{9}
\]
where the \(h_j\) are distinct real roots of the probabilists'
Hermite polynomial. For \(\tau<0\) use
\(\sqrt{\tau}=i\sqrt{|\tau|}\). Distinct leading separations have
size proportional to \(\sqrt{|\tau|}\), which dominates the
event-dependent \(O(|\tau|)\) errors for sufficiently small
nonzero \(\tau\). These \(m\) roots exhaust the disk and are simple.
At \(\tau=0\) the disk contains only \(z_0\).

Thus each point of \(\mathcal E_{X,R}\) is isolated in **space and
time**, not just as a root of a fixed slice. A compact discrete
subset of a metric space is finite: any infinite subset would have
an accumulation point in the same closed set, contradicting this
local isolation. Hence \(\mathcal E_{X,R}\), and its projection
\(T_{X,R}\) onto time, are finite.

This argument includes possible spatial-boundary accumulations:
their limiting point lies in the same closed box and is subject to
(9). It also includes accumulation at \(\lambda=0,1/2\):
the jointly entire canonical family gives the local analytic
extension needed to apply (9) there. Only the part of the
neighborhood inside the declared interval is used in the assembly.
No common event radius, multiplicity bound or separation is
claimed. Their dependence on \(X,R\) is harmless.

## 4. Joining the simple intervals with the same Lipschitz constant

Order the finite set \(T_{X,R}\) and add the endpoints \(0,1/2\).
On each complementary open interval the roots relevant to the
support are simple in local bounded root charts. E10 therefore
gives \(|Q_\lambda|\le M_{X,R}\) there, with exactly the same
constant on every interval. By the mean-value theorem and the
continuity (7), the bound extends to both interval endpoints.

Given any \(0\le\alpha<\beta\le1/2\), split \([\alpha,\beta]\)
at its finitely many event times. Summing its interval bounds
gives
\[
 |Q(\beta)-Q(\alpha)|
 \le M_{X,R}\sum_\ell(t_{\ell+1}-t_\ell)
 =M_{X,R}(\beta-\alpha).
 \tag{10}
\]
This proves (1). The number of summands does not multiply the
constant: only their total duration appears.

Consequently \(Q\) is absolutely continuous and belongs to
\(W^{1,\infty}(0,1/2)\), with its continuous representative on the
closed interval and
\[
 \|Q_\lambda\|_{L^\infty}\le M_{X,R},\qquad
 Q(\beta)-Q(\alpha)=\int_\alpha^\beta Q_\lambda(t)\,dt.
 \tag{11}
\]
This is a full-time theorem for the whole stated \(X,R\) family.
The event sets may vary with those parameters; their number and
separation do not occur in (1).

## 5. Complete interaction identity after integration

Choose
\[
 Z=\max\{1,\sqrt{(X+R)^2+1}\},\quad
 G=R^{-1}\|\chi'\|_\infty+2\|\chi\|_\infty,\quad U\ge2Z+2.
 \tag{12}
\]
Let \(C_0\) be the complete-source zero-count constant in E08,
\(N_\lambda(r)\le C_0r\log(r+2)\), uniform on \([0,1/2]\).
Define the Newman-time interaction approximant
\[
 \mathcal J_U(\lambda)
 =-2\sum_{\substack{j<k\\|z_j|,|z_k|\le U}}K_{jk}(\lambda).
 \tag{13}
\]
At a coincident active pair its value can be assigned arbitrarily,
say zero. The relevant event times are finite and do not affect any
integral. Coincident inactive repeated roots have their exact zero
endpoint contribution, as in E08. Radial cutoffs include complete
opposite pairs.

For every \(\lambda\notin T_{X,R}\), E08 gives
\[
 |Q_\lambda-\mathcal J_U|
 \le \epsilon_U:=
 \frac{16}{3}C_0^2Z^2\log(Z+2)G
                   \frac{\log(U+2)+1}{U}
 \longrightarrow0.
 \tag{14}
\]
The bound is independent of distance to the event set. It uses
only bounded active gradients, a uniform zero count and the signed
paired far field; it has no small-gap denominator.

The finite symmetric sums in (13) are measurable. Locally, this
follows from continuous root multisets, a Borel radial indicator
and the bounded off-diagonal kernel with an assigned diagonal
value. Uniform zero counts bound their finite number of terms.
Thus (14) is an essential-uniform bound on the whole time interval,
not merely separate convergence on compact subintervals away from
collisions. In particular
\[
 \|\mathcal J_U-Q_\lambda\|_{L^\infty(0,1/2)}
 \le\epsilon_U,\qquad
 \|\mathcal J_U\|_{L^\infty}\le M_{X,R}+\epsilon_U.
 \tag{15}
\]
Changing the finitely many exceptional time values if needed has
no effect. Therefore the complete identity holds almost everywhere
and has the integrated form
\[
 Q(\beta)-Q(\alpha)
   =\lim_{U\to\infty}\int_\alpha^\beta\mathcal J_U(t)\,dt,
 \quad
 \left|Q(\beta)-Q(\alpha)-\int_\alpha^\beta\mathcal J_U(t)\,dt\right|
       \le(\beta-\alpha)\epsilon_U.
 \tag{16}
\]
For \(\varphi\in C_c^\infty(0,1/2)\), equivalently,
\[
 -\int Q\varphi'
   =\int Q_\lambda\varphi
   =\lim_{U\to\infty}\int\mathcal J_U\varphi.
 \tag{17}
\]
This proves the distributional identity and justifies the cutoff
interchange. The first derivative is the \(L^\infty\) density
\(Q_\lambda\,d\lambda\); it has no atom at a collision. No extension
by zero outside the parameter interval, with artificial endpoint
atoms, is being made. The finite cutoffs are interaction
approximants, not derivatives of truncated heat polynomials.

## 6. Analytic centroid and the one-sided slope law

This calculation is local and applies at an arbitrary complex
multiple zero \(z_0=x_0+iy_0\). Choose a fixed small isolating
contour \(\Gamma\) on which \(H\ne0\) for parameters near
\(\lambda_0\). Its displacement sum
\[
 S(\tau)=\frac1{2\pi i}\oint_\Gamma
       (z-z_0)\frac{H_z(\lambda_0+\tau,z)}
                       {H(\lambda_0+\tau,z)}\,dz
       =\sum_{j=1}^m(z_j-z_0)
 \tag{18}
\]
is holomorphic in \(\tau\), so
\[
 S(\tau)=c\tau+O(\tau^2).
 \tag{19}
\]
This analytic sum, or \(S/m\) as the centroid displacement, supplies
one common derivative on both sides. Put
\[
 M_m=m(m-1),\qquad
 B_f=f_x(z_0)\Re c+f_y(z_0)\Im c.
 \tag{20}
\]
The probabilists' Hermite coefficients give
\(\sum_jh_j=0\) and \(\sum_jh_j^2=M_m\): the monic
coefficient of \(x^{m-2}\) is \(-m(m-1)/2\).

For \(\tau>0\), (9) implies
\[
 \sum_j(\Delta x_j)^2=2M_m\tau+o(\tau),\qquad
 \sum_j(\Delta y_j)^2,\ \sum_j\Delta x_j\Delta y_j=o(\tau).
 \tag{21}
\]
For \(\tau<0\), it implies
\[
 \sum_j(\Delta y_j)^2=-2M_m\tau+o(|\tau|),\qquad
 \sum_j(\Delta x_j)^2,\ \sum_j\Delta x_j\Delta y_j=o(|\tau|).
 \tag{22}
\]
Use the \(C^2\) Taylor expansion of \(f\), summing its linear
part through the exact analytic sum (19), not through separate
unknown root remainders. For
\(q(\lambda)=\sum_{j=1}^m f(z_j(\lambda))\), this gives
\[
 q(\lambda_0+\tau)-mf(z_0)=
 \begin{cases}
  \tau[B_f+M_m f_{xx}(z_0)]+o(\tau),&\tau>0,\\
  \tau[B_f-M_m f_{yy}(z_0)]+o(|\tau|),&\tau<0.
 \end{cases}
 \tag{23}
\]
The event one-sided difference quotients therefore exist and equal
\[
 q'_+=B_f+M_mf_{xx},\qquad
 q'_-=B_f-M_mf_{yy}.
 \tag{24}
\]
Subtracting cancels the complete centroid contribution and proves
\[
 q'_+-q'_-=M_m(f_{xx}+f_{yy})(z_0)
        =m(m-1)[a''(x_0)y_0^2+2a(x_0)].
 \tag{25}
\]
No \(O(\tau)\) root remainder has been differentiated.

The adjacent ordinary derivatives also tend to these slopes,
if “jump” is interpreted as a jump of the derivative density.
Here is a justification beyond the difference quotients. With
\(w^2=\tau\), the heat equation and multiplicity make
\[
 w^{-m}H(\lambda_0+w^2,z_0+wu)
 \tag{26}
\]
holomorphic at \(w=0\): terms of parabolic weight below \(m\)
vanish. Its leading polynomial is a nonzero constant times
\(\operatorname{He}_m(u/\sqrt2)\), with simple roots.
The analytic implicit-function theorem supplies holomorphic
branches \(u_j(w)\) and exact roots \(z_j=z_0+wu_j(w)\).
This proves the derivative estimates
\(z_j'=O(|\tau|^{-1/2})\) directly from analytic branches.
For the negative side take \(w=i\sqrt{|\tau|}\).

Expand \(\nabla f(z_j)=\nabla f(z_0)+D^2f(z_0)\Delta z_j
+o(|\Delta z_j|)\), and sum its product with \(z_j'\).
The first term sums to \(B_f+o(1)\) by differentiating only
the analytic \(S\). The horizontal quadratic products tend to
\(M_m\) on the positive side and the vertical products to
\(-M_m\) on the negative side; mixed products tend to zero.
The gradient remainder contributes \(o(1)\), using
\(|\Delta z_j|=O(\sqrt{|\tau|})\).
This proves the two neighboring derivative limits (24) using
\(C^2\) alone. It does not formally differentiate a bare remainder
in (9), nor assert uniform high-derivative bounds.

## 7. Real events, simultaneous clusters and endpoints

At a real event \(y_0=0\),
\[
 \nabla f(z_0)=0,\quad f_{xx}(z_0)=0,\quad
 f_{yy}(z_0)=2a(x_0).
\]
Thus
\[
 \boxed{q'_-=-2m(m-1)a(x_0),\qquad q'_+=0.}
 \tag{27}
\]
The positive-Newman-time branches are in fact real for a real
event: their limiting Hermite roots are real, and conjugation plus
local branch uniqueness preserves reality. In reverse heat time
a double event has post-event slope \(+4a(x_0)\), matching the
isolated polynomial pair.

At a time with several multiple clusters, choose disjoint isolating
contours and add (25). The remaining finitely many relevant simple
roots have continuous derivatives there. Hence the jump of the
complete observable is
\[
 Q'_+(\lambda_0)-Q'_-(\lambda_0)
 =\sum_\ell m_\ell(m_\ell-1)\Delta f(z_\ell).
 \tag{28}
\]
A true boundary point of the zero-extended support has vanishing
jets through order two, so it introduces no omitted support-edge
term. Multiple clusters outside the support have zero local
contribution. No global labeling is required.

At \(\lambda_0=0\) or \(1/2\), only the inward slope belongs
to the declared full observable on \([0,1/2]\). Both local cluster
slopes and their algebraic jump can be discussed using the
jointly entire mathematical continuation through the endpoint;
this does not assert a global strip or moment theorem outside
the declared interval.

## 8. Scope, source use and bounded verification

The global result is (1), (11), (16) and (17), with complete
zero index, all multiplicities and unbounded-height parameter
dependence \(R^{-2}\log^2(2+X)\). Fixed width costs \(\log^2X\);
mean-spacing width \(R\asymp1/\log X\) costs \(\log^4X\).
The local result is the exact kink law (25), including the real
case (27). None gives favorable spatial flux, small endpoint
mass, an RH exclusion or a collision envelope.

The real and complex local laws are generic heat geometry and
are shared by polynomial controls. Smooth reflected or
positive-primitive controls share the local calculus without
canonical square arithmetic. Weighted-square controls do not
supply complete reflection, and Euler-factor controls alter
literal canonical arithmetic. Their global assembly must still
verify its actual strip, count and field bounds; no unproved
small-flux assertion is assigned to them. The existing
[result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[patterns index](../../../../../avoid/README.md),
[classification01](../../../../../avoid/01_restating_the_target.md)
and [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
remain the screening baseline. All-covering-window vanishing at
time zero remains RH, rather than a tested consequence.

The primary HTML of Polymath, arXiv:1904.12438v2, 4 August 2019,
was freshly checked on 7 November 2026 UTC at Proposition 3.1(ii)
and its proof. Its factor \(\sqrt{2\tau}\), probabilists' Hermite
normalization, local exhaustion, simplicity and event-dependent
error constants match (9). M §2 supplies joint entire dependence;
M's multiplicity section supplies the inherited finite heat
normal form. The assembly and contour-centroid calculation are
explicit here. Existing reference records identify the same
article; no new article/PDF or reference file is added.

One independent-scope read-only follow-up went to the existing
kernel checker, while the executor handled the global assembly:
verify the centroid kink law, derivative-limit qualification and
space/time isolation. Its contract was the actual pre-work
message, not a separate frozen packet file. It inherited the
same dispatch selection, wrote no files, and returned the
derivation by message. The executor checked and incorporated it.
This is internal LLM checking with shared inherited premises,
not independent specialist assessment.

One local consistency pass checked compact-discrete finiteness,
endpoint and spatial-boundary accumulation, support crossings,
the unchanged Lipschitz constant, the uniform interaction
remainder, distributional sign, analytic centroid, both Hermite
orientations and simultaneous/endpoint slopes. No mathematical
repair, new observable, numerical or symbolic research run,
shared-file edit, manuscript revision, snapshot, commit or push
was required. No worker source transcript exists; none was
fabricated or registered.

**Next: [E] TND-O-E13 — Sol:** assess the exact assembled package.
**[B] TND-O-B05 — Astra** must identify the additional canonical
input for any genuine collision consumer; global regularity and
the generic kink law alone do not exclude one.
