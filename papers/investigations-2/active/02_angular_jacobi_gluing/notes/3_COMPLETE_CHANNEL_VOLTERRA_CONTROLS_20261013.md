# Complete-channel Volterra reduction and stationary-sign controls

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: `gpt-6-astra` (Codex); reasoning effort **ultra**.
This is an internal analytic continuation, not independent validation.
It follows the [complete elliptic insertion](ELLIPTIC_INSERTION_TRANSPORT_AND_HEAT_OBSTRUCTIONS_20261013.md)
and the [source-rigidity controls](ANGULAR_GLUING_AND_RIGIDITY_REVIEW_SEEDS_20261013.md).
The companion [positive-anchor continuation](2_VOLTERRA_RECOVERY_POSITIVE_ANCHOR_AND_TRANSFER_GAP_20261013.md)
gives the explicit genuine lower bound and complete recovery operators;
the focus here is what those scalar inputs can and cannot imply.

The positive correction in the short-period identity has an exact
Volterra description. Its positivity, decreasing and convex source,
and a strictly positive Fourier transform do not by themselves imply
either required stationary sign. This note proves that failure using
two explicit source families and, more sharply, proves that the earlier
arbitrarily close theta perturbations with remote collisions retain
the positive correction channel on the full interval `0<=t<=1`.
Those controls do not preserve the genuine imaginary elliptic law.
The remaining input must use that law quantitatively.

## 1. The complete correction as a positive Volterra operator

At angular coordinate zero, the exact short-period projection is

\[
\mathscr A_t(x)=H_t(x)-P_t(x),\qquad
P_t(x)=\int_0^\infty e^{tu^2}R(u)\cos(xu)\,du,
\]
\[
R(u)=2\pi^2e^u\sum_{n\ge1}n^2e^{-\pi n^2e^{4u}}>0,
\qquad u\ge0.
\tag{1}
\]

Direct differentiation of the complete theta series gives

\[
R'+5R=-4\pi e^{-4u}\Phi(u).
\]

The rapid-decay boundary condition at infinity determines the solution:

\[
\boxed{R(u)=4\pi e^{-5u}\int_u^\infty e^v\Phi(v)\,dv.}
\tag{2}
\]

In particular this scalar relation is not exclusive to theta. For any
positive even smooth source `psi` with the needed decay, define `R_psi`
by (2) with `Phi` replaced by `psi`. The same first-order relation and
the scalar identity `A_psi=H_psi-P_psi` then hold. This construction
does not manufacture an angular lift obeying both elliptic laws.

The adjoint formula makes the entire correction explicit as a linear
observation of the physical source. If `f_t(v)=exp(tv²)psi(v)`, then

\[
P_{\psi,t}(x)=\int_0^\infty f_t(v)\,\mathcal V_t(v,x)\,dv,
\quad
\mathcal V_t(v,x)=4\pi e^{v-tv^2}
          \int_0^v e^{tu^2-5u}\cos(xu)\,du.
\tag{3}
\]

All integrals and exchanges are absolutely convergent for the genuine
source and the super-Gaussian controls below, uniformly on compact
complex `t,x` sets. Differentiating the inner cosine supplies the exact
kernel for each frequency derivative. This is an actual adjoint kernel,
not an assumed positive Fourier multiplier: its cosine factor changes
sign.

At `t=0`, put `E(x)=int exp(-4u)psi(u)cos(xu)du` and
`F(x)=int exp(-4u)psi(u)sin(xu)du`, both on the positive half-line.
Evaluation of the inner integral gives

\[
\boxed{P_{\psi,0}(x)=
 \frac{5R_\psi(0)-20\pi E(x)+4\pi xF(x)}{25+x^2}.}
\tag{4}
\]

The `R_psi(0)` endpoint is essential. The two oscillatory terms in (4)
cannot be discarded when bounding the complete observation.

## 2. A general criterion for a positive Fourier correction

Let `r_t(u)=exp(tu²)R_psi(u)`. Differentiating (2) twice gives

