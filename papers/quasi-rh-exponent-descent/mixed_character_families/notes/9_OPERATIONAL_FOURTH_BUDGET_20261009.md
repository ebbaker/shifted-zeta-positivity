# Operational whole-slot budgets for the inverse-weighted fourth route

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model derivation and audit are internal validation, not independent
specialist review or formal proof verification.

**Result.** The favorable fourth-saving deficit in the organized manuscript
is not a uniform budget for the operational wedge. This note gives the exact
fixed-bin whole-slot optimization, a closed continuous map of the relaxed
fourth deficit, and a uniform sufficient target under stated slot assumptions.
With the universal envelopes, total selected inverse-slot shortfall
`t_I=ell/2`, and a legal fourth-subset shortfall at most `1/1000`, the required
extra fourth saving is less than `1/540` throughout the operational wedge.
The stronger common target with saving `1/540` still permits the inverse-ratio
cutoff `N f_inv <= U^(1/2)` with reserve greater than `1/500`.

This is exponent bookkeeping and finite subset optimization. It proves no
new asymptotic fourth moment, actual detector/slot realization, mixed energy,
or zero-free boundary. The remaining signed fourth correlation is still
unproved. All existing conditional source inputs remain necessary.

## 1. What counts as an admissible original slot

Use the original physical polynomials, selected full bin, high-conductor
selector, native orientations and zeros of the
[organized manuscript](../mixed_character_reductions.tex). The local source
transfer records specify whole physical prime sums with smooth full annuli,
fixed ray-class restrictions/exclusions and fixed finite-ray coefficient
expansions. Their lists and coefficients are row independent; supports are
pairwise disjoint. Each positive slot satisfies the source fourth-moment
mesh, fixed before the slot count and before the target-dependent height
orders. Arbitrarily deleting primes from a physical annulus is not an
admissible way to create a smaller slot. See the parent
[selector-preserving note](../../../quasi-rh-character-amplification/notes/SELECTOR_PRESERVING_SUBCASES_20261008.md)
and [structural audit](../../../quasi-rh-character-amplification/reviews/MOMENT_STRUCTURAL_AUDIT_20261008.md),
which record the transfer from source Lemma 18.1 and Sections 19.1–19.2.
The external primary source is the
[30 September companion paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).
Its deep moment and detector proofs are not independently replayed here.

The local records allow a sufficiently fine *fixed* physical subdivision
to be chosen before the relevant target. They do not provide a concrete
vector of original slot IDs, widths, profiles, ray coefficients and actual
witness gains for the current buffered bins. No such operational vector
was recovered in the manuscript or mixed Notes 7–8. A formal list in the
checker illustrates the arithmetic; it is not a reconstruction of detector
data. An existing physical slot must not be split during an application to
meet the numerical budget below.

For an original fixed list record, at minimum, each slot's identifier,
physical width `z_i`, additive proved pointwise envelope `Gamma_i`, and
unsquared witness lower gain `G_i`; record the full profile/support/ray
provenance and the source mesh certificate separately. These are different
numbers. In the universal envelope `Gamma_i=d z_i`; an amplitude lower gain
does not automatically improve that upper envelope.

An admissibility certificate has two stages:

1. Choose whole slots `I` satisfying
   `r+2 z_I <= 1-c_1`, `2r+8 z_I <= 3-c_2`, with fixed positive margins,
   and all original shape, exclusion, mesh, derivative and height conditions.
   On the common witness require the actual product lower gain
   `G_I=sum_{i in I}G_i`, with its allocated losses.
2. Choose whole slots `J subset I` satisfying
   `2m+(9/2)z_J <= 1-c_4`, with fixed `c_4>0` and the same source legality.
   This certifies the selected plain fourth input for this exact subset.

Arithmetic inequalities do not certify that these source/profile conditions
or the simultaneous witness hold. Empty `J` is allowed, using the source's
zero-slot assertion; it need not have a favorable fourth deficit.

