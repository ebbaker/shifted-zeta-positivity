"""Exact finite A/B comparison for B04, 13 November 2026.

Prepared for Edward Baker with substantial OpenAI Codex LLM assistance.
Subagent dispatch gpt-6.1-sol / ultra. Backend configuration unavailable.
"""

import json
from fractions import Fraction as Q


BASE = (Q(1, 6), Q(2, 3))
LEFT, RIGHT = Q(1, 8), Q(1, 2)
WIDTH = Q(567, 1000)
CAP = Q(669, 20000)


def process(letter, pair):
    k, ell = pair
    if letter == "A":
        divisor = 2 * k + 2
        return k / divisor, (k + ell + 1) / divisor
    return ell - Q(1, 2), k + Q(1, 2)


def g(pair, v):
    k, ell = pair
    return k / v + ell - k - 1 + v / 4


def finite_envelope(pairs):
    """Intersect each line's lower half-spaces to recover its active interval."""
    rows = []
    for pair, word in pairs.items():
        k, ell = pair
        left, right = LEFT, RIGHT
        for other_k, other_ell in pairs:
            slope_difference = (ell - k) - (other_ell - other_k)
            intercept_difference = other_k - k
            if slope_difference > 0:
                right = min(right, intercept_difference / slope_difference)
            elif slope_difference < 0:
                left = max(left, intercept_difference / slope_difference)
            elif intercept_difference < 0:
                left = RIGHT
            if left >= right:
                break
        if left < right:
            rows.append((left, right, pair, word))
    rows.sort()
    assert rows[0][0] == LEFT and rows[-1][1] == RIGHT
    assert all(first[1] == second[0] for first, second in zip(rows, rows[1:]))
    return max((g(pair, v), v, word) for left, right, pair, word in rows
               for v in (left, right)), len(rows)


def main():
    pairs = {BASE: ""}
    frontier = pairs.copy()
    stages = []
    for depth in range(1, 9):
        next_frontier = {}
        for pair, word in frontier.items():
            for letter in "AB":
                candidate = process(letter, pair)
                if candidate not in pairs:
                    next_frontier.setdefault(candidate, letter + word)
        pairs.update(next_frontier)
        frontier = next_frontier
        if depth >= 5:
            (peak, location, word), pieces = finite_envelope(pairs)
            stages.append({
                "max_word_length": depth, "distinct_pairs": len(pairs),
                "active_intervals": pieces, "peak": str(peak),
                "peak_at": str(location), "peak_word": word,
                "width_allowance": str(Q(1, 2) + 2 * peak),
            })

    assert peak == Q(406319, 12161760) and location == Q(1040, 5847)
    assert Q(1, 2) + 2 * CAP < WIDTH < Q(2927, 5152)
    cuts = [LEFT, Q(4, 25), Q(89, 500), Q(11, 50), Q(9, 20), RIGHT]
    words = ["AAAAA", "AAAAABAA", "AAAABABA", "AAABAABA", ""]
    partition = []
    for left, right, word in zip(cuts, cuts[1:], words):
        pair = BASE
        for letter in reversed(word):
            pair = process(letter, pair)
        assert pair in pairs
        left_value, right_value = g(pair, left), g(pair, right)
        assert max(left_value, right_value) <= CAP
        partition.append({
            "word": word or "identity", "pair": list(map(str, pair)),
            "left": str(left), "right": str(right),
            "g_at_left": str(left_value), "g_at_right": str(right_value),
        })

    drift = Q(1, 100000)
    power = Q(1, 200000)
    delta = (WIDTH - Q(1, 2)) / 2
    assert (delta - CAP) / 8 - drift / 16 > power
    assert delta - drift / 4 > Q(1, 32)
    assert delta - Q(1, 32) - 7 * drift / 32 > Q(1, 512)
    assert Q(1, 6) - WIDTH / 2 < -Q(1, 32)
    assert Q(1, 6) - WIDTH / 4 - (1 - drift) / 16 < -Q(1, 32)
    assert -1 - WIDTH / 2 + Q(17, 32) < -Q(1, 2)

    print(json.dumps({
        "finite_search": stages,
        "fixed_partition": partition, "cap": str(CAP),
        "target_width": str(WIDTH), "target_power": str(power),
        "clock_tolerance": str(drift),
    }, indent=2))


if __name__ == "__main__":
    main()
