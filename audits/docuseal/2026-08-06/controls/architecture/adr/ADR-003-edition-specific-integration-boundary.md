# ADR-003: Edition-Specific Integration Boundary

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

The pinned Community source exposes some API and webhook implementation, while checked-in OpenAPI documentation targets hosted servers and includes Pro-classified paths. External embedding is Pro/external code and Community serves upgrade placeholders; extension hooks permit unavailable code to alter topology.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Community routes/serializers differ from hosted/OpenAPI and external embed surfaces | [Component packet §6, §8, §10](../../../evidence/packets/architecture-component-api-ui-contracts.md) | Pro implementation is out of scope |
| Runtime/live state | unknown | No Pro or target environment | Entitlement and compatibility untested |
| Rationale | unknown | Public/README edition statements are not architecture rationale | Packaging may change |
| Approval | unknown | Community-versus-Pro decision not made | Vendor and authority input required |

## Constraints, Options, And Tradeoffs

The target web/mobile onboarding requirement cannot be bound safely to a generic “DocuSeal API.” Options are a versioned Pro contract, a bounded Community subset if licensed/fit, or an organization-owned adapter with explicit package and endpoint compatibility.

## Impacts And Boundaries

Wrong edition assumptions can invalidate capability, licensing, support and security conclusions. This is a decision dependency, not a defect finding about unavailable Pro code.

## Change, Reversal, And Follow-Up

OI-001 and OI-005 require a release-specific edition matrix, Pro component map, package provenance, support/deprecation commitments and authority decision before target design freezes.
