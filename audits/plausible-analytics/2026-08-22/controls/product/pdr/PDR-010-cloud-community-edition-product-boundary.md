# PDR-010: Cloud And Community Edition Product Boundary

- Status: observed
- Evidence cutoff: 2026-08-22 22:08:28 EDT

## Decision Statement

Observed product position (not evidence of approval): Managed Cloud and Community Edition share a monorepo but visibly differ in operational responsibility, release/support cadence, data-hosting responsibility, and premium capability availability.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Product behavior/promise | README/public comparison assigns operations to Cloud or CE owner and excludes premium features from CE. | [E-028](../../../evidence/evidence-ledger.md#e-028) | CE support/viability not independently verified. |
| Implementation | Compile-time CE/EE paths and feature gates exist in one monorepo. | [E-011](../../../evidence/evidence-ledger.md#e-011) | Separate CE packaging repo excluded. |
| Runtime/demonstration | unknown | [OI-004](../../open-items.md#oi-004) | Neither edition was run. |
| Approval/specialist sign-off | Publicly documented; formal decision authority unknown. | [provenance](../provenance-notes.md) | No internal product record. |

## Constraints, Options, And Tradeoffs

Shared source supports reuse, while compile-time branches and distinct release/support promises expand the compatibility matrix and make edition-specific expectations explicit.

## Impacts And Boundaries

Cloud availability/backup/security claims cannot be transferred to CE. CE operational responsibility cannot be used to infer cloud control effectiveness.

## Change, Reversal, And Follow-Up

Quantify supported edition/feature/variant combinations under [OI-004](../../open-items.md#oi-004) before changing packaging or premium boundaries.
