# PDR-004: Layered Conversion Analysis

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

Observed product position (not evidence of approval): conversion analysis builds from typed goals and custom events into revenue, funnels, and bounded user journeys, with capability gates applied to advanced layers.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Public guides describe page/event/scroll goals, revenue goals, funnels, and 20-step journeys. | [E-023](../../../evidence/evidence-ledger.md#e-023) | Customer adoption/acceptance unknown. |
| Implementation | Goal validation/caps, revenue matching, funnel ordering, and exploration bounds are visible. | [E-023](../../../evidence/evidence-ledger.md#e-023) | Output correctness not demonstrated. |
| Runtime/demonstration | unknown | [OI-008](../../open-items.md#oi-008) | No approved live tenant. |
| Approval/specialist sign-off | unknown | [PDR-006](PDR-006-versioned-commercial-entitlements.md) | Tier placement is observed, not approved here. |

## Constraints, Options, And Tradeoffs

Layering creates an understandable upgrade path while making goal configuration a prerequisite for valid revenue/funnel outputs. Limits bound query and configuration complexity.

## Impacts And Boundaries

Invalid revenue may be discarded without rejecting the event. Funnel order mode and journey direction materially affect interpretation.

## Change, Reversal, And Follow-Up

Preserve configuration prerequisites in documentation and contract tests; validate tier entitlements under [OI-009](../../open-items.md#oi-009).
