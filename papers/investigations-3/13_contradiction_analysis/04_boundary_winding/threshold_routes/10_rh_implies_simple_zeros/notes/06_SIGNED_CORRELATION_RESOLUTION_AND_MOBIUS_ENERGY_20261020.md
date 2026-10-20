# Signed correlations: resolution and arithmetic precision

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded turn metadata. Separate same-model derivations and
[internal review][review]; no specialist review or priority claim.

**Outcome:** a sharp bandwidth cost for one full-window second-moment
consumer; an asymptotically exact limit on universal multiplicative-phase
positivity; and a sharp local Möbius-energy cost of multiplicity. These
quantify three proposed arithmetic approaches. None obtains an upper bound
that excludes a multiple zero of the unchanged theta function.

The [program][program], [result index][results], [collision catalogue][controls]
and [avoid index][avoid] apply, especially [equivalent targets][a01],
[control premises][a02], [scoped conclusions][a07], [separate payments][a12]
and [gain before expansion][a20]. The gains below are the explicit costs
and constants, not the reformulations of simplicity. No new numerical
campaign or manuscript is justified by them. Ordinates in this note use
the original zeta coordinate, half the heat-coordinate height.

## 1. A full-window second moment has a sharp resolution floor

Assume RH when interpreting the following finite real configuration as
zeta zeros. Let an interval `I=[a,b]`, of width `W=b-a>0`, contain distinct
ordinates `lambda_1<...<lambda_M` of multiplicities `m_i`, and let
`N=sum m_i`. Retain these endpoint conventions. Using Note 02's Fourier
convention and kernel, put
\[
 K_\Delta(x)=\left(\frac{\sin\pi\Delta x}{\pi\Delta x}\right)^2,
 \quad S_{I,\Delta}(t)=\sum_i m_iK_\Delta(t-\lambda_i),
 \quad \mathcal C_{I,\Delta}=\frac{3\Delta}{2}
                         \int_{\mathbb R}S_{I,\Delta}(t)^2dt.
                                                               \tag{1}
\]
Squaring the triangular Fourier transform gives the exact autocorrelation
\[
 \frac{3\Delta}{2}\int K_\Delta(t-u)K_\Delta(t-v)dt
 =R(2\pi\Delta(u-v)),\qquad
 R(z)=\frac{6(z-\sin z)}{z^3},\quad R(0)=1.             \tag{2}
\]
The unnormalized value at `u=v` is `2/(3 Delta)`. Since `R` is even
and strictly positive,
\[
 \boxed{\mathcal E_{I,\Delta}:=\mathcal C_{I,\Delta}-N
 =\sum_i m_i(m_i-1)
  +2\sum_{i<j}m_im_jR(2\pi\Delta(\lambda_j-\lambda_i)).} \tag{3}
\]
Thus `E<2` excludes every multiple zero in `I`. A double contributes
exactly two to the first sum; arbitrary multiplicities are retained.
For a fixed finite configuration the second sum tends to zero as
`Delta->infinity`. The resulting existence criterion is a reformulation,
not the result claimed here. The quantitative result is
\[
 \boxed{\liminf_{N\to\infty}\frac{\Delta W}{N^{3/2}}
 \ge\frac12\quad\text{for any sequence with }\mathcal E_{I,\Delta}<2.}
                                                               \tag{4}
\]
It applies even if every signed arithmetic term is evaluated exactly.

### Proof including clustered configurations

For all real `z`,
\[
                         R(z)\ge\frac6{(|z|+3)^2}.       \tag{5}
\]
For `0<=z<=2`, the alternating Taylor bound gives
`R(z)>=1-z^2/20>=4/5`, whereas the right side is at most `2/3`.
For `z>=2`, use `R(z)>=6(z-1)/z^3` and
`(z-1)(z+3)^2-z^3=5z^2+3z-9>0`. Evenness finishes the proof.

