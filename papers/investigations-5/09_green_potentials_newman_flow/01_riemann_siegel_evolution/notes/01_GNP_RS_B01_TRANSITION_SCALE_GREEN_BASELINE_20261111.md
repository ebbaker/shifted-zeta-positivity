# GNP-RS-B01: a transition-scale Green baseline and the remaining signed value

11 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual model identifier and effort
are unavailable in child chat0001 capture metadata. **Task B; recommended
GPT-6 Astra.** No model setting is inferred from that recommendation.

**Status:** conceptual decision with an elementary representation lemma
proved below, an application of an inherited absolute-mass obstruction,
and a **proposed uniform estimate frozen for E01**. The proposed baseline
estimate is not reported as proved. No canonical signed upper value,
zero exclusion, numerical run or specialist review is supplied.
The [decision][decision], [self-check][review] and [E01 request][packet]
separate these evidence levels.

## 1. Choice, quantifiers and classification

Keep the complete source and \(\partial_\lambda H=-H_{zz}\). Select the
existing **Gaussian evolution of the complete reflected RS expression**.
Use the HDA fixed-buffer crossover theorem as its field provider, rather
than inventing a second saddle representation. Freeze
\[
 L_X=\log(X/(4\pi)),\qquad
 \lambda=\frac{c}{L_X},\quad \frac12\le c\le1,\qquad X\ge X_* .
 \tag{1}
\]
Here \(X_*\) is a single sufficiently large onset, not a list of sampled
heights; include \(L_X\ge2\), so \(0<\lambda\le1/2\).
In every spatial integral \(\lambda\) is held fixed; it is **not**
replaced by \(c/\log(x/(4\pi))\) at each integration point. The chosen
Green consumer has \(d=1/2,\ r=1\), hence
\[
 m_*=\frac{\sin(\pi/8)}{2\cosh(\pi/8)}>0.
 \tag{2}
\]
Every \(X\ge X_*\) and every \(c\in[1/2,1]\), including exceptional
centers, is required. This band approaches time zero as height grows
but does not include the time-zero slice or all positive times.
The finite initial range remains a separate obligation.

The new analytical target is an **outer-boundary/center acquisition
estimate**, not the favorable sign of the critical-boundary logarithm.
The parent retains its time-zero signed-value task. The physical source,
Green kernel, strip and normalization of \(H\) are unchanged. A known
nonzero holomorphic comparison factor will be used only inside the
observable, with its harmonic contribution explicitly accounted for.

Read the [result index][results], [heat-flow cluster11][cluster11] and
[controls12][controls], and the [avoidance index][avoid], particularly
[target01][a01], [premise02][a02], [scope07][a07] and
[separate bounds12][a12]. The representation below is not an
RH-equivalent milestone. A future universal time-zero vanishing statement
would be the target already classified in the overview.

## 2. The complete provider and what is actually reused

[HDA Ansatz Note04][hda04], CS3 and CS6, retains both arithmetic arms,
the corrected RS term and its field remainder on every fixed horizontal
and vertical buffer. For nonnegative \(\lambda\), it gives relative
field error \(O(X^{-3/4})\) against the **sum of the two nonzero arm
moduli**, uniformly for \(\lambda L_X\le8\). Its constants and onset
are finite but unevaluated. Its [Assessment03][hda-review] accepts
these statements at same-model internal scope.

That source's §§5–6 pay the Gaussian exterior using height-relative
gamma bounds, the full source on the distant real tail, and the full
growing mode population. This reuse does not integrate a strip-only
remainder over an unbounded Gaussian line. Choose fixed target buffers
\(r=1,\ b=9\) and retain all enlarged buffers/onsets demanded there.
The heights \(4,8\) are covered by this inherited result, not by silently
extending the printed constants of [Polymath Theorem 1.3][polymath].

At each large real \(x\), recenter a fixed HDA chart and use its
\(N_x=\lfloor\sqrt{x/(4\pi)}\rfloor\). The complete correction handles
cutoff transitions. No derivative of a floor function is used.
Recentring will cover a slowly growing integration window with the
same fixed-buffer constants; increasing a chart radius and retaining
its old constants would not.

## 3. A zero-free comparison factor with no interior pole correction

