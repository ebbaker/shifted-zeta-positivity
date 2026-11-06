# TND-A-B01 r1: supplied proper-time response decision

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, verified in local turn metadata. Auxiliary branch chat0001, thread `01a1af3f-7952-7d83-baba-420517ea9f00`. **B — conceptual decision**, one conceptual pass and one local clarification; no supporting agents.

**Decision: select the overview's single candidate as a conditional, externally prepared Euclidean response interpretation.** This is a useful first explanation of what the fixed Hamiltonian does to an absolutely calibrated theta amplitude after preparation. It is not an intrinsic explanation of that preparation or an established laboratory realization. The apparatus premise is accepted as a stated model input for this limited purpose, not proved to be physically available. No additional preparation premise is left implicit.

| Next task | Type/model and reason | Readiness/dependency | Expected output |
| --- | --- | --- | --- |
| **TND-A-E01 r1** | **E — Sol**; the field, operation, observation and direct-integral proof route are fixed | [Request issued][request], exact [inputs frozen][execution-inputs]; ready for author selection, **unactivated** | Complete-spectrum conditional response theorem, or a precise failure of this contract |

The [sole register][progress] owns live status. E02 and later successors remain pending. This decision completes B01 at construction/contract scope only. In particular the predicted nonvanishing multiplier is still an **E01 target**, not an accepted result. The [intake][intake] preserves the opening versions; the [return][return] binds this decision and request.

## 1. Purpose and one supplied apparatus

The free cylinder's Green diagonal is independent of position. Moving its probe cannot create the scan \(\beta(u)=\pi e^{4u}\). Parent [E01 §§4–7][e01] and [MC11's fixed contract §§3–4][mc-contract] already separate spectral response, source processing and physical preparation. The present choice pays that distinction by declaring **one external source-and-reference bank**. Its duties are:

1. Supply the complete angular Green-response scan, the canonical differential source processing and full reflection, then imprint the resulting scalar amplitude at physical coordinate \(v=u\).
2. Supply a matched, phase-calibrated countable bank of angular input/reference ports with the weights below. The passive port labels have no Hamiltonian or spatial dynamics.
3. Supply a linear, phase-sensitive Fourier-amplitude readout and known absolute gains. The bank reports complex amplitudes relative to its fixed reference; it does not replace them by squared magnitudes, normalize the source separately at each parameter, or discard an unknown phase.

This is one apparatus extension already present in the overview, not an interaction with a second evolving system. Ideal infinite extent and complete port control are part of the exact model. E01 will establish mathematical finite-norm/domain properties, not finite-resource hardware construction. No choice of optical, fermionic, reservoir or detector technology is made or inferred from the word spinor.

If the author later requires **intrinsic preparation**, the missing premise is a specified source-placement law that derives this complete spatial imprint and calibrated port amplitudes from the fixed Hamiltonian and independently specified physical inputs, without prescribing the desired theta profile. If the author requires **laboratory realization**, an additional concrete device law must implement those port amplitudes, their phase-sensitive readout and the proper-time transfer over the stated range, with physical units and errors. Merely naming the prescribed field or analytically continuing a unitary is not that law. Either stronger objective requires a dated B01 revision; neither is claimed impossible.

## 2. Fixed field and the one local clarification

Retain \(C=\mathbb R_v\times S^2_{1/2}\), \(K=L^2(S^2,\Sigma;d\Omega)\), \(A=D^2\), \(\mathcal D_C=-i\Gamma\partial_v+2D\), and \(L_0=-\partial_v^2+4A\). These conventions and full-line realizations are inherited from [E01 §§1–4][e01]. Unit-sphere \(D\) has \(\pm n\), \(n\ge1\), multiplicity \(2n\) per sign; \(P_n\) has rank \(4n\). The [checked Camporesi–Higuchi passages][source-use] use an anti-Hermitian slash operator; the factor \(-i\) and radius scaling remain explicit.

