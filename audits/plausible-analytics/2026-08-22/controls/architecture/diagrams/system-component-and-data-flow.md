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

Read the panels from top to bottom. Repeated application or state nodes refer
to the same source-visible boundary.

### Panel 1 — Client Entry And Application Routing

```mermaid
flowchart TB
  subgraph ENTRY["Confirmed clients and contracts"]
    T["Compiled tracker variants"] --> EV["POST /api/event"]
    UI["Dashboard TypeScript"] --> IQ["Internal stats query contexts"]
    PA["Public API clients"] --> PQ["Public API contexts"]
  end

  EP["Phoenix endpoint/router"]
  ING["Request validation and enrichment"]
  Q["Stats/query contexts"]
  AUTH["Auth, teams, billing, settings"]
  TOPO["Cloud nodes, replicas, routing, ownership\nUNKNOWN"]

  EV --> EP
  IQ --> EP
  PQ --> EP
  EP --> ING
  EP --> Q
  EP --> AUTH
  EP -. "runtime realization unknown" .-> TOPO
```

### Panel 2 — Event Persistence And Remote Boundary

```mermaid
flowchart TB
  ING["Request validation and enrichment\n(same application boundary)"]
  PER["Pluggable persistor"]
  SC["ETS/session cache"]
  BUF["Local event/session write buffers"]
  CH["ClickHouse: events, sessions, imports, counters"]
  RP["Remote persistence service deployment\nUNKNOWN"]

  ING --> PER
  PER --> SC
  PER --> BUF
  BUF --> CH
  PER -. "remote backend path; deployment unknown" .-> RP
  RP -. "remote ClickHouse write path unknown" .-> CH
```

### Panel 3 — Query, Account, And Background State

```mermaid
flowchart TB
  Q["Stats/query contexts\n(same application boundary)"]
  AUTH["Auth, teams, billing, settings\n(same application boundary)"]
  JOB["Oban workers and cron"]
  PG["PostgreSQL: relational state + Oban"]
  CH["ClickHouse: events, sessions, imports, counters\n(same state boundary)"]

  Q --> CH
  Q --> PG
  AUTH --> PG
  JOB --> PG
  JOB --> CH
```

## Known Gaps And Follow-Up

`[Unknown]` Live service count, backend selection, database topology, ownership, and data-loss/consistency SLOs. Close [OI-001](../../open-items.md#oi-001), [OI-002](../../open-items.md#oi-002), and [OI-003](../../open-items.md#oi-003). Product promise validation belongs to Product Value.
