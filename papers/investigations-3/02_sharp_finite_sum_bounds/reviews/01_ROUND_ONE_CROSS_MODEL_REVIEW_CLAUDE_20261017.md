# Round-one cross-model review of the sharp finite-sum bounds

17 October 2026, evening, America/New_York. Prepared for Edward Baker with
LLM assistance. Model: Claude Opus 5.5 (configured identifier
`claude-opus-5-5`), Claude Cowork, reasoning effort max; the serving model
may differ from the configured identifier. This is a cross-model LLM review
of [round one](../notes/round-1/README.md) of Project 02, recorded by
**gpt-6.1-sol (Codex)**, effort **ultra**: Notes 01–02, the programs and
records of [`numerics/round-1/`](../numerics/round-1/README.md), and the
user-requested [working manuscript](../manuscript/sharp_finite_sum_bounds/main.tex),
all committed at `efba736` and unchanged at HEAD `7e56ba2`. It is not
independent specialist review. After drafting, one same-model subagent
(Claude, fresh context) checked the activation lemma of §3, by reading the
proof and by brute force on toy parameters, recomputed the planning meshes
with its own code, and checked the quoted figures against the records; its
corrections are incorporated. That check is same-model, not independent.

**Independence.** Round one is Codex's work, and on it this review is
cross-model. Some of its inputs are not. The sharp-weight option, the proof
that the improved inequality is monotone in the bound for \(|\gamma|\), and
the audits of the window freeze, the tail lemma and the uniform error
budget were written by Claude Opus 5.5 in the
[Newman certificate audit](../../../investigations-2/newman_certificate_audit/README.md)
(its Notes 3–4 and the cross-model review of its Notes 1–2). On those links
this review is same-family with their authors
([avoid 05](../../../../avoid/05_same_model_reviews_and_shared_premises.md)).
Codex's [cross-model review of that audit](../../../investigations-2/newman_certificate_audit/reviews/CROSS_MODEL_REVIEW_OF_CLAUDE_AUDIT_CODEX_20261013.md)
is the only other reading, and two of its findings bear on this round
(§6). The activation lemma of §3 is mine and needs Codex's check before
use. Every statement below is labelled as a verification of the round's
text, a replay of its programs, an independent computation (exact,
interval or floating), a proof sketch by the reviewer, a literature reading
or a recommendation.

**Summary.** I found no mathematical error in Notes 01–02 or in the
manuscript. Every record replays in substance, two of them only with the
wall caps raised and one with a memory gate failing on my host (§4): the
first-row enclosure digit for digit,
the accepted-leaf digests of the transfer engine on all four legs and on
the completion suffix, the tail and error budgets at both heads, the
counterexample and the arithmetic checker. An independent float64
implementation with a different enumeration reproduces the certified first
row to \(8.9\cdot10^{-17}\), and a finite difference of the summand computed
from its definition reproduces the engine's gate numerator (8) to relative
\(5\cdot10^{-30}\) at 900 actual integer points; with the decay term
removed, the engine rejects 267 of 504 actual points, so its predicate can
fail (§2). Three findings change how the round should be read:

1. **The remaining bridge is about twenty rows, not three million (§3).**
   The round leaves open \(L^{\rm sh}_N(y_0)>3\cdot10^{-7}\) for
   \(690989\le N<3840000\) and plans an amortized producer. A short lemma
   closes a whole run of indices from one certified row: freezing the
   scalars of the run's first index can only lose, and each later index
   activates \(2^{|P|}\) divisor pairs whose total effect is a
   one-dimensional sum in which the Euler majorant cancels. In float64, a
   greedy mesh needs 4, 5, 5 and 6 rows on the four legs, **20 rows** in
   all, also when the cap lemma bounds every span but the last
   (§3.2). The round's own pilot, unchanged, certified a row of this size
   in about four minutes (§3.3). If Codex accepts the lemma and the planned
   rows and activation bounds certify, Corollary 7.1 of the manuscript is
   discharged and \(\Lambda\le0.1745354\) follows from its stated imports.
   The same lemma would let the inherited audit close its open producer
   item with about 41 rows (§3.5).
2. **The replays depend on the host (§4).** Under the declared 45-second
   and 512-MiB guards, my host completes only patterns 0–144 of leg 0 in
   the first pass, the completion wrapper (which hard-codes 45 seconds)
   needs 58.7 seconds, and the tail record's required resource gate fails
   at 564 MiB. With the wall caps raised where needed, every digest and
   every mathematical gate reproduces exactly. The guards should be
   recorded as resource outcomes, not counted among the mathematical gates.
3. **The margins are now measured (§5).** \(t=0.157\) lies about
   \(10^{-4}\) above the first row's own boundary (\(t\approx0.15691\)). The
   transfer gate keeps at least half of the \(n^{-\sigma}\) decay in reserve
   on legs 2–3, where an interval probe at half the slope still passes, and
   by float sampling only about 40% on legs 0–1, where that probe fails, as
   it should. The tail margin is 0.0230 against an error of
   \(1.5\cdot10^{-8}\). The bound is at the edge of this lane: a smaller
   \(t\) needs a different first-leg mollifier or a different height, and
   either change needs the transfer certificate rerun.

