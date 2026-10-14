# Manuscript rewrite and continuation

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**, verified
from this reply's rollout configuration. Earlier research and certificates
also used gpt-6.1-sol. This is an internal research handoff, not an external
referee report or a formal verification.

## Current manuscript and preserved version

The author requested a fresh exposition, permission to remove peripheral
material, a backup of the previous manuscript, and this continuation note.
The stable [source](../manuscript/quaternion_theta_geometry.tex) has been
rewritten as **Uniform Laguerre signs and hypercomplex jets of the theta
heat flow**. The [PDF](../../../../../output/pdf/quaternion_theta_geometry.pdf)
is 24 pages, compared with the previous 35 pages. The author field reads
“Drafted for Edward Baker”; the acknowledgment describes LLM assistance.

Before replacement, byte-identical copies were saved as the
[previous source](../manuscript/quaternion_theta_geometry.backup_20261014.tex),
[previous PDF](../manuscript/quaternion_theta_geometry.backup_20261014.pdf),
and [previous build record](../manuscript/BUILD_RECORD.backup_20261014.json).
The [backup receipt](../manuscript/BACKUP_RECORD_20261014.json) records their
hashes and the author's explicit backup request. No snapshot directory,
commit, or tag was created in this reply. The pre-rewrite checkout was at
`507fd88928f97c29ec063f6d4df03b67867ed31a`.

The final source SHA-256 is
`6242fd49c4d1c8f08efbfa798ef5f1ac66544999e11e1426af43418950971e12`;
the exported PDF SHA-256 is
`3999525f5fedd9508881e9bd28b65bbf9529fe425b274d66c93c8f3149746b3e`.
The [build record](../manuscript/BUILD_RECORD.json) and
[integration review](../reviews/13_MANUSCRIPT_REWRITE_INTEGRATION_REVIEW_20261014.md)
bind the delivered version and distinguish current checks from earlier
numerical replays.

## Exposition and results retained

The new manuscript begins with the four physical derivatives
\(h_j=\partial_x^jH\), the first-pair energy
\(E=h_0^2+h_1^2\), and the two Laguerre forms
\(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\). Its main line is:

1. **Uniform outer positivity (Sections 1–2).** For every fixed
   \(\varepsilon>0\), both forms are strictly positive for
   \(0<t\le1/2\), \(|x|\ge X_\varepsilon\), and
   \(t\log(|x|/(4\pi))\ge4+\varepsilon\). All four derivatives share
   one nonzero complex arithmetic amplitude. The proof retains the
   uniform weighted-sum argument as time varies, replaces the moving
   cutoff by an analytic model, and uses discs of radius \(1/\log x\)
   before taking derivatives. Four is a sufficient summability threshold,
   not an asserted optimal boundary. No numerical \(X_\varepsilon\)
   has been evaluated. See [Note 17](17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md).
2. **The collision criterion (Section 3).** The scalar heat-flow inputs
   imply RH if and only if there is no positive-time real multiple zero.
   Uniform confinement prevents a positive threshold from being attained
   only at infinite height. Both even- and odd-multiplicity predecessor
   branches are included. A bound
   \(\mathcal L_j\ge-K_jE\) on \(h_{j+1}=0\), with \(K_j\) locally
   bounded through each candidate positive-time collision, excludes it.
   The cubic control explains why the second stationary set is necessary.
3. **Quaternionic and octonionic geometry (Section 4).** The independent-
   time Fueter lift, its heat/jet equations, and the explicit eight-
   dimensional monogenic extension are proved. The physical four-jet
   package lies in an associative quaternion subalgebra. Its total norm
   does not detect the vanishing of the distinguished first pair, whereas
   oriented associators recover \(E\), \(\mathcal L_0\),
   \(\mathcal L_1\), and \(E_t\) exactly. A strictly positive entire
   source with a positive-time collision shows that these identities and
   source positivity alone cannot supply the theta-specific sign.
   See [Note 15](15_OCTONIONIC_LIFT_AND_ASSOCIATOR_SIGN_TARGET_20261014.md).
4. **Centered residuals and shared arithmetic (Section 5).** Complete-
   source contour shifting, the exact common carrier, its staircase
   cutoff, logarithmic weights, full stationary-ideal sum-of-squares
   identities, and balanced quaternion evolution are retained. The
   varying-parameter correction is explicit. Source and integration
   remainder proofs are collected in Appendix A.
5. **Closed finite coverage (Section 6).** The central analytic theorem,
   the 272-cell cover through 41, the 510 cells through 100, and the
   32-cell centered pilot through 104 together prove
   \(|F|>10^{-16}\) and both strict stationary signs on
   \(0\le t\le1/2,\ |x|\le104\). The pilot's residual cone proves
   the first strict sign and a second bounded-loss estimate; the second
   strict sign is separately certified. See
   [Note 16](16_THETA_CENTERED_RESIDUAL_AND_SHARED_ARITHMETIC_20261014.md).
6. **Obstructions and the remaining estimate (Section 7).** Absolute
   first-channel dominance fails in the inner scaling below four.
   Validated examples disprove phase-independent and actual-carrier
   pointwise integrand positivity at specified points; they do not
   disprove integrated Laguerre positivity. Staircase boundary phases
   cancel exactly. A close-pair control shows that a small residual norm
   can charge favorable curvature as an error. These results lead to the
   one-sided target below.

