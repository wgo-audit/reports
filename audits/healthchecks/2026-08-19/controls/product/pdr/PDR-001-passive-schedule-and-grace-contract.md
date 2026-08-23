# PDR-001: Passive Schedule And Grace Contract

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

A Healthchecks check is a passive dead-man's switch. Simple schedules expect the
next success after the configured period; Cron and OnCalendar schedules expect it at
a wall-clock expression in a configured timezone. The check becomes Late at the
expected boundary and Down only after grace.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | New, Up, Late, Down, and Paused are the visible lifecycle. | [E-014](../../../evidence/evidence-ledger.md#E-014) | Documentation is not demonstration. |
| Implementation | `get_grace_start`, `going_down_after`, and `get_status` implement the schedule/grace transition. | [E-014](../../../evidence/evidence-ledger.md#E-014) | Clock and database operation unknown. |
| Runtime/demonstration | unknown | [OI-006](../../open-items.md#OI-006) | No safe environment or fixture. |
| Approval/specialist sign-off | Acme approves only the 300-second outcome, not concrete schedules/grace. | [audit brief](../../../audit-brief.md) | Job values unknown. |

## Constraints, Options, And Tradeoffs

Grace absorbs expected run-time variance but directly consumes the five-minute alert
budget. The 60-second form minimum leaves theoretical delivery time; source cannot
prove the remaining path fits.

## Impacts And Boundaries

This fits known-schedule jobs, not uptime probing, metrics, or business-result
validation. A success ping at the wrong point can produce false assurance.

## Change, Reversal, And Follow-Up

Keep the upstream rule for pull. Change it in a fork only after OI-006/OI-009 show a
server-side deficiency. Record and test each critical schedule, timezone, and grace
under [OI-009](../../open-items.md#OI-009).
