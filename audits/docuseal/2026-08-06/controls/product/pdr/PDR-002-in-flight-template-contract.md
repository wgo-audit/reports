# PDR-002: In-Flight Template Contract

- Status: observed
- Evidence cutoff: Community source effective 2026-08-03

## Decision Statement

Submission creation conditionally copies template fields/schema/submitters/variables into a submission; downstream reads can fall back to the current mutable template when a snapshot is absent.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | In-flight forms can follow copied or current template state. | E-012; architecture component packet section 5 | No public compatibility promise. |
| Implementation | Conditional copy/fallback is source-visible. | `create_from_submitters.rb:22-77,224-246`; `submission.rb:127-175` | Contract version is not explicit. |
| Runtime/demonstration | unknown | No fixture | Change-during-signing behavior not observed. |
| Approval/specialist sign-off | unknown | No rationale/approval record | Intent cannot be inferred. |

## Constraints, Options, And Tradeoffs

Fallback reduces duplication for simple flows but can couple in-flight submissions to later template edits. Full snapshot/version binding improves reproducibility at storage and migration cost.

## Impacts And Boundaries

Onboarding evidence may depend on the template state effective when each signer acts unless the organization enforces a snapshot/version rule.

## Change, Reversal, And Follow-Up

Adopt immutable/versioned in-flight contracts, migration semantics, and regression tests before production acceptance.
