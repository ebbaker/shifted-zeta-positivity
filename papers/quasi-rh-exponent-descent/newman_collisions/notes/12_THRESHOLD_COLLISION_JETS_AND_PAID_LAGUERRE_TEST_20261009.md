# Threshold collision jets and a paid Laguerre test

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model audits are internal checks, not independent validation.

This continues the exact interface in
[Heat Note 8](8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md),
the actual-phase estimates in
[Heat Note 9](9_GENUINE_SIGNED_EDGE_CANCELLATION_AND_AVERAGED_PROBES_20261009.md),
the separately scoped relaxation in
[Heat Note 10](10_COMPLETE_MULTIPLICATIVE_PHASE_OBSTRUCTION_20261009.md),
and the derivative-core work in
[Heat Note 11](11_ASYMMETRIC_DERIVATIVE_CORES_AND_JOINT_PROBES_20261009.md).
The new input is a necessary higher-jet inequality at an **all-real
threshold collision**, together with complete approximation payments.
It retains the actual heat function and actual arithmetic phases. No
strict opposite signed inequality for those phases is established here.

## 1. Exact normalization and the backward heat equation

The flow satisfies \(\partial_tH_t=-\partial_x^2H_t\). Write
\(H_t=A_tQ_t\), using the manuscript's nonvanishing symmetric analytic
normalizer. Let

\[
\ell(t,x)=\log A_t(x),\qquad
b=\partial_x\ell,\qquad a_0=\partial_t\ell,\qquad
c=a_0+\partial_xb+b^2.
\]

The exact normalized equation is

\[
\partial_tQ_t=-Q_t''-2bQ_t'-cQ_t,
\qquad
(\partial_t+a_0)Q_t=-(\partial_x+b)^2Q_t.
\tag{1}
\]

