# Product Decision Candidate Inventory

## Coverage Domains

| Domain | Evidence boundary | Candidate count | Limitation/closure |
|---|---|---:|---|
| Maturity/demonstration | Pinned source, tests, and repository documentation | 2 | No safe environment, identity, fixture, or live job was supplied; demonstration remains under OI-009. |
| Users/workflows | Check setup, pinging guides, API routes, and client examples | 3 | Acme job inventory and actual clients are unknown. |
| Lifecycle | Check state, schedule/grace, pause, start/success/fail, and overlap rules | 4 | Runtime timing and job correctness are not demonstrated. |
| Configuration/persistence | Forms, model fields, auto-provisioning, payload/event storage | 3 | Acme-approved configuration and retention are unknown. |
| Outputs/provenance | Status, durations, events, logs, notifications, API representations | 3 | Stored pings prove receipt, not the monitored business result or human receipt. |
| Identity/governance | Project roles, API/ping identifiers, ownership transfer | 1 | Acme ownership, access review, and account configuration are unknown. |
| Specialist sign-off | No approved specialist sign-off evidence | 0 | Route job acceptance through OI-009 and security approval through OI-004. |
| External dependencies | Client network, notification providers, hosted service | 2 | Provider delivery and hosted runtime are not proven. |
| Public promises | Repository documentation for cron, Windows examples, notifications, and limits | 2 | Public hosted commitments were not established from local evidence. |
| Operator/admin acceptance | Source-supported configuration controls | 1 | No Acme operator acceptance or runbook exists. |

## Decision Candidates

| Candidate ID | Decision or durable behavior | Domain | Evidence | Observed/approved status | Disposition | Record or closure |
|---|---|---|---|---|---|---|
| PROD-DC-001 | One check is a passive dead-man's switch with New, Up, Late, Down, and Paused states. | Lifecycle | [E-014](../../evidence/evidence-ledger.md#E-014) | Observed in source/docs; approval unknown | record-created | [PDR-001](pdr/PDR-001-passive-schedule-and-grace-contract.md) |
| PROD-DC-002 | Simple schedules use last-success plus period; Cron/OnCalendar use wall-clock expression/timezone; grace delays Down/alert eligibility. | Configuration/lifecycle | [E-014](../../evidence/evidence-ledger.md#E-014) | Observed; Acme values unknown | merged-into | PDR-001; configure and prove under OI-009/OI-006. |
| PROD-DC-003 | UUID/slug endpoints accept success, start, fail, log, and numeric exit status; nonzero exit is failure. | Workflow/lifecycle | [E-015](../../evidence/evidence-ledger.md#E-015) | Observed; client use unknown | record-created | [PDR-002](pdr/PDR-002-execution-signal-contract.md) |
| PROD-DC-004 | Start-to-completion durations are displayable only for paired events under 72 hours, with optional UUID run IDs. | Output/provenance | [E-015](../../evidence/evidence-ledger.md#E-015) | Observed; runtime correctness unknown | record-created | [PDR-003](pdr/PDR-003-overlapping-run-correlation-limit.md) |
| PROD-DC-005 | Run IDs correlate displayed durations, but overrun alerting tracks only the most recently started concurrent run. | Lifecycle/output | [E-015](../../evidence/evidence-ledger.md#E-015) | Observed and explicitly documented; acceptance unknown | merged-into | PDR-003; choose an overlap policy under OI-009. |
| PROD-DC-006 | Content classification precedence is failure, success, start; unmatched input is ignored or failed by configuration. | Rules/configuration | [E-016](../../evidence/evidence-ledger.md#E-016) | Observed; keyword correctness unknown | record-created | [PDR-004](pdr/PDR-004-ingress-classification-and-pause.md) |
| PROD-DC-007 | Sticky pause causes all pings to be ignored until explicit resume; normal pause is cleared by a success/fail ping. | Lifecycle/governance | [E-016](../../evidence/evidence-ledger.md#E-016) | Observed; operator acceptance unknown | merged-into | PDR-004; include pause state in OI-009. |
| PROD-DC-008 | Down/up flips fan out to enabled project-scoped channels; documentation recommends multiple channels. | Output/dependency | [E-017](../../evidence/evidence-ledger.md#E-017) | Observed implementation/guidance; delivery unproven | record-created | [PDR-005](pdr/PDR-005-alert-routing-and-five-minute-budget.md) |
| PROD-DC-009 | A responsible human must receive an actionable alert within 300 seconds after a critical job misses expected completion. | Operator acceptance | [audit brief](../../audit-brief.md#business-concerns) | Approved Acme requirement; implementation unverified | merged-into | PDR-005 and OI-006. |
| PROD-DC-010 | POST payloads and `/log` events are retained as diagnostic outputs; `/log` does not change state. | Output/provenance | [E-018](../../evidence/evidence-ledger.md#E-018) | Observed; data acceptance unknown | record-created | [PDR-006](pdr/PDR-006-payload-and-event-provenance.md) |
| PROD-DC-011 | Slug auto-provisioning creates checks with one-day period, one-hour grace, all integrations enabled, and may exceed the nominal check limit to 2x. | Configuration/lifecycle | [E-019](../../evidence/evidence-ledger.md#E-019) | Observed; production acceptance unknown | record-created | [PDR-007](pdr/PDR-007-auto-provisioning-defaults.md) |
| PROD-DC-012 | Projects scope checks, integrations, API keys, and separate owner/member/manager/read-only access. | Identity/governance | [E-019](../../evidence/evidence-ledger.md#E-019) | Observed; Acme mapping unknown | record-created | [PDR-008](pdr/PDR-008-project-scoped-governance.md) |
| PROD-DC-013 | Windows is documented only through generic PowerShell/C# HTTP examples; platform-neutral endpoints make protocol compatibility plausible but not demonstrated. | Public promise/workflow | [E-015](../../evidence/evidence-ledger.md#E-015), [E-019](../../evidence/evidence-ledger.md#E-019) | Observed documentation boundary; operational fit unknown | record-created | [PDR-009](pdr/PDR-009-windows-example-support-boundary.md) |
| PROD-DC-014 | Pull and make expose the same source-backed product capabilities at the pinned commit; make changes capability only if a fork delta is approved. | Maturity/options | [E-014](../../evidence/evidence-ledger.md#E-014), [E-015](../../evidence/evidence-ledger.md#E-015), [Architecture report](../../reviewer-reports/architecture/report.md) | Observed baseline; no fork delta proposed | deferred | Make has no product-value justification until OI-006/OI-009 isolate a source-level deficiency. |
| PROD-DC-015 | Buy is expected to expose a similar workflow, but hosted feature parity, limits, controls, and service operation are not proven by the pinned repository. | External dependency/public promise | [E-019](../../evidence/evidence-ledger.md#E-019), [OI-004](../open-items.md#OI-004) | Unknown | blocked | Bounded hosted security/service and contract review under OI-004. |

The project is feature-rich rather than decision-poor: the inventory separates nine
durable, independently changeable product contracts from six merged, blocked, or
deferred decision edges. No candidate is based on a live demonstration.
