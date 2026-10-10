# Theta spin screen

Run `python3 screen_theta_spins.py --enclose` to reproduce both the rigorous
42-digit midpoint enclosure and the exploratory finite-spin fit. The
standard-library program retains
[theta_spin_screen_record_20261010.json](theta_spin_screen_record_20261010.json).
The default uses 2,048 interval cells; `--cells` changes this only for the
outward enclosure. Without `--enclose`, the program reruns the exploratory
fit and preserves an enclosure only if its source hash matches.

The enclosure proves a moment mismatch for independent equal spins and
two equal ferromagnetic spins at time zero. The ten-spin fitted coupling,
amplitude, and sixth-moment comparison are floating-point experiments.
Neither part proves a Lee–Yang property of the theta measure, complex
convergence, or any genuine collision exclusion. All records are small.