**Local clarification — passive ports and phase reference.** Write a distinct copy \(K_{\rm ref}\), with one fixed unitary identification \(J:K_{\rm ref}\to K\), and set
\[
W=(4\sqrt A)^{-1},\quad Q_1(\beta)=\sum_{n\ge1}e^{-\beta n^2},\quad
R=We^{-\pi A}/Q_1(\pi),\quad B=R^{1/2}J.
\]
The amplified field space is
\[
\mathscr H=L^2(\mathbb R_v;\operatorname{HS}(K_{\rm ref},K)).
\]
The generator acts on the physical index on the **left only**. In the matched basis, \(B e_{n,\sigma,a}=\sqrt{r_n}\chi_{n,\sigma,a}\), where \(r_n=e^{-\pi n^2}/[4nQ_1(\pi)]\), \(\sigma=\pm\), \(1\le a\le2n\). Each column is a linear complex spinor response amplitude. The Hilbert–Schmidt field is not a density operator; no commutator, right heat factor, Born probability or quantum purification is assigned to it. The reference bank adds apparatus multiplicity, not physical angular degeneracy. Choosing \(J=I\) in matched coordinates recovers exactly the overview, rather than a second mechanism.

The readout is the conjugate-linear-first-slot pairing
\[
\mathcal O_{\lambda,\tau}(k)
=\sqrt{\pi/2}\operatorname{Tr}_{K_{\rm ref}}
   [B^*\widehat S_{\lambda,\tau}(k)].
\]
Thus the reference phases and angular weights belong to the declared apparatus. The same fixed identification is used for preparation and readout. A reference basis change must transform both; a changed relative physical phase is a changed preparation/readout. E01 must check the pairing and domains locally; it imports no pending MC11 Note13 measurement theorem. Angular Hilbert–Schmidt pairing is bounded, whereas fixed-\(k\) radial evaluation requires the prepared regular family. Real \(k\) is the ideal spectral readout; complex \(z\) is mathematical continuation, not a detector setting.

## 3. Literal source and absolute calibration

The externally processed source is fixed on \(u\ge0\) by
\[
x=\pi e^{4u},\qquad
\Phi(u)=\tfrac18(\partial_u^2-1)[e^uQ_1(x)]
=e^u\sum_{m\ge1}[2(m^2x)^2-3m^2x]e^{-m^2x}.
\]
Use the complete theta reflection to extend \(\Phi\) smoothly and evenly to the full line, then identify the extended source coordinate with \(v\) and prepare
\[
F_\lambda(v)=e^{\lambda v^2}\Phi(v),\qquad
S_{\lambda,0}(v)=F_\lambda(v)B.
\]
This is the amplitude itself, not \(\sqrt{F_\lambda}\). The source index \(m\) and physical left-channel index \(n\) are independent after source processing; replacing \(F_\lambda\) in channel \(n\) by its \(m=n\) summand changes the candidate. Complete unit coefficients and the zero-mode correction in theta inversion remain essential. Reflection is the canonical full-source identity, not the even extension of each finite source prefix with assumed smooth endpoints. [MC11 Note08 §§2–3][mc-source], its [assessment][mc-assessment], and [E01 §§4,6][e01] supply these inherited bounds and qualifications; [DLMF 20.7.32][source-use] supplies the recorded modular convention.

The Fourier transform uses \((2\pi)^{-1/2}\int e^{-ikv}\cdot\,dv\). The canonical observation is
\[
H_\lambda(z)=\int_0^\infty F_\lambda(v)\cos(zv)\,dv,
\qquad H_0(z)=\xi((1+iz)/2)/8.
\]
These are the [checked Rodgers–Tao v5 Introduction definitions][source-use], reused through E01, not a new normalization. The factors \(1/8\), \(1/(4n)\), \(Q_1(\pi)\), and \(\sqrt{\pi/2}\) are fixed independently of observed zeros. The Green weight comes from the complete radial integral \(\int dk/[2\pi(k^2+4n^2)]\), not a zero-momentum state.

