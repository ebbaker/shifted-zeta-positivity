# Full threshold time cover and a physical norm gap through height 41

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**,
verified in the current turn's transcript metadata. Parallel agents
performed the numerical extension, analytic continuation derivation,
and internal review; these are LLM checks, not specialist refereeing.

The construction in [Note 8](8_COMPENSATED_STATIONARY_SIGN_DERIVATION_20261014.md)
now extends from its short time band to the whole closed rectangle

\[
Q^+=[0,1/2]\times[7,41].
\]

Throughout Q+, with h_k=partial_x^k H and L_j=h_(j+1)^2-h_j h_(j+2),

\[
h_1=0\ \Longrightarrow\ L_0>5\,10^{-10},\qquad
h_2=0\ \Longrightarrow\ L_1>10^{-11}.
\tag{1}
\]

A separate direct enclosure establishes |H+j H_x|>1.89*10^(-6) on Q+.
The complete-source central norm and signs overlap Q+ on [7,8].
Evenness therefore gives the convenient uniform conclusion

\[
\boxed{|F(t,x)|>\frac9{5000000}\quad
       (0\le t\le1/2,\ |x|\le41).}
\tag{2}
\]

Both stationary signs hold throughout this whole strip. Thus any
positive threshold collision, if one exists, must have |a|>41. The time
gaps listed at the end of Note 8 are now closed at these heights.
No all-height RH conclusion follows.

## 1. Exact cover and retained observations

The new [parameterized driver](../numerics/certify_compensated_stationary_time_extension.py)
imports the original reviewed source machinery without changing it.
Its [execution record](../numerics/COMPENSATED_STATIONARY_TIME_EXTENSION_20261014.json)
binds both Python sources by SHA-256. The cover is exactly

\[
[r/16,(r+1)/16]\times[k,k+1],\qquad
r=0,\ldots,7,\quad k=7,\ldots,40.
\]

There are 272 closed cells and eight closed time slabs. The rational
cover audit checks endpoints, strict widths, adjacency, and full spatial
coverage on every elementary time slab. Their shared boundaries and all
outer boundaries are included. No adaptive subdivision was necessary.

The run retains K=2, N=3, the exact compensated diagonal/cross-term
identity, and the genuine stationary error formula of Note 8. It uses
256-bit Arb/Acb arithmetic, source cutoff U=1, spatial Taylor order 12,
time Taylor order 5, and Gaussian Taylor order 24. Python 3.10.0 and
python-flint 0.9.0 are recorded. Its measured execution time was
40.755 seconds; the compact record is 666,674 bytes, below one MiB.

## 2. Why the larger time interval is paid

For each slab the driver sets the raw-source center t_c to its exact
midpoint, radius d=1/32, and moment-majorant time t_+ to its right
endpoint. It recomputes all retained positive moments at that endpoint.
This updates all three time parameters, rather than changing only a
printed domain label.

For eta=x-x_c, tau=t-t_c, and
J_(n,k)=partial_x^k G_n(t_c,x_c), the retained polynomial is

\[
T_{n,k}=\sum_{\ell=0}^4\sum_{m=0}^{11}
\frac{(-\tau)^\ell\eta^m}{\ell!m!}J_{n,k+2\ell+m}.
\]

Its whole-cell remainder is at most

\[
\sum_{\ell=0}^4\frac{d^\ell}{\ell!}
\frac{(1/2)^{12}}{12!}M_{n,k+2\ell+12}(t_+)
+\frac{d^5}{5!}M_{n,k+10}(t_+),
\]

where M_(n,m)(t_+)=int_0^infinity u^m g_(n,t_+)(u)du. Positivity,
monotonicity in time and the raw heat equation justify these bounds.
The affine compensation e_n+6t b_n is then evaluated on the whole slab;
the finite-channel residual is retained exactly.

Every source-jet and moment integral on [0,1] uses its validated returned
Acb quadrature enclosure and rounding radius. The concavity bound of
Note 8 pays the entire remaining half-line at the actual slab endpoint.
The Gaussian compensation transforms and their full half-line Gaussian
moment Taylor bounds are unchanged. The K=2 positive-polynomial index
majorant was already proved uniformly on 0<=t<=1, so it covers every
omitted theta index on every new slab. No asymptotic error is substituted
for any of these enclosures.

