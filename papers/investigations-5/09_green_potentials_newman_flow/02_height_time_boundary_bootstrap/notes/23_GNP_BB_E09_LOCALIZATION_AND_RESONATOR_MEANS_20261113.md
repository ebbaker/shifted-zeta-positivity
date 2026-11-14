# GNP-BB-E09 — localization and resonator means of the exact Poisson tail

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Proof dispatch explicitly selected
**gpt-6.1-sol / ultra**. Independent backend and usage metadata are unavailable.

**Status.** Proved in-note under the stated classical logarithmic-phase
exponent-pair input. Additional-agent assessment E10 is pending. This
executes the frozen [E09 r1 packet][packet] selected in [Note20][decision]
and [Decision05][b05]. [Notes21][upper] and [22][resonance] supply the
bounded comparisons. The result is a quantitative estimate of the actual
moment and a scoped limitation of a lower-witness method, with the
classification and control screen in §7. [Result index][results],
[heat-flow cluster11][r11], [avoid index][avoid].

## 1. Fixed kernel, clock and population

For sufficiently large real \(X\), use the [Note15][green] definitions
\[
 L_X=\log(X/(4\pi)),\qquad t_X=1/L_X,\qquad
 \tau_X=X/2+\pi/(8L_X),\qquad
 w_n(X)=n^{-65/64}\exp((\log n)^2/(4L_X)).
\]
Write
\[
 K_X=\lfloor e^{L_X/32}\rfloor,\quad N_X=\lfloor e^{L_X/2}\rfloor,\quad
 K_X^{\mathrm m}=\lfloor e^{3L_X/64}\rfloor,\quad
 N_X^{\mathrm m}=\lfloor e^{5L_X/16}\rfloor,
\]
and define
\[
 \begin{split}
 T_X(v)&=\sum_{K_X<n\le N_X}w_n(X)e^{i(\tau_X+v/2)\log n},\\
 M_X(v)&=\sum_{K_X^{\mathrm m}<n\le N_X^{\mathrm m}}
                        w_n(X)e^{i(\tau_X+v/2)\log n}.
 \end{split}
\]
At observation height \(37/64\) above the real axis and strip lower edge
\(17/32\), put \(H=5/64\), \(\theta=\pi(3/64)/H=3\pi/5\). The bottom-edge
strip kernel is
\[
 P(v)=\frac{\sin\theta}{2H(\cosh(\pi v/H)-\cos\theta)}\ge0.
\]
The substitution \(s=\tanh(\pi v/(2H))\) reduces its integral to
\((\sin\theta/\pi)\int_{-1}^1 ds/[(1-\cos\theta)+(1+\cos\theta)s^2]
=1-\theta/\pi=2/5\). Also \(P(v)\ll e^{-\pi |v|/H}\) for \(|v|\ge1\).
Write \(\|f\|_P=(\int_{\mathbb R}P(v)|f(v)|^2\,dv)^{1/2}\),
\(Q(X)=\|T_X\|_P^2\), and \(Q_M(X)=\|M_X\|_P^2\).
The spatial integral uses the time \(t_X\) at its fixed center \(X\).
The center averages below follow the family \(t_X\) as \(X\) varies.
A common-time contour would require a different estimate.

## 2. Uniform localization, including the Poisson exterior

For \(K_X<n\le K_X^{\mathrm m}\), the inequality
\(\log n\le 3L_X/64\) gives
\(w_n(X)\le n^{-65/64+3/256}=n^{-1-1/256}\).
Thus the absolute sum of the lower population is
\(O(K_X^{-1/256})=O(X^{-1/8192})\) by the integral test.
This holds for every \(v\), so the same bound holds in the Poisson norm
using its finite mass.

