# PDR-012: Signature Capture And Disclosure

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03

## Decision Statement

Signature fields can capture drawn, typed, camera/uploaded, or reusable signature images. A linked eSignature disclosure is conditional on `withDisclosure`, defaults false, and is not enabled by the Community submission partial.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Public pages describe signer consent/intent and legal effect. | PV-E-005 | Promise is not a Community acceptance record. |
| Implementation | Modalities and optional disclosure are source-visible; `complete_form` records completion interaction. | PV-E-007; PV-E-001 | No durable disclosure-acceptance record found. |
| Runtime/demonstration | unknown | No safe signer fixture | Accessibility, comprehension, modality, and correction unobserved. |
| Approval/specialist sign-off | unknown | Mandate reserves legal/KYC determination | Consent/intent/legal sufficiency cannot be inferred. |

## Constraints, Options, And Tradeoffs

Multiple capture modes improve accessibility and device fit, but their evidentiary meaning depends on an approved disclosure, intent, identity, correction, and audit contract.

## Impacts And Boundaries

A signature image and completion event are implemented evidence atoms, not proof by themselves of informed consent, intent, signer identity, or enforceability.

## Change, Reversal, And Follow-Up

Product/legal/compliance define required disclosure and intent evidence by transaction class; enable/implement durable acceptance evidence and test all supported modalities/devices.
