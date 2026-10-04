# Internal review of the first selective Schur loss continuation

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Separate agents with the same model
configuration checked the block algebra, source domains, head selection,
residual lifting, and exact source geometry. This is an internal check,
not independent specialist refereeing.

Reviewed the [program overview](../notes/selective-loss-program/overview.md),
[first approach note](../notes/selective-loss-program/01_schur_completion_20261003.md),
and [exact covariance package](../numerics/selective_loss_schur_20261003/README.md).

## 1. Algebra and domain checks

The full Schur identity retains the mixed columns G=PHU and assumes the
independently certified full-tail inequality D>=delta I. Its sign is
S=I-H00-G*D^(-1)G. The completed tail square is nonnegative, so clipping
the finite S produces a valid positive main and finite loss.

The approximate-response identity was expanded directly:
S=S_Y-R*D^(-1)R with R=G-DY. In particular S_Y is an upper approximation
to S. The finite lower certificate pays the full weighted residual.
Unobserved complementary rows cannot be omitted. The note explicitly
avoids applying a matrix negative-part function to a Loewner inequality.

The template head U=B^(-1/2)W G0^(-1/2), G0=W*B^(-1)W, is an isometry
when W has independent columns. Its range is in V=D(B^(1/2)), and its
source coefficients are G0^(-1/2)W*F. The pullback loss is therefore a
bounded finite-rank L2 source form. Adding that loss to the closed
semibounded form Q gives a closed positive main once the certificate
is proved. No form-domain assumption on W is required beyond membership
in the prepared source Hilbert space.

The raw Gram congruence is T0=G0^(1/2)S G0^(1/2). A certified M0<=T0
and the joint test M0+G0 Lambda G0>=0 imply Q[F]+(W*F)*Lambda(W*F)>=0.
This avoids separate scalar bounds on G0 inverse. It does not prove that
the prescribed template head has a safe complement.

The two-profile sum and difference allowances were checked by an exact
two-by-two matrix congruence. A large difference allowance can accommodate
the mixed entry when the sum diagonal has a positive margin. It cannot
repair a negative sum diagonal. The target sum source is charged exactly
the sum allowance.

The lift R0=D^(1/2)Z0 gives residual energy Z0*Z0. The generalization
D>=t M_tail and R0=M_tail^(1/2)Z0 gives an upper matrix t^(-1)Z0*Z0.
The note requires an independently constructed and controlled full lift;
merely naming the inverse square-root lift supplies no estimate. The
boundary metric I-C^2 is distinguished from this relative source metric.

## 2. Exact continuous source geometry

The numerical package uses standard-library rational arithmetic. It
reconstructs g0=-h'''+h'/4, independently checks its squared norm, and
derives the compact autocorrelation polynomial on [0,1/2]. The
normalization, zero integral, and endpoint value are checked exactly.

Direct integration of both half-shell overlap vectors agrees with the
structured four-by-four covariance. All 15 principal minors of Xi and
of Xi-I/32 pass exact positivity checks. The moving-block row sums give
Xi<=I/2. Thus I/32<Xi<=I/2 is a rational certificate covering every
integer shell j>=2 by translation of the physical templates. The root
agent replayed the calculation successfully.

These facts imply the valid shell identity A_j=Tr(Lambda_j Xi) and
pointwise bound L_j(r)<=32 A_j for one common positive four-template
allowance. That finding limits the benefit of averaging in this fixed
family. It says nothing about a changing head or an r-dependent allowance.

The physical templates capture mean ordinary L2 energy approximately
0.62696836166. This is not a measurement of B energy or the transformed
relative complement. No Sonin operator or arithmetic positivity matrix
was computed.

## 3. Scope and unresolved obligations

The saved work establishes fixed-window algebra and source geometry,
with all positive-main claims conditional on stated complement and
residual certificates. It does not establish useful growing-window
complement constants, a polynomial head-size bound, the required source
weighted resolvent bound, or RH.

A fixed-window safe head can be obtained from actual B eigenvectors
with k/b_(n+1)<1, using the existing K norm estimate. The current
worst-scalar constants make this a potentially enormous construction.
Augmenting a template head requires accounting for the source overlaps
and losses of all added vectors. The special two- and four-template
formulas do not cover those contributions automatically.

Schur loss is not pointwise ordered with the exact relative spectral
loss. Enlarging a head does not automatically reduce its clipped source
loss. The note gives explicit counterexamples or cautions and retains
the independent full-tail obligation. The source-specific scalar target
is not claimed to be an already proved estimate.

Applying the established one-sided theorem still requires either a bound
for every sufficiently large real separation or the stated global weighted
integrability condition. Finite windows and the exact correlation
calibration provide neither. Support-adapted prime sets and full
prime-power definitions are retained.

## 4. Repository checks

The new records are small and follow the repository large-files policy.
Markdown local links, displayed-math delimiters, and whitespace were
checked. The source covariance record includes its generating script hash;
exact rational sign checks, rather than the hash or diagnostic decimals,
justify its inequalities.

Existing research changes were preserved. The manuscript and draft-history
hashes were checked before and after this continuation and remained
unchanged. No synchronized ChatGPT reference file was edited. No
manuscript snapshot, commit, push, or large numerical run was created.
