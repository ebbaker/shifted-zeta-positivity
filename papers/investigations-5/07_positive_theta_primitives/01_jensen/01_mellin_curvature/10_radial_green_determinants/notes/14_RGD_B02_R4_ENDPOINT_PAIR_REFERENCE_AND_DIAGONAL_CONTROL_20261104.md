# RGD-B02 r4: endpoint-matched pair reference and a diagonal control

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6-astra / ultra**, continuing
chat0007, thread `01a1a819-6502-7722-93b6-a63794209eda`, turn
`01a1a884-aace-7902-ad64-f6ed9468a14e`.
Type **B**, author-activated under [Handoff19][input].
[Review11][review] records author/same-model checks, not independent
specialist review. No numerical work or enlarged zero prefix.

## 1. Return and its limits

One primary mechanism is examined: replace each nonreal conjugate pair
in the **complete** genus-zero product by a repeated positive pair,
chosen to preserve its endpoint value. All real factors and multiplicities
remain. No localized adjustment is used.

The reference has strictly positive rectangular margins in every dimension
and exactly matches C(0) and C(1). Its positive-axis growth differs from
the canonical source by at most a bounded multiplicative factor. Thus
this construction genuinely removes Note12's Gaussian growth mismatch.
It is an algebraic spectral reference: a positive cosh-transform source
or positive Green primitive for it is **not** constructed. Its full zero
parameters are implicit mathematical data, not a newly acquired spectrum.

The complete scalar coefficient residual is paid by (9), and the whole
pair Schur expansion gives the explicit finite-order margin (12).
That finite-order mechanism is classical sector positivity, not new
canonical coverage. Its pairwise sign premise cannot hold at every
order for a fixed nonzero angle.

A stronger control makes the growing-dimension limitation precise. For
arbitrarily large q there are complete algebraic products with the same
c0 and b, positive coefficients, an infinite positive tail, the canonical
leading radial zero count, and a paired residual allowance O(q^(-2)),
yet their (q,q) determinant is negative. These controls can also obey
the critical-strip geometry for sufficiently large q. They are not
asserted to have a positive smooth theta-type source or theta arithmetic.
They refute a transfer based only on the stated spectral/endpoint/growth
and scalar smallness data, not positivity of the actual theta determinant.
The family depends on q; one fixed control with infinitely many negative
diagonal minors is not proved.

This is a scoped reference/estimate result and information-sufficiency
stop under [avoid/01][a01], [02][a02] and [07][a07]. The all-pair-sign
condition at every degree is an RH reformulation for theta and is stated
once below, not promoted by finite checks. Read the [result index][results],
[control cluster12][controls] and [avoid index][avoid], especially
[12][a12] and [16][a16]. No novelty or new theta-positivity range is claimed.

## 2. Complete product, multiplicity and the pair map

Keep the accepted source and normalization:
\[
 C(z)=\int_0^\infty\Phi(u)\cosh(u\sqrt z)\,du
 =\tfrac18\xi((1+\sqrt z)/2),\quad
 C(1)=b=\tfrac1{16},\quad c_0=C(0)\in(1/32,b),
 \quad E=C/c_0=\sum_{m\ge0}e_mz^m.
 \tag{1}
\]
The full unit-weight infinite theta square source and its primitive
remain the target: p''-p=8 Phi, p'(0)=-1/2,
d0=8(b-c0). All coefficient sequences used below are zero at negative
indices. Let B_*=E(1)=b/c0, so 1<B_*<2.

The classical order-one-half Hadamard product is
\[
 E(z)=\prod_j(1+x_jz),\qquad x_j=\alpha_j^{-1},\quad
 \alpha_j=-(2\rho_j-1)^2,\qquad\sum_j|x_j|<\infty.
 \tag{2}
\]
Index xi zeros rho_j with Im rho_j>0, counted with multiplicity. This
selects one member of each functional-equation pair; indexing all xi
zeros would double the factors. Upper-half-plane reflected zeros give
conjugate alpha pairs; critical-line zeros give positive alpha entries.
[References04][refs] records the checked order/product, symmetry and
count sources. No simplicity is assumed.

For rho=sigma+i gamma, write delta=2sigma-1. Then
|alpha|=4gamma²+delta² and
|arg alpha|=2 arctan(|delta|/(2gamma)). The inherited published
zero-height information from [Note10][note10] gives gamma>14; it is
reused, not enlarged or replayed. Together with |delta|<1 this gives
Re x_j>0 and a common angle bound below pi/2.

