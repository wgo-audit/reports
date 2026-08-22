# PDR-006: Alternate Dashboard Sharing

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

Dashboard data can be exposed outside membership RBAC by making a site public or creating a unique shared link. Shared links may be password-protected and segment-limited.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Public documentation says shared-link viewers need no account and see the selected dashboard. | [E-021](../../../evidence/evidence-ledger.md#e-021) | Post-cutoff validation only. |
| Implementation | Authorization resolves public/shared access; editor-or-higher manages shared links; password hashes and optional segment association persist. | [E-018](../../../evidence/evidence-ledger.md#e-018) | Live visibility state unknown. |
| Runtime/demonstration | unknown | [OI-006](../../open-items.md#oi-006) | No link/access test. |
| Approval/specialist sign-off | unknown | [OI-006](../../open-items.md#oi-006) | Governance policy absent. |

## Constraints, Options, And Tradeoffs

Sharing enables transparent or low-friction reporting, but is a separate access mode from role-restricted staff dashboards. Password protection and segment limits narrow exposure but are not proof of approved governance.

## Impacts And Boundaries

The library can disable this optional mode; the audit cannot establish whether it is enabled now.

## Change, Reversal, And Follow-Up

Inventory public/shared settings and validate intended policy through [OI-006](../../open-items.md#oi-006); Security and Privacy assesses control adequacy.
