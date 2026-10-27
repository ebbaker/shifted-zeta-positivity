# High-order endpoint probes and the uniform count gate

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**. HCB chat0001, thread `01a17aca-de9a-7533-9bb8-8ee0e9bdb282`.

**Status: conditional analytical transfer, proved in-note under RH and
reviewed by a separate same-model agent; no specialist validation.**
The actual uniform endpoint inequalities and counts are **not acquired**.
The new result shows that a high-order positive measurement on the fixed
safe strips can resolve a shrinking endpoint band, pay an endpoint floor
above the current source error, and isolate an arbitrary complete integer
count. It replaces Note06's restrictive fixed first-order budget with an
explicit source-stable detector; it does not prove that the canonical
sequence passes that detector. No new source values, numerical experiment
or certificate replay were executed in this return.

Read the [result index][results], [heat-flow cluster][cluster],
[collision controls][controls] and [avoid index][avoid]. Under
[target classification][a01], this is a quantified acquisition interface,
not evidence for the unproved arithmetic inequality or a simplicity
criterion. Preserve [scoped conclusions][a07] and [count/precision
qualifications][a04]. [Review05][review] and the [chat handoff][handoff]
record the proof checks and exact remaining input. The classical RH
argument/count inputs are those already checked in [Note04][n04] and
its [primary-source catalog][refs]; no new primary reference is imported.

## 1. Unchanged family and theorem

Retain [Note03][n03]'s entire family, including integer m≥16,
\[
 X=4\pi e^m,\quad L=m,\quad \tau_X=X^{-1/4},\quad
 \Gamma=\partial([-4,4]+i[-2,2]),\quad
 \mathcal B=[-6,6]+i[-3,3],
\]
\[
 h_X(\tau,u)=H(\tau/L^2,X+u/L)/A_X,\qquad
 A_X=\pi^{1/4}X^{7/4}e^{-\pi X/8}/16.
\]
Use exactly the completed holomorphic model f_X and its declared complete
buffer allowance e_src=C_0B_XX^{-3/4}, with fixed positive C_0 and
1≤B_X=O(1). Its finite constants/onset are still uninstantiated.
Write F(u)=h_X(0,u), D=F'/F. Under RH its microscopic zeros r are real,
with multiplicity; all sums below include the whole infinite population.

Put
\[
 q=\lfloor\sqrt L\rfloor,\qquad
 \beta_q(c)=\sum_r\left(\frac4{(c-r)^2+4}\right)^q,
 \qquad c=\pm4.                                      \tag{1}
\]
The **unproved arithmetic gate** in this note is
\[
 \beta_q(-4)\le L^{-3},\qquad\beta_q(4)\le L^{-3}.      \tag{2}
\]
All conclusions below involving (2) are conditional on these actual
canonical inequalities for the member(s) in question. They are not
consequences of RH supplied here.

For all sufficiently large m satisfying (2), the following implications
hold, with uniform asymptotic constants:

1. Every initial zero is at distance at least
   \(d=2\sqrt{L^{3/q}-1}\sim2\sqrt{3\log L}\,L^{-1/4}\)
   from each real endpoint; no separation between internal zeros is needed.
2. Throughout 0≤τ≤τ_X, both endpoint moduli, and the complete canonical
   contour modulus, are at least \(X^{-5/8-o(1)}\). The model has the
   same floor after subtracting e_src. This beats that allowance with
   relative loss at most \(X^{-1/8+o(1)}\).
3. A normalized high-order Poisson functional C_q has
   \(|n_m-C_q|=O(L^{-2}/\sqrt{\log L})\). Replacing F by f_X costs
   at most \(\kappa_q4^q\nu/\sqrt3=X^{-1/4+o(1)}\), where
   \(\nu=X^{-1/4+o(1)}\) is the safe-strip logarithm bound below.
   An additional actual enclosure of Re C_{q,f} with radius at most 1/8
   therefore isolates the exact integer n_m for all sufficiently large m.
   No fixed value of n_m is implied.

These are asymptotic implications, **not a certificate for all m≥16**.
In particular d is larger than 1 at some small members, so the small-d
proof below is used only after d≤1. The m=16 witness remains exactly
[Note06][n06]'s separate finite result.