Keep positive real x_j unchanged. For each nonreal conjugate pair write
x=s exp(i theta), its conjugate=s exp(-i theta), s>0,
0<theta<pi/2, and define
\[
 y=\sqrt{1+2s\cos\theta+s^2}-1,\qquad
 d=s^2-y^2,\qquad
 F(z)=1+2s\cos\theta\,z+s^2z^2,\quad G(z)=(1+yz)^2.
 \tag{3}
\]
Direct algebra gives
\[
 s\cos\theta\le y<s,\quad d>0,\quad
 F-G=d\,z(z-1),\quad {d\over y^2}\le\tan^2\theta.
 \tag{4}
\]
In particular F(0)=G(0)=1 and F(1)=G(1). Construct E_0 from all kept
real factors and all G factors. Its positive alphabet (a_j) is summable,
since y<=s, and infinite. Both E_0 and E converge locally uniformly;
\[
 E_0(0)=1,\qquad E_0(1)=B_*,\qquad C_0=c_0E_0.
 \tag{5}
\]
This retains the target's boundary values without altering its source.
Endpoint matching does not establish a nonnegative source realization
for C_0. Nor does (2) provide numerical access to every zero.

## 3. Growth matching, positive margins and full residual payment

For R>=1 each pair quotient F(R)/G(R) increases from one to s²/y².
Moreover
\[
 0\le2\log(s/y)\le-2\log\cos\theta\le\tan^2\theta.
\]
The strip bound gives tan theta<=2/gamma using gamma>14. Ordinary
multiplicity zero counting gives sum gamma^(-2)<infinity. Hence
\[
 V:=\prod_{\mathrm{pairs}}{s^2\over y^2}
 \le\exp\!\left(\sum_{\mathrm{pairs}}\tan^2\theta\right)<\infty,
 \qquad 1\le {E(R)\over E_0(R)}\le V\quad(R\ge1).
 \tag{6}
\]
Dominated convergence of the logarithms gives E(R)/E_0(R)->V as
R tends to infinity. Because both functions have nonnegative coefficients,
their maximum moduli on a circle equal their positive-axis values.
Thus the bounded-factor match concerns the full maximum-modulus growth,
not merely the order label. This removes the specific Gaussian-scale
obstruction, but does not estimate a determinant ratio.

For r,k>=1 put n=rk, A_ij=e_(k+j-i), A0_ij=[z^(k+j-i)]E_0(z).
Elementary/complete rectangular duality gives
\[
 \det A=s_{(r^k)}(x),\qquad
 m_{r,k}:=\det A_0=s_{(r^k)}(a)
 \ge(a_1\cdots a_k)^r>0.
 \tag{7}
\]
Any enumeration of the positive alphabet can be used for the lower
bound. In a finite product with at least k factors, bidiagonal
Cauchy--Binet supplies the term (a1...ak)^r; all other terms are
nonnegative. Pass to the locally uniform limit. Repeats are allowed;
zero negative-index entries remain exact. The inequality is explicit
in the reference parameters, not a numerically evaluated canonical margin.

The full signed residual has an exact meromorphic quotient identity,
with the entire product identity understood across removable products:
\[
 E=E_0\prod_{\mathrm{pairs}}
 \left(1+{d\,z(z-1)\over(1+yz)^2}\right).
 \tag{8}
\]
It retains each pair's two endpoint cancellations before estimating.
There is also a complete, all-radius coefficient payment. If
E-E_0=sum epsilon_m z^m, then
\[
 \boxed{\sum_{m\ge0}|\varepsilon_m|R^m
       \le (V-1)E_0(R)\qquad(R\ge0).}
 \tag{9}
\]
To prove it, first expand the exact difference of finite products in
F=G+d z(z-1). Taking coefficient absolute values is bounded by replacing
each selected z(z-1) by z(z+1). The resulting sum is
E_0(R)[product(1+d R(R+1)/(1+yR)^2)-1]. Here y<=s<1/784,
so y<=2 and R(R+1)/(1+yR)^2<=1/y². This gives (9), and summability
permits passage to the complete product. Real factors are common and
positive. The endpoint cancellations remain present in (8), although
(9) pays their absolute coefficient envelope. No source mode is omitted.
Small V-1 controls this scalar residual; it is not by itself a payment
for the sign-sensitive determinant.

## 4. Exact pair branching and the bounded-order payment

Classical Schur branching into disjoint alphabets expresses the complete
Schur polynomial as a sum with nonnegative integer coefficients of
products of the Schur polynomials of each pair and each real variable.
One justification is restriction of the polynomial GL representation
to its block groups; complete reducibility gives nonnegative multiplicities.
The character identification is recorded in the checked Etingof source
in [References04][refs]. This is standard algebra, not a theta estimate.

