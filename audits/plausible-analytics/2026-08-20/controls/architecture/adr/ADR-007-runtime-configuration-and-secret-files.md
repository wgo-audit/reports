# ADR-007: Runtime Configuration And Secret Files

- Status: observed
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto

## Decision Statement

Runtime settings and secret values can be read from environment variables or files under a configurable secret directory, while optional integrations expand the dependency boundary when enabled.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | Source validates required base/key material and configures databases, mail, geolocation, telemetry, S3, and other integrations conditionally. | [E-006](../../../evidence/evidence-ledger.md#e-006) | No secret values were accessed or recorded. |
| Runtime/live state | unknown | [OI-001](../../../controls/open-items.md#oi-001) | Provider, rotation, access, and enabled set unknown. |
| Rationale | Environment/file lookup supports container secret mounting and portable deployment. | [E-006](../../../evidence/evidence-ledger.md#e-006) | Rationale is inferred from mechanism. |
| Approval | unknown | [OI-001](../../../controls/open-items.md#oi-001) | No governance/ownership evidence. |

## Constraints, Options, And Tradeoffs

Flexible injection avoids source-embedded credentials but does not itself establish least privilege, rotation, encryption, ownership, or safe defaults. Optional dependencies create additional failure and data-flow boundaries.

## Impacts And Boundaries

Run requires an explicit inventory of configured integrations and secret ownership. Subscribe changes this boundary but cannot be inferred from CE source.

## Change, Reversal, And Follow-Up

Capture only redacted keys, providers, owners, rotation dates, and dependency endpoints through [OI-001](../../../controls/open-items.md#oi-001); Security/Privacy and Cloud Security own control evaluation.
