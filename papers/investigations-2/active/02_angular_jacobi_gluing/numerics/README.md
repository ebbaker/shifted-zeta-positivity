# Angular Jacobi gluing numerics

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Initialization model: `gpt-6.1-sol` (Codex); reasoning effort **ultra**.

The initialization prescribed the bounded task in the
[research program](../notes/INITIAL_RESEARCH_PROGRAM_20261013.md), requiring
complete-source error payments and a distinction between diagnostics and certificates.
Completed calculations are recorded below.
Keep reproducible code and small records here. Follow
[LARGE_FILES.md](../../../../../LARGE_FILES.md) for external generated data.

## Completed elliptic transport checks

13 October 2026. Prepared for Edward Baker with substantial LLM assistance;
recorded model `gpt-6-astra`, effort **ultra**.

The [standard-library checker](check_elliptic_transport.py) and
[retained record](ELLIPTIC_TRANSPORT_RECORD_20261013.json) verify 13 exact
angular-polynomial identities and a rational negative-origin bound for the
shifted auxiliary source. Eighteen truncated-theta checks and a changed
preparation control are floating diagnostics, not interval certificates.

Replay from the repository root without changing the saved record:

```sh
python3 papers/investigations-2/active/02_angular_jacobi_gluing/numerics/check_elliptic_transport.py --output /tmp/elliptic-transport.json
```

The [research derivation](../notes/ELLIPTIC_INSERTION_TRANSPORT_AND_HEAT_OBSTRUCTIONS_20261013.md)
proves the complete transport, convergence domain and analytic tail bounds.
That first calculation did not enclose a heat integral or physical stationary sign.

## Complete angular correction and transfer test

13 October 2026. Prepared for Edward Baker with substantial LLM assistance;
recorded model `gpt-6-astra` (Codex), effort **ultra**, inherited from the
recorded parent session. Internal checks are not independent validation.

The [complete-channel checker](check_complete_angular_channels.py) and
[small record](COMPLETE_ANGULAR_CHANNELS_RECORD_20261013.json) retain three
distinct kinds of evidence for the
[Volterra and positive-anchor derivation](../notes/2_VOLTERRA_RECOVERY_POSITIVE_ANCHOR_AND_TRANSFER_GAP_20261013.md):

- Exact rational checks for `R'+5R=-4*pi*exp(-4u)*Phi` and the elementary
  constants in the uniform correction lower bound
  `P_t(x)>1/[3000*(1+x²)]`, for every real `x` and `0<=t<=1`.
- Floating diagnostics of the Volterra representation and complete
  Fourier transport equation, including the heat derivative at `t=.05`.
  These finite-sum diagnostics have no certified tails.
- A complete outward heat-transform certificate at `t=0,x=32`, which gives
  `H<0`, `P>0`, and `|A|/P>1`, with `A=H-P`. This rejects the proposed global
  transfer through `|A|<=P`, including every stricter relative bound.

Replay from the repository root without changing the saved record:

```sh
python3 papers/investigations-2/active/02_angular_jacobi_gluing/numerics/check_complete_angular_channels.py \
  --record /tmp/complete-angular-channels.json
```

The script uses only the standard library, hash-checks the imported
60-digit outward Decimal implementation and records its own source hash.
It takes about three seconds with 512 Simpson panels. No binary floating
values enter the certificate's sign tests.

The paid enclosures, rounded here to wider intervals, are

```text
-9.608802e-5 < H_0(32) < -9.608627e-5,
 .00964664039 < P_0(32) < .00964664291,
 1.00996033 < |A_0(32)|/P_0(32) < 1.00996104.
```

For `delta=1/10`, the curvature expression

```text
2*pi²*((4*pi-1)²-16*pi)*exp(-pi*exp(4*delta))
```

is enclosed near `15.1944928127`. The analytic uniform bound uses the
simpler rational lower value `5`. The checker verifies the exact estimate
`exp(2/5)<97/65<3/2`, which, together with the stated elementary pi and
exponential inequalities, gives curvature greater than `146/27>5`.
The low- and high-frequency cosine estimates then give the global
constant `1/3000`. This anchor belongs to the correction `P`; it supplies
no positive lower bound on the physical observation `H=A+P`.

For the outward integration on `[0,1]`, the retained theta terms are
`n=1,2,3`. With `z=pi*n²*exp(4u)`, derivative polynomials for
`exp(u-z)Q(z)` obey

```text
Q_(k+1) = (1-4z) Q_k + 4z Q_k'.
```

The initial polynomials are `2z²-3z` for `Phi_n` and `1` for `R_n`,
with the latter multiplied by `2*pi²*n²`. Directed cell evaluation bounds
the fourth derivative of the full cosine integrand by the binomial
Leibniz sum. Every Simpson panel pays `h^5 sup|f''''|/2880`.

For omitted `n>=4`, the full absolute half-line integral is bounded by

```text
2*pi²*4^p*exp(-16*pi)
----------------------------------------------,
[1-(5/4)^p*exp(-9*pi)]*(64*pi-b)
```

using `(p,b)=(4,9)` for `Phi` and `(2,1)` for `R`. This follows from
`exp(4u)>=1+4u` and the consecutive theta-tail ratio. For `u>=U=1`,
the complete sources are bounded by `4*pi²*exp(bu-pi*exp(4u))`.
Concavity of the exponent bounds each remaining integral by

```text
4*pi²*exp(bU-pi*exp(4U))/(4*pi*exp(4U)-b).
```

All remainder bounds appear in the small record before the signs are
tested. This certificate is one frequency and one time, with no stationary
constraint asserted. It establishes neither the missing complete-channel
observation inequality nor a paired-kernel sign or RH conclusion.
