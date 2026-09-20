# Arithmetic sign: boundary response, certified mixed terms and two obstructions

13 September 2026. This continuation uses the **live** manuscript through
note 19, not its archived predecessor. The preceding live PDF and complete
sources are preserved in [this snapshot](../archive/drafts/20260913-before-sign-analysis/README.md).
The mathematical results below have internal review and small exact checks;
no independent specialist review or priority claim is asserted.

The strongest new intermediate result is an exact, bounded **noncompact**
boundary correction to the Neumann gamma model. It gives equality of the
operator domains, explicit low-mode columns, and controlled tails for the
mixed response. Its essential norm is exactly \(\pi/2\) at every fixed
positive support length. Thus a finite mass approximation to this correction
cannot converge in operator norm, although its low-mode columns do converge.

A second result concerns arithmetic information: replacing the prime measure
by \(e^r\,dr\), while preserving the gamma term, both poles and the contact,
gives a strictly negative form already at length two. Leading prime density
alone cannot supply positivity. An exact discrepancy identity explains which
information that replacement loses.

Neither result proves the remaining sign. Throughout,
\[
\|\Phi_Lf\|^2=Q_L[f]+\langle Pf,D_NPf\rangle,
\qquad D_N>0,
\]
\[
Q_L\ge0\quad\Longleftrightarrow\quad
S_N=G-D_N=M-\alpha I-B^*H^{-1}B\ge0.
\tag{20.1}
\]
The positive completion is retained with its error and unused output.

## 1. Audit: what the reduction actually uses

On \(X=L^2(I_L)\), with zero extension \(E_L\), set
\[
b(s)=\sum_{k\ge0}\frac{2}{a_k}\frac{s}{a_k^2+s},
\quad a_k=2k+\tfrac12,\quad
w_0=\psi(\tfrac14)-\log\pi,
\]
\[
W_L=T_L+w_0I+P_L^{\rm pole}-J_L^{\rm off},
\quad P_L^{\rm pole}=2cc^*-2ss^*,
\quad
J_L^{\rm off}=\sum_{m\log p<L}(\log p)p^{-m/2}
(T_{m\log p}+T_{m\log p}^*).
\tag{20.2}
\]
Here \(T_L\) is the zero-extension gamma operator, \(c(x)=\cosh(x/2)\),
\(s(x)=\sinh(x/2)\), and \(T_d=E_L^*U_dE_L\). Inner products are
antilinear in their first argument. Its form domain is exactly
\[
\mathcal D_{\log,L}=\left\{f:\int_{\mathbb R}\log(2+|\tau|)
|\widehat{E_Lf}(\tau)|^2\,d\tau<\infty\right\}.
\]

The audit of sections 10--15 and notes 18--19 finds no invalidating gap in
the reduction under their stated hypotheses:

* The bounded-component closure, support contraction and mollification
  arguments justify the source and its smooth core. The adjoint condition is
  the **interval restriction** of the distributional whole-line expression;
  imposing a whole-line \(L^2\) condition would be stronger than necessary.
  Source/form and operator domains remain different. Section 3 below sharpens
  the comparison-domain inclusion to an exact Neumann-domain description.
* Exterior-energy removal and zero extension of Dirichlet competitors have
  the stated inequality directions. They compare different auxiliary
  preparations; they do not change the actual gamma boundary conditions.
* Cosine modes belong to the operator domain, not just the form domain.
  Therefore \(B=QW_LP\) is a bounded finite-dimensional input map, the
  restricted operator \(H\) is well defined, and \(H^{-1}BP\) maps into its
  operator domain. This justifies the minimizer in the Schur equivalence.
* \(A^*A=W_L+\alpha I\), with
  \(\alpha=e^D+c_{\mathcal S}-w_0\), counts the contact once. Every active
  prime power is present. A return at distance exactly \(L\) has zero
  correlation; an inactive prime changes the reference contact and
  \(\alpha\) by the same amount. The unused component
  \(Z=(I-\Pi_H)A|_{PX}\) must be retained.
* The high response uses a previously proved positive gap, and its source
  tails are controlled after multiplication by the unbounded source. The
  identity \(H^{-1}-V=\alpha VH^{-1}\ge0\) is valid because
  \(V=(H+\alpha I)^{-1}\); it does not justify commuting prime translations
  with a compressed gamma resolvent.