For a two-variable partition nu=(a,b), a>=b>=0, set ell=a-b+1.
The exact pair multiplier is
\[
 R_\nu={s_\nu(se^{i\theta},se^{-i\theta})\over s_\nu(y,y)}
 =\left({s\over y}\right)^{a+b}
       {\sin(\ell\theta)\over\ell\sin\theta}.
 \tag{10}
\]
This follows from the two-variable alternant, including equal-variable
limits. Terms of length more than two vanish for both pairs and are
omitted. Evaluating the branching expansion on the positive reference
and dividing by m_(r,k) makes det A/m_(r,k) a nonnegative weighted
average, with weights summing to one, of products of (10). This is an
exact complete-pair correlation identity, not an assertion of its sign.
Finite products prove it first; the bounds below pass to the infinite
product.

Let Theta=sup theta over nonreal pairs, with Theta=0 if there are none.
Every pair partition in branching of (r^k) has a<=r: an individual
variable has degree at most r in this Schur polynomial, and a is a
highest-weight exponent of its component. Nonnegative character
multiplicities cannot cancel such a highest-weight monomial. Hence
ell<=r+1. If
\[
 (r+1)\Theta<\pi,\qquad
 \kappa_r={\sin((r+1)\Theta)\over(r+1)\Theta}>0
 \quad(\kappa_r=1\text{ if }\Theta=0),
 \tag{11}
\]
then sinc decreases on (0,pi), sin(theta)<=theta, and y<=s<=y sec Theta
give the lower bound kappa_r<=R_nu. For the upper bound, the finite
geometric sum gives |sin(ell theta)|<=ell sin(theta), hence
R_nu<=sec(Theta)^(a+b). For nonempty blocks these bounds apply. There are
at most n=rk nonempty blocks and their degrees sum to at most n.
Therefore
\[
 \boxed{\kappa_r^{rk}\le{\det A\over m_{r,k}}
                  \le\sec(\Theta)^{rk},\qquad
 D_{r,k}\ge c_0^r(a_1\cdots a_k)^r\kappa_r^{rk}>0.}
 \tag{12}
\]
The scalar determinant residual is consequently paid by
max(1-kappa_r^(rk), sec(Theta)^(rk)-1) times the reference margin.
This allowance need not be below one; the signed lower bound is the
positivity statement. Real factors and every pair remain in the sum.

Equation (12) is a bounded-order sector mechanism of the classical
Schoenberg type, already applied to xi coefficients in Katkova. It is
not new canonical coverage, and no finite-order integer threshold or
numerical test is sought here. It permits k to grow with bounded r;
it gives no unbounded-r step unless a correspondingly stronger angular
input is supplied. For fixed nonzero Theta, (11) eventually fails.

More sharply, for any single nonzero theta, the pair's complete
coefficient is
\[
 h_j=s^j{\sin((j+1)\theta)\over\sin\theta},\qquad
 h_j^{\rm ref}=(j+1)y^j>0.
 \tag{13}
\]
At j=floor(pi/theta) the first quantity is negative. Thus requiring
every pair block to have nonnegative sign at every degree fails for any
nonreal pair. For the canonical product that all-degree block premise
is exactly global zero reality (RH), without simplicity. It is not an
acquired input. A negative individual block does not force a negative
complete canonical Schur sum: other branches may compensate.

## 5. A complete diagonal control with arbitrarily small scalar payment

This section disproves an information-only transfer rule in a larger,
explicitly algebraic class. It does not substitute a control for theta.
Fix the same B_*=b/c0 in (1,2). For q>=26 set
\[
 r=k=q,\quad m=q-1,\quad \theta_q={9\pi\over4q+8}.
\]
Choose the unique s>0 such that
\[
 (1+4s)^m(1+2s\cos\theta_q+s^2)=B_*.
 \tag{14}
\]
The left side starts at one, increases strictly and tends to infinity.
Let the finite alphabet be
X={s exp(i theta_q),s exp(-i theta_q),4s repeated m times},
with N=q+1 entries and positive product P. For any such N-entry
alphabet, elementary coefficient reversal e_(N-j)(X)=P e_j(X^(-1)),
transposition and the k=1 duality give
\[
 \det[e_{q+j-i}(X)]_{i,j<q}=P^q h_q(X^{-1}).
 \tag{15}
\]
Out-of-range coefficients on both sides of reversal are zero.
Repeated entries cause no division problem.

