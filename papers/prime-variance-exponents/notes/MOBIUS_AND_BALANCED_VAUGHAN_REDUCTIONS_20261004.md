# Arithmetic localization by Möbius inversion and Vaughan's identity

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
These are internal calculations, not independent specialist review.

## Result and scope

For the fixed prepared response in [the manuscript](../manuscript.tex),
two unconditional reductions isolate the still-unproved arithmetic:

1. In the elementary divisor identity for Λ, all divisors
   d≤X^(11/12)/(log X)^(1/6) contribute only O(X²) shell variance.
   The remaining signed Möbius sum has cofactors at most
   2B X^(1/12)(log X)^(1/6).
2. Vaughan's identity can be used with U=V=X^(11/24). Its nonconstant
   logarithmic continuum term must be retained explicitly. After that
   term is combined with Type II, every remaining error has O(X²)
   variance. Both surviving Type II factors lie between X^(11/24)
   and 2B X^(13/24).

Each remaining signed estimate has exactly the same admissible variance
exponents 2+δ, δ≥0, as the original response, including δ=0.
These are arithmetic localizations with proved quadratic error, not a
proved decrease in the actual-prime exponent. Their useful additional
content is that the discarded divisor ranges really have been bounded,
and the retained coefficients are explicitly Möbius/von Mangoldt
coefficients. The generic oscillatory models from the earlier notes do
not possess these exact convolution identities.

The parent notes
[06](../../investigations/sonin-critical-boundary/notes/selective-loss-program/06_global_mechanism_tests_20261003.md),
[09](../../investigations/sonin-critical-boundary/notes/selective-loss-program/09_actual_error_projection_and_frequency_20261003.md),
and [10](../../investigations/sonin-critical-boundary/notes/selective-loss-program/10_subpower_growth_and_investigation_paths_20261003.md)
already exclude generic PNT, positive frame bounds, absolute coefficient
norms and the tested central-frequency estimates as sufficient inputs.
The present note does not reuse any of those as a claimed power saving.

## 1. A uniform lattice lemma with an explicit constant

Keep A=e^(-1/4), B=e^(1/4), and the fixed real zero-extended w from the
manuscript. It is compactly supported on [A,B], C⁴, and has sixth
distributional derivative a finite signed measure. The same is true of
v(u)=(log u)w(u), extended by zero; its support stays away from zero.
Define

\[
\mathscr C_w=\frac{\|D^6w\|_{\rm TV}}{30240},\qquad
\mathscr C_v=\frac{\|D^6v\|_{\rm TV}}{30240},\qquad
c_w=\int_A^B (\log u)w(u)\,du.
\]

For any such function f and every real y>0, Poisson summation gives

\[
\sum_{k\ge1}f(k/y)
=y\int f+E_f(y),\qquad
|E_f(y)|\le \frac{\|D^6f\|_{\rm TV}}{30240}y^{-5}. \tag{1}
\]

Indeed, with the Fourier convention exp(-2πiξu), distributional
integration by parts gives
|f̂(ξ)|≤||D⁶f||TV/(2π|ξ|)⁶ for ξ≠0. The nonzero terms in
y Σ_j f̂(jy) are absolutely summable and their bound is
2ζ(6)/(2π)⁶=1/30240 times ||D⁶f||TV y^(-5).
Poisson follows, for example, by forming the C⁴ periodic sum of
f((k+t)/y), whose Fourier series converges absolutely. All negative and
zero lattice samples vanish because supp f⊂(0,∞).

Since ∫w=0, (1) gives the exact uniform bounds

\[
L(y):=\sum_{k\ge1}w(k/y),\qquad |L(y)|\le\mathscr C_w y^{-5}, \tag{2}
\]
\[
\sum_{k\ge1}(\log k)w(k/y)=c_w y+E_{\log}(y),\qquad
|E_{\log}(y)|\le
(\mathscr C_w|\log y|+\mathscr C_v)y^{-5}. \tag{3}
\]

Equation (3) follows from log k=log y+log(k/y). There is a nonzero
continuum in (3). In the manuscript's plus-exponent convention,

\[
c_w=-G'(-1/2)=-\frac{H(-1/2)}{2\sqrt\nu}<0. \tag{4}
\]

The last equality differentiates G(z)=z(z²-1/4)H(z)/√ν at z=-1/2.
Thus preparation annihilates the constant lattice density, but does not
annihilate the logarithmic lattice density. This is the essential
qualification in a Vaughan decomposition.

