# Contributing-agent review of the forest coefficient filter

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Separate same-model mathematical review; not independent specialist or cross-model review.

Reviewed [HDC Note 11](../notes/11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md), **Forest polynomial and gap-free filtered-spectrum enclosure**, after the Section 5 alternative-allowance correction. **No blocking issue remains in the reviewed finite theorem.** The coefficient-to-filter estimate is a real additional finite interface: it can enclose the scalar continuation on a neighborhood containing a double collision without an internal separation floor. It does not supply a canonical theta coefficient bound or a new simplicity conclusion.

## 1. Algebra and error theorem

The incidence-matrix derivation of the forest factor \(m(F)=\prod_C|C|\) is correct. A cyclic edge set has dependent incidence columns; a forest's nonzero maximal minors delete exactly one row per tree component, leaving \(\prod_C|C|\) choices. Multiplication by one discriminant clears each forest denominator. Relabeling makes the resulting polynomial symmetric, and the integer symmetric-polynomial reduction gives a genuine polynomial in the prepared coefficients.

The coefficient majorant in (6) bounds each monomial difference by its exact expansion at the reference. With \(|D_*|>E_D\), the ratio estimate follows without actual root matching or a discriminant floor. Combining \(K=G-q_*D\) before the coefficientwise estimate correctly preserves cancellation; its majorant is no larger than the separately combined majorants. The quotient and its error bound concern the scalar trace, not the norm of a potentially nonnormal complex resolvent.

One issue was identified and repaired during review. The nested cubic estimate based on \(B=b^2-3c\) can be **smaller** than the previously defined raw coefficientwise majorant, especially at \(B_*=0\). It must therefore be an alternative valid allowance for the actual variation, not an asserted upper bound on that particular functional. The revised \(E_D^{\rm alt}\), \(E_K^{\rm alt}\) notation and permission to take minima are correct.

The derivative in \(G=a\partial_aD\) holds coefficient/time data fixed. It is not a total derivative along \(a=4t\); the revised note consistently preserves this distinction.

## 2. Collision conditioning has a precise boundary

For real root multisets and fixed \(a>0\), the forest formula gives the exact dichotomy

\[
 D>0\quad\Longleftrightarrow\quad
 \text{every root multiplicity is at most two}.
\]

If a cluster has at least three coincident roots, a surviving forest would have to contain every zero-distance edge inside that cluster, which forces a cycle. If every cluster has size at most two, the forest consisting of all double-pair edges is a matching with strictly positive complement factors; all other terms are nonnegative. Thus simultaneous separated doubles genuinely lie within the polynomial-denominator method's possible domain. A triple does not, even though a restricted real limit of the scalar filter can be finite.

The stated nonextension example at a triple is decisive. For the centered cubic \(P=z^3+pz+r\),

\[
 D=-4p^3-27r^2+18ap^2-18a^2p,
 \qquad G=18ap^2-36a^2p.
\]

At fixed \(a\ne0\), \(r=0,p\to0^-\) gives \(G/D\to2\), whereas \(p=0,r\to0\), \(r\ne0\), gives \(G/D=0\). The latter split roots are complex and form an equilateral configuration. Therefore no continuous extension exists on a full complex coefficient neighborhood. This does not contradict continuity within the restricted real-rooted cone or a directional Hermite heat limit.

The supporting agent's **restricted real cubic extension** is correct and gives that distinction quantitatively. For a real-rooted cubic, \(B=b^2-3c\ge0\) and \(0\le\Delta\le4B^3/27\). For \(B>0\), division by \(B\) gives

\[
 q=\frac{2aB+12a^2}{\Delta/B+2aB+6a^2},\qquad
 \frac{2\kappa+12}{4\kappa^2/27+2\kappa+6}
 \le q\le\frac{2\kappa+12}{2\kappa+6},\quad\kappa=B/a,
\]

with \(a>0\). The reduced denominator is at least \(6a^2\), and both bounds tend to 2 as \(B\to0\) at fixed \(a\). This defines a continuous real-cone value at the triple without a discriminant floor. It assumes real-rootedness independently and gives no holomorphic complex extension. Its floor still degenerates if \(a=4t\to0\), so it is compatible with the physical heat-scale costs below.

For two doubles at distinct sites \(\pm b\), the mandatory matching and four possible extra cross edges give exactly
\(D=4a^2(2b)^8+16a^3(2b)^6\), agreeing with (16). The fixed-\(a\) continuation and the \(a=4t\to0\) heat-birth limit are different limits and should not be interchanged.

## 3. Negative time still has genuine resolvent poles

The quadratic pole at a noncollision is correctly retained. A useful higher-order exact check is the shifted triple heat polynomial

\[
 P_s(\tau,z)=z^3-6(\tau+s)z,\qquad s>0,\qquad a=4\tau.
\]

Its forest denominator is

\[
 D=864(\tau+s)(2\tau+s)(3\tau+s),
 \qquad
 q=\frac{\tau}{2\tau+s}+\frac{2\tau}{3\tau+s}.
\]

The resolvent poles occur at \(-s/2\) and \(-s/3\), where the roots are still distinct and real. The actual triple collision is at \(-s\). The factor \(\tau+s\) cancels from this **particular time-path quotient**, whose collision limit is 2; it does not cancel from the general coefficient-space rational function. This is exactly why a denominator floor, an explicit justified cancellation, or another local chart is still necessary on a complex/negative contour.

## 4. Sharp heat-scale precision and the valid rescaling

For an isolated \(m\)-fold heat birth, \(J=m(m-1)/2\), the exact Hermite calculation gives

