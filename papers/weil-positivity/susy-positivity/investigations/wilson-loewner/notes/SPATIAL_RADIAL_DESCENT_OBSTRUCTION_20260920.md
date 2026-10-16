# Spatial radial evolution does not descend to the fixed Higgs hemisphere sector

Date: 20 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; identity supplied by the session instructions).
Effort setting: not exposed in this session; not inferred.
Status: a scoped analytical obstruction and a free observable calculation,
with reproducible algebraic and floating-point checks. Specialist review
outstanding. No manuscript revision or arithmetic positivity claim.

## Result

**Ordinary spatial dilation does not act on the full fixed-supercharge
cohomology represented by the selected hemisphere wavefunctions.** A
protected scalar inserted away from the radial origin gives an explicit
counterexample: its dilated image has a nonzero fermionic supersymmetry
variation. The same failure occurs for a neutral, separated two-scalar
insertion. Thus the free radial generator with one-particle rates
`ell+1/2` does not induce the boundary-field Mellin generator in this
representation. This test determines **no affine dictionary between the
spatial Laplace variable p and s = 1/2 - i sigma**.

An R-symmetry compensation repairs closure, but changes the generator to a
twisted dilation which is trivial in the relevant local-operator cohomology.
Changing the supercharge and boundary data with the scale is another
possibility, requiring intertwiners between different complexes. Neither
operation is ordinary radial evolution on the fixed representation.

The simplest massless free open-arc control nevertheless has a definite
state at the fixed hemisphere:

\[
 \Psi_{\rm pair}(Y,\bar Y)=Y\bar Y\Psi_0
 =\epsilon x\Psi_0,\qquad
 \widehat\Psi_{\rm pair}(\sigma,B)
 =\frac{\epsilon\delta_{B,0}}{\sqrt{2\pi}}\Gamma(s+1),
 \quad \epsilon=(4\pi r)^{-1},\quad x=|Y|^2/\epsilon.
 \tag{1}
\]

Here transport is the identity. The only ordering contact is fixed by the
free canonical commutator. No extra current or polynomial is selected.
Equation (1) is a boundary amplitude, with no derived spatial spectral
interpretation. Comparison with the complete prime-free arithmetic factor
therefore stops before a spectral identification; the earlier conditional
polynomial-degree obstruction is not promoted to a universal one.

## 1. Inputs, conventions, and the different radial variables

Read first in this session: the
[predictive hemisphere note](PREDICTIVE_LOCALIZATION_HEMISPHERE_TEST_20260920.md)
and its [handoff](RESEARCH_CONTINUATION_AFTER_LOCALIZATION_TEST_20260920.md).
The current version 0.4 main and supplementary sources were consulted,
including the free kernel, endpoint supersymmetry, fixed-window response,
and localization sections. Their historical claims and snapshots are
unchanged. The input hashes are recorded separately.

The external physical inputs are the free hypermultiplet action and Higgs
charge/twist in [D, (2.8)–(2.10), (3.1)–(3.10), (C.7), (C.13)], and the
boundary polarization, vacuum, and operator actions in [G, §§4.2, 4.3.2].
Both primary references were inspected directly. The calculations below
apply these inputs; they do not recompute a localization determinant.

| Symbol | Meaning |
|---|---|
| `rho`, `u = log(rho/rho_*)` | Spatial radius and dimensionless spatial cylinder time |
| `r` | Fixed round-three-sphere radius in the localization problem |
| `t` | Signed spatial coordinate on the protected diameter; `rho = abs(t)` there |
| `Y`, `x = 4 pi r abs(Y)^2` | Boundary field and its dimensionless squared magnitude |
| `ell`, `m` | Spatial spherical-harmonic degree and magnetic label, with multiplicity `2 ell+1` |
| `d`, `k` | Total degree in `Y,bar Y`, and degree in `x` for a neutral monomial (`d=2k`) |
| `B` | Fourier label of the phase of `Y`; the mirror description calls it flux |
| `sigma`, `s = 1/2-i sigma` | Spectral variable of field-magnitude dilations and Mellin exponent |
| `p`, `omega` | Arithmetic spatial Laplace variable and arithmetic shift; neither is identified with a localization parameter |

In particular, neither the spatial coordinate `t` nor the sphere radius `r`
is the Mellin integration variable. We use `mathcal Q` for supersymmetry
and `Q,tilde Q` for protected scalar operators.

