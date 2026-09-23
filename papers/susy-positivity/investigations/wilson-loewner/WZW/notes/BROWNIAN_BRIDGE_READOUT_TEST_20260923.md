# Brownian bridge readout test: first passage, logarithmic range and phase

**Numerical correction, later on 23 September 2026:** the transformed prime-free kernel correction integral in the diagnostic used `exp(-2*v)` instead of `exp(-(3-2*omega)*v)`. The written convolution formula was correct. The implementation and record have been corrected and the complete suite replayed successfully. See the [modular-scattering note, Section 8](MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) for the derivation, independent regressions and scope; the analytical exclusions are unchanged.


23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Status:** a specified Brownian/Bessel response is derived and excluded as the arithmetic transfer. A separate logarithmic readout recovers the arithmetic boundary phase but does not establish its causality. There are 51 floating diagnostics, no interval certification, no independent specialist review, and no RH result.

This executes the bounded test proposed in the [independent-source search](INDEPENDENT_ARITHMETIC_SOURCE_SEARCH_20260923.md). The comparison target and first-delay conventions are those of the [WZW bounded test](BOUNDED_ARITHMETIC_READOUT_TEST_20260923.md) and the [arithmetic-source calculation](../../notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md).

## 1. Result

The Brownian bridge remains an independently specified source of the full scalar xi function. Its most direct first-passage implementation also supplies a genuine directed response, a strong initial identity and an ordinary L2 norm balance. But the response is a Laplace transform of a random waiting time, whereas the xi function is its Mellin transform. The two roles do not coincide.

For the first-passage construction below the response is

\[
F_\lambda(p)=\left(\frac{\sqrt{\pi\lambda p}}
{\sinh\sqrt{\pi\lambda p}}\right)^2.
\]

It is not K_omega(p). For every positive radius its time kernel is flat at the origin and analytic at log 2. The arithmetic kernel instead has a fractional singularity at the origin and a second delayed singularity at log 2. No positive change of the radius clock repairs these local mismatches.

There is also a wider exclusion: a nontrivial average over positive random delays attenuates some real-frequency amplitudes, whereas the arithmetic quotient has unit modulus on the imaginary axis. Thus an ordinary positive delay average cannot be the exact arithmetic transfer, even if its waiting-time distribution has all the correct xi moments.

Using logarithmic range makes the xi moments directly visible to the transform variable, but its native averaging kernels have both positive and negative delays. Their quotient does have a bounded unitary phase extension equal to K_omega on the boundary. Establishing that this phase operator is causal for the full shift family is the unresolved step, not a consequence of Brownian positivity.

## 2. Independently specified stochastic system

For a standard Brownian bridge b on [0,1], put

\[
Y=\sqrt{2/\pi}\,\bigl(\max b-\min b\bigr).
\]

