# RH pays the return-height cost of the translated prime notches

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded turn metadata. Separate same-model derivations and
[internal review][review]; no specialist review or novelty claim.

**Result.** For Note 09's fixed `d=2` or `d=3` prime-phase recurrence, RH forces

\[
\log X\le(2+o(1))\log\log R,
\qquad X=e^{2\pi\Delta}.                                    \tag{H1}
\]

Consequently its completely paid translated-sum and scalar-square kernels, at the stated heights `gamma` comparable with `R`, satisfy

\[
\boxed{U(\gamma)\ge\left(\frac d2-o(1)\right)
              \frac{L}{\log L},\qquad L=\log(\gamma/(2\pi)).} \tag{H2}
\]

Thus their respective leading lower constants are `1` and `3/2`, both larger than the existing Fejér constant `1/2`. This closes the previously unpaid return-height gate **for these constructions**. It does not reverse their small discrete-prime-payment examples, exclude unrestricted bandlimited kernels, or exclude any original multiple zero.

This continues [Note 09][n9] and the [research program][program]. The
[result index][results], [collision controls][controls] and [avoid index][avoid]
apply, particularly [scoped conclusions][a07] and [quantitative gain][a20].
The changed number is the necessary return height and its complete-envelope
coefficient. This is a proved conditional cost for a specified construction,
not another equivalent simplicity criterion.

## 1. The exact primary approximation and its range

