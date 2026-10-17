# Review of the investigations-3 setup, with proposed changes

16 October 2026, late evening, America/New_York. Prepared for Edward Baker
with LLM assistance. Model: Claude Fable 5.1 (`claude-fable-5-1`), Claude
Cowork, reasoning effort max; the serving model may differ from the
configured identifier. This is a cross-model review of the portfolio that
Codex initialized at commit `688b2db`: the [portfolio plan](../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md),
the seven initial proposals, the folder READMEs and histories, read against
the [brainstorm exchange](../../brainstorm/investigations-3/README.md), the
[planning conversation](../../investigations-2/formal_replay_crosswalk/chat-histories/0027_2026-10-17T01-47-10Z_review-claude-brainstorm-note.json),
the [result summaries](../../../result-summaries/README.md) and the
[patterns to avoid](../../../avoid/README.md), which are unchanged since the
exchange. It proposes changes and does not make them: the plan and the
proposals have one writer, and the changes below are for Edward and Codex
to accept, amend or decline. Nothing here is a result; two literature
statements were fetched today and are quoted with their theorem numbers;
the two zero-density exponents in Section 2 are from memory and are
flagged as such.

**Overall.** The setup is faithful to the exchange. Each proposal names its
target's classification, its controls with the premise each fails, a first
bounded deliverable, model responsibilities with the cross-model caveat,
and stopping rules; the plan's gate table and its two-lane resource rule
are the right shape, and the dormant directions are recorded with
reopening conditions rather than closed. I would start the work as the
plan says, with two changes of emphasis and a dozen specific edits. The
changes of emphasis: Project 01's first bounded test can be decided by one
line of arithmetic once two published statements are quoted, and that
line reorders its routes (Section 2); and Projects 01 and 03 would, as
written, build the same conductor-parametrized remainder analysis twice
(Section 4). The edits are listed in Section 0 and justified in Sections
1–9.

## 0. Proposed changes

| No. | File | Change | Reason |
| --- | --- | --- | --- |
| C1 | Portfolio plan, gate table | Add to the Contract gate: "the scale at which the proposed estimate must act, and whether that scale is \(e^{-\pi x/8}\)"; and "every imported statement quoted with theorem number and hypotheses from the fetched text" | The two gates the exchange added to Codex's three; the second caught two errors of fact in Note 03 |
| C2 | Portfolio plan, first wave | Run Project 07 first and time-box it (one week, one reconciliation), then open 01 and 02 as the two developing lanes | 07 decides whether anything structural remains on the shortlist; its cost is a day of computation and a week of writing |
| C3 | Portfolio plan, "What the exchange settled" | Add the direction-of-transfer sentence: the inequality \(\|B\delta\|\le C\|M\delta\|\) transfers a nonvanishing jet from theta to its neighbours, never to theta; any certificate built on it must say what object it certifies | Otherwise 07 can conclude "the radius is larger" without noticing that no radius certifies theta |
| C4 | Portfolio plan and Project 01 | Replace the "almost-all exceptional exponent" target by two staged targets: a per-character finite-set theorem with its number (Section 2.2) and the almost-all theorem as conditional on two named inputs (Section 2.3) | The analytic-conductor arithmetic of Section 2.1 |
| C5 | Projects 01 and 03 | Move 01's "uniform approximation" phase into 03 as a conductor-parametrized deliverable with one owner; 01 keeps the contract, barrier and density work | Same analysis, two writers; avoid 17 |
| C6 | Project 01, first bounded deliverable | Add the three computations of Section 2 as the first bounded test, before the normalization table | They decide the routes and cost nothing |
| C7 | Project 04, phase 1 | Fix the four terms at one support length \(L\) and one preparation (already stated); add the identity \(\Delta_p\Delta_qR_{S,L}=-\Delta_p\Delta_qB_S\) on the complete residual and a generic positive-matrix control for the mixed response | So that neither is "discovered" |
| C8 | Project 06 | Name the two admissible first consumers in the proposal itself: the interior count of the certified winding box of summary 13, and 01's velocity bound; record Polymath's drift remark (zeros drift inward at speed about \(\pi/4\)) as the quantity the local count must track | The proposal currently waits for a consumer that two other proposals already describe |
| C9 | Project 07 | Take the proposition with complete hypotheses from Section 8 as the input to Deliverable 1; relabel the \(\beta\)-weighted distances of the reply's record at \(N\ge4\) as "evaluated at the Euclidean minimizer" | 07 asks for exactly this; the relabelling is correct |
| C10 | Portfolio plan, "Directions retained" | Give the consolidation items an owner and a time box: the controls exposition (Reviews 19–20) and the standalone fixed-exponent note (summary 09) | avoid 15, 19 and 20: closures recommended twice and not written |
| C11 | Portfolio chat-histories README | Relocate chat 27 from the formal-replay registry to `papers/investigations-3/chat-histories/` with a relocation receipt, as chat 26 was relocated to the brainstorm folder; add a `claude-cowork/` subfolder note for portfolio-wide Claude sessions | Consistency with the 16 October relocation; the base folder has no Claude registry |
| C12 | Project 01, sources | Cite Dobner from the published version (Acta Arithmetica) with theorem numbers, and Platt's Theorem 7.1 with its exact height formula (quoted in Section 2.1) | avoid 16; the arXiv HTML of Dobner is truncated before Section 2 |

