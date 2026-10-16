# The exclusion map: what has been ruled out, by what argument, with what scope

**Author: Claude Opus 5 (Anthropic), 17 September 2026.** Written at the
investigator's request as a synthesis of the exclusions this investigation has
accumulated, organised by the *kind* of argument rather than by the order in
which they were found, and with each scope clause made explicit — the purpose
being to see where the loopholes are. Sections 1, 2, 4, 5, 6 and 7 restate
results already in the notes and in working manuscript 0.6 and claim nothing
new. The one piece of new mathematics is the observation of section 3.3, which
is elementary and is labelled where it occurs. No check programme is added and
no manuscript change is proposed here.

## 0. The map

| # | What is excluded | Where | Argument | Status | Scope clause |
|---|---|---|---|---|---|
| 1 | A further positive channel, adjoined orthogonally, supplying `R_L` | Prop 7.3 | Positivity on a codimension-two subspace | Proof | Only summands `\|Sf\|^2` adjoined to the rest |
| 2 | The gamma-channel/prime-channel architecture | Lemma 7.4, Thm 7.5 | Hilbert-space algebra + explicit certificates | Proof at `L = 1`, `5/4`, large `L` | Only the specific pair `(K, sum_p B_p)` |
| 3 | The same pair with constants and pole shares moved into the channels | Exclusion note, sec. 5 | `alpha`-scan of the same bound | **Numerical only** | Floor at `5e-8` is discretisation |
| 4 | Coherent gluing with fixed output vectors | Prop 7.2 | Kernel support: an atom at `log(3/2)` | Proof | Operator-valued junctions cancelling mixed returns identically |
| 5 | The first-prime resolvent source, contact and poles adjustable | Gauge note, sec. 5 | Kernel cusp at `x - y = d` | Proof (local) | Finite positive sums of mode branches only |
| 6 | Arithmetic coordinate as Euclidean preparation time | Gauge note, sec. 2 | `x + y` versus `x - y` | Proof | Spatial, nonlinear, normalised or extended preparations |
| 7 | Finite rational feedback on one reference operator | Analysis note, sec. 3 | Sum of squares cannot equal `z - alpha` | Proof | Nonrational response, couplings not functions of `T`, infinite families |
| 8 | Bounded sources `f -> int f(x) U_x Omega dx` | Sphere note, sec. 5.1 | `Q_L[chi e^{iNx}]/log N -> \|chi\|^2` | Proof | A selection rule; distributional sources are required, not forbidden |
| 9 | One `q` serving every negative magnetic power at every prime | Prop 7.1 | `l^2` criterion plus `2^a != 3^b` | Proof (formal coefficients) | Finite words are unaffected |
| 10 | Connes-Consani as a tool for (8.1) | Sec. 8.1 | Their hypothesis is exactly `P_L = 0` | Proof | Retained as a precedent for the *mechanism* |
| — | *Withdrawn:* the ghost pair | v0.4 sec. 8.2 | Conflicts with Cor. 2.2 | Struck in 0.5 | See section 6 |
| — | *Withdrawn:* the mirror weight is unreachable | Rem. 7.10 of 0.4 | A fourth route exists | Settled in 0.5 | See section 6 |

## 1. The two facts that power almost all of it

**(a) The target is minuscule compared with its own terms.** By the explicit
formula `Q_L[f] = sum_rho F^(gamma_rho) conj(F^(conj gamma_rho))`. On `I_4`
with a smooth input the four terms of (2.9) are `3.40`, `-8.06`, `9.11`,
`-4.46` and the sum is `1.4e-7`. Every argument of the form "these pieces
cannot be assembled" is drawing on that ratio: the assembly must be correct to
seven digits at every test function, not on average.

