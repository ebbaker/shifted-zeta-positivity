# Smooth-weight uniformity source pass

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred.

**Finding.** The fixed reference-window theorem and its Fourier transfer admit
a paper-level derivation of U2 with the required quantifier order. Choose the
reference window and its Fourier exponent before the support interval, then
use a finite smooth dyadic partition. A smaller positive capacity margin
handles the rescaled column lengths. The resulting constant is homogeneous of
degree two in the ordinary smooth-weight seminorm. Conditional on U1's exact
arithmetic dictionary, this gives October 5 Proposition `thm:ms` as a
mathematical consequence of the read contracts. **U2 is not closed as a checked
Lean application:** the ordinary-derivative conversion, finite partition and
scale transport have not been instantiated or compiled here.

This pass invokes no Lean, Lake, comparator or VM command. It does not establish
the other crosswalk applications or independently validate the theorems whose
source contracts it reads.

## Pinned contracts and source identities

All upstream sources are at
`openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. The seven main Lean
files below were fetched into a separate sparse audit checkout; their contents
match the hashes in the saved source-closure manifest. Line numbers in this
pass are physical one-based lines at that pin.

| Contract | Exact declaration and locator |
| --- | --- |
| Required O5 quantifiers | [October 5 `paper2.tex:679–689`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex#L679-L689): `k=k(theta,epsilon)` precedes every compact interval `I`, every smooth weight supported in `I`, and `D>=2`; its implied constant may depend on `nu,S,I,theta,epsilon`. |
| Centrally normalized polynomial | `OAI.SevenEighths.HeckeDyadic.polynomial`, [Dyadic.lean:44–49](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/Dyadic.lean#L44-L49): at `(sigma,freq)=(0,0)`, it is `D^(-1/2)` times the ideal sum. |
| Full raw predicate | `OAI.SevenEighths.HeckeInverseAmplification.RawMoment`, [InverseAmplificationRaw.lean:11–16](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Hecke/InverseAmplificationRaw.lean#L11-L16): all `H>=1`, `D>0`, `D^(1+c)<=H`, and all admissible finite nonzero-element row sets; upper bound `C H (H max(1,D))^kappa`. |
| Fixed reference and twists | `OAI.SevenEighths.DetectorDictionaryInverseRawReference.raw_reference_moment`, [InverseRawReference.lean:132–143](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Dictionary/InverseRawReference.lean#L132-L143): `exists J, forall data, exists C>0, forall t`, raw bound for `childLogTest W t` with constant `C(1+|t|)^(2J)`. |
| Exact quadratic transfer | `OAI.SevenEighths.DetectorDictionaryInverseRawFourier.rawMoment_reference`, [InverseRawEnergy.lean:60–80](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Dictionary/InverseRawEnergy.lean#L60-L80): arbitrary smooth annular `V` agreeing with a reference window transfers with exactly `C B_J(V)^2`. |
| Logarithmic profile | `OAI.CubicReflectionKernel.logSchwartz` and `logSchwartz_apply`, [ReflectedKernel.lean:167–186](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Mellin/ReflectedKernel.lean#L167-L186): `g(u)=V(exp u)`, with compact support in `[log a,log b]`. |
| Existing Fourier seminorm bound | `OAI.FourierBridge.uniform_fourier_one_plus_moment`, [LogProfiles.lean:1123–1186](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Mellin/LogProfiles.lean#L1123-L1186): weighted Fourier `L1` is controlled by source Schwartz seminorms of derivative orders through `J+p`, where `p=(volume : Measure R).integrablePower`. Its [coefficientMomentBound:1113–1121](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Mellin/LogProfiles.lean#L1113-L1121) is linear in the bound parameter. |
| Uniform bounded-scale controls | `inverse_polynomial_bound`, [InverseRawCompact.lean:29–55](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Dictionary/InverseRawCompact.lean#L29-L55), and `nonzero_element_rows_card`, [same file:76–84](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Dictionary/InverseRawCompact.lean#L76-L84). These retain explicit dependence on a supplied sup-norm bound and hold for all `D>0`. |

The corresponding SHA-256 identities are:

| File, relative to `lean/OAI/NumberTheory/DirichletL/` | SHA-256 |
| --- | --- |
| `Dictionary/InverseRawReference.lean` | `72ba8916857bb07d0420518975cc1393facbd958b36932a13a0ef0e3ef28d0d1` |
| `Dictionary/InverseRawEnergy.lean` | `5c8ed5e967fd98ce8e65808ac7ade110af40473c3bbfab763d00170866663af6` |
| `Hecke/InverseAmplificationRaw.lean` | `b769af45d6c89e213a94e1c964486b5c9cfaa186824678a734d44008093e29c6` |
| `Hecke/Dyadic.lean` | `532a488b08c81b0f60a9f765693a9cf26d800cd08caba9c261a79fb65921dcd3` |
| `Dictionary/InverseRawCompact.lean` | `187dd0f0114c1693d264f45f5756b259570abd971fb726657770375c01278268` |
| `Mellin/ReflectedKernel.lean` | `1b8cdac8957ad098d2834e9ddc30a6653abd526dd91632e5477dfc8525e2a1e6` |
| `Mellin/LogProfiles.lean` | `ff8735e421a2ee659df15272704206f2d114d7e2a849e8a755d545508f4038be` |

The October 5 source hash is the already recorded
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.

## Seminorm and reference choice

For a smooth complex function on `R`, use

\[
 M_k(W)=\max_{0\le r\le k}\sup_{x\in\mathbb R}|W^{(r)}(x)|.
\]

The zeroth derivative is included; absolute value is the complex norm.
For a compactly supported smooth function on `(0,infinity)` whose support is
contained in a compact positive interval, extend it by zero to `R`. The
extension is smooth and has the same seminorm. This is the convention in the
O5 proposition.

Fix the standard annulus `A=[1/2,2]` once, before choosing `I` or `W`. Choose a
Schwartz cutoff `R` that is one on `A` and supported in `[1/4,3]`. The exact
source construction is
`OAI.SevenEighths.InverseSecondChildWindows.positive_cutoff`,
[SecondChildWindows.lean:14–34](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Inversion/SecondChildWindows.lean#L14-L34),
with `a=1/2,b=2`.

For prescribed positive `c,kappa`, choose `c0=c/2`. Apply the fixed reference
theorem to this **one** cutoff and `(c0,kappa)`:

\[
 \exists J\in\mathbb N\ \forall\mathrm{data}\ 
 \exists C_{\mathrm{data},c,\kappa}>0\ \forall t,
 \quad\mathrm{RawMoment}
 (\mathrm{data},\mathrm{childLogTest}(R,t),c_0,\kappa,
 C_{\mathrm{data},c,\kappa}(1+|t|)^{2J}).
\]

In particular, `J` precedes both `data` and every later interval `I`. Changing
the reference window with `I` would lose this useful quantifier order.

## Weighted Fourier bound on the standard annulus

For `V` supported in `A`, put `g(u)=V(exp u)` and

\[
 B_J(V)=\int_{\mathbb R}(1+|v|)^J|\widehat g(v)|\,dv.
\]

The source Fourier convention is the standard `2 pi` convention; its inverse
phase is [LogProfiles.lean:1188–1190](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/OAI/NumberTheory/DirichletL/Mellin/LogProfiles.lean#L1188-L1190).
Splitting at `|v|=1` and integrating by parts `m=J+2` times gives

\[
 B_J(V)\le 2^{J+1}
 \left(\|g\|_{L^1}+(2\pi)^{-(J+2)}
                  \|g^{(J+2)}\|_{L^1}\right).
\]

Indeed, the small-frequency region uses `|hat g|<=||g||_1`; outside it,
`|hat g(v)|<=(2 pi |v|)^(-m)||g^(m)||_1`, and the remaining tail integral is
`integral_(|v|>1) |v|^(-2) dv=2`. Compact support eliminates boundary terms.
This is a paper-level derivation, not a newly compiled Fourier lemma.

On the fixed log annulus `[log(1/2),log 2]`, of length `L=log 4`,

\[
 g^{(m)}(u)=
 \sum_{r=1}^{m}{m\brace r}e^{ru}V^{(r)}(e^u),\qquad m\ge1,
\]

where the coefficients are Stirling numbers of the second kind. Therefore
`||g||_1<=L M_0(V)` and
`||g^(m)||_1<=L (sum_(r=1)^m {m brace r} 2^r) M_m(V)`. Consequently

\[
 B_J(V)\le K_J M_{J+2}(V),
\]

with `K_J` depending only on the fixed annulus and `J`. This supplies the
explicit sufficient derivative order `k=J+2>=2` for the paper-level argument.

There is also a route closer to existing Lean declarations. The displayed
`uniform_fourier_one_plus_moment` uses derivative order `J+p`, with the fixed
natural number `p=(volume : Measure R).integrablePower`. Because `g` and its
derivatives have fixed compact support, its two source Schwartz seminorms are
bounded by a fixed constant times `M_(J+p)(V)`. The bound parameter appears
linearly, so that theorem likewise yields a homogeneous Fourier bound. This
would give `k=max(1,J+p)`, still before `I`. This pass does not identify `p`
numerically with two or claim to have compiled the ordinary-to-Schwartz
seminorm conversion. Either finite order suffices for O5; optimality is not
needed.

Since `R V=V` on positive inputs, the exact `rawMoment_reference` contract then
gives, for every such standard-annulus `V`,

\[
 \mathrm{RawMoment}
 (\mathrm{data},V,c_0,\kappa,
 C_{\mathrm{data},c,\kappa}K_J^2M_k(V)^2).
\]

Its coefficient is exactly quadratic in `V`; no `1+M_k(V)` term is introduced.

## Finite partition of an arbitrary positive support interval

Fix `I=[a,b]` with `0<a<=b`. Choose one smooth function `psi`, supported in
`[1/2,2]`, satisfying

\[
 \sum_{j\in\mathbb Z}\psi(2^{-j}x)=1,\qquad x>0.
\]

For example, choose a nonnegative smooth bump `chi` supported in the standard
annulus and positive on `[3/4,3/2]`. The locally finite sum
`Q(x)=sum_(j in Z) chi(2^(-j)x)` is positive for all positive `x` and satisfies
`Q(2x)=Q(x)`. Set `psi(x)=chi(x)/Q(x)` there, and extend it by zero outside the
positive axis. The extension is smooth because its support is bounded away
from zero. This fixes the same `psi` for all intervals.

Only the finite set

\[
 F_I=\{j\in\mathbb Z:a/2\le 2^j\le2b\}
\]

can meet the support of `W`. Write `lambda_j=2^j`, `N=|F_I|`, and define

\[
 W_j(x)=W(x)\psi(x/\lambda_j),\qquad
 V_j(y)=W(\lambda_j y)\psi(y).
\]

Then `V_j` is supported in the one standard annulus,
`W_j(x)=V_j(x/lambda_j)`, and `W=sum_(j in F_I) W_j` as functions on all `R`.
The latter identity is needed only where `W` is nonzero; outside its support
every summand is zero. The zero-weight or empty-set case is immediate.

Leibniz and the ordinary chain rule give

\[
 M_k(V_j)\le B_{\psi,k}\max(1,\lambda_j)^k M_k(W),
\]

where, for example,
`B_(psi,k)=max_(0<=r<=k) sum_(ell=0)^r binomial(r,ell)
||psi^(r-ell)||_infinity`. Thus the derivative **order** stays `k`; the finitely
many dilation costs may depend on `I`.

## Central normalization and the capacity margin

For a fixed row character, abbreviate the inverse polynomial at zero twists
by `P_D(W)`. Its definition gives, for every `D>0` and `lambda_j>0`,

\[
 P_D(W_j)=\sqrt{\lambda_j}\,P_{\lambda_jD}(V_j),
 \qquad |P_D(W_j)|^2=\lambda_j|P_{\lambda_jD}(V_j)|^2.
\]

The square-root factor comes from **central normalization**. It cannot be
dropped. The unnormalized ideal sums have identical summands, and positive
real scales justify the complex power factorization. No row character,
excluded prime, row label or coefficient is changed by this identity.
Compact support ensures the ideal sums have finite support, so their
linearity under this finite partition is legitimate.

Do not apply the reference raw predicate at the old gap `c` to `lambda_j D`:
`H>=D^(1+c)` need not imply `H>=(lambda_j D)^(1+c)`. Instead use the previously
chosen `c0=c/2`. Let

\[
 L_I=\max(1,\max_{j\in F_I}\lambda_j),\qquad
 D_0=\max\left(2,L_I^{(1+c_0)/(c-c_0)}\right).
\]

For `D>=D0` and `H>=D^(1+c)`,

\[
 (\lambda_jD)^{1+c_0}
 \le D^{c-c_0}D^{1+c_0}
 =D^{1+c}\le H.
\]

This threshold depends on `I,c`, not on `W`. The condition `c-c0>0` is
essential. All nonzero-element row sets and their original bound `norm(u)<=H`
are preserved.

For every positive `D`,
`max(1,lambda_j D)<=max(1,lambda_j) max(1,D)`. Keeping these maxima avoids an
unnecessary assumption that every rescaled column length is at least one.
For `D>=D0`, finite Cauchy–Schwarz row by row gives the correctly quadratic
bound

\[
\begin{aligned}
 \sum_u|P_D(W)|^2
 &\le N\sum_{j\in F_I}\sum_u|P_D(W_j)|^2\\
 &\le C_{\mathrm{data},c,\kappa}K_J^2 B_{\psi,k}^2\,
 N\left(\sum_{j\in F_I}
       \lambda_j\max(1,\lambda_j)^{\kappa+2k}\right)
 M_k(W)^2\,H\bigl(H\max(1,D)\bigr)^\kappa.
\end{aligned}
\]

`N` is fixed with `I`; it does not grow with `D`, and no extra scale loss is
needed. Replacing this finite Cauchy estimate by an unqualified sum of energies
would omit a required factor.

## Bounded scales, including scales near zero

O5 requires only `D>=2`. Its missing bounded segment is `2<=D<D0`, which must
be controlled with a constant independent of the weight. The source raw
predicate is stronger, quantifying **every** `D>0`; that range can also be
retained rather than silently narrowed.

For `B=M_k(W)>=M_0(W)`, the explicit inverse-polynomial bound supplies

\[
 |P_D(W)|\le128\max(1,b)B\sqrt D,\qquad D>0.
\]

The source row-count bound is `#rows<=128H` for `H>=1`. Thus, for every
`0<D<D0`, even without using the capacity condition,

