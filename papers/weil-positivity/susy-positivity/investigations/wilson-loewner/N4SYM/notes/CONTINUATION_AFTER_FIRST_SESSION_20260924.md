# Continuation after the first N4SYM session

24 September 2026. Prepared for Edward Baker by Claude Opus 5.5 (Anthropic; model identifier `claude-opus-5-5` as reported by the runtime; session configuration `claude-fable-5-1`; reasoning effort not exposed).

This note hands the investigation to the next session. The block below is a ready prompt.

```
Continue the N4SYM investigation in the shifted-zeta-positivity repo:
papers/susy-positivity/investigations/wilson-loewner/N4SYM. It was opened 23
September 2026 from a GPT-6 (Codex) proposal; the first working session
(Claude, 23-24 September) completed the straight-line audit and analyzed a
replacement growing-trace observable. Nothing from that session is committed.

READ FIRST, in this order (do not re-derive the framing from them):
  N4SYM/README.md                                        - status in brief
  N4SYM/notes/STRAIGHT_LINE_RESPONSE_AND_TRACE_COMPLETION_20260923.md
      Section 0 and the ledger in Section 7
  N4SYM/notes/FLIPPED_RETURN_TRACE_ANALYSIS_20260924.md  - Sections 0, 2, 5, 7
  N4SYM/reviews/review_claude_first_session_20260923.md  - what the referee
      caught, and the residual concerns
  N4SYM/notes/N4SYM_DISPLACEMENT_LOEWNER_RESEARCH_PROPOSAL_20260923.md
      Sections 7 and 11 (work package D, milestones)

WHERE THINGS STAND.
  - Straight half-BPS line, all lambda, N. The quadratic shape response is
    pi B int (|k|^3|h|^2 - |k||j|^2) plus one perimeter constant c_R = -m_R/2.
    The linear retarded response is LOCAL: chi_R = m_R w^2 + 2 pi i B w^3,
    i.e. <D> = -m_R h'' + 2 pi B h'''. The reason is 1d conformal symmetry
    with integer Delta_D = 2, which holds in any bulk dimension (NOT Huygens;
    an earlier draft said Huygens and was corrected). Total work is
    2 pi B ||h''||^2 = CHMS. The renormalized finite-time account (Schott
    term) is negative just after every finite-order onset for any finite m_R.
    The tilt channel is an exact resistor. So the linear straight-line channel
    is CLOSED as an arithmetic candidate.
  - Growing trace. In the CFT, W depends on t only through s = a sqrt(t)
    (plus cusp scaling and regulator/sqrt(t)). Constant n0 with a straight
    return chord is a thin sliver: log W ~ (3 lambda'/(2 pi s)) log(1/eps),
    divergent. n = M T (Zarembo) has <W> = 1, a null control. RECOMMENDED
    family: n0 on the trace, -n0 on the chord ("flipped return").
  - Flipped return:
      Qdot = [ik(J + iG) + gamma Phihat(1)] Q, with gamma = d(L_tr - L_ch)/dt.
      The second equation follows from d_t Xhat = r (qdot.DX)^ + [Xhat, K(r)].
      Both are verified.
      At fixed flow: W = 1 + (2a^2t^3/81)(C^Phi - C) + (a^4 t^3/1458) S,
      confirmed at one loop by the flowed Feynman integral.
      Continuum one loop, vertex excision:
      log W = B_1[-(2 pi s/3) log(l/eps) + (4 pi/3) s + O(s^2 log)].
      Flow scheme: three regimes, with |s| log|s| in regime III.
      Open: the all-orders coefficient H = lim Gamma(pi - alpha, pi)/alpha
      (one loop: lambda'/(16 pi)).

THE TASK, in order.
  1. H(lambda, N). Drukker-Forini (arXiv:1105.5144) give the generalized cusp
     Gamma(phi, theta) at two loops and at strong coupling. VERIFY those
     formulas from the paper itself before use. Expand at phi = pi - alpha,
     theta = pi, alpha -> 0, and report H at two loops and at strong coupling.
     Test the hint in the flipped note, Section 7: does the effective coupling
     lambda(1 - phi^2/pi^2) -> 0 make the leading coefficient one-loop exact?
     A sharp "no" is a fine result. Beware: the linearized near-BPS formula is
     off by a factor 2 at one loop in this corner (sin phi -> 0).
  2. Rounded flipped family. Choose a rounding at scale delta = dhat sqrt(t)
     with a stated scalar profile on the arcs (for example n rotating with the
     tangent). Compute W(s, dhat) at one loop. This gives a finite,
     scheme-free function.
  3. Closure audit. Do the finite-regulator Schwinger-Dyson audit of the
     flipped first moment (flipped note, Section 6), keeping the transverse
     gauge current, the scalar current, Yukawa and scalar-potential terms and
     the flow response. Produce an inventory, not a closure claim.
  4. Only if 1-3 are done: the quartic straight-line response from the known
     displacement-multiplet four-point functions (Giombi-Roiban-Tseytlin,
     Ferrero-Meneghelli; verify the citations). This is where nonlocal
     response first appears on the straight line.

DO NOT: run arithmetic comparisons (no nonlocal causal kernel exists yet);
re-open the linear straight-line channel; use the constant-n0 chord family or
the tangent-coupled family as evolution observables; re-inflate the corrected
claims ("every smooth drive", "Huygens", "positive in h" without c_R = 0).

TRAPS that cost time in the first session.
  - The linear-driver implicit relation a q + 2 log(1 - aq/2) = a^2 t is
    ill-conditioned for s < 0.05, because it cancels to O(q^2). Use the exact
    series there; c1..c12 agree with the parent record.
  - Finite-difference second derivatives of tr Q are roundoff-limited
    (tr Q ~ 2, while its second derivative ~ 1e-3). Use a step ~ 0.1 t with
    Richardson extrapolation.
  - Regime I of the flowed one loop: the two leading terms cancel near
    s^2 = 4.5/tau_hat, and M_0 cancels O(1) pieces down to (s^2/27)^2.
    Compare on the scale of the pieces, not relative to the total.
  - Vertex excision and separation-based regulators (flow, point splitting)
    differ at a near-BPS cusp by Gamma(alpha) log(alpha): an |s| log|s|
    term. State the scheme.
  - Sign conventions: m_R = -2 c_R. With w = i p, chi(p) = -m_R p^2 +
    2 pi B p^3. Euclidean D = iF_{i sigma} + D_i Phi, which is OS-real.
  - validation/check_package.py was already failing at 8b22141 (the proposal
    commit). Its 'refresh' rewrites the curated author/scope fields of
    PACKAGE_RECORD.json; if you refresh, restore them.

STANDARDS. Classify every statement as a proof, proof sketch, labelled
numerical computation, observation, reading or literature. Check the algebra
independently. Use a separate referee context for high-stakes derivations;
it caught seven errors last time. Prefer a sharp negative result, and say so
plainly if the direction looks wrong.

CONVENTIONS. Notes in N4SYM/notes, programs in N4SYM/numerics with records in
N4SYM/numerics/records (standard library only, JSON to stdout, deterministic,
not registered in validation/drafts.py until a manuscript exists), audits in
N4SYM/reviews. Put the model at the top of anything you write. Follow the
repository LARGE_FILES policy. Update the N4SYM READMEs, the investigation
README line and CHANGELOG.md in the same pass. End with a continuation note.
```

## Notes on the prompt

**Why task 1 comes first.** It is cheap, because the formulas already exist in the literature. It also decides whether the continuum short-time law of the recommended family is coupling dependent. If the coefficient turns out to be one-loop exact in this corner, that would be a structural statement worth recording. If not, the family is simply a controlled near-BPS observable.

**Why the arithmetic comparison is deferred.** Neither the straight-line channel nor the flipped family has produced a nonlocal causal kernel. Proposal work package F requires one before any comparison is meaningful.

**State of the files.** This session added, uncommitted:

- two research notes and this continuation;
- three check programs with records (72 + 77 + 47 cases, all passing);
- an audit and the numerics and reviews READMEs;
- updates to the N4SYM README and notes README, the investigation README and CHANGELOG.md.

The proposal commit is `8b22141`.