## 2. Safe-strip source payment for the detector

The proof of Note04 applies uniformly on the closed strips
\[
 S_\pm=\{u:|\Re u|\le5,\ 1\le\pm\Im u\le3\},
\]
with canonical initial floor m_strip≤inf_{S_+∪S_-}|F| and
m_strip≥X^{-1/2-o(1)}. On each strip the quotient F/f_X
has its small analytic logarithm
\[
 \ell=-\operatorname{Log}(f_X/F),\qquad
 |\ell|\le\nu=-\log(1-e_{\rm src}/m_{\rm strip})
       \le X^{-1/4+o(1)}.                           \tag{3}
\]
Here and below the model is evaluated at τ=0. The logarithms are chosen
by the near-one quotient, separately on the two strips. No analytic log
is continued across the real axis.

For |λ−4|≤1 let w=√λ with Re w>0. Then Re w≥√3 and
\[
 |w-2|\le\rho=2-\sqrt3.
\]
Every x±iw, −4≤x≤4, remains in the safe strips. Cauchy on its remaining
radius 1−ρ bounds |ell'|≤ν/(1−ρ). Define
\[
 G_c(\lambda)=\frac{D(c-iw)-D(c+iw)}{2iw}
       =\sum_r\frac1{(c-r)^2+\lambda}.               \tag{4}
\]
The complete order-one real-zero product justifies the convergent
resolvent difference. Its real linear exponential term cancels.
Define G_{c,f} from f_X in the same way. On the λ-circle,
\[
 |G_c-G_{c,f}|\le\frac{\nu}{\sqrt3(1-\rho)}<\nu.
\]
Cauchy's formula in λ gives, without assuming a high-order source jet,
\[
 \beta_q(c)=\frac{4^q(-1)^{q-1}}{(q-1)!}
                 G_c^{(q-1)}(4),\qquad
 |\beta_q(c)-\beta_{q,f}(c)|\le4^q\nu
                     \le X^{-1/4+o(1)}.            \tag{5}
\]
Thus the amplification remains affordable because q=o(L). For example,
a valid model enclosure whose upper real endpoint, plus 4^qν, is ≤L^{-3}
would certify (2). Neither these model enclosures nor their uniform
inequalities have been supplied. Finite evaluations must separately
instantiate (3), pay arithmetic enclosure error and fix a bounded protocol.

Each summand in (1) is nonnegative. Under (2) each is ≤L^{-3}, so
\[
 |c-r|^2\ge4(L^{3/q}-1)=d^2.                         \tag{6}
\]
A zero at either endpoint contributes at least one and fails (2), even
when it has even multiplicity. The detector does not cap the interior
population at one, two or three.

## 3. Endpoint modulus and the whole time interval

First extend the **initial** kernel calculation of Note04 to a small
microscopic height b>0. Its zeta offset is a=b/(2L), and its exact kernel
variation is 2log(2/a)=2log(4L/b). For b=d in (6),
\[
 \log(4L/d)=(5/4+o(1))\log L.
\]
The already named RH argument bound, with leading constant 1/4, gives
\[
 |F(c+id)|\ge X^{-5/8-o(1)},\qquad c=\pm4.           \tag{7}
\]
The identity, anchor/gamma error, kernel mass and boundary payments in
Note04 were uniform for 0<a≤1; this step does not substitute into an
estimate stated only for a fixed positive physical offset. The completion
factor divided by A_X stays bounded above and below here.

We must pay the move from c+id to the real endpoint. The real-zero product
has the exact modulus identity
\[
 \log\frac{|F(c+id)|}{|F(c)|}
       =\frac12\sum_r\log\left(1+\frac{d^2}{(c-r)^2}\right). \tag{8}
\]
The real linear exponential has equal modulus at these two points; it
has not been discarded from the field. To bound (8), put x=X+c/L and
h=1/log L in physical z coordinates. The Riemann–von Mangoldt formula
and the same RH |S| bound show
\[
 \#\{\rho:|\rho-x|\le h\}=O(hL+L/\log L)=O(L/\log L).
\]
The microscopic gap (6) bounds every near-root summand by log 2. For the
remaining roots, first use the physical unit-interval count O(L) in
h<|rho−x|≤1, then sum farther unit annuli with counts
O(log(X+j+3)). This gives
\[
 \sum_{|\rho-x|>h}(c-r)^{-2}=O(\log^2 L/L).
\]
Consequently (8) is O(L/log L)+O(d²log²L/L)=o(L). Combining with (7),
\[
 |F(\pm4)|\ge X^{-5/8-o(1)}.                         \tag{9}
\]
Only a boundary gap was used; repeated or unresolved interior roots are
allowed.

