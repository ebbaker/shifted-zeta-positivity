# B02 geometry and observation selection over the continuum of heights

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, **GPT-6.1 Sol / ultra** by explicit
delegation. **Status: proved conditional geometry and a supported design
choice within B02.** Canonical estimate acquisition is a separate task.

Read the [result index][results] and [avoid index][avoid], especially
[collision controls12][r12], [classification01][a01], [premises02][a02] and
[scope07][a07]. This work pays geometric factors in a quantitative
positive-time milestone. See [Notes03–05][program] for the original
collar, separate roles of the contour and observation, and the scope of
the unbounded-height program.

## 1. Vary the contour with observation, target and time fixed

At one real center \(X\), write \(F=H_\lambda/A\) with a prescribed
analytic nonzero carrier \(A\), and freeze \(\lambda\) across the domain.
Let \(k=a-\delta\), \(b=a+\eta\), \(p=X+ib\), and
\(K=\{X+iy:k\le y\le a\}\), where \(0<k<a<b\).
Write \(d=b-k\). Take the rectangle
\[
 D=\{|x-X|<W,\ \ell<y<u\},
 \qquad e_-=k-\ell>0,\quad e_+=u-b>0.
\]
If the quotient is analytic near \(\bar D\) and
\(\sup_{\bar D}|F-1|\le\varepsilon\) for \(0<\varepsilon<1\), every point of \([X+ik,p]\) has a Cauchy
disk of radius \(r=\min(W,e_-,e_+)\). Hence \(m=1-\varepsilon\) and
\(M=\varepsilon/r\) suffice for the field consumer. It pays the requested
gain \(\delta\) with retained floor \(m/2\) whenever
\[
  d\le\frac{(1-\varepsilon)r}{2\varepsilon},
  \qquad\text{equivalently }\quad
  \varepsilon\le\frac{r}{2d+r}.
\]
At fixed total vertical height \(H=u-\ell>d\), the largest available
radius is \(\min(W,(H-d)/2)\). Centering the vertical interval
\([k,b]\) in the rectangle attains it. Any separate constraint on
the least admissible \(\ell\) must be included in this placement.

The complete Green allowance under the same disk error in the range of
\(F\) is \(J_D(p)\le\log((1+\varepsilon)/(1-\varepsilon))\).
The carrier's log modulus is harmonic and all four edges are integrated.
For a spatial disk centered halfway between \(X+ik\) and \(p\) of
radius \(R>d/2\), the worst target Green signal is
\[
  g_{\rm disk}=\log\frac{R^2+d^2/4}{Rd}.
\]
Indeed the disk Green kernel on its diameter is
\(\log((R^2-st)/(R|s-t|))\) in signed center coordinates. With
\(s=d/2\), it increases with the target coordinate \(t<s\).
This disk is available inside the rectangle for
\(R\le\min(W,d/2+e_-,d/2+e_+)\), and gives \(g_D\ge g_{\rm disk}\)
by domain monotonicity. With \(R=d/2+r\) and \(W\ge R\),
strict Green exclusion is paid by
\[
  \varepsilon<\left(\frac{r}{d+r}\right)^2,
\]
obtained by comparing the two explicit logarithms.

For the infinite strip \(S=\{\ell<y<u\}\) at the same observation and
target, put \(\alpha=\pi(b-\ell)/H\), \(\beta=\pi(y-\ell)/H\). The
Green kernel, from mapping the strip to the upper half-plane, is
\[
 G_S(p,x+iy)=\tfrac12\log\frac{\cosh(\pi(x-X)/H)-\cos(\alpha+\beta)}
                                   {\cosh(\pi(x-X)/H)-\cos(\alpha-\beta)}.
\]
The worst centerline signal is attained at \(y=k\) and equals
\(\log[\sin(\pi(b+k-2\ell)/(2H))/\sin(\pi(b-k)/(2H))]\).
For the rectangle with the same horizontal edges,
\[
 0\le G_S(p,z)-G_D(p,z)\le [\cosh(\pi W/H)-1]^{-1},\qquad z\in D.
\]
The difference is harmonic after canceling the pole, is zero along the
horizontal edges, and satisfies the bound on the vertical edges by
\(\log(1+v)\le v\). Thus large \(W/H\) yields an explicit strip-signal
approximation at an unchanged observation. This comparison concerns
Green kernels. A domain enlargement also changes the logarithmic
boundary data that must be estimated.

