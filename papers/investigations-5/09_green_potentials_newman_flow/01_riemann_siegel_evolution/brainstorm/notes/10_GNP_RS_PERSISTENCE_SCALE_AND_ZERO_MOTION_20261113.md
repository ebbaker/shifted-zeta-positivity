# What persistence would have to mean after B10

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Same research chat as child
chat0007, thread `01a1d19b-462e-7722-a6be-3d1555a82423`. Actual backend
model and reasoning effort are unavailable in its recorded configurations.

**Status: brainstorm with elementary analytical deductions and a scoped
polynomial control, checked by the same assistant.** B10's separate internal
audit and manuscript integration are complete; their input scopes remain
those of [Note31][audit], [Note33][integration] and [Review17][verification].
This discussion supplies no new canonical arithmetic estimate, persistence
theorem, every-center exclusion or manuscript revision.

Read the [result index][results], especially [cluster11][cluster] and
[local-geometry cluster13][geometry], and the [avoid index][avoid]. The
classification under [avoid01][a01] is quantitative diagnosis: the useful
new numbers here are the cubic-transfer constant **27/128**, the required
exceptional-set scale **ell / log U**, and the exact single-zero Green mass
**pi times its upper height**. Merely postulating a strong persistence law
is a sufficient-condition restatement, not progress toward proving it. The
[controls12][controls] screen is in §8, following [avoid02][a02] and
[avoid07][a07]. [Continuation guidance][continuation] is separate.

## 0. Clarification: observation centers and the curve between two zeros

**Terminology correction requested by the author, 13 November 2026:**
reserve **zeta height** for T=|X|/2. In z=X+ib, call b the
**transverse offset** and a zero's imaginary coordinate its transverse
depth. Earlier "height" language about these imaginary coordinates
belongs to the H-plane, not the original zeta plane. The coordinate map
and the proposed lower-offset continuation are developed in
[the subsequent brainstorm](12_GNP_RS_LOWER_TRANSVERSE_OFFSET_AND_LOG_OBSERVATION_20261113.md).

Added 13 November 2026 in response to the author's background question;
same authorship and unavailable model/effort metadata as above. This is
a notation and scope clarification, not an additional research result.

An **observation center** is a freely chosen real spatial coordinate
\(X\). The actual point used by the Green construction is \(X+4i\),
and its boundary averages are weighted by \(K(x-X)\). Thus the word
"center" describes where that observation is horizontally positioned.
It does not mean that \(X\) is automatically a zero, the midpoint of
two zeros, or a critical point of the field. At time zero the field
coordinate satisfies \(H_0(z)=\tfrac18\xi(\tfrac12-iz/2)\), so
positive \(X\) corresponds to absolute zeta height \(X/2\).

There are indeed curves associated with a pair in the collision analysis:

| Object | Definition and role |
| --- | --- |
| Pair midpoint | \(m(\lambda)=(z_+(\lambda)+z_-(\lambda))/2\); between the two real roots on their real side, and real for a conjugate pair |
| Critical-point curve | \(x_c(\lambda)\) satisfies \(\partial_xH_\lambda(x_c)=0\); near an ordinary double event it is the critical point between the two nearby real roots and continues locally through the event |
| Observation center | \(X\), chosen independently; one may choose \(X=m(\lambda)\) or \(X=x_c(\lambda)\), but that is an additional choice |
| B10 sampling curve | \(\lambda=1/\log(X/(4\pi))\) in the **time-position plane**; it is prescribed independently of any pair |

The midpoint and critical-point curves agree in the pure quadratic model
and meet at the collision, but generally differ away from it because of
the surrounding analytic factor. The [local collision section][collision]
explicitly distinguishes their velocities. The observation point
\(X+4i\) is above the zero strip, so it is not the point between the
two zeros even when its horizontal coordinate is chosen to be their midpoint.