## 2. Large Möbius divisors and small cofactors

The elementary identity

\[
\Lambda(n)=-\sum_{d\mid n}\mu(d)\log d \tag{5}
\]

holds also at n=1 with both sides zero. One proof differentiates the
finite product ∏_(p|n)(1-p^t) at t=0; only a single distinct prime factor
can give a nonzero first derivative. Consequently, for every x>0,

\[
V_g(x)=-\sum_{d,k\ge1}\mu(d)(\log d)w(dk/x). \tag{6}
\]

Every sum here is finite on a fixed shell. Fix the cutoff D using X,
and keep that cutoff fixed as x varies in [X,2X]. Put

\[
E_{X,D}(x)=-\sum_{d\le D}\mu(d)(\log d)L(x/d),
\]
\[
R_{X,D}(x)=-\sum_{k\le K}\sum_{d>D}\mu(d)(\log d)w(dk/x),
\qquad K=\left\lfloor\frac{2BX}{D}\right\rfloor.
\]

Then V_g=E_(X,D)+R_(X,D) exactly throughout the shell. Inclusion of a
possible upper endpoint does not matter because w vanishes there.
For D≥1, (2) and |μ(d)|≤1 imply

\[
|E_{X,D}(x)|\le \mathscr C_w X^{-5}
\sum_{d\le D}d^5\log d
\le\mathscr C_w X^{-5}D^6\log D, \tag{7}
\]
\[
\|E_{X,D}\|_{L^2(X,2X)}
\le\mathscr C_w X^{-9/2}D^6\log D. \tag{8}
\]

For X≥e choose

\[
D_X=\frac{X^{11/12}}{(\log X)^{1/6}},\qquad
K_X=\left\lfloor2B X^{1/12}(\log X)^{1/6}\right\rfloor. \tag{9}
\]

Here D_X≥1 and log D_X≤(11/12)log X. Thus

\[
\boxed{\quad
\|E_{X,D_X}\|_{L^2(X,2X)}
\le\tfrac{11}{12}\mathscr C_w X.
\quad} \tag{10}
\]

Writing Q_μ(X)=∫_X^(2X)|R_(X,D_X)(x)|²dx, the reverse triangle
inequality gives the unconditional quantitative comparison

\[
\boxed{\quad
\left|\sqrt{\mathcal V_g(X)}-\sqrt{Q_\mu(X)}\right|
\le\tfrac{11}{12}\mathscr C_w X.
\quad} \tag{11}
\]

In particular, for every fixed δ≥0,

\[
Q_\mu(X)=O(X^{2+\delta})
\quad\Longleftrightarrow\quad
\mathcal V_g(X)=O(X^{2+\delta}), \tag{12}
\]

with all estimates quantified over every sufficiently large real X.
The logarithmic adjustment in (9) is sufficient to include the exact
δ=0 endpoint. Using D=X^(11/12) directly in (7) would give an O(X log X)
norm error and would only immediately preserve the positive exponents.
No bound for cancellation of μ was used in discarding the small divisors.

There is useful room below the limiting cutoff. More generally, taking
D=X^θ with 0<θ<11/12 in (8) gives

\[
\|E_{X,D}\|_2\ll_w X^{6\theta-9/2}\log X,
\qquad K\le2B X^{1-\theta}.
\tag{12a}
\]

For the particularly simple choice D=X^(9/10),

\[
\boxed{\quad K\le2B X^{1/10},\qquad
\|E_{X,D}\|_2\ll_w X^{9/10}\log X,\qquad
\int_X^{2X}|E_{X,D}|^2\ll_w X^{9/5}(\log X)^2=o(X^2).\quad}
\tag{12b}
\]

Thus the discarded arithmetic sector has a genuine power saving even
against the quadratic scale. The difference of the two response norms,
divided by X, tends to zero. This does not bound the retained norm: it
locates all possible superquadratic growth in the signed small-cofactor
sum. Alternatively, D=X^(11/12)/(log X)^r with r>1/6 gives
\(\|E\|_2\ll_w X(\log X)^{1-6r}=o(X)\), at the same cofactor
power 1/12 with a larger logarithmic factor.