## 2. Exact finite subset optimization and fixed-bin thresholds

Fix an already admissible `I`. Put

\[
 R=R_*+\ell,\quad g=dr+\Gamma_I,\quad
 \mu=(1-R-g)_+,\quad
 D_J=2dm+\Gamma_J-g,\quad
 \chi_J=(2s-\mu-D_J)_+.
\]

The manuscript's sufficient direct target is

\[
 F_J=\sum_{u\in\mathcal C^+}|M_u|^2|S_u|^4|Q_J(u)|^2
       \ll U^{1+dr-\chi_J+\varepsilon}H^b. \tag{1}
\]

Since `g,mu,s` are fixed after `I` is chosen, minimizing `chi_J` is the
finite knapsack problem

\[
 \Gamma_*(c)=\max_{J\subset I,\;z_J\le c}\sum_{j\in J}\Gamma_j,
 \qquad c=c_m-\nu_4,\quad c_m=\frac{2(1-2m)}9,
 \quad \nu_4>0. \tag{2}
\]

The decrement gives `c_4=(9/2)nu_4`. If `c<0`, a positive-length marked
subset is unavailable; the empty fourth input must be treated separately.
For arbitrary additive envelopes, maximizing the total selected width or
taking a prefix need not optimize (2). The checker implements an exact
rational Pareto dynamic program on the original IDs: after each whole
slot is considered, discard a state only if another state has no greater
width and no smaller envelope. Such domination persists after addition
of any future subset, proving the pruning rule. A finite brute-force
comparison on nonuniform synthetic envelopes checks the optimizer and its
strict-capacity boundary behavior. The algorithm can have exponentially
many states for unrestricted rational lists; no polynomial complexity is
claimed. Repeated equal-width mesh systems have few reachable states.

If `I` itself is not fixed, enumerate admissible `(I,J)` with `J subset I`
using the three assignments absent, inverse-only, and inverse-and-fourth.
Apply the actual witness-gain inequality before comparing fourth deficits.
This is a finite optimization specification, not a license to choose a new
row-dependent subset. One may keep a Pareto frontier in capacity, gain and
envelope, but domination must respect all inverse capacities and gain
requirements, rather than only the fourth capacity.

For a universal envelope let

\[
 t_I=\frac{1-r}{2}-z_I\ge0,\quad
 h_J=c_m-z_J\ge0,\quad
 g_{\rm cap}=\frac{d(1+r)}2,
\]
\[
 D_{\rm cap}=2dm+dc_m-g_{\rm cap}+dt_I,
 \quad H_{\rm cap}=2s-\mu-D_{\rm cap}.
\]

Here `D_cap` uses the *actual* total inverse-slot deficit `t_I`; only `J`
is relaxed to the continuous fourth capacity. Exactly,

\[
 D_J=D_{\rm cap}-dh_J,\qquad
 \boxed{\chi_J=(H_{\rm cap}+dh_J)_+.} \tag{3}
\]

It is not always `chi_cap+dh_J`: the positive-part kink matters when the
continuous fourth branch already has spare saving. With a new saving
`kappa>=0`, the exact fourth-budget test is

\[
 h_J\le\frac{\kappa-H_{\rm cap}}d. \tag{4}
\]

The right side must be nonnegative for any subset to qualify. Existing
scalar inputs already give the mixed energy when `mu>=s`, or when
`H_cap+dh_J<=0`; these bins do not need a new fourth estimate. A positive
fourth deficit is a deficit of this sufficient criterion, not a lower
bound for the true energy.

The small inverse-ratio sector from Note 7 costs `U^(1+upsilon/2)`. Its
reserve is

\[
 \gamma_J=dr-\chi_J-\upsilon/2. \tag{5}
\]

For `upsilon=1/2` and `dr>1/4`, the exact shortfall threshold is

\[
 \boxed{h_J<r-\frac1{4d}-\frac{H_{\rm cap}}d.} \tag{6}
\]

