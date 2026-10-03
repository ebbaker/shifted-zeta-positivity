# Review of the all window mechanism and its continuation

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Exact serving variant and configured reasoning effort
are not exposed in this session and are not inferred. This is an internal
review with separate same-model analytic audits and a numerical replay,
not independent specialist refereeing.

Reviewed repository state: `ea0ec42c0d14270497525286dace08bc0df476dd`.
The working tree was clean when the review began.

## Assessment

The [outcome note](../notes/ALL_WINDOW_MECHANISM_OUTCOME_20261003.md)
correctly separates effective fixed-window reductions, obstructions to
particular estimates, and the unresolved all-window sign. I found no
substantive error in its six main conclusions. In particular, its large
counting bounds are upper bounds from pessimistic estimates, whereas its
doubly exponential scalar-tail obstruction is a necessary cost within
a precisely restricted proof strategy. These are different assertions,
and the note distinguishes them.

The results identify why independent absolute estimates lose the relevant
cancellation. They do not yet provide an unconditional estimate controlling
that cancellation. Conditional certificate completeness supplies no
termination theorem on an unbounded sequence of windows. The five
two-source calculations validate particular covariances and their
implementation; their margins provide no quantitative control of the
unbounded separation variable.

The continuation below adds two analytic results and one bounded joint
matrix certificate. The principal advance is that the *existing exact
polynomial probe* already detects every possible zero to the right of the
critical line. Its subexponential signed-prime growth is equivalent to RH
and hence to the all-window target. This removes the complete family of
probes from one formulation of the target, while making explicit the
strength of the still-unproved growth estimate. No proof of RH or of that
estimate is claimed.

## Checks of the original reductions

For the [effective relative tails](../notes/ALL_WINDOW_EFFECTIVE_RELATIVE_TAILS_20261003.md),
the identity `H-J_n=(I-E_n)H(I-E_n)` gives the claimed `k/b_(n+1)`
remainder, with rank at most `2n`. This uses a genuine spectral projection
and retains the full mixed columns. A numerical compression alone is not
such a projection. The time-band trace constant is `LR/pi`; choosing
`m(R)=E+1` gives the stated counting bound. The shifted resolvent argument
uses positive inverse order, a valid convex-chord bound, and full equation
residuals. It does not assume commutation with the trial projection.
These inputs have not been computed to give a new source gap.

For the [spatial arithmetic reduction](../notes/ALL_WINDOW_SPATIAL_PRIME_REDUCTION_20261003.md),
positive-kernel domination identifies the spectral top of `W_L` with its
norm. Simultaneous recurrence of the finite set of active prime phases
produces weakly null modulations that preserve that top Rayleigh value.
Finite-dimensional projection and exact smooth moment correction therefore
cannot reduce it. The archimedean energy of those modulations increases;
the construction is not a negative source for the joint form. The endpoint
packet calculation has the correct single cross contribution, and PNT
gives the claimed exponential arithmetic scale. Intersecting the first
`N+4` Dirichlet modes with three moments gives the required `N+1`
dimensional trial space for the scalar-tail obstruction.

For the [centered reference and completeness audit](ALL_WINDOW_MECHANISM_OBSTRUCTION_AUDIT_20261003.md),
the off-diagonal kernel is
`-exp(-5|u|/2)/(1-exp(-2|u|))`. Translated negative prepared packets
give a negative index growing at least linearly. Thus a fixed-rank repair
is impossible in that route. The signed-cutoff completeness proof correctly
retains the weakly escaped mass as `lambda(1-||u||^2)`; it is conditional
on a strict fixed-window gap. Local continuation does not exclude a first
finite loss of that gap.

For the [translated probes](../notes/ALL_WINDOW_TRANSLATED_PROBE_CRITERION_20261003.md),
only one arithmetic shift branch survives between separated supports.
The covariance therefore contains `-M_g(r)`, with no extra factor two.
Pole neutrality cancels the leading archimedean exponential exactly, and
the remaining absolute bound has the stated decay. The complete-family
density argument is valid in the smooth source class. The polynomial
probe lies in its logarithmic form closure, with exact moments preserved
by preparation and mollification. The same-model numerical auditor replayed
the original 256-bit package and reproduced all five positive margins.

This review checked the displayed analytic reductions and the small probe
implementation. It is not a fresh revalidation of every earlier Sonin
construction or of the separate full-window certificate packages cited
by these notes.

## A stronger theorem for the same probe

The [single-probe growth theorem](../notes/SINGLE_PROBE_GROWTH_THEOREM_20261003.md)
uses the same source as the original experiment:

    h(x)=(1-16x^2)^8 on |x|<1/4, zero elsewhere,
    g=(-D^2+1/4)Dh / ||(-D^2+1/4)Dh||_2.

For `H(s)=integral exp(sx)h(x) dx`, exact integration gives

    H(s)/H(0)=0F1(19/2;s^2/64).

A weighted Sturm–Liouville integration shows that every zero of `H` is
purely imaginary. Consequently the autocorrelation transform

    Phi(s)=-s^2(s^2-1/4)^2 H(s)^2 / ||(-D^2+1/4)Dh||_2^2