\[
 \sum_u|P_D(W)|^2
 \le128^3\max(1,b)^2M_k(W)^2HD
 \le128^3\max(1,b)^2D_0M_k(W)^2H
 \le128^3\max(1,b)^2D_0M_k(W)^2H
       \bigl(H\max(1,D)\bigr)^\kappa.
\]

The last inequality uses `H>=1,kappa>0`. This also handles `D` near zero; it
does not introduce a spurious negative power of `D` from central
normalization. The explicit source bound incorporates the disappearance of
the ideal support at very short lengths. Using the predicate's `max(1,D)` is
necessary for this unrestricted small-scale formulation.

Taking the sum, or maximum, of the positive large- and bounded-scale
constants therefore gives the paper-level quantified consequence

\[
\begin{gathered}
 \forall c,\kappa>0\ \exists k=k(c,\kappa)\ge1,\\
 \forall I\subset(0,\infty)\text{ compact interval}\
 \forall\mathrm{data}\ \exists C_{\mathrm{data},I,c,\kappa}>0,\\
 \forall W\in C_c^\infty(I;\mathbb C),\\
 \mathrm{RawMoment}
 (\mathrm{data},W,c,\kappa,C_{\mathrm{data},I,c,\kappa}M_k(W)^2).
\end{gathered}
\]

