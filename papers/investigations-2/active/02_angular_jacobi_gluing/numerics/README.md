# Angular Jacobi gluing numerics

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6.1-sol` (Codex); reasoning effort **ultra**.

No calculations have been run for this initialization. Future computations
should implement the declared bounded task in the
[research program](../notes/INITIAL_RESEARCH_PROGRAM_20261013.md), preserve
complete-source error payments, and distinguish diagnostics from certificates.
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
No physical stationary sign or heat-integral enclosure is claimed here.
