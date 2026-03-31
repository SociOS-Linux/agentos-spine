# agentos-spine

Current Linux-side integration/workspace spine for AgentOS / SourceOS.

This repo is the working Linux-side assembly spine that ties together SourceOS substrate, typed contracts, execution/runtime layers, opt-in automation, and upstream platform orchestration without collapsing them into one repo.

## Topology position

- **Role:** current Linux-side integration/workspace spine.
- **Connects to:**
  - `SociOS-Linux/SourceOS` — immutable OS substrate
  - `SourceOS-Linux/sourceos-spec` — canonical typed contracts, JSON-LD contexts, and shared vocabulary
  - `SociOS-Linux/workstation-contracts` — workstation/CI contract and conformance lane
  - `SociOS-Linux/socios` — opt-in automation commons
  - `SocioProphet/sociosphere` — platform meta-workspace controller
  - `SociOS-Linux/socioslinux-web` — Linux public web/docs surface
- **Not this repo:**
  - immutable OS substrate
  - final typed-contract registry
  - public docs site
  - opt-in automation plane
- **Operational note:** current imported working material lives under `agentos-spine/agentos-spine/`. That should be normalized over time, but this root README is the canonical repo-role statement now.
- **Semantic direction:** this repo should eventually publish a repo-level JSON-LD descriptor using the shared SourceOS/SociOS vocabulary from `sourceos-spec`.

## Where to look next

- `agentos-spine/agentos-spine/README.md` — imported spine notes
- `agentos-spine/agentos-spine/manifest/workspace.toml` — imported workspace map
- `agentos-spine/agentos-spine/interfaces/` — imported interface set
