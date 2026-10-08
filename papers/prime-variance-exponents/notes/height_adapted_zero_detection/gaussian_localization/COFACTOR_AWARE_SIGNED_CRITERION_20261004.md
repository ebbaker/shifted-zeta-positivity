# A signed Gaussian criterion retaining cofactor cancellation

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model analysis and internal cross-review are not independent
specialist refereeing or formal proof verification.
Repository base: `ef02c696bee11362286fe31c237fc169329c1812`.

This supplement proves an amplitude derivative bound for the entire
cofactor Poisson discrepancy and uses it to weaken the sufficient signed
input in the [first signed block attempt](SIGNED_DYADIC_ATTEMPT_20261004.md).
The arithmetic hypothesis remains unproved. It is a finite twisted-Möbius
prefix bound of exponent \(13/20\), in place of the earlier sufficient
exponent \(3/5\). This is an improvement of a proved conditional transfer,
not a proved saving for actual Möbius sums or a new zero-free region.

The cofactor phase is retained during a conditional secondary deletion.
Its amplitude derivative has no added factor of the carrier height.
Every Poisson mode, cofactor, product endpoint, and finite continuum is
paid for below. No numerical evaluation of the enormous arithmetic
target is used.

## The finite target and the unproved arithmetic input

Use the Gaussian definitions and saved detector samples from the
[finite Gaussian reduction](FINITE_GAUSSIAN_MOBIUS_REDUCTION_20261004.md)
and [unconditional Poisson refinement](POISSON_SMALL_DIVISOR_REFINEMENT_20261004.md):

\[
b=3/4,\quad T=|t|\ge100,\quad
g_k(v)=\frac{e^{-v^2/(4k)}}{\sqrt{4\pi k}},\quad
W(x)=x^{-b-it}g_k(20k-\log x),
\]
\[
\Phi=\int_0^\infty W(x)\,dx,
\quad D=e^{77k/5},\quad B=e^{26k},\quad
\eta_N=(8e)^{-N},
\quad k=4(N+1),4(N+2),\ldots,8N.
\tag{1}
\]

Here \(N\ge10\), \(T+1<e^N\), and, for a zero-exclusion application,
the prescribed radius-three guard-count bound holds uniformly over the
covered carrier interval. Define, for any fixed real cutoff \(U>1\),

\[
P_U^B=\sum_{\substack{d>U,r\ge1\\dr\le B}}
             \mu(d)\log d\,W(dr),\qquad
L_U=\sum_{d\le U}\mu(d)\log d/d,
\]
\[
\mathcal G_U=-P_U^B-\Phi(1+L_U).
\tag{2}
\]

The target to be bounded is \(\mathcal G_D\), the refined target already
defined in the Poisson note. The product cap is weak, the lower divisor
cutoff is strict, and its active cofactor range is \(r<B/D\).

The following finite input is sufficient. Put \(Y_j=2^jD\). For every
relevant carrier and sample, suppose that

\[
\boxed{
\left|\sum_{Y_j<d\le x}\mu(d)d^{-it}\right|
\le Y_j^{13/20}
\quad\text{for every }Y_j<x\le\min(2Y_j,B),\quad Y_j<B.}
\tag{3}
\]

Every partial prefix is required, including the terminal values arising
from a product cap. Equation (3) is an independent, currently unproved
arithmetic hypothesis. It is not inferred from the contour calculation.
The proved result of this note is the implication

\[
\boxed{\text{(3)}\quad\Longrightarrow\quad
 |\mathcal G_D|<(1/8+1/500)\eta_N<\eta_N/4.}
\tag{4}
\]

Together with the existing detector and its omitted-error bounds, this
would exclude the covered box \(3/4\le\beta<1\). The universal carrier
and sample quantifiers in (3) are essential.

## A derivative lemma for the complete cofactor amplitude

For real \(d>0\), set

\[
R(d)=\sum_{r\ge1}W(dr)-\Phi/d,\qquad C(d)=d^{it}R(d).
\tag{5}
\]

The full cofactor sum and its derivatives converge locally uniformly in
\(d>0\), by logarithmic Gaussian decay. The zero extensions of the
functions below are Schwartz and flat at zero. Thus ordinary
differentiation, Poisson summation, and the Fourier contour rotation are
legitimate, without a truncated cofactor sum or a lost endpoint.

**Cofactor amplitude lemma.** For \(T\ge100\), \(k\ge8\), and every
\(d>0\),

