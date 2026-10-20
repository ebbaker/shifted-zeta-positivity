# Close positive sources with normalized double zeros

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded turn metadata. Separate same-model derivations and
[internal review][review]; no specialist review or priority claim.

**Outcome:** under RH, arbitrarily small uniform relative perturbations
of the theta source can have an exact double zero at time zero while
preserving the leading source tail, the functional equation, the
displayed completion factors, pole residue one and normalization at
positive real infinity. The perturbed functions fail ordinary Dirichlet
series arithmetic. This is a control for an explicitly stated set of
retained information, not a counterexample to RH implying simplicity.

A separate calculation adds a strong log-concavity bound to Note 03's
polynomial control.
A short horizontal-shift audit identifies an exact comparison with the
already tested Poisson consumer. Neither supplies the signed theta
estimate required by the [program][program]. The [result index][results],
[collision catalogue][controls] and [avoid index][avoid] apply,
especially [control premises][a02], [scoped conclusions][a07],
[normalization][a08] and [gain before expansion][a20].

## 1. Source inputs and normalization

Use the unchanged source and heat coordinate
\[
 \Phi(u)=\sum_{n\ge1}\pi n^2(2\pi n^2e^{4u}-3)e^{5u-\pi n^2e^{4u}},
 \quad F(x)=\int_0^\infty\Phi(u)\cos(xu)\,du
          =\tfrac18\xi(1/2+ix/2).                         \tag{1}
\]
The source is positive, even and smooth, with `Phi'(u)<0` for `u>0`
and super-Gaussian decay of every derivative. These properties, in
exactly this normalization, are recorded in [Csordas][cs], equation
(4.2) and Theorem 4.1. Theorems 4.2 and 4.5 also give strict source
log concavity away from zero. No all-derivative concavity conjecture
is being imported.

We will use `Phi''(0)<0`. Here is a direct check. For `Y=pi n^2`,
\[
 \Phi''(0)=\sum_{n\ge1}e^{-Y}
 (32Y^4-224Y^3+330Y^2-75Y).                              \tag{2}
\]
For `3<pi<22/7`, the first polynomial is less than `-711`, and
`e^pi<25`. For `n>=2`, the polynomial is at most `35Y^4`, so its
total contribution is at most `8960 sum_{n>=2}n^8 e^(-3n^2)<18`.
For the last bound, consecutive terms have ratio below `1/1000`;
`e>8/3` gives the upper bound
`8960 (1000/999) 256 (3/8)^12<18`. Thus
`Phi''(0)<-711/25+18<0`. For example `pi<19/6`, `e<11/4` and
`e^(1/6)<6/5` suffice for the elementary exponential upper bound.

The first term of (1), with differentiated remainders, gives
\[
 \Phi(u)=2\pi^2e^{9u-\pi e^{4u}}(1+O(e^{-4u})),\quad
 \kappa(u):=-\Phi'(u)/\Phi(u)\sim4\pi e^{4u}.             \tag{3}
\]
In particular `Phi''(u)>0` and `kappa'(u)>0` eventually,
`kappa'/kappa^2->0`, and
`(log Phi)''=-16 pi e^(4u)+O(e^(-4u))`. The higher source terms
are exponentially smaller; differentiating their series is legitimate.
The source asymptotics are also used in [Investigation 21, Note 52][n52].

## 2. Dividing out a high real zero while keeping a positive source

For a sufficiently decaying function `f` on the half-line define
\[
 T_b f(u)=\frac1b\int_u^\infty\sin(b(v-u))f(v)\,dv,
 \qquad b>0,\ u\ge0.                                    \tag{4}
\]
It satisfies `(T_b f)''+b^2 T_b f=f`. If `f` is positive and strictly
decreasing to zero, splitting the sine integral into half-periods gives
\[
                 0<T_bf(u)\le\frac{2f(u)}{b^2}.          \tag{5}
\]
Indeed successive half-period integrals form a decreasing alternating
sequence; the sum is positive and at most its first term. Pairing each
positive half-period with the next proves strict positivity.

Suppose `b` is a positive real zero of `F`, and set `q_b=T_b Phi`.
Then `q_b'(0)=-F(b)=0`. The differential equation and evenness of Phi
make every odd derivative of `q_b` vanish at zero, so it has a smooth
even extension. Twice integrating the cosine transform by parts gives
\[
 \int_0^\infty q_b(u)\cos(xu)\,du=\frac{F(x)}{b^2-x^2},  \tag{6}
\]
with removable singularities at `+/-b`. All its derivatives retain
super-Gaussian decay, by (4) or its differentiated integral.

