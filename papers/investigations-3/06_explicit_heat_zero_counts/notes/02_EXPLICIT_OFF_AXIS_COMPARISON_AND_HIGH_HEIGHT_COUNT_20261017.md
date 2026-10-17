# Explicit off-axis comparison and the first high-height count

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort:
**ultra**, verified from the conversation metadata. Three same-model
development subagents supplied the ordinary-term estimates, carrier paths
and general-real-part remainder calculation.

**Status: analytic derivation proved in this note from the named classical
inputs; unreviewed.** The user requested continued extraction on 17 October
and postponed review for further rounds. No new stand-alone review is
claimed. This is quantitative infrastructure, not an RH-equivalent
criterion, a new zero-free region or a Newman-bound improvement. There is
still no active consumer with an application tolerance.

This continues [Note 01](01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md).
The [result index](../../../../result-summaries/README.md), especially
[11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
and [12](../../../../result-summaries/12_collision_controls_and_screening.md),
and the [avoid index](../../../../avoid/README.md), especially
[08](../../../../avoid/08_normalization_and_constant_slips.md),
[16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md) and
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), remain
the routing and scope controls. The earlier conditional lemma is retained
unchanged, including its reviewed hash; this note supplies its missing
premise only on the restricted domain stated below.

## 1. Result and remaining domain

In the physical coordinate and heat normalization of Note 01, for

\[
 0<t\le\tfrac12,\qquad x\ge2\cdot10^6,\qquad 3\le y\le4,
\]

put \(s_+=(1+y-ix)/2\) and \(B_t(x+iy)=M_t(s_+)\). Then

\[
 \left|\frac{H_t(x+iy)}{B_t(x+iy)}-1\right|
 <\frac{95}{147}+\frac{11}{1000}+\frac1{25000}
                +\frac{26}{2\cdot10^6}
 <\frac{33}{50}<\frac7{10}.                         \tag{1}
\]

Consequently, counting all complex zeros with multiplicity in the
half-open unit window,

\[
 \boxed{\quad
 K_t(X):=\#\{\rho:H_t(\rho)=0,\ X<\Re\rho\le X+1\}
 \le\frac65\log(X+2)+22,\quad
 0<t\le\tfrac12,\quad X\ge2\cdot10^6.\quad}          \tag{2}
\]

No unevaluated comparison constant remains in (1)-(2). The original
200<=X<2,000,000 region is **not covered by this derivation**. This
restriction replaces the proposed compactness step explicitly. The
cutoff is chosen to match the convenient general-real-part remainder
lemma below, not asserted optimal. The cumulative count, exact integer
counts and a consumer gain remain open or unrequested. Review is deferred.

## 2. Precisely imported source statements

