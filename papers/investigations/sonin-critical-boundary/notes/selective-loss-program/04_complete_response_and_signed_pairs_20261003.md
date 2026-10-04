# Complete response energy and the signed prime-pair target

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Separate agents using the inherited
model configuration checked the causal identity, projection, prime-pair
kernel, explicit formula, and numerical decomposition. These are internal
same-model checks, not independent specialist refereeing. No global
polynomial estimate or RH proof is claimed.

This continues the [centered dual-energy target](03_centered_dual_energy_20261003.md).
There is a useful sharper reduction: the diagonal prime energy already has
polynomial growth. The remaining sufficient estimate is an upper bound on
the **aggregate signed off-diagonal energy**, after all pairs in a complete
window have been combined. Individual positive pair terms cost
exponentially and cannot supply that bound.

## 1. One local signal, with the complete upper window

Put a=1/4 and ell=2a=1/2. Keep the normalized real odd g from the previous
notes and define the locally finite causal signal

\[
p(y)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(y-\log n),
\qquad J(Y)=\int_0^Y p(y)^2\,dy.
\tag{1}
\]

It vanishes for y<=log 2-a>a. In particular no initial-endpoint correction
is needed in the causal formulas below. At a given Y every contributing
prime power has log n<Y+a. That full final band is retained.

On the centered source interval I_r=(-r/2-a,r/2+a), set y=x+r/2.
Oddness of g converts the two moving responses into

\[
w_r(x)=\frac{p(y)-p(r-y)}{\sqrt2},
\qquad -a<y<r+a.
\tag{2}
\]

This is the complete response for L=r+ell: both terms use only prime
powers with log n<L. For r>ell it is the response of the normalized
prepared source F_r. The same response formula can be used for 0<=r<=ell
when deriving integral identities; the associated two-packet source then
need not have norm one. That compact range has no effect on a tail growth
criterion.

The continuous-density signal is