The same constant works for all weights on the interval. There is no division
by a seminorm, so the zero-weight case remains valid.

## Specialization to O5 and remaining application obligations

Set `c=theta>0`, `kappa=epsilon/(2+theta)>0`, and `H=D^(1+theta)`.
For `D>=2`, the previous consequence gives a centrally normalized energy bound
with exponent `1+theta+epsilon`. **Conditional on U1**,
`P_D(W)=D^(-1/2) A_u(D)` on every nonzero-element row with the complete fixed
zero support retained. Multiplying the energy by `D` gives exactly

\[
 \sum_{0<N(u)\le D^{1+\theta}}|A_u(D)|^2
 \le C_{\nu,S,I,\theta,\varepsilon}
 M_{k(\theta,\varepsilon)}(W)^2D^{2+\theta+\varepsilon}.
\]

`k` precedes `I,W,nu,S` because `J` in the reference theorem precedes
`RowData`; those fixed-data choices affect the permitted constant. The
argument uses only `theta>0`, hence covers the stated `0<theta<=1/10` range.
It keeps the element-row multiplicity, including units, and does not quotient
the rows by the six units.

For a checked Lean crosswalk, the remaining work is concrete:

1. Package the ordinary-derivative/Schwartz-seminorm bound for logarithmic
   pullback on the **fixed** annulus, with a linear dependence on `M_k(V)`.
   Either the displayed `J+2` analytical proof or the existing `J+p` theorem
   can be used; no claim that these are already the same compiled application
   is made.
2. Construct the one smooth dyadic partition, prove its finite restriction
   and derivative bound on an arbitrary fixed `I`, and instantiate polynomial
   linearity and the `sqrt(lambda)` scale identity. The inspected raw predicate
   does not itself supply this profile-dilation identity: its
   `RawMoment.scaleEnergy` scales the amplification energy and is not a
   substitute for the required weight/column-length transport.
3. Apply the smaller capacity margin and bounded-scale source declarations
   with all positive-scale hypotheses, assemble a constant independent of
   `W`, and then connect U1's arithmetic equality to the O5 family.

No obstruction was found in the exposed predicates to this **conditional
paper-level route**. No existing declaration packaging the complete
quantifier-preserving argument was identified in the files inspected here;
that is a scoped source-search statement, not an assertion that none exists
elsewhere. Replay of a terminal zero-free theorem cannot replace these new
application obligations.
