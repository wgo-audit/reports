# Business Continuity

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether Plausible can be deployed, operated, recovered, and transferred when a person, account, datastore, environment, vendor, or supporting service disappears, and how that changes the Run/Subscribe/Replace decision. The cutoff is 2026-08-20 at onboarding start, America/Toronto. Evidence is the approved `primary-code` snapshot at commit `9cc669b97ece3ecd37fcb3950791cb3873d7944d`, cutoff-effective public terms/account/export material, predecessor evidence, and current hosted-security claims used only as post-cutoff validation.

The review covered PostgreSQL, ClickHouse, in-process buffers/session transfer, images, migration/rollback mechanisms, Oban queues/schedules, monthly mail delivery, site deletion, health/telemetry surfaces, software ownership transfer, CE maintenance/support, hosted public continuity statements/terms, and exit mechanisms. It did not inspect or change a library or hosted environment, restore data, run load/failure tests, install dependencies, access traffic/accounts/contracts, interview staff, assess a replacement candidate, or make legal conclusions. Source mechanisms and vendor statements are not recovery proof.

## Coverage And Material Gaps

The source supports a bounded continuity model, but option acceptance remains conditional. Run lacks approved proof of the deployed topology, dual-store backup/restore, coordinated rollback, queue/report/deletion health, alert ownership, and primary/successor control. Subscribe has public continuity claims but no approved independent control evidence, negotiated commitment, support escalation, recovery objectives, or exercised exit. Replace has no candidate evidence.

