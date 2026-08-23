# ADR-003: Single-Source Tracker Variants

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

Web snippet, legacy, plugin-support, and NPM tracker targets compile from shared tracker source, with compile flags and site-specific configuration controlling behavior.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Shared source compiles many variants; payloads go to a configurable event endpoint and can be filtered/transformed client-side. | [E-002](../../../evidence/evidence-ledger.md#e-002) | Deployed variants across library properties unknown. |
| Runtime/live state | unknown | [OI-001](../../../controls/open-items.md#oi-001) | No website/runtime inspection approved. |
| Rationale | Documented goals include small size, shared maintenance, configurability, and legacy support. | [E-002](../../../evidence/evidence-ledger.md#e-002) | Does not prove library acceptance. |
| Approval | unknown | [OI-001](../../../controls/open-items.md#oi-001) | No implementation inventory or owner evidence. |

## Constraints, Options, And Tradeoffs

Shared source simplifies consistent change, but compiled variants and dynamic settings broaden the compatibility matrix. Client `keepalive` improves delivery opportunity but does not provide a durable delivery guarantee.

## Impacts And Boundaries

Search/registration measurement depends on consistent event names, properties, endpoints, and deployed tracker versions across 18 assumed properties ([E-002](../../../evidence/evidence-ledger.md#e-002)). The Product Value review should determine or route ownership of that measurement contract; source architecture does not establish organizational ownership.

## Change, Reversal, And Follow-Up

Inventory deployed snippets/NPM versions and proxy endpoints in [OI-001](../../../controls/open-items.md#oi-001); define event semantics with Product Value.