[Granville–Soundararajan, *Extreme values of |zeta(1+it)|*, Lemma 2.1, PDF p.3](https://arxiv.org/pdf/math/0501232), has been checked in the primary PDF. Under RH, apply it with `sigma_0=1/2` and `sigma=1`. For `y>=e^4` and `t>=y+3`, its zero-free rectangle lies strictly to the right of the critical line and away from the pole. Its `sigma_1=1/2+1/log y` gives

\[
\log\zeta(1+it)
 =\sum_{n\le y}\frac{\Lambda(n)}{n^{1+it}\log n}
 +O\!\left(\frac{\log t\,(\log y)^2}{\sqrt y}\right).        \tag{H3}
\]

Only real parts are used below, so there is no logarithm-branch ambiguity. All multiplicities on the critical line are allowed. The statement is uniform in this declared range; no exceptional set of heights is removed. In particular, this uses Lemma 2.1, not the later almost-all-height Euler-product approximation.

Fix `delta>0`, put `t=dR`, and take

\[
y_0=(\log t)^{2+\delta/2},\qquad
y_1=(\log t)^{2+\delta}.                                    \tag{H4}
\]

For sufficiently large `t` both satisfy the source's height restriction. The error in (H3) at `y_0` is
`O_delta((log log t)^2/(log t)^(delta/4))=o(1)`, and the error at `y_1` is smaller. Subtracting the real parts of the two approximations gives

\[
\Re\sum_{y_0<n\le y_1}\frac{\Lambda(n)}{n^{1+it}\log n}
 =o_\delta(1).                                               \tag{H5}
\]

The higher prime-power part is uniformly negligible:

\[
\sum_{p^k>y_0,\ k\ge2}\frac1{k p^k}\ll y_0^{-1/2}.          \tag{H6}
\]

For `p>sqrt(y_0)` use the geometric tail starting at `k=2` and sum `O(p^-2)` over integers. For `p<=sqrt(y_0)`, start at the first power exceeding `y_0`; each resulting geometric tail is `O(1/y_0)`, and there are at most `sqrt(y_0)` such primes. Thus (H5) implies

\[
\Re\sum_{y_0<p\le y_1}\frac{p^{-it}}p=o_\delta(1),\qquad
\sum_{y_0<p\le y_1}\frac1p
 =\log\frac{2+\delta}{2+\delta/2}+o_\delta(1)>0.             \tag{H7}
\]

The second assertion is the ordinary reciprocal-prime Mertens asymptotic, also obtainable by partial summation from the PNT. Its positive limiting constant, rather than a subtraction on a vanishing scale, is what is used.

## 2. Tiny root-of-unity phase returns cannot precede this scale

Note 09 chooses `omega=e^(2pi i/d)` and returns satisfying

\[
|p^{-iR}-\omega|\le\epsilon_\Delta
\quad(p\le X),\qquad \epsilon_\Delta\longrightarrow0.        \tag{H8}
\]

Its actual accuracy `epsilon_Delta=1/[Delta^2(1+B_Delta)]` is more than sufficient. Raising unit complex numbers to the `d`th power gives

\[
|p^{-it}-1|\le d\epsilon_\Delta,\qquad
\Re p^{-it}\ge1-\frac{d^2\epsilon_\Delta^2}{2}.              \tag{H9}
\]

Suppose along a sequence that `X>=y_1`. Every prime in (H7) then satisfies (H9), so its weighted real sum has a strictly positive limiting lower bound. This contradicts (H7). There is no accumulated phase-error problem: the weighted prime sum on this shell tends to a fixed constant, and all higher powers have already been paid separately in (H6).

Therefore, for every fixed `delta>0`, sufficiently large returns satisfying (H8) have

\[
X<(\log(dR))^{2+\delta}.                                    \tag{H10}
\]

Because `d` is fixed, this is exactly (H1). In return-height language,
`R>=exp(X^(1/2-o(1)))`; equivalently, `log R>=exp((pi-o(1))Delta)`. This is an asymptotic lower bound on successful returns, not an asserted effective search bound or a construction of a return near that lower bound.

There is a useful quantitative phase corollary. From (H7), the weighted mean of `|p^(-it)-1|^2` tends to two. Hence

\[
\max_{y_0<p\le y_1}|p^{-it}-1|\ge\sqrt2-o_\delta(1).        \tag{H11}
\]

More directly in the original root phase, with any fixed `omega^d=1`,

\[
\boxed{\max_{y_0<p\le y_1}|p^{-iR}-\omega|
 \ge2\sin\frac{\pi}{4d}-o_{d,\delta}(1).}                   \tag{H12}
\]

Indeed a fixed smaller chord distance puts every relative angle strictly inside `(-pi/(2d),pi/(2d))`, forcing `Re(p^(-idR))` to be uniformly positive and contradicting (H7). For `d=2` and `d=3` the constants are respectively `2 sin(pi/8)` and `2 sin(pi/12)`. This statement concerns the specific logarithmic prime shell (H4), not every prime or every kernel.

## 3. Consequence for the two kernel constructions and their full budgets

In Note 09, the translated sum has `I=d/(Delta D_R)`, with `D_R->1`; its scalar-square version has `I=d/Delta+o(1/Delta)`. The already proved gamma and pole budgets hold for `gamma in [4dR,8dR]`, including a choice of an actual zero ordinate in that interval. Thus for either allowed complete upper envelope,

\[
U(\gamma)\ge(1-o(1))\frac{LI}{2\pi}
 =\left(\frac d{2\pi}-o(1)\right)\frac L\Delta.             \tag{H13}
\]

Here `C(h)>=0`, and exact pole retention is covered by its paid negative-part budget. No negative pole term is silently discarded.

Since these heights are comparable with `R`, one has `log log(dR)=log L+o(1)`. Equations (H1) and `log X=2pi Delta` give

\[
\Delta\le\left(\frac1\pi+o(1)\right)\log L.
\]

Substitution into (H13) proves (H2). The conclusion is a lower bound, with no claim that these constants are attained. The same recurrence which made prime payment small has forced the target height sufficiently high that the mass term alone costs more than the Fejér comparison.

**Scope.** The translated-sum and scalar-square constructions from Note 09 still demonstrate `C(h)->1` at `I Delta->2` (from below for the translated sum) and `C(h)->0` at `I Delta->3`; their prime-payment counterexamples remain correct. What is now paid is the specific phase-return height in their complete envelope. No lower bound for arbitrary signed Fourier samples, arbitrary nonnegative bandlimited kernels, or all possible translation patterns follows. The proof uses RH only through the checked short-log-zeta approximation and never imports simplicity.


## 4. A sharper necessary return scale from the same estimate

For a modest second-order refinement, put \(\ell=\log\log t\) and choose
\(y_0=A(\log t)^2\ell^6,\ y_1=2y_0\), where \(A\) is fixed sufficiently
large. Equation (H3) at these two cutoffs, together with (H6), gives
\[
\left|\Re\sum_{y_0<p\le2y_0}\frac{p^{-it}}p\right|
\le\frac{C A^{-1/2}+o(1)}{\ell}.
\]
Here one may choose \(C\) independently of fixed \(A\), since
\(\log y_0/\ell\to2\); the threshold may depend on \(A\). PNT and partial
summation on the positive dyadic shell give
\[
\sum_{y_0<p\le2y_0}\frac1p
=\frac{\log2+o(1)}{2\ell}.
\]
Choose \(A\) so that \(C A^{-1/2}<(\log2)/4\). If \(X\ge2y_0\), (H9)
contradicts these two estimates for sufficiently large returns. Thus
\[
\boxed{\log X\le2\log\log(dR)+6\log\log\log(dR)+O(1).}       \tag{H14}
\]
The constant is not numerically specified. This does not construct a
return at that scale or change the leading coefficient \(d/2\).
The sharper limiting chord constant in (H12) remains attached to its
original shell (H4); the fixed-\(A\) dyadic argument has only small,
not vanishing, relative error.

## 5. Control and acceptance boundary

This argument concerns the unchanged zeta prime phases at arbitrary large
heights. It makes no event-exclusion claim for the quadratic, atomic,
heat-polynomial, Euler-factor, weighted-square, reflected or
positive-primitive controls in the linked catalogue and opening notes.
Their local collision geometry is not a premise of the shell estimate.
Applying (H3) to a modified arithmetic object would require its own exact
coefficients and error statement; the unchanged \(\Lambda(n)\) identity
cannot simply be assigned to it. In particular, neither Note 09's
arithmetic control nor Note 05's completion-preserving control acquires
the other's preservation list.

The small prime payments in Note 09 remain valid. What fails is their
proposed use to improve the complete height envelope under uniform
root-of-unity alignment. Actual-height signed estimates, partial or
nonuniform phase alignment, other translation patterns and other kernels
remain outside this conclusion. RHS-02's opposing arithmetic estimate,
the strict cap surplus and all-zero coverage remain open.

**Subsequent broader result:** [Note 11][n11] proves the sharp leading
one-half floor for the complete absolute-prime envelope of every
admissible nonnegative bandlimited kernel, with the same explicit gamma
and pole budgets. It uses a different full-tail argument and does not
erase this note's stronger d/2 comparison for the aligned-copy family.
Signed arithmetic and kernels without those complete budgets remain
outside that theorem.

[n11]: 11_FULL_ABSOLUTE_PRIME_ENVELOPE_AND_LOGARITHMIC_SPREAD_20261020.md

[review]: ../reviews/10_PRIME_PHASE_RETURN_HEIGHT_REVIEW_20261020.md
[n9]: 09_ARITHMETIC_CONTROLS_TRANSLATED_KERNELS_AND_STABLE_EXTRACTION_20261020.md
[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