Equality spends all the reserve. A positive fixed reserve must remain
larger than the actual preliminary losses. For another ratio cutoff use
(5) directly; this does not change the original inverse annulus `U^r`.

Under the universal envelope and `z_I>=c_m-nu_4`, greedy selection of
whole slots gives `h_J<=nu_4+h_mesh`, where `h_mesh=max_{i in I}z_i`.
Stop before the next slot crosses `c_m-nu_4`; a crossing slot costs at
most `h_mesh`. If all slots fit, the supply assumption gives the same
bound. This is a conditional property of the actual original list. In
the setting below, `z_I>c_m` throughout the wedge, so a source certificate
`nu_4+h_mesh<=1/1000` is enough. Optimizing (2) may improve this bound.

## 3. Closed map on the operational wedge

Use the manuscript's exact `eta=1/5000`, `ell=10^-6`, and set
`t_I=ell/2`. Write `u=a_r`, `v=b_m`, and use the closed operational region

\[
 \frac9{25}\le d\le\frac{21}{50},\quad
 \frac{49}{100}\le x\le\frac12,\quad
 -\frac{39\ell}{14}\le u\le u_H:=\frac{\eta+\ell}{d(1-x)},
 \quad v_L:=-\frac{\ell}{dB_x}\le v\le u+\ell. \tag{7}
\]

Only feasible `(u,v)` are included; the actual manuscript has the stated
strict boundaries. Put `r=r_new+u`, `m=m_new-v`,
`s=eta-d(1-x)u+ell`, and

\[
 a=\frac56-d,\quad B_x=2-\frac89x,\quad
 D_x=3-\frac{17}{9}x,\quad P_x=B_x(1-x),\quad J_x=aD_x+dP_x.
\]

All relaxed formulas refer to the original annular scales and profiles.
Define

\[
 Q(d,x)=\frac a{J_x}\left(d-\frac{2\eta}{1-x}\right),\quad
 L(d,x)=\frac{5(1-2x)}{18}Q(d,x),\quad
 c=\frac{14\ell}{9}-t_I=\frac{19\ell}{18}.
\]

For each fixed `(d,x)`, the exact minimum and supremum of the relaxed
fourth deficit over (7) are

\[
 C_{\min}(d,x)=
 \left(L(d,x)-\frac{5\ell(1-2x)}{9B_x(1-x)}-dt_I\right)_+,
 \tag{8}
\]
\[
 \boxed{C_{\max}(d,x)=L(d,x)
       +\frac{28\eta+37\ell}{18(1-x)}+dc.} \tag{9}
\]

The extrema occur at `(u_H,v_L)` and `(u_H,u_H+ell)`, respectively,
in the closure. The maximum has `s=0` and is a limiting operational
boundary; it is not a claim that an actual bin attains it.

To prove the map, before taking the positive part consider
`H_cap=2s-mu-D_cap`. Its derivative in `v` is `14d/9>0`.
At fixed `v`, its derivative in `u` is `d(2x-3/2)` when `mu=0`,
and `d(2x-1)` when `mu>0`; both are nonpositive. Thus the lower edge
has minimum at `u_H`. Along the upper edge `v=u+ell`, these derivatives
become `d(2x+1/18)` and `d(2x+5/9)`, both positive; its maximum is
at `u_H`. At this endpoint,

\[
 \mu_0=\frac{aB_x}{4J_x}
       \left(d(2x-1)-\frac{2\eta}{1-x}\right)
       -\ell\left(1+\frac1{2(1-x)}\right)+dt_I<0. \tag{10}
\]

Consequently `mu=0`. Substitution gives (8)–(9), including their
positive-part convention. Feasibility holds at both endpoint edges.

The continuous signs in (9) can be checked with small rational envelopes.
In particular

\[
 Q_d=\frac{a^2D_x-d^2P_x+(5/6)P_x[2\eta/(1-x)]}{J_x^2}>0. \tag{11}
\]

