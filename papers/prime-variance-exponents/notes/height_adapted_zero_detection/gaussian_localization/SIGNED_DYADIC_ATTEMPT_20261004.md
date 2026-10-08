# A complete signed block criterion for the Gaussian arithmetic target

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model analysis and internal cross-review are not independent
specialist refereeing or formal proof verification.
Repository base: `ef02c696bee11362286fe31c237fc169329c1812`.

This note follows the
[proved Poisson refinement](POISSON_SMALL_DIVISOR_REFINEMENT_20261004.md).
It derives an exact signed block representation, a full-target sufficient
bound from finite twisted Möbius sums, and an explicit block condition
that would activate the zero detector. Ordinary absolute and elementary
mean-square estimates do not prove that condition. No new signed saving,
zero-free box, or actual-zero certificate is claimed.

## Exact partial summation with every terminal cap

Retain \(b=3/4\), \(T=|t|\ge100\), the prescribed \(N,k,\eta_N\),
and set

\[
D=e^{\alpha k},\quad \alpha=77/5,\quad B=e^{26k},\qquad
w_k(x)=x^{-3/4}g_k(20k-\log x).
\]

The signed pair part of the refined target is

\[
S_{k,t}=\sum_{1\le r<B/D}r^{-it}
       \sum_{D<d\le B/r}\mu(d)d^{-it}\log d\,w_k(rd),
\]
\[
\mathcal G^{\rm new}_{k,t}=-S_{k,t}
                -\Phi_{k,t}(1)(1+L_D).
\tag{1}
\]

Define the right-continuous interval prefix
\(M_t(D,x)=\sum_{D<d\le x}\mu(d)d^{-it}\) and the real smooth
amplitude \(f_r(x)=\log x\,w_k(rx)\). For \(L_r=B/r\),

\[
\sum_{D<d\le L_r}\mu(d)d^{-it}f_r(d)
=M_t(D,L_r)f_r(L_r)
        -\int_D^{L_r}M_t(D,x)f_r'(x)\,dx.
\tag{2}
\]

The lower atom is excluded; the upper atom is included. The terminal
term in (2) is essential and need not vanish. No rectangular factor cap
replaces \(B/r\). A dyadic split may be made with \(Y_j=2^jD\)
and each interval \((Y_j,\min(2Y_j,B/r)]\); use the corresponding
interval prefix in (2), including the last partial block.

The carrier phase factors exactly as \(d^{-it}r^{-it}\). Differencing
between two divisor terms cancels the cofactor from that phase. An
estimate based only on a mixed oscillatory phase therefore does not
automatically create a saving.

## A sufficient finite twisted prefix estimate

Assume, as an independent arithmetic hypothesis, that for some
\(A_0>0\), \(0<\delta\le1\),

\[
|M_t(D,x)|\le A_0 x^{1-\delta}\quad(D<x\le B).
\tag{3}
\]

This is a finite interval condition, not a claim about actual Möbius sums.
An effective full-target consequence is

\[
\boxed{|S_{k,t}|\le\frac{A_0}{\delta}(2+24k)
                e^{(81/16-\alpha\delta)k},\qquad k\ge8.}
\tag{4}
\]

To prove it, put
\(q_0(z)=-3/4+(20k-\log z)/(2k)\). Then

\[
|f_r'(x)|\le\frac{w_k(rx)}x
                  [1+\log x\,|q_0(rx)|].
\]

After \(z=rx\), summing the nonnegative integral majorants in (2)
uses

\[
\sum_{1\le r<z/D}r^{\delta-1}\le(z/D)^\delta/\delta.
\]

Since \(r\ge1\) and \(x>D>1\), \(\log x\le\log z\).
The integral contribution is at most

\[
\frac{A_0}{\delta}D^{-\delta}
  \int_D^B w_k(z)[1+\log z\,|q_0(z)|]\,dz.
\tag{5}
\]