All spatial primes below hold time fixed. This equation follows by
differentiating \(H_t=A_tQ_t\); no approximation or arithmetic estimate
is used. At a common zero \(Q_t=Q_t'=0\), it gives

\[
\partial_tQ_t=-Q_t'',\qquad
\partial_tQ_t'=-Q_t'''-2bQ_t''.
\tag{2}
\]

At an ordinary double collision, the Jacobian of \((Q_t,Q_t')\),
in column order \((x,t)\), consequently has determinant \((Q_t'')^2>0\).
Normalization and the transport term therefore preserve the ordinary
transverse collision geometry.

For exact coefficient evaluation, put \(s=(1-ix)/2\) and use the
manuscript's \(m_t(s)=m_0(s)+t\alpha(s)^2/4\). On the real axis,

\[
a_0=\tfrac14\Re(\alpha(s)^2),\qquad
b=\tfrac12\Im m_t'(s),\qquad
m_t'(s)=\alpha(s)(1+t\alpha'(s)/2),
\]
\[
b_x=-\tfrac14\Re\left\{\alpha'(s)
+\tfrac t2\bigl(\alpha'(s)^2+\alpha(s)\alpha''(s)\bigr)\right\},
\qquad
\alpha''(s)=s^{-3}+2(s-1)^{-3}-\tfrac12s^{-2}.
\tag{3}
\]

These are fixed-time derivatives of the explicit normalizer, including
its heat correction. In the shrinking regime below, \(b_x=O(x^{-2})\)
uniformly. The real part of \(\alpha'\) is \(O(x^{-2})\),
\(\alpha'^2=O(x^{-2})\), and the remaining real product in (3) is
bounded after multiplication by \(t\), because \(t\log x=O(1)\).

The carrier can also be conjugated out exactly. Set
\(M=M_t(s)=A_te^{i\theta_t}\), \(U=H_t/M=e^{-i\theta_t}Q_t\), and
\(\Omega=\tfrac12\Re m_t'(s)=-\theta_t'\). Then

\[
\partial_tU=-U''-2(b-i\Omega)U'-v_MU,
\qquad
v_M=\tfrac14\{\alpha^2-(m_t')^2-m_t''\},
\tag{4}
\]

where \(m_t''=\alpha'+t(\alpha'^2+\alpha\alpha'')/2\).
The real potential in (1) satisfies \(c=\Omega^2+\Re v_M\).
At \(U=U'=0\), (4) still gives \(\partial_tU=-U''\).
This carrier transformation reorganizes the equation but supplies no
nonvanishing condition at a candidate collision.

## 2. What Laguerre evolution permits at a positive collision

For the genuine unnormalized function, let

\[
W=(H_t')^2-H_tH_t''.
\]

Direct differentiation of the backward heat equation gives

\[
\partial_tW=-W''+2\{(H_t'')^2-H_t'H_t'''\}.
\tag{5}
\]

At an ordinary double real collision \((T,x_*)\),

\[
W=0,\qquad W''=\partial_tW=(H_T''(x_*))^2>0.
\tag{6}
\]

Thus \(W(T-h,x_*)=-h(H_T''(x_*))^2+O(h^2)<0\) for sufficiently
small \(h>0\). This is consistent with nonreal zeros just before the
collision and all real zeros at the threshold. Equation (5) is backward
parabolic and has a nonzero source at the collision. Laguerre
nonnegativity at the all-real time does not yield a forward maximum
principle that excludes such an event.

The exact normalized Laguerre expression is

\[
W/A_t^2=(Q_t')^2-Q_tQ_t''-b_xQ_t^2.
\tag{7}
\]

The normalizer's second logarithmic derivative is part of this identity.
At the collision, both the normalized expression and its first spatial
derivative vanish, while its time and second spatial derivatives equal
\((Q_t'')^2\). The PDE consequently does not improve the ordinary
collision into an impossible configuration.

## 3. The all-real threshold is the valid source of the extra sign

If RH fails, the classical threshold property gives \(\Lambda>0\).
The manuscript's finite-collision reduction supplies a nonzero real
\(x_*\) with \(H_\Lambda(x_*)=H_\Lambda'(x_*)=0\). At this particular
time, **all zeros are real**, by the threshold theorem. This global
fact is not inferred from the local equations, from a maximizing root,
or from an arbitrary positive-time collision.

The primary source
[Polymath, Section 3 and the proof of Proposition 3.1](https://arxiv.org/html/1904.12438v2#S3)
records that \(H_t\) is even, real entire of order one, nonzero at zero,
and has a locally uniformly convergent Hadamard product grouped in
opposite-root pairs. Differentiating that product, and then differentiating
once more, gives the usual inverse-square sum. The second sum converges
absolutely off the roots. These are the imported canonical-product facts;
the Laguerre deductions below are elementary consequences.

**Proposition 1 (deflated mirror inequality, every multiplicity).**
Suppose \(T\) is a time at which all zeros of \(H_T\) are real, and
\(x_*\ne0\) is a root of multiplicity \(m\ge2\). With
\(H_j=H_T^{(j)}(x_*)\),

\[
2H_3^2-3H_2H_4\ge\frac{9H_2^2}{x_*^2}.
\tag{8}
\]

In particular this holds at every finite positive threshold collision,
including higher multiplicities.

To prove it, deflate exactly two copies of the root:
\(g(z)=H_T(z)/(z-x_*)^2\). This is real entire of order at most one,
and all its roots are real. Evenness of \(H_T\) supplies at least two
remaining copies of the mirror root \(-x_*\). Away from the real roots,
the canonical product gives

\[
(g')^2-gg''
=g^2\sum_{\rho\text{ root of }g}\frac1{(z-\rho)^2}
\ge\frac{2g(z)^2}{(z+x_*)^2}
\tag{9}
\]

for real \(z\). Take the continuous limit as \(z\to x_*\), along
points away from roots. This remains valid if \(m>2\), when
\(g(x_*)=0\); no logarithmic derivative at that zero is taken.
The Taylor coefficients are

\[
g(x_*)=H_2/2,\qquad g'(x_*)=H_3/6,\qquad g''(x_*)=H_4/12.
\]

Multiplying the limiting inequality (9) by 72 proves (8). For
\(m=3\), its left side is \(2H_3^2>0\); for \(m\ge4\), both sides
of (8) are zero. The latter case is allowed by the necessary inequality,
not excluded by it.

At the collision put \(q_j=Q_T^{(j)}(x_*)\). Product differentiation
using \(q_0=q_1=0\) gives

\[
H_2=A_Tq_2,\quad H_3=A_T(q_3+3bq_2),\quad
H_4=A_T\{q_4+4bq_3+6(b_x+b^2)q_2\}.
\]

All \(b\)-terms cancel except \(b_x\). Define

\[
\gamma(t,x)=18b_x(t,x)+9/x^2,
\qquad
\mathscr L(q_2,q_3,q_4)=2q_3^2-3q_2q_4-\gamma q_2^2.
\tag{10}
\]

Then every such collision satisfies the exact genuine sign condition

\[
\mathscr L(q_2,q_3,q_4)\ge0.
\tag{11}
\]

In the shrinking regime, \(\gamma=O(x^{-2})\). Additional disjoint
real-root blocks could strengthen (9), but no unprinted counting constant
is assigned a numerical value here. The forced mirror alone supplies
the explicit coefficient 9 in (8).

The fourth-jet test does not resolve higher multiplicities: for
\(m\ge4\), \(q_2=q_3=0\), and (11) is the vacuous equality zero,
even when \(q_4\ne0\). At an exact multiplicity \(m\), deflating all
\(m\) copies instead gives the nonvacuous mirror condition

\[
\frac{q_{m+1}^2}{(m+1)^2}
-\frac{2q_mq_{m+2}}{(m+1)(m+2)}
-\left(b_x+\frac{m}{4x_*^2}\right)q_m^2\ge0.
\tag{11a}
\]

Indeed \(g=H_T/(z-x_*)^m\) has at least \(m\) mirror copies,
and its Laguerre inequality has lower bound
\(m g(x_*)^2/(4x_*^2)\). Substitute its first three Taylor
coefficients and differentiate \(H_T=A_TQ_T\); the \(b\)-terms
again cancel. This uses jets \(m,m+1,m+2\) and requires their own
approximation payments. It is not a consequence of a bounded
second-through-fourth-jet certificate. A strict paid opposite test of
(11) covers any candidate at which it can be proved, but the existence
of such a test for higher-multiplicity candidates is not established.

## 4. A sharp scoped example for the PDE/Laguerre mechanism

The coefficient in (8), and compatibility with a positive threshold,
can be checked on an even polynomial heat flow. Fix \(T>0\), \(a>0\),
put \(\delta=t-T\), and define

\[
P_t(z)=z^4-(2a^2+12\delta)z^2
+a^4+4a^2\delta+12\delta^2
=e^{-\delta\partial_z^2}(z^2-a^2)^2.
\tag{12}
\]

It obeys \(\partial_tP_t=-P_t''\) exactly. Regarding it as a quadratic
in \(z^2\), its discriminant is \(32\delta(a^2+3\delta)\), and
its constant coefficient is positive for every real \(\delta\).
For \(\delta\ge0\), both roots in \(z^2\) are positive, so all four
zeros are real. For \(-a^2/3<\delta<0\), the discriminant is negative.
For \(\delta\le-a^2/3\), the roots in \(z^2\) are negative, including
the equal-root endpoint. Thus its all-real threshold is exactly \(T\).
If \(a^2>6T\), also \(P_t(iy)>0\) for every \(t\ge0\),
\(y\in\mathbb R\), by inspection of its positive coefficients after
substituting \(z=iy\).

At \((T,a)\), the spatial jets are
\(P_2=8a^2\), \(P_3=24a\), and \(P_4=24\), and

\[
2P_3^2-3P_2P_4=576a^2=9P_2^2/a^2.
\tag{13}
\]

The mirror inequality is sharp in this general class. Dividing this flow
by the same explicit zero-free normalizer yields (1) with the same
normalizer coefficients and retains its positive-time collisions.
This is a counterexample to a mechanism using only the heat PDE,
normalization, threshold real-rootedness, and the stated Laguerre signs.
It is not the zeta heat function, does not have zeta's infinite zero set
or arithmetic coefficients, and is not asserted to arise from the
positive theta kernel. The example does not obstruct additional signed
arithmetic input.

## 5. Complete paid approximation of the genuine threshold jet

Retain the shrinking regime

\[
1\le\kappa\le2,\quad 0<t\le1/20,\quad
L=\kappa/t,\quad x=4\pi e^L,\quad
N=\lfloor\sqrt{e^L+t/16}\rfloor,
\]
\[
\mathfrak a=\kappa(4-\kappa)/16,
\qquad \mathfrak b=\kappa(\kappa+4)/16.
\]

The complete small-disk bound from Note 8 is
\(|Q_t-F_{t,N}|\le\eta_N\le5e^{-\mathfrak b/t}\) on radius \(1/L\),
including normalizer conversion, reflection, and possible cutoff changes.
Cauchy's formula consequently gives at the center

\[
|Q_t^{(j)}-F_{t,N}^{(j)}|\le j!\eta_NL^j.
\tag{14}
\]

For an integer \(K\le N\), fixed when differentiating, let
\(f_j=F_{t,K}^{(j)}(x)\), and choose proven nonnegative tail payments
\(\tau_j\ge|F_{t,N}^{(j)}-F_{t,K}^{(j)}|\), \(j=2,3,4\).
Then

\[
|q_j-f_j|\le\delta_j:=j!\eta_NL^j+\tau_j.
\tag{15}
\]

This is the original holomorphic error followed by an exact signed
finite-tail subtraction. It does not invoke an unpaid approximation
with a moving cutoff or differentiate the parameter-dependent choice
of \(K\).

Define the measured payment

\[
\begin{split}
\Delta(f,\delta)={}&4|f_3|\delta_3+2\delta_3^2
+3|f_2|\delta_4+3|f_4|\delta_2+3\delta_2\delta_4\\
&+|\gamma|\{2|f_2|\delta_2+\delta_2^2\}.
\end{split}
\tag{16}
\]

Product expansion and the triangle inequality give
\(|\mathscr L(q)-\mathscr L(f)|\le\Delta(f,\delta)\).
Thus the sufficient paid arithmetic condition

\[
\boxed{\quad\mathscr L(f_2,f_3,f_4)<-\Delta(f,\delta)\quad}
\tag{17}
\]

excludes an all-real-time collision at that parameter point. It includes
all multiplicities \(m\ge2\), by Proposition 1. No claim that (17)
holds for the actual phases is made.

For an RH application, it is enough to prove (17) at every putative
positive threshold collision under consideration. One may restrict the
arithmetic task to the genuine candidate conditions
\(|F_{t,N}|\le\eta_N\), \(|F_{t,N}'|\le L\eta_N\), or their paid
core analogues. Those conditions follow from an exact collision.
The all-real threshold input remains separate; (11) is not asserted at
an arbitrary positive-time collision while other zeros are nonreal.
This regime alone would still leave other heights and scaling regimes.

### Full cutoff: the quadratic approximation error tends to zero

For \(K=N\), take \(\tau_j=0\). The complete genuine absolute spatial
jet budgets from Note 9's weighted frequency moments, extended to the
fixed orders 2--4, give

\[
|f_j|=O_j(e^{\mathfrak a/t}),\qquad j=2,3,4.
\tag{18}
\]

The leading terms are bounded by
\(2\sum w_n|\lambda_n|^j=(4j!+o(1))e^{\mathfrak a/t}\).
All amplitude and frequency-variation terms have smaller total mass;
the exact real-axis formulas give spatial variations of order \(x^{-1}\)
or smaller, and the same weighted moment bounds pay their products.
No cancellation is needed for this error ledger.

Equations (14), (16), and (18) imply

\[
\Delta_N
=O\left(L^4e^{(\mathfrak a-\mathfrak b)/t}
+L^6e^{-2\mathfrak b/t}\right)
=O\left(L^4e^{-\kappa^2/(8t)}
+L^6e^{-2\mathfrak b/t}\right)=o(1).
\tag{19}
\]

The approximation is therefore accurate with a vanishing **absolute**
error even for this quadratic jet expression, despite exponentially
large complete absolute coefficient mass. Equation (19) establishes
accuracy of the test, not its required negative sign.

### The value core also has a vanishing quadratic payment

For \(K_v=N-\lfloor N^{3/4}\rfloor\), Note 11 gives the fixed-time
raw derivative-tail payments

\[
\tau_j=O_j\left(N^{7/12-s_\kappa-j/4}\right),
\qquad s_\kappa=1/2+\kappa/8,\qquad j=2,3,4.
\tag{20}
\]

Their uniform exponents are respectively \(-13/24,-19/24,-25/24\).
The complete absolute jet bound (18) applies to a retained prefix too.
Since \(e^{\mathfrak a/t}=(1+o(1))N^{(4-\kappa)/8}\), the dominant
product of a tail payment with an absolute jet is bounded by

\[
e^{\mathfrak a/t}\tau_2
=O\left(N^{1/12-\kappa/4}\right)=O(N^{-1/6}).
\]

The corresponding exponents for \(\tau_3\) and \(\tau_4\) have an
additional \(-1/4\) and \(-1/2\). The products of two tail payments
also tend to zero. Inserting the analytic errors from (15) gives

\[
\Delta_{K_v}
=O\left(N^{-1/6}+L^4e^{-\kappa^2/(8t)}
+L^6e^{-2\mathfrak b/t}\right)=o(1).
\tag{21}
\]

All raw derivatives and their conversion factors are retained. The
strict signed condition (17) can therefore use either the complete
cutoff or this core with a uniform vanishing absolute payment.

### A deeper derivative core needs its measured product payment

For \(K_d=N-\lfloor N^{7/8}\rfloor\), Note 11 instead gives

\[
\tau_j=O_j\left(N^{17/24-s_\kappa-j/8}\right),
\qquad j=2,3,4.
\tag{22}
\]

Each derivative-tail payment tends to zero uniformly. However, the
available absolute bound for the product \(|f_4|\tau_2\) has exponent

\[
\frac{4-\kappa}{8}+\frac{17}{24}-s_\kappa-\frac14
=\frac{11}{24}-\frac\kappa4,
\tag{23}
\]

which is positive for \(\kappa<11/6\). This ledger does not prove a
uniform vanishing absolute quadratic error for the deeper core. A
positive exponent in an upper bound does not prove that the actual
error grows. The measured criterion (16)--(17) remains valid with (22);
it must retain those product payments. Individual derivative-tail
smallness cannot be substituted for their paid products.

## 6. Checkpoint and the still-missing genuine signed input

The result is an additional local constraint on a collision at the
all-real threshold, derived from the genuine canonical product. Its
approximation can be paid with a vanishing absolute error at the complete
cutoff and at the \(N^{3/4}\) edge core. The heat PDE and Laguerre
evolution themselves permit ordinary positive-time collisions; the
polynomial model even attains the forced-mirror jet inequality sharply.

The next missing input is a proof of the strict signed opposite test
(17), conditioned if useful on both small collision coordinates, or
the actual complete local value/derivative lower bound from Notes 8--11.
The higher-jet interface is a reduction to genuine arithmetic, not an
established collision exclusion. It does not replace the actual phases
by arbitrary or multiplicative twists, nor infer a threshold collision
from the separate twist examples.

The [small checker](../../numerics/check_local_heat_jet_input.py)
checks only its specified finite algebraic and scalar assertions.
Canonical-product validity, all-real threshold information, the genuine
signed tail bounds, and analytic uniformity remain mathematical inputs;
no zero grid or phase sampling is asserted. See the
[scoped review](../../reviews/HEAT_LOCAL_JET_AND_DERIVATIVE_INPUT_REVIEW_20261009.md).
No manuscript change, RH claim, actual collision, or literature-novelty
claim is made.
