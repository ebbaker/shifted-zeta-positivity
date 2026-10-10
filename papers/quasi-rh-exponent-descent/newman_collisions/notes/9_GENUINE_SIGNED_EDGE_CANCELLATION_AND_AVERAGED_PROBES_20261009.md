# Genuine signed edge cancellation and averaged probes

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model audits are internal checks, not independent validation.

This continues [Heat Note 8](8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md)
and its [review](../../reviews/HEAT_SIGNED_SHRINKING_COLLISION_REVIEW_20261009.md).
Two estimates now use the genuine phases: the last growing short interval
has a vanishing signed value/derivative contribution, and a sufficiently
long translated average of the complete normalized heat function has
positive mean square. Neither gives a pointwise joint lower bound at a
candidate collision. A separate [multiplicative-twist theorem](10_COMPLETE_MULTIPLICATIVE_PHASE_OBSTRUCTION_20261009.md)
shows why complete multiplicativity alone does not provide that bound.

## 1. Exact interface retained from Note 8

Throughout, put

\[
1\le\kappa\le2,\quad 0<t\le1/20,\quad L=\kappa/t,\quad
x=4\pi e^L,\quad N=\lfloor\sqrt{e^L+t/16}\rfloor,
\]
\[
\mathfrak a=\kappa(4-\kappa)/16,\quad
\mathfrak b=\kappa(\kappa+4)/16,\quad
\mathfrak d=\kappa(\kappa+12)/16.
\]

All spatial derivatives hold time and the integer cutoff fixed. Write
\(Q_t=H_t/A_t\), with the symmetric zero-free analytic normalizer of the
stable manuscript, and retain its exact fixed-cutoff approximant \(F_{t,N}\).
Note 8 pays reflection, normalizer conversion, possible cutoff changes,
and the full disk/Cauchy error:

\[
\eta_N\le5e^{-\mathfrak b/t},\quad
|Q_t(x)-F_{t,N}(x)|\le\eta_N,\quad
|Q_t'(x)-F_{t,N}'(x)|\le L\eta_N.                 \tag{1}
\]