On the nonreal side, write the pair as \(m(\lambda)\pm i y(\lambda)\).
Only its upper member lies in the upper Green strip, and the pair's
contribution to this upper-strip potential is
\[
 G(X-m(\lambda),y(\lambda)).
\]
Thus the earlier phrase "one upper zero" was counting one member of a
conjugate pair, not discarding the second zero from the heat dynamics.
When both members are real, their contribution to this potential is zero;
it also tends to zero as the conjugate pair reaches the real axis.

The slow-motion discussion in §4 is **conditional**, not a bound proved
for canonical zeros. More accurately, it illustrates a slowly moving
pair midpoint, with controlled nonzero separation, while the independently
chosen observation center moves past the pair. The vertical velocities
can be singular near a collision even if the midpoint is regular.

If the observation instead follows the pair, \(X=m(\lambda)\), its
contribution is \(G(0,y(\lambda))\); the horizontal decay from scanning
past the pair disappears. That is a legitimate different persistence
question. B10's average over centers with \(\lambda=1/L_X\) does not
automatically estimate this pair-following quantity. One would need a
new estimate or a justified comparison between the two curves. No
conclusion here rules out studying persistence along the pair midpoint
or the critical-point curve.

### Why the imaginary height is four, and who chooses the observation path

Added in the author's subsequent 13 November follow-up. The imaginary
height four is a convenient fixed choice for the auxiliary Green
construction; it is not a heat time or a location selected by a zero.
The strip is \(0<\Im z<8\), and observing on its midline gives equal
harmonic-measure densities on the two boundaries, each of mass one half:
\(K(u)=1/[16\cosh(\pi u/8)]\). The canonical zeros satisfy
\(|\Im z|\le1\) on the stated time range, so \(X+4i\) is separated
from all of them. In particular its logarithmic field value is finite.
These heights also support the [proved outer arithmetic comparison](../../../manuscript/sections/10a_transition_green.tex):
the normalized dominant-arm weights at imaginary heights four and eight
are bounded by \(n^{-5/2}\), placing that step in an absolutely convergent
region. These are useful properties of the chosen heights, not a claim
that four is uniquely optimal. Other observation/strip heights are
possible geometrically; changing them changes the kernel, margins and
estimates and is not already covered by the fixed B10 theorem.

Observation points have no intrinsic equation of motion. The analyst
chooses which values of the two-variable quantity \(J_\lambda(X)\)
to compare. Holding X fixed and varying lambda keeps the point fixed
while the field evolves. Holding lambda fixed and varying X scans one
field horizontally. Choosing \(X=m(\lambda)\) follows the pair's
midpoint horizontally, still observing at imaginary height four.
B10 instead studies the prescribed observations
\((\lambda,X)=(1/L_X,X)\): as X varies the point moves horizontally
and the sampled heat time changes. That schedule fixes the transition
parameter \(\lambda L_X=1\); it is a chosen time-height scaling,
not a law followed by the zeros. One should not speak of an observation
"velocity" without specifying this choice of path and its parameter.

## 1. The gap is a question about spatial mass

Write
\[
 L_X=\log(X/(4\pi)),\quad \lambda(X)=1/L_X,\quad
 j(X)=J_{\lambda(X)}(X),\quad \beta=17/81.
\]
For fixed \(0<\rho\le47/162\), B10 applies on
\(I=[U,U+\ell]\), \(U^{\beta+\rho}\le\ell\le U\), at an
unevaluated sufficiently large onset. Take the **block-constant** cutoff
\(P_U=\lfloor L_U^2\rfloor\). Its quantitative inputs include
\[
 \frac1\ell\int_I R_{P_U}(X,1)\,dX\le\frac{C_\rho}{L_U},
 \qquad
 j(X)\le\frac\delta4+
       \frac{R_{P_U}(X,1)}{2\delta^2}+\frac{C_0}{L_U}
       \quad(\delta>0).                                      \tag{1}
\]
The second inequality, including its uniformity in the regulator, comes
from [E06 (E06.6)][e06] and the audited block-cutoff specialization in
[manuscript §14][b10]. Physical time is fixed inside the spatial integral
defining each residual. Changing its center changes that time.

