# LRK Runtime Spine Note

This note anchors the LRK / Semantic Holography runtime integration in `agentos-spine`.

## Role of this repo

`agentos-spine` is the Linux-side assembly spine.

It is the correct home for:
- runtime wrappers for surface emission
- ProofOfLife binding into local state
- DeltaSurface generation wrappers
- publication bundle assembly wrappers
- trust-closure and governance-grade verification wrappers
- protocol-binding runtime references to the external canonical `SocioProphet/TriTRPC` repo

## Follow-on work

- land the LRK integration wrapper files
- land service units for collector / invariant / delta / publication / trust runtime slices
- align surface naming to upstream TruthSurface / DeltaSurface semantics where required
