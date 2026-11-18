# VCD-GT-GR-E08 r1 — Compact radial Gaussian weak law

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Explicit executor dispatch requested
**gpt-6.1-sol / ultra**. Independent actual serving-model and effort
metadata were unavailable.

**Proved in-note on the paid canonical tube, pending E09 assessment.**
All five pins in [frozen E08 r1][request] matched. This is a regularity and
representation estimate under [Classification01][classification], within
the radial weak repair selected by [B03][decision]. The [E01 audit][e01]
identified a finite-polynomial radial cusp. The law below uses the compact
heat balance of [Note40 §§1–2][n40], assessed in [Assessment19 §1][a19].

[Result index][results] · [Cluster13][cluster] · [Controls12][controls] ·
[Avoid index][avoid] · [Premises02][premises] · [Scope07][scope]

## 1. Test and full complement

Use the unchanged canonical theta field in physical time, \(\partial_t H=-H_{zz}\),
on a compact paid interval \(I=[t_0,t_1]\subset[0,1/2]\).
Freeze \(T\ge64,\ L=\log T,\ \ell=L^{-1}\), with \(c\in[T,2T]\),
\(d\ge0,\ |D|\le d\ell^2,\ \max(2,4\sqrt d)\le a\le L\).
The tracked occurrences are \(c\pm\sqrt D\), including repetition,
and each exterior displacement \(w=\rho-c\) satisfies \(|w|\ge a\ell=r_0\).
The target displacements satisfy \(|w|\le r_0/4\). We use the
closed-slab strip \(|\Im\rho|\le1\), the complete closed-unit count, and
the upper safe-line estimate of [Note41 §§1,3][n41], with its common
constant \(C_{\rm u}\). Put \(\delta=D/\ell^2\), \(\sigma=(t-t_0)/\ell^2\).
A prime denotes physical differentiation, and a dot denotes
\(\sigma\)-differentiation.

Take \(P(s)=6s^5-15s^4+10s^3\) on \([0,1]\), extended by zero below
and one above. Let \(\kappa(x)=1-P(|x|-1)\) and \(\chi(v)=P(6v-2)\).
For fixed \(p\in\{1,2,3\}\), \(\alpha>0\), set
\[
 f(u,\delta)=\chi(|u|/a)\frac{e^{-\alpha |u|^2}}{(u^2-\delta)^p},
 \qquad
 \psi(w,D)=\kappa(\Re w)f(w/\ell,D/\ell^2).
\]
Define \(f\) by zero on \(|u|\le a/3\). For \(|u|\ge a/3\),
\(|u^2-\delta|\ge (7/16)|u|^2\), since \(d\le a^2/16\).
The extension is \(C^2\) in the real spatial variables and has a
continuous \(D\)-derivative, including parameter endpoints by local
extension. The inner cutoff equals one on all exterior occurrences
and zero in a neighborhood of all target occurrences.

Write \(\mu(w)=\ell^2/(w^2-D)\). With all occurrences counted, define
\[
 \begin{aligned}
 J_p(t)&=\sum_{\rho}\psi(\rho-c,D),\\
 A_p(t)&=\sum_{\rho\ {\rm exterior}}e^{-\alpha |w|^2/\ell^2}\mu(w)^p,\\
 E_p(t)&=\sum_{\rho\ {\rm exterior}}
       (1-\kappa(\Re w))\,e^{-\alpha |w|^2/\ell^2}\mu(w)^p,
 \qquad A_p=J_p+E_p.
 \end{aligned}                                                    \tag{1}
\]
The sums are real by conjugation. Set \(q_0=16/15\). The exterior
collar gives \(|\mu(w)|\le q_0 L^{-2}|w|^{-2}\). On
\(n\le|\Re w|<n+1\), \(n\ge1\), [Note41 §3][n41] bounds the complete
shell count by \(2C_{\rm u}(2L+\log(n+1))\), including both horizontal
directions. Since \(1-\kappa\) is supported in \(|\Re w|\ge1\),
\[
 \begin{aligned}
 |E_p|
 &\le 2C_{\rm u}q_0^p L^{-2p}
 \sum_{n\ge1}(2L+\log(n+1))\,n^{-2p}e^{-\alpha L^2 n^2}\\
 &\le 10 C_{\rm u}q_0^p L^{1-2p}e^{-\alpha L^2}.
 \end{aligned}                                                    \tag{2}
\]
Here the two shell sums with weights \(1,\log(n+1)\) are at most \(2,3\),
respectively, and \(L\ge3\). These are uniform absolute tail bounds
at fixed \(T\) on \(I\). Local continuity of finite zero multisets
then gives continuity of \(E_p\). In taking finite truncations for
continuity one can use local fixed zero-free boundaries, since the
uniform tail can be made arbitrarily small. The inner cutoff extends
the complementary test through target poles in the same way as in \(J_p\).