For \(N_X^{\mathrm m}<n\le N_X\), use real blocks
\((D,\min(2D,e^{L_X/2})]\) with \(D=2^j e^{5L_X/16}\), \(j\ge0\),
and \(D<e^{L_X/2}\). For any real \(Y\) and integer \(n\), the conditions
\(n>\lfloor Y\rfloor\) and \(n\le\lfloor Y\rfloor\) are equivalent to
\(n>Y\) and \(n\le Y\), respectively. The open-left, closed-right blocks
cover exactly the high population once, including a final clipped block.
There are \(O(1+L_X)\) blocks.

On \(|v|\le\log X\) the actual frequency \(F=\tau_X+v/2\) lies in
\([X/3,2X/3]\) eventually. Use the classical Montgomery–Vaughan
*Multiplicative Number Theory II*, Chapter 16, Definitions 16.1–16.2,
(16.55)–(16.58), and Theorems 16.23, 16.25, as checked in
[source-use02][src02] and retained in [source-use05][src05].
For \(F\log u/(2\pi)\) on \([D,2D]\) the derivative parameter is 1,
the scale is \(F/(2\pi)\), and the relative errors in the derivatives
of the model phase vanish. The imported bound applies on arbitrary
subintervals of \([D,2D]\), with
\[
 \left|\sum_{n\in I_D}e^{iF\log n}\right|
    \ll F^k D^{l-k}+D/F
    \ll X^k D^{l-k}+D/X .
\]
Use only \((k,l)=AABABA(1/6,2/3)=(1/24,27/32)\).
With the [Note14][pairs] right-to-left convention,
\(A(k,l)=(k/(2k+2),(k+l+1)/(2k+2))\) and
\(B(k,l)=(l-1/2,k+1/2)\). The successive pairs after applying
\(A,B,A,B,A,A\) to \((1/6,2/3)=AB(0,1)\) are
\[
 (1/14,11/14),\ (2/7,4/7),\ (1/9,13/18),\
 (2/9,11/18),\ (1/11,3/4),\ (1/24,27/32).
\]

Extend \(w_n(X)\) by the same formula to a real index \(u\).
On each clipped block its logarithmic derivative in \(u\) satisfies
\[
 u\,\partial_u\log w_u(X)=-65/64+\log u/(2L_X)<0.
\]
For block right endpoint \(E\), Abel summation applies the bound on the
partial sums over \((D,u]\), \(D\le u\le E\), with cost
\(w_E(X)+\int_D^E|\partial_u w_u(X)|\,du=w_D(X)\).
Writing \(s=\log D/L_X\), the primary term is a constant multiple of
\((X/(4\pi))^{E_0(s)}\), where
\[
 E_0(s)=\frac1{24}-\frac{41}{192}s+\frac{s^2}{4},
 \qquad E_0(5/16)=-1/1536,\qquad E_0(1/2)=-1/384.
\]
By convexity, its maximum on \([5/16,1/2]\) is \(-1/1536\).
The inverse-frequency term is \(O(w_D(X)D/X)=O(X^{-1/2})\), since
\(w_D(X)\le1\) and \(D\le e^{L_X/2}\). Summing over all blocks,
the high piece has supremum \(O((1+L_X)(X^{-1/1536}+X^{-1/2}))\)
on \(|v|\le\log X\). Its Poisson norm there costs at most
\(\sqrt{2/5}\) times this supremum.

For every \(n\le N_X\), \(w_n(X)\le n^{-65/64+1/8}=n^{-57/64}\).
The full absolute sum from \(n=1\) to \(N_X\) is
\(O(N_X^{7/64})=O(X^{7/128})\), which majorizes the high population
at every real \(v\). On \(|v|>\log X\), the squared Poisson norm of
that piece costs \(O(X^{7/64-\pi/H})\), from integrating the exponential
kernel at both ends. The triangle inequality now gives
\[
 \|T_X-M_X\|_P
 \ll X^{-1/8192}+(1+L_X)(X^{-1/1536}+X^{-1/2})
        +X^{7/128-\pi/(2H)}
 \ll X^{-1/8192}.                                               \tag{1}
\]
This also bounds \(|\sqrt{Q(X)}-\sqrt{Q_M(X)}|\). The constants are
uniform in the real center, including at floor changes.