\[
 D(t,4t)=(2t)^J\left(\prod_{j=1}^m j^j\right)m!,
 \qquad q\longrightarrow m-H_m.
\]

This agrees with the double and triple constants, including \(D_3(t,4t)=5184t^3\). An absolute denominator and residual budget must be controlled on this scale. That is not a universal obstruction: after the declared change \(z=z_0+\sqrt{2t}\,y\), both numerator and denominator carry the same factor \((2t)^J\), and the normalized Hermite denominator is nonzero. The finite ratio theorem is uniformly conditioned in a sufficiently small fixed normalized coefficient neighborhood.

The physical coefficient error of degree index \(j\) is then divided by \((2t)^{j/2}\). This scaling is substantive. At a fixed declared \(t>0\), compare the cubic snapshots

\[
 P_*=z^3-6tz,\qquad P=z^3-6tz+4t^{3/2},\qquad a=4t.
\]

Both have distinct real roots at that slice. Their discriminants are \(864t^3\) and \(432t^3\). The numerator stays \(6048t^3\), while the denominator changes from \(5184t^3\) to \(4752t^3\); hence

\[
 q_* = 7/6,\qquad q=14/11,\qquad q-q_*=7/66.
\]

An absolute constant-coefficient error tending to zero like \(t^{3/2}\) can therefore produce a fixed filter error. This is a finite coefficient-conditioning control, not an assertion about endpoint reality or a single time-varying perturbation source. Each chosen snapshot can be realized by a heat polynomial with that constant coefficient frozen for the comparison.

The note's shrinking-wall qualification is also correct: for a reference unit with nonzero finite limit, a wall of radius \(R\sqrt{2t}\) on which the normalized Hermite polynomial has a floor has unnormalized field scale \(t^{m/2}\). A fixed small relative wall error needs a sufficiently small constant times that absolute scale; a vanishing relative error needs little-o of it. Normalization does not supply this source accuracy.

## 5. Assessment

The revised note preserves the distinction between a finite scalar error theorem, a directional collision model and an independently acquired canonical-source bound. Its double-collision neighborhood demonstrates a genuine advantage over mandatory root disks for this scalar consumer. Higher collisions, complex resolvent poles, heat-scale source accuracy and growing-rank conditioning remain paid conditions or open applications. No additional change is required for the reviewed finite claims.

## 6. Separate contributing-agent control derivation and replay

23 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Separate same-model control derivation and exact-arithmetic replay; no specialist review, cross-model independence or theta acquisition is claimed.

**Disposition: the stated finite forest identities, double-collision enclosures and restricted real cubic bounds pass.** The useful controls are incorporated into Note 11; no duplicate standalone research note was saved.

One copy of the discriminant clears every denominator because a forest contains each edge at most once. Multiplying the forest expansion leaves a symmetric polynomial in the roots. For fixed a>0 and real repeated root locations, its denominator D is positive exactly when every multiplicity is at most two: a forest can contain all zero-gap edges precisely in that case. Thus the coefficient estimator has a real finite advantage at isolated or simultaneous doubles, but a triple requires another argument.

The cubic formulas are

D=Delta+2aB^2+6a^2B,   aD_a=2aB^2+12a^2B,   B=b^2-3c.

For a real-rooted cubic, 0<=Delta<=4B^3/27. Dividing by B>0 gives the stated sandwich in kappa=B/a. Its lower bound decreases because the derivative numerator is

-(8/27)kappa^2-(32/9)kappa-12<0.

At kappa=1/10 the lower endpoint is exactly **8235/4186**. Consequently 0<=B<=a/10 implies 8235/4186<=q<=2, with q=2 at B=0 understood only as the continuous extension within the real-rooted cone. It is not a holomorphic coefficient-neighborhood extension: the complex path z^3-r^3 has q=0, while the real Hermite path tends to 2 at fixed a.

For P=z^3-6tz+eta t^(3/2) and a=4t,

q=6048/(5184-27eta^2).

Real-rootedness requires |eta|<=sqrt(32). The range is then 7/6<=q<=7/5. A fixed nonzero normalized constant perturbation therefore changes the limiting filter by a nonvanishing amount. Sufficient small-error claims should refer to **centered/depressed coefficients**: o(t) in the linear coefficient and o(t^(3/2)) in the constant coefficient preserve the resolved Hermite shape. For an uncentered cubic, centering must also be controlled; raw lower-coefficient errors alone are insufficient. These are sufficient precision conditions, not an assertion that every possible correlated estimator requires them separately.

The quadratic coefficient disk |p|<=a/8 has |D|>=3a/2 and |q-1|<=1/3 without an internal root separation or discriminant floor. Its real interval -a/8<=p<=0 gives 4/5<=q<=1. This is a valid bounded spectral enclosure across a double, and **does not pass q<1/2 or establish simplicity**.

The final replay is **219 exact rational assertions, PASS**, using Python's standard-library Fraction. It enumerates all labeled forests for N=2,...,5 (2,7,38,291 forests), checks 36 actual matrix evaluations over 12 root configurations, cubic formulas, repeated-cluster denominator behavior, double coefficient-ball constants, simultaneous-double formulas, Hermite resultant discriminants through degree seven, rational-root Hermite matrix cases, the heat-scale cubic perturbation and the complex equilateral control. The [script](../numerics/05_check_forest_filter_20261023.py) and [record](../numerics/05_FOREST_FILTER_CHECKS_20261023.json) are saved with the investigation. The script emits JSON to stdout by default; writing a file requires explicit `--output` or shell redirection. These checks validate finite algebra and constants; the analytic proofs establish the parameter-range claims. They provide no evidence for an unacquired theta upper estimate.
