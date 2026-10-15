# Research priorities after the closed strip extension

14 October 2026 (America/New_York). Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from this conversation's current turn metadata. Parallel internal LLM readings informed the prioritization. This is a research proposal with conditional deductions; it proves no new theta sign estimate or extension of the covered domain.

The strongest program has two concurrent objectives: obtain the next strip theorem through a weaker weighted remainder estimate, and develop a signed stationary estimate that can reach the inner cusp. The second deserves the larger research investment. Completing the strip beginning at theta=5/2 would still leave the unbounded inner cusp and the finite transition above height 112.

Sources are [Note 32](32_CLOSED_STRIP_EXTENSION_AND_MIDDLE_BLOCK_LEMMA_20261014.md), [Note 31](31_SIGNED_CUTOFF_LEMMA_AND_THRESHOLD_EIGHT_THIRDS_20261014.md), [Note 30](30_THETA_SIGNED_CUTOFFS_AND_ANALYTIC_LOG_LOSS_20261014.md), [the collision analysis](28_COLLISION_SCALES_AND_DELAYED_COMPARISONS_20261014.md), and [the earlier research assessment](27_RESULTS_ASSESSMENT_AND_RESEARCH_PATHS_20261014.md).

Integration clarification, 15 October 2026: the source-envelope transfers below are used on declared positive-height domains with 0<t<=1/2. A collision conclusion requires that the domain contain the relevant nearby predecessor points; small-energy localization alone does not establish that coverage. These restrictions are explicit in the integrated manuscript.

Write h_k=partial_x^k H, E=h_0^2+h_1^2, L_j=h_{j+1}^2-h_jh_{j+2}, and S_j={h_{j+1}=0}, j=0,1. Let Gamma be the explicitly nonvanishing Stirling carrier magnitude used in Note 32; Gamma does not contain a zeta factor or a physical jet denominator.

## Prioritize the signed stationary estimate in the cusp

The RH-relevant target is a source-derived lower bound at the scale of the full physical energy, on both full stationary sets. Strict positivity everywhere is stronger than needed. A prescribed locally bounded loss L_j>=-K_j E suffices near every candidate positive-time collision and its predecessor branch. The collision pole is -L_j/E=r/(T-t)+O(1), with r>=1, so a bounded loss excludes the event.

A useful finite-resolution formulation is the full-amplitude observation from Note 31,

\[
J_{j,N}=-h_j h_{j+2}^{(N)}\quad\text{on }S_j.
\]

Seek, for all integers N>=N_0>=8,

\[
J_{j,N}\ge-A_j(t,x)N^pE-B_j(t,x)e^{-cN^2},
\tag{S}
\]

with fixed finite p>=0, c>0, nonnegative coefficients prescribed from the source, and A_j,B_j,c^{-1},N_0 locally bounded through candidate events. A uniform version on a first declared unbounded cusp subdomain would be an initial milestone; full RH coverage remains the eventual requirement.

The exact advantage of J is that it retains the full amplitude h_j. It vanishes at E=0 for j=0,1 without requiring every raw truncated Laguerre form to be nonnegative. This removes an unnecessary constraint imposed by an unpaid raw-cutoff inequality. It does not establish (S).

The transfer is elementary. Note 31 gives, for some source-prescribed locally bounded D_j,

\[
|J_{j,N}-L_j|\le D_j\sqrt E\,e^{-c_0N^2}.
\]

Young's inequality bounds this by

\[
\tfrac12E+\tfrac12D_j^2e^{-2c_0N^2}.
\]

Thus (S) implies the paid full-form family of Note 30 with adjusted constants. Optimizing N of order sqrt(log(1/E)) gives

\[
L_j\ge-C_jE[1+\log_+(M/E)]^{p/2},
\]

for fixed M>0. Note 30's analytic rigidity and the collision analysis explain why this excludes a collision in the covered domain. The polynomial cutoff loss is a quantitative allowance, not a way to evade the local analytic obstruction. The cutoff family must be proved uniformly before optimizing its cutoff; fitting A_j from J/E would be circular.

### Concentrate the hard estimate near small energy

Choose a fixed delta>0 in advance and restrict the genuinely new work to

\[
S_j\cap\{E\le\delta\Gamma^2\}.
\tag{D}
\]