The existing Green mean is \(O_\rho(L_U^{-1/3})\), and for fixed
\(h>0\) the exceptional proportion is \(O_{h,\rho}(L_U^{-1})\).
Neither says the exceptional set is empty. Even one fixed-size positive
peak fits the permitted total mass on polynomial-length intervals.

Three different statements must be distinguished:

1. A nonreal zero remains nonreal for nearby **heat times**.
2. At one fixed time, its Green signal remains appreciable for nearby
   **spatial centers**.
3. The actual sampled function \(j(X)=J_{1/L_X}(X)\) stays appreciable
   on enough centers in a B10 interval to exceed its permitted mass.

Only the third, or another estimate giving the same mass contradiction,
would bridge this particular gap. Strict positivity without a quantitative
lower size is insufficient: at fixed time even one upper zero makes the
Green potential positive at every center through exponentially small tails.

## 2. An elementary stronger consequence: a cubic mass budget

Put \(\epsilon_U=C_0/L_U\) and \(v=(j-\epsilon_U)_+\). Optimizing
the right side of (1) gives, for \(R>0\),
\[
 \inf_{\delta>0}\left(\frac\delta4+\frac R{2\delta^2}\right)
 =3\,2^{-7/3}R^{1/3},\qquad \delta=(4R)^{1/3}.
\]
The case \(R=0\) follows by taking \(\delta\downarrow0\).
Consequently
\[
 \boxed{(j(X)-\epsilon_U)_+^3\le\frac{27}{128}R_{P_U}(X,1)},
 \qquad
 \int_I (j-\epsilon_U)_+^3\,dX
 \le\frac{27C_\rho}{128}\frac\ell{L_U}.        \tag{2}
\]
No derivative, interchange of optimization and integration, varying prime
cutoff or new estimate for the arithmetic residual is used. We first apply
the uniform pointwise inequality for each regulator and then integrate.
Also \(j\le v+\epsilon_U\) and \((a+b)^3\le4(a^3+b^3)\), so
\(\ell^{-1}\int_I j^3=O_\rho(L_U^{-1})\).

For every \(h>\epsilon_U\), (2) makes the height dependence explicit:
\[
 |\{X\in I:j(X)\ge h\}|
 \le\frac{27C_\rho}{128(h-\epsilon_U)^3}\frac\ell{L_U}.
                                                               \tag{3}
\]
This is an elementary consequence of the audited transfer, not a new
arithmetic milestone. It is the better budget for discussing a fixed-height
defect than the first-moment allowance \(O(\ell L_U^{-1/3})\).

Suppose a seed has \(j(X_0)\ge h\), and a proposed mechanism forces
\(j\ge h/2\) on a set \(E\subset I\). If \(\epsilon_U\le h/4\),
\[
 |E|\le \frac{27C_\rho}{2h^3}\frac\ell{L_U}.                  \tag{4}
\]
Thus a contradiction needs a lower bound greater than that allowance.
For fixed \(h\), the asymptotic sufficient comparison is
\(|E|L_U/\ell\to\infty\). A bound merely of order \(\ell/L_U\)
would require a successful comparison of the currently unevaluated
constants. The set need not be connected: replication at many separated
centers could replace one broad interval.

At the shortest available scale the required length is of order
\(U^{17/81+\rho}/\log U\), which diverges. A fixed-width neighborhood
does not suffice, however accurately its persistence is proved.

## 3. What the Green kernel actually propagates

The [complete Green identity][green] is
\[
 J_\lambda(X)=\sum_{y_k(\lambda)>0}
 G(X-x_k(\lambda),y_k(\lambda)),\qquad
 G(u,y)=\operatorname{atanh}\!\bigl(\sin(ay)\operatorname{sech}(au)\bigr),
 \quad a=\pi/8,\quad 0<y\le1.                              \tag{5}
\]
Each term is positive. Real zeros contribute zero; the observation at
imaginary height four is separated from the canonical zero strip.

