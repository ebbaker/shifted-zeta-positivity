"""Verified archive lookup for the storage-depth continuation package.

Only two locations are searched: the normal numerics-relative path, then the
same relative path under STORAGE_DEPTH_ARCHIVES. This module has no downloads.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG = HERE / "ARCHIVE_RECORDS.json"

def file_hash(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def matrix_content_hash(data):
    """SHA256 of UTF-8 compact sorted-key JSON of data['matrices'] only.

    List order and every serialized Arb midpoint/radius entry are preserved.
    Metadata, elapsed time, gzip filename, gzip time, and compression are
    excluded. This is data identity, not a substitute for an arithmetic test.
    """
    h = hashlib.sha256()
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"),
                               ensure_ascii=True, allow_nan=False)
    for chunk in encoder.iterencode(data["matrices"]):
        h.update(chunk.encode("utf-8"))
    return h.hexdigest()

def read_data(path):
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)

def describe(path, relative_path):
    data = read_data(path)
    parameters = {k: data[k] for k in
                  ("N", "M", "precision_bits", "horizon", "log_horizon",
                   "old_modes", "new_modes", "profile_degree", "log_series_degree")
                  if k in data}
    return {"path": relative_path, "bytes": Path(path).stat().st_size,
            "matrix_archive_sha256": file_hash(path),
            "matrices_content_sha256": matrix_content_hash(data),
            "parameters": parameters}

def catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))["archives"]

def locate(relative_path):
    rel = Path(relative_path)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError("Archive path must be a safe numerics-relative path")
    primary = HERE / rel
    if primary.is_file():
        return primary
    external_root = os.environ.get("STORAGE_DEPTH_ARCHIVES")
    if external_root:
        external = Path(external_root).expanduser() / rel
        if external.is_file():
            return external
    raise FileNotFoundError(
        f"Missing archive: {relative_path}\n"
        "Set STORAGE_DEPTH_ARCHIVES to the supplied numerics-archives folder, "
        "or regenerate with:\n"
        "  python numerics/replay.py rebuild --output-dir /your/new/run-folder\n"
        "For the optional 128-mode cache use rebuild-initial. See ARCHIVES.md.")

def verify(relative_path):
    records = {r["path"]: r for r in catalog()}
    if relative_path not in records:
        raise ValueError(f"No committed hash record for {relative_path}")
    record = records[relative_path]
    path = locate(relative_path)
    if path.stat().st_size != record["bytes"]:
        raise ValueError(f"Archive size mismatch: {relative_path}")
    if file_hash(path) != record["matrix_archive_sha256"]:
        raise ValueError(f"Archive file hash mismatch: {relative_path}")
    data = read_data(path)
    if matrix_content_hash(data) != record["matrices_content_sha256"]:
        raise ValueError(f"Archive matrix content hash mismatch: {relative_path}")
    return path