For a hypothetical finite positive-time collision with Gamma>0 whose nearby predecessor points stay in the declared domain, E=0 and continuity place those points in (D). Consequently a suitable bound on this restricted domain confronts every collision whose predecessor neighborhood it covers; no positive physical energy floor is assumed.

On the complementary domain E>delta Gamma^2, independent absolute source estimates can already be converted into relative bounds. For example, the raw cutoff envelope in Note 32 yields

\[
L_j^{(N)}\ge-
\frac{e^{-2ax}\mathsf M_j\mathsf M_{j+2}}
     {\delta\Gamma^2}\,E.
\]

This coefficient is independent of N and locally bounded at finite points because Gamma is nonzero. For J, the analogous product of the complete h_j envelope and retained h_{j+2} envelope gives the same type of conclusion. Growth at infinity is allowed by the local collision criterion.

This localization removes regions that can be handled by an independent energy floor. It does not prove the missing relation in (D), where cancellation is strongest.

## Weaken the middle block hypothesis to the actual weighted remainder

The fixed power saving in Note 32's (MB) is sufficient, but more than positivity needs. Keep the closed strip 5/2<=theta<=8/3, the two analytic branches, and a complex disc of radius proportional to 1/L. Use Note 32's split Y=exp(19 ell/100). A useful alternative target is

\[
\sum_{Y<n\le N_{\rm RS}}
 e^{t\log^2n/4}n^{-w_\pm(z)}=o(1),
\tag{W}
\]

uniformly on that disc and throughout the strip, including the small boundary displacement already accounted for in Note 32. Here ell=log(Re(z)/(4pi)), and all notation and the Riemann--Siegel cutoff are as in that note.

Conditional on (W), the existing low-index discrepancy is O(1/L), the ordinary zeta tail tends to zero, and the imported heat-flow approximation errors are negligible. Hence

\[
H(t,z)-Q_+(z)-Q_-(z)=o(\Gamma)
\]

uniformly on the disc. Cauchy estimates give derivative errors o(Gamma L^k), k<=3. The carrier zeta factors remain uniformly above zero in the half-plane used for this fixed strip. Thus the normalized four-jet error is o(1), sufficient for the strict quadratic signs at large height. This conclusion does not claim Note 32's stronger O(1/L) error rate from (W) alone.

The opportunity is to retain the actual weights, cancellation among neighboring blocks, and both analytic branches for a directly combined alternative. A logarithmic saving for the complete weighted remainder can suffice. Merely smoothing blocks or replacing every-subinterval bounds by complete-block bounds is not automatically an exponent improvement: completion can recover interval bounds at subpower cost. Any smoothing must be an exact decomposition with its complement and endpoint payments retained.

Candidate tools are a smooth exact partition, Poisson or van der Corput transformation adapted specifically to the logarithmic phase, and a common treatment of adjacent scales before applying absolute values. The first deliverable should identify a cancellation that survives the actual heat weight and complex-disc perturbation. A bounded audit of the existing exponent machinery should precede a new estimate; an unrestricted search for more A/B words is lower priority.

### What the current exponent literature says about the gap

