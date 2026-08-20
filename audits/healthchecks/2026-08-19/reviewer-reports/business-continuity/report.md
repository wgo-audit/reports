# Business Continuity

## Audit Question, Depth, And Evidence Boundary

This detailed review asks whether Acme can continue, recover, and transfer
control of critical-job monitoring when a person, account, environment,
provider, vendor, or upstream maintainer disappears. It compares pull, make,
and buy against the five-minute actionable-human-alert mandate at
`HC-CODE-001` commit `fafac59eeb00cfdc87166242544fa071ecad1723` and cutoff
2026-08-19. Primary continuity evidence is
[E-027 through E-030](../../evidence/evidence-ledger.md); the selected control
views also cite directly linked, registered predecessor evidence where
relevant.

No approved evidence in the audit source set establishes an Acme runtime,
account or owner inventory, backup/restore control, on-call route, dashboard,
incident drill, billing record, vendor contract, or team-readiness control. No
service was deployed or mutated, no dependency was installed, and no live
recovery or delivery test was run. Public hosted material does not prove hosted
internal controls or historical availability.

## Coverage And Material Gaps

The review traced schedule-to-flip detection, worker claim and restart,
provider/human handoff, built-in health and metrics, database/object-store
state, migration/rollback, project ownership transfer, management-API exit
surface, license continuity, hosted status/terms, and time-bound maintenance.
The five triggered control views are linked below.

The dominant gap is not the absence of source mechanisms; it is the absence of
an independent and exercised continuity system. The built-in Docker probe
checks the web endpoint and database query, not alert-worker liveness, lost
post-claim delivery, provider outcome, or human receipt. Upstream explicitly
tells self-hosters to monitor ping acceptance and alert sending, but no such
Acme control is approved. Existing OI-005 and OI-006 retain this gate.

