# PDR-008: Project-Scoped Governance

- Status: observed
- Evidence cutoff: 2026-08-19

## Decision Statement

Projects scope checks, integrations, API keys, and teams. Roles are Owner, Manager,
Team Member, and Read-only; members can modify monitoring and view/regenerate project
API keys, managers also administer membership, and read-only members cannot modify.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Separate project teams and roles are documented. | [E-019](../../../evidence/evidence-ledger.md#E-019) | Hosted/SSO behavior not observed. |
| Implementation | Project records bind checks/channels/keys; detailed security behavior belongs to Security and Privacy. | [E-006](../../../evidence/evidence-ledger.md#E-006), [E-019](../../../evidence/evidence-ledger.md#E-019) | Not all identity code re-reviewed here. |
| Runtime/demonstration | unknown | [OI-004](../../open-items.md#OI-004) | No identity test. |
| Approval/specialist sign-off | unknown | [audit brief](../../../audit-brief.md) | Acme owner/access model absent. |

## Constraints, Options, And Tradeoffs

Project scoping supports separation, but ordinary members retain broad monitor and API-key
control. Operational actionability also needs named responders beyond account roles.

## Impacts And Boundaries

Pull/make require Acme identity and ownership design; buy needs vendor/control review.
Product roles alone do not prove least privilege, access review, or on-call accountability.

## Change, Reversal, And Follow-Up

Map projects to environments/ownership and validate access before production. Security
and Privacy owns detailed control conclusions; OI-009 owns responder/job mapping.
