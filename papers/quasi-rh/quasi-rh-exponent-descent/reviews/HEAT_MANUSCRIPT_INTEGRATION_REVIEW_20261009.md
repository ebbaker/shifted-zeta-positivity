# Heat manuscript integration and next-chat handoff

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex). Reasoning effort: ultra, verified from the current
chat's recorded configuration. Same-model read-throughs are internal checks,
not independent mathematical validation.

## Stable manuscript and scope

The heat investigation previously had research notes rather than a manuscript.
The stable source is now
[newman_collision_reductions.tex](../newman_collisions/newman_collision_reductions.tex).
It consolidates Heat Notes 1–7 and the
[analytic continuation assessment](../notes/ANALYTIC_RH_CONTINUATION_AND_MANUSCRIPT_RESULTS_20261009.md),
with proofs, explicit imported inputs, and a conditional research outlook.
The separate short-family and mixed-family manuscripts retain their own scope.
No snapshot folder or new Git commit is created by this integration.

The main text develops the finite positive-time collision reduction, the
positive-kernel counterexample, the theta-cutoff endpoint obstruction, the
holomorphic normalized approximation and derivative-error interface, the sharp
exact-field probe comparison, and the all-zero count floor with its landing
argument. The appendix presents the effective high-sector probe and the two
compact local certificates. The ordinary double-collision expansion explains
why finite attraction gains do not rule out a positive collision time.

The manuscript does not assert RH, a new zero-free strip, an effective value
for the unprinted counting constant, or a competitive Newman bound. The
conditional high-sector endpoint remains conditional on every maximizing root
staying in that sector. The tiny mirror-patch gain is stated only as a
historical comparison with its actual earlier-time canopy input. Compact
certificates retain their local scope and explicit arithmetic/software inputs.
Literature novelty remains unestablished. Polymath, Rodgers–Tao, and the
existing collective-attraction framework receive attribution.

## Validation

The complete standalone source compiled successfully with the desktop
editor's built-in compiler. The main-text and appendix read-throughs checked
the Fourier and normalization constants, derivative signs, explicit disk
majorants, own-pair subtraction, pairwise comparison polynomials, all-zero
counting blocks, landing derivative and gain, paid phase criterion, and
last-block absolute-mass asymptotic against their source notes and direct
algebra. A missing spacing-command backslash was corrected, and the
maximum-envelope proof now explicitly extends the local Hermite splitting
argument to complex multiple roots. The revised source also compiled
successfully. Bibliographic titles and version identifiers for Polymath,
Gasper, and Planat were checked against their primary arXiv records.

The existing effective-probe checker passed all 105 exact scalar assertions;
its output was byte-identical to the saved record and its checker hash
matched. The compact certificates were checked against their existing
programs, notes, and records; no new grid or numerical investigation was run.
Archive validation checked original public message text, timestamps and
order, all seven human requests, the parent/children mapping, stable numbering
1 with next 2, file hashes, and preservation of imported fields. A shorter or
older refresh is refused by default, without changing the registry; explicit
override preserves the existing number. The final installed files are
hash-checked and remain below the repository's small-file limit.

Successful compilation checks source syntax and typesetting. These scoped
internal audits do not independently prove the imported analytic theorems
or replace specialist review. No compiled PDF export is asserted: the stable
source opens in the built-in editor with its PDF preview.

## Next chat: positive-time collision exclusion

Begin with the direct target

\[
H_t(x)=H_t'(x)=0,\qquad t>0,\ x\in\mathbb R,
\]

and the signed many-term collision vector in the shrinking-time regime

\[
\kappa=t\log(x/(4\pi))\in[1,2],\qquad
x=4\pi e^{\kappa/t},\qquad N\asymp e^{\kappa/(2t)}.
\]

The bounded next task is to retain the genuine coefficient phases and derive
one useful uniform joint value/derivative inequality with complete
approximation and cutoff payments, or to prove a precise obstruction for the
chosen analytic mechanism. It is not a request to prove RH in one step.
Absolute coefficient tails grow exponentially for compact \(\kappa\)-ranges
inside \((0,4)\); a finite head or fixed finite-prime mollifier does not remove
that obstruction. The conditional amplitude/phase criterion in the manuscript
is an interface, not an established nonvanishing estimate in this regime.

Retain collective attraction as an optional positive-bound application.
Correlated translated probes may supply useful signed information, but have
no endpoint theorem here. The fixed-scale response contraction, short-family
compensation, and gated mixed covariance remain separate conditional routes;
the current assessment lists their exact open inputs. Do not substitute a
large numerical grid or threshold optimization for the signed estimate
without a fresh reason tied to the endpoint obstruction.

## Conversation archive

This chat starts the investigation's
[chat-histories folder](../chat-histories/README.md) as number **1**.
[index.json](../chat-histories/index.json) reserves **2** for the next new
conversation. Dates and message timestamps come from the recorded source;
capture times are recorded separately in UTC and America/New_York. The JSON
uses a ChatGPT-style conversation mapping with original public messages,
including commentary. It is explicitly identified as a local export-style
conversion. Runtime instructions, internal reasoning, tool output, and
subagent messages are excluded. A capture during an active response records
completed messages through capture; a later refresh can include subsequent
messages without changing number 1.

Future chats should use the next unused number from the registry. Historical
imports keep their original dates and receive a new stable capture/import
number; they do not renumber existing records. The folder's recorder accepts
individual conversations from a provider JSON data export and preserves their
original message fields. Large account exports and raw runtime session files
remain outside this repository under its large-file policy.
