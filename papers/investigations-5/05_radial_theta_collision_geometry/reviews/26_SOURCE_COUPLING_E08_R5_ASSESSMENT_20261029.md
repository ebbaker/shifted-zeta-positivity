# CTF-E08 R5: source-coupling assessment and integration

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 **chat0024**, **Continue radial theta research**.

**Accepted without mathematical correction, within the inherited prepared
radial class on [0,1/2] x [1,6].** This executes the five checks in the
[frozen R5 packet][packet] and integrates its supported consequence.
The gain is 49/600 in the compact compression coefficient. It supplies
no independent compression bound through a collision deadline.

This is a separate-chat **same-model internal assessment** of Astra/max
[Note47][n47], with shared inherited premises. The current chat actually
runs Astra/max; the handoff's Sol recommendation did not change that
setting. The author subsequently acknowledged the missed model switch.
No subagents, cross-model check, formal proof or specialist review are
claimed. [Self-assessment25][r25] remains the authoring check, not a
substitute for this execution return.

## 1. Complete-tail and source-slope audit

All ten packet hashes matched at intake. The exact complete density
factorization is Note40 (1), with q=r^2 in Note47 (2). The positive
tail is independent of T. For each n>=2 and q>=4, write
x=pi(n^2-1)q>=36. Differentiating twice gives exactly the three
majorants n^4 exp(-x), n^4(1+x)exp(-x), and
n^4(x^2+2x+2)exp(-x). In the second derivative the two negative
terms involving beta/q are both retained. Their common bound is
2n^4 exp(-x/2). The geometric comparison uses n^4<=16^(n-1) and
n^2-1>=3+5(n-2); it sums every square, with no finite truncation.
The result is <64 exp(-18)<1/4096<epsilon=1/100. These summable
majorants justify differentiating on the entire q>=4 half-line.

For p0=1-beta/q and t=tau/p0, the first quotient constant is
8/7+8/49=64/49. The second is
8/7+16/49+16/49+16/343=632/343. Thus, with
z=2qP_q/P and z0=2beta/(q-beta),

\[
 |z|\le\frac{221}{700}<\frac13,\qquad
 |2qz_q|\le\frac{389041}{490000}<1.
\]

The term 9 epsilon^2 in the second bound is essential accounting for
the square of t_q; it has not been omitted. These constants were also
recomputed with exact rational arithmetic as a transcription check;
the written infinite-tail argument, not that finite calculation, proves
the universal estimate.

For L=-r ell'_T, direct differentiation gives
L>=5q, rL'<=(65/4)q, and rL'-2L>=13/12, uniformly in
0<=T<=1/2. The lower bound for log2 follows by pairing x and 3-x
inside its integral. Consequently c_T=(log r)L is strictly positive
before division, and 2<=rc_T'/c_T<=19/4. The unchanged drift has
lambda<=6/5 and 0<=-rd'<=2; since L>=20, its correction is <=1/10.
Thus k<=29/5<6 and k>=2 on r>=2. No division is used at r=0 or r=1.

