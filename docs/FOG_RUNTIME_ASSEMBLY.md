# Fog Runtime Assembly in agentos-spine

This document captures the intended **assembly/integration role** of `agentos-spine` for the Fog layer.

The Fog layer is split across multiple repos by design:
- contracts in `SourceOS-Linux/sourceos-spec`
- substrate positioning in `SociOS-Linux/SourceOS`
- first-boot realization in `SociOS-Linux/socios-ignition`
- conformance in `SociOS-Linux/workstation-contracts`

`agentos-spine` is where those pieces are assembled into a working Linux-side runtime topology.

## What belongs in this repo

### 1. Workspace assembly

This repo should define how the fog-capable workspace is composed, including references to:
- substrate lanes
- contract packages
- runtime agents
- deployment manifests
- evidence and policy surfaces

### 2. Runtime graph / adjacency

This repo is the right place to show how the fog runtime connects:
- local storage substrate
- topic replication agent(s)
- compute worker agent(s)
- optional CSI / Kubernetes deployment artifacts
- optional bridge adapters (e.g. external compute market interfaces)

### 3. Deployment/integration manifests

Future assembly artifacts in this repo may include:
- Kubernetes manifests or Helm values for local-storage + fog agents
- workspace manifests / lockfiles describing required components
- runtime topology notes for workstation vs cluster lanes

### 4. Boundary preservation

This repo should **assemble** the system without collapsing boundaries:
- do not redefine schemas that belong in `sourceos-spec`
- do not move substrate invariants out of `SourceOS`
- do not move first-boot logic out of `socios-ignition`
- do not move conformance policy out of `workstation-contracts`

## Candidate assembled components

A future fog assembly in this repo will likely reference or stage:
- local LVM-backed storage readiness
- local CSI/LVM manifests (e.g. TopoLVM lane)
- Hypercore topic replication worker
- FogCompute worker and receipt emitter
- bridge adapters for external settlement/market interfaces

## Expected follow-up

Future PRs here should add:
1. workspace / manifest references for fog-capable lanes
2. deployment manifests for local-storage + fog agents
3. runtime dependency graph notes
4. integration acceptance criteria tying together spec, substrate, ignition, and conformance
