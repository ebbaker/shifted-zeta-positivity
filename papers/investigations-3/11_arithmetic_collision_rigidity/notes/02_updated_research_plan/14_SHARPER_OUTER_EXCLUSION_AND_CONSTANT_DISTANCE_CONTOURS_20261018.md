# Sharper outer exclusion, constant-distance contours and the remaining global contract

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual reasoning
effort ultra**, verified from the parent execution metadata. Parallel
derivations and adversarial checks are internal same-model review; no
independent specialist review is claimed.

This is the final research note for the present bounded continuation of
[overview 02][plan], following Notes 11–13. The separately requested
[round summary][summary] covers the entire overview 02 execution, including
its earlier max-effort phase. The [result-summary index][summaries] and
[patterns-to-avoid index][avoid] govern this note, especially [target
classification][target], [collision controls][controls], [scoped
exclusions][scope] and [preserving cancellation][pairing].

**Earned outcome.** An explicit real first-jet exterior exclusion now begins
at exp(20/epsilon), improving the inherited exp(64/epsilon). A new
constant-distance contour supplies an effective O(x^(-1/4)) omitted-mode
error without logarithmic retreat. The exact current slab gap is
**1001<abs(x)<exp(2000), 1/100<=t<=1/5**. A remote polynomial control
shows why the finite-wall/strip/baseline premises alone cannot remove it.
A canopy ledger binds the already completed initial and moving-barrier
obligations and isolates the missing final-time complex exterior.

The exterior and approximation results below are **proved in-note from
named inputs**, with outward scalar replay; the polynomial identities and
brackets have exact-rational replay. None supplies the missing physical
lower margin, a complete global consumer or a new Newman bound. The latest
[coverage ledger][ledger] supersedes the earlier exp(6400) outer inventory
without changing the finite certificates or pinned manuscript sources.

## A. Explicit smaller real exterior

### 1. Statement and primary-source verification

In the normalization H(0,z)=xi((1+iz)/2)/8,

\[
 \boxed{0<\epsilon\le\tfrac12,\quad
 \epsilon\le t\le\tfrac12,\quad |x|\ge e^{20/\epsilon}
 \quad\Longrightarrow\quad (H(t,x),H_x(t,x))\ne(0,0).}\tag{1}
\]

This is a real first-jet exterior exclusion. It is not complex
nonvanishing throughout an exterior strip and is not a new Newman bound.
At epsilon=1/100 it replaces exp(6400) by **exp(2000)**; the finite bridge
1001<|x|<exp(2000) remains unclosed.

The imported approximation was freshly checked in
[D.H.J. Polymath, *Effective approximation of heat flow evolution of the
Riemann xi function*, arXiv:1904.12438v2, Theorem 1.3](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem3).
Its domain is equation (5): 0<t≤1/2, x≥200, 0≤y≤1. Its normalization and
analytic functions are equations (6)–(10); its approximation, natural
cutoff and explicit errors are (13)–(24). The fixed-cutoff holomorphic
property is explicitly stated following (24). The local repository
Proposition (diskerror) reflects the symmetric-normalized remainder and
pays its normalizer and cutoff changes before Cauchy differentiation.
That proposition's full hypotheses are preserved here. The exact local
[fixed-cutoff contract](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex)
is pinned in the replay record.

### 2. The fixed disk and collision contradiction

By evenness take an arbitrary positive real X≥exp(20/epsilon). Freeze

\[
 Z=\log X,\quad L=\log(X/(4\pi)),\quad
 R=\frac{5}{2L},\quad a=0,\quad N=1,\quad \tau=\tfrac12.
\]

Use the local proposition's enclosing rectangle
X−R≤Re z≤X+R, 0≤Im z≤R, then reflection to the disk |z−X|≤R.
Write x_±=X±R, q_±=x_±/(4π), V=x_−/2, and

\[
 \alpha_-={1\over2}\log q_- -V^{-2},\quad
 A_*={3\over2V}+{1\over2}
       \sqrt{\log^2(S/(2\pi))+\pi^2/4},\quad
 S={1\over2}\sqrt{x_+^2+(1+R)^2},\quad
 D_*={3\over2V^2}+{1\over2V},\quad
 K_* =\exp\{RA_*(1+\tau D_*/2)/2\},\quad
 \omega_*={\alpha_--\tau A_*D_*/2\over2}.
\]

