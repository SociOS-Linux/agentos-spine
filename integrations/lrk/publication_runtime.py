from __future__ import annotations
import json
import subprocess
from pathlib import Path


def build_publication(bundle_id: str, artifacts, out_path: str, prev_hash: str = "0000", creator_sig: str = "", twin_sig: str = "") -> str:
    cmd = [
        "lrk-build-publication",
        "--bundle-id", bundle_id,
        "--prev-hash", prev_hash,
        "--out", out_path,
    ]
    if creator_sig:
        cmd.extend(["--creator-sig", creator_sig])
    if twin_sig:
        cmd.extend(["--twin-sig", twin_sig])
    cmd.extend(list(artifacts))
    subprocess.check_call(cmd)
    return out_path


def load_publication(path: str):
    return json.loads(Path(path).read_text())
