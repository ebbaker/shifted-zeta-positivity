# Spacetime collision degree checks

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6-astra` (Codex); reasoning effort **ultra**, verified from the
recorded session. Parallel internal assessments used the same configuration;
they are not independent specialist or formal validation.

Run `python3 check_collision_degree.py` in this directory. The standard-library
checker prints a deterministic JSON record. The retained
[record](COLLISION_DEGREE_SEED_RECORD_20261013.json) contains rationally
certified boundary windings for heat polynomials of multiplicity 2 through
10, reversed orientations, a collision-free control and a nonheat control
with cancelling indices. Every curved edge is connected to its polygon
inside a certified open half-plane.

The [genuine-theta pilot](check_genuine_theta_boundary_pilot.py) now adds a
fully paid 60-digit outward certificate on `[0,0.05] × [8,12]`. Run
`python3 check_genuine_theta_boundary_pilot.py --record /tmp/genuine-theta-boundary-pilot.json`.
Its [retained record](GENUINE_THETA_BOUNDARY_PILOT_RECORD_20261013.json)
certifies zero winding with four complete boundary pair integrals; the same
evaluator excludes joint zeros with one interior pair integral. All theta
and integration tails are included. No performance advantage is established.

See the [initial program](../notes/INITIAL_RESEARCH_PROGRAM_20261013.md)
for the degree argument and the
[pilot note](../notes/1_GENUINE_THETA_BOUNDARY_PILOT_20261013.md) for payments
and the stop decision. Keep large regenerable artifacts outside Git under
[LARGE_FILES.md](../../../../../LARGE_FILES.md).
