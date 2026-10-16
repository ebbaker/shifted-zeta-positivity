"""Streaming, fail-closed loader for the gzipped JSON ball-matrix archives.

The recorded archives decompress to 344 MB (first step) and 635 MB (second
step); ``json.load`` of the larger one needs more than 3 GB of memory. This
module parses the archive incrementally, converts every entry to an Arb ball
as it is read, and recomputes the canonical matrix-content hash while
streaming, so that the same two hash checks as ``archive.load`` and the v0.1
``archive_io.verify`` are performed without ever holding the JSON object tree.

Canonical serialization (unchanged from ARCHIVE_RECORDS.json): compact UTF-8
JSON of ``data['matrices']`` with sorted dictionary keys, list order and Arb
entries retained, ``ensure_ascii=True``, ``allow_nan=False``. Because the
archives store the matrices in file order (``head`` first) while the canonical
order is sorted, each matrix's canonical text is spooled to a temporary file
and the digest is taken in sorted key order at the end.

Nothing here weakens a check: a size, file-hash, content-hash, or builder-source
mismatch raises, exactly as in the non-streaming loaders.
"""
import gzip
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path
from flint import arb as A, arb_mat as AM
from common import PAPER, HISTORY, legacy_io, verify_legacy, source_hashes

_KEY = re.compile(r'"matrices"\s*:\s*\{')
_NAME = re.compile(r'\s*"([A-Za-z0-9_]+)"\s*:\s*\[')
_WS = re.compile(r'\s*')
_ENC = json.JSONEncoder(sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False)


def unpack(v):
    return A((int(v[0][0]), v[0][1]), (int(v[1][0]), v[1][1]))


def stream_archive(path, want=None, chunk=1 << 22):
    """Return (metadata, {name: arb_mat}, canonical_content_sha256).

    ``want`` restricts which matrices are materialized as arb_mat; every matrix
    is still parsed and hashed. Metadata is the archive with ``matrices``
    replaced by an empty dict.
    """
    dec = json.JSONDecoder()
    f = gzip.open(path, 'rt', encoding='utf-8')
    buf = f.read(chunk)
    m = _KEY.search(buf)
    while not m:
        more = f.read(chunk)
        if not more:
            raise ValueError('Archive has no matrices object')
        buf = buf[-64:] + more
        m = _KEY.search(buf)
    meta_text = buf[:m.start()]
    pos = m.end()
    mats = {}
    spools = {}

    def ensure(pos, n):
        nonlocal buf
        while len(buf) - pos < n:
            more = f.read(chunk)
            if not more:
                break
            buf += more
        return pos

    try:
        while True:
            pos = ensure(pos, 1 << 16)
            m = _NAME.match(buf, pos)
            if not m:
                break
            name = m.group(1)
            pos = m.end()
            spool = tempfile.TemporaryFile(mode='w+b')
            spool.write(b'[')
            first = True
            rows = []
            while True:
                pos = ensure(pos, chunk)
                pos = _WS.match(buf, pos).end()
                if buf[pos] == ']':
                    pos += 1
                    break
                if buf[pos] == ',':
                    pos += 1
                    continue
                while True:
                    try:
                        row, end = dec.raw_decode(buf, pos)
                        break
                    except json.JSONDecodeError:
                        more = f.read(chunk)
                        if not more:
                            raise
                        buf += more
                if not first:
                    spool.write(b',')
                first = False
                spool.write(_ENC.encode(row).encode('utf-8'))
                if want is None or name in want:
                    rows.append([unpack(x) for x in row])
                pos = end
                if pos > (1 << 23):
                    buf = buf[pos:]
                    pos = 0
            spool.write(b']')
            spools[name] = spool
            if want is None or name in want:
                mats[name] = AM(rows)
            del rows
            pos = ensure(pos, 1 << 16)
            pos = _WS.match(buf, pos).end()
            if buf[pos] == ',':
                pos += 1
        rest = buf[pos:] + f.read()
        f.close()
        meta = json.loads(meta_text + '"matrices":{' + rest)
        h = hashlib.sha256()
        h.update(b'{')
        for i, name in enumerate(sorted(spools)):
            if i:
                h.update(b',')
            h.update(_ENC.encode(name).encode('utf-8') + b':')
            spool = spools[name]
            spool.seek(0)
            for block in iter(lambda: spool.read(1 << 22), b''):
                h.update(block)
        h.update(b'}')
        return meta, mats, h.hexdigest()
    finally:
        for spool in spools.values():
            spool.close()


def _locate(rel, primary_root):
    rel = Path(rel)
    if rel.is_absolute() or '..' in rel.parts:
        raise ValueError('Unsafe archive path')
    path = Path(primary_root) / rel
    if not path.is_file():
        root = os.environ.get('STORAGE_DEPTH_ARCHIVES')
        if root:
            path = Path(root).expanduser() / rel
    if not path.is_file():
        raise FileNotFoundError(f'Missing {rel}. Set STORAGE_DEPTH_ARCHIVES or regenerate using ARCHIVES.md.')
    return path


def load_record(record_path, want=None):
    """Streaming equivalent of archive.load: current-step build record."""
    record = json.loads(Path(record_path).read_text())
    path = _locate(record['matrix_archive'], PAPER / 'numerics')
    if path.stat().st_size != record['bytes']:
        raise ValueError('Archive size mismatch')
    if legacy_io.file_hash(path) != record['matrix_archive_sha256']:
        raise ValueError('Archive file hash mismatch')
    meta, mats, content = stream_archive(path, want)
    if content != record['matrices_content_sha256']:
        raise ValueError('Matrix content hash mismatch')
    for name, digest in meta['source_sha256'].items():
        if source_hashes().get(name) != digest:
            raise ValueError(f'Builder source mismatch: {name}')
    verify_legacy()
    return meta, mats, record, path


def load_legacy(relative_path, want=None):
    """Streaming equivalent of the v0.1 archive_io.verify + read_data."""
    records = {r['path']: r for r in legacy_io.catalog()}
    if relative_path not in records:
        raise ValueError(f'No committed hash record for {relative_path}')
    record = records[relative_path]
    path = _locate(relative_path, legacy_io.HERE)
    if path.stat().st_size != record['bytes']:
        raise ValueError(f'Archive size mismatch: {relative_path}')
    if legacy_io.file_hash(path) != record['matrix_archive_sha256']:
        raise ValueError(f'Archive file hash mismatch: {relative_path}')
    meta, mats, content = stream_archive(path, want)
    if content != record['matrices_content_sha256']:
        raise ValueError(f'Archive matrix content hash mismatch: {relative_path}')
    for name, digest in meta.get('source_sha256', {}).items():
        if legacy_io.file_hash(HISTORY / name) != digest:
            raise ValueError(f'Seed source mismatch: {name}')
    verify_legacy()
    return meta, mats, record, path
