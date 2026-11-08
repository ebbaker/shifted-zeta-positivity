# E08 r1: complete paired-zero transverse calculus and an exact sign obstruction

7 November 2026 UTC; 6 November 2026 America/New_York. Prepared for
**Edward Baker** with substantial OpenAI Codex assistance. Tool-selected
executor dispatch configuration: **gpt-6.1-sol, ultra**. Two read-only
analytical subdelegates inherited that selection. This records dispatch
provenance, not independent verification of the serving backend.

**Task:** TND-O-E08 r1, Type E. The frozen
[request20](../research-progress/handoffs/20_TND_O_E08_REQUEST_20261107.md)
and [inputs20](../research-progress/handoffs/20_TND_O_E08_INPUTS_20261107.json)
govern this note. All eighteen input byte counts and SHA-256 hashes matched
before work. Exact hashes and the output digest are recorded in
[return20](../research-progress/handoffs/20_TND_O_E08_RETURN_20261107.json).
Only this note and that return are worker-owned outputs.

**Result, proved in-note:** the mixed-Hessian cancellation is exact; the
complete canonical interaction sum converges with opposite-zero grouping
and an explicit time-uniform tail. Arbitrary nonnegative compact spatial
localization does **not** preserve transverse monotonicity, even for an
even real quartic heat flow with four simple zeros in a common strict
strip. The exact example has \(Q_a'(0)=-9/34\). No canonical sign theorem,
small-flux estimate, or collision-time improvement is obtained.

| Next task | Type / model | Readiness | Required output |
| --- | --- | --- | --- |
| TND-O-E09 | E — Sol/ultra | This fixed package and return are available | Claim-level assessment and the declared correction check |
| TND-O-B04 | B — Astra/ultra | Conceptual successor, in the lead's declared order | Select an independently accessible canonical estimate of the combined localization cost |

The [sole register](../research-progress/02_SMOOTH_LOCALIZATION_RESEARCH_PROGRESS_20261106.md),
[Decision07](../brainstorm/notes/07_TND_O_B03_R4_LOCALIZED_TRANSVERSE_DECISION_20261107.md)
and [Continuation16](16_TND_O_SMOOTH_LOCALIZATION_CONTINUATION_ASTRA_SOL_ULTRA_20261106.md)
retain their ownership and status.

## 1. Domain and theorem

Retain exactly

\[
 H_0(z)=\tfrac18\xi(\tfrac12+iz/2),\qquad
 \partial_\lambda H_\lambda=-\partial_z^2H_\lambda,\qquad
 s=\lambda_*-\lambda.
 \tag{1}
\]

Let \(I\subset[0,1/2]\) be compact. Zeros are counted with multiplicity,
opposite pairing, and conjugation symmetry. The time-zero critical strip
and de Bruijn's strip theorem give \(|\Im z|\le1\) on this domain.
One may use any common strip height \(Y\) below; canonically \(Y=1\).

Fix real \(a\in C_c^2(\mathbb R)\), \(a\ge0\), and set

\[
 f(x,y)=a(x)y^2,\quad Q_a(s)=\sum_jf(x_j(s),y_j(s)),\quad
 A_q=\|a^{(q)}\|_\infty\quad(q=0,1,2).
 \tag{2}
\]

The strip makes the sum finite. A **simple interval for this observable**
means that, locally in time, the zeros above the horizontal support of
\(a\) have simple root charts in a bounded isolating neighborhood.
Repeated exterior roots are permitted and counted with multiplicity.
No global simplicity or extension across a relevant multiple-root time
is asserted.

For distinct \(z_j=x_j+iy_j,z_k=x_k+iy_k\), write
\(d=x_j-x_k,\ e=y_j-y_k,\ D=d^2+e^2\) and
\((x_t,y_t)=(x_k,y_k)+t(d,e)\). Then

\[
 \boxed{Q_a'=2\sum_{j<k}'K_a(z_j,z_k)},
 \tag{3}
\]

where

\[
\begin{aligned}
 K_a&=\frac{(f_y(z_j)-f_y(z_k))e-(f_x(z_j)-f_x(z_k))d}{D}\\
 &=\int_0^1\frac{2a(x_t)e^2-a''(x_t)y_t^2d^2}{D}\,dt.
\end{aligned}
\tag{4}
\]

The prime means the limit of the **endpoint** kernel through full
origin-centered disks. Equivalently, group each remote \(w,-w\) pair
before summing its interaction with an active root. Section 5 proves
absolute summability of those groups and pays the remainder. Arbitrary
rearrangement of individual remote terms is not authorized. If two
coincident repeated roots both lie outside the active region, their
zero interaction is defined as zero rather than writing \(0/0\).

## 2. Finite identity and exact mixed-term cancellation

For a polynomial \(P_s=P_{zz}\), at a simple root,

\[
 (z_j)_s=-P_{zz}(z_j)/P_z(z_j)
        =-2\sum_{k\ne j}(z_j-z_k)^{-1}.
 \tag{5}
\]

Thus \((x_j)_s=-2\sum d/D\), \((y_j)_s=2\sum e/D\).
The chain rule and pairing the ordered terms \(j,k\) and \(k,j\)
give the finite version of (3). For a finite isolated cluster of an
entire heat solution with exterior factor \(U\) and \(g=U_z/U\),
one must retain the additional term

\[
 -2\sum_j\{f_x(z_j)\Re g(z_j)+f_y(z_j)\Im g(z_j)\}.
 \tag{6}
\]

For \(f\in C^2\), chord integration yields

\[
\begin{aligned}
 DK_a
 &=\int_0^1[e(f_{yx}d+f_{yy}e)
                  -d(f_{xx}d+f_{xy}e)](x_t,y_t)\,dt\\
 &=\int_0^1[f_{yy}e^2-f_{xx}d^2](x_t,y_t)\,dt.
\end{aligned}
\tag{7}
\]

The mixed terms cancel exactly because \(f_{yx}=f_{xy}=2a'(x)y\).
Since \(f_{yy}=2a(x)\) and \(f_{xx}=a''(x)y^2\), this proves (4).
No \(C^3\) strengthening is needed. The entire chord stays in
\(|y_t|\le Y\), so

\[
 \boxed{|K_a|\le K_0:=\max\{2A_0,Y^2A_2\}},\qquad
 K_a\ge-Y^2A_2\,d^2/D.
 \tag{8}
\]

There is no reciprocal minimum-gap loss. The diagonal limit can depend
on direction \(d:e\); boundedness is not a single continuous diagonal
extension or a theorem about crossing collisions.

## 3. Complete-source, time-uniform canonical zero count

Use the complete source majorant of frozen M §2, not a finite theta
prefix. With \(B_0=a(P_0)C_2(0)=5C_2(0)\), define

\[
 D_{\rm src}=B_0\pi^2,\quad c=\pi-1>2,\quad
 D_*=\frac{D_{\rm src}e^{-c/2}}{2c},\quad m=H_0(0)>0.
 \tag{9}
\]

For \(u\ge0,\ 0\le\lambda\le1/2\),

\[
 0<F_\lambda(u)\le D_{\rm src}
 e^{u^2/2+9u-\pi e^{4u}}
 \le D_{\rm src}e^{-c e^{4u}},
 \tag{10}
\]

because
\[
 (u^2/2+9u)e^{-4u}\le1/(8e^2)+9/(4e)<1
\]
(the final inequality follows, for example, from \(e>8/3\)).
The canonical half-line transform satisfies
\(|\cos(zu)|\le e^{ru}\) on \(|z|\le r\).
Elementary maximization, putting \(v=e^{4u}\ge1\), gives

\[
 ru-(c/2)e^{4u}\le(r/4)\log(r+2).
\]

The maximum is attained at \(v=1\) or \(v=r/(2c)\), and either value
satisfies the bound. Splitting the exponential in (10) and using
\(e^{4u}\ge1+4u\) for the remaining integral proves

\[
 M_\lambda(r):=\max_{|z|\le r}|H_\lambda(z)|
 \le D_*\exp\{(r/4)\log(r+2)\}\qquad(r\ge0).
 \tag{11}
\]

Also \(F_\lambda\ge F_0\), so \(H_\lambda(0)\ge m\). Put

\[
 A=\log_+(D_*/m),\qquad
 C_1=(A/\log3+1)/\log2.
 \tag{12}
\]

Jensen's formula at radius \(2r\), with a limiting radius if needed,
gives for \(r\ge1\)

\[
\begin{aligned}
 N_\lambda(r)\log2
 &\le\log M_\lambda(2r)-\log H_\lambda(0)\\
 &\le A+(r/2)\log(2r+2)\le A+r\log(r+2).
\end{aligned}
\tag{13}
\]

Here \(N_\lambda(r)\) counts **all** zeros in \(|z|\le r\), with
multiplicity. Thus \(N_\lambda(r)\le C_1r\log(r+2)\) for \(r\ge1\).
To make an all-\(r>0\) bound explicit, define

\[
 M_1=D_*3^{1/4},\quad
 \delta=\min\{1/2,m/(4M_1)\},\quad
 C=C_1\log3/(\delta\log2).
 \tag{14}
\]

Cauchy's estimate from (11) gives \(|H_\lambda'|\le2M_1\) on
\(|z|\le1/2\). Hence \(|H_\lambda(z)-H_\lambda(0)|\le m/2\) on
\(|z|\le\delta\), which is zero-free. For \(\delta<r<1\),
\(N_\lambda(r)\le C_1\log3\le Cr\log(r+2)\). Consequently

\[
 \boxed{N_\lambda(r)\le Cr\log(r+2)\quad(r>0,\ 0\le\lambda\le1/2).}
 \tag{15}
\]

These coarse constants depend only on the complete fixed source.
They are uniform including \(\lambda=0\), independent of \(X,R\)
below, and are not numerically optimized or evaluated.

## 4. Full paired dynamics and explicit velocity tail

The order-at-most-one growth in (11), evenness, and nonvanishing at
zero give the Hadamard product

\[
 H_\lambda(z)=H_\lambda(0)
 \prod_{\{w,-w\}}(1-z^2/w^2).
 \tag{16}
\]

The inverse-square summability below supplies local uniform convergence.
Opposite pairing cancels genus-one exponential factors; evenness removes
the remaining linear exponential, and the order excludes a quadratic
one. Multiplicities repeat the corresponding factors. At a selected
simple root, taking the regular part of its logarithmic derivative gives

\[
 (z_j)_s=-2\sum_{k\ne j}'(z_j-z_k)^{-1}.
 \tag{17}
\]

The \(-j\) term is retained alone, and all other \(k,-k\) terms are paired.
This agrees with Polymath,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2),
Proposition 3.1(i), which requires only the selected root to be simple.

