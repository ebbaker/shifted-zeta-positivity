# Chat0003 research summary and next-session handoff

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**.
Entire conversation: **Derive negative-time correction**, ansatz chat0003,
thread `01a17626-abf5-7a90-9ba2-7a2395254aee`.

## Outcome and authority

This chat executed **HDA-A02-AN03, AN04, AN05 and AN06**, each at the
user's request. AN03/AN05 are bounded analytical results; AN04/AN06 are
their faithful manuscript integrations and production checks. The first
negative-time curvature correction and its fixed compact-away-zero
family are **proved in-note from named classical inputs, same-model
internal analytical assessment only**. No independent specialist review
or numerical/machine-symbolic research was performed.

The [maintained manuscript][tex] now contains the [1,2] result in
Section6.3/Proposition6.1 and compact family in Section6.4/Proposition6.2,
with explicit endpoint/onset Appendix A. Current reading copy: 33 pages,
no warnings, all-page visual review; [AN06 build record][build] binds
source/PDF hashes and checks. Older stronger growing-order theorem is
now Proposition6.3 and keeps its old scope. No snapshot folders or
commit/tag were created. The PDF is generated in ignored repo-root
output/pdf/heat_density_ansatz/, not a tracked manuscript source.

[Progress02][ledger] is the sole live ledger, [Overview02][overview] the
current acceptance contract. **HDA-A02 Partial; HDA-17 Partial,
HDA-18 Gated, HDA-20 unfulfilled.** A03-AN01 stays deferred supporting;
no status promotion follows from these results or clean builds.

## Mathematical setup to preserve

Canonical heat convention is H_t=-H_zz with
`H(0,z)=xi((1+iz)/2)/8`. Negative time is t=-T, T>0. Let
`L=log(X/(4pi))`, `N=floor(sqrt(X/(4pi)))`,
`M(w)=w(w-1)pi^(-w/2)Gamma(w/2)/16`, `alpha=M'/M`, and
`w_e(z)=(1+e i z)/2`, e=+1,-1. With s=(1+iz)/2, the nonzero gamma envelope is
`G(z)=[M(s)M(1-s)]^(1/2)`, using the real-positive branch at the chart
center and its analytic continuation on the fixed chart.

Retain full charts with r=ell+2, b=1+h+2 and one extra analytic unit.
Cutoffs, chart center, real initial partitions and integration endpoints
are frozen in z and T. Do not spatially differentiate a height-dependent
cutoff or insert a localization commutator into the exact global identity.
Physical q, fixed K, xi anchor and normalization remain inherited.

For each mode define
`h_en=M(w_e)n^(-w_e)`,
`beta_en=(log h_en)_z=e i/2[alpha(w_e)-log n]`,
`gamma_en=beta'_en=-alpha'(w_e)/4`.
The evaluated first mode correction is

    A_en(T,z)=h_en(z) exp(T beta_en(z)^2)
              [1+gamma_en(z)(T+2T^2 beta_en(z)^2)].

The model retains every n<=N mode plus the bounded real-data integral
of `Q_X1(u)=S_m(u)-S_N(u)+R_m,1(u)`, where m is the true real cutoff,
RS order K_RS=1 retains C0 and C1, and adjacent cutoff transfers are
exact. This is not an integral-free short formula or a full unevaluated
Duhamel solution. The integral itself solves the homogeneous heat equation
on frozen charts. Its real-data form does not assume unproved C1
coefficient regularity or continue gamma modes through remote poles.

## AN03: first evaluated correction on 1<=T<=2

[Note10][n10], [Assessment07][r07],
[AN03 work record][w03] and [AN03 return][p03] hold the details.
Use initial window [X-8L,X+8L]. The correction above with independent
K=1 initial matching yields, uniformly on full target charts,

    |partial_z^j(H-F)| <= C |G| X^(-5/4),  0<=j<=3,
    |partial_t(H-F)|  <= C |G| X^(-5/4),
    |r_F|+|partial_z r_F| <= C |G| X^(-7/4),
    r_F=F_t+F_zz.

There are no log losses in these fixed-buffer bounds. This improves
the old natural gamma-scale X^-3/4 field allowance by X^-1/2.
The field proof pays initial mismatch independently of residual
cancellation. Using only old K=0 RS data would leave the X^-3/4
allowance even after the mode residual improves.

Key payments: cancel transverse height/n powers before absolute values;
pay the full O(X^1/4) weighted population; bound local gamma curvature
at X^-2 per mode; retain complex Gaussian weights and every true and
artificial tail. Weighted moments give X^-7/4 arithmetic error, while
K=1 RS initial error dominates at X^-5/4. Fixed-margin Cauchy gives
spatial j<=3 without differentiating target-centered polynomials as if
only the kernel varied. First time comes from direct kernel
differentiation or the already established error PDE and residual.

