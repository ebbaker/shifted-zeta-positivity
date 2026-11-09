#!/usr/bin/env python3
"""Exact E13 census/tree inspection and B10 r3 constants; no source/kernel calls.

9 November 2026. Prepared for Edward Baker with substantial OpenAI Codex
assistance, OC chat0011, recorded thread gpt-6-astra/max. Per-turn backend
configuration unavailable. This imports the E13 winding certificate; it
does not re-evaluate its outward source balls or parse displays as proofs.
"""
import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RETURN = ROOT / 'research-progress/handoffs/27_TND_OC_E13_R1_RETURN_20261109.json'
EXECUTION = ROOT / 'numerics/18_TND_OC_E13_R1_EXECUTION_20261109.json'
RETURN_SHA = 'bc1d7983c472fe4f3b4d556fe0dd69d466bf6a88598c04056ddfe0dcd3c3011f'
N = 388
U, V = F(5, 32768), F(15, 131072)


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def coordinates(strings):
    require(len(strings) == 4 and all(isinstance(s, str) for s in strings), 'coordinate schema')
    box = tuple(F(s) for s in strings)
    require(all(q.denominator & (q.denominator - 1) == 0 for q in box), 'non-dyadic coordinate')
    require(box[0] < box[1] and box[2] < box[3], 'empty or reversed cell')
    return box


def geometry(cells):
    require(len(cells) == N, 'census size')
    require(len({c['cell'] for c in cells}) == N, 'duplicate cell')
    require(all(type(c['count']) is int and c['count'] == 1 for c in cells), 'singleton count')
    boxes = sorted((coordinates(c['box']), c['cell']) for c in cells)
    for (a, b, c, d), _ in boxes:
        require(F(988) <= a < b <= F(2012) and -F(3, 2) <= c < d <= F(3, 2), 'outer containment')
        require(b - a <= U and d - c <= V, 'coordinate width')
        require((b - a)**2 + (d - c)**2 <= F(1, 2**24), 'diameter')
    gaps = [(boxes[i+1][0][0] - boxes[i][0][1], boxes[i][1], boxes[i+1][1])
            for i in range(N - 1)]
    require(min(gaps)[0] > F(1, 2), 'horizontal separation')
    return {
        'labels': N, 'occupied_cells': N,
        'x_width_max': str(max(b[1] - b[0] for b, _ in boxes)),
        'y_width_max': str(max(b[3] - b[2] for b, _ in boxes)),
        'min_horizontal_gap': str(min(gaps)[0]),
        'min_gap_cell_ids': list(min(gaps)[1:]),
        'max_diameter_squared': str(max((b[1]-b[0])**2 + (b[3]-b[2])**2 for b, _ in boxes)),
        'ordered_pairs': N*(N-1), 'unordered_pairs': N*(N-1)//2,
    }