Stieltjes integration using (15) gives

\[
\begin{aligned}
 S_\lambda(U):=\sum_{|w|>U}^{\rm all}|w|^{-2}
 &=-N_\lambda(U)/U^2+2\int_U^\infty N_\lambda(r)r^{-3}\,dr\\
 &\le2C\left\{\frac{\log(U+2)}U+\tfrac12\log(1+2/U)\right\}\\
 &\le\frac{2C}{U}[\log(U+2)+1].
\end{aligned}
\tag{18}
\]

The equality follows also by summing
\(\int_{|w|}^\infty2r^{-3}\,dr\), which handles the strict exterior
cutoff without boundary-atom ambiguity. Opposite representatives
contribute exactly half of \(S_\lambda(U)\).

For \(|z|\le Z,\ U\ge2Z+2\), keep the signed pair

\[
 \frac1{z-w}+\frac1{z+w}=\frac{2z}{z^2-w^2}.
 \tag{19}
\]

The velocity omitted from (17), or the same expression at any evaluation
point of this disk, therefore satisfies

\[
\begin{aligned}
 T_U(z)&=-2\sum_{\substack{\{w,-w\}\\|w|>U}}
             \left(\frac1{z-w}+\frac1{z+w}\right),\\
 |T_U(z)|
 &\le\frac{4CZ}{1-(Z/U)^2}\frac{\log(U+2)+1}{U}\\
 &\le\boxed{\frac{16}{3}CZ\frac{\log(U+2)+1}{U}}.
\end{aligned}
\tag{20}
\]

