# Effective relative tails, transport comparison, and the remaining gap input

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), separate same-model analytic derivation. The exact
serving variant and configured reasoning effort are not exposed and are
not inferred. This is internal research, not independent specialist
refereeing. No new support-window certificate or large numerical run is
performed here.

The [signed two-prime result](ALL_WINDOW_EXTENSION_OUTCOME_20261003.md)
and [relative compactness audit](../reviews/ALL_WINDOW_SCALING_AUDIT_20261003.md)
leave an effective spectral question. This note supplies explicit counting
bounds, a relative approximation retaining the mixed blocks, and a
finite-column certificate for a positive source gap that does not assume
arithmetic positivity. The available constants are too pessimistic to
justify executing that certificate at large rank. In particular these
results do not establish the all-window inequality `K<=B`.

## 1. Inherited objects and what is not new

On the fixed source interval `I_L=(-L/2,L/2)`, use the closed complex
three-moment source space `H_L` and its logarithmic Fourier form domain.
For fixed finite `S`, let `B=B_{S,L}` be the positive closed source operator
and let `K=K_{S,L}` be the bounded selfadjoint correction. The preceding
audit proves compact resolvent and a strictly positive, initially
nonnumerical gap for B. The correction has the independent bound

\[
\|K\|\le k_{S,L}:=L\sqrt{(1-g_S)/g_S},\qquad
g_S=\rho_Sg_0,\quad g_0=57/10^6,
\]
\[
\rho_S=\left[\prod_{p\in S}
\frac{1-p^{-1/2}}{1+p^{-1/2}}\right]^2.
\tag{1}
\]

Let

\[
C_{S,L}=2\sum_{\substack{p\in S,m\ge1\\m\log p<L}}
                     (\log p)p^{-m/2}.
\tag{2}
\]

Only these powers contribute on the source interval, even though the
fixed-set phase contains all powers. Capturing all active primes is needed
to identify the resulting bulk with the complete arithmetic Q, but is not
needed for the spectral estimates for B itself.

The actual metric transport comparison

\[
\boxed{\rho_SB_{\varnothing,L}\le B_{S,L}
                         \le\rho_S^{-1}B_{\varnothing,L}}
\tag{3}
\]

is **already established**, as equation (27) of the
[canonical comparison audit](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md).
Here the empty prime set denotes the archimedean Sonin operator, not an
infinite-place limit. For clarity, its proof uses
`J_S=D Pi_0 M_S^(-1/2)`, `M_S=Pi_0 D*D Pi_0` on the archimedean Sonin
space, and `Pi_S=J_S J_S*`. Commutation of source convolution with D gives

\[
\|C_F\Pi_S\|_{\rm HS}^2
=\|D C_F\Pi_0M_S^{-1/2}\|_{\rm HS}^2.
\]

The bounds `ell I<=|D|<=u I` and `ell² I<=M_S<=u² I` prove (3).
Replacing the inverse compressed metric by the identity would not prove
this comparison. It implies, on the same source moment space,

\[
\rho_S b_{0,n}\le b_{S,n}\le\rho_S^{-1}b_{0,n},\qquad
\beta_{S,L}\ge\rho_S\beta_{0,L}.
\tag{4}
\]

Thus a numerical archimedean source gap can be transferred without
subtracting `k_{S,L}`. The comparison does not supply that archimedean
gap numerically.

The repository already has scalar infinite Legendre-tail and Schur
reductions in the [Weil-depth manuscript, section 4](../../../shifted-zeta/weil-depth/manuscript/finite_horizon_weil.tex).
Neither scalar high-energy reduction nor the warning about discarded
arithmetic cancellation is a new proof mechanism. The added results below
apply them to the **actual positive Sonin source operator**, quantify
relative spectral tails, and separate mixed-block approximation from
plain compression.

## 2. An explicit global logarithmic lower bound