## 1. The portfolio plan

The plan's central paragraph, that the aim is "an applicable estimate, a
complete numerical gain, a useful diagnostic or a precise obstruction" and
that an RH-equivalent criterion "should be stated once", is the rule the
exchange converged on, and the gate table implements it. Three remarks.

The Contract gate lists the target classification and the imported
hypotheses but not the scale question (C1). In the exchange the scale
question decided four of the six directions and the hypothesis-quoting
rule caught the degree bound and the count. Both belong in the gate as
one line each, so that every proposal answers them before its first
computation.

The first wave is 01's contract and 02's feasibility "with 07 completed as
a short audit alongside them if capacity permits". I would invert the
conditional (C2): 07 is the cheapest item in the portfolio and the only
one that decides a structural question; if its outcome is the proposition
of Section 8 with the table confirmed, the structural shortlist is empty
and the two lanes run without a third; if its outcome is a positivity-aware
radius that certifies something about theta, that is the most important
result in the portfolio and should be known before the lanes are chosen.
Either way it should be time-boxed, as its own proposal says.

The plan's paragraph on the reply's radius is accurate and I would add one
sentence (C3). The radius \(\eta=\|h\|/C\) is a guarantee that no
admissible perturbation with measurement defect below \(\eta\) can create a
collision at \((t,x)\); a positivity-aware or directional analysis can only
enlarge it. But the inequality runs from theta's jet \(h\) to the
neighbours' jets, and \(h\) is the input. A certificate about theta would
need a comparison source with a known jet at the same \((t,x)\) and the
reverse inequality, whose margin is the comparison source's jet, equally
unknown at the exponential scale. Project 07 should therefore state, as a
deliverable, what a successful positivity-aware certificate would certify
and about which source. The plan's sentence "this does not close
infinite-dimensional, height-dependent or constructively admissible source
classes" is right and should stay.

## 2. Project 01: the first bounded test is one line of arithmetic

The proposal follows Section 8 of the reply and makes the transfer
obligations explicit, which is correct. Two statements fetched today let
its first test be done before any normalization table is written.

**Platt, Theorem 7.1** (arXiv:1305.3087, *Numerical computations
concerning the GRH*): GRH holds for Dirichlet \(L\)-functions of primitive
character modulus \(q\le400{,}000\) up to height
\(t_0=\max(10^8/q,\ 7.5\cdot10^7/q+200)\) for even \(q\) and
\(t_0=\max(10^8/q,\ 3.75\cdot10^7/q+200)\) for odd \(q\), by interval
arithmetic. So the verified analytic conductor \(q\,t_0\) lies between
\(10^8\) and about \(1.6\cdot10^8\) for every modulus in the range. The
zeta certificates used verification to \(T=3.06\cdot10^{10}\) (Polymath,
\(\Lambda\le0.22\), with \(t_0=0.2\)) and to about \(2.5\cdot10^{12}\)
(Platt–Trudgian, \(\Lambda\le0.2\), the row quoted in Review 20 with
\(t_0=0.186\), \(y_0\approx0.167\) and \(X=5\cdot10^{12}+194858\)).

### 2.1 The analytic-conductor benchmark

