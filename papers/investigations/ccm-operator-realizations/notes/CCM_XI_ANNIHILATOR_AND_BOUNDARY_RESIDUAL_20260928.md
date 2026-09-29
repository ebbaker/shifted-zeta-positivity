# Xi-kernel annihilation and quantitative truncation residuals

Date: 28 September 2026. Drafted for Edward Baker with LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed.
Status: analytic working derivation, with explicit estimates; no new numerical experiment, no RH assumption, and no claim of novelty. Standard Guinand–Weil explicit-formula input is distinguished from the estimates derived here. This is not formal verification or independent human refereeing.

## 1. Result and limitation

The full Xi kernel is unconditionally annihilated by the whole-line Weil **distribution**, in the sense of its pairing with compact smooth tests. This is not the assertion that an everywhere-defined positive operator on ordinary whole-line L2 has a kernel. The distribution is not being assumed positive.

For the hard restriction `f_b=1_[-b,b] k`, with `b=L/2≥1`, its compressed-operator residual and Rayleigh energy satisfy

\[
\|W_Lf_b\|_2\le C(1+b)^{3/2}e^{-b}k(b)
 \le C'(1+b)^{3/2}e^{7b/2}e^{-\pi e^{2b}},                  \tag{1}
\]
\[
|QW(f_b,f_b)|\le C(1+b)\frac{k(b)^2}{\pi e^{2b}}
 \le C'(1+b)e^{7b}e^{-2\pi e^{2b}}.                        \tag{2}
\]

Constants are absolute; explicit expressions precede the big-O simplifications below. After dividing by the nonvanishing L2 norm of `f_b`, the same support orders hold. Equation (2) uses exact cancellation, not the weaker Cauchy–Schwarz bound from (1).

These estimates construct a very accurate near-null vector. They do not identify it with the least eigenvector. There is a whole family of unconditional annihilators, including translates and derivatives of `k`, which yields a growing near-null cluster. The finite CCM prolate comparison therefore contains a substantial **ground-selection** requirement even after an absolute residual has been made extremely small.

## 2. Normalization and the unconditional identity

Use Fourier transform `hat f(z)=∫f(x)e^(-izx)dx`. Let

\[
k(x)=e^{x/2}\sum_{n\ge1}h(ne^x),\qquad
h(u)=\frac\pi2u^2(2\pi u^2-3)e^{-\pi u^2}.
\]

