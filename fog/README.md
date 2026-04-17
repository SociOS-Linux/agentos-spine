# Fog runtime assembly scaffold

This directory is the first runtime assembly scaffold for the Fog layer inside `agentos-spine`.

## Intended contents

- workspace or manifest descriptors for fog-capable lanes
- deployment manifests / values for local-storage plus fog agents
- runtime graph notes for workstation vs cluster lanes

## Current scaffold

- `manifests/topolvm-values.yaml` — local-storage values placeholder
- `manifests/fog-agents.values.yaml` — fog agent deployment values placeholder

## Boundary note

This directory assembles components but does not redefine:
- contracts from `sourceos-spec`
- substrate semantics from `SourceOS`
- first-boot logic from `socios-ignition`
- conformance logic from `workstation-contracts`
