# Growing norm-compensated cofactor differences still retain the coherent power

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: an internal analytic deduction under Note 24's imported fixed-field
prime ideal theorem and lattice count, with exact finite checks. This is
neither independent specialist validation nor a bound for the full response.

[Note 27](27_COHERENT_COVARIANCE_AND_FINITE_SPAN_BARRIER_20261009.md)
leaves growing cofactor combinations outside its fixed finite-span result.
This note tests a particularly strong version: compensate the prime-pair
Jacobian exactly, then take a growing mixed finite difference which kills
its first arbitrarily many logarithmic terms. The continuum still has size
\(D^{1-o(1)}\). In a stated growing range the imported prime ideal theorem
transfers this to the actual signed response, giving coherent energy
\(D^{16/15-o(1)}\). For larger combinations, that transfer requires a
stronger error estimate; the continuum calculation alone does not prove
an actual-response lower bound.

## 1. A growing combination of complete actual blocks

Use all conventions of
[Note 24](24_SHORT_FAMILY_FINITE_COFACTOR_PAIRING_20261008.md), including
the trivial permitted fixed twist, physical deletion zeros,
\(H=D^{2/5}\), \(z=\sqrt{CD}\), \(B=\log z\), the fixed complex
nonzero mean-zero profile \(W\), and its complete blocks
\(\mathcal B_{u,M}\). Let
\[
 P=\prod_{i=1}^J p_i,\quad q_i=Np_i,\quad h_i=\log q_i,
 \quad NP\le D^\beta,\qquad 0<\beta<1/20.                 \tag{1}
\]
The good prime ideals are distinct; equal norms are allowed. Both \(P\)
and \(J\) may grow. Define
\[
 a_M=NM\prod_{p\mid P/M}(1-Np),\qquad
 \mathcal L_{u,P}=\sum_{M\mid P}a_M\mathcal B_{u,M}.       \tag{2}
\]
These are signed, scale-dependent coefficients on complete actual blocks.
This is a method test, not a claimed decomposition of the original full
response with its prescribed coefficients.

On the actual coherent rows
\[
 \mathcal C_P(D)=\{u=v^6:0<Nv\le D^{1/15},\ (v,P)=1\},
\]
the coefficient of each divisor cofactor \(b\mid P\) is exactly
\[
 \mu_K(b)\sum_{\substack{M\mid P\\b\mid M}}a_M
       =\mu_K(b)Nb.                                    \tag{3}
\]
Indeed each prime outside \(b\) contributes \((1-q_i)+q_i=1\).
Note 24's cutoff and phase checks apply uniformly to every \(M\mid P\).
Thus, with ordered distinct prime pairs and both original upper cutoffs,
\[
 \mathcal L_{u,P}
 =\sum_{b\mid P}\mu_K(b)Nb
     \sum_{\substack{q\ne r\text{ good primes}\\Nq,Nr\le z}}
          W(Nb\,Nq\,Nr/D).                              \tag{4}
\]
No physical zero was overwritten. The large pair primes exceed \(NP\)
on the support, so the common exclusion condition is automatic there.
Different prime ideals of equal norm are kept distinct in (3)--(4).

The exact coefficient cost is
\[
 \sum_{M\mid P}|a_M|=\prod_{i=1}^J(2q_i-1),
 \qquad NP\le\sum_M|a_M|\le 2^J NP.                     \tag{5}
\]
There are \(2^J\) blocks. These costs cannot be omitted when such a
combination is proposed as part of a proof for the full response.

## 2. What the growing cancellation actually removes

Let \(v(t)=\log(C/t)\), and keep Note 24's exact kernel
\[
 F_B(x)=\frac{2}{2B-x}\log\frac{B}{B-x}
       =\frac1B f(x/B),\qquad
 f(y)=\frac{-\log(1-y)}{1-y/2}.                          \tag{6}
\]
Its continuum for (4) is
\[
 A_{P,W}(D)=D\int_c^C W(t)K_{P,B}(v(t))\,dt,
 \quad K_{P,B}(v)=\sum_{b\mid P}\mu_K(b)F_B(v+\log Nb).
                                                               \tag{7}
\]
The norm factor in (3) has canceled the essential Jacobian \(1/Nb\).
Unlike the unweighted Euler subtraction, this does remove many terms:
\[
 \sum_{b\mid P}\mu_K(b)(\log Nb)^k=0\quad(0\le k<J),
 \qquad
 \sum_{b\mid P}\mu_K(b)(\log Nb)^J
       =(-1)^J J!\prod_i h_i.                           \tag{8}
\]
These identities are valid even when some \(q_i\) coincide.
The fundamental theorem of calculus gives the more useful exact formula
\[
 K_{P,B}(v)=(-1)^J\int_{\prod_i[0,h_i]}
                F_B^{(J)}(v+t_1+\cdots+t_J)\,d\mathbf t.
                                                               \tag{9}
\]
It retains every cofactor shift before taking an absolute value.