The checker gives the positive numerator lower bound
`13316689/63281250` after omitting the last positive term. Hence
`partial_d C_max >=19/18000000>0`. An explicit one-box envelope for
`partial_x C_max` is less than `-0.05987189489`; it bounds the negative
`-2(d-2eta/(1-x))/J_x` term below in magnitude and the positive
`-(1-2x)(d-2eta/(1-x))J'_x/J_x^2` term above, using the lower bound on
`a` for the negative term and the upper bound on `a` for the positive
term. The remaining derivative
term from `eta/(1-x)` is negative and may be discarded for this upper
bound. These are inequalities on the entire box, not sampled signs.
Therefore the global relaxed supremum is exactly

\[
 \boxed{C_{\max}(21/50,49/100)
   =\frac{43774520332379}{30789918900000000}
   =0.0014217159997904\ldots.} \tag{12}
\]

The global relaxed minimum is zero; the `x=1/2` side contains an open
region with `H_cap<0`. At `x=49/100` the fixed-bin minima are already
about `0.0007441` for `d=9/25` and `0.0008070` for `d=21/50`.

For comparison, the central offsets `u=1/20000`, `v=1/40000` give:

| `d` | `x` | relaxed `chi` | `mu` |
| --- | --- | --- | --- |
| .36 | .49 | .0009546709376 | 0 |
| .36 | .50 | .0001341688206 | .0000726511794 |
| .39 | .49 | .0009895913370 | 0 |
| .39 | .50 | .0001313305621 | .0000758911046 |
| .42 | .49 | .0010183452808 | 0 |
| .42 | .50 | .0001282332326 | .0000793901008 |

These exact rational evaluations illustrate that the central-slice
`d` behavior changes with `x`; they are not the continuous certificate.
The proved worst-case envelope (9) increases in `d` and decreases in `x`.

## 4. Uniform inverse-ratio reserve and a common sufficient theorem

For relaxed `J`, the exact infimum of the variable-deficit half-cap
reserve over the operational wedge is the minimum of

\[
 G(d,x)=d-\frac14
 -\frac{a(23-18x)}{18J_x}\left(d-\frac{2\eta}{1-x}\right)
 -\frac{28\eta+19\ell}{18(1-x)}-dc. \tag{13}
\]

This formula is the reserve at the upper operational corner used in (9).
To justify that it is the fixed-bin minimum, write the reserve as
`min(dr-1/4,dr-H_cap-1/4)`. The second expression decreases as `v`
increases. Along `v=u+ell`, its derivatives in `u` are
`d(17/18-2x)` on `mu=0`, and `d(4/9-2x)` on `mu>0`; both are negative.
Thus its minimum is at `u_H`. Feasibility requires
`u>=v_L-ell>=-39ell/14`, because `dB_x>=14/25`. For the first expression
the exact fixed-bin minimum is `d r_new-1/4-ell/B_x-d ell`. Subtracting
(13) from that minimum gives

\[
 L(d,x)+\frac{10\eta+19\ell}{18(1-x)}
       +\frac{d\ell}{18}-\frac{\ell}{B_x}>0.
\]

The positive middle term already dominates `ell/B_x` on the box. This
proves that (13) is the exact infimum for each fixed `(d,x)`, rather
than only a global lower bound.

For the continuous signs, let `K=23-18x`. Then

\[
 A=-18J_x-KJ'_x
   =-\frac{475}{54}+d\left(41-\frac{368}9x+16x^2\right)
   \ge\frac{59}{1350}>0,
\]
\[
 G_x=-\frac{aA}{18J_x^2}\left(d-\frac{2\eta}{1-x}\right)
 +\frac{2\eta aK/J_x-(28\eta+19\ell)}{18(1-x)^2}<0. \tag{14}
\]