For the unprotected free scalar, the Weyl rescaling
`phi(u,Omega)=rho^(1/2) q(rho Omega)` takes flat space to the unit cylinder.
The conformal curvature term is `R_cyl/8=1/4`, so its quadratic operator is

\[
 -\partial_u^2-\Delta_{S^2}+\tfrac14,
 \qquad H_1=\sqrt{-\Delta_{S^2}+\tfrac14},
 \qquad H_1Y_{\ell m}=(\ell+\tfrac12)Y_{\ell m}.
 \tag{2}
\]

The full radial Hamiltonian `D` is the conformal dilation generator, with
vacuum energy subtracted; (2) gives its scalar one-particle energies. It
acts on a dimension-one-half scalar by
`[D,q(X)]=(X dot partial+1/2)q(X)`. Positive Euclidean propagation uses
`exp(-a D)`. With the manuscript's covariance normalization,

\[
 C(u,v)=[2(\cosh u-v)]^{-1/2}
 =\sum_{\ell\geq0}e^{-(\ell+1/2)|u|}P_\ell(v).
 \tag{3}
\]

The physical action normalization adds `1/(4 pi)` to this covariance.
Even angular smearing samples `ell=2n`; it does not change the field's
Hilbert space into one oscillator per even degree. None of these facts
identifies `ell` with a boundary polynomial degree.

## 2. The chosen boundary and a compatible radial center

Keep exactly the boundary polarization of the earlier note:

\[
 q_1|=Y,\quad\widetilde q_2|=\bar Y,\quad
 G|=-iY/(2r),\quad\bar G|=i\bar Y/(2r),
 \tag{4}
\]

with its fermionic completion. In the free theory the first auxiliary
condition means `partial_perp q_2|=-Y/(2r)`. It is not zero Neumann data.
The localizing charge is
`mathcal Q = Q_1^+ + Q_2^- = mathcal Q_1^H + mathcal Q_2^H`.
The fixed-sector cohomology is taken on the invariant subspace of
`mathcal Q^2`.

There is a geometrical subtlety in using a flat-space dilation. In [G] the
cut is at great-circle angles `varphi=0,pi`; the retained arc is
`0<varphi<pi`. The usual [D] stereographic coordinate
`z=2r tan(varphi/2)` puts its origin at one end of this arc. Dilation about
that point is not the concentric-sphere quantization of this hemisphere.

For concentric radial slices, stereographically project from the antipode
of the hemisphere center `varphi=pi/2`. On the protected diameter this gives

\[
 t=2r\tan\frac{\varphi-\pi/2}{2},\qquad -2r<t<2r.
 \tag{5}
\]

The hemisphere becomes the ball of radius `2r`. Its Weyl factor is
`Omega=(1+rho^2/(4r^2))^(-1)`. The sphere polarization
`(cos(varphi/2),sin(varphi/2))`, divided by `sqrt(Omega)` on this
diameter, becomes

\[
 u_{\rm flat}(t)=\frac1{\sqrt2}
 (1-t/(2r),\ 1+t/(2r)).
 \tag{6}
\]

A constant change of field basis
`q'_1=(q_1+q_2)/sqrt(2)`, `q'_2=(-q_1+q_2)/sqrt(2)` therefore writes
the protected flat scalar as

\[
 {\cal O}(t)=q'_1(t)+\frac{t}{2r}q'_2(t).
 \tag{7}
\]

This is a passive description of the same hemisphere and charge, not a
replacement of (4) by Dirichlet conditions on `q'_1`. Below the primes
are suppressed only in the local flat-frame calculation. Formula (6)
also allows that calculation to be checked without changing the H basis.
The obstruction thus applies to the radial center appropriate to the
selected boundary, not merely to the original stereographic origin.

## 3. Explicit failure of descent

For a fixed complex `(ker mathcal Q)/(im mathcal Q)`, descent of an actual
evolution requires it to preserve closed representatives and their
equivalence. A nonzero commutator alone would not suffice to disprove
this: for example, `[D,mathcal Q]=c mathcal Q` would preserve both.
Here there is a direct counterexample.

First, in the standard flat frame the charge is a sum of Poincare and
conformal pieces `mathcal Q=P+(2r)^(-1) S`. Their dilation weights are
`+1/2` and `-1/2`, respectively. Thus

