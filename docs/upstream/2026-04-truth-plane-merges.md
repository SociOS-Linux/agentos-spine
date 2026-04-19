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

1. PR #17 — initial Truth Plane ADR work (historical; superseded)
   - merge commit: `17335dd9b0b48e75f1803333147f6d8bbb78577e`
   - note: Truth Plane ADR numbering was later canonicalized to ADR-0009 to eliminate ADR number collisions.
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/17

2. PR #18 — incident schema + truth/delta examples (historical example naming)
   - merge commit: `f51801818f2ed4c1341326105239bfd4ec4561ff`
   - note: truth/delta example filenames were later canonicalized to snake_case in PR #35.
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/18

3. PR #27 — truth-plane OpenAPI/AsyncAPI patch files
   - merge commit: `42e166dd14a152f4594aa2fcd2b520d582608d5c`
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/27

4. PR #35 — spec hygiene: canonicalize Truth Plane ADR + examples + schema IDs
   - merge commit: `258139e16e4a611b0440927b26c93baaf525fcc9`
   - canonical ADR: `docs/adr/0009-truth-surfaces-b11-delta.md`
   - canonical examples: `examples/truth_surface.json`, `examples/delta_surface.json`
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/35

5. PR #38 — control-plane: canonical srcos $id wrappers for legacy schemas
   - merge commit: `62b56ea26677f09d963a734c672f40e53d450a19`
   - establishes two-layer schema identity model in `schemas/control-plane/README.md`
   - canonical wrapper schemas under `schemas/control-plane/*.json`
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/38

6. PR #39 — spec hygiene: eliminate duplicate IncidentEvent $id + reference canonical wrapper
   - merge commit: `ab92673037cce99f82bbf4ca645e1a6d86e214d4`
   - IncidentEvent canonical identity is `schemas/control-plane/IncidentEvent.json`
   - OpenAPI truth-plane patch now references the canonical wrapper
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/39

7. PR #40 — ci(validate): guardrail against duplicate schema $id values
   - merge commit: `a13fbbc91bad1cb3f12e6a4ce6d4dc41a401f8bd`
   - adds `scripts/check_duplicate_schema_ids.py` and wires it into `.github/workflows/validate.yml`
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/40

8. PR #41 — ci(validate): preload control-plane schemas + validate canonical wrapper $id resolution
   - merge commit: `d88db4688ea712883db91c4e9453a5f8fd99b7cf`
   - preloads `schemas/control-plane/*.json` and `schemas/control-plane/*.schema.json` for example validation
   - adds `scripts/validate_control_plane_wrapper_ids.py` guardrail (wrapper id resolution)
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/41

9. PR #42 — ci(validate): extend wrapper $id resolution test to multiple control-plane wrappers
   - merge commit: `b84bf08d7512c25ead0f23986858b5d06a75ecdd`
   - validates wrapper ids and internal $refs for: IncidentEvent, MeshSkill, EnrollmentToken, SkillExecutionEvent
   - https://github.com/SourceOS-Linux/sourceos-spec/pull/42

Canonical files to reference after these merges:

Truth Plane:

- `schemas/TruthSurface.json`
- `schemas/DeltaSurface.json`
- `openapi.truth-plane.patch.yaml`
- `asyncapi.truth-plane.patch.yaml`
- `docs/adr/0009-truth-surfaces-b11-delta.md`
- `docs/adr/0009-truth-surfaces-b11-delta-appendix-a-reuse-map.md`
- `examples/truth_surface.json`
- `examples/delta_surface.json`

Control-plane identity model:

- canonical wrappers: `schemas/control-plane/*.json` (srcos $id)
- legacy imports: `schemas/control-plane/*.schema.json` (legacy $id)
- canonical IncidentEvent: `schemas/control-plane/IncidentEvent.json`
- legacy IncidentEvent schema: `schemas/control-plane/incident-events.schema.json`

CI guardrails:

- `scripts/check_duplicate_schema_ids.py`
- `scripts/validate_control_plane_wrapper_ids.py`

### B) SociOS-Linux/workstation-contracts (portable conformance)

1. PR #3 — Truth Plane fixtures validator (requires local sourceos-spec checkout)
   - merge commit: `1bd6c2a280fe219069f8df7cea3cae6c2ac8e080`
   - note: fixture filenames were later canonicalized to snake_case to match sourceos-spec.
   - https://github.com/SociOS-Linux/workstation-contracts/pull/3

Canonical conformance artifacts:

- `tools/validate_sourceos_truth_plane.py`
- `fixtures/sourceos-spec/examples/{truth_surface.json,delta_surface.json}`
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
They provide runnable v0 tooling (local-first, dev signatures, minimal privilege).

- TruthSurface emitter: `5b04639ad762c754e9fffecb683aef8d4f4e2542`
- DeltaSurface emitter: `8ba144366acca47768d152ef64bfdb4f9a612ac8`
- IncidentEvent emitter: `b8f193440578eb1a1a0ed59312f7be07f6fb8818`
- nft default-deny egress baseline: `007834685a69bdfcc32a3d9a4bcd1834d770f962`
- egress gate skeleton + replay cache: `4bd982f68e20d2b5ca011dae83261ec1dac7fc22`
- truth-plane runbook: `65e10e266b2eb142f51cd735af88f65e312c189c`
- tools package marker (enables intra-tools imports): `cbfa88b18c8f50990b74086020717b8ddc4de9d4`
- tick orchestrator: `d82c372c8cf466090f0d998274c47f134622e99f`
- systemd tick service (initial): `5488e613915f362221aac3e7a8052b31fbc0b964`
- systemd tick service (path/hardening fix): `c89eb038e96b29b47567c3b9eb1341c5195f80cf`
- Truth Plane smoke harness: `de7b1467fb1dd186dea1f783ff1236228b1355ad`

---

## 3) What is runnable now (v0)

### A) Conformance proof (workstation/CI lane)

- Validate TruthSurface/DeltaSurface fixtures against the canonical schemas using a local clone of `sourceos-spec`.

### B) Substrate emitters (SourceOS)

- Emit TruthSurface (system.sealed)
- Emit DeltaSurface between the last two TruthSurfaces
- Emit incident.freeze event object
- Initialize replay cache and record egress grants
- Run a full smoke harness locally (ts0 → ts1 → Δ → incident.freeze)

### C) Scheduling note

- A hardened `sourceos-truth-plane-tick.service` exists (periodic work unit).
- A `*.timer` is intentionally treated as **deployment-lane material** until packaging/policy review is complete.

---

## 4) Explicit non-goals (still pending)

- Real signing backend (TPM/HSM/SSHsig) for TruthSurface/DeltaSurface.
- Fully privileged nftables integration (apply/remove allow rules) inside the gate (v0 begins with controlled, explicit apply).
- Fork/Kill incident automation (Freeze is currently event-only in code).
- Runtime truth depth (thread clustering, namespace transition detection).

---

## 5) Next closure criteria

We consider Truth Plane v0 “closed” when:

1) Substrate emits schema-valid TruthSurface/DeltaSurface by default, and
2) Gate enforces default deny + applies scoped allow rules (with replay cache), and
3) A smoke harness demonstrates the end-to-end sequence locally without manual edits.