**Disposition (§9).** Accept round one as correct, with the edits of §7.
The contract, binding, transfer, first window, error budget and tail pass
their gates. The finite-floor gate should be met through the activation
lemma rather than a producer campaign: write the lemma into a note,
certify about twenty rows with the existing pilot and outward activation
bounds, and route the completed certificate through one cross-model review
before any status word changes. The manuscript should stay an unreviewed
working draft until then; afterwards its Corollary 7.1 becomes a
computer-assisted theorem conditional on the named imports, and the
public-claims comparison of §6 must precede any statement about
competitiveness.

## 1. Scope, artifacts and method

**Read in full.** Notes 01–02 and the round README; every program and
record of `numerics/round-1/` and its run plans; the manuscript source, its
README and build record (the committed PDF and source match its hashes);
the project README, draft history, proposal and folder READMEs; the
project chat record (history 1). For context: all of
[`avoid/`](../../../../avoid/README.md) and
[`result-summaries/`](../../../../result-summaries/README.md); the
[portfolio plan](../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md),
README and [setup review](../../reviews/01_PORTFOLIO_SETUP_REVIEW_CLAUDE_20261016.md);
the inherited audit's README, its Notes 1, 3 and 4, the statement of
hypothesis (iii) in its Note 5, and Codex's cross-model review of it; and,
in the inherited helpers, the scalar, table, enumeration and error-bound
functions of
[`check_finite_row_certified_replay.py`](../../../investigations-2/newman_certificate_audit/numerics/check_finite_row_certified_replay.py)
and the uniform-budget function of
[`check_tail_and_uniform_error_budget.py`](../../../investigations-2/newman_certificate_audit/numerics/check_tail_and_uniform_error_budget.py).

**Replays.** On the cloud workspace (Python 3.13.16, Linux x86-64), against
the round's records (Python 3.10.0, macOS): the pilot with its self-test;
the transfer engine with the declared caps and again with the wall cap
relaxed; the completion suffix with the wall cap relaxed, by a filed
wrapper that makes the round's own call on the same engine, box cap 30,000
and depth 36; the tail adapter at both heads; the arithmetic checker; the
counterexample. Results in §2 and §4.

**Independent checks.** [`claude-review/`](../numerics/round-1/claude-review/README.md)
holds one standard-library program and its record, in seven sections:
digests (A); float64 rows by an independent code path, with cross-checks
against certified or recorded values and a boundary control (B); the gate
numerator against definition-based finite differences (C); fault
injection, an interval slack probe and a float scan of the required slope
(D); exact rational checks of the seminorm properties the activation lemma
uses (E); the activation planning meshes, floating and labelled as
planning (F); and the contract arithmetic (G). The program exits nonzero
if a comparison leaves its tolerance or a negative control fails to fail
([avoid 11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)).
The same folder keeps the small wrapper used for the completion replay of
§4, the record of one cost probe (§3.3), and the comparison of a replay on
Edward's machine with the record.

**Literature fetched today.** Polymath, arXiv:1904.12438v2 (HTML), for the
statements of Theorems 1.2 and 1.3: the three hypotheses of Theorem 1.2,
with the curved barrier region
\(\sqrt{y_0^2+2(t_0-t)}\le y\le\sqrt{1-2t}\), \(X\le x\le X+\sqrt{1-y_0^2}\),
\(0\le t\le t_0\), agree with Note 01 §1 and with the audit's Note 1 §3;
the definitions of \(f_t\), \(\gamma\), \(s_*\), \(\kappa\), \(N\) and the
three bounds the binding uses agree with the manuscript (§1.1). The
extraction garbles the positive part in the bound for
\(\operatorname{Re}s_*\); the audit read it from the TeX source (its Note 4
§2). A search for current upper bounds on \(\Lambda\) is reported in §6.

## 2. What was verified

N01, N02 are the round's notes and MS the manuscript; equation and theorem
numbers are those of the cited file.