The total mass of \(w_k(z)\,dz\) is \(e^{81k/16}\). Under its
normalized measure, \(y=\log z\) is normal with mean \(41k/2\)
and variance \(2k\); \(q_0\) has mean minus one and second moment
\(1+1/(2k)\). For \(k\ge8\), Cauchy--Schwarz gives
\(\mathbb E|yq_0|<22k\), so (5) is at most
\((A_0/\delta)D^{-\delta}(1+22k)e^{81k/16}\).

The terminal terms in (2) sum to at most

\[
\frac{A_0}{\delta}D^{-\delta}B w_k(B)\log B
=\frac{A_0}{\delta}D^{-\delta}
        \frac{26k}{\sqrt{4\pi k}}e^{-5k/2}
\le\frac{A_0}{\delta}D^{-\delta}e^{81k/16}
\tag{6}
\]

for \(k\ge8\). For example \(26k/\sqrt{4\pi k}<13k\) and
\(e^{121k/16}>13k\). This proves the slightly stronger coefficient
\(2+22k\); (4) retains a simple generous coefficient. Both endpoints
and all cofactor values have been included.

## An explicit dyadic input that would exclude the box

Here is one concrete sufficient input, with no unspecified amplitude
constant. For every relevant carrier and sample, suppose that every
dyadic block \(Y_j=2^jD<B\) satisfies

\[
\boxed{\left|\sum_{Y_j<d\le x}\mu(d)d^{-it}\right|
\le Y_j^{3/5}
\quad\text{for every real }Y_j<x\le\min(2Y_j,B).}
\tag{7}
\]

All partial prefixes are required, including every value \(x=B/r\)
inside a terminal block. Summing completed blocks and the current prefix
gives \(|M_t(D,x)|<3x^{3/5}\), because
\(1/(1-2^{-3/5})<3\). The last inequality follows from
\((3/2)^5<2^3\). Thus (4) applies with \(\delta=2/5\) and
\(A_0=3\):

\[
|S_{k,t}|<\frac{15}{2}(2+24k)e^{-439k/400}.
\tag{8}
\]

Dividing by \(\eta_N\), taking the least sample, and using
\(\log(8e)<31/10\) gives

\[
\frac{|S_{k,t}|}{\eta_N}
<(720N+735)e^{-129N/100-439/100}<1/1000
\quad(N\ge10).
\tag{9}
\]

The expression decreases in \(k\ge44\) and then in \(N\ge10\).
At \(N=10\), its numerator is 7935 and its exponential exponent is
\(-1729/100\). Since \(e>8/3\) and
\(e^{1729/100}>e^{17}>(8/3)^{17}>7935000\),
the base inequality is an exact elementary check.
The retained continuum is below \(\eta_N/16\) by the Poisson note,
so (7) implies

\[
|\mathcal G^{\rm new}_{k,t}|
< (1/1000+1/16)\eta_N<\eta_N/4.
\tag{10}
\]

The existing Gaussian theorem would then exclude the candidate box
\(3/4\le\beta<1\), provided (7) holds for every covered carrier
and every prescribed sample. This is a proved conditional implication.
The finite arithmetic hypothesis (7) is unproved and is the actual gap.

## What the elementary arithmetic attempts establish

**Absolute envelope.** The divisor coefficient cumulative bound from the
finite reduction, followed by partial summation and Gaussian moments,
gives only

\[
|S_{k,t}|\le240k^2e^{81k/16}\qquad(k\ge8).
\tag{11}
\]

One way to check the coefficient is to discard only the favorable
increasing part of \(w_k\), combine its decreasing tail with the
upper-cap boundary, and bound the resulting integral by
\(\tfrac12e^{81k/16}\mathbb E[(|y|+y^2)|q_0|]\).
For \(k\ge8\), \(\mathbb Ey^2\le421k^2\),
\(\mathbb Ey^4<421^2k^4\), and \(\mathbb E q_0^2\le17/16\).
Cauchy--Schwarz bounds the coefficient by
\(11k+217k^2<240k^2\).
This is far above the detector allowance. It is an upper-envelope
failure, not a lower bound for the signed target and not an impossibility
theorem for cancellation between cofactors.

