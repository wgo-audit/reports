# PDR-007: Monthly Email Summary

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

Editors, admins, and owners can schedule a monthly email for the previous calendar month in site timezone. Source constructs a fixed summary of pageviews, visitors, bounce rate, and up to five pages, sources, and goals, sends it to configured recipients, and gives the worker one attempt.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Current documentation describes first-of-month embedded email reports and multiple recipients. | [E-022](../../../evidence/evidence-ledger.md#e-022) | Post-cutoff validation only. |
| Implementation | PostgreSQL report settings, scheduler, query assembly, recipient loop, and mail worker are present. | [E-019](../../../evidence/evidence-ledger.md#e-019) | Mail configuration/delivery unverified. |
| Runtime/demonstration | unknown | [OI-006](../../open-items.md#oi-006) | No delivered sample or reconciliation. |
| Approval/specialist sign-off | unknown | [OI-006](../../open-items.md#oi-006) | Recipient and content governance unknown. |

## Constraints, Options, And Tradeoffs

The summary directly supports lightweight monthly awareness but is not a configurable formal report, PDF, or attachment. Recipients are independent of dashboard membership, and single-attempt delivery raises a continuity dependency.

## Impacts And Boundaries

Monthly reporting is functionally present but should not be marked accepted until content, delivery, and recipient governance are validated.

## Change, Reversal, And Follow-Up

Validate a prior-month fixture, delivery, recipients, and content through [OI-006](../../open-items.md#oi-006); define outage tolerance in [OI-002](../../open-items.md#oi-002).