| Claim | Where | Check |
| --- | --- | --- |
| Contract: \(t_*=157/1000\), \(y_0^2=87677/2500000\), \(y_1^2=1-2t_*\), target \(872677/5000000\) | N01 §1, MS (1.2) | Verified exactly (G) |
| Polymath Theorem 1.2: (i) depends only on \(X,y_0\); the new curved barrier lies in the audited box \([X,X+1]\times[0.1809,1]\times[0,0.16125]\) | N01 §1, MS §7 | Verified against the fetched statement; \(y_0>0.1809\), \(t_*<0.16125\), \(\sqrt{1-y_0^2}<1\) exactly (G). The barrier itself is inherited, not re-audited here |
| First window: \(x_{690988}<X+\sqrt{1-y_0^2}<x_{690989}\) at \(t_*\) | N01 §1 | Verified, margins \(5{,}377{,}393.98\) and \(11{,}989{,}041.18\); the edge shift from \(t_0\) is \(0.00334\) (G) |
| Native binding (1); one division by \(M\); \(K\) not divided again | N01 §2, MS Prop. 2.2 | Verified by hand, including the inverse of \(T_\Gamma\), \(\Gamma=\gamma E/\overline E\), \(w_1=1\), \(|m^{-\kappa}-1|\le m^{|\kappa|}-1\) and \(E\ne0\) |
| \(U_g\) identity and monotonicity in \(g\); \(W_g\) need not be monotone | N01 §2, MS Lemma 2.1, Remark 2.3 | Verified; three-branch derivatives by hand; exact random checks (E) |
| Gate (2): right Dini derivative with zeros, ties and the \(\sigma\) kink | N01 §3, MS Lemma 3.1 | Verified by hand |
| Divisor-pattern factorization \(B=b_t(n)C_0\), \(A=b_t(n)e^{yL}C_y\), and \(v'\) | N01 §3 | Verified; also implicitly by (C) |
| \(M_N\) and \(K_N\) decrease in \(y\); rate bound \(<-0.631\) | N01 §3, MS Cor. 4.4 | Verified, including \(\tfrac{d}{dy}\log(m^{\rho y}-1)\le\rho\log m+1/y\) |
| Exact generic obstruction (\(n=16\)) | N01 §3, MS Prop. 3.2 | Verified by hand; replay identical |
| Coordinates (7), activity test, numerators (8)–(9) | N02 §§2–3, MS §4 | Verified by hand; (8) agrees with a definition-based finite difference at 900 single-branch actual points to relative \(5.2\cdot10^{-30}\), and no accepted point has a positive derivative (C) |
| Integer feasibility and sector bookkeeping | N02 §2 | Verified by reading `trim`: strict and inclusive sector bounds are enforced or over-enclosed, candidate tests only discard infeasible pairs |
| Singleton lemma and prime-zero lemma | N02 §4, MS Lemmas 4.2–4.3 | Verified by hand: branch activity through \(2\ell+a<0\), the \(\tanh\) comparison, and \(-52663/9350\) |
| Interval arithmetic of the engine | N02 §5 | Read: directed `Decimal` operations, \(10^{-38}\) padding of correctly rounded `exp`, `ln`, `sqrt`; a zero-containing numerator uses \(|T|\); no midpoint signs |
| Four-leg transfer certificate | N02, MS Thm. 4.1 | Replayed: leaf digests identical on legs 1–3; the leg-0 prefix and the suffix identical with the wall cap relaxed (§4); the decay-free variant rejects 267 of 504 points (D1) |
| One sharp row (3) | N01 §4, MS Thm. 5.2 | Replayed identically; independent float64 value \(0.001775526910138382\), \(8.9\cdot10^{-17}\) from the enclosure midpoint, with the same 11,024,402 terms (B1); fixed-point error propagation of the new weight checked by reading |
| Error budget (4): \(E_{\max}<2.829444\cdot10^{-7}\) | N01 §4, MS Prop. 5.1 | Replayed, every result field identical. The two U3 gates (\(-0.42558\), \(-0.47805\)) are the \(\log N\)-derivatives of the moving cap, with exponent \(\sigma_N\) retained, as Codex's audit review requires (§6) |
| Tail (5) with head 600000; head 153814 does not close | N01 §4, MS Thm. 6.3 | Replayed, every result field identical at both heads; the reverse reduction order (MS Prop. 6.2) checked by hand; displayed endpoints are read with an outward last-place guard |
| Control screen | N01 §6, MS §7 | Agreed: the sharp algebra is generic and the theta-specific input is the approximation with its errors; no shape claim is made |

The independent rows also reproduce the audit's numbers: the plain weight
at \(t_0=129/800\), \(N=690988\), gives \(7.913667452574855\cdot10^{-7}\)
against the certified lower end \(7.9136674559413\cdot10^{-7}\); the sharp
weight at \(t_0\) gives 0.076995 (audit float 0.0770); the plain weight at
\(t_*\) gives \(-0.087007\), \(-0.087568\), \(-0.089204\), \(-0.091602\) at
the four leg starts (audit float \(-0.0870\), \(-0.0876\), \(-0.0892\),
\(-0.0916\)) (B2–B3).

## 3. Finding 1: the remaining finite bridge

### 3.1 The lemma

Fix a leg (prime set \(P\), \(D=\prod P\)), \(y\in[y_0,y_1]\) and indices
\(N_a\le N\) of the leg. Write \(g_a,\sigma_a,k_a,M_a\) for the frozen
quantities (1.12)–(1.14) of the manuscript at \(N_a\), and
\[
\Delta_y(N_a,N)=\sum_{N_a<m\le N}b_{t_*}(m)\,m^{-\sigma_a}
\Bigl[(1-g_a)\,U_{g_a}(1,m^y)+g_a\,(m^{k_a}-1)\,m^{y}\Bigr].
\]

**Lemma (activation bound; proof sketch by the reviewer).** Here \(y>0\),
so \(g_a<1\). If \(L^{\rm sh}_{N_a}(y)-\Delta_y(N_a,N)>0\), then
\(L^{\rm sh}_N(y)\ge L^{\rm sh}_{N_a}(y)-\Delta_y(N_a,N)\).

*Proof.* (a) As \(N\) increases, \(q_N\) and \(x_N\) increase, so
\(g_N\le g_a\), \(k_N\le k_a\) and \(\sigma_N\ge\sigma_a\) (the positive
part in \(\sigma_N\) and its factor \(x_N^{-2}\) both decrease); hence
\(M_N\le M_a\). These are the freeze directions of N01 §2, read in \(N\).

(b) Let \(V_{\rm hyb}\) and \(C_{\rm hyb}\) be \(V_N\) and \(C_N\) computed
with the coefficients \(B_{N,n},A_{N,n}\) of \(N\) and the scalars of
\(N_a\). By (a), Lemma 2.1 (monotonicity of \(U_r\) in \(r\)) and
\(n^{-\sigma_N}\le n^{-\sigma_a}\), we have \(V_N\le V_{\rm hyb}\) and
\(C_N\le C_{\rm hyb}\). So
\(L^{\rm sh}_N\ge L_{\rm hyb}:=(1-g_a)(1-V_{\rm hyb})/M_a-g_aC_{\rm hyb}\)
whenever \(V_{\rm hyb}<1\).

(c) A pair \((n,d)\) with \(d\mid D\), \(d\mid n\) is active at \(N\) but not
at \(N_a\) exactly when \(m=n/d\in(N_a,N]\). Thus
\(B_{N,n}-B_{N_a,n}=\sum\lambda_db_{t_*}(m)\) and
\(A_{N,n}-A_{N_a,n}=\sum\lambda_db_{t_*}(m)m^y\) over those pairs. Since
\(U_g(B,A)=(|B-g^2A|+g|A-B|)/(1-g^2)\) is a seminorm in \((B,A)\),
\[
U_{g_a}(B_{N,n},A_{N,n})\le U_{g_a}(B_{N_a,n},A_{N_a,n})
+\sum|\lambda_d|\,b_{t_*}(m)\,U_{g_a}(1,m^y).
\]

(d) Multiply by \(n^{-\sigma_a}=d^{-\sigma_a}m^{-\sigma_a}\) and sum. Each
\(d\mid D\) occurs once for each \(m\), and
\(\sum_{d\mid D}|\lambda_d|d^{-\sigma_a}=M_a\), so
\(V_{\rm hyb}\le V_{N_a}+M_a\sum_{N_a<m\le N}b_{t_*}(m)U_{g_a}(1,m^y)m^{-\sigma_a}\).
Also \(C_{\rm hyb}=C_{N_a}+\sum_{N_a<m\le N}b_{t_*}(m)(m^{k_a}-1)m^{y-\sigma_a}\).
Inserting both in \(L_{\rm hyb}\), the factor \(M_a\) cancels and
\(L_{\rm hyb}\ge L^{\rm sh}_{N_a}-\Delta_y(N_a,N)\).

(e) If the right side is positive, so is \(L_{\rm hyb}\); then
\(V_{\rm hyb}<1\) and (b) applies. \(\square\)

Only \(y=y_0\) is needed: Theorem 4.1 already transfers each index's own
floor through the strip (Corollary 4.4), so
\(L^{\rm sh}_N(y_0)>3\cdot10^{-7}\) for every \(N\) is exactly the premise
of Corollary 7.1. Besides bookkeeping, the lemma uses the round's
Lemma 2.1, the freeze directions and the seminorm property of \(U_g\). The
subagent check found no gap in the proof, and no violation in more than
35,000 brute-force cases on toy parameters in which the hypothesis holds,
including cases with \(\sigma\) shifted upward so that it holds at
\(t=0.157\) (a floating test of the inequality, not of the application).
The same argument holds for the plain
weight \(|B|+g|A|\), which is also a seminorm, with \((1-g)U_g(1,a)\)
replaced by \(1+ga\). It is the explicit form of the amortization the
package's producer already performs through frozen runs; nothing here is
claimed as new.

**Closed form.** For \(a=m^{y_0}\ge1\) and \(g^2a\le1\) (true on every
planned span, where \(g_a^2m^{y_0}<0.1\)),
\((1-g)U_g(1,a)=(1-g)(1+ga)/(1+g)\) (checked exactly, E). So
\(\Delta_{y_0}\) is a combination of the two sums
\(\sum_{N_a<m\le N}b_{t_*}(m)m^{-s}\), \(s\in\{\sigma_a,\sigma_a-y_0\}\),
with \(m^{k}-1\le k\log m\,m^{k}\). Lemma 6.1 of the manuscript bounds both
outwardly, since \(\sigma_a-y_0>1.46>(t_*/2)\log N\). A certificate
therefore needs, per mesh step, one certified row and two cap evaluations,
or an outward direct sum.

### 3.2 The planning mesh

Section F of the review program builds greedy meshes in float64: from the
first index of a leg, take the largest \(N_b\) in the leg with
\(L^{\rm sh}_{N_a}(y_0)-\Delta_{y_0}(N_a,N_b)>3\cdot10^{-7}\), then restart
at \(N_b+1\). The plan I recommend bounds \(\Delta\) by the cap lemma on
every span except the last of each leg, where an outward direct sum is
cheaper; its mesh rows and their float floors are:

| Leg | \(P\) | Mesh rows \(N_a\) (float \(L^{\rm sh}_{N_a}(y_0)\)) | Rows |
| --- | --- | --- | ---: |
| 0 | 2, 3, 5, 7, 11 | 690988 (0.00178), 694671 (0.00316), 701278 (0.00561), 713205 (0.00997) | 4 |
| 1 | 2, 3, 5, 7 | 729000 (0.00263), 734948 (0.00476), 745860 (0.00861), 766078 (0.0156), 804222 (0.0280) | 5 |
| 2 | 2, 3, 5 | 819000 (0.00358), 828800 (0.00675), 847622 (0.0127), 884345 (0.0238), 958160 (0.0444) | 5 |
| 3 | 2, 3 | 1028000 (0.00478), 1046971 (0.00975), 1086872 (0.0198), 1173176 (0.0400), 1370859 (0.0794), 1880119 (0.153) | 6 |

These are **planning values, not a certificate**. On leg 3 the direct sum
over the last span, from \(N=1{,}880{,}119\) to the leg's end, about two
million terms of one exponential each, has float value 0.14878 against the
floor 0.15289 there. With exact activation sums throughout the mesh is
also 4, 5, 5 and 6 rows, with largest row \(N=1{,}974{,}864\); with caps
throughout, the last span of leg 3 costs one row more, at
\(N=3{,}550{,}349\), which the pilot's memory guard would not admit
(§3.3) (F). The floors roughly
double from one mesh row to the next: near the first row each index adds
about \(3.8\cdot10^{-7}\) to the true floor while the activation bound
charges about \(4.8\cdot10^{-7}\), so the first span is about 3,700
indices and later spans grow geometrically. On a span in the first leg and
one in the last, the program checks the lemma's bookkeeping directly by
computing the hybrid row: \(L_{\rm hyb}(691988)=0.001539\) against the
bound \(L_{690988}-\Delta=0.001294\) and the own-scalar row 0.002152, and
\(L_{\rm hyb}(1030000)=0.004498\) against 0.004273 and 0.005306 (F0). The
activation bound is about twice the actual loss, as expected from a
triangle inequality over new pairs.

### 3.3 Cost and what the certificate needs

As a cost probe I ran the round's pilot, unchanged, at the largest row of
the exact-sum mesh: it certified
\(L^{\rm sh}_{1974864}(y_0)\in[0.163564430553564191107,\,0.163564430553564191115]\)
in 247 seconds with a peak of 339 MiB on the cloud workspace, inside its
600-second and 512-MiB guards, in agreement with the float plan to
\(10^{-16}\). Its record is kept in `claude-review/` with the executor
stated, since the program writes its author's model into every record it
produces. Peak memory grows about linearly with \(N\) (132 MiB at 690,988,
339 MiB at 1,974,864), so a row near 3.55 million would need about
590 MiB and the unchanged pilot, which asserts its guard before writing a
record, would abort there; the recommended plan's rows all lie below
1.9 million. The first-leg rows take about 100 seconds each, so the whole
mesh is under an hour of computation. The certificate consists of:

1. a note stating and proving the activation lemma, with the coverage
   condition: for consecutive mesh rows \(N_i\) of every leg, each leg's
   first index included, the certified lower end of
   \(L^{\rm sh}_{N_i}(y_0)\) minus a certified upper bound for
   \(\Delta_{y_0}(N_i,N_{i+1}-1)\) exceeds the allowance \(3\cdot10^{-7}\);
2. the certified rows, with `certify_sharp_pilot.py --N` unchanged;
3. outward bounds for the activation sums, by the cap lemma or a direct
   outward sum;
4. a record binding rows, bounds and the inequality of each step.

The greedy rule leaves no slack at the end of each span, so the
certificate should choose its mesh with a safety factor, for example
\(\Delta\le\tfrac12(L-3\cdot10^{-7})\), at the cost of a few more rows.

### 3.4 What this would and would not establish

With the finite floors certified, Corollary 7.1 gives
\(\Lambda\le872677/5000000=0.1745354\), conditional on the imports the
manuscript names: Polymath's Theorems 1.2 and 1.3 with the audited reading
of (21) and of the \(10.50\) weld, Platt–Trudgian's verification to
\(X/2\), and the inherited barrier certificate on its audited status. The
transfer, first window, error budget, tail and floors would then have had
same-model checks and this one cross-model review, which is not
independent validation. I recommend no status stronger than "conditional
computer-assisted result, internally reviewed" until a cross-model review
of the completed floor certificate, and no comparison with other bounds
before §6 is done.

### 3.5 Consequence for the inherited audit

The audit's last open item is the package's producer: of its 3,149,013
stored rows, 32 have been certified independently and 3,148,981 have not.
The lemma applies to the plain
weight at the package's time \(t_0=129/800\) with its
\(E_{\max}=2.33494905\cdot10^{-7}\): the planning mesh needs 41 rows (16,
8, 8 and 9 on the four legs; F). Certifying those rows with the audit's
own replay programme, together with its audited Dini transfer, would
discharge the producer item for hypothesis (ii) at \(t_0\) without
regenerating the sweep. This is a recommendation for the audit's owner;
the audit folder is not changed here.

## 4. Finding 2: reproducibility under the resource guards

The transfer certificate's mathematics does not depend on time or memory,
but its declared procedure does:

- **First pass.** Each leg stops at 30,000 evaluated boxes or 45 seconds,
  whichever comes first. On Codex's machine leg 0 reached the box cap
  (36.2 seconds) after completing patterns 0–171. On the cloud workspace,
  which ran the engine about 1.7 times slower, leg 0 reached the wall cap
  after 21,866 boxes with patterns 0–144 complete. With the wall cap raised
  and the box cap unchanged, the replay stops at the box cap after exactly
  30,000 boxes, completes patterns 0–171, and reproduces the record's
  accepted-leaf digest `a190c9ce…` and every count.
- **Completion.** The wrapper hard-codes `certify_leg(0,45,30000,36)` and
  requires `seconds<=45`. The same suffix took 58.7 seconds here; with the
  wall cap raised it completes all 71 patterns with 19,935 boxes and digest
  `f222a5c9…`, as recorded. Run as written on this host, the wrapper would
  report no certificate.
- **Tail adapter.** The 600000-head run took 115.4 seconds against its
  120-second alarm and peaked at 564 MiB, so its required gate
  `resource.peak_resident_bytes_below_512MiB` fails and
  `all_required_gates_pass` is false. Every mathematical gate and every
  result field are identical to the record; the record itself peaked at
  509.9 MiB, 2.1 MiB below the guard.
- **Pilot.** Identical, in 110 seconds against its 600-second guard.

Recommendations: record wall and memory guards as resource outcomes beside
the mathematical gates, never inside `required_gates`; let the completion
wrapper take its caps as arguments and record them; state in the transfer
record that the box cap, not the wall cap, ended the first pass's prefix.
The certificate is reproducible in substance, and its replay instructions
should not depend on the host's speed.

## 5. Finding 3: margins and robustness

- **First row in \(t\).** The sharp first row is \(-1.246\cdot10^{-4}\) at
  \(t=0.1569\) and \(+8.26\cdot10^{-4}\) at \(t=0.15695\) (float, B4), so
  its boundary is near \(t=0.15691\), as the audit's Note 3 §5 said. The
  round's \(t_*=0.157\) is about \(10^{-4}\) inside it, and at this \(X\),
  \(y_0\) and leg structure no further lowering is worth more than
  \(10^{-4}\) in \(\Lambda\).
- **Transfer slack.** Define the required slope \(s^*\) of a summand as
  \(\partial_y\log U\) divided by \(\log n\); the gate needs \(s^*\le\tfrac12\).
  An interval probe with the slope bound halved to \(\tfrac14\) passes
  legs 3 and 2, so there \(s^*\le\tfrac14\) is certified and at least half
  of the decay is in reserve; on leg 1 it leaves strictly positive boxes
  (\(G=105\), sector \((5,7]\), \(n\) just above \(5N\)) (D2). Float sampling
  of actual integer terms (all patterns, three indices per leg, 31 values
  of \(y\); D3) gives sampled suprema 0.306, 0.294, 0.121 and 0.106 on
  legs 0–3, all at \(y=y_0\) and the first index of the leg: on legs 0–1
  at \(G=210\) with \(n\) just above \(15N\), on legs 2–3 at the top of the
  full-active sector (\(n=N\) and \(n=N-2\)). For legs 0–1 the reserve of
  about 40% is therefore a floating estimate, since a sampled supremum
  bounds the true one only from below; the interval certificate itself
  proves only \(s^*\le\tfrac12\) there. Nothing suggests a thin gate, in
  contrast to the package's reported plain-gate ratio, which the audit's
  Note 3 §4.3 traced to its stopping rule.
- **Tail and error budget.** The tail margin is 0.02303 against an error
  of \(1.49\cdot10^{-8}\); its thinnest gate is the \(A\)-cap box gate,
  1.10728, and the largest head keeping that gate above one is 718,226.
  The finite allowance \(E_{\max}<2.83\cdot10^{-7}\) is
  \(1.6\cdot10^{-4}\) of the first row's floor.

## 6. Scope, status, inherited corrections and literature

The round's scope statements are accurate: the notes and manuscript claim
no bound, say "certified" only for outward computations with records, and
keep the inherited barrier and initial verification as imports.

**Inherited corrections.** Codex's cross-model review of the audit has two
findings that touch this round. Its Finding 1 says that the written U3
reduction in the audit's Note 4 freezes the cap exponent too early; the
correct form keeps \(\sigma_N=(1+y_0)/2+(t/2)\log N-\delta_1\) inside
\(\operatorname{Cap}(2000,N;\sigma_N)\), and the gates U3b–U3c then show
that this moving cap decreases in \(N\). The adapter's two U3 gates are
exactly those derivatives (\(-(t_*/2)\log m_0+1/(\log N_0-\log m_0)\) and
\((1-y_0)/2+\delta_1-(t_*/2)\log N_0+1/(\log N_0-\log m_0)\)), so
\(E_{\max}\) is uniform as claimed; but the proof of MS Prop. 5.1 writes
\(\operatorname{Cap}_{t_*}(m_0,N_0;\sigma_0)\) without saying that the
exponent moves with \(N\), and it should (§7). Its Finding 2, nearest
rounding in exported endpoints, is already handled: the tail adapter reads
every displayed endpoint with an outward last-place guard, and the
manuscript's Table 3 rounds outward.

**Public comparison.** A search today found Platt–Trudgian's
\(\Lambda\le0.2\) as the published bound and the Gomila package's claim
\(\Lambda\le0.1787854\), publicized in August 2026 and self-described as
not peer reviewed. The audit's Note 1 records three further public claims
it never inspected (Gordon \(<0.158\), Planat \(0.17795\ldots\), Raymond
\(<0.149396\)); my searches did not find their sources. Two of them are
below 0.1745354. The proposal's rule applies: refresh and pin the public
comparison before presenting a gain as competitive or new
([avoid 06](../../../../avoid/06_status_stronger_than_the_evidence.md),
[avoid 16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md)).
Independently of that comparison, a replayable certificate that consumes an
audited public package at a lower \(t\), with a finite lane of about twenty
rows, is a useful artifact.

**The \(\sigma_N\) kink.** The finite lane uses Polymath's displayed (21)
for \(\operatorname{Re}s_*\), which the audit found true but not by its
written proof; Codex's review supplies a uniform comparison. Its
positive-part term is below \(10^{-26}\) on every window. Bounding the
positive part by one, as the tail and the error budget already do, would
remove both the kink and that dependence, and the gate would have
\(\sigma_N'=\tfrac12\) exactly (§7).

## 7. Smaller points

1. **Moving cap in MS Prop. 5.1.** Replace the frozen display by the
   moving one, citing Codex's audit review, Finding 1: the head is frozen
   at \(N_0\), the cap keeps \(\sigma_N\), and the U3 gates give its
   decrease. N01 §4 should say the same in one sentence.
2. **Cost baseline.** The setup review asked 02 to fix the baseline for
   "a measurable reduction in certification cost" before the first row. It
   is not recorded. Suggested: the package's producer, 3,149,013 rows; the
   audit's certified replay, about 100 seconds per row; and, if adopted,
   the activation mesh.
3. **\(\sigma_N\) kink.** As in §6, replace the positive part by one in
   \(\sigma_N\) (N01 §2, MS (1.13)). The change is below \(10^{-26}\) in
   \(\sigma\), but the transfer certificate's inputs change, so it should
   be rerun rather than assumed.
4. **Record attribution.** The pilot and the engine write
   `model='gpt-6.1-sol'` into every record, so a replay by anyone else is
   misattributed; record the author and the executor separately. The tail
   adapter's header says the serving model is not visible to its subagent,
   and `REQUIRED_GATE_SET.json` supplies it; one line in the round README
   would make that findable from the adapter.
5. **Manuscript bibliography.** Cite the published versions of Polymath
   (Research in the Mathematical Sciences, 2019) and Platt–Trudgian
   (Bulletin of the London Mathematical Society, 2021) beside the arXiv
   identifiers; I did not fetch the journal pages, so the volume and page
   data should be taken from them.
6. **Records.** The compiled PDF is committed, as in five other
   investigations-3 projects. The project's recorded convention keeps only
   `.tex` sources in the repository; whether it applies to working drafts
   is Edward's decision. Nothing else in the folder departs from
   [LARGE_FILES.md](../../../../LARGE_FILES.md).

## 8. Avoid patterns and the control screen

The round is a quantitative milestone, not an equivalent reformulation
([avoid 01](../../../../avoid/01_restating_the_target.md)). Its sharp
weight keeps the pairing that the plain triangle inequality loses, which is
the instruction of
[avoid 12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md);
the tail keeps the plain inequality where its margin is large. Counts are
reported with their scope
([avoid 04](../../../../avoid/04_counts_and_precision_as_evidence.md)); the
run plans precede the runs and cap their resources
([avoid 10](../../../../avoid/10_numerics_ahead_of_the_question.md)); the
allowance \(3\cdot10^{-7}\) is a declared budget above the computed
\(2.83\cdot10^{-7}\), not a floor reported as a measurement
([avoid 09](../../../../avoid/09_round_floors_and_fitted_laws.md)); the
normalized and unnormalized masses are distinguished in the manuscript
([avoid 08](../../../../avoid/08_normalization_and_constant_slips.md)).
The control screen of N01 §6 is the right one for a finite certificate:
the sharp algebra holds for any paired real coefficients, so it cannot
separate theta from a control; what is theta-specific is the approximation
theorem and its error, and a certificate for a control would need its own.
The one risk is
[avoid 11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)
turned around: resource gates that fail a correct certificate on a slower
host (§4).

## 9. Disposition and recommendations

1. **Accept as correct**, with the edits of §7: the contract, the native
   binding and freeze, the active-branch gate and its certificate on all
   four legs, the first-window margin, the error budget at the new time,
   the tail with head 600000 and its reduction order, and the generic
   obstruction.
2. **Gates.** The contract gate, the first bounded result and the transfer
   part of the feasibility gate pass. The feasibility gate's "positive
   complete margins" is open only for the finite floors.
3. **Next bounded task: the activation certificate (§3).** One note with
   the lemma and coverage condition, about twenty certified rows with
   their activation bounds, one record, then one cross-model review. The
   lemma is a proof sketch by the reviewer for Codex to check first. No
   producer campaign is needed.
4. **Reproducibility (§4).** Separate resource guards from mathematical
   gates in the tail record and the completion wrapper before the next
   run, and record which cap ended the first pass.
5. **Manuscript.** Keep it as an unreviewed working draft. After the floor
   certificate and its review, Corollary 7.1 becomes the main theorem and
   the activation lemma a short section; then the Manuscript gate applies.
   Do not expand it before then
   ([avoid 20](../../../../avoid/20_volume_without_a_gain.md)).
6. **Public comparison (§6)** before any status upgrade or claim of
   competitiveness.
7. **Audit (§3.5).** Offer the lemma to the Newman certificate audit for
   its producer item.
8. **After Codex's reconciliation:** update
   [summary 11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
   with the reviewed status of the transfer, first window and tail, and
   the floor status. No avoid entry is proposed; the round avoided the
   recorded patterns.
9. **Files changed here.** Besides this review and its
   [`claude-review/`](../numerics/round-1/claude-review/README.md) folder,
   I changed the [reviews README](README.md) (its index row), the
   [numerics README](../numerics/README.md) (one pointer) and, by the
   standing project instruction, this session's chat record. The edits of
   §7 are proposals for the files' owners.

## Appendix A. Artifact digests at review (SHA-256, first 16 hex digits)

| Artifact | Digest |
| --- | --- |
| Project README | `a88fa3255786997c` |
| `DRAFT_HISTORY.md` | `0045213e82c8f1af` |
| Initial proposal | `5e1879b0a65617bd` |
| Note 01 | `cd657c83b03d0f85` |
| Note 02 | `c4ebd9ff98d46b41` |
| `main.tex` | `277d6ffbd1be22c1` |
| `certify_sharp_pilot.py` | `860f9c0fe5aeea63` |
| `check_sharp_y_transfer_gate.py` | `aa6c73e0aa6672b5` |
| `complete_sharp_y_transfer_gate.py` | `3667ec2318994f52` |
| `check_gate_arithmetic.py` | `e85b6e380d55f4b6` |
| `check_t157_tail_budget.py` | `1a83895472f9254b` |
| `check_transfer_counterexample.py` | `32f666e782b01a47` |
| `SHARP_PILOT_RECORD_20261017.json` | `a9368a68cfd73b81` |
| `SHARP_Y_TRANSFER_GATE_RECORD_20261017.json` | `7ef1dd07f9bde167` |
| `SHARP_Y_TRANSFER_COMPLETION_RECORD_20261017.json` | `b38bc21312bf827d` |
| `TAIL_T157_M600000_RECORD.json` | `369de7d47141b862` |
| `TAIL_T157_M153814_RECORD.json` | `6d459f7a1dc56911` |
| `check_finite_row_certified_replay.py` (inherited) | `37d525ed2e8b4244` |
| `check_tail_and_uniform_error_budget.py` (inherited) | `c48c737e75baa70e` |

## Appendix B. Computations

The [review-check program](../numerics/round-1/claude-review/review_checks_claude_20261017.py)
(`5f5f78d77fb940df`) and its
[record](../numerics/round-1/claude-review/REVIEW_CHECKS_CLAUDE_20261017.json)
(`a89771dcb61ddbcf`) contain every computed number quoted above except the
replays of §4 and the cost probe of §3.3. The replays used the round's own
programs and records unchanged, with the wall caps raised where stated;
the completion suffix was replayed with the filed
[wrapper](../numerics/round-1/claude-review/replay_completion_suffix_relaxed_wall.py)
(`1fb767650a3326f9`), which makes the round's own call with only the wall
budget raised and checks the recorded digest. The cost probe's
[record](../numerics/round-1/claude-review/COST_PROBE_PILOT_N1974864_CLAUDE_20261017.json)
(`e56ba84e671699cd`) sits beside them. Section B sums float64 terms with
`math.fsum`, enumerated by gcd class first and cofactor second, unlike the
pilot's cofactor-first loop; section C uses 80-digit `Decimal` arithmetic
and a forward difference of step \(10^{-30}\); section D modifies the
engine only in memory, after checking its hash, and its slope scan is
floating; section E is exact rational arithmetic; section F is floating
planning. The full program run, with `--slack`, took 616 seconds on one
core of the cloud workspace (Python 3.13.16) and passed. A replay in the Linux VM on
Edward's machine (Python 3.10.12, aarch64), by sections and with
section F one leg per run, matched the record in all 775 compared fields,
floating fields included; the
[comparison](../numerics/round-1/claude-review/REPLAY_ON_EDWARDS_MACHINE_20261017.json)
is filed with the record.