With \(s=(1-ix)/2\), \(\alpha(s)=\alpha_r+i\alpha_i\), and
\(\alpha'(s)=U+iV\), define the exact quantities

\[
w_n=e^{t\log^2n/4-(1/2+t\alpha_r/2)\log n},\quad
\phi_n=\theta_t(x)+(x-t\alpha_i)\log n/2,
\]
\[
r_n=\frac2L\Re\{(\alpha-\log n)(1+t\alpha'/2)\},\quad
c_n=\frac{tV\log n}{L},\quad z_n=r_n-ic_n.
\]

Thus

\[
\mathcal V_N=\left(F_{t,N}/2,\,2F_{t,N}'/L\right)
=\left(\Re\sum_{n\le N}w_ne^{i\phi_n},\,
        \Im\sum_{n\le N}w_nz_ne^{i\phi_n}\right).       \tag{2}
\]

The \(c_n\) term records amplitude variation. At a genuine collision,
\(Q_t(x)=Q_t'(x)=0\), so

\[
|\mathcal V_{N,1}|\le\eta_N/2,\qquad
|\mathcal V_{N,2}|\le2\eta_N,\qquad
|\mathcal V_N|^2\le17\eta_N^2/4.                  \tag{3}
\]

No arbitrary coefficient phases replace \(\phi_n\) in this note.
All asymptotic statements below are uniform in \(\kappa\in[1,2]\).

## 2. A growing signed edge can be removed with explicit errors

Let

\[
H_e=\lfloor N^{3/4}\rfloor,\qquad K=N-H_e,\qquad
s_\kappa=1/2+\kappa/8.
\]

**Proposition 1.** For every parameter point in Section 1,

\[
\left|\sum_{K<n\le N}w_ne^{i\phi_n}\right|
\le40N^{-1/24},\qquad
\left|\sum_{K<n\le N}w_nz_ne^{i\phi_n}\right|
\le\frac{800}{L}N^{-7/24}.                         \tag{4}
\]

Here both sums retain the actual logarithmic phases. In particular, define
\(F_{t,K}\) by deleting these terms from the same approximant, with the
same normalizer, and differentiate with cutoff \(K\) fixed. Then

\[
\left|\frac{Q_t-F_{t,K}}2\right|
\le\eta_N/2+40N^{-1/24},\qquad
\left|\frac{2(Q_t'-F_{t,K}')}{L}\right|
\le2\eta_N+\frac{800}{L}N^{-7/24}.                \tag{5}
\]

Thus a candidate collision forces the corresponding two coordinates
of \(\mathcal V_K\) below the right sides of (5). The analytic error is
still \(\eta_N\), followed by the exact signed subtraction in (4);
no larger positive error majorant for cutoff \(K\) is substituted.

### Proof of the exponential-sum bound

Set \(T=(x-t\alpha_i)/2\), and \(f(u)=T\log u/(2\pi)\).
The common phase \(\theta_t\) does not affect the modulus of a sum. On
\([K,N]\),

\[
f'''(u)=T/(\pi u^3),\qquad 1/N\le f'''(u)\le4/N.       \tag{6}
\]

Indeed \(N\ge22000\), \(K\ge.9N\),
\(N^2-t/16\le e^L<(N+1)^2\), and \(|\alpha_i|\le1\).
In particular \(T/\pi\le2.01N^2\) and \(2.01/.9^3<4\);
the lower bound follows from \(T/\pi\ge N^2\).

We import the explicit derivative theorem of
[J. Arias de Reyna, equation (2), with derivative order three](https://arxiv.org/html/2407.02094v1).
For an interval of length \(Y\) with \(\lfloor Y\rfloor>3\), and
\(0<\lambda\le f'''\le\Lambda\), it gives

\[
\left|\sum e(f(n))\right|
\le11\max\{Y^{3/4}(\Lambda/\lambda)^{1/4},\,
 Y(\Lambda^2/\lambda)^{1/6},\,
 Y^{1/4}\lambda^{-1/4}\}.                         \tag{7}
\]

The stated differentiability and positivity hypotheses hold in (6).
Use \(\lambda=1/N\), \(\Lambda=4/N\). Every partial interval of the
edge has \(Y\le H_e\), so (7) bounds its sum by

\[
11\max\{4^{1/4}N^{9/16},16^{1/6}N^{7/12},N^{7/16}\}
\le18N^{7/12}.                                      \tag{8}
\]

Partial intervals with at most three terms satisfy the same bound trivially.
This includes the initial intervals required by Abel summation.

### Proof of the exact coefficient-variation payment

The real-axis formulas are

\[
\alpha_r=L/2+\tfrac14\log(1+x^{-2})-(1+x^2)^{-1},\quad
\alpha_i=3x/(1+x^2)-\tfrac12\arctan x,
\]
\[
U=(7x^2-5)/(1+x^2)^2,\qquad V=x(x^2+5)/(1+x^2)^2.
\]

Write \(\delta=\log N-L/2\). The floor gives \(|\delta|\le2/N\),
and \(|\alpha_r-L/2|\le x^{-2}\). The exact endpoint identity is

\[
\log w_N+s_\kappa\log N
=\frac t4\log N\,\delta
 -\frac t2(\alpha_r-L/2)\log N.
\]

Consequently \(w_N\le1.01N^{-s_\kappa}\). On the edge the logarithmic
slope of \(w(u)\) lies between \(-.504\) and \(-.499\), hence \(w\)
decreases and \(w_K\le2N^{-s_\kappa}\). Abel summation and (8) give
\(18N^{7/12}w_K\le36N^{7/12-s_\kappa}\), which proves the first
inequality in (4) with reserve to 40, because \(s_\kappa\ge5/8\).

At the endpoint and across the edge, direct substitution gives

\[
|z_N|\le6/(LN),\qquad
z'(u)=-\frac1u\left\{\frac2L(1+tU/2)+i\frac{tV}{L}\right\},
\]
\[
\operatorname{TV}(z)\le4H_e/(LN),\qquad
\sup_{[K,N]}|z|\le10H_e/(LN).                      \tag{9}
\]

For example, \(|U|\le8/x^2\), \(|V|\le2/x\), \(x\ge11N^2\),
and \(|\alpha_r-\log N|\le2/N+x^{-2}\) prove the endpoint bound.
The derivative in (9) has modulus at most \(3/(Lu)\).
The product-variation ledger is therefore

\[
|w_Nz_N|+\operatorname{TV}(wz)
\le(6.06+28H_e)\frac{N^{-s_\kappa}}{LN}
\le40\frac{H_eN^{-s_\kappa}}{LN}.                  \tag{10}
\]

Multiplying (10) by (8) gives at most
\(720N^{1/3-s_\kappa}/L\le800N^{-7/24}/L\).
This proves (4), and (1)--(2) prove (5). Raw value and derivative
payments corresponding to (4) are respectively \(80N^{-1/24}\) and
\(400N^{-7/24}\); the scaling factors in (5) are essential.

The absolute mass of this same edge is
\((1+o(1))H_ew_N=(1+o(1))N^{1/4-\kappa/8}\).
It grows when \(\kappa<2\). Thus (4) supplies actual cancellation in a
growing set of terms. The remaining core still has \(N-o(N)\) terms.
For an edge length \(N^\beta\), the three powers in (7) give decay
if \(\beta<2/3+\kappa/8\); the strongest uniform constraint is
\(\beta<19/24\). The choice \(3/4\) leaves a strict reserve.

## 3. The long-block exponent-pair budget

For a dyadic block near \(M=e^{\vartheta L}\),
\(0<\vartheta\le1/2\), a logarithmic-phase exponent pair \((p,q)\)
gives a bound \(O(T^pM^{q-p})\) for every partial interval. Abel summation
with the exact decreasing weight gives, on the exponential scale,

\[
E_{p,q}(\vartheta,\kappa)
=p+\vartheta(q-p-1/2-\kappa/4)+\kappa\vartheta^2/4,\qquad
|\text{weighted block}|\le\exp\{L(E_{p,q}+o(1))\}.       \tag{11}
\]

The phase has derivative \(T/(2\pi u)\), so it meets the logarithmic
case of the exponent-pair definition. The endpoint block already gives a necessary threshold
for this particular blockwise tail estimate:

\[
E_{p,q}(1/2,\kappa)=\frac{p+q}{2}-\frac14-\frac\kappa{16}.
\]

A strictly vanishing bound there requires

\[
p+q<1/2+\kappa/8.                                  \tag{12}
\]

For source conventions and the surveyed convex hull \(\mathscr H\), see
[Trudgian--Yang, Sections 1.1, 1.2 and 1.4](https://arxiv.org/html/2306.05599v3).
The Bourgain pair in that survey is
\((13/84+\epsilon,55/84+\epsilon)\). Its bound in (11) has endpoint
exponent \(13/84-\kappa/16+\epsilon\ge5/168+\epsilon>0\).
The vertex definition in their Section 1.4 also implies
\(\min_{\mathscr H}(p+q)=17/21\), so the whole cited hull misses (12)
throughout the present range.

Here is the elementary minimum check. Its nine nonnegative-index
finite vertices have sums at least \(17/21\), as verified by exact
rational arithmetic in the linked checker. Reflection by the source's
\(B\) transformation preserves the sum. For its remaining vertex family
indexed by integers \(m\ge5\), the deficit from one is

\[
\frac{3m^2-7m+2}{m(m-1)^2(m+2)}
\le\frac3{(m-1)(m+2)}\le\frac3{28}<\frac4{21}.
\]

The two limiting endpoints have sum one, and convexity preserves a
linear minimum. The central vertex attains \(17/21\).
This statement is scoped to the hull explicitly defined in that cited
survey; it does not assert completeness of all later exponent-pair work.

A positive exponent in an upper bound is a deficit of that estimate,
not a lower bound proving that the actual signed block grows. The short
edge result (4) uses a shorter interval than the dyadic endpoint block.
Even a stronger tail upper bound would still require a lower bound for
the retained core in (5), conditioned on simultaneous small value and
derivative.

## 4. Complete genuine averaged probes and the Taylor-transfer deficit

This section gives a lower bound for the mean square of the **complete genuine
sum** on one sufficient spatial range. It then pays the passage to the exact
normalized heat function and explains why the available curvature budget does
not turn that average into a pointwise collision exclusion. No necessary
probe range, actual pointwise lower bound, or collision exclusion is asserted.

### Definitions and imported approximation interface

Let

\[
1\le\kappa\le2,\qquad t\downarrow0,\qquad
L=\kappa/t,\qquad x=4\pi e^L,\qquad
N=\left\lfloor\sqrt{e^L+t/16}\right\rfloor,
\]
\[
\mathfrak a=\frac{\kappa(4-\kappa)}{16},\qquad
\mathfrak b=\frac{\kappa(\kappa+4)}{16}.
\]

Every asymptotic statement is uniform in \(\kappa\in[1,2]\). All spatial
derivatives hold **time and the integer cutoff fixed**. Write
\(s=(1-ix)/2\), \(\alpha(s)=A+iB\), and \(\alpha'(s)=U+iV\). The exact formulas are

\[
\begin{aligned}
A&=L/2+\tfrac14\log(1+x^{-2})-(1+x^2)^{-1},\\
B&=3x/(1+x^2)-\tfrac12\arctan x,\\
U&=(7x^2-5)/(1+x^2)^2,\qquad
V=x(x^2+5)/(1+x^2)^2.
\end{aligned}                                                    \tag{AP1}
\]

Using the manuscript's symmetric normalizer \(A_t(z)\), set
\(Q_t=H_t/A_t\), and retain its holomorphic approximant \(F_{t,N}\).
For the terms at the center define

\[
w_n=\exp\{t\log^2n/4-(1/2+tA/2)\log n\},\qquad
\sigma=(x-tB)/2,\qquad \phi_n=\theta_t(x)+\sigma\log n,
\]
\[
c=\tfrac12(1+tU/2),\qquad
\Omega=\tfrac12\Re\{\alpha(s)(1+t\alpha'(s)/2)\},\qquad
\lambda_n=\Omega-c\log n.
                                                               \tag{AP2}
\]

In particular
\[
F_{t,N}(x)/2=\sum_{n\le N}w_n\cos\phi_n,\qquad
(\log w_n)'=-tV\log n/4,\qquad \phi_n'=-\lambda_n.
                                                               \tag{AP3}
\]

The only imported analytic approximation input is the manuscript's
holomorphic disk/reflection/cutoff interface, derived from Polymath's
effective Riemann--Siegel approximation. In the present regime a disk of
radius \(1/L\) pays the normalized remainder by
\(\eta_N\le5e^{-\mathfrak b/t}\), including a possible one-term cutoff
correction and the cost of the symmetric normalizer. Cauchy's estimate gives
\(|Q_t^{(j)}-F_{t,N}^{(j)}|\le j!\eta_NL^j\) at its center. The translation
argument below applies this interface in small disks; it does not assume a
remainder estimate on a single disk of the much larger probe radius.

### The sufficient averaged range

**Proposition 2.** There are absolute constants \(D,t_0>0\) such that, for
\(0<t<t_0\), put
\[
H_p=DLe^{2\mathfrak a/t}.
\]
Then
\[
\frac1{H_p}\int_0^{H_p}
 \left(F_{t,N}(x+y)/2\right)^2\,dy\ge\frac14,
\qquad
\frac1{H_p}\int_0^{H_p}
 \left(Q_t(x+y)/2\right)^2\,dy\ge\frac18.
                                                               \tag{AP4}
\]
Both integrands contain the complete sum or exact normalized heat function.
The proof makes no assumption on the initial phases beyond their actual
definitions; in fact its frozen mean-square bound is uniform in those phases.
This is averaged coercivity, not a pointwise nonvanishing result.

First record positive coefficient budgets
\[
S:=\sum_{n\le N}w_n=O(e^{\mathfrak a/t}),\qquad
B_1:=\sum_{n\le N}n w_n^2=O(e^{2\mathfrak a/t}),
\]
\[
w_N=O(e^{-\mathfrak b/t}),\qquad
N^2w_N^2=O(e^{2\mathfrak a/t}).                  \tag{AP5}
\]
For example, \(n=e^{L/2-v}\) gives the continuous masses
\[
e^{\mathfrak a/t}e^{-v/2+tv^2/4}(1+o(1))\,dv,
\qquad
e^{2\mathfrak a/t}e^{-v+tv^2/2}(1+o(1))\,dv
                                                               \tag{AP6}
\]
for \(S\) and \(B_1\), respectively. On \(0\le v\le L/2\),
\(tv\le\kappa/2\le1\), so their integrands are bounded by
\(e^{-v/4}\) and \(e^{-v/2}\). Monotone integral comparison, with the
first summand and the at-most-one cutoff interval included, proves (AP5).
The small possible negative endpoint value of \(v\) contributes a
negligible single interval. The errors from \(A-L/2=O(x^{-2})\) are uniform
because \(t\log n\) is bounded.

The near-zero cutoff frequency requires explicit treatment. From (AP1),
\[
\frac\Omega c=A-\frac{B(tV/2)}{1+tU/2}
 =\frac L2+\frac{t\pi}{8x}+O(x^{-2}),
\]
\[
\log\sqrt{x/(4\pi)+t/16}
 =\frac L2+\frac{t\pi}{8x}+O(t^2x^{-2}).
\]
Thus the exact phase center is
\[
M_\phi:=e^{\Omega/c}
 =\sqrt{x/(4\pi)+t/16}+O(x^{-3/2}).             \tag{AP7}
\]
The \(t\pi/(8x)\) terms agree. There is no missing \(tL/x^2\) term here:
the exact quotient \(\Omega/c\) eliminates the real-product term.
Since \(N\le\sqrt{x/(4\pi)+t/16}\), for all sufficiently small \(t\)
and all \(n<N\),
\[
\lambda_n=c\log(M_\phi/n)\ge c_0\log(N/n)>0
                                                               \tag{AP8}
\]
with an absolute \(c_0>0\). Indeed
\(\log(M_\phi/N)\ge-O(x^{-2})\), whereas
\(\log(N/(N-1))\ge1/N\). The exact difference frequencies are
\[
|\lambda_n-\lambda_m|=c|\log(n/m)|,
\qquad c=\tfrac12+o(1).                       \tag{AP9}
\]

Freeze the exact center data and temporarily omit only the last term:
\[
f_-(y)=\sum_{n<N}w_n\cos(\phi_n-\lambda_n y).
\]
The exact product identity gives a constant diagonal
\(\tfrac12\sum_{n<N}w_n^2\), difference-phase terms, and sum-phase terms,
including the oscillatory diagonal terms. Integrating any nonzero frequency
\(\omega\) over \([0,H]\) bounds its normalized contribution by
\(2/(H|\omega|)\). All adverse cross terms are paid as follows.

For \(n<m<2n\),
\[
\frac1{\log(m/n)}\le\frac m{m-n},\qquad
m w_nw_m\le C(nw_n^2+mw_m^2).
\]
Summing the harmonic denominators, and separately treating \(m\ge2n\)
where \(\log(m/n)\ge\log2\), yields
\[
\sum_{n<m<N}\frac{w_nw_m}{|\lambda_n-\lambda_m|}
 \le C(\log N)B_1+CS^2
 =O(Le^{2\mathfrak a/t}).                     \tag{AP10}
\]

For sum frequencies, if at least one index is at most \(N/2\), (AP8)
gives a positive absolute denominator, and these pairs cost \(O(S^2)\).
For the remaining pairs, write \(j=N-n\), \(k=N-m\). The exact logarithmic
slope of \(w_n\) on this half-block is bounded in magnitude by an absolute
constant, so \(w_n,w_m\le Cw_N\); also
\[
\lambda_n+\lambda_m\ge c_1(j+k)/N.
\]
Grouping by \(j+k\) gives
\(\sum_{1\le j,k\le N/2}(j+k)^{-1}\le N\). Consequently
\[
\sum_{n,m<N}\frac{w_nw_m}{\lambda_n+\lambda_m}
 =O(S^2+N^2w_N^2)=O(e^{2\mathfrak a/t}).        \tag{AP11}
\]
There is no division by the possibly near-zero \(\lambda_N\).

The complete signed expansion, with (AP10)--(AP11), proves
\[
\frac1H\int_0^H f_-(y)^2\,dy
 \ge\frac12\sum_{n<N}w_n^2
       -C\frac{Le^{2\mathfrak a/t}}H.          \tag{AP12}
\]
Since \(w_1=1\), choosing the absolute constant \(D\) large enough makes
the right side at \(H=H_p\) at least \(3/8\). Restore the omitted term,
\[
f_0(y)=f_-(y)+w_N\cos(\phi_N-\lambda_N y).
\]
The normalized \(L^2\) distance between \(f_0\) and \(f_-\) is at most
\(w_N=o(1)\). Thus the full frozen sum has the same lower bound with an
\(o(1)\) loss.

### Restoring the genuine translated phases and paying the heat remainder

The sufficient range has
\[
H_p/N=O(Le^{-\kappa^2/(8t)})\longrightarrow0,
\qquad H_p^2/x=O(L^2e^{-\kappa^2/(4t)})\longrightarrow0.
                                                               \tag{AP13}
\]
For \(0\le y\le H_p\), the spatial argument is comparable to \(x\), and
\(t\log((x+y)/(4\pi))=\kappa+o(1)\). Exact fixed-time differentiation of
(AP1)--(AP3) gives, uniformly in \(n\le N\),
\[
|(\log w_n)'|\le C/x,\qquad |\phi_n''|\le C/x.
                                                               \tag{AP14}
\]
For the second bound, \(\theta_t''=-1/(4x)+O(x^{-2})\), while
\(\sigma''\log n=O(t\log n/x^3)\); since \(t\log n\) is bounded,
the latter is smaller. Hence Taylor's theorem and (AP5) give
\[
\sup_{0\le y\le H_p}
 \left|F_{t,N}(x+y)/2-f_0(y)\right|
 \le CS(H_p/x+H_p^2/x)
 =O\!\left(L^2e^{(5\mathfrak a-\kappa)/t}\right)=o(1).
                                                               \tag{AP15}
\]
The last exponent is uniformly negative:
\[
5\mathfrak a-\kappa
 =\frac{\kappa(4-5\kappa)}{16}\le-\frac1{16}.
                                                               \tag{AP16}
\]
This controls the complete sum, including its exponentially large absolute
mass. The normalized \(L^2\) triangle inequality now gives the first part
of (AP4).

To pay the actual heat function on the physical interval, use at every
center \(z_y=x+y\) the small disk of radius
\(R_y=1/L_y\), where \(L_y=\log(z_y/(4\pi))\), with the same time and
fixed cutoff \(N\). By (AP13), the change in the continuous cutoff across
the whole interval, including these disk radii, is \(o(1)\). The possible
natural integer cutoffs differ from \(N\) by at most one. Pay that single
coefficient in the existing holomorphic majorant. Its symmetric-normalizer
factor is still \(K_*<1.3\); reflection is part of the disk proof.

For clarity about the endpoint \(\kappa=2\), the translated parameter is
\(\kappa_y=tL_y\in[1,2+o(1)]\). The strict reserves in the small-disk
ledger persist uniformly for \(1\le\kappa_y\le2.01\): the coefficient
mass integral is at most
\(1/(1/2-2.01/8)<4.03\), still within the reserve of five; and the
numerator for the local \(U_n\) error is at most
\(2.01^2/16+.626+o(1)<.879\), still within the relaxed \(.9/x\) bound.
The remaining normalizer, cutoff, and Cauchy bounds keep their original
strict margins. Equivalently, one may allow a larger absolute prefactor;
only the uniform \(O\)-bound is used here. Since
\[
\frac{\mathfrak b(\kappa_y)-\mathfrak b(\kappa)}t=O(H_p/x)=o(1),
\]
this proves
\[
\sup_{0\le y\le H_p}|Q_t(x+y)-F_{t,N}(x+y)|
 =O(e^{-\mathfrak b/t})=o(1).                 \tag{AP17}
\]
This argument explicitly pays the physical translations and \(A_t\)
normalization. It never applies the small-disk bound to a radius \(H_p\)
disk. A final normalized \(L^2\) triangle inequality proves the second
part of (AP4).

### Paid curvature and the local-to-average deficit

The preceding averaged lower bound does not exclude a common zero of
\(Q_t,Q_t'\). To quantify the missing transfer, the same coefficient
calculation gives a usable second-derivative majorant.

Put \(d_n=(\log w_n)'\). At any point of the physical interval,
\[
\partial_x^2(w_ne^{i\phi_n})
 =w_ne^{i\phi_n}\{d_n'+d_n^2-\lambda_n^2
                 -i(\lambda_n'+2d_n\lambda_n)\}.
                                                               \tag{AP18}
\]
Here \(d_n=O(x^{-1})\), \(d_n'=O(x^{-2})\), and
\(\lambda_n'=O(x^{-1})\), uniformly in \(n\). The weighted moments
\(\sum w_n|\lambda_n|^j\) have the following asymptotic for each fixed
integer \(j\ge0\):
\[
\sum_{n\le N}w_n|\lambda_n|^j
 =(2j!+o(1))e^{\mathfrak a/t}.                \tag{AP19}
\]
Indeed (AP6) and \(\lambda_n=v/2+o(1)\) on bounded logarithmic blocks
give the limiting integral
\(\int_0^\infty(v/2)^je^{-v/2}\,dv=2j!\). First truncate to a fixed
bounded \(v\)-interval, where the mesh is exponentially small. Then use
the uniform majorant \(C_j(1+v)^je^{-v/4}\) for the remaining mass; the
first-summand integral-comparison error is \(O(L^j)\), negligible compared
with \(e^{\mathfrak a/t}\). This establishes the uniform limit. The same
proof works at translated centers because \(L_y-L=o(1)\) and any fixed
cutoff correction is exponentially small.

Equations (AP18)--(AP19) give the complete absolute curvature budget
\[
|F_{t,N}''(x+y)|
 \le(8+o(1))e^{\mathfrak a/t},\qquad 0\le y\le H_p.
                                                               \tag{AP20}
\]
All drift and frequency-variation terms in (AP18) have
\(o(e^{\mathfrak a/t})\) total mass. At each translated small-disk center,
the holomorphic remainder payment gives, for every fixed \(j\),
\[
|Q_t^{(j)}-F_{t,N}^{(j)}|
 \le j!\eta_{N,y}L_y^j
 =O(j!L^je^{-\mathfrak b/t}).                 \tag{AP21}
\]
In particular there is an absolute \(C_2\) such that
\(|Q_t''|\le M_2:=C_2e^{\mathfrak a/t}\) on the whole physical interval.
Higher-derivative payments therefore do not hide an uncharged error term.

At a hypothetical genuine collision at its left endpoint,
\(Q_t(x)=Q_t'(x)=0\), Taylor's theorem gives
\[
|Q_t(x+y)|\le M_2y^2/2,
\qquad
\frac1H\int_0^H(Q_t(x+y)/2)^2\,dy
 \le M_2^2H^4/80.                            \tag{AP22}
\]
With the proved majorant, a small constant upper bound in (AP22) is
available only on the scale \(H=O(e^{-\mathfrak a/(2t)})\), whereas
the sufficient averaged lower-bound range used here is
\(H_p=DLe^{2\mathfrak a/t}\). Their ratio grows like
\[
L e^{5\mathfrak a/(2t)}.
\]
At \(H=H_p\) the Taylor upper bound grows exponentially and gives no
contradiction to (AP4).

This is a deficit of the **proved averaged estimate plus the paid absolute
curvature budget**, not a necessary-range theorem for every correlated
probe, nor a lower bound on the actual curvature of a candidate collision.
A sharper estimate conditional on both small collision coordinates might
behave differently. The exact averaged inequality retains the complete
genuine sum but has no pointwise force by itself; isolated double zeros are
compatible with positive averaged energy even for elementary trigonometric
sums. A continuation still needs a local signed implication using the
actual arithmetic phases, or a new transfer principle stronger than these
absolute Taylor payments.

## 5. Checkpoint and next local input

The new actual-phase contributions are the explicit paid core reduction
(5) and the complete translated mean-square lower bound (AP4). The latter
uses the actual amplitude and phase evolution, pays all cutoff and
normalizer errors, and needs no numerical phase sampling. The surveyed
exponent-pair budget is a method deficit; the independent multiplicative
twist obstruction is a separate relaxation theorem in Note 10.

A sufficient next input can now be stated for the retained genuine core.
Put

\[
\epsilon_0=\eta_N/2+40N^{-1/24},\qquad
\epsilon_1=2\eta_N+800N^{-7/24}/L.
\]

Uniformly proving

\[
|\mathcal V_{K,1}|>\epsilon_0
\quad\text{or}\quad
|\mathcal V_{K,2}|>\epsilon_1
\]

would exclude a collision in the present range. This is a local signed
condition on the same genuine phases and fixed-time derivatives, not a
claim that the core has been shown nonzero. Alternatively, one can keep
the complete sum and seek the strict reverse of (3). A useful continuation
would improve the central signed arithmetic or prove an implication
conditioned on both small coordinates; the existing absolute Taylor
conversion of the averaged bound does not do that.

The [standard-library checker](../../numerics/check_genuine_signed_heat_input.py)
and [small record](../../numerics/genuine_signed_heat_input_record_20261009.json)
check exact exponent identities, scalar reserves, finite monotone group
discrepancies, and formal multiplicative orthogonality. They evaluate no
heat function or enormous cutoff and prove neither the imported analytic
estimates nor the limiting prime counts. The mathematical arguments and
imported theorems remain proof inputs. See the
[scoped review](../../reviews/HEAT_GENUINE_SIGNED_INPUT_REVIEW_20261009.md).
No RH, actual collision, or literature-novelty claim is made.