def tree_check(trace, returned, execution):
    require(digest(trace) == execution['contour_log']['stored_sha256'], 'trace stored hash')
    require(trace.stat().st_size == execution['contour_log']['bytes'], 'trace size')
    nodes, counts, splits, leaves = {}, {}, {}, {}
    events = Counter()
    outer, complete = [], []
    canonical = hashlib.sha256()
    with trace.open('rb') as stream:
        for line in stream:
            require(line.endswith(b'\n'), 'truncated trace')
            r = json.loads(line)
            canonical.update((json.dumps(r, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n').encode())
            event = r.get('event', r.get('kind', 'unspecified'))
            events[event] += 1
            if event == 'cell_attempt':
                require(r['id'] not in nodes, 'duplicate node')
                nodes[r['id']] = r
            elif event == 'cell_winding':
                require(r['id'] not in counts and type(r['count']) is int and r['count'] >= 0, 'winding count schema')
                counts[r['id']] = r['count']
            elif event == 'candidate_cut_accepted':
                require(r['cell'] not in splits, 'duplicate accepted split')
                splits[r['cell']] = r
            elif event == 'occupied_leaf':
                require(r['cell'] not in leaves, 'duplicate leaf')
                leaves[r['cell']] = r
            elif event == 'outer_count':
                outer.append(r['count'])
            elif event == 'leaf_completeness':
                complete.append((r['count'], r['leaves']))
    require(canonical.hexdigest() == execution['contour_log']['canonical_content_sha256'], 'trace canonical hash')
    require(dict(events) == execution['contour_log']['event_counts'], 'event counts')
    require(outer == [N] and complete == [(N, N)], 'completeness events')
    require(coordinates(nodes[1]['box']) == (F(988), F(2012), -F(3, 2), F(3, 2)), 'outer rectangle')
    require(nodes[1]['parent'] is None and counts[1] == N, 'root identity')
    visited, occupied = set(), {}

    def walk(ident):
        require(ident not in visited, 'tree cycle or repeated child')
        visited.add(ident)
        node = nodes[ident]
        box = coordinates(node['box'])
        count = counts[ident]
        if ident in splits:
            split = splits[ident]
            require(count > 0 and len(split['children']) == 2, 'split count')
            axis = 0 if box[1]-box[0] >= box[3]-box[2] else 1
            fraction = F(split['fraction'])
            require(fraction in (F(1,2), F(3,8), F(5,8)), 'cut fraction')
            cut = box[2*axis] + fraction*(box[2*axis+1]-box[2*axis])
            left, right = list(box), list(box)
            left[2*axis+1], right[2*axis] = cut, cut
            for child, expected in zip(split['children'], (tuple(left), tuple(right))):
                require(nodes[child]['parent'] == ident and nodes[child]['depth'] == node['depth']+1, 'child lineage')
                require(coordinates(nodes[child]['box']) == expected, 'exact child partition')
                walk(child)
            require(sum(counts[c] for c in split['children']) == count, 'child count sum')
        elif count:
            require(ident in leaves and leaves[ident]['count'] == count, 'occupied leaf count')
            require(F(leaves[ident]['diameter_squared']) == (box[1]-box[0])**2+(box[3]-box[2])**2, 'leaf diameter record')
            occupied[ident] = (box, count)

    walk(1)
    expected = {c['cell']: (coordinates(c['box']), c['count'])
                for c in returned['certified_cell_census']['cells']}
    require(occupied == expected and set(leaves) == set(expected), 'trace-to-return census')
    return {'status': 'passed_structure_only_inherits_E13_outward_windings',
            'stored_sha256': digest(trace), 'canonical_content_sha256': canonical.hexdigest(),
            'bytes': trace.stat().st_size, 'accepted_tree_nodes': len(visited),
            'accepted_splits': len(splits), 'event_counts': dict(events)}


def rejection_checks(cells):
    variants = {}
    q = deepcopy(cells); q.pop(); variants['missing_cell'] = q
    q = deepcopy(cells); q[1]['cell'] = q[0]['cell']; variants['duplicate_id'] = q
    q = deepcopy(cells); q[0]['count'] = 2; variants['changed_multiplicity'] = q
    q = deepcopy(cells); q[1]['box'] = q[0]['box'][:]; variants['overlapping_cells'] = q
    q = deepcopy(cells); q[0]['box'][1] = str(F(q[0]['box'][0]) + 2*U); variants['enlarged_width'] = q
    q = deepcopy(cells); q[0]['box'][0] = str(F(q[0]['box'][0]) + F(1,3)); variants['non_dyadic'] = q
    for name, q in variants.items():
        try:
            geometry(q)
        except ValueError:
            continue
        raise ValueError('injected input accepted: '+name)
    return list(variants)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trace', type=Path, required=True, help='Exact external E13 trace; must match both recorded hashes')
    args = parser.parse_args()
    require(digest(RETURN) == RETURN_SHA, 'frozen return hash')
    returned = json.loads(RETURN.read_text())
    require(digest(EXECUTION) == returned['execution_record_sha256'], 'execution hash')
    execution = json.loads(EXECUTION.read_text())
    for name, expected in execution['code_sha256'].items():
        require(digest(ROOT/'numerics'/name) == expected, 'E13 code hash: '+name)
    require(returned['certified_cell_census']['source_log_sha256'] == execution['contour_log']['stored_sha256'], 'census trace link')
    cells = returned['certified_cell_census']['cells']
    g = geometry(cells)
    geometric_radius = F(4*N, 1000)*(10*U+4*V)
    total = geometric_radius + F(1,1000) + F(1,2**32)
    require(geometric_radius == F(1261,409600), 'radius arithmetic')
    require(total < F(41,10000) < F(1,200), 'total radius target')
    output = {
        'date_local': '2026-11-09', 'timezone': 'America/New_York',
        'prepared_for': 'Edward Baker', 'llm_assistance': 'substantial OpenAI Codex',
        'recorded_thread_model': 'gpt-6-astra', 'recorded_thread_effort': 'max',
        'per_turn_backend_configuration': None, 'task': 'TND-OC-B10 r3',
        'status': 'exact_geometry_and_bookkeeping_passed_not_a_projection_evaluation',
        'arithmetic': 'Python fractions.Fraction and integer/hash/JSON checks',
        'return_sha256': digest(RETURN), 'execution_sha256': digest(EXECUTION),
        'geometry': g, 'trace_check': tree_check(args.trace, returned, execution),
        'geometry_rejection_checks': rejection_checks(cells),
        'geometric_radius_upper': str(geometric_radius),
        'arithmetic_endpoint_radii_sum_gate': '1/1000', 'omitted_tail': '1/4294967296',
        'total_radius_upper': str(total), 'strictly_below': '41/10000',
        'canonical_source_calls': 0, 'kernel_function_calls': 0,
        'elementary_exp_erf_calls_per_pass': 4*N+6*(N*(N-1)//2),
        'pass_count_max': 3,
        'scope': 'Imported E13 census, exact geometry, accepted count tree and analytical constants; no fresh source-ball verification, kernel value, or analytic proof certificate.'
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
