# External review of project 17 at commit 9e98460

11 October 2026. Prepared for Edward Baker. Reviewer model: Claude Fable 5.1
(`claude-fable-5-1`), Anthropic, in Claude Cowork. Cross-model review of
material prepared with GPT-6 / GPT-6.1-sol (Codex). Source state: GitHub
`main` at `9e98460` ("Index quasi-RH strategy continuation in project 17
history", 10 October 15:04), merged into the author's working branch.

This updates the project-17 section of
`../../reviews/NEWMAN_COLLISION_CORE_PROJECTS_EXTERNAL_REVIEW_CLAUDE_20261010.md`,
which reviewed the folder at `eddf25c` (manuscript only, 38 KB, one note).
Since then: the manuscript grew to 66 KB (new §§3.3–3.5, 5, 6 and a Note-8
appendix); Notes 2–8; Reviews 2–5; seven standard-library checkers with
JSON records. Two parallel Claude reviewers split the material (A:
manuscript, Notes 1–5, transport/stationary-criterion sections, three
checkers; B: Notes 6–8, theta-sign and Laguerre-kernel sections, four
checkers). I verified the two structural claims below myself.

Facts carried over from the earlier reviews and used here: (A) at an
all-real double zero the threshold expression is `72W²Σ(x−ρ)⁻² > 0`; (B)
the kernel `q_{T,b}` has de Bruijn–Newman constant exactly `T`; (C) the
adjoint-transport certificate is an equivalence — a certificate with
residual `R` and multiplier norm `Y` exists on a cell iff
`‖(F/2, F'/2L)‖ ≥ (1−R)/Y` there; (D) every zero of `H_t` with
`|x| ≤ 6·10¹⁰`, `0 ≤ t ≤ 0.2`, is real and simple (Polymath 15 barrier +
Platt).

## 1. Verdict

Everything new is correct. Every displayed identity in the new sections
and notes checks by hand or sympy (fold jets through order six, the
predecessor lemma for multiplicities 2, 4, 6 with generic jets, the score
dictionary, all Gaussian controls, the kernel Fourier identities, the
divisor-pair identity to 28 digits, the Note-8 exponent arithmetic). All
seven checkers pass under `python3 -I` and regenerate their records
exactly (modulo `python_version`/`runtime_seconds`). Two independent
40-digit implementations of `F_{t,N}` reproduce the `N = 22066` cell with
every one of 123 pointwise values inside its stored subcell enclosure
(minimum slack equal to the paid physical error), and an independent
mpmath replay of the low-height theta jets reproduces the inflection
point `x*(t) ∈ [9.4958, 9.5005]` and the certified product
`H_x H_xxx ∈ (−4.18·10⁻⁷, −3.78·10⁻⁷)`.

The conclusion of the earlier review is unchanged: close with a closure
note, promise 1/5. The project has moved from a transport certificate that
is provably an identity (C) to a Laguerre-type sign criterion whose global
form is equivalent to RH, whose only certified instances lie where known
results force the sign, and whose "theta targets" contain no theta data.
The README's own sentence — "the two bounded stationary calibrations add
no collision coverage" — is correct and, as shown below, understated. The
one genuinely new object, the divisor-pair representation of the kernels,
is a correct exact rewriting with no sign.

## 2. The stationary-sign criterion

Theorem `thm:stationary-signs` is the nicest piece in the folder and its
proof is complete: for a real-analytic solution of `H_t = −H_xx` on an
open set, if (S0) `H H_xx ≤ 0` wherever `H_x = 0` and (S1)
`H_x H_xxx ≤ 0` wherever `H_xx = 0`, then there is no multiple real zero.
The predecessor lemma (an exact zero of multiplicity `2r` at `(T, a)` has,
for small `h = T − t > 0`, a critical curve on which
`F F_xx = F_m² h^{2r−1}/(r!(r−1)!) + O(h^{2r}) > 0`) was verified
symbolically for `m = 2, 4, 6`; the odd case via `F = H_x` genuinely needs
(S1). No all-real hypothesis is used.

What the criterion is. For `H_t` with Hadamard product
`H_t(0)Π(1 − z²/ρ²)`,

    H_x² − H H_xx = −H² (log H)'' = H² Σ_ρ (x − ρ)⁻².

So (S0) is Laguerre's inequality restricted to the critical set and (S1)
the same for `H_x`. Three consequences the manuscript does not state:

- At every time at which all zeros are real — every `t ≥ Λ`, and all
  `t ≥ 0` under RH — both signs hold automatically, with equality in (S0)
  exactly at a multiple zero. The criterion asks nothing at LP times.
- On `Ω = (0, ∞) × ℝ` the criterion is equivalent to RH: (⇐) Laguerre;
  (⇒) the theorem excludes every positive-time collision, so `Λ ≤ 0`, and
  `Λ ≥ 0` (Rodgers–Tao) gives `Λ = 0`.
- Its nontrivial content lives only on `0 < t < Λ`, where a conjugate pair
  `a ± ib` contributes `2[(x−a)² − b²]/[(x−a)² + b²]²` to the sum,
  negative iff `|x − a| < b`: (S0) fails at a critical point exactly when
  near-real complex pairs dominate — the precursor signature of a
  collision. The criterion is therefore not a restatement at the collision
  point in the sense of (A); it is a restatement through the collision's
  necessary precursor, "no near-real complex pair is visible at any
  positive time", which is the Csordas–Varga programme (RH ⇔ Laguerre-type
  inequalities) deformed in `t` and restricted to the stationary sets.

