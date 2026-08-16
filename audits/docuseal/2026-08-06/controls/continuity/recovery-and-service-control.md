# Recovery And Service Control

Coordinator mapping: local `BC-OI-004` is serialized as canonical OI-014. Local labels remain below for traceability to the reviewer draft.

Reader question: Which source-visible dependencies and interruption paths must be covered by a target recovery design before self-hosted DocuSeal can support revenue-critical onboarding?

## Evidence Boundary

This source-bounded control view covers DocuSeal Community `3.1.7` at commit `a2d8b855491793870b7b4acf176d2d95ae95ff83`, registered Architecture/Security evidence, and the [continuity recovery packet](../../evidence/packets/business-continuity-recovery-dataops-alerting.md). The auditor supplied availability and RPO targets; the view does not establish their measurement definitions, implementation, ownership, achievement, backup completion, restore success, alert delivery, incident response, or production readiness. No exercise was run.

## Evidence Dimensions Used

| Dimension | Evidence present | Material limit |
|---|---|---|
| Implementation | SQL/blob authority, Puma/Sidekiq/Redis topology, migration, mail/webhook, health/log, and artifact-generation source | Source presence does not prove effective operation or recovery. |
| History/rationale | Cutoff-bounded release/CI/image history and a volume-dependent migration note | Release activity and estimates do not establish target objectives or tested recovery. |
| Observed operation | Successful upstream CI/image build only | No target service, backup, restore, alert, incident, queue, or failover observation. |
| Ownership/approval | Auditor-approved availability/RPO boundary present; execution ownership otherwise `unknown` | No continuity owner, incident roles, service owner, measurement approval, or accepted runbook. |
| Cost/commercial | `unknown` | No target service tiers, vendor terms, replacement lead times, or recovery cost. |
| Specialist evidence | `unknown` | No legal/compliance/security acceptance of recovery, retention, key custody, or evidence preservation. |

## Current Source-Bounded Position

| Dependency or interruption | Source-visible position | Detection evidence | Source-visible control | Material unknown | Required closure route |
|---|---|---|---|---|---|
| Rails/Puma service | One process surface serves operator, signer, API, files, jobs, and setup; repository Compose publishes Caddy and Rails port 3000. | `/up` and stdout request logs | Puma process lifecycle; Caddy example | Readiness dependencies, HA, replica/session behavior, ingress failover, measurement definitions, SLO/alert owner | OI-003/BC-OI-004: demonstrate 99.5% monthly signing and 99% onboarding availability measurement/recovery. Onboarding may pause; communication, reconciliation, and controlled resume remain required. |
| PostgreSQL/application database | SQL owns workflow, signer, events, hashes, configuration, and file metadata. | No database-specific target probe or alert evidenced | Adapter selection; transaction boundaries; PostgreSQL Compose health only | Production engine/version, HA/PITR, backup frequency/retention, replica/failover, restore order, integrity oracle | OI-003/OI-006: design and exercise point-in-time recovery with blob/key reconciliation against the two-hour RPO. |
| Active Storage bytes | Disk/S3/GCS/Azure hold source, upload, result, audit, and combined artifacts. | No blob/object-store target probe or alert evidenced | Configurable private proxy/provider selection | Provider, versioning/lock, replication, encryption keys, backup, restore, orphan cleanup, residency, legal hold, deletion | OI-006: define the authoritative set and prove restored bytes, references, hashes, and access controls. |
| Redis/Sidekiq | Completion, mail, webhooks, indexing, schedules, and retries depend on Redis/Sidekiq; defaults can be Puma-managed. | Sidekiq UI for admins; no approved queue dashboard/alert evidence | Named queues, retries, scheduled jobs; local Redis death interrupts Puma | External/embedded target, persistence/HA, drain, dead set, backlog thresholds, replay, schedule recovery, owner | OI-003/OI-006: isolate/test queue failure, lost schedule, backlog, restart, replay, and reconciliation. |
| Artifact generation | SQL lock events suppress duplicate result/audit/combined generation; blob upload and completion marker are separate. | Errors reach logs and conditional Rollbar hooks | Retry/fail lock states and 90-second waits | Stale-lock/orphan cleanup, artifact correctness after crash, repair/reconciliation owner, terminal alert | OI-006: run crash-point and known-answer recovery tests with retained artifacts. |
| Database migration/startup | Production boot migrates unless disabled; pinned data migration can be non-reversible. | Startup/log outcome only; no migration alert evidence | `RUN_MIGRATIONS=false` can decouple application boot | Dedicated migration identity/connection, replica coordination, backup/rehearsal, compatibility, rollback/roll-forward, recovery time | OI-004: establish a controlled migration/release gate and test failure/restore. |
| SMTP/email | Completion/invitation mail is queued; delivery errors are not raised by default. | Email-event rows after delivery observer; no bounce/alert path evidenced | SMTP timeouts; job retries; setup test mail | Provider SLA, queue/bounce monitoring, credential owner, terminal failure response | BC-OI-004: define delivery SLO, detection, escalation, communication, replay, reconciliation, and controlled resume. |
| Webhook integration | Event/attempt rows, HMAC, finite timeouts, and exponential retries exist. | Persisted success/error attempts; settings UI can filter/resend | Bounded retries and manual test resend | Consumer SLA, ordering/deduplication, terminal failure alert, replay authority, downstream reconciliation, alternate path | BC-OI-004 plus OI-005: approve consumer contract and demonstrate failure/replay/reconciliation. |
| Signing key/TSA and root secrets | Secret roots decrypt/sign multiple purposes; PKCS#12/TSA are application-managed and signing is conditional. | Conditional errors/log hooks; no key/TSA expiry or availability alert evidenced | Environment/AWS/file secret loading; optional TSA fallback; encrypted record | Custody, versions, rotation, expiry, revocation, escrow, HSM/KMS, restore, independent validation, TSA outage behavior | OI-002/OI-006: decide custody and prove recovery without invalidating evidence. |
| Release image and dependencies | Tag-built multi-arch image succeeded; source/public paths use mutable references and lack a demonstrated promotion/rollback chain. | Upstream Actions status only | Pinned identifiable source and observed upstream image build | Candidate digest, mirror/retention, SBOM/provenance, target admission, rollback artifact, vendor/source outage path | OI-004/OI-013: retain verified digests/source, define vendor maintenance, and exercise rollback/alternate supply. |

## Material Unknowns And Closure Routes

### Proposed continuity open-item placeholders

| Placeholder | Type | Priority | Item and consequence | Owner | Closure route |
|---|---|---|---|---|---|
| BC-OI-004 | action | P1 | Define availability measurement, dependency-aware monitoring, terminal-failure response, on-call/escalation, incident command, safe pause, communication, reconciliation, and controlled resume. | IT Operations Director, Product Manager, VP Software Engineering | Implement readiness/metrics/alerts; prove delivery and acknowledgement; assign roles; exercise incident handling and demonstrate retained monthly signing/onboarding availability evidence. |

BC-Q-001 was answered on 2026-08-06; no separate target item was serialized. Recovery/restore/reconciliation work is already covered by OI-003/OI-006, and release/key/vendor continuity by OI-002/OI-004/OI-013, so BC-OI-002/003/005 were not serialized. Local BC-OI-004 was serialized as OI-014.

- No approved backup, restore, recovery, failover, queue, alert-delivery, or incident evidence exists; configuration is not accepted as operation.
- Public Cloud recovery/monitoring and external status history have a different boundary. The status domain is **Documented outside audited scope; not independently verified.**
- The exact observability-and-response-path artifact was not selected because no approved dashboard, alert ownership, incident, or alert-delivery evidence met its trigger.
