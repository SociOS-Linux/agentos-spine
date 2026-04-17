from __future__ import annotations
from pathlib import Path
import yaml


def load_tritrpc_binding(path: str):
    data = yaml.safe_load(Path(path).read_text())
    return data.get("protocol_bindings", {}).get("tritrpc", {})
