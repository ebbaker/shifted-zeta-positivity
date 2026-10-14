# Certified stationary theta and Euler controls

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: `gpt-6.1-sol` (Codex), reasoning effort **ultra**.
This is an internal computer assisted local result, with outward arithmetic.

The Euler control from investigation 19 has a **negative margin on an
actual stationary curve**, throughout a small positive Newman-time interval.
Two genuine theta stationary curves have positive margins on the same time
interval. This checks the physical constrained target directly and supplies
a quantitative screen for the operator ansatz. It is a local benchmark;
it does not construct a theta square or cover all heights and times.

## Three declared compact boxes

Use the unnormalized convention
\[
H_t(x)=\int_0^\infty\Phi(u)e^{tu^2}\cos(xu)\,du,
\quad
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
 e^{-\pi n^2e^{4u}},\quad u\ge0.
\]
For the control, let \(\Phi_e\) be the even extension, and set
\[
\psi(u)=\Phi_e(u)+\tfrac14[\Phi_e(u+a)+\Phi_e(u-a)],
\qquad a=\tfrac12\log41.
\]
Every time below belongs to the exact interval
\[
I=[199999/10^6,200001/10^6].
\]
The following outward conclusions hold for **every** \(t\in I\).
In each row there is exactly one stationary point inside the given spatial
interval. The corresponding critical point varies differentiably with time.

| Source and constraint | Spatial center | Radius | Stationary Laguerre enclosure |
| --- | --- | --- | --- |
| Theta, \(H_x=0\) | \(31.05753718634\) | \(10^{-5}\) | \(1.48579\cdot10^{-9}<\mathscr L_0<1.48582\cdot10^{-9}\) |
| Theta, \(H_{xx}=0\) | \(9.4822468462\) | \(10^{-4}\) | \(4.02686\cdot10^{-7}<\mathscr L_1<4.02694\cdot10^{-7}\) |
| Control, \(H_x=0\) | \(1.68413603215\) | \(10^{-6}\) | \(-5.346\cdot10^{-6}<\mathscr L_0<-5.254\cdot10^{-6}\) |

All decimal centers and radii are exact rationals. The labels locate the
curves; no claim that these are the first stationary points is needed.
The checker verifies stricter intervals stored as exact dyadic endpoints
in the [execution record](../numerics/STATIONARY_OPERATOR_CONTROLS_20261014.json).
The control extends the [fixed nonstationary witness in 19](../../19_euler_factor_controls/notes/2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md).

## Integral and tail ledger

For any nonnegative integer derivative order \(j\), define
\[
w_j(r)=r^je^{tr^2}\cos(xr+j\pi/2).
\]
The control jets equal
\[
H^{(j)}_{\psi,t}(x)=\int_0^\infty\Phi(v)
 \{w_j(v)+\tfrac14[w_j(v+a)+w_j(v-a)]\}\,dv.
\tag{1}
\]
This follows by translating the full even-source integral and returning
to the positive half-line. In particular both shifted tails remain present.
For absolute moments, replace \(w_j(r)\) by \(|r|^je^{tr^2}\).
Denote these positive moment integrals by \(M_j(t)\).

The checker retains \(n\le4\) on \(0\le v\le1\).
With \(m=5\) and
\[
q=((m+1)/m)^4e^{-\pi(2m+1)},\quad
B_N=\frac{2\pi^2m^4e^{-\pi m^2}}{1-q},
\]
the omitted density is between zero and \(B_N\). The finite-interval
jet or moment payment is
\[
D_j=B_N(1+c)(1+a)^je^{t(1+a)^2},
\tag{2}
\]
where \((c,a)=(1/2,\log41/2)\) for the control and \((0,0)\)
for theta. The full source bound
\(\Phi(v)\le4\pi^2e^{9v-\pi e^{4v}}\) gives the entire tail payment
\[
T_j=\frac{(1+c)4\pi^2(1+a)^j
 e^{9+t(1+a)^2-\pi e^4}}
 {4\pi e^4-9-2t(1+a)-j/(1+a)}.
\tag{3}
\]
The denominator is strictly positive and the logarithmic derivative
continues decreasing beyond the cutoff. All of these hypotheses are
checked with real balls; the complete theta series and shifted tails
are bounded, rather than inferred from finite samples.

