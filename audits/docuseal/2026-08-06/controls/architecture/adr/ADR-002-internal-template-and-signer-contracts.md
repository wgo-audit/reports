# ADR-002: Internal Template And Signer Contracts

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

Template and signer state crosses Rails serializers, ERB data attributes, generic Vue objects, controller parameter allow-lists and API serializers without one evidenced versioned schema. Submissions conditionally snapshot template JSON and otherwise read current template state.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Parallel implicit payload definitions; conditional snapshot/fallback | [Component packet §3–5](../../../evidence/packets/architecture-component-api-ui-contracts.md) | No runtime compatibility test inspected |
| Runtime/live state | unknown | No approved traffic or consumer evidence | Existing consumers may impose undocumented constraints |
| Rationale | unknown | No decision record found | Conditional behavior's intent is unproved |
| Approval | unknown | No target compatibility authority supplied | Implemented behavior is not organization acceptance |

## Constraints, Options, And Tradeoffs

Direct shared hashes reduce adapter code but make compatible evolution dependent on synchronized edits. A versioned canonical schema with validation/generated adapters adds discipline; an organization integration adapter can contain vendor drift without changing upstream code.

## Impacts And Boundaries

In-flight submissions can follow different effective template state. Web/mobile and API consumers must not infer backward compatibility from successful current rendering.

## Change, Reversal, And Follow-Up

OI-005 should obtain a release/edition contract and require compatibility tests for selected flows. Product Value must define which in-flight submission behavior is acceptable.

