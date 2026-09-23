# SU(2) level 2: a completed deterministic boundary Loewner pilot

22 September 2026. Prepared for Edward Baker.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed in this session; not inferred.  
**Status:** internal analytical research with exact finite algebra and floating
controls; specialist review outstanding. Prepared with LLM assistance. This is
a research note, not a manuscript revision or a claim of a new CFT theorem.

## 1. Assessment and result

The [proposed Chern--Simons/WZW pilot](CHERN_SIMONS_WZW_AND_NATURAL_LOEWNER_EVOLUTION_20260922.md)
is still the most worthwhile **next bounded calculation for the physical
Wilson--Loewner question**, on the evidence in this investigation. Its advantage
over the pending four-dimensional Yang--Mills calculation is concrete: the
boundary fields, admissible channels, and differential identities can all be
specified before trying to close their evolution. This assessment does not
rank WZW as the most promising route to RH, and it does not supersede the
separate arithmetic continuation work.

The pilot is carried out below in the diagonal SU(2)_2 boundary WZW theory.
It produces an explicit, nonconstant four-point observable, its complete
deterministic evolution, an initial block selected by boundary conditions,
composition and fusion rules, and a spatial-smearing statement.

The useful calculation is the following reduction, with K=k+2, nu=1/K:

\[
 \boxed{\dot M_t=-\nu\bigl(2Q_t^2+\dot u_t Q_t\bigr)M_t,\qquad
 Q_t=\frac{T_{01}}{g_t(x)-u_t}+\frac{T_{02}}{g_t(y)-u_t}.}
 \tag{1}
\]

The actual pilot has k=2 and nu=1/4. Both spectator insertions are on the real
boundary. Consequently Q is Hermitian in the ordinary invariant spin-tensor
inner product. A constant driver therefore gives an exact positive balance
in that pairing. A moving driver can give growth, including for the selected
Cardy block. Neither statement identifies this tensor pairing with the
Chern--Simons gluing pairing or with the arithmetic L2 norm.

The calculation uses established Ward/KZ identities. Its contribution here is
to complete and test the proposed construction, including the distinctions
between its state spaces and pairings. No novelty priority is asserted.

## 2. Theory, boundary conditions, and the observable

Use the unitary diagonal SU(2)_2 WZW model, c=3/2, with maximally symmetric
Cardy boundary conditions and the identity current-gluing automorphism. Write
V_j for the integrable affine module, including its descendants, at spin j.
The permitted primary labels are 0, 1/2, and 1. The boundary sector is

\[
 \mathcal H_{ab}=\bigoplus_j N_{aj}^{\ b}V_j.
 \tag{2}
\]