The classical square-series convention was checked at
[NIST DLMF 20.2.3](https://dlmf.nist.gov/20.2.E3), retrieved 29 October
2026, using the existing [reference record][reference]. That formula
does not establish these source-slope inequalities; they are the
analytical argument in Note47 checked above. No new external theorem
or reference acquisition is needed.

## 2. Signed completion and full payments

The radial commutator is C1 W=a1 W'-k c_T W, with
a1=r(r lambda' log r-lambda)<0. Substitution of the actual definition
Z=omega(a_b W'+c_TW-Theta) gives

\[
 \omega\mathscr C_1W=-kZ+
 \omega\{(a_1+ka_b)W'-k\Theta\}.
\]

The minus sign on kTheta is correct. The bound
abs(a1)/a_b<=53/25<4<=2k proves abs(a1+k a_b)<=k a_b.
The fixed r>=2 bounds omega a_b<=2/25 and omega<=1/25 give
the exterior payment -2Y_out+(48/625)G_out+(12/625)||Theta||_out^2
after Young's inequality. Theta=(AV,V+AJ2) uses the actual fixed-mark
second derivative, not -u^2U; its full cost is <=38E_out+72Q_out.

With the unchanged C0 diffusion payment and exact radial remainder,
the four exterior coefficients are

| Energy | Exterior coefficient | Check against 274/25 |
| --- | --- | --- |
| G | 6298/625 | Strictly smaller |
| Y | 217/24 | Strictly smaller |
| Q | 4614/625 | Strictly smaller |
| E | 14949/2500 | Strictly smaller |

Inside r<2, the respective coefficients are 10+B1,
274/25+B1+B0, 6 and 21/4+B0. The weight maximum follows from
h'_omega(q)=(11-q)/(1+q)^3. These are coefficients of disjoint
restricted energies; no full energy is counted twice. Their maximum is
bounded by kappa1,src=274/25+B1+B0. The entire C0 term, including
all cutoff derivatives and second-order forcing, still consumes only
one of the two units of N and leaves the same kappa0 allowance.

The full integrals are derived before the r=2 partition, which is never
differentiated. There is no additional flux or transmission condition.
The origin extension, all inner energies, and R=-Theta at r=1 remain.
No two singular quotients are estimated separately. The original
prepared Schwartz/weighted class and its continuation theorem are
imported from Notes28/40 within their stated hypotheses; this assessment
does not reprove that local PDE construction.

## 3. Consequence, controls and evidence scope

Integration with exp(-kappa0 s-kappa1,src B) preserves the weighted
dissipation and alpha H_rad on the left. The same fixed-ball bound
follows from omega^(-2)<=(1+R_b^2)^4. Exact arithmetic gives

\[
 \frac{265}{24}-\frac{274}{25}=\frac{49}{600},\quad
 \frac{274}{25}+\frac{69}{4}=\frac{2821}{100},\quad
 30-\frac{2821}{100}=\frac{179}{100}.
\]

Hence U_src/U_rad=exp(-49B/600), with the same initial energy,
kappa0 and actual B. This compares upper allowances, not actual
energies. B is still unknown beyond the existing independently paid
local interval; no improvement to the best gradient-only interval,
first-jet floor, collision-free rectangle or threshold coverage follows.
Equally informed direct analysis has the same estimate.

The [registered controls][controls] were screened against the actual
premises rather than rerunning their witnesses:

| Control | Premise/domain distinction and outcome here |
| --- | --- |
| Exact Gaussian-polynomial at (1/4,2sqrt6) | Literal theta raw source identity fails; with the same theta operator both preparation-commutator and raw-mismatch terms remain. It satisfies the new estimate and still breaks down by its own deadline. |
| Weighted-square | Unit coefficients/full reflection fail; witnesses near 44.13 and 83.53 are outside A in [1,6]. |
| Finite-prime orbit | Selected-prime constraints do not supply full reflection; high-gap events have no fixed location in this compact rectangle. |
| Reflected super-Gaussian | Complete square arithmetic fails; pi/4 witness is below the rectangle. |
| Smooth shape / positive primitive | Named shape/primitive data do not specify the literal theta amplitude; no new witness location in this rectangle is asserted. |
| Euler-factor | Arithmetic and conductor change; a Laguerre witness is not automatically a double event in this rectangle. |
| RH-conditional endpoint | Keep its RH assumption, failed ordinary Dirichlet arithmetic and escaping double heights. |
| Atomic / continuous compact | Atoms are outside the imported smooth source-function theorem; admissible prepared comparisons retain their actual raw mismatch. |

Failure of a literal theta source premise does not imply failure of this
same-operator estimate. In particular the theta-only vanishing of the
raw mismatch is not used in the new production bound. The limitation
is about this proof and this comparison class, not all possible coupled
or trajectory-dependent estimates. See [target classification][a01],
[shape controls][a02], [scoped exclusions][a07] and [combined bounds][a12].

## 4. Integration and disposition

Section 7.5 of the [existing manuscript][manuscript] now contains
Proposition 7.8, equations (7.29)-(7.36), with one complete added proof.
The abstract, introduction, remaining-estimate discussion,
acknowledgment and references are updated proportionately. All 14
inherited proof blocks remain byte-identical and in order (15 total).
The author field, original source/flow/preparation/cutoff, actual jets
and companion source are retained. Issued packets, Notes31/39-48 and
prior reviews remain unchanged.

The saved source compiled successfully in the built-in compiler and
locally to 28 pages. The final local log has no warnings or
overfull/underfull boxes. All pages received contact-sheet inspection;
pp.1,2,21-28 received full-page PNG inspection at 120 dpi. No visible
clipping, overlap, missing glyphs or unresolved references was found
in that bounded scope. This is not a line-by-line audit of every page
or mathematical validation by compilation. [Record24][build] carries
source/PDF/log hashes, exact finite arithmetic and preservation checks.

**CTF-E08 R5 complete; parent B02 remains partial.** No new candidate,
radius optimization, source acquisition, PDE simulation or coverage
extension was performed. The [research return][return] states the
accepted result; [Continuation50][next] routes the next conceptual
choice to **[B] CTF-B02 — Astra**. A fixed execution contract should
then go to Sol; no redundant E07/E03 stage is issued for this proof.

The [result index][results] and [avoid index][avoid] are navigation and
status discipline, not additional validation. Thread identity:
01a188b4-0e1a-7522-8c93-30235f85ae00; initial turn identity:
01a188b4-ee1b-76c2-a89d-4ec0bf50abbe. The [own public history][history]
is uniquely registered as chat0024. Registry metadata, not this prose,
own its current capture counts and hashes.

[packet]: ../research-progress/handoffs/CTF-E08_SOURCE_COUPLING_ASSESSMENT_REQUEST_R5_20261029.md
[n47]: ../notes/47_EXTERIOR_SOURCE_RESIDUAL_COUPLING_B02_R5_20261029.md
[r25]: 25_SOURCE_COUPLING_B02_R5_SELF_ASSESSMENT_20261029.md
[reference]: ../references/01_CIRCLE_HEAT_AND_JACOBI_NORMALIZATIONS_20261027.md
[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[build]: ../numerics/24_SOURCE_COUPLING_INTEGRATION_BUILD_RECORD_20261029.json
[return]: ../notes/49_SOURCE_COUPLING_E08_R5_RESEARCH_RETURN_20261029.md
[next]: ../notes/50_SOURCE_COUPLING_INTEGRATION_AND_MODEL_CONTINUATION_20261029.md
[history]: ../chat-histories/0024_2026-10-29T17-27-43Z_continue-radial-theta-research.json
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