## 3. Exact center integrals and the logarithmic harmonic row

Work on an arbitrary interval \(I\subset[U,2U]\) of length \(1\le h\le U\).
Use \((\sigma,\rho)=(1/32,1/2)\) or \((3/64,5/16)\), and denote the
corresponding sum by \(S_X(v)\), so \(S_X=T_X\) or \(M_X\).
Let \(K=\lfloor e^{\sigma L_U}\rfloor\), \(N=\lfloor e^{\rho L_{2U}}\rfloor\),
and \(\alpha=65/64-\rho/4\in(1/2,1)\).
The exact membership interval for a positive integer \(n\) is
\[
 I_n=I\cap[4\pi n^{1/\rho},\,4\pi n^{1/\sigma}).
\]
Indeed \(n\le\lfloor e^{\rho L_X}\rfloor\) is equivalent to
\(X\ge4\pi n^{1/\rho}\), and
\(\lfloor e^{\sigma L_X}\rfloor<n\) is equivalent to
\(X<4\pi n^{1/\sigma}\). Each \(I_n\) is an interval and only
\(K<n\le N\) enter. On \(I_n\), \(w_n(X)\le n^{-\alpha}\).
The amplitude and phase satisfy
\[
 \frac{w_n'(X)}{w_n(X)}=-\frac{(\log n)^2}{4XL_X^2},\qquad
 \tau_X'=\frac12-\frac{\pi}{8XL_X^2}\ge\frac14,\qquad
 \tau_X''=\frac{\pi}{8X^2}(L_X^{-2}+2L_X^{-3})>0
\]
for sufficiently large \(U\). In the expansion of the weighted squared
sum with resonator frequencies \(\log r,\log s\), the \(X\)-phase is
\(\lambda \tau_X\), \(\lambda=\log(nr/(ms))\). Its remaining factor
\(e^{iv\log(n/m)/2}\) is independent of \(X\) and has modulus one.

If \(\lambda\ne0\), integrate on \(I_n\cap I_m\). With \(A=w_nw_m\),
\(g=A/\tau_X'\) is positive and nonincreasing. A nonempty intersection
of positive length has endpoints \(p,q\) where the smooth amplitudes
are taken by one-sided limits. Integration by parts bounds the modulus by
\[
 \frac{g(p)+g(q)+\int_p^q |g'(X)|\,dX}{|\lambda|}
 =\frac{2g(p)}{|\lambda|}
 \le\frac{8(nm)^{-\alpha}}{|\lambda|}.
                                                                    \tag{2}
\]
Empty or singleton intersections give zero. Formula (2) pays both
endpoints and all variation without differentiating a cutoff.
For \(\lambda=0\) use the bound \(h(nm)^{-\alpha}\).
The same argument with \(A=1\) gives \(8/|\log(r/s)|\) for the
off-diagonal resonator-square integrals.

For clarity, if \(C_{jk}\) is a symmetric nonnegative matrix and \(p_j>0\),
\[
 \sum_{j,k} C_{jk}|u_j||u_k|
 \le \sum_j |u_j|^2\sum_k C_{jk}\frac{p_k}{p_j}.
                                                                    \tag{3}
\]
This follows by summing \(2|u_j||u_k|\le |u_j|^2p_k/p_j+|u_k|^2p_j/p_k\)
and using symmetry. For indices \(1\le j\le J\), take
\(u_j=\sqrt{j}b_j\), \(C_{jk}=1/(\sqrt{jk}|\log(j/k)|)\) off the
diagonal and \(C_{jj}=0\), and \(p_j=j^{-1/2}\).
The weighted row is \(\sum_{k\ne j}1/(k|\log(j/k)|)\).
For \(k<j\), \(\log(j/k)=\int_k^j dt/t\ge (j-k)/j\), so the summand
is at most \(1/k+1/(j-k)\).
For \(k>j\), \(\log(k/j)\ge (k-j)/k\), so it is at most \(1/(k-j)\).
Each resulting harmonic sum is bounded by \(1+\log J\), including
the interpretation of an empty sum as zero. Thus for \(b_j\ge0\),
\[
 \sum_{j\ne k}\frac{b_j b_k}{|\log(j/k)|}
 \le 3(1+\log J)\sum_j j b_j^2.                                  \tag{4}
\]

## 4. Product frequencies and the two coincidence forms

Fix real \(R\ge1\), with all resonator indices positive integers
\(r\le R\), and write
\[
 B(X)=\left|\sum_{r\le R} c_r e^{i\tau_X\log r}\right|^2,\qquad
 \sum_{r\le R}|c_r|^2=1,\qquad
 D_R=\frac1U\int_U^{2U} B(X)\,dX .
\]
The vector \(c_r\) can depend arbitrarily on \(U\) and is held fixed
under integration in \(X\). The diagonal of its dyadic square mean
is exactly 1. Apply (2) with \(A=1\) and (4) with
\(b_r=|c_r|\), \(J=\lfloor R\rfloor\), so
\(\sum_{r\le R} r|c_r|^2\le R\). This gives
\[
 D_R=1+O(R\log(2R)/U).                                           \tag{5}
\]

For \(S_X\) as in §3, put \(J=N\lfloor R\rfloor\) and
\[
 b_j=\sum_{\substack{nr=j\\K<n\le N,\ r\le R}} n^{-\alpha}|c_r|.
\]
Expanding \(|\sum_{r\le R}c_r e^{i\tau_X\log r}\, S_X(v)|^2\)
and using (2) inside the finite sum shows that the terms with
\(nr=ms\) contribute at most a constant times \(\sum_j b_j^2\)
to its \(h^{-1}\)-normalized integral. Terms with \(nr\ne ms\)
contribute in absolute value at most
\((8/h)\sum_{j\ne k} b_j b_k/|\log(j/k)|\).
The \(v\)-factor in §3 is retained, and all these estimates are
uniform for real \(v\). Integration over the full \(P(v)\,dv\)
therefore costs its mass \(2/5\). In particular,
\[
 \frac1h\int_I B(X)\|S_X\|_P^2\,dX
 \ll \sum_j b_j^2+\frac{\log(2J)}{h}\sum_j j b_j^2.              \tag{6}
\]

Both forms in (6) are coincidence matrices indexed by \(r,s\).
Write \(r=dh_0\), \(s=dk_0\), where \(d=\gcd(r,s)\) and
\(\gcd(h_0,k_0)=1\). Then \(nr=ms\) is equivalent to
\(n=k_0 q, m=h_0 q\) for a positive integer \(q\), and
\(j=dh_0k_0q\). The two lower and upper cutoffs together are
\[
  K/\min(h_0,k_0)<q\le N/\max(h_0,k_0).
\]
For \(\sum_j b_j^2\), keep the lower restriction. The corresponding
matrix entry after factoring out \(|c_r||c_s|\) is at most
\[
 \begin{split}
 (h_0k_0)^{-\alpha}\sum_{q>K/\min(h_0,k_0)}q^{-2\alpha}
 &\ll_\alpha K^{1-2\alpha}(h_0k_0)^{-\alpha}
                    \min(h_0,k_0)^{2\alpha-1}\\
 &\le C_\alpha K^{1-2\alpha}(h_0k_0)^{-1/2}
  = C_\alpha K^{1-2\alpha}\frac{d}{\sqrt{rs}}.
 \end{split}                                                     \tag{7}
\]
The power tail bound \(\sum_{q>x}q^{-2\alpha}\ll_\alpha x^{1-2\alpha}\)
follows by integration for \(x\ge1\), allowing the first term, and
uses the full convergent sum for \(0<x<1\). The second inequality
uses \(\min(h_0,k_0)\le\sqrt{h_0k_0}\).

For \(\sum_j j b_j^2\), keep the upper restriction. The entry is
at most
\[
 d(h_0k_0)^{1-\alpha}\sum_{q\le N/\max(h_0,k_0)}q^{1-2\alpha}
 \ll_\alpha d N^{2-2\alpha}.                                    \tag{8}
\]
Here the sum is zero for upper bound below 1, and for \(Y\ge1\)
the integral test gives \(\sum_{q\le Y} q^{1-2\alpha}\ll_\alpha Y^{2-2\alpha}\).
The factor \((h_0k_0)^{1-\alpha}\) is at most
\(\max(h_0,k_0)^{2-2\alpha}\). The upper estimate (8) uses the
factor \(j\); the decay in (7) uses the lower cutoff and the
summable \(q^{-2\alpha}\) tail.

For \(G_{rs}=\gcd(r,s)/\sqrt{rs}\), the weight \(p_r=r^{-1/2}\)
gives the row estimate
\[
 \sum_{s\le R}G_{rs}\frac{p_s}{p_r}
 =\sum_{s\le R}\frac{\gcd(r,s)}{s}
 \le\sum_{d\mid r}\sum_{\substack{s\le R\\ d\mid s}}\frac d s
 \le d(r)(1+\log R),
\]
where \(d(r)\) is the number of divisors of \(r\).
For fixed \(\varepsilon>0\), \(d(r)\le C_\varepsilon r^\varepsilon\).
Indeed, \(e+1\le2^e\le p^{\varepsilon e}\) for primes with
\(p^\varepsilon\ge2\) and exponent \(e\ge0\). For each of the remaining
finitely many primes the maximum of \((e+1)p^{-\varepsilon e}\) on
\(e\ge0\) is finite, and multiplying those constants proves the bound.
Apply (3) with \(G\) and \(\sum|c_r|^2=1\), using
\(d\le R\,d/\sqrt{rs}\) in (8). This yields
\[
 \sum_j b_j^2\ll_\varepsilon K^{1-2\alpha}R^\varepsilon(1+\log R),
 \qquad
 \sum_j j b_j^2\ll_\varepsilon
        N^{2-2\alpha}R^{1+\varepsilon}(1+\log R).
                                                                    \tag{9}
\]
These bounds include all exact product coincidences, also when a
fixed ratio \(m/n\) occurs at indices diverging with \(U\).

## 5. Short-center and raw means

For \(R=1\), \(B=1\), and directly from the definition,
\(\sum_j b_j^2=\sum_{K<n\le N}n^{-2\alpha}\ll K^{1-2\alpha}\) and
\(\sum_j j b_j^2=\sum_{K<n\le N}n^{1-2\alpha}\ll N^{2-2\alpha}\).
For the middle sum \(\alpha=15/16\),
\(K\asymp U^{3/64}\), \(N\ll U^{5/16}\).
In (6), \(K^{1-2\alpha}\ll U^{-21/512}\) and
\(N^{2-2\alpha}\ll U^{5/128}\), hence
\[
 \frac1h\int_I Q_M(X)\,dX
 \ll U^{-21/512}+\frac{U^{5/128}\log U}{h}.                     \tag{10}
\]
Use (1) and the triangle inequality in the joint norm for
\(h^{-1}dX\,P(v)\,dv\) over \(I\times\mathbb R\). The difference
has norm \(O(U^{-1/8192})\). Squaring using \((a+b)^2\le2(a^2+b^2)\),
\[
 \frac1h\int_I Q(X)\,dX
 \ll U^{-1/4096}+U^{-21/512}+\frac{U^{5/128}\log U}{h}.          \tag{11}
\]
The mean tends to zero uniformly in the position of \(I\) when
\(h/(U^{5/128}\log U)\to\infty\), for example on
\(U^{5/128+\eta}\le h\le U\) for fixed \(0<\eta\le123/128\).
For bounded \(h\) the last allowance grows with \(U\).

The raw sum has \(\alpha=57/64\), \(K\asymp U^{1/32}\), \(N\ll U^{1/2}\).
Applying (6) and (9) with \(h=U\) and \(\log(2J)\ll\log(2UR)\) gives
\[
 \frac1U\int_U^{2U} B(X)Q(X)\,dX
 \ll_\varepsilon U^{-25/1024}R^\varepsilon(1+\log R)
 +U^{-57/64} R^{1+\varepsilon}(1+\log R)\log(2UR).               \tag{12}
\]
For \(R=1\) this retains the stronger dyadic estimate without the
localization error in (11):
\[
 \frac1U\int_U^{2U}Q(X)\,dX\ll U^{-25/1024},\qquad
 \frac{\operatorname{meas}\{X\in[U,2U]: Q(X)>s_0\}}{U}
      \ll_{s_0} U^{-25/1024}\quad(s_0>0\ \text{fixed}).         \tag{13}
\]
For the first inequality \(U^{-57/64}\log(2U)\) is absorbed by
\(U^{-25/1024}\); the second follows by integrating the inequality
\(Q(X)\ge s_0\) on the exceptional set.

## 6. Localized resonator mean and uniform support range

Apply (6) and (9) to \(M_X\) on the dyadic window. With the middle
parameters from §5 this gives
\[
 \frac1U\int_U^{2U} B(X)Q_M(X)\,dX
 \ll_\varepsilon U^{-21/512}R^\varepsilon(1+\log R)
 +U^{-123/128} R^{1+\varepsilon}(1+\log R)\log(2UR).
\]
The nonnegative joint measure is now \(U^{-1}B(X)dX\,P(v)\,dv\).
The omitted population has joint norm \(O(U^{-1/8192}D_R^{1/2})\)
by (1), with constants uniform over every coefficient vector.
Take the triangle inequality for \(T_X=M_X+(T_X-M_X)\) in this norm
and square. The resulting full-tail bound is
\[
 \begin{split}
 \frac1U\int_U^{2U} B(X)Q(X)\,dX
 &\ll U^{-1/4096}D_R\\
 &\quad+C_\varepsilon\big[
 U^{-21/512}R^\varepsilon(1+\log R)
 +U^{-123/128}R^{1+\varepsilon}(1+\log R)\log(2UR)\big].
 \end{split}                                                     \tag{14}
\]
This joint inequality pays cross terms with the discarded modes.

For a fixed \(0<\delta<123/128\) and \(1\le R\le U^\delta\),
(5) gives \(D_R=1+O(U^{\delta-1}\log(2U))\) uniformly. Put
\[
 m_\delta=\min\{21/512,\ 123/128-\delta\}>0,\qquad
 \varepsilon=\frac{m_\delta}{2\delta}.
\]
Then \(-21/512+\delta\varepsilon\le-m_\delta/2\) and
\(-123/128+\delta(1+\varepsilon)\le-m_\delta/2\).
Both logarithmic prefactors together are bounded by
\(O_\delta((1+\log U)^2)\) in each term. Absorbing them gives, after
division by \(D_R\),
\[
 \frac{\int_U^{2U} B(X)Q(X)\,dX}{\int_U^{2U}B(X)\,dX}
   \ll_\delta U^{-1/4096}+U^{-m_\delta/4}=o(1).                 \tag{15}
\]
The denominator is positive and bounded away from zero after
\(U^{-1}\) normalization for all sufficiently large \(U\) in this
range. The same exponent argument applied to (12) gives a vanishing
normalized mean for the raw estimate alone on every fixed
\(0<\delta<57/64\), by taking
\(\varepsilon=\min(25/1024,57/64-\delta)/(2\delta)\).
All limits hold uniformly in the stated coefficient class.
The support thresholds used here are sufficient open ranges.

## 7. Lower-witness scope and canonical control screen

Equation (15) excludes a fixed positive lower bound on the normalized
whole-dyadic weighted mean along any unbounded sequence of windows for
this support class. Thus that weighted-average lower-witness criterion
cannot produce a constant lower witness for \(Q\). It covers arbitrary
normalized coefficient vectors fixed within each window, even if the
choice of vector varies between windows. It leaves pointwise exceptional
centers, shorter/adaptively chosen averaging intervals, \(X\)-dependent
vectors, other weights, and larger supports open. Equation (13) bounds
an exceptional proportion for the moment only. There is no implication
for a zero count or the occurrence of zeros at the exceptional centers.

The quantitative classification is a mean estimate and a scoped
estimating-class exclusion. Note15's conditional \(9/16\) curve
consumer still needs \(Q(X)\le4/66^2\) at every sufficiently large
real \(X\), or its own separately paid substitute. In particular
(1) would allow a uniform strictly smaller cap on
\(\sqrt{Q_M(X)}\) to transfer after paying the localization error.
No such cap is obtained from (10)–(15). The symbolic onsets and
[E07's][e07] accepted \(567/1000\) curve and common-time tail
width retain their recorded domains. Interior and compact heights,
time-zero descent, a global Newman bound and iteration remain separate
obligations. [Classification01][a01], [Scope07][a07],
[Separate bounds12][a12], [Imports16][a16].

The [controls12 catalog][controls] and [premises02][a02] screen the
canonical interpretation via the full Note15 reduction. The relevant
premise failures are as follows.

| Control class | Failed canonical premise |
| --- | --- |
| Euler-factor and translated sources | Unmodified ordinary Dirichlet coefficients and the full canonical two-arm identification |
| Weighted-square and finite-tail sources | Full unit coefficient sequence jointly with full normalized reflection |
| Finite-prime orbit controls | Complete coefficient and reflection identities beyond the chosen primes and finite coefficient prefix |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | Exact normalized theta integer-square arithmetic |
| Positive heat counter-kernels and atom-based threshold models | The completed \(\xi\) source and its two canonical arithmetic arms |
| Atomic, finite-profile and compact continuous controls | Full canonical source and coefficients, and full profile beyond the matched observations |
| RH-conditional normalized endpoint perturbations | Ordinary Dirichlet-series arithmetic, even with the retained conditional normalization |
| Fixed-amplitude variable readouts | Actual cosine/Newman evolution for the readout |
| Relaxed zero measures and altered or finitely calibrated free phases | Exact integer zero divisor for the former and the exact common logarithmic phase at the actual height for the latter |

The arithmetic mean argument uses the integer frequency family, common
clock and amplitude bounds. Any sums with the same hypotheses can
satisfy its estimates, including when separately embedded in control
models. A small center mean is compatible with a localized defect.
A zero in the fixed Green target would contradict the full strict
Green margin if the domain, carrier, observation and boundary payments
held on that box. The arithmetic lemma by itself makes no prediction of
which controls collide. This proof imports the checked logarithmic-phase
bound only, with no novelty or endpoint claim.

[packet]: ../research-progress/handoffs/GNP-BB-E09-r1.md
[b05]: ../brainstorm/notes/05_GNP_BB_B05_DECISION_20261113.md
[decision]: 20_GNP_BB_B05_LOCAL_MOMENT_DECISION_20261113.md
[upper]: 21_GNP_BB_B05_LOCAL_MOMENT_UPPER_ESTIMATES_20261113.md
[resonance]: 22_GNP_BB_B05_MOVING_TAIL_RESONATOR_TEST_20261113.md
[green]: 15_GNP_BB_B04_SIGNED_GREEN_ACQUISITION_20261113.md
[pairs]: 14_GNP_BB_B04_BROADER_PAIR_COMPARISON_20261113.md
[e07]: 18_GNP_BB_E07_FIVE_PAIR_WIDTH_20261113.md
[src02]: ../references/02_GNP_BB_SIGNED_TAIL_SOURCE_USE_20261113.md
[src05]: ../references/05_GNP_BB_B05_SOURCE_USE_20261113.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