The usual theta/Poisson identity makes `k` real, smooth, even and rapidly decreasing at both ends; with the literal h displayed here, its Fourier transform is Xi/4. The scalar was corrected in [round 7](CCM_BOUNDARY_SELECTION_AND_COMPLEMENT_20260928.md#2-a-scalar-normalization-correction); no annihilation or normalized-profile statement changes.

Write `z_ρ=(ρ−1/2)/i` for every nontrivial zeta zero, without assuming `z_ρ` real. The explicit formula reads

\[
\Psi(F)=\sum_\rho\widehat F(z_\rho).
\]

For `F=f* * k`, its transform is

\[
\widehat F(z)=\overline{\widehat f(\overline z)}\,\Xi(z)/4.
\]

Every summand at a zero is therefore zero. Consequently

\[
QW(f,k)=\Psi(f^**k)=0,\qquad \mathcal W*k=0.                \tag{3}
\]

For compact smooth `f`, the explicit formula applies directly to the rapidly decreasing correlation. The identity also extends to the hard restriction and tail used below: their weighted total variations are finite, so their transforms are O(1/|Re z|) uniformly for `|Im z|≤1/2`; products decay quadratically. The unconditional zero count `N(T)=O(T log T)` then makes the zero-side sum absolutely convergent. Smooth approximations with bounded weighted variation justify the extension. On the arithmetic side, the correlation is continuous, has at most the usual derivative cusps, has integrable regularized archimedean difference at zero, and decays rapidly at infinity. These properties justify the same limiting passage.

This use of the zero side is not circular: Xi is known to vanish at all its zeros whether or not they lie on the real axis. The conclusion is an annihilator identity, not a positive sum of squares over real ordinates.

Set `r_b=k−f_b`. Hermitian polarization and (3), including `QW(k,k)=0`, give

\[
QW(f_b,r_b)=-QW(r_b,r_b),\qquad
\boxed{QW(f_b,f_b)=QW(r_b,r_b).}                           \tag{4}
\]

More generally every translate of `k` has transform `e^(-itz)Xi(z)/4` and is an annihilator; derivatives multiply Xi by powers of `iz`. Taking even combinations does not remove this multiplicity of candidate near-null directions.

## 3. Elementary kernel envelope

For `x≥1`, each summand in

\[
k(x)=\pi^2e^{9x/2}\sum_{n\ge1}n^4
 \left(1-\frac{3}{2\pi n^2e^{2x}}\right)e^{-\pi n^2e^{2x}}
\]

is positive. If `t=πn²e^(2x)`, the logarithmic derivative of that summand is

\[
\frac92+\frac6{2t-3}-2t\le-t\le-\pi e^{2x}.
\]

The first inequality holds for `t≥6`, as here. Summing yields, with

\[
a=\pi e^{2b},\qquad K=k(b)>0,
\]

\[
0<k(b+s)\le K e^{-as}\quad(s\ge0).                         \tag{5}
\]

Also

\[
K\le2\pi^2e^{9b/2}e^{-\pi e^{2b}}.                        \tag{6}
\]

For example, the remaining sum after taking out the `n=1` exponential is bounded by `Σ_(n≥1)(16e^(-12))^(n−1)<2`, using `n⁴≤16^(n−1)` and `πe²>12`.

The tail has

\[
\|r_b\|_1\le2K/a,\quad \|r_b\|_2^2\le K^2/a,
\quad\operatorname{Var}(r_b)=4K,
\]
\[
|\widehat r_b(t)|\le\min(2K/a,4K/|t|).                    \tag{7}
\]

The jumps at the two endpoints are included in the total variation.

## 4. The hard restriction is in the required operator domain

The archimedean operator on zero-extended functions is the real multiplier

\[
A(t)=\operatorname{Re}\psi(1/4+it/2)-\log\pi.
\]

The existing audit proves `−6<A(t)≤(1/2)log(1+t²)`. A compact piecewise-smooth function with finite jumps has Fourier decay O(1/|t|), which is enough for `A(t)hat f(t)` to lie in L2. In particular the zero extension of `f_b` lies in the full-line logarithmic multiplier domain. Compressing its action to the interval gives the archimedean part of the closed restricted Weil operator; its prime and pole parts are bounded there. Thus `f_b∈Dom(W_L)`.

There is no H1-zero-extension assertion: hard truncation usually fails that stronger condition. Its logarithmic endpoint singularity is square integrable and will be accounted for explicitly below.

On the interior interval, (3) gives the identity in distributions and then in L2:

\[
W_Lf_b=-1_{[-b,b]}(\mathcal W*r_b).                        \tag{8}
\]

Whole-line prime/pole operators need not act boundedly on ordinary L2. In (8) their action on this particular superexponential tail is a locally absolutely convergent integral/sum. No unjustified global bounded operator is used.

## 5. Explicit L2 residual estimate

Off the origin the archimedean convolution kernel is

\[
-H(s),\qquad H(s)=\frac{e^{s/2}}{2\sinh s}
=\frac{e^{-s/2}}{1-e^{-2s}}\le1+\frac1{2s},\quad s>0.
\]

The inequality follows from `1/(1−e^(−u))≤1+1/u`. For an interior point the contact term multiplies `r_b(x)=0`, so no contact term is dropped. Let `E(t)=e^t E_1(t)=∫_0^∞e^(−u)/(t+u)du`. Then

\[
|(A(D)r_b)(x)|\le K\left[\frac2a+rac12E(a(b-x))+rac12E(a(b+x))\right].
\]

The elementary identity

\[
\int_0^\infty E(t)^2dt=\int_0^\infty\frac{\log v}{v^2-1}dv
=\frac{\pi^2}{4}
\]

follows by its Laplace-integral representation and Tonelli; splitting the last integral at one gives twice the odd reciprocal-square sum. Therefore

\[
\|1_I A(D)r_b\|_2\le
K\left[\frac{2\sqrt{2b}}a+\frac\pi{2\sqrt a}\right].       \tag{9}
\]

The pole kernel is `2cosh((x−y)/2)`. Since the tail is even,

\[
\|1_I W^{\rm pole}r_b\|_2
\le\frac{4K e^{b/2}\sqrt{b+\sinh b}}{a-1/2}.              \tag{10}
\]

For the prime part, put `X=e^(2b)`. Its absolute L2 norm is bounded by twice the sum over positive shifts with weights `Λ(n)/sqrt n`. Equation (5) gives

\[
\|1_I r_b(\cdot+\log n)\|_2
\le\frac K{\sqrt{2a}}
\begin{cases}1,&n\le X,\\(n/X)^{-a},&n>X.\end{cases}
\]

Use `Λ(n)≤log n` and `Σ_(n≤X)n^(−1/2)≤2sqrt X`. For any `d>1/2`, monotonicity and an integral comparison give

\[
S_d(b):=\sum_{n>X}\frac{\log n}{\sqrt n}(n/X)^{-d}
\le 2be^{-b}+e^b\left[\frac{2b}{d-1/2}+\frac1{(d-1/2)^2}\right]. \tag{11}
\]

The summand is decreasing for `t≥X` in the cases `d=a,a/2` used here. One may bound the integer sum by its value at X plus the integral from X; X need not be an integer. Therefore

\[
\|1_I W^{\rm prime}r_b\|_2
\le K\sqrt{2/a}\,[4be^b+S_a(b)].                          \tag{12}
\]

Equations (9)–(12) already give an explicit, weaker bound `K R(b)`, where

\[
R(b)=\frac{2\sqrt{2b}}a+\frac\pi{2\sqrt a}
+\frac{4e^{b/2}\sqrt{b+\sinh b}}{a-1/2}
+\sqrt{2/a}\,[4be^b+S_a(b)]=O(1+b).
\]

This separate-prime estimate is useful here because it is applied to the already superexponentially small omitted tail after the exact whole-form cancellation. It is not the earlier failed attempt to dominate all prime translations on an arbitrary high-frequency subspace.

### 5.1 A sharper bound retaining separation of translated tails

For `2≤n≤X`, put `x_n=b−log n` and let

\[
U_n(x)=K e^{-a(x-x_n)}1_{x\ge x_n},\qquad x\in I.
\]

The actual positive-shift tail is bounded pointwise by `U_n`. For every pair `m,n≤X`, integration from the larger onset point gives

\[
\langle U_n,U_m\rangle_{L^2(I)}
\le\frac{K^2}{2a}e^{-a|\log n-\log m|}
\le\frac{K^2}{2a}e^{-\pi|n-m|}.                            \tag{17}
\]

The last step uses `|log n−log m|≥|n−m|/X` and `a=πX`. The matrix on the right has row sum at most

\[
c_\pi=\sum_{j\in\mathbb Z}e^{-\pi|j|}
=\coth(\pi/2).
\]

Since all prime weights and all tail profiles are nonnegative, the same Gram upper bound controls the actual sum. Also

\[
\sum_{2\le n\le X}\frac{\Lambda(n)^2}n
\le(\log X)^2\sum_{n\le X}\frac1n
\le4b^2(1+2b).
\]

Accounting for both directions by the triangle inequality, and retaining the earlier estimate above X, yields

\[
\boxed{\|1_I W^{\rm prime}r_b\|_2
\le K\left[\sqrt{8c_\pi/a}\,b\sqrt{1+2b}
+\sqrt{2/a}\,S_a(b)\right].}                              \tag{18}
\]

Together with (9)–(10), this proves (1). Here `S_a(b)=O((1+b)e^(−b))`, so the second term in (18) is smaller. This is an unconditional arithmetic-coordinate improvement over the full triangle estimate: the relevant translated boundary packets have controlled overlap because distinct integers have separated logarithms. No claim is made that (18) is the optimal residual order.

## 6. Stronger squared-tail Rayleigh bound

Use the exact energy identity (4). The archimedean symbol bound and (7), splitting Fourier frequency at a, give

\[
|Q^{\rm arch}(r_b)|\le
\left[6+\frac{10}\pi\log(1+a^2)+\frac{16}\pi\right]\frac{K^2}a.
                                                                    \tag{13}
\]

For detail, the full integral of `log(1+t²)|hat r_b(t)|²` is bounded by
`(K²/a)[40log(1+a²)+64]`: the low part uses `2K/a`, the high part uses `4K/|t|`, and integration by parts gives `∫_a^∞log(1+t²)t^(−2)dt≤[log(1+a²)+2]/a`. Multiplying by the symbol's factor `1/(4π)` and adding `6||r_b||²` gives (13).

The even pole energy obeys

\[
0\le Q^{\rm pole}(r_b)
\le\frac{8K^2e^b}{(a-1/2)^2}.                             \tag{14}
\]

For `s≥0`, split the tail autocorrelation into equal-sign and opposite-sign rays. Equation (5) gives

\[
C_r(s)=\int r_b(y)r_b(y+s)dy
\le\frac{K^2}a e^{-as}
+K^2(s-2b)_+e^{-a(s-2b)_+}1_{s\ge2b}.
\]

Since `d e^(−ad)≤a^(−1)e^(−ad/2)` for `d≥0`,

\[
|Q^{\rm prime}(r_b)|
\le\frac{2K^2}a\left[S_0(a)+S_{a/2}(b)\right],\qquad
S_0(a)=\frac{\log2}{a-1/2}+\frac1{(a-1/2)^2}.             \tag{15}
\]

Here `Σ_(n≥2)log n · n^(−a−1/2)≤S_0(a)`: on `[n−1,n]`, `log n≤log(2t)` and `n^(−a−1/2)≤t^(−a−1/2)`, so summing reduces to an integral from one. The opposite-ray part uses (11) with `d=a/2`. These are elementary integer estimates; no prime-number theorem or RH is used.

Combining gives the explicit coefficient

\[
|QW(f_b,f_b)|\le\frac{K^2}a\left[
6+\frac{10}\pi\log(1+a^2)+\frac{16}\pi
+\frac{8ae^b}{(a-1/2)^2}+2S_0(a)+2S_{a/2}(b)\right].       \tag{16}
\]

The bracket is O(1+b), proving (2). All terms in the bracket are bounds on absolute component energies; the crucial extra cancellation occurred earlier in (4). Equation (16) does not assert a sign for the Rayleigh energy.

## 7. Smooth cutoffs and finite Fourier projections

A smooth even cutoff equal to one on `[-b+1,b−1]` and zero outside `[-b,b]` has a tail bounded pointwise by the hard tail beginning at `B=b−1`. For a monotone transition on each side, its tail has variation at most `4k(B)`. Thus the same squared-tail energy estimate holds with B. A full multiplier L2 bound from `log²` in (7), plus the same prime/pole argument with observation interval `[-b,b]`, gives residual `O((1+b)k(b−1))`. This is weaker in the double-exponential constant but avoids endpoint jumps. It is not necessary for the hard-cutoff argument, whose domain was checked above.

These continuum estimates do **not** automatically establish the corresponding tiny residual for a polynomial-size finite Fourier projection. An L2 approximation bound for a candidate is not an operator-residual bound for an unbounded logarithmic operator with support-growing bounded terms. The earlier `N≥cL^(7/2)` schedule resolves the candidate to polynomial L2 accuracy only. To exploit (1) in a finite matrix residual/separation argument, one must separately control the projection in the relevant operator norm or directly estimate the projected arithmetic residual. No necessary cutoff-growth rate is claimed here.

## 8. What follows and what does not

- The normalized hard restriction has spectral distance to zero at most its residual, and an extremely small Rayleigh quotient. The limiting target function is already Xi by construction.
- Neither fact places the vector at the bottom of the spectrum. If a negative compact-test direction exists, it persists in all sufficiently large windows, while this near-null vector still exists.
- Even under positivity, multiple truncated translates/derivatives furnish competing near-null directions. Absolute residual smallness may coexist with a very small even separation. A rank-one residual ratio can be ineffective although the actual overlap is high.
- A useful next theorem should control a candidate-adapted **low-energy subspace** and the effective operator within it, or produce a structural selection rule for its ground direction. Merely reproducing (3) or (1) does not do that.

The existing CCM source already distinguishes its prolate candidate's transform convergence from approximation of the actual Weil ground state. The present derivation makes one part of that distinction quantitative: unconditional null-vector truncation explains why very small absolute residuals can be obtained without solving the selection problem.

## Inputs inspected

- Repository: [round-5 audit](CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md), especially the symbol bound, candidate/true-ground distinction and residual/separation target; and the odd-tail note for operator conventions.
- [CCM, Zeta Spectral Triples, §§3 and 7–8](https://arxiv.org/html/2511.22755v1): explicit-formula normalization, closed restricted Weil form, Xi kernel, and stated missing ground comparison. Primary source inspected 28 September 2026. Its assumptions are not upgraded to proved ground-state properties.