For **all sufficiently large such roots b**, `q_b` is strictly
decreasing on `u>0`. To see the uniform large-b step, integration by
parts gives
`T_b f=f/b^2-T_b(f'')/b^2` and
`|T_b g(u)|<=(|g(u)|+integral_u^infinity |g'|)/b^2`.
On every fixed compact interval,
\[
 q_b'=\Phi'/b^2+O(b^{-4}),\qquad
 q_b''=\Phi''/b^2+O(b^{-4}),                             \tag{7}
\]
uniformly there. Near zero, (2), continuity and `q_b'(0)=0` imply
`q_b'<0`. On the rest of a fixed compact interval use `Phi'<0`.
Beyond a fixed `U` where `Phi''>0`, the function `-Phi'` is positive
and decreasing; (5) applied to it gives `q_b'=T_b Phi'<0` directly,
for every `b`. This covers the whole unbounded half-line.

More explicitly, choose `eta,U,mu0,mu1>0` so that `Phi''<=-mu0`
on `[0,eta]`, `-Phi'>=mu1` on `[eta,U]`, and `Phi''>0` past `U`.
Set `K1=||Phi'''||_infinity+||Phi^(4)||_1` and
`K2=||Phi^(4)||_infinity+||Phi^(5)||_1`, with norms on the half-line.
The integrations by parts above show that
`b^2>max(K1/mu1,K2/mu0)` suffices for the compact part of the argument.

Choose another positive real zero `c>b` of `F`. Since (6) vanishes at
`c`, the source `q_bc=T_c q_b` is again smooth and even, and
\[
 0<q_b\le2\Phi/b^2,\qquad
 0<q_{bc}\le4\Phi/(b^2c^2),\qquad
 \widehat q_{bc}^{\,\cos}(x)
 =\frac{F(x)}{(b^2-x^2)(c^2-x^2)}.                       \tag{8}
\]
Only the first division required the proved large-b monotonicity;
positivity of the second division follows from that monotonicity.
No simplicity assumption on either old zero was used: one occurrence
of each pair is divided out.

## 3. A double zero with unchanged residue and leading tail

Assume RH and choose `b<c` to be consecutive **distinct** sufficiently
high positive zeros of `F`. Put
\[
 A=\frac{b^2+c^2}{2},\quad d=\frac{c^2-b^2}{2},\quad
 e=A+1-\sqrt{(b^2+1)(c^2+1)}
   =\frac{d^2}{A+1+\sqrt{(A+1)^2-d^2}},\quad a^2=A-e.
                                                                  \tag{9}
\]
Then `0<e<d` and `b<a<c`. Define
\[
 \widetilde F(x)=F(x)
 \frac{(a^2-x^2)^2}{(b^2-x^2)(c^2-x^2)}.                 \tag{10}
\]
This is entire and all-real under RH. It removes one occurrence from
each pair `+/-b,+/-c` and adds an **exactly double** pair `+/-a`,
because the original function has no zero between `b` and `c`.
All other zero multiplicities are retained.

Expanding the multiplier and using
`q_bc''+c^2q_bc=q_b` gives the exact source
\[
 \boxed{\widetilde\Phi=\Phi-2e q_b+(d+e)^2q_{bc}.}        \tag{11}
\]
The negative term is essential for the normalization below. By (8),
\[
 \widetilde\Phi\ge(1-4e/b^2)\Phi,\qquad
 \boxed{\left|\frac{\widetilde\Phi}{\Phi}-1\right|
 \le\varepsilon_{b,c}:=\frac{4e}{b^2}
       +\frac{4(d+e)^2}{b^2c^2}.}                       \tag{12}
\]
The bound holds on the entire real source axis after even extension.
Riemann–von Mangoldt implies `c/b->1` for consecutive distinct high
roots under RH: every interval `(B,(1+eta)B]`, with fixed `eta>0`,
contains a root for all sufficiently large `B`, including multiplicities
and consistent endpoints. Consequently `d/b^2->0`, `e/b^2->0`, and
`epsilon_{b,c}->0`. In particular the source is strictly positive for
all sufficiently high pairs. The bound in (12), rather than an
unquantified continuity assertion on a compact set, pays its whole tail.

For fixed `b,c`, endpoint Laplace scaling in (4) also gives
\[
 q_b(u)/\Phi(u)\sim\kappa(u)^{-2},\qquad
 q_{bc}(u)/\Phi(u)\sim\kappa(u)^{-4}.                    \tag{13}
\]
For the first formula set `v-u=y/kappa(u)`. The ratio of source values
tends to `e^(-y)` locally uniformly, by (3); eventual increase of
`kappa` bounds it by `e^(-y)`, and
`kappa sin(by/kappa)/b->y`. Dominated convergence gives
`integral_0^infinity y e^(-y)dy=1`. The second formula follows from
the double integral for `T_c T_b Phi`, scaling both increments;
the majorant is `y z e^(-y-z)`, with integral one. Therefore
\[
 \frac{\widetilde\Phi}{\Phi}
 =1-2e\kappa^{-2}(1+o(1))\longrightarrow1.               \tag{14}
\]
This preserves the leading theta tail with its coefficient and
exponential rate. It does not preserve the complete source series or
all subleading coefficients.