\[
p_0(y)=\int_0^\infty e^{u/2}g(y-u)\,du
=v(y),\qquad
v=\frac{-h''-h'/2}{\sqrt\nu}.
\tag{3}
\]

It is supported in [-a,a] by the prepared exponential moment. Therefore
the discrepancy d=p-v equals p for y>a. For Y>=a its cumulative squared
energy and J differ by a fixed initial-cap constant: p is zero throughout that
cap, so the cross term there vanishes. The complete discrepancy response
is [d(y)-d(r-y)]/sqrt2. Its continuum part has the previously proved fixed
squared norm 917180/580421327.

Thus J applies the signed compact smoothing before taking a square. It
can be sharper than the unsmoothed Chebyshev-error comparison in the
previous note; no estimate for J is obtained merely by this change.

## 2. Exact norm, convolution, and moment subtraction

Let N(r)=||w_r||_2^2, without the prepared moment projection. Reflection
of [-a,r+a] gives

\[
\boxed{N(r)=J(r+a)-(p*p)(r),\qquad
(p*p)(r)=\int_0^r p(y)p(r-y)\,dy.}
\tag{4}
\]

For real odd g, g*g=-phi, so the cross term also has the finite arithmetic
formula

\[
(p*p)(r)=-
\sum_{n,m\ge2}\frac{\Lambda(n)\Lambda(m)}{\sqrt{nm}}
             \phi(\log n+\log m-r).
\tag{5}
\]

All terms with nonzero kernel are present. This reflected cross term is a
signed product correlation; it must not be replaced silently by a sum of
absolute prime amplitudes.

Define

\[
J_\pm(Y)=\int_0^Y e^{\pm y/2}p(y)\,dy,\qquad
d_r=\sinh((r+\ell)/2)-(r+\ell)/2>0.
\]

The exact sinh moment is

\[
m_r=\int_{I_r}\sinh(x/2)w_r(x)\,dx
=\frac{e^{-r/4}J_+(r+a)-e^{r/4}J_-(r+a)}{\sqrt2}.
\]

The full projected energy is consequently

\[
\boxed{R_{\rm ar}(r)=J(r+a)-(p*p)(r)-m_r^2/d_r.}
\tag{6}
\]

The constant and cosh moment directions are even and do not contribute.
Both J_+ and J_- vanish on every fully included packet because g has both
prepared exponential moments. Only packets with r<log n<r+ell contribute
to these moment integrals. This localizes the subtraction; it does not
authorize dropping that top band.

There are two useful inequalities:

\[
R_{\rm ar}(r)\le N(r)\le2J(r+a),
\tag{7}
\]
\[
N(r)=\int_r^{r+a}p(y)^2\,dy+
\frac12\int_0^r[p(y)-p(r-y)]^2\,dy
\ge\int_r^{r+a}p(y)^2\,dy.
\tag{8}
\]

The two overhang caps in (2) give the first term of (8). The upper bound
in (7) follows from Cauchy--Schwarz for the convolution, not from assuming
its sign. The lower bound in (8) is for N, not for R_ar.

## 3. The diagonal cost is already polynomial

For fixed Y define the complete truncated Gram kernel

\[
K_Y(u,v)=\int_0^Y g(y-u)g(y-v)\,dy.
\]

The exact finite pair expansion is

\[
J(Y)=D(Y)+\Theta(Y),
\tag{9}
\]
\[
D(Y)=\sum_{\log n<Y+a}\frac{\Lambda(n)^2}{n}K_Y(\log n,\log n),
\]
\[
\Theta(Y)=2\sum_{\substack{n<m\\\log m<Y+a}}
\frac{\Lambda(n)\Lambda(m)}{\sqrt{nm}}K_Y(\log n,\log m).
\tag{10}
\]

All zero-weight integers can be omitted. K_Y vanishes if |u-v|>=ell.
For the arithmetic arguments u,v>=log 2, if at least one is <=Y-a,
its packet is entirely within [0,Y], so K_Y(u,v)=phi(u-v).
The only altered block is the top-top square
(Y-a,Y+a)^2, where the partially included polynomial packets must be
integrated as written. Replacing that block by the full phi kernel can
create an artificial final-window error.

Let

\[
A_2(t)=\sum_{\log n\le t}\frac{\Lambda(n)^2}{n}.
\]

Interchanging a finite sum and integral gives the useful exact diagonal
formula

\[
\boxed{D(Y)=\int_{-a}^{a}g(v)^2A_2(Y-v)\,dv.}
\tag{11}
\]

For every n>=2, log n+v is positive, so no lower-endpoint term occurs.
The elementary inequality Lambda(n)<=log n already yields

\[
D(Y)\le\sum_{n\le e^{Y+a}}\frac{(\log n)^2}{n}
\le(Y+a)^2(1+Y+a).
\tag{12}
\]

The ordinary unconditional prime number theorem sharpens this to

\[
A_2(t)=t^2/2+o(t^2),\qquad
\boxed{D(Y)=Y^2/2+o(Y^2).}
\tag{13}
\]

Here is the short derivation. From theta(x)~x, partial summation gives
sum_(p<=x)(log p)^2=x log x+o(x log x), then
sum_(p<=x)(log p)^2/p=(log x)^2/2+o((log x)^2).
All powers of exponent at least two contribute a bounded total because
sum_p (log p)^2/[p(p-1)] converges. Finally (11), ||g||_2=1, and the
fixed compact v range give (13). The PNT input is the classical one
recorded in [DLMF 25.16](https://dlmf.nist.gov/25.16.E3); this argument
does not assume RH or a prime-pair correlation law.

Since J>=0, an unconditional lower bound is automatic:

\[
\Theta(Y)\ge-D(Y).
\tag{14}
\]

Only the opposite direction is missing. A polynomial upper bound on
Theta, or just on its scalar positive part Theta_+=max(Theta,0), proves
polynomial J. It is unnecessary to prove a polynomial bound on the
sum of absolute pair terms.

## 4. Selective loss after the signed sum

Let a_*=2A[g]=2(q+c), C_Gamma be the fixed archimedean norm constant
from the preceding note, and X(r)=<QF_r,A^(-1)QF_r>. Equations (7)--(10)
and the previous complete-response comparison give

\[
X(r)\le
\left(C_\Gamma+\sqrt{2D(r+a)}+
                    \sqrt{2\Theta_+(r+a)}\right)^2.
\tag{15}
\]

The known positive-square construction Q=P_epsilon-E_epsilon therefore
has an optimized certified allowance bounded by

\[
\boxed{\mathcal E(r)\le\sqrt{a_*}
\left(C_\Gamma+\sqrt{2D(r+a)}+
                    \sqrt{2\Theta_+(r+a)}\right).}
\tag{16}
\]

When a certified positive upper bound x(r)>=X(r) is available, use
epsilon=sqrt(x(r)/A[F_r]) as in the preceding note; (16) follows from
that exact construction. It is not an independently proved estimate of
Theta_+.

This matches the proposed selective absorption: the favorable aggregate
Theta_- costs nothing in (16). The diagonal has at worst a cubic cost
by (12), and in fact a quadratic cost by PNT. For example, proving

\[
\Theta_+(Y)\le C(1+Y)^2
\quad\hbox{for all sufficiently large real }Y
\tag{17}
\]

would give a linear adverse allowance in r. Any fixed polynomial degree
would suffice for the established arithmetic criterion. Equation (17)
is a proposed theorem target, not a proved assertion or an inferred
asymptotic from a finite pilot.

The positive part in (16) is taken **after** summing every signed
off-diagonal pair. No assertion about operator monotonicity or
entrywise matrix clipping is used.

## 5. Why clipping positive pairs individually fails

Even the sum of just the positive off-diagonal pair terms has
exponential size. Since phi(0)=1 and phi is continuous, choose a fixed
narrow logarithmic block below Y-a so that phi(u-v)>=c_0>0 for every
pair in the block. Its kernels are the full phi values. PNT and partial
summation give

\[
\sum_{\log p\ {\rm in\ the\ block}}\frac{\log p}{\sqrt p}
\asymp e^{Y/2}.
\]

Squaring this sum and removing its O(Y^2) diagonal proves that the
positive off-diagonal mass in that block is at least c_1 e^Y for all
large Y. The absolute pair sum is at least as large. Thus polynomial
control must combine this mass with negative terms elsewhere.

In contrast, the double integral of K_Y against the complete smooth
density is exactly

\[
\int_0^\infty\!\!\int_0^\infty
 e^{(u+v)/2}K_Y(u,v)\,du\,dv
=\int_0^Y p_0(y)^2\,dy,
\tag{18}
\]

which is constant for Y>=a. This is an exact signed cancellation of
the continuous main density, including the final partial-packet block.
It does not estimate the actual prime-pair discrepancy.

The positive-counting/PNT model in the
[one-sided note](../GLOBAL_GROWTH_ONE_SIDED_20261003.md) also applies here.
For dpsi_model(x)=[1+delta x^(alpha-1/2)cos(gamma log x)]dx, with
0<alpha<1/2, gamma!=0 and 0<delta<1, the local signal for y>a is

\[
p_{\rm model}(y)=
\delta\,\operatorname{Re}\!\left[e^{(\alpha+i\gamma)y}
                                G(\alpha+i\gamma)\right],
\tag{19}
\]

where G uses the minus-transform convention below. Its cumulative
square grows exponentially because G(alpha+i gamma)!=0. This is not
a model of the Euler product or of actual primes. It proves that
positive density, PNT, and the prepared smoothing alone cannot close
the signed-pair target.

## 6. Exact prime-by-prime increment

At a fixed Y, group the included powers of one prime p into

\[
b_p(y)=\sum_{\substack{k\ge1\\k\log p<Y+a}}
\frac{\log p}{p^{k/2}}g(y-k\log p),\qquad 0\le y\le Y.
\]

Different powers of the same p have disjoint packet interiors because
log p>=log 2>ell. Their self energy is therefore purely diagonal:

\[
\|b_p\|_2^2
=(\log p)^2\sum_k p^{-k}K_Y(k\log p,k\log p)
\le\frac{(\log p)^2}{p-1}.
\tag{20}
\]

On adding that entire prime to an existing partial signal p_old,

\[
\Delta J=\|b_p\|_2^2+2\langle p_{\rm old},b_p\rangle.
\tag{21}
\]

The first term's cumulative cost is already polynomial in Y. The
second term is signed and contains every old/new interaction; it need
not be positive. In particular J need not increase when a prime is
added, even though J(Y) for the actual complete signal increases with Y.

Equations (20)--(21) make the bridge to the proposed prime-place
normalization concrete: the square-order cost is controlled, and the
remaining first-order interactions are precisely Theta. They supply
no cancellation law for those interactions. A summable weighted
diagonal or a finite trace does not alone control a coherent sum of
all prime packets.

The direct Cauchy--Schwarz attempt at each insertion gives
Delta J<=||b_p||^2+2 sqrt(J_old)||b_p||. Iteration bounds J by
(sum_p ||b_p||)^2. Using (20), the resulting majorant
(sum_(p<=exp(Y+a)) log p/sqrt(p-1))^2 has exponential size by PNT.
Thus controlling the self term does not make this iterative absolute
estimate polynomial. The missing step is a signed aggregate estimate
for the cross terms in (21).

## 7. An unconditional reduction to primes alone

Let

\[
p_{\mathbb P}(y)=\sum_p\frac{\log p}{\sqrt p}g(y-\log p),
\qquad b(y)=p(y)-p_{\mathbb P}(y).
\]

The complete higher-power correction is bounded and tends to zero
unconditionally. For squares, write

\[
p_2(y)=\int t^{-1}g(y-2\log t)\,d\theta(t).
\]

For large y its continuous dt term equals (1/2)int g=0. PNT,
theta(t)=t+o(t), and integration by parts over the fixed-ratio support
make the error o(1). For k>=3, theta(t)<=C t and the support
restriction give O_g(exp(-y(1/2-1/k))) per exponent. There are O(1+y)
active exponents, and 1/2-1/k>=1/6, so their sum is
O_g((1+y)exp(-y/6)). Local finiteness handles the initial compact range.

Thus b=o(1), in particular |b|<=C_b for all y>=0. Consequently

\[
J(Y)\le2J_{\mathbb P}(Y)+2C_b^2Y,\qquad
J_{\mathbb P}(Y)\le2J(Y)+2C_b^2Y.
\tag{22}
\]

Polynomial cumulative energy, or finiteness with every positive
exponential square weight, is therefore unchanged by removing higher
powers analytically. They must still be included in an exact finite
response calculation unless this separate correction bound is used.
The argument parallels the established scalar prime-only reduction;
it now applies to the local linear g response rather than its phi
autocorrelation.

## 8. Weighted complete energy has a coercive local equivalent

For epsilon>0 put

\[
J_\varepsilon=\int_0^\infty e^{-2\varepsilon y}p(y)^2\,dy,\qquad
I_\varepsilon=\int_0^\infty e^{-2\varepsilon r}N(r)\,dr.
\]

These are integrals of the actual complete response. Integrating the
overhang bound (8) with Tonelli gives, including possible infinities,

\[
I_\varepsilon\ge
\frac{e^{2\varepsilon a}-1}{2\varepsilon}J_\varepsilon.
\tag{23}
\]

The coefficient is exact because p vanishes below a: the admissible
r interval for each nonzero p(y) is [y-a,y]. Thus finiteness of
I_epsilon forces finiteness of J_epsilon without assuming it first.

If J_epsilon is finite, Cauchy--Schwarz makes
P(2epsilon)=int_0^infinity exp(-2epsilon y)p(y)dy absolutely convergent.
Fubini applied to (4) then proves

\[
\boxed{I_\varepsilon=
\frac{e^{2\varepsilon a}}{2\varepsilon}J_\varepsilon
-P(2\varepsilon)^2
\le\frac{e^{2\varepsilon a}}{2\varepsilon}J_\varepsilon.}
\tag{24}
\]

In particular these two weighted energies are finite simultaneously.
The projected energy is no larger than N, so this local criterion
suffices for the previous program.

No universal version of (23) holds with R_ar in place of N. For
example the abstract causal signal exp(y/2)1_(y>=b), b>a, has a
reflected response whose full exponential part is proportional to
sinh(x/2). Projection removes it. Its remaining fixed endpoint caps
have bounded projected energy, while J_epsilon diverges for
epsilon<=1/2. This is a geometric counterexample, not an arithmetic
prime signal; the prime transform below excludes that hidden pole.

## 9. Transform, explicit formula, and exact strength of the target

To fix signs, use

\[
G(s)=\int g(x)e^{-sx}\,dx
=\frac{s(1/4-s^2)H_h(s)}{\sqrt\nu},\qquad
H_h(s)=\int h(x)e^{-sx}\,dx.
\]

The earlier [probe theorem](../SINGLE_PROBE_GROWTH_THEOREM_20261003.md)
uses the opposite sign for its G; h is even and these conventions
agree after s is replaced by -s. It proves noncancellation here:
G(s)!=0 when Re s>0, except for the simple zero at s=1/2.

Differentiating the absolutely convergent
[Euler product](https://dlmf.nist.gov/25.2.E11) gives, initially for
Re s>1/2,

\[
\boxed{P(s)=\int_0^\infty e^{-sy}p(y)\,dy
=-G(s)\frac{\zeta'(1/2+s)}{\zeta(1/2+s)}.}
\tag{25}
\]

The zero G(1/2)=0 cancels the pole's logarithmic derivative. A
nontrivial zero rho with Re rho>1/2 instead leaves a nonzero residue
-m_rho G(rho-1/2). If every J_epsilon is finite, Cauchy--Schwarz makes
P holomorphic throughout Re s>0, contradicting such a residue.
The standard zero symmetry then implies RH.

Conversely, the full linear explicit formula for y>a is

\[
p(y)=-
\sum_\rho m_\rho G(\rho-1/2)e^{(\rho-1/2)y}
-\sum_{k\ge1}G(-2k-1/2)e^{-(2k+1/2)y}.
\tag{26}
\]

All nontrivial zeros, with both signs of their imaginary parts and
their multiplicities, are included. There is no extra factor two.
The pole contribution e^(y/2)G(1/2) is zero. One way to derive (26)
is to take the logarithmic derivative of the
[canonical product](https://dlmf.nist.gov/25.2.E12), expand its
gamma term by the [digamma series](https://dlmf.nist.gov/5.7.E6),
and convolve the resulting causal exponential kernels with g.
Canonical constant corrections multiply g(y) and vanish for y>a.
Residues of -zeta'/zeta have negative multiplicity at both kinds
of zeros, fixing the two minus signs.

The sixth distributional derivative of g is a finite measure.
Integration by parts therefore gives
|G(s)|<=C exp(a|Re s|)/|s|^6 away from zero. In the critical strip
the nontrivial-zero series is absolutely convergent at each fixed y
using N(T)=O(T log T); its proof and source are in the preceding note.
The trivial series is bounded uniformly for y>=a by the same
sixth-power estimate. These estimates justify the smoothed canonical
limit; they do not assume RH to state (26).

If RH is assumed for this converse, every nontrivial exponential in
(26) has modulus one. Thus p=O(1), J(Y)=O(1+Y), N(r)=O(1+r),
and all positive weighted energies are finite. Local finiteness covers
the initial cap. This pole-inclusive argument also supplies the
unprojected converse left unasserted in Section 8 of the preceding note.

Therefore the following are equivalent for this actual arithmetic signal:
RH; polynomial cumulative J; finiteness of every J_epsilon;
polynomial unprojected N; and the previously established polynomial
projected-response target. The implication from projected response
passes through its arithmetic RH criterion and (26), not through the
false generic geometric comparison just discussed. No bound in this
list has been proved unconditionally here.

For epsilon>1/2, ordinary Plancherel gives the additional exact identity

\[
J_\varepsilon=\frac1{2\pi}\int_{\mathbb R}
\left|G(\varepsilon+it)
\frac{\zeta'(1/2+\varepsilon+it)}
     {\zeta(1/2+\varepsilon+it)}\right|^2dt.
\tag{27}
\]

If J_epsilon is subsequently proved finite for a smaller epsilon,
the L2 Fourier transform of exp(-epsilon y)p(y), equivalently the
L2 boundary values of its Laplace transform, has the same Plancherel
identity on that line. Boundary values and removable values must be
interpreted accordingly; absolute Laplace convergence on the line
itself is not implied by J_epsilon alone.
Meromorphic continuation alone proves neither this smaller-weight
energy nor a half-plane Hardy bound. In (24) the scalar convolution
term uses P(2epsilon); in (27) the vertical line is Re s=epsilon.
These two arguments must not be conflated.

## 10. Exact projected discrepancy Gram at the top boundary

Assume r>ell and L=r+ell in this section. There is also a direct formula
retaining the projection before the norm,
useful if the stronger J bound is pessimistic. Let

\[
f_u(x)=\frac{g(x+r/2-u)+g(x-r/2+u)}{\sqrt2},\qquad 0\le u\le L,
\]
\[
m(u)=\langle\sinh(x/2),f_u\rangle_{I_r},\qquad
\mathcal K_r(u,v)=\langle f_u,f_v\rangle_{I_r}-m(u)m(v)/d_r.
\tag{28}
\]

For the complete signed discrepancy measure
dmu(u)=sum Lambda(n)/sqrt(n) delta_(log n)(du)-exp(u/2)du,

\[
\boxed{\|P_{\mathcal H}e_r\|_2^2
=\iint_{[0,L]^2}\mathcal K_r(u,v)\,d\mu(u)d\mu(v).}
\tag{29}
\]

At a fixed window mu has finite total variation. Thus this exact Gram
identity and Fubini are legitimate without an infinite-series exchange.
The kernel is positive semidefinite as a Gram kernel; its individual
values can still have either sign.

If u<=r, its two packets are fully inside I_r and prepared, so m(u)=0.
If either u<=r or v<=r, the full-space overlap therefore gives

\[
\mathcal K_r(u,v)=\phi(u-v)+\phi(u+v-r).
\tag{30}
\]

Only the upper-upper square needs spatial and projection corrections.
For u=r+t, v=r+s, 0<t,s<=ell, they are explicit:

\[
\mathcal K_r(r+t,r+s)=
\int_{-a}^a g(z-t)g(z-s)\,dz-\frac{m_t m_s}{d_r},
\]
\[
m_t=
\frac{-2\sinh(L/4)h''(a-t)+\cosh(L/4)h'(a-t)}{\sqrt{2\nu}}.
\tag{31}
\]

The latter formula follows by using the two exact exponential
antiderivatives of g on the truncated cap. It vanishes at t=0 and
t=ell. All spatial truncation and moment corrections are thus
localized to a fixed-width complete top block.

The top/interior overlap in (30) couples only to delays near zero or
near r. There are no actual prime atoms in [0,ell], since log 2>ell;
the continuum discrepancy density in that region still contributes.
It must be retained in (29) when keeping the density cancellation.
This explicit block formula does not bound its discrepancy or permit
separate absolute estimates of its exponentially large pieces.

## 11. Records and next analytic obligation

The [decomposition pilot](../../numerics/selective_loss_signed_pairs_20261003/README.md)
separates the diagonal D, signed off-diagonal Theta, reflected
convolution, and moment subtraction in the actual complete response.
It is a floating diagnostic on a bounded range, without outward
enclosures or a global estimate.

The concrete next theorem to attempt is (17), or any polynomial
upper bound on the combined signed pair sum (10), retaining its
top-top cap block. An alternative is a direct local-shell bound on
int_Y^(Y+1) p_P(y)^2dy, which yields polynomial cumulative energy
through (22). The sharper positive-A dual target remains available
if the L2 response is too expensive.

The progress here is an exact reduction and a controlled diagonal
cost. The missing estimate is an arithmetic cancellation statement
for distinct prime channels. It is not provided by positivity,
PNT, individual pair clipping, or continuation of the zeta expression.
See the [internal review](../../reviews/SELECTIVE_LOSS_SIGNED_PAIRS_REVIEW_20261003.md)
and [program overview](overview.md).


## 12. Subsequent quadratic-target continuation

The [next theorem note](05_quadratic_target_and_finite_sign_20261003.md)
now supplies explicit unconditional quadratic upper and lower bounds for
D(Y), rather than only its asymptotic leading term. Its outward finite
zero-envelope certificate proves Theta(Y)<-5 for every real 100<=Y<=225.
The global target Theta_+(Y)<=C(1+Y)^2 remains open.
The [mechanism audit](06_global_mechanism_tests_20261003.md) tests the
factorization/frame routes and specifies the actual-prime variance needed;
the [weighted continuation](07_weighted_energy_abscissa_20261003.md)
identifies the physical convergence abscissa and the Hardy analyticity
obligation. These continuations retain the full caps and do not change
the exact identities established above.
