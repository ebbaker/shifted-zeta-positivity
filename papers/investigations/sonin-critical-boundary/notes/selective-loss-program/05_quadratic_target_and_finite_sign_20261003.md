# Quadratic signed-pair target: an explicit diagonal and a finite sign theorem

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Separate same-model agents audited
the analytic reductions and certificate. These are internal checks, not
independent specialist refereeing.

## 1. Outcome and the outstanding theorem

The next concrete global target from the
[complete-response note](04_complete_response_and_signed_pairs_20261003.md)
is

\[
\Theta_+(Y)\le C(1+Y)^2\qquad(Y\ge Y_0),\qquad
\Theta_+=\max(\Theta,0).
\tag{1}
\]

Here J=D+Theta is the exact cumulative energy of the complete smoothed
prime response. Theta is summed with its signs before its positive part
is taken. This target remains open. The present continuation establishes
two concrete statements:

**Theorem A, unconditional elementary diagonal bounds.** For every real
Y>=0,

\[
\boxed{\max(0,Y^2/4-48)\le D(Y)
\le2\log2\,(Y^2+17/16).}
\tag{2}
\]

**Theorem B, computer-assisted finite continuum sign.** Using the
published finite-height zero verification and the outward constants
described below, for every real 100<=Y<=225,

\[
\boxed{\Theta(Y)<-5,\qquad \Theta_+(Y)=0.}
\tag{3}
\]

In addition, Theta_+(Y)<=25(1+Y) throughout 0<=Y<=225. Theorem B is
an interval theorem, not a sampled sign observation. It requires no
global RH assumption. It does use a published verification of RH up to
a specified finite height. Neither theorem establishes (1) on unbounded
windows, and no full A or B inverse, Sonin complement, or source-wide
selective-loss certificate is numerically computed here.

The [certificate package](../../numerics/selective_loss_quadratic_target_20261003/README.md)
contains a generator, two outward records, and a rational replay.
The [internal review](../../reviews/SELECTIVE_LOSS_QUADRATIC_TARGET_REVIEW_20261003.md)
records the scope of the checks. The subsequent
[mechanism tests](06_global_mechanism_tests_20261003.md) and
[weighted-energy analysis](07_weighted_energy_abscissa_20261003.md)
identify what remains necessary for a global result.

## 2. Exact normalization and complete finite windows

Keep a=1/4 and the existing prepared probe

