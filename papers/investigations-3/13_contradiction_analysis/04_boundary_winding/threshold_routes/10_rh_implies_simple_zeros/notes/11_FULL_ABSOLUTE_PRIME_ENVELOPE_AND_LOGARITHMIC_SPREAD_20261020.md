# Full absolute-prime envelope and logarithmic spread

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded turn metadata. Separate same-model derivations and
[internal review][review]; no specialist review or novelty claim.

**Result: proved under RH within the stated complete-budget class.** The completely paid absolute-prime envelope for every admissible nonnegative bandlimited kernel from Note 08 has leading lower bound `1/2`, without a restriction on `I Delta` or Fourier signs. The bound is sharp in this class by the existing centered Fejér comparison. A separate quantitative inequality relates absolute prime payment, mass, and the kernel's logarithmic pair moment. Neither statement bounds a retained signed-prime consumer or excludes an original multiple zero.

The [result index](../../../../../../../result-summaries/README.md), [avoid index](../../../../../../../avoid/README.md), especially [scope](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [quantitative gain](../../../../../../../avoid/20_volume_without_a_gain.md), apply. This continues [Note 10][n10] and the [progress register][progress].
The [collision catalogue][controls] and [complete-payment warning][a12]
also apply. This proof removes a declared class restriction in the existing cost comparison; it does not supply a new simplicity margin.

## 1. Class, exact payment, and logarithmic moment

Let `h` be an admissible kernel from [Note 08][n8]: entire, real and nonnegative on the real axis, `h(0)=1`, with
\[
|h(x+iy)|\le C_{h,Y}(1+x^2)^{-1}\quad (|y|\le Y)
\]
for every fixed \(Y\), and continuous Fourier transform

\[
\phi(v)=\int_{\mathbb R}h(x)e^{-2\pi ixv}dx,
\qquad \operatorname{supp}\phi\subset[-\Delta,\Delta].
\]

Write

\[
I=\phi(0)>0,\quad B=2\pi\Delta,\quad
C=\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       |\phi(\log n/(2\pi))|.
\tag{G1}
\]

All prime powers are retained. Define the probability measure and its characteristic function by

\[
d\mu(x)=\frac{h(x)}I dx,\qquad
S(u)=\int e^{-ixu}d\mu(x)=\frac{\phi(u/(2\pi))}I.
\]

Thus `|S|<=1` and `S(u)=0` for `|u|>B`. For independent variables with law `mu`, put

\[
\mathcal M=\iint\log(2+|x-y|)d\mu(x)d\mu(y).
\tag{G2}
\]

Quadratic decay makes this finite: `log(2+|x-y|)<=log(2+|x|)+log(2+|y|)` and each one-variable integral converges.

## 2. RH controls the entire upper Fourier tail

Fix a smooth `chi` with `0<=chi<=1`, zero on `(-infinity,0]` and one on `[1,infinity)`. For `B>=A>=2`, take

\[
F(u)=e^{u/4}\chi(u-A+1)\chi(B+1-u),\qquad
J(u)=e^{-u/2}F(u).
\]

Both are smooth and supported in `[A-1,B+1]`; `F(u)=e^{u/4}` on `[A,B]`. Direct differentiation gives, uniformly in the upper support endpoint,

\[
\|J\|_1+\|J''\|_1\ll e^{-A/4},\qquad
\left|\int J(u)e^{ivu}du\right|
\ll\frac{e^{-A/4}}{1+v^2}.
\tag{G3}
\]

The second bound follows by two integrations by parts. The smooth upper cutoff avoids any endpoint regularity assumption on `phi`; no derivatives of `S` are used.

The starting formula and local zero count have been checked in the primary source [Tao, *246B Notes 4*, Exercises 22(iii) and 20(iii)](https://terrytao.wordpress.com/2021/02/12/246b-notes-4-the-riemann-zeta-function-and-the-prime-number-theorem/). Applying the smoothed explicit formula to `eta(x)=x^{-1-it}F(log x)`, under RH, gives

\[
\begin{aligned}
\sum_n\frac{\Lambda(n)}n F(\log n)n^{-it}
={}&\int F(u)e^{-itu}du
-\sum_\rho\int J(u)e^{i(\Im\rho-t)u}du\\
&-\int F(u)\frac{e^{-(1+it)u}}{e^{2u}-1}du.
\end{aligned}
\tag{G4}
\]

Every nontrivial zero is counted with its full multiplicity. The trivial-zero integral is `O(e^{-11A/4})`. The complete local zero count, summed over unit intervals, implies

\[
\sum_\rho\frac1{1+(\Im\rho-t)^2}\ll\log(2+|t|).
\]

Consequently (G4)'s entire zero error is `O(e^{-A/4}log(2+|t|))`, uniformly for every real `t`, including zero. This assertion uses RH but not simplicity.

Integrate (G4) at `t=x-y` against `mu(x)mu(y)`. Absolute interchange of the zero sum and the pair integral is justified by (G2)--(G3). The ordinary integrals and finite arithmetic sum also permit Fubini. Since the averaged phase is `|S(u)|^2`,

\[
\int F(u)|S(u)|^2du
=\sum_n\frac{\Lambda(n)}n F(\log n)|S(\log n)|^2
 +O(e^{-A/4}\mathcal M).
\tag{G5}
\]

The complete arithmetic sum is nonnegative and, by `|S|<=1`, is at most

\[
e^{-(A-1)/4}\sum_n\frac{\Lambda(n)}{\sqrt n}|S(\log n)|
=\frac{\pi C}{I}e^{-(A-1)/4}.
\tag{G6}
\]

There is no deletion of higher powers and no replacement of the exact prime samples by continuous values. Multiplying (G5) by `I^2`, and restricting the nonnegative integral to `[A,B]`, gives

\[
\int_A^B e^{u/4}|\phi(u/(2\pi))|^2du
\ll e^{-A/4}(IC+I^2\mathcal M).
\]

Weighted Cauchy--Schwarz now pays the *entire* tail, independently of the bandwidth:

\[
\boxed{Z_A:=\int_A^\infty|\phi(u/(2\pi))|du
\ll e^{-A/4}\sqrt{IC+I^2\mathcal M}.}
\tag{G7}
\]

For `B<A`, the left side is zero. The implicit constant is absolute after fixing `chi`.

## 3. Stable Poisson summation recovers the factor two

For these kernels, Poisson's identity is valid and all spatial terms
are nonnegative. The quadratic strip bound makes the periodization
uniformly convergent; compact Fourier support makes its Fourier series
finite. This is the pointwise justification from Note 08 §6. For `v>0`,

\[
1\le\sum_{k\in\mathbb Z}h(k/v)
=v\left(I+2\sum_{n\ge1}\Re\phi(nv)\right).
\tag{G8}
\]

Hence `sum_(n>=1)|phi(nv)|>=(1/v-I)/2`. Let `a>0`, `H_a=int_a^infinity |phi(v)|dv`. If `r=Ia<1`, set `delta=1-r` and integrate over `[a,(1+delta)a]`. The lower bound is

\[
\frac12\{\log(1+\delta)-(1-\delta)\delta\}
\ge\frac{\delta^2}4.
\]

Changing variable `u=nv` bounds the same integral above by

\[
\int_a^\infty|\phi(u)|
\sum_{u/((1+\delta)a)\le n\le u/a}\frac1n\,du
\le(1+\log2)H_a.
\]

The harmonic overlap is bounded independently of the bandwidth and number of harmonics. Therefore

\[
\boxed{Ia\ge1-2\sqrt{(1+\log2)H_a}.}
\tag{G9}
\]

The inequality is trivial when `Ia>=1`. With `a=A/(2pi)` and `H_a=Z_A/(2pi)`, it follows that `Z_A=o(1)` forces `I>=(2pi/A)(1-o(1))`. This supplies the factor two lost by a pointwise Fourier-inversion estimate. A bound on a single remote shell would not suffice.

## 4. Exact complete-envelope hypotheses and the sharp leading floor

At target height `gamma->infinity`, write

\[
L=\log(\gamma/(2\pi)),\qquad
g_\gamma(v)=\Re\psi(1/4+i(\gamma+v)/2)-\log\pi,
\qquad G=(2\pi)^{-1}\int h(v)g_\gamma(v)dv.
\]

Let `P=h(-gamma+i/2)+h(-gamma-i/2)` (real), `E=|h(-gamma+i/2)|+|h(-gamma-i/2)|`. The two complete envelopes are `U=G+P+C` and `U=G+E+C`. Require Note 08's gamma localization

\[
\int h(v)|g_\gamma(v)-L|dv\le\epsilon_\gamma LI,
\qquad\epsilon_\gamma\to0,
\tag{G10}
\]

and, for exact pole retention, `(P)_-=o(LI)`. These give

\[
U\ge(1-o(1))\frac{LI}{2\pi}+C.
\tag{G11}
\]

The same gamma budget bounds the pair moment. Uniformly for real `v`, the digamma asymptotic and compact-range continuity give

\[
g_\gamma(v)=\log(2+|\gamma+v|)+O(1).
\]

Since `|x-y|<=|gamma+x|+|gamma+y|`,

\[
\log(2+|x-y|)
\le\log2+\max\{\log(2+|\gamma+x|),\log(2+|\gamma+y|)\}
\le L+O(1)+|g_\gamma(x)-L|+|g_\gamma(y)-L|.
\]

Averaging and using (G10) proves

\[
\mathcal M\le(1+2\epsilon_\gamma)L+O(1)=(1+o(1))L.
\tag{G12}
\]

To prove the leading lower bound it suffices to consider a sequence with `U=O(L/log L)`. By (G11), `I=O(1/log L)` and `C=O(L/log L)`. Take `A=2log L`. Equations (G7) and (G12) give `Z_A=O(1/log L)=o(1)`. Thus (G9) yields

\[
I\ge\frac\pi{\log L}
 \left(1-O((\log L)^{-1/2})\right).
\]

If `B<A`, ordinary Poisson gives `I>=1/Delta=2pi/B>2pi/A` directly. Inserting either bound into (G11) gives

\[
\boxed{\liminf_{\gamma\to\infty}
 \frac{U(\gamma)}{L/\log L}\ge\frac12.}
\tag{G13}
\]

The implicit mass-error constant can depend on the bounded-envelope constant; the final little-oh also includes the gamma and pole budgets. The existing centered Fejér envelope attains leading `1/2` and satisfies these budgets ([Note 02][n2] and [Note 08][n8]). Hence this leading constant is sharp for the declared class. The theorem is a sequential liminf with the displayed vanishing budgets; a classwise uniform infimum would additionally require uniform budgets.

## 5. A standalone mass--moment tradeoff

There is also a bound that does not assume a target height or gamma localization. For `0<I<=1/4`, set

\[
a=1/I-1,\qquad b=1/I-1/2,\qquad A=2\pi a.
\]

Poisson gives `I Delta>=1`, hence `B>=2pi/I>A`. Throughout `[a,b]`, (G8)'s Fourier-tail lower bound is at least

\[
\frac{1/b-I}{2}=\frac{I^2}{2(2-I)}\ge\frac{I^2}4.
\]

The interval length is `1/2`; its integrated lower bound is `I^2/8`. The harmonic overlap is at most `K_0=1+log2`, so `Z_A>=pi I^2/(4K_0)`. Square (G7), use `A/2=pi/I-pi`, and absorb the fixed constants. Under RH there is an absolute `c>0` such that

\[
\boxed{C+I\mathcal M\ge c I^3e^{\pi/I}\qquad(0<I\le1/4).}
\tag{G14}
\]

No numerical value for `c` is claimed. In particular, if `C` stays bounded and `I->0`, then `mathcal M>>I^2 exp(pi/I)` and `liminf I log(mathcal M)>=pi`. Small absolute prime payment is possible, as Note 09 shows, but it must carry this logarithmic spread cost. The gamma budget pays that cost in (G13).

**Scope.** No upper bound on `I Delta`, no Fourier-sign condition, no finite-mixture representation, and no translation-diameter restriction remains in (G13). The nonnegative kernel, actual normalization, full exact sample payment, admissibility, RH, gamma localization, and pole budget are retained. The conclusion is a bound for this absolute-prime envelope, not for a separately estimated signed-prime expression, an unbudgeted kernel, or every possible multiplicity method. Note 10's stronger family-specific coefficients `d/2` remain valid for its specified aligned-copy constructions. No original multiple zero is excluded.


## 6. Research consequence and control boundary

This completes the leading-cost comparison for the entire admissible
nonnegative-kernel class under the displayed complete budgets.
The signed arithmetic term remains outside this theorem.
Do not repeat kernel optimization while retaining this absolute prime
payment and the same complete budgets. A proposed next estimate must
retain signed arithmetic or state and justify the additional information
that changes the consumer. A kernel without a verified gamma or pole
budget is outside the theorem; merely omitting those payments is not a
valid escape.

This is an estimating result, not a new multiplicity theorem or a control
event exclusion. The exact weights in (G4) and (G6) are those of zeta.
The quadratic, atomic and heat-polynomial controls do not supply that
arithmetic identity. Euler-factor and weighted-source controls change
its arithmetic or completion data; the reflected and positive-primitive
controls do not restore the unchanged complete theta arithmetic.
Note 05's normalized source control fails ordinary Dirichlet-series
arithmetic, while Note 09's arithmetic control preserves only selected
finite data and fails exact reflection and the unchanged full tail.
Their separate preservation lists remain separate. The cost bound may
be applied to any admissible test function with the genuine prime
weights, but its use as a changed field's multiplicity majorant would
require that field's own complete explicit formula.

Note 09's near-zero prime-payment examples survive: (G14) charges their
logarithmic spread, and (G12) places it in the full height budget.
Note 10's stronger family-specific return bound remains useful.
No original theta multiple zero has been excluded, and the original
signed-estimate, strict-cap-surplus and all-zero gates remain open.


[review]: ../reviews/11_GENERAL_KERNEL_ENVELOPE_REVIEW_20261020.md
[n8]: 08_RECIPROCAL_PRECISION_AND_BANDLIMITED_ARITHMETIC_COSTS_20261020.md
[n10]: 10_UNIFORM_PRIME_PHASE_RETURN_HEIGHT_COST_20261020.md
[n2]: 02_FINITE_PRIME_FEJER_RESOLUTION_TEST_20261020.md
[progress]: ../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