The rewrite removes the chronological buildup, repeated criterion maps,
the separate global scalar-curvature route, full Cauchy–Fueter boundary
and current developments, angular-gluing estimates, and guarded forward-
collar details from the main exposition. Their research records remain
in Notes 1–14 and the backup. The untwisted transverse/primitive
associator variants remain in Note 15; the directly signed twisted
associators carry the new exposition. Earlier padded-rectangle steps are
summarized through their stronger full-time certificates. No historical
note, review, numerical source, or certificate was deleted.

## What remains open

For fixed \(\varepsilon>0\), the unresolved domain consists of the finite
transition strip \(104<|x|<X_\varepsilon\) and the high-height inner region
\[
0<t\le1/2,\qquad |x|\ge X_\varepsilon,\qquad
 t\log(|x|/(4\pi))<4+\varepsilon.
\]
The outer theorem is uniform in time, but its height bound is not yet
numerically connected to the finite certificate. It implies only the
asymptotic statement
\(\limsup T_k\log(|a_k|/(4\pi))\le4\) for any hypothetical sequence of
positive-time real collisions with \(|a_k|\to\infty\). Neither a finite
universal cutoff of four nor RH has been proved.

With \(\mu=a^2+b^2\) and
\(C_j=-h_{j+2}-2ah_{j+1}-\mu h_j\), the useful remaining target is
\[
 h_jC_j\ge-\mu h_j^2-K_jE
 \quad\text{on }h_{j+1}=0,\qquad j=0,1.
\]
The loss must remain locally bounded through every candidate joint zero
at positive time. Growth towards time zero is allowed. A definition of
\(K_j\) by dividing an uncontrolled negative remainder by the unknown
energy would be circular. A proof must retain all arithmetic and
integration cross terms and pay every omitted index and integration tail.

## Recommended next work

**Primary analytic target:** derive a signed estimate for oscillatory
blocks of the exact common arithmetic sum and its first two logarithmic
moments in the inner scaling \(t=\vartheta/\log x\). Keep the staircase
\(n\le e^{2v}\), its entering-index terms, and the actual carrier phase.
Then express the stationary quadratic observation as the complete double
integral, retaining cross terms between different carrier coordinates.
The desired outcome is a one-sided bound for the adverse part of
\(h_jC_j\), with an explicit loss regular at a candidate positive-time
collision. Pointwise phase-free positivity is already too strong.
Dyadic block bounds or a cancellation-preserving transform are candidate
routes, not established estimates. Any improvement of the number four
must be uniform in time and in all four physical derivatives.

**Parallel quantitative target:** make the constants in Section 2
explicit for one chosen value, for example \(\varepsilon=1\). Bound the
weighted-sum discrepancy, imported approximation errors, microscopic-disc
amplitude comparison, and derivative errors until the normalized
four-jet error is at most \(1/8\). The displayed perturbation algebra
then gives positive Laguerre lower bounds without phase exclusions.
Report the resulting \(X_1\) even if large; assess finite-strip coverage
only after that bound is known. Do not treat the existing certificate
through 104 as covering that strip automatically.

A useful computational pilot should test whole closed cells, retain true
stationary conditions, and distinguish failure of a sufficient cone from
failure of the one-sided target. Selected-point calculations can guide
this work but cannot close an unbounded domain. Further algebraic
extensions should be pursued only when they sharpen the signed arithmetic
observation or reveal a source-specific identity.

## Validation and reproduction

The saved source passed the desktop LaTeX compiler. The exported PDF has
24 pages; the stabilized export log has no warnings. All pages were
inspected in contact sheets and representative mathematical, certificate,
and provenance pages were inspected individually. The source has 118
unique labels, six bibliography entries, and no missing references or
citations. The focused independent internal review covers the outer
proof, hypercomplex section, residual/shared-carrier section, obstructions,
and source-payment appendix. Its author drafted the collision and finite-
certificate sections, so those are not described as independently reviewed
by that same agent. Root checked their integration and final artifact.

Fresh compact replays passed **6682 + 547 + 248 + 9** exact checks.
These audit existing records and algebra; full interval quadratures were
not rerun for this editorial rewrite. Their independent numerical replays
remain documented in Reviews 6, 9, and 11. The new compact
[check receipt](../numerics/MANUSCRIPT_REWRITE_CHECKS_20261014.json)
records the sources, inputs, and scope.

From the investigation's `numerics/` directory:

```sh
python3 audit_correlated_source_height_records.py --output /tmp/inv21-height-audit.json
python3 audit_theta_centered_residual_record.py --record THETA_CENTERED_RESIDUAL_100_104_20261014.json --output /tmp/inv21-centered-audit.json
python3 check_octonion_jet_identities.py --output /tmp/inv21-octonion-checks.json
python3 check_theta_centered_residual_identities.py --output /tmp/inv21-residual-checks.json
```

These four use the Python standard library. See Appendix B, the retained
numerics guides, and the earlier reviews for the longer interval runs.

## Chat-history continuation

This chat retains thread id `01a13c7b-d95c-72d0-85a3-a8a118ae8cec` and its
sole formal-replay registration, number **8**:
[registered history](../../../formal_replay_crosswalk/chat-histories/0008_2026-10-14T22-15-11Z_summarize-quaternion-theta-results.json).
The user requested that identity be preserved. Completed public text was
refreshed at the beginning of this reply; the final workflow refreshes it
again and arranges the bounded exact-turn capture for
`01a13cc2-f5cd-7e71-800c-f2fb71c9e3b4`. The unsent final reply cannot yet be
part of this note's capture evidence. Check the registry or worker status
at the next turn, and use the ordinary refresh to catch any missed final
message. Native-hook activation has not been verified. Future unrelated
investigation chats should use their own investigation history folder.
