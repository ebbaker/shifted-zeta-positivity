# Continuation after the second N4SYM session

24 September 2026. Prepared for Edward Baker by Claude Opus 5.5 (Anthropic; model identifier `claude-opus-5-5` as reported by the runtime; session configuration `claude-fable-5-1`; reasoning effort not exposed). This supersedes the [first continuation](CONTINUATION_AFTER_FIRST_SESSION_20260924.md), which is preserved.

```
Continue the N4SYM investigation in the shifted-zeta-positivity repo:
papers/susy-positivity/investigations/wilson-loewner/N4SYM. Two Claude
sessions (23-24 September) have run. Nothing from either is committed.
A zero-byte .git/index.lock left by a 'git status' may be present; ask me to
remove it before any git operation.

READ FIRST:
  N4SYM/README.md                                               - status
  N4SYM/notes/NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md  - Sections 0, 1.4-1.6, 4
  N4SYM/notes/FLIPPED_RETURN_TRACE_ANALYSIS_20260924.md         - Sections 0, 2
  N4SYM/notes/STRAIGHT_LINE_RESPONSE_AND_TRACE_COMPLETION_20260923.md - Section 0
  N4SYM/reviews/review_claude_second_session_20260924.md

WHERE THINGS STAND.
  - Straight line: the linear response is local (Abraham-Lorentz), so the
    linear straight-line channel is closed as an arithmetic candidate.
  - Growing trace: the recommended family is the flipped return (n0 on the
    trace, -n0 on the chord). Its first two smooth-field equations are exact
    and verified. At fixed flow the short-time law is t^3, confirmed at one
    loop. Continuum one loop: 1 - B_1 A(s) log(l mu) + ....
  - The corner coefficient: Gamma(pi - u, pi - x u) has effective coupling
    g = lambda u.
      Exact slope at the BPS line: (pi^2/2) B(2 lambda u/pi) (from CHMS).
      Two loops: (1 - x^2)[g/(16 pi) - g^2/(192 pi^2)].
      H = lambda(1 - 1/N^2)/(16 pi), one-loop exact order by order, under a
      multi-angle antiparallel bound.
      Strong coupling, 1/lambda << u << 1: Gamma = sqrt(lambda u) F(x), with
      F parametric and F(0) = 0.1750.
    For the flipped loop g(t) = lambda |a| sqrt(t)/3: Loewner time sets the
    corner coupling.
  - Rounded family: log W = -B_1[A(s) log(1/dhat) + (2 pi s/3)(log(s/3) - 2)
    - h s], with h = -4.0202 (convention dependent).
  - The Schwinger-Dyson audit does not close the flipped hierarchy. The
    irreducible terms are the transverse currents and scalar Laplacian,
    scalar and fermion currents, potential and Yukawa insertions, transported
    commutators, the tip gradient and ordered pairs.
  - The arithmetic link has not strengthened. The growing-trace observables
    are Euclidean expectation values with no input/output channel.

DECIDE FIRST (ask me if unclear). Either (A) complete the flipped family as a
self-contained physics result, or (B) return to the arithmetic goal by
looking for a physical channel with memory.

  (A) 1. Phi(g, 0) at three loops, from the known three-loop generalized
         cusp (Correa-Henn-Maldacena-Sever arXiv:1203.1019; VERIFY the
         citation and formulas before use). Does (1 - x^2) survive at O(g^3)?
      2. The one-loop string correction around the classical corner,
         including how the S^4 zero modes at theta = pi smooth the kink.
      3. If the results hold, a manuscript through the BUILD workflow, with
         the programs registered at that point.
  (B) 1. A finite-mass heavy source: the string endpoint at z_m, i.e. the
         Chernicoff-Garcia-Guijosa equation. Its displacement response has a
         memory scale set by the mass. Compute the retarded kernel and the
         energy account; test for a variable front or delays before any
         arithmetic comparison.
      2. The quartic straight-line response from the displacement-multiplet
         four-point function (Giombi-Roiban-Tseytlin, Ferrero-Meneghelli;
         verify), the first nonlocal response on the straight line.

DO NOT: run arithmetic comparisons on local or Euclidean-only observables;
extrapolate the two-loop corner form (1 - x^2)(pi^2/2)B(2g/pi) beyond two
loops; call H "exact" nonperturbatively; use the strong-coupling corner at
fixed lambda as u -> 0.

TRAPS.
  - cos(theta) - cos(phi) must be written as -2 sin((theta+phi)/2)
    sin((theta-phi)/2); the naive form loses all digits in the corner.
  - The classical corner string is NOT thin: its depth is zeta0 ~ sqrt(Omega)
    while the opening is Omega. That is the source of the sqrt(lambda u)
    scaling.
  - The minimal branch at theta = pi has a classical kink (antipodal S^5).
    Evaluate F on the branch with theta <= pi.
  - Fillet rounding and flow are separation-based regulators and give
    |s| log|s|; vertex excision does not. State the scheme.
  - The Zarembo-stadium test has an identically zero integrand and checks
    only conventions.
  - All earlier traps in CONTINUATION_AFTER_FIRST_SESSION_20260924.md still
    apply.

STANDARDS and CONVENTIONS as before: classify every statement; use a
separate referee context for derivations; standard-library programs with
records under N4SYM/numerics/records; put the model at the top of every
file; update the READMEs and CHANGELOG in the same pass; end with a
continuation note.
```

## State at handoff

This session added, uncommitted:

- one research note, [NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md](NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md);
- two programs with records (56 + 20 cases, all passing, deterministic);
- a [second audit](../reviews/review_claude_second_session_20260924.md);
- this continuation;
- updates to the N4SYM READMEs, the investigation README and CHANGELOG.md.

The whole N4SYM record now has five programs and 272 cases.