Nothing theta-specific enters. The "complete theta score/overlap targets"
(T0), (T1) are built from `D = 4C + E`, but the score density cancels
identically: `D = −β²A'' − 2βxA' − (x² + 2β)A`, a differential operator on
the readout `A` alone (sympy), so (T0) is `−β²AA''` on `A' = 0` and (T1)
is `−β²A'A'''` on `A'' = 0`. The project's own Gaussian controls
(`(16u⁴ + 24)e^{−(1+1/40)u²}`, with Newman constant exactly `1/40`; the
triple and quadruple densities) and kernel (B) all satisfy every generic
hypothesis and violate (S0) before their collisions, which the text
concedes.

## 3. The two "paid genuine-theta stationary signs"

Both are correct, rigorously enclosed, and independently reproduced; both
are foregone conclusions.

High cell (`N = 22066`, `x − x₀ ∈ [0.3, 0.7]`, `t ∈ [t₀, t₀ + 8·10⁻⁶]`):
inside the box of (D), so every zero is real and simple, the two nearest
real zeros (at distance ≈ 0.27 and ≈ 0.33 from the critical point)
contribute ≈ 22 to `Σ(x−ρ)⁻²`, and any hypothetical complex zero beyond
`6·10¹⁰` contributes at most `6·10⁻¹¹` in total. `H H_xx < 0` at the
critical point, with margin `≈ 30H²`, is therefore a corollary of
Polymath 15 + Platt, unconditionally — stronger than the certified
statement, which is conditional on the imported disk bound. The
independent replay gives `H_xx/H ≈ −26`, consistent.

Low rectangle (`x ∈ [8, 12]`, `t ∈ [0, 0.05]`, direct theta integrals):
the nearest zero of `H_t` is at `x = 28.27` (`t = 0`) / `28.24`
(`t = 0.05`), sixteen units away; `H_t > 0` and `H_x < 0` throughout; no
collision is geometrically possible, and the inflection sign is the generic
sign of a positive decreasing function with all zero structure far away.
The enclosure (theta tail `n ≥ 4` by the stated bound, `e^{tu²}` taken
over the whole time interval, trig by cell-centre rotation plus Lipschitz
padding, `u > 1` tail by the Gaussian envelope) is sound; the hull is
~10% wide because the phase padding is coarse, harmless here.

The README says the calibrations "add no collision coverage: their first
jets already exclude joint zeros". True; the sharper statement is that
they certify a sign in regions where the sign cannot fail.

## 4. Sharp residuals, restricted primes, regular cell

All corollaries of (C), and the text now effectively says so
("unrestricted pointwise transport optimization exactly reproduces the
correlated first-jet test"; eq:sharp-directional proves a strict
directional certificate exists iff `(F/η)² + |F'/(Lη)| > 1`). The explicit
prime-division-tree witness is correct, but by (C) any witness is as good
as any other. The restricted-prime obstruction (`𝓡 ≥ 1 + 82‖y‖` with
primes 2, 3 only, `L ≥ 160`) is correct, elementary (fewer edges enlarge
the kernel and add pairing constraints), holds only for `x ≳ 10⁷⁰`, and
retires a construction (C) had already retired. The regular cell with
`y = (1, 0.15L)` is the scalar test `Re S + 0.15 Re S' > 0.0149` on a
window inside the box of (D); the record's own "38 by value, 2 by
derivative" shows the correlation was unnecessary. Independent replay:
`Re S + 0.15 Re S' ∈ [0.6088, 1.3271]` against certified
`[0.5701, 1.3557]`.

## 5. Laguerre kernels and the divisor-pair identity

`𝓛_j(H; x) = Ĵ_{j,t}(2x)` with
`J_{j,t}(s) = ∫ r²(r² − s²)^j m_t(s+r) m_t(s−r) dr` is the classical
weighted-autocorrelation identity (Csordas–Varga; Csordas 2013, which the
notes cite), verified to 12 digits at `(x, t) = (9.5, 0.03)`. "Positive
definiteness of the complete kernels" is, by Bochner, `𝓛_0(H_t) ≥ 0` and
`𝓛_0(H_t') ≥ 0` on the whole line: at `t = 0` the open Laguerre
inequality for `Ξ` (Csordas's Open Problem 4.7, as Note 7 itself
reports); for all `t ≤ 0.22`, equivalent to RH by §2; automatic for
`t ≥ Λ`. The `J_{1,t}(0.3) < 0` computation is correct and reproduced
(`−1.744·10⁻⁹` to `−1.761·10⁻⁹`) and refutes nothing anyone held: with
`m_t` concentrated in `|u| ≲ 0.14`, negativity for `s² > 3/(4a_eff)` is
what the Gaussian model predicts. The triple-blindness lemma is a one-line
consequence of `𝓛_0 = H²Σ(x−ρ)⁻²`.