This is uniform on \(I\), including exterior repeated-root times,
and needs no active minimum-gap lower bound. It estimates the velocity
remainder, not its time derivatives or arbitrary high derivatives.

## 5. Paying the \(K\) sum with the signed endpoint groups

For \(\operatorname{supp}a\subset[-B,B]\), put

\[
 Z=\max\{1,\sqrt{B^2+Y^2}\},\quad
 G=Y^2A_1+2YA_0,\quad U\ge2Z+2.
 \tag{21}
\]

Every root with nonzero \(\nabla f\) lies in \(|z|\le Z\). Define

\[
 D_U(s)=2\sum_{\substack{j<k\\|z_j|,|z_k|\le U}}K_a(z_j,z_k).
 \tag{22}
\]

This is an **interaction approximant**. A finite zero prefix need not be
a polynomial heat solution, so (22) is not its purported derivative.
For remote \(w\), \(f_x(w)=f_y(w)=0\). Define the real-linear functional
\(\ell_j(q)=-f_x(z_j)\Re q-f_y(z_j)\Im q\). The endpoint formula gives

\[
 K_a(z_j,w)+K_a(z_j,-w)
 =\ell_j\!\left(\frac{2z_j}{z_j^2-w^2}\right).
 \tag{23}
\]

Its absolute value is at most
\(|\nabla f(z_j)|\,2|z_j|/(|w|^2-|z_j|^2)\); the series of
**groups** is absolutely convergent. The finite chain rule, (17),
and (20) prove

