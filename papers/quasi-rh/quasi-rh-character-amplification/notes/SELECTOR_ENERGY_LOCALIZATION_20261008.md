# Selector energy and the small wedge still needed by the application

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

Status: selector-preserving consequences of explicitly stated source
inputs, and a sharper sufficient domain for the still-unproved mixed
estimate. No new arithmetic cancellation or zero-free boundary is proved.
The source's detector, moments, buffered estimates, and seven-eighths
theorem remain imported assumptions. This supplements
[the selector gate](SELECTOR_FEASIBILITY_20261008.md) and
[the fixed-slot mixed subcases](SELECTOR_PRESERVING_SUBCASES_20261008.md).

The useful application refinement is quite narrow: after the already
calculated rebalances, a new mixed estimate is needed only in a triangle
with both coordinate widths at most `1/900` for each fixed `(delta,x)`.
The old marginal estimates handle the rest of the witness region. This
localizes the required arithmetic theorem; it does not prove it inside
that triangle and does not change the stated full-rectangle mixed target.

## 1. Two count-sensitive estimates that preserve the selector

Work at fixed separating parameters on any subset of `C_+`, with the
actual inverse, plain and physical prime polynomials and their original
masks. Write `H=1+T_1`, `eta=1/5000`, and `K=1+delta*m-eta`.
Besides the manuscript's hypotheses, state the following inputs
explicitly:

    #C <= U^(R+epsilon) H^A,
    |M_r(u)|^2 <= U^(delta*r+epsilon) H^A,
    |S_m(u)|^2 <= U^(delta*m+epsilon) H^A,
    |Q_L(u)|^2 <= U^(Gamma_L+epsilon) H^A.

Here `L` is a displayed set of physical slots and `Gamma_L` is an
additive upper amplitude exponent for their actual tests, obtained by
summing chosen per-slot exponents. In particular
`Gamma_I=Gamma_J+Gamma_(I\J)`. The inverse pointwise input is source
Lemma 8.2. For the original physical ray-class prime sums, with their
fixed exclusions and smooth annuli, Lemma 19.1 permits the universal
envelope `Gamma_L = delta*z_L`, up to the small bin losses. Finite-ray
coefficients on arbitrary prime subsets do not by themselves suffice:
for such lists the displayed pointwise bounds are additional hypotheses.
They are not inferred from the arbitrary bounded coefficients allowed in
the manuscript's elementary reduction. A smaller measured profile
exponent may be used at fixed tests, but need not survive differentiation
of those tests.

Direct counting gives the first exact sufficient estimate

    E_(C_+) := sum_(u in C_+) |M_r S_m Q_I|^2
             << U^(R+delta*(r+m)+Gamma_I+epsilon) H^A.       (1)

There is also a useful combination with a plain fourth moment. Suppose
`J` is a subset of `I` for which the original, masked source moment is
valid:

    sum_(u in C_+) |S_m(u)|^4 |Q_J(u)|^2
                       << U^(1+epsilon) H^A.

The empty `J` is permitted. A positive-length `J` must use the source's
original prime-sum support class as well as its finite-ray coefficient
condition, slot mesh, primitive-character exclusion and length condition,
as detailed in the fixed-slot note. For more general lists the displayed
fourth moment is itself an additional hypothesis.
Bounding `M_r` and `Q_(I\J)` pointwise and applying Cauchy gives

    E_(C_+) <= sup |M_r Q_(I\J)|^2
              (sum |S_m|^4|Q_J|^2)^(1/2)
              (sum |Q_J|^2)^(1/2)
      << U^((1+R)/2+delta*r+Gamma_I-Gamma_J/2+epsilon) H^A.  (2)

All sums before the final positive enlargements retain `C_+`. No
coefficient, row selector, or coprimality mask has been inserted into a
complete-family Poisson formula.

For comparison with the target `K=1+delta*m-eta`, put

    s_count = 1-R-delta*r-Gamma_I,
    s_pair  = (2*delta*m+Gamma_J-delta*r-Gamma_I)/2.

Equation (1) saves `s_count` over `1+delta*m`; (2) saves
`s_pair+s_count/2`. The fixed-slot argument independently saves
`s_pair`. Thus the available sufficient saving is at least

    max(0, s_count, s_pair, s_pair+s_count/2).               (3)

