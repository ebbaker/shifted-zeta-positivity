# Internal review of the compensated stationary sign construction

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

This review concerns the next bounded construction requested in
[Note 7](../notes/7_CONTINUATION_AND_NEXT_SIGNED_ESTIMATE_20261014.md).
It is an internal LLM mathematical and implementation review, not specialist
refereeing or formal verification. A separate reviewing agent read the
analytic derivation and numerical source and replayed the cell calculation
independently. The recorded result certifies both stationary signs on the
whole padded rectangle; no sign or branch cells remain unresolved there.

## Exact observations and index payment

For the genuine source, write \(h_k=p_k+r_k\), where
\(p_k=\sum_{n\le N}a_{n,k}\) comes from the endpoint-compensated
channels. Expanding the quadratic form gives

\[
\mathscr L_j(H)=D_j+X_j+2p_{j+1}r_{j+1}+r_{j+1}^2
-p_jr_{j+2}-p_{j+2}r_j-r_jr_{j+2}.
\]

On **genuine** stationarity, \(h_{j+1}=0\), the substitution
\(p_{j+1}=-r_{j+1}\) yields exactly the identity and sufficient
signed inequality stated in Note 7. In particular the square remainder
has sign **minus** after this substitution. The payment

\[
B_j=\varepsilon_{j+1}^2+|p_j|\varepsilon_{j+2}
+|p_{j+2}|\varepsilon_j+\varepsilon_j\varepsilon_{j+2}
\]

is sufficient if \(D_j+X_j\ge B_j\) throughout a cell that can
contain genuine stationarity. This is algebraically the requested
cross-term inequality \(X_j\ge-D_j+B_j\). Evaluating the aggregate
form can reduce interval dependency; it is legitimate only with the exact
identity retaining every off-diagonal pair. Separate channel signs are
neither assumed nor needed.

The displayed K=2 functions have the required first and third derivative
Kronecker jets. The complete-source odd jets cancel their subtractions.
The manuscript's all-index majorant is analytically sound at K=2,N=3:
\(\alpha_4=16\pi>25=8K+9\), and every positive exponent in the
geometric sum is at most five. Negative exponents in \(T_s\) cause no
problem. The ratio proof uses \(2s\le\alpha_n\) and bounds successive
terms by \(e^{-\pi(n+1)}\), giving the stated denominator at n=4.
The four integrations by parts have vanishing boundary jets for each
physical derivative through order three, with the correct sine/cosine
parity. This is an absolute four-jet bound on a bounded-height domain.

## Requirements for a rigorous cell cover

Every physical jet enclosure must pay all omitted theta indices, the
finite integration endpoint, endpoint-compensation integrals, numerical
integration, rounding, and variation throughout its time/height cell.
The Gaussian-polynomial compensation tails must be paid for each
individual channel when computing D and X. A small aggregate compensation
coefficient does not by itself bound the individual channels.

A direct cell exclusion requires the **genuine** enclosure of
\(h_{j+1}\) to exclude zero. A second valid exclusion proves uniform
strict endpoint signs and separates \(h_{j+2}\) from zero throughout
the cell; spatial monotonicity then excludes a zero between the endpoints.
Both tests concern the genuine jets. Truncated stationarity and sampled
values cannot decide this. An unresolved or degenerate cell must remain
in the record unless its sign is itself certified. Nonvanishing
\(h_{j+2}\) alone proves spatial regularity; opposite strict endpoint
signs additionally prove branch existence and uniqueness. A cover by
closed cells must include their common boundaries and the padded
rectangle's boundaries.

Signed coverage on all of
\(R^+=[1/200,3/50]\times[7,41]\) supplies an open interior containing
the smaller target \(R=[1/100,1/20]\times[8,40]\). The local heat
collision theorem therefore applies in that interior. The strict first
stationary sign obtained here also excludes a joint zero directly on
the whole closed R+: at \(H=H_x=0\), one would have
\(\mathscr L_0=0\), contradicting its positive margin.
Only the complete theta family satisfies the heat equation used in the
collision theorem; compensated finite channels generally do not. No
reciprocal of an unproved physical norm, or ambient Fueter formula omitting
its residual, is used to establish the sign.

## Shifted polynomial controls

Put \(h=T-t>0\), \(y=x-24\), \(T=1/40\). Both controls satisfy
\(Q_t=-Q_{xx}\) and collide at an interior point of R.

For \(Q_2=y^2+2h\), its first stationary predecessor is y=0, with

\[
\mathscr L_0(Q_2)=-4h,\qquad
\mathcal E(Q_2)=4h^2,\qquad
\frac{-\mathscr L_0}{\mathcal E}=\frac1h.
\]

Its second stationary set is empty because \(Q_{2,xx}=2\).
For \(Q_3=y^3+6hy\), its second stationary predecessor is y=0, with

\[
\mathscr L_1(Q_3)=-36h,\qquad
\mathcal E(Q_3)=36h^2,\qquad
\frac{-\mathscr L_1}{\mathcal E}=\frac1h.
\]

Its first stationary set is empty for h>0 because
\(Q_{3,x}=3y^2+6h>0\), and everywhere
\(\mathscr L_0(Q_3)=3y^4+36h^2\ge0\). Thus both stationary levels
are necessary. The controls defeat any claim based only on heat,
analyticity, or quaternion regularity. Their first-jet polynomial data do
not equal the fixed complete theta source and its compensated integral
observations. A theta certificate identifies that source by evaluating
and paying those observations, not by a universal heat-sign assertion.

