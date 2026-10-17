# Round-one cross-model review of the source-measurement audit

17 October 2026, America/New_York. Prepared for Edward Baker with LLM
assistance. Model: Claude Opus 5.5 (configured identifier
`claude-opus-5-5`), Claude Cowork, reasoning effort max; the serving model
may differ from the configured identifier. This is the designated Claude
assessment at the boundary of [round one](../notes/round-1/README.md),
under the [round execution plan](../research-overview/02_ROUND_BASED_EXECUTION_PLAN_20261017.md).
It is a cross-model LLM review of work recorded by **gpt-6.1-sol (Codex)**,
effort **ultra**; it is not independent specialist review, and no subagents
were used. One caveat on independence: the claims the audit was opened to
test, [Reply 03](../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md)
§§1–2, were written by another Claude model (Claude Fable 5.1). On the
disposition of those claims this review is same-family, and
[avoid 05](../../../../avoid/05_same_model_reviews_and_shared_premises.md)
applies; the two new findings below are therefore given with proofs and
with checks that can fail, so that the reconciliation can test them
directly. Every statement is labelled as a verification of the round's
text, a proof sketch by the reviewer, a floating computation, an interval
computation, or a recommendation. Nothing here is a statement about the
zeros of zeta.

**Summary.** I found no mathematical error in Notes 01–05 or in the working
manuscript, and every finite computation reproduces. Re-running the replay
regenerates its certificates with identical enclosures; an independent
program that shares no code and uses different methods agrees with every
committed jet ball to about 58 digits, with all 24 conditioning constants
and with all 32 feasibility decisions; the Note 02 and Note 05 constants
recompute exactly. The analytic statements — finite endpoint separation,
the uniform endpoint expansion, the two-direction construction,
nondegeneracy, the complete-jet envelope and the threshold 3915 — are
correct as stated and carefully scoped. Two findings change how the
round's numbers should be read, and I would settle them in the one
reconciliation before the round closes:

1. **The sufficient radius is attained once in every zero gap (§3).** The
   ratios \(r_M/\eta\) between \(1.6\cdot10^5\) and \(3.1\cdot10^{11}\) in
   Note 03 are properties of the six prescribed abscissae. Between any two
   consecutive simple real zeros of \(H_\theta(t,\cdot)\), under a mild rank
   condition that holds in all 24 replay combinations, there is an
   abscissa at which the actual equality distance equals \(\eta\) exactly
   (two-line proof below). In the gaps containing all six replay points,
   \(r_M=\eta\) there to 60 digits, \(\eta\) there lies within a factor
   \(0.9999\)–\(25.4\) of the tabulated value, and in the unanchored
   recurrence design the minimizing source is strictly positive, with a
   nondegenerate collision at \(t=1/4\). Read at the scale of one zero gap,
   the reply's table of \(\eta\) measures, within those factors, the actual
   distance to a double jet, so the replay does not show that fixed designs
   are more powerful than the reply said. The headline of Note 03, one
   disposition row of the manuscript and the 32-case table need the
   qualifier "at the prescribed abscissa".
2. **Every nonzero finite perturbation has \(\Lambda=+\infty\) (§4)**, for
   nonnegative sources, which is the class the round works in. A
   finite perturbation's transform has an algebraic tail of fixed sign,
   while theta's jet decays exponentially; so the perturbed heat transform
   has only finitely many real zeros at every heat time, and, being of
   order one and infinite type, infinitely many non-real ones. With the
   round's own constants this is explicit: a change of \(10^{-16}\) along
   the Note 05 direction \(A\) leaves no real zero above \(x=264\) (above
   \(269\) at recurrence norm \(10^{-16}\)) for every \(0\le t\le1/4\), by
   interval arithmetic, and a preregistered floating illustration places
   the loss near \(x\approx145\), close to the reply's "about 140 at
   sixteen digits". The scoped obstruction of Theorem 1.1 and Corollary 5.1
   therefore holds in a stronger and more elementary form, already for
   one-dimensional \(V\). The prescribed-point construction and the
   threshold 3915 remain correct; they locate collisions and are
   refinements, not the main content.

Neither finding contradicts anything the round proves. Both remove
readings of its numbers on which a later portfolio decision could rely.
With them recorded, I would close round one and the project (§7).

## 1. Scope, artifacts and method