Let η1 denote the full disk remainder bound for N=1. At its real center,
the leading pair is F(t,X)=2cos θ(t,X), with |θ_x|≥ω*. The local
proposition gives |Q−F|≤η1 and |Q_x−F_x|≤η1/R, where Q=H/A and A is
its symmetric, positive-on-the-real-axis, nonzero analytic normalizer.
Thus a collision would imply

\[
 \cos^2\theta+\sin^2\theta
 \le(\eta_1/2)^2+(\eta_1/(2R\omega_*))^2.
\]

It suffices to prove the right side strictly below one.

### 3. Uniform all-height relaxations

The following bounds hold simultaneously for every X≥exp(20/epsilon),
0<epsilon≤1/2. They do not rely on sampling X or enumerating its natural
cutoff. Since Z≥40,

\[
 L>37,\quad R<0.068<1,\quad X-R>200,\quad V>10^{17}.
\]

Let δ=10^-15 and X0=exp(40). The elementary estimates

\[
 |\log q_\pm-L|\le2R/X<\delta,\qquad
 0\le\log(S/(2\pi))-L<\delta
\]

follow from |log(1±u)|≤2u for 0≤u≤1/2, and
log sqrt(1+u)≤u/2. Explicit majorants at X0 are
0.136/X0 and 0.068/X0+1.068²/(2X0²), both below δ.
Because log(4π)<2.54,

\[
 \epsilon\log q_-
 \ge20-\epsilon(\log(4\pi)+\delta)
 >20-\tfrac12(2.54+\delta)>18.7,
 \qquad\log q_->37.
\]

Dividing the A* formula by L and using L>37 and
V≥(X0−.068)/2 gives the explicit upper bound

\[
 {3\over2V_0\cdot37}+{1\over2}
 \sqrt{(1+\delta/37)^2+\pi^2/(4\cdot37^2)}<.51.
\]

Also D*<.001 and V^-2<.001, so

\[
 A_*<.51L,\quad
 \alpha_->\tfrac12\log q_--.001,\quad
 K_*<\exp\{(5/4)(.51)(1.00025)\}<1.9,
\]
\[
 R\omega_*>
 {5\over4}\left[\tfrac12(1-\delta/37)-.001/37-.0001275\right]>.62.
\]

These establish a strictly positive phase speed with the derivative
normalizer cost paid. The natural cutoffs m_−,m_+ obey

\[
 m_-\ge10^8,\qquad
 \log m_+\le\tfrac12\log q_-+.01<\tfrac12 Z.
\]

For the first bound use q_−>(10^8+1)². For the second, use

\[
 \log\frac{q_++\tau/16}{q_-}
 \le \frac{2R+\pi/8}{X-R}<.02.
\]

The final inequality log m+<Z/2 follows from log(4π)>2, the δ
perturbation and .01 slack. This last bound, rather than log m+≤Z,
is used in the k* estimate below.

### 4. The arithmetic and analytic errors

For n≤m+ use the exact majorants from the local proposition,

\[
 d_n=\tfrac14\log^2 n-\tfrac12\alpha_-\log n,
 \quad V_n=n^{-1/2}e^{\max(\epsilon d_n,\tau d_n)},
 \quad P_n=n^{R/2}V_n.
\]

Since log n≤(log q−)/2+.01<2α−, each d_n≤0. Therefore the maximum is
epsilon d_n, and

\[
 P_n\le n^{-p},\qquad
 p={1-R\over2}+{\epsilon\alpha_-\over2}
                         -{\epsilon\log m_+\over4}
 >.466+18.7/8-.0015=2.802>14/5.\tag{2}
\]

No arithmetic cancellation or special phase alignment is used. A sharp
enough elementary power-sum bound is

\[
 \sum_{n=2}^{m_+}P_n\le S_0,
 \qquad S_0=2^{-14/5}+3^{-14/5}
                      +\frac{3^{1-14/5}}{14/5-1}
 <.266623.\tag{3}
\]

The integral in this bound begins at 3, after retaining terms 2 and 3.

The auxiliary exponent k*=τR/[2(x−−6)] satisfies

