# Theta cutoff matching: internal analytic and numerical review

11 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort unavailable and not inferred.
Internal independent-agent derivation and review, not independent mathematical validation.

## Result

The explicit correction can be matched across one natural-cutoff change
without applying the published approximation outside its natural cutoff.
The direct comparison below gives an entering-wave error of order
`P/x`, smaller than the existing corrected source error of order `P/N`.
It applies to the complex upper half-disk, with the reflected wave retained;
conjugation covers the lower half. A cruder real-edge continuity check
is also available but is not used in the full-disk theorem.

The imported source remains [Polymath Corollary 6.4 and Proposition 6.6](https://arxiv.org/html/1904.12438v2#S6.SS3).
Everything below compares its explicit finite wave and correction by
elementary analytic estimates. It makes no stationary-sign assertion.

## 1. Exact correction jump

The quotient defining `C0` satisfies

\[
 C_0(p+2)+C_0(p)=e^{i\pi(p^2/2+p+3/8)}.
\]

The exponential numerators combine through `1+e^(2 pi i p)` and the cosine
numerators cancel. Removable points are handled by analytic continuation.

Write the entering index as `m`, `tau=x/2+pi*t/8`,
`a=sqrt(tau/(2*pi))`, `d=a-m`, and `ell=log m`. For the lower cutoff
`N=m-1`, the phase is `p=-1-2d`. Therefore the correction jump is the real
part of a single explicit wave whose phase contains `2*pi*d^2`.

## 2. Compare the actual entering wave

For `s=sigma+i*T`, `T=x/2`, define

\[
 W_\sigma=M_0(s)m^{-s}\exp\{t(\alpha(s)-\ell)^2/4\},
\]

\[
 B_\sigma=(-1)^m e^{t\pi^2/64}M_0(i\tau)U(\tau)
 e^{2\pi i d^2}e^{i\pi(\sigma-1/2)/4}.
\]

For `z=x+iy`, the entering finite term is
`W_((1-y)/2)+conj(W_((1+y)/2))`. The analogous pair of B waves equals
the printed correction jump, including its factor `exp(-pi*i*y/8)`.
Thus both reflected channels are accounted for at nonreal points.

Set

\[
 \delta=\sigma-i\pi t/8,\qquad \eta=\log(a/m),\qquad
 F(a)=a^2\log(a/m)-a^2/2-(a-m)^2+m^2/2.
\]

Taylor expansion of the prescribed `m0=log M0` at `i*tau`, followed by
completion of the heat square, gives an exponential identity

\[
 W_\sigma=B_\sigma\exp\{\sigma\eta+t\eta^2/4+2\pi iF(a)+E\}.
\]

This is a constructed exponent, not necessarily the principal logarithm
of the ratio. The phase difference in a direct calculation is
`pi*m*(m+1)`, an integer multiple of `2*pi`, which does not alter the
identity.

Let `M` bound `|alpha'|` on the segment from `i*tau` to `s`, put
`epsilon0=3/(2*tau)`, and `epsilon=epsilon0+M*|delta|`. Then

\[
 |E|\le \epsilon_0|\delta|+\frac M2|\delta|^2
 +\frac t4\left[2\sqrt{\eta^2+\pi^2/16}\,\epsilon+\epsilon^2\right].
\]

Indeed `alpha(i*tau)=log a+i*pi/4+O_(<=)(epsilon0)` follows from its two
explicit rational terms; the first derivative controls its variation and
the second-order remainder for `m0`. For example, if imaginary parts on
the segment have modulus at least `V>0`, then
`M=3/(2*V^2)+1/(2*V)` is valid directly from the rational/log formula.

Moreover `F(m)=F'(m)=F''(m)=0` and `F'''(a)=2/a`. With a positive lower
bound `a_min` between `a` and `m`,

\[
 |2\pi F(a)|\le\frac{2\pi|d|^3}{3a_{\min}}.
\]

Combining these estimates, define

\[
 \Lambda=|\sigma\eta|+t\eta^2/4+
 \frac{2\pi|d|^3}{3a_{\min}}+\text{the displayed bound for }|E|.
\]

Since `|B_sigma|=P=e^(t*pi^2/64)*|M0(i*tau)|`,

\[
 |W_\sigma-B_\sigma|\le P(e^\Lambda-1).
\]

A common upper bound for both real sigma values gives the complete
entering-wave payment `2*P*(exp(Lambda)-1)`. Note 20's prefactor and
normalizer bounds therefore yield `2*K*Z*(exp(Lambda)-1)` on the relevant
disk. Close to a cutoff, `|d|=O(r/m)`, `eta=O(r/m^2)`, and
`Lambda=O(1/x)` for bounded t, sigma, and disk radius. This gives the
claimed smaller matching scale.

## 3. How the source theorem is used

At each point, first apply the published approximation with the actual
natural cutoff. If that differs from the chosen fixed cutoff by one,
replace the finite sum and correction using the exact jump identity and
the preceding entering-wave estimate. This produces a pointwise bound
for the chosen fixed representation. Its finite sum is holomorphic;
its printed correction must still be replaced by Note 20's holomorphic
exponential surrogate before Cauchy estimates are used.

The proof must check that only one cutoff is crossed, that every real
phase needed in both correction formulas is within the proved profile
range, and that the complete enlarged disk satisfies the source theorem's
time/height range. Both reflected waves and the logarithmic-carrier
normalization remain necessary. A hard switch between two local Cauchy
certificates is not itself a derivative theorem at the edge.

## 4. Separate continuity cross-check

At `b=4*pi*m^2-pi*t/4>200`, taking real one-sided limits in the source
theorem is legitimate: H is continuous, and each fixed finite sum and
correction has a finite limit. The jump discrepancy is bounded by the
sum of the two source errors. This is order `P/N`.

## 5. Portable checker and retained record audit

Reviewed the [checker](../numerics/check_theta_cutoff_matching.py) and its
[retained record](../numerics/THETA_CUTOFF_MATCHING_RECORD_20261011.json).
The source SHA-256 is
`b7707547a4997e1ebf224cbbfc669f6deb2cb5f598cec0d00827f02a6f34e954`.

A separate invocation of the entire outward checker passed in 10.38 seconds.
Every retained JSON field except elapsed runtime agrees with that replay.
The checker verifies the source hypotheses, both possible natural cutoffs,
the fixed reference profile range, and the moving edge's inclusion in the
center family. It uses the endpoint maximum for the time-dependent finite
weight exponent and the smaller natural index in the corrected source
error denominator. The matching payment contains both reflected finite
waves. Constant-center normalization justifies direct physical Cauchy
payments, without a normalizer derivative convolution.

The resulting rigorous upper bounds include:

| Quantity | Upper bound |
| --- | ---: |
| Matching logarithmic error `Lambda` | `2.995742e-10` |
| Extra cutoff matching payment over `A_t(X)` | `1.484686e-12` |
| Complete corrected disk error over `A_t(X)` | `3.135204e-7` |
| First physical derivative error over `A_t(X)` | `6.270408e-6` |
| Third physical derivative error over `A_t(X)` | `0.015048978` |

Exact rational operations on the retained decimal endpoints independently
confirmed that the recorded total encloses the sum of its three payments,
and that every physical derivative allowance encloses `j! eta/r^j`.

The independent real-edge check was also audited from the original polar
formula for `log M0`, without using the checker's stabilized phase. For
`s=1/2+iT`, put `theta=atan(2T)` and `R^2=1/4+T^2`. Then

\[
\operatorname{Im}m_0(s)=\pi-\frac T2\log\pi
-\frac{\theta}{4}+\frac T2(\tfrac12\log R^2-\log2)-\frac T2.
\]

The entering wave's phase is this expression minus `T log m`, plus
`t Im(alpha(s))(Re(alpha(s))−log m)/2`. Independently computing the
correction jump from `M0(i tau) U` gives the rigorous enclosure

\[
3.92003701457416031159544524870370568345\,10^{-13}
<\frac{\Delta G-\Delta C}{A_t(X)}
<3.92003701457416031159544524870370607726\,10^{-13}.
\]

This contains the record's narrower enclosure and is strictly positive.
It independently checks the parity, heat shift, carrier phase, and jump
sign. In particular, the natural piecewise approximation `G_nat−C_nat`
still has a nonzero jump; analyticity comes from freezing the finite
cutoff and replacing its correction with the holomorphic surrogate.
No differentiation of the natural piecewise approximation is justified.

The family certificate fixes `m=22066` for all center offsets `[-.1,.1]`.
It remains valid for individual disks entirely to one side of the edge:
over the global enclosing rectangle the natural cutoff is always either
`m−1` or `m`, so the same pointwise one-term replacement applies. No
pre-existing finite-jet spatial transport hull is invoked here.

## 6. Candidate localization from the same disk certificate

At a joint zero `H(X)=H'(X)=0`, write `f_j=G_m^(j)(X)/A_t(X)`,
`c=C_m(t,X)/A_t(X)`, and `k=pi/8`. The analytic error obeys
`E(X)/A=c−f_0` and `E'(X)/A=−f_1−kc`. Schwarz–Pick applied to the
unit-disk rescaling `E(X+r w)/(A eta)` therefore gives the necessary
condition

\[
\frac{r|f_1+kc|}{\eta}+\left(\frac{f_0-c}{\eta}\right)^2\le1.
\]

This is a useful correlated candidate-localization target. It supplies
neither a zero nor the relative error needed for bounded stationary loss.

## Integrated note scan

The final [Note 22](../notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md)
was checked after integration. Its family extension covers the globally
frozen cutoff even for individual disks wholly to one side of the edge.
All displayed certified bounds round outward. The numerical result is
limited to the declared rectangle; the broader theorem is analytic.
The nonzero piecewise jump, constant-center derivative normalization and
necessary-only candidate condition are explicit. No blocker was found.

## Status

The direct matching algebra, explicit remainder structure, implementation,
retained record, and independent edge phase evaluation pass this audit.
The result removes the fixed-cutoff restriction locally and quantifies its
cost. It does not prove uniform bounded/Hölder stationary loss or collision
exclusion. The published source theorem remains imported rather than
formally verified by the checker.