Write `gamma_0=gamma(0)=-gamma_E-pi/2-3 log 2-log pi` and

\[
m(t)=\tfrac12\log(1+4t^2)\ge0.
\]

The digamma series gives

\[
\gamma(t)-\gamma_0
=\sum_{n\ge0}\frac{2t^2}{a_n(a_n^2+t^2)},\qquad a_n=2n+1/2.
\]

For fixed t the summand, viewed as a function of positive `a_n`, is
decreasing. Comparison with its integral therefore yields

\[
\gamma(t)-\gamma_0
\ge\int_{1/2}^{\infty}\frac{t^2}{a(a^2+t^2)}\,da
=\tfrac12\log(1+4t^2)=m(t).
\tag{5}
\]

This elementary bound is valid for every real t. Put `M_L=P_H m(D) P_H`
in the sense of closed forms on supported sources. The bulk identity and
(1) imply

\[
B_{S,L}\ge M_L-d_{S,L}I,\qquad
d_{S,L}=C_{S,L}+k_{S,L}-\gamma_0.
\tag{6}
\]

Alternatively (3) and its empty-set counterpart give

\[
B_{S,L}\ge\rho_S M_L-\rho_Sd_{0,L}I,\qquad
d_{0,L}=k_{0,L}-\gamma_0.
\tag{7}
\]

The following estimates allow any proved constants `a>0,d>=0` such that

\[
B\ge aM_L-dI.
\tag{8}
\]

Both (6) and (7) are available; neither should silently replace the
actual arithmetic term by a smaller loss. Known sharper archimedean or
signed prime estimates can later replace these crude constants.

## 3. Explicit eigenvalue counting from a time-band trace

Let `A_R=P_H P_{I_L}1_{[-R,R]}(D)P_{I_L}P_H` on `H_L`. It is a positive
contraction and

\[
\operatorname{Tr}A_R\le LR/\pi.
\tag{9}
\]

The equality before moment compression follows from the diagonal value
`R/pi` of the sine kernel. Since `m(t)>=m(R)` outside the band,

\[
M_L\ge m(R)(I-A_R).
\tag{10}
\]

Suppose an n-dimensional subspace lies in the spectral subspace
`1_{(-infinity,Lambda]}(B)`. Its unit vectors have m-energy at most
`E=(Lambda+d)/a`. Summing the low-frequency mass over an orthonormal
basis and using (9) gives

\[
n\left(1-\frac E{m(R)}\right)\le LR/\pi
\quad\text{whenever }m(R)>E.
\]

Consequently the eigenvalue counting function, with multiplicities,
satisfies the explicit bound

\[
\boxed{N_B(\Lambda)\le
\inf_{m(R)>E}\frac{LR}{\pi(1-E/m(R))}.}
\tag{11}
\]

For `E>=0`, choosing `m(R)=E+1` gives the convenient closed expression

\[
\boxed{N_B(\Lambda)\le
\frac L{2\pi}(E+1)\sqrt{e^{2(E+1)}-1}
<\frac L{2\pi}(E+1)e^{E+1}.}
\tag{12}
\]

This is an upper bound on a finite number, not a prediction of the true
number of low modes. Equivalently, minmax gives, for every `0<eta<1`,

\[
\boxed{b_n\ge
a(1-\eta)m(\eta\pi n/L)-d.}
\tag{13}
\]

Indeed in any n-dimensional subspace there is a unit vector with
band mass at most `LR/(pi n)`; take `R=eta pi n/L` and use (8).
These estimates remain valid after all three moment constraints, because
compression can only decrease the time-band trace.

For comparison with existing code, the inherited fractional Legendre-tail
lemma gives a sharper explicit polynomial-complement bound. If a source
is orthogonal to the first N Legendre polynomials, `N>=1`, then

\[
\int\log|t|\,|\widehat F(t)|^2\frac{dt}{2\pi}
\ge[\psi(N+1)+\log(2/L)]\|F\|^2.
\]

