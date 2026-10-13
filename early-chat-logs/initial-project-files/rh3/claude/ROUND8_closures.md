# Round 8: three closures, and one route left

**2026-08-26.** Supersedes the consolidated ranking of `BRIEF_three_live_routes`. Technical detail
for all of it is in `NOTE_4d_anisotropic_cycles.md`; this is the state of play only.

## What closed

| item | brief's rank | status after round 8 | how it closed |
|---|---|---|---|
| Route 3 — quaternionic Jensen / Weierstrass | 2 | **closed** | deciding check done; prediction refuted; loose end closed; binding constraint isolated to one scalar |
| Route 5(a) — Chern–Simons → quantum modular chain | 3 | **closed** | McSpirit–Rolen read: arrow is one-way; species mismatch confirmed twice |
| Lefschetz thimbles / Stokes integrality (new this round) | — | **closed** | Riemann–Siegel has one saddle, not several; saddle is zero-independent; polynomial analogue refuted at `z²+1` |
| Route 4 — Jensen polynomials of gauge sequences | 4 | closed in the brief | unchanged |
| **Route 5(b) — retarget to Nyman–Beurling** | **1** | **the only live item** | untouched |

## The two findings worth carrying forward

**1. Route 3's obstruction, stated exactly.** Every `SO(3)`-invariant cycle in `ℍ` has volume element
`dV₃ = 4πy² ds`, `y = |Im q|`. A single orbit 2-sphere returns `log|F|` pointwise, so the invariant 4D
data is *pointwise equivalent* to the classical 1D data on the closed upper half-plane — no loss, no
gain. The one thing four dimensions contributes is the `y²` factor, and its only real cost is that it
forces the integration weight to vanish on the real axis, which pins the weight's constant term. That
single pinned scalar is what kills detection of a near-real conjugate pair: freeing it recovers the
full Hermite cone to four digits at every `ε`; keeping it (the actual geometry) loses everything below
`ε ≈ 0.15`.

> **The four-dimensional volume element is blind to the critical line.** That is the whole of route 3.

**2. A cheap new screening question.** Route 3 failed because the geometry's natural weight *vanishes*
on the locus of interest. Kenyon–Okounkov–Sheffield (`NOTE_existence_loophole` §5.2(b)) works because
the geometry's natural degeneration *is* the locus of interest — total reality ⟺ maximal degeneration
of the amoeba map. Same for the refuted Stokes idea: "maximal degeneracy ⟺ reality" had exactly the
right shape and failed only on the converse.

> **Screen.** Does the candidate structure's natural degeneration *coincide with* the target locus, or
> *avoid* it?

This is cheaper to evaluate than round 1's rigidity question and it separated three of this round's
items correctly in advance. Worth applying to the Nyman–Beurling candidates first.

## One thing that got *more* interesting, in the opposite direction

Fantini–Rella, *Modular resurgent structures* ([arXiv:2404.11550](https://arxiv.org/abs/2404.11550)):
the Stokes constants there **are the Dirichlet coefficients of an `L`-function**. That upgrades route
5(a)'s "physics *produces* arithmetic" card from an analogy to an explicit `L`-function — and it says
nothing about zeros, so it does not revive the chain. But it is the only place in eight rounds where
the production direction is concrete, and it is the natural thing to read if route 5(b) stalls.
*(Verified through an extraction layer, not read directly.)*

## What to open the next thread with

Route 5(b), unchanged from the brief's §5.4 and still unstarted:

1. Read the Nyman–Beurling / Báez-Duarte / Bettin–Conrey literature properly. This project has never
   touched it.
2. Run the Davenport–Heilbronn control against the criterion. The brief flags this as the first thing
   to check and expects it to pass *informatively*, unlike the N=4 reformulation.
3. Only then: does any physical or geometric structure supply the density statement? Apply the new
   degeneration screen above alongside the round-1 rigidity question. **Build nothing before this is
   answered** — the brief's own instruction, and the round-6/round-8 methodological rule that a
   computable question should be answered rather than proposed.

Sarnak's warning still applies with full force and should be restated at the top of that thread:
switching criteria is not progress by itself.

## Methodological note

Three of round 8's four corrections were self-caught by controls run *before* the conclusion was
drawn, against one inherited error. That is the first time in this project the ratio has gone that
way. The `NOTE_existence_loophole` §10 corrective — *for every claim of the form "X cannot happen,"
run the control that would show X happening in a case where it does* — plus the round-6 companion —
*before proposing a computational question, check whether it is computable now* — are both earning
their keep and should stay standing policy.
