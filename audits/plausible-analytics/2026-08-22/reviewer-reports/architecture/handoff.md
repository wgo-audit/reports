# Architecture Handoff

## Confirmed Navigation

Use the [report](report.md), [decision inventory](../../controls/architecture/adr-candidate-inventory.md), [ADR register](../../controls/architecture/adr-register.md), and three linked diagrams. Direct evidence is [E-001–E-012](../../evidence/evidence-ledger.md).

## Constraints And Conflicts

Source is pinned to `9cc669b`; CodeGraph omits Elixir, which was inspected directly. `202` acceptance is not ClickHouse durability; image-build notifications are not deployment proof; monitoring configuration is not operation.

## Material Unknowns

Live persistor/config, deletion convergence, promotion/migration/rollback, topology, decision authority, and supported CE/tracker matrix remain [OI-001–OI-005](../../controls/open-items.md).

## Downstream Use

Code Quality, Product Value, and Security/Privacy may use source topology and observed decisions. Do not assume live state, ownership, approval, data correctness, customer acceptance, or compliance.
