# Upstream Receipt — Truth Plane v0 (2026-04)

This document is an **integration receipt** for the Truth Plane v0 work stream.

Goal: provide a single, human-readable reference that answers:

- what merged upstream,
- where the canonical artifacts live,
- what we can run now,
- what remains implementation-only.

---

## 1) Canonical merges (by repository)

### A) SourceOS-Linux/sourceos-spec (contracts + API/event spine)

1. PR #17 — ADR-0001 (TruthSurface B¹¹ + DeltaSurface Δ + incident semantics)
   - merge commit: `17335dd9b0b48e75f1803333147f6d8bbb78577e`
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/17

2. PR #18 — incident schema + truth/delta examples
   - merge commit: `f51801818f2ed4c1341326105239bfd4ec4561ff`
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/18

3. PR #27 — truth-plane OpenAPI/AsyncAPI patch files
   - merge commit: `42e166dd14a152f4594aa2fcd2b520d582608d5c`
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/27

Canonical files to reference after these merges:

- `schemas/TruthSurface.json`
- `schemas/DeltaSurface.json`
- `schemas/control-plane/incident-events.schema.json`
- `openapi.truth-plane.patch.yaml`
- `asyncapi.truth-plane.patch.yaml`

### B) SociOS-Linux/workstation-contracts (portable conformance)

1. PR #3 — Truth Plane fixtures validator (requires local sourceos-spec checkout)
   - merge commit: `1bd6c2a280fe219069f8df7cea3cae6c2ac8e080`
   - https://github.com/SociOS-Linux/workstation-contracts/pull/3

Canonical conformance artifacts:

- `tools/validate_sourceos_truth_plane.py`
- `fixtures/sourceos-spec/examples/{truth-surface.sample.json,delta-surface.sample.json}`
- `conformance/good/truth-plane-fixtures.json`

### C) SociOS-Linux/SourceOS (substrate enforcement plan)

1. PR #3 — Truth Plane enforcement plan + implementation slice
   - merge commit: `a0823e1a510e314485cfb51696c1bad49155c155`
   - https://github.com/SociOS-Linux/SourceOS/pull/3

Canonical docs:

- `docs/TRUTH_PLANE.md`
- `docs/TRUTH_PLANE_IMPLEMENTATION.md`

---

## 2) Substrate v0 implementation commits (post-PR, direct commits)

These commits landed on `SociOS-Linux/SourceOS/main` after the enforcement plan merged.
They provide runnable v0 tooling (local-first, dev signatures, no privileged automation yet).

- TruthSurface emitter: `5b04639ad762c754e9fffecb683aef8d4f4e2542`
- DeltaSurface emitter: `8ba144366acca47768d152ef64bfdb4f9a612ac8`
- IncidentEvent emitter: `b8f193440578eb1a1a0ed59312f7be07f6fb8818`
- nft default-deny egress baseline: `007834685a69bdfcc32a3d9a4bcd1834d770f962`
- egress gate skeleton + replay cache: `4bd982f68e20d2b5ca011dae83261ec1dac7fc22`
- truth-plane runbook: `65e10e266b2eb142f51cd735af88f65e312c189c`
- tick orchestrator: `d82c372c8cf466090f0d998274c47f134622e99f`
- systemd tick service (initial): `5488e613915f362221aac3e7a8052b31fbc0b964`
- systemd tick service (path/hardening fix): `c89eb038e96b29b47567c3b9eb1341c5195f80cf`

---

## 3) What is runnable now (v0)

### A) Conformance proof (workstation/CI lane)

- Validate TruthSurface/DeltaSurface fixtures against the canonical schemas using a local clone of `sourceos-spec`.

### B) Substrate emitters (SourceOS)

- Emit TruthSurface (system.sealed)
- Emit DeltaSurface between the last two TruthSurfaces
- Emit incident.freeze event object
- Initialize replay cache and record dry-run egress grants (no nft mutation yet)

---

## 4) Explicit non-goals (still pending)

- Real signing backend (TPM/HSM/SSHsig) for TruthSurface/DeltaSurface.
- Privileged nftables integration (apply/remove allow rules) inside the gate.
- Fork/Kill incident automation (Freeze is currently event-only in code).
- Runtime truth depth (thread clustering, namespace transition detection).

---

## 5) Next closure criteria

We consider Truth Plane v0 “closed” when:

1) Substrate emits schema-valid TruthSurface/DeltaSurface by default, and
2) Gate enforces default deny + applies scoped allow rules (with replay cache), and
3) A smoke harness demonstrates the end-to-end sequence locally without manual edits.
