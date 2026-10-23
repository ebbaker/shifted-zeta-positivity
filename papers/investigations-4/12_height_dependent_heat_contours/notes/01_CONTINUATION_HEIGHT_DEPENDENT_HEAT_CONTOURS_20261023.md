# Continuation of the height dependent heat contour program

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **max**.

Resume in [Investigation 12][home]. The next research task is **HDC-01**, the finite-height geometry and comparison contract in the [sole progress register][progress]. Setup is complete; the first complete theta estimate and a demonstrated advantage over direct estimation remain open. This continuation records the agreed direction and the handoff, without changing those statuses.

## The question to carry forward

The author proposes a contour whose right face is a fixed small positive time \(\delta_{H_{\max}}>0\) for each finite maximum height, interpreted eventually as \(0^+\). The left face is \(t=-\epsilon(h)\), with its backward width allowed to shrink as height increases. Divide the intervening region into moving cells adapted to heat evolution, cancel their shared faces exactly, and estimate what remains using Rodgers–Tao reference subtraction and controlled evolution or Taylor remainders.

The latest refinement takes priority: **use the deformation to make the original time-zero integral easier to bound**. Collision exclusion is a possible subsequent application. Do not require a collision-free collar merely to obtain the lower-bound transfer that is already available.

For the physical first jet \(G=(H,H_z)\), with \(H_\tau=-H_{zz}\), the inherited negative-collar balance is

\[
I_0=I_{-\epsilon}-S_\epsilon+Q_-,
\qquad Q_-\ge0.
\]

Here both caps have the forward parameter orientation, and \(S_\epsilon\) includes every other outward face. Thus the immediate observable is

\[
B_\epsilon:=I_{-\epsilon}-S_\epsilon,
\qquad I_0\ge B_\epsilon.
\]

These statements require a regular complete boundary; boundary events need excisions or a justified limiting treatment. Exact equality with the complete deformed representative requires \(Q_-=0\). The nonnegative charge counts complex joint events, so the physical cap includes imaginary time. A real zero-trajectory calculation alone does not estimate that cap.

## What is already available

The [founding brainstorm][brainstorm], [self-review][review] and [program overview][overview] contain the working formulas and their hypotheses:

- Projective transport of \(q=H/H_z\) gives a material velocity agreeing with zero motion. Constant projective-radius sides have zero flux on actual regular charts. Chart degeneracies can occur away from collisions, so a covering and its connecting faces must be justified.
- For an isolated finite simple cluster, the complete product \(\mathscr D=\prod_jH_z(\tau,z_j)\) satisfies
  \[
  \frac{d}{d\tau}\log\mathscr D
  =8\sum_{j<k}(z_k-z_j)^{-2}+\mathcal B_U.
  \]
  The analytic-factor term \(\mathcal B_U\) is explicit in the overview and stays in every estimate. Its cancellation with the pair term can matter.
