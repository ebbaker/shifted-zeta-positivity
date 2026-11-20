# What the high-height approximation actually says

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex LLM assistance. The captured source supplies no per-turn model or
reasoning-effort configuration. [Public discussion](../../chat-histories/0004_2026-11-20T18-21-26Z_explain-zero-approximation-cutoff.json).

Status: explanatory derivation from the published fixed-positive-time
approximation and elementary Gaussian/Stirling algebra. No new coverage,
effective onset, numerical experiment, or research milestone. This expands
the short high-height discussion in [Note 09](09_EZ_TWO_LIMITS_AND_THE_ROLE_OF_K_20261120.md).
Read with the [result index](../../../../../../result-summaries/README.md),
the [explicit-position entries in cluster 18](../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
the [patterns index](../../../../../../avoid/README.md), and the rules on
[classification](../../../../../../avoid/01_restating_the_target.md),
[normalization](../../../../../../avoid/08_normalization_and_constant_slips.md),
and [scope](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 1. An explicit envelope and phase

Keep physical heat time fixed with 0<t<=1/2, and let x tend to positive
infinity. Put ell_x=log(x/(4pi)), which is distinct from the large-time
real saddle L(T). Define
\[
 \mathcal A_t(x)=\frac{\pi^{1/4}}{16}x^{7/4}
   \exp\left(-\frac{\pi x}{8}+\frac{t\ell_x^2}{16}
                                -\frac{t\pi^2}{64}\right),
 \qquad
 \varphi_t(x)=\frac{x}{4}(\ell_x-1)+\frac{7\pi}{8}
                                      +\frac{t\pi\ell_x}{16}.
 \tag{1}
\]
Polymath's Proposition 9.1 and Lemma 9.2, with the elementary expansion in
§2 below, give for some absolute c>0, made smaller if needed,
\[
 H_t(x)=\mathcal A_t(x)\{\cos\varphi_t(x)+O(x^{-ct})\}
 \quad\text{for }x\ge \exp(C/t),
 \tag{2}
\]
where C is sufficiently large. This is additive error relative to the
positive envelope, not relative to H_t or to cos(varphi_t). In particular,
(2) does not divide by a quantity that vanishes at a zero. No numerical
value of the onset constant is extracted here.
[Polymath v2, Proposition 9.1 and Lemma 9.2](https://arxiv.org/html/1904.12438v2#S9).

## 2. Where the envelope and phase come from

With s=(1+ix)/2, the exact time-zero identity is H_0(x)=G(s) zeta(s), where
\[
 G(s)=\frac{s(s-1)}{16}\pi^{-s/2}\Gamma(s/2).
\]
Let M_0 be its Stirling model,
\[
 M_0(s)=\frac{\sqrt{2\pi}}{16}s(s-1)\pi^{-s/2}
     \exp\left((s/2-1/2)\operatorname{Log}(s/2)-s/2\right),
\]
and define
\[
 \alpha(s)=\frac{M_0'(s)}{M_0(s)}
       =\frac1{2s}+\frac1{s-1}+\frac12\operatorname{Log}\frac{s}{2\pi},
 \qquad M_t(s)=M_0(s)e^{t\alpha(s)^2/4}.
 \tag{3}
\]
These are the explicit functions in Polymath (6)–(10). The prior notation
A_t(x) meant |M_t((1+ix)/2)|; its twice-amplitude is asymptotic to the
elementary envelope mathcal A_t in (1). Neither M_t nor this amplitude
is the half-line transform B_T used for the origin inverse.

Here is the prefactor calculation. Since s(s-1)=-(1+x^2)/4,
\[
 |G(s)|=\frac{1+x^2}{64}\pi^{-1/4}
             |\Gamma(1/4+ix/4)|
       \sim\frac{\pi^{1/4}}{32}x^{7/4}e^{-\pi x/8}.
\]
On the continuous phase branch at large x, complex Stirling gives
\[
 \arg M_0(s)=\frac{x}{4}(\ell_x-1)+\frac{7\pi}{8}+O(1/x),
 \qquad \alpha(s)=\frac{\ell_x}{2}+\frac{\pi i}{4}+O(1/x).
\]
Squaring the last expression yields
\[
 \frac t4\alpha(s)^2
 =\frac{t\ell_x^2}{16}-\frac{t\pi^2}{64}
                  +i\frac{t\pi\ell_x}{16}+O(t\log x/x).
 \tag{4}
\]
The real part changes the amplitude and the imaginary part changes the
phase. Adding M_t(s) and its conjugate supplies the factor two and the
cosine in (1)–(2). The errors of replacing M_t by its elementary leading
expression are O(log x/x) relative to its amplitude; these fit inside
O(x^{-ct}) after reducing c in the stated bounded-time range.
[Complex Stirling](https://dlmf.nist.gov/5.11.E1) ·
[Gamma modulus asymptotic](https://dlmf.nist.gov/5.11.E9).

The heat multiplier in (3) also has a direct interpretation. In the
completed-zeta variable, heating averages a function at s+sqrt(t)v with
weight exp(-v^2)/sqrt(pi). Replacing its logarithm locally by a linear
function of slope alpha gives the Gaussian integral exp(t alpha^2/4).
For an arithmetic term M_0(s)n^{-s}, the logarithmic slope is
alpha-log n. This gives the next section's formula. The published
estimates justify the approximation and bound its summed errors; a local
linearization alone would not supply those bounds.
[Polymath, (35), (39) and Proposition 6.1](https://arxiv.org/html/1904.12438v2#S4).

## 3. Why the arithmetic correction decreases with height

The Riemann–Siegel decomposition gives two conjugate sums on the real
x-axis, plus a remainder. A term of the first sum has the approximation
\[
 M_0(s)n^{-s}e^{t(\alpha(s)-\log n)^2/4}
   =M_t(s)\frac{e^{t\log^2n/4}}{n^{s+(t/2)\alpha(s)}}.
 \tag{5}
\]
Its conjugate is in the second sum. The n=1 terms are M_t(s) and its
conjugate. After factoring out M_t, the magnitude of term n is
\[
 w_n(t,x)=\exp(t\log^2n/4)\,
                   n^{-\Re(s+(t/2)\alpha(s))}.
\]
The exact definition (3) gives Re(alpha)=ell_x/2+O(x^{-2}). Consequently
\[
 w_n(t,x)=n^{-1/2}
  \exp\left[-\frac t4\log n(\ell_x-\log n)
                                  +O(t\log n/x^2)\right].
 \tag{6}
\]
For each fixed n>=2, this decreases as a constant times x^{-t log n/4}.
The n=1 weight stays one. Importantly, the whole sum also shrinks: the
actual truncation N=floor(sqrt(x/(4pi)+t/16)) has
log N<=ell_x/2+O(t/x), so uniformly for 2<=n<=N,
\[
 w_n(t,x)\le n^{-\sigma_x},\qquad
 \sigma_x=\tfrac12+\tfrac{t\ell_x}{8}
                                      -O(t^2/x+t/x^2).
\]
Once sigma_x>1,
\[
 \sum_{n=2}^N w_n(t,x)
 \le 2^{-\sigma_x}\left(1+\frac{2}{\sigma_x-1}\right).
 \tag{7}
\]
The right side tends to zero because t>0 is fixed. This is the mechanism
that allows two conjugate arithmetic sums to reduce to one cosine.
The other Riemann–Siegel error terms also tend to zero in amplitude units,
as controlled by the cited theorem.

Normalization check: (6) uses Polymath's defining (9), (17) and bound
(21), giving Re(s+(t/2)alpha)=1/2+t ell_x/4+O(t/x^2).
The uniform post-weight exponent is therefore 1/2+t ell_x/8 up to the
displayed losses. The same factors occur in the branch's
[strip-tail derivation](../../notes/05_EZ_EXPLICIT_POSITIVE_TIME_STRIP_TAIL_20261120.md).

## 4. How this predicts positions and gaps

Let u_j be the sufficiently high solution of
\[
 \varphi_t(u_j)=(j-\tfrac12)\pi.
\]
Equivalently,
\[
 \frac{u_j}{4\pi}\left(\log\frac{u_j}{4\pi}-1\right)
      +\frac{11}{8}+\frac{t}{16}\log\frac{u_j}{4\pi}=j.
 \tag{8}
\]
This is the published elementary clock. Its local frequency is
\[
 \varphi_t'(x)=\frac14\log\frac{x}{4\pi}+\frac{t\pi}{16x}.
\]
A field error epsilon in cosine units displaces a crossing by order
epsilon/varphi_t'(u_j). The published local complex estimate and count
establish exactly one simple real zero near each sufficiently high clock;
the bound after (104) gives
\[
 |x_j^{\mathrm{near}}-u_j|
    =O\left(\frac{u_j^{-ct}}{\log u_j}\right),\qquad
 u_{j+1}-u_j\sim\frac{4\pi}{\log u_j}.
 \tag{9}
\]
Thus the error as a fraction of a spacing is O(u_j^{-ct}). The small
real-axis error alone is not being used to prove uniqueness. The label j
in (8) is initially a clock label, not automatically absolute rank.
[Note 13](../../notes/13_EZ_CLOCK_RANK_20261120.md) identifies it with
absolute positive rank at t=1/2, using its separate count argument.

## 5. The role of positive time and the comparison with the inverse

At t=0 the suppression factor in (6) disappears. The arithmetic weights
return to n^{-1/2}, so this argument no longer permits retaining just
n=1. The sufficient high-tail onset grows like exp(C/t) as t tends to
zero. No uniform t=0 result follows.

For the origin inverse at large T, the leading phase is a(T)x and the
source cumulants describe its corrections. For the far tail at fixed
positive t, the phase in (1) has slope growing like (log x)/4. This is
another asymptotic description of the same field. The origin result's
upper rank bound and the far-tail result's lower height threshold do not
by themselves supply a common-time overlap.

The calculation uses the canonical arithmetic expansion, its exact unit
coefficients, the gamma completion and the complete remainder estimates.
It is not a shape-only collision exclusion. The
[inherited control screen](../../notes/05_EZ_EXPLICIT_POSITIVE_TIME_STRIP_TAIL_20261120.md)
names the failed premises: Euler-factor, weighted-square and finite-prime
controls change the arithmetic terms; reflected and positive-primitive
controls lack the canonical expansion; fixed-event and finite-profile
controls lack its complete error budget; conditional normalized controls
lack ordinary Dirichlet arithmetic; altered observations change the
literal cosine field. These failures do not assert that a control cannot
obey its own high-height asymptotic. See the
[control catalogue](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [premise rule](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md).
