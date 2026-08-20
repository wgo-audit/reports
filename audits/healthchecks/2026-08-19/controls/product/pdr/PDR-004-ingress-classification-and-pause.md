# PDR-004: Ingress Classification And Pause

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

Checks may require POST and classify HTTP/email content with case-sensitive precedence
failure, success, then start. Unmatched input is ignored or failed by configuration.
Sticky pause ignores all pings until explicit resume.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Method/filter and sticky-pause controls are documented. | [E-016](../../../evidence/evidence-ledger.md#E-016) | No approved Acme rules. |
| Implementation | Ping ingestion assigns `fail`, `success`, `start`, or `ign` before state mutation. | [E-016](../../../evidence/evidence-ledger.md#E-016) | Runtime behavior unobserved. |
| Runtime/demonstration | unknown | [OI-009](../../open-items.md#OI-009) | No fixture. |
| Approval/specialist sign-off | unknown | [audit brief](../../../audit-brief.md) | Operator acceptance absent. |

## Constraints, Options, And Tradeoffs

Filtering supports clients that cannot choose distinct URLs, but case-sensitive keyword
configuration can misclassify. Sticky pause prevents accidental resume but can suppress
monitoring indefinitely.

## Impacts And Boundaries

An HTTP 200 can correspond to an ignored ping, so response status is not proof of a
state transition. Preview-bot protection depends on requiring POST and identifier hygiene.

## Change, Reversal, And Follow-Up

Default to explicit endpoint signals for critical jobs where possible. OI-009 must test
negative/unmatched cases, pause/resume, and event/status output.
