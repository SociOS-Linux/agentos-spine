# LRK Runtime Slice in agentos-spine

This document defines the first practical runtime binding for the LRK / Semantic Holography layer.

## Purpose

`agentos-spine` is the Linux-side assembly spine. It is the correct home for:

- truth/B11-style surface emission wrappers
- ProofOfLife binding into local runtime state
- DeltaSurface generation wrappers
- publication bundle and trust-closure wrappers
- protocol binding references to the external canonical `SocioProphet/TriTRPC` repo

## Follow-on work

- land the LRK integration wrapper files
- land service units for collector / invariant / delta / publication / trust runtime slices
- align naming to upstream TruthSurface / DeltaSurface semantics where required
