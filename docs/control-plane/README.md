# Control-Plane Contracts

`agentos-spine` is the Linux-side integration/workspace spine, but it should not become the long-term canonical home for the MeshSkill and validation lifecycle contract package.

## Canonical source

The typed control-plane contract surface is being re-homed into:

- `SourceOS-Linux/sourceos-spec`

That lane should carry the canonical:

- MeshSkill descriptor specification
- skill execution lifecycle specification
- control-plane schemas
- starter policy packs
- starter contract examples

## Spine responsibility

This repository should consume, reference, and route those contracts into Linux-side integration and workspace assembly flows. It should not fork the canonical schema/doc surface unless a Linux-specific extension is required.

## Public-surface responsibility

Public repos may continue to explain the package downstream, but the spec lane should be treated as the source of truth once the re-home PR lands.
