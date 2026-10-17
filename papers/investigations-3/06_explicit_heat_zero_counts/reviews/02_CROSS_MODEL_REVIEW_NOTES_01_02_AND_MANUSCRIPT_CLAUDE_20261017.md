# Cross-model review of Notes 01–02 and the working manuscript

17 October 2026, America/New_York. Prepared for Edward Baker with LLM
assistance. Model: Claude Opus 5.5 (configured identifier
`claude-opus-5-5`), Claude Cowork, reasoning effort max; the serving model
may differ from the configured identifier. This is the Claude analytic
audit that the [initial proposal](../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
assigns to Claude ("Claude audits the analytic proof and uniformity"). It
covers the [opening ledger](../notes/01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md)
(Note 01), the [round-two derivation](../notes/02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md)
(Note 02), the [working manuscript](../manuscript/explicit_heat_zero_counts.tex)
and the two arithmetic checkers, all recorded by **gpt-6.1-sol (Codex)**,
effort **ultra**. It is a cross-model LLM review, not independent
specialist review, and no subagents were used. One caveat on
independence: the project was opened on the advice of
[Reply 03 §4](../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md)
and the [setup review §7](../../reviews/01_PORTFOLIO_SETUP_REVIEW_CLAUDE_20261016.md),
both by Claude Fable 5.1, so on whether the project should continue and
which consumers count, this review is same-family and
[avoid 05](../../../../avoid/05_same_model_reviews_and_shared_premises.md)
applies. The analytic verdict rests on a line-by-line re-derivation
against the source and on computations that can fail.

Labels: **[V]** verification of the round's text against its source;
**[P]** a proof or proof sketch by the reviewer; **[F]** a floating
computation (30–60 digits, not outward rounded); **[R]** a
recommendation. Nothing here is a statement about the zeros of zeta or
about \(\Lambda\).

**Summary.**

1. **Correct as stated.** I found no mathematical error in Note 01,
   Note 02 or the manuscript that affects a stated result. The comparison
   (manuscript Theorem 1.2: \(|H_t(x+iy)/M_t(s_+)-1|<96624791/147000000\)
   for \(0<t\le\tfrac12\), \(x\ge2\cdot10^6\), \(3\le y\le4\)) and the
   count (Theorem 1.1: \(K_t(X)\le\tfrac{82123}{72000}\log(X+2)+\tfrac{574}{27}
   \le\tfrac65\log(X+2)+22\) for \(X\ge2\cdot10^6\)) follow from the named
   statements of Polymath ([arXiv:1904.12438v2](https://arxiv.org/abs/1904.12438v2))
   by the arguments written. I checked every imported statement against
   the paper's LaTeX as rendered in its arXiv HTML, display by display
   (§1). The three observations
   the notes make about the source are right, and each is harmless for
   Polymath's conclusions: the display after (99) has \(t/2\) where (17)
   and (21) give \(t/4\); the inequality printed before (60) is false by a
   factor of about two; and the displayed bound for (63) omits the
   Riemann–Siegel remainder when the height index wins (§4).
2. **The direct test passes, and the budget is nearly used.** A program
   that shares no code with the project's checkers computes \(H_t\) from
   the heat-kernel convolution of \(\xi\) at 26 points of the claimed
   domain. Every point satisfies the comparison, and the Riemann–Siegel
   main terms reproduce \(H_t/M_t(s_+)\) to within \(4.8\cdot10^{-6}\),
   where the note allows \(4.3\)–\(5.3\cdot10^{-5}\) for those error
   terms. At a point chosen
   so that the dominant Dirichlet polynomial nearly aligns
   (\(x\approx2.324\cdot10^6\), \(y=3\), \(t=10^{-4}\)) the value is
   \(|F-1|=0.6169\), against the budget \(0.6573\) and the premise
   \(7/10\): the \(\zeta(2)-1\) term is close to attained as \(t\to0\)
   (§3). Injecting the wrong heat coefficient makes the test fail.
3. **What the bound is worth.** The theorem is an explicit form, on
   \(X\ge2\cdot10^6\), of Polymath's absolute \(O(\log(2+X))\) local count.
   At \(X=2\cdot10^6\) it allows 39.4 zeros in a unit window, where the mean
   density is 0.95 and an explicit \(t=0\) bound gives 7.0 (Bellotti–Wong;
   it does not apply at \(t>0\)). The computations locate the loss. The
   Poisson kernel costs a factor \((41/9)\pi\approx14.3\) in the
   coefficient. The additive constant \(574/27\approx21.3\) is \(41/9\)
   times the Cauchy allowance \(14/3\), charged for a logarithmic
   derivative that measures 0.05–0.19. No consumer has appeared since
   Note 01's audit.
4. **Disposition.** Accept Notes 01–02 and the manuscript's results with
   the status "proved from named imports; one cross-model LLM review".
   Make the four small corrections in §7, update the status files, and
   freeze the project at this result until a consumer states a tolerance,
   as the proposal's stopping rule and the portfolio plan's line for 06
   require. The cutoff \(2\cdot10^6\) is a convenience, not a limit of the
   method; §5 gives planning numbers in case the count is ever needed
   lower.

## 1. Scope, artifacts and method

**Artifacts.** The project folder at repository `HEAD` `38da114`; its
files were last changed in `146b3f9` and the working tree was clean.
Digests are in Appendix A. I read, in full: the README, draft history,
proposal, Notes 01–02, the manuscript source, both checkers and their
records, the build record and the same-model
[Review 01](01_OPENING_LEDGER_REVIEW_CODEX_20261017.md); and, before
starting, the [patterns to avoid](../../../../avoid/README.md) (all twenty)
and the [result summaries](../../../../result-summaries/README.md), with
[11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)–[13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md)
in full. I also read the portfolio plan's lines for 06, Reply 03 §4, the
setup review §7, and the user's three requests in the project's
[Codex chat](../chat-histories/0001_2026-10-17T15-58-02Z_begin-heat-zero-count-investigation.json):
begin the work, continue and postpone review "until a few more rounds",
and write a draft manuscript.

**Source.** Polymath v2 was read in the arXiv HTML rendering, extracting
the LaTeX of every display: Theorem 1.3 and (5)–(24), Theorem 1.5,
Section 3 (Proposition 3.1, Theorem 3.2), (35)–(41), Lemma 5.1,
Propositions 6.1–6.3 with their proofs through (64), Corollaries 6.4–6.5,
and Section 9 through Remark 9.4. This workspace could not reach arXiv
directly, so the page was read in the desktop app's browser. I did not
render the printed PDF pages myself. The journal version (Res. Math. Sci.
6, article 31) is paywalled and was not checked for the three slips in §4.

**Method.** I re-derived every displayed inequality of Notes 01–02 and of
manuscript Sections 2–6 by hand (§2). I replayed both project checkers on
Edward's machine (Python 3.10.12): same results, exit codes 0, 1, 0, 1 as
recorded. I rebuilt the manuscript with `latexmk` on the same machine,
outside the repository: no warnings, 11 pages, and text identical to
the committed PDF. The independent program
[`numerics/claude-review/review_checks_claude_20261017.py`](../numerics/claude-review/README.md)
(mpmath only; imports nothing from the project) has seven sections:
direct comparison (A), the comparison disk (B), sampled carrier
inequalities (C), the Gaussian moment (D), the source observations (E),
benchmarks (F) and planning arithmetic (G).

## 2. What was verified

**Normalizations [V].** \(H_t\), \(\Phi\), \(\xi\), \(H_0(z)=\xi((1+iz)/2)/8\)
and \(\partial_tH_t=-\partial_z^2H_t\) match Polymath (1)–(4); \(x=2T\);
\(M_0,\alpha,M_t\) match (6), (9), (10); \(B_t(x+iy)=M_t((1+y-ix)/2)\) is
(11). The comparison function \(g(X,t)\), with constant \(11/8\) and drift
\(\tfrac t{16}\log\tfrac X{4\pi}\), is exactly Theorem 1.5's; the averaged
\(7/8\) appears only in the heuristic after the theorem, so Note 01 §2 is
right to keep \(11/8\). \(N_t\) and \(K_t\) (half-open windows, with
multiplicity) agree with Theorem 1.5's counting convention. Expansion
(39) is transcribed correctly with \(s_-=(1+iz)/2\) and
\(s_+=(1-iz)/2\). Proposition 6.1 is stated for every real \(\sigma\) and
\(T>10\), and Proposition 6.2 for every real \(\sigma\). Proposition 6.3
is restricted to \(0\le\sigma\le1\), \(T\ge100\), and the notes rightly
do not extend its final constants.

**Extraction lemma (Note 01 §4; manuscript Lemma 6.1) [P].** The disk
centred at \(U+\tfrac72i\) with radius \(\tfrac12\) maps to \(\operatorname{Re}s\ge2\);
the Cauchy quotient is \((7/10)/((1/2)(3/10))=14/3\). At
\(s=\tfrac94-\tfrac{iU}2\), \(|\alpha|\le L_U/2+\pi/4+3/U+81/(16U^2)\)
(from \(|s|\ge U/2\) and \(\log|s|\le\log(U/2)+81/(8U^2)\)) and
\(|\alpha'|\le1/U+6/U^2\); the chain rule
\(B_t'/B_t=-\tfrac i2\alpha(1+\tfrac t2\alpha')\) gives \(2003/8000\).
The paired Hadamard sum (Polymath (105)) is absolutely convergent in its
imaginary part, every term of \(D_t(U)\) is positive (mirror zeros
included), and the kernel floor is
\(\min_{5/2\le a\le9/2}a/(a^2+\tfrac14)=9/41\), with the factorization as
stated. The constants \(82123/72000\) and \(574/27\) are exact.

**Ordinary terms (Note 02 §3; Lemma 3.1) [P, F].** Both bounds in (4)
follow from the triangle inequality. The second is attained to first
order at \(\sigma=5/2\), where the three error terms align; the sampled
margin there is exactly \(25/(4x^2)\) at leading order (section C), which
confirms that the constant is not loose. With the exact weight
\(W_n=\exp\{\tfrac t4\log n(\log n-2\operatorname{Re}\alpha)\}\) and
\(\log N\le L/2+\pi/(16x)\), \(W_n\le1\) for \(n\le N\). The ordinary-term
error (6) holds, the dominant excess is at most \(\zeta(2)-1\le95/147\)
(using \(\pi<22/7\)), and the opposite sum is at most \(N^{(y+1)/2}\) times
the carrier ratio.

**Remainder lemma (Note 02 §4; manuscript Lemma 4.1) [P, F].** The
envelope (8) is right. The Taylor segment is horizontal at height \(T'\),
so it holds for every real \(u\). Its Stirling term is
\(1/(6(T'-0.66))\le(2/3)/(4D)\), and the \(+1\) covers it (§4.2). The
Gaussian moment formula (9) follows by completing the square and agrees
with quadrature to \(10^{-40}\) (section D). \(J_0<4/3\) and the
"factor below 2" hold (at \(\sigma=5/2\), \(t=1/2\), \(D=10^6-3\),
\(J_0=1.0000075\)). The coefficient summation reproduces Polymath's
(62)–(64) for \(u\ge0\) and \(u<0\). The fixed-index case analysis is
correct: the remainder lies in the displayed tail exactly when
\(\lfloor-u\rfloor+3\ge m\), so it is missed when the height index \(m\)
strictly wins (section E(iv)), and \(E_a\) bounds it with an enormous
margin (\(\log_{10}\) of the bound is \(-31744\) at \(a=300.5\), against
\(-19611\) for \(E_a\)). The tail \(\delta_3\) uses
\((u-\sigma)^2\ge\tfrac9{16}u^2\) for \(u\le-10\), \(|\sigma|\le5/2\),
which is right; \(f(14),f(15)<10^{-30}\) and the ratio
\(2.42k\,e^{-4k+12}\) are right. The bracket
\(\tfrac12\cdot\tfrac43+\tfrac{100}{300}=1\) is an equality; the strict
inequality comes from \(J_0<4/3\) and \(\sum\delta_j<100/a\) upstream
(see §6 on the checker's label).

**Carriers (Note 02 §5; manuscript Lemma 5.1) [P, F].** The integration
of \(\operatorname{Re}(\alpha+\tfrac t2\alpha\alpha')\) from \(C\) to \(A\),
with the denominator conjugated to \(A+iT\), gives (15). The exact
identity
\(G(A,T)-G(0,T)-AL/2=\tfrac14\log(1+A^2/T^2)+\tfrac12\log\tfrac{T^2+(A-1)^2}{T^2+1}+\tfrac14\int_0^A\log(1+\sigma^2/T^2)\,d\sigma\)
is right. I re-derived it, and it matches direct evaluation to
\(10^{-12}\) at \(T=10^6\). It is nonnegative because \(A\ge2\). Then
\(\partial_\tau G(0,\tau)=-\pi/4+1/(2\tau)+\tau/(1+\tau^2)\),
\(\operatorname{Re}(\alpha^2)\ge L^2/4-\pi^2/16\) and the \(T\to T'\)
displacement give (16). That bound is tight only to \(O(T^{-2})\) as
\(t\to0\) (sampled margin \(9\cdot10^{-6}\) at \(t=10^{-6}\)), but it is
valid. (17) and the budget
\(95/147+11/1000+1/25000+26/(2\cdot10^6)=96624791/147000000\) are exact.

**Imports [V].** The proof imports Polymath's (39)–(41), Lemma 5.1(v),
Propositions 6.1 and 6.2, (58) and (105), and Theorem 3.2 for the strip.
Through Proposition 6.2 and (58) it depends on Arias de Reyna
(Math. Comp. 80 (2011), Theorems 3.1, 4.1, 4.2 and 6.1), and through
Lemma 5.1(v) on Boyd (Proc. R. Soc. A 447 (1994)). I did not check
those two sources, and neither did the notes. Polymath's own
Proposition 6.3 integrates the same coefficient bounds over all real
\(u\), including \(u\to-\infty\), so the notes' reliance on them is of the
same kind, only re-centred at \(\sigma\in[-3/2,5/2]\). The manuscript
should still name these as imports through Polymath that were not
checked at their source ([avoid 16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md)).

## 3. The direct comparison and the disk [F]

Section A evaluates \(F=H_t/M_t(s_+)\) with \(H_t\) from Polymath (35) (a
trapezoid rule on \(v\in[-16,12]\), step \(1/4\); halving the step and
widening the range changes \(F\) by less than \(10^{-30}\)). It compares
\(F\) with the main-term approximant
\(f=\sum_{n\le N}b_n^tn^{-s_+-(t/2)\alpha(s_+)}+\frac{M_t(s_-)}{M_t(s_+)}\sum_{n\le N}b_n^tn^{-s_--(t/2)\alpha(s_-)}\).
Selected rows (all 26 are in the record). "Allowance" is the note's
\(1/25000+26/x\) for the ordinary-term errors and the remainders together.
"Majorant" is the note's \(\sum_{n\ge2}n^{-(1+y)/2}W_n\), which the note
bounds by \(\zeta(2)-1\approx0.645\). The note bounds the opposite branch
by \(11/1000\).

| \(x\) | \(y\) | \(t\) | \(\lvert F-1\rvert\) | \(\lvert F-f\rvert\) | allowance | majorant | opposite branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| \(2\cdot10^6\) | 3 | \(10^{-4}\) | 0.2809 | \(4.8\cdot10^{-6}\) | \(5.3\cdot10^{-5}\) | 0.6422 | \(6.8\cdot10^{-5}\) |
| \(2\cdot10^6\) | 3 | 0.05 | 0.2551 | \(3.0\cdot10^{-6}\) | \(5.3\cdot10^{-5}\) | 0.5396 | \(4.4\cdot10^{-5}\) |
| \(2\cdot10^6\) | 3 | 0.5 | 0.1045 | \(8.1\cdot10^{-7}\) | \(5.3\cdot10^{-5}\) | 0.1444 | \(8.2\cdot10^{-7}\) |
| \(2\cdot10^6\) | 4 | \(10^{-4}\) | 0.1975 | \(9.4\cdot10^{-8}\) | \(5.3\cdot10^{-5}\) | 0.3413 | \(3.0\cdot10^{-6}\) |
| \(10^7\) | 3 | \(10^{-4}\) | 0.5395 | \(1.0\cdot10^{-6}\) | \(4.3\cdot10^{-5}\) | 0.6435 | \(5.5\cdot10^{-5}\) |
| \(10^7\) | 3 | 0.5 | 0.1135 | \(2.1\cdot10^{-7}\) | \(4.3\cdot10^{-5}\) | 0.1196 | \(2.0\cdot10^{-7}\) |
| \(2324466.298474\) (stress) | 3 | \(10^{-4}\) | 0.6169 | \(4.0\cdot10^{-6}\) | \(5.1\cdot10^{-5}\) | 0.6424 | \(3.1\cdot10^{-4}\) |
| \(2324466.298474\) (stress) | 3 | 0.05 | 0.5205 | \(2.6\cdot10^{-6}\) | \(5.1\cdot10^{-5}\) | 0.5384 | \(2.0\cdot10^{-4}\) |

The stress abscissa was found by maximizing
\(\operatorname{Re}\sum_{n=2}^{40}n^{-2-iT}\) over \(T\in[10^6,1.2\cdot10^6]\)
(value 0.6083 against the maximum possible 0.6203), so that the
\(n\)-phases nearly align at \(y=3\).

The disk of the extraction lemma, at the stress abscissa (centre
\(U=2324466.298474\), so the bottom point is the stress point; 12 circle
points; the mean-value check reproduces \(F(w)\) to \(10^{-10}\)):

| \(t\) | max \(\lvert F-1\rvert\) on circle | \(\lvert F'/F(w)\rvert\) (lemma: 14/3) | \(\lvert B_t'/B_t(w)\rvert\) | \(D_t(U)\) (lemma: 8.337) | \((41/9)D_t(U)\) | theorem's count | mean density |
| --- | --- | --- | --- | --- | --- | --- | --- |
| \(10^{-4}\) | 0.6169 | 0.187 | 3.057 | 2.845 | 12.96 | 39.59 | 0.965 |
| 0.5 | 0.1404 | 0.045 | 3.057 | 2.988 | 13.61 | 39.59 | 0.965 |

Three readings. First, the comparison holds at every sample, including
the near-worst alignment. The sample leaves 0.083 below \(7/10\), and
since the dominant excess can approach \(\sum_{n=2}^Nn^{-2}\approx0.642\)
when the phases align, the worst-case reserve as \(t\to0\) is only about
0.05. Polymath's "\(\pi^2/6-1\) against 0.7" really is the binding term,
and the extraction cannot simply take a larger \(q\).
Second, the count's looseness lies in the extraction, not in the
comparison. From the measured \(D_t(U)\), \((41/9)D\approx13\), against
the theorem's 39.6, and the remaining factor of about 14 over the mean
density is the Poisson kernel at height \(7/2\). Third, these are
samples: they test normalizations and implementation, and they say
nothing between the samples. With the heat coefficient deliberately
changed to \(t/2\) (`--inject-normalization`), every point fails,
including \(t=10^{-4}\), where \(|F-f|=9\cdot10^{-4}\) against an
allowance of \(5.3\cdot10^{-5}\). So the test would have caught the slip
discussed in §4.1 had it entered the carrier.

## 4. The three source observations [V, P, F]

**4.1 The heat coefficient after (99).** Confirmed. The proof of
Proposition 9.1 displays
\(\operatorname{Re}s_*\ge\tfrac{1+y}2+\tfrac t2\log\tfrac x{4\pi}-O(x^{-2})\),
while (17) gives \(\operatorname{Re}s_*=\tfrac{1+y}2+\tfrac t2\operatorname{Re}\alpha\)
with \(\operatorname{Re}\alpha=\tfrac12\log\tfrac x{4\pi}+O(x^{-2})\),
which is (21)'s \(t/4\). Numerically \(\operatorname{Re}s_*\) exceeds the
\(t/4\) form by \(7.5\cdot10^{-13}\) and falls short of the \(t/2\) form by
1.497 at \(x=2\cdot10^6\), \(t=1/2\) (section E(ii)). The exponents of
\(e_A,e_B\) and the sum after "By (15)" inherit the slip. Polymath's
asymptotic conclusion survives the correction: with \(t/4\) the exponent
of \(n\) is \(-\tfrac{1+y}2-\tfrac t4\log\tfrac x{4\pi n}+O(x^{-1})\), and
\(\log\tfrac x{4\pi n}\ge\tfrac12\log\tfrac x{4\pi}-O(x^{-1})\) for
\(n\le N\), so a bound \(ct\log x\) still holds with a smaller \(c\).
Note 01's "does not refute Theorem 1.5(iv)" is the right scope.

**4.2 The inequality before (60).** Polymath bounds the Stirling term by
writing \(\frac1{12(T'/2-0.33)}\le\frac{1/3}{4(T-3)}\). The left side is
about \(1/(6T)\) and the right side about \(1/(12T)\), so the printed
inequality is false for every \(T\ge6\), by a factor that tends to two
(\(1.678\cdot10^{-3}\) against \(8.59\cdot10^{-4}\) at \(T=100\); section
E(i)). With the correct \(2/3\), Polymath's envelope
\((\sigma+\sqrt tv)^2+\tfrac56\) becomes \((\sigma+\sqrt tv)^2+\tfrac{11}{12}\).
That is a negligible change to (59), (61) and (65): for example, the
\(10/3\) of (61) becomes \(41/12\). The notes avoid the slip by using
\(u^2+1\), but the manuscript calls it a "compressed constant". It is
clearer to say that the printed inequality fails by a factor of about two,
give the corrected \(2/3\), and say it is harmless
([avoid 08](../../../../avoid/08_normalization_and_constant_slips.md):
record the size of a slip, not only that one exists).

**4.3 The remainder omitted from Polymath's display for (63).** Confirmed.
Polymath chooses \(\tilde K_u=\max(\lfloor-u\rfloor+3,\lfloor T'/\pi\rfloor)\)
and then bounds everything above index \(T'/\pi\) by a tail over
\(T'/\pi\le k\le-u+4\). When \(\lfloor T'/\pi\rfloor>\lfloor-u\rfloor+3\),
the remainder \(RS_{\tilde K_u}\) has index \(\lfloor T'/\pi\rfloor+1>-u+4\)
and is not in that tail. Its size is at most \((5/a)e^{-4a^2/5}\), so the
omission does not affect Polymath's numbers; Note 02's \(E_a\) restores
it. This deserves the same plain sentence in the manuscript.

A smaller point in the same section: Polymath's proof of (iv) applies
Proposition 9.1(ii), stated for \(3\le y\le4\), through a Cauchy formula
centred at \(X+4i\), which needs a neighbourhood that leaves that strip
(the proof of (ii) works for larger \(y\), so nothing breaks). Note 01's
disk, centred at height \(7/2\) with radius \(1/2\), avoids the issue
and is the cleaner choice.

## 5. Value, consumers and the cutoff [R, F]

The portfolio plan's rule for 06 reads "stop that application when the
count uncertainty removes its proposed gain. A separately useful explicit
theorem may survive." The explicit theorem survives, and the
applications are where Note 01 left them. The winding-box interior count
needs the exact integer 2 at \(x\in[25,45]\), which an upper bound cannot
supply. Investigation 01's velocity route is dormant, and its
[latest contract](../../01_dirichlet_newman_families/notes/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md)
still places counts in that route. A velocity also needs more than an
upper local count. The proposal's consumer table asks a tail consumer
for a summable distance kernel, and the principal-value kernel of
\(\sum'1/(z_j-z_k)\) is not summable, so its tail needs the symmetric
cancellation, which takes two-sided cumulative information. An upper
local count bounds only tails such as \(\sum1/|z_j-z_k|^2\). Reply 03
predicted that an explicit positive-time count would be
weaker than the time-zero one, and section F quantifies by how much:

| \(X\) | theorem | sharp constants | mean density | explicit \(t=0\) bound |
| --- | --- | --- | --- | --- |
| \(2\cdot10^6\) | 39.4 | 37.8 | 0.95 | 7.04 |
| \(10^{10}\) | 49.6 | 47.5 | 1.63 | 8.39 |
| \(10^{20}\) | 77.3 | 73.8 | 3.46 | 32.0 |

The last column is Bellotti–Wong ([arXiv:2412.15470v2](https://arxiv.org/abs/2412.15470),
Corollary 1.6) for \(N(T+1)-N(T)\) with \(T=X/2\), which contains the
half-unit \(T\)-window of a unit \(x\)-window. It is a benchmark at
\(t=0\), outside the theorem's domain, not a competitor.

**The cutoff is a convenience.** Note 02 chose \(T\ge10^6\) so that the
remainder bracket is at most 1 once \(a>300\). Section G carries the
remainder constant \(K_R(a)=\tfrac12e^{14/(T-6)}+97.374/(a-0.865)+2/a\)
as a function of \(a\) instead. The notes' own budget for the
\([3,4]\) band then closes from \(x\approx7.9\cdot10^4\), where the
opposite-branch bound \(4Q^{-1/2}\) becomes the binding term. Moving the
disk up to \(4\le y\le5\) (centre \(\tfrac92i\), kernel floor \(11/61\))
lowers the dominant excess to \(\zeta(5/2)-1\approx0.342\) and the
opposite bound to \(4Q^{-3/4}\). With the same ingredients, extended to
\(\sigma\le3\), that gives about \(1.39\log(X+2)+5.8\), or 25.9 at
\(X=2\cdot10^6\) against 39.4, from \(x\approx2.2\cdot10^4\) under the
side conditions as written. These are planning numbers from my
arithmetic, not proved extensions: Lemma 4.1 would have to be restated
with \(K_R(a)\) and its side conditions rechecked. They matter only if
a consumer appears. Using the comparison's actual budget \(q=0.657\) in
the Cauchy step instead of \(7/10\) would already lower \(574/27\approx21.3\)
to about 17.4, at no cost.

I found no explicit-constant zero count for \(H_t\) at \(t>0\) in a brief
search, but that is not an originality search. The manuscript rightly
makes no priority claim, and house rule 2 of
[`CONTRIBUTING.md`](../../../../CONTRIBUTING.md) applies before any
external use.

## 6. Records, reproducibility and conventions

- **Replays [V].** Both checkers reproduce their records, including the
  two failure injections. The hashes of the notes, scripts, source and
  PDF match the run records and the build record. The checkers verify
  rational arithmetic only, as they say; the counts of checks (19 and
  51) are not used as evidence anywhere, which is right
  ([avoid 04](../../../../avoid/04_counts_and_precision_as_evidence.md)).
- **One checker label [R].** "full remainder bracket strictly below one"
  tests the equality \(\tfrac12\cdot\tfrac43+\tfrac{100}{300}=1\). Rename
  it, or test the strict chain it stands for
  ([avoid 11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md)).
- **Build [V].** The source compiles cleanly. The rebuilt text matches the
  committed PDF, and the author field ("Drafted for Edward Baker"), the
  LLM acknowledgement and the model attribution are as the project
  requires.
- **Status lag [R].** The [portfolio README](../../README.md) still lists
  06 as "Waiting for a precisely stated consumer". The
  [research-overview index](../research-overview/README.md) still calls
  the proposal "Current opening plan; not executed". The project README
  and [draft history](../DRAFT_HISTORY.md) say that review is deferred.
  The owner of those files should update them in the commit that adds
  this review ([avoid 19](../../../../avoid/19_status_files_that_lag_the_findings.md)).
  The draft-history entries identify their sources by hash; adding the
  commit `146b3f9` would follow the convention that milestones reference
  commits.
- **The compiled PDF.** Edward's stated convention is that manuscripts
  keep only the `.tex` source. All five investigations-3 manuscripts
  commit their PDFs, and [`LARGE_FILES.md`](../../../../LARGE_FILES.md)
  treats compiled PDFs as normal small files. This is a portfolio-level
  choice, not a defect of this project.

## 7. Disposition and recommendations

**Disposition.** Accept Note 01, Note 02 and manuscript Theorems 1.1–1.2
with Lemmas 3.1, 4.1, 5.1 and 6.1 as proved from the named imports, with
this as their one cross-model LLM review. No specialist human review has
taken place. The manuscript is a complete and honestly scoped working
draft of an explicit lemma.

1. **Freeze [R].** Stop at this result. Do not open the range
   \(200\le X<2\cdot10^6\), the cumulative count or constant optimization
   until a consumer states its kernel, domain and tolerance
   ([avoid 10](../../../../avoid/10_numerics_ahead_of_the_question.md),
   [20](../../../../avoid/20_volume_without_a_gain.md)). If one appears,
   §5 gives the inexpensive levers.
2. **Four corrections [R].** (a) In the manuscript appendix, state §4.2
   and §4.3 plainly, as slips of stated size that do not affect
   Polymath's results. (b) In §1 of the manuscript, add the mean density,
   the \(t=0\) benchmark and the loss decomposition of §3, so that a reader
   sees the price of uniformity in \(t\). (c) In §2 of the manuscript, name
   the Arias de Reyna and Boyd bounds as imported through Polymath and not
   checked at source. (d) Rename the checker test noted in §6.
3. **Status files [R].** Update the portfolio README row, the
   research-overview index, the project README and the draft history to
   record this review and the freeze.
4. **Result summary [R].** After (2), the explicit count meets the
   [result-summaries](../../../../result-summaries/README.md) rule
   (written proof and one review in the tree). A two-line entry in
   summary 11, with the status words above and its scope
   \(X\ge2\cdot10^6\), would make it findable. I have not edited the
   summaries.

## Appendix A. Artifact digests at review (SHA-256, first 16 hex digits)

| File | Digest |
| --- | --- |
| `README.md` | `01aebb9c29a8020f` |
| `DRAFT_HISTORY.md` | `8f6c633762dce668` |
| `research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md` | `672e68e10b4ef923` |
| `notes/01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md` | `46266338f670fde0` |
| `notes/02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md` | `ad3e9893648e47a8` |
| `numerics/check_local_count_reduction.py` | `e6d6912113e9c4a0` |
| `numerics/LOCAL_COUNT_REDUCTION_CHECKS_20261017.json` | `fcb4d803330e47c9` |
| `numerics/check_off_axis_comparison.py` | `934cca6a2c1fe023` |
| `numerics/OFF_AXIS_COMPARISON_CHECKS_20261017.json` | `f10ab518e2b9a9ee` |
| `reviews/01_OPENING_LEDGER_REVIEW_CODEX_20261017.md` | `54b98e3ad86ab826` |
| `manuscript/explicit_heat_zero_counts.tex` | `24ad21c235eec117` |
| `manuscript/explicit_heat_zero_counts.pdf` | `1980bcbc29780bdf` |
| `manuscript/BUILD_RECORD.json` | `5f18ef436887c8ee` |

## Appendix B. Computations

[`numerics/claude-review/`](../numerics/claude-review/README.md) holds
the program and its record. Run from that folder:

```sh
python3 -I review_checks_claude_20261017.py --output /tmp/REVIEW_CHECKS.json
python3 -I review_checks_claude_20261017.py --sections A --quick --inject-normalization   # must exit 1
```

The record [`REVIEW_CHECKS_CLAUDE_20261017.json`](../numerics/claude-review/REVIEW_CHECKS_CLAUDE_20261017.json)
was produced in the cloud workspace with Python 3.13.16 and mpmath
1.4.1, script SHA-256 `dba938e819303732…`, in 640 seconds, with status
pass. On Edward's machine, with Python 3.10.12 and mpmath 1.3.0, sections
C–G gave byte-identical numerical content, the quick form of section A
gave the same digits, and the normalization injection failed at all four
of its points with exit status 1. The stress-point search that chose
\(x=2324466.298474\) used numpy once and is not part of the program; the
program uses the abscissa as a fixed input.
