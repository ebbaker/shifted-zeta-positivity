# Heat-density research and its relevance to the RH applications investigation

26 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded reasoning effort max**, verified from the current turn metadata. Chat **Review heat-density research**, thread `01a17a52-1100-7750-b776-5bdecb7f6014`, registered as heat-density chat 0026.

**Assessment: the new bounds materially improve the inputs available for quantitative zero calculations. The most consequential advance for Investigation 5/02 is the retained-arithmetic field estimate through zero time. No reviewed result yet establishes the lower margin or endpoint energy inequality needed to exclude a positive threshold, improve a complete Newman bound, or prove RH-conditional simplicity.** The next application should measure a complete margin, energy error, onset, or cost on a specified domain.

This is a focused research/application review. It reads the Book's main file and all nine sections, the current and historical overviews, Summary67, and selected parent-manuscript statements and derivations concerning exact equations, global assembly, source compression, evaluation and limitations. The complete written argument of Ansatz Note26 was inspected, especially its growing-shift remainder, population bound, time derivative, residual and overlaps. For Notes23–25 and recurrence Note20, the theorem contracts and selected mechanisms were checked alongside the available assessments. The applications brainstorm, positive-threshold note, maintained summary, Rodgers–Tao initial note, overview and progress register were read. This is not a line-by-line audit of every companion proof, HDA-20 completion, specialist validation, a numerical certificate, or a new manuscript build. File identities and inspection levels are in the [input record](44_HEAT_DENSITY_RH_REVIEW_INPUTS_20261026.json).

