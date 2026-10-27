# Real endpoint transport and a finite complete count

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**. Same HCB chat0001, thread `01a17aca-de9a-7533-9bb8-8ee0e9bdb282`.

**Status: generic estimates proved in-note under the stated real-zero
premises; one finite interval-arithmetic witness under RH; separate-agent
same-model internal review. No specialist validation.** The unchanged
family now has an acquired canonical wall/count member at **m=16**.
Uniform-in-m endpoint bounds and counts remain open. This is a bounded
method comparison in an RH all-real region, not a new RH/Newman result.

The [fixed protocol][protocol] preceded every source-value evaluation.
Its first contour integral returned a nonfinite enclosure within the
fixed allowance, and the [original source run][raw] remains **stopped**.
A separate [witness][witness] deduces the count from completed earlier
data, without another source evaluation or retry. The failed integration
is not presented as successful. [Review04][review] checks the proofs,
implementation and this distinction.

Read the [result index][results], [collision controls][controls] and
[avoid index][avoid], especially [target classification][a01], [scope][a07]
and [counting checks as evidence][a04]. The gain is the actual finite
margin/count and explicit transport estimate. No novelty claim is made
for canonical products, Gaussian evolution or elementary integer bounds.

## 1. Unchanged coordinates and acquired finite data

Keep [Notes03–04][n04]'s exact family and normalization:
\[
 X=4\pi e^m,\quad L=m,\quad u=L(z-X),\quad\tau=tL^2,
 \quad\tau_X=X^{-1/4},\quad
 h_X(\tau,u)=H(\tau/L^2,X+u/L)/A_o(0,X),
\]
\[
 \Gamma=\partial([-4,4]+i[-2,2]),\qquad 0\le\tau\le\tau_X.
 \tag{1}
\]
All canonical zeros are real on this interval under RH. The finite
result uses **exactly m=16**, without shifting either endpoint or wall.
The witness establishes under RH
\[
 \inf_{0\le\tau\le\tau_X}|h_X(\tau,-4)|>0.8144,\quad
 \inf_{0\le\tau\le\tau_X}|h_X(\tau,4)|>0.2789,
 \tag{2}
\]
\[
 n(\tau)=1\ \text{counted with multiplicity},\qquad
 \inf_{[0,\tau_X]\times\Gamma}|h_X|>0.0697. \tag{3}
\]
These are canonical-field statements. They do not instantiate Note03's
\(F_N\) error constant or transfer the floor to that arithmetic model.
Their source is the complete initial \(\xi/8\), evaluated in balls,
and exact heat transport below. No zero database, selected root disks,
internal separation or root-slope denominator is an input.

## 2. A global real-endpoint Gaussian estimate

Let \(F(u)=h_X(0,u)\), let \(c\in\mathbb R\) with \(F(c)\ne0\), and put
\[
 A=F'(c)/F(c)\in\mathbb R,\qquad
 Q=-(\log F)''(c)=\sum_r(c-r)^{-2}\ge0. \tag{4}
\]
This is not a simplicity premise.
Every real microscopic zero occurs with multiplicity. The paired
order-one canonical product gives for every real \(v\)
\[
 \frac{F(c+iv)}{F(c)}=\exp\{ivA+D(v)\},\qquad
 |D(v)|\le v^2Q/2. \tag{5}
\]
For each real \(s=c-r\ne0\), integrate the derivative of
\(\log(1+it)-it\) along real \(t\) to get
\(|\log(1+it)-it|\le t^2/2\). Its zero-free vertical path fixes
the branch. Summing the remainders is absolutely convergent by (4);
the paired first derivative supplies \(A\). Any real linear exponential
factor is retained there. No finite-v truncation occurs.

The exact-source Gaussian identity has variance \(2\tau\), so (5)
and its characteristic function give, whenever \(2\tau Q<1\),
\[
 \boxed{\left|\frac{h_X(\tau,c)}{F(c)}-e^{-\tau A^2}\right|
 \le(1-2\tau Q)^{-1/2}-1.} \tag{6}
\]
Indeed \(|e^{D(v)}-1|\le e^{v^2Q/2}-1\), whose entire Gaussian
integral is the right side. Thus no tail allowance is hidden.
A monotone sufficient error from one is
\[
 E_c(\tau)=1-e^{-\tau A^2}+(1-2\tau Q)^{-1/2}-1. \tag{7}
\]
If \(E_c(\tau_X)<1\), the whole-interval endpoint floor is
\(|F(c)|(1-E_c(\tau_X))\). For \(\tau Q\le1/4\), the simpler
upper bound is \(E_c(\tau)\le\tau A^2+2\tau Q\).
This reduces a time-uniform requirement to certified initial value and
two logarithmic jets. It does not assert that they are favorable on
every member of the family.

For context, an initial endpoint distance \(d\le1\), the canonical
unit-interval count and paired tails give
\(|A|\ll L(1+d^{-1})\), \(Q\ll Ld^{-2}+L^{-1}\).
Therefore \(d/(L\sqrt{\tau_X})\to\infty\) is one sufficient
clearance for vanishing relative time error. This is a boundary
clearance, not an internal root-gap assumption.

