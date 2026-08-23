# Identity And Sensitive-Data Trust Boundaries

Reader question: Where do operator identity, signer capability, machine credentials, signing keys, and sensitive onboarding data cross source-visible trust boundaries?

## Purpose And Evidence Boundary

- **Evidence cutoff:** 2026-08-06, America/Toronto; pinned Community source effective 2026-08-03.
- **Confirmed notation:** solid arrows and solid-border nodes are source-visible paths/surfaces.
- **Inferred notation:** no inferred relationship is asserted in this view.
- **Unknown notation:** dotted arrows and dashed-border nodes identify absent live, Pro, organization, or specialist evidence.
- **Evidence links:** [identity/secrets/data packet](../../../evidence/packets/security-identity-secrets-data-boundaries.md), [architecture data packet](../../../evidence/packets/architecture-data-jobs-migrations-provenance.md), [architecture runtime packet](../../../evidence/packets/architecture-runtime-deployment-delivery-identity-secrets.md), and [signing/verification diagram](../../architecture/diagrams/signing-and-verification-trust-boundary.md).

## Diagram

The panels are read from top to bottom. Repeated application or target-control
nodes refer to the same trust boundary; they are repeated to keep each panel
legible at the default GitHub page width.

### Panel 1 — Operator And Integration Entry

```mermaid
flowchart TB
  classDef unknown stroke-dasharray: 5 5,fill:#f7f7f7,color:#555;

  Operator["Organization operator\npassword + optional TOTP"]
  Integration["Web/mobile integration\nX-Auth-Token bearer credential"]
  IdP["Target IdP / SAML / SCIM / roles\nUNKNOWN; Pro/vendor dependency"]
  App["Community Rails app\n(same application boundary)"]

  Operator -->|"session; account-scoped admin ability"| App
  Integration -->|"API request"| App
  IdP -.-> App

  class IdP unknown;
```

### Panel 2 — Signer Identity And Assurance

```mermaid
flowchart TB
  classDef unknown stroke-dasharray: 5 5,fill:#f7f7f7,color:#555;

  Assurance["Required KYC-to-signer assurance\nUNKNOWN; specialist decision"]
  Signer["External signer\ncapability link; optional email check"]
  App["Community Rails app\n(same application boundary)"]

  Assurance -.-> Signer
  Signer -->|"public form request"| App

  class Assurance unknown;
```

### Panel 3 — Secrets, Encryption, And PDF Signing

```mermaid
flowchart TB
  classDef unknown stroke-dasharray: 5 5,fill:#f7f7f7,color:#555;

  Target["Target IAM, KMS/HSM, network, monitoring\nUNKNOWN"]
  SecretSource["Environment / AWS secret / dotenv fallback"]
  SigningRecord["Encrypted PKCS#12 bytes + password"]
  TSA["Timestamp authority / trust chain\nUNKNOWN"]
  App["Community Rails app\n(same application boundary)"]
  DBKey["Active Record encryption key"]

  Target -.-> App
  SecretSource -->|"root and configuration secrets"| App
  SecretSource -->|"default key derivation"| DBKey
  SigningRecord -->|"optional PDF signing"| App
  TSA -.-> App

  class Target,TSA unknown;
```

### Panel 4 — Runtime Processing

```mermaid
flowchart TB
  classDef unknown stroke-dasharray: 5 5,fill:#f7f7f7,color:#555;

  Target["Target runtime, recovery, and monitoring controls\nUNKNOWN"]
  App["Community Rails app\n(same application boundary)"]
  Queue["Redis / Sidekiq\njobs and retries"]

  Target -.-> App
  App --> Queue
  Target -.-> Queue

  class Target unknown;
```

### Panel 5 — Sensitive-Data Stores

```mermaid
flowchart TB
  classDef unknown stroke-dasharray: 5 5,fill:#f7f7f7,color:#555;

  Target["Target storage, retention, backup, and recovery controls\nUNKNOWN"]
  App["Community Rails app\n(same application boundary)"]
  DBKey["Active Record encryption key\n(same key boundary)"]
  SQL["SQL authority\nPII, workflow, events, search/text derivatives"]
  Blob["Active Storage authority\ndocuments, uploads, results, audit artifacts"]

  App --> SQL
  App --> Blob
  DBKey -->|"selected credential/config fields"| SQL
  Target -.-> SQL
  Target -.-> Blob

  class Target unknown;
```

### Panel 6 — External Webhook Egress

```mermaid
flowchart TB
  classDef unknown stroke-dasharray: 5 5,fill:#f7f7f7,color:#555;

  Target["Target egress, allow-list, and monitoring controls\nUNKNOWN"]
  App["Community Rails app\n(same application boundary)"]
  Webhook["Configured webhook destination"]

  App -->|"PII, values, document/audit URLs"| Webhook
  Target -.-> Webhook

  class Target unknown;
```

## Confirmed Paths And Limits

| Path | Source establishes | Source does not establish | Closure route |
|---|---|---|---|
| Operator → app | Password/TOTP-capable sessions and one account-scoped admin role | Target IdP, global MFA enforcement, least privilege, lifecycle, or live session policy | OI-001 and OI-003 |
| Integration → app | Header bearer-token lookup and account-wide authorization | Pro entitlement, per-client scope/expiry, revocation behavior, or consumer security | OI-001 and OI-005 |
| Signer → app | Slug capability and optional email/link verification | Required identity assurance, secure delivery, or KYC binding | OI-006 plus specialist decision |
| App → SQL/blob/queue | Separate workflow, file, and job authorities | Target encryption, isolation, residency, recovery, retention, deletion, or durability | OI-003 and OI-006 |
| App → webhook | Source-visible signed outbound payload carrying personal and document metadata | Entitlement, enabled destinations, allow-list, receiver controls, residency, or minimization | OI-005 plus target egress/privacy approval |
| Secret/key sources → app | Secret bootstrap, encryption derivation, and optional PKCS#12 signing consumers | Purpose separation, live custody, rotation, revocation, HSM/KMS, or specialist acceptance | OI-002 and OI-003 |

## Known Gaps And Follow-Up

This diagram is a source topology, not a live exposure map. An edge-exposure diagram is intentionally omitted until approved DNS, TLS, ingress, WAF, and reachability evidence exists.
