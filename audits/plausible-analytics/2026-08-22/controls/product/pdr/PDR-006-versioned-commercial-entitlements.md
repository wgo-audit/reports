# PDR-006: Versioned Commercial Entitlements

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

Observed product position (not evidence of approval): commercial access is determined by versioned plan generations, central feature modules, team/site limits, enterprise overrides, and sustained-overage handling rather than by public price copy alone.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Starter/Growth/Business/Enterprise capabilities and overage grace are publicly described. | [E-025](../../../evidence/evidence-ledger.md#e-025) | Mutable page is not a customer contract. |
| Implementation | Plan files/benefits/features and quota logic broadly mirror the ladder; price is fetched from Paddle and custom plans exist. PRs #5392/#5426/#5489 show v5 creation and revision. | [E-025](../../../evidence/evidence-ledger.md#e-025), [E-033](../../../evidence/evidence-ledger.md#e-033) | Customer-specific result unknown. |
| Runtime/demonstration | unknown | [OI-009](../../open-items.md#oi-009) | No subscription/tenant sample. |
| Approval/specialist sign-off | unknown | [provenance](../provenance-notes.md) | Pricing/product authority not supplied. |

## Constraints, Options, And Tradeoffs

Grandfathering preserves customer expectations but increases plan-generation and support complexity. Central gates reduce ad hoc checks but must reconcile with Paddle/custom terms and public copy.

## Impacts And Boundaries

Misalignment can deny paid capability, expose unpaid capability, or make upgrades/overage enforcement surprising. Public list prices do not prove a tenant's price.

## Change, Reversal, And Follow-Up

Build and exercise the version/plan/edition/capability matrix under [OI-009](../../open-items.md#oi-009) before pricing migration or feature repackaging.