**(b) Rigidity (Corollary 2.2).** If `\|Phi(f)\|^2 = Q_L[f]` for all `f`
supported in `I_L`, then RH holds and `Phi` is unitarily equivalent to
`f -> (F^(gamma_rho))_rho` in `l^2` of the zero multiset. The Hilbert space and
the source are not free data. This is what allows structures to be excluded
rather than merely not found — and, in the one case where the tool was used
carelessly, it is also what refuted an exclusion of our own (section 6).

## 2. Family A — a positive object cannot be a negative one

**No orthogonal augmentation (Prop. 7.3).** `P_L` is rank two. On the
codimension-two subspace where both pole moments vanish, `R_L` is `c \|f\|^2`
with `c < 0`. A norm is not negative on a subspace. Airtight, and narrow: it
speaks about a summand `\|Sf\|^2` *adjoined* to the others.

Worth restating, because the proposition is routinely misread: the obstruction
here is carried by the **negative contact**, not by the poles. The pole-term
note makes this explicit, and it is why the poles turned out not to need a
mechanism.

**Rational feedback (Analysis note, sec. 3).** The same theme one level up. With
channels `A_0 r_j(T)` and `s_l(T)`, rational in one reference operator,
evaluation on eigenvectors gives
`lambda sum_j |r_j|^2 + sum_l |s_l|^2 = lambda - alpha`. The left side extends
to a rational `R(z)` with a sum-of-squares representation, hence `R(x) >= 0` at
real `x` off its poles, while `x - alpha < 0` for `0 < x < alpha`. So finitely
many rational filters of a single reference operator cannot manufacture an exact
negative constant. Outside it: nonrational response functions, couplings that
are not functions of `T`, infinite channel families, agreement on only finitely
many inputs.

## 3. Family B — the interference bound, and exactly what it says

### 3.1 The bound

Two lines of Hilbert-space algebra, no arithmetic and no physics:

```
 t A[f] + t^{-1} B[f] + C[f] = || sqrt(t) G f + t^{-1/2} S f ||^2 >= 0   (t > 0).
```

At `t = 1` this is only positivity of the total. Every other `t` is strictly
stronger. The form to keep in mind is

```
 | sqrt(A[f]) - sqrt(B[f]) |  <=  sqrt(Q_L[f])   for every f,
```

or, multiplying through by `sqrt A + sqrt B`, the equivalent linear form

```
 | A[f] - B[f] |  <=  sqrt(Q_L[f]) ( sqrt(A[f]) + sqrt(B[f]) ).      (*)
```

Combined with fact 1(a) this says the two channel norms must be **nearly
identical forms**. At `L = 5/4`, `f = 1_{I_L}`: `A = 4.302142`,
`B = 7.197439`, so `|sqrt A - sqrt B| = 0.6086` against
`sqrt(Q_L[f]) = 0.2776`. It fails by a factor of `2.2`, and at large `L` by a
factor tending to infinity, `2 sqrt(AB) = O(L^{1/2} e^{L/4})` against
`-R_L ~ 4(L-2) e^{L/2}`.

### 3.2 The one soft spot in the exclusion chain

The natural repair — let each channel carry a constant and a share of the pole
term — is ruled out **numerically only**, by the `alpha`-scan of section 5 of
the exclusion note, whose best values decay like `1/alpha` down to a floor of
`5e-8` that is the discretisation. The mechanism is clear
(`D[f]^2 / (4 alpha) <= Q_L[f]` with `D = A' - B'` fixed) but making it a
theorem needs a rigorous lower bound on `lambda_min(Q_L)` against `D`. That is
loose end 1 of the exclusion note and it is the only place in the chain where
"ruled out" means "strong numerical evidence".

Note also what that scan did *not* vary: `A' = K + alpha\|f\|^2 + sigma P_L`
moves constants and pole shares between the channels, but never an operator
share of the gamma energy or of the prime references. The family
`A' = K - M`, `B' = sum_p B_p + M` for a positive form `M` is untested, and by
(*) it is exactly the family the bound is least able to touch.