The repository [result index](../../../../result-summaries/README.md), [heat-flow cluster](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md), [local geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) and [avoid index](../../../../avoid/README.md) govern the interpretation. In particular, retain [target classification](../../../../avoid/01_restating_the_target.md), [control screening](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scoped conclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [quantitative gain](../../../../avoid/20_volume_without_a_gain.md). The conclusions below concern the reviewed estimates and their specified consumers; they are not an obstruction to other theta-specific methods.

**The research at a high level.** The program constructs controlled descriptions of one canonical entire field,
\[
 H_t=-H_{zz},\qquad H(0,z)=\xi((1+iz)/2)/8.
\]
Three mechanisms cover its different regimes: Gaussian smoothing and completed arithmetic expansions at negative time; finite source approximation for the central region; and moving gamma-saddle expansions at positive time. The Book organizes these mechanisms and their overlaps. The parent manuscript supplies the more elaborate transfer to regulated, spatially averaged potential, density, current and actual covariance, including all defects created by joins. The ansatz and recurrence companions supply sharper regional field estimates.

There are two different achievements. The parent gives a finite construction with any prescribed absolute accuracy for its full physical tuple at every real time and height on the declared transverse strip. The regional formulas give much sharper, more interpretable errors, with spatial derivatives, direct time estimates and actual heat residuals. Source compression and fixed-data evaluation make the construction more explicit. The constants and sufficient onsets can still be enormous; polynomial cost in additional accuracy at a fixed descriptor and query box is not a practical joint cost bound in height, small time and resolution.

**What Summary67 adds.** Write \(L=\log(X/(4\pi))\) and \(\mathcal L=1+\log X\), reserving \(\Lambda\) for the Newman constant. The six completed returns in [Summary67](../notes/67_CHAT0025_RESEARCH_SUMMARY_AND_HANDOFF_20261026.md) have distinct uses:

| Return | Actual improvement | Application significance |
| --- | --- | --- |
| Named centers, Ansatz Note22 | Explicit center shifts smaller than the \(1/(X\log X)\) rounding width; exact switch sensitivity | Corrects the finite-height description of the prescribed regulator transition; the simplified layer's old error rate is retained. |
| Moving negative endpoint, recurrence Note20 | Outer field/spatial 0–3/direct-time allowance \(e^{-L^2/4}\) on \(1/L\le -t\le2\) | Strong data for negative-time analysis. It excludes zero and the closer scale \(-t\asymp L^{-2}\). |
| Fixed \(P_4\) physical transfer, Ansatz Note23 | On \([63,65]\): static errors \(X^{-7}\), current/covariance \(X^{-7}\mathcal L^2\), time/source \(X^{-6}\mathcal L^2\), at specified derivative orders | A substantive nonlinear transfer gain and a useful model for future transfer proofs. Its time domain is remote from the unresolved small-positive-time problem. |
| Small positive slab, Ansatz Note24 | Two-arm field on \([1/2,1]\), with full arithmetic allowance \(X^{-t\log2/4}\) | Fills a regional approximation interval and supplies an overlap. |
| Intermediate band, Ansatz Note25 | Corrected two-arm field on \([3/4,33]\), with complete allowance \(\mathcal L^4/X^2+X^{-t\log2/4}\) | Connects the small-positive and existing positive-saddle regimes. |
| Retained arithmetic, Ansatz Note26 | \(O(\sqrt X)\) retained modes plus explicit RS completion; allowance \(\epsilon_X=\mathcal L^2X^{-3/4}\) on \(4/L\le t\le1\) | The most directly relevant new input: the identical model in the crossover extends this coverage to \(0\le t\le1\). |

All six retain their source status, **proved in-note from named inputs, with same-model internal assessment only**. This review supplies a focused separate-chat LLM assessment, not a blanket upgrade of that evidence.

Note26's proof addresses a real domain issue. Positive Gaussian evolution samples initial imaginary shifts of order \(tL\). Its argument supplies a new growing-shift remainder using the complete ordinary Dirichlet tail and gamma ratios; it does not merely substitute that width into a fixed-strip theorem. The complete finite population costs \(X^{1/4}\), while the mode curvature/calibration contributes \(\mathcal L^2/X\), yielding the stated \(\epsilon_X\). The direct-time argument integrates Gaussian moments before applying the lower time bound. The same frozen \(F_N\), including completion, appears on the overlap \(4\le tL\le8\). I found no new obstruction in these inspected mechanisms or in the union argument; the inherited initial RS theorem and full source chain were not independently re-proved.

Together the returns provide an atlas of high-height field estimates on every fixed finite positive-time interval, including zero. They do not provide one newly joined holomorphic field across all charts, sharper physical transfer throughout that interval, or the stronger negative error through zero.

**The manuscript status needs reconciliation.** The Book's crossover section still describes the small-positive bridge as unexecuted and the interval up to the positive saddle as a principal gap. Its physical/frontier sections and the parent manuscript's remaining-work section still call the fixed-P4 physical consumer open. Those statements describe the older production baseline. The unified overview contains the later completed rows, but also retains an earlier table qualification saying corrected physical transfer is open. Summary67 and the source notes resolve the chronology: the regional field coverage and the specified P4 consumer have closed; bounded-height refinements, stronger through-zero precision, new small-positive physical consumers, global reassembly and useful cost remain separate. The existing [B02 integration request](../research-progress/handoffs/HDA-B02-MI1.md) is the proper production follow-through. This review does not execute it or modify the manuscripts.

**Where the bounds are now close enough to be useful.** The [applications summary](../../02_heat_flow_rh_applications/summary/CURRENT_SUMMARY.md) and [Rodgers–Tao overview](../../02_heat_flow_rh_applications/rodgers_tao/research-overview/01_RODGERS_TAO_RESEARCH_OVERVIEW_20261026.md) already incorporate Note26; their current assessment should take precedence over the opening brainstorm's older field-domain gap.

| Application requirement | Present position |
| --- | --- |
| B1: small-positive field and derivatives | High-height domain gap reported closed, including zero, with the full retained arithmetic. Numerical constants/onsets, lower margins and the finite core remain. |
| B2: microscopic field data | The signed crossover already includes \(|t|=O(L^{-2})\). Its derivative losses are compatible with that scaling on a fixed microscopic block. An energy theorem still needs margins and population/boundary accounting. |
| B3: nonvanishing or simple-root margin | Still the central missing local input. Upper errors do not establish a lower bound for the approximant. |
| B4–B5: exterior interaction and localized energy | Exact quantities and missing payments are identified. No new complete Rodgers–Tao energy estimate is established by the reviewed application notes. |
| B6: shrinking resolution | Fixed filters and the late-time weak-transfer result do not supply uniform transfer as the filter widths shrink to individual gaps. |
| B7: endpoint simplicity/noncollision | No theta-specific estimate beating the allowed collision behavior has been obtained. |
| B8: useful joint cost | Source compression and fixed-box evaluation help, but do not yet instantiate an affordable complete application. |

The strongest late-time hierarchy is not automatically the best input here. Its two-arm arithmetic allowance is \(X^{-t\log2/4}\). Formally, at \(t=c/L\), this allowance tends to \(2^{-c/4}\), rather than zero; at \(t=c/L^2\), it tends to one. This is a diagnosis of that allowance, not a lower bound on the true error or an extension of the two-arm theorem outside its domain. It explains why retaining the arithmetic modes is more relevant near zero than adding gamma corrections alone.

For a fixed microscopic chart, freeze \(X,L\), set \(z=X+u/L\), \(t=v/L^2\), and write \(\mathcal E=H-F_N\). Note26's positive-side contract implies
\[
 \frac{|L^{-j}\partial_z^j\mathcal E|}{E_o}
       \le C_j\epsilon_X\quad(j\le3),\qquad
 \frac{|L^{-2}\partial_t\mathcal E|}{E_o}
       \le C_t\epsilon_X.
\]
These are scaled derivatives of the error, normalized afterward; no derivative of the envelope is being asserted. The existing signed crossover is stronger on \(|v|\le A\), with allowance \(O_A(X^{-3/4})\). Thus ordinary microscopic rescaling does not destroy the approximation. The mean heat-coordinate spacing is \(4\pi/L\), so using that length changes only fixed constants here. No growing-block or shrinking-filter theorem follows from this observation.

For example, the existing first-jet transfer test can now ask for the explicit model margin
\[
 m_X=\inf_{(t,z)\in\mathcal D}
 \frac{\bigl(|F_N|^2+L^{-2}|(F_N)_z|^2\bigr)^{1/2}}{E_o}
 >\sqrt{C_0^2+C_1^2(\mathcal L/L)^2}\,\epsilon_X
   +\text{evaluation/coverage allowance}.
\]
On a declared high-height domain \(\mathcal D\), this would exclude a common zero there. The vanishing right-hand side is now available analytically; the left-hand lower bound is not supplied. For a global positive-time claim one must also cover the finite core and the exterior. This is the applications program's existing interface, not a new RH criterion.

On an already isolated block with proved simple-root slopes of size at least \(\kappa E_oL\) and compatible curvature/contour bounds, field error can give root-position error \(O(\epsilon_X/(\kappa L))\). If gaps are at least \(\gamma/L\), with the position errors much smaller than those gaps, differentiating \(g^{-2}\) gives a per-pair allowance of order
\[
 O\!\left(\frac{\epsilon_X L^2}{\kappa\gamma^3}\right).
\]
A crude sum over \(M\) roots costs at most another \(M^2\), before weights and boundary terms. This is a conditional sensitivity calculation, not an established canonical slope/separation bound. It shows exactly why one should compare the present error against the actual margin before requesting further approximation orders.

**Why the positive-threshold problem remains different.** The primary [Rodgers–Tao v5](https://arxiv.org/html/1801.05914v5) uses \(\Lambda<0\), real-zero evolution up to the original zeta slice, and a spacing contradiction there. Its corrected propagation step moves energy estimates forward on a slightly smaller index interval. Changing the premise to \(\Lambda>0\) loses that endpoint comparison; translating time also translates the zeta slice. This supports the application's sign analysis, not an impossibility theorem for a different positive-threshold argument.

The relevant published comparison is already strong: [Polymath v2, Theorem 1.5](https://arxiv.org/html/1904.12438v2#S1) gives regular real high zeros at positive time beyond an exponential-in-\(1/t\) height. Its Theorem 1.2 requires initial verification, an exterior exclusion and a time barrier together. Therefore improved positive-time asymptotics alone cannot be called a new Newman upper bound. The current project must improve a complete consumer or reach a quantitatively new regime.

A direct algebraic diagnostic makes the remaining endpoint issue precise. The exact heat solution
\[
 F(t,z)=(z-a)^2-2(t-T)
\]
has a double zero at \(T\), simple real roots for \(s=t-T>0\), and
\[
 g^2=8s,\qquad E_{\rm pair}=g^{-2}=1/(8s).
\]
The heat equation holds because \(F_t=-2=-F_{zz}\). Its field at the critical point has magnitude \(2s\); root slopes are of size \(\sqrt s\). A field perturbation of size \(e\) can therefore cause root displacement of size \(e/\sqrt s\), and resolving the gap relatively requires \(e=o(s)\). These are exact-model sensitivity statements, not a universal sufficient criterion for a perturbed heat flow.

Moreover, even a bounded smooth exterior drift does not itself contradict such an event. For an isolated two-root cluster with \(H=U(z-a_-)(z-a_+)\), put \(D=2U_z/U\) and \(g=a_+-a_-\). The exact local equations give
\[
 (g^2)'=8+2g\{D(a_+)-D(a_-)\}.
\]
If \(|D_z|\le K\) near the cluster, the last term is \(O(Kg^2)\); starting from a double event still permits \(g^2=8s+O(Ks^2)\). Thus a better exterior estimate can help a complete energy calculation, while an endpoint exclusion additionally needs a theta-specific restriction on whether that cluster can occur.

At a fixed candidate event height, the present height-only approximation allowance does not vanish as \(s\downarrow0\). Improving it, or evaluating to arbitrarily many digits, is not by itself a proof of the required lower margin. The application notes correctly classify \(sE_W(T+s)\to0\) as a final-strength target. It would rule out the displayed collision behavior; it has not been derived. Higher multiplicities require the corresponding Hermite cluster constants, rather than copying the double-root coefficient.

The physical approximation has a further limitation for this purpose. With the prescribed regulator at fixed \(t\le64\), the canonical field becomes very small at large height while the regulator is independent of height. Absolute regulated-density accuracy can therefore coexist with little information about individual high zeros. Fixed smoothing also merges the signal of a nearby pair toward that of a double. Spatially joined approximants are nonholomorphic in their transition bands. These facts scope the all-time physical theorem; they do not diminish its stated approximation achievement.

**Control check.** The polynomial diagnostic above passes the heat identity and fails the proposed sub-\(1/s\) endpoint target. For a valid first-jet error bound, its strict exclusion margin necessarily fails at any actual common zero, including a control event. The source-level screen remains that of [cluster12](../../../../result-summaries/12_collision_controls_and_screening.md): Euler-factor sources alter the canonical coefficients; weighted-square/finite-tail sources lack the complete reflection/completion premise; reflected and smooth/primitive controls lack full theta arithmetic; finite-prime/profile controls retain only their selected constraints; normalized RH-conditional endpoint controls fail ordinary Dirichlet arithmetic; older positive-kernel and polynomial controls lack the canonical theta source. These identify absent source premises, not automatic failure of every derived estimate. A proposed arithmetic lower bound must be checked at their events. No stored numerical control certificate was rerun.

**Recommended next deliverables.** First complete the existing RT-01/RT-02 selection of a particular corrected propagation term and observable, then derive its RT-03/RT-04 requirements using the available \(\epsilon_X\), rather than reopening the closed high-height time-domain task. On a fixed positive slab and buffered block, obtain a certified contour/first-jet margin, root enclosures when needed, and the complete exterior-drift variation. Compare the resulting energy allowance with a direct first-jet or established barrier certificate using the same inputs. Report a better complete margin, onset, range or acquisition cost, or the precise unpaid term. A successful pilot in a region already known to be real is a methods result; a smaller Newman upper bound requires all additional coverage obligations.

For the parent bound program, prioritize explicit constants and onsets for Note26, arithmetic margin information, and a consumer-specific complete cost comparison. Stronger negative-time accuracy at \(-t\asymp L^{-2}\) is a reasonable separate target, but the existing crossover already supplies vanishing microscopic field error; its necessity should be judged against the chosen consumer. More late-time correction orders and higher precision around the regulator switch are lower priorities for this particular RH application unless a new transfer shows how they pay an endpoint term.

The research has advanced from incomplete regional coverage to a usable collection of complete field inputs, including the relevant small-positive-time range. The next decisive evidence would be a proved lower margin or complete localized energy improvement. Neither is currently supplied by the reviewed application work.

Primary-source inspection on this review: Rodgers–Tao v5 introduction, §7 definitions (62)–(63), and the corrected §8 propagation statement in primary HTML; Polymath v2 Theorems 1.2/1.5 and Proposition 3.1 in primary HTML. HTML/PDF numbering differs for Rodgers–Tao. Existing canonical PDF receipts are retained in the [applications reference catalog](../../02_heat_flow_rh_applications/references/README.md); no fresh PDF verification or current-record survey is claimed. No manuscripts, task acceptance states, source data or numerical certificates are changed by this assessment.