For the labels needed here, H_00=V_0, H_(0,1/2)=V_(1/2), and
H_(1/2,1/2)=V_0 plus V_1. These are infinite-dimensional affine modules;
they are not the two-dimensional space used in the KZ calculation. Cardy
boundary sectors and their fusion constraints are the standard BCFT input;
see [Cardy, sections 2--3](https://arxiv.org/html/hep-th/0411189) and
[Behrend--Pearce--Petkova--Zuber, sections 2.3 and 4.2](https://arxiv.org/html/hep-th/9908036).

Let D_t be the upper half-plane with a prescribed simple Loewner slit removed.
The hydrodynamically normalized map satisfies

\[
 \dot g_t(z)=\frac{2}{g_t(z)-u_t},\qquad g_0(z)=z,
 \qquad u_0=0.
 \tag{3}
\]

Take a C1 driver on a time interval on which the chosen slit and all marked
prime ends are well defined. Fix real spectators 0<x<y, not swallowed during
this interval. On the uniformized boundary, the successive boundary labels,
starting just after minus infinity, are

\[
 0\ \xrightarrow{\,u_t\,}\ \tfrac12
 \ \xrightarrow{\,g_t(x)\,}\ 0
 \ \xrightarrow{\,g_t(y)\,}\ \tfrac12
 \ \xrightarrow{\,\infty\,}\ 0.
 \tag{4}
\]

Each arrow carries the unique spin-1/2 boundary-changing primary in the
corresponding boundary sector. In D_t these labels are pulled back to the
boundary and the two banks of the slit. The tip is a boundary-changing field;
the two remaining finite fields are genuine boundary fields, so no mirror
insertions are required. All four weights are h=3/16.

Normalize the four-field tensor amplitude by the two-field amplitude having
the same tip and infinity fields, with their invariant contraction normalized
to one in the half-plane. Equivalently, the extra changes at x and y are a
pair of boundary-changing insertions on the reference 0-to-1/2 boundary.
Fix field normalizations so that the identity OPE at the first two insertions
has leading coefficient one in the normalized singlet tensor below.

Let F(u,X,Y,infinity) be this half-plane tensor amplitude. With

\[
 a_t=g_t(x)-u_t,\quad b_t=g_t(y)-u_t,\quad
 J_x=g_t'(x),\quad J_y=g_t'(y),
\]

the slit observable is precisely

\[
 M_t(x,y)=J_x(t)^hJ_y(t)^h F(0,a_t,b_t,\infty).
 \tag{5}
\]

The following choices account for the endpoint and scalar factors in (5).

* The local coordinate at the tip is the uniformizing prime-end coordinate
  zeta=g_t(z)-u_t. Use the same coordinate and cutoff in numerator and
  denominator. Their tip-primary factors cancel. There is no use of a finite
  Euclidean derivative g_t'(tip), which generally does not exist.
* The infinity field means the limit z^(2h) phi(z). Hydrodynamic normalization
  gives derivative one in its reciprocal local coordinate. The reference
  two-point function with infinity is independent of u.
* The two spectators contribute exactly the two Jacobians in (5).
* A common domain/Weyl anomaly factor cancels in this normalized ratio. We
  do not calculate an unnormalized slit partition function. There is no
  extra freely chosen time-dependent scalar factor in (5).

This is the deterministic counterpart of the normalized slit-correlator
setup in [Alekseev--Bytsko--Izyurov, equations (3)--(7)](https://arxiv.org/html/1012.3113).
The driver is prescribed; no Brownian or internal-group average is taken.

For the Wilson interpretation, use holomorphic polarization on the doubled
disk, a sphere with the four marked boundary insertions, and fixed ribbon
framings/local coordinates. The SU(2)_2 Chern--Simons state space for these
four spin-1/2 punctures has two allowed fusion channels, 0 and 1. A framed
network preparing the 01 vacuum channel selects the state used here.
Wilson endpoints as conformal-block data are supported by
[Alekseev--Barmaz--Mnev, section 5](https://arxiv.org/html/1212.6256).
This supplies a CS interpretation of the chiral data; it does not identify
the two-dimensional slit with the bulk Wilson trajectory or derive a new
CS boundary action with corners.

## 3. Explicit tensor basis and the selected initial block

The invariant tensor space W=Inv((C2)^(tensor 4)) has an orthonormal basis

\[
 e_0=s_{01}s_{23},\qquad
 e_1=\frac{t^+_{01}t^-_{23}+t^-_{01}t^+_{23}-t^0_{01}t^0_{23}}{\sqrt3},
 \tag{6}
\]

where s=(|up,down>-|down,up>)/sqrt(2), with the usual triplets. Use generators
t^a=sigma^a/sqrt(2), not sigma^a/2, and T_ij=sum_a t_i^a t_j^a. Then the
Casimir is C_(1/2)=3/2 and h=C_(1/2)/(2K). In the basis (6),

\[
 T_{01}=D=\begin{pmatrix}-3/2&0\\0&1/2\end{pmatrix},\quad
 T_{02}=C=\begin{pmatrix}0&-\sqrt3/2\\-\sqrt3/2&-1\end{pmatrix},\quad
 T_{12}=B=\begin{pmatrix}0&\sqrt3/2\\\sqrt3/2&-1\end{pmatrix}.
 \tag{7}
\]

In particular D+C+B=-(3/2)I. This normalization reproduces the identity-OPE
exponent -2h=-3/8; using Pauli/2 without changing the KZ coefficient would
give the wrong exponent by a factor of two.

Scale and translation covariance, including the infinity convention, give

\[
 F(0,a,b,\infty)=b^{-2h}f(r),\qquad r=a/b,\qquad
 f'(r)=\nu\left(\frac D r+\frac B{r-1}\right)f(r).
 \tag{8}
\]

The first two fields in (4) have boundary label 0 on both outside intervals.
Their OPE must therefore lie in H_00=V_0. This selects the solution

\[
 f^{(0)}(r)=r^{-3/8}\bigl(e_0+O(r)\bigr)
 \tag{9}
\]

with no independent spin-one Frobenius branch. This is a boundary-condition
selection, not a fit of arbitrary initial data. Both tensor components of
this one selected block are generally nonzero. The full two-dimensional
solution space is useful for transport and sewing, even though these fixed
boundary labels select one vector-valued solution.

At level 2 both solutions are elementary. Set s=sqrt(1-r),
p=[r(1-r)]^(-3/8), with positive real roots for 0<r<1. The columns with
unit leading Frobenius tensors e_0 and e_1 are

\[
 f^{(0)}(r)=\frac p{2\sqrt2}
 \begin{pmatrix}(1+s)^{3/2}\\-\sqrt3(1-s)\sqrt{1+s}\end{pmatrix},
 \tag{10}
\]

\[
 f^{(1)}(r)=\frac p{\sqrt6}
 \begin{pmatrix}-(1-s)^{3/2}\\\sqrt3(1+s)\sqrt{1-s}\end{pmatrix}.
 \tag{11}
\]

One direct derivation eliminates the second component of (8), writing the
first as r^(-3/8)(1-r)^(-3/8)P(r). It gives

\[
 r(1-r)P''-\tfrac12P'-\tfrac3{16}P=0.
\]

Changing to s gives (1-s^2)P_ss+sP_s-(3/4)P=0, solved by (1+s)^(3/2)
and (1-s)^(3/2). Substitution into the first KZ equation and the leading
normalizations yield (10)--(11). Thus these formulas can be checked without
assuming a hypergeometric connection identity.

For another independent construction, if f=r^lambda sum_(n>=0) v_n r^n,

\[
 [(\lambda+n)I-\nu D]v_n=-\nu B\sum_{m=0}^{n-1}v_m,\qquad n\ge1.
 \tag{12}
\]

Use (lambda,v_0)=(-3/8,e_0) or (1/8,e_1). The exponent difference is 1/2,
so every displayed inverse exists. For example the selected block begins

\[
 r^{-3/8}\left[
 \binom10+r\binom0{-\sqrt3/4}
 +r^2\binom{3/64}{-\sqrt3/8}+O(r^3)\right].
\]

For the numerical initial geometry (u,x,y)=(0,1,2), the specified state is

\[
 M_0=2^{-3/8}f^{(0)}(1/2)
   \simeq(1.02266239412001,-0.30390758736355)^T.
 \tag{13}
\]

## 4. Complete deterministic generator and its square reduction

Before collision or swallowing,

\[
 \dot a=2/a-\dot u,\quad \dot b=2/b-\dot u,\quad
 \partial_t\log J_x=-2/a^2,\quad \partial_t\log J_y=-2/b^2.
 \tag{14}
\]

The KZ connections for the two relative coordinates are

\[
 A_a=\nu\left(\frac Da+\frac B{a-b}\right),\qquad
 A_b=\nu\left(\frac Cb+\frac B{b-a}\right).
 \tag{15}
\]

The moving tip is already included: translation invariance gives
partial_u F=-(partial_a+partial_b)F=-nu(D/a+C/b)F. Combining (5), (14),
and (15) gives the Ward/KZ generator

\[
 G=\nu\left[
 \left(\frac2{a^2}-\frac{\dot u}a\right)D
 +\left(\frac2{b^2}-\frac{\dot u}b\right)C
 -\frac{2B}{ab}\right]
 -2h\left(\frac1{a^2}+\frac1{b^2}\right)I.
 \tag{16}
\]

The B coefficient follows from
[(2/a-dot u)-(2/b-dot u)]/(a-b)=-2/(ab). In particular an equation
containing only the spectator velocities 2/a and 2/b misses the tip term
when the driver moves. Omitting the conformal Jacobians misses the last
scalar in (16).

The finite spin identities

\[
 D^2=\tfrac34I-D,\qquad C^2=\tfrac34I-C,\qquad DC+CD=B
 \tag{17}
\]

immediately turn (16) into (1). They are also the spin-1/2 identities used
in the stochastic KZ reduction; here they are applied to deterministic
transport with the original conformal weights. No Ito term or renormalized
stochastic weight is imported.

There is a modest algebraic generalization: for a spin-1/2 tip and any finite
family of real boundary primary spectators, Q=sum_i T_(0i)/w_i and
h_i=nu C_i/2 give the same formula, using
T_(0i)^2=C_i I/2-T_(0i) and
{T_(0i),T_(0j)}=T_ij for i unequal j. Appropriate boundary conditions and
integrable fusion channels must still be selected. For bulk/mirror positions
w_i are complex and Q need not be Hermitian; the norm result below must not
be transferred to that alternative pilot.

On a compact time interval bounded away from marked-point collisions and
swallowing, G is continuous and bounded. The ordinary matrix initial-value
problem therefore has a unique invertible propagator. This supplies closure
for the selected finite block system without a moment truncation.

## 5. What positivity does and does not follow

For a constant driver, Q=Q^dagger in the spin-tensor metric and

\[
 \boxed{
 \|M_T\|_W^2+4\nu\int_0^T\|Q_tM_t\|_W^2\,dt
 =\|M_0\|_W^2.}
 \tag{18}
\]

This holds for every initial evaluated vector in W, not just (13). It is an
analytic identity following from (1). The matrices at distinct times need
not commute. With a=1, b=2, the k=2 generator is

\[
 G_{\dot u=0}=\begin{pmatrix}
 -39/32&-3\sqrt3/16\\-3\sqrt3/16&-3/32
 \end{pmatrix}.
 \tag{19}
\]

It is strictly negative. More generally det Q=-(3/4)(1/a-1/b)^2, so Q is
invertible when the finite spectators are distinct. The constant-driver
slit gives nontrivial evolution here, unlike the exactly retracing bulk
loop with its particular chord completion in the earlier YM control.

A general driver gives instead

\[
 \frac d{dt}\|M\|_W^2
 =-4\nu\|QM\|_W^2-2\nu\dot u\langle M,QM\rangle_W.
 \tag{20}
\]

For a=1, b=2, dot u=4, one obtains

\[
 G=\begin{pmatrix}9/32&\sqrt3/16\\\sqrt3/16&-3/32\end{pmatrix}.
 \tag{21}
\]

Thus e_0 has initial squared-norm derivative 9/16>0. More strongly, the
actual Cardy-selected state (13) has derivative approximately
0.436388495438834>0. This is a counterexample to an all-driver contraction
claim in the very pairing used in (18), without changing the boundary
preparation. Its norm need not keep growing at later times.

Completing the square gives a useful control:

\[
 G=-2\nu(Q+\dot u I/4)^2+\nu\dot u^2 I/8,\qquad
 \|U(T,0)\|_W\le
 \exp\left(\frac\nu8\int_0^T\dot u^2dt\right).
 \tag{22}
\]

Multiplication of M by exp[-nu integral(dot u^2)/8] would make this pairing
contractive for every C1 driver. That is an additional mathematical
normalization, not part of the observable (5), and has not been derived
from a physical partition function. It cannot be used to claim the desired
fixed arithmetic normalization.

## 6. Composition, fusion, and the two different pairings

Write Phi(r)=[f^(0)(r),f^(1)(r)] and

\[
 E_t=J_x(t)^hJ_y(t)^h b_t^{-2h}\Phi(a_t/b_t).
\]

There are no braids on the chosen real ordered path. The exact propagator is

\[
 U(t,s)=E_tE_s^{-1},\qquad
 U(t,s)U(s,r)=U(t,r),\qquad U(s,s)=I.
 \tag{23}
\]

Equivalently it is the time-ordered exponential of G. Loewner map composition
and the primary-Jacobian chain rule supply the same composition. If the
normalized coordinate map is restarted at time s, the remaining driver is
translated accordingly; it must not be reset to the original starting
geometry. Formula (23) uses a single consistent original-coordinate frame.

For explicit fusion, put

\[
 R=\begin{pmatrix}1/2&\sqrt3/2\\-\sqrt3/2&1/2\end{pmatrix},\qquad
 Z=\operatorname{diag}(1,-1),\qquad
 \Phi_t(r)=RZ\Phi(1-r)Z.
\]

The columns of Phi_t have the normalized leading tensors of the 12 channels.
Substitution of (10)--(11) gives the constant connection

\[
 \Phi(r)=\Phi_t(r)\mathsf C,\qquad
 \mathsf C=\begin{pmatrix}
 1/\sqrt2&-\sqrt{2/3}\\\sqrt{3/8}&1/\sqrt2
 \end{pmatrix}.
 \tag{24}
\]

The displayed signs are a basis convention. In the unitary channel gauge
N=diag(1,sqrt(3)/2),

\[
 \widehat{\mathsf C}=N^{-1}\mathsf C N
 =\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}.
 \tag{25}
\]

This makes the fusion gluing explicit. With channel coefficients c,d in
the raw Frobenius basis of (10)--(11), the positive unitary CS pairing,
normalized to give the vacuum channel norm one, is

\[
 \langle c,d\rangle_{\rm CS}
 =c^\dagger H_c d,\qquad H_c=\operatorname{diag}(1,4/3).
 \tag{26}
\]

Indeed local full monodromies have the distinct phases corresponding to
-3/8 and 1/8, so their invariant Hermitian metric is diagonal. Requiring
the connection (24) to preserve that metric fixes the ratio 4/3. Equations
(24)--(26) give its unitary fusion realization explicitly. In the normalized
channel coefficients N^(-1)c the pairing is just the ordinary sum over
the two channels. Orientation reversal conjugates the amplitude, and sewing
contracts the matching channel indices with this pairing. For example,
the selected s-vacuum state c=(1,0) has norm one and has equal-magnitude
components 1/sqrt(2) in the normalized t-channel basis.

In evaluated tensor coordinates M=E_t c, that same gluing form is

\[
 H_t=E_t^{-\dagger}H_cE_t^{-1},\qquad
 U(t,s)^\dagger H_tU(t,s)=H_s.
 \tag{27}
\]

It is **not** the constant identity matrix on W used in (18). Thus the
channel state has constant CS norm while its evaluated, conformally
weighted color tensor can decrease in the fixed tensor norm. Equating
these two facts would be a false physical positivity argument.

A scalar boundary observable can be obtained without confusing the pairings:
choose an explicitly fixed invariant polarization p in W and use p^dagger M.
For example p=e_0 pairs the finite spin indices in the 01/23 singlet pattern.
A scalar CS amplitude obtained by sewing to a prepared channel bra d uses
d^dagger H_c c instead. Neither pairing is silently an L2 boundary integral.

## 7. Spatial smearing and a precise limitation of the raw kernel

For disjoint compact intervals I_x<I_y to the right of the starting tip,
and before either approaches the hull, define

\[
 M_t[f,g]=\int_{I_x}\!\int_{I_y}
 f(x)g(y)M_t(x,y)\,dy\,dx,
 \qquad f,g\in C_c^\infty.
 \tag{28}
\]

This is a superposition of insertion positions, with fixed physical boundary
coordinates and measure dx dy. Its derivative is the integral of G_t(x,y)M_t.
Because G depends on x and y, one smeared two-vector does not itself obey a
closed two-by-two equation. Retaining the full position-dependent family
does give a multiplication evolution on a suitable W-valued function space.
For constant driving, integrating (18) against a positive spatial measure
gives the corresponding direct-integral norm identity. The actual BCFT
preparation still has the conformal-block dependence (10); arbitrary functions
in that enlarged space have not been constructed as physical states.

There is an additional useful test of the proposed two-boundary-kernel format.
Fix I=[epsilon,L] on the positive real boundary and a polarization p. On x<y
define K_t(x,y)=p^dagger M_t(x,y), extended by zero for the opposite order.
This tests this particular ordered kernel; the ordering convention does not
derive the arithmetic direction of causality.

The 12 identity OPE is the worst collision singularity. Here 2h=3/8, so

\[
 |K_t(x,y)|\le C_T\bigl(1+|x-y|^{-3/8}\bigr)
 \tag{29}
\]

uniformly on a compact time interval when g_t remains regular on I. The
Jacobian factors preserve this power under uniformization. Consequently
|K_t|^2 has at worst |x-y|^(-3/4), which is integrable. The associated
integral operator on L2(I) is Hilbert--Schmidt and compact, including at t=0.
The explicit blocks and the same integrable bound also give K_t -> K_0 in
Hilbert--Schmidt norm as t decreases to zero.

Thus **this raw normalized four-point kernel does not have the identity
initial condition** on the infinite-dimensional L2(I): its initial operator
is compact, not the delta kernel. A finite scalar normalization or an
ordinary time reparameterization does not repair that. This does not exclude
a different physical sewing construction, descendants, a separate identity
term derived from that construction, or a distinct singular limiting regime.
It prevents this completed pilot from being mislabeled as the arithmetic
transfer simply by smearing it.

No prime-power translations, arithmetic pole response, or equality between
capacity t, window length L, and shift omega has been derived.

## 8. Reproducible checks

The [checker](../numerics/check_wzw_loewner_pilot.py) and
[small record](../numerics/records/wzw-loewner-pilot-20260922.json) use only
Python and NumPy. From the investigation directory run

```sh
python3 -B numerics/check_wzw_loewner_pilot.py --output /tmp/wzw-loewner-replay.json
```

There are 72 checks: seven exact rational identities and 65 floating controls.
They all passed. The controls include the independent 16-dimensional Pauli
construction, algebraic blocks versus a Frobenius series, complex-step KZ
derivatives in all three finite insertion coordinates, fusion and pairings,
Ward-to-square reduction, full two-channel evolution, norm balances, and
two-stage composition for five drivers at two integration resolutions.
Negative controls detect omission of the tip drift or Jacobians, scalar
component closure, and an all-driver contraction claim.

For x=1, y=2 and final capacity 0.2:

| Driver | Initial selected tensor norm squared | Final selected tensor norm squared | Largest propagator singular value |
|---|---:|---:|---:|
| u=0 | 1.1381981940 | 0.8772251458 | 0.9993155549 |
| u=0.8t | 1.1381981940 | 0.9140272726 | 0.9957985079 |
| u=4t | 1.1381981940 | 1.1237629942 | 1.0029796534 |
| u=-0.8t | 1.1381981940 | 0.8453990280 | 1.0021154561 |
| u=0.4 sin(2t) | 1.1381981940 | 0.9127125337 | 0.9958813085 |

The u=4t selected state initially grows, even though its final value in this
table lies below its initial value. For u=0 the integrated loss is
0.260973048240009. The largest floating equality residual in the recorded
checks is below 6.7e-14; this is diagnostic agreement, not a certified bound
on the analytic formulas. The CS fusion residual is below 1.1e-15.

The analytic derivations of (1), (18), and (29), rather than numerical sign
sampling, support the corresponding claims. There is no quantum path-integral
sampling or interval certificate in this package.

## 9. Research decision after the pilot

The five requested pilot deliverables are now present:

| Requested item | Result |
|---|---|
| Observable and physical spaces | Cardy sectors (2), slit labels (4), normalized amplitude (5), and CS channels |
| Complete deterministic variation | Tip, infinity, Jacobians, and anomaly convention; equations (14)--(16) |
| Ward/KZ reduction and initial state | Exact blocks (10)--(13) and closed generator (1) |
| Gluing/composition and pairings | Equations (23)--(27), with the two metrics distinguished |
| Meaning of spatial smearing | Equation (28) and the compact-kernel initial-condition obstruction |

Continue this direction for one further bounded physical question: construct
the **actual slit-sewing map on the boundary affine-module Hilbert space**,
retaining descendants and the prescribed endpoint fields, and compute its
reflected gluing form with the normalization fixed by (5). H_(0,1/2)=V_(1/2)
is the first concrete candidate sector. The decision criterion is whether
this construction gives a well-defined map between cut boundary state spaces
and a controlled positive balance in its physical pairing. It must explain
its relation to the finite tensor identity (18), rather than assume them
equal. The exact pilot provides a check on its primary matrix elements.

Do not spend the next step merely increasing k, fitting arithmetic coefficients,
or interpreting (22)'s compensating scalar as already physical. The four-point
question is now solved at the pilot level. If the full sewing construction
does not provide useful operator structure, retain this as a controlled
benchmark and reconsider the more expensive YM hierarchy calculation.

All existing manuscripts, historical snapshots, and prior research notes are
preserved. This addendum is based on local repository commit 20f252d and the
three pre-existing uncommitted clarification/proposal notes. No claim about
changes on the remote repository is needed for this assessment.
