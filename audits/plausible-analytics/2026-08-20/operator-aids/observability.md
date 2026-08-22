# Observability And Response Guide

- Status: untested
- Selected precursor: [capacity and degradation view](../controls/scalability/capacity-envelope-and-degradation-view.md), [recovery and control view](../controls/continuity/recovery-and-control-view.md), and [OI-014/OI-019](../controls/open-items.md#oi-014)

## Purpose And Evidence Boundary

Operator question: How should the library detect, interpret, and route loss of measurement or reporting before relying on Plausible during normal and high-demand periods?

This guide defines an untested signal and response framework. It does not enable telemetry, expose an endpoint, set a threshold, inspect traffic, or prove alert delivery. No live dashboard, metric, log, alert rule, recipient, incident, workload, or service objective was inspected. The assumed annual traffic does not establish peak demand, and source telemetry does not establish that Run or Subscribe is observable in operation.

## Existing Runbook And Coverage

No applicable alert-response or observability runbook was found in the approved catalog or source. `primary-code:lib/plausible_web/controllers/api/system_controller.ex:21-92` defines liveness and readiness checks; readiness probes PostgreSQL, ClickHouse, critical caches, and whether session takeover was attempted. `primary-code:config/runtime.exs:977-1028` configures conditional OpenTelemetry/BEAM export and disables PromEx by default. `primary-code:lib/plausible/telemetry/plausible_metrics.ex:1-260` defines ingestion, cache, buffer, session-transfer, and deletion signals. `primary-code:lib/workers/send_email_report.ex:1-54` and `primary-code:lib/plausible/mailer.ex:1-21` show why monthly email needs independent reconciliation. These mechanisms do not define library thresholds, alert routing, ownership, or incident response.

## Authority And Preconditions

Library IT/operations owns Run telemetry wiring and response; Digital Services owns measurement/report acceptance; security/privacy approves diagnostic content and access; continuity approves incident severity and recovery escalation. For Subscribe, the SaaS owner and procurement/vendor contact own vendor notices and escalation while the library retains usage/report reconciliation.

Before configuring or testing anything, record:

- exact option, environment, signal source, collection destination, retention, access, and primary/successor owner;
- approved event-loss and reporting-outage thresholds from [OI-002](../controls/open-items.md#oi-002);
- approved data/diagnostic contract from [OI-008](../controls/open-items.md#oi-008), including mitigations for [OI-010](../controls/open-items.md#oi-010) and [OI-012](../controls/open-items.md#oi-012);
- exact Run topology and telemetry configuration under [OI-001](../controls/open-items.md#oi-001), or hosted service/notice/support boundary under [OI-015](../controls/open-items.md#oi-015); and
- a representative non-production demand and degradation scenario under [OI-019](../controls/open-items.md#oi-019).

Until those decisions exist, thresholds, recipients, and escalation times are `UNKNOWN`.

## Procedure And Stop Conditions

1. **Build an outcome-first signal register.** Map every signal to one library outcome and owner:

   | Outcome | Minimum evidence to design and validate | Known limitation |
   |---|---|---|
   | Event collection | requests accepted/dropped/failed, event and session buffer depth, ClickHouse ingest errors, accepted-versus-stored synthetic count | HTTP 202 and liveness do not prove durability |
   | Staff reporting | representative dashboard/API/CSV query success and latency; PostgreSQL/ClickHouse readiness | readiness is narrower than useful reporting |
   | Monthly report | scheduled job, queue age/state, query completion, delivery result, recipient reconciliation | source permits one attempt and can swallow mail failure |
   | Jobs and lifecycle | Oban backlog/age/failure, deletion pending/completion, export state | enabled queues, CE deletion schedule, and alerting are unknown |
   | Capacity and integrity | queue/pool wait, buffer depth, query timeouts, storage/parts/headroom, replica/session reconciliation | no safe numeric envelope exists |
   | Hosted continuity | billable usage/quota, service notices, support case, dashboard/report availability | quota and public claims are not an SLA or capacity proof |

2. **Define severity from approved consequences.** Use the OI-002 loss/outage decisions and OI-019 operating envelope. Separate collection degradation, report unavailability, data-integrity mismatch, security/privacy diagnostic exposure, and commercial quota/lock conditions. Do not invent numeric thresholds from source defaults.
3. **Design least-data collection.** Restrict metrics/logs to operational fields; exclude visitor IP/User-Agent, URLs/query strings, referrers, custom properties, OAuth parameters, API secrets, recovery codes, and payload bodies. Protect metrics endpoints and diagnostic destinations by role.
4. **Define the response path.** For each signal, name primary/successor recipients, acknowledgement target, first read-only checks, evidence to capture, decision authority, vendor escalation where applicable, and when to invoke the [recovery guide](recovery.md). Preserve accepted-versus-stored and report-output reconciliation as independent checks.
5. **Validate in non-production only after separate approval.** Exercise one alert per outcome, including datastore unavailability, event-buffer or queue pressure, monthly mail failure, report-query failure, deletion/export backlog, and hosted escalation simulation where contractually permitted. Confirm correct recipient, timing, evidence, data minimization, and clear recovery route.
6. **Establish the operating calendar.** Apply the provisional cadence in the [care envelope](../controls/maintenance/time-to-safety-and-care-envelope.md#recurring-activity-and-proposed-cadence) only as a hypothesis: normal review, first-of-month reporting, seasonal active watch, release/renewal review, and periodic successor checks. Revise it from the OI-020 activity log.
7. **Review after change or incident.** Update the signal register, thresholds, owners, and links when the topology, instrumentation, reporting path, retention, roles, vendor terms, or service objective changes.

Stop if a telemetry change could expose a public or unprotected endpoint; sensitive visitor, credential, or callback data appears; the signal has no named response owner; a test could touch production/live traffic; a source default is being promoted to an acceptance threshold; or a health check conflicts with synthetic outcome evidence. Preserve the inconsistency and escalate.

## Expected Evidence And Records

Retain a versioned signal register with outcome, source, query/metric/log name, data classification, environment, owner/successor, threshold authority, severity, response link, retention, and last validation. For each authorized test or incident, retain timestamps, synthetic fixture identifier, alert delivery/acknowledgement, read-only observations, accepted-versus-stored or output reconciliation, escalation, disposition, and residual owner. Store no secrets or visitor payloads.

This aid becomes `executed-successfully` only when a canonical, authorized validation proves alert delivery and response for every required outcome. Source metrics, an exporter configuration, or a green health endpoint alone are insufficient.

## Escalation, Recovery, And Unknowns

Escalate measurement mismatch or report failure to Digital Services and Library IT under OI-003/OI-006/OI-014; capacity/session/storage degradation under OI-019; sensitive diagnostics under OI-010/OI-012; and hosted notice, quota, outage, or support gaps under OI-015/OI-017. Invoke the recovery guide when the approved consequence threshold is crossed or data authorities may be inconsistent.

Live signals, dashboards, alert rules, thresholds, recipients, response times, incident history, metrics protection, hosted internal monitoring, and the true peak operating envelope are `UNKNOWN`.