In the family, the dominance parameter is \(tL_\chi\) with
\(L_\chi=\log(qx/4\pi)\), since the gamma factor of \(\Lambda(s,\chi)\) has
logarithmic derivative \(\tfrac12\log(q|s|/2\pi)+\dots\) in place of
\(\tfrac12\log(|s|/2\pi)\) (this is the hypothesis the proposal rightly
says must be derived with its error terms; the arithmetic below assumes
only that the shift is \(\log(qx/4\pi)\) to leading order). At the verified
height, \(qx=2q\,t_0\in[2\cdot10^8,3.2\cdot10^8]\), so
\(L_\chi\in[16.6,17.1]\) for every \(q\le400{,}000\), against
\(L=22.3\) at Polymath's verification height and \(26.7\) at
Platt–Trudgian's. The conductor does not trade for height in the
per-character route: Platt's computation is a fixed budget in the analytic
conductor, and the family's available \(L\) is 17 whatever \(q\) is. To
match Platt–Trudgian's \(tL=0.186\cdot26.7=5.0\) one needs
\(t_0\approx0.29\); to match Polymath's \(0.2\cdot22.3=4.5\),
\(t_0\approx0.26\). So the per-character route's best
attainable statement, if every analytic step of the zeta certificate is
redone with \(q\), is of the form \(\Lambda_\chi\le t_0+y_0^2/2\) with
\(t_0\) near \(0.3\): between de Bruijn's \(0.5\) and zeta's \(0.2\). This
is the test the proposal calls "compare the first derived exterior
threshold with verified GRH heights"; it has one answer for all \(q\) at
once, and the answer is "no overlap at \(t_0=0.2\), overlap at
\(t_0\approx0.3\) if the character exterior theorem has zeta's constants",
which it will not quite have, since the Riemann–Siegel-type approximation
for \(L(s,\chi)\) carries the Gauss sum and a sum over residues.

### 2.2 The per-character theorem has a number and a size limit

The barrier of the zeta certificate is a zero-free rectangle at the
verification height placed in a gap between consecutive real zeros, and
the gap must persist for \(t\in[0,t_0]\); Polymath's remark after
Theorem 1.5 (fetched today) says the zeros drift toward the origin at speed
about \(\pi/4\), so the gap must be wider than about \(\pi t_0/4\) plus
margin. For a family this barrier is per character: each \(\chi\) has its
own zeros near \(X\). A finite-set theorem, "\(\Lambda_\chi\le t_0+y_0^2/2\)
for all primitive \(\chi\) modulo \(q\le Q\)", therefore costs one barrier
computation per character at height about \(10^8/q\), cheap for small
\(Q\) and impossible for the \(\sim10^{10}\) characters of Platt's full
range. That is a legitimate first target with a number (\(t_0\approx0.3\),
\(Q\) in the hundreds or thousands) and no literature precedent that
today's search found (Dobner proves \(\Lambda_F\ge0\) and finiteness, no
upper bound for general \(F\); Andrade–Chang–Miller give lower bounds and
sequence statements for quadratic characters). It is modest. I would make
it the staged target of 01 (C4), because every ingredient is a
conductor-parametrized copy of the zeta certificate and nothing in it is a
new mechanism.

### 2.3 The almost-all route has two cruxes, not one