\[
r_t''=e^{tu^2}\left\{
 [(2tu-5)^2+2t]R_\psi
 +4\pi e^{-4u}[(9-4tu)\psi-\psi']\right\}.
\tag{5}
\]

Consequently, for `t>=0`, the sufficient source condition

\[
\psi'(u)/\psi(u)<9-4tu\qquad(u\ge0)
\tag{6}
\]

implies `r_t''>0`. With rapid decay at infinity this also implies
`r_t'<0`. Two integrations by parts give the useful exact formula

\[
\boxed{P_{\psi,t}(x)=\frac1{x^2}
 \int_0^\infty r_t''(u)\{1-\cos(xu)\}\,du>0,
 \qquad x\ne0.}
\tag{7}
\]

At zero, positivity follows directly from (1). Formula (7) proves
pointwise positivity of this particular Fourier transform; positivity
of `R_psi` alone would not do so.

The genuine source meets (6) on `0<=t<=1`. For a single positive theta
summand and `q=pi n²e^{4u}`, its logarithmic derivative is

\[
9+\frac{12}{2q-3}-4q\le13-4\pi e^{4u}.
\tag{8}
\]

The logarithmic derivative of the positive sum is a weighted average
of these quantities. The displayed bound implies (6) uniformly on
that time interval. Thus the auxiliary short-period channel can safely
be normalized by `P_t` on the real spectral axis. The normalization
does not by itself supply a sign or a physical value-and-slope bound.

## 3. Exact nearby collisions retain the positive correction

Choose a time `0<T<1`. The earlier rigidity note constructs, for all
sufficiently large `X`, a positive source

\[
\psi_X(u)=s_X\Phi_e(u)W_X(u),\qquad
W_X(u)=1+a_X\cos((X-d)u)+b_X\cos((X+d)u),
\tag{9}
\]

whose heat transform satisfies `H_{psi_X,T}(X)=H'_{psi_X,T}(X)=0`.
Here `d>0` is fixed and small, `s_X>0` supplies the original positive
normalization, and `a_X,b_X` solve the explicit two-by-two system in
that note. Its limiting matrix is invertible. The genuine heat
transform and its derivatives are Schwartz, so for every fixed `N`,

\[
|a_X|+|b_X|=O_N(X^{-N}).
\tag{10}
\]

Define

\[
\varepsilon_X=|a_X|+|b_X|,\qquad
\nu_X=\frac{|a_X|(X-d)+|b_X|(X+d)}{1-\varepsilon_X}.
\]

For large `X`, `epsilon_X<1` and `nu_X<=1`. Since
`|W_X'/W_X|<=nu_X`, (8) gives

\[
\frac{\psi_X'}{\psi_X}\le14-4\pi e^{4u}.
\tag{11}
\]

Uniformly for `0<=t<=1`, write `E=e^{4u}` and use `4u<=E-1` to obtain

\[
9-4tu-\frac{\psi_X'}{\psi_X}
\ge4\pi E-4u-5
\ge(4\pi-1)E-4>0.
\tag{12}
\]

Thus (5)-(7) prove

\[
R_{\psi_X}>0,\qquad r_{\psi_X,t}'<0,
\qquad r_{\psi_X,t}''>0,
\qquad P_{\psi_X,t}(x)>0
\tag{13}
\]

for every real `x` and `0<=t<=1`, while the physical transform has the
exact joint zero specified above. The sources tend to genuine theta
in relative supremum norm. Their fixed-order source derivatives also
have vanishing modulation errors because of (10).

Even the numerical constant in the genuine positive-anchor estimate can
be retained. On `0<=u<=1/10`, the sources and their first derivatives
converge uniformly to `Phi,Phi'`. The Volterra corrections converge there
as well, since `s_X W_X` tends uniformly to one on the full real axis.
Formula (5) therefore gives uniform convergence of `r_{psi_X,t}''` to
`r_t''` on this source interval and `0<=t<=1`. The companion note proves
the genuine lower bound `r_t''>146/27>5` there. For sufficiently large
`X`, the perturbed curvature is consequently still greater than 5.
The same integral argument then gives
`P_{psi_X,t}(x)>1/[3000(1+x²)]` for all real `x` and `0<=t<=1`.
This statement has no effective displacement threshold; it is part of
the analytic control construction, not an additional numerical certificate.

This is a direct obstruction to inferring physical nonvanishing from
the positive correction, the Volterra law, scalar reflection, and
arbitrarily close real-axis source data. It is an existence construction
with sufficiently large `X`, not a certified numerical collision.
The perturbed sources do **not** obey the genuine imaginary elliptic
law. Nor does a joint zero at time `T` alone imply that one of the two
stationary inequalities is strictly wrong at that same time. The next
section supplies separate direct controls for those two inequalities.

## 4. Each stationary sign can fail inside the same scalar class

These examples use only elementary Gaussian transforms. A small
super-Gaussian factor then gives all heat moments without changing
the strict signs. They are source controls, not theta counterexamples.

### First stationary sign

Start with

\[
\psi_0(u)=e^{-u^2}\{1+\tfrac12\cos(8u)\}>0.
\]

Apart from the positive constant `sqrt(pi)/2`, its time-zero transform is

\[
h(x)=e^{-x^2/4}+\tfrac14e^{-(x-8)^2/4}
                         +\tfrac14e^{-(x+8)^2/4}>0.
\tag{14}
\]

On the whole interval `[2,6]`, each of the three Gaussian terms has
strictly positive second derivative, because its distance from its
center is at least 2. Also

\[
h'(2)=-e^{-1}+\tfrac34e^{-9}-\tfrac54e^{-25}<0,
\]
\[
h'(6)=-3e^{-9}+\tfrac14e^{-1}-\tfrac74e^{-49}>0.
\]

There is a unique `x_*` in `(2,6)` with `h'(x_*)=0`, and there

\[
L_0(h;x_*)=-h(x_*)h''(x_*)<0.
\tag{15}
\]

For any sufficiently small fixed `epsilon>0`, replace the source by
`psi_epsilon=exp(-epsilon u^4)psi_0`. The transform and its first
three derivatives converge uniformly on compact frequency intervals
as `epsilon` decreases to zero. The strict endpoint and curvature
bounds above therefore survive. The new source admits every Gaussian
heat weight. Moreover

\[
\psi_\epsilon'/\psi_\epsilon
\le8-2u-4\epsilon u^3.
\]

Equations (5)-(7) give a positive Fourier correction on the entire
interval `0<=t<=1/2`. The strict wrong stationary sign persists for
some positive times by the implicit function theorem. This last
assertion is non-effective; no numerical time radius is claimed.

### Second stationary sign

Start instead with

\[
\psi_0(u)=e^{-u^2}
 +\frac3{1000}e^{-u^2/100}\{1+\tfrac12\cos(4u)\}>0.
\]

After division by the same positive constant `sqrt(pi)/2`, its
transform is

\[
h(x)=e^{-x^2/4}+\frac3{100}e^{-25x^2}
 +\frac3{400}\{e^{-25(x-4)^2}+e^{-25(x+4)^2}\}.
\tag{16}
\]

On `I=[19/5,4]`, all the terms have negative third derivative: the
wide Gaussian has `x>sqrt(6)`; the narrow centered and far-left
Gaussians are on their far positive tails; and the right-hand bump
has displacement in `[-1/5,0]`, where its third derivative is
nonpositive. The other terms keep the sum strictly negative at the
endpoint with displacement zero. Thus `h'''<0` on `I`.

At `19/5` all four second derivatives are positive. At 4 the
right-hand bump contributes `-3/8`; the broad contribution is
`(7/2)e^{-4}<7/32`, and the two remaining positive contributions
are less than `1/100`. Consequently `h''(4)<0`. The harmless last
bound follows directly from their factors `e^{-400}` and `e^{-1600}`.
There is a unique `y_*` in `(19/5,4)` with `h''(y_*)=0`.

The broad first derivative is at most `-2e^{-4}` on `I`. The only
positive contribution is from the nearby narrow bump, whose maximum is
`3/(40 sqrt(2e))`. The elementary inequality

\[
\frac3{40\sqrt{2e}}<2e^{-4}
\tag{17}
\]

holds, for example by squaring and using `e<11/4`. All other first
derivatives are negative. Hence `h'<0` throughout `I`, and

\[
L_1(h;y_*)=-h'(y_*)h'''(y_*)<0.
\tag{18}
\]

Again multiply the source by `exp(-epsilon u^4)` for sufficiently
small positive `epsilon`. All strict signs survive, while the source
acquires every heat moment. The logarithmic derivative of each
positive component is at most `4-u/50-4epsilon u³`, so the same
is true of their sum. Conditions (5)-(7) hold throughout
`0<=t<=1/200`. The wrong second stationary sign again persists
for some positive times. No effective choice of `epsilon` or time
radius is asserted; compact uniform convergence and nonzero stationary
derivatives prove their existence.

Thus even a positive Fourier correction obtained from a decreasing,
strictly convex Volterra source does not imply either stationary sign.

## 5. The exact complete inequality, and what would be new

For the genuine source and `0<=t<=1`, `P_t>0` permits the real-axis
definitions

\[
Y=\frac{H}{P}=1+\frac{\mathscr A}{P},\qquad
p=\frac{P'}P,\qquad Z=Y'+pY=\frac{H'}P.
\]

The exact identities are

\[
\frac{L_0(H)}{P^2}=Y'^2-YY''-p'Y^2,\qquad
\frac{L_1(H)}{P^2}=Z'^2-ZZ''-p'Z^2.
\tag{19}
\]

The two physical stationary sets are `Y'+pY=0` and `Z'+pZ=0`.
Accordingly the needed bounds become

\[
Y'^2-YY''\ge p'Y^2\quad\text{when }Y'+pY=0,
\]
\[
Z'^2-ZZ''\ge p'Z^2\quad\text{when }Z'+pZ=0.
\tag{20}
\]

These are exact normalization formulas, **not new inequalities already
proved**. Merely renaming (20) an angular observation theorem would
restate the old missing input. The controls in Sections 3-4 prove that
the scalar Volterra law and correction positivity cannot establish
it. Likewise expanding `L_j(A+P)` gives a cross-channel balance
equivalent to the same target, rather than an independent bound.

A concrete next research question is whether the **full imaginary
elliptic shift law**, including its transported insertion and endpoint
terms, admits a convergent adjoint multiplier identity whose physical
projection is either left side of (19), with nonnegative residual and
only a multiple of the relevant stationary equation left over. The
identity must use the integer coefficient relation `c_n=c_{n+1}`;
an argument using only (2), (5), or the scalar angular-jet dictionary
would also apply to the controls and is therefore insufficient.
Its multiplier, domain, endpoint payment and infinite-sum remainder
must be explicit before positivity is inferred. This identifies a
specific missing construction rather than announcing a new sign theorem.
