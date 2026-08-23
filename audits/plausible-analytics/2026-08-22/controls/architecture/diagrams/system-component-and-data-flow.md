# System Component and Data Flow

## Purpose And Evidence Boundary

- Reader question: How do tracker/client, Phoenix, PostgreSQL, ClickHouse, and background work relate in the approved source?
- Evidence cutoff: 2026-08-22 22:08:28 EDT
- Confirmed notation: solid node/edge, directly observed in source
- Inferred notation: dotted edge labelled `inferred`
- Unknown notation: dotted boundary labelled `unknown`
- Evidence links: [E-001](../../../evidence/evidence-ledger.md#e-001), [E-002](../../../evidence/evidence-ledger.md#e-002), [E-004](../../../evidence/evidence-ledger.md#e-004), [E-006](../../../evidence/evidence-ledger.md#e-006), [E-008](../../../evidence/evidence-ledger.md#e-008), [E-009](../../../evidence/evidence-ledger.md#e-009)

## Evidence Dimensions Used

Implementation and selected history/rationale are present. Observed live operation, ownership/approval, commercial cost, and specialist assurance are unknown.

## Diagram

```mermaid
flowchart TB
  subgraph CLIENTS["Confirmed clients and contracts"]
    direction LR
    T["Compiled tracker variants"]
    EV["POST /api/event"]
    UI["Dashboard TypeScript"]
    PA["Public API clients"]
  end

  subgraph APP["Confirmed Phoenix/OTP application boundary"]
    direction LR
    EP["Phoenix endpoint/router"]
    ING["Request validation and enrichment"]
    IQ["Internal stats query contexts"]
    PQ["Public API contexts"]
    EP --> Q["Stats/query contexts"]
    EP --> AUTH["Auth, teams, billing, settings"]
    ING --> PER["Pluggable persistor"]
    JOB["Oban workers and cron"]
  end

  subgraph STATE["Confirmed source-level state boundaries"]
    direction LR
    PG["PostgreSQL: relational state + Oban"]
    CH["ClickHouse: events, sessions, imports, counters"]
    SC["ETS/session cache"]
    BUF["Local event/session write buffers"]
  end

  subgraph UNKNOWN["Unknown live boundary"]
    direction LR
    RP["Remote persistence service deployment"]
    TOPO["Cloud nodes, replicas, routing, ownership"]
  end

  T --> EV
  EV --> EP
  UI --> IQ
  IQ --> EP
  PA --> PQ
  PQ --> EP
  EP --> ING
  ING --> PER
  PER --> SC
  PER --> BUF
  BUF --> CH
  PER -. "remote backend path; deployment unknown" .-> RP
  RP -. "remote ClickHouse write path unknown" .-> CH
  Q --> CH
  Q --> PG
  AUTH --> PG
  JOB --> PG
  JOB --> CH
  EP -. "runtime realization unknown" .-> TOPO
```

## Known Gaps And Follow-Up

`[Unknown]` Live service count, backend selection, database topology, ownership, and data-loss/consistency SLOs. Close [OI-001](../../open-items.md#oi-001), [OI-002](../../open-items.md#oi-002), and [OI-003](../../open-items.md#oi-003). Product promise validation belongs to Product Value.