Existing routes are preserved: deployment [OI-001](../../controls/open-items.md#oi-001), tolerance [OI-002](../../controls/open-items.md#oi-002), representative failure [OI-003](../../controls/open-items.md#oi-003), migration/recovery [OI-004](../../controls/open-items.md#oi-004), provenance [OI-005](../../controls/open-items.md#oi-005), functional acceptance [OI-006](../../controls/open-items.md#oi-006), journey requirement [OI-007](../../controls/open-items.md#oi-007), and governance [OI-008](../../controls/open-items.md#oi-008). New source-correction and accountability routes are [OI-014](../../controls/open-items.md#oi-014) and [OI-015](../../controls/open-items.md#oi-015).

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| Run is not continuity-ready until coordinated PostgreSQL/ClickHouse/persistent-file backup, irreversible/non-atomic migration handling, RPO/RTO, and a dated non-production restore are evidenced. The image volume and migration/rollback commands are mechanisms, not recovery proof. | High | M | [E-003](../../evidence/evidence-ledger.md#e-003), [E-005](../../evidence/evidence-ledger.md#e-005), [E-038](../../evidence/evidence-ledger.md#e-038), [recovery view](../../controls/continuity/recovery-and-control-view.md), [OI-004](../../controls/open-items.md#oi-004) | High confidence in source boundaries; deployed topology and any external CE procedures are unavailable. No claim that a library backup failed. | A failed upgrade, datastore corruption, or operator loss could make collection or historical reporting unrecoverable or inconsistent across stores. | project-defined continuity/recovery control |
| Required monthly email delivery can fail without a retryable Oban failure: the job permits one attempt, the mailer catches exceptions, and the worker ignores the returned error. Separately, the session-buffer metric samples the event buffer again. | Medium | S | [E-035](../../evidence/evidence-ledger.md#e-035), [E-036](../../evidence/evidence-ledger.md#e-036), [OI-014](../../controls/open-items.md#oi-014) | High source confidence; no live missed report or alert was observed, and dashboard/API/CSV can provide alternate outputs if governed. | A monthly report can be silently missed, and session-buffer pressure can be misrepresented during incident diagnosis. | project-defined observability/report-delivery control |
| In the reviewed source, site deletion records pending ClickHouse work, but the cleanup worker's weekly cron entry is cloud-only rather than part of self-host cron. | Medium | S | [E-037](../../evidence/evidence-ledger.md#e-037), [OI-008](../../controls/open-items.md#oi-008) | High confidence in the approved repository; the separate CE deployment source is outside scope and may invoke the worker independently. No retained library data is claimed. | Run can leave analytics deletion incomplete unless external automation or an operator invokes and verifies cleanup, weakening retention/exit governance. | project-defined data-lifecycle continuity control |
| Source-visible application ownership transfer does not establish transferable operation: library owners/successors for infrastructure, datastores, backups, secrets, observability, SaaS administration, billing, support, or exit are unknown. | High | M | [E-039](../../evidence/evidence-ledger.md#e-039), [access/ownership view](../../controls/continuity/access-and-ownership-view.md), [OI-015](../../controls/open-items.md#oi-015) | High confidence that mechanisms exist and effective library ownership was unavailable by design. | Departure or loss of one person/account can delay patching, recovery, procurement, data export, or access restoration even if the application itself is healthy. | project-defined control-transfer control |
| Subscribe shifts infrastructure operation to Plausible, but current detailed backup/restore/on-call claims are post-cutoff public assertions, while cutoff-effective standard terms do not guarantee uninterrupted/error-free service and offer reasonable-effort email support. | Medium | M | [E-030](../../evidence/evidence-ledger.md#e-030), [E-039](../../evidence/evidence-ledger.md#e-039), [vendor view](../../controls/continuity/vendor-control-view.md), [OI-015](../../controls/open-items.md#oi-015) | High confidence in evidence classification; no contract, SLA, control report, support case, hosted system, or independent test was approved. | Procurement could transfer work without obtaining the recovery, escalation, termination, and data-portability outcomes the library needs. | none |

## Mandate-Relevant Strengths

- Readiness checks both data stores and critical caches; Oban persists job state in PostgreSQL and defines orphan rescue, pruning, and queue/cron controls ([E-035](../../evidence/evidence-ledger.md#e-035), [E-036](../../evidence/evidence-ledger.md#e-036)).
- The application attempts buffer flush on orderly termination and has an optional session-cache takeover path, giving Run concrete restart mechanisms to validate rather than design from nothing ([E-035](../../evidence/evidence-ledger.md#e-035)).
- Cross-store up-migration ordering is explicit, and the release includes commands to inspect pending work and request rollback; the visible irreversible boundary prevents a responsible reviewer from treating rollback as universally safe ([E-038](../../evidence/evidence-ledger.md#e-038)).
- Product roles, sole-owner safeguards, ownership transfer, CSV/API export, and hosted account-transfer documentation provide useful building blocks for succession and exit ([E-039](../../evidence/evidence-ledger.md#e-039)).
- Hosted public material describes daily encrypted backups, quarterly restore tests, continuity/DR review, and on-call monitoring. These are useful procurement claims to verify, not control-effectiveness evidence ([E-030](../../evidence/evidence-ledger.md#e-030)).

### Decision Insights

1. **Run is an operational-capability decision, not merely an infrastructure-cost decision.** Dual authorities, interwoven/irreversible migration history, buffered acknowledgement, background jobs, and external services create multiple recovery modes. A wrong assumption can lose measurement or historical access. Close [OI-002](../../controls/open-items.md#oi-002)–[OI-004](../../controls/open-items.md#oi-004) and [OI-015](../../controls/open-items.md#oi-015) before calling Run dependable.
2. **Subscribe reduces owned infrastructure but does not eliminate continuity ownership.** The library still controls staff roles, instrumentation, billing, procurement, escalation, export, and termination. Standard public terms provide no availability guarantee. Obtain option-specific assurance and name successors through [OI-015](../../controls/open-items.md#oi-015).
3. **Monthly reporting needs a controlled delivery outcome independent of option marketing.** The source-visible email path can mask delivery failure. Correct it or approve a reconciled API/CSV reporting route through [OI-014](../../controls/open-items.md#oi-014) before accepting the requirement.
4. **Deletion must be tested as an end-to-end continuity path.** A source-visible pending marker is useful, but CE scheduling differs and backup expiry is unknown. Use [OI-008](../../controls/open-items.md#oi-008) to validate pending-to-ClickHouse-to-backup completion for the selected option.
5. **Replace cannot be credited with better continuity without a candidate.** Carry the recovery, ownership, service-commitment, reporting, deletion, portability, and exit criteria into any later selection rather than treating unknown as safer.

## Selected Outputs

- [Recovery and operations evidence packet](../../evidence/packets/recovery-and-operations.md)
- [Environment and service continuity view](../../controls/continuity/environment-and-service-view.md)
- [Recovery and control view](../../controls/continuity/recovery-and-control-view.md)
- [Access and ownership continuity view](../../controls/continuity/access-and-ownership-view.md)
- [Vendor control and exit view](../../controls/continuity/vendor-control-view.md)
- [Expiry and maintenance continuity view](../../controls/continuity/expiry-and-maintenance-view.md)

The observability-and-response-path diagram was not triggered: approved source defines optional telemetry and health mechanisms, but no approved dashboard, alert, owner, incident, or live response evidence satisfies the card's live-evidence trigger.

Exactly one independent artifact-quality review returned `PASS`. One final revision recorded that terminal outcome; no material correction was requested or left unresolved.

## Material Omissions, Unknowns, And Auditor Questions

The material auditor question remains [OI-002](../../controls/open-items.md#oi-002): **What maximum event-loss window and dashboard/reporting outage are acceptable during high-demand library services?** The auditor resumed work without supplying a threshold, so no acceptance target is inferred. [OI-007](../../controls/open-items.md#oi-007) also remains unanswered, and [OI-008](../../controls/open-items.md#oi-008) remains an authority decision.

Proof-only needs are routed to the deployed inventory, failure exercise, restore evidence, artifact provenance, functional acceptance, deletion verification, source corrections, and responsibility matrix. Documented outside audited scope; not independently verified: the separate Community Edition deployment repository and library procedures are the smallest useful expansion for Run installation/backup/upgrade/rollback controls. Hosted internal controls and negotiated terms require procurement/assurance evidence. No replacement candidate was approved.

## Reconciliation

Architecture's dual-store, buffered-ingestion, Oban, configuration, and cross-store migration boundaries are retained. E-038 sharpens OI-004: the visible rollback command is not interwoven and reviewed history includes an irreversible, potentially non-atomic ClickHouse migration. Code Quality's green exact-commit result and source checks remain provenance evidence, not recovery proof; OI-005 stays open.

Security/Privacy and Application Security open items OI-009 through OI-013 remain open without duplication. OI-008 is expanded with option-specific deletion completion. The earlier security flow correctly identified pending deletion plus a cleanup worker, but E-037 adds an edition boundary: the worker's source cron entry is cloud-only, so CE invocation remains outside-scope/unknown. OI-010/OI-012 diagnostic risks make telemetry configuration a security as well as continuity decision; this review does not reopen their source analysis.

Product Value's monthly-email mechanism is retained, while E-036 distinguishes successful content generation from delivery recovery. No material conflict was found between cutoff-effective hosted terms and post-cutoff hosted security claims: the former defines no uninterrupted-service guarantee; the latter supplies current control assertions that still require verification. The bounded recovery collector completed once and its evidence was reconciled; no collector remained open.

## Bounded Conclusion And Downstream Guidance

Plausible has meaningful continuity building blocks, but the available evidence does not establish dependable library operation. Run is viable only conditionally on explicit loss/outage tolerances, deployed inventory/provenance, coordinated dual-store backup/restore and upgrade controls, observable reports/deletion/queues, and successor ownership. Subscribe can reduce the library's technical operations burden, but must pass procurement/assurance for recovery, escalation, terms, account succession, deletion, and export/exit. Replace cannot yet be compared.

Maintenance Cost should price the Run proof/control set and the source-visible OI-014 corrections without assuming hosted equivalence. Contributor and Vendor Value should use the vendor/exit and ownership views without treating public claims as effective controls. Expense and Cloud Security may use the option responsibility boundary, but must not assume that a mechanism, public statement, health check, backup schedule, or runbook proves recovery.
