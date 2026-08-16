# ADR-001: Modular Monolith And UI Boundary

- Status: observed
- Evidence cutoff: 2026-08-06

## Decision Statement

The inspected Community release implements authenticated administration, public signing, JSON API, MCP, and embed placeholders in one Rails application/route set. Server-rendered ERB and Turbo host Vue/custom-element islands for the builder and signing form.

## Observed Position, Rationale, And Approval

| Dimension | Position | Evidence | Limitation |
|---|---|---|---|
| Implementation | One Rails application with domain modules and mixed server/client UI | [Component packet §1–2](../../../evidence/packets/architecture-component-api-ui-contracts.md) | Source topology only |
| Runtime/live state | unknown | No approved live evidence | Process count, ownership and isolation unobserved |
| Rationale | unknown | No source-backed decision rationale found | Framework presence is not rationale |
| Approval | unknown | No organization architecture decision supplied | Observation is not target acceptance |

## Constraints, Options, And Tradeoffs

The boundary simplifies local deployment and synchronous domain access, but shares a code/release surface across administrative UI, signer traffic and integrations; scaling and failure coupling depends on the deployed process topology. Target options are to accept the monolith behind organization controls, isolate selected processes while retaining the codebase, or place organization-owned adapters around it.

## Impacts And Boundaries

Downstream security, continuity, scalability and maintenance work must treat the topology as shared source, not proof of a single live process. See the [component diagram](../diagrams/component-contract-boundaries.md).

## Change, Reversal, And Follow-Up

OI-003 must define the deployed process/network boundary, ownership, health model and scaling isolation before production approval. Revisit this record if Pro extensions or an organization adapter materially change the component graph.
