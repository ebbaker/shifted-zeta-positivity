# Explicit Gaussian constants and a smaller finite prime-scale interval

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model analysis and cross-review are internal checks, not
independent specialist refereeing.

Status: effective analytic inverse bounds, explicit physical and zero-count
constants, and a conditional finite-interval detector with every displayed
remainder below its allowance. The independent arithmetic cancellation
hypothesis remains unproved. No actual zeta-zero certificate or new zero-free
region is claimed. Mathematical priority has not been established.

This completes the first follow-up gate in the
[opening investigation](INITIAL_INVESTIGATION_20261004.md): the inverse
constants no longer depend on an unevaluated compact-frequency minimum.
The revised physical covering interval is

\[
\boxed{J_*=[24(N+1),208N],}
\tag{1}
\]

instead of \([16(N+1),368N]\). These are intervals for \(y=\log X\),
not for \(X\). The upper logarithmic endpoint falls by about 43.5 percent
at the same \(N\). A direct guard count also replaces the much larger
seven-unit-interval count. The resulting prime scales remain enormous.

Retain the opening note's exact transforms, full prepared prime observable,
pole subtraction, and total moment. Fix

\[
b=\frac34,\quad d=\frac9{16},\quad c=\frac{13}4,\quad
T=|t|\ge100,\quad k\ge8.
\]

The proved usable constants are