- On the declared regular real-symmetric root tubes, the physical cap is an imaginary-time integral of the real part of this logarithmic derivative. Its transverse Taylor remainder involves the second time derivative. Those domains and derivative bounds remain source inputs.
- A separately isolated two-root cluster obeys \(\Delta'=8+A\Delta\). With an independently bounded wall coefficient \(|A|\le K\), the sufficient radius from an anchor discriminant \(\Delta_0\) is
  \[
  T_K=K^{-1}\log(1+K|\Delta_0|/8),
  \qquad T_0=|\Delta_0|/8.
  \]
  A cross-zero rectangle must satisfy
  \(\sqrt{(\delta+\epsilon)^2+Y^2}<T_K\).
  This is a survival comparator when survival is the target, not a replacement for the cap comparison.

The [exact algebra record][checks] supports the finite identities. It is not a theta certificate. The review is by the same assistant. Rodgers–Tao supplies the reference subtraction mechanism; its hypothetical all-real negative-time interval cannot be imported as an unconditional premise here. Real convexity also does not give a sign after complex-time continuation.

The candidate scale \(\epsilon(h)=c(h)/\ell(h)^2\), with \(\ell(h)=\tfrac14\log(h/(4\pi))\) for \(h>4\pi\), remains a proposed normalization. Close gaps and exterior interactions may demand smaller widths. No decreasing positive schedule has been established.

## The next bounded task

Complete HDC-01 in a new research note before starting a broad numerical campaign:

1. **Fix one finite band and one observable.** Specify the cap population, spatial boundary, imaginary-time thickness, negative width, projective radii and orientations. Start with a constant width on that band if useful. Retain the small positive face when considering the full cross-zero region.
2. **Declare boundary and event treatment.** List spatial walls, imaginary-time faces, exposed joins and endpoint excisions. Distinguish independently justified charts from proposed ones. Do not assume interior separation or an all-real interval to establish their own continuation.
3. **Specify the reference and complete inputs.** State which source tails, jets, wall minima, population counts, analytic-factor derivatives and complex-time bounds are available, conditional, or still to be acquired.
4. **Fix the comparison.** Give direct estimation the same source information and signed correlations. The default deliverable is a lower bound for \(I_0\) obtained through the complete \(B_\epsilon\). Compare the resulting lower bound, verification cost, or strength of hypotheses with direct estimation of the same quantity.
5. **Identify the first coupled estimate.** State precisely which combination will be bounded after shared-face cancellation and reference subtraction. Keep linear corrections, exterior terms, analytic-factor terms, transverse errors and joins together as required by the identity.

HDC-02 then derives that complete renormalized expression. HDC-03 acquires or proves its theta inputs; HDC-04 performs the comparison. Height assembly and event-exclusion applications remain later tasks in the existing register. A useful result may be a sharper bound, an equally strong bound at lower cost, a simpler applicable theorem, or a precisely scoped failure of the tested mechanism.

Use the [result summaries][results], especially [local heat geometry][geometry] and [collision controls][controls], together with the [patterns to avoid][avoid], [target classification][classification] and [coupled-estimation rule][coupling]. The proposed finite estimate is a quantitative milestone; an eventual RH-equivalent criterion would require separate classification. Preserve the canonical-source distinctions listed in the overview when applying the control families.

Retain the elementary controls: \(H=z^2-2\tau\) prevents a false crossing of an event at zero; a shifted quadratic prevents an unsupported extension to later positive times; the sine heat solution checks the analytic-factor contribution. A failed comparison concerns its specified information and estimator class.

## Reading and records

Read the [original structural-cancellation continuation][original], the founding brainstorm and self-review, then the new overview and progress register. The [README reading guide][home] also links the inherited collar and two-root derivations and the primary papers by Rodgers–Tao, Csordas and collaborators, Papanicolaou and collaborators, and Polymath.

Save new Investigation 12 derivations in notes, computations in numerics, and assessments in reviews. The founding brainstorm notes are now housed in the series-wide Investigations 4 brainstorm, following the author's 23 October affiliation correction. Update the sole HDC register when a deliverable is actually completed.

The conversation **Study height-dependent epsilon** retains its unique [brainstorm archive 0001][chat]. The [verification record][verification] identifies the checked snapshot, source coverage, stored-byte and canonical-content hashes, and prior completed-turn capture. Later ordinary refreshes legitimately change the snapshot hashes and count. This turn's final reply is captured only after it is sent, through the bounded exact-turn follow-up prescribed by the [history workflow][history-policy].

## Suggested continuation request

> Continue Investigation 12 from this note and complete HDC-01. Specify one finite-height contract for a lower bound on the original time-zero physical cap through the complete negative-time deformation. Preserve all connecting faces and the analytic-factor contribution; identify independently obtainable source inputs and an equally informed direct comparator. Then identify the precise coupled estimate to attempt in HDC-02. Keep derivations in this investigation's notes folder and update its sole progress register. Preserve this conversation's existing archive identity.

[home]: ../README.md
[overview]: ../research-overview/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRAM_20261023.md
[progress]: ../research-progress/01_HEIGHT_DEPENDENT_HEAT_CONTOURS_PROGRESS_20261023.md
[brainstorm]: ../../brainstorm/notes/02_MOVING_COLLAR_MATERIAL_ENERGY_AND_HEIGHT_DEPENDENT_EPSILON_20261023.md
[original]: ../../brainstorm/notes/01_CONTINUATION_STRUCTURAL_CANCELLATION_RODGERS_TAO_AND_BACKWARD_HEAT_20261023.md
[review]: ../../brainstorm/reviews/01_MOVING_COLLAR_AND_MATERIAL_ENERGY_SELF_REVIEW_20261023.md
[checks]: ../../brainstorm/numerics/MATERIAL_JET_ENERGY_CHECKS_20261023.json
[chat]: ../../brainstorm/chat-histories/0001_2026-10-23T07-39-02Z_study-height-dependent-epsilon.json
[verification]: ../chat-histories/VERIFICATION_20261023.json
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[classification]: ../../../../avoid/01_restating_the_target.md
[coupling]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[history-policy]: ../../../../tools/CHAT_HISTORY.md
