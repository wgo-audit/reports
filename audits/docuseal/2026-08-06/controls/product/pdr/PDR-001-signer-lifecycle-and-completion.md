# PDR-001: Signer Lifecycle And Completion

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03

## Decision Statement

DocuSeal models signing as template/submission/submitter records reached through public signer links, with validation and signer events preceding per-signer and overall submission completion; result/audit generation and notifications finalize asynchronously.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | Multi-party, mobile-optimized signing is promised. | `README.md:25-47` | Promise is not demonstration. |
| Implementation | Guards, validation, completion, jobs, outputs, emails, and webhooks are implemented. | PV-E-001 | Failure/runtime behavior unobserved. |
| Runtime/demonstration | unknown | No approved golden path | No device/browser fixture. |
| Approval/specialist sign-off | unknown | Audit brief | Customer and legal acceptance absent. |

## Constraints, Options, And Tradeoffs

The source supports ordered or parallel parties and multiple output channels. This gives workflow flexibility but separates business completion from async artifact readiness.

## Impacts And Boundaries

The repository is a credible evaluation foundation for the core flow. It does not establish production readiness, legal validity, or web/mobile acceptance.

## Change, Reversal, And Follow-Up

Define the authoritative completion/readiness state, partial-document policy, and acceptance matrix; then run controlled actor/device/failure fixtures.
