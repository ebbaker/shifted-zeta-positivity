# UAR analytic manuscript integration and generalization review

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring and reviewing model **gpt-6-astra
(Codex)**, actual reasoning effort **max**. This is internal self-review of
the new derivations and a cross-model assessment/replay of the inherited
Sol-ultra UAR results; no independent specialist review is claimed.

**Assessment:** the manuscript now presents coherent analytic cutoff
matching as a principal result and explains what the complete residual
estimate buys. Two further consequences are **proved in-note from the
stated inherited analytic estimates**: an explicit bound between arbitrary
endpoints in the original sector, and a qualitative compact-band extension
of edge and corrected-transition control. The latter has no new numerical
onset or explicit constants. Neither extends physical collision exclusion.

The [verification receipt][receipt] pins this fourteen-file manuscript,
its new [Section 13][section], [S03 Note 13][extension] and the relevant
inherited inputs. The [build record][build] preserves the previous version.
[Review 17][prior] retains its earlier source-version scope and research
ranking. The repository [result summaries][results] and [patterns to
avoid][avoid] apply, particularly [collision controls][controls],
[normalization][normalization], [signed recombination][pairing] and
[scoped claims][scope]. Classification: quantitative approximation and
residual estimates, not a new RH-equivalent or nonvanishing criterion.

## 1. Manuscript changes and inherited accomplishments

The abstract now identifies the coherent UAR-03 construction, full UAR-04
bound and analytic extensions. Sections 1–10 have unchanged bytes.
Section 11 clarifies that its coverage table concerns the full indicated
time slab and points to the later small UAR-05 island. Section 12's
then-open UAR work is brought up to date. Section 13 gives statements,
proof outlines and links to the longer analytic and numerical records.

The central accomplishment is uniform cancellation through a moving
arithmetic cutoff. The exact entering heat mode is compensated by the
Riemann–Siegel edge change before either is bounded. Keeping the true gamma
factor, heat phase, reflected channel and shared truncation lengths produces
one holomorphic edge model per frozen integer. Its error is below
1000 Z_c exp(-3.99 L), including infinite heat/contour tails and either
cutoff. Corrected transitions have a summable inverse-square allowance.

UAR-04 then pays the retained signed endpoints, finite gamma/heat correction,
all transitions and endpoint errors. Its ordinary-prefix bound is
3.246 exp(-13/(16t)) on the entire original sector. This is much stronger
than merely exhibiting a tiny omitted edge tail. These analytic statements
are the most reusable results of the round. The manuscript preserves their
actual contracts and separates the value of the retained integral from
the error of approximating it.

UAR-05 contributes one fully paid physical box, with rotating margin >.539
and energy/A^2>.27. UAR-06 shows that direct certification on that box
has the larger margin at the same dominant acquisition cost. The new
section records that completed scoped loss and its stopping decision.
It does not describe the new analytic extensions as reversing it.

## 2. Explicit arbitrary-endpoint corollary

For a=min(u,v) in the original J_t, S_a=exp(-3L_a/4-tL_a^2/16), Note 13
proves |I_t(u,v)|<3.246 S_a. The proof reruns the decreasing-envelope
argument at the actual lower endpoint; it is stronger than using the
generic difference of two original prefixes.

The following points were checked directly against UAR-03/04:

- The ordinary integral has the positive sum of Z_h because the residual
  jump is minus h. Initial right charts, terminal left/right descriptions
  and reversal are consistent. No distributional jump was inserted.
- At a crossing, 3 Z/n^2 <= 3 S/n. The envelope derivative is bounded
  below by (tL_a+6) S/(4v), so the transition sum is at most
  (3/U_a)S_a + [12/(tL_a+6)](S_a-S_b). The first discrete term is paid
  separately, including when a lies arbitrarily close to a crossing.
- With endpoint coefficient 1.53, maximizing over 0<=S_b/S_a<=1 yields
  1.53+max(1.53,12/(tL_a+6))+3/U_a <3.245. Both remaining endpoint
  errors fit within the reserve to 3.246. This maximization remains valid
  when 12/(tL_a+6) becomes smaller than 1.53.
- At t=.05 and L_a=30, the resulting bound is <3.3e-11. This illustrates
  a different starting-height contract; it is not an actual-error ratio.

The prior 2B rebasing deduction remains correct under the information
then used. On the UAR-05 box, which has no interior switch, the existing
local two-endpoint residual payment is stronger than this general
crossing allowance. The corollary therefore leaves UAR-06 unchanged.

## 3. Compact-band generalization and its limits

For a fixed positive band kappa_-<=tL<=kappa_+ and fixed p>eta>0, use
the same shared lengths V_t=S_t=sqrt(p kappa_+/t). Note 13 proves that,
for sufficiently small t, the complete edge error is at most
C Z_c exp(-(p-eta)L). Same-N overlap agreement and exact-mode compensation
are preserved. Fixed-order spatial derivatives follow from Cauchy on the
same radius-1/L disks. The original corrected jumps remain O(Z_c/c),
so their prefix sum has order
exp[-(kappa_-^2+12 kappa_-)/(16t)].

