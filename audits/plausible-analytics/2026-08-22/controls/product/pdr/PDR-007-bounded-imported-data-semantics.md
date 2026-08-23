# PDR-007: Bounded Imported-Data Semantics

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

Observed product position (not evidence of approval): GA/CSV imports extend historical analysis as aggregate data with explicit exclusions and query warnings rather than pretending to be equivalent to native events.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Import guides state count differences and missing revenue, exit, scroll, and other dimensions. | [E-026](../../../evidence/evidence-ledger.md#e-026) | No customer acceptance. |
| Implementation | Import workflow caps completed imports and query outputs carry imported-data warnings/skip reasons. | [E-026](../../../evidence/evidence-ledger.md#e-026) | CE cleanup defect can destroy imported data. |
| Runtime/demonstration | unknown | [OI-006](../../open-items.md#oi-006), [OI-008](../../open-items.md#oi-008) | No live import/reconciliation. |
| Approval/specialist sign-off | unknown | [provenance](../provenance-notes.md) | No data migration owner record. |

## Constraints, Options, And Tradeoffs

Aggregate imports enable migration/history with lower ingestion complexity but cannot reproduce native-event analysis. Honest warnings reduce misinterpretation.

## Impacts And Boundaries

Imported and native results can differ by definition; full native export excludes imported data. The destructive cleanup path in [OI-006](../../open-items.md#oi-006) is a material exception.

## Change, Reversal, And Follow-Up

Fix/reconcile import cleanup, then demonstrate a representative import and warning/output matrix.