\[
h(v)=(1-16v^2)^8\mathbf1_{|v|<a},\quad
g_0=-h'''+h'/4,\quad g=g_0/\sqrt\nu,
\quad \nu=\frac{146640624550936576}{37921101075}.
\]

The function g is real, odd, supported on [-a,a], and has norm one.
It is C^4 after zero extension. Let

\[
p(y)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(y-\log n),\qquad
J(Y)=\int_0^Yp(y)^2\,dy,
\]
\[
K_Y(u,v)=\int_0^Yg(y-u)g(y-v)\,dy,
\]
\[
D(Y)=\sum_n\frac{\Lambda(n)^2}{n}K_Y(\log n,\log n),
\quad
\Theta(Y)=2\sum_{n<m}\frac{\Lambda(n)\Lambda(m)}{\sqrt{nm}}
K_Y(\log n,\log m).
\tag{4}
\]

These are finite sums: every nonzero packet has log n<Y+a. Both ends
of every partial packet are retained. Since log2>a, the lower endpoint
of every packet lies above zero. With

\[
A_2(t)=\sum_{\log n\le t}\frac{\Lambda(n)^2}{n},
\]

finite interchange gives the exact diagonal convolution

\[
D(Y)=\int_{-a}^{a}g(v)^2 A_2(Y-v)\,dv.
\tag{5}
\]

No cutoff at exp(Y), or replacement of a partial packet by a whole
packet, occurs in (5). The prior asymptotic D(Y)~Y^2/2 remains valid;
(2) supplies explicit global constants without a PNT error estimate.

## 3. Elementary counting bounds

Write C=4 log2. For each integer n>=1, Legendre's valuation formula
shows that every prime power in (n,2n] contributes one to
log binomial(2n,n), while all other valuation summands are zero or one.
Consequently

\[
\psi(2n)-\psi(n)\le\log\binom{2n}{n}\le2n\log2.
\]

Summing at dyadic points and rounding a real x up to the next dyadic
point gives

\[
\psi(x)\le Cx,\qquad\theta(x)\le Cx\quad(x\ge1).
\tag{6}
\]

For a lower bound, binomial(n,k) divides lcm(1,...,n): its p-adic
valuation is a sum of at most floor(log_p n) terms, each zero or one.
The largest binomial coefficient is at least 2^n/(n+1). Choose
n=floor(x)-1 for x>=2. Then n>=x-2 and n+1<=x, so

\[
\psi(x)\ge(x-2)\log2-\log x.
\tag{7}
\]

The same inequality holds trivially on 1<=x<2. The prime-power identity
psi-theta=sum_{j>=2}theta(x^{1/j}) and (6) imply

\[
\psi(x)-\theta(x)\le C\left[\sqrt{x}
+\frac{\log x}{\log2}x^{1/3}\right].
\]

For u=log x>=10, division by x therefore yields

\[
\frac{\theta(x)}x\ge \log2
-(2\log2+u)e^{-u}-4\log2\,e^{-u/2}-4u e^{-2u/3}.
\tag{8}
\]

Every subtracted term decreases for u>=10. Its value at u=10 is
enclosed by the certificate and is greater than 1/2 (approximately
0.62304333568). Thus

\[
\theta(x)\ge x/2\quad(x\ge e^{10}).
\tag{9}
\]

This last numerical check is elementary and could instead be replaced
by rational exponential bounds; the zero verification is not used in
(6)--(9).

## 4. Proof of Theorem A

Since Lambda(n)^2<=Lambda(n)log n, use partial summation with
f(x)=log(x)/x. For t>=1,

\[
A_2(t)\le f(e^t)\psi(e^t)-\int_1^{e^t}f'(x)\psi(x)\,dx.
\]

Here f'>=0 on [1,e], so its contribution can be discarded in an upper
bound; f'<=0 beyond e. Apply (6) to the endpoint and the remaining
integral to obtain

\[
A_2(t)\le Ct+C\int_e^{e^t}\frac{\log x-1}{x}\,dx
=\frac C2(t^2+1).
\tag{10}
\]

For 0<=t<1 only n=2 can contribute, and its weight
(log2)^2/2<C/2; for t<0 the sum is empty. Thus (10) holds for every
real t. Evenness of g^2, its unit integral, and
mu_2=int v^2 g(v)^2dv<=1/16 give

\[
D(Y)\le\frac C2(Y^2+1+\mu_2)
\le2\log2\,(Y^2+17/16).
\]

For t>=10 retain just primes in (e^{10},e^t]. Stieltjes partial
summation with theta, the upper endpoint lower bound (9), the lower
endpoint upper bound (6), and -f'>=0 gives

\[
A_2(t)\ge t/2-10C
+\frac12\int_{e^{10}}^{e^t}\frac{\log x-1}{x}\,dx
=t^2/4-(20+10C)>t^2/4-48.
\tag{11}
\]

For Y>=10+a, apply (11) in (5), obtaining
D(Y)>=Y^2/4-48. For 0<=Y<10+a, that polynomial is negative and
D(Y)>=0 suffices. This proves (2) for all real Y>=0. In particular
the diagonal cost is now explicitly quadratic unconditionally.

## 5. A uniform finite-height bound for the local signal

Use the minus-Laplace convention

\[
G(s)=\int_{-a}^a g(v)e^{-sv}\,dv
=\frac{s(1/4-s^2)}{\sqrt\nu}H_h(s),\qquad
H_h(s)=\int_{-a}^a h(v)e^{-sv}\,dv.
\]

For y>a the complete linear smoothed explicit formula is

\[
p(y)=-\sum_\rho m_\rho G(\rho-1/2)e^{(\rho-1/2)y}
-\sum_{k\ge1}G(-2k-1/2)e^{-(2k+1/2)y}.
\tag{12}
\]

The nontrivial sum includes both imaginary signs and multiplicities.
The zeta-pole term vanishes because G(1/2)=0. This is the linear
response formula, so its decay is sixth power, rather than the twelfth
power of the autocorrelation formula in the earlier growth certificate.
The derivation and normalization are inherited from the complete-response
note and [zero-tail analysis](../GLOBAL_GROWTH_ZERO_TAIL_20261003.md).

The distributional sixth derivative of zero-extended g_0 is a finite
signed measure: an interior polynomial plus two endpoint atoms. Exact
rational arithmetic gives

\[
\|g_0^{(6)}\|_{L^2(-a,a)}^2
=\frac{2504085215525628254072340480}{19},
\quad B_{\rm atom}=2\,8!\,8^8=1352914698240.
\]

The interior L1 norm is at most the L2 norm times sqrt(1/2), hence
strictly less than 8117695446119. Set

\[
B=9470610144359,\quad K=B/\sqrt\nu
=4816053226.128421\ldots.
\]

Distributional integration by parts therefore proves

\[
|G(s)|\le K e^{a|\Re s|}|s|^{-6}\quad(s\ne0).
\tag{13}
\]

Let N(t) count positive-ordinate nontrivial zeros with multiplicity.
The [explicit zero-count theorem of Hasanalizade, Shen and Wong](https://arxiv.org/abs/2107.06506)
implies N(t)<=t log t for t>=100, as checked in the existing zero-tail
note. Counting both signs and omitting a nonpositive endpoint gives

\[
\sum_{|\Im\rho|>T}m_\rho|\Im\rho|^{-6}
\le12T^{-5}\left(\frac{\log T}{5}+\frac1{25}\right),\quad T\ge100.
\tag{14}
\]

The [Platt--Trudgian finite-height theorem](https://arxiv.org/abs/2004.09765)
places every zero up to T_*=3*10^{12} on the critical line. This is a
finite verified input, not a hypothesis that all zeros are on that line.

At the low cutoff T_0=500, the generator certifies N(500)=269 and
enumerates 270 consecutive positive zeros. It checks gamma_269<500,
gamma_270>500, disjoint ordered enclosures, and real part exactly 1/2.
The low mass, including both signs, is enclosed as

\[
S_{500}=2\sum_{j=1}^{269}|G(i\gamma_j)|
=4.813490676290039592\ldots.
\tag{15}
\]

Completeness uses both a rigorous count and the consecutive-zero API;
merely producing a list of 269 approximations would be insufficient.
The [FLINT zero-count and enumeration documentation](https://flintlib.org/doc/acb_dirichlet.html)
describes the Turing-based count and interval routines used here.

For the critical zeros between 500 and T_*, (13)--(14) give

\[
A_{500}=12K\,500^{-5}\left(\frac{\log500}{5}+\frac1{25}\right)
=0.002372589621254\ldots.
\]

Using an infinite counting majorant bounds this finite critical segment;
it makes no assertion about criticality above T_*. Above T_* we use
|Re(rho-1/2)|<=1/2 and |rho-1/2|>=|Im rho|. Its allowance is

\[
\delta_* e^{y/2},\quad
\delta_*=12K e^{1/8}T_*^{-5}
\left(\frac{\log T_*}{5}+\frac1{25}\right)
=1.55928674349103\ldots\times10^{-51}.
\tag{16}
\]

Finally ||g||_1<=sqrt(1/2) implies for y>a the trivial-zero allowance

\[
T_{\rm triv}(y)=
\frac{\sqrt{1/2}\,e^{-5(y-a)/2}}{1-e^{-2(y-a)}}.
\tag{17}
\]

It decreases for y>=1. Combining (12)--(17), for every real 1<=y<=225,

\[
|p(y)|\le S_{500}+A_{500}+\delta_*e^{225/2}
+T_{\rm triv}(1)
<\frac{497}{100}.
\tag{18}
\]

The enclosed right side before rational rounding is
4.966694406960983244... . The statement covers the whole real interval:
the critical terms have absolute exponential factor one, the unknown
tail is increasing in y, and the trivial tail is decreasing. There is
no y-grid interpolation or arithmetic sieve near exp(225).

The generator reconstructs the polynomial, norm, and derivative
constants exactly, then uses Arb/Acb outward arithmetic for the zero
mass and all transcendental constants. Separate 192-bit and 256-bit
runs both prove the strict rational threshold. The rational replay
checks the records, source identity, overlapping enclosures, and final
inequalities; it does not replace the analytic proofs or the published
finite-height theorem.

## 6. Proof of Theorem B

At Y=1, only the packets n=2,3 can contribute, because
3<exp(1+a)<4. By the L2 triangle inequality and ||g||_2=1,

\[
J(1)\le\left(\frac{\log2}{\sqrt2}
+\frac{\log3}{\sqrt3}\right)^2<\frac{127}{100}.
\tag{19}
\]

This initial bound is deliberately coarse and is enclosed in both
production records. Equations (18)--(19) give for 1<=Y<=225

\[
J(Y)<\frac{127}{100}+\left(\frac{497}{100}\right)^2(Y-1).
\tag{20}
\]

Subtract (20) from the lower bound for D in (2). At Y=100 the
resulting lower margin is

\[
\frac{100^2}{4}-48-\frac{127}{100}
-\left(\frac{497}{100}\right)^2\!99
=\frac{53409}{10000}>5.
\]

The derivative of that polynomial difference is
Y/2-24.7009>=25.2991>0 for Y>=100. Therefore D(Y)-J(Y)>5 on the
entire interval [100,225], which proves (3). For Y<=1, J(Y)<=J(1)<1.27;
for 1<=Y<=225, (20) is less than 25(1+Y). Since Theta_+<=J,
the additional finite linear bound follows.

## 7. Implication for the selective allowance and the next obligation

The previous source-energy construction has

\[
X(r)\le\left(C_\Gamma+\sqrt{2D(r+a)}
+\sqrt{2\Theta_+(r+a)}\right)^2,
\quad
E(r)\le\sqrt{a_*}
\left(C_\Gamma+\sqrt{2D(r+a)}+\sqrt{2\Theta_+(r+a)}\right).
\tag{21}
\]

On 399/4<=r<=899/4, Theorem B makes the last term zero, and Theorem A
gives the finite-range linear allowance

\[
E(r)\le\sqrt{a_*}\left[
C_\Gamma+2\sqrt{\log2}\,
\sqrt{(r+1/4)^2+17/16}\right].
\tag{22}
\]

This is an analytic consequence of the already established dual
inequality; C_Gamma and a_* are not newly numerically certified here.
It has a bounded range of r and cannot be inserted as a global input
to the one-sided RH theorem.

By Theorem A, target (1) is equivalent to J(Y)=O((1+Y)^2). For this
particular probe either global estimate is RH-equivalent: polynomial
energy makes the true Laplace transform holomorphic in Re s>0, while
-G(s)zeta'/zeta(1/2+s) has a noncancelled pole at every offcritical
right-half-plane zero. Conversely RH makes the absolutely summable
zero expansion bounded, so J(Y)=O(1+Y). The noncancellation theorem
is specific to the chosen h and g and was proved in the earlier notes.

The finite sign theorem proves that aggregate cancellation is effective
on a substantial bounded interval. The unknown-zero allowance in (16)
eventually grows exponentially, so enlarging finite verification cannot
alone prove (1). The next concrete global target should bound the
actual fixed-kernel dyadic prime variance, or a signed pair expression
equivalent to it, while retaining complete caps. The following two
notes formulate that obligation and rule out several shortcuts.
