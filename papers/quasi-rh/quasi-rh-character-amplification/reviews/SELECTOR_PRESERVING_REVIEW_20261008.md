# Scoped review of the selector-preserving continuation

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

This review checks the new sector reductions and their stated source
hypotheses. It is a same-model parallel critique, not independent specialist
refereeing or formal verification. The imported September 30 preprint
remains assumed; its consulted PDF has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
No Lean proof was replayed.

## Plain-ratio conductor reduction

Reviewed the complete note
[SELECTOR_PRESERVING_PLAIN_CONDUCTOR_20261008.md](../notes/SELECTOR_PRESERVING_PLAIN_CONDUCTOR_20261008.md).
The weighted expansion and adaptive total-conductor cutoff pass this
scoped check. No mathematical correction was required.

The key distinction is correct: expand only the plain factor, retaining

\[
w(u)=1_{\mathcal C_+}(u)|M_r(u)Q_I(u)|^2\ge0.
\]

The marked inverse input bounds its total mass by
`U^(1+epsilon) H^A`. The restricted weighted plain-ratio kernel has
modulus at most this mass, with all numerator zeros and the canceled-phase
mask preserved before taking absolute values. Applying the elementary
ideal-pair count at column scale `N` gives `N V^(1/2+epsilon)` pairs;
the original `N^(-1)` normalization cancels `N`. Thus the low plain-ratio
block has absolute size `O(U^(1+epsilon) V^(1/2+epsilon) H^A)`.
The proof does not require smoothness of the selected physical rows.

This absolute estimate is for each already-assembled weighted plain
kernel. It is not an absolute estimate for the individual inverse/prime
tuples. The note observes this distinction and does not insert a total
conductor truncation into `w`.

The final direct proof removes the entire low plain-ratio block, including
the diagonal, before expanding the inverse and prime variables. It then
removes small total conductor only in the complementary plain sector.
This gives three disjoint error contributions: low primitive row
conductor, low plain-ratio conductor on the retained rows, and low total
conductor among the remaining pairs. The high plain-ratio condition
already implies `k != k'` because its cutoff is at least one.

Let `eta=1/5000` and `gamma=1/6250`. The choices

\[
v_{\rm pl}=2\delta m-2(\eta+\gamma),\qquad
\tau_0=2\delta(m+23/20)-1/4-2(\eta+\gamma)
\]

satisfy exactly

\[
1+v_{\rm pl}/2=K-\gamma,
\qquad (9/8-23\delta/20)+\tau_0/2=K-\gamma.
\]

Both are increasing in `delta,m` on the box. Exact rational endpoint
checks give

\[
v_{\rm pl}\in[3231/12500,5241/12500],\qquad
\tau_0\in[2614/3125,14191/12500].
\]

In particular, the total cutoff uniformly exceeds `4/5`. Its upper
endpoint exceeding one is not a defect: the ratio conductor belongs to
two total columns and is not bounded by the physical row norm.

The optional intersection correction comparing with the old retained sum
is exact. The off-diagonal low plain-ratio block equals its high
total-ratio portion plus its low total-ratio portion.
The latter has the existing **absolute tuple majorant** for small total
conductor; adding a further plain-pair restriction only reduces that
majorant. Subtracting the intersection therefore justifies the removal
inside the old retained sum without invoking positivity for a truncated
inverse norm. Equivalently, one may remove low plain conductor first,
then low total conductor restricted to the complementary plain sector.

The remaining tuple sum has the actual original coefficient array and
both zero masks. Its regions are invariant under swapping the two
tuples, and the summands conjugate under that swap, so the complete sum
is real. The reduction to it retains the old error exponent
`K-1/6250`. Positivity of the original full norm controls the negative
part of the retained sum, but does not make its individual summands
positive. A whole-sum modulus bound is consequently equivalent at the
target scale; a sum of individual tuple moduli remains a stronger demand.

The note's derivative-profile discussion is appropriately limited to
fixed permitted parameters followed by the source's positive-norm
Sobolev step. A row-dependent family of unrelated coefficients would
not have the displayed kernel. The conductor regions and physical row
selector must be fixed during each coefficient identity; no differentiation
of a sharp arithmetic selector is authorized.

## Status retained

These are conditional sector bounds. They leave a signed correlation
with both plain and total ratio conductors large. They do not prove the
uniform `1/5000` mixed saving or establish a new zero-free boundary.
The sparse-cofactor calculation in the separate subcase note is also
only a conditional subcase: no decomposition of the full plain annulus
into such sparse families with controlled total cost has been supplied.

## Manuscript additions reviewed

Reviewed the saved manuscript sections `sec:two-ratios` and
`sec:mixed-subcase` against the research notes and source statements.
The two-ratio theorem retains precisely the original three analytic
hypotheses. Its proof removes low primitive row conductor, then the
complete low plain-ratio block, then low total conductor in the remaining
sector. Its cutoff exponents, normalizations, real-symmetry claim and
unchanged `1/6250` error margin agree with the checked note.

The upper-band proposition explicitly requires additional inputs. The
source application uses the original physical ray-class prime sums and
smooth annuli, the mesh for Lemma 18.1, and the imported global theorem
to permit `kappa=3/4`. Source (13.1) and the logarithmic-derivative
arguments in Sections 18.2 and 19.1 do not authorize arbitrary subsets
of primes merely because the retained coefficients are finite-ray
combinations. The manuscript's alternative formulation, stipulating
the fourth norm and the pointwise envelopes, avoids that ambiguity.

The positive Cauchy factorization is exact, including when any character
factor vanishes. Both enlarged norms are nonnegative before enlargement.
The high primitive-conductor condition excludes the source's fixed
exceptional family for all sufficiently large row scales. The fourth
norm has two plain lengths equal to `m` and capacity
`2m+(9/2)z_J <= 1`; its zero-slot case is separate and valid.