\[
 k_*\log m_+\le.0085\,\frac Z{e^Z-6.068}<10^{-16},
\]

so m_+^k*<2. The function Z/(e^Z−6.068) decreases for Z≥40, which
justifies evaluating its majorant at 40. For all relevant n,
ell_n≤Z: the positive endpoint is below log(q+) < Z, while the negative
endpoint magnitude is below log[(q++tau/16)/q-] < .02. Hence

\[
 U_n\le\exp\left\{\frac{Z^2/64+.626}{e^Z-6.728}\right\}-1
 \le\exp\left\{\frac{25+.626}{e^{40}-6.728}\right\}-1<10^{-14}.
\]

The displayed rational function decreases on Z≥40: its differentiated
numerator is e^Z[(2Z−Z²)/64−.626]−6.728 Z/32<0. As
p−R/2>2, comparison to the convergent n^-2 series gives

\[
 E_m^{AB}\le10^{-14}\sum_{n\ge1}(1+2n^R)V_n<6\cdot10^{-14}.
\]

For the correction error E_m^C, drop the additional factor q−^-1/4≤1.
Its negative exponent is below −18.7·37/16. Its positive exponent is
bounded by

\[
 \frac{1.24(3^{.068}+3^{-.068})}{10^8-.125}
       +\frac{4Z}{e^Z-12.068}
 \le\frac{1.24(3^{.068}+3^{-.068})}{10^8-.125}
       +\frac{160}{e^{40}-12.068}<1.
\]

Here the second fraction decreases in Z≥40, and its numerator bound
uses 3sqrt(log²q++π²/4)+10.44≤3Z+3π/2+10.44<4Z.
Consequently

\[
 E_m^C<\exp(-18.7\cdot37/16+1)<10^{-17}.
\]

All these bounds hold for every permitted cutoff m, including at natural
cutoff jumps. Changing to fixed N=1 is paid by exactly the sum in (3).
Therefore

\[
 \eta_1<1.9(6\cdot10^{-14}+10^{-17}+2S_0)
 <1.013165306.
\]

The final strict scalar comparison is

\[
 (\eta_1/2)^2+(\eta_1/(2R\omega_*))^2
 <(1.013165306/2)^2+(1.013165306/1.24)^2
 <.924228<1.
\]

This proves (1) at the arbitrary X. Evenness supplies negative x. All
derivatives use the fixed disk's cutoff N=1; no jumping cutoff or
height-dependent choice is differentiated.

### 5. Replay, scope, controls and next route

The companion checker [outer scalar checker](../../numerics/analytic_continuation/certify_outer20_exclusion.py) uses 192-bit Arb arithmetic with a fresh 256-bit replay,
records source and script hashes, checks 25 strict scalar inequalities,
and rejects zero/out-of-domain times and a height below the theorem's
threshold. It does not enumerate m or scan heights. Its result is
[outer scalar record](../../numerics/analytic_continuation/OUTER20_EXCLUSION_20261018.json); the strict pair expression is enclosed below
0.924227400051. All-X coverage comes from the monotonic estimates proved
above, not from interpreting the scalar check as a height sweep.

The exact theta Riemann–Siegel contract is a premise. Finite-prime,
weighted-square, reflected super-Gaussian, positive-primitive,
Euler-factor and counter-kernel controls do not supply the unchanged
normalized theta approximation and its imported error constants. The
leading-pair cosine comparison itself is generic: if a control did
satisfy its complete approximation/error hypotheses on a genuine event,
the strict scalar comparison would necessarily fail. This statement is
an explicit outer estimate for theta, not a new control replay.

At epsilon=1/100, Notes 12–13 plus (1) leave precisely
1001<|x|<exp(2000). The threshold is exponentially smaller than the old
exp(6400), but it does not make direct numerical coverage feasible.
Reducing this coefficient further without a practical change would not
complete Stage 4 or change the shrinking-time signed mechanism. The
next useful route remains an effective many-term signed estimate or a
complete canopy/barrier contract; the existing fixed-cutoff Riemann–Siegel
representation is the relevant analytic consumer. No larger scan follows
from this constant improvement.


## B. Constant-distance arithmetic tails and bounded scalability

### An explicit uniform theorem for distance A/x

