# One-sided sign tests: a quantitative zero obstruction and positive averaging

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not inferred. Internal analytical work,
not independent specialist refereeing. No global exponent or new prime
estimate is established; no priority claim is made.

## Outcome

This note tests two possible shortcuts to the one-sided scalar target:
positivity of its transform on the real axis, and fixed positive averaging
of the prepared kernel. Neither supplies the required sign inequality.
The obstruction can be quantified: a single hypothetical zero to the
right of the critical line forces both positive and negative scalar
excursions with an explicit nonzero lower amplitude. No rightmost zero
is assumed.

The main arithmetic attack is developed separately in the
[prime-discrepancy centering note](PRIME_DISCREPANCY_CENTERING_20261004.md).
These sign tests explain which analytic properties that remaining signed
integral would need beyond known real-axis or scalar-kernel positivity.

## 1. A quantitative necessary sign balance

Use the [scalar detector](SCALAR_DETECTOR_20261004.md):

\[
\lambda_V(X)=\frac{\int_X^{2X}xV_g(x)dx}{qX^3},\quad q=7/3,
\quad S(X)=X\lambda_V(X),
\]
\[
D(z)=\frac1qG(1/2-z)\frac{2^{z+2}-1}{z+2},\qquad
\int_0^\infty e^{-zt}S(e^t)dt
=-D(z)\frac{\zeta'}{\zeta}(z)-C_0(z),\quad\Re z>1.
\tag{1}
\]

The compact initial cap C_0 is entire. Preparation removes the pole
at one. At a nontrivial zero rho=beta+i gamma with beta>1/2 and
multiplicity m, D(rho) is nonzero and the residue in (1) is −mD(rho).
There are no nontrivial real zeros, so gamma is nonzero.

**Conditional oscillation statement.** If such a zero exists, then

\[
\boxed{\begin{aligned}
\limsup_{X\to\infty}X^{1-\beta}\lambda_V(X)&\ge m|D(\rho)|,\\
\liminf_{X\to\infty}X^{1-\beta}\lambda_V(X)&\le-m|D(\rho)|.
\end{aligned}}                                                    \tag{2}
\]

The limits are understood in the extended real sense. This is a
conditional consequence of a hypothetical zero, not evidence for one.

For the first inequality, suppose an eventual envelope
S(e^t)<=c e^(beta t) holds with 0<=c<m|D(rho)|. Choose t_0 so the
function f(t)=1_(t>=t_0)[c e^(beta t)−S(e^t)] is nonnegative.
The Landau argument already proved for the scalar detector gives
absolute Laplace convergence of f throughout Re z>beta. Its real
convergence abscissa cannot exceed beta because its meromorphic
continuation has no real singularity above beta. This step does not
assume that rho is a rightmost zero.

Write F for that true Laplace transform. For real sigma>beta,
nonnegativity gives the elementary inequality

\[
|F(\sigma+i\gamma)|\le F(\sigma).
\tag{3}
\]

The meromorphic expression for F is
c e^(-(z−beta)t_0)/(z−beta) minus the transform in (1), plus an
entire initial correction. Therefore

\[
\lim_{\sigma\downarrow\beta}(\sigma-\beta)F(\sigma)=c,
\qquad
\lim_{\sigma\downarrow\beta}(\sigma-\beta)
F(\sigma+i\gamma)=mD(\rho).
\tag{4}
\]

The first limit uses holomorphy of the scalar transform near the positive
real point beta. In the second limit the artificial pole at beta is
regular at beta+i gamma, and the zero's simple pole supplies the displayed
residue. Multiplying (3) by sigma−beta contradicts c<m|D(rho)|.
If the first limsup in (2) were smaller than m|D(rho)|, one could choose
such a nonnegative c above that limsup. The lower statement follows
from the analogous nonnegative tail c e^(beta t)+S(e^t). QED.

For the complete centered Vaughan scalar J, the established error
J−lambda_V=O(X^−1/2) disappears after multiplication by X^(1−beta),
so (2) holds for J for every beta>1/2. For the prime-inner scalar J_0,
the available error is O(X^−11/48 log X); thus the same amplitudes
transfer when beta>37/48. This includes every forbidden zero for the
current first-saving target kappa<11/24.

The extra shell-averaging multiplier satisfies
K(beta+i gamma)=O_beta((1+|gamma|)^−1), while the fixed probe has
G(1/2−beta−i gamma)=O_beta((1+|gamma|)^−6). Hence
|D(rho)|=O_beta((1+|gamma|)^−7). The constant in (2) is nonzero,
but this upper decay estimate gives no useful lower bound or effective
first-excursion scale. Finite sign samples cannot rule out a distant,
small-amplitude oscillatory obstruction.

## 2. Real-axis transform positivity does not imply a one-sided bound

Analyticity near every real z>b is an ingredient in the conditional
Landau argument. It does not construct the required nonnegative tail.
A concrete test function makes the distinction explicit. For
1/2<beta<1 and gamma nonzero, set

\[
g(t)=e^{\beta t}\cos(\gamma t),\qquad
\int_0^\infty e^{-zt}g(t)dt
=\frac{z-\beta}{(z-\beta)^2+\gamma^2},\quad\Re z>\beta.
\tag{5}
\]

Its transform is positive at every real z>1 and admits meromorphic
continuation holomorphic near the whole real axis. Nevertheless g
changes sign with size e^(beta t) and violates either eventual envelope
C e^(bt) for every b<beta. The obstruction lies at the two nonreal poles.
Thus checking a real-axis sign, or merely the absence of a real pole,
cannot prove the desired one-sided arithmetic bound.

This is a test of that inference, not a counterexample involving actual
primes. Positivity of a true inverse transform or a justified positive
representation would be substantially stronger. Treating it as already
available would assume the missing sign information.

## 3. Fixed positive averaging preserves the signed-kernel problem

Let nu be a nonzero finite positive measure on a fixed compact real
interval, independent of X. Define a positive log-scale average and its
physical kernel by

\[
S_\nu(X)=\int S(e^vX)d\nu(v),\qquad
\ell_\nu(u)=\int\ell(ue^{-v})d\nu(v),\qquad
K_\nu(z)=\int e^{zv}d\nu(v).
\tag{6}
\]

The complete multiplicative transform is exactly
−D(z)K_nu(z) zeta'/zeta(z), initially for Re z>1. Any use of a
one-sided logarithmic transform must again retain its finite initial cap.
The fixed compact shifts change that cap but not pole detection.

By the preparation and log moment of ell,

\[
\int\ell_\nu(u)du=0,\qquad
\int\ell_\nu(u)\log u\,du=q c_w K_\nu(1)\ne0.
\tag{7}
\]

Here K_nu(1)>0. Thus ell_nu is a nonzero continuous compactly supported
kernel with zero integral; it necessarily has both signs. No such
positive average turns this prepared arithmetic probe into a pointwise
nonnegative weight. Taking positive or negative lobes separately still
destroys the zero-density cancellation.

A fixed positive measure need not have a zero-free multiplier in the
right half-plane. For example nu=delta_0+c delta_h, 0<c<1, h>0,
has K_nu(z)=1+c e^(hz), with zeros on
Re z=log(1/c)/h. If a proposed filter cancels a hypothetical forbidden
zero this way, it has lost that detector and cannot retain the full
criterion without another covering filter.

An explicit detector-preserving family is
\(d\nu(v)=e^{av}\mathbf1_{[0,h]}(v)\,dv\), with a>=0 and h>0. Then

\[
K_\nu(z)=\frac{e^{h(z+a)}-1}{z+a},
\tag{8}
\]

whose zeros are z=−a+2 pi i n/h for nonzero integers n; z=−a is
removable and has value h. All forbidden zeros therefore survive, and
the same proof as (2) gives forced positive and negative excursions of
S_nu(X)/X with amplitude at least m|D(rho)K_nu(rho)|. Its one-sided
fixed-power bound is another equivalent target, still unproved.

This does not rule out every useful averaging construction. It shows
that fixed positive smoothing alone neither makes the prepared kernel
nonnegative nor neutralizes a forbidden pole while keeping the same
single-detector criterion. X-dependent averaging would need a new support,
normalization and transfer proof; (6) cannot silently be reused for it.

There is also no fixed pointwise-kernel majorant with a free density
budget. If a continuous h compactly supported in (0,infinity) satisfies h>=ell and is
not identical to ell, then
\(\int h=\int(h-\ell)>0\). The ordinary weighted PNT gives
\[
\frac1{qX}\sum_n\Lambda(n)h(n/X)\longrightarrow\frac1q\int h>0.
\tag{9}
\]
Thus the resulting valid upper bound for lambda_V does not decay at a
fixed power, or even tend to zero. A majorant with the same zero integral
must equal ell. The lower-minorant statement is identical with signs
reversed. This concerns a fixed pointwise replacement, not every signed
majorant method. An X-dependent replacement would have to charge its
integrated excess at the target scale and control its increasing
complexity; the fixed-kernel argument supplies neither estimate.

## 4. Consequence for the active arithmetic attempt

The remaining signed prime-discrepancy integral needs an actual estimate
using its coefficients. Real-axis regularity and a positive smoothing
operator do not supply one. For the present kernel, a future one-sided
arithmetic proof must be strong enough to exclude the two-sided excursions
(2) of every hypothetical forbidden zero. The current centering removes
the deterministic density and endpoint costs; it does not justify
positivity of the residual measure or its kernel.

Verification: the residue limits, cap treatment, envelope-to-Landau step,
the generic cosine transform, both kernel moments and the two multiplier
zero sets were checked algebraically. No numerical sign certificate or
new external prime-distribution theorem is used in this note.
