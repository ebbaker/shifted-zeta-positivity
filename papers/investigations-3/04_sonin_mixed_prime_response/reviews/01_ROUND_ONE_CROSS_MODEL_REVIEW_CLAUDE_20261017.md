# Round-one cross-model review of the Sonin mixed-prime response

17 October 2026, America/New_York. Prepared for Edward Baker with LLM
assistance. Model: Claude Opus 5.5 (configured identifier
`claude-opus-5-5`), Claude Cowork, reasoning effort max; the serving model
may differ from the configured identifier. This is a cross-model LLM review
of [round one](../notes/round-1/README.md) of Project 04, recorded by
**gpt-6.1-sol (Codex)**, effort **ultra**: Notes 01–02, committed at
`4929ce1`, and the requested
[working manuscript](../manuscript/sonin_mixed_prime_response.tex),
committed at `74eb892`, all unchanged at HEAD `b864142`. It is not
independent specialist review, and no subagents were used.

One caveat on independence. The claim this round was opened to test, that
accumulated mixed responses are "the Weil form on the span of the
\(G\)-translates of the prepared source", is Claude's
([Reply 03](../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md)
§5, Claude Fable 5.1), and the
[setup review](../../reviews/01_PORTFOLIO_SETUP_REVIEW_CLAUDE_20261016.md)
(Claude) asked in its change C7 for the two controls that Note 01 supplies.
On the reconciliation of that claim this review is same-family with its
author ([avoid 05](../../../../avoid/05_same_model_reviews_and_shared_premises.md)).
It withdraws the claim (§3), with a proof sketch and with checks that can
fail. Every statement below is labelled as a verification of the round's
text, a proof sketch by the reviewer, an exact or floating computation, a
literature reading, or a recommendation. Nothing here bears on the zeros of
zeta.

**Summary.** I found no mathematical error in Notes 01–02 or in the
manuscript, and one expository slip (§7). The round's operator identities
hold exactly in rational finite models; its boundary-to-source kernel
identity holds exactly by three independent routes; its gamma asymptotic
agrees with direct quadrature to \(2\cdot10^{-7}\) at \(\tau\approx10^5\)
(§2). The proofs are careful, the inherited inputs are named, and every
negative statement is scoped. Three findings change how the round should be
read:

1. **The translate-span reading fails at first order, for one structural
   reason (§3).** Adding places moves the space; the translate-span picture
   moves the source. For every finite place set \(A\),
   \(B_{S\cup A}-B_S=-(W_{S\cup A}-W_S)+(K_{S\cup A}-K_S)\) is a bounded
   form on \(L^2(I_L)\), an explicit prime-power sum plus a compact boundary
   part, while \(B_S[J_AF]-B_S[F]\) carries shifted gamma terms that are
   unbounded as soon as one of their shifts is shorter than \(L\). The
   inverse metric exists to cancel them. Already for one prime with
   \(\log p<L\), the metric correction is
   \(Z_p[F_\tau]=\beta_p\kappa_h(\log p)\cos(\tau\log p)\log\tau+O(1)\).
   Theorem 5.1 is the second-order case, and its hypothesis
   \(L>|\log(p/q)|\) is sharp (§4). I withdraw Reply 03's identification.
2. **Phase 2 has no candidate (§5).** The proposal gives Claude the next
   step, one bound on the actual source. I have none that passes its gate.
   At a fixed window the mixed response enters \(Q=B_A-K_A\) only as one of
   four terms of \(K_A\), which the same transfer theorem and the same
   base-space data give whole; along the support-adapted family, mixed
   responses of every order enter with condition factors \((u/\ell)^2\)
   that reach \(10^{68.6}\) at \(L=10\); and the one a priori bound that
   (10) yields is generic. The proposal's stopping condition is met.
3. **The verification contract is correct and expensive (§6).** With the
   inherited gap bounds, Proposition 7.1 multiplies the boundary
   approximation error by about \(4.8\cdot10^{10}\) at the final corner of
   the first pair. In an exact instance the bound is attained to within
   \(10^{-13}\), so the factor is the conditioning of \(C(I-C^2)^{-1}\) near
   the top of its spectrum, not slack in the bound. Nothing consumes the
   enclosure, so I would not run it.

**Disposition (§9).** Accept the round as correct, with the edits of §7.
Phase 1 passes its acceptance criterion. Close the opening phase and make
Project 04 dormant, with the scoped disposition and reopening input of §9;
this is what the round's commit message anticipates. The manuscript is an
accurate working record, but in its present framing I do not think it
passes the portfolio's Manuscript gate. Its reusable content is the compact
transfer theorem and the place-change identity of §3.2.

