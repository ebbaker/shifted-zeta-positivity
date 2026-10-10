# Asymmetric derivative cores and complete joint probes

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model audits are internal checks, not independent validation.

This continues the actual-phase estimates of
[Heat Note 9](9_GENUINE_SIGNED_EDGE_CANCELLATION_AND_AVERAGED_PROBES_20261009.md)
and the [local-input review](../../reviews/HEAT_GENUINE_SIGNED_INPUT_REVIEW_20261009.md).
The derivative coordinate admits a larger signed cutoff removal than the
value coordinate. Its complete mean square also has a shorter sufficient
averaging range, obtained from a weighted Hilbert estimate. Neither result
settles the remaining local joint lower bound. The accompanying
[threshold-jet test](12_THRESHOLD_COLLISION_JETS_AND_PAID_LAGUERRE_TEST_20261009.md)
adds an all-real-threshold constraint with a paid fourth-derivative interface.

Use the same exact scaling throughout:

\[
1\le\kappa\le2,\quad 0<t\le1/20,\quad L=\kappa/t,\quad
x=4\pi e^L,\quad N=\lfloor\sqrt{e^L+t/16}\rfloor,
\]
\[
\mathfrak a=\kappa(4-\kappa)/16,\quad
\mathfrak b=\kappa(\kappa+4)/16,\quad s_\kappa=1/2+\kappa/8.
\]

Let \(Q_t=H_t/A_t\), with the manuscript's symmetric analytic normalizer,
and \(F_{t,M}\) its genuine approximant at a fixed cutoff \(M\).
All spatial derivatives hold both time and that integer cutoff fixed.
The center quantity \(L\), when used as a derivative-coordinate scale,
is also held fixed. The inherited disk payment is

\[
\eta_N\le5e^{-\mathfrak b/t},\qquad
|Q_t^{(j)}(x)-F_{t,N}^{(j)}(x)|\le j!L^j\eta_N
\quad(j\ge0).
\]

This is the full reflected, normalized, cutoff-corrected complex-disk
payment from [Note 8](8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md).
It does not replace an actual signed tail by its absolute coefficient mass.

## 1. A wider signed edge for the derivative coordinate

Retain the exact coefficients, normalizer, and fixed-cutoff approximant from
Note 9. In particular, write

\[
q_n(x)=w_n(x)e^{i\phi_n(x)},\qquad
F_{t,N}(x)=2\Re\sum_{n\le N}q_n(x),\qquad
s_\kappa=\frac12+\frac\kappa8.
\]

All derivatives below hold time and the integer cutoffs fixed. At the
parameter point under consideration, put

\[
H_{e,v}=\lfloor N^{3/4}\rfloor,\quad K_v=N-H_{e,v},\qquad
H_{e,d}=\lfloor N^{7/8}\rfloor,\quad K_d=N-H_{e,d}.
\]

The wider edge has the explicit derivative payment

\[
\left|\sum_{K_d<n\le N}w_nz_ne^{i\phi_n}\right|
\le\frac{800}{L}N^{-1/24},\qquad
|F_{t,N}'-F_{t,K_d}'|\le400N^{-1/24}.                 \tag{A1}
\]

The value payment is still taken from the shorter edge in Note 9.
Consequently the mixed pair

