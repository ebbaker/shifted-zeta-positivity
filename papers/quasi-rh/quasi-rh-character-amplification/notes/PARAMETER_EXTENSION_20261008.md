# Conditional parameter extension below seven eighths

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

Inspected external PDF SHA-256:
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The PDF remains in temporary storage outside this repository.

The [subsequent geometry extension](GEOMETRY_OPTIMIZATION_20261008.md)
supports the stronger conditional candidate `7/8 - 1/24000`. This record
retains the first displacement and its explicit Euler-domain repair.

## Result and status

The displayed estimates in OpenAI's [September 30 quasi-RH paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
admit a small change of geometry. Conditional on that paper's stated
structural lemmas and its already obtained seven-eighths theorem, the
argument below gives the candidate improved boundary

\[
\sigma_r=\frac78-\frac1{600000}
=\frac{524999}{600000}=0.8749983333\ldots.
\tag{1}
\]

The conditional derivation has passed targeted internal checks by two
additional agents and exact rational exponent checks. This is not an
independent validation of the external 199-page proof, a Lean proof, or a
claim of mathematical priority. Its reflection, inverse-moment, and
fourth-moment machinery remain external assumptions. No existing
manuscript or historical status has been upgraded to an unconditional
new zero-free theorem.

The improvement is deliberately small. It tests whether the published
boundary is forced by the current inequalities. The useful finding is
that a small row-norm loss can be paid for by a rescaling factor already
present in the physical probe. No stronger moment inequality is required
for this conditional perturbation.

## External inputs and conventions

Write F=Q(sqrt(-3)). Let beta_* be the supremum of 1/2 and the real
parts of zeros of all primitive finite-order Hecke L-functions over F,
as in source (2.1). Assume the source Theorem 1.1, beta_*<=7/8.
Suppose, for contradiction, beta_*>sigma_r.

The external inputs retained with their full coefficient classes, masks,
and uniformity are: the smooth-profile calculus and global bounds of
Section 4; the exact low separation and Euler identities of Sections
6 and 7; the detector Proposition 8.3; the general reflected estimate
(14.14) and Lemma 14.3; the additive Gram estimate Proposition 15.2;
inverse estimates Lemmas 17.1 and 17.6; and Lemma 18.1. The contour
and height arguments of Section 10 and Lemma 11.1 are used with the
expanded domain proved below. The continuation principle Proposition
2.1 is already stated for any boundary in (1/2,1).
Also retained are Lemma 13.1 for the prime normalizer, the full corrected
identities (16.3) and (16.7), central Proposition 16.1, and Lemma 19.1's
prime-amplitude estimate.

No arbitrary residual coefficient is added, no zero on a nonunit is
removed, and no prime-slot support or common row orientation is changed.
The physical expression is exactly source (12.5), with the new X,Y
scales below. The selected prime supports remain disjoint; their defining
slot windows and lengths are fixed before Z tends to infinity, while the
primes in those windows vary with Z. In this note r denotes the geometry
perturbation, not the inverse-witness length used elsewhere in the source.

## Geometry and the low estimate

Set

\[
r=\frac1{100000},\quad b=\frac18,\quad\ell=\frac16,\quad
h=\frac{13}{16}+r,
\]
\[
l_x=\frac{17}{48}-r,\quad l_y=\frac{23}{48}-r,\quad
X=Z^{l_x},\quad Y=Z^{l_y},\quad M=l_x+l_y=\frac56-2r.
\tag{2}
\]

Then h=1-l_x+ell and l_y-l_x=b remain exact. The source's specialized
identity M+ell=1 becomes M+ell=1-2r; it must not be reused unchanged.

For a rescaled subset of total prime-slot length d in [0,ell], put
M'=M-2d and ell'=ell-d. Retain the source's dyadic variables H,O,
Delta_H and the small annular displacement theta_N. The comparison on
source p.103 now gives

\[
T_d\le H-3d-2r+O(\epsilon_0+\kappa_G+\epsilon_Z).
\tag{3}
\]

It is stronger than the old comparison, so the estimates for the actual
dual ranges and max(H,v+ell_b) remain valid. In the unspecialized identity
(15.3), the potentially positive term in the second energy branch is

\[
\frac{1+3\ell'-2M'-2\Delta_H+\theta_N}{4}
=\frac{d-1/6+4r-2\Delta_H+\theta_N}{4}.
\]

The other branch is bounded by M'-Delta_H up to small losses.
Both decrease with Delta_H, whose lower bound is minus an arbitrarily
small dyadic error. The proof of Lemma 15.1 therefore yields the modified
bound

