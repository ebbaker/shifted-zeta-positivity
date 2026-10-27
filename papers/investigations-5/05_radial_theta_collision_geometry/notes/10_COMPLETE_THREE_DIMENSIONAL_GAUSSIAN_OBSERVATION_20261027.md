# A complete three-dimensional Gaussian observation for H(t,z)

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Conversation: **Continue higher-dimensional H-rep**, Investigation05 chat0003, thread `01a17f2b-8196-7683-ab85-434b4bd2ac20`.

**Status: exact representation and convergence proved in-note; same-assistant checks and self-review.** This completes the first task in [Note09](09_SIMPLER_HIGHER_DIMENSIONAL_H_REPRESENTATION_CONTINUATION_20261027.md): a native rank-three Gaussian sum and a genuine three-dimensional integral now recover the complete H, for every finite complex t,z. Two Gaussian channels, a parity character, a cosine plane wave, one elementary correction, and the completion boundary constant remain. This is a concrete baseline for simplifying the full system, not a claim that it is optimal or a new zero estimate.

The substantive step is to remove the two lattice sites lying on an observation sphere **before** the scale integral, and to integrate their contribution exactly. The remaining lattice is separated from the sphere by a positive distance. This turns the finite two-scale recovery of Note08 into an absolutely convergent scale-and-angle integral, even at positive Newman time.