The proof uses uniform estimates rather than a finite parameter scan:

1. A fixed positive lower endpoint forces L,c and the saddle scale to
   infinity uniformly. The alternate cutoff still has saddle distance
   at most 1/2+o(1), and no contour pole or branch cut enters a disk.
2. The explicit normalizer formulas give P/|A|=O(Z_c) on the actual
   complex disk and |omega|>=L/5 on the real half-window.
3. UAR-03's global contour estimate and reflected gamma estimate yield
   a heat majorant C_0 exp[-(1-o(1))v^2+o(1)|v|]. Reflection remains
   necessary on the infinite left tail. The chosen lengths make the
   heat tails O(exp(-(p-eta)L)); central-heat contour tails are smaller.
   Their disjoint partition pays the entire omitted rectangle once.
4. The earlier Note 22 has an explicit printed-jump mismatch exponent
   O(1/c), uniformly for bounded t and radius <=1. The analytic single-wave
   conversion costs O(P/(Lc)); dividing by the actual normalizer and
   using coupled Schwarz–Pick produces the corrected-transition bound.

These steps support the qualitative proposition; they do not transfer
1000, 3.246 or t=1/20 to an arbitrary new band. A practical extension
should fix a target band first, compute the normalizer/tail/matching
constants and onset, and then extend the retained saddle and finite
correction estimates needed for the complete UAR-04 residual. For example,
[1/2,3] is a possible target contract, not a certified range at t=.05.

The result does not cover unbounded tL at a fixed t, a fixed-width complex
strip, larger positive times without fresh estimates, or a different
arithmetic source. Increasing p retains a larger contour and shrinks its
omitted tails; it does not bound the retained model's value or its
acquisition cost. Time derivatives require the moving truncation limits
and normalizer/forcing terms. Higher spatial error derivatives alone do
not provide a complete Laguerre or second-jet certificate.

## 4. Replays, controls and document verification

Fresh UAR-03 and UAR-04 scalar replays verify their 192/256-bit records.
A fresh UAR-06 replay verifies both production precisions, the physical
comparison and its source-own controls: five event-box rejections and the
separate Euler negative-Laguerre witness. These use the existing numerical
implementations and are not implementation-independent proofs.

The new [checker][checker] and [receipt][extension-record] verify the
arbitrary-endpoint coefficient reserve and example at 192/256 bits, plus
exact rational sign, endpoint and reversal fixtures. A polynomial double
event with zero residual still has zero physical margin once the complete
approximant variation is paid. No new compact-band numerical onset is
claimed by those checks. The written proofs supply uniformity.

The source premises are explicit. Finite-prime and weighted-square
controls lack the unchanged full theta coefficients/reflection; smooth,
reflected and positive-primitive controls lack its square expansion and
matching contour. Euler changes alter level or coefficients; polynomial
controls lack the gamma/RS source. Their generic endpoint identities do
not supply a physical anchor, and no theta constant is reassigned to them.

Three successful terminal passes produce a 52-page PDF without warnings
or overfull/underfull boxes. All pages were rendered and inspected in
contact sheets; pages 47–52 were also reviewed at page scale. Text and
link checks, source identities, desktop compilation and the installed
checker replay are recorded in the integration receipt/build record.
The first development compile exposed an undefined math font command,
which was replaced before the successful final passes. Compilation and
layout checks validate the document, not its mathematics.

## 5. Research priority after integration

The most promising continuation is to combine this uniform error control
with an estimate for separation of the retained arithmetic first jet over
a useful domain, or a demonstrably cheaper complete acquisition. In the
existing paid box the approximant variation costs about 1.0051, while the
direct residual allowance is below 1.341e-7. Further reducing an already
tiny omitted tail will barely change that particular margin.

The compact-band proposition establishes that coherent matching is not
tied to the arbitrary endpoints 1 and 2. Turning that flexibility into
larger certified domains requires explicit constants and a physical lower
margin. No all-sector noncollision, closed global bridge, complex exterior
or improved Newman bound is claimed by this milestone.

[receipt]: ../numerics/UAR_ANALYTIC_MANUSCRIPT_INTEGRATION_20261019.json
[section]: ../manuscript/positive_arithmetic_packets/sections/13_uniform_coherent_edge.tex
[extension]: ../symmetries/03_normalized_jet_rotation/notes/13_REBASED_RESIDUAL_AND_COMPACT_SECTOR_EDGE_EXTENSIONS_20261019.md
[checker]: ../symmetries/03_normalized_jet_rotation/numerics/check_rebased_residual_envelope.py
[extension-record]: ../symmetries/03_normalized_jet_rotation/numerics/REBASED_RESIDUAL_ENVELOPE_20261019.json
[build]: ../manuscript/positive_arithmetic_packets/BUILD_RECORD.json
[prior]: 17_ACCOMPLISHMENTS_AND_POST_UAR_RESEARCH_PRIORITIES_REVIEW_ASTRA_20261019.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[normalization]: ../../../../avoid/08_normalization_and_constant_slips.md
[pairing]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