Let A,b,X>0 and T,Y>=0. For x>=X set

    d(x)=pi/8-A/x,    m(x)=ceil(sqrt(b*x)),
    G0(x)=x^(7/4)*exp(-pi*x/8).

The integer m is the first **omitted** mode. Derivatives always hold d,m
fixed. Define the following constants at the single onset X:

    v=4A/X,
    kappa=1-v^2/6,             sigma=1-v^2/2,
    M=1+1/sqrt(bX),
    q_*=4*pi*A*kappa*b,       B_*=4q_*-9-Y,
    eta=4*pi*sigma-1/b-T*pi/(4bX).

Assume

    0<v<pi/2, kappa>0, q_*>=1, 8q_*>=T, B_*>0, eta>0.

For any fixed integer j>=0 put

    Qbar_j = sum_{k=0}^j binom(j,k)*(pi/8)^(j-k)*k!/B_*^k,

and define

    C_X = exp(A-q_*)/eta * [
          4*pi^2*M^2*b/sqrt(X)
        + pi*M*sqrt(b)/(2*A*kappa)
        + 1/(16*A^2*kappa^2*sqrt(b))
        + 6*pi/X^(3/2)
        + 3/(4*A*kappa*sqrt(b)*X) ].

Then, for every x>=X, 0<=t<=T and |Im z|<=Y, with Re z=x,

    |partial_z^j(H-Htilde_{m,d})(t,z)| / G0(x)
          <= Qbar_j * C_X * x^(-1/4).                 (CD)

For j=0,1,2 a common bound C_X*x^(-1/4) follows if Qbar_1,Qbar_2<=1.
No geometric-ratio condition is needed for this theorem.

**Proof.** Write c=cos(4d)=sin(4A/x), s=sin(4d)=cos(4A/x), and p=pi*c.
The elementary Taylor inequalities on 0<=4A/x<=v give

    p>=4*pi*A*kappa/x,   s>=sigma,
    q:=p*m^2>=q_*,       sqrt(bx)<=m<=M*sqrt(bx).

In particular `0<d<pi/8`, `B=4q-9-Y>=B_*>0`, and `8q>=T`.
For n>=m one has x<=n^2/b and n^2>=bX. Since `2Td<=T*pi/4`,

    4*pi*s*n^2-x-2Td >= eta*n^2 >0.                 (P)

Thus the hypotheses of Note 11's one-integration-by-parts argument hold
uniformly. Its denominator may be kept mode by mode. The polynomial
factor bound in that proof is Q_j<=Qbar_j, since d<=pi/8 and B>=B_*.
Consequently the normalized error is at most

    exp(A)*x^(-7/4) * Qbar_j/eta *
       sum_{n>=m}(4*pi^2*n^2+6*pi)*exp(-p*n^2).    (G)

For q>=1 the function u^2*exp(-p*u^2) decreases on [m,infinity).
First-term-plus-integral summation and one integration by parts give

    sum_{n>=m} n^2*exp(-p*n^2)
       <= exp(-q)*[m^2+m/(2p)+1/(4p^2*m)],
    sum_{n>=m} exp(-p*n^2)
       <= exp(-q)*[1+1/(2pm)].

The Gaussian integral remainder uses
`int_m^infinity exp(-p*u^2)du <= exp(-q)/(2pm)`.
These are infinite-tail inequalities, not finite numerical summations.
Substituting the preceding bounds on p,m,q into (G) yields

    error_j/G0 <= Qbar_j*exp(A-q_*)/eta*x^(-1/4) * [
          4*pi^2*M^2*b/sqrt(x)
        + pi*M*sqrt(b)/(2*A*kappa)
        + 1/(16*A^2*kappa^2*sqrt(b))
        + 6*pi/x^(3/2)
        + 3/(4*A*kappa*sqrt(b)*x) ].

Every x-dependent term in the bracket decreases for x>=X; replacing them
by their values at X proves (CD). Its right side decreases as x^(-1/4).
This establishes the entire unbounded range from the displayed
inequalities, rather than extrapolating a numerical height table.

### Scalar realization

[constant-distance checker](../../numerics/analytic_continuation/certify_constant_distance_tail.py) and
[scalar record](../../numerics/analytic_continuation/CONSTANT_DISTANCE_TAIL_20261018.json) evaluate the displayed
expressions with python-flint 0.9.0 at 192 bits, with a fresh 256-bit replay. They use only the two
predeclared choices below; no physical field is evaluated.

