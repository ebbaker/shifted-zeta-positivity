# Scoped review: theta arithmetic and finite collision certificates

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed and are not inferred.
This is a separate same-model review, not independent specialist validation.

**Verdict.** The exact arithmetic transforms, finite-theta-cutoff
Wronskian obstruction, tail formulas and compact collision certificate
pass this scoped check. Two qualifications were requested and verified
in the revised note: vanishing odd endpoint jets do not distinguish zeta
from general even kernels, and the normalized Cauchy argument requires
holomorphy and a nonvanishing normalizer on the whole closed disk.
No outstanding correction remains in the reviewed scope.

Reviewed
[ZETA_COLLISION_ARITHMETIC_20261008.md](../notes/ZETA_COLLISION_ARITHMETIC_20261008.md),
its [script](../numerics/zeta_collision_arithmetic_check.py), and its
[small record](../numerics/zeta_collision_arithmetic_record_20261008.json).
The script reproduced the saved record byte for byte in the current
environment. Its floating computations remain reconnaissance; they do
not enclose quadrature errors or certify a rectangle.

## 1. Normalization and exact arithmetic representations

Consulted the primary
[Polymath paper](https://arxiv.org/html/1904.12438#S1) on 8 October 2026.
Its equations (1)--(4) confirm the note's normalization of `H_0`, the
theta kernel, its evenness and the backwards heat equation. Its
[Theorem 1.5(i)](https://arxiv.org/html/1904.12438#S1.Thmtheorem5)
has the stated positive-time cutoff with an absolute constant and
requires `0<t<=1/2`. This checks the quoted scope, not that theorem's
full proof. The nonuniformity as time tends to zero remains necessary.

The double-integral formula for `W=H'^2-HH''` has the correct factor
`1/4`: symmetrizing `-HH''` contributes `(u^2+v^2)/2` to its cosine
product, and the sine product contributes `uv`. The resulting coefficients
of `cos(x(u-v))` and `cos(x(u+v))` are respectively `(u+v)^2/4` and
`(u-v)^2/4`. Positivity of the theta summands does not give a sign for
these oscillatory integrals.

For the change of variables `v=pi n^2 e^(4u)`, put `a=pi n^2`. Then

    (2a^2 e^(9u)-3a e^(5u)) du
       = a^(-1/4) (2v-3)v^(1/4) dv/4.

Consequently the prefactor `pi^(-1/4)/4`, the `n^(-1/2)` weight and
the finite cutoff `n<=sqrt(v/pi)` in formula (4) are correct. At time
zero, expanding the cosine as a real part produces the powers
`(pi n^2)^(-ix/4)` and the two upper incomplete gamma functions with
parameters `9/4+ix/4` and `5/4+ix/4`, as in (5). The derivative phase
`cos(xu+j pi/2)` is also correct. These calculations do not create an
Euler product or justify importing a character-family theorem.

## 2. Endpoint jets and the cutoff obstruction

Direct differentiation gives

    phi_n'(0) = -a(8a^2-30a+15)e^(-a),  a=pi n^2.

The larger root of the quadratic is `(15+sqrt(105))/8`. Every tail term
for `n>N>=1` is beyond that root. Full theta evenness and Gaussian
convergence therefore give precisely the strictly positive tail
representation for `A_N=Phi_N'(0)` in equation (6).

For `f=e^(tu^2)Phi_N`, the heat multiplier does not change `f'(0)`.
All derivatives used in integration by parts are integrable uniformly
on compact time intervals. Applying the argument separately to the
three integrals gives

    H_N=-A_N/x^2+O(x^-4),
    H_N'=2A_N/x^3+O(x^-5),
    H_N''=-6A_N/x^4+O(x^-6).

Thus the leading Wronskian coefficient is `4A_N^2-6A_N^2=-2A_N^2`.
The note properly avoids differentiating an uncontrolled remainder.
The eventual sign is uniform in compact time intervals for fixed `N`;
no uniform onset in `N` is asserted.

The extension to nonreal zeros of every finite cutoff is valid. The
integral bounds its maximum modulus by an exponential of order
`O(r log(r+2))`, giving an entire function of order at most one.
A nonzero real entire function of order below two, all of whose zeros
are real, has a Hadamard product with no quadratic exponential factor;
away from its zeros its logarithmic second derivative is the negative
sum of reciprocal squared distances, with the multiplicity contribution
at zero included. It therefore satisfies the Laguerre inequality
`F'^2-FF''>=0`, contrary to the cutoff asymptotic. This argument uses
the order restriction, which is present in the note.

The warning about naive analytic symmetrization is also correct:
`Phi_N(-u)` has a negative nonzero leading multiple of `e^(-5u)`.
Multiplying this tail by `e^(tu^2)` prevents absolute integrability for
every positive `t`.

One interpretation required correction. The earlier general-kernel
counterexample is itself even and analytic, so all its odd endpoint
jets also vanish. The revised note now explicitly separates this
shared property from zeta's particular arithmetic theta decomposition
and the cancellation between its retained summands and omitted tail.
It no longer claims to have found a sign-forcing invariant absent from
the general-kernel example. The new obstruction concerns the **fixed
theta cutoff**, not general even heat kernels.

## 3. Tail constants and Wronskian error propagation

For `m=N+1`, monotonicity gives

    sum_(n>=m) n^4 e^(-pi n^2)
      <= m^4 e^(-pi m^2) + integral_m^infinity v^4 e^(-pi v^2) dv.

Two integrations by parts give the first two tail terms
`m^3/(2pi)` and `3m/(4pi^2)`, multiplied by `e^(-pi m^2)`.
The remaining integral is at most `e^(-pi m^2)/(2pi m)`, with
prefactor `3/(4pi^2)`. This verifies the last coefficient
`3/(8pi^3 m)` in `B_N`.

On `[0,U]`, discard the negative part of each positive theta summand,
bound `e^(tu^2+9u)` by `e^(tau U^2+9U)`, and bound
`e^(-pi n^2 e^(4u))` by `e^(-pi n^2)`. Integrating `u^j` gives exactly
the lattice error (8), including its factor `2pi^2/(j+1)`.

For the spatial tail, `n^4<=16^(n-1)` and `n^2-1>=3(n-1)` imply
the geometric bound below two used in (9). With

    L_j(u)=j log u+tau u^2+9u-pi e^(4u),

one has `L_j'(U)=-d_j` and
`L_j''(u)=-j/u^2+2tau-16pi e^(4u)<0` for `u>=U>0`,
`0<=tau<=1/2`. Its tangent line integrates to the denominator `d_j`
in (10), provided `d_j>0`. These are absolute errors uniform in real
`x`; a relative-error or sign conclusion near a very small transform
does not follow.

The error formula (11) follows by expanding
`(a_1+delta_1)^2-(a_0+delta_0)(a_2+delta_2)` and using
`|delta_j|<=e_j`. All five terms displayed there are necessary and
present. The claimed reconstructions explicitly require certified
quadrature errors in addition to the analytic tail estimates.

## 4. Compact coverage and the normalized derivative criterion

The rectangle certificate uses valid componentwise Lipschitz bounds:

    |partial_x H|<=M_1,  |partial_t H|<=M_2,
    |partial_x H'|<=M_2, |partial_t H'|<=M_3.

The heat equation provides the time derivatives. The entire straight
paths from the cell center to a point remain inside the rectangle,
where the moment majorants with `t_+` apply. Either strict inequality
in (12) therefore gives a nonzero component throughout that cell.
A finite covering certifies the whole rectangle, including its
boundary; isolated sampled points would not.

The converse is an existence statement justified by compactness: no
common zero gives a positive minimum of `sqrt(H^2+H'^2)`, so sufficiently
fine cells and sufficiently accurate validated center values pass.
Choose the spatial truncation first and then the theta cutoff large
enough for its lattice error; the bounds tend to zero in that order.
This does not supply an a priori lower bound for the collision vector
or a practical finite run without certified numerical work.

The normalizer identity (13) follows by differentiating `H=BQ`; the
cross terms cancel and `B'^2-BB''=-B^2(log B)''`. Common-zero
equivalence uses `B!=0`. The revised Cauchy paragraph now requires
`B,F` holomorphic on a neighborhood of the closed disk and `B`
nonvanishing there, so a circle bound on `Q-F` legitimately bounds
its derivative at the center. The earlier phrase 'locally nonzero'
alone would not have excluded interior poles elsewhere in that disk.

The paper's scalar Riemann--Siegel approximation is not promoted to
an analytic-neighborhood derivative theorem. The revised note retains
the branch, cutoff and two-sided-neighborhood obligations. Nor does
a compact certificate supply all-height or all-positive-time coverage:
the required height cutoff deteriorates as time tends to zero.

## 5. Reproducibility and retained limits

The reviewed note's SHA-256 is
`f3d1cd1e62699e6b712d785ca236dd9cbfff7515ae72e0a34e96c91c4c8342bd`.
The script's SHA-256 is
`ad3887f7a36bdb719da3127532bbfafed2bfffb3d425cde61f8a22f0b6d1ff6e`;
the saved JSON's is
`608f42035f3dbe09309c9515c28c7ccbe74bfd2b75f1631ee10416ed83644f74`.
These identify the reviewed files and reproducible exploratory run;
they do not strengthen its numerical certification status.

The note proves a meaningful approximation obstruction and supplies
a correct sufficient finite-certificate format. It proves no new
uniform arithmetic nonvanishing estimate, no completed collision-free
rectangle, and no RH implication. Its proposed next task needs a
derivative-controlled normalized approximation and new arithmetic
control of the collision vector, not just smaller absolute theta tails.
