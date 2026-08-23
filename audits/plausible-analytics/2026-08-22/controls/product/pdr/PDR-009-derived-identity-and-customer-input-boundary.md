# PDR-009: Derived Identity And Customer-Input Boundary

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

Observed product position (not evidence of approval): visitor identity and device/location attributes are derived from transient request data, while customer-provided URLs, referrers, custom properties, and revenue remain a separate data-classification boundary.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Data policy describes day/site/device-scoped identifiers and no stored raw IP/User-Agent. | [E-027](../../../evidence/evidence-ledger.md#e-027) | Policy wording is not legal sign-off. |
| Implementation | Ingestion derives geo/device/user ID and accepts bounded custom property values. History shows daily rotation later moved to ETS/GenServer and cross-node refresh while keeping two salts. | [E-027](../../../evidence/evidence-ledger.md#e-027), [E-031](../../../evidence/evidence-ledger.md#e-031) | Logs/caches/live schemas not inspected. |
| Runtime/demonstration | unknown | [OI-011](../../open-items.md#oi-011) | No production data inventory. |
| Approval/specialist sign-off | unknown | [OI-011](../../open-items.md#oi-011) | Privacy/legal review required. |

## Constraints, Options, And Tradeoffs

Derived identifiers reduce persistent cross-day identity, but useful custom dimensions and URLs can carry user-supplied sensitive content if integrations are not governed.

## Impacts And Boundaries

Source does not show that customers actually send personal data. Current/previous salt handling and `>48h` row deletion need reconciliation with public 24-hour wording.

## Change, Reversal, And Follow-Up

Close [OI-011](../../open-items.md#oi-011) with owner-reviewed semantics, deployed configuration, data inventory, deletion/retention tests, and customer-input guidance.
