# Positive tail orientation and a complete finite box certificate

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Coordinating model gpt-6-astra, reasoning effort ultra, as recorded by the parent session. The next phase implements the bounded positive-tail experiment proposed in [strategy 07](../00_research_coordination/07_RESEARCH_PATHS_AFTER_COUPLED_PRODUCT_20261015.md), following the [scalar stationary reduction](../01_physical_jet_geometry/03_SCALAR_STATIONARY_GEOMETRY_AND_INVARIANT_TRACE_20261015.md).

This uses the physical source and primitive identities already proved in Investigation 22. It proves a uniform complete-tail orientation on a compact domain. Full-field noncollision still requires a separately certified finite head. It proves no global theta sign or collision exclusion theorem.

## 1. Primitive moments with explicit mode decay

Write

\[
\lambda_n=\pi n^2,\qquad d_n=4\lambda_n-1,\qquad
p_n(u)=e^u e^{-\lambda_ne^{4u}},\qquad
\beta_n=d_ne^{-\lambda_n},\qquad
8\phi_n=p_n''-p_n.
\]

For \(T\ge 0\), assume \(\lambda_n\ge T/8\). Then, for all \(u\ge 0\),

\[
Tu^2\le\frac T8(e^{4u}-1-4u)
\le\lambda_n(e^{4u}-1-4u).
\]

Consequently

\[
\frac{p_n(u)}{\beta_n}e^{Tu^2}
=\frac1{d_n}\exp\{Tu^2+u-\lambda_n(e^{4u}-1)\}
\le\frac{e^{-d_nu}}{d_n}.
\tag{1}
\]

Thus every integer \(k\ge 0\) has the explicit moment bound

\[
P_{k,n}(T):=\frac1{\beta_n}\int_0^\infty
u^k p_n(u)e^{Tu^2}\,du
\le\frac{k!}{d_n^{k+2}}.
\tag{2}
\]

This estimate is sufficient for all compact real time intervals after finitely many modes, and it holds for every \(n\ge1\) when \(T\le1/2\). All integration-by-parts upper boundaries below vanish by the original double-exponential decay.

## 2. Uniform enclosure of the complete normalized mode vectors

For \(|t|\le T\), \(|x|\le X\), integration by parts twice against \(e^{tu^2}\cos(xu)\) gives

\[
\frac{H_n(t,x)}{\beta_n}
=\frac18+\frac18\int_0^\infty\frac{p_n(u)}{\beta_n}e^{tu^2}
\left[(2t+4t^2u^2-x^2-1)\cos(xu)-4txu\sin(xu)\right]\,du.
\tag{3}
\]

