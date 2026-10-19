# S03 opening: signed transport and the direct first jet

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual reasoning
effort ultra**, verified from the parent turn metadata. Parallel same-model
analysis and internal review; no independent specialist review.

The complete signed rotation-defect integral has an exact endpoint
primitive involving only the first jet. This removes a quadrature and
second-derivative payment when that primitive is used. It also exposes a
precise limitation: **the endpoint-envelope transport bound is dominated
by the direct first-jet radius bound**, when both use the same approximant,
phase, norm, and independently paid endpoint residuals. A smaller bound
using residual correlations can escape this limitation.

## Contract and prior work

This executes [S03's bounded task][s03] after reading the [program guide][guide],
repository [result summaries][summaries] and [patterns to avoid][avoid].
The relevant entries are [collision controls][controls], [local geometry][geometry],
[target reformulations][target], [scoped exclusions][scope], and
[preserving cancellation][cancellation]. The objective is a scoped comparison
of the specified transport estimate with direct first-jet exclusion on
`[1/100,1/5] x [999,1001]`. This is already covered by the prior complete-source
certificate. Agreement here is validation, not new coverage or a global
nonvanishing result.

[Note 07][n07], equations (7)–(12), already gives the rotation identity.
The [earlier collision manuscript][earlier], `sc:vector`, retains amplitude
drift; `prop:absmass` concerns its specified terminal-block absolute norm;
`sc:packet` concerns diagonal coercivity for adjacent packets; `lem:phase`
is a conditional error-paid phase test. Investigation 22's [marked Gauss
map][manifold] already retains signed angular information. These results
are prior work. The endpoint formula below is an elementary consequence
of Note 07, not a new arithmetic identity or a literature-priority claim.