| A | q_* lower (descriptive) | eta lower | C_X upper (rounded) | Common error/G0 for every x>=1000 |
|---|---:|---:|---:|---:|
| 28 | 43.89034 | 4.48441 | 5.818140e-9 | <1.1e-9 |
| 33 | 51.68574 | 4.45375 | 3.521252e-10 | <7e-11 |

The actual onset evaluations are enclosed below
`1.034627704198514e-9` and `6.261769880014859e-11`.
For A=28, Qbar_1<0.398740 and Qbar_2<0.159030.
For A=33, Qbar_1<0.397782 and Qbar_2<0.158257.
The exact outward expressions, not these descriptive rounded values,
are the consumed scalar proof. T=1/2 and Y=1 include the smaller time
range of Notes 12–13.

The improvement over the old absolute arithmetic-tail estimate is
structural. With p~4*pi*A/x and m~sqrt(bx), its Gaussian S bound is of
order x^(5/2), and B is bounded, so the normalized old absolute bound
is of order x^(3/4). Note 11's positive phase gap supplies a denominator
of order x; the new normalized estimate is of order x^(-1/4).
Thus its nonstationary argument, not a fitted cutoff, removes the log.
The sufficient constant-distance conditions include a lower bound on A*b;
unlike the log-distance family, q no longer tends to infinity automatically.

### Retained enumeration and the outer onset

For either `d=pi/8-4log(x)/x` or `d=pi/8-A/x` with the same mode rule,

    N(x)=m(x)-1=ceil(sqrt(bx))-1,
    sqrt(bx)-1 <= N(x) < sqrt(bx).

The phase-gap premise itself forces

    m^2 > (x+2Td)/(4*pi*sin(4d)) >= x/(4*pi).

It therefore cannot make the explicit retained list sub-square-root by
changing A. At b=1/8 and x=exp(2000), the scalar checker proves

    log10 N(x) > 433.8429369097558.

The current code materializes every lambda_n and loops over every
retained mode inside every quadrature callback. Even constructing the
list, or one integrand callback, therefore entails more than `10^433`
mode operations. This scoped lower bound already prevents this explicit
finite-enumeration code from closing a bridge to that onset. It does not
assume a callback growth law and does not rule out faster theta assembly.
At the older inherited onset exp(6400), the same count is still larger.

### Source domain growth and what U=2 cannot pay

For the n=1 retained-source tangent, even its weakest j=0,Y=0 premise
requires `4*c*pi*exp(4U)>9`. For the constant-distance family, c<=4A/x,
so necessarily

    U > (log x)/4 + (1/4)*log[9/(16*pi*A)].        (U0)

At x=exp(2000), A=33, the checker gives U>498.69584960.
For the log-distance family c<=16log(x)/x, the analogous necessary bound
is `U>log(x)/4+log[9/(64*pi*log x)]/4`, giving U>497.32317728 there.
These are premises of the existing source-tail payment, not lower bounds
on the true oscillatory tail.

The actual D condition includes `9+Y+2TU+j/(U+d)`, making it stronger.
At U=2, T=1/5,Y=1,j=0, the log-distance D obeys

    D <= 64*pi*exp(8)*log(x)/x -10.8.

For x>=10^6 this is negative: use pi<22/7, exp(8)<3000,
log(10^6)<14 and monotonic decrease of log(x)/x to bound the first
term by 8.448. For constant A<=33 it is at most
`16*pi*A*exp(8)/x-10.8`, also negative on that range.
Thus U=2 is rigorously inadmissible there under the current tangent
payment, independently of any physical margin.

### The fixed polynomial consumer is also bounded in scope

Its common moment is a positive absolute majorant. For constant A, an
explicit lower bound shows why fixed degree 24 cannot be kept forever.
Assume U>=1/4, `A*b>=1/(pi*e)`, `b*x>=4`, and
`x>=64*pi*A*e`. Put R=sqrt[x/(4*pi*A*e)]>=4. All integers n<=floor(R)
are retained, because R<=sqrt(bx)/2<=m-1. On 0<=u<=1/4,
`pi*c*n^2*exp(4u)<=1`. At least the upper half of these n satisfy

    sum n^4 >= R^5/1024.

