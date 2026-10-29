# CTF-E08 R7: assessment of the fixed cosine jet proof

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 **chat0027**, **Assess CTF-E08 R7 proof**.

**Verdict: accepted without mathematical correction at the single frozen
mark (T,A)=(1/4,2), within the inherited prepared whole-space solution
class.** All seven obligations in the [R7 packet][packet] pass. [Note55][n55]
proves a supporting jet-energy gain; it supplies no independent compression
bound, collision-deadline payment or enlarged physical domain.

This is a separate-chat, different-model internal assessment of
Astra/max's proof and [same-assistant check29][r29]. Three read-only
Sol subagents checked, respectively, the moment/preparation argument,
energy/residual accounting, and control scopes. They did not edit files
or capture histories. These checks share inherited premises, including
Sol's Note40, and are neither specialist independence nor formal proof
verification. The parent checked the displayed argument and owns this
verdict. Model and effort were read from this turn's session metadata.

## 1. Complete-source moment bound — pass

The canonical summand is exactly
\[
q_n=\pi n^2e^{5u}(x-3)e^{-x/2+u^2/4},\qquad x=2\pi n^2e^{4u}>6.
\]
With x'=4x, differentiation gives
\[
\ell_n'=9+\frac{12}{x-3}-2x+\frac u2,
\qquad \ell_n''=\frac12-8x-\frac{48x}{(x-3)^2}.
\]
For y=x-6>=0, multiplication of the proposed lower bound by (x-3)^2
gives exactly 8y^3+21(y-1)^2+24. Hence ell_n''<=-149/2<-74.
The function 9+12/(x-3)-2x is decreasing, so pi>25/8 implies
ell_n'(0)<=5/26<1/5. Thus every mode satisfies
q_n'<=(1/5-74u)q_n, and their sum satisfies the same first-derivative
inequality. No claim about log concavity of a mixture is needed.

The elementary pi bound in Note55 is valid: integrate
1-t^2+t^4-t^6 below 1/(1+t^2) at 1/2 and 1/3, then use the arctangent
addition formula. The two polynomial integrals sum to more than 25/32.
The exponential series gives 8/3<e<11/4; for example the tail after
1+1+1/2+1/6 is at most 5/96. These imply all exponential comparisons
used in the Gaussian test below.

On compact u-intervals, differentiation of the complete sum is justified
by its Gaussian n-tail. Factoring out the n=1 exponential bounds q and
q' by constants times, respectively,
e^(9u+u^2/4-pi e^(4u)) and
(1+u)e^(13u+u^2/4-pi e^(4u)). Therefore the weighted derivatives are
integrable, all stated moments are finite, and u^3q vanishes at both
endpoints. Integration gives
\[
74M_4\le3M_2+\tfrac15 M_3
\le3M_2+\tfrac15\sqrt{M_2M_4}.
\]
For z>=1/24, 74z-sqrt(z)/5 is increasing and is greater than 3 at
1/24. Since M2>0, this proves the strict M4/M2<1/24 with all modes retained.

## 2. Literal cosine and preparation order — pass

The actual raw fields obey
\[
2F_2-F_1=\rho u\{\sin(2u)-2u\cos(2u)\}.
\]
The exact identity sin(x)-x cos(x)=integral_0^x t sin(t) dt gives the
bound |sin(x)-x cos(x)|<=|x|^3/3. Therefore
|2F2-F1|<=(8/3)rho u^4. The radial Jacobian
4pi r^2 rho dr=q du and Young's convolution inequality give
\[
\|C_0\|_2\le c_K\tfrac83M_4\le c_K\tfrac19M_2,
\qquad c_K=\|K_1\|_2=(8\pi)^{-3/4}.
\]
Here C0=S(2F2-F1). Multiplication occurs before the one unit of
preparation, and J2,s=-P_s^p S(u^2 F0). Neither a multiplier on the
prepared U nor a derivative of the feedback path is substituted.

## 3. Prepared Gaussian denominator and entire tail — pass