Use exactly the [exterior contract's][outer] symmetric nonvanishing
normalizer `A`, phase `theta`, and `Q=H/A`. Put `omega=theta_x`,
`D_theta=omega^{-1} partial_x`, and keep its orientation. Use the complete
analytic S02 approximation `f=Fhat_8=(G_8-Chat_8)/A`, retaining all eight
modes and the entire signed correction. The [S02 proof][s02] supplies
`Q=f+r`, with real symmetry and `|r|<=eta` on every radius-`d=1/2` disk
centered on the real test box; `eta<0.226300`. Its imported approximation
theorem remains an accepted hypothesis here, with source and code pins
checked before use. No theta tail constant is assigned to an altered source.

The natural cutoff is 8 throughout the enclosing pilot rectangle; no
floor-defined cutoff is differentiated. The separate S02 cutoff-9 crossing
and removable-profile checks remain at their canonical source. This S03
comparison claims coverage only on its declared pilot interval.

## Complete signed primitive and stable evaluation

For any real `C^2` function `g`, define

\[
 W_g=g-i g_x/\omega,\qquad Z_g=e^{-i\theta}W_g,\qquad
 R_g=g+g_{xx}/\omega^2-\omega_xg_x/\omega^3.
\]

On an interval with nonzero omega, the chain rule gives

\[
 \partial_x Z_g=-i e^{-i\theta}\omega R_g,
 \qquad
 I_g(x):=\int_{\theta(x_0)}^{\theta(x)}e^{-is}R_g(s)\,ds
       =i\{Z_g(x)-Z_g(x_0)\}.                 \tag{1}
\]

The phase-coordinate integral uses the inverse of the prescribed monotone
phase at fixed t. Formula (1) is valid in either orientation and at a
candidate first-jet zero. It does not divide by the unknown jet.
Endpoint evaluation makes the quadrature error exactly zero. Interval
evaluation error, phase uncertainty, and coverage between endpoints remain
to be paid; evaluation at only the two outer endpoints would not do that.

For stable arithmetic evaluation on the real axis write
`F_N=e^{i theta}P+e^{-i theta} conjugate(P)`, with `P=sum_{n<=N} w_n(s)`.
Direct differentiation, including amplitude drift, gives

\[
 Z_{F_N}=2P-\frac{i}{\omega}
       \{P_x+e^{-2i\theta}\overline{P_x}\}.             \tag{2}
\]

For `k=Chat_N/A`, subtract `e^{-i theta}(k-i k_x/omega)` from (2).
The first mode has `P_1=1`, `P_{1,x}=0`, so its contribution is exactly
2 and cancels algebraically in `Z_f(x)-Z_f(x0)`. Combine the remaining
signed contributions before taking a norm. The conjugations in (2) are
real-axis identities; analytic derivatives come from the fixed holomorphic
formula. The checker also checks against the original formula directly.

## Residual payments, including a joint disk bound

Separate Cauchy bounds, using real symmetry at each real center, give

\[
 |W_r|\le e_C:=\eta\sqrt{1+(d|\omega|)^{-2}}.           \tag{3}
\]

This is conservative. A joint bound follows from the same disk contract,
without importing a new theta estimate:

\[
 \boxed{|W_r|\le e_J:=\eta\max\{1,(d|\omega|)^{-1}\}.} \tag{4}
\]

To prove it, set `h(z)=r(x+dz)/eta`, so `h(0)=a` is real, `|a|<=1`.
For `|a|<1`, the disk automorphism `(h-a)/(1-a h)` vanishes at zero
and is bounded by one. Schwarz's lemma, or Cauchy's inequality after
dividing by z on disks increasing to the unit disk, gives
`|h'(0)|<=1-a^2`. Boundary equality `|a|=1` makes h constant by the
maximum modulus principle. With `v=a^2` and `b=(d|omega|)^{-1}`,

\[
 |W_r|^2/\eta^2\le v+b^2(1-v)^2
       \le\max\{1,b^2\},\quad 0\le v\le1,
\]

because this quadratic is convex. Constants and a linear disk map show
the two endpoint optima for this centered real-symmetric disk class.
This does not assert optimality for the actual theta residual or its
overlapping disks. For a general complex residual the real orthogonality
used in (3)–(4) is unavailable.

Either valid first-jet envelope `e(x)` gives, by (1),

\[
 |I_r(x)|\le e(x)+e(x_0).                              \tag{5}
\]

This is an independent endpoint triangle payment, not a bound exploiting
correlation of the residuals. Compare the second-derivative route from
Note 07, which pays

\[
 B_D\le |x-x_0|\eta\left\{\Omega_*+
 \frac{2}{d^2\omega_*}+\frac{\Omega_{1,*}}{d\omega_*^2}\right\},
 \quad |\omega|\in[\omega_*,\Omega_*],\quad
 |\omega_x|\le\Omega_{1,*}.                            \tag{6}
\]

Here `|ds|=|omega|dx` is included. A smaller bound for the complete
signed `I_r`, proved by additional arithmetic or residual correlation,
would be a different estimate and could improve on (5).

## Scoped comparison theorem

Suppose `|W_Q(x0)|>=m0` is certified and `|W_r(y)|<=e(y)` at both
endpoints. Transport with (5) gives the radius lower bound

\[
 L_T(x)=m_0-|Z_f(x)-Z_f(x_0)|-e(x_0)-e(x).
\]

For the exact finite approximant values,

\[
 \boxed{L_T(x)\le |W_f(x)|-e(x)=:L_{\rm direct}(x).}     \tag{7}
\]

Indeed `m0<=|W_Q(x0)|<=|W_f(x0)|+e(x0)`. Substitute this upper bound
and apply `|Z_f(x0)|-|Z_f(x)-Z_f(x0)|<=|Z_f(x)|=|W_f(x)|`.
Thus this scalar transport test cannot certify a point that the ideal
same-approximant direct radius test fails to certify. Finite interval
implementations can still have different enclosure widths or costs; (7)
does not compare those operational costs. An independently tighter anchor
can improve the computed transport bound, while (7) still holds.

This exclusion is restricted to the same phase, norm, approximant and
independent endpoint envelopes in (5). It excludes neither S03 as a whole,
nor direction-sensitive vector enclosures, correlated residual estimates,
nor long-interval evaluation methods with a separately measured cost gain.

## Bounded comparison and decision

The [192-bit run][r192] and [256-bit replay][r256] use python-flint 0.9.0,
outward Arb/Acb arithmetic, and the same closed rational cover: 32 time
slabs of width `19/3200`, each with 128 spatial cells of width `1/64`.
There are 4,096 cells, including all boundaries. At each fixed time the
anchor is `x0=999`. The entire phase enclosure is contained in
`[-848.206,-845.838]`, with omega negative on every cell, and

\[
 1.093934<|\omega|<1.094473,\quad
 |\omega_x|<0.000250249,\quad |(\log A)_x|<0.390946.
\]

The code retains direct whole-cell enclosures and also propagates the
signed spatial midpoint value across each same cell. If its half-width is
h, the exact identities `Z_f,x=-i e^{-i theta} omega R_f` and
`W_f,x=i omega(W_f-R_f)` give variation payments
`h sup|omega| sup|R_f|` and
`h sup|omega|(sup|W_f|+sup|R_f|)` respectively. Every supremum encloses
the complete analytic expression on the whole closed cell. This is a
finite-expression second-derivative calculation, not a second-derivative
payment for the unknown residual. Time variation is already included by
interval evaluation on each closed time slab. No quadrature, additional
mode truncation, or source integration is introduced. Rounding is included
by the ball arithmetic; there is no separate floating error omitted.

| Paid quantity or lower bound | Certified descriptive value |
| --- | ---: |
| Complete signed integral modulus supremum, retaining all modes and correction | `<2.216523` |
| Approximant anchor radius, uniformly in time | `>3.113757` |
| Separate Cauchy first-jet residual `e_C` | `<0.471581` |
| Joint disk first-jet residual `e_J` | `<0.413735` |
| Direct normalized jet radius lower, separate Cauchy / joint disk | `>0.909445` / `>0.967290` |
| Residual integral via (6), full length two | `<3.805423` |
| Residual integral via independent endpoints, Cauchy / joint | `<0.943161` / `<0.827470` |
| Whole-box transport lower, Cauchy defect route | approximately `-3.151345` |
| Whole-box transport lower, endpoint Cauchy / joint | approximately `-0.289082` / `-0.115546` |

The table's rounded negative numbers describe computed lower bounds.
A negative lower bound alone would not prove the physical quantity or an
ideal estimate negative. There is a separate point witness for the
**specified uniform Cauchy payment rules**, at `t=1/100`, `x=1001`:

\[
 |W_f(999)|\approx3.426361079,\quad
 |I_f(1001)|\approx2.062384362,
\]
\[
 |W_f(999)|-|I_f(1001)|-e_C-B_D<-2.913026,
 \qquad |W_f(999)|-|I_f(1001)|-3e_C<-0.050763.
\]

Thus those conservative declared rules cannot give a positive uniform
certificate. The joint-disk refinement was derived during opening review;
it was not the original separate-Cauchy payment. Its point slack is
positive, `>0.122772`, while its fixed-cover whole-box lower bound is
negative. **That sharper whole-box propagation attempt is inconclusive.**
The witness does not refute it, and no extra grid scan was launched to
obtain a pass. Equation (7) still proves its intrinsic scalar lower bound
cannot exceed the ideal direct test with the same joint endpoint errors.

The declared scoped-comparison gate passes: it supplies the proof (7),
the specific Cauchy-payment witness, and a complete paid direct reference.
There is no propagation advantage, new covered region, or performance
milestone. The successful direct calculation uses the same midcell
propagation machinery for a fair enclosure comparison. Setup and replay
each take a few seconds in this environment; these descriptive costs are
recorded, not a matched performance claim.

The next useful S03 input must reduce the complete signed residual integral
using correlations, or supply a measured evaluation advantage over direct
jets. An oscillator residual example below shows what information (5)
loses. Do not enlarge a height scan merely to recheck existing exclusion.
The real bridge `(1001,exp(2000))` and the global complex exterior remain
open. No manuscript or snapshot is created by this round.

## Physical return and controls

With `a=(log A)_x` and `J=(Q,-Q_x/omega)`,

\[
 E=A^2J^\mathsf TMJ,\qquad
 M=\begin{pmatrix}1+a^2&-a\omega\\-a\omega&\omega^2\end{pmatrix},
 \qquad \lambda_{\min}(M)\ge
 \frac{\omega^2}{1+a^2+\omega^2}.                       \tag{8}
\]

The inequality follows from positive determinant `omega^2` and the
trace bound for the larger eigenvalue. A paid radius `|W_Q|>=m>0`
therefore gives `sqrt(E)/A >=omega_* m/sqrt(1+B^2+Omega_*^2)` when
`|a|<=B`. Normalized radii are never identified with physical energies.

Three generic diagnostic controls delimit the method:

- For `Q=c!=0`, `theta=x`, the direct radius is `|c|` but
  `|I_Q|=2|c sin((x-x0)/2)|`. The strict single-anchor scalar test already
  fails at phase distance `pi/3`. This is conservatism of that test on
  the stated `C^2` class, not a theta counterexample.
- The backward-heat polynomial `H=x^2-2(t-tc)`, `A=1`, `theta=x`,
  has a double event at `(tc,0)`. From anchor 1 at the event time,
  `|I_H(0)|=|W_H(1)|=sqrt(5)`. A strict propagation test must reject it.
- For `r=c cos(theta)`, `R_r=0` and the exact integrated residual is
  zero, while the independent endpoint allowance is positive. This is
  an explicit reason to retain the scope qualifier in (7).

The [fresh source-specific control replay][control-record] also rejects
the five existing event boxes and the separate Euler negative-Laguerre
witness using their own source errors. This is an interface check, not
a new S03 certificate for those sources. Finite-prime and finite-square
controls fail full normalized theta reflection/coefficient data; reflected,
smooth-shape and primitive controls fail the unchanged theta square series;
Euler controls fail level-one coefficient data; polynomial/counter-kernels
fail the exact theta source; auxiliary smooth-density and two-channel
constructions lack the required complete physical-observation comparison.
All share (1). At a genuine event the integral cancels the anchor exactly,
so every valid strict smaller-than-anchor test fails there. See the
[control summary][controls] for the different premise scopes and which
families have effective event boxes.

[s03]: ../README.md
[guide]: ../../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[target]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[cancellation]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[n07]: ../../../notes/07_HODGE_MODULAR_DUALITY_AND_ROTATION_DEFECT_20261018.md
[earlier]: ../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[manifold]: ../../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[outer]: ../../../manuscript/positive_arithmetic_packets/sections/10_outer_exclusion.tex
[s02]: ../../02_cutoff_reflection/notes/01_ANALYTIC_CUTOFF_CORRECTION_AND_COMPLETE_JET_ERRORS_20261018.md
[control-record]: ../numerics/S03_CONTROLS_20261018.json
[r192]: ../numerics/S03_ROTATION_192_20261018.json
[r256]: ../numerics/S03_ROTATION_256_20261018.json
