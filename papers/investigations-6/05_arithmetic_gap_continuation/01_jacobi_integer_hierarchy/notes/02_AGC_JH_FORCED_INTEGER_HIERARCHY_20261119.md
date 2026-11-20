# E01 r1: the forced integer hierarchy for the moving Jacobi head

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Explicit helper dispatch **gpt-6.2-sol /
ultra**. Independent serving-model and effort metadata are unavailable.
This is an exact conditional identity on a counted chart, with an
internal algebraic self-check. The [B01 decision](../brainstorm/notes/02_AGC_JH_B01_MOVING_HEAD_CONTRACT_20261119.md)
and [E01 r1 request](../research-progress/handoffs/AGC_JH_E01_REQUEST_R1_20261119.md)
fix the inputs and ownership. The source links below route through the
[result index](../../../../../result-summaries/README.md) and
[patterns index](../../../../../avoid/README.md).

## 1. Counted chart and complete traces

Use forward physical time \(t\) on a compact interval \(I\subset[0,1/2]\).
The unchanged normalized field is \(F_t=2H(t,\cdot)/Z_t\), with the
complete theta source and cosine observation. The moving comparison
readouts are \(G_{N,t}\) and \(G_{N+2,t}\), for \(N\ge2\), with
\(G_{L,t}=\langle e_0,e^{izJ_L(t)}e_0\rangle\). Apply the single-field
identities below to each \(Y\) separately. Assume the same positively
oriented circle \(\Gamma:|z-a|=r\), \(a\in\mathbb R\), counts two zeros
of each compared field with multiplicities, has an open cleared collar,
and each pair lies in \(|z-a|\le r-b\) for a common \(b>0\).
The count, buffer and denominator floors are inputs for any quantitative
application. Each field is holomorphic in space and differentiable in
time with spatial derivatives on the collar. The canonical moment
determinants at fixed finite degree are positive on the real interval,
so the moving links, matrix exponential and normalized theta field are
locally holomorphic in \(t\) around every real slice there.
[VCD cluster resolution](../../../03_volterra_coefficient_dynamics/manuscript/sections/cluster_resolution.tex).

Write \(\langle f\rangle=(2\pi i)^{-1}\oint_\Gamma f(z)\,dz\),
\(B=Y_z/Y\), and \(m_j=\langle (z-a)^jB\rangle\). Set
\[
 c=a+\tfrac12m_1,\qquad D=\tfrac12m_2-(c-a)^2,\qquad
 w=z-c,\qquad Q=w^2-D,\qquad A=Y/Q,\qquad U=A_z/A .
\]
The count gives the monic quadratic of the two enclosed occurrences.
The unit \(A\) extends holomorphically and is zero-free throughout the
disk and a collar, and \(c,D\) are real at real time. On \(\Gamma\),
\(|z-z_\pm|\ge b\) and \(|Q|\ge b^2\), including at \(D=0\).

The complete theta field has the inherited even order-at-most-one product and
count \(O_I(x\log(2+x))\).
[AGC source and pair chain](../../manuscript/sections/01_source.tex),
[product and trace regime](../../manuscript/sections/02_pair_chain.tex).
For a fixed finite degree \(L\), the real symmetric \(J_L\) supplies
\(G_{L,t}(z)=\sum_j\omega_j e^{izx_j}\), \(\omega_j>0\),
\(\sum_j\omega_j=1\). The diagonal parity matrix conjugates \(J_L\) to
\(-J_L\) and fixes \(e_0\), so \(G_{L,t}\) is even, real-symmetric, and
\(G_{L,t}(0)=1\). With \(K_L=\sup_I\|J_L(t)\|<\infty\),
\[
 |G_{L,t}(z)|\le e^{K_L|\operatorname{Im}z|},\qquad
 n_{L,t}(x)\le \frac{2K_Lx}{\log 2}\quad(x>0).
\]
The count follows from Jensen at radius \(2x\) (or a limiting outer
radius if a zero lies there). Partial summation gives a fixed-\(L\)
inverse-square tail \(O(K_L/x)\). Apply the same order-at-most-one
Hadamard argument as in the cited pair chain. Opposite genus-one factors
pair to \(1-z^2/\rho^2\); evenness eliminates the linear exponential
and the value at zero fixes the constant. Thus both readouts have the
complete even product with all occurrences. This establishes a uniform
count in time for each selected degree and leaves the stated dependence
on \(K_L\). It uses the spectral nodes only to prove growth and parity.
[VCD finite readouts](../../../03_volterra_coefficient_dynamics/manuscript/sections/readouts.tex).

