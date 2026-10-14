# Internal review: uniform outer-region signs and threshold four

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Independent reviewing agent; the reviewer did not author Note 17, its
analytic derivation, or the diagnostic checker. Parent-verified inherited
configuration: **gpt-6-astra (Codex)**, reasoning effort **ultra**.

**Assessment:** the reviewed argument establishes the stated qualitative,
uniform outer-region proposition from the cited effective approximation.
For every fixed positive epsilon and sufficiently large height depending
on epsilon, both full Laguerre forms are strictly positive when
`0<t<=1/2` and `t log(x/(4pi))>=4+epsilon`. The shared four-jet
asymptotic and balanced norm estimate are supported by the proof. No
numerical value of the height cutoff, inner-region estimate, or RH
conclusion follows. There is no priority assessment or novelty claim.

## Bound versions and replay

| Reviewed file | SHA-256 |
|---|---|
| `17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md` | `5a1d79e1c57ba0a928b9971a0c220fb0b9d90c116138686c2a0e235f5acc7f4f` |
| `analytic_findings.md` (staged derivation) | `acae098b6d4c2bb3934d1596b56252fb319a53190001e5326d9761ff7cf6a344` |
| `check_outer_cusp_and_phase_obstructions.py` | `9f6a7a141ca78fd45244de45972ca062b05162ead0f2f5b940a87ebf8176808d` |
| `check_shifted_contour_payments.py` (imported diagnostic source) | `b6f0114e1a4de2e1848f20ab0ab2f1022d9b55015184a879ae0c0536a62d6ad6` |
| `OUTER_CUSP_AND_PHASE_OBSTRUCTION_CHECKS_20261014.json` | `ec7e5d13c87ba31c7f288912ac558f3ab0ede07d5626f01d994e2ab460ea0870` |

The reviewer read the primary
[Polymath Theorem 1.3 and its definitions and error bounds](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem3)
directly, independently reconstructed the reduction, and checked the
added geometric and diagnostic claims. The following assessment is
analytic internal review, not proof-assistant verification or an external
referee report.

The diagnostic checker was independently rerun with the bundled Python
runtime and python-flint. It returned **PASS**. The independent record
`/tmp/inv21-global/OUTER_CUSP_INDEPENDENT_REPLAY_20261014.json` has SHA-256
`5298965b9869bf6e1756f89347817f8a201aa6b4b1a4525ac673ed45458dffb6`.
It agrees with the producer record in every field except elapsed time.
Those finite checks do not prove the uniform asymptotic proposition;
that proposition rests on the argument reviewed below.

## Exact model and the uniform weighted-sum estimate

The normalization of `M_0` is correct for `H_0=xi/8`. The two-branch
finite approximation is exactly the imported theorem's expression:
its first exponent is `w_-`, and its second exponent after including
the numerator `n^v` is `conjugate(s_*)+kappa-v=w_+`. There is no
missing factor of two or change of gamma normalization. Both branches
of `M_t` and alpha are analytic on the small discs used in the proof,
and reflection interchanges the two branches.

The threshold calculation is correct. Write `L_u=log(u/(4pi))` and
`theta_u=t L_u`. For a retained index, the positive heat weight is
bounded by changing the Dirichlet exponent from approximately
`1/2+theta_u/4` to `1/2+theta_u/8`, because
`log N<=L_u/2+O(1/u)`. The small imaginary coordinate and elementary
alpha errors can be absorbed into a nonnegative quantity tending to
zero uniformly on the disc of radius `1/L`.

The crucial uniformity issue is handled explicitly in (10)--(12).
Putting `theta_0=4+epsilon/2` and `s=theta_u-theta_0>=0` gives an
effective exponent at least `1+epsilon/32+s/8`. Consequently

\[
\frac{t}{4}\sum_{n\ge2}(\log n)^2 n^{-p}
\le \frac{D_\varepsilon}{4L_u}
       (\theta_0+s)2^{-s/8}=O_\varepsilon(L^{-1}).
\]

This remains valid when theta grows with height and time stays as large
as one half. A proof that replaced the sum only by a fixed convergent
zeta moment and then used `t<=1/2` would not establish the necessary
`1/L` factor; the reviewed proof avoids that error. The omitted ordinary
zeta tail is uniformly `O(x^(-1/8))` using the deliberately weaker
bound `Re w>=5/4`, so it is also absorbed in `O(1/L)`.

The constant four is therefore a sufficient boundary for this absolute
summability argument. Nothing in this step proves that four is optimal
or intrinsic to the heat family.

## Imported errors, analytic discs, and four derivatives

On the upper half-disc, the factors multiplying the weighted sums in
the imported `e_A+e_B` estimate are uniformly bounded. In particular,
`N^|kappa|` stays bounded; the factor `n^v` is paid by the lower real
part corresponding to the other branch. The exponential error multiplier
is `O((1+theta_u^2)/u)`, hence at most `O(L^2/x)`. The remaining
`e_(C,0)` estimate is `O_epsilon(x^(-1/2))` in this region. All three
imported errors are retained. The proof does not silently replace a
value approximation by a derivative approximation.

