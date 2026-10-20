# Reciprocal precision and bandlimited arithmetic costs

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded turn metadata. Separate same-model derivations and
[internal review][review]; no specialist review or priority claim.

**Outcome:** under RH, a fixed finite zeta sum gives a vanishing error
for the normalized logarithmic derivative at distance `c/log gamma` when
its cutoff is `gamma^(1+epsilon)`. A stronger use of the same primary
reciprocal bound improves the recorded energy envelope from a logarithmic
power `5+2eta` to `2+epsilon`. A separate Poisson argument extends the
leading `1/2` absolute-prime cost to nonnegative kernels with arbitrary
Fourier signs and `I Delta<=eta<2`, with complete gamma/pole budgets.
None supplies the opposing sign needed to exclude an original multiple zero.

The [program][program], [result index][results], [collision catalogue][controls]
and [avoid index][avoid] apply, especially [equivalent targets][a01],
[control premises][a02], [scoped conclusions][a07], [separate payments][a12]
and [gain before expansion][a20]. These are quantitative estimates and a
specified class comparison, not new unquantified criteria. [Note 06][n6]
defines the exact Möbius energy and its multiplicity cost; [review 07][r7]
records the preceding finite-sum conditioning assessment. The [BW09
manuscript][bw09] still requires a strict cap surplus beyond its exact
multiplicity baseline.

## 1. The exact primary bound and its uniform microscopic consequence

