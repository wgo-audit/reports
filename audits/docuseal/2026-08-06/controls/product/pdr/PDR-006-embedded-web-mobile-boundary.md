# PDR-006: Embedded Web And Mobile Boundary

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03; public pages post-cutoff validation

## Decision Statement

External embedded signing/form-builder components are Pro/external dependencies; the Community `/js` endpoint serves upgrade placeholders and does not prove the external component contract or mobile behavior.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Public docs/guides show JS frameworks and iOS WebView flows. | PV-E-005 | Hosted/API examples and dynamic content. |
| Implementation | Community embed script is a placeholder; internal Vue signer UI is a separate surface. | PV-E-003; E-012 | External repositories/Pro code out of scope. |
| Runtime/demonstration | unknown | No package/device test | Accessibility, callbacks, token handling unknown. |
| Approval/specialist sign-off | unknown | OI-001/OI-005 | Product/security acceptance absent. |

## Constraints, Options, And Tradeoffs

Direct vendor embed may accelerate delivery but introduces external package, token, browser/WebView, version, and commercial dependencies. Hosting the Community signer link avoids the external component but changes experience and integration requirements.

## Impacts And Boundaries

The mandated web/mobile onboarding path is not established by Community source alone.

## Change, Reversal, And Follow-Up

Request pinned component provenance/support/device/accessibility/security contracts and run controlled web/iOS/Android success/failure/upgrade tests.