The disc radius `1/L` is essential to the particular argument. The
logarithmic derivative of each `M_t(s_±(z))` is `O(L)` uniformly in
`0<t<=1/2`; integrating it over this radius makes each branch magnitude
comparable to its magnitude at the real center by fixed factors.
Using a fixed-radius disc without additional gamma normalization would
not justify this comparison.

The analytic model `A_t=Q_++Q_-` is defined with full zeta functions.
Pointwise application of the imported finite-sum theorem, followed by
the uniform replacement of each finite sum, bounds `H_t-A_t` even at
locations where the finite cutoff changes. The function being
differentiated is holomorphic, with no finite cutoff in its definition.
Schwarz symmetry of both terms extends the upper-half-disc estimate
to the lower half-disc. Thus Cauchy's derivative bounds apply on the
whole circle without differentiating a jump or assuming an unstated
negative-imaginary-part version of the imported theorem.

Nonvanishing of `Q` is obtained independently of the physical norm:
`Re w>=5/4` puts both zeta and its reciprocal in an absolutely
convergent Dirichlet-series half-plane. This gives upper and positive
lower bounds for `|zeta(w)|`. The resulting derivative error is
`O_epsilon,k(|Q| L^(k-1))`, including `O(|Q|/L)` for `k=0`.

Direct differentiation of the analytic carrier gives
`(log Q_+)'=iL/4+O(1)` and bounded second and third logarithmic
derivatives. The gamma contributions use the stated derivatives of
alpha; the fixed zeta logarithmic derivatives are uniformly bounded
in `Re w>=5/4`. This proves the required common four-jet expansion.
No time derivative is taken in this step: time is held fixed, so the
shrinking disc and the lower bound on `tL` do not create an extra
differentiation term.

## Phase-independent strict signs

The common phase is preserved through all four jets. After scaling,
the leading vector is `(c,-s,-c,s)` with `c^2+s^2=1`. The two quadratic
forms and the balanced norm therefore have leading value one,
uniformly even when individual leading jets vanish. This establishes
both full Laguerre inequalities, not merely their stationary restrictions.

The explicit perturbation constants in Section 7 are correct. With
each coordinate error bounded by delta, retain the nonnegative error
square and pay the single mixed quadratic error by `delta^2`. Each
Laguerre form is at least `1-4delta-delta^2`; the balanced norm is at
least `1-4delta`. At `delta=1/8` these are respectively `31/64` and
`1/2`. The diagnostic checker independently expands the three relevant
polynomials exactly. This algebra gives a concrete target for a future
effective cutoff, but the analytic constants required to calculate that
cutoff have not yet been supplied.

The octonionic conclusions follow from the previously established
identities `A_j=2u L_j`. Positivity of the time-oriented associator is
asserted only on the genuine stationary union, where the corresponding
energy identity applies. The note correctly avoids claiming that the
energy derivative is positive at every point of the outer region.

## Finite diagnostics and the remaining target

The diagnostic definitions and Hermitian projection identity were
checked independently. Each shared arithmetic sum is a finite,
exactly specified integrand object; its floor cutoff is certified by
inequalities. The numerical record rigorously finds negative
phase-independent margins at the two stated points, and a negative
quadratic form even for the actual carrier phase at `x=4898.7`.
This rules out a proof requiring that particular pointwise integrand
form to be nonnegative there. It does not determine the Laguerre form
after integration, which includes further cross-coordinate terms.

The staircase jump identity is correct: the carrier's phase cancels
the factor `exp(-i x d_n)` when the channel enters at `v=d_n`, and
the remaining heat factor is `exp(-t a^2)`. All twelve recorded
four-jet jump comparisons pass. The checker also evaluates four
complete time-zero jets through an Acb series for the completed zeta
function and two heated points with both complete source tails paid.
These are selected-point diagnostics, not coverage or asymptotic tests.
Their convention `theta=t log x` is explicitly distinguished from the
theorem's convention and places the obstructions outside its domain.

The close-pair polynomial control and its residual formula are correct.
It demonstrates that a small two-component residual norm can require
large payments even when the necessary one-sided stationary loss is
zero. The proposed one-sided target (27) remains exactly equivalent to
the needed stationary bounded-loss inequality, with all source errors
still payable.

One defect was found in a separate geometric working draft: a local
Hermite positivity discussion could not be extended to simple
time-zero roots at its second stationary level. The example
`H(t,y)=(1-6t)y+y^3` shows the problem. That discussion was not
incorporated into Note 17, so the defect does not affect the version
bound above. Minor display-formatting defects in the appended section
were corrected before the final hash was bound.

For each fixed epsilon, the proof leaves a finite transition region up
to its unspecified `X_epsilon`, and the entire high-height inner region
`t log(|x|/(4pi))<4+epsilon`. It does not replace the older localization
constant by exactly four at every finite height. The valid asymptotic
consequence is the stated limsup bound for any unbounded sequence of
candidate positive-time joint zeros. The existing certified finite
baseline through height 104 is unchanged. Completing the inner-region
signed estimate and making any desired finite transition cutoff
effective remain separate tasks.