Using only their `2*pi^2*n^4` coefficient, time/source factors >=1,
and `1+(u+d)^J>=1`, the normalized positive common moment obeys

    M_J >= [pi^2*exp(A-1)/(2048*(4*pi*A*e)^(5/2))]
               * x^(3/4).                          (M0)

This holds for every J>=0. The scalar factor may be small or large; it is
fixed and positive. At the y=1 end of a wall expanded about real z=x,
the spatial radius remains R_space=1 even after subdividing y cells.
The displayed degree-24 majorant payment contains M_52/25!, so (M0)
forces that G0-relative payment to diverge and eventually exceed the fixed
1e-8 component allowance. This does not prove failure against a growing
physical-envelope margin allowance. More subdivision with the same midpoint
and degrees cannot fix it. Raising degrees or recentering and obtaining
new certified jets would be additional work; the claim is about the
current payment and cache, not impossibility of whole-cell methods.

For log distance the same argument with A=4log x gives a lower bound
of order `x^(19/4)/(log x)^(5/2)`. Positive time can make the actual
majorant larger still; no estimate of actual callback cost is inferred
from those bounds.

### What remains a missing consumer

The constant-distance theorem supplies a uniform approximation error.
It gives neither a lower bound for H nor a signed first-jet inequality,
and it does not discharge the complex-wall margin at new heights.
The seven-cell wall of Note 13 remains the only wall produced here.

The finite propagation lemma also requires initial reality throughout
the entire interior of a proposed new wall. The verified input used in
Note 13 does not automatically become initial verification up to a newly
chosen enormous X. Wall certificates alone cannot silently enlarge that
initial-data hypothesis. An outer eventual-exclusion theorem is a
different input with its own scope and seams.

Consequently a scan extension is not justified. The useful analytic gain
is the explicit constant-distance arithmetic theorem. A complete bridge
would require a new physical signed/exterior estimate or a representation
and consumer that avoids the explicit square-root enumeration, alongside
all required initial and boundary contracts. This draft does not claim
such a bridge or a global Newman bound.


## C. Global route and adversarial scope

### A complete quantitative canopy ledger

Polymath Theorem 1.2 has parameters `t0,X>0`, `0<y0<=1`. Its initial
condition excludes zeta zeros at `sigma>=(1+y0)/2`, `0<=Im s<=X/2`.
Its final exterior is

`x>=X+sqrt(1-y0^2), y0<=y<=sqrt(1-2t0)` at `t=t0`.

Its moving barrier is

`X<=x<=X+sqrt(1-y0^2), sqrt(y0^2+2(t0-t))<=y<=sqrt(1-2t)`
for every `0<=t<=t0`. Its conclusion is `Lambda<=t0+y0^2/2`.

Choose `0<t0<=1/5`, `0<y0<=1` and

`X=1000-sqrt(1-y0^2)>999`.

Then:

* Initial verification follows from Platt–Trudgian Theorem 1, needing
  height only `X/2<500`, far below its verified range.
* The entire moving barrier lies inside `999<x<=1000`. Note 13 proves
  every zero there real for `0<t<=1/5`; at `t=0` the initial verification
  applies. Since the moving barrier's lower imaginary height is at least
  `y0>0`, it is zero-free, including the final endpoint and seams.
* The final exterior begins exactly at `x=1000`. The wall includes that
  seam. The missing statement is zero-freeness of the complete theta field
  for **every** `x>1000`, `y0<=y<=sqrt(1-2t0)` at `t=t0`.

For a concrete falsifiable contract, take `t0=1/10`, `y0=2/5`,
`X=1000-sqrt(21)/5`. The conditional conclusion is `Lambda<=9/50=0.18`.
Everything except the final exterior is supplied by the present finite
theorem and named published inputs. The remaining region is exactly

`x>1000, 2/5<=y<=sqrt(4/5), t=1/10`.

This is a scenario, not an earned upper bound. No scan or new target
decimal is authorized merely by displaying this exact contract.