Since (5) also gives `gamma(t)>=gamma_0+log(2|t|)` for `t!=0`,

\[
B_{S,L}[F]\ge
\bigl[\psi(N+1)+\log(4/L)+\gamma_0-C_{S,L}-k_{S,L}\bigr]\|F\|^2.
\tag{14}
\]

This reuses the earlier lemma; it is not a fresh derivation of the
Weil-depth scalar tail. On the moment source space the same complement
is obtained by taking the span of the exact moment projections of those
polynomials. Its dimension is at most N. Formula (14) can improve the
counting constants, but the subtractive loss `k_{S,L}` still remains.

## 4. Relative spectral tails without an unknown bottom gap

Let `H=B^(-1/2) K B^(-1/2)` as in the preceding audit. The two operator
inequalities

\[
-kB^{-1}\le H\le kB^{-1}
\tag{15}
\]

show that, for `epsilon>0`,

\[
\#\{\lambda(H)>\epsilon\}\le N_B(k/\epsilon),\qquad
\#\{\lambda(H)<-\epsilon\}\le N_B(k/\epsilon).
\tag{16}
\]

Thus (11) or (12) gives an explicit finite bound for each count, without
knowing a numerical `beta=inf spec B`. These statements count eigenvalues;
they do not certify a chosen finite trial subspace or its eigenvectors.

There is a related approximation which handles the mixed blocks more
efficiently than compression alone. Let E be the actual spectral
projection onto the first n B modes, and set `Q_E=I-E`. Define

\[
J_n=EH+HE-EHE=H-Q_EHQ_E.
\]

Then

\[
\boxed{\operatorname{rank}J_n\le2n,\qquad
\|H-J_n\|\le k/b_{n+1}.}
\tag{17}
\]

The range is contained in `Ran E + Ran HE`; all mixed blocks remain in
`J_n`. In contrast, replacing H by `EHE` requires separately controlling
the mixed block, with the crude bound `k/sqrt(beta b_{n+1})`. Formula
(17) avoids that dependence in the **remainder**, but its implementation
still requires the full columns `HE`, not just matrix entries `EHE`.
If approximations to these columns have operator error at most eta,
selfadjoint symmetrization gives a finite-rank approximation with an
additional error at most `3 eta`, by the same calculation in section 6.

The spectral subspace here is not provided by (12). A numerical Legendre
compression cannot simply be declared to be the first n B eigenmodes.
Section 6 provides an alternative that uses a specified polynomial
subspace and a shifted resolvent instead.

## 5. What actual metric transport helps, and where its constants hurt

Comparison (3) transfers an independently certified `beta_{0,L}` to
`rho_S beta_{0,L}`. It also yields a bounded positive metric in
archimedean source-energy coordinates:

\[
G=B_{0,L}^{-1/2}B_{S,L}B_{0,L}^{-1/2},\qquad
\rho_S I\le G\le\rho_S^{-1}I.
\tag{18}
\]

The form in (18) defines a bounded operator; it is not a claim that the
unbounded factors can be multiplied on an arbitrary vector. With
`N=B_{0,L}^{-1/2}K_SB_{0,L}^{-1/2}`, arithmetic positivity is equivalent
to `G-N>=0`. The metric G must be retained, including its mixed blocks.
It generally does not commute with an archimedean spectral projection.

For the crude counting bound (12), the direct and transported energy
parameters are respectively

\[
E_{\rm direct}=\Lambda+C_{S,L}+k_{S,L}-\gamma_0,
\qquad E_{\rm transport}=\Lambda/\rho_S+k_{0,L}-\gamma_0.
\tag{19}
\]

One may use the smaller resulting count bound. Avoiding a subtractive
`k_S` is helpful near the spectral bottom if a real archimedean gap is
available. It does not automatically improve high-energy tails: the
factor `1/rho_S` in (19) can cost much more.