The equivalent elementary-arm display is retained only on [1,2]:
`D_en(t,z)=e i/z[1/24-t/4-(7t/4)B_en-(t^2/8)B_en^2]`,
`B_en=b_e-log n`. Both the initial gamma phase and slope terms matter.
It does not replace the RS integral. Exact product residuals are checked
separately from actual canonical solution comparison.

Mode damping is exp(-T k_n²). Fixed-n damping involves T log²X;
relative arithmetic damping involves T log X. There remain order sqrt X
near-cutoff modes and absolute arm weight comparable to G X^1/4.
Neither the absolute population nor first-correction absolute weight is
a leading asymptotic for the signed sum H. Do not drop the population
from a one-mode damping picture.

## AN04: first integration

[Note11][n11], [Assessment08][r08] and the historical
[AN04 build record][b04] integrated the preceding result into
Section6.3/Proposition6.1, with retained integral, failed outer allowance
and physical consumer explicit. That milestone built at 29 pages with
zero warnings and preserved all 73 then-inherited math blocks. It was
production work, not a new estimate or independent proof validation.
Its PDF hash is historical because AN06 rebuilt the stable output path.

## AN05: every declared fixed compact-negative-time family

[Note12][n12], [Assessment09][r09], [AN05 work record][w05] and
[AN05 return][p05] extend the exact-gamma formula to every **declared
fixed** `0<tau<=T<=B<infinity`. Freeze
`V_B=8 sqrt(max(1,B))L`, use window [X-V_B,X+V_B], retain all modes,
K=1 RS data and exact transfer. The same powers above hold with
explicit endpoint/buffer constants and sufficient onset gates.

Do not replace those constants with an unexplained generic compact-time
constant. CF7/11/15/16/22/25 display the endpoint factors, CF24 the gates,
and CF26--28 the bounds. The manuscript Appendix A reproduces them:
M_m/T_m pay complex kernels and time differentiation; Pi_d/W_d pay
the complete damped population; P2/P3 pay mode residual polynomials;
D/J factors pay true-initial, artificial-polynomial and far-source tails.
The field factors are E=3+M0+M3+M4 and E_t=3+T0+T3+T4;
residual factor is R=Pi4(P2+P3). Time can alternatively use a
buffer-dependent multiple of E+R. Remaining constants depend only on
fixed buffers and named classical inputs.

The gates include classical RS/gamma validity, window/comparability,
threshold crossing, slope/curvature exponential control, tail absorption,
global-source tails and the near-cutoff lower-population smallness
condition. No numerical onset was evaluated. The factors and height
onsets degenerate as tau decreases to zero or B increases to infinity;
this theorem permits neither tau=tau(X) nor B=B(X).

For an overlap with [1,2], compare the differing window models to the
same canonical H only after both onsets. Do not equate their formulas.
The existing growing-order FN25 theorem and joined [-2,0] model keep
their own hypotheses, stronger outer-scale accuracy and separate
residual terms. AN05 does not enlarge their domain or prove a new join.

## Remaining outer loss and physical boundary

The envelope comparison is
`E_o(-T,z)>=c_rb |G(z)| exp(-T L²/16+pi²T/64)`.
Thus the new fixed-order family gives outer-relative allowances

    C_rb E   X^(-5/4) exp(T L^2/16-pi^2 T/64),
    C_rb R   X^(-7/4) exp(T L^2/16-pi^2 T/64).

The first-time factor is E_t. For every fixed positive T the positive
quadratic logarithm eventually dominates the algebraic gain: these
allowances grow. This is a failure of the displayed error budget, not
an actual error lower bound, a failed theorem at gamma scale, or a
universal obstruction to a better resummation. The previously proved
growing-order finite outer model remains stronger on its actual domain.

Insert the actual residual into PE37--39's potential, density and
current forcing equations, retaining their signs and all terms. The
first unpaid consumer is a regulator-uniform weak/collar comparison
between this new model and H, including actual signed Q. Small field
or residual errors alone do not give that consumer. No simplicity,
root-free collar, noncollision, full covariance/current transfer or RH
result was proved. Physical regulators and full joining defects remain.

## AN06: final integration and preservation

[Note13][n13], [Assessment10][r10] and [AN06 build record][build]
record Section6.4/Proposition6.2 and Appendix A. Final build: **33 pages,
zero warnings, no unresolved references**; all pages rendered and
visually inspected, selected pages read at full useful size. All 85
inherited equation/align/gather/proposition blocks appear verbatim.
Notes10--12, Reviews07--09, A03-AN01 and standing inputs were preserved.
Same-model read-only source audit found no remaining scope conflict.
A final notation fix defines real tail displacement v=u-X without
changing physical q. No source/PDF production check validates a proof.

