# The De Bruijn–Newman flow is a straight line on Calogero–Moser space

**Draft note. 2026-08-25.** Status: the central identity turns out to be George Wilson's
tau-function formula for rational KP solutions, read in an unfamiliar variable. What remains
plausibly new is the framing: the De Bruijn–Newman constant of a real polynomial is the
real-spectrum threshold of a linear matrix pencil on Calogero–Moser space, and the backward heat
flow that defines it is the second KP flow. This note states the dictionary, gives a self-contained
proof, and fixes the attributions. It should be positioned as a short expository bridge — integrable
systems ↔ the De Bruijn–Newman circle — with one new corollary, not as a new identity.

---

## 1. Statement

Let `p` be a monic polynomial of degree `n` with distinct roots `z_1, …, z_n ∈ ℂ`. Define the
**Calogero–Moser pair**

`X = diag(z_1, …, z_n)`,  `Y_{jk} = 2/(z_j − z_k)` for `j ≠ k`,  `Y_{jj} = Σ_{k≠j} 2/(z_j − z_k)`.

Then `[X, Y] + 2I = 2J` where `J` is the all-ones matrix; in particular `rank([X,Y] + 2I) = 1`,
so `(X, −Y/2)` is a point of the (complex) Calogero–Moser space `𝒞_n` in the normalisation
`rank([X,Z] − I) = 1`.

> **Theorem.** For all `t ∈ ℂ`,  `(e^{−t∂_z²} p)(z) = det(zI − X − tY)`.

Here `e^{−t∂²}` is the (terminating) heat semigroup on polynomials,
`e^{−t∂²} z^m = Σ_j (−t)^j m!/(j!(m−2j)!) · z^{m−2j} · (m−2j)!/(m−2j)!`… i.e. the standard
coefficient action; `t > 0` smooths (drives roots together onto the real axis for real data),
`t < 0` sharpens.

**Corollary 1 (DBN constant as a spectral threshold).** For real `p`, the De Bruijn–Newman
constant satisfies

> `Λ(p) = inf { t : spec(X + sY) ⊂ ℝ for all s ≥ t }`,

and by the classical monotonicity of hyperbolicity under the heat flow this equals
`inf { t : spec(X + tY) ⊂ ℝ }`. The De Bruijn–Newman flow — the object at the centre of
Newman's conjecture and the Rodgers–Tao theorem — is the **straight line** `X + tY` in `𝒞_n`.

**Corollary 2 (hyperbolicity as reality of a pencil spectrum).** `p` is hyperbolic iff the
non-normal matrix `X` (equivalently `X + tY` at `t = 0`) has real spectrum — trivially — but the
pencil upgrades this to a quantitative statement: the local margin of hyperbolicity is the
backward collision time of the pencil spectrum, computable by bisection on one eigendecomposition
per step. The positive-definite `H` with `HX` Hermitian, whose existence is equivalent to
hyperbolicity, is the Hermite/Bezoutian form; the pencil does not evade Hilbert–Pólya, it
furnishes it.

## 2. Proof

Both sides are monic degree-`n` polynomials in `z` whose coefficients are polynomials in `t`, so
it suffices to prove equality for `t` in a real neighbourhood of `0` (for generic data; the
degenerate cases follow by continuity).

*Left side.* Write `H_t = e^{−t∂²}p`, so `∂_t H = −∂_z² H`. Implicit differentiation at a simple
root `z_j(t)` gives `ż_j = H''(z_j)/H'(z_j)`, and partial fractions of `H'/H` at a simple root give
`H''(z_j)/H'(z_j) = Σ_{k≠j} 2/(z_j − z_k)`. Hence the roots satisfy the first-order system

`ż_j = Σ_{k≠j} 2/(z_j − z_k)`  (∗)

and, differentiating (∗) along itself, the second-order rational Calogero–Moser system

`z̈_j = −8 Σ_{k≠j} (z_j − z_k)^{−3}`.  (∗∗)

