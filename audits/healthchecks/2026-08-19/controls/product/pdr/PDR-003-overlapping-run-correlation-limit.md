# PDR-003: Overlapping Run Correlation Limit

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

Optional UUID run IDs correlate start/completion events for displayed durations, but
the check-level overrun timer retains only the most recent start. Healthchecks does not
alert on every concurrent run exceeding grace.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Docs explicitly warn that only the most recently started run is monitored for duration. | [E-015](../../../evidence/evidence-ledger.md#E-015) | Customer acceptance unknown. |
| Implementation | `last_start`/`last_start_rid` are single check fields; events retain per-ping RID and duration pairing. | [E-015](../../../evidence/evidence-ledger.md#E-015) | Tests were inspected, not locally run. |
| Runtime/demonstration | unknown | [OI-009](../../open-items.md#OI-009) | No overlapping workload observed. |
| Approval/specialist sign-off | unknown | [audit brief](../../../audit-brief.md) | Acme overlap policy unknown. |

## Constraints, Options, And Tradeoffs

RID gives useful history without creating one state machine per run. The tradeoff is
that an older hung run can be hidden by a later run completing within grace.

## Impacts And Boundaries

For jobs that prohibit overlap, scheduler-level mutual exclusion may make the limit
acceptable. For legitimate concurrent runs requiring per-run deadlines, one check is
not sufficient evidence of complete protection.

## Change, Reversal, And Follow-Up

OI-009 must classify each critical job as non-overlapping, overlap-tolerant, or needing
per-run monitoring. Use separate checks/external per-run control before considering a
fork; fork only if measured product need remains.