[Trudgian and Yang](https://arxiv.org/html/2306.05599v3) provide systematic exponent-pair optimization. The later [systematic ANTEDB paper, Table 1](https://arxiv.org/html/2501.16779v1) still uses

\[
b(\beta)=\frac{18}{199}+\frac{521}{796}\beta
\]

on a range containing beta=2/5. The [current database](https://teorth.github.io/expdb/blueprint/exponent-pairs-chapter.html) likewise retains this relevant bound. Its notation calls the scale alpha and the resulting exponent beta; b here avoids confusing it with our block scale.

At our beta=2/5 this gives b=701/1990, whereas the theta=5/2 target before its extra saving is 7/20. Their exact difference is 9/3980, about 0.00226131. This does not rule out a logarithmic-phase-specific improvement or a stronger future theorem; it does mean that choosing a different pair already displayed in these catalogues is not an obvious solution at the central troublesome scale. A small numerical exponent gap can still require a substantial new arithmetic argument.

The primary [database definition and non-asymptotic formulation](https://teorth.github.io/expdb/blueprint/beta-chapter.html) are also useful for auditing subinterval, phase-class, and uniformity assumptions. Database entries guide a proof; the required source theorems and losses must still be checked.

## Find the theta relation that controls the sign

The strongest speculative mechanism is to exploit exact theta or Poisson relations before taking absolute values, so that actual arithmetic block amplitudes are constrained. The paired kernel is indefinite for arbitrary amplitudes. Heat evolution, rapid decay, positive source weights, and stationarity alone admit collision controls and cannot supply the required sign.

One concrete line is to pair complete transformed contributions, then derive a signed shell identity with every staircase entry and outer boundary term included. Ask whether adverse interactions telescope, become a full stationary factor, or are bounded by a favorable term at the physical E scale. The first valuable output is a new usable relation among actual theta amplitudes. A representation without a sign consequence is not enough. In particular, entry phases which cancel in x cannot be assigned fictitious oscillatory decay.

A second, closely related diagnostic uses the cumulative moments of Note 30. On S_j, put a_j(u)=e^{tu^2}Phi(u)u^j cos(xu+j pi/2), W=h_j, and F_j(r)=integral_0^r a_j(u)du. Then

\[
L_j=\int_0^R2r\{W^2-WF_j(r)\}\,dr
 +W\int_R^\infty(u^2-R^2)a_j(u)\,du.
\]

Study the integrated signed overshoot, grouping adjacent lobes before bounding it. The pointwise condition WF_j(r)<=W^2+A_jE is stronger than needed and fails for generic positive sources. Allowing adverse pieces to cancel inside the displayed integral is a better starting point. An ordinary absolute estimate proportional to |W| remains insufficient near W=0; the aim is the physical energy scale.

## Use computation to discriminate mechanisms

A small stationary-root pilot should compare a few predeclared theta values on both sides of theta=2, at heights where complete validated evaluation is affordable. Its purpose is to locate which interactions support or defeat a candidate bound.

1. Isolate roots of both full observations h_1 and h_2 along t=theta/L(x). These are physical partial-derivative stationary conditions. Along this sampling curve, the root-isolation derivative is h_{j+2}+theta h_{j+3}/(xL^2).
2. Assemble all retained moment pairs with independent source coordinates and both Hermitian and bilinear sectors. Compare J, the raw truncated form, the full form, and predeclared groups of interacting blocks.
3. Choose cutoffs and precision from complete source-tail and cancellation budgets. A fixed tiny cutoff ladder is not justified at growing height: the contour-tail exponential and the physical carrier exponential differ, so N and precision may have to increase substantially with height. If the available enclosure does not resolve a sign, record it as undecided.
4. Use exploratory data to formulate a coefficient rule, then freeze it and validate on fresh cells, including cases of small normalized E. Displaying ratios may aid discovery but cannot define the theorem's coefficient.

A certified violation rejects that candidate inequality. Favorable finite cells identify a mechanism to prove; they do not extend it to unbounded height. A fresh pilot should be commissioned only after the exact observable, coefficient rule family, and error budget have been declared.

## Preserve the global endpoint

The present carrier has nominal real part 1/2+theta/4. Its elementary uniformly nonvanishing zeta input works with a fixed margin when theta>2. At and below two, this specific justification no longer applies; known zero-free regions may refine a boundary but do not automatically supply nonvanishing throughout the right half of the critical strip. Continuing by dividing by an unproved nonzero zeta factor would import the missing information. This is a limitation of the present argument, not a theorem that no carrier method can work.

Even a sequence of theorems with thresholds theta_n tending to zero must address their starting heights X_n: for a fixed hypothetical collision, making theta_n small can move X_n beyond its height. A finite-cover or other global argument must close that quantifier gap.

The finite bridge deserves targeted effective work once an analytic starting height is evaluated and computationally reachable. The saved high-block power in Note 32 is only 1/20000; unknown constants and slow decay make practical bridging a separate problem. Extending the finite certificate a few units at a time is useful for a declared diagnostic, not a substitute for the unbounded cusp theorem.

Recommended next deliverables are an exact weighted-remainder target with its transfer conditions, a full-amplitude signed cutoff target localized near small normalized energy, and one affordable discriminating pilot for a specified theta identity. Delay tuning, additional hypercomplex lifts, arbitrary-amplitude positivity, and an unbounded exponent-pair search should wait for a concrete mechanism that changes these estimates.

This note preserves conversation history 12 in the formal replay lane, thread 01a13da8-2366-7031-8699-3e8b6f0cefa2. It is a strategy note, not a manuscript milestone, and creates no manuscript snapshot, commit, or tag.
