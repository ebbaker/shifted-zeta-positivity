# Independent internal review of oscillatory blocks, paired forms, and an explicit height

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent configuration supplied for this review: **gpt-6-astra (Codex)**,
reasoning effort **ultra**. The reviewing subagent inherited that configuration.
This is an independent internal mathematical audit, not external refereeing or
formal proof verification. No shared repository files were edited by the reviewer.

## Scope and conclusion

Reviewed Notes 12, 16, 17, and 18 and the mathematical source drafts
integrated into [Note 19](../notes/19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md)
and [Note 20](../notes/20_EXPLICIT_OUTER_HEIGHT_BOUND_20261014.md).
The integrating agent corrected the reported TeX punctuation and added
self-contained statements, provenance and continuation links.

The substantive mathematical claims in those drafts pass this review:

1. The sufficient asymptotic outer threshold can be decreased from four
   to three, with an arbitrary fixed positive margin and a presently
   unspecified height cutoff.
2. The exact two-coordinate representation of both Laguerre forms has
   the stated coefficient and signs. Its direct tail bound pays all mixed
   omitted pairs and all fully omitted pairs.
3. For the separate condition `t log(x/(4 pi)) >= 5`, the explicit cutoff
   `X_1 = 4 pi exp(10^9)` is sufficient for normalized four-jet error below
   `1/8`, uniformly for `0 < t <= 1/2`.

None of these claims provides the remaining one-sided estimate through an
unknown positive-time collision. The explicit cutoff is not attached to the
new threshold three, and neither result fills the finite strip above height
104. The manuscript was not part of this continuation audit.

## 1. Oscillatory blocks and uniformity