Repository HEAD `9390c848dd9eee12dd053f5179162fb7ea1d10df`, working tree
clean at inspection; the SHA-256 digests of the reviewed files are in
Appendix A. Read in full: the project README, draft history, both
research overviews, the round-one notes 01–05 with both indexes, the two
numerics READMEs, all eight programs and all seven JSON records, the
manuscript source; Reply 03 (all sections, with §§1–2 in detail), the
[Codex response](../../../brainstorm/investigations-3/reviews/02_RESPONSE_TO_CLAUDE_BRAINSTORM_CODEX_20261016.md)
§§1–2, the original [solver](../../../brainstorm/investigations-3/numerics/check_codex_response_reply_claude_20261016.py)
and its record, the [portfolio plan](../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md),
the [portfolio setup review](../../reviews/01_PORTFOLIO_SETUP_REVIEW_CLAUDE_20261016.md)
(whose §8 supplies the repaired proposition the proposal asked of Claude),
[22 Note 05/01](../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md)
and §5 of 22 Note 05/04; and, before writing, the whole of
[`avoid/`](../../../../avoid/README.md) and
[`result-summaries/`](../../../../result-summaries/README.md).

Method, in four parts.

- **Proof reading.** Every displayed identity and inequality of Notes 01,
  02, 04, 05, the tail bounds of Note 03 §1, and manuscript §§1–6 and
  Appendix A was re-derived by hand.
- **Replay.** `run_replay.py` and `concrete_onset_budget.py` were re-run in
  the cloud workspace (Python 3.13.16, mpmath 1.4.1, python-flint 0.9.0;
  33 s and 0.01 s).
- **Independent program.** [`review_checks_claude_20261017.py`](../numerics/round-1/claude-review/review_checks_claude_20261017.py)
  (mpmath only) and its record [`REVIEW_CHECKS_CLAUDE_20261017.json`](../numerics/round-1/claude-review/REVIEW_CHECKS_CLAUDE_20261017.json).
  It imports nothing from the round's programs and changes method wherever
  practical: at \(t=0\) the mode jets come from the closed form
  \(H_n(0,x)=\operatorname{Re}\tfrac14[2\lambda_n^2G_n(\tfrac94+\tfrac{ix}4)-3\lambda_nG_n(\tfrac54+\tfrac{ix}4)]\),
  \(G_n(s)=\lambda_n^{-s}\Gamma(s,\lambda_n)\), and theta's jet from
  \(\xi\) itself; at \(t=1/4\) by Gauss–Legendre quadrature after the
  substitution \(e^{4u}=1+v/\lambda_n\) (checked against the closed forms
  at \(t=0\) to \(3\cdot10^{-59}\)); conditioning by a whitened
  \(2\times2\) matrix and, separately, by a KKT solve on \(\mathbb R^6\);
  endpoint polynomials by Leibniz and Hermite rather than the combined
  recurrence; feasibility by rank and planar Carathéodory rather than
  Farkas witnesses. Floating at 60 digits except Sections G–H, which use
  mpmath interval arithmetic. Section letters below refer to that record.
- **Manuscript build.** Two pdfTeX passes: 14 pages, no warnings.

## 2. What was verified

| Claim | Where | Check | Result |
| --- | --- | --- | --- |
| Finite endpoint separation | Note 01 §2; manuscript Lemma 2.1 | re-derived the \(u\to-\infty\) series and \(c_k=(-1)^k(2k+1)\pi^k/(k-1)!\) | correct |
| Endpoint expansion with explicit remainders, cosine and sine | Note 01 (1)–(3); Note 02 (5); Lemma 2.2 | re-derived, including \((ug)^{(k)}(0)=kg^{(k-1)}(0)\) and the orders of \(E_p,F_p\) | correct |
| Two-direction construction, determinant and inverse bounds | Note 01 (5)–(6); Note 02 (7)–(9); manuscript (13)–(14), (24)–(26) | re-derived \(K_2,K_4,K_D\) and the root condition (8) | correct |
| Nondegeneracy outside a discrete set | Note 04 §2; Proposition 4.1 | ODE uniqueness and the asymptotic contradiction; \(H_\theta(t,0)>0\) | correct |
| Local heat event | Note 04 §3; Proposition 4.2 | Taylor model \(\tfrac k2(y^2-2s)\) and the real-analytic change of variable | correct |
| Envelope \(\|h\|\le\tfrac65e^{-\pi x/16}\), \(0\le t\le1/4\) | Note 02 §1; Proposition 6.1 | contour shift and majorants re-derived; constants in interval arithmetic (G) | correct: \(K_H\le1.1258087668\), \(K_X\le0.3144202767\), \(K\le1.1688907091\); at the sampled heights \(\|h\|e^{\pi x/16}\le0.25\) |
| Carrier modulus, asymptotic and derivative | Note 02 (10)–(12); manuscript Appendix A | re-derived from Polymath's (6), (9), (10) as quoted | correct |
| Note 05 constants and the threshold 3915 | Note 05; Theorem 6.2 | Leibniz–Hermite recomputation (F) | all ten constants agree to \(1.4\cdot10^{-60}\) relative; \(\|\delta\|_\infty\le3.414363786\cdot10^{-307}\) at 3915 |
| Remainder bounds can fail | Note 05 constants | actual remainders at \(x\in\{5,10,20,40,80\}\), \(t\in\{0,\tfrac14\}\) (F) | every remainder below 5.4% of its bound; determinant remainder below 0.015% |
| Measurement bounds \(\sqrt{35}\) and \(K_{\rm ref}<1.916\) | Note 05 §4 | direct | correct (\(K_{\rm ref}=1.91502\ldots\)) |
| Jets at the six observations | Note 03 §1 | closed forms and quadrature against the committed balls (A) | agree with the ball midpoints to \(3\cdot10^{-58}\) relative |
| \(C,\eta,r_M\) in 24 combinations | Note 03 §2; Table 1 | whitened \(2\times2\) and KKT (B) | \(C,\eta\) agree to \(2.4\cdot10^{-58}\), \(r_M\) to \(5\cdot10^{-41}\) |
| 32 feasibility decisions | Note 03 §3; Table 2 | rank and planar Carathéodory (P) | 32 of 32 agree |
| Source findings about the original solver | Note 01 §4 | read the solver | accurate: Stirling corrections in `carrier_abs`, weighted value at the Euclidean minimizer, normal equations in `restricted_norm_ratio`, the "overdetermined" and anchored wording; the inspected digests still match |
| Replay reproducibility | numerics README | re-run | `FEASIBILITY_WITNESSES.json` byte-identical; every enclosure in the other certificates identical, their bytes differing only in runtime fields and in hashes derived from them (§6) |

