# Architecture Handoff

## Confirmed Navigation

Use the [report](report.md), [inventory](../../controls/architecture/adr-candidate-inventory.md), [ADR register](../../controls/architecture/adr-register.md), and [component](../../controls/architecture/diagrams/component-and-data-authority-view.md), [ingestion](../../controls/architecture/diagrams/event-ingestion-and-durability-boundary.md), and [deployment](../../controls/architecture/diagrams/deployment-and-runtime-path.md) views.

## Constraints And Conflicts

No material source conflict was found. Do not assume `master` is deployed, HTTP 202 proves durability, CE source proves hosted architecture, or source topology proves live controls/capacity/recovery.

## Material Unknowns

Routes: deployment [OI-001](../../controls/open-items.md#oi-001); tolerance [OI-002](../../controls/open-items.md#oi-002); failure behavior [OI-003](../../controls/open-items.md#oi-003); migration/recovery [OI-004](../../controls/open-items.md#oi-004).

## Downstream Use

Reviewers may use linked source evidence for tracker/Phoenix, PostgreSQL/ClickHouse, buffering, Oban, runtime configuration, image build, and migrations—not live state.