\[
\sum_m |B_m^J(Z)|^2
\ll Z^{M'+(d-1/6+4r)_+/4+\epsilon}.
\tag{4}
\]

The stronger old assertion with no positive part is unnecessary.
All lengths needed by the additive Gram estimate remain positive:

\[
l_x-\ell=3/16-r>0,\quad l_y-\ell=5/16-r>0,
\quad l_y-\ell-11b/6=1/12-r>0,
\]

and P_a=q_{b_*}^{-1}Z^{1/8} is unchanged. Apply Proposition 15.2 and
Cauchy-Schwarz exactly as on p.107. The rescaled tuple count, its
coefficient, and X'^(1/2) contribute the factor Z^{-d} from (15.8).
The total additional exponent is consequently

\[
f_r(d)=-d+\frac18(d-1/6+4r)_+\le0
\quad(0\le d\le1/6,\ 0\le r\le1/24).
\tag{5}
\]

For d<=1/6-4r this is -d. Above that breakpoint it is affine with
negative slope -7/8 and starts at a nonpositive value. Thus the full
finite probe has the low estimate

\[
|I_{\eta,\mathrm{modified}}^{(r)}(Z)|
\ll_{\eta,\epsilon}Z^{L_r+\epsilon},\qquad
L_r=\frac{l_x}{2}+\frac b{12}=\frac3{16}-\frac r2.
\tag{6}
\]

The finite number of homogeneous seminorms and polynomial height orders
are inherited from the same profile and reflected estimates on fixed
bounded parameter ranges. The extra positive part in (4) changes a real
power, not the coefficient class or the separation procedure.

## Enlarging the Euler and contour domain

The published second Euler region (7.15), Definition 10.1, and several
Section 10 statements stop at Re(s)=7/8. Quoting them below that line
would leave a gap. An explicit larger region suffices:

\[
\Re s\ge87/100,\qquad \Re w\ge19/20,\qquad
\Re z\ge33/200.
\tag{7}
\]

It contains sigma_r. The local formulas (7.11) and (7.17) give
|R|<=Q^(-221/100), |V|<=Q^(-99/100), and |D|<=Q^(-87/100).
Their denominators are therefore bounded away from zero. At primes not
dividing the row, the largest defect exponent is

\[
1-\Re s-\Re w-6\Re z\le-181/100.
\]

The other displayed good-prime terms have exponents at most -182/100,
-186/100, -194/100, and -221/100. At ramified primes the largest
exponent is 1-Re(s)-Re(w)<=-41/50. The same product argument as on
source p.55 proves normal convergence and the q_u^epsilon bound on
(7). For the principal row, summing the good-prime tail gives decay
P_0^(-81/100), hence the original conservative P_0^(-4/5) bound.
Enlarging the fixed excluded set therefore gives

\[
\sup_{\Re s>87/100}|H_\eta(s)-1|\le1/2,
\tag{8}
\]

uniformly in the target's unit phases, as required by Proposition 2.1.

For the principal multiplier, the four exponents on source p.112 become

\[
-87/100,\quad-99/100,\quad-134/100,\quad-94/100.
\]

Thus B_p=-1+O(Q^(-87/100)) throughout (7). The full correction remains
the quotient-free expression (16.3); its absolute bound by Z^(ell Re z)
follows as before. Individual division by H_p is used only where the
principal lower bound has been established.

For the small-row contours Re(s)=beta_*+e, Re(w)=1/2, Re(z)=17/50,
use D_1(1/3), rather than the source's D_1(3/8). This is valid because
87/100+1/2>1+1/3. The four coprime-prime error exponents are negative.
For a ramified selected prime the strict term still has exponent 1/2;
the boundary terms are bounded by -1/2, -24/100, -61/100, and
-135/100, with the common R term smaller. Hence G_p=O(1) off the
row and G_p<<Q^(1/2) on it. Lemma 16.2's full-tuple bound survives.
The absolute large-row contours are unchanged.

These bounds supply the expanded-domain versions of Lemma 7.1,
Definition 10.1, the contour arguments in Lemmas 10.3--10.6, and the
principal/outer-row parts of Section 16. Central buffered contours
already lie in D_1(10e) and require no changed local arithmetic. All
new bounds are uniform in imaginary parts, so the same finite height
orders and external-tail procedure apply. Only their fixed constants
can change.

## Principal normalization and moment capacities

The signal exponent dictated by the exact residues is

\[
C_r(s)=s+l_x/2-1+h/6=s-11/16-r/3,
\qquad C_r(\sigma_r)=L_r.
\tag{9}
\]

The two principal poles remain w=1 and z=1/6. Keep the factor 1/6,
Gaussian, and the normalization formulas for c_S and A_T(Z) from
(10.1) and (20.1). The physical expression, c_S, H_eta and the signal
must all use the same final enlarged excluded set S. The numerical
value of c_S need not equal its value in the original application. The prime
normalizer uses fixed ray classes and satisfies |A_T|^{-1}<<Z^epsilon.
The new B_p estimate gives a residue error Z^(-mu) for any fixed
0<mu<(87/100)min_i ell_i. Lemma 10.5's proof, now within (7), gives
principal error margins

\[
m_w=(23/48-r)/20>0,\qquad m_z=(13/16+r)/600>0.
\tag{10}
\]

For the plain moment use kappa=3/4 exactly. Lemma 18.1 permits this
value and the assumed beta_*<=7/8 supplies its zero-free prerequisite.
Do not put kappa=2beta_*-1 below 3/4. With this permitted fixed kappa,
the plain capacity in (19.2) is exactly 2(1-2m)/9. Repeating the proof
of Proposition 19.2 therefore gives its baseline row exponents without
the Delta/4 penalty. Its original assumption Delta>0 is not invoked.

For delta=2a-1 in (1/50,3/4], x=q/delta in [0,1/2], set

\[
\alpha=5/6,\quad D_x=3-17x/9,\quad
P_x=(2-8x/9)(1-x),\quad
J=(\alpha-\delta)D_x+\delta P_x.
\]
\[
t=1+\frac{\delta P_x}{2J},\qquad
R^*=1-\delta+\frac{(\alpha-\delta)\delta P_x}{2J}.
\tag{11}
\]

The short and long witness counts cross at t. All inverse-width
inequalities retain the source's strict margin. The source's coefficient
and inducing-character exclusions are unchanged. The required prime
supply is available because ell/h>1/5>7/37; the same remains true for
h+zeta with a sufficiently small fixed positive zeta. This is a proof
with the existing moment bounds, not an extension of their kappa domain.

## High estimate and exact margins

For a bin of row length U=Z^d, the general exponent relative to the
new low scale, from source (10.15), is

\[
E_r(d)=a-\sigma_r+h(z_0-1/6)-a l_y-\ell/2+q\ell
+d(R+\delta/2-z_0),\qquad z_0=17/50.
\tag{12}
\]

The source endpoint certificate gives E_0(h_0)<=-49/440640 when
R=R^*. Direct subtraction at the changed endpoint gives

\[
E_r(h)-E_0(h_0)=r(R^*+\delta+1/2).
\]

To bound its coefficient, put y=1/2-x. The identity
16-20y-24y^2=(1/2-y)(24y+32)>=0 proves P_x/D_x<=2/3.
Since J>=(alpha-delta)D_x, (11) implies R^*<=1-2delta/3.
Therefore, using delta<=3/4,

\[
E_r(h)\le-\frac{49}{440640}+\frac{7r}{4}
=-\frac{51611}{550800000}<0.
\tag{13}
\]

The source certificate (20.9) is an exact polynomial identity with a
nonnegative right side, not a grid search. It and the ratio identity
were independently expanded with exact rational arithmetic.

All other ranges retain strictly positive margins before adjustable
losses. Conservative values sufficient here are:

| Range | Retained saving |
| --- | --- |
| Floor bin at d=h | 7/1200-(38/25)r |
| Intermediate d<=1/2 | 49/14400-(243/200)r |
| Small rows | 63/800-(101/150)r |
| Principal w remainder | (23/48-r)/20 |
| Principal z remainder | (13/16+r)/600 |

For fixed d the perturbation of (12) is r(a+17/50), explaining the
middle bound. The small-row change is (101/150)r. In the adaptive
range the frequency slope is positive, since R^*>=1-delta. It is
less than two. The same is true for the floor. Thus a positive extension
zeta costs at most 2zeta. For example, taking zeta equal to one sixteenth
of the saving in (13) preserves both a positive high margin and
ell/(h+zeta)>1/5. Large rows then decay by selecting a sufficiently
large fixed terminal z-contour, as in Lemma 10.6.

Choose the detector widths, capacity decrements, slot mesh and other
real losses small enough to preserve these margins and a fixed fraction
of beta_*-sigma_r. They are chosen before the target. For each target,
choose its allowed height exponent only after the finite internal height
orders are known, then choose external tail orders, as in Lemma 11.1.
The source permits target-dependent constants and lower thresholds;
the positive real exponent margins remain independent of the target.

Consequently the normalized physical probe J_eta=I/(c_S A_T) and its
principal Mellin signal satisfy Proposition 2.1 with boundary sigma_r,
affine exponent C_r, some 0<omega<beta_*-sigma_r, and a common
positive high saving. The proposition contradicts beta_*>sigma_r.
This closes the conditional extension under the listed external inputs.

## Consequence and next validation step

Quadratic base change transfers the conditional Hecke boundary to
Dirichlet L-functions as in the source. Through our
[fixed-probe equivalence](../../prime-variance-exponents/manuscript.tex),
the resulting local variance bound would be

\[
\mathcal V_g(X)=O\!\left(X^{11/4-1/300000}\right),\qquad
\delta=\frac34-\frac1{300000}.
\tag{14}
\]

The arithmetic gain is tiny and does not establish an iterative route
to RH. The next priority is an independent audit of the external
structural inputs and this written extension, followed by a broader
parameter optimization only if that audit succeeds. More substantial
improvements from shorter character families remain separate unproved
inputs; see the [transfer note](CHARACTER_FAMILY_TRANSFER_20261008.md).

The [review](../reviews/PARAMETER_EXTENSION_REVIEW_20261008.md) records
the precise check scope. The [exact check script](../numerics/check_parameter_extension.py)
and [small result record](../numerics/parameter_extension_check.json)
verify polynomial identities, piecewise exponent inequalities, and
positive rational margins. They do not verify analytic continuation,
automorphy, or the external moment lemmas.