Use [Balazard–de Roton, arXiv:0810.3587](https://arxiv.org/pdf/0810.3587),
Propositions 1 and 18 (PDF pp. 3 and 16), under RH. These have been checked
in the primary PDF. To avoid confusing the typicality parameter with a
horizontal shift, call the former `theta`, fixed in `(0,1]`.
For sufficiently large `t`, put
\[
 L=\log t,\quad \ell=\log L,\quad \ell_2=\log\ell,\qquad
 V=L\left(\frac1{2\ell}+\frac{\ell_2}{\ell^2}\right).
 \tag{R1}
\]
This is an admissible value in Proposition 18, so `t` is `V`-typical
(take its `T=t`). It also lies in Proposition 1's admissible range.
For `0<h<=V/L`, those propositions give
\[
 \log|\zeta(1/2+h+it)|^{-1}
 \le V\left[\log\frac{V}{hL}
       +2(1+\theta)\log\log V+C_\theta\right].       \tag{R2}
\]
For `V/L<=h<=3/2`, the right bound can instead be `C_theta V`.
Constants and the sufficiently-large-height threshold may depend on the
fixed `theta`; they are independent of `h` and of the particular height
in these ranges. No simplicity assumption enters either proposition.

For `h=c/L`, where `c` lies in any fixed compact subset of `(0,infinity)`,
(R2) gives
\[
 \boxed{|\zeta(1/2+c/\log t+it)|^{-1}
                 \le t^{1/2+o(1)},}                  \tag{R3}
\]
uniformly in that set of `c`. Indeed `log(V/c)=ell-ell_2+O_c(1)` and
`log log V=ell_2+o(1)`, so the exponent is
`L/2+O_theta,c(L ell_2/ell)=L/2+o(L)`.
The source's simpler Proposition 19 would give a weaker leading power;
(R3) uses the near-half value of `V` specifically allowed by Proposition 18.

## 2. A fixed finite sum now certifies reciprocal precision

Fix `epsilon>0`, `c>0`, let `gamma` tend to infinity, and put
\[
 \delta=\frac c{\log\gamma},\quad s_0=1/2+\delta+i\gamma,
 \quad N=\lceil\gamma^{1+\epsilon}\rceil,
 \quad A_N(s)=\sum_{n\le N}n^{-s}+\frac{N^{1-s}}{s-1}.
 \tag{R4}
\]
**Hold this integer cutoff fixed when differentiating.** The finite
Euler-summation formula and uniform remainder follow, for example, from
[Simonic, arXiv:1910.08274](https://arxiv.org/pdf/1910.08274), Theorems 2
and 5. On the disc `|s-s0|<=delta/2`, write `zeta=A_N+R_N`.
Here `Re s>=1/2+delta/2`, while `|Im s|/N->0`, so that source gives
uniformly
\[
 |R_N(s)|\ll_{c,\epsilon}\gamma^{-(1+\epsilon)/2},
 \qquad
 |R_N'(s_0)|\ll_{c,\epsilon}
          (\log\gamma)\gamma^{-(1+\epsilon)/2}.       \tag{R5}
\]
The derivative estimate is Cauchy's inequality on the fixed-cutoff disc,
not a differentiation of a scalar big-O. Formula (R3) therefore gives
\[
 \frac{|R_N(s_0)|}{|\zeta(s_0)|}
                 \le\gamma^{-\epsilon/2+o(1)}.        \tag{R6}
\]
In particular `A_N(s0)!=0` for all sufficiently large `gamma`.

For completeness, the required local bound
`delta|zeta'/zeta(s0)|=O_c(log gamma)` can be proved without a derivative
moment assumption. RH gives an analytic logarithm `g=log zeta` on the
same disc. The elementary finite Euler sum at a separate cutoff
`ceil(2 gamma)` gives `Re g<= (1/2)log gamma+O_c(1)` throughout it.
Equation (R3) gives `Re g(s0)>=-(1/2)log gamma-o(log gamma)`.
The positive-real-part derivative inequality
`|g'(s0)|<=2(sup Re g-Re g(s0))/(delta/2)` then gives
`g'(s0)=O_c((log gamma)^2)`. Equivalently one may use RH's local partial
fraction formula and the unconditional `O(log gamma)` count in a unit
interval, retaining multiplicities.

For any analytic decomposition `zeta=A+R`, when
`eta=|R|/|zeta|<1`, exact division gives
\[
 \delta\left|\frac{A'}A-\frac{\zeta'}\zeta\right|
 \le\frac{\delta|R'|+
          \delta|\zeta'/\zeta|\,|R|}
              {(1-\eta)|\zeta|}.
\]
Using (R3), (R5) and (R6) proves the applicable finite-sum estimate
\[
 \boxed{\delta\frac{\zeta'}\zeta(s_0)
 =\delta\frac{A_N'}{A_N}(s_0)
               +O_{c,\epsilon}(\gamma^{-\epsilon/2+o(1)})
 =\delta\frac{A_N'}{A_N}(s_0)+o(1).}                  \tag{R7}
\]
The same conclusion is uniform for `c` in a fixed positive compact set.
The elementary pole/gamma terms completing `xi'/xi` remain exact.
This is an analytic finite approximation on the critical-strip side of
`Re s=1`; it is not a continuation of a termwise Euler series.

For comparison, at cutoff `N=ceil(gamma)`, the corresponding absolute
error and (R3) do not certify a vanishing relative error. Increasing the
cutoff to `gamma^(1+epsilon)` suffices. It does **not** bound the real part of (R7)
in the direction required by the multiplicity consumer. At a hypothetical
multiple zero the finite sum approximates the permitted pole contribution
as well. Nor does (R3), at a fixed microscopic distance, lower-bound
`zeta''(rho)/2`: taking `delta->0` at a fixed ordinate is a different limit.

## 3. The same primary estimate sharpens the energy upper envelope

Keep Note 06's exact quantity
\[
 E(\alpha)=\int_1^\infty M(x)^2x^{-2-\alpha}dx
 =\frac1{2\pi}\int_{\mathbb R}
 \left|\frac1{(1/2+\alpha/2+it)
                  \zeta(1/2+\alpha/2+it)}\right|^2dt.
 \tag{R8}
\]
For every fixed `epsilon>0`, (R2) yields the stronger consequence
\[
 \boxed{\log(2+E(\alpha))
   \ll_\epsilon\alpha^{-1}
                 (\log(1/\alpha))^{2+\epsilon}
        \qquad(\alpha\downarrow0).}                 \tag{R9}
\]
Here is the complete parameter comparison, including both regimes.
Set `h=alpha/2`, `a=log(1/h)`, and use (R1). For fixed `theta in (0,1]`,
large `ell` satisfies `log log V<=log ell=ell_2`, and
`log(V/L)=-log(2ell)+log(1+2ell_2/ell)`.
Thus in the small-shift regime (R2),
\[
 2\log|\zeta(1/2+h+it)|^{-1}
 \le\frac L\ell\left(1+\frac{2\log\ell}{\ell}\right)
              [a+(1+2\theta)\log\ell+C_\theta].      \tag{R10}
\]
For `t=e^L`, the factor `dt/|1/2+h+it|^2` is at most `e^{-L}dL`.
Consequently its integrand exponent is bounded by
\[
 F_a(L)=-L+\frac L\ell\left(1+\frac{2\log\ell}{\ell}\right)
              [a+(1+2\theta)\log\ell+C_\theta].      \tag{R11}
\]
For `ell<=a/2`, this is at most `O_theta(a e^(a/2))`.
For `a/2<=ell<=a-sqrt(a)`, it is at most `O_theta(e^(a-sqrt(a)))`.
In the central range `a-sqrt(a)<=ell<=2a`, the factor multiplying
`L/ell` in (R11) is at most
\[
 A:=a+(3+2\theta)\log a+C'_\theta.
\]
This follows by expanding the product, using
`a/ell<=1+O(a^(-1/2))` and `log ell<=log a+log 2`.
There,
\[
 F_a(L)\le e^\ell(A/\ell-1)
          \ll_\theta e^A/A
          \ll_\theta h^{-1}a^{2+2\theta}.             \tag{R12}
\]
To check the middle estimate directly, if `ell<A`, put `u=A-ell>=0`;
then `ell>=a-sqrt(a)` makes
`e^ell(A/ell-1)<=2 e^A u e^(-u)/a` for sufficiently large `a`.
If `ell>=A`, it is nonpositive.
For `ell>=2a`, (R10) is at most `3L/4` when `a` is large, so
`F_a(L)<=-L/4`. In the other source regime `h>=V/L`, use instead
`2 log|1/zeta|<=C_theta V`; this also gives `-L/4` for sufficiently
large `ell`. That other regime cannot occur with `ell<=2a` once `a`
is large, since then `V/L>=1/(4a)>>e^(-a)=h`.

The region `L<=e^(2a)` has length at most `e^(2a)`, whose logarithm is
negligible compared with the bound in (R12); beyond it the integral is
bounded by the decaying exponential. On the remaining compact height
range, `1/(s zeta(s))` is meromorphic with finitely many poles, all on
`Re s=1/2` under RH. If their largest order is `m0`, a bound
`O(h^(-2m0))` for the compact integral suffices. This allows arbitrary
finite multiplicities and is absorbed by (R12); no negative derivative
moment or simplicity input is used. Finally choose fixed
`theta=min(epsilon/2,1/2)`. This proves (R9).

Equation (R9) improves Note 06's exponent `5+2eta` obtained from the
pointwise Mertens bound. It still allows every fixed polynomial divergence.
In particular the exact double-zero implication
\[
 \liminf_{\alpha\downarrow0}\alpha^3E(\alpha)
          \ge16/|\rho\zeta''(\rho)|^2>0
\]
remains entirely compatible with (R9). No subcubic bound is obtained.

## 4. The finite Möbius and Euler-product checks retain the missing term

For a fixed integer `N>=1`, write `M_N(s)=sum_(n<=N) mu(n)n^(-s)`.
Partial summation gives, under RH and `Re s>1/2`, the exact identity
\[
 \frac1{s\zeta(s)}
 =\frac{M_N(s)-M(N)N^{-s}}s
               +\int_N^\infty M(x)x^{-s-1}dx.        \tag{R13}
\]
The first term is the Laplace transform of the truncated logarithmic
Mertens function; dropping its endpoint would be an error. Plancherel
separates the two time supports exactly. Its tail energy is
`integral_N^infinity M(x)^2 x^(-2-alpha) dx`. Using only the previously
recorded RH Mertens envelope on this tail reproduces Note 06's old
`exp(O(alpha^(-1) log^(5+2eta)(1/alpha)))` payment. The finite cutoff does
not itself improve it. The improvement (R9) instead uses the stronger
uniform reciprocal information (R2), and still falls far short of
subcubic energy.

Likewise the exact finite Euler factor
`F_P(s)=product_(p<=P)(1-p^(-s))` never vanishes at `rho=1/2+i gamma`.
The analytically continued function `zeta(s)F_P(s)` has exactly the same
zero order there, with its leading coefficient multiplied by `F_P(rho)`.
Its positive rough-integer Dirichlet expansion is valid for `Re s>1`;
using that termwise positivity at the event is not justified.
This finite-factor operation has supplied no lower bound here for the
unchanged endpoint deflated coefficient.

**Disposition:** the concrete gains are (R7) and the improved but still
superpolynomial envelope (R9). The proposed finite-mollifier arithmetic
has not supplied an opposing signed estimate, an endpoint coefficient
lower bound, or a simplicity proof. No weak-Mertens assertion or negative
derivative-moment hypothesis has been imported.

## 5. Admissibility and the exact complete envelope

Let \(h\) be entire, real and nonnegative on \(\mathbb R\), with \(h(0)=1\). Assume
\[
 |h(x+iy)|\le C_{h,Y}(1+x^2)^{-1}\quad (|y|\le Y)
\]
for each fixed \(Y\), and, in the Fourier convention
\[
 \phi(v)=\widehat h(v)=\int_{\mathbb R}h(x)e^{-2\pi ixv}\,dx,
\]
assume \(\operatorname{supp}\phi\subset[-\Delta,\Delta]\), \(\Delta>0\). The transform is continuous, so \(\phi(\pm\Delta)=0\); no nonnegative or real Fourier-transform hypothesis is imposed. Put
\[
 I=\int_{\mathbb R}h(x)\,dx=\phi(0)>0,
 \qquad C(h)=\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
            |\phi(\log n/(2\pi))|.                         \tag{K1}
\]
The sum is finite. The kernel may depend on the target height or on event data, provided all the displayed hypotheses and budgets hold.

Under RH, the Guinand–Weil formula, in [Goldston–Gonek, Lemma 1](https://arxiv.org/pdf/math/0511092), gives
\[
 S_h(\gamma):=\sum_\lambda m_\lambda h(\lambda-\gamma)
 =G_\gamma(h)+P_\gamma(h)-Q_\gamma(h),                       \tag{K2}
\]
\[
 G_\gamma(h)=\frac1{2\pi}\int_{\mathbb R}h(v)g_\gamma(v)\,dv,
 \quad g_\gamma(v)=\Re\psi\!\left(\frac14+\frac{i(\gamma+v)}2\right)-\log\pi,
\]
\[
 P_\gamma(h)=h(-\gamma+i/2)+h(-\gamma-i/2),
\quad
 Q_\gamma(h)=\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \Re\!\left[e^{-i\gamma\log n}\phi(\log n/(2\pi))\right].
\]
All multiplicities and all exterior zeros remain in (K2). Its sums converge by quadratic decay and the usual zero count. At an actual zero, \(m(\gamma)\le S_h(\gamma)\).

Two valid upper envelopes are
\[
 U_{\rm mod}=G_\gamma+E_\gamma+C(h),\qquad
 E_\gamma=|h(-\gamma+i/2)|+|h(-\gamma-i/2)|,
\]
\[
 U_{\rm exact}=G_\gamma+P_\gamma+C(h).                       \tag{K3}
\]
Here \(P_\gamma\) is real but need not be positive. Exact pole retention and modulus pole payment are distinguished throughout.

For the height-dependent optimization theorem below, put \(L=\log(\gamma/(2\pi))\). Require the explicit gamma budget
\[
 \int_{\mathbb R}h(v)|g_\gamma(v)-L|\,dv
 \le\epsilon_\gamma L I,\qquad\epsilon_\gamma\longrightarrow0.    \tag{K4}
\]
For \(U_{\rm exact}\), additionally require
\[
 2\pi(P_\gamma)_-\le\epsilon'_\gamma L I,
 \qquad\epsilon'_\gamma\longrightarrow0.                    \tag{K5}
\]
Thus the non-prime part of the chosen envelope is at least
\((1-o(1))LI/(2\pi)\). For \(U_{\rm mod}\), (K5) is unnecessary because \(E_\gamma\ge0\). These are explicit paid hypotheses; gamma localization is not silently inferred from bandlimitation, nonnegativity, or \(h(0)=1\).

## 6. A discrete Poisson inequality valid for signed Fourier coefficients

For every \(a>0\),
\[
 \sum_{j\in\mathbb Z}h(j/a)=a\sum_{k\in\mathbb Z}\phi(ka).  \tag{K6}
\]
The stated quadratic decay suffices: the periodization \(\sum_jh(t+j/a)\) converges uniformly on a period and is continuous; its Fourier coefficients are \(a\phi(ka)\). Only finitely many are nonzero, so uniqueness of Fourier coefficients gives a finite trigonometric polynomial and (K6) pointwise. There is no appeal to a Poisson formula requiring unproved Schwartz regularity.

Nonnegativity and \(h(0)=1\) now imply
\[
 I+2\sum_{k\ge1}\Re\phi(ka)\ge\frac1a,
 \qquad
 I+2\sum_{k\ge1}|\phi(ka)|\ge\frac1a.                      \tag{K7}
\]
Taking \(a=\Delta\), with endpoint samples zero, proves
\[
                         I\Delta\ge1.                     \tag{K8}
\]

For a prime \(p\), set \(a_p=\log p/(2\pi)\) and \(K_p=\lfloor\Delta/a_p\rfloor\). If \(1-a_pI>0\), then (K8) gives \(K_p\ge1\). The contribution of its powers to (K1) satisfies
\[
 \begin{aligned}
 C_p(h)
 &=\frac{\log p}{\pi}\sum_{k=1}^{K_p}p^{-k/2}|\phi(ka_p)|\\
 &\ge p^{-K_p/2}(1-a_pI)_+
 \ge e^{-\pi\Delta}(1-a_pI)_+.
 \end{aligned}                                             \tag{K9}
\]
Consequently
\[
 C(h)\ge e^{-\pi\Delta}\sum_p
       \left(1-\frac{I\log p}{2\pi}\right)_+.              \tag{K10}
\]
The powers of distinct primes are disjoint indices of the prime payment. In particular this argument has not summed the same prime-power payment more than once.

For completeness, if \(B=2\pi/I\to\infty\), partial summation gives the exact expression
\[
 \sum_{p\le e^B}\left(1-\frac{\log p}{B}\right)
 =\frac1B\int_2^{e^B}\frac{\pi(x)}x\,dx
 \sim\frac{e^B}{B^2}.                                     \tag{K11}
\]
The last step uses the ordinary [prime number theorem](https://dlmf.nist.gov/25.16.i). The integral proof avoids subtracting two main terms with an uncontrolled cancellation.

## 7. First-harmonic primes give the sharper uniform cost

Fix \(1\le\eta<2\), and suppose
\[
                         1\le I\Delta\le\eta.             \tag{K12}
\]
Write \(X=e^{2\pi\Delta}\) and \(B=2\pi/I\). For primes in
\[
                  \sqrt X<p<e^B,
\]
one has \(a_p>\Delta/2\), so every harmonic \(ka_p\), \(k\ge2\), lies outside the support. Also \(a_p<1/I\le\Delta\). Therefore (K7) directly forces a positive first Fourier sample:
\[
 \Re\phi(a_p)\ge\frac{\pi}{\log p}-\frac I2>0.
\]
Its absolute payment is at least \(p^{-1/2}(1-\log p/B)\). Hence
\[
 C(h)\ge
 \sum_{e^{\pi\Delta}<p\le e^B}
 p^{-1/2}\left(1-\frac{\log p}{B}\right).                 \tag{K13}
\]
The zero weight at the upper endpoint and the omitted lower endpoint cause no issue.

As \(I\to0\), the right side of (K13) is
\[
 \left(4+o_\eta(1)\right)\frac{e^{B/2}}{B^2},
\]
uniformly over (K12). Here is a positive-weight derivation. Set
\(f_B(x)=x^{-1/2}(1-\log x/B)\) on \([2,e^B]\). It is nonnegative and decreasing, and \(f_B(e^B)=0\). Partial summation against the PNT shows
\[
 \sum_{p\le e^B}f_B(p)
 \sim\int_2^{e^B}\frac{f_B(x)}{\log x}\,dx.
\]
For example, use \(\pi(x)\sim\operatorname{Li}(x)\) in
\(-\int_2^{e^B}\pi(x)f'_B(x)\,dx\), first separating a fixed lower cutoff. Both measures give a bounded lower-cutoff contribution, while the positive main integral diverges; this makes the relative error arbitrarily small without subtracting uncontrolled leading terms. The main integral is
\[
 e^{B/2}\int_0^{B-\log2}\frac{u e^{-u/2}}{B(B-u)}\,du
 \sim\frac{4e^{B/2}}{B^2}.                                \tag{K14}
\]
On \(u\le B/2\), dominated convergence gives the constant
\(\int_0^\infty ue^{-u/2}du=4\); the remaining part is exponentially smaller. Removing primes up to \(e^{\pi\Delta}\) costs at most
\[
 \sum_{n\le e^{\pi\Delta}}n^{-1/2}
 \le 2e^{\pi\Delta/2}
 \le 2e^{\eta B/4}
 =o_\eta(e^{B/2}/B^2).
\]
This proves the uniform lower bound
\[
 \boxed{\displaystyle
 C(h)\ge\left(\frac{I^2}{\pi^2}+o_\eta(I^2)\right)e^{\pi/I},
 \qquad I\to0,\quad 1\le I\Delta\le\eta<2.}               \tag{K15}
\]
The stronger exponent in (K15), rather than the weaker exponent obtainable from (K10), is essential for the leading constant below. No regularity of \(\phi\) beyond the declared assumptions is needed, and arbitrary Fourier signs are allowed.

## 8. Sharp leading absolute-envelope cost in the declared class

Let \(\gamma\to\infty\), and let \(h=h_\gamma\) satisfy (K12), the admissibility assumptions, and (K4). If using exact pole retention, assume (K5) too. Then for either corresponding envelope in (K3),
\[
 \boxed{\displaystyle
 \liminf_{\gamma\to\infty}
 \frac{U(\gamma)}{L/\log L}\ge\frac12.}                   \tag{K16}
\]
To prove this, it suffices to examine a subsequence on which
\(U=O(L/\log L)\). The complete non-prime lower bound and \(C\ge0\) force \(I=O(1/\log L)\), so (K15) applies. If, for some fixed \(\delta>0\),
\[
 U\le\left(\frac12-\delta\right)\frac{L}{\log L},
\]
then the same non-prime lower bound forces
\[
 I\le\frac{\pi(1-2\delta+o(1))}{\log L}.
\]
For small \(I\), the function \(I^2e^{\pi/I}\) decreases as \(I\) increases. Thus (K15) makes \(C\) at least a fixed positive constant times
\(L^{1+c_\delta}/(\log L)^2\), contradicting the displayed competitive upper bound. This proves (K16).

The coefficient is sharp whenever the declared class includes the Fejér kernels and their already established complete budgets. Indeed
\[
 h(v)=K_\Delta(v),\qquad I=1/\Delta,\qquad
 \Delta=\frac{\log L}{\pi}
\]
has \(I\Delta=1\), satisfies (K4), and has negligible modulus pole payment. Note 02 proves
\(U_{\rm mod}=(1/2+o(1))L/\log L\); the exact-pole version has the same leading asymptotic. Thus any uniformly budgeted class satisfying (K12) and containing these Fejér choices has optimized envelope
\[
             \inf_h U(\gamma)=\left(\frac12+o(1)\right)
                                \frac{L}{\log L}.         \tag{K17}
\]
Uniformity of the budgets over a class is required for this infimum formulation; the sequence formulation (K16) needs them only along the chosen sequence.

Here the absolute gamma budget for the Fejér choice is verified directly, rather than inferred from an asymptotic for the signed integral \(G\). Uniformly for \(\Delta\ge1\), split at \(|v|=\sqrt\gamma\). On the inner interval the digamma expansion gives \(|g_\gamma(v)-L|\ll\gamma^{-1/2}\), while \(\int K_\Delta=1/\Delta\). On the complement use
\[
 K_\Delta(v)\le\frac1{\pi^2\Delta^2v^2},\qquad
 |g_\gamma(v)-L|\ll\log\gamma+\log(2+|v|).
\]
Consequently
\[
 \int_{\mathbb R}K_\Delta(v)|g_\gamma(v)-L|\,dv
 \ll\frac1{\Delta\sqrt\gamma}
       +\frac{\log\gamma}{\Delta^2\sqrt\gamma}
 =o\!\left(\frac L\Delta\right),                          \tag{K17a}
\]
uniformly for \(\Delta\ge1\). The sine formula also gives
\[
 E_\gamma(K_\Delta)
 \le\frac{2\cosh^2(\pi\Delta/2)}
          {\pi^2\Delta^2(\gamma^2+1/4)}
 \ll\frac{e^{\pi\Delta}}{\Delta^2\gamma^2}.               \tag{K17b}
\]
At \(\Delta=\log L/\pi\), this is \(O(L/(\Delta^2\gamma^2))=o(L/\Delta)\). Thus both (K4) and, because \((P_\gamma)_-\le E_\gamma\), (K5) hold for the sharpness sequence with their required absolute budgets.

## 9. Exact removal of every prime sample and the remaining scope

One narrow conclusion holds without (K12). If \(C(h)=0\), all samples
\(\phi(k\log2/(2\pi))\), \(k\ge1\), vanish: samples within the support have positive weights in (K1), and the others vanish by support. Equation (K6) with \(a=\log2/(2\pi)\) then gives
\[
                         I\ge\frac{2\pi}{\log2}.          \tag{K18}
\]
This is sharp: the Fejér kernel of bandwidth \(\log2/(2\pi)\) has precisely this mass, while every prime-power Fourier sample lies at or beyond its zero endpoint. Under the gamma budget, its non-prime cost is of order \(L\). An exact zero-prime-payment notch cannot be both nonnegative and of small mass. This does **not** prove a useful uniform near-zero-payment bound when the bandwidth is unrestricted; the factors \(p^{-K_p/2}\) in (K9) may become very small.

**Continuation:** [Note 09](09_ARITHMETIC_CONTROLS_TRANSLATED_KERNELS_AND_STABLE_EXTRACTION_20261020.md)
constructs translated nonnegative kernels with I Delta tending to two
from below and C(h) tending to one, and with I Delta tending to three,
I tending to zero and C(h) tending to zero. Their complete gamma/pole
budgets can be paid at sufficiently large selected heights. Thus the
fixed margin below two in (K15) is essential, and exact zero payment does
not imply a useful unrestricted near-zero payment bound. No improved
complete height envelope follows without paying the quantitative
simultaneous phase-return height.

The full unrestricted kernel problem remains open in this calculation. In particular, (K16) does not cover sequences with \(I\Delta\ge2\), or \(I\Delta\uparrow2\) without a sufficient quantitative margin, or kernels failing the complete archimedean budgets. The bandwidth is the actual declared support bound; artificially inflating it does not strengthen the theorem. Prime-sample notches cannot be handled by replacing the discrete sum with an unproved continuous weighted norm of \(|\widehat h|\). A signed estimate for the actual \(Q_\gamma\), rather than payment by (K1), is also outside this result.

The event condition itself grants neither (K12) nor the missing signed prime cancellation. No simplicity assumption enters (K6)–(K18). For the required control screen, the endpoint Euler controls change the logarithmic prime coefficients and completion data, while Note 05's normalized positive-source controls fail the ordinary Dirichlet-series arithmetic. They therefore do not satisfy the unchanged-zeta explicit formula (K2) with its exact positive von Mangoldt weights; shape, all-real endpoint zeros, and source positivity alone are not being used to exclude them. No original theta zero is excluded by this note.


[review]: ../reviews/08_RECIPROCAL_PRECISION_AND_KERNEL_REVIEW_20261020.md
[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[n6]: 06_SIGNED_CORRELATION_RESOLUTION_AND_MOBIUS_ENERGY_20261020.md
[r7]: ../reviews/07_LOCAL_CORRELATION_AND_JENSEN_MARGIN_REVIEW_20261020.md
[bw09]: ../../09_expanding_contour_later_collision/manuscript/main.tex
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
