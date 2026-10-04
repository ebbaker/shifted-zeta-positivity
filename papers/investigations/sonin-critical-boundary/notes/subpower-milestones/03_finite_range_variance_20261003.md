# Complete finite-range quadratic variance bounds

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Separate same-model agents checked the transfer and constants. These are
internal checks, not independent specialist refereeing.

This continuation proves a finite milestone for the
[subpower program](README.md): quadratic upper bounds on the exact
variance throughout very large, explicitly bounded continuous ranges.
It reuses existing rigorous calculations rather than enumerating new
zeros or prime sums. The first fixed global delta below one remains open.

## The finite theorem

Keep the exact normalized g, complete w, and Vcal_g from the
[baseline note](01_baseline_and_exponent_budget_20261003.md). Then:

\[
\boxed{\begin{aligned}
\mathcal V_g(X)&<38X^2 &&(e\le X\le10^{99}),\\
\mathcal V_g(X)&<40X^2 &&(e\le X\le10^{100}),\\
\mathcal V_g(X)&<72X^2 &&(e\le X\le10^{102}).
\end{aligned}}
\tag{1}
\]

Every endpoint and every real X in each interval is included. The
published finite-height RH verification is a proved input; global RH is
not assumed. These are consequences of earlier project certificates,
not a new zero-location theorem or a claim of mathematical priority.

## The linear explicit-formula allowance

Use the manuscript's plus-exponent transform G(z)=integral g(v) exp(zv)dv.
The complete linear explicit formula from
[selective-loss note 05](../selective-loss-program/05_quadratic_target_and_finite_sign_20261003.md)
gives for y>a=1/4:

\[
p_g(y)=-\sum_\rho m_\rho G(1/2-\rho)e^{(\rho-1/2)y}
       -\sum_{k\ge1}G(2k+1/2)e^{-(2k+1/2)y}.
\tag{2}
\]

Both signs of the ordinate and all multiplicities occur. The pole at one
is canceled by preparation. The sixth distributional derivative of g
gives |G(z)|<=K exp(|Re z|/4)|z|^-6, with the already established
K=9470610144359/sqrt(nu). In particular, the linear coefficient tail has
sixth-power decay. The twelfth-power bound for G(z)G(-z) cannot be used
for this linear signal.

The zero-count theorem of
[Hasanalizade, Shen and Wong, Corollary 1.2](https://arxiv.org/pdf/2107.06506)
implies N(t)<=t log(t) for t>=100, where N counts positive ordinates with
multiplicity. Stieltjes integration by parts, counting both signs, gives

\[
\sum_{|\Im\rho|>H}m_\rho|\Im\rho|^{-6}
\le12H^{-5}\left(\frac{\log H}{5}+\frac1{25}\right).
\tag{3}
\]

[Platt and Trudgian, Theorem 1](https://arxiv.org/pdf/2004.09765)
rigorously verify critical-line location through the height used here,
H=3*10^12. The existing 192-bit and 256-bit records certify all 269
positive zeros below L=500 and the absolute linear coefficient mass
including both signs, S_500. Define

\[
b=S_{500}+12K\,500^{-5}
       \left(\frac{\log500}{5}+\frac1{25}\right)
       +\frac{\sqrt{1/2}\,e^{-15/8}}{1-e^{-3/2}},
\]
\[
R_H=12K e^{1/8}H^{-5}
          \left(\frac{\log H}{5}+\frac1{25}\right).
\tag{4}
\]

The middle term in b bounds the finite critical segment from 500 to H
by an infinite counting majorant; it does not assume criticality above
H. The last term bounds the trivial-zero sum for every y>=1. The high
zeros have exp((Re rho-1/2)y)<=exp(y/2). Thus the earlier proof actually
provides, with no upper restriction on y,

\[
\boxed{|p_g(y)|\le b+R_H e^{y/2}\quad(y\ge1).}
\tag{5}
\]

The earlier note rounded (5) on y<=225 for a signed-pair result. Here
we retain its dependence on y. Its existing outward records imply the
strict rational roundings

\[
b<\frac{124}{25}=4.96,\qquad
R_H<\frac{39}{25}10^{-51}=1.56\,10^{-51}.
\tag{6}
\]

## Exact integration over the whole shell

Since V_g(x)=sqrt(x) p_g(log x), (5) gives
|V_g(x)|<=b sqrt(x)+R_H x for x>=e. Integrating its square on the
complete physical interval [X,2X] yields

\[
\boxed{\mathcal V_g(X)\le
\frac32b^2X^2+
\frac45(2^{5/2}-1)bR_H X^{5/2}
+\frac73R_H^2X^3\quad(X\ge e).}
\tag{7}
\]

There is no packet truncation or replacement of the caps by complete
packets. The response itself, rather than its individual prime pairs,
was bounded before integration.

The normalized right side of (7) is increasing in X. Bound its cross
coefficient by 466/125=3.728, using (283/50)^2>32, and insert (6).
At X=10^99 use sqrt(10)<16/5; the resulting rational budget is below
38. At X=10^100 it is below 40, and at X=10^102 it is below 72.
The exact fractions and input hashes appear in the
[small certificate record](../../numerics/subpower_finite_variance_20261003/record.json).
This proves (1) throughout the stated continuous ranges.

## What systematically improves here

For any fixed C>(3/2)b^2, let q_C be the positive root of

\[
\frac73q^2+\frac45(2^{5/2}-1)bq+\frac32b^2=C.
\]

Formula (7) proves Vcal_g(X)<=C X^2 whenever
e<=X<=(q_C/R_H)^2. For a family of rigorously verified heights and
a fixed low cutoff, this certified range grows on the scale

\[
X_{\max}\asymp_g\frac{H^{10}}{(\log H)^2}.
\tag{8}
\]

This is a tangible finite-range improvement law. It concerns the range
of a quadratic bound, not the global delta in the baseline theorem.
At any fixed H, the allowance in (7) eventually has cubic growth. A
finite range, however large, cannot be entered as a proved global delta.

The next practical improvement to this finite certificate would retain
the low-zero cross terms in its exact dyadic Gram integral instead of
using their coefficient triangle bound. That could reduce C and enlarge
the finite range. Such work should be secondary to testing an actual-prime
power-saving mechanism for the global milestone, as organized in the
[short-interval investigation](02_short_interval_transfer_and_gate_20261003.md).