For each kernel \(k\) below define
\[
 \tau[k]=-\langle k B\rangle
 =\sum_{\rho_j\ \mathrm{exterior}}k(\rho_j).
\]
Here \(k=Q^{-n}\) for \(n\ge1\), \(k=wQ^{-n}\) for \(n\ge2\), or,
for \(D\ne0\), \(k=k_{p,q}=(z-z_+)^{-p}(z-z_-)^{-q}\) with integer
\(p,q\ge0\), \(p+q\ge2\). Denote the traces by \(S_n,T_n,P_{p,q}\)
respectively, with \(M=S_1=P_{1,1}\) where split coordinates are used.
These kernels and every kernel derivative used below decay at least as
\(O(|z|^{-2})\) and have all their poles inside \(\Gamma\).
For one exterior occurrence the residue of \(k(z)/(z-\rho_j)\) at
\(\rho_j\) is \(k(\rho_j)\), while the residue at infinity is zero.
Each product regularizer is constant and multiplies \(\langle k\rangle=0\).
The enclosed contribution \(k Q_z/Q\) has zero total residue because
all its poles are enclosed and it decays at infinity. The fixed-order
series converge absolutely by the counts, and the locally uniform
paired product justifies passing to its logarithmic derivatives on
the collar. The trace also equals \(-\langle kU\rangle\).
The contour formula defines the local trace through any exterior
multiplicity and through a merger in the \(S,T\) coordinates.
It involves the complete readout on the collar, so no exterior
zero cutoff enters the computation.
[AGC integer traces](../../manuscript/sections/03_hierarchy.tex).

## 2. Pair motion and the general forced row

