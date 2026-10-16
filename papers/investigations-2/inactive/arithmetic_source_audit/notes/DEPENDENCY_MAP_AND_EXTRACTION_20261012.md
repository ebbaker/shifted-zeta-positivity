# Dependency map and fixed-character extraction

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed and are not inferred.
This is an internal mathematical read-through, not independent specialist
validation or formal verification.

## Source and scope

The source is the manuscript dated **5 October 2026**,
[`build/paper2.tex` at openai/math commit fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
fetched by the parent audit on 12 October 2026. The commit is dated
8 October 2026; the manuscript date and repository version are distinct.
Its SHA-256 is
`d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
All line numbers below refer to that exact TeX file; labels are supplied
to remain searchable if subsequent typesetting changes the numbering.

This note checks Sections 3–5's logical dependence, extraction, and
iteration bookkeeping. It does **not** independently establish the two
major analytic inputs, the completed mean square and the two-Poisson
transfer. Their proofs in Sections 6–7 and Appendix A remain explicit
obligations of the larger source audit. The earlier September 30
[interface audit](../../../../quasi-rh/quasi-rh-character-amplification/reviews/UPSTREAM_REFLECTION_POISSON_SIEVE_AUDIT_20261009.md)
is useful context, but is not automatically a version-matched proof of
these October 5 assertions.

**Scoped finding:** the fixed-character extraction and the displayed
finite induction are logically valid conditional on their stated family
estimates. The principal case is included, and no separate estimate for
the principal Möbius sum is used to perform the extraction. This does
not validate the family estimates themselves.

## One-page dependency map

| Stage | Exact source location | Hypotheses and output | Nature of dependence |
| --- | --- | --- | --- |
| Arithmetic coefficient class | `lem:arithmetic`, lines 795–862 | Squarefree primary columns prime to fixed `S`; `a_xi(n)=conj(alpha(n))*gamma_2(n)*xi(n)`; finite ray class containing the conductor of fixed `nu` and reciprocity factors | Source derives identities from Gauss–Jacobi identities and reciprocity; these do not give the cancellation estimate |
| Primitive Poisson and masks | `lem:poisson`, lines 875–932 | Primitive character of conductor `m`, independent exclusion ideal `r`; dual weight has argument `H*N(h)/(N(d)*N(m))`; retains principal zero mode | Derived from classical lattice Poisson and primitive Gauss-sum identities |
| Completed theta bound | `prop:R`, `eq:R`, lines 1317–1332 | `1 <= H,X,N(f) <= D^C0`, squarefree primary `f` prime to `S`; sum over all nonzero element rows of `abs(T(X;k,f))^2` is bounded by `D^epsilon norm(W)^2 (H+H^2*N(f)/X)` | Source's derived assertion, not a quoted black-box theorem; depends on its reflection and uniformity construction plus the imported quadratic large sieve |
| Actual external cancellation theorem | `lem:quadratic`, `eq:Q`, lines 1886–1913 | Squarefree row and column ideals; arbitrary complex column coefficients; quadratic twists, fixed finite reciprocity classes; bound `(H*U)^epsilon (H+U) sum abs(beta)^2` | Goldmakher–Louvel Theorem 1.1 is imported; source checks the quadratic-family interface |
| Cube removal | `lem:cube-reduction`, lines 1334–1467 | `H <= Sigma=XF`, each scale polynomial in `D`; `Hc^3=min(X,X^2/H^2)`; leaves energies with `Lb=X/N(b)^3>1` and `N(b)>Hc` | Finite Möbius inversion and Cauchy–Schwarz plus `prop:R`; no arbitrary replacement coefficient profile is allowed |
| Return transfer | `prop:transfer`, `eq:transfer-summary`, lines 1487–1508 | `max(H,LF)<=Sigma`; inputs and children in the precise `eq:energy` class, child `C^m` norm at most 1; `H'<=HL/(Sigma F)`, `H'/Sigma'<=H/Sigma`, `Sigma'<=L` | Source's derived assertion, proved by its two Poisson lemmas and smooth-weight/exclusion arguments; this is the decisive closure obligation |
| Canonical dual bound | `prop:canonical`, lines 1261–1277; proof lines 1516–1609 | Fixed positive gap `H/Sigma<=D^(-kappa)`, `Sigma<=D^C0`; gives `E << D^epsilon Sigma norm(W)^2` | Finite induction conditional on cube removal and transfer |
| Original family moment | `prop:poisson-reduction`, lines 1000–1022; `sec:completion`, lines 1613–1629 | Original row scale `H0=D^(1+theta)`; dual `Sigma=D/B`, `Hdual<=C D^(1-theta)/B^2`; gives `thm:ms` | Source's Poisson reduction and canonical bound; **not** an independent imported moment theorem |
| Fixed-character extraction | `eq:prime-extract`, lines 694–724 | Fixed finite-order Hecke `nu`, fixed `S`, smooth fixed `W`; positive family moment and many rows `p^6` | Derived inequality plus the prime ideal theorem for the fixed field |
| Continuation and Dirichlet conclusion | lines 726–770 | Bound for every fixed test `W` and every positive exponent loss; Mellin transform, Hecke continuation, base change | Standard analytic imports turn the extracted cancellation into the claimed nonvanishing conclusion |

The asserted analytic chain is therefore

\[
\text{theta automorphy + quadratic sieve}
\Longrightarrow R,\qquad
R+\text{cube inversion}+\text{two-Poisson transfer}
\Longrightarrow E\ll D^\varepsilon\Sigma
\Longrightarrow\text{original moment}
\Longrightarrow\text{fixed-character bound}.
\]

The quadratic sieve supplies the favorable completed-family bound; the
strictly decreasing transfer is required to carry it back to squarefree
columns. The exponent `11/12` arises later from extracting roughly
`H0^(1/6)` coherent rows from a moment of size `H0*D`.

## What the principal case actually uses

Fix `nu` and take `S` to contain the primes above 2 and 3 and the conductor
of `nu` (lines 665–674). There is no nonprincipal hypothesis in
`thm:ms`, lines 679–688. With `H0=D^(1+theta)` and `Y=H0^(1/6)`, the
zero-extended sextic symbol satisfies, for each prime ideal represented
by `p`,

\[
\chi_n(p^6)=\mathbf 1_{p\nmid n},\qquad
|A_1(D)-A_{p^6}(D)|\ll_W D/Y.
\]

For fixed `S`, the prime ideal theorem supplies
`J asymp Y/log Y` distinct rows `p^6` with `Y/2<N(p)<=Y`. Positivity and
the assumed moment give

\[
|A_1(D)|^2
\le {2\over J}\sum_p|A_{p^6}(D)|^2+O_W(D^2/Y^2)
\ll D^{11/6+5\vartheta/6+\varepsilon}
   +D^{5/3-\vartheta/3}.
\]

The second exponent is smaller for every allowed `theta>0`. Taking square
roots and then choosing `theta` and the moment loss sufficiently small
proves `A1(D) << D^(11/12+delta)` for any fixed `delta>0`, conditional
on `thm:ms`. This calculation also works for `nu=1`: it bounds the
principal Hecke Möbius sum directly. The coherent rows are the legitimate
extraction mechanism; their presence neither proves nor disproves the
input moment.

Four distinct uses of “principal” must not be conflated:

1. `nu=1` is the original fixed Hecke twist. It is allowed throughout.
2. `xi` indexes a finite ray family after reciprocity. Even `nu=1` can
   produce several `xi`; one cannot replace all of them by `xi=1`.
3. The primitive principal **Poisson** character has conductor 1. Its zero
   frequency is retained in `lem:poisson`, lines 908–931. In the initial
   reduction it occurs exactly for `z1=z2=1`, giving the explicit diagonal
   `Z << H0 ||W||_infinity^2` at lines 1054–1061. This diagonal is not the
   estimate for `A1`.
4. The coherent row `u=p^6` is principal on units but still has the mask
   `p does not divide n`. Dropping this mask would erase the extraction
   error and would be incorrect.

For the Mellin step, the test is allowed to depend on a hypothetical
zero `rho`: set `W(y)=y^(-rho) phi(y)`, with nonnegative nonzero
`phi` supported in `(1,2)`. Then `W_hat(rho)>0` (lines 729–733).
For any compact subset of `Re(s)>11/12`, choose the exponent loss smaller
than its distance to `11/12`; the integral defining `M_W` converges
locally uniformly. Thus it is holomorphic there. The identity

\[
L_K^S(s,\nu)\,M_W(s)=\widehat W(s)
\]

first holds for `Re(s)>1` and extends meromorphically. If `nu=1`, the
possible pole at 1 is removable in the product by this identity; a zero
of `L_K` would occur at a regular point and give a contradiction.
The omitted Euler factors are nonzero for positive real part.
Finally `L_K(s,1)=zeta(s)L(s,chi_{-3})` up to the indicated finite
factors; away from 1 the second factor has no pole that could cancel
a zeta zero. At 1 the principal factor has a pole and the quadratic
factor is nonzero by the cited Dirichlet theorem. No estimate for zeta
on a height aspect is silently inserted here.

## The decreasing parameter and uniformity contract

The canonical proposition assumes fixed `kappa>0`, `C0>=1`,
`Sigma=XF<=D^C0`, and `H/Sigma<=D^(-kappa)` (`eq:positive-gap`, lines
1261–1276). Its base case `H<=1` uses only

\[
E\ll_I HX\|W\|_\infty^2\le\Sigma\|W\|_\infty^2
\]

because `F>=1` (lines 1532–1547). A nonempty cube-tail supremum has
`H^2>X`, `N(b)>Hc`, and `Lb>1`. Assuming the transfer's stated bounds,

\[
H'\le {HL_b\over\Sigma F}
={H\over N(b)^3F^2}
<H\left({H\over\Sigma}\right)^2
\le HD^{-2\kappa},
\qquad {H'\over\Sigma'}\le D^{-\kappa},
\qquad\Sigma'\le L_b\le\Sigma.
\]

This is a genuine decreasing row scale, not a return to the same target
without progress. It also covers `Hc<1`: `N(b)>=1` still gives `Lb<=X`.
If the child range with `H'>=1` is empty, its supremum is zero. The source
inducts on `H<=D^(j*kappa)` and stops at
`j=ceil(C0/kappa)` (lines 1517–1529, 1563–1608).

The following uniformities are essential, and belong beside any use of
this induction:

- `D` is the common ambient parameter throughout the recursion. `kappa`
  stays fixed; it cannot tend to zero with `D` in this argument.
- The child must be the same arithmetic coefficient class `a_xi`,
  with the same fixed excluded-prime set and finite ray family. A moving
  prime cannot be absorbed into that fixed data without tracking its cost.
- Masks may be removed by `lem:remove-exclusions`, lines 962–991, only
  with the displayed scale change `(X,F)->(X/N(d),F*N(d))`; this preserves
  `XF`. It is not permission to delete them in a pointwise identity.
- The transfer controls every child with `||U||_(C^m)<=1` and support
  `[u/16,4v]`. Each iteration expands the fixed support interval, but
  there are only finitely many iterations. The derivative order grows
  at least by `m -> 4m+12`, and is chosen before applying the parent
  estimate (lines 1503–1508, 1530–1531, 1550–1559, 1593–1602).
- The exponent losses are budgeted in thirds in each induction step;
  constants and derivative orders may depend on the finite depth.
  There is no assertion of a single bounded derivative order for all
  positive gaps at once.
- Constants may depend on fixed `nu`, `S`, the ray group, support, and
  the exponent loss. This is sufficient for the qualitative common
  half-plane, since the exponent `11/12` is common. It does not supply
  an unstated uniform conductor or height bound for the constants.

The initial dual range has
`Hdual/Sigma << D^(-theta)` because `B>=1`; for large `D`, the source
chooses `kappa=theta/2`, `C0=2` (`eq:initial-positive-gap`, lines
1613–1628). Bounded `D`, `Hdual<1`, and `X<1` with nonempty fixed
support are treated separately by counting. No limit `theta=0` is
taken inside the canonical proposition.

## Remaining decision

There is no extraction or formal induction obstruction in this scoped
read-through. Before treating the claimed fixed-character result as
established, verify the full quantitative `prop:R` and `prop:transfer`
interfaces on the pinned version: the selected nonempty branch must
retain primitive conductors, masks, squarefree restrictions, coefficient
norms, support and derivative costs, and coherent/zero contributions,
then return to `eq:energy` with **all three** transfer scale inequalities.
If that closure fails, the downstream chain remains conditional even
though the extraction calculation is correct. A successful single
branch also leaves the other branches and analytic imports to audit.
