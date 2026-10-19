# S03 G3 arithmetic investigation: internal mathematical review

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: delegated **gpt-6.1-sol**, actual inherited reasoning effort
**ultra**. This is separate same-model internal review, not independent
specialist review. The reviewer changed no repository or chat-history files.

## Verdict and permitted scope

No blocking mathematical error was found in the bounded first
heat–Stirling correction theorem in `remainder-proof.md`, in its constant
checker, or in the five-point exact finite Gaussian-mode decomposition.
The explicit correction and its modewise value/first/second physical-x
remainder are supportable as written. They concern **only the eight exact
gamma–Gaussian Dirichlet modes**. They do not bound the complete physical
residual, provide a new G3 prefix allowance, or prove uniform cancellation
between the finite modes and the Riemann–Siegel edge.

The RS hierarchy evaluated in `rs_gaussian.py` is a no-fit arithmetic
diagnostic with enclosed finite integrals. Its omitted Gaussian tails and
RS remainder are not thereby enclosed. The revised source audit explicitly
keeps this distinction. The inferred exact edge in `exact_modes.json` is
certified at the specified points by subtraction from the existing complete
theta-source enclosure; it is not an independent arithmetic edge certificate.

Repository policy context read: `AGENTS.md`, `LARGE_FILES.md`,
`result-summaries/README.md`, `avoid/README.md`; the relevant mathematical
comparison is S03 Note 03's complete filtered residual, rather than generic
leading-pair annihilation. Applicable pitfalls are normalization/factors
(avoid/08), splitting signed pieces before taking bounds (avoid/12), and
status exceeding evidence (avoid/06).

## First correction and uniform proof

Let `a=alpha(s)-log(n)` and `delta=sqrt(t)w+t*a/2`. Completing the
Gaussian square gives exactly

    r_n/g_n = E exp[S(s+delta)+m0(s+delta)-m0(s)-alpha(s)delta].

The contour shift remains in the lower half-plane; gamma poles are never
crossed. Gaussian decay dominates the gamma growth on connecting ends.
The branch in the proof is the analytic Stirling logarithm of gamma, as
required; using the principal logarithm of the gamma *value* would be wrong.
The proof does not do that.

`E delta^2=t/2+t^2*a^2/4`, so the retained coefficient is exactly

    kappa_n = 1/(6s) + alpha'(s)*(t/4+t^2*a^2/8).

The signs and factors of two are correct. `1/(6s)` is the first
**logarithmic** Stirling term after substituting `s/2`; the exponential
remainder in the proof pays the difference between logarithmic and
multiplicative correction. The curvature term is prescribed by Gaussian
averaging, with no coefficients fitted to physical-source values.

On the enlarged complex-s domain, `|s|,|s-1|>=494.5` and `|s|<505.6`.
The `|a|<2.35` cap is valid for `1<=n<=8`. For maximum clarity the saved
proof can spell out that

    Re alpha >= (1/2) log(494.5/(2*pi))-1.5/494.5 > log(8),

so subtracting `log(n)` only reduces the positive real-part contribution
to the displayed norm bound. This is an explanatory clarification, not
a failed inequality.

The central logarithmic-gamma remainder follows directly from
[DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii): retaining the `B2` term
and substituting `s/2` gives `sec(arg(s)/2)^4/(45|s|^3)`. The stated
sector and distance bounds validate its use. The elementary reciprocal
difference, cubic Taylor remainder, and exponential remainder are all
paid. The Gaussian moments and the combination of their majorants are
correct.

I independently replayed `check_remainder_constants.py` at 192 and 256
bits. All its assertions pass. The unrounded central error bound is

    5.6288339719216981123909562222381362449e-7 < 6e-7.

For the `|w|>=40` tails, the gamma recurrence to real part `[1,2]`
works for every negative real part because all recurrence denominators
have imaginary part of modulus greater than 247. For positive real part,
the gamma integral estimate and `sigma<=.3|w|` give the claimed
`exp(.09w^2)` bound. The polynomial, pi, and linear-exponent factors
give the stated aggregate `exp(450-.86w^2)` bound. Its initial-point
and derivative comparisons are sound. The omitted tails of `1+q` have
the separate Gaussian-polynomial payment. Neither tail uses a fixed-sector
Stirling estimate at horizontal infinity.

The exact normalized error is holomorphic on a neighborhood of the
enlarged domain. Its value estimate on radius-5 s discs is therefore
available on radius-10 **physical x** discs. Cauchy yields

    |e_x| < 6e-8,       |e_xx| < 2!*6e-7/10^2 = 1.2e-8.