Self-adjointness, K1*K1=K2 and r^2=e^(4u) give exactly
\[
\langle J_{2,0},K_1\rangle=-(8\pi)^{-3/2}I,\qquad
I=\int_0^\infty u^2q(u)e^{-e^{4u}/8}\cos(2u)\,du.
\]
The three input intervals pay all signs: the weight is at least 1/6
on [0,1/2], nonnegative on [1/2,3/4], and at least -1/4 on [3/4,infinity).
The first assertion uses cos(2u)>=1/2 and e^2<8; the second uses
3/2<pi/2; the third uses e^3>16 and e^2>4. In particular the last
interval is not discarded. Its moment payment is
\[
I\ge\tfrac16M_2-
\left(\tfrac23+\tfrac49\right)M_4
\ge\frac{13}{108}M_2>0.
\]
Dividing the inner product bound by ||K1||2 gives
||J2,0||2>=c_K(13/108)M2. The prepared norm ratio is consequently
(1/9)/(13/108)=12/13, as stated. Q0>0 follows as well.
These input-u partitions create no spatial boundary in the flow.

## 4. Fixed-path propagation and energy crossing — pass

With the mark and alpha path fixed, C=2J2-V solves the common
homogeneous equation. On every compact lifespan interval the inherited
regularity permits whole-space integration by parts, giving
\[
\frac d{ds}\|C\|_2^2=-2\|\nabla C\|_2^2+
\alpha\int d|C|^2\le6\alpha\|C\|_2^2.
\]
The same estimate applies to J2. Since alpha>=0, E=E0 and
X=Q0 exp(6B),
\[
Q\le\min\left\{X,
\left(\frac{\sqrt{E_0}}2+\frac6{13}\sqrt X\right)^2\right\}.
\]
Young's weaker bound is E0/2+(72/169)X. The sharper allowance divided
by X tends algebraically to 36/169. The two constants describe different
allowances; there is no factor-of-two correction.

The sharper allowance is less than X exactly when
\[
X>\frac{169}{196}E_0
\quad\Longleftrightarrow\quad
B>B_c=\frac16\log\frac{169E_0}{196Q_0}.
\]
Initially ||V0||2>=2||J2,0||2-||C0||2>=(14/13)||J2,0||2.
The raw F0 is nonzero and heat convolution is injective, so U0!=0;
thus E0>(196/169)Q0 and Bc>0. No assertion that the trajectory reaches
Bc, or that the ratio describes actual energies, is required.

## 5. Same-path jet forcing and exterior consumer — pass

At A=2, Theta=(2V,V+2J2)=(2V,2V+C). Both stated triangle allowances
are valid:
\[
\mathcal T_{\rm gen}=4E_0+(\sqrt{E_0}+2\sqrt X)^2,
\quad
\mathcal T_{\rm corr}=4E_0+(2\sqrt{E_0}+\tfrac{12}{13}\sqrt X)^2.
\]
Their comparison reduces to sqrt(E0)<(14/13)sqrt(X), so the strict
crossing is exactly the same Bc. The baseline is already sharper than
the coarser Young allowance 6E0+8X in [Note47][n47].

Note47 retains (12/625)alpha||Theta||^2 on r>=2. Replacing that
restricted norm by min(Tgen,Tcorr) is legitimate, and the stated saving
against the same whole-space Tgen payment is exactly
(12/625)alpha(Tgen-Tcorr)_+. This does not lower the compact R5
coefficient 274/25+B1+B0: the inner-region maximum remains payable,
and a whole-space substitution can lose localization. No improved
allowance for the complete functional, G or alpha is proved here.

## 6. Residual, boundaries and direct comparison — pass

The supporting C is not the source residual. [Notes31][n31] and
[40][n40] retain the nonzero initial preparation commutator on
(F0,F1), and
R_s=L_s R+[A_T,L_s]W. The full second-order commutator, derivatives
of the exact cutoff, source multiplication, and all inner-ball energies
remain. At r=1, R=-Theta, so the combined numerator Theta+R still
cancels. Nonzero residual does not mean nonzero trace at every mark.
No singular quotient is split by the new estimate.

The direct comparison is also correct. Integrating cos(x)>=1-x^2/2
gives sin(x)>=x-x^3/6 for x>=0; hence
\[
-H_a(1/4,2)\ge2M_2-\tfrac43M_4\ge\frac{35}{18}M_2>0.
\]
This uses the same moment budget before auxiliary evolution. The
accepted gain is a numerical-constant milestone under [avoid01][a01],
not a new regularity criterion, collision-free domain, or dynamical
separator. Both improved and original allowances retain positive
exp(6B) growth. **The improved allowance remains compatible with B
tending to infinity at a finite endpoint.** This observation concerns
the displayed upper bounds; it is not a theta blowup theorem or a
universal exclusion of signed methods.