A fixed prefactor 0<c≤1 is also permitted in (9). For sufficiently large
X that D=cD_X≥1, (10) improves to
\(\|E\|_2\le(11/12)c^6\mathscr C_wX\), while the cofactor ceiling
increases by 1/c. The numerical pilot uses c=1/4 and the exact integer
condition d>floor(cD_X).

For an explicit signed covariance, set
C_(k,X)(x)=Σ_(d>D_X) μ(d)log d·w(dk/x). Then

\[
Q_\mu(X)=\sum_{1\le k,l\le K_X}
\int_X^{2X}C_{k,X}(x)C_{l,X}(x)\,dx. \tag{13}
\]

Both cofactor cross terms and Möbius signs are retained. At each fixed k
the complete shell divisor band is
d∈[AX/k,2BX/k]∩(D_X,∞). In particular the hard cutoff d>D_X must
remain for the largest cofactors. It can be omitted only when the full
support already lies above it; for example k≤AX/D_X suffices. A
numerical calculation should retain these terminal partial bands.

## 3. A balanced Vaughan reduction with quadratic error

We derive the identity to specify its exact conventions. For Dirichlet
convolution, μ*1=δ₁ and 1*Λ=log. Split μ and Λ at real U,V≥1.
Then

\[
\Lambda
=\mu_{\le U}*\log-\mu_{\le U}*1*\Lambda_{\le V}
  +\Lambda_{\le V}+\mu_{>U}*1*\Lambda_{>V}. \tag{14}
\]