The second numerator is negative because `aK/J_x<=K/D_x`, and a
coarse rational box bound is `-105807/37000000`. Also, from
`0<Q_d<a/J_x<=1/D_x`,

\[
 G_d>1-c-\frac{K}{18D_x}
       \ge\frac{410759297}{666000000}>\frac12. \tag{15}
\]

Thus the exact relaxed uniform infimum is

\[
 \boxed{G(9/25,1/2)=\frac{1945769219}{507450000000}
       =0.0038344057917036\ldots.} \tag{16}
\]

With an actual legal whole-slot shortfall `h_J<=1/1000`, (3) implies

\[
 \chi_J\le C_{\max}(21/50,49/100)+\frac{21}{50000}
      =0.0018417159997904\ldots<\frac1{540}, \tag{17}
\]
\[
 \gamma_J\ge G(9/25,1/2)-\frac{21}{50000}
      =\frac{1732640219}{507450000000}
      >\frac{17}{5000}. \tag{18}
\]

The inequality (18) uses the bin's actual variable `chi_J`. For the
*stronger common* fourth target with saving `1/540`, independently
certify `dr-1/540-1/4>1/500`: the gain parameter
`F_x=aB_x/J_x` decreases in `d` and increases in `x`, since

\[
 (F_x)_d=-\frac{(5/6)B_x^2(1-x)}{J_x^2}<0,\qquad
 (F_x)_x=\frac{a[(10/9)a+dB_x^2]}{J_x^2}>0.
\]

With `F_hi=F(9/25,1/2)`, `F_lo=F(21/50,49/100)`, every permitted `r`
obeys

\[
 r\ge r_L:=1-\frac{F_{\rm hi}}2
 -\frac{(1-F_{\rm lo})\eta}{(9/25)(1-1/2)}
 -\frac{39\ell}{14}
 =\frac{67258421363926019}{95311904506000000}
 =0.7056665346529931\ldots.
\]

This also gives `dr-1/4>G(9/25,1/2)`, as used above. Finally,

\[
 \boxed{dr-\frac1{540}-\frac14
 \ge\frac9{25}r_L-\frac1{540}-\frac14
 =\frac{140772625414022617}{64335535541550000000}
 =0.0021881006232257\ldots>\frac1{500}.} \tag{19}
\]

**Conditional sufficient theorem.** Suppose the actual original slot
arrangement on every required operational bin has the stated source
legality, `t_I=ell/2`, `h_J<=1/1000`, and actual witness/loss budgets.
If one proves, uniformly in all permitted profiles and heights,

\[
 \boxed{F_J\ll U^{1+dr-1/540+\varepsilon}H^b,} \tag{20}
\]

then the manuscript's weighted Cauchy criterion gives the desired mixed
energy. Equivalently it is enough to prove the corresponding one-sided
large-inverse-ratio remainder bound after removing `N f_inv<=U^(1/2)`;
the removed sector has reserve greater than `1/500` against (20).
The uniform conclusion also holds for `t_I>=ell/2`, provided `h_J<=1/1000`
and the actual witness budget below is still met using this same `s`.
At fixed `r,m,s,h_J`, increasing `t_I` makes `g` decrease with slope `-d`,
`D_cap` increase with slope `d`, and `mu` nondecrease. Thus the derivative
of `H_cap` is `-d` when `mu=0`, or `-2d` when `mu>0`; the required
`chi_J` cannot increase. The common-target reserve (19) is independent
of `t_I`. This allows an interval of total whole-slot rounding loss;
it does not permit ignoring the accompanying reduction in prime gain.
Equations (8)–(16) remain the exact base map for `t_I=ell/2`.

This is a uniform, somewhat stronger alternative to adapting `chi_J`
bin by bin. The theorem (20) is **unproved**. The budget comparison does
not establish an implication between the fourth and cubic targets or a
comparison of their inherent analytic difficulty.

## 5. The total inverse-slot and detector budget is tighter

