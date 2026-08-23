# PDR-004: Trend And Export Outputs

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

Plausible exposes interactive historical/realtime dashboard queries with filters, date ranges, comparisons, and breakdowns, plus ZIP/CSV and authenticated Stats API outputs.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Dashboard, trend comparisons, CSV, and API reporting are documented. | [E-015](../../../evidence/evidence-ledger.md#e-015), [E-022](../../../evidence/evidence-ledger.md#e-022) | Public page is post-cutoff validation. |
| Implementation | Query builder maps date/filter/comparison state to metrics; dashboard export and public Stats API routes are present. | [E-017](../../../evidence/evidence-ledger.md#e-017), [E-019](../../../evidence/evidence-ledger.md#e-019) | Deployed version, correctness, and hosted entitlement unknown. |
| Runtime/demonstration | unknown | [OI-006](../../open-items.md#oi-006) | No output reconciliation. |
| Approval/specialist sign-off | unknown | [OI-006](../../open-items.md#oi-006) | No accepted monthly-report format. |

## Constraints, Options, And Tradeoffs

Dashboard and API/CSV can support reusable monthly reporting beyond the fixed email. They add API-key, query-definition, and reconciliation work; CE raw ClickHouse access adds flexibility but bypasses a stable product contract.

## Impacts And Boundaries

The source covers monthly and seasonal visitor trends. It does not prove performance at assumed scale, metric acceptance, or compatibility with existing library reporting workflows.

## Change, Reversal, And Follow-Up

Reconcile one representative month across dashboard, CSV, and API in [OI-006](../../open-items.md#oi-006); Scalability assesses performance.