(The cross terms cancel pairwise; this is the classical computation, cf. Rodgers–Tao, Thm 11.)

*Right side.* By the projection method for rational CM (Airault–McKean–Moser; Kazhdan–Kostant–
Sternberg; Moser), if `[X,Y] + 2I` has rank one then the eigenvalues `λ_j(t)` of `X + tY` solve
(∗∗). Their initial values are `λ_j(0) = z_j`, and the standard first-order perturbation formula
gives `λ̇_j(0) = (Y)_{jj}` in the eigenbasis of `X` — which is exactly the right side of (∗) at
`t = 0`. (Note the pencil trajectory satisfies (∗) only at `t = 0`; it is the *second-order* system
that both trajectories share, with matching initial position and velocity.)

*Conclusion.* Two solutions of the same nonsingular second-order ODE system with identical initial
position and velocity coincide until the first collision; on that interval the two monic
polynomials have the same roots, hence are equal; and two polynomials in `(z, t)` that agree on an
open `t`-interval agree identically. ∎

## 3. Attribution and relation to known work

1. **The identity is Wilson's tau-function formula.** For a Calogero–Moser pair normalised as
   `rank([X,Z] − I) = 1`, the tau function of the associated rational KP solution is
   `τ_𝒳(t_1, t_2) = det(t_1 I + 2 t_2 Z − X)` — see G. Wilson, *Collisions of Calogero–Moser
   particles and the adelic Grassmannian*, Invent. Math. 133 (1998), and, stated in exactly this
   determinantal form, Kasman–Milson–Gekhtman, *Orthogonality with respect to the Hermite product,
   KP wave functions, and the bispectral involution*, SIGMA (2026), §6.3 ("the usual τ-function
   associated to 𝒳 ∈ CM_N is (cf. [Wilson]) τ_𝒳(x,y) = det(xI + 2yZ − X)"). With `Z = −Y/2`,
   `t_1 = z`, `t_2 = t`, this is the Theorem: **the heat flow is the second KP time on polynomial
   tau functions**, which is itself classical. Round 2's guess that the identity was "unsurprising
   but unstated" was half right: it is stated, in the integrable-systems dialect.
2. **The expectation version** is finite free probability: `E_G det(zI − A − G_t)` over a suitable
   Gaussian ensemble equals the heat-flowed characteristic polynomial (Marcus–Spielman–Srivastava,
   arXiv:1504.00350). The Theorem is its exact derandomisation — the CM matrix `Y` is the
   deterministic representative that the expectation happens to equal.
3. **The root ODE** (∗) in the DBN context is Rodgers–Tao (arXiv:1801.05914, Thm 11); as pole
   dynamics of rational solutions of Burgers/KP it goes back to Airault–McKean–Moser (1977) and
   Choquard-era literature.
4. **What appears new** is only the two corollaries' framing: `Λ(p)` as the real-spectrum threshold
   of the linear pencil, and the observation that the De Bruijn–Newman flow — including the flow
   Polymath15 pushed quantitatively — is a straight line on the same Calogero–Moser space that
   appears as the noncommutative-instanton moduli space in the RH3 project's Rounds 1–2. Whether
   this earns a standalone note or a remark in the detector paper is a judgement call; the honest
   default is the latter.

## 4. Numerical certificates (Round 3, independent)

Identity verified to relative coefficient error `≤ 2.8e−10` (conditioning-limited; `1.2e−15` at
`n = 2`) across `n = 2…7`, real and conjugate-pair data, four times each; rank-one condition to
`2e−15`; `Λ(z² + y_0²) = y_0²/2` exact via the pencil; five nontrivial `k = 2` configurations
matched to 5 digits against direct root tracking; Hermite benchmark `Λ(normalised H_d) =
−1/(2(d−1))` confirmed. Scripts: `v1_pencil.py`, `v2_spot.py` in the Round-3 bundle.
