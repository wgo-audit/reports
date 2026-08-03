# PDR-004: Link Lifecycle And Schedules

- Status: observed
- Evidence cutoff: July 22, 2026

## Decision Statement

Links can be permanent, ephemeral, expired, disabled, maintenance, or deactivated; expiry and routing state select user-facing status responses, while ordered timezone-aware schedules can temporarily replace a normal target and fall back when no rule matches.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Reference docs specify lifecycle states, HTTP outcomes, schedule syntax, precedence, fallback, and timezone behavior. | Link-format, schedules, and public-pages docs | Boundary cases not observed. |
| Implementation | Parser and Worker implement states, expiry, ordered schedule evaluation, timezone conversion, and status pages. | `scripts/lib/links-file.mjs`; `scripts/workers/worker.mjs` | No time-window test executed. |
| Runtime/demonstration | The public instance source contains one schedule example. | `v8s-link/custom/v8s-links.txt` | Deployment and target availability unknown. |
| Approval/specialist sign-off | Durable documented behavior exists. | [E-014](../../../evidence/evidence-ledger.md) | No product-owner acceptance record. |

## Constraints, Options, And Tradeoffs

Inline schedules keep history with links but clock/timezone behavior and ordered precedence increase semantic complexity. Static status pages are predictable but may require localization and operator customization.

## Impacts And Boundaries

Evolution must preserve state HTTP semantics and schedule precedence. Scalability owns runtime load; Business Continuity owns clock/provider and rollback consequences.

## Change, Reversal, And Follow-Up

Run transition tests across timezone and daylight-saving boundaries in an approved environment before altering semantics.
