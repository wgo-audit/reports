# PDR-009: Windows Example Support Boundary

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

Healthchecks' repository documents generic PowerShell and C# HTTP requests, and its
ping endpoints are platform-neutral. Protocol compatibility is plausible, not
demonstrated, and the approved source does not define a production Windows Task
Scheduler monitoring contract.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | PowerShell documentation mentions Task Scheduler and sends a success ping; C# sends a timed GET. | [E-019](../../../evidence/evidence-ledger.md#E-019) | Basic examples only. |
| Implementation | Generic HTTP endpoints are present; the examples target them from PowerShell/C#. | [E-015](../../../evidence/evidence-ledger.md#E-015), [E-019](../../../evidence/evidence-ledger.md#E-019) | Protocol compatibility is plausible, not demonstrated. |
| Runtime/demonstration | unknown | [OI-009](../../open-items.md#OI-009) | No Windows fixture/host. |
| Approval/specialist sign-off | unknown | [audit brief](../../../audit-brief.md) | No Acme Windows owner. |

## Constraints, Options, And Tradeoffs

The basic PowerShell example does not propagate task exit status, send start/fail,
set timeout/retry, define overlap, protect endpoint secrets, or verify alerts.

## Impacts And Boundaries

Windows support is plausible at protocol level but insufficient for a critical-job claim.
This is an Acme client/operations gap unless testing isolates a server deficiency.

## Change, Reversal, And Follow-Up

Build and test a small standard wrapper plus Task Scheduler configuration under
[OI-009](../../open-items.md#OI-009). Do not fork solely to supply Windows procedure.
