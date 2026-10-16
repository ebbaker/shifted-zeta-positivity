#!/usr/bin/env python3
"""Read-only exact-rational audit of retained microlocal atlas certificates.

This checks record identity and finite logical consequences of stored
outward enclosures. It does not rebuild the interval sums or reprove the
imported holomorphic approximation. Use the original replay sources for
fresh interval arithmetic. Only Python's standard library is required.
"""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

BUILD_RECORDS = (
    'CANDIDATE_CURRENT_ATLAS_BUILD_RECORD_20261010.json',
    'MULTI_CUTOFF_CANDIDATE_FAMILY_BUILD_RECORD_20261010.json',
)
CASES = (
    (22066, 'CANDIDATE_CURRENT_ATLAS_CERTIFICATE_20261010.json', 46, 29, 13, '0.03728'),
    (22067, 'MULTI_CUTOFF_M22067_CERTIFICATE_20261010.json', 29, 16, 12, '0.03117'),
    (22068, 'MULTI_CUTOFF_M22068_CERTIFICATE_20261010.json', 28, 14, 12, '0.02205'),
    (22080, 'MULTI_CUTOFF_M22080_CERTIFICATE_20261010.json', 32, 15, 13, '0.0032919'),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def interval(values):
    require(len(values) == 2, 'Interval must have exactly two endpoints.')
    lo, hi = map(Fraction, values)
    require(lo <= hi, 'Reversed interval endpoints.')
    return lo, hi


def distance(values):
    lo, hi = interval(values)
    return Fraction(0) if lo <= 0 <= hi else min(abs(lo), abs(hi))


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def audit(numerics_dir):
    cache = {}

    def read(name):
        require(Path(name).name == name, 'Expected a local numerics filename.')
        if name not in cache:
            cache[name] = (numerics_dir / name).read_bytes()
        return cache[name]

    hash_entries = 0
    record_summaries = []
    for name in BUILD_RECORDS:
        data = read(name)
        record = json.loads(data)
        require(record['status'] == 'PASS', f'Nonpassing build record: {name}')
        for filename, expected in record['files'].items():
            payload = read(filename)
            require(len(payload) == expected['bytes'], f'Size mismatch: {filename}')
            require(sha256(payload) == expected['sha256'], f'Hash mismatch: {filename}')
            hash_entries += 1
        record_summaries.append({
            'file': name, 'sha256': sha256(data),
            'verified_file_entries': len(record['files']),
        })

    results = []
    total_leaves = total_bands = 0
    for M, name, leaf_count, pruned_count, zero_count, claimed_floor in CASES:
        data = read(name)
        cert = json.loads(data)
        require(cert['status'] == 'PASS', f'Nonpassing certificate: {name}')
        require(cert['M'] == M and cert['N'] == M, f'Cutoff mismatch: {name}')
        source_name = ('check_candidate_current_atlas.py' if M == 22066
                       else 'check_multi_cutoff_candidate_family.py')
        require(cert['source_sha256'] == sha256(read(source_name)),
                f'Certificate/source mismatch: {name}')
        require(cert['rectangle']['exact_time_domain'] == [f'1/(2*log({M}))', '1/20'],
                f'Exact time-domain mismatch: {name}')
        require(cert['rectangle']['exact_height_domain'] == [f'4*pi*{M}^2', f'4*pi*{M}^2+8'],
                f'Exact height-domain mismatch: {name}')
        L_up = interval(cert['rectangle']['L'])[1]
        eta_up = interval(cert['full_holomorphic_payment']['eta'])[1]
        Leta_up = interval(cert['full_holomorphic_payment']['L_eta'])[1]
        require(L_up > 0 and eta_up > 0 and Leta_up > 0, 'Nonpositive payment.')
        cells = cert['closed_leaves']
        coverage = cert['coverage']
        require(len(cells) == leaf_count, f'Leaf count mismatch: {name}')
        require(coverage['number_of_closed_leaves'] == leaf_count, 'Coverage leaf count mismatch.')
        require(coverage['value_pruned_leaves'] == pruned_count, 'Coverage pruned count mismatch.')
        offsets = [interval(c['height_offset']) for c in cells]
        require(offsets[0][0] == 0 and offsets[-1][1] == 8, 'Missing height endpoint.')
        require(all(lo < hi for lo, hi in offsets), 'Empty height leaf.')
        require(all(a[1] == b[0] for a, b in zip(offsets, offsets[1:])), 'Height coverage gap.')
        require(sum((hi - lo for lo, hi in offsets), Fraction(0)) == 8, 'Incorrect total height width.')
        require(coverage['all_leaves_cover_entire_exact_closed_time_domain'], 'Missing full-time assertion.')
        require(coverage['exact_adjacency_and_total_width_checked'], 'Missing closed-coverage assertion.')
        require(coverage['joint_H_Hprime_nonvanishing'], 'Missing joint-nonvanishing assertion.')
        floors, survivors = [], []
        for cell, offset in zip(cells, offsets):
            a0 = distance(cell['complete_S']['real'])
            a1 = distance(cell['physical_Sprime']['real'])
            interval(cell['complete_S']['imaginary'])
            interval(cell['physical_Sprime']['imaginary'])
            current = interval(cell['complete_current'])
            tolerance = interval(cell['rectangular_current_tolerance'])
            require(Fraction(cell['paid_current_gap']) <= distance(current) - tolerance[1],
                    'Nonconservative current gap.')
            schur = (2*a0/eta_up)**2 + 2*a1/Leta_up
            require(Fraction(cell['correlated_candidate_lower']) <= schur,
                    'Nonconservative Schur lower bound.')
            stored_floor = Fraction(cell['normalized_joint_vector_lower'])
            if cell['kind'] == 'value_pruned':
                exact_floor = 2*a0 - eta_up
                require(Fraction(cell['value_candidate_gap']) > 0, 'Nonpositive value gap.')
            else:
                survivors.append((cell, offset))
                exact_floor = 2*a1/L_up - eta_up
                require(2*a1 > Leta_up, 'Derivative payment not exceeded.')
                require(Fraction(cell['derivative_candidate_gap']) > 0, 'Nonpositive derivative gap.')
                if M == 22066:
                    require(Fraction(cell['paid_current_gap']) > 0, 'Baseline current predicate failed.')
                else:
                    require(cell['first_jet_Schur_predicate_used'], 'Schur predicate missing.')
                    require(Fraction(cell['correlated_candidate_lower']) > 1, 'Schur predicate failed.')
            require(0 < stored_floor <= exact_floor, 'Nonpositive or nonconservative joint floor.')
            floors.append(stored_floor)
        require(len(cells) - len(survivors) == pruned_count, 'Actual pruned count mismatch.')
        minimum = min(floors)
        require(minimum == Fraction(coverage['minimum_normalized_joint_vector_lower']),
                'Coverage joint-floor mismatch.')
        require(minimum > Fraction(claimed_floor), 'Manuscript joint floor not proved.')
        groups = []
        for _, (lo, hi) in survivors:
            if groups and groups[-1][1] == lo:
                groups[-1] = (groups[-1][0], hi)
            else:
                groups.append((lo, hi))
        bands = coverage['zero_isolating_bands']
        require(len(groups) == len(bands) == zero_count, 'Zero-band count mismatch.')
        require(coverage['number_of_unique_simple_zeros_per_time'] == zero_count,
                'Coverage zero count mismatch.')
        for group, band in zip(groups, bands):
            require(interval(band['height_offset']) == group, 'Zero band does not match survivor union.')
            left = interval(band['Q_left_all_times'])
            right = interval(band['Q_right_all_times'])
            derivative = interval(band['Qprime_entire_band_all_times'])
            require((left[1] < 0 < right[0] and derivative[0] > 0)
                    or (right[1] < 0 < left[0] and derivative[1] < 0),
                    'Endpoint signs or derivative sign failed.')
            require(band['unique_simple_H_zero_per_time'], 'Missing simple-zero assertion.')
        current_passing = sum(Fraction(cell['paid_current_gap']) > 0 for cell, _ in survivors)
        require(current_passing == (17 if M == 22066 else 2), 'Paid-current pass count mismatch.')
        total_leaves += len(cells)
        total_bands += len(bands)
        results.append({
            'M': M, 'certificate': name, 'sha256': sha256(data),
            'closed_leaves': len(cells), 'value_pruned_leaves': pruned_count,
            'survivor_leaves': len(survivors), 'simple_zeros_per_time': len(bands),
            'minimum_stored_joint_floor': coverage['minimum_normalized_joint_vector_lower'],
            'survivors_passing_paid_current': current_passing,
        })
    return {
        'status': 'PASS',
        'scope': 'Read-only record-identity and exact-rational logical audit; no fresh interval sums or imported analytic proof.',
        'build_records': record_summaries,
        'verified_build_record_file_entries': hash_entries,
        'total_closed_leaves_audited': total_leaves,
        'total_zero_bands_audited': total_bands,
        'checks': [
            'Build-record sizes and SHA-256 hashes match.',
            'Exact domains, adjacent closed leaves, and full height width match.',
            'Every stored joint floor is positive and conservative; derivative denominator is L_up.',
            'Every stored Schur lower bound is conservative; retained acceptance predicates pass.',
            'Every zero band equals a connected survivor union and has strict all-time endpoint/derivative signs.',
        ],
        'certificates': results,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--numerics-dir', type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    try:
        summary = audit(args.numerics_dir)
    except (KeyError, OSError, ValueError, TypeError, ZeroDivisionError) as error:
        print(json.dumps({'status': 'FAIL', 'error': str(error)}, indent=2))
        raise SystemExit(1)
    print(json.dumps(summary, indent=2))