These are positive-norm estimates for actual polynomials. They do not
claim a saving when the displayed exponents fail to provide one.

## 2. Use the actual full-bin count, not its coarse envelope

Write `x=q/delta`, `alpha=5/6`, `a=alpha-delta`, and

    D_x=3-17*x/9, B_x=2-8*x/9, P_x=B_x*(1-x),
    J=a*D_x+delta*P_x,
    R*=1-delta+a*delta*P_x/(2J).

The manuscript justifies this count for the full fixed bin before the
current witness lengths are selected. It is therefore available in (1)
without imposing the simultaneous-witness lower bound on every row.
Define

    h(delta,x)=(1-R*)/delta
             =1-a*p/[2(a+delta*p)],  p=P_x/D_x.

On the hard box, `p` decreases with `x`; indeed

    p'(x)=-4*(34*x^2-108*x+99)/(81*D_x^2)<0.

Also `h` increases with `delta` and decreases with `p`. Consequently
`h` increases with both `delta` and `x`, and its exact minimum is

    h(9/25,49/100)=3646037/4283333.

Under the universal physical envelope `Gamma_I<=delta*z` and
`z<=(1-r)/2`, equation (1) saves at least

    delta*[h(delta,x)-(1+r)/2].                            (4)

This proves a genuine additional rectangular subcase: for every

    7/10 <= r <= 701/1000,  9/25 <= m <= 1/2,

and the full stated `(delta,x)` box, the saving in (4) is at least

    55121103/214166650000 = 0.0002573748200... .

Hence `E_(C_+) << U^(K-c+epsilon)H^A` there, with

    c=12287773/214166650000 = 0.0000573748200... >0.          (5)

This conclusion is conditional on the stated pointwise physical-profile
inputs; it is uniform for derivative families only when their universal
envelopes have been established. It requires no new signed cancellation.
The coarser count `9/8-23*delta/20` would miss this uniform strip. The
exact curved condition (4), or a smaller actual `Gamma_I`, can remove
more points than (5). The application wedge below lies to the right of
this particular uniform strip.

## 3. Exact localization after the two existing rebalances

This section concerns which mixed input is sufficient for the proposed
application. It is not a claim that the full moment outside this domain
has been estimated by the old row counts.

Keep `eta=1/5000` and the established conditional rebalance quantities

    t0=1+delta*P_x/(2J),
    t_new=t0-B_x*eta/J,
    r_new=(B_x*t_new-5*x/9)/D_x-eta/(delta*D_x),
    m_new=t_new-r_new,
    F=a*B_x/J,
    R_new=R*-F*eta.

Within the original short-witness rectangle, the old scalar count
exponents for a selected inverse or plain witness are respectively

    A_I(r)=1-delta*[x+(1-x)*r],
    P_plain(m)=1-delta*[4*x/9+B_x*m].

The rebalance identities give exactly

    A_I(r_new)=R_new+eta,
    P_plain(m_new)=R_new.                                 (6)

Since their slopes are negative, old estimates already reach `R_new`
whenever

    r >= r_new+w,  w=eta/[delta*(1-x)],
    or m >= m_new.                                       (7)

The detector support gives `r+m>=t_new`, at leading exponent before
the adjustable annular losses. If `r<=r_new`, this forces `m>=m_new`.
It follows that the only surviving leading-exponent region is

    a_r=r-r_new,  b_m=m_new-m,
    0 < a_r < w,  0 < b_m <= a_r.                         (8)

Thus the request for a new estimate can be confined to this triangle
for each `(delta,x)`. The prime lists used for the two old marginal
bounds may be selected separately by the already justified whole-slot
procedure. No independence of the witnesses or prime events is assumed.
The other original witness-length ranges retain their earlier marginal
coverage; no new extension of either scalar line beyond its legal range
is used here.

There is an exact tapered sufficient saving within the triangle:

    s(r)=eta-delta*(1-x)*(r-r_new)>0,
    E_C << U^(1+delta*m-s(r)+epsilon)H^A.                 (9)