Use the shared scalar normalization \(\beta_1(t)\) and set \(f=R/Y\) with
\(R=(\partial_t+\partial_z^2+\beta_1)Y\). For \(F_t\), \(R=0\)
because \(\beta_1=Z_t'/Z_t\) is the source second moment. For the
moving \(L\)-site head,
\[
 R_L=\beta_L\beta_{L-1}\,\partial_{\beta_{L-1}}G_{L,t},\qquad
 f_L=R_L/G_{L,t}.
\]
Use the actual last-edge direction, with all other links held fixed
in this partial derivative. This is the VCD physical heat defect,
including the spectral contour representation and the normalization
\(G_{L,t}(0)=1\).
[VCD regular pair law and finite defect](../../../03_volterra_coefficient_dynamics/manuscript/sections/gap_transport.tex).

The collar permits differentiation and integration by parts:
\[
 B_t=(Y_t/Y)_z=-B_{zz}-2BB_z+f_z,\qquad
 \dot c=-\tfrac12\langle Y_t/Y\rangle,\qquad
 \dot D=-\langle wY_t/Y\rangle .
\]
A dot always refers to physical \(t\). From \(Y=QA\),
\[
 Y_{zz}/Y=2/Q+2(Q_z/Q)U+A_{zz}/A .
\]
The scalar normalization and the holomorphic unit term integrate to
zero in both pair equations. Since \(\langle1/Q\rangle=0\),
\(\langle w/Q\rangle=1\), \(2wQ_z/Q=4+4D/Q\), and
\(\langle U/Q\rangle=-M\), one obtains
\[
 \boxed{\quad
 \dot c=\langle Q_zU/Q\rangle+\gamma,\qquad
 \dot D=2-4DM+\delta,\qquad
 \gamma=-\tfrac12\langle f\rangle,\qquad
 \delta=-\langle w f\rangle .
 \quad} \tag{1}
\]
The first heat term is \(U(z_+)+U(z_-)\), evaluated as \(2U(c)\)
at a double, so it needs no separate first-order exterior sum.
At \(D=0\) the defect pieces are \(\gamma=-\tfrac12(R/A)_z(c)\)
and \(\delta=-(R/A)(c)\). Thus the double has
\(\dot D=2-(R/A)(c)\).

For a fixed-order kernel \(k(z;c,D)\) the exact derivative is
\[
 \dot\tau[k]=\langle k(B_{zz}+2BB_z)\rangle
    +\dot c\,\tau[k_c]+\dot D\,\tau[k_D]+\langle k_zf\rangle ,
 \qquad
 \boxed{\ \varepsilon[k]=\langle k_zf\rangle+
              \gamma\,\tau[k_c]+\delta\,\tau[k_D]\ }. \tag{2}
\]
The partial derivatives here hold the other kernel parameters fixed.
The last term in the derivative comes from
\(-\langle k f_z\rangle=\langle k_z f\rangle\), by integrating
\((kf)_z\) around the same closed contour. No moving-boundary term
arises for this fixed circle. Both terms from its moving rational
kernel remain in \(\varepsilon[k]\). Equivalently the forcing is one
signed integral with kernel \(k_z-\tfrac12\tau[k_c]-w\tau[k_D]\)
against \(f\). For \(Y=G_L\), \(\gamma,\delta,\varepsilon[k]\) are
also \(\beta_L\beta_{L-1}\) times the respective last-link derivatives
of \(c,D,\tau[k]\). This follows by inserting
\(f_L=\beta_L\beta_{L-1}(\partial_{\beta_{L-1}}G_L)/G_L\)
into the same contour differentiation, including the varying pair
parameters in the trace. All these formulas take boundary values of the
complete residual quotient, including contributions from its holomorphic
part on the disk.

The part of (2) with \(\gamma=\delta=f=0\) is the inherited
unforced integer recurrence, evaluated on the *current* divisor of \(Y\).
To apply the inherited proof to a forced \(Y\), at each slice truncate
its even product with the targets, opposite partners, conjugates and
multiplicities retained. The truncated polynomials converge along with
all needed spatial jets on the collar. Give each polynomial the
unforced heat first time jet there, which is
\(-B_{zz}-2BB_z\) for the logarithmic derivative. Their pair and trace
heat first jets converge by the fixed-contour formulas. At finite
multiple-root slices, use simple perturbations preserving the count
and the same continuity of first jets. The finite simple root
identities cancel the first-power sums before passage to the infinite
divisor, leaving only absolute fixed-order products. This uses the
slice proof in [AGC integer hierarchy](../../manuscript/sections/03_hierarchy.tex)
and identifies the heat part for \(G_L\) without assigning it heat
evolution in time. Subtracting that heat first jet from the actual
one leaves exactly (2). The approximation here is at one time slice.

## 3. Symmetric hierarchy and explicit low rows

Write a sum with reversed endpoints as zero. In the domains
\(n\ge1\) for \(S_n\) and \(n\ge2\) for \(T_n\),
\[
\begin{aligned}
 \dot S_n={}&2n\sum_{k=1}^n S_kS_{n+1-k}
       +2n\sum_{k=2}^n(T_kT_{n+2-k}+DS_kS_{n+2-k})\\
       &-4n(n+2)S_{n+1}-4n(n+3)DS_{n+2}+\varepsilon^S_n,\\
 \dot T_n={}&2(2n-1)\sum_{k=2}^nT_kS_{n+1-k}
       +4nD\sum_{k=2}^n T_kS_{n+2-k}\\
       &-4(n^2+n-1)T_{n+1}-4n(n+3)DT_{n+2}+\varepsilon^T_n .
\end{aligned}\tag{3}
\]
For \(Q^{-n}\), \(k_z=-2nwQ^{-n-1}\) and \(k_D=nQ^{-n-1}\).
For \(wQ^{-n}\), \(k_z=(1-2n)Q^{-n}-2nDQ^{-n-1}\) and
\(k_D=nwQ^{-n-1}\). In both cases \(k_c=-k_z\). This gives
\[
\begin{aligned}
 \varepsilon^S_n&=-2n\langle wQ^{-n-1}f\rangle
                    +2n\gamma T_{n+1}+n\delta S_{n+1},\\
 \varepsilon^T_n&=\langle[(1-2n)Q^{-n}-2nDQ^{-n-1}]f\rangle\\
               &\qquad+\gamma[(2n-1)S_n+2nDS_{n+1}]
                    +n\delta T_{n+1}.
\end{aligned}\tag{4}
\]
In particular the full equations needed at low order read
\[
\begin{aligned}
 \dot D={}&2-4DM+\delta,\\
 \dot M={}&2M^2-12S_2-16DS_3
          -2\langle wQ^{-2}f\rangle+2\gamma T_2+\delta S_2,\\
 \dot S_2={}&8MS_2+4T_2^2+4DS_2^2-32S_3-40DS_4
          -4\langle wQ^{-3}f\rangle+4\gamma T_3+2\delta S_3,\\
 \dot T_2={}&(6M+8DS_2)T_2-20T_3-40DT_4\\
          &+\langle(-3Q^{-2}-4DQ^{-3})f\rangle
                    +\gamma(3S_2+4DS_3)+2\delta T_3 .
\end{aligned}\tag{5}
\]
Each formula is regular at \(D=0\) and keeps its higher rows.

## 4. Split integer rows and axes

On a \(D\ne0\) subchart choose \(s^2=D\), let \(h=2s\),
\(z_\pm=c\pm s\), \(X=z-z_+\), \(Z=z-z_-\), so \(Z-X=h\).
The forcing parts of \(\dot z_\pm\) and of \(\dot h\) are
\[
 v_\pm=\gamma\pm\delta/h,\qquad
 \dot h=4/h-2hM+2\delta/h .
\]
In particular \(v_+=-\langle Zf\rangle/h\) and
\(v_-=\langle Xf\rangle/h\), in agreement with
\(-R(z_\pm)/Y_z(z_\pm)\) at simple targets.
For \(k_{p,q}=X^{-p}Z^{-q}\),
\[
 k_z=-p k_{p+1,q}-q k_{p,q+1},\quad
 k_{z_+}=p k_{p+1,q},\quad k_{z_-}=q k_{p,q+1}.
\]
Consequently, with any summand with zero coefficient omitted,
\[
 \varepsilon_{p,q}=p\{v_+P_{p+1,q}-\langle k_{p+1,q}f\rangle\}
                  +q\{v_-P_{p,q+1}-\langle k_{p,q+1}f\rangle\}. \tag{6}
\]
Use \(A_h=2/h-hM\) and
\[
\begin{aligned}
 C_{m,n}&=\sum_{i=2}^{m}P_{i,0}P_{m+1-i,n}
          +\sum_{j=1}^{n-1}P_{m,j}P_{0,n+1-j}\quad(m,n\ge1),\\
 C_{m,0}&=\sum_{i=2}^{m-1}P_{i,0}P_{m+1-i,0},\qquad
 C_{0,n}=\sum_{j=2}^{n-1}P_{0,j}P_{0,n+1-j}.
\end{aligned}
\]
The mixed and both axis rows, using the inherited heat terms, are
\[
\begin{aligned}
 \dot P_{p,q}={}&p\{C_{p+1,q}-(p+3)P_{p+2,q}
                   -(q+2)P_{p+1,q+1}+A_h P_{p+1,q}\}\\
               &+q\{C_{p,q+1}-(p+2)P_{p+1,q+1}
                   -(q+3)P_{p,q+2}-A_h P_{p,q+1}\}
                    +\varepsilon_{p,q} &&(p,q\ge1),\\
 \dot P_{p,0}={}&p\{C_{p+1,0}-(p+3)P_{p+2,0}-2P_{p+1,1}
                  +(2/h+v_+)P_{p+1,0}-\langle k_{p+1,0}f\rangle\}
                   &&(p\ge2),\\
 \dot P_{0,q}={}&q\{C_{0,q+1}-2P_{1,q+1}-(q+3)P_{0,q+2}
                  +(-2/h+v_-)P_{0,q+1}-\langle k_{0,q+1}f\rangle\}
                   &&(q\ge2).
\end{aligned}\tag{7}
\]
Under \(s\mapsto-s\) the labels and their forcing exchange. The mixed
\(p=q=n\) forcing reduces to \(\varepsilon^S_n\) using
\(P_{n+1,n}+P_{n,n+1}=2T_{n+1}\) and
\(P_{n+1,n}-P_{n,n+1}=h S_{n+1}\), with the same identities at the
kernel level. The symmetric average
\(T_n=(P_{n-1,n}+P_{n,n-1})/2\) gives the \(T\) forcing by applying
(2) to the averaged kernel \(wQ^{-n}\). The identities use only
\(p+q\ge2\). At a merger the \(S,T\) coordinates provide the regular
equations, with any branch-specific split limit read from those
traces and the local square root. The proof uses no assumption on
individual exterior root velocities or reality.

## 5. Signed all-subinterval transport and algebra checks

For \(u\le v\) in the counted chart, let
\(W_Y(u,v)=\exp(-4\int_u^v M_Y(t)\,dt)\). The full forward identity is
\[
 D_Y(v)=W_Y(u,v)D_Y(u)
      +\int_u^v W_Y(t,v)(2+\delta_Y(t))\,dt . \tag{8}
\]
Solving for \(W_Y(u,v)D_Y(u)\) subtracts that whole integral from
\(D_Y(v)\). For the two selected heads write \(+\) for \(N+2\), plain
symbols for \(N\), and \(\Delta\) for \(+\) minus plain. Subtract (1)
using the plain integrating factor to obtain on **every** subinterval
\[
 \Delta D(v)=W_N(u,v)\Delta D(u)
   +\int_u^v W_N(t,v)\{\Delta\delta(t)-4D_+(t)\Delta M(t)\}\,dt .
 \tag{9}
\]
In the same orientation, the retained interaction
\(J=12S_2+16DS_3\) satisfies
\[
 \Delta M(v)=\Delta M(u)+
   \int_u^v\{2(M_++M)\Delta M-\Delta J+\Delta\varepsilon^S_1\}\,dt .
 \tag{10}
\]
These identities keep the incoming values and the signed combined
integrands. The same subtraction applies to \(F_t\) versus a head,
with \(\delta_F=\varepsilon^S_{1,F}=0\). They are exact transport
descriptions of the readouts and use the same contour data as direct
evaluation. [VCD signed transport](../../../03_volterra_coefficient_dynamics/manuscript/sections/gap_transport.tex).

**Quadratic heat field.** For \(Y=z^2-2(t-T)\) on a short counted
chart around \(T\) take \(\beta_1=0\). Here \(R=0\), \(c=0\),
\(D=2(t-T)\), \(A=1\), and every exterior trace vanishes. The rows
give \(\dot D=2\), \(\dot c=0\), and zero trace derivatives.
Equation (8) gives \(D(v)-D(u)=2(v-u)\), including across a double.
On a chart with \(u<T\) the strict positive-gap transport margin fails.

**Two-site Jacobi readout.** Let \(k_0=\sqrt{\beta_1}\) and
\(\lambda_2=\beta_2/2\). For \(Y=G_2=\cos(k_0z)\),
\(Y_{zz}/Y=-\beta_1\) and
\[
 f=\beta_2\beta_1\frac{\partial_{\beta_1}G_2}{G_2}
   =\lambda_2 zB.
\]
The heat parts of the two count derivatives and of \(B_t\) vanish
because \(Y_{zz}/Y\) is spatially constant. The contour moments
\(\langle zB\rangle=2c\), \(\langle wzB\rangle=2D\) give
\(\gamma=-\lambda_2 c\), \(\delta=-2\lambda_2D\) and
\(v_\pm=-\lambda_2 z_\pm\). For a kernel of scaling degree \(-d\)
under \((z,c,D)\mapsto(\ell z,\ell c,\ell^2D)\), (2) now gives
\[
 \varepsilon[k]=\lambda_2
  \langle (zk_z+ck_c+2Dk_D)B\rangle
  =\lambda_2 d\,\tau[k].
\]
Thus \(\dot M=2\lambda_2 M\), \(\dot S_2=4\lambda_2 S_2\),
\(\dot T_2=3\lambda_2 T_2\), and
\(\dot P_{p,q}=(p+q)\lambda_2 P_{p,q}\) including the axes.
This agrees with direct scaling of every root by
\(\beta_1^{-1/2}\), whose logarithmic physical-time derivative is
\(-\lambda_2\). It also checks the center correction on adjacent
pairs with \(c\ne0\).

For an independent check of the even low heat rows, use the target
pair \(\pm s\), \(s=\pi/(2k_0)\). The exterior is
\(\{\pm(2j+1)s:j\ge1\}\), so \(T_n=0\) and
\(S_n=2(4D)^{-n}\mathcal B_n\) with
\(\mathcal B_n=\sum_{j\ge1}[j(j+1)]^{-n}\). Partial fractions give
\(\mathcal B_1=1\), \(\mathcal B_2=2\zeta(2)-3\),
\(\mathcal B_3=10-6\zeta(2)\), and
\(\mathcal B_4=20\zeta(2)+2\zeta(4)-35\).
The free \(D\) row gives zero since \(M=1/(2D)\).
The \(M,S_2\) heat rows vanish by
\(3\mathcal B_2+\mathcal B_3=1\) and
\(8\mathcal B_2-16\mathcal B_3+\mathcal B_2^2-5\mathcal B_4=0\),
using \(2\zeta(2)^2=5\zeta(4)\) in the second identity.
The odd row vanishes by symmetry in this example. Its general
forcing was checked in (4) by the odd kernel derivatives.

## 6. Evidence boundary

The new statement is a fixed-order exact identity conditional on the
counted chart. A quantitative use falls under
[mechanism classification](../../../../../avoid/01_restating_the_target.md).
The [control screen](../../../../../result-summaries/12_collision_controls_and_screening.md)
and the branch [overview §7](../research-overview/01_AGC_JH_RESEARCH_OVERVIEW_20261119.md#7-analytical-control-screen-at-setup)
give the relevant premise failures. In brief, Euler-factor, weighted-square
and finite-tail controls miss the complete theta coefficients, with
weighted-square and selected finite-prime matches also lacking full
reflection. Reflected super-Gaussian and smooth positive-primitive
controls miss the genuine square expansion despite their respective
reflection or primitive data. Atomic and finite-profile controls,
including their continuous compact extensions, miss the full theta
profile/growth and threshold simplicity. The RH-conditional endpoint
control misses ordinary Dirichlet arithmetic and retains its RH premise.
Variable-kernel controls miss the literal cosine observation. The
VCD finite canonical-score E07 and smooth next-defect E10 controls lose
later smooth reflection and exact arithmetic, respectively. Their
nonreal-zero and sign conclusions have the separate scopes in overview §7.
The analytic identities themselves apply to controls whenever their stated
analytic premises hold, and the quadratic test gives an actual merger
with zero heat defect. A quantitative sign hypothesis would require
its own event-domain screen under [shape-only controls](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
with the restrictions in [scope](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

No canonical cell, collar floor, numerical sign, error phase, tail, or
closure has been acquired here. The inherited source-error and
observation-height memory identities remain in
[VCD error law](../../../03_volterra_coefficient_dynamics/manuscript/sections/error_law.tex),
[degree step](../../../03_volterra_coefficient_dynamics/manuscript/sections/zero_geometry.tex)
and [boundary memory](../../../03_volterra_coefficient_dynamics/manuscript/sections/memory.tex).
The matching degree comparison is E02's separate remit. E02's
time-compatibility check can use (1), (4) and (9)–(10); B02 retains the
in-scope choice of a noncircular quantitative premise. The proof and
the checks here have internal LLM provenance and share the inherited
source premises.