The established inputs are the identities E[Y^s] = 2 xi(s), the equivalent law of Y squared, and the Bessel first-passage representations. See [Biane--Pitman--Yor, equations (4)--(5), Proposition 1 and Section 4.5](https://arxiv.org/html/math/9912170). The following response and its comparison with K are derived here from those inputs.

Take two independent three-dimensional Brownian motions, with generator one half the Laplacian, started at the center of a ball of radius r. Let tau_r and tau'_r be their first exit times. Equivalently these are first-passage times of radial BES(3) diffusions. Arrange the two waits in succession, and measure the total delay in units

\[
D_\lambda=\frac\pi2(\tau_{\sqrt\lambda}+\tau'_{\sqrt\lambda}),
\qquad \lambda=r^2\ge0.
\]

The constant pi/2 fixes the normalization to the specified bridge observable. It is not fitted to a prime coefficient. Neither the diffusions nor the stopping rule use zeta zeros or prime energies. Lambda is a physical radius-squared parameter; identifying it with arithmetic omega is a test, not an assumed physical dictionary.

### 2.1 Derivation of the native response

For radial starting position x inside a radius-r ball,

\[
v_p(x)=\mathbb E_x e^{-p\tau_r}
\]

solves

\[
\tfrac12v_p''+\frac1xv_p'=p v_p,\qquad v_p(r)=1,
\]

with the solution regular at zero. Solving gives

\[
v_p(x)=\frac{r\sinh(x\sqrt{2p})}
{x\sinh(r\sqrt{2p})},\qquad
v_p(0)=\frac{r\sqrt{2p}}{\sinh(r\sqrt{2p})}.
\]

Independence of the two waits and the specified time units therefore give F_lambda above, for Re p >= 0 with its continuous value at zero. The expression is even in the square root, so no physical branch ambiguity is introduced.

Brownian scaling gives D_lambda equal in distribution to lambda D_1. The known bridge law, or uniqueness of Laplace transforms, gives

\[
D_1\stackrel{d}=Y^2,\qquad
\mathbb E[D_1^{s/2}]=2\xi(s).
\]

This is equality in distribution. It is not a pathwise identification of bridge physical time with a logarithmic propagation coordinate. Useful normalizations are

\[
\mathbb E D_1=\pi/3,\qquad
\operatorname{Var}(D_1)=\pi^2/45.
\]

The model also has genuine nested-radius conditional responses. By the strong Markov property, for lambda_2 > lambda_1 the additional pair of exit waits has transform F_(lambda_2)/F_(lambda_1). For example, the symmetric radius-squared change eta-omega to eta+omega has response F_(eta+omega)/F_(eta-omega), with 0 <= omega < eta. This supplies a native identity limit and oriented propagation, but not the desired shifts in the xi argument. It is covered by the positive-delay exclusion below.

## 3. Preparation, readout and an exact physical norm balance

Prepare a scalar input waveform f in ordinary L2(0,L), extend it by zero to the real line, and transmit each copy after the two specified waits. Read out the ensemble mean amplitude:

\[
(T_\lambda f)(u)=\mathbb E[f(u-D_\lambda)].
\]

This is an explicitly chosen classical mean-signal readout. It does not assert that diffusion probabilities are quantum scattering amplitudes. The internal space is the product of the signal L2 space and the probability space of the two paths. Constant path preparation is isometric; path-dependent translation preserves the full signal norm; expectation is an orthogonal projection onto the mean output.

Since D_lambda >= 0, this response is causal. T_0 = I, and T_lambda tends strongly to I as lambda decreases to zero. This follows from the strong continuity of translations and the scaling coupling D_lambda = lambda D_1 in distribution. Operator-norm convergence is not claimed.

For the response restricted to (0,L), the exact balance is

\[
\begin{split}
\|f\|_{(0,L)}^2-\|T_\lambda f\|_{(0,L)}^2
={}&\mathbb E\int_0^L
|f(u-D_\lambda)-T_\lambda f(u)|^2\,du\\
&+\mathbb E\int_L^\infty |f(u-D_\lambda)|^2\,du.
\end{split}
\]

The first term is the output retained in fluctuations rather than the mean. The second is signal that arrives after the observation window. There is no earlier-than-zero output. Conditional variance, translation invariance and Tonelli's theorem prove the formula for arbitrary L2 input; a differentiability assumption on f is unnecessary.

For L = 1, lambda = 1/4 and unit constant input on the window, the computed components are

| Component | Squared norm / energy |
|---|---:|
| Mean output inside the window | 0.6754761763409908 |
| Fluctuation term inside the window | 0.0627389402570588 |
| Future signal beyond the window | 0.2617848834019504 |

They sum to one. This is a positive norm balance in the declared signal space, not an arithmetic norm imposed on a correlator.

## 4. Arithmetic comparison: failure already before the first prime

Recall

\[
H(p)=\xi(1/2+p),\qquad
K_\omega(p)=H(p-\omega)/H(p+\omega),\qquad
a_\omega(p)=H'(p-\omega)/H(p-\omega)+H'(p+\omega)/H(p+\omega).
\]

The scalar Brownian identity indeed yields K and a as ratios of moments and logarithmic moments. The numerical diagnostics independently integrate the native density and verify both identities. But the causal waveform response is F, obtained by a Laplace transform in the actual waiting time. Taking a Mellin quotient instead is a different readout operation.

### 4.1 Exact native kernel and short delays

Let g be the density of D_1. Differentiating the bridge range distribution, with its theta transform, yields the two equal representations

\[
g(d)=2\pi\sum_{n\ge1}n^2(2\pi n^2d-3)e^{-\pi n^2d},
\]

\[
g(d)=4\pi d^{-7/2}\sum_{n\ge1}
n^2(\pi n^2-\tfrac32d)e^{-\pi n^2/d},\qquad d>0.
\]

The native impulse response is b_lambda(u) = lambda^(-1) g(u/lambda) for u > 0, and zero for u <= 0. The second expansion gives

\[
b_\lambda(u)\sim
4\pi^2\lambda^{5/2}u^{-7/2}e^{-\pi\lambda/u}
\quad (u\downarrow0).
\]

For every fixed lambda > 0, this kernel and all its derivatives vanish at zero. It is real analytic at every positive u. Convergence of the displayed series and their derivatives is uniform on compact subintervals of positive u.

The inherited complete prime-free arithmetic kernel instead satisfies

\[
k_\omega^<(u)\sim A_\omega u^{\omega-1},\qquad
A_\omega=(2\pi)^\omega/\Gamma(\omega)>0.
\]

For the tested range 0 < omega <= 1/2 this diverges at zero. Thus the native readout fails on arbitrarily short positive windows. A clock lambda(omega) > 0, a fixed finite rescaling of time, or finite constant normalization cannot change exponential flatness into a fractional singularity. Taking lambda = 0 gives the identity, not the nontrivial positive-shift arithmetic transfer.

### 4.2 Generator and large-p controls

For lambda > 0 the native logarithmic source is

\[
-\partial_\lambda\log F_\lambda(p)
=\sqrt{\pi p/\lambda}\,\coth\sqrt{\pi\lambda p}-1/\lambda,
\]

with zero-radius limit pi p/3. Any differentiable clock with finite nonzero initial derivative leaves this proportional to p. The arithmetic zero-shift source grows logarithmically at large positive p. At p = 2 the values are approximately 2.0943951024 and 0.1836685430, respectively, for the direct clock lambda = omega.

At fixed positive parameters, the transform asymptotics also disagree:

\[
F_\lambda(p)\sim4\pi\lambda p\,e^{-2\sqrt{\pi\lambda p}},
\qquad K_\omega(p)\sim(2\pi/p)^\omega
\quad(p\to+\infty).
\]

For a finite-scale example, p = 2 and lambda = omega = 1/4 give

\[
F_{1/4}(2)=0.60736129846844\ldots,\qquad
K_{1/4}(2)=0.95512532048644\ldots.
\]

These numerical mismatches illustrate the analytic exclusions; the argument does not depend on choosing this parameter value or clock.

## 5. First prime and the wider positive-delay exclusion

On log 2 < u < log 3 the full arithmetic comparison is

\[
k_\omega(u)=k_\omega^<(u)+c_2(\omega)k_\omega^<(u-\log2),
\qquad c_2(\omega)=(2^\omega-2^{-\omega})/\sqrt2.
\]

For omega = 1/4 the delayed contribution multiplied by epsilon^(3/4), at u = log 2 + epsilon, tends to

\[
c_2(1/4)A_{1/4}=0.107551311336445\ldots.
\]

The diagnostic values are 0.1071750107 at epsilon = 10^(-3) and 0.1075136697 at epsilon = 10^(-4). The same scaling applied to the smooth Brownian response gives approximately 0.000332407 and 0.000059690 and tends to zero. Thus the first delayed singularity is absent, as the analyticity argument already proves. No prime filter has been added to the native response.

There is a second exclusion that does not depend on the chosen Bessel waiting law.

**Proposition.** A causal convolution that averages over a nondegenerate positive random delay cannot equal the full arithmetic transfer K_omega.

**Proof.** For a probability measure mu on nonnegative delays its boundary multiplier is the characteristic function

\[
\widehat\mu(\nu)=\mathbb E e^{-i\nu D},\qquad |\widehat\mu(\nu)|\le1.
\]

If equality holds for all frequencies, equality in the triangle inequality forces D to be constant almost surely. One can apply the equality condition to a countable dense set of frequencies to make this conclusion simultaneous. A nondegenerate delay therefore attenuates some frequencies; for the present everywhere-positive continuous density the inequality is strict at every nonzero frequency.

On the other hand, evenness and real type of H give

\[
H(-\omega+i\nu)=\overline{H(\omega+i\nu)},\qquad
|K_\omega(i\nu)|=1
\]

where the quotient is defined. Possible common boundary zeros are isolated and irrelevant to the almost-everywhere multiplier statement. A positive delay average has a continuous characteristic function, so equality almost everywhere would force modulus one everywhere. It would be a deterministic delay. Such a delay has transform exp(-p d_0), which disagrees with the polynomial large-p behavior of K_omega for omega > 0. QED.

This applies to positive first-passage mixtures and nested-radius conditional delays as well. A subprobability readout cannot repair the result because K_omega(0) = 1 fixes total mass one. It does not apply to coherent signed or complex amplitudes, matrix-valued scattering, or a nonstationary readout.

For one fixed finite window the local kernel argument in Section 4 is sufficient. The boundary proposition concerns equality of the complete convolution response, equivalently compatibility over all windows. These scopes should not be conflated.

## 6. Logarithmic range: exact phase, unresolved direction

The obvious alternative is to use X = log Y, since p is a Mellin variable in the bridge identity. Center the path law by

\[
d\mathbb P_* = \frac{Y^{1/2}}{\mathbb E Y^{1/2}}d\mathbb P,
\qquad M(z)=\mathbb E_*e^{zX}=H(z)/H(0).
\]

The density q of X is even and strictly positive on the whole real line. In terms of g,

\[
q(x)=\frac{2e^{5x/2}g(e^{2x})}{\mathbb E[Y^{1/2}]}.
\]

Define two native, positively tilted, normalized mean readouts on L2(R):

\[
(C_{\pm\omega}f)(u)=
\int_{\mathbb R}f(u-x)\frac{e^{\mp\omega x}q(x)}{M(\omega)}\,dx.
\]

Both are bounded probability averages and contractions. They are adjoints of one another. With the bilateral Laplace/Fourier convention exp(-p x), their symbols are

\[
B_{\pm\omega}(p)=\frac{M(p\pm\omega)}{M(\omega)},\qquad
\frac{B_{-\omega}(p)}{B_{+\omega}(p)}=K_\omega(p).
\]

The scalar normalization agrees for the two tilts by evenness of M. Thus the quotient is exact, including every completion factor.

### 6.1 The native mean readouts are not causal

Both kernels are strictly positive at arbitrarily negative x. No finite shift of the reference point makes them causal. For example, the negative-delay probability of C_(+1/4) is approximately 0.5216422070. This is not a small truncation artifact. Truncating the law to x >= 0 would change its moments and destroy the displayed exact symbols.

Moreover B_(+omega)(i nu) tends to zero at large frequency by the Riemann--Lebesgue lemma. Consequently C_(+omega) has no bounded inverse on ordinary L2. At omega = 1/4, its reciprocal multiplier magnitude at frequency 50 is about 1.04 times 10^14. This illustrates the problem with implementing the quotient by separately undoing the mean smoothing.

### 6.2 An unbounded inverse does not imply an unbounded quotient

The previous point must not be used as an invalid no-go argument. In fact the quotient has a canonical **bounded unitary extension** on L2(R). Define it on the dense range of C_(+omega) by

\[
U_\omega(C_{+\omega}f)=C_{-\omega}f.
\]

The two outputs have equal L2 norm by their conjugate Fourier multipliers. The multiplier of C_(+omega) is nonzero almost everywhere: its numerator is an entire nonzero function, with isolated real-frequency zeros at most. Thus both ranges are dense, and the isometry extends uniquely to a unitary. Its Fourier multiplier is

\[
U_\omega:\quad
\frac{\overline{B_{+\omega}(i\nu)}}{B_{+\omega}(i\nu)}
=K_\omega(i\nu)
\quad\text{almost everywhere}.
\]

This is a polar-phase construction, not a bounded implementation of C_(+omega)^(-1) as a separate device. U_0 = I almost everywhere, including across the isolated zeros by an arbitrary measure-zero assignment. Dominated convergence gives the strong limit U_omega -> I as omega -> 0.

What is missing is a causal physical implementation of this phase operation. The two mean readouts used to define it are already two-sided. Their equal norms do not supply an arrow of propagation for U. A finite-window compression of U is automatically contractive, but its omitted output can lie before time zero as well as after L. Identifying that compression with the causal arithmetic Volterra response would require the very causality or contour-shift assertion still at issue.

For the whole positive-shift family, the corresponding innerness/causality condition is the RH-equivalent condition already identified in the [arithmetic-source note](../../notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md) and [Suzuki's canonical-system analysis](https://arxiv.org/html/1204.1827). It is known in the safe shift range; deriving it for every positive shift from this Brownian construction has not been accomplished. Boundary modulus one and a positive path measure do not establish it.

This phase construction is useful because it locates the remaining step precisely. It neither excludes a coherent Brownian scattering realization nor constitutes one.

## 7. Decision from the bounded test

| Requirement | Two-exit mean readout | Logarithmic readout / phase |
|---|---|---|
| Independent stochastic source | Explicit Brownian diffusions and stopping rule | Same bridge range with explicit positive tilts |
| Entire xi as a scalar observable | Exact Mellin moments | Exact centered moment transform |
| Initial identity | Strong limit as radius vanishes | U_0 = I and strong limit for the phase extension; native C_0 is smoothing |
| Ordinary norm control | Exact variance plus future-output balance | Native averages are contractions; phase extension is unitary |
| Directed causal mean response | Established | Native logarithmic means are two-sided |
| Correct arithmetic response | Excluded already at short delay | Boundary phase matches; causal realization unestablished |
| First prime singularity | Absent from the native response | Present in the arithmetic comparison only after establishing the appropriate causal realization |

The original scalar-source lead survives. The proposed ordinary first-passage readout does not. Further Brownian work needs a coherent or otherwise non-averaging phase readout whose causality follows from independently specified dynamics. Increasing moment precision, adding path samples, or dividing measured moments would not address the remaining question. Modular cusp scattering remains the concrete comparison system for investigating that kind of phase response.

## 8. Diagnostics, replay and limitations

The [program](../numerics/check_brownian_readout.py), [51-case record](../numerics/records/brownian-readout-20260923.json), and [same-assistant audit](../reviews/review_codex_brownian_readout_20260923.md) are separate from the previous WZW and arithmetic suites. All 51 floating diagnostics pass. Passing here includes reproducing the predicted exclusions, not passing the physical arithmetic-realization test.

The calculations compare the two theta density expansions, density moments with completed xi, the density Laplace transform with the exit-ODE response, full arithmetic moment ratios and logarithmic derivatives, short-delay and first-prime asymptotics, boundary moduli, the finite-window norm balance, reflection of the log-range density, negative-delay mass, and the phase quotient. The largest residual among identities assigned tolerance 10^(-30) or smaller was below 3 times 10^(-46). A complex moment integral was repeated at 15 extra decimal digits.

The run uses mpmath 1.3.0 at 45 decimal digits, with 12 theta terms in the branch appropriate to small or large d. Oscillatory density integrals for the phase comparison use 15 guard digits because their transforms become small. On the selected density branch the omitted terms decay at least as fast in their exponential factor as exp(-pi n^2); polynomial prefactors are retained in the implemented summands. These are high-precision floating diagnostics, not rigorous tail-and-rounding enclosures. No Monte Carlo simulation, Brownian time grid, xi-zero table, or assumption of RH is used. The analytical arguments establish the operator and regularity claims; finite samples do not prove them.

From the parent Wilson--Loewner directory, with Python 3 and mpmath installed:

```sh
python3 -B WZW/numerics/check_brownian_readout.py --output /tmp/brownian-readout-replay.json
```

Manuscript PDFs, TeX inputs and the parent WZW/arithmetic numerical records are unchanged; the two continuation records were corrected as described above. The note is a research addendum rather than a manuscript revision.