Read the [result index](../../../../result-summaries/README.md), especially [theta identities](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [hypercomplex results](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md), and [controls](../../../../result-summaries/12_collision_controls_and_screening.md), together with the [avoid index](../../../../avoid/README.md), [coordinate lifts](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [target classification](../../../../avoid/01_restating_the_target.md). The user has explicitly selected representation as the present objective. No RH-equivalent sign criterion is proposed or numerically supported.

## 1. Independently specified lattice field

Let

\[
 C=(1,0,0)+2\mathbb Z^3,\qquad
 \chi(v)=(-1)^{v_3/2},\qquad e_1=(1,0,0),
 \qquad d\sigma(\omega)=\frac{dS(\omega)}{4\pi}.
\]

For r>=1 and omega on the unit sphere define

\[
 T(r,\omega)=\sum_{v\in C}\chi(v)
      e^{-\pi r^2|v|^2}\cos\!\left(\frac\pi2 v\cdot\omega\right),
\tag{1}
\]
\[
 D(r,\omega)=\sum_{v\in C\setminus\{e_1,-e_1\}}
       \chi(v)e^{-\pi r^2|v-\omega|^2/4},
\tag{2}
\]
\[
 \boxed{F(r,\omega)=\frac\pi2T(r,\omega)
             +\frac{\pi r^2}{4}D(r,\omega)
             -\frac12e^{-\pi r^2}.}
\tag{3}
\]

These definitions use only a fixed lattice coset, an elementary character, ordinary Gaussian kernels and a plane wave. They do not use A, Phi, H, their coefficients, or their zeros as input. The constant correction is independent of omega, but the two infinite fields have genuine angular dependence; the sphere is not an appended normalized factor.

The key identity, proved below, is

\[
 \boxed{\int_{S^2}F(r,\omega)\,d\sigma(\omega)
       =\sum_{n\ge1}e^{-\pi r^2 n^2}=A(r).}
\tag{4}
\]

All three lattice coordinates contribute. As in Note08, the signed shell at squared radius 9 has coefficient -6, of which only +2 comes from the axial points. Deleting the transverse sites changes the answer.

## 2. The complete H formula

Set r=e^(2u) and define the observation

\[
 W_{t,z}(u)=(\partial_u^2-1)
                  \{e^{tu^2}\cos(zu)\}
\]
\[
 =e^{tu^2}\left[
 (2t+4t^2u^2-z^2-1)\cos(zu)-4tuz\sin(zu)\right].
\tag{5}
\]

Then

\[
 \boxed{
 H(t,z)=\frac1{16}+\frac18
  \int_{[0,\infty)\times S^2}
  e^u F(e^{2u},\omega)W_{t,z}(u)\,du\,d\sigma(\omega).
 }
\tag{6}
\]

This is an ordinary absolutely convergent integral on a three-dimensional cylinder with boundary. The discrete dimension is also three. There is no extra scale sum or uncounted integration variable. Formula (6) includes the whole H, rather than just the odd theta sector or a primitive with unrelated zeros.

At t=0 it becomes

\[
 H(0,z)=\frac1{16}-\frac{1+z^2}{8}
  \int_{[0,\infty)\times S^2}
  e^u F(e^{2u},\omega)\cos(zu)\,du\,d\sigma(\omega).
\tag{7}
\]

For general time, (5) is the full cost of transferring completion to the observation. Equivalently one may first form the primitive integral J and use Note01's second-order frequency reconstruction; neither convention removes those terms.

**Parameter dictionary.** u is a logarithmic scale, omega is the actual direction on a unit sphere, and v is an independent lattice label. The damping parameter in both (1) and (2) is r²=e^(4u), with different Gaussian distances. Newman time is t in (5), not r². Since

\[
 (\partial_t+\partial_z^2)W_{t,z}=0,
\]

and the same is true of the constant in (6), differentiation proves H_t=-H_zz. All finite parameter derivatives are legitimate by Section 4. In particular, (6) is valid on all of C², not only at t=0 or in a small real-time interval.

## 3. Proof of the angular identity and the two-site correction

The signed shell identity already proved in [Note08](08_GENUINE_THREE_DIMENSIONAL_LATTICE_SUMS_AND_THETA_RECOVERY_20261027.md) is

\[
 \sum_{\substack{v\in C\\|v|^2=N}}\chi(v)
 =\begin{cases}2n\chi_4(n),&N=n^2,\ n>0\text{ odd},\\0,&\text{otherwise},\end{cases}
\tag{8}
\]

with chi_4(n)=(-1)^((n-1)/2). Its infinite proof uses Jacobi's derivative identity, not a finite enumeration. The classical input and its normalization are retained in [reference06](../references/06_QUATERNION_LATTICES_AND_COMPLETE_OBSERVATION_20261027.md).

The normalized angular mean of cos(pi v dot omega/2) is sinc(pi |v|/2). Thus

\[
 \frac\pi4\int T(r,\omega)d\sigma(\omega)=P(r),
 \qquad P(r)=\sum_{n>0\text{ odd}}e^{-\pi r^2n^2}.
\tag{9}
\]

For a vector of length R>0, direct integration in its polar axis gives

\[
 \int_{S^2}e^{-\pi r^2|v-\omega|^2/4}d\sigma(\omega)
 =\frac{e^{-\pi r^2(R-1)^2/4}-e^{-\pi r^2(R+1)^2/4}}
        {\pi r^2R}.
\tag{10}
\]

Initially include all sites in the second sum and multiply (10) by pi r²/4. Applying (8) makes its angular integral

\[
 \frac12\sum_{j\ge0}(-1)^j
       \left[e^{-\pi r^2j^2}-e^{-\pi r^2(j+1)^2}\right]
 =\frac12+\sum_{n\ge1}(-1)^n e^{-\pi r^2n^2}.
\tag{11}
\]

The two unit sites have total contribution

\[
 \frac{\pi r^2}{4}\int_{S^2}
 \left(e^{-\pi r^2|e_1-\omega|^2/4}
       +e^{-\pi r^2|-e_1-\omega|^2/4}\right)d\sigma
 =\frac12(1-e^{-\pi r^2}).
\tag{12}
\]

Removing precisely these sites from (11) proves

\[
 \frac{\pi r^2}{4}\int D\,d\sigma
 =\sum_{n\ge1}(-1)^n e^{-\pi r^2n^2}
       +\frac12e^{-\pi r^2}.
\tag{13}
\]

Equations (9), (13), and the final term in (3) give (4), since twice the odd sector plus the alternating full sector has coefficient one at every positive integer square.

This proof avoids relying on an uncomputed off-sphere modular transformation. For comparison, Poisson summation of Note08's inverse-scale heat field produces the Gaussian in (2), after interchanging the first and third coordinate axes. Equations (11)-(12) are the explicit resolution of its two touching image sites. The new correction -exp(-pi r²)/2, rather than -1/2, is forced by that integration.

To finish the proof of (6), let psi(u)=e^u A(e^(2u)). The inherited canonical normalization is Phi=(psi''-psi)/8. Theta reflection gives psi'(0)=-1/2. With w=e^(tu²)cos(zu), w(0)=1 and w'(0)=0. Twice integrating by parts gives

\[
 8H=\frac12+\int_0^\infty\psi(u)(w''(u)-w(u))du.
\tag{14}
\]

The upper endpoints vanish. Substituting (4) yields (6). No endpoint or contact term is dropped.

## 4. Absolute convergence, and why the subtraction matters

The only points of C on the unit sphere are +/-e_1. Every remaining site has |v|>=sqrt(5), so

\[
 |v-\omega|\ge\sqrt5-1,\qquad
 \kappa=\frac\pi4(\sqrt5-1)^2>0.
\tag{15}
\]

For r>=1, the absolutely summed second field is bounded by

\[
 \sum_{v\ne\pm e_1}e^{-\pi r^2|v-\omega|^2/4}
 \le C e^{-\kappa(r^2-1)},
\tag{16}
\]

uniformly in omega. Indeed, split r²=(r²-1)+1, use the distance gap for the first factor, and bound the remaining sum by the finite sum of exp[-pi(|v|-1)²/4]. The first field is bounded in absolute sum by C exp[-pi(r²-1)]. Hence

\[
 |F(r,\omega)|\le C'(1+r^2)e^{-\kappa r^2}.
\tag{17}
\]

Finite scale derivatives introduce only polynomial factors in r and the lattice coordinates; reserving half the Gaussian exponent gives the same type of bound with a smaller positive constant. Since r²=e^(4u), these estimates dominate exp(Tu²+Zu) times every fixed power of u, uniformly on compact complex t,z sets. They justify lattice/angle/scale interchanges, both integrations by parts, parameter differentiation and joint entire dependence.

Leaving the two unit-site Gaussians inside D gives an angular mass tending to 1/2 after multiplication by pi r²/4, as (12) shows. Its cancellation against a constant occurs only after the angular integration; it cannot be treated as a separate absolutely integrable channel under the growing scale weight. For example, at t=z=0 the absolute scale integral of that positive channel already grows like integral e^u du. The exact subtraction in (12) repairs this issue. This is a scoped failure of the uncombined channels, not a prohibition on iterated or suitably renormalized formulas.

## 5. Complexity and relation to quaternionic proposals

The representation has met both dimensional requirements of Note09. Compared with the original source summand, it removes the n^4/n^2 polynomial and puts only elementary Gaussians in the lattice fields. Compared with directly inserting Note08's inverse-scale recovery, it supplies an ordinary all-time convergent integral and the explicit cancellation needed for it.

Its costs remain substantial: two fields, a parity character, a selected unit sphere, an oscillating plane wave, the lower boundary, and a second-order observation. The signed angular field is not asserted nonnegative. The identity is not a new arithmetic inequality, and no evaluation-speed advantage is claimed.

Identifying v with v_1 i+v_2 j+v_3 k writes C as a coset in the imaginary Lipschitz lattice, |v-omega|² as a quaternion norm and v dot omega as -Re(v omega). This does **not** itself add a quaternionic theorem. The separate [Note11](11_HURWITZ_HOPF_AND_UNIT_QUATERNION_HEAT_REPRESENTATIONS_20261027.md) investigates the Hurwitz order, a genuinely quadratic Hopf map, and the unit-quaternion sphere, instead of counting a change of notation as another construction.

## 6. Controls, verification and next task

No collision mechanism is asserted. The [control register](../../../../result-summaries/12_collision_controls_and_screening.md) still blocks inferences from Gaussian kernels, positivity of A or an auxiliary heat operator alone. Euler-factor controls change the canonical source/conductor; weighted-square controls change the coefficients in the complete shell identity and fail full reflection; reflected smooth and primitive-compatible controls lack the unchanged integer-square arithmetic. This formula specifies that arithmetic exactly but does not prove an inequality which separates the physical observation from those controls. Their event certificates are not rerun for an identity with no exclusion claim.

The [checker](../numerics/09_check_complete_lattice_and_quaternions_20261027.py) enumerates the signed coset through squared radius 225 and verifies the two nearest sites and next squared radius 5 exactly. It separately compares direct three-dimensional quadrature, analytically averaged raw lattice sums, the original canonical source, and Note11's sphere trace formula at five parameter pairs, including positive, negative and complex time. Two angular/scale grids are recorded in the [execution record](../numerics/09_COMPLETE_LATTICE_AND_QUATERNION_CHECKS_20261027.json). The largest fine-grid absolute discrepancy for (6) is below 1.6e-15. These are floating normalization diagnostics, **not interval-certified error bounds**. The infinite claims follow from (8)-(17), not numerical agreement. The [self-review](../reviews/06_COMPLETE_OBSERVATION_AND_QUATERNION_SELF_REVIEW_20261027.md) is by the same assistant.

The next useful comparison is now concrete: can the unit-quaternion local heat construction of Note11 supply an equally explicit three-dimensional observation with fewer completion operations, without adding spectator angles or hiding the scale integral? Alternatively, can a natural quaternionic projector replace Note11's Möbius correction? Keep the present two-channel formula as the fully specified comparator. Do not begin an unbounded search over lattices or infer a sign from the geometric form.
