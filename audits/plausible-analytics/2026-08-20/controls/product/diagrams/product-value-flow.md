# Product Value Flow

## Purpose And Evidence Boundary

- Reader question: How do library interactions become role-governed reports, and where are the decision boundaries?
- Evidence cutoff: 2026-08-20 at onboarding start, America/Toronto.
- Confirmed notation: solid arrows/nodes are source-implemented.
- Inferred notation: dotted arrows labelled `option inference` are bounded comparisons, not observed operation.
- Unknown notation: dotted nodes/edges labelled `unknown` require validation.
- Evidence links: [E-004](../../../evidence/evidence-ledger.md#e-004), [E-016](../../../evidence/evidence-ledger.md#e-016), [E-017](../../../evidence/evidence-ledger.md#e-017), [E-018](../../../evidence/evidence-ledger.md#e-018), [E-019](../../../evidence/evidence-ledger.md#e-019).

## Evidence Dimensions Used

Implementation and source-documented promises are present. Runtime demonstration, deployment, library approval, specialist sign-off, cost, and hosted operation are unknown.

## Diagram

```mermaid
flowchart TB
  LIB["Unknown library instrumentation across 18 assumed properties"] -. "unknown: OI-006" .-> ENTRY
  subgraph ENTRY["Confirmed collection interfaces"]
    direction LR
    TRACKER["Browser tracker"] --> PAYLOAD["Pageview or named event + properties"]
    API["Events API"] --> PAYLOAD
  end
  subgraph PROCESS["Confirmed source processing"]
    direction LR
    VALIDATE["Request validation / filtering"] --> BUFFER["In-process event/session buffers"] --> CH["ClickHouse analytics"]
    GOAL["PostgreSQL goal configuration"] --> QUERY["Stats query semantics"]
    CH --> QUERY
  end
  subgraph OUTPUT["Confirmed output surfaces"]
    direction LR
    DASH["Dashboard trends / goal reports"] --> CSV["ZIP / CSV"]
    STATSAPI["Authenticated Stats API"]
    EMAIL["Fixed prior-month email summary"]
  end
  subgraph ACCESS["Confirmed access modes"]
    direction LR
    RBAC["Owner / admin / editor / viewer / guest"]
    SHARE["Optional public or shared-link view"]
    RECIPIENT["Configured email recipients"]
  end
  ENTRY --> PROCESS --> OUTPUT --> ACCESS
  CE["CE: discrete goals; no ordered funnel/journey endpoints"] -. "option inference" .-> OUTPUT
  HOSTED["Hosted: EE journey source; entitlement/live service unknown"] -. "unknown: OI-007 / OI-006" .-> OUTPUT
```

## Known Gaps And Follow-Up

HTTP 202 is not durability proof ([OI-002](../../open-items.md#oi-002), [OI-003](../../open-items.md#oi-003)). The exact deployed flow and outputs require [OI-001](../../open-items.md#oi-001) and [OI-006](../../open-items.md#oi-006). Whether CE's discrete goals are sufficient for a "journey" requires [OI-007](../../open-items.md#oi-007).