Progress, overview, navigation, history guide, result cluster and avoid
lesson are current. Chat0003 retains its unique original number,
filename, creation and first-capture provenance. The recorder owns
capture counts/hashes; public text is refreshed, actual final capture
is arranged only after the completed turn. No raw transcript or private
reasoning is committed as research content.

## Scope limits, lessons and next action

Read the [result index][results], [heat-flow cluster11][r11],
[collision controls12][controls] and [avoid index][avoid], especially
[shared-premise05][a05], [scope07][a07], [separate bounds12][a12],
[checked imports16][a16] and [status19][a19]. This is an approximation
program, not an RH-equivalent criterion. The heat identities hold for
the collision controls too. Existing screen: Euler-factor controls fail
full canonical Dirichlet coefficients; weighted-square/theta-cutoff
controls fail canonical completion/RS; reflected, shape, primitive,
counter-kernel and fixed-event controls lack that complete arithmetic
identity. Those failed premises do not themselves prove noncollision.

The main methodological gains of this chat are independently paid
initial mismatch, full population and complex tails, derivative buffers,
and explicit endpoint dependence. Build success and shared-model review
must remain separate from mathematical validation. Fixed-family results
must remain separate from joint limits and through-zero assembly.

Still open: integral-free fixed-order correction, outer-scale resummation,
useful cost; enlarged negative-time join; compact-positive gap
1/2<t<32; joint positive/negative time-height limits; physical transfer,
full spatial/time assembly and fine regulator center/rounding. No new
mathematical result was added by AN06. The fine t=64 work remains useful
supporting research, with A03-AN01 preserved but deferred.

**Next owner — Analysis, Sol: [HDA-A08-AN01 r1][next]**, prepared only,
not executed or dispatched. Seek one canonical buffered field estimate
on **[1/2,1]**, with spatial j<=3, direct first-time error and actual
residual, paying every arithmetic and contour contribution. First pin
source hypotheses: parent Note27's positive Gaussian identity GO6 is
valid for t>0, while its GO7 estimate is stated strictly above64;
parent t>=32 and published small-positive-time inputs retain their
actual domains and strip restrictions. None is a theorem on [1/2,1]
by formal substitution. No Astra escalation is currently justified;
request it only for a named resistant mechanism.

> Please execute HDA-A08-AN01 r1 using Note14, Overview02 and Progress02.
> Pin actual source hypotheses and derive one canonical comparison on
> 1/2<=t<=1 with full fixed buffers, spatial j<=3, direct first time and
> actual heat residual. Pay all arithmetic/contour terms and preserve
> all prior domains. Stop at one proved slab or a precise failed estimate.
> Update research progress, notes, assessment, execution record and the
> affiliated chat history.

[tex]: ../manuscript/main.tex
[build]: ../manuscript/BUILD_RECORD_20261025_A02_AN06.json
[ledger]: ../research-progress/02_EVOLUTION_ASYMPTOTICS_RESEARCH_PROGRESS_20261025.md
[overview]: ../research-overview/02_EVOLUTION_ASYMPTOTICS_RESEARCH_OVERVIEW_20261025.md
[n10]: 10_FIRST_NEGATIVE_TIME_EVOLUTION_CORRECTION_20261025.md
[n11]: 11_AN04_MANUSCRIPT_INTEGRATION_20261025.md
[n12]: 12_COMPACT_NEGATIVE_TIME_FAMILY_20261025.md
[n13]: 13_AN06_MANUSCRIPT_INTEGRATION_20261025.md
[r07]: ../reviews/07_FIRST_NEGATIVE_CORRECTION_ASSESSMENT_20261025.md
[r08]: ../reviews/08_AN04_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261025.md
[r09]: ../reviews/09_COMPACT_NEGATIVE_FAMILY_ASSESSMENT_20261025.md
[r10]: ../reviews/10_AN06_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261025.md
[w03]: ../numerics/AN03_ANALYTICAL_WORK_RECORD_20261025.json
[w05]: ../numerics/AN05_ANALYTICAL_WORK_RECORD_20261025.json
[p03]: ../research-progress/handoffs/HDA-A02-AN03.md
[p05]: ../research-progress/handoffs/HDA-A02-AN05.md
[b04]: ../manuscript/BUILD_RECORD_20261025_A02_AN04.json
[next]: ../research-progress/handoffs/HDA-A08-AN01.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[a19]: ../../../../../avoid/19_status_files_that_lag_the_findings.md