\[
 [D,\mathcal Q]=\tfrac12P-\frac1{4r}S,
 \tag{8}
\]

which is not proportional to `mathcal Q`. This is a warning, not the
proof. A conformal frame change conjugates this test; the following
calculation uses the centered frame (5) directly.

The free scalar variations and the protected polarization (7) give

\[
 \mathcal Q q_2(t)=\chi(t),\qquad
 \mathcal Q q_1(t)=-\frac{t}{2r}\chi(t),\qquad
 \mathcal Q {\cal O}(t)=0.
 \tag{9}
\]

Here `chi` denotes the nonzero linear combination of free fermions in
`mathcal Q q_2`; its overall convention is immaterial. Its nonvanishing
is substantive: the Poincare part acts on this component, and the two
terms in `mathcal Q_1^H+mathcal Q_2^H` involve independent fermion
components. There is one scalar polarization kernel, not a charge
annihilating the whole hypermultiplet doublet. Equation (9) follows
equivalently by inserting the affine conformal Killing spinor in
`delta q=xi psi` and using the annihilating row `(-t/(2r),1)`.

Ordinary dilation acts on the fields, keeping the coefficient of the
specified insertion fixed. Consequently

\[
 [D,{\cal O}(t)]
 =(t\partial_t+\tfrac12){\cal O}(t)-\frac{t}{2r}q_2(t),
 \qquad
 \boxed{\ \mathcal Q[D,{\cal O}(t)]
 =-\frac{t}{2r}\chi(t)\ne0\quad(t\ne0).\ }
 \tag{10}
\]

The derivative in the first term differentiates the *whole protected
family*, including its position-dependent polarization. Omitting the
last term would silently add a change of the observable.

The finite calculation is equally explicit. For `a` sufficiently small
to keep the insertion inside the ball,

\[
 e^{aD}{\cal O}(t)e^{-aD}
 =e^{a/2}\left\{{\cal O}(e^at)
       +(1-e^a)\frac{t}{2r}q_2(e^at)\right\},
 \tag{11}
\]

whose supersymmetry variation is
`e^(a/2)(1-e^a)t chi(e^a t)/(2r)`. Replacing `a` by `-a` gives the same
failure for the Euclidean propagation convention. In the original H
basis (6), the determinant between the old polarization and the one
required at `e^a t` is proportional to `(1-e^a)t/r`, again nonzero.

This is also a boundary-state counterexample. Insert (7) inside the
empty hemisphere, which creates the conformal vacuum. It gives a
`mathcal Q`-closed state in the domain of boundary localization. Since
the vacuum is invariant under both `D` and `mathcal Q`, its dilated
state has the nonzero fermionic variation (10). A free fermion inserted
at an interior point creates a nonzero state. Localizing its boundary
pairing by the same fixed-sector formula is therefore not justified.

Moreover, protected motion makes `O(t)-O(0)` exact. Its dilation has
the same nonzero variation in (10), so choosing the representative at
the center does not make the action on arbitrary representatives
well-defined. One may define a separate action after choosing and
projecting to special representatives; it is not the descent of `D`
just tested.

Restricting to neutral pairs does not avoid the problem. For distinct
interior points,

\[
 \mathcal Q[D,{\cal O}(t_1)\widetilde{\cal O}(t_2)]
 =-\frac{t_1}{2r}\chi(t_1)\widetilde{\cal O}(t_2)
  -\frac{t_2}{2r}{\cal O}(t_1)\widetilde\chi(t_2).
 \tag{12}
\]

The two independent fermionic insertions do not cancel as operator
identities. For a particularly simple witness set `t_2=0`, `t_1!=0`.
There is no gauge transport variation in this free control to supply
a missing term. A nonzero or even invariant expectation of an operator
would not by itself repair its failure of closure.

## 4. What the two natural repairs actually do

In the adapted H frame let `R_*` act on `(q_1,q_2)` with weights
`(+1/2,-1/2)`. Then

\[
 \widehat D=D-R_*,\qquad
 [\widehat D,{\cal O}(t)]=t\partial_t{\cal O}(t).
 \tag{13}
\]

The superconformal algebra identifies `-widehat D` with the exact
twisted dilation of [D, (3.4)], with the same conjugation of frames as
in (5)–(7). It is exact also for the equivariant combination on its
invariant subspace. Thus it acts trivially on these local-operator
cohomology classes. Its R-current contribution is precisely the
compensation required to follow the changing polarization; adding it
changes the requested evolution.

