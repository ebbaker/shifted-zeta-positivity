# Fixed point theorems, and the margin any existence argument must forgo

**Author: Claude Opus 5 (Anthropic).** 16 September 2026. Written in answer to a
direct question: could a generalized fixed point theorem give existence? It
corrects an overstatement in
[the q-Weyl note](QWEYL_TRACE_SPACE_20260916.md), §1, and adds a measurement
that bears on every method, not only this one.

## 1. The correction I owe

The q-Weyl note said that non-constructive existence "is exactly RH and cannot
be shortcut", and treated that as closing the question. Two things are wrong
with how that was put.

First, "an existence proof would be a proof of RH" is not an objection. It is
the **goal**. The programme's stated target (Proposition 3.2) is precisely an
implication ending in RH. Calling that circular confuses "this argument assumes
what it proves" with "this argument proves what we want".

Second, what is actually circular is much narrower than what I wrote:

> An argument whose **only** input is `||Pi|| <= 1` returns its input, because
> `||Pi|| <= 1` is the Weil criterion and Corollary 7.9's dilation is available
> the moment it holds.

A fixed point theorem is not an argument of that kind. It takes *structure* as
input — a complete metric and a contraction, a compact convex set and a
continuous self-map, a complete lattice and a monotone map — and returns an
object. If the structure comes from the model rather than from the target's
positivity, nothing is circular. So fixed point theorems are **not** excluded by
anything in the previous note.

What follows is what they would need here, which of them are blocked, and by
what.

## 2. The problem is membership, not existence

This is the first thing to be clear about, because it decides which theorems are
even the right shape.

A fixed point theorem answers: *does this equation have a solution?* It is for
underdetermined or implicitly defined objects. But here:

- The source is **not** underdetermined. By Corollary 2.2 a realization
  compatible in `L` is, up to one unitary, the evaluation map on the zeros. There
  is nothing to search for.
- The contraction is **not** implicitly defined. `<Gf, Pi Gg> = T_L(f,g)` defines
  `Pi` by a formula on the range of `G`; the only question is whether
  `||Pi|| <= 1`.

So the question is not "does an object satisfying these equations exist" but
"does this *determined* object lie in that model's positive cone". That is a
**membership** question, and the canonical non-constructive tools for membership
are separation and duality — Hahn-Banach, Farkas, a Positivstellensatz,
moment-problem duality — not fixed points. The dual formulation is worth writing
down for its own sake:

> `Q_L >= 0` fails if and only if there is a separating functional. So RH is
> equivalent to the **non-existence** of a dual certificate.

Non-existence statements can be proved by invariants, which is what the
selection rules are. That is a different and, I think, better-matched line than
fixed points — but it is not an argument that fixed points cannot be made to fit,
and §3 is about how they could.

## 3. What each family of fixed point theorem would need

### Banach (strict contraction on a complete metric space)

Gives a unique fixed point with a rate. To use it one needs an iteration whose
fixed point is the source or the model parameter that produces it. The natural
candidate is the **infinite-prime limit**: the map that adjoins one more local
factor to a positive pairing. A contraction estimate for that map in a suitable
metric would give both convergence and existence, and would settle the open half
of selection rule 6.

The obstruction is concrete and quantitative: that map is not contracting in any
obvious metric, because the contacts it adds diverge,
`sum_{p < X} kappa_p ~ 4 sqrt(X)`. Any metric in which it contracts has to see
the cancellation of that divergence against the archimedean growth, which is the
whole problem.

### Schauder, Ky Fan, Kakutani (continuous self-map of a compact convex set)

This is the family with the most going for it, and the reason is new: **the
classifications supply the compact convex sets.** Klyuev's Theorem 4.7 gives the
cone of positive definite equivariant traces as `C_l x R^r_{>0}`, and EKRS give
uniqueness outright for small Kleinian singularities. Before that work there was
no description of the set a fixed point theorem would live on; now there is.

Two obstructions, one soft and one hard.

*Soft, but decisive in practice:* the matching conditions are **linear** on the
trace — they prescribe values of `T` on specified elements. A linear feasibility
problem over a convex body is decided by separation, not by a fixed point; the
fixed point theorems that do apply to it are the nonexpansive ones (alternating
projections, Krasnoselskii-Mann), whose theory says exactly that the iterates
converge when the intersection is nonempty and otherwise produce a **gap vector
which is the separating certificate**. That is a genuine formulation and it is
implementable in finite truncations. But the two sets touch *tangentially* — the
answer is on the boundary of the cone, see §5 — so there is no linear regularity
and the convergence rate degenerates. It is a formulation, not a decision
procedure.

