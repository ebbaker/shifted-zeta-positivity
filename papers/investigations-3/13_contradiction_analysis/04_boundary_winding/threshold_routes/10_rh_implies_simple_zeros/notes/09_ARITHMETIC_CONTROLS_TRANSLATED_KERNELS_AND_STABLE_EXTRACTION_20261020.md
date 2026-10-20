# Arithmetic controls, translated kernels, and stable extraction

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded turn metadata. Separate same-model derivations and
[internal review][review]; no specialist review or priority claim.

**Outcome:** three quantitative results refine the open route. A normalized
arithmetic control preserves every prescribed finite coefficient block,
positive ordinary and logarithmic coefficients, pole residue one, and
the global RH prime-counting error class, while inserting multiple zeros;
it fails the exact functional equation and entire completion. Translated
nonnegative kernels have arbitrarily small discrete absolute prime cost
outside Note 08's fixed mass-bandwidth class, but their required return
height is now shown in [Note 10][n10] to prevent a better complete envelope
for these uniformly aligned constructions. Finally, a stable
combination of logarithmic derivatives reduces the sufficient finite-sum
cutoff for multiplicity extraction under a separately certified gap.
None supplies an opposing signed estimate or excludes an original theta zero.

This continues the [program][program] and [Note 08][n8], with the
[result index][results], [collision catalogue][controls] and [avoid
index][avoid], particularly [control premises][a02], [scoped conclusions][a07],
[complete payments][a12] and [quantitative gain][a20]. These are explicit
controls and a stated cost comparison, not additional unquantified
simplicity criteria. The [BW09 manuscript][bw09] still requires strict
surplus beyond the exact multiplicity baseline.

The three parts have separate hypotheses. The arithmetic control is not
an original theta flow; the kernel construction is an unchanged-prime
test-function construction; and the extraction theorem uses actual xi
under RH plus an independently certified noncentral gap.

## 1. A positive arithmetic control with exact finite data and residue

