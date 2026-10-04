# Internal review of positive channel absorption

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning
effort are not exposed and are not inferred. The parent and three
separate agents used the same model family. This is an internal
analytic audit, not independent specialist refereeing. No priority claim.
Repository baseline: `5052fc961dc755718f2cf88516e78096eb9e8edf`.

Reviewed source:
[Positive channel absorption](../notes/POSITIVE_CHANNEL_ABSORPTION_20261003.md).

## Mathematical assessment

The continuation establishes an exact positive ambient construction and
an unconditional obstruction to its intended asymptotic use. It also
establishes a selective relative-source construction with a precise
unproved loss estimate. The obstruction applies to positive ambient
operator splittings, not all positive quadratic-form constructions on
the source space.

The following points received separate internal checks:

- The explicit boundary maps W_plus/W_minus multiply to the positive
  and negative ambient spectral clips; the Sonin projection is in the
  negative clip. The main is B+N and the adverse loss is E, with K=E-N.
- The state-space maps are contractions, but they do not yield a
  contraction against the independently positive source energy B.
- Multiplication by sign(mathcal Q) establishes the absolute smoothed
  trace class. The actual C4 probe has sufficient finite regularity;
  the harmonic-oscillator factorization uses only four kernel
  derivatives and has inverse squared HS norm pi squared/24.
- Testing the signed trace by a bounded frequency multiplier gives the
  absolute diagonal lower bound with measure dt/(2pi). Its sign and
  factor one half in the loss bound are correct.
- Partial summation from ordinary PNT is uniform on each fixed compact
  frequency interval. All higher powers of the finite Euler phase
  contribute O(log X), and no zero-free-strip assumption is used.
- The moving-pair multiplier is a_g(1+cos rt), without an extra factor
  two. The even harmonics of absolute cosine cannot resonate with
  r=log X-ell. Consequently the exponential adverse-loss obstruction
  holds on the actual normalized pair, not just on the fixed bump.
- The signed pair form is o(sqrt X) by preparation and ordinary PNT;
  this is weaker than the target subexponential bound and does not
  assume it.
- The crossing kernel splits into a local triangle plus half a remote
  strip. Compression gives (r-ell)/2<=nuclear norm<=(r+ell)/2. The
  HS identity has coefficient r/4. Moment neutrality does not remove
  this linear nuclear growth.
- Exact source clipping at threshold one has a finite-rank adverse
  form. Its nonzero relative eigenvectors lie in the B form domain,
  so the loss is also a bounded finite-rank form on ordinary source L2.
- The approximate source split uses a full norm enclosure of H-J. It
  never uses operator monotonicity of the positive-part function. Its
  positive defect G_J gives an exact split, and its loss depends on
  source-weighted eigenvector overlaps, not merely on relative entries.
- Mixed columns and source-domain regularity are retained. An ordinary
  finite numerical compression is not substituted for the inherited
  full-space approximation.
- The primal residual factors through T. Coisometry removes one scalar
  inverse-gap factor; the proposed dual preimage still requires an
  independent full norm estimate. Onto-ness alone does not supply it.

## Corrections incorporated during review

Two agents independently requested an explicit distinction between the
finite-product bulk Q_S and full Q. The final note now labels its
ambient identity Q_S and requires capture of every active prime before
identifying it with Q. The source scope is smooth compact prepared
sources plus the specific g-pairs covered by the proved extension.

Two agents also identified the boundary case eta=1: the complementary
main then vanishes, but the loss J_plus is still finite rank. The final
note correctly distinguishes this from eta>1, where the complementary
loss has infinite rank. Choosing eta<1 retains positive complementary
energy.

A third agent noted a notation collision between the prime cutoff and
crossing operator. The prime cutoff is now mathsf X_r and the crossing
operator remains X_r.

## Inputs and scope

The inherited finite Euler identity, source closure, relative compactness,
mixed-column approximation, and special-probe one-sided theorem are
linked in the note. The external analytic input is ordinary PNT;
[NIST DLMF 27.12](https://dlmf.nist.gov/27.12) was checked on this date.
No third-party PDF or new generated data was saved.

The exponential lower bound is asymptotic. No numerical value for its
first applicable separation is certified. The selective source loss
has no proved global growth bound, and fixed-window compactness does
not bound its ranks or overlaps uniformly. Neither RH nor all-window
positivity is proved. The result does not rule out the user's broader
absorption strategy.

## Artifact validation

Only the new research note, this review, and a targeted README index
entry are installed. The manuscript, draft history, existing numerical
records, and all pre-existing uncommitted changes are preserved. No
manuscript compilation is needed because no LaTeX source is edited.

Validation covers relative links in the two new files, file sizes under
the repository's 1 MiB convention, and whitespace checks on the new
files and index edit. No new numerical experiment is claimed; the
validation of the mathematical results is analytic and internally
cross-checked. No commit or push is made.
