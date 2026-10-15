# Uniform Laguerre signs and hypercomplex jets of the theta heat flow

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Current rewrite: **gpt-6-astra (Codex)**, reasoning effort **ultra**.
Earlier research and certificates also used gpt-6.1-sol.

The [standalone LaTeX manuscript](quaternion_theta_geometry.tex) is the
stable investigation 21 source. At the author's request it has been
rewritten around the uniform outer-region Laguerre theorem, its collision
consequences, the quaternionic/octonionic jet constructions, the exact
shared arithmetic carrier, and the complete finite certificate through
height 104. Source-payment proofs and reproducibility details are in
appendices. Earlier peripheral developments remain in the notes and backup.

The principal analytic result proves both Laguerre forms strictly positive
at sufficiently large heights with t log(|x|/(4 pi)) >= 4 + epsilon, for
each fixed epsilon > 0, uniformly over 0 < t <= 1/2. The height cutoff has
not been evaluated numerically. The bounded result proves both stationary
signs and |F| > 1e-16 on 0 <= t <= 1/2, |x| <= 104. The finite transition
strip and the high-height inner region remain unresolved; no RH theorem
is claimed.

The [PDF](../../../../../output/pdf/quaternion_theta_geometry.pdf) has
**24 pages**. The saved source compiled successfully with the desktop
compiler; the terminal export has no warnings. All pages passed contact-
sheet inspection, with additional individual-page checks. Standard LaTeX
packages suffice. Build auxiliaries remain outside the checkout.

The [build record](BUILD_RECORD.json),
[integration review](../reviews/13_MANUSCRIPT_REWRITE_INTEGRATION_REVIEW_20261014.md),
and [continuation note](../notes/18_MANUSCRIPT_REWRITE_AND_CONTINUATION_20261014.md)
identify the final version, current checks, earlier independent numerical
replays, and remaining targets. Open the source for editable text and
live PDF preview.

The previous **35-page** version was preserved before replacement:
[source backup](quaternion_theta_geometry.backup_20261014.tex),
[PDF backup](quaternion_theta_geometry.backup_20261014.pdf), and
[build-record backup](BUILD_RECORD.backup_20261014.json).
The [backup receipt](BACKUP_RECORD_20261014.json) verifies their identity.
This individual-file backup fulfills the author's explicit request; no
new manuscript snapshot directory, commit, or tag was created.

## Subsequent research, 14 October 2026

[Note 19](../notes/19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md)
proves a sufficient asymptotic threshold of three and develops exact paired
Laguerre integrals; [Note 20](../notes/20_EXPLICIT_OUTER_HEIGHT_BOUND_20261014.md)
gives an explicit height for the separate threshold-five region. These
internally reviewed developments are saved as research notes and have not
yet been integrated into this manuscript. The current source, PDF and
build record retain their delivered identities. Prepared for Edward Baker
with substantial LLM assistance, **gpt-6-astra**, effort **ultra**.
