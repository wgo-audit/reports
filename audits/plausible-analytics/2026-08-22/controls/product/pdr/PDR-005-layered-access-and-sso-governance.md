# PDR-005: Layered Access And SSO Governance

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

Observed product position (not evidence of approval): collaboration uses three distinct access layers—team/site roles, constrained public links, and enterprise SAML policy.

| Access layer | Consumer and boundary | Distinct failure mode | Closure |
|---|---|---|---|
| Team/site roles | Authenticated members and guests; permissions vary by role and site/team scope | Role transition or site-isolation error | [OI-013](../../open-items.md#oi-013) |
| Shared links | Unauthenticated recipient; optional password and segment limit | Link leakage or constraint bypass | [OI-013](../../open-items.md#oi-013) |
| Enterprise SSO | IdP/JIT/session/force policy; owners retain recovery access | IdP/session failure, wrong default role, or recovery lockout | [OI-013](../../open-items.md#oi-013) |

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Role, shared-link, and SSO documentation states permission and session rules. | [E-024](../../../evidence/evidence-ledger.md#e-024) | No tenant/IdP evidence. |
| Implementation | Roles, owner/admin checks, password/segment limits, SSO default role/timeout/force modes are visible. | [E-024](../../../evidence/evidence-ledger.md#e-024) | Deployed configuration unknown. |
| Runtime/demonstration | unknown | [OI-013](../../open-items.md#oi-013) | No safe identity/environment approved. |
| Approval/specialist sign-off | unknown | [provenance](../provenance-notes.md) | Security review was not supplied. |

## Constraints, Options, And Tradeoffs

Owner bypass supports recovery but is a deliberate exception to forced SSO. Public links improve sharing while relying on passwords/segments rather than account authentication.

## Impacts And Boundaries

Authorization correctness depends on role transitions, JIT mapping, session expiry, invitation state, and shared-link constraints across tiers.

## Change, Reversal, And Follow-Up

Close [OI-013](../../open-items.md#oi-013) before representing tenant access-control effectiveness.
