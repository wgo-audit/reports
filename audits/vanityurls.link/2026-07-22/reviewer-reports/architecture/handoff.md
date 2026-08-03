# Architecture Handoff

## Confirmed Navigation

[ADR register](../../controls/architecture/adr-register.md), [repository boundary](../../controls/architecture/diagrams/cross-repository-control-boundary.md), and [build/request path](../../controls/architecture/diagrams/build-deploy-request-path.md) map the portable Git-backed Worker design and its four-repository split.

## Constraints And Conflicts

Terraform and repository rules are intended controls, not verified live state. No build, deployment, request, plan/apply, or authenticated setting was observed.

## Material Unknowns

GitHub/Cloudflare/registrar ownership, signer recovery, Terraform state, deployment connections, alerting, capacity, cost, and recovery effectiveness remain unknown.

## Downstream Use

Product Value may use implemented flows. Security, Scalability, Continuity, and Cost may use boundaries. Do not assume source presence proves deployment, control effectiveness, transferability, or recoverability.