List the `N` zero occurrences in increasing order, allowing equal
locations when multiplicities exceed one. Equation (3) is twice the
sum of `R` over distinct occurrence indices, including coincident pairs.
For their `k`-neighbor distances `d_(i,k)`, each consecutive gap occurs
at most `k` times in the sum, giving `sum_i d_(i,k)<=kW`.
Apply Jensen to the decreasing convex function
`x -> 6/(3+2 pi Delta x)^2`. This proves the explicit lower bound
\[
 \boxed{\mathcal E_{I,\Delta}\ge
 12\sum_{k=1}^{N-1}
 \frac{(N-k)^3}{[3(N-k)+2\pi\Delta kW]^2}.}             \tag{6}
\]
No separation assumption on individual zeros was used. The `k=1`
term, together with `E<2`, implies
\[
 \Delta W>\frac{N-1}{2\pi}
                 \left(\sqrt{6(N-1)}-3\right).          \tag{7}
\]
In particular `liminf Delta W/N^(3/2)>=sqrt(6)/(2 pi)>0`.
Along a subsequence with that ratio tending to finite `c`, retain the
first `K` terms of (6), let `N->infinity`, and then `K->infinity`:
\[
 \liminf\mathcal E_{I,\Delta}\ge
 \frac3{\pi^2c^2}\sum_{k\ge1}k^{-2}=\frac1{2c^2}.       \tag{8}
\]
Any `c<1/2` contradicts `E<2`. Unbounded subsequences cause no issue,
proving (4).

The constant is sharp for this geometric consumer. For equally spaced
simple points of gap `W/(N-1)` and `Delta W=c N^(3/2)`, write
`q=2 pi c N^(3/2)/(N-1)`. Then
\[
 \mathcal E=2\sum_{k=1}^{N-1}(N-k)R(qk)
 =\frac{12}{q^2}\sum_{k=1}^{N-1}\frac{N-k}{k^2}
       +O(N/q^3)\longrightarrow\frac1{2c^2}.            \tag{9}
\]
Every fixed `c>1/2` eventually passes in this model. Equal spacing is
not asserted for zeta; this checks the leading cost, not theta zeros.

For `(0,T]`, Riemann–von Mangoldt gives `N~T log T/(2 pi)` under RH's
identification of these ordinates. Hence this particular full-window
certificate needs
\[
 \Delta\ge\left(\frac1{2(2\pi)^{3/2}}+o(1)\right)
                         \sqrt T(\log T)^{3/2}.        \tag{10}
\]
The associated Fejér prime horizon is `X=exp(2 pi Delta)`, so even its
nominal `log X` is at least
`(1/(2 sqrt(2 pi))+o(1)) sqrt(T)(log T)^(3/2)`.
The finite-window projection still has to be paid, as below. A normalized
average with error `o(N)` cannot exclude one double by (3); the excess
must be bounded in absolute units below two. The classical
[pair-correlation account][goldston], §5, obtains a proportion result;
[Goldston–Lee–Schettler–Suriajaya][pcc], Theorem 1, likewise states an
asymptotic 100% conclusion under PCC, not simplicity of every zero.

### The arithmetic retains both correlations and exterior zeros

Note 02 gives the full zero sum
`S_Delta(t)=A_Delta(t)-Q_Delta(t)`, where `A=G+P` retains the complete
gamma integral and both pole terms, and
\[
 Q_\Delta(t)=\sum_{n\le X}a_n\cos(t\log n),\qquad
 a_n=\frac{\Lambda(n)}{\pi\Delta\sqrt n}
                   \left(1-\frac{\log n}{\log X}\right).
\]
For a nonnegative compactly supported integrable `w`, set
`W_hat(v)=integral w(t) exp(i v t)dt`. Direct expansion, with finite
prime sums, gives
\[
 \begin{aligned}
 \int wS_\Delta^2
 &=\int wA_\Delta^2-2\sum_n a_n\int wA_\Delta\cos(t\log n)dt\\
 &\quad+\frac12\sum_{n,r}a_na_r\Re\{
       \widehat W(\log(n/r))+\widehat W(\log(nr))\}.
 \end{aligned}                                                   \tag{11}
\]
For `w=1_[gamma-H,gamma+H]/(2H)`, its transform is
`exp(i gamma v) sinc(Hv)`. Both sum and difference frequencies matter.
The diagonal prime sum is not an upper bound for this expression.

