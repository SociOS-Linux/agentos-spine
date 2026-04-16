#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print("[build-locks] ERROR: PyYAML is required (pip install pyyaml).", file=sys.stderr)
    raise SystemExit(2) from exc

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        print(f"[build-locks] ERROR: missing {path}", file=sys.stderr)
        raise SystemExit(2)
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        print(f"[build-locks] ERROR: expected mapping in {path}", file=sys.stderr)
        raise SystemExit(2)
    return data


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def normalize_repo(entry: dict[str, Any]) -> dict[str, Any]:
    required = ["id", "org", "repo", "role", "spaces", "sourceType", "status"]
    for k in required:
        if k not in entry:
            raise ValueError(f"repo entry missing required field: {k}")

    return {
        "id": entry["id"],
        "org": entry["org"],
        "repo": entry["repo"],
        "canonicalUrl": f"https://github.com/{entry['org']}/{entry['repo']}",
        "role": entry["role"],
        "category": entry.get("category"),
        "spaces": entry["spaces"],
        "websiteSurface": entry.get("websiteSurface"),
        "canonical": entry.get("canonical"),
        "sourceType": entry["sourceType"],
        "updatedPublic": entry.get("updatedPublic"),
        "status": entry["status"],
        "notes": entry.get("notes"),
        "bootstrapSource": entry.get("bootstrapSource"),
    }


def normalize_framework(entry: dict[str, Any]) -> dict[str, Any]:
    required = ["id", "name", "originClass", "kind", "licensing", "placement", "runtime"]
    for k in required:
        if k not in entry:
            raise ValueError(f"framework entry missing required field: {k}")

    upstream = entry.get("upstream") or {}
    licensing = entry["licensing"]
    placement = entry["placement"]
    runtime = entry["runtime"]

    return {
        "id": entry["id"],
        "name": entry["name"],
        "originClass": entry["originClass"],
        "kind": entry["kind"],
        "upstream": {
            "repo": upstream.get("repo"),
            "sourceType": upstream.get("sourceType"),
            "pin": upstream.get("pin"),
            "provenanceStatus": upstream.get("provenanceStatus"),
            "artifactRefs": upstream.get("artifactRefs", []),
            "related": upstream.get("related", []),
            "conflicts": upstream.get("conflicts", []),
        },
        "bootstrapSource": entry.get("bootstrapSource"),
        "licensing": {
            "declared": licensing.get("declared"),
            "detected": licensing.get("detected"),
            "policyClass": licensing.get("policyClass"),
            "reviewStatus": licensing.get("reviewStatus"),
        },
        "placement": {
            "lane": placement.get("lane"),
            "layer": placement.get("layer"),
            "spaces": placement.get("spaces", []),
            "installPhase": placement.get("installPhase"),
            "packaging": placement.get("packaging"),
            "boxed": placement.get("boxed"),
        },
        "runtime": {
            "os": runtime.get("os", []),
            "arch": runtime.get("arch", []),
            "requires": runtime.get("requires", {}),
        },
        "interfaces": entry.get("interfaces", {"provides": [], "consumes": []}),
        "notes": entry.get("notes"),
        "replacement": entry.get("replacement", {"strategy": None, "candidate": None}),
    }


def build_repos_lock() -> dict[str, Any]:
    path = REGISTRY / "repos.yaml"
    src_text = path.read_text(encoding="utf-8")
    src = read_yaml(path)
    repos = src.get("repos")
    if not isinstance(repos, list):
        raise ValueError("repos.yaml must contain a top-level 'repos' list")
    return {
        "schemaVersion": "0.1-lock",
        "generatedAt": now_utc(),
        "sourceFile": "registry/repos.yaml",
        "inputsHash": sha256_text(src_text),
        "captureMode": src.get("captureMode"),
        "repos": [normalize_repo(r) for r in repos],
    }


def build_frameworks_lock() -> dict[str, Any]:
    path = REGISTRY / "frameworks.yaml"
    src_text = path.read_text(encoding="utf-8")
    src = read_yaml(path)
    frameworks = src.get("frameworks")
    if not isinstance(frameworks, list):
        raise ValueError("frameworks.yaml must contain a top-level 'frameworks' list")
    return {
        "schemaVersion": "0.1-lock",
        "generatedAt": now_utc(),
        "sourceFile": "registry/frameworks.yaml",
        "inputsHash": sha256_text(src_text),
        "policy": src.get("policy", {}),
        "frameworks": [normalize_framework(fw) for fw in frameworks],
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    write_json(REGISTRY / "repos.lock.json", build_repos_lock())
    write_json(REGISTRY / "frameworks.lock.json", build_frameworks_lock())
    print("[build-locks] wrote registry/repos.lock.json")
    print("[build-locks] wrote registry/frameworks.lock.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