## 1. Scope, artifacts and method

**Read in full.** Notes 01–02 and the round README; the manuscript source
and README; the project README, draft history, proposal and folder READMEs;
the project chat record (history 1). For context: all of
[`avoid/`](../../../../avoid/README.md) and
[`result-summaries/`](../../../../result-summaries/README.md), including the
17 October lines that point at this round (avoid 12, summary 07); the
[portfolio plan](../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md)
and README; the setup review's §5 and change C7; Reply 03 §§5 and 10; and
the inherited sources the round builds on, the
[finite Euler identity](../../../investigations/sonin-critical-boundary/notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md),
the [canonical comparison audit](../../../weil-positivity/susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md),
the [place-addition note](../../../weil-positivity/susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_PLACE_ADDITION_AND_ERROR_CONTROL_20260929.md),
the [closed-source comparison](../../../investigations/sonin-critical-boundary/notes/CLOSED_SOURCE_RELATIVE_COMPARISON_20261003.md)
and the [compact-correction note](../../../investigations/sonin-critical-boundary/notes/COMPACT_CORRECTION_AND_REVISED_B_20261003.md).

**Checks.** [`claude-review/`](../numerics/round-1/claude-review/README.md)
holds one standard-library program and its record. Sections B, C and E and
the identities of D are exact rational arithmetic; the operator norms of D
and sections F–G are floating. The finite models check the operator
algebra, which holds for any commuting unitaries, positive source operator
and projection. No finite model contains the actual Sonin projection, so
these sections test the bookkeeping, and the analytic statements rest on the
proofs, which I checked by hand, and on the inherited inputs. The program
has negative controls (a dropped inverse metric, a sign flip in (11), a
missing factor two, an unreflected output) that must fail and do, and it
exits nonzero on any failure
([avoid 11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)).
It replays on Edward's machine (Python 3.10.12) identically in every exact
field.

**Literature fetched today.** Connes–Consani–Moscovici, arXiv:2310.18423v2
(PDF): Theorem 4.6 states that \(\theta_S\) is a "hilbertian isomorphism of
the Sonin spaces", a footnote uses "hilbertian" for "the underlying
topological vector space structure of a Hilbert space", and §4.8 says that
"the choice of the finite set S plays a key role in fixing the inner
product". Equation (57) carries the multiplier
\(\prod_{p\in S\setminus\{\infty\}}(1-p^{-1/2-is})\) (the extraction is
garbled but legible). This supports the round's reading, "Stability does
not remove \(M_A^{-1}\)". The journal reference, Ann. Funct. Anal. 15
(2024), no. 4, Paper 87, is confirmed by the Springer record. For
Connes–Consani, Selecta Math. (N.S.) 27, no. 4 (2021), is confirmed by
Consani's publication list; the article number 77 and the DOI in the
manuscript's bibliography were not confirmed in a fetched source. DLMF
5.11.2 was read as quoted.

## 2. What was verified

N01 and N02 are the round's notes and MS the manuscript; equation numbers
are those of the cited file. "Exact" means rational arithmetic in the finite
models of sections B–E.