For \(0<\Im z<8\), use \(0<\arg z<\pi\) and set
\[
 L(z)=\Log(z/(4\pi)),\qquad
 A(\lambda,z)=\frac{\pi^{1/4}}{16}z^{7/4}
 \exp\!\left[-\frac{\pi z}{8}
       +\frac{\lambda}{16}\left(L(z)^2-\frac{\pi^2}{4}\right)\right],
\]
\[
 \Theta(\lambda,z)=\frac z4(L(z)-1)
        +\frac{\pi\lambda L(z)}{16}+\frac{7\pi}{8},\qquad
 C_-(\lambda,z)=\frac{A(\lambda,z)}2e^{-i\Theta(\lambda,z)} .
 \tag{3}
\]
This is the elementary dominant arm of [HDA Note03, CB3–5][hda03],
continued into the upper strip. It is not the exact gamma factor
\(M(s)\), nor Polymath's differently defined \(M_t(s)\).
The explicit logarithm in (3) makes \(C_-\) holomorphic and zero-free
in the open strip. On the real boundary use upper boundary values
and omit the single point \(x=0\) from pointwise quotients.

**Lemma (harmonic cancellation).** With the parent's two-boundary
functional \(\mathcal J\), for real \(X\) and \(0\le\lambda\le1/2\),
\[
 \mathcal J[C_-](X)=0 .
 \tag{4}
\]
All logarithmic boundary integrals in this statement converge absolutely.

**Proof.** The real part of the explicit logarithm of (3) is harmonic
in the open strip. Near \(z=0\) it is \(O(1+|\log|z||^2)\), with
gradient \(O((1+|\log|z||)/|z|)\); these boundary singularities are
integrable. On the two horizontal boundaries, at large \(|x|\),
its absolute value is \(O(1+|x|+\log^2(2+|x|))\), uniformly in the
stated compact time range. Apply the strip Green formula on a rectangle,
removing a small upper semicircle at zero. Its Green kernel vanishes
linearly at the lower boundary, so the small-circle terms are
\(O(\epsilon(1+|\log\epsilon|^2))\) and vanish. The far vertical-side
terms vanish by exponential harmonic-measure decay against the stated
growth. The remaining boundary measures are the parent's two copies
of \(K(t)=1/[16\cosh(\pi t/8)]\), proving (4). ∎

As a boundary check, for real \(x\ne0\),
\[
 |C_-(\lambda,x+i0)|=
 \frac{\pi^{1/4}}{32}|x|^{7/4}
 \exp\!\left[-\frac{\pi|x|}{8}
 +\frac{\lambda}{16}
   \left(\log^2(|x|/(4\pi))-\frac{\pi^2}{4}\right)\right].
 \tag{5}
\]
For negative \(x\), the \(\arg z=\pi\) terms in (3) give exactly this
modulus. The normalization is therefore compatible with both real tails.

Define \(V_\lambda(z)=H_\lambda(z)/C_-(\lambda,z)\) in the open strip
and by boundary values almost everywhere. Equations (4) and the inherited
[complete Green identity][green] give the **exact** decomposition
\[
 J_\lambda(X)=I_\lambda(X)+O_\lambda(X),\qquad
 I_\lambda(X)=\int_{\mathbb R}K(x-X)\log|V_\lambda(x+i0)|\,dx,
\]
\[
 O_\lambda(X)=
 \int_{\mathbb R}K(x-X)\log|V_\lambda(x+8i)|\,dx
       -\log|V_\lambda(X+4i)|.
 \tag{6}
\]
Here \(O_\lambda\) denotes the named outer contribution, not big-O.
The parent's strip input makes the subtracted center nonzero.
Real zeros and the integrable singularity at \(x=0\) remain in \(I_\lambda\).
There is **no extra \(G(X,1)\) term in (6)**: (3) has no interior zero.
This differs from removing the exact xi/gamma completion in the parent's
time-zero zeta formula. Adding that old pole correction again would change
the identity.

## 4. Frozen E01 target: a uniformly shifted prime baseline

Put
\[
 \nu_{X,\lambda}=\frac X2+\frac{\pi\lambda}{8},\qquad
 P_{c,\lambda}(X)=
 \sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\log n}
 \frac{n^{-5/2-c/4}}{1+n^{-4}}
 \cos(\nu_{X,\lambda}\log n).
 \tag{7}
\]
This prime-power series is absolutely convergent. For integer \(Q\ge2\)
its omitted tail is at most
\(Q^{-3/2-c/4}/(3/2+c/4)\le(2/3)Q^{-3/2}\).
It is a proposed approximation to the **outer contribution**, not an
Euler product assigned to \(H_\lambda\).

**Proposed statement, to be proved in E01:** there are finite constants
\(C_*,X_*\), independent of \(X,c\) in (1), such that
\[
 \left|J_{c/L_X}(X)-I_{c/L_X}(X)+P_{c,c/L_X}(X)\right|
       \le \frac{C_*}{L_X}.
 \tag{8}
\]
Its expected intermediate field estimate, for \(y=4,8\) and
\(|x-X|\le R_X=(32/\pi)\log X\), is
\[
 V_\lambda(x+iy)=
 \zeta\!\left(\frac{1+y}{2}+\frac c4
          -i\left(\frac x2+\frac{\pi\lambda}{8}\right)\right)
       +O(L_X^{-1}).
 \tag{9}
\]
Equations (8)–(9) are **request targets**, not proved results of this
decision note. Write \(s_-(z)=(1-iz)/2\). E01 must pay the following
complete proof ledger.

