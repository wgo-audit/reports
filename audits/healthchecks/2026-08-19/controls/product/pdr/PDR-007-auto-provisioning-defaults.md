# PDR-007: Auto-Provisioning Defaults

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

Slug pings with `create=1` can create a missing check and its first event. New checks
use a one-day period, one-hour grace, all integrations enabled, and may be created until
twice the account's normal check limit.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Dynamic clients can self-register; defaults are explicit. | [E-019](../../../evidence/evidence-ledger.md#E-019) | Hosted plan behavior unobserved. |
| Implementation | Slug ingestion creates, assigns all channels, and permits temporary 2x limit. | [E-019](../../../evidence/evidence-ledger.md#E-019) | Concurrency/cleanup unobserved. |
| Runtime/demonstration | unknown | [OI-009](../../open-items.md#OI-009) | No provisioning flow run. |
| Approval/specialist sign-off | unknown | [audit brief](../../../audit-brief.md) | No Acme monitor governance. |

## Constraints, Options, And Tradeoffs

Availability-first creation reduces missing-monitor risk, but defaults are unsuitable for
Acme's critical five-minute requirement and all-channel assignment can create noise.

## Impacts And Boundaries

Unreviewed auto-provisioned checks can exist yet offer false confidence for up to an
hour beyond expected completion. Temporary over-limit creation affects plan/capacity.

## Change, Reversal, And Follow-Up

Do not treat auto-provisioned checks as production-approved. Reconcile them immediately
through the Management API/configuration gate and OI-009, or pre-provision critical checks.
