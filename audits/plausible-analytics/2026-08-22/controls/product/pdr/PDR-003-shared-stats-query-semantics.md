# PDR-003: Shared Statistics Query Semantics

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

Observed product position (not evidence of approval): dashboard and public Stats API requests converge on shared query construction/result semantics, including explicit warnings or skip reasons where comparisons, revenue, or imported data constrain interpretation.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Stats API documents metrics, dimensions, filters, imports, limits, and heuristic variance. | [E-022](../../../evidence/evidence-ledger.md#e-022) | Documentation is not acceptance evidence. |
| Implementation | Dashboard/controller/API use shared query types/builders/runner/result metadata. | [E-022](../../../evidence/evidence-ledger.md#e-022) | v1 invalid-page path remains defective. |
| Runtime/demonstration | unknown | [OI-008](../../open-items.md#oi-008) | No live cross-surface comparison. |
| Approval/specialist sign-off | unknown | [provenance](../provenance-notes.md) | No product owner record. |

## Constraints, Options, And Tradeoffs

Shared semantics reduce dashboard/API drift, but complex filters, imported aggregates, rate limits, and table/heuristic selection create qualified rather than absolute equality.

## Impacts And Boundaries

API clients need warning/meta handling and versioned error behavior. Fix the known invalid `page` path under [OI-007](../../open-items.md#oi-007).

## Change, Reversal, And Follow-Up

Any API version or query-engine change should run cross-surface contract tests and preserve or explicitly supersede documented warning semantics.
