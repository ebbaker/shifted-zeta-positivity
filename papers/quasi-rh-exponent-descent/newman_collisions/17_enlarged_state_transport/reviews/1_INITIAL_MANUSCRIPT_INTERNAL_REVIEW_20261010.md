# Project 17 initial manuscript: internal mathematical review

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex), reasoning effort ultra, as verified from the
recorded drafting-turn configuration. This source cross-reading and exact
algebra replay are internal LLM work, not independent mathematical validation.

## Scope and disposition

Reviewed [Enlarged-state transport and visibility for the Newman heat
flow](../enlarged_state_transport_and_heat_flow.tex) against
[Heat Note 25](../../notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md)
and the physical dictionary and complete holomorphic interface in
[program 09](../../09_prime_phase_torus/prime_phase_torus_signed_reductions.tex).
The manuscript is suitable as an initial account of exact structures and
conditional criteria. No defect was found in the main certificate,
shrinking-sector implication, chord equations, Gaussian control, angular
identity, or reflection operator. Useful multiplier bounds and a signed
theta estimate remain open; the manuscript establishes no new collision
exclusion or RH conclusion.

## Checked mathematical boundaries

- **Imported physical interface.** The draft defines the genuine kernel,
  nonvanishing normalizer, complete finite sum, actual carrier and amplitude
  drift. Its radius-\(1/L\) bound is explicitly an imported complete
  fixed-cutoff hypothesis, including normalization, reflection and cutoff
  conversion. All spatial derivatives freeze time, the integer cutoff and
  the center scale. A smaller block or shifted source does not inherit the
  complete candidate equations. A strictly positive error majorant is used
  when dividing by \(\eta_N\).
- **Source selection and elimination.** Prescribed divisor edges and the
  index-one source uniquely determine the state. The twist defect requires
  complete multiplicativity, which is now stated. Positivity of the anchored
  operator and its hidden coordinate blocks is proved without observation
  nonvanishing. The added block Schur formula retains both the hidden
  reconstruction and the induced source; its signs and inverse placement
  are correct. The source derivative and fixed-\(t,\sigma\) gauge relation
  are correct. A positive bulk gap alone cannot control the projected
  oscillatory response.
- **Visibility certificate.** Realification introduces no missing factor:
  each integer block has norm \(w_n\), and pairing the adjoint identity gives
  \(1=y\cdot Cq_R+r\cdot q_R\). The weighted residual payment and the
  Euclidean and directional candidate bounds have the printed constants.
  The strict margins exclude every multiplicity on their certified domain.
  The text correctly distinguishes this lemma from a constructed certificate
  and forbids division by the unknown joint observation. Uniform residual
  gap and multiplier growth below the stated exponent would give eventual
  exclusion; those hypotheses and an effective starting time are not proved.
- **Chord lift and control.** The backward heat sign, gradient-overlap
  commutator and transverse source coefficient \(r(2r-1)/2\) are correct.
  The observed slice is autonomous, and no transverse feedback theorem is
  inferred. The gradient density has a signed Fourier transform. The
  polynomial-closure obstruction excludes only the stated finite local
  closure. The Gaussian quartic, discriminant and ordinary doubles at
  \(\pm\sqrt6\) are correct on the stated bounded time interval; this is
  not an all-time theta family.
- **Angular preparation.** The differential-shift identity has the required
  endpoint source and positive \(2it\mathcal T_z\) term. Jacobi symmetry
  gives \(k'(0,0)=-1\); the resulting affine Ward identity has the correct
  constant and derivative signs. Actual integer coefficients and gluing
  retain more data than periodic heat evolution. The fixed shift by \(-4i\)
  lies outside the imported approximation disk and requires its own
  normalization, correlation and error payment. The displayed growth
  envelope does not claim such a small approximation payment.
- **Stationary reflection.** The map on \(L^2(\mathbb R_+,dv)\) is a linear
  unitary involution; adding conjugation gives a different antiunitary map.
  The leading stationary coefficient is correctly scoped as local data.
  Literal intervals reflect to their paired exterior intervals. The ideal
  moment reflection fixes the threshold quadratic; actual center, carrier,
  weight and endpoint defects remain payable before using it.

The motivation's finite-threshold reduction also names the needed external
input. [Polymath Theorem 1.5(i),(ii)](https://arxiv.org/html/1904.12438v2)
provides large-height reality and simplicity uniformly away from time zero;
together with simple-root continuation and compact zero control, this
supports the stated finite collision consequence of a positive threshold.
It is not deduced from the new local lift.

## Corrections and verification

The review requested complete-multiplicativity wording, definitions of the
moment symbols in the reflection discussion, explicit ideal-reflection
scope, and removal or definition of an otherwise undefined rational-frequency
integral notation. The positive-majorant convention and the real-time scope
of the angular growth envelope were also identified for explicit wording.
All were incorporated in the reviewed final source. These are local
precision and self-containment clarifications, not changes to the
substantive proofs. The final added elementary Schur reduction was also
cross-read and verified. The root agent saved that final source in
`17_enlarged_state_transport/` and reported a successful native
`compile_latex_document` result for the saved manuscript. This confirms
compilation; this review does not claim PDF export or a page count.

A fresh replay of the shared
[exact checker](../../13_microlocal_phase_space/numerics/check_enlarged_state_identities.py)
passed **15,446 exact Fraction assertions**: 257 graph, 27 Gaussian, 162
chord and 15,000 score checks. The source SHA-256 was
`645292360a4afc8edb49a6ffec550ec4277d4c74c8497164050aaf1f058b2435`.
The replay record was written only in temporary storage; the original
checker and shared record were not changed. This replay validates finite
printed algebra, not the infinite theta state, imported disk theorem,
huge-height signs, outward candidate coverage or useful multiplier bounds.

The next mathematical milestone is a regular adjoint witness with a strict,
fully paid margin on a stated nonempty domain, or a genuine theta-specific
signed overlap estimate feeding that margin. Global cutoff and parameter
coverage remain separate obligations.