The genuine arithmetic inputs are the gamma masses and their coefficients,
the exact scalar \(w_0\), the two pole residues, and the entire active list
of distances \(m\log p\) and weights \((\log p)p^{-m/2}\). The cutoff proof
uses only a coarse norm bound on that list. Closed-source calculus, range
projection, square completion, the binomial response, finite-dimensional
Schur reduction and residual estimates are generic operator theory. None
of those generic steps correlates primes with the archimedean data.

In particular, for fixed \(L,P\), changing the permitted delay or adding
inactive primes changes \(G,D_N\) separately but leaves
\[
M-\alpha I=PW_LP,\qquad B=QW_LP,\qquad H=QW_LQ|_{QX}
\tag{20.3}
\]
unchanged. Tuning that positive reference cannot improve \(S_N\).

The physical cap is still a unit tensor label in these arithmetic channels.
Its residue calibration is relevant to that normalization, but does not
give \(G\ge D_N\). Any use of metric selection retains the **conditional**
identification of the physical Hodge family with the exact chiral equation
in the specified source frame. Hodge existence is not that identification.

## 2. Four routes and their precise missing inputs

### A. Ordered response and a one-sided tail budget

In note 19 write
\[
V=V_0^{1/2}(I-F_0)^{-1}V_0^{1/2},\qquad
F_0=V_0^{1/2}(tI-K_H)V_0^{1/2},\quad 0\le F_0\le\rho I<I.
\]
Consequently
\[
0\le V-\sum_{j=0}^{r}V_0^{1/2}F_0^jV_0^{1/2}
\le\frac{\rho^{r+1}}{1-\rho}V_0.
\tag{20.4}
\]
The sandwiches equal \([V_0(tI-K_H)]^jV_0\) in precisely that order.
For exact \(V\), put
\[
F_\ell=\sum_{j=0}^{\ell}\alpha^jV^{j+1},\qquad
0\le H^{-1}-F_\ell\le\frac{\theta^{\ell+1}}{\delta}I,
\quad\theta=\frac\alpha{\alpha+\delta}.
\tag{20.5}
\]
Functional calculus proves both tail bounds. A concrete sufficient new
lemma would be, for each \(L\), a specified \(\ell(L)\) and a proof that
\[
PW_LP-B^*F_\ell B
\ \ge\ \frac{\theta^{\ell+1}}{\delta}B^*B.
\tag{20.6}
\]
An approximation to \(V\) additionally needs its own propagated error from
(20.4). The missing arithmetic input is cancellation between the full low
block and the ordered mixed responses, not convergence of either series.
For a fixed prescription, (20.6) is a stronger sufficient estimate rather
than the exact Weil criterion; no all-length proof of it is available.
Merely asking for an optimal tail equal to the true error returns (20.1).

**Exact failure test.** For any \(\ell\ge0\), let
\[
W=\begin{pmatrix}a&1\\1&1\end{pmatrix},\quad
a=1-2^{-\ell-2},\quad \alpha=1,
\quad P=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]
Then \(T=W+I>0\), \(H=1\), \(V=1/2\), and
\[
a-F_\ell=2^{-\ell-2}>0,
\qquad S=a-H^{-1}=-2^{-\ell-2}<0.
\tag{20.7}
\]
The omitted inverse tail has the wrong direction for inferring positivity
from the truncated matrix. This family has all the generic hypotheses of
note 19's negative control. An arithmetic proof of (20.6), which this
family fails, is what would distinguish the target.

Positive grouped terms also do not give signs to individual prime words.
For instance \(X=\operatorname{diag}(1,1/4)\) and
\(Y=\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\ge0\)
have
\(\det(XY+YX)=-9/16\). Reordering or splitting mixed words can destroy
positivity even when the original sandwiches are positive.

### B. Boundary-resolved mixed-response estimates (selected route)

