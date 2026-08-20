# PDR-002: Execution Signal Contract

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

UUID and slug ping URLs encode success by the base endpoint, start by `/start`,
failure by `/fail`, state-neutral logging by `/log`, and an exit result by
`/<exit-status>` where 0 succeeds and 1-255 fail.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Explicit start/fail/exit signals are optional enhancements to passive completion. | [E-015](../../../evidence/evidence-ledger.md#E-015) | Client correctness unknown. |
| Implementation | Routes normalize signals into `Check.ping`, which updates status, duration fields, event metadata, and flips. | [E-015](../../../evidence/evidence-ledger.md#E-015) | No endpoint was exercised. |
| Runtime/demonstration | unknown | [OI-009](../../open-items.md#OI-009) | No live job or fixture. |
| Approval/specialist sign-off | unknown | [audit brief](../../../audit-brief.md) | No job contract supplied. |

## Constraints, Options, And Tradeoffs

Success-only integration is simple but detects only absence. Explicit failure reduces
detection latency and start enables overrun timing, while increasing wrapper complexity.

## Impacts And Boundaries

The event represents what the client asserts. It does not independently validate the
job's business output, and a reporting call can fail separately from the job.

## Change, Reversal, And Follow-Up

Prefer explicit exit/failure only when Acme can preserve the actual task result and
avoid unconditional success. Validate wrappers and failed-reporting behavior through
[OI-009](../../open-items.md#OI-009); no fork is indicated.