OI-007 already owns backup, restore, rollback, and recovery exercise. OI-004
owns hosted contract/control evidence; OI-011 owns capability and secret
lifecycle. New [OI-012](../../controls/open-items.md#OI-012) owns account and
control-transfer proof. New [OI-013](../../controls/open-items.md#OI-013) is a
decision-needed route for recovery time and data-loss tolerance.

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| The source can mark an alert flip processed before delivery completes; a crash or delivery fault has no source-observed durable flip requeue. The built-in healthcheck cannot detect that boundary. | Critical | M | [E-027](../../evidence/evidence-ledger.md#E-027), [environment/service view](../../controls/continuity/environment-and-service-continuity.md), [OI-006](../../controls/open-items.md#OI-006) | High for control flow; no live loss was observed | A critical job can be recorded down while no actionable alert reaches a human, directly violating the silent-failure guard and potentially the 300-second contract. | none |
| Pull and make have no approved backup/restore, cross-store reconciliation, migration rollback, or recovery exercise; the reference container applies migrations at startup. | High | M | [E-028](../../evidence/evidence-ledger.md#E-028), [recovery view](../../controls/continuity/recovery-and-rollback-control.md), [OI-007](../../controls/open-items.md#OI-007) | High for source/docs; Acme topology and stores unknown | A routine upgrade or store failure can disable the monitoring plane or lose configuration/history with no proved return path. | none |
| The image probe establishes only HTTP plus database connectivity. Worker liveness, aged work, alert-provider delivery, and responsible-human receipt remain outside it. | High | M | [E-027](../../evidence/evidence-ledger.md#E-027), [environment/service view](../../controls/continuity/environment-and-service-continuity.md), [OI-005](../../controls/open-items.md#OI-005) | High for probe scope; no deployment evidence | Monitoring can appear healthy while its reason for existence—timely actionable notification—is unavailable. | none |
| No Acme primary/deputy, break-glass access, account inventory, billing owner, or loss-of-owner transfer drill is evidenced. The supported project transfer requires current-owner initiation and recipient acceptance. | High | M | [E-029](../../evidence/evidence-ledger.md#E-029), [access/ownership view](../../controls/continuity/access-and-ownership-boundary.md), [OI-012](../../controls/open-items.md#OI-012) | High for source transfer workflow; all Acme ownership is unknown | Departure, illness, credential loss, or failed billing can strand administration or alert routing for any option. | none |
| Buy has public component status and current queue metrics, but standard terms disclaim uninterrupted/secure availability and no Acme SLA, support escalation, recovery, incident, or exit commitment was approved. | High | M | [E-026](../../evidence/evidence-ledger.md#E-026), [E-030](../../evidence/evidence-ledger.md#E-030), [vendor/transfer view](../../controls/continuity/vendor-and-transfer-control.md), [OI-004](../../controls/open-items.md#OI-004) | High for public statements/current snapshot; hosted internals and negotiated terms unknown | Buy can reduce Acme's infrastructure burden while leaving an unbounded core-vendor outage and recovery dependency. | none |
| Optional object storage creates a second recovery domain: large-body upload follows relational save, disabling S3 makes external bodies inaccessible, and no reverse-migration command is documented. | Medium | M | [E-028](../../evidence/evidence-ledger.md#E-028), [recovery view](../../controls/continuity/recovery-and-rollback-control.md) | High for source/docs; actual S3 use and payload criticality unknown | Restoring only the database can yield incomplete diagnostic context and inconsistent retention, complicating incident recovery. | none |
| BSD-3-Clause preserves the legal ability to operate or modify the source if upstream disappears, but no approved evidence proves Acme can rebuild, patch, merge, or succeed the maintainer. | Medium | M | [E-029](../../evidence/evidence-ledger.md#E-029), [vendor/transfer view](../../controls/continuity/vendor-and-transfer-control.md), [OI-002](../../controls/open-items.md#OI-002) | High for license; maintainer concentration and Acme skill coverage are not established here | Pull can remain pinned during upstream interruption; make immediately converts upstream continuity risk into an Acme staffing and release obligation. | none |
| Acme has not set monitoring-service RTO or acceptable configuration/event-data loss. | High | S | [recovery view](../../controls/continuity/recovery-and-rollback-control.md), [OI-013](../../controls/open-items.md#OI-013) | Confirmed evidence gap; the CTO answer is pending | Architecture, backup frequency, failover, and cost cannot be responsibly sized; an independent alert route is still required while service recovery is underway. | none |

## Mandate-Relevant Strengths

- Detection state, pending flips, project configuration, and notification
  records are relationally mediated, giving pull/make a coherent authoritative
  state boundary to back up and recover.
- The source exposes an authenticated metrics endpoint with backlog and latest
  event identifiers and emits per-channel success/failure, dwell, and send-time
  metrics. These are useful inputs to an external control, though no live
  receiver or alert rule was observed.
- Project ownership transfer is implemented and tested in source, reducing
  cooperative handoff friction when the current owner is available.
- BSD-3-Clause licensing permits source and binary redistribution and
  modification, reducing legal lock-in for pull/make.
- The hosted status page separates the Ping API, Notification Sender, Email
  Delivery, and Dashboard, which is more useful than one aggregate status. It
  remains vendor-controlled current-state evidence only.

### Decision Insights

1. **Continuity evidence favors pull before make.** The material gaps—worker
   supervision, independent alerting, recovery, ownership, and promotion—must
   be solved outside the application for both options. A fork does not close
   them and adds successor-maintainer duty. Smallest action: close OI-005..OI-013
   for the selected pull design, then fork only if a measured source-level
   defect remains.
2. **Buy changes the owner of runtime recovery; it does not remove continuity
   design.** Vendor operation may reduce Acme maintenance, but account/billing,
   producer secrets, provider routes, human escalation, independent watchdog,
   and exit remain Acme controls. Smallest proof: OI-004 vendor review plus the
   same OI-006 end-to-end fault test and OI-012 transfer drill.
3. **The five-minute alert objective requires a parallel control, not merely
   fast restore.** A monitor outage can outlast the alert budget even under a
   reasonable service RTO. Smallest action: set RTO/RPO through OI-013 and test
   an independent synthetic path that can alert while Healthchecks is impaired.

## Selected Outputs

- [Access and ownership boundary](../../controls/continuity/access-and-ownership-boundary.md)
- [Environment and service continuity](../../controls/continuity/environment-and-service-continuity.md)
- [Vendor and transfer control](../../controls/continuity/vendor-and-transfer-control.md)
- [Expiry and maintenance control](../../controls/continuity/expiry-and-maintenance-control.md)
- [Recovery and rollback control](../../controls/continuity/recovery-and-rollback-control.md)

The live-evidence observability and response diagram was not triggered because
no approved dashboard, alert, incident, or ownership evidence exists.

## Material Omissions, Unknowns, And Auditor Questions

No approved evidence establishes live backup success, restoration, rollback,
worker supervision, independent monitoring, provider delivery, human
acknowledgement, ownership, break-glass access, account recovery, billing
continuity, vendor recovery, or exit rehearsal.

Auditor question routed through [OI-013](../../controls/open-items.md#OI-013):
**After Healthchecks becomes unavailable, what is the maximum acceptable time
to restore monitoring service, and how much monitor configuration or event
history may be lost?** The answer changes topology, backup frequency,
failover, cost, and potentially the pull/make/buy recommendation.

## Executed Checks

Working directory for source checks: `HC-CODE-001:./`.

| Exact command | Intended coverage | Outcome | Dependency state and bounded conclusion |
|---|---|---|---|
| `git rev-parse HEAD; git rev-parse --is-shallow-repository` | Confirm source pin and history availability | Pass: pin matched; repository is shallow | No installation. Source is usable; local history cannot support maintainer-continuity claims. |
| `rg -n 'backup|restore|rollback|dump|loaddata' README.md docker templates/docs hc -g '*.md' -g '*.py'` | Locate recovery/export declarations | Pass: backup guidance and API examples found; no complete restore/rollback/export procedure found in the searched tree | Absence is bounded to the pinned approved tree. |
| `rg -n 'transfer_project|transfer.*project|new_owner|owner=' hc/accounts hc/front hc/api -g '*.py'` | Trace supported project control transfer | Pass: owner-initiation/member-acceptance flow located | Source behavior, not live account readiness or emergency recovery. |

No project tests were started for this review: 0 passed, 0 failed, 0 errors,
and 0 skipped. Dependency installation and live execution were outside the
approved boundary.

## Reconciliation

No material source conflict was found. Architecture's alert-path and recovery
gaps and Security/Privacy's account, secret, and hosted-evidence limits were
confirmed and retained. Existing OI-004..OI-011 keep their identifiers and
routes. OI-012 and OI-013 cover distinct transfer and decision gaps. The
recovery evidence collector completed once with no artifact writes. The
artifact-quality worker completed once with no artifact writes; its feedback
was applied in one revision. No child task remains running or ambiguously
terminated. The canonical structural validator passed with 0 errors and 0
warnings after the required handoff headings were added.

## Bounded Conclusion And Downstream Guidance

None of pull, make, or buy is continuity-approved on available evidence. Pull
is the least structurally burdensome self-host candidate if Acme proves an
external watchdog, five-minute human receipt, recoverability, and ownership.
Make is not continuity-justified without a source defect and accepted
successor-maintainer duty. Buy may reduce infrastructure recovery work but
remains stopped on vendor commitments, transfer/exit, and the same independent
alert outcome.

Expense Exposure may price the required controls; Contributor and Vendor Value
may assess upstream/vendor concentration; Maintenance Cost may estimate the
ongoing duties; Revenue Risk may model interruption. They must not assume
source guidance, public status, a backup declaration, or a transfer feature
proves live recovery, ownership, or five-minute alert continuity.
