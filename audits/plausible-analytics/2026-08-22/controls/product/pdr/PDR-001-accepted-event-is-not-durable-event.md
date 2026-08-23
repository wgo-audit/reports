# PDR-001: Accepted Event Is Not A Durable Event

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

Observed product position (not evidence of approval): the public Events API acknowledges accepted or policy-dropped work with HTTP `202`; that response does not mean the event is durably stored or will appear in statistics.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Documentation describes `202` and dropped-event cases; issue #1246/its fix made `ok` explicit and PR #2351 added drop-header semantics. | [E-021](../../../evidence/evidence-ledger.md#e-021), [E-032](../../../evidence/evidence-ledger.md#e-032) | Success-body example conflicts with visible `ok`. |
| Implementation | Controller returns `202` after build/buffer; persistence can be embedded, remote, or relay. | [E-002](../../../evidence/evidence-ledger.md#e-002), [E-003](../../../evidence/evidence-ledger.md#e-003) | ClickHouse completion is later. |
| Runtime/demonstration | unknown | [OI-001](../../open-items.md#oi-001) | No approved live event path. |
| Approval/specialist sign-off | unknown | [provenance](../provenance-notes.md) | Public source does not identify decision authority. |

## Constraints, Options, And Tradeoffs

Asynchronous acceptance favors low tracker latency and filtering tolerance, while moving loss/retry semantics behind the response boundary. Any change among preserving, strengthening, or delaying acknowledgment requires the live contract evidence routed through [OI-001](../../open-items.md#oi-001); this record does not recommend one without that proof.

## Impacts And Boundaries

Integrators must not treat `202` as query visibility. Analytics accuracy, retry strategy, and incident measurement depend on the unverified live persistor/SLO.

## Change, Reversal, And Follow-Up

Close [OI-001](../../open-items.md#oi-001) before changing acceptance semantics. Correct or explicitly version the response-body contract under [OI-012](../../open-items.md#oi-012).