## 3. What safe corner data can supply

Write \(D_b(c)=F'(c+ib)/F(c+ib)\), and retain *all* real zeros in
\[
 P_b(c)=-\Im D_b(c)=\sum_r\frac b{(c-r)^2+b^2},\quad
 \beta=bP_b(c).
\]
If \(\beta\le1-\delta<1\), the real-zero product implies
\[
 \frac{|F(c)|^2}{|F(c+ib)|^2}
 =\prod_r\left(1-\frac{b^2}{(c-r)^2+b^2}\right)
 \ge1-\beta\ge\delta. \tag{8}
\]
The product inequality follows for finite products and passes to the
limit since the nonnegative sum is finite. It also gives
\[
 d^2\ge\frac{b^2\delta}{1-\delta},\quad
 Q\le\frac{1-\delta}{b^2\delta},\quad
 |A|\le|\Re D_b(c)|+\frac{(1-\delta)^{3/2}}{b\sqrt\delta}. \tag{9}
\]
For the last bound, subtract the real part of the corner quotient from
\(A\), then bound the convergent sum
\(\sum_r b^2/[(c-r)((c-r)^2+b^2)]\) by \(\beta/d\).

In particular \(b=2\), \(P_2(c)\le3/8\) gives an amplitude factor
at least \(1/2\), distance at least \(2/\sqrt3\), \(Q\le3/4\), and
\(|A|\le|\Re D_2(c)|+3\sqrt3/8\). Together with Note04 this would
give the full-time endpoint floor \(X^{-1/2-o(1)}\), if that arithmetic
corner inequality were proved uniformly. **It has not been proved
uniformly for the frozen sequence.** The generic \(P_2=O(L)\) upper
bound is insufficient.

This test is source-stable. Note04's proof extends uniformly to the
fixed strip \(|\Re u|\le5\), \(1\le\Im u\le3\), with the same
\(X^{-1/2-o(1)}\) floor: the kernel offset is \(b/(2L)\), with
\(b\) in a fixed interval bounded away from zero. Let
\(\nu=-\log(1-e_{\rm src}/m_{\rm strip})\), where the model strip
floor is \(m_{\rm strip}\). On the entire upper strip, and hence the unit disks about its two corners,
\(\ell=\operatorname{Log}(h_X/f_X)\) is a single bounded holomorphic
branch with \(|\ell|\le\nu\),
and Cauchy gives \(|D_h-D_f|\le\nu\le X^{-1/4+o(1)}\).
Thus the actual model test must pay its corner error, e.g.
\(P_f+\nu\le3/8\), not silently apply the exact-field inequality.

## 4. Integer count without internal root locations

For any real root \(r\in[-4,4]\), its two-corner contribution satisfies
\[
 \frac2{(r+4)^2+4}+\frac2{(r-4)^2+4}
 =\frac{4(r^2+20)}{r^4-24r^2+400}\ge\frac15. \tag{10}
\]
Subtracting \(1/5\) leaves
\(r^2(44-r^2)/[5(r^4-24r^2+400)]\ge0\). Every exterior root
contributes positively too. Consequently the complete count obeys
\[
 n\le5\{P_2(-4)+P_2(4)\}. \tag{11}
\]
If this upper bound is below two and the real endpoint signs are
opposite, the intermediate value theorem supplies one root and the
integer/multiplicity upper bound gives **exactly one**. No claim that
endpoint signs alone determine the count is made. If both corners
only meet the weaker \(3/8\) gateway, (11) gives \(n\le3\).

For that wider case a fourth-order Poisson filter is another exact
count interface. With the upper horizontal integral oriented left to
right, set
\[
 C_2=\frac{-\Im\int_{-4}^{4}(F'/F)(x+2i)\,dx
 +2\Re\{(F'/F)(4+2i)-(F'/F)(-4+2i)\}}\pi.
\]
It integrates the positive kernel
\(2b^3/[\pi(s^2+b^2)^2]\) at \(b=2\). The tail is
\([\arctan(b/s)-bs/(s^2+b^2)]/\pi\). Dividing it by the corner
Poisson kernel gives a decreasing function of \(s/b\). Using the
gateway distance \(s\ge2/\sqrt3\) and summing both endpoint tails
over all roots therefore gives
\[
 |n-C_2|\le2/3-\sqrt3/(2\pi)<1/2. \tag{12}
\]
This leaves arithmetic allowance less than
\(\sqrt3/(2\pi)-1/6\) for integer isolation. The model source payment
is at most \(6\nu/\pi\): the integral of \(\ell'\) is the endpoint
log difference, and the two corner derivative errors cost \(4\nu\).
All exterior zeros remain in this filter and its leakage bound.
This optional continuous-integration stage did **not** succeed in
the finite run; (11) is the route used for its post-stop count.

## 5. From endpoint floors and complete count to the whole wall

At any fixed time suppose the complete real population in \((-4,4)\)
has count \(n\), and both real endpoints have modulus at least \(E>0\).
Factor \(h_X=P G\), with monic \(P\) containing exactly those roots.
The exterior real entire factor \(G\) has no zeros on \([-4,4]\),
and its order-one real-zero product gives
\[
 (\log|G(x)|)''=-\sum_{r\ \mathrm{exterior}}(x-r)^{-2}\le0.
\]
Thus \(|G(x)|\ge\min(|G(-4)|,|G(4)|)\ge E/8^n\).
Real-zero modulus monotonicity for \(G\), including its real linear
exponential factor, gives \(|G(x+2i)|\ge|G(x)|\), while
\(|P(x+2i)|\ge2^n\). The vertical sides have their minima at the
real endpoints. Therefore
\[
 \boxed{\inf_{u\in\Gamma}|h_X(\tau,u)|\ge E/4^n.} \tag{13}
\]
The exterior unit has been used through its concavity, not declared
constant or discarded. Internal repeated roots are allowed. The
argument is pointwise in time and needs no chosen root labels.

## 6. Fixed m=16 execution and verified consequence

The initial source was exactly \(H(0,z)=\xi((1+iz)/2)/8\), evaluated
with python-flint **0.9.0**, **192 bits**, using its complete gamma
and zeta factors and analytic logarithmic derivatives through order two.
The script and raw record retain the precise formulas, outward balls,
source hash, limits and failure. The source run took about **48.3 s**;
that timing describes this run, not a complexity theorem.

The completed data include

| Datum | Conservative consequence of the outward ball |
| --- | --- |
| \(F(-4)\) | positive, greater than 0.8150 |
| \(F(4)\) | negative, modulus greater than 0.2797 |
| \(P_2(-4)\) | less than 0.111 |
| \(P_2(4)\) | less than 0.254 |
| Endpoint errors (7) at \(\tau_X\) | left below 0.000709; right below 0.002772 |
| Uniform endpoint floors | left above 0.8144; right above 0.2789 |

The first continuous edge integral returned a nonfinite enclosure with
the fixed 4096-evaluation allowance; the run stopped without a retry,
precision increase, different height or later C_2 calculation. The
raw status remains stopped. A separate post-stop witness plan was
recorded before verifying the retained data.

The [witness verifier][verifier] hashes the raw record and original
script, parses the outward printed balls and recomputes the endpoint
inequalities. It uses **zero new source evaluations**. Its two-corner
sum is enclosed near
\(0.3640165847965266965\), so (11) gives
\(n<1.820083<2\). Opposite endpoint signs then give \(n=1\), counted
with multiplicity. Under RH, the positive endpoint floors prevent
crossings throughout (1), and all zeros remain real, so this complete
count is constant on the entire interval.

Finally (13) gives \(E/4=0.2789/4=0.069725>0.0697\), proving (3).
The original failed integral is not needed for this separately identified
inference. No assertion count or high precision is offered as evidence
in place of these margins. No source values beyond the one fixed case
were executed.

## 7. Remaining scope and controls

HCB-02 is **Partial**, with a finite canonical endpoint/wall/count witness.
For all sufficiently large \(m\), the missing input is still an actual
corner budget or real endpoint jet/value estimate at the prescribed
heights. Neither the one case nor the generic lemmas proves it.
The finite source is exact initial \(\xi\), followed by conditional
canonical heat transport; Note03's retained \(F_N\) conversion, monic
coefficient errors and favorable continuous second moment remain unpaid.
The asymptotic horizontal floor alone still does not pay its two-root
Poisson demand, and Note04's n≥6 fallback exclusion retains its scope.

The global product/heat lemmas pass admissible all-real polynomial
collision controls. A boundary zero makes the endpoint premise fail;
an interior multiple zero contributes its multiplicity to (11).
No internal separation was assumed to reject it. The unchanged complete
theta arithmetic distinguishes the actual evaluations from Euler-factor,
weighted-square/finite-tail, reflected/positive-primitive, finite-prime/
profile and theta-close endpoint controls as specified in [cluster12][controls].
No control certificates were rerun, and no specialist review occurred.

The next uniform task is a justified corner or real-jet bound for the
frozen sequence; the next finite implementation task, if selected, is
to specify a new bounded protocol before another source evaluation.
There is no ongoing sweep. Keep the same-source direct/J comparison
and the [sole progress register][progress].

[n04]: 04_HORIZONTAL_WALL_ACQUISITION_AND_ENDPOINT_COUNT_20261026.md
[protocol]: 05_ENDPOINT_COUNT_PILOT_PROTOCOL_20261026.md
[raw]: ../numerics/FROZEN_ENDPOINT_COUNT_RECORD_20261026.json
[witness]: ../numerics/RETAINED_ENDPOINT_COUNT_WITNESS_20261026.json
[verifier]: ../numerics/02_verify_retained_endpoint_count_20261026.py
[review]: ../reviews/04_REAL_ENDPOINT_AND_FINITE_COUNT_INTERNAL_REVIEW_20261026.md
[progress]: ../research-progress/01_COLLISION_BOUNDS_RESEARCH_PROGRESS_20261026.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a04]: ../../../../avoid/04_counts_and_precision_as_evidence.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
