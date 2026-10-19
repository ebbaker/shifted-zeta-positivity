# S04 full-cutoff scaling: internal assessment

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**. The authoring assistant integrated a separate same-model
reviewer's mathematical inspection and fresh numerical replay. This is
internal LLM review, without independent specialist review.

**Disposition:** no blocking mathematical or checker issue found in the
bounded opening contract. The [note][note] is **proved in-note**, importing
the established complete Riemann–Siegel contract. The finite interval
checks and analytic proof have different roles.

## Mathematical checks

The reviewer checked the exact complex defect identity, its fixed-time
derivative, and the elementary real-axis estimates for alpha, alpha prime,
and the complete weight mass. The constants multiplying exp(-d_*/t) in
the two scaled coordinates are each below 0.7; their Euclidean bound is
below one. The proof applies to every prefix M<=N on kappa in [1,2],
0<t<=1/20, without an exchange of limit and growing sum.

The scalar model's derivative uses L_x=1/x at fixed t,M. Its exact Omega
and amplitude-derivative cosine term are retained. Holding kappa fixed
while taking the physical x derivative would be incorrect. The code's
stable per-mode derivative difference agrees with the differentiated
scalar; its independent short-series transition check also passes.

The AB/C payments, normalizer conversion, and all permitted natural-to-fixed
cutoff changes follow the current exterior contract. The checker uses mhi
in the AB multiplier to dominate both possible natural cutoffs. Cauchy
gives eta_M/R=L*eta_M at the center. The factors in the return
(H,Hx)/A=(Q,Qx+aQ) are correct. Both the authoring assistant and reviewer
checked [Polymath Theorem 1.3][polymath] and its effective error formulas;
the source theorem remains an imported input, not independently re-proved.

The generic prefix proposition does not extend the earlier uniform
5*exp(-b_*/t) source payment to arbitrary short prefixes. The note restricts
that assertion to the natural-center contract and uses a fresh explicit
eta_M for its fixed-cutoff crossing. Its symbolic center has exactly
natural cutoff 22027; the entire analytic disk permits 22026 and 22027.
Only fixed-cutoff functions are differentiated.

## Numerical checks and replay scope

The authoring assistant executed the [checker][code] at 192 and 256 bits
with python-flint 0.9.0. Each run encloses three point jets and a fixed-cutoff
crossing disk. The separate reviewer freshly ran the 192-bit checker to
`/private/tmp/s04-review.json`, reproducing all four printed model-error
bounds and complete scaled-jet lower bounds. The reviewer inspected the
256-bit record's matching script/source identities and agreement at the
displayed precision, without independently executing that precision.
The main records are [192-bit][r192] and [256-bit][r256].

The four model-vector differences are below 3.851e-11, 1.300e-11,
1.298e-11 and 4.746e-11. Fresh complete-source disk errors eta_M are
approximately 0.002481, 0.001815, 0.001700 and 0.008852. They dominate
the added model defect and are separately paid. The complete scaled-jet
norm lower bounds exceed 0.4678, 1.1875, 1.1765 and 2.7399 at those
points. No time-height cell cover is inferred from those point values.

All phases, low/intermediate/terminal signed sums, rounded balls, and
physical first-jet conversion are retained. There is no extra source
quadrature or unreported source cutoff: the complete source representation
is the imported analytic theorem. Repeating finite arithmetic at a higher
precision does not independently establish that theorem or the uniform
analytic proof.

The [fresh source-specific control replay][controls] rejects five prior
event boxes and the separate Euler negative-Laguerre witness. Their own
sources and errors are used, with no theta constants substituted. These
checks validate the inherited rejection interface, not the new analytic
replacement theorem. The note names the missing theta-specific premises
for controls without an effective numerical event box as well.

## Gate, credit and limitations

The explicit derivative-consistent full-cutoff replacement gate passes.
The earlier uniform source remainder, exact signed vector, coordinate
asymptotics, absolute mass obstruction, and signed terminal-edge reduction
are credited. This round supplies no improved *total* approximation error,
evaluation-cost gain, uniform signed lower bound, effective exterior onset,
or new time-height exclusion region. In particular the small extra payment
is compared with an existing upper bound, rather than with an unknown
actual error.

The coefficientwise warning is scoped correctly: deleting the growing
Gaussian amplitude drift or the order-one terminal heat phase fails as
the stated uniform summand approximation. This does not prove divergence
or a lower bound for the complete signed field, or rule out another signed
asymptotic. Only the first jet is paid. A second-derivative rotation or
Laguerre consumer needs an additional proof and payment.

The continuation should target a retained signed arithmetic quantity with
a strict gain over its current allowance. Further amplitude plots, higher
heights showing the same absolute mass, or the reformulated nonvanishing
target alone would not advance this gate. The global real bridge and the
complex exterior remain open. See the repository [result summaries][summaries]
and [patterns to avoid][avoid], especially [collision controls][control-summary],
[scoped claims][scope] and [preserving cancellations][cancellation]. Exact
file identities are in the [opening manifest][identities].

[note]: ../notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md
[code]: ../numerics/check_time_height_scaling.py
[r192]: ../numerics/S04_SCALING_192_20261018.json
[r256]: ../numerics/S04_SCALING_256_20261018.json
[controls]: ../numerics/S04_CONTROLS_20261018.json
[polymath]: https://arxiv.org/html/1904.12438v2#S1.Thm3
[identities]: S04_OPENING_FILE_IDENTITIES_20261018.json
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[control-summary]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[cancellation]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
