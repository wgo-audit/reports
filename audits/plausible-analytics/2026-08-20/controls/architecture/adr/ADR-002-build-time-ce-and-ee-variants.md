# ADR-002: Build-Time CE And Hosted/Enterprise Variants

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

One monorepo produces CE and hosted/enterprise behaviors using compile-time macros/environments, supplemented by runtime self-host configuration.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | `on_ce`/`on_ee`, CE build environment, and a tagged CE image workflow create product/runtime variants. | [E-003](../../../evidence/evidence-ledger.md#e-003), [E-007](../../../evidence/evidence-ledger.md#e-007) | Workflow source does not prove published or deployed image. |
| Runtime/live state | unknown | [OI-001](../../../controls/open-items.md#oi-001) | Deployed digest/ref unavailable. |
| Rationale | Shared code supports both offerings; public project material distinguishes features and responsibilities. | [E-001](../../../evidence/evidence-ledger.md#e-001) | No formal choice record. |
| Approval | unknown | [OI-001](../../../controls/open-items.md#oi-001) | Library acceptance not evidenced. |

## Constraints, Options, And Tradeoffs

Shared code reduces duplication, while compile-time boundaries mean `master` is not a neutral proxy for a CE release. Feature, clustering, bot-filtering, and integration paths may differ by build.

## Impacts And Boundaries

Run must be assessed against the exact CE tag/image; Subscribe must be assessed against service evidence rather than assuming the CE build describes hosted runtime.

## Change, Reversal, And Follow-Up

Record the deployed digest and exact tag in [OI-001](../../../controls/open-items.md#oi-001). Review the separate CE deployment source through [OI-004](../../../controls/open-items.md#oi-004).
