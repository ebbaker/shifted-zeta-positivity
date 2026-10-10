# Paid genuine-theta stationary signs on two bounded rectangles

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is not exposed to this session
and is not inferred. The derivations, outward replays and parallel reviews
are internal LLM work, not independent mathematical validation.

The [two-sign criterion](5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md)
now has a nonvacuous bounded calibration of each sign on the actual theta
flow. They occur in different rectangles:

| Domain | Complete input | Nonempty stationary set and paid sign | Other stationary set |
| --- | --- | --- | --- |
| N=22066 shrinking-time cell | Imported complete holomorphic disk plus regenerated complete finite sum | One physical Hx zero per time; HHxx/normalizer² < -90.3133241620 | Hxx has no zeros |
| 0≤t≤0.05, 8≤x≤12 | Direct full theta integral with every omitted term and integral tail paid | One physical Hxx zero per time; HxHxxx < -3.78300454912e-7 | Hx has no zeros |

These are calibrations of the sufficient conditions, not extra collision
coverage: the first jet already excludes joint zeros on both rectangles.
Neither a uniform stationary sign nor the predecessor neighborhoods needed
for a global application has been proved. The high cell is conditional on
the imported disk interface; the low rectangle does not use that interface.

## 1. Physical signs on the shrinking-time cell

Put N=22066, t0=1/(2 log N), x0=4πN² and consider the full closed rectangle

\[
 t_0\le t\le t_0+8\cdot10^{-6},\qquad
 x_0+0.3\le x\le x_0+0.7.
\tag{1}
\]

The natural divisor cutoff is N throughout. Write H=𝒩Q, where 𝒩=A_t>0
is the manuscript's real normalizer, not the chord readout A=2H. With
λ=(log 𝒩)x, the exact physical jets Kj=Hj/𝒩 are

\[
 K_0=Q,\quad K_1=Q'+\lambda Q,
\]
\[
 K_2=Q''+2\lambda Q'+(\lambda^2+\lambda_x)Q,
\]
\[
 K_3=Q'''+3\lambda Q''+3(\lambda^2+\lambda_x)Q'
 +(\lambda^3+3\lambda\lambda_x+\lambda_{xx})Q.
\tag{2}
\]

For s=(1-ix)/2 and the manuscript's α,

\[
 \lambda=\tfrac12\Im\{\alpha(1+t\alpha'/2)\},
\]
\[
 \lambda_x=-\tfrac14\Re\{\alpha'+(t/2)[(\alpha')^2+\alpha\alpha'']\},
\]
\[
 \lambda_{xx}=-\tfrac18\Im\{\alpha''+(t/2)[3\alpha'\alpha''+
 \alpha\alpha''']\}.
\tag{3}
\]

The outward λ interval is near -0.392699081392283. Symmetric enclosures
|λx|≤4.085855e-11 and |λxx|≤6.677684e-21 pay the remaining channels.
The candidate condition is K1=0, never Q'=0 or F'=0.

Eighty complete height subcells of width 0.005, each retaining the whole
time interval, give

\[
 -65.043341<K_2<-13.004812,
 \qquad K_1(x_0+0.3)>12.7522169,
 \qquad K_1(x_0+0.7)<-4.8624084.
\tag{4}
\]

Since Hxx=𝒩K2<0, Hx decreases strictly at each fixed time. The endpoint
signs and continuity prove exactly one genuine Hx zero per time. Only
three subcells admit zero in their K1 intervals, so all these critical
points lie in x-x0∈[0.590,0.605]. On that complete candidate band,

\[
 K_0>1.9879895535,\qquad K_2<-45.2890285603,
\]
\[
 \boxed{HH_{xx}/\mathcal N^2<-90.3133241620.}
\tag{5}
\]

Thus S0 is strict on a nonempty physical stationary set. S1 is vacuous
because Hxx never vanishes. The exact frozen-β score dictionary consequently
gives the T0 score product divided by 𝒩² greater than
361.253296648 β². This is the same scalar sign through an exact dictionary,
not a new independent source-overlap theorem.

## 2. High-cell approximation payments through the third jet

