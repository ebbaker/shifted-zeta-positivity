# BW-08: finite exact profiles and finite-error full profiles do not control normalized event jets

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**,
actual reasoning effort **ultra**, verified by the parent from its turn
metadata and inherited by this full-history research subagent.

**Status: scoped analytic obstructions, proved in-note; [separate
same-model internal review][review], with no specialist review.**
This executes one BW2-03 observation contract. It gives three quantitative
failures of a proposed upper estimate for the normalized fourth jet:

1. An arbitrary finite number of imaginary-axis logarithmic derivatives
   can be held **exactly fixed**, together with `F(0)=1`, while an exact
   double event of an even real-rooted polynomial has unbounded `S_2`.
   The complete polynomial heat flow has the prescribed positive
   all-real threshold. This class has no positive source.
2. In the existing positive three-atom threshold family, the **whole
   profile on `0<=b<infinity`** converges uniformly, with explicit error
   at most `8 epsilon/a`, while `S_2` diverges at least as
   `25/(8 a^2 epsilon^2)`. This class is positive but atomic and fails
   theta's unbounded imaginary-axis growth.
3. A positive finite-atom threshold family holds any prescribed finite
   number of distinct profile samples exactly fixed, together with event
   normalization and complete moment budgets, while `S_2` diverges.
   Section 5A is the main stronger own-source obstruction; it retains
   infinitely many simultaneous events and fails full theta growth.

None of these statements says that the actual theta profile at a specified
time admits a collision, or that every finite profile vector admits the
construction. The first and third exact sample vectors are constructed, not prescribed
theta values. The second limiting profile belongs to an atomic
fourth-order event. All conclusions are
about explicit information classes, not all profile methods.

The [result summaries][results], [control cluster 12][controls] and
[patterns to avoid][avoid] govern the classification, especially
[target reformulations][a01], [control premises][a02] and
[scoped exclusions][a07]. The [new program][program] asks for a genuinely
quantitative profile consumer rather than another floor or a uniqueness
claim. The named failed consumer here is a finite upper estimate for
`S_2`, to be assembled into

$$
Q_L=18h_2^2(S_2-L),\qquad
S_2={h_3^2\over9h_2^2}-{h_4\over6h_2},\qquad L>0.
\tag{1}
$$

An independently obtained upper bound `S_2<=L` would contradict the
inherited theta lower bound on an applicable event class. The selected
profile information does not supply such a universal upper bound.

## 1. Contract and exact observations

Fix a positive event height `a`, any prescribed positive threshold `T`,
and distinct observation heights `b_1,...,b_k>0`, `k>=1`. The selected exact theoretical
observations are

$$
F(0)=1,\qquad D_F(b_i)={d\over db}\log F(ib)\big|_{b=b_i}.
\tag{2}
$$

For the first construction, the allowed class consists of normalized
even real-rooted polynomials with exact double zeros at `+a` and `-a`,
all other zeros simple, and their actual polynomial heat flows
`H(t,z)=exp(-(t-T)partial_z^2)F(z)`. Their only multiple zeros at `T`
are the two designated events; eventual simplicity at `T` is therefore
satisfied. No positivity of a Fourier source, theta source identity,
infinite zero counting law or full large-height growth is included.

The event jets are evaluated exactly at `(T,a)`. There are no acquisition,
parameter, truncation, normalization or differentiation errors in the
first construction. In particular, positive acquisition tolerance is not
the reason its upper estimate fails.

The second construction retains positive atomic sources and all their
complete moment budgets, but replaces exact profile acquisition by a
uniform additive error in `D` on the entire positive half-axis. The
event time, height and normalization are exact. This tests a stronger
observation norm than finitely many noisy samples or any compact profile
interval. It does not compare that limiting profile with theta.

## 2. A polynomial pencil with exactly unchanged profile samples

Write `A=a^2` and `B_i=b_i^2`. Choose `c>A` and put

