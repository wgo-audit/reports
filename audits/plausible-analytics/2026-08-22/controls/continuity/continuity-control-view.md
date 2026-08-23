# Continuity Control View

Reader question: what is supported by cutoff-bounded evidence about Plausible's ability to deploy, operate, recover, and transfer control if a person, provider, account, or environment disappears?

CTO decision: current public evidence supports code/configuration and bounded incident history, but not reliance on deploy, recovery, or transferable-control effectiveness until [OI-021](../open-items.md#oi-021), [OI-022](../open-items.md#oi-022), and [OI-023](../open-items.md#oi-023) close.

## Evidence Boundary

This view uses the pinned `primary-code` commit, cutoff-effective public pages, and pre-cutoff GitHub issue, PR, release, Actions, and status history. No production, cloud, account, vendor, billing, staff, or private-runbook evidence was approved. No deploy, restore, alert, access, or failover exercise ran. The expected `recovery-and-operations`, `live-environment-and-access`, and `vendor-ownership-commercial` packets are absent because their live/internal collection was not authorized; no substitute packet was fabricated.

The March 2026 security page is the cutoff-bounded claim baseline. The currently served page labels itself updated August 2026 and adds backup, restore-test, BCP/DR, incident, on-call, and rollback specifics. Those additions have unknown post-cutoff effective time and do not support cutoff assurance ([E-046](../../evidence/evidence-ledger.md#e-046)).

## Evidence Dimensions Used

| Dimension | Evidence available | Bound |
|---|---|---|
| Implementation/configuration | Pinned source for delivery, migration, health, telemetry, queues, and export/object-storage behavior | Defines possible behavior, not deployed state or effectiveness |
| History and rationale | Public GitHub issues, PRs, releases, Actions, and status incidents | Shows selected changes/incidents, not a complete operating record |
| Observed operation | Public incident updates only | No approved dashboard, alert-delivery, restore, deploy, or account evidence |
| Ownership and approval | Public roles and workflow dependencies only | No accountable operator, successor, approval, or break-glass proof |
| Commercial and vendor | Public terms/responsibility statements and named integrations | No contracts, billing, tenant custody, exit plan, or provider recovery proof |
| Specialist or customer corroboration | None approved | Claims remain public-claim or source-bounded positions |

## Source-Bounded Control Position

| Boundary | Cutoff-bounded position | Interruption or transfer exposure | Closure route |
|---|---|---|---|
| Cloud vs CE responsibility | The pinned README assigns managed Cloud availability, backups, security, and maintenance to Plausible, while CE operators own their deployment, upgrades, capacity, uptime, backups, security, and consistency ([E-047](../../evidence/evidence-ledger.md#e-047)). | The public responsibility allocation is stated, but the separately referenced CE packaging/upgrade corpus and effective Cloud operating controls were outside scope. | Verify service-by-service responsibility and keep Cloud evidence distinct from CE operator guidance. |
| Commit to image to live | GitHub workflows build/push private images from `master` and publish CE images from version tags. Pinned Actions show CI and private-image build can complete independently; no Cloud promotion/deploy step is present ([E-007](../../evidence/evidence-ledger.md#e-007), [E-049](../../evidence/evidence-ledger.md#e-049)). | A build notification says “Deploying,” but image creation is not deployment; live identity, authority, approval, and rollback are unknown. | [OI-003](../open-items.md#oi-003), [OI-022](../open-items.md#oi-022) |
| Migration and rollback | Source interweaves PostgreSQL/ClickHouse migrations, segregates schema and application/config changes in PRs, and exposes a generic rollback helper. Issue #5319 and v3.0.1 show a real CE migration-order failure and correction ([E-049](../../evidence/evidence-ledger.md#e-049)). | Deployed order, stop conditions, restore point, backwards compatibility, and exercised rollback are unknown. | [OI-003](../open-items.md#oi-003), [OI-021](../open-items.md#oi-021) |
| Data recovery | The cutoff page claimed remote backups and DR procedures. Source exposes PostgreSQL, ClickHouse, ingestion buffers, asynchronous deletion, and import/export object storage; a public incident said lost data was being restored ([E-002](../../evidence/evidence-ledger.md#e-002), [E-005](../../evidence/evidence-ledger.md#e-005), [E-046](../../evidence/evidence-ledger.md#e-046), [E-050](../../evidence/evidence-ledger.md#e-050), [E-051](../../evidence/evidence-ledger.md#e-051)). | Backup scope, isolation, retention, RPO/RTO, restore completion, cross-store consistency, buffered loss, and deletion interaction are unproved. Object-storage export code is not backup evidence. | [OI-001](../open-items.md#oi-001), [OI-002](../open-items.md#oi-002), [OI-021](../open-items.md#oi-021) |
| Background-job recovery | PostgreSQL-backed Oban configures retries, pruning, peer election, two-hour orphan rescue, and error reporting; some job-specific success/failure paths exist ([E-008](../../evidence/evidence-ledger.md#e-008), [E-051](../../evidence/evidence-ledger.md#e-051)). | Live queue health, delivery, idempotency, replay, and business-result reconciliation are unknown. | [OI-014](../open-items.md#oi-014), [OI-023](../open-items.md#oi-023) |
| Detection and response | Source defines multi-store readiness, multi-region Checkly probes, five-minute PagerDuty routing, Instatus webhooks, Sentry/Oban reporting, and conditional OTel/PromEx. Public status history records provider and ingestion incidents ([E-048](../../evidence/evidence-ledger.md#e-048), [E-050](../../evidence/evidence-ledger.md#e-050)). | Runtime enablement, delivery, dashboard/SLO coverage, responder ownership, diagnosis, recovery validation, customer communication, and postmortem closure are unknown. | [observability path](diagrams/observability-and-response-path.md), [OI-023](../open-items.md#oi-023) |
| Accounts, credentials, and vendors | Public source names critical service/account dependencies but contains no operational ownership or successor register ([E-052](../../evidence/evidence-ledger.md#e-052)). | A person's, provider's, or environment's disappearance can strand authority, MFA, billing, credentials, data export, DNS/registry, status, or support access; the audit cannot identify which are single points of control. | [OI-017](../open-items.md#oi-017), [OI-022](../open-items.md#oi-022) |
| Published images and advisories | Public workflows publish CE images; a Critical CE advisory, removal PR, and fixed release are public and the pinned source is fixed ([E-041](../../evidence/evidence-ledger.md#e-041), [E-049](../../evidence/evidence-ledger.md#e-049)). | Registry authority, affected-image inventory, adoption, incident review, and continuity of advisory/release publishing are unproved. | [OI-020](../open-items.md#oi-020), [OI-022](../open-items.md#oi-022) |

## Material Open Verification

- [OI-021](../open-items.md#oi-021) owns backup/restore scope, RPO/RTO, cross-store recovery, and the public lost-data restoration record.
- [OI-022](../open-items.md#oi-022) owns transferable control, successor access, provider exit, and published-image/advisory authority.
- [OI-023](../open-items.md#oi-023) owns live detection, alert delivery, on-call, job recovery, incident response, and closure evidence.
- Architecture [OI-001](../open-items.md#oi-001)–[OI-005](../open-items.md#oi-005) and Security/Application Security [OI-015](../open-items.md#oi-015)–[OI-020](../open-items.md#oi-020) remain open where they govern runtime truth, deployment, credentials, privacy telemetry, supply-chain authority, and advisory response.

## Documented Outside Audited Scope

- The separately referenced Community Edition packaging and upgrade repository.
- Private BCP/DR, backup/restore, on-call, incident, vendor, account, credential, and commercial records, if they exist.
- Live production/cloud configuration, deployment identity, telemetry state, alert delivery, restoration evidence, and successor access.

These are scope statements, not claims that the controls or records exist.