### 3.3 Observation: the bound does not exclude two channels, only *these* two

*New in this note; elementary, and abstract-existence only.*

Take `M = (K - sum_p B_p)/2`, i.e. the symmetric split

```
 A'[f] = B'[f] = P[f] := ( K[E_L f] + sum_p B_p[E_L f] ) / 2,
 C'[f] = R_L[f].
```

Then (*) is satisfied with its left side identically zero. More than that, the
split is abstractly realisable:

> **Observation.** Suppose `Q_L >= 0` on `C_c^infty(I_L)` and `-R_L >= 0` there.
> Then there are complex-linear maps `G, S` from `C_c^infty(I_L)` into a common
> Hilbert space with `\|Gf\|^2 = \|Sf\|^2 = P[f]` and `\|(G + S)f\|^2 = Q_L[f]`.

*Proof.* Put `X = R_L/2`, a Hermitian form, and let `M` be the form on
`V (+) V` with diagonal blocks `P` and off-diagonal block `X`. The identity
`P[f] + P[g] + 2 Re X(f,g) = ( (P+X)[f+g] + (P-X)[f-g] ) / 2` shows `M >= 0`
as soon as `P + X >= 0` and `P - X >= 0`. Here `P + X = Q_L/2 >= 0` by
hypothesis and `P - X = (K + sum_p B_p - R_L)/2 >= 0` since the first two terms
are positive forms and `-R_L >= 0`. A positive form has a Gram representation
`M(.,.) = <Psi(.), Psi(.)>`; set `Gf = Psi(f,0)` and `Sf = Psi(0,f)`. Then
`\|Gf\|^2 = \|Sf\|^2 = P[f]`, `2 Re <Gf,Sf> = R_L[f]`, and the three add to
`Q_L[f]`. QED

The side hypothesis is cheap. By Cauchy-Schwarz,
`P_L[f] <= 2\|cosh(x/2)\|^2 \|f\|^2 = (L + 2 sinh(L/2))\|f\|^2`, so `-R_L >= 0`
whenever

```
 sum_{p < e^L} kappa_p - w_0  >=  L + 2 sinh(L/2),      kappa_{r,d} = 2dr/(1-r).
```

Floating-point evaluation of the two sides (not a registered check programme):

```
   L     sum kappa_p    |c| = sum kappa - w0    L + 2 sinh(L/2)    margin
  0.3        0.000            5.372                 0.601           4.77
  log 2      0.000            5.372                 1.400           3.97
  1.0        3.347            8.719                 2.042           6.68
  1.25       6.348           11.721                 2.583           9.14
  2.0       11.317           16.689                 4.350          12.34
  3.0       18.924           24.296                 7.259          17.04
  5.0       49.243           54.615                17.100          37.51
  8.0      222.641          228.013                62.580         165.43
 12.0     1621.104         1626.476               415.426        1211.05
```

The margin never comes close to zero, and asymptotically the left side is
`4 e^{L/2}(1 + o(1))` against a right side `e^{L/2} + L`; the partial-summation
bound already recorded for Proposition 8.1 covers the tail. I have not written
the right-endpoint argument out as a proof.

**What the observation is worth.** Nothing arithmetic: it uses `Q_L >= 0`,
which is RH on `I_L`, and produces an abstract Gram space, exactly as
Corollary 2.2 does. Its content is entirely about scope. Theorem 7.5 cannot be
strengthened to "no two-channel architecture": a two-channel architecture
exists the moment Weil positivity holds. What is excluded is a two-channel
architecture whose channels **segregate** the archimedean from the arithmetic
data, and (*) says why — the channels have to agree to within `sqrt(Q_L)`,
so each one must carry roughly half of everything, primes and gamma together.
That is the same conclusion the jump-form presentation of Section 7.7 reaches
from the other direction, where a single Levy measure carries the archimedean
density as its continuous part and the primes as its atoms.

