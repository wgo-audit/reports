# PDR-001: Event Collection Contract

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

Plausible accepts pageviews and named custom events from a browser tracker or Events API. Payloads may include URL, domain, referrer, properties, and interactivity. A 202 response can mean buffered or non-validation-dropped; it is not a stored-event receipt.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Tracker/API support pageviews and custom events; drop debugging uses a response header. | [E-016](../../../evidence/evidence-ledger.md#e-016), [E-020](../../../evidence/evidence-ledger.md#e-020) | Public page is post-cutoff validation. |
| Implementation | Tracker builds/sends payloads; server validates, filters, buffers, and returns 202/400 as coded. | [E-004](../../../evidence/evidence-ledger.md#e-004), [E-016](../../../evidence/evidence-ledger.md#e-016) | No deployed proxy/script configuration. |
| Runtime/demonstration | unknown | [OI-003](../../open-items.md#oi-003), [OI-006](../../open-items.md#oi-006) | No golden-path or failure reconciliation. |
| Approval/specialist sign-off | unknown | [OI-006](../../open-items.md#oi-006) | No library acceptance or privacy sign-off. |

## Constraints, Options, And Tradeoffs

Client transformation/exclusion gives integration control but can suppress events. Server validation and filtering reduce unsuitable traffic but 202 is deliberately not a durable receipt. Search/registration instrumentation therefore needs a controlled event dictionary plus downstream reconciliation.

## Impacts And Boundaries

This contract supports custom service measurement in principle. It does not establish event completeness, deployment equivalence, acceptable loss, or visitor-data governance.

## Change, Reversal, And Follow-Up

Validate one representative search/registration fixture through [OI-006](../../open-items.md#oi-006) and failure behavior through [OI-003](../../open-items.md#oi-003) after [OI-002](../../open-items.md#oi-002) is decided.