Use D.H.J. Polymath, [arXiv:1904.12438v2](https://arxiv.org/pdf/1904.12438v2),
4 August 2019. Printed pages 20 and 22-27 were additionally inspected this
round; the source's equations are also available in its
[HTML rendering](https://arxiv.org/html/1904.12438). No third-party PDF is
stored in the repository.

The proof imports the exact expansion (39), contour shift (41), explicit
Stirling estimate Lemma 5.1(v), Proposition 6.1 for every real sigma,
and the general-real-part coefficient and remainder bounds of Proposition
6.2, including |C_0(p)|<=1/2. These are the classical analytic inputs;
finite arithmetic checks do not prove them. We do **not** import Proposition
6.3's final constants outside its stated range 0<=sigma<=1, or the
discrepant heat coefficient after (99).

Write

\[
 T=x/2,\quad T'=T+\pi t/8,\quad Q=x/(4\pi),\quad L=\log Q,
 \quad a=\sqrt{T'/(2\pi)},\quad N=\lfloor a\rfloor,
\]
\[
 s_-=(1-y+ix)/2,\qquad b_n^t=e^{t\log^2 n/4},\qquad
 \alpha(s)=\frac1{2s}+\frac1{s-1}+\frac12\operatorname{Log}\frac{s}{2\pi}.
\]

The two real parts lie in [-3/2,5/2]. All logarithms are natural and use
the source's analytic branches; conjugation supplies the corresponding
lower-half-plane estimates. Expansion (39) is valid at these nonreal
arguments. Its two ordinary sums have approximants

\[
 M_t(s_\pm)\sum_{n=1}^N b_n^t n^{-s_\pm-(t/2)\alpha(s_\pm)}.       \tag{3}
\]

The exact expansion has one R_{t,N} term on each branch, with the
reflections specified in (39). The bounds below use their moduli and
are unaffected by those reflections. The same N is used throughout.

## 3. Ordinary terms and the corrected heat weight

For s=sigma+/-iT with -3/2<=sigma<=5/2, direct use of alpha gives

\[
 \Re\alpha(s)\ge L/2-13/x^2,\qquad
 |\alpha(s)-L/2\mp i\pi/4|
 \le\frac{11}{2x}+\frac{25}{4x^2}<\frac6x.            \tag{4}
\]

For the first bound, the real rational terms are at least -13/x^2 and
the log-modulus correction is nonnegative. For the second, use
|arctan(sigma/T)|<=|sigma|/T, log(1+sigma^2/T^2)<=sigma^2/T^2,
and the modulus bounds for the rational terms. Also

\[
 \log N\le L/2+\pi/(16x),\qquad
 |\alpha(s)-\log n|\le L/2+1\le\log x\quad(1\le n\le N).
\]

In particular the exact, correctly normalized heat weight satisfies

\[
 W_n(s):=b_n^t n^{-(t/2)\Re\alpha(s)}
 =\exp\left[\frac t4\log n\{\log n-2\Re\alpha(s)\}\right]\le1.   \tag{5}
\]

Indeed 2Re alpha-log N >= L/2-pi/(16x)-26/x^2>0 on the stated domain.
This uses t/4 in the exponent of b_n^t, rather than the erroneous
coefficient in the later asymptotic display discussed in Note 01.

Proposition 6.1 supplies an ordinary-term relative error at most

\[
 \exp\left(\frac{(t^2/8)|\alpha(s)-\log n|^2+t/4+1/6}{T-3.33}\right)-1
 \le \exp\left(\frac{3(\log x)^2/32+7/8}{x}\right)-1
 <\frac1{50000}.                                    \tag{6}
\]

Here T-3.33>=x/3. Both (log x)^2/x and 1/x decrease on this domain.
At x=2,000,000, log x<15, so the exponent is at most
703/(32*2,000,000)<1/8; e^u-1<=8u/7 then proves (6).

Thus the dominant branch's nonleading terms total at most
zeta(2)-1<=95/147, with its leading term exactly 1 after normalization.
The opposite branch is bounded in Section 5.

## 4. General-real-part remainder with explicit constants

We establish the following auxiliary estimate for

\[
 T\ge10^6,\quad -\tfrac32\le\sigma\le\tfrac52,
 \quad 0<t\le\tfrac12,
 \quad T'=T+\pi t/8,\quad a=\sqrt{T'/(2\pi)},\quad N=\lfloor a\rfloor:
\]
\[
 |R_{t,N}(\sigma+iT)|\le e^{t\pi^2/64}|M_0(iT')|.     \tag{7}
\]

This is a deliberately coarse extension proved from the general source
inputs, not an assertion that its stated Proposition 6.3 has this domain.

### Gaussian envelope

In (41), shift by beta=pi*i/4 and put u=sigma+sqrt(t)*v, D=T-3.
After factoring out the phase and the carrier on the right of (7), the
Stirling and Taylor errors in the integrand have combined modulus at most

\[
 \frac{u^2}{4(T'-3)}+\frac{3|u|}{2T'}+\frac1{6(T'-0.66)}
 \le\frac{u^2+6|u|+2/3}{4D}
 \le\frac{u^2+1}{D}.                                \tag{8}
\]

The last step uses 6|u|<=3u^2+3. The horizontal Taylor segment stays at
imaginary part T', so (8) holds for every real u, however large. The
contour shift preserves positive imaginary part. Using +1 in (8) avoids
the printed constant compression immediately before (60); all subsequent
Gaussian integrations below use D consistently.

For u distributed with density exp(-(u-sigma)^2/t)/sqrt(pi*t), let
J_b=E exp((u^2+1)/D+b*u), and h=1-t/D. Completing the square gives

\[
 J_b=h^{-1/2}\exp\left(\frac{\sigma^2+1}{D}+b\sigma
             +\frac{t(\sigma/D+b/2)^2}{h}\right).     \tag{9}
\]

The elementary bound u^2<=2sigma^2+2t*v^2 also gives

\[
 J_0\le e^{14/(T-6)}<4/3.                            \tag{10}
\]

For b=log 9 or -log 2, remove the factor e^{b*sigma} in (9).
Its remaining factor is <2: use h>=999/1000,
(sigma^2+1)/D<1/1000, |sigma|/D<1/1000,
-(log h)/2<1/1000, and log 3<11/10. Its logarithm is less than

\[
 \frac2{1000}+\frac12(1101/1000)^2(1000/999)<2/3<\log2.
\]

### Coefficients, including the fixed-index remainder

Choose K_u=1 for u>=0, and K_u=max(floor(-u)+3,m), m=floor(2a^2),
for u<0. This satisfies the negative-real-part condition K_u+u>=2 in
Proposition 6.2. The coefficient estimates (54)-(57), summed by the
gamma recurrence as in the proof of (62)-(64), give the pointwise majorant

\[
 \begin{split}
 S(u):=\sum_{k=1}^{K_u}\frac{|C_k(p,u)|}{a^k}+|RS_{K_u}(u+iT')|
 \le{}&\frac{0.2\,9^u}{a-0.865}+\frac{0.029\,2^{-u}}{a-0.353}\\
 &+\frac{2^{-u}}2\sum_{2a^2\le k\le-u+4}
         \frac{1.1^k\Gamma(k/2)}{a^k}+E_a,
 \qquad E_a:=a^{-1}e^{-a^2/2}.                        \tag{11}
 \end{split}
\]

The added E_a is essential bookkeeping for our proof. When K_u=m,
the source's displayed tail range can be empty while RS_m is still
present. To bound that term, put nu=(m+1)/2 in (a^2,a^2+1/2]. Then

\[
 |RS_m|\le\tfrac12\Gamma(\nu)(1.1/a)^{2\nu}
 \le\frac3{2a}\exp\{\nu\log(\nu/a^2)-4\nu/5\}
 <\frac5a e^{-4a^2/5}\le E_a.                        \tag{12}
\]

Here a>300, explicit real Stirling gives
Gamma(nu)<=3nu^(nu-1/2)e^(-nu), log(1.21)<1/5,
log(nu/a^2)<=1/(2a^2), and 3a^2/10>log 5.
When K_u>m, every coefficient beyond m has index greater than 2a^2;
the remainder index K_u+1=floor(-u)+4 is also greater than 2a^2 and
at most -u+4. Thus the displayed tail covers all remaining terms.
This exhausts the floor cases without discarding a remainder.

For completeness, the elementary coefficient summation in (11) uses
0.200*9^u/a+0.173*2^(3u/2)/a^2 on u>=0. On u<0 its low-index
portion is at most

\[
 0.036\,2^{-u}\left(\frac{0.445\sqrt\pi}{a}
                      +\frac{0.247}{a^2}+\frac{0.098}{a^3}\right)
 \le\frac{0.029\,2^{-u}}{a-0.353}.
\]

These are numerical bounds from (54)-(57), not new limiting assumptions.
The geometric summations use Gamma((k+2)/2)=k*Gamma(k/2)/2 for k<=2a^2.

### Integrating the four remainder contributions

Let delta_j be the four expectations from (11), after multiplication by
exp((u^2+1)/D). Equation (9) yields

\[
 \delta_1+\delta_2
 <\frac{0.4\,9^\sigma+0.058\,2^{-\sigma}}{a-0.865}
 \le\frac{97.374}{a-0.865}\le\frac{98}{a}.           \tag{13}
\]

We used 9^sigma<=243 and 2^(-sigma)<3. In the tail delta_3,
k>=14 and u<=4-k<=-10. Therefore (u-sigma)^2>=9u^2/16 and

\[
 \frac{u^2+1}{D}-\frac{(u-\sigma)^2}{t}
 \le\frac1D-\frac{u^2}{2t}.
\]

Integrating exp(-u^2/(2t)-u*log2) over u<=4-k gives

\[
 \delta_3\le\frac{4\cdot10^{-30}}{a^{14}}<1/a.       \tag{14}
\]

The numerical tail constant can be checked without unbounded gamma
asymptotics. For f(k)=1.1^k*Gamma(k/2)*exp(-(k-4)^2+(k-4)*log2),
the explicit values at k=14,15 are below 10^(-30), and
f(k+2)/f(k)=2.42*k*exp(-4k+12)<1 for k>=14. The arithmetic record
checks rational upper bounds using e>8/3 and sqrt(pi)<2. The geometric
sum in 1/a and the harmless exp(1/D)<2 give (14).

Finally, delta_4<=E_a*J_0<(4/3)*E_a<1/a. Combining (10),
(13)-(14), |C_0|<=1/2 and a>300 proves

\[
 \frac{|R_{t,N}|}{e^{t\pi^2/64}|M_0(iT')|}
 \le\tfrac12J_0+\sum_{j=1}^4\delta_j
 <\tfrac12\cdot\tfrac43+\frac{100}{300}=1,
\]

which establishes (7). The auxiliary cutoff T>=10^6 implies a>300
using pi<22/7. No compactness constant was used.

## 5. Carrier ratios and closing the budget

Put A=(1+y)/2 in [2,5/2], C=1-A in [-3/2,-1], and
G(sigma,tau)=Re log M_0(sigma+i*tau). On every path below the
imaginary part is positive, after conjugating the denominator if needed.
For -3/2<=sigma<=5/2, direct estimates give

\[
 |\Re\alpha(\sigma+iT)-L/2|\le85/(16T^2),\quad
 |\Im\alpha(\sigma+iT)-\pi/4|\le11/(4T),
\]
\[
 |\alpha|\le L/2+1,\qquad |\alpha'|\le1/(2T)+3/(2T^2).
\]

Integrating Re(alpha+(t/2)alpha*alpha') from C to A consequently gives

\[
 \log\left|\frac{M_t(s_-)}{M_t(s_+)}\right|
 \le-\frac y2 L+\frac{85}{x^2}
       +(L/2+1)(1/x+6/x^2)
 \le-\frac y2 L+\frac{\log x}{x}.
\]

The final inequality holds already for x>=8500, log x>=3, and so on
our domain. Since log x/x<1/2 here,

\[
 \left|M_t(s_-)/M_t(s_+)\right|<2Q^{-y/2}.           \tag{15}
\]

For the remainder carrier, an exact horizontal integration gives

\[
 \begin{split}
 G(A,T)-G(0,T)-AL/2={}&\tfrac14\log(1+A^2/T^2)\\
 &+\tfrac12\log\frac{T^2+(A-1)^2}{T^2+1}
  +\tfrac14\int_0^A\log(1+\sigma^2/T^2)\,d\sigma\ge0,
 \end{split}
\]

because A>=2. Along the imaginary axis,
partial_tau G(0,tau)<=-pi/4+3/(2T) for tau>=T. At A+iT,
Re alpha>=L/2 and 0<=Im alpha<=pi/4. Hence the heat normalization
and the T-to-T' vertical displacement combine to give

\[
 e^{t\pi^2/64}\frac{|M_0(iT')|}{|M_t(s_+)|}
 \le Q^{-A/2}\exp\{-tL^2/16+3\pi t/(8x)\}
 \le Q^{-(1+y)/4}.                                  \tag{16}
\]

The last exponent is nonpositive since L>1>6pi/x. This cancellation
retains both heat contributions and the gamma decay; none is dropped
with an incorrect sign.

Since N<=sqrt(Q+t/16),

\[
 N^{(y+1)/2}<2Q^{(y+1)/4},\qquad
 |M_t(s_-)/M_t(s_+)|N^{(y+1)/2}
 <4Q^{-1/2}<11/1000.                                \tag{17}
\]

Indeed (1+t/(16Q))^((y+1)/4)<(33/32)^2<2 and
16*13/(2,000,000)<(11/1000)^2. Equations (5)-(6) bound the
normalized ordinary approximation error by

\[
 (\zeta(2)+11/1000)/50000<1/25000.
\]

The two R terms, by (7) and (16), total at most
2Q^(-(1+y)/4)<=2/Q<26/x. The dominant nonleading sum, opposite
sum, ordinary errors and remainders now give (1). For the disk centered
at X+1/2+(7/2)i with radius 1/2, all real parts are at least X and
all imaginary parts are in [3,4]. Thus (1) supplies Note 01's premise
(C), and its proved extraction lemma yields (2), with the same endpoint
and multiplicity conventions.

## 6. Verification, controls and next work

The standard-library [checker](../numerics/check_off_axis_comparison.py)
and [run record](../numerics/OFF_AXIS_COMPARISON_CHECKS_20261017.json)
verify the rational numerical allowances, Gaussian-moment budget,
initial tail coefficients, recurrence decrease and final comparison
budget. A requested comparison ceiling of 13/20 deliberately fails
the current sufficient budget with nonzero exit; that failure is not a
counterexample to the analytic comparison. These finite checks complement
the written proof and do not formally verify its classical imports,
contour shifts or universal analytic statements.

The [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
are treated exactly as in Note 01, Section 5. The generic count step
permits their collisions and counts multiplicity. Their modified sources
are outside the exact theta expansion (39) used to establish (1). This
does not assert that any particular control fails the numerical comparison
on a tested box; no new noncollision implication is made.

The next bounded analytic task is to lower the cutoff or cover the omitted
200<=X<2,000,000 region with explicit estimates, while recording a complete
gain-versus-error budget if a consumer becomes active. No numerical zero
survey, replacement certificate or manuscript is part of this round.
The requested review remains deferred; no
accepted manuscript milestone or new result-summary status is recorded.