After factoring s^(-q), the sign is that of
H_q=h_q(exp(i theta_q),exp(-i theta_q),1/4 repeated m times).
Let Y be the nonnegative integer variable with probability generating
function ((3/4)/(1-w/4))^m. Direct differentiation gives
mu=E Y=m/3 and Var Y=W=4m/9. Coefficient extraction using (13) gives
\[
 H_q={(4/3)^m\over\sin\theta_q}
 E\left[\sin((q+1-Y)\theta_q)\,1_{Y\le q}\right].
 \tag{16}
\]
This is an exact series identity, not a simulated distribution.
Because (q+1-mu)theta_q=3pi/2, cos x>=1-x²/2 and Chebyshev's
variance inequality imply
\[
\begin{split}
 E[\sin((q+1-Y)\theta_q)1_{Y\le q}]
 &\le-1+\tfrac12\theta_q^2W+\Pr(Y>q)\\
 &\le-1+\tfrac12\theta_q^2W+{W\over(q-\mu)^2}
 <-1+{13\over q}\le-\tfrac12.
\end{split}
 \tag{17}
\]
Indeed the two positive terms are less than 11.25/q and 1/q,
respectively, using pi²<10. Thus the (q,q) determinant in (15) is
strictly negative. This is a growing diagonal, not an edge-only witness.

Complete the product with an infinite positive tail
\[
 Q_J(z)=\prod_{j>J}(1+u_jz),\qquad
 u_j=\left({\log j\over4\pi j}\right)^2,\qquad J\ge3.
 \tag{18}
\]
Since sum u_j converges, Q_J tends locally uniformly to one as J tends
to infinity. For each fixed q choose J sufficiently large that Q_J(1)<B_*;
choose s_J>0 by replacing B_* in (14) by B_*/Q_J(1). Then s_J->s,
and the complete product
\[
 E_q(z)=(1+4s_Jz)^m F_{s_J,\theta_q}(z)Q_J(z)
 \tag{19}
\]
has E_q(0)=1, E_q(1)=B_* and positive coefficients. Its fixed (q,q)
determinant stays negative for all sufficiently large J, by coefficient
continuity and the strict gap (17). No effective cutoff J(q) is evaluated
or interval-certified. This is an analytical existence construction.

The tail zeros are -(4pi j/log j)^2. Elementary inversion of this
sequence gives, for every fixed J,
\[
 n_{Q_J}(R)\sim {\sqrt R\log R\over8\pi}.
 \tag{20}
\]
Indeed j/log j<=sqrt(R)/(4pi) inverts to
j~sqrt(R)log(R)/(8pi). The convergence exponent of the zeros is one-half;
also u_j=O(j^(-2+epsilon)) for every epsilon>0, and splitting the
positive product bounds its order from above by 1/(2-epsilon). The count
bounds it from below by one-half. Thus its order is exactly one-half.
Finite factors do not change this leading radial count, which matches
the canonical count in Note10. The tail has genus zero and order one-half;
there is no Gaussian growth mismatch. Reference E_(0,q) replaces only
the one pair in (19) by (1+yz)^2 and keeps every other factor. It has
strictly positive reference minors and the same two endpoints.

Here y<sqrt(B_*)-1<1. The coefficient-envelope proof of (9) therefore
yields, with Delta e denoting the **complete** coefficient difference,
\[
 \boxed{\sup_{R\ge0}
 {\sum_{j\ge0}|\Delta e_j|R^j\over E_{0,q}(R)}
 \le {s_J^2-y^2\over y^2}\le\tan^2\theta_q=O(q^{-2}),
 \quad \det[e_{q+j-i}(E_q)]_{i,j<q}<0.}
 \tag{21}
\]
The same bound controls |E_q(R)/E_(0,q)(R)-1| on the entire positive
axis. Both endpoint cancellations are exact. Thus arbitrarily small
uniform scalar coefficient payments, growth matching and positive
reference margins do not imply determinant positivity uniformly in
unbounded diagonal dimension. A dimension-dependent sufficient condition
with a more restrictive rate/constant is not excluded.

The artificial complex pair need not violate strip geometry. Without
the tail, s~log(B_*)/(4q). Choose J(q) still larger if necessary so
s_J/s->1 along the family. Then
\[
 {\sin(\theta_q/2)\over\sqrt{s_J}}\to0,\qquad
 \gamma_q={\cos(\theta_q/2)\over2\sqrt{s_J}}\to\infty.
\]
Writing |2sigma-1|=sin(theta_q/2)/sqrt(s_J) realizes the pair as
reciprocals of -(2rho-1)^2 inside 0<sigma<1 for all sufficiently large q.
Real tail and repeated positive entries similarly lie on the critical
line under this algebraic mapping. This is only zero geometry, not an
actual xi/Dirichlet source. No actual finite zero prefix is asserted
preserved by this family.