Instead of approximating the whole source, approximate only the high
responses to the finite low-input space. Choose the cutoff \(N\) by note
18. For \(K>N\), let \(P_{N,K}\) project onto cosine modes
\(N,\ldots,K-1\), and define the independently positive Galerkin response
\[
Y_K=(P_{N,K}HP_{N,K})^{-1}P_{N,K}B,
\qquad R_K=B-HY_K.
\tag{20.8}
\]
The inverse is on \(P_{N,K}X\), and \(Y_K\) is extended into \(QX\).
Section 4 proves the sufficient certificate
\[
S_N\ge PW_LP-B^*Y_K-d_K^{-1}R_K^*R_K,
\quad d_K=b((K\pi/L)^2)-\beta_L>0.
\tag{20.9}
\]
**Missing lemma B:** find a rule \(K=K(L)\), justified from the actual
arithmetic entries, for which the right side of (20.9) is nonnegative for
every \(L\). A nonnegative margin including all enclosure errors is needed.

For each prescribed \(L,K\), this is an independently checkable sufficient
inequality: it uses a known positive high compression and finite Gram
data, with an explicit infinite-tail bound. It is not an independent
explanation of its own sign. Allowing arbitrary exact responses and zero
error would return the original criterion. The new boundary theorem below
supplies the previously hidden gamma part of \(B\) and of \(R_K\), so this
route has concrete intermediate lemmas that can be proved without Weil
positivity. It keeps the actual prime shifts and their interference with
those columns. It must fail to certify the negative control, by (20.9).

This is the selected route because it estimates the unresolved mixed
response directly. The naive stronger variant, norm approximation of the
entire gamma boundary correction by finitely many masses, fails. The
finite-input variant survives with quantitative bounds.

### C. A physical contraction with an arithmetic intertwining identity

In note 19's original output space retain \(Zp\) and define the known
defect preparation
\[
\mathcal E_Np=\sqrt\alpha\,
\bigl(p,V^{1/2}H^{-1/2}Bp\bigr),
\qquad \mathcal E_N^*\mathcal E_N=D_N.
\tag{20.10}
\]
A genuine sufficient physical lemma would construct, from independent
gluing data, a unitary \(\mathcal U_L\), an isometric injection \(\iota_L\)
of the original output, and an output projection \(\pi_L\), such that
\[
\mathcal C_L=\pi_L\mathcal U_L\iota_L,
\qquad \mathcal C_LZp=\mathcal E_Np
\quad\hbox{for every low input }p.
\tag{20.11}
\]
The contraction bound then gives \(D_N\le G\) without discarding another
port: its complementary output supplies the nonnegative difference.
Arithmetic must enter the **intertwining identity**, including the contact,
gamma response, poles and every active return, not only unitarity.

The abstract existence of a contraction satisfying (20.11) is **exactly
equivalent** to the unresolved ordering. To see this, define
\(\mathcal C(Zp)=\mathcal E_Np\), possible since \(Z\) is injective.
It is contractive precisely when \(p^*D_Np\le p^*Gp\), and can then be
extended by zero on \(\operatorname{Ran}(Z)^\perp\). This is not a physical
construction. Specifying this map through \(G^{-1}\) and asserting its
norm bound would be circular. Tensoring either the arithmetic system or
note 19's negative control by the same unit cap leaves this test unchanged.
Thus the present cap geometry cannot distinguish them; an independent
arithmetic gluing identity could. No such microscopic identity is supplied.

### D. Prime discrepancy instead of separately large terms

Section 5 rewrites the form in terms of
\(E(r)=\psi_{\rm Ch}(e^r)-e^r+1\), with
\(\psi_{\rm Ch}(x)=\sum_{p^m\le x}\log p\). The exact required lemma is
\[
-2\int_0^L e^{-r/2}\operatorname{Re}\langle F,U_rF\rangle\,dE(r)
\ge -(4+w_0)\|f\|^2-K_{\ge1}[F].
\tag{20.12}
\]
For every input this is **a restatement** of Weil positivity, not a new
proof. A useful new number-theoretic input would have to prove a stronger,
independently accessible estimate on this autocorrelation class, or on
the specified finite response family of route B. A pointwise bound on
\(|E|\) alone gives no favorable sign when integrated against a function
whose derivative changes sign. This statement does not exclude every use
of explicit prime-counting bounds together with additional structure.

This formulation distinguishes the actual atomic prime data from a smooth
control with the same leading density. Section 5 proves that the smooth
control fails. Note 19's arbitrary rational matrix need not even admit
these prescribed arithmetic kernel data. Demanding those data is
substantive; proving the required correlation inequality is still open.