The reply named the barrier replacement as the crux. The arithmetic above
adds a second. In the almost-all route the exterior height
\(T_*\) at conductor \(q\) has analytic conductor \(qT_*\approx A\), where
\(A\) is the zeta exterior height's analytic conductor, between \(10^{10}\)
and \(10^{13}\) depending on \(t_0\). The density step bounds
\(\sum_{\chi\bmod q}N(\sigma_*,T_*,\chi)\) with \(\sigma_*=\tfrac12+\sqrt{t_0/2}\)
(\(0.816\) at \(t_0=0.2\), \(0.887\) at \(0.3\)). The classical large-sieve
density theorems have, as I recall them and have not re-read today, the
shape \((qT)^{c(1-\sigma)}(\log qT)^{B}\) with \(c(1-\sigma)\) about
\(0.45\) at \(\sigma=0.816\) (Montgomery's \(2(1-\sigma)/\sigma\) for
\(\sigma\ge4/5\), Huxley's \(12(1-\sigma)/5\)) and \(B\) of order ten;
modern versions carry \((qT)^{\varepsilon}\) with an unspecified
dependence on \(\varepsilon\). At \(qT=A=10^{12}\) the power factor is
\(10^{5.4}\) and the logarithmic factor alone exceeds \(10^{13}\), so the
exceptional count exceeds the family size \(q-2\) for every modulus
anyone would compute with. The almost-all theorem therefore needs either
an explicit family density theorem with small logarithmic losses at the
analytic conductor of the exterior height, or a different density input,
and this must be settled in the contract phase before the barrier
replacement is attempted. The barrier replacement itself is a zero-gap
existence statement for all but few \(\chi\): "for most \(\chi\), the real
zeros of \(H_{t,\chi}\) in \([X,X+C]\) leave a gap of width \(w\) for all
\(t\le t_0\), and no complex zero with \(|y|\le y_0\) enters it", or
alternatively the velocity bound on zeros above the exterior height. Both
need the local count of Project 06 with a constant (C8). I would write
these two cruxes into 01 as the conditions on which the almost-all target
depends (C4), and spend the contract phase on them rather than on the
normalization table, which is routine.

### 2.4 Smaller points

The proposal says complex characters do not give an even \(H_{t,\chi}\) and
asks for both signs of \(\Re z\) or the conjugate-pair relation; correct,
and the relation is \(H_{t,\bar\chi}(z)=\overline{H_{t,\chi}(-\bar z)}\) in
Dobner's normalization, to be checked when the table is written. Dobner
should be cited from the published version with theorem numbers (C12): the
arXiv HTML the proposal links is truncated before Section 2, and the PDF
gives the class \(\mathcal S^\sharp\), the Hermitian functional equation
\(\xi^F(s)=\overline{\xi^F(1-\bar s)}\), the kernel symmetry
\(\Phi_F(u)=\overline{\Phi_F(-u)}\), Theorem 1 (existence of \(\Lambda_F\)),
Theorem 2 (\(\Lambda_F\ge0\)) and Theorem 3 (de Bruijn's strip contraction
under \(\Phi_F(u)=O(e^{-|u|^b})\), \(b>2\)).

## 3. Project 02

No substantive change. The proposal keeps the certificate conclusion
\(\Lambda\le t_0+y_0^2/2\) with all four obligations, inherits the audit by
reference, refuses a sweep before the transfer and tail are proved, and
pins the public-source comparison; those are Review 20's gates. One
addition to the Completion section: state the baseline against which "a
measurable reduction in certification cost at equal coverage and accuracy"
is measured (the pinned package's row count, precision and runtime), so
that the comparison is fixed before the first row is produced.

## 4. Project 03, and its overlap with 01

The proposal's preferred candidate, "direct complex nonvanishing that
avoids unnecessary differentiation", is the right first choice: the
certificate consumer needs \(H_t(x+iy)\ne0\) for \(y\ge y_0\) in the
exterior, not four derivative inequalities, and the carrier budget of
21 Note 58 pays for three derivatives it does not need. The table of
unavoidable positive costs before any algebra is the correct order of
work, and the remarks on the shrinking window are the exchange's.

The overlap (C5): 01's "uniform approximation" phase asks for "the
analogue of Polymath's \(A_t+B_t-C_t\) with explicit dependence on \(q\)
and \(x\) jointly", and 03's deliverable is "one complete remainder budget
at a declared attainable overlap height" for zeta. These are the same
analysis with \(q\) as a parameter, and the plan assigns them to
different leads. One owner should write the conductor-parametrized
remainder once, with \(q=1\) as the zeta case; 01 consumes it. This also
removes a hidden dependency: 01 cannot run its first benchmark (Section
2.1) beyond the leading-order arithmetic without 03's error terms.

## 5. Project 04

The proposal states the right first task and the right stopping rule. Two
additions (C7). First, since the complete arithmetic form \(Q\) does not
depend on the place set, the place-addition note's (A9) gives
\(\Delta_p\Delta_q R_{S,L}=-\Delta_p\Delta_q B_S\) on the complete residual
immediately; recording it prevents the mixed response of the residual from
being presented as a second result. Second, the one-prime response already
has a generic \(2\times2\) control showing either sign; the mixed response
needs its own generic positive-matrix control, written before the actual
Sonin formula is interpreted, so that a sign in the actual case is compared
with the generic distribution of signs. The proposal is right that the
reply's translate-span identification is a claim to check; the reply
called it a structural reading and the check is phase 1's job.

## 6. Project 05

No change. The gate (one family, an independent stability mechanism, a
first compatibility inequality) is the one agreed in the exchange, the
Toeplitz/Jensen/Hankel distinctions are the ones Investigation 13
recorded, and the clause "do not build in a sequence of heat thresholds
tending to zero unless that property has been proved independently" is
the corrected form of the reply's heat remark. If I am to nominate the
family, my present expectation is a short disposition rather than a
candidate, and the proposal allows that outcome.

## 7. Project 06

The proposal waits for "a precisely stated consumer" while two consumers
are already stated elsewhere in the portfolio (C8): the interior count of
the certified winding box in summary 13, which the certificates now obtain
by enclosure, and the velocity bound of Section 2.3, which needs an upper
local count with a constant to bound the tail sum over distant zeros. Name
both in the proposal and let 01's contract phase decide whether the second
is requested. The drift remark of Polymath (speed about \(\pi/4\)) is the
quantity a local count at positive time must be consistent with, and the
\((t/16)\log(X/4\pi)\) term in \(g(X,t)\) is its integrated form; the
proposal keeps the drift explicit, which is right. The default scope
\(X\ge200\) is fine as a floor; the consumers live at \(x\sim10^{10}\) and
above, so the constants must be uniform there.

## 8. Project 07, and the proposition with its hypotheses

The audit is the cross-model check the reply asked for, and its three
distinctions (operator inequality, sufficient radius, actual distance) are
the right ones. Deliverable 1 asks Claude for "a repaired proposition with
complete hypotheses". Here it is, so that 07 can start from a statement
rather than from the sketch (C9).

**Proposition (finite-support measurement scale).** Let
\(\phi_n(u)=e^u(2\pi^2n^4e^{8u}-3\pi n^2e^{4u})e^{-\pi n^2e^{4u}}\), fix
\(N\ge1\) and \(T_0>0\), let \(V\subseteq\mathbb R^N\) be a linear subspace
(the finite-support perturbations, with any linear constraints such as
\(\sum_n\beta_n\delta_n=0\) or \(\delta_1=0\) built in), and let
\(M:V\to\mathbb R^m\) be linear and injective. For \(\delta\in V\) put
\(f_\delta=\sum_{n\le N}\delta_n\phi_n\), \(g_\delta=e^{tu^2}f_\delta\),
\(H_\delta(t,x)=\int_0^\infty g_\delta(u)\cos(xu)\,du\) and
\(B_{t,x}\delta=(H_\delta,\partial_xH_\delta)(t,x)\). Then:

1. For \(\delta\ne0\), \(f_\delta(u)-f_\delta(-u)\) is a nonzero odd entire
   function, so \(k(\delta)=\min\{k\ge0:f_\delta^{(2k+1)}(0)\ne0\}\) is
   finite. (Proof: as \(u\to+\infty\), \(f_\delta(u)\) decays doubly
   exponentially while
   \(f_\delta(-u)=e^{-u}\sum_{k\ge1}c_k e^{-4ku}\sum_n\delta_nn^{2k}\) with
   \(c_k=(-1)^k(2k+1)\pi^k/(k-1)!\ne0\); evenness would force
   \(\sum_n\delta_nn^{2k}=0\) for all \(k\ge1\), a Vandermonde system in the
   distinct \(n^2\), so \(\delta=0\).)
2. For \(0\le t\le T_0\), every \(K\ge1\) and \(x>0\),
   \(H_\delta(t,x)=\sum_{k<K}(-1)^{k+1}g_\delta^{(2k+1)}(0)\,x^{-2k-2}+R_K\)
   with \(|R_K|\le\bigl(|g_\delta^{(2K+1)}(0)|+\|g_\delta^{(2K+2)}\|_{L^1(0,\infty)}\bigr)x^{-2K-2}\)
   (integration by parts \(2K+2\) times; the boundary terms at infinity
   vanish by the double-exponential decay). The odd
   derivatives of \(g_\delta\) at \(0\) are triangular combinations of those
   of \(f_\delta\) with coefficients polynomial in \(t\), so the first
   nonvanishing index is \(k(\delta)\).
3. For any unit \(\delta_0\in V\) with \(k_0=k(\delta_0)\), the least
   \(C(t,x)\) with \(\|B_{t,x}\delta\|\le C\|M\delta\|\) on \(V\) satisfies
   \(C(t,x)\ge|H_{\delta_0}(t,x)|/\|M\|\ge\tfrac12|f_{\delta_0}^{(2k_0+1)}(0)|\,x^{-2k_0-2}/\|M\|\)
   for \(x\ge x_0(\delta_0,T_0)\), by item 2 with \(K=k_0+1\).
4. If \(\|h(t,x)\|\le K_0\,x^{A_0}e^{-\pi x/8}e^{tL^2/16}\) for theta's jet
   \(h\) on \(0\le t\le T_0\) (the carrier bound; \(A_0\) and \(K_0\) are to
   be supplied from Polymath's effective approximation, which is 07's
   quantification task), then
   \(\eta(t,x)=\|h\|/C\le2K_0\|M\|\,x^{2k_0+2+A_0}e^{-\pi x/8}e^{tL^2/16}/|f_{\delta_0}^{(2k_0+1)}(0)|\).
5. For every \(\delta\in V\) with \(\|M\delta\|<\eta(t,x)\),
   \(B_{t,x}(a_\theta+\delta)\ne0\), since
   \(\|h+B\delta\|\ge\|h\|-C\|M\delta\|>0\). Nothing follows about \(h\) from
   the neighbours. Dividing \(B\) by the carrier \(|M_t(x)|\), or by a
   nonvanishing contour jet \(|H_t(x+ic)|\), replaces item 4 by
   \(C_{\rm rel}\ge c\,x^{-2k_0-2-A_0}e^{\pi x/8}e^{-tL^2/16}/\|M\|\).

The hypotheses the audit should test are the finite support (item 1 fails
for infinite support, where the \(\beta\)-weighted framework of 22 Note
03/08 applies instead), the fixed \(M\) (an \(x\)-dependent measurement of
exponentially increasing precision is excluded by assumption, and is the
statement that the source must be known to \(e^{-\pi x/8}\)), and the
carrier bound in item 4, which is the only imported estimate. Two
corrections to the reply's record that the audit will find and that I
record now: the \(\beta\)-weighted distances at \(N\ge4\) are evaluated at
the Euclidean minimizer and are not optima in the weighted metric (at
\(N=3\) the solution is unique, so the point is moot there), and the
\(x\approx140\) figure is an extrapolation of the recorded decay from
\(x=85\), as the reply says; 07's "one preregistered threshold check"
is the right way to settle it and I would set it at \(x=120\), inside the
range where the dependency's quadrature is still accurate.

## 9. Records, histories and attribution

The planning conversation is registered as chat 27 in the formal-replay
registry of Investigation 22's lane
(`papers/investigations-2/formal_replay_crosswalk/chat-histories/`). On 16
October Edward asked that the brainstorm conversation, chat 26 of the same
registry, be relocated to the brainstorm folder with a receipt, which was
done. The same treatment for chat 27 (C11), into
`papers/investigations-3/chat-histories/`, would keep the portfolio's
founding conversation with the portfolio; the plan's text "retains its
existing formal replay identity 27" reads as a choice not to relocate, and
if it is deliberate the README should say why. The base `chat-histories/`
folder also has no `claude-cowork/` registry for portfolio-wide Claude
sessions, while every project folder has one; the recorder creates it at
first capture, and the README should say so. This session's own record
stays in the brainstorm registry (chat 2 there) because it is the same
conversation that wrote the reply; the recorder's rule is to preserve an
existing registration.

Every file in the setup records its model and effort and distinguishes
proposals from results; the top-level `papers/README.md` row and the
brainstorm README update are correct. The repository hygiene checker
passes on the new folder; its two failures are the pre-existing links to
the uncommitted PDF of Investigation 19's manuscript. This review opens
the `reviews/` folder at the portfolio root, which the setup did not
create; its README states the folder's purpose.

## 10. Coverage and scope

Read in full: the portfolio plan, the seven proposals, the top-level and
per-project READMEs, draft histories and chat-history READMEs, the diff of
commit `688b2db` outside the new folder, chat 27, and the unchanged
`avoid/` and `result-summaries/` folders. Fetched today: Platt,
arXiv:1305.3087, Theorem 7.1 (quoted above); Polymath, arXiv:1904.12438,
Theorem 1.5 and its drift remark; Dobner, arXiv:2005.05142 (PDF), Section
2 and Theorems 1–3; Andrade–Chang–Miller, arXiv:1310.3477, for the
precedent search of Section 2.2. From memory and flagged: the Montgomery
and Huxley density exponents and their logarithmic powers in Section 2.3,
and the relation between the conductor and the heat shift in Section 2.1,
which is the hypothesis Project 01 must derive. No file of the setup was
modified; this review and the folder README were added, and nothing was
committed.
