# Continuation after the third N4SYM session

24 September 2026. Prepared for Edward Baker by Claude Fable 5.1 (Anthropic; session configuration `claude-fable-5-1`, the serving model can differ; no model identifier was exposed by the runtime; reasoning effort not exposed). This supersedes the [second continuation](CONTINUATION_AFTER_SECOND_SESSION_20260924.md), which is preserved.

```
Continue the N4SYM investigation in the shifted-zeta-positivity repo:
papers/susy-positivity/investigations/wilson-loewner/N4SYM. Three Claude
sessions (23-24 September) have run. Nothing from any of them is committed.
Ask me before any git operation; a zero-byte .git/index.lock may reappear.

READ FIRST:
  N4SYM/README.md                                              - status
  N4SYM/notes/FINITE_MASS_MEMORY_AND_QUARTIC_RESPONSE_20260924.md - Sections 0, 2.3-2.5, 3.4, 5
  N4SYM/reviews/review_claude_third_session_20260924.md
  N4SYM/manuscript.tex (18 pages; sections/*.tex)               - the draft

WHERE THINGS STAND.
  - Straight line: linear response local (Abraham-Lorentz); channel closed.
  - Flipped return: exact first two equations; regular in every regime;
    corner coefficient one-loop exact order by order with g = lambda|s|;
    sqrt(lambda|s|) window at strong coupling with F(0) = 0.1750; rounded
    family finite; Schwinger-Dyson hierarchy not closed.
  - Finite-mass source (option B1, done): exactly F = m Y'', X = Y + z_m Y',
    m X'' = F + z_m F'. One exponential memory, chi_m = -m w^2/(1 - i w z_m).
    W(T) = (m/2) Y'^2 + (sqrt(lambda)/2pi) int Y''^2 >= 0 at every T; the
    Schott term is the O(z_m) truncation. The dilaton-coupled boundary field
    is EXACTLY local in the retarded time t - r_m, r_m = sqrt(r^2 + z_m^2):
    the depth integrand is a total derivative, transfer = e^{i w r_m} P_4(w)
    with P_4 in closed form (note, Section 2.3). Front test fails; no
    arithmetic comparison run.
  - Quartic straight-line response (option B2, structural): GFF is linear;
    cubic response = connected 4-pt function, O(1/sqrt lambda); memory tied
    to non-protected dimensions (Delta_6 = 1 + lambda/4pi^2 weak,
    2 - 5/sqrt(lambda) + 295/24lambda - ... strong); the straight line has
    no scale, so no fixed delays at any order. GRT Delta = 1 four-point
    functions (eq. 4.19) validated by crossing and OPE; the Delta = 2
    transcription failed crossing and is NOT used.
  - A referee context reports that Callan-Guijosa (hep-th/9906153, eqs. 25-26)
    claimed an "infinitely broadened pulse" for the dilaton observable with
    an intermediate kernel that disagrees with the exact one beyond w = 0.
    UNVERIFIED BY EYE (fetch rate limit). Do not state publicly until checked.
  - Manuscript: first draft at N4SYM/manuscript.tex, 18 pages, builds
    cleanly with latexmk (no overfull boxes), inspected page by page by the
    same assistant. No BUILD_RECORD yet; programs not registered.

SUGGESTED ORDER OF WORK (ask me if the priority has changed).
  1. Check Callan-Guijosa by eye (journal version NPB 565 (2000) 157, or the
     arXiv PDF): compare their eq. (25) kernel with
     32 g_4 e^{-i w rho} = w^4/rho^5 + 10 i w^3/rho^6 - 45 w^2/rho^7
                           - 105 i w/rho^8 + 105/rho^9,
     and their eq. (26) with T = e^{i w r} (1 - i w r)/(4 r^6) at z_m = 0.
     Record the outcome in the note's Section 2.4 and in the manuscript
     Remark 5.4 (soften or sharpen accordingly).
  2. Nonlinear localization: does the dilaton response of the full
     Mikhailov string localize on the light cone at O(Y^2)? (The energy
     density does: ACLNR 1001.3880, HIMT 1011.3763/1102.0232, Hubeny
     1012.3561.) A total-derivative structure at second order would make
     Proposition 5.3 of the manuscript a statement about the exact string.
  3. Lorentzian cubic kernel of the tilt channel: continue the validated
     G^(1) (S, T, A) across chi = 0, 1, infinity with i epsilon
     prescriptions, or compute the Lorentzian tree Witten diagram on AdS_2
     with the light-cone-supported Delta = 1 propagator. This makes
     Proposition 6.2 quantitative and gives the first explicit nonlocal
     kernel on the straight line.
  4. Option (A) items remain open if the physics route is preferred:
     three-loop corner Phi(g,0) from CHMS arXiv:1203.1019 (VERIFIED
     citation this session: JHEP 05 (2012) 098; formulas still to verify),
     and the one-loop string correction that smooths the kink of F at
     theta = pi.
  5. Manuscript: visual re-review after any change; then the BUILD
     workflow (record, register the seven programs in a replay, update
     DRAFT_HISTORY.md with the containing commit). Confirm by eye every
     equation number cited from fetch summaries (CHMS eq. 8, 55, 14, 20,
     25, 6, 5, 58; DF 3.1-3.2; CGG 4, 6, 28, 34, 35; GRT 4.3, 4.19, 4.34,
     4.43, 5.17-5.19, 5.24; BGT 3.6-3.7).

DO NOT: run arithmetic comparisons (every channel examined fails the front
test or is not a channel); use the transcribed GRT Delta = 2 functions;
call the exact localization a nonlinear result; call H exact
nonperturbatively; extrapolate the two-loop corner form; treat the
Callan-Guijosa discrepancy as established.

TRAPS (new this session).
  - The oscillatory depth integral int_{z_m}^inf dz (...) e^{i w u(z)} is
    unreliable on the real axis at large w; rotate the contour
    z = z_m + t e^{i theta} (theta ~ 0.6) or use the antiderivative G.
  - The endpoint asymptotics of that integral are w^4 z_m^3/(32 r_m^5 u')
    for w z_m >> 1 and w/(4 r^5) for z_m = 0 (exponent 1, not 2: the
    amplitude vanishes like z^2 and (1 - i w z) supplies a power).
  - A Laurent-polynomial ansatz in (z, rho) for the antiderivative has NO
    solution; the (rho + z)^{-3} denominator (i.e. (rho^2 - z^2)^{-3}) is
    essential.
  - With Y = e^{-i w t}, -i w r Y = + r Y': the massless limit is
    Y(t - r) + r Y'(t - r) = x(t, z = r), not Y - r Y'.
  - The point-limit remainder is O(sqrt(lambda) z_m) at fixed lambda, not
    O(z_m^2).
  - In the quartic program, evaluating G^(1) directly at chi <= 1e-6 loses
    the chi^2 log chi structure to cancellation; extract log coefficients
    from the rational prefactors instead.
  - Earlier traps (both continuations) still apply, in particular the
    cos(theta) - cos(phi) form and the flow/excision scheme distinction.

STANDARDS and CONVENTIONS as before: classify every statement; separate
referee context for derivations; standard-library programs with records
under N4SYM/numerics/records; model at the top of every file; READMEs and
CHANGELOG in the same pass; end with a continuation note.
```

## State at handoff

This session added, uncommitted:

- one research note, [FINITE_MASS_MEMORY_AND_QUARTIC_RESPONSE_20260924.md](FINITE_MASS_MEMORY_AND_QUARTIC_RESPONSE_20260924.md);
- two programs with records (107 + 93 cases, all passing, deterministic on the author's machine);
- a [third audit](../reviews/review_claude_third_session_20260924.md) with two referee passes;
- the first draft [manuscript](../manuscript.tex) with `preamble.tex`, `references.tex`, `sections/`, `manuscript.pdf` (18 pages, 452 KB), [BUILD.md](../BUILD.md) and [DRAFT_HISTORY.md](../DRAFT_HISTORY.md);
- this continuation;
- updates to the N4SYM READMEs, the investigation README and CHANGELOG.md.

The whole N4SYM record now has seven programs and 472 cases. Pages that could not be fetched this session (arXiv rate limit): the abstract page of 0903.2047 and the PDF of hep-th/9906153; INSPIRE supplied the publication data.
