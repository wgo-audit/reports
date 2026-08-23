# Application Security Handoff

## Confirmed Navigation

Use the [report](report.md) and [attack-path/control view](../../controls/application-security/attack-path-and-control-view.md), with E-031–E-034.

## Constraints And Conflicts

Source shows layered session/API/site/team controls. It also shows client-reachable ingestion header semantics, unredacted Sentry context, and weak optional credential acceptance. No live bypass, exploitation, hosted effectiveness, dependency vulnerability, or penetration-test coverage was established.

## Material Unknowns

Edge/replay trust [OI-011](../../controls/open-items.md#oi-011); OAuth diagnostics [OI-010](../../controls/open-items.md#oi-010); visitor diagnostics [OI-012](../../controls/open-items.md#oi-012); alternate credentials [OI-013](../../controls/open-items.md#oi-013). Preserve OI-002/OI-007 unanswered and OI-008 as governance.

## Downstream Use

Cloud Security validates effective ingress/header/IAM/runtime controls. Maintenance Cost includes correction and recurring negative checks. Do not transfer EE replay behavior to CE Run or source controls to hosted/live proof.