*Hard:* the self-map property. Verifying that a map sends the cone into itself is
normally done by exhibiting a margin, and §5 says the available margin collapses
with `L`.

### Knaster-Tarski (monotone map on a complete lattice)

Blocked at the operator level, and it is worth recording why, because it is a
clean structural fact rather than a difficulty. By **Kadison's antilattice
theorem** the self-adjoint part of a C*-algebra is an anti-lattice: two
self-adjoint elements have a least upper bound only when they are comparable.
So the operator interval `[0, K_+]`, which is where `Pi` lives, is not a
lattice, and order-theoretic fixed point theorems do not apply to it.

On the *trace* cone the situation is different and depends on the algebra. A
simplicial cone `R^r_{>0}` is a lattice, so for an algebra with `l = 0` in
Klyuev's Theorem 4.7 monotone methods are available. The algebra of Section 6.1
has `l = 1` and `r = 0` (see [the q-Weyl note](QWEYL_TRACE_SPACE_20260916.md)),
so they are not available there.

### The renormalization group fixed point

This is the reading a physicist reaches for first, and it is cleanly excluded by
scale. Any RG fixed point is scale invariant. The Weil form fixes an **absolute**
scale twice over: the dilation `x -> lambda x` sends the prime translations
`log p -> lambda log p`, destroying every atom, and shifts the density symbol
`log(tau/2pi) -> log(tau/2pi lambda)`. So no source for `Q_L` sits at a
scale-invariant fixed point of an RG flow.

It may of course sit on a trajectory, which is the picture of Section 5.3 — and
Section 5.3 already notes that an isometric RG description transports a source
without repairing a mismatch. So the RG gives transport, not existence.

## 4. Summary of the four

| Theorem | Needs | Status here |
|---|---|---|
| Banach | complete metric, strict contraction | open; the natural map has divergent contacts |
| Schauder / Ky Fan | compact convex set, continuous self-map | **the set now exists** (Klyuev, EKRS); the self-map is the problem, and the conditions are linear so separation fits better |
| Knaster-Tarski | complete lattice, monotone map | blocked on operators (Kadison antilattice); available on simplicial trace cones, which Section 6.1's algebra is not |
| RG fixed point | scale invariance | excluded: the primes fix an absolute scale |

## 5. The margin, measured

Whatever the method, it produces an object with `||Pi_L|| = 1 - lambda_min(L)`,
and any hypothesis that supplies a margin **uniform in `L`** proves something
false. So the size of `lambda_min(L)` is a constraint on every method, and it was
worth measuring properly.

Every Rayleigh quotient is an upper bound on `lambda_min(Q_L; K_+)`, so a
well-adapted trial space gives a better bound than a coarse one. Two things make
the measurement delicate and both can be removed:

- **Cancellation.** Assembling `Q_L` from (2.9) cancels terms of size 10 down to
  the size of the answer. In double precision the assembled matrix is wrong by
  more than its own entries: for `L = 1` in a five-dimensional smooth basis the
  direct assembly and the spectral assembly differ by `1.6e-6` while the entries
  themselves are of order `1e-7`. This is the manuscript's own warning
  (Section 2.4) made lethal.
- **The trial space.** Indicator cells are badly adapted, because their
  transforms decay like `1/tau` and so cannot avoid `gamma_1`.

Both are removed by building `Q_L` from its **spectral** form,
`Q_L[f] = sum_rho |F^(gamma_rho)|^2` (Corollary 2.2), which is a sum of positive
terms with no cancellation at all, in the smooth basis
`phi_k(x) = (1 - (2x/L)^2)^k`, whose transform is the spherical Bessel function
`phi^_k(tau) = (L/2) sqrt(pi) Gamma(k+1) (2/z)^{k+1/2} J_{k+1/2}(z)`, `z = tau L/2`
(verified against direct quadrature to 30 digits). With 80 zero ordinates and 50
digits:

| `L` | `K = 4` | `K = 8` | `K = 12` | `K = 16` |
|---|---|---|---|---|
| 1.0 | 6.20e-7 | **1.91e-7** | 6.43e-10 | 1.62e-16 |
| 1.5 | 3.21e-8 | 1.39e-11 | 2.50e-14 | 7.22e-16 |
| 2.0 | 4.07e-9 | 2.18e-13 | 1.72e-17 | 1.08e-21 |
| 3.0 | 1.85e-11 | 6.51e-17 | 1.24e-24 | 4.14e-25 |