has no zeros in `Re s>0` except the prescribed double zero at `s=1/2`.
The width `1/2<log 2` makes the following transform identity exact without
endpoint corrections:

    integral_0^infinity exp(-sr) M_g(r) dr
       = -Phi(s) zeta'(1/2+s)/zeta(1/2+s),   Re s>1/2.

If `M_g(r)=O_epsilon(exp(epsilon r))` for every `epsilon>0`, the left
side is holomorphic on `Re s>0`. Each hypothetical right-of-line zero
would give an uncanceled pole on the right side. The zeta pole is canceled
by the prescribed moment zero. Functional symmetry then gives RH.
Conversely RH gives all-window positivity through the established explicit
formula, hence bounded covariance and bounded `M_g` for this probe.

Thus a global pairwise condition for this *particular arithmetic probe*
is sufficient. This does not contradict the original counterexample for
arbitrary kernels: the extra ingredient is the exact logarithmic-derivative
transform and its zero detection, not a general implication from two-by-two
positive minors to full matrix positivity. The union of two translated
supports still has unbounded diameter. A fixed probe does not remove the
all-support quantifier.

The theorem also permits weighted integral growth hypotheses, recorded
precisely in the proof note. These are more flexible research targets
than a sharp uniform pointwise bound. None is established unconditionally
by the current work.

## Quantitative centered negative index

The [negative-index sharpening](../notes/CENTERED_NEGATIVE_INDEX_SHARPENING_20261003.md)
observes the exact identity

    gamma(t)+1/(t^2+1/4)=Re psi(5/4+it/2)-log pi =: m_c(t).

This multiplier increases strictly for positive `t`, from a negative value
to infinity. Let `t_*` be its unique positive zero. The function
`v -> m_c(sqrt(v))` is increasing and concave. Jensen's inequality and
the derivative-energy bound on the first `n` Dirichlet modes show that
their centered energy is at most `m_c(pi n/L)`. Removing the three
moments leaves dimension at least `n-3`. In particular,

    negative_index((Gamma+J)|E_L)
        >= max(0, ceil(L t_*/pi)-4).

This supplies an explicit leading lower coefficient for the growing
negative block, with no prime estimate, RH assumption, or spectral
asymptotic theorem. It is a lower bound, not a proof of an exact asymptotic
negative index or a lower bound on the cost of every possible method.
The companion scalar certificate gives
`1.94992548206433579713 < t_*/pi < 1.94992548206433579715`.

## A joint seven-source certificate

The [bounded joint package](../numerics/single_probe_joint_20261003/README.md)
checks the full Gram matrix for translates at `0,2,4,6,8,10,12`.
The preflight fixes seven sources, the original sieve cutoff `268338`,
and just one additional separation, `r=2`. All active prime powers and
both signs of the archimedean remainder are enclosed. Outward interval
LDL factorization proves

    [Q(tau_(2i)g,tau_(2j)g)]_(i,j=0)^6 > (1/20) I.

The translates are disjoint and L2 orthonormal, so this also certifies
`Q[F]>(1/20)||F||_2^2` on their seven-dimensional span. Both 192-bit
and 256-bit records pass. This is a genuine joint test with arbitrary
complex coefficients, rather than a collection of pairwise tests.

The simple row-sum lower bound is enclosed between -1.511672 and
-1.495987, whereas all seven shifted LDL pivots are strictly positive.
The smallest pivot lower endpoint exceeds 0.01286159; that number is a
pivot bound, not an eigenvalue bound. The primary agent also reran the
256-bit generator and the consistency checker successfully. These checks
give a concrete example where the joint factorization proves the stated
margin and the elementary row-sum estimate does not.
A second, standard-library rational interval implementation also certifies
the shifted matrix directly from each saved first-row enclosure. It checks
the matrix algebra independently while relying on the original arithmetic
enclosures. The scalar centered-reference bracket also passed a primary
agent replay.

The total containing support length is 12.5. The certificate does not
cover every source in that interval, every translate of this probe, or
the weighted/global growth criteria of the new theorem. It enlarges the
verified finite-dimensional span without enlarging the original prime
cutoff. No large derived files or new manuscript snapshots were produced.

## Remaining theorem and next useful input

One exact scalar route is now to prove, for the fixed rational polynomial
autocorrelation, subexponential growth of the signed prime sum, or the
weighted integral condition stated in the theorem note. The proof that
such an estimate suffices is complete; the estimate itself remains open.
The alternative joint operator and full Gram positivity routes remain
valid, with their complementary and mixed blocks still requiring control.

An absolute PNT-error estimate does not settle the new scalar target:
it retains the factor `exp(r/2)` in the discrepancy identity. A useful next
analytic input must exploit the sign of the smoothed error or provide a
global averaged cancellation estimate. Further bounded matrices can test
such a proposed estimate, but cannot establish it by extrapolation.

The appropriate status is therefore **reviewed reductions, a sharper
equivalent scalar theorem, and a certified seven-source continuation**.
All-window positivity and RH remain unproved.