Making `I` smaller improves several upper-bound terms but reduces the
prime lower gain. That tradeoff must be included before claiming a count
payoff. In the ideal flat profile `q=dx`, with
`G_I=dx z_I`, let `s_0=eta-d(1-x)a_r`. The exact count identity gives

\[
 1-R_{\rm new}-dr-2G_I=s_0+2dx t_I. \tag{21}
\]

More generally, if `Delta_G=dx z_I-G_I>=0` is the actual lower-gain
shortfall from that comparison and `Lambda` is the combined allocated
witness/profile/count loss, the available saving `s=s_0+ell` requires

\[
 \boxed{2dx t_I+2\Delta_G+\Lambda\le\ell.} \tag{22}
\]

If the actual profile gives more gain, use the exact `G_I` inequality;
do not impose `Delta_G>=0` artificially. The first strict inverse capacity
requires `2t_I>=c_1`; compatibility in the flat case therefore requires
`dx c_1+2Delta_G+Lambda<=ell`. For the choice here `c_1=ell`,
`t_I=ell/2`, the flat capacity cost is `dx ell`, leaving

\[
 2\Delta_G+\Lambda\le\ell(1-dx)
      \ge\frac{79}{100}\ell. \tag{23}
\]

This is a remaining conditional budget, not evidence that the detector
losses fit it. With no other losses, (22) bounds `t_I` by
`ell/(2dx)`, only a few parts in a million; this requirement is much
tighter than the fourth-subset `1/1000` shortfall allowance. The two
mesh/capacity choices must not be conflated. The source permits choosing
fixed finer meshes in principle, but an existing list still needs the
actual certificate. The second inverse margin at this choice is
`2r-1+4ell>0`, so it is not the tight numerical capacity on this wedge.

As a formal check at the manuscript's favorable rational point, 512 equal
*synthetic* slots of width `z_I/512`, upper envelope `d z_i`, and lower gain
`dx z_i` have first inverse margin `ell` and positive second margin.
With fourth decrement `10^-7`, the exact whole subset chooses 145 slots,
has `h_J=0.00022909510164...`, and requires
`chi_J=0.00021664305716...`. Its remaining witness loss budget is
`41/50000000=0.00000082`. This verifies that the rational constraints are
jointly consistent for an abstract finite vector. It supplies no actual
prime windows, profiles, selected-row population or witness realization.

## 6. Reproduction, scope, and the next mathematical obligation

The standalone standard-library checker
[check_mixed_operational_budget.py](../../numerics/check_mixed_operational_budget.py)
prints the deterministic small
[record](../../numerics/mixed_operational_budget_record_20261009.json).
Run it from the investigation directory with
`python3 numerics/check_mixed_operational_budget.py`; redirect stdout to
the record path to regenerate the JSON. Its `--slots` option accepts a
JSON object with `capacity`, `capacity_decrement`, and `slots`, each
containing an ordinary string `id` and rational-string `length`, `envelope`,
and optional `gain`.
For example `"length":"1/10000"` uses exact arithmetic. A
`source_provenance` object is echoed but not verified by the script.

The checker uses exact `Fraction` operations and rational continuous
envelopes for every sign needed in the proof. Its finite tests compare
the nonuniform optimizer with a distinct exhaustive enumeration, check a
strict capacity boundary, and test one fully labeled formal vector. The
six slice evaluations are illustrative only. No random sampling, floating
optimization, ideal-family moment experiment or detector data are used.
Decimals are displays of exact rational results. Both source and record
remain small, following the repository large-files policy.

The next proof task is the signed inverse-ratio estimate retaining the
actual annular Möbius coefficients, selector, selected fourth weight and
all canceled-phase zero masks, as in Note 7 and the new ratio-core note.
The continuous certificate narrows the necessary quantitative request;
it does not supply cancellation. A completed arithmetic theorem must
then be coupled to an actual slot/witness certificate satisfying (22),
the profile/height uniformity, and finite operational-bin recombination.
