# VCD-E16 r1 — Fourier error after finite midpoint calibration

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded task dispatch **gpt-6.1-sol / ultra**.
Separate runtime model and effort attestation unavailable.

**Complete, proved in-note.** This is a conditional approximation estimate
for the [frozen E16 request][request] from [B04 decision 09][decision].
All four input hashes match. The proof uses the fixed-time integrability
in [E04][e04], the midpoint normalization in [E13][e13], and the classical
maximum-modulus principle checked in the [reference catalog][reference].
The [result index][results], [coefficient cluster][cluster],
[avoid index][avoid], and patterns [01][a01], [02][a02], and [07][a07]
govern classification and control scope.

## 1. Source, calibration and repeated zeros

At \(\lambda=0\), let \(Z_0=\int_{\mathbb R}\Phi(u)\,du\) and
\(d\mu=\Phi(u)\,du/Z_0\) for the complete canonical even source.
Use the literal normalized Fourier readout
\[
 F(w)=\int_{\mathbb R} e^{iwu}\,d\mu(u)=2H_0(w)/Z_0,\qquad F(0)=1.
\]
Take real even \(h\in L^\infty(\mu)\) with \(\|h\|_\infty\le\eta\),
where \(\eta\ge0\), and put
\(\delta F(w)=\int_{\mathbb R} h(u)e^{iwu}\,d\mu(u)\).
Assume \(\int u^k h\,d\mu=0\) for \(0\le k\le2L\), with integer \(L\ge0\).
The zeroth match preserves total mass, so \(\delta F=F_{(1+h)\mu}-F\)
in the probability normalization whenever \((1+h)\mu\) is nonnegative.
The estimate below also applies when \((1+h)\mu\) is signed.

Fix \(z_*=x+iy\) with \(xy\ne0\), put \(a=z_*/2\), and assume
\(\delta F^{(j)}(a)=0\) for \(0\le j\le r\), with integer \(r\ge0\).
Whenever the comparison is between probability sources, this condition
follows from the corresponding \(c_0\) jet matches at \(z_*\).
Indeed \(q_0=1\) on either source and E13 gives
\(c_0(z)=F(z/2)\), hence
\(\delta c_0^{(j)}(z_*)=2^{-j}\delta F^{(j)}(a)\).

For bounded complex \(w\), the differentiated integrands are dominated
by constants times \(|u|^j e^{M|u|}\), integrable for every \(j\) and
finite \(M\) by the canonical exponential moments. Thus \(\delta F\)
is entire and its derivatives can be taken under the integral.
Evenness gives \(\delta F(-w)=\delta F(w)\). Reality of \(h\) then
gives \(\delta F(\bar w)=\overline{\delta F(w)}\).
The moment matches give zeros of the derivatives through order \(2L\)
at \(0\), and the odd derivative at order \(2L+1\) also vanishes.
Consequently the zero at \(0\) has order at least \(2L+2\).
The matching jet and the two symmetries give zeros of order at
least \(r+1\) at each member of
\(\mathcal A=\{a,-a,\bar a,-\bar a\}\).
The four members are distinct and nonzero because \(xy\ne0\).
If \(\delta F\) is identically zero, all the ensuing bounds hold directly.

## 2. Disk estimate and moment-series alternative

For real \(\rho>|z_*|\) and \(|v|<\rho\), put
\[
 B_{\rho,v}(w)=\frac{\rho(w-v)}{\rho^2-\bar v w}.
\]
The denominator is nonzero on \(|w|\le\rho\).
The identity
\[
 |\rho^2-\bar v w|^2-\rho^2|w-v|^2
    =(\rho^2-|v|^2)(\rho^2-|w|^2)
\]
proves \(|B_{\rho,v}(w)|=1\) on the boundary and
\(|B_{\rho,v}(w)|<1\) in the disk. Its only zero there is the
simple zero at \(v\). The entire perturbation obeys the boundary
growth estimate
\[
 |\delta F(w)|\le\eta\int_{\mathbb R} e^{-(\Im w)u}\,d\mu(u)
      =\eta\int_{\mathbb R}\cosh((\Im w)u)\,d\mu(u)
      \le \eta F(i\rho),\qquad |w|\le\rho .
\]
The last inequality follows from monotonicity of \(\cosh(s)\)
for \(s\ge0\) and \(|\Im w|\le\rho\).

Define \(P(w)=(w/\rho)^{2L+2}\prod_{v\in\mathcal A}
B_{\rho,v}(w)^{r+1}\). The known zero orders make every
singularity of \(\delta F/P\) removable on the disk.
The resulting function is holomorphic in the disk and continuous on
its closure, where \(|P|=1\) on the boundary. The maximum-modulus
principle applied to this quotient gives the finite Blaschke-factor
bound
\[
 |\delta F(w)|
 \le \eta F(i\rho)
      \left(\frac{|w|}{\rho}\right)^{2L+2}
      \prod_{v\in\mathcal A}|B_{\rho,v}(w)|^{r+1},
 \qquad |w|<\rho .                                               \tag{1}
\]
The bound is continuous and gives equality at each of the specified
zeros. This uses the classical bounded-domain boundary form of the
principle. [NIST DLMF §1.10(v)][dlmf]

