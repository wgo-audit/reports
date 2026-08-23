# Architecture Handoff

## Confirmed Navigation

Architecture is `completed-with-open-verification`. Use the [report](report.md),
[E-001..E-008](../../evidence/evidence-ledger.md), [ADR register](../../controls/architecture/adr-register.md),
and [alert path](../../controls/architecture/diagrams/heartbeat-to-human-alert-path.md).

## Constraints And Conflicts

The pinned source is a database-mediated Django application; its reference
Docker runtime co-locates web and workers. No material source/document conflict
was found. Source is not live-state proof.

## Material Unknowns

Do not assume Acme deploys the sample, tests ran, team readiness, hosted-runtime
equivalence, recovery, or five-minute delivery. OI-005 selects topology; OI-006
requires T1−T0 ≤300 seconds without silent loss; OI-007 closes recovery.

## Downstream Use

Code Quality, Product Value, and Security and Privacy may use cited behavior.
Pull remains plausible; make needs measured source-level necessity; buy needs
OI-004 and equivalent timing evidence.
