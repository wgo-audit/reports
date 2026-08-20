# Technical Lead Notes

The audit-work API-equivalent cost closeout is [Final](controls/cost-estimate.md)
at `$103.02` displayed. It is an API-equivalent audit-execution estimate, not a
technical product cost estimate.

## Current Technical Position

Pursue a minimal hosted pilot first, retain a source-pinned pull design as the
fallback/exit path, and do not fork. No deployment is approved. The technical
acceptance contract is option-independent: per-job correctness, `T0` to
actionable-human `T1` at or below 300 seconds with no silent loss, an independent
watchdog/route, RTO 30 minutes, RPO 5 minutes, account/successor continuity,
capacity margin, and accountable change authority.

Upstream source quality is useful: the pinned commit had 22,750 successful
hosted test executions, strict mypy, and three successful CodeQL jobs. Local
tests, coverage, and mypy could not start because dependencies were absent;
Ruff found two lint findings and five files that its unpinned version would
reformat. Branch/ruleset enforcement was not established. Upstream green is an
input to, not a substitute for, Acme promotion.

## Architecture, Operations, Quality, And Security Findings

| Finding | Severity | Effort | Taxonomy | Technical consequence |
|---|---|---|---|---|
| Flip state is marked processed before asynchronous delivery; durable redelivery after channel failure was not found. | High | Large | none | Worker death or provider failure can silently lose the actionable alert. |
| Five-minute delivery is unproven with one default worker, sequential channels, up to three 30-second HTTP attempts, bursts, and one-hour deferral after due-check calculation failure. | High | Large | none | Queue or fault behavior can exceed 300 seconds by construction in stress cases. |
| Per-job heartbeat capability UUIDs are bearer secrets and not independently rotatable; project ping keys/slugs expand blast radius. | High | Medium | CWE-798/CWE-522 boundary | Leaked paths can forge or suppress monitor state; recreate/migrate is required after UUID disclosure. |
| The reference self-host topology is not a production design and its health probe does not cover alert-worker delivery. | High | Large | none | Shared host/database/worker failure can disable both monitoring and notification. |
| No Acme immutable promotion, recovery/rollback, capacity, or change-authority gate exists. | High | Large | none | A green upstream release can enter production without job, alert, restore, or rollback acceptance. |
| Ping ingress reads request bodies and writes relational state; same-check events serialize, while no ping-route limiter was found. | Medium | Medium | CWE-400 | Burst, overlap, or abuse can consume web/database capacity. |
| Stored payloads and integration values span DB, logs, backups, providers, and optional object storage without an approved lifecycle. | High | Medium | CWE-200/CWE-312 boundary | Diagnostic convenience can create sensitive-data and credential exposure. |
| Make adds fork merge, security response, release, documentation, provenance, and successor obligations without an evidenced source need. | High | Large | none | It increases change risk and feature opportunity cost over 36 months. |

For pull, require a durable managed database or equivalent proven design,
separately supervised web and alert workers, TLS/edge controls, no direct app
ingress, secret management, encrypted/restricted backups, immutable images,
pre-migration backups, restore/rollback rehearsal, cleanup, telemetry, and an
external watchdog. Do not enable shell execution. Treat ordinary read/write
project membership as privileged because members can manage keys/integrations.

For buy, minimize metadata and payloads before review; use unique per-job
capabilities and preferably an Acme-scoped relay; validate MFA/account recovery,
processors, retention/deletion, incident and availability commitments, quotas,
service-change handling, export, and exit. Vendor operation does not replace
Acme's independent alert path or change acceptance.

## Safe Evolution Priorities

1. Freeze make under OI-017. Define OI-022 authority and the selected option's
   immutable decision record before accepting changes.
2. Define a small critical-job contract set under OI-009, including Windows
   service account, exit-code propagation, concurrency, history, and secret
   handling where applicable.
3. Implement the independent watchdog and fault suite under OI-006. Exercise
   worker death, database interruption, slow/failing providers, bursts, quota
   exhaustion, and absent expected alerts.
4. For buy, close OI-004/OI-012/OI-015/OI-016 before the decision gate. For
   pull, close OI-005/OI-007/OI-008/OI-010 in addition.
5. Measure production-shaped capacity and opportunity time under OI-014/OI-018;
   the preliminary CPU, RAM, disk, setup-day, and monthly-hour figures are not
   planning evidence.
6. Preserve closure-to-learning under OI-023: failed tests, incidents, and
   changes must update the relevant test, runbook, claim, or control.

## Traceability And Limits

Primary technical routes are the [architecture report](reviewer-reports/architecture/report.md),
[alert path](controls/architecture/diagrams/heartbeat-to-human-alert-path.md),
[security boundary](controls/security/identity-secret-and-data-boundaries.md),
[recovery control](controls/continuity/recovery-and-rollback-control.md),
[capacity envelope](controls/scalability/capacity-envelope.md),
[quality control](controls/quality/test-health-and-change-safety.md), and
[release/change control](controls/project-health/release-change-control.md).

No Acme topology, live service, load result, provider quota, backup, identity
configuration, contract, job set, or operator coverage was inspected. Tests
reported here are upstream hosted evidence or reviewer-tool checks, not a live
Acme acceptance run. Exact team ability and sustainable effort remain unknown.