The disappearance of the spatial separation is visible without a
cohomological argument. In conventions where the scalar contraction
tensor is `E_12=1`, the free polarized contraction on the flat diameter is

\[
 \frac{\det((1,t_1/(2r)),(1,t_2/(2r)))}{4\pi|t_1-t_2|}
 =\frac1{8\pi r}\operatorname{sgn}(t_2-t_1).
 \tag{14}
\]

The twist has canceled the distance dependence. This protected
two-point function is not (3). The radial Weyl factors can be restored,
but then do not turn it into the stationary untwisted covariance.
The original even-angular smearing has not been provided with a
protected completion either.

Alternatively one can transport the charge itself. In the standard
flat frame,

\[
 e^{aD}\mathcal Q_r e^{-aD}
 =e^{a/2}\mathcal Q_{e^ar}.
 \tag{15}
\]

This maps between complexes. It is not an endomorphism of the fixed
one. A proposal based on it must give a connection/intertwiner for the
family of boundary polarizations and its ordinary adjoint, and show
how the original unprotected radial propagation is retained.

Do not mistake overall change of units for the missing dynamics. Under
`r -> c r`, `Y -> c^(-1/2)Y`, the variable `x` is invariant. Condition
(4) is covariant: both its normal derivative and `Y/r` scale with
weight `3/2`. The vacuum normalization scales as `sqrt(c)`, while
`d^2Y` scales as `c^(-1)`, preserving the gluing norm. Thus curvature
alone is not a no-go for a family of scaled boundary problems; the
failure proved here is closure under `D` with the protected problem
held fixed.

There is also a useful algebra check on a tempting shortcut. At fixed
`epsilon`, the protected generators obey
`[tilde Q_L,Q_L]=-epsilon I`. No commutator action on this algebra can
give *both* generators conformal weight `+1/2`: applying that action
to the relation would give `-epsilon I` on the left and zero on the
right. A scaling of `epsilon` would be needed. This excludes that
shortcut, not every possible projected grading of selected states.
The chiral-primary fact `Delta=d/2` at the origin survives; it does
not identify the polynomial degree with `ell` or prove descent on
the finite-radius boundary module.

## 5. The Mellin generator that really is present

Although it is not the image of spatial `D`, the field-magnitude
generator and its ordinary adjoint are unambiguous. Write

\[
 \Psi(Y,\bar Y)=(\pi\epsilon)^{-1/2}f(x,\vartheta),
 \qquad
 \|\Psi\|^2=\int_0^\infty dx\int_0^{2\pi}\frac{d\vartheta}{2\pi}
                  |f(x,\vartheta)|^2.
 \tag{16}
\]

For `f_B(x)=(2pi)^(-1) integral e^(iB vartheta)f d vartheta`, the
normalized transform is

\[
 F_B(\sigma)=\frac1{\sqrt{2\pi}}
 \int_0^\infty x^{-1/2-i\sigma}f_B(x)\,dx,
 \qquad \sigma\in\mathbb R,
 \qquad \|\Psi\|^2=\sum_{B\in\mathbb Z}\int_{\mathbb R}|F_B|^2d\sigma.
 \tag{17}
\]

Setting `v=log x` takes `f` to `g(v)=e^(v/2)f(e^v)` and turns (17)
into the ordinary unitary Fourier transform. This derives its contour,
weight, and measure. In the neutral sector,

\[
 N=-x\partial_x,\quad N^\dagger=1-N,\quad
 A=N-\tfrac12,\quad A^\dagger=-A,
 \quad {\cal M}Af=-i\sigma F.
 \tag{18}
\]

These identities hold first on a smooth compactly supported core and
extend by Fourier equivalence. The group generated by `A` is
`U_a f(x)=e^(-a/2) f(e^(-a)x)`; `iA` is self-adjoint with real spectrum
`sigma`. Thus the offset `1/2` comes from the measure `dx`, and the
scale is translation of `log x`. Neither has been derived from spatial
`u`. On the real contour the ordinary bra conjugates `s` to `1-s`.
A vacuum gluing phase is not a rule to square an inserted analytic
polynomial instead of taking its modulus squared.

This is the real-coordinate boundary norm used in the preceding
control. It is not an established isometric map from the full radial
state space, or from arithmetic storage, into these wavefunctions.

