# Prime-density centering and a signed dilation target

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not inferred. These are internal
calculations, not independent specialist refereeing. No new fixed global
exponent or mathematical priority is claimed.

## 1. Result

The complete scalar in the [previous continuation](SIGNED_COVARIANCE_CONTINUATION_20261004.md)
admits a useful further elimination. Replacing its inner prime measure by
ordinary Lebesgue measure cancels **the entire** continuum
\(c_wM_1(U)\), with a uniform lattice error

\[
O_w((U^2/X)^8).
\tag{1}
\]

No estimate for a Mertens sum is used. At \(U=X^{11/24}\), this is
\(O_w(X^{-2/3})\). Only a signed average of the normalized prime
discrepancy remains. Its explicit lower-cutoff boundary also costs at most
\(O_w((U^2/X)^7)=O_w(X^{-7/12})\). Both eliminations retain real
cutoffs, all terminal product bands, and the sign of every coefficient.

This removes two apparent obligations, estimating the reciprocal Möbius
sum and estimating the continuum prime density, from the next target.
It does **not** establish a power bound for the remaining signed prime
discrepancy. The currently available PNT input gives logarithmic savings
after absolute estimation, and neither a sufficient power nor a sign.

## 2. Definitions and exact prime-measure decomposition

Keep \(A=e^{-1/4}\), \(B=e^{1/4}\), \(C=2B\), \(q=7/3\), and
the fixed prepared probe \(w\). Define

\[
\ell(v)=\int_1^2 y w(v/y)\,dy,
\qquad H(v)=\int_v^\infty\ell(s)\,ds,
\qquad f(v)=H(v)/v\quad(v>0).
\tag{2}
\]

All three functions are extended by zero where appropriate. They have
support in \([A,C]\), because

\[
\int\ell=0,\qquad
\int\ell(v)\log v\,dv=q c_w,
\qquad \int f(v)\,dv=q c_w.
\tag{3}
\]