## 3. The gamma boundary correction and its surviving finite-input limit

Translate the interval to \((0,L)\); translate the pole functions as well
whenever the complete form is used. Let \(H_{\rm N}\) be its Neumann
Laplacian. For \(a>0\) write
\[
u_a(x)=e^{-ax},\quad v_a(x)=e^{-a(L-x)},\quad r_a=e^{-aL},
\]
\[
\mathcal K_a=
\frac{u_au_a^*+v_av_a^*+r_a(u_av_a^*+v_au_a^*)}{1-r_a^2},
\qquad \mathcal K^{(J)}=\sum_{k=0}^{J-1}\mathcal K_{a_k}.
\tag{20.13}
\]

**Theorem 20.1 (boundary operator, domains and essential norm).**
For every \(L>0\), the increasing positive finite-rank operators
\(\mathcal K^{(J)}\) converge strongly to a bounded positive operator
\(\mathcal K_L\), and
\[
T_L=b(H_{\rm N})+\mathcal K_L,
\quad \operatorname{Dom}T_L=\operatorname{Dom}b(H_{\rm N}),
\quad \mathcal D_{\log,L}=\operatorname{Dom}b(H_{\rm N})^{1/2}.
\tag{20.14}
\]
Moreover
\[
\|\mathcal K_L\|_{\rm ess}=\frac\pi2,
\qquad
\|\mathcal K_L-\mathcal K^{(J)}\|\ge\frac\pi2
\quad\hbox{for every finite }J.
\tag{20.15}
\]
Here essential norm means distance in operator norm from the compact
operators. Finite cosine sums are an operator core for \(T_L\).

**Proof.** The free interval resolvent is the compression of the whole-line
kernel \(e^{-a|x-y|}/(2a)\). The Neumann Green function is
\[
R_{{\rm N},a}(x,y)=
\frac{\cosh(a\min(x,y))\cosh(a(L-\max(x,y)))}{a\sinh(aL)}.
\]
Subtracting gives
\(2a(R_{{\rm N},a}-R_{{\rm f},a})=\mathcal K_a\).
The coefficient matrix
\((1-r_a^2)^{-1}\left(\begin{smallmatrix}1&r_a\\r_a&1\end{smallmatrix}\right)\)
is positive. Since a gamma summand is \((2/a)I-2aR\), this proves
the finite-tower identity with the positive sign in (20.13).

Let \(n(t)=\sum_{k\ge0}e^{-a_kt}=e^{-t/2}/(1-e^{-2t})\).
The sum kernel in (20.13), away from the two corner singularities, is
\[
n(x+y)+n(2L-x-y)+\mathcal R_L(x,y),
\tag{20.16}
\]
where \(\mathcal R_L\) is bounded on the square. Indeed, all extra image
paths have length at least \(L\), and their geometric denominators are
bounded below by \(1-e^{-L}\). For example their total absolute kernel
is bounded by \(2[n(2L)+n(L)]/(1-e^{-L})\).
The function \(n(t)-(2t)^{-1}\) is bounded for \(0<t\le2L\), by its
removable expansion at zero and continuity elsewhere. Thus
\[
\mathcal K_L=\tfrac12(C_{\rm left}+C_{\rm right})+
\text{an operator with a bounded kernel},
\tag{20.17}
\]
where the two displayed kernels are \((x+y)^{-1}\) and
\((2L-x-y)^{-1}\). They are bounded: the weighted Schur test with
weight \(x^{-1/2}\) uses
\(\int_0^\infty y^{-1/2}(x+y)^{-1}dy=\pi x^{-1/2}\).
It also bounds every partial tower uniformly, by applying the positive
kernel bound to \(|f|\). Monotone bounded positive operators converge
strongly. The finite-tower form identity now proves (20.14), including
its domain equality. A bounded perturbation preserves the operator
domain and its finite cosine core.