## 4. Family C — kernel support and atoms

These are the sharpest arguments in the investigation, because they compare
distribution kernels rather than numbers, and numbers are where the cancellation
hides.

**Mixed returns (Prop. 7.2).** A coherent sum with *fixed* output vectors
`v_2, v_3` produces a cross term with an atom at `log(3/2)` of mass
`sqrt(c_2 c_3)(1-r_2)(1-r_3) <v_2,v_3>`. The Weil kernel has atoms only at
`{m log p}`; its gamma and pole kernels are smooth off the diagonal and its
contact sits at zero, so nothing can cancel it. Hence `v_2 _|_ v_3`, which
returns the separate positive references and hands the problem to Theorem 7.5.
The only number theory used is that `3^{n-1} = 2^{m-1}` forces `n = m = 1`.
**Outside it:** an operator-valued junction with further terms cancelling mixed
returns *as an identity*. The note is explicit that a failed fixed-vector ansatz
gives no licence to treat unwanted atoms as a small residual.

**The cusp mismatch (Gauge note, sec. 5).** The first-prime resolvent source has
a nonzero derivative jump at `x - y = d`, where the target — after the matched
delta is removed — is smooth. Finite positive sums of mode branches all have
jumps of the same sign and cannot cancel. Local, and needs no operator norm.
**Outside it:** coherent couplings between outputs; section 6 of that note then
shows the cusp *can* be cancelled coherently, which is what pushed the
investigation toward interference in the first place.

**`x + y` versus `x - y` (Gauge note, sec. 2).** A preparation
`Phi_L(f) = int f(x) e^{-(b+x)H} eta dx` has kernel `C(2b + x + y)`, a function
of `x + y`; the Weil kernel depends on `x - y`. Invariance under simultaneous
translation would force `C'` to vanish on an interval, hence `eta` into the
zero-energy subspace and the kernel to be constant. **Outside it:** spatial,
nonlinear, normalised or extended preparations.

## 5. Family D — domains and boundedness

**Higher magnetic powers (Prop. 7.1).** The formal output of `u_-^k` has an
`l^2` coefficient sequence iff `a < q^k` or `a in {q, q^3, ...}`. For the prime
states `a_p = q p^{-1/2}`, surviving every negative power would force
`p^{-1/2} = q^{2 j_p}`, impossible for `2` and `3` at once. **Outside it:** any
fixed finite word — choose `q^{K-1} > 2^{-1/2}` and every prime state is in the
strictly decaying regime through power `K`. A field theory need not put every
state in the domain of every unbounded power. This restricts junction words, not
the programme.

**The source must be unbounded (Sphere note, sec. 5.1).**
`Q_L[chi e^{iNx}]/log N -> \|chi\|^2`, from `b(tau^2) ~ log|tau|`. Any
preparation `f -> int f(x) U_x Omega dx` with `U_x` unitary and `Omega` of finite
norm is bounded on `L^2(I_L)` and therefore cannot realise `Q_L`. This is the
single explanation of several unrelated-looking earlier failures, and it is a
selection rule rather than a no-go: local fields are distributions.

## 6. The two withdrawn exclusions, and the transferable lesson

**The ghost pair.** Version 0.4 argued: `P_L` is hyperbolic of signature `(1,1)`
with the two pole evaluations as null lines, therefore a realization must contain
a null pair — a BRST doublet or an indefinite-metric sector. The refutation is
fact 1(b). Lemma 2.3 is a statement about the *form* `P_L` on test functions; a
realization realizes `Q_L`, in a positive `l^2` with no null vectors, and the two
poles are not vectors of that space at all — they are the two points the
functional equation adds to the zero set. What survived is the involution of
Proposition 2.4, a genuine and cheap necessary condition, together with the
parity split, which bounds the whole negative direction by
`2(sinh(L/2) - L/2) = 0.042` at `L = 1`; below `log 2` the binding direction of
the form is *even*, where the pole term is positive.