## 7. Control premises and scopes — pass

The [registered controls][controls] screen the actual sufficient
premises, following [avoid02][a02] and [avoid07][a07].

| Control | Checked premise and limit of the conclusion |
| --- | --- |
| R6 fixed-amplitude polynomial kernels | For x=Au the general raw combination is rho u[x K''(x)-K'(x)], not the literal sine/cosine expression. A finite cosine prefix gives no global remainder payment. The trigonometric identity itself is valid; it is its application to these kernels that fails. Some kernels can satisfy the final norm inequality, so none are excluded collectively. |
| Gaussian-polynomial cosine | q=(64u^4+6)e^(-4u^2). Gaussian moments give M2=21 sqrt(pi)/32 and M4=123 sqrt(pi)/256; M4/M2=41/56>1/24. The quantitative moment premise fails; the registered event A=2 sqrt(6) is outside R7's mark. This does not establish failure of every correlation inequality. |
| Positive weighted-square | Fixed nonnegative weights preserve the per-mode first-derivative inequality and hence the same moment bound at T=1/4. Full canonical coefficients/reflection are absent, but this sufficient input is shared. The registered events near 44.13 and 83.53 are not A=2. |
| Finite-prime orbit | Canonical full source/reflection are not fixed. No moment failure is asserted, and its high-gap events do not give an event at this mark. |
| Reflected super-Gaussian | Canonical amplitude fails; its registered pi/4 event is elsewhere. No R7 moment ratio has been acquired. |
| Smooth shape / positive primitive | Canonical source fails. Shape and primitive conditions alone do not supply the required quantitative ratio; no unmeasured failure is asserted. |
| Euler-factor | Shifted source/conductor differs. No R7 moment evaluation or automatic double event is inferred from its Laguerre witnesses. |
| Atomic/profile / continuous compact | Atomic inputs are outside the imported source-function theorem. Admitted continuous prepared sources may share the sufficient moment test. |
| RH-conditional endpoint | Preserve RH conditionality, altered arithmetic and escaping heights. No moment evaluation or fixed-mark witness is supplied. |

This is a premise audit against existing evidence, not a new numerical
replay. In particular the moment class is broader than theta; the proof
is not an all-height arithmetic discriminator.

## Disposition and file identity

All **eleven** frozen input hashes in the packet matched at intake.
Their full values remain in the packet; the final recheck is recorded
in [Return57][return]. Note55, Review29, the issued packet and prior
evidence are preserved. In particular the unchanged TeX hashes are:

- Main manuscript: c9934699f8ca3ed840f3031259c2cf14a081c73e51ca73de18c3eeefd3df62f9.
- Companion: b954e99f992ff44fafc2745661257e2d5ce730360c3f9292862b195469f95abb.

No proof repair, source acquisition, numerical campaign, new candidate,
mark extension, manuscript edit or compilation was needed. Hash matches
establish input identity only. The [result index][results], especially
[spatial-flow results][theta-results], and [avoid index][avoid], especially
[quantitative utility][a20], retain their stated evidence standards.

**E08 R7 complete; B02 R7 proved in-note and assessed; parent B02 partial.**
[Progress05][progress] owns live status. **Next: [B] CTF-B02 — Astra**,
select one bounded route to independent compression control under
[Continuation58][next]. No further candidate is selected by this review;
E03/B03 remain gated.

[packet]: ../research-progress/handoffs/CTF-E08_COSINE_JET_CORRELATION_ASSESSMENT_REQUEST_R7_20261029.md
[n55]: ../notes/55_COSINE_JET_CORRELATION_B02_R7_20261029.md
[r29]: 29_COSINE_JET_CORRELATION_B02_R7_SELF_ASSESSMENT_20261029.md
[n31]: ../notes/31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
[n40]: ../notes/40_WEIGHTED_RESIDUAL_CLOSURE_E07_R1_RETURN_20261029.md
[n47]: ../notes/47_EXTERIOR_SOURCE_RESIDUAL_COUPLING_B02_R5_20261029.md
[return]: ../notes/57_COSINE_JET_CORRELATION_E08_R7_RESEARCH_RETURN_20261029.md
[next]: ../notes/58_COMPRESSION_CONTROL_AND_MODEL_CONTINUATION_20261029.md
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[theta-results]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../avoid/20_volume_without_a_gain.md
