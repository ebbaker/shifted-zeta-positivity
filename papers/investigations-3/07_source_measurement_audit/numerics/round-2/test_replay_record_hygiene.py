"""Focused identity/provenance and Linux/macOS resource-unit checks."""
import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'round-1'))
from replay_record_hygiene import mathematical_content_digest, peak_rss_bytes


class HygieneTests(unittest.TestCase):
    def setUp(self):
        self.record = {
            'schema': 'fixture_v1', 'precision_bits': 448,
            'cases': [{'h': ['[0.1 +/- 1e-90]', '[-0.2 +/- 2e-90]'],
                       'wall_seconds': 0.1}],
            'elapsed_seconds': 1.0, 'python_version': '3.10.0',
            'evaluation_sha256': 'a' * 64, 'checker_sha256': 'b' * 64,
            'record_content_sha256': {'certificate': 'c' * 64},
        }

    def test_runtime_and_dependent_byte_provenance_do_not_change_identity(self):
        changed = copy.deepcopy(self.record)
        changed.update(elapsed_seconds=8.0, python_version='3.13.16',
                       evaluation_sha256='d' * 64, checker_sha256='e' * 64)
        changed['cases'][0]['wall_seconds'] = 9.0
        self.assertEqual(mathematical_content_digest(self.record),
                         mathematical_content_digest(changed))

    def test_serialization_and_key_order_do_not_change_identity(self):
        reordered = dict(reversed(list(self.record.items())))
        reformatted = json.loads(json.dumps(reordered, indent=4))
        self.assertEqual(mathematical_content_digest(self.record),
                         mathematical_content_digest(reformatted))

    def test_enclosure_precision_and_math_reference_mutations_change_identity(self):
        mutations = [
            lambda r: r['cases'][0]['h'].__setitem__(0, '[0.2 +/- 1e-90]'),
            lambda r: r.__setitem__('precision_bits', 512),
            lambda r: r['record_content_sha256'].__setitem__('certificate', 'f' * 64),
        ]
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                changed = copy.deepcopy(self.record)
                mutate(changed)
                self.assertNotEqual(mathematical_content_digest(self.record),
                                    mathematical_content_digest(changed))

    def test_summary_self_hash_is_excluded(self):
        changed = copy.deepcopy(self.record)
        changed['mathematical_content_sha256'] = 'f' * 64
        self.assertEqual(mathematical_content_digest(self.record),
                         mathematical_content_digest(changed))

    def test_linux_and_macos_rss_units(self):
        self.assertEqual(peak_rss_bytes(32976, 'Linux'), 33767424)
        self.assertEqual(peak_rss_bytes(33767424, 'Darwin'), 33767424)
        with self.assertRaises(ValueError):
            peak_rss_bytes(32976, 'Unspecified')

    def test_nonfinite_json_is_rejected(self):
        with self.assertRaises(ValueError):
            mathematical_content_digest({'ball': float('nan')})


if __name__ == '__main__':
    unittest.main(verbosity=2)