**Elementary carrier mean square.** On a divisor block \((Y,2Y]\),
for any carrier interval \(I\) of length \(H_0\), expanding the square
and bounding all off-diagonal integrals gives

\[
\int_I\left|\sum_{Y<d\le2Y}\mu(d)d^{-it}\right|^2dt
\le2H_0Y+16Y^2(1+\log(2Y)).
\tag{12}
\]

Indeed \(\log(n/m)\ge(n-m)/(2Y)\) and the harmonic sum bounds
every pair. The estimate is insensitive to coefficient phases.
Even over a broad admissible carrier interval with \(H_0\) comparable
to \(e^N\), the block scale \(Y\ge e^{77k/5}\) is much larger.
The corresponding root-mean-square envelope has relative size of order
\(H_0^{-1/2}\) times logarithmic factors, whereas (7) needs
\(Y^{-2/5}\). At the least samples, those exponential scales are
approximately \(e^{-N/2}\) and \(e^{-24.64N}\), respectively.
More importantly, an average does not exclude an exceptional carrier,
which could be the hypothetical zero's ordinate. No mean square is
silently promoted to a pointwise bound.

**Coherent coefficient control.** Any argument using only
\(|\mu(d)|\le1\) must also tolerate the formal coefficients
\(c_d=d^{it}\). At that carrier, \(\sum c_dd^{-it}\) equals the
number of terms, rather than a \(Y^{3/5}\) bound. These are synthetic
coefficients, not actual Möbius values. The control shows why phase
factorization and coefficient moduli alone cannot prove (7).

## The strength and limits of the missing input

For a general bound (3) with an amplitude constant subexponential in
\(k\), the sufficient envelope (4) beats the least-sample scale only
when

\[
\delta>\frac{81/16+\log(8e)/4}{77/5}
\approx0.3787247.
\tag{13}
\]

This improves the old coefficient-15 diagnostic, approximately 0.388824,
but remains a substantial arithmetic obligation. It is a diagnostic of
this absolute-over-cofactors bound, not a necessary barrier for the
complete signed sum.

An untwisted global Mertens hypothesis \(|M(x)|\le Cx^{1-\delta}\)
does not transfer without height cost. For \(0<\delta<1\), exact
partial summation gives at most

\[
|M_t(D,x)|\le C[2+T/(1-\delta)]x^{1-\delta}.
\tag{14}
\]

In the worst saved height budget this increases the numerator in (13)
by \(1/4\), to a threshold approximately 0.3949585. More fundamentally,
such a global power hypothesis is itself a strong zero-free input.
For a fixed carrier, a global twisted-prefix bound of order \(x^{3/5}\)
would analytically continue \(1/\zeta(s+it)\) into \(\Re s>3/5\).
It cannot be imported as routine arithmetic. The finite condition (7)
is a legitimate local target, but it still requires an independent proof.

The complete signed identity also retains every forbidden zero residue:
for fixed \(D\), its infinite high-divisor coefficient series is
\(-\zeta'/\zeta(s)+\zeta(s)M_{\log,D}(s)\), as proved in the finite
reduction. The second term is analytic and zero at a nontrivial zero.
Changing the cutoff does not attenuate the zero's multiplicity residue.
The arithmetic estimate therefore cannot be obtained by re-inserting
that identity and assuming the desired zero mode has disappeared.

The [cofactor-aware continuation](COFACTOR_AWARE_SIGNED_CRITERION_20261004.md)
now proves the amplitude-derivative lemma and its complete conditional
budget. It preserves more cofactor cancellation than (4), weakening the
sufficient dyadic input from \(Y^{3/5}\) to \(Y^{13/20}\).
That new finite arithmetic input also remains unproved. The present
continuation records the simpler complete block criterion and its
ordinary-estimate controls; no independent signed saving is obtained.

The [internal review](../../../reviews/height_adapted_zero_detection/gaussian_localization/POISSON_AND_SIGNED_REVIEW_20261004.md)
and [replay guide](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
record the proof checks, exact algebra, and limitations. No actual
enormous Möbius sum was evaluated, and no manuscript or historical
snapshot was changed.