At each center the checker obtains jets through order five, and obtains
moments through order seven at \(t_{\max}=200001/10^6\).
Validated complex integration encloses the finite integrals, followed by
symmetric outward payment of (2) and (3). The finite integrands are entire.
For an odd absolute control moment on this finite interval, \(|v-a|=a-v\)
because \(a>1\); its polynomial entire extension agrees on the actual
integration path. The tail uses the majorant \(v+a\), so it needs no such
replacement. The [python-flint integration contract](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral)
is therefore met without a branch-cut assumption.

## Transport from centers to whole boxes

Write \(h_j=\partial_x^jH\), \(t=t_0+\tau\), \(x=x_0+\eta\),
with \(|\tau|\le\delta_t\) and \(|\eta|\le\delta_x\).
Backward heat gives \(\partial_t h_j=-h_{j+2}\). Taylor's theorem
along the straight parameter segment gives
\[
h_j(t,x)=h_j(t_0,x_0)+\eta h_{j+1}(t_0,x_0)
 -\tau h_{j+2}(t_0,x_0)+R_j,
\]
\[
|R_j|\le\tfrac12\eta^2M_{j+2}(t_{\max})
 +|\eta|\delta_tM_{j+3}(t_{\max})
 +\tfrac12\delta_t^2M_{j+4}(t_{\max}).
\tag{4}
\]
Absolute moments bound the spatial derivatives uniformly on the real
axis and at every time along the segment. This includes the mixed
parameter derivative and both second derivatives.

At each spatial endpoint, (4) gives opposite strict signs for the
stationary derivative, uniformly in time. On the whole box it gives a
strict positive sign for the next spatial derivative: \(H_{xx}>0\) in
the first and third rows, \(H_{xxx}>0\) in the second. The intermediate
value theorem gives existence for each time; strict monotonicity gives
uniqueness. The implicit-function theorem then supplies the stationary
curve, with
\[
x_s'(t)=h_{j+3}(t,x_s(t))/h_{j+2}(t,x_s(t)).
\]
On that curve the appropriate \(h_{j+1}\) vanishes, and
\[
\mathscr L_j=-h_jh_{j+2}
 =\tfrac12\frac d{dt}h_j(t,x_s(t))^2.
\tag{5}
\]
Outward products of the whole-box jets give the table's three signs.
This proof avoids treating a numerically small derivative as exact zero.

## Consequence for a proposed constrained square

The control has an even, strictly positive, smooth, rapidly decreasing
source and analytic Newman evolution. Its multiplication Dirac operator
is selfadjoint on its usual domain; all needed source vectors are analytic
for compact Newman time intervals. Nevertheless, its stationary critical
value has a strictly decreasing square throughout \(I\).

If a proposed exact identity on this curve reads
\[
\mathscr L_0=\|\mathcal A\Psi\|^2+H_xM+\mathcal D+E,
\]
then it must satisfy
\[
\mathcal D+E<-5.254\cdot10^{-6}
\]
on the control curve, or invoke a hypothesis the control violates.
The quantified negative payment follows from stationarity and the square's
nonnegativity. Source positivity, ordinary Dirac factorization, and heat
analyticity cannot supply that missing distinction.

The two theta margins check the same stationary-energy readout for both
\(j=0\) and \(j=1\) locally. They are obtained by full-source interval
estimation, not by a new source-specific square or imaginary-gluing
multiplier. Those construction tasks remain open.

## Replay

With python-flint available, run from the investigation's `numerics/`:

```sh
python3 -B certify_stationary_operator_controls.py --output /tmp/stationary-controls.json
```

The retained run uses 160 bits, four explicit theta terms and validated
finite quadrature with tolerance goal \(2^{-120}\). Returned enclosures,
rather than requested tolerances, decide every sign. The record binds the
executed script by SHA-256 and retains all quadrature and tail payments.
Replay establishes the inequalities from its own arithmetic; hashes record
source identity rather than mathematical validity.
