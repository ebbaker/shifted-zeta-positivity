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

These are exact finite polynomial controls. No genuine-theta rectangle has
been evaluated. See the [program](../notes/INITIAL_RESEARCH_PROGRAM_20261013.md)
for the analytic argument and proposed benchmark. Keep large regenerable
artifacts outside Git under [LARGE_FILES.md](../../../../../LARGE_FILES.md).