There is a genuine fixed-time spatial regularity estimate. Set
\(q=\sin(ay)\operatorname{sech}(au)\). Since
\(G=\operatorname{atanh}q\ge q\),
\[
 |\partial_uG|
 =\frac{a q|\tanh(au)|}{1-q^2}
 \le C_G G,\qquad C_G=a\sec^2a.                            \tag{6}
\]
Integrating this for each term and summing positive convergent terms gives
\[
 e^{-C_G|s|}J_\lambda(X)\le J_\lambda(X+s)
 \le e^{C_G|s|}J_\lambda(X).                               \tag{7}
\]
This argument avoids differentiating the infinite zero sum. A positive
value at fixed time therefore retains half its height for
\(|s|\le(\log2)/C_G\), a constant independent of \(U\). It is
perfectly compatible with an isolated bounded-width peak.

An exact mass calculation is more informative:
\[
 \boxed{\int_{\mathbb R}G(u,y)\,du=\pi y}\qquad(0\le y\le1).
                                                               \tag{8}
\]
Indeed
\(\partial_yG=a\cos(ay)\cosh(au)/[\cosh^2(au)-\sin^2(ay)]\).
The substitution \(w=\sinh(au)\) gives
\(\int\partial_yG\,du=\cos(ay)\int dw/(w^2+\cos^2(ay))=\pi\).
Integrate from \(y=0\); nonnegativity justifies the interchange.

The bound already present in the manuscript is
\[
 G(u,y)\le 2a\sec^2(a)\,y e^{-a|u|}.                       \tag{9}
\]
Together with \(G(u,y)\ge y\sin(a)\operatorname{sech}(au)\), it
also shows \(\int G(u,y)^3du\asymp y^3\), with absolute constants
for \(0<y\le1\). One zero of fixed positive depth thus contributes
only bounded first and third spatial mass. That mass cannot exhaust (2)
on the currently available intervals.

For the unchanged zero class \(y\ge d\), \(|x-X|\le r\), the
manuscript's conservative margin is
\(m(d,r)=d\sin(a)/\cosh(ar)\). The height in (3)–(4) can be tied
to this fixed margin. The sharper value \(G(r,d)\) is also a lower
bound, but it must not be silently substituted for the manuscript's
named \(m_*\).

## 4. Slow heat time is not slow relative spatial displacement

For a simple zero \(z(\lambda)=x(\lambda)+iy(\lambda)\), implicit
differentiation of \(\partial_\lambda H=-H_{zz}\) gives
\[
 z_\lambda=H_{zz}(\lambda,z)/H_z(\lambda,z),\qquad
 \lambda'(X)=-\frac1{X L_X^2}.                              \tag{10}
\]
Thus, along the observation trajectory,
\[
 \frac d{dX}\{X-x(\lambda(X))\}
   =1+\frac{x_\lambda}{X L_X^2},\qquad
 \frac d{dX}y(\lambda(X))=-\frac{y_\lambda}{X L_X^2}.        \tag{11}
\]
If zero velocities were uniformly bounded by powers of \(\log X\),
the zero would barely move while the observer moves at speed one.
That would preserve the bounded-width profile in (9), not broaden it.
For the **same zero** to stay within a fixed spatial distance of the
observer over a long interval, its horizontal heat-time velocity would
instead have to average approximately \(-X L_X^2\). This is a
kinematic requirement, not a claim that such velocity is impossible.

The formal total derivative, where justified, is
\[
 j'(X)=\partial_XJ_\lambda(X)
        -\frac1{X L_X^2}\partial_\lambda J_\lambda(X).
                                                               \tag{12}
\]
The small coefficient of the second term does not give a uniform bound
on it. Near a nondegenerate double event, the local model
\((z-x_*)^2-2(\lambda-\lambda_*)\) has
\(y=\sqrt{2(\lambda_* -\lambda)}\) and \(y_\lambda=-1/y\).
Its Green time derivative is singular as the pair reaches the real axis.
The [local collision section][collision] has regular midpoint and squared
gap variables, but its regular-factor bounds are event-dependent. They
are not a uniform high-center estimate on (12).