## 2. Complete force in a compact chart

At each reference time \(t_*\), choose fixed vertical boundaries
\(c(t_*)-b_-,c(t_*)+b_+\) with \(5/2<b_\pm<11/4\), free of zeros in
\(|\Im z|\le2\) at \(t_*\). Horizontal edges at \(\Im z=\pm2\) are
zero-free by the strip. The fixed rectangle stays zero-free on its
boundary locally in time, and the chart may be shrunk to
\(|c-c(t_*)|<1/4\). Its multiset \(\mathcal C\) contains the test
support and both target occurrences. It obeys \(|\Re(\rho-c)|<3\)
with \(N=\#\mathcal C\le N_0L,\ N_0=12C_{\rm u}\), by the six closed
unit intervals covering \([c-3,c+3]\). Outside the rectangle every
root has \(|\Re(\rho-c)|\ge 9/4\).

Put \(h_t(z)=H_z(t,z)/H(t,z)\). At \(z=c+x+iy\) with \(|x|\le2, |y|\le1\),
let \(s=c+x+4i\). The full exterior reciprocal field for this force
cluster is
\[
 \mathcal B_{\mathcal C}(z)=h_t(s)
       -\sum_{k\in\mathcal C}(s-\rho_k)^{-1}
       +\sum_{k\notin\mathcal C}
          \big[(z-\rho_k)^{-1}-(s-\rho_k)^{-1}\big].                 \tag{3}
\]
This is the safe-line subtraction of [Note40 (2)][n40]. In the
opposite-paired Hadamard convention, start with full cutoffs containing
\(\mathcal C\). Subtract at \(s\), remove \(\mathcal C\) as a finite
multiset, then pass to the absolute difference series. Thus even for
a nonsymmetric \(\mathcal C\), (3) retains the canonical exterior field
from both signs. The subtractions cancel the regularizers.
At a simple root in the support, the physical velocity equals
\(H_{zz}/H_z\), twice the constant term of \(h_t\) at that root.
By (3) it is
\(2\sum_{k\in\mathcal C,\,k\ne j}(\rho_j-\rho_k)^{-1}
 +2\mathcal B_{\mathcal C}(\rho_j)\).

The safe-line value in (3) costs at most \(2C_{\rm u}L\), and the
finite subtraction at most \(N/3\). For the difference series with
\(|\Re(\rho_k-c)|<4\), there are at most \(16C_{\rm u}L\) occurrences,
and each difference costs at most \(4+1/3\) by the horizontal padding
and safe-line clearance. For the remaining shells \(n\ge4\), both
denominators have modulus at least \(n-2\ge n/2\), and \(|s-z|\le5\).
The cost per occurrence is at most \(20/n^2\). The same shell sum as
in (2), now without its Gaussian, bounds their aggregate by
\(200C_{\rm u}L\). Hence
\[
 |\mathcal B_{\mathcal C}(z)|\le C_{\rm ext}L,\qquad
 C_{\rm ext}=280C_{\rm u}.                                         \tag{4}
\]
Only the differences in (3) were summed absolutely.

## 3. Symmetrization and uniform weak derivative

Identify a complex increment \(v\) with \(\mathbf v=(\Re v,\Im v)\).
Let \(\nabla\psi\) be the real-linear spatial derivative with values in
\(\mathbb C\), and evaluate \(\nabla\psi_j,\ \psi_{D,j}\) at
\((\rho_j-c,D)\). At a time when all chart roots are simple the
chain rule and (3) give \(J_p'=\mathcal L_p\), where
\[
 \begin{aligned}
 \mathcal L_p={}&2\sum_{j<k\in\mathcal C}
       (\nabla\psi_j-\nabla\psi_k)\,
          \mathbf{(\rho_j-\rho_k)^{-1}}\\
 &+2\sum_{j\ {\rm in\ test\ support}}
             \nabla\psi_j\,\mathbf{\mathcal B_{\mathcal C}(\rho_j)}
   -c'\sum_{j\in\mathcal C}\partial_x\psi_j
   +D'\sum_{j\in\mathcal C}\psi_{D,j}.
 \end{aligned}                                                    \tag{5}
\]
The inverse vector in the pair term has components
\((\Re(\rho_j-\rho_k),-\Im(\rho_j-\rho_k))/|\rho_j-\rho_k|^2\).
Targets have zero test derivatives but remain in the pair sum, since
they exert force on exterior occurrences. For clarity, with
\(W=e^{-\alpha |w|^2/\ell^2}\ell^{2p}/(w^2-D)^p\) and
\(\chi_w=\chi(|w|/r_0)\), the spatial derivative in (5) is
\(\kappa\chi_w\nabla W+\kappa W\nabla\chi_w+
 \chi_wW\kappa'(\Re w)(1,0)\) where the rational formula applies,
and vanishes in \(|w|\le r_0/3\). This includes both cutoff fluxes.
The inner-cutoff flux vanishes at all occurrences by the strict
separation of the transition annulus from the divisor. The bounds
use the full extended function on chords through that annulus.

For an explicit norm constant define
\[
 F_j=\sup_{\substack{u\in\mathbb C\\|\delta|\le d}}\|D_u^j f(u,\delta)\|
      \quad(j=0,1,2),\qquad
 F_\delta=\sup_{\substack{u\in\mathbb C\\|\delta|\le d}}
                   |\partial_\delta f(u,\delta)|.
\]
Use Euclidean operator norms, and modulus for \(F_0\).
These are finite by the extension and Gaussian decay. Set
\[
 G=F_1+\|\kappa'\|_\infty F_0,\qquad
 K_2=F_2+2\|\kappa'\|_\infty F_1+\|\kappa''\|_\infty F_0 .
\]
Then \(\|\nabla\psi\|_\infty\le LG\),
\(\|D_w^2\psi\|_\infty\le L^2K_2\) and
\(\|\psi_D\|_\infty\le L^2F_\delta\).
The gradient difference in (5) is bounded along the straight chord
by \(L^2K_2|\rho_j-\rho_k|\). The resulting pair summand has a
uniform bound even as its two endpoints approach a merger.

For the moving coordinates, [Note41 (3), §3][n41] gives
\[
 \begin{aligned}
 |c'|&\le 16 C_{\rm u}L^2/a+190 C_{\rm u}L\le C_cL^2,
   && C_c=C_{\rm u}(16/a+190),\\
 \dot\delta&=D'=2-4\delta m,\qquad
 |D'|\le2+4dB L,
   && m=\ell^2 S_1,\quad B=14C_{\rm u}q_0/a^2.
 \end{aligned}                                                    \tag{6}
\]
The center estimate uses the deflated field on \(|z-c|\le r_0/2\)
at the two target occurrences. It requires neither simple target
labels at an event nor an absolute first-power reciprocal sum.
Multiplying (5) by \(\ell^2\) and using (4), (6) gives
\[
 \begin{aligned}
 |\dot J_p|
 &\le N_0^2 K_2 L^2+2N_0 C_{\rm ext}G L
    +N_0 G C_c L^2+N_0F_\delta L(2+4dB L)\\
 &\le C_p L^2,\qquad
 C_p=N_0^2 K_2+
      N_0 G(2C_{\rm ext}+C_c)+N_0F_\delta(2+4dB).
 \end{aligned}                                                    \tag{7}
\]
The constant depends only on \(p,a,d,\alpha,C_{\rm u}\) and the fixed
cutoff choice. The bound is uniform in \(T\) and interval duration.

For assembly use [Note40 §2][n40] and its inherited
[TND-O Note19 §§2–4][hermite]. The latter gives the local
\(\rho_j(t_*+s)=\rho_*+\sqrt{2s}\,h_j+O(|s|)\) splitting in a disk that
exhausts the \(m\) occurrences of an \(m\)-fold zero, with distinct
Hermite roots \(h_j\). The leading separations dominate the error on
both available real sides. At \(s=0\) the isolating disk contains only
the one multiple point. Thus each multiple point is isolated in the
space-time multiple locus. In
\(I\times[T-3,2T+3]\times[-2,2]\) that locus is closed and compact.
It has finitely many points, hence finitely many event times, with
endpoint events covered by the available inward side. This fixed box
contains every chart force cluster.

Zero-free charts and continuity of finite zero multisets give
continuity of \(J_p\), including support crossings and events.
Between event times \(J_p\) is locally \(C^1\), by the simple-root
charts, and (7) bounds its derivative there. Finite-endpoint joins
using continuity preserve the same Lipschitz constant. In particular,
both physical and normalized time give absolute continuity. For any
\(\sigma_u\le\sigma_v\) in the scaled tube,
\[
 J_p(\sigma_v)-J_p(\sigma_u)
       =\int_{\sigma_u}^{\sigma_v}\ell^2\mathcal L_p\,d\sigma.
                                                                    \tag{8}
\]
The local formulas agree by the chain rule on overlaps. The
distributional derivative of \(J_p\) has the density in (8), hence
has no event atoms. The density can be assigned any values at the
finite event times.

## 4. Exact normalized radial forcing

Set \(\mathcal F_{\rm rad}=12A_2+16\delta A_3\),
\(\mathcal F_J=12J_2+16\delta J_3\), and
\(R=12E_2+16\delta E_3\). Equation (1) gives
\(\mathcal F_{\rm rad}=\mathcal F_J+R\) with
\[
 |R|\le C_{\rm u}\big(120q_0^2L^{-3}
                  +160d q_0^3 L^{-5}\big)e^{-\alpha L^2}.           \tag{9}
\]
For \(u\le v\) in normalized time the exact integrated law is
\[
 \mathcal F_{\rm rad}(v)-\mathcal F_{\rm rad}(u)
 =\int_u^v\!\big[
      12\ell^2\mathcal L_2+16\delta\ell^2\mathcal L_3
      +16(2-4\delta m)J_3\big]\,d\sigma +R(v)-R(u).                \tag{10}
\]
Equivalently, the weak derivative of \(\mathcal F_{\rm rad}-R\)
is the bracketed density. It is \(O(L^2)\) by (7), (6) and
\(|J_3|\le B_3 L,\ B_3=14C_{\rm u}q_0^3/a^6\) from Note41.
Formula (10) retains the full complementary increment. The estimates
here bound its size and give continuity, while the derivative
estimate is for the compact part.

If used in the physical Riccati identity [Note41 (13)][n41], let
\(U_p=\sum_{\rm exterior}(1-e^{-\alpha |w|^2/\ell^2})\mu(w)^p\).
The full forcing there is exactly
\(\mathcal F_J+R+12U_2+16\delta U_3\). Regularity gives no improved
signed forcing or adverse-cost rate here.

## 5. Premise replay and scope

The documentary screen in [E01][e01] and [Assessment19 §2][a19]
applies, with the following specific premise checks against
[Controls12][controls]. The compact test, pair symmetrization and
event assembly are structural and can apply to finite colliding
examples. No new control certificates were run.

| Control class | Canonical premise check |
| --- | --- |
| Quadratic and even quartic heat families | Complete theta arithmetic and growing zero population are absent. A finite divisor can satisfy a coarse upper count and the compact weak law, including at an exterior double. |
| Euler-factor translates | The normalized theta source changes, and the documented endpoint discrepancy fails. The coarse count upper bound alone cannot detect that discrepancy. |
| Endpoint-defective weighted-square, finite-source and finite-score changes | The full reflected theta source fails, as does the width-one strip for the documented defective classes. The finite measurements pay no common canonical count or safe line. |
| Finite-prime orbit changes | Full reflection and the unchanged source fail. Finite compatible measurements supply no uniform complete-field payment. |
| Reflected super-Gaussian | Order at most one fails for the documented source, leaving the canonical opposite-paired product passage unpaid. |
| Smooth shape and positive-primitive controls | The normalized theta arithmetic changes. Transfer of the complete strip, count and safe-line data is untested. |
| Fixed-event atoms and finite/compact-profile controls | The sources change, with canonical zero population and full profile growth absent in the stated control classes. |
| RH-conditional normalized endpoint mergers | Ordinary Dirichlet-series arithmetic changes, with RH in the construction. The compact law itself permits mergers. |
| Variable observation kernels and fractional-profile relaxations | The varied kernel lacks the physical cosine/Newman readout. The relaxed profile lacks the complete integer divisor needed by the force and the occurrence count. |
| Equal-count opposite-sign slices | Strip and upper-count forms may hold at a slice. These sources change and the examples do not supply a common canonical physical-time tube. |

The bound is for compact radial Gaussian moments on this independently
paid count-two tube, for either discriminant sign, including
multiplicities. The full uncut radial moments appear in (1) and (10).
This establishes the weak regularity requested by B03. Collision
exclusion and a canonical signed improvement remain open.

[request]: ../research-progress/handoffs/VCD-GT-GR-E08-r1.md
[decision]: ../brainstorm/notes/02_VCD_GT_GR_B03_RADIAL_WEAK_REPAIR_20261117.md
[e01]: ../reviews/02_VCD_GT_GR_E01_INPUT_AUDIT_20261117.md
[n40]: ../../notes/40_VCD_GT_E20_FIXED_COLLAR_TIME_OCCUPATION_20261117.md
[n41]: ../../notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md
[a19]: ../../reviews/19_VCD_GT_E22_FIXED_COLLAR_ASSESSMENT_20261117.md
[hermite]: ../../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/notes/19_TND_O_E12_COLLISION_STABLE_MOMENT_ASSEMBLY_20261107.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[classification]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