The spatial Hamiltonian in (2) and the unitary field-dilation group
have different definitions and adjoints. This is a useful consistency
check, not a claim that discreteness of (2) alone precludes every
transform between continuous spectral variables. The actual
obstruction is (10).

For a monomial `Y^a bar Y^b`, its field-phase label is `B=b-a`, its
total degree is `d=a+b`, and its transform on the vacuum is proportional
to `epsilon^(d/2) Gamma(s+d/2)`. These relationships follow from polar
coordinates in *field space*. They impose no relation to spatial
harmonics. Likewise `M[x^alpha f](s)=F(s+alpha)` is a field insertion,
not a derivation of an arithmetic shift.

The action fixes the coefficient `4pi r` in `x`. A unitary relabeling
`x'=c x` multiplies (17) by `c^(s-1/2)`, a phase on this contour.
Choosing such a relabeling to manufacture an exponential in an
unidentified `p` would not fix the arithmetic finite part.

## 6. The compatible two-scalar arc and its forced terms

Take the hemisphere great semicircle `0<=varphi<=pi`. Insert the
twisted `Q` at its north end and `tilde Q` at its south end, understood
as limits of separated interior insertions. Their endpoint components
are `q_1` and `tilde q_2`, exactly the variables fixed in (4). Join
them by the identity transport of the trivial gauge representation.
This is the free conformal bilocal limit of an open line, not a
nontrivial four-dimensional Wilson operator.

There is no dynamical vector multiplet or nonzero background mass.
The reduced kinetic operator is `partial_varphi`, with action
`-epsilon^(-1) integral tilde Q partial_varphi Q dvarphi`. Its Ward
identity fixes the propagator jump to `-epsilon`. Antiperiodicity
then gives, on a chosen lift of the circle,

\[
 \langle Q(\varphi_1)\widetilde Q(\varphi_2)\rangle
 =-\frac{\epsilon}{2}\operatorname{sgn}(\varphi_1-\varphi_2),
 \quad 0<|\varphi_1-\varphi_2|<2\pi.
 \tag{19}
\]

The jump is understood with the antiperiodic delta distribution.
The endpoint order chosen here gives `+epsilon/2`. Equation (14)
checks the same sign and normalization directly from the 3d action.
An inverse background transport would cancel the mass exponential
if that background were turned on and included in the transport;
here its value is exactly one. The R polarization is already in the
twisted fields. It is not an additional gauge Wilson factor.

On the boundary the separated poles act by multiplication:

\[
 Q_L\widetilde Q_R\Psi_0=Y\bar Y\Psi_0
 =\epsilon x\Psi_0,\qquad
 \Psi_0=(\pi\epsilon)^{-1/2}e^{-x}.
 \tag{20}
\]

No contact subtraction is forced at separated endpoints. If one
instead collides the operators, the canonical Ward identity requires

\[
 Q_L\widetilde Q_L\Psi_0=\epsilon x\Psi_0,\qquad
 \widetilde Q_LQ_L\Psi_0=\epsilon(x-1)\Psi_0.
 \tag{21}
\]

Their difference is the prescribed `-epsilon` in the reverse ordering.
The symmetric *local composite* has state
`epsilon(x-1/2)Psi_0`. This is an explicitly different definition of
the observable, not an automatic correction to (20). In particular,
orthogonalizing a composite to the vacuum is not a Ward identity
requiring the separated bilocal to have zero expectation.

As an independent gluing check,

\[
 \frac{\langle\Psi_0,\Psi_{\rm pair}\rangle}
      {\langle\Psi_0,\Psi_0\rangle}
 =\epsilon\frac{\int_0^\infty x e^{-2x}dx}
                   {\int_0^\infty e^{-2x}dx}
 =\frac\epsilon2,
 \qquad \|\Psi_{\rm pair}\|^2=\frac{\epsilon^2}{4}.
 \tag{22}
\]

The transformed state is (1). The action has not varied, so there is
no `partial S` insertion for this calculation. Protected endpoint
motion away from collisions gives zero derivative by the kinetic
Ward identity. Attempting **ordinary spatial** dilation instead
produces (12); the optional R-current compensation (13) changes the
operation. It supplies no forced quartic descendant or arithmetic
normalization.

## 7. What comparison with the arithmetic factor is permitted

The complete prime-free arithmetic amplitude, in the repository's
fixed normalization, is