The [stationary cell checker](../numerics/check_theta_stationary_cell.py)
regenerates the retained complete N=22066 frequency moments by rerunning
the hash-checked regular calibration. It uses the frozen spatial Taylor
polynomial of degree eleven and the complete absolute twelfth frequency
moment to enclose derivatives through order three.

For γ=(log q)x and χ=(log q)t, the spatial Bell coefficients are

\[
 q_x=\gamma q,\quad q_{xx}=(\gamma^2+\gamma_x)q,
 \quad q_{xxx}=(\gamma^3+3\gamma\gamma_x+\gamma_{xx})q.
\]

Their time derivatives include γt, γxt, γxxt and all multiplications
by χ. The spatial comparison with the frozen frequency
-i log(N/n)/2 includes its full residual, derivative residuals and
exponential growth. Rational bounds

\[
 |\alpha''|\le2/x^2+24/x^3,\qquad
 |\alpha'''|\le8/x^3+144/x^4
\]

pay the small normalizer and drift channels. The mixed third derivative
budget is retained even though the S1 stationary set is empty.

From the imported real-symmetric holomorphic disk, the Q-jet errors are
at most j!Ljη, with η=5 exp(-tL²/16-L/4). Conservative outward upper
shortenings of their complete hulls through j=3 are

    [0.009641459, 0.192863754, 7.715933530, 463.039030961].

Applying the complete triangular dictionary (2) gives physical Hj/𝒩
error costs at most

    [0.009641459, 0.196649946, 7.868895202, 472.218960911].

The finite transport errors for Re Σq and its first three derivatives
are at most

    [0.017606839, 0.017544256, 0.032493481, 0.082046843],

and are doubled for F=2 Re Σq. Taylor remainders are paid separately for
each derivative and subcell. All stated products use paid physical jets.
The [record](../numerics/THETA_STATIONARY_CELL_RECORD_20261010.json)
contains source hashes, normalizer channels, transport costs, all eighty
subcells, complete Cauchy costs and the three candidate subcells.

The approximately 472 third-jet error is a real limitation of this
interface. Finer spatial subdivision cannot remove a fixed Cauchy cost.
A nonvacuous huge-height S1 test must improve the complete remainder,
use a stronger signed estimate or choose an appropriate physical region.

## 3. Direct full-theta second stationary sign

On the closed physical rectangle

\[
 0\le t\le0.05,\qquad 8\le x\le12,
\tag{6}
\]

the [direct theta checker](../numerics/check_theta_stationary_low_height.py)
integrates the physical half-line derivatives themselves:

\[
 H_x=-\int_0^\infty u e^{tu^2}\Phi(u)\sin(xu)\,du,
\]
\[
 H_{xx}=-\int_0^\infty u^2 e^{tu^2}\Phi(u)\cos(xu)\,du,
 \quad
 H_{xxx}=\int_0^\infty u^3 e^{tu^2}\Phi(u)\sin(xu)\,du.
\tag{7}
\]

Every parameter point is covered by complete intervals, not sampled
midpoint signs. The outward whole-rectangle hulls give

\[
 -0.004248758920<H_x<-0.003823911011,
\]
\[
 0.00006360493465<H_{xxx}<0.00010664729466.
\tag{8}
\]

At x=8 the paid Hxx upper endpoint is less than -0.0001447758850;
at x=12 its lower endpoint exceeds 0.0001964016309. Since Hxxx>0,
Hxx increases strictly and has exactly one zero per time. Its complete
candidate band is x∈[9.4,9.6], comprising four height subcells. On it,

\[
 \boxed{-4.17828941255\cdot10^{-7}<H_xH_{xxx}
 <-3.78300454912\cdot10^{-7}.}
\tag{9}
\]

S1 is consequently strict and nonvacuous. S0 is vacuous because Hx<0.
No finite-arithmetic approximation disk or normalizer is used in this
direct source calculation.

The stronger whole-rectangle consequence is

\[
 \mathscr L_1(H)=H_{xx}^2-H_xH_{xxx}
 \ge -H_xH_{xxx}>2.43219610004\cdot10^{-7}.
\tag{10}
\]

The [complete kernel dictionary](7_COMPLETE_LAGUERRE_KERNELS_AND_TRIPLE_ZERO_LIMIT_20261010.md)
identifies this with J1's Fourier transform at frequency 2x. Thus the
genuine theta response is positive on frequencies 16–24, throughout (6),
despite the negative genuine source value J1,t(0.3)<0 on the same time
interval. These compatible facts demonstrate why the missing condition
is a Fourier correlation rather than pointwise source positivity. No
global positive-definiteness conclusion follows.

## 4. Direct integration and complete tail payment

The default run uses 2,048 outward u intervals on [0,1] and eighty
height intervals on [8,12]. Every density evaluation retains the full
time interval. Terms n=1,2,3 of Φ are evaluated directly, and each cell
includes a positive enclosure of every n≥4 term. For m=2,4,

\[
 \sum_{n\ge4}n^m e^{-\pi n^2e^{4u}}
 \le\frac{4^m e^{-16\pi e^{4u}}}
 {1-(5/4)^m e^{-9\pi e^{4u}}}.
\tag{11}
\]

The denominator is outward-proved positive. All true theta summands are
positive for u≥0, so adding the interval [0,tail upper bound] is valid.

For each height interval, cell-center sin/cos phases advance by outward
interval rotations. The initial phase and increment use rigorous Taylor
enclosures from the retained interval core. Padding by the outward maximum
of |xu-center phase| encloses every true phase within the complete x/u
rectangle, since sine and cosine have derivative magnitude at most one.
Integration uses the full cell ranges times their widths; there is no
unproved numerical quadrature remainder.

The full-source Gaussian envelope for u≥0 is

\[
 \Phi(u)\le C e^{-8\pi u^2},\qquad C=4\pi^2e^{-\pi}.
\tag{12}
\]

Drop the negative polynomial part, use n4≤16^(n-1) and n²-1≥3(n-1),
and sum the geometric ratio 16 exp(-3π)<1/2. Then e4u≥1+4u+8u²
and 4π>9 prove (12). Put a=8π-0.05 and R=1. The absolute u>R
errors for physical jets one, two and three are paid by

\[
 E_1=Ce^{-aR^2}/(2a),\quad
 E_2=Ce^{-aR^2}[R/(2a)+1/(4a^2R)],
\]
\[
 E_3=Ce^{-aR^2}[R^2/(2a)+1/(2a^2)].
\tag{13}
\]

The odd moments are exact Gaussian integrals; the even estimate uses
integration by parts and the Gaussian Mills bound. Errors enter
symmetrically because the oscillatory tail sign is not assumed.

The [low-height record](../numerics/THETA_STATIONARY_LOW_HEIGHT_RECORD_20261010.json)
binds the checker hash, two retained interval source hashes, full
omitted-source and integral-tail payments, all subcells, endpoint signs
and stationary candidate band. All sign arithmetic uses 60-digit directed
Decimal intervals with corrected integer powers.

## 5. Limits and the next target

These proofs certify the desired physical signs on two bounded rectangles;
they neither establish a uniform theorem nor improve the existing joint-zero
coverage there. At the lower time boundaries no quantitative earlier-time
buffer is supplied. Direct first-jet exclusion covers the closed rectangles;
the stationary-sign theorem can be used only where its open-domain
predecessor hypotheses are met.

The next substantive target is a uniform conditional Fourier estimate for
the complete J0 and J1 kernels, or their stronger positive-definiteness
property, using the genuine theta structure. It must cover predecessor
neighborhoods and pay approximation/cutoff costs. The first Laguerre sign
alone is locally blind to every exact triple, and a positive second source
does not automatically propagate the first sign to earlier times; the
exact limitations and signed kernel calculations are in Note 7.

All new checkers write records only when an explicit `--record` path is
provided. Replaying into a temporary path therefore leaves the retained
records intact. Mathematical sign conclusions come from the outward
calculations; a matching source hash establishes identity of the input
implementation, not independent proof or cross-platform arithmetic identity.