There is also a scale test for any proposed derivative bound. If
\(j(X_0)\ge h\), \(|j'|\le D\), and the surrounding interval contains
\([X_0-h/(2D),X_0+h/(2D)]\), then \(j\ge h/2\) on a set of
length \(h/D\). Combining with (4) requires
\[
 D\ge\frac{2h^4}{27C_\rho}\frac{L_U}{\ell}
 \quad\text{if such a peak exists}.                        \tag{12a}
\]
A smaller uniform derivative upper bound would contradict the peak.
For fixed \(h\), however, the sufficient derivative scale is
\(D=o(L_U/\ell)\), which tends to zero polynomially on B10 intervals.
An \(O(1)\) derivative bound, or a power of \(\log U\), is not enough.
The displayed implication also requires its spatial domain to fit inside
an admissible interval; a one-sided version changes only the constant.

On a spatial interval of length \(w\le U/2\) near \(U\),
\(\Delta\lambda=O(w/(UL_U^2))\). In the exact quadratic model,
a zero of initial depth \(d\) barely changes depth if
\(w/(UL_U^2)\ll d^2\). This explains why temporal survival of a
fixed-depth defect is plausible without any broad spatial signal. For
canonical clusters, the regular factor, isolation radius and higher
multiplicities must be paid before using that model uniformly.

## 5. An exact even heat control retaining an isolated peak

This control extends the elementary polynomial already used in
[Note20 §5][geometry-note]. It tests only generic heat evolution, symmetry,
strip geometry and the displayed Green mean consequences.

Fix \(0<d\le1/2\), take \(A\) sufficiently large, and set
\[
 \lambda_0=1/L_A,\qquad \lambda_*=\lambda_0+d^2/2,
 \qquad s=\lambda-\lambda_*,
\]
\[
 F_\lambda(z)=(z^2-A^2)^2-s(12z^2-4A^2)+12s^2.              \tag{13}
\]
Direct differentiation gives \(\partial_\lambda F_\lambda=-\partial_z^2F_\lambda\), with \(F\)
even in \(z\) and real on the real axis. Its squared roots are
\[
 z^2=A^2+6s\ \pm\sqrt{8s(A^2+3s)}.                         \tag{14}
\]
For \(s=-t<0\), write the upper roots as \(\pm a_t+i b_t\).
Then
\[
 b_t^2=\frac{\sqrt{A^4-4A^2t+12t^2}-A^2+6t}{2}
       =2t+O(t^2/A^2),\qquad a_t=A+O(t/A).                 \tag{15}
\]
The estimates are uniform for bounded \(t\). More explicitly,
\[
 0\le b_t^2-2t
 =\frac{4t^2}{\sqrt{A^4-4A^2t+12t^2}+A^2-2t}
 \le\frac{2t^2}{A^2-2t}.                                 \tag{16}
\]
Choose \(A\ge2\) and \(\lambda_*\le1/4\). For
\(0\le\lambda<\lambda_*\), (16) puts every zero in
\(|\Im z|<1\). For \(s\ge0\), both values in (14) are positive:
their sum and product \(A^4+4A^2s+12s^2\) are positive. All four
zeros are then real. This is an actual finite all-real threshold for
this polynomial family, not a threshold assertion about theta.

Along \(\lambda(X)=1/L_X\), for \(|X-A|\le A/2\),
\[
 t(X)=d^2/2+1/L_A-1/L_X=d^2/2+O(L_A^{-2}).                 \tag{17}
\]
It follows, at a sufficiently large \(d\)-dependent onset, that
\(a_{t(X)}=A+O(A^{-1})\), \(b_{t(X)}=d+O_d(L_A^{-2}+A^{-2})\).
The polynomial's complete Green signal satisfies
\[
 j_F(A)\longrightarrow G(0,d)>0,\qquad
 0\le j_F(X)\le C_d\{e^{-a|X-A|}+e^{-a|X+A|}\}.            \tag{18}
\]
In particular, for intervals \(I\subset[A/2,3A/2]\) and
\(p=1,3\), \(\int_I j_F^p\le C_{d,p}\), uniformly in \(A\).
If \(|I|=\ell\) is polynomial in \(A\), the averages are
\(O(1/\ell)\), far below the B10 Green allowances, despite the
fixed positive peak and the zero's temporal survival.

**Scoped conclusion:** generic backward heat evolution, evenness, an
integer zero multiset, this strip bound and these Green average upper
bounds do not force the long spatial persistence needed in (4). The
control is a family of polynomials, not the canonical theta field or
its Dirichlet residual. No single theta counterexample, positive-source
representation or universal exclusion of arithmetic persistence is claimed.

## 6. Enlarging the observation strip does not supply free mass

For an auxiliary strip of height \(B>2y\), observed at \(B/2\), the
same calculation gives
\[
 G_B(u,y)=\operatorname{atanh}\!
   \left(\frac{\sin(\pi y/B)}{\cosh(\pi u/B)}\right),
 \qquad \int_{\mathbb R}G_B(u,y)du=\pi y.                   \tag{19}
\]
For fixed \(y\), increasing \(B\) spreads the profile on scale
\(B\), while reducing its peak to order \(y/B\). In fact,
\[
 \int G_B(u,y)^3du
   =\frac{\pi^3y^3}{2B^2}+O(y^5/B^4)
   \quad (y/B\to0).                                      \tag{20}
\]
To check the remainder, expand sine and atanh uniformly with their
exponentially integrable sech factors, set \(v=\pi u/B\), and use
\(\int\operatorname{sech}^3v\,dv=\pi/2\). Thus width alone loses
the required amplitude. Multiplying the detector by \(B\) also multiplies
its upper-bound errors and changes the consumer. B10 has not been proved
uniformly for a growing strip. This calculation screens a free-broadening
argument only, not every possible new observation geometry.

## 7. What additional information could actually help

The relevant comparison for an isolated depth-\(d\) zero is
\[
 \text{local cubic signal}\asymp d^3,
 \qquad \text{available cubic budget}\ll_\rho\ell/L_U.
                                                               \tag{21}
\]
The first is a fixed-time calculation; applying it to the moving trajectory
requires an explicit local time-transfer estimate. It does not yet follow
uniformly for canonical clusters.

This separates three potential directions:

| Direction | Input that would be needed | Present status |
| --- | --- | --- |
| Keep B10's intervals and force a broad or repeated signal | A consequence of the **unchanged complete arithmetic field** forcing enough centers with substantial \(j\), beyond (4) | No such estimate supplied; generic transport fails to force it |
| Estimate the residual on much shorter intervals | A genuine local arithmetic estimate with total residual tending to zero, plus bounded-scale persistence on the moving trajectory | At the present \(1/L_U\) mean rate, \(\ell=o(L_U)\) would suffice for a fixed-height peak; this range is far outside B10 |
| Exploit the assumed zero directly | A quantitative constraint on the complete field near that zero that defeats its allowed local residual, with every remainder paid | A possible conceptual route; simply restating the forbidden event as a residual inequality is not an acquired estimate |

For a shrinking depth, the scale check becomes
\(\ell/(L_Ud^3)\to0\), with \(\epsilon_U=o(d)\), if one attempts
the same local-mass argument. This is conditional arithmetic bookkeeping,
not a uniform shrinking-depth theorem. Constants and time transport must
also be uniform. The fixed \(d\) result would still leave all smaller
depths, the full \(c\)-band, bounded heights and time zero unaddressed.

My present judgment is that **temporal persistence alone is not a plausible
bridge from B10 to every center**. A successful persistence route would
need a mechanism forcing extra spatial mass: a zero inducing many nearby
defects, unusual collective drift, or a lower bound on the surrounding
canonical arithmetic residual. None is supplied by positivity of (5) or
the ordinary collision expansion. Further polynomial-exponent improvements
to the same mean estimate do not by themselves resolve this mismatch.

The useful brainstorming question is concrete: what canonical arithmetic
feature would make an isolated off-axis pair expensive across many nearby
centers? Before investing in a derivative theorem, identify how its actual
numerical bound could exceed (4), rather than merely prove continuity.

## 8. Collision screen and verification boundaries

The elementary kernel statements apply to any positive zero potential
in the indicated strip; they **do not fail** merely because a source is
noncanonical. Likewise, local square-root splitting is shared by controls.
Those shared facts cannot distinguish theta. The explicit control (13)
already defeats broad persistence based solely on that shared class.

For a proposed **arithmetic** amplification, the existing screen requires
the following premise checks. This is an applicability screen, not a claim
that every control violates each derived averaged inequality.

| Control family from controls12 | Canonical input absent, or implication not supplied |
| --- | --- |
| Euler-factor and translated heat sources | Unchanged complete theta coefficients and the precise full evolved arm; their heat evolution alone survives |
| Weighted squares and finite-tail changes | Full canonical coefficient sequence and reflection; some have no finite all-real threshold, so their local events are not global threshold controls |
| Finite-prime orbit controls | Full source reflection and unrestricted coefficient information; any fixed finite prime list remains insufficient by that control's scope |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Canonical integer-square/ordinary Dirichlet arithmetic; positivity, reflection or endpoint matching separately survive |
| Atomic, exact finite-profile and compact continuous controls | Complete theta profile, coefficients and the stated global growth/simplicity inputs, rather than finitely matched observations |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic; their conditional construction is not an unconditional theta counterexample |
| Fixed-amplitude variable observation kernels | Literal cosine readout and its Newman equation; these are not physical zero trajectories of the unchanged readout |
| Relaxed positive-measure profiles | Actual integer zero multiset and complete-field identification; (13) is a stronger integer/heat control for the narrower generic-persistence test |
| RSCT calibrated multiplicative models | Full common-height trajectory, complete Green window and all unfrozen arithmetic coefficients |

Same-assistant checks: minimized (1) with exact coefficient 27/128;
checked the threshold constants in (3)–(4), the heat-clock sign in
(10)–(11), the integral (8), the polynomial heat equation and squared-root
formula, the rational remainder in (16), and the wide-strip expansion.
All statements involving B10 keep its block cutoff, fixed positive rho,
unchanged physical geometry, unevaluated constants and sufficiently large
onset. No numerical zero scan, external new mathematical theorem or
specialist review is claimed.
The small [algebra/check record](../../numerics/19_GNP_RS_PERSISTENCE_ALGEBRA_CHECKS_20261113.json)
records exact rational constants and polynomial coefficient cancellation;
it is not numerical evidence about theta zeros.

Chat capture: the registered refresh currently fails because the source
creation time is `2026-11-12T21:12:56.660Z`, while the verified archive has
`2026-11-12T21:12:56.623Z`. The 37 ms discrepancy has not been bypassed or
repaired by changing either record. The prior verified archive is intact;
an explicitly unregistered public-text supplement records available new
messages separately. Capture provenance does not validate these claims.

[audit]: ../../notes/31_GNP_RS_B10_PREINTEGRATION_PROOF_AUDIT_20261112.md
[integration]: ../../notes/33_GNP_RS_B10_MANUSCRIPT_INTEGRATION_20261112.md
[verification]: ../../reviews/17_GNP_RS_B10_MANUSCRIPT_VERIFICATION_20261112.md
[b10]: ../../../manuscript/sections/10d_short_window_means.tex
[e06]: ../../notes/17_GNP_RS_E06_ADAPTIVE_PHASE_AND_TANGENT_20261111.md
[green]: ../../../manuscript/sections/05_green.tex
[collision]: ../../../manuscript/sections/04_logarithmic_collision.tex
[geometry-note]: ../../notes/20_GNP_RS_GREEN_GEOMETRY_AND_CRITICAL_TIME_20261111.md
[continuation]: 11_GNP_RS_PERSISTENCE_CONTINUATION_20261113.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[geometry]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