The full `S_Delta` is not `S_(I,Delta)`; its unweighted squared integral
on the entire line diverges. For `J=[a-R,b+R]`, `R>0`, positivity under
RH and the two reciprocal-fourth-power tails give instead
\[
 \boxed{\mathcal C_{I,\Delta}\le
 \frac{3\Delta}{2}\int_J S_\Delta(t)^2dt
                    +\frac{N^2}{\pi^4\Delta^3R^3}.}    \tag{12}
\]
Indeed `0<=S_I<=S` on `J`; outside it, each side contributes at most
`N^2/(3 pi^4 Delta^4 R^3)` before multiplying by `3 Delta/2`.
All exterior-zero contributions inside `J`, including positive cross
terms, remain on the right. Removing them requires independent
membership and tail information. Neither (11) nor (12) has been bounded
below the required `N+2` here.

## 2. Universal multiplicative-phase positivity saves only one unit

This section tests a different information class. Put `V=2 pi Delta`,
`X=e^V`. For arbitrary phases `z_p` on the unit circle, extended completely
multiplicatively to `z_n`, define
\[
 Q_V(z)=\frac2V\sum_{p^k\le e^V}
 \frac{\log p}{p^{k/2}}\left(1-\frac{k\log p}{V}\right)
                     \Re z_p^k,
 \quad C_V=\frac2V\sum_{n\le e^V}\frac{\Lambda(n)}{\sqrt n}
                              \left(1-\frac{\log n}{V}\right),
 \quad \mu(V)=\min_z Q_V(z).                            \tag{13}
\]
The actual phases are `z_p=exp(i gamma log p)`. A lower bound based
only on identities and positivity valid for **every** multiplicative
phase assignment cannot exceed `mu(V)`. This includes universal
nonnegative squares of Dirichlet polynomials and their Gram inequalities.
It excludes additional height, RH zero-data or event-conditioned input.

The precise result is
\[
                         \boxed{\mu(V)=-C_V+1+o(1).}    \tag{14}
\]
To prove it, assign `z_p=-1`. The even powers alone give
\[
 Q_V(-1)+C_V
 =\frac4V\sum_{n\le e^{V/2}}\frac{\Lambda(n)}n
                                  \left(1-\frac{2\log n}{V}\right)
 =1+o(1).                                               \tag{15}
\]
The last equality is partial summation from the prime number theorem:
the sum is asymptotic to `V/4`. Higher even powers are automatically
included by the substitution `n=p^j`; no square term is omitted.

This phase assignment is within `O(1/V)` of the exact minimum. Discard
the zero-weight endpoint if `p=e^V`. For `64<=p<e^V`, let
`r=p^(-1/2)<=1/8` and
`b_k=r^k(1-k log p/V)_+`. The first harmonic is minimized at phase
`pi`, and
\[
 \sum_{k\ge2}k^2b_k\le b_1\sum_{k\ge2}k^2r^{k-1}
 \le\frac{233}{343}b_1<b_1.                             \tag{16}
\]
Here `sum_{k>=2} k^2 r^(k-1)=(1+r)/(1-r)^3-1`.
The inequality `1-cos(k theta)<=k^2(1-cos theta)` shows that the first
harmonic's increase away from `pi` dominates any decrease in the rest.
Thus each such prime polynomial is minimized there. The finitely many
primes below 64 can improve the value by only `O(1/V)`, since their
geometric coefficient sums are bounded independently of `V`. Equation
(15) proves (14).

