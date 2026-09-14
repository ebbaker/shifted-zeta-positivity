"""Small tests of external-data integrity and lookup; no mathematical claims."""
import gzip
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import archive_io as io

class ArchiveIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.local, self.external = self.root/"local", self.root/"external"
        self.local.mkdir()
        self.external.mkdir()
        self.rel = "history/test/matrices.json.gz"
        self.target = self.external/self.rel
        self.target.parent.mkdir(parents=True)
        self.data = {"matrices": {"B": [["0","1"]], "A": [["2","3"]]},
                     "elapsed": 1}
        with gzip.open(self.target, "wt") as stream:
            json.dump(self.data, stream)
        self.record = io.describe(self.target, self.rel)
        self.catalog = self.root/"catalog.json"
        self.write_catalog()
        self.patches = [patch.object(io,"HERE",self.local),
                        patch.object(io,"CATALOG",self.catalog),
                        patch.dict(os.environ,{"STORAGE_DEPTH_ARCHIVES":str(self.external)})]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in reversed(self.patches):
            p.stop()
        self.temp.cleanup()

    def write_catalog(self):
        self.catalog.write_text(json.dumps({"archives":[self.record]}))

    def test_external_lookup_and_both_hashes(self):
        self.assertEqual(io.verify(self.rel), self.target)

    def test_normal_location_precedes_external_and_bad_local_fails(self):
        local = self.local/self.rel
        local.parent.mkdir(parents=True)
        local.write_bytes(self.target.read_bytes())
        self.assertEqual(io.verify(self.rel), local)
        local.write_bytes(b"x"*local.stat().st_size)
        with self.assertRaisesRegex(ValueError,"file hash mismatch"):
            io.verify(self.rel)

    def test_missing_message_explains_regeneration(self):
        with self.assertRaisesRegex(FileNotFoundError,"replay.py rebuild"):
            io.locate("history/missing.json.gz")

    def test_path_escape_rejected(self):
        with self.assertRaises(ValueError):
            io.locate("../matrices.json.gz")

    def test_content_mismatch_fails_even_with_valid_file_hash(self):
        self.record["matrices_content_sha256"] = "0"*64
        self.write_catalog()
        with self.assertRaisesRegex(ValueError,"content hash mismatch"):
            io.verify(self.rel)

    def test_content_canonicalization_ignores_metadata_and_key_order(self):
        other = {"elapsed": 99, "matrices":{"A":[["2","3"]],"B":[["0","1"]]}}
        self.assertEqual(io.matrix_content_hash(self.data),io.matrix_content_hash(other))
        other["matrices"]["A"][0][0] = "4"
        self.assertNotEqual(io.matrix_content_hash(self.data),io.matrix_content_hash(other))

if __name__ == "__main__":
    unittest.main()