Dividing (9) by the detector's actual simultaneous-witness and selected
prime lower bounds yields `A_I(r)-s(r)=R_new` at leading exponent.
A uniform `eta` saving on the triangle is a stronger sufficient request.
Neither version of (9) has been proved here.

The mixed estimate is on the full fixed bin, before selecting the large
witness subset, just as in the manuscript. The taper describes the
required exponent; it does not authorize unrelated row-dependent
coefficients. For a chosen actual prime product with squared amplitude
lower exponent `2G_I`, the exact count budget instead asks for saving

    s_actual=1-R_new-delta*r-2G_I,

plus the reserved witness losses. The scalar formula (9) uses
`2G_I>=2q*(1-r)/2` in the capacity limit. A total capacity and whole-slot
length loss `rho` raises the sufficient saving by at most `2q*rho`, in
addition to the separately reserved amplitude-bin losses.

## 4. Continuous bounds and the buffered operational domain

The exact width obeys

    1/1071 <= w <= 1/900.                                (10)

The positions can also be bounded continuously, without a floating grid.
Useful simplified identities are

    r_new=1-F/2-(1-F)*w,
    m_new=1/2-(a/J)*[(1-x)/2-eta/delta].                  (11)

The manuscript gives `F_delta<0` and `F_x>0`. Moreover `0<F<1`,
`w_delta<0`, `w_x>0`, and `w<1/2`. Differentiating the first identity
shows that `r_new` increases with `delta` and decreases with `x`.

For the second, put `T=(1-x)/2-eta/delta`. Its derivatives are

    (m_new)_delta = alpha*P_x*T/J^2 - a*eta/(delta^2*J),
    (m_new)_x = a*[J/2+T*J_x]/J^2,
    J/2+T*J_x = [5a-4delta*(1-x)^2]/9-(eta/delta)*J_x.

The last expression is positive since `J_x<0` and the first bracket
is positive throughout the box. For the delta derivative, expand the
`eta` term in `T` before taking bounds:

    delta^2*J^2*(m_new)_delta
       =alpha*P_x*delta^2*(1-x)/2-eta*(alpha*P_x*delta+a*J).

Its positive term is at least
`alpha*(7/9)*(9/25)^2/4=21/1000`, while its subtracted term is at most
`eta*[alpha*(21/50)+(71/150)*(3/2)]=53/250000`.
Here `P_x>=7/9`, `P_x<=1`, and `J<3/2` throughout the box.
Therefore `m_new` increases with both `delta` and `x`.

The corner extrema are consequently rigorous:

    47749/67660 <= r_new <= 10261670/14086891,
       0.705719775...        0.728455270...,

    3470383/8566666 <= m_new <= 28646/69475,
       0.405103105...          0.412320978... .            (12)

The ideal wedge is thus contained in
`0.7057<r<0.7296`, `0.4039<m<0.4124`, strictly inside the originally
requested length box. It is disjoint from the proved `m>=0.42` subcase.
That subcase alone therefore does not settle the application wedge.

For actual annuli, use an outer buffer. Suppose a single nonnegative
budget `ell` dominates each marginal count-exponent loss and the
detector support loss, so that the old exponents are `A_I+ell` and
`P_plain+ell`, and `r+m>=t_new-ell`. Then rows not already counted at
exponent `R_new` lie in

    a_r < (eta+ell)/[delta*(1-x)],
    b_m > -ell/(delta*B_x),
    b_m <= a_r+ell.                                      (13)

In particular `a_r>-(39/14)*ell`, its upper endpoint is at most
`w+(50/9)*ell`, and the lower `b_m` endpoint is at least
`-(25/14)*ell`. These bounds follow from the positive slope lower
bounds `delta*(1-x)>=9/50` and `delta*B_x>=14/25`.
Apply the mixed theorem with its actual capacity/profile losses in this
outer wedge, not with a zero-loss sharp cutoff. All such fixed losses
must be chosen inside the already reserved conditional payoff surplus.

The resulting research target is an estimate uniform over this buffered
triangle, the full `(delta,x)` rectangle, and the original profile and
height families. The new arithmetic saving remains open even there.
Exact rational checks are in `numerics/check_selector_energy.py`.