The lesson generalises, and is the one I would carry into any new direction:
**an exclusion about a decomposition was silently upgraded into an exclusion
about a realization.** Propositions 7.3 and Theorem 7.5 are both statements
about channels. Neither constrains a source that never isolates the pieces.
Anything that begins "a realization must therefore contain" deserves to be
checked against Corollary 2.2 before it is believed.

**Remark 7.10.** The mirror weight was thought unreachable, with three routes
blocked. A fourth works, and in fact every state analytic past the unit circle
is reachable. Note where the loophole sat: all three blocked routes acted on the
*output* after the fact; the working route acted on the dressing's zeros and
poles at radius `q^{-1}`, one level down in the construction. The consequence is
deflationary rather than enabling — producing a prime weight in a positive sector
is a statement about the dressing chosen, not about the representation, and
should no longer count as evidence for a candidate.

## 7. Connes-Consani: excluded as a tool, retained as a mechanism

Their functional is the archimedean local term with the two pole contributions
removed, and their hypothesis `g^(i/2) = 0` is, by Lemma 2.3, exactly the
statement that the source vector lies on a null line of the hyperbolic pole
pairing — that is, `P_L = 0`, which a norm on all of `C_c^infty(I_L)` cannot
discard. So it is not a tool for (8.1). It remains the precedent for the shape
of the mechanism: a negative contact relative to a positive reference arising as
`\|(1 - Pi)v\|^2`, never as an added channel.

## 8. What is not excluded

1. **Compressions and differences.** Lemma 7.4 bounds the norm of a *sum*.
   Nothing above constrains `\|Gf\|^2 - \|Pi G f\|^2`.
2. **Sources that never separate archimedean from arithmetic data**, the jump
   form among them. Section 3.3 says the interference bound positively
   recommends this.
3. **Two channels each carrying half of everything.** Permitted by (*),
   abstractly realisable by section 3.3, and not scanned.
4. **Operator-valued junctions cancelling mixed returns identically.**
   Explicitly outside Proposition 7.2.
5. **Unbounded and distributional sources**, and infinite insertion families.
   Required by section 5, not forbidden.
6. **Nonrational response functions and couplings that are not functions of the
   reference operator.** Outside the rational-feedback proposition.
7. **Every actual theory.** None of these arguments touches sphere
   quantization, Schur quantization, Yang-Mills or any protected sector. They
   are all bookkeeping about forms.

The one structural fact that is not a loophole and will not become one:
`\|Pi\|` is saturated. Any mechanism yielding a uniform strict contraction, or
any hypothesis supplying a margin uniform in `L`, is producing a false
statement. The least generalized eigenvalue is at most `6.4e-10` at `L = 1` and
`1.2e-24` at `L = 3`, and the near-null count grows with `L`.

## 9. Status of each claim in this note

- Sections 1, 2, 4, 5, 6, 7 and the table of section 0 are **restatements**;
  their proofs are in the cited notes and in manuscript 0.6, unchanged.
- The rearrangement (*) in section 3.1 is **elementary algebra** from
  Lemma 7.4.
- The Observation of section 3.3 is a **written proof**, conditional on
  `Q_L >= 0` and `-R_L >= 0`. Its first hypothesis is RH on `I_L`; it therefore
  establishes nothing arithmetic and is a scope statement about Theorem 7.5
  only.
- The Cauchy-Schwarz criterion for `-R_L >= 0` is a **written proof**; the table
  verifying it is **labelled floating point**, computed outside the repository
  and not a registered check programme. The right-endpoint argument covering all
  `L` is not written out.
- The numbers quoted from the existing record — the `L = 5/4` certificate, the
  saturation values, the Galerkin tables — are reproduced, not re-derived, and
  carry the status recorded where they were first stated: one-sided subspace
  values certify failure above the threshold and nothing below it.
