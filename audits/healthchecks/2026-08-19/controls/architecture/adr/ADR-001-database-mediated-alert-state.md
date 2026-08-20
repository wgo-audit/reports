# ADR-001: Database-Mediated Monitoring And Alert State

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

The source uses relational `Check`, `Ping`, and `Flip` records as the durable
monitoring state and handoff between ping ingestion and notification delivery.
`sendalerts` detects overdue checks and claims a `Flip` by setting its
`processed` timestamp before submitting channel delivery.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | HTTP and SMTP ingress update a locked `Check`, persist `Ping`, and create `Flip`; `sendalerts` polls and claims flips. | [E-002](../../../evidence/evidence-ledger.md#E-002), [E-003](../../../evidence/evidence-ledger.md#E-003), [alert-path diagram](../diagrams/heartbeat-to-human-alert-path.md) | Code proves control flow, not production execution. |
| Runtime/live state | unknown | [OI-006](../../open-items.md#OI-006) | No deployed database, worker, provider, queue-depth, or latency evidence was approved. |
| Rationale | unknown. As an implementation consequence, the transaction and row lock serialize concurrent updates, and conditional flip claiming avoids two workers successfully claiming the same row. | `HC-CODE-001:hc/api/models.py:503-510,651-671`; `HC-CODE-001:hc/api/management/commands/sendalerts.py:105-120` | These consequences are inferred from implementation; they are not evidence of an approved design rationale. Repository history available in the temporary clone was shallow. |
| Approval | unknown | [audit brief](../../../audit-brief.md) | Acme has not selected or approved a deployment. |

## Constraints, Options, And Tradeoffs

- The relational database is both monitoring-state authority and work-handoff
  dependency; database unavailability affects ingestion, timeout detection, and
  alert processing.
- The two-second polling loop is compatible with a five-minute target in the
  no-failure path, but the target also includes grace, queueing, channel
  delivery, and human routing.
- Marking a flip processed before delivery prevents duplicate worker claims but
  creates at-most-once behavior at the flip handoff. Channel errors are recorded;
  the reviewed source does not return the flip to an unprocessed state.
- The default is one notification worker. A flip's channels are called
  sequentially, and an HTTP channel may consume three 30-second attempts. This
  simplifies concurrency but permits queue delay under provider degradation or
  simultaneous misses.

The audit's measurement contract is: `T0` is the first instant a critical job
is late against its Acme-approved expected-completion schedule; `T1` is the
first instant a responsible human receives enough job identity, failure context,
and response routing to act. A required fault case passes only when
`T1 - T0 <= 300 seconds` and no alert is silently lost. Healthchecks grace,
polling, queueing, provider delivery, and escalation consume that same budget.

## Impacts And Boundaries

This architecture is central to pull, make, and hosted comparison. Pull can be
acceptable only if deployment controls, worker supervision, channel diversity,
and an independent watchdog close the failure paths. Make becomes relevant only
if measured requirements cannot be met operationally and a durable delivery
queue/redelivery change is justified. Public source cannot establish hosted
service runtime internals.

## Change, Reversal, And Follow-Up

Do not change the upstream state machine based on source review alone. First
complete [OI-006](../../open-items.md#OI-006) against the selected topology and
channels. If tests show the five-minute boundary cannot survive required fault
cases, document a proposed queue/redelivery design and its idempotency and
upgrade implications before choosing make. Self-hosting is stopped until the
measurement contract passes; buy requires equivalent vendor evidence or an
Acme-controlled end-to-end test.