With Note 02's same complete gamma and absolute pole payments, put
`U_torus=G+E-mu(V)` and `U_abs=G+E+C_V`. For `Delta>=1`,
\[
 \boxed{\inf_{\Delta\ge1}U_{\rm torus}(\gamma)
 =\inf_{\Delta\ge1}U_{\rm abs}(\gamma)-1+o(1)
 =\left(\frac12+o(1)\right)
                         \frac{\log\gamma}{\log\log\gamma}.}    \tag{17}
\]
The correction `mu+C` is uniformly bounded for `V>=2 pi` and tends to
one. Every competitive bandwidth tends to infinity: bounded `V` leaves
a gamma cost of order `log gamma`, whereas Note 02 gives a candidate
of order `log gamma/log log gamma`. Applying (14) to near-minimizing
sequences for either envelope proves the first equality.

Thus this universal positivity class recovers an additive unit but no
leading improvement. On the concrete microscopic rule `V=log gamma`,
the gamma term tends to one but
`C_V~8 sqrt(gamma)/(log gamma)^2`; the phase relaxation retains that
divergent cost. Keeping the exact signed pole term instead of its
absolute payment also leaves (17) unchanged: Note 02's pole bound gives
`E/C_V=O(gamma^(-2))` uniformly for `V>=2 pi`. At any competitive
bandwidth `C_V=O(log gamma/log log gamma)`, so this pole payment is
`o(1)`. No missing main/pole cancellation explains the comparison.

The witness is a finite-horizon torus assignment,
not an actual zero ordinate or an RH-compatible replacement for zeta.
Even fixed-horizon phase approximation says nothing about the coupled
rule `V` proportional to `log gamma` or the condition `zeta=zeta'=0`.
Signed remaining-zero terms in a Toeplitz explicit formula must still
be retained; Note 04's warning about dropping them is unchanged.

## 3. Reciprocal-zeta energy measures a different, sharp cost

Let `M(x)=sum_(n<=x) mu(n)`, `f(y)=e^(-y/2)M(e^y)`, and
\[
 E(\alpha)=\int_1^\infty M(x)^2x^{-2-\alpha}dx,
 \qquad A(Y)=\int_1^{e^Y}M(x)^2x^{-2}dx.                \tag{18}
\]
Under RH, `M(x)=O_eta(x^(1/2+eta))` for each `eta>0`. Partial summation
and continuation give, for `Re z>0`,
\[
 B(z)=\int_0^\infty f(y)e^{-zy}dy
     =\frac1{(z+1/2)\zeta(z+1/2)},\qquad
 E(\alpha)=\frac1{2\pi}\int_{\mathbb R}
                             |B(\alpha/2+it)|^2dt.      \tag{19}
\]
The second identity is Plancherel for the zero extension of
`e^(-alpha y/2)f(y)`; no pointwise reciprocal-zeta bound is supplied.

If `rho=1/2+i gamma`, `gamma>0`, has exact multiplicity `m`, set
`a_m=m!/[rho zeta^(m)(rho)]`. Its local Laurent expansion is
`B(z)=a_m/(z-i gamma)^m+O(|z-i gamma|^(1-m))`.
Choose disjoint fixed neighborhoods of the conjugate pair. Scaling
`t-gamma=(alpha/2)v` in (19) and using the local bound
`|B(z)|<=C|z-i gamma|^(-m)` gives dominated convergence. Each
neighborhood contributes
`binom(2m-2,m-1)|a_m|^2` after multiplying by `alpha^(2m-1)`.
All remaining energy is nonnegative. Therefore
\[
 \boxed{\liminf_{\alpha\downarrow0}\alpha^{2m-1}E(\alpha)
 \ge2\binom{2m-2}{m-1}
                 \left|\frac{m!}{\rho\zeta^{(m)}(\rho)}\right|^2.}
                                                               \tag{20}
\]
No simplicity of other zeros or global expansion over their reciprocals
is used. For a double zero,
\[
 \boxed{\liminf_{\alpha\downarrow0}\alpha^3E(\alpha)
          \ge\frac{16}{|\rho\zeta''(\rho)|^2}>0.}       \tag{21}
\]
The constant in (20) is sharp for isolated-pole extraction: the real
function `2 Re[a_m y^(m-1)e^(i gamma y)/(m-1)!]` attains it
asymptotically. This is an analytic sharpness example, not a Möbius model.
The Abel identity `E(alpha)=alpha integral e^(-alpha Y)A(Y)dY` yields
only the correctly one-sided consequence
\[
 \limsup_{Y\to\infty}\frac{A(Y)}{Y^{2m-1}}
       \ge\frac{2|a_m|^2}{(2m-1)((m-1)!)^2}.           \tag{22}
\]
For its proof, a finite upper limsup bounds `A(Y)` eventually by
`(C+epsilon)Y^(2m-1)`; insert that bound into the Abel transform and
use its gamma integral. An infinite limsup already satisfies (22).
In particular no lower-liminf claim about `A` is inferred.