$$
x_0=A,\quad x_j=B_j+c\quad(1\le j\le k),\qquad
R_0(w)=\prod_{j=0}^{k}(w-x_j).
\tag{3}
$$

Set `r_0=1` and solve the `k` linear equations

$$
\sum_{j=1}^{k}{r_j\over(B_i+x_j)^2}
       =-{1\over(B_i+A)^2},\qquad 1\le i\le k.
\tag{4}
$$

This system is nonsingular. Its matrix is

$$
K_{ij}={1\over(B_i+B_j+c)^2}
 =\int_0^\infty t e^{-ct}e^{-B_it}e^{-B_jt}\,dt.
\tag{5}
$$

For a nonzero vector `v`, the Gram form is positive because the
exponentials with distinct exponents are linearly independent:
`sum_i v_i exp(-B_i t)` cannot vanish identically. One elementary proof
differentiates at zero `0,...,k-1` times and uses the Vandermonde
determinant. Thus `K` is positive definite. Equations (3)--(5) are
exact; they require no condition-number assumption. If data are rational,
all coefficients below are rational. The size of `K^{-1}` affects the
explicit admissible perturbation, rather than being hidden.

Define

$$
V(w)=\sum_{j=0}^{k}r_j\prod_{\ell\ne j}(w-x_\ell),\qquad
R_\varepsilon(w)=R_0(w)+\varepsilon V(w).
\tag{6}
$$

The identity

$$
{V(w)\over R_0(w)}=\sum_{j=0}^{k}{r_j\over w-x_j}
\tag{7}
$$

and (4) give `(V/R_0)'(-B_i)=0`. Consequently