The table's "correct" means that I could follow every step and found no
gap; it is not specialist validation.

## 3. Finding 1: the sufficient radius is attained in every zero gap

*Lemma (reviewer's proof).* Fix \(t\), a space \(V\), an injective
measurement \(M\) on \(V\), and consecutive simple real zeros \(z<z'\) of
\(H_\theta(t,\cdot)\). Suppose that on \([z,z']\) the matrix
\(A(x)=B_{t,x}QR^{-1}\) of Note 03 §2 has rank two and a simple largest
singular value, with left singular vector \(u_1(x)\) never vertical. Then
there is \(x_*\in(z,z')\) with \(r_M(t,x_*)=\eta(t,x_*)\), attained by the
perturbation along the top singular direction, the one that defines \(C\).

*Proof.* Writing \(A=\sigma_1u_1v_1^{\mathsf T}+\sigma_2u_2v_2^{\mathsf T}\),
\(r_M^2=(u_1\cdot h)^2/\sigma_1^2+(u_2\cdot h)^2/\sigma_2^2\) and
\(\eta^2=\|h\|^2/\sigma_1^2\), so \(r_M=\eta\) exactly when \(h\parallel u_1\).
Choose \(u_1\) continuously with positive first component and put
\(s(x)=(h_2u_{1,1}-h_1u_{1,2})/\|h\|\). At a simple zero,
\(h=(0,H_x)\neq0\) and \(s=\operatorname{sign}(H_x)\,u_{1,1}\); consecutive
simple zeros have opposite signs of \(H_x\). So \(s\) vanishes in
\((z,z')\). \(\square\)

The same argument with a single direction \(v\) gives an exact double jet
wherever \(h\parallel B_{t,x}v\), once per gap. Note 01 §3 lists a
one-dimensional space and a fixed finite height box as uncovered; the
lemma covers both, at one abscissa per gap rather than at every prescribed
abscissa. Claude's original record already called \(\eta\) "saturated in
direction only"; the lemma says the direction is met once per gap.

*Computation (C, floating).* For each replay point, in the zero gap of
\(H_\theta(t,\cdot)\) that contains it, the alignment abscissa \(x_*\) was
found by bracketing \(s\). Unanchored rows (anchored rows are in the
record):

| Listed point | Zero gap | \(x_*\) | \(\eta=r_M\) at \(x_*\), recurrence / reflection | \(\eta\) at listed point | \(r_M\) at listed point | Least coefficient of the recurrence minimizer at \(x_*\) |
| --- | --- | --- | --- | --- | --- | --- |
| \((0,30)\) | \((28.2695,42.0441)\) | 31.3170 | 8.9248 / 2.4165 | 7.9212 / 2.1448 | \(3.51\cdot10^8\) / \(2.27\cdot10^7\) | 0.99776 |
| \((0,44.1303)\) | \((42.0441,50.0217)\) | 44.2848 | 0.11439 / 0.030972 | 0.11403 / 0.030874 | 534308 / 34590 | 0.888 |
| \((\tfrac14,44.1303)\) | \((41.8558,49.8750)\) | 44.1060 | 0.12169 / 0.032950 | 0.12170 / 0.032953 | 83530 / 5407 | 0.881 |
| \((0,60)\) | \((50.0217,60.8498)\) | 52.6652 | 0.011976 / 0.0032427 | \(6.015\cdot10^{-4}\) / \(1.629\cdot10^{-4}\) | 48523 / 3141 | 0.999997 |
| \((0,70)\) | \((65.8701,75.1724)\) | 68.4895 | \(5.952\cdot10^{-5}\) / \(1.612\cdot10^{-5}\) | \(5.054\cdot10^{-5}\) / \(1.368\cdot10^{-5}\) | 1116 / 72.25 | 0.99999998 |
| \((0,85)\) | \((81.8374,86.6541)\) | 83.5129 | \(1.521\cdot10^{-7}\) / \(4.118\cdot10^{-8}\) | \(1.136\cdot10^{-7}\) / \(3.077\cdot10^{-8}\) | 5.908 / 0.3825 | 1 − \(1.5\cdot10^{-7}\) |

In all 24 combinations, anchored included, \(|r_M/\eta-1|\le2\cdot10^{-61}\)
at \(x_*\), the ratio \(\eta(x_*)/\eta(\text{listed})\) lies in
\([0.99992,25.36]\), and the frozen curvature \(H_{a,xx}(t,x_*)\) is
nonzero. At \((1/4,44.1060)\) the recurrence minimizer is a strictly
positive normalized theta-tail source at recurrence distance \(0.12169\)
with \(H_{a,xx}=-2.55\cdot10^{-7}\): a nondegenerate positive-time
collision, against the distance \(83530\) recorded at \(x=44.1303\). The
reflection-design minimizers are often not positive; positivity is not
part of \(r_M\).

*Consequences.*

- (a) Note 03's sentence "Small sufficient radii therefore do not measure
  nearby feasibility in these cases" is true at the prescribed abscissae
  and should say so. At the scale of one zero gap the reverse holds: the
  distance to a double jet somewhere in the gap lies between the least
  \(\eta\) on the gap and \(\eta(x_*)\), so the reply's table measures, to
  the factors above, what a fixed design can exclude within a gap.
- (b) The manuscript's §5 sentence "an exponentially small sufficient
  radius need not imply an exponentially small actual distance" is
  correct pointwise and needs the companion statement. The disposition row
  "Is \(\|h\|/C\) the distance to a double jet?" should read, in substance:
  at a prescribed abscissa, no, with replay gaps \(1.6\cdot10^5\)–\(3.1\cdot10^{11}\);
  within each zero gap, yes at one abscissa.
- (c) The 32-case positivity classification is likewise a property of the
  prescribed abscissae (D). Take, in the same two gaps, the abscissae at
  which the first-\(N\) Euclidean minimizer is aligned in the same sense.
  At \(t=0\) (gap \((50.02,60.85)\); \(x_*=52.6652\) unanchored, \(52.4832\)
  anchored) all seven nontrivial theta-tail classes are positive-feasible,
  the unanchored ones with coefficients
  \((0.999997,1.00876,1+5.6\cdot10^{-9},1,1,1)\). At \(t=1/4\)
  (\(x_*=44.1060\) unanchored) the four unanchored classes are
  positive-feasible, with \((1.0000306,0.910972,0.99999995,1,1,1)\) and a
  nondegenerate collision, while the anchored classes are not positive at
  their abscissa \(43.9361\) (\(a_3\approx-4.3\cdot10^5\)). Even \(N=2\),
  equality-infeasible at both prescribed points, has an exact positive
  solution at \(x_*\); the anchored \(N=2\) space is \(\{0\}\). A byproduct:
  a positive normalized source that differs from theta by 9% in \(a_2\),
  with a compensating \(3\cdot10^{-5}\) in \(a_1\), collides at \(T=1/4\),
  \(x\approx44.106\). It lies in the same reflection-breaking premise class
  as the weighted-square controls and screens nothing new, but it is far
  closer to theta than the three-square control.

## 4. Finding 2: every nonzero finite perturbation has non-real zeros at every heat time

*Proposition (reviewer's proof sketch; not in the round's notes).* Let
\(\Psi\ge0\) on \([0,\infty)\), \(\Psi\not\equiv0\), be either theta's source
plus a nonzero finite combination \(f=\sum_{n\le N}c_n\phi_n\) (the
theta-tail class) or such a finite combination itself (the zero-tail
class), and let \(H_\Psi(t,x)=\int_0^\infty e^{tu^2}\Psi(u)\cos(xu)\,du\).
Then for every real \(t\), \(H_\Psi(t,\cdot)\) has only finitely many real
zeros and infinitely many non-real zeros. In particular its de
Bruijn–Newman constant is \(+\infty\).

*Proof sketch.* (i) By Lemma 2.1 there is a least odd order \(2k+1\) with
\(f^{(2k+1)}(0)\ne0\), and by Lemma 2.2
\(H_f(t,x)=(-1)^{k+1}f^{(2k+1)}(0)x^{-2k-2}(1+O_t(x^{-2}))\), with leading
coefficient independent of \(t\). Theta's jet, when present, is
\(O_t(x^{-K})\) for every \(K\) (manuscript (3)). So \(H_\Psi(t,x)\ne0\) for
\(|x|\ge x_0(t)\), and the nonzero entire function has finitely many zeros
in \([-x_0,x_0]\). (ii) Let \(n_0\) be the least index with a nonzero
coefficient \(a_{n_0}\); it dominates at \(u\to+\infty\), so
\(a_{n_0}>0\), and since \(2q^2-3q\ge q^2\) for \(q\ge3\),
\(\Psi(u)\ge\tfrac12a_{n_0}\lambda_{n_0}^2e^{9u-\lambda_{n_0}e^{4u}}\) for
large \(u\). Integrating over a unit interval ending at
\(u_y=\tfrac14\log(y/4\lambda_{n_0})\) gives
\(H_\Psi(t,iy)\ge\exp\{\tfrac y4\log y-O(y)\}\) as \(y\to\infty\), while
\(|H_\Psi(t,z)|\le\exp\{O(|z|\log|z|)\}\). So \(H_\Psi(t,\cdot)\) has order one
and infinite type. By Hadamard's theorem an entire function of order one
with finitely many zeros is \(P(z)e^{\alpha z+\beta}\), of finite type;
hence there are infinitely many zeros, all but finitely many non-real.
\(\square\)

*Explicit height (H, interval arithmetic).* For \(\delta=\varepsilon A\),
with Note 05's direction \(A\), leading coefficient \(a\) and constant
\(E_A\), and Note 02's envelope,
\(|\varepsilon H_A(t,x)|\ge|\varepsilon|(|a|x^{-2}-E_Ax^{-4})>\tfrac65e^{-\pi x/16}\ge|H_\theta(t,x)|\)
for all \(x\ge X\) and \(0\le t\le1/4\), with \(X=264\) when
\(|\varepsilon|=10^{-16}\) and \(X=269\) when
\(\|M_{\rm rec}\varepsilon A\|_2=10^{-16}\) (\(\|M_{\rm rec}A\|_2=2.4501\)).
The ratio is increasing beyond \(X\), by a log-derivative bound recorded in
the program. So a perturbation that sixteen-digit recurrence measurements
cannot see removes every real zero above height 269, at every heat time
up to \(1/4\).

*Illustration (floating, preregistered).* The plan allows "at most one
additional, preregistered threshold check". Its contract, fixed in the
program before evaluation: \(t=0\), \(\varepsilon=\pm10^{-16}/\|M_{\rm rec}A\|_2\),
sign changes of \(H_\theta+\varepsilon H_A\) on \([100,300]\) at step
\(1/20\). Theta has 42 sign changes there; the two perturbed functions have
8 and 9, the last near \(x=143.5\) and \(x=147.3\). A close pair can be
missed near the crossover, not beyond it.

*Consequences.*

- (a) Corollary 5.1 holds for \(\dim V\ge1\), in the stronger form "every
  nonzero member of the class has non-real zeros at every heat time". The
  hypothesis \(\dim V\ge2\) is needed only for double jets at a prescribed
  \((t,x)\), which is what Theorem 1.1 asserts.
- (b) The phenomenon behind the reply's "a design fed with sixteen-digit
  measurements guarantees nothing above \(x\approx140\)" occurs at that
  scale: proved above 269 with the present envelope and seen near 145. As
  a statement about \(\eta\) the figure remains an unverified
  extrapolation, and I would record it as unverified rather than as wrong.
- (c) The canonical three- and four-square controls are finite nonnegative
  combs with a nonzero third or fifth source derivative at the origin, so
  they also have \(\Lambda=+\infty\); their certified events at \(T=1/4\)
  and \(T=1/100\) are two among infinitely many. The screening statements
  of [summary 12](../../../../result-summaries/12_collision_controls_and_screening.md)
  remain true; one line there would stop the controls being read as having
  a finite constant near those times.
- (d) Theorem 1.1 remains the only statement placing collisions at a
  chosen \((t,x)\), and 3915 its only explicit onset; both are correct and
  secondary to (a).

*Context, from memory and not fetched today.* The algebraic endpoint
expansion of a one-sided Fourier integral is standard asymptotics; de
Bruijn (1950) and Newman (1976) set up \(\Lambda\) and allow the value
\(+\infty\). The manuscript claims no novelty; citing these in its
introduction, after checking the statements against the printed papers,
would place Lemma 2.2 and the remark above correctly
([avoid 16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md)).

## 5. Smaller mathematical and expository points

1. **The three-square bracket (E).** For the normalized three-weight
   zero-tail problem at \(t=1/4\), \(\Phi_a'(0)=+6.2585\cdot10^{-6}\) at
   \(x=44.1303\) and \(-8.0715\cdot10^{-6}\) at \(44.1304\); its root is
   \(x=44.13034367\), where the solution rescaled to \(a_1=1\) is
   \((1,\,0.8791733,\,57742.495)\) with normalizing factor \(1.0000347152\)
   and \(\Phi'''(0)=-39.9924\), inside every interval of the certified table
   of 22 Note 05/01. So Reply 03 §2's "reproduces the three-square control"
   holds up to the abscissa inside the bracket, which the reply itself
   attributed the difference to, and Note 03's caution is right at the
   bracket endpoint. The manuscript sentence "The nearby positive replay
   source is not the canonical three-square control" should add that the
   same family meets the control at its interior root.
2. **What sets 3915.** Sampled true \(L^1\) norms, at \(t=0\) and
   \(t=1/4\), are 10 to 340 times smaller than the majorants (F):
   \(\|g_A^{(4)}\|_1\approx42.3\) against \(703\),
   \(\|(ug_A)^{(5)}\|_1\approx171\) against \(58446\). With the sampled norms
   in place of the majorants the determinant threshold would be about 397
   (floating, not a bound).
   The step \(u^j\le j!e^u\) and the half-rate envelope set the number, not
   the determinant structure. I agree with Note 05 that no tuning is
   warranted; an explicit carrier-rate envelope would matter only to a
   consumer the portfolio does not have.
3. **The setup review's proposition.** Item 4 of the portfolio setup
   review's §8 left the carrier-rate envelope "to be supplied from
   Polymath's effective approximation". The round instead proved an
   unconditional envelope at half the rate. That choice is sound and
   should be recorded as the resolution of item 4.
4. **Wording.** In the manuscript's control table, "Its third odd derivative
   is nonzero" reads as the third of the odd derivatives; "its third
   derivative at the origin" is meant (similarly for "fifth"). The
   super-Gaussian row's \(\log\Phi_*=-u^4+O(u^3)\) matches 22 Note 05/04.
   Theorem 1.1 restricts to \(V\subset\ker\beta^{\mathsf T}\); Notes 01 and
   04 allow any homogeneous constraints, which is harmless.

## 6. Records, reproducibility and conventions

1. **Certificate bytes.** The replay reproduces every enclosure, but the
   runtime fields `python_version` and `elapsed_seconds` inside
   `CERTIFIED_EVALUATION.json` change its bytes, and its SHA-256 is then
   embedded in three other certificates and the summary. A replay therefore
   cannot match the committed hashes even when every ball agrees. The
   content-hash convention of [LARGE_FILES.md](../../../../LARGE_FILES.md)
   §1.3 would fix this: hash the enclosures, or keep runtime fields only in
   the summary.
2. **Memory units.** `run_replay.py` stores `ru_maxrss` as
   `largest_child_peak_rss_bytes`; on Linux the value is in KiB (32976 in
   my run, about 32 MiB). `concrete_onset_budget.py` already converts.
3. **Compiled PDF.** `manuscript/source_measurement_audit.pdf` is tracked,
   as in four sibling projects, and the manuscript README says to keep it.
   The project convention stated in October is to store only the `.tex`
   source; `LARGE_FILES.md` still lists PDFs among tracked sources. This is
   Edward's decision; if the `.tex`-only rule stands, the PDF and that
   README sentence change.
4. **Scope discipline.** The round kept its contract: no height grid, no
   support sweep and no run at \(x=140\); Notes 04–05 added analytic
   content rather than computation; the manuscript was requested by Edward
   and says it is unreviewed
   ([avoid 10](../../../../avoid/10_numerics_ahead_of_the_question.md),
   [avoid 20](../../../../avoid/20_volume_without_a_gain.md)). The only
   extra evaluation in this review is the preregistered check of §4 that
   the plan allows.
5. **Attribution and status words** are consistent throughout: the actual
   model and effort are recorded, same-model collaborators are labelled as
   such, and "sufficient", "floating" and "working draft" are used
   correctly. No assertion count is offered as evidence
   ([avoid 04](../../../../avoid/04_counts_and_precision_as_evidence.md)).
   The README, notes index and manuscript accurately say the round is
   active and unreviewed.
6. **After reconciliation** the README status line, the round index, the
   manuscript README, the draft history and the portfolio README row need
   the outcome; I have added only this review's row to the reviews index.

## 7. Disposition and recommendations

**Reply 03 §§1–2, after round one and this review.**

| Claim in Reply 03 | Disposition |
| --- | --- |
| Item 1: every nonzero finite perturbation has an algebraic jet | Correct (Lemmas 2.1–2.2), with the least index taken over the space |
| Item 2: \(\eta\le C'\|M\|x^{2k_0+15/4}e^{-\pi x/8}e^{tL^2/16}\) | Inequality direction correct; the jet bound imported an unquantified convexity factor. Proved replacement: \(\eta\le\tfrac65e^{-\pi x/16}/C\) with \(C=A_Mx^{-p}(1+O(x^{-2}))\) (Note 01 (3), Note 02 (1)) |
| Item 3: the relative constant grows like \(X^{-A}e^{\pi X/8}\) | Correct as an asymptotic with \(A=p+7/4\), now proved (Note 02 (12)); the reply had only the lower bound |
| \(\eta\) is "the measurement defect below which no collision can be created inside \(V\) at \((t,x)\)" | Correct as a pointwise sufficient radius; within each zero gap it is also the actual distance (§3) |
| The numbers of section B | Reproduced: \(C\) to about \(1.6\cdot10^{-11}\), the jet at \(x=85\) to \(1.1\cdot10^{-5}\) |
| "No coverage above \(x\approx140\) at sixteen digits" | As a statement about \(\eta\): unverified extrapolation. The underlying loss of all real zeros under a perturbation invisible at that accuracy: proved above 269, seen near 145 (§4) |
| §2: the repaired experiment reproduces the three-square control and nothing else | Correct up to the abscissa inside the bracket (§5.1). Its statements that no positive collision source exists "at these points" are correct and are prescribed-abscissa facts: at alignment abscissae of the same gaps positive theta-tail collision sources exist (§3(c)). They are generic linear algebra in the same premise class, which supports "nothing else" in the reply's structural sense |
| "I would not run the pilot as a research step" | The round ran it as the cross-model check the reply allowed. With §§3–4 the question is answered and the computation should stop |

**Repaired proposition (consolidating Notes 01–05 and §§3–4).** Let \(V\)
be a nonzero fixed space of finite-support perturbations with its linear
constraints built in, \(M\) a fixed measurement injective on \(V\), \(q\)
the least index with \(\ell_q\not\equiv0\) on \(V\), \(p=2q+2\) and
\(A_M=\sup|\ell_q(\delta)|/\|M\delta\|\).

- (a) Uniformly on bounded heat times, \(C(t,x)=A_Mx^{-p}(1+O(x^{-2}))\);
  for \(0\le t\le1/4\), \(\|h(t,x)\|\le\tfrac65e^{-\pi x/16}\); hence
  \(\eta(t,x)\le\tfrac65A_M^{-1}x^pe^{-\pi x/16}(1+O(x^{-2}))\). [Notes 01–02]
- (b) In every gap between consecutive simple real zeros of
  \(H_\theta(t,\cdot)\) on which the jet map has rank two with a simple top
  singular value, \(r_M=\eta\) at some abscissa. [§3]
- (c) Every nonzero \(\delta\in V\) with positive coefficients gives a
  source with finitely many real and infinitely many non-real zeros at
  every heat time. Along the normalized unanchored direction \(A\), a change
  of \(10^{-16}\) removes all real zeros above 264 for \(0\le t\le1/4\).
  [§4]
- (d) If \(\dim V\ge2\), exact positive double jets exist at every
  prescribed \((t,x)\) with \(x\) beyond a space-dependent height, with
  changes \(O(x^{-K})\) for every \(K\), nondegenerate at each fixed
  \(t>0\) outside a discrete set; for the normalized unanchored
  three-coordinate space the height is at most 3915 and the change below
  \(4\cdot10^{-307}\). [Notes 01, 04, 05]
- (e) Nothing transfers to theta: all of this concerns sources that fail
  exact reflection, and \(\|B\delta\|\le C\|M\delta\|\) carries
  nonvanishing from theta's jet to its neighbours, never back.

**Recommendations for the one reconciliation (Codex), then closeout.**

- R1. Test the gap lemma. If it is accepted, add "at the prescribed
  abscissa" to Note 03's summary paragraph and §4, to the manuscript
  abstract, §5, the disposition row and the captions of Tables 1–2, with a
  pointer to this review rather than a silent edit.
- R2. Test the non-reality proposition. If it is accepted, add it as a
  remark after Corollary 5.1, relax that corollary to \(\dim V\ge1\), and
  add a disposition row.
- R3. Add the bracket sentence of §5.1, and record the \(x\approx140\)
  disposition as in the table above.
- R4. Fix §6.1–6.2; Edward to decide §6.3.
- R5. Close round one after the reconciliation, and close the project
  through the plan's closeout gate: a current README, a concise history,
  the exact class (fixed finite measurement designs, absolute errors,
  finite reflection-breaking coefficient classes), and the reopening
  input (a consumer that needs a fixed-design statement on a
  reflection-preserving or infinite-dimensional class, or an explicit
  carrier-rate envelope). No round two; the plan's own stopping rule
  says an inconclusive result is no reason to extend the grid, and this
  result is conclusive.
- R6. At closeout, add a short entry to result summary 12 or 14 in the
  source's status words ("proved in-note; cross-model LLM review; no
  specialist review"), and a candidate line for
  [avoid 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
  or [09](../../../../avoid/09_round_floors_and_fitted_laws.md): a
  distance computed at prescribed generic abscissae read as the distance
  to an event within the region, with Note 03 and this review as the
  evidence.

For the portfolio the outcome is the one the plan anticipated, now with
proofs: in the stated class, fixed finite measurements cannot exclude
collisions or non-real zeros at large height, because every nonnegative
source in the class other than theta itself has \(\Lambda=+\infty\).
Nothing here closes exact
source identification, reflection-preserving or infinite-dimensional
classes, height-dependent designs, or comparison-source transfers.
Projects 04 and 05 do not depend on this outcome.

## Appendix A. Artifact digests at review (SHA-256, first 16 hex digits)

| File | Digest |
| --- | --- |
| `README.md` | `458794727e6204e7` |
| `DRAFT_HISTORY.md` | `cdd859a7fbab9059` |
| `research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md` | `4a764bbde6d157ee` |
| `research-overview/02_ROUND_BASED_EXECUTION_PLAN_20261017.md` | `57ff30f4dfcc94a7` |
| `notes/round-1/01_OPENING_ANALYTIC_AUDIT_AND_REPLAY_CONTRACT_CODEX_20261016.md` | `943d8f54a5b27131` |
| `notes/round-1/02_EXPLICIT_THETA_JET_AND_ENDPOINT_BOUNDS_CODEX_20261017.md` | `30157a0c589de6c7` |
| `notes/round-1/03_BOUNDED_REPLAY_AND_POSITIVE_FEASIBILITY_CODEX_20261017.md` | `807b361dd664188d` |
| `notes/round-1/04_NONDEGENERATE_FINITE_SOURCE_COLLISIONS_CODEX_20261017.md` | `b27a50bc72d949c6` |
| `notes/round-1/05_CONCRETE_NORMALIZED_ONSET_BUDGET_CODEX_20261017.md` | `5c7e7bf1b0adfe9f` |
| `manuscript/source_measurement_audit.tex` | `12928d08b62bd048` |
| `manuscript/source_measurement_audit.pdf` | `56210a3c541c1076` |
| `numerics/round-1/CERTIFIED_EVALUATION.json` | `5bad95e1a3f1a899` |
| `numerics/round-1/CERTIFIED_MEASUREMENTS.json` | `05ab2930c38a85e4` |
| `numerics/round-1/CERTIFIED_FEASIBILITY.json` | `d46917c0c2c446c4` |
| `numerics/round-1/FEASIBILITY_WITNESSES.json` | `6f043d1ba760f1fb` |
| `numerics/round-1/ANALYTIC_BOUND_CHECKS.json` | `a342f701fd504406` |
| `numerics/round-1/CONCRETE_ONSET_BUDGET.json` | `0918273f5c834c4b` |
| `numerics/round-1/REPLAY_SUMMARY.json` | `01294f6abebe18e4` |
| `numerics/round-1/concrete_onset_budget.py` | `50cf6d703e3f7d07` |
| Reply 03 / original solver / original record | `0871fb3829301bd2` / `b5d9d9c5c45ae329` / `3a9e555cafa456a5` |

The seven replay programs match the digests in `REPLAY_SUMMARY.json`. The
full digests of the committed records are repeated in the review record.

## Appendix B. Computations

The review program's record states its own SHA-256, environment and
runtime. Sections: A jets (6 points), B conditioning (24), C alignment
(24 roots in 6 gaps), D theta-tail feasibility at alignment (16), P
prescribed classification (32), E three-square bracket, F Note 05
constants and remainder tests, G envelope constants (interval), H
non-reality heights (interval) and the preregistered illustration. Run
from the folder of the program with
`python3 -I review_checks_claude_20261017.py --output OUT.json --committed-dir ../`;
the full run takes about 20 minutes on one core. The replay re-run of §2
used the round's own command lines and wrote outside the checkout.
