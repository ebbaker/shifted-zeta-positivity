# A certified heat cell containing a simple real zero

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred. Internal
verification and same-model review are not independent specialist validation.

**The next bounded heat checkpoint is met.** For every
\(t\in[1/5,3/10]\), the function \(H_t\) has exactly one real zero in
\((4005.2,4005.8)\), and that zero is simple. On the full rectangle the
symmetric normalized function of [Note 3](3_NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md)
satisfies the certified inequalities

\[
\boxed{\quad Q'_t(x)>2.3\quad
 (1/5\le t\le3/10,\ 4005.2\le x\le4005.8),\quad}
\tag{1}
\]
\[
Q_t(4005.2)<-0.44,\qquad Q_t(4005.8)>0.59.
\tag{2}
\]

The sign change proves existence for every time, while (1) proves uniqueness
and simplicity. At a zero, \(H'_t=A_tQ'_t\ne0\), because \(A_t>0\) on
the real axis. Thus this is a cell containing actual zeros, with useful
derivative control, beyond Note 4's value-positive rectangle. Evenness gives
the corresponding statement on the reflected negative interval.

These conclusions use the imported effective approximation theorem and
Note 3's analytic disk error, with explicit outward interval evaluation.
They establish a local real-zero statement at a fixed positive time floor;
they do not cover the complete finite-height interval, exclude all complex
zeros, improve the Newman constant, or control the limit toward time zero.

## 1 Analytic inputs and the fixed cutoff