### The signed coefficient term remains unpaid

For every `alpha>0` under RH, summation by parts for the step function
`M(x)^2` proves
\[
 \boxed{(1+\alpha)E(\alpha)
 =\frac{\zeta(1+\alpha)}{\zeta(2+2\alpha)}
       +2\sum_{n\ge1}\frac{\mu(n)M(n-1)}{n^{1+\alpha}}.}          \tag{23}
\]
Use `M(n)^2-M(n-1)^2=mu(n)^2+2mu(n)M(n-1)`.
RH makes the endpoint `M(N)^2 N^(-1-alpha)` vanish and the integral
converge. Thus the displayed series converges in increasing `n`; it
is not asserted absolutely convergent near zero. The diagonal is
`6/(pi^2 alpha)+O(1)`. A double zero would force the cubic energy
in (21) into the signed off-diagonal sum. Coefficient positivity of
the diagonal does not bound that sum. Applying absolute values with
the basic RH pointwise bound only pays it for `alpha>1/2`.

**Continuation:** [Note 08](08_RECIPROCAL_PRECISION_AND_BANDLIMITED_ARITHMETIC_COSTS_20261020.md) strengthens the
recorded energy upper envelope to
`log(2+E(alpha)) <<_epsilon alpha^-1 (log(1/alpha))^(2+epsilon)`
by using the underlying uniform reciprocal estimate directly. The
following `5+2eta` bound remains valid for the stated Mertens-envelope
argument; neither bound contradicts the cubic double-zero cost.

The verified [Balazard–de Roton RH bound][bdr] gives
`M(x)<<_eta sqrt(x) exp(sqrt(log x)(log log x)^(5/2+eta))`.
It implies, with any fixed `eta>0`,
\[
 \log(2+E(\alpha))\ll_\eta
       \alpha^{-1}(\log(1/\alpha))^{5+2\eta}.           \tag{24}
\]
Split at `Y0=C alpha^(-2)(log(1/alpha))^(5+2eta)` with a large fixed
`C`: the growing exponent is bounded by the displayed order before
`Y0`, and at most `alpha Y/2` afterward. This bound still permits
every fixed polynomial divergence, including (21). No best-bound
survey or impossibility theorem for all RH methods is intended.

[Bui–Florea, Theorem 1.2][bf] gives shifted negative-moment bounds
under RH with `log(1/beta)/log log T=O(1)`. It does not allow `beta->0`
at fixed height near a candidate zero; its admissible averages retain
the interval-length factor. Separately, the optimal Nyman–Beurling
rate theorem of [Bettin–Conrey–Farmer][bcf] explicitly assumes a
negative derivative moment that already requires simplicity. Neither
is imported as the missing fixed-pole upper bound. Note 03's
weak-Mertens benchmark is likewise still an unproved stronger input.

Fixed positive Gaussian smoothing does not repair the exponent: for
the frequency weight `exp(-2tau t^2)` in (19), the local pair constant
in (20) is multiplied by `exp(-2tau gamma^2)>0`. Norm contraction
supplies no bound for the original unknown energy. This reciprocal-zeta
energy is not the theta Gaussian deficit of Note 01.

### Localized reciprocal energy: the same pointwise payment remains insufficient

20 October 2026. For Edward Baker with LLM assistance, **gpt-6-astra, ultra**;
same-model internal cross-check. This is a scoped assessment, not a new criterion.