The strip `|Im z|<=sqrt(1-2t0)` gives no exclusion inside that region.
Making the region empty by choosing `y0>sqrt(1-2t0)` forces
`t0+y0^2/2>1/2`. At equality the closed boundary still needs exclusion;
even if excluded, the resulting bound is only `1/2`. Reusing the global
published `Lambda<=1/5` at `t0=1/5` supplies final-time exterior
nonvanishing, but then the conclusion is `1/5+y0^2/2>1/5`. Taking a
limit recovers the inherited baseline and does not improve it.

### Why the new arithmetic tail does not fill that premise

Note 11 bounds the omitted modes after the complete reflected contour
has been shifted. It does not give a lower bound for the retained sum.
Those retained modes include real stationary points whenever
`n^2<x/(4*pi)`; they carry the complete arithmetic cancellation. The
nonstationary omitted-mode proof cannot be applied to them, since its
phase-gap hypothesis then fails. The existing absolute tail remains
valid, but no absolute upper bound for a remainder supplies the missing
signed or nonvanishing estimate for the retained field.

The sharpened real first-jet exterior beginning at `exp(2000)` is
real-axis collision exclusion, not automatically the whole final-time
complex exterior needed by this canopy ledger. Where a stronger imported
outer theorem is used, its exact imaginary range and time must be stated.
In particular, the effective-probe appendix at `x>=10^16`, `1/5<=t<=3/10`
and one disk around `y=9/10` does not cover the above final exterior at
`t0=1/10`, `2/5<=y<=sqrt(4/5)`.

### Exact remote polynomial control

Let `L=2000`, `q=2/5`, and

`F_0(z)=((z-L)^2+q)((z+L)^2+q)`.

Its exact backward heat evolution is

`F_t(z)=z^4-2A(t)z^2+B(t)`,

where

`A(t)=L^2-q+6t`,

`B(t)=(L^2+q)^2+4t(L^2-q)+12t^2`.

Coefficient differentiation proves `partial_t F=-partial_z^2 F`.
It is even, real, entire of order at most one, and

`F_t(iy)=y^4+2A(t)y^2+B(t)>0`

for all real `y` and `0<=t<=1/5`.

Put `f(t)=6t^2+2(L^2-q)t-L^2q`. Then

`A(t)^2-B(t)=4f(t)`.

The polynomial `f` increases strictly for `t>=0`. Its positive root is

`lambda_L = (sqrt((L^2-q)^2+6L^2q)-(L^2-q))/6`.

Before that time the four roots form two nonreal conjugate pairs; at that
time they are two real double roots; afterwards all four roots are real.
Thus this polynomial family's all-real threshold is exactly `lambda_L`.
Exact rational evaluation gives

`1/5-1/L^2 < lambda_L < 1/5`,

and the tighter interval

`0.1999999875 < lambda_L < 0.19999999375`.

In particular it is all-real at the inherited baseline time `1/5` and
still has nonreal zeros at `1/100`. As `L` grows its threshold tends to
`1/5` from below.

All roots remain beyond `|Re z|>1400` throughout `0<=t<=1/5`. Indeed,
when `f(t)<0`, their real parts squared are
`(sqrt(B)+A)/2>=A(0)/2>1400^2`. When `f(t)>=0`, the roots are real,
and `4f(t)<=4f(1/5)=8/25<1`, so their squared absolute values are at
least `A(0)-1>1400^2`. This proves no zero on the entire wall
`Re z=1000`, for any imaginary height, and no zero anywhere in the
finite real region `|x|<=1001`. It gives the explicit uniform bounds
`|F(t,1000+iy)|>400^4` and `|F(t,x)|>399^4` for `|x|<=1001`.

The control also obeys the contracted initial strip. For its nonreal
roots, `b(t)^2=(sqrt(B)-A)/2`, while

`(L^2+q+2t)^2-B(t)=8t(q-t)>=0`

up to the threshold. Hence `b(t)^2<=q-2t<=1-2t`; after the threshold
all roots are real. Its initial zeros `+/-L+/-i*sqrt(q)` lie outside
the verified finite region. It therefore satisfies the finite propagation
lemma's initial and boundary premises, unit strip, imaginary-axis
positivity, evenness, and the all-real time `1/5`, yet its global threshold
is close to `1/5`, not `1/100`.

