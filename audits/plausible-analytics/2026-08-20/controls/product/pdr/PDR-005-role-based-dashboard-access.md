# PDR-005: Role-Based Dashboard Access

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

Team and guest memberships separate dashboard viewing from site-setting and membership administration. Viewer/guest-viewer can read assigned dashboards; editor-or-higher can change measurement settings; admin/owner govern broader membership. CE compiles unlimited application site/member limits.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Current public role documentation describes team and per-site guest roles. | [E-021](../../../evidence/evidence-ledger.md#e-021) | Post-cutoff validation only. |
| Implementation | Membership schemas, role resolution, authorization plugs, settings routes, and CE limits implement the separation. | [E-018](../../../evidence/evidence-ledger.md#e-018) | No library assignments or hosted plan. |
| Runtime/demonstration | unknown | [OI-006](../../open-items.md#oi-006) | No role test identities. |
| Approval/specialist sign-off | unknown | [OI-006](../../open-items.md#oi-006) | Least-privilege matrix/offboarding not approved. |

## Constraints, Options, And Tradeoffs

The source can represent 25 staff across 18 sites without an application limit in CE. Hosted limits are plan-driven. Editor access includes goal/report/shared-link settings, so "dashboard access" and "measurement administration" require separate assignment decisions.

## Impacts And Boundaries

This supports the role-restriction need in principle. It does not prove assignments, authentication controls, offboarding, or hosted capacity.

## Change, Reversal, And Follow-Up

Define and exercise the library role matrix through [OI-006](../../open-items.md#oi-006).