For orientation only, ordinary floating evaluation at `L=6/5,S={2,3}`
gives

\[
\rho_S\simeq0.002113499569,\quad k_{0,L}\simeq158.939353,
\quad k_{S,L}\simeq3457.344931,\quad C_{S,L}\simeq2.248826.
\]

The logarithm to base ten of the simple upper bound (12), at
`Lambda=k/epsilon`, is approximately:

| Relative tail threshold epsilon | Direct count bound: log10 | Transport count bound: log10 |
|---|---:|---:|
| 1 | 3010 | 710513 |
| 1/2 | 4512 | 1420949 |
| 1/10 | 16524 | 7104437 |

These are **resource diagnostics for this pessimistic sufficient bound**,
not outward records, measured ranks, lower bounds on necessary work, or
an obstruction to better estimates. Their scale is already sufficient
reason not to launch a rank expansion based on (12).

The small [cost script](../numerics/all_window_mechanism_20261003/cost_preflight.py)
and [record](../numerics/all_window_mechanism_20261003/cost_preflight.json)
reproduce the six entries in logarithmic arithmetic without constructing
any source space or matrix at these scales.

As the support-adapted prime set grows,

\[
\log\rho_S^{-1}=4\sum_{p\in S}p^{-1/2}+O(1),
\tag{20}
\]

because the remaining odd powers have a summable `p^(-3/2)` majorant.
The prime-number-theorem scale already used in the original strategy
therefore makes `k_S` much worse than the finite prime-amplitude loss.
Inserting that norm into an exponential count bound compounds the loss.
Neither more arithmetic precision nor the two-sided transport identity
repairs this scalar-estimate problem.

## 6. A finite-column shifted-resolvent certificate for beta

There is a way to make the fixed-window positive B gap reviewable without
assuming Q positive or possessing B eigenvectors. It still needs genuine
operator residuals and can be expensive.

Assume (8), choose `tau>d`, and write

\[
R_\tau=(B+\tau I)^{-1},\quad s=\tau-d>0,
\quad c=a m(R).
\]

Positivity of B gives the known bound `||R_tau||<=1/tau`. Equations
(8) and (10), and order reversal for inverses, give

\[
0<R_\tau\le[sI+c(I-A_R)]^{-1}.
\tag{21}
\]

For `0<=x<=1`, the convex function `1/(s+c(1-x))` lies below the chord
joining its endpoint values. Functional calculus therefore yields

\[
R_\tau\le\frac1{s+c}I+
       \left(\frac1s-\frac1{s+c}\right)A_R.
\tag{22}
\]

This chord estimate is useful because the chosen source projection need
not commute with `A_R` or B.

Let E be the orthogonal projection in `H_L` onto the exact moment
projections of the first N Legendre polynomials, and let `Q_E=I-E`.
The subspace and its finite Gram matrix are explicit; zero vectors are
removed before orthonormalizing it. Under unitary dilation to `I_1`,
the distance from `v_t=P_H exp(iLty)` to this subspace is at most the
**raw** plane-wave Legendre tail, because `P_H P_N exp(iLty)` belongs
to its range. No approximation to the moment functions is made.

Using the tail function from the preceding scaling audit, provided
`(LR/2)^2<(2N+1)(2N+3)`, one obtains

\[
\|Q_E A_R Q_E\|\le\operatorname{Tr}(Q_E A_R Q_E)
\le\frac{LR}{\pi}\tau_N(LR/2)^2.
\]

Set

\[
\delta=\min\left(1,\frac{LR}{\pi}\tau_N(LR/2)^2\right),\qquad
\epsilon_{R,N}=\frac{1-\delta}{s+c}+\frac\delta s.
\tag{23}
\]

Compression of (22) proves

\[
\|Q_E R_\tau Q_E\|\le\epsilon_{R,N}.
\]

Therefore the mixed-block-retaining operator

\[
J=ER_\tau+R_\tau E-ER_\tau E
\]