The divisor-pair identity (Note 8, eq. 10), re-indexing the double theta
sum by `P = nm` with `d_n = ¼ log(m/n)` and polynomial factor
`π²P²e^{10s}[z² − 6z cosh 4ρ + 9]`, `z = 2πPe^{4s}`, is correct
(symbolically and numerically to 19–28 digits; the divisor-moment formula
`μ₂(P)/τ(P) = Σ_{p^b‖P} b(b+2)(log p)²/48` checks for `P = 12, 360, 1024,
77`). It is the first object in the folder with arithmetic content, and it
is a representation: `B_P` is signed and the Fourier phase remains, as
Note 8 says. Heat Note 14's caveat applies verbatim.

## 6. Note 8: the conditional 33/41 step

Arithmetic correct: with `θ_out = max{(1+a)/2 + 5h/12, θ(1 − h/6)}`,
balancing gives `h* = 6(2θ−1−a)/(5+2θ)` and `T_a(θ) = θ(6+a)/(5+2θ)`; at
`θ = 11/12`, `a = 0`: `h* = 30/41`, both branches `33/41`. The external
preprint was not fetched or evaluated; its theorem is taken as the stated
hypothesis.

Beyond the assumed `11/12` strip the step needs: (H1) a quantitative
smooth Möbius bound `|A_1| ≪ L^{11/12+ε}` uniform in scale and profile
class (derivable from the strip via reciprocal growth, as the note says);
(H2) the unproved short-row mean square
`Σ_{Nu ≤ D^{30/41}} |A_u(D)|² ≪ D^{71/41+ε}` with loss `a = 0`, for all
permitted profiles — square-root cancellation on average over `D^{30/41}`
characters with Möbius weights, beyond the large sieve, and not supplied
by the preprint's rows up to `D^{1+ϑ}`; (H3) replication bookkeeping
(`χ_n(p⁶) = 1` for `p ∤ n`, prime-ideal counts, mask compatibility) and
the converse Mellin argument; (H4) for iteration, the same at every stage
with `h* ↓ 0`, an infinite sequence of increasingly strong unproved
estimates whose limit is RH-strength on the unit row (acknowledged).

A point the note does not make: (H2) alone, applied to the single row
`u = 1`, already gives `|A_1(D)| ≪ D^{71/82+ε}` (`0.866 < 11/12`) with no
use of the strip. The strip enters only the error term `θ(1 − h/6)`. The
honest headline is "(H2) ⇒ 33/41", not "11/12 ⇒ 33/41". The arithmetic
lane belongs to the short-families project, not to 17.

## 7. Checkers and hygiene

All seven pass; records identical to the repository copies apart from
`python_version` and `runtime_seconds`; source hashes match Review 4's
table. Runtimes here: optimality 0.2 s, transversality 0.4 s, regular
cell 51 s (Note 3 says ~25 s), Laguerre algebra <1 s, theta kernel 3 s,
low-height 23 s, stationary cell 86 s. Assertion counts are loop counts:
1,878 ≈ ten distinct identities; 1,819 ≈ twenty-five; 167 ≈ six (112 are
one hierarchy identity over 14 polynomials × 7 orders). None tests anything
about ζ. `check_regular_adjoint_cell.py` overwrites its record in place on
a bare run (the others require `--record`/an explicit path).
`DRAFT_HISTOR.md` remains misnamed; the 3-node example
`eq:rational-source` is still a chain rather than the divisor graph; the
manuscript cites its own notes as the proof of two propositions. Internal
Reviews 2–5 are same-model restatements. Attribution, LLM disclosure and
the records' limitation lists are present and candid throughout.

## 8. What the closure note should contain

Fact (C) with its directional form `eq:sharp-directional`. The Laguerre
identity `H_x² − HH_xx = H²Σ(x−ρ)⁻²`, hence: (S0)/(S1) automatic at LP
times; the global criterion equivalent to RH; the local one nontrivial
only on `0 < t < Λ` and strictly stronger than "no collision in `Ω`" (it
also forbids precursor humps of collisions outside `Ω`). That `D` is a
differential operator on `A`. That `J_0, J_1` are Csordas's kernels with
their listed open status. Fact (D) for every certified window below
`6·10¹⁰` and the zero-free status of `[8, 12]`. That the 33/41 step is
conditional on (H2), which does the work.

What should stop: multiplier and transport constructions (Notes 2–3 close
that door themselves); calibrations below `x = 6·10¹⁰`; rewriting the
Laguerre expressions as theta overlaps. What could continue, narrowly and
only with a concrete idea in hand: a signed estimate from the divisor-pair
representation using `μ₂, μ₄, R_P` that kernel (B) and the Gaussian
controls cannot satisfy. Nothing in the folder proposes one.

No collision exclusion, threshold result, or RH conclusion is claimed or
refuted in this review.