In the original `s` coordinate, write `w=s-1/2` and
\[
 R(s)=\frac{(a^2+4w^2)^2}{(b^2+4w^2)(c^2+4w^2)},\qquad
 \widetilde\xi(s)=\xi(s)R(s),\qquad
 \widetilde D(s)=\zeta(s)R(s).                           \tag{15}
\]
Zeros cancel every denominator pole. The function is real under
conjugation and `R(s)=R(1-s)`. The choice (9) gives
\[
 R(0)=R(1)=1,\qquad R(\sigma)\longrightarrow1
                       \quad(\sigma\longrightarrow+\infty).
                                                                  \tag{16}
\]
Thus the completed function has the same functional equation and values
`xi(0)=xi(1)=1/2`. In the displayed completion it has the same gamma
and conductor-one factors; the de-completed function has pole residue
one at `s=1` and tends to one along the positive real axis. The derivative
`xi'/xi(1)` and the unchanged Euler coefficients are **not** preserved;
indeed `R'(1)=-8e/[(b^2+1)(c^2+1)]<0`.
The source identity (11) exactly preserves its corresponding cosh-weighted
moment `integral_0^infinity Phi(u)cosh(u)du=1/16`.

The failed arithmetic premise is explicit. For fixed `b,c`,
\[
 R(s)=1-\frac{e}{2w^2}+O(w^{-4}),\qquad
 -\frac{\widetilde D'}{\widetilde D}(\sigma)
 =-\frac{e}{\sigma^3}+O(\sigma^{-4})+O(2^{-\sigma})<0
                                                                  \tag{17}
\]
for sufficiently large positive `sigma`. An ordinary Dirichlet series
with first coefficient one, absolutely convergent in any right
half-plane, satisfies `D(sigma)-1=O(2^(-sigma))`. The nonzero algebraic
correction in (17) violates this. In particular this is not a genuine
zeta-arithmetic counterexample, despite its preserved normalizations.

## 4. Heat evolution and what approximation can establish

The source in (11) is smooth, even and integrable with every real heat
multiplier and polynomial weight. Its transform solves the same
backward heat equation. Applying the real-zero preservation and local
splitting arguments already used in Notes 01 and 03 gives all-real
zeros for `t>=0`, simple zeros for `t>0`, and nonreal zeros immediately
before the added double event at `t=0`. Its all-real threshold is zero.
These are the control's own data, not transferred zeta arithmetic.

Uniform relative source closeness has the following explicit consequence.
For fixed nonnegative integers `j,k` and finite `T,Y>=0`,
\[
 \sup_{|t|\le T,\ |\Im z|\le Y}
 |\partial_t^j\partial_z^k(\widetilde H-H)(t,z)|
 \le\varepsilon_{b,c}\int_0^\infty
 u^{2j+k}e^{Tu^2+Yu}\Phi(u)\,du.                         \tag{18}
\]
Thus the endpoint-double controls approach the original source in the
relative norm (12), and their transforms in every displayed finite
heat-jet seminorm, even uniformly over all real spectral centers.
They leave every fixed bounded set of original zeros unchanged once
`b` is sufficiently high. The doubled zeros move to infinity.

This establishes a precise limitation on a **fixed positive tolerance**
or these broad source/completion premises alone. It does not invalidate
local certified simplicity checks, error bounds that shrink with height
against a proved nonzero margin, or arguments using the exact complete
theta identity. No fixed high root has been shown to be multiple in
the original function. The finite cap baseline remains compatible with
all these controls, as in the earlier notes.

## 5. Separate curvature screen for the polynomial control

For clarity, this section concerns **Note 03's polynomial multiplier**,
not a claim of curvature preservation for the normalized merger above.
Let
\[
 c_*:=\inf_{u\in\mathbb R}[-(\log\Phi)''(u)]>0.
\]
Positivity follows from strict concavity away from zero, (2), continuity
on compact sets and the curvature tail in (3). For every fixed
`0<c0<c_*`, the isolated control
\[
 \Phi_M=\Phi+2M^{-2}\Phi''+M^{-4}\Phi^{(4)}
\]
obeys
\[
 \boxed{-(\log\Phi_M)''(u)\ge c_0\quad
 \text{for every real }u\text{ and all sufficiently large }M.}     \tag{19}
\]
To prove this uniformly, set `r_j=Phi^(j)/Phi` for `j=2,4`.
The differentiated first source term gives
`r_j=(-4pi)^j e^(4ju)(1+O(e^(-4u)))` and
`r_j''/r_j->(4j)^2`. These differentiated expansions follow from
polynomials in `pi e^(4u)` for the first source term and exponentially
smaller higher terms. On a fixed sufficiently distant tail,
`r_j>0`, `r_j''<=300r_j`. For
`Q_M=1+2M^(-2)r_2+M^(-4)r_4`, therefore
`(log Q_M)''<=Q_M''/Q_M<=300`, uniformly in `M`.
Choose the tail where `(log Phi)''<=-300-c0`; compact `C^2`
convergence of `Q_M` to one handles the remainder. This proves (19)
and positivity of the source for large `M` without treating compact
convergence as a bound at infinity.

The heat-weighted source retains curvature at most `-c0/2` for
`|t|<=c0/4`. Choose `M` off the original zero set. Under RH its
transform `F_M(x)=F(x)(1-x^2/M^2)^2` has an exact added double zero,
and the own-data Gaussian estimate of Note 01 gives
\[
 D_{M,s}\ge\frac{384s^4F(M)^2}{M^8}>0,
                   \qquad 0<s\le M^2/4.                 \tag{20}
\]
Here `F_M''(M)=8F(M)/M^2`; substitution in the earlier estimate verifies
the constant. Strong source log concavity, even with any fixed slack
below theta's uniform floor, therefore does not supply the opposing
Gaussian sign. This strengthens the earlier [source-shape control][n53]
for this particular all-real endpoint family. It does not assert
preservation of square-variable or all-derivative concavity.

## 6. Short audit: finite horizontal shifts

One other signed attempt has an exact disposition, before any absolute
prime estimate. In ordinary zero-ordinate coordinates under RH let
`B_u(gamma)=sum_lambda m_lambda u^2/(u^2+(gamma-lambda)^2)`.
For `delta,h>0`, set
`J=log|xi(1/2+delta+h+i gamma)/xi(1/2+delta+i gamma)|`.
Integration of the completed logarithmic derivative gives
\[
 \boxed{B_\delta(\gamma)\le
 \frac{J}{\log(1+h/\delta)}
 =\frac{\int_\delta^{\delta+h}B_u(\gamma)\,du/u}
        {\int_\delta^{\delta+h}du/u}
 \le B_{\delta+h}(\gamma).}                             \tag{21}
\]
Every Poisson summand increases with `u`, proving the bounds. Thus this
particular finite-shift consumer cannot improve the exact starting-width
one; the best limit is `h->0`. This is not a conclusion about every
signed shift combination.

For `sigma=1/2+delta>1`, the Euler quotient with nonnegative ordinary
Dirichlet coefficients is `zeta(s)/zeta(s+h)`. Its modulus is bounded
above by `zeta(sigma)/zeta(sigma+h)`. With
`C(s)=s(s-1)pi^(-s/2)Gamma(s/2)/2`, this gives
\[
 J\ge\log|C(s+h)/C(s)|-
        \log[\zeta(\sigma)/\zeta(\sigma+h)].             \tag{22}
\]
It is a lower bound where the proposed multiplicity argument needed
a small upper bound. No useful event-conditioned bound in that missing
direction was obtained. The series was used only in `sigma>1`.
The log-derivative/Pick formulation similarly assigns positive spectral
mass `m` at a zero of multiplicity `m` (the residue is `m` for
`xi'/xi`, and `-m` in the usual Pick-function convention).
Positivity of that mass is not an upper bound of one.

## 7. Disposition

The new control (11) improves the earlier screens by combining uniform
relative source closeness, the same leading tail and exact residue
normalization. Its arithmetic failure (17) remains indispensable to
the scope. The curvature result (19) concerns a different control;
their preservation lists must not be silently combined.

These results rule out the stated inference from approximate source
information and retained structural properties. They do not rule out
the exact theta source or unchanged discrete Euler arithmetic supplying
the required signed estimate. That estimate, a strict finite-cap surplus
or a negative direct Gaussian deficit remains unproved. The
[progress register][progress] retains those open gates; no numerical
sign campaign, new theta exclusion interval or manuscript follows.

[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[progress]: ../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md
[review]: ../reviews/05_SOURCE_CONTROL_AND_SHIFT_AUDIT_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../../../avoid/08_normalization_and_constant_slips.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
[cs]: https://arxiv.org/pdf/1309.0055
[n52]: ../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md
[n53]: ../../../../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/53_SOURCE_CONCAVITY_AND_POSITIVE_TIME_COLLISION_CONTROL_20261015.md