For whole-slot selection loss at most `1/1000`, the exact minimum ideal
gain on `m >= 21/50` is `1/1000`, the maximum selection loss in the
energy exponent is `21/100000`, and subtracting the required saving
`1/5000` leaves `59/100000`. Adding the low primitive-conductor part
reduces the guaranteed full-moment margin to `1/6250`, as stated.

One wording clarification was requested and verified in the saved
manuscript: source physical inputs provide the required derivative-family
uniformity, whereas stipulating the displayed fixed-profile bounds alone
does not. The abstract alternative now explicitly requires the bounds for
the derivative profiles as well before using the rowwise Sobolev argument.
This does not change the fixed-parameter proposition or its exponent.

The separate `selector_audit` agent independently checked the upper-band
note's amended source hypotheses, fixed-subset factorization, exceptional
character exclusion, common-orientation handling and whole-slot bound.
That same-model cross-review found no mathematical correction; the
conservative `59/100000` margin is valid. This provides a separate check
of the derivation, not independent specialist validation.

## Count-sensitive bounds and the application wedge

Reviewed
[SELECTOR_ENERGY_LOCALIZATION_20261008.md](../notes/SELECTOR_ENERGY_LOCALIZATION_20261008.md)
and ran `numerics/check_selector_energy.py` successfully. The note's two
count-sensitive energy bounds follow from its explicit pointwise
envelopes, row count, and fourth moment. Their combination with the
fixed-subset estimate gives exactly the four sufficient savings displayed
there. Source support and derivative-family caveats remain necessary;
neither is inferred from arbitrary bounded prime coefficients.

The sharper full-bin exponent `R*` may be used before selecting the
current witness pair, as stated in the manuscript. For
`h=(1-R*)/delta`, the derivative signs in the note imply that `h`
increases with both parameters on the hard box. Its minimum and the
resulting saving for `7/10 <= r <= 701/1000` agree with the exact
rational check. The proof uses that this lower saving is positive before
multiplying by the lower bound on `delta`; there is no hidden reversal
of an inequality with a negative factor.

The rebalance identities give old inverse count `R_new+eta` at `r_new`
and old plain count `R_new` at `m_new`. Their negative slopes and the
detector support `r+m >= t_new` therefore leave precisely the ideal
triangle

\[
0<r-r_{\rm new}<\frac\eta{\delta(1-x)},\qquad
0<m_{\rm new}-m\le r-r_{\rm new}.
\]

The taper `eta-delta(1-x)(r-r_new)` is the exact sufficient ideal
mixed saving there. This reasoning localizes the mixed estimate needed
for the application; it does not estimate the full mixed norm at every
point outside the triangle. The actual selected-slot amplitude and its
rounding losses are separately retained in the note's count budget.

The simplified formulas for `r_new,m_new` and their derivative signs
were checked. For the derivative of `m_new` in `delta`, the cleared
numerator is

\[
\alpha P_x\delta^2(1-x)/2
-\eta(\alpha P_x\delta+aJ).
\]

The positive and negative terms are bounded respectively below by
`21/1000` and above by `53/250000`, so the sign argument has a large
fixed margin. The derivative in `x` is also positive. These analytic
monotonicity arguments justify using the corner values as continuous
extrema; the script's finite corner assertions alone would not do so.
The ranges checked are

\[
r_{\rm new}\in[47749/67660,10261670/14086891],\quad
m_{\rm new}\in[3470383/8566666,28646/69475],\quad
w\in[1/1071,1/900].
\]

Finally, the operational outer buffer follows directly from adding one
loss budget `ell` to each old count exponent and allowing support
`r+m >= t_new-ell`. Its lower and upper bounds, including coefficients
`39/14`, `50/9`, and `25/14`, follow from the stated positive slope
lower bounds. A theorem only on the zero-loss sharp triangle would not
be sufficient for the actual annular application; the note correctly
requires the buffered domain and all profile/height uniformity.

## Final saved-source confirmation

The final read of manuscript subsection `sec:application-wedge` confirms
the checked rebalance identities, ideal triangle, exact location and width
ranges, tapered saving and operational outer buffer. Its wording correctly
distinguishes localization of a sufficient count application from a bound
for the full mixed norm everywhere outside that domain. It also states
that the leading wedge is disjoint from the proved upper plain-length
band and that the required mixed estimate there remains open.

The final remaining-question and dependency sections now refer to
`T_joint`, both ratio-conductor restrictions, the partial upper-band
proposition and its additional inputs, and the smaller buffered
application region. The derivative-family clarification above is present.
No outstanding mathematical or quantifier correction remains within this
review's stated scope. Native compilation and the final build hash are
recorded separately by the coordinating agent; this review does not claim
rendered-page inspection or independent validation of the imported source.
## Parent build and reproducibility record

The final saved manuscript compiled successfully with the built-in
desktop LaTeX compiler on 8 October 2026. The existing source and editor
were retained. This records compilation, not a rendered-page visual
inspection or an exported PDF.

Both `check_selector_preserving.py` and `check_selector_energy.py` pass
and reproduce their saved JSON records byte-for-byte. The former checks
the adaptive conductor and upper-band identities and 32,788 finite
character/mask identities; the latter checks the exact energy and
application-domain algebra with the stated continuous sign arguments.
Neither computation establishes the remaining arithmetic cancellation.
The source has 89 unique labels and 99 resolved `ref`/`eqref` uses.
Local links in the updated indexes and selector notes resolve.

Final manuscript SHA-256:
`81d1b7ecc02d15469577eec34b8b21cef41a6f6f874aafc153afd29b692ab3dd`.
No commit, tag, replacement manuscript, or third-party PDF was created.