It also satisfies the newly sharpened real-jet exterior exclusion itself:
every root stays in `|z|<3000` through `0<=t<=1/2`, so no real common zero
can lie beyond `exp(20/epsilon)>=exp(40)>3000`. To verify the root bound,
use monotonicity of `A,B,f` for nonnegative t. If `f<0`, then
`|z|^4=B(t)<=B(1/2)<3000^4`; if `f>=0`, then
`z^2<=A(1/2)+sqrt(4f(1/2))<A(1/2)+4000<3000^2`.
Thus its positive-time collisions occur entirely in the remaining finite
bridge, even when that exterior conclusion is added to the tested premises.

For the variable-L family, the finite-wall, strip and all-real-baseline
premises alone admit thresholds arbitrarily close to 1/5. The new exterior
conclusion is not uniformly imposed as L tends to infinity. For the fixed
L=2000 control, even adding that exterior conclusion does not imply
Lambda<=1/100: its remote collision lies inside the uncovered bridge. It is **not** a theta collision control:
it lacks the complete normalized theta square source. It also fails
`L0>E/100` at `(t,x)=(1/100,1000)`, as the exact checker confirms; no
obstruction is asserted for an argument using that stronger signed
information quantitatively outside its certified box.

The alternative `q=1/4` has a threshold near `1/8`, still above `1/100`
and below `1/5`. The main `q=2/5` choice is sharper because it approaches
the inherited baseline itself.

### Next admissible research gate

The genuinely missing output is a complete-field final-time exterior
estimate with explicit height, strict margin and every remainder payment,
or an independently justified arithmetic lower bound strong enough to
supply it. A bounded test can assess that lower-bound mechanism; the
height-1000 wall and omitted-mode tail alone cannot be counted as one.
For a proposed source-specific estimate, keep the existing weighted,
reflected, primitive and Euler-factor screens, naming their missing theta
premises. Use the remote polynomial above specifically to challenge any
step that relies only on finite E coverage and the global strip/baseline.

The [remote-control checker](../../numerics/analytic_continuation/check_remote_polynomial_control.py) is a pure standard-library exact-rational checker
of the heat identity, threshold brackets, all-time root location, strip
identity, positive imaginary-axis coefficients, and the explicitly failed
signed D1 premise. Decimal endpoints in its report are display only.

Primary sources freshly checked on 18 October 2026:

* [Polymath, Theorem 1.2 and Section 3](https://arxiv.org/html/1904.12438v2):
  exact canopy regions; Proposition 3.1 local splitting; Theorem 3.2 strip
  contraction.
* [Platt–Trudgian, Theorem 1](https://arxiv.org/pdf/2004.09765): initial
  verification through height 3,000,175,332,800; Section 3.4 gives the
  inherited global baseline 1/5.


## Final disposition

The new outer estimate is consumed in the slab coverage ledger, with the
finite/outer equality endpoint included. Evenness supplies the negative
side. The central finite cover and its overlaps are unchanged. The open
bridge is (1001,exp(2000)) on [1/100,1/5], and the alternative canopy still
lacks its full final-time complex exterior. A real collision-exclusion
theorem is not silently promoted to that complex nonvanishing hypothesis.

The current explicit-mode evaluator cannot feasibly enumerate its retained
modes at the new outer onset. The narrowed gap is not a reason to launch a
height scan or optimize more scalar constants without changing feasibility.
The next research input must be an independently proved many-term physical
signed estimate or an effective complex exterior for the canopy, together
with a consumer that pays every remainder. These are missing research
inputs, not additional names for an established conclusion.

The [analytic replay record][replay] binds the new source bytes, 192/256-bit
scalar checks, exact polynomial check, complete declared domains and
measured bounded execution cost. [Review 12][review] records independent
same-model proof checks and the limits of these certificates. The bounded
continuation closes at this auxiliary milestone; **Stage 4 remains open**.

[plan]: ../../research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md
[summary]: ../../research-progress/03_OVERVIEW02_ROUND_SUMMARY_20261018.md
[summaries]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[target]: ../../../../../avoid/01_restating_the_target.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[pairing]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[ledger]: ../../numerics/analytic_continuation/GLOBAL_ANALYTIC_CONTINUATION_LEDGER_20261018.json
[replay]: ../../numerics/analytic_continuation/ANALYTIC_CONTINUATION_REPLAY_20261018.json
[review]: ../../reviews/12_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_REVIEW_20261018.md