In physical amplitude units let the source be \(S^{\rm phys}=gS\), with a fixed known \(g>0\). Let the raw complex signal be \(y(k)=\eta\operatorname{Tr}(B^*\widehat S^{\rm phys}(k))\), with fixed known nonzero complex detector gain \(\eta\), including phase. The stipulated calibrated output is \(\sqrt{\pi/2}\,y/(\eta g)\). Units and both gains are supplied premises. Unknown gains or phase would permit only proportional recovery and would fail this absolute-calibration contract. No division by \(H_\lambda(0)\), field norm, survival probability or measured signal is permitted. \(\operatorname{Tr}R=1\) calibrates the angular bank; it does not normalize the radial source. Product-measure spinors convert to metric-volume spinors with the inherited factor 2, consistently at input and readout.

## 4. Proper time and the unproved response target

Define \(S_{\lambda,\tau}=e^{-\tau L_0^{\rm left}}S_{\lambda,0}\), \(\tau\ge0\). With \(H_{\rm kin}=\varepsilon L_0\), \(\varepsilon=\hbar^2/(2m\ell_0^2)\), dimensionful Euclidean time obeys \(\tau=\varepsilon t_E/\hbar\). Here proper time means the positive heat/Schwinger parameter used in the inherited resolvent integral. No relativistic world-line proper time is asserted. Laboratory unitary time \(t_{\rm lab}\), angular damping \(\beta\), and the independently prepared Newman parameter \(\lambda\) are different variables; no clock law connecting them is supplied.

The **target to prove in E01**, with complete domains and sums, is
\[
\mathcal O_{\lambda,\tau}(z)
\stackrel{?}{=}e^{-\tau z^2}\frac{Q_1(\pi+4\tau)}{Q_1(\pi)}H_\lambda(z).
\]
Its intended consequence, conditional on that proof, is recovery by a known entire nonvanishing factor for each finite real \(\tau\ge0\). Existing zeros and multiplicities would be preserved at each \(\lambda\), including collisions as \(\lambda\) varies. At real high frequency the inverse factor grows like \(e^{\tau k^2}\); no uniform recovery stability or computational advantage is selected. The observed family must not be assigned the unchanged Newman equation: the spectral derivatives also differentiate this Gaussian. E01 is asked to check that distinction, not to introduce another flow.

All \(k\in\mathbb R\), all \(n\ge1\), both angular signs and both first-order dispersion signs remain. There is no wall, confinement, scalar-shell substitution or normalizable radial plane wave. The [frozen request][request] specifies maximal left-weighted domains, a finite-reference/finite-angular smooth radial core, arbitrary finite compact parameter ranges and order-dependent estimates. Heat-evolved fields need their own exponential-moment bounds; original double-exponential spatial tails are not simply carried through convolution.

## 5. Evidence inventory, controls and stopping boundary

| Ingredient | Status here |
| --- | --- |
| Cylinder operators, Green weight, complete source bounds | Inherited MC11 internal acceptance, with shared premises; parent E01 additions remain proof-author pending shared TND-E03 |
| Canonical scan, reflection usage, spatial imprint, gains, passive bank and linear detector law | Explicitly supplied apparatus/model input; no hardware or intrinsic-preparation theorem |
| Choice of Euclidean-response purpose and precise contract | B01 conceptual decision completed here |
| Amplified realization, domain membership, complete observation identity and derivatives | Unexecuted E01 obligations; no theorem acceptance by design algebra |
| Laboratory implementation or intrinsic source generation | Outside selected first purpose; precise stronger premises in §1 |
| Collision exclusion, signed estimate, practical recovery gain | None selected or obtained |

Classification is **conditional physical response representation**, not an RH criterion or collision gain; see [result index][results], [theta cluster][theta], [patterns index][avoid] and [avoid/01][a01], [03][a03], [07][a07]. This is the analytical planning control screen required by [control register][controls] and [avoid/02][a02], with no new computations:

