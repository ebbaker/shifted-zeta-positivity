# Heat-scale trace and control comparison review

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. **Same-assistant self-review only**; no
independent model or specialist validation.

**Assessment:** [Note 22][note] completes the first bounded HMC-05
comparison. It gives a quantitative complete-source error around the
heat-scale tube profile, including an explicit all-multiplicity outer
formula. The leading profile is common to matching analytic controls.
This closes the selected leading-profile discriminator, while HMC-05's
separating theta estimate and HMC-06 remain open.

The review follows the [result index][results], [local heat summary][heat],
[control register][controls] and [avoid index][avoid]. The conclusion is
an estimate and a scoped control comparison; it is not a new equivalent
simplicity criterion supported by finite examples.

## 1. Source, normalization and root membership

The scale is \(\tau=\sqrt{2t}\), not \(\sqrt t\). With
\(a_m=H^{(m)}(0,a_0)/m!\), the normalized leading polynomial is
the monic probabilists' \(\operatorname{He}_m\). The source generating
function and the independently rechecked primary Polymath/DLMF
normalizations agree. The bound in HT2 controls complex heat parameter
\(w^2/2\) and complex displacement \(wz\) on the full polydisk.
Its majorant is \(e^{R^2u^2/2+R(Y+1)u}\Phi(u)\); both infinite tails
are covered by Note 21's stated formulas with the substituted parameters.

Cauchy's coefficient estimate gives
\(M\tau/[|a_m|R^{m+1}(1-\tau/R)]\), so the factor two in HT2
is valid for \(\tau\le R/2\). The extra unit disk in the spatial
variable supplies the \(j!\) derivative factors. The event's exact
vanishing derivatives, rather than small individual source summands,
remove the lower powers. The leading derivative normalization remains a
material event-dependent input; the estimate is not uniform in height
or multiplicity and does not certify an actual theta event.

HT12's sign changes and derivative bounds isolate each actual endpoint
and the critical point. Its middle-interval minimum excludes intervening
zeros. Thus the selected pair is an actual adjacent cap, not merely two
formal roots. The argument retains the complete field, including every
other member of a higher-order birth cluster.

## 2. Physical phase measure and finite error

The identity
\[
\frac{\tau(p'^2-pp'')}{p'^2+\tau^2p^2}\,dy
=\frac{-\tau(p'/p)'}{\tau^2+(p'/p)^2}\,dy
\]
preserves the physical denominator exactly. It does not substitute the
rescaled jet \(H+i\tau H_x\). Under RH the complete real-root sum
gives \(-s'\ge8/d_*^2\), keeping the other cluster and exterior
contributions. The full change of variables has mass \(\pi\).

The integrated displacement bound HT7 has the logarithmic term with
coefficient \(\tau/\kappa\), and tail allowance \(2\tau/\kappa\).
There is no extra factor of \(\pi\) in that displacement integral.
The central value comparison in HT15 does have a factor \(\pi\),
because it is a constant integrated against this measure.

The derivative of the Hermitian numerator simplifies to
\(\operatorname{Re}(p'\overline{p''}-p\overline{p'''})\).
This verifies the Lipschitz constant \(K\) and avoids an unnecessary
three-term absolute payment. The finite difference \(\Delta\) controls
both the averaged numerator and the real Laguerre denominator.
\(l_0>0\) is a minimum of a known fixed Hermite polynomial expression,
and is not a disguised positive floor for physical \(H^2+H_x^2\) at
the original event. The displayed constants therefore give the claimed
uniform \(O(\tau\log(1/\tau))\) estimate for bounded \(r\).

The local analytic extension is separate from the global root argument.
From \(L_\tau\ge l\) and \(|p_\tau|\le N_0\), it uses
\(\kappa=l/N_0^2\), which remains positive as \(\tau\to0\).
Consequently the same local profile applies to analytic collision controls
without an all-real heat slice. HT5's complete-root constant is not used
for those controls. This distinction is explicit in the final note.

## 3. Profile and multiplicity audit

At a critical point, \(P''=-mP\), hence the profile denominator is
\(mP(\nu_i)^2\). The transverse average is
\((2r)^{-1}\partial_r|P(\nu_i+ir)|^2\), so the double profile is
\(1+r^2\). In the alternative convention \(\eta=c\sqrt t\), its
residual is \(\pi c^2/2+o(1)\). This agrees with Note 21's lower
witness and is a sharper asymptotic, not a change of normalization.

The finite-product coefficients in \(|P(\nu_i+ir)|^2\) are strictly
positive. The coefficient \((4m-2-\nu_i^2)/6\) follows by differentiating
the Hermite equation, not by extrapolating a numerical table.

For the outer profile, the Gaussian quadrature weights are
\((m-1)!/P(\nu_i)^2\). Reducing the shifted polynomial at roots of
\(\operatorname{He}_{m-1}\) leaves only degrees at most \(m-2\),
so quadrature exactly preserves the required squared norm. The constant
and second-order shift terms combine in the same Hermite degree and must
be retained together. Differentiation gives
\[
\sum_i\Gamma_{m,i}(r)=(m-1)+
\sum_{j=1}^{m-1}\binom m{j+1}\frac{r^{2j}}{j!}
=L_{m-1}^{(1)}(-r^2)-1.
\]
The physical outer baseline is \((m-1)\pi\), so its residual is
\(\pi[L_{m-1}^{(1)}(-r^2)-m]\), not the expression with minus one.
The proof covers each fixed finite \(m\); no uniform large-\(m\)
error constant is asserted.

The thickness equivalence HT21 is restricted to bounded
\(r(t)=\eta(t)/\sqrt{2t}\). Uniformity of HT15 and the positive
quadratic coefficient prove both directions. It is not extended to
unbounded \(r(t)\), and a thinning tube does not regularize its
endpoint into a nonvanishing contour.

## 4. Controls, verification and research decision

The positive atomic, Euler-factor and close positive endpoint controls
share the double profile. Their failed premises are explicitly the
unchanged theta expansion/completion/arithmetic, not the generic heat
or phase identities. Weighted-square, finite-prime, reflected and
positive-primitive controls use the local analytic extension with their
own constants; no full all-real spectrum is assigned to them.
The close-source moment comparison does not claim comparable event
derivatives or a uniform time threshold.

The scoped negative result concerns decisions using only these common
leading profiles. It does not rule out a source-specific bound below the
conditional profile or an estimate of a nonuniversal correction. Such a
bound would require new arithmetic information. No such estimate has
been proved in this round.

The [exact replay][script] passed for the frozen degrees two through
eight. It computes individual profiles in rational polynomial quotient
rings and checks the outer identity against its separately written
orthogonality proof. It also checks rational phase-measure fixtures.
The [receipt][replay] binds the script and helper hashes. This is finite
algebra, not a theta numerical certificate or evidence for universal
asymptotic quantifiers. No specialist review or priority claim follows.

No unresolved discrepancy remains in this bounded self-review. Record
the improved finite error and the failed leading-profile discriminator;
keep HMC-05 open and HMC-06 gated. The next bounded question is the first
surviving nonuniversal correction after subtracting this profile, including
its control response. An identity for that correction alone will not meet
HMC-05's separating-estimate requirement. The manuscript is unchanged;
no commit, tag or draft snapshot was created.

[note]: ../notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md
[script]: ../numerics/check_hmc_endpoint_trace_algebra.py
[replay]: ../numerics/HMC_ENDPOINT_TRACE_ALGEBRA_REPLAY_20261021.json
[results]: ../../../../../../../result-summaries/README.md
[heat]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