$$
{R_\varepsilon'(-B_i)\over R_\varepsilon(-B_i)}
 ={R_0'(-B_i)\over R_0(-B_i)}
\tag{8}
$$

whenever the denominator is nonzero. The positivity and denominator
payment are included in the next section.

Let `W(w)` be either `1`, or a fixed polynomial with simple positive
roots disjoint from the intervals used below and from `A`. Define

$$
F_\varepsilon(z)=
{(z^2-A)^2 R_\varepsilon(z^2)W(z^2)
 \over A^2 R_\varepsilon(0)W(0)}.
\tag{9}
$$

Then `F_epsilon(0)=1`, and (8) implies that every value in (2) is
independent of `epsilon`. Indeed

$$
D_{F_\varepsilon}(b_i)
=2b_i\left\{
 {2\over A+B_i}
 +\sum_{j=0}^{k}{1\over x_j+B_i}
 +\sum_{y:\,W(y)=0}{1\over y+B_i}\right\}.
\tag{10}
$$

Thus *every signed combination* of these finitely many exact observations
is fixed as well. Equation (10) is the constructed vector, not the
unchanged theta vector.

## 3. Explicit root and conditioning payment

Choose

$$
0<r\le \min\left\{{A\over2},
 {1\over3}\min_{j\ne\ell}|x_j-x_\ell|\right\}.
\tag{11}
$$

The intervals `[x_j-r,x_j+r]` are positive and disjoint. Put

$$
C=\max_j|r_j|\ge1,\qquad
M_j=\sum_{\ell\ne j}{|r_\ell|\over|x_j-x_\ell|-r},
\quad M=\max_j M_j,
$$
$$
0<\varepsilon<\varepsilon_0
 :=\min\left\{{r\over4C},{1\over4M}\right\},
\tag{12}
$$

with the second cap omitted if `M=0`. Close to `x_j`, the root equation
for `R_epsilon` is

$$
f_j(d):=d+\varepsilon r_j+
\varepsilon d\sum_{\ell\ne j}{r_\ell\over x_j+d-x_\ell}=0.
\tag{13}
$$

For `|d|<=r`, the sum has modulus at most `M_j`. At `d=r` the
expression is at least `r/2`; at `d=-r` it is at most `-r/2`.
There is one real root in each interval, and the degree `k+1` shows
there is exactly one and each is simple. Denote it `alpha_j(epsilon)`.
Equation (13) gives the explicit displacement

$$
|\alpha_j(\varepsilon)-x_j|
 \le {\varepsilon |r_j|\over1-\varepsilon M_j}
 \le {4\over3}\varepsilon|r_j|
 \le2\varepsilon|r_j|.
\tag{14}
$$

For `j=0`, `r_0=1` implies `alpha_0<A`, `alpha_0 ne A`, since
`1+epsilon sum>0` in (13). In particular `F_epsilon` has *exactly*
double zeros at `+a` and `-a`. All its other roots are real and simple.
The positive root placement proves
`R_epsilon(-B_i) ne 0`, `R_epsilon(0) ne 0`, and
`F_epsilon(ib)>0` for every real `b`. This pays all denominators in
(8)--(10), including the logarithm.

At the event,

$$
h_2={8\varepsilon V(A)\over A R_\varepsilon(0)W(0)}W(A)
\ne0,\qquad V(A)=\prod_{j=1}^{k}(A-x_j)\ne0.
\tag{15}
$$

The curvature therefore degenerates linearly while the exact data (2)
do not change. This is the explicit normalization loss; it is not an
unpaid numerical division.

## 4. The normalized jet is unbounded at the fixed observation vector

The deflated paired-root identity gives

$$
S_2={1\over2a^2}
 +\sum_{j=0}^{k}\left\{
 {1\over(a-\sqrt{\alpha_j})^2}
 +{1\over(a+\sqrt{\alpha_j})^2}\right\}
 +\sum_{y:\,W(y)=0}\left\{
 {1\over(a-\sqrt y)^2}
 +{1\over(a+\sqrt y)^2}\right\}.
\tag{16}
$$

By (14),

$$
0<a-\sqrt{\alpha_0}
 ={A-\alpha_0\over a+\sqrt{\alpha_0}}
 <{2\varepsilon\over a+\sqrt{A-r}},
$$
$$
\boxed{\quad
S_2>{1\over2a^2}
 +{(a+\sqrt{A-r})^2\over4\varepsilon^2}.
\quad}
\tag{17}
$$

Every finite positive `L` is eventually exceeded at the *same* data
vector, and `Q_L>0`. Therefore no upper-bound function of (2) can be
valid on this entire class and finite at the constructed vector.
In particular a proposed universal `Q_L<=0` based only on these data,
the stated real-rooted threshold facts and exact event cancellation is
false. This does **not** show failure at every possible finite vector.
Restrictions placing a positive lower bound on `|h_2|`, excluding a
nearby real root, or using the full theta source are outside the theorem.

### The flow really has threshold T

For a real-rooted polynomial `p`, each `p+v p'` is real-rooted for
real `v`: away from its roots, `p'/p=sum 1/(x-rho)` is strictly
decreasing between consecutive roots and has the required endpoint
limits; repeated roots lose at most one copy. Consequently
`(1-u partial_z^2)p=(1-sqrt(u)partial_z)
(1+sqrt(u)partial_z)p` is real-rooted for `u>=0`, where the product
of the two operators is intended. Taking

$$
\left(1-{s\over n}\partial_z^2\right)^n F_\varepsilon
 \longrightarrow e^{-s\partial_z^2}F_\varepsilon
\qquad(s\ge0)
\tag{18}
$$

coefficientwise proves that all zeros remain real for every `t>=T`;
real-rooted polynomials of a fixed degree form a closed set. The monic
leading coefficient is unchanged, so no root-loss issue occurs.

At the exact double root at `t=T`, the local heat expansion is
`(h_2/2)(z-a)^2-h_2(t-T)` to leading parabolic order. For
`t<T` sufficiently close to `T`, it has a nonreal conjugate pair
near `a`, by the inherited local heat collision law (or by its direct
quadratic rescaling and Rouché argument). If an earlier slice had
all real roots, (18) would propagate that property to these nonreal
near-threshold slices, a contradiction. Thus `T` is the exact
all-real threshold.

There can be no multiple root at a later time: the same local
multiplicity heat law would produce a nonreal root at an immediately
earlier time, already above `T`. Hence all later zeros are simple.
This uses only the inherited local law, not a source-positivity
theorem or a claim about a Fourier measure.

## 5. A positive-source full-profile error obstruction

Here use the own-source family from [BW-01 Note 04][atomic], with
arbitrary fixed `a>0`, prescribed `0<T<=1/2`, and

$$
0<\eta\le\tfrac12,\qquad q=\cos\eta,\qquad
\lambda={\pi-\eta\over a},\qquad A_q=(1+q)^{-2}.
$$

Its complete source has atoms at `0,lambda,2lambda`, all positive;
at the exact threshold,

$$
F_\eta(z)=A_q(\cos(\lambda z)+q)^2,\qquad F_\eta(0)=1.
\tag{19}
$$

The zero at `a` is exactly double for every `eta>0`. Its genuine
threshold and exact jets were proved in the cited source. Write
`lambda_0=pi/a` and define the limiting profile

$$
D_*(b)=2\lambda_0\tanh(\lambda_0b/2),\qquad
D_\eta(b)={2\lambda\sinh(\lambda b)\over\cosh(\lambda b)+q}.
\tag{20}
$$

This is an explicit *full-axis* observation error, beyond the
predecessor's two selected lower floors:

$$
\boxed{\quad
\sup_{b\ge0}|D_\eta(b)-D_*(b)|\le {8\eta\over a},
\qquad
S_2(F_\eta)\ge {25\over8a^2\eta^2}.
\quad}
\tag{21}
$$

To prove the first bound set
`f(lambda,q;b)=2lambda sinh(lambda b)/(cosh(lambda b)+q)`.
For `lambda>0`, `q in [1/2,1]`, `x=lambda b>=0`,

$$
|\partial_qf|\le2\lambda,\qquad
0\le\partial_\lambda f
 ={2\sinh x\over\cosh x+q}
 +{2x(1+q\cosh x)\over(\cosh x+q)^2}
\le6.
\tag{22}
$$

The last estimate uses `sinh x<=cosh x`,
`1+q cosh x<=2 cosh x`, and `x/cosh x<=1`. Change lambda
and then q in (22). Since `1-cos eta<=eta^2/2`,

$$
|D_\eta-D_*|
\le {6\eta\over a}+{\pi\eta^2\over a}
<{8\eta\over a}
\quad(0<\eta\le1/2),
\tag{23}
$$

using `pi<4`. The exact own-source jet identity is

$$
S_2=\lambda^2{4-q^2\over6(1-q^2)}
\ge{\lambda^2\over2\eta^2}
>{25\over8a^2\eta^2},
\tag{24}
$$

because `pi>3`, `eta<=1/2`, and `sin eta<=eta`.

The limiting field has fourth-order zeros at the same locations.
For *every* fixed uniform tolerance `delta>0` and every finite `K`,
choose eta sufficiently small that `8eta/a<=delta` and the right
side of (24) exceeds `K`. Thus the ball
`||D-D_*||_(L-infinity[0,infinity))<=delta` contains actual positive
atomic-source double threshold events with arbitrarily large `S_2`.
There is no finite upper bound on `S_2` depending only on that error
ball, `T,a`, normalization and the common moment budgets. This is a
conditioning obstruction for the stated center, not a nonuniqueness
claim at zero tolerance.

For a finite interval `[0,B]`, integration also pays the normalized
value error:

$$
\left|\log{F_\eta(ib)\over F_*(ib)}\right|
\le {8B\eta\over a},\qquad 0\le b\le B,
\tag{25}
$$

since both functions equal `1` at zero. This explicitly records the
normalization needed when passing from `D` to `F`.

The source moments remain uniformly bounded by
`M_j(T+Delta)<=exp(Delta(2pi/a)^2)(2pi/a)^j`, exactly as in the
predecessor. The source is complete; no omitted tail pays for (21).
The construction still has infinitely many simultaneous events at `T`,
and `D_*` is bounded. It does not meet theta's smooth-source or
large-height-growth premises.

## 5A. Arbitrarily many exact profile samples in a positive finite-atom source

This is the main own-source strengthening. It improves the polynomial
construction to a positive source, and improves the predecessor's
positive-source example from selected lower floors to **any prescribed
finite number of exact profile samples at prescribed distinct heights**.

Fix `a>0`, `0<T<=1/2`, `q_0=1/2`, and
`lambda=2pi/(3a)`. Choose any distinct `q_1,...,q_k` in `(0,1)`
different from `q_0`, and any distinct positive observation heights
`b_1,...,b_k`. Set `C_i=cosh(lambda b_i)>1`, and reorder these
and the compensation parameters so both lists are increasing.
Set `r_0=1` and solve

$$
\sum_{j=1}^k{r_j\over(C_i+q_j)^2}
       =-{1\over(C_i+q_0)^2},\qquad i=1,\ldots,k.          \tag{26}
$$

The matrix is nonsingular, as the following elementary integral proof
shows. Expand both determinants by permutations and integrate term by
term to obtain

$$
\det\!\left[{1\over(C_i+q_j)^2}\right]
=\int_{0<t_1<\cdots<t_k}
 \det[e^{-C_i t_\ell}]\det[e^{-q_j t_\ell}]
 \prod_{\ell=1}^k t_\ell\,dt_\ell>0.                     \tag{27}
$$

The integral converges absolutely because all parameters are positive.
For increasing exponents and increasing `t_l`, each exponential
determinant has the constant sign `(-1)^(k(k-1)/2)`. For completeness,
a nontrivial linear combination of `k` exponentials with distinct real
exponents has at most `k-1` distinct zeros: divide out the first
exponential, differentiate and apply Rolle, inducting on `k`.
This proves the determinants never vanish in the ordered region.
Their sign follows by bringing the `t_l` close together: the leading
term is their Wronskian, whose sign is the displayed sign by the
Vandermonde formula. The two signs therefore cancel pointwise in
(27), proving strict positivity. This establishes the needed matrix
fact in-note rather than importing a total-positivity assertion.

For `k=2` the determinant proof reduces to the explicit identity
with `U=(C_1+q_2)(C_2+q_1)` and
`V=(C_1+q_1)(C_2+q_2)`:

$$
\det K={(C_2-C_1)(q_2-q_1)(U+V)\over U^2V^2}>0.
\tag{28}
$$

Use (6)--(7), now with `x_j=-q_j`, `0<=j<=k`. Choose

$$
0<r\le\min\left\{
 \tfrac12\min_j\{q_j,1-q_j\},
 \tfrac13\min_{j\ne\ell}|q_j-q_\ell|\right\},
$$
$$
C=\max_j|r_j|\ge1,\qquad
M_j=\sum_{\ell\ne j}{|r_\ell|\over|q_j-q_\ell|-r},
\quad M=\max_jM_j,\qquad
0<\varepsilon<\min\{r/(4C),1/(4M)\}.                    \tag{29}
$$

The proof (13)--(14) places all `k+1` roots
`-q_j(epsilon)` in disjoint intervals inside `(-1,0)`.
They are simple, with
`|q_j(epsilon)-q_j|<=2epsilon|r_j|`. For `j=0`,
`q_0(epsilon)>q_0`, so it is distinct from `q_0`.
In the rational replay below, `k=2`, `q_1=1/4,q_2=3/4`,
and `r=1/16` satisfies all the displayed requirements.

Put

$$
P_\varepsilon(y)=(y+q_0)^2R_\varepsilon(y),\qquad
F_\varepsilon(z)={P_\varepsilon(\cos(\lambda z))
                         \over P_\varepsilon(1)}.
\tag{30}
$$

All coefficients of `P_epsilon` are positive, since its factors are
`y+q` with `0<q<1`. Every power `cos^m(lambda z)` has nonnegative
cosine coefficients. Therefore, with `N=k+3`,

$$
F_\varepsilon(z)=\sum_{n=0}^{N}w_n(\varepsilon)\cos(n\lambda z),
\qquad w_n>0,\qquad \sum_{n=0}^{N}w_n=1.                 \tag{31}
$$

Strictness follows because the positive coefficient of `y^n`
contributes positively to frequency `n`. The complete positive physical
source at time zero is

$$
\mu_\varepsilon
=\sum_{n=0}^{N}w_n(\varepsilon)
       e^{-T(n\lambda)^2}\delta_{n\lambda}.              \tag{32}
$$

Its exact heat flow is
`H_epsilon(t,z)=sum_n w_n exp((t-T)(n lambda)^2)cos(n lambda z)`.
The event normalization is `H_epsilon(T,0)=1`. For every `Delta>=0`
and integer `j>=0`, including the `j=0` mass convention,

$$
M_j(T+\Delta)\le e^{\Delta(N\lambda)^2}(N\lambda)^j.
\tag{33}
$$

These are common complete moment budgets for every admissible epsilon.

The event at `a` is exactly double because
`cos(lambda a)=-q_0` and `sin(lambda a) ne 0`. Equations (26) and
(7) prove **exactly fixed** profile samples:

$$
D_\varepsilon(b_i)=\lambda\sinh(\lambda b_i)
\left\{ {2\over C_i+q_0}
+\sum_{j=0}^{k}{1\over C_i+q_j}\right\},\quad 1\le i\le k. \tag{34}
$$

At every positive `b`, `F_epsilon(ib)>0`; the denominators
`C_i+q_j(epsilon)` are positive. The exact curvature is

$$
h_2=
{2\lambda^2(1-q_0^2)\varepsilon V(-q_0)\over P_\varepsilon(1)}
\ne0.                                                    \tag{35}
$$

The extra simple root
`a_epsilon=acos(-q_0(epsilon))/lambda` satisfies

$$
0<a_\varepsilon-a
\le {2\varepsilon\over
 \lambda\sqrt{1-(q_0+r)^2}},
\qquad
\boxed{\quad S_2(F_\varepsilon)
\ge {\lambda^2[1-(q_0+r)^2]\over4\varepsilon^2}
\longrightarrow+\infty.\quad}                           \tag{36}
$$

The first inequality uses the mean-value theorem and
`q_0(epsilon)<=q_0+r`; the second keeps this root's positive
contribution to the convergent deflated zero sum. Every finite `L`
is eventually exceeded at the **same** exact profile vector (34),
fixed `T,a`, mass normalization and moment budgets (33).

The threshold assertion also holds for this complete own-source flow.
At `T`, each factor `cos(lambda z)+q`, `0<q<1`, has only real zeros:
if `z=x+iy` with `y ne 0`, the imaginary part forces
`sin(lambda x)=0`, and the real part then has modulus greater than
one. The explicit zeros are periodic with linear density; their paired
inverse-square sum converges. The even order-one paired product, or
the elementary shifted-cosine products, consequently express
`F_epsilon` as a locally uniform limit of real-rooted paired-product
polynomials.

The `p+v p'` argument preceding (18), and local convergence of
derivatives, show that `1+v partial_z` preserves this class of
limits for real `v`. Apply the two factors in (18) repeatedly.
For (31), their limit is the displayed heat flow, uniformly on compact
complex sets: each of the finitely many modes receives
`(1+s(n lambda)^2/m)^m -> exp(s(n lambda)^2)`.
Hurwitz therefore gives only real zeros for every `t>=T`; the limit
is nonzero because its value at zero is positive.

The local double-event law gives nonreal predecessors immediately below
`T`. Any earlier all-real slice would itself be an even entire finite
cosine polynomial of order one, with positive value at zero, hence its
paired product permits the same forward-preservation proof. That would
contradict those predecessors. A later multiple zero would likewise
have a nonreal predecessor above `T`. Thus **T is the genuine positive
all-real threshold**, and every zero is simple for every `t>T`.

This source has infinitely many simultaneous double events at `T`;
it does not satisfy theta's eventual simplicity at its threshold.
Its profile is bounded by `Nlambda`, and it fails the all-height theta
floor. For `a=20,k=2` it nevertheless passes the selected floors
uniformly in epsilon:

$$
D_\varepsilon(b)\ge5\lambda\tanh(\lambda b/2),\qquad
D_\varepsilon(20)>{3\over8},\quad
D_\varepsilon(40)>{3\over8}.                              \tag{37}
$$

Indeed each `q_j(epsilon)<1`,
`lambda=pi/30>1/10`, `lambda*20/2=pi/3>1` and
`tanh(1)>3/4`. These exceed the predecessor's safe upper bounds
`3/20` and `297/1000` for the respective theta floors.
One may choose `b_1=20,b_2=40` in (26) to freeze those observations
exactly. The rational replay instead chooses `C_1=2,C_2=3`, so
`b_i=acosh(C_i)/lambda` and all residue and root-interval inequalities
are exact rational computations. Neither replay measures theta.


## 6. Control screen and exact finite replay

The accompanying rational checker uses `a=20`, observations `b=20,40`,
`c=500`, and five fixed root squares `1100,1200,1300,1400,1500`.
It computes the residues in (4), the constants in (11)--(12), and
four admissible positive epsilon values. It verifies exact event
cancellation, the PDE, fixed normalization, identical profile samples,
and the signed values of `S_2` and `Q_L` for `L=1/200`.
The positive six-atom replay uses `q_0=1/2,q_1=1/4,q_2=3/4`,
`C_1=2,C_2=3`, radius `1/16`, epsilon cap `1/64`, and the exact
fixed normalized profile values `994/495` and `1954/1365`. It checks
positive cosine coefficients, event jets, root intervals, fixed samples,
and the diagonal heat operator identity with exact rational arithmetic.
The polynomial fixed samples exceed the safe rational upper bounds
`3/20` and `297/1000` for the two theta floors, using the
predecessor's already-proved strict floor comparisons. These are
constructed polynomial observations, not measurements of theta.

The actual selected polynomial coefficients, rational inequalities and
root-interval signs carry the result; decimal printouts are only
readability aids. The [checker][checker] and [small record][record]
bind the source versions used, including working-tree contents, over
Git parent `06acae6a0aba05b8f44ea8609bd7c7986029d9d5`. Hashes identify
those versions; the proof and exact inequalities carry the claims.
No numerical assertion about the actual theta
threshold is made.

| Control | Actual comparison and scope |
| --- | --- |
| Present polynomial pencil | Exactly shares the chosen finite `D` vector, normalization, fixed event and threshold. Its exact `Q_L` becomes positive; this is the counterexample. It fails positive smooth source, theta coefficients and full theta growth. |
| Positive finite-atom pencil | Holds any finite collection of samples exactly fixed, has positive source, actual threshold, fixed height and common complete moments, yet `S_2` diverges. It fails smooth theta source, full growth and eventual simplicity at its threshold. |
| BW-01 three-atom family | Its own `D` is (20), and (21) is the actual quantified comparison. It shares positivity, exact cancellation, genuine threshold and common moments, but its limiting profile is not theta. It is not asserted to match the polynomial's fixed sample vector. |
| Euler-factor family | At time zero its own profile difference is `D_0^(c,p)-D_0=c alpha sinh(alpha b)/(1+c cosh(alpha b))>0`. It passes every inherited lower floor, but does not share a prescribed finite theta vector merely because it passes those floors. No event height, multiplicity or threshold jet has been invented. At later times that product formula is not used. |
| Even quartic/Hermite controls | Real-rooted polynomial threshold geometry applies; the unchanged source and full theta profile are absent. Their own profile values need not equal (10). |
| Weighted-square and finite-prime controls | Their documented local events do not provide the all-real threshold premise used by the first theorem. Their intermediate positive-source facts are not evidence of threshold matching. |
| Reflected, smooth and positive-primitive controls | Their stated positive channels and reflection do not supply the unchanged theta profile; no uncomputed exact threshold or sign is assigned. |

The Euler comparison is included because a failure of literal theta
identity does not imply a failure of a derived inequality. The exact
finite-profile construction only shows that a function of the selected
data cannot distinguish the members of *that* constructed fiber.
Euler's own data need not lie on it.

## 7. Stopping scope and next useful observation

Finite observations can bound the jet on other, separated classes.
Under the same order-at-most-one, even paired-product hypotheses,
`F(0)>0`, an exact double all-real event at `a>0`, and `b>0`,
set `A=a^2`, `B=b^2` and

$$
R={D(b)\over b}-{4\over A+B}
 =\sum_{\rho>0,\,\rho\ne a}{2m_\rho\over\rho^2+B}.
\tag{38}
$$

If `0<R<2/(A+B)`, then every other root satisfies
`rho^2>=Y:=2/R-B>A`; this follows by retaining one copy of that
root's positive contribution. The ratio of its deflated kernel to
its profile kernel is

$$
{(A+y)(B+y)\over(y-A)^2},
$$

which decreases for `y>A`: its derivative has numerator
`-(3A+B)y-A^2-3AB<0`. Hence there is a genuine upper estimate

$$
S_2\le{1\over2a^2}
 +R\,{(A+Y)(B+Y)\over(Y-A)^2}.                           \tag{39}
$$

If `R=0`, only the mirror contribution remains. This observation
explains why the obstruction must be stated at its constructed
vectors, and not as "no finite profile data can bound a jet."
It also gives a concrete comparison with the actual theta premise:
for every `b>=40`, the inherited full-source floor gives

$$
{D_T(b)\over b}>{1\over4b}
 >{6\over b^2}\ge{6\over A+B},
\quad\hbox{hence}\quad R>{2\over A+B}.
\tag{40}
$$

Here `log((b+1)/(4pi))>1` for `b>=40`, using
`4pi e<4(22/7)3<41`. Thus the simple small-residual-mass upper
consumer (39) has an explicitly failed premise on theta at every
height `b>=40`, including the inherited adaptive observation.
This does not exclude combinations of profile data with signed or
source-specific information. The upper bound is a conditional
geometric estimate; the theta feasibility failure is proved from
the existing lower floor, not from a newly acquired theta profile.

Stop a proposed universal upper estimate whose complete information is
only the finite observations (2) plus the first theorem's stated
threshold class, unless it supplies an additional condition excluding
the degenerating root. Also stop a uniform normalized-jet claim based
only on a finite-error full-profile ball centered at `D_*` in the
positive atomic class. Those exact attempts are closed by the explicit
families, with all conditioning constants retained.

This does not close BW-08, BW2-03 or a profile argument tied to the
actual unchanged theta source. A next meaningful contract would need
one of: a quantitatively separated root/multiplicity class; an acquired
curvature floor as an explicitly restricted class; or a source-specific
profile estimate whose actual values exclude these degenerating fibers.
Adding more finitely many samples alone does not remove the first
construction. Exact knowledge of the entire analytic profile is outside
both obstructions and remains a uniqueness fact, not a useful sign
estimate by itself.

The results supply scoped failures, not a usable theta upper bound,
so they do not activate BW2-04 or a multiplicity transfer. No theta
region, improved Newman bound, physical winding claim or later witness
is recorded.

[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[program]: ../../../research-overview/02_THRESHOLD_SIGNED_ARITHMETIC_RESEARCH_PROGRAM_20261020.md
[atomic]: ../../01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md
[review]: ../reviews/03_FINITE_PROFILE_CONDITIONING_REVIEW_20261020.md
[checker]: ../numerics/check_finite_profile_conditioning.py
[record]: ../numerics/FINITE_PROFILE_CONDITIONING_CONTROLS_20261020.json