\[
\begin{aligned}
 |Q_a'-D_U|
 &\le\frac{16}{3}CZ\frac{\log(U+2)+1}{U}
                  \sum_{\rm active\ j}|\nabla f(z_j)|\\
 &\le\boxed{\frac{16}{3}CZ\frac{\log(U+2)+1}{U}N_\lambda(Z)G}\\
 &\le\frac{16}{3}C^2Z^2\log(Z+2)G\frac{\log(U+2)+1}{U}.
\end{aligned}
\tag{24}
\]

“Active” can mean nonzero gradient; including every root above the
support only enlarges the estimate. Equations (22)–(24) define and prove
(3) in its stated grouping. Bounded local root charts justify the
ordinary chain rule for \(Q_a\). The remainder is uniform on compact
simple time intervals, so the cutoff is removable there. No derivative
of the radial indicator is taken. Remote repeated roots need no
velocities of their own.

Two cancellations must be retained. For active \(j\) and remote
\(w=p+iq\) in a strip, the endpoint expression has expansion

\[
 K_a(z_j,w)=f_x(z_j)/p+O_{z_j,a,Y}(|p|^{-2})
                    \quad(|p|\longrightarrow\infty).
 \tag{25}
\]

The leading odd term cancels with \(-w\); separate absolute bounds
would leave a potentially nonsummable inverse-first-power tail.
Also, two endpoints with zero gradient have \(K_a=0\) exactly, even
when their chord crosses the support. Separately bounding the positive
and curvature chord pieces destroys that cancellation. Formula (4)
pays finite small gaps; (23) pays the far field. No separate infinite
positive-chord or curvature-chord sums are claimed.

If \(m_a\) roots lie above the support and \(n_U=N_\lambda(U)\),
at most \(m_an_U\) unordered pairs can contribute. Thus, for example,

\[
 |D_U|\le2m_an_UK_0,\qquad
 Q_a'\ge-2m_an_UY^2A_2-|Q_a'-D_U|.
 \tag{26}
\]

These are coarse, gap-free bounds, without favorable arithmetic size.

## 6. Translating and scaling the spatial weight

For fixed \(\chi\in C_c^2\), \(\chi\ge0\),
\(\operatorname{supp}\chi\subset[-L,L]\), let
\(a(x)=\chi((x-X)/R)\), \(R>0\). Then use

\[
\begin{aligned}
 B&=|X|+RL,\quad Z=\max\{1,\sqrt{(|X|+RL)^2+Y^2}\},\\
 A_0&=\|\chi\|_\infty,\quad A_1=R^{-1}\|\chi'\|_\infty,
       \quad A_2=R^{-2}\|\chi''\|_\infty,\\
 K_0&=\max\{2\|\chi\|_\infty,Y^2R^{-2}\|\chi''\|_\infty\},\\
 G&=Y^2R^{-1}\|\chi'\|_\infty+2Y\|\chi\|_\infty.
\end{aligned}
\tag{27}
\]

The source constant \(C\) is independent of \(X,R\); the displayed
\(Z,G,K_0,N_\lambda(Z)\) are not. For fixed windows, (24) tends to zero
uniformly in time. For jointly varying windows a sufficient explicit
condition is

\[
 U\ge2Z+2,\qquad
 Z^2\log(Z+2)G[\log(U+2)+1]/U\longrightarrow0.
 \tag{28}
\]

No hidden uniformity in unbounded center or shrinking width is asserted.
An ordinate window width \(h\) corresponds to \(H\)-coordinate width \(R=2h\).

