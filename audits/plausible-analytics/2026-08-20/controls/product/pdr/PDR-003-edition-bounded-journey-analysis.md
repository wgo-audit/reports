# PDR-003: Edition-Bounded Journey Analysis

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

CE provides discrete goals, conversion reporting, and session-level behavioral filters, but ordered funnels and user-journey exploration are compiled only for EE and are publicly listed among hosted premium capabilities unavailable in CE.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | README distinguishes hosted funnels from CE; targeted history says the comparison was aligned with the website. | [E-015](../../../evidence/evidence-ledger.md#e-015) | Hosted entitlement and current commercial terms unknown. |
| Implementation | Funnel/exploration routes and journey output are inside EE build branches; goal/behavioral query paths are outside them. | [E-017](../../../evidence/evidence-ledger.md#e-017) | Exact deployed CE version unknown. |
| Runtime/demonstration | unknown | [OI-006](../../open-items.md#oi-006) | No hosted or CE journey demonstration. |
| Approval/specialist sign-off | Library acceptance threshold is unknown. | [OI-007](../../open-items.md#oi-007) | Decision owner must define sufficient journey measurement. |

## Constraints, Options, And Tradeoffs

Run can report stage goals and filtered cohorts without extra subscription dependency, but cannot supply the in-product ordered step/path experience from assessed source. Subscribe may supply it, subject to plan and service validation. Replace remains unevaluated.

## Impacts And Boundaries

This is the largest functional discriminator among current options. Calling discrete stage totals a complete journey would overstate Run fit if drop-off order/path is required.

## Change, Reversal, And Follow-Up

Resolve [OI-007](../../open-items.md#oi-007), then test only the accepted workflow through [OI-006](../../open-items.md#oi-006).