## 3. Uniform lower bound after a growing number of differences

Let \(k_0\ge1\) be the first nonzero moment
\(M_k(W)=\int W(t)v(t)^k\,dt\). Set \(V=\log(C/c)\),
\(L_P=\log NP\), and \(n=J+k_0\). Distinct prime ideals in this
quadratic field have at most two representatives of any integer norm.
Consequently
\[
 NP\ge (\lfloor J/2\rfloor !)^{2},\qquad
 J=O_\beta\left(\frac{\log D}{\log\log D}\right).        \tag{10}
\]
Only the upper bound is needed; the factorial estimate is deliberately
weak. In particular \(n/B\to0\), and
\(L_P+V\le\theta B\) eventually for some fixed \(\theta<1\).

For completeness the growing-order Taylor error has a uniform budget.
Write \(g(y)=-\log(1-y)\), \(h(y)=(1-y/2)^{-1}\).
All terms in the Leibniz formula for \(f^{(m)}=(gh)^{(m)}\)
are nonnegative on \([0,1)\). For a term with at least one derivative
on \(g\), its logarithmic derivative is at most
\((m+1)/(1-y)\). The derivative \(g'h^{(m)}\) of the term
with no derivative on \(g\) is at most
\(f^{(m)}(y)/(2-y)\), by comparison with its existing term
\(m g'h^{(m-1)}\). The other part of that term has logarithmic
derivative \((m+1)/(2-y)\). Therefore, for \(m\ge1\),
\[
 0<F_B^{(m+1)}(x)
       \le\frac{m+2}{B-x}F_B^{(m)}(x),\qquad 0\le x<B. \tag{11}
\]
The positive series in Note 24 also gives
\[
 F_B^{(m)}(x)\ge F_B^{(m)}(0)
 =m!\alpha_m B^{-m-1}\ge(m-1)!B^{-m-1},\quad m\ge1.     \tag{12}
\]
Here \(\alpha_m=\sum_{j=1}^m2^{-(m-j)}/j\ge1/m\).

Expand (9) in the bounded variable \(v(t)\) through order \(k_0\).
The lower moments vanish, giving
\[
 \frac{A_{P,W}(D)}D
 =\frac{(-1)^J M_{k_0}(W)}{k_0!}
      \int_{\prod[0,h_i]}F_B^{(n)}(\textstyle\sum t_i)\,d\mathbf t
       +E.                                             \tag{13}
\]
By integrating (11), the absolute value of the error, divided by the
absolute value of the displayed main term, is at most
\[
 C_W\frac{n+2}{B-L_P-V}
        \exp\!\left(\frac{(n+2)V}{B-L_P-V}\right)=o(1). \tag{14}
\]
For example this follows directly from the integral Taylor remainder
bounded by \(\int|W|\,V^{k_0+1}/(k_0+1)!\) times the next
derivative. This bound works for complex \(W\): the leading scalar
\(M_{k_0}(W)\) is nonzero and the derivative integral is positive.
It does not rely on a positivity assumption for the profile.

Equations (12)--(14) imply, uniformly under (1),
\[
 |A_{P,W}(D)|\ge c_W D
       \frac{(J+k_0-1)!\prod_i h_i}{B^{J+k_0+1}}
       =D^{1-o(1)}.                                    \tag{15}
\]
For the last equality as a lower bound, use \(h_i\ge\log2\),
Stirling's elementary lower bound, and (10). The negative logarithm
of the factor in (15) is at most
\[
 J\log(eB/J)+O_W(J+\log B)
   =O_{\beta,W}\!\left(
        \frac{\log D\,\log\log\log D}{\log\log D}\right)
   =o(\log D).                                         \tag{16}
\]
A direct upper bound from (7),
\(|K_{P,B}|\le2^J\sup_{0\le x\le L_P+V}|F_B(x)|\ll_\beta2^J/B\),
also gives \(|A_{P,W}(D)|\le D^{1+o(1)}\). Only the lower bound is
needed for the obstruction. Growing cancellation order has produced a
subpower attenuation, not the fixed power required by the target.

## 4. Actual-response transfer and its limit

Multiplying Note 24's individual prime-pair errors by the actual weights
\(Nb\) in (4) gives
\[
 \mathcal L_{u,P}=A_{P,W}(D)
   +O_{\beta,W}(D\,2^J e^{-c_\beta\sqrt{\log D}})
   +O_W\!\left(\sqrt D\prod_i(1+\sqrt{q_i})\right).      \tag{17}
\]
The second error pays the removed prime-square diagonal. It is bounded
by \(D^{1/2+\beta/2}2^J=D^{1/2+\beta/2+o(1)}\).
The first error is a signed sum estimated absolutely; no unproved
cancellation of the prime ideal theorem errors is used.

An explicit sufficient growing regime for (17) to preserve (15) is
\[
 \boxed{J=o\!\left(
       \frac{\sqrt{\log D}}{\log\log D}\right).}        \tag{18}
\]
In this regime (16)'s attenuation is \(o(\sqrt{\log D})\),
so the main term is at least \(D e^{-o(\sqrt{\log D})}\);
both errors in (17) are smaller. More generally it suffices that
\(J\log(eB/J)+O_W(J+\log B)=o(\sqrt{\log D})\).
Thus the actual response, uniformly on \(\mathcal C_P\), satisfies
\[
 |\mathcal L_{u,P}|\ge D^{1-o(1)}.                     \tag{19}
\]
This covers truly growing numbers of blocks, for example a slowly growing
sequence of good prime ideals with \(J=\lfloor(\log D)^{1/3}\rfloor\)
and \(NP\le D^\beta\).

The coprime lattice count from Note 24, with \(X=D^{1/15}\), is
\[
 \#\{v:0<Nv\le X,(v,P)=1\}
 =\kappa_K X\prod_{p\mid P}(1-(Np)^{-1})
      +O_K(2^J(\sqrt X+1)).                            \tag{20}
\]
Its Euler product is \(\gg_\beta1/\log\log D\), as already proved
there. Equation (10) gives \(2^J=D^{o(1)}\), so the error is negligible.
Counting each sixth-power image once costs at most six. With the
original weights \(w_u=D^{-1}\Phi(Nu/H)\), this yields
\[
 \sum_{u\in\mathcal C_P}w_u=D^{-14/15-o(1)},\qquad
 \boxed{\sum_u w_u|\mathcal L_{u,P}|^2
                   \ge D^{16/15-o(1)}}                 \tag{21}
\]
under (18). This is incompatible with \(D^{4/5+\varepsilon}\)
for every fixed \(\varepsilon<4/15\) for this method test.

For \(J\) approaching the larger budget in (10), (15) is still a
continuum lower bound, but the first error in (17) can exceed it. This
note does **not** extend (19)--(21) to that regime. A proposed large-order
arithmetic compensation must pay both the coefficient cost (5) and a
stronger signed error estimate; the present PNT input does not supply it.

## 5. Consequence for the continuation

This removes another plausible bounded repair: exact Jacobian compensation
and a growing number of cofactor differences, within (18), still retain
the coherent power. It strengthens the case for working on the actual
mean and centered covariance of the broader remaining-product response
in Note 27, rather than optimizing this cofactor filter. Arbitrary
scale-dependent combinations, other product shapes, and cancellation
against the original remainder remain open. A lower bound for (2) is
not a lower bound for their full sum.

The [checker](../../numerics/check_growing_cofactor_barrier.py) and its
[record](../../numerics/growing_cofactor_barrier_record_20261009.json)
test the exact divisor coefficients, their cost, norm grouping, vanishing
finite-difference moments, the integral identity for polynomial kernels,
positive-series coefficients, and the termwise derivative comparisons
in (11). Formal rational shifts in these finite tests are labeled as such;
they are not substituted for logarithms in the analytic proof. The checker
does not certify the imported PNT, lattice asymptotic, or unbounded limit.

Two runs passed 5,881 exact assertions. A separate same-model read-through
checked the derivative ratio, complex-profile Taylor error, PNT transfer
range, diagonal cost and coherent-row count; it suggested the simpler
upper bound now displayed above. This remains internal validation.