| Claim | Where | Check |
| --- | --- | --- |
| One source \(F=\mathcal Ah\) at all four corners; actual projections \(\Pi_A=\mathscr D_A\Pi_\infty M_A^{-1}\Pi_\infty\mathscr D_A^*\), inverses on \(\mathcal K_\infty\) | N01 §1, MS §1 | Verified against the canonical audit (13)–(14) and the finite Euler note (7); the source is not renormalized between corners (the proposal's phase-0 check) |
| Four traces (8) by the transported isometry; scalar normalizations cancel | N01 (8), MS Thm 2.1 | Verified; exact against directly computed projections in four models |
| Mixed formula (10) and resolvent step (11) | N01 (10)–(11) | Verified; exact; the dropped-inverse and sign-flip variants fail |
| Defects (12) and return (13); \(a,b\) need not commute | N01 (12)–(13) | Verified; exact, with \([a,b]\ne0\) and \(c-ab\ne0\) in every model; in a commuting-projection model every increment vanishes |
| \(\mathfrak M=\Delta_p\Delta_qK_S\); complete and partial residuals | N01 (14)–(16), MS (2.4) | Verified (\(\Gamma\) fixed, \(W\) additive); this is the identity of the setup review's C7, recorded as asked |
| Modulated family exactly prepared; conjugation identity (19); \(K_A[F_\tau]\to0\) | N01 §4 | Verified, including \(\mathcal A(e^{i\tau x}h)=e^{i\tau x}(\tau^2h-2i\tau h'+\mathcal Ah)\) and the conjugate-source term of (19) |
| Literal translate obstruction (20)–(22); linear independence; \(\Gamma[H_\tau]=(\log\tau)\|H_\tau\|_2^2+O(1)\) | N01 §5, MS Prop 6.1 | Verified; diagonal check \(\Gamma[F_\tau]/\|h\|_2^2-(\log\tau-\log2\pi)=8\cdot10^{-7}\) at \(\tau\approx10^5\) (F). Simplification in §4 |
| Bare-sample statement | N01 §5, MS §6 | Verified (Bohr means of an almost-periodic function that tends to zero) |
| Two-dimensional control (23); \(z_2,z_3>0\) | N01 §6, MS §8 | Verified exactly with rational stand-ins, and at the actual weights: \(z_2=0.942809=\beta_2\), \(z_3=0.704104\), \(\mathfrak M=\pm0.328542\). Refinement in §7 |
| Normalized transport (4); mixed numerators \(E_pE_q\); coefficient (5); eigenvalues \(0,\pm\beta_p\beta_q/(2\sqrt2)\) | N02 (2)–(7), MS Thm 4.1 | Verified; exact; characteristic polynomial \(\lambda^3-2w^2\lambda\) exactly |
| Corrected identity (9) and second description (10) | N02 (9)–(10), MS (4.2)–(4.3) | Verified (linearity of \(\mathcal G_T\) in \(T\)) |
| Gamma asymptotic (12)–(13), \(c_h=\tfrac12\beta_p\beta_q\kappa_h(a_-)\) | N02 §3, MS Thm 5.1 | Verified; quadrature gives \(\mathcal G_\Gamma[F_\tau]=c_h(\log\tau-\log2\pi)\cos(\tau a_-)\) to \(1.7\cdot10^{-7}\) at \(\tau\approx10^5\), with both signs, and the \(a_+\) part at rounding level (F) |
| First pair: coefficient \(\sqrt6/6\); \(a_-<6/5<a_+\); active primes \(\{2,3\}\) | N02 §3, MS §5 | Verified; \((\beta_2\beta_3/2)^2=1/6\) exactly |
| Crossing bound (15) | N02 (15), MS Lemma 3.1 | Verified (Hilbert–Schmidt factorization, \(a+b=L\|F\|_2^2\)); expository slip in MS, §7 |
| Compact transfer (16)–(19); no factor two in \(k_N\) | N02 §4, MS Thm 3.2 | Verified; (18) exactly by three routes with a complex source, each \(17208319/7983360\); the orientation and factor-two variants fail |
| Resolvent bound (21) | N02 (21), MS Prop 7.1 | Verified; the identity exactly; the bound in three instances, attained to \(1+7\cdot10^{-14}\) in one |
| Kernel discretization (22), enclosures (23)–(24), role of the complement | N02 §5, MS (7.3)–(7.4) | Verified (Schur bound; the compressed finite-rank operator vanishes on an infinite-dimensional complement) |
| Connes–Consani–Moscovici citations | N01 §1, MS §1 and bibliography | Read in the fetched PDF (§1) |

## 3. Finding 1: the translate-span reading fails at first order

### 3.1 The claim and what survives of it

Reply 03 §5 said that the mixed term "is the source autocorrelation sampled
at \(\pm\log p\pm\log q\) through the compressed metric. That is a definite
formula", and that "Accumulated over a group \(G\) of primes it is the Weil
form on the span of the \(G\)-translates of the prepared source". Note 02 (7)
makes the first sentence exact,
\(\mathfrak M=\mathcal G_{B_S}+\mathcal R_{\rm met}\): \(\mathcal G_{B_S}\)
contracts the \(B_S\)-Gram entries at the four shifts, and
\(\mathcal R_{\rm met}\) is "through the compressed metric". Theorem 5.1
shows that \(\mathcal R_{\rm met}\) is not a correction to
\(\mathcal G_{B_S}\) but cancels its principal part, and Proposition 6.1
shows that the second sentence is false as a literal identity. Both results
are correct.

### 3.2 The reason, at every order

What follows reorganizes the finite Euler identity and Theorem 3.2, both of
which the round uses (reviewer's arrangement; the two facts are the
round's). For a finite prime set \(A\) disjoint from \(S\), write
\(J_A=\prod_{j\in A}J_j\) and \(E_C=\prod_{j\in C}E_j\).

- **Moving the space.** \(B_{S\cup A}[F]-B_S[F]=-(W_{S\cup A}-W_S)[F]+(K_{S\cup A}-K_S)[F]\).
  The first term is a finite prime-power form, bounded by a constant times
  \(\|F\|_2^2\); the second is the form of \(Y_{S\cup A}-Y_S\), compact by
  Theorem 3.2. Every change of the place set is a bounded form on
  \(L^2(I_L)\) with no gamma sector.
- **Moving the source.** \(B_S[J_AF]-B_S[F]=\sum_{\emptyset\ne C\subseteq A}\operatorname{Tr}(V^*E_CV)\),
  since \(J_A^*J_A=\prod_{j\in A}(I+E_j)\). Each term is a combination of
  \(B_S(F,U_aF)\) over the shifts \(a=\sum_{j\in C}\pm\log j\), which are
  distinct by unique factorization, and the gamma part of
  \(B_S(F,U_aF)\) is unbounded with both signs on prepared sources as soon
  as \(|a|<L\) (the computation of N02 (12)).
- **The metric correction is the difference.**
  \(Z_A=(B_{S\cup A}-B_S)-(B_S[J_AF]-B_S[F])\) must cancel the shifted
  gamma terms that moving the source introduces.

The "Weil form on the span of the translates" belongs to the second object:
\(B_S[J_GF]=Q[J_GF]+W_{\notin S}[J_GF]+K_S[J_GF]\). The finite-place trace is
the first. They differ by an unbounded amount already for one prime.

**Proposition R1 (reviewer; proof sketch).** Fix \(S\), a prime
\(p\notin S\) with \(\log p<L\), a real nonnegative
\(h\in C_c^\infty(I_L)\) with support diameter in \((\log p,L)\), and the
prepared family \(F_\tau\) of N02 (11). Then
\(B_{S\cup\{p\}}[F_\tau]-B_S[F_\tau]=O(1)\), while
\[
B_S[J_pF_\tau]-B_S[F_\tau]=-\beta_p\kappa_h(\log p)\cos(\tau\log p)\log\tau+O(1),
\qquad
Z_p[F_\tau]=\beta_p\kappa_h(\log p)\cos(\tau\log p)\log\tau+O(1).
\]
*Sketch.* The first difference is \(-w_p+\Delta_pK_S\), a bounded
prime-power form plus a compact form, on a bounded family. The second is
\(\operatorname{Tr}V^*E_pV=-\beta_p\Re B_S(F,U_{\log p}F)\); polarize
\(B_S=\Gamma-W_S+K_S\) on the support hull of length \(L+\log p\), where
the \(W_S\) and \(K_S\) parts are bounded, and apply the computation of N02
(12) to the single shift \(\log p\). \(\square\)

Section F checks the gamma part with a box-spline bump centred at
\(\pm\tfrac12\log2\), for which \(\kappa_h(\log2)/\|h\|_2^2=1/2\): at
\(\tau\approx10^5\) it is \(\pm4.5609\) on sources whose norms tend to
\(\|h\|_2\), against the prediction to \(6\cdot10^{-7}\). In the exact
models, the commuting-projection case has
\(\mathcal R_{\rm met}=-\mathcal G_{B_S}=-1920/841\) with every increment
zero, and the four generic models have the two pieces of comparable size
and opposite sign around a smaller mixed response (for example \(0.7822\),
\(-0.7795\) and \(0.0026\)). The decomposition of N02 (7) splits an object
that vanishes for a translation-invariant base space into two that do not.

So the reply's picture, transport the source and correct by the metric,
does not describe the finite-place trace at any order once a shift is
accessible, and Theorem 5.1 is its second-order instance. The correct form
of the reply's §5 is N01 (16): the mixed response is a second difference of
the boundary correction. As the Claude reconciliation I withdraw the reply's
identification; §9 proposes the pointer that the
[redaction checklist](../../../../early-chat-logs/initial-project-files/rh3/REDACTION_CHECKLIST.md)
asks for. I did not find the first-order statement in the files I read. It
follows in a few lines from the round's Theorem 3.2 and the finite Euler
identity, and I make no priority claim for it.

## 4. Two sharpenings

**Proposition 6.1 needs only boundedness.** For any coefficients with
\(\sum_Ac_A=0\), the gamma terms cancel and
\(\sum_Ac_AB_{S\cup A}=-\sum_Ac_AW_{S\cup A}+\sum_Ac_AK_{S\cup A}\) is a
bounded form on \(L^2(I_L)\), whereas
\(Q[\sum_jc_jU_{t_j}F_\tau]\to+\infty\). So no single increment, mixed
difference of any order, or accumulation over a group equals the full Weil
form of a fixed nonzero translate combination. Compactness is needed only
for the note's bare-sample statement, which uses
\(\mathcal E[F_\tau]\to0\). Both obstructions are statements about order:
\(Q\) and \(\Gamma\) are logarithmic-order forms, place changes are bounded,
mixed differences are compact.

**Theorem 5.1 is sharp (reviewer; proof sketch).** For fixed \(S\) and
\(p\ne q\), \(\mathcal R_{\rm met}\) is a bounded form on \(L^2(I_L)\) if and
only if \(L\le|\log(p/q)|\). The forward direction is Theorem 5.1.
Conversely, suppose \(L\le a_-<a_+\). From
\(\psi(z)=-\gamma+\int_0^\infty(e^{-v}-e^{-zv})(1-e^{-v})^{-1}dv\), the
kernel of \(\gamma_\infty(D)\) away from the diagonal is
\(-e^{-|u|/2}/(1-e^{-2|u|})\), smooth and exponentially decaying, with a
\(-1/(2|u|)\) singularity at \(u=0\). For \(F\in C_c^\infty(I_L)\) the
supports of \(F\) and \(U_{a_\pm}F\) are at positive distance, so
\(\mathcal G_\Gamma\) has a smooth kernel there; uniformly in that distance,
the \(1/|u|\) bound and Hilbert's inequality (norm \(\pi\) for the kernel
\(1/(x+y)\) on the half-line) bound it, and it extends by density. With N02
(10), \(\mathcal R_{\rm met}=-\mathcal G_\Gamma+\mathcal G_{W_S}+(\text{compact})\)
is bounded. Section F illustrates this with a bump of diameter
\(0.3<a_-\): \(\mathcal G_\Gamma[F_\tau]\) stays at rounding level
(\(<4\cdot10^{-14}\)).

## 5. Finding 2: phase 2 has no candidate

The proposal assigns phase 2 to Claude: "Claude proposes one bound on the
actual arithmetic source, stating its support and place dependence", which
Codex then checks for "whether the hypothesis is weaker than the desired
positivity and whether the constant remains useful", with a margin chosen
in advance, "for example, a mixed contribution bound that reduces a named
residual budget on a declared finite support". I have no bound that passes
this gate, for three reasons.

1. **Fixed windows.** Once \(A=S\cup\{p,q\}\) contains the active primes,
   \(Q=B_A-K_A\) and \(K_A=K_S+\Delta_pK_S+\Delta_qK_S+\mathfrak M\). All
   four are compact forms with the same transfer theorem, and the
   base-space data that give \(\mathfrak M\) through (10) (\(\Pi_S\),
   \(E_p\), \(E_q\), \(A_F\)) give \(B_A\) through (8), hence \(K_A\),
   directly. A separate bound on \(\mathfrak M\) adds error terms and
   removes none, so by itself it cannot improve a fixed-window comparison.
   The intermediate corners do not satisfy \(Q=B-K\) and carry no budget of
   their own.
2. **Growing windows.** Along \(S_L=\{p\le e^L\}\), \(K_{S_L}\) is the sum
   over subsets of mixed differences of every order, and every fixed-place
   constant deteriorates with the condition factor
   \((u_{S_L}/\ell_{S_L})^2\) of the canonical audit (27): \(10^{4.2}\) at
   \(L=2\), \(10^{16.6}\) at \(L=6\), \(10^{68.6}\) at \(L=10\) (G). The
   estimate a pair bound would have to feed is \(K_{S_L}\le B_{S_L}\), the
   target itself ([avoid 01](../../../../avoid/01_restating_the_target.md)).
3. **The available bound is generic.** From (10), using only
   \(\|E_j\|\le\beta_j\) and the metric bounds,
   \[
   |\mathfrak M_{S;p,q}[F]|\le\frac{2\beta_p\beta_q}{(1-\beta_p)(1-\beta_q)}
   \Bigl(1+\frac{1+\beta_p}{1-\beta_p}+\frac{1+\beta_q}{1-\beta_q}\Bigr)B_S[F],
   \]
   about \(6\beta_p\beta_q\,B_S\) for large primes and
   \(1.04\cdot10^4\,B_S\) at \((2,3)\). It holds in every positive-matrix
   model (in all four exact models, with ratios from \(6\cdot10^{-7}\) to
   \(1.05\cdot10^{-4}\)), so it is the "generic positive-matrix argument"
   of the stopping rule.

The proposal says to stop "if the only proposed estimate is equivalent to
\(K_S\le B_S\), if a generic positive-matrix argument is the entire
mechanism, or if the fixed-support budget cannot improve after all return
terms are paid". Each applies in the sense just given. Reply 03 §10 set the
stop as "stop if it is Weil positivity on a translate span"; the mixed
response is not that, but the project stops anyway, for these reasons. The
reply's recorded prediction, "either generic operator algebra or that
target", is borne out in this scoped sense, with the identification it
rested on withdrawn. None of this is a theorem about collective prime
estimates ([avoid 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md));
§9 states what would reopen the question.

## 6. Finding 3: the verification contract and its cost

Proposition 7.1 is correct, and its proof needs no commutation. Its factor
\((1+cc_N)/((1-c_N^2)\sqrt g)\) is about \(2g^{-3/2}\) when \(c_N\approx c\)
and \(1-c^2\approx g\), and this is intrinsic: in the third instance of
section D, where \(C\) and \(C_N\) commute and \(g=2.5\cdot10^{-3}\), the
bound exceeds the actual error by a factor \(1+7\cdot10^{-14}\) and the
amplification is \(1.6\cdot10^4\). The derivative of \(c\mapsto c/(1-c^2)\)
near \(c=1\), times the singular values \(\sqrt g\) of \(T\), is the
reason.

With the inherited gap bounds \(g_A=(\ell_A/u_A)^2\cdot57\cdot10^{-6}\), whose
archimedean factor is the one the closed-source note §2 uses, the factors at
the four corners of the first pair are \(4.6\cdot10^6\) (\(\varnothing\)),
\(9.2\cdot10^8\) (\(\{2\}\)), \(2.4\cdot10^8\) (\(\{3\}\)) and
\(4.8\cdot10^{10}\) (\(\{2,3\}\)), and the a priori bound (16) is
\(|\mathfrak M|\le5.1\cdot10^3\|F\|_2^2\) at \(L=6/5\) (G; the \(\{2\}\) value
\(c/\sqrt g=771.993\ldots\) reproduces the closed-source note). For scale,
the complete form at that window is already certified at
\(Q\ge\tfrac3{2000}\|F\|_2^2\)
([summary 07](../../../../result-summaries/07_sonin_critical_boundary.md));
an enclosure of \(\mathfrak M\) at that resolution would need a final-corner
approximation error below about \(3\cdot10^{-14}\). The true gaps may be
larger than the inherited lower bounds, and the factors are what the
contract costs with the bounds on record. Since no budget consumes
\(\mathfrak M\) (§5), I recommend recording the contract as a scoped tool
with this cost and not running phase 3
([avoid 10](../../../../avoid/10_numerics_ahead_of_the_question.md)).

## 7. Smaller points

1. **MS Lemma 3.1, last step.** "Conjugating the source reverses the
   frequency multiplier and interchanges the two norms." Conjugation
   reverses the multiplier but leaves both
   \(\int(L/2\mp v)|F(v)|^2dv\) unchanged; reflection \(F(x)\mapsto F(-x)\)
   reverses it and interchanges them, which is what N02 and the
   closed-source note say. The bound is unaffected, since
   \(\sqrt{ab}\le\tfrac L2\|F\|_2^2\) either way.
2. **The two-dimensional control is degenerate at second order.** With the
   balanced projection onto \((1,1)/\sqrt2\), \(z_j\le\beta_j\), so
   \(|\mathfrak M|\le|d|\beta_p\beta_q(\beta_p+\beta_q)\), third order. In
   general (derived here; the limit is checked in exact arithmetic in
   sections B and C)
   \[
   \mathfrak M=\beta_p\beta_q\,\mu_2+O(\beta^3),\qquad
   \mu_2=\operatorname{Tr}\bigl(Pe_q(I-P)e_p(I-P)A_FP\bigr)
   -\operatorname{Tr}\bigl((Pe_pP)(Pe_q(I-P)A_FP)\bigr),
   \]
   with \(e_j=-\tfrac12(U_{\log j}+U_{\log j}^*)\). For a tilted unit vector
   \((c,s)\) in the two-dimensional control,
   \(\mu_2=-c^2s^2(s^2-c^2)(1-\cos\theta_p)(1-\cos\theta_q)(k_2-k_1)\),
   of either sign (C: \(\pm0.0929\) at \((3/5,4/5)\)); in an
   eight-dimensional model \(\mu_2=-0.02808\), symmetric in \(p,q\). The
   control's sign conclusion stands; its size is not representative, and one
   sentence, or the tilted version, would say so.
3. **N02 (12).** The remainder can be stated:
   \(\mathcal G_\Gamma[F_\tau]=c_h\cos(\tau a_-)(\log\tau-\log2\pi)+o(1)\),
   and numerically the \(o(1)\) is \(O(\tau^{-2})\) for the bump used.
   Likewise \(\gamma_\infty(t)=\log|t|-\log2\pi+O(t^{-2})\); the stated
   \(O(|t|^{-1})\) is correct but weaker.
4. **Whether \(\mathfrak M\not\equiv0\).** N01 §5 rightly does not assert
   it. For large primes the leading term is \(\beta_p\beta_q\mu_2\), a
   double-return trace; no current decision depends on it.
5. **MS §9 table.** "Both unbounded signs when \(L>|\log(p/q)|\)" can add
   "and bounded when \(L\le|\log(p/q)|\)" (§4).
6. **Bibliography.** Confirm the Selecta article number and DOI; the arXiv
   v2 title of Connes–Consani–Moscovici carries the subtitle "Semilocal
   adelic operators", and the journal title does not.

## 8. Records, reproducibility and conventions

1. **Claim discipline is good.** Each note separates inherited inputs,
   identities and scoped obstructions, names the premise each control
   lacks, and claims no numerics. The round reproduces cleanly from its
   text.
2. **Status files lag** ([avoid 19](../../../../avoid/19_status_files_that_lag_the_findings.md)).
   The project README and round README say "active round 1"; the
   research-overview README says "Current opening plan; not executed"; the
   portfolio README row says "One analytic calculation proposed"; the
   reviews README said "No project result has been reviewed yet" (I changed
   only its index row) and the numerics README "No computation has been
   performed" (I added a pointer to `claude-review/`).
3. **Draft history.** The entries cite the working tree, with baselines
   `b2a957e` and `4929ce1`. The notes are at `4929ce1` and the manuscript
   at `74eb892`, whose message reads "mostly negative results, will close
   if confirmed by review"; record the hashes.
4. **Process.** The proposal assigned the phase-0 and phase-1 checks and
   phase 2 to Claude. Round one ran without them, as the 17 October cadence
   allows, and was written up at Edward's request before review. This
   review is the first cross-model check, and the README should say so.
5. **Volume** ([avoid 20](../../../../avoid/20_volume_without_a_gain.md)).
   About 37 KB of notes and a 770-line manuscript record one exact formula,
   one identity that follows from the finite Euler note in a line, one
   transfer lemma, two corollaries of it and a contract: about three pages
   of mathematics.
6. **Chat record.** History 1 is registered; this session is recorded in
   `chat-histories/claude-cowork/`.

## 9. Disposition and recommendations

1. **Accept as correct**, with the edits of §7: the exact mixed formula,
   the boundary identity \(\mathfrak M=\Delta_p\Delta_qK_S\), the corrected
   signed Gram identity, the compact transfer theorem, the metric sign
   asymptotic, the literal translate obstruction, the resolvent bound and
   the enclosure contract.
2. **Phase 1 passes** the proposal's criterion, "an equality with justified
   operator products, traces and inverses, plus an explicit comparison with
   the translate-span claim".
3. **Phase 2 has no candidate** (§5). The stopping condition is met after
   this reconciliation, subject to Codex's response to it. The four
   statements this review adds (Proposition R1, the sharpness of Theorem
   5.1, the a priori bound of §5 and the coefficient \(\mu_2\) of §7) are
   proof sketches for Codex to check in that response.
4. **Close the opening phase and make Project 04 dormant.** Proposed
   disposition for the README: *The mixed response of the finite-place
   Sonin trace is exactly the mixed difference of the boundary correction,
   a compact form on each fixed support. Place changes move only the
   boundary sector and the explicit prime-power sum. The translate-span
   reading, which transports the source rather than the space, fails
   already for one prime whose logarithm is shorter than the support; the
   metric term of the corrected signed Gram identity is what cancels the
   shifted gamma terms, and it is unbounded if and only if
   \(L>|\log(p/q)|\). A bound on the mixed response cannot by itself
   improve a fixed-window comparison, which consumes it only through the
   complete boundary form; along growing place sets the needed estimate is
   \(K_{S_L}\le B_{S_L}\). This is a scoped disposition, not an exclusion of
   collective prime estimates.* Reopening input, sharpening the proposal's:
   (i) a named consumer, that is, a declared window and residual budget
   into which a bound on mixed differences enters with a stated margin;
   (ii) an actual-Sonin estimate for the boundary operators along \(S_L\)
   that does not deteriorate with \((u/\ell)^2\), for example for the
   positive part of \(H_{K_{S_L}}\) relative to \(B_{S_L}\); or (iii) a
   cancellation among the return terms of (10) that the tilted control
   lacks.
5. **Manuscript.** Keep it as an unreviewed working record, not a
   milestone. Its framing gives six results equal weight, while four follow
   in a few lines from Theorem 3.2 and the logarithmic order of \(\Gamma\);
   in my judgment it does not pass the Manuscript gate ("substantial
   precise obstruction"). If a citable record is wanted, a three-page note
   would carry the place-change identity with compact transfer for every
   fixed finite place set, the source-versus-space dichotomy with its sharp
   threshold at one and two primes, the literal translate obstruction as a
   corollary, and the tilted generic control. That is a judgment for
   Edward, not a finding.
6. **Withdrawal pointer.** Proposed for the head of Reply 03 §5, not made
   here: *Correction, 17 October 2026 (Claude Opus 5.5, cross-model
   reconciliation of Project 04): the identification of accumulated mixed
   responses with the Weil form on a translate span is false as a literal
   identity, and the compressed metric is not a lower-order correction; it
   cancels shifted gamma terms already at one prime. See Project 04 Notes
   01 §5 and 02 §3 and its round-one review §3.*
7. **After Codex's reconciliation.** Update the 17 October paragraph of
   [summary 07](../../../../result-summaries/07_sonin_critical_boundary.md)
   with the reviewed status and the dormancy, adding the compact transfer
   theorem as a reusable item; add an evidence line to
   [avoid 06](../../../../avoid/06_status_stronger_than_the_evidence.md) for
   Reply 03 §5 ("That is a definite formula", stated before any derivation
   and withdrawn after this round). The avoid 12 line that Codex added
   stands.
8. **Proposed file changes, not made here** (one writer per file): the §7
   edits in N02 and MS; the draft-history hashes; the status lines of the
   project README, round README, research-overview README and portfolio
   README; the Reply 03 pointer; summary 07 and avoid 06. Besides this
   review and its `claude-review/` folder, I changed the reviews README
   (its index row), the numerics README (one pointer) and, by the standing
   project instruction, this session's chat record.

## Appendix A. Artifact digests at review (SHA-256, first 16 hex digits)

| Artifact | Digest |
| --- | --- |
| Note 01 | `570a6326bc277d70` |
| Note 02 | `35e04b143c944627` |
| Round-one README | `75b6857cc17c236b` |
| `sonin_mixed_prime_response.tex` | `6e7df9efe1bc04f3` |
| Manuscript README | `523dc6adfcd4d7e8` |
| Project README | `f1d97ddf83689689` |
| `DRAFT_HISTORY.md` | `ffd42c6e54cb4670` |
| Initial proposal | `b4e1485e7b671e84` |
| Finite Euler identity note (inherited) | `513267200bc9d37d` |
| Canonical comparison audit (inherited) | `3e194a9f3bfca1c5` |
| Place-addition note (inherited) | `c9372fbe2959c053` |
| Closed-source comparison (inherited) | `cb94a4e0fe7fa589` |
| Compact-correction note (inherited) | `743d3ea1bc9adfa7` |
| Reply 03 (inherited) | `0871fb3829301bd2` |
| Setup review (inherited) | `2f0413af82e04a13` |

## Appendix B. Computations

The [review-check program](../numerics/round-1/claude-review/review_checks_claude_20261017.py)
(`cfd20ad70b258139`) and its
[record](../numerics/round-1/claude-review/REVIEW_CHECKS_CLAUDE_20261017.json)
(`3d038327f577bd5c`) contain every computed number quoted above, in seven
sections: A digests; B exact finite models (eight-dimensional, commuting
Pythagorean rotations, rank-two and rank-three rational projections, four
weight pairs), with the commuting-projection case, \(\mu_2\) and the
negative controls; C the two-dimensional control; D the resolvent identity
and bound on exact symmetric involutions; E the kernel identity in exact
Gaussian-rational polynomial arithmetic; F the gamma-sector asymptotics by
composite Gauss–Legendre quadrature with a digamma implementation checked
against \(\gamma_\infty(0)=-\gamma-\pi/2-3\log2-\log\pi\), with an explicit
tail majorant below \(2\cdot10^{-20}\) (relative to \(\|h\|_2^2\)) for the
mixed-term bump; G constants. Section F uses box-spline bumps
(\(C^4\)) in place of smooth bumps, since the asymptotics use only moment
bounds on \(|\widehat h|^2\). The full run takes about 13 seconds on one
core. The record was produced in the cloud workspace with Python 3.13.16
and replayed on Edward's machine with Python 3.10.12; see the folder README.