\[
 F_{\rm ar}(p)=\pi^{-p/2}(p-\tfrac12)
                 \Gamma(p/2+5/4),\qquad
 K^<_\omega(p)=\frac{F_{\rm ar}(p-\omega)}{F_{\rm ar}(p+\omega)}.
 \tag{23}
\]

This includes the rational factor and the finite local normalization,
not just the gamma function. Its causal compression gives the target
on the prime-free spatial window; the whole-line arithmetic problem
also requires the integer delays.

The independently predicted amplitude here is
`epsilon Gamma(s+1)/sqrt(2pi)`. But (10) prevents this computation from
assigning it a spatial `p`. Therefore there is no physical right-half-
plane contour, affine scale or offset, `p`-dependent normalization,
or `p -> p +/- omega` operation to use in (23) in this fixed control.
The field-space contour and measure in (17) do not answer those
spatial questions. Analytic continuation does not create a missing
intertwining relation.

In particular, this note does not assume either previous trial map
`s=(p+1/2)/2` or `s=(p+5/2)/2`, and does not infer a universal
polynomial-degree mismatch from either. The obstruction precedes
that comparison. `N(2N-1)`, adjustable identity mixing, or a selected
exponential in `p` would not cure (10). A coefficient of a Q-exact
localizing term also cannot become the physical shift.

## 8. Reproduction, scope, and next decision

From this investigation directory:

```sh
python3 numerics/check_spatial_radial_descent.py \
  --output /tmp/spatial-radial-descent-replay.json
```

The checker uses the Python standard library; its quadrature helper
is imported from the preserved hemisphere checker. Exact rational
checks cover the polarization residual, compensated charge weights,
boundary operator ordering, the failed equal-weight algebra action,
gluing moments and the ordinary adjoint. Floating-point checks compare
the free spatial harmonic series, the centered stereographic twist,
the 3d contraction against the 1d Ward propagator, and the field-space
Mellin identities. The saved small record and provenance are under
`numerics/records/`. These checks audit signs and algebra; they do
not independently establish the cited supersymmetry transformations.

All 83 cases pass at quadrature orders 24 and 40: 57 exact rational
checks and 26 floating-point checks. At order 24 the largest absolute
floating discrepancy is below `9.4e-14`. These are finite diagnostics,
not interval certificates or a substitute for the argument (9)–(12).

**Scope of the obstruction:** fixed finite `r`, the specified free
massless hypermultiplet, its fixed Higgs localization charge and
polarization, and an action on closed representatives modulo exact
ones compatible with the ordinary spatial `D`. It does not exclude
an enriched representation with nonclosed states, a family of charges
with specified intertwiners, a different protected sector, a chosen
grading of center-inserted chiral primaries, or an interacting
four-dimensional defect construction.

The smallest algebraic repair is the R-current compensation, but it
removes the requested radial dynamics in this cohomology. To retain
that dynamics one must keep the discarded fermionic/untwisted data
or give an explicit family-of-complexes construction and prove what
survives it. Another gamma-function calculation cannot resolve this
compatibility failure. The independent cumulative-defect program can
resume without counting this negative control as positivity input.

No causal transfer on arbitrary spatial inputs, arithmetic ordinary
adjoint, cumulative positive norm, new horizon, or Loewner driver has
been obtained. The next-session handoff is
[here](RESEARCH_CONTINUATION_AFTER_RADIAL_DESCENT_20260920.md).

## Primary references

- [D] M. Dedushenko, S. Pufu and R. Yacoby, *A one-dimensional theory
  for Higgs branch operators*, arXiv:1610.00740v2,
  [primary text](https://arxiv.org/html/1610.00740v2).
  Relevant equations: (2.8)–(2.10), (3.1)–(3.10), (6.2)–(6.5),
  (C.7)–(C.14).
- [G] M. Dedushenko, *Gluing II: Boundary Localization and Gluing
  Formulas*, arXiv:1807.04278v3,
  [primary text](https://arxiv.org/html/1807.04278v3).
  Relevant locations: the cut after (52), (78)–(82), the localization
  charge after (107), and (125)–(141).

LLM disclosure: the new descent test, observable calculation, note and
checker were prepared with the model recorded above. The external
localization framework is an input. Independent specialist review of
the conformal-frame and state-cohomology argument is the next audit,
not a completed review.