has rank at most `2 rank E` and satisfies

\[
\boxed{\|R_\tau-J\|\le\epsilon_{R,N}.}
\tag{24}
\]

Only finitely many full resolvent columns are needed. Let
`U:C^n -> H_L` be an exact orthonormal synthesis of the specified E,
and let `Y:C^n -> D(B)` approximate `R_tau U`. Suppose the full source
residual obeys

\[
\mathcal R=U-(B+\tau I)Y,\qquad\|\mathcal R\|\le r.
\tag{25}
\]

Then `||R_tau U-Y||<=r/tau`, with no numerical beta assumption. Define
the finite-rank selfadjoint operator

\[
J_Y=YU^*+UY^*-U\operatorname{Re}(U^*Y)U^*.
\tag{26}
\]

It has range in `Ran U + Ran Y`, and subtraction of the three terms
from their exact counterparts gives

\[
\boxed{\|R_\tau-J_Y\|
\le\epsilon_{R,N}+3r/\tau=:\eta.}
\tag{27}
\]

A nonorthogonal Gram representation on this at-most-2n-dimensional
range is acceptable if the metric is included. If an outward finite
calculation proves `J_Y<=mu I` with `mu>=0`, and

\[
u:=\mu+\eta<1/\tau,
\]

then spectral calculus proves the explicit source gap

\[
\boxed{B\ge\left(\frac1u-\tau\right)I>0.}
\tag{28}
\]

This is a concrete sufficient certificate for beta, not the assertion
that beta exists under another name. Its inputs are a chosen exact source
subspace, finitely many full equation residuals, and outward finite
matrix bounds. Tested-row residuals do not suffice. A finite state trace
cannot replace the resolvent columns: it is a compact source operator and
cannot independently provide the needed coercivity.

The ability to evaluate the full residuals (25) efficiently for the actual
multi-prime B remains an implementation obligation. The norm bound for K
alone does not compute those residuals. This note supplies no such computed
Y or positive numerical beta; the two-prime arithmetic certificate is not
being reused as an assumption that B has a particular gap.

## 7. Cost and the precise limit of the new reduction

The polynomial tail can be made small by increasing N proportionally to
`LR`. Even after that, (23) only decreases like `1/log R`. If the true
source gap is beta, distinguishing

\[
\|R_\tau\|=\frac1{\tau+\beta}<\frac1\tau
\]

requires errors smaller than `beta/[tau(tau+beta)]`. For small beta this
means `a m(R)` on the scale `tau^2/beta` in this elementary remainder,
and therefore R on an exponential scale in that quantity. This diagnoses
the cost of the displayed sufficient certificate; it is not a lower
bound for better resolvent algorithms. Applying it first to the empty-set
B and then (4) can reduce tau substantially, but still leaves a numerical
archimedean source-gap and full-residual problem.

The scalar data `B>=0`, injectivity, compact resolvent, (6), and (3) cannot
by themselves force a positive numerical beta: the lower bound (6) is
negative on the low-energy region, and a positive first eigenvalue can
approach zero while all the stated high-energy bounds remain fixed.
Finite head information or a new analytic lower bound is therefore
essential. Equations (25)--(28) specify one way to supply it.

What has advanced is the quantitative form of the reduction:

- explicit counting estimates (11)--(13) now bound the number of relative
  modes that can exceed any prescribed threshold;
- retaining full mixed columns yields (17), without a beta-dependent
  truncation loss;
- the shifted-resolvent construction (23)--(28) gives a gap certificate
  in a specified source subspace, without B eigenvectors or arithmetic
  positivity.

The estimates also show why a norm-only all-window route is presently
uncompetitive. An all-window proof still needs signed arithmetic or
Sonin structure controlling the finite relative comparison and its mixed
columns at useful cost. No amount of enlarging a scalar tail bound proves
the missing finite comparison `H<=I`, and no new support sweep is justified
by the bounds in this note.