For the essential norm, split the interval at \(L/2\). All cross blocks
in (20.17), and the opposite endpoint's kernel on each diagonal block,
are bounded kernels and hence Hilbert--Schmidt. Modulo compact operators,
\(\mathcal K_L\) is the direct sum of two half-Carleman operators on
\((0,L/2)\), so its essential norm is at most \(\pi/2\).
For the reverse bound, on the positive half-line use
\[
\phi_R(t)=\frac{t^{-1/2}1_{[1,R]}(t)}{\sqrt{\log R}}.
\]
The Carleman Rayleigh quotient tends to \(\pi\) as \(R\to\infty\): the
change to logarithmic coordinates gives convolution kernel
\([2\cosh((u-v)/2)]^{-1}\) whose integral is \(\pi\), tested on longer
normalized constant intervals. For fixed \(R\), dilate this unit vector
into \((\varepsilon,\varepsilon R)\). As \(\varepsilon\downarrow0\) it
converges weakly to zero, its Carleman quotient is unchanged, and every
compact remainder has vanishing quadratic value. First take that limit,
then \(R\to\infty\). This proves the lower essential-norm bound. Each
\(\mathcal K^{(J)}\) is finite rank, proving (20.15). \(\square\)

The Carleman calculation is consistent with [Yafaev, equations (1.2)--(1.4)](https://arxiv.org/pdf/1210.5709);
the elementary norm argument needed here was included in the proof.
This does not contradict compact resolvent of \(T_L\), which is an
unbounded logarithmic operator. Nor does it contradict note 19's compact
**source correction**, which is a different operator.

Even after removing any finite number of cosine modes the mass tail has
essential norm \(\pi/2\), since finite-codimension compression changes a
bounded operator by finite rank. Therefore treating the boundary term as
a compact or norm-small gamma remainder is not a valid repair.

**Theorem 20.2 (explicit columns and a quantitative low-input tail).**
Let \(\omega_j=j\pi/L\), \(\nu_0=L^{-1/2}\), \(\nu_j=\sqrt{2/L}\)
for \(j>0\), and \(e_j(x)=\nu_j\cos(\omega_jx)\). Then
\[
\mathcal K_a e_j=
\frac{\nu_j a}{a^2+\omega_j^2}
\bigl(u_a+(-1)^jv_a\bigr).
\tag{20.18}
\]
Opposite parities have zero matrix element; for equal parities,
\[
\langle e_i,\mathcal K_L e_j\rangle
=2\nu_i\nu_j\sum_{k\ge0}
\frac{a_k^2(1-(-1)^j e^{-a_kL})}
{(a_k^2+\omega_i^2)(a_k^2+\omega_j^2)}.
\tag{20.19}
\]
For \(P=P_N\), the finite-input operator tail obeys
\[
\|(\mathcal K_L-\mathcal K^{(J)})P\|
\le\eta_{J,N,L}:=
\sqrt{\frac{2(2N-1)}L}
\bigl(a_J^{-1/2}+a_J^{-3/2}\bigr)\longrightarrow0.
\tag{20.20}
\]

**Proof.** Direct integration gives
\[
\langle u_a,e_j\rangle
=\frac{\nu_j a(1-(-1)^jr_a)}{a^2+\omega_j^2},\qquad
\langle v_a,e_j\rangle=(-1)^j\langle u_a,e_j\rangle.
\]
Substitution in the two-by-two coefficient matrix proves (20.18), and
one more integration proves (20.19). In particular all boundary-mediated
mixed cosine coefficients are explicit. Since
\(\|u_a\|,\|v_a\|\le(2a)^{-1/2}\), each column term has norm at most
\(\sqrt2\nu_j a^{-3/2}\). The decreasing-series integral bound gives
\(\sum_{k\ge J}a_k^{-3/2}\le a_J^{-3/2}+a_J^{-1/2}\).
Sum the squared column bounds, using
\(\sum_{j<N}\nu_j^2=(2N-1)/L\). \(\square\)

Because \(P\) commutes with \(b(H_{\rm N})\), the **entire** mixed block is
\[
B=Q\mathcal K_LP+QP_L^{\rm pole}P-QJ_L^{\rm off}P.
\tag{20.21}
\]
Its gamma part is a boundary response. This is the useful structure lost
by replacing \(T_L\) with its diagonal Neumann lower comparison. It is
not legitimate to square the three terms separately and omit their cross
terms. With all pole and prime terms exact, (20.20) controls the error
from replacing \(\mathcal K_L\) in (20.21) by a finite mass sum.

## 4. A response-residual bound that keeps the mixed terms

Retain the high-sector lower comparison and define on \(QX\)
\[
\Lambda_N e_j=d_je_j,\quad
d_j=b(\omega_j^2)-\beta_L\ge\delta>0\quad(j\ge N),
\qquad H\ge\Lambda_N.
\tag{20.22}
\]

**Proposition 20.3 (certified mixed response).** For any bounded map
\(Y:PX\to\operatorname{Dom}H\), put
\[
R_Y=B-HY,\qquad U_Y=B^*Y+Y^*B-Y^*HY.
\]
Then
\[
B^*H^{-1}B=U_Y+R_Y^*H^{-1}R_Y,
\qquad
U_Y\le B^*H^{-1}B\le U_Y+R_Y^*\Lambda_N^{-1}R_Y.
\tag{20.23}
\]
For the Galerkin choice (20.8),
\(P_{N,K}R_K=0\) and \(U_{Y_K}=B^*Y_K\), giving (20.9).
These are matrix inequalities, not estimates only on real or individual
sampled inputs.

**Proof.** Expand
\((B-HY)^*H^{-1}(B-HY)\), with every factor in its order. The inverse
comparison \(H^{-1}\le\Lambda_N^{-1}\) follows from the positive form
comparison. Galerkin orthogonality gives
\(Y_K^*HY_K=Y_K^*B=B^*Y_K\). On the residual's cosine support
\(j\ge K\), \(\Lambda_N^{-1}\le d_K^{-1}I\). Substitution proves all
claims. \(\square\)

This bound handles the **infinite response** by its residual, so no inverse
tail is silently dropped. Its input data can be bounded without a large
positivity sweep. For example, for a known residual \(R\) with rows
\(r_j=e_j^*R\), any \(K>N\) gives
\[
R^*\Lambda_N^{-1}R\le
\sum_{j=N}^{K-1}\frac{r_j^*r_j}{d_j}
+\frac1{d_K}\left(R^*R-\sum_{j=N}^{K-1}r_j^*r_j\right).
\tag{20.24}
\]
Thus infinitely many mode rows are bounded by the full residual Gram,
not discarded. If a finite mass computation produces \(\widetilde R\)
with \(\|\Lambda_N^{-1/2}(R-\widetilde R)\|\le\epsilon\), the further
error in that Gram is bounded above by
\[
\bigl(2\|\Lambda_N^{-1/2}\widetilde R\|\epsilon+\epsilon^2\bigr)I.
\tag{20.25}
\]
For cosine-supported trial columns, (20.20) supplies such an error for
both \(B\) and \(HY\). Finite mass columns, poles, and the complete finite
list of translated cosine columns have elementary integrable products;
their full \(L^2\) Grams can be enclosed before (20.24) is used. The
diagonal multiplier also has the independent upper tail bound
\[
0\le b(s)-\sum_{k<J}\frac2{a_k}\frac{s}{a_k^2+s}
\le s\left(\frac2{a_J^3}+\frac1{2a_J^2}\right).
\tag{20.26}
\]
No new enclosure of the arithmetic sign is claimed in this note.

There is a useful completeness qualification. At fixed \(L,N\), the
Galerkin \(Y_K\) converge to \(H^{-1}B\) in the form norm, because finite
cosine sums form a core. Write \(H=\Lambda_N+E_N\) with \(E_N\) bounded,
as supplied by Theorem 20.1 and the bounded arithmetic remainder. Then
\[
R_K=(I-P_K)(B-E_NY_K)\longrightarrow0
\quad\hbox{in operator norm from }PX\hbox{ to }QX.
\]
Indeed the input space is finite dimensional, \(Y_K\to H^{-1}B\) in
\(L^2\), and the tail projection tends strongly to zero on each fixed
column. The right side of (20.9) therefore converges to \(S_N\).
If \(S_N>0\) at this fixed length, some finite \(K\) will certify it
with sufficiently small rigorous enclosure errors. For a semidefinite
matrix with a kernel, this eventual finite-certificate assertion is not
made: the negative residual allowance can persist on a null direction.
Neither this completeness fact nor its proof establishes the sign.

## 5. Exact prime-density cancellation and a negative control

Let \(h_f(r)=\operatorname{Re}\langle E_Lf,U_rE_Lf\rangle\).
It is continuous, vanishes for \(r\ge L\), and \(h_f(0)=\|f\|^2\).
Define the locally bounded-variation discrepancy
\[
E(r)=\psi_{\rm Ch}(e^r)-e^r+1,
\qquad \psi_{\rm Ch}(x)=\sum_{p^m\le x}\log p.
\tag{20.27}
\]
There is no atom at zero and \(E(0)=0\). Let \(K_{\ge1}\) be the gamma
tower with its lowest mass \(a_0=1/2\) omitted, **only** in the following
identity, where its contribution is accounted for exactly.

**Proposition 20.4 (discrepancy form).** On the full logarithmic domain,
\[
Q_L[f]=K_{\ge1}[E_Lf]+(4+w_0)\|f\|^2
-2\int_0^L e^{-r/2}h_f(r)\,dE(r).
\tag{20.28}
\]
For smooth compactly supported inputs it also equals
\[
K_{\ge1}[E_Lf]+(4+w_0)\|f\|^2
+2\int_0^L E(r)e^{-r/2}\bigl(h_f'(r)-h_f(r)/2\bigr)\,dr.
\tag{20.29}
\]

**Proof.** The pole form is
\(4\int_0^L\cosh(r/2)h_f(r)\,dr\). The full prime term is
\(-2\int_0^L e^{-r/2}h_f(r)\,d\psi_{\rm Ch}(e^r)\), with every
prime power counted. Subtracting its density part \(e^rdr\) from the
pole term leaves \(2\int_0^L e^{-r/2}h_f(r)\,dr\). This is precisely
the quadratic form of the kernel \(e^{-|x-y|/2}\). The lowest gamma
summand is \(4I\) minus this same kernel, proving (20.28).
All the manipulations beyond the gamma form are bounded at fixed \(L\),
so the identity holds on the full domain. Stieltjes integration by parts
gives (20.29) on the smooth core; both boundary terms vanish because
\(E(0)=0\) and \(h_f(L)=0\). Derivative regularity of an arbitrary
logarithmic-domain autocorrelation is not assumed. \(\square\)

The normalization can also be checked directly against [Suzuki's Weil
functional, section 1.1](https://arxiv.org/html/2606.09096v2#S1.SS1).
Its contact becomes \(w_0\) after writing the gamma integral as a
difference energy, using \(\psi(1/2)=-\gamma_E-2\log2\).

**Theorem 20.5 (smooth-density obstruction).** Replace the atomic measure
\(d\psi_{\rm Ch}(e^r)\) by \(e^rdr\) in the full form, retaining exactly
the original gamma term, contact and poles. Call the resulting form
\(Q_L^{\rm dens}\). It is closed and semibounded on the same logarithmic
domain and has a negative smooth compactly supported direction for every
\(L\ge2\). At \(L=2\), the unit input
\(f(x)=\cos(\pi x/2)\), \(-1<x<1\), in \(H_0^1(-1,1)\), satisfies
\[
Q_2^{\rm dens}[f]<-\frac{2979}{6125}<0.
\tag{20.30}
\]

**Proof.** In this model \(E=0\), so (20.28) gives the exact operator
\[
W_L^{\rm dens}=T_{\ge1,L}+(4+w_0)I.
\tag{20.31}
\]
For zero extensions in \(H^1(\mathbb R)\),
\[
K_{\ge1}[F]\le\left(\sum_{k\ge1}\frac2{a_k^3}\right)\|F'\|^2
\le\frac{26}{125}\|F'\|^2.
\]
The final bound is the first term at \(a_1=5/2\) plus its decreasing
integral tail: \(2/a_1^3+1/(2a_1^2)=26/125\).
The digamma special value gives
\(w_0=-\gamma_E-\pi/2-3\log2-\log\pi\).
Elementary strict bounds then give \(w_0<-5\):
\(\gamma_E>H_8-\log9>H_8-11/5=29/56>1/2\),
\(\pi>3\), \(\log2>2/3\), and \(\log\pi>1\).
Here a finite exponential sum proves \(e^{11/10}>3\), while \(e<3\).
The harmonic lower bound follows from integral comparison. These
constants and the earlier \(\pi<22/7\) proof use exact rational series.
For the displayed unit cosine, \(\|F'\|^2=\pi^2/4\), and hence
\[
Q_2^{\rm dens}[f]<-1+\frac{26}{125}\frac{(22/7)^2}{4}
=-\frac{2979}{6125}.
\]
Approximate this \(H_0^1\) input by \(C_c^\infty(-1,1)\); the strict
negative value persists. Zero extension preserves the form in every
larger support. \(\square\)

This control has the full archimedean normalization and exact pole
cancellation, and a positive leading density \(\psi_{\rm dens}(x)=x-1\).
It is a more structured negative test than an arbitrary finite matrix.
It also admits generic positive completion: choose
\(\alpha>-(4+w_0)\) and use the positive higher-mass source together
with \(\sqrt{\alpha+4+w_0}\,I\). Its Gram is
\(W_L^{\rm dens}+\alpha I\), it has compact resolvent, and a positive
high sector can be selected just as before. A unit supersymmetric cap can
be tensored into this control as well.

The excluded mechanism is specific: replace the prime measure by its
smooth leading density and treat the discarded discrepancy as a harmless
error, or use only hypotheses satisfied by that density to force the
required ordering. The theorem does not exclude methods that control the
signed correlation of the actual discrepancy with the relevant inputs.
For example, if the actual arithmetic form is nonnegative, (20.28) on
the displayed cosine requires its discrepancy contribution to exceed
\(2979/6125\); it cannot be dropped. This is a necessary conditional
bound, not a claimed new prime-counting estimate.

## 6. Arbitrary support is a theorem quantifier, not a source limit

**Proposition 20.6 (cofinal support criterion).** Let \(L_j\to\infty\).
Suppose that at each \(L_j\) some valid finite cutoff and an independent
argument prove \(S_{N_j,L_j}\ge0\). Then the complete Weil form is
nonnegative on every logarithmic-domain compactly supported input.
Conversely, full positivity implies every such Schur inequality.

**Proof.** For any finite \(L\), select \(L_j\ge L\). Zero extension to
\(I_{L_j}\) preserves the Fourier gamma form, the two pole amplitudes and
all active prime correlations. Additional distances with no overlap
contribute zero. Apply (20.1) on the larger interval. The converse is its
square-completion equivalence at each fixed support. \(\square\)

Thus a theorem proving the sufficient bound (20.9) for every \(L\), or
even a cofinal sequence of lengths, would suffice. The dimensions, trial
sizes, positive **high-sector** gaps and enclosure precision may depend
on the length. No fixed matrix dimension, positive uniform gap for the
full form, or single all-prime physical system is required. Positivity
on one fixed support alone does not extend upward: variationally the
lowest Rayleigh infimum is nonincreasing under support enlargement.

Constructing physically compatible sources across different envelopes is
a separate task. Note 19's within-envelope restriction law remains valid;
rebuilding its positive completion changes its finite error. None of
Theorems 20.1--20.5 constructs that all-envelope physical law. The earlier
stationary all-prime contact divergence still has its stated scope.

## 7. Validation, primary inputs and limitations

The existing nine standard-library programs reproduced all **49** earlier
labelled checks before this continuation. Their exact records and notes
00--19 are preserved. The new [checker](../numerics/check_arithmetic_sign.py)
tests the Green-kernel algebra and boundary derivatives, parity-column
coefficients, the ordered-tail counterexamples, mixed residual identities,
the positive-reference shift cancellation, and the rational constants in
the continuum obstruction. It does not certify compactness, domains,
infinite-dimensional limits, or the actual arithmetic matrix sign.

Primary inputs are the [digamma partial fractions](https://dlmf.nist.gov/5.7.E6)
and [special values](https://dlmf.nist.gov/5.4), the explicit Weil
functional in [Suzuki](https://arxiv.org/html/2606.09096v2), and the
Carleman model in [Yafaev](https://arxiv.org/abs/1210.5709). The new
boundary identities, domain strengthening, essential-norm argument,
residual estimates and density obstruction are derived above. The
physical discussion invokes no new Hodge or chiral theorem.

No floating-point positivity sweep, certified arithmetic support interval,
large derived dataset, assumed positive square root of the target, or
all-support Weil positivity result is claimed. The surviving next task
is **missing lemma B**, preferably with an analytical rule for the trial
response and a signed arithmetic cancellation estimate. The exact
boundary columns and discrepancy identity specify the inputs to that
task; they do not supply its answer.