Consider also a regular graph collar inside an ambient strip of height
\(H\) and vertical midpoint \(y_m\), with fixed \(p\) and \(K\)
in its interior. In an exhaustion at \(x=X\pm R\), the total harmonic
measure of the two ends is at most
\[
  \frac{\operatorname{sech}(\kappa R)}{\cos(\kappa H/2)},
  \qquad 0<\kappa<\pi/H .
\]
A harmonic barrier is
\(\cosh(\kappa(x-X))\cos(\kappa(y-y_m))/
[\cosh(\kappa R)\cos(\kappa H/2)]\).
It is at least one on the ends and nonnegative on the graph edges.
For instance, polynomial bounds on absolute boundary logs along the
graphs and along a sequence of admissible, zero-free end cuts suffice
for exhaustion of the complete Green identity. The end integrals then
decay by the barrier. To pass the graph integrals, continuous compactly
supported boundary data converge by the same end bound and maximum
principle, and the uniform tail bound follows by applying the barrier
at each integer distance before reaching the farther graph; exponential
decay absorbs polynomial growth. The Green sums converge monotonically
by exhaustion and positivity. These are sufficient bounds to prove in
any such use, including for a subtracted normalization if applicable.
An adequate canonical log bound on graph edges and end cuts is a
separate arithmetic obligation.

## 2. Vary the observation on fixed domains

Fix \(k,a,\ell,u,W\) and vary \(b>a\). The guaranteed Cauchy radius
\(\min(W,k-\ell,u-b)\) is nonincreasing in \(b\), while the distance
\(d=b-k\) strictly increases. For the fixed symmetric disk, rectangle,
or strip, the exact worst centerline Green signal also strictly
decreases as \(b\) rises. In each domain a conformal map to the unit
disk can send its vertical centerline to a diameter: choose
its zero on that line and its derivative positive along the upward
direction, and reflect to obtain the same uniquely normalized map.
Write \(t(y)\in(-1,1)\) for the strictly increasing mapped diameter
coordinate. For \(b>y\) the pseudohyperbolic distance is
\((t(b)-t(y))/(1-t(b)t(y))\), strictly increasing in \(b\) and
decreasing in \(y\). Taking minus its logarithm proves both the
observation monotonicity and that the worst target is \(k\).

With one common uniform bound on \(|F-1|\), use the smallest
independently admissible observation buffer. If the initial enclosure
is the only anchor, every \(\eta>0\) is above it; a strictly positive
fractional buffer gives an attained choice. If the observation floor
or boundary estimate depends on \(b\), those costs enter the selection.
For example, strip harmonic measure assigns the bottom and top
masses \(1-(b-\ell)/H\) and \((b-\ell)/H\); a high observation may
reduce the allowance when only the bottom boundary is expensive.
A comparison based on these two distinct upper bounds and an
independent observation floor then has a different input from
the uniform \(|F-1|\) bound. Symmetric-domain monotonicity need not
apply to arbitrary graph geometry.

## 3. Couple scale, contours and observations

Here is one controlled fractional rule. At each center with
\(0<a\le1\), choose
\[
 k=3a/4,\qquad b=9a/8,\qquad
 \ell=a/2,\quad u=11a/8,\quad W\ge7a/16.
\]
Then \(d=3a/8\), \(r=a/4\), \(R=7a/16\), and
\(M\le4\varepsilon/a\). The Cauchy condition is
\(\varepsilon\le1/4\); the disk floor is \(\log(29/21)\), which
pays strict Green exclusion for \(\varepsilon<4/25\).
In this scaled geometry, the inverse-width derivative cost cancels
against the length of the inward segment. The Green floor is
scale-invariant. If one vertical margin shrinks as \(r=o(d)\), the same
Cauchy argument with the uniform disk error requires
\(\varepsilon=O(r/d)\); this particular centered-disk Green comparison
requires \(\varepsilon=O((r/d)^2)\) when the disk fits. For any
domain contained between the two horizontal lines, even its exact
target signal is at most
\[
 \min\{\log(1+2e_-/d),\ \log(1+2e_+/d)\}.
\]
The upper bound uses the Green kernels of the containing half-planes
at \(X+ik\). Therefore vertical margins much smaller than the span
can erode even the exact Green signal. These losses concern the
stated uniform-error consumers and containing lines.