\[
\boxed{|C(d)|<\frac18 T^{5/2}d^{3/2}e^{-639k/16},\qquad
 |dC'(d)|<\frac14 T^{5/2}d^{3/2}e^{-639k/16}.}
\tag{6}
\]

To verify the derivative statement without a height loss, define

\[
q_0(x)=-b+\frac{20k-\log x}{2k},\qquad V(x)=W(x)q_0(x).
\]

Since \(xW'(x)+itW(x)=V(x)\), integration by parts gives
\(\int V=(it-1)\Phi\). Consequently the exact differentiated identity is

\[
dC'(d)=d^{it}\left[
  \sum_{r\ge1}V(dr)-\frac1d\int_0^\infty V(x)\,dx\right].
\tag{7}
\]

The carrier factors cancel before the amplitude is estimated. It would
be wasteful to bound the derivative of \(R\) before factoring \(d^{-it}\).

Here is an explicit bound for all Fourier modes in both (5) and (7).
Put \(p=5/2\), \(\theta=1/T\), and use Fourier convention
\(e^{-2\pi i\xi x}\). For a nonzero mode \(m\), rotate to
\(z=xe^{-i\operatorname{sgn}(m)\theta}\). The same endpoint arc
argument as in the Poisson refinement applies also to \(V\), whose extra
logarithmic factor does not defeat the Gaussian decay. If
\(w(x)=|W(x)|\), then

\[
|\widehat W(m/d)|\le
 e^{1+\theta^2/(4k)}\int_0^\infty
        w(x)e^{-2\pi |m|\sin\theta\,x/d}\,dx.
\tag{8}
\]

For \(u>0\), \(e^{-u}\le(p/e)^p u^{-p}\). The exact moment is

\[
J_p=\int_0^\infty w(x)x^{-p}\,dx=e^{-639k/16}.
\tag{9}
\]

After summing every nonzero mode, Poisson therefore yields

\[
|R(d)|\le K_pT^p d^{p-1}J_p,\qquad
K_p=\frac{2\zeta(p)e^{1+\theta^2/(4k)}(p/e)^p}
              {(2\pi T\sin\theta)^p}<\frac18.
\tag{10}
\]

Here each Fourier mode is bounded before summing it, so \(\zeta(p)\)
pays for that mode sum. The earlier geometric-denominator proof uses a
different majorant and sums the modes before applying its power bound;
it does not need this factor.

The last inequality has an elementary rational verification:
\(\zeta(5/2)<5/3\), \((p/e)^p<1\), and
\(e^{1+\theta^2/(4k)}<3\). For the exponential bound use
\(e<11/4\), \(\theta^2/(4k)\le1/320000\), and
\(e^u\le(1-u)^{-1}\). Also
\(T\sin(1/T)\ge59999/60000\) and \(\pi>3\), so
\(2\pi T\sin\theta>59/10\). Its \(5/2\) power is above 80,
because \(\sqrt{59/10}>12/5\) and
\((59/10)^2(12/5)>80\). The numerator in (10) is below ten.

For \(V\), the rotated amplitude has the additional factor
\[
-b+\frac{20k-\log x-i\varphi}{2k},
\qquad |\varphi|=\theta.
\]
Under the normalized positive measure \(w(x)x^{-p}\,dx/J_p\),
the real part of this factor has mean \(p-1=3/2\) and variance
\(1/(2k)\). Cauchy--Schwarz therefore bounds its absolute mean by

\[
\sqrt{(p-1)^2+1/(2k)+\theta^2/(4k^2)}<2.
\tag{11}
\]

Applying (8)--(10) to \(V\), followed by (7), proves the second
inequality in (6). This uses the entire Poisson series; no stationary
phase approximation or uncharged transition range is present.

## Conditional secondary deletion with no added carrier factor

Let \(M_t(D,x)=\sum_{D<d\le x}\mu(d)d^{-it}\). Summing the completed
dyadic blocks and the current prefix in (3) gives

\[
|M_t(D,x)|<3x^{13/20}\quad(D<x\le B),
\tag{12}
\]

because \(1/(1-2^{-13/20})<1/(1-2^{-3/5})<3\).
The last strict inequality follows from \((3/2)^5<2^3\).

Choose the real secondary cutoff and power parameter

\[
E=e^{71k/4},\qquad \delta=7/20,\qquad p-\delta=43/20.
\tag{13}
\]

In particular \(D<E<B\). The secondary lattice error is

\[
S_{D,E}=\sum_{D<d\le E}\mu(d)\log d\,R(d)
       =\sum_{D<d\le E}\mu(d)d^{-it}\log d\,C(d).
\tag{14}
\]

Exact partial summation, with the lower atom excluded and upper atom
included, gives

\[
S_{D,E}=M_t(D,E)\log E\,C(E)
 -\int_D^E M_t(D,x)\frac{d}{dx}[\log x\,C(x)]\,dx.
\tag{15}
\]

Using (6), (12), and \(\log x\le\log E\), the full boundary and
integral are bounded by

\[
|S_{D,E}|<\frac38 T^p e^{-639k/16}E^{p-\delta}
 \left[\log E+\frac{1+2\log E}{p-\delta}\right]
 <15kT^{5/2}e^{-71k/40}.
\tag{16}
\]

For the final coefficient, before multiplying by three the bracket and
factor \(1/8\) equal
\(5893k/1376+5/86<5k\) for \(k\ge8\). The exponent is exact:
\((71/4)(43/20)-639/16=-71/40\).

The derivative in (15) hits the complete cofactor amplitude. Its
Gaussian derivative was paid for by (7)--(11); no factor \(T\) was
added after the original \(T^{5/2}\) Poisson cost.

## The complete high-divisor sum with its product cap

For \(E<x\le B\), (12) also gives

\[
|M_t(E,x)|=|M_t(D,x)-M_t(D,E)|<6x^{13/20}.
\tag{17}
\]

The full-target partial-summation bound from the first signed attempt
applies to any lower divisor cutoff greater than one. To make its
endpoint and cofactor accounting explicit here, write

\[
P_E^B=\sum_{1\le r<B/E}r^{-it}
      \sum_{E<d\le B/r}\mu(d)d^{-it}f_r(d),
\qquad f_r(x)=\log x\,w(rx).
\]

For each \(r\), the exact terminal term is
\(M_t(E,B/r)f_r(B/r)\), and the integral is against
\(f_r'(x)=w(rx)[1+\log x\,q_0(rx)]/x\).
After changing variables \(z=rx\), summing its nonnegative majorants
uses
\(\sum_{1\le r<z/E}r^{\delta-1}\le(z/E)^\delta/\delta\).
Thus no rectangle replaces the cap \(B/r\).

The mass of \(w(z)\,dz\) is \(e^{81k/16}\). Under the normalized
measure, \(\log z\) has mean \(41k/2\) and variance \(2k\), while
\(q_0\) has mean minus one and second moment \(1+1/(2k)\).
For \(k\ge8\), Cauchy--Schwarz gives
\(\mathbb E|\log z\,q_0(z)|<22k\).
The terminal terms sum to at most
\((6/\delta)E^{-\delta}B w(B)\log B\), which is below
\((6/\delta)E^{-\delta}e^{81k/16}\).
These complete contributions give the convenient bound

\[
|P_E^B|<\frac6\delta(2+24k)
            e^{(81/16-(71/4)\delta)k}
 =\frac{120}{7}(2+24k)e^{-23k/20}.
\tag{18}
\]

Every cofactor and terminal partial block is included. The carrier twist
is retained in the signed Möbius prefixes; differentiating the weights
does not differentiate that twist.

## Effective budgets at every saved sample

Both \(k e^{-71k/40}\) and \((2+24k)e^{-23k/20}\) decrease for
\(k\ge44\). Use \(T^{5/2}<e^{5N/2}\),
\(\log(8e)<31/10\), and the least sample \(k=4(N+1)\).
Equations (16) and (18) give

\[
\frac{|S_{D,E}|}{\eta_N}
 <60(N+1)e^{-3N/2-71/10}<1/1000,
\]
\[
\frac{|P_E^B|}{\eta_N}
 <\frac{120}{7}(96N+98)e^{-3N/2-23/5}<1/1000
 \qquad(N\ge10).
\tag{19}
\]

The two displayed right sides decrease in \(N\ge10\). At \(N=10\),
the first is \(660e^{-221/10}\) and the second is
\((126960/7)e^{-98/5}\). Their bounds by \(1/1000\) require no
floating calculation: \(e>5/2\),
\((5/2)^{22}>660000\), and
\((5/2)^{19}>126960000/7\) suffice. These are exact rational
inequalities. For scale only, the two base envelopes are approximately
\(1.666\cdot10^{-7}\) and \(5.577\cdot10^{-5}\).

The continuum at the secondary cutoff is retained exactly. The finite
harmonic bound gives

\[
|\Phi(1+L_E)|
\le[1+(71k/4)+(71k/4)^2]e^{-k(T^2-81/16)}
<334k^2e^{-k(T^2-81/16)}<\eta_N/16.
\tag{20}
\]

For example, for \(k\ge44\), \(334k^2<e^k\) and
\(\eta_N>e^{-k}\); the remaining exponent
\(T^2-81/16-2\) exceeds 9992. The polynomial inequality follows
from monotonicity of \(e^k/k^2\) for \(k>2\) and its base at 44.

## Exact secondary-cutoff identity and the full tail

The secondary cutoff was conditional. It has not replaced the original
unconditional deletion theorem. Define its strict product tail

\[
J_{D,E}^B=\sum_{\substack{D<d\le E,r\ge1\\dr>B}}
                 \mu(d)\log d\,W(dr).
\]

The finite product sums in (2), the full cofactor identity, and (14)
give exactly

\[
P_D^B-P_E^B=\Phi(L_E-L_D)+S_{D,E}-J_{D,E}^B,
\]
\[
\boxed{\mathcal G_D=\mathcal G_E-S_{D,E}+J_{D,E}^B.}
\tag{21}
\]

Both continuum coefficients and the tail sign in (21) are necessary.
There is no replacement of a weak product cap by an infinite sum
without paying its strict upper tail.

The saved product-tail argument bounds this restricted tail as well.
For every product \(n\), its absolute divisor coefficient is at most
\(\sum_{d\mid n}\log d=\tau(n)\log n/2\), so the same cumulative
coefficient majorant and Gaussian integration give

\[
|J_{D,E}^B|\le250k^{3/2}e^{-5k/2}<\eta_N/16.
\tag{22}
\]

This uses no Möbius cancellation and includes every divisor coefficient
in the omitted sector. Combining (19)--(22) proves

\[
|\mathcal G_D|\le|P_E^B|+|\Phi(1+L_E)|+|S_{D,E}|+|J_{D,E}^B|
 <(1/8+1/500)\eta_N<\eta_N/4,
\]

which is (4). The existing unconditional small-divisor error, complete
product-tail error, and fixed-line spectral remainder remain those of
the saved detector. Each is strictly below \(\eta_N/16\).

## What was improved and what remains open

The first signed attempt took absolute values over all cofactors after
partial summation. That sufficient envelope required a divisor saving
exponent above approximately 0.378725 when its amplitude constant is
subexponential in \(k\). The present proof retains cofactor cancellation
in the secondary deletion and establishes the weaker concrete input
\(\delta=7/20\), with exact all-sample constants.

For a scale diagnostic, let \(c=81/16+\log(8e)/4\) and keep
\(p=5/2\). A secondary cutoff coefficient \(\beta\) must satisfy
\(\beta\delta>c\) for the retained pair bound and
\(\beta(p-\delta)<p(81/4-p)-c\) for the secondary deletion,
ignoring only polynomial amplitude costs. They are jointly feasible
when

\[
\delta>\frac{c}{81/4-p}\approx0.3285837.
\tag{23}
\]

The choice \(\beta=71/4=81/4-p\) balances these two exponent costs.
The proved explicit input \(\delta=7/20\) lies comfortably above
(23). Equation (23) is a diagnostic of these sufficient envelopes;
it is not a necessary barrier for the true signed target or a proof of
any arithmetic saving.

Actual Möbius prefixes have not been bounded as in (3). Ordinary
coefficient moduli, phase factorization, or a carrier mean square do not
provide it. The earlier coherent-coefficient control applies unchanged:
formal coefficients \(c_d=d^{it}\) obey \(|c_d|=1\) but have a prefix
of order the number of terms at that carrier. Thus the new derivative
lemma cannot by itself produce a Möbius saving. A mean square also needs
separate control at every exceptional carrier, including a hypothetical
zero's ordinate.

A global twisted-prefix bound of order \(x^{13/20}\), unlike the
finite hypothesis (3), would itself analytically continue
\(1/\zeta(s+it)\) into \(\Re s>13/20\). It must not be imported
as routine arithmetic. The original high-divisor Dirichlet identity
also retains the multiplicity residue at every forbidden nontrivial
zero. Neither the unconditional cutoff improvement nor the conditional
secondary deletion removes that zero coefficient.

The next actual arithmetic task is to prove a finite bound such as (3),
or a weaker complete weighted estimate that bypasses uniform prefix
control. The present result narrows and strengthens the conditional
interface while leaving that central signed estimate open.

The [internal review](../../../reviews/height_adapted_zero_detection/gaussian_localization/POISSON_AND_SIGNED_REVIEW_20261004.md)
and [exact replay guide](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
record the proof checks, arithmetic certificates, and their limits.