| Payment | Fixed route and intended allowance |
| --- | --- |
| Full HDA field remainder | Recenter \(r=1,b=9\) charts; \(E_o/\lvert C_-\rvert\) is bounded for \(y=4,8\). Retain CS6's \(O(x^{-3/4})\), all cutoff corrections and inherited Gaussian-tail gates. |
| Dominant arithmetic sum | Its exponent is \(s_-(z)+\lambda L(z)/4-i\pi\lambda/8\), with weight \(e^{\lambda\log^2n/4}\). Prove the uniform \(O(\lambda)\) replacement by the ordinary zeta sum only on these safe lines. |
| Reflected arm and RS correction | Keep them before estimating. The reflected population should be \(O(x^{-3/4})\) at \(y=4\) and smaller at \(y=8\); track the nonzero carrier ratios and corrected term. |
| Center-based parameters | Replacing \(\lambda L(z)\) by \(c\) costs \(O(\lambda(R_X+1)/X)\). Hold \(\lambda\) fixed, and prove \(\lambda L_x<8\) on all recentered charts. |
| Logarithmic transfer on the safe lines | The comparison zeta has real part at least \(5/2\). An Euler/Dirichlet bound gives modulus \(>1/2\); an eventual field error \(<1/4\) gives a true floor and a Lipschitz log payment. This floor is never asserted on the critical boundary. |
| Remote boundary | Use the exact \(H\) unit-interval logarithmic bound plus (3), not the far-field approximant. With the frozen \(R_X\), the intended uniform allowance is \(O(X^{-3}\log^2X)\). Account for the neighborhood of \(x=0\). |
| Prime combination | Apply the parent's exact Fourier transform of \(K\) to the safe zeta logarithm. The upper-line-minus-center coefficient is \(-n^{-5/2-c/4}/(1+n^{-4})\), with the phase in (7). |

A concrete reason for (9) to be tractable is that at these outer heights
the exponent has real part at least \(5/2\). For \(n\le N_x\), the heat
weight can be bounded by a small additional power of \(n\). The inequality
\(e^u-1\le u e^u\), \(u\ge0\), then reduces its removal to a convergent
\(\lambda\sum n^{-a}\log^2n\) payment with fixed \(a>1\).
That argument is invalid on the critical boundary: its exponent is only
\(1/2+c/4\). The growing population must not be replaced there by a
fixed-mode limit. This distinction is the reason to select the outer
baseline as E01's bounded task.

For the stated safe-line comparison,
\[
 |\zeta(\sigma+it)-1|\le
 \sum_{n\ge2}n^{-5/2}
 \le 2^{-5/2}+\int_2^\infty u^{-5/2}\,du
 =\frac7{12\sqrt2}<\frac12\quad(\sigma\ge5/2).
 \tag{10}
\]
Thus the floor route is independent of unknown zeros. The eventual onset
must be expressed in terms of the inherited constants; no numerically
evaluated onset is promised.

If E01 proves (8), its error can be made less than \(m_*/4\) after the
additional explicit gate \(L_X>4C_*/m_*\). The **remaining** quantity is
\(I_\lambda-P_{c,\lambda}\). No favorable upper value for it is supplied
here. Even a completed E01 will not by itself exclude a defect.

## 5. Why the separate-magnitude substitute fails in this band

This is an application of prior work, not a new discovery of the
growing-cutoff obstruction. The earlier collision manuscript's
[Proposition “Last-block absolute mass”][mass-source] and
[S04 Note01][s04] retain the physical heat weight and prove the relevant
coefficient growth. In the present notation, on the real boundary,
\[
 W_n(\lambda,x)=
 n^{-1/2}\exp\!\left\{\frac{\lambda}{4}
          (\log^2n-L_x\log n)\right\},\qquad
 \lambda L_x=c_x.
\]
Their last-block calculation gives, uniformly on compact
\(c_x\)-subintervals of \((0,4)\),
\[
 \sum_{N_x/2\le n\le N_x}W_n
 =\left(2(1-2^{-1/2})+o(1)\right)
   \exp\!\left(\frac{4-c_x}{16}L_x\right).
 \tag{11}
\]
The harmless natural-cutoff convention difference is within one
endpoint term and does not change this asymptotic.

