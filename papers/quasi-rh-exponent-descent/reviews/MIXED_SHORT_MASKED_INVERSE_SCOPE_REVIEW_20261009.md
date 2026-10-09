# Source scope review of the shortened masked inverse bound

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: inherited configuration, not exposed;
the exact serving variant is not inferred. This same-model source-scope
audit and derivation are not independent specialist review or formal proof
verification.

The source's actual all-length pointwise inverse lemma, rather than a new
moment theorem at a smaller row scale, controls the shorter inverse sums
created by gcd coprimality inversion. A convolution with ideals supported
on the deletion primes proves the required added-mask bound without
changing a character, adding a growing twist, or modifying a profile.
This permits a much smaller gcd cutoff than the global seven-eighths
reciprocal-growth bound alone.

## 1. Source scope used here

Primary source: the [30 September companion paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
Lemma 8.2, pages 57–58, with the source bin and buffered parameters of
Lemma 8.1. The primary PDF was retrieved and extracted in memory by the
parallel source auditor; its SHA-256 matches the previously recorded
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
I audited its reported statement and proof structure against the local
manuscript's notation. The source's deep analytic proof remains imported.

The important scope is a fixed bounded **nonnegative** range of inverse
length exponents, not just the one detector length `r`. The source
explicitly permits a range enclosing `0 <= r,m <= 22`. Profiles are
uniformly smooth on a fixed positive annulus. Its common pure norm twist
and additional Mellin frequencies retain the specified finite-height
allocation. The bound is

\[
 |M_\psi(t;A_0)|^2
 \ll_\varepsilon U^{d t+\varepsilon}H^b,
 \qquad d=2a-1,
 \tag{1}
\]

for a row of the original buffered bin, at inverse length `U^t`. The
source chooses its small buffer after the bounded length ranges and
before the finite height and tail orders. In its proof the central
Mellin frequency is moved to the right-hand buffered line with real part
`a+6e`; the tails stay on an absolute-convergence line, and the joins
stay in the common zero-free rectangle. The whole range is uniform in
the same original row and height parameters.

Here `a=(1+d)/2` lies in `[17/25,71/100]`. The numerical symbol `d`
is the manuscript's local zero-bin parameter. It is not the global
reciprocal-growth exponent `3/4`. Equation (1) is **pointwise**; it
does not assert a marked inverse moment for rescaled physical rows.

## 2. A direct deletion-convolution lemma

Let `q` be a good ideal of norm at most a fixed power of `U`, and retain
the physical, completely multiplicative, zero-extended character
`psi_u`. The permitted norm phase has modulus one on its nonzero
values, so `|psi_u(n)| <= 1`. Define

\[
 T_{u,q}(L)=\sum_{(n,q)=1}\mu_F(n)\psi_u(n)A_0(Nn/L).
 \tag{2}
\]

For `L` between a fixed positive constant and `C U^r`, the source
all-length bound implies

\[
 \boxed{|T_{u,q}(L)|^2
   \ll_\varepsilon U^\varepsilon H^b L^{1+d}.}
 \tag{3}
\]

To prove this, let `b_q(k)=psi_u(k)` when every prime divisor of `k`
divides `q`, and zero otherwise. As ideal coefficient sequences,

\[
 \mu_F\psi_u\,\mathbf1_{(\,\cdot\,,q)=1}
       =(\mu_F\psi_u)*b_q.
 \tag{4}
\]

At a prime in `q`, multiplying the two local series gives
`(1-psi_u(p)x)/(1-psi_u(p)x)=1`; at every other prime the first series
remains unchanged. This argument also works when the physical phase is
zero. Thus no canceled zero is being replaced by one.

The smoothed form of (4) is the finite identity

\[
 T_{u,q}(L)=\sum_{k:\operatorname{supp}(k)\subseteq\operatorname{supp}(q)}
       \psi_u(k)\sum_n\mu_F(n)\psi_u(n)
                             A_0(Nn/(L/Nk)).
 \tag{5}
\]

The inner profile is still `A_0`; only its length changes. Its common
norm twist and Mellin-frequency allocation are unchanged. Terms can
occur only when `Nk <= C L`. For `L/Nk >= 1`, applying (1) in its fixed
nonnegative enclosing length range gives an unnormalized bound
`(L/Nk)^a U^epsilon H^b`, uniformly in `k`. A fixed bounded subunit
range `1/C <= L/Nk < 1` has only boundedly many ideals on the profile
support and satisfies the same inequality after changing the constant.
Smaller lengths give zero. Consequently

\[
 |T_{u,q}(L)|
 \ll U^\varepsilon H^b L^a
       \sum_{k:\operatorname{supp}(k)\subseteq\operatorname{supp}(q)}(Nk)^{-a}
 = U^\varepsilon H^b L^a
       \prod_{p\mid q}(1-(Np)^{-a})^{-1}.
 \tag{6}
\]

For every fixed `sigma>0` and every `epsilon>0`, the last product with
`a>=sigma` is `O_{sigma,epsilon}((Nq)^epsilon)`. Separate finitely many
small primes; for the rest each local factor is at most `(Np)^epsilon`.
The polynomial norm bound for `q` therefore absorbs this cost into the
requested arbitrary small power of `U`. Squaring and reallocating that
power proves (3).

This route uses no contour theorem for an arbitrary new coefficient
sequence: it uses the **actual original** inverse bound once for each
shorter length in an exact convolution. It creates no extra norm
frequency. Every original physical zero survives (4) and (5). The
original permitted derivative-profile families obey the same argument;
fixed powers of logarithms are absorbed in the existing arbitrarily
small losses. The source's common finite-height ordering must still be
retained, and the original `H^b` factor is not removed.

For an already fixed preliminary source buffer, retain its literal exponent
as `d+rho`; the all-loss display above presupposes the permitted choice of
buffer for the requested loss before the final height allocation. The
[main note](../mixed_character_families/notes/14_SIGNED_HIGH_GCD_REDUCTION_20261009.md)
quantifies `rho<=1/100000` as a sufficient allocation: both the high-gcd
removal and the compatible finite-prime completion still retain reserve
greater than `1/1000`. An unknown fixed buffer is not absorbed into every
arbitrarily small loss. All exact cutoff and shell deductions remain
conditional on that actual source scope.

## 3. Consequence for the high-gcd signed fourth sector

Write `G=Ng`, `D=U^r`, and fix a squarefree original gcd `g`. After
retaining `(a,g)=(b,g)=1`, coprimality inversion in the ratio factors
gives the exact full fixed-gcd expression

\[
 B_g(u)=\sum_{\substack{h\ \mathrm{squarefree}\\(h,g)=1}}
       \mu_F(h)|\psi_u(h)|^2
       |T_{u,gh}(D/(GNh))|^2.
 \tag{7}
\]

The exterior factor `|psi_u(g)|^2` is retained in the original pair
expansion. Since `gh` divides each relevant original squarefree
inverse column, `N(gh) <= C D`. Applying (3), then the convergent
ideal sum `sum_h (Nh)^(-1-d)`, gives

\[
 |B_g(u)|\ll U^\varepsilon H^b (D/G)^{1+d}.
 \tag{8}
\]

Use the **original** selected fourth weight
`V_u=1_(C+)|S_u|^4|Q_J(u)|^2`, whose legal source mass is at most
`U^(1+epsilon) H^b`. Sum (8) over the original squarefree gcds
`G >= G_0 >= 1`, and retain `D^-1` from the inverse square:

\[
 \boxed{|F_{J,\mathrm{gcd}\ge G_0}^{\mathrm{full\ ratio}}|
       \ll U^{1+\varepsilon}H^b D^d G_0^{-d}.}
 \tag{9}
\]

The ideal-counting tail `sum_(Ng>=G0) (Ng)^(-1-d)` is
`O(G0^(-d))`, uniformly on `d>=9/25`. Equation (9) preserves the
cross terms within each original fixed-gcd sector through (7); replacing
them by separate ratio packets would not give the same saving.

At the fixed choice `G_0=U^(1/125)`, its saving relative
to the uniform target `U^(1+dr-1/540)` is at least

\[
 \frac{9}{3125}-\frac1{540}
       =\frac{347}{337500}>\frac1{1000}.
 \tag{10}
\]

Restoring the existing condition `Nf>U^(1/2)` subtracts a subset of
the old small-ratio error, whose absolute bound is `O(U^(5/4+epsilon)
H^b)`. Note 9 gives that error reserve greater than `1/500` against
the uniform target. Thus the high-gcd part of the **actual signed
large-ratio moment** is affordable with a combined reserve greater
than `1/1000`.

Its retained complement has `Ng<U^(1/125)`. Original annular balance
`cD <= G Na,G Nb` forces

\[
 Nf=Na\,Nb>c^2D^2U^{-2/125}.
 \tag{11}
\]

The unresolved correlation is therefore a joint near-coprime, near-
maximal-ratio remainder. Equation (11) does not justify an isolated
bound for every core range without its gcd restriction. No actual
slot/witness vector, new fourth theorem, or new zero-free boundary is
certified by this reduction.

## 4. Other input routes checked

Threshold localization in the inverse response follows from the original
fourth mass: rows with `|M_u|^2 <= U^(dr-kappa-delta)` contribute at most
`U^(1+dr-kappa-delta)H^b`. It leaves a new correlation between the
remaining inverse response and `V_u`; the marked inverse mass and
ordinary fourth mass alone do not prove that correlation. The scalar
sharpness construction in mixed Note 6 already rules out a gain from
those marginals alone. Changing a threshold or using the original
high-response set simply reproduces the existing Holder envelope.

The full polynomial `M S^2 Q_J` has physical column radius of order
`U^(r+2m+z_J)`, before taking sixth-power-free kernels. A canonical
sieve cannot be applied at the much smaller ratio radical merely by
relabeling these columns. Its complete positive enlargement is weaker
than the inherited pointwise-inverse/fourth-mass bound on the working
range. A generic bilinear or entrywise residue estimate likewise needs
an additional selected-weight correlation; the original sharp selector
does not become a complete smooth row sum after expansion.

The significant legal deduction is consequently (9), obtained by signed
coprimality inversion and the actual all-length local inverse input.