## Analytic signed overlap estimate

[Note 8](../notes/8_COMPENSATED_STATIONARY_SIGN_DERIVATION_20261014.md)
pays the entire source in a strengthened signed fourth/sixth moment.
Its source-core bounds follow by differentiating
\(q(2q-3)e^{-q}\) and using the positive first theta summand.
The complete upper tail uses the manuscript's all-index envelope,
concavity of its logarithm, and an explicit exponential payment.

The sign change of \(u^4(1-32u^2/3)\) occurs above the tail anchor
3/10. The derivation handles this correctly: on the tail it uses the
nonpositive lower bound
\(-(32/3)u^4(u^2-(3/10)^2)\), whose Gaussian-free exponential integral
is exactly paid. It does not substitute an upper source envelope into
an unseparated signed integrand.

The global sine inequality then gives a positive \(h_3\), while the
previous complete-source moment gives negative \(h_1\). Their product
proves the signed \(\mathscr L_1\) estimate on the entire overlap band.
Its transfer to the compensated sum includes the general, unrestricted
quadratic error \(2|p_2|\varepsilon_2+E_1\). Consequently the claimed
\(10^{-10}\) cross-term surplus holds on the whole band, without a
stationarity hypothesis or an assumption that a stationary set meets it.
The genuine jet caps used here are proved in the manuscript for all real
x and \(0\le t\le1\).

The rational
[checker](../numerics/check_compensated_tail_and_signed_overlap.py)
was read independently and replayed from a temporary copy outside the
repository; all 46 exact rational checks passed. Its positive-polynomial recurrence, Gaussian moments,
complete geometric-index majorant, source-core comparisons, and signed
moment and error-payment formulas match the analytic argument. The
extension of the moment gap to \(0\le t\le1\) uses the valid slightly
sharper tail envelope \(e^{-32(u-3/10)}/49\). Its rational Machin
alternating-series bound and tangent identity establish the needed
\(\pi>333/106\), with the usual acute-angle branch of Machin's identity.

## Cell implementation and recorded outcome

The full
[certificate source](../numerics/certify_compensated_stationary_theta.py)
and [record](../numerics/COMPENSATED_STATIONARY_THETA_CERTIFICATE_20261014.json)
were inspected independently. They use Python 3.10.0, python-flint 0.9.0,
and 256-bit Arb/Acb arithmetic. All deciding values are enclosures.
The quadrature result's returned radius enters the jet enclosure, rather
than being replaced by its requested tolerance.

Finite raw theta channels are integrated on [0,1]; their whole remaining
half-line is paid by the explicit concavity envelope. Absolute source
moments at \(t=3/50\) pay both the order-five time Taylor remainder and
the order-twelve spatial Taylor remainders. The raw channels obey heat;
the compensation coefficients are carried explicitly as affine time
functions. This correctly handles the finite-channel heat residual.
The Gaussian transform is integrated on the full half-line through its
entire erfi formula and exact moment recurrence. Its order-twenty-four
spatial Taylor remainder uses Gaussian moments, not theta moments.
Every omitted theta index is paid by the manuscript's K=2 all-index bound.

The aggregation subtracts summed endpoint coefficients once, preserving
their cancellation. The formal coefficientwise expansion in all retained
jet variables checks \(D_j+X_j=p_{j+1}^2-p_jp_{j+2}\). The exact
general identity also follows directly by collecting each ordered index
pair. Thus deciding the signed surplus with the sharper aggregate
enclosure is mathematically legitimate. The individual D and X
enclosures can be much wider and can include negative values; no separate
positivity assertion is made.

The final cover consists of 34 closed unit spatial cells, each spanning
the full time interval [1/200,3/50]. An independent exact-rational check
of the stored dyadic endpoints verifies widths, endpoints 7 and 41, and
equality of all neighboring endpoints. The final classifications are:

| Level | Stationarity excluded | Unique regular stationary branch |
|---|---:|---|
| j=0 | 33 cells | [31,32] |
| j=1 | 32 cells | [9,10] and [34,35] |

Every retained branch has a next derivative separated from zero and
opposite endpoint signs uniformly in time. The exclusions in [30,31]
at j=0 and [33,34] at j=1 use the rigorous monotonicity test described
above. There are no unresolved sign cells, unresolved branch cells,
or retained degenerate cells on this cover.

The recorded strict surplus targets imply throughout R+:

\[
h_1=0\ \Longrightarrow\ \mathscr L_0(H)>5\,10^{-10},\qquad
h_2=0\ \Longrightarrow\ \mathscr L_1(H)>10^{-11}.
\]

All three retained lower dyadic surpluses exceed their declared rational
targets. The smallest retained lower surplus is greater than
\(1.4\,10^{-11}\), on [34,35] at j=1.
The reviewing agent's replay returned PASS with the same classifications;
after removing only the elapsed-time field, its final JSON record equals
the repository certificate. All 25 exact interpolation, polynomial
identity, and shifted-control checks passed. Its temporary record remains
outside the repository. The final source
and execution record are bound by the recorded SHA-256.
That hash identifies the inspected source; the analytic estimates and
ball arithmetic, rather than the hash, establish the inequalities.

## Remaining scope

Even a complete certificate on R+ leaves times and heights outside its
cover untreated. Evenness transfers a bounded statement to negative
heights, but neither finite-height compensation nor absolute jet accuracy
provides an all-height relative sign estimate. Global RH remains open in
this investigation.