| Quantity | Explicit bound |
|---|---|
| Physical baseline | \(|f_t(y)|\le(33/4)e^y(1+y_+)\) |
| Weighted inverse norm | \(M_{b,t}(k)=\|q_{b,t,k}\|_1\le32\) |
| Early contour norm | \(P_d(t,k)\le4e^{9k/256}/\sqrt{k}\) |
| Late contour norm | \(P_c(t,k)\le2e^{25k/4}/\sqrt{k}\) |
| Restored-pole reciprocal | \(|D_t'(1)|^{-1}<T^{13}/(5\cdot10^{11})\) |
| Global unit-height count | \(\#\{\rho:v<\gamma\le v+1\}\le12\log(2+|v|)\) |

The late norm actually admits the stronger constant \(11/10\); two keeps
the final budgets simple. All norms refer to the full inverse of \(D_t\).
They do not assert Gaussian decay of the restored pole in physical space.

## An effective lower bound for the base transform

Write \(I_0=\int h\), \(a_0=\int h^2\), \(f=H/I_0\), and
\(z=x+i\nu\). Exact integration and the parent normalization give

\[
\frac{\int v^2h(v)\,dv}{I_0}=\frac1{304},\qquad
\frac{I_0}{\sqrt{a_0}}>\frac{91}{200},\qquad
N_t<\frac{111}{100}T^3\sqrt{a_0}\quad(T\ge100).
\tag{2}
\]

Evenness implies
\(|f(w)-1|\le |w|^2\cosh(|w|/4)/608\).
Thus \(|f(w)|>1/2\) for \(|w|\le8\), since \(\cosh2<4\).
Also Cauchy--Schwarz in the probability measure \(h(v)\,dv/I_0\)
gives \(|f'(x+i\nu)|\le e^{|x|/4}/\sqrt{304}\).

The manuscript's differential equation gives, for \(u(r)=f(zr)\),

\[
(r^{18}u')'=\frac{z^2}{16}r^{18}u.
\]

Multiply by \(\overline u\), integrate from zero to one, and take
imaginary parts without imposing \(u(1)=0\). The boundary at zero
vanishes, and

\[
\frac{|x\nu|}{8}\int_0^1r^{18}|u(r)|^2\,dr
\le |zf'(z)|\,|f(z)|.
\]

On \([0,r_0]\), \(r_0=\min(1,8/|z|)\), the integral is at least
\(r_0^{19}/76\). Therefore, when \(x\nu\ne0\),

\[
\boxed{\frac{|H(x+i\nu)|}{I_0}\ge
\frac{\sqrt{304}|x\nu|}{608|x+i\nu|e^{|x|/4}}
\min\left(1,\frac8{|x+i\nu|}\right)^{19}.}
\tag{3}
\]

This is a fully effective global bound. Its nineteenth power is weaker
than the ninth-power endpoint asymptotic, but the Gaussian makes this
loss inexpensive in the remote frequency tail.

On the central frequencies a much better bound is available:

\[
\Re H(x+i\nu)\ge
I_0\left[1-\frac{\nu^2\cosh(|x|/4)}{608}\right].
\tag{4}
\]

Indeed expand the real part as the integral of
\(h(v)\cosh(xv)\cos(\nu v)\), then use \(\cos u\ge1-u^2/2\).
For \(|\nu|\le16\), (4) gives \(|H|>I_0/2\) when \(|x|\le3/4\),
and \(|H|>9I_0/19\) when \(|x|\le11/4\), since
\(\cosh(11/16)<5/4\).

For \(|\nu|\ge16\), (3) gives the explicit tail bounds

\[
|H(x+i\nu)|^{-1}\le\frac{420}{I_0}
             \left(\frac{|\nu|}{8}\right)^{19}
\quad\left(-\frac34\le x\le-\frac18\right),
\tag{5}
\]

\[
|H(x+i\nu)|^{-1}\le\frac{2000}{I_0}
             \left(\frac{|\nu|}{8}\right)^{19}
\quad\left(-\frac{11}4\le x\le-\frac1{16}\right).
\tag{6}
\]

For (5), use \(\sqrt{304}>17\), \(|\nu|/|z|>99/100\),
\(e^{3/16}<5/4\), and
\((1+9/4096)^{19/2}<33/32\). For (6), use
\(|\nu|/|z|>49/50\), \(e^{11/16}<2\), and
\((1+121/4096)^{19/2}<3/2\). The smaller real displacement
\(1/16\) is explicitly charged.

## Contour norms and the weighted physical norm

Put \(\gamma=t+\nu\). The preparation polynomial has modulus
\(|s(s-1/2)(s-1)|\), and

\[
|K(\sigma+i\nu)|^{-1}\le
\frac{\sqrt{(\sigma+2)^2+\nu^2}}{2^{\sigma+2}-1}.
\tag{7}
\]

For \(|\nu|\le16\), \(|\gamma|\ge84\) and
\(T/|\gamma|\le25/21\); each preparation factor is at least
\(|\gamma|\). Combining (2), (4), and (7) yields

\[
|D_t(d+i(t+\nu))|^{-1}\le5(41/16+|\nu|),
\qquad
|D_t(c+i(t+\nu))|^{-1}\le\frac23(21/4+|\nu|).
\tag{8}
\]

On the neighborhood \(5/8\le\sigma\le7/8\) of \(b\), the core
bound is \(|D_t(\sigma+i(t+\nu))|^{-1}\le13+4|\nu|\).
These coefficients follow from rational comparisons after using
\(2^{41/16}-1>4\), \(2^{21/4}-1>31\), and
\(2^{21/8}-1>5\), respectively.

The preparation lower bounds over the whole frequency line are
\((63/4096)(1+\gamma^2)^{3/2}\) on \(d,c\), and
\((15/512)(1+\gamma^2)^{3/2}\) on \([5/8,7/8]\).
For the latter, setting \(a=\sigma-1/2\) gives
\(\sigma(\sigma-1/2)(1-\sigma)=a/4-a^3\); its minimum on
\([1/8,3/8]\) is \(15/512\).
Also \(T/\sqrt{1+\gamma^2}\le1+|\nu|\).
Thus (5)--(7) imply, for \(|\nu|\ge16\),

\[
|D_t(\sigma+i(t+\nu))|^{-1}\le
\begin{cases}
25000|\nu|^{23}/8^{19},&5/8\le\sigma\le7/8,\\
400000|\nu|^{23}/8^{19},&\sigma=d,c.
\end{cases}
\tag{9}
\]

Integrating the core polynomials against \(e^{-k\nu^2}/(2\pi)\)
gives, after extracting \(k^{-1/2}\), the coefficients

\[
\frac{205}{32\sqrt\pi}+\frac5{2\pi\sqrt k}<\frac{221}{56},
\qquad
\frac7{4\sqrt\pi}+\frac1{3\pi\sqrt k}<1+\frac4{105}.
\]

The tails contribute less than \(1/(100\sqrt k)\).
For instance extract half the Gaussian in the second line of (9):
the remaining monomial times Gaussian decreases for \(|\nu|\ge16\),
so the tail is at most
\([400000\,16^{23}/8^{19}]e^{-128k}/\sqrt k\).
This proves the stated \(P_d\) bound and the stronger \(P_c\) constant
\(11/10\). There is no numerical integration.

For the physical norm use \(R(\nu)=D_t(b+i(t+\nu))^{-1}\) and
\(\psi(\nu)=e^{-k\nu^2}R(\nu)\).
Cauchy's estimate on a complex \(\nu\)-disk of radius \(1/8\),
inside the inverse pole-free strip, gives

\[
|R'(\nu)|\le108+32|\nu|\quad(|\nu|\le127/8),\qquad
|R'(\nu)|\le10^6|\nu|^{23}/8^{19}\quad(|\nu|\ge127/8).
\tag{10}
\]

For the overlap in the second estimate, extend the first polynomial bound
in (9) down to \(|\nu|\ge63/4\): on \([63/4,16]\) it exceeds the
core bound. The Cauchy disk at \(127/8\) is then fully covered. Its
polynomial enlargement costs at most \((128/127)^{23}<5/4\).

Exact Gaussian moments and (9)--(10) give

\[
\|\psi\|_2\le16k^{-1/4},\qquad
2k\|\nu e^{-k\nu^2}R\|_2\le16k^{1/4},\qquad
\|e^{-k\nu^2}R'\|_2\le128k^{-1/4}.
\tag{11}
\]

For completeness the squared core coefficients, after extracting the
indicated powers of \(k\), are

\[
A^2=169\sqrt{\pi/2}+52/\sqrt k+
                       8\sqrt\pi/(2^{3/2}k),
\]
\[
B^2=4[169\sqrt\pi/(2\cdot2^{3/2})+26/\sqrt k+
                       12\sqrt\pi/(2^{5/2}k)],
\]
\[
C^2=11664\sqrt{\pi/2}+3456/\sqrt k+
                       512\sqrt\pi/(2^{3/2}k).
\]

They are below \(16^2,16^2,128^2\) for \(k\ge8\), with room for
tails below \(10^{-6}\) of the squared scales. The companion checker
uses rational bounds \(\sqrt\pi<71/40\), \(\sqrt2>141/100\),
\(\sqrt8>14/5\), and decreasing monomial/Gaussian bounds.

With the Fourier convention of the opening note, weighted
Cauchy--Schwarz and Plancherel give exactly
\(\|q\|_1\le(\|\psi\|_2\|\psi'\|_2)^{1/2}\).
From (11),

\[
M_{b,t}(k)\le\sqrt{16(16+128/\sqrt8)}<32.
\tag{12}
\]

## Physical amplitude and the restored-pole coefficient

For the zero-extended base polynomial,

\[
a_0=\frac{1073741824}{9917826435},\qquad
\frac{13}{40}<\sqrt{a_0}<\frac13,
\quad \|h'\|_\infty<11,\quad
\|h''\|_\infty\le256,\quad \|h'''\|_\infty<8192.
\]

To check the derivative bounds put \(u=4v\). Then
\(h'=-64u(1-u^2)^7\),
\(h''=-256(1-u^2)^6(1-15u^2)\), and
\(h'''=43008u(1-u^2)^5(1-5u^2)\).
The first maximum squared is \(4096(14/15)^{14}/15<121\).
For the second, the nontrivial maximum of
\((1-z)^6(15z-1)\) is \(2(4/5)^6<1\).
For the third, split \(z=u^2\) at \(1/5\); the squared majorants
are \((10/11)^{10}/11\) and
\(25(3/13)^3(10/13)^{10}\), each below \((4/21)^2\).

The exact demodulated amplitude from the opening note therefore obeys

\[
\sup|A_t|\le\frac{40}{13}
\left[\frac{40001}{40000}
+11\left(\frac3{100}+\frac1{4000000}\right)
+\frac{3\cdot256}{10000}+\frac{8192}{1000000}\right]
=\frac{5660079}{1300000}.
\]

Multiplication by the physical factor costs \(e^{1/8}<8/7\), and
shell integration costs \(3/2\). Hence
\(M_h\le16980237/2275000\), and
\(CM_h/q<33/4\), using \(C=2e^{1/4}<18/7\).
This proves the baseline in the table without PNT.

For the pole, use an exact endpoint polynomial rather than the cruder
nineteenth-power bound. Set \(c_0=8^8\,8!=676457349120\) and

\[
Q(z)=z^8+144z^7+10080z^6+443520z^5+13305600z^4
+276756480z^3+3874590720z^2+33210777600z+132843110400.
\]

Repeated integration by parts gives exactly

\[
H(z)=c_0z^{-17}[e^{z/4}Q(-z)-e^{-z/4}Q(z)].
\tag{13}
\]

Let \(M_\pm(y)=|Q(\pm1/2+i\sqrt y)|^2\), polynomials in \(y\).
Every coefficient of \(M_-\) is positive and its leading coefficient
is one. Every coefficient of
\((51/50)^2M_-(10000+w)-M_+(10000+w)\) is strictly positive.
The exact coefficients are recorded in the companion rational certificate.
Consequently, for \(T\ge100\),
\(|Q(-1/2+it)|\ge T^8\) and
\(|Q(1/2+it)|<(51/50)|Q(-1/2+it)|\).

The reverse triangle inequality in (13),
\(e^{-1/8}>7/8\), \(e^{1/4}>5/4\), and
\((1+1/40000)^9<1001/1000\) imply

\[
|H(-1/2+it)|>\frac{c_0}{5T^9}.
\]

Finally \(N_t<(37/100)T^3\),
\(|K(1-it)|\ge7/\sqrt{T^2+9}>7000/(1001T)\), and the exact
opening identity \(D_t'(1)=-H(-1/2+it)K(1-it)/(2qN_t)\) give

\[
|D_t'(1)|^{-1}<\frac{37037}{30000c_0}T^{13}
                         <\frac{T^{13}}{5\cdot10^{11}}.
\tag{14}
\]

## Effective counts, including closed guard endpoints

Use [Bellotti--Wong, arXiv:2412.15470v2, Theorem 1.1](https://arxiv.org/html/2412.15470v2).
For \(u\ge e\), their two simultaneous zero-count bounds give
\(|\mathcal N(u)-\mathcal M(u)|\le\mathcal E(u)\), where
\(\mathcal N\) counts positive-ordinate nontrivial zeros with
multiplicity, and

\[
\mathcal M(u)=\frac{u}{2\pi}\log\frac{u}{2\pi e},
\]
\[
\mathcal E(u)=\min\{0.10076\log u+0.24460\log\log u+8.08344,
                    0.11200\log u+0.12567\log\log u+3.77417\}.
\tag{15}
\]

All decimal constants here are exact inputs from version two. Distinguish
the published count \(\mathcal N\) from the integer sample allowance \(N\).
For \(T\ge100\), the total multiplicity in \(|\gamma-t|\le3\)
is at most

\[
\mathcal Q(T)=\mathcal M(T+3)-\mathcal M(T-3)
                       +\mathcal E(T+3)+\mathcal E(T-3).
\tag{16}
\]

Use \(\mathcal N((T-3)^-)\) at the lower endpoint. The bounds survive
that limit by continuity; negative carriers follow by conjugation. Thus
no boundary zero is discarded.

A global unit-count constant \(C_0=12\) follows from (15). First,
\(\mathcal M(5)+\mathcal E_2(5)<4\), so \(\mathcal N(5)\le3\).
There are no real nontrivial zeros, as the alternating eta-series is
positive on the real interval \((0,1)\), where zeta is negative.
Any interval contained in \([-5,5]\) therefore contains at most six
zeros, less than \(12\log2\).
For \(v\ge4\), (15) bounds the unit count by

\[
\frac{\log(v+1)}{2\pi}+0.224\log(v+1)
       +0.25134\log\log(v+1)+7.54834
<\log(v+2)+7.54834<12\log(v+2).
\]

For \(v\le-5\), reflect to \(-v-1\ge4\), taking endpoint limits.
The remaining intervals lie in \([-5,5]\). Multiplicities are retained.

There is also a useful lower bound on the expression \(\mathcal Q\):

\[
\mathcal Q(T)\ge(3/\pi+0.20152)\log(T-3)
                 +7.54834-(3/\pi)\log(2\pi)
>\log(T-3)+5>\log(T+6).
\tag{17}
\]

Here \(\mathcal E(u)\ge0.10076\log u+3.77417\) for \(u\ge97\),
and \(\log(T+6)-\log(T-3)\le9/97<0.1\).
This is a lower bound on our chosen upper-count expression; it does not
assert a lower bound for the actual cluster size.

Choose throughout

\[
N\ge\max(10,\lceil\mathcal Q(T)\rceil),\qquad
\eta_N=(8e)^{-N}.
\tag{18}
\]

For the opening parameters \(a=20\), \(\delta=1/16\), \(R=3\),
\(h=4\), \(m=N\), the zero-side left and remote errors are now
bounded by

\[
N e^{-(319/64)(N+1)}<\eta_N/16,
\qquad 72N e^{-(63/4)(N+1)}<\eta_N/16.
\tag{19}
\]

For the second, the global constant gives
\(2C_0 B_R(k)\le72\log(T+6)<72N\).
Both inequalities hold for all integers \(N\ge1\): use
\(\log(8e)<4\), \(Ne^{-N/2}<1\),
\(319/64>9/2\), and \(72e^{-63/4}<1/16\).
The Kolesnik--Straus argument from the opening note therefore still
forces, at one sample,

\[
|\mathcal Z_{b,t}(k,20k)|\ge\eta_N/2,
\quad k=4(N+1),4(N+2),\ldots,8N.
\tag{20}
\]

## Every omitted physical budget is below its allowance

Choose \(L_-=14k\), \(L_+=6k\), so \(J_k=[6k,26k]\).
The exact sufficient budgets in the opening note now satisfy

\[
E_{\rm early}\le\frac{528}{7}\frac{1+6k}{\sqrt k}
                              e^{-279k/256},
\tag{21}
\]
\[
E_{\rm late}\le\frac{33}{2\sqrt k}
  \left[\frac49(1+26k)+\frac{16}{81}\right]e^{-9k/4},
\tag{22}
\]
\[
E_{\rm pole}\le e^{-k(T^2-81/16)}
 \left[1+\frac{33T^{13}}{20\cdot10^{11}}
                          (26k+1/4+338k^2)\right],
\tag{23}
\]

and \(E_{-1}\) retains its exact opening bound.
The contour position \(c=13/4\) gives the late exponent
\(5+25/4-(9/4)6=-9/4\). The earlier choice \(c=5/4\)
paid for the same physical growth with a much wider late interval.

Each of the four budgets is strictly below \(\eta_N/16\) for
every \(N\ge10\) and every sample in (20). Here is an analytic check
covering the full range, rather than a sampled numerical test.

For the early budget enlarge \(1+6k\) to \(1+20k\).
Its logarithmic derivative in \(k\) is below
\(1/(2k)-279/256<0\), so \(k=4(N+1)\) is worst.
The logarithm of its ratio to \(\eta_N/16\) has derivative in \(N\)
below \(1/[2(N+1)]+31/10-279/64<0\).
At \(N=10,k=44\), its prefactor including sixteen is below \(e^{13}\),
while \(N\log(8e)<31\) and
\((279/256)44=3069/64>44\). Thus the ratio is below one.
The rational checker also encloses the sharper actual logarithmic ratio.

The late bound is weaker than \(400\sqrt k e^{-9k/4}\).
It decreases in \(k\), and the logarithm of its ratio at the least
sample has derivative below \(1/[2(N+1)]+31/10-9<0\).
At \(N=10,k=44\), \(6400\sqrt{44}<44800<e^{12}\),
so that ratio is below \(e^{12+31-99}<1\).

For the pole, its bracket is at most \(2T^{13}k^2\).
Use \(13\log T\le T^2/4\) for \(T\ge100\) and \(k^2\le e^k\)
for the sampled \(k\ge44\). Then
\(E_{\rm pole}\le2e^{-7493k}<\eta_N/16\).
This retains the exact known total moment and finite-prefix bound;
no unevaluated quantitative PNT norm has been introduced.

Finally (17)--(18) imply \(\log(1+T)<N\) and \(\eta_N>e^{-k}\).
The bracket of \(E_{-1}\) is below \(1+k\), so

\[
E_{-1}/\eta_N<(1+k)e^{-495k/16}
                          \le e^{-479k/16}<1/16.
\tag{24}
\]

All fixed-line, physical, and pole errors thus sum to less than
\(\eta_N/4\). PNT remains the established convergence input for the
total moment; the arithmetic cancellation hypothesis is a separate input.

## The explicit conditional detector and its actual cost

For a candidate box \(3/4\le\beta<1\),
\(|\gamma-t_0|\le\Delta\), cover every carrier in that ordinate band,
all with \(|t|\ge100\). Choose one integer \(N\ge10\) that exceeds
\(\mathcal Q(|t|)\) throughout the band. The function \(\mathcal Q\)
is increasing for \(T\ge100\), so its upper endpoint suffices.
Explicitly use the maximum magnitude
\(T_{\max}=\max(|t_0-\Delta|,|t_0+\Delta|)\), including negative
carrier bands, when choosing \(N\).
If the full prepared scalar satisfies

\[
\boxed{\sup_{y\in[24(N+1),208N]}
             e^{y/4}|\lambda_t(e^y)|\le\frac{(8e)^{-N}}{256}
\quad\text{for every covered carrier }t,}
\tag{25}
\]

the box contains no zero. Indeed the observed convolution is at most
\(32\eta_N/256=\eta_N/8\), the remainders sum to less than
\(\eta_N/4\), and the resulting \(3\eta_N/8\) contradicts (20).
This is a proved implication with an unproved arithmetic hypothesis.
It concerns a continuous physical interval and the exact complex scalar,
including prime powers and preparation, not finitely many prime samples.

The rational replay record gives these illustrative choices:

| Carrier magnitude \(T\) | \(\mathcal Q(T)\), approximate | \(N\) | Cover in \(y=\log X\) |
|---|---:|---:|---|
| \(100\) | \(11.60604\) | \(12\) | \([312,2496]\) |
| \(10^6\) | \(22.74078\) | \(23\) | \([576,4784]\) |
| \(3\cdot10^{12}\) | \(40.50750\) | \(41\) | \([1008,8528]\) |
| \(10^{20}\) | \(61.04759\) | \(62\) | \([1512,12896]\) |

The exact outward enclosures in the record decide each ceiling.
At \(T=3\cdot10^{12}\), the opening interval formula at the same \(N\) gives
\([672,15088]\); the new upper prime scale is still \(e^{8528}\).
These are detector costs under a hypothetical off-line zero, not examples
of new exclusions or proposed direct prime enumeration.

## What to pursue next

The next substantive gate is the arithmetic reduction of (25) over its
actual carrier and scale ranges. The Gaussian analysis now supplies
effective constants and an explicit target, so further kernel sharpening
should be judged by how much it eases that arithmetic inequality.

A bounded parameter optimization is also worthwhile before a large
arithmetic computation. The trial \(a=8\), \(\delta=1/4\), \(R=2\),
\(m=4N\), \(h=3/2\) balances the left and remote gaps at \(31/16\)
and gives a power-sum loss \((20e)^{-N}\), with a smaller guard count.
It should be run through the complete finite-height budgets rather than
promoted from its spectral exponents alone. This continuation retains
the original spectral parameters to keep the present milestone auditable.

One useful simplification is to include every zero inside the ordinate
guard in the power-sum cluster. The present count already charges all of
them, so excluding nearby left zeros brings no count saving at this stage.
A better count for zeros in the right part of the strip would be needed
before that split lowers the loss. Both options should be compared against
the complete arithmetic cost and established zero-free inputs.

The [replay source and small record](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
verify rational normalization, endpoint-polynomial positivity, Gaussian
moment majorants, elementary-function enclosures, and example count ceilings.
The all-height deductions are the analytic proofs above, not an inference
from the four examples. The [internal review](../../../reviews/height_adapted_zero_detection/gaussian_localization/EXPLICIT_CONSTANTS_REVIEW_20261004.md)
records the corrections and scope. No large arrays or third-party PDFs are
saved, and no manuscript snapshot is created.
