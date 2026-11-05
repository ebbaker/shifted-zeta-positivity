# MC11 progress and open questions

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6-astra (Codex), reasoning effort xhigh**, as recorded for this conversation. Chat title: **Summarize theta overlap progress**; thread `01a1a9d4-3d44-7472-ae0f-54705423d86b`, MC11 history0002.

The completed E03 calculation resolves the main finite-order question posed by MC11: restoring the excited spectrum increases the three-orbital unnormalized overlap, and the first excited level accounts for almost all of that increase. These are validated acquisition and proof-author conclusions awaiting E04 disposition. Edward Baker reported in this conversation that **E04 has now been started in parallel**. The handoff and register read for this summary still recorded it as unstarted; the assessment owns its subsequent status and conclusions.

## The comparison

The canonical energies are \(E_n=\pi n^2\). The ground level retains weight one while every excited level has the same weight \(s\), increasing from zero to one. The observable is the real, unnormalized determinant overlap
\[
D_q(s)=\det[c_{q+j-i}(s)]_{0\le i,j<q}.
\]
Thus \(D_q(0)\) uses the ground mode on the full half-line and \(D_q(1)\) uses the complete unit-weight theta source. Here \(q\) counts source orbitals. It is distinct from the energy-level index \(n\).

For order three the change is separated as
\[
\Delta_3=D_3(1)-D_3(0)=L_2+L_{\ge3}.
\]
Both contributions are integrated along the same path, with the cofactors evaluated using all the levels present at that filter setting. This retains their mixed effects. [Research overview](../../research-overview/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md)

## What the completed stages established

| Stage | Progress | Evidence status |
| --- | --- | --- |
| E01 | Accepted the starting deductions: every excited level lowers the two-orbital overlap throughout the path, with total fractional loss below \(10^{-4}\); the three-orbital high-energy limiting response is positive. | Internal different-model assessment of the originating derivation, with inherited integration premises. |
| E02 | Derived the exact common-path split and proved a positive response for every \(n\ge3\) level throughout the path. Established a positive full-half-line ground reference. The first-excited and total signs were unresolved because the five first-excited moment bounds were too broad. | Completed bounded calculation; its inconclusive intervals remain evidence of the limits of those inputs. |
| E03 | Acquired precisely those five moments, included the spatial exterior, and replayed the same calculation. Every width target was met in one 384-bit acquisition without refinement. Both spectral groups and their sum are positive. | Validated acquisition/replay and author checks; E04 disposition pending. |

Sources: [E01 assessment](../../reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md), [E02 return](../../notes/02_MC11_E02_R1_COMMON_PATH_SPECTRAL_SPLIT_20261104.md), [E03 return](../../notes/03_MC11_E03_R1_FIRST_EXCITED_ACQUISITION_AND_RETURN_20261104.md), and the [sole live register](../../research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md).

## The quantitative result

E03 reports the conservative enclosures
\[
2.22665020\times10^{-33}<\Delta_3<2.22665075\times10^{-33},
\]
\[
1.34020588635\times10^{-5}<\frac{\Delta_3}{D_3(0)}<1.34020621148\times10^{-5}.
\]
The relative increase is about **0.001340206 percent**, or **13.4021 parts per million**, against a positive ground reference near \(1.66142398817\times10^{-28}\).

The first excited level contributes more than **99.99997573 percent** of the net gain. The complete higher group satisfies \(0<L_{\ge3}<5.402\times10^{-40}\), so the groups reinforce. The higher-group allowance now controls the width of the net enclosure; further precision in the five acquired moments is unnecessary to settle the reported signs.

A separate bound over the entire interval \(0\le s\le1\) establishes the first excited level's positive instantaneous response. Combined with E02, this covers every excited level at every filter setting. The pointwise claim has its own argument; it does not follow merely from a positive integrated change. [E03 handoff](../../research-progress/handoffs/03_MC11_E03_RETURN_AND_E04_MODEL_CONTINUATION_20261104.md)

## Significance and remaining questions

The gain is a signed, energy-resolved comparison at fixed order. Two orbitals lose a small amount of overlap as the spectrum is restored; three orbitals gain a small amount, overwhelmingly from the lowest excited level. The high-energy explanation involves the cofactor receiving the dominant lowest-moment contribution: it is \(-c_3(s)\) at order two and \(c_4(s)^2-c_3(s)c_5(s)>0\) at order three. E02 and E03 extend the order-three conclusion from that limiting argument to the actual discrete excited spectrum.

These results do not establish an alternating pattern in order, a growing-order estimate, a neighboring-shift comparison, a new canonical positivity range, or an RH conclusion. The parent Mellin-curvature problem still requires control across neighboring coefficient shifts as well as determinant order. Canonical source and cofactor estimates also cannot be transferred automatically to reweighted spectra or other collision controls. See the [result index](../../../../../../../../result-summaries/README.md), its [theta cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and [collision controls](../../../../../../../../result-summaries/12_collision_controls_and_screening.md).

E04's immediate job is to assess normalization, common-path cofactor algebra, validated integration, complete spatial and energy tails, and each sign and magnitude using the frozen evidence. The subsequent B01 question is whether the assessed cofactor mechanism supports a useful estimate beyond order three, including the dependence on order and the neighboring shifts needed by Mellin curvature. This conversation summarizes that question without activating B01 or specifying E05.

E01's different-model assessment and E02/E03's same-model author checks remain distinct from specialist review. Replay agreement also leaves identified numerical and analytical premises in place. The [patterns index](../../../../../../../../avoid/README.md), particularly [shared-premise review](../../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md) and [joint estimates](../../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), supplies the applicable caution. This note is a progress summary, not an E04 assessment.
