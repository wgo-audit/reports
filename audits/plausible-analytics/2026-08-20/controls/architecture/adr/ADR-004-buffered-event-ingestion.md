# ADR-004: Buffered Event Ingestion

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

The reviewed embedded ingestion path validates and sessionizes an event, casts event/session rows to in-process buffers, and returns HTTP 202 before the reviewed ClickHouse write completes.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Buffers flush on configured size/timer thresholds and on orderly termination. | [E-004](../../../evidence/evidence-ledger.md#e-004) | Remote/relay backend may differ; live backend unknown. |
| Runtime/live state | unknown | [OI-001](../../../controls/open-items.md#oi-001), [OI-003](../../../controls/open-items.md#oi-003) | No failure exercise or live telemetry. |
| Rationale | Batching is consistent with efficient ClickHouse ingestion; no formal rationale record was found. | [E-004](../../../evidence/evidence-ledger.md#e-004) | Inference is source-bounded, not approval. |
| Approval | unknown | [OI-002](../../../controls/open-items.md#oi-002) | Acceptable loss/outage tolerance is unset. |

## Constraints, Options, And Tradeoffs

The design reduces per-event database overhead and lets requests return promptly. It also creates an acknowledged-but-not-yet-durable interval: orderly shutdown tries to flush, while abrupt process/host loss may lose unflushed rows. No magnitude is claimed.

## Impacts And Boundaries

This boundary materially affects completeness of programme-registration and seasonal reporting. It is not proof that production data has been lost.

## Change, Reversal, And Follow-Up

Set the tolerance in [OI-002](../../../controls/open-items.md#oi-002), identify the live backend/configuration in [OI-001](../../../controls/open-items.md#oi-001), and validate representative failure behavior in [OI-003](../../../controls/open-items.md#oi-003).
