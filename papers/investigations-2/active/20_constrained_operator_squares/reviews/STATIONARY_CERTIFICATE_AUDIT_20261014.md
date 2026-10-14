# Audit of the stationary theta and Euler certificate

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded audit model: **gpt-6.1-sol**; reasoning effort: **ultra**.
This is a separate-agent mathematical/code audit within the same LLM-assisted
research session, not independent specialist validation.

**Result: pass for the three declared compact boxes.** I read the complete
proof note and checker, replayed the checker with its default 160-bit/four-term
settings, and obtained `PASS` for every case. I also reconstructed each exact
dyadic Laguerre endpoint as a rational and verified that the note's displayed
strict decimal bounds strictly contain both endpoints. No numerical midpoint
or requested quadrature tolerance was used to decide these comparisons.

The multivariable Taylor payment is correct: along the straight segment the
second derivative is
\(\eta^2h_{j+2}-2\eta\tau h_{j+3}+\tau^2h_{j+4}\).
The integral Taylor remainder therefore gives the stated coefficients
\(1/2,1,1/2\). Positive absolute source moments at the exact maximum time
bound every intermediate real time and every real spatial argument. The
checker obtains central jets through order five and moments through order
seven, which suffice for every transported derivative it uses.

The theta-index payment follows by dropping the negative term in each
positive omitted theta summand, observing that its upper majorant decreases
with source coordinate, and summing the geometric bound on index ratios.
The full-source majorant follows from the ratio
\(16e^{-3\pi}<1/2\). For a nonnegative derivative order, both shifted
absolute weights are bounded by
\((v+a)^je^{t(v+a)^2}\), with total factor \(1+c\). The logarithmic
derivative of the infinite-tail majorant is negative at the cutoff and
continues decreasing under the explicitly checked slope conditions. Thus
neither omitted theta indices nor either shifted tail is lost.

The odd absolute shifted finite moments satisfy \(|v-a|^j=(a-v)^j\)
on the actual interval \(0\le v\le1<a\). Their callback uses this
polynomial entire extension, rather than complex absolute value. All other
callback factors are polynomial, exponential, sine or cosine. Ignoring the
analytic flag is consequently valid under the documented
[python-flint integration contract](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral).

The endpoint stationarity signs hold for the entire time interval, and the
next spatial derivative has a strict uniform sign throughout each box.
The intermediate value and implicit-function arguments therefore establish
one differentiable stationary branch for every time, rather than a sampled
or approximately stationary point. The claimed derivative of that branch
and the stationary identity \(\mathscr L_j=-h_jh_{j+2}\) follow by exact
differentiation. Uniform outward products of the jet balls correctly bound
the margin along each branch. The negative control payment follows from
subtracting a nonnegative square at exact stationarity.

One wording correction was resolved before installation: replace “For any integer derivative
order \(j\)” with “For any nonnegative integer derivative order \(j\).”
The argument and implemented orders are nonnegative. No code repair is
needed for the declared certificate. The conclusion remains local;
this audit does not establish a constrained theta square or global time
and height coverage.