| Control | What survives; failed premise and scope |
| --- | --- |
| Euler-factor sources | Applicable smooth positive even source/Fourier/heat machinery survives; exact canonical arithmetic source fails. Their positive-threshold witnesses are not rejected by this representation. |
| Weighted-square and finite-prime controls | Applicable positive half-line and square-response formulas survive; unchanged complete unit weights/full canonical reflection fail. Finite endpoint matching does not imply global smooth reflection or every operator domain. |
| Reflected super-Gaussian and smooth positive-primitive controls | Applicable smoothness, positivity, reflection and exponential-moment Fourier/heat operations survive; exact theta arithmetic fails. The proposed multiplier would also preserve their collisions wherever these hypotheses apply. |
| Atomic and finite-profile controls | Fourier/moment observations may survive; smooth-field and full operator-domain hypotheses need not. No unproved smooth realization or universal exclusion is inferred. |

Naming canonical input identifies the source but is no quantitative separation. Investigation05's [ordinary heat and constant-linear benchmark][book] retains [same-assistant evidence][book-review] and the latter's interval \(0\le\tau<\pi/(4\sqrt{\alpha\beta})\), \(\alpha,\beta>0\). [Investigation06's conclusions][aux-lessons] retain their tested response/recovery classes. They are background, not additional candidates. MC11-OBS-E01 and MC11-E05 statuses are unchanged. Branch E02 awaits both branch E01 and the shared TND-E03 disposition; this choice does not perform or duplicate either review.

**Boundary:** one conceptual pass selected the conditional purpose; one local clarification typed and calibrated its passive reference pairing. No different mechanism, new proof, numerics, manuscript, external status change or successor activation followed. A changed source, object, observation, clock, interaction or requirement of intrinsic/laboratory realization needs a dated B01 revision. E01's direct-integral proof and local apparatus/domain checks now belong to Sol.

**Next: [E] TND-A-E01 r1 — Sol.** Use the [frozen request][request] and its [input record][execution-inputs]. Prove the declared conditional complete-spectrum realization or report its exact failed premise; keep preparation supplied and the multiplier unaccepted until proved. Author selection remains required to start that task.


[decision]: 01_TND_A_B01_R1_SUPPLIED_PROPER_TIME_RESPONSE_DECISION_20261106.md
[request]: ../../research-progress/handoffs/02_TND_A_E01_R1_FROZEN_REQUEST_20261106.md
[source-use]: ../../references/01_TND_A_B01_SOURCE_USE_20261106.md
[progress]: ../../research-progress/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_PROGRESS_20261105.md
[plan]: ../../research-plan/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_PLAN_20261105.md
[overview]: ../../research-overview/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_OVERVIEW_20261105.md
[e01]: ../../../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md
[intake]: ../../research-progress/handoffs/01_TND_A_B01_R1_INPUT_VERSIONS_20261106.json
[return]: ../../research-progress/handoffs/01_TND_A_B01_R1_RETURN_RECORD_20261106.json
[execution-inputs]: ../../research-progress/handoffs/02_TND_A_E01_R1_INPUT_VERSIONS_20261106.json
[mc-source]: ../../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/08_MC11_AR_E03_R1_SOURCE_MEMBERSHIP_AND_ENDPOINT_PAIRINGS_20261105.md
[mc-assessment]: ../../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/reviews/05_MC11_AR_E04_R1_MODEL_SOURCE_AND_SCOPED_TRANSFER_ASSESSMENT_20261105.md
[mc-contract]: ../../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/06_MC11_BR01_R1_FROZEN_CYLINDER_MODEL_AND_ANALYTIC_CONTRACT_20261105.md
[mc-refs]: ../../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/README.md
[bib]: ../../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/references.bib
[parent-refs]: ../../../references/README.md
[results]: ../../../../../../result-summaries/README.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[workflow]: ../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[reference-workflow]: ../../../../../../REFERENCE_WORKFLOW.md
[capture]: ../../../../../../tools/CHAT_HISTORY.md
[large]: ../../../../../../LARGE_FILES.md
[book]: ../../../../05_radial_theta_collision_geometry/book/main.tex
[book-review]: ../../../../05_radial_theta_collision_geometry/reviews/21_BOOK_REWRITE_ASSESSMENT_20261028.md
[aux-lessons]: ../../../../06_auxiliary_collision_flows/notes/06_APPROACH_SUMMARY_AND_GOALS_FOR_NEXT_BRAINSTORM_20261029.md