Note06's generic jet estimates at gap d≤1 give
\[
 |A_c|\ll L(1+d^{-1}),\qquad Q_c\ll Ld^{-2}+L^{-1}.
\]
In particular τ_X(A_c²+Q_c)=o(1). Its global Gaussian endpoint lemma,
including its complete tail, now gives
\[
 \inf_{0\le\tau\le\tau_X}|h_X(\tau,\pm4)|
        \ge (1-o(1))|F(\pm4)|\ge X^{-5/8-o(1)}.      \tag{10}
\]
No new shrinking-height heat-tail assertion is needed: (7) is initial,
and heat transport is applied at the real endpoints through their jets.
By Note04's vertical-minimum identity and its unchanged horizontal floor,
\[
 \inf_{\tau,u\in\Gamma}|h_X(\tau,u)|\ge X^{-5/8-o(1)}. \tag{11}
\]
This uses the direct horizontal floor, not the weaker E/4^n bound at a
growing count. Source subtraction transfers (10)–(11) to f_X and
Rouché gives its same complete zero count inside Γ for sufficiently large
m satisfying (2); this does not assert that the model zeros are real. The canonical count is constant throughout the interval: under RH
all roots remain real and (10) prevents crossings at the only real wall
points. No tracking of individual internal roots is required.

## 4. Exact integer extraction without a fixed population cap

For q≥2 set
\[
 \kappa_q=\frac{\Gamma(q)}{\sqrt\pi\Gamma(q-1/2)}
       =O(\sqrt q),\quad\kappa_q\le2\sqrt q,
 \qquad k_q(s)=\frac{\kappa_q2^{2q-1}}{(s^2+4)^q}.
\]
Then ∫_R k_q=1. Define
\[
 C_q=\sum_r\int_{-4}^4 k_q(x-r)\,dx,\quad
 V(\lambda)=\frac1{2\pi i\sqrt\lambda}
       \int_{-4}^4[D(x-i\sqrt\lambda)-D(x+i\sqrt\lambda)]\,dx.
\]
Convergence of the positive kernel sums permits interchange, and
\[
 C_q=\frac{\kappa_q\pi2^{2q-1}(-1)^{q-1}}{(q-1)!}
                         V^{(q-1)}(4).             \tag{12}
\]
The x integrals always run from −4 to 4; a counterclockwise upper contour
edge has the opposite orientation. This is a smoothed complete zero count,
not the Poisson **second moment** used by consumer P.

For T_q(s)=∫_s^∞ k_q(v)dv, s>0, substituting v=2t gives
\[
 T_q(s)\le\frac{\kappa_q}{2(q-1)(s/2)}
                       (1+(s/2)^2)^{1-q}.
\]
Write P_2(c)=Σ_r 2/((c−r)²+4) and δ=d/2. Since
P_2(s)=1/[2(1+(s/2)²)], the ratio T_q(s)/P_2(s) is bounded, for
s≥d, by
\[
 B_q(d)=\frac{\kappa_q}{(q-1)\delta}(1+\delta^2)^{2-q}.
\]
Each root's indicator error is bounded by its two endpoint tails;
this includes all exterior roots and all multiplicities. Hence
\[
 |n_m-C_q|\le B_q(d)[P_2(-4)+P_2(4)]
             =O(L^{-2}/\sqrt{\log L}).              \tag{13}
\]
For the final equality, use the unconditional generic bound P_2(−4)+P_2(4)
=O(L) from Note04's safe-strip log derivative, together with
1+δ²=L^{3/q}, q~√L. In particular this argument has not assumed n≤3.

