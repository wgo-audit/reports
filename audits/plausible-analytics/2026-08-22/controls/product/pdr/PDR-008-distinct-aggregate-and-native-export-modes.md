# PDR-008: Distinct Aggregate And Native Export Modes

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

Observed product position (not evidence of approval): Plausible exposes quick aggregate CSV/ZIP reports and queued full native-data exports as separate workflows with different scope and limits.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Public guides distinguish quick CSV from full native export and disclose caps/exclusions. | [E-026](../../../evidence/evidence-ledger.md#e-026) | Scheduled raw delivery is separate and unverified. |
| Implementation | Dashboard export limits and queued S3/local export workers are visible. | [E-026](../../../evidence/evidence-ledger.md#e-026) | Completion/retrieval not observed. |
| Runtime/demonstration | unknown | [OI-014](../../open-items.md#oi-014) | No export executed. |
| Approval/specialist sign-off | unknown | [provenance](../provenance-notes.md) | Data lifecycle approval unknown. |

## Constraints, Options, And Tradeoffs

Quick exports optimize common reports with caps; full exports trade immediacy for broader native data. Imported aggregates are not part of the native-data export.

## Impacts And Boundaries

Customers must choose the mode based on scope and downstream needs. Scheduled Enterprise raw delivery must not be inferred from these workers.

## Change, Reversal, And Follow-Up

Verify queued native-export completion/security under [OI-014](../../open-items.md#oi-014). Independently close the scheduled raw-export promise under [OI-010](../../open-items.md#oi-010).
