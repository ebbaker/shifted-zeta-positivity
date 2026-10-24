# Review of the provisional conserved contour manuscript section

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. The derivations and research direction received separate same-model agent checks and an integration review by the main assistant. This is internal LLM review, not specialist or formal verification.

**Assessment:** the author-requested conservation material is incorporated provisionally in [main.tex](../../manuscript/main.tex), through [conserved_contours.tex](../../manuscript/conserved_contours.tex). Its exact identities, stationary actions and controls are distinguished from the missing canonical estimate. The source of [book.tex](../../manuscript/book.tex) is preserved. The [new overview](../research-overview/03_CONSERVED_SPATIAL_CONTOURS_ANALYTIC_PROGRAM_20261023.md) prioritizes analytical results and proofs for eventual book inclusion; numerics always have a supporting role.

## Mathematical incorporation

The section keeps the spatial graph z=T+i epsilon(T,t) and the backward-heat sign. Its material form, open-arc endpoint law, positive density/current, primitive and two Noether formulations agree with [Note 16](../notes/16_NATURAL_CONTOUR_EVOLUTION_20261023.md) and [Review 07](07_SPATIAL_CONTOUR_EVOLUTION_REVIEW_20261023.md). The primitive is written as mathcal P to avoid conflict with the existing prepared polynomial P. The section uses unique cc-prefixed equation/proposition labels.

The canonical Fourier constant is pi Phi_even; the heat-polynomial moments have the factor i^n. Smooth even source continuation is justified by the theta transformation and 16 Phi=h''-h for h(u)=e^u vartheta(e^(4u)). Superexponential source tails justify Schwartz Fourier manipulations on compact real time intervals. The full Fourier data determine the heat field, while arbitrary Schwartz moment completeness is not claimed. Explicit time-dependent weights do not establish autonomous Hamiltonian integrability or a coercive energy bound.

The three-adjoint argument correctly rules out simultaneous preservation of all local material subarc forms by a single velocity, allowing constant-current gauges. It does not contradict conservation of the whole-line integrals. The Burgers variable is 2H_z/H, whereas the primary material velocity is H_z/H.

The explicit positive Gaussian-source control has conserved complete Fourier/moment data, all-real simple zeros on the indicated positive-time interval and endpoint doubles. Its constants and source differ from theta and its time interval has a finite upper singularity. It screens a generic hierarchy-only exclusion, not a quantitative theorem using the actual theta data. The H=z control also prevents claiming material regularity from H dz conservation alone.

The scalar current, moving-wall sign, augmented mass balance and end terms are retained. The conditional graph bound requires a containing buffer, and the displacement bound retains the adaptive small-value trace. Source normalization, reference carrier derivatives, bottom flux and regulator dependence are not discarded. Signed mean control still does not bound one-sided inward variation.

The first-jet curvature formula and full spacetime action have the checked signs and pi factors. Projective curvature, line circulation and the physical Chern–Hopf three-form remain separate. The action must retain its time component; positive compliance does not remove a joint-zero singularity of the physical jet. The section does not infer an interior collision exclusion from a regular enclosing contour.

## Branch continuation and the next analytic claim

The added primitive asymptotic-value observation follows from evenness, real-axis decay and the zero-frequency invariant: P(t,+infinity)=pi Phi_even(0)/2. Avoidance of critical values alone therefore does not prevent global inverse escape. Conversely, separation from all global critical values can unnecessarily exclude a regular branch sharing another branch's critical value. The manuscript now asks for branch-local containment and escape control.

The positive conserved metric is a pullback of Euclidean geometry under the primitive. It degenerates at zeros, and its real high-height end has finite weighted length because H is integrable there. A separate canonical comparison is needed to control ordinary contour geometry. The exact tangent ratio supplies a sharper object than an indiscriminate norm bound, particularly its continuous argument.

[Continuation 17](../notes/17_CONTINUATION_CONSERVED_SPATIAL_CONTOURS_20261023.md) and the overview identify a concrete microscopic Gaussian-expansion target under initial RH. It is expressly **unproved** and is not presented as a theorem in main.tex. Its fixed positive-offset strip, scale s<=c/(log Y)^2, initial logarithmic-derivative bounds, complete relative tails and derivative margins are explicit obligations. If proved, it would give a conditional canonical wall/contour lemma, not the missing interior resource estimate or completion of the overarching SIMP goal.

The progress file therefore keeps SCF-01–04 open at their analytic scope. Promotion to the book requires a completed useful proof and a demonstrated role in a stronger estimate or a significant intermediate theorem. A numerical campaign, formal hierarchy count or generic conditional flow criterion cannot satisfy those goals.

## References and verification

Seven bibliography entries were added to main.tex: Noether, Cole, Hopf, Ibragimov's distinct 2006 and 2007 articles, Anco, and Papanicolaou–Kallitsi–Smyrlis. The [catalog](../../references/README.md) retains their exact reading/availability scope. The archived ALGA volume is not misidentified as the JMAA article. No general hierarchy-completeness or collision theorem is imported from those references.

The [build record](../../manuscript/CONSERVATION_BUILD_RECORD_20261023.json) records the final compilation, PDF text/layout checks and source identities. The [chat verification receipt](../chat-histories/VERIFICATION_SPATIAL_CONSERVATION_20261023.json) records local archive integrity and source coverage, with the wider registration scan distinguished from archive validation. Build and transcript checks do not establish mathematical correctness.

This is a provisional exposition and research-handoff milestone. No new simplicity proportion, every-zero theorem, useful growing-height inward-flux estimate or stochastic cancellation is claimed.