The lower boundary equals \(\beta_n/8\) because \(p_n'(0)=-\beta_n\), the test equals one at zero, and its first source derivative vanishes there. Using (2) and \(|\sin(xu)|\le X u\) gives

\[
\left|\frac{H_n(t,x)}{\beta_n}-\frac18\right|
\le a_n(T,X):=
\frac18\left\{
\frac{1+2T+X^2}{d_n^2}
+\frac{8(T^2+TX^2)}{d_n^4}\right\}.
\tag{4}
\]

Differentiating (3) with respect to x gives the exact identity

\[
\begin{aligned}
\frac{H_{n,x}(t,x)}{\beta_n}
=\frac18\int_0^\infty\frac{p_n(u)}{\beta_n}e^{tu^2}
\bigl[&-2x\cos(xu)\\
&-u(6t+4t^2u^2-x^2-1)\sin(xu)\\
&-4txu^2\cos(xu)\bigr]du.
\end{aligned}
\tag{5}
\]

Hence

\[
\left|\frac{H_{n,x}(t,x)}{\beta_n}\right|
\le b_n(T,X):=\frac18\left\{
\frac{2X}{d_n^2}
+\frac{2X(1+10T+X^2)}{d_n^4}
+\frac{96T^2X}{d_n^6}\right\}.
\tag{6}
\]

Therefore every normalized vector \(V_n=(H_n,H_{n,x})/\beta_n\) lies in

\[
[1/8-a_n,\ 1/8+a_n]\times[-b_n,b_n].
\tag{7}
\]

Both widths are \(O(n^{-4})\), explicitly and uniformly on the prescribed compact box. This proves the uniform limit \((1/8,0)\) and supplies shrinking complete-tail enclosures rather than only a mode-independent bound. The rectangles decrease as n increases. Take the closed convex hull of the union of tightly integrated early-tail rectangles, the rectangle (7) for all later modes, and the limit point. This encloses the complete normalized tail hull.

For comparison, a direct positive-source estimate also gives

\[
\frac1{\beta_n}\int_0^\infty u^k e^{Tu^2}\phi_n(u)\,du
\le\frac{2\lambda_n^2}{4\lambda_n-1}
\frac{k!}{(4\lambda_n-9)^{k+1}},
\tag{8}
\]

when \(\lambda_n\ge T/8\). This follows by discarding the negative term in \(\phi_n\), applying the same quadratic-exponent absorption, and using \(4\lambda_n-9>0\) for \(n\ge1\). Bound (8) can control quadrature remainders, but (4)–(6) retain the correct center \((1/8,0)\) more effectively.

## 3. A signed enclosure for every mode after the first

Now assume \(0\le t\le T\) and \(0<x\le X\). An elementary substitution gives a useful lower primitive mass. Put \(z=e^{4u}-1\); then

\[
\frac1{\beta_n}\int_0^\infty p_n(u)\,du
=\frac1{4d_n}\int_0^\infty(1+z)^{-3/4}e^{-\lambda_n z}\,dz.
\]

Convexity gives \((1+z)^{-3/4}\ge 1-3z/4\) for \(z\ge 0\). It follows that

\[
\frac1{\beta_n}\int_0^\infty p_n(u)\,du
\ge\frac1{4d_n}\left(\frac1{\lambda_n}-\frac3{4\lambda_n^2}\right)
=\frac{d_n-2}{d_n(d_n+1)^2}=:L(d_n).
\tag{9}
\]

Because \(t\ge0\) and \(\cos(xu)\ge 1-x^2u^2/2\),

\[
C_n(t,x):=\int_0^\infty\frac{p_n(u)}{\beta_n}e^{tu^2}\cos(xu)\,du
\ge L(d_n)-\frac{x^2}{d_n^4}.
\tag{10}
\]

In (5), the absolute value of the remaining two terms after \(-2x C_n\) is bounded by

\[
x(1+10T+X^2)P_{2,n}(T)+4T^2xP_{4,n}(T)
\le\frac{2x(1+10T+X^2)}{d_n^4}
+\frac{96T^2x}{d_n^6}.
\]

Combining this with (10) proves the explicit one-sided bound

\[
\boxed{
-\frac{H_{n,x}(t,x)}{\beta_n}
\ge\frac x4\left[
L(d_n)-\frac{1+10T+2X^2}{d_n^4}
-\frac{48T^2}{d_n^6}\right].}
\tag{11}
\]

No trigonometric sign assumption over the full integration interval is used.

For general \(T,X\), a sufficient tail-start condition is

\[
d_*>2,\qquad \lambda_*\ge T/8,\qquad
\frac{d_*^3(d_*-2)}{(d_*+1)^2}
>1+10T+2X^2+\frac{48T^2}{d_*^2}.
\tag{11a}
\]

The left side increases for \(d>2\), since its logarithmic derivative is \(3/d+1/(d-2)-2/(d+1)>0\); the last term on the right decreases. Therefore verifying (11a) at the first retained mode proves strict orientation for every subsequent mode. This is an explicit scalable finite-index test, with no search over infinitely many tail vectors.

Take \(T=1/2\), \(X=30\), and \(n\ge 2\). Since \(\pi>3\), \(d_n>47\). Multiplying the bracket in (11) by \(d_n^2\) gives

\[
f(d_n):=\frac{d_n(d_n-2)}{(d_n+1)^2}
-\frac{1806}{d_n^2}-\frac{12}{d_n^4}.
\]

This function increases for \(d\ge 47\): the first term is \(1-(4d+1)/(d+1)^2\), whose derivative is \((4d-2)/(d+1)^3>0\), and both negative reciprocal powers increase. Exact rational arithmetic gives

\[
f(47)=\frac{125421739}{1249198336}>\frac1{10},
\qquad
f(47)-\frac1{10}=\frac{2509527}{6245991680}>0.
\]

Therefore

\[
\boxed{
-\frac{H_{n,x}(t,x)}{\beta_n}
>\frac{x}{40(4\pi n^2-1)^2}>0,
\quad n\ge2,\quad 0\le t\le\frac12,\quad 0<x\le30.}
\tag{12}
\]

The complete tail points lie strictly in the negative second-coordinate half-plane, while their required limit point lies on its boundary. Thus the closed convex hull has

\[
\inf_{n\ge2} (0,-1)\cdot V_n=0,
\]

The infimum equals zero because \(V_n\) tends to \((1/8,0)\), while every finite n has strictly positive pairing. No positive margin uniform in all n is claimed; the lower bound tends to zero with n.

## 4. Frozen pilot and outcome

Use the exact box

\[
0.009\le t\le0.011,\qquad 28.2\le x\le28.4,
\]

retain only mode 1 as the fixed head, and prescribe the separator \(\lambda=(0,-1)\). Exploration evaluated the first four normalized modes near the box center; these choices were frozen before the replay checker was written. The checker performs no optimization or root search. No failed certificate candidate was suppressed.

The uniform analytic tail argument in Section 3 proves

\[
H_{n,x}(t,x)<0\qquad(n\ge2)
\]

throughout this box. The complete tail vectors \(V_n=(H_n,H_{n,x})/\beta_n\) tend uniformly to \((1/8,0)\). Therefore

\[
\inf_{n\ge2}\lambda\cdot V_n=0,
\]

with the infimum supplied by the required limit point in the closed cone. Arb integration and a full parameter-error bound certify

\[
-H_{1,x}\in[8.44278420683205418\times10^{-5}\ \pm\ 5.58\times10^{-6}].
\]

Thus the positive-tail separator is strictly positive on the entire box. In particular \(H_x<0\) for every normalized positive-tail relaxation with \(a_1=1\).

This successful sign argument actually does **not** require the primitive endpoint normalization or the coefficient recurrence. It applies to any nonnegative tail weights with \(a_1=1\), whenever their derivative transform converges: adding the tail can only make the derivative more negative. Consequently this pilot supplies no theta-specific arithmetic discrimination.

For the actual equal-weight theta field, additional complete-source and complete-mode enclosures give

\[
\begin{aligned}
H(t,28.2)&\in[5.36025198799804\times10^{-6}\ \pm\ 3.66\times10^{-6}],\\
H(t,28.4)&\in[-1.15847491148620\times10^{-5}\ \pm\ 3.66\times10^{-6}].
\end{aligned}
\]

These hold for every time in the box. Continuity and the derivative sign therefore give exactly one real theta zero within this spectral interval at each such time. This is a local bracket near the expected first zero; the checker does not prove that no earlier zero exists outside the box.

## 5. What the validated integration covers

The checker integrates the normalized source directly:

\[
\frac{e^{tu^2+u-\lambda_n(e^{4u}-1)}}{4\lambda_n-1}
 (2\lambda_n^2e^{8u}-3\lambda_ne^{4u}),
\qquad \lambda_n=\pi n^2.
\]

The finite source interval is \([0,1]\). For moments through order 5, the absolute remaining source tail is bounded by

\[
\tau_n=\frac{\lambda_n}{4\lambda_n-1}
 \exp\left(\lambda_n-4-\frac{\lambda_n e^4}{2}\right).
\]

Indeed, for \(u\ge1\), \(t\le1/4\), and \(0\le k\le5\),

\[
k\log u+tu^2+9u
\le\tfrac14 e^{2u}+14e^u
\le\tfrac{\lambda_n}{2}e^{4u}.
\]

The last inequality is checked at \(u=1,n=1\), where its left-to-right ratio is largest. Convexity gives \(e^{4u}\ge e^4[1+4(u-1)]\) for \(u\ge1\), so

\[
\int_1^\infty e^{-\lambda_n e^{4u}/2}\,du
\le\frac{e^{-\lambda_n e^4/2}}{2\lambda_n e^4}.
\]

Multiplying by the source prefactor \(2\lambda_n^2e^{\lambda_n}/(4\lambda_n-1)\) gives \(\tau_n\). Every finite integral includes this allowance; the computation does not truncate the starting field without its tail.

Parameter uncertainty is paid with a second-order Taylor bound, not by sampling. At the midpoint \((t_c,x_c)=(0.01,28.3)\), let \(c_j=h_{j,n}/\beta_n\), and let \(M_j\) be a complete positive source-moment bound at \(T=0.011\). With \(d_t=0.001,d_x=0.1\),

\[
\left|\frac{h_{j,n}(t,x)}{\beta_n}-c_j\right|
\le d_x|c_{j+1}|+d_t|c_{j+2}|
 +\frac{d_x^2}{2}M_{j+2}+d_xd_tM_{j+3}
 +\frac{d_t^2}{2}M_{j+4}.
\]

This follows from \(\partial_t h_j=-h_{j+2}\) and the complete Hessian bounds on the line segment joining each point to the midpoint. For the two endpoint signs, the signed linear spatial term is retained before the same remainder is added.

Modes 2, 3, and 4 are optionally enclosed individually to display the finite tail geometry. All modes \(n\ge5\) lie in the preceding explicit shrinking rectangle around \((1/8,0)\). The exact remaining endpoint mass is \(R_4=1/2-\sum_{n\le4}\beta_n\), evaluated with enough precision to certify positivity. The closed convex hull of those finite rectangles, the infinite rectangle with its additional negative-derivative half-plane restriction, and the limit point encloses the entire normalized tail hull over the box.

## 6. Comparison and stopping decision

All three methods use the same validated head enclosure. With \(R_1=1/2-\beta_1\), the ordinary directional cutoff pays \(R_1\sup_{n\ge2}|H_{n,x}/\beta_n|\). A deliberately coarser radial cutoff pays \(R_1\sup_{n\ge2}\|V_n\|\). The preceding uniform bounds give:

| Method | Certified separator enclosure |
|---|---|
| Positive tail cone | \(8.44278420683205\times10^{-5}\ \pm\ 5.58\times10^{-6}\) |
| Ordinary directional complete-start cutoff | \(8.37580089357755\times10^{-5}\ \pm\ 5.58\times10^{-6}\) |
| Ordinary radial complete-start cutoff | \(5.57982750435037\times10^{-5}\ \pm\ 5.58\times10^{-6}\) |

Every lower endpoint is positive. The cone removes a small directional tail penalty, but both ordinary cutoffs already certify the same box. Each needs no extra tail quadrature after the common head integrals. Accordingly no computational advantage is demonstrated here.

The 160-bit run uses 32 small validated integrals: eight head integrals, and 24 optional finite-tail diagnostics used for the displayed cone rectangles and theta root bracket. It passes **52 assertions** with timings recorded as indicative single-run measurements, not a performance guarantee. Three exact rational checks also verify the preceding stronger uniform tail-orientation threshold on \([0,1/2]\times(0,30]\):

\[
f(47)=\frac{125421739}{1249198336},\qquad
f(47)-\frac1{10}=\frac{2509527}{6245991680}>0.
\]

This supports \(-H_{n,x}/\beta_n>x/[40(4\pi n^2-1)^2]\) for every \(n\ge2\) on that broader rectangle; it does not enlarge the certified head box. The certificate is reproducible with `python-flint` 0.9.0 using `check_positive_tail_cone.py --output POSITIVE_TAIL_CONE_CHECKS_20261015.json`. Its receipt records library/runtime versions, exact inputs, all integral and source-tail enclosures, the infinite-tail proof parameters, costs, scope, and the checker hash. Two independent internal analytic audits found no issue. The final 52-check script was independently replayed, and its mathematical receipt matched after removing only the three elapsed-time fields. The checker hash is `6cc280db4d51ae9f49e474c826946ef76c34b3561677a7113216a81caf64eb4b`.

The next source problem remains an arithmetic signed estimate that survives where a componentwise positive-mixture sign argument fails. This pilot does not supply the all-event boundary estimate, an exterior-domain certificate, or a reason to enlarge the finite cone machinery.


## 7. Reproducibility and scope

The [portable checker](../../numerics/check_positive_tail_cone.py) and [receipt](../../numerics/POSITIVE_TAIL_CONE_CHECKS_20261015.json) retain the exact box, fixed separator, all complete integral enclosures and the required tail limit. The [integration and continuation manifest](../../numerics/SCALAR_MANUSCRIPT_AND_TAIL_CONE_CHECKS_20261015.json) binds their identities and the independent replay. The [internal review](../../reviews/12_SCALAR_MANUSCRIPT_AND_TAIL_CONE_REVIEW_20261015.md) records separate analytic and numerical checks.

The broad tail theorem is analytic; finite rational checks verify its displayed threshold, not its universal quantifiers. The finite head and root bracket are validated by interval arithmetic over the full box. This local box lies within the previously investigated finite-height range and does not close any global coverage gap. The new tail theorem and finite certificate remain incremental research in this note; the accompanying manuscript integration promotes the previously reviewed scalar geometry and joint-current results.