## 7. Exact even polynomial sign obstruction in a strict strip

Consider

\[
 P(s,z)=z^4+(12s-\tfrac{15}{2})z^2
              +\tfrac{289}{16}-15s+12s^2.
 \tag{29}
\]

Direct differentiation proves \(P_s=P_{zz}\), and
\[
 P(0,z)=[(z-2)^2+\tfrac14][(z+2)^2+\tfrac14].
\]
The test roots are \(\pm2\pm i/2\), all simple.

For an explicit common strip interval \(|s|\le1/100\), put
\[
 h=\tfrac{15}{4}-6s,\quad c_s=\tfrac{289}{16}-15s+12s^2,
 \quad q=c_s-h^2=4+30s-24s^2.
\]
Then \(3<h<4,\ c_s<25,\ q\ge2311/625>0\). Define
\[
 u^2=(\sqrt{c_s}+h)/2,\qquad v^2=(\sqrt{c_s}-h)/2.
 \tag{30}
\]
Because \(3<h<\sqrt{c_s}<5\), \(1<u<3\) and \(0<v<1\).
Also \(u^2-v^2=h\), \(4u^2v^2=q\), so the four roots
\(\pm u\pm iv\) remain distinct and simple in \(|\Im z|<1\).
To place the test inside the declared Newman-time domain, set
\(\lambda=1/4-s\) and
\(\widetilde P_\lambda(z)=P(1/4-\lambda,z)\). Then
\(\partial_\lambda\widetilde P=-\widetilde P_{zz}\) on
\([6/25,13/50]\subset[0,1/2]\).
This is a simple-interval test; \(s=0\) is not claimed to be a collision.

