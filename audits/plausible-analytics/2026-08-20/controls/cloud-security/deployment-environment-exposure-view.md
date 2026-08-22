# Deployment And Environment Exposure View

## Purpose And Evidence Boundary

- Reader question: Where can identity, artifact, environment, and network trust change between approved source and a library or hosted runtime?
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto.
- Confirmed notation: solid source-declared build/runtime edge.
- Conditional notation: dashed relationship whose enforcement is not observed.
- Unknown notation: dotted deployment, identity, registry, or hosted boundary not accessed.
- Evidence links: [E-007](../../evidence/evidence-ledger.md#e-007), [E-010](../../evidence/evidence-ledger.md#e-010), [E-028](../../evidence/evidence-ledger.md#e-028), and [E-040](../../evidence/evidence-ledger.md#e-040)–[E-043](../../evidence/evidence-ledger.md#e-043).

## Evidence Dimensions Used

Build/release and runtime implementation are present. Public exact-commit CI evidence is present. Tag authority, effective workflow and bot-token permissions, registry controls, promotion/admission, library deployment, hosted deployment, live operation, and ownership/approval are unknown.

## Source-Bounded Exposure Path

```mermaid
flowchart TB
  subgraph CHANGE["Source-visible change and build"]
    direction LR
    PR["Tracker-update pull-request workflow"] --> PRJOB["Validation and bot-token mutation share one job"]
    TAG["v* tag push"] --> BUILD["CE multi-architecture image build"] --> DIGEST["Per-platform digests and manifest"]
  end
  subgraph CONSUME["Unknown library consumption"]
    direction LR
    REG["GHCR policy, immutability, scanning: unknown"] -.-> PIN["Library digest pin/admission: unknown"] -.-> RUN["UID 999 container on library runtime: unknown"]
  end
  subgraph RUNTIME["CE source-declared runtime interfaces"]
    direction LR
    PORT["0.0.0.0:8000 / optional CE TLS"] --> EDGE["DNS, TLS termination, proxy-header rewrite, WAF: unknown"]
    SECRET["Environment or /run/secrets values"] --> APP["Phoenix and optional integrations"]
    APP --> PG["PostgreSQL transport/control: configuration-dependent"]
    APP --> CH["ClickHouse transport/control: configuration-dependent"]
  end
  PRJOB -. "credential scope/isolation and any influence on tag/release: unknown" .-> PRBOUNDARY["Release-authority boundary: unknown"]
  DIGEST -. "registry handoff" .-> REG
  RUN -. "port publication and secret wiring unknown" .-> RUNTIME
  HOSTED["Separate Subscribe boundary: hosted build, IAM, registry, edge and runtime evidence unavailable"]

  classDef unknown stroke-dasharray: 3 3,fill:#fff7ed,stroke:#c2410c;
  class PRBOUNDARY,REG,PIN,RUN,EDGE,HOSTED unknown;
```

## Current Source-Bounded Position

| Stage | Confirmed mechanism | Exposure or unknown | Closure |
|---|---|---|---|
| Change identity | Default branch had enforced merge checks for the exact commit. Tracker NPM publishing uses OIDC. | Tag authority and environment approvals are unknown; tracker repository mutation still uses a bot token. | [OI-005](../open-items.md#oi-005), [OI-016](../open-items.md#oi-016) |
| Pull-request automation | The tracker update job narrows `GITHUB_TOKEN` permissions. | A separate bot token is provided in the same job that later runs pull-request-controlled dependency/install/build code; scope and isolation are unknown. | [OI-016](../open-items.md#oi-016) |
| CE image production | Commit-pinned Actions build digest-addressed platform images and one manifest; base images are digest-pinned. | Public workflow token scopes depend on repository settings; no source-visible SBOM/signature/attestation or quality-workflow dependency was found. | [OI-005](../open-items.md#oi-005) |
| Registry and promotion | Produced digests can be consumed by immutable reference. | Registry policy, scan results, retention, tag mutability, promotion, and library admission are unavailable. | [OI-005](../open-items.md#oi-005) |
| Container and data path | Image runs non-root and exposes an explicit data volume/port. | Deployed digest, security context, volume permissions/sharing, network policy, secret provider, and datastore transport are unknown. | [OI-001](../open-items.md#oi-001) |
| Subscribe | Public hosted security assertions describe control categories. | Hosted CI/CD, IAM, registry, deployment, network, and runtime evidence is non-public and excluded; CE source cannot substitute. | Obtain dated service-specific control evidence and assign retained library/vendor responsibilities through [OI-015](../open-items.md#oi-015). |

## Known Gaps And Follow-Up

Documented outside audited scope; not independently verified. The separate Community Edition repository and the library's redacted deployment definition are the smallest useful Run expansion for image selection, network/volume wiring, and upgrades. For Subscribe, obtain service-specific assurance and responsibility evidence through procurement/security review. Do not use the diagram to claim current exposure, compromise, control effectiveness, or hosted implementation.