Truncating the zero sum only ever *lowers* these numbers, so each is an
underestimate; a sensitivity run over 20, 40, 60 and 80 ordinates shows the
`K = 12` column roughly converged (`L = 1`: 5.1e-11, 3.9e-10, 5.6e-10, 6.4e-10)
while the `K = 16` column is still rising and should be read only as an order of
magnitude.

**Defensible reading.** `lambda_min(L) <~ 1e-9` at `L = 1`, `2.5e-14` at
`L = 1.5`, `1.7e-17` at `L = 2`, `1.2e-24` at `L = 3`. The margin does not merely
shrink; it collapses superexponentially in `L`.

### Consequence for any existence argument

> **Rule.** A hypothesis providing a margin uniform in `L` — a self-map into a
> fixed compact subset of the cone's interior, a contraction ratio bounded away
> from one uniformly, a spectral gap — proves something false. The margin must
> degrade at least as fast as the table above.

Schauder is safe on this count, since it asks for no margin; it simply gives no
control on where in the set the fixed point sits, which is the whole question
here. Banach is the one to be suspicious of.

### And a correction to the sibling manuscript

Section 7.6 of manuscript 0.5 states that the largest generalized eigenvalue of
`(T_L, K_+)` is `1 - 1.9e-7` at `L = 1` and `1` to within `1e-15` at
`L = 3/2, 2, 3`, attributing this to "a Fourier-Galerkin space of 41 modes". Three
observations:

1. The investigation's own registered programme,
   `numerics/check_gamma_compression.py`, uses **40 indicator cells**, not 41
   Fourier modes, and reports `lambda_min = 5.51e-4, 4.12e-4, 3.67e-4, 3.01e-4`
   at `L = 1, 3/2, 2, 3`. The manuscript's figures are therefore **not
   reproduced by the check registered against them**, by three orders of
   magnitude.
2. The value `1.9e-7` at `L = 1` *is* reproducible — it is the `K = 8` entry
   above, to two digits. So the figure is real and comes from a small smooth
   space, not from the cell computation in the repository.
3. The claim "`1` to within `1e-15`" is, if anything, far too weak: the true
   values are near `1e-17` at `L = 2` and `1e-24` at `L = 3`.

So the manuscript's qualitative conclusion is right and understated, while its
quantitative claims are attached to a computation that does not produce them.
Both should be fixed, and the fix strengthens the argument.

## 6. What I would actually try

1. **The dual side.** RH on `I_L` is the non-existence of a separating
   functional. Selection rules are non-existence proofs by invariant. This is the
   line that matches the shape of the problem.
2. **Alternating projections in truncation**, between the model's positive cone
   and the affine set of Weil-matching functionals. Not as a decision procedure —
   the tangency kills the rate — but because the gap vector *is* the dual
   certificate, so one formulation yields both directions.
3. **Schauder on the trace cone**, if and when someone has a candidate self-map.
   The set is now available; the map is not. The place to look for a genuine
   nonlinear self-consistency is the Schur RG flow of Ambrosino-Gaiotto, where
   the pairing is determined by a flow rather than written down — but see §3 on
   why its *fixed points* are the wrong objects.
4. **Not** Knaster-Tarski on operator intervals, and **not** an RG fixed point.

## 7. Status

- §1 and §2: definitional, and a correction of my own earlier overstatement.
- §3's RG exclusion: **proved** (the dilation action on `{log p}` and on the
  density symbol).
- §3's Kadison citation: quoted, not reproved. Kadison, *Order properties of
  bounded self-adjoint operators*, Proc. AMS 2 (1951), 505-510.
- §3's Klyuev citations: as in [the q-Weyl note](QWEYL_TRACE_SPACE_20260916.md).
- §5's spectral assembly and the Bessel closed form: the latter **verified** to 30
  digits against quadrature; the former is Corollary 2.2, classical input.
- §5's table: **numerical**, computed with `mpmath` at 50 digits with 80 zero
  ordinates, outside the repository's standard-library-only convention. It is
  therefore **not yet a registered check**; porting it is the first item of
  [the continuation note](CONTINUATION_20260916.md). The entries are
  underestimates (truncation of the zero sum only lowers them) and upper bounds
  on the true `lambda_min` (any Rayleigh quotient is).
- §5's three observations about manuscript 0.5: the first is a direct run of the
  repository's own programme, the second and third follow from the table.
