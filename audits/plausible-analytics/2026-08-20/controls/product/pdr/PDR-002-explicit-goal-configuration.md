# PDR-002: Explicit Goal Configuration

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

A received event becomes a named conversion only through site-level goal configuration. Source supports pageview, custom-event, and scroll goals, optional goal properties, and goal outputs for visitors, events, and conversion rate.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Goals turn selected actions into conversion reports. | [E-015](../../../evidence/evidence-ledger.md#e-015), [E-017](../../../evidence/evidence-ledger.md#e-017) | Public/customer acceptance unknown. |
| Implementation | Goal records persist in PostgreSQL; editor-or-higher may configure them; unconfigured recent events are suggestions, not conversions. | [E-017](../../../evidence/evidence-ledger.md#e-017), [E-018](../../../evidence/evidence-ledger.md#e-018) | Deployed goals unknown. |
| Runtime/demonstration | unknown | [OI-006](../../open-items.md#oi-006) | No configured fixture. |
| Approval/specialist sign-off | unknown | [OI-006](../../open-items.md#oi-006) | Metric definitions not approved by library. |

## Constraints, Options, And Tradeoffs

Explicit configuration makes conversions understandable and editable, but creates an administration dependency: event receipt alone is insufficient. Custom-property constraints require a deliberate, privacy-reviewed event dictionary.

## Impacts And Boundaries

Discrete search and registration stages can be measured as goals. This does not provide ordered path/drop-off analysis or prove that the resulting metric answers the library's service question.

## Change, Reversal, And Follow-Up

Define representative event names/properties and acceptance examples, then reconcile them through [OI-006](../../open-items.md#oi-006).