Fix an integer \(m\ge2\), a real gamma>0, and a sufficiently large integer
P>(2m)^2. The letter gamma here is a prescribed ordinate; it need not
already be a zeta-zero ordinate. Define the meromorphic function
\[
 B_P(s)=\{\zeta(s+1/2+i\gamma)\zeta(s+1/2-i\gamma)\}^{-m}
 \prod_{p\le P}\{(1-p^{-s-1/2-i\gamma})
                    (1-p^{-s-1/2+i\gamma})\}^{-m}.
 \tag{A1}
\]
On Re s>1/2 this is the convergent tail product
\[
 B_P(s)=\prod_{p>P}
       \{(1-p^{-s-1/2-i\gamma})(1-p^{-s-1/2+i\gamma})\}^{m}.
\]
It is positive at \(s=1\). The usual zeta Euler product and its simple pole
of residue one are recorded in [DLMF §25.2](https://dlmf.nist.gov/25.2).
All continuation statements below use (A1), not a termwise Euler series
inside its convergence half-plane boundary.

For \(n=p^k\), put
\[
 a_{p,k}=1-2m\mathbf1_{p>P}p^{-k/2}\cos(k\gamma\log p)>0.
 \tag{A2}
\]
On Re s>1, the logarithmic Dirichlet coefficients of zeta(s)B_P(s)
are \(a_{p,k}/k\). Thus its logarithmic derivative has prime-power weights
\(a_{p,k}\Lambda(p^k)\). Positivity is uniform in gamma because
\(a_{p,k}\ge1-2m/\sqrt P>0\).

We also enforce the exact residue, without changing any coefficient
supported on primes at most P. Write
\[
 b_P=-\log B_P(1),\quad
 A_P=\sum_{P<q\le2P}\frac{a_{q,1}}q,\quad
 \lambda_P=b_P/A_P,\quad
 D_P(s)=\lambda_P\sum_{P<q\le2P}a_{q,1}q^{-s}.
 \tag{A3}
\]
The sums are over primes. The [prime number theorem](https://dlmf.nist.gov/25.16.i),
with partial summation on [P,2P], gives
\(A_P\sim(\log2)/\log P\), uniformly in gamma: the alteration from
\(a_{q,1}=1\) has relative size at most \(2m/\sqrt P\).
Also \(|b_P|=O_m(P^{-1/2})\), by the convergent logarithmic tail in (A1).
Consequently \(|\lambda_P|=O_m(\log P/\sqrt P)<1\) for sufficiently large
P. Define
\[
                         Z_P(s)=\zeta(s)B_P(s)e^{D_P(s)}.
 \tag{A4}
\]
Its residue at 1 is exactly one, since \(D_P(1)=b_P\). Its logarithmic
coefficient at a selected prime q is now \(a_{q,1}(1+\lambda_P)>0\);
all other prime-power coefficients are unchanged. Therefore, on Re s>1,
\[
 Z_P(s)=\sum_{n\ge1}c_P(n)n^{-s},\qquad c_P(n)>0,
 \quad c_P(1)=1,
 \quad c_P(n)=1\ \hbox{if every prime factor of }n\hbox{ is at most }P.
 \tag{A5}
\]
Indeed each local factor is the exponential of a power series with
strictly positive real coefficients and constant term zero. Its
exponential has strictly positive coefficients, and absolute convergence
permits multiplication of the local series. In particular all ordinary
Dirichlet coefficients up through P agree exactly with zeta. The
correction exp(D_P) by itself need not have positive coefficients when
b_P<0; positivity is asserted only after combining its logarithm with
the other local coefficients.

Writing \(-Z_P'/Z_P=\sum\Lambda_P(n)n^{-s}\), we have
\[
 \Lambda_P(n)=0\quad\hbox{off prime powers},\qquad
 \Lambda_P(p^k)>0,
 \qquad
 \sup_{p,k}\left|\frac{\Lambda_P(p^k)}{\Lambda(p^k)}-1\right|
                 =O_m(\log P/\sqrt P).
 \tag{A6}
\]
For selected q this follows from (A2) and lambda_P's bound; elsewhere
the deviation is at most \(2m/\sqrt P\). Thus finite exact coefficient
agreement and uniform small relative changes to every logarithmic weight
coexist with the inserted multiple event below.

## 2. Uniform right-half-plane approximation and the inserted zeros

For \(u>1\), define the explicit elementary tail allowance
\[
 T_P(u)=\frac{P^{1-u}}{(u-1)(1-P^{-u})}.
\]
The canonical logarithm of the tail product satisfies, for sigma>1/2,
\[
 |\log B_P(\sigma+it)|\le2mT_P(\sigma+1/2).
 \tag{A7}
\]
To see this, discard the cosine signs only for this comparison and use
\(
 \sum_{p>P,k\ge1}p^{-ku}/k
 \le(1-P^{-u})^{-1}\sum_{n>P}n^{-u}
 \le T_P(u).
\)
The correction has coefficients of a single sign, so (A3) also gives
\[
 |D_P(\sigma+it)|
 \le |b_P|\max\{P^{1-\sigma},(2P)^{1-\sigma}\}.
 \tag{A8}
\]
For every fixed epsilon>0, (A7)–(A8) imply, uniformly in t and the
chosen ordinate gamma,
\[
 \sup_{\Re s\ge1/2+\epsilon}
 \left|\frac{Z_P(s)}{\zeta(s)}-1\right|
                =O_{m,\epsilon}(P^{-\epsilon}).
 \tag{A9}
\]
At a common zero or the pole the quotient is understood as the analytic
factor B_P exp(D_P). For epsilon>1/2 the same bound follows directly
from (A7)–(A8); there is no need to weaken it to the bound at sigma=1.

Assume RH now. Then the reciprocal zeta factors in (A1) have no poles
in Re s>0: nontrivial denominator zeros occur on Re s=0, and trivial
ones lie farther left. The finite local reciprocal factors have poles
only on Re s=-1/2. In the open half-plane Re s>0 the only zeros of
B_P are at
\[
                            s=1/2+i\gamma,\quad1/2-i\gamma,
 \tag{A10}
\]
each of exact order m. This uses the simple poles of the respective
zeta factors at argument 1; the other factor has argument 1±2i gamma
and is finite and nonzero. Zeta's absence of zeros on Re s=1 is stated
in [DLMF §25.10](https://dlmf.nist.gov/25.10).
The finite correction is entire and zero-free. Thus Z_P is meromorphic
in Re s>0 with its sole pole the simple pole at 1, and all its zeros
there lie on Re s=1/2. Their multiset consists of zeta's original zeros
and the inserted pair, adding order m at each selected ordinate. If an
ordinate was already a zeta zero, its order increases by m.

These conclusions are conditional controls, not new functions satisfying
every premise of the zeta problem. In particular the agreement in (A9)
is on each fixed right half-plane, not uniformly up to its boundary at
Re s=1/2. A boundary zero is compatible with that convergence.

## 3. The prime-supported counting function retains the global RH error class

Define \(\Psi_P(x)=\sum_{n\le x}\Lambda_P(n)\) and retain
\(\Psi(x)=\sum_{n\le x}\Lambda(n)\). Exactly,
\[
 \Psi_P(x)-\Psi(x)
 =-2m\sum_{\substack{p>P,\ k\ge1\\p^k\le x}}
       (\log p)p^{-k/2}\cos(k\gamma\log p)
   +\lambda_P\sum_{P<q\le\min(2P,x)}a_{q,1}\log q.
 \tag{A11}
\]
The first term is \(O_m(\sqrt x)\), since Chebyshev's
\(\Psi(t)\ll t\) and partial summation give
\(\sum_{n\le x}\Lambda(n)n^{-1/2}\ll\sqrt x\).
The correction is zero for \(x\le P\). Otherwise it is at most
\(O_m(\sqrt P\log P)=O_m(\sqrt x\log(2x))\), using the bound
for \(\lambda_P\) and \(\sum_{P<q\le2P}a_{q,1}\log q\ll_m P\).
Consequently, uniformly in the sufficiently large cutoff and ordinate,
\[
 |\Psi_P(x)-\Psi(x)|\ll_m\sqrt x\log(2x),\qquad x\ge2.
 \tag{A12}
\]
Under RH, the checked bound for \(\Psi(x)-x\) in Note 03 therefore gives
\(\Psi_P(x)=x+O_m(\sqrt x\log^2(2x))\). Positivity and prime-power
support of this counting measure are exact. Its weights are altered;
this is preservation of the global error class, not of the original
von Mangoldt data or its signed correlation at the event.

## 4. The failed completion premise is explicit

Put R_P(s)=B_P(s)exp(D_P(s)). If the usual completed function
xi(s)R_P(s) satisfied zeta's exact reflection equation, then
R_P(s)=R_P(1-s) would hold meromorphically wherever xi is nonzero,
and hence identically. This is impossible. Choose a nontrivial zeta
zero rho=1/2+i tau with tau≠gamma. At s0=i(tau-gamma), the first
denominator factor in (A1) vanishes. The second factor and the finite
local factors cannot supply a cancelling zero there: the second argument
has real part 1/2 and is not the pole 1. The finite reciprocal local
factors are nonzero there; their poles lie only at real part -1/2.
Thus R_P has a genuine pole at s0. By contrast
R_P(1-s0) is finite and nonzero, since its real part is 1.

Equivalently, forcing symmetry by replacing R_P(s) with
R_P(s)R_P(1-s) introduces genuine poles on Re s=1. Zeta and its
completion do not cancel them: 1-s0≠1 and zeta has no zeros on that
line. The [standard reflection formula](https://dlmf.nist.gov/25.4)
therefore remains a decisive missing premise. The control also fails
whole-plane entireness after the usual completion; it is not an original
theta heat flow and supplies no cap-winding counterexample.

This extends a control screen in a specific direction: arbitrary finite
coefficient agreement, coefficient positivity, logarithmic positivity,
residue one, and right-half-plane proximity do not jointly exclude a
multiple boundary zero. Note 05's positive-source control preserves
different completion data and fails the ordinary Dirichlet-series
premise. These preservation lists must not be combined. Neither control
satisfies the complete unchanged arithmetic and completion of zeta.

Finally, agreement of the first P coefficients does **not** transfer
Note 08's finite Euler-sum remainder to Z_P. That remainder uses the
exact tail with all zeta coefficients equal to one. A proposed signed
estimate that retains that exact tail or the exact functional equation
is outside this control's scope. No conclusion is drawn against such an
estimate, and no original multiple zero is excluded.

## 5. Translated copies and finite simultaneous prime phases

In Note 08's Fourier convention, let

\[
K_\Delta(x)=\left(\frac{\sin\pi\Delta x}{\pi\Delta x}\right)^2,
\qquad \widehat K_\Delta(v)=\frac1\Delta(1-|v|/\Delta)_+.
\]

Fix `d=2` or `d=3`, let `Delta->infinity`, and put `X=e^(2pi Delta)`. For a positive real `R`, define

\[
D_R=\sum_{j=0}^{d-1}K_\Delta(jR),\qquad
h_{\Delta,R}(x)=\frac1{D_R}\sum_{j=0}^{d-1}K_\Delta(x-jR).       \tag{K1}
\]

It is entire, nonnegative on the real line, and has the required quadratic decay in every fixed horizontal strip. Exactly,

\[
h(0)=1,\quad I=\frac d{\Delta D_R},\quad
\widehat h(v)=\frac{(1-|v|/\Delta)_+}{\Delta D_R}
       \sum_{j=0}^{d-1}e^{-2\pi i vjR}.                         \tag{K2}
\]

Its support is `[-Delta,Delta]`. For fixed `d`,

\[
D_R=1+O_d((\Delta R)^{-2}).                                  \tag{K3}
\]

Let `omega=e^(2pi i/d)`. For any prescribed `epsilon>0`, there are arbitrarily large `R` such that

\[
|e^{-iR\log p}-\omega|<\epsilon\qquad(p\le X).                \tag{K4}
\]

Here is a self-contained existence argument. Unique factorization gives `sum_p k_p log p !=0` for every nonzero integer vector on this finite prime set. Thus the time average of every nonconstant torus character of `R->(e^(-iR log p))_(p<=X)` tends to zero by elementary integration. Approximation of continuous functions by trigonometric polynomials shows that a nonnegative continuous bump supported in the product of the prescribed phase neighborhoods has time average equal to its strictly positive torus integral. Hence its support is visited at arbitrarily large positive times. No rational independence involving the number one is needed because `R` is continuous. A discrete integer-time version is not being assumed.

Make the phase accuracy quantitative in its subsequent use by defining the finite number

\[
B_\Delta=\frac1{\pi\Delta}
 \sum_{p^k\le X} k(\log p)p^{-k/2}
                \left(1-\frac{k\log p}{2\pi\Delta}\right),
\qquad
\epsilon_\Delta=\frac1{\Delta^2(1+B_\Delta)}.                 \tag{K5}
\]

Choose a return `R>=exp(Delta^2)` satisfying (K4) with this accuracy. An additional arbitrarily large lower threshold on `R` may be imposed. For the two-copy statement “from below”, choose `R` outside the discrete zero set of `sin (pi Delta R)`, which is possible because the admissible phase neighborhoods are open.

For every prime power in the support,

\[
\left|\sum_{j=0}^{d-1}e^{-ijkR\log p}
          -d\,\mathbf1_{d\mid k}\right|
 \le \frac{d(d-1)}2 k\epsilon_\Delta.                         \tag{K6}
\]

This follows by telescoping powers of two unit complex numbers and summing `j`. The Lipschitz inequality for absolute value now proves the exact discrete comparison

\[
\left|C(h)-\frac{d}{\pi\Delta D_R}
 \sum_{p^{dj}\le X}(\log p)p^{-dj/2}
       \left(1-\frac{dj\log p}{2\pi\Delta}\right)\right|
 \le\frac{d(d-1)}{2D_R}\epsilon_\Delta B_\Delta
 =O_d(\Delta^{-2}).                                         \tag{K7}
\]

All powers of every prime are included. In particular the construction cancels only specified harmonics; it does not discard the remaining powers.

## 6. Two copies give cost one; three give cost tending to zero

For `d=2`, the retained sum in (K7) is

\[
\sum_{p^j\le e^{\pi\Delta}}\frac{\log p}{p^j}
       \left(1-\frac{j\log p}{\pi\Delta}\right)
       =\frac{\pi\Delta}{2}+o(\Delta).                       \tag{K8}
\]

Indeed the `j>=2` part is bounded uniformly by the absolutely convergent series `sum_p log p/[p(p-1)]`. For `j=1`, partial summation and the ordinary PNT give
`sum_(p<=e^T) (log p)/p (1-log p/T)=T/2+o(T)`, with `T=pi Delta`. One may obtain it by integrating the positive weight against `theta(x)~x`; the two main terms are of orders `T` and `T/2`, so no smaller-order cancellation is used.

Consequently,

\[
I\Delta=\frac2{1+K_\Delta(R)}\uparrow2\ \text{in the sense of convergence from below},
\qquad C(h)\longrightarrow1.                                \tag{K9}
\]

No monotonicity in `Delta` is asserted. The deficit satisfies
`0<2-I Delta<=2/(pi^2 Delta^2 R^2)`. In particular Note 08's exponential expression `I^2 exp(pi/I)` diverges while `C(h)` remains bounded. The constant or error in its fixed-`eta<2` bound cannot be made uniform through this boundary.

For every fixed integer `d>=3` the same calculation applies. Absolute convergence now gives, by dominated convergence,

\[
\sum_{p^{dj}\le X}(\log p)p^{-dj/2}
       \left(1-\frac{dj\log p}{2\pi\Delta}\right)
 \longrightarrow A_d:=\sum_p\frac{\log p}{p^{d/2}-1}
 =-\frac{\zeta'(d/2)}{\zeta(d/2)}.                            \tag{K10}
\]

Therefore the three-copy case already yields

\[
\boxed{I\Delta\longrightarrow3,\quad I\longrightarrow0,
\quad C(h)=\frac{A_3}{\pi}I+o(I)\longrightarrow0.}            \tag{K11}
\]

The payment is not exactly zero. This is fully consistent with Note 08's exact-zero result `C(h)=0 => I>=2pi/log2`: near-zero payment has fundamentally different behavior once the bandwidth-mass product is unrestricted.

## 7. Complete gamma and pole budgets can be paid

For any selected return `R`, choose a target height `gamma=4dR` and set `L=log(gamma/(2pi))`. If the target is required to be a zero ordinate, take any ordinate in `[4dR,8dR]`, which exists for sufficiently large `R` by the usual zero-count asymptotic; all estimates below are uniform in this interval. No multiple zero is postulated or selected.

For a copy centered at `jR`, put `v=jR+u`. On `|u|<=sqrt(gamma)`, the digamma asymptotic gives
`|g_gamma(jR+u)-L|=O_d(1)`, because `0<=jR<=gamma/4`. On the complementary set, use

\[
K_\Delta(u)\le\frac1{\pi^2\Delta^2u^2},\qquad
|g_\gamma(jR+u)-L|\ll_d L+\log(2+|u|).
\]

The real part of the digamma function at real part `1/4` is bounded at bounded imaginary argument, so this bound also covers the point where `gamma+jR+u` is near zero. Summing the copies proves

\[
\frac{\int h(v)|g_\gamma(v)-L|\,dv}{LI}
 \ll_d\frac1L+\frac1{\Delta\sqrt\gamma}\longrightarrow0.      \tag{K12}
\]

The pole arguments are `-gamma-jR +/- i/2`, all at distance at least `gamma` horizontally. The sine bound gives

\[
E_\gamma(h)\le
 \frac{2d\cosh^2(\pi\Delta/2)}
 {\pi^2\Delta^2D_R(\gamma^2+1/4)},\qquad
\frac{E_\gamma(h)}{LI}
 \ll\frac{e^{\pi\Delta}}{\Delta\gamma^2L}\longrightarrow0.     \tag{K13}
\]

The last limit uses `R>=exp(Delta^2)`. Thus both Note 08(K4) and(K5) hold, and either its modulus-pole or exact-pole upper envelope is admissible.

However these budgets do not make the full envelope small. Its value along this family is

\[
U(\gamma)=\left(\frac d{2\pi}+o(1)\right)\frac L\Delta
          +C(h).                                           \tag{K14}
\]

**Continuation, 20 October 2026:** [Note 10][n10], proved under RH from
a checked short-log-zeta approximation, forces
`log X<=(2+o(1))log log R` for these uniformly aligned returns.
Thus (K14), including the scalar-square variant below, has full-envelope
leading coefficient at least `d/2`: one for two copies and three-halves
for three. Both exceed Fejér's one-half. The small prime-payment examples
are unchanged, but the complete-height comparison for this construction
is now resolved against an improvement.

The original recurrence argument gives no useful upper bound on the phase-return height `R` as a function of `Delta` and `epsilon_Delta`. Note 10 supplies a lower bound instead, sufficient for the stated comparison with Note 08. If a deliberately uncompetitive fully paid sequence is desired, impose the additional threshold `R>=exp(exp(Delta^2))`; recurrence still supplies it, and then `U/(L/log L)->infinity`. The counterexample concerns the unrestricted prime-payment bound, not the complete optimized height envelope.

## 8. The same effect occurs for an explicit scalar square

The translated sum is already within Note 08's class. To realize the requested scalar-square form without importing a spectral factorization theorem, let

\[
s_j(x)=\frac{\sin\pi\Delta(x-jR)}{\pi\Delta(x-jR)},\quad
g(x)=\sum_{j=0}^{d-1}s_j(x),\quad
\widetilde h(x)=\frac{g(x)^2}{g(0)^2}.                        \tag{K15}
\]

On the real line this is `|g(x)/g(0)|^2`. Since `g(0)=1+O_d((Delta R)^(-1))`, the denominator is nonzero for the chosen large returns. The diagonal terms have exactly the Fourier samples used above. For `i!=j`, direct convolution of the two interval transforms gives

\[
\widehat{s_i s_j}(v)=
 e^{-\pi iv(i+j)R}
 \frac{\sin (\pi(i-j)R(\Delta-|v|))}{\pi(i-j)R\Delta^2}
 \quad(|v|\le\Delta),                                      \tag{K16}
\]

and zero otherwise. Hence every cross transform is bounded by
`1/(pi|i-j|R Delta^2)`. Their entire discrete prime payment is

\[
\ll_d\frac1{R\Delta^2}
       \sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
 \ll_d\frac{e^{\pi\Delta}}{R\Delta}=o(\Delta^{-2}),           \tag{K17}
\]

where the last majorant follows even from `Lambda(n)<=log n`. Thus `I_tilde Delta->d`, and (K9)'s cost limit and (K11)'s linear cost asymptotic hold also for this scalar-square family. For `d=2` this version need not approach the mass-bandwidth boundary from below; the sum family already proves that sharper directional statement.

Finally, `|sum_j s_j|^2<=d sum_j|s_j|^2` on the real line pays (K12) for the square family, whose mass is `d/Delta+O_d(1/(R Delta^2))`. The same inequality at complex arguments pays (K13), with a constant depending only on fixed `d`. Its positivity, strip decay, and bandlimitation are preserved. No hidden continuous replacement of the discrete prime sum occurs in (K17).

**Disposition.** Small mass plus nonnegative bandlimitation does permit arbitrarily small absolute prime payment for `I Delta->3`, even with the explicit archimedean budgets. An unrestricted extension of Note 08(K15), or a uniform near-zero-payment consequence of its exact-zero statement, is therefore false. [Note 10][n10] now pays the uniform phase-return lower height and proves the full-envelope comparison for this particular family. Arbitrary kernels and other phase patterns remain outside the result; no original theta zero or multiplicity event is excluded.

**Subsequent general comparison:** [Note 11][n11] extends the leading
one-half full-envelope floor to every admissible nonnegative kernel under
the complete gamma/pole budgets. Its joint prime-payment/logarithmic-spread
bound explains why the small C(h) examples here do not improve that full
envelope. Note 10 retains the stronger d/2 cost for these aligned copies.

## 9. Exact filter and its uniform stability

Assume RH. Let \(\gamma>0\) be an actual zero ordinate of exact multiplicity \(m\), and assume a separately justified number \(0<d\le1/2\) satisfies
\[
 0<|\lambda-\gamma|<d\quad\Longrightarrow\quad
 \lambda\text{ is not a zero ordinate}.                    \tag{E1}
\]
Zeros at distance exactly \(d\) are allowed. A larger available gap may be truncated to \(1/2\). No uniform lower bound for \(d\) is inferred from RH or finite root-wall continuation.

Write
\[
 B_a(\gamma)=a\Re\frac{\xi'}\xi(1/2+a+i\gamma)
 =\sum_\lambda m_\lambda\frac{a^2}{a^2+(\lambda-\gamma)^2}.
                                                               \tag{E2}
\]
This is the full paired-product identity from the preceding notes; it includes negative ordinates, exterior zeros, and every multiplicity. The complete zeta relation is
\[
 \frac{\xi'}\xi(s)=D(s)+\frac{\zeta'}\zeta(s),\qquad
 D(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2).
                                                               \tag{E3}
\]
The pole and gamma terms in \(D\) will remain exact.

For an integer \(r\ge1\), choose
\[
 a_j=d\,2^{j-r}\quad(0\le j<r),\qquad
 c_j=\prod_{k\ne j}\frac{a_k^2}{a_k^2-a_j^2}.
\]
Partial fractions, checked by the residues at \(-a_j^2\), give
\[
 \sum_{j=0}^{r-1}c_j\frac{a_j^2}{a_j^2+v^2}
 =K_r(v):=\prod_{j=0}^{r-1}\frac{a_j^2}{a_j^2+v^2}\ge0.
                                                               \tag{E4}
\]
In particular \(\sum c_j=1\). Thus
\[
 M_r(\gamma):=\sum_jc_jB_{a_j}(\gamma)
 =m+\sum_{\lambda\ne\gamma}m_\lambda K_r(\lambda-\gamma).
                                                               \tag{E5}
\]
No negative zero contribution has been discarded when forming this signed combination.

Put \(q=1/4\), and \((q;q)_n=\prod_{k=1}^n(1-q^k)\). Directly from the displayed coefficients,
\[
 c_j=\frac{(-1)^j q^{j(j+1)/2}}
              {(q;q)_j(q;q)_{r-1-j}},
 \qquad
 \sum_j|c_j|=
 \prod_{k=1}^{r-1}\frac{1+4^{-k}}{1-4^{-k}}<2.             \tag{E6}
\]
The finite product equality is the elementary finite \(q\)-binomial identity, obtainable by expanding \(\prod_{k=1}^{r-1}(1+zq^k)\); see [DLMF 17.2.35](https://dlmf.nist.gov/17.2.E35) with \(z=-q\). For an explicit bound on the infinite product, separate \(k=1\) and use \(\log((1+x)/(1-x))\le2x/(1-x^2)\). The remaining logarithm is at most
\[
 \frac{2}{1-1/256}\sum_{k=2}^\infty4^{-k}
 =\frac{128}{765}<\log(6/5),
\]
so the whole product is less than \((5/3)(6/5)=2\). In particular, absolute error \(\nu\) in each input \(B_{a_j}\) produces less than \(2\nu\) error in \(M_r\).

## 10. Complete noncentral leakage and location payment

For \(|v|\ge d\),
\[
 K_r(v)\le2^{-r(r+1)}(d/|v|)^{2r}.                        \tag{E7}
\]
Indeed \(\prod_j a_j^2=d^{2r}2^{-r(r+1)}\).
Define disjoint noncentral count shells
\[
 n_0=\sum_{0<|\lambda-\gamma|\le1}m_\lambda,
 \qquad n_k=\sum_{k<|\lambda-\gamma|\le k+1}m_\lambda\quad(k\ge1),
\]
and pay
\[
 T_\gamma(d)=n_0+d^2\sum_{k\ge1}\frac{n_k}{k^2}.
\]
Then (E1), (E5), and (E7) prove the all-zero bound
\[
 0\le M_r(\gamma)-m\le T_\gamma(d)\,2^{-r(r+1)}
                  \le C\log(\gamma+3)\,2^{-r(r+1)}.       \tag{E8}
\]
For the last inequality use \(n_k\ll\log(\gamma+k+3)\), the standard unit-interval consequence of the Riemann–von Mangoldt formula, with multiplicities. Splitting the convergent series and using
\(\log(\gamma+k+3)\le\log(\gamma+3)+\log(k+1)\)
pays the entire tail. An explicit Riemann–von Mangoldt bound is displayed in [Simonic, equation (1)](https://arxiv.org/pdf/1910.08274), and can instantiate the absolute constant. No zero-height scan or numerical value for that constant is claimed here. Certified shell bounds may replace the coarser final expression. The half-open shell definitions prevent endpoint duplication; gap equality is harmless.

If the computed center differs from the exact \(\gamma\) by at most \(e\), there is an additional payment. With \(a_*:=a_0=d2^{-r}\),
\[
 |(\log K_r)'(v)|
 \le\sum_j\frac1{a_j}<\frac2{a_*}.
\]
Positivity and summation therefore give
\[
 |M_r(\gamma+u)-M_r(\gamma)|
 \le(e^{2e/a_*}-1)M_r(\gamma)\qquad(|u|\le e).             \tag{E9}
\]
The local zero count also gives \(m\ll\log(\gamma+3)\), so centering precision \(e\ll\tau a_*/\log\gamma\) suffices for location error \(O(\tau)\). Exact-center statements below do not silently include this extra payment.

## 11. Uniform finite-zeta precision over all selected widths

Let \(L=\log\gamma\), \(\ell=\log L\), choose a fixed typicality parameter \(\theta\in (0,1]\), and put
\[
 V=L\left(\frac1{2\ell}+\frac{\log\ell}{\ell^2}\right),
\]
\[
 R_*=V\left[\log^+\!\frac{V}{a_*L}
                  +2(1+\theta)\log\log V+C_\theta\right]. \tag{E10}
\]
Here \(C_\theta\) is a sufficiently large fixed constant. [Balazard–de Roton, Propositions 1 and 18](https://arxiv.org/pdf/0810.3587), as used in Note 08, imply under RH
\[
 |\zeta(1/2+a+i\gamma)|^{-1}\le e^{R_*}
          \qquad(a_*\le a\le d/2).                        \tag{E11}
\]
The \(\log^+\) includes their second, larger-shift regime; no estimate is continued to zero shift at fixed height.

Use one fixed integer \(N\ge2\gamma\) at all selected points, and define
\[
 A_N(s)=\sum_{n\le N}n^{-s}+\frac{N^{1-s}}{s-1},
 \qquad\zeta(s)=A_N(s)+R_N(s).
\]
[Simonic, Theorems 2 and 5](https://arxiv.org/pdf/1910.08274) give, on the disc of radius \(a/2\) about \(s_a=1/2+a+i\gamma\),
\[
 |R_N|\ll N^{-1/2},\qquad a|R_N'(s_a)|\ll N^{-1/2}.       \tag{E12}
\]
The second bound is Cauchy's inequality with the cutoff held fixed. Since \(a\le d/2\le1/4\), every such disc stays in the primary theorem's stated real-part range \((0,1]\); also \(|\Im s|/N\) stays bounded away from its endpoint. Constants are independent of \(a,r,N\).

For the needed logarithmic derivative bound, RH gives an analytic logarithm \(g=\log\zeta\) on the disc. A separate elementary sum at cutoff \(\lceil2\gamma\rceil\) gives \(\Re g\le L/2+O(1)\) there; (E11) gives \(\Re g(s_a)\ge-R_*\). The positive-real-part derivative inequality yields
\[
 a|\zeta'/\zeta(s_a)|\ll1+L+R_*.
\]
Exact division, as in Note 08, now shows that whenever \(e^{R_*}N^{-1/2}\) is sufficiently small,
\[
 \left|B_a(\gamma)-a\Re\left[D(s_a)+\frac{A_N'}{A_N}(s_a)\right]\right|
 \le C_0(1+L+R_*)e^{R_*}N^{-1/2}.                         \tag{E13}
\]
In particular all denominators \(A_N(s_a)\) are then nonzero. This pays the complex division error before taking a real part; gamma and pole terms are exactly those in (E3).

Consequently, for \(0<\tau\le1/8\), a sufficient common cutoff is
\[
 N\ge\max\left\{2\gamma,
 \left[\frac{2C_0(1+L+R_*)e^{R_*}}\tau\right]^2\right\}.  \tag{E14}
\]
After increasing the absolute constant if necessary, (E6), (E13), and (E14) give arithmetic error at most \(\tau\) in the combined expression. These are analytic error bounds, not claims about implemented floating-point roundoff; a numerical implementation would pay its finite-sum roundoff separately.

Choose \(r\) so that \(T_\gamma(d)2^{-r(r+1)}\le\tau\). With exact center and no additional arithmetic error, the finite value \(\widehat M_r\) then locates the actual integer multiplicity in
\[
                 m\in[\widehat M_r-2\tau,\widehat M_r+\tau].\tag{E15}
\]
The interval has length less than one. This recovers whichever multiplicity is present. It does not assert the recovered integer is one.

## 12. The explicit cost comparison

Fix a positive tolerance \(\tau\), and suppose the independently available gap has \(d=c/L\), with \(c\) in a fixed positive compact set. Using the last bound in (E8), one may choose
\[
 r=\sqrt{\ell/\log2}+O_\tau(1),\qquad
 a_* =\frac cL\exp\{-\sqrt{\ell\log2}+O_\tau(1)\}.         \tag{E16}
\]
Substitution into (E10) gives
\[
 2R_*=L\left[1+\sqrt{\frac{\log2}{\ell}}
                +O_{\theta,c,\tau}\!\left(\frac{\log\ell}{\ell}\right)\right].
\]
The polynomial prefactor in (E14) does not change this expansion. Thus a sufficient common cutoff has
\[
 \boxed{\displaystyle
 \log N=L\left[1+\sqrt{\frac{\log2}{\log\log\gamma}}
           +O_{\theta,c,\tau}\!\left(
             \frac{\log\log\log\gamma}{\log\log\gamma}\right)\right].}
                                                               \tag{E17}
\]
In particular, every fixed cutoff power \(N=\lceil\gamma^{1+\epsilon}\rceil\) suffices eventually for each fixed \(\epsilon>0\), at the selected \(r\) widths. The unspecified source constants have not been numerically instantiated, so (E17) is a proved asymptotic cost bound rather than an executed certificate.

For comparison, the **same** gap and coarse count budget gives for one Poisson width \(a\le d\)
\[
 0\le B_a-m\le (a/d)^2 T_\gamma(d).
\]
Paying this by \(C L\) selects \(a=d\sqrt{\tau/(CL)}\asymp L^{-3/2}\). At that selected width, (E10) and (E14) give
\[
                  N=\gamma^{3/2+o(1)}                    \tag{E18}
\]
as a sufficient cutoff. The geometric-width scheme improves this declared sufficient payment from (E18) to (E17), while its additional number of evaluation points is only \(O(\sqrt{\log\log\gamma})\) and its absolute error amplification stays below two. Neither exponent is claimed to be an optimal computational complexity. Better direct tail information, stronger reciprocal estimates, or other zeta algorithms can change this comparison.

## 13. What this does and does not provide

The input gap (E1), all noncentral zero counts, analytic remainder, division error, completion terms, and optional center uncertainty are separately visible. The method does not manufacture noncentral isolation or bound the endpoint coefficient \(\zeta^{(m)}(\rho)\). Finite wall continuation still supplies no uniform lower bound for the gap.

The signed coefficients in (E4) cancel low-order leakage but leave a nonnegative full zero kernel. At an exact double zero, the computed quantity converges to two and satisfies all the proved inequalities. The normalized endpoint controls of Note 05 obey this zero-side identity as well; their ordinary Dirichlet-series premise fails for (E10)–(E14), but this does not turn the unchanged-zeta estimate into a contradiction. No positive-coefficient or Turán argument has supplied an opposing event-conditioned arithmetic sign in this calculation.

Direct first-jet exclusion at a known zero requires a certified positive lower bound for the actual first derivative. The present extraction uses different extra information, particularly (E1), and returns the integer mass without providing that lower bound analytically. If its finite interval (E15) happens to contain only one, it certifies that particular zero; if the zero is double it instead contains two. There is no theorem here that the finite arithmetic expression must yield one at every target, and no established advantage over a direct first-jet certificate using the same complete data. The genuine gain is the bounded-tail/finite-precision cost (E8), (E6), and (E17) within the explicitly compared extraction scheme.


[review]: ../reviews/09_CONTROLS_KERNELS_AND_EXTRACTION_REVIEW_20261020.md
[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[n8]: 08_RECIPROCAL_PRECISION_AND_BANDLIMITED_ARITHMETIC_COSTS_20261020.md
[bw09]: ../../09_expanding_contour_later_collision/manuscript/main.tex
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md

[n10]: 10_UNIFORM_PRIME_PHASE_RETURN_HEIGHT_COST_20261020.md

[n11]: 11_FULL_ABSOLUTE_PRIME_ENVELOPE_AND_LOGARITHMIC_SPREAD_20261020.md
