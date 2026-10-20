# Mathematical assessment of heat flow contours and Gaussian cap energy

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6-astra (Codex)**,
actual reasoning effort **ultra**, confirmed by the coordinating agent
from current recorded turn metadata.

**Disposition: no blocking mathematical errors found in the reviewed
version.** This is a separate same-model internal mathematical audit.
It is not a cross-model or specialist review, an independent numerical
implementation, or a theta certificate.

Reviewed artifact:
[Note 06: Heat flow contours, collision patches, and Gaussian cap energy][note].
SHA256 of its complete reviewed bytes:

```text
a6a7cd796d458a37db7ae7599175f2757bc67d14276606513eed1b6ace90effe
```

The [result index][results] and [avoid index][avoid], particularly
[same-model review limits][a05] and [scope limits][a07], govern the
assessment. External exposition links and the figure renderer were not
independently audited; the mathematical identities below were checked
directly.

## Accepted calculations

1. **Time direction and collision geometry.** The reversal
   \(u(s,y)=H(T-s,a+y)\) gives the ordinary heat equation. Substitution
   in the local expansion verifies the root displacement
   \(2h_3\tau/(3h_2)\), in addition to the leading
   \(\pm\sqrt{2\tau}\). The real root walls lie on the physical
   post-event side. The Gaussian's infinite spatial support prevents a
   square-root opening from becoming a finite domain of influence.

2. **Splitting and orientation.** Index additivity requires every
   interface to avoid \(J=0\) and every shared arc to appear with
   opposite orientations. A nonvanishing annular complement has zero
   total boundary degree without having zero circulation around its
   hole. For the rounded quadratic lens, the top cap and the lower
   connector each contribute \(-\pi\), while the root walls contribute
   zero. Thus the stated \(dt\wedge dx\) orientation gives \(W_J=-1\).
   The complement can contain no additional event. The unrounded
   collision apex would instead make physical winding undefined.

3. **Nonzero level arc.** On \(F=H/h_2=e>0\), the normalized jet
   \(J/h_2=e+iF_y\) remains in the right half-plane. Its continuous
   phase change is its endpoint difference. Together with the cap
   crossing calculation this proves \(W_J=-N/2\) under the stated
   simple-zero and Jordan-domain hypotheses. The final text correctly
   defines the endpoint principal phases using \(J/h_2\), including
   when \(h_2<0\), and identifies the potentially failing graph as
   \(\tau=\tau(y)\). The separation
   \(|J|\ge |h_2|e\) is event-dependent. Global continuation and the
   stronger cap count remain separate obligations.

4. **Gaussian propagation and energy constants.** Complete Gaussian
   convolution cancels the source multiplier \(e^{su^2}\). The two
   moment identities and their derivative versions follow by Fubini
   and Gaussian integration by parts. Integrability of every finite
   theta source moment gives bounded real-axis derivatives and the
   required Gaussian Sobolev hypotheses. For variance \(2s\), removal
   of the first two Hermite modes gives the exact constants
   \[
   \int G_s f^2\le s\int G_s(f')^2
                    \le 2s^2\int G_s(f'')^2.
   \]
   The coefficients \(c_n=(2s)^{n/2}h_n/n!\) yield the convergent
   deficit expansion
   \[
   D_s=-h_0^2-sh_1^2+
      \sum_{n\ge3}\frac{n-2}{2}\frac{(2s)^n}{n!}h_n^2.
   \]
   Equality at a double event requires the quadratic Hermite mode.
   Consequently a nonzero bounded theta cap has strict positive
   deficit under the event hypothesis, without a uniform margin.

5. **Controls, tails, and the source kernel.** The quadratic and cubic
   substitutions give \(D_s=0\) and
   \(D_s=(2/3)h_3^2s^3\), respectively. For the positive atomic control
   \(1+e^{t-T_0}\cos x\), the all-real threshold is \(T_0>0\), future
   roots are simple, and
   \(D_s=1+s\sinh(2s)-\cosh(2s)>0\). Its simultaneous periodic
   threshold events and non-theta source are stated. The
   product-to-sum derivation confirms both signs and the factor
   \(1/2\) in the two-source kernel. The quadratic Gaussian mass and
   signed-integral calculations also confirm that discarding the
   exterior of the root wedge loses an essential cancellation.

6. **Heat balances.** Differentiating the integral between moving
   simple roots gives the stated endpoint derivative difference.
   The identity
   \(E_t+E_{xx}=2(H_x^2+H_{xx}^2)\), for \(E=H^2+H_x^2\),
   yields the Gaussian Bochner balance with the stated signs and
   factor two. Its quadratic check is
   \(2h_2^2(s+s^2)\).

## Scope and continuation

A certified \(D_s\le-\delta<0\) would exclude the **initial** common
zero by \(h_0^2+s h_1^2\ge\delta\). It would not prove a later
collision. At a non-event point, the positive Hermite tail is
\(O(s^3)\) as \(s\downarrow0\), so an unspecified adaptive choice of
\(s\) only reformulates first-jet nonvanishing. A meaningful next
comparison therefore needs a fixed positive scale, a parameter
window, complete tails and source errors, and a measured advantage
over the direct consumer using the same source data.

The note supplies an exact wall-phase simplification and an exact
Gaussian event-exclusion criterion. It does not supply an actual
theta sign estimate, extra winding, an additional collision, or a
numerical cost advantage. The quadratic, cubic and atomic controls
are compatible with the identities, as they should be. The figure
is an illustration of the exact quadratic calculation, not numerical
evidence for theta. These limitations are represented correctly in
the reviewed version.

[note]: ../notes/06_HEAT_FLOW_CONTOURS_AND_GAUSSIAN_CAP_ENERGY_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
