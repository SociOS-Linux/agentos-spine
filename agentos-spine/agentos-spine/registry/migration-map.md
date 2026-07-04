# Migration Map: `tools.yaml` -> `repos.yaml` + `frameworks.yaml`

## Purpose
Split the current mixed bootstrap registry into:

- `registry/repos.yaml` for internal repos
- `registry/frameworks.yaml` for external frameworks/packages and internal packs/templates
- later generated locks:
  - `registry/repos.lock.json`
  - `registry/frameworks.lock.json`

## Why this exists
The current spine registry mixes:
- first-party ecosystem repos
- external frameworks/packages
- internal packs/templates/examples
- unresolved archive provenance (`Archive.zip:*`, `*-main.zip`, `external`)

That is valuable bootstrap evidence, but not yet a durable integration model.

## Bucket A -> `registry/repos.yaml`
Move internal ecosystem repos here.

### From current `tools.yaml`
- `sourceos`
- `sociosphere`
- `tritrpc`
- `standards-storage`
- `standards-knowledge`
- `agentplane`
- `tritfabric`
- `socios`
- `global-devsecops-intelligence` (keep blocked until licensing is resolved)

### Add directly from current public org topology
#### SocioProphet
- `SocioProphet/socioprophet`
- `SocioProphet/agentplane`
- `SocioProphet/sociosphere`
- `SocioProphet/contractforge`
- `SocioProphet/prophet-platform`
- `SocioProphet/TriTRPC`
- `SocioProphet/policy-fabric`
- `SocioProphet/socioprophet-agent-standards`
- `SocioProphet/socioprophet-standards-storage`
- `SocioProphet/socioprophet-standards-knowledge`
- `SocioProphet/prophet-platform-standards`

#### SociOS-Linux
- `SociOS-Linux/source-os`
- `SociOS-Linux/SourceOS`
- `SociOS-Linux/socioslinux-web`
- `SociOS-Linux/agentos-spine`
- `SociOS-Linux/socios`
- `SociOS-Linux/workstation-contracts`
- `SociOS-Linux/homebrew-socios`
- `SociOS-Linux/videolab`
- `SociOS-Linux/agentos-starter`
- `SociOS-Linux/enhancements`
- `SociOS-Linux/cloudshell-fog`

#### SourceOS-Linux
- `SourceOS-Linux/sourceos-spec`
- `SourceOS-Linux/openclaw`
- `SourceOS-Linux/nocalhost`
- `SourceOS-Linux/MMTEB-MCP`

## Bucket B -> `registry/frameworks.yaml` as internal packs/templates
Move these as `originClass: internal-pack`:
- `aiwg`
- `skill-seekers`
- `seomachine`
- `agent-inbox`
- `anus`
- `argos`
- `bmad-builder`
- `ace-framework`
- `full-small-app-workflow`
- `rappy-lobster` (keep blocked)

## Bucket C -> `registry/frameworks.yaml` as external frameworks
Move these as `originClass: external-framework`:
- `vercel-ai-sdk`
- `browser-use`
- `agent-s`
- `inbox-zero`
- `fortemi`
- `gastown`
- `opencode`
- `goose`
- `aider`
- `continue`
- `stagehand`
- `tabby`
- `mem0`
- `ad4m`
- `ontogpt`
- `vlmrun`
- `subconscious`
- `zed`
- `warp`

## Unresolved / blocked
### `source-os` vs `SourceOS`
Keep both in `repos.yaml` and mark `canonical: unresolved` until topology is explicitly decided.

### `global-devsecops-intelligence`
Keep in `repos.yaml` but blocked until licensing is explicit.

### `rappy-lobster`
Keep in `frameworks.yaml` but blocked until the license contradiction is resolved.

### `Archive.zip:*` / `*-main.zip` / coarse `external`
Preserve as `bootstrapSource`, but require canonical upstream + pin before allowing inclusion into `system` space.

## Exit criteria
Migration is complete enough to proceed when:
1. Every internal repo entry is present in `repos.yaml` with role + spaces.
2. Every external/framework/internal-pack entry is present in `frameworks.yaml`.
3. Every entry has either canonical upstream + pin or explicit `provenanceStatus: unresolved`.
4. `source-os` vs `SourceOS` is explicitly unresolved until decided.
5. No `Archive.zip:*` entry is treated as canonical provenance.

## Immediate next files
1. `registry/repos.yaml`
2. `registry/frameworks.yaml`
3. `registry/repos.lock.json`
4. `registry/frameworks.lock.json`