This factor conversion is correct and does not differentiate a real
envelope. The lower channel's product rule is also correct:

    L(g_n e_n)/g_n = sigma_n e_n
       +(2i*omega+2lambda_n-mu)e_n,x+e_n,xx.

The upper channel uses its conjugate version. The `n=1` annihilation
removes the `sigma_n` and `lambda_n` terms there, leaving only derivatives
of the small correction. It does not annihilate the full correction or
the modes near the cutoff.

## Exact finite-mode point computation

I read `probe_exact_gaussian_modes.py`, independently replayed its
complete 192-bit five-point run using the pinned setup
`/private/tmp/s03-correlated-reference/SETUP.json`, and saved
`review_exact_modes_192.json`. The 192-bit run objects are identical to
the author's retained output. The source setup SHA-256 is
`abd7889c7880e6acd941e95f0a103ab19601e68edec8267a8eb5c377376938d9`.

For a fixed point, the finite integral contains the actual gamma factor,
not its Stirling approximation. Differentiating the physical mode gives
the correct factors `-i*(M'/M-log n)/2` and
`-[(M'/M-log n)^2+(M'/M)']/4`. Conjugating the channel gives `2 Re` of
each derivative. Normalizing to Q jets includes all A derivatives through
`b,b_x`; the defect includes `omega_x` with the correct sign.

