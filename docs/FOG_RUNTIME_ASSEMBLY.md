# Fog Runtime Assembly in agentos-spine

`agentos-spine` is where the Fog layer's independently-owned pieces are **assembled** into a
working Linux-side runtime topology. It assembles; it does not redefine contracts, substrate
invariants, first-boot logic, or conformance policy.

## Canonical location

The fog-capable-lane workspace descriptor lives in the repo's canonical integration layout
alongside the main workspace manifest:

- **`agentos-spine/agentos-spine/manifest/workspace.fog.toml`**

It mirrors `workspace.toml`'s format (same runner tooling), declares the assembly assets, the
upstream lanes consumed, the runtime adjacency, and the workstation/cluster lane variants.

## Assembly assets (in this repo)

| Asset | File | Role |
|-------|------|------|
| Local storage | `fog/manifests/topolvm-values.yaml` | local-lvm / TopoLVM storage class over `vg_fog` |
| Fog agents | `fog/manifests/fog-agents.values.yaml` | topic replicator + compute worker over `/srv/fog` |

## Consumed upstream lanes (referenced, never redefined)

| Lane | Repo | Reference |
|------|------|-----------|
| Contract | `SociOS-Linux/workstation-contracts` | `contracts/fog-node.contract.json` |
| Conformance | `SociOS-Linux/workstation-contracts` | `tools/check_fog_node.py` + `fog-node.check-receipt.v0` (`make validate-fog-node`) |
| Ignition (first boot) | `SociOS-Linux/socios-ignition` | `profiles/fog/fog-node.bu` (enabled `lvm-bootstrap` + `fog-dirs` units, `/srv/fog` contract) |
| Substrate | `SociOS-Linux/sourceos-build` | `schemas/sourceos/build-request.v0.1.schema.json` (BuildRequest/BuildReceipt) |
| Canonical schemas | `SourceOS-Linux/sourceos-spec` | referenced only — canonical authority stays there |

## Runtime adjacency

```
vg_fog (ignition) ──▶ local-lvm storage class (topolvm-values) ──▶ /srv/fog mount
                                                                       │
                                          fog replicator ◀────────────┘
                                              │ urn:srcos:topic:fog-offers
                                              ▼
                                          fog compute worker ──▶ urn:srcos:topic:fog-receipts
```

## Lane variants — dependencies & acceptance

### Workstation lane (single node, Podman-backed Agent Machine)

- **Requires:** local LVM `vg_fog` (provisioned by the ignition lane), a container host
  (podman/docker), and the `/srv/fog` directory contract materialized at first boot.
- **Storage:** `local-lvm`, `WaitForFirstConsumer`.
- **Acceptance:** `workstation-contracts` `make check-fog-node-host` passes on the node and the
  emitted `fog-node.check-receipt.v0` shows `passed: true`.

### Cluster lane (multi-node, TopoLVM CSI + Kubernetes)

- **Requires:** the TopoLVM CSI installed, `vg_fog` on each fog-capable node, and a namespace
  for the fog agents.
- **Storage:** the `topolvm` `local-lvm` storage class from `topolvm-values.yaml`.
- **Acceptance:** `topolvm-values` + `fog-agents.values` apply cleanly and the
  `urn:srcos:topic:fog-receipts` topic is reachable with receipts emitted.

## Boundary preservation

This repo **assembles** without collapsing boundaries:

- schemas that belong in `sourceos-spec` are referenced, not redefined;
- substrate invariants stay in the substrate lane;
- first-boot logic stays in `socios-ignition`;
- conformance policy stays in `workstation-contracts`.

Image digests are **not** pinned here: `fog-agents.values.yaml` carries logical `imageRef`
URNs that the opt-in catalog layer resolves to digest-pinned images. This repo holds no
registry credentials and no secrets.