Let V_f and C_{q,f} denote the same holomorphic functionals of f_X.
Integrals of D−D_f=ell' become endpoint differences, leaving four
logarithm values on the λ-circle. Therefore
\[
 |V-V_f|\le\frac{2\nu}{\pi\sqrt3},\qquad
 |C_q-C_{q,f}|\le\frac{\kappa_q4^q\nu}{\sqrt3}
                          \le X^{-1/4+o(1)}.       \tag{14}
\]
This correlated logarithm payment is essential; independently bounding
high derivatives by unspecified constants would not justify (14).
If an actual finite enclosure for Re C_{q,f} has radius ε_eval≤1/8,
then (13), (14) and ε_eval eventually total less than 1/4. The enlarged
interval contains exactly one integer, the complete n_m. It can vary
with m, and remains the canonical/model count for the whole time interval
by (10)–(11). **No such functional enclosure or resulting new integer was
computed in this return.** A stable formula does not establish its
computational cost or its unknown arithmetic value.

## 5. First unpaid input, limitations and controls

The progress is the explicit detector's resolution and source amplification,
the conditional exponent 5/8, and the leakage/source payments for integer
extraction with variable n. It is not a uniform acquisition. At the actual
frozen heights the present cited RH estimates do not establish (2),
nonvanishing of Z(T±2/L), or an exact sequence of counts. They do not show
that the task is impossible or logically independent of RH either.

The next exact arithmetic input can be supplied as model bounds
\[
 \operatorname{upper}\Re\beta_{q,f}(\pm4)
       +4^q\nu\le L^{-3},                           \tag{15}
\]
plus a paid enclosure for Re C_{q,f}. The first term in (15), its uniform
margin, effective onsets/constants and evaluation cost remain unpaid.
This is a stronger input than qualitative nonvanishing and could fail for
some members. If it fails, preserve the failure and reconsider the route;
do not infer a canonical boundary zero or an unfavorable second moment.
The floor in (11) by itself still does not meet Note03's n=2 baseline
o(X^{-5/16}) relative Poisson demand: this route only guarantees
X^{-1/8+o(1)}. The specified n≥6 binomial fallback exclusion is unchanged.
No coefficient precision, favorable P integral, J lower bound, finite-core
coverage, RH/simplicity theorem or Newman-bound improvement follows.

Admissible real-root polynomial/double/Hermite controls satisfy the generic
resolvent and heat arguments. A boundary zero fails (2), while an internal
multiple zero is counted with its multiplicity and is not excluded. The
complete theta arithmetic, RH product and named zeta count estimates are
additional canonical premises: Euler-factor controls with nonreal zeros
can fail realness; weighted-square/finite-tail controls have no all-real
time; reflected/positive-primitive, finite-prime/profile and theta-close
controls fail the unchanged complete theta arithmetic premises as specified
in [cluster12][controls]. Where a control is all-real and meets the actual
quantitative hypotheses, these acquisition estimates apply and do not
exclude its internal collision. No control certificate was rerun.

HCB-02 remains **Partial**. The [sole register][progress] retains the
m=16 finite result and the open uniform gate. No new source campaign or
research automation is running. Any further source evaluation needs its
cases, source versions, encodings, tolerances, comparator and stop rules
fixed before execution. See [Note08][handoff] for the complete handoff.

[n03]: 03_MICROSCOPIC_WALL_PAYMENT_AND_POISSON_BUDGET_20261026.md
[n04]: 04_HORIZONTAL_WALL_ACQUISITION_AND_ENDPOINT_COUNT_20261026.md
[n06]: 06_REAL_ENDPOINT_TRANSPORT_AND_FINITE_COUNT_20261026.md
[review]: ../reviews/05_UNIFORM_PROBE_AND_COUNT_INTERNAL_REVIEW_20261026.md
[handoff]: 08_CHAT0001_RESULTS_AND_HANDOFF_20261026.md
[refs]: ../references/01_MICROSCOPIC_WALL_PRIMARY_SOURCES_20261026.md
[progress]: ../research-progress/01_COLLISION_BOUNDS_RESEARCH_PROGRESS_20261026.md
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a04]: ../../../../avoid/04_counts_and_precision_as_evidence.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