The source is [Polymath, Theorem 1.3 and equations 19–24](https://arxiv.org/html/1904.12438#S1.Thmtheorem3),
checked in the primary arXiv text on 9 October 2026. Its stated domain is
\(0<t\le1/2\), \(x\ge200\), \(0\le y\le1\). Note 3 supplies the
holomorphic fixed-cutoff formula, symmetric normalizer, reflected error and
Cauchy derivative estimate. Those analytic inputs remain imported or inherited
proof obligations with the status stated there.

Use the uniform parameters

\[
X=4005.5,\quad R=0.7,\quad a=0.3,\quad
\varepsilon=0.2,\quad\tau=0.3,\quad N=17.
\tag{3}
\]

The outer disks have real part at least \(4004.8>200\) and imaginary part
at most \(0.7<1\) in modulus. Their entire enclosing rectangle has natural
cutoff 17: outward evaluation encloses
\(x/(4\pi)+t/16\) strictly between \(17^2\) and \(18^2\).
Consequently the cutoff correction in Note 3's equation (14) is empty.
Unlike Note 4, this cell does not cross a cutoff. Keeping the single cutoff
17 nevertheless remains essential to the holomorphic derivative argument.

The 50-digit record gives, rounded outward here,

\[
0.55384522254735808682286242265157
 <\eta_{17}<
0.55384522254735808682286242265158<0.554.
\tag{4}
\]

Thus \(|Q_t-F_{t,17}|\le\eta_{17}\) throughout each outer disk. On the
inner real interval Cauchy's formula gives

\[
|Q'_t-F'_{t,17}|\le\eta_{17}/(R-a)<1.385.
\tag{5}
\]

The disk error is uniform over the complete time interval in (3), before
any time subdivision. Reflection below the real axis is paid through the
symmetric normalizer exactly as in Note 3.

## 2 Direct differentiation improves interval evaluation

Retain Note 4's real variables \(d=1+x^2\), \(\alpha_r,\alpha_i\),
\(a_n,\phi_n\) and \(F_{t,N}=2\sum_{n\le N}a_n\cos\phi_n\).
Write the real and imaginary components of the complex derivative
\(\alpha'(s)\) as

\[
u=6(x^2-1)/d^2+1/d,\qquad v=4x/d^2+x/d.
\tag{6}
\]

Because \(s=(1-ix)/2\), the real spatial derivatives satisfy
\(\partial_x\alpha_r=v/2\) and
\(\partial_x\alpha_i=-u/2\). Also
\(\partial_x\theta=-\tfrac12\operatorname{Re}m'_t(s)\). Hence, with
\(l_n=\log n\),

\[
L_n=(\alpha_r-l_n)(1+tu/2)-\alpha_i tv/2,
\qquad \partial_x\phi_n=-L_n/2,
\qquad \partial_xa_n/a_n=-tv l_n/4.
\tag{7}
\]

Direct differentiation gives the exact real formula

\[
\boxed{\quad F'_{t,N}(x)=\sum_{n\le N}a_n
 \left[L_n\sin\phi_n-\frac{tv l_n}{2}\cos\phi_n\right].\quad}
\tag{8}
\]

This agrees algebraically with Note 4's \(G'/A-bF\). In that representation
the cosine coefficient is \(\operatorname{Im}\lambda_n-2b\), exactly
\(-tv l_n/2\). Simplifying this cancellation before interval evaluation
reduces dependency inflation; it introduces no new analytic approximation.
The checker verifies the rational coefficient cancellation in 216 cases and
compares both formulas at 20 exact time/height points with overlapping outward
enclosures. The proof of equality is (6)–(8), not those finite comparisons.

## 3 Closed interval coverage and the zero statement

The [checker](../../numerics/check_zero_bearing_heat_cell.py) imports the
existing interval backend and disk error from
`check_fixed_heat_checkpoint.py`. Run from the repository root:

```sh
python3 papers/quasi-rh-exponent-descent/numerics/check_zero_bearing_heat_cell.py
```

It prints JSON without modifying files. The retained
[small record](../../numerics/zero_bearing_heat_cell_record_20261009.json)
can be compared with a new stdout record. Every input decimal is exact.
Directed Decimal operations, widened correctly rounded elementary functions,
the Machin enclosure of pi and Taylor remainders for trigonometric functions
are the same as in Note 4. No floating point, sampled derivative or numerical
quadrature enters the certificate. The documented
[Decimal guarantees](https://docs.python.org/3/library/decimal.html) remain
software inputs.

Thirty closed spatial intervals of width \(0.02\) and twenty closed time
intervals of width \(0.005\) cover the rectangle. Formula (8) is evaluated
on all 600 full cells. The lower bound over those cells is

\[
F'_{t,17}>3.70369693788561627638561691122419.
\tag{9}
\]

Subtracting the full upper error in (5), with directed rounding, gives

\[
Q'_t>2.31908388151722105932846085459526>2.3.
\tag{10}
\]

The two spatial endpoints are each enclosed on all twenty closed time cells.
Their worst finite-approximant values satisfy

\[
F_{t,17}(4005.2)<-1.00070755527001164680391657716326,
\quad F_{t,17}(4005.8)>1.14811396910029846563530687173480.
\tag{11}
\]

Paying (4) proves the stronger endpoint bounds
\(Q_t(4005.2)<-0.4468623327\) and
\(Q_t(4005.8)>0.5942687465\), where these displayed decimal endpoints are
again rounded outward. Equations (1)–(2) follow. The intermediate value
theorem and strict increase now prove exactly one zero in the open spatial
interval for each time. Its simplicity follows at the zero, as explained
above. These are statements about \(H_t\), rather than just the finite
approximant, because both value and derivative errors have been paid.

## 4 Scope and the next finite task

This completes the requested zero-containing derivative checkpoint without a
new approximation theorem or higher correction term. The useful computational
change is cancellation in the exact differentiated formula before interval
evaluation, combined with a height where the existing analytic error is small
enough. It remains a modest local result.

The next bounded heat task is an explicit finite cover at a specified positive
time floor, mixing value and derivative alternatives and paying every cutoff
crossing. A feasible height range should be fixed before starting that cover.
Neither this cell nor any one finite cover addresses the unbounded growth of
the remaining interval as the time floor tends to zero. The mixed-character
arithmetic estimate remains the main program priority.