Choose
\[
 b(t)=
 \begin{cases}(1-t)^3(1+t)^{12},&|t|<1,\\0,&|t|\ge1,\end{cases}
 \qquad a(x)=b(x-2)+b(-x-2).
 \tag{31}
\]
The endpoint orders imply that \(b,b',b''\) extend continuously by zero.
Thus \(a\) is even, nonnegative and \(C_c^2\), supported in
\([-3,-1]\cup[1,3]\), with
\[
 a(\pm2)=1,\qquad a'(2)=9,\qquad a'(-2)=-9.
 \tag{32}
\]

At \(z=2+i/2\), exact algebra gives
\[
 z_s=-\frac{P_{zz}}{P_z}
     =-\frac{30+24i}{-4+16i}
     =-\frac{33}{34}+\frac{36}{17}i.
 \tag{33}
\]
Hence \(u_s(0)=-33/34,\ v_s(0)=36/17\).
All four weights are equal, so
\(Q_a(s)=4b(u(s)-2)v(s)^2\) near zero and \(Q_a(0)=1\). Therefore
\[
\begin{aligned}
 Q_a'(0)
 &=\underbrace{4\cdot9\cdot(-33/34)\cdot(1/4)}
       _{\text{horizontal flux }=-297/34}
   +\underbrace{8\cdot(1/2)\cdot(36/17)}
       _{\text{transverse production }=288/34}\\
 &=\boxed{-9/34<0}.
\end{aligned}
\tag{34}
\]

This is an exact algebraic construction, with no numerical campaign.
Both real reflection and evenness are already present. Multiplying
\(a\) by a positive constant, including normalizing its supremum,
preserves the sign.

The excluded information class consists of real even polynomial heat
flows with simple roots, a common bounded strip, and arbitrary
nonnegative compact \(C^2\) weights. A polynomial also has a coarse
count bound of the form (15). It lacks the complete theta source and
zeta arithmetic. This is not a counterexample to a theta-specific
estimate or an obstruction to every smooth-localization method.

## 8. Inherited balance, benchmark, controls and unpaid canonical estimate

Frozen M §12 gives the finite-cluster transverse balance with exterior
force and carried-weight derivatives. For \(a_j=a(x_j)\), the weight
derivative is \(a'(x_j)(x_j)_s\). Combining it with the transverse term
produces (7): the mixed \(a'\) chord terms cancel, leaving (4).
The gains here are the gap-free estimate, full-index remainder (24),
and exact negative test (34). They supply no new arithmetic sign.

Polymath's Theorem 1.5 and §9 already give real/simple high zeros at
positive time beyond a uniform scale \(\exp(C/\lambda)\), with the
theorem's disk/index margins retained. This package improves neither
that threshold nor its hypotheses. Its source/Jensen count does not
depend on that positive-time asymptotic regime. No novelty or priority
claim is made.

The **actual-theta** conclusion is (3), (15), (20) and (24) on the
stated simple intervals. The **generic** conclusion is the calculus
under its explicit strip/product/count premises. The **control**
conclusion is the scoped failure in §7. The remaining canonical need
is an independently acquired bound for the **combined signed
localization/transport cost**, or for the signed \(K\) sum, in a
declared height/time/width regime. The far tail is paid; the near and
intermediate interactions have not been shown favorable or
arithmetically small. Generic localized transverse production also
has no universal sign; (34) is stronger in showing failure even when
the production term itself is positive.

As in [avoid01](../../../../../avoid/01_restating_the_target.md),
\(Q_a=0\) for every covering window at \(\lambda=0\) is RH, not a
new tested criterion. Equations (8), (24), (34) are quantitative
intermediate/scoped results. The baseline is the
[result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[patterns index](../../../../../avoid/README.md),
[control rule02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scope rule07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

| Control | Shared premises actually relevant here | Failed or unasserted canonical premise |
| --- | --- | --- |
| Quartic (29) | Heat equation, real/opposite/conjugate reflection, simplicity, common strip, coarse zero count | Complete theta source/arithmetic; it explicitly fails the proposed generic sign |
| Isolated polynomial pair | Local heat law and positive transverse production | Theta arithmetic; positive production is compatible with a collision |
| Smooth reflected / positive-primitive | Regularity, reflection, local heat calculus | Complete canonical square coefficients; global use still needs its actual strip/count/product hypotheses |
| Weighted-square | Local heat and finite-cluster identities | Complete reflection; square support alone supplies no global strip/count/product assertion |
| Euler-factor | Paired-zero calculus where its convergence/strip premises hold | Literal unmodified theta/zeta arithmetic; no unstated canonical small-flux bound is claimed to hold or fail |

An absent source identity is not evidence for a derived theta inequality.

## 9. Source use and bounded verification

The frozen policies, controls/classification/scope files, Note16,
Register02, Overview02, Decision07, M §2, M §12, M's localized-statistics
source, and G = Brainstorm06 were read. M §2 supplies the complete-source
majorant; the count and tail constants are derived here. M §12 supplies
the finite-cluster comparator. G supplies inherited scope and benchmark
context, not a sign estimate.

The primary HTML of **D. H. J. Polymath**, *Effective approximation of
heat flow evolution of the Riemann ξ function, and a new upper bound
for the de Bruijn–Newman constant*, arXiv:1904.12438v2, 4 August 2019,
was freshly checked on 7 November 2026 UTC: Proposition 3.1(i) and its
product proof, Theorem 3.2 and Theorem 1.5. The existing
[source-use record](../references/08_TND_O_B03_LOCALIZED_STATISTICS_SOURCE_USE_20261106.md)
and [benchmark record](../references/10_TND_O_B03_R4_BENCHMARK_SOURCE_CHECK_20261106.md)
already identify that version. No new paper/PDF was discovered,
downloaded or added; two-file ownership is preserved.

Two disjoint read-only checks were dispatched by messages before their
work: the exact polynomial test, and the kernel/count/tail derivation.
They wrote no files and returned proofs by message. Their contracts
were those actual dispatch messages, not separate frozen packet files.
The executor checked and incorporated the derivations. This remains
an internal LLM proof-author package sharing inherited premises,
not independent specialist assessment; E09 is distinct.

One local proof/consistency pass checked time sign, factors of two,
mixed cancellation, inverse-square count integration, the half-count
for opposite representatives, remote repeated-root convention,
quartic jets, strict-strip interval and window dependence.
The routine clarifications are the directional diagonal limit,
interaction-approximant interpretation and endpoint/pair grouping.
No redesign, new observable, numerical campaign, manuscript change
or relevant-multiple-root extension was performed.

Only this note and return20 are worker outputs. No source transcript
exists for this worker; none was fabricated or registered. The worker
did not modify histories, register, overview, indexes, root summaries
or manuscript.

**Next: [E] TND-O-E09 — Sol/ultra:** assess this exact note and return.
The next conceptual question remains **[B] TND-O-B04 — Astra/ultra**:
select a canonical bound that pays the combined localization cost in
a useful uniform regime.