Assume RH and keep (19)'s `B(z)=1/((z+1/2) zeta(z+1/2))`. Fix a sufficiently large
ordinate `gamma` with an exact double zero `rho=1/2+i gamma`. Let
`w>=0` be continuous, compactly supported in a neighborhood containing
no other zero ordinate, with `w(gamma)>0`. The same Laurent expansion and
dominated-convergence argument as (20) give

\[
\lim_{\alpha\downarrow0}\frac{\alpha^3}{2\pi}
 \int w(t)|B(\alpha/2+it)|^2dt
 =\frac{8w(\gamma)}{|\rho\zeta''(\rho)|^2}.
\tag{LE1}
\]

This is one ordinate; the conjugate pair gives (21)'s factor sixteen.

For a fixed neighborhood `|t-gamma|<=d`, put `V_* = sup V(t)`, with
`V(t)` defined in [Note 08](08_RECIPROCAL_PRECISION_AND_BANDLIMITED_ARITHMETIC_COSTS_20261020.md)(R1).
For sufficiently small `alpha`, its (R2), at `h=alpha/2`, is uniformly

\[
 \log|\zeta(1/2+\alpha/2+it)|^{-1}
 \le V_*\log(1/\alpha)+O_\gamma(1).
\tag{LE2}
\]

Indeed, the remaining terms in that displayed bound are bounded on this
fixed compact height neighborhood. Thus `|B|<<_gamma alpha^(-V_*)`, and
`V_*~log(gamma)/(2 log log(gamma))` as gamma increases with fixed d.
Here gamma is fixed **before** taking `alpha->0`; this is not Note 08's
coupled microscopic-height limit.

Shrinking the window does not repair the large-height exponent. For
nonnegative continuous compactly supported `W`, with `W(0)>0`, set

\[
 E_W(\alpha)=\frac1{2\pi}\int
 W((t-\gamma)/\alpha)|B(\alpha/2+it)|^2dt.
\]

Writing `a_2=2/(rho zeta''(rho))`,

\[
 \alpha^3E_W(\alpha)\longrightarrow
 \frac{|a_2|^2}{2\pi}\int\frac{W(v)}{(1/4+v^2)^2}dv>0,
 \qquad E_W(\alpha)\ll_{\gamma,W}\alpha^{1-2V_*}.
\tag{LE3}
\]

The paid upper exponent no longer opposes the event when `V_*>=2`.
Windows narrower than alpha remove the same width factor from the local
pole contribution and this pointwise allowance. No signed Möbius
correlation bound or endpoint-coefficient lower bound follows. This
assesses only (LE2)'s pointwise payment, not all localized-energy methods.

[Continuation review](../reviews/14_REMOTE_GAP_COMPLETE_PAYMENT_AND_EVENT_ATTEMPTS_REVIEW_20261020.md).

## 4. Disposition for the contour program

The correlation atom `m(m-1)` reweights the same multiplicity whose
local phase charge is `(m-1)pi`; it supplies no opposing sign. Existing
endpoint controls give at least two in (3) on their own zero data.
They fail the unchanged arithmetic specified in Notes 03 and 05 and
are not counterexamples to an estimate using the genuine Möbius data.

The precise new restrictions are (4), (17), and (20)–(24). A useful
next estimate must exploit actual-height/event information beyond
universal phase positivity, or bound a genuinely localized signed
correlation with its exterior contribution and absolute error paid.
No such upper estimate was obtained. The arithmetic, strict-surplus
and all-zero gates in the [progress register][progress] remain open.

[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[progress]: ../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md
[review]: ../reviews/06_CORRELATION_AND_MOBIUS_ENERGY_REVIEW_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
[goldston]: https://arxiv.org/pdf/math/0412313
[pcc]: https://arxiv.org/pdf/2503.15449
[bdr]: https://arxiv.org/pdf/0810.3587
[bf]: https://arxiv.org/pdf/2302.07226
[bcf]: https://arxiv.org/pdf/1211.5191
