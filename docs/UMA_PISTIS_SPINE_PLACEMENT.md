# UMA Pistis spine placement

This document records what belongs in `agentos-spine` for the UMA Pistis local-first platform assembly.

It is intentionally scoped to integration and composition. It does **not** redefine the immutable substrate, the canonical contract layer, or the opt-in automation plane.

---

## Why this repo is the right home

`agentos-spine` already declares itself as the Linux-side integration/workspace spine that ties together substrate, typed contracts, execution/runtime layers, opt-in automation, and upstream platform orchestration.

That makes it the correct place for the following UMA Pistis concerns:

- local-first service composition
- CloudHaven-facing workspace and service routing
- promotion from local-first to shared mesh when quorum exists
- runtime binding of typed contracts to actual execution surfaces
- graceful degradation when the mesh is unavailable or inadmissible

---

## Placement rules

### What belongs here

1. **CloudHaven / workspace composition**
   - service discovery
   - provider binding
   - local-first fallback routing
   - shared-mesh promotion and demotion behavior

2. **Runtime assembly**
   - mapping typed `sourceos-spec` objects to runnable surfaces
   - binding execution lanes, local services, and shared services
   - routing between ingress, overlay, event fabric, and viewer/search surfaces

3. **Promotion orchestration**
   - quorum-aware transition logic
   - health/admissibility checks before promotion
   - drain and rollback choreography

4. **Operational integration**
   - integration with Argo/Tekton execution control when validated lanes are run
   - consumption of Foreman/Katello-provisioned images/content inputs

### What does not belong here

- canonical schema definitions (`sourceos-spec`)
- immutable substrate/image definition (`source-os`)
- lane contract definition and conformance (`workstation-contracts`)
- opt-in automation commons (`socios`)

---

## Canonical UMA Pistis surfaces this repo should compose

| Surface | Role in spine |
|---|---|
| UMA Pistis | overall local-first platform shell |
| MICHAEL | identity/session binding to execution surfaces |
| ANSER | ingress / front-door binding for user and service entry |
| IANUS | overlay bridge wiring across local, mesh, and cluster lanes |
| PHAROS / ARIADNE | event fabric and thread semantics consumed by runtime services |
| ASHAMAAT | consensus/finality source consulted for shared-mesh trust state |
| PRAXIS | immutable act stream consumed for evidence, replay, and state reflection |
| Arbor / Codex | immutable roots and object/edition storage presented to services |
| Mnemosyne / Hypethia | search and evidence-view surfaces |
| ARGUS PHYLAX | observability and admissibility inputs |
| Kairos | deadline/SLO windows used during routing and retries |
| Shiloh | quorum and promotion controller logic |

---

## Promotion model

The spine should treat promotion to shared execution as a **runtime orchestration concern**, not a schema concern and not a substrate concern.

Promotion should require at minimum:

- sufficient human quorum
- healthy overlay corridors
- acceptable event-watermark freshness
- capacity/admissibility green state
- privacy/policy constraints satisfied

If any gate fails, the spine keeps the workload local-first and must expose a human-readable denial reason.

---

## Immediate backlog

1. Add a spine-level runtime descriptor for UMA Pistis surfaces and bindings.
2. Add promotion-state documentation and examples for local-first → shared-mesh → rollback.
3. Add integration notes showing how CloudHaven binds to local and shared providers through the spine.
4. Add a simple operator-facing matrix showing which repo owns which change type.
5. Add examples of how Argo/Tekton lane execution and Foreman/Katello content inputs meet here without collapsing responsibilities.

---

## Recommended next steps

1. Add a repo-level descriptor that imports the shared `sourceos-spec` vocabulary and identifies UMA Pistis runtime bindings.
2. Add docs or values/examples for promotion gating inputs (`quorum`, `watermark freshness`, `capacity`, `privacy policy`).
3. Add CloudHaven-facing service binding examples for local-only, mesh-enabled, and degraded states.