The third derivative theorem was checked against the author's primary
article: Olivier Robert, *On van der Corput's k-th derivative test for
exponential sums*, Theorem 2 and preceding proof,
[author PDF, p. 8](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf),
[DOI](https://doi.org/10.1016/j.indag.2015.11.009).
Applied to `f(y)=-(T/(2 pi)) log y` on a subinterval of `(M,2M]`, it gives
an absolute bound proportional to
`T^(1/6) M^(1/2) + T^(-1/6) M`. The same bound holds for every terminal
partial sum, because the interval length can be shortened before applying
the derivative estimate. The draft's independent differencing derivation
also gives the stated two terms. There is no missing complete-block
assumption.

The remainder of the following audit concerns the new application rather
than a claim imported from that theorem. With `ell=log(u/(4 pi))`,
`theta=t ell`, and split `Y=exp(ell/3)`, the low-index discrepancy has
summable exponent

\[
 p=\tfrac12+\theta/6-\delta.
\]

For `theta >= 3+epsilon/2` and `delta <= epsilon/72`, this is at least
`1+epsilon/24+(theta-3-epsilon/2)/6`. Pulling the last exponent out using
`n>=2` leaves the bounded factor
`(theta_0+s) 2^(-s/6)`. This verifies uniformity when `theta` grows as well
as when it remains fixed. The ordinary zeta tail beyond `Y` is paid
absolutely, since `Re w >= 5/4`.

On each high-index interval, the amplitude with any fixed logarithmic
moment is decreasing once `ell` is large. The cancellation of the
`theta/4` terms in its logarithmic derivative is the reason this
monotonicity remains uniform. Exact Abel summation, applied to the maximal
partial-sum estimate, pays a shortened final interval at the actual floor
cutoff. The two exponential powers are

\[
 E_1=\tfrac16-\tfrac\theta4\beta(1-\beta)+\delta\beta,
 \qquad
 E_2=-\tfrac16+\tfrac\beta2
     -\tfrac\theta4\beta(1-\beta)+\delta\beta.
\]

For `1/3 <= beta <= 1/2`, the first is at most `-epsilon/48` under the
draft's assumptions. At `theta=3`, the second is a convex quadratic with
endpoint values `-1/6` and `-5/48`, leaving room for its stated `-1/16`
bound. The extension of the final endpoint beyond `1/2` is `O(1/(u ell))`;
its contribution remains harmless even when `theta <= ell/2`. The
`O(ell)` block count and fixed logarithmic powers are absorbed by the
strict exponential decay. Thus the asserted discrepancy is uniformly
`O_epsilon(1/L)` for the first four logarithmic moments.

The positive error sums in the effective Riemann--Siegel estimate do not
need oscillatory cancellation. Their weaker absolute bound by `O(u^(1/4))`
still gives `e_A+e_B=O(L^2 u^(-3/4))`. The complete remaining error is
`O(u^(-7/16))`. The gamma factors are comparable on discs of radius
`1/L`; the replacement by an analytic zeta carrier occurs before Cauchy
differentiation. These points suffice to transfer the approximation to all
four physical derivatives. The leading phase algebra then proves both
strict Laguerre signs and excludes first-pair zeros. The resulting
collision-sequence consequence is a limsup at most three, not a universal
finite cutoff at exactly three.

## 2. Staircase terms

For the exact common source, the moving upper index is retained. Direct
differentiation between jumps gives `B_r'=-t B_(r+1)`, while the jump at
`v=d_n=(log n)/2` has coefficient `(log n)^r A_n(d_n)`. Thus the stated
distributional formula has the correct delta coefficient, without an
extra Jacobian. On `v>0` the initial index `n=1` is a lower-endpoint term.

The formula

\[
 D'_j=-2t(v+ia)D_j-2itD_{j+1}+ijD_{j-1}
\]

follows from `d_n=v+ia+i q_n`. At each entering index,

\[
 K(d_n)A_n(d_n)(-a)^j=e^{-ta^2}(-a)^j\phi_n(ia).
\]

The `x` phases cancel exactly. Consequently one cannot give these jumps
an artificial oscillatory gain in `x`. The ordinary Abel identity is valid
for every real frequency; the quoted third derivative bound is to be used
under its stated hypothesis `|T|>=1`. These identities preserve the
source's geometry but are not signed lower bounds for the integrated
quadratic observation.

## 3. Paired Laguerre forms and tails

Let `I_k=integral W_alpha q_alpha^k`, where
`q_alpha=-a+i y_alpha` with the same frozen `a` for every coordinate.
The real-product identity
`Re A Re B = (1/2) Re(A conjugate(B)+AB)` and symmetrization give the
coefficient `1/4` in the paired Laguerre formula. Its two differences are

\[
 -\tfrac12(q_\alpha-\overline{q_\beta})^2
   =\tfrac12(y_\alpha+y_\beta)^2,
 \qquad
 -\tfrac12(q_\alpha-q_\beta)^2
   =\tfrac12(y_\alpha-y_\beta)^2.
\]

Conjugate exchange preserves the real Hermitian integral. These arguments
actually prove the identity for every nonnegative integer `j`; the
application requires only `j=0,1`. The source majorant in Note 16 has all
polynomial moments, so both double integrals converge absolutely before
symmetrization. The signs of their amplitude products remain unrestricted.
The signed two-atom control correctly exhibits negative total curvature
with positive diagonal contributions; it is expressly outside the theta
source class.

The paired residual coefficient is likewise `1/4`, with multiplier
`y_alpha^2+y_beta^2-2b^2`. Direct four-jet algebra gives exactly

\[
 \mathcal L_j-\mu h_j^2-h_jC_j
   =h_{j+1}(h_{j+1}+2ah_j).
\]

This vanishes on the genuine stationary condition, and requires payment
if only approximate stationarity is available.

For retained absolute masses `R_k` and omitted masses `T_k`, all defined
before multiplication by `exp(-ax)`, the direct pair-tail payment is

\[
 |\mathcal L_j-\mathcal L_j^A|
 \le e^{-2ax}
 \left(R_jT_{j+2}+R_{j+2}T_j+T_jT_{j+2}\right).
\]

It follows by adding the two nonnegative frequency squares, obtaining
`2(y_alpha^2+y_beta^2)`, and using `y_alpha^2<=|q_alpha|^2`. Integration
over the symmetric omitted-pair domain gives precisely the three terms
above, with no missing factor two. The integration and index bounds from
Notes 12 and 16 must consequently have their outside `exp(-ax)` factor
removed when used as bounds for `T_k`; the draft states this convention.
The intersection of omitted regions may be overpaid. Quadrature and
whole-cell parameter errors remain separate obligations.

As an additional reproducibility check, the reviewer inspected and reran
[pair/block driver](../numerics/check_signed_carrier_pair_identities.py). All **34** exact
rational sparse-polynomial and signed-atom checks passed. The independent replay was compared with the saved
[receipt](../numerics/SIGNED_CARRIER_PAIR_IDENTITY_CHECKS_20261014.json). This replay checks
finite identities, including the stationary ideal, quadratic-tail
expansions, exponent endpoint and convex-chord algebra, smooth staircase
recurrences through order three, and entry-phase cancellation. It is not an infinite-domain sign proof or an interval
quadrature certificate.

## 4. Explicit outer height

The imported expressions and branch matching were checked independently
against D. H. J. Polymath, Theorem 1.3,
[primary equations (13)--(24)](https://arxiv.org/html/1904.12438v2#S1).
In particular, the numerator of the exponential in (23) includes
`t^2 log^2(u/(4 pi n^2))/16 + 0.626`; the draft retains the constant
without adding a spurious factor of `t`. The complete correction in
(24), the gamma ratio, and the kappa bound are also retained.

Every displayed quantitative stage in the draft was checked. For
`L>=1000` and `tL>=5`, the disc has `Re w>=3/2`; the finite weighted
exponent is at least `17/16+s_0/8`. Integral comparison yields the
logarithmic-square constant `8720<9000`, from which the conservative
`31000/L` discrepancy follows, including the ordinary zeta tail. The
full positive error-weight sum is at most `85`; each imported error is
bounded as stated, with total at most `2/L`.

The microscopic-disc amplitude comparison costs less than `3`, and the
reciprocal zeta series gives `Gamma<=3|Q|`. These produce
`|H-A|<=560000|Q|/L`. The maximum Cauchy normalization factor for
`0<=k<=3` is `k! 4^k=384`, giving `107520000/L`.

The prime-power series bounds for the first three logarithmic zeta
derivatives are respectively `6`, `26`, and `158`. The chain-rule bounds
`7`, `33`, and `243` for the carrier logarithm follow. Exponential
recombination produces, at order three, the numerator
`21 omega^2+246 omega+1279`. Thus the carrier contributes at most
`100/L`. The total bound is

\[
 \frac{107520100}{L}<\frac{108000000}{L}.
\]

At `L>=10^9` this is below `0.108<1/8`. All intermediate elementary
inequalities hold on the larger domain `L>=1000`; the final threshold is
used only to obtain the small normalized error. This establishes the
explicit theorem and its quadratic lower bounds, without evaluating an
astronomically large exponential or assuming a physical norm gap.

The reviewer also inspected and independently reran
[constant driver](../numerics/check_explicit_outer_constants.py): all **52** exact
arithmetic and half-line polynomial checks passed. Its independent replay was compared with the saved
[receipt](../numerics/EXPLICIT_OUTER_CONSTANT_CHECKS_20261014.json). Nonnegative coefficients
after shifting `L=1000+y` certify the tested polynomial inequalities for
every real `L>=1000`. The driver explicitly does not verify the imported
theorem, the complex analytic arguments, or their reduction to these
polynomial bounds; those were assessed in the mathematical audit above.

Reviewed source hashes:

- Pair/block driver SHA-256: `3b429b096dabc20490f8f564f10b3bbfe40de10210078e6304d24c9d6a424e61`.
- Explicit-constant driver SHA-256: `0323d888f7e36c9233e92de5d24d6e81a4bc884defed2713842f6cac58fd856b`.

## Corrections and limits

No substantive mathematical correction was required in the reviewed
drafts. Minor TeX punctuation defects in the paired draft were reported
to the integrating agent. The integrated notes preserve the distinct status of the two outer
bounds, retain exact stationary conditions, and keep the finite certificate
through height 104 as the existing baseline.
An absolute truncation error, even an extremely small one, cannot be
divided by the unknown energy to manufacture a locally bounded loss at a
candidate collision. RH and the remaining inner region remain open.


## Integrated source identity

The integrating agent records the final note identities below; the detailed
check receipt also binds the drivers and replay records. Hashes identify
reviewed content and are not mathematical validation.

- `19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md`: `8c9f15a256c78671fabcf6b6df4465d615f5b4e1b45f889e35bb6a227c28b6ff`.
- `20_EXPLICIT_OUTER_HEIGHT_BOUND_20261014.md`: `efc35b4cbafad27aa74716230a46f6d29cf83b504a17c69010ff4ca300a4fb5c`.

See the [integration check receipt](../numerics/OSCILLATORY_CONTINUATION_CHECKS_20261014.json).

The independent reviewer subsequently reread both integrated notes and
confirmed these exact hashes. The final integration review found no
substantive regression or further correction.