## 6. Control screen and precise failed premises

The positive cosh control from [Note12][note12] has Theta=0; its pair
reference is itself and every rectangle remains positive. The new map
therefore does not wrongly stop that control merely for its order.
Note10's Gaussian-mixture finite-prefix example still shows that a
verified finite real-simple packet alone cannot establish global reality.

The new diagonal family shares endpoint values, positive coefficients,
summable paired spectral data, leading radial count, arbitrarily small
complete scalar payment and, eventually, strip geometry. It fails the
canonical complete square-source/Dirichlet identity. A nonnegative smooth
cosh-transform source or positive Green primitive is **not established**
for it. Accordingly (21) does not refute an estimate that uses additional
canonical arithmetic correlations or positive-source structure not
encoded in those retained data. It also does not prove a negative theta
determinant or a positive-time collision.

The existing cluster12 controls keep their separate premise failures:

| Control family | Canonical premise not retained |
| --- | --- |
| Euler-factor shifts | Unmodified theta coefficients/source |
| Weighted-square and finite sources | Full unit-weight infinite sum and full reflection |
| Reflected super-Gaussian and positive-primitive shapes | Canonical arithmetic square expansion |
| Finite-prime or finite-profile constructions | Complete source identity rather than selected data |
| BW-01 atoms | Smooth canonical source and full profile |
| RH-conditional endpoint controls | Ordinary theta Dirichlet-series arithmetic |
| Variable observation kernels | Actual cosh/cosine transform equation |

Their failure of an exact-source premise does not establish failure of
a derived quantitative estimate. Positive-time events do not refute
arbitrary time-zero inequalities. No collision tests or finite-prefix
numerics were run.

The retained scalar data cannot justify a dimension-uniform positivity
transfer: (21) is a counterexample to that proposed premise in its named
class. The separate all-degree pairwise sign premise requires RH for
actual theta. Neither statement excludes complete signed compensation
between branches, a more informative dimension-dependent bound, or a
new canonical arithmetic estimate.

## 7. Disposition, sources and continuation

**RGD-B02 r4 complete as a scoped conceptual return.** The reference
now matches growth and endpoints and has a nonzero growing-dimension
margin. A complete scalar residual payment and a bounded-order signed
margin are available, but the latter is classical finite-order territory.
The attempted generic small-angular-defect transfer stops by the explicit
diagonal construction. No new canonical growing-r positivity step or
all-index induction has been obtained. No localized adjustment was used.

[References04][refs] records inspected product, count, Chebyshev,
Schur-character and classical sector sources. Its qualification about
a displayed integer mismatch in Katkova's PF44 argument is not a finding
that PF44 is false; the present proof imports no numerical cutoff from
that argument and does not rewrite earlier frozen assessments. A full
literature/priority or external certificate audit was not performed.

**Next: [E] RGD-E04 r7 — Sol**, the fixed assessment in [Packet20][packet].
It checks (2)--(21), multiplicities, uniformity, the infinite-tail existence
argument and the exact class of the controls. No numerical acquisition
is justified. [Handoff21][guide] gives model-change continuity. A later
B02 r5 would need an author-activated estimate using information absent
from the diagonal controls, rather than further scalar growth or angle
matching. No such new mechanism is issued here. This is no manuscript
milestone or closure of the investigation.

[input]: ../research-progress/handoffs/19_RGD_E04_R6_RETURN_AND_MODEL_CONTINUATION_20261104.md
[note10]: 10_RGD_B02_R2_RECIPROCAL_POLE_INDUCTION_AND_SCOPED_STOP_20261104.md
[note12]: 12_RGD_B02_R3_GAUSSIAN_REFERENCE_GROWTH_STOP_20261104.md
[review]: ../reviews/11_RGD_B02_R4_AUTHOR_AND_SAME_MODEL_CHECKS_20261104.md
[refs]: ../references/04_PAIR_PRODUCT_SECTOR_AND_CONTROL_SOURCES_20261104.md
[packet]: ../research-progress/handoffs/20_RGD_E04_R7_PAIR_REFERENCE_ASSESSMENT_20261104.md
[guide]: ../research-progress/handoffs/21_RGD_B02_R4_RETURN_AND_MODEL_CONTINUATION_20261104.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