For an independently nonzero carrier and a uniform \(|F-1|<1\) on a
domain, direct nonvanishing already pays the whole domain. Hence
select bounded local rectangles and direct consumption when the
canonical input is a uniform relative estimate. The other consumers
give explicit conditional margins and could use different
information, such as a complete signed logarithmic boundary estimate
with an independent observation floor. A global strip or graph
integral would need that boundary estimate and the applicable
exhaustion payments. There is no reason from a uniform disk error
alone to incur them.

For an unbounded-height statement, apply a rectangle at **every real**
\(X\ge X_0\), with the canonical estimate and chart constants
uniform in \(X\). Its own centerline covers the target at that height.
There are no gaps from sampling centers, and each rectangle has
its full boundary. If \(\lambda=\lambda(X)\), the statement is on
that prescribed curve and the field is \(H_{\lambda(X)}\) throughout
each rectangle. Neighboring rectangles may use different times.
They cannot be combined into one Green identity for
\(z\mapsto H_{\lambda(\Re z)}(z)\). An exhaustion on a single graph
instead uses one fixed time throughout. Heights below \(X_0\) need
their own coverage on the relevant time domain.

A complete canonical estimate on the fractional rectangles with the
same error bound at every stage would support \(a_{n+1}=3a_n/4\).
For a fixed height on the chosen time curve, convergence to the line
requires every step there. An onset \(X_n\to\infty\) leaves at most
finitely many successive steps there. At a common time, the same
test requires a proof at that time for every step; at time zero, or
in a limit of positive times, it requires a separate passage with
the needed local uniform information. An asymptotic positive-time
curve theorem alone does not supply it. No geometry above supplies
a replacement for failing arithmetic allowances. The scoped
\(y>3/4\) restriction concerns [Note03's specific absolute estimates][baseline].
A next canonical acquisition can use any independently justified
strictly deeper fixed lower edge. Iteration additionally needs
carrier nonvanishing and actual complete field error on shrinking
collars, or a complete signed Green allowance below the local
target margin, with explicit stage and height dependence.

## 4. Collision-control premise screen

Geometry and both consumer inequalities are valid for controls when
their analytic premises hold. If a compared domain contains a
control zero, \(|F-1|\ge1\) there for a nonzero carrier, and a
control zero in the Green target contributes at least the target
floor. The screen concerns domains containing the tested zero or
bounds contradicted by its witness. The canonical arithmetic provider
has the following independent source requirements. [Cluster12][r12],
[Note03 §5][baseline].

| Control | Failed premise of the canonical provider |
| --- | --- |
| Euler-factor or translated theta source | Unchanged theta coefficients and identification with the ordinary zeta finite arm |
| Weighted-square and finite-tail sources | Full unit square coefficients with full reflection |
| Reflected super-Gaussian, smooth shape, and primitive-compatible controls | Complete normalized theta square arithmetic |
| Finite-prime orbit | Full reflection and agreement beyond the fixed primes and prefix |
| Atomic fixed-event, finite-profile and compact continuous controls | Full theta source and profile beyond selected measurements |
| RH-conditional normalized endpoint | Ordinary Dirichlet-series arithmetic |
| Fixed-amplitude variable readout | Actual cosine or Newman field |
| Polynomial heat localization diagnostic | Canonical theta source/provider |

Reflection rigidity applies with its full conjunction of hypotheses.
The premise screen licenses use of a canonical provider in its stated
domain. It supplies no pointwise arithmetic inequality by itself.

[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[baseline]: 03_GNP_BB_B01_COLLAR_COMPARISON_20261113.md
[program]: 05_GNP_BB_ANALYTICAL_PROGRAM_AND_SELECTION_PROTOCOLS_20261113.md
