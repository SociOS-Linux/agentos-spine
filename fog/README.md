# Fog runtime assembly

Runtime assembly for the Fog layer inside `agentos-spine`. This directory holds the
deployment values that the fog-capable-lane workspace descriptor composes.

## Contents

- `manifests/topolvm-values.yaml` — local-lvm / TopoLVM storage-class values over `vg_fog`
- `manifests/fog-agents.values.yaml` — topic replicator + compute worker values over `/srv/fog`

## Descriptor

These assets are wired together by the canonical fog workspace descriptor:

- **`../agentos-spine/agentos-spine/manifest/workspace.fog.toml`**

See [`../docs/FOG_RUNTIME_ASSEMBLY.md`](../docs/FOG_RUNTIME_ASSEMBLY.md) for the assembled
topology, the workstation vs cluster lanes (dependencies + acceptance), and the map of
upstream lanes this repo consumes.

## Boundary note

This directory assembles components but does not redefine:
- contracts / canonical schemas from `SourceOS-Linux/sourceos-spec`
- substrate from `SociOS-Linux/sourceos-build`
- first-boot logic from `SociOS-Linux/socios-ignition`
- conformance logic from `SociOS-Linux/workstation-contracts`