The maximum returned source-jet radius is below 2.426*10^(-63); the
maximum separately paid retained integration tail is below
1.300*10^(-72). These descriptive decimals do not decide signs. The
record's outward dyadic endpoints do.

## 3. Sign decisions and moving branch windows

| Level | Stationarity excluded | Signed, unique in its cell | Signed cell requiring a merged window |
|---|---:|---:|---:|
| j=0 | 263 | 7 | 2 |
| j=1 | 255 | 15 | 2 |

Exclusions use either a genuine derivative interval separated from zero
or strict uniform endpoint signs together with strict spatial
monotonicity. On every signed cell, the exact aggregate D_j+X_j is
used, with all retained diagonal and cross terms evaluated and recorded.
Subtracting the complete genuine-stationary payment gives minimum exact
lower surpluses approximately

\[
5.447243714975249\,10^{-10},\qquad
1.4409891995267208\,10^{-11}.
\]

Exact rational comparisons to 5*10^(-10) and 10^(-11), not these rounded
displays, prove (1). There are no unresolved sign cells.

A branch can cross an integer cell boundary within a slab, so requiring
one branch inside every individual unit cell would give false unresolved
flags. The driver joins adjacent signed cells. A common strict sign of
the next derivative on every member cell, with opposite strict signs
at the two outer endpoints, proves a unique regular branch in each
merged window at every time. There are no unresolved branch windows.

There is one h_1=0 branch: its windows move from [31,32] through
[30,32] to [30,31]. There are two h_2=0 branches: the lower stays in
[9,10], while the upper moves from [34,35] through [33,35] to [33,34].
The record gives the exact time slabs. Uniqueness and ordering join
the windows across their shared closed time boundaries.

## 4. Direct physical norm payment

For each cell let I_0,I_1 be the full genuine H,H_x interval enclosures,
including every retained and omitted-source error. Define
v_k=dist(0,I_k), using their exact outward dyadic endpoints. Then,
without stationarity or a quotient,

\[
H^2+H_x^2\ge v_0^2+v_1^2.
\]

The minimum over all 272 cells is strictly positive. A directed integer
square-root calculation gives the rational lower bound

\[
q=\frac{321849425817089107558489508215301}
        {170141183460469231731687303715884105728}
>\frac{189}{100000000}.
\]

The record checks q^2 against the exact minimum energy lower bound.
The minimizing cell is [7/16,1/2] x [40,41]. Combining this direct
bound with |F|>1/120000 on 0<=t<=1, |x|<=8 proves (2), including
negative heights by evenness. This obtains a lower norm from paid
observations; it never assumes one to divide an error estimate.

## 5. Replay and review

With python-flint available, run from the numerics directory:

```sh
python3 certify_compensated_stationary_time_extension.py --output /tmp/inv21-full-time-replay.json
```

The [internal review](../reviews/6_FULL_TIME_STATIONARY_CERTIFICATE_INTERNAL_REVIEW_20261014.md)
independently reads the extension, replays the arithmetic, and audits
exact coverage, branch decisions, surplus targets, source hashes and the
norm-gap extraction. Its independently regenerated record agrees after
removing only elapsed runtime. The original exact shifted double and
triple collision controls remain in the new record. The
[guarded continuation note](10_FORWARD_STATIONARY_COLLARS_AND_BRANCH_CREATION_20261014.md)
adds a quartic branch-creation control.

The stable [manuscript](../manuscript/quaternion_theta_geometry.tex) now
includes Note 8's central fourth/sixth moment theorem, explicit two-jet
compensation and stationary payment, this full-time certificate, and
the guarded forward-continuation theorem. No manuscript snapshot was
created.

## 6. Next mathematical obligation

For the positive-threshold collision criterion, only |x|>41 remains
uncovered. One possible continuation uses the exact stationary branch
identity A'=-C, where A=h_j and C=h_(j+2): an initial strict sign
-AC>0 persists forward on every regular branch. Note 10 gives complete
moment payments, strict derivative-pair guards against branch creation,
and edge guards against branches entering a spatial interval.

An arbitrary-height construction must establish these gaps and cover
all possible collision predecessor neighborhoods. At large heights the
physical source observation is Schwartz while fixed-K truncation errors
are algebraic. Higher compensation, larger theta cutoffs, precision,
or subdivisions can reduce absolute error, but each step must certify
its signed or direct norm surplus against every error. Neither this
finite cover nor the conditional collar theorem supplies the missing
uniform all-height estimate.