At the target \(w=z_*\), let
\(\theta_\rho(z_*)=\prod_{v\in\mathcal A}|B_{\rho,v}(z_*)|\).
All four factors are positive since \(|z_*|=2|a|>|v|\), and
each is strictly less than one, so \(0<\theta_\rho(z_*)<1\).
The disk bound from moments alone, with the same \(\rho\) and
\(\eta\), comes from dividing only by \((w/\rho)^{2L+2}\).
Equation (1) multiplies that allowance at \(z_*\) by
\(\theta_\rho(z_*)^{r+1}\). At fixed \(z_*,\rho,\eta\), each
increment of \(r\) multiplies the allowance by \(\theta_\rho(z_*)\)
and each increment of \(L\) multiplies it by \((|z_*|/\rho)^2\).
For increasing height or increasing \(\rho\), the prefactor
\(F(i\rho)\) must be included in any rate calculation.

Independently, evenness and expansion of the exponential give
\[
 |\delta F(w)|
 \le \eta\sum_{p\ge L+1}\frac{|w|^{2p}m_{2p}}{(2p)!},
 \qquad m_{2p}=\int_{\mathbb R}u^{2p}\,d\mu(u).                    \tag{2}
\]
Absolute summability under the integral follows from the exponential
moments, and the terms \(p=0,\ldots,L\) vanish by the moment matches.
One can take the minimum of (1) and (2) on the disk. The geometric
comparison above uses only the moment-only version of (1).

## 3. Attainable radius and scope

Consider any set of perturbations obeying these same fixed
calibrations and the common tolerance \(\|h\|_\infty\le\eta\).
Every Fourier displacement at \(z_*\) lies in the closed disk
centered at zero with radius given by (1) there, or the smaller
of (1) and (2). Any centered attainable disk therefore has radius
at most that allowance. If its retained amplitudes also agree
at \(z_*\), the same bound applies to the displacement of the
omitted midpoint sum \(R_N\) by E13.

In the [E12 construction][e12], for its fixed data and
\(x\ne0,\ 0<|y|<4\), the two real parameter directions map linearly
onto complex displacements. For any fixed \(\eta>0\), one can
also restrict the E12 parameter ball to radius at most \(\eta/K_0\),
where \(K_0=\|h_1\|_\infty+\|h_2\|_\infty>0\) for its two test
directions. The restricted ball still has positive radius and all
its displacements satisfy (1). Thus local freedom at each finite
calibration is compatible with a geometrically decreasing upper
allowance as the calibrations increase. At fixed \(z_*,\rho,\eta\),
that upper decay precludes a positive lower radius uniform in an
increasing calibration order. The derivation of (1) starts directly
from the stipulated zero orders.

The upper bound uses relative source tolerance, evenness, the
moment matches, and the calibrated \(c_0\) jet. Neither the bounded
score symbol \(b\) nor its matrix entries, canonical arithmetic,
the other midpoint amplitudes, or the finite tail tests enter it.
The exact \(c_0(z)=F(z/2)\) is full-chain data, as E13 shows.
A closure application still needs a source model with the stated
tolerance and matches, and a lower Fourier or model modulus with the
required separation from the error allowance. The centered disk
gives a magnitude bound with all phases allowed and yields no
zero-free claim.

The interpolation argument applies to every even base probability with
the relevant exponential moments under the same matched relative
perturbation hypotheses. The [collision catalog][catalog] and
[E13 screen][e13screen] therefore distinguish this bound from a
theta-specific condition. The known examples have these scope limits.

| Control | Premise comparison |
| --- | --- |
| Euler-factor translates | For a positive shift \(d\), the shifted summand has ratio \(\Phi(u-d)/\Phi(u)\to\infty\) by the first-mode exponential tails, so the bounded relative tolerance fails. Their normalized time-zero second moment also changes, failing that match when \(L\ge1\). |
| Weighted-square and finite-prime orbit controls | Full canonical reflection fails. The generic Fourier bound is available on a common even base with the required tolerance and calibrations. Their certified collisions do not test these particular midpoint derivative matches. |
| Reflected super-Gaussian and smooth shape or positive-primitive controls | The super-Gaussian fails canonical exponential confinement. The smooth shape and primitive controls lack the square-summand formula. Their exponential moments suffice for the generic argument with their own base. |
| Positive finite square changes, including E07 | E07 preserves selected finite moments and score data in its class, where the inherited nonreal-zero theorem applies and full smooth reflection fails. Its checked data do not include these midpoint jets. |
| E10 and E12 smooth compact multipliers | The constant-coefficient canonical square representation fails in the stated absolutely convergent class. E10 allows the next defect to vary. E12 allows complex midpoint displacement, subject to the bound above when the same tolerances and calibrations hold. Their Fourier zero locations remain open. |
| Atoms and finite-profile controls | Atoms and compact triangular extensions fail positive full-line density. Their own compact base measures provide exponential moments for the generic Fourier estimate. |
| RH-conditional endpoint controls | Ordinary Dirichlet arithmetic and the unchanged theta source fail. Their zero conclusions retain the stated RH hypothesis. |
| Fixed amplitude with varied readout and actual-profile relaxation | The varied observation fails the literal Fourier readout. The relaxation lacks the corresponding physical source and literal field. |

[request]: ../research-progress/handoffs/VCD-E16-r1.md
[decision]: ../brainstorm/notes/09_VCD_B04_CALIBRATION_RADIUS_DECISION_20261116.md
[e04]: 04_VCD_E04_TAIL_FOUNDATIONS_20261116.md
[e12]: 12_VCD_E12_FINITE_MIDPOINT_FREEDOM_20261116.md#2-exact-matches-and-attainable-disk
[e13]: 11_VCD_E13_MIDPOINT_AUDIT_20261116.md
[e13screen]: 11_VCD_E13_MIDPOINT_AUDIT_20261116.md#5-degree-increments-and-control-scope
[reference]: ../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md#quantitative-midpoint-calibration-16-november-2026-chat0003
[dlmf]: https://dlmf.nist.gov/1.10#v
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