Replacing the complete normalized critical-boundary expression by the
sum of the two arms' absolute mode weights, plus absolute correction and
remainder, gives an upper envelope \(\mathfrak M\ge2\sum W_n\).
On \(|x-X|\le R_X\), (11) implies
\[
 \log\mathfrak M(\lambda,x)
 \ge \frac{4-c}{16}L_X+O(1).
\]
Indeed \((4-c_x)L_x=4L_x-\lambda L_x^2\) differs from
\((4-c)L_X\) by \(O(R_X/X)\), with \(\lambda\) held fixed.
Since \(\int_{-R_X}^{R_X}K(t)\,dt=1/2+o(1)\), this replacement's compact
logarithmic allowance is at least
\[
 \frac{4-c}{32}L_X+O(1)\ \ge\ \frac3{32}L_X+O(1).
 \tag{12}
\]
The \(O(1)\) here is uniform in the selected band and may have either sign.
The exact omitted critical-boundary integral has absolute value
\(O(X^{-3}\log^2X)\): combine the parent's unit-interval logarithmic
bound with (5), sum the exponential kernel tails, and use
\(e^{-\pi R_X/8}=X^{-4}\). The carrier's logarithmic-square
singularity on the unit interval containing zero is integrable, so
that interval obeys the same finite bound. Even granting its exact
value cannot cancel (12). Any globally valid envelope has a remote
logarithmic integral no smaller than this exact remote contribution.
The prime baseline is uniformly bounded, by the same convergent sum in
(10). Consequently, **even if E01 pays the outer baseline**, this particular
separate-magnitude replacement cannot yield a strict upper bound below
the fixed margin \(m_*\) at all large heights.

**The lower bound is on the chosen positive envelope, not on \(H\) or \(J\).**
It excludes this payment rule in (1), not phase-retaining logarithmic
estimates, coupled contour arguments, other time bands, or all RS methods.
Retaining the small correction is mandatory but does not remove the
already large positive mode envelope. The existing stronger signed
diagnostics elsewhere in the repository are not imported as obstructions
to this different Green observable.

## 6. Controls, ownership and decision

The control screen is analytical. No new control computation is needed
to test (4): it holds for every logarithmically admissible field divided
by this same zero-free carrier, including colliding fields. It therefore
cannot distinguish theta. Equation (12) supplies a failed upper-bound
recipe, not a collision exclusion.

For the prospective (8), the source-specific input is the **complete
HDA arithmetic expansion**, not positivity or the heat equation alone.
The [overview's control table][overview] remains the complete family map:
Euler/translated sources change the completion; weighted-square,
finite-prefix and finite-prime controls lack full normalized arithmetic
and reflection; reflected super-Gaussian and smooth/primitive controls
lack theta arithmetic; \(q,q_{T,a}\) lack the literal completed zeta field;
atomic/finite-profile controls lack the full source/profile; the
RH-conditional endpoint controls lack ordinary Dirichlet arithmetic;
variable readouts lack the cosine/Newman equation; the three-profile
relaxation lacks the full integer zero-measure constraint.

These are missing premises for unchanged use of the provider, not
claims that every control must fail (8). An outer-baseline identity alone
permits a positive Green value. Any later signed upper bound must be
tested on the controls' actual witness domains, with their own
normalization and baseline. A control may pass a collision-free finite
box. No finite check supports an RH-equivalent assertion.

**B01 decision:** proceed to the single fixed analytical proof request
E01 for (8), using (3) and the inherited HDA provider. Do not open a second
complete contour construction or a numerical campaign. The new useful
contract is the uniform nonzero-time outer baseline; the signed
critical-boundary estimate remains a separately named conceptual gap.
The [model-change return][return] recommends **GPT-6.1 Sol for E01**.

[decision]: ../brainstorm/notes/02_GNP_RS_B01_DECISION_20261111.md
[review]: ../reviews/02_GNP_RS_B01_DECISION_SELF_CHECK_20261111.md
[packet]: ../research-progress/handoffs/01_GNP_RS_E01_UNIFORM_OUTER_BASELINE_R1_20261111.md
[return]: 02_GNP_RS_B01_RETURN_AND_MODEL_CHANGE_20261111.md
[overview]: ../research-overview/01_GNP_RS_RESEARCH_OVERVIEW_20261110.md
[green]: ../../manuscript/sections/05_green.tex
[hda03]: ../../../01_heat_density_asymptotics/ansatz/notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[hda04]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[hda-review]: ../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[mass-source]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[s04]: ../../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md
[polymath]: https://arxiv.org/html/1904.12438v2
[results]: ../../../../../result-summaries/README.md
[cluster11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
