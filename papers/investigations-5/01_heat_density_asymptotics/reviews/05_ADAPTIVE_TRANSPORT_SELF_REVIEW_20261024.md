# Same-assistant assessment: adaptive transport and differentiated clock

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**Scope: same-assistant assessment, not independent mathematical review.**
This audits [Note 16][note], its [exact/allowance checks][checks] and its
[floating theta pilot][pilot]. The analytical claims remain proved-in-note.
There is no certified finite onset, autonomous closure, evolved boundary
solution, specialist review or RH/endpoint-simplicity conclusion.

## 1. Source differentiation and the growing domain

The extension of Note 12's weighted source integrals through degree six
uses the same pointwise central and tail envelopes; it introduces no
uncontrolled theta truncation. The centered fourth-moment comparison
retains normalization and the change from the saddle L to the mean mu.
Its O(kappa^-9/4) allowance is sufficient, without a formal Edgeworth
expansion or a derivative of an asymptotic O term.

The exact covariance identities give
m3'=2mu(m4-3v^2)+m5-4vm3. In f_t-alpha z f_z, the cubic coefficient
is C3-3mu'v=m3'. Keeping this cancellation is what improves the earlier
crude growing-window velocity allowance from order kappa^-1 to
kappa^-7/6. The remainder is bounded from moments through degree six;
the derivative floor is explicit and eventually comparable to L.

The derivative comparison uses the complete mu-clock. It does not
replace mu'/mu by 2/kappa: with only the inherited variance allowance,
the height factor would make that replacement too expensive on
X~kappa^(1/3). There is no hidden upgrade from fixed labels to growing
labels; the X powers are displayed before the rate is taken.

## 2. Collars, poles, and regulator correlations

The fixed phase radius beta=1/4 is distinct from the much smaller
root-localization radius s/mu. With s<beta/2, the enlarged disks are
disjoint, contain exactly the same single real simple roots, and have
a nonvanishing boundary floor of order one. Both transverse and
horizontal buffers include the complete touched collars.

The logarithmic mass bound is O(kappa^-2), including the logarithm:
n=O(L), c=Theta(L), and log(kappa)/L stays bounded. This is an
improvement of an earlier sufficient allowance, not a correction to
the truth of Note 14's weaker result.

The quotient H_zz/H is not bounded across a zero. Its residue is the
actual velocity a'. Subtracting that residue gives a regular part
bounded by a circle estimate. The integrated pole term is proportional
to epsilon/M, not its square, and is retained explicitly in I_0.

The distributional current bridge has the sign
j-J_nu=(h2*w*(1-w)*partial_bar r-partial_bar(h2*w))/pi.
The circle residue supplies J_nu with the correct positive coefficient.
The derivative convention partial_bar=(partial_x+i partial_y)/2 and
current vector (Re j,Im j) are consistent with H_t=-H_zz and
a'=H_zz(a)/H_z(a). Stationary points where H_z=0 are not divided by.

The density bias is differentiated as an exact weak identity. The
new coefficients include grad r_t and Delta r_t, and the derivative
of w(1-w) is w_t(1-2w). The estimates preserve correlations before
taking absolute values. The linear-zero control has signed source
mass zero but absolute mass |r_t|/2; bounding the original source
pointwise and then integrating would miss that distinction.

## 3. Averaged evolution versus a reduced equation

AT26 bounds the current and density time derivative against the finite
moving lattice, with error O(L kappa^-7/6)=o(L/kappa). This follows
from root velocities, compact-kernel derivatives and the finite-epsilon
bridges. It is not obtained by differentiating static closeness.

AT27 separately pays the derivative of the lattice phase. Its allowance
grows with |x|. On fixed height ranges the continuum derivative is
accurate at o(L/kappa); on the entire growing window this estimate does
not justify discarding the lattice correction. It is a scoped limit
of the present comparison, not a universal obstruction to other kernels.

Neither the true differentiated potential covariance Q nor its
approximation error is bounded here. The moving lattice is an explicit
reference driven by complete source moments, not an independently
closed model. The mixed-sign boundary operator, source-fixed harmonic
data, outer-height transition, negative-time derivative budgets and
stability remain obligations for the full program.

## 4. Checks and computational limits

The standard-library checks give 16 zero polynomial residuals for the
new current/time identities on H=z^2-2t with four regulators, plus nine
exact moment identities on three rational discrete laws. A cleared
polynomial derivative verifies the radial primitive -s/(1+s)^2.
These controls include a polynomial with a double event; the local
simple-root hypotheses are explicitly inapplicable at that event.

The finite-allowance script uses upper/lower mean bounds consistently:
L+e in upper numerators and L-e in denominators, the larger collar
radius beta/(L-e), a conservative local population, and the lower
derivative floor. At t=10^4 the concentration/collar gate fails and no
downstream allowance is reported. At 10^6 and 10^9 the differentiated
clock allowances exceed L/kappa; the first sampled allowance below
that scale is at 10^12. This is floating evaluation, not a certified
threshold or monotonic-in-time assertion.

Six theta contour observations use the existing saddle-coordinate
source evaluator with eight modes. They refine source order/cutoff,
contour order and contour height. The current numerator subtracts its
constant analytic part before quadrature, using the centered source
covariance. This matters because the observed time derivatives are small.

The largest observed continuum derivative discrepancy is about 0.3143%
of the mean derivative mu'/pi. Retaining the finite clock reduces the
sample discrepancies to at most 1.923e-9 of that mean; the maximum
derivative refinement change is 3.991e-10, and several discrepancies
are below their own refinement changes. Do not treat those tiny values
as certified accuracy or a universal asymptotic rate. The observations
are of the zero measure, not finite-epsilon peaks. Their transfer to
the adaptive density comes from the analytical bounds.

No new literature theorem was imported. The complete-source inputs and
elementary contour arguments are identified in the note; the unresolved
high-height literature import remains unresolved.

## 5. Status and next work

The bounded adaptive forcing/current and differentiated-clock task is
complete at the stated eventual inner-window scope. HDA-02/04/05/06
advance but remain partial; HDA-07--09 stay gated. The maintained
fixed-epsilon manuscript is unchanged. New results remain in Note 16
until an explicit manuscript expansion.

Prioritize an audit of an actual covariance closure or a complete
outer-height estimate; retain independent review and certified finite
onset as separate verification tasks. Do not rerun the existing pilots
without a new question, changed formula or failed check.

[note]: ../notes/16_ADAPTIVE_FORCING_AND_DIFFERENTIATED_CLOCK_20261024.md
[checks]: ../numerics/ADAPTIVE_TRANSPORT_CHECKS_20261024.json
[pilot]: ../numerics/ADAPTIVE_TRANSPORT_THETA_PILOT_20261024.json
