# Proof-of-Self Interface Set

This interface family describes how the Linux-side integration spine interacts with the SourceOS Proof-of-Self runtime.

## Owned elsewhere
- Canonical schemas: `SourceOS-Linux/sourceos-spec`
- Runtime implementation: `SourceOS-Linux/sourceos-proof-of-self`
- Substrate hooks: `SociOS-Linux/SourceOS`
- Contract/conformance lanes: `SociOS-Linux/workstation-contracts`
- Optional commons: `SociOS-Linux/socios`

## Interface surfaces
- validator packet create / sign / collect
- PoST issue / verify / revoke / recover
- trust-root resolution
- attestation drift events
- mesh publish / subscribe