The last identity follows by integration by parts with \(H'=-\ell\):
\(\int H(v)/v\,dv=\int\ell(v)\log v\,dv\). All boundary terms
vanish; in particular \(H(v)=0\) for \(v\le A\), not just for
\(v\ge C\).

Let \(X>0\), \(U\ge1\) be real and suppose

\[
U^2\le AX.
\tag{4}
\]

Set \(N=X/U\),
\(A_U(m)=\sum_{d\mid m,d>U}\mu(d)\), and
\(M_1(U)=\sum_{d\le U}\mu(d)/d\). Integers at the outer and inner
cutoffs are included according to these displayed strict or weak
inequalities. Write

\[
\theta(t)=\sum_{p\le t}\log p,\qquad E(t)=\theta(t)-t,
\]
\[
J_0(X;U)=c_wM_1(U)
+\frac1{qX}\sum_{m>U}A_U(m)
   \int_{(U,\infty)}\ell(mt/X)\,d\theta(t).
\tag{5}
\]

Since \(d\theta=dt+dE\), this is exactly

\[
J_0=c_wM_1(U)+D_{X,U}+Q_{X,U},
\]
\[
D_{X,U}=\frac1q\sum_{m>U}\frac{A_U(m)}m H(m/N),
\qquad
Q_{X,U}=\frac1{qX}\sum_{m>U}A_U(m)
\int_{(U,\infty)}\ell(mt/X)\,dE(t).
\tag{6}
\]

The density term has support only in the terminal outer band
\(AN<m<CN\). The discrepancy term retains the larger complete
range \(U<m<CN\). Endpoint equality causes no difficulty because
\(H\) and \(\ell\) vanish at their support endpoints.

## 3. Two extra derivative orders and exact density cancellation

The zero extension of \(w\) is \(C^4\), piecewise smooth, and
\(D^6w\) is a finite signed measure, as proved in the
[parent reduction](../../MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md).
The shell average has the exact derivative formula

\[
\ell'(v)=\frac{2\ell(v)}v+\frac{w(v)-4w(v/2)}v.
\tag{7}
\]

Consequently \(\ell\) is \(C^5\) and \(D^7\ell\) is a finite
signed measure. This follows either by repeatedly differentiating (7)
as distributions on its support away from zero, or by using
\(\ell(v)=v^2\int_{v/2}^v w(s)s^{-3}\,ds\). A primitive gains
one further derivative: \(H\) and \(f=H/v\) are \(C^6\), with
\(D^8f\) a finite signed measure. Multiplication by \(1/v\) is
harmless on their compact support. There is no unsupported assumption
that the original probe is infinitely differentiable.

For this zero-extended \(f\), Poisson summation therefore gives, for
every real \(y>0\),

\[
\sum_{k\ge1}f(k/y)=y\int f+r_f(y),
\qquad
|r_f(y)|\le C_f y^{-7},
\qquad C_f=\frac{\|D^8f\|_{\rm TV}}{1209600}.
\tag{8}
\]

The constant is \(2\zeta(8)/(2\pi)^8=1/1209600\).
Absolute convergence of the Fourier series follows from the eighth-order
distributional derivative bound. Negative and zero lattice samples vanish.

For every retained \(m>U\),
\(A_U(m)=-\sum_{d\mid m,d\le U}\mu(d)\). Condition (4) lets
us extend the outer sum to all positive \(m\), since all added
\(H(m/N)\) vanish. Thus (6) becomes

\[
D_{X,U}
=-\frac1{qN}\sum_{d\le U}\mu(d)\sum_{k\ge1}f(dk/N)
=-c_wM_1(U)+R_{X,U},
\tag{9}
\]
\[
R_{X,U}=-\frac1{qN}\sum_{d\le U}\mu(d)r_f(N/d),
\qquad
|R_{X,U}|\le\frac{C_f}{qN^8}\sum_{d\le U}d^7
\le\frac{C_f}{q}(U^2/X)^8.
\tag{10}
\]

The equality in (9), including its minus sign, is the cancellation of
the full continuum. Hence

\[
\boxed{\quad J_0(X;U)=Q_{X,U}+R_{X,U}.\quad}
\tag{11}
\]

The real cutoff \(U\) has not been rounded inside \(H(mU/X)\) or
in an integral limit. Only integer summation bounds involve its floor.

## 4. The lower endpoint and the signed dilation average

Stieltjes integration by parts, with right-continuous \(E\), gives

\[
\int_{(U,\infty)}\ell(mt/X)\,dE(t)
=-E(U)\ell(mU/X)
-\frac mX\int_U^\infty E(t)\ell'(mt/X)\,dt.
\tag{12}
\]

This formula uses \(E(U)\), not \(E(U-)\). It is valid when
\(U\) is prime, in which case its atom is correctly excluded.
An equivalent exact formula is

\[
\int_{(U,\infty)}\ell(mt/X)\,dE(t)
=-\frac mX\int_U^\infty [E(t)-E(U)]\ell'(mt/X)\,dt.
\tag{13}
\]

The boundary in (12) is itself affordable. Put

\[
C_\ell=\frac{2\zeta(7)}{(2\pi)^7}\|D^7\ell\|_{\rm TV}.
\]

Since \(\int\ell=0\), the seventh-order lattice estimate and (4)
give

\[
\left|\sum_{m>U}A_U(m)\ell(m/N)\right|
\le C_\ell N^{-6}\sum_{d\le U}d^6
\le C_\ell N^{-6}U^7.
\tag{14}
\]

Use the elementary Chebyshev estimate \(|E(U)|\ll U\). The first
term of (12), after summing and normalizing, is therefore
\(O_w(U^{14}/X^7)=O_w((U^2/X)^7)\).

Define the normalized prime discrepancy \(\varepsilon(t)=E(t)/t\)
and the **signed** functional

\[
\mathcal I(X;U)=
\sum_{U<m<CX/U}\frac{A_U(m)}m
\int_{mU/X}^{C}
\varepsilon(Xv/m)\,v\ell'(v)\,dv.
\tag{15}
\]

Changing variables in the second term of (12) now proves

\[
\boxed{\quad
J_0(X;U)=-\frac1q\mathcal I(X;U)
+O_w((U^2/X)^7+(U^2/X)^8).
\quad}
\tag{16}
\]

All prime discrepancies in (15) are sampled at
\(U\le Xv/m\le CX/U\). For \(m\le AX/U\), the effective
inner interval is the full \([A,C]\); for larger \(m\), its lower
cutoff must stay. The identity
\(\int_A^C v\ell'(v)\,dv=0\) does not allow removal of these
terminal intervals. Nor does it give a sign for the functional.

At the original cutoff (16) has error \(O_w(X^{-7/12})\). For
every fixed \(0<\kappa<11/24\), the previous prime-power reduction
and scalar detector therefore make each of

\[
\mathcal I(X;X^{11/24})\ge-CX^{-\kappa/2},
\qquad
\mathcal I(X;X^{11/24})\le CX^{-\kappa/2}
\tag{17}
\]

separately sufficient, on all sufficiently large real \(X\), for
the desired variance exponent. The direction reverses in (16): a lower
bound on \(\mathcal I\) gives the upper bound on \(J_0\).
Neither inequality in (17) has been established.

## 5. The scalar allows a slightly narrower product range

The gain of one derivative for \(\ell\) also improves the allowable
Vaughan cutoffs when only the scalar is compared. Apply the same
seventh-order lattice estimate directly to \(\ell/q\), whose ordinary
moment is zero and logarithmic moment is \(c_w\). For real
\(U,V\ge1\), with \(U\le X\) and \(V<AX\), the scalar error
between the exact response and the centered full Vaughan scalar is

\[
O_w\!\left(X^{-7}
\{U^7(1+\log X)+(UV)^7\}\right).
\tag{18}
\]

Indeed, the Type I sum costs
\(X^{-7}\sum_{d\le U}d^6(1+\log(X/d))\), and the mixed sum
costs \(X^{-7}\sum_{d\le U}d^6\sum_{n\le V}\Lambda(n)n^6\).
Chebyshev bounds the latter by \(O(X^{-7}U^7V^7)\).
The low prime-response term vanishes because \(V<AX\).

Thus fixed positive exponents \(U=X^u,V=X^v\) with

\[
u+v\le1-\kappa/14
\tag{19}
\]

preserve the exact scalar target \(O(X^{-\kappa/2})\). The positive
\(v\) absorbs the logarithm in the first term of (18). In particular
balanced cutoffs can be chosen as

\[
U=V=X^{1/2-\kappa/28}.
\tag{20}
\]

This is a scalar comparison, not an asserted improvement to the earlier
norm comparison. At (20), the density remainder in (10) is
\(O(X^{-4\kappa/7})\), and the lower-endpoint term is
\(O(X^{-\kappa/2})\). Both are adequate. The inner higher-prime-power
scalar bound \(O(U^{-1/2}\log X)\) is smaller than the target when
\(\kappa<1/2-\kappa/28\), equivalently \(\kappa<14/29\).
In particular this includes the illustrative \(\kappa=0.01\).
For that choice the balanced exponent is \(1399/2800\), and the
ratio of the largest to smallest possible factor has power \(1/1400\).

## 6. What existing arithmetic input actually supplies

The classical quantitative prime number theorem supplies
\(E(t)\ll_M t/(\log t)^M\) for every fixed \(M\); for instance
see Corollary 39 in
[Tao's complex-analytic number theory notes](https://terrytao.wordpress.com/2014/12/09/254a-notes-2-complex-analytic-multiplicative-number-theory/).
The passage from \(\psi\) to \(\theta\) costs only the elementary
higher-prime-power bound. No fixed-power PNT error is being assumed.

For any fixed balanced exponent \(0<a<1/2\), \(U=X^a\) gives

\[
\sum_{U<m<CX/U}\frac{|A_U(m)|}{m}
\le\sum_{d\le U}\frac1d\sum_{k\le CX/(Ud)}\frac1k
\ll (\log X)^2.
\tag{21}
\]

Applying the PNT bound inside (15) and using the fixed integral
\(\int_A^C|v\ell'(v)|\,dv\), we obtain

\[
|\mathcal I(X;X^a)|\ll_{M,w,a}(\log X)^{-M}
\quad\hbox{for every fixed }M,
\tag{22}
\]

after increasing the input logarithmic power by two. A quantitative
zero-free-region error similarly transfers as a subpower function.
Neither dominates \(X^{-\kappa/2}\) for any fixed positive
\(\kappa\). Taking absolute values has erased precisely the joint
Möbius/prime-discrepancy cancellation needed by (17).

Conversely, substituting a hypothesized pointwise power estimate for
\(E\), or a power Mertens estimate to bound the outer coefficients,
would introduce fixed-strip strength as an assumption. The present
calculation makes neither substitution. Its useful conclusion is that
the density, continuum, and cutoff boundary have all been rigorously
removed at affordable power cost; the remaining obstruction is their
actual signed dilation average of prime errors.

## 7. Verification and scope

The definitions, signs, support caps, derivative gains, Poisson constants,
and cutoff exponents were checked internally. A separate exact-rational
checker is provided at
[check_prime_discrepancy_centering.py](../../../numerics/01_signed_arithmetic_covariance/check_prime_discrepancy_centering.py).
It uses a compact polynomial scalar kernel with zero ordinary moment and
rationally weighted prime atoms to exercise the algebra, including prime
and noninteger cutoffs. Its
[retained record](../../../numerics/01_signed_arithmetic_covariance/prime_discrepancy_centering_record_20261004.json)
reports 386 exact comparisons on 32 cases; intentionally omitting the
cutoff boundary fails in 28 cases. This is an algebra and endpoint check, not a
numerical certificate for the fixed probe or the analytic derivative-TV
constants. No asymptotic rate is inferred from these finite checks.

No new global exponent, sign inequality, or zero-free strip is proved.
