# Weak transfer budget and bounded method decision

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from this session's metadata. Thread
`01a170a3-5f6e-7aa2-9e33-bcae4835c782`, chat **0011**.

**Status: bounded floating diagnostic and exact selected identity controls;
no accepted finite core.** This is the return to
[HDA-17-AN01 r1](../research-progress/handoffs/HDA-17-AN01.md).
The mathematical source, regulator, kernel, physical offsets and targets
are unchanged. The [result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[control screen](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md) govern interpretation.
Under [avoid 01](../../../../avoid/01_restating_the_target.md) this is a
quantitative approximation milestone, not an RH-equivalent criterion.
See also [scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [same-model review](../../../../avoid/05_same_model_reviews_and_shared_premises.md).

## Decision and evidence

**Close AN01 r1 as a completed bounded floating diagnostic with retained
failure. Use the local transfer as the default for covariance and signed
source, with a componentwise weak/local choice where weak transfer helps.**
Neither route pays the whole requested norm in this trial. The next useful
change is source interpolation and peak-sensitive integration, rather than
more arithmetic modes, a larger source cutoff or more precision. HDA-17
remains Partial with no accepted finite core; HDA-18 remains Gated.
No exceptional analytical escalation is needed for this next bounded work.

The [index record](../numerics/WEAK_TRANSFER_DIAGNOSTIC_20261024.json)
links and hashes separate T64/T96/T128 records, each below 1 MiB. Together
they retain all externally targeted coefficient rows, source categories,
actual observable values, and both observable and positive-allowance
filter refinements. Internal current order-three coefficients enter the
source rows but are not assigned additional external targets.
[Code](../numerics/weak_transfer_diagnostic.py),
[coefficient maps](../numerics/weak_coefficients.py),
[exact controls](../numerics/exact_controls.py) and
[assessment](../reviews/18_WEAK_TRANSFER_BUDGET_ASSESSMENT_20261024.md)
make the return auditable. All eight frozen input hashes matched; the
working HEAD was `db79f03d5b2c5017c05c614ea6fee7ec3dfdeb0e`.

### Cost/accuracy comparison

The twelve observation centers are exactly t=64,96,128, x=0,4,
y=0,1/2. Uniform source meshes have 192,384,768 cells, cutoff 1.5 and
four modes. They contain 193,385,769 nodal coefficients, each with four
source terms. Source quadrature uses 6 and 10 Gaussian nodes per cell;
filter orders per direction are 16,32,64. At the largest combination,
one field evaluation uses 7680 source quadrature nodes and 4096 filter
nodes; source/filter arrays are regenerated and not stored in Git.
There was no N=8 trial because the mode allowance is negligible.

The following are **mapped source allowance / (0.8 target)** maxima over
the four centers at each time, using fixed 192-cell caps for the weak
linear tables. These are values of sufficient estimates evaluated in
floating arithmetic, not measured actual errors or lower bounds on them.

| Time | 192 cells | 384 cells | 768 cells | Weak bottleneck |
| --- | ---: | ---: | ---: | --- |
| 64 | 1.41932e7 | 2.86472e6 | 6.44352e5 | Delta Q |
| 96 | 1.21105e11 | 2.00797e10 | 4.05032e9 | source xy |
| 128 | 1.97354e11 | 2.36965e10 | 4.16294e9 | source yy |

The overall scalar-buffer maximum is 2.43698e12, versus 1.97354e11
for the positive-convolution weak diagnostic. Thus scalar bounds are
unhelpful and the required local-envelope comparison was tried. The
improvement does not pay a target. Common caps were frozen before mesh
comparison; every mesh's d0,d2 lies within them. The finite field changes
with the mesh, so its newly evaluated coefficient table is retained rather
than described as an identical numerical matrix across all meshes.

The fair 192-cell comparison uses identical source data and caps for both
transfers. At t=64,x=y=0, weak/local allowances for R are
0.443460 / 3.09060e-6, for Q 58.9567 / 0.124620, and for signed source
0.345256 / 4.82976e-8. Near the peak, t=64,x=4,y=0, weak helps R_t:
4.81409 versus local 196.975. There is no uniform dominance. Over the
whole t=64 sample, the worst local allowance/(0.8 target) is 6.20380e6,
versus weak 1.41932e7, both for Delta Q. This is a scoped implementation
comparison, not an exclusion of every weak approach.

The finer local route uses its actual smaller source-error interval,
whereas the main weak tables retain the original caps. To check that
this conservatism does not decide the conclusion by itself, one alternate
table freezes the 768-cell caps **before** computing coefficients at the
existing t=64,x=4,y=1/2 observation. No new observation or refinement is
introduced. Its weak/local source allowances are:

| Row | Weak, tight frozen caps | Local |
| --- | ---: | ---: |
| R | 0.0805760 | 0.00362895 |
| R_t | 0.0340541 | 0.00936345 |
| Q | 10.6917 | 1.28907 |
| Delta Q | 2687.98 | 129.122 |
| signed source | 0.0788650 | 6.48646e-5 |

This still favors local transfer for covariance/source. The weak map
remains useful as an alternative for individual rows, not a replacement
for the entire local contract.

### Error ledger and allocation

The source ledger keeps LC4's interpolation, omitted modes, complete tail
and candidate nodal arithmetic distinct. Source orders 1,3 are retained
only for the older local comparison/evaluator; the weak accuracy table
uses orders 0,2. Representative zeroth-jet interpolation allowances are:

| Time | 192 cells | 384 cells | 768 cells |
| --- | ---: | ---: | ---: |
| 64 | 0.0563935 | 0.0113742 | 0.00255806 |
| 96 | 315.828 | 50.8669 | 10.2255 |
| 128 | 1.64077e8 | 2.06110e7 | 3.66067e6 |

At 192 cells the omitted-mode zeroth-jet contributions are approximately
4.53e-33 to 4.55e-33; candidate nodal arithmetic is 1.50e-12,
2.34e-9,4.98e-4 at the three times. Complete tails have log10 allowances
-483.767,-452.489,-421.211. They remain positive analytical terms,
recorded logarithmically rather than called zero after underflow. All
mapped rows retain their source components and a separate tail logarithm.
Interpolation dominates each nonzero mapped source row; refining modes
or cutoff cannot address that dominant allowance. No asymptotic mesh-cost
law is inferred from three meshes.

CJ21's diagnostic source requirements, taking minima over the specified
observations, reach d0<=1.30428e-9 and d2<=1.08159e-7 for the baseline
coefficient tables. The strict d0 row is source xy at t=96,x=4,y=0;
the strict d2 row is source yy at t=64,x=4,y=0. These are source-accuracy
columns, not achieved field errors or a continuous coefficient enclosure.
Every per-observation requirement is retained in the part records.

The 80/10/10 categories all remain visible:

- **Source, 80%:** interpolation plus modes plus complete tail plus nodal
  arithmetic candidate, mapped by A,B. The estimates fail the allocation
  by the ratios above. Nodal arithmetic is not counted again as evaluator
  arithmetic. The nodal candidate `1e-12 Phi_N(binary64 node)+1e-300`
  has maximum sampled discrepancy/candidate 0.106694 against 80-digit
  exact-rational grid nodes. It remains unproved, including elementary
  function and node arithmetic; it is not certified.
- **Later evaluator, 10%:** no continuous rounding or quadrature-truncation
  enclosure is supplied. The largest sampled 6-to-10 source-rule observable
  change is 2.77112e-13 (U at t=128,x=4,y=0,192 cells), or 2.77112e-8
  of its reserved allocation. Two selected low-amplitude source-node
  cases use 80 digits and one 120-digit comparison each. Binary64 versus
  those references differs by at most 1.406e-16 in the four jets. These
  references promote the *identical* implemented nodal coefficients, so
  they isolate later evaluation/node-geometry arithmetic from nodal source
  coefficients. Tiny precision/refinement differences are diagnostics,
  not a truncation or rounding proof. The bare error-function subtraction
  is not used.
- **Filter, 10%:** the maximum 32-to-64 actual-observable change/allocation
  is 5275.90, for Delta Q at t=96,x=4,y=1/2,768 cells. The change is
  5.27590 against the separate 0.001 filter allocation. At t=64,
  768 cells,x=4,y=1/2 it is 1.45679. Derivative/source *positive allowance*
  integrals have their own failed refinement: the largest
  change/allocation is 3.35582e10, for source y at t=96,x=4,y=0,192
  cells. Observable convergence cannot pay positive-envelope integration,
  and neither refinement is a rigorous integration remainder. Both
  16-to-32 and 32-to-64 changes are retained; local positive-envelope
  32-to-64 changes are retained separately.

All actual fields include W,W_t, both curvature derivatives C_t and
square C through their spatial rows, physical B, signed source, actual Q
and Delta Q. In particular t=96,128 use full r_x,r_xx,r_tx,r_txx and
2r_x r_tx, not the pre-switch simplifications. Actual source values are
evaluated by the equivalent exact finite-field balance R_t+div J with
E=0; the source allowance bounds the independently defined signed source.
The covariance uses signed gradient squares and the actual squared means;
no correlation is replaced by a product of averages.

### Time-join budget and stopping decision

For a declared cutoff derivative constant c_theta, CJ27 would require

    (h_1,0+h_2,0)/tau <= min_(C>0)
      [theta-A*d0-B*d2-evaluator-filter-C*component_residual]/(c_theta*C),

with a nonnegative numerator for every other row as well. **Unpaid.**
Some mapped source allowances alone exceed the full target at every
candidate mesh, and evaluator/filter enclosures are unpaid. Actual
endpoint field h_i,0 and residual allowances are also uninstantiated;
PE6 observable errors are not substituted for them. Thus no positive
numerical cutoff allowance or endpoint overlap is accepted.

Stop here: interpolation, kernel/covariance amplification and peak-sensitive
integration already decide this request. No larger source sweep, new root
search, full gamma saddle/onset computation, regulator change, precision
escalation or spatial splice was attempted. The retained numerical run
uses 53.7824 seconds; exact controls rerun in 0.313443 seconds. Interrupted
implementation work and small checks are conservatively charged another
240 seconds, giving a budget debit below five minutes, versus the
30-minute aggregate numerical cap. The environment and exact timings are
in the index. This bound is numerical execution accounting, not a claim
that the whole research session took five minutes.

Two routine implementation corrections were caught before evidence was
accepted: the saddle Lambert-W argument must be
`-8*pi/t*exp(-18/t)`, not `-2*pi/t*exp(-18/t)`; and the shared scalar
cap argument needs positive moment(F_192)+3*baseline error to ensure
P_j>=sup|F_m,j|+bar_j for every mesh. Failed runs were interrupted and
excluded; both corrections and retained direct saddle residuals are
recorded. The residual is about -2.84e-14 at96 and zero in binary64 at128,
which is a check, not an exact equation certificate. These correct the
implementation to frozen r1; no mathematical contract revision is made.

**Next concrete deliverable — Analysis and numerics, Sol:** on the existing
t=64 peak observations, compare integrated LC2 cell weights and tighter
source-curvature/cell allocation against the present LC4 interpolation
allowance, and resolve the corresponding positive/filter integrals.
Extend the direct adaptive local signed-source transfer using
r_t rho+r_x Re j, retaining all coefficient derivatives, before enlarging
the switch-time trial. Keep weak transfer where its individual row wins.
A small bounded packet should choose the next source representation or
integration rule; a broad mesh campaign is not justified. The separate
spatial compatibility problem remains open, but it is not necessary to
escalate this tractable next deliverable to Astra.



## Exact common regulator

Let rb=2 log(eta C)-log(1+t^2)/2, ap=2 log M0-2 log kappa.
For 64<t<128, v=(t-64)/64 and chi=logistic(g),
g=-1/v+1/(1-v). Consequently

    chi'=chi(1-chi)[v^-2+(1-v)^-2]/64.

Set chi=0 at and below 64, chi=1 at and above 128. Every derivative
of chi of positive order vanishes at both endpoints: near the first,
chi is a smooth nonzero factor times exp(-1/v), and near the second
1-chi is a smooth nonzero factor times exp(-1/(1-v)). Thus the quotient
formula is evaluated only in the open switch interval, never by assigning
0 times infinity at an endpoint.

Set a=(1-chi)rb+chi ap and beta=chi/kappa (beta=0 before 64).
The physical r=log q is exactly a-beta x^2. The saddle equation gives

    L'=2L/kappa,
    kappa'=8L+16tL/kappa-2,
    (log M0)'=L^2-kappa'/(2 kappa),
    ap'=2L^2-3kappa'/kappa,
    rb'=-t/(1+t^2),
    a'=rb'+chi'(ap-rb)+chi(ap'-rb'),
    beta'=chi'/kappa-chi kappa'/kappa^2.

At t=64 use a=rb,a'=rb',beta=beta'=0. At t=128 use
a=ap,a'=ap',beta=1/kappa,beta'=-kappa'/kappa^2. These values include
the full physical mass and regulator; no offset is dropped.

The needed coefficient fields are

    r_t=a'-beta' x^2; r_x=-2beta x; r_xx=-2beta;
    r_xt=-2beta' x; r_xxt=-2beta';
    2 grad r dot grad r_t=8 beta beta' x^2;
    b=a'-beta+(2beta^2-beta')x^2;
    c=-2beta+4beta^2 x^2.

At a fixed time on the centered full buffer |x|<=X, exact scalar maxima
are q_min=exp(a-beta X^2), q_max=exp(a), e_*=sqrt(q_min),

    a0=max(|a'|,|a'-beta'X^2|), R1=2beta X, R2=2beta,
    T1=2|beta'|X, T2=2|beta'|, Th=8|beta beta'|X^2,
    b0=max(|a'-beta|,|a'-beta+(2beta^2-beta')X^2|),
    c0=max(2beta,|-2beta+4beta^2X^2|).

These maxima follow because the absolute value of each affine function
of x^2 is convex; beta>=0. A sampled time maximum would not enclose a
time slab. Pointwise positive-convolution diagnostics need no such claim.

## Positive source-accuracy columns

Represent each nonnegative linear map by its (d0,d2,eta_E) coefficient
triple. With CJ4's fixed a,k,b_* and fixed P2,

    s=(2a,0,0), w=(k,0,0), z=(0,0,1/(2e_*)),
    v_m=(P2 b_*+mP2 a k,a,0),
    s_t=(2P2 b_*+a0 k,2a,1/e_*),
    w_t=(2P2 b_*+2P2 a k+a0 k,2a,1/e_*),
    c_t=(6P2 b_*+10P2 a k+a0 k,6a,3/e_*).

CJ8--CJ14 then act componentwise on these triples with only addition
and multiplication by nonnegative scalars. In CJ13, e_gamma has triple
(2a L_gamma,0,0), and U_gamma^* is fixed before source refinement.
This supplies an auditable implementation without finite differences of
the source caps. For sharper pointwise evaluation, a is evaluated at
clamp(sqrt(q),m,M), and k at clamp(sqrt(q/3),m,M); b_*=(q+m^2)^-1.
The exact unrestricted maximum k is (3 sqrt(3)/8)/sqrt(q), so using
1/e_* is conservative as CJ4 states.

In particular let

    H_alpha=[D_alpha+2M_alpha R1+
             L_alpha(R2+3R1^2)]/(4pi e_*).

Then the residual coefficient C for R_t and D_E is H_alpha, and for
the actual signed source is 2H_alpha. For U_t,W_t it is L_alpha/e_*;
for averaged C_t it is H_alpha-D_alpha/(4pi e_*). Every static row,
J,Q and averaged B has residual column zero. This is a useful direct
check on the source and cutoff columns of an implementation.

## Identity derivation and 12 controls

CJ15 in strong differential form is

    4pi rho=Delta S-2 div(w grad r)+w Delta r+c_F |grad r|^2.

It follows by the two spatial derivatives of log(|F|^2+q). Subtracting
rho from Delta S/(4pi) gives the curvature formula. Differentiating this
identity at fixed physical coordinates retains both grad r_t and Delta
r_t and both terms in the derivative of c_F|grad r|^2.

For CJ16 differentiate V0 directly. The denominator derivative gives
-V1 partial_bar r, which cancels the added regulator term; the remaining
term is pi j. The signed-gradient identity follows from
square D=4 Re(Fzz conjugate F)+(r_xx+r_x^2)q. No F_t premise is used.

CJ17 follows by differentiating D using F_t=-Fzz+E. Varying CJ15 in
the direction E at fixed q gives delta S=2Re Z0, delta w=-2Re Z1,
delta c_F=-2Re(Z1-2Z2). This proves CJ18 with coefficients 2,-4,-2
and hence its strong form used in the script. Combining the potential
identity with Delta S=4pi(rho+C) gives the adaptive density equation;
direct differentiation of rho and divergence of j gives the already
defined source plus D_E. No covariance is defined to force the equation.

[exact_controls.py](../numerics/exact_controls.py) uses exact Python fractions and truncated multivariate Taylor
jets of total degree 4. There are 12 handpicked cases: F=z, z-a(t) with
a(t)=t+t^2/3, and z^2-2t; q=2 and q=2+t+t^2+x^2; at each of (t,x,y)=
(0,0,0) and (1,1/3,1/2). The varying q is globally positive because its
minimum is 7/4. The translated field has E=-1-2t/3, and the polynomial
includes the double event at zero. Each checks CJ15, both current
components, signed covariance integrand, all three CJ17 time identities,
CJ18, differentiated weak density, curvature, C_t, square C, and the
adaptive potential/density/current-source equations. Every reported
rational difference is exactly zero. No transcription correction was
found in these identities. These controls test local differential forms;
they do not certify the theta source, continuous D, filter integration,
or the nonlinear transfer inequalities.

Final exact-control arithmetic execution: 0.313442958 seconds. Python 3.10.0, macOS
27.0.1 arm64; standard library only. [EXACT_CONTROLS_20261024.json](../numerics/EXACT_CONTROLS_20261024.json) records environment, all case
inputs and all exact differences. Final exact-control script SHA-256:
e7e96188d9e53dfd44fc9278d43ec856ac9bd1e8256265fbc15b2ea585e526ec.
No web access, large sweep, precision escalation or repository write was
performed by this subagent.

The selected nonzero residuals are spatially constant (E_z=0); these
controls are not a separate direct test of a nonzero E_z term. Exact
selected identities do not validate the theta source or establish a
continuous transfer inequality. No mathematical transcription correction
was found in the frozen CJ identities.

## Control screen and provenance

The generic regulated identities and transfers permit colliding smooth
controls; no collision exclusion follows. Euler-factor controls alter the
canonical theta source, weighted-square controls alter its fixed weights
and full reflection, reflected controls lack its integer-square expansion,
and smooth/positive-primitive controls lack the unchanged theta arithmetic
source. Atomic controls fail the C2 source-density premise; the polynomial
controls used here fail canonical source representation but deliberately
pass generic holomorphic and positive-q premises, including the double
event. The two-channel exclusion in result cluster04 concerns its stated
channel class and supplies no theta-source accuracy here. The exact
canonical LC3/LC5 constants are not inherited by these changed sources.
These are premise checks against the established control catalog, not a
new numerical evaluation of every collision family. No RH, simplicity,
regulator-removal or global assembly conclusion is drawn.

The review includes a separate same-model subagent's read-only audit of
the coefficients, code, records and decision. Shared Note34 premises
remain shared; this is not independent specialist review or HDA-20.
The manuscript, prior numerical records, prior request text and other
chats' transcripts were not edited. No commit or snapshot was created.

## Reproduction

With NumPy and mpmath available, run from this investigation's numerics
folder (choose an external or ignored output folder for local reruns):

```sh
python3 exact_controls.py
python3 weak_transfer_diagnostic.py --repo /path/to/shifted-zeta-positivity --output /tmp/WEAK_TRANSFER_DIAGNOSTIC_20261024.json
```

The first script writes its small control record beside itself; the second
reads that record beside the scripts and writes an index plus three
per-time JSON records. The index records Python3.10, NumPy1.25.1,
mpmath1.3.0, macOS arm64, source hashes and frozen input matches; use its
actual recorded package versions if a later rerun differs. Source/evaluator
refinement, arithmetic and all continuous-domain gates retain the
limitations stated above.
