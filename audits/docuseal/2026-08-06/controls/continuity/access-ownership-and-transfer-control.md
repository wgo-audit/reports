# Access, Ownership, And Transfer Control

Coordinator mapping: local `BC-OI-006` and `BC-OI-007` are serialized as canonical OI-015 and OI-016. Local labels remain below for traceability to the reviewer draft.

Reader question: Which accounts, service controls, credentials, vendor dependencies, expiries, and successor capabilities must be assigned and transferable for self-hosted continuity?

## Evidence Boundary

This view uses pinned Community source, registered predecessor evidence, and the [delivery/account/transfer packet](../../evidence/packets/business-continuity-delivery-account-transfer.md). It records source-visible control surfaces and approved evidence limits. It does not infer account ownership, administrator access, staffing, approval, vendor terms, service operation, cost, or transfer readiness from configuration or Git identities.

## Evidence Dimensions Used

| Dimension | Evidence present | Material limit |
|---|---|---|
| Implementation | Release workflow, setup/admin, secret, provider, token, and settings paths | Mechanisms do not establish who controls or can transfer them. |
| History/rationale | Public Git/release activity and source history | Author labels and merges do not prove maintainership authority or succession. |
| Observed operation | Upstream pinned CI/image-build success | No organization target or account access observed. |
| Ownership/approval | `unknown` for every target service/account | No redacted owner/admin/access-review or named successor record supplied. |
| Cost/commercial | `unknown` | No signed support/Pro/on-premises agreement, SLA, renewal, pricing, or exit terms. |
| Specialist evidence | `unknown` | No legal/security/compliance acceptance of custody, transfer, retention, or vendor terms. |

## Current Source-Bounded Position

| Control surface | Source-visible mechanism/dependency | Confirmed owner/admin | Backup owner/successor | Expiry/maintenance boundary | Transfer evidence | Closure route |
|---|---|---|---|---|---|---|
| Source repository and release tags | GitHub tag triggers upstream workflows | `unknown` | `unknown` | Supported versions, review authority, protected release, and vendor response targets unknown | `unknown` | OI-013 and BC-OI-006: obtain release/security ownership, escalation, and successor evidence. |
| Upstream Docker Hub image | Workflow uses repository secrets to publish `docuseal/docuseal` | `unknown` | `unknown` | Token expiry, image retention, digest availability, emergency publish unknown | `unknown` | OI-004/OI-013: mirror/retain verified digest, prove organization-owned intake/rollback, and define vendor escalation. |
| Organization artifact registry/runtime | Required target boundary; no supplied record | `unknown` | `unknown` | Image/base/runtime renewal, patch, capacity, and platform end-of-life unknown | `unknown` | OI-003/OI-004 plus BC-OI-006: service/account inventory and access-transfer rehearsal. |
| DNS, certificate, and ingress | Caddy/example and `HOST`/`FORCE_SSL` configuration only | `unknown` | `unknown` | Domain/certificate ownership, expiry, renewal, emergency change unknown | `unknown` | OI-003/BC-OI-007: redacted registrar/DNS/cert ownership and renewal/failover evidence. |
| First/admin operator | Setup creates first user; Community users are broad admins | `unknown` | `unknown` | MFA/session/access-review/offboarding/break-glass lifecycle unknown | `unknown` | BC-OI-007 with OI-001/OI-003: nominate two trained operators, segregate duties, and prove emergency/offboarding paths. |
| Database and blob storage | Environment/application-selectable SQL and disk/S3/GCS/Azure | `unknown` | `unknown` | Engine/provider support, keys, region, retention, contract, capacity, and replacement lead time unknown | `unknown` | OI-003/OI-006/BC-OI-006: assign service/data owners and exercise export/restore/provider replacement. |
| Redis/Sidekiq | External Redis or Puma-managed local child | `unknown` | `unknown` | Persistence/HA/version/maintenance and dead-set ownership unknown | `unknown` | OI-003/OI-006/BC-OI-006: assign queue owner and demonstrate failover/replay/access transfer. |
| Secret manager/root and signing keys | Environment/AWS/file root; encrypted PKCS#12 plus password; optional TSA | `unknown` | `unknown` | Key/certificate/TSA expiry, rotation, revocation, escrow, HSM/KMS and compromise response unknown | `unknown` | OI-002/OI-004/BC-OI-007: dual-control custody, expiry alerts, break-glass and recovery tests. |
| API/integration credentials | Broad per-user bearer token; replaceable | `unknown` | `unknown` | Scope/expiry/overlap/deprovisioning/consumer inventory unknown | `unknown` | OI-005/BC-OI-007: dedicated identities, rotation handoff, revocation and consumer update evidence. |
| SMTP and webhook services | Operator/environment-configurable providers/destinations | `unknown` | `unknown` | SLA, credential/certificate expiry, bounce/receiver support, replacement path unknown | `unknown` | BC-OI-004/BC-OI-006: provider/consumer ownership, escalation, replacement and failure drill. |
| Monitoring/paging/incident tooling | `/up`, stdout, optional browser Rollbar hooks only | `unknown` | `unknown` | Dashboard/alert/on-call schedule, token/contract renewal, incident record retention unknown | `unknown` | BC-OI-004/BC-OI-006: implement and transfer monitoring, paging, incident roles and retained evidence. |
| DocuSeal vendor/Pro support | Public pages, security mailbox, release history; no signed target commitment | `unknown` | `unknown` | Supported versions, response/patch/notification SLA, Pro entitlement, renewal and exit assistance unknown | `unknown` | OI-001/OI-005/OI-013 and BC-OI-006: obtain release-specific contract/evidence and vendor-exit plan. |

## Material Unknowns And Closure Routes

### Proposed continuity open-item placeholders

| Placeholder | Type | Priority | Item and consequence | Owner | Closure route |
|---|---|---|---|---|---|
| BC-OI-006 | action | P1 | Create a redacted target service/account/vendor control inventory with primary and backup owners; otherwise a person, account, or vendor loss can block deployment, recovery, notification, or customer onboarding. | IT Operations Director, VP Software Engineering, CISO | Record system/account, role, two maintainers, least privilege, access review, region/SLA, renewal/expiry, escalation, export/termination, replacement lead time, and evidence locator; rehearse handoff. |
| BC-OI-007 | verification | P1 | Prove emergency access, privileged-account replacement, secret/key rotation, and control transfer without losing decryptability, trust, or service administration. | IT Operations Director and CISO | Use non-production/safe fixtures to transfer DNS/runtime/database/blob/Redis/monitoring/application administration and rotate integration/key material with rollback and retained evidence. |

Local BC-OI-006 and BC-OI-007 were serialized as OI-015 and OI-016. Release/key/vendor retention work remains covered by OI-002/OI-004/OI-013; no BC-OI-005 was serialized.

- No account console, contract, billing, access review, owner roster, expiry record, offboarding record, or successor exercise was approved or obtained.
- Git identities and successful upstream workflows are not ownership or succession evidence.
- Deployment-template repositories, Docker Hub artifacts, external embed packages, and public status history are **Documented outside audited scope; not independently verified.**