\[
\mathcal W=
\left(\frac{F_{t,K_v}}2,\frac{2F_{t,K_d}'}L\right)
\]

has, at every genuine collision, the necessary bounds

\[
|\mathcal W_1|\le\eta_N/2+40N^{-1/24},\qquad
|\mathcal W_2|\le2\eta_N+\frac{800}{L}N^{-1/24}.       \tag{A2}
\]

This is a pair of two specified observables with different cutoffs; its
second coordinate is not the derivative of its first coordinate. The same
complete analytic error \(\eta_N\le5e^{-\mathfrak b/t}\) is paid before
the exact signed term subtraction. A positive error estimate for a new
natural cutoff is not substituted for that subtraction.

### Explicit proof of the wider derivative payment

Since \(N\ge22000>(10/3)^8\),
\(H_{e,d}\le.3N\) and \(K_d\ge.7N\). With
\(T=(x-t\alpha_i)/2\) and \(f(u)=T\log u/(2\pi)\),

\[
\frac1N\le f'''(u)=\frac{T}{\pi u^3}\le\frac6N,
\qquad K_d\le u\le N.                              \tag{A3}
\]

The lower estimate follows from \(T/\pi\ge N^2\); the upper one uses
\(T/\pi\le2.01N^2\) and \(2.01/.7^3<6\).
The phase is real and smooth on this interval. We apply the
[explicit derivative theorem of Arias de Reyna, equation (2)](https://arxiv.org/html/2407.02094v1)
with derivative order three, \(\lambda=1/N\), and \(\Lambda=6/N\).
Its hypotheses require \(\lfloor Y\rfloor>3\) on an interval of length
\(Y\), and positivity of the indicated derivative. Every such partial
interval in the edge has \(Y\le H_{e,d}\). The theorem gives

\[
\left|\sum e(f(n))\right|
\le11\max\{6^{1/4}N^{21/32},\,
             36^{1/6}N^{17/24},\,N^{15/32}\}
\le20N^{17/24}.                                    \tag{A4}
\]

Partial intervals with at most three terms satisfy the same estimate
trivially. The exact scalar reserves are
\(6\cdot11^4<20^4\), \(36\cdot11^6<20^6\), and \(11<20\);
both other powers of \(N\) are below \(17/24\).
Thus (A4) bounds every partial sum needed in Abel summation.

The endpoint bounds proved in Note 9 remain valid:

\[
w_N\le1.01N^{-s_\kappa},\quad |z_N|\le\frac6{LN},
\qquad |z'(u)|\le\frac3{Lu}.                        \tag{A5}
\]

Here the prime on \(z(u)\) in (A5) means differentiation in the continuous
index \(u\), not a spatial derivative. On \([.7N,N]\), the logarithmic
slope of \(w(u)\) is negative with modulus less than one: explicitly it is

\[
\frac{d\log w}{d\log u}
=\frac t2\log u-\frac12-\frac{t\alpha_r}2,
\]

and lies between \(-.511\) and \(-.499\), using
\(|\log N-L/2|\le2/N\), \(|\alpha_r-L/2|\le x^{-2}\),
\(t\le1/20\), and \(|\log .7|<.4\).
In particular \(w\) decreases and
\(w_{K_d}\le(10/7)w_N\le2N^{-s_\kappa}\).
The exact variation estimates are therefore

\[
\operatorname{TV}(z)\le\frac{30}{7}\frac{H_{e,d}}{LN}
<\frac{5H_{e,d}}{LN},\qquad
\sup|z|\le\frac{11H_{e,d}}{LN},
\]
\[
|w_Nz_N|+\operatorname{TV}(wz)
\le(6.06+32H_{e,d})\frac{N^{-s_\kappa}}{LN}
\le40\frac{H_{e,d}N^{-s_\kappa}}{LN}.                  \tag{A6}
\]

For the product estimate use
\(\operatorname{TV}(wz)\le w_{K_d}\operatorname{TV}(z)
+\sup|z|\operatorname{TV}(w)\), with
\(\operatorname{TV}(w)\le2N^{-s_\kappa}\).
Abel summation with (A4)--(A6) gives

\[
\left|\sum_{K_d<n\le N}w_nz_ne^{i\phi_n}\right|
\le\frac{800}{L}N^{17/24+7/8-1-s_\kappa}
=\frac{800}{L}N^{7/12-s_\kappa}
\le\frac{800}{L}N^{-1/24}.
\]

The exact identity \(2F_{t,N}'/L=\Im\sum_{n\le N}w_nz_ne^{i\phi_n}\)
converts this to (A1); the complete approximation and Note 9 give (A2).
No arbitrary replacement phases have been introduced.

## 2. Higher derivative orders and the limit of this estimate

Consider a fixed derivative order \(d\ge3\), a fixed exponent
\(0<\beta<1\), and an edge of length \(H=\lfloor N^\beta\rfloor\).
For the actual logarithmic phase,

\[
f^{(d)}(u)=(-1)^{d-1}\frac{(d-1)!T}{2\pi u^d}
\asymp_d N^{2-d}.
\]

For even \(d\), apply the source theorem to \(-f\); conjugation preserves
the sum's modulus. On an endpoint edge \(u\asymp N\), its positive
derivative bounds have bounded ratio for each fixed \(d\). Write

\[
A_d^{\rm pow}=2^{1-d},\qquad
B_d^{\rm pow}=\frac{d-2}{2^d-2}.
\]

These names denote exponents, not the constants called \(A_d,B_d\) in
the source theorem. Multiplying its three mean-value terms by interval
length gives the partial-sum exponent

\[
v_d(\beta)=\max\left\{
\beta(1-A_d^{\rm pow}),\quad
\beta-B_d^{\rm pow},\quad
\beta(1-dA_d^{\rm pow})+(d-2)A_d^{\rm pow}
\right\}.                                         \tag{A7}
\]

All three powers of interval length are nonnegative, so the same bound
holds for every partial interval; intervals too short for the theorem
are bounded trivially. Decreasing-weight Abel summation gives a value
tail \(O_d(N^{v_d(\beta)-s_\kappa})\).

For \(d=3\), all three terms give decay precisely under
\(\beta< s_\kappa+1/6\); throughout the present range this is the
smallest of the three strict thresholds. Hence the uniform value-edge
threshold supplied by this bound is \(\beta<19/24\).
For every \(d\ge4\), the first term alone requires

\[
\beta<\frac{s_\kappa}{1-A_d^{\rm pow}},\qquad
A_d^{\rm pow}\le1/8.
\]

At \(\kappa=1\) this caps the uniform threshold by
\((5/8)/(7/8)=5/7<19/24\). Thus order three is optimal for uniform
value-edge removal within this explicit derivative-bound and Abel
calculation. Raising the derivative order in that calculation cannot
improve the retained value core.

There is also a macroscopic-block deficit. On a fixed-proportion
endpoint block \([cN,N]\), \(0<c<1\), put \(\beta=1\) in (A7).
Then \(v_3(1)=5/6\), while every fixed \(d\ge4\) has
\(v_d(1)\ge7/8\). Even the best displayed weighted exponent is
\(5/6-s_\kappa\ge1/12>0\). Splitting that block into
\(N^{1-\beta}\) intervals and adding these upper bounds does not repair
the deficit: its aggregate exponent includes \(1-B_d^{\rm pow}\),
equal to \(5/6\) for \(d=3\), and includes
\(1-\beta A_d^{\rm pow}\ge7/8\) for \(d\ge4\).
This conclusion concerns those bounds and that triangle aggregation;
it is not a lower bound on the genuine signed sum and does not rule out
a different transformation that retains correlations between blocks.

## 3. Exact fixed-time raw jets on both edges

The raw derivative multipliers can be controlled without differentiating
the scale \(x=4\pi e^{\kappa/t}\), the edge length, or an integer cutoff.
For the exact summand define

\[
v_n=\frac{q_n'}{q_n}
=-\frac{tV\log n}{4}-i\frac{Lr_n}{4}.
                                                               \tag{A8}
\]

This follows from \((\log w_n)'=-tV\log n/4\) and
\(\phi_n'=-Lr_n/4\); the displayed \(Lr_n/4\) is shorthand for the
unscaled exact expression
\(\frac12\Re\{(\alpha-\log n)(1+t\alpha'/2)\}\).
Thus it is differentiated with fixed \(t,n\), not by holding a scaling
parameter fixed. Put \(h=H/N\) on either endpoint edge.
The endpoint estimate and the real-axis formulas for \(\alpha\) give

\[
\sup|v_n|+\operatorname{TV}_n(v_n)=O(h),\qquad
\sup|\partial_x^k v_n|=O_k(N^{-2k}),\qquad
\operatorname{TV}_n(\partial_x^k v_n)=O_k(hN^{-2k})
\quad(k\ge1).                                      \tag{A9}
\]

The constants are uniform in \(t,\kappa\) in the stated range.
Here \(\operatorname{TV}_n\) is total variation of the continuous
index interpolation with \(x,t\) fixed. To verify the higher estimates,
\(\partial_x^k\alpha_r=O_k(x^{-k})\),
\(\partial_x^k\alpha_i=O_k(x^{-k-1})\),
\(\partial_x^k U=O_k(x^{-k-2})\), and
\(\partial_x^k V=O_k(x^{-k-1})\).
The factors \(t\log n\) are bounded uniformly.
Each \(\partial_x^k v_n\) is affine in \(\log n\); its varying
coefficient has size at most \(O_k(x^{-k})\) for \(k\ge1\).
Since the logarithmic length of the edge is \(O(h)\) and
\(x\asymp N^2\), these facts prove the corresponding variation
estimates. For \(k=0\), the exact index slope of the phase multiplier
is \(O(1/u)\), which gives the first variation bound in (A9).

Write \(q_n^{(j)}=q_nP_j\), where \(P_j\) is the complete derivative
polynomial in \(v_n,v_n',\ldots\). For the orders needed here,

\[
P_1=v,\qquad P_2=v^2+v',\qquad
P_3=v^3+3vv'+v'',
\]
\[
P_4=v^4+6v^2v'+3(v')^2+4vv''+v'''.                 \tag{A10}
\]

Every monomial has differential weight \(j\), assigning weight
\(k+1\) to \(v^{(k)}\). For fixed \(\beta>0\),
\(N^{-2k}=O(h^{k+1})\) for every \(k\ge1\).
Product variation and (A9) therefore show

\[
\sup|P_j|+\operatorname{TV}_n(P_j)=O_j(h^j),
\qquad
|w_NP_j(N)|+\operatorname{TV}_n(wP_j)
=O_j(N^{-s_\kappa}h^j).                            \tag{A11}
\]

All coefficients in (A10), including the amplitude derivatives, are
included. Applying Abel summation to these exact multipliers yields

\[
|F_{t,N}^{(j)}-F_{t,N-H}^{(j)}|
=O_{d,j}\!\left(N^{v_d(\beta)-s_\kappa+j(\beta-1)}\right).
                                                               \tag{A12}
\]

For the two concrete edges, (A4) and Note 9 specialize this to

\[
|F_{t,N}^{(j)}-F_{t,K_v}^{(j)}|
=O_j(N^{7/12-s_\kappa-j/4}),\qquad
|F_{t,N}^{(j)}-F_{t,K_d}^{(j)}|
=O_j(N^{17/24-s_\kappa-j/8}).                      \tag{A13}
\]

The uniform powers for \(j=2,3,4\) are respectively
\((-13/24,-19/24,-25/24)\) for \(K_v\), and
\((-1/6,-7/24,-5/12)\) for \(K_d\).
The \(j=1\) wider-edge result has the explicit constant in (A1);
the higher-jet constants in (A13) are uniform constants rather than
printed numerical certificates. Complete approximation payments are

\[
|Q_t^{(j)}-F_{t,K}^{(j)}|
\le j!\eta_NL^j+C_jN^{p-s_\kappa+j(\beta-1)},
                                                               \tag{A14}
\]

with \((p,\beta)=(7/12,3/4)\) or \((17/24,7/8)\).
The first term is the complete disk/Cauchy payment at cutoff \(N\),
followed by the exact signed subtraction at fixed cutoffs.

More generally the order-three raw-\(j\) threshold is

\[
\beta<\frac{j+s_\kappa+1/6}{j+1}
=1-\frac{5/6-s_\kappa}{j+1},\qquad
\beta<1-\frac{5}{24(j+1)}\quad\hbox{uniformly}.       \tag{A15}
\]

The middle term of (A7) determines this threshold: the cross-differences
between the other two thresholds and it have numerators
\((2j+6s_\kappa-3)/24>0\) and
\(j/3+3s_\kappa/4-7/24>0\), respectively.
For every fixed \(d\ge4\), the first-term threshold is at most
\((j+s_\kappa)/(j+7/8)\), which is strictly smaller than (A15),
because the cross-difference in the opposite direction is
\((2j-6s_\kappa+7)/48>0\).
This stronger order comparison remains confined to the same imported
derivative estimate and Abel calculation.

## 4. Paying the quadratic jet at the shorter common cutoff

Let \(b=\partial_x\log A_t\), \(b_x=\partial_x^2\log A_t\),
\(\gamma=18b_x+9/x^2\), and define the real jet expression

\[
\mathcal J(f)=2(f^{(3)})^2-3f^{(2)}f^{(4)}
              -\gamma(f^{(2)})^2.
\]

For any real jets with errors \(\Delta_j\ge|q^{(j)}-f^{(j)}|\),
\(j=2,3,4\), exact product expansion gives the paid difference

\[
|\mathcal J(q)-\mathcal J(f)|\le
4|f^{(3)}|\Delta_3+2\Delta_3^2
+3|f^{(2)}|\Delta_4+3|f^{(4)}|\Delta_2+3\Delta_2\Delta_4
+|\gamma|(2|f^{(2)}|\Delta_2+\Delta_2^2).            \tag{A16}
\]

In applications the actual jet sizes in (A16) may be used. An absolute
asymptotic payment is also available. For either retained core and every
fixed \(j\le4\),

\[
|F_{t,N}^{(j)}|+|F_{t,K}^{(j)}|
=O_j(e^{\mathfrak a/t})
=O_j(N^{(4-\kappa)/8}).                            \tag{A17}
\]

For completeness, set \(y=L/2-\log u\). The weighted mass integral
satisfies
\(uw(u)\le C e^{\mathfrak a/t}e^{-y/4}\) for
\(0\le y\le L/2\): its exponent is
\(\mathfrak a/t-y/2+ty^2/4+O(x^{-2})\), and
\(ty^2/4\le\kappa y/8\le y/4\).
The exact raw derivative multiplier has size
\(O_j((1+y)^j)\). Discrete summation is bounded by the same integral
up to a fixed factor and the initial term; the latter has size
\(O_j(L^j)\) and is absorbed by \(e^{\mathfrak a/t}\).
The negligible endpoint displacement beyond \(e^{L/2}\) is also
absorbed. This proves (A17) with uniform constants.

For \(K=K_v\), the largest linear product in (A16) is the
second-derivative tail times an absolute fourth-derivative jet. Its
power is

\[
\frac7{12}-s_\kappa-\frac24+\frac{4-\kappa}{8}
=\frac1{12}-\frac\kappa4\le-\frac16.
\]

The other linear tail products decay faster, the quadratic tail
products decay faster still, and \(\gamma=O(x^{-2})\).
Consequently

\[
\mathcal J(F_{t,N})-\mathcal J(F_{t,K_v})
=O(N^{-1/6})                                      \tag{A18}
\]

uniformly on \(\kappa\in[1,2]\). Including the complete analytic
payments in (A14) preserves (A18) with \(Q_t\) in place of
\(F_{t,N}\): their largest linear products have exponential factor
\(e^{(\mathfrak a-\mathfrak b)/t}
=e^{-\kappa^2/(8t)}\), times a fixed power of \(L\), and hence decay
with a strict reserve relative to \(N^{-1/6}\).

For \(K=K_d\), all the individual tails in (A13) tend to zero, but
the absolute quadratic transfer has leading budget

\[
N^{11/24-\kappa/4};
\]

the other linear products have powers \(1/3-\kappa/4\) and
\(5/24-\kappa/4\). The leading power is positive at \(\kappa=1\).
Thus the wider common cutoff does not supply a uniformly vanishing
quadratic jet payment by (A16)--(A17). It supplies one for each fixed
\(\kappa>11/6\), uniformly on every closed subrange
\([11/6+\varepsilon,2]\). At \(\kappa=11/6\) this budget is only
bounded. This is a limitation of the absolute transfer estimate, not
evidence that the genuine quadratic jet difference grows.

## 5. Complete genuine derivative probes on a shorter averaged range

The following argument strengthens Note 9's sufficient averaging range.
The weighted Montgomery--Vaughan inequality removes its logarithmic loss;
the scaled derivative's endpoint weight gives a further factor \(t^2\).
The final inequalities concern the complete genuine approximant and heat
function. They do not supply a pointwise lower bound or exclude a collision.

Use the scaling and symmetric normalization of Notes 8--9:
\[
1\le\kappa\le2,\qquad L=\kappa/t,\qquad x=4\pi e^L,\qquad
N=\left\lfloor\sqrt{e^L+t/16}\right\rfloor,
\]
\[
\mathfrak a=\kappa(4-\kappa)/16,\qquad
\mathfrak b=\kappa(\kappa+4)/16.
\]
All limits are uniform in \(\kappa\in[1,2]\) as \(t\downarrow0\).
Every spatial derivative holds time and the integer cutoff fixed. In the
coordinates below, **the denominator \(L\) is the fixed center value**;
it is not differentiated or replaced by a translated value.

At the center write \(s=(1-ix)/2\), \(\alpha(s)=A+iB\), and
\(\alpha'(s)=U+iV\). Retain the exact data
\[
w_n=\exp\{t\log^2n/4-(1/2+tA/2)\log n\},\qquad
\phi_n=\theta_t(x)+(x-tB)\log n/2,
\]
\[
c=\tfrac12(1+tU/2),\qquad
\Omega=\tfrac12\Re\{\alpha(s)(1+t\alpha'(s)/2)\},\qquad
\lambda_n=\Omega-c\log n,
\]
\[
r_n=4\lambda_n/L,\qquad c_n=tV\log n/L.
                                                               \tag{DP1}
\]
The same definitions at a translated spatial point, with the fixed
denominator \(L\), give exactly
\[
G_F(y):=\frac{2F_{t,N}'(x+y)}L
=\sum_{n\le N}w_n(x+y)
 \{r_n(x+y)\sin\phi_n(x+y)-c_n(x+y)\cos\phi_n(x+y)\}.
                                                               \tag{DP2}
\]
Here \(Q_t=H_t/A_t\) and \(F_{t,N}\) are the manuscript's genuine
normalized heat function and fixed-cutoff holomorphic approximant.

**Proposition 2.** There are absolute constants \(D,t_0>0\) such that,
for \(0<t<t_0\), put
\[
H_d=Dt^2e^{2\mathfrak a/t},\qquad
G_Q(y)=2Q_t'(x+y)/L.
\]
Then
\[
\frac1{H_d}\int_0^{H_d}G_F(y)^2\,dy\ge\frac14,
\qquad
\frac1{H_d}\int_0^{H_d}G_Q(y)^2\,dy\ge\frac18.
                                                               \tag{DP3}
\]
The corresponding joint energies
\((F_{t,N}(x+y)/2)^2+G_F(y)^2\) and
\((Q_t(x+y)/2)^2+G_Q(y)^2\) inherit these lower bounds because their
additional value-coordinate terms are nonnegative. No coefficient is
omitted from the final expressions.

### Imported weighted Hilbert inequality and the exact frozen coefficients

For distinct real frequencies \(\omega_j\), let
\(\delta_j=\min_{k\ne j}|\omega_j-\omega_k|\). The weighted
Montgomery--Vaughan inequality states
\[
\left|\sum_{j\ne k}
 \frac{z_j\overline{z_k}}{\omega_j-\omega_k}\right|
\le\frac{3\pi}{2}\sum_j\frac{|z_j|^2}{\delta_j}.
                                                               \tag{DP4}
\]
The primary source is
[Montgomery and Vaughan, *Hilbert's Inequality* (1974), Theorem 2,
equation (1.7), and Corollary 2, equation (1.9)](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf).
The distinct-frequency hypothesis and weighted local gaps are essential;
the argument does not import a conjectural sharp weighted constant.
Applying (DP4) at the two endpoints of the integrated exponential sum gives
\[
\left|\frac1H\int_0^H\left|\sum_jz_je^{i\omega_jy}\right|^2\,dy
               -\sum_j|z_j|^2\right|
\le\frac{3\pi}{H}\sum_j\frac{|z_j|^2}{\delta_j}.
                                                               \tag{DP5}
\]
This also follows directly by integrating each off-diagonal exponential:
its numerator is the difference of the two endpoint phase products.

Temporarily omit only \(n=N\), and freeze the exact center data:
\[
g_-(y)=\sum_{n<N}w_n
 \{r_n\sin(\phi_n-\lambda_ny)-c_n\cos(\phi_n-\lambda_ny)\}.
\]
As an exponential sum, its complete reflected frequency set is
\(\{\pm\lambda_n:n<N\}\), with exact coefficients
\[
z_{n,-}=\frac{w_n}{2}e^{i\phi_n}(-c_n-ir_n),\qquad
\omega_{n,-}=-\lambda_n,
\]
\[
z_{n,+}=\overline{z_{n,-}},\qquad
\omega_{n,+}=\lambda_n.
                                                               \tag{DP6}
\]
Consequently the exact diagonal is
\[
\sum_{n<N}\bigl(|z_{n,-}|^2+|z_{n,+}|^2\bigr)
 =\frac12\sum_{n<N}w_n^2(r_n^2+c_n^2).          \tag{DP7}
\]
Differences between same-sign frequencies retain the difference phases;
differences between opposite-sign frequencies retain the sum phases.
Thus (DP5) pays all signed cross terms together, including the reflected
oscillatory diagonal, without assigning independent phases or deleting a
coefficient tail.

### Uniform local gaps, including the near-zero endpoint issue

Note 9's exact phase-center expansion gives
\[
M_\phi:=e^{\Omega/c}
 =\sqrt{x/(4\pi)+t/16}+O(x^{-3/2}),\qquad c=\tfrac12+o(1).
                                                               \tag{DP8}
\]
Since \(N\le\sqrt{x/(4\pi)+t/16}\), for all sufficiently small
\(t\) and every \(n<N\),
\[
\lambda_n=c\log(M_\phi/n)
 \ge .45\log(N/n)>0.                         \tag{DP9}
\]
Indeed \(\log(M_\phi/N)\ge-O(x^{-2})\), while the smallest relevant
\(\log(N/n)\) is at least \(1/N\); the former error is negligible
relative to the latter.

Same-sign gaps satisfy the exact identity
\(|\lambda_n-\lambda_m|=c|\log(n/m)|\).
The nearest successor gap is at least
\(c\log(1+1/n)\ge c/(n+1)\ge c/(2n)\); a predecessor gap is at
least \(c/n\). At an index without a successor only the latter is needed.
For opposite signs the distance is
\(\lambda_n+\lambda_m\ge\lambda_n\). Concavity of
\(z\log(N/z)\) on \([1,N-1]\) shows
\[
n\log(N/n)\ge\frac12,
\]
by checking its two endpoints. Together with (DP9), this bounds every
opposite-sign distance from the frequency indexed by \(n\) below by
\(.225/n\). Hence all local gaps in (DP6) obey
\[
\delta_{n,\pm}\ge\frac1{8n},\qquad n<N,       \tag{DP10}
\]
uniformly. The possibly very small or slightly negative \(\lambda_N\)
has not been divided by. Its exact term is restored after the averaging
argument.

### The refined derivative-weighted budget

Define the complete positive budget
\[
B_d:=\sum_{n\le N}nw_n^2(r_n^2+c_n^2).
\]
Its uniform asymptotic is
\[
B_d=\left(\frac{8t^2}{\kappa^2}+o(t^2)\right)
             e^{2\mathfrak a/t}.             \tag{DP11}
\]
To prove it, use \(n=e^{L/2-v}\). The exact weight supplies the mass
\[
nw_n^2\,dn=e^{2\mathfrak a/t}
        e^{-v+tv^2/2}(1+o(1))\,dv.
\]
On bounded logarithmic blocks,
\(r_n=2tv/\kappa+o(t)\), and \(c_n=O(t/x)\). The limiting integral is
\[
\frac{4t^2}{\kappa^2}\int_0^\infty v^2e^{-v}\,dv
 =\frac{8t^2}{\kappa^2}.
\]
Uniform domination follows from \(tv\le1\), so the tail is bounded by
an absolute constant times \(t^2(1+v)^2e^{-v/2}\). First truncate to
bounded \(v\), where the mesh is exponentially small, and then let the
truncation grow. Integral-comparison errors bounded by a polynomial in
\(L\) are negligible compared with \(t^2e^{2\mathfrak a/t}\).
The floor contributes only a negligible endpoint interval. The exact
uniform errors in \(r_n\), after division by \(t\), tend to zero, and
the \(c_n^2\) part is \(O(t^2x^{-2}\sum nw_n^2)\); this pays both
terms in (DP11).

Combining (DP5)--(DP7) with (DP10) gives the explicit signed estimate
\[
\frac1H\int_0^H g_-(y)^2\,dy
\ge\frac12\sum_{n<N}w_n^2(r_n^2+c_n^2)
       -\frac{12\pi}{H}\sum_{n<N}nw_n^2(r_n^2+c_n^2).
                                                               \tag{DP12}
\]
The last sum can be enlarged to the complete \(B_d\). Its prefactor
has no logarithmic loss. The leading coefficient has
\(w_1=1,c_1=0,r_1=1+o(1)\), so the diagonal in (DP12) is at least
\(1/2+o(1)\). By (DP11), choosing an absolute \(D\) sufficiently
large in \(H=H_d\) makes (DP12) at least \(3/8\).

Restore the exact last frozen term to obtain \(g_0\). Its supremum,
and hence normalized \(L^2\) norm, is at most
\[
w_N\sqrt{r_N^2+c_N^2}=o(1),
\]
since \(w_N=O(e^{-\mathfrak b/t})\) and \(|r_N|+|c_N|\) is bounded.
The normalized \(L^2\) triangle inequality now gives the same complete
frozen lower bound with an \(o(1)\) loss.

### Genuine physical movement, cutoff, and normalizer payments

The new sufficient range satisfies
\[
H_d/N=O(t^2e^{-\kappa^2/(8t)})\longrightarrow0,
\qquad H_d^2/x=O(t^4e^{-\kappa^2/(4t)})\longrightarrow0.
                                                               \tag{DP13}
\]
It is contained, for small \(t\), in Note 9's proved physical interval
of length \(H_p=D_9Le^{2\mathfrak a/t}\). Its center-data bounds and
error payments therefore apply. More explicitly, at \(0\le y\le H_d\),
exact fixed-time differentiation gives
\[
|(\log w_n)'|=O(x^{-1}),\quad |\phi_n''|=O(x^{-1}),\quad
|r_n'|=O((Lx)^{-1}),\quad |c_n'|=O(t/x^2),
                                                               \tag{DP14}
\]
uniformly for \(n\le N\). The denominator in the last two expressions
remains the fixed \(L\). The bounds \(|r_n|+|c_n|\le2\) and
\(S=\sum w_n=O(e^{\mathfrak a/t})\) give the sufficient complete-sum
movement estimate
\[
\sup_{0\le y\le H_d}|G_F(y)-g_0(y)|
 \le CS(H_d/x+H_d^2/x)=o(1).                 \tag{DP15}
\]
This includes amplitude variation, the nonlinear phase remainder,
and the change in the derivative coefficients. The largest exponential
factor is \(e^{(5\mathfrak a-\kappa)/t}\), and
\[
5\mathfrak a-\kappa
 =\kappa(4-5\kappa)/16\le-1/16.
\]
Therefore the complete genuine scaled derivative has the first lower
bound in (DP3).

For the exact heat function, at each physical center \(x+y\) use the
existing disk of radius \(1/L_y\), with
\(L_y=\log((x+y)/(4\pi))\), at the same time and fixed cutoff \(N\).
By (DP13), the continuous cutoff changes by \(o(1)\) across the whole
interval and these disks. Every possible natural cutoff differs from
\(N\) by at most one. The holomorphic majorant pays that coefficient,
the conversion to the symmetric normalizer \(A_t\), and the lower-half
reflection. Cauchy's estimate at each center then gives
\[
|Q_t'(x+y)-F_{t,N}'(x+y)|\le L_y\eta_{N,y}.
\]
As in Note 9, \(tL_y\in[1,2+o(1)]\); the ledger's strict reserves
extend to this vanishing neighborhood (for example, \(tL_y\le2.01\)
for small \(t\)). Also \(L_y/L=1+o(1)\) and the change in the error
exponent is \(O(H_d/x)=o(1)\). Thus
\[
\sup_{0\le y\le H_d}|G_Q(y)-G_F(y)|
 \le\sup_{0\le y\le H_d}2(L_y/L)\eta_{N,y}
 =O(e^{-\mathfrak b/t})=o(1).                \tag{DP16}
\]
This is the full physical derivative payment; it is not an assumption
about a remainder on a single radius-\(H_d\) disk. The normalized
\(L^2\) triangle inequality completes (DP3).

For comparison, applying the same Hilbert argument componentwise to the
whole frozen joint vector replaces \(B_d\) by
\(\sum nw_n^2(1+r_n^2+c_n^2)=O(e^{2\mathfrak a/t})\). It therefore
removes Note 9's logarithm already at \(H=De^{2\mathfrak a/t}\).
The derivative-only argument gives the shorter \(H_d\) because the
near-cutoff squared weight contains \(r_n^2\asymp t^2v^2\).
Derivative weighting suppresses the endpoint budget polynomially; its
exponential scale remains. Both ranges are **sufficient**, and no lower
bound on the necessary range of all probe methods is proved.

### The derivative Taylor-transfer deficit and a limited measure consequence

Note 9's full absolute curvature budget and its Cauchy remainder payment
give \(|Q_t''|\le M_2:=C_2e^{\mathfrak a/t}\) on this physical interval.
At a hypothetical genuine collision at its left endpoint,
\(Q_t(x)=Q_t'(x)=0\), Taylor's theorem yields
\[
|Q_t'(x+y)|\le M_2y,\qquad
\frac1H\int_0^H\left(2Q_t'(x+y)/L\right)^2\,dy
 \le\frac{4M_2^2H^2}{3L^2}.                 \tag{DP17}
\]
With this proved majorant, a small constant Taylor upper bound is
available on the scale \(H=O(Le^{-\mathfrak a/t})\). The ratio of the
new sufficient averaging range to that scale is
\[
\frac{H_d}{Le^{-\mathfrak a/t}}
 =\frac{Dt^2}{L}e^{3\mathfrak a/t}\longrightarrow\infty.
                                                               \tag{DP18}
\]
At \(H=H_d\), (DP17) therefore provides no contradiction to (DP3).
Equivalently, the derivative average at a collision forces only the
weak necessary condition
\(\sup|Q_t''|\ge\sqrt{3/32}\,L/H_d\), an exponentially small lower
bound compatible with the paid curvature budget. This is a deficit of
the proved average plus the available absolute transfer, not a theorem
that no stronger collision-conditioned transfer can exist.

There is a limited measure consequence. The same absolute first-derivative
moment used in Note 9 gives \(\sup|G_Q|\le Ct e^{\mathfrak a/t}\).
For
\[
E=\{y\in[0,H_d]:|G_Q(y)|\ge1/4\},
\]
(DP3) and the supremum bound imply
\[
|E|/H_d\ge c\,t^{-2}e^{-2\mathfrak a/t},
\qquad |E|\ge c'>0
                                                               \tag{DP19}
\]
with absolute constants, after fixing \(D\). Indeed the mean square is
at most \(1/16+C^2t^2e^{2\mathfrak a/t}|E|/H_d\). The proved lower
bound on relative measure tends to zero; it does not bound the actual
relative measure above or prevent isolated double zeros.

The checkpoint remains local. The complete genuine derivative has proved
positive averaged energy on a shorter sufficient range, with all
reflected cross terms, physical movement, cutoff changes, normalization,
and holomorphic derivative errors paid. A pointwise implication using
both small collision coordinates and their actual arithmetic phases is
still required.

## 6. The remaining signed input

The two paid collision coordinates in (A2) give a smaller derivative core
without asserting it is large. The threshold fourth-derivative test in
Note 12 supplies an additional necessary condition at the all-real
threshold. For its quadratic products the common cutoff \(K_v\) has a
uniformly vanishing payment; the larger derivative cutoff needs its
measured jet errors retained.

A useful next implication would show that both coordinates in (A2) being
small forces the actual threshold expression below the negative error
budget in Note 12. Alternatively, a uniform strict reverse of one
coordinate bound in (A2) would exclude a local collision directly.
Neither implication is proved here. The complete derivative average
(DP3) remains an averaged statement, and the fixed-order derivative
method cannot dispose of a whole endpoint block by triangle aggregation.

The [small exact checker](../../numerics/check_local_heat_jet_input.py)
and [record](../../numerics/local_heat_jet_input_record_20261009.json)
check their stated algebraic identities, scalar reserves, exponents,
and finite polynomial models. They evaluate no actual heat function,
height phases, huge cutoff, or zero grid. Imported inequalities and
analytic limits remain mathematical proof inputs. See the
[scoped review](../../reviews/HEAT_LOCAL_JET_AND_DERIVATIVE_INPUT_REVIEW_20261009.md).
The stable manuscript is left for the planned progress review. No RH,
global collision exclusion, or literature-novelty claim is made.