For example, start from Λ=μ≤U*log+μ>U*1*Λ, split the last Λ,
and replace μ>U*1 by δ₁-μ≤U*1 only in its Λ≤V part.
This is the standard Vaughan identity; see
[Tao's author-hosted lecture, Lemma 18](https://terrytao.wordpress.com/2015/01/10/254a-notes-3-the-large-sieve-and-the-bombieri-vinogradov-theorem/).
The identity above is proved here and no distribution theorem from that
lecture is imported.

Keep U,V fixed over [X,2X]. Define

\[
A_U(m)=\sum_{\substack{d\mid m\\d>U}}\mu(d),\qquad
M_1(U)=\sum_{d\le U}\frac{\mu(d)}d,
\]
\[
B_{U,V}(x)=\sum_{m>U}\sum_{n>V}
A_U(m)\Lambda(n)w(mn/x). \tag{15}
\]

The fourth convolution in (14) is exactly (15). There is no contribution
from Λ≤V when V<AX. Equations (2) and (3) treat the two Type I terms:

\[
\sum_{d\le U}\mu(d)\sum_{k\ge1}(\log k)w(dk/x)
=c_w x M_1(U)+E_I(x),
\]
\[
|E_I(x)|\le U^6X^{-5}
(\mathscr C_w\log(2X)+\mathscr C_v) \tag{16}
\]

provided U≤X, so that 1≤x/d≤2X. For the other Type I term,

\[
\begin{split}
\left|\sum_{d\le U}\sum_{r\le V}\mu(d)\Lambda(r)L(x/(dr))\right|
&\le\mathscr C_w X^{-5}
\left(\sum_{d\le U}d^5\right)
\left(\sum_{r\le V}\Lambda(r)r^5\right)\\
&\le(4\log2)\mathscr C_w X^{-5}U^6V^6. \tag{17}
\end{split}
\]

We used the elementary Chebyshev bound ψ(V)≤(4 log 2)V, already proved
in the manuscript. Keeping the product structure in (17) removes the
extra logarithm that would result from a generic divisor-coefficient
bound.

Set

\[
U=V=X^{11/24},\qquad
T_X(x)=B_{U,V}(x)+c_w xM_1(U). \tag{18}
\]

For every sufficiently large real X, V<AX. Since U⁶=X^(11/4) and
U⁶V⁶=X^(11/2), (14)–(17) give

\[
\boxed{\quad
V_g(x)=T_X(x)+E_X(x),\qquad
|E_X(x)|\le
(4\log2)\mathscr C_w X^{1/2}
+(\mathscr C_w\log(2X)+\mathscr C_v)X^{-9/4}.
\quad} \tag{19}
\]

Thus ||E_X||_(L²(X,2X))=O_g(X). In particular,

\[
\boxed{\quad
\int_X^{2X}|T_X(x)|^2dx=O(X^{2+\delta})
\quad\Longleftrightarrow\quad
\mathcal V_g(X)=O(X^{2+\delta})\qquad(\delta\ge0).
\quad} \tag{20}
\]

Every nonzero Type II pair in (15) satisfies mn∈[AX,2BX]. Since both
factors exceed X^(11/24), each also satisfies

\[
X^{11/24}<m,n\le2B X^{13/24}. \tag{21}
\]

This is a narrow region around the balanced size X^(1/2). The remaining
coefficient can itself be written

\[
A_U(m)=\sum_{\substack{k\mid m\\m/k>U}}\mu(m/k),
\qquad k<\frac mU\le2B X^{1/12}. \tag{22}
\]

The strict cutoff matters if U is integral. All these statements use
the original fixed w, including full support windows and real X.

The explicit linear term c_w xM₁(U) cannot be dropped. Equation (4)
shows c_w≠0. An absolute bound for M₁(U) from a subpower PNT estimate
does not put this term on the O(√X) amplitude scale. The desired estimate
must combine it with B_(U,V), or provide a new sufficiently strong bound
for it and for B separately. Calling all Type I pieces negligible without
this subtraction is incorrect for the present prepared probe.

As in (12b), a slightly wider factor range gives a strictly smaller
error. Taking U=V=X^(9/20) in (16)–(17) yields

\[
\|V_g-[B_{U,V}+c_wxM_1(U)]\|_{L^2(X,2X)}\ll_w X^{9/10},
\qquad X^{9/20}<m,n\le2BX^{11/20}.
\tag{22a}
\]

Indeed the constant-inner error has amplitude X^(2/5), and the
logarithmic-inner error has amplitude O(X^(-23/10)log X).
This buys an o(X) norm error while keeping both factors near the
square-root scale; the centered balanced sum itself is still unbounded
at any improved global exponent.

## 4. Prime powers are harmless in the original response

Let V_pr(x)=Σ_p(log p)w(p/x), and let P(x)=V_g(x)-V_pr(x).
By Chebyshev,

\[
|P(x)|\le\|w\|_\infty
\sum_{2\le j\le\log(Bx)/\log2}\theta((Bx)^{1/j})
\ll_g x^{1/2}+x^{1/3}\log(2x)\ll_g x^{1/2}. \tag{23}
\]

It follows that ∫_X^(2X)|P(x)|²dx=O_g(X²). The original response and
its prime-only version therefore have identical admissible exponents
2+δ for δ≥0. No prime-power cancellation is needed for this observation.
It does **not** authorize deleting prime powers from the inner Λ(n) in
(15): those are different terms of the convolution identity and would
require their own estimate. Equations (14)–(20) retain them.

## 5. What this advances and the next test

The new estimates (10) and (19) are unconditional sector eliminations for
the actual arithmetic response. They are distinct from merely labeling
an arbitrary residual: the cutoffs, surviving arithmetic coefficients,
and uniform quadratic errors are explicit. Their exponents follow from
the fixed probe's sixth-power Fourier decay. Increasing smoothing in a
different probe could alter these localization widths, but would not by
itself add cancellation in the surviving sums.

The still-missing statement is one fixed κ>0 such as

\[
Q_\mu(X)\ll X^{3-\kappa}
\quad\text{or}\quad
\int_X^{2X}|B_{X^{11/24},X^{11/24}}(x)
+c_w xM_1(X^{11/24})|^2dx\ll X^{3-\kappa}. \tag{24}
\]

For 0<κ≤1, this would give the actual exponent δ=1-κ, hence the fixed
zero strip in the manuscript. An extra unbounded subpower factor gives
the strict frontier instead. No such bound is proved in this note.

In particular, the weight w(mn/x) varies on the scale mn≈X and does not
automatically supply a rapidly oscillating bilinear phase. A generic
Cauchy–Schwarz, coefficient norm, or large-sieve bound does not acquire
a power saving just because both factors are near √X. Bounding the
cofactor covariance entries separately can also discard the required
Möbius cancellation. These reductions remain equivalent formulations
of a difficult global theorem; the progress is the justified elimination
of the easy ranges and an arithmetic target on which a new theorem can
be tested.

A small pilot can check (6), compare V_g with the large-divisor sum,
and retain the signed cofactor covariance (13). A balanced pilot should
also report c_w xM₁(U), B_(U,V), and their sum separately, to expose rather
than hide the continuum cancellation. Such finite calculations would
diagnose a proposed mechanism and verify bookkeeping; no measured slope
would establish (24).