The unshifted Gaussian tail payment has a valid independent basis.
[Polymath Lemma 5.1(v)](https://arxiv.org/html/1904.12438v2#S5)
provides `|S(z)|<=1/[6(|z|-.66)]` for `|Im z|>=2`, uniformly in the
real part. Direct differentiation gives
`|alpha'|<=1/[2(Tlo-3)]` along each horizontal segment. Thus the code's
`exp(-c*v^2+beta*|v|)` envelope is valid. Its integrated denominator
is positive, and its channel and two-tail factors are correct.
The bound is uniform on radius-1 physical-x discs, so Cauchy factors
`1,1,2` pay the first two derivatives of the omitted infinite tails.

At `t=21/200,x=1000`, the independently replayed normalized defects are

| Component | Defect R |
| --- | ---: |
| Exact finite-mode correction | `+0.000133439544936848` |
| Inferred exact edge discrepancy | `-0.000136027672101115` |
| Complete residual | `-0.000002588127165638` |

The complete-source radius is `7.05e-11` at this point. The first
heat–Stirling correction differs from the exact finite-mode defect by
about `1.1974e-8`, consistently with its much smaller modewise remainder.
These numbers support a concrete center diagnosis. They do **not** prove
that this signed cancellation persists on B: at `x=999` the complete
defect is approximately `+0.0002929720`, and at `x=1001` approximately
`-0.0002374900`.

## Edge hierarchy and finite coherence identity

The displayed `C1` and Gaussian-mean `C2` coefficients agree with direct
expansion of the stated exact d-coefficient recurrence. The `eta_bar`
term retains the rational alpha part, leading Stirling coefficient, and
quadratic moment with the correct factors. Both `C1/a` and `eta_bar F`
are needed: their recombined physical contributions have opposite signs
at the pilot, and the eta term is larger.

I also independently differentiated the revised finite auxiliary profile
`A_K=U*a^(-u)*sum Cj*a^(-j)`. Using the stated coefficient identity,
all interior terms in `(partial_tau-i partial_u)A_K` cancel, leaving
exactly the two endpoint terms in the source audit's equation (I).
The path `(u-y/2+lambda*y/2,tau+i*lambda*y/2)` keeps the exact gamma
argument constant and has the claimed derivative. This offers a coherent
complex-disc remainder route, but its endpoint suprema, negative-u order
conditions, full Gaussian tails, and complete RS remainder must still be
evaluated before it is used for physical jet certification.

## Conclusion

The bounded finite-mode theorem and source-checked five-point diagnosis
can be saved as the completed bounded output of this investigation.
The arithmetic explanation of full G3 is **partial**: the work identifies
and controls the finite gamma/heat contribution and explicitly locates the
missing signed edge cancellation. It establishes no complete arithmetic
G3 allowance, no new coverage, no general collision exclusion, and no
all-height cancellation law.

## Final assembled note and finite-error ledger review

I subsequently reviewed the assembled
`06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md`,
`check_heat_stirling_remainder.py` with
`HEAT_STIRLING_REMAINDER_192_256.json`, and
`check_rs_edge_hierarchy.py` with `RS_EDGE_HIERARCHY_20261019.json`.
No blocking error was found in their mathematics or their declared scope.
The assembled note correctly states that both point runs use the same
historical 192-bit complete-source setup; increasing the finite-mode
arithmetic precision is not a second source quadrature.

The new finite-error ledger is a uniform outward interval image of the
entire real B box. In particular, the normalized mode rate is
`i*omega+lambda_n`, with acceleration
`(i*omega+lambda_n)^2+i*omega_x+lambda_n,x`; the physical rates add
`b` and `b_x` in precisely the required product-rule positions. The
filtered ledger retains `sigma_n`, uses both conjugate channels, and
divides by the **lower** modulus of omega squared. It pays the finite
error after the signed retained correction; it does not replace that
correction by its absolute value.

I independently replayed that new ledger at 192 and 256 bits. The
results are retained in `REVIEW_HEAT_STIRLING_REMAINDER_192_256.json`.
Both precisions reproduce the author's totals:

| Finite remainder payment on all B | Safe upper bound |
| --- | ---: |
| Normalized value | `5.206260e-6` |
| Normalized first x derivative | `3.404651e-6` |
| Normalized second x derivative | `2.961263e-6` |
| Physical first derivative divided by A | `4.240070e-6` |
| Physical second derivative divided by A | `3.923632e-6` |
| Normalized filtered defect | **`3.874872e-6`** |

The filtered unrounded upper value is
`3.8748711618956029724617249503276257522e-6`. These payments consume
the companion proved relative-mode bounds, rather than numerically
proving the theorem. Their conditional wording identifies a proved
mathematical input; it does not hide a physical-source or edge assumption.

The reorganized RS hierarchy preserves its prescribed coefficient
recurrence, coherent physical-x differentiation, exact gamma prefactor,
and explicit unpaid remainder list. I independently replayed it at
192 bits, including all 126 exact rational coefficient identities, in
`REVIEW_RS_EDGE_HIERARCHY_192.json`. The printed K=0 through 4 defects
agree. I did not repeat a separate 256-bit hierarchy replay; the author's
256-bit record was read and has consistent results and scope.

One exposition clarification was sent to the parent: introduce the
enlarged domain explicitly as the union of closed radius-5 s discs about
`(1-ix)/2` for `999<=x<=1001` before using its central bounds. The last
derivative paragraph already specifies those discs, so this is not a
counterexample or a changed constant. The new ledger does not alter the
main scope conclusion: a complete independent arithmetic edge jet and
signed spatial-prefix payment remains the next mathematical obligation.

### Final script refresh

After the exact-mode probe explicitly restored the requested arithmetic
precision before every point and immediately after the historical source
evaluator, I reran the current script at 192 bits and replaced
`review_exact_modes_192.json`. The change prevents the historical
192-bit source evaluator from silently lowering later work in a 256-bit
run; the independently replayed 192-bit results remain unchanged.

The hierarchy script also now records the separate first formal
`C1/a`, `eta_bar*C0`, and mean `C2/a^2` profiles. I checked those
expressions against the already reviewed formulas, replayed the current
script at 192 bits, and replaced `REVIEW_RS_EDGE_HIERARCHY_192.json`.
The displayed signs and values agree, including the positive `C1`
defect and larger negative gamma-prefactor defect. Both refreshed
reviewer records' `script_sha256` fields match their current scripts.
No mathematical scope was enlarged: the complete edge remainder and
signed spatial-prefix estimate remain open.

## Retained paths

The reviewed finite-mode proof is included in [Note 06](../notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md).
Temporary producer names in this review map to
[exact Gaussian modes](../numerics/probe_exact_gaussian_modes.py),
[heat remainder checker](../numerics/check_heat_stirling_remainder.py),
and [RS hierarchy checker](../numerics/check_rs_edge_hierarchy.py).
Retained replays are [exact modes 192](../numerics/S03_G3_EXACT_MODES_REVIEW_192_20261019.json),
[heat constants and ledger 192/256](../numerics/S03_G3_HEAT_REVIEW_192_256_20261019.json),
and [RS hierarchy 192](../numerics/S03_G3_RS_REVIEW_192_20261019.json).

[Saved file identities and precision overlap checks](S03_G3_FILE_IDENTITIES_20261019.json)
record code/source pins,120 exact-mode ball overlaps and33 hierarchy/term
ball overlaps; these checks support the stated scope only.
