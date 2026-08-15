# PDR-003: Community Operator Access

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03

## Decision Statement

Community enables only the `admin` operator role, and the Community `Ability` grants broad management across account templates, submissions, users, configuration, tokens, and webhooks.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | User management is Community; additional roles are Pro. | `README.md:43,49-56`; role-select UI | Public wording does not prove target fit. |
| Implementation | One role constant and broad abilities. | PV-E-002 | Pro authorization implementation unknown. |
| Runtime/demonstration | unknown | No target identity/live users | Configuration/effectiveness unobserved. |
| Approval/specialist sign-off | unknown | OI-001/OI-003 context | Least-privilege acceptance absent. |

## Constraints, Options, And Tradeoffs

Single-role administration is simple but cannot express granular product/operations/security role separation. Whether separation or compensating controls are adequate is an organization/CISO decision; the stated workload scale is unknown.

## Impacts And Boundaries

Community source alone does not demonstrate adequate operator access control for KYC and identity data. This is an edition/target requirement, not evidence that unavailable Pro roles fail.

## Change, Reversal, And Follow-Up

Define the operator-role matrix, select Community compensating controls or Pro, and validate privilege boundaries with CISO approval.
